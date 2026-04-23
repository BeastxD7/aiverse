"""SynthData engine — synthetic NLP dataset generation pipeline."""

from .config import JobConfig, load_config
from .pipeline import JobResult, run_job

__all__ = ["JobConfig", "JobResult", "load_config", "run_job"]
