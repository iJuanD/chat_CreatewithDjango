from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthorSerializer, MessageSerializer
from .models import Author, Message

@api_view(["GET"])
def get_messages(request):
    messages = Message.objects.all().order_by("created_at")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_message(request):
    username = request.data.get("username")
    content = request.data.get("content")
    attachment = request.FILES.get("attachment")  # Capturar el archivo adjunto

    # Validar que haya al menos un campo proporcionado (content o attachment)
    if not username or (not content and not attachment):
        return Response(
            {"error": "Se requiere al menos contenido o un archivo adjunto."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Obtener o crear el autor
    author, _ = Author.objects.get_or_create(name=username)

    # Crear el mensaje con el contenido y/o archivo adjunto
    message_data = {"content": content, "attachment": attachment}
    serializer = MessageSerializer(data=message_data)

    if serializer.is_valid():
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def update_profile_picture(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return Response(
         {
            "error": "Autor no encontrado"
         }, status=status.HTTP_404_NOT_FOUND       
        )
    serializer = AuthorSerializer(author, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_author_by_username(request, username):
    try:
        author, _ = Author.objects.get_or_create(name=username)
    except Author.DoesNotExist:
        return Response(
         {
            "error": "Autor no encontrado"
         }, status=status.HTTP_404_NOT_FOUND       
        )
    serializer = AuthorSerializer(author, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)