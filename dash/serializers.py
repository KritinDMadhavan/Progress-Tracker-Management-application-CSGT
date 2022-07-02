from rest_framework import serializers
from .models import *

class personalserializer(serializers.ModelSerializer):
	class Meta:
		model=personal
		fields='__all__'

class conferneceserializer(serializers.ModelSerializer):
	class Meta:
		model=conference
		fields='__all__'

class journalserializer(serializers.ModelSerializer):
	class Meta:
		model=journal
		fields='__all__'

class bookchapterserializer(serializers.ModelSerializer):
	class Meta:
		model=book_chapters
		fields='__all__'

class bookeditorserializer(serializers.ModelSerializer):
	class Meta:
		model=book_editor
		fields='__all__'

class consultancyserializer(serializers.ModelSerializer):
	class Meta:
		model=consultancy_project
		fields='__all__'

class patentserializer(serializers.ModelSerializer):
	class Meta:
		model=patent
		fields='__all__'
