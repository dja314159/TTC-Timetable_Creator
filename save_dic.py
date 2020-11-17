import pickle
dic=[{"test":1,"test2":2},{"test":1,"test2":2}]

#쓰기
file=open("fileName.bin","wb+")
pickle.dump(dic,file)
file.close()


#읽어오기
file=open("fileName.bin","rb")
content=pickle.load(file)

for lecture in content:
    print(lecture)



