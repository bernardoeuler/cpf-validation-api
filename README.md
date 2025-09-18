# API de validação de CPF
API de validação de CPF serverless, implementada com Azure Functions.

## Como funciona
Acesse o site e coloque o cpf na query string no formato `cpf=xxxxxxxxxxx`, ou no corpo da requisição usando o formato json, tal como em `{"cpf": "xxxxxxxxxxx"}`. A API então vai retornar a validade do CPF.