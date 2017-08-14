import requests

from nba_images_client.utilities import convert_from_svg_to_png, resize_image
from nba_images_client.models import Team, FileType, ImageDimensions


class NbaImagesClient:

    @staticmethod
    def get_team_logo(team, file_type=FileType.PNG, image_dimensions=ImageDimensions(height=150, length=150)):
        r = requests.get('http://i.cdn.turner.com/nba/nba/assets/logos/teams/primary/web/{team_abbreviation}.svg'
                         .format(team_abbreviation=Team.get_abbreviation(team)))

        r.raise_for_status()

        return resize_image(png_data=convert_from_svg_to_png(r.content),
                            file_type=file_type,
                            image_dimensions=image_dimensions)

    @staticmethod
    def get_player_head_shot(player_id, file_type=FileType.PNG, image_dimensions=ImageDimensions(height=260, length=190)):
        r = requests.get('https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png'
                         .format(player_id=player_id))

        r.raise_for_status()

        return resize_image(png_data=r.content,
                            file_type=file_type,
                            image_dimensions=image_dimensions)
