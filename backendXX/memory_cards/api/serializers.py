from rest_framework import serializers
from .models.models import Deck, Category, Card


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description')


class CategoryMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class DeckMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('name',)


class CardsSerializer(serializers.ModelSerializer):
    deck = DeckMiniSerializer(many=False)

    class Meta:
        model = Card
        fields = ('deck', 'title', 'question', 'answer')
        read_only_fields = ('deck', )
        depth = 1


class CardsMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title',)


class DeckSerializer(serializers.ModelSerializer):
    category = CategoryMiniSerializer(many=True)
    cards = CardsMiniSerializer(many=True)
    class Meta:
        model = Deck
        fields = ('name', 'description', 'category', 'cards')
