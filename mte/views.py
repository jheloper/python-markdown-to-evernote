from django.views.generic.edit import FormView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from mte.forms import TestInputForm
from mte.serializers import MarkdownSerializer


class MarkdownAPIView(APIView):

    def post(self, request, format=None):
        serializer = MarkdownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestInputView(FormView):
    form_class = TestInputForm
    template_name = 'mte/input_form.html'
