class Paciente:
    def __init__(self, nome, nroPlano, nivelPlano, idade):
        self.__nome = nome
        self.__nroPlano = nroPlano
        self.__nivelPlano = nivelPlano
        self.__idade = idade
        self.__listaServ = []

    def obtemCustoFixo(self):
        tabela_custos = {
            'ouro': [420, 520, 620, 720, 820, 920],
            'prata': [320, 420, 520, 620, 720, 820],
            'bronze': [220, 320, 420, 520, 620, 720]
        }

        if 0 <= self.__idade <= 19:
            return tabela_custos[self.__nivelPlano][0]
        elif 20 <= self.__idade <= 29:
            return tabela_custos[self.__nivelPlano][1]
        elif 30 <= self.__idade <= 39:
            return tabela_custos[self.__nivelPlano][2]
        elif 40 <= self.__idade <= 49:
            return tabela_custos[self.__nivelPlano][3]
        elif 50 <= self.__idade <= 59:
            return tabela_custos[self.__nivelPlano][4]
        else:
            return tabela_custos[self.__nivelPlano][5]

    def calculaValorMensal(self, mes, ano):
        custoFixo = self.obtemCustoFixo()
        valorExames = 0
        valorConsultas = 0

        for servico in self.__listaServ:
            if servico['ano'] == ano and servico['mes'] == mes:
                if servico['tipo'] == 'exame':
                    valorExames += servico['valor']

                else:
                    valorConsultas += servico['valor']

        if self.__nivelPlano == 'ouro':
            valorTotal = custoFixo

        elif self.__nivelPlano == 'prata':
            valorTotal = custoFixo + 0.5 * valorExames

        elif self.__nivelPlano == 'bronze':
            valorTotal = custoFixo + 0.5 * (valorExames + valorConsultas)

        print(f'Paciente: {self.__nome}')
        for servico in self.__listaServ:
            if servico['ano'] == ano and servico['mes'] == mes:
                if 'Exame' in servico:
                    print(f"{servico['dia']}/{mes}/{ano} - Exame: {servico['descricao']} - Clínica {servico['clinica']}")
                elif 'Consulta' in servico:
                    print(f"{servico['dia']}/{mes}/{ano} - Consulta: {servico['medico']}")
        print(f'Valor a pagar: {valorTotal}')

    def insereConsulta(self, dia, mes, ano, valor, medico):
        consulta = {
            'dia': dia,
            'mes': mes,
            'ano': ano,
            'valor': valor,
            'medico': medico,
            'tipo': 'consulta'
        }
        self.__listaServ.append(consulta)

    def insereExame(self, dia, mes, ano, descricao, valor, clinica, clinicaConv):
        exame = {
            'dia': dia,
            'mes': mes,
            'ano': ano,
            'descricao': descricao,
            'valor': valor * (0.8 if clinicaConv else 1),
            'clinica': clinica,
            'clinicaConv': clinicaConv,
            'tipo': 'exame'
        }
        self.__listaServ.append(exame)

if __name__ == "__main__":
    listaPac = []
    pac1 = Paciente('João Santos', '111222', 'ouro', 43)
    pac1.insereConsulta(10, 4, 2023, 300, 'Dr. Antonio Souza')
    pac2 = Paciente('Felipe Mendes', '222333', 'prata', 35)
    pac2.insereConsulta(14, 4, 2023, 350, 'Dra. Ana Silva')
    pac2.insereExame(18, 4, 2023, 'Ultrasom abdomen', 500, 'Sul Mineira', True)
    pac3 = Paciente('Márcio Cruz', '333444', 'bronze', 58)
    pac3.insereConsulta(7, 4, 2023, 350, 'Dra. Ana Silva')
    pac3.insereConsulta(12, 3, 2023, 320, 'Dr. Marcelo Silveira')
    pac3.insereConsulta(11, 4, 2023, 300, 'Dr. Antonio Souza')
    pac3.insereExame(22, 4, 2023, 'Raio X Torax', 280, 'Radiologia Ita', False)
    pac3.insereExame(24, 4, 2023, 'Hemograma Completo', 250, 'LabClin', True)
    listaPac.append(pac1)
    listaPac.append(pac2)
    listaPac.append(pac3)
    for pac in listaPac:
        pac.calculaValorMensal(4, 2023)