import csv
from scrapper import search_books

def save_to_csv(books):
    file = open("./downloads.csv", mode="w", encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerow(["제목", "정보", "알라딘 링크", "예스24 링크"])

    for i, book in enumerate(books):
        writer.writerow([book['title'], book['info'], book['link']])