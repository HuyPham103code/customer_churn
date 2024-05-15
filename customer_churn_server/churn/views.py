from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import joblib


model = joblib.load(r'D:\nam_3\data_analysis\customer_churn\decision_tree_model.pkl')
print('log')
# Create your views here.
def transform_and_predict(features):
    # Transform the features to the expected format
    transformed_features = [[
        features['creditScore'],
        features['age'],
        features['tenure'],
        int(features['hasCrCard']),
        int(features['isActiveMember']),
        features['estimatedSalary'],
        features['geography'] == 'France',
        features['geography'] == 'Germany',
        features['geography'] == 'Spain',
        features['gender'] == 'Female',
        features['gender'] == 'Male',
        features['totalProducts'] > 2,
        features['totalProducts'] == 1,
        features['totalProducts'] == 2,
        features['accountBalance'] > 0,
        features['accountBalance'] == 0,
    ]]
    # test = [[300, 20, 1, 1, 1, 1000.67, True, False, False, False, True, True, False, False, True, False]]
    # print([test])
    prediction = model.predict(transformed_features)
    # Return a simple string for demonstration
    result = "Churn" if prediction[0] == 1 else "No Churn"
    print(result)
    if prediction[0] == 1:
        print('Churn')
    elif prediction[0] == 0:
        print('No churn')
    else:
        print('diffirent!')
    return prediction

class ChurnPredictionView(APIView):
    def post(self, request):
        try:
            data = request.data  # Use request.data with REST Framework
            prediction = transform_and_predict(data)
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        



    ####    đang chạy thử chương trình
    ##  nó bị lỗi không có đủ library để đọc plk
    #   và còn bị xung đột version, vì mình train model trên colab, nên nó sẽ bị xung đột với version ở local