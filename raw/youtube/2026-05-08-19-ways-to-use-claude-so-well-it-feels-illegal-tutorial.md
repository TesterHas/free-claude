---
source: farmer/youtube
farmed: 2026-05-08T14:28:34.643466
channel: "Sabrina Ramonov 🍄"
title: "19 Ways to Use Claude So Well It Feels Illegal (Tutorial)"
url: https://www.youtube.com/watch?v=CmqrlXdQYjk
upload_date: 2026-05-08
duration: 2170
---

# 19 Ways to Use Claude So Well It Feels Illegal (Tutorial)

**Channel:** Sabrina Ramonov 🍄  **URL:** https://www.youtube.com/watch?v=CmqrlXdQYjk  **Uploaded:** 2026-05-08  **Duration:** 36:10

---

## Summary

- /btw — run a side question in the same Claude Code session while a long-running prompt is still executing, without losing context
- /model — switch between Opus, Sonnet, and Haiku per task to match complexity and manage token consumption; use Haiku for simple file ops
- /effort — set reasoning depth (low/medium/high/max) independently of model; pair Sonnet + medium effort as a token-efficient default
- /advisor — configure a fallback model (e.g., Opus 4.7) that Claude auto-escalates to when it is stuck, without manual switching
- ultrathink keyword — append anywhere in a prompt to force best model + max reasoning for that single request, bypassing your default settings
- Context and compaction commands (/compact, /clear, etc.) cut token waste on long sessions; Sabrina demos 19 total Claude Code slash commands and keywords
- Target audience: both Claude beginners and experienced users — video provides a free swipe file of all 19 commands with usage guidance

_Token-saving note for ingest: read this section first. Open the Transcript only if needed._

---

## Key Frames

![[assets/19-ways-to-use-claude-so-well-it-feels-illegal-tutorial-frame-001.jpg]]
![[assets/19-ways-to-use-claude-so-well-it-feels-illegal-tutorial-frame-019.jpg]]
![[assets/19-ways-to-use-claude-so-well-it-feels-illegal-tutorial-frame-036.jpg]]
![[assets/19-ways-to-use-claude-so-well-it-feels-illegal-tutorial-frame-054.jpg]]
![[assets/19-ways-to-use-claude-so-well-it-feels-illegal-tutorial-frame-072.jpg]]

---

## Transcript

--- [00:00:00] ---

I'm going to share with you 19 secret
codes for Claude Code to 10X your
productivity in the next 45 minutes. I
teach AI to millions of people every
month. I hit 30 million views last month
and I've tested all the Claude commands
to find the ones most people have no
idea exist. And these work whether
you're new to Claude or you've been
using it for 2 years. So, if you're
thinking, "I already know how to
prompt." Trust me, the next 45 minutes
will change how you use Claude forever.
I'll explain each code and give you a
free swipe file with all 19 commands and
when to use each one. And don't sleep on
this because 99% of people type basic
prompts into Claude, but the ones who
know these secret codes get 10 times
better outputs in half the time and
don't blow through all of their tokens.
That's why I'll give you everything so
you can skip the trial and error of
testing random commands for hours. So,
without further ado, here are the 19
secret codes for Claude Code. and make
sure to hit like, hit subscribe, and hit
the notification bell so you don't miss
my next training. Number one, /btw. So,

--- [00:01:00] ---

my next training. Number one, /btw. So,
right now, open up Claude Code. And what
you want to do first is type a prompt
that's going to get Claude running for a
long time. So, for example, start with
research, some market or competitor,
like something that you know it's going
to take Claude code 5 minutes to run.
Now the annoying thing is when you start
running it you can't do something else
in that session right like it's thinking
it's doing all of these things but now
with this command you can. So while it's
running this prompt then what you're
going to do is type /btw and you can ask
it any question you want. So you can ask
it what is 2 + 2 and it's going to
answer. So what this code does is it
allows you to continue using cloud even
though it's working on a long running
task. You don't have to start a new
session. You don't have to open another
tab. You can remain within the same
conversation with the same context and
run /btwa
to answer your quick questions while

--- [00:02:01] ---

