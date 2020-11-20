import os

# 项目顶层结构
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

case_dir = os.path.join(base_dir, "case")

htmlreport_dir =  os.path.join(base_dir, "outputs/report")

logs_dir = os.path.join(base_dir, "output/logs")

screenshot_dir = os.path.join(base_dir, "output/image")


if __name__ == "__main__":
    print (screen_dir)