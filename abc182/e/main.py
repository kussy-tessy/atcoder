#!/usr/bin/env python3

H, W, N, M = map(int,(input().split()))
# ABs = []
# CDs = []
# for _ in range(N):
#     ABs.append(tuple(map(int,(input().split()))))
# for _ in range(M):
#     CDs.append(tuple(map(int,(input().split()))))

grid = [[0] for i in range(W)] * H

# https://zenn.dev/wapa5pow/articles/abc182-e-466c22605203cd42efd4
