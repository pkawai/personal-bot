---
name: forex-rates
description: Use this skill when the user asks about exchange rates, currency rates, forex rates, "what's EUR/USD", "convert USD to MNT", "currency conversion", or asks how much a currency is worth. Trigger on any message mentioning exchange rates, forex, or currency pairs.
version: 1.0.0
---

# Forex Rates Skill

Fetch and display live foreign exchange rates using the free Open Exchange Rates API (no key required).

## When to Use

Activate when the user asks about:
- Currency exchange rates (e.g. "what's EUR/USD?", "USD to MNT rate")
- Forex rates or FX rates
- Converting one currency to another
- A list of major currency rates

## Core Workflow

1. Identify the **base currency** and **target currencies** from the user's message. Default base: USD. Default targets: EUR, MNT, GBP, JPY, CNY if not specified.

2. Fetch live rates using WebFetch:
   - URL: `https://open.er-api.com/v6/latest/{BASE_CURRENCY}` (replace `{BASE_CURRENCY}` with the actual base, e.g. `USD`)
   - Extract the `rates` object and `time_last_update_utc` field

3. If the user asks about a **specific pair** (e.g. EUR/USD):
   - Show just that rate with timestamp
   - Include the inverse rate (e.g. 1 EUR = X USD)

4. If the user asks for **general rates** or a list:
   - Show a formatted table with the most useful currencies: USD, EUR, MNT, GBP, JPY, CNY, KRW, CNH
   - Include the timestamp of when rates were last updated

5. Format the response clearly:
   ```
   Exchange Rates (base: USD)
   Updated: [timestamp]

   EUR  0.9234
   MNT  3,450.00
   GBP  0.7891
   JPY  149.32
   CNY  7.24
   ```

6. If the API call fails, inform the user that live rates are temporarily unavailable and suggest checking xe.com.

## Notes

- The API at `https://open.er-api.com/v6/latest/USD` is free with no API key required
- Rates update approximately every hour
- MNT (Mongolian Tugrik) is always included since this bot is used in Mongolia
- For conversion calculations: `amount × rate = converted amount`
