from project.room import Room


class Hotel:
    def __init__(self,name):
        self.name = name
        self.rooms = []




    @property
    def guests(self):
        guests = 0
        for guest_num in self.rooms:
            guests += guest_num.guests
        return guests


    @classmethod
    def from_stars(cls,stars_count):
        return cls(f"{stars_count} stars Hotel")


    def add_room(self,room:Room):
        self.rooms.append(room)

    def take_room(self,room_number,people):
        room = [x for x in self.rooms if room_number == x.number][0]
        room.take_room(people)


    def free_room(self,room_number):
        room = [room for room in self.rooms if room_number == room.number][0]
        room.free_room()


    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"

        return result