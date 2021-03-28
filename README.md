# :zap: Cargas Verificadas Crawler

Web Scraping das Cargas Verificadas Fornecidas pelo [ONS](http://tr.ons.org.br/)

## Começando

As instruções a seguir irão lhe proporcionar uma cópia deste projeto e de como rodar em sua máquina local para propósito de desenvolvimento e testes. Veja na sessão de [deployment](#Deployment) para saber com mais detalhes de como dar deploy em sua aplicação.

### Pré-requisitos

Dependências necessárias para se instalar o software e como instalá-las.

1. É necessário que você tenha Docker instalado na sua máquina. Para verificar, rode o seguinte comando:

```bash
$ docker -version
```

### Instalação

Para rodar a aplicação, execute os próximos passos:

1. Faça o clone do projeto

```bash
$ git clone https://github.com/felipefariasdasilva/energy_ons.git
```

2. Entre na pasta

```bash
$ cd energy_ons
```

3. Execute a aplicação com Docker Compose

```bash
$ docker-compose up -d
```

## Executando os testes

Para rodar os testes automáticos do seu sistema siga os comandos abaixo:

```bash
# rodando todos testes unitários
$ python ...
```

### Análise dos testes fim-a-fim

Explique o que esses testes testam e o porquê.

```
Dê um exemplo
```

### Estilo de criação dos testes

Explique o que esses testes testam e o porque.

```
Dê um exemplo
```

## Deployment

Adicione notas de como dar deploy do sistema em produção.

## Desenvolvido com
* [Python](https://www.python.org/) - Linguagem

## Contribuições

Criar um arquivo chamado CONTRIBUTING.md e colocar suas regras para contribuição nesse repositório.

Por favor leia [CONTRIBUTING.md]() para mais detalhes a respeito do nosso código de contuda e o processo de submissão de pull-requests para nós.

## Versionamento

Nós usamos [GitHub](https://github.com/) para versionamento. Para visualizar as versões disponíveis veja [tags nesse repositórios](https://github.com/your/project/tags).

## Autores

* **Hugo Araujo** - *Trabalho inicial* - [hugo.araujo@vivazenergia.com.br](hugo.araujo@vivazenergia.com.br)

Veja também a lista completa de [contribuidores](https://github.com/your/project/contributors) que contribuiram para o desenvolvimento deste projeto.

## Licença

Esse projeto é licenciado pela MIT License - veja também [LICENSE.md](LICENSE.md) para mais detalhes

## Agradecimentos

* Inspiração
* etc

## Apêndice

### AWS CLI Tool
> Baixe e instale o [AWS CLI TOOL](https://aws.amazon.com/pt/cli/)

```bash
# configurar aws cli tool
$ aws configure
```

### Chaves de Acesso
> Você irá precisar das suas chaves de acesso que podem ser obtidas na página do [IAM (Identity and Acess Management)](https://console.aws.amazon.com/iam/home?region=us-east-2#/security_credentials$access_key)

### AWS ECR (Elastic Container Registry)
```bash
# autenticação aws no ECR
$ aws ecr get-login-password --region <REGIAO_DO_REPOSITORIO_ECR> | docker login --username AWS --password-stdin <URI_DO_REPOSITORIO_ECR>
```

### Docker

```bash
# faça o build da sua imagem docker
$ docker build -t <NOME_DA_SUA_IMAGEM> .
```

```bash
# crie uma tag para sua imagem docker
$ docker tag <NOME_DA_SUA_IMAGEM>:<VERSÃO_DA_SUA_IMAGEM> <URI_DO_REPOSITORIO_ECT>:<VERSÃO_DA_SUA_IMAGEM>
```

```bash
# envie sua imagem docker para o repositório ECR
$ docker push <URI_DO_REPOSITORIO_ECT>:<VERSÃO_DA_SUA_IMAGEM>
```

