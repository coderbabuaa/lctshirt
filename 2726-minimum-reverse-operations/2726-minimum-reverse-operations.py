IMPOSSIBLE = -1
EVEN, ODD = 0, 1
class Solution:
    def minReverseOperations(self, N: int, p: int, banned: List[int], k: int) -> List[int]:
        if k == 1 or len(banned) == N-1:
            numOps = [IMPOSSIBLE] * N
            numOps[p] = 0
            return numOps
        
        numOps = [IMPOSSIBLE] * N
        numOps[p] = 0
        
        remaining = [[], []]
        banned = set(banned)
        for pos in range(0, N, 2):
            if pos != p and pos not in banned:
                remaining[EVEN].append(pos)
            pos += 1
            if pos != p and pos not in banned:
                remaining[ODD].append(pos)
        
        # BFS
        numOp = 1
        p0s = [p]
        while p0s:
            p1s = []
            for p0 in p0s:
                i_lo = max(0, p0+1-k)
                i_hi = min(N-k, p0)
                p1_lo = p1_hi = k-1-p0
                p1_lo += 2*i_lo
                p1_hi += 2*i_hi
                parity = p1_lo & 0b1
                rem = remaining[parity]
                lo = bisect_left(rem, p1_lo)
                hi = bisect_right(rem, p1_hi)

                # Alt 1
                for j in reversed(range(lo, hi)):
                    p1 = rem.pop(j)
                    numOps[p1] = numOp
                    p1s.append(p1)

                # # Alt 2
                # for _ in range(hi - lo):
                #     p1 = rem.pop(lo)
                #     numOps[p1] = numOp
                #     p1s.append(p1)
            
            p0s = p1s
            numOp += 1
        
        return numOps