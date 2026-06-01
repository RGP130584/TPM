# TPM Runtime Architecture Report (MCCA Runtime v0.x)

## 1. Visão Geral
Este documento cobre as definições iniciais da segunda track arquitetural ("Runtime Architecture"). O foco foi preparar os pilares lógicos de execução, gerenciamento de ciclo de vida (lifecycle), multi-tenancy, segurança interna e modelagem de eventos de um ambiente que operará sobre o projeto.

## 2. Componentes Entregues

### 2.1. Runtime Architecture
* **Lifecycle**: Adição do enumerador `LifecycleState` padronizando os estados possíveis (`INITIALIZED`, `STARTING`, `RUNNING`, `STOPPING`, `STOPPED`, `FAILED`).
* **Interfaces**: Estabelecida `IRuntimeComponent` obrigando implementações a lidar com contexto seguro através de `start()` e liberação via `stop()`.
* **Execution**: Implementação do `ExecutionContext` transportando rastros sobre as requisições em tempo de execução.
* **Discovery**: Adicionado o `ComponentDiscovery` para agir como proxy abstrato sob os registries desenvolvidos na primeira fase, providenciando resolução estrita a componentes atrelados por `component_type` (ex: agentes, skills).

### 2.2. Event Architecture
* Abstrações estruturadas e tipadas de eventos usando `Pydantic` no módulo `runtime.events.models`.
* O modelo `BaseEvent` traz suporte padrão para timestamps `UTC`, metadados (preparação de headers de serialização para broker) e payload `dict`.
* Estruturado com subclasses para uso transparente em um Message Broker como **Kafka**: `AgentEvent`, `SkillEvent`, `TransformerEvent`, `MCPEvent` e `SecurityEvent`.

### 2.3. Security Architecture
* **RBAC & Authorization**: Implementação estrutural de roles e granularidade baseada em `Permission` (Resource + Action) no modelo de RBAC.
* **Policies**: `SecurityPolicy` implementa decisões baseadas no esquema *allow/deny*.
* **Audit Logs**: Interfaces e definições `AuditLogger` obrigam integrações futuras a gravarem em coletores os eventos do tipo `SecurityEvent`.

### 2.4. Tenancy Architecture
* **Isolamento de Domínio**: Modelos hierárquicos entre `Tenant -> Workspace -> Environment` com validação provida via pydantic.
* **Enforcement (IsolationContext)**: Componentes obrigados a processar `tenant_id` atestados através da interface abstrata de `IsolationContext`.

## 3. Remaining Gaps before MCCA Runtime v1
Para que a runtime saia da abstração e execute fluxos ponta a ponta na v1, as seguintes lacunas estruturais precisam de foco arquitetural:
1. **Engine de Mensageria Concreta:** Conectar o `BaseEvent` a um consumer/producer Kafka real com tópicos particionados por tenant.
2. **Context Var Enforcement:** Em um ambiente async em Python, o `tenant_id` e o `workspace_id` do ExecutionContext precisam ser atrelados transparentemente via `contextvars`, ou propagados explicitamente em middlewares injetores, para evitar cross-tenant leakage.
3. **Execution Runtime (Worker Engine):** Criar os *Executors* propriamente ditos que consomem um `IRuntimeComponent` do Discovery e o iniciam num Task/Thread pool em infraestrutura de Cloud.
4. **Resolução de Segredos Dinâmicos:** A estrutura atual conta com `src/tpm/security/secrets/` contudo falta implementação do *resolver* para provedores como AWS Secrets Manager, HashiCorp Vault, ou SO Envs para que Skills e Agentes extraiam chaves de API contextuais com base no Tenant isolado.
5. **Autenticação:** A autorização (RBAC) está modelada, mas falta atrelar um token JWT ao tenant_id na borda de um roteador (Gateway).
