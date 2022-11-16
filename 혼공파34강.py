#빈도를 셀 때 
numbers = [1,2,6,8,4,3,2,1,9,5]
#4,9,7,2,1,3,5,4,8,9,7,2,3
counter = {}

# {1} 요소으 ㅣ출현 확인 코드
#for number in numbers:
  #counter[number] = 0
  #numbers의 요소를 number로 하나하나 꺼내면서 요소 옆에 0을 부과 1:0 2:0 이런 식


# 2 해당 요소의 빈도 확인 코드   
#for number in numbers:
  #counter[number] += 1 #counter[number] = counter[number] + 1
  #위에서 카운터넘버가 0이였고 0+1을 하니까 1
# 위에 키:값중 값에 해당하는 1:0 2:0 에 +1씩 추가함 1:1 2:1 6:1 이런 식


#3 통합

for number in numbers:
  if number not in counter: #카운터에 넘버라는 키가 없다면
    counter[number] = 0 #counter[number] = 값 
  counter[number] += 1    

print(counter)  

#1.numbers라는 리스트가 생기고 counter라는 딕셔너리가 생기고 반복문 진입
#2.처음엔 number에 1이 들어가고 1이 들어간 시점엔 counter에 1이 없으므로 값이 0이됨
#3.아래 counter[number]= counter[number] + 1에 counter[number]가 0이므로 0+1 해서 값이 1이됨 (키값은 그대로 1이여서 1:1 처럼 출력)
# 반복하다가 2가 또 나오면 2:1인 상태이므로 if number not in counter가 false 이므로 counter[number] = 0이 실행되지 않고 바로 counter[number] += 1가 실행되므로 1+1을 해서 값이 2가 나옴 키 2 값 2 2:2

#히스토그램

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
  if number not in counter:
    counter[number] = ""
  counter[number] += "■"

  for key in sorted(counter.keys()):
    print(f"{key}: {counter[key]}")  

# 연습문제


#정보창 
character = {
  "name": "기사 ",
  "level": 12,
  "items": {
    "sword": "불꽃의 검",
    "armor": "풀플레이트"
},
"skill": ["베기", "세게 베기", "아주 세게 베기"]
}


for key in character:
  if type(character[key]) is dict:
    print(character[key])    
    for 키 in character[key]:
      print(f"{키} : {character[key][키]}")
  elif type(character[key]) is list:
    for 요소 in character[key]:
      print(f"skill : {요소}")
    
  else:
    print(f"{key} : {character[key]}")