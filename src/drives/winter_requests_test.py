from .winter_requests import WinterRequest


def test_requests_id_anime(request) :
    url = 'https://api.myanimelist.net/v2/anime/season/2006/winter?offset=1&limit=100'
    response_contest = {'teste': 'teste'}
    wr = WinterRequest()
    request_response = wr.requests_id_anime('2016', 'winter', 1, 1)
    assert 'status_code' in request_response
    assert 'json' in request_response
    assert request_response['status_code'] == 200