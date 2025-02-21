a1=int(input("enter A1"))
a2=int(input("enter A2"))
a3=int(input("enter A3"))
a4=int(input("enter A4"))
b1=int(input("enter b1"))
b2=int(input("enter b2"))
b3=int(input("enter b3"))
b4=int(input("enter b4"))
m1=(a1+a4)*(b1+b4)
m2=(a3+a4)*b1
m3=a1*(b2-b4)
m4=a4*(b3-b1)
m5=(a1+a2)*b4
m6=(a3-a1)*(b1+b2)
m7=(a2-a4)*(b3+b4)
c1=m1+m4-m5+m7
c2=m3+m5
c3=m2+m4
c4=m1+m3-m2+m6
print("Result:")
print(c1,c2)
print(c3,c4)
