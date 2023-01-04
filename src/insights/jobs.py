from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
# Referência: https://docs.python.org/pt-br/3/library/csv.html#module-contents
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            jobs = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(jobs)
    except OSError:
        raise FileNotFoundError("File not found")


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    jobs_read = read(path)
    unique_jobs = set()
    for job in jobs_read:
        unique_jobs.add(job["job_type"])
    return list(unique_jobs)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
