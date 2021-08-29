# limitMax = BaseTotalDFOthers['turbiedad'].quantile(0.75) + 1.5 * (BaseTotalDFOthers['turbiedad'].quantile(0.75) - BaseTotalDFOthers['turbiedad'].quantile(0.25))
fechaThreshold = '2020-12-03'
limitMax = 300
# DataBaseTMNoOutliers = BaseTotalDFOthers.loc[BaseTotalDFOthers['turbiedad'] < limitMax]
# DataBaseTMNoOutliers = BaseTotalDFFull.loc[BaseTotalDFFull['turbiedad'] < limitMax]
# DataBaseTMNoOutliers = BaseTotalDFPopayan.loc[BaseTotalDFPopayan['turbiedad'] < limitMax]

DataBaseTMNoOutliers = DataBaseTMNoOutliers.drop(['Unnamed: 0', 'turbiedad'], axis = 'columns')
DataBaseTMNoOutliers['Fecha'] = pd.to_datetime(DataBaseTMNoOutliers['Fecha'])
DataBaseTMNoOutliers = DataBaseTMNoOutliers.set_index(['Fecha'])

DataBaseTMNoOutliers = DataBaseTMNoOutliers.drop_duplicates()

DataBaseTMNoOutliers_dummies = pd.get_dummies(DataBaseTMNoOutliers['IDestacion'])
DataBaseTMNoOutliers = DataBaseTMNoOutliers.drop(['IDestacion'], axis = 'columns')
DataBaseTMNoOutliers = DataBaseTMNoOutliers.merge(DataBaseTMNoOutliers_dummies, left_index = True, right_index = True).resample('180T').mean()
DataBaseTMNoOutliers = DataBaseTMNoOutliers.dropna()

X_trainNO = DataBaseTMNoOutliers.loc[DataBaseTMNoOutliers.index < fechaThreshold].drop(['logTurbiedad'], axis = 'columns')
y_trainNO = DataBaseTMNoOutliers.loc[DataBaseTMNoOutliers.index < fechaThreshold]['logTurbiedad']

X_testNO = DataBaseTMNoOutliers.loc[DataBaseTMNoOutliers.index >= fechaThreshold].drop(['logTurbiedad'], axis = 'columns')
y_testNO = DataBaseTMNoOutliers.loc[DataBaseTMNoOutliers.index >= fechaThreshold]['logTurbiedad']


# ListKeyVariables = ['pH', 'potOxiReduccion', 'T', 'HR', 'PV', 'VV', 'P']
# X_trainNO = X_trainNO[ListKeyVariables]
# X_testNO = X_testNO[ListKeyVariables]