#HW>1
print("jai shree ram")
#HW>2
A,B=20,30
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A//B)
print(A%B)
print(A**B)
#SWAPING 2 VARIABLES
a=2
b=3
a,b=b,a 
print(a)
#USING 3 VARIABLE
a=5
b=6
c=a
a=b 
b=c 
print(b)
#HW>3
'''
a=input("NAME: ")
b=(input("AGE: "))
print("hello " + a + "! you are " + b + " yeras old")
print(f"hello {a} you are {b} years old")
'''
#2'''

x=input("sentence: ")
print(x.upper())
print(x.lower())
print(x.replace(" ","_"))
print(x.strip())
#3
'''
d=input("string: ")
print(len(d.replace(" ","")))
#4
print("hello\n\tworld\n this is a backslash: \\")
'''
#HW>4
'''
f,g=4,77
print(f>10 and g>10)
print(f<5 or g<5)
print(not(f>10))
#2
l=int(float(input("AGE: ")))
if l>=18:print("you are an adult")
else:print("you are a minor")
#3
h=input("string: ")
print("a" in h)
print("python" not in h)
'''
#HW>5
'''
a=["apple",4,"king",5]
a.append("fish")
a.insert(2,"kiwi")
print(a)
a.pop(2)
print(a)
#2
p=[1,33,4,55,6]
p.sort()
print(p)
p.reverse()
print(p)
'''
#HW>6

q=("rama","krishna","shiva","kali","kalki")
print(q[1:3])
a=(1,2,33,4)
d=q+a 
print(d)
#2
d={"mango","apple","cherry"}
k={"banana","peach","mango"}
print(d|k)
print(d&k)
print(d-k)
d.add("kiwi")
print(d)
d.remove("mango")
print(d)
#3
a=[1,2,4,55,6]
b=set(a)
c=tuple(a)
print(b,c)
b.add(9)
print(b,c)
'''
#HW>7
d={
    "mandya":"ragi ball",
    "banglore":"dosa",
    "manglore":"fish",
    "mysur":"mysur pak",
    "hubbli":"roti"
}

print(d)
d["davangere"]="idli"
print(d)
d["banglore"]="rice bath"
print(d)
del d["mandya"]
print(d)
print(d.keys())
print(d.values())
#2
t={
    "f1":{
        "name":"mahesh",
        "fav sub":"maths",
        "fav food":"dosa"
    },
    "f2":{
        "name":"suresh",
        "fav sub":"science",
        "fav food":"idli"
    }
}
print(t["f1"]["fav sub"])
