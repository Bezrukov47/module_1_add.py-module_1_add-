grades = [[5,3,3,5,4], [2,2,2,3]],[4,5,5,2], [4,4,3],[5,5,5,4,5]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted (students)
print(sorted_students)
sorted_students = {'Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve'}
print(sorted_students,[0])

midl_0= sum([5,3,3,5,4])/len([5,3,3,5,4])
print(midl_0)
midl_1= sum([2,2,2,3])/len([2,2,2,3])
print(midl_1)
midl_2= sum([4,5,5,2])/len([4,5,5,2])
print(midl_2)
midl_3= sum([4,4,3])/len([4,4,3])
print(midl_3)
midl_4= sum([5,5,5,4,5])/len([5,5,5,4,5])
print(midl_4)
#result = {sorted_students,[0],':',float (midl_0),',',sorted_students,[1],':',float(midl_1),',',sorted_students,[2],':',float (midl_2),',',sorted_students,[3],':',float (midl_3),',',sorted_students,[4],':',float (midl_4)}
result = {'Aaron':int (midl_0), 'Bilbo':int(midl_1),'Johnny':int (midl_2),'Khendrik':int(midl_3),'Steve':int(midl_4)}
#,',','Bilbo':int(midl_1),'Johnny':int (midl_2),'Khendrik':int(midl_3),'Steve':int(midl_4)}
print(result)
