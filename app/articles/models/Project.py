from app.articles.utils.MetaJSON import MetaJSONBase

class ProjectJSON(MetaJSONBase):
    def add_asset(self, asset_name, asset_data):
        if 'assets' not in self._data:
            self._data['assets'] = {}
        self._data['assets'][asset_name] = asset_data

    def get_asset(self, asset_name):
        return self._data.get('assets', {}).get(asset_name)

    def list_assets(self):
        return list(self._data.get('assets', {}).keys())

    def remove_asset(self, asset_name):
        if 'assets' in self._data and asset_name in self._data['assets']:
            del self._data['assets'][asset_name]
