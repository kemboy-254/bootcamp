a = create1D(10, 0)  
for i in range(10):  
   a[i] = 9 - i  
for i in range(10):  
   a[i] = a[a[i]]  
for v in a:  
   writeln(v)
