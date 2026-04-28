import pandas as pd
import base64
import os
from datetime import datetime

# 데이터 로드
df = pd.read_csv('data/nemo_items.csv')

# 요약 통계 계산
total_listings = len(df)
avg_deposit = df['deposit'].mean()
avg_monthly_rent = df['monthlyRent'].mean()
avg_size = df['size'].mean()
top_subway = df['nearSubwayStation'].mode()[0] if not df['nearSubwayStation'].empty else "N/A"
top_industry = df['businessMiddleCodeName'].mode()[0] if not df['businessMiddleCodeName'].empty else "N/A"

# 이미지 Base64 인코딩 함수
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return ""

# 이미지 리스트 및 Base64 변환
image_files = [
    "cat_businessMiddleCodeName.png", "cat_nearSubwayStation.png", "cat_priceTypeName.png",
    "tfidf_keywords.png", "scatter_size_rent.png", "barh_biz_deposit.png",
    "scatter_dep_rent_floor.png", "bar_subway_count.png", "hexbin_popularity.png",
    "hist_area_price.png", "box_deposit.png", "box_rent.png", "hist_size.png", "bar_biz_size.png"
]

images_b64 = {name: get_base64_image(f"images/{name}") for name in image_files}

# HTML 템플릿 작성
html_template = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nemo 부동산 데이터 분석 대시보드</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">
    <style>
        body {{
            font-family: 'Inter', 'Noto Sans KR', sans-serif;
            background-color: #0f172a;
            color: #f1f5f9;
        }}
        .glass-card {{
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 1rem;
        }}
        .gradient-text {{
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .stat-value {{
            font-size: 1.875rem;
            font-weight: 700;
            color: #38bdf8;
        }}
        .chart-container {{
            transition: transform 0.3s ease;
        }}
        .chart-container:hover {{
            transform: translateY(-5px);
        }}
        /* DataTables Custom Styling for Dark Theme */
        table.dataTable {{
            background-color: transparent !important;
            color: #f1f5f9 !important;
            border-collapse: collapse !important;
        }}
        table.dataTable tbody tr {{
            background-color: transparent !important;
        }}
        table.dataTable tbody tr:nth-child(even) {{
            background-color: rgba(255, 255, 255, 0.03) !important;
        }}
        table.dataTable tbody td {{
            color: #e2e8f0 !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
            padding: 12px 10px !important;
        }}
        /* Sorting Column Visibility Fix */
        table.dataTable tbody td.sorting_1, 
        table.dataTable tbody td.sorting_2, 
        table.dataTable tbody td.sorting_3 {{
            background-color: rgba(56, 189, 248, 0.05) !important; /* Very subtle blue tint */
            color: #38bdf8 !important; /* Blue text for sorted column */
            font-weight: 600 !important;
        }}
        table.dataTable.display tbody tr.odd > .sorting_1, 
        table.dataTable.order-column.stripe tbody tr.odd > .sorting_1 {{
            background-color: rgba(56, 189, 248, 0.08) !important;
        }}
        table.dataTable.display tbody tr.even > .sorting_1, 
        table.dataTable.order-column.stripe tbody tr.even > .sorting_1 {{
            background-color: rgba(56, 189, 248, 0.12) !important;
        }}

        .dataTables_wrapper .dataTables_length, 
        .dataTables_wrapper .dataTables_filter, 
        .dataTables_wrapper .dataTables_info, 
        .dataTables_wrapper .dataTables_processing, 
        .dataTables_wrapper .dataTables_paginate {{
            color: #cbd5e1 !important;
            margin-bottom: 15px;
        }}
        .dataTables_wrapper .dataTables_length select, 
        .dataTables_wrapper .dataTables_filter input {{
            background-color: #1e293b !important;
            color: #f1f5f9 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 0.375rem;
            outline: none;
            padding: 4px 8px;
        }}
        .dataTables_wrapper .dataTables_paginate .paginate_button {{
            color: #f1f5f9 !important;
            border-radius: 0.375rem !important;
            border: 1px solid transparent !important;
        }}
        .dataTables_wrapper .dataTables_paginate .paginate_button.current, 
        .dataTables_wrapper .dataTables_paginate .paginate_button.current:hover {{
            background: #38bdf8 !important;
            color: #0f172a !important;
            border: 1px solid #38bdf8 !important;
        }}
        .dataTables_wrapper .dataTables_paginate .paginate_button:hover {{
            background: rgba(56, 189, 248, 0.1) !important;
            color: #38bdf8 !important;
            border: 1px solid #38bdf8 !important;
        }}
        thead {{
            background-color: #1e293b;
        }}
        th {{
            color: #f1f5f9 !important;
            font-weight: 600 !important;
            border-bottom: 2px solid rgba(56, 189, 248, 0.5) !important;
            padding: 15px 10px !important;
        }}
    </style>
</head>
<body class="p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
        <!-- Header -->
        <header class="mb-10 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-2 gradient-text">Nemo Real Estate Analytics</h1>
            <p class="text-slate-400 text-lg">강남/서초 상업용 부동산 시장 심층 분석 대시보드</p>
            <p class="text-slate-500 text-sm mt-2">마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </header>

        <!-- Summary Stats -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
            <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">전체 매물 수</p>
                <p class="stat-value">{total_listings:,} <span class="text-sm font-normal text-slate-500">건</span></p>
            </div>
            <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">평균 보증금</p>
                <p class="stat-value">{int(avg_deposit):,} <span class="text-sm font-normal text-slate-500">만원</span></p>
            </div>
            <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">평균 월세</p>
                <p class="stat-value">{int(avg_monthly_rent):,} <span class="text-sm font-normal text-slate-500">만원</span></p>
            </div>
            <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">평균 면적</p>
                <p class="stat-value">{avg_size:.2f} <span class="text-sm font-normal text-slate-500">㎡</span></p>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
             <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">주요 역세권</p>
                <p class="text-2xl font-semibold text-indigo-400">{top_subway}</p>
            </div>
            <div class="glass-card p-6">
                <p class="text-slate-400 text-sm mb-1">최다 등록 업종</p>
                <p class="text-2xl font-semibold text-indigo-400">{top_industry}</p>
            </div>
        </div>

        <!-- Charts Grid -->
        <div class="space-y-10">
            <!-- Section 1: Market Overview -->
            <section>
                <h2 class="text-2xl font-bold mb-6 flex items-center">
                    <span class="w-2 h-8 bg-blue-500 rounded mr-3"></span>
                    시장 개요 및 업종 분포
                </h2>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">업종별 매물 분포 (Top 30)</h3>
                        <img src="data:image/png;base64,{images_b64['cat_businessMiddleCodeName.png']}" class="w-full h-auto rounded-lg">
                        <p class="mt-4 text-sm text-slate-400">기타창업모음과 다용도점포가 상위권을 차지하며 유연한 공간 수요를 반영합니다.</p>
                    </div>
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">지하철역별 접근성 분포</h3>
                        <img src="data:image/png;base64,{images_b64['cat_nearSubwayStation.png']}" class="w-full h-auto rounded-lg">
                        <p class="mt-4 text-sm text-slate-400">강남/역삼/신논현역 인근 도보 5분 이내 매물이 압도적으로 밀집되어 있습니다.</p>
                    </div>
                </div>
            </section>

            <!-- Section 2: Pricing Analysis -->
            <section>
                <h2 class="text-2xl font-bold mb-6 flex items-center">
                    <span class="w-2 h-8 bg-indigo-500 rounded mr-3"></span>
                    가격 지표 및 상관관계 분석
                </h2>
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <div class="glass-card p-6 chart-container lg:col-span-2">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">면적 대비 월세 상관관계</h3>
                        <img src="data:image/png;base64,{images_b64['scatter_size_rent.png']}" class="w-full h-auto rounded-lg">
                    </div>
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">거래 형태 비율</h3>
                        <img src="data:image/png;base64,{images_b64['cat_priceTypeName.png']}" class="w-full h-auto rounded-lg">
                        <p class="mt-4 text-sm text-slate-400">99% 이상이 임대 매물로, 수익형 자산으로서의 성격이 강합니다.</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-8">
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">업종별 평균 보증금</h3>
                        <img src="data:image/png;base64,{images_b64['barh_biz_deposit.png']}" class="w-full h-auto rounded-lg">
                    </div>
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">층별 임대료 분포 (보증금 vs 월세)</h3>
                        <img src="data:image/png;base64,{images_b64['scatter_dep_rent_floor.png']}" class="w-full h-auto rounded-lg">
                    </div>
                </div>
            </section>

            <!-- Section 3: Popularity & Keywords -->
            <section>
                <h2 class="text-2xl font-bold mb-6 flex items-center">
                    <span class="w-2 h-8 bg-cyan-500 rounded mr-3"></span>
                    인기도 및 마케팅 인사이트
                </h2>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">매물 제목 주요 키워드 (TF-IDF)</h3>
                        <img src="data:image/png;base64,{images_b64['tfidf_keywords.png']}" class="w-full h-auto rounded-lg">
                        <p class="mt-4 text-sm text-slate-400">'무권리', '역세권', '인테리어' 등이 핵심 소구점으로 나타납니다.</p>
                    </div>
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">조회수 및 즐겨찾기 상관관계</h3>
                        <img src="data:image/png;base64,{images_b64['hexbin_popularity.png']}" class="w-full h-auto rounded-lg">
                        <p class="mt-4 text-sm text-slate-400">단순 노출보다 매물의 조건적 우월성이 실제 관심(즐겨찾기)으로 이어집니다.</p>
                    </div>
                </div>
            </section>

             <!-- Section 4: Efficiency & Distribution -->
            <section>
                <h2 class="text-2xl font-bold mb-6 flex items-center">
                    <span class="w-2 h-8 bg-emerald-500 rounded mr-3"></span>
                    면적 및 가격 효율성
                </h2>
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">단위 면적당 가격 분포</h3>
                        <img src="data:image/png;base64,{images_b64['hist_area_price.png']}" class="w-full h-auto rounded-lg">
                    </div>
                    <div class="glass-card p-6 chart-container">
                        <h3 class="text-lg font-semibold mb-4 text-slate-300">매물 면적 분포 히스토그램</h3>
                        <img src="data:image/png;base64,{images_b64['hist_size.png']}" class="w-full h-auto rounded-lg">
                    </div>
                </div>
            </section>
        </div>

        <!-- Data Explorer -->
        <section class="mt-16">
            <h2 class="text-2xl font-bold mb-6 flex items-center">
                <span class="w-2 h-8 bg-amber-500 rounded mr-3"></span>
                Data Explorer
            </h2>
            <div class="glass-card p-6 overflow-x-auto">
                <table id="listingsTable" class="display w-full text-sm">
                    <thead>
                        <tr>
                            <th>제목</th>
                            <th>업종</th>
                            <th>보증금</th>
                            <th>월세</th>
                            <th>면적(㎡)</th>
                            <th>지하철역</th>
                            <th>조회수</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Data rows will be injected by Python script or just pre-rendered -->
                        { "".join([f"<tr><td>{row['title']}</td><td>{row['businessMiddleCodeName']}</td><td>{row['deposit']:,}</td><td>{row['monthlyRent']:,}</td><td>{row['size']}</td><td>{row['nearSubwayStation']}</td><td>{row['viewCount']}</td></tr>" for _, row in df.iterrows()]) }
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Footer Footer -->
        <footer class="mt-20 pt-10 border-t border-slate-800 text-center text-slate-500 text-sm">
            <p>© 2026 Nemo Real Estate Analytics Project. All rights reserved.</p>
            <p class="mt-2 italic">"데이터는 거짓말을 하지 않습니다. 숫자의 이면에 숨겨진 가치를 발견하십시오."</p>
        </footer>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>
    <script>
        $(document).ready( function () {{
            $('#listingsTable').DataTable({{
                "language": {{
                    "url": "//cdn.datatables.net/plug-ins/1.11.5/i18n/ko.json"
                }},
                "pageLength": 10,
                "order": [[ 6, "desc" ]]
            }});
        }});
    </script>
</body>
</html>
"""

# 결과 저장
os.makedirs('report', exist_ok=True)
with open('report/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"대시보드가 생성되었습니다: report/dashboard.html")
