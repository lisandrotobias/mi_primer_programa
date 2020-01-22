
data_list = ["hola", 20,"replica", 60,"prueba", 80,"testeoooooo", 502]
str_list = []
int_list = []

for data in data_list:
    if str(data).isdigit():
        int_list.append(data)
    else:
        str_list.append(data)

print(str_list)
print(int_list)
