from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


class SourceMetadata(BaseModel):
    source_id: str
    title: str
    url: HttpUrl
    publisher: str
    publish_date: Optional[datetime]
    accessed_at: datetime
    excerpt: str
    reliability_notes: Optional[str] = None


class ArticleSection(BaseModel):
    title: str
    content: str
    citations: List[str] = Field(default_factory=list)


class ArticleOutput(BaseModel):
    overview: str
    key_points: List[str]
    sections: List[ArticleSection]
    implications: str
    limitations: str
    confidence_notes: str


class InfographicBlock(BaseModel):
    type: str
    heading: str
    content: str
    citation_markers: List[str] = Field(default_factory=list)


class InfographicSpec(BaseModel):
    title: str
    generated_at: datetime
    template: str
    blocks: List[InfographicBlock]


class ProvenanceInfo(BaseModel):
    retrieved_at: datetime
    last_accessed: datetime
    source_fetch_method: str
    query_terms: List[str]
    trace_id: str
    reliability_summary: str


class ResearchResult(BaseModel):
    result_id: str
    prompt: str
    created_at: datetime
    confidence: float = Field(..., ge=0.0, le=1.0)
    article: ArticleOutput
    infographic: InfographicSpec
    sources: List[SourceMetadata]
    provenance: ProvenanceInfo
