Features
============================

MRAG application comes with lot of features to enable a user to index the documents, chat with the index documents. 
Below are the details of the features present in MRAG application.

======================================
Provides Interactive QA Bot
======================================

.. raw:: html

   <br>

.. image:: images/features/chatbot.png
   :alt: Chatbot
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

- You can chat with your documents by asking questions to the chatbot. 
- MRAG also supports voice chat where you can use your voice to ask a question.
- The retrieved context will be shown on the left (relevant text will be highlighted in yellow) for the user to verify the correctness of the bot's response.
- Each indexing pipeline will have its own chatbot and associated settings.


======================================
Customizable QA Chat Bot Settings
======================================

.. raw:: html

   <br>

.. image:: images/features/chat_settings.gif
   :alt: Chat Settings
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

- MRAG allows a user to configure the following settings
    - Prompt Template
    - Query Settings 
        - Query Cleaning
        - Query Rewriting
        - Query Decomposition
        - Self Querying
    - Retrieval Techniques
        - Simple Vector Retriever
        - Multi Query / Query Expansion Retriever
        - Reciprocal Rank Fusion (RRF) Retriever
    - Retriever Settings
        - Similarity Top K
        - Sparse Top K
        - Hybrid Top K
        - Hybrid Search Alpha
    - Reranker Settings
        - Reranker Model
        - Reranker Top K
    - Context Compression / Denoising
        - Context Extraction
        - Context Filtering
    - LLM Settings
        - Model
        - Model Temperature 
    - Post-processing of response
        - Combine sub query responses
    - Metrics
        - Context Relevance Score
        - Response Hallucination Score


======================================
Supports Query Enrichment
======================================

.. raw:: html

   <br>

.. image:: images/features/query_enrichment.png
   :alt: Query Enrichment
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

- Enables users to enrich the query for better retrieval and LLM responses.
- Supports query decomposition by generating sub queries to fetch answers for multiple queries in a single request.
- Supports query cleaning and query rewriting for better retrieval and LLM response.