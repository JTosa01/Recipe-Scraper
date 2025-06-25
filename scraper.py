import requests
from bs4 import BeautifulSoup



URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

for job in job_elements:
    print (job, end="\n" * 2)
