def main():
    voltajes = []
    for i in range(5):
        voltaje = int(input(f'Ingrese el voltaje #{i+1}: '))
        voltajes.append(voltaje)
    
    # Obtener voltaje promedio
    voltaje_promedio = sum(voltajes) / len(voltajes)
    
    if voltaje_promedio > 220:
        print(f'ALTO VOLTAJE: {voltaje_promedio}')
    else: 
        print(f'VOLTAJE CORRECTO: {voltaje_promedio}')



if __name__ == '__main__':
    main()