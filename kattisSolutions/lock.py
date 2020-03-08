
from sys import stdin

for line in stdin:
  if line.rstrip() == '0 0 0 0':
    break
  start, fst, snd, thd = map(int, line.rstrip().split())
  angle = 1080 + 9 * (
    (start - fst if start >= fst else 40 - fst + start)
    + (snd - fst if snd >= fst else snd + 40 - fst)
    + (snd - thd if snd >= thd else 40 - thd + snd)
  )
  print(angle)

