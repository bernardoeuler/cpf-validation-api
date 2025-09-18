# API de validação de CPF
API de validação de CPF serverless, implementada com Azure Functions.

## Como funciona
Acesse a API [aqui](https://microservice-validate-cpf-cshndydbh3gahhf9.eastus-01.azurewebsites.net/api/validate_cpf) e coloque o cpf na query string no formato `cpf=xxxxxxxxxxx`, ou no corpo da requisição usando o formato json, tal como em `{"cpf": "xxxxxxxxxxx"}`. A API então vai retornar a validade do CPF.