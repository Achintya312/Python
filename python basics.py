DATA TYPES = FOUR TYPES OF DATA TYPES (main three types)=

INTEGERS (int.) = 53
STRING (STR.) = " ACHINTYA"
FLOAT = 2.3, 5.7
THE LANGUAGE A COMPUTER CAN UNDERSTAND IS CALLED MACHINE LANGUAGE

VARIABLES= BOXES THAT CAN HOLD SOMETHING eg.- AGE OF FATHER= X AGE OF SON= Y (X= 2Y)

type(35)
-int

type("achintya")
-str

type("achintya12")
-str

type(3.5)
-float

print("hello everyone")
-hello everyone


print("hello sir", "how are you",sep="(--)")
-hello sir(--)how are you

print("hello again","my name is achintya wadhwa","i study in class vi",sep=" --> ")
-hello again --> my name is achintya wadhwa --> i study in class vi

print("hello sir\n------------\nhow are you")  #\n is a function that inserts a line in between two sentences   
-hello sir
------------
how are you

print("hello everyone")
print("\thello everyone again")  #\t is a function which puts 8 spaces.
-hello everyone
	hello everyone again

type(input)
-method


Athematic Operators
+= addition
-= subtraction
"*"= multiplication
/= division
%= modulus
**= exponentiation
//= floor division


print(2+3)
print(5-3)
print(1*5)
print(12/5)

5
2
5
2.4

print(2**3) #it means - 2 raised to the power 3
8

