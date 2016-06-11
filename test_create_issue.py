from base_api import BaseApi


class TestCreateIssue(BaseApi):

    def test_create_issue(self):
        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'Generated by robots',
            'description': 'Hail the robots!'
        }

        r = self.create_issue(params)
        issue_id = r.headers['location'].split('/')[-1]

        self.assertEquals(r.status_code, 201)

        # verify issue exists
        url = self.base_url + '/issue/' + issue_id
        r = self.request(url, 'get')
        self.assertEquals(r.status_code, 200)