to answer your quick questions while
it's working on the big task at hand.
And obviously it can answer way more
complicated questions than this. I'm
just trying to illustrate the scenario,
right? Super longunning prompt over
here, super short prompt over here. And
honestly, 99.9% of Cloud users have no
idea that you can do this. This is a
fairly new feature within the past
month. Now, the next set of commands
we're going to talk about, number 2
through 7, are all about managing your
token consumption. So, let's start with
a really basic one, and then it's going
to get like more advanced techniques.
So, number two, /mod. when you type
/model. So go ahead, open up claude.
This will work in Visual Studio Code.
And that basically allows you to choose
the model. So there's a new Opus 4.7,
there's Sonnets, and then there's kind
of the not very sophisticated one,
Haiku. So you can think of these as like
one star, two star, and then this is the
most advanced model over here, three
stars. The reason why this is important

--- [00:03:01] ---

stars. The reason why this is important
is because often times people have their
default setting to be like the most
advanced model which is great by the way
for technical tasks, for complex tasks,
for highly sensitive tasks where you do
not want AI to make any mistakes or
hallucinate. For example, let's say I'm
writing a LinkedIn post for social
media. I really don't need to use Opus
4.7. If you're on a lower tier plan,
it's really important to just like
manage your token consumption. And one
of the easiest ways to do that is just
to switch to one of these lower tier
models depending on the task you have at
hand. If you're just organizing some
local files and renaming them, honestly
like haiku can do that. So that's number
two /model. So go ahead and try that. So
related to the model is this command
called slasheffort. The slasheffort will
basically change the reasoning effort.
So like how hard is it thinking? And
there's four levels to it. It's called
low, medium, high effort, and max
effort. You can choose sonnet. And maybe
you want to do medium reasoning as your

--- [00:04:01] ---

you want to do medium reasoning as your
default. Again, this will help you save
tokens because what reasoning means is
like it'll think multiple turns. Like
number one, here I thought about it
again. Here I reflected on it again.
Here I reflected on it again. If you
choose effort that is lower, then it's
not going to do like so many of these
thinking iterations or terms of
thinking. So usually what you want to do
is like experiment a bit with both model
and effort and choose the one that makes
sense for most of your tasks. You can
set it as the default. I'm going to show
you in the next couple of commands how
you can like escape that default if you
have a task that requires a lot more
thinking, higher accuracy, higher
reasoning. Now we're going to get into
some cooler options which many people
don't know about. Right? These first
three hopefully at least some of you
already know about these. Number four.
So this is a brand new Claude command.
So it's it's secret because nobody
really knows about it or uses it yet.
Brand new. It's called advisor. So type

--- [00:05:02] ---

Brand new. It's called advisor. So type
/advisor. Right now this only works in
claude code terminal. So make sure you
have the terminal open. It's not going
to work if you have Visual Studio Code
yet. So what this does is when claude
needs stronger judgment. So, a complex
decision, you're trying to debug
something that it's really not clear
what's going on. Let's say you have a
problem that Claude keeps kind of
circling around without making any
progress. What advisor will do, it will
escalate this problem to the most
advanced model with max reasoning
effort. And you can actually configure
this. So basically, you can have your
default over here. So let's say your
default is sonnet with medium level
thinking. Okay, efficient token
consumption we're aiming for here. And
then when you do slashadvisor, basically
this will set it up so that if claude
needs that stronger judgment, it's
really struggling, it will automatically
escalate from your default mode to

--- [00:06:02] ---

escalate from your default mode to
what's called the adviser. and the
advisor. It uses additional tokens. It
runs server side, but it gives you kind
of like the benefits of using opus, but
you don't have to turn it on all of the
time. Okay. So, type it. You'll see the
options. Type /dvisor. Claude is going
to ask you like which model do you want
to be your advisor. Okay. So, let's talk
about that. So, I in my opinion, my
preference is to set the most advanced
model as your adviser. Okay? That way
your default can remain something like
sonnet medium effort. This configuration
is how you can get basically near opus
level performance but reducing and
managing your token consumption
efficiently cuz like think about what
it's doing. It's like okay well your
basic task over here I'm just going to
use the default thing. Oh wait I'm like
really stuck on this problem. Let me go
ask opus 4.7 over there. Like that's
what it sets up. And so it's much more

--- [00:07:01] ---

