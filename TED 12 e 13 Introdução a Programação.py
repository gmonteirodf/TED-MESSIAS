from time import sleep
glosário = {'ram ':'uma memória não permanente',
            'rom':'uma memoria permanente',
            'IOS' : 'um sistema operacional',
            'processador':'uma ferramenta que processa',
            'cooler':' uma ferramenta que resfria o processador'
            }
for i in glosário:
    sleep(1)
    print('\n -----------------')
    print(f'{i} é {glosário[i]}')


