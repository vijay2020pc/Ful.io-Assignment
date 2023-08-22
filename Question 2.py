import re
import requests
from bs4 import BeautifulSoup

def extract_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        social_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'facebook.com' in href or 'linkedin.com' in href:
                social_links.append(href)
        
        email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', response.text)
        
        contact = re.findall(r'(\+\d{1,3} \d{3} \d{3} \d{4})', response.text)
        
        return social_links, email, contact
    else:
        print("Failed to fetch the webpage.")
        return [], [], []

if __name__ == "__main__":
    user_input = input("Enter a website URL: ")
    social_links, email, contact = extract_details(user_input)
    
    print("Social links:")
    for link in social_links:
        print(link)
    
    if email:
        print("Email:", email[0])
    else:
        print("No email found.")
    
    if contact:
        print("Contact:", contact[0])
    else:
        print("No contact found.")
