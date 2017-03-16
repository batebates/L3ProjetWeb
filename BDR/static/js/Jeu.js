function modeAttente(message){

}
function affichageReponses(message){

}
function affichageScore(message){

}

ws.onmessage = function(message) {

  var reception = message.data;
  console.log(reception);
};

$('form[id^=carte-]').on('submit',function(event){
  var reponse = JSON.stringify({"path": path,
  "reponse":this.childNodes[3].value,
  "user":user
});
  //console.log(reponse);
  ws.send(reponse);
  return false;
});
