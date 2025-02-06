import pyxel
import numpy as np
import math


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
        camera_pos: カメラの座標
        camera_h_angle: 水平方向の角度(-pi/2 ~ pi/2)。0でz軸方向を向く。+pi/2で、x軸と同じ向き
        camera_v_angle: 垂直方向の角度(-pi/2 ~ pi/2)。0でz軸方向を向く。+pi/2で、y軸と同じ向き
        aov_h: 水平画角(スクリーンの大きさから計算する)
        aov_w: 垂直画角(スクリーンの大きさから計算する)
        """
        self.camera_pos: np.array[int, int, int] = np.array([0, 0, 0])
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
        screen_pos: 空間上のスクリーンの左上の座標
        screen_w: スクリーンの横幅
        screen_h: スクリーンの縦幅
        screen_u: スクリーンの横ベクトル
        screen_v: スクリーンの縦ベクトル
        u, vの二つのベクトルでスクリーンを張る
        """
        self.screen_d: float
        self.screen_pos: np.array[int, int, int]
        self.screen_w: int = 160
        self.screen_h: int = 120
        self.screen_u: np.array[float, float, float]
        self.screen_v: np.array[float, float, float]

        pyxel.run(self.update, self.draw)

    def cal_camera_angle(self, velocity: float) -> tuple[float, float]:
        """
        描画スクリーン上のマウスの位置からカメラの角度を割り出す
        velocity: 角度変更強度
        """
        mid_w = self.screen_w // 2
        mid_h = self.screen_h // 2
        diff_w = mid_w - pyxel.mouse_x
        diff_h = mid_h - pyxel.mouse_y
        u_angle = (mid_w / diff_w) * (math.pi / 2) * velocity
        h_angle = (mid_h / diff_h) * (math.pi / 2) * velocity
        return u_angle, h_angle

    def cal_screen_pos(self) -> None:
        """
        スクリーンの座標を計算する
        """
        ul = self.cal_camera_pos(-self.aov_w, self.aov_h, self.screen_d)
        ur = self.cal_camera_pos(self.aov_w, self.aov_h, self.screen_d)
        dl = self.cal_camera_pos(-self.aov_w, -self.aov_h, self.screen_d)
        dr = self.cal_camera_pos(self.aov_w, -self.aov_h, self.screen_d)
        self.screen_u = ur - ul
        self.screen_h = dr - dl

    def cal_camera_pos(self, h_angle: float, v_angle: float, d: float) -> np.array:
        """
        カメラ視点の球座標を世界座標系に変換する
        """
        x = int(d * np.sin(self.camera_v_angle + v_angle))
        y = int(d * np.sin(self.camera_h_angle + h_angle))
        z = int(d * np.cos(self.camera_v_angle + v_angle))
        return np.array([x, y, z])

    def cal_pos_from_camera(self, pos: np.array) -> np.array:
        """
        世界座標系をカメラからのベクトルに変換する
        """
        return pos - self.camera_pos

    def cal_pos_on_screen(self, pos: np.array) -> tuple[int, int]:
        """
        世界座標系をスクリーン上のベクトルに変換する
        """
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


App()
