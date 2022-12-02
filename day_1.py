
#%% Part 1, Draft 2solution 1
with open('day_1.txt','r') as calories_count: 
    calories = calories_count.readlines()
    sum =0
    max_calories = sum

for i in range(len((calories))):
    if calories[i]!='\n':
        calories[i].replace('\n','')
        sum =sum + int(calories[i])
    else: 
        sum = 0
        continue
    if sum>max_calories:
        max_calories = sum 
print(max_calories)

#%% Part 1, Draft 2
for i in range(len(calories)):
    if calories[i]!='\n':
        sum = sum +int(calories[i])
        if sum>max_calories:
            max_calories = sum
    else: 
        sum = 0
print(sum)

#%% Using enumerate, did not find much difference anyhow. 
with open('day_1.txt','r') as calories_count: 
    calories = calories_count.readlines()
    sum =0
    max_calories = sum
    top_3 = []
    test = []

for index, calories_ in enumerate(calories):
    if calories_!='\n':
        calories_.replace('\n','')
        sum =sum + int(calories_)
        test.append(sum)
    else: 
        sum = 0
        continue
    if sum>max_calories:
        max_calories = sum
        

test.sort(reverse = True)
i = 0 
p2 = 0
while i<3:
    p2 = p2 +test[i]
    i += 1


print(max_calories)
print(p2)

# %%
