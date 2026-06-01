from ej5a3 import SafeWalletCredentials


def test_wallet():
    wallet = SafeWalletCredentials("1234")
    assert wallet.get_password() == "1234", "Incorrect password retrieval"

    wallet.set_password("4321")
    assert wallet.get_password() == "4321", "Incorrect password setting"
