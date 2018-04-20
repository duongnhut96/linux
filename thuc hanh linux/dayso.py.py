print "Nhap n"

n=input()
for i in range(1, n+1):	

print "So Thu %d" %i

def Chan(i):
	if(i % 2 == 0):
		return 1

def TingTong(n):	
tong=0	

for i in range(n+1):		

if(Chan(i)==1):		
	tong=tong+i	

print "Tong =",tong

TingTong(n)
