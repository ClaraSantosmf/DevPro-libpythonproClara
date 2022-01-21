from libpythonpro.spam.enviador_email import Enviador, EmailInvalido

import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente',
                         ['clarasantosmf@gmail.com', 'foo@bar.com.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'clarasantosmf@gmail.com',
        'arquivamento de procedimento',
        'Desejamos consultar se você quer descartar seus procedimentos')
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'foo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente,
                        'clarasantosmf@gmail.com',
                        'arquivamento de procedimento',
                        'Desejamos consultar se você quer descartar seus procedimentos')
