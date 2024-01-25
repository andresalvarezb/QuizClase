def metros_kilometros(distancia):
    return distancia/1000

def main():
    distancia_m = float(input('Distancia en metros: '))
    distancia_km = metros_kilometros(distancia_m)
    print(f'{distancia_m} m es igual a {distancia_km} km')



if __name__ == '__main__':
    main()