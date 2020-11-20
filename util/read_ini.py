#code=utf-8
import configparser, os, sys
base_path = os.getcwd()
sys.path.append(base_path)


class ReadIni:
    def __init__(self):
        self.data = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        config_path = os.path.join(base_path, "config", "LocalElement.ini")
        cf.read(config_path)
        return cf

    def get_value(self, options, key):
        print('-->', key)
        return self.data.get(options, key)

    def set_value(self, options, key, t):
        value = self.get_value(options, key).format(t)
        self.data.set(options, key, value)
        config_path = os.path.join(base_path, "config", "LocalElement.ini")
        self.data.write(open(config_path, "w"))

    def replace_value(self, options, key, old, new="{}"):
        value = self.get_value(options, key).replace(old, new)
        self.data.set(options, key, value)
        config_path = os.path.join(base_path, "config", "LocalElement.ini")
        self.data.write(open(config_path, "w"))


read_ini = ReadIni()

if __name__ == "__main__":
    read_ini = ReadIni()
    data = read_ini.replace_value('shoppingcart', "remove_button", "铂金钻石戒指")
    g = read_ini.get_value('shoppingcart', "remove_button")
    print(g)