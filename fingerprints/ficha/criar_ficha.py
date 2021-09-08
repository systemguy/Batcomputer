from datetime import datetime   #importa datetime
import json #importa json
import os
kill = input('aperte enter para iniciar  a tarefa e k para finalizar :')
while kill != 'k':

    dados = dict()         #cria dicionario
    dados['nome'] = str(input('nome:'))
    nasci = int(input('Ano de nascimento:'))
    dados['sexo'] = input('Sexo (M ou F):')
    dados['idade'] = datetime.now().year - nasci    #calcula idade
    dados['cabelo'] = str(input('cor do cabelo:'))
    dados['olhos'] = str(input('cor dos olhos:'))
    dados['antescendentes'] = str(input('antescedentes:'))

    print('-=' * 30)
    for k, v in dados.items():
        print(f' - {k} recebe : {v}')

    print('-=' * 30)
    os.mkdir('./ficha/' + dados['nome'])
    open('./ficha/' + dados['nome'] + '/' + dados['nome'], 'a',encoding='utf8').write(json.dumps(dados,ensure_ascii=False,indent=2))  #cria arquivo .json

    kill = input('aperte enter para iniciar  a tarefa e k para finalizar :')
