name = "ameen ahmed"
age = 27
rank = 20

print("my name is %s my age is %d my rank is %.2f"% (name,age,rank))

mes = "ameen is good but have some mistakes in his love "
print("message is %.15s" % mes)

name = "ameen"
age = 27
rank = 20

print("my name is {:s}".format(name))

mymoney = 6521488

print("my money in bank is {:_f}".format(mymoney))

a,b,c = "one","two","three"

print("hello {} {} {}" .format(a,b,c))
print("hello {1} {0} {2}" .format(a,b,c))

a,b,c = 10 , 20 , 30

print("hello {} {} {}" .format(a,b,c))
print("hello {1:f} {0:f} {2:f}" .format(a,b,c))

name = "ali"
age = 28
print("my name is %s and my age is %d" %(name,age))

a , b , c = "first","second","third"
print ("hello to {} {} {}".format(a , b , c))
print ("hello to {2} {0} {1}".format(a , b , c))

name = "ameen"
age = 27
print(f"my name is soo {name} and my age is {age}")

print(float(100))
print(8%2)
print(100//5)

mymen = ["one","two","three", 1.100, True]
nn = ["four","five",False]

mymen.append(nn)
mymen.extend(nn)
print (mymen)

a = [1,2,5,9,7,8,10,3,6,8,2]
a.count(2)
print (a)

ee = {1, 2, 3, 5, 8, 7, 9}
ee.add(10)
print(ee)

qq = {1, 2, 3, 5, 8, 7, 9,10}
ww = {1,2,3}
print(qq.issubset(ww))

user = {

"name":"ameen",
   "age":27,
   "nationality":"egy"
}
print(user)
print(user['name'])
user.update({'rating':200})
user.copy()
print(user.keys())
print(user.values())

main = {
      "name":"reemo"
}
b= main.copy()
print(b)