what it sets up. And so it's much more
token efficient. And what's nice is like
it's uh you don't have to switch
manually every single time when you
enable this mode. It's supposed to
switch it to opus 4.7 when Claude
decides that it needs that extra bit of
horsepower, that stronger judgment. So
we covered /mod/effort/advisor.
Okay. Now this one is one of my
favorites. Number five. It's called
ultrathink.
Okay. So, what you're going to do is
type any prompt and then append this
anywhere in your prompt. It can be at
the beginning, it can be at the middle,
it can be at the end. And what you
should see is it should turn into a
rainbow color and you can type it
anywhere. And what it does is it tells
Claude to use the max reasoning effort
and the best model available. So, the
purpose of this is like again, let's say
your default is a lesser model. Let's
say it's sonnet medium effort, but
you're about to run a prompt that you
know is pretty challenging. So let's say

--- [00:08:01] ---

know is pretty challenging. So let's say
it's like fix this bug that is super
broken. Type ultrathink as part of that
prompt and that tells Claude for this
particular prompt I want you to use the
best model available at maximum
reasoning. That way you don't have to
manually change like /mod/effort.
Claude will just know it's going to try
its very best to figure out this problem
and complete your task. So this is what
I used all the time before slashadvisor
came out. Again, slashadvisor is brand
new. Ultrink has been around for a while
now. So that's another way of operating.
So have your default model and effort
lower. And then if you know that a
specific task is really complicated and
requires stronger judgment and planning
capabilities, you just append this
keyword ultraink anywhere in your
prompt. And then number six and seven
also related to context/caveman.
So this is not a pre-built Claude code
skill. This is actually an open-source

--- [00:09:00] ---

skill. This is actually an open-source
skill or plugin that you have to
install. Basically all you need to ask
Claude is like, I want to install the
caveman plugin. It's very well
supported. It has like thousands and
thousands of stars on GitHub, open
source, and its purpose is to cut output
tokens substantially. So when you
actually use it, when you type /caveman,
it's going to reduce like a bunch of
stuff in the output that it thinks is
not necessary context for Claude to
continue performing well. And so, and by
cutting out all of those output tokens,
it just makes it much more efficient to
use Claude because it's cutting that
out. Related to this, this wasn't
originally on my list, but related to
this, I personally use uh this
open-source plugin as well called
context mode. So, you can also tell
Claude, hey, install this context mode
plugin. It will know what to do. And
this one is really useful for reducing
token usage across all of your MCP tool
calls. So, MCP in general is known to be
very like token consumptionheavy. So,
what this will do is basically reduce a

--- [00:10:02] ---

what this will do is basically reduce a
lot of the token consumption with your
MCP tool calls. just ask Claude, hey,
install context mode. The nice thing I
like about context mode is that you
don't have to remember to do anything.
So there's there's actually no code or
command you have to run after you
install it and you give it permission.
Like it just works in the background. So
this is another one that I really like.
But if you're on the lower tier plan, I
recommend using both of them, right?
/caveman as well as context mode. So
number seven is called slash context. I
think this is the last secret code
related to token consumption. And this
basically will visualize your current
context usage as a colored grid. So it's
literally like kind of looks like this.
So like let's say this is how much
context usage you're allowed and then
like this will be a different color
based on what you're actually using it
for like this. So it's cute though. So
run it right now. I don't think this
works in Visual Studio Code. I think
this is only terminal at this point, but

--- [00:11:01] ---

this is only terminal at this point, but
it'll also break down like what is your
estimated usage by category. So your
categories are like prompts, tools,
memory skills, memory files, like
there's a couple other categories as
well, but you'll see the breakdown per
category so you can like better optimize
what's happening. And then it'll also
show you optimization suggestions. So if
you are running like pretty close to the
limit, it'll show you optimization
suggestions for things that are taking a
lot of context. If specific tools are
taking a lot of context, like maybe you
want to reevaluate using those tools, if
it's memory bloat, if you have capacity
warnings, you'll see that here as well.
So go ahead and run this. It's actually
just like a really cool visual grid, and
it will give you a better sense of like
where are you actually burning all of
your tokens. Okay, so number eight is
also related to context, but it's also
generally useful. So slashclear. So I
use this all the time, especially when I
switch between tasks. So what this does

--- [00:12:01] ---

