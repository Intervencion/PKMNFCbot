// Setup polling way
var bot = new TelegramBot(token, {polling: true});

bot.on('text', function (msg) {
  
  if( msg.text == "/tits")
  
  { 
    
    exec("curl -Ls  \"http://www.hugeboobsbigtits.com/teen-big-tits\" | grep -o \'http[^\"]*.jpg\' > tits.txt");
    
    var rd = readline.createInterface({
    input: fs.createReadStream('tits.txt'),
    output: process.stdout,
    terminal: false
    });
    
    var chatId = msg.chat.id;
    
    rd.on('line', function(line) {
         bot.sendMessage(chatId, line );
    });

    
  }
  else if(msg.text == "/big_tits")
  {
    exec("curl -Ls  \"http://www.hugeboobsbigtits.com/big-natural-tits/\" | grep -o \'http[^\"]*.jpg\' > big.txt");
    
    var rd = readline.createInterface({
    input: fs.createReadStream('big.txt'),
    output: process.stdout,
    terminal: false
    });
    
    var chatId = msg.chat.id;
    
    rd.on('line', function(line) {
         bot.sendMessage(chatId, line );
    });
  }