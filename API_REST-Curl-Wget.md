# Implementar el Juego usando un API REST y usar curl/wget como cliente.

## Obtener el Tablero del Juego (GET)

```
curl -X GET http://localhost:8000/tictactoe/
```
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe Board</title>
</head>
<style>
    h1 {
        color: orangered;
        margin-bottom: -5px;
    }

    p {
        margin-bottom: -10px;
    }

    .ui {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .row {
        display: flex;
    }

    .cell {
        border: none;
        width: 80px;
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        text-align: center;
        cursor: pointer;
        border: 1px solid gray;
    }

    .cell:active {
        outline: none;
    }

    /* Reset Button */
    #but {
        box-sizing: border-box;
        width: 95px;
        height: 40px;
        border: 1px solid dodgerblue;
        margin: 0;
        border-radius: 8px;
        font-family: Verdana,
            Geneva, Tahoma, sans-serif;

        background-color: whitesmoke;
        color: dodgerblue;
        font-size: 20px;
        cursor: pointer;
    }

    /* Player turn space */
    #print {
        font-family: Verdana,
            Geneva, Tahoma, sans-serif;
        color: dodgerblue;
        font-size: 20px;
    }

    /* Main Container */
    #main {
        text-align: center;
    }

    /* Game Instruction Text */
    #ins {
        font-family: Verdana, Geneva,
            Tahoma, sans-serif;
        color: dodgerblue;
    }

</style>

<body>
    <div id="main">
        <h1>TIC TAC TOE</h1>
        <p id="ins">
            Game starts by just Tap on
            box<br><br>First Player starts as
            <b>Player X </b>And Second Player as
            <b>Player O</b>
        </p>
        <br><br>
        <form action="/turn/" method="POST"> <input type="hidden" name="csrfmiddlewaretoken" value="00q4Yp1Y9PWQN0xuxdoENR8lBIS6n66zME7QR6wcYw7GFGaQUEjEp0Y59BBRK0rv">
            <div class="ui">

                <div class="row">

                    <input type="submit" id="cell_1_1"
                        name="cell_1_1" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_1_2"
                        name="cell_1_2" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_1_3"
                        name="cell_1_3" class="cell" value=" "
                        maxlength="1">

                </div>

                <div class="row">

                    <input type="submit" id="cell_2_1"
                        name="cell_2_1" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_2_2"
                        name="cell_2_2" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_2_3"
                        name="cell_2_3" class="cell" value=" "
                        maxlength="1">

                </div>

                <div class="row">

                    <input type="submit" id="cell_3_1"
                        name="cell_3_1" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_3_2"
                        name="cell_3_2" class="cell" value=" "
                        maxlength="1">

                    <input type="submit" id="cell_3_3"
                        name="cell_3_3" class="cell" value=" "
                        maxlength="1">

                </div>
            </div>
                <br><br><br>
        </form>
        <form action="/reset/" method="POST"> <input type="hidden" name="csrfmiddlewaretoken" value="00q4Yp1Y9PWQN0xuxdoENR8lBIS6n66zME7QR6wcYw7GFGaQUEjEp0Y59BBRK0rv">
            <button id="but">
                RESET
            </button>
        </form>
        <br><br>
        <p id="print">Turn de: X </p>
        <p id="print">playerX 1 - 0 playerO</p>
        <p id="print">Número de partidas jugadas: 1</p>

    </div>

</body>

</html>
```
## Procesar un turno del Juego (POST)

### Con los tokens correspondientes se puede realizar el post y se procesa el turno modificando la celda a1 con una X
```
curl -X POST -b "sessionid=te2hsmwosfj0g58r3fvortsktfztgh3r; csrftoken=mwCVUKRTXdp70mHivYr7pNbjAXqKWRFkBfUMOM268TQaxM94dgNMOYJFDL6h8jSq" -d "csrfmiddlewaretoken=rr3SPbaKpSCZhwLpoXphCPiNNEi3h8hkGalJJdlXAy32OWdb6fLW10Q9QsYAtAuq&cell_1_1=X" http://localhost:8000/turn/