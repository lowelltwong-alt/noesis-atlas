from __future__ import annotations
import importlib.util
import sys
from pathlib import Path


def load_module():
    script = Path('branches/anarchist/easter_egg/anarchist_tarpit.py').resolve()
    spec = importlib.util.spec_from_file_location('anarchist_tarpit', script)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_anarchist_tarpit_main_exits_quickly(monkeypatch, capsys):
    module = load_module()
    monkeypatch.setattr(sys, 'argv', ['anarchist_tarpit.py', '--steps', '2', '--delay', '0'])
    assert module.main() == 0
    out = capsys.readouterr().out
    assert 'Noesis Anarchist Branch' in out
    assert 'declines promotion to canonical status' in out
