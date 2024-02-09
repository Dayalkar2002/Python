def min_players_to_be_shot(N, K, heights):
    heights.sort()
    min_players = 0
    for height in heights:
        if height > K:
            break
        min_players += 1
    return N - min_players

# Input reading
T = int(input("Enter the test Cases").strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    heights = list(map(int, input().strip().split()))
    print(min_players_to_be_shot(N, K, heights))


