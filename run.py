from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json, sanitize_url_for_filename, keyword_search
from monitor_utils.check import save_entry_if_new, get_all_entries
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
    entries = fetch_rss_feed(url, limit=1)
    if not entries:
        print("[!] No entries found.")
        return

    entry = parse_articles(entries)[0]
    site = sanitize_url_for_filename(url)
    save_to_json([entry], f"output/rss/{site}")

    if save_entry_if_new(entry, table):
        print(f"[+] New entry saved for {table}")
    else:
        print(f"[-] No new entry for {table}")

    # 🧠 Semantic search comparison
    prompt = "electronics import disruptions"

    # Get the text to search in (title and summary)
    search_text = f"{entry['title']} {entry['summary']}"

    # Load existing entries from database for comparison
    existing_entries = get_all_entries(table)

    if existing_entries:
        # Extract text from existing entries for comparison
        existing_texts = []
        for existing_entry in existing_entries:
            existing_text = f"{existing_entry.get('title', '')} {existing_entry.get('summary', '')}"
            existing_texts.append(existing_text)

        # Perform semantic search
        semantic_results = get_semantic_search_results(prompt, existing_texts, threshold=0.1, top_k=3)

        # Perform keyword search
        keyword_results = keyword_search(prompt, existing_texts)

        print(f"\n🔍 Search results for '{prompt}':")

        print("\n🧠 Semantic Matches:")
        if semantic_results:
            for i, (doc, score) in enumerate(semantic_results, 1):
                # Truncate document text for display
                display_text = doc[:100] + "..." if len(doc) > 100 else doc
                print(f"  {i}. ({score:.2f}) {display_text}")
        else:
            print("  No significant semantic matches found.")

        print("\n🔤 Keyword Matches:")
        if keyword_results:
            for i, doc in enumerate(keyword_results, 1):
                # Truncate document text for display
                display_text = doc[:100] + "..." if len(doc) > 100 else doc
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

