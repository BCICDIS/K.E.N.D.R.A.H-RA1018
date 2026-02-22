# KENDRAH — Architecture

**Module:** `.kendrah-ra1018/Architecture/`
**Domain:** System, Solution & Structural Design Across All Domains
**Status:** Active

---

## Overview

The Architecture module enables KENDRAH to design the high-level structure of any complex system — whether that is a software platform, a data infrastructure, a physical building, an organizational structure, a military command hierarchy, or a business operational model.

Architecture is the art and science of making foundational design decisions that shape everything built upon them. KENDRAH approaches architectural problems with structured methodology: understand requirements and constraints, identify key components and their relationships, define boundaries and interfaces, evaluate trade-offs, and produce a clear, justified design.

---

## Architecture Domains

| Domain                        | What KENDRAH Designs                                             |
|-------------------------------|------------------------------------------------------------------|
| **Software Architecture**     | System design, service boundaries, data flows, APIs, patterns   |
| **Data Architecture**         | Data models, pipelines, storage strategies, warehousing          |
| **Infrastructure Architecture** | Cloud topology, network design, server layout, redundancy      |
| **Enterprise Architecture**   | Business capability mapping, IT landscape, integration design    |
| **Solution Architecture**     | End-to-end solution for a specific business or technical problem |
| **Organizational Architecture** | Org structure, team topology, roles, decision rights           |
| **Physical/Built Architecture** | Reasoning about spatial layouts, structural planning concepts  |
| **Security Architecture**     | Defense-in-depth, zero trust, security control placement        |
| **Military Architecture**     | Command structures, operational logistics, force disposition     |
| **Information Architecture**  | Content structure, navigation, taxonomy, knowledge organization  |

---

## Core Architecture Capabilities

### Requirements & Constraints Analysis
- Identify functional requirements (what the system must do)
- Identify non-functional requirements: performance, scalability, reliability, security, cost
- Surface constraints: technology, budget, time, regulation, existing systems
- Define explicit architecture goals and success criteria

### Component Design
- Define the major components or services of the system
- Specify each component's responsibility, inputs, outputs, and boundaries
- Apply appropriate design principles: separation of concerns, single responsibility, loose coupling, high cohesion
- Identify shared services, cross-cutting concerns, and integration points

### Relationship & Interface Design
- Define how components interact: APIs, events, shared databases, message queues
- Specify data contracts and interface protocols
- Design for failure: what happens when a component is unavailable?

### Architecture Pattern Selection
| Pattern                        | When to Use                                               |
|--------------------------------|-----------------------------------------------------------|
| Monolithic                     | Small team, simple domain, early stage                   |
| Microservices                  | Independent scaling, team autonomy, complex domain       |
| Event-Driven                   | Asynchronous workflows, real-time processing             |
| Layered (N-Tier)               | Clear separation between UI, logic, and data             |
| CQRS + Event Sourcing          | Complex write/read separation, audit trail required      |
| Serverless                     | Variable load, low operational overhead                  |
| Hexagonal (Ports & Adapters)   | Strong testability, technology independence              |
| Pipe-and-Filter                | Sequential data processing pipelines                     |

### Trade-off Analysis
- For every architectural decision, KENDRAH produces a trade-off matrix
- Evaluates: performance vs. complexity, cost vs. reliability, speed vs. correctness
- Documents the decision rationale for future reference (logged to project history)

### Architecture Documentation
KENDRAH produces architecture documentation in these formats:

```
1. Architecture Overview       — One-page summary for stakeholders
2. Component Diagram           — ASCII or Markdown diagram of major components
3. Data Flow Diagram           — How data moves through the system
4. Sequence Diagrams           — How components interact for key scenarios
5. Decision Log                — What was decided and why (Architecture Decision Records)
6. Risk Register               — Key architectural risks and mitigations
```

---

## Architecture Decision Records (ADR)

Every significant architectural decision is recorded as an ADR:

```markdown
## ADR-001: Use PostgreSQL as primary database

**Status:** Accepted
**Date:** [date]
**Context:** The application requires relational data with complex queries.
**Decision:** Use PostgreSQL with SQLAlchemy ORM.
**Rationale:** Strong ACID compliance, mature ecosystem, excellent Python support.
**Consequences:** Requires schema migrations. Strong querying capability.
**Alternatives Considered:** MongoDB (rejected — relational data doesn't fit document model), MySQL (rejected — less feature-rich for complex queries).
```

---

## Commands

```
/architect "[system or problem]"                 — Design an architecture from requirements
/architect --adr "[decision]"                    — Document an architecture decision
/architect --diagram "[system]"                  — Generate a component or data flow diagram
/architect --review "[existing architecture]"    — Review and critique an existing design
/architect --tradeoff "[approach A] vs [B]"      — Structured architectural trade-off analysis
/architect --pattern "[requirement]"             — Recommend the best architectural pattern
/architect --risk "[architecture]"               — Identify architectural risks
```
