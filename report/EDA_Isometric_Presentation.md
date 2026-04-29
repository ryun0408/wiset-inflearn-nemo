---
marp: true
theme: default
paginate: true
header: 'Nemo Analytics - Isometric 3D Flat Style'
footer: 'Data Architecture & Insights'
backgroundColor: #1E1E2E
style: |
  @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
  @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&display=swap');
  
  section {
    font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    background-color: #1E1E2E;
    color: #FFFFFF;
    padding: 50px 70px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  h1 { 
    font-family: 'Barlow Condensed', sans-serif;
    color: #FFFFFF;
    font-size: 3.8em;
    text-transform: uppercase;
    margin-bottom: 0.1em;
    letter-spacing: -1px;
    font-weight: 800;
  }
  
  h2 {
    font-family: 'Pretendard', sans-serif;
    color: #A594FF;
    font-size: 1.8em;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 30px;
  }

  .iso-layout {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 75%;
    gap: 50px;
  }

  .iso-visual {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .iso-content {
    flex: 1.2;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* Isometric Block System */
  .block-group {
    position: relative;
    width: 250px;
    height: 250px;
  }

  .cube {
    position: absolute;
    width: 120px;
    height: 80px;
    background: #6254E8; /* Right face */
  }

  .cube::before {
    content: '';
    position: absolute;
    left: -30px;
    width: 30px;
    height: 100%;
    background: #4A3FCC; /* Left face */
    transform: skewY(45deg);
    transform-origin: right;
  }

  .cube::after {
    content: '';
    position: absolute;
    top: -30px;
    width: 100%;
    height: 30px;
    background: #7C6FFF; /* Top face */
    transform: skewX(45deg);
    transform-origin: bottom;
  }

  .cube-highlight::after {
    background: #A594FF !important;
  }

  .stat-box {
    background: rgba(124, 111, 255, 0.15);
    border-left: 5px solid #A594FF;
    padding: 25px;
    margin: 12px 0;
    border-radius: 0 12px 12px 0;
  }

  .stat-value {
    font-size: 2.8em;
    font-weight: 800;
    color: #E8FF3B;
    line-height: 1.1;
  }

  .label {
    font-size: 0.9em;
    color: #A594FF;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 700;
    margin-bottom: 5px;
  }

  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    width: 100%;
  }

  footer { font-size: 0.5em; color: #6254E8; }
  header { font-size: 0.6em; color: #A594FF; opacity: 0.5; }
  
  img {
    border: 3px solid #6254E8;
    box-shadow: 20px 20px 0 rgba(124, 111, 255, 0.15);
    max-height: 100%;
    max-width: 100%;
    object-fit: contain;
    border-radius: 12px;
  }
---

# 🎯 EDA REPORT
## Nemo Real Estate Analytics

<div class="iso-layout">
  <div class="iso-content">
    <p style="font-size: 1.4em; line-height: 1.5; font-weight: 600;">20년 경력의 데이터 사이언티스트가<br>분석한 강남/서초 상권의 구조적 통찰</p>
    <div class="stat-box">
      <div class="label">Analysis Target</div>
      <div class="stat-value">673 SAMPLES</div>
    </div>
    <p style="opacity: 0.7; font-size: 1em; margin-top: 10px;">건축적 관점과 데이터 공학적 관점을 결합한<br>입체적 시장 분석 리포트입니다.</p>
  </div>
  <div class="iso-visual">
    <div class="block-group">
      <div class="cube cube-highlight" style="top: 60px; left: 80px; z-index: 3;"></div>
      <div class="cube" style="top: 120px; left: 40px; z-index: 2;"></div>
      <div class="cube" style="top: 180px; left: 0px; z-index: 1;"></div>
    </div>
  </div>
</div>

---

# 📋 OVERVIEW
## 데이터 개요 및 하이라이트

<div class="iso-layout">
  <div class="iso-visual">
    <div class="block-group">
      <div class="cube" style="top: 80px; left: 100px; height: 120px; background: #FF6B6B;"></div>
      <div class="cube" style="top: 140px; left: 40px; height: 60px;"></div>
    </div>
  </div>
  <div class="iso-content">
    <div class="stat-box">
      <div class="label">Avg Deposit</div>
      <div class="stat-value">6,895만</div>
    </div>
    <div class="stat-box">
      <div class="label">Avg Monthly Rent</div>
      <div class="stat-value">534만</div>
    </div>
    <p style="font-size: 1.1em; font-weight: 500; margin-top: 15px;">입지 간의 위계가 명확하며<br>고정비 부담이 높은 구조입니다.</p>
  </div>
</div>

---

# 📊 POLARIZATION
## 보증금 및 월세 양극화 분석

<div class="iso-layout">
  <div class="iso-content">
    <div class="stat-box">
      <div class="label">Top 10% Cluster</div>
      <div class="stat-value">1.5억 / 1,000만+</div>
    </div>
    <p style="margin-top: 25px; font-size: 1.15em; line-height: 1.6;"><b>핵심 통찰:</b><br>단순 판매를 넘어 브랜드 가치를 증명하는<br><span style="color: #E8FF3B; font-weight: 700;">'플래그십' 요충지</span>로서의 성격이 강함</p>
  </div>
  <div class="iso-visual">
    <div class="block-group">
      <div class="cube cube-highlight" style="top: 30px; left: 100px; height: 180px;"></div>
      <div class="cube" style="top: 160px; left: 20px; height: 40px; opacity: 0.5;"></div>
    </div>
  </div>
</div>

---

# 🏗️ STRUCTURE
## 업종 및 시장 구조 분석

<div class="iso-layout">
  <div class="iso-visual">
    <div class="block-group">
      <div class="cube" style="top: 100px; left: 50px; width: 200px;"></div>
      <div class="cube cube-highlight" style="top: 160px; left: 100px; width: 100px;"></div>
    </div>
  </div>
  <div class="iso-content">
    <div class="label">임대 비율</div>
    <div class="stat-value" style="font-size: 4.5em; margin-bottom: 15px;">99%</div>
    <p style="font-size: 1.3em; line-height: 1.6; font-weight: 600;">오프라인 공간의 기능이<br><span style="color: #E8FF3B;">'판매'에서 '체험'</span>으로<br>완전한 패러다임 전환</p>
  </div>
</div>

---

# 🔍 KEYWORDS
## TF-IDF 키워드 분석

<div class="iso-layout">
  <div class="iso-content" style="flex: 0.9;">
    <div class="stat-box">
      <div class="label">Core Tag</div>
      <div style="font-size: 1.8em; font-weight: 800; color: #4ECDC4; margin-top: 8px;">#무권리 #역세권</div>
    </div>
    <p style="font-size: 1.1em; line-height: 1.5; margin-top: 15px;">CapEx 절감을 노리는<br>실속형 창업 수요가<br>키워드에 그대로 투영됨</p>
  </div>
  <div class="iso-visual" style="flex: 1.3;">
    <img src="../images/tfidf_keywords.png">
  </div>
</div>

---

# 📈 CORRELATION
## 면적 대비 월세 상관관계

<div class="iso-layout">
  <div class="iso-visual" style="flex: 1.3;">
    <img src="../images/scatter_size_rent.png">
  </div>
  <div class="iso-content" style="flex: 0.9;">
    <h2 style="margin-bottom: 10px;">'골든 존' 포착</h2>
    <p style="font-size: 1.2em; line-height: 1.5;">면적의 경제보다<br><b>'입지의 경제'</b>가 압도적</p>
    <div class="stat-box">
      <div class="label">Efficiency</div>
      <div class="stat-value">HIGH</div>
    </div>
  </div>
</div>

---

# 💰 CATEGORY
## 업종별 평균 보증금 추이

<div class="iso-layout" style="flex-direction: column; justify-content: center;">
  <div style="height: 70%; width: 100%; display: flex; justify-content: center;">
    <img src="../images/barh_biz_deposit.png" style="width: auto;">
  </div>
  <p style="text-align: center; width: 90%; font-size: 1.2em; font-weight: 600; margin-top: 30px; line-height: 1.5;">
    시설 비중이 큰 업종일수록 원상복구 리스크를 반영한 <span style="color:#FF6B6B;">고액 보증금</span> 형성
  </p>
</div>

---

# 🏢 FLOORS
## 층별 가치 분포 비교

<div class="iso-layout">
  <div class="iso-content" style="flex: 0.9;">
    <div class="stat-box">
      <div class="label">1F Premium</div>
      <div class="stat-value">MAXIMUM</div>
    </div>
    <p style="font-size: 1.1em; line-height: 1.6; margin-top: 15px;">목적형 방문 업종은<br>상층부 선택을 통해<br><b>고정비 효율화</b>를<br>꾀하는 것이 유리</p>
  </div>
  <div class="iso-visual" style="flex: 1.3;">
    <img src="../images/scatter_dep_rent_floor.png">
  </div>
</div>

---

# 🚉 SUBWAY
## 지하철역별 매물 공급 현황

<div class="iso-layout">
  <div class="iso-visual" style="flex: 1.3;">
    <img src="../images/bar_subway_count.png">
  </div>
  <div class="iso-content" style="flex: 0.9;">
    <div class="stat-box">
      <div class="label">Hot Zones</div>
      <div style="font-size: 1.8em; font-weight: 800; color: #E8FF3B; margin-top: 5px;">강남 / 역삼 / 신논현</div>
    </div>
    <p style="font-size: 1.1em; line-height: 1.5; margin-top: 15px;">테헤란로 핵심 축을 중심으로<br>공급이 밀집된 구조적 특징</p>
  </div>
</div>

---

# 📐 EFFICIENCY
## 면적당 가격 효율성 분포

<div class="iso-layout">
  <div class="iso-content">
    <div class="stat-box">
      <div class="label">Market Price</div>
      <div class="stat-value">90 ~ 192</div>
    </div>
    <p style="font-size: 1.1em; line-height: 1.5; margin-top: 15px;">분포 범위를 벗어난 매물은<br>입지적 특수성 혹은<br><span style="color:#FF6B6B; font-weight: 700;">권리 관계 검토</span> 필수</p>
  </div>
  <div class="iso-visual">
    <img src="../images/hist_area_price.png">
  </div>
</div>

---

# 💡 STRATEGY
## 결론 및 종합 전략 제언

<div class="iso-layout" style="height: 70%;">
  <div class="grid-2">
    <div class="stat-box">
      <div class="label">01. CASH FLOW</div>
      <p style="font-size: 1.1em; font-weight: 600;">무권리 매물 선점으로<br>초기 리스크 최소화</p>
    </div>
    <div class="stat-box">
      <div class="label">02. LOCATION</div>
      <p style="font-size: 1.1em; font-weight: 600;">초역세권 핵심 동선 위주<br>입지 위계 분석</p>
    </div>
    <div class="stat-box">
      <div class="label">03. EXIT PLAN</div>
      <p style="font-size: 1.1em; font-weight: 600;">다용도 특성 활용,<br>업종 변경 용이성 확보</p>
    </div>
    <div class="stat-box">
      <div class="label">04. DATA-DRIVEN</div>
      <p style="font-size: 1.1em; font-weight: 600;">객관적 지표 근거<br>임대료 협상 우위 점유</p>
    </div>
  </div>
</div>

---

# 🚀 SYSTEM ARCHITECTURE
## Data is your partner.

<div class="iso-layout">
  <div class="iso-visual">
    <div class="block-group">
      <div class="cube" style="top: 40px; left: 100px;"></div>
      <div class="cube cube-highlight" style="top: 100px; left: 160px;"></div>
      <div class="cube" style="top: 160px; left: 100px;"></div>
      <div class="cube" style="top: 100px; left: 40px;"></div>
    </div>
  </div>
  <div class="iso-content">
    <h1 style="font-size: 3.2em; letter-spacing: -2px;">THANK YOU</h1>
    <p style="color: #A594FF; font-weight: 800; font-size: 1.5em; margin-bottom: 5px;">Nemo Real Estate Analytics</p>
    <p style="opacity: 0.7; font-size: 1.1em;">숫자 너머의 가치를 설계합니다.</p>
  </div>
</div>
