"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import enrich_features, preprocess_new_york_taxi_fare_preditions


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_new_york_taxi_fare_preditions,
            inputs=["new-york-city-taxi-fare-prediction"],
            outputs="preprocessed-taxi-fare-prediction",
            name="preprocessing_new_york_taxi_fare_predictions_node"
        ),
        node(
            func=enrich_features,
            inputs=["preprocessed-taxi-fare-prediction"],
            outputs="model_input_table",
            name="enrich_feature_taxi_fare_predictions_node"
        )
    ])
