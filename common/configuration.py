import json
from common.settings import CONFIG_DEPLOY


class DeployConfig:

    def __init__(self):
        self.conf = self._read_config_file()
        self.base_url = ConfigItem(self.conf["base_url"]["value"])

    @staticmethod
    def _read_config_file():
        """
        Prepare config.json file for deploy.
        :return: None.
        """
        with open(CONFIG_DEPLOY, encoding="utf-8") as config_file:
            config = json.loads(config_file.read())
        return config


class ConfigItem:
    """
    Create object for work with dict.
    """

    def __init__(self, config_dict):
        for key, value in config_dict.items():
            self.__dict__[key] = value['value']