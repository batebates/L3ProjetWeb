function modeAttente(message){
$('#enonce').text(message.question);
$('#reponse_activate').text("Attendez Votre Tour");
}
function affichageReponses(message){
$('#enonce').text(message.question);
}
function affichageScore(message){
  $('#joueur1').text(message.joueur[0]);
  $('#joueur2').text(message.joueur[1]);
  $('#joueur3').text(message.joueur[2]);
  $('#joueur4').text(message.joueur[3]);
  $('#score1').text(message.score[0]);
  $('#score2').text(message.score[1]);
  $('#score3').text(message.score[2]);
  $('#score4').text(message.score[3]);
}

ws.onmessage = function(message) {

  var reception = JSON.parse(message.data);
  if (reception.etat==0){
    affichageReponses(reception)
  }
  else{
    modeAttente(message)
  }
  console.log(message);
  console.log(reception);
  affichageScore(reception);
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
