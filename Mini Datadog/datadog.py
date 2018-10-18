class Datadog:
    
    def __init__(self):
        self.count = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.count.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        cut = timestamp - 5 * 60
        
        # binary search
        left, right = 0, len(self.count) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.count[mid] <= cut:
                left = mid + 1
            else:
                right = mid - 1
        
        return len(self.count) - left
