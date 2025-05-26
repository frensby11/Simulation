
class World:
    def __init__(self, width: int = 100, height: int = 100):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.subjects = {}

    def add_subject(self, subject_id: float, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] is None:
                self.grid[y][x] = subject_id
                self.subjects[subject_id] = (x, y)
                return True
        return False

    def remove_subject(self, subject_id: str) -> bool:
        if subject_id in self.subjects:
            x, y = self.subjects[subject_id]
            self.grid[y][x] = None
            del self.subjects[subject_id]
            return True
        return False

    def move_subject(self, subject_id: str, new_x: int, new_y: int) -> bool:
        if subject_id in self.subjects:
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                if self.grid[new_y][new_x] is None:
                    old_x, old_y = self.subjects[subject_id]
                    self.grid[old_y][old_x] = None
                    self.grid[new_y][new_x] = subject_id
                    self.subjects[subject_id] = (new_x, new_y)
                    return True
        return False

    def get_subject_position(self, subject_id: str) -> tuple:
        return self.subjects.get(subject_id, None)

    def get_subjects_in_range(self, x: int, y: int, radius: int) -> list:
        subjects = []
        for sy in range(max(0, y - radius), min(self.height, y + radius + 1)):
            for sx in range(max(0, x - radius), min(self.width, x + radius + 1)):
                if self.grid[sy][sx] is not None:
                    subjects.append((self.grid[sy][sx], sx, sy))
        return subjects
