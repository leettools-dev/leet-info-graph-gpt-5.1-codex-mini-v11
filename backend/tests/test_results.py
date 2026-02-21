from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_demo_result_structure():
    response = client.get("/results/demo")
    assert response.status_code == 200

    payload = response.json()
    assert "article" in payload
    assert "infographic" in payload
    assert "sources" in payload

    sources = payload["sources"]
    assert isinstance(sources, list)
    assert sources

    source_ids = {source["source_id"] for source in sources}

    # Article citations should map to source identifiers
    sections = payload["article"]["sections"]
    for section in sections:
        for citation in section.get("citations", []):
            assert citation in source_ids

    # Infographic blocks should also reference the same sources
    blocks = payload["infographic"]["blocks"]
    for block in blocks:
        for marker in block.get("citation_markers", []):
            assert marker in source_ids
