var _year;
var _month;
var _day;
var _functionCallResult;

LoopVeryOut :
for(_year = 99; _year >= 0; _year--){
    for(_month = 12; _month >= 1; _month--){
        for(_day = 31; _day >= 1; _day--){
            trialDate = String(_year).padStart(2,'0') + String(_month).padStart(2,'0') + String(_day).padStart(2,'0')
            _functionCallResult = _0x9a220(trialDate)
            console.log(trialDate)
            
            if(_functionCallResult != "Wrong"){
              console.log(trialDate + ' got successful!!... are you ready to get flag?')
              break LoopVeryOut;
            }
        }
    }
    console.clear()
}
