---
marp: true
theme: default
paginate: true
header: 'Nemo 상권 분석 - Bento Grid Style (Full Width)'
footer: '20년 경력 데이터 분석가 리포트'
backgroundColor: #F8F8F2
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
  section {
    font-family: 'Inter', 'Pretendard', sans-serif;
    padding: 35px 50px;
    background-color: #F8F8F2;
    display: block;
  }
  h1 { color: #1A1A2E; font-size: 2.5em; font-weight: 800; margin-bottom: 0.3em; }
  h2 { color: #1A1A2E; font-size: 1.5em; font-weight: 600; margin-top: 0; }
  .grid-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 25px;
    height: 88%;
    width: 100%;
  }
  .cell {
    border-radius: 28px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 10px 20px rgba(0,0,0,0.04);
  }
  .cell-navy { background-color: #1A1A2E; color: #FFFFFF; }
  .cell-yellow { background-color: #E8FF3B; color: #000; }
  .cell-coral { background-color: #FF6B6B; color: #FFF; }
  .cell-teal { background-color: #4ECDC4; color: #000; }
  .cell-warm { background-color: #FFE66D; color: #000; }
  .cell-white { background-color: #FFFFFF; color: #000; border: 1px solid #E0E0E0; }
  
  .stat-large { font-size: 3.8em; font-weight: 800; line-height: 1; margin: 15px 0; }
  .label { font-size: 1em; text-transform: uppercase; letter-spacing: 0.12em; opacity: 0.8; margin-bottom: 8px; font-weight: 600; }
  
  footer { font-size: 0.5em; color: #888; }
  header { font-size: 0.6em; color: #1A1A2E; opacity: 0.5; }
---

# 🎯 부동산 매물 데이터 EDA 보고서
### 강남/서초 상권 데이터 심층 분석 리포트

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 8; grid-row: span 4;">
    <h2 style="color: #E8FF3B;">Core Analysis</h2>
    <p style="font-size: 1.4em; line-height: 1.5; margin-bottom: 20px;">20년 경력 데이터 사이언티스트가 분석한<br>숫자 너머의 시장 심리와 비즈니스 전략</p>
    <p style="opacity: 0.7; font-size: 1.05em;">강남 상권은 대한민국에서 가장 역동적이고 복잡한 곳입니다. 이번 분석이 여러분의 의사결정에 강력한 데이터 기반의 이정표가 되기를 바랍니다.</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">Total Samples</div>
    <div class="stat-large">673</div>
  </div>
  <div class="cell cell-teal" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">Region</div>
    <div class="stat-large" style="font-size: 2.8em;">강남/서초</div>
  </div>
</div>

---

# 📋 Slide 2: 데이터 개요 및 하이라이트

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">평균 보증금</div>
    <div class="stat-large" style="font-size: 3.2em;">6,895만</div>
    <p style="font-size: 1.1em;">입지 간 격차 매우 큼</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">평균 월세</div>
    <div class="stat-large" style="font-size: 3.2em;">534만</div>
    <p style="font-size: 1.1em;">고정비 부담 높은 편</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 12; grid-row: span 2;">
    <h2>📍 주요 위치 스냅샷</h2>
    <p style="font-size: 1.3em;">역삼, 강남, 신논현 초역세권 테헤란로 핵심 축 집중 분석</p>
    <p style="font-size: 0.95em; opacity: 0.8;">핵심 입지와 이면 도로 입지 간의 위계가 철저히 나뉘어 있음을 시사합니다.</p>
  </div>
</div>

---

# 📊 Slide 3: 보증금 및 월세 양극화

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 4;">
    <div class="label">Top 10% 보증금</div>
    <div class="stat-large" style="font-size: 3.2em;">1.5억+</div>
    <div class="label">Top 10% 월세</div>
    <div class="stat-large" style="font-size: 3.2em;">1,000만+</div>
  </div>
  <div class="cell cell-warm" style="grid-column: span 4; grid-row: span 4;">
    <div class="label" style="color: #1A1A2E;">💡 비즈니스 통찰</div>
    <p style="font-size: 1.3em; line-height: 1.5; color: #1A1A2E;">단순 판매를 넘어 브랜드 가치를 증명하는 <b>'플래그십 스토어'</b> 요충지</p>
  </div>
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4;">
    <div class="label">Strategy</div>
    <p style="font-size: 1.3em; line-height: 1.5;">목적에 따른 타겟팅 필요:<br><br><span style="color: #FF6B6B; font-weight: 800;">브랜드 홍보 vs 실질 이익</span></p>
  </div>
</div>

---

# 📊 Slide 4: 면적 및 관리비 특성

<div class="grid-container">
  <div class="cell cell-teal" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">면적 중앙값</div>
    <div class="stat-large">102㎡</div>
    <div class="label">약 30평 규모</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 8; grid-row: span 2;">
    <h2>🏢 소규모 최적화</h2>
    <p style="font-size: 1.3em;">IT, 뷰티 등 고부가가치 업종에 최적화된 집약적 공간 구조</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 12; grid-row: span 2;">
    <div class="label">평균 관리비</div>
    <div class="stat-large" style="font-size: 3em;">60만 원대</div>
    <p style="font-size: 1.1em;">월세의 10~15% 수준. 실질 현금 흐름 분석 시 필수 고려 사항</p>
  </div>
</div>

---

# 🏗️ Slide 5: 업종 및 시장 구조

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4;">
    <div style="font-size: 3em; margin-bottom: 10px;">🏢</div>
    <div class="label">공간의 유연성</div>
    <p style="font-size: 1.2em;">'기타창업모음', '다용도점포' 등 트렌드 민감 업종 대다수</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 4; grid-row: span 4;">
    <div class="label">임대 비율</div>
    <div class="stat-large" style="font-size: 4.5em;">99%</div>
    <p style="font-size: 1.2em; font-weight: 600;">안정성</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 4;">
    <p style="font-size: 1.4em; line-height: 1.4;">오프라인 공간이 '판매'에서<br><br><span style="color:#E8FF3B; font-weight: 800;">'체험 및 서비스'</span><br>중심으로 재편</p>
  </div>
</div>

---

# 🔍 Slide 6: 키워드 분석 (TF-IDF)

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 8; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/tfidf_keywords.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">Keywords</div>
    <p style="font-size: 1.2em; line-height: 1.6;">#무권리<br>#역세권<br>#인테리어완비</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 4; grid-row: span 2;">
    <p style="font-size: 1.1em; font-weight: 600;">CapEx 절감을 위한<br>실속형 수요 집중</p>
  </div>
</div>

---

# 📈 Slide 7: [시각화] 면적 대비 월세 상관관계

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 8; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/scatter_size_rent.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-teal" style="grid-column: span 4; grid-row: span 4;">
    <div style="font-size: 3em; margin-bottom: 10px;">💡</div>
    <div class="label">입지 분석</div>
    <p style="font-size: 1.2em; line-height: 1.5;">면적 대비 고효율<br><b>'골든 존'</b> 매물 존재</p>
    <p style="font-size: 0.95em; opacity: 0.8; margin-top: 15px;">면적의 경제보다 '입지의 경제'가 압도적으로 작용하는 시장입니다.</p>
  </div>
</div>

---

# 💰 Slide 8: [시각화] 업종별 평균 보증금

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 12; grid-row: span 3; padding: 10px; overflow: hidden;">
    <img src="../images/barh_biz_deposit.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 12; grid-row: span 1;">
    <p style="text-align: center; font-size: 1.2em;">시설 비중이 큰 <b>레스토랑/주점</b> 업종일수록 원상복구 리스크로 인한 고액 보증금 형성</p>
  </div>
</div>

---

# 🏢 Slide 9: [시각화] 층별 가치 분포 비교

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 7; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/scatter_dep_rent_floor.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 5; grid-row: span 1;">
    <div class="label" style="margin: 0;">1층: 압도적 접근성 프리미엄</div>
  </div>
  <div class="cell cell-teal" style="grid-column: span 5; grid-row: span 1;">
    <div class="label" style="margin: 0;">지하/고층: 공간 효율 및 비용 절감</div>
  </div>
  <div class="cell cell-navy" style="grid-column: span 5; grid-row: span 2;">
    <p style="font-size: 1.15em; line-height: 1.5;">목적형 방문 업종은 <b>상층부</b>를 선택하여 고정 임대료를 낮추는 전략이 유효합니다.</p>
  </div>
</div>

---

# 🚉 Slide 10: [시각화] 지하철역별 공급 현황

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 8; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/bar_subway_count.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-coral" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">Hotspots</div>
    <p style="font-size: 1.3em; font-weight: 800;">강남, 역삼, 신논현</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">Opportunity</div>
    <p style="font-size: 1.1em;">비주류 역세권의<br><b>블루오션</b> 공략 제언</p>
  </div>
</div>

---

# 🌟 Slide 11: [시각화] 매물 인기도 분석

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 9; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/hexbin_popularity.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 3; grid-row: span 4;">
    <div style="font-size: 3em; margin-bottom: 10px;">🎯</div>
    <div class="label">킬러 조건</div>
    <p style="font-size: 1.2em; line-height: 1.5;">'무권리' 파격 조건이<br><b>실제 계약 의지</b>를<br>결정짓는 핵심 변수</p>
  </div>
</div>

---

# 📐 Slide 12: [시각화] 면적당 가격 효율성

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 8; grid-row: span 4; padding: 10px; overflow: hidden;">
    <img src="../images/hist_area_price.png" style="width: 100%; height: 100%; object-fit: contain; border-radius: 20px;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 4; grid-row: span 2;">
    <div class="label">합리적 시세</div>
    <div class="stat-large" style="font-size: 3.5em;">90~192</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 2;">
    <p style="font-size: 1.05em; font-weight: 600;">시세 이탈 매물은<br><span style="color: #FF6B6B;">심층 하자 검토</span> 필수</p>
  </div>
</div>

---

# 💡 Slide 13: 결론 및 종합 전략 제언

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">01. 현금 흐름 우선</div>
    <p style="font-size: 1.2em;">무권리 매물 선점을 통한 초기 리스크 최소화</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">02. 입지 위계 분석</div>
    <p style="font-size: 1.2em;">면적을 줄이더라도 초역세권 핵심 동선 확보</p>
  </div>
  <div class="cell cell-teal" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">03. 유연한 출구 전략</div>
    <p style="font-size: 1.2em;">다용도 특성 활용, 업종 변경이 용이한 공간 선택</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">04. 데이터 기반 협상</div>
    <p style="font-size: 1.2em;">객관적 지표 근거로 임대료 협상의 우위 점유</p>
  </div>
</div>

---

# 🚀 숫자의 이면에 숨겨진 심리를 읽는 것
### 그것이 강남 상권 생존의 핵심 전략입니다.

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 12; grid-row: span 4;">
    <p style="font-size: 2em; text-align: center; font-weight: 800;">20년 경력 데이터 분석가 리포트<br><span style="color: #E8FF3B;">Nemo Real Estate Analytics</span></p>
    <hr style="border: 2px solid #E8FF3B; width: 40%; margin: 40px auto;">
    <p style="text-align: center; opacity: 0.8; font-size: 1.3em;">데이터는 여러분의 가장 강력한 비즈니스 파트너입니다.</p>
  </div>
</div>
