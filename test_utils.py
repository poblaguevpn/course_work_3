from utils import get_data, get_filtered_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{
        'date': '2019-07-03T18:35:29.512364',
        'description': 'Перевод организации',

    }]