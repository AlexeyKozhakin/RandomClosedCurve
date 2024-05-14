import numpy as np
#Окружность
def circle(N=1000):
    # Генерируем углы от 0 до 2*pi равномерно
    angles = np.linspace(0, 2 * np.pi, N)

    # Создаем массив X с координатами точек на окружности
    X = np.zeros((N, 2))
    X[:, 0] = np.sin(angles)  # Координаты x
    X[:, 1] = np.cos(angles)  # Координаты y
    return X

# Квадрат
def square_top(N):
    a=np.sqrt(np.pi)/2
    # Генерируем углы от 0 до 2*pi равномерно
    angles = np.linspace(-np.pi/4, np.pi/4, N)
    # Создаем массив X с координатами точек на окружности
    X = np.zeros((N, 2))
    X[:, 0] = a*np.tan(angles)  # Координаты x
    X[:, 1] = a  # Координаты y
    return X

def square_low(N):
    a=np.sqrt(np.pi)/2
    # Генерируем углы от 0 до 2*pi равномерно
    angles = np.linspace(3*np.pi/4, 5*np.pi/4, N)
    angles = angles[::-1]
    # Создаем массив X с координатами точек на окружности
    X = np.zeros((N, 2))
    X[:, 0] = a*np.tan(angles)  # Координаты x
    X[:, 1] = -a  # Координаты y
    return X

def square_right(N):
    a=np.sqrt(np.pi)/2
    # Генерируем углы от 0 до 2*pi равномерно
    angles = np.linspace(np.pi/4, 3*np.pi/4, N)

    # Создаем массив X с координатами точек на окружности
    X = np.zeros((N, 2))
    X[:, 0] = a  # Координаты x
    X[:, 1] = a/np.tan(angles)  # Координаты y
    return X

def square_left(N):
    a=np.sqrt(np.pi)/2
    # Генерируем углы от 0 до 2*pi равномерно
    angles = np.linspace(5*np.pi/4, 7*np.pi/4, N)
    angles = angles[::-1]
    # Создаем массив X с координатами точек на окружности
    X = np.zeros((N, 2))
    X[:, 0] = -a  # Координаты x
    X[:, 1] = a/np.tan(angles)  # Координаты y
    return X

def square(N=1000):
    return np.concatenate((square_top(N//4),
                           square_right(N//4),
                           square_low(N//4),
                           square_left(N//4)))
                           
                           
#Отрисовка фигур
import matplotlib.pyplot as plt
def plot(X,color='red'):
    # Выводим точки
    plt.plot(X[:, 0], X[:, 1], color=color)
    #plt.scatter(X[:, 0], X[:, 1], color='blue')
    # Устанавливаем равный масштаб по осям
    plt.axis('equal')
    plt.show()

def plots(*Curvs,color='red'):
    # Выводим точки
    for X in Curvs:
        plt.plot(X[:, 0], X[:, 1], color=color)
        #plt.scatter(X[:, 0], X[:, 1], color='blue')
        # Устанавливаем равный масштаб по осям
        plt.axis('equal')
    plt.show()

