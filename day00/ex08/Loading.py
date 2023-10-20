def ft_tqdm(lst: range) -> None:
    bar_length = 42
    total = len(lst)
    block = chr(0x2588)
    for i, item in enumerate(lst, start=1):
        progress = i / total
        filled_length = int(bar_length * progress)
        bar = f"|{block * filled_length}{' ' * (bar_length - filled_length)}|"
        print(f"\r{progress * 100:.0f}%{bar} {i}/{total}", end="")
        yield
    print()
