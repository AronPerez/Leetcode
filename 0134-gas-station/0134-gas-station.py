class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        petrolpumps = list(zip(gas, cost))
        bestPump = 0
        currentPetrol = 0
        totalPetrol = 0

        for i in range(len(petrolpumps)):
            petrol, distance = petrolpumps[i]
            currentPetrol += petrol - distance
            totalPetrol += petrol - distance
            
            if currentPetrol < 0: # We reset and go to next one
                bestPump = i + 1
                currentPetrol = 0
            
        return bestPump if totalPetrol >= 0 else -1 
        