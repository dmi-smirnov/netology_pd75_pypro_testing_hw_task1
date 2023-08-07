import pytest

import input_data
from tasks import task1, task2, task3


@pytest.mark.parametrize(
  'input_data, expected_result',
  [
    (input_data.task1, 
      [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
      ]
    )
  ]
)
def test_task1(input_data, expected_result):
  result = task1(input_data)

  # result must be list
  assert isinstance(result, list)

  for visit in result:
    # visit must be dict
    assert isinstance(visit, dict)

    # visit dict must contain only 1 element
    assert len(visit) == 1

    # visit dict value must be list
    visit_dict_value = list(visit.values())[0]
    assert isinstance(visit_dict_value, list)

    # The second element of visit dict value must be 'Россия'
    assert visit_dict_value[1] == 'Россия'

  # result must equal expected result
  assert result == expected_result


@pytest.mark.parametrize(
  'input_data, expected_result',
  [
    (input_data.task2, [98, 35, 213, 54, 119, 15])
  ]
)
def test_task2(input_data, expected_result):
  result = task2(input_data)

  # result must be list
  assert isinstance(result, list)

  # result list must contain more than 0 elements
  assert len(result) > 0

  # result list must contain only integer numbers
  for elem in result:
    assert isinstance(elem, int)

  # result list must contain unique numbers
  assert len(result) == len(set(result))

  # result must equal expected result
  assert result == expected_result


@pytest.mark.parametrize(
  'input_data, expected_result',
  [
    (input_data.task3, {2: 43, 3: 57})
  ]
)
def test_task3(input_data, expected_result):
  result = task3(input_data)

  # result must be dict
  assert isinstance(result, dict)

  # result must contain more than 0 elements
  assert len(result) > 0

  # result dict keys and values must be integer
  for k, v in result.items():
    assert isinstance(k, int)
    assert isinstance(v, int)
  
  # result must equal expected result
  assert result == expected_result