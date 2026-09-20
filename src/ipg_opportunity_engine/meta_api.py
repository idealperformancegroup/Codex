from __future__ import annotations

import json
import os
import time
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_VERSION = os.getenv("META_API_VERSION", "v23.0")
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def get_access_token() -> str:
    token = os.getenv("META_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("META_ACCESS_TOKEN is not configured")
    return token


def get_ad_account_id() -> str:
    account = os.getenv("META_AD_ACCOUNT_ID")
    if not account:
        raise RuntimeError("META_AD_ACCOUNT_ID is not configured")
    return account if account.startswith("act_") else f"act_{account}"


def get_json(path: str, params: dict[str, Any] | None = None, timeout: int = 60) -> dict[str, Any]:
    params = dict(params or {})
    params["access_token"] = get_access_token()
    response = requests.get(f"{BASE_URL}/{path.lstrip('/')}", params=params, timeout=timeout)
    data = response.json()
    if response.status_code >= 400 or "error" in data:
        raise RuntimeError(json.dumps(data.get("error", data)))
    return data


def post_form(path: str, data: dict[str, Any], timeout: int = 120) -> dict[str, Any]:
    payload = dict(data)
    payload["access_token"] = get_access_token()
    response = requests.post(f"{BASE_URL}/{path.lstrip('/')}", data=payload, timeout=timeout)
    result = response.json()
    if response.status_code >= 400 or "error" in result:
        raise RuntimeError(json.dumps(result.get("error", result)))
    return result


def validate_connection() -> dict[str, Any]:
    me = get_json("me", {"fields": "id,name"})
    account = get_json(get_ad_account_id(), {"fields": "account_id,name,currency,timezone_name,account_status"})
    return {"user": me, "ad_account": account}


def paginate(path: str, params: dict[str, Any]) -> list[dict[str, Any]]:
    url = f"{BASE_URL}/{path.lstrip('/')}"
    payload = dict(params)
    payload["access_token"] = get_access_token()
    rows: list[dict[str, Any]] = []
    while url:
        response = requests.get(url, params=payload, timeout=60)
        data = response.json()
        if response.status_code >= 400 or "error" in data:
            raise RuntimeError(json.dumps(data.get("error", data)))
        rows.extend(data.get("data", []))
        url = data.get("paging", {}).get("next")
        payload = None
    return rows


def create_paused_ad(adset_id: str, name: str, creative: dict[str, Any], pixel_id: str | None = None) -> str:
    payload: dict[str, Any] = {
        "adset_id": adset_id,
        "name": name,
        "status": "PAUSED",
        "creative": json.dumps(creative),
    }
    if pixel_id:
        payload["tracking_specs"] = json.dumps([{
            "action.type": ["offsite_conversion"],
            "fb_pixel": [pixel_id],
        }])
    last_error = None
    for attempt in range(4):
        try:
            return str(post_form(f"{get_ad_account_id()}/ads", payload)["id"])
        except RuntimeError as exc:
            last_error = exc
            if attempt == 3:
                raise
            time.sleep(min(60, 5 * (2 ** attempt)))
    raise RuntimeError(str(last_error))
