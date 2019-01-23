class Company
    def __init__(self, row):
        self.row = row

    @property
    def name(self):
        return f"{self.row.title} ({self.row.org})"    