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
                Input(size = (10, 1)), 
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

            data[i] = int(data[i])

    def window_loop(self):
        while True:
            events, values = self.window.Read()

            if events == WINDOW_CLOSED:
                break

            elif events == 'Gerar valor':
                filament = values['filament']
                weight = values['weight']
                watts = values['watts']
                hours = values['hours']
                manual_price = values['manual_price']
                manual_hours = values['manual_hours']
                other = values['other']
                profit = values['profit']

                self.treat_data([filament, weight, watts, hours, manual_price, manual_hours, other, profit])         
    
calculator = Calculator()
calculator.create()
calculator.window_loop()
