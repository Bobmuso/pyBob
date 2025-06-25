import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.parse

def get_jobs(searchedJob):
    """Scrape jobs from CareerJunction"""
    url = f"https://www.careerjunction.co.za/jobs/search?keywords={urllib.parse.quote_plus(searchedJob)}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find job elements 
        jobs = soup.select('article[data-testid="job-card"]') or soup.select('div[class*="job"]')
        jobs = jobs[:10]  # Limit to 10 jobs
        
        job_list = []
        for job in jobs:
            # Get all text for regex extraction
            text = job.get_text()
        #web data extraction
            # Extract title 
            title_elem = (job.select_one('h2 a') or 
                         job.select_one('h3 a') or 
                         job.select_one('[data-testid="job-title"]') or
                         job.select_one('.job-title') or
                         job.select_one('a[title]'))
            
            # Extract company
            company_elem = (job.select_one('[data-testid="company-name"]') or
                           job.select_one('.company-name') or 
                           job.select_one('.recruiter') or
                           job.select_one('.employer'))
            
            # Extract location
            location_elem = (job.select_one('[data-testid="location"]') or
                            job.select_one('.location') or 
                            job.select_one('.place') or
                            job.select_one('.city'))
            
            # Extract salary from text
            salary_match = re.search(r'R\s*\d+[\d\s,]*(?:\s*-\s*R?\s*\d+[\d\s,]*)?', text)
            salary = salary_match.group().strip() if salary_match else "Not specified"
            
            # Extract date
            date_match = re.search(r'\d+\s+(?:day|week|month)s?\s+ago|today|yesterday', text, re.IGNORECASE)
            date = date_match.group().strip() if date_match else "Not specified"
            
            title_text = title_elem.get_text().strip() if title_elem else "Not specified"
            
            job_data = {
                'Title': title_text,
                'Recruiter': company_elem.get_text().strip() if company_elem else "Not specified", 
                'Salary': salary,
                'Position': title_text,
                'Location': location_elem.get_text().strip() if location_elem else "Not specified",
                'Date Posted': date
            }
            
            # Only add if we have at least a title
            if title_text != "Not specified":
                job_list.append(job_data)
        
        return job_list
        
    except Exception as e:
        print(f"Error: {e}")
        return []

def save_csv(jobs, searchedJob):
    """Save jobs to CSV file"""
    if not jobs:
        print("No jobs found")
        return
    
    df = pd.DataFrame(jobs)
    filename = f"{searchedJob.replace(' ', '-')}job-results.csv"
    df.to_csv(filename, index=False)
    
    print(f"Saved {len(jobs)} jobs to {filename}")
    print(df.head())

def askUser():
    """Prompt the user to input a job title they wish to search for."""
    print("Job Scraper - CareerJunction")
    searching = input("Enter job title: ").strip()

    if searching:
        print(f"Searching for '{searching}'...")
        jobs = get_jobs(searching)
        save_csv(jobs, searching)
    else:
        print("Please enter a job title")

if __name__ == "__main__":
    askUser()