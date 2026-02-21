from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI

from .schemas import (
    ArticleOutput,
    ArticleSection,
    InfographicBlock,
    InfographicSpec,
    ProvenanceInfo,
    ResearchResult,
    SourceMetadata,
)

app = FastAPI(title="Research Infographic Studio Backend")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


def build_demo_research_result() -> ResearchResult:
    now = datetime.now(timezone.utc)

    sources = [
        SourceMetadata(
            source_id="source-1",
            title="AI research synthesis in 2025",
            url="https://example.com/ai-research-synthesis-2025",
            publisher="Research Digest",
            publish_date=datetime(2025, 1, 15, tzinfo=timezone.utc),
            accessed_at=now,
            excerpt="A meta-study highlighting best practices for rapid insight extraction in AI research.",
            reliability_notes="Peer-reviewed summary with citations to official conferences",
        ),
        SourceMetadata(
            source_id="source-2",
            title="Designing impactful infographics",
            url="https://designweekly.com/infographic-guidelines",
            publisher="Design Weekly",
            publish_date=datetime(2024, 10, 2, tzinfo=timezone.utc),
            accessed_at=now,
            excerpt="Guidelines for pairing narrative structure with visual cues to support retention.",
        ),
        SourceMetadata(
            source_id="source-3",
            title="Citing sources in multimedia deliverables",
            url="https://citationcorner.org/multimedia",
            publisher="Citation Corner",
            publish_date=datetime(2023, 8, 30, tzinfo=timezone.utc),
            accessed_at=now,
            excerpt="Checklist for matching inline references with shared resource lists.",
            reliability_notes="Maintained by librarians and educators",
        ),
    ]

    article = ArticleOutput(
        overview="AI-powered research briefs now take under two minutes by unifying prompt interpretation, source retrieval, and visualization planning.",
        key_points=[
            "Query expansion + search, claim extraction, and outline synthesis are orchestrated automatically.",
            "Infographic planning reuses the same source metadata to anchor visual claims with traceable citations.",
            "Exportable markdown + PNG packages are generated together so sharing is a single action.",
        ],
        sections=[
            ArticleSection(
                title="Detailed explanation",
                content="The pipeline runs three parallel workers: one expands the prompt into search terms, another fetches prioritized sources and claims, and the third crafts structured article sections with inline citations.",
                citations=["source-1", "source-3"],
            ),
            ArticleSection(
                title="Implications / applications",
                content="Researchers can start sharing slides and posts quickly because the article and infographic share the same source links, eliminating reconciliation work.",
                citations=["source-2"],
            ),
            ArticleSection(
                title="Limitations / uncertainties",
                content="While automated, the pipeline still flags low-confidence sources in the citations pane so users can decide whether to replace them.",
                citations=["source-3"],
            ),
        ],
        implications="Shareable content can now be produced while keeping every claim anchored to the original data, reducing follow-up research by days.",
        limitations="Very niche or proprietary sources still require explicit user guidance before the pipeline can surface them.",
        confidence_notes="Confidence is high for synthesized technical summaries but falls when any citation has low reliability notes.",
    )

    infographic = InfographicSpec(
        title="Research Pipeline Speedup",
        generated_at=now,
        template="multi-step-flow",
        blocks=[
            InfographicBlock(
                type="header",
                heading="Speeding from question to shareable insight",
                content="Pipeline coordinates search → article → infographic in under two minutes.",
                citation_markers=["source-1"],
            ),
            InfographicBlock(
                type="stat-card",
                heading="Sources per result",
                content="3 curated sources verified for relevance.",
                citation_markers=["source-1", "source-2", "source-3"],
            ),
            InfographicBlock(
                type="timeline",
                heading="Process steps",
                content="1. Prompt expansion  2. Source fetch  3. Article + infographic generation",
                citation_markers=["source-1", "source-2"],
            ),
        ],
    )

    provenance = ProvenanceInfo(
        retrieved_at=now,
        last_accessed=now,
        source_fetch_method="Rapid web search + curated list",
        query_terms=[
            "AI research workflows",
            "infographic storytelling",
            "citation-first content",
        ],
        trace_id=str(uuid4()),
        reliability_summary="Sources prioritized by reputed publications with librarian curation",
    )

    return ResearchResult(
        result_id=str(uuid4()),
        prompt="How can I summarize the latest research workflow for AI-generated infographics?",
        created_at=now,
        confidence=0.88,
        article=article,
        infographic=infographic,
        sources=sources,
        provenance=provenance,
    )


@app.get("/results/demo", response_model=ResearchResult)
async def demo_research_result():
    return build_demo_research_result()
