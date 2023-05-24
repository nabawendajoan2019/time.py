def sum_timestamps(timestamps):
    total_seconds = 0
    for timestamp in timestamps:
        minutes, seconds = map(int,timestamp.split(':'))
        total_seconds += minutes * 60 + seconds
        # Convert the total_seconds back to the MM:SS format
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        total_timestamp = f"{minutes:02d}{seconds:02d}"
        return total_timestamp
        def main():
            timestamps = ['01:30', '02:15', '03:45']
            total_timestamp = sum_timestamps(timestamps)
            print("sum of timestamps:",total_timestamp)
            