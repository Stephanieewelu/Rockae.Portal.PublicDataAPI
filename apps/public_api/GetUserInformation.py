from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from django.contrib.auth import get_user_model
from apps.contract.models import Quiz, QuizResultSnapshot, Flashcard, UserProfile
from rest_framework import serializers


class UserInfoSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    bio = serializers.CharField(allow_blank=True, required=False)
    total_quiz_taken = serializers.IntegerField()
    average_score = serializers.FloatField()
    total_quizzes_owned = serializers.IntegerField()
    total_flashcards_owned = serializers.IntegerField()


User = get_user_model()
@extend_schema(
    operation_id='public_user_dashboard_by_identifier',
    parameters=[
        OpenApiParameter(
            name='X-API-KEY',
            type=str,
            location=OpenApiParameter.HEADER,
            description='API key for authentication',
            required=True
        ),
        OpenApiParameter(
            name='user_id',
            type=int,
            location=OpenApiParameter.QUERY,
            description='The ID of the user for whom to retrieve dashboard data (optional if username or email is provided)'
        ),
        OpenApiParameter(
            name='username',
            type=str,
            location=OpenApiParameter.QUERY,
            description='The username of the user (optional if user_id or email is provided)'
        ),
        OpenApiParameter(
            name='email',
            type=str,
            location=OpenApiParameter.QUERY,
            description='The email of the user (optional if user_id or username is provided)'
        )
    ],
    responses={
        200: OpenApiResponse(
            response=UserInfoSerializer,
            description='Successful response with user dashboard data'
        ),
        400: OpenApiResponse(
            response={'type': 'object', 'properties': {'error': {'type': 'string'}}},
            description='Bad Request'
        ),
        401: OpenApiResponse(
            response={'type': 'object', 'properties': {'error': {'type': 'string'}}},
            description='API key is missing or invalid'
        ),
        404: OpenApiResponse(
            response={'type': 'object', 'properties': {'error': {'type': 'string'}}},
            description='User or user profile not found'
        )
    },
    description=(
        "Public endpoint to retrieve a user's information data by specifying either user_id, username, or email. "
        "An API key is required in the header. Returns profile details along with aggregated statistics: total quizzes "
        "taken, average score, total quizzes owned, and total flashcards owned."
    ),
    examples=[
        OpenApiExample(
            'Success Response',
            value={
                'firstname': 'John',
                'lastname': 'Doe',
                'bio': 'Passionate about learning',
                'total_quiz_taken': 15,
                'average_score': 78.5,
                'total_quizzes_owned': 4,
                'total_flashcards_owned': 2
            },
            response_only=True
        )
    ],
    tags=['User']
)
@api_view(['GET'])
def get_user_info(request):
    user_id = request.query_params.get('user_id')
    username = request.query_params.get('username')
    email = request.query_params.get('email')

    if user_id:
        profile = UserProfile.objects.filter(user__id=user_id).first()
    elif username:
        profile = UserProfile.objects.filter(user__username=username).first()
    elif email:
        profile = UserProfile.objects.filter(user__email=email).first()
    else:
        return Response({'error': 'One of user_id, username, or email query parameters must be provided'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    if not profile:
        return Response({'error': 'User or user profile not found'}, status=status.HTTP_404_NOT_FOUND)
    
    target_user = profile.user
    stats = get_user_stats(target_user)
    dashboard_data = {
        "firstname": profile.firstname,
        "lastname": profile.lastname,
        "bio": profile.bio or "",
        **stats
    }

    serializer = UserInfoSerializer(dashboard_data)
    return Response(serializer.data, status=status.HTTP_200_OK)



def get_user_stats(target_user):
    total_quiz_taken = QuizResultSnapshot.objects.filter(candidate=target_user).count()

    avg_result = QuizResultSnapshot.objects.filter(candidate=target_user).aggregate(avg_score=Avg('percentage_score'))
    average_score = avg_result.get('avg_score') or 0

    total_quizzes_owned = Quiz.objects.filter(user=target_user).count()

    total_flashcards_owned = Flashcard.objects.filter(user=target_user).count()

    return {
        "total_quiz_taken": total_quiz_taken,
        "average_score": average_score,
        "total_quizzes_owned": total_quizzes_owned,
        "total_flashcards_owned": total_flashcards_owned
    }


