import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as Token
from rest_framework.views import APIView
from .models import Chat, User
from .serializers import UserSignUpSerializer, UserLoginSerializer, ChatSerializer, UserSerializer

class UserSignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(Token):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    predefined_responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm an AI, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
    }

    def post(self, request):
        user = request.user
        if user.tokens < 100:
            return Response({"error": "Not enough tokens"}, status=status.HTTP_400_BAD_REQUEST)

        message = request.data.get('message', '').lower()
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Deduct tokens
        user.tokens -= 100
        user.save()

        keyword_responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I assist you with?",
            "help": "Sure, I'm here to help. What do you need assistance with?",
            "bye": "Goodbye! Have a great day!",
            "thanks": "You're welcome! If you have any other questions, feel free to ask."
        }

        # Default generic responses
        generic_responses = [
            "Thank you for your message. How can I assist you further?",
            "I'm here to help! What do you need assistance with?",
            "Your message has been received. How can I assist you today?",
            "Thanks for reaching out! What can I do for you?",
            "I appreciate your message. How may I assist you?"
        ]

        # Check for keyword in the message and select response
        ai_response = next((response for keyword, response in keyword_responses.items() if keyword in message.lower()), None)

        # If no keyword match, select a random generic response
        if not ai_response:
            ai_response = random.choice(generic_responses)

        # Generate a response
        response = self.predefined_responses.get(message, "This is a dummy AI response.")

        # Save chat history
        chat = Chat.objects.create(user=user, message=message, response=ai_response)

        # Serialize the chat instance
        serializer = ChatSerializer(chat)

        return Response(serializer.data, status=status.HTTP_200_OK)

class TokenBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
