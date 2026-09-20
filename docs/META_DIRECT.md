# Direct Meta Marketing API Integration

This integration follows the same direct-to-Meta pattern used by the reference repository `krusemediallc/arcads-claude-code`.

## Required runtime secrets
Store these in `.env`; never commit them:

- `META_ACCESS_TOKEN`
- `META_AD_ACCOUNT_ID`
- optional: `META_PAGE_ID`, `META_IG_USER_ID`, `META_PIXEL_ID`
- optional: `META_API_VERSION`

For ReadyToGrow.biz the known ad account is:

`1064978189784735`

Use `act_1064978189784735` for account endpoints.

## What v1 can do
- validate the token + selected ad account
- pull ad-level spend/performance
- extract creative copy
- rank observed ads by ROAS or spend
- summarize account performance
- create ads in PAUSED state through the shared Meta helper

## Guardrail
Creation defaults to PAUSED. A human should review the target ad set, destination URL, creative, and budget before any live spend is enabled.

## Next setup step
Create/authorize a Meta developer app and obtain a long-lived token with the permissions needed for ad reading/management. Put the token in the local `.env`; do not paste it into chat.
