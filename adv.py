from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
from util import Stack, Queue

world = World()

# MAPS
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# MAP INTO DICT
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# world.print_rooms()

player = Player(world.starting_room)


# 1. traverse a path
# 2. at end of rd, go back to first room with unexplored exit
# 3. loop(?)
traversal_path = []
mapDictionary = {}

def get_adj_rooms(self, starting_room): # current_room.get_exits() is same?
    if starting_room in self.rooms:
        return self.rooms[starting_room]
    else:
        print('Error: this room does not exist.')
        raise ValueException


def bfs(starting_room_id): #player.current_room.id
    q = Queue()
    q.enqueue([starting_room_id])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        room = path[-1]
        if room not in visited:
            visited.add(room)
            for direction in mapDictionary[room]:
                if mapDictionary[room][direction] is '?':
                    return path
                if mapDictionary[room][direction] not in visited:
                    path_copy = list(path)
                    path_copy.append(mapDictionary[room][direction])
                    q.enqueue(path_copy)

            # for adj_rooms in self.get_adj_rooms(room):
            #     path_copy = path.copy()
            #     path_copy.enqueue()


def dft(self, starting_room): 
        s = Stack()
        s.push([starting_room]) #add .directions here?
        visited = {}
        while s.size() > 0:
            path = s.pop()
            room_id = path[-1]
            if room_id not in visited:
                visited[room_id] = path
                for adj_rooms in self.get_adj_rooms[room_id]:
                    path_copy = path.copy()
                    path_copy.push(adj_rooms)
                    s.push(path_copy)
        return visited

def explore_all_rooms(room_graph, player):
    starting_room = player.current_room
    starting_room_id = player.current_room.id
    opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    room_count = 0

    while len(mapDictionary) != len(room_graph):
        current_room = player.current_room
        room_id = current_room.id
        room_dict = {}

        if room_id not in mapDictionary:
            for i in current_room.get_exits():
                room_dict[i] = '?'

            if traversal_path:
                prev_room = opposite_directions[traversal_path[-1]]
                room_dict[prev_room] = room_count
            mapDictionary[room_id] = room_dict

        else: 
            room_dict = mapDictionary[room_id]

        all_exits = list()
        for direction in room_dict:
            if room_dict[direction] is '?':
                all_exits.append(direction)

        if len(all_exits) != 0:
            random.shuffle(all_exits)
            direction = all_exits[0]
            traversal_path.append(direction)

            player.travel(direction)
            new_room = player.current_room
            mapDictionary[current_room.id][direction] = new_room.id
            new_room_id = current_room.id
        else:
            next_room = bfs(room_id)

            if next_room is not None and len(next_room) > 0:
                for i in range(len(next_room)-1):
                    for direction in mapDictionary[next_room[i]]:
                        if mapDictionary[next_room[i]][direction] == next_room[i+1]:
                            traversal_path.append(direction)
                            player.travel(direction)
            else:
                break

    # player.current_room.id
    # player.current_room.get_exits()
    # player.travel(direction)

explore_all_rooms(room_graph, player)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")




# UNCOMMENT TO WALK AROUND
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
