from rest_framework import serializers
import markdown


class MarkdownContent(object):
    def __init__(self, title, content, view_format='json'):
        self.title = title
        self.content = content
        self.view_format = view_format


class MarkdownSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    view_format = serializers.CharField()
    md = markdown.Markdown()

    def create(self, validated_data):
        # TODO post 메서드로 데이터를 받아 마크다운 포맷으로 변환 후 리턴.
        title = validated_data.get('title')
        # TODO 파라미터로 넘어온 내용의 개행문자를 replace 해줘야한다... 혹시 다른 방법이 있을까?
        content = self.md.convert(validated_data.get('content').replace('\\n', '\n'))
        view_format = validated_data.get('view_format')
        return MarkdownContent(title, content, view_format)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.view_format = validated_data.get('view_format', instance.view_format)
        return instance
