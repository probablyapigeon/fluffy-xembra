from modules.run_engine import Engine


def test_engine_step():
    eng = Engine(seed=42)
    line = eng.step()
    assert isinstance(line, str)
    assert line.strip() != ""
