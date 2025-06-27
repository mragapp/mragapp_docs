Q&A Chatbot
=============

Using the Q&A chatbot you can ask questions and get answers from your indexed documents. 
You can access the chatbot of an indexing pipeline from the indexing pipelines list.
Click on **Chat** menu item from the **Actions** menu of a specific pipeline as shown in the image below.

.. raw:: html

   <br>

.. image:: images/14_view_chatbot.png
   :alt: View Chatbot
   :align: center
   :class: bordered-image


============================
Chatbot components
============================
.. raw:: html

   <br>

.. image:: images/15_chatbot_components.png
   :alt: Chatbot Components
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

The chatbot has the components listed below.

- **Query Input**: Query input lets a user enter the query.

- **Submit**: The submit button is next to the Query Onput text input. A user hits the Submit button after entering the query.

- **Speak**: The Speak button is next to the Submit button. A user can click it, ask his query and hit the button again. Then the user's query will appear in the Query Input. 

- **Chat Settings**: The chat settings button displays the chat settings dialog box using which  a user can configure chat settings. 


============================
Chat Settings
============================
.. raw:: html

   <br>

.. image:: images/features/chat_settings.gif
   :alt: Chatbot Components
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Using the chat settings, a user can configure the chat settings for a given pipeline. Each indexing pipeline has its own chat settings.
Below are the settings a user can configure.

.. raw:: html

   <br>


Prompt Template
^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/16_prompt_template.png
   :alt: Prompt Template
   :align: center
   :class: bordered-image

.. raw:: html

   <br>


Prompt template enables a user to configure the prompt sent to  the LLM. The Prompt Template must definitely contain **{context_str}** and 
**{query}** placeholders that represent retreived context and the user query respectively.

.. raw:: html

   <br>


Query Settings
^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/17_query_settings.png
   :alt: Query Settings
   :align: center
   :class: bordered-image

.. raw:: html

   <br>


Query Settings enables a user to configure the settings for query enrichment. Below is the description of each query setting.

.. raw:: html

   <span class="param-highlight">Clean Query</span>
   <p>Cleans a query by removing few unwanted stop words. The cleaned query is used only for retrieval that may result in a more efficient retrieval. However, once the context is retrieved it is combined with the original user query and sent to LLM for response.</p>

.. raw:: html

   <span class="param-highlight">Rewrite Query</span>
   <p>Rewrites the user query using an LLM, such that it results in more efficient context retrieval and LLM response.
   </p>

.. raw:: html

   <span class="param-highlight">Generate Sub Queries</span>
   <p>Implements query decomposition where a user query is divided into multiple sub queries and each sub query is handled independently.
   This helps when a user query has multiple sub queries in a single query. 
   In such a case the context might not be retrieved properly for all the sub queries.
   </p>


.. raw:: html

   <span class="param-highlight">Enable Self Query</span>
   <p>Enables metadata filtering where the chunks are filtered using metadata filters. If no chunks are retrieved after metadata filtering 
   then the chunks are retrieved using vector index retrieval. 
   This setting is enabled only if at least one splitter in the indexing pipeline has a metadata schema selected. 
   </p>


.. raw:: html

   <br>



Retrieval Techniques
^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/18_retrieval_techniques.png
   :alt: Retrieval Techniques
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Retrieval Techniques enable a user to choose the right technique for efficient retrieval. Below is the description of each retrieval technique.

.. raw:: html

   <span class="param-highlight">Simple Retriever</span>
   <p>Performs simple vector index retrieval that uses cosine similarity to retrieve the relevant top-k chunks from the vector store.</p>

.. raw:: html

   <span class="param-highlight">Multi Query Retriever</span>
   <p>Implements query expansion by generating <b>N Queries</b> using an LLM such that the user query is represented in multiple forms 
   resulting in efficient retrieval. Then top-k (specified using Similarity Top K in Retriever Settings) chunks are retrieved for each query. 
   The chunks retrieved by all the queries are first sorted in descending order based on similarity score 
   and deduplicated and top-k chunks are returned as context. 
   </p>

.. raw:: html

   <span class="param-highlight">RRF Retriever</span>
   <p>Implements Reciprocal Rank Fusion (RAG Fusion) by generating <b>N Queries</b> using an LLM such that the user query is represented in multiple forms 
   resulting in efficient retrieval. 
   Then top-k (specified using Similarity Top K in Retriever Settings) chunks are retrieved for each query.
   The reciprocal rank of the chunks retrieved by each query is computed independently. 
   Then the reciprocal rank of a context retrieved from all the queries is summed to get a final reciprocal rank for a chunk. 
   Then the chunks are sorted in descending order and top-k chunks are returned as context.
   </p>


.. raw:: html

   <br>


