<script>
  import { onMount } from "svelte";
  import * as d3 from "d3"
  import albums from "/src/data/albums_copy.csv"
  
  // import atletas from "/src/data/athletes.json"

  let streams = [];
  let anios = [];
  let currentYear = 2003; // Año inicial
  let maxYear = 2023; // Año máximo

  for (let i = 0; i < albums.length; i++) {
    streams.push(parseInt(albums[i].Streams));
  }

  for (let i = 0; i < 21; i++){
    anios.push(2003+i);
  }

  let bubble_size = d3
    .scaleRadial()
    .domain([d3.min(streams), d3.max(streams)])
    .range([85, 200])

  function albums_of(anio){
    const begin = (anio - 2003)*5;
    const end = begin + 5;
    const rta = albums.slice(begin, end);
    return rta;
  }

  function genres(generos){
    const rta = generos.split(";");
    return rta;
  }

  function generarPosiciones(n, pos) {
    console.log("antes",pos);
    const cubiculos = [[-12.5,-20], [-10,20], [-1,-1], [10,20], [12.5,-20]];
    for (var i = 0; i < n; i++) {
      const x = (1+ (Math.random())*0.5) * cubiculos[i][0];
      const y = (1+ (Math.random())*0.5) * cubiculos[i][1]-5;
      pos[i] = [x,y];
    }
    console.log("desp",pos);
  }

  function posicion_circulos(n) {
    const vertices = [];
    const r = 25;
    // Caso n = 1
    if (n === 1) {
      return [[0, 0]]; // Única posición en el centro
    }

    for (let k = 0; k < n; k++) {
      const theta = ((2 * Math.PI * k) / n) + Math.PI/2;
      const pos = [r * Math.cos(theta), r * Math.sin(theta)];
      vertices.push(pos);
    }
    
    return vertices;
  }

  let posiciones = [[0,0], [0,0], [0,0], [0,0], [0,0]];
  //console.log(posiciones);
  generarPosiciones(5, posiciones);
  //console.log(posiciones);
  generarPosiciones(5, posiciones);
  //console.log(posiciones);

  function cambiar(arreglo){
    arreglo[0] = arreglo[0]+1;
  }

  const color_genero = {
    "Hip Hop/Rap": ["195",	"45",	"107", "0.75"],
    "Pop": ["210",	"111",	"235", "0.75"],
    "Rock": ["210",	"88",	"11", "0.75"],
    "R&B/Soul": ["1",	"151",	"246", "0.75"],
    "Latin/Regueton": ["252",	"186",	"4", "0.75"],
    "Otros": ["95",	"205",	"138", "0.75"],
  }

  var scrolling = false;

  // Función para manejar la animación de cambio de año
  function handleScroll(event) {
    if (scrolling) return;

    if (event.deltaY > 0 && currentYear < maxYear) {
      currentYear += 1;
    } else if (event.deltaY < 0 && currentYear > 2003) {
      currentYear -= 1;
    }

    scrolling = true;
    setTimeout(() => scrolling = false, 500);
  }

  onMount(() => {
    window.addEventListener("wheel", handleScroll);
    return () => {
      window.removeEventListener("wheel", handleScroll);
    };
  });

</script>

