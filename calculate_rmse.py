def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    return (tar-pred).sum()