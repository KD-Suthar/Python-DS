"""Link to questions - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md"""
#1 Problem 1 
arr = []

with open("nyc_weather.csv","r") as file:
    #reader = csv.reader(file)
    next(file,None)
    for line in file:
        words = line.split(',')
        arr.append(int(words[1]))

print(arr)
print(sum(arr[0:7])/len(arr[0:7]))

print(max(arr[0:10]))

#2 question

weather_info = {}

with open("nyc_weather.csv","r") as file:
    #reader = csv.reader(file)
    next(file,None)
    for line in file:
        words = line.split(',')
        weather_info[words[0]] = int(words[1])
    
print(f'Weather on Jan 9 -',weather_info['Jan 9'])
print(f'Weather on Jan 4 -',weather_info['Jan 4'])

##3 Question Poem

poem_count = {}

with open("poem.txt","r") as file:
    for line in file:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n','')
            if word in poem_count:
                poem_count[word] += 1
            else:
                poem_count[word] = 1

print(poem_count)
