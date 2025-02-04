from functools import wraps
import datetime


def funzione_decoratore(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper():
        print("ciao")
        funzione_parametro()
        print("fine")

    return wrapper


@funzione_decoratore
def mia_funzione():
    print("Hello World!")


@funzione_decoratore
def mia_funzione2():
    print("funzione 2")


# mia_funzione2()
mia_funzione()
