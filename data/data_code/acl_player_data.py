import pandas as pd

data = []

with open('십자인대 터진 축구선수 목록.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            name, content = line.split(':', 1)
        else:
            name, content = line, ''  # 콜론이 없으면 content는 빈 문자열
        data.append({'name': name.strip(), 'content': content.strip()})

df_acl = pd.DataFrame(data)
