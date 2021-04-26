list1 = ["AAA", "BBB"]
print (list1)
for item in list1:  #循环打印list的每个元素
    print(item)
    
# 转小写方法1
list2 = ["AAA", "BBB"]
lower_list1 = []
for item in list2:  #循环遍历list的每个元素
    lower_list1.append(item.lower())
print (lower_list1)

    
# 转小写方法2
list3 = ["AAA", "BBB"]
lower_list2= [item.lower() for item in list3]
print (lower_list2)       
    

#字典的每一个元素都是成对出现
# key:value
dict1 = {"file1":["AAA","BBB"], 
         "file2":["CCC","DDD"]}
print (dict1)   #打印整个字典
for key in dict1:       #循环遍历整个字典，key是字典的每一个元素
    print (dict1[key])  #打印字典的元素key对应的value 
    dict1[key] = ["change", "dict"] #修改字典key对应的value
    print(dict1[key])   #打印修改后的结果

print (dict)
    
