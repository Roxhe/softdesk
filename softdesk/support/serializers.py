from django.utils import timezone
from rest_framework import serializers
from .models import User, Project, Issue, Comment, Contributor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthdate', 'can_be_contacted', 'can_data_be_shared']

    def validate_birthdate(self, value):
        today = timezone.now().date()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 15:
            raise serializers.ValidationError("User must be at least 15 years old")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

    def validate_other_contributors(self, value):
        user_ids = User.objects.filter(username__in=value).values_list('id', flat=True)
        project_id = self.context['request'].data.get('project')
        project_contributor_ids = Contributor.objects.filter(project_id=project_id).values_list('user', flat=True)
        for user_id in list(user_ids):
            if user_id not in project_contributor_ids:
                raise serializers.ValidationError("User(s) aren't contributor(s) of the project.")
        return list(user_ids)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
