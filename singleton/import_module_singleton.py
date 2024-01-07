# O python transforma por padrão todo modulo em um singleton

# Aqui o print do arquivo module_singleton.py será executado
import module_singleton

print(f'O modulo importado foi: {module_singleton.NOME}')

module_singleton.funcao_1()


# Aqui o print do arquivo module_singleton.py NÃO será executado
import module_singleton

module_singleton.funcao_2()