import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, "3D Test", fps=60)

        """
        座標は左手系に従う(z軸が奥にむかって正)
        """

        """
        カメラのパラメータ
        camera_x: カメラのx座標
        camera_y: カメラのy座標
        camera_z: カメラのz座標
        camera_h_angle: 水平方向の角度。0でz軸方向を向く。+pi/2で、x軸と同じ向き
        camera_v_angle: 垂直方向の角度。0でz軸方向を向く。+pi/2で、y軸と同じ向き
        """
        self.camera_x: int
        self.camera_y: int
        self.camera_z: int
        self.camera_h: int
        self.camera_h_angle: float
        self.camera_v_angle: float

        # スクリーンのパラメータ
        self.screen_x: int
        self.screen_y: int
        self.screen_z: int

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass
