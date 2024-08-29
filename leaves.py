class Leave:
    def __init__(self, leave_id: int, start_date: date, end_date: date, leave_type: str, status: str):
        self.leave_id = leave_id
        self.start_date = start_date
        self.end_date = end_date
        self.type = leave_type
        self.status = status

    def apply_leave(self):
        # Logic to apply for a leave
        pass