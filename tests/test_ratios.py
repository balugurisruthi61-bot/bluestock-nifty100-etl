from src.analytics.ratios import *


def test_net_profit_margin():
    assert net_profit_margin(100,1000)==10


def test_sales_zero():
    assert net_profit_margin(100,0)==None


def test_roe():
    assert return_on_equity(100,200,300)==20


def test_roa():
    assert return_on_assets(100,1000)==10