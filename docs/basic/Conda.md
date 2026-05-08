## Conda管理

conda --version
- 查看conda版本

conda config --show
- 查看conda的环境配置

conda update conda	
- 更新 Conda 本身

conda create --help
- 查询某个命令的帮助

## 环境管理命令

conda create -n <环境名> python=<版本>  
- 创建新环境（如 conda create -n myenv python=3.10）  

conda activate <环境名>  
- 激活环境  

conda deactivate  
- 退出当前环境  

conda env list / conda info --envs / conda info -e	 
- 查看所有已创建的环境    

conda env remove -n <环境名>  
- 删除指定环境    

conda env export > environment.yml  
- 导出当前环境配置到文件  

conda env create -f environment.yml	  
- 从配置文件创建环境  

## 包管理命令

conda install <包名>	
- 安装指定包（如 conda install pandas=2.0，指定版本）

conda install <包1> <包2>	
- 同时安装多个包

conda update <包名>	
- 更新指定包到最新兼容版本

conda remove <包名>	
- 卸载指定包

conda list	
- 查看当前环境中已安装的所有包

conda search <包名>	
- 搜索 Conda 仓库中可用的包版本

注意：conda命令的一些选项开关有两种指定方式

一种两个连接号“--”后跟选项名全程

一种是一个连接号“-”后跟简称

比如说"-n"和"--name"是等价的

但是要注意有些例外，比如说，“--version”对应的是“-V”

conda有一个缺省的名为base的环境。但是不建议把程序放在base环境中，应该创建不同的虚拟环境分别管理不同的开发项目

