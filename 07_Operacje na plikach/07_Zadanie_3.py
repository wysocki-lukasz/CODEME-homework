# coding=utf-8
# 3▹ Wyświetl tylko 5 pierwszych linii

with open('cytat.txt', 'r') as fopen:
  lines = fopen.readlines()

expected_lines = 5
for l in range(expected_lines):
  print(lines[l])