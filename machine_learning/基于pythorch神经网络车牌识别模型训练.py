import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pathlib
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
gpus = tf.config.list_physical_devices("GPU")
if gpus:
    tf.config.experimental.set_memory_growth(gpus[0], True)  # 设置GPU显存用量按需使用
    tf.config.set_visible_devices([gpus[0]],"GPU")
np.random.seed(1)
tf.random.set_seed(1)
#2.导入数据
import os
import pathlib
# 设置数据目录
data_dir = pathlib.Path(r"...")
# 列出部分文件
file_list = os.listdir(data_dir)[:20]  # 列出前20个文件
print("部分文件列表：", file_list)
# 获取图片路径并计算图像总数
pictures_paths = list(data_dir.glob('*'))
pictures_paths = [str(path) for path in pictures_paths]
image_count = len(pictures_paths)
print("图片总数为：", image_count)
# 获取数据标签
all_label_names = [path.split("\\")[-1].split("_")[1].split(".")[0] for path in pictures_paths]
all_label_names[:3]
#3.数据可视化
plt.figure(figsize=(10, 5))
plt.suptitle("数据示例", fontsize=15)
for i in range(20):
    plt.subplot(5, 4, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    # 显示图片
    images = plt.imread(pictures_paths[i])
    plt.imshow(images)
    # 显示标签
    plt.xlabel(all_label_names[i], fontsize=13)
plt.show()
#4.标签数字化
char_enum = ["京","沪","津","渝","冀","晋","蒙","辽","吉","黑","苏","浙","皖","闽","赣","鲁",\
              "豫","鄂","湘","粤","桂","琼","川","贵","云","藏","陕","甘","青","宁","新","军","使"]
number   = [str(i) for i in range(0, 10)]    # 0 到 9 的数字
alphabet_upper = [chr(i) for i in range(65, 91)]   # A 到 Z 的大写字母
alphabet_lower = [chr(i) for i in range(97, 123)]  # a 到 z 的小写字母
char_set       = char_enum + number + alphabet_upper + alphabet_lower
char_set_len   = len(char_set)
label_name_len = len(all_label_names[0])
# 将字符串数字化
def text2vec(text):
    vector = np.zeros([label_name_len, char_set_len])
    for i, c in enumerate(text):
        idx = char_set.index(c)
        vector[i][idx] = 1.0
    return vector

all_labels = [text2vec(i) for i in all_label_names]

# 构建数据集
AUTOTUNE = tf.data.experimental.AUTOTUNE

def preprocess_image(image):
    image = tf.image.decode_jpeg(image, channels=1)
    image = tf.image.resize(image, [50, 200])
    return image / 255.0

def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    return preprocess_image(image)

path_ds = tf.data.Dataset.from_tensor_slices(pictures_paths)
image_ds = path_ds.map(load_and_preprocess_image, num_parallel_calls=AUTOTUNE)
label_ds = tf.data.Dataset.from_tensor_slices(all_labels)
image_label_ds = tf.data.Dataset.zip((image_ds, label_ds))

train_ds = image_label_ds.take(5000).shuffle(5000).batch(16).prefetch(buffer_size=AUTOTUNE)
val_ds = image_label_ds.skip(5000).shuffle(1000).batch(16).prefetch(buffer_size=AUTOTUNE)
# 构建模型
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(50, 200, 1)),  # 使用 Input(shape) 对象指定输入形状
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(label_name_len * char_set_len),
    tf.keras.layers.Reshape([label_name_len, char_set_len]),
    tf.keras.layers.Softmax()
])
# 设置学习率调度和优化器
initial_learning_rate = 1e-3
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=50,
        decay_rate=0.96,
        staircase=True)
optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

# 编译模型
model.compile(optimizer=optimizer,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# 训练模型
epochs = 5
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)
# 可视化训练过程
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs_range = range(epochs)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# 保存和加载模型
model.save('model/15_model.h5')
new_model = tf.keras.models.load_model('model/15_model.h5')

# 预测
def vec2text(vec):
    text = []
    for i, c in enumerate(vec):
        text.append(char_set[c])
    return "".join(text)

plt.figure(figsize=(10, 8))
for images, labels in val_ds.take(1):
    for i in range(6):
        ax = plt.subplot(5, 2, i + 1)
        plt.imshow(images[i])
        img_array = tf.expand_dims(images[i], 0)
        predictions = model.predict(img_array)
        plt.title(vec2text(np.argmax(predictions, axis=2)[0]), fontsize=15)
        plt.axis("off")
plt.show()