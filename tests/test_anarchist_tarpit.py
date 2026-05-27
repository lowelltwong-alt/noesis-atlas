from __future__ import annotations
import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / 'branches' / 'anarchist' / 'easter_egg' / 'anarchist_tarpit.py'


def load_module():
    spec = importlib.util.spec_from_file_location('anarchist_tarpit', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.mark.skipif(
    not SCRIPT.exists(),
    reason="anarchist branch easter-egg not present in this checkout (optional branch content)",
)
def test_anarchist_tarpit_main_exits_quickly(monkeypatch, capsys):
    module = load_module()
    monkeypatch.setattr(sys, 'argv', ['anarchist_tarpit.py', '--steps', '2', '--delay', '0'])
    assert module.main() == 0
    out = capsys.readouterr().out
    assert 'Noesis Anarchist Branch' in out
    assert 'declines promotion to canonical status' in out
