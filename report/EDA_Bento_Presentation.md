---
marp: true
theme: default
paginate: true
header: 'Nemo 상권 분석 - Bento Grid Style (Wide)'
footer: '20년 경력 데이터 분석가 리포트'
backgroundColor: #F8F8F2
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
  section {
    font-family: 'Inter', 'Pretendard', sans-serif;
    padding: 50px;
    background-color: #F8F8F2;
    display: block;
  }
  h1 { color: #1A1A2E; font-size: 2.2em; font-weight: 800; margin-bottom: 0.5em; }
  h2 { color: #1A1A2E; font-size: 1.4em; font-weight: 600; margin-top: 0; }
  .grid-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 20px;
    height: 85%;
    width: 100%;
  }
  .cell {
    border-radius: 24px;
    padding: 25px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 8px 15px rgba(0,0,0,0.04);
  }
  .cell-navy { background-color: #1A1A2E; color: #FFFFFF; }
  .cell-yellow { background-color: #E8FF3B; color: #000; }
  .cell-coral { background-color: #FF6B6B; color: #FFF; }
  .cell-teal { background-color: #4ECDC4; color: #000; }
  .cell-warm { background-color: #FFE66D; color: #000; }
  .cell-white { background-color: #FFFFFF; color: #000; border: 1px solid #E0E0E0; }
  
  .stat-large { font-size: 3.5em; font-weight: 800; line-height: 1; margin: 15px 0; }
  .label { font-size: 0.9em; text-transform: uppercase; letter-spacing: 0.12em; opacity: 0.8; margin-bottom: 5px; }
  
  footer { font-size: 0.5em; color: #888; }
  header { font-size: 0.6em; color: #1A1A2E; opacity: 0.5; }
---

# 🎯 부동산 매물 데이터 EDA 보고서
### 강남/서초 상권 데이터 심층 분석 리포트

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 3; grid-row: span 4;">
    <h2 style="color: #E8FF3B;">Core Analysis</h2>
    <p style="font-size: 1.3em; line-height: 1.4;">20년 경력 데이터 사이언티스트가 분석한<br>숫자 너머의 시장 심리와 비즈니스 전략</p>
    <p style="opacity: 0.7; font-size: 0.95em;">강남 상권은 대한민국에서 가장 역동적이고 복잡한 곳입니다. 이번 분석이 여러분의 의사결정에 강력한 데이터 기반의 이정표가 되기를 바랍니다.</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">Samples</div>
    <div class="stat-large">673</div>
  </div>
  <div class="cell cell-teal" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">Region</div>
    <div class="stat-large" style="font-size: 2.5em;">강남/서초</div>
  </div>
</div>

---

# 📋 Slide 2: 데이터 개요 및 하이라이트

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">평균 보증금</div>
    <div class="stat-large" style="font-size: 2.8em;">6,895만</div>
    <p>입지 간 격차 매우 큼</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">평균 월세</div>
    <div class="stat-large" style="font-size: 2.8em;">534만</div>
    <p>고정비 부담 높은 편</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 2;">
    <h2>📍 주요 위치 스냅샷</h2>
    <p style="font-size: 1.1em;">역삼, 강남, 신논현 초역세권 테헤란로 핵심 축 집중 분석</p>
    <p style="font-size: 0.85em; opacity: 0.8;">핵심 입지와 이면 도로 입지 간의 위계가 철저히 나뉘어 있음을 시사합니다.</p>
  </div>
</div>

---

# 📊 Slide 3: 보증금 및 월세 양극화

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 4;">
    <div class="label">Top 10% 보증금</div>
    <div class="stat-large">1.5억+</div>
    <div class="label">Top 10% 월세</div>
    <div class="stat-large">1,000만+</div>
  </div>
  <div class="cell cell-warm" style="grid-column: span 2; grid-row: span 2;">
    <h2>💡 비즈니스 통찰</h2>
    <p>단순 판매를 넘어 브랜드 가치를 증명하는 '플래그십 스토어' 요충지</p>
  </div>
  <div class="cell cell-white" style="grid-column: span 2; grid-row: span 2;">
    <p style="font-size: 1.1em;">목적에 따른 타겟팅 필요:<br><b>브랜드 홍보 vs 실질 이익</b></p>
  </div>
</div>

---

# 📊 Slide 4: 면적 및 관리비 특성

<div class="grid-container">
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">면적 중앙값</div>
    <div class="stat-large">102㎡</div>
    <div class="label">약 30평 규모</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 2; grid-row: span 2;">
    <h2>🏢 소규모 최적화</h2>
    <p>IT, 뷰티 등 고부가가치 업종에 최적화된 집약적 공간 구조</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">평균 관리비</div>
    <div class="stat-large">60만 원대</div>
    <p>월세의 10~15% 수준. 실질 현금 흐름 분석 시 필수 고려 사항</p>
  </div>
</div>

---

# 🏗️ Slide 5: 업종 및 시장 구조

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 2;">
    <h2>🏢 공간의 유연성</h2>
    <p>'기타창업모음', '다용도점포' 등 트렌드 민감 업종 대다수</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 1; grid-row: span 4;">
    <div class="label">임대 비율</div>
    <div class="stat-large">99%</div>
    <p>안정성</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 3; grid-row: span 2;">
    <p style="font-size: 1.2em;">오프라인 공간이 '판매'에서<br><span style="color:#E8FF3B;">'체험 및 서비스'</span> 중심으로 재편</p>
  </div>
</div>

---

# 🔍 Slide 6: 키워드 분석 (TF-IDF)

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/tfidf_keywords.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">Keywords</div>
    <p style="font-size: 0.9em;">#무권리<br>#역세권<br>#인테리어</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 1; grid-row: span 2;">
    <p style="font-size: 0.8em;">CapEx 절감 실속형 수요</p>
  </div>
</div>

---

# 📈 Slide 7: [시각화] 면적 대비 월세 상관관계

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/scatter_size_rent.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-teal" style="grid-column: span 1; grid-row: span 4;">
    <h2>💡 입지</h2>
    <p style="font-size: 0.9em;"><b>'골든 존'</b><br>특이점 존재</p>
    <p style="font-size: 0.8em; opacity: 0.8;">입지의 경제가 강력하게 작용</p>
  </div>
</div>

---

# 💰 Slide 8: [시각화] 업종별 평균 보증금

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 3; padding: 0; overflow: hidden;">
    <img src="../images/barh_biz_deposit.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 1;">
    <p>레스토랑/주점 등 <b>시설 비중 큰 업종</b>일수록 고액 보증금 형성 (원상복구 리스크)</p>
  </div>
</div>

---

# 🏢 Slide 9: [시각화] 층별 가치 분포 비교

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 2; grid-row: span 3; padding: 0; overflow: hidden;">
    <img src="../images/scatter_dep_rent_floor.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 2; grid-row: span 1;">
    <div class="label">1층: 접근성</div>
  </div>
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 1;">
    <div class="label">지하/고층: 효율성</div>
  </div>
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 1;">
    <p>목적형 업종은 <b>상층부</b>로 고정비 절감</p>
  </div>
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 1;">
    <p style="text-align: center;">층별 특성에 따른 <b>전략적 임차</b>가 강남 생존의 핵심</p>
  </div>
</div>

---

# 🚉 Slide 10: [시각화] 지하철역별 공급 현황

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/bar_subway_count.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-coral" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">Hot</div>
    <p>강남, 역삼</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">Blue</div>
    <p>틈새 공략</p>
  </div>
</div>

---

# 🌟 Slide 11: [시각화] 매물 인기도 분석

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/hexbin_popularity.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 1; grid-row: span 4;">
    <h2>🎯 조건</h2>
    <p style="font-size: 0.9em;">'무권리'가<br><b>계약 의지</b> 유도</p>
  </div>
</div>

---

# 📐 Slide 12: [시각화] 면적당 가격 효율성

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/hist_area_price.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 1; grid-row: span 2;">
    <div class="label">시세</div>
    <div class="stat-large" style="font-size: 2em;">90~192</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 1; grid-row: span 2;">
    <p style="font-size: 0.8em;">하자 검토 필수</p>
  </div>
</div>

---

# 💡 Slide 13: 결론 및 종합 전략 제언

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">01. 현금 흐름</div>
    <p>무권리 매물 선점</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">02. 입지 우선</div>
    <p>초역세권 핵심 동선</p>
  </div>
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">03. 출구 전략</div>
    <p>다용도 특성 활용</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">04. 데이터 협상</div>
    <p>객관적 지표 근거</p>
  </div>
</div>

---

# 🚀 숫자의 이면에 숨겨진 심리를 읽는 것
### 그것이 강남 상권 생존의 핵심 전략입니다.

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 4;">
    <p style="font-size: 1.8em; text-align: center;">20년 경력 데이터 분석가 리포트<br><b>Nemo Real Estate Analytics</b></p>
    <hr style="border: 2px solid #E8FF3B; width: 40%; margin: 30px auto;">
    <p style="text-align: center; opacity: 0.8; font-size: 1.1em;">데이터는 여러분의 가장 강력한 비즈니스 파트너입니다.</p>
  </div>
</div>
