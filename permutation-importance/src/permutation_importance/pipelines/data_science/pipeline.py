"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import evaluate_features, split_data, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=split_data,
                inputs=["model_input_table", "params:model_options"],
                outputs=["train_X", "test_X", "train_y", "test_y"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["train_X", "train_y"],
                outputs="regressor",
                name="train_model_node",
            ),
            node(
                func=evaluate_features,
                inputs=['regressor', 'test_X', 'test_y'],
                outputs='permutation_importance',
                name="evaluate_features_node",
            ),
    ])
