AI web scraper: Intelligent Web Data Extraction for LLMs
Rufus is an AI-powered tool designed to intelligently crawl websites, extract relevant information based on user-defined prompts, and synthesize the data into structured documents. This tool is specifically built to provide useful data for Retrieval-Augmented Generation (RAG) systems, enabling LLMs to retrieve real-time, relevant content from the web.

Approach
Problem Breakdown
The key challenge was to build a system that could:

Crawl complex web structures: Handle both simple pages and deeper nested or dynamically loaded content.
Extract relevant data based on user prompts: Use AI-driven methods to ensure only the necessary data is retrieved.
Synthesize structured documents: Convert raw content into structured formats that can be easily plugged into RAG systems.
Core Components
1. Web Crawler
Rufus utilizes BeautifulSoup for HTML parsing and link extraction. The web crawler intelligently follows links and scrapes pages recursively, managing nested pages and handling dynamically loaded content.

Dynamic Crawling: The crawler focuses on pages that are contextually important based on the prompt, extracting only useful content while skipping irrelevant pages.
2. Data Extractor
The extractor module is responsible for processing the raw content scraped by the crawler and synthesizing it into structured formats, such as JSON or CSV. It utilizes:

Pandas: To structure and organize data into rows and columns for easier integration.
LangChain: To handle dynamic prompts and filter data based on the user’s specific query.
3. Semantic Search
The semantic search component is powered by FIAS, which ensures that Rufus doesn’t just look for keywords but understands the context of the user’s prompt. It applies AI-driven search techniques to provide the most relevant information.

4. Error Handling
Rufus has robust error handling in place. This includes:

Retry logic for failed web requests.
Handling page access restrictions (e.g., 404 or 403 errors).
Dealing with websites that change structure dynamically (e.g., JavaScript-loaded content).
Key Features
Prompt-Based Crawling: Rufus can crawl websites intelligently based on user input, focusing on relevant sections such as FAQs, pricing pages, or product descriptions.
AI-Powered Data Extraction: With semantic search, Rufus ensures only relevant data is extracted and synthesized.
Structured Output: The final output is a structured document (JSON), which can be directly integrated into RAG pipelines for downstream LLM applications.
Installation
Clone the repository:
bash
Copy code
git clone :
cd web_scraper
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Here’s a basic usage example to see Rufus in action:

python
Copy code
from Rufus import RufusClient

client = RufusClient()
instructions = "Find information about product features and customer FAQs."
documents = client.scrape("https://example.com")
print(documents)
Example Task
You can use Rufus to scrape public websites. For example, given a prompt:

python
Copy code
instructions = "We're making a chatbot for the HR department in San Francisco."
documents = client.scrape("https://www.sfgov.com")
WebScraper will crawl the given URL, extract relevant content (e.g., application forms, FAQs), and return structured data in JSON format.

API Overview
The API is designed to be simple and intuitive. Here’s a brief overview:

Initialization:
python
Copy code
client = RufusClient()
Scraping a website:
python
Copy code
documents = client.scrape(url, instructions)
url: The URL of the website to be scraped.
instructions: A user-defined prompt that guides Rufus on what content to extract.
Output:
The scrape function returns the extracted content as a structured JSON document, ready for use in LLM pipelines.

Error Handling
Rufus includes robust error handling. In case of an error (e.g., inaccessible pages, website structure changes), Rufus will either retry the request or skip the page and continue with the crawl.