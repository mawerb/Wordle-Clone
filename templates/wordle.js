var height = 6; //number of guesses
var width = 5; // length of the word

var row = 0; // current guess
var col = 0; // attempt number

var gameOver = false;
var word = "SQUID";

window.onload = function(){
    initalize();
}

function initalize(){

    //Creating board
    for (let r = 0; r < height; r++){
        for(let c = 0; c < width; c++){
            //<span id = "0-0" class = "title"></span>
            let tile = document.createElement("span");
            tile.id = r.toString() + "-" + c.toString();
            tile.classList.add("tile");
            tile.innerText = "";
            document.getElementById("board").appendChild(tile);
        }
    }

    document.addEventListener('keyup',(e) => {
        if (gameOver) return;

        // alert(e.code);
        if ("KeyA" <= e.code && e.code <= "KeyZ"){
            if(col < width){
                let currTile = document.getElementById(row.toString() + "-" + col.toString())
                if(currTile.innerText == "")  {
                    currTile.innerText = e.code[3];
                    col+=1;
                }
            }
        }
        else if(e.code == "Backspace"){
            if(col > 0){
                col -= 1;
            }
            let currTile = document.getElementById(row.toString() + "-" + col.toString())
            currTile.innerText = "";
        }
        else if(e.code == "Enter"){
            if(col == width){
                row += 1
                col = 0
            }
        }
        if (!gameOver && row == height) {
            gameover = true;
            document.getElementById("answer").innerText = word
        }
    })


}