from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json, sanitize_url_for_filename, keyword_search
from monitor_utils.check import save_entry_if_new, get_all_entries
from monitor_utils.scraper import scrape_multiple_articles
import sys
import os

#Add path to semantic search project
semantic_path = os.path.abspath("../overworked_intern")
sys.path.append(semantic_path)

from keyword_extractor import extract_keywords, get_embeddings
from prompt_interpreter import PromptInterpreter
from matcher import Matcher


def get_semantic_search_results(query, documents, threshold=0.3, top_k=5):
    """
    Perform semantic search on documents using the query.

    Args:
        query: The search query string
        documents: List of document strings to search through
        threshold: Minimum similarity threshold (0.0 to 1.0)
        top_k: Maximum number of results to return

    Returns:
        List of tuples (document, similarity_score) sorted by score
    """
    if not documents:
        return []

    interpreter = PromptInterpreter()
    matcher = Matcher()

    # Convert query to vector
    query_vector = interpreter.to_vector(query)

    # Find matches
    results = matcher.top_matches(query_vector, documents, threshold=threshold, top_k=top_k)

    return results


table = "federal_registry"
site = table


def get_last_rss_entry(url):
    entries = fetch_rss_feed(url, limit=20)
    if not entries:
        print("[!] No entries found.")
        return

    parsed_entries = parse_articles(entries)
    site = sanitize_url_for_filename(url)
    save_to_json(parsed_entries, f"output/rss/{site}")

    # 🕷️ Web scraping for deeper content (scrape first 5 articles)
    print("\n🕷️ Scraping full article content...")
    scraped_articles = scrape_multiple_articles(entries, max_articles=5, delay=2)

    # Merge scraped content with parsed entries
    for i, scraped in enumerate(scraped_articles):
        if i < len(parsed_entries) and scraped.get('content'):
            parsed_entries[i]['full_content'] = scraped['content']
            parsed_entries[i]['scraped_summary'] = scraped.get('summary', '')
            parsed_entries[i]['metadata'] = scraped.get('metadata', {})

    # Process each entry
    new_entries_count = 0
    for entry in parsed_entries:
        if save_entry_if_new(entry, table):
            new_entries_count += 1
            print(f"[+] New entry saved: {entry['title'][:50]}...")

    if new_entries_count > 0:
        print(f"[+] Total new entries saved: {new_entries_count}")
    else:
        print(f"[-] No new entries for {table}")

    # 🧠 Enhanced semantic search with full content
    if parsed_entries:
        latest_entry = parsed_entries[0]
        prompt = "imports trade regulations"

        # Load existing entries from database for comparison
        existing_entries = get_all_entries(table)

        if existing_entries:
            # Extract text from existing entries for comparison (now including full content)
            existing_texts = []
            for existing_entry in existing_entries:
                # Combine title, summary, and full content for richer search
                search_text = f"{existing_entry.get('title', '')} {existing_entry.get('summary', '')}"
                if existing_entry.get('full_content'):
                    # Use first 2000 chars of full content to avoid overwhelming the search
                    search_text += f" {existing_entry.get('full_content', '')[:2000]}"
                existing_texts.append(search_text)

            # Perform semantic search
            semantic_results = get_semantic_search_results(prompt, existing_texts, threshold=0.3, top_k=5)

            # Perform keyword search
            keyword_results = keyword_search(prompt, existing_texts)

            print(f"\n🔍 Enhanced search results for '{prompt}' (using full content):")

            print("\n🧠 Semantic Matches:")
            if semantic_results:
                for i, (doc, score) in enumerate(semantic_results, 1):
                    # Truncate document text for display
                    display_text = doc[:150] + "..." if len(doc) > 150 else doc
                    print(f"  {i}. ({score:.2f}) {display_text}")
            else:
                print("  No significant semantic matches found.")

            print("\n🔤 Keyword Matches:")
            if keyword_results:
                for i, doc in enumerate(keyword_results, 1):
                    # Truncate document text for display
                    display_text = doc[:150] + "..." if len(doc) > 150 else doc
                    print(f"  {i}. {display_text}")
            else:
                print("  No keyword matches found.")
        else:
            print("  No existing entries to compare against.")

def run():
    rss_sources = [
        "https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest"
        # Add more RSS URLs as needed
    ]
    for url in rss_sources:
        get_last_rss_entry(url)

if __name__ == "__main__":
    run()

