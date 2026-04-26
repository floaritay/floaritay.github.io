# import pulp
# import math
# import matplotlib.pyplot as plt
# import numpy as np

# # --- 1. 参数设置 ---
# WAREHOUSES = {
#     'W1': {'loc': (45, 25), 'stock': 100},
#     'W2': {'loc': (20, 75), 'stock': 100},
#     'W3': {'loc': (70, 75), 'stock': 100}
# }
# CUSTOMERS = [
#     {'id': 1, 'loc': (35, 35), 'demand': 1}, {'id': 2, 'loc': (15, 50), 'demand': 4}, {'id': 3, 'loc': (10, 70), 'demand': 22},
#     {'id': 4, 'loc': (15, 85), 'demand': 8}, {'id': 5, 'loc': (25, 55), 'demand': 6}, {'id': 6, 'loc': (30, 45), 'demand': 10},
#     {'id': 7, 'loc': (25, 90), 'demand': 7}, {'id': 8, 'loc': (20, 95), 'demand': 24}, {'id': 9, 'loc': (35, 65), 'demand': 24},
#     {'id': 10, 'loc': (45, 95), 'demand': 8}, {'id': 11, 'loc': (40, 70), 'demand': 3}, {'id': 12, 'loc': (55, 80), 'demand': 18},
#     {'id': 13, 'loc': (60, 70), 'demand': 8}, {'id': 14, 'loc': (65, 85), 'demand': 19}, {'id': 15, 'loc': (75, 95), 'demand': 12},
#     {'id': 16, 'loc': (85, 65), 'demand': 14}, {'id': 17, 'loc': (95, 90), 'demand': 9}, {'id': 18, 'loc': (85, 75), 'demand': 2},
#     {'id': 19, 'loc': (90, 40), 'demand': 16}, {'id': 20, 'loc': (95, 55), 'demand': 7}, {'id': 21, 'loc': (55, 15), 'demand': 6},
#     {'id': 22, 'loc': (45, 10), 'demand': 11}, {'id': 23, 'loc': (65, 10), 'demand': 14}, {'id': 24, 'loc': (25, 15), 'demand': 15},
#     {'id': 25, 'loc': (10, 25), 'demand': 16}, {'id': 26, 'loc': (85, 45), 'demand': 16}, {'id': 27, 'loc': (85, 30), 'demand': 16},
#     {'id': 28, 'loc': (95, 25), 'demand': 16}, {'id': 29, 'loc': (75, 20), 'demand': 14}, {'id': 30, 'loc': (20, 80), 'demand': 2},
#     {'id': 31, 'loc': (15, 10), 'demand': 10}
# ]
# VEHICLE_CAPACITY = 50
# MAX_DISTANCE = 200
# COST_PER_KM = 1.0

# # 求解器参数
# SOLVER_TIME_LIMIT = 120  # 增加时间限制
# MIP_GAP = 0.02          # 允许2%的求解间隙

# # --- 2. 辅助函数 ---
# def calculate_distance(p1, p2): 
#     return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# def assign_customers_to_warehouses(customers, warehouses):
#     assigned = {w_id: [] for w_id in warehouses}
#     for customer in customers:
#         closest_warehouse = min(warehouses.keys(), key=lambda w: calculate_distance(customer['loc'], warehouses[w]['loc']))
#         assigned[closest_warehouse].append(customer)
#     return assigned

# # --- 3. 求解器核心算法 ---
# def solve_vrp_for_warehouse(warehouse_id, warehouse_loc, customers):
#     # 创建客户ID列表和映射
#     customer_ids = [c['id'] for c in customers]
#     customer_data = {c['id']: c for c in customers}
    
#     # 估算需要的车辆数
#     total_demand = sum(c['demand'] for c in customers)
#     max_vehicles = max(2, math.ceil(total_demand / VEHICLE_CAPACITY))
#     print(f"仓库 {warehouse_id}: 总需求={total_demand}, 车辆容量={VEHICLE_CAPACITY}, 预估最大车辆数={max_vehicles}")
    
#     # 节点定义：仓库为0，客户为1,2,3...
#     nodes = [0] + list(range(1, len(customer_ids) + 1))  # 0是仓库，1到n是客户
#     depot = 0
#     customer_nodes = list(range(1, len(customer_ids) + 1))
    
#     # 位置和距离映射
#     node_locations = {0: warehouse_loc}
#     for i, c_id in enumerate(customer_ids):
#         node_locations[i+1] = customer_data[c_id]['loc']
    
#     # 距离矩阵
#     dist_matrix = {}
#     for i in nodes:
#         for j in nodes:
#             if i != j:
#                 dist_matrix[(i, j)] = calculate_distance(node_locations[i], node_locations[j])
    
