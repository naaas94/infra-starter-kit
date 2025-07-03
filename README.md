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
```

### Enter the container

```bash
make bash
```

### Run dummy pipeline

```bash
python -m scripts.dummy_run
```

### Run tests

```bash
pytest
```

### Lint and format

```bash
make lint
```

#### STATUS AND ROADMAP

This repo is considered ready for forking or cloning.

Dummy pipeline and tests included for functional validation.

- Next steps (optional):
- Replace dummy model with your own
- Add real config.yaml + .env
- Plug into Flyte, MLflow, or CI/CD

#### DESIGN PRINCIPLES

- Keep your infra boring. Your model is the complex part.
- Everything should run with make build && make bash.
- Don’t mix notebooks with pipelines unless you’re debugging.
- One repo = one pipeline = one purpose.