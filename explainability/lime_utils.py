import lime
import lime.lime_tabular
import pandas as pd

def explain_with_lime(model, scaler, X, row_index, num_features=10):
    """
    Generates a LIME explanation for a row from a dataset.
    """
    X_scaled = scaler.transform(X)

    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=X_scaled,
        feature_names=X.columns.tolist(),
        class_names=["Legitimate", "Fraud"],
        mode="classification",
        discretize_continuous=True
    )

    explanation = explainer.explain_instance(
        data_row=X_scaled[row_index],
        predict_fn=model.predict_proba,
        num_features=num_features
    )

    return explanation


def explain_input_with_lime(model, scaler, X_train, input_df, num_features=10):
    """
    Generates a LIME explanation for a new user/input transaction.
    X_train is the training feature set used to fit the explainer.
    input_df is a single-row DataFrame with the same feature columns.
    """
    X_train_scaled = scaler.transform(X_train)
    input_scaled = scaler.transform(input_df)

    explainer = lime.lime_tabular.LimeTabularExplainer(
        training_data=X_train_scaled,
        feature_names=X_train.columns.tolist(),
        class_names=["Legitimate", "Fraud"],
        mode="classification",
        discretize_continuous=True
    )

    explanation = explainer.explain_instance(
        data_row=input_scaled[0],
        predict_fn=model.predict_proba,
        num_features=num_features
    )

    return explanation