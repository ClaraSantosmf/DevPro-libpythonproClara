import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from unittest.mock import Mock


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Clara', email='clarasantosmf@gmail.com'),
         Usuario(nome='Mauricio', email='mauricioma@usp.br')
         ],
        [
            Usuario(nome='Clara', email='clarasantosmf@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'clarasantosmf@gmail.com',
        'Curso Python Pro',
        'Confira os móduclos fantásticos')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Clara', email='clarasantosmf@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mauricioma@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos')
    enviador.enviar.assert_called_once_with(
        'mauricioma@gmail.com',
        'clarasantosmf@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
