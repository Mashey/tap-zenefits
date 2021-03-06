import json
import requests

class ZenefitsClient:
    BASE_URL = "https://api.zenefits.com"

    def __init__(self, api_key):
        self._client = requests.Session()
        self._client.headers.update({'Authorization': api_key})

    def fetch_departments(self, company_id, starting_after=None):
        url = f"{self.BASE_URL}/core/companies/{company_id}/departments"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()

    def fetch_employments(self, starting_after=None):
        url = f"{self.BASE_URL}/core/employments"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()

    def fetch_people(self, company_id, starting_after=None):
        url = f"{self.BASE_URL}/core/companies/{company_id}/people"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()

    def fetch_time_durations(self, starting_after=None):
        url = f"{self.BASE_URL}/time_attendance/time_durations"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()

    def fetch_payruns(self, starting_after=None):
        url = f"{self.BASE_URL}/payroll/payruns"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()

    def fetch_pay_stubs(self, starting_after=None):
        url = f"{self.BASE_URL}/payroll/payrun_pay_stubs"
        params = { "starting_after": starting_after } if starting_after else None
        return self._client.get(url, params=params).json()


