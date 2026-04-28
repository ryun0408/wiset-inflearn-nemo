import requests
import pandas as pd
import sqlite3
import os
import time

# API 설정
URL = "https://www.nemoapp.kr/api/store/search-list"
PARAMS = {
    "Subway": "222",
    "Radius": "1000",
    "CompletedOnly": "false",
    "NELat": "37.51881599458073",
    "NELng": "127.05728295870226",
    "SWLat": "37.4753653067897",
    "SWLng": "127.00226104982909",
    "Zoom": "15",
    "SortBy": "29"
}
HEADERS = {
    "referer": "https://www.nemoapp.kr/store",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

def scrape_nemo():
    all_items = []
    page_index = 0
    
    print("Nemo API 전체 데이터 수집 시작...")
    
    while True:
        current_params = PARAMS.copy()
        current_params["PageIndex"] = page_index
        
        print(f"페이지 {page_index} 수집 중...")
        try:
            response = requests.get(URL, params=current_params, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            items = data.get("items", [])
            
            if not items:
                print(f"페이지 {page_index}에서 데이터를 찾을 수 없습니다. 수집을 종료합니다.")
                break
                
            all_items.extend(items)
            print(f"페이지 {page_index}: {len(items)}개 아이템 추가 (현재 총 {len(all_items)}개)")
            
            page_index += 1
            time.sleep(0.5) # 서버 부하 방지를 위한 짧은 지연
            
        except Exception as e:
            print(f"페이지 {page_index} 수집 중 에러 발생: {e}")
            break
            
    if all_items:
        print(f"수집 완료. 총 {len(all_items)}개의 아이템을 처리합니다.")
        
        # 데이터프레임 변환
        df = pd.DataFrame(all_items)
        
        # 중복 제거 (ID 기준)
        if 'id' in df.columns:
            before_count = len(df)
            df = df.drop_duplicates(subset=['id'])
            after_count = len(df)
            if before_count != after_count:
                print(f"중복 제거 완료: {before_count} -> {after_count}")
        
        # SQLite 저장을 위해 리스트나 딕셔너리 타입을 문자열로 변환
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                df[col] = df[col].apply(lambda x: str(x) if x is not None else x)
        
        # 저장 경로 설정
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        csv_path = os.path.join(data_dir, "nemo_items.csv")
        db_path = os.path.join(data_dir, "nemo_data.db")
        
        # CSV 저장
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"CSV 저장 완료: {csv_path}")
        
        # SQLite 저장
        try:
            conn = sqlite3.connect(db_path)
            df.to_sql("nemo_stores", conn, if_exists="replace", index=False)
            conn.close()
            print(f"SQLite DB 저장 완료: {db_path}")
        except Exception as e:
            print(f"SQLite 저장 중 에러 발생: {e}")
    else:
        print("수집된 데이터가 없습니다.")

if __name__ == "__main__":
    scrape_nemo()
