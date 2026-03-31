from rest_framework.views import APIView

class PublicAPIView(APIView):
    authentication_classes = []
    permission_classes = []