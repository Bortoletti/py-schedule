import schedule
import time

def exibir_servico():
    print("Servico executando")

schedule.every(5).seconds.do( exibir_servico )

while True:
    schedule.run_pending()

    