from manim import *
import copy
import numpy as np

## /!\ COME USARE IL CODICE ##
# installare python e manim con tutte le dipendenze del caso, vedere il link
#   https://docs.manim.community/en/stable/installation.html
# lanciare uno dei seguenti comandi (il primo crea il video in bassa qualità e
# lo mostra immediatamente, il secondo lo crea in 4K)
# > manim -pql albero_natale.py albero natale
# > manim -qk albero_natale.py albero natale

def crea_cono(R, h, clr=GREEN, res=[5, 5]):
    # Crea un manim object fatto a cono con raggio R e altezza h, di colore clr,
    # e con risoluzione res
    def surf_cono(rho, theta):
        # definiamo la funzione che parametrizza il cono in coordinate polari
        cono_param = np.array([
            rho * np.cos(theta),
            rho * np.sin(theta),
            rho * h / R
            ])
        return cono_param


    # creiamo il manim object
    cono = Surface(
        lambda rho, theta : surf_cono(rho, theta),
        u_range = [0, R], # dominio di rho
        v_range = [0, 2*PI], # dominio di theta
        resolution = res, # risoluzione
        fill_color = clr,
        checkerboard_colors=[clr, clr]
        )
    return cono

def crea_nastro(R, h, num_spire, offset=0, clr=RED, res=100):
    # Crea un manim object che "gira" attorno al cono di raggio R e altezza h.
    # num_spire rappresenta il numero di giri completi fatti attorno al cono.
    # offset indica l'angolo di partenza per mettere spazio tra più ghirlande.
    # clr è il colore e res il numero di punti

    # la decorazione viene implementata come l'immagine di una curva
    t_span = np.linspace(0, 2*PI, res)
    path = [[
        _t / 2/PI * R * np.cos(num_spire*_t + offset)*1.1, # 1.1 serve a distanziare la curva dal cono
        _t / 2/PI * R * np.sin(num_spire*_t + offset)*1.1,
        _t / 2/PI * h
        ] for _t in t_span]
    nastro = VMobject(color=clr)
    nastro.set_points(path)
    return nastro

def crea_palla(R, h, rho, theta, clr=BLUE, rad=0.1):
    # pallina decorativa, implementata come una sfera di raggio rad e colore clr.
    # R ed h sono raggio e altezza del cono.
    # theta e rho indica la posizione della pallina: l'altezza viene determinata
    # automaticamente.
    palla = Sphere(
        center = (
            rho*np.cos(theta)*1.1,
            rho*np.sin(theta)*1.1,
            h * rho/R
            ),
        radius=rad,
        resolution=[5,5]
        ).set_color(clr)
    return palla


class albero_natale(ThreeDScene):
    def construct(self):
        R = 2 # raggio del cono
        h = 6 # altezza del cono

        # albero
        clr_albero = GREEN
        res_albero = [10, 10]
        corpo = crea_cono(R, h, clr_albero, res_albero)
        corpo.shift((0, 0, -h/2)) # sposteremo tutto di h/2 dall'origine

        # nastri
        clr_nastri = [BLUE, RED, YELLOW]
        num_spire = [5, 5, 5]
        offset = [_t * TAU/3 for _t in range(3)]
        nastri = []
        for _clr, _n, _off in zip(clr_nastri, num_spire, offset):
            _nastro = crea_nastro(R, h, _n, _off, _clr, 10000).shift((0, 0, -h/2))
            nastri.append(_nastro)

        # palle
        clr_palle = [BLUE, RED, YELLOW, ORANGE, PURPLE]
        n_palle = 100
        palle = []
        # le palline sono generate randomicamente
        for _n in range(n_palle):
            palle.append(
                crea_palla(
                    R,
                    h,
                    np.random.rand()*R,
                    np.random.rand()*TAU,
                    np.random.choice(clr_palle),
                    0.15).shift((0, 0, -h/2)))
        # /!\ l'albero è capovolto rispetto all'asse z: questa rotazione della
        #     camera lo farà apparire dritto
        self.set_camera_orientation(phi = 270*DEGREES)
        self.move_camera(phi = 270*DEGREES)
        #self.add_foreground_mobjects(corpo)
        #[self.add(_n) for _n in nastri]
        #[self.add(_p) for _p in palle]
        self.play(Create(corpo), run_time=2)
        self.wait(3)
        self.play(*[Create(_n) for _n in nastri], run_time=2)
        self.wait(3)
        self.play(*[Create(_p) for _p in palle], run_time=2)
        self.wait(3)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)
        return super().construct()



