---
title: "Self-Socratic Dialogues"
emoji: "🔮"
pubDate: 22-Jun-2023
updatedDate: 22-Jun-2023
tags: ["topic/technology", "project/104-days"]
---

This note is the **eighth** letter in the [[104-days-of-summer-vacation]] series. You can also follow the full twitter thread [here](https://twitter.com/solderneer/status/1668911213810716672), and leave any thoughts and comments that might come up!

---

**Dearest Reader,**

This letter is backlogged, I am writing this on the 23rd of June, but in my defense, there is incredible joy in getting fully absorbed into making something work. That's what consumed me for the most of yesterday, and I hope that a similar kind of focus state might bless you as well.

Ever since LLMs went mainstream, I've wondered how natural language processing techniques might enable us to interact with our past. As a [quantified self](https://quantifiedself.com/) nerd, and a person who obsesses over personal knowledge management techniques, it would really be incredible to be able to talk to myself as simulated by a LLM.

_Self-socratic dialogues_ as I might call them, dialogues which are arguments and discussions between an embodied, present self and the past self as recorded through personal writings and notes. I briefly mentioned this in [[i-write-for-thought-lego]].

This could be as rudimentary as being able to ask, in natural language, how I felt on a specific day and having that be pulled from my daily notes. Or it could be as advanced as a tool which helps to pull together different streams of thought to compose something original. I've also wanted to integrate something like this into [my website](https://solderneer.me) for a while now, so that visitors can use generative semantic search to ask questions on my written repo of notes.

Which brings me back to the focus state that consumed me yesterday. I stumbled across [txtai](https://github.com/neuml/txtai) which is a neat little python library that enables semantic search workflows, and ended up writing a script to run a basic version of what I envisioned.

<iframe width="560" height="315" src="https://www.youtube.com/embed/NNVnNmH7OLs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The results are, really good actually! It did definitely help surface a lot of thoughts which I didn't even recall having, and it is especially cool that the embeddings and indexing is all done locally at a reasonable pace. The only time an external API call is required, is to invoke the HuggingFace model with the context-enhanced prompt.

And I can clearly see how workflows like this could really empower human agency when done right. My next steps might be to work out how to integrate some of this technology into my workflow in Obsidian. Some thoughts off the top of my head are:

1. Automatic topic classification from a list of topics
2. Suggested "similar notes" for linking based on semantic distance
3. Building generative semantic search into an Obsidian plugin

It's also interesting what parallels might be drawn between self-socratic dialogues and psychological methods like [[internal-family-systems]]. Could self-socratic dialogue also have therapeutic use cases, like the ability to become more self-aware by externalizing your thoughts into an LLM and inspecting them? One of the original names I had for this letters was `semantic-soul-searching` which I thought was quite funny.

Anyway, needless to say, there's lots more to experiment with as the technology slowly gets integrated into stuff we use everyday. [[manufactured-normalcy]] will probably prevail in the end, I can imagine a time where generative semantic search is just going to be everywhere and we take it for granted.

In the meantime, find something to obsess over for a day. I promise it's fun :)

~ Shan