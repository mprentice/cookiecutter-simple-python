from {{cookiecutter.project_slug}}.cli import main

def test_main():
    assert main("-v") is None
    assert main("-vv") is None