switch between tasks. So what this does
is, you know how you have like a really
long clawed conversation. When I'm done
with a task, I run slashcle and it
removes all of this previous context in
the conversation. The reason this is
useful, obviously reducing token
consumption, then for each new prompt
you run, Claude does not have to like
pass back and forth all of this
irrelevance context from past
conversations. But the other reason it's
useful is to ensure high accuracy and
quality. A known problem with LLMs is
like when you feed it like a ton of
context, especially context that's not
even relevant. Like let's say you're
jumping between tasks that already done.
When you fill up all of that context,
the answers degrade in quality. So, this
solves two problems. And I use this all
the time. Like, whenever I'm done with
one thing and I'm going to switch to
another thing, I just do slash clear.
So, a lot of people don't run this, but
I run it frequently, multiple times in
the same session, many times a day.

--- [00:13:00] ---

the same session, many times a day.
Okay? So, just get in the habit of using
this. The next two we're going to talk
about are related to improving the
quality of your experience with cloud
code. Improving the skills you have,
improving how you're using cloud code,
identifying where you're using cloud
code poorly and how you could be using
it better. Number nine is slashinsights.
And this is only available through the
terminal right now. So if you have cloud
code terminal open, which I encourage
you to do to actually try these
commands, type /insits. It's gonna take
a while. So like either let it be on its
own session or you can use slashbtw
right number one on our talk today. But
yeah, go ahead and run this. Basically
cloud will analyze all of your sessions
from the past 30 days or so and suggest
how to be more productive using cloud
code. Like it will literally tell you
here's where you're doing a really good
job using cloud code. Here's what's
holding you back. Here are some quick
wins you should try. Here are some
skills you should create. Here are some

--- [00:14:00] ---

skills you should create. Here are some
features in cloud code you don't know
about that you should probably try
because based on your usage pattern like
we notice these are your use cases so
these features make the most sense for
you to try. So go ahead and run that
again. I believe it's about 30 days and
it's almost kind of like a report card.
you're going to get like this cool super
detailed report card with charts and all
of this stuff and it's a way to like
evaluate on your own usage of AI tools
and literally AI Claude is telling you
here's how you could use me better.
Okay, number 10 is super super cool.
This is like one of my favorite things
now. It's called Skill Creator. Now this
does not come out of the box in either
Claude Code or Co-work. So, in co-work,
I think you have to go to like customize
and then either plugins or skills and
you have to look for the pre-built
anthropic skill called skill creator.
You have to like add it to your
co-workspace and then make sure it's
toggled enabled on. If you ever want to
create a skill without it, you can just

--- [00:15:00] ---

create a skill without it, you can just
toggle it off in your customize
settings. For cloud code, you will have
to install it from the plug-in
marketplace. So you can tell Claude to
do it, but I can also tell you the
command. So just do /plugin marketplace
addthropics/cloud-plugins-official.
Just tell Claude to install it for you.
So that will add the plugin for the
marketplace. And then the next command
is /pluginstall
skill creator at anthropic. Go ahead and
do that. The reason this skill is super
cool, it's kind of like a meta skill
that creates really high quality skills
for you. So, it walks you through the
process of creating skills, testing, and
improving your own skills. It's it's a
skill that builds amazing skills. And
there are a couple reasons why like it's
pretty unique and powerful compared to
not using it. So, it's not just about
creating the skillmd file. It also
creates what are known as eval. This is

--- [00:16:00] ---

creates what are known as eval. This is
like shorthand nickname for evaluations.
You can kind of think of it like a
grading rubric. So let's say I have a
skill and then I want to know like how
well is that skill working. So we have
like a grading rubric and maybe it
scored 80% on that grading rubric. But
it keeps track of this over time. So
like when you make changes to the skill,
it will evaluate it again and then
decide did your changes improve the
quality of the skill based on this
grading rubric or not, right? Cuz like
cuz to this date, you know, you change
your skill and it's like did it get
better? I hope so. Like that's that's a
pretty normal way of doing things. But
now with skill creator, you can actually
have like very structured eval. So every
time you change a skill, it will run the
evals, grade it, and make sure your
changes improve the skill and didn't
degrade it. There's even a benchmark
mode. Okay, I don't use this one as
much, but there's a benchmark mode that

--- [00:17:01] ---

