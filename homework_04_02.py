with open('cats.txt','w',encoding='utf-8') as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")


def get_cats_info(path):
    cats_info=[]
    with open('cats.txt','r', encoding='utf-8') as file:
        for line in file.readlines():
            line.strip()
            content = [line.strip().split(',')[0],line.strip().split(',')[1],line.strip().split(',')[2]]
            kitty = {"id":content[0],"name" : content[1],"age" : content[2]}
            cats_info.append(kitty)
    return cats_info
    
path  = ("./file/cats.txt")
cats_info = get_cats_info(path)
print(cats_info)