<font size=４>A telegram bot based on a finite state machine<br />
## <font size=５>1.Setup ##

# <font size=４>Prerequisite #
<font size=３>Python 3.4.0
# <font size=２>Install Dependency #
 <pre> <code> 
<font size=３>py -m pip install transitions==0.5.0<br />
<font size=３>py -m pip install Flask==0.12.1<br />
<font size=３>py -m pip install pygraphviz==1.3.1<br />
<font size=３>py -m pip install python-telegram-bot==5.3.0<br />
</code></pre>
# <font size=４>Secret Data #
<font size=4>**API TOKEN** and **WEBHOOK URL** in app.py MUST be set to proper values. Otherwise, you might not be able to run your code.
# <font size=４>Run Locally #
<font size=３>You can either setup https server or using **ngrok** as a proxy.
<pre> <code><font size=4>ngrok http 5000
</code></pre>
<font size=３>After that, **ngrok **would generate a https URL.<br />
<font size=３>You should set **WEBHOOK URL** (in app.py) to your-https-URL/hook.<br />
# <font size=４>Run the sever #
<pre> <code><font size=4>py app.py
</code></pre>
##　<font size=５>2.Finite State Machine　##<br />
![](https://i.screenshot.net/jrqxlsp)<br />
##　<font size=５>３.Usage　##
<font size=３>The initial state is set to user.

Every time user state is triggered to advance to another state, it will go_back to user state after the bot replies corresponding message.

●user<br />

　○input:"ncku csie"<br />
　　　■reply:"history or professor"<br />
　○input:"test"<br />
　　　■reply:"love or personality or work"<br />
　○input:"chat"<br />
　　　■reply:"Hi!"<br />
　○input:"joke"<br />
　　　■reply:"normal or turbo"<br /><br />

●stateNCKUCSIEIntroduction<br />

　○input:"history"<br />
　　　■reply:NCKU CSIE’s history<br />
　○input:"professor"<br />
　　　■reply:List all professors<br /><br />

●state1~state42<br />

　○input:"1"~"42"<br />
　　　■reply:professor’s　introduction<br /><br />

●statePsychologicalTest<br />

　○input:"love"<br />
　　　■reply:a　psychological　test<br />
　　　　　　(choose an answer and it will go to next state which will show you result)<br />
　○input:"personality"<br />
　　　■reply:a　psychological　test<br />
　　　　　　(choose an answer and it will go to next state which will show you result)<br />
　○input:"work"<br />
　　　■reply:a　psychological　test<br />
　　　　　　(choose an answer and it will go to next state which will show you result)<br /><br />
●stateChat   <br />
　○input:"hi"<br />
　　　■reply:"How are you?"<br /><br />
●stateChat1<br />
　○input:"good"<br />
　　　■reply:"Are you single?"<br /><br />
●stateChat2<br />
　○input:"no"<br />
　　　■reply:"Congratulations!\nhttps://pbs.twimg.com/media/DB4AHDFU0AEu6G4.jpg"<br />
　○input:"yes"<br />
　　　■reply:"Ok~This is for you.\nhttps://youtu.be/WCpKhCyqmFE"<br /><br />
●stateJoke<br />
　○input:"normal"<br />
　　　■reply:show you a joke<br />
　○input:"turbo"<br />
　　　■reply:show you a joke<br /><br />
## <font size=５>Author ##
<font size=３>LGY3030
