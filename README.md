# PASSO A PASSO 
---
Configuração da ferramenta de automatização de testes "Travis" no Github. O Travis é um sistema de integração contínua que executa de forma automática através de uma maquina virtual ou Docker (Uma forma de virtualizar aplicações) na nuvem, os testes de projetos adicionados no github, que nesse contexto são em Verilog e VHDL apartir do simulador de projetos de descrição de hardware Modelsim.

## O repositório utilizado nesse exemplo 
---
(https://github.com/marioallan/Verilog_VHDL_examples_with_Travis)

---
## PASSOS:
---
1- Se logar no site do Travis (https://travis-ci.org/) com sua conta do Github.

---
2- Ir na opção "My Repositories", escolher o repositório que vai usar o travis e ativar essa função a partir do botão informado.

---
3- Ir no repositório e adicionar o arquivo script ".travis.yml" (Olhar como ficou os comandos nesse arquivo no repositório).

Nesse script deve conter: 

Os comandos para:

- Iniciar uma maquina virtual ou docker. (Escolhido o comando para instalar uma máquina virtual linux)
- Instalar a linguagem de programação que vai interagir e executar os testes. (Escolhido o comando para instalar a linguagem "python".)
- Instalar via "python" as dependências necessárias para executar os projetos feitos em Verilog e VHDL. (Nesse exemplo os comandos para instalar as dependencias foram reunidas no arquivo "requeriments.txt".
- Instalar o Modelsim e suas dependências, no qual irá executar os testes dos projetos de descrição de hardware em Verilog e VHDL. Além de configurar suas variáveis de inicialização.

E os caminhos:

- Dos arquivos python "run.py" que através da biblioteca "Vunit" do python instalado nas "dependencias necessarias", é a responsável pela execução dos projetos e seus respectivos testbenchs em Verilog (.sv) e em VHDL (.vhd).

---
4- Com tudo configurado, realize um "commit" no repositório do github para que o processo do teste automatico pelo travis se inicie. Caso esteje com o repositório localmente no PC, realize um "commit" seguido de um "push".    

---
5- Para confirmar que deu certo, vá no github, no repositorio que foi configurado o travis e veja se ao lado do código do commit apareceu um "circulo amarelo" no qual indica que o teste esta sendo executado. Se depois de um tempo aparecu um "ok em verde" é porque o resultado do teste esta correto e tudo ocorreu como o esperado. Mas se estiver um "X vermelho", então o resultado falhou.
Pelo site do travis e visto com mais detalhes o processo de teste em andamento. e depois de finalizado os detalhes, se o teste foi bem sucedido ou se falhou. 

---
## Configuração dos arquivos de testbenchs em Verilog (.sv) e VHDL(.vhd) usando a biblioteca "Vunit". (Olhar os exemplos do repositório para facilitar o entendimento)

OBS: (Nos exemplos em Verilog, cada exemplo foi adicionado em uma pasta "src" e "test". Já no exemplo em VDHL, todos os exemplos foram colocados em uma única pasta "src" e "test" respectivamente).

## Em Verilog

OBS:(Os comandos adicionados do "Vunit" em verilog só funcionam com a extensão ".sv")

No arquivo de testbench adicionar:

---
No topo do arquivo: 

````
`include "vunit_defines.svh"
````

No final do arquivo antes do "endmodule":

````
`TEST_SUITE begin

    `TEST_CASE("Test that pass") begin
       @(Variavel_de_saída);
       `CHECK_EQUAL(Variavel_de_saída, 0);
    end
		
   `TEST_CASE("Test that fail") begin
         @(Variavel_de_saída);
         `CHECK_EQUAL(Variavel_de_saída, 1);
    end
end

````
---
## Em VHDL

No arquivo de testbench adicionar:

---
Após as declarações do "LIBRARY" e "USE" os comandos:

```
library vunit_lib;
context vunit_lib.vunit_context;
```
---
NO campo da ENTITY o comando:

```
generic (runner_cfg : string);
```

Exemplo:

```
entity nome_da_entidade is
  generic (runner_cfg : string);
end entity;
```

---
Após a linha com o comando "main":

```
test_runner_setup(runner, runner_cfg);

assert(variavel_de_saida = '30')  report "Falha em teste: Resultado != 30" severity error;
	
test_runner_cleanup(runner); -- Simulacao acaba aqui
```

---
## REFERÊNCIAS:

- https://insper.github.io/Z01.1/A-Ambiente-Lab-1/#travis-ci
- https://insper.github.io/Z01.1/LogiComb-Lab-2/

Entendendo a biblioteca "Vunit" usado nos arquivos de Testbench em VHDL do projeto de exemplo para ser usado em projetos Verilog.

- http://vunit.github.io/user_guide.html
- http://vunit.github.io/run/user_guide.html#run-library
