from random import shuffle, choice # shuffle: list 내부의 값의 인덱스 값을 섞어준다. / choice: 리스트 값 중 랜덤하게 선택하게 해준다.

count = 0
for i in range(100001): 
# 문과 선택 생성

  doors = [0,1,0]
  shuffle(doors)

  choice_result = choice(doors)

#choice_result = doors.index(choice(doors))

#사용자가 선택한 결과 보여주고 각 확률별 카운트하기

#del new_doors[int(choice_result)]

#new_doors
  choice_result_index = doors.index(choice_result)

  option_list = [0,1,2]
  option_list.remove(choice_result_index)
  option = option_list


  if doors[int(option[0])] == 0:
    del doors[int(option[0])] 
  
  else:
    del doors[int(option[1])]

#결과값 바꾸기
  old_choice_index = doors.index(choice_result)
  del doors[old_choice_index]

  if doors[0] == 1:
    count +=1

  else: 
    count = count

result1 = count/100000

count1 = 0
for i in range(100001): 
# 문과 선택 생성

  doors = [0,1,0]
  shuffle(doors)

  choice_result = choice(doors)

#choice_result = doors.index(choice(doors))

#사용자가 선택한 결과 보여주고 각 확률별 카운트하기

#del new_doors[int(choice_result)]

#new_doors
  choice_result_index = doors.index(choice_result)

  option_list = [0,1,2]
  option_list.remove(choice_result_index)
  option = option_list



  if doors[int(option[0])] == 0:
    del doors[int(option[0])] 
  
  else:
    del doors[int(option[1])]

#결과값 안바구기
  if int(choice_result) == 1:
    count1+=1
  else:
    count1=count1

result2 = count1/100000
print("change: "+ str(result1)+", unchange: "+str(result2))
