# from rest_framework import serializers
# from .models import User


# class UserRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email','password1',)       # description #
        
# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password1', 'password2')  # description #

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = super().create(validated_data)
#         user.set_password(password)
#         user.save()
#         return user