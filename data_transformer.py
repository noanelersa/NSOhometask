#class DataTransformer:
def transform(self, data):
    transformed=[]
    for date in data.get('near_earth_objects', {}):
        for asteroid in data['near_earth_objects'][date]:
            transformed.append({
                'name': asteroid['name'],
                'diameter': asteroid['estimated_diameter']['meters']['estimated_diameter_max'],
                'approachDate': asteroid['close_approach_data'][0]['close_approach_date'],
                'velocity': float(asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second'])
            })
    return transformed