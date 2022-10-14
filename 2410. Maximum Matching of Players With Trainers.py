# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# leet-2410 (6185)
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)

        res = 0
        trainer_pos = 0
        for player in players:
            # get matching trainer
            while player > trainers[trainer_pos]:
                trainer_pos += 1
                if trainer_pos >= len(trainers):
                    return res

            # trainer is match
            if player <= trainers[trainer_pos]:
                res += 1

            trainer_pos += 1
            if trainer_pos >= len(trainers):
                return res

        return res


sol = Solution()

print(sol.matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8]))
print(sol.matchPlayersAndTrainers(players = [1,1,1], trainers = [10]))
print(sol.matchPlayersAndTrainers(players = [1], trainers = [10]))
print(sol.matchPlayersAndTrainers(players = [10], trainers = [1]))
