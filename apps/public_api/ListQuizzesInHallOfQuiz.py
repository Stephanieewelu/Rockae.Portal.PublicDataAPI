from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from apps.contract.models import Quiz
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    attempts = serializers.IntegerField(read_only=True)
    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_creator_name(self, obj) -> str:
        if obj.user and hasattr(obj.user, 'profile'):
            profile = obj.user.profile
            return f"{profile.firstname} {profile.lastname}".strip()
        return ""



@extend_schema(
    methods=["GET"],
    parameters=[
        OpenApiParameter(
            name='X-API-KEY',
            type=str,
            location=OpenApiParameter.HEADER,
            description='API key for authentication',
            required=True
        ),
        OpenApiParameter(
            name="quiz_id",
            type=int,
            location=OpenApiParameter.QUERY,
            description="Filter by quiz ID"
        ),
        OpenApiParameter(
            name="title",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by quiz title"
        ),
        OpenApiParameter(
            name="category",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by quiz category"
        ),
        OpenApiParameter(
            name="creator",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by the quiz creator's name (first or last name)"
        ),
        OpenApiParameter(
            name="page",
            type=int,
            location=OpenApiParameter.QUERY,
            description="Page number"
        ),
        OpenApiParameter(
            name="page_size",
            type=int,
            location=OpenApiParameter.QUERY,
            description="Number of items per page"
        ),
    ],
    responses={
        200: QuizSerializer(many=True),
        400: {"description": "Bad Request"}
    },
    summary="Retrieve All Global Quizzes",
    description=(
        "Retrieves a paginated list of all global quizzes in the system (where is_global is True), ordered by the "
        "number of quiz attempts. Optional filters include quiz_id, title, category, and the quiz creator's name. "
        "The number of attempts is computed using the QuizSubmission model, and the creator's full name is included "
        "in the response."
    ),
    tags=["Hall Of Quiz"]
)
@api_view(['GET'])
def list_quizzes_in_hallofquiz(request):
    # Retrieve only global quizzes
    quizzes = Quiz.objects.filter(is_global=True)

    # Filtering based on query parameters
    quiz_id = request.query_params.get('quiz_id')
    title = request.query_params.get('title')
    category = request.query_params.get('category')
    creator = request.query_params.get('creator')  # New query parameter for filtering by creator name
    
    if quiz_id:
        quizzes = quizzes.filter(id=quiz_id)
    if title:
        quizzes = quizzes.filter(quiz_title__icontains=title)
    if category:
        quizzes = quizzes.filter(category__icontains=category)
    if creator:
        # Filter quizzes based on the quiz creator's first or last name
        quizzes = quizzes.filter(
            Q(user__profile__firstname__icontains=creator) | Q(user__profile__lastname__icontains=creator)
        )

    # Annotate each quiz with "attempts" (i.e. number of related QuizSubmission records)
    quizzes = quizzes.annotate(
        attempts=Count('quizsubmission')
    ).order_by('-attempts')

    # Pagination parameters with defaults
    page = request.query_params.get('page', 1)
    page_size = request.query_params.get('page_size', 10)

    paginator = Paginator(quizzes, page_size)
    try:
        quizzes_page = paginator.page(page)
    except PageNotAnInteger:
        quizzes_page = paginator.page(1)
    except EmptyPage:
        quizzes_page = paginator.page(paginator.num_pages)

    serializer = QuizSerializer(quizzes_page, many=True)
    response_data = {
        "count": paginator.count,
        "num_pages": paginator.num_pages,
        "current_page": quizzes_page.number,
        "results": serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)
