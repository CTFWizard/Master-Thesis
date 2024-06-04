# Installation
`git clone https://github.com/CTFWizard/PentestGPT_Rewrite.git PentestGPT_Rewrite`

`cd PentestGPT_Rewrite`

`virtualenv -p python3 .venv`

| OS | Command |
| --- | --- |
| Windows | `.\.venv\Scripts\activate` |
| Win Bash | `source .venv/Scripts/activate` |
| Linux | `source .venv/bin/activate` |

`pip3 install -e`

# Help
Available models:
- `gpt4all`
- `localAI-phi2`
- `localAI-mistral`
- `localAI-mixtral`
- `localAI-tinyllama`
- `localAI-dolphin`
- `localAI-codellama`
- `devAPI` - This is testing purposes only, does not actually connect to an LLM.

## usage:
```
pentestgpt [-h] [--log_dir LOG_DIR] [--reasoning_model REASONING_MODEL] [--parsing_model PARSING_MODEL] [--logging] [--useDynamic] [--useDetect] [--useAPI] [--useRAG] [--rag_dir RAG_DIR] [--rag_chunk_size RAG_CHUNK_SIZE]
```
## options:
```
  -h, --help            show this help message and exit
  --log_dir LOG_DIR     path to the log directory, where conversations will be stored
  --reasoning_model REASONING_MODEL
                        parsing models deal with the structural and grammatical aspects of language, choose 'gpt-4' or 'gpt-3.5-turbo-16k'
  --parsing_model PARSING_MODEL
                        reasoning models are responsible for higher-level cognitive tasks, choose 'gpt-4' or 'gpt-3.5-turbo-16k'
  --logging             allow PentestGPT developers to collect data through langfuse logging
  --useDynamic          set to True to enable dynamic prompt engineering
  --useDetect           set to enable automatic CTF challenge type detection
  --useAPI              deprecated: set to False only for testing if using cookie
  --useRAG              Enable Retrieval Augmented Generation(RAG) for the generation and reasoning module.
  --rag_dir RAG_DIR     The directory containing all the data the RAG will embedd
  --rag_chunk_size RAG_CHUNK_SIZE
                        The size of the splitted chunks of documents in the RAG data.
```