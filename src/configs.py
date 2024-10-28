Evaluating_UserResponse_Prompt = """
Generate a JSON evaluation of a user’s response by analyzing the provided chat history. Follow the scoring guidelines and variables below.

-- Begin Instructions --
Analyze the chat history provided below. Focus on extracting relevant narrative insights for each variable listed, considering the user's tone, language, and content. For each narrative variable, rate the user’s engagement on a scale of 1-5, or mark it as "N/A" if it’s not addressed.

Agency: User’s sense of control over experiences.
Communion: Emphasis on relationships or connectedness.
Growth Goals: Focus on self-development.
Positive Resolution: Ability to achieve peace with a challenging event.
Accommodative Processing: Shifts in worldview or self-perception.
Exploratory Processing: Effort to reflect on experiences.
Meaning-Making: Deriving meaning from events.
Contamination: Transition from positive to negative outcomes.
Redemption: Transition from negative to positive outcomes.
Coherence: Narrative clarity and context.
Complexity: Depth of thought and engagement with the narrative.
Return a JSON with scores and a brief justification for each variable.

Chat History:
{{ $recent_history }}

-- End Instructions --\n

Return a JSON file with the following format: {
    "agency": <string>, "communion": <string>,"growth goals": <string>,"positive resolution": <string>, "accommodative processing": <string>, "exploratory processing": <string>, "meaning-making": <string>, "contamination": <string>, "redemption":<string>, "coherence":<string>, "complexity":<string>,                                                                                  
"reasoning": <string>, "interview tips", "question": <string>
}

-- EXAMPLES --
USER :: 'A defining moment in my life was when I decided to leave my stable corporate job to start my own business. It was a huge risk, and I was terrified, but I knew I needed to follow my passion. The initial months were tough, and there were moments when I doubted myself, but eventually, I found my footing. The experience taught me the value of perseverance and the importance of believing in myself.'

INTERVIEWER :: 
   {
  "agency": "5: User demonstrated strong agency by making the significant decision to leave their job and pursue entrepreneurship, showing a high level of control and self-mastery.",
  "communion": "3: While the user expressed a personal journey, there is no strong emphasis on relationships or external support, though moments of doubt could imply a need for encouragement.",
  "growth_goals": "5: User's decision to start a business indicates a clear focus on personal growth and development, with intentional efforts to achieve self-defined goals.",
  "positive_resolution": "4: The user reached a point of stability and success in their business, indicating a mostly positive outcome, though the narrative reflects some ongoing challenges.",
  "accommodative_processing": "5: The decision to leave a stable job and take a risk led to a significant shift in the user's worldview and self-perception, highlighting deep change.",
  "exploratory_processing": "4: User reflected on their doubts and growth throughout the experience, showing depth and an openness to learning from the journey.",
  "meaning-making": "5: User derived a strong sense of purpose and important life lessons from the experience, particularly around perseverance and self-belief.",
  "contamination": "2: Although there were challenging moments, the narrative predominantly focuses on overcoming adversity, with no sustained negative shift.",
  "redemption": "3: The experience includes elements of redemption, where initial difficulties transformed into eventual success and stability.",
  "coherence": "5: The narrative is well-organized, with a clear beginning (decision), middle (challenges), and end (finding stability), supporting emotional clarity.",
  "complexity": "4: User demonstrated an understanding of different aspects of the journey, including fear, doubt, and perseverance, contributing to a nuanced narrative.",
}

---

USER :: 'Deciding to move to a different country for work was one of the toughest decisions I've made. The first few months were incredibly challenging; I felt out of place and missed home. But over time, I adjusted and even started to enjoy the new culture. Now, I feel more confident in facing unfamiliar situations.'
INTERVIEWER :: {
  "agency": "4: User demonstrated a considerable amount of agency by choosing to move abroad and facing the challenges that came with it, showing personal initiative.",
  "communion": "3: While the user mentions missing home, there is limited emphasis on relationships, suggesting some degree of separation or adaptation to being on their own.",
  "growth_goals": "5: The experience reflects intentional efforts toward self-growth, particularly in adapting to a new environment and building confidence.",
  "positive_resolution": "5: The narrative ends with a positive outcome, as the user grew more comfortable and confident in their new surroundings.",
  "accommodative_processing": "4: The experience shifted the user’s perception of their own resilience and adaptability, indicating significant change.",
  "exploratory_processing": "3: There is some reflection on the process of adaptation, but the narrative does not deeply analyze the emotional or psychological impact.",
  "meaning-making": "4: User found meaning in the experience by recognizing their increased confidence and adaptability as outcomes of the decision to move.",
  "contamination": "2: The initial challenges did not persist throughout the narrative, as the user eventually adjusted and found positive aspects in the situation.",
  "redemption": "4: The experience included a transition from feeling out of place to finding enjoyment and confidence, indicating a redemptive quality.",
  "coherence": "5: The narrative is clear and structured, with a defined progression from initial struggle to adaptation and eventual confidence.",
  "complexity": "3: The user addressed different phases of the experience, but there is limited exploration of diverse emotions or deeper underlying factors.",
}

---
USER :: "I've always been someone who likes to plan things out, so I sat down last year and created a five-year plan for my life. I outlined the career goals I wanted to achieve, the personal milestones I hoped to reach, and even some travel destinations. Since then, I've been able to check off a few smaller goals, like learning a new language and saving up for a major trip. 
It feels great to have a clear direction, even though I know some things might change along the way."
INTERVIEWER :: {
"agency": "5: User demonstrated a strong sense of agency by creating a structured five-year plan, taking control of their life trajectory and actively pursuing their goals.",
  "communion": "3: While the narrative focuses on personal goals, there isn't a strong emphasis on relationships or social connections, although these may still play a role in the background.",
  "growth_goals": "5: The user’s focus on career achievements, personal milestones, and skill development highlights a commitment to intentional self-improvement and goal-setting.",
  "positive_resolution": "4: The user experienced progress by achieving smaller goals and feeling satisfaction from having a sense of direction, though some aspects of the plan are ongoing.",
  "accommodative_processing": "3: The user shows some flexibility by acknowledging that the plan may change over time, though there is no indication of significant shifts in worldview yet.",
  "exploratory_processing": "3: The reflection provides a general overview of their experiences with life planning, but lacks deep emotional or cognitive analysis of the impact of these goals.",
  "meaning-making": "4: User finds meaning in setting and achieving goals, as it gives them a sense of purpose and direction, which is valuable in their overall life journey.",
  "contamination": "1: There are no elements of contamination present; the narrative maintains a positive tone throughout, with no setbacks or negative shifts.",
  "redemption": "2: While the user finds fulfillment in checking off goals, the narrative does not involve a transformation from a negative to a positive state.",
  "coherence": "5: The narrative is coherent and structured, detailing the planning process, progress made, and future outlook, which supports a clear understanding of the user’s approach.",
  "complexity": "3: User addresses multiple aspects of their life (career, personal growth, travel) in a straightforward manner, but the narrative does not delve deeply into diverse emotions or perspectives.",
}

---

USER:: "I’ve always dreamt of traveling to 50 countries before I turn 40. I’m planning to leave for my next adventure in a few months. While it feels overwhelming to manage work, savings, and planning all the trips, I’m excited to immerse myself in new cultures, meet interesting people, and expand my perspective. I hope that by the time I reach my goal, I will have grown both personally and professionally, with a deeper understanding of the world."
INTERVIEWER :: {
 "agency": "4: User takes active control of their future, demonstrating a high level of personal initiative in pursuing their dream of traveling the world.", 
 "communion": "4: The user highlights their desire to connect with new people and cultures, suggesting a focus on forming relationships through shared experiences.",
   "growth_goals": "5: The goal reflects a strong focus on personal growth, both in terms of exploring the world and developing a broader outlook on life.", 
   "positive_resolution": "N/A: Since this is a future event, the outcome is yet to be determined, but the user expresses optimism about achieving their goal.", 
   "accommodative_processing": "N/A: This element does not apply since the event hasn’t occurred yet.", "exploratory_processing": "3: There is some exploration of the excitement and challenges that come with balancing work and travel, but not much depth regarding potential struggles.", 
   "meaning-making": "3: The user anticipates that this journey will help them grow, but further reflection is limited since it hasn't happened yet.", "contamination": "N/A: There is no negative resolution mentioned, as this is a future-oriented story.", "redemption": "N/A: Since the event is in the future, there’s no clear redemptive theme.", "coherence": "4: The narrative is well-structured, outlining the user’s goal and expected challenges along the way.", "complexity": "3: The user briefly mentions potential difficulties but focuses mostly on the excitement and personal growth aspects.", "reasoning": "User expresses a clear goal and anticipation for personal and professional development, showing thoughtfulness in balancing aspirations with practical concerns.", 
 }

 ---
USER:: ""I’m currently in the middle of a career transition. After years of working in one field, I realized I wasn’t fulfilled, so I decided to pursue something more aligned with my passions. It’s been a challenging process—learning new skills and adjusting to a completely different industry. I’ve had moments of doubt, but I’m excited by the opportunities ahead. Right now, I’m focusing on developing my expertise and building connections in the new field. Even though I don’t have everything figured out yet, I feel more motivated and inspired than I have in a long time."
INTERVIEWER :: 
{ "agency": "5: The user is actively taking steps to change their career, showing strong initiative and determination.", 
"communion": "3: While relationships are not the focus, the user mentions building connections in their new field, indicating some social integration.",
 "growth_goals": "5: The user is clearly focused on self-improvement and aligning their work with their passions.", "positive resolution": "N/A: As this is an ongoing event, the outcome has not yet been determined.", 
 "accommodative processing": "N/A: The event is still unfolding, so no significant change in perception has been discussed.", "exploratory processing": "4: The user reflects on the challenges of changing careers and the emotional rollercoaster involved, showing some depth of thought.", 
 "meaning-making": "3: The user finds meaning in pursuing something they are passionate about but does not yet reflect deeply on the overall impact.", 
 "contamination": "N/A: As the story is ongoing, there is no negative conclusion.", "redemption": "N/A: Since the event is still happening, no clear redemptive outcome is present yet.",
"coherence": "4: The narrative is structured but incomplete due to its present nature.", "complexity": "3: The user addresses their current situation, but more emotional complexity could be explored.", "reasoning": "User emphasizes the importance of pursuing passions and facing challenges head-on, showing insight into personal motivations.",
}


---
USER::"I hope I can buy a penthouse in Dalat city in the next chapter of my life"

INTERVIEWER ::{
  "agency": "3: The user expresses a hope to buy a penthouse, which indicates some level of personal initiative but lacks a concrete plan of action or specific steps they will take to achieve this. The goal is aspirational rather than decisively proactive.",
  "communion": "2: The statement focuses on an individual goal (buying a penthouse) and does not mention relationships or connections to others, which suggests limited emphasis on communion or interpersonal aspects.",
  "growth goals": "4: The desire to purchase a penthouse reflects ambition and forward-thinking, suggesting a personal growth goal related to financial success, stability, or lifestyle improvement.",
  "positive resolution": "N/A: Since this is a future-oriented statement, there is no clear resolution yet, but the user's optimistic tone implies a desire for a positive outcome in this chapter of their life.",
  "accommodative processing": "N/A: The statement does not indicate any adjustment in beliefs or behavior based on past experiences. It focuses solely on future aspirations.",
  "exploratory processing": "2: The statement expresses a clear hope but does not delve into deeper reflection or analysis regarding the reasons behind the desire or the emotional significance of achieving this goal.",
  "meaning-making": "3: Buying a penthouse may hold symbolic meaning for the user, perhaps representing a milestone in success, stability, or comfort. However, this deeper meaning is not explicitly explored in the statement.",
  "contamination": "N/A: There is no mention of negative experiences or potential challenges that could affect the user's goal in this statement.",
  "redemption": "N/A: The goal is future-focused, with no narrative of overcoming obstacles or turning negative situations into positive outcomes at this point.",
  "coherence": "4: The statement is clear and easy to understand, outlining a specific future aspiration. However, providing more context around the goal could enhance the overall coherence and richness of the narrative.",
  "complexity": "2: The statement is straightforward and lacks exploration of diverse emotions, underlying motivations, or the broader context that could add depth to the narrative.",
}
-- END EXAMPLES --
"""

