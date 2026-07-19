import requests
from bs4 import BeautifulSoup


def search_books(keyword, page=1):
    url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={keyword}&page={page}&display=40"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select('div.ss_book_box')
    
    results = []
    for item in items:
        if len(results) >= 20: 
            break
            
        title_tag = item.select_one('a.bo3')
        if not title_tag: continue
        
        author_tag = item.select_one('a[href*="AuthorSearch"]')
        author = author_tag.text.strip() if author_tag else "저자 정보 없음"
        img_tag = item.select_one('img.front_cover') or item.select_one('img.i_s')
        img_url = img_tag.get('src') if img_tag else "https://via.placeholder.com/100x140?text=No+Img"
        
        results.append({
            "title": title_tag.text.strip(),
            "info": author,
            "link": title_tag.get('href', '#'),
            "img_url": img_url
        })
    return results