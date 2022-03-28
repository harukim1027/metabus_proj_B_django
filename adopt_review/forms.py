from django import forms
from adopt_review.models import Review, AdoptReviewComment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

class AdoptReviewCommentForm(forms.ModelForm):
    class Meta:
        model = AdoptReviewComment
        fields = ["user", "comment_content"]