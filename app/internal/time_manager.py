import time


class TimeManager:

    @staticmethod
    def get_ts() -> int:
        return int(time.time())
