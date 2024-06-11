import keras

early_stopping_callback = keras.callbacks.EarlyStopping(
    monitor='val_accuracy',
    patience=5,
    mode="max",
    verbose=1
)

history = model.fit(
    train_dataset, 
    epochs=30, 
    validation_data=valid_dataset, 
    callbacks=[early_stopping_callback]
)
