import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    dataset = pd.read_csv('./data/felicidad.csv')
    print(dataset.describe())

    X = dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
    y = dataset[['score']]

    print(X.shape)
    print(y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

    modelLinear = LinearRegression().fit(X_train,y_train)
    y_predict_linear = modelLinear.predict(X_test)

    modelLasso = Lasso(alpha=0.02).fit(X_train, y_train)
    y_predict_lasso = modelLasso.predict(X_test)

    modelRidge = Ridge(alpha=1).fit(X_train, y_train)
    y_predict_ridge = modelRidge.predict(X_test)

    linear_loss = mean_squared_error(y_test, y_predict_linear)

    lasso_loss = mean_squared_error(y_test, y_predict_lasso)

    ridge_loss = mean_squared_error(y_test, y_predict_ridge)

    print(f'PERDIDA LINEAR= {linear_loss}\nPERDIDA LASSO= {lasso_loss}\nPERDIDA RIDGE= {ridge_loss}')

    print('-'*80)
    print('Coef Lasso')
    print(modelLasso.coef_)
    
    print('-'*80)
    print('Coef Ridge')
    print(modelRidge.coef_)  
