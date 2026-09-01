from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_coords = []
        start_pos = (0, 0)
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_pos = (r, c)
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                    
        k = len(litter_coords)
        if k == 0:
            return 0
            
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        target_mask = (1 << k) - 1
        
        best_energy = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        
        queue = deque()
        start_r, start_c = start_pos
        best_energy[start_r][start_c][0] = energy
        queue.append((start_r, start_c, 0, energy, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, e, moves = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                    continue
                
                ne = e - 1
                if ne < 0:
                    continue
                
                nmask = mask
                cell = classroom[nr][nc]
                
                if cell == 'R':
                    ne = energy
                elif cell == 'L':
                    nmask |= (1 << litter_map[(nr, nc)])
                
                if nmask == target_mask:
                    return moves + 1
                
                if ne <= best_energy[nr][nc][nmask]:
                    continue
                
                best_energy[nr][nc][nmask] = ne
                queue.append((nr, nc, nmask, ne, moves + 1))
                
        return -1