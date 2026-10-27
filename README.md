# Document Question-Answering Assistant

## 1. Project Overview

The Document Question-Answering Assistant answers questions using
information from a provided text document. It retrieves a relevant
passage, displays the supporting source passage, and gives a fallback
message when no relevant passage is found.

This project uses free, local Python tools and does not require a paid
API key.

## 2. Objective

-   Read text from a document.
-   Split the document into smaller passages.
-   Retrieve relevant passages for a user's question.
-   Display the answer together with its supporting source passage.
-   Transparently reject unsupported questions with the message:
    `Information not found in provided document.`

## 3. Technologies Used

-   Python
-   Jupyter Notebook
-   Scikit-learn
-   TF-IDF vectorization
-   Cosine similarity

## 4. Project Files

``` text
Document-QA-Assistant/
├── Document_QA_Assistant.ipynb
├── document_qa.py
├── sample_document.txt
├── requirements.txt
└── README.md
```

`Document_QA_Assistant.ipynb` contains the step-by-step development and
testing work. `sample_document.txt` is the sample corpus used for
testing. `document_qa.py` is the standalone source-code version of the
assistant.

## 5. Installation

Install the required library:

``` bash
pip install scikit-learn
```

The `requirements.txt` file should contain:

``` text
scikit-learn
```

## 6. How It Works

1.  **Document ingestion:** Load the supplied text document.
2.  **Chunking:** Split the text into passages.
3.  **TF-IDF:** Convert passages into numerical vectors.
4.  **Retrieval:** Convert the user's question into a vector and compare
    it with the passages using cosine similarity.
5.  **Grounded response:** Display the most relevant passage as the
    answer and show its source passage number.
6.  **Fallback:** If no matching terms are found or the similarity score
    is below the configured threshold, display
    `Information not found in provided document.`

## 7. Running the Project

### In Jupyter Notebook

1.  Open `Document_QA_Assistant.ipynb`.
2.  Run the cells in order, starting with the library
    installation/import cells.
3.  Run the document creation and chunking cells.
4.  Build the TF-IDF matrix.
5.  Run the answer function and the test cells.
6.  Run the interactive question loop to ask questions. Type `exit` to
    stop.

### From the Python source file

After `document_qa.py` is created and saved alongside
`sample_document.txt`, run:

``` bash
python document_qa.py
```

## 8. Sample Test Transcripts

The following examples show the expected behavior using the included
sample document. Exact similarity scores can vary with document content
and implementation.

### Test 1: Supported question

**Question**

``` text
What is Machine Learning?
```

**Expected behavior**

The assistant retrieves the passage explaining that Machine Learning is
a branch of AI that allows computers to learn patterns from data and
make predictions. It displays the passage as the supporting source.

### Test 2: Another supported question

**Question**

``` text
What does NLP do?
```

**Expected behavior**

The assistant retrieves the passage explaining that Natural Language
Processing helps computers understand, process, and generate human
language, and displays that passage as the source.

### Test 3: TF-IDF question

**Question**

``` text
What does TF-IDF stand for?
```

**Expected behavior**

The assistant retrieves the passage stating that TF-IDF stands for Term
Frequency-Inverse Document Frequency and displays it as the supporting
source.

### Test 4: Unsupported question

**Question**

``` text
Who invented ML?
```

**Observed output in the notebook**

``` text
Answer: Information not found in provided document.
```

This information is not included in the sample document, so the
assistant uses the fallback response.

### Test 5: Interactive exit

**Input**

``` text
exit
```

**Observed output**

``` text
Assistant stopped.
```

## 9. Limitations

-   TF-IDF is keyword-based retrieval, not a true semantic embedding
    model.
-   The answer is the retrieved passage rather than a generated
    paraphrase.
-   A similarity threshold is a simple fallback mechanism; it cannot
    guarantee that every possible answer is supported.
-   The sample corpus is small. Larger document collections may require
    more advanced chunking and retrieval methods.

## 10. Acceptance Checklist

-   [ ] Document text is loaded and split into passages.
-   [ ] TF-IDF retrieval finds relevant passages.
-   [ ] Supported answers display the source passage.
-   [ ] Unsupported questions show the required fallback message.
-   [ ] Sample document corpus is included.
-   [ ] Source code and README are included.
-   [ ] Test transcripts are checked against the actual notebook output.
-   [ ] Project files are uploaded to GitHub.

## 11. Notes

Before submission, verify that the standalone `document_qa.py` file
exists and runs successfully, and update the sample transcripts if your
final test output differs from the examples above.
