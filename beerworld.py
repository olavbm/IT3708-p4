import random

size = [30, 15]
tracker_width = 5

class Beer(object):
    def __init__(self):
        self.board = {}
        self.spawn_object()
        self.tracker_pos = random.randrange(size[0])

    def spawn_object(self):
            self.object_pos = random.randrange(0, size[0])
            self.object_width = random.randint(1, 6)
            self.object_height = size[1]

    def modify_on_action(self, action):
        self.tracker_pos = (self.tracker_pos + action) % size[0]

        result = 'N'
        if self.object_height == 0:
            visible = sum(self.sensor_cells())
            if visible == 0:
                result = 'N'  # miss
            elif (visible == self.object_width) and self.object_width < tracker_width:
                result = 'S'  # capture
            else:
                result = 'B'  # crash

            self.spawn_object()

        self.object_height -= 1

        self.board['object_pos'] = self.object_pos
        self.board['object_width'] = self.object_width
        self.board['object_height'] = self.object_height
        self.board['tracker_pos'] = self.tracker_pos

        return result

    # Get the new sensors cells in accordance with shadows made by the objects above.
    def sensor_cells(self):
        cells = []
        for i in range(tracker_width):
            sensor_pos = ((self.tracker_pos+i) % size[0])
            object_end = self.object_pos + self.object_width
            wrap_end = object_end % size[0]
            cells.append(
                    (self.object_pos <= sensor_pos < object_end)
                    or ((sensor_pos < wrap_end) and (wrap_end < self.object_pos)))

        return cells
