class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0

        # Energy training
        total_energy = sum(energy)
        if initialEnergy <= total_energy:
            need = total_energy + 1 - initialEnergy
            ans += need
            initialEnergy += need

        # Experience training
        for exp in experience:
            if initialExperience <= exp:
                need = exp + 1 - initialExperience
                ans += need
                initialExperience += need

            initialExperience += exp

        return ans