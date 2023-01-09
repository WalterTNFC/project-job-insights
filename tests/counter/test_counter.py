import pytest
from src.pre_built.counter import count_ocurrences

#  Será verificado se:
# Chamar a função count ocurrence passando dois parametros
# -path (string com caminhos de arquivos)
# -word (string -> palavra a ser contabilizada)

# garantir a contagem correta da palavra solicitada


path = "tests/mocks/jobs.csv"
path_error = "jobs_error.csv"


def test_counter():
    # pass
    # case insentitive
    assert count_ocurrences(path, "developer") == 3
    assert count_ocurrences(path, "DEVELOPER") == 3


def test_counter_type_error():
    with pytest.raises(TypeError):
        count_ocurrences(path)
        count_ocurrences("developer")


def test_counter_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        count_ocurrences(path_error, "developer")
