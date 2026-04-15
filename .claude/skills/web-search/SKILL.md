---
name: web-search
description: Use this skill when the user asks to search for something, "look up", "find information about", "research", "what is", "tell me about", "summarize", or wants to know about any topic that requires current or factual information from the web.
version: 1.0.0
---

# Web Search Skill

Search the web for any topic and return a concise, well-structured summary with key findings and source links.

## When to Use

Activate when the user:
- Says "search for X", "look up X", "find info about X"
- Asks "what is X?" or "tell me about X" where X requires current information
- Asks for news, recent events, or facts about any topic
- Uses words like "research", "summarize", "find out"

## Core Workflow

1. **Extract the search query** from the user's message. Clean it up into a clear, specific search query.

2. **Search the web** using the WebSearch tool with the extracted query.

3. **Analyze the results** — read the top 3-5 results for relevance and accuracy.

4. **Summarize clearly** using this structure:

   ```
   🔍 Search: [query]

   **Summary**
   [2-3 sentence overview of what was found]

   **Key Points**
   • [point 1]
   • [point 2]
   • [point 3]

   **Sources**
   • [Title](URL)
   • [Title](URL)
   ```

5. Keep the summary **concise** — aim for under 200 words total. The user is reading on Telegram.

6. If the search returns no useful results, say so and offer to refine the query.

## Notes

- Prioritize recent, authoritative sources (news sites, official docs, Wikipedia)
- If the topic is ambiguous, ask the user to clarify before searching
- Do not fabricate information — only report what the search results say
- For technical topics (code, APIs), include a code snippet if relevant
