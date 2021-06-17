import pytest
from tp_4_testing import obtener_tercer_resultado_google

def test_tercer_resultado():
    tercer_resultado_naranja = obtener_tercer_resultado_google('naranja')
    tercer_resultado_coca_cola = obtener_tercer_resultado_google('coca cola')
    
    print(tercer_resultado_naranja)
    print(tercer_resultado_coca_cola)

    assert tercer_resultado_naranja == 'https://play.google.com/store/apps/details?id=com.tarjetanaranja.emisor.serviciosClientes.appTitulares&hl=en_US&gl=US'
    assert tercer_resultado_coca_cola == 'https://www.cocacola.es/es/home/'