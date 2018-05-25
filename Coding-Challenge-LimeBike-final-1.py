import bisect
import unittest


class ItemCounter:
    """Counter to process rides and print the items in transit at each unique time interval."""
    def __init__(self):
        self.ride_cnt = 0;
        self.start_time = []
        self.end_time = []
        self.orig_item = {}
        self.intervals = []
        self.item_counter = {}

    def process_ride(self, ride):
        """Processes a ride object and updates the item time intervals."""
        if not ride.items:
            return
        self._add_time(ride.start_time)
        self._add_time(ride.end_time)
        self.start_time.append(ride.start_time)
        self.end_time.append(ride.end_time)
        self.orig_item[self.ride_cnt] = ride.items
        self.ride_cnt = self.ride_cnt+1
        
