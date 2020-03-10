## Capstone


![Logo](/assets/img/logo/brand3.png "Logo")
##### Helps you evaluate your emotions and triggers.
# itone

### 01 - INTRODUCTION

**Project Overview**
- Journaling is an incredible stress management tool, a good habit that mitigates the
impact of physical stressors on your health. Also, a journal helps to clarify our goals
and helps to solve the problems of the past.

- **itone** is a visual mood tracking journal and diary application, which helps you
understand your emotions and trigger.

- **iTone** provides several options to help the user understand the influence of people,
surroundings, environment, time and other factors that impact mood which are
called triggers.

- Improve your strength by leading your emotions.

**Problem Statement**

> *“How might we help veterans and service members who are dealing with depression
journaling to understand the problems and triggers in the easiest way?"*

**Solution**
> *Creates a personal emotion tracking application.*

- Also, this can benefit the mental health treatment plan and support the user to
improve their coping skills.
_____________________________________________________________________________________________

### 02 - RESEARCH

**Target Audience**
- Focusing on veterans and service members who are diagnosed with depression. Currently in the treatment program and assigned individual mental health counselors. Which include psychiatrists, psychologist and social workers.

**Primary Sourcing**
- **Interview 1**<br>

    Name:       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tom<br>
    Age:        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;70<br>
    Occupation: &nbsp;Vietnam Veteran<br>
    Location:   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Colorado Springs, CO<br>

    > **Finding**
    > 1. *"I am a Vietnam Vet, who is struggling with Depression. I am in the recovery path
program in VA hospital. I have to do a journal to keep track of my emotions
daily to improve my coping skills and get help with my trauma."*
    > 2. I am not a good writer, but I have to try. It is too hard to explain how I feel.
    > 3. Sometimes the journaling is difficult when I get triggers and in a mood. I have no
plan to bring the notebook or the writing equipment everywhere I go.
    > 4. I have to fill out the assessment at the hospital every time when I see the doctor
for an update and evaluate my mood.<br>

- **Interview 2**<br>

    Name:       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Samuel<br>
    Age:        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;37<br>
    Occupation: &nbsp;Programmer<br>
    Location:   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;San Francisco, CA<br>

    > **Finding**
    > 1. I don’t like journaling, but I have to show my psychiatric the progress of my treatment
journey.
    > 2. I am not good enough to express my emotions in a writing way because when I’ve got
a trigger, I don’t want to do anything.
    > 3. The psychiatric will talk to me anyway why do I need to do a journal?
    > 4. *"I don’t want to bring paper and pen to journaling. It sounds like that takes a lot of
work."*
    > 5. I accepted that the journaling helps me improve my coping skills for sure.

_____________________________________________________________________________________________

### 03 - PROOF OF CONCEPT

**Persona**

![Persona2.](/assets/img/persona2.png "Persona2")
![Persona1.](/assets/img/persona1.png "Persona1")

**Storyboard**

![Storyboard.](/assets/img/storyboard.png "Storyboard")

**Data Model**

- User table
    - id
    - Name
    - Profile Image
    - Email
    - Username
    - Password

- Emotion table
    - id
    - User id (Foreign key to user )
    - Emotion icon
    - Emotion name

- Journal entry table
    - id
    - User id (Foreign key to user)
    - Emotion id (Foreign key to user)
    - Text
    - Timestamp
    - Intensity

- Journal entry emotion table
    - id
    - Journal entry id (Foreign key to user)
    - Emotion icon
    - Text
    - Timestamp
    - Intensity

**Project Timeline**
![Timeline.](/assets/img/timeline.png "Timeline")

**Information Architecture**
![IA.](/assets/img/ia.png "IA")

**Low-Fidelity Wireframes**
- Click a [Link](https://invis.io/PCWBB86RHQJ#/408353737_landing) to play with Wireframes Prototype..
![Wireframes](/assets/img/wireframe/wf.png "Wireframes")

**Color Palette**
![Color Palette](/assets/img/color.png "Color Palette")

**Button Design**
![Buttons](/assets/img/button.png "Buttons")

**UI Design**
- Click a [Link](https://invis.io/H3WCK1K6JNU#/408554325_landing) to play with Interaction Prototype.
![User Interface](/assets/img/ui/ui.png "User Interface")

_____________________________________________________________________________________________

### 04 - TECHNOLOGIES USAGE

- Development
  - Atom
  - HTML
  - CSS
  - JavaScript
  - Python
  - SQLite

- Framework
  - Bootstrap
  - Vue.js
  - Django

- Design
  - Illustrator
  - Sketch
  - InVision

_____________________________________________________________________________________________

### 05 - REFERENCES

* PsyberGuid: https://psyberguide.org/expert_review/apps-for-bi-polar-disorder-expert-review/
* 8 Reasons Keeping a Journal Can Help You Reach Your Goals: https://www.becomingminimalist.com/reasons-to-journal/
* Turning Trauma Into Story: the Benefits of Journaling: https://www.psychologytoday.com/us/blog/brain-babble/201208/turning-trauma-story-the-benefits-journaling
* 83 Benefits of Journaling for Depression, Anxiety, and Stress Management: https://positivepsychologyprogram.com/benefits-of-journaling/
* Images: https://pixabay.com
