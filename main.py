import numpy as np
import pyxel


class Camera:
    def __init__(
        self,
        pos: np.array,
        h_angle: float,
        v_angle: float,
        screen_d: float,
        screen_w: int,
        screen_h: int,
    ):
        self.camera_pos = np.array(pos, dtype=float)
        self.camera_h_angle = h_angle
        self.camera_v_angle = v_angle
        self.screen_d = screen_d
        self.screen_w = screen_w
        self.screen_h = screen_h

    def cal_pos_on_screen(self, pos: np.array) -> tuple[int, int] | None:
        """
        3Dの世界座標をカメラ視点のスクリーン座標に変換する。
        """
        # 1. カメラ座標系への変換
        relative_pos = pos - self.camera_pos
        x, y, z = relative_pos

        # 2. カメラの回転
        cos_h, sin_h = np.cos(self.camera_h_angle), np.sin(self.camera_h_angle)
        cos_v, sin_v = np.cos(self.camera_v_angle), np.sin(self.camera_v_angle)

        # 水平回転（Yaw）
        x_prime = cos_h * x - sin_h * z
        z_prime = sin_h * x + cos_h * z

        # 垂直回転（Pitch）
        y_prime = cos_v * y - sin_v * z_prime
        z_prime = sin_v * y + cos_v * z_prime

        # 3. 透視投影
        if z_prime <= 0:
            return None  # カメラの後ろにある場合は描画しない

        screen_x = int((x_prime / z_prime) * self.screen_d + self.screen_w / 2)
        screen_y = int((y_prime / z_prime) * self.screen_d + self.screen_h / 2)

        return screen_x, screen_y

    def move(self, dx: float, dy: float, dz: float):
        """カメラの位置を変更する"""
        self.camera_pos += np.array([dx, dy, dz])

    def rotate(self, dh: float, dv: float):
        """カメラの向きを変更する"""
        self.camera_h_angle += dh
        self.camera_v_angle += dv


class App:
    def __init__(self):
        pyxel.init(160, 120, fps=60)
        pyxel.mouse(visible=True)

        h_angle = np.pi / 2
        w_angle = np.pi / 2
        distance = 10

        self.camera = Camera(
            np.array([0, 0, 0]),
            h_angle=h_angle,
            w_angle=w_angle,
            screen_d=distance,
            screen_w=160,
            screen_h=120,
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


App()
