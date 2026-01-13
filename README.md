# Claude Code Skills

A collection of custom skills for Claude Code, providing specialized capabilities for web scraping, meeting intelligence, strategic briefing, and application development.

## Skills

| Skill | Description |
|-------|-------------|
| [Firecrawl](firecrawl/) | Web scraping and crawling using the Firecrawl API |
| [Fireflies Meeting Intelligence](fireflies-meeting-intelligence/) | Access and analyze Fireflies.ai meeting transcripts |
| [Strategic Daily Brief Writer](strategic-daily-brief-writer/) | Generate Strategic Daily Briefs for construction leadership |
| [Firebase + React App Development](SKILL-firebase-react-app-development.md) | Best practices and lessons learned for Firebase + React apps |

## Skill Details

### Firecrawl

Web scraping, crawling, and structured data extraction capabilities:

- **Scrape**: Extract content from a single URL (markdown, HTML, links, metadata)
- **Crawl**: Crawl entire websites and extract content from multiple pages
- **Map**: Discover all URLs on a website
- **Extract**: Extract structured data using AI

**Trigger**: Use when asked to scrape, crawl, or extract data from websites.

---

### Fireflies Meeting Intelligence

Access and analyze meeting transcripts from Fireflies.ai:

- Search transcripts by keyword, participant, or date range
- Retrieve full meeting transcripts with timestamps
- Extract action items and decisions
- Track topics across multiple meetings
- Generate meeting summaries and follow-up tasks

**Trigger**: Use when asked about meetings, transcripts, action items, or discussions.

---

### Strategic Daily Brief Writer

Assist construction leadership in producing Strategic Daily Briefs (SDBs):

- Extract material construction/commercial events from data sources
- Synthesize information into decision-useful briefs
- Apply construction delivery and commercial lens to analysis
- Follow UK construction standards and Columbia Group format

**Trigger**: Use when asked to create daily briefs or summarize construction/commercial events.

---

### Firebase + React App Development

Comprehensive guide covering lessons learned from building applications:

- Firebase Auth (magic links, password flow, session management)
- Firestore patterns (data modeling, security rules, sync handling)
- React contexts and state management
- Role-based permission systems
- Deployment workflows and debugging strategies

**Purpose**: Reference guide for building Firebase + React applications.

## Usage

These skills are automatically available in Claude Code when installed in the `.claude/skills` directory. Skills are triggered based on context and user requests.

## Installation

Clone this repository to your Claude Code skills directory:

```bash
git clone https://github.com/jcnasher-cell/skills.git ~/.claude/skills
```

Or copy individual skill folders as needed.
