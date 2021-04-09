# coding=utf-8
# 4▹ Wyświetl 3 losowe cytaty

with open('cytat.txt', 'r') as fopen:
  lines = fopen.readlines()

import random
selected_lines = random.sample(lines, 3)

for selected_line in selected_lines:
    print(selected_line)
