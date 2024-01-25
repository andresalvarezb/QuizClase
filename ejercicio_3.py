def main():
    voltajes = []
    for i in range(3):
        voltaje = int(input(f'Ingrese el voltaje #{i+1}: '))
        voltajes.append(voltaje)
    
    # Obtener voltaje promedio
    voltaje_promedio = sum(voltajes) / len(voltajes)
    
    if voltaje_promedio <= 155:
        print(f'VOLTAJE CORRECTO: {voltaje_promedio} V')
    elif (voltaje_promedio > 115 and voltaje_promedio < 220):
        print(f'ALTO VOLTAJE: {voltaje_promedio} V')
    else: 
        print(f'¡PELIGRO!')



if __name__ == '__main__':
    main()