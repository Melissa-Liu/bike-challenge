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
    
    def _add_time(self, new_time):
        # Helper function to add time interval into sorted list
        time_index = bisect.bisect(self.intervals, new_time)
        if (time_index > 0):
            if (self.intervals[time_index - 1] != new_time):
                self.intervals.insert(time_index, new_time)
        else:
            self.intervals.insert(time_index, new_time)
