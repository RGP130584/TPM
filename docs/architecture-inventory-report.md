# TPM Architecture Inventory Report (MCCA Runtime Track 3)

## 1. Full Project Tree
O layout da MCCA Runtime foundation após a TRACK 3 (Plugins, Versionamento, Observabilidade, Workflows e Security Runtime):
```text
.
├── README.md
├── docs
│   ├── adr
│   │   └── ADR-001-mcca-to-tpm.md.md
│   ├── architecture-report.md
│   ├── architecture-runtime-report.md
│   ├── capability-map.md
│   ├── coverage_summary.txt
│   ├── glossary.md
│   ├── mvp
│   │   └── mvp-v0.1.md
│   ├── parking-lot.md
│   ├── principles.md
│   ├── roadmap.md
│   ├── threat-model.md
│   ├── tree_inventory.txt
│   └── vision.md
├── pyproject.toml
├── src
│   └── tpm
│       ├── __init__.py
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
│       │   │   ├── __init__.py
│       │   │   └── agent_schema.json
│       │   ├── mcp
│       │   │   ├── __init__.py
│       │   │   └── mcp_schema.json
│       │   ├── skills
│       │   │   ├── __init__.py
│       │   │   └── skill_schema.json
│       │   └── transformers
│       │       ├── __init__.py
│       │       └── transformer_schema.json
│       ├── core
│       │   └── __init__.py
│       ├── hygiene
│       │   └── __init__.py
│       ├── models
│       │   ├── __init__.py
│       │   └── spec.py
│       ├── observability
│       │   ├── __init__.py
│       │   ├── ai_metrics
│       │   │   ├── __init__.py
│       │   │   └── models.py
│       │   ├── logs
│       │   │   ├── __init__.py
│       │   │   └── structured.py
│       │   ├── metrics
│       │   │   ├── __init__.py
│       │   │   └── interfaces.py
│       │   └── traces
│       │       ├── __init__.py
│       │       └── interfaces.py
│       ├── plugins
│       │   ├── __init__.py
│       │   ├── lifecycle
│       │   │   ├── __init__.py
│       │   │   └── interfaces.py
│       │   ├── loader
│       │   │   ├── __init__.py
│       │   │   └── core.py
│       │   ├── manifests
│       │   │   ├── __init__.py
│       │   │   └── model.py
│       │   └── validation
│       │       └── __init__.py
│       ├── registry
│       │   ├── __init__.py
│       │   ├── agents
│       │   │   ├── __init__.py
│       │   │   └── registry.py
│       │   ├── base.py
│       │   ├── mcps
│       │   │   ├── __init__.py
│       │   │   └── registry.py
│       │   ├── skills
│       │   │   ├── __init__.py
│       │   │   └── registry.py
│       │   └── transformers
│       │       ├── __init__.py
│       │       └── registry.py
│       ├── reports
│       │   └── __init__.py
│       ├── runtime
│       │   ├── __init__.py
│       │   ├── discovery
│       │   │   ├── __init__.py
│       │   │   └── service.py
│       │   ├── events
│       │   │   ├── __init__.py
│       │   │   └── models.py
│       │   ├── execution
│       │   │   ├── __init__.py
│       │   │   └── context.py
│       │   ├── interfaces.py
│       │   ├── lifecycle
│       │   │   ├── __init__.py
│       │   │   └── state.py
│       │   └── security
│       │       └── __init__.py
│       ├── schemas
│       │   └── __init__.py
│       ├── security
│       │   ├── __init__.py
│       │   ├── audit
│       │   │   ├── __init__.py
│       │   │   └── logger.py
│       │   ├── audit_runtime
│       │   │   ├── __init__.py
│       │   │   └── execution.py
│       │   ├── authorization
│       │   │   ├── __init__.py
│       │   │   └── rbac.py
│       │   ├── authorization_runtime
│       │   │   ├── __init__.py
│       │   │   └── model.py
│       │   ├── identity
│       │   │   └── __init__.py
│       │   ├── policies
│       │   │   ├── __init__.py
│       │   │   └── model.py
│       │   ├── policy_engine
│       │   │   ├── __init__.py
│       │   │   └── evaluator.py
│       │   └── secrets
│       │       ├── __init__.py
│       │       └── provider.py
│       ├── specs
│       │   ├── __init__.py
│       │   └── loader.py
│       ├── tenancy
│       │   ├── __init__.py
│       │   ├── context
│       │   │   └── __init__.py
│       │   ├── isolation
│       │   │   ├── __init__.py
│       │   │   └── abstractions.py
│       │   ├── models
│       │   │   ├── __init__.py
│       │   │   └── core.py
│       │   └── policies
│       │       └── __init__.py
│       ├── trust
│       │   └── __init__.py
│       ├── validators
│       │   ├── __init__.py
│       │   └── engine.py
│       ├── versioning
│       │   ├── __init__.py
│       │   ├── compatibility
│       │   │   ├── __init__.py
│       │   │   └── engine.py
│       │   ├── migration
│       │   │   ├── __init__.py
│       │   │   └── abstractions.py
│       │   ├── policies
│       │   │   ├── __init__.py
│       │   │   └── deprecation.py
│       │   └── semver
│       │       ├── __init__.py
│       │       └── model.py
│       └── workflows
│           ├── __init__.py
│           ├── definitions
│           │   ├── __init__.py
│           │   └── model.py
│           ├── engine
│           │   ├── __init__.py
│           │   └── interfaces.py
│           ├── execution
│           │   ├── __init__.py
│           │   └── model.py
│           └── models
│               └── __init__.py
└── tests
    ├── __init__.py
    ├── test_cli.py
    ├── test_observability.py
    ├── test_plugins.py
    ├── test_runtime.py
    ├── test_security_runtime.py
    ├── test_specs.py
    ├── test_versioning.py
    └── test_workflows.py

68 directories, 127 files
```

