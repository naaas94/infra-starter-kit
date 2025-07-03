# INFRA STARTER KIT — ML/NLP PROJECT BOILERPLATE  
**Author**: Alejandro Garay  
**Project Type**: Modular MLOps-Ready Scaffolding  
**Stack**: Docker • Makefile • pytest • Black • Scikit-learn • Pandas  

---

## PROJECT PURPOSE

`infra-starter-kit` is a minimal, production-minded boilerplate designed to serve as the base infrastructure for real ML/NLP pipelines.  
It focuses on:

- Environment reproducibility via Docker  
- Modular, testable code layout  
- Linting and formatting out of the box  
- Makefile-based local automation  
- Seamless transition to Flyte, CI/CD, or cloud pipelines  

You can fork or clone this template to bootstrap any serious ML/NLP project.

---

## PROJECT STRUCTURE

<pre>
infra-starter-kit/
├── config/              # YAML or .env-based config
├── data/                # DO NOT COMMIT real data
├── docker/              # Dockerfile + supporting images
├── notebooks/           # Optional EDA or scratchpad notebooks
├── scripts/             # CLI entrypoints (e.g. dummy_run.py)
├── src/infra_kit/       # Your actual Python package
│   ├── __init__.py
│   ├── pipeline.py      # Dummy model pipeline
│   └── utils.py
├── tests/               # Unit tests
├── .env.example         # Copy to .env for local secrets
├── Makefile             # Helper commands (build, lint, test, etc.)
├── docker-compose.yml
├── requirements.txt
└── README.md
</pre>

---

## GETTING STARTED

### Installation

You only need Docker installed. No Python, no venv, no drama.

### Build and start container

```bash
make build
