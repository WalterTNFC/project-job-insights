from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # raise NotImplementedError

    read_jobs = read(path)
    list_salaries = []
    for job in read_jobs:
        salary = job["max_salary"]
        if not salary == "" and salary.isnumeric():
            list_salaries.append(int(salary))
    sort_salaries = sorted(list_salaries)
    max_salary = sort_salaries[len(sort_salaries) - 1]
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # raise NotImplementedError

    read_job = read(path)
    list_salaries = []
    for job in read_job:
        salary = job["min_salary"]
        if not salary == "" and salary.isnumeric():
            list_salaries.append(int(salary))
    sort_salaries = sorted(list_salaries)
    min_salary = sort_salaries[0]
    return min_salary


data = "./data/jobs.csv"
teste = get_min_salary(data)
print(teste)


def validation(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError('Job must have valid min_salary and max_salary')

    # Referência:
    # https://www.geeksforgeeks.org/convert-integer-to-string-in-python/
    verify_min_salary = str(job["min_salary"]).isnumeric()
    verify_max_salary = str(job["max_salary"]).isnumeric()
    if verify_min_salary is False or verify_max_salary is False:
        raise ValueError('Salaries values must be numeric type')

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError('min value canot be greater than max value')

    if str(salary).lstrip('-').isnumeric() is False:
        raise ValueError('salary must have only numerics values')
    return("All validations done!")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validation(job, salary)
    if (int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])) is False:
        return False
    return True


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    # raise NotImplementedError

    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError as error:
            print(error)

    return filtered_jobs