## 2. Package Inventory
- **CLI (`src/tpm/cli`)**: Entrada `tpm init` via typer.
- **Config (`src/tpm/config`)**, **Core (`src/tpm/core`)**, **Hygiene (`src/tpm/hygiene`)**, **Reports (`src/tpm/reports`)**: Pacotes placeholders originais para track de dados.
- **Models (`src/tpm/models`)**: Modelagem base (pydantic specs).
- **Validators (`src/tpm/validators`)**: `ValidationEngine` isolado das engines de runtime.

## 3. Runtime Inventory
- **Discovery (`src/tpm/runtime/discovery`)**: Resolução de `ComponentDiscovery`.
- **Events (`src/tpm/runtime/events`)**: Event model abstrato com fields para Kafka: `BaseEvent`, `AgentEvent`, `SkillEvent`, etc.
- **Execution & Lifecycle (`src/tpm/runtime/execution|lifecycle`)**: Interface genérica `IRuntimeComponent`, tracker `ExecutionContext` e lifecycle states.

## 4. Registry Inventory
- **Registries (`src/tpm/registry/*`)**: Instâncias estendidas de `BaseRegistry` em memory (Agentes, MCPS, Skills, Transformers). Suporte genérico a version control de dependências.

## 5. Contract Inventory
- **Contracts (`src/tpm/contracts/*`)**: JSON Schemas validados (`mcp_schema.json`, `skill_schema.json`, `transformer_schema.json`, `agent_schema.json`) usados como contrato de interoperabilidade.

## 6. Plugin Inventory
- **Plugins (`src/tpm/plugins`)**:
  - `PluginManifest` com definitions base, dependency arrays e ids.
  - Abstrações de interfaces de ciclo de vida de plugin (`IPluginLifecycle`).
  - `PluginLoader` interagindo via callback methods (on_load, on_enable) sincronizado com os registries (Agent, Skill, etc).

## 7. Workflow Inventory
- **Workflows (`src/tpm/workflows`)**:
  - `WorkflowDefinition`: Representa a declaração de execução (passos, next_steps).
  - `WorkflowExecution`: Trackeia state no fluxo temporal guardando `LifecycleState` para cada task resolvida (`StepExecution`).
  - `IWorkflowEngine`: Engine manager (A ser instanciado em uma library como Celery, Temporal).

## 8. Security Inventory
- **Security & Authorization (`src/tpm/security`)**:
  - RBAC Base e Security Policies definidas em definitions originais.
  - Runtime: `RuntimeAuthorizationContext` validando tenant active nas calls.
  - `SecretProvider` preparando suporte a Keycloak e Hashicorp Vault para token resolution.
- **Audit Runtime**: Envio de eventos contínuo a uma task.

## 9. Observability Inventory
- **Observability (`src/tpm/observability`)**:
  - Logs Estruturados (`StructuredLogger`) focados na saída ELK/Datadog.
  - Metrics e Traces em interface abstrata.
  - Ricos modelos AI: `AIMetrics` computando tamanho contextual, latências e custos de inferências em tokens nativamente para orquestradores GPT/LLaMA.

## 10. Test Coverage Summary
O pytest local indica sucesso. As suítes garantem os modelos construídos (`test_specs`, `test_cli`, `test_runtime`, `test_plugins`, `test_observability`, `test_versioning`, `test_workflows`).
```text
```

## 11. Remaining Gaps before MCCA Runtime v1
1. Integrações concretas (Ex: O `StructuredLogger` apenas faz print. Precisamos atrelar à stdlib de logging ou structlog; o `SecretProvider` precisa de binding no python-hvac pro Vault).
2. Refatoração de concorrência. Workflows devem suportar processamento assíncrono real via `asyncio`.
3. Inserir conectores do Apache Kafka ou RabbitMQ nas pontas dos Events (`BaseEvent`).
4. Resolver imports e plugins auto-descobertos usando entry points do python (`importlib.metadata`).

## 12. Recommended roadmap for TRACK 4
**Track 4 - Execution Platform & SDK (v1.0):**
- Finalizar Bindings e integrações com ORM (Ex: SQLAlchemy ou Motor) de metadados dos tenants.
- Publicar a documentação do SDK.
- Adicionar o binding do `Celery` ou `Temporal.io` na `IWorkflowEngine`.
- Integrar os `SecretProvider`s a libs de Cloud nativa.
- Lançar os sub-repositórios dos plugins base do ecossistema.
