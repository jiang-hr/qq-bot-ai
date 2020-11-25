from pydantic import BaseSetting


class Config(BaseSetting):

    # plugin custom config
    plugin_setting: str = "default"

    class Config:
        extra = "ignore"
