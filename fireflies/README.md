# Fireflies.ai Meeting Intelligence Skill

## Purpose
Access, search, and analyze meeting transcripts and records from Fireflies.ai for Chris Nash at Columbia Group.

## Capabilities
- Search meeting transcripts by keyword, date, participant
- Retrieve full meeting transcripts with timestamps
- Extract action items and decisions from meetings
- Analyze meeting sentiment and key topics
- Get meeting summaries and highlights
- Search across all accessible meetings
- Filter by date range, participants, or meeting type

## When to Use This Skill
- "Find meetings about [topic]"
- "Get transcript from [meeting/date]"
- "What action items came from [meeting]?"
- "Search my Fireflies meetings for [keyword]"
- "Summarize last week's meetings"
- "What decisions were made in [meeting]?"

## Authentication
Requires Fireflies.ai API key stored in environment variables:
- FIREFLIES_API_KEY

## API Endpoints Used
- GraphQL API: https://api.fireflies.ai/graphql
- Search transcripts
- Get meeting details
- Extract action items
- Retrieve participants and metadata

## Key Features
1. TRANSCRIPT SEARCH: Find meetings by keywords in transcript content
2. PARTICIPANT SEARCH: Find meetings with specific attendees
3. DATE FILTERING: Search meetings within date ranges
4. ACTION EXTRACTION: Automatically extract action items and decisions
5. TOPIC ANALYSIS: Identify key discussion topics
6. SENTIMENT ANALYSIS: Understand meeting tone and engagement
7. MEETING SUMMARIES: Get AI-generated summaries

## Integration with Columbia Systems
- Cross-reference meeting participants with M365 directory
- Link action items to EspoCRM tasks
- Store meeting notes in SharePoint
- Create follow-up tasks from action items
- Schedule follow-up meetings in Outlook calendar

## Usage Examples

### Search Meetings
```
Search for meetings mentioning "property development" in last 30 days
Find meetings with John Smith from this month
```

### Get Transcript
```
Get full transcript from Board Meeting on November 20
Retrieve yesterday's project sync meeting transcript
```

### Extract Intelligence
```
What action items came from last week's leadership meeting?
List all decisions made in Q3 board meetings
Summarize key discussion points from Formation Homes meetings
```

## Output Formats
- TRANSCRIPT: Full text with speaker labels and timestamps
- SUMMARY: Key points, decisions, action items
- ACTION ITEMS: Extracted tasks with owners and deadlines
- SEARCH RESULTS: Meeting list with relevance scores

## Performance Notes
- Transcript retrieval: ~2-5 seconds
- Search queries: ~1-3 seconds
- Large date range searches may take longer
- Supports pagination for large result sets

## Privacy & Compliance
- Only accesses meetings Chris Nash has permission to view
- Respects Fireflies.ai sharing settings
- No transcript modification (read-only)
- All data remains in Fireflies.ai system

## Skill Metadata
- Skill Type: Meeting Intelligence
- Domain: Communications & Collaboration
- Complexity: Medium
- Prerequisites: Fireflies.ai API access
- Version: 1.0
- Created: 2025-11-24
- Author: Columbia Expert System
