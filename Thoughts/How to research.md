# What am I suffering from? (The Trap of Perfectionism)
Since starting my research in October 2025, I've been eager to produce tangible results, no matter how small. However, looking back, I feel like I've taken a long detour.

Initially, I took a passive stance, just waiting for my senior to assign me tasks. The first task was reading a paper on 3D reconstruction for endoscopic images. As I tried to understand and implement it, I felt overwhelmed by boredom and a severe lack of foundational knowledge—deep learning basics, traditional algorithms, camera calibration, etc.

My conclusion at the time was: "I need to study the basics first." I immediately started watching massive lecture series like CS231n and EECS 498-007. I mistakenly believed that a "true researcher" must master every underlying theory in the world before starting actual research.

But reality contradicted my belief. I saw fellow students publishing papers within just a year. If my "bottom-up" theory was correct, they should have spent at least two years solely studying CS fundamentals before even touching a research topic. Confused by this gap, I consulted my professor.

His advice was a wake-up call:

>"To produce results, you don't need to understand a paper 100%. Understanding just 20% is enough to start. Implement the code right away. As you struggle with the implementation, you will find the defects and limitations of the paper—and that exactly becomes your research topic."

This hit me hard. The scattered pieces of my knowledge finally started to connect. I once heard that the fastest way to learn is not reading a textbook sequentially, but jumping straight into what triggers your curiosity and learning what you need along the way. This is the Top-Down method, whereas I had been stuck in the Bottom-Up method. I don't think bottom-up is entirely wrong, but to be an effective researcher, top-down must be the primary driver.


## What is research?
Research is fundamentally driven by curiosity. Ideally, it begins with imagination. Imagination is where the true value of the "bottom-up" approach emerges: it is the organic combination of existing knowledge, which is the very origin of creation. For instance, I might read papers on SLAM and LLMs simply because they look interesting or are necessary for my work. It is only natural, then, to imagine combining them, resulting in something like Semantic SLAM. It feels akin to observing the historical intersection of geometry and algebra, which gave birth to calculus. Research, in this sense, is the act of making that imagination real—connecting existing knowledge and then rummaging through the vast sea of information (top-down) to bring it to life.

But sometimes, research doesn't start with a grand spark of imagination. As my professor pointed out, it often starts in the trenches. It begins by cloning a repository, running the existing code in various environments, and watching it break. When you test an algorithm in a new setting, it frequently reveals defects or edge cases that the original authors didn't account for. Identifying these specific problems, analyzing why the code fails, and figuring out how to overcome those limitations—that is also the very essence of research. It is the process of finding the gap between a paper's claim and the harsh reality, and bridging that gap.

## How to get through my problem?
The fundamental cause of my struggles was the misconception that to do research, I must first absorb everything. Studying without a clear purpose is a trap. The power of goal-oriented learning is enormous. When you study without the intent to build a robot or complete a project, the connections between fragmented pieces of knowledge remain weak. Conversely, when your learning is anchored to a specific project, you understand exactly how and why that knowledge is used, making it stick.

Therefore, the key to overcoming my problem is project-driven, goal-oriented learning: the Top-Down method.

## How can I balance top-down and bottom-up?
I am not saying the bottom-up approach is entirely useless. In my opinion, devoting 80% of your effort to bottom-up learning is ideal—until high school. The curriculum at that stage consists of general, foundational knowledge like calculus and basic physics. For students figuring out their career paths, broad exposure is crucial.

However, for someone like me who wants to dive into professional research, relying solely on this method is a disaster for efficiency. You cannot study everything "just in case" it might be useful someday. The top-down method provides a clear, laser-focused path.

For instance, if you are researching SLAM to map a stark, barren desert, you only need to dive into specific topics: optimization methods like Bundle Adjustment (BA), IMU sensor fusion, and related geometric concepts (DoF, Epipolar Geometry). To do this, you don't need to simultaneously re-study entire courses in deep learning, algorithms, or computer architecture just to feel "prepared."

That said, studying from scratch still holds value. Sometimes, ideas born from pure, undirected curiosity spark true innovation. Here is my 3-step action plan to balance the two:

>### 1. Define the Problem (Top-Down Trigger)
>Everything starts with a clear problem, driven by pure curiosity or discovered through hands-on experiments 
> ### 2. Learn the Prerequisites (Confined Bottom-Up)
>Once the goal is set, use tools like AI (Gemini/ChatGPT) or research papers to map out exactly what needs to be learned. Then, study those specific prerequisites deeply. This is a "confined bottom-up" approach—digging deep, but only within the strict boundaries of the problem.
>### 3. Study the Basics Regularly (Pure Bottom-Up)
>Allocate time for purely curiosity-driven study without immediate purpose. Read broadly—whether it's machine learning, physics, topology, or random papers. Building this robust, diverse groundwork is vital. Because groundbreaking ideas come from connecting the unconnected, this habit will spark latent connections and lead to unexpected breakthroughs one day.
