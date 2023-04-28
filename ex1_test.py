import get_a_point_for_writing_your_name as name_point
import calculate_rmse as rmse

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is())  > 1 

def test_rmse():
    predictions = [1, 2, 3, 4, 5]
    targets = [1, 2, 3, 4, 5]

    assert rmse.rmse(predictions, targets) == 0

    predictions = [2, 3, 4, 5, 6]
    targets = [1, 2, 3, 4, 5]

    assert rmse.rmse(predictions, targets) == 1

