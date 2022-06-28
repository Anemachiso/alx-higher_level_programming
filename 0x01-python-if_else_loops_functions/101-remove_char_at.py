#!/usr/bin/python3
def remove_char_at(str, n):
	tmp = n
	if n < 0:
	   tmp = tmp * -1
	part1 = str[:tmp]
	part2 = str[tmp+1:]
	return part1 + parts2