<main>
  <div class="container">
    <div class="page">
      <h1>Musical Bubbles</h1>
    </div>
    <div class="page">
      <h1>cheat sheet</h1>
    </div>
    {#each anios as anio}
      <div class="page">
        {#each albums_of(anio) as album, index}
          <div class="album_container" style="width: {bubble_size(parseInt(album.Streams))}px; height: {bubble_size(parseInt(album.Streams))}px; top: {posiciones[index][1]}%; left: {posiciones[index][0]}%; animation-delay: {Math.random() * 3}s; animation-duration: {4 + Math.random() * 2}s;">      
            <div class="bubble">
              {#each posicion_circulos((genres(album.Generos).length)) as [x, y], index}
                {#if genres(album.Generos).length != 1}
                  <div class="circle" style="left: {x}%; top: {y}% ; width: 75%; height: 75%; background-color: rgba({color_genero[genres(album.Generos)[index]][0]},{color_genero[genres(album.Generos)[index]][1]},{color_genero[genres(album.Generos)[index]][2]},{color_genero[genres(album.Generos)[index]][3]});"></div>
                {/if}
                {#if genres(album.Generos).length == 1}  
                  <div class="circle" style="transform: translate(0%, -5%); width: 110%; height: 110%; background-color: rgba({color_genero[genres(album.Generos)[index]][0]},{color_genero[genres(album.Generos)[index]][1]},{color_genero[genres(album.Generos)[index]][2]},{color_genero[genres(album.Generos)[index]][3]});"></div>
                {/if}
              {/each}
              <img src="images/burbuja.png" alt="Bubble" style="width: {bubble_size(parseInt(album.Streams))}px; height: {bubble_size(parseInt(album.Streams))}px">
              {#if album.Valoracion == 1}  
                <img src="/images/circle.png" alt="Circle" style="position: absolute; transform: translate(0%, -5.5%);max-width: {bubble_size(parseInt(album.Streams))*1.125}px; max-height: {bubble_size(parseInt(album.Streams))*1.125}px">
              {/if}
              {#if album.Valoracion == 2}  
                <img src="/images/dashed_circle.png" alt="Circle" style="position: absolute; transform: translate(0%, -5.5%);max-width: {bubble_size(parseInt(album.Streams))*1.125}px; max-height: {bubble_size(parseInt(album.Streams))*1.125}px">
              {/if}
              {#if album.Valoracion == 4}  
                <img src="/images/picos_circle.png" alt="Circle" style="position: absolute; transform: translate(0%, -5.5%);max-width: {bubble_size(parseInt(album.Streams))*1.125}px; max-height: {bubble_size(parseInt(album.Streams))*1.125}px">
              {/if}
              {#if album.aoty == 1}  
                <div class="duck">
                  <img src="/images/patito.png" alt="Duck" style="max-width: {bubble_size(parseInt(album.Streams))*0.25}px; max-height: {bubble_size(parseInt(album.Streams))*0.25}px">
                </div>
              {/if}
            </div>
            <p>{album["Album"]} <br><span>{album["Artista"]}</span></p>
          </div>
        {/each}
      </div>
    {/each}
  </div>
  

</main>

<style>
  .container {
    margin-left: 0px;
    overflow-y: auto;
    width: 100vw;
    height: 100vh;
  }
  
  .page {
    padding: 2rem;
    width: auto;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .album_container {
    position: relative;
    width: auto;
    height: auto;
    animation: float 4s ease-in-out infinite;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .bubble {
    position: relative;
    width: auto;
    height: auto;
    display: flex;
    justify-content: center;
  }

  @keyframes float {
    0% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-20px); /* Subir 20px */
    }
    100% {
      transform: translateY(0); /* Volver a la posición original */
    }
  }

  @keyframes bounce2 {
    0%, 25%, 80%, 100% {
      transform: translateY(0) rotateZ(0deg); /* Posición inicial, sin rotación */
    }
    40% {
      transform: translateY(-150%) rotateZ(-360deg); /* Salto hacia arriba y rotación hacia atrás */
    }
    52% {
      transform: rotateZ(0deg); /* Salto hacia arriba y rotación hacia atrás */
    }
    60% {
      transform: translateY(-7.5px) ; /* Comienza a bajar, con rotación hacia atrás */
    }
  }

  .duck {
    animation: bounce2 2s infinite;
    position: absolute;
    z-index: 2;
    top: -20%;
  }

  .bubble img {
    position: relative;
    z-index: 1;
  }

  .circle {
    position: absolute;
    border-radius: 50%;
    filter: blur(10px);
    transform: translate(15%, 15%);
    z-index: 0;
  }

  .album_container p {
    color: white;
    margin-top: 20px;
    font-size: 14px;
    position: absolute;
    top: 95%;
  }

  .album_container span {
    font-size: 12px;
    color: #ccc;
  }

</style>
