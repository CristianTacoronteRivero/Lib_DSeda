# -*- coding: utf-8 -*-
"""
Created on Thu May 19 09:51:04 2022

@author: crist
"""

import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'dseda' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Cristian Tacoronte Rivero'
AUTHOR_EMAIL = 'cristiantr.develop@gmail.com'
URL = 'https://github.com/CristianTacoronteRivero/Lib_DSeda'

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería para DS. Aun en prueba.' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'pandas'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)