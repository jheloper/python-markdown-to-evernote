from django.http.response import JsonResponse
from django.views.generic.edit import FormView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from mte.forms import TestInputForm
from mte.serializers import MarkdownSerializer
from src.evernote_client_wrapper import EvernoteClientWrapper
from tests.en_api_token import dev_token


class MarkdownAPIView(APIView):

    def post(self, request, format=None):
        serializer = MarkdownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            view_format = serializer.data.get('view_format')
            print(view_format)
            if view_format == 'json':
                return JsonResponse(serializer.data)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkdownToEvernoteView(APIView):

    def post(self, request, format=None):
        serializer = MarkdownSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            client = EvernoteClientWrapper(token=dev_token, sandbox=True)
            client.create_note(note_title=serializer.data.get('title'), note_content=serializer.data.get('content'),
                               parent_notebook=client.get_default_notebook())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestInputView(FormView):
    form_class = TestInputForm
    template_name = 'mte/input_form.html'
