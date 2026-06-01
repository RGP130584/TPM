# TPM Architecture Report

## 1. Estrutura completa do projeto e Arquivos Criados
Abaixo encontra-se a árvore do projeto gerada, demonstrando a evolução estrutural:

```text
.
├── README.md
├── docs
│   ├── adr
│   │   └── ADR-001-mcca-to-tpm.md.md
│   ├── capability-map.md
│   ├── glossary.md
│   ├── mvp
│   │   └── mvp-v0.1.md
│   ├── parking-lot.md
│   ├── principles.md
│   ├── roadmap.md
│   ├── threat-model.md
│   ├── tree_output.txt
│   └── vision.md
├── pyproject.toml
├── src
│   └── tpm
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-312.pyc
│       ├── architecture
│       │   └── __init__.py
│       ├── cli
│       │   ├── __init__.py
│       │   └── main.py
│       ├── config
│       │   └── __init__.py
│       ├── contracts
│       │   ├── __init__.py
│       │   ├── agents
│       │   ├── mcp
│       │   ├── skills
│       │   └── transformers
│       ├── core
│       │   └── __init__.py
│       ├── hygiene
│       │   └── __init__.py
│       ├── models
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   └── spec.py
│       ├── registry
│       │   ├── __init__.py
│       │   ├── agents
│       │   ├── base.py
│       │   ├── mcps
│       │   ├── skills
│       │   └── transformers
│       ├── reports
│       │   └── __init__.py
│       ├── schemas
│       │   └── __init__.py
│       ├── security
│       │   └── __init__.py
│       ├── specs
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   └── loader.py
│       ├── trust
│       │   └── __init__.py
│       └── validators
│           ├── __init__.py
│           ├── __pycache__
│           └── engine.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   └── test_specs.cpython-312-pytest-9.0.3.pyc
    ├── test_cli.py
    └── test_specs.py

34 directories, 38 files
```

## 2. Arquivos Criados
Neste ciclo de desenvolvimento as seguintes implementações foram realizadas para a **Executable Architecture Foundation**:
* `src/tpm/models/spec.py`: Definições tipadas usando Pydantic.
* `src/tpm/validators/engine.py`: Validador customizado focado em conversão e tratamento de erros (usando ValidationError).
* `src/tpm/specs/loader.py`: Carregador do `tpm.yaml` compatível com parsing Pydantic e dicionário.
* `tests/test_specs.py`: Testes unitários do carregamento e validação de specs.
* `src/tpm/registry/base.py`: Interface genérica para registros da plataforma.
* Registries customizados para MCPs, Skills, Transformers e Agents.
* JSON schemas base estruturados em `src/tpm/contracts/`.

## 3. Dependências Instaladas
Adições ao arquivo `pyproject.toml`
- **pydantic>=2.7.0** (Responsável pelo processo de tipagem em models/spec e a serialização).
- (As dependências base `typer` e `pyyaml` já estavam presentes).

## 4. Commits Realizados
No momento do relatório as alterações estão sendo preparadas para um Pull Request único agrupando as Tasks 003, 004 e 005.

## 5. Decisões Arquiteturais e Tradeoffs
* **Uso do Pydantic**: Foi adotado por ser muito superior e robusto a dataclasses ou dicionários puros. Pydantic fornece tipagem estrita ao ecossistema Python com validação durante a instanciação, economizando trabalho ao desenvolver "checkers". O tradeoff está em atrelar a arquitetura a uma lib externa fortemente (embora compatível com as premissas Python modernas).
* **Camada de Especificação (Specs Engine)**: A engine e os validadores foram separados, com `loader.py` realizando orquestração do file e parsing raw de yaml e injetando no `ValidationEngine`.
* **JSON Schemas nos Contratos**: Implementação JSON Schema agnóstica de linguagem permite a interoperabilidade e portabilidade do contrato de `Agent`, `Skill`, `Transformer` e `MCP` caso haja integração de componentes em outra linguagem.
* **Registry Genérico**: Foi utilizada abordagem de Generics em Python (`TypeVar` + `Generic`) em `BaseRegistry` para garantir reuso. Ele permite controle de versão (onde o Registry guarda versões múltiplas do mesmo objeto e fornece resolução baseada na tag). Tradeoff: pode onerar a memória ao invés de singletons, mas essencial em plataformas plugáveis.

## 6. Problemas Encontrados
- Ao executar `pip install -e .[dev]` a restrição de versão requerida para python (`>=3.13`) exigiu um ajuste temporário ou adequação de ambiente local de sandbox que pode estar restrito à build anterior `3.12`. Para contornar, o ambiente executa sobre `3.12` temporariamente em runtimes passados para fins de validação no ambiente de commit do github, mas a diretiva no `pyproject.toml` segue rigorosa conforme especificação (`3.13`).

## 7. Recomendações para a próxima fase
* Adicionar validação em runtime contra os JSON schemas de contracts construídos (usar lib `jsonschema`).
* Ampliar a CLI (`tpm` Typer App) para invocar o loader do `tpm.yaml` (Exemplo: `tpm validate` para checkar syntax e conformidade da inicialização do projeto).
* Implementar mecanismos de auto-discovery/carregamento dinâmico (plugins entry_points) para os Registries preencherem a si mesmos usando instâncias detectadas de `Agent`, `Skill`, etc.
