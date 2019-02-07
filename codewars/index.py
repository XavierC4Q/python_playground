def solution(string, ending):
  a = len(ending)
  return string[- a:] == ending


def remove_duplicate_words(s):
    new_str = {}
    split_str = s.split()
    answer = ''
    for i in split_str:
      if not i in new_str:
        new_str[i] = True
        answer = answer + i + ' '

    return answer[: -1]

    
def reverse(a):
  copy = a[::-1]
  for i in range(len(copy)):
    copy[i] = copy[i][::-1]
  new_list = []
  start = 0
  copy_str = ''.join(copy)
  for x in a:
    new_list.append(copy_str[start: start + len(x)])
    start += len(x)
  return new_list
    
    
def repeater(string, n):
    return string * n

def DNAtoRNA(dna):
  return dna.replace('T', 'U')

def is_prime(num):
  if num < 0 or num < 2: return False
  if num == 2: return True
  count = 0
  half = int(round(num / 2))

  for i in range(1, half + 1):
    if count > 1: return False
    elif num % i == 0:
      count += 1
  return count == 1

print(is_prime(6))