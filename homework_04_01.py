with open('salary.txt','w',encoding='utf-8') as file:
    file.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")


def total_salary(path):
    with open('salary.txt','r', encoding='utf-8') as file:
        content = [int(line.strip().split(',')[1]) for line in file.readlines() if line]
        total = sum(content)
        avarage = int(total/len(content))
        return total,avarage
        print(content)


path  = ("./file/salary_file.txt")
total, average = total_salary(path)
print((f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"))