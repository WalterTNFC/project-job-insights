from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # raise NotImplementedError

    read_jobs = read(path)
    industries = print(read_jobs)
    industries = set()
    for job in read_jobs:
        get_industry = job['industry']
        if not get_industry == '':
            industries.add(get_industry)
    return industries


data = "./data/jobs.csv"
teste = get_unique_industries(data)
print(teste)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
