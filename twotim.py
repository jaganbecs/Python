from datetime import datetime, time as datetime_time, timedelta
def time_diff(start, end):
    if isinstance(start, datetime_time): 
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) 
        assert end > start
        return end - start
for time_range in ['10:33:26-11:15:49', '23:55:00-00:25:00']:
    s, e = [datetime.strptime(t, '%H:%M:%S') for t in time_range.split('-')]
    print(time_diff(s, e))
    assert time_diff(s, e) == time_diff(s.time(), e.time())