Retriever Settings
^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/19_retriever_settings.png
   :alt: Retriever Settings
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Retriever Settings enable a user to configure the settings related to number of chunks to retrieve from vector store. 
Below is the description of each retriever setting.

.. raw:: html

   <span class="param-highlight">Similarity Top K</span>
   <p>Number of chunks to retrieve using dense vectors.</p>

.. raw:: html

   <span class="param-highlight">Sparse Top K</span>
   <p>Applies only when the vector store supports hybrid search. Number of chunks to be retrieved using sparse vectors.
   </p>


.. raw:: html

   <span class="param-highlight">Hybrid Top K</span>
   <p>Applies only when the vector store supports hybrid search. Final number of top-k chunks (sparse + dense) to be retrieved from vector store.
   </p>


.. raw:: html

   <span class="param-highlight">Hybrid Search Alpha</span>
   <p>Applies only when the vector store supports hybrid search. When 0, sparse vector retrieval is enabled. When 1, dense vector search is enabled.
   Anythin between 0 and 1 balances both sparse and dense vector retrieval.
   </p>


.. raw:: html

   <br>


Reranker Settings
^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/20_reranker_settings.png
   :alt: Reranker Settings
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Reranker Settings enable a user to configure the settings related to reranker. 
Below is the description of each reranker setting.

.. raw:: html

   <span class="param-highlight">Enable Reranker</span>
   <p>Whether reranker must be enabled.</p>

.. raw:: html

   <span class="param-highlight">Reranker Model</span>
   <p>Choose the reranker model.</p>


.. raw:: html

   <span class="param-highlight">Reranker Top K</span>
   <p>Top-k chunks to return after reranking.</p>


.. raw:: html

   <br>


Context Compression / Denoising
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/21_context_compression.png
   :alt: Context Compression / Denoising
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Context Compression / Denoising Settings enable a user to configure the settings related to filtering or denoising the retrieved context from vector store. 
These settings are enabled only when the reranker is not enabled. Below is the description of each Context Compression / Denoising setting. 

.. raw:: html

   <span class="param-highlight">Extract Context</span>
   <p>Extracts relevant information using an LLM from the retrieved context required to answer a user query.</p>

.. raw:: html

   <span class="param-highlight">Filter Context</span>
   <p>Returns only the chunks relevant to the user query using an LLM from the chunks retrieved from the vector store.</p>


.. raw:: html

   <br>


LLM Settings
^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/22_llm_settings.png
   :alt: LLM Settings
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

LLM Settings enable a user to configure the settings related to the large language model. Below is the description of each LLM setting. 

.. raw:: html

   <span class="param-highlight">LLM Model</span>
   <p>Large language model to use for generating LLM responses wherever required like Query Rewriting, Context Filtering, etc.</p>

.. raw:: html

   <span class="param-highlight">Temperature</span>
   <p>Set the LLM model's temperature. Value close to 0 returns deterministic response and value close to 1 returns probabilistic response.</p>


.. raw:: html

   <br>


Response Processing
^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/23_response_processing.png
   :alt: Response Processing
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Response Processing Settings enable a user to configure the settings related to response synthesis. 
Below is the description of each Response Processing setting. 

.. raw:: html

   <span class="param-highlight">Combine Sub Query Responses</span>
   <p>Combines responses of sub queries into a single response. This setting is enabled only when "Generate Sub Queries" in "Query Settings" is enabled.</p>


.. raw:: html

   <br>


Metrics
^^^^^^^^^^^^^^^^^^^^

.. raw:: html

   <br>

.. image:: images/24_metrics.png
   :alt: Metrics
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Metrics settings enable to user to choose which metrics to be displayed in the chat response. 
Below is the description of each Metrics setting.

.. raw:: html

   <span class="param-highlight">Context Relevance Score</span>
   <p>Context relevance score helps in evaluating the retriever's performance.</p>

.. raw:: html

   <span class="param-highlight">Response Hallucination Score</span>
   <p>Response hallucination score helps in evaluation the LLM response quality.</p>



============================
Suggested Queries
============================
.. raw:: html

   <br>

.. image:: images/features/query_suggestions.png
   :alt: Suggested Queries
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

Suggested Queries feature shows the queries a document can answer. This feature is enabled only if a user includes HyPE component in the indexing pipeline.
Below screenshot shows how to access this feature.

.. raw:: html

   <br>

.. image:: images/25_access_suggested_queries.png
   :alt: How To Access Suggested Queries
   :align: center
   :class: bordered-image

.. raw:: html

   <br>

In the Chatbot screen click on the menu on the top right to access the "Suggested Queries" feature. 
This will display the suggested queries for each document extracted using HyPE when it is included in the indexing pipeline. 
If HyPE is not included in the indexing pipeline then suggested queries will not be available.
A user can select the required query and it will be inserted in the "Query Input" and the user can hit the "Submit" button after making any required changes to the query. 
