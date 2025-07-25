import requests
from bs4 import BeautifulSoup

# Step 1: Ask user for topic
topic = input("Enter Wikipedia topic to search: ").replace(" ", "_")
url = f"https://en.wikipedia.org/wiki/{topic}"

# Step 2: Fetch page
response = requests.get(url)

if response.status_code != 200:
    print("Article not found!")
    exit()

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract title
title = soup.find("h1").text

# Step 5: Extract first paragraph
first_para = ""
for p in soup.select("div.mw-parser-output > p"):
    if p.text.strip():
        first_para = p.text.strip()
        break

# DEBUG: Print if paragraph found
if not first_para:
    print("⚠️ Warning: No paragraph found.")

# Step 6: Extract all headings (h2 to h4)
headings = soup.find_all(["h2", "h3", "h4"])

# Step 7: Print data
print("\n📰 Title:", title)
print("\n📜 Summary:\n", first_para.strip())

print("\n📚 Headings:")
for heading in headings:
    print("-", heading.text.strip())

# Optional: Save to file
with open(f"{topic}_summary.txt", "w", encoding="utf-8") as f:
    f.write("Title: " + title + "\n\n")
    f.write("Summary:\n" + first_para.strip() + "\n\n")
    f.write("Headings:\n")
    for heading in headings:
        f.write("- " + heading.text.strip() + "\n")

print(f"\n📄 Saved to '{topic}_summary.txt'")
