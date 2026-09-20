from __future__ import annotations

from typing import Any

from .meta_api import get_ad_account_id, get_json, paginate


INSIGHT_FIELDS = [
    "ad_id","ad_name","campaign_name","adset_name","spend","impressions",
    "reach","clicks","ctr","cpc","cpm","actions","action_values",
]


def _action_value(rows: list[dict[str, Any]] | None, action_type: str) -> float:
    for row in rows or []:
        if row.get("action_type") == action_type:
            try:
                return float(row.get("value", 0))
            except (TypeError, ValueError):
                return 0.0
    return 0.0


def pull_ad_insights(date_preset: str = "last_30d") -> list[dict[str, Any]]:
    rows = paginate(
        f"{get_ad_account_id()}/insights",
        {
            "level": "ad",
            "fields": ",".join(INSIGHT_FIELDS),
            "date_preset": date_preset,
            "limit": 100,
        },
    )
    output = []
    for row in rows:
        spend = float(row.get("spend", 0) or 0)
        revenue = _action_value(row.get("action_values"), "purchase")
        purchases = _action_value(row.get("actions"), "purchase")
        output.append({
            "ad_id": row.get("ad_id"),
            "ad_name": row.get("ad_name"),
            "campaign_name": row.get("campaign_name"),
            "adset_name": row.get("adset_name"),
            "spend": spend,
            "impressions": int(row.get("impressions", 0) or 0),
            "reach": int(row.get("reach", 0) or 0),
            "clicks": int(row.get("clicks", 0) or 0),
            "ctr": float(row.get("ctr", 0) or 0),
            "cpc": float(row.get("cpc", 0) or 0),
            "cpm": float(row.get("cpm", 0) or 0),
            "purchases": purchases,
            "revenue": revenue,
            "roas": (revenue / spend) if spend else 0,
        })
    return output


def fetch_creative_copy(ad_id: str) -> dict[str, list[str]]:
    data = get_json(ad_id, {"fields": "creative{id,name,title,body,object_story_spec,asset_feed_spec}"})
    creative = data.get("creative", {}) or {}
    afs = creative.get("asset_feed_spec") or {}
    bodies = [x.get("text","") for x in afs.get("bodies",[]) if x.get("text")]
    titles = [x.get("text","") for x in afs.get("titles",[]) if x.get("text")]
    descriptions = [x.get("text","") for x in afs.get("descriptions",[]) if x.get("text")]
    story = creative.get("object_story_spec") or {}
    link = story.get("link_data") or {}
    video = story.get("video_data") or {}
    if not bodies:
        value = creative.get("body") or link.get("message") or video.get("message")
        if value:
            bodies = [value]
    if not titles:
        value = creative.get("title") or link.get("name")
        if value:
            titles = [value]
    return {"bodies": bodies, "titles": titles, "descriptions": descriptions}


def rank_ads(date_preset: str = "last_30d", min_spend: float = 0, sort_by: str = "roas") -> list[dict[str, Any]]:
    rows = [x for x in pull_ad_insights(date_preset) if x["spend"] >= min_spend]
    for row in rows:
        row["copy"] = fetch_creative_copy(str(row["ad_id"])) if row.get("ad_id") else {}
    rows.sort(key=lambda x: x.get(sort_by, 0), reverse=True)
    return rows
