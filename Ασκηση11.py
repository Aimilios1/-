import json
file = open("dictionary.txt", "r")
cont = file.read()
diction = json.loads(cont)
file.close()
freq={}
def get_all_keys(diction):
    for k, value in diction.items():
        if type(value) is dict:
            get_all_keys(value)
            if (k in freq):
                freq[k] += 1
            else:
                freq[k]=1
        elif (k in freq):
            freq[k] += 1
        else:
            freq[k]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    get_all_keys(value[i])
get_all_keys(diction)
keyWithMaxValue = max(freq.items(), key=lambda x: x[1])
listOfKeysWithMaxFreq = list()
for key, value in freq.items():
    if value == keyWithMaxValue[1]:
        listOfKeysWithMaxFreq.append(key)
print(listOfKeysWithMaxFreq)
