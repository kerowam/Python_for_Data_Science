def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 58

    for i, elem in enumerate(lst, start=1):
        filled_length = bar_length \
            if total == 0 else int(bar_length * i / total)
        if i < total:
            bar = '=' * (filled_length - 1) + '>' + '.' * \
                (bar_length - filled_length)
        else:
            bar = '=' * (bar_length - 1) + '>'

        percent = 100 if total == 0 else int(i * 100 / total)
        print(f'\r{percent:3d}%|[{bar}]| {i}/{total}', end='', flush=True)
        yield elem

    print()
