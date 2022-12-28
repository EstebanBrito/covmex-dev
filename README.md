# PROYECTO COV-MEX-AI

# Instalación y configuración del proyecto

Este proyecto fue realizado utilizando Python 3, Git y DVC. Si no los tienes instalados, puedes hacerlo con las siguientes instrucciones:

* [Python](https://realpython.com/installing-python/)
* [Git](https://www.atlassian.com/git/tutorials/install-git)
* [DVC](https://dvc.org/)

Además, se usa la librería _graphviz_ para visualizar redes neuronales en Tensorflow. Para instalarla sólo es necesario hacer:

```bash
sudo apt-get install graphviz
```

Más información en los siguientes enlaces: [1](https://datascience.stackexchange.com/questions/12851/how-do-you-visualize-neural-network-architectures), [2](https://pyimagesearch.com/2021/05/22/visualizing-network-architectures-using-keras-and-tensorflow/)

## Clonando el proyecto

Situáte en el directorio en el que desees descargar el proyecto y ejecuta el siguiente comando en la terminal:

```bash
git clone https://github.com/EstebanBrito/covid19-mexico
```

## Instalando Pipenv

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
# Crea un entorno virtual de Python
pipenv shell 
```

Después de creado el entorno, use Pipenv para instalar las librerías:

```bash
# Instala los paquetes necesarios para el proyecto
(covid19-mexico) pipenv install --ignore-pipfile 
```
