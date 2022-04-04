function doGet(e) {
  if (typeof e!=="undefined"){
  var recieve=e.parameter;
  var token=recieve.token;
  var SpreadSheet = SpreadsheetApp.openById("1GtMZYKKZetspkvu8fpGm9R05zAKWqhaJP8y0ali9qp0");
  var Sheet = SpreadSheet.getSheetByName("工作表1");
  var LastRow = Sheet.getLastRow();
  var replyMsg='';
  }
  for (var i=2;i<=LastRow;i++){
    replyMsg+=Sheet.getSheetValues(i,1,1,1);
  }
  var area=['tn','ntp']
  for (var i=0;i<area.length;i++){
    if (token=='ss123'+area[i]){
      if (Sheet.getSheetValues(i+2,6,1,1)==''){
        Sheet.getRange(i+2,6).setValue('OK');
        return ContentService.createTextOutput(replyMsg);
        }
      else return ContentService.createTextOutput('-1');
    }
    else if (token=='ss123end'+area[i]) sheet.getRange(i+2,6).setValue('')
  }
  if (token=="ss1231"){
    return ContentService.createTextOutput(SpreadSheet.getSheetByName("工作表2").getSheetValues(SpreadSheet.getSheetByName("工作表2").getLastRow,5,1,1));
  }
  else if (token=="ss1231del"){
    SpreadSheet.getSheetByName("工作表2").getRange(SpreadSheet.getSheetByName("工作表2").getLastRow(),5).setValue('');
  }
  else if (token=="ss123rep"){
    if (Sheet.getSheetValues(4,4)!==''){
      Sheet.getRange(4,4).setValue('OK');
      return ContentService.createTextOutput("OK");
    }
    else return ContentService.createTextOutput("-1");
  }
  else if (token=='ss123repend'){
    Sheet.getRange(4,4).setValue('');
    return ContentService.createTextOutput("OK");
  }
  else {
    return ContentService.createTextOutput("Wrong Token!");
  }
}
