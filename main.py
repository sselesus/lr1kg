
import numpy as np
from PIL import Image

# 1 задание
# чёрное одноканальное
# image_matrix = np.zeros((255, 255), dtype=np.uint8)  # изображение h на w
# for i in range(255):
#     for j in range(255):
#         image_matrix[i, j] = 0
# image = Image.fromarray(image_matrix, mode='L')  # полутон
# image.save('image.png')

# белое одноканальное
# image_matrix = np.zeros((255, 255), dtype=np.uint8)  # изображение h на w
# for i in range(255):
#     for j in range(255):
#         image_matrix[i, j] = 255
# image = Image.fromarray(image_matrix, mode='L')  # полутон
# image.save('image.png')

# красное трёхканальное, [red, green, blue]
# image_matrix = np.zeros((255, 255, 3), dtype=np.uint8)  # изображение h на w
# for i in range(255):
#     for j in range(255):
#         image_matrix[i, j, 0] = 255
# image = Image.fromarray(image_matrix, mode='RGB')  # цвкетное
# image.save('image.png')

# градиент
# image_matrix = np.zeros((255, 255, 3), dtype=np.uint8)
# for i in range(255):
#     for j in range(255):
#         image_matrix[i, j] = ((i+j)//2) % 256
# image = Image.fromarray(image_matrix, mode='RGB')
# image.save('image.png')

# заполнить значения массива можно и так (вместо цикла)
# image_matrix[0:255, 0:255, 0] = 255
# image_matrix[..., 0] = 255


# 2 задание
# image_matrix = np.zeros((200, 200), dtype=np.uint8)
# for i in range(200):
#     for j in range(200):
#         image_matrix[i, j] = 0  # получили чёрную картинку
# 1-й алгоритм, просто прямая
# x0, y0 = 10, 170
# x1, y1 = 80, 20
# point_count = 1000
# for t_i in range(0, point_count):
#     t = t_i / point_count
#     x = int(x0 * (1 - t) + x1 * t)
#     y = int(y0 * (1 - t) + y1 * t)
#     image_matrix[x, y] = 255
# image = Image.fromarray(image_matrix, mode='L')
# image.save('image1.png')

# 2-й алгоритм, половина звёздочки
# x0, y0 = 100, 100
# point_count = 1000
# for i in range(0, 13):
#     a = 2 * np.pi * i / 13
#     x1, y1 = 100 + 95 * np.cos(a), 100 + 95 * np.sin(a)
#     for x in range(x0, int(x1) + 1):
#         t = (x - x0) / (x1 - x0)
#         y = int(y0 * (1 - t) + y1 * t)
#         image_matrix[y, x] = 255
# image = Image.fromarray(image_matrix, mode='L')
# image.save('image2.png')

# 3-й алгоритм, полная звёздочка
# point_count = 99
# for i in range(0, 13):
#     x0, y0 = 100, 100
#     a = 2 * np.pi * i / 13
#     x1, y1 = int(100 + 95 * np.cos(a)), int(100 + 95 * np.sin(a))
#     steep = False
#     if np.abs(x0 - x1) < np.abs(y0 - y1):
#         x0, y0 = y0, x0
#         x1, y1 = y1, x1
#         steep = True
#     if x0 > x1:
#         x0, x1 = x1, x0
#         y0, y1 = y1, y0
#     for x in range(x0, int(x1) + 1):
#         t = (x - x0) / (x1 - x0)
#         y = int(y0 * (1 - t) + y1 * t)
#         if steep:
#             image_matrix[y, x] = 255
#         else:
#             image_matrix[x, y] = 255
# image = Image.fromarray(image_matrix, mode='L')
# image.save('image3.png')

# 4-й алгоритм, Алгоритм Брезенхема


# def line(x0, y0, x1, y1, my_image, color):  # функция отрисовки линии
#     steep = False
#     if np.abs(x0 - x1) < np.abs(y0 - y1):  # Если смещение по оси X меньше смещения по оси Y
#         x0, y0 = y0, x0
#         x1, y1 = y1, x1
#         steep = True
#     if x0 > x1:  # Если начало прямой находится правее конца, меняем начало и конец местами
#         x0, x1 = x1, x0
#         y0, y1 = y1, y0
#     dx = x1 - x0
#     dy = y1 - y0
#     derror = np.abs(dy / dx)  # отношение сдвига по Y и по X (значение, добавляемое на каждом шаге к смещению по Y)
#     error = 0.0  # переменная, накапливающая смещение по Y
#     y = y0
#     for x in range(x0, int(x1) + 1):
#         if steep:  # если координаты менялись местами
#             my_image[y, x] = color
#         else:
#             my_image[x, y] = color
#         error += derror
#         if error > 0.5:  # Как только error превышает 0,5 – увеличиваем/уменьшаем значение y на 1.
#             y += 1 if y1 > y0 else -1
#             error -= 1.
#     return my_image


# point_count = 99
# for i in range(0, 13):
#     X0, Y0 = 100, 100
#     a = 2 * np.pi * i / 13
#     X1, Y1 = int(100 + 95 * np.cos(a)), int(100 + 95 * np.sin(a))
#     line(X0, Y0, X1, Y1, image_matrix, 255)
# image = Image.fromarray(image_matrix, mode='L')
# image.save('image4.png')

