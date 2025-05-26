#  OpenAI Swarm and Agents SDK 

## Swarm Kya Hai?

Socho ke tumhare paas kai AI helpers hain. Har ek kisi kaam mein expert hai — koi billing ka, koi support ka, koi general info ka.

**Swarm** ek experimental system framework hai jo multiple AI agents ko ek team ki tarah kaam karne deta hai.

### Two Important Concepts:

- **Agents** – Ye AI ke parts hain jo instructions ko follow karke kaam karte hain.
- **Handoff** – Jab ek agent ko lagta hai ke koi aur agent kisi kaam mein behtar hai, to wo usay wo kaam transfer (handoff) kar deta hai.


Swarm bhi yehi karta hai — lekin yahan agents humans nahi, software hote hain.

---

##  OpenAI Agents SDK

OpenAI ne Swarm ko aur behtar banake **Agents SDK** banaya hai.

###  Kya karta hai ye SDK?

- Developers ke liye easy banata hai AI agents ka network banana.
- Agents apas mein mil kar real-life kaam karte hain:
  - Ek agent user se info leta hai.
  - Doosra agent info process karta hai.
  - Teesra agent result deta hai.

Yeh sab AI agents team ki tarah mil kar kaam karte hain — har agent ko apna role pata hota hai.

---

##  Anthropic Design Patterns – Asaan Alfaaz Mein

**Anthropic** ek AI company hai jinhon ne kuch smart patterns design kiye hain jo AI agents ko behtar banate hain. OpenAI ka **Agents SDK** inhi patterns ko follow karta hai.

### 5 Design Patterns:

---

### 1️⃣ Prompt Chaining (Chain Workflow)

** Matlab**:  
Bari mushkil task ko chhoti-chhoti steps mein divide karna.

** SDK mein kaise hota hai?**  
Har step ke liye alag agent banaya jata hai, jo ek sequence mein kaam karta hai.

**🔍 Example**:
- Ek agent subject likhta hai.
- Dusra body.
- Teesra grammar check karta hai.

---

### 2️ Routing

** Matlab**:  
Har kaam us agent ko dena jo us kaam mein expert ho.

** SDK mein kaise hota hai?**  
Agents apas mein kaam handoff karte hain — jise Routing kehte hain.

**🔍 Example**:  
General agent ne billing ka sawal suna — to billing agent ko transfer kar diya.

---

### 3️⃣ Parallelization

** Matlab**:  
Multiple kaam ek saath karwana — time save karne ke liye.

** SDK mein kaise hota hai?**  
Agents parallel mein kaam karte hain — sab apna kaam side-by-side karte hain.

**🔍 Example**:  
Ek document mein:
- Ek agent spell check karta hai.
- Doosra formatting.
- Teesra translation — sab ek saath.

---

### 4️⃣ Orchestrator-Workers

** Matlab**:  
Ek leader agent (Orchestrator) poore task ko todta hai, aur helpers (Workers) agents ko kaam deta hai.

** SDK mein kaise hota hai?**  
Orchestrator agent poore flow ko manage karta hai.

**🔍 Example**:  
Blog likhna hai:
- Ek agent title banata hai,
- Ek headings,
- Ek image choose karta hai.

---

### 5️⃣ Evaluator-Optimizer

** Matlab**:  
Ek agent doosre agents ka kaam check karta hai aur improve karne ke suggestions deta hai.

** SDK mein kaise hota hai?**  
Guardrails aur feedback system ka use hota hai.

**🔍 Example**:  
Evaluator agent grammar, tone, aur structure check karta hai aur improve karne ke liye guide karta hai.

---

## Conclusion:

OpenAI ka Agents SDK developers ko madad deta hai ek **smart, scalable aur efficient AI agents system** banane mein — jo in design patterns par based hota hai:

- 🔹 **Prompt Chaining** – Structured workflows
- 🔹 **Routing** – Smart task transfer
- 🔹 **Parallelization** – Fast multi-tasking
- 🔹 **Orchestrator** – Proper management
- 🔹 **Evaluator** – Continuous improvement

---

## 🏢 OpenAI Kya Hai?

**OpenAI** ek research company hai jo advanced Artificial Intelligence banati hai.

### 🔧 Famous Tools:
- **ChatGPT**
- **DALL·E**
- **Agents SDK**

🎯 **Mission**:  
Safe, powerful aur human-friendly AI banana.

---

## 🏢 Anthropic Kya Hai?

**Anthropic** bhi ek AI company hai — OpenAI jaisi.

### 🔧 Famous Product:
- **Claude** – ek AI chatbot

🎯 **Focus**:  
AI ko **safe aur understandable** banana.

---

## 🧩 Anthropic Design Patterns Kya Hain?

Ye wo **guidelines** hain jo batati hain:

> "AI agents ko aise design karo ke wo smart, efficient aur scalable hon."
