## MajiXorter

This is a dumb little project I made to bench test sorting a large csv file that is too large to read into memory. I think it scales O(n^2)..... Which is pretty bad, but it exchanges the necessaty for memory for higher CPU usage and disk I/O.

# Usage

`python majixorter.py unsorted.csv sorted.csv \"Column Heading\"`
