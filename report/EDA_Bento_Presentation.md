---
marp: true
theme: default
paginate: true
header: 'Nemo 상권 분석 - Bento Grid Style'
footer: '20년 경력 데이터 분석가 리포트'
backgroundColor: #F8F8F2
style: |
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
  section {
    font-family: 'Inter', 'Pretendard', sans-serif;
    padding: 40px;
    background-color: #F8F8F2;
    display: block;
  }
  h1 { color: #1A1A2E; font-size: 2.2em; font-weight: 800; margin-bottom: 0.5em; }
  h2 { color: #1A1A2E; font-size: 1.4em; font-weight: 600; margin-top: 0; }
  .grid-container {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(4, 1fr);
    gap: 15px;
    height: 80%;
    width: 100%;
  }
  .cell {
    border-radius: 20px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }
  .cell-navy { background-color: #1A1A2E; color: #FFFFFF; }
  .cell-yellow { background-color: #E8FF3B; color: #000; }
  .cell-coral { background-color: #FF6B6B; color: #FFF; }
  .cell-teal { background-color: #4ECDC4; color: #000; }
  .cell-warm { background-color: #FFE66D; color: #000; }
  .cell-white { background-color: #FFFFFF; color: #000; border: 1px solid #E0E0E0; }
  
  .stat-large { font-size: 3em; font-weight: 800; line-height: 1; margin: 10px 0; }
  .label { font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.8; }
  .highlight { font-weight: 800; color: #FF6B6B; }
  
  footer { font-size: 0.5em; color: #888; }
  header { font-size: 0.6em; color: #1A1A2E; opacity: 0.5; }
---

# 🎯 부동산 매물 데이터 EDA 보고서
### 강남/서초 상권 데이터 심층 분석 리포트

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 4;">
    <h2 style="color: #E8FF3B;">Core Analysis</h2>
    <p style="font-size: 1.2em;">20년 경력 데이터 사이언티스트가 분석한<br>숫자 너머의 시장 심리와 비즈니스 전략</p>
    <p style="opacity: 0.7;">강남 상권은 대한민국에서 가장 역동적이고 복잡한 곳입니다. 이번 분석이 여러분의 의사결정에 강력한 데이터 기반의 이정표가 되기를 바랍니다.</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">Total Samples</div>
    <div class="stat-large">673</div>
    <div class="label">Nemo API Data</div>
  </div>
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">Region</div>
    <div class="stat-large">강남/서초</div>
  </div>
</div>

---

# 📋 Slide 2: 데이터 개요 및 하이라이트

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">평균 보증금</div>
    <div class="stat-large" style="font-size: 2.2em;">6,895만</div>
    <p>입지 간 격차 매우 큼</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">평균 월세</div>
    <div class="stat-large" style="font-size: 2.2em;">534만</div>
    <p>고정비 부담 높은 편</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 2;">
    <h2>📍 주요 위치 스냅샷</h2>
    <p>역삼, 강남, 신논현 초역세권 테헤란로 핵심 축 집중 분석</p>
    <p style="font-size: 0.8em; opacity: 0.8;">핵심 입지와 이면 도로 입지 간의 위계가 철저히 나뉘어 있음을 시사합니다.</p>
  </div>
</div>

---

# 📊 Slide 3: 보증금 및 월세 양극화

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 3; grid-row: span 4;">
    <div class="label">Top 10% 보증금</div>
    <div class="stat-large">1.5억+</div>
    <div class="label">Top 10% 월세</div>
    <div class="stat-large">1,000만+</div>
  </div>
  <div class="cell cell-warm" style="grid-column: span 3; grid-row: span 2;">
    <h2>💡 비즈니스 통찰</h2>
    <p>단순 판매를 넘어 브랜드 가치를 증명하는 '플래그십 스토어' 요충지</p>
  </div>
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 2;">
    <p>목적에 따른 타겟팅 필요:<br><b>브랜드 홍보 vs 실질 이익</b></p>
  </div>
</div>

---

# 📊 Slide 4: 면적 및 관리비 특성

<div class="grid-container">
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">면적 중앙값</div>
    <div class="stat-large">102㎡</div>
    <div class="label">약 30평</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 2;">
    <h2>🏢 소규모 최적화</h2>
    <p>IT, 뷰티 등 고부가가치 업종에 최적화된 집약적 공간 구조</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 2;">
    <div class="label">평균 관리비</div>
    <div class="stat-large">60만 원대</div>
    <p>월세의 10~15% 수준. 실질 현금 흐름 분석 시 필수 고려 사항</p>
  </div>
</div>

---

# 🏗️ Slide 5: 업종 및 시장 구조

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 2;">
    <h2>🏢 공간의 유연성</h2>
    <p>'기타창업모음', '다용도점포' 등 트렌드 민감 업종 대다수</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 2; grid-row: span 4;">
    <div class="label">임대 비율</div>
    <div class="stat-large">99%</div>
    <p>수익형 자산으로서의 압도적 안정성</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 4; grid-row: span 2;">
    <p>오프라인 공간이 '판매'에서<br><span style="color:#E8FF3B;">'체험 및 서비스'</span> 중심으로 재편</p>
  </div>
</div>

---

# 🔍 Slide 6: 키워드 분석 (TF-IDF)

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/tfidf_keywords.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">핵심 키워드</div>
    <p>#무권리<br>#역세권<br>#인테리어완비</p>
  </div>
  <div class="cell cell-coral" style="grid-column: span 2; grid-row: span 2;">
    <p>초기 투자비(CapEx)를 줄이려는 실속형 수요 증가</p>
  </div>
</div>

---

# 📈 Slide 7: [시각화] 면적 대비 월세 상관관계

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/scatter_size_rent.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 4;">
    <h2>💡 입지 특이점</h2>
    <p>면적은 좁지만 월세가 높은 <b>'골든 존'</b> 존재</p>
    <p style="font-size: 0.9em; opacity: 0.8;">면적의 경제보다 '입지의 경제'가 강력하게 작용</p>
  </div>
</div>

---

# 💰 Slide 8: [시각화] 업종별 평균 보증금

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 6; grid-row: span 3; padding: 0; overflow: hidden;">
    <img src="../images/barh_biz_deposit.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 1;">
    <p>레스토랑/주점 등 <b>시설 비중 큰 업종</b>일수록 원상복구 리스크로 인한 고액 보증금 형성</p>
  </div>
</div>

---

# 🏢 Slide 9: [시각화] 층별 가치 분포 비교

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 3; grid-row: span 3; padding: 0; overflow: hidden;">
    <img src="../images/scatter_dep_rent_floor.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">1층</div>
    <p>압도적 접근성 및 프리미엄</p>
  </div>
  <div class="cell cell-teal" style="grid-column: span 3; grid-row: span 1;">
    <div class="label">지하/상층부</div>
    <p>공간 효율성 및 고정비 절감</p>
  </div>
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 1;">
    <p>목적형 방문 업종은 상층부 선택으로 <b>수익성 극대화</b> 전략 유효</p>
  </div>
</div>

---

# 🚉 Slide 10: [시각화] 지하철역별 공급 현황

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/bar_subway_count.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-coral" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">Hotspots</div>
    <p>강남, 역삼, 신논현</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">Strategy</div>
    <p>틈새 역세권 블루오션 공략 제언</p>
  </div>
</div>

---

# 🌟 Slide 11: [시각화] 매물 인기도 분석

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/hexbin_popularity.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 4;">
    <h2>🎯 킬러 조건</h2>
    <p>단순 노출보다 '무권리' 등 파격적 조건이 <b>실제 계약 의지(즐겨찾기)</b> 유도</p>
    <p style="font-size: 0.9em; opacity: 0.7;">고객의 뇌리에 꽂힐 핵심 조건을 전면에 내세울 것</p>
  </div>
</div>

---

# 📏 Slide 12: [시각화] 면적당 가격 효율성

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/hist_area_price.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-yellow" style="grid-column: span 2; grid-row: span 2;">
    <div class="label">합리적 구간</div>
    <div class="stat-large">90~192</div>
  </div>
  <div class="cell cell-white" style="grid-column: span 2; grid-row: span 2;">
    <p>시세 구간 이탈 매물은 <b>건물 하자 심층 검토</b> 필요</p>
  </div>
</div>

---

# ⚠️ Slide 13: [시각화] 보증금 데이터 이상치

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/box_deposit.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-navy" style="grid-column: span 2; grid-row: span 4;">
    <h2>🏆 이중 시장</h2>
    <p>프라임 리그 vs 일반 리그</p>
    <p style="font-size: 0.9em; opacity: 0.7;">자본 조달 능력에 맞는 철저한 포지셔닝 필수</p>
  </div>
</div>

---

# 💸 Slide 14: [시각화] 월세 데이터 이상치

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/box_rent.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-coral" style="grid-column: span 2; grid-row: span 4;">
    <h2>📢 안테나숍</h2>
    <p>월세 1,000만 이상은 마케팅 비용 성격</p>
    <p style="font-size: 0.9em; opacity: 0.8;">매출 대비 임대료 15% 이내 매물 선별</p>
  </div>
</div>

---

# 📐 Slide 15: [시각화] 매물 면적 분포

<div class="grid-container">
  <div class="cell cell-white" style="grid-column: span 4; grid-row: span 4; padding: 0; overflow: hidden;">
    <img src="../images/hist_size.png" style="width: 100%; height: 100%; object-fit: contain;">
  </div>
  <div class="cell cell-teal" style="grid-column: span 2; grid-row: span 4;">
    <h2>📦 공간 분할</h2>
    <p>16~46평 집중</p>
    <p style="font-size: 0.9em; opacity: 0.8;">흔한 평수일수록 <b>차별화된 컨셉</b>으로 승부해야 함</p>
  </div>
</div>

---

# 💡 Slide 16: 결론 및 종합 전략 제언

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">01. 현금 흐름</div>
    <p>무권리 매물 선점으로 초기 리스크 최소화</p>
  </div>
  <div class="cell cell-yellow" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">02. 입지 우선</div>
    <p>면적 타협하더라도 초역세권 핵심 동선 확보</p>
  </div>
  <div class="cell cell-teal" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">03. 출구 전략</div>
    <p>다용도 특성 활용, 업종 변경 용이한 계약</p>
  </div>
  <div class="cell cell-warm" style="grid-column: span 3; grid-row: span 2;">
    <div class="label">04. 데이터 협상</div>
    <p>객관적 지표 근거로 임대료 협상 우위 점유</p>
  </div>
</div>

---

# 🚀 숫자의 이면에 숨겨진 심리를 읽는 것
### 그것이 강남 상권 생존의 핵심 전략입니다.

<div class="grid-container">
  <div class="cell cell-navy" style="grid-column: span 6; grid-row: span 4;">
    <p style="font-size: 1.5em; text-align: center;">20년 경력 데이터 분석가 리포트<br><b>Nemo Real Estate Analytics</b></p>
    <hr style="border: 1px solid #E8FF3B; width: 50%;">
    <p style="text-align: center; opacity: 0.7;">데이터는 여러분의 가장 강력한 비즈니스 파트너입니다.</p>
  </div>
</div>
