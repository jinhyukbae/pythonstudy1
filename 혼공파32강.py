# 딕셔너리
# {}를 사용
# 키: 값 쌍을 여러 개 입력
# 키: 숫자, 문자열, 불, 튜플
# 값: 모든 값

pro = {"제품명": "건망고 슬라이스", "가격": 4000, "분류": "식품", 10: 20, "원산지": "태국"}
for flower in pro:
  print(flower)  #왼쪽 값 출력
  print(pro[flower])  #오른쪽 값 출력
  print("-", *20)  # ----- 출력후 다시 처음부터 반복
  #

products = [{
  "제품명": "건망고 슬라이스",
  "가격": 4000,
  "분류": "식품",
  10: 20,
  "원산지": "태국"
}, {
  "제품명": "건망고 슬라이스",
  "가격": 4000,
  "분류": "식품",
  10: 20,
  "원산지": "태국"
}]

for product in products:
  for key in product:
    print(key)
    print(product[key])
    print()
  print("-" * 20)

#product = {
#"제품명":"건망고 슬라이스",
#"가격" : 4000,
#"분류" : "식품",
#10: 20,
#"원산지" : "태국"
#}

#print(product["제품명"]) #"건망고 슬라이스"
#print(product["가격"]) #4000
#print(product["분류"]) #"식품"
#print(product[10]) # 20
#print(product["원산지"])

#for 반복변수 in 반복할수있는것:
#  복합구문
# 딕셔너리도 반복가능 product 넣고 반복변수엔 key를 복합구문엔 product[key]

#for key in product:
#print(key) # 앞에있는 키  제품명 가격 등
#print(product[key]) # 뒤에있는 값 건망고슬라이스 4000 등
#print("-" * 20)
