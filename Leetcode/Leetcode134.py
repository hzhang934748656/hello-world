
#BF
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        for i in range(n):
            tank = 0
            if gas[i] < cost[i]:
                continue
            tank += gas[i]
            j = (i + 1) % n
            while j != i:
                if j == 0:
                    tank -= cost[n-1]
                else:
                    tank -=cost[j-1]
                if tank < 0:
                    break
                tank += gas[j]
                j = (j + 1) % n
            if i ==0:
                tank -= cost[n-1]
            else:
                tank -= cost[i-1]
            if j == i and tank >= 0:
                return i
        return -1
