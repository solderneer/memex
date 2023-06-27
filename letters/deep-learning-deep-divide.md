---
title: "The Deep Divide in Deep Learning"
description: "iS ChAtGpT cAPaBle oF ReaSOn?"
emoji: "🧠"
pubDate: "Mar 29 2023"
updatedDate: "Mar 29 2023"
tags: ["topic/technology"]
---

It took ChatGPT just two months to reach a hundred million global active users. For reference, TikTok took nine months and Instagram took a comparative eternity of two and a half years [^1] . The age of widespread artificial intelligence (AI) is not a distant future, it has arrived and is growing at record pace. This growth is primarily driven by deep learning companies like OpenAI and DeepMind who deliver improvements to their models on the timescale of months rather than years. The whole scene is reminiscent of the early dot-com companies where every week brings new technological leaps, prompting the CEO of OpenAI, Sam Altman, to respond with grandeur visions of a post-AI civilisation [^2] .

But some researchers call for pause. In _"Deep Learning is hitting a wall"_ [^3], Gary Marcus criticises contemporary AI research for not making meaningful progress. Specifically, he believes that the use of deep learning in AI has shown diminishing returns with regards to what he terms _"genuine comprehension"_. Namely, **the lack of interpretability, reasoning, safety and scalability** in many black-box neural networks are dealbreakers to Gary's mental model of intelligence and he echoes these themes throughout his written work [^3] [^4] [^5] .

Instead, Gary posits that funding and attention be redirected to an earlier AI architecture, known as symbolic AI, which when combined with the deep learning (connectionist) approach could yield better performance. This hybrid approach is also called _neurosymbolic AI_ [^6] and it is the architecture that Gary is a fierce advocate for. This essay offers an account of his arguments and shows that neurosymbolic AI might happen a lot quicker but in a radically different way from what Gary believes.

## Symbolic vs Connectionist AI

Before diving into Gary's arguments, it is helpful to outline the difference between symbolic and connectionist AI. The theory of cognition has long rested on the opposing views of nativism and empiricism [^7] . Nativists such as Steven Pinker [^8] hold that cognition is innate and derives from pre-programmed logic and mechanisms, while empiricists like John Locke [^8] deny this and claim that all knowledge is learnt from experience.

Similarly, symbolic AI takes a nativist approach by relying on formal logic and the manipulation of symbols according to pre-programmed rules. In contrast, connectionist AI forgoes pre-programmed rules for statistical equations and relies on data (experience) to learn solutions to problems [^9] .

Popular deep learning models today are connectionist, requiring a massive dataset to learn responses to a problem. They are able to automatically extract features and be applied across various domains, avoiding the intractability of symbolically modelling features even in simple problems. However, connectionist AI suffers from a lack of reasoning and interpretability, unlike symbolic models they do not follow deterministic and legible rules which humans can verify. In short, deep learning and other connectionist AI architectures typically trade off human interpretability for greater accuracy: they are black boxes.

It is this lack of reasoning and interpretability that compels Gary to suggest that deep learning models do not have genuine understanding.

## Interpretability, Reasoning and Safety

**Interpretability** is the ability to introspect an AI model and work out _why_ it made a specific decision. In mission critical applications, like self-driving cars and radiology, knowing why a model acted in a certain way is important to verify its behaviour. This is also related to **reasoning**, which is the ability of a model to procedurally solve multi-step problems using a logical approach.

Gary highlights that connectionist AI models have difficulty explaining their own decisions, and struggle to generalize consistently beyond their training dataset. He illustrates this using Tesla's "Full Self Driving Mode", where the car's vision system was unable to recognize a man holding a stop sign [^10] . He also shows evidence of GPT-3's inability to reason when provided with common-sense situations, calling it a _"fluent spouter of bullshit"_ [^5] .

