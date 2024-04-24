from __future__ import annotations
from typing import List
from snowflake.snowpark import Session

from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings


DEFAULT_MODEL_NAME = 'snowflake/snowflake-arctic-embed-l'
DEFAULT_MODEL_KWARGS = {'device': 'cpu'}
DEFAULT_ENCODE_KWARGS = {'normalize_embeddings': True}


def _extend_defaults(model_name: str, model_kwargs: dict, encode_kwargs: dict):
    if model_name == '':
        model_name = DEFAULT_MODEL_NAME
    if model_kwargs == {}:
        model_kwargs = DEFAULT_MODEL_KWARGS
    if encode_kwargs == {}:
        encode_kwargs = DEFAULT_ENCODE_KWARGS
    return model_name, model_kwargs, encode_kwargs


def _initialize_model(model_name: str, model_kwargs: dict, encode_kwargs: dict):
    print("Initializing Model...")

    # Get Model Defaults
    _model_name, _model_kwargs, _encode_kwargs = _extend_defaults(
        model_name,
        model_kwargs,
        encode_kwargs
    )

    print("Model Settings:")
    print(f"Model Name: {_model_name}")
    print(f"Model Kwargs: {_model_kwargs}")
    print(f"Encode Kwargs: {_encode_kwargs}")

    # Initialize Model
    return HuggingFaceEmbeddings(
        model_name=_model_name,
        model_kwargs=_model_kwargs,
        encode_kwargs=_encode_kwargs
    )


def embed_documents(
    session: Session,
    documents: List[str],
    model_name: str = '',
    model_kwargs: dict = {},
    encode_kwargs: dict = {}
) -> List[List[float]]:
    print("Starting Embed Documents...")
    # Intialize the Embedding Model
    model = _initialize_model(model_name, model_kwargs, encode_kwargs)
    # Embed The Documents
    print("Embedding Documents...")
    return model.embed_documents(documents)


def embed_query(
    session: Session,
    query: str,
    model_name: str = '',
    model_kwargs: dict = {},
    encode_kwargs: dict = {}
) -> List[List[float]]:
    print("Starting Embed Query...")

    # Intialize the Embedding Model
    model = _initialize_model(model_name, model_kwargs, encode_kwargs)

    # Embed The Query
    print("Embedding Query...")
    return model.embed_query(query)
