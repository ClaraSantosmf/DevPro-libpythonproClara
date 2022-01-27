import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario

@pytest.mark.parametrize(
    'usuarios',
    [
        [   Usuario(nome='Clara', email='clarasantosmf@gmail.com'),
            Usuario(nome='Mauricio', email ='mauricioma@usp.br')
        ],
        [
            Usuario(nome='Clara', email='clarasantosmf@gmail.com')
        ]
    ]
)

def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'clarasantosmf@gmail.com',
        'Curso Python Pro',
        'Confira os móduclos fantásticos')

    assert len(usuarios) == enviador.qtd_email_enviados