from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q

class RegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "email","password"]
        # extra_kwargs = {"password":{"read_only":True}}

    def validate(self, data):
        """
        This method takes the dictionary of the field values that is why
        we are able to access both email and username
        => If you want to validate only one field than you can use
        validate_<Field_name>
        """
        username = data.get('username', None)
        email = data.get('email', None)

        if self.user_exists(username, email):
            raise serializers.ValidationError(f"{username} with {email} already exists in the database")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"] #need to hash the password and store in future
        )
        return user

    def user_exists(self, username,email):
        return User.objects.filter(Q(username=username) | Q(email=email)).exists()
