class Republica:
    """Definición geométrica de México"""
    json = __import__('json')
    os = __import__('os')
    np = __import__('numpy')

    class Estado:
        mplPath = __import__('matplotlib.path', locals = None, globals = None, fromlist = [None], level = 0)
        np = __import__('numpy')
        def __init__(self, nombre, poligonos):
            self.nombre = nombre
            self.poligonos = []
            for poligono in poligonos:
                self.poligonos.append(self.mplPath.Path(poligono))
        def contiene(self, punto):
            for poligono in self.poligonos:
                if(poligono.contains_point(tuple(punto))):
                    return True
            return False
            
    def __init__(self):
        geojson = self.os.path.join(self.os.path.dirname(__file__), 'mexican_states.geojson')
        data = self.json.load(open(geojson, encoding = "utf-8"))
        self.estados = []
        for state in data["features"]:
            if(state["geometry"]["type"] == "Polygon"):
                self.estados.append(self.Estado(state["properties"]["NOM_ENT"], [state["geometry"]["coordinates"][0]]))
            else:
                self.estados.append(self.Estado(state["properties"]["NOM_ENT"], state["geometry"]["coordinates"][0]))

    def estadoSegunPunto(self,latitud, longitud):
        for estado in self.estados:
            if(estado.contiene([longitud, latitud])):
                return estado.nombre
        return self.np.NaN