much, but there's a benchmark mode that
will run your skill multiple times and
measure variance across the results. So
like maybe normal people change skill,
run the skill once, output looks good,
hey, it works. A more scientific robust
approach would be like you run the skill
10 times and then measure the output 10
times and make sure it worked like nine
out of 10 times or 10 out of 10 times.
That's what the benchmarking is for. And
number three, it has an improve mode. So
it will like analyze the results of the
benchmark. So let's say we run the
benchmark and it got like seven out of
10 correct. It will analyze like hey
what went wrong? and then try to refine
improve the skill so that it will score
higher next time. Now, I don't think you
need to use skill creator for like every
possible skill. like it kind of could be
overkill, especially if you have things
that aren't like clearly measurable, but
I encourage everybody to go through the

--- [00:18:01] ---

I encourage everybody to go through the
process of using it because it really
teaches you how to think systematically
about building skills that are
highquality, robust, that work in like
multiple cases, not just like try it
once and hope for the best. It just
gives you that like framework and
mindsets that is really useful. Okay, so
number 11. So this is new as well. It's
called /team onboarding. This should
come out of the box with cloud code. So
you shouldn't have to install a separate
plugin, but this only works in cloud
code terminal right now, not Visual
Studio Code. And what's really cool
about this is it'll basically create a
team onboarding guide based on your
project and your sessions and stuff,
your cloud code usage history. It'll
analyze like the commands you've been
running in the project, what MCP tools
that you've been using from the past 30
days, and it'll produce a file that a
teammate can copy and paste into Claude
as their first message, and it will
basically onboard them onto the project.

--- [00:19:01] ---

basically onboard them onto the project.
Let's say you have a project that
creates all of your content. So, I have
one that's called like content empire
project. It's committed to GitHub. It's
its own repo project and everything. And
so like I would run team onboarding. And
if I had a team for all my shorts and
content, then they would get like this
nice little guide that they could copy
and paste as their first message into
Claude. And Claude is going to basically
like explain everything about the
project. What are the most useful MCPs
you should set up? What are the most
useful commands to run, etc. And that's
the key part here. That's like the
differentiator. Like obviously you can
have Claude write an onboarding doc
based on what's in your project. like,
hey, here's how the files are
structured. Here's like what this does.
But the most important thing is like,
how do I actually use this project?
Like, how am I using all of these
YouTube skills for research and
outlining and writing and hooks? And I
think this is a top of- mind concern

--- [00:20:00] ---

think this is a top of- mind concern
because like a lot of people are
struggling to figure out how to use
Claude in a collaborative setting. So if
you are doing like cloud training, cloud
consulting, this might be like a really
good one to focus on because there's so
many questions like how do I use cloud
productively within a team setting. So
the next two I'm going to talk about are
related to scheduling tasks. Like you
know it's nice you can go go to cloud
code and have it do something, but what
if you want it do like a recurring
report, a scheduled summary, a recurring
automation? Like how do you do that in
cloud code? Honestly, currently it's way
easier to do that in cloud core. That is
one of the areas where I think co-work
is superior is scheduling and also
visuals like artifacts and stuff like
that but you can kind of start to do it
within cloud code. Okay, so this command
is called slash loop. Okay, so go ahead
and type that like let's try a real
command. So type like /loop 5 minutes
and then whatever other skill you have.
So I don't know what your skills are but

--- [00:21:00] ---

So I don't know what your skills are but
like replace this third thing with a
skill you actually have. So what this is
saying is Claude every five minutes
that's this interval run this skill
slash write post. It doesn't have to be
a skill by the way. You can just like
replace this with any prompt or task. So
maybe that's easier. But yeah, go ahead
and type this into cloud code. And what
this will do is it'll create a repeating
task that runs every 5 minutes in your
current session. Okay, so that's really
important to note. So, it's your current
session, which means your laptop has to
be on. The session has to be alive.
Like, you can't close the session. It's
scoped to your session. So, if you open
a new session, it's not going to know
about what's happening over here. The
minimum interval I believe is 1 minute.
And unfortunately, loops expire after 3
days. Okay. So, this isn't really meant
for longunning things like every single
day for the next year. like an email

--- [00:22:00] ---

