class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]

        while queue:
            room = queue.pop(0)
            if room in visited:
                continue
            visited.add(room)
            queue.extend(rooms[room])

        return len(visited) == len(rooms)
        