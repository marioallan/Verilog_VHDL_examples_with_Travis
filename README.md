# Verilog_VHDL_examples_with_Travis

# PASSO A PASSO 
---
Configuração da ferramenta de automatização de testes "Travis" no Github. O Travis é um sistema de integração contínua que executa de forma automática através de uma maquina virtual ou Docker (Uma forma de virtualizar aplicações) na nuvem, os testes de projetos adicionados no github, que nesse contexto são em Verilog e VHDL apartir do simulador de projetos de descrição de hardware Modelsim.

# O repositório utilizado nesse exemplo 
---
(https://github.com/marioallan/Verilog_VHDL_examples_with_Travis)

---
# PASSOS:
---
1- Se logar no site do Travis (https://travis-ci.org/) com sua conta do Github.

---
2- Ir na opção "My Repositories", escolher o repositório que vai usar o travis e ativar essa função a partir do botão.

---
3- Ir no repositório e adicionar o arquivo script ".travis.yml".
Nesse script deve conter: 

Os comandos para:

* Iniciar uma maquina virtual ou docker.
** Nesse contexto foi usado o comando para instalar uma máquina virtual linux:

sudo: enabled
dist: trusty

* Instalar a linguagem de programação que vai executar os testes.
** Nesse contexto foi usado o comando para instalar o "python".

python:
  - '3.6'

* Instalar via "python" as dependências necessárias para executar os projetos feitos em Verilog e VHDL.

termcolor
vunit
vunit_hdl
requests
joblib
subprocess.run
pymongo
datetime
pymongo

 ** Nesse exemplo os comandos para instalar as dependencias foram reunidas no arquivo "requeriments.txt".

* Instalar o Modelsim e suas dependências, no qual irá executar os testes dos projetos de descrição de hardware em Verilog e VHDL. Além de configurar suas variáveis de inicialização.

 // dependencias modelsim 
  - sudo dpkg --add-architecture i386
  - sudo apt-get update
  - sudo apt-get install build-essential
  - sudo apt-get install gcc-multilib g++-multilib lib32z1 lib32stdc++6 lib32gcc1 expat:i386 fontconfig:i386 libfreetype6:i386 libexpat1:i386 libc6:i386 libgtk-3-0:i386 libcanberra0:i386 libpng12-0:i386 libice6:i386 libsm6:i386 libncurses5:i386 zlib1g:i386 libx11-6:i386 libxau6:i386 libxdmcp6:i386 libxext6:i386 libxft2:i386 libxrender1:i386 libxt6:i386 libxtst6:i386

// modelSim download
  - wget http://download.altera.com/akdlm/software/acdsinst/17.1std/590/ib_installers/ModelSimSetup-17.1.0.590-linux.run -O modelsim.run

// Modelsim install
  - chmod +x modelsim.run
  - ./modelsim.run --mode unattended --accept_eula 1 --installdir $HOME

// Corrigi bug modelsim com kernel 4
  - sed -i '209 a\        4.[0-9]*)             vco="linux" ;;' $HOME/modelsim_ase/vco 

// Define o modelsim como simulador para o VUNIT
  - export VUNIT_SIMULATOR=modelsim
  - export VUNIT_MODELSIM_PATH=$HOME/modelsim_ase/bin/

* O caminho dos arquivos de exemplos em Verilog e VHDL que o mesmo vai executar.

  - python3 Verilog/exemplos_system_verilog/uart/run.py
  - python3 Verilog/exemplos_system_verilog/and/run.py
  - python3 Verilog/exemplos_system_verilog/dut/run.py
  - python3 VHDL/exemplos_vhdl/run.py

---
4- Com tudo configurado, realize um "commit" no repositório do github, mas se for localmente, realize um "commit" seguido de um "push" no repositório para que o processo do teste automatico pelo travis se inicie.  

---
5- Para confirmar que deu certo, vá no github, no repositorio que foi configurado o travis e veja se ao lado do código do commit apareceu um "circulo amarelo" no qual indica que o teste esta sendo executado. Se depois de um tempo aparecu um "ok em verde" é porque o resultado do teste esta correto e ocorreu como o esperado. Mas se estiver um "X vermelho", então o resultado falhou e não ocorreu o esperado.
No site do travis se consegue ver com mais detalhes o processo de teste em andamento e depois de finalizado os detalhes se o teste foi bem sucedido ou se falhou. 

---
# REFERÊNCIAS:

- https://insper.github.io/Z01.1/A-Ambiente-Lab-1/#travis-ci
- https://insper.github.io/Z01.1/LogiComb-Lab-2/

Entendendo a biblioteca "Vunit" usado nos arquivos de Testbench em VHDL do projeto de exemplo para ser usado em projetos Verilog.

- http://vunit.github.io/user_guide.html
- http://vunit.github.io/run/user_guide.html#run-library
