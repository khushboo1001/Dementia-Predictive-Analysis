def Train(gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF):
    
    import pandas as pd
    import numpy as np
    import seaborn as sns
    oasis_long = pd.read_csv('data\\oasis_longitudinal.csv')
    oasis_long = oasis_long.drop(columns = ['Hand', 'MRI ID', 'MR Delay', 'Subject ID',
                                            'Visit'])
    
    y = oasis_long['Group'].astype('category')
    X = oasis_long.iloc[:, 1:]
    #X1 = X
    
    
    X["M/F"].fillna("M",inplace = True)
    X["Age"].fillna(method='ffill',inplace=True)
    X["EDUC"].fillna(method='ffill',inplace=True)
    X["CDR"].fillna("0",inplace = True)
    X["eTIV"].fillna(method='ffill',inplace=True)
    
    
    from sklearn.preprocessing import LabelEncoder
    le =  LabelEncoder()
    X.iloc[:, 0] = le.fit_transform(X.iloc[:, 0])
    
    #Female 0 Male 1
    
    
    from sklearn.impute import SimpleImputer
    imputer_SES = SimpleImputer(missing_values=np.nan, strategy='median')
    imputer_MMSE = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer_nWBV = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer_ASF = SimpleImputer(missing_values=np.nan, strategy='median')
    X.iloc[:, 3:4] = imputer_SES.fit_transform(X.iloc[:, 3:4])   
    X.iloc[:, 4:5] = imputer_MMSE.fit_transform(X.iloc[:, 4:5])
    X.iloc[:,7:8] = imputer_nWBV.fit_transform(X.iloc[:, 7:8])
    X.iloc[:,8:] = imputer_ASF.fit_transform(X.iloc[:, 8:])
    
    ''''
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    
    '''
#def __Predict__(self,gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score
            
    models_list = []
    models_list.append(('LOG', LogisticRegression()))
    models_list.append(('RFC', RandomForestClassifier()))
    models_list.append(('SVM', SVC(gamma = 'scale'))) 
    models_list.append(('NB', GaussianNB()))
    models_list.append(('KNN', KNeighborsClassifier()))
            
    results = []
    names = []
            
    accuracy_score = {}
            
    for name, model in models_list:
        cv_results = cross_val_score(estimator = model, X = X, y = y, cv=10,
                                             scoring='accuracy', n_jobs = -1)
        results.append(cv_results)
        names.append(name)
        #print( "%s: %f " % (name, cv_results.mean()))
        accuracy_score[name]=cv_results.mean()
            
    #print(accuracy_score)
            
    Pred_Form1 = [[gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF]]
            #Pred_Form2 = [[0,60,16,4,30,0,1500,0.8,1]]
            
    max_key = max(accuracy_score, key=accuracy_score.get)
    #print(max_key)
            
    if(max_key=='RFC'):
                
        from sklearn.ensemble import RandomForestClassifier
                #rf = RandomForestClassifier()
        rf = RandomForestClassifier(n_estimators = 50, criterion = 'entropy', bootstrap= True,
                                            max_features = 'auto')
        rf.fit(X, y)
                
        y_pred1 = rf.predict(Pred_Form1)
                #print(y_pred1)
        return y_pred1
                
    elif(max_key=='LOG'):
        #print("CheckPoint1")
                #LogReg
        from sklearn import linear_model
                
        log_reg = linear_model.LogisticRegression(penalty='l2')
        log_reg.fit(X,y)
                
        y_pred_log1 = log_reg.predict(Pred_Form1)
        #print (y_pred_log1)       
        return y_pred_log1
            
    elif(max_key=='NB'):
            #GAUBAS
        from sklearn.naive_bayes import GaussianNB
                
        GB = GaussianNB()
        GB.fit(X,y)
                
        y_pred_GB1 = GB.predict(Pred_Form1)
                
        return y_pred_GB1


def main(gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF):
    result = Train(gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF)
    #print(gender,age,educ,SES,MMSE,CDR,eTIV,nWBV,ASF)
    return result


#if __name__ = '__main__':
    
'''
import statsmodels.api as sm
y1 = le.fit_transform(y)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categories = [0])
y1 = ohe.fit_transform(y1)


from sklearn.model_selection import GridSearchCV
parameters = [{'n_estimators' : [1, 5, 10, 15, 20], 'criterion' : ['gini', 'entropy'],
               'max_features' :['auto', 'sqrt'], 'bootstrap' : [True, False]}]
grid = GridSearchCV(estimator= rf, param_grid = parameters,
                    scoring = 'accuracy',
                    cv = 10, n_jobs=-1)
grid.fit(X_train, y_train)
best_accuracy = grid.best_score_
best_paramenters = grid.best_params_


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
cm = confusion_matrix(y_test, y_pred, labels=['Demented', 'Nondemented'])
acc = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))




import statsmodels.api as sm
y1 = le.fit_transform(y)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categories = [0])
y1 = ohe.fit_transform(y1)


regressor_OLS = sm.OLS(y1, X1).fit()
regressor_OLS.summary()

corr = oasis_long.corr()
sns.heatmap(corr, vmin = 0, vmax = 1, cmap=sns.light_palette("green"),
            linewidths = 2)

sns.set(style="whitegrid")

sns.boxenplot(x=  X1.iloc[:, 5], y = X1.iloc[:, 3],
              color="b", scale='linear')

sns.boxenplot(x= X1['SES'], y=y,
              color="pink", scale='linear')

sns.boxenplot(x= X1['CDR'], y=y,
              color="orange", scale='linear')

sns.boxenplot(x= X1['EDUC'], y=y,
              color="green", scale='linear')

sns.boxenplot(x= X1['Age'], y=y,
              color="purple", scale='linear')

sns.boxenplot(x= X1['eTIV'], y=y,
              color="grey", scale='linear')
'''