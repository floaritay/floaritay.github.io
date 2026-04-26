import numpy as np
import random
import matplotlib.pyplot as plt
import math

# --- 1. 参数设置 (提取图片) ---
# 仓库参数
WAREHOUSES = {
    'W1': {'loc': (45, 25), 'stock': 100},
    'W2': {'loc': (20, 75), 'stock': 100},
    'W3': {'loc': (70, 75), 'stock': 100}
}

# 顾客参数 
CUSTOMERS = [
    {'id': 1, 'loc': (35, 35), 'demand': 1}, {'id': 2, 'loc': (15, 50), 'demand': 4}, {'id': 3, 'loc': (10, 70), 'demand': 22},
    {'id': 4, 'loc': (15, 85), 'demand': 8}, {'id': 5, 'loc': (25, 55), 'demand': 6}, {'id': 6, 'loc': (30, 45), 'demand': 10},
    {'id': 7, 'loc': (25, 90), 'demand': 7}, {'id': 8, 'loc': (20, 95), 'demand': 24}, {'id': 9, 'loc': (35, 65), 'demand': 24},
    {'id': 10, 'loc': (45, 95), 'demand': 8}, {'id': 11, 'loc': (40, 70), 'demand': 3}, {'id': 12, 'loc': (55, 80), 'demand': 18},
    {'id': 13, 'loc': (60, 70), 'demand': 8}, {'id': 14, 'loc': (65, 85), 'demand': 19}, {'id': 15, 'loc': (75, 95), 'demand': 12},
    {'id': 16, 'loc': (85, 65), 'demand': 14}, {'id': 17, 'loc': (95, 90), 'demand': 9}, {'id': 18, 'loc': (85, 75), 'demand': 2},
    {'id': 19, 'loc': (90, 40), 'demand': 16}, {'id': 20, 'loc': (95, 55), 'demand': 7}, {'id': 21, 'loc': (55, 15), 'demand': 6},
    {'id': 22, 'loc': (45, 10), 'demand': 11}, {'id': 23, 'loc': (65, 10), 'demand': 14}, {'id': 24, 'loc': (25, 15), 'demand': 15},
    {'id': 25, 'loc': (10, 25), 'demand': 16}, {'id': 26, 'loc': (85, 45), 'demand': 16}, {'id': 27, 'loc': (85, 30), 'demand': 16},
    {'id': 28, 'loc': (95, 25), 'demand': 16}, {'id': 29, 'loc': (75, 20), 'demand': 14}, {'id': 30, 'loc': (20, 80), 'demand': 2},
    {'id': 31, 'loc': (15, 10), 'demand': 10}
]

# 车辆参数 
VEHICLE_CAPACITY = 50      # 最大载重
MAX_DISTANCE = 200         # 最大行驶距离 (适当放宽以确保路径可行)
COST_PER_KM = 1.0          # 单位距离成本

# PSO 参数
POP_SIZE = 50              # 粒子群大小
MAX_ITER = 200             # 最大迭代次数
W = 0.7                    # 惯性权重
C1 = 1.5                   # 个体学习因子
C2 = 1.5                   # 社会学习因子

