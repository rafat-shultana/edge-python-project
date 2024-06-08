def func1():
    with open("text.text","w")as f:
        n=input('Enter your name: ')
        d=input('Enter your faculty name: ')
        if d=='cse' or d=='agriculture' and d.upper() and d.lower():
           if 'cse' or 'CSE' or 'Cse' in d or 'agriculture' in d:
            f.write(f"Welcome {n} to Basic Programming with Python Course")
           else:
            print('Please input correctly!')

           x=f.close()
           print(x)
        
        elif d=='bba' or d=='lla' or d.upper() and d.lower():
         if 'bba' in d or 'lla' in d:
            f.write(f"welcome{n} to digital marketing course")
    
        else: 
            x=f.write(f"Welcome {n} to MS word and Excel Course")
            x=f.close()
            print(x)
def func2():
    with open ("text.text","r") as f:
        x=f.read()
        print(x)
func1()
func2()        

    