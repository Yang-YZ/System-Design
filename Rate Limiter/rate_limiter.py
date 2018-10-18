class RateLimiter:
    
    def __init__(self):
        self.log = {}
        self.rate2sec = {"s": 1, "m": 60, "h": 60 * 60, "d": 24 * 60 * 60}
    
    """
    @param: {int} timestamp: an integer of current timestamp
    @param: {str} event: a string to distinct different event
    @param: {str} rate: a string with the format [integer]/[s/m/h/d]
    @param: {bool} increment: a bool value indicates whether we should increase the counter
    @return: {bool} true or false to indicate the event is limited or not
    """
    def is_ratelimited(self, timestamp, event, rate, increment):
        limit, unit = rate.split("/")

        count = self.count_event(timestamp, event, self.rate2sec[unit])
        
        if increment and count < int(limit):
            self.add_event(timestamp, event)

        return count >= int(limit)
    
    def add_event(self, timestamp, event):
        self.log[event] = self.log.get(event, []) + [timestamp]
    
    def count_event(self, timestamp, event, rate):
        visits = self.log[event]
        if len(visits) == 0 or visits[-1] <= timestamp - rate:
            return 0
        
        left, right = 0, len(visits) - 1
        # find the left boundary of time interval within the rate range
        for i in range(len(visits)):
            if visits[i] >= timestamp - rate:
                left = i
                break
            
        # find the right boundary of time interval within the rate range
        for j in range(len(visits) - 1, -1, -1):
            if visits[j] <= timestamp:
                right = j
                break
        
        return right - left + 1
