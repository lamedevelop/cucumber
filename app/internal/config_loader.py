import os
import importlib


class ConfigLoader:

    configs_folder = 'configs'
    default_config_name = 'default'
    config_env_var_name = 'CUCUMBER_CONFIG'

    @staticmethod
    def getConfig():
        """Get application config by config environment variable value."""

        config_name = os.getenv(
            ConfigLoader.config_env_var_name,
            ConfigLoader.default_config_name
        )
        return importlib.import_module(f'{ConfigLoader.configs_folder}.{config_name}')