day for the next year. like an email
summary would be the second category.
Okay, but this is nice for like kind of
these little tasks that are confined to
a single session while your laptop's
running. So like let's say you're like
doing some other stuff and you're
polling for something to be done. Like
check every 1 minute that my V3 video is
done cuz like if you're generating
really high quality videos, it can take
10 minutes for the video to complete. So
like you could pull and check until it's
done. Okay, so that's one option for
scheduling. But again, the downside is
loops expire after 3 days and it's
session scoped. So if you close the
session, the loop dies, right? Okay. So
number 13 is another option that's
better for like scheduled reporting,
scheduled summaries, and it's literally
called slash schedule. So go ahead and
type that into cloud code, and you
should see it. It's a fairly new
feature, I think just within the past
month. And this basically will run
independently on the cloud somewhere. So

--- [00:23:01] ---

independently on the cloud somewhere. So
this is cloud. Okay. So instead of
running locally on your computer, it's
going to run on the cloud. The nice
thing about this is you don't have to
worry about your computer being on. You
don't have to worry about your session
being active. Okay? It what it will do
is it will basically create a remote
chrome or cron trigger that runs
independently over here in the cloud.
Now the downside of this is it does not
have access to your local files.
Basically cloud code in the cloud will
clone your project over here. So it will
clone it to this cloud and then run the
scheduled task. So it's not going to
have local file system access but it can
still be useful for a lot of things like
daily summaries, recurring automations,
scheduled reports, etc. There are
limitations though. So, to the best of
my knowledge, as of today, there's like
the number of times you can run a
scheduled task per day is capped. So, I
believe it's five for the pro plan, 15

--- [00:24:01] ---

believe it's five for the pro plan, 15
for the max plan, and like 25 or so for
the team or enterprise plan, but you can
check that in the cloud documentation.
The minimum interval is 1 hour, right?
So, for loop, remember minimum interval
was 1 minute. You can literally create a
loop thing that runs every single
minute. for the schedule the minimum is
1 hour. So here's an example if you want
to try it. So slash schedule let's see 9
star 15 and then let's make this like a
research task or research like AI news
or something something simple like this.
You can type like any variation of this.
So SLC schedule09
star star one-5 research trending AI
news or whatever. So basically every
weekday at 9:00 a.m. week, this is the
weekday part here. I'm not great with
interpreting cron jobs, but 1 to 5 means
weekday 9 is not 9:00 a.m. So every
weekday at 9:00 a.m. a cloud-based cloud

--- [00:25:01] ---

weekday at 9:00 a.m. a cloud-based cloud
code agent will run automatically and
research AI news. Okay, so like this is
an example of what you can do. Yeah, the
next three commands I'm going to focus
on are all about continuity. like, "Oh,
we're using Claude Code, but I I'm
leaving or like I'm going on vacation or
I'm going to a dentist appointment. Can
I still use cloud code somehow?" And the
good news is now you can. So, type slash
remote-control.
Another shortcut for this is, by the
way, /rc. And this basically allows you
to sync your phone with cloud code on
your computer. Okay. So, let's say this
is a laptop. Cool. And now they are like
synced. So Cloud Code is actually
running on your computer. It still has
access to all of your local files and
everything on your computer. But when
you turn remote control mode on, okay,
what you're going to do is on your
phone, download the Claude app. Okay,
when you do that, open the Claude app.
On the left sidebar, click code. Okay,
and then you're going to see your Claude

--- [00:26:00] ---

and then you're going to see your Claude
code sessions that are available.
Usually the active ones will be at the
top. So just look for it at the top. And
now you can type anything on your phone
like, "Hey, go organize all the files in
my downloads folder." Okay, so you're
typing it from your phone over here, but
it's actually executing on your laptop
over here. Let's say you're doing stuff
on your laptop, but you have to go to a
dentist appointment. Okay, so you start
it / RC or SL remote control. And then
from your phone, you could be like, "Oh
yeah, continue doing this." You get
permission notifications as well, like
always allow allow once. You can just
click it from your phone. So it's just a
nice way to have a continuous cloud code
session even if you are no longer
present at your computer. The only thing
is your computer has to be on. So it has
to be on. So how do you keep it on? So
there are tools like amphetamine but
yeah there are like Mac apps for example
like amphetamine which you can just tell
it how long do you want your computer to
be on. So one common thing I'll do is
like oh I got a cloud code session

