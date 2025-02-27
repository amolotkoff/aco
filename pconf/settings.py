from pathlib import Path
import argparse, json, __main__

class SettingNotFoundException(Exception):
    pass

class SettingsFileNotExists(Exception):
    pass


class Pconf:
    SETTINGS_FILE_NAME : str = 'settings.json'
    settings_path : Path
    stand : str

    def __init__(self, settings_path):
        parser = argparse.ArgumentParser()
        parser.add_argument('--stand',
                            type=str,
                            default='dev',
                            help='provide dev or prod')

        settings = parser.parse_args()
        self.stand = settings.stand

        settings_path = Path(settings_path)

        if settings_path.is_file():
            settings_path = settings_path.parent

        self.settings_path = settings_path

    def get(self, setting_path : str):
        """Example of setting_path parameter: '/api/loader/load_as' """

        def get_path_as_array(_path : str) -> [str]:
            result_path : [str] = _path.split('/')
            return result_path

        def get_space(file_path: Path) -> dict:
            with open(file_path) as file:
                return json.load(file)

        def get_setting(space: dict, _path : [str]):
            subspace = space

            for subpath in _path:
                if subpath not in subspace:
                    return None
                subspace = subspace[subpath]

            return subspace

        def get_settings_from_down_to_up(current_settings_dir_path : Path, path : [str]):
            current_settings_file_path = current_settings_dir_path.joinpath(self.SETTINGS_FILE_NAME)
            highest_directory_path = Path(__main__.__file__).parent

            if current_settings_file_path.is_file():
                _space = get_space(current_settings_file_path)
                _setting = get_setting(_space, path)

                if _setting:
                    return _setting

            if (not current_settings_file_path.is_file() and
                    current_settings_dir_path == highest_directory_path):
                return None

            if current_settings_dir_path.parent.is_dir():
                return get_settings_from_down_to_up(current_settings_dir_path.parent, path)

            return None

        path : [str] = get_path_as_array(setting_path)
        path.insert(0, self.stand)

        settings = get_settings_from_down_to_up(self.settings_path, path)

        if settings is None:
            raise SettingNotFoundException(f'setting was not found:{settings}')

        return settings