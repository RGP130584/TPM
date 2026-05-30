# TPM MVP v0.1

## Objetivo

Construir a primeira versão funcional do TPM (Trusted Cognitive Platform).

O objetivo desta versão NÃO é construir o TPM completo.

O objetivo é validar a proposta central:

"Transformar desenvolvimento assistido por IA em Engenharia e Arquitetura de Software Segura, Confiável e Governada."

---

# Escopo

Esta versão deve implementar apenas:

* tpm init
* tpm scan
* tpm validate
* tpm hygiene

Nada além disso.

---

# Stack Tecnológica

## Linguagem

Python 3.13+

## Ferramentas

* Typer
* Pydantic
* Pytest
* Ruff

---

# Estrutura Esperada

```text
src/tpm/

├── cli/
├── core/
├── security/
├── architecture/
├── hygiene/
├── trust/
├── config/
└── reports/
```

---

# Funcionalidades

## 1. tpm init

Objetivo:

Criar a configuração inicial do projeto.

Deve gerar:

```yaml
project:
  classification: confidential
  criticality: high
  environment: enterprise
  multi_tenant: true
```

Perguntas mínimas:

* Classificação dos dados
* Criticidade
* Ambiente
* Multi-tenant

---

## 2. tpm scan

Objetivo:

Executar análises básicas de segurança.

Detectar:

* Secrets expostos
* API Keys
* Tokens
* Senhas hardcoded
* Dependências vulneráveis

Gerar relatório.

---

## 3. tpm validate

Objetivo:

Executar validações mínimas de confiança.

Resultado:

PASS

ou

FAIL

Com justificativa.

---

## 4. tpm hygiene

Objetivo:

Detectar:

* Código morto
* Imports não utilizados
* Dependências órfãs
* TODOs esquecidos

Gerar relatório.

---

# Trust Score

O MVP deve calcular um score simples.

Categorias:

* Security
* Architecture
* Hygiene

Exemplo:

Security: 80

Architecture: 70

Hygiene: 90

Overall: 80

---

# Fora do Escopo

As funcionalidades abaixo NÃO devem ser implementadas nesta versão:

* Learning Layer
* Conselho Gestor
* Knowledge Graph
* MCP
* Multiagentes
* IA própria
* SAP
* TOTVS
* Hubspot
* Digital Twin
* Trust Gateway
* TPM Enterprise
* TPM Government
* TPM Defense

---

# Critérios de Aceite

O MVP será considerado concluído quando os comandos abaixo funcionarem:

```bash
tpm init

tpm scan .

tpm validate .

tpm hygiene .
```

e gerarem relatórios utilizáveis.

---

# Definition of Done

Para cada tarefa:

* Código implementado
* Testes automatizados
* Documentação atualizada
* Sem erros de lint
* Pull Request criado

---

# Diretriz Arquitetural

Priorizar:

* Simplicidade
* Clareza
* Modularidade
* Reutilização

Evitar:

* Superengenharia
* Framework próprio
* Funcionalidades não aprovadas
* Dependências desnecessárias

O objetivo é validar o conceito do TPM, não construir a versão final do produto.
