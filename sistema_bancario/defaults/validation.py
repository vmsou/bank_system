"""Validador de inputs

Esse seção permite verificar as entradas do úsuario ou do gerente.
Seguinda uma base de críterios retorna ao sistema se as informações
inseridas são validas
"""


def check_name(name):
    """TODO: Verificar se nome possui nome e sobrenome"""
    ...


def check_job(title):
    """TODO: Verificar se profissão é valida [Talvez não seja necessário]"""
    ...


def check_income(income):
    if income >= 0:
        return True
    return False


def check_address(address):
    """TODO: Verificar se endereço é valido [Pode ser OPCIONAL]"""
    ...


def check_phone(phone_number):
    """TODO: Usar regex para identificar validade do telefone"""
    ...


def check_password(password):
    """
    -> Para facilitar usar módulo string
    TODO: Senha maior que 8 caracteres
    TODO: precisando de letras maisculas e minusculas
    TODO: Recusar acentos e/ou caracteres especiais
    """
    ...
