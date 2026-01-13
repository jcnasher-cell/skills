---
name: firecrawl
description: Web scraping and crawling using Firecrawl API. Use when the user wants to scrape a webpage, crawl a website, extract structured data from URLs, discover all URLs on a site, or get content in markdown format.
---

# Firecrawl Web Scraping Skill

This skill enables web scraping, crawling, and structured data extraction using the Firecrawl API.

## Capabilities

1. **Scrape**: Extract content from a single URL (markdown, HTML, links, metadata)
2. **Crawl**: Crawl an entire website and extract content from multiple pages
3. **Map**: Discover all URLs on a website
4. **Extract**: Extract structured data using AI

## API Key

The API key is stored in the environment variable `FIRECRAWL_API_KEY`.

## Usage Examples

### Scrape a Single Page

```python
import requests
import os

url = "https://api.firecrawl.dev/v1/scrape"
headers = {
    "Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}",
    "Content-Type": "application/json"
}
data = {
    "url": "https://example.com",
    "formats": ["markdown", "html"]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result["data"]["markdown"])
```

### Crawl a Website

```python
import requests
import os

url = "https://api.firecrawl.dev/v1/crawl"
headers = {
    "Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}",
    "Content-Type": "application/json"
}
data = {
    "url": "https://example.com",
    "limit": 10,  # Max pages to crawl
    "scrapeOptions": {
        "formats": ["markdown"]
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
# Returns a job ID for async crawling
print(result["id"])
```

### Check Crawl Status

```python
import requests
import os

job_id = "your-job-id"
url = f"https://api.firecrawl.dev/v1/crawl/{job_id}"
headers = {
    "Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}"
}

response = requests.get(url, headers=headers)
result = response.json()
print(result["status"])  # "scraping", "completed", "failed"
print(result["data"])    # Array of scraped pages when complete
```

### Map a Website (Discover URLs)

```python
import requests
import os

url = "https://api.firecrawl.dev/v1/map"
headers = {
    "Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}",
    "Content-Type": "application/json"
}
data = {
    "url": "https://example.com"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result["links"])  # List of all discovered URLs
```

### Extract Structured Data

```python
import requests
import os

url = "https://api.firecrawl.dev/v1/scrape"
headers = {
    "Authorization": f"Bearer {os.environ['FIRECRAWL_API_KEY']}",
    "Content-Type": "application/json"
}
data = {
    "url": "https://example.com/product",
    "formats": ["extract"],
    "extract": {
        "schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "price": {"type": "string"},
                "description": {"type": "string"}
            }
        }
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result["data"]["extract"])
```

## Scrape Options

When scraping, you can specify:

- **formats**: `["markdown", "html", "rawHtml", "links", "screenshot", "extract"]`
- **onlyMainContent**: `true` to exclude headers, footers, navigation
- **includeTags**: CSS selectors to include
- **excludeTags**: CSS selectors to exclude
- **waitFor**: Milliseconds to wait for dynamic content

## Best Practices

1. **Start with scrape** for single pages, use crawl for multiple pages
2. **Use map first** to discover URLs before crawling
3. **Set reasonable limits** on crawl to avoid excessive API usage
4. **Use onlyMainContent: true** to get cleaner results
5. **Check crawl status** periodically for async jobs

## Error Handling

Always check for errors in the response:

```python
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.json())
```

## Rate Limits

Firecrawl has rate limits based on your plan. Handle 429 errors with exponential backoff.