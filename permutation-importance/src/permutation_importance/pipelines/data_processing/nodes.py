import pandas as pd

def preprocess_new_york_taxi_fare_preditions(taxi_fare_preditions: pd.DataFrame) -> pd.DataFrame:
    # remove data with extreme outlier coodinates or negative fares
    taxi_fare_preditions = taxi_fare_preditions.query('pickup_latitude > 40.7 and pickup_latitude < 40.8 and ' +
                  'dropoff_latitude > 40.7 and dropoff_latitude < 40.8 and ' +
                  'pickup_longitude > -74 and pickup_longitude < -73.9 and ' +
                  'dropoff_longitude > -74 and dropoff_longitude < -73.9 and ' +
                  'fare_amount > 0'
                  )
    return taxi_fare_preditions

def enrich_features(data: pd.DataFrame) -> pd.DataFrame:
    data['abs_lon_change'] = abs(data.dropoff_longitude - data.pickup_longitude)
    data['abs_lat_change'] = abs(data.dropoff_latitude - data.pickup_latitude)
    return data