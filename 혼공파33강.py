product = {
  "name": "7D 건조 망고",
  "type": "당절임",
}
#요소의 값을 변경하는 방법
product["name"] = "8D 건조 망고"
#요소를 추가하는 방법
product["price"] = 4000
#요소를 제거하는 방법
del product["type"]
#키의 존재 확인하는 방법 in

#if "price" in product:
  #print(product["price"])
#else:
  #print("가격 요소가 없습니다")

if product.get("price") !=None: #price라는 요소가 none이 아니라면
  print(product["price"]) #price의 값을 출력 4000 오른쪽
else:
  print("가격 요소가 없습니다") #아니면 이거 출력 
  
#get()
print(product.get("name")) #name 이라는 요소의 값을 꺼내서 출력함 건조 망고
print(product.get("price")) #존재 하지 않는 키를 입력하면 None을 출력
#print(product)

#확인문제 1-1
dict_a = {}
dict_a["name"] = "구름"
print(dict_a) # {"name":"구름"}

dict_a = {"name": "구름"}
del dict_a["name"] #name 값 전체를 지움 오른쪽 구름 까지 
print(dict_a)

# 구름 5살
# 초코 3살 이런식으로 출력하기 

pets = [
  {"name": "구름", "age": 5},
  {"name": "초코", "age": 3},
  {"name": "아지", "age": 1},
  {"name": "호랑이", "age": 1}
  
]

print("#우리 동네 애완동물들")

for pet in pets:
    print(f"{pet['name']} {pet['age']}살 입니다.")