#     # 需求映射
#     demands = {0: 0}  # 仓库需求为0
#     for i, c_id in enumerate(customer_ids):
#         demands[i+1] = customer_data[c_id]['demand']
    
#     # 定义变量
#     x = {}  
#     u = {} 
    
#     for k in range(max_vehicles):
#         for i in nodes:
#             for j in nodes:
#                 if i != j:
#                     x[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
#             if i != 0:  # depot doesn't have load variable
#                 u[(i, k)] = pulp.LpVariable(f"u_{i}_{k}", lowBound=0, upBound=VEHICLE_CAPACITY, cat='Continuous')

#     # 创建问题
#     prob = pulp.LpProblem(f"VRP_{warehouse_id}", pulp.LpMinimize)
    
#     # 目标函数：最小化总距离
#     prob += pulp.lpSum(dist_matrix[(i, j)] * x[(i, j, k)] for i in nodes for j in nodes for k in range(max_vehicles) if i != j)
    
#     # 每个客户必须被访问一次（出度=1）
#     for j in customer_nodes:
#         prob += pulp.lpSum(x[(i, j, k)] for i in nodes for k in range(max_vehicles) if i != j) == 1
    
#     # 每个客户必须离开一次（入度=1）
#     for i in customer_nodes:
#         prob += pulp.lpSum(x[(i, j, k)] for j in nodes for k in range(max_vehicles) if i != j) == 1
    
#     # 每辆车从仓库出发最多一次
#     for k in range(max_vehicles):
#         prob += pulp.lpSum(x[(0, j, k)] for j in customer_nodes) <= 1
    
#     # 每辆车回到仓库最多一次
#     for k in range(max_vehicles):
#         prob += pulp.lpSum(x[(i, 0, k)] for i in customer_nodes) <= 1
    
#     # 流量平衡：如果车辆k访问客户i，则必须离开客户i
#     for i in customer_nodes:
#         for k in range(max_vehicles):
#             prob += pulp.lpSum(x[(j, i, k)] for j in nodes if j != i) == pulp.lpSum(x[(i, j, k)] for j in nodes if j != i)
    
#     # 容量约束
#     for k in range(max_vehicles):
#         prob += pulp.lpSum(demands[j] * x[(i, j, k)] for i in nodes for j in customer_nodes if i != j) <= VEHICLE_CAPACITY
    
#     # 距离约束
#     for k in range(max_vehicles):
#         prob += pulp.lpSum(dist_matrix[(i, j)] * x[(i, j, k)] for i in nodes for j in nodes if i != j) <= MAX_DISTANCE
    
#     # 子回路消除约束 
#     for k in range(max_vehicles):
#         for i in customer_nodes:
#             for j in customer_nodes:
#                 if i != j:
#                     prob += u[(i, k)] - u[(j, k)] + VEHICLE_CAPACITY * x[(i, j, k)] <= VEHICLE_CAPACITY - demands[j]
    
#     # 使用Gurobi求解器
  
#     import gurobipy as gp
#     from gurobipy import GRB
#     print("使用 Gurobi 求解器...")
#     solver = pulp.GUROBI(msg=1, timeLimit=SOLVER_TIME_LIMIT, MIPGap=MIP_GAP)
    
#     # 求解
#     prob.solve(solver)
    
#     print(f"求解状态: {pulp.LpStatus[prob.status]}")
#     if pulp.LpStatus[prob.status] in ['Optimal', 'Feasible']:
#         print(f"目标值: {pulp.value(prob.objective):.2f}")
#     else:
#         print("求解失败或不可行")
#         return [], 0
    
#     # 重构路径
#     routes = []
#     for k in range(max_vehicles):
#         route = []
#         # 找到从仓库出发的路径
#         for j in customer_nodes:
#             if pulp.value(x[(0, j, k)]) > 0.5:
#                 current = j
#                 route.append(customer_ids[current-1])  # 将节点编号转换为客户ID
#                 break
        
#         if route:  # 如果这辆车有从仓库出发的路径
#             # 追踪路径直到回到仓库
#             while True:
#                 next_node = None
#                 for j in nodes:
#                     if j != current and pulp.value(x[(current, j, k)]) > 0.5:
#                         next_node = j
#                         break
                
#                 if next_node is None or next_node == 0:  # 回到仓库或没有下一个节点
#                     break
                
#                 route.append(customer_ids[next_node-1])  # 将节点编号转换为客户ID
#                 current = next_node
            
#             if route:
#                 routes.append(route)
    
