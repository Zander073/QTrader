# date format: '%Y-%m-%d'
TRAIN_START_DATE = "2009-01-06"
TRAIN_END_DATE = "2021-12-01"

TEST_START_DATE = "2021-12-02"
TEST_END_DATE = "2022-20-02"

DDPG_PARAMS = {'batch_size': 128, 'buffer_size': 1000, 'learning_rate': 0.001}

TICKER = [
  "AAPL"
]

INDICATORS = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
]
