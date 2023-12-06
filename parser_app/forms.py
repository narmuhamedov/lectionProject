from django import forms
from . import models, parser, parser2


class ParserForm(forms.Form):
    MEDIA_CHOISCES = (("manas.kg", "manas.kg"),('ts.kg', 'ts.kg'))
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "manas.kg":
            film_parser = parser.parser_manas()
            for i in film_parser:
                models.ParserModel.objects.create(**i)

        elif self.data["media_type"] == "ts.kg":
            film_parser = parser2.parser_games()
            for i in film_parser:
                models.ParserModel.objects.create(**i)