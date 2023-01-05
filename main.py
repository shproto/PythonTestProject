import copy #for deep copy
dict1 = {
    "ip": "127.0.0.1",
    ("port"): {         #строго говоря не является кортежем, но обычной строкой. для кортежа надо запятую (4000, )
        "1":4000,
        "2":5000}
}
dict2 = dict(he=36, she=35, little1=7, little2=4)
print("dict1: ", dict1['port']['2'])
print("dict2: ", dict2)

#annotations
def get_dict() -> dict:
    return dict(one=1, two=[2, 22, 222], three=3, four=4)

a: dict = get_dict()
print(a.get("four", "есть в наличии"))
print(a.get("five", "nothing"))


# add key to dict
a["five"]=5
a.update({"six":6, "seven": 7})
print(a)

#del key from dict
del a["seven"]
print(r'"a after del a['seven']: ", a)
print("default a.pop message when nothing found: ", a.pop("seven", "nothing found"))

#check key in dict
print("seven" in a)
print("six" in a)

#copy a dict
b = a # this is a ling
print(f'a id: {id(a)}, b id: {id(b)}') # a and b are the same. The same cell in the memory
c = a.copy() #this is a  copy of a
#this is the same cell:
c['two'] = 22
print(id(a['two']), "a: ", a)
print(id(c['two']), "c: ", c)
d = copy.deepcopy(a) #deep copy
d['two'] = 222
print(id(a['two']),"a: ", a)
print(id(d['two']),"d: ", d)

print('stop row')