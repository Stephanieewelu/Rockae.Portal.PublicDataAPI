from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from apps.contract.models import QuizFeedback
from rest_framework import serializers
from apps.contract.models import QuizFeedback

class QuizFeedbackSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = QuizFeedback
        # Return only the fields we are interested in.
        fields = ('title', 'message', 'rating', 'full_name', 'email')

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
        "You can filter by title, full_name, and email. "
        "The most recent feedback records are returned first."
    ),
    tags=["Quiz Feedback"]
)
@api_view(['GET'])
def list_quiz_feedback(request):
    # Retrieve all QuizFeedback records, ordered by most recent first.
    feedbacks = QuizFeedback.objects.all().order_by('-create_date')

    # Optional filtering parameters
    title = request.query_params.get('title')
    full_name = request.query_params.get('full_name')
    email = request.query_params.get('email')

    if title:
        feedbacks = feedbacks.filter(title__icontains=title)
    if full_name:
        feedbacks = feedbacks.filter(
            Q(firstname__icontains=full_name) | Q(lastname__icontains=full_name)
        )
    if email:
        feedbacks = feedbacks.filter(email__icontains=email)

    # Apply pagination with defaults
    page = request.query_params.get('page', 1)
    page_size = request.query_params.get('page_size', 10)
    paginator = Paginator(feedbacks, page_size)
    try:
        feedbacks_page = paginator.page(page)
    except PageNotAnInteger:
        feedbacks_page = paginator.page(1)
    except EmptyPage:
        feedbacks_page = paginator.page(paginator.num_pages)

    serializer = QuizFeedbackSerializer(feedbacks_page, many=True)
    response_data = {
        "count": paginator.count,
        "num_pages": paginator.num_pages,
        "current_page": feedbacks_page.number,
        "results": serializer.data
    }
    return Response(response_data, status=status.HTTP_200_OK)