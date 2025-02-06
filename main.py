import pyxel
import numpy as np


class App:
    def __init__(self):
        pyxel.init(160, 120, "3D Test", fps=60)
        pyxel.mouse(visible=True)

        """
        座標は左手系に従う(z軸が奥にむかって正)
        """

        """
        今回実装するのは、フィールド上の座標を
        カメラからスクリーン上の座標に変換する処理
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
        self.dh_angle: float
        self.hw_angle: float

        """
        スクリーンのパラメータ
        screen_d: カtupleメラからのユークリッド距離
        screen_x: 空tuple間上のスクリーンの左上のx座標
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
        self.screen_u: np.array[float, float, float]
        self.screen_v: np.array[float, float, float]

        pyxel.run(self.update, self.draw)

    def change_camera_angle(self, velocity: float) -> tuple[float, float]:
        """
        描画スクリーン上のマウスの位置からカメラの角度を割り出す
        velocity: 角度変更強度
        """

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


App()
