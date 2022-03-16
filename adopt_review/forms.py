from django import forms
from adopt_review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
