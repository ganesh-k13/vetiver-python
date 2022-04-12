import pytest 

from vetiver.mock import get_mock_data, get_mock_model
from vetiver.pin_read_write import vetiver_pin_read, vetiver_pin_write
from vetiver.vetiver_model import VetiverModel
import sklearn
import pins

# Load data, model
X_df, y = get_mock_data()
model = get_mock_model().fit(X_df, y)


def test_board_pin_write():
    v = VetiverModel(model=model, ptype_data=X_df,
        model_name="model", versioned=None)
    board = pins.board_folder(path=".")
    vetiver_pin_write(board=board, model=v)
    assert isinstance(board.pin_read("model"), sklearn.dummy.DummyRegressor)
