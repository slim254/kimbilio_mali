# Kimbilio Mali Architecture Documentation

## System Overview
Kimbilio Mali is built on a modular client-server architecture separating the high-performance React frontend from the robust Python backend service.

### 1. Frontend Architecture
- Built with React, TypeScript, and TailwindCSS.
- Utilizes component-driven design for dashboards, charts, and data tables.

### 2. Backend Architecture
- RESTful API endpoints handling users, properties, rentals, expenses, transactions, and market trends.
- Relational database schema optimized for fast financial aggregations and cash flow calculations.

### 3. Deployment & Containerization
- Fully containerized using Docker with multi-stage builds.
- Orchestrated via `docker-compose` for seamless local development and cloud deployment.
