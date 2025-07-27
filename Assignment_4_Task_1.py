print("File Processing")
try:
  f=open("sample.txt","r")
  r=f.readlines()
  for i in range(len(r)-1):
    print("line",i+1,":",r[i])  
  f.close()
except FileNotFoundError:
  print("File","sample.txt","not found")