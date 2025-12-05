# Adicione ao repositório o script banco.py (no Moodle) e implemente a classContaBancaria:
# Atributos:
# - titular: O nome do titular da conta (string).´
# - saldo: O saldo da conta (float).
# - limite: O limite de crédito da conta (float).

# Métodos:
# - __init__(titular, saldo, limite): Inicializa os atributos da classe.
# - depositar(valor): Adiciona o valor passado ao saldo da conta. Se o valor for positivo, imprime 1; caso contrário, imprime 0.
# - levantar(valor): Subtrai o valor passado do saldo da conta, se o valor for menor ou igual ao saldo disponível, considerando o limite de crédito.
# Se a operação for bem-sucedida, imprime 1; caso contrário, imprime 0.
# - exibir_saldo(): Imprime o saldo atual da conta com duas casas decimais.
# - exibir_info(): Imprime as informações da conta no formato: "[titular] [saldo] [limite]".


import argparse


class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
            if valor > 0:
                self.saldo += valor
                print(1)
            else:
                print(0)

        # levantar(valor): Subtrai o valor passado do saldo da conta, se o valor for menor ou igual ao saldo disponível, considerando o limite de crédito.
        # Se a operação for bem-sucedida, imprime 1; caso contrário, imprime 0.
    def levantar(self, valor):
            if valor <= self.saldo + self.limite:
                self.saldo -= valor
                print(1)
            else:
                print(0)

        # exibir_saldo(): Imprime o saldo atual da conta com duas casas decimais.
    def exibir_saldo(self):
            print(f"{self.saldo:.2f}")

        # exibir_info(): Imprime as informações da conta no formato: "[titular] [saldo] [limite]".
    def exibir_info(self):
            print(f"{self.titular} {self.saldo} {self.limite}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerir Uma Conta Bancária")
    parser.add_argument(
        "-A",
        "--acao",
        required=True,
        choices=["depositar", "levantar", "saldo", "info"],
        help="Ação a Executar",
    )
    parser.add_argument(
        "-V", "--valor", type=float, help="Valor para Depositar ou Levantar"
    )
    args = parser.parse_args()

    conta = ContaBancaria("Carlos", 500.0, 100.0)

    if args.acao == "depositar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Depositar.")
        else:
            conta.depositar(args.valor)
    elif args.acao == "levantar":
        if args.valor is None:
            print("É Necessário Fornecer o Valor Para Levantar (-v VALOR).")
        else:
            conta.levantar(args.valor)
    elif args.acao == "saldo":
        conta.exibir_saldo()
    elif args.acao == "info":
        conta.exibir_info()
