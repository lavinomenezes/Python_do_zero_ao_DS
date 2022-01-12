def set_currency(ax):
    """
    transform the numerical data in the y axis into monetary data
    """
    import locale
    locale.setlocale(locale.LC_ALL, 'English_United States.1252');
    f = lambda x: locale.currency(x, grouping=True)
    ax.set_yticks(ax.get_yticks().tolist())
    ax.set_yticklabels(map(f, ax.get_yticks().tolist()), fontweight="bold")
    return None