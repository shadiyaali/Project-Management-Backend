from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
import logging
logger = logging.getLogger(__name__) 
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import logging

logger = logging.getLogger(__name__)

class AdminLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        logger.info(f"Attempting to login user with email: {email}")

        if email is None or password is None:
            return Response({'error': 'Email and password must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_staff and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

        logger.warning(f"Failed login attempt for user: {email}")
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)






class UIDesignersAPIView(APIView):
 
    def get(self, request):
        designers = UIDesigners.objects.all()
        serializer = UIDesignersSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer = UIDesignersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UIDesignersDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return UIDesigners.objects.get(pk=pk)
        except UIDesigners.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "UIDesigner not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UIDesignersSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "UIDesigner not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UIDesignersSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "UIDesigner not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "UIDesigner deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class DevelopersAPIView(APIView):
 
    def get(self, request):
        designers = Developers.objects.all()
        serializer = DevelopersSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer =DevelopersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DevelopersDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Developers.objects.get(pk=pk)
        except Developers.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Developer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UIDesignersSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Developer not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer =DevelopersSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Developer not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "UIDesigner deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class SocialMediaAPIView(APIView):
 
    def get(self, request):
        designers = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer =SocialMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialMediaDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return SocialMedia.objects.get(pk=pk)
        except SocialMedia.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Social Media not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SocialMediaSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Social Media not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SocialMediaSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Social Media not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "Social Media deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class AccountAPIView(APIView):
 
    def get(self, request):
        designers = Account.objects.all()
        serializer = AccountSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AccountSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class ClientAPIView(APIView):
 
    def get(self, request):
        designers = Client.objects.all()
        serializer = ClientSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer =ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class ProjectsAPIView(APIView):
 
    def get(self, request):
        designers = Projects.objects.all()
        serializer = ProjectsSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer =ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Projects not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectsSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Projects not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectsSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Projects not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "Projects deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class InvoiceAPIView(APIView):
 
    def get(self, request):
        designers = Invoice.objects.all()
        serializer = InvoiceSerializer(designers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 
    def post(self, request):
        serializer =InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk=pk)
        except Invoice.DoesNotExist:
            return None

 
    def get(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(designer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InvoiceSerializer(designer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
    def delete(self, request, pk):
        designer = self.get_object(pk)
        if not designer:
            return Response({"error": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
        designer.delete()
        return Response({"message": "Invoice deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    