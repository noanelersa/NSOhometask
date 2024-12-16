class DataTransformer:
    def __init__(self, field_mappings=None):
        """
        Initialize the transformer with field mappings.
        :param field_mappings: A dictionary defining how to map input keys to output keys.
        """
        self.field_mappings = field_mappings or {
            'name': 'name',
            'diameter': 'estimated_diameter.meters.estimated_diameter_max',
            'approachDate': 'close_approach_data.0.close_approach_date',
            'velocity': 'close_approach_data.0.relative_velocity.kilometers_per_second',
        }

    def _get_nested_value(self, obj, path, default=None):
        """
        Safely fetch a value from a nested dictionary using dot notation.
        :param obj: The dictionary to fetch the value from.
        :param path: Dot-separated key path (e.g., 'a.b.c').
        :param default: Default value if the key path does not exist.
        """
        keys = path.split('.')
        for key in keys:
            if isinstance(obj, list) and key.isdigit():
                key = int(key)  # Convert list indices to integers
            try:
                obj = obj[key]
            except (KeyError, IndexError, TypeError):
                return default
        return obj

    def transform(self, data) -> list:
        """
        Transform the input data based on the field mappings.
        :param data: The raw input data (e.g., API response).
        :return: A list of transformed dictionaries.
        """
        transformed = []
        for date in data.get('near_earth_objects', {}):
            for asteroid in data['near_earth_objects'][date]:
                transformed_asteroid = {}
                for output_key, input_path in self.field_mappings.items():
                    value = self._get_nested_value(asteroid, input_path)
                    if output_key == 'velocity':  # Ensure type conversion for velocity
                        value = float(value) if value is not None else 0.0
                    transformed_asteroid[output_key] = value
                transformed.append(transformed_asteroid)
        return transformed
