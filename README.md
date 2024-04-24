## Snowpark Bug Tracker

This repository is used to track bugs and feature requests for the Snowpark project.

---

### Initial Setup

1. Clone the repository
2. Set your environment variables, using the example file: `.env.example`
3. Run the setup script: `$ bash scripts/setup.sh`

### Projects

#### Langchain Demo:

Problem: The project is designed to embed a query string or documents via langchain and sentence transformers. The project runs well locally, and deploys via snow-cli with no errors. When calling the procedures, a PyTorch exception is thrown:

```
OSError: /home/udf/13128080689/package.zip/torch/lib/libtorch_global_deps.so: cannot open shared object file: Not a directory in function EMBED_DOCUMENTS with handler procedures.embed_documents
```

Steps to reproduce:

1. Install the dependencies `$ pip install -r langchain_demo/requirements.txt`
2. Run the build and deploy script: `$ bash scripts/langchain_demo.sh`
3. Call the procedures in the demo script: `scripts/demo.sql`
