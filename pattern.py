def print_pattern():
    position = 1  # Posisi sekaranag
    tmp_string = "PATTERN PARKIR\n"
    for pos in rows:
        x1, y1 = pos
        tmp_list = []
        for pos1 in posList:
            x2, y2 = pos1
            if (x1 == x2 and y1 == y2) or (x1 == x2 + pixels_w and y1 == y2):
                tmp_list.append(pos)
        if position != no_w:
            if len(tmp_list) < 1:
                tmp_string += "_"
                # Empty
            else:
                tmp_string += "M"
                # Field
            position += 1
        else:
            tmp_string += "_/\n"
            position = 1
    print(tmp_string)
