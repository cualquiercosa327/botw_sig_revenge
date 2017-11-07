class Config:
    draw_coverage = False
    draw_textures = False
    draw_grid = False
    draw_overdraw = False

    draw_texTypes = ['hght', 'mate', 'grass.extm', 'water.extm']
    draw_texType = "hght"

    draw_channels = ['all', 'r', 'g', 'b', 'a']
    draw_channel = "all"

    disable_alpha = False

    @staticmethod
    def NextTexType():
        for i in range(0, len(Config.draw_texTypes)):
            if Config.draw_texTypes[i] == Config.draw_texType:
                Config.draw_texType = Config.draw_texTypes[(i + 1) % len(Config.draw_texTypes)]
                break

    @staticmethod
    def NextChannel():
        for i in range(0, len(Config.draw_channels)):
            if Config.draw_channels[i] == Config.draw_channel:
                Config.draw_channel = Config.draw_channels[(i + 1) % len(Config.draw_channels)]
                break
