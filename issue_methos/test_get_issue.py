import unittest
import requests
import xmltodict


class TestGetIssue(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        id = 'API-1'
        url = self.base_url + '/issue/' + id
        response = requests.get(url, auth=self.creds)
        response_dict = xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], id)

    def test_get_issue_invalid_id(self):
        url = self.base_url + '/issue/' + 'ZZZZZZ'
        r = requests.get(url, auth=self.creds)

        self.assertEquals(r.status_code, 403)


if __name__ == '__main__':
    unittest.main()
