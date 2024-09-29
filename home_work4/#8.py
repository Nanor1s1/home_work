ku=int(input("введите кол-во участков: "))
td=0
ts=0
tt=0

for i in range (ku):
    section_length = float(input(f"Введите длину участка {i+1}: "))
    td += section_length
    speed = float(input(f"Введите среднюю скорость на участке {i+1}: "))
    ts += speed 
    tt+=td/ts

print(f"Общее время поездки: {tt}")