import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file

# Chamar a função read_brazilian_file
# Receber a path = "tests/mocks/brazilians_jobs.csv"
# Retornar uma lista de dicionários em inglês -> Usar compreensão de lista

path = "tests/mocks/brazilians_jobs.csv"
path_error = "file_error.csv"


def test_brazilian_jobs():
    # pass
    jobs = read_brazilian_file(path)

    for job in jobs:
        assert "título" not in job
        assert "salario" not in job
        assert "tipo" not in job


def test_word_translation(path):
    jobs = read_brazilian_file(path)

    for job in jobs:
        assert "title" not in job
        assert "salary" not in job
        assert "type" not in job


def test_error_file():
    with pytest.raises(FileNotFoundError):
        read_brazilian_file(path_error)
