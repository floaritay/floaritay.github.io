# 目录


---
## 快捷键
### **一、代码编辑与格式化**
1. **注释与取消注释**  
   - `Ctrl + R`：注释当前行或选中的代码块。  
   - `Ctrl + T`：取消注释当前行或选中的代码块。  

2. **代码缩进**  
   - `Tab`：增加缩进（光标在行首或选中多行时生效）。  
   - `Shift + Tab`：减少缩进（光标在行首或选中多行时生效）。  
   - `Ctrl + I`：自动调整选中代码的缩进格式。  

3. **复制与移动代码**  
   - `Ctrl + C`：复制选中代码。  
   - `Ctrl + X`：剪切选中代码。  
   - `Ctrl + V`：粘贴代码。  
   - `Ctrl + Shift + C`：复制当前行到下一行（无需选中）。  

4. **代码折叠与展开**  
   - `Ctrl + Shift + [`：折叠当前代码块。  
   - `Ctrl + Shift + ]`：展开当前代码块。  

---

### **二、代码运行与调试**
1. **运行代码**  
   - `F5`：保存并运行当前脚本或函数。  
   - `Ctrl + Enter`：运行选中的代码块（调试时非常有用）。  
   - `F9`：在选中的代码行设置或取消断点。  

2. **调试控制**  
   - `F10`：单步执行（不进入函数内部）。  
   - `F11`：单步执行（进入函数内部）。  
   - `Shift + F5`：退出调试模式。  
   - `Ctrl + C`：中断正在运行的程序（需在命令窗口激活）。  

---

### **三、窗口与文件管理**
1. **窗口切换**  
   - `Ctrl + Tab`：在编辑器、命令窗口、工作区等窗口间切换。  
   - `Ctrl + Shift + Tab`：反向切换窗口。  

2. **文件操作**  
   - `Ctrl + N`：新建脚本或函数文件。  
   - `Ctrl + O`：打开现有文件。  
   - `Ctrl + S`：保存当前文件。  
   - `Ctrl + Shift + S`：另存为文件。  
   - `Ctrl + W`：关闭当前文件。  

---

### **四、命令窗口操作**
1. **命令历史**  
   - `↑` / `↓`：在命令历史中上下翻页。  
   - `Page Up` / `Page Down`：快速翻页。  

2. **命令补全与执行**  
   - `Tab`：自动补全命令、变量名或函数名。  
   - `Enter`：执行当前命令。  
   - `Shift + Enter`：在命令窗口中换行（不执行）。  
   - `Esc`：清除当前输入的命令（未执行时）。  

3. **常用命令**  
   - `clc`：清空命令窗口。  
   - `clear`：清除工作区变量。  
   - `close all`：关闭所有图形窗口。  
   - `who` / `whos`：列出工作区变量。  

---

### **五、搜索与替换**
1. **查找**  
   - `Ctrl + F`：在文件中查找字符串。  
   - `F3`：查找下一个匹配项。  
   - `Shift + F3`：查找上一个匹配项。  

2. **替换**  
   - `Ctrl + H`：替换文件中的字符串。  

---

### **六、其他实用快捷键**
1. **撤销与重做**  
   - `Ctrl + Z`：撤销上一步操作。  
   - `Ctrl + Y`：重做上一步操作。  

2. **行号跳转**  
   - `Ctrl + G`：输入行号跳转到指定行。  

3. **变量编辑器**  
   - `Ctrl + Shift + I`：打开变量编辑器（查看或编辑工作区变量）。  

4. **函数浏览器**  
   - `Ctrl + Shift + F`：打开函数浏览器（查看 MATLAB 内置函数）。  

---

### **七、自定义快捷键**
- MATLAB 允许用户自定义快捷键：  
  - 进入路径：`主页` → `环境` → `键盘快捷键` → `自定义`。  
  - 例如，可以将常用功能（如保存所有文件）绑定到未使用的快捷键组合。  

---

### **注意事项**
1. **快捷键冲突**：如果某些快捷键与其他软件冲突，可以在 MATLAB 设置中修改。  
2. **版本差异**：不同版本的 MATLAB 可能存在快捷键差异，建议参考官方文档。  
3. **macOS 系统**：将 `Ctrl` 替换为 `Command`，例如 `Command + R` 用于注释。  

---

通过熟练掌握这些快捷键，可以显著提升 MATLAB 编程效率，减少鼠标操作，专注于代码逻辑。建议在日常使用中逐步熟悉并形成肌肉记忆。

