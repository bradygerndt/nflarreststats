
var tabletojson = require('tabletojson');
var json2csv = require('json2csv');
var sleep = require('sleep');
var fs = require('fs');
var promises = [];
var teams = ['crd', 'nwe', 'buf', 'mia', 'nyj', 'pit', 'rav', 'cin', 'cle', 'oti', 'jax', 'htx', 'clt', 'kan', 'rai', 'sdg', 'den', 'phi', 'dal', 'was', 'nyg', 'min', 'gnb', 'det', 'chi', 'nor', 'car', 'atl', 'tam', 'ram', 'sea', 'sfo']
for(let year = 2000; year <=2013; year++){
    
  for(let i in teams )
  {
    sleep.msleep(500)

    //var url = 'http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year +'&seasonType=REG&experience=&Submit=Go&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=QUARTERBACK&qualified=true' //qb
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p +'&conference=null&statisticPositionCategory=RUNNING_BACK&qualified=true' //runningback
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=WIDE_RECEIVER&qualified=true'// Wide receiver 
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&experience=&Submit=Go&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=TIGHT_END&qualified=true'  // tight end
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p='+ p+'&statisticPositionCategory=DEFENSIVE_LINEMAN&qualified=true' //d line
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=LINEBACKER&qualified=true'  //linebacker
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=DEFENSIVE_BACK&qualified=true'  //D back
    // var url ='http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticPositionCategory=KICKOFF_KICKER&season='+ year+'&seasonType=REG&experience=&tabSeq=1&qualified=true&Submit=Go' // Kickoff kicker
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=KICK_RETURNER&qualified=true' // kickoff returner 
    // var url ='http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticPositionCategory=PUNTER&season='+ year+'&seasonType=REG&experience=&tabSeq=1&qualified=true&Submit=Go' //punter
    // var url ='http://www.nfl.com/stats/categorystats?tabSeq=1&season='+ year+'&seasonType=REG&Submit=Go&experience=&archive=false&d-447263-p='+ p+'&conference=null&statisticPositionCategory=PUNT_RETURNER&qualified=true' // punt returner 
    // var url ='http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticPositionCategory=FIELD_GOAL_KICKER&season='+ year+'&seasonType=REG&experience=&tabSeq=1&qualified=true&Submit=Go' // kicker
    var url = 'https://widgets.sports-reference.com/wg.fcgi?css=1&site=pfr&url=%2Fteams%2F'+ teams[i] +'%2F'+ year +'_roster.htm&div=div_games_played_team'

    console.log(url)
    tabletojson.convertUrl(url)
    .then(function(tablesAsJson) {
      //console.log(tablesAsJson)
      var standardAndPoorCreditRatings = tablesAsJson[0];
      //console.log(standardAndPoorCreditRatings);
      json2csv({ data: standardAndPoorCreditRatings}, function(err, data) {  

                var players = data.split('\n')

                players.map((player)=>{
                  var playr= player+',"' + year + '","' + teams[i]+'"';
                  changedPlayer.push(playr);
                });

                outfile = "./TeamRoster/"+teams[i]+".csv"
                  fs.appendFile(outfile,changedPlayer.join('\n'), function(err) {
                  if(err) {
                    return console.log(err);
                  }
  
                  console.log("The file was saved!");
                });
      });
    });
  }
}