--- [00:27:01] ---

like oh I got a cloud code session
running but I'm going to go to the gym
and shower now. So, I'll just do / RC,
right? Put empetamine on maybe like 2
hours cuz that's like roughly how long
it takes for me to work out and shower.
And then, you know, in between sets or
like after I shower, I'll just be like,
"Oh, is it stuck on anything or should I
run another prompt?" And so, that's an
easy way to do that. And if you're on
Windows, I'm sure there's like a similar
analog to this or maybe you could do it
natively in Windows or whatever. But,
this is just a really nice Mac app and
it's free, right? I just choose how many
hours that I want to leave my computer
on. Okay, so related to remote control,
the next two are kind of related to
this. So 15 slash rename and it is
exactly what it sounds. So let's say you
have like multiple cloud code sessions.
Now you can actually rename each one.
And to be honest, I never used this
feature until I started using remote
control cuz what happens is you open up
cloud code sessions on your phone and
you have like no idea which one is
which. It's like confusing. So this is
really handy. So if I know I'm going to

--- [00:28:00] ---

really handy. So if I know I'm going to
be using remote control, I will do
slashreame to rename the session so that
when I'm in my phone, I can like
understand oh like this session is was
making a YouTube script. This other
session was like trying to fix a bug in
my code. And then related to that, this
one I do use outside of remote control
slash resume. It's exactly what it
sounds. So basically you continue a
previous session. So for example, I have
like multiple computers and devices. cuz
I have like my Mac Studio down here to
my left. I have a laptop. When the
weather is nice, I just like to sit on
my patio with my laptop and then I have
my phone, right? So, let's say I'm
working on a YouTube script on my
desktop over here. This is my basement.
And I'm like, "Oh, the sun came out. I
want to go sit on my patio." So, then
I'll open cloud code in my laptop.
Again, this is supposed to be a laptop.
And be like slashres so that I can just
continue the conversation I was having
over here. and I can continue it on my
laptop. Okay, so number 17 is the Claude
Chrome extension. So to install this,

--- [00:29:02] ---

Chrome extension. So to install this,
open Google and type Claude Chrome
extension and the first result should be
the official Anthropic Chrome extension.
So go ahead and click install it. Then
you'll be prompted to log in. Then on
your browser, there will be like kind of
like an orange star icon on the top
right. So you can always open the Claude
Chrome extension. And basically how to
think about it is it gives Claude access
to the browser. So whatever you can do
on the browser, Claude can do as well.
For example, it can go to a website. It
can click around on stuff. It can scroll
up and down. It can type stuff like it
can handle a lot of different browser
automation. If you're using it in cloud
code, I believe you still have to run
this claude- chrome. Okay, so let's say
you're in your terminal. So run this
claude- chrome and it will open a
session of cloud code with Chrome
enabled. I think now you can toggle it
on during a session, but for a long time
you had to launch it this way and then
to actually run it, you can just run a
prompt like go to whatever website, say

--- [00:30:00] ---

prompt like go to whatever website, say
go to blot.com and I don't know, click
around or something. Honestly, it could
be anything. Go to facebook.com and like
like a comment, like a post. So you can
talk to Claude code and then it will
interpret your task. So if it thinks,
oh, I need to navigate to the browser
with Claude Chrome to accomplish this
task. Then it's going to open the
browser. You're going to see it
visually. It's going to like open a
browser. It's going to be like
highlighted orange and stuff. And then
it's going to start interacting with the
web page. It's going to like click
around. It's going to type stuff, etc.
And so this is really really nice
because now you can just tell Claude to
like go to websites that don't have APIs
and like automate different browser
tasks. You do want to be careful, right?
Don't do things like automate Tik Tok
comments. You will be shadowbanned for
that. So, don't do that. But it can do a
lot of things. So, for example, I have a
free school community. I can tell cloud
code like oh like analyze everything on
the calendar and create a nice email
update cuz for some reason school

--- [00:31:00] ---

