from pathlib import Path
import argparse, json

class SettingNotFoundException(Exception):
    pass


class SettingsFileNotExists(Exception):
    pass


def get(*path):
    def get_space(file_path : Path) -> dict:
        with open(file_path) as file:
            return json.load(file)

    def get_setting(space : dict, _path):
        subspace = space

        for subpath in _path:
            if subpath not in subspace:
                return None
            subspace = subspace[subpath]

        return subspace

    def get_setting_from_space_with_default_space(_space, _stand, _path):
        _settings = _space['settings'][_stand]
        _setting = get_setting(_settings, _path)

        if _setting is None:
            _settings = _space['settings']['default']
            _setting = get_setting(_settings, _path)

        return _setting

    parser = argparse.ArgumentParser()
    parser.add_argument('--stand',
                        type=str,
                        default='dev',
                        help='provide dev or prod')

    settings = parser.parse_args()
    setting = None
    stand = settings.stand

    inner_space = get_space(Path(__file__).parent.joinpath('settings.json'))

    outer_space_settings_path = inner_space['meta']['path']

    if Path(outer_space_settings_path).exists():
        outer_space = get_space(outer_space_settings_path)
        setting = get_setting_from_space_with_default_space(outer_space, stand, path)

    if setting is None:
        setting = get_setting_from_space_with_default_space(inner_space, stand, path)

    if setting is None:
        raise SettingNotFoundException(f'setting was not found:{setting}')

    return setting