print(10//3)  # it will give us quotient
3

print(10%3)   # it will give us remainder
1


Logical Conditions
equal= a==b,
not equal= a!=b,
less than= a<b,
less than or equal to= a<=b,
greater than= a>b,
greater then or equal to = a>=b,


print(2==3)
False

print(3!=4)
True

print(5>10)
False

print(2>=2)    
True


Logical Operators
and= Logical AND: true if both the operands are true
or= Logical NO : true if either of the operands is the true
not= Logical Not: true if operand is false


print(2<3 and 50>8)
True

print(5==5)
True

print(2==5 and 199==5)
False

  
a=5                       # "=" assigns that is, it gives a value a unknown variable and "==" checks if both the parties have equal values
b=2
print(a==b,a>b,a<b)
False True False

print(2==3 or 5>3)
True

print(not(38765==355869739738257648765 or 35468847856895>77588657641878457354375475764))
True

marks=int(input("enter you marks:- "))
if marks<33:
  print ("you have failed the exam, sorry")
  print("try hard next time")
if marks>33:
  print("you have passed the exam, kudos!!!")
     
enter you marks:- 40
you have passed the exam, kudos!!!

     

marks=int(input("enter you marks:- "))
if marks<33:
  print ("you have failed the exam, sorry")
  print("try hard next time")
elif marks>=33 and marks <60:
  print("you have passed, not satisfactory")
elif marks>=60 and marks <80:
  print("good performance")
else:
  print("Excellentttttt, proud of you")
  print("go home, invite me in your party")


account_circle
enter you marks:- 90
Excellentttttt, proud of you
go home, invite me in your party


a=int(input())
b=int(input())
c=int(input())
if (a>=b and a>=c):
  print("a is largest")
elif (b>=a and b>=c):
  print("b is the largest")
else:
  print("c is the largest")
187
567
35
b is the largest


a=int(input())
b=int(input())
c=int(input())
largest=a
if b>largest:
  largest=b
elif c>largest:
  largest=c
elif a==b==c:
  print("All are equal")
elif a==b:
  print("a and b are equal")
elif a==c:
  print("a and c are equal")
elif b==c:
  print("b and c are equal")

print("the largest number is",largest)
123154243
135412546
143434544
the largest number is 135412546

       
Dictionary
List = it is a collection which is ordered and changeable. allows duplicate members.
Tuple = it is a collection which is ordered and unchangeable. allows duplicate members.
  

List Methods

append()= adds an element at the end of the list
clear()= removes all the elements from the list
copy()= returns a copy of the list
count()= returns the number of elements with the specified value
index()= returns the index of the first element with the specified value
insert()= adds an element at thes pecified position
pop()= removes the element at the specified position
remove()= removes the item with the specified value
reverse()= reverses the order of the list
sort()= sorts the list


list=["maths","phy","chem","eng"]
print(list)
['maths', 'phy', 'chem', 'eng']

list=["achintya","kushagra","meetu","sanjay"]
print(list)
['achintya', 'kushagra', 'meetu', 'sanjay']

list=["maths","eng","science","ssc"]
print(list)
list.append("geography")
print(list)
print(list[4])

['maths', 'eng', 'science', 'ssc']
['maths', 'eng', 'science', 'ssc', 'geography']
geography

list=["maths","eng","science","ssc"]
print(list)
list.append("geography")
print(list)
print(list[-4])
account_circle
['maths', 'eng', 'science', 'ssc']
['maths', 'eng', 'science', 'ssc', 'geography']
eng

list=["achintya","kushagra","meetu","sanjay"]
print(list)
list.append("achintya")
print(list)
print(list[0])
account_circle
['achintya', 'kushagra', 'meetu', 'sanjay']
['achintya', 'kushagra', 'meetu', 'sanjay', 'achintya']
achintya

list=["maths","eng","science","ssc"]
print(list)
list.append("geography")
print(list)
print(list[-4])
list.insert(0,"eco")
print(list)
  
['maths', 'eng', 'science', 'ssc']
['maths', 'eng', 'science', 'ssc', 'geography']
eng
['eco', 'maths', 'eng', 'science', 'ssc', 'geography']

list=["maths","eng","science","ssc"]
print(list)
list.append("geography")
print(list)
print(list[-4])
list.insert(0,"eco")
print(list)
list.reverse()
print(list)
list.clear()
print(list)
  
['maths', 'eng', 'science', 'ssc']
['maths', 'eng', 'science', 'ssc', 'geography']
eng
['eco', 'maths', 'eng', 'science', 'ssc', 'geography']
['geography', 'ssc', 'science', 'eng', 'maths', 'eco']
[]


ilist=[10,23,45,60,15,234,23456,3445534,34443435546456334,3275678617563786284223]
sum=0
count=0
for x in ilist:
  if x%2==0:
    sum+=x
    count+=1
average=sum/count
print(count)
print("Average is ",average)
output
6
Average is  5740572591654271.0

ilist=[10,23,45,60,15,234,23456,3445534,34443435546456334,46766477662756,566278647364756,6746374474,46746578,575848394]
sum=0
count=0
for x in ilist:
  if x%2==0:
    sum+=x
    count+=1
sum=sum
print(count)
print("The sum of even numbers is ",sum)
output
11
The sum of even numbers is  35056488043922586
[ ]
  1
  2
  3
  4
  5
  6
  7
  8
count=20
i=1;
j=1;
print("1:",i)
print("2:",j)
for x in range(3,count+1):
  print(x,":",i+j)
  i,j=j,i+j
output
1: 1
2: 1
3 : 2
4 : 3
5 : 5
6 : 8
7 : 13
8 : 21
9 : 34
10 : 55
11 : 89
12 : 144
13 : 233
14 : 377
15 : 610
16 : 987
17 : 1597
18 : 2584
19 : 4181
20 : 6765

limit=1000
i=1;
j=1;
count=2
print("1:",i)
print("2:",j)
while i+j<limit:
  count+=1
  print(count,":",i+j)
  i,j=j,i+j
output
1: 1
2: 1
3 : 2
4 : 3
5 : 5
6 : 8
7 : 13
8 : 21
9 : 34
10 : 55
11 : 89
12 : 144
13 : 233
14 : 377
15 : 610
16 : 987
   
num=int(input("Enter A Number:- "))     #using for loop
for x in range(2,num):
  if num%x==0:
    print(num,"- Is Not A Prime Number")
    break 
else:
  print(num,"- Is A Prime Number")
  print()
output
Enter A Number:- 145423
145423 - Is A Prime Number


xcount=3
ycount=2
zcount=3
for x in range(1,xcount+1):
    print("x=",x,"inside x loop")
    for y in range(1,ycount+1):#start a for loop and run it ycount times
        print("y=","inside y loop  ")
        for z in range(1,zcount+1):
            print("z=","inside z loop")
            print(x,",",y,",",z,end=" | ")#print x and y in same line
    print()#move pointer to next line 
output
x= 1 inside x loop
y= inside y loop  
z= inside z loop
1 , 1 , 1 | z= inside z loop
1 , 1 , 2 | z= inside z loop
1 , 1 , 3 | y= inside y loop  
z= inside z loop
1 , 2 , 1 | z= inside z loop
1 , 2 , 2 | z= inside z loop
1 , 2 , 3 | 
x= 2 inside x loop
y= inside y loop  
z= inside z loop
2 , 1 , 1 | z= inside z loop
2 , 1 , 2 | z= inside z loop
2 , 1 , 3 | y= inside y loop  
z= inside z loop
2 , 2 , 1 | z= inside z loop
2 , 2 , 2 | z= inside z loop
2 , 2 , 3 | 
x= 3 inside x loop
y= inside y loop  
z= inside z loop
3 , 1 , 1 | z= inside z loop
3 , 1 , 2 | z= inside z loop
3 , 1 , 3 | y= inside y loop  
z= inside z loop
3 , 2 , 1 | z= inside z loop
3 , 2 , 2 | z= inside z loop
3 , 2 , 3 | 
