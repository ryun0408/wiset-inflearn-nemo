"""index.html에 보고서 인사이트를 주입하는 스크립트"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 각 차트 이미지 태그 뒤에 인사이트 블록을 삽입하는 함수
def insight_block(text):
    return f'''<div class="mt-4 p-4 rounded-lg" style="background:rgba(56,189,248,0.07);border-left:3px solid #38bdf8;">
<p class="text-sm text-slate-300 leading-relaxed">{text}</p></div>'''

replacements = [
    # 업종별 매물 분포
    (
        "기타창업모음과 다용도점포가 상위권을 차지하며 유연한 공간 수요를 반영합니다.</p>",
        "기타창업모음과 다용도점포가 상위권을 차지하며 유연한 공간 수요를 반영합니다.</p>" +
        insight_block("업종 분포에서 '기타창업모음'과 '다용도점포'의 비중이 압도적으로 높습니다. 이는 강남 지역 상권이 특정 업종에 고착화되기보다, 시장 트렌드에 따라 유연하게 변모하는 다목적 공간에 대한 수요가 매우 높음을 시사합니다. '커피점/카페'와 '한식점'이 상위권에 포진한 것은 직장인 배후 상권으로서의 견고함을 보여줍니다. 신규 진입 시 일반 판매업보다는 서비스와 식음료가 결합된 형태가 유리하며, 주변 업종과의 시너지를 고려한 전략적 배치가 필수적입니다.")
    ),
    # 지하철역 접근성
    (
        "강남/역삼/신논현역 인근 도보 5분 이내 매물이 압도적으로 밀집되어 있습니다.</p>",
        "강남/역삼/신논현역 인근 도보 5분 이내 매물이 압도적으로 밀집되어 있습니다.</p>" +
        insight_block("인근 지하철역 분포 데이터는 '강남-역삼-신논현'으로 이어지는 테헤란로 핵심 축의 매물 집중 현상을 명확히 보여줍니다. 비즈니스 관점에서 역과의 거리는 단순한 물리적 거리를 넘어 브랜드 신뢰도와 인력 채용의 용이성까지 직결되는 핵심 변수입니다. 임대료가 다소 높더라도 초역세권 입지를 확보하는 것이 장기적 운영 효율성 측면에서 유리하며, 이 지역 매물 회전율이 높은 이유이기도 합니다.")
    ),
    # 거래 형태 비율
    (
        "99% 이상이 임대 매물로, 수익형 자산으로서의 성격이 강합니다.</p>",
        "99% 이상이 임대 매물로, 수익형 자산으로서의 성격이 강합니다.</p>" +
        insight_block("매매 물건이 극도로 희소하고 99% 이상이 임대 매물인 현상은 이 지역 상업용 부동산의 자산 가치가 매우 안정적임을 시사합니다. 소유주들이 매각보다 꾸준한 월세 수익을 선호하며, 이는 시장 진입 장벽을 높입니다. 임차인 입장에서는 장기 임대차 계약 시 유리한 조건을 선점하는 것이 사업 연속성을 확보하는 핵심 전략입니다.")
    ),
    # TF-IDF 키워드
    (
        "'무권리', '역세권', '인테리어' 등이 핵심 소구점으로 나타납니다.</p>",
        "'무권리', '역세권', '인테리어' 등이 핵심 소구점으로 나타납니다.</p>" +
        insight_block("TF-IDF 분석에서 '무권리', '역세권', '인테리어' 등의 키워드가 최상위권을 점유합니다. '무권리' 키워드의 부상은 고비용 상권에서 초기 투자비(CapEx)를 절감하려는 임차인의 강한 욕구를 반영합니다. '인테리어 완비'나 '깔끔한' 등의 키워드는 즉시 영업 개시가 가능한 매물 선호 트렌드를 보여줍니다. 매물 등록 시 이러한 핵심 키워드를 전략적으로 노출하는 것이 조회수와 실제 계약 전환율을 높이는 데 결정적 역할을 합니다.")
    ),
    # 조회수/즐겨찾기
    (
        "단순 노출보다 매물의 조건적 우월성이 실제 관심(즐겨찾기)으로 이어집니다.</p>",
        "단순 노출보다 매물의 조건적 우월성이 실제 관심(즐겨찾기)으로 이어집니다.</p>" +
        insight_block("조회수와 즐겨찾기의 상관계수는 약 0.46으로, 단순 노출보다 임차인의 니즈를 충족하는 '조건의 우월성'이 실제 계약 의향(즐겨찾기)으로 이어집니다. 시장 가격 대비 현저히 저렴하거나 독보적인 입지 조건을 갖춘 매물에서 즐겨찾기가 급증하는 현상이 관찰됩니다. 마케팅 시 단순 조회수 증대보다 타겟 고객이 즐겨찾기를 누를 '킬러 조건'을 전면에 내세우는 전략이 필요합니다.")
    ),
]

# 차트 섹션에 추가할 인사이트 (이미지 다음 위치 기준)
# 면적 대비 월세
old = 'scatter_size_rent.png\'" class="w-full h-auto rounded-lg">\n                     </div>'
new = 'scatter_size_rent.png\'" class="w-full h-auto rounded-lg">' + insight_block("면적과 월세는 전체적으로 양의 상관관계를 보이나, 일부 소형 매물에서 월세가 급격히 높은 '입지 특이점'들이 관찰됩니다. 강남 핵심 역세권 1층 점포는 면적이 좁더라도 유동인구와 가시성이 담보된다면 대형 평수 이상의 임대 가치를 창출합니다. 창업자는 본인 업종이 '면적 집약형'인지 '입지 집약형'인지 냉철히 판단해야 합니다.") + '\n                     </div>'
html = html.replace(old, new)

# 업종별 평균 보증금
old = 'barh_biz_deposit.png\'" class="w-full h-auto rounded-lg">\n                     </div>'
new = 'barh_biz_deposit.png\'" class="w-full h-auto rounded-lg">' + insight_block("레스토랑과 기타주점 업종에서 압도적으로 높은 평균 보증금이 형성됩니다. 주방 설비 및 대규모 인테리어가 수반되는 업종 특성상, 임대인은 원상복구 비용과 공실 리스크를 보증금으로 담보하려 합니다. 예비 창업자는 본인 업종이 상위권이라면, 초기 자본금 산정 시 보증금 비중을 일반 업종보다 1.5~2배 높게 설정해야 합니다.") + '\n                     </div>'
html = html.replace(old, new)

# 층별 임대료 분포
old = 'scatter_dep_rent_floor.png\'" class="w-full h-auto rounded-lg">\n                     </div>'
new = 'scatter_dep_rent_floor.png\'" class="w-full h-auto rounded-lg">' + insight_block("1층 매물은 보증금과 월세 모두에서 타 층 대비 월등히 높은 가격대를 형성하며 '1층 불패'의 법칙을 수치로 재확인합니다. 지하 1층이 일부 상층부보다 높은 월세를 형성하는 경우는 헬스장 등 대형 평수 업종이 지하를 선호하기 때문입니다. 가시성이 불필요한 목적형 방문 업종(예약제 스튜디오, 전문 상담실)은 상층부를 선택하여 고정비를 낮추는 가성비 전략이 유효합니다.") + '\n                     </div>'
html = html.replace(old, new)

# 단위 면적당 가격
old = 'hist_area_price.png\'" class="w-full h-auto rounded-lg">\n                     </div>'
new = 'hist_area_price.png\'" class="w-full h-auto rounded-lg">' + insight_block("면적당 가격(areaPrice)의 대다수 매물이 90~192 구간에 밀집되어 있어, 시장에서 형성된 '합리적 시세' 구간이 존재합니다. 최대값이 평균의 수십 배에 달하는 극단적 사례들은 대로변 초역세권 특수 매물로, 하이엔드 시장이 공존함을 보여줍니다. 평당 단가가 중앙값(127) 근처인 매물이 리스크가 낮으며, 현저히 낮은 매물은 권리금 유무나 건물 하자를 심층 검토해야 합니다.") + '\n                     </div>'
html = html.replace(old, new)

# 면적 분포 히스토그램
old = 'hist_size.png\'" class="w-full h-auto rounded-lg">\n                     </div>'
new = 'hist_size.png\'" class="w-full h-auto rounded-lg">' + insight_block("54㎡~152㎡(약 16~46평) 구간에 대부분의 매물이 집중되어, 강남 상가 건물이 소규모 분할 임대 전략을 취하고 있음을 시사합니다. 이 구간이 매물이 가장 풍부하여 선택의 폭이 넓지만 동시에 경쟁도 가장 치열합니다. 200㎡ 이상 대형 평수를 원한다면 매물 자체가 희소하므로 신축 빌딩 사전 임대 등 빠른 의사결정이 필요합니다.") + '\n                     </div>'
html = html.replace(old, new)

# 문자열 치환 적용
for old_str, new_str in replacements:
    html = html.replace(old_str, new_str)

# 종합 인사이트 섹션 — Data Explorer 앞에 삽입
insights_section = '''
        <!-- 종합 인사이트 섹션 -->
        <section class="mt-16">
            <h2 class="text-2xl font-bold mb-6 flex items-center">
                <span class="w-2 h-8 rounded mr-3" style="background:#a78bfa;"></span>
                20년 경력 데이터 분석가의 종합 인사이트
            </h2>
            <div class="space-y-6">
                <div class="glass-card p-6">
                    <h3 class="text-lg font-semibold mb-3" style="color:#a78bfa;">① 강남 상권의 이중 구조: '하이엔드'와 '마이크로'의 공존</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">본 시장은 월세 1,000만 원 이상의 하이엔드 시장과 300~500만 원 사이의 마이크로 시장으로 명확히 구분됩니다. 박스플롯의 수많은 이상치는 단순한 통계적 오류가 아니라, 강남대로변 랜드마크급 입지의 독점적 지위를 상징합니다. 이면 도로와 지하층의 20평 미만 소형 매물들은 스타트업, 공유 주방, 프라이빗 스튜디오 등 새로운 비즈니스 모델의 인큐베이터 역할을 합니다. 투자자와 창업자는 자산 규모에 따라 어떤 리그에 참여할 것인지 명확한 포지셔닝이 필요합니다.</p>
                </div>
                <div class="glass-card p-6">
                    <h3 class="text-lg font-semibold mb-3" style="color:#38bdf8;">② 데이터로 본 '입지 가치'의 재정의: 역세권 5분의 법칙</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">nearSubwayStation 데이터 분포는 강남 상권에서 '역세권'이 가지는 절대적 위상을 보여줍니다. 역삼역과 강남역 인근의 높은 매물 수와 인기도 지표는, 공급이 많음에도 수요가 이를 초과하는 '공격적 시장'임을 시사합니다. 차라리 면적을 줄이더라도 역세권 내 '핵심 동선'을 확보하는 것이 ROI 관점에서 우월한 전략입니다.</p>
                </div>
                <div class="glass-card p-6">
                    <h3 class="text-lg font-semibold mb-3" style="color:#34d399;">③ 업종 트렌드: 서비스와 경험 중심의 재편</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">'기타창업모음'과 '커피점/카페'의 높은 비중은 오프라인 공간의 기능 변화를 시사합니다. 단순 상품 판매는 온라인으로 빠르게 대체되고 있으며, 강남의 오프라인 상가는 '서비스 제공', '브랜드 체험', '비즈니스 네트워크'의 장으로 기능합니다. 신규 창업자는 단순 소매업보다 고부가가치 서비스가 결합된 융합 업종(뷰티+카페, 갤러리+바 등)을 고려할 만합니다.</p>
                </div>
                <div class="glass-card p-6">
                    <h3 class="text-lg font-semibold mb-3" style="color:#fb923c;">④ 리스크 요인 및 전략적 제언</h3>
                    <p class="text-sm text-slate-300 leading-relaxed mb-4">고비용 구조(고임대료, 고관리비)는 강남 상권의 가장 큰 위협 요인입니다. 데이터상 '무권리' 매물이 지속적으로 등장하는 것은 빠른 매물 순환과 동시에 실패 사례도 적지 않음을 암시합니다.</p>
                    <ul class="space-y-2 text-sm text-slate-300">
                        <li class="flex items-start gap-2"><span style="color:#38bdf8;">▶</span><span><strong class="text-slate-100">현금 흐름 최적화:</strong> 보증금과 권리금 등 초기 투자비용을 최소화할 수 있는 '무권리' 또는 '인테리어 완비' 매물을 우선순위에 두십시오.</span></li>
                        <li class="flex items-start gap-2"><span style="color:#38bdf8;">▶</span><span><strong class="text-slate-100">공간의 유연성 확보:</strong> 향후 업종 변경이나 전대(Sublease)가 용이한 구조의 매물을 선택하여 출구 전략(Exit Strategy)을 마련하십시오.</span></li>
                        <li class="flex items-start gap-2"><span style="color:#38bdf8;">▶</span><span><strong class="text-slate-100">데이터 기반 입지 분석:</strong> 조회수가 높지만 즐겨찾기가 적은 매물은 '허수'일 가능성이 높으므로 주의가 필요합니다.</span></li>
                    </ul>
                </div>
                <div class="glass-card p-6">
                    <h3 class="text-lg font-semibold mb-3" style="color:#f472b6;">⑤ 향후 전망: 테헤란로의 수직적 확장과 공간의 프리미엄화</h3>
                    <p class="text-sm text-slate-300 leading-relaxed">앞으로 강남/서초 상권은 테헤란로를 중심으로 수평적 확장보다 '수직적 확장(고층화, 지하화)'과 '공간의 프리미엄화'가 더욱 가속화될 것입니다. 1층 임대료가 한계치에 달함에 따라 독특한 컨셉을 가진 지하 및 상층부 매물의 가치가 재조명받을 것입니다. <span class="font-semibold text-slate-100">결론적으로, 강남 상가 시장은 '데이터가 승패를 결정하는 정밀한 시장'입니다.</span> 본 보고서의 분위수별 가격 지표와 업종별 면적 데이터를 비즈니스 모델 설계의 기준으로 삼는다면, 불확실한 시장 속에서도 성공적인 안착을 위한 강력한 나침반을 확보하게 될 것입니다.</p>
                </div>
            </div>
        </section>

'''

html = html.replace('        <!-- Data Explorer -->', insights_section + '        <!-- Data Explorer -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("인사이트 주입 완료!")
