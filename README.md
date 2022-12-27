# PROYECTO COV-MEX-AI

# Instalación y configuración del proyecto

Este proyecto fue realizado utilizando Python 3, Git y DVC. Si no los tienes instalados, puedes hacerlo con las siguientes instrucciones:

* [Python](https://realpython.com/installing-python/)
* [Git](https://www.atlassian.com/git/tutorials/install-git)
* [DVC](https://dvc.org/)

## Clonando el proyecto

```bash
git clone https://github.com/EstebanBrito/covid19-mexico
```

## Installing Pipenv

Pipenv es utilizado para la instalación de paquetes y el manejo de entornos virtuales. Esto puede realizarse sin la ayuda de Pipenv, pero es MUY recomendado tenerlo. Pipenv es fácilmente instalable con pip:

```bash
pip install pipenv
```

## Añadiendo pipenv al PATH

Los siguientes pasos de la configuración del proyecto dan por sentado que el usuario ha configuado la variable PATH  de tal manera que permita correr ciertos comandos de pipenv. Si ya lo has hecho, salta esta sección. Si no, sigue los siguientes pasos.

### En Linux

Agrega estas líneas a tu archivo ~./bashrc

```bash
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

Cierra las terminales abiertas para que las modificaciones surtan efecto.

### En Windows

Agrega la ruta del directorio de scripts de Python al PATH de tu computadora. Más información de cómo hacerlo [aquí](). Después de seguir los pasos, es posible que se necesite reiniciar Windows para que las modificaciones surtan efecto.

## Configurando entornos virtuales e instalando librerías del proyecto

Sitúease dentro de la carpeta que se generó al clonar el proyecto. Use Pipenv para la creación de un entorno virtual:

```bash
pipenv shell # Crea un entorno virtual de Python
```

Después de creado el entorno, use Pipenv para instalar las librerías:

```bash
(covid19-mexico) pipenv install --ignore-pipfile # Instala los paquetes necesarios para el proyecto
```
