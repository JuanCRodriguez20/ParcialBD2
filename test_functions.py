from job_parcial2 import puntoA
from job_parcial2_b import get_info_eltiempo
from pytest_mock import mocker


# Tests that the function successfully downloads and stores web content in S3 bucket for each URL in content_to__download list. 
def test_happy_path_download_and_store(mocker):
    # Mocking boto3 client and urllib.request.urlopen
    mock_client = mocker.patch('boto3.client')
    mock_urlopen = mocker.patch('urllib.request.urlopen')
    mock_response = mocker.Mock()
    mock_response.read.return_value = b'Test content'
    mock_urlopen.return_value = mock_response

    # Calling function
    puntoA()

    # Asserting that put_object was called for each URL in content_to__download
    assert mock_client.return_value.put_object.call_count == 3

def test_properly_formatted_csv():
        html = "<div class='article-details'><div class='category-published'><a>Category</a></div><h3 class='title-container'><a href='link'>Title</a></h3></div>"
        expected_csv = "categoria, titulo, link\nCategory, Title, eltiempo.comlink\n"
        assert get_info_eltiempo(html) == expected_csv