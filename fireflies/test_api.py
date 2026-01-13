#!/usr/bin/env python3
"""
Fireflies API Test Script
Tests connection and lists recent meeting transcripts
"""

import json

# Note: This script requires 'requests' library
# Install: pip install requests

try:
    import requests
except ImportError:
    print("ERROR: requests library not found")
    print("Install with: pip install requests")
    exit(1)

# Configuration
API_KEY = "263eb9e6-5d37-488d-b6b3-0f62083a45f6"
ENDPOINT = "https://api.fireflies.ai/graphql"

def test_connection():
    """Test basic API connectivity"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    query = """
    {
      transcripts(limit: 10) {
        id
        title
        date
        duration
        organizer_email
        participants
      }
    }
    """
    
    try:
        print("Testing Fireflies API Connection...")
        print("=" * 70)
        
        response = requests.post(
            ENDPOINT,
            headers=headers,
            json={"query": query},
            timeout=15
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if 'errors' in data:
                print("\nAPI ERRORS:")
                for error in data['errors']:
                    print(f"  - {error.get('message', 'Unknown error')}")
                return False
            
            if 'data' in data and 'transcripts' in data['data']:
                transcripts = data['data']['transcripts']
                print(f"\nSUCCESS! Found {len(transcripts)} meeting transcripts\n")
                
                for i, transcript in enumerate(transcripts, 1):
                    print(f"{i}. {transcript.get('title', 'Untitled Meeting')}")
                    print(f"   Date: {transcript.get('date', 'Unknown')}")
                    print(f"   Duration: {transcript.get('duration', 0)} seconds")
                    print(f"   Organizer: {transcript.get('organizer_email', 'Unknown')}")
                    print(f"   Participants: {len(transcript.get('participants', []))}")
                    print(f"   ID: {transcript.get('id')}")
                    print()
                
                return True
            else:
                print("\nUnexpected response structure:")
                print(json.dumps(data, indent=2))
                return False
        else:
            print(f"\nHTTP Error: {response.status_code}")
            print(response.text[:500])
            return False
            
    except requests.exceptions.Timeout:
        print("\nERROR: Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        print("\nERROR: Connection failed - check internet connectivity")
        return False
    except Exception as e:
        print(f"\nERROR: {type(e).__name__}: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_connection()
    exit(0 if success else 1)
