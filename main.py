from PySimpleGUI import *

class Calculator:
    def __init__(self):
        theme('Reddit')

        self.layout = [
            [Text('Calculadora de custos da Impressão 3D', font = ('Arial', 15, 'bold'))],

            [Text('Filamento', font = ('Arial', 12, 'bold'))],
            [
                Text('Preço do filamento (1Kg):'), 
                Input(size = (10, 1), key = 'filament'), 
                Text('Quantidade utilizada (g):'), 
                Input(size = (10, 1), key = 'weight'), 
            ],

            [Text('Energia', font = ('Arial', 12, 'bold'))],
            [
                Text('Taxa de distribuição de energia:'), 
                Input(size = (10, 1), key = 'tax'), 
                Text('Gasto da impressora (W):'), 
                Input(size = (10, 1), key = 'watts'), 
                Text('Tempo de impressão: (h):'), 
                Input(size = (10, 1), key = 'hours')
            ],

            [Text('Trabalho manual', font = ('Arial', 12, 'bold'))],
            [
                Text('Valor por hora (R$):'),
                Input(size = (10, 1), key = 'manual_price'), 
                Text('Horas trabalhadas (h):'),
                Input(size = (10, 1), key = 'manual_hours')
            ],

            [Text('Gastos adicionais', font = ('Arial', 12, 'bold'))],
            [
                Text('Valor gasto em outras coisas:'),
                Input(size = (10, 1), key = 'other')
            ],

            [Text('Lucro', font = ('Arial', 12, 'bold'))],
            [
                Text('Margem de lucro (%):'),
                Input(size = (10, 1), key = 'profit')
            ],

            [Button('Gerar valor')]
        ]

    def create(self):
        self.window = Window('Calculadora 3D', self.layout)

    def treat_data(self, data: list):
        parameters = ['Preço do filamento (1Kg)', 'Quantidade utilizada (g)', 'Taxa de distribuição de energia', 'Gasto da impressora (W)', 'Tempo de impressão (h)', 'Valor por hora manual', 'Horas trabalhadas', 'Outros', 'Lucro']

        for i in range(len(data)):
            if data[i] == '':
                popup_error('Preencha todos os parâmetros (ponha 0 se não quiser algum parâmetro)')
                return 

            try:
                data[i] = float(data[i])
            except:
                popup_error('Em números decimais, troque "," por "."')
                return

        filament_price = (data[0] * data[1]) / 1000
        energy = (data[2] * data[3] * data[4]) / 1000
        manual = data[5] * data[6] 
        other = data[7]
        total_np = filament_price + energy + manual + other
        profit = total_np * (data[8] / 100)
        total = total_np + profit

        self.total_screen([filament_price, energy, manual, other, profit, total])

    def total_screen(self, data: list):
        layout = [
            [Text('Valores finais:', font = ('Arial', 15, 'bold'))],
            [Text('Preço do filamento:', font = ('Arial', 12, 'bold')), Text(f'R${data[0]}')],
            [Text('Preço da energia:', font = ('Arial', 12, 'bold')), Text(f'R${data[1]}')],
            [Text('Preço pelo trabalho manual:', font = ('Arial', 12, 'bold')), Text(f'R${data[2]}')],
            [Text('Outros:', font = ('Arial', 12, 'bold')), Text(f'R${data[3]}')],
            [Text('Seu lucro:', font = ('Arial', 12, 'bold')), Text(f'R${data[4]}')],
            [Text('Total', font = ('Arial', 12, 'bold')), Text(f'R${data[5]}')]
        ]

        self.window.close()

        total_window = Window('Calculadora 3D', layout)

        while True:
            events, values = total_window.Read()
            
            if events == WINDOW_CLOSED:
                break

    def window_loop(self):
        while True:
            events, values = self.window.Read()

            if events == WINDOW_CLOSED:
                break

            if events == 'Gerar valor':
                filament = values['filament']
                weight = values['weight']
                tax = values['tax']
                watts = values['watts']
                hours = values['hours']
                manual_price = values['manual_price']
                manual_hours = values['manual_hours']
                other = values['other']
                profit = values['profit']

                self.treat_data([filament, weight, watts, hours, tax, manual_price, manual_hours, other, profit])         
    
calculator = Calculator()
calculator.create()
calculator.window_loop()
