贪吃蛇


```python
import tkinter as tk
import random

# 创建主窗口
app = tk.Tk()
app.title("Snake Game")

# 创建Canvas控件用于绘制游戏界面
canvas = tk.Canvas(app, width=800, height=800, borderwidth=0, highlightthickness=0)
canvas.pack()

# 初始化游戏参数
snake_x = 10
snake_y = 10
snake = [(snake_x, snake_y), (snake_x - 1, snake_y), (snake_x - 2, snake_y)]
food = (15, 15)
direction = "Right"


# 创建食物
def create_food():
    # 这里是在随机网格(40*40)位置，但是这个位置不能是蛇所在位置
    while True:
        x = random.randint(0, 39)
        y = random.randint(0, 39)
        if (x, y) not in snake:
            return x, y


food = create_food()


# 画出食物
def draw_food():
    x, y = food
    canvas.create_oval(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="red", outline="red")


# 画出蛇
def draw_snake():
    for x, y in snake:
        canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")


# 移动蛇
def move_snake():
    global direction, food

    # 每次步进一个网格
    head = snake[0]
    if direction == "Right":
        new_head = (head[0] + 1, head[1])
    elif direction == "Left":
        new_head = (head[0] - 1, head[1])
    elif direction == "Up":
        new_head = (head[0], head[1] - 1)
    elif direction == "Down":
        new_head = (head[0], head[1] + 1)

    snake.insert(0, new_head)
    
    # 如果你吃到食物了，则新头不需要删掉
    if snake[0] == food:
        food = create_food()
    else:
        snake.pop()

    canvas.delete("all")
    draw_snake()
    draw_food()

    app.after(100, move_snake)


# 设置方向
def set_direction(new_direction):
    global direction
    if (new_direction == "Up" and direction != "Down") or \
       (new_direction == "Down" and direction != "Up") or \
       (new_direction == "Left" and direction != "Right") or \
       (new_direction == "Right" and direction != "Left"):
        direction = new_direction


# 设置键盘控制
app.bind("<Up>", lambda event: set_direction("Up"))
app.bind("<Down>", lambda event: set_direction("Down"))
app.bind("<Left>", lambda event: set_direction("Left"))
app.bind("<Right>", lambda event: set_direction("Right"))

draw_snake()
draw_food()
move_snake()

app.mainloop()


```

小钢琴


```python
import tkinter as tk
import winsound

# 音符映射，用于将键盘键映射到音符频率
note_mapping = {
    "a": 261.63,  # C4
    "w": 277.18,  # C#4
    "s": 293.66,  # D4
    "e": 311.13,  # D#4
    "d": 329.63,  # E4
    "f": 349.23,  # F4
    "t": 369.99,  # F#4
    "g": 392.00,  # G4
    "y": 415.30,  # G#4
    "h": 440.00,  # A4
    "u": 466.16,  # A#4
    "j": 493.88,  # B4
}

# 创建主窗口
root = tk.Tk()
root.title("Virtual Piano")
root.geometry("400x300")

# 创建Canvas来显示琴键
canvas = tk.Canvas(root, width=400, height=150)
canvas.pack()

# 创建标签以显示按下的琴键
pressed_key_label = tk.Label(root, text="")
pressed_key_label.pack()

# 创建钢琴键的坐标和颜色
keys = [
    {
        "note": "C4",
        "x": 0,
        "color": "white"
    },
    {
        "note": "C#4",
        "x": 40,
        "color": "black"
    },
    {
        "note": "D4",
        "x": 60,
        "color": "white"
    },
    {
        "note": "D#4",
        "x": 100,
        "color": "black"
    },
    {
        "note": "E4",
        "x": 120,
        "color": "white"
    },
    {
        "note": "F4",
        "x": 160,
        "color": "white"
    },
    {
        "note": "F#4",
        "x": 200,
        "color": "black"
    },
    {
        "note": "G4",
        "x": 220,
        "color": "white"
    },
    {
        "note": "G#4",
        "x": 260,
        "color": "black"
    },
    {
        "note": "A4",
        "x": 280,
        "color": "white"
    },
    {
        "note": "A#4",
        "x": 320,
        "color": "black"
    },
    {
        "note": "B4",
        "x": 340,
        "color": "white"
    },
]

# 绘制钢琴键
for key in keys:
    key_x = key["x"]
    key_color = key["color"]
    key_height = 100
    canvas.create_rectangle(key_x, 0, key_x + 40, key_height, fill=key_color, outline="black")


# 按键按下事件处理函数
def play_note(event):
    key = event.keysym.lower()
    if key in note_mapping:
        frequency = note_mapping[key]
        winsound.Beep(int(frequency), 300)  # 播放音调
        pressed_key_label.config(text=f"Pressed Key: {key}")


# 将按键按下事件与处理函数绑定
root.bind("<KeyPress>", play_note)

# 运行主循环
root.mainloop()

```
