<script>
  import * as d3 from "d3"
  import albums from "/src/data/albums_copy.csv"
  // import atletas from "/src/data/athletes.json"

  console.log("albums", albums)

  let diccionarioColores = {
    0: "#FF0000",
    1: "#00FF00",
    2: "#0000FF"
  };

  console.log(diccionarioColores[0])

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
    }/*
    if (n === 2) {
      return [[0, -50], [0, 50]]; // Semirecta vertical
    }

    for (let k = 0; k < n; k++) {
      const theta = (2 * Math.PI * k) / n;
      const x = r * Math.cos(theta);
      const y = r * Math.sin(theta);

      // Transformar a porcentajes
      const xPerc = x * 100;
      const yPerc = -y * 100; // Invertir y para cumplir con el requerimiento

      vertices.push([xPerc, yPerc]);
  }
*/
  return vertices;
}

const n = 3; // Número de vértices
console.log(posicion_circulos(n));

</script>

<main>
  <div class="container">
    <div class="album_container" style="top:50%; left:50%">
      <div class="album">
        <div class="bubble">
          {#each posicion_circulos(3) as [x, y], index}
            <div class="circle" style="left: {x}%; top: {y}% ; width: 80%; height: 80%; background-color: rgba(210, 88, 11, 0.75);"></div>
          {/each}
          <img src="./public/images/burbuja.png" alt="Bubble">
        </div>
        <p>In Between Dreams <br><span>Jack Johnson</span></p>
      </div>
    </div>
      <!---
      <div class="album" style="top: 40%; left: 50%;">
        <img src="./public/images/burbuja.png" alt="Bubble" style="width: 100px; height: 100px">
        <p>Late Registration <br><span>Kanye West</span></p>
      </div>
      <div class="album" style="top: 60%; left: 15%;">
        {#each posicion_circulos(1) as [x, y], index}
        <div class="circle" style="top: {y}%; left: {x}%; width: 100%; height: 100%; color: {diccionarioColores[0]}"></div>
        {/each}
        <img src="./public/images/burbuja.png" alt="Bubble" style="width: 100px; height: 100px">
        <p>X&Y <br><span>Coldplay</span></p>
      </div>
      <div class="album" style="top: 30%; left: 70%;">
        <img src="./public/images/burbuja.png" alt="Bubble" style="width: 100px; height: 100px">
        <p>Demon Days <br><span>Gorillaz</span></p>
      </div>
      <div class="album" style="top: 80%; left: 40%;">
        <img src="./public/images/burbuja.png" alt="Bubble" style="width: 100px; height: 100px">
        <p>The Massacre <br><span>50 Cent</span></p>
      </div>
    -->
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
  width: auto;
  height: auto;
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
  transform: translate(10%, 10%);
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
