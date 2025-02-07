import numpy as np
import pyxel


class Camera:
    def __init__(
        self,
        pos: np.array,
        h_angle: float,
        v_angle: float,
        z_angle: float,
        screen_d: float,
        screen_w: int,
        screen_h: int,
    ):
        self.camera_pos = np.array(pos, dtype=float)
        self.camera_h_angle = h_angle  # 水平角度
        self.camera_v_angle = v_angle  # 垂直角度
        self.camera_z_angle = z_angle  # z角度
        self.screen_d = screen_d
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.z_prime_handler = 4
        self.rotate(0, 0)

    def cal_pos_on_screen(self, pos: np.array) -> tuple[int, int, int] | None:
        """
        三次元の世界座標をカメラ視点のスクリーン座標に変換する。
        """
        # カメラ座標系への変換
        relative_pos = pos - self.camera_pos
        x, y, z = relative_pos
        d = np.sqrt((x**2 + y**2 + z**2))

        # 描画距離制限をかける
        if d > 60:
            return None

        # 水平回転（Yaw）
        x_prime = self._cos_h * x - self._sin_h * z
        z_prime = self._sin_h * x + self._cos_h * z

        # 垂直回転（Pitch）
        y_prime = self._cos_v * y - self._sin_v * z_prime
        z_prime = self._sin_v * y + self._cos_v * z_prime

        z_prime /= self.z_prime_handler

        # 透視投影
        if z_prime <= 0.0001:
            return None  # カメラの後ろにある場合は描画しない

        screen_x = int((x_prime / z_prime) * self.screen_d + self.screen_w / 2)
        screen_y = int((y_prime / z_prime) * self.screen_d + self.screen_h / 2)

        return screen_x, screen_y, d

    def move(self, dx: float, dy: float, dz: float):
        """カメラの位置を変更する"""
        self.camera_pos += np.array([dx, dy, dz])

    def rotate(self, dh: float, dv: float):
        """カメラの向きを変更する"""
        self.camera_h_angle += dh
        self.camera_v_angle += dv
        # カメラの回転
        self._cos_h = np.cos(self.camera_h_angle)
        self._sin_h = np.sin(self.camera_h_angle)
        self._cos_v = np.cos(self.camera_v_angle)
        self._sin_v = np.sin(self.camera_v_angle)


class App:
    def __init__(self):
        pyxel.init(160, 120, fps=60)
        pyxel.mouse(visible=True)

        h_angle = 0
        v_angle = 0
        z_angle = 0
        distance = 10

        self.camera = Camera(
            np.array([0, 0, 0]),
            h_angle=h_angle,
            v_angle=v_angle,
            z_angle=z_angle,
            screen_d=distance,
            screen_w=160,
            screen_h=120,
        )
        self.move_velo = 0.1

        pyxel.run(self.update, self.draw)

    def update(self):
        # 移動
        if pyxel.btn(pyxel.KEY_W):
            self.camera.move(
                self.move_velo * np.sin(self.camera.camera_h_angle),
                0,
                self.move_velo * np.cos(self.camera.camera_h_angle),
            )
        if pyxel.btn(pyxel.KEY_S):
            self.camera.move(
                -self.move_velo * np.sin(self.camera.camera_h_angle),
                0,
                -self.move_velo * np.cos(self.camera.camera_h_angle),
            )
        if pyxel.btn(pyxel.KEY_K):
            self.camera.move(0, -self.move_velo, 0)
        if pyxel.btn(pyxel.KEY_J):
            self.camera.move(0, self.move_velo, 0)

        # 角度調整
        v = 360
        if pyxel.btn(pyxel.KEY_LEFT):
            self.camera.rotate(-np.pi / v, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.camera.rotate(np.pi / v, 0)
        if pyxel.btn(pyxel.KEY_UP):
            self.camera.rotate(0, -np.pi / v)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.camera.rotate(0, np.pi / v)

        # 奥行スケールを調整
        if pyxel.btn(pyxel.KEY_Z):
            self.camera.z_prime_handler += 0.01
        if pyxel.btn(pyxel.KEY_X):
            self.camera.z_prime_handler -= 0.01

    def draw_debug(self):
        """
        デバッグ情報を出力
        """
        pyxel.text(0, 0, "camera_pos: " + str(self.camera.camera_pos), 7)
        pyxel.text(0, 8, "h_angle: " + str(np.rad2deg(self.camera.camera_h_angle)), 7)
        pyxel.text(0, 16, "w_angle: " + str(np.rad2deg(self.camera.camera_v_angle)), 7)
        pyxel.text(0, 24, "z_prime: " + str(self.camera.z_prime_handler), 7)

    def draw(self):
        pyxel.cls(0)
        d = 20
        for z in range(50):
            for x in range(50):
                pos = self.camera.cal_pos_on_screen(np.array([x * 5, 10, z * 5]))
                if pos != None:
                    px, py, pd = pos
                    pyxel.pset(px, py, (8 if ((x + z) % d == 0) else 7))
        self.draw_debug()


App()
