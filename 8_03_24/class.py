def file_writing():
    with open('files.text','w') as f:
     n = input('enter your name: ')
     d = input("enter yout faculty name: ")
     d = d.upper
   
     if d=='cse' or d=='agreculture' or d=='fisheries' or d== 'AGRECULTURE' or  d=='CSE' or d=='FISHERISE':
      f.write(f"welcome {n} to basic programing with python course")
      f.read(f"welcome {n} to basic programing with python course")
     else:
          f.write('Input Correct Department Name')
       

def file_reading():
   with open("files.text","r") as f:
      x =f.read()
      print(x)
file_writing()
file_reading()    
          
    