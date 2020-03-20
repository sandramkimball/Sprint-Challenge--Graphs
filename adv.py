from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


def explore_all_rooms(player, traversal_path):
    # Fill this out with directions to walk: ['n', 'n']
    traversal_path = []
    starting_room = player.current_room

    # player.current_room.id
    # player.current_room.get_exits()
    # player.travel(direction)

    def get_adj_rooms(self, starting_room): # current_room.get_exits() is same?
        if starting_room in self.rooms:
            return self.rooms[starting_room]
        else:
            print('Error: this room does not exist.')
            raise ValueException


    def bfs(self, starting_room, dest_point): #player.current_room.id
        # create queue
        q = Queue()
        # enqueu path to start
        q.append(starting_room)
        # create a set? dict? to store visited rooms
        visited = {}
        # while queue is full...
        while q.size() > 0:
            #dequeue first path
            path = q.dequeue()
            # grab room from end
            room = path[-1]
            # check if visited. if not...
            if room not in visited:
                #mark as visited
                visited.add(room)
                # check if is target: ? 
                if room == dest_point:
                    # dft(room) -- this go here?
                    return room
                #enqueu path to its neigbors
                for adj_rooms in self.get_adj_rooms(room):
                    path_copy = path.copy()
                    path_copy.enqueue()


    def dft(self, starting_room): 
        #create stack
        s = Stack()
        #push starting v
        s.push([starting_room]) #add .directions here?
        #create path for visited
        visited = {}
        #while stack is full:
        while s.size() > 0:
            #pop first vertx and check if visited
            path = s.pop()
            room_id = path[-1]
            if room_id not in visited:
                #mark as visited
                visited[room_id] = path
                #push neighbors onto stack
                for adj_rooms in self.get_adj_rooms[room_id]:
                    path_copy = path.copy()
                    path_copy.push(adj_rooms)
                    s.push(path_copy)
        return visited

    results = dft
    traversal_path.append(results)

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



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