#     objective_value = pulp.value(prob.objective) if pulp.value(prob.objective) is not None else 0
#     return routes, objective_value

# # --- 4. 主程序与可视化 ---
# def main():
#     # 步骤1: 分配顾客
#     assigned_customers = assign_customers_to_warehouses(CUSTOMERS, WAREHOUSES)
    
#     all_final_routes = []
#     total_min_cost = 0

#     # 步骤2: 对每个仓库的子问题进行优化
#     for w_id, customers in assigned_customers.items():
#         if not customers:
#             continue
            
#         print(f"\n--- 正在为仓库 {w_id} 优化路径 ---")
#         print(f"分配的顾客: {[c['id'] for c in customers]}")
        
#         warehouse_loc = WAREHOUSES[w_id]['loc']
#         routes, cost = solve_vrp_for_warehouse(w_id, warehouse_loc, customers)
        
#         print(f"仓库 {w_id} 的最终路径: {routes}")
#         print(f"仓库 {w_id} 的最小成本: {cost:.2f}")
        
#         all_final_routes.append({'warehouse': w_id, 'routes': routes})
#         total_min_cost += cost if cost is not None else 0

#     print(f"\n========================================")
#     print(f"全局最小总成本: {total_min_cost:.2f}")
#     print(f"========================================")

#     # 检查是否所有客户都被访问
#     all_visited_customers = []
#     for route_info in all_final_routes:
#         for route in route_info['routes']:
#             all_visited_customers.extend(route)
    
#     all_customer_ids = [c['id'] for c in CUSTOMERS]
#     unvisited_customers = [cid for cid in all_customer_ids if cid not in all_visited_customers]
    
#     if unvisited_customers:
#         print(f"警告: 以下客户未被访问: {unvisited_customers}")
#         print(f"被访问的客户: {sorted(all_visited_customers)}")
#     else:
#         print("所有客户都被成功访问!")

#     # 步骤3: 可视化结果
#     visualize_solution(WAREHOUSES, CUSTOMERS, all_final_routes)

# def visualize_solution(warehouses, customers, all_routes):
#     """可视化最终的配送方案"""
#     plt.figure(figsize=(12, 10))
#     colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
#     # 绘制仓库
#     for i, (w_id, w_data) in enumerate(warehouses.items()):
#         plt.scatter(w_data['loc'][0], w_data['loc'][1], c='black', marker='s', s=200, label=f'Warehouse {w_id}')
#         plt.text(w_data['loc'][0], w_data['loc'][1] + 2, w_id, ha='center', fontsize=12, fontweight='bold')

#     # 绘制顾客
#     for customer in customers:
#         plt.scatter(customer['loc'][0], customer['loc'][1], c='blue', marker='o')
#         plt.text(customer['loc'][0], customer['loc'][1] + 1, f"{customer['id']}({customer['demand']})", ha='center', fontsize=9)

#     # 绘制路径
#     route_idx = 0
#     for w_routes in all_routes:
#         w_id = w_routes['warehouse']
#         w_loc = warehouses[w_id]['loc']
#         for route in w_routes['routes']:
#             if not route: continue
            
#             color = colors[route_idx % len(colors)]
            
#             # 构建完整路径点
#             full_path_locs = [w_loc]
#             for c_id in route:
#                 full_path_locs.append(next(c['loc'] for c in customers if c['id'] == c_id))
#             full_path_locs.append(w_loc)
            
#             # 绘制路径线
#             for i in range(len(full_path_locs) - 1):
#                 plt.plot([full_path_locs[i][0], full_path_locs[i+1][0]], 
#                          [full_path_locs[i][1], full_path_locs[i+1][1]], 
#                          color=color, linestyle='-', alpha=0.8, linewidth=2)
            
#             route_idx += 1

#     plt.title('Optimized Delivery Routes (VRP Solver Solution)')
#     plt.xlabel('X Coordinate')
#     plt.ylabel('Y Coordinate')
#     plt.grid(True, alpha=0.3)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

# if __name__ == '__main__':
#     main()


import gurobipy as gp
from gurobipy import GRB

# 创建一个简单的模型
model = gp.Model("test")

# 添加一个变量
x = model.addVar(name="x")

# 设置目标函数
model.setObjective(x, GRB.MAXIMIZE)

# 添加一个约束
model.addConstr(x <= 1)

# 优化模型
model.optimize()

# 打印结果
if model.status == GRB.OPTIMAL:
    print(f"Optimal value: {model.objVal}")
    print(f"Optimal solution for x: {x.X}")
else:
    print("No solution found.")

# 输出版本信息，可以确认库和求解器版本
print(f"Gurobi library version: {gp.gurobi.version()}")



