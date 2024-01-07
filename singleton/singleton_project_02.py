import subprocess

class ServidorCheck:
    __instance = None

    def __new__(cls, *args, **kwargs):
        
        if not ServidorCheck.__instance:
            ServidorCheck.__instance = super(ServidorCheck, cls).__new__(cls, *args, **kwargs)
        
        return ServidorCheck.__instance

    def __init__(self):
        self.__servidores = []

    def verifica_servidor(self, servidor):
        
        # '-c' define o número de pacotes a enviar (neste caso, 4)
        comando_ping = ['ping', '-c', '4', self.__servidores[servidor]]  
        

        try:
            resultado = subprocess.run(comando_ping, capture_output=True, text=True, timeout=10)
            if resultado.returncode == 0:
                return f"O servidor {self.__servidores[servidor]} está acessível."
            else:
                return f"O servidor {self.__servidores[servidor]} não está acessível."
        
        except subprocess.TimeoutExpired:
            return f"O tempo de execução expirou para o servidor {self.__servidores[servidor]}. Verifique sua conexão ou tente novamente mais tarde."

    def add_servidor(self, ip):
        self.__servidores.append(ip)


sanidade_check_1 = ServidorCheck()
sanidade_check_2 = ServidorCheck()

sanidade_check_1.add_servidor('8.8.8.8')

resultado = sanidade_check_2.verifica_servidor(0)
print(resultado)