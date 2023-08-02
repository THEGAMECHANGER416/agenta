from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime
from enum import Enum

# ComparisonTableTypes = ["app_evaluation"]
class EvaluationTypeSettings(BaseModel):
    similarity_threshold: Optional[float]


class EvaluationType(str, Enum):
    auto_exact_match = "auto_exact_match"
    auto_similarity_match = "auto_similarity_match"
    auto_ai_critique = "auto_ai_critique"
    human_a_b_testing = "human_a_b_testing"
    human_scoring = "human_scoring"


class ComparisonTable(BaseModel):
    id: str
    status: str
    evaluation_type: EvaluationType
    evaluation_type_settings: Optional[EvaluationTypeSettings]
    variants: Optional[List[str]]
    app_name: str
    dataset: Dict[str, str] = Field(...)
    created_at: datetime
    updated_at: datetime


class EvaluationScenarioInput(BaseModel):
    input_name: str
    input_value: str


class EvaluationScenarioOutput(BaseModel):
    variant_name: str
    variant_output: str


class EvaluationScenario(BaseModel):
    comparison_table_id: str
    inputs: List[EvaluationScenarioInput]
    outputs: List[EvaluationScenarioOutput]
    vote: Optional[str]
    score: Optional[str]
    correct_answer: Optional[str]
    id: Optional[str]


class EvaluationScenarioUpdate(BaseModel):
    vote: Optional[str]
    score: Optional[str]
    outputs: List[EvaluationScenarioOutput]


class NewComparisonTable(BaseModel):
    evaluation_type: EvaluationType
    evaluation_type_settings: Optional[EvaluationTypeSettings]
    app_name: str
    variants: List[str]
    inputs: List[str]
    dataset: Dict[str, str] = Field(...)
    status: str = Field(...)


class DeleteComparisonTable(BaseModel):
    comparison_tables_ids: List[str]
