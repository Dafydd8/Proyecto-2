<script>
  import * as d3 from "d3"
  import albums from "/src/data/albums_copy.csv"
  
  // import atletas from "/src/data/athletes.json"

  let streams = [];
  for (let i = 0; i < albums.length; i++) {
    streams.push(parseInt(albums[i].Streams));
  }

  let bubble_size = d3
    .scaleRadial()
    .domain([0, d3.max(streams)])
    .range([0, 200])

  function albums_of(anio){
    const begin = (anio - 2003)*5;
    const end = begin + 5;
    const rta = albums.slice(begin, end);
    return rta;
  }

  function genres(generos){
    const rta = generos.split(";");
    console.log("rta", rta);
    return rta;
  }

  function generarPosiciones(n) {
    const padding = 20; // Margen para evitar posiciones demasiado cerca de los bordes
    const posiciones = [];
    const cubiculos = [[10,10], [60,10], [10,50], [60,50], [35,30]];
    for (var i = 0; i < n; i++) {
      const x = (1+ (Math.random())*0.3) * cubiculos[i][0]+0.5;
      const y = (1+ (Math.random())*0.3) * cubiculos[i][1]+1;
      posiciones.push([x, y]);
    }
    return posiciones;
  }

  function posicion_circulos(n) {
    const vertices = [];
    const r = 25; // Usamos 0.5 para que el vértice superior esté en (0%, -50%)

    // Caso n = 1
    if (n === 1) {
      return [[0, 0]]; // Única posición en el centro
    }

    // Caso n = 2
    for (let k = 0; k < n; k++) {
      const theta = ((2 * Math.PI * k) / n) + Math.PI/2;
      const pos = [r * Math.cos(theta), r * Math.sin(theta)];
      vertices.push(pos);
    }
    
    return vertices;
  }

  const posiciones = generarPosiciones(5);
  const color_genero = {
    "Hip Hop/Rap": ["195",	"45",	"107", "0.75"],
    "Pop": ["210",	"111",	"235", "0.75"],
    "Rock": ["210",	"88",	"11", "0.75"],
    "R&B/Soul": ["1",	"151",	"246", "0.75"],
    "Latin/Regueton": ["252",	"186",	"4", "0.75"],
    "Otros": ["95",	"205",	"138", "0.75"],
  }
  console.log(albums_of(2023));

</script>

<main>
  <div class="container">
    {#each albums_of(2007) as album, index}
    <div class="album_container" style="top: {posiciones[index][1]}%; left: {posiciones[index][0]}%">
      <div class="album">
        <div class="bubble">
          {#each posicion_circulos((genres(album.Generos).length)) as [x, y], index}
            {#if genres(album.Generos).length != 1}
            <div class="anio_dist">
              <div class="circle" style="left: {x}%; top: {y}% ; width: 75%; height: 75%; background-color: rgba({color_genero[genres(album.Generos)[index]][0]},{color_genero[genres(album.Generos)[index]][1]},{color_genero[genres(album.Generos)[index]][2]},{color_genero[genres(album.Generos)[index]][3]});"></div>
            </div>
            {/if}
            {#if genres(album.Generos).length == 1}  
              <div class="circle" style="transform: translate(-5%, -7.5%); width: 110%; height: 110%; background-color: rgba({color_genero[genres(album.Generos)[index]][0]},{color_genero[genres(album.Generos)[index]][1]},{color_genero[genres(album.Generos)[index]][2]},{color_genero[genres(album.Generos)[index]][3]});"></div>
            {/if}
          {/each}
          <img src="./public/images/burbuja.png" alt="Bubble" style="width: {bubble_size(parseInt(album.Streams))}px; height: {bubble_size(parseInt(album.Streams))}px">
        </div>
        <p>{album["Album"]} <br><span>{album["Artista"]}</span></p>
      </div>
    </div>
    {/each}

    <!-- Burbujas adicionales de relleno -->
    <div class="bubble filler" style="top: 25%; left: 85%;"></div>
    <div class="bubble filler" style="top: 70%; left: 5%;"></div>
  </div>

</main>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  position: relative;
  width: 100vw;
  height: 100vh;
}

.album_container {
  position: absolute;
  width: auto;
  height: auto;
}

.bubble {
  position: relative;
  width: auto;
  height: auto;
}
.album {
  display: flex;
  width: auto;
  height: auto;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
  
}

.bubble img {
  position: relative;
  width: 100px;
  height: 100px;
  object-fit: contain;
  z-index: 1;
}

.circle {
  position: absolute;
  border-radius: 50%;
  filter: blur(10px);
  transform: translate(15%, 15%);
  z-index: 0;
}

.album p {
  color: white;
  margin-top: 10px;
  font-size: 14px;
  position: absolute;
  top: 95%;
}

.album span {
  font-size: 12px;
  color: #ccc;
}

.filler {
  background-color: transparent;
  width: 120px;
  height: 120px;
}

</style>
