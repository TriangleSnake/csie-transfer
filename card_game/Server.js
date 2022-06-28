function doGet(e) {
  function check_roomlst(str){
    for (var i=1;i<=Sheet.getLastColumn();i++){
      if (Sheet.getRange(2,i).getValue()==str) return i
    }
    return -1
  }
  function add_player(str,roomnum){
    for (var i=4;i<=7;i++){
      if (Sheet.getRange(i,roomnum).getValue()==''){
        Sheet.getRange(i,roomnum).setValue(str);
        return i-4;
      }
    }
    return -1
  }
  function search(name,roomnum){
    for (var i=4;i<=7;i++){
      if (Sheet.getRange(i,roomnum).getValue()==name) return i-4;
    }
  }
  function send_card(player_number,roomnum){
    var new_card=[]
    var card=Sheet.getRange(9,roomnum).getValue().replace('[','').replace(']','').split(',')
    for (var i=0;i<52;i++){
      if (i%4==player_number){
        new_card.push(card[i]);
      }
    }
    return new_card.toString()
  }
  if (typeof(e)=='undefined') return ContentService.createTextOutput('-1');
  var receive=e.parameter;
  var win=receive.win;
  var SpreadSheet=SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/11Y7bocc0FVuHIJWCgbjCczjXPksejnRcjE6FZtc-kEc/");
  Sheet=SpreadSheet.getSheetByName("工作表1");
  var room=receive.room
  var name=receive.name
  var wait=receive.wait
  var create_room=receive.create_room
  var first=receive.first
  var send=receive.send
  var start=receive.start
  if (typeof(first)!=="undefined"){
    var roomnum=check_roomlst(room)
    Sheet.getRange(11,roomnum).setValue(first)
    return ContentService.createTextOutput("OK")
  }
  if (typeof(win)!=='undefined'){
    var roomnum=check_roomlst(room)
    Sheet.getRange(20,roomnum).setValue(win)
    return ContentService.createTextOutput('ok')
  }
  if (typeof(wait)!=="undefined"){
    if (wait=='1'){
      var roomnum=check_roomlst(room);
      var card=Sheet.getRange(13,roomnum).getValue()
      var turn=String(Sheet.getRange(11,roomnum).getValue())
      var player=[]
      var player_card_number=[]
      for (var i=4;i<=7;i++){
        player.push(String(Sheet.getRange(i,roomnum).getValue()))
        player_card_number.push(String(Sheet.getRange(i+11,roomnum).getValue()))
      }
      var msg={
        "turn":turn,
        "card":card,
        "player1":{
          "name":player[0],
          "number":player_card_number[0]
        },
        "player2":{
          "name":player[1],
          "number":player_card_number[1]
        },
        "player3":{
          "name":player[2],
          "number":player_card_number[2]
        },
        "player4":{
          "name":player[3],
          "number":player_card_number[3]
        }
      }
      if (Sheet.getRange(20,roomnum).getValue()!==''){
        var msg={
        "turn":"U2FsdGVkX19Fug/Za/QfXk5FH8b4HAoTMsNS9/RC3bY=",
        "card":card,
        "player1":{
          "name":player[0],
          "number":player_card_number[0]
        },
        "player2":{
          "name":player[1],
          "number":player_card_number[1]
        },
        "player3":{
          "name":player[2],
          "number":player_card_number[2]
        },
        "player4":{
          "name":player[3],
          "number":player_card_number[3]
        },
        "win":Sheet.getRange(20,roomnum).getValue().toString()
      }
        msg=JSON.stringify(msg)
        return ContentService.createTextOutput(msg)
      }
      msg=JSON.stringify(msg)
      return ContentService.createTextOutput(msg);
    }
    else return ContentService.createTextOutput("WTF")
  }
  if (typeof(receive.card_num)!='undefined'){
    var roomnum=check_roomlst(room)
    var card_num=receive.card_num
    player_number=search(name,roomnum)
    player_number+=15
    Sheet.getRange(player_number,roomnum).setValue(card_num)
    return ContentService.createTextOutput('ok')
  }
  if (typeof(send)!=="undefined"){
    var roomnum=check_roomlst(room)
    var player_number=search(name,roomnum)
    player_number+=1
    player_number%=4
    player_number+=4
    var turn=Sheet.getRange(player_number,roomnum).getValue()
    var pass=receive.pass
    Sheet.getRange(11,roomnum).setValue(turn);
    Sheet.getRange(13,roomnum).setValue(receive.card);
    
    if (typeof(pass)!="undefined"){
      var pass_num=parseInt(Sheet.getRange(19,roomnum).getValue())
      pass_num+=1
      if (pass_num==3){
        Sheet.getRange(13,roomnum).setValue('["P"]');
        pass_num=0
      }
      Sheet.getRange(19,roomnum).setValue(pass_num)
    }
    else {
      Sheet.getRange(19,roomnum).setValue('0')
    }
    return ContentService.createTextOutput("OK")
  }
  if (typeof(start)!=="undefined"){
    var roomnum=check_roomlst(room)
    if (roomnum==-1)return ContentService.createTextOutput('{"is_exist":"false"}');
    var player_number=add_player(name,roomnum)
    if (player_number==-1)return ContentService.createTextOutput("{'is_exist':'full'}")
    else {
      var get_card=send_card(player_number,roomnum)
      return ContentService.createTextOutput('{"is_exist":"true","card":"['+get_card+']"}');
    }
    }
  if (typeof(create_room)!="undefineed"){
    var cards=receive.card
    var name=receive.name
    Sheet.getRange(2,Sheet.getLastColumn()+1).setValue(create_room);
    Sheet.getRange(9,Sheet.getLastColumn()).setValue(cards);
    var roomnum=Sheet.getLastColumn()
    Sheet.getRange(13,roomnum).setValue("[]")
    Sheet.getRange(19,roomnum).setValue('0')
    var player_number=add_player(name,roomnum);
    var get_card=send_card(player_number,roomnum);
    for (var i=15;i<=18;i++){
      Sheet.getRange(i,roomnum).setValue(13)
    }
    return ContentService.createTextOutput('{"is_exist":"true","card":"['+get_card+']"}');
  }
}
