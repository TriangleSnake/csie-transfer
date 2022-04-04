function doPost(e){
    var commands=[
      '/closetunnel',
      '/talktoall',
      '/opentunnel',
      '/checklist'
    ]
    const TriSnakeID='812518094'
    function sndmsg(id,text){
      UrlFetchApp.fetch("https://api.telegram.org/bot1908290137:AAFmO6RjCX6XlrRhyIVl-NTKrsZLkCP1QcQ/sendMessage?chat_id="+id+"&text="+text);
    }
    //紀錄內容
    var receive = JSON.parse(e.postData.contents);
    console.log("receive:"+receive);
    var d = new Date();
    var id = receive.message.from.id;
    var FirstName=receive.message.from.first_name;
    var LastName=receive.message.from.last_name;
    var group=receive.message.chat.title;
    var message = receive.message.text;
    var name=FirstName + " " + LastName;
    var photo =receive.message.photo;
    var SpreadSheet = SpreadsheetApp.openById("1GtMZYKKZetspkvu8fpGm9R05zAKWqhaJP8y0ali9qp0");
    var Sheet = SpreadSheet.getSheetByName("工作表1");
    var Sheet2 =SpreadSheet.getSheetByName("工作表2");
    var LastRow = Sheet.getLastRow();
    var LastRow2=Sheet2.getLastRow();
    Sheet2.getRange(LastRow2+1,1).setValue(id);
    Sheet2.getRange(LastRow2+1,2).setValue(name);
    Sheet2.getRange(LastRow2+1,3).setValue(group);
    Sheet2.getRange(LastRow2+1,4).setValue(receive.message.chat.id);
    Sheet2.getRange(LastRow2+1,5).setValue(message);
    if (photo != null){
      Sheet2.getRange(LastRow2+1,6).setValue(photo.id);
    }
  
    //蒐集全部名單
    flag=false;
    for (var i=2;i<=LastRow;i++){
      if (Sheet.getSheetValues(i,2,1,1)==id){
        flag=true;
        break;
      }
    }
    if (flag==false){
      Sheet.getRange(LastRow+1,2).setValue(id);
      Sheet.getRange(LastRow+1,3).setValue(name);
      sndmsg(TriSnakeID,"有新的人傳送訊息給TriangleSnakeBot");
      sndmsg(TriSnakeID,name+":"+message);
    }
  
    //地震警報模組
    if (message=="/eq"){
      flag=false;
      for (var i=2;i<=LastRow;i++){
        if (Sheet.getSheetValues(i,1,1,1)==(id+",")){
          Sheet.getRange(i,1).setValue('');
          flag=true;
          UrlFetchApp.fetch("https://api.telegram.org/bot1908290137:AAFmO6RjCX6XlrRhyIVl-NTKrsZLkCP1QcQ/sendMessage?chat_id="+id+"&text=SUCCESS! 已關閉地震通報功能");
          break;
        }
      }
      if (flag==false){
        for (var i=1;i<=LastRow+1;i++){
          if (Sheet.getSheetValues(i,1,1,1)==''){
            Sheet.getRange(i, 1).setValue(id+',');
            UrlFetchApp.fetch("https://api.telegram.org/bot1908290137:AAFmO6RjCX6XlrRhyIVl-NTKrsZLkCP1QcQ/sendMessage?chat_id="+id+"&text=SUCCESS! 已開啟地震通報功能");
            break;
          }
        }
      }  
        
    }
  
    //對話模組
    var talkid=Sheet.getSheetValues(2,4,1,1);
    if (message=='/talktotrianglesnake'){
      if (talkid==''){
        Sheet.getRange(2,4).setValue(id);
        sndmsg(id,"已建立通道");
        sndmsg(TriSnakeID,name+" 想和你說話，對話通道已開啟:");
      }
      else if (talkid==id){
        Sheet.getRange(2,4).setValue('');
        sndmsg(id,"通道已關閉");
        sndmsg(TriSnakeID,"通道已關閉");
      }
      else{
        sndmsg(id,"很抱歉，有人正在和TriangleSnake對話");
      }
    }
    else if (id==talkid){
      sndmsg(TriSnakeID,message);
    }
    else if (id==TriSnakeID && talkid!=''){
      if (message=='/closetunnel'){
        sndmsg(talkid,"TriangleSnake粗暴的關閉了通道(恐龍咆嘯");
        Sheet.getRange(2,4).setValue('');
        sndmsg(TriSnakeID,"通道已關閉")
      }
      else if (message[0]!='/')sndmsg(talkid,message);
    }
  
    //command
    if (id==TriSnakeID){
      if (message.includes('/talktoall')==true){
        message=message.split(" ")[1];
        for (var i=2;i<LastRow;i++){
          var sndid=Sheet.getSheetValues(i,2,1,1);
          if (sndid=='')break;
          sndmsg(sndid,message);
        }
        sndmsg(TriSnakeID,"已發送全體訊息:"+message)
      }
      else if (message.includes('/opentunnel')){
        message=message.split(" ")[1];
        Sheet.getRange(2,4).setValue(message);
        sndmsg(TriSnakeID,"通道已成功開啟");
        sndmsg(message,"通道已被TriangleSnake開啟")
      }
      else if (message=='/checklist'){
        for (var i=2;i<=LastRow;i++){
          if (Sheet.getRange(i,2).getValue()=='')break
          sndmsg(TriSnakeID,Sheet.getSheetValues(i,3,1,1)+": "+Sheet.getSheetValues(i,2,1,1));
        }
      } 
    }
    else if (commands.indexOf(message)!=-1){
     sndmsg(id,"嘿 衝殺小 你是怎麼發現這個指令的\n這個指令只有TriangleSnake可以用");
     sndmsg(id,"權限不足")
     for (var i=0;i<10;i++){
       sndmsg(id,":(")
     }
     sndmsg(TriSnakeID,name+" 正嘗試使用"+message)
   }
  }