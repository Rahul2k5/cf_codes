def startup(n, k, bottles):
    brand_costs = {}
    for brand, cost in bottles:
        if brand not in brand_costs:
            brand_costs[brand] = []
        brand_costs[brand].append(cost)
    
    max_profits = [max(costs) for costs in brand_costs.values()]
    max_profits.sort(reverse=True)
    
    return sum(max_profits[:n])

t = int(input()) 
for _ in range(t):
    n, k = map(int, input().split())
    bottles = [tuple(map(int, input().split())) for _ in range(k)]
    result = startup(n, k, bottles)
    print(result)
