from example import like_fruit
import pytest

class TestLikeFruit:
    @pytest.fixture
    def nom_fruit(self):
        return {
            "Pierre": {"ananas", "pomme"}, 
            "Paul": {"banane", "pomme"}
            }

    def test_pierre_likes_ananas(self, nom_fruit):
        assert like_fruit("Pierre", "ananas", nom_fruit) == True

    def test_pierre_dont_like_poire(self, nom_fruit):
        assert like_fruit('Pierre', 'poire', nom_fruit) is False