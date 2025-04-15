#高斯批量提交的任务是否正常结束
import os

def check_gaussian_log(directory):
    normal_termination_files = []
    abnormal_termination_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()
                    last_lines = lines[-10:]  # 取最后10行
                    for line in last_lines:
                        if "Normal termination of Gaussian" in line:
                            normal_termination_files.append(file)
                            break
                    else:  # 如果没有找到"Normal termination of Gaussian"，则认为是非正常结束
                        abnormal_termination_files.append(file)
    return normal_termination_files, abnormal_termination_files

# 使用方法：将下面的路径替换为你要检查的目录
normal_files, abnormal_files = check_gaussian_log("\ligand")
print("正常结束的文件：", normal_files)
print("非正常结束的文件：", abnormal_files)
