

#Dynamic Programming (DP) with HashSet optimization

def AbilityToCrossRiver(stones):
    #Quick reject if the second stone is not at position 1
    if stones[1] != 1:
        return False
    
    stone_positions = set(stones)
    last_stone = stones[-1]
    
    #DP dictionary to store reachable jump sizes for each stone
    dp = {stone: set() for stone in stones}
    dp[0].add(0)  # starting position
    
    #Iterate through stones
    for stone in stones:
        for jump in dp[stone]:
            # Try next possible jumps (k-1, k, k+1)
            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0:
                    next_pos = stone + next_jump
                    if next_pos == last_stone:
                        return True
                    if next_pos in stone_positions:
                        dp[next_pos].add(next_jump)
    
    return False


#Example for  test
if __name__ == "__main__":
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    print(AbilityToCrossRiver(stones))  # Expected output: True

    stones = [0,1,2,3,4,8,9,11]
    print(AbilityToCrossRiver(stones))  # Expected output: False
