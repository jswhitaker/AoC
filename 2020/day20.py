import re
from typing import List, Optional


########################################################################################################################
# Class for a single tile. Edges are based on sides of the un-rotated/ flipped input data.
#   000
#  3   1
#  3   1
#  3   1
#   222
########################################################################################################################
class Tile(object):
    def __init__(self, id_num, data):
        self.id_num = id_num
        # edges and data extraction from input
        edge_0 = ''
        edge_1 = ''
        edge_2 = ''
        edge_3 = ''
        data_list = []
        data_lines = data.split('\n')
        for i, line in enumerate(data_lines):
            if i == 0:
                edge_0 = line.rstrip()
            if i == (len(data_lines) - 1):
                edge_2 = line.rstrip()
            edge_1 += line[-1]
            edge_3 += line[0]
            data_list.append(line[1:-1])
        self.data = '\n'.join(data_list[1:-1])
        self.edges = edge_0, edge_1, edge_2, edge_3

    def __eq__(self, other):
        return self.id_num == other.id_num

    def __str__(self):
        return self.id_num

    def __repr__(self):
        return self.id_num

    def flip(self):
        self.data = flip_data(self.data)
        self.edges = self.edges[2], self.edges[1][::-1], self.edges[0], self.edges[3][::-1]

    def rotate(self):
        self.data = rotate_data(self.data)
        self.edges = self.edges[3][::-1], self.edges[0], self.edges[1][::-1], self.edges[2]

    # Used to match any edge of unmatched tiles to a given edge. Edge number is required to properly orientate the tile.
    def matches_any_edge(self, edge_num: int, edge_str: str):
        for i in range(4):
            if self.edges[edge_num] == edge_str:
                return True
            else:
                self.rotate()
        self.flip()
        for i in range(4):
            if self.edges[edge_num] == edge_str:
                return True
            else:
                self.rotate()
        return False


class Picture(object):
    rows: List[List[Tile]]

    def __init__(self, tiles: List[Tile]):
        self.unmatched = tiles
        self.rows = []

    def build_row(self, starting_tile):
        row = [starting_tile]
        head_complete = False
        tail_complete = False
        # build row from head fo row
        while not head_complete:
            head_edge = row[0].edges[3]
            curr_row_len = len(row)
            for tile in self.unmatched:
                if tile.matches_any_edge(1, head_edge):
                    row.insert(0, tile)
                    self.unmatched.remove(tile)
                    break
            if len(row) == curr_row_len:
                head_complete = True
        # Build row from tail of row, since it can no longer grow at the head.
        while not tail_complete:
            tail_edge = row[-1].edges[1]
            curr_row_len = len(row)
            for tile in self.unmatched:
                if tile.matches_any_edge(3, tail_edge):
                    row.insert(len(row), tile)
                    self.unmatched.remove(tile)
                    break
            if len(row) == curr_row_len:
                tail_complete = True
        return row

    def fix_picture(self):
        row = self.build_row(self.unmatched.pop())
        self.rows.append(row)
        top_match = self.__find_top_match()
        while top_match is not None:
            self.unmatched.remove(top_match)
            row = self.build_row(top_match)
            self.rows.insert(0, row)
            top_match = self.__find_top_match()
        bottom_match = self.__find_bottom_match()
        while bottom_match is not None:
            self.unmatched.remove(bottom_match)
            row = self.build_row(bottom_match)
            self.rows.insert(len(self.rows), row)
            bottom_match = self.__find_bottom_match()

    def __find_top_match(self) -> Optional[Tile]:
        for t in self.rows[0]:
            top_edge = t.edges[0]
            for u in self.unmatched:
                if u.matches_any_edge(2, top_edge):
                    return u
        return None

    def __find_bottom_match(self) -> Optional[Tile]:
        for t in self.rows[-1]:
            bottom_edge = t.edges[2]
            for u in self.unmatched:
                if u.matches_any_edge(0, bottom_edge):
                    return u
        return None

    def get_merged_image(self):
        tile_data_height = len(self.rows[0][0].data.split('\n'))
        str_rows: List[str] = [''] * len(self.rows) * tile_data_height
        index = 0
        for r in self.rows:
            for t in r:
                lines = t.data.split('\n')
                for i, l in enumerate(lines):
                    str_rows[index + i] += l
            index += tile_data_height
        return '\n'.join(str_rows)


def rotate_data(data: str) -> str:
    data_split = data.split('\n')
    data_split = list(zip(*data_split[::-1]))
    return '\n'.join([''.join(line) for line in data_split])


# Flips data top to bottom
def flip_data(data: str) -> str:
    return '\n'.join(reversed(data.split('\n')))


def find_monsters(data: str) -> int:
    found_monsters = 0
    row_length = len(data.split('\n', 1)[0])
    monster_length = 20
    for i in range(row_length - monster_length):
        n = i
        m = row_length - monster_length - i
        regex_pattern = f'^[.#]{{{n}}}[.#]{{18}}#[.#][.#]{{{m}}}$(?:\n|\r\n?)^[.#]{{{n}}}#[.#]{{4}}##[.#]{{4}}##[.#]{{4}}###[.#]{{{m}}}$(?:\n|\r\n?)^[.#]{{{n}}}[.#]#[.#]{{2}}#[.#]{{2}}#[.#]{{2}}#[.#]{{2}}#[.#]{{2}}#[.#]{{3}}[.#]{{{m}}}$'
        monsters = re.findall(regex_pattern, data, re.MULTILINE)
        found_monsters += len(monsters)
    return found_monsters


def main():
    tiles = []
    with open('inputs/20-input.txt') as input_file:
        data = input_file.read()
    raw_tiles = data.split('\n\n')
    for rt in raw_tiles:
        id_num, tile = tuple(rt.split('\n', 1))
        id_num = re.search(r'([0-9]+)', id_num)[0]
        tiles.append(Tile(id_num, tile))
    picture = Picture(tiles)
    picture.fix_picture()
    for r in picture.rows:
        print(r)
    merged = picture.get_merged_image()

    found_monsters = 0
    for _ in range(4):
        found_monsters = find_monsters(merged)
        if found_monsters > 0:
            break
        merged = rotate_data(merged)
    merged = flip_data(merged)
    if found_monsters == 0:
        for _ in range(4):
            found_monsters = find_monsters(merged)
            if found_monsters > 0:
                break
            merged = rotate_data(merged)

    print(f'\n{merged}')
    octothorpes = merged.count('#')
    # 15 `#` make up the monster in the images.
    return octothorpes - (found_monsters * 15)


if __name__ == '__main__':
    result = main()
    print(result)