# for i in range(200): ????
#     for j in range(200):
#         image_matrix_v[i, j] = 0
#     point_count = 99
#     for i in range(0, 13):
#         X0, Y0 = 100, 100
#         a = 2 * np.pi * i / 13
#         X1, Y1 = int(100 + 95 * np.cos(a)), int(100 + 95 * np.sin(a))
#         line(X0, Y0, X1, Y1, image_matrix_v, 255)
#     image = Image.fromarray(image_matrix_v, mode='L')
#     image.save('image_1.png')


# 3-6 задание


class Point(object):  # координаты точки

    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z


class Polygon(object):  # полигон

    def __init__(self, a, b, c):
        self.point1 = a
        self.point2 = b
        self.point3 = c

    def line(self, x0, y0, x1, y1, my_image, color):  # функция отрисовки линии
        steep = False
        if np.abs(x0 - x1) < np.abs(y0 - y1):  # Если смещение по оси X меньше смещения по оси Y
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            steep = True
        if x0 > x1:  # Если начало прямой находится правее конца, меняем начало и конец местами
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        derror = np.abs(dy / dx)  # отношение сдвига по Y и по X (значение, добавляемое на каждом шаге к смещению по Y)
        error = 0.0  # переменная, накапливающая смещение по Y

        y = y0 * 25000
        # y = y0 * 2  # для оленя

        for x in range(int(25000 * x0), int(25000 * x1) + 1):
            # for x in range(int(2 * x0), int(2 * x1) + 1):  # для оленя
            if steep:  # если координаты менялись местами
                my_image[int(y) + 2500, int(x) + 1500] = color
            else:
                my_image[int(x) + 2500, int(y) + 1500] = color
            error += derror
            if error > 0.5:  # Как только error превышает 0,5 – увеличиваем/уменьшаем значение y на 1.
                y += 1 if y1 > y0 else -1
                error -= 1.
        return my_image


class ImageObj(object):  # массивы, изображения

    def __init__(self):
        self.v_arr = []
        self.f_arr = []
        self.image_matrix_v = np.zeros((1000, 1000), dtype=np.uint8)
        self.image_matrix_f = np.zeros((5000, 5000), dtype=np.uint8)

    def read_vert(self, filein):  # считывание координат вершин (v)
        for x in filein:
            xs = x.split()  # разделяет строку по пробелам
            if xs:
                flag = False
                if xs[0] == "v":
                    self.v_arr.append(Point(float(xs[1]), float(xs[2]), float(xs[3])))
                    flag = True
                else:
                    if flag:
                        break
        return self

    def read_pol(self, filein):  # счмтывает вершины полигонов из файла (f)
        for x in filein:
            xs = x.split()
            if xs:
                flag = False
                if xs[0] == "f":
                    xsX = xs[1].split("/")
                    xsY = xs[2].split("/")
                    xsZ = xs[3].split("/")
                    self.f_arr.append(Polygon(int(xsX[0]), int(xsY[0]), int(xsZ[0])))
                    flag = True
                else:
                    if flag:
                        break
        return self

    def print_vertex(self):  # рисует точки
        for i in range(len(self.v_arr)):
            self.image_matrix_v[int(5000 * self.v_arr[i].X) + 500, int(5000 * self.v_arr[i].Y) + 250] = 255  # для зайца
            # self.image_matrix_v[int(self.v_arr[i].Y / 2) + 100, int(self.v_arr[i].X / 2) + 500] = 255  # для оленя

    def print_polygon(self):  # проходит по массиву полтгонов и вызывает функцию отрисовки для каждой пары вершин
        for i in range(len(self.f_arr)):
            self.f_arr[i].line(self.v_arr[self.f_arr[i].point1 - 1].X, self.v_arr[self.f_arr[i].point1 - 1].Y,
                               self.v_arr[self.f_arr[i].point2 - 1].X, self.v_arr[self.f_arr[i].point2 - 1].Y,
                               self.image_matrix_f, 255)  # вершины 1 и 2
            self.f_arr[i].line(self.v_arr[self.f_arr[i].point1 - 1].X, self.v_arr[self.f_arr[i].point1 - 1].Y,
                               self.v_arr[self.f_arr[i].point3 - 1].X, self.v_arr[self.f_arr[i].point3 - 1].Y,
                               self.image_matrix_f, 255)  # вершины 1 и 3
            self.f_arr[i].line(self.v_arr[self.f_arr[i].point3 - 1].X, self.v_arr[self.f_arr[i].point3 - 1].Y,
                               self.v_arr[self.f_arr[i].point2 - 1].X, self.v_arr[self.f_arr[i].point2 - 1].Y,
                               self.image_matrix_f, 255)  # вершины 2 и 3


if __name__ == "__main__":
    file = open('model_1.obj')  # открываем файл
    obim = ImageObj().read_vert(file)  # создаём объект и вызываем метод чтения вершин
    file.close()  # закрываем файл
    file = open('model_1.obj')
    obim.read_pol(file)  # метод чтения полигонов
    file.close()

    obim.print_vertex()  # рисуем вершины
    obim.print_polygon()  # рисуем полигоны

    image_matrixf = Image.fromarray(obim.image_matrix_f, mode='L')
    image_matrixf.save('image_f1.png')
    image_matrixv = Image.fromarray(obim.image_matrix_v, mode='L')
    image_matrixv.save('image_v1.png')
    print("Hello, world!")


