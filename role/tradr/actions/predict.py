#prediction tools to help AI models make better decisions
from pandas import DataFrame

def get_moving_average(stock:DataFrame, window_size:int) -> DataFrame:
    """
    Calculate the moving average of a stock's closing prices.

    Parameters:
    stock (DataFrame): A pandas DataFrame containing stock data with a 'Close' column.
    window_size (int): The number of periods to calculate the moving average over.

    Returns:
    Series: A pandas Series containing the moving average values.
    """
    return stock['Close'].rolling(window=window_size).mean()


def get_rsi(stock:DataFrame, period:int=14) -> DataFrame:
    """
    Calculate the Relative Strength Index (RSI) of a stock's closing prices.

    Parameters:
    stock (DataFrame): A pandas DataFrame containing stock data with a 'Close' column.
    period (int): The number of periods to calculate the RSI over.

    Returns:
    Series: A pandas Series containing the RSI values.
    """
    delta = stock['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_previous_resistance_levels(stock:DataFrame, window_size:int=20) -> DataFrame:
    """
    Identify previous resistance levels in a stock's closing prices.

    Parameters:
    stock (DataFrame): A pandas DataFrame containing stock data with a 'Close' column.
    window_size (int): The number of periods to look back for resistance levels.

    Returns:
    Series: A pandas Series containing the resistance levels.
    """
    resistance_levels = stock['Close'].rolling(window=window_size).max()
    return resistance_levels

def get_previous_support_levels(stock:DataFrame, window_size:int=20) -> DataFrame:
    """
    Identify previous support levels in a stock's closing prices.

    Parameters:
    stock (DataFrame): A pandas DataFrame containing stock data with a 'Close' column.
    window_size (int): The number of periods to look back for support levels.

    Returns:
    Series: A pandas Series containing the support levels.
    """
    support_levels = stock['Close'].rolling(window=window_size).min()
    return support_levels

