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
        aov_h: 水平画角(スクリーンの大きさから計算する)
        aov_w: 垂直画角(スクリーンの大きさから計算する)
        """
        self.camera_x: int
        self.camera_y: int
        self.camera_z: int
        self.camera_h: int
        self.camera_h_angle: float
        self.camera_v_angle: float
        self.aov_h: float
        self.aov_w: float

        """
        スクリーンのパラメータ
        screen_d: カメラからのユークリッド距離
        screen_x: 空間上のスクリーンの左上のx座標
        screen_y: 空間上のスクリーンの左上のy座標
        screen_z: 空間上のスクリーンの左上のz座標
        screen_w: スクリーンの横幅
        screen_h: スクリーンの縦幅
        screen_u: スクリーンの横ベクトル
        screen_v: スクリーンの縦ベクトル
        """
        self.screen_d: float
        self.screen_x: int
        self.screen_y: int
        self.screen_z: int
        self.screen_w: int = 160
        self.screen_h: int = 120
        self.screen_u: tuple[float, float, float]
        self.screen_v: tuple[float, float, float]

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass
