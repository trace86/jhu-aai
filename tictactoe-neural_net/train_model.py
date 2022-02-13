from functions import *
from matplotlib import pyplot as plt

games = [simulateGame() for _ in range(10000)]

print(gameStats(games))

model = getModel()
print(model.summary())

# Split out train and validation data
X_train, X_test, y_train, y_test = gamesToWinLossData(games)

nEpochs = 5000
batchSize = 100
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=nEpochs, batch_size=batchSize)

model_name = "model_epochs={0}_batch={1}".format(nEpochs, batchSize)
model.save(model_name)

simulate_games = [simulateGame(p1=model, p2=model, rnd=0.6) for _ in range(1000)]
gameStats(simulate_games, player=1, save=True, filename="{0}.results".format(model_name))

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()
