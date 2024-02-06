## RDD



### What is RDD?

```
* Resilient Distributed Datasets (RDD) is a fundamental data structure of Spark.
* At the core, an RDD is an immutable distributed collection of elements of your data, partitioned across nodes in your cluster that can be operated in parallel with a low-level API that offers transformations and actions.

```

### When to use RDDs ?

```

* You want low-level transformation and actions and control on your dataset;
* Your data is unstructured, such as media streams or streams of text;
* You want to manipulate your data with functional programming constructs than domain specific expressions;
* You don’t care about imposing a schema, such as columnar format while processing or accessing data attributes by name or column; and
* You can forgo some optimization and performance benefits available with DataFrames and Datasets for structured and semi-structured data.
```