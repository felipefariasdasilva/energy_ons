# :zap: Cargas Verificadas Crawler

Web Scraping das Cargas Verificadas Fornecidas pelo [ONS](http://tr.ons.org.br/)

## Começando

As instruções a seguir irão lhe proporcionar uma cópia deste projeto e de como rodar em sua máquina local para propósito de desenvolvimento e testes. Veja na sessão de [deployment](#Deployment) para saber com mais detalhes de como dar deploy em sua aplicação.

### Pré-requisitos

Dependências necessárias para se instalar o software e como instalá-las.

1. É necessário que você tenha [docker](https://www.docker.com/products/docker-desktop) instalado na sua máquina. Para verificar, rode o seguinte comando:

```bash
$ docker --version
```

2. O [git](https://git-scm.com/) é fundamental estar na sua máquina, verifique se está instalado usando o comando:

```bash
$ git --version
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

3. Execute a aplicação com `docker-compose`

```bash
$ docker-compose up --build
```

## Executando os testes

Para rodar os testes automáticos do seu sistema siga os comandos abaixo:

```bash
# rodando todos testes unitários
$ python -m unittest
```

> Saiba mais sobre teste unitários nesse [link](https://docs.python.org/pt-br/3/library/unittest.html)
### Análise dos testes fim-a-fim

Explique o que esses testes testam e o porquê.

```
$ Dê um exemplo
```

### Estilo de criação dos testes

Explique o que esses testes testam e o porque.

```
$ Dê um exemplo
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

> Crie um repositório no ECR

```bash
# autenticação aws no ECR
$ aws ecr get-login-password --region <REGIAO_DO_REPOSITORIO_ECR> | docker login --username AWS --password-stdin <URI_DO_REPOSITORIO_ECR>
```

### Docker

```bash
# faça o build da sua imagem docker
$ docker build -t <NOME_DA_SUA_IMAGEM>:<VERSÃO_DA_SUA_IMAGEM> .
```

```bash
# crie uma tag para sua imagem docker
$ docker tag <NOME_DA_SUA_IMAGEM>:<VERSÃO_DA_SUA_IMAGEM> <URI_DO_REPOSITORIO_ECT>:<VERSÃO_DA_SUA_IMAGEM>
```

```bash
# envie sua imagem docker para o repositório ECR
$ docker push <URI_DO_REPOSITORIO_ECT>:<VERSÃO_DA_SUA_IMAGEM>
```

## Sugestões de melhoria

1. Criar `testes unitários`;

> Pode começar por [aqui](https://dev.to/womakerscode/testes-em-python-parte-1-introducao-43ei#:~:text=%20Testes%20em%20Python%20-%20Parte%201%3A%20Introdu%C3%A7%C3%A3o,para%20fazer%20o%20teste%20rodar.%20Essa...%20More%20)

2. Deixar valores sensíveis (access key, por exemplo) em `variáveis ambiente`;

> Leia mais [aqui](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1)

3. Utilizar `try/catch` para capturar exceção e não deixar o sistema morrer, principalmente em conexões e operações de abrir/fechar arquivos;

> Etapa bem importante pra saúde da aplicação, leia [aqui](https://www.bing.com/newtabredir?url=https%3A%2F%2Fmedium.com%2F%40halilylm%2Ftry-except-blocks-in-python-7372fe20d4af)

4. `Versionar` código-fonte;
5. `Versionar` imagem docker;

6. Criar o `deploy` automático na AWS quando uma alteração no github for identificada;

> Leia um pouco sobre `CI/CD` e como utilizar com a AWS

7. Utilizar `banco de dados relacionais` ao invés de arquivo `.csv`;

> Postgres, MySql, MySqlite, etc são alguns exemplos

8. Usar e abusar da `programação orientada a objetos`;

> Fazer código procedural não é errado, porém você não aproveita os recursos que a linguagem oferece

9. Implementar classe/arquivo sempre com uma `responsabilidade única`;

> Nada de criar uma classe/arquivo "Deus", ou seja, aquela classe/arquivo que faz tudo! O melhor a fazer é separar cada tarefa em funções/classe bem específica e bem delimitada. "Faça apenas uma coisa e faça-a bem feito". Se quiser saber mais pesquise pelo conceito "SOLID".

10. Não implementar strings e números do nada, sempre aplicar os valores a uma variável com um nome `auto-explicativo`;

Exemplo:
```python
# modo não recomendado de calcular área do círculo
a = 3.14 * 2 * 2

# modo recomendado de calcular área do círculo
PI = 3.14159
radius = 2
area_of_circle = PI * radius * radius
```

11. Aprenda usar o [Github](https://github.com); 

> O recomendado é deixar na branch `main` o código que está estável, testado e em produção. Quando estiver em `desenvolvimento`, crie branch específica para aquela atividade, assim você garante que o código estável só sera modificado caso o novo código esteja pronto pra isso.

12. Use e abuse de `IDE's`;

> A maioria delas possui diversas features que nos ajuda na implementação do nosso código, além de permitir a instalação de extensões. Eu recomendo o [PyCharm](https://www.jetbrains.com/pycharm/)