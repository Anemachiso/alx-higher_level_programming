#!/usr/bin/python3
def remove_char_at(str, n):
	if n < 0:
	   return str
	part1 = str[:n]
	part2 = str[n+1:]
	return part1 + parts2
