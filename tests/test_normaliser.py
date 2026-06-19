import sys
import os

sys.path.append(os.path.abspath("src"))
from etl.normaliser import normalize_year, normalize_ticker

def test_normalize_year_2012():
    assert normalize_year("Dec 2012") == "2012"

def test_normalize_year_2014():
    assert normalize_year("Mar 2014") == "2014"

def test_normalize_ticker_abb():
    assert normalize_ticker("abb") == "ABB"

def test_normalize_ticker_spaces():
    assert normalize_ticker("  tcs  ") == "TCS"
def test_normalize_year_2015():
    assert normalize_year("Mar 2015") == "2015"

def test_normalize_year_2016():
    assert normalize_year("Mar 2016") == "2016"

def test_normalize_year_2017():
    assert normalize_year("Mar 2017") == "2017"

def test_normalize_year_2018():
    assert normalize_year("Mar 2018") == "2018"

def test_normalize_year_2019():
    assert normalize_year("Mar 2019") == "2019"

def test_normalize_year_2020():
    assert normalize_year("Mar 2020") == "2020"

def test_normalize_year_2021():
    assert normalize_year("Mar 2021") == "2021"

def test_normalize_year_2022():
    assert normalize_year("Mar 2022") == "2022"

def test_normalize_year_2023():
    assert normalize_year("Mar 2023") == "2023"

def test_normalize_year_2024():
    assert normalize_year("Mar 2024") == "2024"
def test_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_infosys():
    assert normalize_ticker("infy") == "INFY"

def test_ticker_hdfc():
    assert normalize_ticker("hdfc") == "HDFC"

def test_ticker_reliance():
    assert normalize_ticker("reliance") == "RELIANCE"

def test_ticker_uppercase():
    assert normalize_ticker("ABB") == "ABB"

def test_ticker_mixed_case():
    assert normalize_ticker("AbB") == "ABB"

def test_ticker_left_space():
    assert normalize_ticker(" ABB") == "ABB"

def test_ticker_right_space():
    assert normalize_ticker("ABB ") == "ABB"

def test_ticker_both_spaces():
    assert normalize_ticker(" ABB ") == "ABB"
def test_ticker_number():
    assert normalize_ticker("123") == "123"

def test_year_string():
    assert normalize_year("Year 2024") == "2024"

def test_year_dec():
    assert normalize_year("Dec 2020") == "2020"

def test_year_mar():
    assert normalize_year("Mar 2021") == "2021"

def test_year_jun():
    assert normalize_year("Jun 2022") == "2022"

def test_year_sep():
    assert normalize_year("Sep 2023") == "2023"
def test_ticker_wipro():
    assert normalize_ticker("wipro") == "WIPRO"

def test_ticker_lt():
    assert normalize_ticker("lt") == "LT"

def test_ticker_itc():
    assert normalize_ticker("itc") == "ITC"

def test_ticker_axis():
    assert normalize_ticker("axis") == "AXIS"

def test_year_2010():
    assert normalize_year("Mar 2010") == "2010"

def test_year_2011():
    assert normalize_year("Mar 2011") == "2011"

def test_year_2013():
    assert normalize_year("Mar 2013") == "2013"

def test_year_2009():
    assert normalize_year("Dec 2009") == "2009"