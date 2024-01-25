import math

def alturaTriangulo(lado):
    # a -> altura, h-> hipotenusa, b -> base
    a = math.sqrt((pow(lado,2))-(pow(lado/2, 2)))
    return a

def main():
    lado = int(input('Lado: '))
    altura = alturaTriangulo(lado)
    area = round(((lado/2)*(altura))/2, 2)
    if area > 1000:
        print('DATOS NO VALIDOS')
    else:
        print(f'El area es: {area} cm2')



if __name__ == '__main__':
    main()