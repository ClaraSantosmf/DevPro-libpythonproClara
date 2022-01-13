from libpythonpro.spam.enviador_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'clarasantosmf@gmail.com',
        'mauricioma@usp.br',
        'arquivamento de procedimento',
        'Desejamos consultar se você quer descartar seus procedimentos'

    )
    assert 'clarasantosmf@gmail.com' in resultado