Pretext_Prompt = """
You are going to synthesized pretext for crafting follow-up questions based on the evaluation scores and user’s chat history.
You need to return the JSON file.

-- Begin Instructions --
Using the user’s chat history and evaluation scores from the previous prompt, summarize the main themes, topics, and tones in 2-3 sentences. Reflect the user’s tone and show empathy, using phrases like “I see” or “That’s interesting.” Express gratitude to the user for sharing their insights, which will set a positive tone for future interactions.

Include the following in your response:

A brief, empathetic summary of the main topics discussed.
Acknowledgment of any challenges faced and appreciation for sharing.

-- BEGIN CHAT HISTORY --\n {{$recent_history}} -- END CHAT HISTORY --\n
-- BEGIN EVALUATION SUMMARY --\n {{ $evaluation_summary }} -- END EVALUATION SUMMARY --\n
"""

follow_up_question = """
You are aiming to craft a meaningful follow-up question that encourages further exploration for the user based on the context provided by the pretext.

-- Begin Instructions --
Using the pretext and evaluation, create a follow-up question that encourages deeper reflection, particularly in areas that were less addressed. Design the question to gently prompt the user to explore aspects of their journey, such as personal growth, relationships, or meaning derived from experiences. Tailor the question to acknowledge challenges they shared while fostering a supportive environment.

-- BEGIN PRETEXT SUMMARY --\n {{ $pretext_summary }} -- END PRETEXT SUMMARY --\n
-- End Instructions --

"""