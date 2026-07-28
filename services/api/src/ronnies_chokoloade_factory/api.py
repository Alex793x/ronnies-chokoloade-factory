"""HTTP surface for ronnies-chokoloade-factory (an ``api:python`` service).

A minimal FastAPI application exposing a health endpoint. Run it with::

    uvicorn ronnies_chokoloade_factory.api:app --reload

FastAPI ships via the ``api`` extra (the ``dev`` extra includes it)::

    pip install -e ".[api]"

Owned by the Energy department.
"""

from __future__ import annotations

from fastapi import FastAPI

from ronnies_chokoloade_factory import __version__

app = FastAPI(
    title="ronnies-chokoloade-factory",
    description="Verdens bedste italienske chokolade is",
    version=__version__,
)


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    """Liveness/readiness probe.

    Returns:
        A small JSON object reporting service status and version.
    """
    return {"status": "ok", "service": "ronnies-chokoloade-factory", "version": __version__}
