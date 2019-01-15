from rest_framework import serializers
from profiles.models import Profile, Match

def validate_statistics(value):
    if (type(eval(value['statistics'])) is dict == False):
        raise serializers.ValidationError('you did not supply a stringified Python dictionary')
    return value

def validate_achievements(value):
    if (type(eval(value['achievements'])) is list == False):
        raise serializers.ValidationError('you did not supply a stringified Python list')
    return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Profile
        fields = ('username', 'email', 'statistics', 'achievements')
        validators = [
            validate_statistics, validate_achievements
        ]





class MatchSerializer(serializers.ModelSerializer):
    class Meta():
        model = Match
        fields = ('players', 'duration', 'statistics')
        validators = [
            validate_statistics
        ]