## **续行符**
---

### **注意事项**
1. **空格**：`...` 后可以直接换行，无需额外空格。
2. **字符串和注释**：`...` 不能用于字符串或注释的换行。例如：
>   ```matlab
>   % 错误示例：续行符不能用于注释
>   str = 'This is a long string... 
>          that spans multiple lines'; % 会报错
>   ```
3. **矩阵或单元格数组**：续行符可直接用于矩阵或单元格数组的定义：
>   ```matlab
>   A = [1, 2, 3; ...
>        4, 5, 6];
>   ```


function [x,fval] = simulated_annealing(fun,x0,options)
% fun: 目标函数句柄
% x0: 初始解
% options: 选项结构体，包括以下字段：
%   T0: 初始温度
%   alpha: 降温速率
%   T_min: 终止温度
%   max_iter: 最大迭代次数
%   verbose: 是否打印输出
% 返回值：
%   x: 最优解
%   fval: 目标函数在最优解处的取值

% 设置默认选项
default_options = struct('T0',100,'alpha',0.95,'T_min',1e-8,...
                         'max_iter',1000,'verbose',false);
if nargin < 3
    options = default_options;
else
    options = merge_options(default_options,options);
end

% 初始化参数
T = options.T0;
x = x0(:); % 确保是列向量
fval = feval(fun,x);
iter = 0;
best_x = x;
best_fval = fval;

% 初始化绘图
if options.verbose
    figure;
    subplot(2,1,1);
    x_plot = zeros(length(x0), options.max_iter);
    fval_plot = zeros(1, options.max_iter);
    best_fval_plot = zeros(1, options.max_iter);
    
    % 初始化图形
    hold on;
    plot_handles = gobjects(1, length(x0));
    for i = 1:length(x0)
        plot_handles(i) = plot(nan, nan, 'DisplayName', sprintf('x%d', i));
    end
    legend(plot_handles, 'Location', 'best');
    title('解的变化');
    xlabel('迭代次数');
    ylabel('解的值');
    
    subplot(2,1,2);
    best_plot = plot(nan, nan, 'DisplayName', 'Best fval');
    legend(best_plot, 'Location', 'best');
    title('最优目标函数值');
    xlabel('迭代次数');
    ylabel('log(fval)');
end

% 开始迭代
while T > options.T_min && iter < options.max_iter
    % 产生新解（保持维度一致）
    new_x = x + randn(size(x)) * T; % 添加温度影响
    new_fval = feval(fun,new_x);
    delta_f = new_fval - fval;
    
    % 接受新解
    if delta_f < 0 || exp(-delta_f/T) > rand()
        x = new_x;
        fval = new_fval;
        if fval < best_fval
            best_x = x;
            best_fval = fval;
        end
    end
    
    % 降温
    T = options.alpha * T;
    
    % 打印输出和绘图
    if options.verbose
        fprintf('iter=%d, T=%g, fval=%g, best_fval=%g\n',iter,T,fval,best_fval);
        x_plot(:,iter+1) = x;
        fval_plot(iter+1) = fval;
        best_fval_plot(iter+1) = best_fval;
        
        % 更新绘图
        subplot(2,1,1);
        for i = 1:length(x0)
            plot_handles(i).XData = [plot_handles(i).XData, iter];
            plot_handles(i).YData = [plot_handles(i).YData, x_plot(i, iter+1)];
        end
        
        subplot(2,1,2);
        best_plot.XData = [best_plot.XData, iter];
        best_plot.YData = [best_plot.YData, best_fval_plot(iter+1)];
        drawnow;
    end
    
    % 更新迭代计数器
    iter = iter + 1;
end

% 返回最优解和目标函数值
x = best_x;
fval = best_fval;

% 合并选项结构体
function opt = merge_options(default_opt,opt)
if isempty(opt)
    opt = default_opt;
else
    fields = fieldnames(default_opt);
    for i = 1:length(fields)
        if ~isfield(opt,fields{i})
            opt.(fields{i}) = default_opt.(fields{i});
        end
    end
end

% fun = @(x) sum(100*(x(2:end)-x(1:end-1).^2).^2 + (1-x(1:end-1)).^2);
% x0 = [-1.2; 1];
% options = struct('T0',100,'alpha',0.95,'T_min',1e-8,'max_iter',1000,'verbose',true);
% [x, fval] = simulated_annealing(fun, x0, options);
% disp(['Best solution: ', num2str(x')]);
% disp(['Objective function value: ', num2str(fval)]);



```python

```
