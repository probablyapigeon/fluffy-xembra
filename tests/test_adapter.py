import importlib
import sys
from modules.run_engine import Engine


def test_gemma_backend_returns_string():
    e = Engine(backend="gemma")
    line = e.step()
    assert isinstance(line, str)
    assert line.strip() != ""


def test_openai_fallback_when_missing(monkeypatch):
    # Simulate modules.xembra_llm missing by temporarily removing it from sys.modules
    monkeypatch.setitem(sys.modules, 'modules.xembra_llm', None)
    e = Engine(backend="openai")
    # Should not raise, and should return a gemma fallback line
    line = e.step()
    assert isinstance(line, str)
    assert line.strip() != ""