update cuz for some reason school
doesn't have an API to do that easily.
So, think like websites that don't have
an API that don't have an easy way to
programmatically interface with them.
you can use the claude chrome extension
so that you just make claude do it. Now
some people will say but playright mcp
is like a much better alternative and I
don't disagree. So like if you are a
little bit more advanced and you know
how to install MCP servers I personally
almost always prefer playwright MCP if
I'm using it within cloud code but this
is like a really great starting point
for everybody else who has no idea what
this means. One way I like to use the
cloud chrome extension, especially if
you are technical developing an app.
Let's say we implemented a new feature.
Okay, now like go test it until it
works. Say something like don't stop
until feature works as intended on the
front end. So let's just say you built
like a web app and users are supposed to
be able to sign in and then click a
button or something to start your app.
You can tell Claude to do that. Like,
hey Claude, build this app. Don't stop

--- [00:32:02] ---

hey Claude, build this app. Don't stop
until the user can sign in, fill out
this form, push this button, and do this
thing. And Claude will code the app.
Then it will launch your app in the
browser to test it. It will go through
each step like the registration, click
the button, start the app, and it can
visually see like what's going on and
what needs to be fixed. It's basically
the concept of setting up a feedback
loop for your AI agent. And so by
installing a Chrome extension, you're
giving Cloud the ability to literally
see your app and test your app so that
it can just keep working on it until it
works as intended. Okay, number 18. I
don't use this one as much as I probably
should, but I think a lot of you will
find this super helpful. It's basically
what it sounds like. So you can rewind
the conversation to a previous point in
time. Like you can literally rewind to a
selected message. So, type this right
now in Claude Code. I'm not sure this
works in Visual Studio Code. I'm not
sure. This may be limited to terminal

--- [00:33:00] ---

sure. This may be limited to terminal
only. I'm not sure. But basically,
you'll see a popup like this when you
run it. And it'll be like, here's your
all of your messages over here. Which
points would you like to rewind to?
Right? So, if it's like kind of like a
timeline over here, we're over here. And
then you have all these past messages
that you made, you can select the
message and go back and start over here.
So, let's say like your conversation was
going really well up until this point
and then things just did not go well
after that. I'm sure many of us can
relate. So, what you can do is type
rewind, choose this message and it's
just going to rewind it to that point in
time. And it's just like a really nice
shortcut especially if you're not
technical and you know GitHub confuses
you, you don't do branching and things
like that. This is just really nice.
It's kind of like time travel movies. So
you go back in time and then it creates
this new branch, this new universe. So
we have universe number one over here,
universe number two over here. And in
this universe, obviously everything goes

--- [00:34:01] ---

this universe, obviously everything goes
well. Or maybe it doesn't. You messed
everything up again. And then you want
to rewind again. Let's rewind over here.
And then so you create like another
universe. Oh, over here. So this is now
universe 3 where everything actually
goes well and happy ending. This one you
may have heard about on social media. A
lot of influencers like to post about it
because it's visual. So it's called
slash status line. So you know when
you're using cloud code, there's like a
little bar at the bottom. Oh, I'll try
to draw it. I will butcher it. Right. So
this is like where you would type your
input. Right over here, I'd type
something over here. And then there's
stuff below it, but it's often not super
useful. So status line allows you to
customize this stuff below where you
type, right? So this is like the
blinking cursor. That's where you type.
So you can do things like monitoring
your context window usage, tracking your
session costs, right? If you are working
across multiple sessions or want to
visually differentiate between them, you
can do that. If you want your git branch

--- [00:35:01] ---

can do that. If you want your git branch
and status always visible, you can do
that. So the status line is like below
where you would type. So let's say like
this is a folder. So my folder is called
/contents and then my git branch is like
feature slash I don't know YouTube
script writing and then even below that
you can have like a progress bar like
this like 42% usage or something like
that. This is your cost so far for the
session and you can even do like timers
like here's how long like something's
been running. So just check out what the
options are for what you can put in. But
yeah, basically you can show like what
your project is, what your git branch
is, your context window usage, cost for
the session so far, how long the session
has been running and things like that.
You can customize it many different
ways. So just run / status line and then
you'll see what the options are. I think
this is also only available in the
terminal. I don't think this is
available in Visual Studio Code, but

--- [00:36:00] ---

available in Visual Studio Code, but
like that changes. So just depending on
when you're watching this video. Yeah,
if you enjoyed this content, hit like,
hit subscribe, and hit the notification
bell so you don't miss my next training.
