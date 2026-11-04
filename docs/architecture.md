# AWS architecture — editable Mermaid diagram

GitHub renders the following Mermaid source automatically. This diagram represents the lab's logical design, not every configured AWS setting.

```mermaid
flowchart TB
    visitor[Internet user / browser]
    igw[Internet Gateway]

    subgraph vpc["AWS VPC: StartupExcuses-vpc — 10.0.0.0/16 (eu-west-3)"]
        direction TB
        subgraph public["Public subnets"]
            direction LR
            pubA["eu-west-3a: 10.0.1.0/24<br/>EC2 t3.micro<br/>Nginx → Gunicorn → Flask"]
            pubB["eu-west-3b: 10.0.2.0/24<br/>Public subnet (no additional EC2 claimed)"]
        end
        subgraph private["Private database subnets / RDS subnet group"]
            direction LR
            priA["eu-west-3a: 10.0.3.0/24"]
            priB["eu-west-3b: 10.0.4.0/24"]
            rds[("RDS PostgreSQL<br/>startupexcuses-db<br/>db.t4g.micro / TCP 5432")]
        end
    end

    visitor -->|HTTP / web traffic| igw
    igw -->|Public route: 0.0.0.0/0| pubA
    pubA -->|Private VPC connection, TCP 5432| rds
    priA --- rds
    priB --- rds
    publicSG["Web security group<br/>Review HTTP and SSH ingress"] -.-> pubA
    dbSG["DB security group<br/>Restrict 5432 to web SG"] -.-> rds

    classDef publicNode fill:#e9f4ff,stroke:#2962a3,color:#102a43;
    classDef privateNode fill:#ecf8f0,stroke:#218555,color:#153a26;
    class pubA,pubB,igw publicNode;
    class priA,priB,rds privateNode;
```

**Routing clarification:** public subnets use an Internet Gateway default route; the private database subnets have only the local VPC route in the documented lab. The diagram does not imply that the database has its own public endpoint or an outbound NAT route. An RDS subnet group across two AZs does not alone prove Multi-AZ database deployment.
