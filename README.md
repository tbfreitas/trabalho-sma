### Trabalho final da disciplina de Sistema Multi Agentes 1/2020
 * Tarcísio Batista de Freitas Junior - 20/0052128
 
 Este trabalho simula o funcionamento de um sistema com agentes computacionais que interagem entre si.
 Para produção do trabalho, utilizou-se o framework `pade`,
 
 https://github.com/lucassm/Pade
 
 ## Como rodar

#### Python3+

 Para rodar o projeto, precisamos verificar se estamos com a versão instalada do python3+ no sistema. Para tal , damos o comando:
 
    python --version
    
 O output mostra a versão do python instalado. Caso não o possua, ou tenha a versão 2.x, o tutorial para instalação é : `https://docs.python-guide.org/starting/install3/osx/`.

#### Pip 

O pip é o gerenciador de pacotes do python. Para verificar sua instalação e sua versão, damos o comando:
    
    pip --version

Caso não o tenha instalado, o link para instalação é `https://pip.pypa.io/en/stable/installing/`.

________________________________________________________________________________________________________

Com o `python` e o `pip` instalados, agora entramos na pasta e criamos um ambiente virtual limpo pro projeto, através do comando:

    python3 -m venv env

Com a pasta `env` criada na pasta raiz do projeto, entramos na mesma e instalamos o pade com o comando:

    pip install pade

Espere a instalação do framework finalizar. Pronto, agora podemos rodar o projeto. Volte para a pasta raiz do projeto e dê o comando: 

    pade start-runtime main.py

O executável do projeto será chamado e os agentes iniciados. A partir dai, pasta ficar de olho no `output` do terminal e ver a comunicação acontecendo.    


