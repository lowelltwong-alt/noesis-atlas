from __future__ import annotations
import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / 'scripts' / 'score_coherence.py'
spec = importlib.util.spec_from_file_location('score_coherence', module_path)
score_coherence = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(score_coherence)


def test_weighted_score_green_band():
    dims = {key: 0.9 for key in score_coherence.INTERNAL_WEIGHTS}
    assert round(score_coherence.weighted_score(dims, score_coherence.INTERNAL_WEIGHTS), 3) == 0.9
    assert score_coherence.band(0.9) == 'green'


def test_band_boundaries():
    assert score_coherence.band(0.86) == 'green'
    assert score_coherence.band(0.70) == 'yellow'
    assert score_coherence.band(0.50) == 'orange'
    assert score_coherence.band(0.20) == 'red'
