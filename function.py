def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("dip",age=21,add="pune")