Connectionist models are tuned to the data that they are trained on, and learn facts about that data moreso than the world. This problem is called _overfitting_ where a model struggles to generalize and it is hard to anticipate how and in which outlier situations it might fail [^11] . Especially in large models like GPT-3, Gary reminds us to distinguish between robust reasoning and interpolation from a large dataset. Indeed, when language models were trained to solve numerical reasoning tasks, there was significant correlation between numerical term frequencies in the pretraining dataset and model accuracy when presented with that term which raises questions about the model's ability to reason and generalize [^12] .

Although as discussed prior, symbolic AI provides more robust interpretability and reasoning, interpretable AI might not be the panacea Gary makes them to be. Quantifying the interpretability of a model is difficult, and at times accuracy is preferable to transparency [^14] . Taking Gary's example, one could argue that as long as Tesla's self-driving car was empirically more accurate than humans, its interpretability is irrelevant.

With regards to reasoning, one of Gary's own sources [^13] points out that _"large language models are made to say the first thing that comes to mind"_. Gary's anecdotal evidence of GPT-3's shortcomings [^5] might be trivially overcome by enabling large-language models (LLMs) to have inner dialogue and deliberation. Already, adding the zero-shot chain-of-thought prompt _"Let's think step by step"_ dramatically boosts LLM performance on a range of reasoning tasks [^15] .

The concern of **safety** is another roadblock for connectionist models: the widespread use of LLMs have raised concerns around minimizing model toxicity and aligning them to human values. On this, Gary highlights DeepMind's report on the matter [^16] and Timnit Gebru's paper calling LLMs "stochastic parrots" [^17], and specifically bemoans the lack of strategies to stop LLMs from reccommending self harm [^3].

Gary's examples for safety is limited to LLMs, but in his defence, LLMs are likely the first widespread AI tool for which values alignment is an issue. OpenAI's latest answer to that, Reinforcement Learning with Human Feedback (RLHF) [^18] , leaves much to be desired with its outlier failure modes such as _how it reveals nuclear secrets if prompted with uWu furry-speak_ [^19].

Even for symbolic AI, it is difficult to define what safety is, as human values are inherently subjective. This means that AI risk mitigation must take on a broad-based socio-technical approach, as outlined by DeepMind's report [^16] .

## Scaling and Metrics

The connectionist approach to the problems outlined above is to collect more data. In the article, Gary refers to the original 2020 OpenAI paper on empirical scaling laws [^20] which concluded that larger models fed with moderate amount of data performed better. Since then, a 2022 paper from OpenAI has reclarified that model size and dataset size should be scaled equally [^21] , showing that the 2020 paper resulted in undertrained LLMs and further cementing the importance of data for LLM training.

However Gary refutes this approach, saying that the measures that were used to quantify the performance of these models did not adequately reflect _"genuine comprehension"_, by the definition he has already outlined. To back his claim he cites DeepMind's work on scaling Gopher [^22] , and Google's work on LaMDa [^23] : both of which are GPT-like models and find that scaling improves coherence but not reasoning or safety. Gary also notes that the scaling law is purely empirical, even the original paper highlights the lack of a theoretical explanation for it [^20] , and therefore is unreliable in nature.

Although there are valid concerns about continual investment into scaling, latest reports by OpenAI remain promising. Recently, GPT-4's release was accompanies by benchmarks using AP, SAT and other standardized tests, achieving the 80% percentile on most exams **without special training** [^24] . Gary might take issue with model performance measures, but it would certainly be iconoclastic to suggest standardized tests were not measures of genuine comprehension.

## Hybrid AI

Given the aformentioned issues with interpretability, reasoning, safety and scaling, Gary concludes with support for the fusion of symbolic and connectionist paradigms. To him, the hybrid model could bring together the benefits of both architectures [^6] , and he points to the successes of hybrid models in NetHack [^25], Go [^26], and even protein folding [^27] as signposts for his view. Gary also briefly outlines the rivalry between the symbolic and connectionist AI researchers [^28] , criticising deep learning pioneer Geoff Hinton for dismissing and encouraging the move of research investments away from symbolic AI [^29].

The issue with Gary's argument is that all his examples consist of structured and well-defined problems, with (relatively) easily modelled symbolic relations. This is much harder for "open-world" situations with less legible rules like language or even the African savannah that humanity's ancestors used to inhabit.

