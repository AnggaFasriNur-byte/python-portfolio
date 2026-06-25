import os
import csv
import requests
from bs4 import BeautifulSoup


########## CONFIGURATION


URL = "https://www.python.org/jobs/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}


##### REQUEST WEBSITE


response = requests.get(URL, headers=HEADERS)

if response.status_code != 200:
    print(f"Failed to access website. Status code: {response.status_code}")
    exit()

print("Website accessed successfully.")


####### PARSE HTML


soup = BeautifulSoup(response.content, "html.parser")

job_list = soup.find("ol", class_="list-recent-jobs")

if not job_list:
    print("Job list not found.")
    exit()

jobs = []


######### SCRAPING + CLEANING


for job in job_list.find_all("li"):
    #print(job.prettify())
    #break

  
    ### TITLE
    

    title = job.find("h2").get_text(" ", strip=True)

    # hapus kata "New" di depan judul
    if title.startswith("New "):
        title = title.replace("New ", "", 1)

   
    ####### COMPANY
  

    company_tag = job.find(
        "span",
        class_="listing-company-name"
    )

    company = (
        company_tag.get_text(" ", strip=True)
        if company_tag
        else "N/A"
    )

    
    ####### LOCATION
   

    location_tag = job.find(
        "span",
        class_="listing-location"
    )

    location = (
        location_tag.get_text(" ", strip=True)
        if location_tag
        else "N/A"
    )

    
    ###### DATE
   

    date_tag = job.find("time")

    date_posted = (
        date_tag.get_text(" ", strip=True)
        if date_tag
        else "N/A"
    )

    jobs.append({
        "title": title,
        "company": company,
        "location": location,
        "date_posted": date_posted
    })


###### CREATE DATA FOLDER


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

CSV_PATH = os.path.join(
    DATA_DIR,
    "python_jobs_clean.csv"
)


######### SAVE CSV


with open(
    CSV_PATH,
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    fieldnames = [
        "title",
        "company",
        "location",
        "date_posted"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(jobs)


# SUMMARY


print("\n===================================")
print("SCRAPING COMPLETED SUCCESSFULLY")
print("===================================")
print(f"Total jobs collected : {len(jobs)}")
print(f"CSV saved to         : {CSV_PATH}")
print("===================================")