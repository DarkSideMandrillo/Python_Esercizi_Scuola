from functools import wraps
import datetime


def funzione_decoratore(funzione_parametro):
    @wraps(funzione_parametro)
    def wrapper():
        with open("123123123.txt", "a") as file:
            file.write(
                f"Eseguita funzione: {funzione_parametro.__name__} alle: {datetime.datetime.now()}\n"
            )
            funzione_parametro()

    return wrapper


@funzione_decoratore
def mia_funzione():
    print("Hello World!")


@funzione_decoratore
def mia_funzione2():
    print("funzione 2")


# mia_funzione2()
mia_funzione()
mia_funzione2()
mia_funzione()
mia_funzione2()
