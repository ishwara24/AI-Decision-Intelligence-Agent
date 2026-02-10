def profit(sales, cost):
    return sales - cost


def profit_margin(sales, cost):
    if sales == 0:
        return 0
    return (sales - cost) / sales


def discount_impact(sales, discount_percent):
    return sales * (discount_percent / 100)
