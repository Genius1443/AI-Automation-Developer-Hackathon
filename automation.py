# ================================
# 🏆 Prospect Research Agent
# ================================

import requests
from bs4 import BeautifulSoup
import re
import json
import tldextract
import time

# ========= CONFIG =========
API_KEY = ""  # Optional (leave empty if no credits)

headers = {"User-Agent": "Mozilla/5.0"}

# ========= SCRAPER =========
def scrape_page(url):
    try:
        res = requests.get(url, headers=headers, timeout=8)
        if res.status_code == 200:
            return res.text
    except:
        pass
    try:
        return requests.get(url, timeout=10).text
    except:
        return ""

# ========= LINK FILTER =========
def get_relevant_links(base_url):
    html = scrape_page(base_url)
    soup = BeautifulSoup(html, "html.parser")

    links = set()
    keywords = ["about", "contact", "service", "company"]

    for a in soup.find_all("a", href=True):
        href = a["href"].lower()

        if any(k in href for k in keywords):
            if href.startswith("http"):
                links.add(href)
            elif href.startswith("/"):
                links.add(base_url.rstrip("/") + href)

    return [base_url] + list(links)[:4]

# ========= CLEAN TEXT =========
def clean_text(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return " ".join(text.split())[:4000]

# ========= CONTACT EXTRACTION =========
def extract_contacts(text):
    emails = re.findall(r'\S+@\S+', text)
    phones = re.findall(r'\+?\d[\d\-\s]{8,}', text)

    return list(set(emails))[:3], (phones[0] if phones else "N/A")

# ========= RULE-BASED AI FALLBACK =========
def infer_service(text):
    text = text.lower()

    if "crm" in text or "customer" in text:
        return "Customer relationship management software"
    elif "billing" in text or "subscription" in text:
        return "Subscription billing platform"
    elif "api" in text:
        return "API development and collaboration platform"
    elif "cloud" in text:
        return "Cloud-based software solutions"
    else:
        return "Software / Technology Services"

# ========= MAIN FUNCTION =========
def enrich_company(url: str) -> dict:
    try:
        ext = tldextract.extract(url)
        website_name = ext.domain.capitalize()

        links = get_relevant_links(url)

        combined_text = ""

        for link in links:
            html = scrape_page(link)
            text = clean_text(html)
            combined_text += " " + text
            time.sleep(1)

        combined_text = combined_text[:4000]

        emails, phone = extract_contacts(combined_text)

        # 🔥 NO AI → SAFE FALLBACK SYSTEM
        data = {
            "website_name": website_name,
            "company_name": website_name,
            "address": "N/A",
            "mobile_number": phone,
            "mail": emails,
            "core_service": infer_service(combined_text),
            "target_customer": "Businesses and enterprises",
            "probable_pain_point": "Scaling operations efficiently",
            "outreach_opener": f"Hi {website_name} team, I came across your website and would love to explore collaboration opportunities."
        }

        return data

    except Exception as e:
        return {
            "website_name": url,
            "company_name": "",
            "address": "",
            "mobile_number": "",
            "mail": [],
            "core_service": "",
            "target_customer": "",
            "probable_pain_point": "",
            "outreach_opener": ""
        }

# ========= MAIN EXECUTION =========
def main(url):
    """
    Accepts single URL from Streamlit
    Returns Python dict (NOT JSON string)
    """
    try:
        data = enrich_company(url)
        return data
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return {
            "website_name": url,
            "company_name": "",
            "address": "",
            "mobile_number": "",
            "mail": [],
            "core_service": "",
            "target_customer": "",
            "probable_pain_point": "",
            "outreach_opener": ""
        }
