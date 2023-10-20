def ft_statistics(*args: any, **kwargs: any) -> None:

    def mean(list):
        return sum(list) / len(list) if len(list) else None

    def median(list):
        return sorted(list)[int(len(list) / 2)] if len(list) else None

    def quartile(list):
        return [sorted(list)[int(len(list) / 4)], sorted(list, reverse=True)[int(len(list) / 4)]] if len(list) else None

    def var(list):
        return sum([(x - sum(list) / len(list)) ** 2 for x in list]) / len(list) if len(list) else None

    def std(list):
        return (sum([(x - sum(list) / len(list)) ** 2 for x in list]) / len(list)) ** .5 if len(list) else None

    def calc(f, arg):
        for a in arg:
            if not isinstance(a, (int, float)):
                print('ERROR')
                return
        print(f.__name__, ':', f(arg))

    for kwarg in kwargs.values():
        if (kwarg == 'mean' or 'median' or 'quartile' or 'var' or 'std') and (not len(args)):
            print('ERROR')
        elif kwarg == 'mean':
            calc(mean, list(args))
        elif kwarg == 'median':
            calc(median, list(args))
        elif kwarg == 'quartile':
            calc(quartile, list(args))
        elif kwarg == 'var':
            calc(var, list(args))
        elif kwarg == 'std':
            calc(std, list(args))
