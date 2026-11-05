# The Project: Automated Job Aggregator & Match Analyzer

Building a tool to solve your own real-world problem is the absolute best way to prove to employers that your Python skills are practical and valuable. It shows initiative, problem-solving, and technical ability all at once.

## Target Job Platforms (Philippines)
Based on current Philippine job market data, here are the top 5 platforms to target for this project:
1. **JobStreet (ph.jobstreet.com):** The largest traditional corporate job board in the Philippines.
2. **Indeed (ph.indeed.com):** A massive aggregator that pulls from direct company sites and other boards.
3. **Kalibrr (kalibrr.com):** Highly popular for tech roles, modern startups, and enterprise companies in the PH.
4. **OnlineJobs.ph:** The top destination if you are open to remote, direct-to-foreign-client Python roles.
5. **Bossjob (bossjob.ph):** A fast-growing, chat-first platform that is very popular for mid-to-senior tech and BPO roles.

---

## Project Roadmap

### Phase 1: Data Extraction (Web Scraping)
Your first goal is to get Python to read the job websites and pull down job titles, company names, links, and descriptions.
*   **What you will learn:** HTTP requests, DOM parsing, handling dynamic websites.
*   **Tools to use:**
    *   `requests` and `BeautifulSoup` (for simpler, static sites).
    *   `Playwright` or `Selenium` (Required for sites like Indeed and JobStreet, which use heavy JavaScript and anti-bot protections).
*   **The Task:** Write a script that searches for "Python Junior" or "Python Developer" on Kalibrr and Bossjob, and prints the top 10 results to your terminal.

### Phase 2: Data Cleaning & Storage
Once you have the raw text, you need to organize it so you don't apply to the same job twice.
*   **What you will learn:** Data manipulation, working with APIs.
*   **Tools to use:** `pandas` (for structuring the data) and `gspread` (Google Sheets API).
*   **The Task:** Have your script clean the scraped data, remove duplicates, and automatically append new job postings to a Google Sheet. This becomes your personal CRM for job hunting.

### Phase 3: The "Stand Out" Feature (Keyword Matching)
This is what you will talk about in your interviews. You want your script to tell you if a job is actually a good fit.
*   **What you will learn:** Basic Natural Language Processing (NLP) or AI integration.
*   **Tools to use:** Standard Python string methods, or the `google-genai` SDK.
*   **The Task:** Feed your script your resume. For every new job posting it finds, have it check the job description against your resume and assign a "Match Score" (e.g., 85%). Have it flag jobs that require a specific skill you lack so you know what to study next.

### Phase 4: Automation & Alerts
Make the script run on its own so you wake up to fresh leads.
*   **What you will learn:** Task scheduling, webhooks.
*   **Tools to use:** `schedule` (Python library), GitHub Actions (free cloud hosting), or a Telegram Bot API.
*   **The Task:** Set the script to run every morning at 7:00 AM and send a message to your personal Telegram with the top 3 highest-matching jobs of the day.

---

**Interview Talking Point:**
*"I used Python to build an automated pipeline that scrapes the top 5 Philippine job boards, analyzes the requirements, and matches them to my skills—which is exactly how I found this opening."*
