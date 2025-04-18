from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from apps.contract.models import QuizFeedback
from rest_framework import serializers

class QuizFeedbackSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = QuizFeedback
        fields = ('title', 'message', 'rating', 'full_name', 'email', 'quiz','create_date')

    def get_full_name(self, obj) -> str:
        return f"{obj.firstname} {obj.lastname}".strip()


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
            name="title",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by feedback title (case-insensitive partial match)"
        ),
        OpenApiParameter(
            name="full_name",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by full name of feedback creator (matches firstname or lastname)"
        ),
        OpenApiParameter(
            name="email",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Filter by email address (case-insensitive partial match)"
        ),
        OpenApiParameter(
            name="quiz",
            type=int,
            location=OpenApiParameter.QUERY,
            description="Filter by quiz ID"
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
        200: QuizFeedbackSerializer(many=True),
        400: {"description": "Bad Request"}
    },
    summary="List Quiz Feedback",
    description=(
        "Retrieves a paginated list of quiz feedback records containing only title, message, rating, "
        "the creator's full name (combining firstname and lastname), and email. "
        "You can filter by title, full_name, email, and quiz. "
        "The most recent feedback records are returned first."
    ),
    tags=["Quiz Feedback"]
)
@api_view(['GET'])
def list_quiz_feedback(request):
    # Base queryset, newest first
    feedbacks = QuizFeedback.objects.all().order_by('-create_date')

    # Extract filters
    title     = request.query_params.get('title')
    full_name = request.query_params.get('full_name')
    email     = request.query_params.get('email')
    quiz_id   = request.query_params.get('quiz')

    # Apply filters
    if title:
        feedbacks = feedbacks.filter(title__icontains=title)

    if full_name:
        feedbacks = feedbacks.filter(
            Q(firstname__icontains=full_name) | Q(lastname__icontains=full_name)
        )

    if email:
        feedbacks = feedbacks.filter(email__icontains=email)

    if quiz_id:
        print(quiz_id)
        feedbacks = feedbacks.filter(quiz=quiz_id)

    # Paginate
    page      = request.query_params.get('page', 1)
    page_size = request.query_params.get('page_size', 10)
    paginator = Paginator(feedbacks, page_size)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    serializer = QuizFeedbackSerializer(page_obj, many=True)
    return Response({
        "count": paginator.count,
        "num_pages": paginator.num_pages,
        "current_page": page_obj.number,
        "results": serializer.data
    }, status=status.HTTP_200_OK)
