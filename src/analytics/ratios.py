def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity, reserves):
    total_equity = equity + reserves

    if total_equity <= 0:
        return None

    return (net_profit / total_equity) * 100


def return_on_assets(net_profit, total_assets):

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100


def return_on_capital_employed(ebit, equity, reserves, borrowings):

    capital = equity + reserves + borrowings

    if capital <= 0:
        return None

    return (ebit / capital) * 100