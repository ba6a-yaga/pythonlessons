# По введенным пользователем координатам
# двух точек вывести уравнение прямой,
# проходящей через эти точки.

coor = input('Введите 4е координаты x1;y1;x2;y2 через точку с запятой: \n')

arCoor = coor.split(';')

# a = (y1 - y2)
print(f'a = ({arCoor[1]} - {arCoor[3]})')
# b= (x2 - x1)
print(f'a = ({arCoor[2]} - {arCoor[0]})')
# c = (x1 * y2 - x2 * y1)
print(f'c = ({arCoor[0]} * {arCoor[3]} - {arCoor[2]} * {arCoor[1]})')

print('\nУравнение прямой: ax + by + c = 0')
