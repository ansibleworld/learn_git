import requests

def trigger_jenkins_job(jenkins_url: str, job_name: str, auth_token: str) -> bool:
    if not isinstance(jenkins_url , str):
        raise ValueError
    if not isinstance(job_name, str):
        raise ValueError
    if not jenkins_url.strip():
        raise ValueError
    if not job_name.strip():
        raise ValueError
    if not isinstance(auth_token , str):
        raise ValueError
    if not auth_token.strip():
        raise ValueError

    jenkins_url = jenkins_url.strip()
    job_name = job_name.strip()

    url = f"{jenkins_url}/job/{job_name}/build"

    headers = {
        "Authorization" : f"Bearer {auth_token}"
    }

    try :
        response = requests.post(url , headers=headers)
        return response.status_code == 201
    except requests.RequestException:
        return False