Daniel Kahneman refers to two modes of thought: System 1 which is fast, automatic, instinctive and System 2 which is slow, logical and deliberative [^30] . In evolutionary terms, most animals have System 1 but only intelligent animals appear to have System 2, suggesting that System 2 emerges from System 1.

In AI, the stochastic nature of connectionist models approximates System 1 while symbolic models approximate System 2. It is possible that just like in animals, logical reasoning is simply abstraction over the complex sequence learning of connectionist models. Similarly, Goeff Hinton believes that the prediction of _"thought vectors"_ from previous _"thought vectors"_ could capture all of human reasoning without the need for any symbolic AI [^31] .

## Conclusion

Today, with the breakneck pace of AI research, the wall that Gary describes is hard to see. Even with their shortcomings, the capacity of models like GPT-4 to answer complex queries is stunning, and raises questions about the relationship between complex sequence learners and intelligence [^13] .

At the same time, Gary's vision for hybrid AI manifests in an unexpected way, with ChatGPT enabling plugins with Wolfram Alpha and other tools [^32] , allowing the model to lean on symbolic approaches for reasoning tasks. Even without neurosymbolic AI, the ability of LLMs to write and understand natural language enables them to serve as universal interfaces to tools which extend their capabilities.

While Gary's request for openness towards hybrid approaches is well-justified, his claim that deep learning models are overstating their successes appears to unfairly move the goalposts for AI [^33] . The surprising effectiveness of deep learning models across a wide range of problems is impressive and likely revolutionary. Let them enjoy their victory.

---

# References

[^1]: https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/
[^2]: https://moores.samaltman.com/
[^3]: https://nautil.us/deep-learning-is-hitting-a-wall-238440/
[^4]: https://thegradient.pub/gpt2-and-the-nature-of-intelligence/
[^5]: https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/
[^6]: https://www.cs.utexas.edu/~swarat/pubs/PGL-049-Plain.pdf
[^7]: https://plato.stanford.edu/entries/innateness-cognition/
[^8]: https://en.wikipedia.org/wiki/How_the_Mind_Works
[^9]: https://towardsdatascience.com/symbolic-vs-subsymbolic-ai-paradigms-for-ai-explainability-6e3982c6948a
[^10]: https://youtu.be/RVkLI9pPd24?t=166
[^11]: https://nautil.us/is-artificial-intelligence-permanently-inscrutable-236088/
[^12]: https://arxiv.org/pdf/2202.07206.pdf
[^13]: https://medium.com/@blaisea/do-large-language-models-understand-us-6f881d6d8e75
[^14]: https://arxiv.org/pdf/1606.03490.pdf
[^15]: https://arxiv.org/pdf/2205.11916.pdf
[^16]: https://arxiv.org/abs/2112.04359
[^17]: https://dl.acm.org/doi/10.1145/3442188.3445922
[^18]: https://openai.com/research/learning-from-human-preferences
[^19]: https://twitter.com/zswitten/status/1598787052253827072
[^20]: https://arxiv.org/abs/2001.08361
[^21]: https://arxiv.org/abs/2203.15556
[^22]: https://arxiv.org/pdf/2112.11446.pdf
[^23]: https://arxiv.org/abs/2201.08239
[^24]: https://openai.com/research/gpt-4
[^25]: https://nethackchallenge.com/report.html
[^26]: https://www.deepmind.com/research/highlighted-research/alphago
[^27]: https://www.deepmind.com/research/highlighted-research/alphafold
[^28]: https://www.sciencedirect.com/science/article/abs/pii/S0065245808604088
[^29]: https://www.technologyreview.com/2020/11/03/1011616/ai-godfather-geoffrey-hinton-deep-learning-will-do-everything/
[^30]: https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow
[^31]: https://sites.google.com/site/krr2015/home/schedule
[^32]: https://openai.com/blog/chatgpt-plugins
[^33]: https://hugo-alves.github.io/movinggoalposts/
