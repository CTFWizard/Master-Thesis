import loguru
import sys
import argparse

from pentestgpt.pentest_gpt import PentestGPT


def main():
    """main function"""
    parser = argparse.ArgumentParser(description="PentestGPT")

    # parser arguments
    # 0. log directory
    parser.add_argument(
        "--log_dir",
        type=str,
        default="logs",
        help="path to the log directory, where conversations will be stored",
    )
    # 1. Reasoning Model
    parser.add_argument(
        "--reasoning_model",
        type=str,
        default="gpt-4",
        help="parsing models deal with the structural and grammatical aspects of language, choose 'gpt-4' or 'gpt-3.5-turbo-16k'",
    )
    # 2. Parsing Model
    parser.add_argument(
        "--parsing_model",
        type=str,
        default="gpt-3.5-turbo-16k",
        help="reasoning models are responsible for higher-level cognitive tasks, choose 'gpt-4' or 'gpt-3.5-turbo-16k'",
    )

    # 3. use langfuse default logging
    parser.add_argument(
        "--logging",
        action="store_true",
        default=False,
        help="allow PentestGPT developers to collect data through langfuse logging",
    )

    parser.add_argument(
        "--useDynamic",
        action="store_true",
        default=False,
        help="set to True to enable dynamic prompt engineering"
    )

    parser.add_argument(
        "--useDetect",
        action="store_true",
        default=False,
        help="set to enable automatic CTF challenge type detection"
    )

    # Deprecated: set to False only for testing if using cookie
    parser.add_argument(
        "--useAPI",
        action="store_true",
        default=True,
        help="deprecated: set to False only for testing if using cookie",
    )

    parser.add_argument(
        "--useRAG",
        action="store_true",
        default=False,
        help="Enable Retrieval Augmented Generation(RAG) for the generation and reasoning module.",
    )

    parser.add_argument(
        "--rag_dir",
        type=str,
        default="./rag-data",
        help="The directory containing all the data the RAG will embedd",
    )

    parser.add_argument(
        "--rag_chunk_size",
        type=int,
        default=1500,
        help="The size of the splitted chunks of documents in the RAG data.",
    )

    parser.add_argument(
        "--challenge_logging",
        action="store_true",
        default=False,
        help="Enables logging of userprompt and responses with their respective challenge. ",
    )
    args = parser.parse_args()

    pentestGPTHandler = PentestGPT(
        reasoning_model=args.reasoning_model,
        parsing_model=args.parsing_model,
        useDynamic=args.useDynamic,
        useDetect=args.useDetect,
        useAPI=args.useAPI,
        log_dir=args.log_dir,
        use_langfuse_logging=args.logging,
        useRAG=args.useRAG,
        rag_dir=args.rag_dir,
        rag_chunk_size = args.rag_chunk_size,
        useChallengeLogging = args.challenge_logging
    )

    pentestGPTHandler.main()


if __name__ == "__main__":
    main()