# --- 2. 辅助函数 ---
def calculate_distance(p1, p2):
    """计算两点之间的欧几里得距离"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def assign_customers_to_warehouses(customers, warehouses):
    """将顾客分配给最近的仓库"""
    assigned = {w_id: [] for w_id in warehouses}
    for customer in customers:
        min_dist = float('inf')
        closest_warehouse = None
        for w_id, w_data in warehouses.items():
            dist = calculate_distance(customer['loc'], w_data['loc'])
            if dist < min_dist:
                min_dist = dist
                closest_warehouse = w_id
        assigned[closest_warehouse].append(customer)
    return assigned

# --- 3. PSO 核心算法 ---
class PSO:
    def __init__(self, customers, warehouse_loc):
        self.customers = customers
        self.warehouse_loc = warehouse_loc
        self.num_customers = len(customers)
        self.customer_ids = [c['id'] for c in customers]
        self.customer_map = {c['id']: c for c in customers}
        
        # 初始化粒子群
        self.particles = []
        self.velocities = []
        self.pbest_positions = []
        self.pbest_scores = []
        
        for _ in range(POP_SIZE):
            # 粒子位置是顾客ID的一个随机排列
            position = random.sample(self.customer_ids, self.num_customers)
            self.particles.append(position)
            self.pbest_positions.append(position[:])
            
            # 速度是交换序列
            velocity = []
            self.velocities.append(velocity)
            
            # 计算初始适应度
            score = self.calculate_fitness(position)
            self.pbest_scores.append(score)

        # 初始化全局最优
        min_idx = np.argmin(self.pbest_scores)
        self.gbest_position = self.pbest_positions[min_idx][:]
        self.gbest_score = self.pbest_scores[min_idx]

    def calculate_fitness(self, position):
        """计算适应度（总成本）"""
        routes = self.decode_position_to_routes(position)
        total_cost = 0
        for route in routes:
            if not route: continue
            # 路径: 仓库 -> 客户1 -> ... -> 客户n -> 仓库
            full_path = [self.warehouse_loc] + [self.customer_map[c_id]['loc'] for c_id in route] + [self.warehouse_loc]
            route_distance = sum(calculate_distance(full_path[i], full_path[i+1]) for i in range(len(full_path)-1))
            total_cost += route_distance * COST_PER_KM
        return total_cost

    def decode_position_to_routes(self, position):
        """将粒子位置（顾客序列）解码为满足约束的车辆路径"""
        routes = []
        current_route = []
        current_load = 0
        current_distance = 0
        last_loc = self.warehouse_loc

        for customer_id in position:
            customer = self.customer_map[customer_id]
            customer_loc = customer['loc']
            demand = customer['demand']
            
            # 计算如果加入此客户，距离和载重是否超限
            dist_to_customer = calculate_distance(last_loc, customer_loc)
            dist_back_to_warehouse = calculate_distance(customer_loc, self.warehouse_loc)
            
            potential_load = current_load + demand
            potential_distance = current_distance + dist_to_customer + dist_back_to_warehouse

            if potential_load <= VEHICLE_CAPACITY and potential_distance <= MAX_DISTANCE:
                # 可以加入当前路径
                current_route.append(customer_id)
                current_load = potential_load
                current_distance += dist_to_customer
                last_loc = customer_loc
            else:
                # 无法加入，当前路径结束，开始新路径
                if current_route:
                    routes.append(current_route)
                current_route = [customer_id]
                current_load = demand
                current_distance = calculate_distance(self.warehouse_loc, customer_loc)
                last_loc = customer_loc
        
        if current_route:
            routes.append(current_route)
            
        return routes

    def run(self):
        """运行PSO算法"""
        for _ in range(MAX_ITER):
            for i in range(POP_SIZE):
                # 更新速度 (基于交换序列)
                r1, r2 = random.random(), random.random()
                
                # pbest部分的速度
                pbest_vel = self.get_swap_sequence(self.particles[i], self.pbest_positions[i])
                # gbest部分的速度
                gbest_vel = self.get_swap_sequence(self.particles[i], self.gbest_position)
                
                # 合并速度 (简化处理：按概率选择执行)
                new_velocity = []
                if random.random() < C1 * r1:
                    new_velocity.extend(pbest_vel)
                if random.random() < C2 * r2:
                    new_velocity.extend(gbest_vel)
                if random.random() < W and self.velocities[i]:
                    new_velocity.extend(self.velocities[i])

                self.velocities[i] = new_velocity

                # 更新位置
                new_position = self.apply_swap_sequence(self.particles[i], new_velocity)
                self.particles[i] = new_position

                # 评估新位置
                current_score = self.calculate_fitness(new_position)
                
                # 更新个体最优
                if current_score < self.pbest_scores[i]:
                    self.pbest_scores[i] = current_score
                    self.pbest_positions[i] = new_position[:]
                    
                    # 更新全局最优
                    if current_score < self.gbest_score:
                        self.gbest_score = current_score
                        self.gbest_position = new_position[:]
        
        return self.gbest_position, self.gbest_score

    def get_swap_sequence(self, pos1, pos2):
        """计算从pos1变换到pos2所需的交换序列"""
        seq = []
        temp_pos = pos1[:]
        for i in range(len(pos1)):
            if temp_pos[i] != pos2[i]:
                # 找到pos2[i]在temp_pos中的位置
                j = temp_pos.index(pos2[i])
                # 交换
                temp_pos[i], temp_pos[j] = temp_pos[j], temp_pos[i]
                seq.append((i, j))
        return seq

    def apply_swap_sequence(self, position, swap_sequence):
        """将交换序列应用到位置上"""
        new_position = position[:]
        for swap in swap_sequence:
            i, j = swap
            new_position[i], new_position[j] = new_position[j], new_position[i]
        return new_position

# --- 4. 主程序与可视化 ---
def main():
    # 步骤1: 分配顾客
    assigned_customers = assign_customers_to_warehouses(CUSTOMERS, WAREHOUSES)
    
    all_final_routes = []
    total_min_cost = 0

    # 步骤2: 对每个仓库的子问题进行优化
    for w_id, customers in assigned_customers.items():
        if not customers:
            continue
            
        print(f"\n--- 正在为仓库 {w_id} 优化路径 ---")
        print(f"分配的顾客: {[c['id'] for c in customers]}")
        
        warehouse_loc = WAREHOUSES[w_id]['loc']
        pso_solver = PSO(customers, warehouse_loc)
        
        best_position, best_score = pso_solver.run()
        
        print(f"仓库 {w_id} 的最优序列: {best_position}")
        print(f"仓库 {w_id} 的最小成本: {best_score:.2f}")
        
        # 解码最终路径
        final_routes = pso_solver.decode_position_to_routes(best_position)
        print(f"仓库 {w_id} 的最终路径: {final_routes}")
        
        all_final_routes.append({'warehouse': w_id, 'routes': final_routes})
        total_min_cost += best_score

    print(f"\n========================================")
    print(f"全局最小总成本: {total_min_cost:.2f}")
    print(f"========================================")

    # 步骤3: 可视化结果
    visualize_solution(WAREHOUSES, CUSTOMERS, all_final_routes)

def visualize_solution(warehouses, customers, all_routes):
    """可视化最终的配送方案"""
    plt.figure(figsize=(12, 10))
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
    # 绘制仓库
    for i, (w_id, w_data) in enumerate(warehouses.items()):
        plt.scatter(w_data['loc'][0], w_data['loc'][1], c='black', marker='s', s=200, label=f'Warehouse {w_id}')
        plt.text(w_data['loc'][0], w_data['loc'][1] + 2, w_id, ha='center', fontsize=12, fontweight='bold')

    # 绘制顾客
    for customer in customers:
        plt.scatter(customer['loc'][0], customer['loc'][1], c='blue', marker='o')
        plt.text(customer['loc'][0], customer['loc'][1] + 1, f"{customer['id']}({customer['demand']})", ha='center', fontsize=9)

    # 绘制路径
    route_idx = 0
    for w_routes in all_routes:
        w_id = w_routes['warehouse']
        w_loc = warehouses[w_id]['loc']
        for route in w_routes['routes']:
            if not route: continue
            
            color = colors[route_idx % len(colors)]
            
            # 构建完整路径点
            full_path_locs = [w_loc]
            for c_id in route:
                full_path_locs.append(next(c['loc'] for c in customers if c['id'] == c_id))
            full_path_locs.append(w_loc)
            
            # 绘制路径线
            for i in range(len(full_path_locs) - 1):
                plt.plot([full_path_locs[i][0], full_path_locs[i+1][0]], 
                         [full_path_locs[i][1], full_path_locs[i+1][1]], 
                         color=color, linestyle='--', alpha=0.7)
            
            route_idx += 1

    plt.title('Optimized Delivery Routes')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
