"""Functions for other modules (screen messages and error logger).

Has:
- elapsed time decorator
- logger
- progress bar

"""

import time

def create(year):
    prefix = "(%s)" % year
    def foo(*args):
        print (prefix, *args)
    return foo


def print_elapsed_time(foo):
    """Print execution time for *f* to screen."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = foo(*args, **kwargs)
        print("Time elapsed: %.1f seconds" % (time.time()-start_time))
        return result
    return wrapper


class GenericLogger():
    """Log errors while reading rows."""
    def __init__(self, filename):
        self.log_filename = filename

    def start(self):
        with open(self.log_filename, 'w') as f:
            print("Log started", file=f)

    def report(self, *msg):
        with open(self.log_filename, 'a') as f:
            print(*msg)
            print(*msg, file=f)


class Logger(GenericLogger):
    """Logger with predefined filename for error stream."""

    def __init__(self, year):
        filename = config.make_path_error_log(year)
        super().__init__(filename)


class Progress():
    """Minimal progress 'spinner'.
       See also <http://docs.astropy.org/en/v0.2/_generated/astropy.utils.console.Spinner.html#>
    """

    STEP = 100*1000

    def __init__(self):
        self.count = 0
        self.k = 0

    def next(self):
        self.count += 1
        self.k += 1
        if self.k == self.STEP:
            print("%7d lines read" % self.count)
            self.k = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


def pipe(gen):
    """Decorate *gen* with progress messages."""
    with Progress() as prog:
        for item in gen:
            prog.next()
            yield item
