def split_text_by_player(text):
    lines = ([], [])
    player = 0
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        elif line == '0:':
            player = 0
        elif line == '1:':
            player = 1
        else:
            lines[player].append(line)

    return '\n'.join(lines[0]), '\n'.join(lines[1])