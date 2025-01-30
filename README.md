<div align="center">
<h1>
  TRACE: Task-related Reinforced Automated Code Engine 🧑‍💻
</h1>

![image](https://github.com/user-attachments/assets/df699055-c536-4519-9130-463eaee43364)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>  

## <div align="center">Overview 🔎</div>

An innovative framework for automated code generation combining knowledge distillation and iterative refinement techniques. Implements teacher-student architecture with Mistral-7B and CodeLlama-7B models for robust code synthesis.

## <div align="center">Key Features and Components 🧩</div>

- **Teacher-Student Knowledge Distillation -** Transfer reasoning capabilities from large teacher models to efficient student models
- **Dynamic Feedback Mechanisms** include task decomposition planning, explainable error analysis, and edge-case testing (using Grok-generated cases)
- **Benchmark Performance -** 64.29% average pass ratio on BigCodeBench through iterative refinement
- **Resource-Efficient Architecture -** Optimized for CPU execution with memory-aware processing

| Component  | Description | Technologies | 
|---|---|---|
| Knowledge Distillation | Transfer learning from teacher models | [GPT-3.5](https://platform.openai.com/docs/models#gpt-3-5-turbo), [Mistral-7B-instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3)
| Task Decomposition | Atomic subtask breakdown | [CodeLlama-7b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf)
| Edge-Case Generation | Boundary condition testing | [Grok API](https://x.ai/api)
| Evaluation Pipeline | Pass ratio calculation | [BigCodeBench](https://bigcode-bench.github.io/)

## <div align="center">Quick Start ▶️</div>
### Prerequisites
- [Mistral-7B-instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3)
- [CodeLlama-7b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf)
- [GPT-3.5 API access](https://platform.openai.com/docs/models#gpt-3-5-turbo)
- [Grok API access](https://x.ai/api)

### Clone the repository
```
git clone https://github.com/VirajShah30/TRACE.git
cd TRACE
```

<hr>
<div align="center"><b> OR </b></div>
<hr>


### Proceed with running the cells in the following notebooks (can be run independently)
- BaseCode.ipynb [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VirajShah30/TRACE/blob/main/BaseCode.ipynb)
- TaskDecompositionADaPT.ipynb [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VirajShah30/TRACE/blob/main/TaskDecompositionADaPT.ipynb)
- KnowledgeDistillation.ipynb [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VirajShah30/TRACE/blob/main/KnowledgeDistillation.ipynb)
- EdgeTestCaseCode.ipynb [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VirajShah30/TRACE/blob/main/EdgeTestCaseCode.ipynb)

## <div align="center">Results 📊</div>
| Method  | Pass Ratio | Error Reduction | 
|---|---|---|
| Baseline | 41% | - |
| With Knowledge Distillation | 64.29% | 37% ↓ |
| With Edge-Case Testing | 36% | 44% ↓ |

## <div align="center">Contributors ✨</div>
- [Viraj Shah](https://github.com/VirajShah30) - Core architecture & evaluation pipeline
- [Ayush Prasad](https://github.com/bulkpool) - Task decomposition system
- [Mayank Shetty](https://github.com/msmayankshetty99) - Edge-case testing implementation & reinforcement learning integration
- [Shantanu Dhamdhere](https://github.com/ssd391) - CPU optimization strategies
- [Xiaoke Li](https://github.com/shockylove) - Edge-case testing implementation & reinforcement learning integration
- [Apurv Sawant](https://github.com/apurv-sawant15) - Cloud infrastructure & API services
