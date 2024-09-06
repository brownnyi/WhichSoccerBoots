import requests
from bs4 import BeautifulSoup

def fetch_football_data(page_num):
    url = f"https://www.footballbootsdb.com/search/?league=0&brand=&boot=&position=&age-min=15&age-max=45&height-min=155&height-max=210&market-value-min=0&market-value-max=200&page={page_num}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 테이블의 tbody 부분을 찾음
    table_body = soup.find('table', class_='player-list-table').find('tbody')
    rows = table_body.find_all('tr')

    results = []
    for row in rows:
        cols = row.find_all('td')
        
        # 데이터 추출
        position_class = row.get('class', [])[0]
        position = position_class.replace('-tr', '').capitalize()  # 예: 'Goalkeeper-tr' -> 'Goalkeeper'
        
        country_img = cols[0].find('img')
        country = country_img['alt'] if country_img else 'N/A'
        
        name = cols[2].text.strip()
        club = cols[3].text.strip()
        boots = cols[4].text.strip()
        age = cols[5].text.strip()
        height = cols[6].text.strip()
        
        results.append({
            'position': position,
            'country': country,
            'name': name,
            'club': club,
            'boots': boots,
            'age': age,
            'height': height
        })
    
    return results

def fetch_all_pages(start_page, end_page):
    all_data = []
    for page_num in range(start_page, end_page + 1):
        print(f"Fetching page {page_num}...")
        data = fetch_football_data(page_num)
        if data:
            all_data.extend(data)
        else:
            print(f"No data found on page {page_num}.")
    return all_data

# 사용 예
start_page = 1
end_page = 1039
all_data = fetch_all_pages(start_page, end_page)

# 결과를 파일로 저장하거나 다른 방식으로 처리할 수 있습니다.
print(f"Total players fetched: {len(all_data)}")
