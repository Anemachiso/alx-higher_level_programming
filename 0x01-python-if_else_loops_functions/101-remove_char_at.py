#!/usr/bin/python3
def remove_char_at(str, n):
	part1 = str[:n]
	part2 = str[n+1:]
	if n < 0:
	    return str
	else:
	    return part1 + parts2
