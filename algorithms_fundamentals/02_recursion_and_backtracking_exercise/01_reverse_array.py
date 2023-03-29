# https://judge.softuni.org/Contests/Practice/Index/3460#0

def reverse_arr(seq, idx):
    if idx == len(seq) // 2:
        return
    swap_idx = len(seq) - 1 - idx
    seq[idx], seq[swap_idx] = seq[swap_idx], seq[idx]
    reverse_arr(seq, idx + 1)


arr = input().split()
reverse_arr(seq=arr, idx=0)
print(*arr, sep=" ")
