# Bug Analysis Summary

Analyzed 915 Java files with potential issues

## Bug Count by Type

- Unused Code: 11757
- Exception Handling: 730
- Concurrency Issue: 999
- Resource Leak: 45
- Null Pointer: 36
- Infinite Loop: 12



## ../benchmarks/src/main/java/org/elasticsearch/benchmark/bytes/BytesArrayReadLongBenchmark.java

### Unused Code (22)
- Line 41: `private int dataMb;`
- Line 43: `private BytesReference bytesArray;`
- Line 45: `private StreamInput streamInput;`
- Line 11: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 12: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 13: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 14: `import org.elasticsearch.common.io.stream.StreamInput;`
- Line 15: `import org.elasticsearch.common.unit.ByteSizeUnit;`
- Line 16: `import org.elasticsearch.common.unit.ByteSizeValue;`
- Line 17: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 18: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 19: `import org.openjdk.jmh.annotations.Fork;`
- Line 20: `import org.openjdk.jmh.annotations.Measurement;`
- Line 21: `import org.openjdk.jmh.annotations.Mode;`
- Line 22: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 23: `import org.openjdk.jmh.annotations.Param;`
- Line 24: `import org.openjdk.jmh.annotations.Scope;`
- Line 25: `import org.openjdk.jmh.annotations.Setup;`
- Line 26: `import org.openjdk.jmh.annotations.State;`
- Line 27: `import org.openjdk.jmh.annotations.Warmup;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/bytes/BytesArrayReadVLongBenchmark.java

### Unused Code (18)
- Line 41: `private StreamInput streamInput;`
- Line 11: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 12: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 13: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 14: `import org.elasticsearch.common.io.stream.StreamInput;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Measurement;`
- Line 19: `import org.openjdk.jmh.annotations.Mode;`
- Line 20: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 21: `import org.openjdk.jmh.annotations.Param;`
- Line 22: `import org.openjdk.jmh.annotations.Scope;`
- Line 23: `import org.openjdk.jmh.annotations.Setup;`
- Line 24: `import org.openjdk.jmh.annotations.State;`
- Line 25: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/bytes/PagedBytesReferenceReadLongBenchmark.java

### Unused Code (22)
- Line 41: `private int dataMb;`
- Line 43: `private BytesReference pagedBytes;`
- Line 45: `private StreamInput streamInput;`
- Line 11: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 12: `import org.elasticsearch.common.bytes.PagedBytesReference;`
- Line 13: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 14: `import org.elasticsearch.common.io.stream.StreamInput;`
- Line 15: `import org.elasticsearch.common.unit.ByteSizeUnit;`
- Line 16: `import org.elasticsearch.common.unit.ByteSizeValue;`
- Line 17: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 18: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 19: `import org.openjdk.jmh.annotations.Fork;`
- Line 20: `import org.openjdk.jmh.annotations.Measurement;`
- Line 21: `import org.openjdk.jmh.annotations.Mode;`
- Line 22: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 23: `import org.openjdk.jmh.annotations.Param;`
- Line 24: `import org.openjdk.jmh.annotations.Scope;`
- Line 25: `import org.openjdk.jmh.annotations.Setup;`
- Line 26: `import org.openjdk.jmh.annotations.State;`
- Line 27: `import org.openjdk.jmh.annotations.Warmup;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/bytes/PagedBytesReferenceReadVIntBenchmark.java

### Unused Code (18)
- Line 41: `private StreamInput streamInput;`
- Line 11: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 12: `import org.elasticsearch.common.bytes.PagedBytesReference;`
- Line 13: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 14: `import org.elasticsearch.common.io.stream.StreamInput;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Measurement;`
- Line 19: `import org.openjdk.jmh.annotations.Mode;`
- Line 20: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 21: `import org.openjdk.jmh.annotations.Param;`
- Line 22: `import org.openjdk.jmh.annotations.Scope;`
- Line 23: `import org.openjdk.jmh.annotations.Setup;`
- Line 24: `import org.openjdk.jmh.annotations.State;`
- Line 25: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/bytes/PagedBytesReferenceReadVLongBenchmark.java

### Unused Code (18)
- Line 41: `private StreamInput streamInput;`
- Line 11: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 12: `import org.elasticsearch.common.bytes.PagedBytesReference;`
- Line 13: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 14: `import org.elasticsearch.common.io.stream.StreamInput;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Measurement;`
- Line 19: `import org.openjdk.jmh.annotations.Mode;`
- Line 20: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 21: `import org.openjdk.jmh.annotations.Param;`
- Line 22: `import org.openjdk.jmh.annotations.Scope;`
- Line 23: `import org.openjdk.jmh.annotations.Setup;`
- Line 24: `import org.openjdk.jmh.annotations.State;`
- Line 25: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/common/util/IntArrayBenchmark.java

### Exception Handling (1)
- Line 88: `throw new IllegalArgumentException("unsupported [type] " + type);`

### Unused Code (27)
- Line 50: `private String type;`
- Line 52: `private IntArray read;`
- Line 12: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 13: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 14: `import org.elasticsearch.common.bytes.CompositeBytesReference;`
- Line 15: `import org.elasticsearch.common.bytes.PagedBytesReference;`
- Line 16: `import org.elasticsearch.common.bytes.ReleasableBytesReference;`
- Line 17: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 18: `import org.elasticsearch.common.unit.ByteSizeValue;`
- Line 19: `import org.elasticsearch.common.util.BigArrays;`
- Line 20: `import org.elasticsearch.common.util.IntArray;`
- Line 21: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 22: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 23: `import org.openjdk.jmh.annotations.Fork;`
- Line 24: `import org.openjdk.jmh.annotations.Measurement;`
- Line 25: `import org.openjdk.jmh.annotations.Mode;`
- Line 26: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 27: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 28: `import org.openjdk.jmh.annotations.Param;`
- Line 29: `import org.openjdk.jmh.annotations.Scope;`
- Line 30: `import org.openjdk.jmh.annotations.Setup;`
- Line 31: `import org.openjdk.jmh.annotations.State;`
- Line 32: `import org.openjdk.jmh.annotations.Warmup;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.util.ArrayList;`
- Line 36: `import java.util.List;`
- Line 37: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/AggregatorBenchmark.java

### Concurrency Issue (30)
- Line 73: `static final int BLOCK_LENGTH = 8 * 1024;`
- Line 74: `private static final int OP_COUNT = 1024;`
- Line 75: `private static final int GROUPS = 5;`
- Line 77: `private static final BlockFactory blockFactory = BlockFactory.getInstance(`
- Line 82: `private static final String LONGS = "longs";`
- Line 83: `private static final String INTS = "ints";`
- Line 84: `private static final String DOUBLES = "doubles";`
- Line 85: `private static final String BOOLEANS = "booleans";`
- Line 86: `private static final String BYTES_REFS = "bytes_refs";`
- Line 87: `private static final String ORDINALS = "ordinals";`
- Line 88: `private static final String TWO_LONGS = "two_" + LONGS;`
- Line 89: `private static final String TWO_BYTES_REFS = "two_" + BYTES_REFS;`
- Line 90: `private static final String TWO_ORDINALS = "two_" + ORDINALS;`
- Line 91: `private static final String LONGS_AND_BYTES_REFS = LONGS + "_and_" + BYTES_REFS;`
- Line 92: `private static final String TWO_LONGS_AND_BYTES_REFS = "two_" + LONGS + "_and_" + BYTES_REFS;`
- Line 94: `private static final String VECTOR_DOUBLES = "vector_doubles";`
- Line 95: `private static final String HALF_NULL_DOUBLES = "half_null_doubles";`
- Line 96: `private static final String VECTOR_LONGS = "vector_" + LONGS;`
- Line 97: `private static final String HALF_NULL_LONGS = "half_null_" + LONGS;`
- Line 98: `private static final String MULTIVALUED_LONGS = "multivalued";`
- Line 100: `private static final String AVG = "avg";`
- Line 101: `private static final String COUNT = "count";`
- Line 102: `private static final String COUNT_DISTINCT = "count_distinct";`
- Line 103: `private static final String MIN = "min";`
- Line 104: `private static final String MAX = "max";`
- Line 105: `private static final String SUM = "sum";`
- Line 107: `private static final String NONE = "none";`
- Line 109: `private static final String CONSTANT_TRUE = "constant_true";`
- Line 110: `private static final String ALL_TRUE = "all_true";`
- Line 111: `private static final String HALF_TRUE = "half_true";`

### Exception Handling (21)
- Line 185: `default -> throw new IllegalArgumentException("unsupported grouping [" + grouping + "]");`
- Line 200: `default -> throw new IllegalArgumentException("unsupported data type [" + dataType + "]");`
- Line 205: `default -> throw new IllegalArgumentException("unsupported data type [" + dataType + "]");`
- Line 210: `default -> throw new IllegalArgumentException("unsupported data type [" + dataType + "]");`
- Line 215: `default -> throw new IllegalArgumentException("unsupported data type [" + dataType + "]");`
- Line 217: `default -> throw new IllegalArgumentException("unsupported op [" + op + "]");`
- Line 321: `default -> throw new IllegalArgumentException("bad data type " + dataType);`
- Line 346: `default -> throw new IllegalArgumentException("bad data type " + dataType);`
- Line 371: `default -> throw new IllegalArgumentException("bad data type " + dataType);`
- Line 374: `default -> throw new IllegalArgumentException("bad op " + op);`
- Line 423: `default -> throw new IllegalArgumentException("bad grouping [" + grouping + "]");`
- Line 458: `default -> throw new IllegalStateException("Unexpected aggregation type: " + dataType);`
- Line 469: `default -> throw new IllegalStateException("Unexpected aggregation type: " + dataType);`
- Line 480: `default -> throw new IllegalStateException("Unexpected aggregation type: " + dataType);`
- Line 486: `default -> throw new IllegalArgumentException("bad op " + op);`
- Line 535: `default -> throw new IllegalArgumentException("bad blockType: " + blockType);`
- Line 558: `default -> throw new UnsupportedOperationException("bad grouping [" + grouping + "]");`
- Line 619: `default -> throw new UnsupportedOperationException("unsupported grouping [" + grouping + "]");`
- Line 630: `default -> throw new UnsupportedOperationException("can't handle [" + group + "]");`
- Line 675: `default -> throw new IllegalArgumentException("unsupported filter [" + filter + "]");`
- Line 690: `default -> throw new IllegalArgumentException();`

### Unused Code (49)
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 14: `import org.elasticsearch.common.util.BigArrays;`
- Line 15: `import org.elasticsearch.compute.aggregation.AggregatorFunctionSupplier;`
- Line 16: `import org.elasticsearch.compute.aggregation.AggregatorMode;`
- Line 17: `import org.elasticsearch.compute.aggregation.CountAggregatorFunction;`
- Line 18: `import org.elasticsearch.compute.aggregation.CountDistinctDoubleAggregatorFunctionSupplier;`
- Line 19: `import org.elasticsearch.compute.aggregation.CountDistinctLongAggregatorFunctionSupplier;`
- Line 20: `import org.elasticsearch.compute.aggregation.FilteredAggregatorFunctionSupplier;`
- Line 21: `import org.elasticsearch.compute.aggregation.MaxDoubleAggregatorFunctionSupplier;`
- Line 22: `import org.elasticsearch.compute.aggregation.MaxLongAggregatorFunctionSupplier;`
- Line 23: `import org.elasticsearch.compute.aggregation.MinDoubleAggregatorFunctionSupplier;`
- Line 24: `import org.elasticsearch.compute.aggregation.MinLongAggregatorFunctionSupplier;`
- Line 25: `import org.elasticsearch.compute.aggregation.SumDoubleAggregatorFunctionSupplier;`
- Line 26: `import org.elasticsearch.compute.aggregation.SumLongAggregatorFunctionSupplier;`
- Line 27: `import org.elasticsearch.compute.aggregation.blockhash.BlockHash;`
- Line 28: `import org.elasticsearch.compute.data.Block;`
- Line 29: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 30: `import org.elasticsearch.compute.data.BooleanBlock;`
- Line 31: `import org.elasticsearch.compute.data.BooleanVector;`
- Line 32: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 33: `import org.elasticsearch.compute.data.BytesRefVector;`
- Line 34: `import org.elasticsearch.compute.data.DoubleBlock;`
- Line 35: `import org.elasticsearch.compute.data.ElementType;`
- Line 36: `import org.elasticsearch.compute.data.IntBlock;`
- Line 37: `import org.elasticsearch.compute.data.IntVector;`
- Line 38: `import org.elasticsearch.compute.data.LongBlock;`
- Line 39: `import org.elasticsearch.compute.data.OrdinalBytesRefVector;`
- Line 40: `import org.elasticsearch.compute.data.Page;`
- Line 41: `import org.elasticsearch.compute.operator.AggregationOperator;`
- Line 42: `import org.elasticsearch.compute.operator.DriverContext;`
- Line 43: `import org.elasticsearch.compute.operator.EvalOperator;`
- Line 44: `import org.elasticsearch.compute.operator.HashAggregationOperator;`
- Line 45: `import org.elasticsearch.compute.operator.Operator;`
- Line 46: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 47: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 48: `import org.openjdk.jmh.annotations.Fork;`
- Line 49: `import org.openjdk.jmh.annotations.Measurement;`
- Line 50: `import org.openjdk.jmh.annotations.Mode;`
- Line 51: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 52: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 53: `import org.openjdk.jmh.annotations.Param;`
- Line 54: `import org.openjdk.jmh.annotations.Scope;`
- Line 55: `import org.openjdk.jmh.annotations.State;`
- Line 56: `import org.openjdk.jmh.annotations.Warmup;`
- Line 58: `import java.util.List;`
- Line 59: `import java.util.concurrent.TimeUnit;`
- Line 60: `import java.util.stream.LongStream;`
- Line 61: `import java.util.stream.Stream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockBenchmark.java

### Concurrency Issue (5)
- Line 81: `public static final int NUM_BLOCKS_PER_ITERATION = 1024;`
- Line 82: `public static final int BLOCK_TOTAL_POSITIONS = 8096;`
- Line 84: `private static final double MV_PERCENTAGE = 0.3;`
- Line 85: `private static final double NULL_PERCENTAGE = 0.1;`
- Line 86: `private static final int MAX_MV_ELEMENTS = 100;`

### Exception Handling (6)
- Line 185: `throw new IllegalStateException("illegal block kind [" + blockKind + "]");`
- Line 237: `throw new IllegalStateException("illegal block kind [" + blockKind + "]");`
- Line 324: `throw new IllegalStateException("illegal block kind [" + blockKind + "]");`
- Line 411: `throw new IllegalStateException("illegal block kind [" + blockKind + "]");`
- Line 498: `throw new IllegalStateException("illegal block kind [" + blockKind + "]");`
- Line 504: `throw new IllegalStateException("illegal data type [" + dataType + "]");`

### Unused Code (27)
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 14: `import org.elasticsearch.common.util.BigArrays;`
- Line 15: `import org.elasticsearch.common.util.BitArray;`
- Line 16: `import org.elasticsearch.common.util.BytesRefArray;`
- Line 17: `import org.elasticsearch.common.util.DoubleArray;`
- Line 18: `import org.elasticsearch.common.util.IntArray;`
- Line 19: `import org.elasticsearch.common.util.LongArray;`
- Line 20: `import org.elasticsearch.compute.data.Block;`
- Line 21: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 22: `import org.elasticsearch.compute.data.BooleanBigArrayBlock;`
- Line 23: `import org.elasticsearch.compute.data.BooleanBigArrayVector;`
- Line 24: `import org.elasticsearch.compute.data.BooleanVector;`
- Line 25: `import org.elasticsearch.compute.data.BytesRefVector;`
- Line 26: `import org.elasticsearch.compute.data.DoubleBigArrayBlock;`
- Line 27: `import org.elasticsearch.compute.data.DoubleBigArrayVector;`
- Line 28: `import org.elasticsearch.compute.data.DoubleVector;`
- Line 29: `import org.elasticsearch.compute.data.IntBigArrayBlock;`
- Line 30: `import org.elasticsearch.compute.data.IntBigArrayVector;`
- Line 31: `import org.elasticsearch.compute.data.IntBlock;`
- Line 32: `import org.elasticsearch.compute.data.IntVector;`
- Line 33: `import org.elasticsearch.compute.data.LongBigArrayBlock;`
- Line 34: `import org.elasticsearch.compute.data.LongBigArrayVector;`
- Line 35: `import org.elasticsearch.compute.data.LongVector;`
- Line 37: `import java.util.ArrayList;`
- Line 38: `import java.util.BitSet;`
- Line 39: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockKeepMaskBenchmark.java

### Concurrency Issue (1)
- Line 270: `private final BooleanVector mask = buildMask(BLOCK_TOTAL_POSITIONS);`

### Exception Handling (1)
- Line 101: `default -> throw new IllegalStateException("illegal data type [" + dataType + "]");`

### Unused Code (24)
- Line 268: `private BenchmarkBlocks data;`
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.compute.data.Block;`
- Line 14: `import org.elasticsearch.compute.data.BooleanBlock;`
- Line 15: `import org.elasticsearch.compute.data.BooleanVector;`
- Line 16: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 17: `import org.elasticsearch.compute.data.DoubleBlock;`
- Line 18: `import org.elasticsearch.compute.data.IntBlock;`
- Line 19: `import org.elasticsearch.compute.data.LongBlock;`
- Line 20: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 21: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 22: `import org.openjdk.jmh.annotations.Fork;`
- Line 23: `import org.openjdk.jmh.annotations.Level;`
- Line 24: `import org.openjdk.jmh.annotations.Measurement;`
- Line 25: `import org.openjdk.jmh.annotations.Mode;`
- Line 26: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 27: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 28: `import org.openjdk.jmh.annotations.Param;`
- Line 29: `import org.openjdk.jmh.annotations.Scope;`
- Line 30: `import org.openjdk.jmh.annotations.Setup;`
- Line 31: `import org.openjdk.jmh.annotations.State;`
- Line 32: `import org.openjdk.jmh.annotations.TearDown;`
- Line 33: `import org.openjdk.jmh.annotations.Warmup;`
- Line 35: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/BlockReadBenchmark.java

### Exception Handling (2)
- Line 100: `default -> throw new IllegalStateException("illegal data type [" + dataType + "]");`
- Line 143: `throw new IllegalStateException();`

### Unused Code (8)
- Line 291: `private BenchmarkBlocks data;`
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.util.*;`
- Line 14: `import org.elasticsearch.compute.data.*;`
- Line 15: `import org.openjdk.jmh.annotations.*;`
- Line 17: `import java.util.*;`
- Line 18: `import java.util.concurrent.TimeUnit;`
- Line 19: `import java.util.stream.IntStream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/EvalBenchmark.java

### Concurrency Issue (2)
- Line 83: `private static final BlockFactory blockFactory = BlockFactory.getInstance(`
- Line 88: `private static final FoldContext FOLD_CONTEXT = FoldContext.small();`

### Exception Handling (5)
- Line 177: `throw new IllegalArgumentException("Evaluator was [" + evaluator + "] but expected one containing [" + desc + "]");`
- Line 195: `throw new IllegalArgumentException("Evaluator was [" + evaluator + "] but expected one containing [" + desc + "]");`
- Line 248: `default -> throw new UnsupportedOperationException();`
- Line 419: `default -> throw new UnsupportedOperationException(operation);`
- Line 513: `default -> throw new UnsupportedOperationException();`

### Unused Code (62)
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 14: `import org.elasticsearch.common.logging.LogConfigurator;`
- Line 15: `import org.elasticsearch.common.settings.Settings;`
- Line 16: `import org.elasticsearch.common.util.BigArrays;`
- Line 17: `import org.elasticsearch.compute.data.Block;`
- Line 18: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 19: `import org.elasticsearch.compute.data.BooleanBlock;`
- Line 20: `import org.elasticsearch.compute.data.BooleanVector;`
- Line 21: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 22: `import org.elasticsearch.compute.data.BytesRefVector;`
- Line 23: `import org.elasticsearch.compute.data.DoubleBlock;`
- Line 24: `import org.elasticsearch.compute.data.DoubleVector;`
- Line 25: `import org.elasticsearch.compute.data.LongBlock;`
- Line 26: `import org.elasticsearch.compute.data.LongVector;`
- Line 27: `import org.elasticsearch.compute.data.Page;`
- Line 28: `import org.elasticsearch.compute.operator.DriverContext;`
- Line 29: `import org.elasticsearch.compute.operator.EvalOperator;`
- Line 30: `import org.elasticsearch.compute.operator.Operator;`
- Line 31: `import org.elasticsearch.core.TimeValue;`
- Line 32: `import org.elasticsearch.logging.LogManager;`
- Line 33: `import org.elasticsearch.logging.Logger;`
- Line 34: `import org.elasticsearch.xpack.esql.core.expression.Expression;`
- Line 35: `import org.elasticsearch.xpack.esql.core.expression.FieldAttribute;`
- Line 36: `import org.elasticsearch.xpack.esql.core.expression.FoldContext;`
- Line 37: `import org.elasticsearch.xpack.esql.core.expression.Literal;`
- Line 38: `import org.elasticsearch.xpack.esql.core.expression.predicate.regex.RLikePattern;`
- Line 39: `import org.elasticsearch.xpack.esql.core.tree.Source;`
- Line 40: `import org.elasticsearch.xpack.esql.core.type.DataType;`
- Line 41: `import org.elasticsearch.xpack.esql.core.type.EsField;`
- Line 42: `import org.elasticsearch.xpack.esql.evaluator.EvalMapper;`
- Line 43: `import org.elasticsearch.xpack.esql.expression.function.scalar.conditional.Case;`
- Line 44: `import org.elasticsearch.xpack.esql.expression.function.scalar.date.DateTrunc;`
- Line 45: `import org.elasticsearch.xpack.esql.expression.function.scalar.math.Abs;`
- Line 46: `import org.elasticsearch.xpack.esql.expression.function.scalar.multivalue.MvMin;`
- Line 47: `import org.elasticsearch.xpack.esql.expression.function.scalar.nulls.Coalesce;`
- Line 48: `import org.elasticsearch.xpack.esql.expression.function.scalar.string.RLike;`
- Line 49: `import org.elasticsearch.xpack.esql.expression.function.scalar.string.ToLower;`
- Line 50: `import org.elasticsearch.xpack.esql.expression.function.scalar.string.ToUpper;`
- Line 51: `import org.elasticsearch.xpack.esql.expression.predicate.operator.arithmetic.Add;`
- Line 52: `import org.elasticsearch.xpack.esql.expression.predicate.operator.comparison.Equals;`
- Line 53: `import org.elasticsearch.xpack.esql.planner.Layout;`
- Line 54: `import org.elasticsearch.xpack.esql.plugin.EsqlPlugin;`
- Line 55: `import org.elasticsearch.xpack.esql.session.Configuration;`
- Line 56: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 57: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 58: `import org.openjdk.jmh.annotations.Fork;`
- Line 59: `import org.openjdk.jmh.annotations.Measurement;`
- Line 60: `import org.openjdk.jmh.annotations.Mode;`
- Line 61: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 62: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 63: `import org.openjdk.jmh.annotations.Param;`
- Line 64: `import org.openjdk.jmh.annotations.Scope;`
- Line 65: `import org.openjdk.jmh.annotations.State;`
- Line 66: `import org.openjdk.jmh.annotations.Warmup;`
- Line 68: `import java.time.Duration;`
- Line 69: `import java.time.ZoneOffset;`
- Line 70: `import java.util.Arrays;`
- Line 71: `import java.util.List;`
- Line 72: `import java.util.Locale;`
- Line 73: `import java.util.Map;`
- Line 74: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/MultivalueDedupeBenchmark.java

### Concurrency Issue (1)
- Line 66: `public void setup() {`

### Exception Handling (1)
- Line 163: `default -> throw new IllegalArgumentException();`

### Unused Code (32)
- Line 55: `private ElementType elementType;`
- Line 58: `private int size;`
- Line 61: `private int repeats;`
- Line 63: `private Block block;`
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.Randomness;`
- Line 14: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 15: `import org.elasticsearch.common.util.BigArrays;`
- Line 16: `import org.elasticsearch.compute.data.Block;`
- Line 17: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 18: `import org.elasticsearch.compute.data.BooleanBlock;`
- Line 19: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 20: `import org.elasticsearch.compute.data.DoubleBlock;`
- Line 21: `import org.elasticsearch.compute.data.ElementType;`
- Line 22: `import org.elasticsearch.compute.data.IntBlock;`
- Line 23: `import org.elasticsearch.compute.data.LongBlock;`
- Line 24: `import org.elasticsearch.compute.operator.mvdedupe.MultivalueDedupe;`
- Line 25: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 26: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 27: `import org.openjdk.jmh.annotations.Fork;`
- Line 28: `import org.openjdk.jmh.annotations.Measurement;`
- Line 29: `import org.openjdk.jmh.annotations.Mode;`
- Line 30: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 31: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 32: `import org.openjdk.jmh.annotations.Param;`
- Line 33: `import org.openjdk.jmh.annotations.Scope;`
- Line 34: `import org.openjdk.jmh.annotations.Setup;`
- Line 35: `import org.openjdk.jmh.annotations.State;`
- Line 36: `import org.openjdk.jmh.annotations.Warmup;`
- Line 38: `import java.util.ArrayList;`
- Line 39: `import java.util.List;`
- Line 40: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/TopNBenchmark.java

### Concurrency Issue (9)
- Line 54: `private static final BigArrays BIG_ARRAYS = BigArrays.NON_RECYCLING_INSTANCE;  // TODO real big arrays?`
- Line 55: `private static final BlockFactory blockFactory = BlockFactory.getInstance(`
- Line 60: `private static final int BLOCK_LENGTH = 8 * 1024;`
- Line 62: `private static final String LONGS = "longs";`
- Line 63: `private static final String INTS = "ints";`
- Line 64: `private static final String DOUBLES = "doubles";`
- Line 65: `private static final String BOOLEANS = "booleans";`
- Line 66: `private static final String BYTES_REFS = "bytes_refs";`
- Line 67: `private static final String TWO_LONGS = "two_" + LONGS;`

### Exception Handling (4)
- Line 93: `default -> throw new IllegalArgumentException("unsupported data type [" + data + "]");`
- Line 103: `default -> throw new IllegalArgumentException("unsupported data type [" + data + "]");`
- Line 110: `default -> throw new IllegalArgumentException("unsupported data type [" + data + "]");`
- Line 180: `default -> throw new UnsupportedOperationException("unsupported data [" + data + "]");`

### Unused Code (33)
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.breaker.CircuitBreaker;`
- Line 14: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 15: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 16: `import org.elasticsearch.common.settings.Settings;`
- Line 17: `import org.elasticsearch.common.util.BigArrays;`
- Line 18: `import org.elasticsearch.compute.data.Block;`
- Line 19: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 20: `import org.elasticsearch.compute.data.BooleanBlock;`
- Line 21: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 22: `import org.elasticsearch.compute.data.ElementType;`
- Line 23: `import org.elasticsearch.compute.data.Page;`
- Line 24: `import org.elasticsearch.compute.operator.Operator;`
- Line 25: `import org.elasticsearch.compute.operator.topn.TopNEncoder;`
- Line 26: `import org.elasticsearch.compute.operator.topn.TopNOperator;`
- Line 27: `import org.elasticsearch.indices.breaker.CircuitBreakerMetrics;`
- Line 28: `import org.elasticsearch.indices.breaker.CircuitBreakerService;`
- Line 29: `import org.elasticsearch.indices.breaker.HierarchyCircuitBreakerService;`
- Line 30: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 31: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 32: `import org.openjdk.jmh.annotations.Fork;`
- Line 33: `import org.openjdk.jmh.annotations.Measurement;`
- Line 34: `import org.openjdk.jmh.annotations.Mode;`
- Line 35: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 36: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 37: `import org.openjdk.jmh.annotations.Param;`
- Line 38: `import org.openjdk.jmh.annotations.Scope;`
- Line 39: `import org.openjdk.jmh.annotations.State;`
- Line 40: `import org.openjdk.jmh.annotations.Warmup;`
- Line 42: `import java.util.ArrayList;`
- Line 43: `import java.util.List;`
- Line 44: `import java.util.concurrent.TimeUnit;`
- Line 45: `import java.util.stream.IntStream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/ValuesAggregatorBenchmark.java

### Concurrency Issue (5)
- Line 64: `static final int MIN_BLOCK_LENGTH = 8 * 1024;`
- Line 65: `private static final int OP_COUNT = 1024;`
- Line 66: `private static final int UNIQUE_VALUES = 6;`
- Line 96: `private static final String BYTES_REF = "BytesRef";`
- Line 97: `private static final String INT = "int";`

### Exception Handling (9)
- Line 126: `default -> throw new IllegalArgumentException("unsupported data type [" + dataType + "]");`
- Line 134: `throw new IllegalArgumentException(prefix + " expected " + groups + " positions, got " + positions);`
- Line 148: `throw new IllegalArgumentException(prefix + "[" + p + "] expected group " + p + " but was " + groups);`
- Line 203: `default -> throw new IllegalArgumentException(prefix + " unsupported data type " + dataType);`
- Line 221: `default -> throw new IllegalArgumentException(prefix + " unsupported data type " + dataType);`
- Line 241: `throw new IllegalArgumentException(prefix + "[" + position + "] expected " + v + " to be in " + expected);`
- Line 251: `throw new IllegalArgumentException(prefix + "[" + position + "] expected " + v + " to be in " + expected);`
- Line 261: `throw new IllegalArgumentException(prefix + "[" + position + "] expected " + v + " to be in " + expected);`
- Line 301: `default -> throw new IllegalArgumentException("unsupported data type " + dataType);`

### Unused Code (39)
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 14: `import org.elasticsearch.common.util.BigArrays;`
- Line 15: `import org.elasticsearch.compute.aggregation.AggregatorFunctionSupplier;`
- Line 16: `import org.elasticsearch.compute.aggregation.AggregatorMode;`
- Line 17: `import org.elasticsearch.compute.aggregation.ValuesBytesRefAggregatorFunctionSupplier;`
- Line 18: `import org.elasticsearch.compute.aggregation.ValuesIntAggregatorFunctionSupplier;`
- Line 19: `import org.elasticsearch.compute.aggregation.ValuesLongAggregatorFunctionSupplier;`
- Line 20: `import org.elasticsearch.compute.aggregation.blockhash.BlockHash;`
- Line 21: `import org.elasticsearch.compute.data.Block;`
- Line 22: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 23: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 24: `import org.elasticsearch.compute.data.ElementType;`
- Line 25: `import org.elasticsearch.compute.data.IntBlock;`
- Line 26: `import org.elasticsearch.compute.data.LongBlock;`
- Line 27: `import org.elasticsearch.compute.data.LongVector;`
- Line 28: `import org.elasticsearch.compute.data.Page;`
- Line 29: `import org.elasticsearch.compute.operator.AggregationOperator;`
- Line 30: `import org.elasticsearch.compute.operator.DriverContext;`
- Line 31: `import org.elasticsearch.compute.operator.HashAggregationOperator;`
- Line 32: `import org.elasticsearch.compute.operator.Operator;`
- Line 33: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 34: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 35: `import org.openjdk.jmh.annotations.Fork;`
- Line 36: `import org.openjdk.jmh.annotations.Measurement;`
- Line 37: `import org.openjdk.jmh.annotations.Mode;`
- Line 38: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 39: `import org.openjdk.jmh.annotations.Param;`
- Line 40: `import org.openjdk.jmh.annotations.Scope;`
- Line 41: `import org.openjdk.jmh.annotations.State;`
- Line 42: `import org.openjdk.jmh.annotations.Warmup;`
- Line 44: `import java.util.ArrayList;`
- Line 45: `import java.util.HashSet;`
- Line 46: `import java.util.List;`
- Line 47: `import java.util.Set;`
- Line 48: `import java.util.concurrent.TimeUnit;`
- Line 49: `import java.util.stream.Collectors;`
- Line 50: `import java.util.stream.IntStream;`
- Line 51: `import java.util.stream.LongStream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/compute/operator/ValuesSourceReaderBenchmark.java

### Concurrency Issue (4)
- Line 84: `private static final int BLOCK_LENGTH = 16 * 1024;`
- Line 85: `private static final int INDEX_SIZE = 10 * BLOCK_LENGTH;`
- Line 86: `private static final int COMMIT_INTERVAL = 500;`
- Line 87: `private static final BigArrays BIG_ARRAYS = BigArrays.NON_RECYCLING_INSTANCE;`

### Exception Handling (8)
- Line 149: `throw new UnsupportedOperationException("no element type for [" + name + "]");`
- Line 196: `throw new UnsupportedOperationException();`
- Line 206: `throw new UnsupportedOperationException();`
- Line 216: `throw new UnsupportedOperationException();`
- Line 225: `throw new IllegalArgumentException("can't read [" + name + "]");`
- Line 250: `throw new UnsupportedOperationException();`
- Line 298: `throw new UnsupportedOperationException("can't load _source here");`
- Line 523: `default -> throw new IllegalArgumentException("unsupported layout [" + layout + "]");`

### Unused Code (65)
- Line 287: `private Directory directory;`
- Line 288: `private IndexReader reader;`
- Line 12: `import org.apache.lucene.document.FieldType;`
- Line 13: `import org.apache.lucene.document.NumericDocValuesField;`
- Line 14: `import org.apache.lucene.document.StoredField;`
- Line 15: `import org.apache.lucene.index.DirectoryReader;`
- Line 16: `import org.apache.lucene.index.DocValuesType;`
- Line 17: `import org.apache.lucene.index.IndexReader;`
- Line 18: `import org.apache.lucene.index.IndexWriter;`
- Line 19: `import org.apache.lucene.index.IndexWriterConfig;`
- Line 20: `import org.apache.lucene.index.LeafReaderContext;`
- Line 21: `import org.apache.lucene.index.NoMergePolicy;`
- Line 22: `import org.apache.lucene.store.ByteBuffersDirectory;`
- Line 23: `import org.apache.lucene.store.Directory;`
- Line 24: `import org.apache.lucene.util.BytesRef;`
- Line 25: `import org.apache.lucene.util.NumericUtils;`
- Line 26: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 27: `import org.elasticsearch.common.lucene.Lucene;`
- Line 28: `import org.elasticsearch.common.util.BigArrays;`
- Line 29: `import org.elasticsearch.compute.data.BlockFactory;`
- Line 30: `import org.elasticsearch.compute.data.BytesRefBlock;`
- Line 31: `import org.elasticsearch.compute.data.BytesRefVector;`
- Line 32: `import org.elasticsearch.compute.data.DocVector;`
- Line 33: `import org.elasticsearch.compute.data.DoubleBlock;`
- Line 34: `import org.elasticsearch.compute.data.DoubleVector;`
- Line 35: `import org.elasticsearch.compute.data.ElementType;`
- Line 36: `import org.elasticsearch.compute.data.IntBlock;`
- Line 37: `import org.elasticsearch.compute.data.IntVector;`
- Line 38: `import org.elasticsearch.compute.data.LongBlock;`
- Line 39: `import org.elasticsearch.compute.data.LongVector;`
- Line 40: `import org.elasticsearch.compute.data.Page;`
- Line 41: `import org.elasticsearch.compute.lucene.LuceneSourceOperator;`
- Line 42: `import org.elasticsearch.compute.lucene.ValuesSourceReaderOperator;`
- Line 43: `import org.elasticsearch.compute.operator.topn.TopNOperator;`
- Line 44: `import org.elasticsearch.core.IOUtils;`
- Line 45: `import org.elasticsearch.index.IndexSettings;`
- Line 46: `import org.elasticsearch.index.IndexVersion;`
- Line 47: `import org.elasticsearch.index.mapper.BlockLoader;`
- Line 48: `import org.elasticsearch.index.mapper.FieldNamesFieldMapper;`
- Line 49: `import org.elasticsearch.index.mapper.KeywordFieldMapper;`
- Line 50: `import org.elasticsearch.index.mapper.MappedFieldType;`
- Line 51: `import org.elasticsearch.index.mapper.NumberFieldMapper;`
- Line 52: `import org.elasticsearch.search.lookup.SearchLookup;`
- Line 53: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 54: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 55: `import org.openjdk.jmh.annotations.Fork;`
- Line 56: `import org.openjdk.jmh.annotations.Measurement;`
- Line 57: `import org.openjdk.jmh.annotations.Mode;`
- Line 58: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 59: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 60: `import org.openjdk.jmh.annotations.Param;`
- Line 61: `import org.openjdk.jmh.annotations.Scope;`
- Line 62: `import org.openjdk.jmh.annotations.Setup;`
- Line 63: `import org.openjdk.jmh.annotations.State;`
- Line 64: `import org.openjdk.jmh.annotations.TearDown;`
- Line 65: `import org.openjdk.jmh.annotations.Warmup;`
- Line 67: `import java.io.IOException;`
- Line 68: `import java.util.ArrayList;`
- Line 69: `import java.util.Iterator;`
- Line 70: `import java.util.List;`
- Line 71: `import java.util.Map;`
- Line 72: `import java.util.PrimitiveIterator;`
- Line 73: `import java.util.Set;`
- Line 74: `import java.util.concurrent.TimeUnit;`
- Line 75: `import java.util.stream.IntStream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/fs/AvailableIndexFoldersBenchmark.java

### Exception Handling (2)
- Line 67: `throw new IllegalStateException("bad size");`
- Line 70: `throw new IllegalStateException("bad size");`

### Unused Code (21)
- Line 42: `private NodeEnvironment nodeEnv;`
- Line 11: `import org.elasticsearch.common.logging.LogConfigurator;`
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.env.Environment;`
- Line 14: `import org.elasticsearch.env.NodeEnvironment;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Measurement;`
- Line 19: `import org.openjdk.jmh.annotations.Mode;`
- Line 20: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 21: `import org.openjdk.jmh.annotations.Scope;`
- Line 22: `import org.openjdk.jmh.annotations.Setup;`
- Line 23: `import org.openjdk.jmh.annotations.State;`
- Line 24: `import org.openjdk.jmh.annotations.Warmup;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.nio.file.Files;`
- Line 28: `import java.nio.file.Path;`
- Line 29: `import java.util.HashSet;`
- Line 30: `import java.util.Set;`
- Line 31: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/h3/H3Benchmark.java

### Unused Code (9)
- Line 11: `import org.elasticsearch.h3.H3;`
- Line 12: `import org.openjdk.jmh.Main;`
- Line 13: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 14: `import org.openjdk.jmh.annotations.Fork;`
- Line 15: `import org.openjdk.jmh.annotations.Measurement;`
- Line 16: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 17: `import org.openjdk.jmh.annotations.Warmup;`
- Line 18: `import org.openjdk.jmh.infra.Blackhole;`
- Line 20: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/h3/H3State.java

### Unused Code (7)
- Line 11: `import org.elasticsearch.h3.H3;`
- Line 12: `import org.openjdk.jmh.annotations.Level;`
- Line 13: `import org.openjdk.jmh.annotations.Scope;`
- Line 14: `import org.openjdk.jmh.annotations.Setup;`
- Line 15: `import org.openjdk.jmh.annotations.State;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/DecodeConstantIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.ConstantIntegerSupplier;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecodeBenchmark;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/DecodeDecreasingIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecodeBenchmark;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecreasingIntegerSupplier;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/DecodeIncreasingIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecodeBenchmark;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.IncreasingIntegerSupplier;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/DecodeNonSortedIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecodeBenchmark;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.NonSortedIntegerSupplier;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/EncodeConstantIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.ConstantIntegerSupplier;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.EncodeBenchmark;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/EncodeDecreasingIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.DecreasingIntegerSupplier;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.EncodeBenchmark;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/EncodeIncreasingIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.EncodeBenchmark;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.IncreasingIntegerSupplier;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/EncodeNonSortedIntegerBenchmark.java

### Concurrency Issue (1)
- Line 39: `private static final int SEED = 17;`

### Unused Code (19)
- Line 42: `private int bitsPerValue;`
- Line 12: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.AbstractDocValuesForUtilBenchmark;`
- Line 13: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.EncodeBenchmark;`
- Line 14: `import org.elasticsearch.benchmark.index.codec.tsdb.internal.NonSortedIntegerSupplier;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Level;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/AbstractDocValuesForUtilBenchmark.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.index.codec.tsdb.DocValuesForUtil;`
- Line 13: `import org.elasticsearch.index.codec.tsdb.ES87TSDBDocValuesFormat;`
- Line 14: `import org.openjdk.jmh.infra.Blackhole;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/AbstractLongArraySupplier.java

### Unused Code (1)
- Line 12: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/ConstantIntegerSupplier.java

### Unused Code (2)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/DecodeBenchmark.java

### Unused Code (6)
- Line 12: `import org.apache.lucene.store.ByteArrayDataInput;`
- Line 13: `import org.apache.lucene.store.ByteArrayDataOutput;`
- Line 14: `import org.apache.lucene.store.DataOutput;`
- Line 15: `import org.openjdk.jmh.infra.Blackhole;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/DecreasingIntegerSupplier.java

### Unused Code (3)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.Collections;`
- Line 14: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/EncodeBenchmark.java

### Unused Code (4)
- Line 12: `import org.apache.lucene.store.ByteArrayDataOutput;`
- Line 13: `import org.openjdk.jmh.infra.Blackhole;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/IncreasingIntegerSupplier.java

### Unused Code (2)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/codec/tsdb/internal/NonSortedIntegerSupplier.java

### Unused Code (1)
- Line 12: `import java.util.Random;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/mapper/BeatsMapperBenchmark.java

### Unused Code (26)
- Line 47: `private long seed;`
- Line 49: `private Random random;`
- Line 50: `private MapperService mapperService;`
- Line 12: `import org.elasticsearch.common.UUIDs;`
- Line 13: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 14: `import org.elasticsearch.index.mapper.LuceneDocument;`
- Line 15: `import org.elasticsearch.index.mapper.MapperService;`
- Line 16: `import org.elasticsearch.index.mapper.SourceToParse;`
- Line 17: `import org.elasticsearch.xcontent.XContentType;`
- Line 18: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 19: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 20: `import org.openjdk.jmh.annotations.Fork;`
- Line 21: `import org.openjdk.jmh.annotations.Measurement;`
- Line 22: `import org.openjdk.jmh.annotations.Mode;`
- Line 23: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 24: `import org.openjdk.jmh.annotations.Param;`
- Line 25: `import org.openjdk.jmh.annotations.Scope;`
- Line 26: `import org.openjdk.jmh.annotations.Setup;`
- Line 27: `import org.openjdk.jmh.annotations.State;`
- Line 28: `import org.openjdk.jmh.annotations.Warmup;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Random;`
- Line 33: `import java.util.concurrent.TimeUnit;`
- Line 34: `import java.util.zip.GZIPInputStream;`
- Line 36: `import static java.nio.charset.StandardCharsets.UTF_8;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/mapper/DynamicMapperBenchmark.java

### Concurrency Issue (1)
- Line 59: `public void setUp() {`

### Unused Code (32)
- Line 53: `private long seed;`
- Line 55: `private Random random;`
- Line 12: `import org.elasticsearch.common.UUIDs;`
- Line 13: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 14: `import org.elasticsearch.common.compress.CompressedXContent;`
- Line 15: `import org.elasticsearch.common.xcontent.XContentHelper;`
- Line 16: `import org.elasticsearch.index.mapper.DocumentMapper;`
- Line 17: `import org.elasticsearch.index.mapper.LuceneDocument;`
- Line 18: `import org.elasticsearch.index.mapper.MapperService;`
- Line 19: `import org.elasticsearch.index.mapper.Mapping;`
- Line 20: `import org.elasticsearch.index.mapper.ParsedDocument;`
- Line 21: `import org.elasticsearch.index.mapper.SourceToParse;`
- Line 22: `import org.elasticsearch.xcontent.XContentType;`
- Line 23: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 24: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 25: `import org.openjdk.jmh.annotations.Fork;`
- Line 26: `import org.openjdk.jmh.annotations.Measurement;`
- Line 27: `import org.openjdk.jmh.annotations.Mode;`
- Line 28: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 29: `import org.openjdk.jmh.annotations.Param;`
- Line 30: `import org.openjdk.jmh.annotations.Scope;`
- Line 31: `import org.openjdk.jmh.annotations.Setup;`
- Line 32: `import org.openjdk.jmh.annotations.State;`
- Line 33: `import org.openjdk.jmh.annotations.Warmup;`
- Line 35: `import java.util.Arrays;`
- Line 36: `import java.util.List;`
- Line 37: `import java.util.Random;`
- Line 38: `import java.util.concurrent.TimeUnit;`
- Line 39: `import java.util.stream.Collectors;`
- Line 40: `import java.util.stream.DoubleStream;`
- Line 41: `import java.util.stream.IntStream;`
- Line 42: `import java.util.stream.Stream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/mapper/KeywordFieldMapperBenchmark.java

### Concurrency Issue (1)
- Line 45: `public void setUp() {`

### Unused Code (20)
- Line 40: `private MapperService mapperService;`
- Line 42: `private SourceToParse sourceToParse;`
- Line 12: `import org.elasticsearch.common.UUIDs;`
- Line 13: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 14: `import org.elasticsearch.index.mapper.LuceneDocument;`
- Line 15: `import org.elasticsearch.index.mapper.MapperService;`
- Line 16: `import org.elasticsearch.index.mapper.SourceToParse;`
- Line 17: `import org.elasticsearch.xcontent.XContentType;`
- Line 18: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 19: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 20: `import org.openjdk.jmh.annotations.Fork;`
- Line 21: `import org.openjdk.jmh.annotations.Measurement;`
- Line 22: `import org.openjdk.jmh.annotations.Mode;`
- Line 23: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 24: `import org.openjdk.jmh.annotations.Scope;`
- Line 25: `import org.openjdk.jmh.annotations.Setup;`
- Line 26: `import org.openjdk.jmh.annotations.State;`
- Line 27: `import org.openjdk.jmh.annotations.Warmup;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/index/mapper/MapperServiceFactory.java

### Exception Handling (3)
- Line 70: `throw new UnsupportedOperationException();`
- Line 76: `throw new UnsupportedOperationException();`
- Line 87: `throw new UncheckedIOException(e);`

### Unused Code (29)
- Line 12: `import org.apache.lucene.analysis.standard.StandardAnalyzer;`
- Line 13: `import org.elasticsearch.TransportVersion;`
- Line 14: `import org.elasticsearch.cluster.ClusterModule;`
- Line 15: `import org.elasticsearch.cluster.metadata.IndexMetadata;`
- Line 16: `import org.elasticsearch.common.compress.CompressedXContent;`
- Line 17: `import org.elasticsearch.common.settings.Settings;`
- Line 18: `import org.elasticsearch.common.xcontent.LoggingDeprecationHandler;`
- Line 19: `import org.elasticsearch.index.IndexSettings;`
- Line 20: `import org.elasticsearch.index.IndexVersion;`
- Line 21: `import org.elasticsearch.index.analysis.AnalyzerScope;`
- Line 22: `import org.elasticsearch.index.analysis.IndexAnalyzers;`
- Line 23: `import org.elasticsearch.index.analysis.LowercaseNormalizer;`
- Line 24: `import org.elasticsearch.index.analysis.NamedAnalyzer;`
- Line 25: `import org.elasticsearch.index.cache.bitset.BitsetFilterCache;`
- Line 26: `import org.elasticsearch.index.mapper.MapperMetrics;`
- Line 27: `import org.elasticsearch.index.mapper.MapperRegistry;`
- Line 28: `import org.elasticsearch.index.mapper.MapperService;`
- Line 29: `import org.elasticsearch.index.mapper.ProvidedIdFieldMapper;`
- Line 30: `import org.elasticsearch.index.similarity.SimilarityService;`
- Line 31: `import org.elasticsearch.indices.IndicesModule;`
- Line 32: `import org.elasticsearch.script.Script;`
- Line 33: `import org.elasticsearch.script.ScriptCompiler;`
- Line 34: `import org.elasticsearch.script.ScriptContext;`
- Line 35: `import org.elasticsearch.xcontent.NamedXContentRegistry;`
- Line 36: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 38: `import java.io.IOException;`
- Line 39: `import java.io.UncheckedIOException;`
- Line 40: `import java.util.Collections;`
- Line 41: `import java.util.Map;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/indices/breaker/MemoryStatsBenchmark.java

### Unused Code (16)
- Line 39: `private int tokens;`
- Line 11: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 12: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 13: `import org.openjdk.jmh.annotations.Fork;`
- Line 14: `import org.openjdk.jmh.annotations.Measurement;`
- Line 15: `import org.openjdk.jmh.annotations.Mode;`
- Line 16: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 17: `import org.openjdk.jmh.annotations.Param;`
- Line 18: `import org.openjdk.jmh.annotations.Scope;`
- Line 19: `import org.openjdk.jmh.annotations.State;`
- Line 20: `import org.openjdk.jmh.annotations.Threads;`
- Line 21: `import org.openjdk.jmh.annotations.Warmup;`
- Line 22: `import org.openjdk.jmh.infra.Blackhole;`
- Line 24: `import java.lang.management.ManagementFactory;`
- Line 25: `import java.lang.management.MemoryMXBean;`
- Line 26: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/indices/common/RoundingBenchmark.java

### Exception Handling (2)
- Line 79: `throw new IllegalStateException("made a bad date [" + date + "]");`
- Line 96: `default -> throw new IllegalArgumentException("Expected rounder to be [java time] or [es]");`

### Unused Code (21)
- Line 64: `private long min;`
- Line 65: `private long max;`
- Line 12: `import org.elasticsearch.common.Rounding;`
- Line 13: `import org.elasticsearch.common.time.DateFormatter;`
- Line 14: `import org.elasticsearch.core.TimeValue;`
- Line 15: `import org.elasticsearch.search.aggregations.bucket.histogram.DateHistogramAggregationBuilder;`
- Line 16: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 17: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 18: `import org.openjdk.jmh.annotations.Fork;`
- Line 19: `import org.openjdk.jmh.annotations.Measurement;`
- Line 20: `import org.openjdk.jmh.annotations.Mode;`
- Line 21: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 22: `import org.openjdk.jmh.annotations.Param;`
- Line 23: `import org.openjdk.jmh.annotations.Scope;`
- Line 24: `import org.openjdk.jmh.annotations.Setup;`
- Line 25: `import org.openjdk.jmh.annotations.State;`
- Line 26: `import org.openjdk.jmh.annotations.Warmup;`
- Line 27: `import org.openjdk.jmh.infra.Blackhole;`
- Line 29: `import java.time.ZoneId;`
- Line 30: `import java.util.concurrent.TimeUnit;`
- Line 31: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/indices/resolution/IndexNameExpressionResolverBenchmark.java

### Concurrency Issue (1)
- Line 47: `private static final String DATA_STREAM_PREFIX = "my-ds-";`

### Unused Code (31)
- Line 110: `private IndexNameExpressionResolver resolver;`
- Line 111: `private ClusterState clusterState;`
- Line 112: `private Request starRequest;`
- Line 113: `private Request indexListRequest;`
- Line 114: `private Request mixedRequest;`
- Line 12: `import org.elasticsearch.action.IndicesRequest;`
- Line 13: `import org.elasticsearch.action.support.IndicesOptions;`
- Line 14: `import org.elasticsearch.cluster.ClusterName;`
- Line 15: `import org.elasticsearch.cluster.ClusterState;`
- Line 16: `import org.elasticsearch.cluster.metadata.DataStream;`
- Line 17: `import org.elasticsearch.cluster.metadata.IndexMetadata;`
- Line 18: `import org.elasticsearch.cluster.metadata.IndexNameExpressionResolver;`
- Line 19: `import org.elasticsearch.cluster.metadata.Metadata;`
- Line 20: `import org.elasticsearch.cluster.project.DefaultProjectResolver;`
- Line 21: `import org.elasticsearch.common.settings.Settings;`
- Line 22: `import org.elasticsearch.common.util.concurrent.ThreadContext;`
- Line 23: `import org.elasticsearch.index.Index;`
- Line 24: `import org.elasticsearch.index.IndexVersion;`
- Line 25: `import org.elasticsearch.indices.SystemIndices;`
- Line 26: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 27: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 28: `import org.openjdk.jmh.annotations.Fork;`
- Line 29: `import org.openjdk.jmh.annotations.Mode;`
- Line 30: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 31: `import org.openjdk.jmh.annotations.Param;`
- Line 32: `import org.openjdk.jmh.annotations.Scope;`
- Line 33: `import org.openjdk.jmh.annotations.Setup;`
- Line 34: `import org.openjdk.jmh.annotations.State;`
- Line 36: `import java.util.ArrayList;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/routing/allocation/AllocationBenchmark.java

### Concurrency Issue (2)
- Line 109: `public String indicesShardsReplicasNodes = "10|1|0|1";`
- Line 111: `public int numTags = 2;`

### Unused Code (32)
- Line 113: `private AllocationService strategy;`
- Line 114: `private ClusterState initialClusterState;`
- Line 11: `import org.elasticsearch.TransportVersion;`
- Line 12: `import org.elasticsearch.action.ActionListener;`
- Line 13: `import org.elasticsearch.cluster.ClusterName;`
- Line 14: `import org.elasticsearch.cluster.ClusterState;`
- Line 15: `import org.elasticsearch.cluster.metadata.IndexMetadata;`
- Line 16: `import org.elasticsearch.cluster.metadata.Metadata;`
- Line 17: `import org.elasticsearch.cluster.node.DiscoveryNodes;`
- Line 18: `import org.elasticsearch.cluster.routing.RoutingTable;`
- Line 19: `import org.elasticsearch.cluster.routing.ShardRouting;`
- Line 20: `import org.elasticsearch.cluster.routing.allocation.AllocationService;`
- Line 21: `import org.elasticsearch.cluster.version.CompatibilityVersions;`
- Line 22: `import org.elasticsearch.common.settings.Settings;`
- Line 23: `import org.elasticsearch.index.IndexVersion;`
- Line 24: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 25: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 26: `import org.openjdk.jmh.annotations.Fork;`
- Line 27: `import org.openjdk.jmh.annotations.Measurement;`
- Line 28: `import org.openjdk.jmh.annotations.Mode;`
- Line 29: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 30: `import org.openjdk.jmh.annotations.Param;`
- Line 31: `import org.openjdk.jmh.annotations.Scope;`
- Line 32: `import org.openjdk.jmh.annotations.Setup;`
- Line 33: `import org.openjdk.jmh.annotations.State;`
- Line 34: `import org.openjdk.jmh.annotations.Warmup;`
- Line 36: `import java.util.Collections;`
- Line 37: `import java.util.HashMap;`
- Line 38: `import java.util.Map;`
- Line 39: `import java.util.concurrent.TimeUnit;`
- Line 40: `import java.util.stream.Collectors;`
- Line 41: `import java.util.stream.StreamSupport;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/routing/allocation/Allocators.java

### Concurrency Issue (1)
- Line 95: `private static final AtomicInteger portGenerator = new AtomicInteger();`

### Unused Code (25)
- Line 11: `import org.elasticsearch.cluster.ClusterModule;`
- Line 12: `import org.elasticsearch.cluster.EmptyClusterInfoService;`
- Line 13: `import org.elasticsearch.cluster.node.DiscoveryNode;`
- Line 14: `import org.elasticsearch.cluster.node.DiscoveryNodeRole;`
- Line 15: `import org.elasticsearch.cluster.node.VersionInformation;`
- Line 16: `import org.elasticsearch.cluster.routing.ShardRouting;`
- Line 17: `import org.elasticsearch.cluster.routing.allocation.AllocateUnassignedDecision;`
- Line 18: `import org.elasticsearch.cluster.routing.allocation.AllocationService;`
- Line 19: `import org.elasticsearch.cluster.routing.allocation.FailedShard;`
- Line 20: `import org.elasticsearch.cluster.routing.allocation.RoutingAllocation;`
- Line 21: `import org.elasticsearch.cluster.routing.allocation.allocator.BalancedShardsAllocator;`
- Line 22: `import org.elasticsearch.cluster.routing.allocation.decider.AllocationDecider;`
- Line 23: `import org.elasticsearch.cluster.routing.allocation.decider.AllocationDeciders;`
- Line 24: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 25: `import org.elasticsearch.common.settings.Settings;`
- Line 26: `import org.elasticsearch.common.transport.TransportAddress;`
- Line 27: `import org.elasticsearch.gateway.GatewayAllocator;`
- Line 28: `import org.elasticsearch.snapshots.EmptySnapshotsInfoService;`
- Line 30: `import java.util.Collection;`
- Line 31: `import java.util.Collections;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.Map;`
- Line 34: `import java.util.Set;`
- Line 35: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 37: `import static org.elasticsearch.cluster.routing.allocation.AllocateUnassignedDecision.NOT_TAKEN;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/routing/allocation/ShardsAvailabilityHealthIndicatorBenchmark.java

### Concurrency Issue (1)
- Line 83: `public String indicesShardsReplicasNodes = "10|1|0|1";`

### Unused Code (45)
- Line 85: `private ShardsAvailabilityHealthIndicatorService indicatorService;`
- Line 12: `import org.elasticsearch.cluster.ClusterName;`
- Line 13: `import org.elasticsearch.cluster.ClusterState;`
- Line 14: `import org.elasticsearch.cluster.metadata.IndexMetadata;`
- Line 15: `import org.elasticsearch.cluster.metadata.Metadata;`
- Line 16: `import org.elasticsearch.cluster.node.DiscoveryNodes;`
- Line 17: `import org.elasticsearch.cluster.routing.IndexRoutingTable;`
- Line 18: `import org.elasticsearch.cluster.routing.IndexShardRoutingTable;`
- Line 19: `import org.elasticsearch.cluster.routing.RecoverySource;`
- Line 20: `import org.elasticsearch.cluster.routing.RoutingTable;`
- Line 21: `import org.elasticsearch.cluster.routing.ShardRouting;`
- Line 22: `import org.elasticsearch.cluster.routing.UnassignedInfo;`
- Line 23: `import org.elasticsearch.cluster.routing.allocation.AllocationService;`
- Line 24: `import org.elasticsearch.cluster.routing.allocation.DataTier;`
- Line 25: `import org.elasticsearch.cluster.routing.allocation.shards.ShardsAvailabilityHealthIndicatorService;`
- Line 26: `import org.elasticsearch.cluster.service.ClusterService;`
- Line 27: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 28: `import org.elasticsearch.common.settings.Settings;`
- Line 29: `import org.elasticsearch.health.HealthIndicatorResult;`
- Line 30: `import org.elasticsearch.health.node.HealthInfo;`
- Line 31: `import org.elasticsearch.index.IndexVersion;`
- Line 32: `import org.elasticsearch.index.shard.ShardId;`
- Line 33: `import org.elasticsearch.indices.SystemIndices;`
- Line 34: `import org.elasticsearch.tasks.TaskManager;`
- Line 35: `import org.elasticsearch.telemetry.metric.MeterRegistry;`
- Line 36: `import org.elasticsearch.threadpool.DefaultBuiltInExecutorBuilders;`
- Line 37: `import org.elasticsearch.threadpool.ThreadPool;`
- Line 38: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 39: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 40: `import org.openjdk.jmh.annotations.Fork;`
- Line 41: `import org.openjdk.jmh.annotations.Measurement;`
- Line 42: `import org.openjdk.jmh.annotations.Mode;`
- Line 43: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 44: `import org.openjdk.jmh.annotations.Param;`
- Line 45: `import org.openjdk.jmh.annotations.Scope;`
- Line 46: `import org.openjdk.jmh.annotations.Setup;`
- Line 47: `import org.openjdk.jmh.annotations.State;`
- Line 48: `import org.openjdk.jmh.annotations.Warmup;`
- Line 50: `import java.util.Collections;`
- Line 51: `import java.util.HashSet;`
- Line 52: `import java.util.List;`
- Line 53: `import java.util.Map;`
- Line 54: `import java.util.Set;`
- Line 55: `import java.util.concurrent.TimeUnit;`
- Line 57: `import static org.elasticsearch.cluster.metadata.IndexMetadata.INDEX_ROUTING_REQUIRE_GROUP_SETTING;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/routing/allocation/TestShardRoutingRoleStrategies.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cluster.routing.ShardRouting;`
- Line 13: `import org.elasticsearch.cluster.routing.ShardRoutingRoleStrategy;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/script/ScriptScoreBenchmark.java

### Concurrency Issue (5)
- Line 181: `public void setDocument(int docid) {`
- Line 78: `private final PluginsService pluginsService = new PluginsService(`
- Line 83: `private final ScriptModule scriptModule = new ScriptModule(Settings.EMPTY, pluginsService.filterPlugins(ScriptPlugin.class).toList());`
- Line 88: `private final IndexFieldDataCache fieldDataCache = new IndexFieldDataCache.None();`
- Line 89: `private final CircuitBreakerService breakerService = new NoneCircuitBreakerService();`

### Exception Handling (3)
- Line 119: `default -> throw new IllegalArgumentException("Don't know how to implement script [" + script + "]");`
- Line 172: `throw new IllegalArgumentException("script only works when there is exactly one value");`
- Line 176: `throw new RuntimeException(e);`

### Unused Code (56)
- Line 97: `private String script;`
- Line 100: `private double indexingBufferMb;`
- Line 104: `private IndexReader reader;`
- Line 165: `private int docId;`
- Line 12: `import org.apache.lucene.document.SortedNumericDocValuesField;`
- Line 13: `import org.apache.lucene.index.DirectoryReader;`
- Line 14: `import org.apache.lucene.index.IndexReader;`
- Line 15: `import org.apache.lucene.index.IndexWriter;`
- Line 16: `import org.apache.lucene.index.IndexWriterConfig;`
- Line 17: `import org.apache.lucene.index.IndexWriterConfig.OpenMode;`
- Line 18: `import org.apache.lucene.index.SortedNumericDocValues;`
- Line 19: `import org.apache.lucene.search.IndexSearcher;`
- Line 20: `import org.apache.lucene.search.MatchAllDocsQuery;`
- Line 21: `import org.apache.lucene.search.Query;`
- Line 22: `import org.apache.lucene.search.TopDocs;`
- Line 23: `import org.apache.lucene.store.Directory;`
- Line 24: `import org.apache.lucene.store.MMapDirectory;`
- Line 25: `import org.apache.lucene.util.IOUtils;`
- Line 26: `import org.elasticsearch.common.lucene.search.function.ScriptScoreQuery;`
- Line 27: `import org.elasticsearch.common.settings.Settings;`
- Line 28: `import org.elasticsearch.index.IndexVersion;`
- Line 29: `import org.elasticsearch.index.fielddata.FieldDataContext;`
- Line 30: `import org.elasticsearch.index.fielddata.IndexFieldDataCache;`
- Line 31: `import org.elasticsearch.index.fielddata.IndexNumericFieldData;`
- Line 32: `import org.elasticsearch.index.mapper.MappedFieldType;`
- Line 33: `import org.elasticsearch.index.mapper.NumberFieldMapper.NumberFieldType;`
- Line 34: `import org.elasticsearch.index.mapper.NumberFieldMapper.NumberType;`
- Line 35: `import org.elasticsearch.indices.breaker.CircuitBreakerService;`
- Line 36: `import org.elasticsearch.indices.breaker.NoneCircuitBreakerService;`
- Line 37: `import org.elasticsearch.plugins.PluginsLoader;`
- Line 38: `import org.elasticsearch.plugins.PluginsService;`
- Line 39: `import org.elasticsearch.plugins.ScriptPlugin;`
- Line 40: `import org.elasticsearch.script.DocReader;`
- Line 41: `import org.elasticsearch.script.DocValuesDocReader;`
- Line 42: `import org.elasticsearch.script.ScoreScript;`
- Line 43: `import org.elasticsearch.script.ScriptModule;`
- Line 44: `import org.elasticsearch.search.lookup.SearchLookup;`
- Line 45: `import org.elasticsearch.search.lookup.SourceProvider;`
- Line 46: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 47: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 48: `import org.openjdk.jmh.annotations.Fork;`
- Line 49: `import org.openjdk.jmh.annotations.Measurement;`
- Line 50: `import org.openjdk.jmh.annotations.Mode;`
- Line 51: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 52: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 53: `import org.openjdk.jmh.annotations.Param;`
- Line 54: `import org.openjdk.jmh.annotations.Scope;`
- Line 55: `import org.openjdk.jmh.annotations.Setup;`
- Line 56: `import org.openjdk.jmh.annotations.State;`
- Line 57: `import org.openjdk.jmh.annotations.Warmup;`
- Line 59: `import java.io.IOException;`
- Line 60: `import java.nio.file.Path;`
- Line 61: `import java.util.List;`
- Line 62: `import java.util.Map;`
- Line 63: `import java.util.Set;`
- Line 64: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/QueryParserHelperBenchmark.java

### Concurrency Issue (1)
- Line 79: `private static final int NUMBER_OF_MAPPING_FIELDS = 1000;`

### Exception Handling (3)
- Line 184: `throw new UnsupportedOperationException();`
- Line 190: `throw new UnsupportedOperationException();`
- Line 201: `throw new UncheckedIOException(e);`

### Unused Code (60)
- Line 81: `private Directory directory;`
- Line 82: `private IndexReader indexReader;`
- Line 83: `private MapperService mapperService;`
- Line 12: `import org.apache.logging.log4j.util.Strings;`
- Line 13: `import org.apache.lucene.index.DirectoryReader;`
- Line 14: `import org.apache.lucene.index.IndexReader;`
- Line 15: `import org.apache.lucene.index.IndexWriter;`
- Line 16: `import org.apache.lucene.index.IndexWriterConfig;`
- Line 17: `import org.apache.lucene.search.IndexSearcher;`
- Line 18: `import org.apache.lucene.store.ByteBuffersDirectory;`
- Line 19: `import org.apache.lucene.store.Directory;`
- Line 20: `import org.elasticsearch.TransportVersion;`
- Line 21: `import org.elasticsearch.cluster.ClusterModule;`
- Line 22: `import org.elasticsearch.cluster.metadata.IndexMetadata;`
- Line 23: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 24: `import org.elasticsearch.common.compress.CompressedXContent;`
- Line 25: `import org.elasticsearch.common.io.stream.NamedWriteableRegistry;`
- Line 26: `import org.elasticsearch.common.lucene.Lucene;`
- Line 27: `import org.elasticsearch.common.settings.Settings;`
- Line 28: `import org.elasticsearch.common.xcontent.LoggingDeprecationHandler;`
- Line 29: `import org.elasticsearch.core.IOUtils;`
- Line 30: `import org.elasticsearch.index.IndexSettings;`
- Line 31: `import org.elasticsearch.index.IndexVersion;`
- Line 32: `import org.elasticsearch.index.fielddata.IndexFieldDataCache;`
- Line 33: `import org.elasticsearch.index.mapper.MapperMetrics;`
- Line 34: `import org.elasticsearch.index.mapper.MapperRegistry;`
- Line 35: `import org.elasticsearch.index.mapper.MapperService;`
- Line 36: `import org.elasticsearch.index.mapper.ParsedDocument;`
- Line 37: `import org.elasticsearch.index.mapper.ProvidedIdFieldMapper;`
- Line 38: `import org.elasticsearch.index.mapper.SourceToParse;`
- Line 39: `import org.elasticsearch.index.query.SearchExecutionContext;`
- Line 40: `import org.elasticsearch.index.search.QueryParserHelper;`
- Line 41: `import org.elasticsearch.index.shard.IndexShard;`
- Line 42: `import org.elasticsearch.index.similarity.SimilarityService;`
- Line 43: `import org.elasticsearch.indices.IndicesModule;`
- Line 44: `import org.elasticsearch.indices.breaker.NoneCircuitBreakerService;`
- Line 45: `import org.elasticsearch.script.Script;`
- Line 46: `import org.elasticsearch.script.ScriptCompiler;`
- Line 47: `import org.elasticsearch.script.ScriptContext;`
- Line 48: `import org.elasticsearch.xcontent.NamedXContentRegistry;`
- Line 49: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 50: `import org.elasticsearch.xcontent.XContentType;`
- Line 51: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 52: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 53: `import org.openjdk.jmh.annotations.Fork;`
- Line 54: `import org.openjdk.jmh.annotations.Measurement;`
- Line 55: `import org.openjdk.jmh.annotations.Mode;`
- Line 56: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 57: `import org.openjdk.jmh.annotations.Scope;`
- Line 58: `import org.openjdk.jmh.annotations.Setup;`
- Line 59: `import org.openjdk.jmh.annotations.State;`
- Line 60: `import org.openjdk.jmh.annotations.TearDown;`
- Line 61: `import org.openjdk.jmh.annotations.Warmup;`
- Line 63: `import java.io.IOException;`
- Line 64: `import java.io.UncheckedIOException;`
- Line 65: `import java.util.ArrayList;`
- Line 66: `import java.util.Collections;`
- Line 67: `import java.util.List;`
- Line 68: `import java.util.Map;`
- Line 69: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/aggregations/AggConstructionContentionBenchmark.java

### Concurrency Issue (6)
- Line 93: `private final SearchModule searchModule = new SearchModule(Settings.EMPTY, List.of());`
- Line 94: `private final ClusterSettings clusterSettings = new ClusterSettings(Settings.EMPTY, ClusterSettings.BUILT_IN_CLUSTER_SETTINGS);`
- Line 95: `private final PageCacheRecycler recycler = new PageCacheRecycler(Settings.EMPTY);`
- Line 96: `private final Index index = new Index("test", "uuid");`
- Line 97: `private final IndicesFieldDataCache indicesFieldDataCache = new IndicesFieldDataCache(`
- Line 156: `private final Query query = new MatchAllDocsQuery();`

### Exception Handling (17)
- Line 120: `default -> throw new UnsupportedOperationException();`
- Line 226: `throw new UnsupportedOperationException();`
- Line 231: `throw new UnsupportedOperationException();`
- Line 236: `throw new UnsupportedOperationException();`
- Line 241: `throw new UnsupportedOperationException();`
- Line 261: `throw new UnsupportedOperationException();`
- Line 266: `throw new UnsupportedOperationException();`
- Line 271: `throw new UnsupportedOperationException();`
- Line 276: `throw new UnsupportedOperationException();`
- Line 281: `throw new UnsupportedOperationException();`
- Line 286: `throw new UnsupportedOperationException();`
- Line 291: `throw new UnsupportedOperationException();`
- Line 296: `throw new UnsupportedOperationException();`
- Line 316: `throw new UnsupportedOperationException();`
- Line 321: `throw new UnsupportedOperationException();`
- Line 346: `throw new UnsupportedOperationException();`
- Line 351: `throw new UnsupportedOperationException();`

### Unused Code (69)
- Line 103: `private CircuitBreakerService breakerService;`
- Line 104: `private BigArrays bigArrays;`
- Line 105: `private boolean preallocateBreaker;`
- Line 108: `private String breaker;`
- Line 12: `import org.apache.lucene.analysis.Analyzer;`
- Line 13: `import org.apache.lucene.search.IndexSearcher;`
- Line 14: `import org.apache.lucene.search.MatchAllDocsQuery;`
- Line 15: `import org.apache.lucene.search.Query;`
- Line 16: `import org.elasticsearch.common.breaker.CircuitBreaker;`
- Line 17: `import org.elasticsearch.common.breaker.PreallocatedCircuitBreakerService;`
- Line 18: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 19: `import org.elasticsearch.common.settings.Settings;`
- Line 20: `import org.elasticsearch.common.util.BigArrays;`
- Line 21: `import org.elasticsearch.common.util.PageCacheRecycler;`
- Line 22: `import org.elasticsearch.core.Releasable;`
- Line 23: `import org.elasticsearch.core.Releasables;`
- Line 24: `import org.elasticsearch.index.Index;`
- Line 25: `import org.elasticsearch.index.IndexSettings;`
- Line 26: `import org.elasticsearch.index.analysis.NameOrDefinition;`
- Line 27: `import org.elasticsearch.index.analysis.NamedAnalyzer;`
- Line 28: `import org.elasticsearch.index.cache.bitset.BitsetFilterCache;`
- Line 29: `import org.elasticsearch.index.fielddata.FieldDataContext;`
- Line 30: `import org.elasticsearch.index.fielddata.IndexFieldData;`
- Line 31: `import org.elasticsearch.index.fielddata.IndexFieldDataCache;`
- Line 32: `import org.elasticsearch.index.mapper.MappedFieldType;`
- Line 33: `import org.elasticsearch.index.mapper.NestedLookup;`
- Line 34: `import org.elasticsearch.index.mapper.NumberFieldMapper;`
- Line 35: `import org.elasticsearch.index.mapper.NumberFieldMapper.NumberType;`
- Line 36: `import org.elasticsearch.index.query.QueryBuilder;`
- Line 37: `import org.elasticsearch.index.query.support.NestedScope;`
- Line 38: `import org.elasticsearch.indices.breaker.CircuitBreakerMetrics;`
- Line 39: `import org.elasticsearch.indices.breaker.CircuitBreakerService;`
- Line 40: `import org.elasticsearch.indices.breaker.HierarchyCircuitBreakerService;`
- Line 41: `import org.elasticsearch.indices.breaker.NoneCircuitBreakerService;`
- Line 42: `import org.elasticsearch.indices.fielddata.cache.IndicesFieldDataCache;`
- Line 43: `import org.elasticsearch.script.Script;`
- Line 44: `import org.elasticsearch.script.ScriptContext;`
- Line 45: `import org.elasticsearch.search.SearchModule;`
- Line 46: `import org.elasticsearch.search.aggregations.Aggregator;`
- Line 47: `import org.elasticsearch.search.aggregations.AggregatorFactories;`
- Line 48: `import org.elasticsearch.search.aggregations.bucket.terms.TermsAggregationBuilder;`
- Line 49: `import org.elasticsearch.search.aggregations.metrics.SumAggregationBuilder;`
- Line 50: `import org.elasticsearch.search.aggregations.support.AggregationContext;`
- Line 51: `import org.elasticsearch.search.aggregations.support.ValuesSourceRegistry;`
- Line 52: `import org.elasticsearch.search.internal.SubSearchContext;`
- Line 53: `import org.elasticsearch.search.lookup.SearchLookup;`
- Line 54: `import org.elasticsearch.search.sort.BucketedSort;`
- Line 55: `import org.elasticsearch.search.sort.BucketedSort.ExtraData;`
- Line 56: `import org.elasticsearch.search.sort.SortAndFormats;`
- Line 57: `import org.elasticsearch.search.sort.SortBuilder;`
- Line 58: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 59: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 60: `import org.openjdk.jmh.annotations.Fork;`
- Line 61: `import org.openjdk.jmh.annotations.Measurement;`
- Line 62: `import org.openjdk.jmh.annotations.Mode;`
- Line 63: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 64: `import org.openjdk.jmh.annotations.Param;`
- Line 65: `import org.openjdk.jmh.annotations.Scope;`
- Line 66: `import org.openjdk.jmh.annotations.Setup;`
- Line 67: `import org.openjdk.jmh.annotations.State;`
- Line 68: `import org.openjdk.jmh.annotations.Threads;`
- Line 69: `import org.openjdk.jmh.annotations.Warmup;`
- Line 71: `import java.io.IOException;`
- Line 72: `import java.util.ArrayList;`
- Line 73: `import java.util.List;`
- Line 74: `import java.util.Optional;`
- Line 75: `import java.util.Set;`
- Line 76: `import java.util.concurrent.TimeUnit;`
- Line 77: `import java.util.function.Function;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/aggregations/TermsReduceBenchmark.java

### Concurrency Issue (2)
- Line 105: `public void setup() {`
- Line 70: `private final TermsAggregationBuilder builder = new TermsAggregationBuilder("terms");`

### Unused Code (50)
- Line 163: `private int bufferSize;`
- Line 11: `import org.apache.lucene.search.ScoreDoc;`
- Line 12: `import org.apache.lucene.search.TopDocs;`
- Line 13: `import org.apache.lucene.search.TotalHits;`
- Line 14: `import org.apache.lucene.util.BytesRef;`
- Line 15: `import org.elasticsearch.action.search.QueryPhaseResultConsumer;`
- Line 16: `import org.elasticsearch.action.search.SearchPhaseController;`
- Line 17: `import org.elasticsearch.action.search.SearchProgressListener;`
- Line 18: `import org.elasticsearch.action.search.SearchRequest;`
- Line 19: `import org.elasticsearch.common.breaker.CircuitBreaker;`
- Line 20: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 21: `import org.elasticsearch.common.lucene.search.TopDocsAndMaxScore;`
- Line 22: `import org.elasticsearch.index.Index;`
- Line 23: `import org.elasticsearch.index.shard.ShardId;`
- Line 24: `import org.elasticsearch.indices.breaker.NoneCircuitBreakerService;`
- Line 25: `import org.elasticsearch.search.DocValueFormat;`
- Line 26: `import org.elasticsearch.search.SearchShardTarget;`
- Line 27: `import org.elasticsearch.search.aggregations.AggregationBuilders;`
- Line 28: `import org.elasticsearch.search.aggregations.AggregationReduceContext;`
- Line 29: `import org.elasticsearch.search.aggregations.BucketOrder;`
- Line 30: `import org.elasticsearch.search.aggregations.InternalAggregations;`
- Line 31: `import org.elasticsearch.search.aggregations.MultiBucketConsumerService;`
- Line 32: `import org.elasticsearch.search.aggregations.bucket.terms.StringTerms;`
- Line 33: `import org.elasticsearch.search.aggregations.bucket.terms.TermsAggregationBuilder;`
- Line 34: `import org.elasticsearch.search.aggregations.pipeline.PipelineAggregator;`
- Line 35: `import org.elasticsearch.search.builder.SearchSourceBuilder;`
- Line 36: `import org.elasticsearch.search.query.QuerySearchResult;`
- Line 37: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 38: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 39: `import org.openjdk.jmh.annotations.Fork;`
- Line 40: `import org.openjdk.jmh.annotations.Measurement;`
- Line 41: `import org.openjdk.jmh.annotations.Mode;`
- Line 42: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 43: `import org.openjdk.jmh.annotations.Param;`
- Line 44: `import org.openjdk.jmh.annotations.Scope;`
- Line 45: `import org.openjdk.jmh.annotations.Setup;`
- Line 46: `import org.openjdk.jmh.annotations.State;`
- Line 47: `import org.openjdk.jmh.annotations.Warmup;`
- Line 49: `import java.util.AbstractList;`
- Line 50: `import java.util.ArrayList;`
- Line 51: `import java.util.Collections;`
- Line 52: `import java.util.HashSet;`
- Line 53: `import java.util.List;`
- Line 54: `import java.util.Random;`
- Line 55: `import java.util.Set;`
- Line 56: `import java.util.concurrent.CountDownLatch;`
- Line 57: `import java.util.concurrent.ExecutorService;`
- Line 58: `import java.util.concurrent.Executors;`
- Line 59: `import java.util.concurrent.TimeUnit;`
- Line 60: `import java.util.concurrent.atomic.AtomicBoolean;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/aggregations/bucket/terms/LongKeyedBucketOrdsBenchmark.java

### Concurrency Issue (2)
- Line 56: `private static final long DISTINCT_VALUES_IN_BUCKETS = 10;`
- Line 58: `private final PageCacheRecycler recycler = new PageCacheRecycler(Settings.EMPTY);`

### Unused Code (19)
- Line 12: `import org.elasticsearch.aggregations.bucket.histogram.AutoDateHistogramAggregationBuilder;`
- Line 13: `import org.elasticsearch.common.settings.Settings;`
- Line 14: `import org.elasticsearch.common.util.BigArrays;`
- Line 15: `import org.elasticsearch.common.util.PageCacheRecycler;`
- Line 16: `import org.elasticsearch.search.aggregations.CardinalityUpperBound;`
- Line 17: `import org.elasticsearch.search.aggregations.bucket.terms.LongKeyedBucketOrds;`
- Line 18: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 19: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 20: `import org.openjdk.jmh.annotations.Fork;`
- Line 21: `import org.openjdk.jmh.annotations.Measurement;`
- Line 22: `import org.openjdk.jmh.annotations.Mode;`
- Line 23: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 24: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 25: `import org.openjdk.jmh.annotations.Scope;`
- Line 26: `import org.openjdk.jmh.annotations.Setup;`
- Line 27: `import org.openjdk.jmh.annotations.State;`
- Line 28: `import org.openjdk.jmh.annotations.Warmup;`
- Line 29: `import org.openjdk.jmh.infra.Blackhole;`
- Line 31: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/aggregations/bucket/terms/StringTermsSerializationBenchmark.java

### Unused Code (23)
- Line 47: `private int buckets;`
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.io.stream.DelayableWriteable;`
- Line 14: `import org.elasticsearch.common.io.stream.NamedWriteableRegistry;`
- Line 15: `import org.elasticsearch.search.DocValueFormat;`
- Line 16: `import org.elasticsearch.search.aggregations.BucketOrder;`
- Line 17: `import org.elasticsearch.search.aggregations.InternalAggregation;`
- Line 18: `import org.elasticsearch.search.aggregations.InternalAggregations;`
- Line 19: `import org.elasticsearch.search.aggregations.bucket.terms.StringTerms;`
- Line 20: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 21: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 22: `import org.openjdk.jmh.annotations.Fork;`
- Line 23: `import org.openjdk.jmh.annotations.Measurement;`
- Line 24: `import org.openjdk.jmh.annotations.Mode;`
- Line 25: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 26: `import org.openjdk.jmh.annotations.Param;`
- Line 27: `import org.openjdk.jmh.annotations.Scope;`
- Line 28: `import org.openjdk.jmh.annotations.Setup;`
- Line 29: `import org.openjdk.jmh.annotations.State;`
- Line 30: `import org.openjdk.jmh.annotations.Warmup;`
- Line 32: `import java.util.ArrayList;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/fetch/subphase/FetchSourcePhaseBenchmark.java

### Exception Handling (1)
- Line 57: `default -> throw new IllegalArgumentException("Unknown source [" + source + "]");`

### Unused Code (31)
- Line 37: `private BytesReference sourceBytes;`
- Line 38: `private FetchSourceContext fetchContext;`
- Line 41: `private XContentParserConfiguration parserConfig;`
- Line 44: `private String source;`
- Line 46: `private String includes;`
- Line 48: `private String excludes;`
- Line 3: `import org.elasticsearch.common.Strings;`
- Line 4: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 5: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 6: `import org.elasticsearch.common.io.Streams;`
- Line 7: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 8: `import org.elasticsearch.search.fetch.subphase.FetchSourceContext;`
- Line 9: `import org.elasticsearch.search.lookup.Source;`
- Line 10: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 11: `import org.elasticsearch.xcontent.XContentParser;`
- Line 12: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 13: `import org.elasticsearch.xcontent.XContentType;`
- Line 14: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 15: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 16: `import org.openjdk.jmh.annotations.Fork;`
- Line 17: `import org.openjdk.jmh.annotations.Measurement;`
- Line 18: `import org.openjdk.jmh.annotations.Mode;`
- Line 19: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 20: `import org.openjdk.jmh.annotations.Param;`
- Line 21: `import org.openjdk.jmh.annotations.Scope;`
- Line 22: `import org.openjdk.jmh.annotations.Setup;`
- Line 23: `import org.openjdk.jmh.annotations.State;`
- Line 24: `import org.openjdk.jmh.annotations.Warmup;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.util.Set;`
- Line 28: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/fetch/subphase/SourceFilteringBenchmark.java

### Exception Handling (1)
- Line 59: `default -> throw new IllegalArgumentException("Unknown source [" + source + "]");`

### Unused Code (25)
- Line 42: `private BytesReference sourceBytes;`
- Line 43: `private SourceFilter filter;`
- Line 46: `private String source;`
- Line 48: `private String includes;`
- Line 50: `private String excludes;`
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 14: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 15: `import org.elasticsearch.common.io.Streams;`
- Line 16: `import org.elasticsearch.search.fetch.subphase.FetchSourceContext;`
- Line 17: `import org.elasticsearch.search.lookup.Source;`
- Line 18: `import org.elasticsearch.search.lookup.SourceFilter;`
- Line 19: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 20: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 21: `import org.openjdk.jmh.annotations.Fork;`
- Line 22: `import org.openjdk.jmh.annotations.Measurement;`
- Line 23: `import org.openjdk.jmh.annotations.Mode;`
- Line 24: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 25: `import org.openjdk.jmh.annotations.Param;`
- Line 26: `import org.openjdk.jmh.annotations.Scope;`
- Line 27: `import org.openjdk.jmh.annotations.Setup;`
- Line 28: `import org.openjdk.jmh.annotations.State;`
- Line 29: `import org.openjdk.jmh.annotations.Warmup;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/search/query/range/DateFieldMapperDocValuesSkipperBenchmark.java

### Concurrency Issue (3)
- Line 147: `private static final String TIMESTAMP_FIELD = "@timestamp";`
- Line 148: `private static final String HOSTNAME_FIELD = "host.name";`
- Line 149: `private static final long BASE_TIMESTAMP = 1704067200000L;`

### Unused Code (55)
- Line 115: `private int nDocs;`
- Line 121: `private int batchSize;`
- Line 127: `private int deltaTime;`
- Line 133: `private double queryRange;`
- Line 139: `private int commitEvery;`
- Line 145: `private int seed;`
- Line 151: `private IndexSearcher indexSearcherWithoutDocValuesSkipper;`
- Line 152: `private IndexSearcher indexSearcherWithDocValuesSkipper;`
- Line 153: `private ExecutorService executorService;`
- Line 12: `import org.apache.lucene.analysis.standard.StandardAnalyzer;`
- Line 13: `import org.apache.lucene.document.Document;`
- Line 14: `import org.apache.lucene.document.Field;`
- Line 15: `import org.apache.lucene.document.LongPoint;`
- Line 16: `import org.apache.lucene.document.SortedDocValuesField;`
- Line 17: `import org.apache.lucene.document.SortedNumericDocValuesField;`
- Line 18: `import org.apache.lucene.document.StringField;`
- Line 19: `import org.apache.lucene.index.DirectoryReader;`
- Line 20: `import org.apache.lucene.index.IndexWriter;`
- Line 21: `import org.apache.lucene.index.IndexWriterConfig;`
- Line 22: `import org.apache.lucene.search.IndexOrDocValuesQuery;`
- Line 23: `import org.apache.lucene.search.IndexSearcher;`
- Line 24: `import org.apache.lucene.search.IndexSortSortedNumericDocValuesRangeQuery;`
- Line 25: `import org.apache.lucene.search.Query;`
- Line 26: `import org.apache.lucene.search.Sort;`
- Line 27: `import org.apache.lucene.search.SortField;`
- Line 28: `import org.apache.lucene.search.SortedNumericSortField;`
- Line 29: `import org.apache.lucene.store.Directory;`
- Line 30: `import org.apache.lucene.store.FSDirectory;`
- Line 31: `import org.apache.lucene.util.BytesRef;`
- Line 32: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 33: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 34: `import org.openjdk.jmh.annotations.Fork;`
- Line 35: `import org.openjdk.jmh.annotations.Level;`
- Line 36: `import org.openjdk.jmh.annotations.Measurement;`
- Line 37: `import org.openjdk.jmh.annotations.Mode;`
- Line 38: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 39: `import org.openjdk.jmh.annotations.Param;`
- Line 40: `import org.openjdk.jmh.annotations.Scope;`
- Line 41: `import org.openjdk.jmh.annotations.Setup;`
- Line 42: `import org.openjdk.jmh.annotations.State;`
- Line 43: `import org.openjdk.jmh.annotations.TearDown;`
- Line 44: `import org.openjdk.jmh.annotations.Threads;`
- Line 45: `import org.openjdk.jmh.annotations.Warmup;`
- Line 46: `import org.openjdk.jmh.infra.Blackhole;`
- Line 47: `import org.openjdk.jmh.profile.AsyncProfiler;`
- Line 48: `import org.openjdk.jmh.runner.Runner;`
- Line 49: `import org.openjdk.jmh.runner.RunnerException;`
- Line 50: `import org.openjdk.jmh.runner.options.Options;`
- Line 51: `import org.openjdk.jmh.runner.options.OptionsBuilder;`
- Line 53: `import java.io.IOException;`
- Line 54: `import java.nio.file.Files;`
- Line 55: `import java.util.Random;`
- Line 56: `import java.util.concurrent.ExecutorService;`
- Line 57: `import java.util.concurrent.Executors;`
- Line 58: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/spatial/GeometrySimplificationBenchmark.java

### Resource Leak (1)
- Line 90: `BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));`

### Exception Handling (1)
- Line 85: `throw new FileNotFoundException("classpath resource not found: " + name);`

### Unused Code (24)
- Line 12: `import org.elasticsearch.geometry.LinearRing;`
- Line 13: `import org.elasticsearch.geometry.simplify.GeometrySimplifier;`
- Line 14: `import org.elasticsearch.geometry.simplify.SimplificationErrorCalculator;`
- Line 15: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 16: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 17: `import org.openjdk.jmh.annotations.Fork;`
- Line 18: `import org.openjdk.jmh.annotations.Measurement;`
- Line 19: `import org.openjdk.jmh.annotations.Mode;`
- Line 20: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 21: `import org.openjdk.jmh.annotations.Param;`
- Line 22: `import org.openjdk.jmh.annotations.Scope;`
- Line 23: `import org.openjdk.jmh.annotations.Setup;`
- Line 24: `import org.openjdk.jmh.annotations.State;`
- Line 25: `import org.openjdk.jmh.annotations.Warmup;`
- Line 26: `import org.openjdk.jmh.infra.Blackhole;`
- Line 28: `import java.io.BufferedReader;`
- Line 29: `import java.io.FileNotFoundException;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.io.InputStream;`
- Line 32: `import java.io.InputStreamReader;`
- Line 33: `import java.nio.charset.StandardCharsets;`
- Line 34: `import java.text.ParseException;`
- Line 35: `import java.util.concurrent.TimeUnit;`
- Line 36: `import java.util.zip.GZIPInputStream;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/tdigest/SortBench.java

### Concurrency Issue (2)
- Line 55: `private final int size = 100000;`
- Line 56: `private final TDigestArrays arrays = new MemoryTrackingTDigestArrays(new NoopCircuitBreaker("default-wrapper-tdigest-arrays"));`

### Unused Code (20)
- Line 24: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 25: `import org.elasticsearch.search.aggregations.metrics.MemoryTrackingTDigestArrays;`
- Line 26: `import org.elasticsearch.tdigest.Sort;`
- Line 27: `import org.elasticsearch.tdigest.arrays.TDigestArrays;`
- Line 28: `import org.elasticsearch.tdigest.arrays.TDigestDoubleArray;`
- Line 29: `import org.elasticsearch.tdigest.arrays.TDigestIntArray;`
- Line 30: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 31: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 32: `import org.openjdk.jmh.annotations.Fork;`
- Line 33: `import org.openjdk.jmh.annotations.Measurement;`
- Line 34: `import org.openjdk.jmh.annotations.Mode;`
- Line 35: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 36: `import org.openjdk.jmh.annotations.Param;`
- Line 37: `import org.openjdk.jmh.annotations.Scope;`
- Line 38: `import org.openjdk.jmh.annotations.Setup;`
- Line 39: `import org.openjdk.jmh.annotations.State;`
- Line 40: `import org.openjdk.jmh.annotations.Threads;`
- Line 41: `import org.openjdk.jmh.annotations.Warmup;`
- Line 43: `import java.util.Random;`
- Line 44: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/tdigest/TDigestBench.java

### Concurrency Issue (1)
- Line 60: `private static final TDigestArrays arrays = new MemoryTrackingTDigestArrays(new NoopCircuitBreaker("default-wrapper-tdigest-arrays"));`

### Unused Code (26)
- Line 24: `import org.elasticsearch.common.breaker.NoopCircuitBreaker;`
- Line 25: `import org.elasticsearch.search.aggregations.metrics.MemoryTrackingTDigestArrays;`
- Line 26: `import org.elasticsearch.tdigest.TDigest;`
- Line 27: `import org.elasticsearch.tdigest.arrays.TDigestArrays;`
- Line 28: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 29: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 30: `import org.openjdk.jmh.annotations.Fork;`
- Line 31: `import org.openjdk.jmh.annotations.Measurement;`
- Line 32: `import org.openjdk.jmh.annotations.Mode;`
- Line 33: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 34: `import org.openjdk.jmh.annotations.Param;`
- Line 35: `import org.openjdk.jmh.annotations.Scope;`
- Line 36: `import org.openjdk.jmh.annotations.Setup;`
- Line 37: `import org.openjdk.jmh.annotations.State;`
- Line 38: `import org.openjdk.jmh.annotations.Threads;`
- Line 39: `import org.openjdk.jmh.annotations.Warmup;`
- Line 40: `import org.openjdk.jmh.profile.GCProfiler;`
- Line 41: `import org.openjdk.jmh.profile.StackProfiler;`
- Line 42: `import org.openjdk.jmh.runner.Runner;`
- Line 43: `import org.openjdk.jmh.runner.RunnerException;`
- Line 44: `import org.openjdk.jmh.runner.options.Options;`
- Line 45: `import org.openjdk.jmh.runner.options.OptionsBuilder;`
- Line 47: `import java.util.Random;`
- Line 48: `import java.util.concurrent.ThreadLocalRandom;`
- Line 49: `import java.util.concurrent.TimeUnit;`
- Line 50: `import java.util.function.Supplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/time/DateFormatterFromBenchmark.java

### Unused Code (13)
- Line 11: `import org.elasticsearch.common.time.DateFormatter;`
- Line 12: `import org.elasticsearch.common.time.DateFormatters;`
- Line 13: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 14: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 15: `import org.openjdk.jmh.annotations.Fork;`
- Line 16: `import org.openjdk.jmh.annotations.Measurement;`
- Line 17: `import org.openjdk.jmh.annotations.Mode;`
- Line 18: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 19: `import org.openjdk.jmh.annotations.Scope;`
- Line 20: `import org.openjdk.jmh.annotations.State;`
- Line 21: `import org.openjdk.jmh.annotations.Warmup;`
- Line 23: `import java.time.temporal.TemporalAccessor;`
- Line 24: `import java.util.concurrent.TimeUnit;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/vector/DistanceFunctionBenchmark.java

### Exception Handling (1)
- Line 195: `case HAMMING -> throw new UnsupportedOperationException("Unsupported function " + function);`

### Unused Code (31)
- Line 80: `private VectorType docType;`
- Line 83: `private VectorType queryType;`
- Line 86: `private int dims;`
- Line 89: `private Function function;`
- Line 92: `private Implementation type;`
- Line 94: `private DoubleSupplier benchmarkImpl;`
- Line 12: `import org.apache.lucene.util.BytesRef;`
- Line 13: `import org.elasticsearch.common.logging.LogConfigurator;`
- Line 14: `import org.elasticsearch.index.IndexVersion;`
- Line 15: `import org.elasticsearch.script.field.vectors.BinaryDenseVector;`
- Line 16: `import org.elasticsearch.script.field.vectors.ByteBinaryDenseVector;`
- Line 17: `import org.elasticsearch.script.field.vectors.ByteKnnDenseVector;`
- Line 18: `import org.elasticsearch.script.field.vectors.DenseVector;`
- Line 19: `import org.elasticsearch.script.field.vectors.KnnDenseVector;`
- Line 20: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 21: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 22: `import org.openjdk.jmh.annotations.Fork;`
- Line 23: `import org.openjdk.jmh.annotations.Measurement;`
- Line 24: `import org.openjdk.jmh.annotations.Mode;`
- Line 25: `import org.openjdk.jmh.annotations.OperationsPerInvocation;`
- Line 26: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 27: `import org.openjdk.jmh.annotations.Param;`
- Line 28: `import org.openjdk.jmh.annotations.Scope;`
- Line 29: `import org.openjdk.jmh.annotations.Setup;`
- Line 30: `import org.openjdk.jmh.annotations.State;`
- Line 31: `import org.openjdk.jmh.annotations.Warmup;`
- Line 32: `import org.openjdk.jmh.infra.Blackhole;`
- Line 34: `import java.nio.ByteBuffer;`
- Line 35: `import java.util.Random;`
- Line 36: `import java.util.concurrent.TimeUnit;`
- Line 37: `import java.util.function.DoubleSupplier;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/vector/VectorScorerBenchmark.java

### Unused Code (33)
- Line 12: `import org.apache.lucene.codecs.lucene99.Lucene99ScalarQuantizedVectorScorer;`
- Line 13: `import org.apache.lucene.codecs.lucene99.OffHeapQuantizedByteVectorValues;`
- Line 14: `import org.apache.lucene.index.VectorSimilarityFunction;`
- Line 15: `import org.apache.lucene.store.Directory;`
- Line 16: `import org.apache.lucene.store.IOContext;`
- Line 17: `import org.apache.lucene.store.IndexInput;`
- Line 18: `import org.apache.lucene.store.IndexOutput;`
- Line 19: `import org.apache.lucene.store.MMapDirectory;`
- Line 20: `import org.apache.lucene.util.hnsw.RandomVectorScorer;`
- Line 21: `import org.apache.lucene.util.hnsw.RandomVectorScorerSupplier;`
- Line 22: `import org.apache.lucene.util.quantization.QuantizedByteVectorValues;`
- Line 23: `import org.apache.lucene.util.quantization.ScalarQuantizer;`
- Line 24: `import org.elasticsearch.common.logging.LogConfigurator;`
- Line 25: `import org.elasticsearch.core.IOUtils;`
- Line 26: `import org.elasticsearch.simdvec.VectorScorerFactory;`
- Line 27: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 28: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 29: `import org.openjdk.jmh.annotations.Fork;`
- Line 30: `import org.openjdk.jmh.annotations.Measurement;`
- Line 31: `import org.openjdk.jmh.annotations.Mode;`
- Line 32: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 33: `import org.openjdk.jmh.annotations.Param;`
- Line 34: `import org.openjdk.jmh.annotations.Scope;`
- Line 35: `import org.openjdk.jmh.annotations.Setup;`
- Line 36: `import org.openjdk.jmh.annotations.State;`
- Line 37: `import org.openjdk.jmh.annotations.TearDown;`
- Line 38: `import org.openjdk.jmh.annotations.Warmup;`
- Line 40: `import java.io.IOException;`
- Line 41: `import java.nio.file.Files;`
- Line 42: `import java.util.concurrent.ThreadLocalRandom;`
- Line 43: `import java.util.concurrent.TimeUnit;`
- Line 45: `import static org.elasticsearch.simdvec.VectorSimilarityType.DOT_PRODUCT;`
- Line 46: `import static org.elasticsearch.simdvec.VectorSimilarityType.EUCLIDEAN;`

## ../benchmarks/src/main/java/org/elasticsearch/benchmark/xcontent/FilterContentBenchmark.java

### Exception Handling (2)
- Line 73: `default -> throw new IllegalArgumentException("Unknown type [" + type + "]");`
- Line 102: `default -> throw new IllegalArgumentException("Unknown type [" + type + "]");`

### Unused Code (37)
- Line 54: `private String type;`
- Line 57: `private String fieldCount;`
- Line 60: `private boolean inclusive;`
- Line 62: `private BytesReference source;`
- Line 63: `private XContentParserConfiguration parserConfig;`
- Line 65: `private XContentParserConfiguration parserConfigMatchDotsInFieldNames;`
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 14: `import org.elasticsearch.common.io.Streams;`
- Line 15: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 16: `import org.elasticsearch.common.util.Maps;`
- Line 17: `import org.elasticsearch.common.xcontent.XContentHelper;`
- Line 18: `import org.elasticsearch.common.xcontent.support.XContentMapValues;`
- Line 19: `import org.elasticsearch.search.lookup.Source;`
- Line 20: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 21: `import org.elasticsearch.xcontent.XContentParser;`
- Line 22: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 23: `import org.elasticsearch.xcontent.XContentType;`
- Line 24: `import org.openjdk.jmh.annotations.Benchmark;`
- Line 25: `import org.openjdk.jmh.annotations.BenchmarkMode;`
- Line 26: `import org.openjdk.jmh.annotations.Fork;`
- Line 27: `import org.openjdk.jmh.annotations.Measurement;`
- Line 28: `import org.openjdk.jmh.annotations.Mode;`
- Line 29: `import org.openjdk.jmh.annotations.OutputTimeUnit;`
- Line 30: `import org.openjdk.jmh.annotations.Param;`
- Line 31: `import org.openjdk.jmh.annotations.Scope;`
- Line 32: `import org.openjdk.jmh.annotations.Setup;`
- Line 33: `import org.openjdk.jmh.annotations.State;`
- Line 34: `import org.openjdk.jmh.annotations.Warmup;`
- Line 36: `import java.io.IOException;`
- Line 37: `import java.util.Arrays;`
- Line 38: `import java.util.HashSet;`
- Line 39: `import java.util.Map;`
- Line 40: `import java.util.Set;`
- Line 41: `import java.util.concurrent.TimeUnit;`
- Line 42: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 43: `import java.util.stream.Collectors;`

## ../benchmarks/src/test/java/org/elasticsearch/benchmark/compute/operator/EvalBenchmarkTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.test.ESTestCase;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/AstUtils.java

### Unused Code (1)
- Line 12: `import com.puppycrawl.tools.checkstyle.api.DetailAST;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/HiddenFieldCheck.java

### Concurrency Issue (7)
- Line 517: `public void setIgnoreSetter(boolean ignoreSetter) {`
- Line 541: `public void setIgnoreConstructorParameter(boolean ignoreConstructorParameter) {`
- Line 551: `public void setIgnoreAbstractMethods(boolean ignoreAbstractMethods) {`
- Line 555: `public void setIgnoreMethodNames(String ignoreMethodNames) {`
- Line 559: `public void setIgnoreConstructorBody(boolean ignoreConstructorBody) {`
- Line 563: `public void setIgnoreConstructorMethods(String ignoreConstructorMethods) {`
- Line 567: `public void setMinLineCount(int minLineCount) {`

### Unused Code (24)
- Line 56: `private FieldFrame frame;`
- Line 59: `private Pattern ignoreFormat;`
- Line 64: `private boolean ignoreSetter;`
- Line 70: `private boolean setterCanReturnItsClass;`
- Line 73: `private boolean ignoreConstructorParameter;`
- Line 76: `private boolean ignoreConstructorBody;`
- Line 79: `private boolean ignoreAbstractMethods;`
- Line 82: `private String ignoreMethodNames;`
- Line 85: `private String ignoreConstructorMethods;`
- Line 88: `private int minLineCount = -1;`
- Line 23: `import com.puppycrawl.tools.checkstyle.FileStatefulCheck;`
- Line 24: `import com.puppycrawl.tools.checkstyle.api.AbstractCheck;`
- Line 25: `import com.puppycrawl.tools.checkstyle.api.DetailAST;`
- Line 26: `import com.puppycrawl.tools.checkstyle.api.Scope;`
- Line 27: `import com.puppycrawl.tools.checkstyle.api.TokenTypes;`
- Line 28: `import com.puppycrawl.tools.checkstyle.utils.CheckUtil;`
- Line 29: `import com.puppycrawl.tools.checkstyle.utils.ScopeUtil;`
- Line 30: `import com.puppycrawl.tools.checkstyle.utils.TokenUtil;`
- Line 32: `import java.util.HashSet;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Locale;`
- Line 35: `import java.util.Objects;`
- Line 36: `import java.util.Set;`
- Line 37: `import java.util.regex.Pattern;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/MissingJavadocTypeCheck.java

### Concurrency Issue (2)
- Line 72: `public void setScope(Scope scope) {`
- Line 81: `public void setExcludeScope(Scope excludeScope) {`

### Unused Code (17)
- Line 53: `private Scope scope = Scope.PUBLIC;`
- Line 56: `private Scope excludeScope;`
- Line 59: `private Pattern ignorePattern = Pattern.compile("^$");`
- Line 23: `import com.puppycrawl.tools.checkstyle.StatelessCheck;`
- Line 24: `import com.puppycrawl.tools.checkstyle.api.AbstractCheck;`
- Line 25: `import com.puppycrawl.tools.checkstyle.api.DetailAST;`
- Line 26: `import com.puppycrawl.tools.checkstyle.api.FileContents;`
- Line 27: `import com.puppycrawl.tools.checkstyle.api.Scope;`
- Line 28: `import com.puppycrawl.tools.checkstyle.api.TextBlock;`
- Line 29: `import com.puppycrawl.tools.checkstyle.api.TokenTypes;`
- Line 30: `import com.puppycrawl.tools.checkstyle.utils.AnnotationUtil;`
- Line 31: `import com.puppycrawl.tools.checkstyle.utils.CommonUtil;`
- Line 32: `import com.puppycrawl.tools.checkstyle.utils.ScopeUtil;`
- Line 34: `import java.util.Arrays;`
- Line 35: `import java.util.Set;`
- Line 36: `import java.util.regex.Pattern;`
- Line 37: `import java.util.stream.Collectors;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/SnippetLengthCheck.java

### Concurrency Issue (2)
- Line 37: `public void setMax(int max) {`
- Line 31: `private static final Pattern START = Pattern.compile("^( *)//\\s*tag::(?!noformat)(.+?)\\s*$", Pattern.MULTILINE);`

### Unused Code (11)
- Line 32: `private int max;`
- Line 79: `private int lastLineNumber;`
- Line 12: `import com.puppycrawl.tools.checkstyle.api.AbstractFileSetCheck;`
- Line 13: `import com.puppycrawl.tools.checkstyle.api.CheckstyleException;`
- Line 14: `import com.puppycrawl.tools.checkstyle.api.FileText;`
- Line 16: `import java.io.File;`
- Line 17: `import java.util.Arrays;`
- Line 18: `import java.util.Iterator;`
- Line 19: `import java.util.function.BiConsumer;`
- Line 20: `import java.util.regex.Matcher;`
- Line 21: `import java.util.regex.Pattern;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/StringFormattingCheck.java

### Concurrency Issue (1)
- Line 57: `private static final Pattern formatSpecifier = Pattern.compile("%(?:\\d+\\$)?(?:[-#+ 0,\\(<]*)?(?:\\d+)?(?:\\.\\d+)?([tT]?[a-zA-Z%])");`

### Unused Code (7)
- Line 12: `import com.puppycrawl.tools.checkstyle.StatelessCheck;`
- Line 13: `import com.puppycrawl.tools.checkstyle.api.AbstractCheck;`
- Line 14: `import com.puppycrawl.tools.checkstyle.api.DetailAST;`
- Line 15: `import com.puppycrawl.tools.checkstyle.api.TokenTypes;`
- Line 17: `import java.util.Locale;`
- Line 18: `import java.util.regex.Matcher;`
- Line 19: `import java.util.regex.Pattern;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/checkstyle/SwitchBetweenCheck.java

### Concurrency Issue (1)
- Line 36: `public static final String SWITCH_RANDOM_INT_MSG_KEY = "forbidden.switch.randomInt";`

### Unused Code (4)
- Line 12: `import com.puppycrawl.tools.checkstyle.StatelessCheck;`
- Line 13: `import com.puppycrawl.tools.checkstyle.api.AbstractCheck;`
- Line 14: `import com.puppycrawl.tools.checkstyle.api.DetailAST;`
- Line 15: `import com.puppycrawl.tools.checkstyle.api.TokenTypes;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/BuildToolsConventionsPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.info.ParallelDetector;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.precommit.LicenseHeadersPrecommitPlugin;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.tasks.bundling.Jar;`
- Line 18: `import org.gradle.api.tasks.testing.Test;`
- Line 20: `import java.io.File;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/EclipseConventionPlugin.java

### Exception Handling (1)
- Line 80: `throw new GradleException("Cannot configure eclipse", e);`

### Unused Code (23)
- Line 12: `import org.apache.tools.ant.taskdefs.condition.Os;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.Transformer;`
- Line 18: `import org.gradle.api.invocation.Gradle;`
- Line 19: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 20: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 21: `import org.gradle.api.tasks.Copy;`
- Line 22: `import org.gradle.api.tasks.Delete;`
- Line 23: `import org.gradle.plugins.ide.eclipse.EclipsePlugin;`
- Line 24: `import org.gradle.plugins.ide.eclipse.model.Classpath;`
- Line 25: `import org.gradle.plugins.ide.eclipse.model.EclipseModel;`
- Line 26: `import org.gradle.plugins.ide.eclipse.model.EclipseProject;`
- Line 27: `import org.gradle.plugins.ide.eclipse.model.ProjectDependency;`
- Line 28: `import org.gradle.plugins.ide.eclipse.model.SourceFolder;`
- Line 29: `import org.gradle.plugins.ide.eclipse.model.ClasspathEntry;`
- Line 31: `import java.io.File;`
- Line 32: `import java.util.List;`
- Line 33: `import java.io.IOException;`
- Line 34: `import static java.util.stream.Collectors.toList;`
- Line 36: `import static org.apache.commons.io.FileUtils.readFileToString;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/GUtils.java

### Unused Code (1)
- Line 12: `import java.util.Locale;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/GitInfoPlugin.java

### Unused Code (11)
- Line 27: `private ProviderFactory factory;`
- Line 12: `import org.elasticsearch.gradle.internal.conventions.info.GitInfo;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.info.GitInfoValueSource;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.provider.Property;`
- Line 18: `import org.gradle.api.provider.Provider;`
- Line 19: `import org.gradle.api.provider.ProviderFactory;`
- Line 21: `import java.io.File;`
- Line 23: `import javax.inject.Inject;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/LicensingPlugin.java

### Concurrency Issue (1)
- Line 25: `static final String AGPL_ELASTIC_LICENSE_URL_POSTFIX = "/licenses/AGPL-3.0+SSPL-1.0+ELASTIC-LICENSE-2.0.txt";`

### Unused Code (8)
- Line 27: `private ProviderFactory providerFactory;`
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.provider.MapProperty;`
- Line 15: `import org.gradle.api.provider.Provider;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 18: `import java.util.Map;`
- Line 20: `import javax.inject.Inject;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/PublishPlugin.java

### Concurrency Issue (1)
- Line 85: `@SuppressWarnings("unchecked")`

### Unused Code (35)
- Line 51: `private ProjectLayout projectLayout;`
- Line 52: `private BuildLayout buildLayout;`
- Line 53: `private ProviderFactory providerFactory;`
- Line 12: `import groovy.util.Node;`
- Line 14: `import com.github.jengelman.gradle.plugins.shadow.ShadowExtension;`
- Line 15: `import com.github.jengelman.gradle.plugins.shadow.ShadowPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.conventions.info.GitInfo;`
- Line 18: `import org.elasticsearch.gradle.internal.conventions.precommit.PomValidationPrecommitPlugin;`
- Line 19: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 20: `import org.gradle.api.NamedDomainObjectSet;`
- Line 21: `import org.gradle.api.Plugin;`
- Line 22: `import org.gradle.api.Project;`
- Line 23: `import org.gradle.api.XmlProvider;`
- Line 24: `import org.gradle.api.file.ProjectLayout;`
- Line 25: `import org.gradle.api.plugins.BasePlugin;`
- Line 26: `import org.gradle.api.plugins.BasePluginExtension;`
- Line 27: `import org.gradle.api.plugins.ExtensionContainer;`
- Line 28: `import org.gradle.api.plugins.JavaLibraryPlugin;`
- Line 29: `import org.gradle.api.plugins.JavaPlugin;`
- Line 30: `import org.gradle.api.provider.MapProperty;`
- Line 31: `import org.gradle.api.provider.Provider;`
- Line 32: `import org.gradle.api.provider.ProviderFactory;`
- Line 33: `import org.gradle.api.publish.PublishingExtension;`
- Line 34: `import org.gradle.api.publish.maven.MavenPublication;`
- Line 35: `import org.gradle.api.publish.maven.plugins.MavenPublishPlugin;`
- Line 36: `import org.gradle.api.publish.maven.tasks.GenerateMavenPom;`
- Line 37: `import org.gradle.api.tasks.SourceSet;`
- Line 38: `import org.gradle.api.tasks.bundling.Jar;`
- Line 39: `import org.gradle.initialization.layout.BuildLayout;`
- Line 40: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`
- Line 41: `import org.w3c.dom.Element;`
- Line 43: `import java.io.File;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.concurrent.Callable;`
- Line 47: `import javax.inject.Inject;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/VersionPropertiesBuildService.java

### Exception Handling (2)
- Line 38: `throw new GradleException("Cannot load VersionPropertiesBuildService", e);`
- Line 57: `throw new GradleException("Cannot resolve minimum compiler version via VersionPropertiesBuildService", e);`

### Unused Code (11)
- Line 12: `import org.apache.commons.io.FileUtils;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.JavaVersion;`
- Line 15: `import org.gradle.api.file.RegularFileProperty;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import org.gradle.api.services.BuildService;`
- Line 18: `import org.gradle.api.services.BuildServiceParameters;`
- Line 20: `import java.io.File;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.util.Properties;`
- Line 23: `import javax.inject.Inject;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/VersionPropertiesLoader.java

### Resource Leak (1)
- Line 25: `try (InputStream is = new FileInputStream(input)) {`

### Exception Handling (4)
- Line 35: `throw new IllegalStateException("Elasticsearch version is missing from properties.");`
- Line 38: `throw new IllegalStateException(`
- Line 47: `throw new IllegalStateException("Invalid qualifier: " + qualifier);`
- Line 61: `throw new IllegalArgumentException(`

### Unused Code (6)
- Line 13: `import org.gradle.api.provider.ProviderFactory;`
- Line 15: `import java.io.File;`
- Line 16: `import java.io.FileInputStream;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.io.InputStream;`
- Line 19: `import java.util.Properties;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/VersionPropertiesPlugin.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.provider.Provider;`
- Line 17: `import java.io.File;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/FormattingPrecommitPlugin.java

### Unused Code (6)
- Line 12: `import com.diffplug.gradle.spotless.SpotlessExtension;`
- Line 13: `import com.diffplug.gradle.spotless.SpotlessPlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 19: `import java.io.File;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/LicenseHeadersPrecommitPlugin.java

### Unused Code (10)
- Line 40: `private ProviderFactory providerFactory;`
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.api.Task;`
- Line 14: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 15: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 20: `import javax.inject.Inject;`
- Line 21: `import java.util.stream.Collectors;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/LicenseHeadersTask.java

### Resource Leak (1)
- Line 217: `BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(xmlReportFile));`

### Concurrency Issue (2)
- Line 126: `public void setApprovedLicenses(List<String> approvedLicenses) {`
- Line 134: `public void setExcludes(List<String> excludes) {`

### Exception Handling (1)
- Line 158: `throw new IllegalArgumentException("License category name must be exactly 5 characters, got " + categoryName);`

### Unused Code (50)
- Line 282: `private String licenseFamilyCategory;`
- Line 283: `private String licenseFamilyName;`
- Line 284: `private String substringPattern;`
- Line 12: `import org.apache.rat.Defaults;`
- Line 13: `import org.apache.rat.ReportConfiguration;`
- Line 14: `import org.apache.rat.analysis.IHeaderMatcher;`
- Line 15: `import org.apache.rat.analysis.util.HeaderMatcherMultiplexer;`
- Line 16: `import org.apache.rat.anttasks.SubstringLicenseMatcher;`
- Line 17: `import org.apache.rat.api.RatException;`
- Line 18: `import org.apache.rat.document.impl.FileDocument;`
- Line 19: `import org.apache.rat.license.SimpleLicenseFamily;`
- Line 20: `import org.apache.rat.report.RatReport;`
- Line 21: `import org.apache.rat.report.claim.ClaimStatistic;`
- Line 22: `import org.apache.rat.report.xml.XmlReportFactory;`
- Line 23: `import org.apache.rat.report.xml.writer.impl.base.XmlWriter;`
- Line 24: `import org.gradle.api.DefaultTask;`
- Line 25: `import org.gradle.api.GradleException;`
- Line 26: `import org.gradle.api.file.FileCollection;`
- Line 27: `import org.gradle.api.file.ProjectLayout;`
- Line 28: `import org.gradle.api.file.RegularFileProperty;`
- Line 29: `import org.gradle.api.model.ObjectFactory;`
- Line 30: `import org.gradle.api.provider.ListProperty;`
- Line 31: `import org.gradle.api.tasks.CacheableTask;`
- Line 32: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 33: `import org.gradle.api.tasks.Input;`
- Line 34: `import org.gradle.api.tasks.InputFiles;`
- Line 35: `import org.gradle.api.tasks.Internal;`
- Line 36: `import org.gradle.api.tasks.OutputFile;`
- Line 37: `import org.gradle.api.tasks.PathSensitive;`
- Line 38: `import org.gradle.api.tasks.PathSensitivity;`
- Line 39: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 40: `import org.gradle.api.tasks.TaskAction;`
- Line 41: `import org.w3c.dom.Element;`
- Line 42: `import org.w3c.dom.NodeList;`
- Line 43: `import org.xml.sax.SAXException;`
- Line 45: `import java.io.BufferedWriter;`
- Line 46: `import java.io.File;`
- Line 47: `import java.io.FileWriter;`
- Line 48: `import java.io.IOException;`
- Line 49: `import java.io.Serializable;`
- Line 50: `import java.io.Writer;`
- Line 51: `import java.nio.file.Files;`
- Line 52: `import java.util.ArrayList;`
- Line 53: `import java.util.Arrays;`
- Line 54: `import java.util.List;`
- Line 55: `import java.util.stream.Collectors;`
- Line 56: `import javax.inject.Inject;`
- Line 57: `import javax.xml.XMLConstants;`
- Line 58: `import javax.xml.parsers.DocumentBuilderFactory;`
- Line 59: `import javax.xml.parsers.ParserConfigurationException;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/PomValidationPrecommitPlugin.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.GUtils;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.publish.PublishingExtension;`
- Line 16: `import org.gradle.api.publish.maven.tasks.GenerateMavenPom;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/PomValidationTask.java

### Unused Code (16)
- Line 34: `private boolean foundError;`
- Line 12: `import org.apache.maven.model.Model;`
- Line 13: `import org.apache.maven.model.io.xpp3.MavenXpp3Reader;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTask;`
- Line 15: `import org.gradle.api.GradleException;`
- Line 16: `import org.gradle.api.file.RegularFileProperty;`
- Line 17: `import org.gradle.api.model.ObjectFactory;`
- Line 18: `import org.gradle.api.tasks.InputFile;`
- Line 19: `import org.gradle.api.tasks.PathSensitive;`
- Line 20: `import org.gradle.api.tasks.PathSensitivity;`
- Line 21: `import org.gradle.api.tasks.TaskAction;`
- Line 23: `import java.io.FileReader;`
- Line 24: `import java.util.Collection;`
- Line 25: `import java.util.function.Consumer;`
- Line 26: `import java.util.function.Predicate;`
- Line 28: `import javax.inject.Inject;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/PrecommitPlugin.java

### Unused Code (5)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 16: `import org.gradle.api.tasks.TaskProvider;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/PrecommitTask.java

### Exception Handling (1)
- Line 36: `throw new UnsupportedOperationException();`

### Unused Code (9)
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.file.ProjectLayout;`
- Line 13: `import org.gradle.api.tasks.OutputFile;`
- Line 14: `import org.gradle.api.tasks.TaskAction;`
- Line 16: `import javax.inject.Inject;`
- Line 17: `import java.io.File;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.nio.file.StandardOpenOption;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/precommit/PrecommitTaskPlugin.java

### Unused Code (8)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 16: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`
- Line 18: `import org.gradle.api.tasks.testing.Test;`
- Line 19: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/util/Util.java

### Exception Handling (1)
- Line 42: `throw new GradleException("Sysprop [" + property + "] must be [true] or [false] but was [" + propertyValue + "]");`

### Unused Code (15)
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.file.FileTree;`
- Line 16: `import org.gradle.api.initialization.IncludedBuild;`
- Line 17: `import org.gradle.api.internal.GradleInternal;`
- Line 18: `import org.gradle.api.invocation.Gradle;`
- Line 19: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 20: `import org.gradle.api.tasks.SourceSet;`
- Line 21: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 22: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 24: `import java.io.File;`
- Line 25: `import java.util.Optional;`
- Line 26: `import java.util.function.Supplier;`
- Line 28: `import javax.annotation.Nullable;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/info/GitInfo.java

### Concurrency Issue (1)
- Line 32: `private static final Pattern GIT_PATTERN = Pattern.compile("git@([^:]+):([^\\.]+)\\.git");`

### Exception Handling (2)
- Line 125: `throw new GradleException("Can't find revision for refName " + refName);`
- Line 134: `throw new GradleException("unable to read the git revision", e);`

### Unused Code (17)
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.logging.Logging;`
- Line 15: `import java.io.File;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.charset.StandardCharsets;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.nio.file.Paths;`
- Line 21: `import java.util.Arrays;`
- Line 22: `import java.util.HashMap;`
- Line 23: `import java.util.Iterator;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Objects;`
- Line 26: `import java.util.regex.Matcher;`
- Line 27: `import java.util.regex.Pattern;`
- Line 28: `import java.util.stream.Collectors;`
- Line 29: `import java.util.stream.Stream;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/info/GitInfoValueSource.java

### Unused Code (5)
- Line 3: `import org.gradle.api.provider.Property;`
- Line 4: `import org.gradle.api.provider.ValueSource;`
- Line 5: `import org.gradle.api.provider.ValueSourceParameters;`
- Line 6: `import org.jetbrains.annotations.Nullable;`
- Line 8: `import java.io.File;`

## ../build-conventions/src/main/java/org/elasticsearch/gradle/internal/conventions/info/ParallelDetector.java

### Resource Leak (1)
- Line 48: `try (BufferedReader reader = new BufferedReader(new FileReader(cpuInfoFile))) {`

### Concurrency Issue (3)
- Line 33: `private static Integer _defaultParallel = null;`
- Line 34: `private static final Logger LOGGER = Logging.getLogger(ParallelDetector.class);`
- Line 36: `private final static int MACOS_MONTEREY_MAJOR_VERSION = 12;`

### Exception Handling (1)
- Line 67: `throw new UncheckedIOException(e);`

### Unused Code (17)
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.logging.Logger;`
- Line 14: `import org.gradle.api.logging.Logging;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import org.gradle.process.ExecSpec;`
- Line 19: `import java.io.BufferedReader;`
- Line 20: `import java.io.ByteArrayOutputStream;`
- Line 21: `import java.io.File;`
- Line 22: `import java.io.FileReader;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.io.UncheckedIOException;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Map;`
- Line 29: `import java.util.stream.Collectors;`

## ../build-tools/reaper/src/main/java/org/elasticsearch/gradle/reaper/Reaper.java

### Exception Handling (1)
- Line 113: `throw new UncheckedIOException(e);`

### Unused Code (11)
- Line 42: `private Path inputDir;`
- Line 43: `private boolean failed;`
- Line 12: `import java.io.Closeable;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.UncheckedIOException;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Path;`
- Line 17: `import java.nio.file.Paths;`
- Line 18: `import java.util.Comparator;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.stream.Stream;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/AbstractLazyPropertyCollection.java

### Unused Code (1)
- Line 11: `import java.util.List;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/Architecture.java

### Exception Handling (1)
- Line 30: `default -> throw new IllegalArgumentException("can not determine architecture from [" + architecture + "]");`

## ../build-tools/src/main/java/org/elasticsearch/gradle/DistributionDownloadPlugin.java

### Null Pointer (1)
- Line 145: `return distributionsResolutionStrategies.stream()`

### Concurrency Issue (9)
- Line 43: `static final String RESOLUTION_CONTAINER_NAME = "elasticsearch_distributions_resolutions";`
- Line 44: `private static final String CONTAINER_NAME = "elasticsearch_distributions";`
- Line 45: `private static final String FAKE_IVY_GROUP = "elasticsearch-distribution";`
- Line 46: `private static final String FAKE_SNAPSHOT_IVY_GROUP = "elasticsearch-distribution-snapshot";`
- Line 47: `private static final String DOWNLOAD_REPO_NAME = "elasticsearch-downloads";`
- Line 48: `private static final String SNAPSHOT_REPO_NAME = "elasticsearch-snapshots";`
- Line 50: `public static final String ES_DISTRO_CONFIG_PREFIX = "es_distro_";`
- Line 51: `public static final String DISTRO_EXTRACTED_CONFIG_PREFIX = ES_DISTRO_CONFIG_PREFIX + "extracted_";`
- Line 52: `public static final String DISTRO_CONFIG_PREFIX = ES_DISTRO_CONFIG_PREFIX + "file_";`

### Unused Code (20)
- Line 60: `private boolean writingDependencies = false;`
- Line 12: `import org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes;`
- Line 13: `import org.elasticsearch.gradle.transform.SymbolicLinkPreservingUntarTransform;`
- Line 14: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 15: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.artifacts.Configuration;`
- Line 19: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 20: `import org.gradle.api.artifacts.repositories.IvyArtifactRepository;`
- Line 21: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 22: `import org.gradle.api.model.ObjectFactory;`
- Line 23: `import org.gradle.api.provider.Property;`
- Line 24: `import org.gradle.api.provider.Provider;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Collections;`
- Line 28: `import java.util.Comparator;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Objects;`
- Line 32: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/DistributionResolution.java

### Concurrency Issue (2)
- Line 36: `public void setResolver(Resolver resolver) {`
- Line 40: `public void setPriority(int priority) {`

### Unused Code (3)
- Line 15: `private Resolver resolver;`
- Line 17: `private int priority;`
- Line 12: `import org.gradle.api.Project;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/ElasticsearchDistribution.java

### Concurrency Issue (1)
- Line 39: `public static final Platform CURRENT_PLATFORM = OS.<Platform>conditional()`

### Exception Handling (4)
- Line 119: `throw new IllegalArgumentException("Cannot set Elasticsearch Distribution type to " + type + ". Type unknown.");`
- Line 217: `throw new IllegalArgumentException(`
- Line 222: `throw new IllegalArgumentException(`
- Line 248: `throw new IllegalArgumentException(`

### Unused Code (12)
- Line 58: `private boolean frozen = false;`
- Line 12: `import org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes;`
- Line 13: `import org.gradle.api.Buildable;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.model.ObjectFactory;`
- Line 17: `import org.gradle.api.provider.Property;`
- Line 18: `import org.gradle.api.tasks.TaskDependency;`
- Line 20: `import java.io.File;`
- Line 21: `import java.util.Collections;`
- Line 22: `import java.util.Iterator;`
- Line 23: `import java.util.Locale;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/FileSupplier.java

### Unused Code (2)
- Line 11: `import java.io.File;`
- Line 12: `import java.util.function.Supplier;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/FileSystemOperationsAware.java

### Unused Code (1)
- Line 12: `import org.gradle.api.tasks.WorkResult;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/LazyFileOutputStream.java

### Resource Leak (1)
- Line 28: `delegate = new FileOutputStream(file);`

### Unused Code (5)
- Line 21: `private OutputStream delegate;`
- Line 12: `import java.io.File;`
- Line 13: `import java.io.FileOutputStream;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.io.OutputStream;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/LazyPropertyList.java

### Null Pointer (2)
- Line 173: `return delegate.stream()`
- Line 182: `return delegate.stream()`

### Unused Code (8)
- Line 11: `import org.gradle.api.tasks.Input;`
- Line 13: `import java.util.ArrayList;`
- Line 14: `import java.util.Collection;`
- Line 15: `import java.util.Iterator;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.ListIterator;`
- Line 18: `import java.util.function.Supplier;`
- Line 19: `import java.util.stream.Collectors;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/LazyPropertyMap.java

### Null Pointer (2)
- Line 121: `return delegate.entrySet()`
- Line 130: `return delegate.values()`

### Unused Code (10)
- Line 11: `import org.gradle.api.Named;`
- Line 12: `import org.gradle.api.tasks.Input;`
- Line 14: `import java.util.Collection;`
- Line 15: `import java.util.LinkedHashMap;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.Set;`
- Line 19: `import java.util.function.BiFunction;`
- Line 20: `import java.util.function.Supplier;`
- Line 21: `import java.util.stream.Collectors;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/LoggedExec.java

### Concurrency Issue (2)
- Line 60: `private static final Logger LOGGER = Logging.getLogger(LoggedExec.class);`
- Line 238: `private static final Pattern NEWLINE = Pattern.compile(System.lineSeparator());`

### Exception Handling (7)
- Line 152: `throw new GradleException("Capturing output is not supported when spoolOutput is true.");`
- Line 155: `throw new GradleException("Capturing output is not supported when indentingConsoleOutput is configured.");`
- Line 171: `throw new RuntimeException("could not log", e);`
- Line 199: `throw new GradleException("Cannot set standard input", e);`
- Line 216: `throw new GradleException("Failed to read exec output", e);`
- Line 253: `throw new UncheckedIOException(e);`
- Line 320: `throw new IllegalArgumentException("Cannot set commandline with empty list.");`

### Unused Code (40)
- Line 62: `private ProjectLayout projectLayout;`
- Line 63: `private ExecOperations execOperations;`
- Line 105: `private String output;`
- Line 11: `import org.gradle.api.Action;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.file.FileSystemOperations;`
- Line 15: `import org.gradle.api.file.ProjectLayout;`
- Line 16: `import org.gradle.api.logging.Logger;`
- Line 17: `import org.gradle.api.logging.Logging;`
- Line 18: `import org.gradle.api.provider.ListProperty;`
- Line 19: `import org.gradle.api.provider.MapProperty;`
- Line 20: `import org.gradle.api.provider.Property;`
- Line 21: `import org.gradle.api.provider.Provider;`
- Line 22: `import org.gradle.api.provider.ProviderFactory;`
- Line 23: `import org.gradle.api.tasks.CacheableTask;`
- Line 24: `import org.gradle.api.tasks.Input;`
- Line 25: `import org.gradle.api.tasks.Internal;`
- Line 26: `import org.gradle.api.tasks.Optional;`
- Line 27: `import org.gradle.api.tasks.TaskAction;`
- Line 28: `import org.gradle.api.tasks.WorkResult;`
- Line 29: `import org.gradle.process.BaseExecSpec;`
- Line 30: `import org.gradle.process.ExecOperations;`
- Line 31: `import org.gradle.process.ExecResult;`
- Line 32: `import org.gradle.process.ExecSpec;`
- Line 33: `import org.gradle.process.JavaExecSpec;`
- Line 35: `import java.io.ByteArrayInputStream;`
- Line 36: `import java.io.ByteArrayOutputStream;`
- Line 37: `import java.io.File;`
- Line 38: `import java.io.IOException;`
- Line 39: `import java.io.OutputStream;`
- Line 40: `import java.io.UncheckedIOException;`
- Line 41: `import java.io.UnsupportedEncodingException;`
- Line 42: `import java.nio.charset.StandardCharsets;`
- Line 43: `import java.nio.file.Files;`
- Line 44: `import java.util.List;`
- Line 45: `import java.util.function.Consumer;`
- Line 46: `import java.util.function.Function;`
- Line 47: `import java.util.regex.Pattern;`
- Line 49: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/NamedComponentScannerMock.java

### Unused Code (3)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.nio.file.Files;`
- Line 14: `import java.nio.file.Path;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/OS.java

### Exception Handling (2)
- Line 33: `throw new IllegalStateException("Can't determine OS from: " + os);`
- Line 65: `throw new IllegalArgumentException("No condition specified for " + missingOS);`

### Unused Code (5)
- Line 11: `import java.util.EnumMap;`
- Line 12: `import java.util.EnumSet;`
- Line 13: `import java.util.Map;`
- Line 14: `import java.util.Set;`
- Line 15: `import java.util.function.Supplier;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/ReaperPlugin.java

### Concurrency Issue (1)
- Line 28: `public static final String REAPER_SERVICE_NAME = "reaper";`

### Exception Handling (1)
- Line 43: `throw new IllegalArgumentException("ReaperPlugin can only be applied to the root project of a build");`

### Unused Code (5)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.file.ProjectLayout;`
- Line 16: `import java.io.File;`
- Line 18: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/ReaperService.java

### Concurrency Issue (2)
- Line 33: `private static final String REAPER_CLASS = "org/elasticsearch/gradle/reaper/Reaper.class";`
- Line 34: `private static final Pattern REAPER_JAR_PATH_PATTERN = Pattern.compile("file:(.*)!/" + REAPER_CLASS);`

### Exception Handling (6)
- Line 58: `throw new UncheckedIOException(e);`
- Line 70: `throw new UncheckedIOException(e);`
- Line 85: `throw new RuntimeException(e);`
- Line 116: `throw new RuntimeException(e);`
- Line 138: `throw new RuntimeException("Unable to locate " + REAPER_CLASS + " on build classpath.");`
- Line 156: `throw new UncheckedIOException(e);`

### Unused Code (17)
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.file.DirectoryProperty;`
- Line 14: `import org.gradle.api.logging.Logger;`
- Line 15: `import org.gradle.api.logging.Logging;`
- Line 16: `import org.gradle.api.services.BuildService;`
- Line 17: `import org.gradle.api.services.BuildServiceParameters;`
- Line 18: `import org.gradle.internal.jvm.Jvm;`
- Line 20: `import java.io.File;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.io.InputStream;`
- Line 23: `import java.io.OutputStream;`
- Line 24: `import java.io.UncheckedIOException;`
- Line 25: `import java.net.URL;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.util.regex.Matcher;`
- Line 29: `import java.util.regex.Pattern;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/Version.java

### Concurrency Issue (2)
- Line 42: `private static final Pattern pattern = Pattern.compile("(\\d+)\\.(\\d+)\\.(\\d+)(?:-(alpha\\d+|beta\\d+|rc\\d+|SNAPSHOT))?");`
- Line 44: `private static final Pattern relaxedPattern = Pattern.compile(`

### Exception Handling (1)
- Line 74: `throw new IllegalArgumentException("Invalid version format: '" + s + "'. Should be " + expected);`

### Unused Code (4)
- Line 11: `import java.io.Serializable;`
- Line 12: `import java.util.Objects;`
- Line 13: `import java.util.regex.Matcher;`
- Line 14: `import java.util.regex.Pattern;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/VersionProperties.java

### Exception Handling (2)
- Line 75: `throw new IllegalStateException("/version.properties resource missing");`
- Line 80: `throw new IllegalStateException("Failed to load version properties", e);`

### Unused Code (5)
- Line 11: `import java.io.IOException;`
- Line 12: `import java.io.InputStream;`
- Line 13: `import java.util.HashMap;`
- Line 14: `import java.util.Map;`
- Line 15: `import java.util.Properties;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/distribution/ArchiveElasticsearchDistributionType.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.gradle.Architecture;`
- Line 13: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 14: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 15: `import org.elasticsearch.gradle.Version;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/distribution/ElasticsearchDistributionTypes.java

### Concurrency Issue (1)
- Line 15: `public static final ElasticsearchDistributionType ARCHIVE = new ArchiveElasticsearchDistributionType();`

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/distribution/IntegTestZipElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/jarhell/JarHellPlugin.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.Task;`
- Line 17: `import org.gradle.api.artifacts.Configuration;`
- Line 18: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 19: `import org.gradle.api.tasks.SourceSet;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/jarhell/JarHellTask.java

### Concurrency Issue (2)
- Line 76: `public void setClasspath(FileCollection classpath) {`
- Line 85: `public void setJarHellRuntimeClasspath(FileCollection jarHellRuntimeClasspath) {`

### Unused Code (20)
- Line 37: `private FileCollection jarHellRuntimeClasspath;`
- Line 39: `private FileCollection classpath;`
- Line 40: `private ExecOperations execOperations;`
- Line 41: `private ProjectLayout projectLayout;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.ProjectLayout;`
- Line 16: `import org.gradle.api.tasks.CacheableTask;`
- Line 17: `import org.gradle.api.tasks.Classpath;`
- Line 18: `import org.gradle.api.tasks.CompileClasspath;`
- Line 19: `import org.gradle.api.tasks.OutputFile;`
- Line 20: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 21: `import org.gradle.api.tasks.TaskAction;`
- Line 22: `import org.gradle.process.ExecOperations;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.StandardOpenOption;`
- Line 29: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/BasePluginBuildPlugin.java

### Concurrency Issue (4)
- Line 55: `public static final String PLUGIN_EXTENSION_NAME = "esplugin";`
- Line 56: `public static final String BUNDLE_PLUGIN_TASK_NAME = "bundlePlugin";`
- Line 57: `public static final String EXPLODED_BUNDLE_PLUGIN_TASK_NAME = "explodedBundlePlugin";`
- Line 58: `public static final String EXPLODED_BUNDLE_CONFIG = "explodedBundleZip";`

### Unused Code (34)
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.elasticsearch.gradle.VersionProperties;`
- Line 14: `import org.elasticsearch.gradle.dependencies.CompileOnlyResolvePlugin;`
- Line 15: `import org.elasticsearch.gradle.jarhell.JarHellPlugin;`
- Line 16: `import org.elasticsearch.gradle.test.GradleTestPolicySetupPlugin;`
- Line 17: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 18: `import org.elasticsearch.gradle.testclusters.RunTask;`
- Line 19: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 20: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 21: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 22: `import org.gradle.api.Plugin;`
- Line 23: `import org.gradle.api.Project;`
- Line 24: `import org.gradle.api.Task;`
- Line 25: `import org.gradle.api.Transformer;`
- Line 26: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 27: `import org.gradle.api.attributes.Attribute;`
- Line 28: `import org.gradle.api.attributes.LibraryElements;`
- Line 29: `import org.gradle.api.file.CopySpec;`
- Line 30: `import org.gradle.api.file.FileCollection;`
- Line 31: `import org.gradle.api.file.RegularFile;`
- Line 32: `import org.gradle.api.plugins.BasePlugin;`
- Line 33: `import org.gradle.api.plugins.JavaPlugin;`
- Line 34: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 35: `import org.gradle.api.provider.Provider;`
- Line 36: `import org.gradle.api.provider.ProviderFactory;`
- Line 37: `import org.gradle.api.tasks.SourceSet;`
- Line 38: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 39: `import org.gradle.api.tasks.Sync;`
- Line 40: `import org.gradle.api.tasks.TaskProvider;`
- Line 41: `import org.gradle.api.tasks.bundling.Zip;`
- Line 43: `import java.io.File;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.concurrent.Callable;`
- Line 47: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/GenerateNamedComponentsTask.java

### Concurrency Issue (6)
- Line 76: `public void setClasspath(FileCollection classpath) {`
- Line 80: `public void setPluginScannerClasspath(FileCollection pluginScannerClasspath) {`
- Line 34: `private static final Logger LOGGER = Logging.getLogger(GenerateNamedComponentsTask.class);`
- Line 35: `private static final String NAMED_COMPONENTS_DIR = "generated-named-components/";`
- Line 36: `private static final String NAMED_COMPONENTS_FILE = "named_components.json";`
- Line 37: `private static final String NAMED_COMPONENTS_PATH = NAMED_COMPONENTS_DIR + NAMED_COMPONENTS_FILE;`

### Unused Code (22)
- Line 40: `private FileCollection pluginScannerClasspath;`
- Line 41: `private FileCollection classpath;`
- Line 42: `private ExecOperations execOperations;`
- Line 43: `private ProjectLayout projectLayout;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.ProjectLayout;`
- Line 16: `import org.gradle.api.file.RegularFileProperty;`
- Line 17: `import org.gradle.api.logging.Logger;`
- Line 18: `import org.gradle.api.logging.Logging;`
- Line 19: `import org.gradle.api.tasks.CompileClasspath;`
- Line 20: `import org.gradle.api.tasks.InputFiles;`
- Line 21: `import org.gradle.api.tasks.OutputFile;`
- Line 22: `import org.gradle.api.tasks.PathSensitive;`
- Line 23: `import org.gradle.api.tasks.PathSensitivity;`
- Line 24: `import org.gradle.api.tasks.TaskAction;`
- Line 25: `import org.gradle.process.ExecOperations;`
- Line 26: `import org.gradle.process.ExecResult;`
- Line 27: `import org.gradle.workers.WorkerExecutor;`
- Line 29: `import java.io.File;`
- Line 31: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/GeneratePluginPropertiesTask.java

### Resource Leak (1)
- Line 127: `var reader = new BufferedReader(new InputStreamReader(inputStream));`

### Concurrency Issue (2)
- Line 48: `public static final String PROPERTIES_FILENAME = "plugin-descriptor.properties";`
- Line 49: `public static final String STABLE_PROPERTIES_FILENAME = "stable-plugin-descriptor.properties";`

### Exception Handling (3)
- Line 103: `throw new InvalidUserDataException("classname is a required setting for esplugin");`
- Line 106: `throw new InvalidUserDataException("classname is a forbidden for stable esplugin");`
- Line 144: `throw new UncheckedIOException(e);`

### Unused Code (29)
- Line 12: `import groovy.text.SimpleTemplateEngine;`
- Line 13: `import groovy.text.Template;`
- Line 15: `import org.gradle.api.DefaultTask;`
- Line 16: `import org.gradle.api.InvalidUserDataException;`
- Line 17: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 18: `import org.gradle.api.file.ProjectLayout;`
- Line 19: `import org.gradle.api.file.RegularFileProperty;`
- Line 20: `import org.gradle.api.provider.ListProperty;`
- Line 21: `import org.gradle.api.provider.Property;`
- Line 22: `import org.gradle.api.tasks.CacheableTask;`
- Line 23: `import org.gradle.api.tasks.Input;`
- Line 24: `import org.gradle.api.tasks.InputFiles;`
- Line 25: `import org.gradle.api.tasks.Optional;`
- Line 26: `import org.gradle.api.tasks.OutputFile;`
- Line 27: `import org.gradle.api.tasks.PathSensitive;`
- Line 28: `import org.gradle.api.tasks.PathSensitivity;`
- Line 29: `import org.gradle.api.tasks.TaskAction;`
- Line 30: `import org.objectweb.asm.ClassReader;`
- Line 31: `import org.objectweb.asm.tree.ClassNode;`
- Line 33: `import java.io.BufferedReader;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.io.InputStreamReader;`
- Line 36: `import java.io.UncheckedIOException;`
- Line 37: `import java.nio.charset.StandardCharsets;`
- Line 38: `import java.nio.file.Files;`
- Line 39: `import java.nio.file.Path;`
- Line 40: `import java.util.HashMap;`
- Line 41: `import java.util.Map;`
- Line 43: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/PluginBuildPlugin.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.file.RegularFile;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.provider.ProviderFactory;`
- Line 19: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/PluginPropertiesExtension.java

### Concurrency Issue (10)
- Line 66: `public void setName(String name) {`
- Line 75: `public void setVersion(String version) {`
- Line 83: `public void setDescription(String description) {`
- Line 92: `public void setClassname(String classname) {`
- Line 104: `public void setHasNativeController(boolean hasNativeController) {`
- Line 120: `public void setRequiresKeystore(boolean requiresKeystore) {`
- Line 128: `public void setLicenseFile(File licenseFile) {`
- Line 141: `public void setNoticeFile(File noticeFile) {`
- Line 154: `public void setExtendedPlugins(List<String> extendedPlugins) {`
- Line 158: `public void setBundleSpec(CopySpec bundleSpec) {`

### Unused Code (18)
- Line 27: `private String name;`
- Line 29: `private String version;`
- Line 31: `private String description;`
- Line 33: `private String classname;`
- Line 38: `private boolean hasNativeController;`
- Line 41: `private boolean isLicensed = false;`
- Line 44: `private boolean requiresKeystore;`
- Line 47: `private File licenseFile;`
- Line 53: `private File noticeFile;`
- Line 56: `private CopySpec bundleSpec;`
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.api.file.CopySpec;`
- Line 14: `import org.gradle.api.file.RegularFileProperty;`
- Line 15: `import org.gradle.api.plugins.BasePluginExtension;`
- Line 16: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 18: `import java.io.File;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.List;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/plugin/StablePluginBuildPlugin.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.artifacts.Configuration;`
- Line 17: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 18: `import org.gradle.api.file.FileCollection;`
- Line 19: `import org.gradle.api.file.RegularFile;`
- Line 20: `import org.gradle.api.plugins.JavaPlugin;`
- Line 21: `import org.gradle.api.provider.Provider;`
- Line 22: `import org.gradle.api.tasks.SourceSet;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/test/GradleTestPolicySetupPlugin.java

### Unused Code (6)
- Line 12: `import org.gradle.api.JavaVersion;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.invocation.Gradle;`
- Line 16: `import org.gradle.api.tasks.testing.Test;`
- Line 18: `import java.util.List;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/test/JavaRestTestPlugin.java

### Unused Code (14)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.plugin.PluginBuildPlugin;`
- Line 14: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 15: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 16: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 17: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 18: `import org.gradle.api.Plugin;`
- Line 19: `import org.gradle.api.Project;`
- Line 20: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 21: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 22: `import org.gradle.api.tasks.TaskProvider;`
- Line 23: `import org.gradle.api.tasks.bundling.Zip;`
- Line 24: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`
- Line 26: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.BUNDLE_PLUGIN_TASK_NAME;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/test/SystemPropertyCommandLineArgumentProvider.java

### Null Pointer (1)
- Line 37: `return systemProperties.entrySet()`

### Unused Code (7)
- Line 11: `import org.gradle.api.provider.Provider;`
- Line 12: `import org.gradle.api.tasks.Input;`
- Line 13: `import org.gradle.process.CommandLineArgumentProvider;`
- Line 15: `import java.util.LinkedHashMap;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.function.Supplier;`
- Line 18: `import java.util.stream.Collectors;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/test/YamlRestTestPlugin.java

### Concurrency Issue (1)
- Line 45: `public static final String REST_TEST_SPECS_CONFIGURATION_NAME = "restTestSpecs";`

### Unused Code (28)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.plugin.BasePluginBuildPlugin;`
- Line 14: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 15: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 16: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 17: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 18: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 19: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 20: `import org.gradle.api.NamedDomainObjectProvider;`
- Line 21: `import org.gradle.api.Plugin;`
- Line 22: `import org.gradle.api.Project;`
- Line 23: `import org.gradle.api.Task;`
- Line 24: `import org.gradle.api.artifacts.Configuration;`
- Line 25: `import org.gradle.api.artifacts.ConfigurationContainer;`
- Line 26: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 27: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 28: `import org.gradle.api.attributes.Attribute;`
- Line 29: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 30: `import org.gradle.api.tasks.Copy;`
- Line 31: `import org.gradle.api.tasks.SourceSet;`
- Line 32: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 33: `import org.gradle.api.tasks.Sync;`
- Line 34: `import org.gradle.api.tasks.TaskProvider;`
- Line 35: `import org.gradle.api.tasks.bundling.Zip;`
- Line 36: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`
- Line 38: `import java.io.File;`
- Line 40: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.BUNDLE_PLUGIN_TASK_NAME;`
- Line 41: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.EXPLODED_BUNDLE_PLUGIN_TASK_NAME;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/DefaultTestClustersTask.java

### Unused Code (3)
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 13: `import java.util.Collection;`
- Line 14: `import java.util.HashSet;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/ElasticsearchCluster.java

### Concurrency Issue (8)
- Line 150: `protected void setShared(boolean shared) {`
- Line 66: `private static final Logger LOGGER = Logging.getLogger(ElasticsearchNode.class);`
- Line 67: `private static final int CLUSTER_UP_TIMEOUT = 40;`
- Line 68: `private static final TimeUnit CLUSTER_UP_TIMEOUT_UNIT = TimeUnit.SECONDS;`
- Line 70: `private final AtomicBoolean configurationFrozen = new AtomicBoolean(false);`
- Line 85: `private int nodeIndex = 0;`
- Line 89: `private boolean shared = false;`
- Line 91: `private int claims = 0;`

### Exception Handling (7)
- Line 169: `throw new IllegalArgumentException("Number of nodes should be >= 1 but was " + numberOfNodes + " for " + this);`
- Line 423: `throw new IllegalStateException("Configuration for " + this + " can not be altered, already locked");`
- Line 478: `throw new TestClustersException("Ran out of nodes to take to the next version");`
- Line 538: `throw new UncheckedIOException("Failed to write unicast_hosts for " + this, e);`
- Line 641: `throw new UncheckedIOException("IO error while waiting cluster", e);`
- Line 644: `throw new TestClustersException("Interrupted while waiting for " + this, e);`
- Line 646: `throw new RuntimeException("security exception", e);`

### Unused Code (53)
- Line 85: `private int nodeIndex = 0;`
- Line 89: `private boolean shared = false;`
- Line 91: `private int claims = 0;`
- Line 11: `import org.elasticsearch.gradle.FileSupplier;`
- Line 12: `import org.elasticsearch.gradle.PropertyNormalization;`
- Line 13: `import org.elasticsearch.gradle.ReaperService;`
- Line 14: `import org.elasticsearch.gradle.Version;`
- Line 15: `import org.gradle.api.Named;`
- Line 16: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.artifacts.Configuration;`
- Line 19: `import org.gradle.api.artifacts.Dependency;`
- Line 20: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 21: `import org.gradle.api.file.ArchiveOperations;`
- Line 22: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 23: `import org.gradle.api.file.FileCollection;`
- Line 24: `import org.gradle.api.file.FileSystemOperations;`
- Line 25: `import org.gradle.api.file.RegularFile;`
- Line 26: `import org.gradle.api.internal.file.FileOperations;`
- Line 27: `import org.gradle.api.logging.Logger;`
- Line 28: `import org.gradle.api.logging.Logging;`
- Line 29: `import org.gradle.api.provider.Provider;`
- Line 30: `import org.gradle.api.tasks.Classpath;`
- Line 31: `import org.gradle.api.tasks.InputFiles;`
- Line 32: `import org.gradle.api.tasks.Internal;`
- Line 33: `import org.gradle.api.tasks.Nested;`
- Line 34: `import org.gradle.api.tasks.PathSensitive;`
- Line 35: `import org.gradle.api.tasks.PathSensitivity;`
- Line 36: `import org.gradle.api.tasks.Sync;`
- Line 37: `import org.gradle.api.tasks.TaskProvider;`
- Line 38: `import org.gradle.api.tasks.bundling.AbstractArchiveTask;`
- Line 39: `import org.gradle.api.tasks.bundling.Zip;`
- Line 40: `import org.gradle.process.ExecOperations;`
- Line 42: `import java.io.File;`
- Line 43: `import java.io.IOException;`
- Line 44: `import java.io.UncheckedIOException;`
- Line 45: `import java.nio.charset.StandardCharsets;`
- Line 46: `import java.nio.file.Files;`
- Line 47: `import java.security.GeneralSecurityException;`
- Line 48: `import java.util.Collection;`
- Line 49: `import java.util.HashMap;`
- Line 50: `import java.util.LinkedHashMap;`
- Line 51: `import java.util.List;`
- Line 52: `import java.util.Map;`
- Line 53: `import java.util.Objects;`
- Line 54: `import java.util.concurrent.TimeUnit;`
- Line 55: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 56: `import java.util.function.Function;`
- Line 57: `import java.util.function.Predicate;`
- Line 58: `import java.util.function.Supplier;`
- Line 59: `import java.util.stream.Collectors;`
- Line 61: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.EXPLODED_BUNDLE_CONFIG;`
- Line 62: `import static org.elasticsearch.gradle.testclusters.TestClustersPlugin.BUNDLE_ATTRIBUTE;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/ElasticsearchNode.java

### Null Pointer (1)
- Line 1209: `IOException ioe = null;`

### Concurrency Issue (23)
- Line 276: `public void setTestDistribution(TestDistribution testDistribution) {`
- Line 431: `public void setPreserveDataDir(boolean preserveDataDir) {`
- Line 1024: `public void setNameCustomization(Function<String, String> nameCustomizer) {`
- Line 1663: `}`
- Line 1667: `}`
- Line 1671: `}`
- Line 100: `private static final Logger LOGGER = Logging.getLogger(ElasticsearchNode.class);`
- Line 101: `private static final int ES_DESTROY_TIMEOUT = 20;`
- Line 102: `private static final TimeUnit ES_DESTROY_TIMEOUT_UNIT = TimeUnit.SECONDS;`
- Line 104: `private static final int NODE_UP_TIMEOUT = 3;`
- Line 105: `private static final TimeUnit NODE_UP_TIMEOUT_UNIT = TimeUnit.MINUTES;`
- Line 106: `private static final int ADDITIONAL_CONFIG_TIMEOUT = 15;`
- Line 107: `private static final TimeUnit ADDITIONAL_CONFIG_TIMEOUT_UNIT = TimeUnit.SECONDS;`
- Line 117: `private static final int TAIL_LOG_MESSAGES_COUNT = 40;`
- Line 123: `private static final String HOSTNAME_OVERRIDE = "LinuxDarwinHostname";`
- Line 124: `private static final String COMPUTERNAME_OVERRIDE = "WindowsComputername";`
- Line 136: `private final AtomicBoolean configurationFrozen = new AtomicBoolean(false);`
- Line 170: `private int currentDistro = 0;`
- Line 173: `private boolean isWorkingDirConfigured = false;`
- Line 174: `private String httpPort = "0";`
- Line 175: `private String transportPort = "0";`
- Line 177: `private String keystorePassword = "";`
- Line 1177: `private static final int RETRY_DELETE_MILLIS = OS.current() == OS.WINDOWS ? 500 : 0;`

### Exception Handling (42)
- Line 304: `throw new UnsupportedOperationException("Not Supported API");`
- Line 308: `throw new UnsupportedOperationException("Not Supported API");`
- Line 318: `throw new IllegalStateException("Not Supported API");`
- Line 323: `throw new IllegalStateException("Not Supported API");`
- Line 480: `throw new UncheckedIOException(msg, e);`
- Line 524: `throw new TestClustersException("supplied keystore file " + file + " does not exist, require for " + this);`
- Line 570: `throw new UncheckedIOException(e);`
- Line 583: `throw new TestClustersException("Ran out of versions to go to for " + this);`
- Line 600: `throw new TestClustersException("Can't create extra config file from " + from + " for " + this + " as it does not exist");`
- Line 608: `throw new UncheckedIOException("Can't create extra config file for", e);`
- Line 627: `throw new IllegalArgumentException("extra jar file " + from + " doesn't appear to be a JAR");`
- Line 660: `throw new TestClustersException(`
- Line 670: `throw new UncheckedIOException("Can't append roles file " + from + " to " + dst, e);`
- Line 689: `throw new IllegalArgumentException("Not a valid module " + module + " for " + this);`
- Line 700: `throw new IllegalArgumentException("extra config file destination can't be relative, was " + destination + " for " + this);`
- Line 708: `throw new IllegalArgumentException("extra config file destination can't be relative, was " + destination + " for " + this);`
- Line 725: `throw new TestClustersException("Unknown keys in user definition " + keys + " for " + this);`
- Line 757: `throw new TestClustersException(`
- Line 777: `throw new UncheckedIOException("Failed to run " + tool + " for " + this, e);`
- Line 827: `throw new TestClustersException(`
- Line 862: `throw new IllegalStateException("testcluster does not allow overwriting the following env vars " + commonKeys + " for " + this);`
- Line 895: `throw new TestClustersException("Failed to set the keystore password for " + this, e);`
- Line 903: `throw new TestClustersException("Failed to start ES process for " + this, e);`
- Line 989: `throw new UncheckedIOException(e);`
- Line 1018: `throw new UncheckedIOException(e);`
- Line 1057: `throw new TestClustersException("Was not able to terminate elasticsearch process for " + this);`
- Line 1111: `throw new UncheckedIOException("Failed to tail log " + this, e);`
- Line 1150: `throw new TestClustersException("Found resource leaks in node log: " + from);`
- Line 1191: `throw new IOException("Interrupted while deleting.", x);`
- Line 1200: `throw new UncheckedIOException(e);`
- Line 1217: `throw new IOException("File still exists after " + times + " waits.");`
- Line 1284: `throw new LinkCreationException("Failed to create hard link " + d + " pointing to " + s, e);`
- Line 1294: `throw new UncheckedIOException("Failed to copy " + s + " to " + d, e);`
- Line 1343: `throw new UncheckedIOException("Can't walk source " + sourceRoot, e);`
- Line 1396: `throw new IllegalArgumentException(`
- Line 1426: `throw new UncheckedIOException("Could not write config file: " + configFile, e);`
- Line 1441: `throw new IOException("template property " + origin + " not found in template.");`
- Line 1447: `throw new UncheckedIOException(ioException);`
- Line 1467: `throw new IllegalStateException("Configuration for " + this + " can not be altered, already locked");`
- Line 1475: `throw new UncheckedIOException("Failed to read transport ports file: " + transportPortFile + " for " + this, e);`
- Line 1483: `throw new UncheckedIOException("Failed to read http ports file: " + httpPortsFile + " for " + this, e);`
- Line 1640: `throw new TestClustersException("Interrupted while waiting for ports files", e);`

### Infinite Loop (1)
- Line 1210: `while (true) {`

### Unused Code (94)
- Line 170: `private int currentDistro = 0;`
- Line 171: `private TestDistribution testDistribution;`
- Line 173: `private boolean isWorkingDirConfigured = false;`
- Line 174: `private String httpPort = "0";`
- Line 175: `private String transportPort = "0";`
- Line 176: `private Path confPathData;`
- Line 177: `private String keystorePassword = "";`
- Line 178: `private boolean preserveDataDir = false;`
- Line 1683: `private String name;`
- Line 1684: `private File file;`
- Line 11: `import org.apache.commons.io.FileUtils;`
- Line 12: `import org.elasticsearch.gradle.Architecture;`
- Line 13: `import org.elasticsearch.gradle.DistributionDownloadPlugin;`
- Line 14: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 15: `import org.elasticsearch.gradle.FileSupplier;`
- Line 16: `import org.elasticsearch.gradle.LazyPropertyList;`
- Line 17: `import org.elasticsearch.gradle.LazyPropertyMap;`
- Line 18: `import org.elasticsearch.gradle.LoggedExec;`
- Line 19: `import org.elasticsearch.gradle.OS;`
- Line 20: `import org.elasticsearch.gradle.PropertyNormalization;`
- Line 21: `import org.elasticsearch.gradle.ReaperService;`
- Line 22: `import org.elasticsearch.gradle.Version;`
- Line 23: `import org.elasticsearch.gradle.VersionProperties;`
- Line 24: `import org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes;`
- Line 25: `import org.elasticsearch.gradle.util.Pair;`
- Line 26: `import org.gradle.api.Action;`
- Line 27: `import org.gradle.api.Named;`
- Line 28: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 29: `import org.gradle.api.Project;`
- Line 30: `import org.gradle.api.file.ArchiveOperations;`
- Line 31: `import org.gradle.api.file.FileCollection;`
- Line 32: `import org.gradle.api.file.FileSystemOperations;`
- Line 33: `import org.gradle.api.file.FileTree;`
- Line 34: `import org.gradle.api.file.RegularFile;`
- Line 35: `import org.gradle.api.internal.file.FileOperations;`
- Line 36: `import org.gradle.api.logging.Logger;`
- Line 37: `import org.gradle.api.logging.Logging;`
- Line 38: `import org.gradle.api.provider.Provider;`
- Line 39: `import org.gradle.api.tasks.Classpath;`
- Line 40: `import org.gradle.api.tasks.Input;`
- Line 41: `import org.gradle.api.tasks.InputFile;`
- Line 42: `import org.gradle.api.tasks.InputFiles;`
- Line 43: `import org.gradle.api.tasks.Internal;`
- Line 44: `import org.gradle.api.tasks.Nested;`
- Line 45: `import org.gradle.api.tasks.Optional;`
- Line 46: `import org.gradle.api.tasks.PathSensitive;`
- Line 47: `import org.gradle.api.tasks.PathSensitivity;`
- Line 48: `import org.gradle.api.tasks.Sync;`
- Line 49: `import org.gradle.api.tasks.TaskProvider;`
- Line 50: `import org.gradle.api.tasks.bundling.Zip;`
- Line 51: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 52: `import org.gradle.process.ExecOperations;`
- Line 54: `import java.io.ByteArrayInputStream;`
- Line 55: `import java.io.File;`
- Line 56: `import java.io.IOException;`
- Line 57: `import java.io.InputStream;`
- Line 58: `import java.io.LineNumberReader;`
- Line 59: `import java.io.PrintWriter;`
- Line 60: `import java.io.StringWriter;`
- Line 61: `import java.io.UncheckedIOException;`
- Line 62: `import java.net.URL;`
- Line 63: `import java.nio.charset.StandardCharsets;`
- Line 64: `import java.nio.file.FileVisitResult;`
- Line 65: `import java.nio.file.Files;`
- Line 66: `import java.nio.file.NoSuchFileException;`
- Line 67: `import java.nio.file.Path;`
- Line 68: `import java.nio.file.SimpleFileVisitor;`
- Line 69: `import java.nio.file.StandardCopyOption;`
- Line 70: `import java.nio.file.StandardOpenOption;`
- Line 71: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 72: `import java.time.Instant;`
- Line 73: `import java.util.ArrayList;`
- Line 74: `import java.util.Arrays;`
- Line 75: `import java.util.Collections;`
- Line 76: `import java.util.HashMap;`
- Line 77: `import java.util.HashSet;`
- Line 78: `import java.util.LinkedHashMap;`
- Line 79: `import java.util.LinkedList;`
- Line 80: `import java.util.List;`
- Line 81: `import java.util.Map;`
- Line 82: `import java.util.Objects;`
- Line 83: `import java.util.Set;`
- Line 84: `import java.util.concurrent.ExecutionException;`
- Line 85: `import java.util.concurrent.TimeUnit;`
- Line 86: `import java.util.concurrent.TimeoutException;`
- Line 87: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 88: `import java.util.function.BiConsumer;`
- Line 89: `import java.util.function.Function;`
- Line 90: `import java.util.function.Predicate;`
- Line 91: `import java.util.function.Supplier;`
- Line 92: `import java.util.stream.Collectors;`
- Line 93: `import java.util.stream.Stream;`
- Line 95: `import static java.util.Objects.requireNonNull;`
- Line 96: `import static java.util.Optional.ofNullable;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/MockApmServer.java

### Null Pointer (1)
- Line 90: `instance = null;`

### Concurrency Issue (2)
- Line 36: `private static final Logger logger = Logging.getLogger(MockApmServer.class);`
- Line 117: `private static final int STOP_TIME = 3;`

### Exception Handling (2)
- Line 110: `} catch (Exception e) {`
- Line 129: `} catch (Exception e) {`

### Unused Code (11)
- Line 37: `private int port;`
- Line 12: `import com.sun.net.httpserver.HttpExchange;`
- Line 13: `import com.sun.net.httpserver.HttpHandler;`
- Line 14: `import com.sun.net.httpserver.HttpServer;`
- Line 16: `import org.gradle.api.logging.Logger;`
- Line 17: `import org.gradle.api.logging.Logging;`
- Line 19: `import java.io.ByteArrayOutputStream;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.io.InputStream;`
- Line 22: `import java.io.OutputStream;`
- Line 23: `import java.net.InetSocketAddress;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/RunTask.java

### Concurrency Issue (20)
- Line 64: `public void setDebug(boolean enabled) {`
- Line 69: `public void setCliDebug(boolean enabled) {`
- Line 100: `public void setApmServerEnabled(Boolean apmServerEnabled) {`
- Line 115: `public void setPreserveData(Boolean preserveData) {`
- Line 140: `public void setUseHttps(boolean useHttps) {`
- Line 151: `public void setUseTransportTls(boolean useTransportTls) {`
- Line 37: `public static final String CUSTOM_SETTINGS_PREFIX = "tests.es.";`
- Line 38: `private static final Logger logger = Logging.getLogger(RunTask.class);`
- Line 39: `private static final String tlsCertificateAuthority = "public-ca.pem";`
- Line 40: `private static final String httpsCertificate = "private-cert1.p12";`
- Line 41: `private static final String transportCertificate = "private-cert2.p12";`
- Line 43: `private Boolean debug = false;`
- Line 44: `private Boolean cliDebug = false;`
- Line 46: `private Boolean apmServerEnabled = false;`
- Line 48: `private Boolean preserveData = false;`
- Line 50: `private Path dataDir = null;`
- Line 52: `private String keystorePassword = "";`
- Line 54: `private Boolean useHttps = false;`
- Line 56: `private Boolean useTransportTls = false;`
- Line 58: `private final Path tlsBasePath = Path.of(`

### Exception Handling (1)
- Line 273: `throw new GradleException("Elasticsearch cluster died");`

### Unused Code (31)
- Line 43: `private Boolean debug = false;`
- Line 44: `private Boolean cliDebug = false;`
- Line 46: `private Boolean apmServerEnabled = false;`
- Line 48: `private Boolean preserveData = false;`
- Line 50: `private Path dataDir = null;`
- Line 52: `private String keystorePassword = "";`
- Line 54: `private Boolean useHttps = false;`
- Line 56: `private Boolean useTransportTls = false;`
- Line 61: `private MockApmServer mockServer;`
- Line 11: `import org.gradle.api.GradleException;`
- Line 12: `import org.gradle.api.logging.Logger;`
- Line 13: `import org.gradle.api.logging.Logging;`
- Line 14: `import org.gradle.api.tasks.Input;`
- Line 15: `import org.gradle.api.tasks.Optional;`
- Line 16: `import org.gradle.api.tasks.TaskAction;`
- Line 17: `import org.gradle.api.tasks.options.Option;`
- Line 19: `import java.io.BufferedReader;`
- Line 20: `import java.io.Closeable;`
- Line 21: `import java.io.File;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.nio.file.Paths;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.HashSet;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Set;`
- Line 31: `import java.util.function.BooleanSupplier;`
- Line 32: `import java.util.function.Function;`
- Line 33: `import java.util.stream.Collectors;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/SslTrustResolver.java

### Resource Leak (2)
- Line 200: `try (InputStream input = new FileInputStream(file)) {`
- Line 208: `try (InputStream input = new FileInputStream(pemFile)) {`

### Concurrency Issue (6)
- Line 49: `public void setCertificateAuthorities(File... certificateAuthorities) {`
- Line 53: `public void setTrustStoreFile(File trustStoreFile) {`
- Line 57: `public void setTrustStorePassword(String trustStorePassword) {`
- Line 61: `public void setServerCertificate(File serverCertificate) {`
- Line 65: `public void setServerKeystoreFile(File keyStoreFile) {`
- Line 69: `public void setServerKeystorePassword(String keyStorePassword) {`

### Exception Handling (3)
- Line 113: `throw new IllegalStateException("Expected to configure trust, but all configuration values are null");`
- Line 138: `throw new IllegalStateException("Trust-store does not contain any trusted certificate entries");`
- Line 177: `throw new CertificateException("This trust manager is for client use only and cannot trust other clients");`

### Unused Code (32)
- Line 43: `private File trustStoreFile;`
- Line 44: `private String trustStorePassword;`
- Line 45: `private File serverCertificate;`
- Line 46: `private File serverKeyStoreFile;`
- Line 47: `private String serverKeyStorePassword;`
- Line 12: `import java.io.File;`
- Line 13: `import java.io.FileInputStream;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.io.InputStream;`
- Line 16: `import java.security.GeneralSecurityException;`
- Line 17: `import java.security.KeyStore;`
- Line 18: `import java.security.KeyStoreException;`
- Line 19: `import java.security.SecureRandom;`
- Line 20: `import java.security.cert.Certificate;`
- Line 21: `import java.security.cert.CertificateException;`
- Line 22: `import java.security.cert.CertificateFactory;`
- Line 23: `import java.security.cert.X509Certificate;`
- Line 24: `import java.util.Arrays;`
- Line 25: `import java.util.Collection;`
- Line 26: `import java.util.Enumeration;`
- Line 27: `import java.util.HashSet;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Locale;`
- Line 30: `import java.util.Objects;`
- Line 31: `import java.util.Set;`
- Line 32: `import java.util.stream.Collectors;`
- Line 33: `import java.util.stream.Stream;`
- Line 35: `import javax.net.ssl.KeyManager;`
- Line 36: `import javax.net.ssl.SSLContext;`
- Line 37: `import javax.net.ssl.TrustManager;`
- Line 38: `import javax.net.ssl.TrustManagerFactory;`
- Line 39: `import javax.net.ssl.X509TrustManager;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/StandaloneRestIntegTestTask.java

### Concurrency Issue (2)
- Line 55: `public void setDebugServer(boolean enabled) {`
- Line 43: `private boolean debugServer = false;`

### Unused Code (20)
- Line 43: `private boolean debugServer = false;`
- Line 11: `import org.elasticsearch.gradle.FileSystemOperationsAware;`
- Line 12: `import org.gradle.api.provider.ProviderFactory;`
- Line 13: `import org.gradle.api.services.internal.BuildServiceProvider;`
- Line 14: `import org.gradle.api.services.internal.BuildServiceRegistryInternal;`
- Line 15: `import org.gradle.api.tasks.CacheableTask;`
- Line 16: `import org.gradle.api.tasks.Internal;`
- Line 17: `import org.gradle.api.tasks.Nested;`
- Line 18: `import org.gradle.api.tasks.WorkResult;`
- Line 19: `import org.gradle.api.tasks.options.Option;`
- Line 20: `import org.gradle.api.tasks.testing.Test;`
- Line 21: `import org.gradle.internal.resources.ResourceLock;`
- Line 22: `import org.gradle.internal.resources.SharedResource;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.Collection;`
- Line 26: `import java.util.Collections;`
- Line 27: `import java.util.HashSet;`
- Line 28: `import java.util.List;`
- Line 30: `import javax.inject.Inject;`
- Line 32: `import static org.elasticsearch.gradle.testclusters.TestClustersPlugin.THROTTLE_SERVICE_NAME;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClusterConfiguration.java

### Exception Handling (3)
- Line 145: `throw new TestClustersException("process was found dead while waiting for " + description + ", " + this);`
- Line 169: `throw new TestClustersException(message);`
- Line 181: `throw new TestClustersException(message + extraCause, lastException);`

### Unused Code (20)
- Line 11: `import org.elasticsearch.gradle.FileSupplier;`
- Line 12: `import org.elasticsearch.gradle.PropertyNormalization;`
- Line 13: `import org.elasticsearch.gradle.Version;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.RegularFile;`
- Line 16: `import org.gradle.api.logging.Logging;`
- Line 17: `import org.gradle.api.provider.Provider;`
- Line 18: `import org.gradle.api.tasks.Sync;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 20: `import org.gradle.api.tasks.bundling.Zip;`
- Line 21: `import org.slf4j.Logger;`
- Line 23: `import java.io.File;`
- Line 24: `import java.util.LinkedHashMap;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Locale;`
- Line 27: `import java.util.Map;`
- Line 28: `import java.util.concurrent.TimeUnit;`
- Line 29: `import java.util.function.Function;`
- Line 30: `import java.util.function.Predicate;`
- Line 31: `import java.util.function.Supplier;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClusterInfo.java

### Unused Code (2)
- Line 11: `import java.io.File;`
- Line 12: `import java.util.List;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClusterValueSource.java

### Unused Code (4)
- Line 12: `import org.gradle.api.provider.Property;`
- Line 13: `import org.gradle.api.provider.ValueSource;`
- Line 14: `import org.gradle.api.provider.ValueSourceParameters;`
- Line 15: `import org.jetbrains.annotations.Nullable;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClustersAware.java

### Unused Code (9)
- Line 11: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 12: `import org.gradle.api.Task;`
- Line 13: `import org.gradle.api.provider.Property;`
- Line 14: `import org.gradle.api.provider.Provider;`
- Line 15: `import org.gradle.api.services.ServiceReference;`
- Line 16: `import org.gradle.api.tasks.Nested;`
- Line 18: `import java.util.Collection;`
- Line 20: `import static org.elasticsearch.gradle.testclusters.TestClustersPlugin.REGISTRY_SERVICE_NAME;`
- Line 21: `import static org.elasticsearch.gradle.testclusters.TestClustersPlugin.TEST_CLUSTER_TASKS_SERVICE;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClustersPlugin.java

### Concurrency Issue (8)
- Line 91: `public void setRuntimeJava(Provider<File> runtimeJava) {`
- Line 95: `public void setIsReleasedVersion(Function<Version, Boolean> isReleasedVersion) {`
- Line 55: `public static final String EXTENSION_NAME = "testClusters";`
- Line 56: `public static final String THROTTLE_SERVICE_NAME = "testClustersThrottle";`
- Line 58: `private static final String LIST_TASK_NAME = "listTestClusters";`
- Line 59: `public static final String REGISTRY_SERVICE_NAME = "testClustersRegistry";`
- Line 60: `private static final Logger logger = Logging.getLogger(TestClustersPlugin.class);`
- Line 61: `public static final String TEST_CLUSTER_TASKS_SERVICE = "testClusterTasksService";`

### Exception Handling (4)
- Line 68: `throw new UnsupportedOperationException();`
- Line 73: `throw new UnsupportedOperationException();`
- Line 78: `throw new UnsupportedOperationException();`
- Line 83: `throw new UnsupportedOperationException();`

### Unused Code (36)
- Line 11: `import org.elasticsearch.gradle.DistributionDownloadPlugin;`
- Line 12: `import org.elasticsearch.gradle.ReaperPlugin;`
- Line 13: `import org.elasticsearch.gradle.ReaperService;`
- Line 14: `import org.elasticsearch.gradle.Version;`
- Line 15: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 16: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 17: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 18: `import org.gradle.api.Plugin;`
- Line 19: `import org.gradle.api.Project;`
- Line 20: `import org.gradle.api.Task;`
- Line 21: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 22: `import org.gradle.api.attributes.Attribute;`
- Line 23: `import org.gradle.api.file.ArchiveOperations;`
- Line 24: `import org.gradle.api.file.FileSystemOperations;`
- Line 25: `import org.gradle.api.internal.file.FileOperations;`
- Line 26: `import org.gradle.api.invocation.Gradle;`
- Line 27: `import org.gradle.api.logging.Logger;`
- Line 28: `import org.gradle.api.logging.Logging;`
- Line 29: `import org.gradle.api.provider.Property;`
- Line 30: `import org.gradle.api.provider.Provider;`
- Line 31: `import org.gradle.api.provider.ProviderFactory;`
- Line 32: `import org.gradle.api.services.BuildService;`
- Line 33: `import org.gradle.api.services.BuildServiceParameters;`
- Line 34: `import org.gradle.build.event.BuildEventsListenerRegistry;`
- Line 35: `import org.gradle.internal.jvm.Jvm;`
- Line 36: `import org.gradle.process.ExecOperations;`
- Line 37: `import org.gradle.tooling.events.FinishEvent;`
- Line 38: `import org.gradle.tooling.events.OperationCompletionListener;`
- Line 39: `import org.gradle.tooling.events.task.TaskFailureResult;`
- Line 40: `import org.gradle.tooling.events.task.TaskFinishEvent;`
- Line 42: `import java.io.File;`
- Line 43: `import java.util.HashMap;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.function.Function;`
- Line 47: `import javax.inject.Inject;`
- Line 49: `import static org.elasticsearch.gradle.util.GradleUtils.noop;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClustersRegistry.java

### Concurrency Issue (3)
- Line 27: `private static final Logger logger = Logging.getLogger(TestClustersRegistry.class);`
- Line 28: `private static final String TESTCLUSTERS_INSPECT_FAILURE = "testclusters.inspect.failure";`
- Line 29: `private final Boolean allowClusterToSurvive = Boolean.valueOf(System.getProperty(TESTCLUSTERS_INSPECT_FAILURE, "false"));`

### Infinite Loop (1)
- Line 65: `for (int i = 1;; i += i) {`

### Unused Code (12)
- Line 11: `import org.gradle.api.logging.Logger;`
- Line 12: `import org.gradle.api.logging.Logging;`
- Line 13: `import org.gradle.api.provider.Provider;`
- Line 14: `import org.gradle.api.provider.ProviderFactory;`
- Line 15: `import org.gradle.api.services.BuildService;`
- Line 16: `import org.gradle.api.services.BuildServiceParameters;`
- Line 18: `import java.util.HashMap;`
- Line 19: `import java.util.HashSet;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.stream.Collectors;`
- Line 24: `import javax.inject.Inject;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/TestClustersThrottle.java

### Unused Code (2)
- Line 11: `import org.gradle.api.services.BuildService;`
- Line 12: `import org.gradle.api.services.BuildServiceParameters;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/testclusters/WaitForHttpResource.java

### Concurrency Issue (4)
- Line 56: `public void setValidResponseCodes(int... validResponseCodes) {`
- Line 87: `public void setUsername(String username) {`
- Line 91: `public void setPassword(String password) {`
- Line 38: `private static final Logger logger = Logging.getLogger(WaitForHttpResource.class);`

### Exception Handling (2)
- Line 142: `throw new IllegalStateException("SSL trust has been configured, but [" + url + "] is not a 'https' URL");`
- Line 150: `throw new IllegalStateException("Basic Auth user [" + username + "] has been set, but no password has been configured");`

### Infinite Loop (1)
- Line 101: `while (true) {`

### Unused Code (18)
- Line 44: `private String username;`
- Line 45: `private String password;`
- Line 12: `import org.gradle.api.logging.Logger;`
- Line 13: `import org.gradle.api.logging.Logging;`
- Line 15: `import java.io.File;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.net.HttpURLConnection;`
- Line 18: `import java.net.MalformedURLException;`
- Line 19: `import java.net.URL;`
- Line 20: `import java.nio.charset.StandardCharsets;`
- Line 21: `import java.security.GeneralSecurityException;`
- Line 22: `import java.util.Base64;`
- Line 23: `import java.util.Collections;`
- Line 24: `import java.util.HashSet;`
- Line 25: `import java.util.Set;`
- Line 26: `import java.util.concurrent.TimeUnit;`
- Line 28: `import javax.net.ssl.HttpsURLConnection;`
- Line 29: `import javax.net.ssl.SSLContext;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/transform/FilteringJarTransform.java

### Resource Leak (1)
- Line 53: `ZipOutputStream output = new ZipOutputStream(new BufferedOutputStream(new FileOutputStream(transformed)))`

### Exception Handling (1)
- Line 68: `throw new UncheckedIOException("Failed to patch archive", e);`

### Unused Code (25)
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 14: `import org.gradle.api.artifacts.transform.InputArtifact;`
- Line 15: `import org.gradle.api.artifacts.transform.TransformAction;`
- Line 16: `import org.gradle.api.artifacts.transform.TransformOutputs;`
- Line 17: `import org.gradle.api.artifacts.transform.TransformParameters;`
- Line 18: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 19: `import org.gradle.api.file.FileSystemLocation;`
- Line 20: `import org.gradle.api.provider.Provider;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 23: `import java.io.BufferedOutputStream;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.FileOutputStream;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.Serializable;`
- Line 28: `import java.io.UncheckedIOException;`
- Line 29: `import java.nio.file.FileSystems;`
- Line 30: `import java.nio.file.Path;`
- Line 31: `import java.nio.file.PathMatcher;`
- Line 32: `import java.util.ArrayList;`
- Line 33: `import java.util.Enumeration;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.zip.ZipEntry;`
- Line 36: `import java.util.zip.ZipFile;`
- Line 37: `import java.util.zip.ZipOutputStream;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/transform/SymbolicLinkPreservingUntarTransform.java

### Resource Leak (2)
- Line 34: `TarArchiveInputStream tar = new TarArchiveInputStream(new GzipCompressorInputStream(new FileInputStream(tarFile)));`
- Line 56: `try (FileOutputStream fos = new FileOutputStream(destination.toFile())) {`

### Concurrency Issue (1)
- Line 30: `private static final Path CURRENT_DIR_PATH = Paths.get(".");`

### Unused Code (13)
- Line 12: `import org.apache.commons.compress.archivers.tar.TarArchiveEntry;`
- Line 13: `import org.apache.commons.compress.archivers.tar.TarArchiveInputStream;`
- Line 14: `import org.apache.commons.compress.compressors.gzip.GzipCompressorInputStream;`
- Line 15: `import org.gradle.api.artifacts.transform.TransformOutputs;`
- Line 17: `import java.io.File;`
- Line 18: `import java.io.FileInputStream;`
- Line 19: `import java.io.FileOutputStream;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.nio.file.Files;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.nio.file.Paths;`
- Line 24: `import java.util.function.Function;`
- Line 26: `import static org.elasticsearch.gradle.util.PermissionUtils.chmod;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/transform/UnpackTransform.java

### Resource Leak (1)
- Line 158: `try (InputStream is = new DigestInputStream(new FileInputStream(file), digest)) {`

### Unused Code (27)
- Line 12: `import org.gradle.api.artifacts.transform.InputArtifact;`
- Line 13: `import org.gradle.api.artifacts.transform.TransformAction;`
- Line 14: `import org.gradle.api.artifacts.transform.TransformOutputs;`
- Line 15: `import org.gradle.api.artifacts.transform.TransformParameters;`
- Line 16: `import org.gradle.api.file.FileSystemLocation;`
- Line 17: `import org.gradle.api.logging.Logger;`
- Line 18: `import org.gradle.api.logging.Logging;`
- Line 19: `import org.gradle.api.provider.Property;`
- Line 20: `import org.gradle.api.provider.Provider;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 22: `import org.gradle.api.tasks.Internal;`
- Line 23: `import org.gradle.api.tasks.Optional;`
- Line 24: `import org.gradle.api.tasks.PathSensitive;`
- Line 25: `import org.gradle.api.tasks.PathSensitivity;`
- Line 27: `import java.io.File;`
- Line 28: `import java.io.FileInputStream;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.io.InputStream;`
- Line 31: `import java.io.UncheckedIOException;`
- Line 32: `import java.nio.file.Path;`
- Line 33: `import java.nio.file.Paths;`
- Line 34: `import java.security.DigestInputStream;`
- Line 35: `import java.security.MessageDigest;`
- Line 36: `import java.security.NoSuchAlgorithmException;`
- Line 37: `import java.util.HexFormat;`
- Line 38: `import java.util.List;`
- Line 39: `import java.util.function.Function;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/transform/UnzipTransform.java

### Resource Leak (1)
- Line 50: `try (FileOutputStream outputStream = new FileOutputStream(outputPath.toFile())) {`

### Unused Code (13)
- Line 12: `import org.apache.commons.io.IOUtils;`
- Line 13: `import org.apache.tools.zip.ZipEntry;`
- Line 14: `import org.apache.tools.zip.ZipFile;`
- Line 15: `import org.gradle.api.artifacts.transform.TransformOutputs;`
- Line 16: `import org.gradle.api.logging.Logging;`
- Line 18: `import java.io.File;`
- Line 19: `import java.io.FileOutputStream;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.nio.file.Files;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.util.Enumeration;`
- Line 24: `import java.util.function.Function;`
- Line 26: `import static org.elasticsearch.gradle.util.PermissionUtils.chmod;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/util/FileUtils.java

### Exception Handling (3)
- Line 74: `throw new UncheckedIOException(e);`
- Line 82: `throw new UncheckedIOException(e);`
- Line 90: `throw new UncheckedIOException(e);`

### Unused Code (6)
- Line 12: `import org.gradle.api.UncheckedIOException;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.util.Collections;`
- Line 17: `import java.util.LinkedList;`
- Line 18: `import java.util.List;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/util/GradleUtils.java

### Exception Handling (1)
- Line 79: `throw new GradleException("Unable to find build service with name '" + name + "'.");`

### Unused Code (28)
- Line 11: `import org.gradle.api.Action;`
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.UnknownTaskException;`
- Line 16: `import org.gradle.api.artifacts.Configuration;`
- Line 17: `import org.gradle.api.artifacts.ModuleDependency;`
- Line 18: `import org.gradle.api.artifacts.ProjectDependency;`
- Line 19: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 20: `import org.gradle.api.plugins.JavaPlugin;`
- Line 21: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 22: `import org.gradle.api.provider.Provider;`
- Line 23: `import org.gradle.api.services.BuildService;`
- Line 24: `import org.gradle.api.services.BuildServiceRegistration;`
- Line 25: `import org.gradle.api.services.BuildServiceRegistry;`
- Line 26: `import org.gradle.api.specs.Spec;`
- Line 27: `import org.gradle.api.tasks.SourceSet;`
- Line 28: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 29: `import org.gradle.api.tasks.TaskContainer;`
- Line 30: `import org.gradle.api.tasks.TaskProvider;`
- Line 31: `import org.gradle.api.tasks.testing.Test;`
- Line 32: `import org.gradle.plugins.ide.eclipse.model.EclipseModel;`
- Line 33: `import org.gradle.plugins.ide.idea.model.IdeaModel;`
- Line 35: `import java.util.ArrayList;`
- Line 36: `import java.util.Arrays;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Map;`
- Line 39: `import java.util.function.Function;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/util/PermissionUtils.java

### Exception Handling (1)
- Line 38: `throw new IllegalArgumentException("permissions [" + permissions + "] out of range");`

### Unused Code (7)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.nio.file.Files;`
- Line 14: `import java.nio.file.Path;`
- Line 15: `import java.nio.file.attribute.PosixFileAttributeView;`
- Line 16: `import java.nio.file.attribute.PosixFilePermission;`
- Line 17: `import java.nio.file.attribute.PosixFilePermissions;`
- Line 18: `import java.util.Set;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/util/PlatformUtils.java

### Null Pointer (1)
- Line 17: `return input.lines()`

### Unused Code (1)
- Line 12: `import java.util.stream.Collectors;`

## ../build-tools/src/main/java/org/elasticsearch/gradle/dependencies/CompileOnlyResolvePlugin.java

### Unused Code (5)
- Line 12: `import org.gradle.api.NamedDomainObjectProvider;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.artifacts.Configuration;`
- Line 16: `import org.gradle.api.plugins.JavaPlugin;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/BuildConfigurationAwareGradleRunner.java

### Unused Code (12)
- Line 12: `import org.gradle.testkit.runner.BuildResult;`
- Line 13: `import org.gradle.testkit.runner.GradleRunner;`
- Line 14: `import org.gradle.testkit.runner.InvalidPluginMetadataException;`
- Line 15: `import org.gradle.testkit.runner.InvalidRunnerConfigurationException;`
- Line 16: `import org.gradle.testkit.runner.UnexpectedBuildFailure;`
- Line 17: `import org.gradle.testkit.runner.UnexpectedBuildSuccess;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.Writer;`
- Line 21: `import java.net.URI;`
- Line 22: `import java.util.ArrayList;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/InMemoryJavaCompiler.java

### Null Pointer (1)
- Line 108: `return files.stream()`

### Exception Handling (1)
- Line 156: `throw new RuntimeException("Could not compile " + className + " with source code " + sourceCode);`

### Unused Code (17)
- Line 12: `import java.io.ByteArrayOutputStream;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.OutputStream;`
- Line 15: `import java.net.URI;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.function.Supplier;`
- Line 19: `import java.util.stream.Collectors;`
- Line 21: `import javax.tools.FileObject;`
- Line 22: `import javax.tools.ForwardingJavaFileManager;`
- Line 23: `import javax.tools.JavaCompiler;`
- Line 24: `import javax.tools.JavaCompiler.CompilationTask;`
- Line 25: `import javax.tools.JavaFileManager;`
- Line 26: `import javax.tools.JavaFileObject;`
- Line 27: `import javax.tools.JavaFileObject.Kind;`
- Line 28: `import javax.tools.SimpleJavaFileObject;`
- Line 29: `import javax.tools.ToolProvider;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/InternalAwareGradleRunner.java

### Unused Code (14)
- Line 28: `private GradleRunner delegate;`
- Line 12: `import org.gradle.testkit.runner.BuildResult;`
- Line 13: `import org.gradle.testkit.runner.GradleRunner;`
- Line 14: `import org.gradle.testkit.runner.InvalidPluginMetadataException;`
- Line 15: `import org.gradle.testkit.runner.InvalidRunnerConfigurationException;`
- Line 16: `import org.gradle.testkit.runner.UnexpectedBuildFailure;`
- Line 17: `import org.gradle.testkit.runner.UnexpectedBuildSuccess;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.Writer;`
- Line 21: `import java.net.URI;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.stream.Collectors;`
- Line 25: `import java.util.stream.Stream;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/JarUtils.java

### Unused Code (12)
- Line 12: `import java.io.ByteArrayInputStream;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.OutputStream;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Path;`
- Line 17: `import java.nio.file.StandardOpenOption;`
- Line 18: `import java.util.Map;`
- Line 19: `import java.util.jar.JarEntry;`
- Line 20: `import java.util.jar.JarOutputStream;`
- Line 21: `import java.util.jar.Manifest;`
- Line 23: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 24: `import static java.util.stream.Collectors.toUnmodifiableMap;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/NormalizeOutputGradleRunner.java

### Unused Code (17)
- Line 31: `private GradleRunner delegate;`
- Line 162: `private BuildResult delegate;`
- Line 163: `private String normalizedString;`
- Line 12: `import org.gradle.testkit.runner.BuildResult;`
- Line 13: `import org.gradle.testkit.runner.BuildTask;`
- Line 14: `import org.gradle.testkit.runner.GradleRunner;`
- Line 15: `import org.gradle.testkit.runner.InvalidPluginMetadataException;`
- Line 16: `import org.gradle.testkit.runner.InvalidRunnerConfigurationException;`
- Line 17: `import org.gradle.testkit.runner.TaskOutcome;`
- Line 18: `import org.gradle.testkit.runner.UnexpectedBuildFailure;`
- Line 19: `import org.gradle.testkit.runner.UnexpectedBuildSuccess;`
- Line 21: `import java.io.File;`
- Line 22: `import java.io.Writer;`
- Line 23: `import java.net.URI;`
- Line 24: `import java.util.List;`
- Line 25: `import java.util.Map;`
- Line 27: `import static org.elasticsearch.gradle.internal.test.TestUtils.normalizeString;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/StableApiJarMocks.java

### Unused Code (8)
- Line 12: `import net.bytebuddy.ByteBuddy;`
- Line 13: `import net.bytebuddy.dynamic.DynamicType;`
- Line 15: `import org.elasticsearch.plugin.Extensible;`
- Line 16: `import org.elasticsearch.plugin.NamedComponent;`
- Line 17: `import org.elasticsearch.plugin.scanner.test_classes.ExtensibleClass;`
- Line 18: `import org.elasticsearch.plugin.scanner.test_classes.ExtensibleInterface;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.nio.file.Path;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/TestResultExtension.java

### Unused Code (5)
- Line 12: `import org.spockframework.runtime.AbstractRunListener;`
- Line 13: `import org.spockframework.runtime.extension.IGlobalExtension;`
- Line 14: `import org.spockframework.runtime.model.ErrorInfo;`
- Line 15: `import org.spockframework.runtime.model.IterationInfo;`
- Line 16: `import org.spockframework.runtime.model.SpecInfo;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/gradle/internal/test/TestUtils.java

### Null Pointer (1)
- Line 26: `return input.lines()`

### Exception Handling (1)
- Line 36: `throw new RuntimeException(e);`

### Unused Code (3)
- Line 12: `import java.io.File;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.util.stream.Collectors;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/plugin/Extensible.java

### Unused Code (4)
- Line 11: `import java.lang.annotation.Retention;`
- Line 12: `import java.lang.annotation.RetentionPolicy;`
- Line 13: `import java.lang.annotation.Target;`
- Line 15: `import static java.lang.annotation.ElementType.TYPE;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/plugin/NamedComponent.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/plugin/scanner/test_classes/ExtensibleClass.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.Extensible;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/plugin/scanner/test_classes/ExtensibleInterface.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.Extensible;`

## ../build-tools/src/testFixtures/java/org/elasticsearch/plugin/scanner/test_classes/TestNamedComponent.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.NamedComponent;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/BaseInternalPluginBuildPlugin.java

### Unused Code (11)
- Line 12: `import groovy.lang.Closure;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 15: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 16: `import org.elasticsearch.gradle.internal.precommit.JarHellPrecommitPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.test.ClusterFeaturesMetadataPlugin;`
- Line 18: `import org.elasticsearch.gradle.plugin.PluginBuildPlugin;`
- Line 19: `import org.elasticsearch.gradle.plugin.PluginPropertiesExtension;`
- Line 20: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 21: `import org.gradle.api.Plugin;`
- Line 22: `import org.gradle.api.Project;`
- Line 24: `import java.util.Optional;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/BuildPlugin.java

### Concurrency Issue (1)
- Line 36: `public static final String LICENSE_PATH = "licenses/AGPL-3.0+SSPL-1.0+ELASTIC-LICENSE-2.0.txt";`

### Exception Handling (1)
- Line 56: `throw new InvalidUserDataException(`

### Unused Code (16)
- Line 12: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.precommit.InternalPrecommitTasks;`
- Line 14: `import org.elasticsearch.gradle.internal.snyk.SnykDependencyMonitoringGradlePlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.test.ClusterFeaturesMetadataPlugin;`
- Line 16: `import org.gradle.api.InvalidUserDataException;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.file.ProjectLayout;`
- Line 20: `import org.gradle.api.file.RegularFileProperty;`
- Line 21: `import org.gradle.api.model.ObjectFactory;`
- Line 22: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 23: `import org.gradle.api.provider.ProviderFactory;`
- Line 24: `import org.gradle.api.tasks.bundling.Jar;`
- Line 25: `import org.gradle.initialization.layout.BuildLayout;`
- Line 27: `import java.io.File;`
- Line 29: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/BwcGitExtension.java

### Concurrency Issue (2)
- Line 36: `public void setBwcVersion(Provider<Version> bwcVersion) {`
- Line 44: `public void setBwcBranch(Provider<String> bwcBranch) {`

### Unused Code (6)
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.gradle.api.model.ObjectFactory;`
- Line 14: `import org.gradle.api.provider.Property;`
- Line 15: `import org.gradle.api.provider.Provider;`
- Line 17: `import java.io.File;`
- Line 19: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/BwcSetupExtension.java

### Concurrency Issue (2)
- Line 43: `private static final String MINIMUM_COMPILER_VERSION_PATH = "src/main/resources/minimumCompilerVersion";`
- Line 44: `private static final Version BUILD_TOOL_MINIMUM_VERSION = Version.fromString("7.14.0");`

### Exception Handling (1)
- Line 198: `throw new GradleException("Cannot read java properties file.", ioException);`

### Unused Code (23)
- Line 12: `import org.apache.commons.io.FileUtils;`
- Line 13: `import org.elasticsearch.gradle.LoggedExec;`
- Line 14: `import org.elasticsearch.gradle.OS;`
- Line 15: `import org.elasticsearch.gradle.Version;`
- Line 16: `import org.gradle.api.Action;`
- Line 17: `import org.gradle.api.GradleException;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.Task;`
- Line 20: `import org.gradle.api.logging.LogLevel;`
- Line 21: `import org.gradle.api.model.ObjectFactory;`
- Line 22: `import org.gradle.api.provider.Property;`
- Line 23: `import org.gradle.api.provider.Provider;`
- Line 24: `import org.gradle.api.provider.ProviderFactory;`
- Line 25: `import org.gradle.api.provider.ValueSource;`
- Line 26: `import org.gradle.api.provider.ValueSourceParameters;`
- Line 27: `import org.gradle.api.tasks.TaskProvider;`
- Line 28: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 29: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 31: `import java.io.File;`
- Line 32: `import java.io.IOException;`
- Line 33: `import java.util.Arrays;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.Locale;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/BwcVersions.java

### Null Pointer (3)
- Line 99: `return versionLines.stream()`
- Line 252: `return versions.stream()`
- Line 314: `return versions.stream()`

### Concurrency Issue (1)
- Line 71: `private static final String GLIBC_VERSION_ENV_VAR = "GLIBC_VERSION";`

### Exception Handling (4)
- Line 83: `throw new IllegalArgumentException("Could not parse any versions");`
- Line 109: `throw new IllegalStateException(`
- Line 231: `throw new IllegalStateException(`
- Line 267: `throw new IllegalStateException("No read-only compatible version found.");`

### Unused Code (20)
- Line 11: `import org.elasticsearch.gradle.Version;`
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 14: `import java.io.Serializable;`
- Line 15: `import java.util.ArrayList;`
- Line 16: `import java.util.Collections;`
- Line 17: `import java.util.Comparator;`
- Line 18: `import java.util.HashSet;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Optional;`
- Line 22: `import java.util.Set;`
- Line 23: `import java.util.TreeMap;`
- Line 24: `import java.util.function.BiConsumer;`
- Line 25: `import java.util.function.Consumer;`
- Line 26: `import java.util.function.Predicate;`
- Line 27: `import java.util.regex.Matcher;`
- Line 28: `import java.util.regex.Pattern;`
- Line 30: `import static java.util.Collections.reverseOrder;`
- Line 31: `import static java.util.Collections.unmodifiableList;`
- Line 32: `import static java.util.Comparator.comparing;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ConcatFilesTask.java

### Concurrency Issue (4)
- Line 47: `public void setFiles(FileCollection files) {`
- Line 56: `public void setHeaderLine(String headerLine) {`
- Line 66: `public void setTarget(File target) {`
- Line 80: `public void setAdditionalLines(List<String> additionalLines) {`

### Unused Code (18)
- Line 38: `private FileCollection files;`
- Line 41: `private String headerLine;`
- Line 43: `private File target;`
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.file.FileCollection;`
- Line 13: `import org.gradle.api.tasks.Input;`
- Line 14: `import org.gradle.api.tasks.InputFiles;`
- Line 15: `import org.gradle.api.tasks.Optional;`
- Line 16: `import org.gradle.api.tasks.OutputFile;`
- Line 17: `import org.gradle.api.tasks.TaskAction;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.nio.charset.StandardCharsets;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.StandardOpenOption;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.LinkedHashSet;`
- Line 26: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/DependenciesInfoPlugin.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.gradle.dependencies.CompileOnlyResolvePlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.precommit.DependencyLicensesTask;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.artifacts.Configuration;`
- Line 17: `import org.gradle.api.attributes.Category;`
- Line 18: `import org.gradle.api.plugins.JavaPlugin;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/DependenciesInfoTask.java

### Concurrency Issue (4)
- Line 67: `public void setRuntimeConfiguration(Configuration runtimeConfiguration) {`
- Line 75: `public void setCompileOnlyConfiguration(Configuration compileOnlyConfiguration) {`
- Line 101: `public void setOutputFile(File outputFile) {`
- Line 166: `public void setMappings(LinkedHashMap<String, String> mappings) {`

### Unused Code (31)
- Line 59: `private File outputFile;`
- Line 109: `private Configuration runtimeConfiguration;`
- Line 114: `private Configuration compileOnlyConfiguration;`
- Line 12: `import org.elasticsearch.gradle.internal.precommit.DependencyLicensesTask;`
- Line 13: `import org.elasticsearch.gradle.internal.precommit.LicenseAnalyzer;`
- Line 14: `import org.gradle.api.artifacts.Configuration;`
- Line 15: `import org.gradle.api.artifacts.Dependency;`
- Line 16: `import org.gradle.api.artifacts.DependencySet;`
- Line 17: `import org.gradle.api.artifacts.ModuleVersionIdentifier;`
- Line 18: `import org.gradle.api.artifacts.ProjectDependency;`
- Line 19: `import org.gradle.api.file.DirectoryProperty;`
- Line 20: `import org.gradle.api.file.ProjectLayout;`
- Line 21: `import org.gradle.api.internal.ConventionTask;`
- Line 22: `import org.gradle.api.model.ObjectFactory;`
- Line 23: `import org.gradle.api.provider.ProviderFactory;`
- Line 24: `import org.gradle.api.tasks.Input;`
- Line 25: `import org.gradle.api.tasks.InputDirectory;`
- Line 26: `import org.gradle.api.tasks.InputFiles;`
- Line 27: `import org.gradle.api.tasks.Optional;`
- Line 28: `import org.gradle.api.tasks.OutputFile;`
- Line 29: `import org.gradle.api.tasks.TaskAction;`
- Line 31: `import java.io.File;`
- Line 32: `import java.io.IOException;`
- Line 33: `import java.nio.file.Files;`
- Line 34: `import java.nio.file.StandardOpenOption;`
- Line 35: `import java.util.Arrays;`
- Line 36: `import java.util.LinkedHashMap;`
- Line 37: `import java.util.Set;`
- Line 38: `import java.util.regex.Pattern;`
- Line 39: `import java.util.stream.Collectors;`
- Line 41: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/DistributionArchive.java

### Unused Code (6)
- Line 12: `import org.gradle.api.Named;`
- Line 13: `import org.gradle.api.file.CopySpec;`
- Line 14: `import org.gradle.api.tasks.Sync;`
- Line 15: `import org.gradle.api.tasks.TaskProvider;`
- Line 16: `import org.gradle.api.tasks.bundling.AbstractArchiveTask;`
- Line 18: `import java.util.function.Supplier;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/DistributionArchiveCheckExtension.java

### Unused Code (2)
- Line 12: `import org.gradle.api.model.ObjectFactory;`
- Line 13: `import org.gradle.api.provider.ListProperty;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchBuildCompletePlugin.java

### Exception Handling (2)
- Line 254: `throw new IOException("Support only file!: " + path);`
- Line 273: `throw new RuntimeException(e);`

### Unused Code (34)
- Line 12: `import com.gradle.develocity.agent.gradle.DevelocityConfiguration;`
- Line 14: `import org.apache.commons.compress.archivers.tar.TarArchiveEntry;`
- Line 15: `import org.apache.commons.compress.archivers.tar.TarArchiveOutputStream;`
- Line 16: `import org.apache.commons.compress.compressors.bzip2.BZip2CompressorOutputStream;`
- Line 17: `import org.apache.commons.io.IOUtils;`
- Line 18: `import org.elasticsearch.gradle.OS;`
- Line 19: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 20: `import org.gradle.api.Plugin;`
- Line 21: `import org.gradle.api.Project;`
- Line 22: `import org.gradle.api.file.FileSystemOperations;`
- Line 23: `import org.gradle.api.flow.FlowAction;`
- Line 24: `import org.gradle.api.flow.FlowParameters;`
- Line 25: `import org.gradle.api.flow.FlowProviders;`
- Line 26: `import org.gradle.api.flow.FlowScope;`
- Line 27: `import org.gradle.api.internal.file.FileOperations;`
- Line 28: `import org.gradle.api.provider.ListProperty;`
- Line 29: `import org.gradle.api.provider.Property;`
- Line 30: `import org.gradle.api.tasks.Input;`
- Line 31: `import org.jetbrains.annotations.NotNull;`
- Line 32: `import org.slf4j.Logger;`
- Line 33: `import org.slf4j.LoggerFactory;`
- Line 35: `import java.io.BufferedInputStream;`
- Line 36: `import java.io.BufferedOutputStream;`
- Line 37: `import java.io.File;`
- Line 38: `import java.io.FileNotFoundException;`
- Line 39: `import java.io.IOException;`
- Line 40: `import java.io.OutputStream;`
- Line 41: `import java.nio.file.Files;`
- Line 42: `import java.nio.file.Path;`
- Line 43: `import java.util.ArrayList;`
- Line 44: `import java.util.Arrays;`
- Line 45: `import java.util.List;`
- Line 46: `import java.util.Optional;`
- Line 48: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchJavaBasePlugin.java

### Unused Code (31)
- Line 52: `private BuildParameterExtension buildParams;`
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTaskPlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 15: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 16: `import org.elasticsearch.gradle.internal.test.MutedTestPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.test.TestUtil;`
- Line 18: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 19: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 20: `import org.gradle.api.JavaVersion;`
- Line 21: `import org.gradle.api.Plugin;`
- Line 22: `import org.gradle.api.Project;`
- Line 23: `import org.gradle.api.artifacts.Configuration;`
- Line 24: `import org.gradle.api.artifacts.ResolutionStrategy;`
- Line 25: `import org.gradle.api.file.FileCollection;`
- Line 26: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 27: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 28: `import org.gradle.api.provider.Provider;`
- Line 29: `import org.gradle.api.tasks.SourceSet;`
- Line 30: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 31: `import org.gradle.api.tasks.compile.AbstractCompile;`
- Line 32: `import org.gradle.api.tasks.compile.CompileOptions;`
- Line 33: `import org.gradle.api.tasks.compile.GroovyCompile;`
- Line 34: `import org.gradle.api.tasks.compile.JavaCompile;`
- Line 35: `import org.gradle.api.tasks.testing.Test;`
- Line 36: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 37: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 39: `import java.util.List;`
- Line 40: `import java.util.Map;`
- Line 41: `import java.util.function.Supplier;`
- Line 43: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchJavaModulePathPlugin.java

### Null Pointer (1)
- Line 126: `return result.getDependencies()`

### Unused Code (30)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Action;`
- Line 15: `import org.gradle.api.Named;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.Task;`
- Line 19: `import org.gradle.api.artifacts.component.ComponentIdentifier;`
- Line 20: `import org.gradle.api.artifacts.component.ProjectComponentIdentifier;`
- Line 21: `import org.gradle.api.artifacts.result.ResolvedComponentResult;`
- Line 22: `import org.gradle.api.artifacts.result.ResolvedDependencyResult;`
- Line 23: `import org.gradle.api.attributes.LibraryElements;`
- Line 24: `import org.gradle.api.file.FileCollection;`
- Line 25: `import org.gradle.api.logging.Logger;`
- Line 26: `import org.gradle.api.plugins.JavaPlugin;`
- Line 27: `import org.gradle.api.tasks.CompileClasspath;`
- Line 28: `import org.gradle.api.tasks.Internal;`
- Line 29: `import org.gradle.api.tasks.SourceSet;`
- Line 30: `import org.gradle.api.tasks.compile.JavaCompile;`
- Line 31: `import org.gradle.process.CommandLineArgumentProvider;`
- Line 33: `import java.io.File;`
- Line 34: `import java.nio.file.Files;`
- Line 35: `import java.util.ArrayList;`
- Line 36: `import java.util.Arrays;`
- Line 37: `import java.util.HashSet;`
- Line 38: `import java.util.List;`
- Line 39: `import java.util.Set;`
- Line 40: `import java.util.stream.Collectors;`
- Line 41: `import java.util.stream.Stream;`
- Line 42: `import java.util.stream.StreamSupport;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchJavaPlugin.java

### Unused Code (29)
- Line 12: `import nebula.plugin.info.InfoBrokerPlugin;`
- Line 14: `import com.github.jengelman.gradle.plugins.shadow.tasks.ShadowJar;`
- Line 16: `import org.elasticsearch.gradle.VersionProperties;`
- Line 17: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 18: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 19: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 20: `import org.gradle.api.Action;`
- Line 21: `import org.gradle.api.JavaVersion;`
- Line 22: `import org.gradle.api.Plugin;`
- Line 23: `import org.gradle.api.Project;`
- Line 24: `import org.gradle.api.Task;`
- Line 25: `import org.gradle.api.artifacts.Configuration;`
- Line 26: `import org.gradle.api.plugins.BasePlugin;`
- Line 27: `import org.gradle.api.plugins.JavaLibraryPlugin;`
- Line 28: `import org.gradle.api.plugins.JavaPlugin;`
- Line 29: `import org.gradle.api.provider.Property;`
- Line 30: `import org.gradle.api.provider.Provider;`
- Line 31: `import org.gradle.api.tasks.TaskProvider;`
- Line 32: `import org.gradle.api.tasks.bundling.Jar;`
- Line 33: `import org.gradle.api.tasks.javadoc.Javadoc;`
- Line 34: `import org.gradle.external.javadoc.CoreJavadocOptions;`
- Line 35: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 36: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 37: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`
- Line 39: `import java.io.File;`
- Line 40: `import java.util.Map;`
- Line 42: `import javax.inject.Inject;`
- Line 44: `import static org.elasticsearch.gradle.internal.conventions.util.Util.toStringable;`
- Line 45: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchJavadocPlugin.java

### Unused Code (16)
- Line 12: `import com.github.jengelman.gradle.plugins.shadow.ShadowPlugin;`
- Line 14: `import org.gradle.api.Action;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.Task;`
- Line 18: `import org.gradle.api.artifacts.Configuration;`
- Line 19: `import org.gradle.api.artifacts.Dependency;`
- Line 20: `import org.gradle.api.artifacts.ProjectDependency;`
- Line 21: `import org.gradle.api.plugins.BasePluginExtension;`
- Line 22: `import org.gradle.api.plugins.JavaPlugin;`
- Line 23: `import org.gradle.api.tasks.javadoc.Javadoc;`
- Line 24: `import org.gradle.external.javadoc.JavadocOfflineLink;`
- Line 25: `import org.gradle.external.javadoc.StandardJavadocDocletOptions;`
- Line 27: `import java.io.File;`
- Line 28: `import java.util.Comparator;`
- Line 29: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ElasticsearchTestBasePlugin.java

### Unused Code (27)
- Line 12: `import com.github.jengelman.gradle.plugins.shadow.ShadowBasePlugin;`
- Line 14: `import org.elasticsearch.gradle.OS;`
- Line 15: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 16: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.test.ErrorReportingTestListener;`
- Line 18: `import org.elasticsearch.gradle.internal.test.SimpleCommandLineArgumentProvider;`
- Line 19: `import org.elasticsearch.gradle.test.GradleTestPolicySetupPlugin;`
- Line 20: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 21: `import org.gradle.api.Action;`
- Line 22: `import org.gradle.api.JavaVersion;`
- Line 23: `import org.gradle.api.Plugin;`
- Line 24: `import org.gradle.api.Project;`
- Line 25: `import org.gradle.api.Task;`
- Line 26: `import org.gradle.api.artifacts.Configuration;`
- Line 27: `import org.gradle.api.file.FileCollection;`
- Line 28: `import org.gradle.api.plugins.JavaPlugin;`
- Line 29: `import org.gradle.api.provider.ProviderFactory;`
- Line 30: `import org.gradle.api.tasks.SourceSet;`
- Line 31: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 32: `import org.gradle.api.tasks.testing.Test;`
- Line 34: `import java.io.File;`
- Line 35: `import java.util.List;`
- Line 36: `import java.util.Map;`
- Line 38: `import javax.inject.Inject;`
- Line 40: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`
- Line 41: `import static org.elasticsearch.gradle.util.FileUtils.mkdirs;`
- Line 42: `import static org.elasticsearch.gradle.util.GradleUtils.maybeConfigure;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/EmbeddedProviderExtension.java

### Unused Code (12)
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.api.Task;`
- Line 14: `import org.gradle.api.artifacts.Configuration;`
- Line 15: `import org.gradle.api.file.Directory;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.Sync;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import static org.elasticsearch.gradle.internal.conventions.GUtils.capitalize;`
- Line 22: `import static org.elasticsearch.gradle.util.GradleUtils.getJavaSourceSets;`
- Line 23: `import static org.gradle.api.artifacts.type.ArtifactTypeDefinition.ARTIFACT_TYPE_ATTRIBUTE;`
- Line 24: `import static org.gradle.api.artifacts.type.ArtifactTypeDefinition.DIRECTORY_TYPE;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/EmbeddedProviderPlugin.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.attributes.Attribute;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import static org.gradle.api.artifacts.type.ArtifactTypeDefinition.ARTIFACT_TYPE_ATTRIBUTE;`
- Line 20: `import static org.gradle.api.artifacts.type.ArtifactTypeDefinition.DIRECTORY_TYPE;`
- Line 21: `import static org.gradle.api.artifacts.type.ArtifactTypeDefinition.JAR_TYPE;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/EmptyDirTask.java

### Concurrency Issue (2)
- Line 56: `public void setDir(File dir) {`
- Line 68: `public void setDirMode(int dirMode) {`

### Exception Handling (1)
- Line 40: `throw new UnsupportedOperationException();`

### Unused Code (9)
- Line 26: `private File dir;`
- Line 27: `private int dirMode = 0755;`
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.tasks.Input;`
- Line 13: `import org.gradle.api.tasks.OutputDirectory;`
- Line 14: `import org.gradle.api.tasks.TaskAction;`
- Line 15: `import org.gradle.internal.file.Chmod;`
- Line 17: `import java.io.File;`
- Line 19: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ExportElasticsearchBuildResourcesTask.java

### Concurrency Issue (1)
- Line 44: `private static final Logger logger = Logging.getLogger(ExportElasticsearchBuildResourcesTask.class);`

### Exception Handling (4)
- Line 78: `throw new GradleException(`
- Line 89: `throw new StopExecutionException();`
- Line 96: `throw new GradleException("Can't export `" + resourcePath + "` from build-tools: not found");`
- Line 100: `throw new GradleException("Can't write resource `" + resourcePath + "` to " + destination, e);`

### Unused Code (22)
- Line 48: `private DirectoryProperty outputDir;`
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.file.DirectoryProperty;`
- Line 14: `import org.gradle.api.logging.Logger;`
- Line 15: `import org.gradle.api.logging.Logging;`
- Line 16: `import org.gradle.api.model.ObjectFactory;`
- Line 17: `import org.gradle.api.tasks.Classpath;`
- Line 18: `import org.gradle.api.tasks.Input;`
- Line 19: `import org.gradle.api.tasks.OutputDirectory;`
- Line 20: `import org.gradle.api.tasks.StopExecutionException;`
- Line 21: `import org.gradle.api.tasks.TaskAction;`
- Line 23: `import java.io.File;`
- Line 24: `import java.io.IOException;`
- Line 25: `import java.io.InputStream;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.nio.file.StandardCopyOption;`
- Line 29: `import java.util.Collections;`
- Line 30: `import java.util.HashSet;`
- Line 31: `import java.util.Set;`
- Line 33: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/FixtureStop.java

### Unused Code (1)
- Line 12: `import org.gradle.api.Task;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/GenerateProviderManifest.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.util.FileUtils;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.RegularFileProperty;`
- Line 16: `import org.gradle.api.tasks.Classpath;`
- Line 17: `import org.gradle.api.tasks.InputFiles;`
- Line 18: `import org.gradle.api.tasks.OutputFile;`
- Line 19: `import org.gradle.api.tasks.TaskAction;`
- Line 21: `import java.io.File;`
- Line 22: `import java.util.stream.Collectors;`
- Line 24: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalAvailableTcpPortProviderPlugin.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.gradle.internal.util.ports.AvailablePortAllocator;`
- Line 13: `import org.elasticsearch.gradle.internal.util.ports.ReservedPortRange;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalBwcGitPlugin.java

### Concurrency Issue (1)
- Line 66: `public void apply(Project project) {`

### Exception Handling (3)
- Line 113: `throw new GradleException("tests.bwc.git_fetch_latest must be [true] or [false] but was [" + fetchProp + "]");`
- Line 201: `throw new IllegalStateException("Found the following merge commits which prevent determining bwc commits: " + mergeCommits);`
- Line 213: `throw new UncheckedIOException(e);`

### Unused Code (28)
- Line 50: `private BwcGitExtension gitExtension;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.info.GitInfo;`
- Line 14: `import org.gradle.api.Action;`
- Line 15: `import org.gradle.api.GradleException;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.Task;`
- Line 19: `import org.gradle.api.file.ProjectLayout;`
- Line 20: `import org.gradle.api.logging.Logger;`
- Line 21: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 22: `import org.gradle.api.provider.Provider;`
- Line 23: `import org.gradle.api.provider.ProviderFactory;`
- Line 24: `import org.gradle.api.tasks.TaskContainer;`
- Line 25: `import org.gradle.api.tasks.TaskProvider;`
- Line 26: `import org.gradle.initialization.layout.BuildLayout;`
- Line 27: `import org.gradle.process.ExecOperations;`
- Line 28: `import org.gradle.process.ExecResult;`
- Line 29: `import org.gradle.process.ExecSpec;`
- Line 31: `import java.io.ByteArrayOutputStream;`
- Line 32: `import java.io.File;`
- Line 33: `import java.io.IOException;`
- Line 34: `import java.io.UncheckedIOException;`
- Line 35: `import java.nio.file.Files;`
- Line 37: `import javax.inject.Inject;`
- Line 39: `import static java.nio.file.StandardOpenOption.CREATE;`
- Line 40: `import static java.nio.file.StandardOpenOption.TRUNCATE_EXISTING;`
- Line 41: `import static java.util.Arrays.asList;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionArchiveCheckPlugin.java

### Exception Handling (2)
- Line 96: `throw new GradleException("Expecting project name containing 'zip' or 'tar'.");`
- Line 207: `throw new GradleException("Unable to read from file " + path, ioException);`

### Unused Code (25)
- Line 41: `private ArchiveOperations archiveOperations;`
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.GUtils;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.LicensingPlugin;`
- Line 15: `import org.gradle.api.Action;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.Task;`
- Line 20: `import org.gradle.api.file.ArchiveOperations;`
- Line 21: `import org.gradle.api.plugins.BasePlugin;`
- Line 22: `import org.gradle.api.provider.ListProperty;`
- Line 23: `import org.gradle.api.provider.Provider;`
- Line 24: `import org.gradle.api.tasks.Copy;`
- Line 25: `import org.gradle.api.tasks.TaskProvider;`
- Line 27: `import java.io.File;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.nio.file.Files;`
- Line 30: `import java.nio.file.Path;`
- Line 31: `import java.util.Arrays;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.Map;`
- Line 34: `import java.util.concurrent.Callable;`
- Line 35: `import java.util.stream.Collectors;`
- Line 37: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionArchiveSetupPlugin.java

### Concurrency Issue (3)
- Line 45: `public static final String DEFAULT_CONFIGURATION_NAME = "default";`
- Line 46: `public static final String EXTRACTED_CONFIGURATION_NAME = "extracted";`
- Line 47: `public static final String COMPOSITE_CONFIGURATION_NAME = "composite";`

### Unused Code (14)
- Line 12: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 16: `import org.gradle.api.attributes.Attribute;`
- Line 17: `import org.gradle.api.plugins.BasePlugin;`
- Line 18: `import org.gradle.api.tasks.AbstractCopyTask;`
- Line 19: `import org.gradle.api.tasks.Sync;`
- Line 20: `import org.gradle.api.tasks.TaskContainer;`
- Line 21: `import org.gradle.api.tasks.bundling.AbstractArchiveTask;`
- Line 22: `import org.gradle.api.tasks.bundling.Compression;`
- Line 23: `import org.gradle.api.tasks.bundling.Zip;`
- Line 25: `import java.io.File;`
- Line 27: `import static org.elasticsearch.gradle.internal.conventions.GUtils.capitalize;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionBwcSetupPlugin.java

### Unused Code (32)
- Line 55: `private ProviderFactory providerFactory;`
- Line 56: `private JavaToolchainService toolChainService;`
- Line 57: `private FileSystemOperations fileSystemOperations;`
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 14: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 15: `import org.gradle.api.Action;`
- Line 16: `import org.gradle.api.InvalidUserDataException;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.Task;`
- Line 20: `import org.gradle.api.file.FileSystemOperations;`
- Line 21: `import org.gradle.api.file.ProjectLayout;`
- Line 22: `import org.gradle.api.model.ObjectFactory;`
- Line 23: `import org.gradle.api.plugins.JvmToolchainsPlugin;`
- Line 24: `import org.gradle.api.provider.Provider;`
- Line 25: `import org.gradle.api.provider.ProviderFactory;`
- Line 26: `import org.gradle.api.tasks.PathSensitivity;`
- Line 27: `import org.gradle.api.tasks.TaskProvider;`
- Line 28: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 29: `import org.gradle.language.base.plugins.LifecycleBasePlugin;`
- Line 31: `import java.io.File;`
- Line 32: `import java.nio.file.Path;`
- Line 33: `import java.util.ArrayList;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.Locale;`
- Line 36: `import java.util.Set;`
- Line 37: `import java.util.stream.Collectors;`
- Line 39: `import javax.inject.Inject;`
- Line 41: `import static java.util.Arrays.asList;`
- Line 42: `import static java.util.Arrays.stream;`
- Line 43: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionDownloadPlugin.java

### Unused Code (24)
- Line 12: `import org.elasticsearch.gradle.Architecture;`
- Line 13: `import org.elasticsearch.gradle.DistributionDependency;`
- Line 14: `import org.elasticsearch.gradle.DistributionDownloadPlugin;`
- Line 15: `import org.elasticsearch.gradle.DistributionResolution;`
- Line 16: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 17: `import org.elasticsearch.gradle.Version;`
- Line 18: `import org.elasticsearch.gradle.VersionProperties;`
- Line 19: `import org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes;`
- Line 20: `import org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes;`
- Line 21: `import org.elasticsearch.gradle.internal.docker.DockerSupportPlugin;`
- Line 22: `import org.elasticsearch.gradle.internal.docker.DockerSupportService;`
- Line 23: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 24: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 25: `import org.gradle.api.GradleException;`
- Line 26: `import org.gradle.api.Plugin;`
- Line 27: `import org.gradle.api.Project;`
- Line 28: `import org.gradle.api.artifacts.Dependency;`
- Line 29: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 30: `import org.gradle.api.provider.Provider;`
- Line 32: `import java.util.HashMap;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Map;`
- Line 35: `import java.util.function.Function;`
- Line 37: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalDistributionModuleCheckTaskProvider.java

### Concurrency Issue (2)
- Line 42: `private static final Logger LOGGER = Logging.getLogger(InternalDistributionModuleCheckTaskProvider.class);`
- Line 44: `private static final String MODULE_INFO = "module-info.class";`

### Exception Handling (3)
- Line 99: `throw new UncheckedIOException(e);`
- Line 113: `throw new GradleException(MODULE_INFO + " no found in " + path);`
- Line 116: `throw new GradleException("Failed when reading jar file " + path, e);`

### Unused Code (21)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.Task;`
- Line 17: `import org.gradle.api.logging.Logger;`
- Line 18: `import org.gradle.api.logging.Logging;`
- Line 19: `import org.gradle.api.tasks.Copy;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.io.UncheckedIOException;`
- Line 24: `import java.lang.module.ModuleFinder;`
- Line 25: `import java.lang.module.ModuleReference;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.function.Function;`
- Line 30: `import java.util.function.Predicate;`
- Line 31: `import java.util.jar.JarEntry;`
- Line 32: `import java.util.jar.JarFile;`
- Line 34: `import static java.util.stream.Collectors.joining;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalPluginBuildPlugin.java

### Unused Code (2)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalReaperPlugin.java

### Unused Code (5)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.file.ProjectLayout;`
- Line 16: `import javax.inject.Inject;`
- Line 18: `import static org.elasticsearch.gradle.ReaperPlugin.registerReaperService;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalTestArtifactBasePlugin.java

### Unused Code (4)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.provider.ProviderFactory;`
- Line 16: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalTestArtifactExtension.java

### Unused Code (10)
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.api.artifacts.Configuration;`
- Line 14: `import org.gradle.api.artifacts.Dependency;`
- Line 15: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 16: `import org.gradle.api.plugins.BasePluginExtension;`
- Line 17: `import org.gradle.api.plugins.JavaPlugin;`
- Line 18: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 19: `import org.gradle.api.provider.ProviderFactory;`
- Line 20: `import org.gradle.api.tasks.SourceSet;`
- Line 21: `import org.gradle.jvm.tasks.Jar;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalTestArtifactPlugin.java

### Unused Code (4)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.tasks.SourceSet;`
- Line 15: `import org.gradle.api.tasks.SourceSetContainer;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/InternalTestClustersPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 14: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 15: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 16: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 20: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/JarApiComparisonTask.java

### Resource Leak (1)
- Line 157: `try (BufferedReader br = new BufferedReader(new InputStreamReader(streamToRead))) {`

### Null Pointer (2)
- Line 114: `return jf.stream()`
- Line 176: `return javapOutput.stream()`

### Exception Handling (6)
- Line 72: `throw new IllegalStateException("Expected a single original jar, but found: " + oldJarNames);`
- Line 85: `throw new RuntimeException(e);`
- Line 152: `throw new RuntimeException(e);`
- Line 160: `throw new RuntimeException(e);`
- Line 212: `throw new IllegalStateException("Classes from a previous version not found: " + deletedClasses);`
- Line 224: `throw new IllegalStateException(`

### Unused Code (22)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTask;`
- Line 13: `import org.gradle.api.file.FileCollection;`
- Line 14: `import org.gradle.api.provider.Property;`
- Line 15: `import org.gradle.api.tasks.CacheableTask;`
- Line 16: `import org.gradle.api.tasks.CompileClasspath;`
- Line 17: `import org.gradle.api.tasks.TaskAction;`
- Line 18: `import org.gradle.internal.jvm.Jvm;`
- Line 20: `import java.io.BufferedReader;`
- Line 21: `import java.io.File;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.io.InputStream;`
- Line 24: `import java.io.InputStreamReader;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.HashSet;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Set;`
- Line 31: `import java.util.jar.JarFile;`
- Line 32: `import java.util.regex.Pattern;`
- Line 33: `import java.util.stream.Collectors;`
- Line 34: `import java.util.zip.ZipEntry;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/JavaClassPublicifier.java

### Concurrency Issue (1)
- Line 56: `public void setClassFiles(List<String> classFiles) {`

### Unused Code (22)
- Line 42: `private DirectoryProperty inputDir;`
- Line 43: `private DirectoryProperty outputDir;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.file.DirectoryProperty;`
- Line 14: `import org.gradle.api.model.ObjectFactory;`
- Line 15: `import org.gradle.api.tasks.Input;`
- Line 16: `import org.gradle.api.tasks.InputDirectory;`
- Line 17: `import org.gradle.api.tasks.OutputDirectory;`
- Line 18: `import org.gradle.api.tasks.TaskAction;`
- Line 19: `import org.objectweb.asm.ClassReader;`
- Line 20: `import org.objectweb.asm.ClassWriter;`
- Line 21: `import org.objectweb.asm.tree.ClassNode;`
- Line 22: `import org.objectweb.asm.tree.InnerClassNode;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.InputStream;`
- Line 27: `import java.nio.file.Files;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.function.Consumer;`
- Line 31: `import javax.inject.Inject;`
- Line 33: `import static org.objectweb.asm.Opcodes.ACC_PRIVATE;`
- Line 34: `import static org.objectweb.asm.Opcodes.ACC_PUBLIC;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/Jdk.java

### Concurrency Issue (2)
- Line 31: `private static final Pattern VERSION_PATTERN = Pattern.compile(`
- Line 34: `private static final Pattern LEGACY_VERSION_PATTERN = Pattern.compile("(\\d)(u\\d+)\\+(b\\d+?)(@([a-f0-9]{32}))?");`

### Exception Handling (10)
- Line 71: `throw new IllegalArgumentException("unknown vendor [" + vendor + "] for jdk [" + name + "], must be one of " + ALLOWED_VENDORS);`
- Line 82: `throw new IllegalArgumentException("malformed version [" + version + "] for jdk [" + name + "]");`
- Line 94: `throw new IllegalArgumentException(`
- Line 107: `throw new IllegalArgumentException(`
- Line 163: `throw new RuntimeException(e);`
- Line 191: `throw new IllegalArgumentException("version not specified for jdk [" + name + "]");`
- Line 194: `throw new IllegalArgumentException("platform not specified for jdk [" + name + "]");`
- Line 197: `throw new IllegalArgumentException("vendor not specified for jdk [" + name + "]");`
- Line 200: `throw new IllegalArgumentException("architecture not specified for jdk [" + name + "]");`
- Line 223: `throw new IllegalArgumentException("Malformed jdk version [" + version + "]");`

### Unused Code (16)
- Line 45: `private String baseVersion;`
- Line 46: `private String major;`
- Line 47: `private String build;`
- Line 48: `private String hash;`
- Line 12: `import org.gradle.api.Buildable;`
- Line 13: `import org.gradle.api.artifacts.Configuration;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.model.ObjectFactory;`
- Line 16: `import org.gradle.api.provider.Property;`
- Line 17: `import org.gradle.api.tasks.TaskDependency;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.util.Iterator;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.regex.Matcher;`
- Line 24: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/JdkDownloadPlugin.java

### Concurrency Issue (6)
- Line 33: `public static final String VENDOR_ADOPTIUM = "adoptium";`
- Line 34: `public static final String VENDOR_OPENJDK = "openjdk";`
- Line 35: `public static final String VENDOR_ZULU = "zulu";`
- Line 37: `private static final String REPO_NAME_PREFIX = "jdk_repo_";`
- Line 38: `private static final String EXTENSION_NAME = "jdks";`
- Line 39: `public static final String JDK_TRIMMED_PREFIX = "(jdk-?\\d.*)|(zulu-?\\d.*).jdk";`

### Exception Handling (1)
- Line 145: `throw new GradleException("JDK vendor zulu is supported only for JDK8 on MacOS with Apple Silicon.");`

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.transform.SymbolicLinkPreservingUntarTransform;`
- Line 13: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.artifacts.Configuration;`
- Line 19: `import org.gradle.api.artifacts.dsl.RepositoryHandler;`
- Line 20: `import org.gradle.api.artifacts.repositories.IvyArtifactRepository;`
- Line 21: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 22: `import org.gradle.api.attributes.Attribute;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/LoggingOutputStream.java

### Unused Code (5)
- Line 30: `private int start = 0;`
- Line 33: `private int end = 0;`
- Line 12: `import java.io.IOException;`
- Line 13: `import java.io.OutputStream;`
- Line 14: `import java.util.Arrays;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/MrjarPlugin.java

### Concurrency Issue (2)
- Line 57: `private static final Pattern MRJAR_SOURCESET_PATTERN = Pattern.compile("main(\\d{2})");`
- Line 58: `private static final String MRJAR_IDEA_ENABLED = "org.gradle.mrjar.idea.enabled";`

### Exception Handling (4)
- Line 243: `throw new IllegalArgumentException(`
- Line 257: `throw new UncheckedIOException(e);`
- Line 268: `throw new UncheckedIOException(e);`
- Line 285: `throw new UncheckedIOException(e);`

### Unused Code (39)
- Line 12: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 13: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.precommit.CheckForbiddenApisTask;`
- Line 15: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 16: `import org.gradle.api.JavaVersion;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.file.FileCollection;`
- Line 20: `import org.gradle.api.plugins.JavaPlugin;`
- Line 21: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 22: `import org.gradle.api.tasks.SourceSet;`
- Line 23: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 24: `import org.gradle.api.tasks.TaskProvider;`
- Line 25: `import org.gradle.api.tasks.compile.CompileOptions;`
- Line 26: `import org.gradle.api.tasks.compile.JavaCompile;`
- Line 27: `import org.gradle.api.tasks.javadoc.Javadoc;`
- Line 28: `import org.gradle.api.tasks.testing.Test;`
- Line 29: `import org.gradle.external.javadoc.CoreJavadocOptions;`
- Line 30: `import org.gradle.jvm.tasks.Jar;`
- Line 31: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 32: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 33: `import org.objectweb.asm.ClassReader;`
- Line 34: `import org.objectweb.asm.ClassWriter;`
- Line 35: `import org.objectweb.asm.tree.ClassNode;`
- Line 37: `import java.io.IOException;`
- Line 38: `import java.io.UncheckedIOException;`
- Line 39: `import java.nio.file.Files;`
- Line 40: `import java.nio.file.Path;`
- Line 41: `import java.util.ArrayList;`
- Line 42: `import java.util.Collections;`
- Line 43: `import java.util.List;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.regex.Matcher;`
- Line 46: `import java.util.regex.Pattern;`
- Line 47: `import java.util.stream.Stream;`
- Line 49: `import javax.inject.Inject;`
- Line 51: `import static de.thetaphi.forbiddenapis.gradle.ForbiddenApisPlugin.FORBIDDEN_APIS_TASK_NAME;`
- Line 52: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`
- Line 53: `import static org.objectweb.asm.Opcodes.V_PREVIEW;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/NoticeTask.java

### Concurrency Issue (2)
- Line 217: `public void setInputFile(File inputFile) {`
- Line 225: `public void setOutputFile(File outputFile) {`

### Exception Handling (1)
- Line 116: `throw new RuntimeException(`

### Unused Code (30)
- Line 51: `private File inputFile;`
- Line 54: `private File outputFile;`
- Line 56: `private FileTree sources;`
- Line 12: `import org.codehaus.groovy.runtime.StringGroovyMethods;`
- Line 13: `import org.elasticsearch.gradle.util.FileUtils;`
- Line 14: `import org.gradle.api.DefaultTask;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.file.FileTree;`
- Line 17: `import org.gradle.api.file.ProjectLayout;`
- Line 18: `import org.gradle.api.file.SourceDirectorySet;`
- Line 19: `import org.gradle.api.internal.file.FileOperations;`
- Line 20: `import org.gradle.api.provider.ListProperty;`
- Line 21: `import org.gradle.api.tasks.CacheableTask;`
- Line 22: `import org.gradle.api.tasks.InputFile;`
- Line 23: `import org.gradle.api.tasks.InputFiles;`
- Line 24: `import org.gradle.api.tasks.Internal;`
- Line 25: `import org.gradle.api.tasks.Optional;`
- Line 26: `import org.gradle.api.tasks.OutputFile;`
- Line 27: `import org.gradle.api.tasks.PathSensitive;`
- Line 28: `import org.gradle.api.tasks.PathSensitivity;`
- Line 29: `import org.gradle.api.tasks.TaskAction;`
- Line 30: `import org.gradle.initialization.layout.BuildLayout;`
- Line 32: `import java.io.File;`
- Line 33: `import java.io.IOException;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.Map;`
- Line 36: `import java.util.TreeMap;`
- Line 37: `import java.util.stream.Collectors;`
- Line 39: `import javax.inject.Inject;`
- Line 41: `import static org.apache.commons.io.FileUtils.readFileToString;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/RepositoriesSetupPlugin.java

### Exception Handling (1)
- Line 49: `throw new GradleException("Malformed lucene snapshot version: " + luceneVersion);`

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.artifacts.dsl.RepositoryHandler;`
- Line 17: `import org.gradle.api.artifacts.repositories.MavenArtifactRepository;`
- Line 19: `import java.util.regex.Matcher;`
- Line 20: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/ResolveAllDependencies.java

### Concurrency Issue (2)
- Line 86: `public void setConfigs(Collection<Configuration> configs) {`
- Line 95: `public void setResolveJavaToolChain(boolean resolveJavaToolChain) {`

### Unused Code (18)
- Line 34: `private boolean resolveJavaToolChain = false;`
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.artifacts.Configuration;`
- Line 15: `import org.gradle.api.artifacts.FileCollectionDependency;`
- Line 16: `import org.gradle.api.artifacts.component.ModuleComponentIdentifier;`
- Line 17: `import org.gradle.api.file.FileCollection;`
- Line 18: `import org.gradle.api.model.ObjectFactory;`
- Line 19: `import org.gradle.api.provider.ProviderFactory;`
- Line 20: `import org.gradle.api.tasks.InputFiles;`
- Line 21: `import org.gradle.api.tasks.Internal;`
- Line 22: `import org.gradle.api.tasks.TaskAction;`
- Line 23: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 24: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 25: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 27: `import java.util.Collection;`
- Line 28: `import java.util.stream.Collectors;`
- Line 30: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/RestrictedBuildApiService.java

### Concurrency Issue (1)
- Line 24: `public static final String BUILD_API_RESTRICTIONS_SYS_PROPERTY = "org.elasticsearch.gradle.build-api-restriction.disabled";`

### Unused Code (8)
- Line 12: `import com.google.common.collect.ArrayListMultimap;`
- Line 13: `import com.google.common.collect.ListMultimap;`
- Line 15: `import org.elasticsearch.gradle.internal.test.LegacyRestTestBasePlugin;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.provider.Property;`
- Line 19: `import org.gradle.api.services.BuildService;`
- Line 20: `import org.gradle.api.services.BuildServiceParameters;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/StringTemplatePlugin.java

### Unused Code (8)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.plugins.JavaPlugin;`
- Line 15: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 16: `import org.gradle.api.tasks.SourceSet;`
- Line 17: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 20: `import java.io.File;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/StringTemplateTask.java

### Concurrency Issue (3)
- Line 106: `public void setInputFile(File inputFile) {`
- Line 115: `public void setOutputFile(String outputFile) {`
- Line 124: `public void setProperties(Map<String, String> properties) {`

### Exception Handling (1)
- Line 88: `throw new GradleException("Cannot generate source from String template", e);`

### Unused Code (23)
- Line 94: `private File inputFile;`
- Line 96: `private String outputFile;`
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.file.DirectoryProperty;`
- Line 16: `import org.gradle.api.file.FileSystemOperations;`
- Line 17: `import org.gradle.api.model.ObjectFactory;`
- Line 18: `import org.gradle.api.provider.ListProperty;`
- Line 19: `import org.gradle.api.tasks.Input;`
- Line 20: `import org.gradle.api.tasks.InputFile;`
- Line 21: `import org.gradle.api.tasks.Nested;`
- Line 22: `import org.gradle.api.tasks.OutputDirectory;`
- Line 23: `import org.gradle.api.tasks.PathSensitive;`
- Line 24: `import org.gradle.api.tasks.PathSensitivity;`
- Line 25: `import org.gradle.api.tasks.TaskAction;`
- Line 26: `import org.stringtemplate.v4.ST;`
- Line 28: `import java.io.File;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.nio.file.Files;`
- Line 31: `import java.util.Map;`
- Line 33: `import javax.inject.Inject;`
- Line 35: `import static java.nio.charset.StandardCharsets.UTF_8;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/SymbolicLinkPreservingTar.java

### Exception Handling (2)
- Line 81: `throw new GradleException("failed writing tar file [" + tarFile + "]", e);`
- Line 186: `throw new GradleException("could not add [" + details + "] to tar file [" + tarFile + "]", e);`

### Unused Code (25)
- Line 12: `import org.apache.commons.compress.archivers.tar.TarArchiveEntry;`
- Line 13: `import org.apache.commons.compress.archivers.tar.TarArchiveOutputStream;`
- Line 14: `import org.apache.commons.compress.archivers.tar.TarConstants;`
- Line 15: `import org.apache.commons.compress.archivers.zip.UnixStat;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.file.FileCopyDetails;`
- Line 18: `import org.gradle.api.file.RegularFile;`
- Line 19: `import org.gradle.api.internal.file.CopyActionProcessingStreamAction;`
- Line 20: `import org.gradle.api.internal.file.archive.compression.ArchiveOutputStreamFactory;`
- Line 21: `import org.gradle.api.internal.file.archive.compression.Bzip2Archiver;`
- Line 22: `import org.gradle.api.internal.file.archive.compression.GzipArchiver;`
- Line 23: `import org.gradle.api.internal.file.archive.compression.SimpleCompressor;`
- Line 24: `import org.gradle.api.internal.file.copy.CopyAction;`
- Line 25: `import org.gradle.api.internal.file.copy.CopyActionProcessingStream;`
- Line 26: `import org.gradle.api.internal.file.copy.FileCopyDetailsInternal;`
- Line 27: `import org.gradle.api.provider.Provider;`
- Line 28: `import org.gradle.api.tasks.WorkResult;`
- Line 29: `import org.gradle.api.tasks.WorkResults;`
- Line 30: `import org.gradle.api.tasks.bundling.Tar;`
- Line 32: `import java.io.File;`
- Line 33: `import java.io.IOException;`
- Line 34: `import java.io.OutputStream;`
- Line 35: `import java.nio.file.Files;`
- Line 36: `import java.util.HashSet;`
- Line 37: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/patches/hdfs/HdfsClassPatcher.java

### Resource Leak (1)
- Line 120: `try (JarFile jarFile = new JarFile(inputFile); JarOutputStream jos = new JarOutputStream(new FileOutputStream(outputFile))) {`

### Exception Handling (1)
- Line 146: `throw new RuntimeException(ex);`

### Unused Code (31)
- Line 12: `import org.gradle.api.artifacts.transform.CacheableTransform;`
- Line 13: `import org.gradle.api.artifacts.transform.InputArtifact;`
- Line 14: `import org.gradle.api.artifacts.transform.TransformAction;`
- Line 15: `import org.gradle.api.artifacts.transform.TransformOutputs;`
- Line 16: `import org.gradle.api.artifacts.transform.TransformParameters;`
- Line 17: `import org.gradle.api.file.FileSystemLocation;`
- Line 18: `import org.gradle.api.provider.Provider;`
- Line 19: `import org.gradle.api.tasks.Classpath;`
- Line 20: `import org.gradle.api.tasks.Input;`
- Line 21: `import org.gradle.api.tasks.Optional;`
- Line 22: `import org.jetbrains.annotations.NotNull;`
- Line 23: `import org.objectweb.asm.ClassReader;`
- Line 24: `import org.objectweb.asm.ClassVisitor;`
- Line 25: `import org.objectweb.asm.ClassWriter;`
- Line 27: `import java.io.File;`
- Line 28: `import java.io.FileOutputStream;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.io.InputStream;`
- Line 31: `import java.util.Enumeration;`
- Line 32: `import java.util.HashMap;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Locale;`
- Line 35: `import java.util.Map;`
- Line 36: `import java.util.function.Function;`
- Line 37: `import java.util.jar.JarEntry;`
- Line 38: `import java.util.jar.JarFile;`
- Line 39: `import java.util.jar.JarOutputStream;`
- Line 40: `import java.util.regex.Pattern;`
- Line 42: `import static java.util.Map.entry;`
- Line 43: `import static org.objectweb.asm.ClassWriter.COMPUTE_FRAMES;`
- Line 44: `import static org.objectweb.asm.ClassWriter.COMPUTE_MAXS;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/patches/hdfs/MethodReplacement.java

### Unused Code (2)
- Line 12: `import org.objectweb.asm.MethodVisitor;`
- Line 13: `import org.objectweb.asm.Opcodes;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/patches/hdfs/ShellPatcher.java

### Unused Code (4)
- Line 12: `import org.objectweb.asm.ClassVisitor;`
- Line 13: `import org.objectweb.asm.ClassWriter;`
- Line 14: `import org.objectweb.asm.MethodVisitor;`
- Line 15: `import org.objectweb.asm.Opcodes;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/patches/hdfs/ShutdownHookManagerPatcher.java

### Concurrency Issue (1)
- Line 23: `private static final String CLASSNAME = "org/apache/hadoop/util/ShutdownHookManager";`

### Unused Code (8)
- Line 12: `import org.objectweb.asm.ClassVisitor;`
- Line 13: `import org.objectweb.asm.ClassWriter;`
- Line 14: `import org.objectweb.asm.MethodVisitor;`
- Line 15: `import org.objectweb.asm.Opcodes;`
- Line 16: `import org.objectweb.asm.Type;`
- Line 18: `import java.util.Set;`
- Line 19: `import java.util.concurrent.ExecutorService;`
- Line 20: `import java.util.concurrent.TimeUnit;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dependencies/patches/hdfs/SubjectGetSubjectPatcher.java

### Concurrency Issue (1)
- Line 35: `private static final String SUBJECT_CLASS_INTERNAL_NAME = "javax/security/auth/Subject";`

### Unused Code (7)
- Line 12: `import org.objectweb.asm.ClassVisitor;`
- Line 13: `import org.objectweb.asm.ClassWriter;`
- Line 14: `import org.objectweb.asm.MethodVisitor;`
- Line 15: `import org.objectweb.asm.Type;`
- Line 17: `import static org.objectweb.asm.Opcodes.ASM9;`
- Line 18: `import static org.objectweb.asm.Opcodes.INVOKESTATIC;`
- Line 19: `import static org.objectweb.asm.Opcodes.POP;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/DebElasticsearchDistributionType.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 13: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 14: `import org.elasticsearch.gradle.Version;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/DockerCloudEssElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/DockerElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/DockerIronBankElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/DockerWolfiElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/ElasticsearchDistributionExtension.java

### Concurrency Issue (1)
- Line 26: `private static final Pattern CONFIG_BIN_REGEX_PATTERN = Pattern.compile("([^\\/]+\\/)?(config|bin)\\/.*");`

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.plugin.PluginPropertiesExtension;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.artifacts.Configuration;`
- Line 15: `import org.gradle.api.tasks.AbstractCopyTask;`
- Line 16: `import org.gradle.api.tasks.TaskProvider;`
- Line 18: `import java.io.File;`
- Line 19: `import java.util.Map;`
- Line 20: `import java.util.concurrent.Callable;`
- Line 21: `import java.util.regex.Pattern;`
- Line 23: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.EXPLODED_BUNDLE_CONFIG;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/ElasticsearchDistributionPlugin.java

### Unused Code (2)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/InternalElasticsearchDistributionTypes.java

### Concurrency Issue (6)
- Line 17: `public static final ElasticsearchDistributionType DEB = new DebElasticsearchDistributionType();`
- Line 18: `public static final ElasticsearchDistributionType RPM = new RpmElasticsearchDistributionType();`
- Line 19: `public static final ElasticsearchDistributionType DOCKER = new DockerElasticsearchDistributionType();`
- Line 20: `public static final ElasticsearchDistributionType DOCKER_IRONBANK = new DockerIronBankElasticsearchDistributionType();`
- Line 21: `public static final ElasticsearchDistributionType DOCKER_CLOUD_ESS = new DockerCloudEssElasticsearchDistributionType();`
- Line 22: `public static final ElasticsearchDistributionType DOCKER_WOLFI = new DockerWolfiElasticsearchDistributionType();`

### Unused Code (2)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 14: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/distribution/RpmElasticsearchDistributionType.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/AsciidocSnippetParser.java

### Concurrency Issue (10)
- Line 18: `public static final Pattern SNIPPET_PATTERN = Pattern.compile("-{4,}\\s*");`
- Line 19: `public static final Pattern TEST_RESPONSE_PATTERN = Pattern.compile("\\/\\/\s*TESTRESPONSE(\\[(.+)\\])?\s*");`
- Line 20: `public static final Pattern SOURCE_PATTERN = Pattern.compile(`
- Line 24: `public static final String CONSOLE_REGEX = "\\/\\/\s*CONSOLE\s*";`
- Line 25: `public static final String NOTCONSOLE_REGEX = "\\/\\/\s*NOTCONSOLE\s*";`
- Line 26: `public static final String TESTSETUP_REGEX = "\\/\\/\s*TESTSETUP\s*";`
- Line 27: `public static final String TEARDOWN_REGEX = "\\/\\/\s*TEARDOWN\s*";`
- Line 42: `private int lastLanguageLine = 0;`
- Line 43: `private String currentName = null;`
- Line 44: `private String lastLanguage = null;`

### Unused Code (7)
- Line 42: `private int lastLanguageLine = 0;`
- Line 43: `private String currentName = null;`
- Line 44: `private String lastLanguage = null;`
- Line 12: `import java.util.List;`
- Line 13: `import java.util.Map;`
- Line 14: `import java.util.regex.Matcher;`
- Line 15: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/DocSnippetTask.java

### Concurrency Issue (2)
- Line 44: `public void setDocs(ConfigurableFileTree docs) {`
- Line 78: `public void setPerSnippet(Action<Snippet> perSnippet) {`

### Unused Code (11)
- Line 37: `private ConfigurableFileTree docs;`
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.InvalidUserDataException;`
- Line 15: `import org.gradle.api.file.ConfigurableFileTree;`
- Line 16: `import org.gradle.api.provider.MapProperty;`
- Line 17: `import org.gradle.api.tasks.Input;`
- Line 18: `import org.gradle.api.tasks.InputFiles;`
- Line 19: `import org.gradle.api.tasks.TaskAction;`
- Line 21: `import java.io.File;`
- Line 22: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/DocsTestPlugin.java

### Unused Code (19)
- Line 33: `private FileOperations fileOperations;`
- Line 34: `private ProjectLayout projectLayout;`
- Line 12: `import org.elasticsearch.gradle.OS;`
- Line 13: `import org.elasticsearch.gradle.Version;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 15: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 16: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 17: `import org.elasticsearch.gradle.testclusters.TestDistribution;`
- Line 18: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 19: `import org.gradle.api.Plugin;`
- Line 20: `import org.gradle.api.Project;`
- Line 21: `import org.gradle.api.file.Directory;`
- Line 22: `import org.gradle.api.file.ProjectLayout;`
- Line 23: `import org.gradle.api.internal.file.FileOperations;`
- Line 24: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 25: `import org.gradle.api.provider.Provider;`
- Line 26: `import org.gradle.api.tasks.TaskProvider;`
- Line 28: `import java.util.Map;`
- Line 30: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/MdxSnippetParser.java

### Concurrency Issue (7)
- Line 19: `public static final Pattern SNIPPET_PATTERN = Pattern.compile("```(.*)");`
- Line 21: `public static final Pattern TEST_RESPONSE_PATTERN = Pattern.compile("\\{\\/\\*\s*TESTRESPONSE(\\[(.*)\\])?\s\\*\\/\\}");`
- Line 22: `public static final Pattern TEST_PATTERN = Pattern.compile("\\{\\/\\*\s*TEST(\\[(.*)\\])?\s\\*\\/\\}");`
- Line 23: `public static final String CONSOLE_REGEX = "\\{\\/\\*\s*CONSOLE\s\\*\\/\\}";`
- Line 24: `public static final String NOTCONSOLE_REGEX = "\\{\\/\\*\s*NOTCONSOLE\s\\*\\/\\}";`
- Line 25: `public static final String TESTSETUP_REGEX = "\\{\\/\\*\s*TESTSETUP\s\\*\\/\\}";`
- Line 26: `public static final String TEARDOWN_REGEX = "\\{\\/\\*\s*TEARDOWN\s\\*\\/\\}";`

### Unused Code (4)
- Line 12: `import java.util.List;`
- Line 13: `import java.util.Map;`
- Line 14: `import java.util.regex.Matcher;`
- Line 15: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/ParsingUtils.java

### Exception Handling (1)
- Line 49: `throw new InvalidUserDataException("Didn't match " + pattern + ": " + content);`

### Unused Code (4)
- Line 12: `import org.gradle.api.InvalidUserDataException;`
- Line 14: `import java.util.function.BiConsumer;`
- Line 15: `import java.util.regex.Matcher;`
- Line 16: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/RestTestsFromDocSnippetTask.java

### Exception Handling (16)
- Line 138: `throw new InvalidUserDataException("Invalid block quote starting at " + start + " in:\n" + body);`
- Line 219: `throw new InvalidUserDataException(snippet + ": No paired previous test");`
- Line 222: `throw new InvalidUserDataException(snippet + ": Result can't be first in file");`
- Line 228: `throw new InvalidUserDataException(snippet + ": Use `[source,console]` instead of `// CONSOLE`.");`
- Line 244: `throw new InvalidUserDataException("// TEST[continued] " + "cannot be on first snippet in a file: " + test);`
- Line 247: `throw new InvalidUserDataException("// TEST[continued] " + "cannot immediately follow // TESTSETUP: " + test);`
- Line 250: `throw new InvalidUserDataException("// TEST[continued] " + "cannot immediately follow // TEARDOWN: " + test);`
- Line 276: `throw new InvalidUserDataException("Continued snippets " + "can't be skipped");`
- Line 305: `throw new InvalidUserDataException("Couldn't find named teardown $name for " + snippet);`
- Line 314: `throw new InvalidUserDataException(snippet + " must follow test setup or be first");`
- Line 428: `throw new InvalidUserDataException(`
- Line 446: `throw new RuntimeException(e);`
- Line 452: `throw new InvalidUserDataException(`
- Line 470: `throw new InvalidUserDataException("Couldn't find named setup " + name + " for " + snippet);`
- Line 502: `throw new InvalidUserDataException(message);`
- Line 548: `throw new RuntimeException(e);`

### Unused Code (24)
- Line 12: `import groovy.transform.PackageScope;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.InvalidUserDataException;`
- Line 16: `import org.gradle.api.file.DirectoryProperty;`
- Line 17: `import org.gradle.api.provider.ListProperty;`
- Line 18: `import org.gradle.api.provider.MapProperty;`
- Line 19: `import org.gradle.api.provider.Property;`
- Line 20: `import org.gradle.api.tasks.Input;`
- Line 21: `import org.gradle.api.tasks.Internal;`
- Line 22: `import org.gradle.api.tasks.OutputDirectory;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.PrintWriter;`
- Line 27: `import java.nio.file.Files;`
- Line 28: `import java.nio.file.Path;`
- Line 29: `import java.util.ArrayList;`
- Line 30: `import java.util.Collections;`
- Line 31: `import java.util.HashSet;`
- Line 32: `import java.util.LinkedHashMap;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Map;`
- Line 35: `import java.util.Set;`
- Line 36: `import java.util.stream.Collectors;`
- Line 38: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/Snippet.java

### Unused Code (2)
- Line 12: `import java.nio.file.Path;`
- Line 13: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/SnippetBuilder.java

### Concurrency Issue (5)
- Line 28: `static final int NOT_FINISHED = -1;`
- Line 34: `private int end = NOT_FINISHED;`
- Line 38: `private MultiValueMap substitutions = MultiValueMap.decorate(new LinkedHashMap<String, String>());`
- Line 50: `private StringBuilder contentBuilder = new StringBuilder();`
- Line 51: `private Boolean console = null;`

### Exception Handling (3)
- Line 207: `throw new InvalidUserDataException(`
- Line 226: `throw new InvalidUserDataException(name + ": " + "No need for NOTCONSOLE if snippet doesn't " + "contain `curl`.");`
- Line 260: `throw new RuntimeException(e);`

### Unused Code (31)
- Line 30: `private Path path;`
- Line 31: `private int lineNumber;`
- Line 32: `private String name;`
- Line 33: `private String language;`
- Line 34: `private int end = NOT_FINISHED;`
- Line 35: `private boolean testSetup;`
- Line 36: `private boolean testTeardown;`
- Line 38: `private MultiValueMap substitutions = MultiValueMap.decorate(new LinkedHashMap<String, String>());`
- Line 39: `private String catchPart;`
- Line 40: `private boolean test;`
- Line 41: `private String skip;`
- Line 42: `private boolean continued;`
- Line 43: `private String setup;`
- Line 44: `private String teardown;`
- Line 46: `private boolean skipShardsFailures;`
- Line 47: `private boolean testResponse;`
- Line 48: `private boolean curl;`
- Line 50: `private StringBuilder contentBuilder = new StringBuilder();`
- Line 51: `private Boolean console = null;`
- Line 12: `import com.fasterxml.jackson.core.JsonFactory;`
- Line 13: `import com.fasterxml.jackson.core.JsonParseException;`
- Line 14: `import com.fasterxml.jackson.core.JsonParser;`
- Line 16: `import org.apache.commons.collections.map.MultiValueMap;`
- Line 17: `import org.gradle.api.InvalidUserDataException;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.file.Path;`
- Line 21: `import java.util.ArrayList;`
- Line 22: `import java.util.LinkedHashMap;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/SnippetParser.java

### Null Pointer (1)
- Line 52: `protected SnippetBuilder snippetBuilder = null;`

### Concurrency Issue (10)
- Line 27: `protected static final String SCHAR = "(?:\\\\\\/|[^\\/])";`
- Line 28: `protected static final String NON_JSON = "(non_json)";`
- Line 29: `protected static final String SKIP_REGEX = "skip:([^\\]]+)";`
- Line 30: `protected static final String SUBSTITUTION = "s\\/(" + SCHAR + "+)\\/(" + SCHAR + "*)\\/";`
- Line 32: `private static final String CATCH = "catch:\\s*((?:\\/[^\\/]+\\/)|[^ \\]]+)";`
- Line 33: `private static final String SETUP = "setup:([^ \\]]+)";`
- Line 34: `private static final String TEARDOWN = "teardown:([^ \\]]+)";`
- Line 35: `private static final String WARNING = "warning:(.+)";`
- Line 36: `private static final String TEST_SYNTAX = "(?:"`
- Line 52: `protected SnippetBuilder snippetBuilder = null;`

### Exception Handling (9)
- Line 67: `throw new SnippetParserException("Failed to parse file " + docFile, e);`
- Line 81: `throw new SnippetParserException(file, lineNumber, e);`
- Line 146: `throw new InvalidUserDataException("TESTRESPONSE not paired with a snippet at ");`
- Line 179: `throw new InvalidUserDataException("TEST not paired with a snippet at ");`
- Line 216: `throw new InvalidUserDataException("Invalid test marker: " + line);`
- Line 227: `throw new InvalidUserDataException("CONSOLE not paired with a snippet");`
- Line 230: `throw new InvalidUserDataException("Can't be both CONSOLE and NOTCONSOLE");`
- Line 236: `throw new InvalidUserDataException("NOTCONSOLE not paired with a snippet");`
- Line 239: `throw new InvalidUserDataException("Can't be both CONSOLE and NOTCONSOLE");`

### Unused Code (13)
- Line 54: `private Path currentPath;`
- Line 12: `import org.gradle.api.InvalidUserDataException;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.nio.charset.StandardCharsets;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.regex.Matcher;`
- Line 23: `import java.util.regex.Pattern;`
- Line 24: `import java.util.stream.Stream;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/doc/SnippetParserException.java

### Unused Code (2)
- Line 12: `import org.gradle.api.InvalidUserDataException;`
- Line 14: `import java.io.File;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerBuildTask.java

### Concurrency Issue (7)
- Line 99: `public void setTags(String[] tags) {`
- Line 108: `public void setPull(boolean pull) {`
- Line 117: `public void setNoCache(boolean noCache) {`
- Line 126: `public void setBaseImages(String[] baseImages) {`
- Line 52: `private static final Logger LOGGER = Logging.getLogger(DockerBuildTask.class);`
- Line 59: `private boolean pull = true;`
- Line 60: `private boolean noCache = true;`

### Exception Handling (2)
- Line 183: `throw new GradleException("Failed to pull Docker base image [" + baseImage + "], all attempts failed");`
- Line 243: `throw new RuntimeException("Failed to write marker file", e);`

### Unused Code (35)
- Line 59: `private boolean pull = true;`
- Line 60: `private boolean noCache = true;`
- Line 11: `import org.elasticsearch.gradle.Architecture;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.file.DirectoryProperty;`
- Line 16: `import org.gradle.api.file.ProjectLayout;`
- Line 17: `import org.gradle.api.file.RegularFileProperty;`
- Line 18: `import org.gradle.api.logging.Logger;`
- Line 19: `import org.gradle.api.logging.Logging;`
- Line 20: `import org.gradle.api.model.ObjectFactory;`
- Line 21: `import org.gradle.api.provider.ListProperty;`
- Line 22: `import org.gradle.api.provider.MapProperty;`
- Line 23: `import org.gradle.api.provider.Property;`
- Line 24: `import org.gradle.api.provider.SetProperty;`
- Line 25: `import org.gradle.api.tasks.Input;`
- Line 26: `import org.gradle.api.tasks.InputDirectory;`
- Line 27: `import org.gradle.api.tasks.Optional;`
- Line 28: `import org.gradle.api.tasks.OutputFile;`
- Line 29: `import org.gradle.api.tasks.PathSensitive;`
- Line 30: `import org.gradle.api.tasks.PathSensitivity;`
- Line 31: `import org.gradle.api.tasks.TaskAction;`
- Line 32: `import org.gradle.process.ExecOperations;`
- Line 33: `import org.gradle.process.ExecSpec;`
- Line 34: `import org.gradle.workers.WorkAction;`
- Line 35: `import org.gradle.workers.WorkParameters;`
- Line 36: `import org.gradle.workers.WorkerExecutor;`
- Line 38: `import java.io.ByteArrayOutputStream;`
- Line 39: `import java.io.IOException;`
- Line 40: `import java.nio.file.Files;`
- Line 41: `import java.util.Arrays;`
- Line 42: `import java.util.List;`
- Line 43: `import java.util.stream.Collectors;`
- Line 45: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerResult.java

### Concurrency Issue (3)
- Line 43: `public void setExitCode(int exitCode) {`
- Line 47: `public void setStdout(String stdout) {`
- Line 51: `public void setStderr(String stderr) {`

### Unused Code (4)
- Line 21: `private int exitCode;`
- Line 22: `private String stdout;`
- Line 23: `private String stderr;`
- Line 12: `import java.util.Objects;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerSupportPlugin.java

### Concurrency Issue (1)
- Line 28: `public static final String DOCKER_SUPPORT_SERVICE_NAME = "dockerSupportService";`

### Unused Code (9)
- Line 11: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.provider.Provider;`
- Line 17: `import java.io.File;`
- Line 18: `import java.util.List;`
- Line 19: `import java.util.stream.Collectors;`
- Line 21: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerSupportService.java

### Concurrency Issue (2)
- Line 51: `private static final Logger LOGGER = Logging.getLogger(DockerSupportService.class);`
- Line 58: `private static final Version MINIMUM_DOCKER_VERSION = Version.fromString("17.05.0");`

### Exception Handling (2)
- Line 252: `throw new GradleException("Failed to read /etc/os-release", e);`
- Line 335: `throw new GradleException(`

### Unused Code (30)
- Line 61: `private DockerAvailability dockerAvailability;`
- Line 11: `import com.avast.gradle.dockercompose.ServiceInfo;`
- Line 13: `import org.elasticsearch.gradle.Architecture;`
- Line 14: `import org.elasticsearch.gradle.OS;`
- Line 15: `import org.elasticsearch.gradle.Version;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.logging.Logger;`
- Line 18: `import org.gradle.api.logging.Logging;`
- Line 19: `import org.gradle.api.provider.Property;`
- Line 20: `import org.gradle.api.provider.ProviderFactory;`
- Line 21: `import org.gradle.api.services.BuildService;`
- Line 22: `import org.gradle.api.services.BuildServiceParameters;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.nio.file.Paths;`
- Line 29: `import java.util.Arrays;`
- Line 30: `import java.util.Collections;`
- Line 31: `import java.util.EnumSet;`
- Line 32: `import java.util.HashMap;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Locale;`
- Line 35: `import java.util.Map;`
- Line 36: `import java.util.Optional;`
- Line 37: `import java.util.Set;`
- Line 38: `import java.util.stream.Collectors;`
- Line 39: `import java.util.stream.Stream;`
- Line 41: `import javax.inject.Inject;`
- Line 43: `import static java.util.function.Predicate.not;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/DockerValueSource.java

### Exception Handling (1)
- Line 53: `throw new IllegalArgumentException("Cannot execute with no command");`

### Unused Code (9)
- Line 12: `import org.gradle.api.provider.ListProperty;`
- Line 13: `import org.gradle.api.provider.Property;`
- Line 14: `import org.gradle.api.provider.ValueSource;`
- Line 15: `import org.gradle.api.provider.ValueSourceParameters;`
- Line 16: `import org.gradle.process.ExecOperations;`
- Line 17: `import org.gradle.process.ExecResult;`
- Line 19: `import java.io.ByteArrayOutputStream;`
- Line 20: `import java.util.List;`
- Line 22: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/ShellRetry.java

### Unused Code (2)
- Line 12: `import java.util.stream.Collectors;`
- Line 13: `import java.util.stream.IntStream;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/docker/TransformLog4jConfigFilter.java

### Unused Code (7)
- Line 12: `import org.apache.commons.io.IOUtils;`
- Line 14: `import java.io.FilterReader;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.io.Reader;`
- Line 17: `import java.io.StringReader;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/dra/DraResolvePlugin.java

### Concurrency Issue (3)
- Line 26: `public static final String USE_DRA_ARTIFACTS_FLAG = "dra.artifacts";`
- Line 27: `public static final String DRA_WORKFLOW = "dra.workflow";`
- Line 28: `public static final String DRA_ARTIFACTS_DEPENDENCY_PREFIX = "dra.artifacts.dependency";`

### Unused Code (8)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.provider.Provider;`
- Line 15: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.stream.Collectors;`
- Line 20: `import javax.inject.Inject;`
- Line 22: `import static java.util.Map.Entry;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/idea/EnablePreviewFeaturesTask.java

### Unused Code (6)
- Line 12: `import groovy.util.Node;`
- Line 13: `import groovy.util.NodeList;`
- Line 15: `import org.gradle.api.DefaultTask;`
- Line 16: `import org.xml.sax.SAXException;`
- Line 18: `import java.io.IOException;`
- Line 20: `import javax.xml.parsers.ParserConfigurationException;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/idea/IdeaXmlUtil.java

### Unused Code (9)
- Line 12: `import groovy.util.Node;`
- Line 13: `import groovy.util.XmlParser;`
- Line 14: `import groovy.xml.XmlNodePrinter;`
- Line 16: `import org.gradle.api.Action;`
- Line 17: `import org.xml.sax.SAXException;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.io.PrintWriter;`
- Line 23: `import javax.xml.parsers.ParserConfigurationException;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/BuildParameterExtension.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.internal.BwcVersions;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.JavaVersion;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.jvm.toolchain.JavaToolchainSpec;`
- Line 19: `import java.io.File;`
- Line 20: `import java.time.ZonedDateTime;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Random;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/BuildParameterService.java

### Unused Code (3)
- Line 12: `import org.gradle.api.provider.Property;`
- Line 13: `import org.gradle.api.services.BuildService;`
- Line 14: `import org.gradle.api.services.BuildServiceParameters;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/DefaultBuildParameterExtension.java

### Concurrency Issue (2)
- Line 237: `public void setBwcVersions(Provider<BwcVersions> bwcVersions) {`
- Line 242: `public void setGitOrigin(Provider<String> gitOrigin) {`

### Unused Code (15)
- Line 216: `private T instance;`
- Line 12: `import org.elasticsearch.gradle.internal.BwcVersions;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.JavaVersion;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.provider.ProviderFactory;`
- Line 18: `import org.gradle.jvm.toolchain.JavaToolchainSpec;`
- Line 20: `import java.io.File;`
- Line 21: `import java.time.ZoneOffset;`
- Line 22: `import java.time.ZonedDateTime;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Random;`
- Line 25: `import java.util.concurrent.atomic.AtomicReference;`
- Line 26: `import java.util.function.Supplier;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/GlobalBuildInfoPlugin.java

### Resource Leak (3)
- Line 197: `try (var is = new FileInputStream(versionsFilePath)) {`
- Line 208: `try (InputStream is = new FileInputStream(branchesFile)) {`
- Line 365: `BufferedReader reader = new BufferedReader(new InputStreamReader(GlobalBuildInfoPlugin.class.getResourceAsStream(resourcePath)))`

### Concurrency Issue (2)
- Line 68: `private static final Logger LOGGER = Logging.getLogger(GlobalBuildInfoPlugin.class);`
- Line 69: `private static final String DEFAULT_VERSION_JAVA_FILE_PATH = "server/src/main/java/org/elasticsearch/Version.java";`

### Exception Handling (7)
- Line 176: `throw new GradleException(`
- Line 201: `throw new IllegalStateException("Unable to resolve to resolve bwc versions from versionsFile.", e);`
- Line 214: `throw new UncheckedIOException(e);`
- Line 280: `throw new UncheckedIOException(ioException);`
- Line 325: `throw new GradleException(message);`
- Line 331: `throw new GradleException(`
- Line 377: `throw new UncheckedIOException("Error trying to read classpath resource: " + resourcePath, e);`

### Unused Code (54)
- Line 71: `private ObjectFactory objectFactory;`
- Line 76: `private JavaToolchainService toolChainService;`
- Line 77: `private Project project;`
- Line 11: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 14: `import org.apache.commons.io.IOUtils;`
- Line 15: `import org.elasticsearch.gradle.VersionProperties;`
- Line 16: `import org.elasticsearch.gradle.internal.BwcVersions;`
- Line 17: `import org.elasticsearch.gradle.internal.conventions.GitInfoPlugin;`
- Line 18: `import org.elasticsearch.gradle.internal.conventions.info.GitInfo;`
- Line 19: `import org.elasticsearch.gradle.internal.conventions.info.ParallelDetector;`
- Line 20: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 21: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 22: `import org.gradle.api.Action;`
- Line 23: `import org.gradle.api.GradleException;`
- Line 24: `import org.gradle.api.JavaVersion;`
- Line 25: `import org.gradle.api.Plugin;`
- Line 26: `import org.gradle.api.Project;`
- Line 27: `import org.gradle.api.logging.Logger;`
- Line 28: `import org.gradle.api.logging.Logging;`
- Line 29: `import org.gradle.api.model.ObjectFactory;`
- Line 30: `import org.gradle.api.plugins.JvmToolchainsPlugin;`
- Line 31: `import org.gradle.api.provider.Property;`
- Line 32: `import org.gradle.api.provider.Provider;`
- Line 33: `import org.gradle.api.provider.ProviderFactory;`
- Line 34: `import org.gradle.internal.jvm.Jvm;`
- Line 35: `import org.gradle.internal.jvm.inspection.JavaInstallationRegistry;`
- Line 36: `import org.gradle.internal.jvm.inspection.JvmInstallationMetadata;`
- Line 37: `import org.gradle.internal.jvm.inspection.JvmMetadataDetector;`
- Line 38: `import org.gradle.internal.jvm.inspection.JvmVendor;`
- Line 39: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 40: `import org.gradle.jvm.toolchain.JavaToolchainService;`
- Line 41: `import org.gradle.jvm.toolchain.JavaToolchainSpec;`
- Line 42: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 43: `import org.gradle.jvm.toolchain.internal.InstallationLocation;`
- Line 44: `import org.gradle.util.GradleVersion;`
- Line 45: `import org.jetbrains.annotations.NotNull;`
- Line 47: `import java.io.BufferedReader;`
- Line 48: `import java.io.File;`
- Line 49: `import java.io.FileInputStream;`
- Line 50: `import java.io.IOException;`
- Line 51: `import java.io.InputStream;`
- Line 52: `import java.io.InputStreamReader;`
- Line 53: `import java.io.UncheckedIOException;`
- Line 54: `import java.nio.file.Files;`
- Line 55: `import java.util.ArrayList;`
- Line 56: `import java.util.List;`
- Line 57: `import java.util.Locale;`
- Line 58: `import java.util.Random;`
- Line 59: `import java.util.concurrent.atomic.AtomicReference;`
- Line 60: `import java.util.stream.Collectors;`
- Line 61: `import java.util.stream.Stream;`
- Line 63: `import javax.inject.Inject;`
- Line 65: `import static org.elasticsearch.gradle.internal.conventions.GUtils.elvis;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/info/JavaHome.java

### Unused Code (3)
- Line 16: `private Integer version;`
- Line 11: `import org.gradle.api.provider.Provider;`
- Line 13: `import java.io.File;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/packer/CacheCacheableTestFixtures.java

### Exception Handling (3)
- Line 90: `throw new RuntimeException(e);`
- Line 103: `throw new InvalidUserDataException("Missing 'classesDirs' or 'classpath' property.");`
- Line 116: `throw new InvalidUserDataException("Failed to build classpath URLs.", mfue);`

### Unused Code (25)
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.InvalidUserDataException;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.tasks.CompileClasspath;`
- Line 17: `import org.gradle.api.tasks.TaskAction;`
- Line 18: `import org.gradle.workers.WorkAction;`
- Line 19: `import org.gradle.workers.WorkParameters;`
- Line 20: `import org.gradle.workers.WorkQueue;`
- Line 21: `import org.gradle.workers.WorkerExecutor;`
- Line 22: `import org.reflections.Reflections;`
- Line 23: `import org.reflections.scanners.SubTypesScanner;`
- Line 24: `import org.reflections.util.ClasspathHelper;`
- Line 25: `import org.reflections.util.ConfigurationBuilder;`
- Line 27: `import java.io.File;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.lang.reflect.Constructor;`
- Line 30: `import java.lang.reflect.Method;`
- Line 31: `import java.lang.reflect.Modifier;`
- Line 32: `import java.net.MalformedURLException;`
- Line 33: `import java.net.URL;`
- Line 34: `import java.net.URLClassLoader;`
- Line 35: `import java.util.LinkedHashSet;`
- Line 36: `import java.util.Set;`
- Line 38: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/packer/CacheTestFixtureResourcesPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.internal.ResolveAllDependencies;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.artifacts.Dependency;`
- Line 17: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 18: `import org.gradle.api.plugins.JavaPlugin;`
- Line 19: `import org.gradle.api.plugins.JavaPluginExtension;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/CheckForbiddenApisTask.java

### Concurrency Issue (11)
- Line 144: `public void setClassesDirs(FileCollection classesDirs) {`
- Line 170: `public void setClasspath(FileCollection classpath) {`
- Line 192: `public void setResourcesDir(File resourcesDir) {`
- Line 197: `public void setSignaturesFiles(FileCollection signaturesFiles) {`
- Line 234: `public void setSignatures(List<String> signatures) {`
- Line 251: `public void setIgnoreFailures(boolean ignoreFailures) {`
- Line 260: `public void setIgnoreMissingClasses(boolean ignoreMissingClasses) {`
- Line 277: `public void setTargetCompatibility(String targetCompatibility) {`
- Line 86: `private static final String NL = System.getProperty("line.separator", "\n");`
- Line 87: `private final PatternSet patternSet = new PatternSet().include("**/*.class");`
- Line 101: `private boolean ignoreFailures = false;`

### Exception Handling (7)
- Line 463: `throw new GradleException("IO problem while reading files with API signatures.", ioe);`
- Line 470: `throw new InvalidUserDataException(`
- Line 482: `throw new GradleException("Failed to load one of the given class files.", ioe);`
- Line 487: `throw new VerificationException("Forbidden API verification failed", e);`
- Line 489: `throw new RuntimeException(e);`
- Line 506: `throw new InvalidUserDataException("Missing 'classesDirs' or 'classpath' property.");`
- Line 520: `throw new InvalidUserDataException("Failed to build classpath URLs.", mfue);`

### Unused Code (72)
- Line 88: `private FileCollection classesDirs;`
- Line 89: `private FileCollection classpath;`
- Line 90: `private String targetCompatibility;`
- Line 92: `private FileCollection signaturesFiles;`
- Line 95: `private ProjectLayout projectLayout;`
- Line 99: `private File resourcesDir;`
- Line 101: `private boolean ignoreFailures = false;`
- Line 102: `private boolean ignoreMissingClasses = false;`
- Line 12: `import de.thetaphi.forbiddenapis.Checker;`
- Line 13: `import de.thetaphi.forbiddenapis.Constants;`
- Line 14: `import de.thetaphi.forbiddenapis.ForbiddenApiException;`
- Line 15: `import de.thetaphi.forbiddenapis.Logger;`
- Line 16: `import de.thetaphi.forbiddenapis.ParseException;`
- Line 17: `import groovy.lang.Closure;`
- Line 19: `import org.gradle.api.DefaultTask;`
- Line 20: `import org.gradle.api.GradleException;`
- Line 21: `import org.gradle.api.InvalidUserDataException;`
- Line 22: `import org.gradle.api.Transformer;`
- Line 23: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 24: `import org.gradle.api.file.FileCollection;`
- Line 25: `import org.gradle.api.file.FileTree;`
- Line 26: `import org.gradle.api.file.FileTreeElement;`
- Line 27: `import org.gradle.api.file.ProjectLayout;`
- Line 28: `import org.gradle.api.file.RegularFileProperty;`
- Line 29: `import org.gradle.api.logging.Logging;`
- Line 30: `import org.gradle.api.model.ObjectFactory;`
- Line 31: `import org.gradle.api.provider.ListProperty;`
- Line 32: `import org.gradle.api.provider.Property;`
- Line 33: `import org.gradle.api.provider.SetProperty;`
- Line 34: `import org.gradle.api.specs.Spec;`
- Line 35: `import org.gradle.api.tasks.CacheableTask;`
- Line 36: `import org.gradle.api.tasks.CompileClasspath;`
- Line 37: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 38: `import org.gradle.api.tasks.Input;`
- Line 39: `import org.gradle.api.tasks.InputDirectory;`
- Line 40: `import org.gradle.api.tasks.InputFiles;`
- Line 41: `import org.gradle.api.tasks.Internal;`
- Line 42: `import org.gradle.api.tasks.Optional;`
- Line 43: `import org.gradle.api.tasks.OutputFile;`
- Line 44: `import org.gradle.api.tasks.PathSensitive;`
- Line 45: `import org.gradle.api.tasks.PathSensitivity;`
- Line 46: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 47: `import org.gradle.api.tasks.TaskAction;`
- Line 48: `import org.gradle.api.tasks.VerificationException;`
- Line 49: `import org.gradle.api.tasks.VerificationTask;`
- Line 50: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 51: `import org.gradle.api.tasks.util.PatternSet;`
- Line 52: `import org.gradle.workers.WorkAction;`
- Line 53: `import org.gradle.workers.WorkParameters;`
- Line 54: `import org.gradle.workers.WorkQueue;`
- Line 55: `import org.gradle.workers.WorkerExecutor;`
- Line 56: `import org.jetbrains.annotations.NotNull;`
- Line 58: `import java.io.File;`
- Line 59: `import java.io.IOException;`
- Line 60: `import java.lang.annotation.RetentionPolicy;`
- Line 61: `import java.net.MalformedURLException;`
- Line 62: `import java.net.URL;`
- Line 63: `import java.net.URLClassLoader;`
- Line 64: `import java.nio.file.Files;`
- Line 65: `import java.nio.file.StandardOpenOption;`
- Line 66: `import java.util.ArrayList;`
- Line 67: `import java.util.EnumSet;`
- Line 68: `import java.util.LinkedHashSet;`
- Line 69: `import java.util.List;`
- Line 70: `import java.util.Locale;`
- Line 71: `import java.util.Objects;`
- Line 72: `import java.util.Set;`
- Line 74: `import javax.inject.Inject;`
- Line 76: `import static de.thetaphi.forbiddenapis.Checker.Option.DISABLE_CLASSLOADING_CACHE;`
- Line 77: `import static de.thetaphi.forbiddenapis.Checker.Option.FAIL_ON_MISSING_CLASSES;`
- Line 78: `import static de.thetaphi.forbiddenapis.Checker.Option.FAIL_ON_UNRESOLVABLE_SIGNATURES;`
- Line 79: `import static de.thetaphi.forbiddenapis.Checker.Option.FAIL_ON_VIOLATION;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/CheckstylePrecommitPlugin.java

### Exception Handling (3)
- Line 56: `throw new UncheckedIOException(e);`
- Line 75: `throw new UncheckedIOException(e);`
- Line 80: `throw new UncheckedIOException(e);`

### Unused Code (21)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.artifacts.VersionCatalogsExtension;`
- Line 17: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 18: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 19: `import org.gradle.api.plugins.quality.Checkstyle;`
- Line 20: `import org.gradle.api.plugins.quality.CheckstyleExtension;`
- Line 21: `import org.gradle.api.provider.Provider;`
- Line 22: `import org.gradle.api.tasks.PathSensitivity;`
- Line 23: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 24: `import org.gradle.api.tasks.TaskProvider;`
- Line 26: `import java.io.File;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.InputStream;`
- Line 29: `import java.io.UncheckedIOException;`
- Line 30: `import java.net.JarURLConnection;`
- Line 31: `import java.net.URL;`
- Line 32: `import java.nio.file.Files;`
- Line 33: `import java.nio.file.StandardCopyOption;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/CopyCheckStyleConfTask.java

### Unused Code (3)
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.file.FileSystemOperations;`
- Line 15: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/DependencyLicensesPrecommitPlugin.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.dependencies.CompileOnlyResolvePlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.artifacts.component.ComponentIdentifier;`
- Line 17: `import org.gradle.api.artifacts.component.ModuleComponentIdentifier;`
- Line 18: `import org.gradle.api.plugins.JavaPlugin;`
- Line 19: `import org.gradle.api.specs.Spec;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/DependencyLicensesTask.java

### Concurrency Issue (2)
- Line 162: `public void setDependencies(FileCollection dependencies) {`
- Line 99: `private final Pattern regex = Pattern.compile("-v?\\d+.*");`

### Exception Handling (7)
- Line 138: `throw new InvalidUserDataException("Missing \"from\" setting for license name mapping");`
- Line 142: `throw new InvalidUserDataException("Missing \"to\" setting for license name mapping");`
- Line 204: `throw new GradleException("No dependencies variable defined.");`
- Line 209: `throw new GradleException("Licenses dir " + licensesDirAsFile + " exists, but there are no dependencies");`
- Line 217: `throw new GradleException("Licences dir " + licensesDirAsFile + " does not exist, but there are dependencies: " + deps);`
- Line 262: `throw new GradleException("Unused " + type + " " + item);`
- Line 302: `throw new GradleException("Missing " + type + " for " + jarName + ", expected in " + fileName);`

### Unused Code (41)
- Line 108: `private FileCollection dependencies;`
- Line 129: `private ProjectLayout projectLayout;`
- Line 11: `import org.elasticsearch.gradle.internal.precommit.LicenseAnalyzer.LicenseInfo;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.InvalidUserDataException;`
- Line 15: `import org.gradle.api.artifacts.Configuration;`
- Line 16: `import org.gradle.api.artifacts.component.ComponentIdentifier;`
- Line 17: `import org.gradle.api.file.Directory;`
- Line 18: `import org.gradle.api.file.DirectoryProperty;`
- Line 19: `import org.gradle.api.file.FileCollection;`
- Line 20: `import org.gradle.api.file.ProjectLayout;`
- Line 21: `import org.gradle.api.logging.Logger;`
- Line 22: `import org.gradle.api.logging.Logging;`
- Line 23: `import org.gradle.api.model.ObjectFactory;`
- Line 24: `import org.gradle.api.provider.Property;`
- Line 25: `import org.gradle.api.provider.Provider;`
- Line 26: `import org.gradle.api.specs.Spec;`
- Line 27: `import org.gradle.api.tasks.CacheableTask;`
- Line 28: `import org.gradle.api.tasks.Input;`
- Line 29: `import org.gradle.api.tasks.InputDirectory;`
- Line 30: `import org.gradle.api.tasks.InputFiles;`
- Line 31: `import org.gradle.api.tasks.Optional;`
- Line 32: `import org.gradle.api.tasks.OutputDirectory;`
- Line 33: `import org.gradle.api.tasks.PathSensitive;`
- Line 34: `import org.gradle.api.tasks.PathSensitivity;`
- Line 35: `import org.gradle.api.tasks.TaskAction;`
- Line 37: `import java.io.File;`
- Line 38: `import java.util.ArrayList;`
- Line 39: `import java.util.Arrays;`
- Line 40: `import java.util.HashMap;`
- Line 41: `import java.util.HashSet;`
- Line 42: `import java.util.LinkedHashMap;`
- Line 43: `import java.util.LinkedHashSet;`
- Line 44: `import java.util.List;`
- Line 45: `import java.util.Map;`
- Line 46: `import java.util.Set;`
- Line 47: `import java.util.regex.Matcher;`
- Line 48: `import java.util.regex.Pattern;`
- Line 50: `import javax.inject.Inject;`
- Line 52: `import static org.elasticsearch.gradle.internal.util.DependenciesUtils.createFileCollectionFromNonTransitiveArtifactsView;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/FilePermissionsPrecommitPlugin.java

### Concurrency Issue (1)
- Line 25: `public static final String FILEPERMISSIONS_TASK_NAME = "filepermissions";`

### Unused Code (9)
- Line 26: `private ProviderFactory providerFactory;`
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import java.util.stream.Collectors;`
- Line 21: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/FilePermissionsTask.java

### Concurrency Issue (1)
- Line 51: `private final PatternFilterable filesFilter = new PatternSet()`

### Exception Handling (2)
- Line 74: `throw new IllegalStateException("unable to read the file " + file + " attributes", e);`
- Line 96: `throw new StopExecutionException();`

### Unused Code (28)
- Line 57: `private File outputMarker = new File(getProject().getBuildDir(), "markers/filePermissions");`
- Line 11: `import org.elasticsearch.gradle.OS;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.FileTree;`
- Line 16: `import org.gradle.api.file.ProjectLayout;`
- Line 17: `import org.gradle.api.provider.ListProperty;`
- Line 18: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 19: `import org.gradle.api.tasks.InputFiles;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 21: `import org.gradle.api.tasks.OutputFile;`
- Line 22: `import org.gradle.api.tasks.PathSensitive;`
- Line 23: `import org.gradle.api.tasks.PathSensitivity;`
- Line 24: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 25: `import org.gradle.api.tasks.StopExecutionException;`
- Line 26: `import org.gradle.api.tasks.TaskAction;`
- Line 27: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 28: `import org.gradle.api.tasks.util.PatternSet;`
- Line 30: `import java.io.File;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.nio.file.Files;`
- Line 33: `import java.nio.file.attribute.PosixFileAttributeView;`
- Line 34: `import java.nio.file.attribute.PosixFilePermission;`
- Line 35: `import java.util.List;`
- Line 36: `import java.util.Set;`
- Line 37: `import java.util.stream.Collectors;`
- Line 39: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ForbiddenApisPrecommitPlugin.java

### Unused Code (13)
- Line 12: `import org.elasticsearch.gradle.internal.ExportElasticsearchBuildResourcesTask;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.Task;`
- Line 17: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 18: `import org.gradle.api.specs.Specs;`
- Line 19: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`
- Line 22: `import java.io.File;`
- Line 23: `import java.util.Set;`
- Line 25: `import static de.thetaphi.forbiddenapis.gradle.ForbiddenApisPlugin.FORBIDDEN_APIS_TASK_NAME;`
- Line 26: `import static org.elasticsearch.gradle.internal.precommit.CheckForbiddenApisTask.BUNDLED_SIGNATURE_DEFAULTS;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ForbiddenPatternsPrecommitPlugin.java

### Concurrency Issue (1)
- Line 25: `public static final String FORBIDDEN_PATTERNS_TASK_NAME = "forbiddenPatterns";`

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.provider.ProviderFactory;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import java.util.stream.Collectors;`
- Line 21: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ForbiddenPatternsTask.java

### Exception Handling (3)
- Line 116: `throw new IllegalArgumentException("Failed to read " + f + " as UTF_8", e);`
- Line 158: `throw new InvalidUserDataException("Missing [name] for invalid pattern rule");`
- Line 162: `throw new InvalidUserDataException("Missing [pattern] for invalid pattern rule");`

### Unused Code (38)
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.InvalidUserDataException;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.FileTree;`
- Line 16: `import org.gradle.api.file.ProjectLayout;`
- Line 17: `import org.gradle.api.provider.ListProperty;`
- Line 18: `import org.gradle.api.provider.Property;`
- Line 19: `import org.gradle.api.provider.Provider;`
- Line 20: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 22: `import org.gradle.api.tasks.InputFiles;`
- Line 23: `import org.gradle.api.tasks.Internal;`
- Line 24: `import org.gradle.api.tasks.Optional;`
- Line 25: `import org.gradle.api.tasks.OutputFile;`
- Line 26: `import org.gradle.api.tasks.PathSensitive;`
- Line 27: `import org.gradle.api.tasks.PathSensitivity;`
- Line 28: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 29: `import org.gradle.api.tasks.TaskAction;`
- Line 30: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 31: `import org.gradle.api.tasks.util.PatternSet;`
- Line 33: `import java.io.File;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.io.UncheckedIOException;`
- Line 36: `import java.net.URI;`
- Line 37: `import java.nio.charset.StandardCharsets;`
- Line 38: `import java.nio.file.Files;`
- Line 39: `import java.util.AbstractMap;`
- Line 40: `import java.util.ArrayList;`
- Line 41: `import java.util.Collections;`
- Line 42: `import java.util.HashMap;`
- Line 43: `import java.util.List;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.regex.Pattern;`
- Line 46: `import java.util.stream.Collectors;`
- Line 47: `import java.util.stream.IntStream;`
- Line 48: `import java.util.stream.Stream;`
- Line 50: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/InternalPrecommitTasks.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.LicenseHeadersPrecommitPlugin;`
- Line 13: `import org.gradle.api.Project;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/JarHellPrecommitPlugin.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.jarhell.JarHellPlugin;`
- Line 14: `import org.elasticsearch.gradle.jarhell.JarHellTask;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.Task;`
- Line 17: `import org.gradle.api.tasks.TaskProvider;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/JavaModulePrecommitPlugin.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.plugins.JavaPlugin;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/JavaModulePrecommitTask.java

### Concurrency Issue (4)
- Line 64: `public void setClassesDirs(FileCollection classesDirs) {`
- Line 74: `public void setResourcesDirs(File resourcesDirs) {`
- Line 92: `public void setClasspath(FileCollection classpath) {`
- Line 44: `private static final String expectedVersion = VersionProperties.getElasticsearch();`

### Exception Handling (1)
- Line 151: `throw new UncheckedIOException(e);`

### Unused Code (29)
- Line 48: `private FileCollection classesDirs;`
- Line 50: `private FileCollection classpath;`
- Line 52: `private File resourcesDir;`
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTask;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.model.ObjectFactory;`
- Line 17: `import org.gradle.api.provider.SetProperty;`
- Line 18: `import org.gradle.api.tasks.Classpath;`
- Line 19: `import org.gradle.api.tasks.InputFiles;`
- Line 20: `import org.gradle.api.tasks.PathSensitive;`
- Line 21: `import org.gradle.api.tasks.PathSensitivity;`
- Line 22: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 23: `import org.gradle.api.tasks.TaskAction;`
- Line 25: `import java.io.File;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.UncheckedIOException;`
- Line 28: `import java.lang.module.ModuleDescriptor;`
- Line 29: `import java.lang.module.ModuleFinder;`
- Line 30: `import java.lang.module.ModuleReference;`
- Line 31: `import java.nio.file.Files;`
- Line 32: `import java.nio.file.Path;`
- Line 33: `import java.util.Comparator;`
- Line 34: `import java.util.Locale;`
- Line 35: `import java.util.Objects;`
- Line 36: `import java.util.Set;`
- Line 38: `import javax.inject.Inject;`
- Line 40: `import static java.util.stream.Collectors.toSet;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/LicenseAnalyzer.java

### Exception Handling (2)
- Line 155: `throw new IllegalStateException("Unknown license for license file: " + licenseFile);`
- Line 167: `throw new UncheckedIOException(e);`

### Unused Code (5)
- Line 12: `import java.io.File;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.UncheckedIOException;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/LoggerUsagePrecommitPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.artifacts.Configuration;`
- Line 16: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/LoggerUsageTask.java

### Concurrency Issue (1)
- Line 72: `public void setClasspath(FileCollection classpath) {`

### Unused Code (23)
- Line 42: `private FileCollection classpath;`
- Line 46: `private ObjectFactory objectFactory;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTask;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.model.ObjectFactory;`
- Line 17: `import org.gradle.api.provider.ListProperty;`
- Line 18: `import org.gradle.api.tasks.CacheableTask;`
- Line 19: `import org.gradle.api.tasks.Classpath;`
- Line 20: `import org.gradle.api.tasks.InputFiles;`
- Line 21: `import org.gradle.api.tasks.PathSensitive;`
- Line 22: `import org.gradle.api.tasks.PathSensitivity;`
- Line 23: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 24: `import org.gradle.api.tasks.SourceSet;`
- Line 25: `import org.gradle.api.tasks.TaskAction;`
- Line 26: `import org.gradle.process.ExecOperations;`
- Line 27: `import org.gradle.workers.WorkAction;`
- Line 28: `import org.gradle.workers.WorkParameters;`
- Line 29: `import org.gradle.workers.WorkQueue;`
- Line 30: `import org.gradle.workers.WorkerExecutor;`
- Line 32: `import java.io.File;`
- Line 34: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/SplitPackagesAuditPrecommitPlugin.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.Task;`
- Line 16: `import org.gradle.api.plugins.JavaPlugin;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 20: `import java.io.File;`
- Line 21: `import java.util.HashMap;`
- Line 22: `import java.util.Map;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/SplitPackagesAuditTask.java

### Concurrency Issue (3)
- Line 99: `public void setClasspath(FileCollection classpath) {`
- Line 129: `public void setProjectBuildDirs(Map<File, String> projectBuildDirs) {`
- Line 64: `private static final Logger LOGGER = Logging.getLogger(SplitPackagesAuditTask.class);`

### Exception Handling (7)
- Line 165: `throw new GradleException(`
- Line 174: `throw new RuntimeException("Failed to create marker file", e);`
- Line 220: `throw new UncheckedIOException(e);`
- Line 271: `throw new GradleException("Unnecessary split package ignores found");`
- Line 290: `throw new GradleException("Unsupported classpath element: " + classpathElement);`
- Line 293: `throw new UncheckedIOException(e);`
- Line 327: `throw new IllegalStateException("Build directory unknown to gradle: " + dependencyFile);`

### Unused Code (43)
- Line 67: `private FileCollection classpath;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.file.ProjectLayout;`
- Line 17: `import org.gradle.api.file.RegularFileProperty;`
- Line 18: `import org.gradle.api.logging.Logger;`
- Line 19: `import org.gradle.api.logging.Logging;`
- Line 20: `import org.gradle.api.model.ObjectFactory;`
- Line 21: `import org.gradle.api.provider.MapProperty;`
- Line 22: `import org.gradle.api.provider.Property;`
- Line 23: `import org.gradle.api.provider.SetProperty;`
- Line 24: `import org.gradle.api.tasks.CacheableTask;`
- Line 25: `import org.gradle.api.tasks.CompileClasspath;`
- Line 26: `import org.gradle.api.tasks.Input;`
- Line 27: `import org.gradle.api.tasks.InputFiles;`
- Line 28: `import org.gradle.api.tasks.OutputFile;`
- Line 29: `import org.gradle.api.tasks.PathSensitive;`
- Line 30: `import org.gradle.api.tasks.PathSensitivity;`
- Line 31: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 32: `import org.gradle.api.tasks.TaskAction;`
- Line 33: `import org.gradle.workers.WorkAction;`
- Line 34: `import org.gradle.workers.WorkParameters;`
- Line 35: `import org.gradle.workers.WorkerExecutor;`
- Line 37: `import java.io.File;`
- Line 38: `import java.io.IOException;`
- Line 39: `import java.io.UncheckedIOException;`
- Line 40: `import java.nio.file.FileSystem;`
- Line 41: `import java.nio.file.FileSystems;`
- Line 42: `import java.nio.file.Files;`
- Line 43: `import java.nio.file.Path;`
- Line 44: `import java.nio.file.StandardOpenOption;`
- Line 45: `import java.util.ArrayList;`
- Line 46: `import java.util.HashMap;`
- Line 47: `import java.util.HashSet;`
- Line 48: `import java.util.List;`
- Line 49: `import java.util.Map;`
- Line 50: `import java.util.Set;`
- Line 51: `import java.util.TreeSet;`
- Line 52: `import java.util.function.Consumer;`
- Line 54: `import javax.inject.Inject;`
- Line 56: `import static org.elasticsearch.gradle.util.GradleUtils.projectPath;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/TestingConventionsCheckTask.java

### Null Pointer (1)
- Line 159: `return testClassCandidates.stream()`

### Concurrency Issue (2)
- Line 93: `private static final String JUNIT3_TEST_METHOD_PREFIX = "test";`
- Line 226: `private static final String CLASS_POSTFIX = ".class";`

### Exception Handling (1)
- Line 220: `throw new RuntimeException("Failed to load class " + name + ". Incorrect classpath?", e);`

### Unused Code (31)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTask;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.EmptyFileVisitor;`
- Line 16: `import org.gradle.api.file.FileTree;`
- Line 17: `import org.gradle.api.file.FileVisitDetails;`
- Line 18: `import org.gradle.api.logging.Logging;`
- Line 19: `import org.gradle.api.provider.ListProperty;`
- Line 20: `import org.gradle.api.tasks.CacheableTask;`
- Line 21: `import org.gradle.api.tasks.Classpath;`
- Line 22: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 23: `import org.gradle.api.tasks.Input;`
- Line 24: `import org.gradle.api.tasks.InputFiles;`
- Line 25: `import org.gradle.api.tasks.Internal;`
- Line 26: `import org.gradle.api.tasks.PathSensitive;`
- Line 27: `import org.gradle.api.tasks.PathSensitivity;`
- Line 28: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 29: `import org.gradle.api.tasks.TaskAction;`
- Line 30: `import org.gradle.workers.WorkAction;`
- Line 31: `import org.gradle.workers.WorkParameters;`
- Line 32: `import org.gradle.workers.WorkQueue;`
- Line 33: `import org.gradle.workers.WorkerExecutor;`
- Line 35: `import java.lang.reflect.Method;`
- Line 36: `import java.lang.reflect.Modifier;`
- Line 37: `import java.util.ArrayList;`
- Line 38: `import java.util.Arrays;`
- Line 39: `import java.util.List;`
- Line 40: `import java.util.function.Predicate;`
- Line 41: `import java.util.stream.Collectors;`
- Line 42: `import java.util.stream.Stream;`
- Line 44: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/TestingConventionsPrecommitPlugin.java

### Unused Code (15)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.test.InternalClusterTestPlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.InternalJavaRestTestPlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.LegacyJavaRestTestPlugin;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.LegacyYamlRestTestPlugin;`
- Line 17: `import org.gradle.api.Action;`
- Line 18: `import org.gradle.api.NamedDomainObjectProvider;`
- Line 19: `import org.gradle.api.Project;`
- Line 20: `import org.gradle.api.Task;`
- Line 21: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 22: `import org.gradle.api.plugins.JavaPlugin;`
- Line 23: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 24: `import org.gradle.api.tasks.SourceSet;`
- Line 25: `import org.gradle.api.tasks.TaskProvider;`
- Line 27: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ThirdPartyAuditPrecommitPlugin.java

### Concurrency Issue (1)
- Line 31: `public static final String JDK_JAR_HELL_CONFIG_NAME = "jdkJarHell";`

### Unused Code (14)
- Line 12: `import org.elasticsearch.gradle.dependencies.CompileOnlyResolvePlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.ExportElasticsearchBuildResourcesTask;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitPlugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.Task;`
- Line 17: `import org.gradle.api.artifacts.Configuration;`
- Line 18: `import org.gradle.api.artifacts.component.ModuleComponentIdentifier;`
- Line 19: `import org.gradle.api.file.FileCollection;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`
- Line 22: `import java.io.File;`
- Line 23: `import java.nio.file.Path;`
- Line 25: `import static org.elasticsearch.gradle.internal.util.DependenciesUtils.createFileCollectionFromNonTransitiveArtifactsView;`
- Line 26: `import static org.elasticsearch.gradle.internal.util.DependenciesUtils.thirdPartyDependenciesView;`
- Line 27: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ThirdPartyAuditTask.java

### Concurrency Issue (5)
- Line 130: `public void setSignatureFile(File signatureFile) {`
- Line 68: `private static final Pattern MISSING_CLASS_PATTERN = Pattern.compile("DEBUG: Class '(.*)' cannot be loaded \\(.*\\)\\.");`
- Line 70: `private static final Pattern VIOLATION_PATTERN = Pattern.compile("\\s\\sin ([a-zA-Z0-9$.]+) \\(.*\\)");`
- Line 71: `private static final int SIG_KILL_EXIT_VALUE = 137;`
- Line 77: `private static final String JDK_JAR_HELL_MAIN_CLASS = "org.elasticsearch.jdk.JdkJarHellCheck";`

### Exception Handling (5)
- Line 227: `throw new IllegalStateException(`
- Line 254: `throw new IllegalStateException("Audit of third party dependencies failed");`
- Line 330: `throw new IllegalStateException("Third party audit task is not configured correctly");`
- Line 363: `throw new IllegalStateException("Third party audit was killed buy SIGKILL, could be a victim of the Linux OOM killer");`
- Line 370: `throw new IllegalStateException("Forbidden APIs cli failed: " + forbiddenApisOutput);`

### Unused Code (50)
- Line 85: `private File signatureFile;`
- Line 11: `import de.thetaphi.forbiddenapis.cli.CliMain;`
- Line 13: `import org.apache.commons.io.output.NullOutputStream;`
- Line 14: `import org.elasticsearch.gradle.OS;`
- Line 15: `import org.elasticsearch.gradle.VersionProperties;`
- Line 16: `import org.gradle.api.DefaultTask;`
- Line 17: `import org.gradle.api.JavaVersion;`
- Line 18: `import org.gradle.api.file.ArchiveOperations;`
- Line 19: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 20: `import org.gradle.api.file.FileSystemOperations;`
- Line 21: `import org.gradle.api.file.FileTree;`
- Line 22: `import org.gradle.api.file.ProjectLayout;`
- Line 23: `import org.gradle.api.model.ObjectFactory;`
- Line 24: `import org.gradle.api.provider.Property;`
- Line 25: `import org.gradle.api.tasks.CacheableTask;`
- Line 26: `import org.gradle.api.tasks.Classpath;`
- Line 27: `import org.gradle.api.tasks.CompileClasspath;`
- Line 28: `import org.gradle.api.tasks.Input;`
- Line 29: `import org.gradle.api.tasks.InputFile;`
- Line 30: `import org.gradle.api.tasks.InputFiles;`
- Line 31: `import org.gradle.api.tasks.Internal;`
- Line 32: `import org.gradle.api.tasks.Optional;`
- Line 33: `import org.gradle.api.tasks.OutputFile;`
- Line 34: `import org.gradle.api.tasks.PathSensitive;`
- Line 35: `import org.gradle.api.tasks.PathSensitivity;`
- Line 36: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 37: `import org.gradle.api.tasks.TaskAction;`
- Line 38: `import org.gradle.process.ExecOperations;`
- Line 39: `import org.gradle.process.ExecResult;`
- Line 41: `import java.io.ByteArrayOutputStream;`
- Line 42: `import java.io.File;`
- Line 43: `import java.io.IOException;`
- Line 44: `import java.nio.charset.StandardCharsets;`
- Line 45: `import java.nio.file.Files;`
- Line 46: `import java.util.Arrays;`
- Line 47: `import java.util.Collections;`
- Line 48: `import java.util.List;`
- Line 49: `import java.util.Set;`
- Line 50: `import java.util.TreeSet;`
- Line 51: `import java.util.regex.Matcher;`
- Line 52: `import java.util.regex.Pattern;`
- Line 53: `import java.util.stream.Collectors;`
- Line 54: `import java.util.stream.IntStream;`
- Line 55: `import java.util.stream.Stream;`
- Line 57: `import javax.inject.Inject;`
- Line 59: `import static org.gradle.api.JavaVersion.VERSION_20;`
- Line 60: `import static org.gradle.api.JavaVersion.VERSION_21;`
- Line 61: `import static org.gradle.api.JavaVersion.VERSION_22;`
- Line 62: `import static org.gradle.api.JavaVersion.VERSION_23;`
- Line 63: `import static org.gradle.api.JavaVersion.VERSION_24;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ValidateJsonAgainstSchemaTask.java

### Concurrency Issue (3)
- Line 59: `public void setInputFiles(FileCollection inputFiles) {`
- Line 68: `public void setJsonSchema(File jsonSchema) {`
- Line 72: `public void setReport(File report) {`

### Exception Handling (1)
- Line 110: `throw new UncheckedIOException(e);`

### Unused Code (33)
- Line 49: `private File jsonSchema;`
- Line 50: `private File report;`
- Line 51: `private FileCollection inputFiles;`
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.networknt.schema.JsonSchema;`
- Line 14: `import com.networknt.schema.JsonSchemaException;`
- Line 15: `import com.networknt.schema.JsonSchemaFactory;`
- Line 16: `import com.networknt.schema.SchemaValidatorsConfig;`
- Line 17: `import com.networknt.schema.SpecVersion;`
- Line 18: `import com.networknt.schema.ValidationMessage;`
- Line 20: `import org.gradle.api.DefaultTask;`
- Line 21: `import org.gradle.api.UncheckedIOException;`
- Line 22: `import org.gradle.api.file.FileCollection;`
- Line 23: `import org.gradle.api.tasks.InputFile;`
- Line 24: `import org.gradle.api.tasks.InputFiles;`
- Line 25: `import org.gradle.api.tasks.Internal;`
- Line 26: `import org.gradle.api.tasks.OutputFile;`
- Line 27: `import org.gradle.api.tasks.TaskAction;`
- Line 28: `import org.gradle.work.ChangeType;`
- Line 29: `import org.gradle.work.FileChange;`
- Line 30: `import org.gradle.work.Incremental;`
- Line 31: `import org.gradle.work.InputChanges;`
- Line 33: `import java.io.File;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.io.PrintWriter;`
- Line 36: `import java.nio.file.Files;`
- Line 37: `import java.nio.file.StandardOpenOption;`
- Line 38: `import java.util.Collection;`
- Line 39: `import java.util.LinkedHashMap;`
- Line 40: `import java.util.LinkedHashSet;`
- Line 41: `import java.util.Map;`
- Line 42: `import java.util.Set;`
- Line 43: `import java.util.stream.StreamSupport;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ValidateJsonNoKeywordsTask.java

### Concurrency Issue (3)
- Line 61: `public void setInputFiles(FileCollection inputFiles) {`
- Line 70: `public void setJsonKeywords(File jsonKeywords) {`
- Line 74: `public void setReport(File report) {`

### Exception Handling (2)
- Line 157: `throw new GradleException("Failed to write keywords report", e);`
- Line 167: `throw new GradleException(message);`

### Unused Code (28)
- Line 51: `private File jsonKeywords;`
- Line 52: `private File report;`
- Line 53: `private FileCollection inputFiles;`
- Line 12: `import com.fasterxml.jackson.core.JsonParser;`
- Line 13: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 14: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 17: `import org.gradle.api.DefaultTask;`
- Line 18: `import org.gradle.api.GradleException;`
- Line 19: `import org.gradle.api.file.FileCollection;`
- Line 20: `import org.gradle.api.tasks.InputFile;`
- Line 21: `import org.gradle.api.tasks.InputFiles;`
- Line 22: `import org.gradle.api.tasks.OutputFile;`
- Line 23: `import org.gradle.api.tasks.TaskAction;`
- Line 24: `import org.gradle.work.ChangeType;`
- Line 25: `import org.gradle.work.Incremental;`
- Line 26: `import org.gradle.work.InputChanges;`
- Line 28: `import java.io.File;`
- Line 29: `import java.io.FileNotFoundException;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.io.PrintWriter;`
- Line 32: `import java.util.HashMap;`
- Line 33: `import java.util.HashSet;`
- Line 34: `import java.util.LinkedHashMap;`
- Line 35: `import java.util.Locale;`
- Line 36: `import java.util.Map;`
- Line 37: `import java.util.Set;`
- Line 38: `import java.util.stream.StreamSupport;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ValidateRestSpecPlugin.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.provider.Provider;`
- Line 17: `import java.io.File;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/precommit/ValidateYamlAgainstSchemaTask.java

### Unused Code (2)
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/AbstractVersionsTask.java

### Exception Handling (2)
- Line 139: `if (split.length != 2) throw new IllegalArgumentException("Invalid tag format [" + l + "]");`
- Line 162: `throw new IllegalArgumentException("CompilationUnit has no lexical information for output");`

### Unused Code (36)
- Line 12: `import com.github.javaparser.GeneratedJavaParserConstants;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 14: `import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;`
- Line 15: `import com.github.javaparser.ast.body.FieldDeclaration;`
- Line 16: `import com.github.javaparser.ast.expr.IntegerLiteralExpr;`
- Line 17: `import com.github.javaparser.ast.observer.ObservableProperty;`
- Line 18: `import com.github.javaparser.printer.ConcreteSyntaxModel;`
- Line 19: `import com.github.javaparser.printer.concretesyntaxmodel.CsmElement;`
- Line 20: `import com.github.javaparser.printer.lexicalpreservation.LexicalPreservingPrinter;`
- Line 22: `import org.gradle.api.DefaultTask;`
- Line 23: `import org.gradle.api.logging.Logger;`
- Line 24: `import org.gradle.api.logging.Logging;`
- Line 25: `import org.gradle.initialization.layout.BuildLayout;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.lang.reflect.Field;`
- Line 29: `import java.nio.file.Files;`
- Line 30: `import java.nio.file.Path;`
- Line 31: `import java.nio.file.StandardOpenOption;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.Map;`
- Line 34: `import java.util.OptionalInt;`
- Line 35: `import java.util.stream.Collectors;`
- Line 37: `import static com.github.javaparser.ast.observer.ObservableProperty.TYPE_PARAMETERS;`
- Line 38: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmConditional.Condition.FLAG;`
- Line 39: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.block;`
- Line 40: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.child;`
- Line 41: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.comma;`
- Line 42: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.comment;`
- Line 43: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.conditional;`
- Line 44: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.list;`
- Line 45: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.newline;`
- Line 46: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.none;`
- Line 47: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.sequence;`
- Line 48: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.space;`
- Line 49: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.string;`
- Line 50: `import static com.github.javaparser.printer.concretesyntaxmodel.CsmElement.token;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/BreakingChangesGenerator.java

### Unused Code (14)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 16: `import java.io.File;`
- Line 17: `import java.io.FileWriter;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.Objects;`
- Line 24: `import java.util.TreeMap;`
- Line 26: `import static java.util.Comparator.comparing;`
- Line 27: `import static java.util.stream.Collectors.groupingBy;`
- Line 28: `import static java.util.stream.Collectors.toList;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ChangelogEntry.java

### Concurrency Issue (18)
- Line 66: `public void setPr(Integer pr) {`
- Line 74: `public void setIssues(List<Integer> issues) {`
- Line 82: `public void setArea(String area) {`
- Line 90: `public void setType(String type) {`
- Line 98: `public void setSummary(String summary) {`
- Line 106: `public void setHighlight(Highlight highlight) {`
- Line 115: `public void setBreaking(Breaking breaking) {`
- Line 123: `public void setDeprecation(Deprecation deprecation) {`
- Line 176: `public void setNotable(boolean notable) {`
- Line 184: `public void setTitle(String title) {`
- Line 192: `public void setBody(String body) {`
- Line 245: `public void setArea(String area) {`
- Line 253: `public void setTitle(String title) {`
- Line 261: `public void setDetails(String details) {`
- Line 269: `public void setImpact(String impact) {`
- Line 277: `public void setNotable(boolean notable) {`
- Line 289: `public void setEssSettingChange(boolean essSettingChange) {`
- Line 35: `private static final Logger LOGGER = Logging.getLogger(GenerateReleaseNotesTask.class);`

### Exception Handling (1)
- Line 58: `throw new UncheckedIOException(e);`

### Unused Code (29)
- Line 37: `private Integer pr;`
- Line 39: `private String area;`
- Line 40: `private String type;`
- Line 41: `private String summary;`
- Line 42: `private Highlight highlight;`
- Line 43: `private Breaking breaking;`
- Line 44: `private Deprecation deprecation;`
- Line 167: `private boolean notable;`
- Line 168: `private String title;`
- Line 169: `private String body;`
- Line 170: `private Integer pr;`
- Line 234: `private String area;`
- Line 235: `private String title;`
- Line 236: `private String details;`
- Line 237: `private String impact;`
- Line 238: `private boolean notable;`
- Line 239: `private boolean essSettingChange;`
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 15: `import org.gradle.api.logging.Logger;`
- Line 16: `import org.gradle.api.logging.Logging;`
- Line 18: `import java.io.File;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.io.UncheckedIOException;`
- Line 21: `import java.util.Arrays;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Locale;`
- Line 24: `import java.util.Objects;`
- Line 25: `import java.util.stream.Collectors;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ExtractCurrentVersionsTask.java

### Concurrency Issue (2)
- Line 43: `public void outputFile(String file) {`
- Line 33: `private static final Logger LOGGER = Logging.getLogger(ExtractCurrentVersionsTask.class);`

### Exception Handling (2)
- Line 50: `throw new IllegalArgumentException("Output file not specified");`
- Line 93: `throw new IllegalArgumentException("No version ids found in " + javaVersionsFile);`

### Unused Code (18)
- Line 35: `private Path outputFile;`
- Line 69: `private Integer highestVersionId;`
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 14: `import com.github.javaparser.ast.body.FieldDeclaration;`
- Line 16: `import org.gradle.api.logging.Logger;`
- Line 17: `import org.gradle.api.logging.Logging;`
- Line 18: `import org.gradle.api.tasks.TaskAction;`
- Line 19: `import org.gradle.api.tasks.options.Option;`
- Line 20: `import org.gradle.initialization.layout.BuildLayout;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.nio.file.StandardOpenOption;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.function.Consumer;`
- Line 30: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/GenerateReleaseNotesTask.java

### Concurrency Issue (1)
- Line 52: `private static final Logger LOGGER = Logging.getLogger(GenerateReleaseNotesTask.class);`

### Exception Handling (1)
- Line 228: `throw new GradleException("Failed to find git tags prior to [v" + currentVersion + "]");`

### Unused Code (31)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 15: `import org.gradle.api.DefaultTask;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 18: `import org.gradle.api.file.FileCollection;`
- Line 19: `import org.gradle.api.file.RegularFile;`
- Line 20: `import org.gradle.api.file.RegularFileProperty;`
- Line 21: `import org.gradle.api.logging.Logger;`
- Line 22: `import org.gradle.api.logging.Logging;`
- Line 23: `import org.gradle.api.model.ObjectFactory;`
- Line 24: `import org.gradle.api.tasks.InputFile;`
- Line 25: `import org.gradle.api.tasks.InputFiles;`
- Line 26: `import org.gradle.api.tasks.OutputFile;`
- Line 27: `import org.gradle.api.tasks.TaskAction;`
- Line 28: `import org.gradle.process.ExecOperations;`
- Line 30: `import java.io.File;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.nio.file.Path;`
- Line 33: `import java.util.ArrayList;`
- Line 34: `import java.util.HashMap;`
- Line 35: `import java.util.HashSet;`
- Line 36: `import java.util.Iterator;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Locale;`
- Line 39: `import java.util.Map;`
- Line 40: `import java.util.Set;`
- Line 41: `import java.util.stream.Stream;`
- Line 43: `import javax.inject.Inject;`
- Line 45: `import static java.util.Comparator.naturalOrder;`
- Line 46: `import static java.util.stream.Collectors.toSet;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/GitWrapper.java

### Unused Code (7)
- Line 12: `import org.gradle.process.ExecOperations;`
- Line 14: `import java.io.ByteArrayOutputStream;`
- Line 15: `import java.nio.charset.StandardCharsets;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.Objects;`
- Line 18: `import java.util.stream.Collectors;`
- Line 19: `import java.util.stream.Stream;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/MigrationIndexGenerator.java

### Unused Code (12)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.FileWriter;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.util.HashMap;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.TreeSet;`
- Line 23: `import java.util.stream.Collectors;`
- Line 25: `import static java.util.Comparator.reverseOrder;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/MinorVersion.java

### Unused Code (2)
- Line 12: `import java.util.Comparator;`
- Line 13: `import java.util.Objects;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/PruneChangelogsTask.java

### Concurrency Issue (2)
- Line 62: `public void setChangelogs(FileCollection files) {`
- Line 44: `private static final Logger LOGGER = Logging.getLogger(PruneChangelogsTask.class);`

### Unused Code (20)
- Line 46: `private FileCollection changelogs;`
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 15: `import org.gradle.api.DefaultTask;`
- Line 16: `import org.gradle.api.GradleException;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.file.FileCollection;`
- Line 19: `import org.gradle.api.logging.Logger;`
- Line 20: `import org.gradle.api.logging.Logging;`
- Line 21: `import org.gradle.api.model.ObjectFactory;`
- Line 22: `import org.gradle.api.tasks.Internal;`
- Line 23: `import org.gradle.api.tasks.TaskAction;`
- Line 24: `import org.gradle.process.ExecOperations;`
- Line 26: `import java.io.File;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.TreeSet;`
- Line 30: `import java.util.stream.Collectors;`
- Line 31: `import java.util.stream.Stream;`
- Line 33: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/QualifiedVersion.java

### Exception Handling (2)
- Line 43: `throw new IllegalArgumentException("Invalid version format: '" + s + "'. Should be " + pattern);`
- Line 109: `throw new IllegalArgumentException("Invalid qualifier [" + qualifier + "] passed");`

### Unused Code (6)
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 14: `import java.util.Comparator;`
- Line 15: `import java.util.Locale;`
- Line 16: `import java.util.Objects;`
- Line 17: `import java.util.regex.Matcher;`
- Line 18: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ReleaseHighlightsGenerator.java

### Unused Code (13)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 16: `import java.io.File;`
- Line 17: `import java.io.FileWriter;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.Comparator;`
- Line 22: `import java.util.HashMap;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Objects;`
- Line 26: `import java.util.stream.Collectors;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ReleaseNotesGenerator.java

### Unused Code (13)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.FileWriter;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.util.HashMap;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.TreeMap;`
- Line 24: `import static java.util.Comparator.comparing;`
- Line 25: `import static java.util.stream.Collectors.groupingBy;`
- Line 26: `import static java.util.stream.Collectors.toList;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ReleaseNotesIndexGenerator.java

### Unused Code (12)
- Line 12: `import com.google.common.annotations.VisibleForTesting;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.FileWriter;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.util.HashMap;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.TreeSet;`
- Line 23: `import java.util.stream.Collectors;`
- Line 25: `import static java.util.Comparator.reverseOrder;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/ReleaseToolsPlugin.java

### Concurrency Issue (1)
- Line 35: `private static final String RESOURCES = "build-tools-internal/src/main/resources/";`

### Unused Code (15)
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.elasticsearch.gradle.VersionProperties;`
- Line 14: `import org.elasticsearch.gradle.internal.conventions.precommit.PrecommitTaskPlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.precommit.ValidateYamlAgainstSchemaTask;`
- Line 16: `import org.gradle.api.Action;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 19: `import org.gradle.api.file.Directory;`
- Line 20: `import org.gradle.api.file.FileTree;`
- Line 21: `import org.gradle.api.file.ProjectLayout;`
- Line 22: `import org.gradle.api.provider.Provider;`
- Line 23: `import org.gradle.api.tasks.util.PatternSet;`
- Line 25: `import java.io.File;`
- Line 26: `import java.util.function.Function;`
- Line 28: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/SetCompatibleVersionsTask.java

### Concurrency Issue (1)
- Line 47: `public void versionIds(List<String> version) {`

### Exception Handling (2)
- Line 59: `throw new IllegalArgumentException("No version ids specified");`
- Line 69: `throw new IllegalArgumentException("TransportVersion id not specified");`

### Unused Code (17)
- Line 33: `private Version thisVersion;`
- Line 34: `private Version releaseVersion;`
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 14: `import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;`
- Line 15: `import com.github.javaparser.ast.expr.NameExpr;`
- Line 16: `import com.github.javaparser.printer.lexicalpreservation.LexicalPreservingPrinter;`
- Line 18: `import org.elasticsearch.gradle.Version;`
- Line 19: `import org.gradle.api.tasks.TaskAction;`
- Line 20: `import org.gradle.api.tasks.options.Option;`
- Line 21: `import org.gradle.initialization.layout.BuildLayout;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.Optional;`
- Line 29: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/TagVersionsTask.java

### Concurrency Issue (2)
- Line 50: `public void tagVersions(List<String> version) {`
- Line 33: `private static final Logger LOGGER = Logging.getLogger(TagVersionsTask.class);`

### Exception Handling (2)
- Line 57: `throw new IllegalArgumentException("Release version not specified");`
- Line 60: `throw new IllegalArgumentException("No version tags specified");`

### Unused Code (18)
- Line 35: `private Version releaseVersion;`
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.gradle.api.logging.Logger;`
- Line 14: `import org.gradle.api.logging.Logging;`
- Line 15: `import org.gradle.api.tasks.TaskAction;`
- Line 16: `import org.gradle.api.tasks.options.Option;`
- Line 17: `import org.gradle.initialization.layout.BuildLayout;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.nio.file.StandardOpenOption;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Optional;`
- Line 26: `import java.util.regex.Matcher;`
- Line 27: `import java.util.regex.Pattern;`
- Line 28: `import java.util.stream.Collectors;`
- Line 30: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/TemplateUtils.java

### Exception Handling (1)
- Line 38: `throw new RuntimeException(e);`

### Unused Code (4)
- Line 12: `import groovy.text.SimpleTemplateEngine;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.io.StringWriter;`
- Line 16: `import java.util.Map;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/release/UpdateVersionsTask.java

### Concurrency Issue (4)
- Line 65: `public void addVersion(String version) {`
- Line 70: `public void addTransportVersion(String transportVersion) {`
- Line 75: `public void setCurrent(boolean setCurrent) {`
- Line 80: `public void removeVersion(String version) {`

### Exception Handling (6)
- Line 100: `throw new IllegalArgumentException("No versions to add or remove specified");`
- Line 103: `throw new IllegalArgumentException("No new version added to set as the current version");`
- Line 106: `throw new IllegalArgumentException("Same version specified to add and remove");`
- Line 109: `throw new IllegalArgumentException("Transport version specified must be in the format '<constant>:<version-id>'");`
- Line 163: `throw new IllegalArgumentException("Duplicate version constants " + v1);`
- Line 215: `throw new IllegalStateException("Duplicate version constant " + f1);`

### Unused Code (33)
- Line 52: `private Version addVersion;`
- Line 53: `private boolean setCurrent;`
- Line 55: `private Version removeVersion;`
- Line 57: `private String addTransportVersion;`
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 14: `import com.github.javaparser.ast.NodeList;`
- Line 15: `import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;`
- Line 16: `import com.github.javaparser.ast.body.FieldDeclaration;`
- Line 17: `import com.github.javaparser.ast.body.VariableDeclarator;`
- Line 18: `import com.github.javaparser.ast.expr.Expression;`
- Line 19: `import com.github.javaparser.ast.expr.NameExpr;`
- Line 20: `import com.github.javaparser.printer.lexicalpreservation.LexicalPreservingPrinter;`
- Line 21: `import com.google.common.annotations.VisibleForTesting;`
- Line 23: `import org.elasticsearch.gradle.Version;`
- Line 24: `import org.gradle.api.logging.Logger;`
- Line 25: `import org.gradle.api.logging.Logging;`
- Line 26: `import org.gradle.api.tasks.TaskAction;`
- Line 27: `import org.gradle.api.tasks.options.Option;`
- Line 28: `import org.gradle.initialization.layout.BuildLayout;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.nio.file.Path;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.NavigableMap;`
- Line 34: `import java.util.Objects;`
- Line 35: `import java.util.Optional;`
- Line 36: `import java.util.TreeMap;`
- Line 37: `import java.util.function.Function;`
- Line 38: `import java.util.regex.Matcher;`
- Line 39: `import java.util.regex.Pattern;`
- Line 40: `import java.util.stream.Collectors;`
- Line 42: `import javax.annotation.Nullable;`
- Line 43: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/shadow/XmlClassRelocationTransformer.java

### Concurrency Issue (2)
- Line 56: `public void transform(TransformerContext context) {`
- Line 38: `public class XmlClassRelocationTransformer implements Transformer {`

### Exception Handling (2)
- Line 130: `throw new RuntimeException(e);`
- Line 132: `throw new RuntimeException(e);`

### Unused Code (24)
- Line 42: `private Document doc;`
- Line 44: `private String resource;`
- Line 12: `import com.github.jengelman.gradle.plugins.shadow.ShadowStats;`
- Line 13: `import com.github.jengelman.gradle.plugins.shadow.relocation.RelocateClassContext;`
- Line 14: `import com.github.jengelman.gradle.plugins.shadow.relocation.Relocator;`
- Line 15: `import com.github.jengelman.gradle.plugins.shadow.transformers.Transformer;`
- Line 16: `import com.github.jengelman.gradle.plugins.shadow.transformers.TransformerContext;`
- Line 18: `import org.apache.commons.io.IOUtils;`
- Line 19: `import org.apache.tools.zip.ZipEntry;`
- Line 20: `import org.apache.tools.zip.ZipOutputStream;`
- Line 21: `import org.gradle.api.file.FileTreeElement;`
- Line 22: `import org.w3c.dom.Document;`
- Line 23: `import org.w3c.dom.Node;`
- Line 24: `import org.w3c.dom.NodeList;`
- Line 26: `import java.io.BufferedInputStream;`
- Line 27: `import java.io.ByteArrayOutputStream;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.util.List;`
- Line 31: `import javax.xml.parsers.DocumentBuilder;`
- Line 32: `import javax.xml.parsers.DocumentBuilderFactory;`
- Line 33: `import javax.xml.transform.TransformerException;`
- Line 34: `import javax.xml.transform.TransformerFactory;`
- Line 35: `import javax.xml.transform.dom.DOMSource;`
- Line 36: `import javax.xml.transform.stream.StreamResult;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/snyk/GenerateSnykDependencyGraph.java

### Exception Handling (1)
- Line 86: `throw new GradleException("Cannot generate dependencies json file", e);`

### Unused Code (19)
- Line 12: `import groovy.json.JsonOutput;`
- Line 14: `import org.gradle.api.DefaultTask;`
- Line 15: `import org.gradle.api.GradleException;`
- Line 16: `import org.gradle.api.artifacts.Configuration;`
- Line 17: `import org.gradle.api.artifacts.ResolvedDependency;`
- Line 18: `import org.gradle.api.file.RegularFileProperty;`
- Line 19: `import org.gradle.api.model.ObjectFactory;`
- Line 20: `import org.gradle.api.provider.Property;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 22: `import org.gradle.api.tasks.InputFiles;`
- Line 23: `import org.gradle.api.tasks.OutputFile;`
- Line 24: `import org.gradle.api.tasks.TaskAction;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.nio.file.Files;`
- Line 28: `import java.nio.file.StandardOpenOption;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Map;`
- Line 31: `import java.util.Set;`
- Line 33: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/snyk/SnykDependencyGraph.java

### Concurrency Issue (1)
- Line 19: `static private final String schemaVersion = "1.2.0";`

### Unused Code (7)
- Line 49: `private String nodeId;`
- Line 50: `private String pkgId;`
- Line 12: `import java.util.HashMap;`
- Line 13: `import java.util.LinkedHashSet;`
- Line 14: `import java.util.Map;`
- Line 15: `import java.util.Objects;`
- Line 16: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/snyk/SnykDependencyGraphBuilder.java

### Concurrency Issue (1)
- Line 48: `private void loadGraph(SnykDependencyNode parent, Set<ResolvedDependency> deps) {`

### Unused Code (6)
- Line 23: `private SnykDependencyNode currentNode;`
- Line 24: `private String gradleVersion;`
- Line 12: `import org.elasticsearch.gradle.internal.snyk.SnykDependencyGraph.SnykDependencyNode;`
- Line 13: `import org.gradle.api.artifacts.ResolvedDependency;`
- Line 15: `import java.util.LinkedHashSet;`
- Line 16: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/snyk/SnykDependencyMonitoringGradlePlugin.java

### Concurrency Issue (1)
- Line 29: `public static final String UPLOAD_TASK_NAME = "uploadSnykDependencyGraph";`

### Unused Code (14)
- Line 30: `private ProjectLayout projectLayout;`
- Line 31: `private ProviderFactory providerFactory;`
- Line 12: `import org.elasticsearch.gradle.internal.conventions.info.GitInfo;`
- Line 13: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.artifacts.Configuration;`
- Line 17: `import org.gradle.api.file.ProjectLayout;`
- Line 18: `import org.gradle.api.plugins.JavaPlugin;`
- Line 19: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 20: `import org.gradle.api.provider.ProviderFactory;`
- Line 21: `import org.gradle.api.tasks.SourceSet;`
- Line 23: `import javax.inject.Inject;`
- Line 25: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/snyk/UploadSnykDependenciesGraph.java

### Concurrency Issue (2)
- Line 37: `public static final String DEFAULT_SERVER = "https://snyk.io";`
- Line 43: `public static final String SNYK_DEP_GRAPH_API_ENDPOINT = "/api/v1/monitor/dep-graph";`

### Exception Handling (2)
- Line 72: `throw new GradleException("Uploading Snyk Graph failed with http code " + statusCode + ": " + responseString);`
- Line 76: `throw new GradleException("Failed to call API endpoint to submit updated dependency graph", e);`

### Unused Code (20)
- Line 12: `import org.apache.hc.client5.http.classic.methods.HttpPut;`
- Line 13: `import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;`
- Line 14: `import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;`
- Line 15: `import org.apache.hc.client5.http.impl.classic.HttpClients;`
- Line 16: `import org.apache.hc.core5.http.ContentType;`
- Line 17: `import org.apache.hc.core5.http.ParseException;`
- Line 18: `import org.apache.hc.core5.http.io.entity.EntityUtils;`
- Line 19: `import org.apache.hc.core5.http.io.entity.FileEntity;`
- Line 20: `import org.gradle.api.DefaultTask;`
- Line 21: `import org.gradle.api.GradleException;`
- Line 22: `import org.gradle.api.file.RegularFileProperty;`
- Line 23: `import org.gradle.api.model.ObjectFactory;`
- Line 24: `import org.gradle.api.provider.Property;`
- Line 25: `import org.gradle.api.tasks.Input;`
- Line 26: `import org.gradle.api.tasks.InputFile;`
- Line 27: `import org.gradle.api.tasks.Optional;`
- Line 28: `import org.gradle.api.tasks.TaskAction;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.net.HttpURLConnection;`
- Line 33: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/ClusterFeaturesMetadataPlugin.java

### Concurrency Issue (2)
- Line 27: `public static final String CLUSTER_FEATURES_JSON = "cluster-features.json";`
- Line 28: `public static final String FEATURES_METADATA_TYPE = "features-metadata-json";`

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.dependencies.CompileOnlyResolvePlugin;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.artifacts.Configuration;`
- Line 16: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import java.util.Map;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/ClusterFeaturesMetadataTask.java

### Concurrency Issue (1)
- Line 40: `public void setClasspath(FileCollection classpath) {`

### Unused Code (15)
- Line 30: `private FileCollection classpath;`
- Line 12: `import org.elasticsearch.gradle.LoggedExec;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.file.RegularFileProperty;`
- Line 17: `import org.gradle.api.tasks.CacheableTask;`
- Line 18: `import org.gradle.api.tasks.Classpath;`
- Line 19: `import org.gradle.api.tasks.OutputFile;`
- Line 20: `import org.gradle.api.tasks.TaskAction;`
- Line 21: `import org.gradle.process.ExecOperations;`
- Line 22: `import org.gradle.workers.WorkAction;`
- Line 23: `import org.gradle.workers.WorkParameters;`
- Line 24: `import org.gradle.workers.WorkerExecutor;`
- Line 26: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/DistroTestPlugin.java

### Concurrency Issue (3)
- Line 65: `private static final String EXAMPLE_PLUGIN_CONFIGURATION = "examplePlugin";`
- Line 66: `private static final String DISTRIBUTION_SYSPROP = "tests.distribution";`
- Line 67: `private static final String BWC_DISTRIBUTION_SYSPROP = "tests.bwc-distribution";`

### Unused Code (44)
- Line 12: `import org.elasticsearch.gradle.Architecture;`
- Line 13: `import org.elasticsearch.gradle.DistributionDownloadPlugin;`
- Line 14: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 15: `import org.elasticsearch.gradle.ElasticsearchDistribution.Platform;`
- Line 16: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 17: `import org.elasticsearch.gradle.Version;`
- Line 18: `import org.elasticsearch.gradle.VersionProperties;`
- Line 19: `import org.elasticsearch.gradle.internal.BwcVersions;`
- Line 20: `import org.elasticsearch.gradle.internal.InternalDistributionDownloadPlugin;`
- Line 21: `import org.elasticsearch.gradle.internal.JdkDownloadPlugin;`
- Line 22: `import org.elasticsearch.gradle.internal.docker.DockerSupportPlugin;`
- Line 23: `import org.elasticsearch.gradle.internal.docker.DockerSupportService;`
- Line 24: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 25: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 26: `import org.gradle.api.Action;`
- Line 27: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 28: `import org.gradle.api.Plugin;`
- Line 29: `import org.gradle.api.Project;`
- Line 30: `import org.gradle.api.Task;`
- Line 31: `import org.gradle.api.artifacts.Configuration;`
- Line 32: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 33: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 34: `import org.gradle.api.file.FileCollection;`
- Line 35: `import org.gradle.api.plugins.JavaPluginExtension;`
- Line 36: `import org.gradle.api.provider.Provider;`
- Line 37: `import org.gradle.api.specs.Specs;`
- Line 38: `import org.gradle.api.tasks.SourceSet;`
- Line 39: `import org.gradle.api.tasks.TaskProvider;`
- Line 40: `import org.gradle.api.tasks.testing.Test;`
- Line 42: `import java.util.ArrayList;`
- Line 43: `import java.util.Arrays;`
- Line 44: `import java.util.HashMap;`
- Line 45: `import java.util.List;`
- Line 46: `import java.util.Map;`
- Line 47: `import java.util.function.Supplier;`
- Line 49: `import static org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes.ARCHIVE;`
- Line 50: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.ALL_INTERNAL;`
- Line 51: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.DEB;`
- Line 52: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.DOCKER;`
- Line 53: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.DOCKER_CLOUD_ESS;`
- Line 54: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.DOCKER_IRONBANK;`
- Line 55: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.DOCKER_WOLFI;`
- Line 56: `import static org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes.RPM;`
- Line 57: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/ErrorReportingTestListener.java

### Resource Leak (2)
- Line 220: `fos = new FileOutputStream(this.outputFile);`
- Line 253: `return new BufferedReader(new FileReader(outputFile));`

### Concurrency Issue (3)
- Line 56: `public void setDumpOutputOnFailure(boolean dumpOutputOnFailure) {`
- Line 40: `private static final String REPRODUCE_WITH_PREFIX = "REPRODUCE WITH";`
- Line 48: `private boolean dumpOutputOnFailure = true;`

### Exception Handling (4)
- Line 130: `throw new UncheckedIOException("Error reading test suite output", e);`
- Line 222: `throw new UncheckedIOException("Unable to create test suite output file", e);`
- Line 243: `throw new UncheckedIOException("Unable to write test suite output", e);`
- Line 255: `throw new UncheckedIOException("Unable to read test suite output file", e);`

### Unused Code (27)
- Line 48: `private boolean dumpOutputOnFailure = true;`
- Line 11: `import org.gradle.api.internal.tasks.testing.logging.FullExceptionFormatter;`
- Line 12: `import org.gradle.api.internal.tasks.testing.logging.TestExceptionFormatter;`
- Line 13: `import org.gradle.api.logging.Logger;`
- Line 14: `import org.gradle.api.tasks.testing.Test;`
- Line 15: `import org.gradle.api.tasks.testing.TestDescriptor;`
- Line 16: `import org.gradle.api.tasks.testing.TestListener;`
- Line 17: `import org.gradle.api.tasks.testing.TestOutputEvent;`
- Line 18: `import org.gradle.api.tasks.testing.TestOutputListener;`
- Line 19: `import org.gradle.api.tasks.testing.TestResult;`
- Line 21: `import java.io.BufferedOutputStream;`
- Line 22: `import java.io.BufferedReader;`
- Line 23: `import java.io.Closeable;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.FileOutputStream;`
- Line 26: `import java.io.FileReader;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.PrintStream;`
- Line 29: `import java.io.PrintWriter;`
- Line 30: `import java.io.UncheckedIOException;`
- Line 31: `import java.io.Writer;`
- Line 32: `import java.util.Deque;`
- Line 33: `import java.util.LinkedHashSet;`
- Line 34: `import java.util.LinkedList;`
- Line 35: `import java.util.Map;`
- Line 36: `import java.util.Set;`
- Line 37: `import java.util.concurrent.ConcurrentHashMap;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/InternalClusterTestPlugin.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.JavaVersion;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import org.gradle.api.tasks.testing.Test;`
- Line 21: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/LegacyRestTestBasePlugin.java

### Concurrency Issue (6)
- Line 62: `public void apply(Project project) {`
- Line 46: `private static final String TESTS_REST_CLUSTER = "tests.rest.cluster";`
- Line 47: `private static final String TESTS_CLUSTER = "tests.cluster";`
- Line 48: `private static final String TESTS_CLUSTER_NAME = "tests.clustername";`
- Line 49: `private static final String TESTS_CLUSTER_READINESS = "tests.cluster.readiness";`
- Line 51: `private static final String TESTS_CLUSTER_REMOTE_ACCESS = "tests.cluster.remote_access";`

### Unused Code (28)
- Line 53: `private ProviderFactory providerFactory;`
- Line 54: `private Project project;`
- Line 12: `import org.elasticsearch.gradle.internal.ElasticsearchJavaBasePlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.ElasticsearchTestBasePlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.FixtureStop;`
- Line 15: `import org.elasticsearch.gradle.internal.InternalTestClustersPlugin;`
- Line 16: `import org.elasticsearch.gradle.internal.RestrictedBuildApiService;`
- Line 17: `import org.elasticsearch.gradle.internal.precommit.InternalPrecommitTasks;`
- Line 18: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 19: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 20: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 21: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 22: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 23: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 24: `import org.gradle.api.Plugin;`
- Line 25: `import org.gradle.api.Project;`
- Line 26: `import org.gradle.api.Task;`
- Line 27: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 28: `import org.gradle.api.provider.Provider;`
- Line 29: `import org.gradle.api.provider.ProviderFactory;`
- Line 30: `import org.gradle.api.specs.NotSpec;`
- Line 31: `import org.gradle.api.specs.Spec;`
- Line 32: `import org.gradle.api.tasks.Sync;`
- Line 33: `import org.gradle.api.tasks.bundling.Zip;`
- Line 35: `import javax.inject.Inject;`
- Line 37: `import static org.elasticsearch.gradle.internal.RestrictedBuildApiService.BUILD_API_RESTRICTIONS_SYS_PROPERTY;`
- Line 38: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.BUNDLE_PLUGIN_TASK_NAME;`
- Line 39: `import static org.elasticsearch.gradle.plugin.BasePluginBuildPlugin.EXPLODED_BUNDLE_PLUGIN_TASK_NAME;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/MutedTestPlugin.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.file.RegularFile;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.tasks.testing.Test;`
- Line 19: `import java.util.Arrays;`
- Line 20: `import java.util.List;`
- Line 22: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/MutedTestsBuildService.java

### Resource Leak (1)
- Line 55: `try (InputStream is = new BufferedInputStream(new FileInputStream(file))) {`

### Concurrency Issue (1)
- Line 37: `private final ObjectMapper objectMapper = new ObjectMapper(new YAMLFactory());`

### Exception Handling (1)
- Line 61: `throw new UncheckedIOException(e);`

### Unused Code (20)
- Line 12: `import com.fasterxml.jackson.annotation.JsonCreator;`
- Line 13: `import com.fasterxml.jackson.annotation.JsonProperty;`
- Line 14: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 15: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 17: `import org.gradle.api.file.RegularFile;`
- Line 18: `import org.gradle.api.file.RegularFileProperty;`
- Line 19: `import org.gradle.api.provider.ListProperty;`
- Line 20: `import org.gradle.api.services.BuildService;`
- Line 21: `import org.gradle.api.services.BuildServiceParameters;`
- Line 23: `import java.io.BufferedInputStream;`
- Line 24: `import java.io.File;`
- Line 25: `import java.io.FileInputStream;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.InputStream;`
- Line 28: `import java.io.UncheckedIOException;`
- Line 29: `import java.util.ArrayList;`
- Line 30: `import java.util.Collections;`
- Line 31: `import java.util.LinkedHashSet;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/RestIntegTestTask.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 13: `import org.gradle.api.tasks.CacheableTask;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/SimpleCommandLineArgumentProvider.java

### Unused Code (3)
- Line 12: `import org.gradle.process.CommandLineArgumentProvider;`
- Line 14: `import java.util.Arrays;`
- Line 15: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/StandaloneRestTestPlugin.java

### Exception Handling (1)
- Line 44: `throw new InvalidUserDataException(`

### Unused Code (17)
- Line 12: `import org.elasticsearch.gradle.internal.ExportElasticsearchBuildResourcesTask;`
- Line 13: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.precommit.InternalPrecommitTasks;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.LegacyJavaRestTestPlugin;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.LegacyYamlRestTestPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.RestTestUtil;`
- Line 18: `import org.gradle.api.InvalidUserDataException;`
- Line 19: `import org.gradle.api.Plugin;`
- Line 20: `import org.gradle.api.Project;`
- Line 21: `import org.gradle.api.plugins.JavaPlugin;`
- Line 22: `import org.gradle.api.tasks.SourceSet;`
- Line 23: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 24: `import org.gradle.api.tasks.testing.Test;`
- Line 25: `import org.gradle.plugins.ide.eclipse.model.EclipseModel;`
- Line 26: `import org.gradle.plugins.ide.idea.model.IdeaModel;`
- Line 28: `import java.util.Arrays;`
- Line 29: `import java.util.Map;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/StandaloneTestPlugin.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.internal.ElasticsearchJavaBasePlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.ElasticsearchTestBasePlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.precommit.InternalPrecommitTasks;`
- Line 16: `import org.gradle.api.Plugin;`
- Line 17: `import org.gradle.api.Project;`
- Line 18: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 19: `import org.gradle.api.tasks.SourceSet;`
- Line 20: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 21: `import org.gradle.api.tasks.TaskProvider;`
- Line 22: `import org.gradle.api.tasks.testing.Test;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/TestUtil.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.gradle.Architecture;`
- Line 13: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 15: `import java.util.Locale;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/TestWithDependenciesPlugin.java

### Unused Code (16)
- Line 12: `import org.apache.commons.lang.StringUtils;`
- Line 13: `import org.gradle.api.Plugin;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.artifacts.Configuration;`
- Line 16: `import org.gradle.api.artifacts.Dependency;`
- Line 17: `import org.gradle.api.artifacts.ProjectDependency;`
- Line 18: `import org.gradle.api.artifacts.dsl.DependencyHandler;`
- Line 19: `import org.gradle.api.attributes.Attribute;`
- Line 20: `import org.gradle.api.attributes.LibraryElements;`
- Line 21: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 22: `import org.gradle.api.tasks.Copy;`
- Line 23: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 25: `import java.io.File;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.stream.Collectors;`
- Line 29: `import static java.util.Arrays.stream;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/TestWithSslPlugin.java

### Unused Code (18)
- Line 12: `import org.elasticsearch.gradle.internal.ExportElasticsearchBuildResourcesTask;`
- Line 13: `import org.elasticsearch.gradle.internal.conventions.util.Util;`
- Line 14: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 15: `import org.elasticsearch.gradle.internal.precommit.FilePermissionsPrecommitPlugin;`
- Line 16: `import org.elasticsearch.gradle.internal.precommit.ForbiddenPatternsPrecommitPlugin;`
- Line 17: `import org.elasticsearch.gradle.internal.precommit.ForbiddenPatternsTask;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.LegacyJavaRestTestPlugin;`
- Line 19: `import org.elasticsearch.gradle.testclusters.ElasticsearchCluster;`
- Line 20: `import org.elasticsearch.gradle.testclusters.TestClustersAware;`
- Line 21: `import org.elasticsearch.gradle.testclusters.TestClustersPlugin;`
- Line 22: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 23: `import org.gradle.api.Plugin;`
- Line 24: `import org.gradle.api.Project;`
- Line 25: `import org.gradle.api.tasks.SourceSet;`
- Line 26: `import org.gradle.api.tasks.TaskProvider;`
- Line 28: `import java.io.File;`
- Line 30: `import static org.elasticsearch.gradle.internal.precommit.FilePermissionsPrecommitPlugin.FILEPERMISSIONS_TASK_NAME;`
- Line 31: `import static org.elasticsearch.gradle.internal.precommit.ForbiddenPatternsPrecommitPlugin.FORBIDDEN_PATTERNS_TASK_NAME;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/CopyRestApiTask.java

### Concurrency Issue (8)
- Line 167: `public void setSourceResourceDir(File sourceResourceDir) {`
- Line 171: `public void setSkipHasRestTestCheck(boolean skipHasRestTestCheck) {`
- Line 175: `public void setConfig(FileCollection config) {`
- Line 179: `public void setAdditionalConfig(FileCollection additionalConfig) {`
- Line 183: `public void setConfigToFileTree(SerializableFunction<FileCollection, FileTree> configToFileTree) {`
- Line 187: `public void setAdditionalConfigToFileTree(SerializableFunction<FileCollection, FileTree> additionalConfigToFileTree) {`
- Line 48: `private static final String REST_API_PREFIX = "rest-api-spec/api";`
- Line 49: `private static final String REST_TEST_PREFIX = "rest-api-spec/test";`

### Unused Code (29)
- Line 54: `private File sourceResourceDir;`
- Line 55: `private boolean skipHasRestTestCheck;`
- Line 56: `private FileCollection config;`
- Line 57: `private FileCollection additionalConfig;`
- Line 11: `import org.elasticsearch.gradle.internal.util.SerializableFunction;`
- Line 12: `import org.gradle.api.DefaultTask;`
- Line 13: `import org.gradle.api.file.DirectoryProperty;`
- Line 14: `import org.gradle.api.file.FileCollection;`
- Line 15: `import org.gradle.api.file.FileSystemOperations;`
- Line 16: `import org.gradle.api.file.FileTree;`
- Line 17: `import org.gradle.api.file.ProjectLayout;`
- Line 18: `import org.gradle.api.model.ObjectFactory;`
- Line 19: `import org.gradle.api.provider.ListProperty;`
- Line 20: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 22: `import org.gradle.api.tasks.InputFiles;`
- Line 23: `import org.gradle.api.tasks.Internal;`
- Line 24: `import org.gradle.api.tasks.OutputDirectory;`
- Line 25: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 26: `import org.gradle.api.tasks.TaskAction;`
- Line 27: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 28: `import org.gradle.api.tasks.util.PatternSet;`
- Line 29: `import org.gradle.internal.Factory;`
- Line 31: `import java.io.File;`
- Line 32: `import java.io.IOException;`
- Line 33: `import java.nio.file.Files;`
- Line 34: `import java.util.stream.Collectors;`
- Line 36: `import javax.inject.Inject;`
- Line 38: `import static org.elasticsearch.gradle.util.GradleUtils.getProjectPathFromTask;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/CopyRestTestsTask.java

### Concurrency Issue (8)
- Line 98: `public void setSubstitutions(Map<String, String> substitutions) {`
- Line 182: `public void setCoreConfig(FileCollection coreConfig) {`
- Line 186: `public void setXpackConfig(FileCollection xpackConfig) {`
- Line 190: `public void setAdditionalConfig(FileCollection additionalConfig) {`
- Line 194: `public void setCoreConfigToFileTree(SerializableFunction<FileCollection, FileTree> coreConfigToFileTree) {`
- Line 198: `public void setXpackConfigToFileTree(SerializableFunction<FileCollection, FileTree> xpackConfigToFileTree) {`
- Line 202: `public void setAdditionalConfigToFileTree(SerializableFunction<FileCollection, FileTree> additionalConfigToFileTree) {`
- Line 51: `private static final String REST_TEST_PREFIX = "rest-api-spec/test";`

### Unused Code (31)
- Line 57: `private FileCollection coreConfig;`
- Line 58: `private FileCollection xpackConfig;`
- Line 59: `private FileCollection additionalConfig;`
- Line 11: `import org.apache.tools.ant.filters.ReplaceTokens;`
- Line 12: `import org.elasticsearch.gradle.internal.util.SerializableFunction;`
- Line 13: `import org.gradle.api.DefaultTask;`
- Line 14: `import org.gradle.api.file.DirectoryProperty;`
- Line 15: `import org.gradle.api.file.FileCollection;`
- Line 16: `import org.gradle.api.file.FileSystemOperations;`
- Line 17: `import org.gradle.api.file.FileTree;`
- Line 18: `import org.gradle.api.file.ProjectLayout;`
- Line 19: `import org.gradle.api.internal.file.FileOperations;`
- Line 20: `import org.gradle.api.model.ObjectFactory;`
- Line 21: `import org.gradle.api.provider.ListProperty;`
- Line 22: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 23: `import org.gradle.api.tasks.Input;`
- Line 24: `import org.gradle.api.tasks.InputFiles;`
- Line 25: `import org.gradle.api.tasks.Optional;`
- Line 26: `import org.gradle.api.tasks.OutputDirectory;`
- Line 27: `import org.gradle.api.tasks.PathSensitive;`
- Line 28: `import org.gradle.api.tasks.PathSensitivity;`
- Line 29: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 30: `import org.gradle.api.tasks.TaskAction;`
- Line 31: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 32: `import org.gradle.api.tasks.util.PatternSet;`
- Line 33: `import org.gradle.internal.Factory;`
- Line 35: `import java.io.File;`
- Line 36: `import java.util.Map;`
- Line 37: `import java.util.stream.Collectors;`
- Line 39: `import javax.inject.Inject;`
- Line 41: `import static org.elasticsearch.gradle.util.GradleUtils.getProjectPathFromTask;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/InternalJavaRestTestPlugin.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.internal.test.RestIntegTestTask;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.registerTestTask;`
- Line 22: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.setupJavaRestTestDependenciesDefaults;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/InternalYamlRestTestPlugin.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.internal.test.RestIntegTestTask;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.registerTestTask;`
- Line 22: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.setupYamlRestTestDependenciesDefaults;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/LegacyJavaRestTestPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.test.LegacyRestTestBasePlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.tasks.SourceSet;`
- Line 17: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.registerTestTask;`
- Line 20: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.setupJavaRestTestDependenciesDefaults;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/LegacyYamlRestTestPlugin.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.test.LegacyRestTestBasePlugin;`
- Line 13: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.tasks.SourceSet;`
- Line 17: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 19: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.registerTestTask;`
- Line 20: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.setupYamlRestTestDependenciesDefaults;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/RestResourcesExtension.java

### Unused Code (4)
- Line 11: `import org.gradle.api.Action;`
- Line 12: `import org.gradle.api.model.ObjectFactory;`
- Line 13: `import org.gradle.api.provider.ListProperty;`
- Line 15: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/RestResourcesPlugin.java

### Concurrency Issue (5)
- Line 79: `public static final String COPY_YAML_TESTS_TASK = "copyYamlTestsTask";`
- Line 80: `public static final String COPY_REST_API_SPECS_TASK = "copyRestApiSpecsTask";`
- Line 81: `public static final String YAML_TESTS_USAGE = "yaml-tests";`
- Line 82: `public static final String YAML_XPACK_TESTS_USAGE = "yaml-xpack-tests";`
- Line 83: `public static final String YAML_SPEC_USAGE = "yaml-spec";`

### Unused Code (10)
- Line 11: `import org.gradle.api.Plugin;`
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.api.artifacts.Configuration;`
- Line 14: `import org.gradle.api.artifacts.Dependency;`
- Line 15: `import org.gradle.api.attributes.Usage;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 20: `import java.util.Map;`
- Line 22: `import static org.gradle.api.tasks.SourceSet.TEST_SOURCE_SET_NAME;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/RestTestBasePlugin.java

### Null Pointer (3)
- Line 314: `return project.getRootProject()`
- Line 374: `return project.getDependencies()`
- Line 380: `return project.getDependencies()`

### Concurrency Issue (16)
- Line 68: `private static final String TESTS_MAX_PARALLEL_FORKS_SYSPROP = "tests.max.parallel.forks";`
- Line 69: `private static final String DEFAULT_DISTRIBUTION_SYSPROP = "tests.default.distribution";`
- Line 70: `private static final String INTEG_TEST_DISTRIBUTION_SYSPROP = "tests.integ-test.distribution";`
- Line 71: `private static final String BWC_SNAPSHOT_DISTRIBUTION_SYSPROP_PREFIX = "tests.snapshot.distribution.";`
- Line 72: `private static final String BWC_RELEASED_DISTRIBUTION_SYSPROP_PREFIX = "tests.release.distribution.";`
- Line 73: `private static final String TESTS_CLUSTER_MODULES_PATH_SYSPROP = "tests.cluster.modules.path";`
- Line 74: `private static final String TESTS_CLUSTER_PLUGINS_PATH_SYSPROP = "tests.cluster.plugins.path";`
- Line 75: `private static final String DEFAULT_REST_INTEG_TEST_DISTRO = "default_distro";`
- Line 76: `private static final String INTEG_TEST_REST_INTEG_TEST_DISTRO = "integ_test_distro";`
- Line 77: `private static final String MODULES_CONFIGURATION = "clusterModules";`
- Line 78: `private static final String PLUGINS_CONFIGURATION = "clusterPlugins";`
- Line 79: `private static final String EXTRACTED_PLUGINS_CONFIGURATION = "extractedPlugins";`
- Line 81: `private static final String FEATURES_METADATA_CONFIGURATION = "featuresMetadataDeps";`
- Line 82: `private static final String DEFAULT_DISTRO_FEATURES_METADATA_CONFIGURATION = "defaultDistrofeaturesMetadataDeps";`
- Line 83: `private static final String TESTS_FEATURES_METADATA_PATH = "tests.features.metadata.path";`
- Line 84: `private static final String MINIMUM_WIRE_COMPATIBLE_VERSION_SYSPROP = "tests.minimum.wire.compatible";`

### Exception Handling (1)
- Line 231: `throw new IllegalArgumentException("Expected exactly one argument of type org.elasticsearch.gradle.Version");`

### Unused Code (46)
- Line 12: `import groovy.lang.Closure;`
- Line 14: `import org.elasticsearch.gradle.Architecture;`
- Line 15: `import org.elasticsearch.gradle.DistributionDownloadPlugin;`
- Line 16: `import org.elasticsearch.gradle.ElasticsearchDistribution;`
- Line 17: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 18: `import org.elasticsearch.gradle.Version;`
- Line 19: `import org.elasticsearch.gradle.VersionProperties;`
- Line 20: `import org.elasticsearch.gradle.distribution.ElasticsearchDistributionTypes;`
- Line 21: `import org.elasticsearch.gradle.internal.ElasticsearchJavaBasePlugin;`
- Line 22: `import org.elasticsearch.gradle.internal.InternalDistributionDownloadPlugin;`
- Line 23: `import org.elasticsearch.gradle.internal.test.ClusterFeaturesMetadataPlugin;`
- Line 24: `import org.elasticsearch.gradle.internal.test.ErrorReportingTestListener;`
- Line 25: `import org.elasticsearch.gradle.plugin.BasePluginBuildPlugin;`
- Line 26: `import org.elasticsearch.gradle.plugin.PluginBuildPlugin;`
- Line 27: `import org.elasticsearch.gradle.plugin.PluginPropertiesExtension;`
- Line 28: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 29: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 30: `import org.elasticsearch.gradle.transform.UnzipTransform;`
- Line 31: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 32: `import org.gradle.api.Action;`
- Line 33: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 34: `import org.gradle.api.Plugin;`
- Line 35: `import org.gradle.api.Project;`
- Line 36: `import org.gradle.api.Task;`
- Line 37: `import org.gradle.api.artifacts.Configuration;`
- Line 38: `import org.gradle.api.artifacts.Dependency;`
- Line 39: `import org.gradle.api.artifacts.DependencySet;`
- Line 40: `import org.gradle.api.artifacts.ProjectDependency;`
- Line 41: `import org.gradle.api.artifacts.type.ArtifactTypeDefinition;`
- Line 42: `import org.gradle.api.attributes.Attribute;`
- Line 43: `import org.gradle.api.file.ConfigurableFileCollection;`
- Line 44: `import org.gradle.api.file.FileCollection;`
- Line 45: `import org.gradle.api.file.FileTree;`
- Line 46: `import org.gradle.api.internal.artifacts.dependencies.ProjectDependencyInternal;`
- Line 47: `import org.gradle.api.provider.ProviderFactory;`
- Line 48: `import org.gradle.api.tasks.ClasspathNormalizer;`
- Line 49: `import org.gradle.api.tasks.PathSensitivity;`
- Line 50: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 52: `import java.util.Collection;`
- Line 53: `import java.util.Iterator;`
- Line 54: `import java.util.LinkedHashSet;`
- Line 55: `import java.util.List;`
- Line 56: `import java.util.Map;`
- Line 57: `import java.util.Optional;`
- Line 59: `import javax.inject.Inject;`
- Line 61: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/RestTestUtil.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.internal.test.RestIntegTestTask;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 15: `import org.gradle.api.plugins.JavaPlugin;`
- Line 16: `import org.gradle.api.provider.Provider;`
- Line 17: `import org.gradle.api.tasks.SourceSet;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import org.gradle.api.tasks.testing.Test;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/ReplaceByKey.java

### Unused Code (3)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 14: `import org.gradle.api.tasks.Input;`
- Line 15: `import org.gradle.api.tasks.Optional;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransform.java

### Unused Code (3)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 14: `import org.gradle.api.Named;`
- Line 15: `import org.gradle.api.tasks.Input;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformByParentArray.java

### Unused Code (1)
- Line 12: `import com.fasterxml.jackson.databind.node.ArrayNode;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformByParentObject.java

### Unused Code (2)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformGlobalSetup.java

### Unused Code (2)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import javax.annotation.Nullable;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformGlobalTeardown.java

### Unused Code (2)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import javax.annotation.Nullable;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/RestTestTransformer.java

### Unused Code (9)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 17: `import java.util.Iterator;`
- Line 18: `import java.util.LinkedList;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.stream.Collectors;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/do_/ReplaceKeyInDo.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/feature/FeatureInjector.java

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformGlobalSetup;`
- Line 19: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformGlobalTeardown;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 22: `import java.util.Iterator;`
- Line 24: `import javax.annotation.Nullable;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/headers/InjectHeaders.java

### Concurrency Issue (1)
- Line 32: `private static JsonNodeFactory jsonNodeFactory = JsonNodeFactory.withExactBigDecimals(false);`

### Unused Code (11)
- Line 12: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.FeatureInjector;`
- Line 19: `import org.gradle.api.tasks.Input;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.Set;`
- Line 24: `import java.util.function.Function;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/length/ReplaceKeyInLength.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/length/ReplaceValueInLength.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.node.NumericNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/match/AddMatch.java

### Concurrency Issue (1)
- Line 28: `private static JsonNodeFactory jsonNodeFactory = JsonNodeFactory.withExactBigDecimals(false);`

### Unused Code (9)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentArray;`
- Line 19: `import org.gradle.api.tasks.Input;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 22: `import java.util.Objects;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/match/RemoveMatch.java

### Unused Code (6)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 16: `import org.gradle.api.tasks.Input;`
- Line 17: `import org.gradle.api.tasks.Internal;`
- Line 18: `import org.gradle.api.tasks.Optional;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/match/ReplaceKeyInMatch.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/match/ReplaceValueInMatch.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/skip/Skip.java

### Concurrency Issue (1)
- Line 30: `private static JsonNodeFactory jsonNodeFactory = JsonNodeFactory.withExactBigDecimals(false);`

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 19: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 20: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformGlobalSetup;`
- Line 21: `import org.gradle.api.tasks.Input;`
- Line 23: `import java.util.Iterator;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/text/ReplaceIsFalse.java

### Unused Code (1)
- Line 12: `import com.fasterxml.jackson.databind.node.TextNode;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/text/ReplaceIsTrue.java

### Unused Code (1)
- Line 12: `import com.fasterxml.jackson.databind.node.TextNode;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/text/ReplaceTextual.java

### Unused Code (8)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 18: `import org.gradle.api.tasks.Input;`
- Line 19: `import org.gradle.api.tasks.Internal;`
- Line 20: `import org.gradle.api.tasks.Optional;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectAllowedWarnings.java

### Concurrency Issue (1)
- Line 30: `private static JsonNodeFactory jsonNodeFactory = JsonNodeFactory.withExactBigDecimals(false);`

### Unused Code (11)
- Line 33: `private String testName;`
- Line 12: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.FeatureInjector;`
- Line 19: `import org.gradle.api.tasks.Input;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 21: `import org.gradle.api.tasks.Optional;`
- Line 23: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectWarnings.java

### Concurrency Issue (1)
- Line 30: `private static JsonNodeFactory jsonNodeFactory = JsonNodeFactory.withExactBigDecimals(false);`

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.JsonNodeFactory;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.FeatureInjector;`
- Line 19: `import org.gradle.api.tasks.Input;`
- Line 20: `import org.gradle.api.tasks.Internal;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Objects;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/RemoveWarnings.java

### Unused Code (11)
- Line 35: `private String testName;`
- Line 12: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestContext;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformByParentObject;`
- Line 17: `import org.gradle.api.tasks.Input;`
- Line 18: `import org.gradle.api.tasks.Internal;`
- Line 19: `import org.gradle.api.tasks.Optional;`
- Line 21: `import java.util.ArrayList;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Set;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/transform/close_to/ReplaceValueInCloseTo.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.node.NumericNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.ReplaceByKey;`
- Line 16: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/compat/compat/AbstractYamlRestCompatTestPlugin.java

### Concurrency Issue (11)
- Line 57: `public static final String BWC_MINOR_CONFIG_NAME = "bwcMinor";`
- Line 58: `private static final String REST_COMPAT_CHECK_TASK_NAME = "checkRestCompat";`
- Line 59: `private static final String COMPATIBILITY_APIS_CONFIGURATION = "restCompatSpecs";`
- Line 60: `private static final String COMPATIBILITY_TESTS_CONFIGURATION = "restCompatTests";`
- Line 61: `private static final Path RELATIVE_API_PATH = Path.of("rest-api-spec/api");`
- Line 62: `private static final Path RELATIVE_TEST_PATH = Path.of("rest-api-spec/test");`
- Line 63: `private static final Path RELATIVE_REST_API_RESOURCES = Path.of("rest-api-spec/src/main/resources");`
- Line 64: `private static final Path RELATIVE_REST_CORE = Path.of("rest-api-spec");`
- Line 65: `private static final Path RELATIVE_REST_XPACK = Path.of("x-pack/plugin");`
- Line 66: `private static final Path RELATIVE_REST_PROJECT_RESOURCES = Path.of("src/yamlRestTest/resources");`
- Line 67: `private static final String SOURCE_SET_NAME = "yamlRestCompatTest";`

### Unused Code (39)
- Line 68: `private ProjectLayout projectLayout;`
- Line 69: `private FileOperations fileOperations;`
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.elasticsearch.gradle.internal.ElasticsearchJavaBasePlugin;`
- Line 14: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.CopyRestApiTask;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.CopyRestTestsTask;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.LegacyYamlRestTestPlugin;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.RestResourcesExtension;`
- Line 19: `import org.elasticsearch.gradle.internal.test.rest.RestResourcesPlugin;`
- Line 20: `import org.elasticsearch.gradle.test.YamlRestTestPlugin;`
- Line 21: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 22: `import org.gradle.api.Plugin;`
- Line 23: `import org.gradle.api.Project;`
- Line 24: `import org.gradle.api.Task;`
- Line 25: `import org.gradle.api.artifacts.Configuration;`
- Line 26: `import org.gradle.api.artifacts.Dependency;`
- Line 27: `import org.gradle.api.file.Directory;`
- Line 28: `import org.gradle.api.file.FileCollection;`
- Line 29: `import org.gradle.api.file.ProjectLayout;`
- Line 30: `import org.gradle.api.file.RelativePath;`
- Line 31: `import org.gradle.api.internal.file.FileOperations;`
- Line 32: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 33: `import org.gradle.api.plugins.JavaBasePlugin;`
- Line 34: `import org.gradle.api.provider.Provider;`
- Line 35: `import org.gradle.api.tasks.SourceSet;`
- Line 36: `import org.gradle.api.tasks.SourceSetContainer;`
- Line 37: `import org.gradle.api.tasks.Sync;`
- Line 38: `import org.gradle.api.tasks.TaskProvider;`
- Line 39: `import org.gradle.api.tasks.testing.Test;`
- Line 40: `import org.gradle.language.jvm.tasks.ProcessResources;`
- Line 42: `import java.io.File;`
- Line 43: `import java.nio.file.Path;`
- Line 44: `import java.util.Arrays;`
- Line 45: `import java.util.Comparator;`
- Line 46: `import java.util.Map;`
- Line 48: `import javax.inject.Inject;`
- Line 50: `import static org.elasticsearch.gradle.internal.test.rest.RestTestUtil.setupYamlRestTestDependenciesDefaults;`
- Line 51: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/compat/compat/LegacyYamlRestCompatTestPlugin.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.gradle.internal.test.rest.LegacyYamlRestTestPlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.test.rest.RestTestUtil;`
- Line 14: `import org.gradle.api.Plugin;`
- Line 15: `import org.gradle.api.Project;`
- Line 16: `import org.gradle.api.file.ProjectLayout;`
- Line 17: `import org.gradle.api.internal.file.FileOperations;`
- Line 18: `import org.gradle.api.tasks.SourceSet;`
- Line 19: `import org.gradle.api.tasks.TaskProvider;`
- Line 20: `import org.gradle.api.tasks.testing.Test;`
- Line 22: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/compat/compat/RestCompatTestTransformTask.java

### Null Pointer (2)
- Line 535: `return skippedTestByFilePatternTransformations.keySet()`
- Line 544: `return skippedTestByTestNameTransformations.keySet()`

### Concurrency Issue (5)
- Line 83: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`
- Line 84: `private static final ObjectMapper MAPPER = new ObjectMapper(YAML_FACTORY);`
- Line 85: `private static final ObjectReader READER = MAPPER.readerFor(ObjectNode.class);`
- Line 86: `private static final ObjectWriter WRITER = MAPPER.writerFor(ObjectNode.class);`
- Line 87: `private static final String REST_TEST_PREFIX = "rest-api-spec/test";`

### Exception Handling (3)
- Line 103: `throw new UnsupportedOperationException();`
- Line 142: `throw new IllegalArgumentException(`
- Line 513: `throw new IllegalArgumentException("could not split " + file + " into expected parts");`

### Unused Code (62)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 14: `import com.fasterxml.jackson.databind.ObjectReader;`
- Line 15: `import com.fasterxml.jackson.databind.ObjectWriter;`
- Line 16: `import com.fasterxml.jackson.databind.SequenceWriter;`
- Line 17: `import com.fasterxml.jackson.databind.node.NumericNode;`
- Line 18: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 19: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 20: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 21: `import com.fasterxml.jackson.dataformat.yaml.YAMLParser;`
- Line 22: `import com.google.common.collect.Sets;`
- Line 24: `import org.apache.commons.lang3.tuple.Pair;`
- Line 25: `import org.elasticsearch.gradle.Version;`
- Line 26: `import org.elasticsearch.gradle.VersionProperties;`
- Line 27: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 28: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransformer;`
- Line 29: `import org.elasticsearch.gradle.internal.test.rest.transform.close_to.ReplaceValueInCloseTo;`
- Line 30: `import org.elasticsearch.gradle.internal.test.rest.transform.do_.ReplaceKeyInDo;`
- Line 31: `import org.elasticsearch.gradle.internal.test.rest.transform.headers.InjectHeaders;`
- Line 32: `import org.elasticsearch.gradle.internal.test.rest.transform.length.ReplaceKeyInLength;`
- Line 33: `import org.elasticsearch.gradle.internal.test.rest.transform.length.ReplaceValueInLength;`
- Line 34: `import org.elasticsearch.gradle.internal.test.rest.transform.match.AddMatch;`
- Line 35: `import org.elasticsearch.gradle.internal.test.rest.transform.match.RemoveMatch;`
- Line 36: `import org.elasticsearch.gradle.internal.test.rest.transform.match.ReplaceKeyInMatch;`
- Line 37: `import org.elasticsearch.gradle.internal.test.rest.transform.match.ReplaceValueInMatch;`
- Line 38: `import org.elasticsearch.gradle.internal.test.rest.transform.skip.Skip;`
- Line 39: `import org.elasticsearch.gradle.internal.test.rest.transform.text.ReplaceIsFalse;`
- Line 40: `import org.elasticsearch.gradle.internal.test.rest.transform.text.ReplaceIsTrue;`
- Line 41: `import org.elasticsearch.gradle.internal.test.rest.transform.text.ReplaceTextual;`
- Line 42: `import org.elasticsearch.gradle.internal.test.rest.transform.warnings.InjectAllowedWarnings;`
- Line 43: `import org.elasticsearch.gradle.internal.test.rest.transform.warnings.InjectWarnings;`
- Line 44: `import org.elasticsearch.gradle.internal.test.rest.transform.warnings.RemoveWarnings;`
- Line 45: `import org.gradle.api.DefaultTask;`
- Line 46: `import org.gradle.api.file.DirectoryProperty;`
- Line 47: `import org.gradle.api.file.FileSystemOperations;`
- Line 48: `import org.gradle.api.file.FileTree;`
- Line 49: `import org.gradle.api.model.ObjectFactory;`
- Line 50: `import org.gradle.api.provider.ListProperty;`
- Line 51: `import org.gradle.api.tasks.IgnoreEmptyDirectories;`
- Line 52: `import org.gradle.api.tasks.Input;`
- Line 53: `import org.gradle.api.tasks.InputFiles;`
- Line 54: `import org.gradle.api.tasks.Internal;`
- Line 55: `import org.gradle.api.tasks.Nested;`
- Line 56: `import org.gradle.api.tasks.OutputDirectory;`
- Line 57: `import org.gradle.api.tasks.SkipWhenEmpty;`
- Line 58: `import org.gradle.api.tasks.TaskAction;`
- Line 59: `import org.gradle.api.tasks.util.PatternFilterable;`
- Line 60: `import org.gradle.api.tasks.util.PatternSet;`
- Line 61: `import org.gradle.internal.Factory;`
- Line 63: `import java.io.File;`
- Line 64: `import java.io.IOException;`
- Line 65: `import java.util.ArrayList;`
- Line 66: `import java.util.Arrays;`
- Line 67: `import java.util.Collections;`
- Line 68: `import java.util.HashMap;`
- Line 69: `import java.util.Iterator;`
- Line 70: `import java.util.LinkedHashMap;`
- Line 71: `import java.util.LinkedList;`
- Line 72: `import java.util.List;`
- Line 73: `import java.util.Map;`
- Line 74: `import java.util.stream.Collectors;`
- Line 76: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rest/compat/compat/YamlRestCompatTestPlugin.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.internal.test.rest.InternalYamlRestTestPlugin;`
- Line 13: `import org.elasticsearch.gradle.internal.test.rest.RestTestUtil;`
- Line 14: `import org.elasticsearch.gradle.testclusters.StandaloneRestIntegTestTask;`
- Line 15: `import org.gradle.api.Plugin;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.api.file.ProjectLayout;`
- Line 18: `import org.gradle.api.internal.file.FileOperations;`
- Line 19: `import org.gradle.api.tasks.SourceSet;`
- Line 20: `import org.gradle.api.tasks.TaskProvider;`
- Line 21: `import org.gradle.api.tasks.testing.Test;`
- Line 23: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rerun/TestRerunPlugin.java

### Unused Code (6)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.model.ObjectFactory;`
- Line 15: `import org.gradle.api.tasks.testing.Test;`
- Line 17: `import javax.inject.Inject;`
- Line 19: `import static org.elasticsearch.gradle.internal.test.rerun.TestTaskConfigurer.configureTestTask;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rerun/TestRerunTaskExtension.java

### Concurrency Issue (1)
- Line 33: `public static final String NAME = "rerun";`

### Unused Code (4)
- Line 12: `import org.gradle.api.model.ObjectFactory;`
- Line 13: `import org.gradle.api.provider.Property;`
- Line 14: `import org.gradle.api.tasks.testing.Test;`
- Line 16: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rerun/TestTaskConfigurer.java

### Exception Handling (2)
- Line 65: `throw new RuntimeException(e);`
- Line 81: `throw new RuntimeException(e);`

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.internal.test.rerun.executer.RerunTestExecuter;`
- Line 13: `import org.gradle.api.Action;`
- Line 14: `import org.gradle.api.Task;`
- Line 15: `import org.gradle.api.internal.tasks.testing.JvmTestExecutionSpec;`
- Line 16: `import org.gradle.api.internal.tasks.testing.TestExecuter;`
- Line 17: `import org.gradle.api.model.ObjectFactory;`
- Line 18: `import org.gradle.api.tasks.testing.Test;`
- Line 20: `import java.lang.reflect.InvocationTargetException;`
- Line 21: `import java.lang.reflect.Method;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rerun/executer/RerunTestExecuter.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.gradle.internal.test.rerun.TestRerunTaskExtension;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.internal.tasks.testing.JvmTestExecutionSpec;`
- Line 15: `import org.gradle.api.internal.tasks.testing.TestDescriptorInternal;`
- Line 16: `import org.gradle.api.internal.tasks.testing.TestExecuter;`
- Line 17: `import org.gradle.api.internal.tasks.testing.TestResultProcessor;`
- Line 18: `import org.gradle.internal.id.CompositeIdGenerator;`
- Line 19: `import org.gradle.process.internal.ExecException;`
- Line 21: `import java.util.Comparator;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.stream.Collectors;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/test/rerun/executer/RerunTestResultProcessor.java

### Unused Code (11)
- Line 35: `private TestDescriptorInternal rootTestDescriptor;`
- Line 12: `import org.gradle.api.internal.tasks.testing.TestCompleteEvent;`
- Line 13: `import org.gradle.api.internal.tasks.testing.TestDescriptorInternal;`
- Line 14: `import org.gradle.api.internal.tasks.testing.TestResultProcessor;`
- Line 15: `import org.gradle.api.internal.tasks.testing.TestStartEvent;`
- Line 16: `import org.gradle.api.tasks.testing.TestFailure;`
- Line 17: `import org.gradle.api.tasks.testing.TestOutputEvent;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/testfixtures/DockerComposeThrottle.java

### Unused Code (2)
- Line 11: `import org.gradle.api.services.BuildService;`
- Line 12: `import org.gradle.api.services.BuildServiceParameters;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/testfixtures/TestFixtureDeployment.java

### Unused Code (4)
- Line 12: `import org.gradle.api.Named;`
- Line 13: `import org.gradle.api.provider.ListProperty;`
- Line 14: `import org.gradle.api.provider.Property;`
- Line 16: `import java.io.File;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/testfixtures/TestFixtureTask.java

### Unused Code (3)
- Line 11: `import org.gradle.api.DefaultTask;`
- Line 12: `import org.gradle.api.file.DirectoryProperty;`
- Line 13: `import org.gradle.api.tasks.Internal;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/testfixtures/TestFixturesDeployPlugin.java

### Concurrency Issue (1)
- Line 27: `public static final String DEPLOY_FIXTURE_TASK_NAME = "deployFixtureDockerImages";`

### Unused Code (10)
- Line 12: `import org.apache.commons.lang.StringUtils;`
- Line 13: `import org.elasticsearch.gradle.Architecture;`
- Line 14: `import org.elasticsearch.gradle.internal.docker.DockerBuildTask;`
- Line 15: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 16: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 17: `import org.gradle.api.Plugin;`
- Line 18: `import org.gradle.api.Project;`
- Line 20: `import java.util.Arrays;`
- Line 21: `import java.util.List;`
- Line 23: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/testfixtures/TestFixturesPlugin.java

### Concurrency Issue (2)
- Line 54: `private static final Logger LOGGER = Logging.getLogger(TestFixturesPlugin.class);`
- Line 56: `static final String DOCKER_COMPOSE_YML = "docker-compose.yml";`

### Exception Handling (4)
- Line 67: `throw new UnsupportedOperationException();`
- Line 102: `throw new UncheckedIOException(e);`
- Line 224: `throw new IllegalArgumentException("Not a task type: " + type);`
- Line 227: `throw new IllegalArgumentException("No such task: " + type);`

### Unused Code (36)
- Line 11: `import com.avast.gradle.dockercompose.ComposeExtension;`
- Line 12: `import com.avast.gradle.dockercompose.DockerComposePlugin;`
- Line 13: `import com.avast.gradle.dockercompose.tasks.ComposeBuild;`
- Line 14: `import com.avast.gradle.dockercompose.tasks.ComposeDown;`
- Line 15: `import com.avast.gradle.dockercompose.tasks.ComposePull;`
- Line 16: `import com.avast.gradle.dockercompose.tasks.ComposeUp;`
- Line 18: `import org.elasticsearch.gradle.internal.docker.DockerSupportPlugin;`
- Line 19: `import org.elasticsearch.gradle.internal.docker.DockerSupportService;`
- Line 20: `import org.elasticsearch.gradle.internal.info.GlobalBuildInfoPlugin;`
- Line 21: `import org.elasticsearch.gradle.test.SystemPropertyCommandLineArgumentProvider;`
- Line 22: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 23: `import org.gradle.api.Action;`
- Line 24: `import org.gradle.api.DefaultTask;`
- Line 25: `import org.gradle.api.Plugin;`
- Line 26: `import org.gradle.api.Project;`
- Line 27: `import org.gradle.api.Task;`
- Line 28: `import org.gradle.api.file.FileSystemOperations;`
- Line 29: `import org.gradle.api.logging.LogLevel;`
- Line 30: `import org.gradle.api.logging.Logger;`
- Line 31: `import org.gradle.api.logging.Logging;`
- Line 32: `import org.gradle.api.plugins.BasePlugin;`
- Line 33: `import org.gradle.api.plugins.ExtraPropertiesExtension;`
- Line 34: `import org.gradle.api.provider.Provider;`
- Line 35: `import org.gradle.api.provider.ProviderFactory;`
- Line 36: `import org.gradle.api.tasks.TaskContainer;`
- Line 37: `import org.gradle.api.tasks.TaskProvider;`
- Line 38: `import org.gradle.api.tasks.testing.Test;`
- Line 40: `import java.io.File;`
- Line 41: `import java.io.IOException;`
- Line 42: `import java.io.UncheckedIOException;`
- Line 43: `import java.nio.file.Files;`
- Line 44: `import java.util.Collections;`
- Line 45: `import java.util.EnumSet;`
- Line 46: `import java.util.function.BiConsumer;`
- Line 48: `import javax.inject.Inject;`
- Line 50: `import static org.elasticsearch.gradle.internal.util.ParamsUtils.loadBuildParams;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/AbstractCustomJavaToolchainResolver.java

### Exception Handling (2)
- Line 28: `default -> throw new UnsupportedOperationException("Operating system " + operatingSystem);`
- Line 37: `default -> throw new UnsupportedOperationException("Architecture " + architecture);`

### Unused Code (4)
- Line 12: `import org.gradle.jvm.toolchain.JavaToolchainResolver;`
- Line 13: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 14: `import org.gradle.platform.Architecture;`
- Line 15: `import org.gradle.platform.OperatingSystem;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/AdoptiumJdkToolchainResolver.java

### Exception Handling (1)
- Line 80: `throw new RuntimeException(e);`

### Unused Code (15)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 15: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 16: `import org.gradle.jvm.toolchain.JavaToolchainDownload;`
- Line 17: `import org.gradle.jvm.toolchain.JavaToolchainRequest;`
- Line 18: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 20: `import java.io.FileNotFoundException;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.net.URI;`
- Line 23: `import java.net.URL;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Optional;`
- Line 26: `import java.util.concurrent.ConcurrentHashMap;`
- Line 27: `import java.util.stream.StreamSupport;`
- Line 29: `import static org.gradle.jvm.toolchain.JavaToolchainDownload.fromUri;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/ArchivedOracleJdkToolchainResolver.java

### Unused Code (13)
- Line 12: `import org.apache.groovy.util.Maps;`
- Line 13: `import org.elasticsearch.gradle.VersionProperties;`
- Line 14: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 15: `import org.gradle.jvm.toolchain.JavaToolchainDownload;`
- Line 16: `import org.gradle.jvm.toolchain.JavaToolchainRequest;`
- Line 17: `import org.gradle.jvm.toolchain.JavaToolchainSpec;`
- Line 18: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 19: `import org.gradle.platform.Architecture;`
- Line 20: `import org.gradle.platform.BuildPlatform;`
- Line 21: `import org.gradle.platform.OperatingSystem;`
- Line 23: `import java.net.URI;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Optional;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/JavaToolChainResolverPlugin.java

### Unused Code (4)
- Line 12: `import org.gradle.api.Plugin;`
- Line 13: `import org.gradle.api.initialization.Settings;`
- Line 14: `import org.gradle.jvm.toolchain.JavaToolchainResolverRegistry;`
- Line 16: `import javax.inject.Inject;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/toolchain/OracleOpenJdkToolchainResolver.java

### Concurrency Issue (1)
- Line 81: `private static final Pattern VERSION_PATTERN = Pattern.compile(`

### Exception Handling (1)
- Line 109: `throw new IllegalStateException("Unable to parse bundled JDK version " + bundledJdkVersion);`

### Unused Code (14)
- Line 12: `import org.elasticsearch.gradle.VersionProperties;`
- Line 13: `import org.gradle.jvm.toolchain.JavaLanguageVersion;`
- Line 14: `import org.gradle.jvm.toolchain.JavaToolchainDownload;`
- Line 15: `import org.gradle.jvm.toolchain.JavaToolchainRequest;`
- Line 16: `import org.gradle.jvm.toolchain.JavaToolchainSpec;`
- Line 17: `import org.gradle.jvm.toolchain.JvmVendorSpec;`
- Line 18: `import org.gradle.platform.Architecture;`
- Line 19: `import org.gradle.platform.BuildPlatform;`
- Line 20: `import org.gradle.platform.OperatingSystem;`
- Line 22: `import java.net.URI;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Optional;`
- Line 25: `import java.util.regex.Matcher;`
- Line 26: `import java.util.regex.Pattern;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/DependenciesUtils.java

### Unused Code (13)
- Line 12: `import com.github.jengelman.gradle.plugins.shadow.ShadowBasePlugin;`
- Line 14: `import org.gradle.api.artifacts.Configuration;`
- Line 15: `import org.gradle.api.artifacts.ResolvableDependencies;`
- Line 16: `import org.gradle.api.artifacts.component.ComponentIdentifier;`
- Line 17: `import org.gradle.api.artifacts.component.ProjectComponentIdentifier;`
- Line 18: `import org.gradle.api.artifacts.result.ResolvedComponentResult;`
- Line 19: `import org.gradle.api.artifacts.result.ResolvedDependencyResult;`
- Line 20: `import org.gradle.api.file.FileCollection;`
- Line 21: `import org.gradle.api.provider.Provider;`
- Line 22: `import org.gradle.api.specs.AndSpec;`
- Line 23: `import org.gradle.api.specs.Spec;`
- Line 25: `import java.util.Set;`
- Line 26: `import java.util.stream.Collectors;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/ParamsUtils.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.gradle.internal.info.BuildParameterExtension;`
- Line 13: `import org.elasticsearch.gradle.internal.info.BuildParameterService;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.provider.Property;`
- Line 16: `import org.gradle.api.services.BuildServiceRegistration;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/SerializableFunction.java

### Unused Code (2)
- Line 12: `import java.io.Serializable;`
- Line 13: `import java.util.function.Function;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/SourceDirectoryCommandLineArgumentProvider.java

### Unused Code (6)
- Line 12: `import org.gradle.api.file.Directory;`
- Line 13: `import org.gradle.api.tasks.InputDirectory;`
- Line 14: `import org.gradle.api.tasks.PathSensitive;`
- Line 15: `import org.gradle.api.tasks.PathSensitivity;`
- Line 16: `import org.gradle.process.CommandLineArgumentProvider;`
- Line 18: `import java.util.Arrays;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/ports/AvailablePortAllocator.java

### Concurrency Issue (4)
- Line 18: `public static final int MIN_PRIVATE_PORT = 10300;`
- Line 19: `public static final int MAX_PRIVATE_PORT = 13300;`
- Line 20: `public static final int DEFAULT_RANGE_SIZE = 10;`
- Line 24: `private ReservedPortRangeFactory portRangeFactory = new DefaultReservedPortRangeFactory();`

### Exception Handling (1)
- Line 30: `throw new IllegalStateException(`

### Unused Code (4)
- Line 24: `private ReservedPortRangeFactory portRangeFactory = new DefaultReservedPortRangeFactory();`
- Line 12: `import org.gradle.internal.Pair;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.List;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/ports/DefaultPortDetector.java

### Unused Code (3)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.net.DatagramSocket;`
- Line 14: `import java.net.ServerSocket;`

## ../build-tools-internal/src/main/java/org/elasticsearch/gradle/internal/util/ports/ReservedPortRange.java

### Concurrency Issue (3)
- Line 51: `public void setCurrent(int current) {`
- Line 23: `private final Lock lock = new ReentrantLock();`
- Line 24: `private PortDetector portDetector = new DefaultPortDetector();`

### Infinite Loop (1)
- Line 85: `while (true) {`

### Unused Code (9)
- Line 24: `private PortDetector portDetector = new DefaultPortDetector();`
- Line 27: `private int current;`
- Line 12: `import java.util.ArrayList;`
- Line 13: `import java.util.HashMap;`
- Line 14: `import java.util.List;`
- Line 15: `import java.util.Map;`
- Line 16: `import java.util.Random;`
- Line 17: `import java.util.concurrent.locks.Lock;`
- Line 18: `import java.util.concurrent.locks.ReentrantLock;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/AbstractDistributionDownloadPluginTests.java

### Concurrency Issue (9)
- Line 27: `protected static final Version BWC_MAJOR_VERSION = Version.fromString("2.0.0");`
- Line 28: `protected static final Version BWC_MINOR_VERSION = Version.fromString("1.1.0");`
- Line 29: `protected static final Version BWC_STAGED_VERSION = Version.fromString("1.0.0");`
- Line 30: `protected static final Version BWC_BUGFIX_VERSION = Version.fromString("1.0.1");`
- Line 31: `protected static final Version BWC_MAINTENANCE_VERSION = Version.fromString("0.90.1");`
- Line 34: `protected static final BwcVersions BWC_MINOR = new BwcVersions(`
- Line 39: `protected static final BwcVersions BWC_STAGED = new BwcVersions(`
- Line 44: `protected static final BwcVersions BWC_BUGFIX = new BwcVersions(`
- Line 49: `protected static final BwcVersions BWC_MAINTENANCE = new BwcVersions(`

### Unused Code (7)
- Line 12: `import org.elasticsearch.gradle.internal.BwcVersions;`
- Line 13: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 17: `import java.io.File;`
- Line 18: `import java.util.Arrays;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/ConcatFilesTaskTests.java

### Unused Code (9)
- Line 11: `import org.gradle.api.Project;`
- Line 12: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 13: `import org.junit.Test;`
- Line 15: `import java.io.File;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.charset.StandardCharsets;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.util.Arrays;`
- Line 21: `import static org.junit.Assert.assertEquals;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/EmptyDirTaskTests.java

### Unused Code (10)
- Line 11: `import org.elasticsearch.gradle.OS;`
- Line 12: `import org.gradle.api.Project;`
- Line 13: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 14: `import org.junit.Test;`
- Line 16: `import java.io.File;`
- Line 17: `import java.io.IOException;`
- Line 19: `import static org.junit.Assert.assertEquals;`
- Line 20: `import static org.junit.Assert.assertFalse;`
- Line 21: `import static org.junit.Assert.assertTrue;`
- Line 22: `import static org.junit.Assume.assumeFalse;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/InternalDistributionDownloadPluginTests.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.gradle.AbstractDistributionDownloadPluginTests;`
- Line 13: `import org.elasticsearch.gradle.ElasticsearchDistributionType;`
- Line 14: `import org.elasticsearch.gradle.VersionProperties;`
- Line 15: `import org.elasticsearch.gradle.internal.distribution.InternalElasticsearchDistributionTypes;`
- Line 16: `import org.gradle.api.Project;`
- Line 17: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 18: `import org.junit.Test;`
- Line 20: `import java.io.File;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/JdkDownloadPluginTests.java

### Unused Code (7)
- Line 12: `import org.gradle.api.NamedDomainObjectContainer;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 15: `import org.junit.Test;`
- Line 17: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 18: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 19: `import static org.junit.Assert.assertThrows;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/checkstyle/SnipptLengthCheckTests.java

### Unused Code (9)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.Arrays;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.function.BiConsumer;`
- Line 19: `import static java.util.Collections.singletonList;`
- Line 20: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 21: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 22: `import static org.junit.Assert.fail;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/docker/DockerSupportServiceTests.java

### Unused Code (8)
- Line 11: `import org.junit.Test;`
- Line 13: `import java.util.HashMap;`
- Line 14: `import java.util.List;`
- Line 15: `import java.util.Map;`
- Line 17: `import static org.elasticsearch.gradle.internal.docker.DockerSupportService.deriveId;`
- Line 18: `import static org.elasticsearch.gradle.internal.docker.DockerSupportService.parseOsRelease;`
- Line 19: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 20: `import static org.hamcrest.MatcherAssert.assertThat;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/docker/TransformLog4jConfigFilterTests.java

### Unused Code (4)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.util.List;`
- Line 16: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 17: `import static org.hamcrest.Matchers.equalTo;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/precommit/DependencyLicensesTaskTests.java

### Concurrency Issue (2)
- Line 37: `private static final String PERMISSIVE_LICENSE_TEXT = "Eclipse Public License - v 2.0";`
- Line 41: `public ExpectedException expectedException = ExpectedException.none();`

### Unused Code (23)
- Line 45: `private Project project;`
- Line 47: `private Dependency dependency;`
- Line 11: `import org.apache.groovy.util.Maps;`
- Line 12: `import org.gradle.api.Action;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.artifacts.Dependency;`
- Line 16: `import org.gradle.api.file.FileCollection;`
- Line 17: `import org.gradle.api.plugins.JavaPlugin;`
- Line 18: `import org.gradle.api.tasks.TaskProvider;`
- Line 19: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 20: `import org.junit.Before;`
- Line 21: `import org.junit.Rule;`
- Line 22: `import org.junit.Test;`
- Line 23: `import org.junit.rules.ExpectedException;`
- Line 25: `import java.io.File;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.nio.charset.StandardCharsets;`
- Line 28: `import java.nio.file.Files;`
- Line 29: `import java.nio.file.Path;`
- Line 30: `import java.util.HashMap;`
- Line 31: `import java.util.Map;`
- Line 33: `import static org.hamcrest.CoreMatchers.containsString;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/precommit/FilePermissionsTaskTests.java

### Null Pointer (1)
- Line 96: `return project.getTasks()`

### Unused Code (16)
- Line 11: `import org.elasticsearch.gradle.OS;`
- Line 12: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 13: `import org.gradle.api.GradleException;`
- Line 14: `import org.gradle.api.Project;`
- Line 15: `import org.gradle.api.plugins.JavaPlugin;`
- Line 16: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 17: `import org.junit.Assert;`
- Line 18: `import org.junit.Test;`
- Line 20: `import java.io.File;`
- Line 21: `import java.nio.charset.Charset;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.stream.Collectors;`
- Line 26: `import static org.junit.Assert.assertEquals;`
- Line 27: `import static org.junit.Assert.assertTrue;`
- Line 28: `import static org.junit.Assume.assumeFalse;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/precommit/ForbiddenPatternsTaskTests.java

### Unused Code (20)
- Line 11: `import org.elasticsearch.gradle.util.GradleUtils;`
- Line 12: `import org.gradle.api.GradleException;`
- Line 13: `import org.gradle.api.Project;`
- Line 14: `import org.gradle.api.file.FileTree;`
- Line 15: `import org.gradle.api.plugins.JavaPlugin;`
- Line 16: `import org.gradle.testfixtures.ProjectBuilder;`
- Line 17: `import org.junit.Test;`
- Line 19: `import java.io.File;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.nio.charset.StandardCharsets;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.util.Arrays;`
- Line 24: `import java.util.HashMap;`
- Line 25: `import java.util.Map;`
- Line 26: `import java.util.Optional;`
- Line 27: `import java.util.concurrent.Callable;`
- Line 28: `import java.util.stream.Collectors;`
- Line 30: `import static org.junit.Assert.assertEquals;`
- Line 31: `import static org.junit.Assert.assertTrue;`
- Line 32: `import static org.junit.Assert.fail;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/BreakingChangesGeneratorTest.java

### Unused Code (8)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Paths;`
- Line 17: `import java.util.List;`
- Line 18: `import java.util.Objects;`
- Line 20: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 21: `import static org.hamcrest.Matchers.equalTo;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/ExtractCurrentVersionsTaskTests.java

### Concurrency Issue (4)
- Line 24: `public void testFieldExtractor() {`
- Line 28: `public static final Version V_2 = def(2);`
- Line 29: `public static final Version V_3 = def(3);`
- Line 32: `public static final Version REF = V_3;`

### Unused Code (6)
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.body.FieldDeclaration;`
- Line 15: `import org.elasticsearch.gradle.internal.release.ExtractCurrentVersionsTask.FieldIdExtractor;`
- Line 16: `import org.junit.Test;`
- Line 18: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 19: `import static org.hamcrest.Matchers.is;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/GenerateReleaseNotesTaskTest.java

### Concurrency Issue (1)
- Line 40: `public void setup() {`

### Unused Code (22)
- Line 37: `private GitWrapper gitWrapper;`
- Line 12: `import org.junit.Before;`
- Line 13: `import org.junit.Test;`
- Line 15: `import java.io.File;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.Set;`
- Line 18: `import java.util.stream.Stream;`
- Line 20: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 21: `import static org.hamcrest.Matchers.aMapWithSize;`
- Line 22: `import static org.hamcrest.Matchers.allOf;`
- Line 23: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 24: `import static org.hamcrest.Matchers.equalTo;`
- Line 25: `import static org.hamcrest.Matchers.hasEntry;`
- Line 26: `import static org.hamcrest.Matchers.hasItem;`
- Line 27: `import static org.hamcrest.Matchers.hasKey;`
- Line 28: `import static org.hamcrest.Matchers.is;`
- Line 29: `import static org.mockito.Matchers.anyString;`
- Line 30: `import static org.mockito.Matchers.eq;`
- Line 31: `import static org.mockito.Mockito.mock;`
- Line 32: `import static org.mockito.Mockito.verify;`
- Line 33: `import static org.mockito.Mockito.verifyNoMoreInteractions;`
- Line 34: `import static org.mockito.Mockito.when;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/PruneChangelogsTaskTests.java

### Unused Code (28)
- Line 43: `private GitWrapper gitWrapper;`
- Line 44: `private DeleteHelper deleteHelper;`
- Line 12: `import org.elasticsearch.gradle.OS;`
- Line 13: `import org.elasticsearch.gradle.internal.release.PruneChangelogsTask.DeleteHelper;`
- Line 14: `import org.gradle.api.GradleException;`
- Line 15: `import org.junit.Before;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.io.File;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.stream.Collectors;`
- Line 23: `import java.util.stream.Stream;`
- Line 25: `import static org.elasticsearch.gradle.OS.WINDOWS;`
- Line 26: `import static org.elasticsearch.gradle.internal.release.PruneChangelogsTask.findAndDeleteFiles;`
- Line 27: `import static org.elasticsearch.gradle.internal.release.PruneChangelogsTask.findPreviousVersion;`
- Line 28: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 29: `import static org.hamcrest.Matchers.contains;`
- Line 30: `import static org.hamcrest.Matchers.equalTo;`
- Line 31: `import static org.junit.Assert.assertThrows;`
- Line 32: `import static org.junit.Assume.assumeFalse;`
- Line 33: `import static org.mockito.Matchers.any;`
- Line 34: `import static org.mockito.Matchers.anyString;`
- Line 35: `import static org.mockito.Mockito.mock;`
- Line 36: `import static org.mockito.Mockito.never;`
- Line 37: `import static org.mockito.Mockito.times;`
- Line 38: `import static org.mockito.Mockito.verify;`
- Line 39: `import static org.mockito.Mockito.when;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/ReleaseHighlightsGeneratorTest.java

### Unused Code (8)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Paths;`
- Line 17: `import java.util.List;`
- Line 18: `import java.util.Objects;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`
- Line 21: `import static org.junit.Assert.assertThat;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/ReleaseNotesGeneratorTest.java

### Unused Code (11)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Paths;`
- Line 17: `import java.util.ArrayList;`
- Line 18: `import java.util.HashSet;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Objects;`
- Line 21: `import java.util.Set;`
- Line 23: `import static org.hamcrest.Matchers.equalTo;`
- Line 24: `import static org.junit.Assert.assertThat;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/ReleaseNotesIndexGeneratorTest.java

### Unused Code (10)
- Line 12: `import org.junit.Test;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Paths;`
- Line 17: `import java.util.Objects;`
- Line 18: `import java.util.Set;`
- Line 19: `import java.util.stream.Collectors;`
- Line 20: `import java.util.stream.Stream;`
- Line 22: `import static org.hamcrest.Matchers.equalTo;`
- Line 23: `import static org.junit.Assert.assertThat;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/SetCompatibleVersionsTaskTests.java

### Concurrency Issue (6)
- Line 24: `final String transportVersionsJava = """`
- Line 27: `public static final TransportVersion V2 = def(200);`
- Line 28: `public static final TransportVersion V3 = def(300);`
- Line 32: `final String updatedJava = """`
- Line 37: `public static final TransportVersion V2 = def(200);`
- Line 39: `public static final TransportVersion V3 = def(300);`

### Unused Code (5)
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 15: `import org.junit.Test;`
- Line 17: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 18: `import static org.hamcrest.Matchers.hasToString;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/TagVersionsTaskTests.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.gradle.Version;`
- Line 13: `import org.junit.Test;`
- Line 15: `import java.util.ArrayList;`
- Line 16: `import java.util.Comparator;`
- Line 17: `import java.util.List;`
- Line 19: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 20: `import static org.hamcrest.Matchers.contains;`
- Line 21: `import static org.hamcrest.Matchers.is;`
- Line 22: `import static org.junit.Assert.assertThrows;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/release/UpdateVersionsTaskTests.java

### Concurrency Issue (58)
- Line 38: `final String versionJava = """`
- Line 41: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 42: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 54: `final String versionJava = """`
- Line 57: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 58: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 61: `final String updatedVersionJava = """`
- Line 66: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 68: `public static final Version V_8_10_2 = new Version(8_10_02_99);`
- Line 70: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 85: `final String versionJava = """`
- Line 88: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 89: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 92: `final String updatedVersionJava = """`
- Line 97: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 99: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 101: `public static final Version V_8_11_1 = new Version(8_11_01_99);`
- Line 116: `final String versionJava = """`
- Line 119: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 120: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 132: `final String versionJava = """`
- Line 135: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 136: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 151: `final String versionJava = """`
- Line 154: `public static final Version V_8_10_1 = new Version(8_10_01_99);`
- Line 155: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 158: `final String updatedVersionJava = """`
- Line 163: `public static final Version V_8_11_0 = new Version(8_11_00_99);`
- Line 243: `public void addTransportVersion() throws Exception {`
- Line 247: `public static final TransportVersion V_1_1_0 = def(1_001_0_00);`
- Line 248: `public static final TransportVersion V_1_2_0 = def(1_002_0_00);`
- Line 249: `public static final TransportVersion V_1_2_1 = def(1_002_0_01);`
- Line 250: `public static final TransportVersion V_1_2_2 = def(1_002_0_02);`
- Line 251: `public static final TransportVersion SOME_OTHER_VERSION = def(1_003_0_00);`
- Line 252: `public static final TransportVersion YET_ANOTHER_VERSION = def(1_004_0_00);`
- Line 255: `""";`
- Line 262: `public static final TransportVersion V_1_1_0 = def(1_001_0_00);`
- Line 264: `public static final TransportVersion V_1_2_0 = def(1_002_0_00);`
- Line 266: `public static final TransportVersion V_1_2_1 = def(1_002_0_01);`
- Line 268: `public static final TransportVersion V_1_2_2 = def(1_002_0_02);`
- Line 270: `public static final TransportVersion SOME_OTHER_VERSION = def(1_003_0_00);`
- Line 272: `public static final TransportVersion YET_ANOTHER_VERSION = def(1_004_0_00);`
- Line 274: `public static final TransportVersion NEXT_TRANSPORT_VERSION = def(1_005_0_00);`
- Line 288: `public void addTransportVersionPatch() throws Exception {`
- Line 292: `public static final TransportVersion V_1_1_0 = def(1_001_0_00);`
- Line 293: `public static final TransportVersion V_1_2_0 = def(1_002_0_00);`
- Line 294: `public static final TransportVersion V_1_2_1 = def(1_002_0_01);`
- Line 295: `public static final TransportVersion V_1_2_2 = def(1_002_0_02);`
- Line 296: `public static final TransportVersion SOME_OTHER_VERSION = def(1_003_0_00);`
- Line 297: `public static final TransportVersion YET_ANOTHER_VERSION = def(1_004_0_00);`
- Line 300: `""";`
- Line 307: `public static final TransportVersion V_1_1_0 = def(1_001_0_00);`
- Line 309: `public static final TransportVersion V_1_2_0 = def(1_002_0_00);`
- Line 311: `public static final TransportVersion V_1_2_1 = def(1_002_0_01);`
- Line 313: `public static final TransportVersion V_1_2_2 = def(1_002_0_02);`
- Line 315: `public static final TransportVersion SOME_OTHER_VERSION = def(1_003_0_00);`
- Line 317: `public static final TransportVersion PATCH_TRANSPORT_VERSION = def(1_003_0_01);`
- Line 319: `public static final TransportVersion YET_ANOTHER_VERSION = def(1_004_0_00);`

### Unused Code (18)
- Line 12: `import com.github.javaparser.StaticJavaParser;`
- Line 13: `import com.github.javaparser.ast.CompilationUnit;`
- Line 14: `import com.github.javaparser.ast.Node;`
- Line 15: `import com.github.javaparser.ast.body.FieldDeclaration;`
- Line 16: `import com.github.javaparser.printer.lexicalpreservation.LexicalPreservingPrinter;`
- Line 18: `import org.elasticsearch.gradle.Version;`
- Line 19: `import org.junit.Test;`
- Line 21: `import java.io.StringWriter;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Optional;`
- Line 26: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 27: `import static org.hamcrest.Matchers.equalTo;`
- Line 28: `import static org.hamcrest.Matchers.hasSize;`
- Line 29: `import static org.hamcrest.Matchers.hasToString;`
- Line 30: `import static org.hamcrest.Matchers.is;`
- Line 31: `import static org.junit.Assert.assertFalse;`
- Line 32: `import static org.junit.Assert.assertThrows;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/AssertObjectNodes.java

### Concurrency Issue (3)
- Line 25: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`
- Line 26: `private static final ObjectMapper MAPPER = new ObjectMapper(YAML_FACTORY);`
- Line 27: `private static final ObjectWriter WRITER = MAPPER.writerFor(ObjectNode.class);`

### Unused Code (9)
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectWriter;`
- Line 14: `import com.fasterxml.jackson.databind.SequenceWriter;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 18: `import org.junit.ComparisonFailure;`
- Line 20: `import java.io.ByteArrayOutputStream;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/TransformTests.java

### Concurrency Issue (3)
- Line 49: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`
- Line 50: `private static final ObjectMapper MAPPER = new ObjectMapper(YAML_FACTORY);`
- Line 51: `private static final ObjectReader READER = MAPPER.readerFor(ObjectNode.class);`

### Exception Handling (1)
- Line 361: `} catch (IOException e) {`

### Unused Code (31)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 14: `import com.fasterxml.jackson.databind.ObjectReader;`
- Line 15: `import com.fasterxml.jackson.databind.SequenceWriter;`
- Line 16: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 17: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 18: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 19: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 20: `import com.fasterxml.jackson.dataformat.yaml.YAMLParser;`
- Line 22: `import org.elasticsearch.gradle.internal.test.rest.transform.headers.InjectHeaders;`
- Line 23: `import org.hamcrest.CoreMatchers;`
- Line 24: `import org.hamcrest.Matchers;`
- Line 25: `import org.hamcrest.core.IsCollectionContaining;`
- Line 26: `import org.junit.Before;`
- Line 28: `import java.io.File;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.ArrayList;`
- Line 31: `import java.util.Collection;`
- Line 32: `import java.util.Collections;`
- Line 33: `import java.util.Iterator;`
- Line 34: `import java.util.LinkedList;`
- Line 35: `import java.util.List;`
- Line 36: `import java.util.Map;`
- Line 37: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 38: `import java.util.concurrent.atomic.LongAdder;`
- Line 39: `import java.util.stream.Collectors;`
- Line 41: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 42: `import static org.junit.Assert.assertEquals;`
- Line 43: `import static org.junit.Assert.assertFalse;`
- Line 44: `import static org.junit.Assert.assertNotNull;`
- Line 45: `import static org.junit.Assert.assertTrue;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/close_to/ReplaceValueInCloseToTests.java

### Concurrency Issue (1)
- Line 26: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`

### Unused Code (9)
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.databind.node.NumericNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 19: `import org.junit.Test;`
- Line 21: `import java.util.Collections;`
- Line 22: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/do_/ReplaceKeyInDoTests.java

### Unused Code (6)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.Collections;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/feature/InjectFeatureTests.java

### Unused Code (4)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 15: `import org.junit.Test;`
- Line 17: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/header/InjectHeaderTests.java

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.InjectFeatureTests;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.headers.InjectHeaders;`
- Line 17: `import org.junit.Test;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.Iterator;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.Set;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/length/ReplaceKeyInLengthTests.java

### Unused Code (6)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.Collections;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/length/ReplaceValueInLengthTests.java

### Concurrency Issue (1)
- Line 26: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`

### Unused Code (9)
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.databind.node.NumericNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 19: `import org.junit.Test;`
- Line 21: `import java.util.Collections;`
- Line 22: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/match/AddMatchTests.java

### Concurrency Issue (1)
- Line 34: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`

### Unused Code (16)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 14: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 15: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 19: `import org.hamcrest.CoreMatchers;`
- Line 20: `import org.junit.Test;`
- Line 22: `import java.util.Collections;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 26: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 27: `import static org.junit.Assert.assertEquals;`
- Line 28: `import static org.junit.Assert.assertFalse;`
- Line 29: `import static org.junit.Assert.assertThrows;`
- Line 30: `import static org.junit.Assert.assertTrue;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/match/RemoveMatchTests.java

### Unused Code (12)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.node.ArrayNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 16: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 17: `import org.hamcrest.CoreMatchers;`
- Line 18: `import org.junit.Test;`
- Line 20: `import java.util.Collections;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 24: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 25: `import static org.junit.Assert.assertFalse;`
- Line 26: `import static org.junit.Assert.assertTrue;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/match/ReplaceKeyInMatchTests.java

### Unused Code (6)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.Collections;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/match/ReplaceValueInMatchTests.java

### Concurrency Issue (1)
- Line 25: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`

### Unused Code (8)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 14: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 15: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 19: `import org.junit.Test;`
- Line 21: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/skip/SkipTests.java

### Unused Code (6)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.Collections;`
- Line 19: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/text/ReplaceTextualTests.java

### Concurrency Issue (1)
- Line 25: `private static final YAMLFactory YAML_FACTORY = new YAMLFactory();`

### Unused Code (8)
- Line 12: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 13: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import com.fasterxml.jackson.databind.node.TextNode;`
- Line 15: `import com.fasterxml.jackson.dataformat.yaml.YAMLFactory;`
- Line 17: `import org.elasticsearch.gradle.internal.test.rest.transform.AssertObjectNodes;`
- Line 18: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 19: `import org.junit.Test;`
- Line 21: `import java.util.List;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectAllowedWarningsRegexTests.java

### Unused Code (8)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.InjectFeatureTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Set;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectAllowedWarningsTests.java

### Unused Code (8)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.InjectFeatureTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Set;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectWarningsRegexTests.java

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.InjectFeatureTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Set;`
- Line 23: `import static org.junit.Assert.assertEquals;`
- Line 24: `import static org.junit.Assert.assertThrows;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/InjectWarningsTests.java

### Unused Code (10)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.feature.InjectFeatureTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Set;`
- Line 23: `import static org.junit.Assert.assertEquals;`
- Line 24: `import static org.junit.Assert.assertThrows;`

## ../build-tools-internal/src/test/java/org/elasticsearch/gradle/internal/test/rest/transform/warnings/RemoveWarningsTests.java

### Unused Code (7)
- Line 12: `import com.fasterxml.jackson.databind.node.ObjectNode;`
- Line 14: `import org.elasticsearch.gradle.internal.test.rest.transform.RestTestTransform;`
- Line 15: `import org.elasticsearch.gradle.internal.test.rest.transform.TransformTests;`
- Line 16: `import org.junit.Test;`
- Line 18: `import java.util.Collections;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Set;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/AbstractBenchmark.java

### Concurrency Issue (1)
- Line 24: `private static final int SEARCH_BENCHMARK_ITERATIONS = 10_000;`

### Unused Code (10)
- Line 11: `import org.elasticsearch.client.benchmark.ops.bulk.BulkBenchmarkTask;`
- Line 12: `import org.elasticsearch.client.benchmark.ops.bulk.BulkRequestExecutor;`
- Line 13: `import org.elasticsearch.client.benchmark.ops.search.SearchBenchmarkTask;`
- Line 14: `import org.elasticsearch.client.benchmark.ops.search.SearchRequestExecutor;`
- Line 15: `import org.elasticsearch.core.SuppressForbidden;`
- Line 17: `import java.io.Closeable;`
- Line 18: `import java.lang.management.GarbageCollectorMXBean;`
- Line 19: `import java.lang.management.ManagementFactory;`
- Line 20: `import java.util.Arrays;`
- Line 21: `import java.util.List;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/BenchmarkMain.java

### Unused Code (3)
- Line 11: `import org.elasticsearch.client.benchmark.rest.RestClientBenchmark;`
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.util.Arrays;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/BenchmarkRunner.java

### Exception Handling (1)
- Line 50: `throw new RuntimeException(ex);`

### Unused Code (8)
- Line 11: `import org.elasticsearch.client.benchmark.metrics.Metrics;`
- Line 12: `import org.elasticsearch.client.benchmark.metrics.MetricsCalculator;`
- Line 13: `import org.elasticsearch.client.benchmark.metrics.Sample;`
- Line 14: `import org.elasticsearch.client.benchmark.metrics.SampleRecorder;`
- Line 15: `import org.elasticsearch.core.SuppressForbidden;`
- Line 17: `import java.util.Arrays;`
- Line 18: `import java.util.List;`
- Line 19: `import java.util.Locale;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/BenchmarkTask.java

### Unused Code (1)
- Line 11: `import org.elasticsearch.client.benchmark.metrics.SampleRecorder;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/ops/bulk/BulkBenchmarkTask.java

### Concurrency Issue (1)
- Line 132: `private static final Logger logger = LogManager.getLogger(BulkIndexer.class);`

### Exception Handling (1)
- Line 120: `throw new ElasticsearchException(e);`

### Unused Code (22)
- Line 39: `private LoadGenerator generator;`
- Line 40: `private ExecutorService executorService;`
- Line 11: `import org.apache.logging.log4j.LogManager;`
- Line 12: `import org.apache.logging.log4j.Logger;`
- Line 13: `import org.elasticsearch.ElasticsearchException;`
- Line 14: `import org.elasticsearch.client.benchmark.BenchmarkTask;`
- Line 15: `import org.elasticsearch.client.benchmark.metrics.Sample;`
- Line 16: `import org.elasticsearch.client.benchmark.metrics.SampleRecorder;`
- Line 17: `import org.elasticsearch.core.PathUtils;`
- Line 18: `import org.elasticsearch.core.SuppressForbidden;`
- Line 20: `import java.io.BufferedReader;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.nio.charset.StandardCharsets;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.concurrent.ArrayBlockingQueue;`
- Line 28: `import java.util.concurrent.BlockingQueue;`
- Line 29: `import java.util.concurrent.ExecutorService;`
- Line 30: `import java.util.concurrent.Executors;`
- Line 31: `import java.util.concurrent.TimeUnit;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/ops/bulk/BulkRequestExecutor.java

### Unused Code (1)
- Line 11: `import java.util.List;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/ops/search/SearchBenchmarkTask.java

### Unused Code (5)
- Line 24: `private SampleRecorder sampleRecorder;`
- Line 11: `import org.elasticsearch.client.benchmark.BenchmarkTask;`
- Line 12: `import org.elasticsearch.client.benchmark.metrics.Sample;`
- Line 13: `import org.elasticsearch.client.benchmark.metrics.SampleRecorder;`
- Line 15: `import java.util.concurrent.TimeUnit;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/rest/RestClientBenchmark.java

### Exception Handling (2)
- Line 77: `throw new ElasticsearchException(e);`
- Line 99: `throw new ElasticsearchException(e);`

### Unused Code (15)
- Line 11: `import org.apache.http.HttpHeaders;`
- Line 12: `import org.apache.http.HttpHost;`
- Line 13: `import org.apache.http.HttpStatus;`
- Line 14: `import org.apache.http.message.BasicHeader;`
- Line 15: `import org.elasticsearch.ElasticsearchException;`
- Line 16: `import org.elasticsearch.client.Request;`
- Line 17: `import org.elasticsearch.client.Response;`
- Line 18: `import org.elasticsearch.client.RestClient;`
- Line 19: `import org.elasticsearch.client.benchmark.AbstractBenchmark;`
- Line 20: `import org.elasticsearch.client.benchmark.ops.bulk.BulkRequestExecutor;`
- Line 21: `import org.elasticsearch.client.benchmark.ops.search.SearchRequestExecutor;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.util.Collections;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Locale;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/metrics/MetricsCalculator.java

### Unused Code (7)
- Line 11: `import org.apache.commons.math3.stat.StatUtils;`
- Line 13: `import java.util.ArrayList;`
- Line 14: `import java.util.Collection;`
- Line 15: `import java.util.HashMap;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.concurrent.TimeUnit;`

## ../client/benchmark/src/main/java/org/elasticsearch/client/benchmark/metrics/SampleRecorder.java

### Unused Code (3)
- Line 11: `import java.util.ArrayList;`
- Line 12: `import java.util.Collections;`
- Line 13: `import java.util.List;`

## ../client/client-benchmark-noop-api-plugin/src/main/java/org/elasticsearch/plugin/noop/NoopPlugin.java

### Unused Code (25)
- Line 11: `import org.elasticsearch.action.ActionRequest;`
- Line 12: `import org.elasticsearch.action.ActionResponse;`
- Line 13: `import org.elasticsearch.action.ActionType;`
- Line 14: `import org.elasticsearch.action.bulk.BulkResponse;`
- Line 15: `import org.elasticsearch.action.search.SearchResponse;`
- Line 16: `import org.elasticsearch.cluster.metadata.IndexNameExpressionResolver;`
- Line 17: `import org.elasticsearch.cluster.node.DiscoveryNodes;`
- Line 18: `import org.elasticsearch.common.io.stream.NamedWriteableRegistry;`
- Line 19: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 20: `import org.elasticsearch.common.settings.IndexScopedSettings;`
- Line 21: `import org.elasticsearch.common.settings.Settings;`
- Line 22: `import org.elasticsearch.common.settings.SettingsFilter;`
- Line 23: `import org.elasticsearch.features.NodeFeature;`
- Line 24: `import org.elasticsearch.plugin.noop.action.bulk.RestNoopBulkAction;`
- Line 25: `import org.elasticsearch.plugin.noop.action.bulk.TransportNoopBulkAction;`
- Line 26: `import org.elasticsearch.plugin.noop.action.search.RestNoopSearchAction;`
- Line 27: `import org.elasticsearch.plugin.noop.action.search.TransportNoopSearchAction;`
- Line 28: `import org.elasticsearch.plugins.ActionPlugin;`
- Line 29: `import org.elasticsearch.plugins.Plugin;`
- Line 30: `import org.elasticsearch.rest.RestController;`
- Line 31: `import org.elasticsearch.rest.RestHandler;`
- Line 33: `import java.util.Arrays;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.function.Predicate;`
- Line 36: `import java.util.function.Supplier;`

## ../client/client-benchmark-noop-api-plugin/src/main/java/org/elasticsearch/plugin/noop/action/bulk/RestNoopBulkAction.java

### Concurrency Issue (1)
- Line 89: `private final BulkItemResponse ITEM_RESPONSE = BulkItemResponse.success(`

### Unused Code (20)
- Line 11: `import org.elasticsearch.action.DocWriteRequest;`
- Line 12: `import org.elasticsearch.action.DocWriteResponse;`
- Line 13: `import org.elasticsearch.action.bulk.BulkItemResponse;`
- Line 14: `import org.elasticsearch.action.bulk.BulkRequest;`
- Line 15: `import org.elasticsearch.action.bulk.BulkShardRequest;`
- Line 16: `import org.elasticsearch.action.support.ActiveShardCount;`
- Line 17: `import org.elasticsearch.action.update.UpdateResponse;`
- Line 18: `import org.elasticsearch.client.internal.node.NodeClient;`
- Line 19: `import org.elasticsearch.index.shard.ShardId;`
- Line 20: `import org.elasticsearch.rest.BaseRestHandler;`
- Line 21: `import org.elasticsearch.rest.RestChannel;`
- Line 22: `import org.elasticsearch.rest.RestRequest;`
- Line 23: `import org.elasticsearch.rest.RestResponse;`
- Line 24: `import org.elasticsearch.rest.action.RestBuilderListener;`
- Line 25: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.util.List;`
- Line 30: `import static org.elasticsearch.rest.RestRequest.Method.POST;`
- Line 31: `import static org.elasticsearch.rest.RestRequest.Method.PUT;`
- Line 32: `import static org.elasticsearch.rest.RestStatus.OK;`

## ../client/client-benchmark-noop-api-plugin/src/main/java/org/elasticsearch/plugin/noop/action/bulk/TransportNoopBulkAction.java

### Unused Code (15)
- Line 11: `import org.elasticsearch.action.ActionListener;`
- Line 12: `import org.elasticsearch.action.DocWriteRequest;`
- Line 13: `import org.elasticsearch.action.DocWriteResponse;`
- Line 14: `import org.elasticsearch.action.bulk.BulkItemResponse;`
- Line 15: `import org.elasticsearch.action.bulk.BulkRequest;`
- Line 16: `import org.elasticsearch.action.bulk.BulkResponse;`
- Line 17: `import org.elasticsearch.action.support.ActionFilters;`
- Line 18: `import org.elasticsearch.action.support.HandledTransportAction;`
- Line 19: `import org.elasticsearch.action.update.UpdateResponse;`
- Line 20: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 21: `import org.elasticsearch.index.shard.ShardId;`
- Line 22: `import org.elasticsearch.injection.guice.Inject;`
- Line 23: `import org.elasticsearch.plugin.noop.NoopPlugin;`
- Line 24: `import org.elasticsearch.tasks.Task;`
- Line 25: `import org.elasticsearch.transport.TransportService;`

## ../client/client-benchmark-noop-api-plugin/src/main/java/org/elasticsearch/plugin/noop/action/search/RestNoopSearchAction.java

### Unused Code (9)
- Line 11: `import org.elasticsearch.action.search.SearchRequest;`
- Line 12: `import org.elasticsearch.client.internal.node.NodeClient;`
- Line 13: `import org.elasticsearch.plugin.noop.NoopPlugin;`
- Line 14: `import org.elasticsearch.rest.BaseRestHandler;`
- Line 15: `import org.elasticsearch.rest.RestRequest;`
- Line 16: `import org.elasticsearch.rest.action.RestRefCountedChunkedToXContentListener;`
- Line 18: `import java.util.List;`
- Line 20: `import static org.elasticsearch.rest.RestRequest.Method.GET;`
- Line 21: `import static org.elasticsearch.rest.RestRequest.Method.POST;`

## ../client/client-benchmark-noop-api-plugin/src/main/java/org/elasticsearch/plugin/noop/action/search/TransportNoopSearchAction.java

### Unused Code (17)
- Line 11: `import org.elasticsearch.action.ActionListener;`
- Line 12: `import org.elasticsearch.action.search.SearchRequest;`
- Line 13: `import org.elasticsearch.action.search.SearchResponse;`
- Line 14: `import org.elasticsearch.action.search.ShardSearchFailure;`
- Line 15: `import org.elasticsearch.action.support.ActionFilters;`
- Line 16: `import org.elasticsearch.action.support.HandledTransportAction;`
- Line 17: `import org.elasticsearch.common.io.stream.Writeable;`
- Line 18: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 19: `import org.elasticsearch.injection.guice.Inject;`
- Line 20: `import org.elasticsearch.plugin.noop.NoopPlugin;`
- Line 21: `import org.elasticsearch.search.SearchHits;`
- Line 22: `import org.elasticsearch.search.aggregations.InternalAggregations;`
- Line 23: `import org.elasticsearch.search.profile.SearchProfileResults;`
- Line 24: `import org.elasticsearch.search.suggest.Suggest;`
- Line 25: `import org.elasticsearch.tasks.Task;`
- Line 26: `import org.elasticsearch.transport.TransportService;`
- Line 28: `import java.util.Collections;`

## ../client/rest/src/main/java/org/elasticsearch/client/Cancellable.java

### Exception Handling (1)
- Line 52: `throw new UnsupportedOperationException();`

### Unused Code (3)
- Line 21: `import org.apache.http.client.methods.AbstractExecutionAwareRequest;`
- Line 22: `import org.apache.http.client.methods.HttpRequestBase;`
- Line 24: `import java.util.concurrent.CancellationException;`

## ../client/rest/src/main/java/org/elasticsearch/client/DeadHostState.java

### Exception Handling (1)
- Line 94: `throw new IllegalArgumentException(`

### Unused Code (2)
- Line 22: `import java.util.concurrent.TimeUnit;`
- Line 23: `import java.util.function.Supplier;`

## ../client/rest/src/main/java/org/elasticsearch/client/HasAttributeNodeSelector.java

### Unused Code (4)
- Line 22: `import java.util.Iterator;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Objects;`

## ../client/rest/src/main/java/org/elasticsearch/client/HeapBufferedAsyncResponseConsumer.java

### Exception Handling (2)
- Line 55: `throw new IllegalArgumentException("bufferLimit must be greater than 0");`
- Line 76: `throw new ContentTooLongException(`

### Unused Code (14)
- Line 22: `import org.apache.http.ContentTooLongException;`
- Line 23: `import org.apache.http.HttpEntity;`
- Line 24: `import org.apache.http.HttpException;`
- Line 25: `import org.apache.http.HttpResponse;`
- Line 26: `import org.apache.http.entity.ContentType;`
- Line 27: `import org.apache.http.nio.ContentDecoder;`
- Line 28: `import org.apache.http.nio.IOControl;`
- Line 29: `import org.apache.http.nio.entity.ContentBufferEntity;`
- Line 30: `import org.apache.http.nio.protocol.AbstractAsyncResponseConsumer;`
- Line 31: `import org.apache.http.nio.util.ByteBufferAllocator;`
- Line 32: `import org.apache.http.nio.util.HeapByteBufferAllocator;`
- Line 33: `import org.apache.http.nio.util.SimpleInputBuffer;`
- Line 34: `import org.apache.http.protocol.HttpContext;`
- Line 36: `import java.io.IOException;`

## ../client/rest/src/main/java/org/elasticsearch/client/HttpAsyncResponseConsumerFactory.java

### Concurrency Issue (1)
- Line 52: `static final int DEFAULT_BUFFER_LIMIT = 100 * 1024 * 1024;`

### Unused Code (3)
- Line 22: `import org.apache.http.HttpResponse;`
- Line 23: `import org.apache.http.nio.protocol.HttpAsyncResponseConsumer;`
- Line 25: `import static org.elasticsearch.client.HttpAsyncResponseConsumerFactory.HeapBufferedResponseConsumerFactory.DEFAULT_BUFFER_LIMIT;`

## ../client/rest/src/main/java/org/elasticsearch/client/HttpDeleteWithEntity.java

### Unused Code (3)
- Line 21: `import org.apache.http.client.methods.HttpDelete;`
- Line 22: `import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;`
- Line 24: `import java.net.URI;`

## ../client/rest/src/main/java/org/elasticsearch/client/HttpGetWithEntity.java

### Unused Code (3)
- Line 21: `import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;`
- Line 22: `import org.apache.http.client.methods.HttpGet;`
- Line 24: `import java.net.URI;`

## ../client/rest/src/main/java/org/elasticsearch/client/LanguageRuntimeVersions.java

### Unused Code (2)
- Line 22: `import java.lang.reflect.Field;`
- Line 23: `import java.lang.reflect.Method;`

## ../client/rest/src/main/java/org/elasticsearch/client/Node.java

### Exception Handling (1)
- Line 70: `throw new IllegalArgumentException("host cannot be null");`

### Unused Code (6)
- Line 22: `import org.apache.http.HttpHost;`
- Line 24: `import java.util.List;`
- Line 25: `import java.util.Map;`
- Line 26: `import java.util.Objects;`
- Line 27: `import java.util.Set;`
- Line 28: `import java.util.TreeSet;`

## ../client/rest/src/main/java/org/elasticsearch/client/NodeSelector.java

### Unused Code (1)
- Line 22: `import java.util.Iterator;`

## ../client/rest/src/main/java/org/elasticsearch/client/PersistentCredentialsAuthenticationStrategy.java

### Unused Code (6)
- Line 22: `import org.apache.commons.logging.Log;`
- Line 23: `import org.apache.commons.logging.LogFactory;`
- Line 24: `import org.apache.http.HttpHost;`
- Line 25: `import org.apache.http.auth.AuthScheme;`
- Line 26: `import org.apache.http.impl.client.TargetAuthenticationStrategy;`
- Line 27: `import org.apache.http.protocol.HttpContext;`

## ../client/rest/src/main/java/org/elasticsearch/client/PreferHasAttributeNodeSelector.java

### Unused Code (4)
- Line 22: `import java.util.Iterator;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Objects;`

## ../client/rest/src/main/java/org/elasticsearch/client/Request.java

### Concurrency Issue (3)
- Line 101: `public void setEntity(HttpEntity entity) {`
- Line 128: `public void setOptions(RequestOptions options) {`
- Line 137: `public void setOptions(RequestOptions.Builder options) {`

### Unused Code (9)
- Line 40: `private HttpEntity entity;`
- Line 41: `private RequestOptions options = RequestOptions.DEFAULT;`
- Line 22: `import org.apache.http.HttpEntity;`
- Line 23: `import org.apache.http.entity.ContentType;`
- Line 24: `import org.apache.http.nio.entity.NStringEntity;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.Map;`
- Line 28: `import java.util.Objects;`
- Line 30: `import static java.util.Collections.unmodifiableMap;`

## ../client/rest/src/main/java/org/elasticsearch/client/RequestLogger.java

### Resource Leak (1)
- Line 171: `try (BufferedReader reader = new BufferedReader(new InputStreamReader(entity.getContent(), charset))) {`

### Concurrency Issue (1)
- Line 49: `private static final Log tracer = LogFactory.getLog("tracer");`

### Unused Code (17)
- Line 22: `import org.apache.commons.logging.Log;`
- Line 23: `import org.apache.commons.logging.LogFactory;`
- Line 24: `import org.apache.http.Header;`
- Line 25: `import org.apache.http.HttpEntity;`
- Line 26: `import org.apache.http.HttpEntityEnclosingRequest;`
- Line 27: `import org.apache.http.HttpHost;`
- Line 28: `import org.apache.http.HttpResponse;`
- Line 29: `import org.apache.http.RequestLine;`
- Line 30: `import org.apache.http.client.methods.HttpUriRequest;`
- Line 31: `import org.apache.http.entity.BufferedHttpEntity;`
- Line 32: `import org.apache.http.entity.ContentType;`
- Line 33: `import org.apache.http.util.EntityUtils;`
- Line 35: `import java.io.BufferedReader;`
- Line 36: `import java.io.IOException;`
- Line 37: `import java.io.InputStreamReader;`
- Line 38: `import java.nio.charset.Charset;`
- Line 39: `import java.nio.charset.StandardCharsets;`

## ../client/rest/src/main/java/org/elasticsearch/client/RequestOptions.java

### Concurrency Issue (1)
- Line 43: `public static final RequestOptions DEFAULT = new Builder(`

### Unused Code (14)
- Line 186: `private HttpAsyncResponseConsumerFactory httpAsyncResponseConsumerFactory;`
- Line 187: `private WarningsHandler warningsHandler;`
- Line 188: `private RequestConfig requestConfig;`
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.client.config.RequestConfig;`
- Line 24: `import org.apache.http.message.BasicHeader;`
- Line 25: `import org.apache.http.nio.protocol.HttpAsyncResponseConsumer;`
- Line 26: `import org.elasticsearch.client.HttpAsyncResponseConsumerFactory.HeapBufferedResponseConsumerFactory;`
- Line 28: `import java.util.ArrayList;`
- Line 29: `import java.util.Collections;`
- Line 30: `import java.util.HashMap;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.Objects;`

## ../client/rest/src/main/java/org/elasticsearch/client/Response.java

### Unused Code (11)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.HttpEntity;`
- Line 24: `import org.apache.http.HttpHost;`
- Line 25: `import org.apache.http.HttpResponse;`
- Line 26: `import org.apache.http.RequestLine;`
- Line 27: `import org.apache.http.StatusLine;`
- Line 29: `import java.util.ArrayList;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Objects;`
- Line 32: `import java.util.regex.Matcher;`
- Line 33: `import java.util.regex.Pattern;`

## ../client/rest/src/main/java/org/elasticsearch/client/ResponseException.java

### Unused Code (5)
- Line 22: `import org.apache.http.HttpEntity;`
- Line 23: `import org.apache.http.entity.BufferedHttpEntity;`
- Line 24: `import org.apache.http.util.EntityUtils;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.util.Locale;`

## ../client/rest/src/main/java/org/elasticsearch/client/RestClient.java

### Null Pointer (1)
- Line 892: `this.response = null;`

### Concurrency Issue (4)
- Line 693: `*/`
- Line 111: `public static final String IGNORE_RESPONSE_CODES_PARAM = "ignore";`
- Line 113: `private static final Log logger = LogFactory.getLog(RestClient.class);`
- Line 120: `private final AtomicInteger lastNodeIndex = new AtomicInteger(0);`

### Exception Handling (11)
- Line 163: `throw new IllegalStateException("cloudId " + cloudId + " must begin with a human readable identifier followed by a colon");`
- Line 173: `throw new IllegalStateException("cloudId " + cloudId + " did not decode to a cluster identifier correctly");`
- Line 185: `throw new IllegalStateException("cloudId " + cloudId + " does not contain a valid port number");`
- Line 216: `throw new IllegalArgumentException("hosts must not be null nor empty");`
- Line 234: `throw new IllegalArgumentException("nodes must not be null or empty");`
- Line 315: `throw new IllegalStateException("unexpected exception type: must be either RuntimeException or IOException", cause);`
- Line 347: `throw new WarningFailureException(response);`
- Line 520: `throw new IOException("NodeSelector [" + nodeSelector + "] rejected all nodes, living " + livingNodes + " and dead " + deadNodes);`
- Line 619: `throw new UnsupportedOperationException("http method not supported: " + method);`
- Line 874: `throw new IllegalArgumentException("ignore value should be a number, found [" + ignoreString + "] instead", e);`
- Line 903: `throw new RuntimeException("thread waiting for the response was interrupted", exception);`

### Infinite Loop (1)
- Line 539: `while (true) {`

### Unused Code (67)
- Line 21: `import org.apache.commons.logging.Log;`
- Line 22: `import org.apache.commons.logging.LogFactory;`
- Line 23: `import org.apache.http.ConnectionClosedException;`
- Line 24: `import org.apache.http.ContentTooLongException;`
- Line 25: `import org.apache.http.Header;`
- Line 26: `import org.apache.http.HttpEntity;`
- Line 27: `import org.apache.http.HttpHost;`
- Line 28: `import org.apache.http.HttpRequest;`
- Line 29: `import org.apache.http.HttpResponse;`
- Line 30: `import org.apache.http.client.AuthCache;`
- Line 31: `import org.apache.http.client.ClientProtocolException;`
- Line 32: `import org.apache.http.client.config.RequestConfig;`
- Line 33: `import org.apache.http.client.entity.GzipCompressingEntity;`
- Line 34: `import org.apache.http.client.entity.GzipDecompressingEntity;`
- Line 35: `import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;`
- Line 36: `import org.apache.http.client.methods.HttpHead;`
- Line 37: `import org.apache.http.client.methods.HttpOptions;`
- Line 38: `import org.apache.http.client.methods.HttpPatch;`
- Line 39: `import org.apache.http.client.methods.HttpPost;`
- Line 40: `import org.apache.http.client.methods.HttpPut;`
- Line 41: `import org.apache.http.client.methods.HttpRequestBase;`
- Line 42: `import org.apache.http.client.methods.HttpTrace;`
- Line 43: `import org.apache.http.client.protocol.HttpClientContext;`
- Line 44: `import org.apache.http.client.utils.URIBuilder;`
- Line 45: `import org.apache.http.concurrent.FutureCallback;`
- Line 46: `import org.apache.http.conn.ConnectTimeoutException;`
- Line 47: `import org.apache.http.impl.auth.BasicScheme;`
- Line 48: `import org.apache.http.impl.client.BasicAuthCache;`
- Line 49: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 50: `import org.apache.http.nio.client.HttpAsyncClient;`
- Line 51: `import org.apache.http.nio.client.methods.HttpAsyncMethods;`
- Line 52: `import org.apache.http.nio.protocol.HttpAsyncRequestProducer;`
- Line 53: `import org.apache.http.nio.protocol.HttpAsyncResponseConsumer;`
- Line 54: `import org.apache.http.protocol.HTTP;`
- Line 56: `import java.io.ByteArrayInputStream;`
- Line 57: `import java.io.ByteArrayOutputStream;`
- Line 58: `import java.io.Closeable;`
- Line 59: `import java.io.IOException;`
- Line 60: `import java.io.InputStream;`
- Line 61: `import java.net.ConnectException;`
- Line 62: `import java.net.SocketTimeoutException;`
- Line 63: `import java.net.URI;`
- Line 64: `import java.net.URISyntaxException;`
- Line 65: `import java.util.ArrayList;`
- Line 66: `import java.util.Arrays;`
- Line 67: `import java.util.Base64;`
- Line 68: `import java.util.Collection;`
- Line 69: `import java.util.Collections;`
- Line 70: `import java.util.HashMap;`
- Line 71: `import java.util.HashSet;`
- Line 72: `import java.util.Iterator;`
- Line 73: `import java.util.LinkedHashMap;`
- Line 74: `import java.util.List;`
- Line 75: `import java.util.Locale;`
- Line 76: `import java.util.Map;`
- Line 77: `import java.util.Objects;`
- Line 78: `import java.util.Set;`
- Line 79: `import java.util.concurrent.ConcurrentHashMap;`
- Line 80: `import java.util.concurrent.ConcurrentMap;`
- Line 81: `import java.util.concurrent.ExecutionException;`
- Line 82: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 83: `import java.util.stream.Collectors;`
- Line 84: `import java.util.zip.GZIPOutputStream;`
- Line 86: `import javax.net.ssl.SSLHandshakeException;`
- Line 88: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 89: `import static java.util.Collections.singletonList;`
- Line 90: `import static org.elasticsearch.client.RestClient.IGNORE_RESPONSE_CODES_PARAM;`

## ../client/rest/src/main/java/org/elasticsearch/client/RestClientBuilder.java

### Concurrency Issue (10)
- Line 51: `public static final int DEFAULT_CONNECT_TIMEOUT_MILLIS = 1000;`
- Line 52: `public static final int DEFAULT_SOCKET_TIMEOUT_MILLIS = 30000;`
- Line 53: `public static final int DEFAULT_MAX_CONN_PER_ROUTE = 10;`
- Line 56: `static final String THREAD_NAME_PREFIX = "elasticsearch-rest-client-";`
- Line 57: `private static final String THREAD_NAME_FORMAT = THREAD_NAME_PREFIX + "%d-thread-%d";`
- Line 72: `private NodeSelector nodeSelector = NodeSelector.ANY;`
- Line 73: `private boolean strictDeprecationMode = false;`
- Line 74: `private boolean compressionEnabled = false;`
- Line 310: `private static final AtomicLong CLIENT_THREAD_POOL_ID_GENERATOR = new AtomicLong();`
- Line 312: `private final long clientThreadPoolId = CLIENT_THREAD_POOL_ID_GENERATOR.getAndIncrement(); // 0-based`

### Exception Handling (5)
- Line 143: `throw new IllegalArgumentException("nodes must not be null or empty");`
- Line 147: `throw new IllegalArgumentException("node cannot be null");`
- Line 223: `throw new IllegalArgumentException("pathPrefix must not be empty");`
- Line 236: `throw new IllegalArgumentException("pathPrefix is malformed. too many trailing slashes: [" + pathPrefix + "]");`
- Line 350: `throw new IllegalStateException("could not create the default ssl context", e);`

### Unused Code (27)
- Line 69: `private HttpClientConfigCallback httpClientConfigCallback;`
- Line 70: `private RequestConfigCallback requestConfigCallback;`
- Line 71: `private String pathPrefix;`
- Line 72: `private NodeSelector nodeSelector = NodeSelector.ANY;`
- Line 73: `private boolean strictDeprecationMode = false;`
- Line 74: `private boolean compressionEnabled = false;`
- Line 75: `private boolean metaHeaderEnabled = true;`
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.client.config.RequestConfig;`
- Line 24: `import org.apache.http.impl.client.CloseableHttpClient;`
- Line 25: `import org.apache.http.impl.client.HttpClientBuilder;`
- Line 26: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 27: `import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;`
- Line 28: `import org.apache.http.nio.conn.SchemeIOSessionStrategy;`
- Line 29: `import org.apache.http.util.VersionInfo;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.io.InputStream;`
- Line 33: `import java.security.AccessController;`
- Line 34: `import java.security.NoSuchAlgorithmException;`
- Line 35: `import java.security.PrivilegedAction;`
- Line 36: `import java.util.List;`
- Line 37: `import java.util.Locale;`
- Line 38: `import java.util.Objects;`
- Line 39: `import java.util.Properties;`
- Line 40: `import java.util.concurrent.ThreadFactory;`
- Line 41: `import java.util.concurrent.atomic.AtomicLong;`
- Line 43: `import javax.net.ssl.SSLContext;`

## ../client/rest/src/main/java/org/elasticsearch/client/WarningFailureException.java

### Unused Code (2)
- Line 22: `import java.io.IOException;`
- Line 24: `import static org.elasticsearch.client.ResponseException.buildMessage;`

## ../client/rest/src/main/java/org/elasticsearch/client/WarningsHandler.java

### Unused Code (1)
- Line 22: `import java.util.List;`

## ../client/rest/src/test/java/org/elasticsearch/client/DeadHostStateTests.java

### Unused Code (10)
- Line 22: `import java.util.concurrent.TimeUnit;`
- Line 23: `import java.util.concurrent.atomic.AtomicLong;`
- Line 25: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 26: `import static org.hamcrest.Matchers.equalTo;`
- Line 27: `import static org.hamcrest.Matchers.greaterThan;`
- Line 28: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`
- Line 29: `import static org.hamcrest.Matchers.is;`
- Line 30: `import static org.hamcrest.Matchers.lessThan;`
- Line 31: `import static org.junit.Assert.assertEquals;`
- Line 32: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/FailureTrackingResponseListenerTests.java

### Exception Handling (2)
- Line 92: `throw new IllegalStateException("onSuccess was called multiple times");`
- Line 99: `throw new IllegalStateException("onFailure was called multiple times");`

### Unused Code (13)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.apache.http.HttpResponse;`
- Line 24: `import org.apache.http.ProtocolVersion;`
- Line 25: `import org.apache.http.RequestLine;`
- Line 26: `import org.apache.http.StatusLine;`
- Line 27: `import org.apache.http.message.BasicHttpResponse;`
- Line 28: `import org.apache.http.message.BasicRequestLine;`
- Line 29: `import org.apache.http.message.BasicStatusLine;`
- Line 31: `import java.util.concurrent.atomic.AtomicReference;`
- Line 33: `import static org.junit.Assert.assertEquals;`
- Line 34: `import static org.junit.Assert.assertNotNull;`
- Line 35: `import static org.junit.Assert.assertNull;`
- Line 36: `import static org.junit.Assert.assertSame;`

## ../client/rest/src/test/java/org/elasticsearch/client/HasAttributeNodeSelectorTests.java

### Unused Code (12)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node.Roles;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.Arrays;`
- Line 27: `import java.util.Collections;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Set;`
- Line 31: `import java.util.TreeSet;`
- Line 33: `import static java.util.Collections.singletonList;`
- Line 34: `import static java.util.Collections.singletonMap;`
- Line 35: `import static org.junit.Assert.assertEquals;`

## ../client/rest/src/test/java/org/elasticsearch/client/HeapBufferedAsyncResponseConsumerTests.java

### Concurrency Issue (2)
- Line 54: `private static final int MAX_TEST_BUFFER_SIZE = 50 * 1024 * 1024;`
- Line 55: `private static final int TEST_BUFFER_LIMIT = 10 * 1024 * 1024;`

### Unused Code (26)
- Line 22: `import org.apache.http.ContentTooLongException;`
- Line 23: `import org.apache.http.HttpEntity;`
- Line 24: `import org.apache.http.HttpResponse;`
- Line 25: `import org.apache.http.ProtocolVersion;`
- Line 26: `import org.apache.http.StatusLine;`
- Line 27: `import org.apache.http.entity.ContentType;`
- Line 28: `import org.apache.http.entity.StringEntity;`
- Line 29: `import org.apache.http.message.BasicHttpResponse;`
- Line 30: `import org.apache.http.message.BasicStatusLine;`
- Line 31: `import org.apache.http.nio.ContentDecoder;`
- Line 32: `import org.apache.http.nio.IOControl;`
- Line 33: `import org.apache.http.nio.protocol.HttpAsyncResponseConsumer;`
- Line 34: `import org.apache.http.protocol.HttpContext;`
- Line 36: `import java.lang.reflect.Constructor;`
- Line 37: `import java.lang.reflect.InvocationTargetException;`
- Line 38: `import java.lang.reflect.Modifier;`
- Line 39: `import java.util.concurrent.atomic.AtomicReference;`
- Line 41: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 42: `import static org.junit.Assert.assertEquals;`
- Line 43: `import static org.junit.Assert.assertSame;`
- Line 44: `import static org.junit.Assert.assertThat;`
- Line 45: `import static org.junit.Assert.assertTrue;`
- Line 46: `import static org.mockito.Mockito.mock;`
- Line 47: `import static org.mockito.Mockito.spy;`
- Line 48: `import static org.mockito.Mockito.times;`
- Line 49: `import static org.mockito.Mockito.verify;`

## ../client/rest/src/test/java/org/elasticsearch/client/HostsTrackingFailureListener.java

### Unused Code (7)
- Line 22: `import org.apache.http.HttpHost;`
- Line 24: `import java.util.HashSet;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Set;`
- Line 28: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 29: `import static org.junit.Assert.assertEquals;`
- Line 30: `import static org.junit.Assert.assertThat;`

## ../client/rest/src/test/java/org/elasticsearch/client/NodeSelectorTests.java

### Unused Code (8)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node.Roles;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.Collections;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.TreeSet;`
- Line 31: `import static org.junit.Assert.assertEquals;`

## ../client/rest/src/test/java/org/elasticsearch/client/NodeTests.java

### Unused Code (15)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node.Roles;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.Collections;`
- Line 27: `import java.util.HashMap;`
- Line 28: `import java.util.HashSet;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Map;`
- Line 31: `import java.util.TreeSet;`
- Line 33: `import static java.util.Collections.singleton;`
- Line 34: `import static java.util.Collections.singletonList;`
- Line 35: `import static java.util.Collections.singletonMap;`
- Line 36: `import static org.junit.Assert.assertEquals;`
- Line 37: `import static org.junit.Assert.assertFalse;`
- Line 38: `import static org.junit.Assert.assertTrue;`

## ../client/rest/src/test/java/org/elasticsearch/client/PreferHasAttributeNodeSelectorTests.java

### Unused Code (12)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node.Roles;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.Arrays;`
- Line 27: `import java.util.Collections;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Set;`
- Line 31: `import java.util.TreeSet;`
- Line 33: `import static java.util.Collections.singletonList;`
- Line 34: `import static java.util.Collections.singletonMap;`
- Line 35: `import static org.junit.Assert.assertEquals;`

## ../client/rest/src/test/java/org/elasticsearch/client/RequestLoggerTests.java

### Exception Handling (3)
- Line 94: `throw new UnsupportedOperationException();`
- Line 143: `throw new UnsupportedOperationException();`
- Line 198: `throw new UnsupportedOperationException();`

### Unused Code (30)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.HttpEntity;`
- Line 24: `import org.apache.http.HttpEntityEnclosingRequest;`
- Line 25: `import org.apache.http.HttpHost;`
- Line 26: `import org.apache.http.ProtocolVersion;`
- Line 27: `import org.apache.http.client.methods.HttpHead;`
- Line 28: `import org.apache.http.client.methods.HttpOptions;`
- Line 29: `import org.apache.http.client.methods.HttpPatch;`
- Line 30: `import org.apache.http.client.methods.HttpPost;`
- Line 31: `import org.apache.http.client.methods.HttpPut;`
- Line 32: `import org.apache.http.client.methods.HttpTrace;`
- Line 33: `import org.apache.http.client.methods.HttpUriRequest;`
- Line 34: `import org.apache.http.entity.ContentType;`
- Line 35: `import org.apache.http.entity.InputStreamEntity;`
- Line 36: `import org.apache.http.entity.StringEntity;`
- Line 37: `import org.apache.http.message.BasicHeader;`
- Line 38: `import org.apache.http.message.BasicHttpResponse;`
- Line 39: `import org.apache.http.message.BasicStatusLine;`
- Line 40: `import org.apache.http.nio.entity.NByteArrayEntity;`
- Line 41: `import org.apache.http.nio.entity.NStringEntity;`
- Line 42: `import org.apache.http.util.EntityUtils;`
- Line 44: `import java.io.ByteArrayInputStream;`
- Line 45: `import java.io.IOException;`
- Line 46: `import java.net.URI;`
- Line 47: `import java.net.URISyntaxException;`
- Line 48: `import java.nio.charset.Charset;`
- Line 49: `import java.nio.charset.StandardCharsets;`
- Line 51: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 52: `import static org.junit.Assert.assertEquals;`
- Line 53: `import static org.junit.Assert.assertThat;`

## ../client/rest/src/test/java/org/elasticsearch/client/RequestOptionsTests.java

### Exception Handling (1)
- Line 205: `throw new UnsupportedOperationException("Unknown mutation type [" + mutationType + "]");`

### Unused Code (14)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.client.config.RequestConfig;`
- Line 24: `import org.elasticsearch.client.HttpAsyncResponseConsumerFactory.HeapBufferedResponseConsumerFactory;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Collections;`
- Line 28: `import java.util.HashMap;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Map;`
- Line 32: `import static org.junit.Assert.assertEquals;`
- Line 33: `import static org.junit.Assert.assertNotEquals;`
- Line 34: `import static org.junit.Assert.assertNull;`
- Line 35: `import static org.junit.Assert.assertSame;`
- Line 36: `import static org.junit.Assert.fail;`
- Line 37: `import static org.mockito.Mockito.mock;`

## ../client/rest/src/test/java/org/elasticsearch/client/RequestTests.java

### Exception Handling (1)
- Line 237: `throw new UnsupportedOperationException("Unknown mutation type [" + mutationType + "]");`

### Unused Code (15)
- Line 22: `import org.apache.http.HttpEntity;`
- Line 23: `import org.apache.http.entity.ByteArrayEntity;`
- Line 24: `import org.apache.http.entity.ContentType;`
- Line 25: `import org.apache.http.entity.StringEntity;`
- Line 26: `import org.apache.http.nio.entity.NStringEntity;`
- Line 27: `import org.elasticsearch.client.HttpAsyncResponseConsumerFactory.HeapBufferedResponseConsumerFactory;`
- Line 29: `import java.io.ByteArrayOutputStream;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.util.HashMap;`
- Line 32: `import java.util.Map;`
- Line 34: `import static org.junit.Assert.assertEquals;`
- Line 35: `import static org.junit.Assert.assertNotEquals;`
- Line 36: `import static org.junit.Assert.assertNull;`
- Line 37: `import static org.junit.Assert.assertSame;`
- Line 38: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/ResponseExceptionTests.java

### Unused Code (20)
- Line 22: `import org.apache.http.HttpEntity;`
- Line 23: `import org.apache.http.HttpHost;`
- Line 24: `import org.apache.http.HttpResponse;`
- Line 25: `import org.apache.http.ProtocolVersion;`
- Line 26: `import org.apache.http.RequestLine;`
- Line 27: `import org.apache.http.StatusLine;`
- Line 28: `import org.apache.http.entity.ContentType;`
- Line 29: `import org.apache.http.entity.InputStreamEntity;`
- Line 30: `import org.apache.http.entity.StringEntity;`
- Line 31: `import org.apache.http.message.BasicHttpResponse;`
- Line 32: `import org.apache.http.message.BasicRequestLine;`
- Line 33: `import org.apache.http.message.BasicStatusLine;`
- Line 34: `import org.apache.http.util.EntityUtils;`
- Line 36: `import java.io.ByteArrayInputStream;`
- Line 37: `import java.io.IOException;`
- Line 38: `import java.nio.charset.StandardCharsets;`
- Line 39: `import java.util.Locale;`
- Line 41: `import static org.junit.Assert.assertEquals;`
- Line 42: `import static org.junit.Assert.assertNull;`
- Line 43: `import static org.junit.Assert.assertSame;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientBuilderIntegTests.java

### Exception Handling (1)
- Line 201: `throw new IllegalArgumentException("Java version string [" + version + "] could not be parsed.");`

### Unused Code (35)
- Line 22: `import com.sun.net.httpserver.HttpExchange;`
- Line 23: `import com.sun.net.httpserver.HttpHandler;`
- Line 24: `import com.sun.net.httpserver.HttpsConfigurator;`
- Line 25: `import com.sun.net.httpserver.HttpsServer;`
- Line 27: `import org.apache.http.HttpHost;`
- Line 28: `import org.elasticsearch.mocksocket.MockHttpServer;`
- Line 29: `import org.junit.AfterClass;`
- Line 30: `import org.junit.BeforeClass;`
- Line 32: `import java.io.IOException;`
- Line 33: `import java.io.InputStream;`
- Line 34: `import java.net.InetAddress;`
- Line 35: `import java.net.InetSocketAddress;`
- Line 36: `import java.nio.file.Files;`
- Line 37: `import java.nio.file.Paths;`
- Line 38: `import java.security.AccessController;`
- Line 39: `import java.security.KeyFactory;`
- Line 40: `import java.security.KeyStore;`
- Line 41: `import java.security.PrivilegedAction;`
- Line 42: `import java.security.cert.Certificate;`
- Line 43: `import java.security.cert.CertificateFactory;`
- Line 44: `import java.security.spec.PKCS8EncodedKeySpec;`
- Line 45: `import java.util.concurrent.CountDownLatch;`
- Line 46: `import java.util.concurrent.TimeUnit;`
- Line 48: `import javax.net.ssl.KeyManagerFactory;`
- Line 49: `import javax.net.ssl.SSLContext;`
- Line 50: `import javax.net.ssl.SSLHandshakeException;`
- Line 51: `import javax.net.ssl.TrustManagerFactory;`
- Line 53: `import static org.hamcrest.Matchers.allOf;`
- Line 54: `import static org.hamcrest.Matchers.containsString;`
- Line 55: `import static org.hamcrest.Matchers.instanceOf;`
- Line 56: `import static org.hamcrest.Matchers.startsWith;`
- Line 57: `import static org.junit.Assert.assertEquals;`
- Line 58: `import static org.junit.Assert.assertThat;`
- Line 59: `import static org.junit.Assert.assertTrue;`
- Line 60: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientBuilderTests.java

### Unused Code (13)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.HttpHost;`
- Line 24: `import org.apache.http.client.config.RequestConfig;`
- Line 25: `import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;`
- Line 26: `import org.apache.http.message.BasicHeader;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.util.Base64;`
- Line 31: `import static org.hamcrest.Matchers.containsString;`
- Line 32: `import static org.hamcrest.Matchers.equalTo;`
- Line 33: `import static org.junit.Assert.assertEquals;`
- Line 34: `import static org.junit.Assert.assertNotNull;`
- Line 35: `import static org.junit.Assert.assertThat;`
- Line 36: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientGzipCompressionTests.java

### Unused Code (22)
- Line 22: `import com.sun.net.httpserver.HttpExchange;`
- Line 23: `import com.sun.net.httpserver.HttpHandler;`
- Line 24: `import com.sun.net.httpserver.HttpServer;`
- Line 26: `import org.apache.http.HttpEntity;`
- Line 27: `import org.apache.http.HttpHost;`
- Line 28: `import org.apache.http.entity.ContentType;`
- Line 29: `import org.apache.http.entity.StringEntity;`
- Line 30: `import org.apache.http.protocol.HTTP;`
- Line 31: `import org.elasticsearch.mocksocket.MockHttpServer;`
- Line 32: `import org.junit.AfterClass;`
- Line 33: `import org.junit.Assert;`
- Line 34: `import org.junit.BeforeClass;`
- Line 36: `import java.io.ByteArrayOutputStream;`
- Line 37: `import java.io.IOException;`
- Line 38: `import java.io.InputStream;`
- Line 39: `import java.io.OutputStream;`
- Line 40: `import java.net.InetAddress;`
- Line 41: `import java.net.InetSocketAddress;`
- Line 42: `import java.nio.charset.StandardCharsets;`
- Line 43: `import java.util.concurrent.CompletableFuture;`
- Line 44: `import java.util.zip.GZIPInputStream;`
- Line 45: `import java.util.zip.GZIPOutputStream;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientMultipleHostsIntegTests.java

### Null Pointer (1)
- Line 182: `restClient = null;`

### Concurrency Issue (2)
- Line 66: `private static boolean stoppedFirstHost = false;`
- Line 129: `private final CountDownLatch requestCameInLatch = new CountDownLatch(1);`

### Exception Handling (1)
- Line 145: `} catch (InterruptedException ignore) {} finally {`

### Unused Code (31)
- Line 22: `import com.sun.net.httpserver.HttpExchange;`
- Line 23: `import com.sun.net.httpserver.HttpHandler;`
- Line 24: `import com.sun.net.httpserver.HttpServer;`
- Line 26: `import org.apache.http.HttpHost;`
- Line 27: `import org.elasticsearch.mocksocket.MockHttpServer;`
- Line 28: `import org.junit.AfterClass;`
- Line 29: `import org.junit.Before;`
- Line 30: `import org.junit.BeforeClass;`
- Line 31: `import org.junit.Ignore;`
- Line 33: `import java.io.IOException;`
- Line 34: `import java.io.OutputStream;`
- Line 35: `import java.net.ConnectException;`
- Line 36: `import java.net.InetAddress;`
- Line 37: `import java.net.InetSocketAddress;`
- Line 38: `import java.nio.charset.StandardCharsets;`
- Line 39: `import java.util.ArrayList;`
- Line 40: `import java.util.Iterator;`
- Line 41: `import java.util.List;`
- Line 42: `import java.util.concurrent.CancellationException;`
- Line 43: `import java.util.concurrent.CopyOnWriteArrayList;`
- Line 44: `import java.util.concurrent.CountDownLatch;`
- Line 45: `import java.util.concurrent.TimeUnit;`
- Line 46: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 48: `import static org.elasticsearch.client.RestClientTestUtil.getAllStatusCodes;`
- Line 49: `import static org.elasticsearch.client.RestClientTestUtil.randomErrorNoRetryStatusCode;`
- Line 50: `import static org.elasticsearch.client.RestClientTestUtil.randomOkStatusCode;`
- Line 51: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 52: `import static org.junit.Assert.assertEquals;`
- Line 53: `import static org.junit.Assert.assertThat;`
- Line 54: `import static org.junit.Assert.assertTrue;`
- Line 55: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientMultipleHostsTests.java

### Concurrency Issue (1)
- Line 58: `private ExecutorService exec = Executors.newFixedThreadPool(1);`

### Exception Handling (1)
- Line 320: `throw new UnsupportedOperationException();`

### Unused Code (28)
- Line 58: `private ExecutorService exec = Executors.newFixedThreadPool(1);`
- Line 60: `private HostsTrackingFailureListener failureListener;`
- Line 22: `import com.carrotsearch.randomizedtesting.generators.RandomNumbers;`
- Line 24: `import org.apache.http.Header;`
- Line 25: `import org.apache.http.HttpHost;`
- Line 26: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 27: `import org.junit.After;`
- Line 29: `import java.io.IOException;`
- Line 30: `import java.util.ArrayList;`
- Line 31: `import java.util.Arrays;`
- Line 32: `import java.util.Collections;`
- Line 33: `import java.util.HashSet;`
- Line 34: `import java.util.Iterator;`
- Line 35: `import java.util.List;`
- Line 36: `import java.util.Set;`
- Line 37: `import java.util.TreeSet;`
- Line 38: `import java.util.concurrent.ExecutorService;`
- Line 39: `import java.util.concurrent.Executors;`
- Line 41: `import static org.elasticsearch.client.RestClientTestUtil.randomErrorNoRetryStatusCode;`
- Line 42: `import static org.elasticsearch.client.RestClientTestUtil.randomErrorRetryStatusCode;`
- Line 43: `import static org.elasticsearch.client.RestClientTestUtil.randomHttpMethod;`
- Line 44: `import static org.elasticsearch.client.RestClientTestUtil.randomOkStatusCode;`
- Line 45: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 46: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 47: `import static org.junit.Assert.assertEquals;`
- Line 48: `import static org.junit.Assert.assertThat;`
- Line 49: `import static org.junit.Assert.assertTrue;`
- Line 50: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientSingleHostIntegTests.java

### Null Pointer (1)
- Line 200: `restClient = null;`

### Exception Handling (1)
- Line 122: `} catch (InterruptedException ignore) {} finally {`

### Unused Code (56)
- Line 84: `private HttpServer httpServer;`
- Line 85: `private RestClient restClient;`
- Line 86: `private String pathPrefix;`
- Line 88: `private WaitForCancelHandler waitForCancelHandler;`
- Line 22: `import com.sun.net.httpserver.Headers;`
- Line 23: `import com.sun.net.httpserver.HttpExchange;`
- Line 24: `import com.sun.net.httpserver.HttpHandler;`
- Line 25: `import com.sun.net.httpserver.HttpServer;`
- Line 27: `import org.apache.http.Consts;`
- Line 28: `import org.apache.http.Header;`
- Line 29: `import org.apache.http.HttpHost;`
- Line 30: `import org.apache.http.HttpResponse;`
- Line 31: `import org.apache.http.auth.AuthScope;`
- Line 32: `import org.apache.http.auth.UsernamePasswordCredentials;`
- Line 33: `import org.apache.http.client.methods.HttpGet;`
- Line 34: `import org.apache.http.client.methods.HttpRequestBase;`
- Line 35: `import org.apache.http.entity.ContentType;`
- Line 36: `import org.apache.http.impl.client.BasicCredentialsProvider;`
- Line 37: `import org.apache.http.impl.client.TargetAuthenticationStrategy;`
- Line 38: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 39: `import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;`
- Line 40: `import org.apache.http.message.BasicHeader;`
- Line 41: `import org.apache.http.nio.entity.NStringEntity;`
- Line 42: `import org.apache.http.util.EntityUtils;`
- Line 43: `import org.elasticsearch.mocksocket.MockHttpServer;`
- Line 44: `import org.junit.After;`
- Line 45: `import org.junit.Before;`
- Line 47: `import java.io.IOException;`
- Line 48: `import java.io.InputStreamReader;`
- Line 49: `import java.io.OutputStream;`
- Line 50: `import java.net.InetAddress;`
- Line 51: `import java.net.InetSocketAddress;`
- Line 52: `import java.util.Arrays;`
- Line 53: `import java.util.HashSet;`
- Line 54: `import java.util.List;`
- Line 55: `import java.util.Map;`
- Line 56: `import java.util.Set;`
- Line 57: `import java.util.concurrent.CancellationException;`
- Line 58: `import java.util.concurrent.CopyOnWriteArrayList;`
- Line 59: `import java.util.concurrent.CountDownLatch;`
- Line 60: `import java.util.concurrent.Future;`
- Line 61: `import java.util.concurrent.TimeUnit;`
- Line 62: `import java.util.concurrent.atomic.AtomicReference;`
- Line 64: `import static org.elasticsearch.client.RestClientTestUtil.getAllStatusCodes;`
- Line 65: `import static org.elasticsearch.client.RestClientTestUtil.getHttpMethods;`
- Line 66: `import static org.elasticsearch.client.RestClientTestUtil.randomHttpMethod;`
- Line 67: `import static org.elasticsearch.client.RestClientTestUtil.randomStatusCode;`
- Line 68: `import static org.hamcrest.Matchers.instanceOf;`
- Line 69: `import static org.hamcrest.Matchers.nullValue;`
- Line 70: `import static org.hamcrest.Matchers.startsWith;`
- Line 71: `import static org.junit.Assert.assertEquals;`
- Line 72: `import static org.junit.Assert.assertFalse;`
- Line 73: `import static org.junit.Assert.assertNull;`
- Line 74: `import static org.junit.Assert.assertThat;`
- Line 75: `import static org.junit.Assert.assertTrue;`
- Line 76: `import static org.junit.Assert.fail;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientSingleHostTests.java

### Concurrency Issue (2)
- Line 104: `private static final Log logger = LogFactory.getLog(RestClientSingleHostTests.class);`
- Line 106: `private ExecutorService exec = Executors.newFixedThreadPool(1);`

### Exception Handling (5)
- Line 176: `throw new ConnectionClosedException();`
- Line 178: `throw new SSLHandshakeException("");`
- Line 180: `throw new URISyntaxException("", "");`
- Line 182: `throw new RuntimeException();`
- Line 604: `throw new UnsupportedOperationException("method not supported: " + method);`

### Unused Code (78)
- Line 106: `private ExecutorService exec = Executors.newFixedThreadPool(1);`
- Line 107: `private RestClient restClient;`
- Line 109: `private Node node;`
- Line 110: `private CloseableHttpAsyncClient httpClient;`
- Line 111: `private HostsTrackingFailureListener failureListener;`
- Line 112: `private boolean strictDeprecationMode;`
- Line 22: `import org.apache.commons.logging.Log;`
- Line 23: `import org.apache.commons.logging.LogFactory;`
- Line 24: `import org.apache.http.ConnectionClosedException;`
- Line 25: `import org.apache.http.Header;`
- Line 26: `import org.apache.http.HttpEntity;`
- Line 27: `import org.apache.http.HttpEntityEnclosingRequest;`
- Line 28: `import org.apache.http.HttpHost;`
- Line 29: `import org.apache.http.HttpRequest;`
- Line 30: `import org.apache.http.HttpResponse;`
- Line 31: `import org.apache.http.ProtocolVersion;`
- Line 32: `import org.apache.http.StatusLine;`
- Line 33: `import org.apache.http.client.methods.HttpHead;`
- Line 34: `import org.apache.http.client.methods.HttpOptions;`
- Line 35: `import org.apache.http.client.methods.HttpPatch;`
- Line 36: `import org.apache.http.client.methods.HttpPost;`
- Line 37: `import org.apache.http.client.methods.HttpPut;`
- Line 38: `import org.apache.http.client.methods.HttpTrace;`
- Line 39: `import org.apache.http.client.methods.HttpUriRequest;`
- Line 40: `import org.apache.http.client.protocol.HttpClientContext;`
- Line 41: `import org.apache.http.client.utils.URIBuilder;`
- Line 42: `import org.apache.http.concurrent.FutureCallback;`
- Line 43: `import org.apache.http.conn.ConnectTimeoutException;`
- Line 44: `import org.apache.http.entity.ContentType;`
- Line 45: `import org.apache.http.entity.StringEntity;`
- Line 46: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 47: `import org.apache.http.message.BasicHttpResponse;`
- Line 48: `import org.apache.http.message.BasicStatusLine;`
- Line 49: `import org.apache.http.nio.protocol.HttpAsyncRequestProducer;`
- Line 50: `import org.apache.http.nio.protocol.HttpAsyncResponseConsumer;`
- Line 51: `import org.apache.http.util.EntityUtils;`
- Line 52: `import org.junit.After;`
- Line 53: `import org.junit.Before;`
- Line 54: `import org.mockito.ArgumentCaptor;`
- Line 55: `import org.mockito.stubbing.Answer;`
- Line 57: `import java.io.IOException;`
- Line 58: `import java.io.PrintWriter;`
- Line 59: `import java.io.StringWriter;`
- Line 60: `import java.net.SocketTimeoutException;`
- Line 61: `import java.net.URI;`
- Line 62: `import java.net.URISyntaxException;`
- Line 63: `import java.nio.charset.StandardCharsets;`
- Line 64: `import java.util.Arrays;`
- Line 65: `import java.util.Collections;`
- Line 66: `import java.util.HashSet;`
- Line 67: `import java.util.List;`
- Line 68: `import java.util.Set;`
- Line 69: `import java.util.concurrent.CountDownLatch;`
- Line 70: `import java.util.concurrent.ExecutorService;`
- Line 71: `import java.util.concurrent.Executors;`
- Line 72: `import java.util.concurrent.Future;`
- Line 73: `import java.util.concurrent.atomic.AtomicReference;`
- Line 75: `import javax.net.ssl.SSLHandshakeException;`
- Line 77: `import static java.util.Collections.singletonList;`
- Line 78: `import static org.elasticsearch.client.RestClientTestUtil.getAllErrorStatusCodes;`
- Line 79: `import static org.elasticsearch.client.RestClientTestUtil.getHttpMethods;`
- Line 80: `import static org.elasticsearch.client.RestClientTestUtil.getOkStatusCodes;`
- Line 81: `import static org.elasticsearch.client.RestClientTestUtil.randomStatusCode;`
- Line 82: `import static org.hamcrest.CoreMatchers.containsString;`
- Line 83: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 84: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 85: `import static org.junit.Assert.assertArrayEquals;`
- Line 86: `import static org.junit.Assert.assertEquals;`
- Line 87: `import static org.junit.Assert.assertFalse;`
- Line 88: `import static org.junit.Assert.assertThat;`
- Line 89: `import static org.junit.Assert.assertTrue;`
- Line 90: `import static org.junit.Assert.fail;`
- Line 91: `import static org.mockito.ArgumentMatchers.any;`
- Line 92: `import static org.mockito.ArgumentMatchers.nullable;`
- Line 93: `import static org.mockito.Mockito.mock;`
- Line 94: `import static org.mockito.Mockito.times;`
- Line 95: `import static org.mockito.Mockito.verify;`
- Line 96: `import static org.mockito.Mockito.when;`

## ../client/rest/src/test/java/org/elasticsearch/client/RestClientTests.java

### Exception Handling (2)
- Line 78: `throw new UnsupportedOperationException("onSuccess cannot be called when using a mocked http client");`
- Line 101: `throw new UnsupportedOperationException("onSuccess cannot be called when using a mocked http client");`

### Unused Code (33)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.HttpHost;`
- Line 24: `import org.apache.http.client.AuthCache;`
- Line 25: `import org.apache.http.impl.auth.BasicScheme;`
- Line 26: `import org.apache.http.impl.client.BasicAuthCache;`
- Line 27: `import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;`
- Line 28: `import org.elasticsearch.client.RestClient.NodeTuple;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.net.URI;`
- Line 32: `import java.util.ArrayList;`
- Line 33: `import java.util.Arrays;`
- Line 34: `import java.util.Collections;`
- Line 35: `import java.util.HashMap;`
- Line 36: `import java.util.Iterator;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Map;`
- Line 39: `import java.util.concurrent.CountDownLatch;`
- Line 40: `import java.util.concurrent.TimeUnit;`
- Line 41: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 42: `import java.util.concurrent.atomic.AtomicLong;`
- Line 43: `import java.util.function.Supplier;`
- Line 45: `import static java.util.Collections.singletonList;`
- Line 46: `import static org.hamcrest.Matchers.instanceOf;`
- Line 47: `import static org.junit.Assert.assertEquals;`
- Line 48: `import static org.junit.Assert.assertFalse;`
- Line 49: `import static org.junit.Assert.assertSame;`
- Line 50: `import static org.junit.Assert.assertThat;`
- Line 51: `import static org.junit.Assert.assertTrue;`
- Line 52: `import static org.junit.Assert.fail;`
- Line 53: `import static org.mockito.Mockito.mock;`
- Line 54: `import static org.mockito.Mockito.times;`
- Line 55: `import static org.mockito.Mockito.verify;`
- Line 56: `import static org.mockito.Mockito.when;`

## ../client/rest/src/test/java/org/elasticsearch/client/documentation/RestClientDocumentation.java

### Concurrency Issue (1)
- Line 85: `private static final String TOKEN = "DUMMY";`

### Unused Code (41)
- Line 22: `import org.apache.http.Header;`
- Line 23: `import org.apache.http.HttpEntity;`
- Line 24: `import org.apache.http.HttpHost;`
- Line 25: `import org.apache.http.RequestLine;`
- Line 26: `import org.apache.http.auth.AuthScope;`
- Line 27: `import org.apache.http.auth.UsernamePasswordCredentials;`
- Line 28: `import org.apache.http.client.CredentialsProvider;`
- Line 29: `import org.apache.http.client.config.RequestConfig;`
- Line 30: `import org.apache.http.entity.ContentType;`
- Line 31: `import org.apache.http.impl.client.BasicCredentialsProvider;`
- Line 32: `import org.apache.http.impl.nio.client.HttpAsyncClientBuilder;`
- Line 33: `import org.apache.http.impl.nio.reactor.IOReactorConfig;`
- Line 34: `import org.apache.http.message.BasicHeader;`
- Line 35: `import org.apache.http.nio.entity.NStringEntity;`
- Line 36: `import org.apache.http.ssl.SSLContextBuilder;`
- Line 37: `import org.apache.http.ssl.SSLContexts;`
- Line 38: `import org.apache.http.util.EntityUtils;`
- Line 39: `import org.elasticsearch.client.Cancellable;`
- Line 40: `import org.elasticsearch.client.HttpAsyncResponseConsumerFactory;`
- Line 41: `import org.elasticsearch.client.Node;`
- Line 42: `import org.elasticsearch.client.NodeSelector;`
- Line 43: `import org.elasticsearch.client.Request;`
- Line 44: `import org.elasticsearch.client.RequestOptions;`
- Line 45: `import org.elasticsearch.client.Response;`
- Line 46: `import org.elasticsearch.client.ResponseListener;`
- Line 47: `import org.elasticsearch.client.RestClient;`
- Line 48: `import org.elasticsearch.client.RestClientBuilder;`
- Line 49: `import org.elasticsearch.client.RestClientBuilder.HttpClientConfigCallback;`
- Line 51: `import java.io.IOException;`
- Line 52: `import java.io.InputStream;`
- Line 53: `import java.nio.charset.StandardCharsets;`
- Line 54: `import java.nio.file.Files;`
- Line 55: `import java.nio.file.Path;`
- Line 56: `import java.nio.file.Paths;`
- Line 57: `import java.security.KeyStore;`
- Line 58: `import java.security.cert.Certificate;`
- Line 59: `import java.security.cert.CertificateFactory;`
- Line 60: `import java.util.Base64;`
- Line 61: `import java.util.Iterator;`
- Line 62: `import java.util.concurrent.CountDownLatch;`
- Line 64: `import javax.net.ssl.SSLContext;`

## ../client/sniffer/src/main/java/org/elasticsearch/client/sniff/ElasticsearchNodesSniffer.java

### Concurrency Issue (2)
- Line 59: `private static final Log logger = LogFactory.getLog(ElasticsearchNodesSniffer.class);`
- Line 61: `public static final long DEFAULT_SNIFF_REQUEST_TIMEOUT = TimeUnit.SECONDS.toMillis(1);`

### Exception Handling (3)
- Line 94: `throw new IllegalArgumentException("sniffRequestTimeoutMillis must be greater than 0");`
- Line 114: `throw new IOException("expected data to start with an object");`
- Line 286: `throw new IOException("expected only a single attribute value for [" + name + "] but got " + valueList);`

### Unused Code (27)
- Line 22: `import com.fasterxml.jackson.core.JsonFactory;`
- Line 23: `import com.fasterxml.jackson.core.JsonParser;`
- Line 24: `import com.fasterxml.jackson.core.JsonToken;`
- Line 26: `import org.apache.commons.logging.Log;`
- Line 27: `import org.apache.commons.logging.LogFactory;`
- Line 28: `import org.apache.http.HttpEntity;`
- Line 29: `import org.apache.http.HttpHost;`
- Line 30: `import org.elasticsearch.client.Node;`
- Line 31: `import org.elasticsearch.client.Node.Roles;`
- Line 32: `import org.elasticsearch.client.Request;`
- Line 33: `import org.elasticsearch.client.Response;`
- Line 34: `import org.elasticsearch.client.RestClient;`
- Line 36: `import java.io.IOException;`
- Line 37: `import java.io.InputStream;`
- Line 38: `import java.net.URI;`
- Line 39: `import java.util.ArrayList;`
- Line 40: `import java.util.HashMap;`
- Line 41: `import java.util.HashSet;`
- Line 42: `import java.util.List;`
- Line 43: `import java.util.Map;`
- Line 44: `import java.util.Objects;`
- Line 45: `import java.util.Set;`
- Line 46: `import java.util.TreeSet;`
- Line 47: `import java.util.concurrent.TimeUnit;`
- Line 49: `import static java.util.Collections.singletonList;`
- Line 50: `import static java.util.Collections.unmodifiableList;`
- Line 51: `import static java.util.Collections.unmodifiableMap;`

## ../client/sniffer/src/main/java/org/elasticsearch/client/sniff/NodesSniffer.java

### Unused Code (3)
- Line 21: `import org.elasticsearch.client.Node;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.util.List;`

## ../client/sniffer/src/main/java/org/elasticsearch/client/sniff/SniffOnFailureListener.java

### Concurrency Issue (1)
- Line 47: `public void setSniffer(Sniffer sniffer) {`

### Exception Handling (2)
- Line 52: `throw new IllegalStateException("sniffer can only be set once");`
- Line 59: `throw new IllegalStateException("sniffer was not set, unable to sniff on failure");`

### Unused Code (4)
- Line 22: `import org.elasticsearch.client.Node;`
- Line 23: `import org.elasticsearch.client.RestClient;`
- Line 25: `import java.util.Objects;`
- Line 26: `import java.util.concurrent.atomic.AtomicBoolean;`

## ../client/sniffer/src/main/java/org/elasticsearch/client/sniff/Sniffer.java

### Concurrency Issue (4)
- Line 53: `private static final Log logger = LogFactory.getLog(Sniffer.class);`
- Line 54: `private static final String SNIFFER_THREAD_NAME = "es_rest_client_sniffer";`
- Line 61: `private final AtomicBoolean initialized = new AtomicBoolean(false);`
- Line 295: `private final AtomicInteger threadNumber = new AtomicInteger(1);`

### Unused Code (20)
- Line 21: `import org.apache.commons.logging.Log;`
- Line 22: `import org.apache.commons.logging.LogFactory;`
- Line 23: `import org.elasticsearch.client.Node;`
- Line 24: `import org.elasticsearch.client.RestClient;`
- Line 25: `import org.elasticsearch.client.RestClientBuilder;`
- Line 27: `import java.io.Closeable;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.security.AccessController;`
- Line 30: `import java.security.PrivilegedAction;`
- Line 31: `import java.util.Collection;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.concurrent.Executors;`
- Line 34: `import java.util.concurrent.Future;`
- Line 35: `import java.util.concurrent.ScheduledExecutorService;`
- Line 36: `import java.util.concurrent.ScheduledThreadPoolExecutor;`
- Line 37: `import java.util.concurrent.ThreadFactory;`
- Line 38: `import java.util.concurrent.TimeUnit;`
- Line 39: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 40: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 41: `import java.util.concurrent.atomic.AtomicReference;`

## ../client/sniffer/src/main/java/org/elasticsearch/client/sniff/SnifferBuilder.java

### Concurrency Issue (4)
- Line 31: `public static final long DEFAULT_SNIFF_INTERVAL = TimeUnit.MINUTES.toMillis(5);`
- Line 32: `public static final long DEFAULT_SNIFF_AFTER_FAILURE_DELAY = TimeUnit.MINUTES.toMillis(1);`
- Line 35: `private long sniffIntervalMillis = DEFAULT_SNIFF_INTERVAL;`
- Line 36: `private long sniffAfterFailureDelayMillis = DEFAULT_SNIFF_AFTER_FAILURE_DELAY;`

### Exception Handling (2)
- Line 54: `throw new IllegalArgumentException("sniffIntervalMillis must be greater than 0");`
- Line 65: `throw new IllegalArgumentException("sniffAfterFailureDelayMillis must be greater than 0");`

### Unused Code (6)
- Line 35: `private long sniffIntervalMillis = DEFAULT_SNIFF_INTERVAL;`
- Line 36: `private long sniffAfterFailureDelayMillis = DEFAULT_SNIFF_AFTER_FAILURE_DELAY;`
- Line 37: `private NodesSniffer nodesSniffer;`
- Line 22: `import org.elasticsearch.client.RestClient;`
- Line 24: `import java.util.Objects;`
- Line 25: `import java.util.concurrent.TimeUnit;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/ElasticsearchNodesSnifferParseTests.java

### Exception Handling (1)
- Line 57: `throw new IllegalArgumentException("Couldn't find [" + file + "]");`

### Unused Code (22)
- Line 22: `import com.fasterxml.jackson.core.JsonFactory;`
- Line 24: `import org.apache.http.HttpEntity;`
- Line 25: `import org.apache.http.HttpHost;`
- Line 26: `import org.apache.http.entity.ContentType;`
- Line 27: `import org.apache.http.entity.InputStreamEntity;`
- Line 28: `import org.elasticsearch.client.Node;`
- Line 29: `import org.elasticsearch.client.Node.Roles;`
- Line 30: `import org.elasticsearch.client.RestClientTestCase;`
- Line 31: `import org.elasticsearch.client.sniff.ElasticsearchNodesSniffer.Scheme;`
- Line 33: `import java.io.IOException;`
- Line 34: `import java.io.InputStream;`
- Line 35: `import java.util.Arrays;`
- Line 36: `import java.util.HashMap;`
- Line 37: `import java.util.HashSet;`
- Line 38: `import java.util.List;`
- Line 39: `import java.util.Map;`
- Line 40: `import java.util.Set;`
- Line 41: `import java.util.TreeSet;`
- Line 43: `import static java.util.Collections.singletonList;`
- Line 44: `import static org.hamcrest.Matchers.hasSize;`
- Line 45: `import static org.junit.Assert.assertEquals;`
- Line 46: `import static org.junit.Assert.assertThat;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/ElasticsearchNodesSnifferTests.java

### Unused Code (42)
- Line 67: `private int sniffRequestTimeout;`
- Line 69: `private SniffResponse sniffResponse;`
- Line 70: `private HttpServer httpServer;`
- Line 22: `import com.carrotsearch.randomizedtesting.generators.RandomNumbers;`
- Line 23: `import com.carrotsearch.randomizedtesting.generators.RandomPicks;`
- Line 24: `import com.carrotsearch.randomizedtesting.generators.RandomStrings;`
- Line 25: `import com.fasterxml.jackson.core.JsonFactory;`
- Line 26: `import com.fasterxml.jackson.core.JsonGenerator;`
- Line 27: `import com.sun.net.httpserver.HttpExchange;`
- Line 28: `import com.sun.net.httpserver.HttpHandler;`
- Line 29: `import com.sun.net.httpserver.HttpServer;`
- Line 31: `import org.apache.http.Consts;`
- Line 32: `import org.apache.http.HttpHost;`
- Line 33: `import org.apache.http.client.methods.HttpGet;`
- Line 34: `import org.elasticsearch.client.Node;`
- Line 35: `import org.elasticsearch.client.Response;`
- Line 36: `import org.elasticsearch.client.ResponseException;`
- Line 37: `import org.elasticsearch.client.RestClient;`
- Line 38: `import org.elasticsearch.client.RestClientTestCase;`
- Line 39: `import org.elasticsearch.mocksocket.MockHttpServer;`
- Line 40: `import org.junit.After;`
- Line 41: `import org.junit.Before;`
- Line 43: `import java.io.IOException;`
- Line 44: `import java.io.OutputStream;`
- Line 45: `import java.io.StringWriter;`
- Line 46: `import java.net.InetAddress;`
- Line 47: `import java.net.InetSocketAddress;`
- Line 48: `import java.util.ArrayList;`
- Line 49: `import java.util.Arrays;`
- Line 50: `import java.util.Collections;`
- Line 51: `import java.util.HashMap;`
- Line 52: `import java.util.HashSet;`
- Line 53: `import java.util.List;`
- Line 54: `import java.util.Map;`
- Line 55: `import java.util.Set;`
- Line 56: `import java.util.TreeSet;`
- Line 58: `import static org.hamcrest.CoreMatchers.containsString;`
- Line 59: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 60: `import static org.hamcrest.CoreMatchers.startsWith;`
- Line 61: `import static org.junit.Assert.assertEquals;`
- Line 62: `import static org.junit.Assert.assertThat;`
- Line 63: `import static org.junit.Assert.fail;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/MockNodesSniffer.java

### Unused Code (4)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node;`
- Line 25: `import java.util.Collections;`
- Line 26: `import java.util.List;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/SniffOnFailureListenerTests.java

### Unused Code (6)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node;`
- Line 24: `import org.elasticsearch.client.RestClient;`
- Line 25: `import org.elasticsearch.client.RestClientTestCase;`
- Line 27: `import static org.junit.Assert.assertEquals;`
- Line 28: `import static org.junit.Assert.fail;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/SnifferBuilderTests.java

### Unused Code (7)
- Line 21: `import com.carrotsearch.randomizedtesting.generators.RandomNumbers;`
- Line 23: `import org.apache.http.HttpHost;`
- Line 24: `import org.elasticsearch.client.RestClient;`
- Line 25: `import org.elasticsearch.client.RestClientTestCase;`
- Line 27: `import static org.junit.Assert.assertEquals;`
- Line 28: `import static org.junit.Assert.assertNotNull;`
- Line 29: `import static org.junit.Assert.fail;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/SnifferTests.java

### Concurrency Issue (2)
- Line 546: `private final AtomicInteger runs = new AtomicInteger(0);`
- Line 547: `private final AtomicInteger failures = new AtomicInteger(0);`

### Exception Handling (2)
- Line 431: `} catch (CancellationException ignore) {}`
- Line 556: `throw new IOException("communication breakdown");`

### Unused Code (47)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node;`
- Line 24: `import org.elasticsearch.client.RestClient;`
- Line 25: `import org.elasticsearch.client.RestClientTestCase;`
- Line 26: `import org.elasticsearch.client.sniff.Sniffer.DefaultScheduler;`
- Line 27: `import org.elasticsearch.client.sniff.Sniffer.Scheduler;`
- Line 28: `import org.mockito.invocation.InvocationOnMock;`
- Line 29: `import org.mockito.stubbing.Answer;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.util.ArrayList;`
- Line 33: `import java.util.Collections;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.Set;`
- Line 36: `import java.util.concurrent.CancellationException;`
- Line 37: `import java.util.concurrent.CopyOnWriteArraySet;`
- Line 38: `import java.util.concurrent.CountDownLatch;`
- Line 39: `import java.util.concurrent.ExecutionException;`
- Line 40: `import java.util.concurrent.ExecutorService;`
- Line 41: `import java.util.concurrent.Executors;`
- Line 42: `import java.util.concurrent.Future;`
- Line 43: `import java.util.concurrent.ScheduledExecutorService;`
- Line 44: `import java.util.concurrent.ScheduledFuture;`
- Line 45: `import java.util.concurrent.ScheduledThreadPoolExecutor;`
- Line 46: `import java.util.concurrent.TimeUnit;`
- Line 47: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 48: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 49: `import java.util.concurrent.atomic.AtomicReference;`
- Line 51: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 52: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 53: `import static org.hamcrest.Matchers.greaterThan;`
- Line 54: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`
- Line 55: `import static org.hamcrest.Matchers.is;`
- Line 56: `import static org.junit.Assert.assertEquals;`
- Line 57: `import static org.junit.Assert.assertFalse;`
- Line 58: `import static org.junit.Assert.assertNotEquals;`
- Line 59: `import static org.junit.Assert.assertNull;`
- Line 60: `import static org.junit.Assert.assertSame;`
- Line 61: `import static org.junit.Assert.assertThat;`
- Line 62: `import static org.junit.Assert.assertTrue;`
- Line 63: `import static org.junit.Assert.fail;`
- Line 64: `import static org.mockito.ArgumentMatchers.any;`
- Line 65: `import static org.mockito.ArgumentMatchers.anyCollection;`
- Line 66: `import static org.mockito.Mockito.mock;`
- Line 67: `import static org.mockito.Mockito.times;`
- Line 68: `import static org.mockito.Mockito.verify;`
- Line 69: `import static org.mockito.Mockito.verifyNoMoreInteractions;`
- Line 70: `import static org.mockito.Mockito.when;`

## ../client/sniffer/src/test/java/org/elasticsearch/client/sniff/documentation/SnifferDocumentation.java

### Unused Code (10)
- Line 22: `import org.apache.http.HttpHost;`
- Line 23: `import org.elasticsearch.client.Node;`
- Line 24: `import org.elasticsearch.client.RestClient;`
- Line 25: `import org.elasticsearch.client.sniff.ElasticsearchNodesSniffer;`
- Line 26: `import org.elasticsearch.client.sniff.NodesSniffer;`
- Line 27: `import org.elasticsearch.client.sniff.SniffOnFailureListener;`
- Line 28: `import org.elasticsearch.client.sniff.Sniffer;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.concurrent.TimeUnit;`

## ../client/test/src/main/java/org/elasticsearch/client/ClientsGraalVMThreadsFilter.java

### Unused Code (1)
- Line 22: `import com.carrotsearch.randomizedtesting.ThreadFilter;`

## ../client/test/src/main/java/org/elasticsearch/client/RestClientTestCase.java

### Unused Code (22)
- Line 22: `import com.carrotsearch.randomizedtesting.JUnit3MethodProvider;`
- Line 23: `import com.carrotsearch.randomizedtesting.MixWithSuiteName;`
- Line 24: `import com.carrotsearch.randomizedtesting.RandomizedTest;`
- Line 25: `import com.carrotsearch.randomizedtesting.annotations.SeedDecorators;`
- Line 26: `import com.carrotsearch.randomizedtesting.annotations.TestMethodProviders;`
- Line 27: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakAction;`
- Line 28: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakFilters;`
- Line 29: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakGroup;`
- Line 30: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakLingering;`
- Line 31: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakScope;`
- Line 32: `import com.carrotsearch.randomizedtesting.annotations.ThreadLeakZombies;`
- Line 33: `import com.carrotsearch.randomizedtesting.annotations.TimeoutSuite;`
- Line 35: `import org.apache.http.Header;`
- Line 37: `import java.util.ArrayList;`
- Line 38: `import java.util.HashMap;`
- Line 39: `import java.util.HashSet;`
- Line 40: `import java.util.List;`
- Line 41: `import java.util.Map;`
- Line 42: `import java.util.Set;`
- Line 44: `import static org.junit.Assert.assertEquals;`
- Line 45: `import static org.junit.Assert.assertNotNull;`
- Line 46: `import static org.junit.Assert.assertTrue;`

## ../client/test/src/main/java/org/elasticsearch/client/RestClientTestUtil.java

### Unused Code (9)
- Line 22: `import com.carrotsearch.randomizedtesting.generators.RandomNumbers;`
- Line 23: `import com.carrotsearch.randomizedtesting.generators.RandomPicks;`
- Line 24: `import com.carrotsearch.randomizedtesting.generators.RandomStrings;`
- Line 26: `import org.apache.http.Header;`
- Line 27: `import org.apache.http.message.BasicHeader;`
- Line 29: `import java.util.ArrayList;`
- Line 30: `import java.util.Arrays;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Random;`

## ../distribution/archives/integ-test-zip/src/javaRestTest/java/org/elasticsearch/test/rest/CreatedLocationHeaderIT.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.client.Request;`
- Line 13: `import org.elasticsearch.client.Response;`
- Line 14: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 15: `import org.junit.ClassRule;`
- Line 17: `import java.io.IOException;`
- Line 19: `import static java.util.Collections.singletonMap;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`
- Line 21: `import static org.hamcrest.Matchers.startsWith;`

## ../distribution/archives/integ-test-zip/src/javaRestTest/java/org/elasticsearch/test/rest/JsonLogsFormatAndParseIT.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.common.logging.JsonLogsIntegTestCase;`
- Line 13: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 14: `import org.elasticsearch.test.cluster.LogType;`
- Line 15: `import org.hamcrest.Matcher;`
- Line 16: `import org.junit.ClassRule;`
- Line 18: `import java.io.InputStream;`
- Line 20: `import static org.hamcrest.Matchers.is;`

## ../distribution/archives/integ-test-zip/src/javaRestTest/java/org/elasticsearch/test/rest/NodeRestUsageIT.java

### Unused Code (16)
- Line 12: `import org.elasticsearch.client.Request;`
- Line 13: `import org.elasticsearch.client.Response;`
- Line 14: `import org.elasticsearch.client.ResponseException;`
- Line 15: `import org.elasticsearch.common.Strings;`
- Line 16: `import org.elasticsearch.search.aggregations.AggregationBuilders;`
- Line 17: `import org.elasticsearch.search.builder.SearchSourceBuilder;`
- Line 18: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 19: `import org.junit.ClassRule;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.util.Collections;`
- Line 23: `import java.util.HashMap;`
- Line 24: `import java.util.Map;`
- Line 26: `import static org.hamcrest.Matchers.containsString;`
- Line 27: `import static org.hamcrest.Matchers.equalTo;`
- Line 28: `import static org.hamcrest.Matchers.greaterThan;`
- Line 29: `import static org.hamcrest.Matchers.notNullValue;`

## ../distribution/archives/integ-test-zip/src/javaRestTest/java/org/elasticsearch/test/rest/RequestsWithoutContentIT.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.client.Request;`
- Line 13: `import org.elasticsearch.client.ResponseException;`
- Line 14: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 15: `import org.junit.ClassRule;`
- Line 17: `import java.io.IOException;`
- Line 19: `import static org.hamcrest.CoreMatchers.containsString;`

## ../distribution/archives/integ-test-zip/src/javaRestTest/java/org/elasticsearch/test/rest/WaitForRefreshAndCloseIT.java

### Exception Handling (1)
- Line 91: `throw new RuntimeException(e);`

### Unused Code (18)
- Line 12: `import org.apache.http.util.EntityUtils;`
- Line 13: `import org.elasticsearch.action.ActionFuture;`
- Line 14: `import org.elasticsearch.action.ActionListener;`
- Line 15: `import org.elasticsearch.action.support.PlainActionFuture;`
- Line 16: `import org.elasticsearch.client.Request;`
- Line 17: `import org.elasticsearch.client.Response;`
- Line 18: `import org.elasticsearch.client.ResponseException;`
- Line 19: `import org.elasticsearch.client.ResponseListener;`
- Line 20: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 21: `import org.junit.After;`
- Line 22: `import org.junit.Before;`
- Line 23: `import org.junit.ClassRule;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.concurrent.ExecutionException;`
- Line 28: `import java.util.concurrent.TimeUnit;`
- Line 30: `import static org.hamcrest.Matchers.containsString;`
- Line 31: `import static org.hamcrest.Matchers.instanceOf;`

## ../distribution/docker/src/yamlRestTest/java/org/elasticsearch/docker/test/DockerYmlTestSuiteIT.java

### Null Pointer (1)
- Line 119: `return Settings.builder()`

### Concurrency Issue (2)
- Line 33: `private static final String USER = "x_pack_rest_user";`
- Line 34: `private static final String PASS = "x-pack-test-password";`

### Exception Handling (4)
- Line 64: `throw new IllegalArgumentException("supported values for tests.distribution are oss or default but it was " + distribution);`
- Line 76: `throw new IllegalStateException(`
- Line 100: `throw new ElasticsearchException("exception while reading the certificate", e);`
- Line 104: `throw new IllegalStateException("Certificate file [" + trustedCertFile + "] does not exist.");`

### Unused Code (17)
- Line 11: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 13: `import org.elasticsearch.ElasticsearchException;`
- Line 14: `import org.elasticsearch.client.Request;`
- Line 15: `import org.elasticsearch.common.settings.SecureString;`
- Line 16: `import org.elasticsearch.common.settings.Settings;`
- Line 17: `import org.elasticsearch.common.util.concurrent.ThreadContext;`
- Line 18: `import org.elasticsearch.core.PathUtils;`
- Line 19: `import org.elasticsearch.test.rest.ESRestTestCase;`
- Line 20: `import org.elasticsearch.test.rest.yaml.ClientYamlTestCandidate;`
- Line 21: `import org.elasticsearch.test.rest.yaml.ESClientYamlSuiteTestCase;`
- Line 22: `import org.junit.AfterClass;`
- Line 23: `import org.junit.Before;`
- Line 24: `import org.junit.BeforeClass;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.net.URISyntaxException;`
- Line 28: `import java.nio.file.Files;`
- Line 29: `import java.nio.file.Path;`

## ../distribution/tools/ansi-console/src/main/java/org/elasticsearch/io/ansi/AnsiConsoleLoader.java

### Concurrency Issue (1)
- Line 34: `private static final Logger logger = getLogger(AnsiConsoleLoader.class);`

### Unused Code (14)
- Line 11: `import org.apache.logging.log4j.Logger;`
- Line 12: `import org.elasticsearch.bootstrap.ConsoleLoader;`
- Line 13: `import org.elasticsearch.core.Nullable;`
- Line 14: `import org.elasticsearch.core.SuppressForbidden;`
- Line 15: `import org.fusesource.jansi.Ansi;`
- Line 16: `import org.fusesource.jansi.AnsiConsole;`
- Line 17: `import org.fusesource.jansi.AnsiPrintStream;`
- Line 18: `import org.fusesource.jansi.AnsiType;`
- Line 19: `import org.fusesource.jansi.io.AnsiOutputStream;`
- Line 21: `import java.lang.reflect.Field;`
- Line 22: `import java.lang.reflect.Method;`
- Line 23: `import java.nio.charset.Charset;`
- Line 24: `import java.util.function.Supplier;`
- Line 26: `import static org.apache.logging.log4j.LogManager.getLogger;`

## ../distribution/tools/ansi-console/src/test/java/org/elasticsearch/bootstrap/ConsoleLoaderTests.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.io.ansi.AnsiConsoleLoader;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.util.function.Supplier;`
- Line 17: `import static org.hamcrest.Matchers.instanceOf;`
- Line 18: `import static org.hamcrest.Matchers.notNullValue;`

## ../distribution/tools/ansi-console/src/test/java/org/elasticsearch/io/ansi/AnsiConsoleLoaderTests.java

### Unused Code (15)
- Line 12: `import org.elasticsearch.bootstrap.ConsoleLoader;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import org.fusesource.jansi.Ansi;`
- Line 15: `import org.fusesource.jansi.AnsiColors;`
- Line 16: `import org.fusesource.jansi.AnsiMode;`
- Line 17: `import org.fusesource.jansi.AnsiPrintStream;`
- Line 18: `import org.fusesource.jansi.AnsiType;`
- Line 19: `import org.fusesource.jansi.io.AnsiOutputStream;`
- Line 20: `import org.fusesource.jansi.io.AnsiProcessor;`
- Line 22: `import java.io.ByteArrayOutputStream;`
- Line 23: `import java.nio.charset.Charset;`
- Line 24: `import java.nio.charset.StandardCharsets;`
- Line 26: `import static org.hamcrest.Matchers.is;`
- Line 27: `import static org.hamcrest.Matchers.notNullValue;`
- Line 28: `import static org.hamcrest.Matchers.nullValue;`

## ../distribution/tools/cli-launcher/src/main/java/org/elasticsearch/launcher/CliToolLauncher.java

### Concurrency Issue (1)
- Line 32: `private static final String SCRIPT_PREFIX = "elasticsearch-";`

### Unused Code (12)
- Line 12: `import org.apache.logging.log4j.Level;`
- Line 13: `import org.elasticsearch.cli.CliToolProvider;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.Terminal;`
- Line 18: `import org.elasticsearch.common.logging.LogConfigurator;`
- Line 19: `import org.elasticsearch.common.settings.Settings;`
- Line 20: `import org.elasticsearch.core.SuppressForbidden;`
- Line 22: `import java.io.Closeable;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.util.Map;`

## ../distribution/tools/cli-launcher/src/test/java/org/elasticsearch/launcher/CliToolLauncherTests.java

### Unused Code (12)
- Line 12: `import org.elasticsearch.cli.MockTerminal;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.io.Closeable;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 20: `import static org.elasticsearch.launcher.CliToolLauncher.createShutdownHook;`
- Line 21: `import static org.elasticsearch.launcher.CliToolLauncher.getToolName;`
- Line 22: `import static org.hamcrest.Matchers.containsString;`
- Line 23: `import static org.hamcrest.Matchers.emptyString;`
- Line 24: `import static org.hamcrest.Matchers.equalTo;`
- Line 25: `import static org.hamcrest.Matchers.is;`

## ../distribution/tools/geoip-cli/src/main/java/org/elasticsearch/geoip/GeoIpCli.java

### Unused Code (27)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.Command;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.Terminal;`
- Line 18: `import org.elasticsearch.common.hash.MessageDigests;`
- Line 19: `import org.elasticsearch.core.PathUtils;`
- Line 20: `import org.elasticsearch.core.SuppressForbidden;`
- Line 21: `import org.elasticsearch.xcontent.XContentGenerator;`
- Line 22: `import org.elasticsearch.xcontent.XContentType;`
- Line 24: `import java.io.BufferedInputStream;`
- Line 25: `import java.io.BufferedOutputStream;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.InputStream;`
- Line 28: `import java.io.OutputStream;`
- Line 29: `import java.nio.charset.StandardCharsets;`
- Line 30: `import java.nio.file.Files;`
- Line 31: `import java.nio.file.Path;`
- Line 32: `import java.nio.file.StandardCopyOption;`
- Line 33: `import java.security.DigestInputStream;`
- Line 34: `import java.security.MessageDigest;`
- Line 35: `import java.util.Arrays;`
- Line 36: `import java.util.Locale;`
- Line 37: `import java.util.stream.Stream;`
- Line 38: `import java.util.zip.GZIPOutputStream;`
- Line 40: `import static java.nio.file.StandardOpenOption.CREATE;`
- Line 41: `import static java.nio.file.StandardOpenOption.TRUNCATE_EXISTING;`

## ../distribution/tools/geoip-cli/src/main/java/org/elasticsearch/geoip/GeoIpCliProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/geoip-cli/src/test/java/org/elasticsearch/geoip/GeoIpCliTests.java

### Unused Code (25)
- Line 42: `private Path source;`
- Line 43: `private Path target;`
- Line 12: `import joptsimple.OptionException;`
- Line 14: `import org.apache.commons.compress.archivers.tar.TarArchiveEntry;`
- Line 15: `import org.apache.commons.compress.archivers.tar.TarArchiveInputStream;`
- Line 16: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 17: `import org.elasticsearch.cli.Command;`
- Line 18: `import org.elasticsearch.cli.CommandTestCase;`
- Line 19: `import org.elasticsearch.xcontent.XContentParser;`
- Line 20: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 21: `import org.elasticsearch.xcontent.XContentType;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.Arrays;`
- Line 27: `import java.util.HashMap;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.stream.Collectors;`
- Line 31: `import java.util.stream.Stream;`
- Line 32: `import java.util.zip.GZIPInputStream;`
- Line 34: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 35: `import static org.hamcrest.Matchers.containsString;`
- Line 36: `import static org.hamcrest.Matchers.hasEntry;`
- Line 37: `import static org.hamcrest.Matchers.hasKey;`

## ../distribution/tools/java-version-checker/src/main/java/org/elasticsearch/tools/java_version_checker/JavaVersionChecker.java

### Unused Code (2)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.Locale;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/AddFileKeyStoreCommand.java

### Exception Handling (2)
- Line 51: `throw new UserException(ExitCodes.USAGE, "Missing setting name");`
- Line 54: `throw new UserException(ExitCodes.USAGE, "settings and filenames must come in pairs");`

### Unused Code (13)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.core.PathUtils;`
- Line 20: `import org.elasticsearch.core.SuppressForbidden;`
- Line 21: `import org.elasticsearch.env.Environment;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/AddStringKeyStoreCommand.java

### Resource Leak (1)
- Line 67: `final BufferedReader stdinReader = new BufferedReader(new InputStreamReader(getStdin(), StandardCharsets.UTF_8));`

### Exception Handling (1)
- Line 59: `throw new UserException(ExitCodes.USAGE, "the setting names can not be empty");`

### Unused Code (17)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.core.CheckedFunction;`
- Line 20: `import org.elasticsearch.env.Environment;`
- Line 22: `import java.io.BufferedReader;`
- Line 23: `import java.io.CharArrayWriter;`
- Line 24: `import java.io.Closeable;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.InputStream;`
- Line 27: `import java.io.InputStreamReader;`
- Line 28: `import java.nio.charset.StandardCharsets;`
- Line 29: `import java.util.Arrays;`
- Line 30: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/BaseKeyStoreCommand.java

### Unused Code (14)
- Line 29: `private KeyStoreWrapper keyStore;`
- Line 30: `private SecureString keyStorePassword;`
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.Terminal;`
- Line 18: `import org.elasticsearch.cli.UserException;`
- Line 19: `import org.elasticsearch.common.cli.KeyStoreAwareCommand;`
- Line 20: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 21: `import org.elasticsearch.common.settings.SecureString;`
- Line 22: `import org.elasticsearch.env.Environment;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.security.GeneralSecurityException;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/ChangeKeyStorePasswordCommand.java

### Unused Code (7)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.ExitCodes;`
- Line 15: `import org.elasticsearch.cli.Terminal;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 18: `import org.elasticsearch.common.settings.SecureString;`
- Line 19: `import org.elasticsearch.env.Environment;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/CreateKeyStoreCommand.java

### Exception Handling (1)
- Line 54: `throw new UserException(ExitCodes.IO_ERROR, "Error creating the elasticsearch keystore.");`

### Unused Code (13)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.Terminal;`
- Line 18: `import org.elasticsearch.cli.UserException;`
- Line 19: `import org.elasticsearch.common.cli.KeyStoreAwareCommand;`
- Line 20: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 21: `import org.elasticsearch.common.settings.SecureString;`
- Line 22: `import org.elasticsearch.env.Environment;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.Arrays;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/HasPasswordKeyStoreCommand.java

### Exception Handling (2)
- Line 42: `throw new UserException(NO_PASSWORD_EXIT_CODE, null);`
- Line 46: `throw new UserException(NO_PASSWORD_EXIT_CODE, null);`

### Unused Code (8)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.cli.Terminal;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.elasticsearch.common.cli.KeyStoreAwareCommand;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import java.nio.file.Path;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/KeyStoreCli.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.cli.MultiCommand;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/KeyStoreCliProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/ListKeyStoreCommand.java

### Unused Code (7)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Terminal;`
- Line 15: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 16: `import org.elasticsearch.env.Environment;`
- Line 18: `import java.util.ArrayList;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/RemoveSettingKeyStoreCommand.java

### Exception Handling (2)
- Line 39: `throw new UserException(ExitCodes.USAGE, "Must supply at least one setting to remove");`
- Line 44: `throw new UserException(ExitCodes.CONFIG, "Setting [" + setting + "] does not exist in the keystore.");`

### Unused Code (8)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/ShowKeyStoreCommand.java

### Exception Handling (3)
- Line 47: `throw new UserException(ExitCodes.USAGE, "Must provide a single setting name to show");`
- Line 53: `throw new UserException(ExitCodes.CONFIG, "Setting [" + settingName + "] does not exist in the keystore.");`
- Line 82: `throw new UserException(ExitCodes.IO_ERROR, "Please redirect binary output to a file instead");`

### Unused Code (16)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.bytes.BytesReference;`
- Line 19: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 20: `import org.elasticsearch.env.Environment;`
- Line 22: `import java.io.InputStream;`
- Line 23: `import java.io.OutputStream;`
- Line 24: `import java.nio.ByteBuffer;`
- Line 25: `import java.nio.CharBuffer;`
- Line 26: `import java.nio.charset.CharacterCodingException;`
- Line 27: `import java.nio.charset.CodingErrorAction;`
- Line 28: `import java.nio.charset.StandardCharsets;`
- Line 29: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/main/java/org/elasticsearch/cli/keystore/UpgradeKeyStoreCommand.java

### Unused Code (4)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Terminal;`
- Line 15: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 16: `import org.elasticsearch.env.Environment;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddFileKeyStoreCommandTests.java

### Unused Code (16)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.core.Tuple;`
- Line 20: `import org.elasticsearch.env.Environment;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.stream.Stream;`
- Line 29: `import static org.hamcrest.Matchers.anyOf;`
- Line 30: `import static org.hamcrest.Matchers.containsString;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/AddStringKeyStoreCommandTests.java

### Unused Code (14)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import java.io.ByteArrayInputStream;`
- Line 22: `import java.io.CharArrayWriter;`
- Line 23: `import java.io.InputStream;`
- Line 24: `import java.nio.charset.StandardCharsets;`
- Line 26: `import static org.hamcrest.Matchers.anyOf;`
- Line 27: `import static org.hamcrest.Matchers.containsString;`
- Line 28: `import static org.hamcrest.Matchers.hasToString;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/BootstrapTests.java

### Unused Code (16)
- Line 11: `import org.elasticsearch.bootstrap.BootstrapUtil;`
- Line 12: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 13: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 14: `import org.elasticsearch.common.settings.SecureString;`
- Line 15: `import org.elasticsearch.common.settings.Settings;`
- Line 16: `import org.elasticsearch.core.IOUtils;`
- Line 17: `import org.elasticsearch.env.Environment;`
- Line 18: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import org.junit.After;`
- Line 20: `import org.junit.Before;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.nio.file.FileSystem;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/ChangeKeyStorePasswordCommandTests.java

### Unused Code (8)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 20: `import static org.hamcrest.Matchers.anyOf;`
- Line 21: `import static org.hamcrest.Matchers.containsString;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/CreateKeyStoreCommandTests.java

### Unused Code (11)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import java.nio.charset.StandardCharsets;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.Path;`
- Line 25: `import static org.hamcrest.Matchers.containsString;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/HasPasswordKeyStoreCommandTests.java

### Unused Code (9)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.elasticsearch.env.Environment;`
- Line 19: `import static org.hamcrest.CoreMatchers.is;`
- Line 20: `import static org.hamcrest.Matchers.containsString;`
- Line 21: `import static org.hamcrest.Matchers.emptyString;`
- Line 22: `import static org.hamcrest.Matchers.nullValue;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/KeyStoreCommandTestCase.java

### Unused Code (19)
- Line 12: `import com.google.common.jimfs.Configuration;`
- Line 13: `import com.google.common.jimfs.Jimfs;`
- Line 15: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 16: `import org.elasticsearch.cli.CommandTestCase;`
- Line 17: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 18: `import org.elasticsearch.common.settings.Settings;`
- Line 19: `import org.elasticsearch.core.IOUtils;`
- Line 20: `import org.elasticsearch.core.PathUtilsForTesting;`
- Line 21: `import org.elasticsearch.env.Environment;`
- Line 22: `import org.elasticsearch.env.TestEnvironment;`
- Line 23: `import org.junit.After;`
- Line 24: `import org.junit.Before;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.InputStream;`
- Line 28: `import java.nio.file.FileSystem;`
- Line 29: `import java.nio.file.Files;`
- Line 30: `import java.nio.file.Path;`
- Line 31: `import java.util.ArrayList;`
- Line 32: `import java.util.List;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/KeyStoreWrapperTests.java

### Unused Code (48)
- Line 12: `import org.apache.lucene.backward_codecs.store.EndiannessReverserUtil;`
- Line 13: `import org.apache.lucene.codecs.CodecUtil;`
- Line 14: `import org.apache.lucene.store.Directory;`
- Line 15: `import org.apache.lucene.store.IOContext;`
- Line 16: `import org.apache.lucene.store.IndexOutput;`
- Line 17: `import org.elasticsearch.common.Randomness;`
- Line 18: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 19: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 20: `import org.elasticsearch.common.settings.SecureString;`
- Line 21: `import org.elasticsearch.core.IOUtils;`
- Line 22: `import org.elasticsearch.env.Environment;`
- Line 23: `import org.elasticsearch.test.ESTestCase;`
- Line 24: `import org.hamcrest.Matchers;`
- Line 25: `import org.junit.After;`
- Line 26: `import org.junit.Before;`
- Line 28: `import java.io.ByteArrayOutputStream;`
- Line 29: `import java.io.DataOutputStream;`
- Line 30: `import java.io.EOFException;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.io.InputStream;`
- Line 33: `import java.io.OutputStream;`
- Line 34: `import java.nio.charset.StandardCharsets;`
- Line 35: `import java.nio.file.FileSystem;`
- Line 36: `import java.nio.file.Files;`
- Line 37: `import java.nio.file.Path;`
- Line 38: `import java.security.GeneralSecurityException;`
- Line 39: `import java.security.MessageDigest;`
- Line 40: `import java.security.SecureRandom;`
- Line 41: `import java.util.ArrayList;`
- Line 42: `import java.util.Arrays;`
- Line 43: `import java.util.List;`
- Line 44: `import java.util.Locale;`
- Line 45: `import java.util.Set;`
- Line 47: `import javax.crypto.Cipher;`
- Line 48: `import javax.crypto.CipherOutputStream;`
- Line 49: `import javax.crypto.SecretKey;`
- Line 50: `import javax.crypto.SecretKeyFactory;`
- Line 51: `import javax.crypto.spec.GCMParameterSpec;`
- Line 52: `import javax.crypto.spec.PBEKeySpec;`
- Line 53: `import javax.crypto.spec.SecretKeySpec;`
- Line 55: `import static org.hamcrest.Matchers.anyOf;`
- Line 56: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 57: `import static org.hamcrest.Matchers.containsString;`
- Line 58: `import static org.hamcrest.Matchers.equalTo;`
- Line 59: `import static org.hamcrest.Matchers.hasSize;`
- Line 60: `import static org.hamcrest.Matchers.instanceOf;`
- Line 61: `import static org.hamcrest.Matchers.is;`
- Line 62: `import static org.hamcrest.Matchers.notNullValue;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/ListKeyStoreCommandTests.java

### Unused Code (10)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 20: `import java.util.List;`
- Line 22: `import static org.hamcrest.Matchers.anyOf;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`
- Line 24: `import static org.hamcrest.Matchers.equalTo;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/RemoveSettingKeyStoreCommandTests.java

### Unused Code (9)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 20: `import java.util.Set;`
- Line 22: `import static org.hamcrest.Matchers.anyOf;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/ShowKeyStoreCommandTests.java

### Unused Code (11)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ExitCodes;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import static org.hamcrest.Matchers.anyOf;`
- Line 22: `import static org.hamcrest.Matchers.contains;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`
- Line 24: `import static org.hamcrest.Matchers.equalTo;`

## ../distribution/tools/keystore-cli/src/test/java/org/elasticsearch/cli/keystore/UpgradeKeyStoreCommandTests.java

### Unused Code (15)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.Command;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 18: `import org.elasticsearch.core.Nullable;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 21: `import java.io.InputStream;`
- Line 22: `import java.io.OutputStream;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 26: `import static org.hamcrest.Matchers.containsString;`
- Line 27: `import static org.hamcrest.Matchers.equalTo;`
- Line 28: `import static org.hamcrest.Matchers.hasItem;`
- Line 29: `import static org.hamcrest.Matchers.hasToString;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/InstallPluginAction.java

### Resource Leak (1)
- Line 582: `final BufferedReader checksumReader = new BufferedReader(new InputStreamReader(in, StandardCharsets.UTF_8));`

### Concurrency Issue (5)
- Line 214: `public void setProxy(Proxy proxy) {`
- Line 484: `// for testing only`
- Line 489: `// for testing only`
- Line 206: `private Proxy proxy = null;`
- Line 498: `private static final int WIDTH = 50;`

### Exception Handling (18)
- Line 150: `throw new UncheckedIOException(e);`
- Line 160: `throw new UncheckedIOException(e);`
- Line 220: `throw new UserException(ExitCodes.USAGE, "at least one plugin id is required");`
- Line 238: `throw new UserException(ExitCodes.CONFIG, "this distribution of Elasticsearch contains X-Pack by default");`
- Line 332: `throw new UserException(ExitCodes.USAGE, msg);`
- Line 342: `throw new UserException(ExitCodes.CONFIG, "Location in ES_PLUGIN_ARCHIVE_DIR does not exist");`
- Line 345: `throw new UserException(ExitCodes.CONFIG, "Location in ES_PLUGIN_ARCHIVE_DIR is not a directory");`
- Line 366: `throw new UserException(`
- Line 572: `throw new UserException(ExitCodes.IO_ERROR, "Plugin checksum missing: " + checksumUrlString);`
- Line 589: `throw new UserException(ExitCodes.IO_ERROR, "Invalid checksum file at " + checksumUrl);`
- Line 604: `throw new UserException(ExitCodes.IO_ERROR, message);`
- Line 609: `throw new UserException(ExitCodes.IO_ERROR, "Invalid checksum file at " + checksumUrl);`
- Line 625: `throw new UserException(`
- Line 677: `throw new IllegalStateException("signature verification for [" + urlString + "] failed");`
- Line 786: `throw new UserException(`
- Line 846: `throw new UserException(ExitCodes.USAGE, "plugin '" + pluginName + "' cannot be installed as a plugin, it is a system module");`
- Line 857: `throw new UserException(PLUGIN_EXISTS, message);`
- Line 867: `throw new IllegalStateException("plugins can not have native controllers");`

### Unused Code (85)
- Line 204: `private Environment env;`
- Line 205: `private boolean batch;`
- Line 206: `private Proxy proxy = null;`
- Line 12: `import org.apache.lucene.search.spell.LevenshteinDistance;`
- Line 13: `import org.apache.lucene.util.CollectionUtil;`
- Line 14: `import org.apache.lucene.util.Constants;`
- Line 15: `import org.bouncycastle.bcpg.ArmoredInputStream;`
- Line 16: `import org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider;`
- Line 17: `import org.bouncycastle.openpgp.PGPException;`
- Line 18: `import org.bouncycastle.openpgp.PGPPublicKey;`
- Line 19: `import org.bouncycastle.openpgp.PGPPublicKeyRingCollection;`
- Line 20: `import org.bouncycastle.openpgp.PGPSignature;`
- Line 21: `import org.bouncycastle.openpgp.PGPSignatureList;`
- Line 22: `import org.bouncycastle.openpgp.PGPUtil;`
- Line 23: `import org.bouncycastle.openpgp.jcajce.JcaPGPObjectFactory;`
- Line 24: `import org.bouncycastle.openpgp.operator.jcajce.JcaKeyFingerprintCalculator;`
- Line 25: `import org.bouncycastle.openpgp.operator.jcajce.JcaPGPContentVerifierBuilderProvider;`
- Line 26: `import org.elasticsearch.Build;`
- Line 27: `import org.elasticsearch.bootstrap.PluginPolicyInfo;`
- Line 28: `import org.elasticsearch.bootstrap.PolicyUtil;`
- Line 29: `import org.elasticsearch.cli.ExitCodes;`
- Line 30: `import org.elasticsearch.cli.Terminal;`
- Line 31: `import org.elasticsearch.cli.UserException;`
- Line 32: `import org.elasticsearch.common.hash.MessageDigests;`
- Line 33: `import org.elasticsearch.common.io.Streams;`
- Line 34: `import org.elasticsearch.common.util.set.Sets;`
- Line 35: `import org.elasticsearch.core.IOUtils;`
- Line 36: `import org.elasticsearch.core.PathUtils;`
- Line 37: `import org.elasticsearch.core.SuppressForbidden;`
- Line 38: `import org.elasticsearch.core.Tuple;`
- Line 39: `import org.elasticsearch.env.Environment;`
- Line 40: `import org.elasticsearch.jdk.JarHell;`
- Line 41: `import org.elasticsearch.jdk.RuntimeVersionFeature;`
- Line 42: `import org.elasticsearch.plugin.scanner.ClassReaders;`
- Line 43: `import org.elasticsearch.plugin.scanner.NamedComponentScanner;`
- Line 44: `import org.elasticsearch.plugins.Platforms;`
- Line 45: `import org.elasticsearch.plugins.PluginDescriptor;`
- Line 46: `import org.elasticsearch.plugins.PluginsUtils;`
- Line 47: `import org.objectweb.asm.ClassReader;`
- Line 49: `import java.io.BufferedReader;`
- Line 50: `import java.io.Closeable;`
- Line 51: `import java.io.IOException;`
- Line 52: `import java.io.InputStream;`
- Line 53: `import java.io.InputStreamReader;`
- Line 54: `import java.io.OutputStream;`
- Line 55: `import java.io.UncheckedIOException;`
- Line 56: `import java.net.HttpURLConnection;`
- Line 57: `import java.net.Proxy;`
- Line 58: `import java.net.URI;`
- Line 59: `import java.net.URISyntaxException;`
- Line 60: `import java.net.URL;`
- Line 61: `import java.net.URLConnection;`
- Line 62: `import java.net.URLDecoder;`
- Line 63: `import java.nio.charset.StandardCharsets;`
- Line 64: `import java.nio.file.DirectoryStream;`
- Line 65: `import java.nio.file.FileVisitResult;`
- Line 66: `import java.nio.file.Files;`
- Line 67: `import java.nio.file.Path;`
- Line 68: `import java.nio.file.SimpleFileVisitor;`
- Line 69: `import java.nio.file.StandardCopyOption;`
- Line 70: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 71: `import java.nio.file.attribute.PosixFileAttributeView;`
- Line 72: `import java.nio.file.attribute.PosixFileAttributes;`
- Line 73: `import java.nio.file.attribute.PosixFilePermission;`
- Line 74: `import java.nio.file.attribute.PosixFilePermissions;`
- Line 75: `import java.security.MessageDigest;`
- Line 76: `import java.security.NoSuchAlgorithmException;`
- Line 77: `import java.util.ArrayList;`
- Line 78: `import java.util.Collections;`
- Line 79: `import java.util.HashSet;`
- Line 80: `import java.util.LinkedHashMap;`
- Line 81: `import java.util.List;`
- Line 82: `import java.util.Locale;`
- Line 83: `import java.util.Map;`
- Line 84: `import java.util.Objects;`
- Line 85: `import java.util.Set;`
- Line 86: `import java.util.Timer;`
- Line 87: `import java.util.TimerTask;`
- Line 88: `import java.util.regex.Matcher;`
- Line 89: `import java.util.regex.Pattern;`
- Line 90: `import java.util.stream.Collectors;`
- Line 91: `import java.util.stream.Stream;`
- Line 92: `import java.util.zip.ZipEntry;`
- Line 93: `import java.util.zip.ZipInputStream;`
- Line 95: `import static org.elasticsearch.cli.Terminal.Verbosity.VERBOSE;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/InstallPluginCommand.java

### Unused Code (10)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 19: `import org.elasticsearch.plugins.PluginDescriptor;`
- Line 21: `import java.util.Arrays;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.stream.Collectors;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/InstallablePlugin.java

### Concurrency Issue (2)
- Line 45: `public void setId(String id) {`
- Line 53: `public void setLocation(String location) {`

### Unused Code (4)
- Line 20: `private String id;`
- Line 21: `private String location;`
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 14: `import java.util.Objects;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/ListPluginsCommand.java

### Unused Code (16)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.Build;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 19: `import org.elasticsearch.plugins.PluginDescriptor;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.nio.file.DirectoryStream;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.Collections;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Objects;`
- Line 30: `import static org.elasticsearch.plugins.cli.SyncPluginsAction.ELASTICSEARCH_PLUGINS_YML_CACHE;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginCli.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 13: `import org.elasticsearch.cli.MultiCommand;`
- Line 14: `import org.elasticsearch.core.IOUtils;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.util.Collection;`
- Line 18: `import java.util.Collections;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginCliProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginSecurity.java

### Exception Handling (1)
- Line 83: `throw new UserException(ExitCodes.DATA_ERROR, "installation aborted by user");`

### Unused Code (17)
- Line 12: `import org.elasticsearch.bootstrap.PluginPolicyInfo;`
- Line 13: `import org.elasticsearch.bootstrap.PolicyUtil;`
- Line 14: `import org.elasticsearch.cli.ExitCodes;`
- Line 15: `import org.elasticsearch.cli.Terminal;`
- Line 16: `import org.elasticsearch.cli.Terminal.Verbosity;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.net.URL;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.security.Permission;`
- Line 23: `import java.security.UnresolvedPermission;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.Collections;`
- Line 26: `import java.util.HashSet;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.stream.Collectors;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/PluginsConfig.java

### Concurrency Issue (2)
- Line 45: `public void setPlugins(List<InstallablePlugin> plugins) {`
- Line 49: `public void setProxy(String proxy) {`

### Exception Handling (3)
- Line 68: `throw new RuntimeException("Cannot have null or empty IDs in [elasticsearch-plugins.yml]");`
- Line 91: `throw new PluginSyncException("Malformed [proxy], expected [host:port] in [elasticsearch-plugins.yml]");`
- Line 95: `throw new PluginSyncException("Malformed [proxy], expected [host:port] in [elasticsearch-plugins.yml]");`

### Unused Code (18)
- Line 38: `private String proxy;`
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.xcontent.ObjectParser;`
- Line 14: `import org.elasticsearch.xcontent.ParseField;`
- Line 15: `import org.elasticsearch.xcontent.XContent;`
- Line 16: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 17: `import org.elasticsearch.xcontent.XContentParser;`
- Line 18: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.io.OutputStream;`
- Line 22: `import java.net.URI;`
- Line 23: `import java.net.URISyntaxException;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.HashSet;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Objects;`
- Line 29: `import java.util.Set;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/ProgressInputStream.java

### Concurrency Issue (1)
- Line 28: `private int count = 0;`

### Unused Code (5)
- Line 27: `private int currentPercent;`
- Line 28: `private int count = 0;`
- Line 12: `import java.io.FilterInputStream;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.InputStream;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/ProxyUtils.java

### Exception Handling (2)
- Line 39: `throw new UserException(ExitCodes.CONFIG, "Malformed [proxy], expected [host:port]");`
- Line 43: `throw new UserException(ExitCodes.CONFIG, "Malformed [proxy], expected [host:port]");`

### Unused Code (6)
- Line 12: `import org.elasticsearch.cli.ExitCodes;`
- Line 13: `import org.elasticsearch.cli.UserException;`
- Line 14: `import org.elasticsearch.common.Strings;`
- Line 15: `import org.elasticsearch.core.SuppressForbidden;`
- Line 17: `import java.net.InetSocketAddress;`
- Line 18: `import java.net.Proxy;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/RemovePluginAction.java

### Concurrency Issue (2)
- Line 60: `public void setPurge(boolean purge) {`
- Line 41: `static final int PLUGIN_STILL_USED = 11;`

### Exception Handling (3)
- Line 75: `throw new UserException(ExitCodes.USAGE, "At least one plugin ID is required");`
- Line 146: `throw new UserException(ExitCodes.CONFIG, message);`
- Line 153: `throw new UserException(ExitCodes.IO_ERROR, "bin dir for " + pluginId + " is not a directory");`

### Unused Code (20)
- Line 45: `private boolean purge;`
- Line 12: `import org.elasticsearch.cli.ExitCodes;`
- Line 13: `import org.elasticsearch.cli.Terminal;`
- Line 14: `import org.elasticsearch.cli.UserException;`
- Line 15: `import org.elasticsearch.core.IOUtils;`
- Line 16: `import org.elasticsearch.env.Environment;`
- Line 17: `import org.elasticsearch.plugins.PluginsUtils;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.file.FileAlreadyExistsException;`
- Line 21: `import java.nio.file.Files;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.util.ArrayList;`
- Line 24: `import java.util.HashMap;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Locale;`
- Line 27: `import java.util.Map;`
- Line 28: `import java.util.StringJoiner;`
- Line 29: `import java.util.stream.Stream;`
- Line 31: `import static org.elasticsearch.cli.Terminal.Verbosity.VERBOSE;`
- Line 32: `import static org.elasticsearch.plugins.cli.InstallPluginAction.PLUGINS_CONVERTED_TO_MODULES;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/RemovePluginCommand.java

### Unused Code (9)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 20: `import java.util.Arrays;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.stream.Collectors;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/SyncPluginsAction.java

### Concurrency Issue (2)
- Line 47: `public static final String ELASTICSEARCH_PLUGINS_YML = "elasticsearch-plugins.yml";`
- Line 48: `public static final String ELASTICSEARCH_PLUGINS_YML_CACHE = ".elasticsearch-plugins.yml.cache";`

### Exception Handling (3)
- Line 66: `throw new UserException(`
- Line 242: `throw new RuntimeException("Couldn't find a PluginInfo for [" + eachPluginId + "], which should be impossible");`
- Line 296: `throw new PluginSyncException("Failed to list existing plugins", e);`

### Unused Code (25)
- Line 12: `import org.elasticsearch.Build;`
- Line 13: `import org.elasticsearch.cli.ExitCodes;`
- Line 14: `import org.elasticsearch.cli.Terminal;`
- Line 15: `import org.elasticsearch.cli.UserException;`
- Line 16: `import org.elasticsearch.env.Environment;`
- Line 17: `import org.elasticsearch.plugins.PluginDescriptor;`
- Line 18: `import org.elasticsearch.xcontent.cbor.CborXContent;`
- Line 19: `import org.elasticsearch.xcontent.yaml.YamlXContent;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.net.Proxy;`
- Line 23: `import java.nio.file.DirectoryStream;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Comparator;`
- Line 28: `import java.util.HashMap;`
- Line 29: `import java.util.Iterator;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Locale;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.Objects;`
- Line 34: `import java.util.Optional;`
- Line 35: `import java.util.Set;`
- Line 36: `import java.util.function.BiConsumer;`
- Line 37: `import java.util.stream.Collectors;`

## ../distribution/tools/plugin-cli/src/main/java/org/elasticsearch/plugins/cli/SyncPluginsCliProvider.java

### Exception Handling (1)
- Line 44: `throw new UserException(`

### Unused Code (12)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.Build;`
- Line 15: `import org.elasticsearch.cli.CliToolProvider;`
- Line 16: `import org.elasticsearch.cli.Command;`
- Line 17: `import org.elasticsearch.cli.ExitCodes;`
- Line 18: `import org.elasticsearch.cli.ProcessInfo;`
- Line 19: `import org.elasticsearch.cli.Terminal;`
- Line 20: `import org.elasticsearch.cli.UserException;`
- Line 21: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 22: `import org.elasticsearch.env.Environment;`
- Line 24: `import java.nio.file.Files;`
- Line 26: `import static org.elasticsearch.plugins.cli.SyncPluginsAction.ELASTICSEARCH_PLUGINS_YML;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/InstallPluginActionTests.java

### Resource Leak (1)
- Line 854: `try (BufferedReader reader = new BufferedReader(new StringReader(mockTerminal.getOutput()))) {`

### Exception Handling (3)
- Line 189: `throw new RuntimeException(e);`
- Line 1053: `throw new UnsupportedOperationException("verify signature should not be called for unofficial plugins");`
- Line 1485: `throw new RuntimeException(e);`

### Unused Code (115)
- Line 125: `private InstallPluginAction skipJarHellAction;`
- Line 126: `private InstallPluginAction defaultAction;`
- Line 129: `private MockTerminal terminal;`
- Line 131: `private Path pluginDir;`
- Line 132: `private NamedComponentScanner namedComponentScanner;`
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 13: `import com.google.common.jimfs.Configuration;`
- Line 14: `import com.google.common.jimfs.Jimfs;`
- Line 16: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 17: `import org.bouncycastle.bcpg.ArmoredOutputStream;`
- Line 18: `import org.bouncycastle.bcpg.BCPGOutputStream;`
- Line 19: `import org.bouncycastle.bcpg.HashAlgorithmTags;`
- Line 20: `import org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider;`
- Line 21: `import org.bouncycastle.openpgp.PGPEncryptedData;`
- Line 22: `import org.bouncycastle.openpgp.PGPException;`
- Line 23: `import org.bouncycastle.openpgp.PGPKeyPair;`
- Line 24: `import org.bouncycastle.openpgp.PGPPrivateKey;`
- Line 25: `import org.bouncycastle.openpgp.PGPPublicKey;`
- Line 26: `import org.bouncycastle.openpgp.PGPSecretKey;`
- Line 27: `import org.bouncycastle.openpgp.PGPSignature;`
- Line 28: `import org.bouncycastle.openpgp.PGPSignatureGenerator;`
- Line 29: `import org.bouncycastle.openpgp.operator.PGPDigestCalculator;`
- Line 30: `import org.bouncycastle.openpgp.operator.jcajce.JcaPGPContentSignerBuilder;`
- Line 31: `import org.bouncycastle.openpgp.operator.jcajce.JcaPGPDigestCalculatorProviderBuilder;`
- Line 32: `import org.bouncycastle.openpgp.operator.jcajce.JcaPGPKeyPair;`
- Line 33: `import org.bouncycastle.openpgp.operator.jcajce.JcePBESecretKeyDecryptorBuilder;`
- Line 34: `import org.bouncycastle.openpgp.operator.jcajce.JcePBESecretKeyEncryptorBuilder;`
- Line 35: `import org.elasticsearch.Build;`
- Line 36: `import org.elasticsearch.cli.ExitCodes;`
- Line 37: `import org.elasticsearch.cli.MockTerminal;`
- Line 38: `import org.elasticsearch.cli.ProcessInfo;`
- Line 39: `import org.elasticsearch.cli.Terminal;`
- Line 40: `import org.elasticsearch.cli.UserException;`
- Line 41: `import org.elasticsearch.common.hash.MessageDigests;`
- Line 42: `import org.elasticsearch.common.io.FileSystemUtils;`
- Line 43: `import org.elasticsearch.common.settings.Settings;`
- Line 44: `import org.elasticsearch.core.PathUtils;`
- Line 45: `import org.elasticsearch.core.PathUtilsForTesting;`
- Line 46: `import org.elasticsearch.core.Strings;`
- Line 47: `import org.elasticsearch.core.SuppressForbidden;`
- Line 48: `import org.elasticsearch.core.Tuple;`
- Line 49: `import org.elasticsearch.env.Environment;`
- Line 50: `import org.elasticsearch.env.TestEnvironment;`
- Line 51: `import org.elasticsearch.jdk.RuntimeVersionFeature;`
- Line 52: `import org.elasticsearch.plugin.scanner.NamedComponentScanner;`
- Line 53: `import org.elasticsearch.plugins.Platforms;`
- Line 54: `import org.elasticsearch.plugins.PluginDescriptor;`
- Line 55: `import org.elasticsearch.plugins.PluginTestUtil;`
- Line 56: `import org.elasticsearch.test.ESTestCase;`
- Line 57: `import org.elasticsearch.test.PosixPermissionsResetter;`
- Line 58: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 59: `import org.elasticsearch.test.jar.JarUtils;`
- Line 60: `import org.junit.After;`
- Line 61: `import org.junit.Before;`
- Line 63: `import java.io.BufferedReader;`
- Line 64: `import java.io.ByteArrayInputStream;`
- Line 65: `import java.io.ByteArrayOutputStream;`
- Line 66: `import java.io.FileNotFoundException;`
- Line 67: `import java.io.IOException;`
- Line 68: `import java.io.InputStream;`
- Line 69: `import java.io.StringReader;`
- Line 70: `import java.net.MalformedURLException;`
- Line 71: `import java.net.URI;`
- Line 72: `import java.net.URL;`
- Line 73: `import java.nio.charset.StandardCharsets;`
- Line 74: `import java.nio.file.DirectoryStream;`
- Line 75: `import java.nio.file.FileAlreadyExistsException;`
- Line 76: `import java.nio.file.FileSystem;`
- Line 77: `import java.nio.file.Files;`
- Line 78: `import java.nio.file.Path;`
- Line 79: `import java.nio.file.StandardCopyOption;`
- Line 80: `import java.nio.file.attribute.GroupPrincipal;`
- Line 81: `import java.nio.file.attribute.PosixFileAttributeView;`
- Line 82: `import java.nio.file.attribute.PosixFileAttributes;`
- Line 83: `import java.nio.file.attribute.PosixFilePermission;`
- Line 84: `import java.nio.file.attribute.UserPrincipal;`
- Line 85: `import java.security.KeyPair;`
- Line 86: `import java.security.KeyPairGenerator;`
- Line 87: `import java.security.MessageDigest;`
- Line 88: `import java.security.NoSuchAlgorithmException;`
- Line 89: `import java.util.ArrayList;`
- Line 90: `import java.util.Arrays;`
- Line 91: `import java.util.Date;`
- Line 92: `import java.util.HashSet;`
- Line 93: `import java.util.List;`
- Line 94: `import java.util.Locale;`
- Line 95: `import java.util.Map;`
- Line 96: `import java.util.Set;`
- Line 97: `import java.util.concurrent.CountDownLatch;`
- Line 98: `import java.util.function.BiFunction;`
- Line 99: `import java.util.function.Function;`
- Line 100: `import java.util.stream.Collectors;`
- Line 101: `import java.util.stream.Stream;`
- Line 102: `import java.util.zip.ZipEntry;`
- Line 103: `import java.util.zip.ZipOutputStream;`
- Line 105: `import static org.elasticsearch.snapshots.AbstractSnapshotIntegTestCase.forEachFileRecursively;`
- Line 106: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 107: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 108: `import static org.hamcrest.Matchers.containsString;`
- Line 109: `import static org.hamcrest.Matchers.empty;`
- Line 110: `import static org.hamcrest.Matchers.endsWith;`
- Line 111: `import static org.hamcrest.Matchers.hasToString;`
- Line 112: `import static org.hamcrest.Matchers.matchesRegex;`
- Line 113: `import static org.hamcrest.Matchers.not;`
- Line 114: `import static org.hamcrest.Matchers.nullValue;`
- Line 115: `import static org.hamcrest.Matchers.startsWith;`
- Line 116: `import static org.mockito.ArgumentMatchers.any;`
- Line 117: `import static org.mockito.Mockito.doAnswer;`
- Line 118: `import static org.mockito.Mockito.doCallRealMethod;`
- Line 119: `import static org.mockito.Mockito.doReturn;`
- Line 120: `import static org.mockito.Mockito.spy;`
- Line 272: `import org.elasticsearch.plugin.*;`
- Line 273: `import org.elasticsearch.plugins.cli.test_model.*;`
- Line 278: `import org.elasticsearch.plugin.*;`
- Line 279: `import org.elasticsearch.plugins.cli.test_model.*;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/ListPluginsCommandTests.java

### Unused Code (23)
- Line 40: `private Path home;`
- Line 41: `private Environment env;`
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 15: `import org.elasticsearch.Version;`
- Line 16: `import org.elasticsearch.cli.Command;`
- Line 17: `import org.elasticsearch.cli.CommandTestCase;`
- Line 18: `import org.elasticsearch.cli.ProcessInfo;`
- Line 19: `import org.elasticsearch.common.settings.Settings;`
- Line 20: `import org.elasticsearch.env.Environment;`
- Line 21: `import org.elasticsearch.env.TestEnvironment;`
- Line 22: `import org.elasticsearch.plugins.PluginTestUtil;`
- Line 23: `import org.junit.Before;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.util.Arrays;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.stream.Collectors;`
- Line 32: `import static org.hamcrest.Matchers.containsString;`
- Line 33: `import static org.hamcrest.Matchers.emptyString;`
- Line 34: `import static org.hamcrest.Matchers.equalTo;`
- Line 35: `import static org.hamcrest.Matchers.startsWith;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/MockInstallPluginCommand.java

### Unused Code (4)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.cli.UserException;`
- Line 16: `import org.elasticsearch.env.Environment;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/MockRemovePluginCommand.java

### Unused Code (3)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.env.Environment;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/PluginsConfigTests.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.List;`
- Line 16: `import java.util.Set;`
- Line 17: `import java.util.stream.Stream;`
- Line 19: `import static org.hamcrest.Matchers.equalTo;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/ProgressInputStreamTests.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.List;`
- Line 17: `import static org.hamcrest.Matchers.hasItem;`
- Line 18: `import static org.hamcrest.Matchers.hasItems;`
- Line 19: `import static org.hamcrest.Matchers.hasSize;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/ProxyMatcher.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.hamcrest.Description;`
- Line 14: `import org.hamcrest.TypeSafeMatcher;`
- Line 16: `import java.net.InetSocketAddress;`
- Line 17: `import java.net.Proxy;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/ProxyUtilsTests.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.cli.UserException;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.net.Proxy.Type;`
- Line 16: `import java.util.stream.Stream;`
- Line 18: `import static org.elasticsearch.plugins.cli.ProxyMatcher.matchesProxy;`
- Line 19: `import static org.elasticsearch.plugins.cli.ProxyUtils.buildProxy;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`
- Line 21: `import static org.hamcrest.Matchers.is;`
- Line 22: `import static org.hamcrest.Matchers.nullValue;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/RemovePluginActionTests.java

### Resource Leak (2)
- Line 231: `BufferedReader reader = new BufferedReader(new StringReader(terminal.getOutput()));`
- Line 232: `BufferedReader errorReader = new BufferedReader(new StringReader(terminal.getErrorOutput()))`

### Unused Code (29)
- Line 45: `private Path home;`
- Line 46: `private Environment env;`
- Line 12: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 13: `import org.elasticsearch.Version;`
- Line 14: `import org.elasticsearch.cli.ExitCodes;`
- Line 15: `import org.elasticsearch.cli.MockTerminal;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.settings.Settings;`
- Line 19: `import org.elasticsearch.env.Environment;`
- Line 20: `import org.elasticsearch.env.TestEnvironment;`
- Line 21: `import org.elasticsearch.plugins.PluginTestUtil;`
- Line 22: `import org.elasticsearch.test.ESTestCase;`
- Line 23: `import org.junit.Before;`
- Line 25: `import java.io.BufferedReader;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.StringReader;`
- Line 28: `import java.nio.file.DirectoryStream;`
- Line 29: `import java.nio.file.Files;`
- Line 30: `import java.nio.file.Path;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.stream.Collectors;`
- Line 35: `import static java.util.Collections.emptyList;`
- Line 36: `import static org.hamcrest.CoreMatchers.containsString;`
- Line 37: `import static org.hamcrest.CoreMatchers.not;`
- Line 38: `import static org.hamcrest.CoreMatchers.nullValue;`
- Line 39: `import static org.hamcrest.Matchers.equalTo;`
- Line 40: `import static org.hamcrest.Matchers.is;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/SyncPluginsActionTests.java

### Unused Code (34)
- Line 46: `private Environment env;`
- Line 47: `private SyncPluginsAction action;`
- Line 48: `private PluginsConfig config;`
- Line 49: `private MockTerminal terminal;`
- Line 11: `import org.apache.lucene.tests.util.LuceneTestCase;`
- Line 12: `import org.elasticsearch.Build;`
- Line 13: `import org.elasticsearch.cli.MockTerminal;`
- Line 14: `import org.elasticsearch.cli.UserException;`
- Line 15: `import org.elasticsearch.common.settings.Settings;`
- Line 16: `import org.elasticsearch.env.Environment;`
- Line 17: `import org.elasticsearch.env.TestEnvironment;`
- Line 18: `import org.elasticsearch.plugins.PluginTestUtil;`
- Line 19: `import org.elasticsearch.plugins.cli.SyncPluginsAction.PluginChanges;`
- Line 20: `import org.elasticsearch.test.ESTestCase;`
- Line 21: `import org.elasticsearch.test.VersionUtils;`
- Line 22: `import org.hamcrest.Matchers;`
- Line 23: `import org.junit.Before;`
- Line 24: `import org.mockito.InOrder;`
- Line 25: `import org.mockito.Mockito;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.nio.file.Files;`
- Line 29: `import java.nio.file.Path;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Objects;`
- Line 32: `import java.util.Optional;`
- Line 34: `import static org.hamcrest.Matchers.containsString;`
- Line 35: `import static org.hamcrest.Matchers.empty;`
- Line 36: `import static org.hamcrest.Matchers.equalTo;`
- Line 37: `import static org.hamcrest.Matchers.hasSize;`
- Line 38: `import static org.hamcrest.Matchers.is;`
- Line 39: `import static org.mockito.ArgumentMatchers.anyList;`
- Line 40: `import static org.mockito.Mockito.mock;`
- Line 41: `import static org.mockito.Mockito.never;`
- Line 42: `import static org.mockito.Mockito.verify;`

## ../distribution/tools/plugin-cli/src/test/java/org/elasticsearch/plugins/cli/test_model/ExtensibleInterface.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.Extensible;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/APMJvmOptions.java

### Exception Handling (4)
- Line 235: `throw new UserException(`
- Line 322: `throw new UserException(`
- Line 336: `throw new UserException(`
- Line 343: `throw new UserException(`

### Unused Code (20)
- Line 12: `import org.elasticsearch.Build;`
- Line 13: `import org.elasticsearch.cli.ExitCodes;`
- Line 14: `import org.elasticsearch.cli.UserException;`
- Line 15: `import org.elasticsearch.common.Strings;`
- Line 16: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 17: `import org.elasticsearch.common.settings.SecureString;`
- Line 18: `import org.elasticsearch.common.settings.Settings;`
- Line 19: `import org.elasticsearch.core.Nullable;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.io.OutputStream;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.Iterator;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Properties;`
- Line 31: `import java.util.Set;`
- Line 32: `import java.util.StringJoiner;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/DefaultSystemMemoryInfo.java

### Unused Code (4)
- Line 12: `import com.sun.management.OperatingSystemMXBean;`
- Line 14: `import org.elasticsearch.core.SuppressForbidden;`
- Line 16: `import java.lang.management.ManagementFactory;`
- Line 17: `import java.util.function.LongSupplier;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ErrorPumpThread.java

### Resource Leak (1)
- Line 50: `this.reader = new BufferedReader(new InputStreamReader(errInput, StandardCharsets.UTF_8));`

### Concurrency Issue (1)
- Line 40: `private final CountDownLatch readyOrDead = new CountDownLatch(1);`

### Unused Code (13)
- Line 12: `import org.elasticsearch.bootstrap.BootstrapInfo;`
- Line 13: `import org.elasticsearch.cli.Terminal;`
- Line 14: `import org.elasticsearch.cli.Terminal.Verbosity;`
- Line 16: `import java.io.BufferedReader;`
- Line 17: `import java.io.Closeable;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.io.InputStream;`
- Line 20: `import java.io.InputStreamReader;`
- Line 21: `import java.nio.charset.StandardCharsets;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.concurrent.CountDownLatch;`
- Line 25: `import static org.elasticsearch.bootstrap.BootstrapInfo.SERVER_READY_MARKER;`
- Line 26: `import static org.elasticsearch.server.cli.ProcessUtil.nonInterruptibleVoid;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/JvmErgonomics.java

### Exception Handling (1)
- Line 121: `throw new IllegalStateException(`

### Unused Code (12)
- Line 12: `import org.elasticsearch.cluster.node.DiscoveryNodeRole;`
- Line 13: `import org.elasticsearch.common.settings.Settings;`
- Line 14: `import org.elasticsearch.common.unit.ByteSizeUnit;`
- Line 15: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 16: `import org.elasticsearch.node.NodeRoleSettings;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.regex.Matcher;`
- Line 24: `import java.util.regex.Pattern;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/JvmOption.java

### Resource Leak (1)
- Line 128: `try (InputStreamReader isr = new InputStreamReader(is, StandardCharsets.UTF_8); BufferedReader br = new BufferedReader(isr)) {`

### Concurrency Issue (1)
- Line 56: `private static final Pattern OPTION = Pattern.compile(`

### Exception Handling (1)
- Line 121: `throw new RuntimeException(message);`

### Unused Code (16)
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 14: `import java.io.BufferedReader;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.io.InputStream;`
- Line 17: `import java.io.InputStreamReader;`
- Line 18: `import java.nio.charset.StandardCharsets;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Locale;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.Optional;`
- Line 24: `import java.util.function.Function;`
- Line 25: `import java.util.regex.Matcher;`
- Line 26: `import java.util.regex.Pattern;`
- Line 27: `import java.util.stream.Collectors;`
- Line 28: `import java.util.stream.Stream;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/JvmOptionsParser.java

### Resource Leak (1)
- Line 183: `BufferedReader br = new BufferedReader(reader)`

### Exception Handling (1)
- Line 188: `throw new JvmOptionsFileParserException(jvmOptionsFile, invalidLines);`

### Unused Code (27)
- Line 12: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 13: `import org.elasticsearch.cli.ExitCodes;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.cli.UserException;`
- Line 17: `import java.io.BufferedReader;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.io.InputStream;`
- Line 20: `import java.io.InputStreamReader;`
- Line 21: `import java.io.Reader;`
- Line 22: `import java.nio.charset.StandardCharsets;`
- Line 23: `import java.nio.file.DirectoryStream;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Arrays;`
- Line 28: `import java.util.Collections;`
- Line 29: `import java.util.HashMap;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Locale;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.SortedMap;`
- Line 34: `import java.util.TreeMap;`
- Line 35: `import java.util.function.Predicate;`
- Line 36: `import java.util.regex.Matcher;`
- Line 37: `import java.util.regex.Pattern;`
- Line 38: `import java.util.stream.Collectors;`
- Line 39: `import java.util.stream.StreamSupport;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/KeyStoreLoader.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.cli.Terminal;`
- Line 13: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 14: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 15: `import org.elasticsearch.common.settings.SecureString;`
- Line 16: `import org.elasticsearch.env.Environment;`
- Line 18: `import java.util.Optional;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/KeystorePasswordTerminal.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.cli.Terminal;`
- Line 13: `import org.elasticsearch.common.settings.SecureString;`
- Line 15: `import java.io.Closeable;`
- Line 16: `import java.io.OutputStream;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/MachineDependentHeap.java

### Concurrency Issue (3)
- Line 36: `protected static final long GB = 1024L * 1024L * 1024L; // 1GB`
- Line 37: `protected static final long MAX_HEAP_SIZE = GB * 31; // 31GB`
- Line 38: `protected static final long MIN_HEAP_SIZE = 1024 * 1024 * 128; // 128MB`

### Unused Code (17)
- Line 12: `import org.elasticsearch.cluster.node.DiscoveryNodeRole;`
- Line 13: `import org.elasticsearch.common.settings.Settings;`
- Line 14: `import org.elasticsearch.node.NodeRoleSettings;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.util.Arrays;`
- Line 18: `import java.util.Collection;`
- Line 19: `import java.util.Collections;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 23: `import static java.lang.Math.max;`
- Line 24: `import static java.lang.Math.min;`
- Line 25: `import static org.elasticsearch.cluster.node.DiscoveryNodeRole.MASTER_ROLE;`
- Line 26: `import static org.elasticsearch.cluster.node.DiscoveryNodeRole.ML_ROLE;`
- Line 27: `import static org.elasticsearch.cluster.node.DiscoveryNodeRole.REMOTE_CLUSTER_CLIENT_ROLE;`
- Line 28: `import static org.elasticsearch.server.cli.JvmOption.isInitialHeapSpecified;`
- Line 29: `import static org.elasticsearch.server.cli.JvmOption.isMaxHeapSpecified;`
- Line 30: `import static org.elasticsearch.server.cli.JvmOption.isMinHeapSpecified;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/OverridableSystemMemoryInfo.java

### Null Pointer (1)
- Line 33: `return userDefinedJvmOptions.stream()`

### Exception Handling (2)
- Line 39: `throw new IllegalArgumentException("Negative memory size specified in [" + totalMemoryBytesOption + "]");`
- Line 43: `throw new IllegalArgumentException("Unable to parse number of bytes from [" + totalMemoryBytesOption + "]", e);`

### Unused Code (2)
- Line 12: `import java.util.List;`
- Line 13: `import java.util.Objects;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/SecureSettingsLoader.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.cli.Terminal;`
- Line 13: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 14: `import org.elasticsearch.common.settings.SecureString;`
- Line 15: `import org.elasticsearch.env.Environment;`
- Line 17: `import java.util.Optional;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ServerCli.java

### Concurrency Issue (1)
- Line 50: `private final AtomicBoolean shuttingDown = new AtomicBoolean(false);`

### Exception Handling (6)
- Line 98: `throw new UserException(ExitCodes.CONFIG, "Elasticsearch secure settings not configured");`
- Line 131: `throw new UserException(exitCode, "Elasticsearch exited unexpectedly");`
- Line 150: `throw new UserException(ExitCodes.USAGE, "Multiple --enrollment-token parameters are not allowed");`
- Line 155: `throw new UserException(ExitCodes.CONFIG, "Missing logging config file at " + log4jConfig);`
- Line 223: `throw new UserException(ExitCodes.USAGE, "pid file parent [" + parent + "] exists but is not a directory");`
- Line 226: `throw new UserException(ExitCodes.USAGE, pidFile + " exists but is not a regular file");`

### Unused Code (23)
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 14: `import joptsimple.OptionSpecBuilder;`
- Line 15: `import joptsimple.util.PathConverter;`
- Line 17: `import org.elasticsearch.Build;`
- Line 18: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 19: `import org.elasticsearch.cli.CliToolProvider;`
- Line 20: `import org.elasticsearch.cli.Command;`
- Line 21: `import org.elasticsearch.cli.ExitCodes;`
- Line 22: `import org.elasticsearch.cli.ProcessInfo;`
- Line 23: `import org.elasticsearch.cli.Terminal;`
- Line 24: `import org.elasticsearch.cli.UserException;`
- Line 25: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 26: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 27: `import org.elasticsearch.common.settings.SecureString;`
- Line 28: `import org.elasticsearch.env.Environment;`
- Line 29: `import org.elasticsearch.monitor.jvm.JvmInfo;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.nio.file.Files;`
- Line 33: `import java.nio.file.Path;`
- Line 34: `import java.util.Arrays;`
- Line 35: `import java.util.Locale;`
- Line 36: `import java.util.concurrent.atomic.AtomicBoolean;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ServerCliProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ServerProcess.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.bootstrap.BootstrapInfo;`
- Line 13: `import org.elasticsearch.core.IOUtils;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.io.OutputStream;`
- Line 18: `import static org.elasticsearch.server.cli.ProcessUtil.nonInterruptible;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ServerProcessBuilder.java

### Exception Handling (3)
- Line 167: `throw new UserException(exitCode, "Elasticsearch died while starting up");`
- Line 171: `throw new RuntimeException(e);`
- Line 173: `throw new UncheckedIOException(e);`

### Unused Code (19)
- Line 42: `private Path tempDir;`
- Line 43: `private ServerArgs serverArgs;`
- Line 44: `private ProcessInfo processInfo;`
- Line 46: `private Terminal terminal;`
- Line 12: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 13: `import org.elasticsearch.cli.ProcessInfo;`
- Line 14: `import org.elasticsearch.cli.Terminal;`
- Line 15: `import org.elasticsearch.cli.UserException;`
- Line 16: `import org.elasticsearch.common.Strings;`
- Line 17: `import org.elasticsearch.common.io.stream.OutputStreamStreamOutput;`
- Line 18: `import org.elasticsearch.core.PathUtils;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.io.OutputStream;`
- Line 22: `import java.io.UncheckedIOException;`
- Line 23: `import java.nio.file.Path;`
- Line 24: `import java.util.HashMap;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.stream.Stream;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/ServerProcessUtils.java

### Exception Handling (3)
- Line 38: `throw new UserException(ExitCodes.CONFIG, "Temporary directory [" + path + "] does not exist or is not accessible");`
- Line 41: `throw new UserException(ExitCodes.CONFIG, "Temporary directory [" + path + "] is not a directory");`
- Line 57: `throw new UncheckedIOException(e);`

### Unused Code (10)
- Line 12: `import org.elasticsearch.cli.ExitCodes;`
- Line 13: `import org.elasticsearch.cli.ProcessInfo;`
- Line 14: `import org.elasticsearch.cli.UserException;`
- Line 15: `import org.elasticsearch.core.SuppressForbidden;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.io.UncheckedIOException;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.nio.file.Path;`
- Line 21: `import java.nio.file.Paths;`
- Line 22: `import java.nio.file.attribute.FileAttribute;`

## ../distribution/tools/server-cli/src/main/java/org/elasticsearch/server/cli/SystemJvmOptions.java

### Exception Handling (2)
- Line 169: `throw new IllegalStateException("Directory for entitlement bridge jar does not exist: " + dir);`
- Line 179: `throw new IllegalStateException("Failed to list entitlement jars in: " + dir, e);`

### Unused Code (10)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 14: `import org.elasticsearch.jdk.RuntimeVersionFeature;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.stream.Stream;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/APMJvmOptionsTests.java

### Unused Code (28)
- Line 44: `private Path installDir;`
- Line 45: `private Path agentPath;`
- Line 12: `import org.elasticsearch.cli.UserException;`
- Line 13: `import org.elasticsearch.common.settings.MockSecureSettings;`
- Line 14: `import org.elasticsearch.common.settings.Settings;`
- Line 15: `import org.elasticsearch.monitor.jvm.JvmInfo;`
- Line 16: `import org.elasticsearch.node.Node;`
- Line 17: `import org.elasticsearch.test.ESTestCase;`
- Line 18: `import org.junit.After;`
- Line 19: `import org.junit.Before;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.Path;`
- Line 24: `import java.util.Arrays;`
- Line 25: `import java.util.HashMap;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.Map;`
- Line 29: `import static org.elasticsearch.test.MapMatcher.matchesMap;`
- Line 30: `import static org.hamcrest.Matchers.allOf;`
- Line 31: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 32: `import static org.hamcrest.Matchers.endsWith;`
- Line 33: `import static org.hamcrest.Matchers.equalTo;`
- Line 34: `import static org.hamcrest.Matchers.hasEntry;`
- Line 35: `import static org.hamcrest.Matchers.hasKey;`
- Line 36: `import static org.hamcrest.Matchers.hasSize;`
- Line 37: `import static org.hamcrest.Matchers.not;`
- Line 38: `import static org.mockito.Mockito.doReturn;`
- Line 39: `import static org.mockito.Mockito.mock;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/JvmErgonomicsTests.java

### Unused Code (29)
- Line 12: `import org.apache.lucene.tests.util.LuceneTestCase.SuppressFileSystems;`
- Line 13: `import org.elasticsearch.cluster.node.DiscoveryNodeRole;`
- Line 14: `import org.elasticsearch.common.settings.Settings;`
- Line 15: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 16: `import org.elasticsearch.node.NodeRoleSettings;`
- Line 17: `import org.elasticsearch.test.ESTestCase;`
- Line 18: `import org.elasticsearch.test.ESTestCase.WithoutSecurityManager;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.util.ArrayList;`
- Line 22: `import java.util.Arrays;`
- Line 23: `import java.util.Collections;`
- Line 24: `import java.util.HashMap;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.stream.IntStream;`
- Line 29: `import static org.hamcrest.Matchers.allOf;`
- Line 30: `import static org.hamcrest.Matchers.containsString;`
- Line 31: `import static org.hamcrest.Matchers.equalTo;`
- Line 32: `import static org.hamcrest.Matchers.everyItem;`
- Line 33: `import static org.hamcrest.Matchers.greaterThan;`
- Line 34: `import static org.hamcrest.Matchers.hasItem;`
- Line 35: `import static org.hamcrest.Matchers.hasToString;`
- Line 36: `import static org.hamcrest.Matchers.is;`
- Line 37: `import static org.hamcrest.Matchers.not;`
- Line 38: `import static org.hamcrest.Matchers.startsWith;`
- Line 39: `import static org.junit.Assert.assertEquals;`
- Line 40: `import static org.junit.Assert.assertThat;`
- Line 41: `import static org.junit.Assert.assertTrue;`
- Line 42: `import static org.junit.Assert.fail;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/JvmOptionsParserTests.java

### Resource Leak (10)
- Line 72: `try (StringReader sr = new StringReader("-Xms1g\n-Xmx1g"); BufferedReader br = new BufferedReader(sr)) {`
- Line 91: `BufferedReader br = new BufferedReader(sr)`
- Line 111: `BufferedReader br = new BufferedReader(sr)`
- Line 137: `BufferedReader br = new BufferedReader(sr)`
- Line 165: `BufferedReader br = new BufferedReader(sr)`
- Line 301: `try (StringReader sr = new StringReader("XX:+UseG1GC"); BufferedReader br = new BufferedReader(sr)) {`
- Line 319: `try (StringReader sr = new StringReader(invalidRangeLine); BufferedReader br = new BufferedReader(sr)) {`
- Line 331: `try (StringReader sr = new StringReader(numberFormatExceptionsLine); BufferedReader br = new BufferedReader(sr)) {`
- Line 339: `try (StringReader sr = new StringReader(multipleInvalidLines); BufferedReader br = new BufferedReader(sr)) {`
- Line 349: `try (StringReader sr = new StringReader(upperBoundGreaterThanLowerBound); BufferedReader br = new BufferedReader(sr)) {`

### Unused Code (30)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 14: `import org.elasticsearch.core.IOUtils;`
- Line 15: `import org.elasticsearch.core.Strings;`
- Line 16: `import org.elasticsearch.test.ESTestCase;`
- Line 17: `import org.elasticsearch.test.ESTestCase.WithoutSecurityManager;`
- Line 18: `import org.junit.AfterClass;`
- Line 19: `import org.junit.BeforeClass;`
- Line 21: `import java.io.BufferedReader;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.io.StringReader;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.NoSuchFileException;`
- Line 26: `import java.nio.file.Path;`
- Line 27: `import java.nio.file.StandardOpenOption;`
- Line 28: `import java.util.Arrays;`
- Line 29: `import java.util.Collections;`
- Line 30: `import java.util.HashMap;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Locale;`
- Line 33: `import java.util.Map;`
- Line 34: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 36: `import static org.hamcrest.Matchers.contains;`
- Line 37: `import static org.hamcrest.Matchers.containsString;`
- Line 38: `import static org.hamcrest.Matchers.empty;`
- Line 39: `import static org.hamcrest.Matchers.equalTo;`
- Line 40: `import static org.hamcrest.Matchers.hasItem;`
- Line 41: `import static org.hamcrest.Matchers.hasKey;`
- Line 42: `import static org.hamcrest.Matchers.hasSize;`
- Line 43: `import static org.hamcrest.Matchers.not;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/MachineDependentHeapTests.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import org.elasticsearch.test.ESTestCase.WithoutSecurityManager;`
- Line 15: `import org.hamcrest.Matcher;`
- Line 17: `import java.util.Collections;`
- Line 18: `import java.util.List;`
- Line 20: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 21: `import static org.hamcrest.Matchers.empty;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/OverridableSystemMemoryInfoTests.java

### Concurrency Issue (1)
- Line 22: `private static final long FALLBACK = -1L;`

### Unused Code (5)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.util.List;`
- Line 16: `import static org.hamcrest.Matchers.is;`
- Line 17: `import static org.junit.Assert.assertThat;`
- Line 18: `import static org.junit.Assert.fail;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/ServerCliTests.java

### Exception Handling (1)
- Line 329: `throw new InterruptedException("interrupted while get jvm options");`

### Unused Code (43)
- Line 60: `private SecureSettingsLoader mockSecureSettingsLoader;`
- Line 12: `import joptsimple.OptionSet;`
- Line 13: `import joptsimple.OptionSpec;`
- Line 15: `import org.elasticsearch.Build;`
- Line 16: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 17: `import org.elasticsearch.cli.Command;`
- Line 18: `import org.elasticsearch.cli.CommandTestCase;`
- Line 19: `import org.elasticsearch.cli.ExitCodes;`
- Line 20: `import org.elasticsearch.cli.ProcessInfo;`
- Line 21: `import org.elasticsearch.cli.Terminal;`
- Line 22: `import org.elasticsearch.cli.Terminal.Verbosity;`
- Line 23: `import org.elasticsearch.cli.UserException;`
- Line 24: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 25: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 26: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 27: `import org.elasticsearch.common.settings.SecureString;`
- Line 28: `import org.elasticsearch.common.settings.Settings;`
- Line 29: `import org.elasticsearch.env.Environment;`
- Line 30: `import org.elasticsearch.monitor.jvm.JvmInfo;`
- Line 31: `import org.hamcrest.Matcher;`
- Line 32: `import org.junit.Before;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.nio.file.Files;`
- Line 36: `import java.nio.file.Path;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Locale;`
- Line 39: `import java.util.Optional;`
- Line 40: `import java.util.concurrent.BrokenBarrierException;`
- Line 41: `import java.util.concurrent.CyclicBarrier;`
- Line 42: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 43: `import java.util.concurrent.atomic.AtomicReference;`
- Line 44: `import java.util.function.Consumer;`
- Line 46: `import static org.hamcrest.CoreMatchers.containsString;`
- Line 47: `import static org.hamcrest.CoreMatchers.equalTo;`
- Line 48: `import static org.hamcrest.Matchers.allOf;`
- Line 49: `import static org.hamcrest.Matchers.emptyString;`
- Line 50: `import static org.hamcrest.Matchers.greaterThan;`
- Line 51: `import static org.hamcrest.Matchers.hasItem;`
- Line 52: `import static org.hamcrest.Matchers.hasSize;`
- Line 53: `import static org.hamcrest.Matchers.is;`
- Line 54: `import static org.hamcrest.Matchers.matchesRegex;`
- Line 55: `import static org.hamcrest.Matchers.not;`
- Line 56: `import static org.hamcrest.Matchers.sameInstance;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/ServerProcessTests.java

### Null Pointer (1)
- Line 100: `forceStopCallback = null;`

### Concurrency Issue (6)
- Line 65: `final MockTerminal terminal = MockTerminal.create();`
- Line 111: `private final PipedOutputStream processStdin = new PipedOutputStream();`
- Line 112: `private final PipedInputStream processStderr = new PipedInputStream();`
- Line 113: `private final PipedInputStream stdin = new PipedInputStream();`
- Line 114: `private final PipedOutputStream stderr = new PipedOutputStream();`
- Line 116: `private final AtomicInteger exitCode = new AtomicInteger();`

### Exception Handling (1)
- Line 185: `throw new IllegalThreadStateException(); // match spec`

### Unused Code (47)
- Line 12: `import org.elasticsearch.bootstrap.BootstrapInfo;`
- Line 13: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 14: `import org.elasticsearch.cli.ExitCodes;`
- Line 15: `import org.elasticsearch.cli.MockTerminal;`
- Line 16: `import org.elasticsearch.cli.ProcessInfo;`
- Line 17: `import org.elasticsearch.cli.UserException;`
- Line 18: `import org.elasticsearch.common.io.stream.InputStreamStreamInput;`
- Line 19: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 20: `import org.elasticsearch.common.settings.SecureSettings;`
- Line 21: `import org.elasticsearch.common.settings.Settings;`
- Line 22: `import org.elasticsearch.core.IOUtils;`
- Line 23: `import org.elasticsearch.test.ESTestCase;`
- Line 24: `import org.junit.AfterClass;`
- Line 25: `import org.junit.Before;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.InputStream;`
- Line 29: `import java.io.OutputStream;`
- Line 30: `import java.io.PipedInputStream;`
- Line 31: `import java.io.PipedOutputStream;`
- Line 32: `import java.io.PrintStream;`
- Line 33: `import java.io.UncheckedIOException;`
- Line 34: `import java.nio.charset.StandardCharsets;`
- Line 35: `import java.nio.file.Files;`
- Line 36: `import java.nio.file.Path;`
- Line 37: `import java.nio.file.Paths;`
- Line 38: `import java.util.HashMap;`
- Line 39: `import java.util.List;`
- Line 40: `import java.util.Map;`
- Line 41: `import java.util.concurrent.CancellationException;`
- Line 42: `import java.util.concurrent.CompletableFuture;`
- Line 43: `import java.util.concurrent.CountDownLatch;`
- Line 44: `import java.util.concurrent.ExecutionException;`
- Line 45: `import java.util.concurrent.ExecutorService;`
- Line 46: `import java.util.concurrent.Executors;`
- Line 47: `import java.util.concurrent.Future;`
- Line 48: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 49: `import java.util.concurrent.atomic.AtomicReference;`
- Line 51: `import static org.elasticsearch.bootstrap.BootstrapInfo.SERVER_READY_MARKER;`
- Line 52: `import static org.elasticsearch.server.cli.ProcessUtil.nonInterruptibleVoid;`
- Line 53: `import static org.hamcrest.Matchers.containsString;`
- Line 54: `import static org.hamcrest.Matchers.equalTo;`
- Line 55: `import static org.hamcrest.Matchers.hasEntry;`
- Line 56: `import static org.hamcrest.Matchers.hasItems;`
- Line 57: `import static org.hamcrest.Matchers.hasKey;`
- Line 58: `import static org.hamcrest.Matchers.is;`
- Line 59: `import static org.hamcrest.Matchers.not;`
- Line 60: `import static org.hamcrest.Matchers.nullValue;`

## ../distribution/tools/server-cli/src/test/java/org/elasticsearch/server/cli/ServerProcessUtilsTests.java

### Unused Code (13)
- Line 12: `import org.elasticsearch.cli.ExitCodes;`
- Line 13: `import org.elasticsearch.cli.ProcessInfo;`
- Line 14: `import org.elasticsearch.cli.UserException;`
- Line 15: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import org.junit.Before;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.Map;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`
- Line 24: `import static org.hamcrest.Matchers.equalTo;`
- Line 25: `import static org.hamcrest.Matchers.is;`
- Line 26: `import static org.hamcrest.Matchers.startsWith;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/ProcrunCommand.java

### Concurrency Issue (1)
- Line 37: `private static final Logger logger = LogManager.getLogger(ProcrunCommand.class);`

### Exception Handling (2)
- Line 65: `throw new IllegalStateException("Missing procrun exe: " + procrun);`
- Line 99: `throw new UserException(ExitCodes.USAGE, "too many arguments, expected one service id");`

### Unused Code (16)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.apache.logging.log4j.LogManager;`
- Line 15: `import org.apache.logging.log4j.Logger;`
- Line 16: `import org.apache.logging.log4j.util.Supplier;`
- Line 17: `import org.elasticsearch.cli.Command;`
- Line 18: `import org.elasticsearch.cli.ExitCodes;`
- Line 19: `import org.elasticsearch.cli.ProcessInfo;`
- Line 20: `import org.elasticsearch.cli.Terminal;`
- Line 21: `import org.elasticsearch.cli.UserException;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Locale;`
- Line 29: `import java.util.Map;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/WindowsServiceCli.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.cli.MultiCommand;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/WindowsServiceCliProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/WindowsServiceDaemon.java

### Unused Code (14)
- Line 12: `import joptsimple.OptionSet;`
- Line 14: `import org.elasticsearch.bootstrap.ServerArgs;`
- Line 15: `import org.elasticsearch.cli.ProcessInfo;`
- Line 16: `import org.elasticsearch.cli.Terminal;`
- Line 17: `import org.elasticsearch.common.cli.EnvironmentAwareCommand;`
- Line 18: `import org.elasticsearch.common.settings.KeyStoreWrapper;`
- Line 19: `import org.elasticsearch.common.settings.SecureString;`
- Line 20: `import org.elasticsearch.env.Environment;`
- Line 21: `import org.elasticsearch.server.cli.JvmOptionsParser;`
- Line 22: `import org.elasticsearch.server.cli.MachineDependentHeap;`
- Line 23: `import org.elasticsearch.server.cli.ServerProcess;`
- Line 24: `import org.elasticsearch.server.cli.ServerProcessBuilder;`
- Line 25: `import org.elasticsearch.server.cli.ServerProcessUtils;`
- Line 27: `import java.io.IOException;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/WindowsServiceDaemonProvider.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.CliToolProvider;`
- Line 13: `import org.elasticsearch.cli.Command;`

## ../distribution/tools/windows-service-cli/src/main/java/org/elasticsearch/windows/service/WindowsServiceInstallCommand.java

### Unused Code (12)
- Line 12: `import org.elasticsearch.Build;`
- Line 13: `import org.elasticsearch.cli.ExitCodes;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.cli.Terminal;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.elasticsearch.core.SuppressForbidden;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.nio.file.Path;`
- Line 21: `import java.nio.file.Paths;`
- Line 22: `import java.util.ArrayList;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/ProcrunCommandTests.java

### Unused Code (14)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 13: `import org.elasticsearch.cli.ExitCodes;`
- Line 14: `import org.elasticsearch.cli.ProcessInfo;`
- Line 15: `import org.elasticsearch.cli.Terminal;`
- Line 16: `import org.elasticsearch.cli.UserException;`
- Line 17: `import org.junit.Before;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.util.Map;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`
- Line 24: `import static org.hamcrest.Matchers.emptyString;`
- Line 25: `import static org.hamcrest.Matchers.equalTo;`
- Line 26: `import static org.hamcrest.Matchers.is;`
- Line 27: `import static org.hamcrest.Matchers.startsWith;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceCliTestCase.java

### Null Pointer (1)
- Line 51: `ProcessValidator mockProcessValidator = null;`

### Concurrency Issue (1)
- Line 118: `private static final Pattern commandPattern = Pattern.compile("//([A-Z]{2})/([\\w-]+)");`

### Unused Code (28)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 14: `import org.elasticsearch.cli.CommandTestCase;`
- Line 15: `import org.junit.Before;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.io.InputStream;`
- Line 19: `import java.io.OutputStream;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.ArrayList;`
- Line 23: `import java.util.HashMap;`
- Line 24: `import java.util.List;`
- Line 25: `import java.util.Map;`
- Line 26: `import java.util.regex.Matcher;`
- Line 27: `import java.util.regex.Pattern;`
- Line 29: `import static java.lang.ProcessBuilder.Redirect.INHERIT;`
- Line 30: `import static org.hamcrest.Matchers.anyOf;`
- Line 31: `import static org.hamcrest.Matchers.containsString;`
- Line 32: `import static org.hamcrest.Matchers.emptyString;`
- Line 33: `import static org.hamcrest.Matchers.equalTo;`
- Line 34: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`
- Line 35: `import static org.hamcrest.Matchers.hasKey;`
- Line 36: `import static org.hamcrest.Matchers.hasSize;`
- Line 37: `import static org.hamcrest.Matchers.is;`
- Line 38: `import static org.hamcrest.Matchers.lessThan;`
- Line 39: `import static org.hamcrest.Matchers.not;`
- Line 40: `import static org.hamcrest.Matchers.notNullValue;`
- Line 41: `import static org.hamcrest.Matchers.nullValue;`
- Line 42: `import static org.hamcrest.Matchers.startsWith;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceInstallCommandTests.java

### Unused Code (17)
- Line 12: `import org.elasticsearch.Build;`
- Line 13: `import org.elasticsearch.cli.Command;`
- Line 14: `import org.elasticsearch.cli.ExitCodes;`
- Line 15: `import org.elasticsearch.core.Strings;`
- Line 16: `import org.junit.Before;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.nio.file.Files;`
- Line 20: `import java.nio.file.Path;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`
- Line 24: `import static java.util.Map.entry;`
- Line 25: `import static org.hamcrest.Matchers.allOf;`
- Line 26: `import static org.hamcrest.Matchers.any;`
- Line 27: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 28: `import static org.hamcrest.Matchers.containsString;`
- Line 29: `import static org.hamcrest.Matchers.emptyString;`
- Line 30: `import static org.hamcrest.Matchers.equalTo;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceManagerCommandTests.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 14: `import java.io.IOException;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceRemoveCommandTests.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 14: `import java.io.IOException;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceStartCommandTests.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 14: `import java.io.IOException;`

## ../distribution/tools/windows-service-cli/src/test/java/org/elasticsearch/windows/service/WindowsServiceStopCommandTests.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.cli.Command;`
- Line 14: `import java.io.IOException;`

## ../docs/src/yamlRestTest/java/org/elasticsearch/smoketest/DocsClientYamlTestSuiteIT.java

### Exception Handling (2)
- Line 157: `throw new IllegalStateException("empty template in templates list:\n" + templates);`
- Line 159: `throw new RuntimeException("Template " + template + " not cleared after test");`

### Unused Code (43)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 14: `import com.carrotsearch.randomizedtesting.annotations.TimeoutSuite;`
- Line 16: `import org.apache.http.HttpHost;`
- Line 17: `import org.apache.http.util.EntityUtils;`
- Line 18: `import org.apache.lucene.tests.util.TimeUnits;`
- Line 19: `import org.apache.lucene.util.BytesRef;`
- Line 20: `import org.elasticsearch.client.Request;`
- Line 21: `import org.elasticsearch.client.RestClient;`
- Line 22: `import org.elasticsearch.common.settings.SecureString;`
- Line 23: `import org.elasticsearch.common.settings.Settings;`
- Line 24: `import org.elasticsearch.common.util.CollectionUtils;`
- Line 25: `import org.elasticsearch.common.util.Maps;`
- Line 26: `import org.elasticsearch.common.util.concurrent.ThreadContext;`
- Line 27: `import org.elasticsearch.core.Strings;`
- Line 28: `import org.elasticsearch.test.rest.ESRestTestCase;`
- Line 29: `import org.elasticsearch.test.rest.yaml.ClientYamlDocsTestClient;`
- Line 30: `import org.elasticsearch.test.rest.yaml.ClientYamlTestCandidate;`
- Line 31: `import org.elasticsearch.test.rest.yaml.ClientYamlTestClient;`
- Line 32: `import org.elasticsearch.test.rest.yaml.ClientYamlTestExecutionContext;`
- Line 33: `import org.elasticsearch.test.rest.yaml.ClientYamlTestResponse;`
- Line 34: `import org.elasticsearch.test.rest.yaml.ESClientYamlSuiteTestCase;`
- Line 35: `import org.elasticsearch.test.rest.yaml.restspec.ClientYamlSuiteRestSpec;`
- Line 36: `import org.elasticsearch.test.rest.yaml.section.ExecutableSection;`
- Line 37: `import org.elasticsearch.xcontent.ConstructingObjectParser;`
- Line 38: `import org.elasticsearch.xcontent.NamedXContentRegistry;`
- Line 39: `import org.elasticsearch.xcontent.ParseField;`
- Line 40: `import org.elasticsearch.xcontent.XContentLocation;`
- Line 41: `import org.elasticsearch.xcontent.XContentParser;`
- Line 42: `import org.elasticsearch.xcontent.XContentParser.Token;`
- Line 43: `import org.junit.After;`
- Line 44: `import org.junit.Before;`
- Line 46: `import java.io.IOException;`
- Line 47: `import java.util.ArrayList;`
- Line 48: `import java.util.Iterator;`
- Line 49: `import java.util.List;`
- Line 50: `import java.util.Map;`
- Line 52: `import static java.util.Collections.emptyList;`
- Line 53: `import static java.util.Collections.emptyMap;`
- Line 54: `import static java.util.Collections.singletonList;`
- Line 55: `import static java.util.Collections.singletonMap;`
- Line 56: `import static org.elasticsearch.xcontent.ConstructingObjectParser.constructorArg;`
- Line 57: `import static org.hamcrest.Matchers.is;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/CliToolProvider.java

### Exception Handling (1)
- Line 87: `throw new UncheckedIOException(e);`

### Unused Code (14)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.io.UncheckedIOException;`
- Line 14: `import java.net.MalformedURLException;`
- Line 15: `import java.net.URL;`
- Line 16: `import java.net.URLClassLoader;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.nio.file.Paths;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.ServiceLoader;`
- Line 23: `import java.util.stream.Collectors;`
- Line 24: `import java.util.stream.Stream;`
- Line 25: `import java.util.stream.StreamSupport;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/Command.java

### Concurrency Issue (1)
- Line 35: `protected final OptionParser parser = new OptionParser();`

### Unused Code (11)
- Line 12: `import joptsimple.OptionException;`
- Line 13: `import joptsimple.OptionParser;`
- Line 14: `import joptsimple.OptionSet;`
- Line 15: `import joptsimple.OptionSpec;`
- Line 17: `import org.elasticsearch.core.SuppressForbidden;`
- Line 18: `import org.elasticsearch.logging.Level;`
- Line 19: `import org.elasticsearch.logging.internal.spi.LoggerFactory;`
- Line 21: `import java.io.Closeable;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.io.StringWriter;`
- Line 24: `import java.util.Arrays;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/ExitCodes.java

### Concurrency Issue (15)
- Line 18: `public static final int OK = 0;`
- Line 19: `public static final int USAGE = 64;          // command line usage error`
- Line 20: `public static final int DATA_ERROR = 65;     // data format error`
- Line 21: `public static final int NO_INPUT = 66;       // cannot open input`
- Line 22: `public static final int NO_USER = 67;        // addressee unknown`
- Line 23: `public static final int NO_HOST = 68;        // host name unknown`
- Line 24: `public static final int UNAVAILABLE = 69;    // service unavailable`
- Line 25: `public static final int CODE_ERROR = 70;     // internal software error`
- Line 26: `public static final int CANT_CREATE = 73;    // can't create (user) output file`
- Line 27: `public static final int IO_ERROR = 74;       // input/output error`
- Line 28: `public static final int TEMP_FAILURE = 75;   // temp failure; user is invited to retry`
- Line 29: `public static final int PROTOCOL = 76;       // remote error in protocol`
- Line 30: `public static final int NOPERM = 77;         // permission denied`
- Line 31: `public static final int CONFIG = 78;         // configuration error`
- Line 32: `public static final int NOOP = 80;           // nothing to do`

## ../libs/cli/src/main/java/org/elasticsearch/cli/MultiCommand.java

### Exception Handling (4)
- Line 63: `throw new IllegalStateException("No subcommands configured");`
- Line 76: `throw new IllegalStateException("No subcommands configured");`
- Line 82: `throw new MissingCommandException();`
- Line 88: `throw new UserException(ExitCodes.USAGE, "Unknown command [" + subcommandName + "]");`

### Unused Code (11)
- Line 12: `import joptsimple.NonOptionArgumentSpec;`
- Line 13: `import joptsimple.OptionSet;`
- Line 14: `import joptsimple.OptionSpec;`
- Line 15: `import joptsimple.util.KeyValuePair;`
- Line 17: `import org.elasticsearch.core.IOUtils;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.LinkedHashMap;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.function.Consumer;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/ProcessInfo.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.nio.file.Path;`
- Line 15: `import java.nio.file.Paths;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.Properties;`
- Line 18: `import java.util.stream.Collectors;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/Terminal.java

### Concurrency Issue (3)
- Line 88: `public void setVerbosity(Verbosity verbosity) {`
- Line 304: `private static final int JDK_VERSION_WITH_IS_TERMINAL = 22;`
- Line 371: `static final int MAX_BUFFER_LENGTH = DEFAULT_BUFFER_LENGTH * 8;`

### Exception Handling (2)
- Line 104: `throw new IllegalStateException("unable to read from standard input; is standard input open and a tty attached?");`
- Line 281: `throw new RuntimeException(e);`

### Infinite Loop (1)
- Line 230: `while (true) {`

### Unused Code (16)
- Line 61: `private Verbosity currentVerbosity = Verbosity.NORMAL;`
- Line 375: `private int count = 0;`
- Line 12: `import org.elasticsearch.core.Nullable;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 15: `import java.io.Console;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.io.InputStream;`
- Line 18: `import java.io.InputStreamReader;`
- Line 19: `import java.io.OutputStream;`
- Line 20: `import java.io.PrintWriter;`
- Line 21: `import java.io.Reader;`
- Line 22: `import java.lang.reflect.InvocationTargetException;`
- Line 23: `import java.lang.reflect.Method;`
- Line 24: `import java.nio.charset.Charset;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.Locale;`

## ../libs/cli/src/main/java/org/elasticsearch/cli/UserException.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.core.Nullable;`

## ../libs/cli/src/test/java/org/elasticsearch/cli/TerminalTests.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.elasticsearch.test.ESTestCase.WithoutSecurityManager;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.io.OutputStream;`
- Line 17: `import java.io.PrintWriter;`
- Line 18: `import java.nio.charset.StandardCharsets;`
- Line 20: `import static org.mockito.ArgumentMatchers.eq;`
- Line 21: `import static org.mockito.Mockito.mock;`
- Line 22: `import static org.mockito.Mockito.times;`
- Line 23: `import static org.mockito.Mockito.verify;`
- Line 24: `import static org.mockito.Mockito.verifyNoMoreInteractions;`

## ../libs/core/src/main/java/module-info.java

### Unused Code (1)
- Line 10: `import org.elasticsearch.jdk.ModuleQualifiedExportsService;`

## ../libs/core/src/main/java/org/elasticsearch/core/AbstractRefCounted.java

### Concurrency Issue (2)
- Line 22: `public static final String ALREADY_CLOSED_MESSAGE = "already closed, can't increment ref count";`
- Line 23: `public static final String INVALID_DECREF_MESSAGE = "invalid decRef call: already closed";`

### Exception Handling (2)
- Line 33: `throw new RuntimeException(e);`
- Line 101: `throw new IllegalStateException(ALREADY_CLOSED_MESSAGE);`

### Unused Code (3)
- Line 12: `import java.lang.invoke.MethodHandles;`
- Line 13: `import java.lang.invoke.VarHandle;`
- Line 14: `import java.util.Objects;`

## ../libs/core/src/main/java/org/elasticsearch/core/Booleans.java

### Exception Handling (1)
- Line 63: `throw new IllegalArgumentException("Failed to parse value [" + value + "] as only [true] or [false] are allowed.");`

## ../libs/core/src/main/java/org/elasticsearch/core/CharArrays.java

### Unused Code (5)
- Line 12: `import java.nio.ByteBuffer;`
- Line 13: `import java.nio.CharBuffer;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.util.Arrays;`
- Line 16: `import java.util.Objects;`

## ../libs/core/src/main/java/org/elasticsearch/core/CheckedConsumer.java

### Unused Code (1)
- Line 12: `import java.util.Objects;`

## ../libs/core/src/main/java/org/elasticsearch/core/CheckedFunction.java

### Unused Code (1)
- Line 12: `import java.util.function.Function;`

## ../libs/core/src/main/java/org/elasticsearch/core/FastMath.java

### Concurrency Issue (29)
- Line 45: `private static final double ONE_DIV_F2 = 1 / 2.0;`
- Line 46: `private static final double ONE_DIV_F3 = 1 / 6.0;`
- Line 47: `private static final double ONE_DIV_F4 = 1 / 24.0;`
- Line 48: `private static final double TWO_POW_N28 = Double.longBitsToDouble(0x3E30000000000000L);`
- Line 49: `private static final double TWO_POW_66 = Double.longBitsToDouble(0x4410000000000000L);`
- Line 50: `private static final double LOG_DOUBLE_MAX_VALUE = StrictMath.log(Double.MAX_VALUE);`
- Line 52: `private static final double TWO_POW_27 = Double.longBitsToDouble(0x41A0000000000000L);`
- Line 53: `private static final double TWO_POW_52 = Double.longBitsToDouble(0x4330000000000000L);`
- Line 55: `private static final double MIN_DOUBLE_NORMAL = Double.longBitsToDouble(0x0010000000000000L); // 2.2250738585072014E-308`
- Line 56: `private static final int MIN_DOUBLE_EXPONENT = -1074;`
- Line 57: `private static final int MAX_DOUBLE_EXPONENT = 1023;`
- Line 70: `private static final double ATAN_MAX_VALUE_FOR_TABS = StrictMath.tan(Math.toRadians(74.0));`
- Line 72: `private static final int ATAN_TABS_SIZE = 1 << 12 + 1;`
- Line 73: `private static final double ATAN_DELTA = ATAN_MAX_VALUE_FOR_TABS / (ATAN_TABS_SIZE - 1);`
- Line 74: `private static final double ATAN_INDEXER = 1 / ATAN_DELTA;`
- Line 81: `private static final double ATAN_HI3 = Double.longBitsToDouble(0x3ff921fb54442d18L); // 1.57079632679489655800e+00 atan(inf)hi`
- Line 82: `private static final double ATAN_LO3 = Double.longBitsToDouble(0x3c91a62633145c07L); // 6.12323399573676603587e-17 atan(inf)lo`
- Line 83: `private static final double ATAN_AT0 = Double.longBitsToDouble(0x3fd555555555550dL); // 3.33333333333329318027e-01`
- Line 84: `private static final double ATAN_AT1 = Double.longBitsToDouble(0xbfc999999998ebc4L); // -1.99999999998764832476e-01`
- Line 85: `private static final double ATAN_AT2 = Double.longBitsToDouble(0x3fc24924920083ffL); // 1.42857142725034663711e-01`
- Line 86: `private static final double ATAN_AT3 = Double.longBitsToDouble(0xbfbc71c6fe231671L); // -1.11111104054623557880e-01`
- Line 87: `private static final double ATAN_AT4 = Double.longBitsToDouble(0x3fb745cdc54c206eL); // 9.09088713343650656196e-02`
- Line 88: `private static final double ATAN_AT5 = Double.longBitsToDouble(0xbfb3b0f2af749a6dL); // -7.69187620504482999495e-02`
- Line 89: `private static final double ATAN_AT6 = Double.longBitsToDouble(0x3fb10d66a0d03d51L); // 6.66107313738753120669e-02`
- Line 90: `private static final double ATAN_AT7 = Double.longBitsToDouble(0xbfadde2d52defd9aL); // -5.83357013379057348645e-02`
- Line 91: `private static final double ATAN_AT8 = Double.longBitsToDouble(0x3fa97b4b24760debL); // 4.97687799461593236017e-02`
- Line 92: `private static final double ATAN_AT9 = Double.longBitsToDouble(0xbfa2b4442c6a6c2fL); // -3.65315727442169155270e-02`
- Line 99: `private static final int LOG_BITS = 12;`
- Line 100: `private static final int LOG_TAB_SIZE = (1 << LOG_BITS);`

## ../libs/core/src/main/java/org/elasticsearch/core/FixForMultiProject.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/core/src/main/java/org/elasticsearch/core/IOUtils.java

### Concurrency Issue (3)
- Line 48: `public static final String UTF_8 = StandardCharsets.UTF_8.name();`
- Line 259: `public static final boolean WINDOWS = System.getProperty("os.name").startsWith("Windows");`
- Line 260: `public static final boolean LINUX = System.getProperty("os.name").startsWith("Linux");`

### Exception Handling (2)
- Line 170: `} catch (final IOException | RuntimeException e) {}`
- Line 184: `} catch (final IOException ignored) {`

### Unused Code (13)
- Line 23: `import java.io.Closeable;`
- Line 24: `import java.io.IOException;`
- Line 25: `import java.nio.channels.FileChannel;`
- Line 26: `import java.nio.charset.StandardCharsets;`
- Line 27: `import java.nio.file.FileVisitResult;`
- Line 28: `import java.nio.file.FileVisitor;`
- Line 29: `import java.nio.file.Files;`
- Line 30: `import java.nio.file.NoSuchFileException;`
- Line 31: `import java.nio.file.Path;`
- Line 32: `import java.nio.file.StandardOpenOption;`
- Line 33: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 34: `import java.util.LinkedHashMap;`
- Line 35: `import java.util.Map;`

## ../libs/core/src/main/java/org/elasticsearch/core/Nullable.java

### Unused Code (7)
- Line 12: `import java.lang.annotation.Documented;`
- Line 13: `import java.lang.annotation.ElementType;`
- Line 14: `import java.lang.annotation.Retention;`
- Line 15: `import java.lang.annotation.RetentionPolicy;`
- Line 16: `import java.lang.annotation.Target;`
- Line 18: `import javax.annotation.CheckForNull;`
- Line 19: `import javax.annotation.meta.TypeQualifierNickname;`

## ../libs/core/src/main/java/org/elasticsearch/core/PathUtils.java

### Unused Code (5)
- Line 12: `import java.net.URI;`
- Line 13: `import java.nio.file.FileSystem;`
- Line 14: `import java.nio.file.FileSystems;`
- Line 15: `import java.nio.file.Path;`
- Line 16: `import java.nio.file.Paths;`

## ../libs/core/src/main/java/org/elasticsearch/core/Predicates.java

### Unused Code (1)
- Line 12: `import java.util.function.Predicate;`

## ../libs/core/src/main/java/org/elasticsearch/core/Releasable.java

### Unused Code (1)
- Line 12: `import java.io.Closeable;`

## ../libs/core/src/main/java/org/elasticsearch/core/ReleasableIterator.java

### Unused Code (3)
- Line 24: `private T value = Objects.requireNonNull(element);`
- Line 12: `import java.util.Iterator;`
- Line 13: `import java.util.Objects;`

## ../libs/core/src/main/java/org/elasticsearch/core/Releasables.java

### Unused Code (3)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.Iterator;`
- Line 14: `import java.util.concurrent.atomic.AtomicReference;`

## ../libs/core/src/main/java/org/elasticsearch/core/RestApiVersion.java

### Concurrency Issue (1)
- Line 27: `private static final RestApiVersion CURRENT = V_9;`

### Exception Handling (1)
- Line 72: `default -> throw new IllegalArgumentException("Unknown REST API version " + major);`

### Unused Code (1)
- Line 12: `import java.util.function.Predicate;`

## ../libs/core/src/main/java/org/elasticsearch/core/Streams.java

### Unused Code (5)
- Line 12: `import java.io.FilterOutputStream;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.InputStream;`
- Line 15: `import java.io.OutputStream;`
- Line 16: `import java.nio.ByteBuffer;`

## ../libs/core/src/main/java/org/elasticsearch/core/Strings.java

### Unused Code (1)
- Line 12: `import java.util.Locale;`

## ../libs/core/src/main/java/org/elasticsearch/core/SuppressForbidden.java

### Unused Code (4)
- Line 11: `import java.lang.annotation.ElementType;`
- Line 12: `import java.lang.annotation.Retention;`
- Line 13: `import java.lang.annotation.RetentionPolicy;`
- Line 14: `import java.lang.annotation.Target;`

## ../libs/core/src/main/java/org/elasticsearch/core/TimeValue.java

### Concurrency Issue (14)
- Line 19: `public static final long NSEC_PER_MSEC = TimeUnit.NANOSECONDS.convert(1, TimeUnit.MILLISECONDS);`
- Line 21: `public static final TimeValue MINUS_ONE = new TimeValue(-1, TimeUnit.MILLISECONDS);`
- Line 22: `public static final TimeValue ZERO = new TimeValue(0, TimeUnit.MILLISECONDS);`
- Line 23: `public static final TimeValue MAX_VALUE = new TimeValue(Long.MAX_VALUE, TimeUnit.NANOSECONDS);`
- Line 24: `public static final TimeValue THIRTY_SECONDS = new TimeValue(30, TimeUnit.SECONDS);`
- Line 25: `public static final TimeValue ONE_MINUTE = new TimeValue(1, TimeUnit.MINUTES);`
- Line 26: `public static final TimeValue ONE_HOUR = new TimeValue(1, TimeUnit.HOURS);`
- Line 28: `private static final long C0 = 1L;`
- Line 29: `private static final long C1 = C0 * 1000L;`
- Line 30: `private static final long C2 = C1 * 1000L;`
- Line 31: `private static final long C3 = C2 * 1000L;`
- Line 32: `private static final long C4 = C3 * 60L;`
- Line 33: `private static final long C5 = C4 * 60L;`
- Line 34: `private static final long C6 = C5 * 24L;`

### Exception Handling (6)
- Line 45: `throw new IllegalArgumentException("duration cannot be negative, was given [" + duration + "]");`
- Line 88: `throw new IllegalArgumentException("time value cannot store values greater than 106751 days");`
- Line 403: `throw new IllegalArgumentException(`
- Line 415: `throw new IllegalArgumentException(`
- Line 428: `throw new IllegalArgumentException("failed to parse [" + initialInput + "], fractional time values are not supported", e);`
- Line 430: `throw new IllegalArgumentException("failed to parse [" + initialInput + "]", e);`

### Unused Code (3)
- Line 12: `import java.util.Locale;`
- Line 13: `import java.util.Objects;`
- Line 14: `import java.util.concurrent.TimeUnit;`

## ../libs/core/src/main/java/org/elasticsearch/core/UpdateForV10.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/core/src/main/java/org/elasticsearch/core/internal/provider/EmbeddedImplClassLoader.java

### Resource Leak (1)
- Line 443: `BufferedReader reader = new BufferedReader(isr)`

### Concurrency Issue (5)
- Line 81: `private static final String IMPL_PREFIX = "IMPL-JARS/";`
- Line 243: `private int jarMetaIndex = 0;`
- Line 245: `private URL url = null;`
- Line 483: `private static final int BASE_VERSION_FEATURE = 8; // lowest supported release version`
- Line 490: `private static final String MRJAR_VERSION_PREFIX = "META-INF/versions/";`

### Exception Handling (7)
- Line 141: `} catch (ClassNotFoundException ignore) {}`
- Line 157: `throw new UncheckedIOException(e);`
- Line 160: `throw new ClassNotFoundException(name);`
- Line 271: `throw new NoSuchElementException();`
- Line 423: `throw new UncheckedIOException(x);`
- Line 465: `throw new UncheckedIOException(e);`
- Line 524: `throw new NoSuchElementException();`

### Unused Code (39)
- Line 243: `private int jarMetaIndex = 0;`
- Line 245: `private URL url = null;`
- Line 502: `private int index;`
- Line 12: `import java.io.BufferedReader;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.InputStream;`
- Line 15: `import java.io.InputStreamReader;`
- Line 16: `import java.io.UncheckedIOException;`
- Line 17: `import java.net.MalformedURLException;`
- Line 18: `import java.net.URI;`
- Line 19: `import java.net.URISyntaxException;`
- Line 20: `import java.net.URL;`
- Line 21: `import java.nio.charset.StandardCharsets;`
- Line 22: `import java.nio.file.FileSystem;`
- Line 23: `import java.nio.file.FileSystems;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.security.AccessController;`
- Line 27: `import java.security.CodeSigner;`
- Line 28: `import java.security.CodeSource;`
- Line 29: `import java.security.PrivilegedAction;`
- Line 30: `import java.security.SecureClassLoader;`
- Line 31: `import java.util.ArrayList;`
- Line 32: `import java.util.Collections;`
- Line 33: `import java.util.Comparator;`
- Line 34: `import java.util.Enumeration;`
- Line 35: `import java.util.HashMap;`
- Line 36: `import java.util.HashSet;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Locale;`
- Line 39: `import java.util.Map;`
- Line 40: `import java.util.NoSuchElementException;`
- Line 41: `import java.util.Objects;`
- Line 42: `import java.util.Set;`
- Line 43: `import java.util.function.Function;`
- Line 44: `import java.util.jar.Manifest;`
- Line 46: `import static java.util.jar.Attributes.Name.MULTI_RELEASE;`
- Line 47: `import static java.util.stream.Collectors.toUnmodifiableMap;`
- Line 48: `import static org.elasticsearch.core.internal.provider.EmbeddedModulePath.isPackageName;`

## ../libs/core/src/main/java/org/elasticsearch/core/internal/provider/EmbeddedModulePath.java

### Concurrency Issue (3)
- Line 88: `private static final String MODULE_INFO = "module-info.class";`
- Line 90: `private static final String SERVICES_PREFIX = "META-INF/services/";`
- Line 94: `private static final int BASE_VERSION_FEATURE = 8; // lowest supported release version`

### Exception Handling (8)
- Line 171: `} catch (IllegalArgumentException ignore) {}`
- Line 53: `throw new UncheckedIOException(e);`
- Line 62: `throw new FindException("automatic module without a manifest name is not supported, for: " + path);`
- Line 120: `throw new UncheckedIOException(x);`
- Line 160: `throw new IllegalArgumentException("unexpected jar name: " + jarName);`
- Line 218: `throw new InvalidModuleDescriptorException(msg);`
- Line 240: `throw new InvalidModuleDescriptorException(msg);`
- Line 258: `throw new IllegalArgumentException("unexpected service " + cf);`

### Unused Code (19)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.io.InputStream;`
- Line 14: `import java.io.UncheckedIOException;`
- Line 15: `import java.lang.module.FindException;`
- Line 16: `import java.lang.module.InvalidModuleDescriptorException;`
- Line 17: `import java.lang.module.ModuleDescriptor;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Map;`
- Line 23: `import java.util.Optional;`
- Line 24: `import java.util.Set;`
- Line 25: `import java.util.function.Predicate;`
- Line 26: `import java.util.jar.Attributes;`
- Line 27: `import java.util.jar.Manifest;`
- Line 28: `import java.util.regex.Matcher;`
- Line 29: `import java.util.regex.Pattern;`
- Line 30: `import java.util.stream.Collectors;`

## ../libs/core/src/main/java/org/elasticsearch/core/internal/provider/InMemoryModuleFinder.java

### Exception Handling (1)
- Line 119: `throw new UnsupportedOperationException();`

### Unused Code (12)
- Line 12: `import java.lang.module.ModuleDescriptor;`
- Line 13: `import java.lang.module.ModuleFinder;`
- Line 14: `import java.lang.module.ModuleReader;`
- Line 15: `import java.lang.module.ModuleReference;`
- Line 16: `import java.net.URI;`
- Line 17: `import java.nio.file.Path;`
- Line 18: `import java.util.Arrays;`
- Line 19: `import java.util.Map;`
- Line 20: `import java.util.Objects;`
- Line 21: `import java.util.Optional;`
- Line 22: `import java.util.Set;`
- Line 23: `import java.util.stream.Collectors;`

## ../libs/core/src/main/java/org/elasticsearch/core/internal/provider/ProviderLocator.java

### Unused Code (15)
- Line 12: `import org.elasticsearch.jdk.ModuleQualifiedExportsService;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.io.UncheckedIOException;`
- Line 16: `import java.lang.module.Configuration;`
- Line 17: `import java.lang.module.ModuleFinder;`
- Line 18: `import java.security.AccessController;`
- Line 19: `import java.security.PrivilegedActionException;`
- Line 20: `import java.security.PrivilegedExceptionAction;`
- Line 21: `import java.util.Locale;`
- Line 22: `import java.util.Objects;`
- Line 23: `import java.util.ServiceConfigurationError;`
- Line 24: `import java.util.ServiceLoader;`
- Line 25: `import java.util.Set;`
- Line 26: `import java.util.function.Supplier;`
- Line 28: `import static org.elasticsearch.jdk.ModuleQualifiedExportsService.exposeQualifiedExportsAndOpens;`

## ../libs/core/src/main/java/org/elasticsearch/jdk/JarHell.java

### Exception Handling (1)
- Line 160: `throw new RuntimeException(e);`

### Unused Code (33)
- Line 12: `import org.elasticsearch.core.PathUtils;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.lang.Runtime.Version;`
- Line 17: `import java.lang.module.Configuration;`
- Line 18: `import java.lang.module.ModuleReference;`
- Line 19: `import java.lang.module.ResolvedModule;`
- Line 20: `import java.net.MalformedURLException;`
- Line 21: `import java.net.URI;`
- Line 22: `import java.net.URISyntaxException;`
- Line 23: `import java.net.URL;`
- Line 24: `import java.net.URLClassLoader;`
- Line 25: `import java.nio.file.FileVisitResult;`
- Line 26: `import java.nio.file.Files;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.nio.file.SimpleFileVisitor;`
- Line 29: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 30: `import java.util.Arrays;`
- Line 31: `import java.util.Collections;`
- Line 32: `import java.util.Enumeration;`
- Line 33: `import java.util.HashMap;`
- Line 34: `import java.util.HashSet;`
- Line 35: `import java.util.LinkedHashSet;`
- Line 36: `import java.util.Locale;`
- Line 37: `import java.util.Map;`
- Line 38: `import java.util.Optional;`
- Line 39: `import java.util.Set;`
- Line 40: `import java.util.function.Consumer;`
- Line 41: `import java.util.jar.JarEntry;`
- Line 42: `import java.util.jar.JarFile;`
- Line 43: `import java.util.jar.Manifest;`
- Line 44: `import java.util.stream.Stream;`
- Line 46: `import static java.util.stream.Collectors.toUnmodifiableSet;`

## ../libs/core/src/main/java/org/elasticsearch/jdk/JdkJarHellCheck.java

### Exception Handling (1)
- Line 60: `throw new IllegalArgumentException("Path does not exist: " + path);`

### Unused Code (11)
- Line 11: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.nio.file.FileVisitResult;`
- Line 15: `import java.nio.file.Files;`
- Line 16: `import java.nio.file.Path;`
- Line 17: `import java.nio.file.Paths;`
- Line 18: `import java.nio.file.SimpleFileVisitor;`
- Line 19: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 20: `import java.util.Collections;`
- Line 21: `import java.util.HashSet;`
- Line 22: `import java.util.Set;`

## ../libs/core/src/main/java/org/elasticsearch/jdk/ModuleQualifiedExportsService.java

### Concurrency Issue (1)
- Line 42: `private static final Logger logger = LogManager.getLogger(ModuleQualifiedExportsService.class);`

### Unused Code (15)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 15: `import java.lang.module.ModuleDescriptor.Exports;`
- Line 16: `import java.lang.module.ModuleDescriptor.Opens;`
- Line 17: `import java.util.ArrayList;`
- Line 18: `import java.util.Collection;`
- Line 19: `import java.util.HashMap;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.ServiceLoader;`
- Line 23: `import java.util.Set;`
- Line 24: `import java.util.function.Function;`
- Line 25: `import java.util.function.Predicate;`
- Line 26: `import java.util.stream.Collectors;`
- Line 27: `import java.util.stream.Stream;`

## ../libs/core/src/test/java/org/elasticsearch/common/CharArraysTests.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.core.CharArrays;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.nio.charset.StandardCharsets;`
- Line 17: `import static org.hamcrest.Matchers.is;`

## ../libs/core/src/test/java/org/elasticsearch/common/collect/TupleTests.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.core.Tuple;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/core/src/test/java/org/elasticsearch/common/unit/TimeValueTests.java

### Concurrency Issue (1)
- Line 114: `private static final String FRACTIONAL_TIME_VALUES_ARE_NOT_SUPPORTED = "fractional time values are not supported";`

### Unused Code (10)
- Line 12: `import org.elasticsearch.core.TimeValue;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.util.concurrent.TimeUnit;`
- Line 17: `import static org.hamcrest.CoreMatchers.instanceOf;`
- Line 18: `import static org.hamcrest.CoreMatchers.not;`
- Line 19: `import static org.hamcrest.Matchers.containsString;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`
- Line 21: `import static org.hamcrest.Matchers.is;`
- Line 22: `import static org.hamcrest.Matchers.lessThan;`
- Line 23: `import static org.hamcrest.object.HasToString.hasToString;`

## ../libs/core/src/test/java/org/elasticsearch/common/util/ESSloppyMathTests.java

### Concurrency Issue (1)
- Line 26: `static double LOG_DELTA_1 = 1E-14; // near 1.0 we can be more accurate`

### Unused Code (4)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import static org.elasticsearch.core.ESSloppyMath.atan;`
- Line 15: `import static org.elasticsearch.core.ESSloppyMath.log;`
- Line 16: `import static org.elasticsearch.core.ESSloppyMath.sinh;`

## ../libs/core/src/test/java/org/elasticsearch/core/AbstractRefCountedTests.java

### Unused Code (4)
- Line 11: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 15: `import static org.hamcrest.Matchers.equalTo;`
- Line 16: `import static org.hamcrest.Matchers.is;`

## ../libs/core/src/test/java/org/elasticsearch/core/IOUtilsTests.java

### Exception Handling (1)
- Line 204: `throw new AccessDeniedException("access denied while trying to delete file [" + path + "]");`

### Unused Code (30)
- Line 21: `import org.apache.lucene.tests.mockfile.FilterFileSystemProvider;`
- Line 22: `import org.apache.lucene.tests.mockfile.FilterPath;`
- Line 23: `import org.apache.lucene.util.Constants;`
- Line 24: `import org.elasticsearch.test.ESTestCase;`
- Line 26: `import java.io.Closeable;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.OutputStream;`
- Line 29: `import java.nio.channels.FileChannel;`
- Line 30: `import java.nio.charset.StandardCharsets;`
- Line 31: `import java.nio.file.AccessDeniedException;`
- Line 32: `import java.nio.file.FileSystem;`
- Line 33: `import java.nio.file.Files;`
- Line 34: `import java.nio.file.NoSuchFileException;`
- Line 35: `import java.nio.file.OpenOption;`
- Line 36: `import java.nio.file.Path;`
- Line 37: `import java.nio.file.attribute.FileAttribute;`
- Line 38: `import java.util.ArrayList;`
- Line 39: `import java.util.Arrays;`
- Line 40: `import java.util.List;`
- Line 41: `import java.util.Objects;`
- Line 42: `import java.util.Set;`
- Line 43: `import java.util.function.Function;`
- Line 45: `import static org.hamcrest.Matchers.arrayWithSize;`
- Line 46: `import static org.hamcrest.Matchers.containsString;`
- Line 47: `import static org.hamcrest.Matchers.equalTo;`
- Line 48: `import static org.hamcrest.Matchers.hasToString;`
- Line 49: `import static org.mockito.Mockito.doThrow;`
- Line 50: `import static org.mockito.Mockito.mock;`
- Line 51: `import static org.mockito.Mockito.verify;`
- Line 52: `import static org.mockito.Mockito.verifyNoMoreInteractions;`

## ../libs/core/src/test/java/org/elasticsearch/core/ReleasablesTests.java

### Unused Code (6)
- Line 11: `import org.elasticsearch.test.ESTestCase;`
- Line 12: `import org.elasticsearch.test.ReachabilityChecker;`
- Line 14: `import java.util.Arrays;`
- Line 15: `import java.util.Iterator;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.concurrent.atomic.AtomicInteger;`

## ../libs/core/src/test/java/org/elasticsearch/core/StreamsTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.io.ByteArrayInputStream;`
- Line 15: `import java.io.ByteArrayOutputStream;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.charset.StandardCharsets;`
- Line 18: `import java.util.Arrays;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/core/src/test/java/org/elasticsearch/core/StringsTests.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/core/src/test/java/org/elasticsearch/core/internal/provider/EmbeddedImplClassLoaderTests.java

### Exception Handling (1)
- Line 601: `throw new UncheckedIOException(e);`

### Unused Code (38)
- Line 12: `import org.elasticsearch.core.Strings;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.core.internal.provider.EmbeddedImplClassLoader.CompoundEnumeration;`
- Line 15: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import org.elasticsearch.test.PrivilegedOperations;`
- Line 17: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 18: `import org.elasticsearch.test.jar.JarUtils;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.io.UncheckedIOException;`
- Line 22: `import java.net.URI;`
- Line 23: `import java.net.URL;`
- Line 24: `import java.net.URLClassLoader;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Collections;`
- Line 28: `import java.util.Enumeration;`
- Line 29: `import java.util.HashMap;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Locale;`
- Line 32: `import java.util.Map;`
- Line 33: `import java.util.NoSuchElementException;`
- Line 35: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 36: `import static java.util.Arrays.stream;`
- Line 37: `import static org.elasticsearch.core.internal.provider.EmbeddedImplClassLoader.basePrefix;`
- Line 38: `import static org.elasticsearch.core.internal.provider.EmbeddedImplClassLoader.rootURI;`
- Line 39: `import static org.hamcrest.Matchers.anyOf;`
- Line 40: `import static org.hamcrest.Matchers.contains;`
- Line 41: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 42: `import static org.hamcrest.Matchers.emptyCollectionOf;`
- Line 43: `import static org.hamcrest.Matchers.endsWith;`
- Line 44: `import static org.hamcrest.Matchers.equalTo;`
- Line 45: `import static org.hamcrest.Matchers.hasSize;`
- Line 46: `import static org.hamcrest.Matchers.hasToString;`
- Line 47: `import static org.hamcrest.Matchers.is;`
- Line 48: `import static org.hamcrest.Matchers.not;`
- Line 49: `import static org.hamcrest.Matchers.nullValue;`
- Line 50: `import static org.hamcrest.Matchers.oneOf;`
- Line 51: `import static org.hamcrest.Matchers.startsWith;`

## ../libs/core/src/test/java/org/elasticsearch/core/internal/provider/EmbeddedModulePathTests.java

### Unused Code (30)
- Line 12: `import org.elasticsearch.core.PathUtils;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 15: `import org.elasticsearch.test.jar.JarUtils;`
- Line 17: `import java.io.ByteArrayInputStream;`
- Line 18: `import java.lang.module.InvalidModuleDescriptorException;`
- Line 19: `import java.lang.module.ModuleDescriptor.Version;`
- Line 20: `import java.nio.file.FileSystem;`
- Line 21: `import java.nio.file.FileSystems;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.Path;`
- Line 24: `import java.util.HashMap;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Map;`
- Line 27: `import java.util.Optional;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.jar.Manifest;`
- Line 31: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 32: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.exportsOf;`
- Line 33: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.opensOf;`
- Line 34: `import static org.elasticsearch.test.hamcrest.OptionalMatchers.isEmpty;`
- Line 35: `import static org.elasticsearch.test.hamcrest.OptionalMatchers.isPresentWith;`
- Line 36: `import static org.hamcrest.Matchers.aMapWithSize;`
- Line 37: `import static org.hamcrest.Matchers.contains;`
- Line 38: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 39: `import static org.hamcrest.Matchers.equalTo;`
- Line 40: `import static org.hamcrest.Matchers.hasEntry;`
- Line 41: `import static org.hamcrest.Matchers.hasItem;`
- Line 42: `import static org.hamcrest.Matchers.is;`
- Line 43: `import static org.hamcrest.Matchers.nullValue;`

## ../libs/core/src/test/java/org/elasticsearch/core/internal/provider/InMemoryModuleFinderTests.java

### Unused Code (28)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 14: `import org.elasticsearch.test.jar.JarUtils;`
- Line 16: `import java.lang.module.ModuleDescriptor;`
- Line 17: `import java.lang.module.ModuleDescriptor.Version;`
- Line 18: `import java.nio.file.FileSystem;`
- Line 19: `import java.nio.file.FileSystems;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.HashMap;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Map;`
- Line 25: `import java.util.Set;`
- Line 27: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 28: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.exportsOf;`
- Line 29: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.opensOf;`
- Line 30: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.providesOf;`
- Line 31: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.requiresOf;`
- Line 32: `import static org.elasticsearch.test.hamcrest.OptionalMatchers.isPresent;`
- Line 33: `import static org.elasticsearch.test.hamcrest.OptionalMatchers.isPresentWith;`
- Line 34: `import static org.hamcrest.Matchers.contains;`
- Line 35: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 36: `import static org.hamcrest.Matchers.empty;`
- Line 37: `import static org.hamcrest.Matchers.equalTo;`
- Line 38: `import static org.hamcrest.Matchers.hasItem;`
- Line 39: `import static org.hamcrest.Matchers.hasSize;`
- Line 40: `import static org.hamcrest.Matchers.is;`
- Line 41: `import static org.hamcrest.Matchers.not;`

## ../libs/core/src/test/java/org/elasticsearch/core/internal/provider/ProviderLocatorTests.java

### Unused Code (20)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.elasticsearch.test.PrivilegedOperations;`
- Line 14: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 15: `import org.elasticsearch.test.jar.JarUtils;`
- Line 17: `import java.lang.module.ModuleDescriptor;`
- Line 18: `import java.net.URL;`
- Line 19: `import java.net.URLClassLoader;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.HashMap;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.Set;`
- Line 25: `import java.util.function.IntSupplier;`
- Line 26: `import java.util.function.LongSupplier;`
- Line 28: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 29: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.exportsOf;`
- Line 30: `import static org.elasticsearch.test.hamcrest.ModuleDescriptorMatchers.opensOf;`
- Line 31: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 32: `import static org.hamcrest.Matchers.equalTo;`
- Line 33: `import static org.hamcrest.Matchers.is;`

## ../libs/core/src/test/java/org/elasticsearch/jdk/JarHellTests.java

### Unused Code (24)
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.core.PathUtils;`
- Line 14: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.lang.Runtime.Version;`
- Line 18: `import java.lang.module.ModuleFinder;`
- Line 19: `import java.net.URL;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.nio.file.StandardOpenOption;`
- Line 23: `import java.util.ArrayList;`
- Line 24: `import java.util.Collections;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Set;`
- Line 27: `import java.util.jar.Attributes;`
- Line 28: `import java.util.jar.JarOutputStream;`
- Line 29: `import java.util.jar.Manifest;`
- Line 30: `import java.util.stream.Collectors;`
- Line 31: `import java.util.zip.ZipEntry;`
- Line 32: `import java.util.zip.ZipOutputStream;`
- Line 34: `import static org.hamcrest.Matchers.containsString;`
- Line 35: `import static org.hamcrest.Matchers.endsWith;`
- Line 36: `import static org.hamcrest.Matchers.equalTo;`
- Line 37: `import static org.hamcrest.Matchers.hasItems;`

## ../libs/dissect/src/main/java/org/elasticsearch/dissect/DissectKey.java

### Concurrency Issue (4)
- Line 29: `private static final Pattern LEFT_MODIFIER_PATTERN = Pattern.compile("([+*&?])(.*?)(->)?$", Pattern.DOTALL);`
- Line 30: `private static final Pattern RIGHT_PADDING_PATTERN = Pattern.compile("^(.*?)(->)?$", Pattern.DOTALL);`
- Line 31: `private static final Pattern APPEND_WITH_ORDER_PATTERN = Pattern.compile("[+](.*?)(/)([0-9]+)(->)?$", Pattern.DOTALL);`
- Line 156: `private static final Pattern MODIFIER_PATTERN = Pattern.compile("[/+*&?]");`

### Unused Code (7)
- Line 33: `private boolean skip;`
- Line 34: `private boolean skipRightPadding;`
- Line 35: `private int appendPosition;`
- Line 36: `private String name;`
- Line 12: `import java.util.EnumSet;`
- Line 13: `import java.util.regex.Matcher;`
- Line 14: `import java.util.regex.Pattern;`

## ../libs/dissect/src/main/java/org/elasticsearch/dissect/DissectMatch.java

### Concurrency Issue (3)
- Line 171: `private void setValue(String value) {`
- Line 175: `private void setKey(String key) {`
- Line 29: `private int implicitAppendOrder = -1000;`

### Exception Handling (1)
- Line 39: `throw new IllegalArgumentException("Expected results are zero, can not construct DissectMatch");// should never happen`

### Unused Code (10)
- Line 29: `private int implicitAppendOrder = -1000;`
- Line 35: `private int matches = 0;`
- Line 159: `private String key;`
- Line 169: `private String value;`
- Line 12: `import java.util.ArrayList;`
- Line 13: `import java.util.Collections;`
- Line 14: `import java.util.HashMap;`
- Line 15: `import java.util.List;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.stream.Collectors;`

## ../libs/dissect/src/main/java/org/elasticsearch/dissect/DissectParser.java

### Concurrency Issue (3)
- Line 30: `* match a string of the form: <pre>foo bar,baz</pre> and will result a key/value pairing of <pre>a=foo, b=bar, and c=baz.</pre>`
- Line 88: `private static final Pattern KEY_DELIMITER_FIELD_PATTERN = Pattern.compile("%\\{([^}]*?)}(.+?(?=%\\{)|.*$)", Pattern.DOTALL);`
- Line 100: `private String leadingDelimiter = "";`

### Unused Code (14)
- Line 100: `private String leadingDelimiter = "";`
- Line 12: `import java.nio.charset.StandardCharsets;`
- Line 13: `import java.util.ArrayList;`
- Line 14: `import java.util.Arrays;`
- Line 15: `import java.util.EnumSet;`
- Line 16: `import java.util.Iterator;`
- Line 17: `import java.util.LinkedHashSet;`
- Line 18: `import java.util.List;`
- Line 19: `import java.util.Map;`
- Line 20: `import java.util.Set;`
- Line 21: `import java.util.function.Function;`
- Line 22: `import java.util.regex.Matcher;`
- Line 23: `import java.util.regex.Pattern;`
- Line 24: `import java.util.stream.Collectors;`

## ../libs/dissect/src/test/java/org/elasticsearch/dissect/DissectKeyTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.hamcrest.CoreMatchers;`
- Line 15: `import java.util.EnumSet;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.stream.Collectors;`
- Line 19: `import static org.hamcrest.Matchers.equalTo;`
- Line 20: `import static org.hamcrest.Matchers.is;`

## ../libs/dissect/src/test/java/org/elasticsearch/dissect/DissectMatchTests.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.util.Map;`
- Line 16: `import java.util.stream.IntStream;`
- Line 18: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/dissect/src/test/java/org/elasticsearch/dissect/DissectParserTests.java

### Unused Code (13)
- Line 12: `import com.fasterxml.jackson.databind.JsonNode;`
- Line 13: `import com.fasterxml.jackson.databind.ObjectMapper;`
- Line 15: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import org.hamcrest.Matchers;`
- Line 17: `import org.mockito.internal.util.collections.Sets;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.Arrays;`
- Line 21: `import java.util.Iterator;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Map;`
- Line 25: `import static com.carrotsearch.randomizedtesting.RandomizedTest.randomAsciiAlphanumOfLengthBetween;`
- Line 26: `import static org.hamcrest.Matchers.contains;`
- Line 27: `import static org.hamcrest.Matchers.empty;`

## ../libs/entitlement/agent/src/main/java/org/elasticsearch/entitlement/agent/EntitlementAgent.java

### Unused Code (3)
- Line 12: `import java.lang.instrument.Instrumentation;`
- Line 13: `import java.lang.reflect.InvocationTargetException;`
- Line 14: `import java.lang.reflect.Method;`

## ../libs/entitlement/asm-provider/src/main/java/module-info.java

### Unused Code (2)
- Line 10: `import org.elasticsearch.entitlement.instrumentation.InstrumentationService;`
- Line 11: `import org.elasticsearch.entitlement.instrumentation.impl.InstrumentationServiceImpl;`

## ../libs/entitlement/asm-provider/src/main/java/org/elasticsearch/entitlement/instrumentation/impl/InstrumentationServiceImpl.java

### Unused Code (24)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.instrumentation.CheckMethod;`
- Line 14: `import org.elasticsearch.entitlement.instrumentation.InstrumentationService;`
- Line 15: `import org.elasticsearch.entitlement.instrumentation.Instrumenter;`
- Line 16: `import org.elasticsearch.entitlement.instrumentation.MethodKey;`
- Line 17: `import org.objectweb.asm.ClassReader;`
- Line 18: `import org.objectweb.asm.ClassVisitor;`
- Line 19: `import org.objectweb.asm.MethodVisitor;`
- Line 20: `import org.objectweb.asm.Opcodes;`
- Line 21: `import org.objectweb.asm.Type;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.lang.reflect.Method;`
- Line 25: `import java.lang.reflect.Modifier;`
- Line 26: `import java.util.ArrayDeque;`
- Line 27: `import java.util.Arrays;`
- Line 28: `import java.util.Collections;`
- Line 29: `import java.util.HashMap;`
- Line 30: `import java.util.HashSet;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.Locale;`
- Line 33: `import java.util.Map;`
- Line 34: `import java.util.Set;`
- Line 35: `import java.util.stream.Collectors;`
- Line 36: `import java.util.stream.Stream;`

## ../libs/entitlement/asm-provider/src/main/java/org/elasticsearch/entitlement/instrumentation/impl/InstrumenterImpl.java

### Concurrency Issue (2)
- Line 46: `private static final Logger logger = LogManager.getLogger(InstrumenterImpl.class);`
- Line 142: `private static final String ENTITLEMENT_ANNOTATION_DESCRIPTOR = Type.getDescriptor(EntitlementInstrumented.class);`

### Exception Handling (1)
- Line 83: `throw new IllegalStateException("Classfile not found in jar: " + fileName);`

### Unused Code (33)
- Line 146: `private boolean isAnnotationPresent;`
- Line 147: `private boolean annotationNeeded = true;`
- Line 241: `private boolean hasCallerSensitiveAnnotation = false;`
- Line 12: `import org.elasticsearch.core.Strings;`
- Line 13: `import org.elasticsearch.entitlement.instrumentation.CheckMethod;`
- Line 14: `import org.elasticsearch.entitlement.instrumentation.EntitlementInstrumented;`
- Line 15: `import org.elasticsearch.entitlement.instrumentation.Instrumenter;`
- Line 16: `import org.elasticsearch.entitlement.instrumentation.MethodKey;`
- Line 17: `import org.elasticsearch.logging.LogManager;`
- Line 18: `import org.elasticsearch.logging.Logger;`
- Line 19: `import org.objectweb.asm.AnnotationVisitor;`
- Line 20: `import org.objectweb.asm.ClassReader;`
- Line 21: `import org.objectweb.asm.ClassVisitor;`
- Line 22: `import org.objectweb.asm.ClassWriter;`
- Line 23: `import org.objectweb.asm.FieldVisitor;`
- Line 24: `import org.objectweb.asm.MethodVisitor;`
- Line 25: `import org.objectweb.asm.Opcodes;`
- Line 26: `import org.objectweb.asm.RecordComponentVisitor;`
- Line 27: `import org.objectweb.asm.Type;`
- Line 28: `import org.objectweb.asm.util.CheckClassAdapter;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.io.InputStream;`
- Line 32: `import java.io.PrintWriter;`
- Line 33: `import java.io.StringWriter;`
- Line 34: `import java.util.Map;`
- Line 35: `import java.util.stream.Stream;`
- Line 37: `import static org.objectweb.asm.ClassWriter.COMPUTE_FRAMES;`
- Line 38: `import static org.objectweb.asm.ClassWriter.COMPUTE_MAXS;`
- Line 39: `import static org.objectweb.asm.Opcodes.ACC_STATIC;`
- Line 40: `import static org.objectweb.asm.Opcodes.GETSTATIC;`
- Line 41: `import static org.objectweb.asm.Opcodes.INVOKEINTERFACE;`
- Line 42: `import static org.objectweb.asm.Opcodes.INVOKESTATIC;`
- Line 43: `import static org.objectweb.asm.Opcodes.INVOKEVIRTUAL;`

## ../libs/entitlement/asm-provider/src/test/java/org/elasticsearch/entitlement/instrumentation/impl/ASMUtils.java

### Unused Code (6)
- Line 12: `import org.objectweb.asm.ClassReader;`
- Line 13: `import org.objectweb.asm.util.Printer;`
- Line 14: `import org.objectweb.asm.util.Textifier;`
- Line 15: `import org.objectweb.asm.util.TraceClassVisitor;`
- Line 17: `import java.io.PrintWriter;`
- Line 18: `import java.io.StringWriter;`

## ../libs/entitlement/asm-provider/src/test/java/org/elasticsearch/entitlement/instrumentation/impl/InstrumentationServiceImplTests.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.entitlement.instrumentation.CheckMethod;`
- Line 13: `import org.elasticsearch.entitlement.instrumentation.InstrumentationService;`
- Line 14: `import org.elasticsearch.entitlement.instrumentation.MethodKey;`
- Line 15: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import org.objectweb.asm.Type;`
- Line 18: `import java.util.List;`
- Line 19: `import java.util.Map;`
- Line 21: `import static org.hamcrest.Matchers.aMapWithSize;`
- Line 22: `import static org.hamcrest.Matchers.containsString;`
- Line 23: `import static org.hamcrest.Matchers.equalTo;`
- Line 24: `import static org.hamcrest.Matchers.hasEntry;`

## ../libs/entitlement/asm-provider/src/test/java/org/elasticsearch/entitlement/instrumentation/impl/InstrumenterTests.java

### Concurrency Issue (2)
- Line 131: `static MockEntitlementCheckerImpl checkerInstance = new MockEntitlementCheckerImpl();`
- Line 150: `int checkCtorCallCount = 0;`

### Exception Handling (1)
- Line 155: `throw new TestException();`

### Unused Code (23)
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.entitlement.instrumentation.CheckMethod;`
- Line 14: `import org.elasticsearch.entitlement.instrumentation.MethodKey;`
- Line 15: `import org.elasticsearch.entitlement.instrumentation.impl.InstrumenterImpl.ClassFileInfo;`
- Line 16: `import org.elasticsearch.logging.LogManager;`
- Line 17: `import org.elasticsearch.logging.Logger;`
- Line 18: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import org.junit.Before;`
- Line 20: `import org.objectweb.asm.Type;`
- Line 22: `import java.io.IOException;`
- Line 23: `import java.lang.reflect.AccessFlag;`
- Line 24: `import java.lang.reflect.Constructor;`
- Line 25: `import java.lang.reflect.Executable;`
- Line 26: `import java.lang.reflect.InvocationTargetException;`
- Line 27: `import java.lang.reflect.Method;`
- Line 28: `import java.util.Arrays;`
- Line 29: `import java.util.HashMap;`
- Line 30: `import java.util.Map;`
- Line 31: `import java.util.Set;`
- Line 32: `import java.util.stream.Stream;`
- Line 34: `import static org.elasticsearch.entitlement.instrumentation.impl.ASMUtils.bytecode2text;`
- Line 35: `import static org.elasticsearch.entitlement.instrumentation.impl.InstrumenterImpl.getClassFileInfo;`
- Line 36: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/EntitlementChecker.java

### Unused Code (84)
- Line 12: `import jdk.nio.Channels;`
- Line 14: `import java.io.File;`
- Line 15: `import java.io.FileDescriptor;`
- Line 16: `import java.io.FileFilter;`
- Line 17: `import java.io.FilenameFilter;`
- Line 18: `import java.io.InputStream;`
- Line 19: `import java.io.OutputStream;`
- Line 20: `import java.io.PrintStream;`
- Line 21: `import java.io.PrintWriter;`
- Line 22: `import java.lang.foreign.AddressLayout;`
- Line 23: `import java.lang.foreign.Arena;`
- Line 24: `import java.lang.foreign.FunctionDescriptor;`
- Line 25: `import java.lang.foreign.Linker;`
- Line 26: `import java.lang.foreign.MemoryLayout;`
- Line 27: `import java.lang.foreign.MemorySegment;`
- Line 28: `import java.lang.invoke.MethodHandle;`
- Line 29: `import java.net.ContentHandlerFactory;`
- Line 30: `import java.net.DatagramPacket;`
- Line 31: `import java.net.DatagramSocket;`
- Line 32: `import java.net.DatagramSocketImplFactory;`
- Line 33: `import java.net.FileNameMap;`
- Line 34: `import java.net.InetAddress;`
- Line 35: `import java.net.MulticastSocket;`
- Line 36: `import java.net.NetworkInterface;`
- Line 37: `import java.net.Proxy;`
- Line 38: `import java.net.ProxySelector;`
- Line 39: `import java.net.ResponseCache;`
- Line 40: `import java.net.ServerSocket;`
- Line 41: `import java.net.Socket;`
- Line 42: `import java.net.SocketAddress;`
- Line 43: `import java.net.SocketImplFactory;`
- Line 44: `import java.net.URI;`
- Line 45: `import java.net.URL;`
- Line 46: `import java.net.URLStreamHandler;`
- Line 47: `import java.net.URLStreamHandlerFactory;`
- Line 48: `import java.net.http.HttpClient;`
- Line 49: `import java.net.http.HttpRequest;`
- Line 50: `import java.net.http.HttpResponse;`
- Line 51: `import java.nio.ByteBuffer;`
- Line 52: `import java.nio.channels.AsynchronousServerSocketChannel;`
- Line 53: `import java.nio.channels.AsynchronousSocketChannel;`
- Line 54: `import java.nio.channels.CompletionHandler;`
- Line 55: `import java.nio.channels.DatagramChannel;`
- Line 56: `import java.nio.channels.ServerSocketChannel;`
- Line 57: `import java.nio.channels.SocketChannel;`
- Line 58: `import java.nio.channels.spi.SelectorProvider;`
- Line 59: `import java.nio.charset.Charset;`
- Line 60: `import java.nio.file.AccessMode;`
- Line 61: `import java.nio.file.CopyOption;`
- Line 62: `import java.nio.file.DirectoryStream;`
- Line 63: `import java.nio.file.FileStore;`
- Line 64: `import java.nio.file.FileVisitOption;`
- Line 65: `import java.nio.file.FileVisitor;`
- Line 66: `import java.nio.file.LinkOption;`
- Line 67: `import java.nio.file.NoSuchFileException;`
- Line 68: `import java.nio.file.OpenOption;`
- Line 69: `import java.nio.file.Path;`
- Line 70: `import java.nio.file.WatchEvent;`
- Line 71: `import java.nio.file.WatchService;`
- Line 72: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 73: `import java.nio.file.attribute.FileAttribute;`
- Line 74: `import java.nio.file.attribute.FileAttributeView;`
- Line 75: `import java.nio.file.attribute.FileTime;`
- Line 76: `import java.nio.file.attribute.PosixFilePermission;`
- Line 77: `import java.nio.file.attribute.UserPrincipal;`
- Line 78: `import java.nio.file.spi.FileSystemProvider;`
- Line 79: `import java.security.KeyStore;`
- Line 80: `import java.security.Provider;`
- Line 81: `import java.security.cert.CertStoreParameters;`
- Line 82: `import java.util.List;`
- Line 83: `import java.util.Locale;`
- Line 84: `import java.util.Map;`
- Line 85: `import java.util.Properties;`
- Line 86: `import java.util.Set;`
- Line 87: `import java.util.TimeZone;`
- Line 88: `import java.util.concurrent.ExecutorService;`
- Line 89: `import java.util.concurrent.ForkJoinPool;`
- Line 90: `import java.util.function.BiPredicate;`
- Line 91: `import java.util.function.Consumer;`
- Line 92: `import java.util.logging.FileHandler;`
- Line 94: `import javax.net.ssl.HostnameVerifier;`
- Line 95: `import javax.net.ssl.HttpsURLConnection;`
- Line 96: `import javax.net.ssl.SSLContext;`
- Line 97: `import javax.net.ssl.SSLSocketFactory;`

## ../libs/entitlement/bridge/src/main/java/org/elasticsearch/entitlement/bridge/HandleLoader.java

### Unused Code (2)
- Line 12: `import java.lang.reflect.InvocationTargetException;`
- Line 13: `import java.lang.reflect.Method;`

## ../libs/entitlement/qa/entitled-plugin/src/main/java/org/elasticsearch/entitlement/qa/entitled/EntitledActions.java

### Concurrency Issue (2)
- Line 33: `private static final SecureRandom random = new SecureRandom();`
- Line 35: `private static final Path testRootDir = Paths.get(System.getProperty("es.entitlements.testdir"));`

### Unused Code (15)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.net.URI;`
- Line 16: `import java.net.URISyntaxException;`
- Line 17: `import java.net.URLConnection;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.nio.file.Paths;`
- Line 21: `import java.nio.file.StandardOpenOption;`
- Line 22: `import java.nio.file.attribute.UserPrincipal;`
- Line 23: `import java.security.SecureRandom;`
- Line 24: `import java.util.jar.Attributes;`
- Line 25: `import java.util.jar.JarEntry;`
- Line 26: `import java.util.jar.JarOutputStream;`
- Line 27: `import java.util.jar.Manifest;`

## ../libs/entitlement/qa/entitled-plugin/src/main/java/org/elasticsearch/entitlement/qa/entitled/EntitledPlugin.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.entitlement.runtime.api.NotEntitledException;`
- Line 13: `import org.elasticsearch.logging.LogManager;`
- Line 14: `import org.elasticsearch.logging.Logger;`
- Line 15: `import org.elasticsearch.plugins.ExtensiblePlugin;`
- Line 16: `import org.elasticsearch.plugins.Plugin;`
- Line 18: `import java.util.concurrent.atomic.AtomicBoolean;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/DummyImplementations.java

### Unused Code (78)
- Line 12: `import jdk.nio.Channels;`
- Line 14: `import org.elasticsearch.core.SuppressForbidden;`
- Line 16: `import java.io.InputStream;`
- Line 17: `import java.io.OutputStream;`
- Line 18: `import java.net.DatagramPacket;`
- Line 19: `import java.net.DatagramSocket;`
- Line 20: `import java.net.DatagramSocketImpl;`
- Line 21: `import java.net.InetAddress;`
- Line 22: `import java.net.NetworkInterface;`
- Line 23: `import java.net.ProtocolFamily;`
- Line 24: `import java.net.ServerSocket;`
- Line 25: `import java.net.Socket;`
- Line 26: `import java.net.SocketAddress;`
- Line 27: `import java.net.SocketException;`
- Line 28: `import java.net.SocketImpl;`
- Line 29: `import java.net.URI;`
- Line 30: `import java.nio.ByteBuffer;`
- Line 31: `import java.nio.MappedByteBuffer;`
- Line 32: `import java.nio.channels.AsynchronousChannelGroup;`
- Line 33: `import java.nio.channels.AsynchronousFileChannel;`
- Line 34: `import java.nio.channels.AsynchronousServerSocketChannel;`
- Line 35: `import java.nio.channels.AsynchronousSocketChannel;`
- Line 36: `import java.nio.channels.CompletionHandler;`
- Line 37: `import java.nio.channels.DatagramChannel;`
- Line 38: `import java.nio.channels.FileChannel;`
- Line 39: `import java.nio.channels.FileLock;`
- Line 40: `import java.nio.channels.Pipe;`
- Line 41: `import java.nio.channels.ReadableByteChannel;`
- Line 42: `import java.nio.channels.SeekableByteChannel;`
- Line 43: `import java.nio.channels.SelectableChannel;`
- Line 44: `import java.nio.channels.ServerSocketChannel;`
- Line 45: `import java.nio.channels.SocketChannel;`
- Line 46: `import java.nio.channels.WritableByteChannel;`
- Line 47: `import java.nio.channels.spi.AbstractSelector;`
- Line 48: `import java.nio.channels.spi.AsynchronousChannelProvider;`
- Line 49: `import java.nio.channels.spi.SelectorProvider;`
- Line 50: `import java.nio.charset.Charset;`
- Line 51: `import java.nio.charset.spi.CharsetProvider;`
- Line 52: `import java.nio.file.AccessMode;`
- Line 53: `import java.nio.file.CopyOption;`
- Line 54: `import java.nio.file.DirectoryStream;`
- Line 55: `import java.nio.file.FileStore;`
- Line 56: `import java.nio.file.FileSystem;`
- Line 57: `import java.nio.file.LinkOption;`
- Line 58: `import java.nio.file.OpenOption;`
- Line 59: `import java.nio.file.Path;`
- Line 60: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 61: `import java.nio.file.attribute.FileAttribute;`
- Line 62: `import java.nio.file.attribute.FileAttributeView;`
- Line 63: `import java.nio.file.spi.FileSystemProvider;`
- Line 64: `import java.security.cert.Certificate;`
- Line 65: `import java.text.BreakIterator;`
- Line 66: `import java.text.Collator;`
- Line 67: `import java.text.DateFormat;`
- Line 68: `import java.text.DateFormatSymbols;`
- Line 69: `import java.text.DecimalFormatSymbols;`
- Line 70: `import java.text.NumberFormat;`
- Line 71: `import java.text.spi.BreakIteratorProvider;`
- Line 72: `import java.text.spi.CollatorProvider;`
- Line 73: `import java.text.spi.DateFormatProvider;`
- Line 74: `import java.text.spi.DateFormatSymbolsProvider;`
- Line 75: `import java.text.spi.DecimalFormatSymbolsProvider;`
- Line 76: `import java.text.spi.NumberFormatProvider;`
- Line 77: `import java.util.Iterator;`
- Line 78: `import java.util.Locale;`
- Line 79: `import java.util.Map;`
- Line 80: `import java.util.Set;`
- Line 81: `import java.util.concurrent.ExecutorService;`
- Line 82: `import java.util.concurrent.Future;`
- Line 83: `import java.util.concurrent.ThreadFactory;`
- Line 84: `import java.util.spi.CalendarDataProvider;`
- Line 85: `import java.util.spi.CalendarNameProvider;`
- Line 86: `import java.util.spi.CurrencyNameProvider;`
- Line 87: `import java.util.spi.LocaleNameProvider;`
- Line 88: `import java.util.spi.LocaleServiceProvider;`
- Line 89: `import java.util.spi.TimeZoneNameProvider;`
- Line 91: `import javax.net.ssl.HttpsURLConnection;`
- Line 92: `import javax.net.ssl.SSLSocketFactory;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/EntitlementTest.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.entitlement.runtime.api.NotEntitledException;`
- Line 14: `import java.lang.annotation.ElementType;`
- Line 15: `import java.lang.annotation.Retention;`
- Line 16: `import java.lang.annotation.RetentionPolicy;`
- Line 17: `import java.lang.annotation.Target;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/EntitlementTestPlugin.java

### Unused Code (18)
- Line 32: `private Environment environment;`
- Line 11: `import org.elasticsearch.cluster.metadata.IndexNameExpressionResolver;`
- Line 12: `import org.elasticsearch.cluster.node.DiscoveryNodes;`
- Line 13: `import org.elasticsearch.common.io.stream.NamedWriteableRegistry;`
- Line 14: `import org.elasticsearch.common.settings.ClusterSettings;`
- Line 15: `import org.elasticsearch.common.settings.IndexScopedSettings;`
- Line 16: `import org.elasticsearch.common.settings.Settings;`
- Line 17: `import org.elasticsearch.common.settings.SettingsFilter;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 19: `import org.elasticsearch.features.NodeFeature;`
- Line 20: `import org.elasticsearch.plugins.ActionPlugin;`
- Line 21: `import org.elasticsearch.plugins.Plugin;`
- Line 22: `import org.elasticsearch.rest.RestController;`
- Line 23: `import org.elasticsearch.rest.RestHandler;`
- Line 25: `import java.util.Collection;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.function.Predicate;`
- Line 28: `import java.util.function.Supplier;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/FileCheckActions.java

### Unused Code (37)
- Line 12: `import org.elasticsearch.core.CheckedRunnable;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 15: `import org.elasticsearch.env.Environment;`
- Line 17: `import java.io.File;`
- Line 18: `import java.io.FileDescriptor;`
- Line 19: `import java.io.FileInputStream;`
- Line 20: `import java.io.FileNotFoundException;`
- Line 21: `import java.io.FileOutputStream;`
- Line 22: `import java.io.FileReader;`
- Line 23: `import java.io.FileWriter;`
- Line 24: `import java.io.IOException;`
- Line 25: `import java.io.RandomAccessFile;`
- Line 26: `import java.net.URISyntaxException;`
- Line 27: `import java.net.http.HttpRequest;`
- Line 28: `import java.net.http.HttpResponse;`
- Line 29: `import java.nio.charset.StandardCharsets;`
- Line 30: `import java.nio.file.Files;`
- Line 31: `import java.nio.file.Path;`
- Line 32: `import java.nio.file.Paths;`
- Line 33: `import java.security.GeneralSecurityException;`
- Line 34: `import java.security.KeyStore;`
- Line 35: `import java.util.Scanner;`
- Line 36: `import java.util.jar.JarFile;`
- Line 37: `import java.util.logging.FileHandler;`
- Line 38: `import java.util.zip.ZipException;`
- Line 39: `import java.util.zip.ZipFile;`
- Line 41: `import javax.imageio.stream.FileImageInputStream;`
- Line 43: `import static java.nio.charset.Charset.defaultCharset;`
- Line 44: `import static java.nio.file.StandardOpenOption.CREATE;`
- Line 45: `import static java.nio.file.StandardOpenOption.WRITE;`
- Line 46: `import static java.util.zip.ZipFile.OPEN_DELETE;`
- Line 47: `import static java.util.zip.ZipFile.OPEN_READ;`
- Line 48: `import static org.elasticsearch.entitlement.qa.entitled.EntitledActions.createTempFileForWrite;`
- Line 49: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_ALLOWED;`
- Line 50: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 51: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/FileStoreActions.java

### Unused Code (5)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.nio.file.Files;`
- Line 14: `import java.nio.file.attribute.FileStoreAttributeView;`
- Line 16: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 17: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.SERVER_ONLY;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/JvmActions.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.qa.entitled.EntitledPlugin;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.net.URL;`
- Line 17: `import java.net.URLClassLoader;`
- Line 18: `import java.util.Locale;`
- Line 19: `import java.util.TimeZone;`
- Line 21: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 22: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/ManageThreadsActions.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.util.concurrent.ForkJoinPool;`
- Line 15: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 17: `import static java.lang.Thread.currentThread;`
- Line 18: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/NativeActions.java

### Unused Code (21)
- Line 12: `import org.elasticsearch.entitlement.qa.entitled.EntitledPlugin;`
- Line 14: `import java.lang.foreign.AddressLayout;`
- Line 15: `import java.lang.foreign.Arena;`
- Line 16: `import java.lang.foreign.FunctionDescriptor;`
- Line 17: `import java.lang.foreign.Linker;`
- Line 18: `import java.lang.foreign.MemoryLayout;`
- Line 19: `import java.lang.foreign.MemorySegment;`
- Line 20: `import java.lang.foreign.SymbolLookup;`
- Line 21: `import java.lang.foreign.ValueLayout;`
- Line 22: `import java.lang.invoke.MethodHandle;`
- Line 23: `import java.lang.invoke.MethodHandles;`
- Line 24: `import java.lang.invoke.MethodType;`
- Line 25: `import java.lang.module.Configuration;`
- Line 26: `import java.lang.module.ModuleFinder;`
- Line 27: `import java.nio.file.Path;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Set;`
- Line 31: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 32: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 33: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`
- Line 34: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.SERVER_ONLY;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/NetworkAccessCheckActions.java

### Unused Code (21)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.io.IOException;`
- Line 15: `import java.net.InetAddress;`
- Line 16: `import java.net.InetSocketAddress;`
- Line 17: `import java.net.Proxy;`
- Line 18: `import java.net.ServerSocket;`
- Line 19: `import java.net.Socket;`
- Line 20: `import java.net.SocketException;`
- Line 21: `import java.nio.ByteBuffer;`
- Line 22: `import java.nio.channels.AsynchronousServerSocketChannel;`
- Line 23: `import java.nio.channels.AsynchronousSocketChannel;`
- Line 24: `import java.nio.channels.CompletionHandler;`
- Line 25: `import java.nio.channels.DatagramChannel;`
- Line 26: `import java.nio.channels.NotYetBoundException;`
- Line 27: `import java.nio.channels.ServerSocketChannel;`
- Line 28: `import java.nio.channels.SocketChannel;`
- Line 29: `import java.security.InvalidAlgorithmParameterException;`
- Line 30: `import java.security.NoSuchAlgorithmException;`
- Line 31: `import java.security.cert.CertStore;`
- Line 32: `import java.util.Arrays;`
- Line 33: `import java.util.concurrent.ExecutionException;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/NioChannelsActions.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 16: `import java.io.FileDescriptor;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.nio.channels.AsynchronousFileChannel;`
- Line 19: `import java.nio.channels.FileChannel;`
- Line 20: `import java.nio.file.StandardOpenOption;`
- Line 21: `import java.util.Set;`
- Line 23: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 24: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/NioFileSystemActions.java

### Unused Code (15)
- Line 12: `import org.elasticsearch.common.util.concurrent.EsExecutors;`
- Line 13: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.net.URI;`
- Line 17: `import java.nio.file.FileSystemException;`
- Line 18: `import java.nio.file.FileSystems;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.nio.file.StandardOpenOption;`
- Line 21: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 22: `import java.nio.file.attribute.FileOwnerAttributeView;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.Set;`
- Line 26: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 27: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`
- Line 28: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.SERVER_ONLY;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/NioFilesActions.java

### Unused Code (27)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 15: `import java.io.ByteArrayInputStream;`
- Line 16: `import java.io.ByteArrayOutputStream;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.nio.charset.Charset;`
- Line 19: `import java.nio.charset.StandardCharsets;`
- Line 20: `import java.nio.file.FileSystemException;`
- Line 21: `import java.nio.file.FileVisitOption;`
- Line 22: `import java.nio.file.FileVisitResult;`
- Line 23: `import java.nio.file.FileVisitor;`
- Line 24: `import java.nio.file.Files;`
- Line 25: `import java.nio.file.Path;`
- Line 26: `import java.nio.file.StandardOpenOption;`
- Line 27: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 28: `import java.nio.file.attribute.FileOwnerAttributeView;`
- Line 29: `import java.nio.file.attribute.FileTime;`
- Line 30: `import java.nio.file.attribute.UserPrincipal;`
- Line 31: `import java.time.Instant;`
- Line 32: `import java.util.List;`
- Line 33: `import java.util.Set;`
- Line 35: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 36: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`
- Line 37: `import static org.elasticsearch.entitlement.qa.test.FileCheckActions.readDir;`
- Line 38: `import static org.elasticsearch.entitlement.qa.test.FileCheckActions.readFile;`
- Line 39: `import static org.elasticsearch.entitlement.qa.test.FileCheckActions.readWriteDir;`
- Line 40: `import static org.elasticsearch.entitlement.qa.test.FileCheckActions.readWriteFile;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/OperatingSystemActions.java

### Unused Code (2)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.util.List;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/PathActions.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.PolicyManager;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.nio.file.FileSystems;`
- Line 17: `import java.nio.file.LinkOption;`
- Line 18: `import java.nio.file.NoSuchFileException;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.nio.file.WatchEvent;`
- Line 21: `import java.util.Arrays;`
- Line 23: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 24: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/RestEntitlementsCheckAction.java

### Null Pointer (3)
- Line 394: `return checkActions.entrySet()`
- Line 402: `return checkActions.entrySet()`
- Line 410: `return checkActions.entrySet()`

### Exception Handling (1)
- Line 432: `throw new IllegalArgumentException("Missing action parameter");`

### Unused Code (52)
- Line 12: `import org.elasticsearch.client.internal.node.NodeClient;`
- Line 13: `import org.elasticsearch.common.Strings;`
- Line 14: `import org.elasticsearch.core.CheckedConsumer;`
- Line 15: `import org.elasticsearch.core.CheckedRunnable;`
- Line 16: `import org.elasticsearch.core.SuppressForbidden;`
- Line 17: `import org.elasticsearch.entitlement.runtime.api.NotEntitledException;`
- Line 18: `import org.elasticsearch.env.Environment;`
- Line 19: `import org.elasticsearch.logging.LogManager;`
- Line 20: `import org.elasticsearch.logging.Logger;`
- Line 21: `import org.elasticsearch.rest.BaseRestHandler;`
- Line 22: `import org.elasticsearch.rest.RestRequest;`
- Line 23: `import org.elasticsearch.rest.RestResponse;`
- Line 24: `import org.elasticsearch.rest.RestStatus;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.lang.reflect.InvocationTargetException;`
- Line 28: `import java.lang.reflect.Method;`
- Line 29: `import java.lang.reflect.Modifier;`
- Line 30: `import java.net.DatagramPacket;`
- Line 31: `import java.net.DatagramSocket;`
- Line 32: `import java.net.HttpURLConnection;`
- Line 33: `import java.net.InetAddress;`
- Line 34: `import java.net.InetSocketAddress;`
- Line 35: `import java.net.MalformedURLException;`
- Line 36: `import java.net.NetworkInterface;`
- Line 37: `import java.net.ProxySelector;`
- Line 38: `import java.net.ResponseCache;`
- Line 39: `import java.net.ServerSocket;`
- Line 40: `import java.net.Socket;`
- Line 41: `import java.net.SocketException;`
- Line 42: `import java.net.URL;`
- Line 43: `import java.net.URLConnection;`
- Line 44: `import java.net.URLStreamHandler;`
- Line 45: `import java.net.spi.URLStreamHandlerProvider;`
- Line 46: `import java.security.NoSuchAlgorithmException;`
- Line 47: `import java.util.ArrayList;`
- Line 48: `import java.util.List;`
- Line 49: `import java.util.Map;`
- Line 50: `import java.util.Map.Entry;`
- Line 51: `import java.util.Set;`
- Line 52: `import java.util.function.Function;`
- Line 53: `import java.util.stream.Collectors;`
- Line 54: `import java.util.stream.Stream;`
- Line 56: `import javax.net.ssl.HttpsURLConnection;`
- Line 57: `import javax.net.ssl.SSLContext;`
- Line 59: `import static java.util.Map.entry;`
- Line 60: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_ALLOWED;`
- Line 61: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 62: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`
- Line 63: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.SERVER_ONLY;`
- Line 64: `import static org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction.CheckAction.alwaysDenied;`
- Line 65: `import static org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction.CheckAction.forPlugins;`
- Line 66: `import static org.elasticsearch.rest.RestRequest.Method.GET;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/SpiActions.java

### Unused Code (4)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.nio.channels.Channel;`
- Line 14: `import java.nio.channels.spi.SelectorProvider;`
- Line 16: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/SystemActions.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.ALWAYS_DENIED;`
- Line 15: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.SERVER_ONLY;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/URLConnectionFileActions.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.core.CheckedConsumer;`
- Line 13: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.net.JarURLConnection;`
- Line 17: `import java.net.URLConnection;`
- Line 19: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/URLConnectionNetworkActions.java

### Exception Handling (2)
- Line 41: `throw new RuntimeException(e);`
- Line 62: `throw new ConnectException();`

### Unused Code (16)
- Line 12: `import org.elasticsearch.core.CheckedConsumer;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.entitlement.qa.entitled.EntitledActions;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.io.InputStream;`
- Line 18: `import java.net.ConnectException;`
- Line 19: `import java.net.HttpURLConnection;`
- Line 20: `import java.net.InetSocketAddress;`
- Line 21: `import java.net.MalformedURLException;`
- Line 22: `import java.net.Proxy;`
- Line 23: `import java.net.URI;`
- Line 24: `import java.net.URISyntaxException;`
- Line 25: `import java.net.URL;`
- Line 26: `import java.net.URLConnection;`
- Line 28: `import javax.net.ssl.HttpsURLConnection;`
- Line 30: `import static org.elasticsearch.entitlement.qa.test.EntitlementTest.ExpectedAccess.PLUGINS;`

## ../libs/entitlement/qa/entitlement-test-plugin/src/main/java/org/elasticsearch/entitlement/qa/test/VersionSpecificNetworkChecks.java

### Unused Code (7)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.net.URI;`
- Line 14: `import java.net.http.HttpClient;`
- Line 15: `import java.net.http.HttpRequest;`
- Line 16: `import java.net.http.HttpResponse;`
- Line 17: `import java.net.spi.InetAddressResolver;`
- Line 18: `import java.net.spi.InetAddressResolverProvider;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/AbstractEntitlementsIT.java

### Unused Code (12)
- Line 12: `import org.elasticsearch.client.Request;`
- Line 13: `import org.elasticsearch.client.Response;`
- Line 14: `import org.elasticsearch.client.ResponseException;`
- Line 15: `import org.elasticsearch.entitlement.qa.EntitlementsTestRule.PolicyBuilder;`
- Line 16: `import org.elasticsearch.test.rest.ESRestTestCase;`
- Line 17: `import org.hamcrest.Description;`
- Line 18: `import org.hamcrest.Matcher;`
- Line 19: `import org.hamcrest.TypeSafeMatcher;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Map;`
- Line 25: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsAllowedIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(true, ALLOWED_TEST_ENTITLEMENTS);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsAllowedNonModularIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(false, ALLOWED_TEST_ENTITLEMENTS);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsAllowedViaOverrideIT.java

### Concurrency Issue (1)
- Line 43: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(`

### Unused Code (11)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.core.Strings;`
- Line 16: `import org.junit.ClassRule;`
- Line 18: `import java.nio.charset.StandardCharsets;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.Base64;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.stream.Stream;`
- Line 24: `import static org.elasticsearch.entitlement.qa.EntitlementsTestRule.ENTITLEMENT_QA_TEST_MODULE_NAME;`
- Line 25: `import static org.elasticsearch.entitlement.qa.EntitlementsTestRule.ENTITLEMENT_TEST_PLUGIN_NAME;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsAlwaysAllowedIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(true, null);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsAlwaysAllowedNonModularIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(false, null);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(true, null);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsDeniedNonModularIT.java

### Concurrency Issue (1)
- Line 21: `public static EntitlementsTestRule testRule = new EntitlementsTestRule(false, null);`

### Unused Code (4)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.Name;`
- Line 13: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 15: `import org.elasticsearch.entitlement.qa.test.RestEntitlementsCheckAction;`
- Line 16: `import org.junit.ClassRule;`

## ../libs/entitlement/qa/src/javaRestTest/java/org/elasticsearch/entitlement/qa/EntitlementsTestRule.java

### Concurrency Issue (1)
- Line 51: `public static final String ENTITLEMENT_QA_TEST_MODULE_NAME = "org.elasticsearch.entitlement.qa.test";`

### Exception Handling (1)
- Line 117: `throw new UncheckedIOException(e);`

### Unused Code (18)
- Line 12: `import org.elasticsearch.common.Strings;`
- Line 13: `import org.elasticsearch.test.cluster.ElasticsearchCluster;`
- Line 14: `import org.elasticsearch.test.cluster.local.PluginInstallSpec;`
- Line 15: `import org.elasticsearch.test.cluster.util.resource.Resource;`
- Line 16: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 17: `import org.elasticsearch.xcontent.yaml.YamlXContent;`
- Line 18: `import org.junit.rules.ExternalResource;`
- Line 19: `import org.junit.rules.RuleChain;`
- Line 20: `import org.junit.rules.TemporaryFolder;`
- Line 21: `import org.junit.rules.TestRule;`
- Line 22: `import org.junit.runner.Description;`
- Line 23: `import org.junit.runners.model.Statement;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.UncheckedIOException;`
- Line 27: `import java.nio.file.Files;`
- Line 28: `import java.nio.file.Path;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Map;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/bootstrap/EntitlementBootstrap.java

### Exception Handling (5)
- Line 59: `throw new IllegalArgumentException("must provide at least one data directory");`
- Line 118: `throw new IllegalStateException("plugin data is already set");`
- Line 151: `throw new IllegalStateException("Unable to attach entitlement agent", e);`
- Line 171: `throw new IllegalStateException("Directory for entitlement jar does not exist: " + dir);`
- Line 180: `throw new IllegalStateException("Failed to list entitlement jars in: " + dir, e);`

### Unused Code (18)
- Line 12: `import com.sun.tools.attach.AgentInitializationException;`
- Line 13: `import com.sun.tools.attach.AgentLoadException;`
- Line 14: `import com.sun.tools.attach.AttachNotSupportedException;`
- Line 15: `import com.sun.tools.attach.VirtualMachine;`
- Line 17: `import org.elasticsearch.core.Nullable;`
- Line 18: `import org.elasticsearch.core.SuppressForbidden;`
- Line 19: `import org.elasticsearch.entitlement.initialization.EntitlementInitialization;`
- Line 20: `import org.elasticsearch.entitlement.runtime.policy.Policy;`
- Line 21: `import org.elasticsearch.logging.LogManager;`
- Line 22: `import org.elasticsearch.logging.Logger;`
- Line 24: `import java.io.IOException;`
- Line 25: `import java.nio.file.Files;`
- Line 26: `import java.nio.file.Path;`
- Line 27: `import java.util.Map;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.function.Function;`
- Line 30: `import java.util.stream.Stream;`
- Line 32: `import static java.util.Objects.requireNonNull;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/initialization/EntitlementInitialization.java

### Concurrency Issue (2)
- Line 85: `private static final String AGENTS_PACKAGE_NAME = "co.elastic.apm.agent";`
- Line 86: `private static final Module ENTITLEMENTS_MODULE = PolicyManager.class.getModule();`

### Exception Handling (3)
- Line 334: `throw new IllegalStateException("user.home system property is required");`
- Line 422: `throw new RuntimeException(e);`
- Line 449: `throw new RuntimeException(e);`

### Unused Code (61)
- Line 12: `import org.elasticsearch.core.Booleans;`
- Line 13: `import org.elasticsearch.core.PathUtils;`
- Line 14: `import org.elasticsearch.core.internal.provider.ProviderLocator;`
- Line 15: `import org.elasticsearch.entitlement.bootstrap.EntitlementBootstrap;`
- Line 16: `import org.elasticsearch.entitlement.bridge.EntitlementChecker;`
- Line 17: `import org.elasticsearch.entitlement.instrumentation.CheckMethod;`
- Line 18: `import org.elasticsearch.entitlement.instrumentation.InstrumentationService;`
- Line 19: `import org.elasticsearch.entitlement.instrumentation.Instrumenter;`
- Line 20: `import org.elasticsearch.entitlement.instrumentation.MethodKey;`
- Line 21: `import org.elasticsearch.entitlement.instrumentation.Transformer;`
- Line 22: `import org.elasticsearch.entitlement.runtime.api.ElasticsearchEntitlementChecker;`
- Line 23: `import org.elasticsearch.entitlement.runtime.policy.PathLookup;`
- Line 24: `import org.elasticsearch.entitlement.runtime.policy.Policy;`
- Line 25: `import org.elasticsearch.entitlement.runtime.policy.PolicyManager;`
- Line 26: `import org.elasticsearch.entitlement.runtime.policy.PolicyUtils;`
- Line 27: `import org.elasticsearch.entitlement.runtime.policy.Scope;`
- Line 28: `import org.elasticsearch.entitlement.runtime.policy.entitlements.CreateClassLoaderEntitlement;`
- Line 29: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 30: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ExitVMEntitlement;`
- Line 31: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 32: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.FileData;`
- Line 33: `import org.elasticsearch.entitlement.runtime.policy.entitlements.InboundNetworkEntitlement;`
- Line 34: `import org.elasticsearch.entitlement.runtime.policy.entitlements.LoadNativeLibrariesEntitlement;`
- Line 35: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ManageThreadsEntitlement;`
- Line 36: `import org.elasticsearch.entitlement.runtime.policy.entitlements.OutboundNetworkEntitlement;`
- Line 37: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ReadStoreAttributesEntitlement;`
- Line 38: `import org.elasticsearch.entitlement.runtime.policy.entitlements.SetHttpsConnectionPropertiesEntitlement;`
- Line 39: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 41: `import java.lang.instrument.Instrumentation;`
- Line 42: `import java.lang.reflect.Constructor;`
- Line 43: `import java.lang.reflect.InvocationTargetException;`
- Line 44: `import java.net.URI;`
- Line 45: `import java.nio.channels.spi.SelectorProvider;`
- Line 46: `import java.nio.file.AccessMode;`
- Line 47: `import java.nio.file.CopyOption;`
- Line 48: `import java.nio.file.DirectoryStream;`
- Line 49: `import java.nio.file.FileStore;`
- Line 50: `import java.nio.file.FileSystems;`
- Line 51: `import java.nio.file.LinkOption;`
- Line 52: `import java.nio.file.OpenOption;`
- Line 53: `import java.nio.file.Path;`
- Line 54: `import java.nio.file.WatchEvent;`
- Line 55: `import java.nio.file.WatchService;`
- Line 56: `import java.nio.file.attribute.FileAttribute;`
- Line 57: `import java.nio.file.spi.FileSystemProvider;`
- Line 58: `import java.util.ArrayList;`
- Line 59: `import java.util.Collections;`
- Line 60: `import java.util.HashMap;`
- Line 61: `import java.util.List;`
- Line 62: `import java.util.Map;`
- Line 63: `import java.util.Set;`
- Line 64: `import java.util.concurrent.ExecutorService;`
- Line 65: `import java.util.function.Function;`
- Line 66: `import java.util.stream.Collectors;`
- Line 67: `import java.util.stream.Stream;`
- Line 68: `import java.util.stream.StreamSupport;`
- Line 70: `import static org.elasticsearch.entitlement.runtime.policy.Platform.LINUX;`
- Line 71: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.BaseDir.DATA;`
- Line 72: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.BaseDir.SHARED_REPO;`
- Line 73: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ;`
- Line 74: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ_WRITE;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/instrumentation/CheckMethod.java

### Unused Code (1)
- Line 12: `import java.util.List;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/instrumentation/EntitlementInstrumented.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/instrumentation/InstrumentationService.java

### Unused Code (1)
- Line 12: `import java.util.Map;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/instrumentation/MethodKey.java

### Unused Code (1)
- Line 12: `import java.util.List;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/instrumentation/Transformer.java

### Concurrency Issue (1)
- Line 32: `public void enableClassVerification() {`

### Unused Code (4)
- Line 23: `private boolean verifyClasses;`
- Line 12: `import java.lang.instrument.ClassFileTransformer;`
- Line 13: `import java.security.ProtectionDomain;`
- Line 14: `import java.util.Set;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/ElasticsearchEntitlementChecker.java

### Exception Handling (1)
- Line 2779: `throw new RuntimeException(e);`

### Unused Code (96)
- Line 12: `import jdk.nio.Channels;`
- Line 14: `import org.elasticsearch.core.SuppressForbidden;`
- Line 15: `import org.elasticsearch.entitlement.bridge.EntitlementChecker;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.PolicyManager;`
- Line 18: `import java.io.File;`
- Line 19: `import java.io.FileDescriptor;`
- Line 20: `import java.io.FileFilter;`
- Line 21: `import java.io.FilenameFilter;`
- Line 22: `import java.io.InputStream;`
- Line 23: `import java.io.OutputStream;`
- Line 24: `import java.io.PrintStream;`
- Line 25: `import java.io.PrintWriter;`
- Line 26: `import java.lang.foreign.AddressLayout;`
- Line 27: `import java.lang.foreign.Arena;`
- Line 28: `import java.lang.foreign.FunctionDescriptor;`
- Line 29: `import java.lang.foreign.Linker;`
- Line 30: `import java.lang.foreign.MemoryLayout;`
- Line 31: `import java.lang.foreign.MemorySegment;`
- Line 32: `import java.lang.invoke.MethodHandle;`
- Line 33: `import java.net.ContentHandlerFactory;`
- Line 34: `import java.net.DatagramPacket;`
- Line 35: `import java.net.DatagramSocket;`
- Line 36: `import java.net.DatagramSocketImplFactory;`
- Line 37: `import java.net.FileNameMap;`
- Line 38: `import java.net.HttpURLConnection;`
- Line 39: `import java.net.InetAddress;`
- Line 40: `import java.net.InetSocketAddress;`
- Line 41: `import java.net.JarURLConnection;`
- Line 42: `import java.net.MalformedURLException;`
- Line 43: `import java.net.MulticastSocket;`
- Line 44: `import java.net.NetworkInterface;`
- Line 45: `import java.net.Proxy;`
- Line 46: `import java.net.ProxySelector;`
- Line 47: `import java.net.ResponseCache;`
- Line 48: `import java.net.ServerSocket;`
- Line 49: `import java.net.Socket;`
- Line 50: `import java.net.SocketAddress;`
- Line 51: `import java.net.SocketImplFactory;`
- Line 52: `import java.net.URI;`
- Line 53: `import java.net.URISyntaxException;`
- Line 54: `import java.net.URL;`
- Line 55: `import java.net.URLConnection;`
- Line 56: `import java.net.URLStreamHandler;`
- Line 57: `import java.net.URLStreamHandlerFactory;`
- Line 58: `import java.net.http.HttpClient;`
- Line 59: `import java.net.http.HttpRequest;`
- Line 60: `import java.net.http.HttpResponse;`
- Line 61: `import java.nio.ByteBuffer;`
- Line 62: `import java.nio.channels.AsynchronousServerSocketChannel;`
- Line 63: `import java.nio.channels.AsynchronousSocketChannel;`
- Line 64: `import java.nio.channels.CompletionHandler;`
- Line 65: `import java.nio.channels.DatagramChannel;`
- Line 66: `import java.nio.channels.ServerSocketChannel;`
- Line 67: `import java.nio.channels.SocketChannel;`
- Line 68: `import java.nio.channels.spi.SelectorProvider;`
- Line 69: `import java.nio.charset.Charset;`
- Line 70: `import java.nio.file.AccessMode;`
- Line 71: `import java.nio.file.CopyOption;`
- Line 72: `import java.nio.file.DirectoryStream;`
- Line 73: `import java.nio.file.FileStore;`
- Line 74: `import java.nio.file.FileVisitOption;`
- Line 75: `import java.nio.file.FileVisitor;`
- Line 76: `import java.nio.file.LinkOption;`
- Line 77: `import java.nio.file.NoSuchFileException;`
- Line 78: `import java.nio.file.OpenOption;`
- Line 79: `import java.nio.file.Path;`
- Line 80: `import java.nio.file.Paths;`
- Line 81: `import java.nio.file.StandardOpenOption;`
- Line 82: `import java.nio.file.WatchEvent;`
- Line 83: `import java.nio.file.WatchService;`
- Line 84: `import java.nio.file.attribute.BasicFileAttributes;`
- Line 85: `import java.nio.file.attribute.FileAttribute;`
- Line 86: `import java.nio.file.attribute.FileAttributeView;`
- Line 87: `import java.nio.file.attribute.FileTime;`
- Line 88: `import java.nio.file.attribute.PosixFilePermission;`
- Line 89: `import java.nio.file.attribute.UserPrincipal;`
- Line 90: `import java.nio.file.spi.FileSystemProvider;`
- Line 91: `import java.security.KeyStore;`
- Line 92: `import java.security.Provider;`
- Line 93: `import java.security.cert.CertStoreParameters;`
- Line 94: `import java.util.Arrays;`
- Line 95: `import java.util.List;`
- Line 96: `import java.util.Locale;`
- Line 97: `import java.util.Map;`
- Line 98: `import java.util.Properties;`
- Line 99: `import java.util.Set;`
- Line 100: `import java.util.TimeZone;`
- Line 101: `import java.util.concurrent.ExecutorService;`
- Line 102: `import java.util.concurrent.ForkJoinPool;`
- Line 103: `import java.util.function.BiPredicate;`
- Line 104: `import java.util.function.Consumer;`
- Line 105: `import java.util.logging.FileHandler;`
- Line 107: `import javax.net.ssl.HostnameVerifier;`
- Line 108: `import javax.net.ssl.HttpsURLConnection;`
- Line 109: `import javax.net.ssl.SSLContext;`
- Line 110: `import javax.net.ssl.SSLSocketFactory;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/api/NotEntitledException.java

### Unused Code (1)
- Line 12: `import java.security.AccessControlException;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/ExternalEntitlement.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 14: `import java.lang.annotation.ElementType;`
- Line 15: `import java.lang.annotation.Retention;`
- Line 16: `import java.lang.annotation.RetentionPolicy;`
- Line 17: `import java.lang.annotation.Target;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/FileAccessTree.java

### Concurrency Issue (2)
- Line 107: `private static final Logger logger = LogManager.getLogger(FileAccessTree.class);`
- Line 108: `private static final String FILE_SEPARATOR = getDefaultFileSystem().getSeparator();`

### Exception Handling (2)
- Line 98: `throw new IllegalArgumentException(`
- Line 148: `throw new UncheckedIOException(e);`

### Unused Code (24)
- Line 12: `import org.elasticsearch.core.Nullable;`
- Line 13: `import org.elasticsearch.core.Strings;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode;`
- Line 16: `import org.elasticsearch.logging.LogManager;`
- Line 17: `import org.elasticsearch.logging.Logger;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.io.UncheckedIOException;`
- Line 21: `import java.nio.file.Files;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.nio.file.Paths;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.HashSet;`
- Line 28: `import java.util.List;`
- Line 29: `import java.util.Map;`
- Line 30: `import java.util.Objects;`
- Line 31: `import java.util.Set;`
- Line 32: `import java.util.function.BiConsumer;`
- Line 34: `import static java.util.Comparator.comparing;`
- Line 35: `import static org.elasticsearch.core.PathUtils.getDefaultFileSystem;`
- Line 36: `import static org.elasticsearch.entitlement.runtime.policy.FileUtils.PATH_ORDER;`
- Line 37: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ_WRITE;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/FileUtils.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import java.io.File;`
- Line 15: `import java.util.Comparator;`
- Line 17: `import static java.lang.Character.isLetter;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PathLookup.java

### Unused Code (3)
- Line 12: `import java.nio.file.Path;`
- Line 13: `import java.util.function.Function;`
- Line 14: `import java.util.stream.Stream;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/Platform.java

### Concurrency Issue (1)
- Line 17: `private static final Platform current = findCurrent();`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/Policy.java

### Unused Code (2)
- Line 12: `import java.util.List;`
- Line 13: `import java.util.Objects;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyManager.java

### Null Pointer (1)
- Line 312: `return StackWalker.getInstance()`

### Concurrency Issue (1)
- Line 142: `public static final String ALL_UNNAMED = "ALL-UNNAMED";`

### Unused Code (46)
- Line 12: `import org.elasticsearch.core.PathUtils;`
- Line 13: `import org.elasticsearch.core.Strings;`
- Line 14: `import org.elasticsearch.core.SuppressForbidden;`
- Line 15: `import org.elasticsearch.entitlement.instrumentation.InstrumentationService;`
- Line 16: `import org.elasticsearch.entitlement.runtime.api.NotEntitledException;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.FileAccessTree.ExclusiveFileEntitlement;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.FileAccessTree.ExclusivePath;`
- Line 19: `import org.elasticsearch.entitlement.runtime.policy.entitlements.CreateClassLoaderEntitlement;`
- Line 20: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 21: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ExitVMEntitlement;`
- Line 22: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 23: `import org.elasticsearch.entitlement.runtime.policy.entitlements.InboundNetworkEntitlement;`
- Line 24: `import org.elasticsearch.entitlement.runtime.policy.entitlements.LoadNativeLibrariesEntitlement;`
- Line 25: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ManageThreadsEntitlement;`
- Line 26: `import org.elasticsearch.entitlement.runtime.policy.entitlements.OutboundNetworkEntitlement;`
- Line 27: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ReadStoreAttributesEntitlement;`
- Line 28: `import org.elasticsearch.entitlement.runtime.policy.entitlements.SetHttpsConnectionPropertiesEntitlement;`
- Line 29: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 30: `import org.elasticsearch.logging.LogManager;`
- Line 31: `import org.elasticsearch.logging.Logger;`
- Line 33: `import java.io.File;`
- Line 34: `import java.io.IOException;`
- Line 35: `import java.lang.StackWalker.StackFrame;`
- Line 36: `import java.lang.module.ModuleFinder;`
- Line 37: `import java.lang.module.ModuleReference;`
- Line 38: `import java.nio.file.NoSuchFileException;`
- Line 39: `import java.nio.file.Path;`
- Line 40: `import java.nio.file.Paths;`
- Line 41: `import java.util.ArrayList;`
- Line 42: `import java.util.HashSet;`
- Line 43: `import java.util.List;`
- Line 44: `import java.util.Map;`
- Line 45: `import java.util.Optional;`
- Line 46: `import java.util.Set;`
- Line 47: `import java.util.concurrent.ConcurrentHashMap;`
- Line 48: `import java.util.function.Function;`
- Line 49: `import java.util.function.Supplier;`
- Line 50: `import java.util.stream.Collectors;`
- Line 51: `import java.util.stream.Stream;`
- Line 53: `import static java.lang.StackWalker.Option.RETAIN_CLASS_REFERENCE;`
- Line 54: `import static java.util.Objects.requireNonNull;`
- Line 55: `import static java.util.function.Predicate.not;`
- Line 56: `import static java.util.stream.Collectors.groupingBy;`
- Line 57: `import static java.util.stream.Collectors.toUnmodifiableMap;`
- Line 58: `import static java.util.zip.ZipFile.OPEN_DELETE;`
- Line 59: `import static java.util.zip.ZipFile.OPEN_READ;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParser.java

### Exception Handling (6)
- Line 73: `throw new IllegalArgumentException(`
- Line 126: `throw new UncheckedIOException(ioe);`
- Line 150: `throw new UncheckedIOException(ioe);`
- Line 170: `throw new UncheckedIOException(ioe);`
- Line 201: `throw new UncheckedIOException(ioe);`
- Line 309: `throw new IllegalStateException("internal error", e);`

### Unused Code (33)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.entitlements.CreateClassLoaderEntitlement;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.entitlements.InboundNetworkEntitlement;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.entitlements.LoadNativeLibrariesEntitlement;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ManageThreadsEntitlement;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.entitlements.OutboundNetworkEntitlement;`
- Line 19: `import org.elasticsearch.entitlement.runtime.policy.entitlements.SetHttpsConnectionPropertiesEntitlement;`
- Line 20: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteAllSystemPropertiesEntitlement;`
- Line 21: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 22: `import org.elasticsearch.xcontent.XContentLocation;`
- Line 23: `import org.elasticsearch.xcontent.XContentParser;`
- Line 24: `import org.elasticsearch.xcontent.XContentParserConfiguration;`
- Line 25: `import org.elasticsearch.xcontent.yaml.YamlXContent;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.InputStream;`
- Line 29: `import java.io.UncheckedIOException;`
- Line 30: `import java.lang.reflect.Constructor;`
- Line 31: `import java.lang.reflect.InvocationTargetException;`
- Line 32: `import java.lang.reflect.Method;`
- Line 33: `import java.lang.reflect.Modifier;`
- Line 34: `import java.util.ArrayList;`
- Line 35: `import java.util.Arrays;`
- Line 36: `import java.util.HashSet;`
- Line 37: `import java.util.List;`
- Line 38: `import java.util.Locale;`
- Line 39: `import java.util.Map;`
- Line 40: `import java.util.Objects;`
- Line 41: `import java.util.Set;`
- Line 42: `import java.util.function.Function;`
- Line 43: `import java.util.function.Predicate;`
- Line 44: `import java.util.stream.Collectors;`
- Line 45: `import java.util.stream.Stream;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserException.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.xcontent.XContentLocation;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/PolicyUtils.java

### Concurrency Issue (2)
- Line 42: `private static final Logger logger = LogManager.getLogger(PolicyUtils.class);`
- Line 50: `private static final String POLICY_FILE_NAME = "entitlement-policy.yaml";`

### Unused Code (25)
- Line 12: `import org.elasticsearch.core.Strings;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 16: `import org.elasticsearch.logging.LogManager;`
- Line 17: `import org.elasticsearch.logging.Logger;`
- Line 19: `import java.io.ByteArrayInputStream;`
- Line 20: `import java.io.IOException;`
- Line 21: `import java.lang.module.ModuleFinder;`
- Line 22: `import java.lang.module.ModuleReference;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.nio.file.StandardOpenOption;`
- Line 26: `import java.util.ArrayList;`
- Line 27: `import java.util.Base64;`
- Line 28: `import java.util.Collection;`
- Line 29: `import java.util.HashMap;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Map;`
- Line 32: `import java.util.Set;`
- Line 33: `import java.util.function.Function;`
- Line 34: `import java.util.stream.Collectors;`
- Line 35: `import java.util.stream.Stream;`
- Line 37: `import static java.util.Objects.requireNonNull;`
- Line 38: `import static org.elasticsearch.entitlement.runtime.policy.PolicyManager.ALL_UNNAMED;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/Scope.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 14: `import java.util.List;`
- Line 15: `import java.util.Objects;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/VersionedPolicy.java

### Unused Code (1)
- Line 12: `import java.util.Set;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/CreateClassLoaderEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/Entitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.Policy;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/FilesEntitlement.java

### Concurrency Issue (1)
- Line 33: `public static final FilesEntitlement EMPTY = new FilesEntitlement(List.of());`

### Exception Handling (13)
- Line 93: `throw new IllegalArgumentException();`
- Line 187: `throw new PolicyValidationException("invalid mode: " + mode + ", valid values: [read, read_write]");`
- Line 199: `throw new PolicyValidationException("invalid platform: " + platform + ", valid values: [linux, macos, windows]");`
- Line 209: `default -> throw new PolicyValidationException(`
- Line 219: `throw new PolicyValidationException("must specify at least one path");`
- Line 273: `throw new PolicyValidationException(`
- Line 279: `throw new PolicyValidationException("files entitlement must contain 'mode' for every listed file");`
- Line 288: `throw new PolicyValidationException("'relative_to' may only be used with 'relative_path'");`
- Line 292: `throw new PolicyValidationException("'basedir_if_relative' may only be used with 'path_setting'");`
- Line 298: `throw new PolicyValidationException("files entitlement with a 'relative_path' must specify 'relative_to'");`
- Line 303: `throw new PolicyValidationException("'relative_path' [" + relativePathAsString + "] must be relative");`
- Line 309: `throw new PolicyValidationException("'path' [" + pathAsString + "] must be absolute");`
- Line 314: `throw new PolicyValidationException("files entitlement with a 'path_setting' must specify 'basedir_if_relative'");`

### Unused Code (14)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.FileUtils;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.PathLookup;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.Platform;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.PolicyValidationException;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.util.ArrayList;`
- Line 20: `import java.util.HashMap;`
- Line 21: `import java.util.List;`
- Line 22: `import java.util.Locale;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.Objects;`
- Line 25: `import java.util.function.BiFunction;`
- Line 26: `import java.util.stream.Stream;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/InboundNetworkEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/LoadNativeLibrariesEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/ManageThreadsEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/OutboundNetworkEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/SetHttpsConnectionPropertiesEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/WriteAllSystemPropertiesEntitlement.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`

## ../libs/entitlement/src/main/java/org/elasticsearch/entitlement/runtime/policy/entitlements/WriteSystemPropertiesEntitlement.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.ExternalEntitlement;`
- Line 14: `import java.util.List;`
- Line 15: `import java.util.Set;`

## ../libs/entitlement/src/main23/java/org/elasticsearch/entitlement/runtime/api/Java23ElasticsearchEntitlementChecker.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.entitlement.bridge.Java23EntitlementChecker;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.PolicyManager;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/FileAccessTreeTests.java

### Concurrency Issue (1)
- Line 56: `private static final PathLookup TEST_PATH_LOOKUP = new PathLookup(`

### Unused Code (25)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.FileAccessTree.ExclusiveFileEntitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.FileAccessTree.ExclusivePath;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.FileData;`
- Line 18: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import org.junit.BeforeClass;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.Path;`
- Line 24: `import java.nio.file.Paths;`
- Line 25: `import java.util.ArrayList;`
- Line 26: `import java.util.HashMap;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Map;`
- Line 29: `import java.util.Set;`
- Line 31: `import static org.elasticsearch.core.PathUtils.getDefaultFileSystem;`
- Line 32: `import static org.elasticsearch.entitlement.runtime.policy.FileAccessTree.buildExclusivePathList;`
- Line 33: `import static org.elasticsearch.entitlement.runtime.policy.FileAccessTree.normalizePath;`
- Line 34: `import static org.elasticsearch.entitlement.runtime.policy.Platform.WINDOWS;`
- Line 35: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ;`
- Line 36: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ_WRITE;`
- Line 37: `import static org.hamcrest.Matchers.equalTo;`
- Line 38: `import static org.hamcrest.Matchers.is;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/FileUtilsTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.core.PathUtils;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import static org.elasticsearch.entitlement.runtime.policy.FileUtils.PATH_ORDER;`
- Line 16: `import static org.elasticsearch.entitlement.runtime.policy.FileUtils.isAbsolutePath;`
- Line 17: `import static org.hamcrest.Matchers.greaterThan;`
- Line 18: `import static org.hamcrest.Matchers.is;`
- Line 19: `import static org.hamcrest.Matchers.lessThan;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyManagerTests.java

### Exception Handling (7)
- Line 81: `throw new IllegalStateException(e);`
- Line 682: `throw new UnsupportedOperationException();`
- Line 692: `throw new UnsupportedOperationException();`
- Line 697: `throw new UnsupportedOperationException();`
- Line 702: `throw new UnsupportedOperationException();`
- Line 707: `throw new UnsupportedOperationException();`
- Line 712: `throw new UnsupportedOperationException();`

### Unused Code (32)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.core.Strings;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.PolicyManager.ModuleEntitlements;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.agent.TestAgent;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.agent.inner.TestInnerAgent;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.entitlements.CreateClassLoaderEntitlement;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ExitVMEntitlement;`
- Line 19: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 20: `import org.elasticsearch.test.ESTestCase;`
- Line 21: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 22: `import org.elasticsearch.test.jar.JarUtils;`
- Line 23: `import org.junit.BeforeClass;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.lang.StackWalker.StackFrame;`
- Line 27: `import java.lang.module.Configuration;`
- Line 28: `import java.lang.module.ModuleFinder;`
- Line 29: `import java.net.URL;`
- Line 30: `import java.net.URLClassLoader;`
- Line 31: `import java.nio.file.Path;`
- Line 32: `import java.util.Arrays;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Map;`
- Line 35: `import java.util.Set;`
- Line 36: `import java.util.stream.Stream;`
- Line 38: `import static java.util.Map.entry;`
- Line 39: `import static org.elasticsearch.entitlement.runtime.policy.PolicyManager.ALL_UNNAMED;`
- Line 40: `import static org.elasticsearch.entitlement.runtime.policy.PolicyManager.SERVER_COMPONENT_NAME;`
- Line 41: `import static org.hamcrest.Matchers.aMapWithSize;`
- Line 42: `import static org.hamcrest.Matchers.allOf;`
- Line 43: `import static org.hamcrest.Matchers.containsString;`
- Line 44: `import static org.hamcrest.Matchers.is;`
- Line 45: `import static org.hamcrest.Matchers.sameInstance;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserFailureTests.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.io.ByteArrayInputStream;`
- Line 15: `import java.nio.charset.StandardCharsets;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyParserTests.java

### Unused Code (21)
- Line 12: `import org.elasticsearch.core.Strings;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.entitlements.CreateClassLoaderEntitlement;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.entitlements.InboundNetworkEntitlement;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.entitlements.LoadNativeLibrariesEntitlement;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.entitlements.OutboundNetworkEntitlement;`
- Line 19: `import org.elasticsearch.entitlement.runtime.policy.entitlements.SetHttpsConnectionPropertiesEntitlement;`
- Line 20: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 21: `import org.elasticsearch.test.ESTestCase;`
- Line 22: `import org.junit.BeforeClass;`
- Line 24: `import java.io.ByteArrayInputStream;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.InputStream;`
- Line 27: `import java.nio.charset.StandardCharsets;`
- Line 28: `import java.nio.file.Path;`
- Line 29: `import java.util.List;`
- Line 30: `import java.util.Map;`
- Line 31: `import java.util.Set;`
- Line 33: `import static org.hamcrest.Matchers.contains;`
- Line 34: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/PolicyUtilsTests.java

### Unused Code (22)
- Line 12: `import org.elasticsearch.entitlement.runtime.policy.entitlements.Entitlement;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.entitlements.InboundNetworkEntitlement;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.entitlements.LoadNativeLibrariesEntitlement;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.entitlements.ManageThreadsEntitlement;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.entitlements.OutboundNetworkEntitlement;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.entitlements.SetHttpsConnectionPropertiesEntitlement;`
- Line 19: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteAllSystemPropertiesEntitlement;`
- Line 20: `import org.elasticsearch.entitlement.runtime.policy.entitlements.WriteSystemPropertiesEntitlement;`
- Line 21: `import org.elasticsearch.test.ESTestCase;`
- Line 23: `import java.nio.charset.StandardCharsets;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.Base64;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.Set;`
- Line 29: `import static org.elasticsearch.entitlement.runtime.policy.PolicyUtils.mergeEntitlement;`
- Line 30: `import static org.elasticsearch.entitlement.runtime.policy.PolicyUtils.mergeEntitlements;`
- Line 31: `import static org.elasticsearch.test.LambdaMatchers.transformedMatch;`
- Line 32: `import static org.hamcrest.Matchers.both;`
- Line 33: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 34: `import static org.hamcrest.Matchers.equalTo;`
- Line 35: `import static org.hamcrest.Matchers.nullValue;`

## ../libs/entitlement/src/test/java/org/elasticsearch/entitlement/runtime/policy/entitlements/FilesEntitlementTests.java

### Concurrency Issue (1)
- Line 45: `private static final PathLookup TEST_PATH_LOOKUP = new PathLookup(`

### Unused Code (21)
- Line 12: `import org.elasticsearch.common.settings.Settings;`
- Line 13: `import org.elasticsearch.entitlement.runtime.policy.PathLookup;`
- Line 14: `import org.elasticsearch.entitlement.runtime.policy.Policy;`
- Line 15: `import org.elasticsearch.entitlement.runtime.policy.PolicyParser;`
- Line 16: `import org.elasticsearch.entitlement.runtime.policy.PolicyValidationException;`
- Line 17: `import org.elasticsearch.entitlement.runtime.policy.Scope;`
- Line 18: `import org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.FileData;`
- Line 19: `import org.elasticsearch.test.ESTestCase;`
- Line 20: `import org.junit.BeforeClass;`
- Line 22: `import java.io.ByteArrayInputStream;`
- Line 23: `import java.nio.charset.StandardCharsets;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Map;`
- Line 28: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.BaseDir.CONFIG;`
- Line 29: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ;`
- Line 30: `import static org.elasticsearch.entitlement.runtime.policy.entitlements.FilesEntitlement.Mode.READ_WRITE;`
- Line 31: `import static org.hamcrest.Matchers.contains;`
- Line 32: `import static org.hamcrest.Matchers.containsInAnyOrder;`
- Line 33: `import static org.hamcrest.Matchers.empty;`
- Line 34: `import static org.hamcrest.Matchers.is;`

## ../libs/entitlement/tools/common/src/main/java/org/elasticsearch/entitlement/tools/ExternalAccess.java

### Concurrency Issue (1)
- Line 21: `private static final String DELIMITER = ":";`

### Exception Handling (1)
- Line 34: `throw new IllegalArgumentException();`

### Unused Code (3)
- Line 12: `import java.util.Arrays;`
- Line 13: `import java.util.EnumSet;`
- Line 14: `import java.util.stream.Collectors;`

## ../libs/entitlement/tools/common/src/main/java/org/elasticsearch/entitlement/tools/Utils.java

### Exception Handling (1)
- Line 50: `throw new RuntimeException(e);`

### Unused Code (12)
- Line 12: `import java.io.IOException;`
- Line 13: `import java.lang.module.ModuleDescriptor;`
- Line 14: `import java.net.URI;`
- Line 15: `import java.nio.file.FileSystem;`
- Line 16: `import java.nio.file.FileSystems;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.util.HashMap;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.Set;`
- Line 23: `import java.util.stream.Collectors;`

## ../libs/entitlement/tools/public-callers-finder/src/main/java/org/elasticsearch/entitlement/tools/publiccallersfinder/FindUsagesClassVisitor.java

### Concurrency Issue (3)
- Line 62: `public void visit(int version, int access, String name, String signature, String superName, String[] interfaces) {`
- Line 88: `public void visitSource(String source, String debug) {`
- Line 136: `public void visitLineNumber(int line, Label start) {`

### Exception Handling (1)
- Line 81: `} catch (ClassNotFoundException ignored) {}`

### Unused Code (17)
- Line 29: `private int classAccess;`
- Line 30: `private boolean accessibleViaInterfaces;`
- Line 51: `private String className;`
- Line 52: `private String source;`
- Line 105: `private int line;`
- Line 12: `import org.elasticsearch.entitlement.tools.ExternalAccess;`
- Line 13: `import org.objectweb.asm.ClassVisitor;`
- Line 14: `import org.objectweb.asm.Label;`
- Line 15: `import org.objectweb.asm.MethodVisitor;`
- Line 16: `import org.objectweb.asm.Type;`
- Line 18: `import java.lang.constant.ClassDesc;`
- Line 19: `import java.lang.reflect.AccessFlag;`
- Line 20: `import java.util.EnumSet;`
- Line 21: `import java.util.Set;`
- Line 23: `import static org.objectweb.asm.Opcodes.ACC_PROTECTED;`
- Line 24: `import static org.objectweb.asm.Opcodes.ACC_PUBLIC;`
- Line 25: `import static org.objectweb.asm.Opcodes.ASM9;`

## ../libs/entitlement/tools/public-callers-finder/src/main/java/org/elasticsearch/entitlement/tools/publiccallersfinder/Main.java

### Exception Handling (2)
- Line 86: `throw new RuntimeException(e);`
- Line 129: `throw new RuntimeException(e);`

### Unused Code (14)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.tools.ExternalAccess;`
- Line 14: `import org.elasticsearch.entitlement.tools.Utils;`
- Line 15: `import org.objectweb.asm.ClassReader;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.nio.file.Path;`
- Line 20: `import java.util.ArrayDeque;`
- Line 21: `import java.util.ArrayList;`
- Line 22: `import java.util.Collection;`
- Line 23: `import java.util.EnumSet;`
- Line 24: `import java.util.HashSet;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Set;`

## ../libs/entitlement/tools/securitymanager-scanner/src/main/java/org/elasticsearch/entitlement/tools/securitymanager/scanner/Main.java

### Concurrency Issue (1)
- Line 55: `private static final String SEPARATOR = "\t";`

### Exception Handling (1)
- Line 38: `throw new RuntimeException(e);`

### Unused Code (8)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.tools.ExternalAccess;`
- Line 14: `import org.elasticsearch.entitlement.tools.Utils;`
- Line 15: `import org.objectweb.asm.ClassReader;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.nio.file.Files;`
- Line 19: `import java.util.HashMap;`
- Line 20: `import java.util.List;`

## ../libs/entitlement/tools/securitymanager-scanner/src/main/java/org/elasticsearch/entitlement/tools/securitymanager/scanner/SecurityCheckClassVisitor.java

### Concurrency Issue (7)
- Line 73: `public void visit(int version, int access, String name, String signature, String superName, String[] interfaces) {`
- Line 80: `public void visitSource(String source, String debug) {`
- Line 93: `public void setCurrentModule(String moduleName, Set<String> moduleExports) {`
- Line 98: `public void setCurrentSourcePath(String path) {`
- Line 191: `public void visitLdcInsn(Object value) {`
- Line 199: `public void visitMethodInsn(int opcode, String owner, String name, String descriptor, boolean isInterface) {`
- Line 263: `public void visitLineNumber(int line, Label start) {`

### Unused Code (35)
- Line 60: `private String className;`
- Line 61: `private int classAccess;`
- Line 62: `private String source;`
- Line 63: `private String moduleName;`
- Line 64: `private String sourcePath;`
- Line 106: `private int line;`
- Line 107: `private String permissionType;`
- Line 108: `private String runtimePermissionType;`
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.entitlement.tools.ExternalAccess;`
- Line 14: `import org.objectweb.asm.ClassVisitor;`
- Line 15: `import org.objectweb.asm.Label;`
- Line 16: `import org.objectweb.asm.MethodVisitor;`
- Line 17: `import org.objectweb.asm.Type;`
- Line 19: `import java.lang.constant.ClassDesc;`
- Line 20: `import java.lang.reflect.InaccessibleObjectException;`
- Line 21: `import java.lang.reflect.Modifier;`
- Line 22: `import java.nio.file.Path;`
- Line 23: `import java.security.Permission;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.EnumSet;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Map;`
- Line 29: `import java.util.Set;`
- Line 31: `import static org.objectweb.asm.Opcodes.ACC_PROTECTED;`
- Line 32: `import static org.objectweb.asm.Opcodes.ACC_PUBLIC;`
- Line 33: `import static org.objectweb.asm.Opcodes.ASM9;`
- Line 34: `import static org.objectweb.asm.Opcodes.GETSTATIC;`
- Line 35: `import static org.objectweb.asm.Opcodes.INVOKEDYNAMIC;`
- Line 36: `import static org.objectweb.asm.Opcodes.INVOKEINTERFACE;`
- Line 37: `import static org.objectweb.asm.Opcodes.INVOKESPECIAL;`
- Line 38: `import static org.objectweb.asm.Opcodes.INVOKESTATIC;`
- Line 39: `import static org.objectweb.asm.Opcodes.INVOKEVIRTUAL;`
- Line 40: `import static org.objectweb.asm.Opcodes.NEW;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/Circle.java

### Concurrency Issue (1)
- Line 19: `public static final Circle EMPTY = new Circle();`

### Exception Handling (1)
- Line 42: `throw new IllegalArgumentException("Circle radius [" + radiusMeters + "] cannot be negative");`

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.utils.WellKnownText;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/GeometryCollection.java

### Exception Handling (2)
- Line 34: `throw new IllegalArgumentException("the list of shapes cannot be null or empty");`
- Line 39: `throw new IllegalArgumentException("all elements of the collection should have the same number of dimension");`

### Unused Code (6)
- Line 26: `private boolean hasAlt;`
- Line 11: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 13: `import java.util.Collections;`
- Line 14: `import java.util.Iterator;`
- Line 15: `import java.util.List;`
- Line 16: `import java.util.Objects;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/GeometryVisitor.java

### Exception Handling (1)
- Line 28: `*   throw new IllegalArgumentException("Unknown object " + obj);`

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.utils.WellKnownText;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/Line.java

### Concurrency Issue (1)
- Line 20: `public static final Line EMPTY = new Line();`

### Exception Handling (5)
- Line 40: `throw new IllegalArgumentException("y must not be null");`
- Line 43: `throw new IllegalArgumentException("x must not be null");`
- Line 46: `throw new IllegalArgumentException("x and y must be equal length");`
- Line 49: `throw new IllegalArgumentException("at least two points in the line is required");`
- Line 52: `throw new IllegalArgumentException("z and x must be equal length");`

### Unused Code (2)
- Line 12: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 14: `import java.util.Arrays;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/LinearRing.java

### Concurrency Issue (1)
- Line 20: `public static final LinearRing EMPTY = new LinearRing();`

### Exception Handling (1)
- Line 31: `throw new IllegalArgumentException("linear ring cannot contain less than 2 points, found " + x.length);`

### Unused Code (1)
- Line 12: `import java.util.Arrays;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/MultiLine.java

### Concurrency Issue (1)
- Line 18: `public static final MultiLine EMPTY = new MultiLine();`

### Unused Code (1)
- Line 12: `import java.util.List;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/MultiPoint.java

### Concurrency Issue (1)
- Line 18: `public static final MultiPoint EMPTY = new MultiPoint();`

### Unused Code (1)
- Line 12: `import java.util.List;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/MultiPolygon.java

### Concurrency Issue (1)
- Line 18: `public static final MultiPolygon EMPTY = new MultiPolygon();`

### Unused Code (1)
- Line 12: `import java.util.List;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/Point.java

### Concurrency Issue (1)
- Line 18: `public static final Point EMPTY = new Point();`

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.utils.WellKnownText;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/Polygon.java

### Concurrency Issue (1)
- Line 20: `public static final Polygon EMPTY = new Polygon();`

### Exception Handling (3)
- Line 38: `throw new IllegalArgumentException("holes must not be null");`
- Line 44: `throw new IllegalArgumentException("holes must have the same number of dimensions as the polygon");`
- Line 64: `throw new IllegalArgumentException("at least 4 polygon points required");`

### Unused Code (3)
- Line 12: `import java.util.Collections;`
- Line 13: `import java.util.List;`
- Line 14: `import java.util.Objects;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/Rectangle.java

### Exception Handling (2)
- Line 75: `throw new IllegalArgumentException("max y cannot be less than min y");`
- Line 78: `throw new IllegalArgumentException("only one z value is specified");`

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.utils.WellKnownText;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/ShapeType.java

### Unused Code (1)
- Line 12: `import java.util.Locale;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/simplify/GeometrySimplifier.java

### Unused Code (13)
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.Line;`
- Line 16: `import org.elasticsearch.geometry.LinearRing;`
- Line 17: `import org.elasticsearch.geometry.MultiPoint;`
- Line 18: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 19: `import org.elasticsearch.geometry.Point;`
- Line 20: `import org.elasticsearch.geometry.Polygon;`
- Line 21: `import org.elasticsearch.geometry.Rectangle;`
- Line 23: `import java.util.ArrayList;`
- Line 24: `import java.util.Arrays;`
- Line 25: `import java.util.List;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/simplify/SimplificationErrorCalculator.java

### Exception Handling (1)
- Line 41: `default -> throw new IllegalArgumentException("Unknown simplification error calculator: " + calculatorName);`

### Unused Code (5)
- Line 12: `import java.util.Locale;`
- Line 14: `import static java.lang.Math.acos;`
- Line 15: `import static java.lang.Math.min;`
- Line 16: `import static org.elasticsearch.geometry.simplify.SimplificationErrorCalculator.Point3D.sin;`
- Line 17: `import static org.elasticsearch.geometry.simplify.SloppyMath.cos;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/simplify/SloppyMath.java

### Concurrency Issue (26)
- Line 156: `private static final double ONE_DIV_F2 = 1 / 2.0;`
- Line 157: `private static final double ONE_DIV_F3 = 1 / 6.0;`
- Line 158: `private static final double ONE_DIV_F4 = 1 / 24.0;`
- Line 161: `private static final double PIO2_HI = Double.longBitsToDouble(0x3FF921FB54400000L);`
- Line 163: `private static final double PIO2_LO = Double.longBitsToDouble(0x3DD0B4611A626331L);`
- Line 164: `private static final double TWOPI_HI = 4 * PIO2_HI;`
- Line 165: `private static final double TWOPI_LO = 4 * PIO2_LO;`
- Line 166: `private static final int SIN_COS_TABS_SIZE = (1 << 11) + 1;`
- Line 167: `private static final double SIN_COS_DELTA_HI = TWOPI_HI / (SIN_COS_TABS_SIZE - 1);`
- Line 168: `private static final double SIN_COS_DELTA_LO = TWOPI_LO / (SIN_COS_TABS_SIZE - 1);`
- Line 169: `private static final double SIN_COS_INDEXER = 1 / (SIN_COS_DELTA_HI + SIN_COS_DELTA_LO);`
- Line 182: `private static final double ASIN_MAX_VALUE_FOR_TABS = StrictMath.sin(Math.toRadians(73.0));`
- Line 184: `private static final int ASIN_TABS_SIZE = (1 << 13) + 1;`
- Line 185: `private static final double ASIN_DELTA = ASIN_MAX_VALUE_FOR_TABS / (ASIN_TABS_SIZE - 1);`
- Line 186: `private static final double ASIN_INDEXER = 1 / ASIN_DELTA;`
- Line 194: `private static final double ASIN_PIO2_HI = Double.longBitsToDouble(0x3FF921FB54442D18L);`
- Line 196: `private static final double ASIN_PIO2_LO = Double.longBitsToDouble(0x3C91A62633145C07L);`
- Line 198: `private static final double ASIN_PS0 = Double.longBitsToDouble(0x3fc5555555555555L);`
- Line 200: `private static final double ASIN_PS1 = Double.longBitsToDouble(0xbfd4d61203eb6f7dL);`
- Line 202: `private static final double ASIN_PS2 = Double.longBitsToDouble(0x3fc9c1550e884455L);`
- Line 204: `private static final double ASIN_PS3 = Double.longBitsToDouble(0xbfa48228b5688f3bL);`
- Line 206: `private static final double ASIN_PS4 = Double.longBitsToDouble(0x3f49efe07501b288L);`
- Line 208: `private static final double ASIN_PS5 = Double.longBitsToDouble(0x3f023de10dfdf709L);`
- Line 210: `private static final double ASIN_QS1 = Double.longBitsToDouble(0xc0033a271c8a2d4bL);`
- Line 212: `private static final double ASIN_QS2 = Double.longBitsToDouble(0x40002ae59c598ac8L);`
- Line 214: `private static final double ASIN_QS3 = Double.longBitsToDouble(0xbfe6066c1b8d0159L);`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/simplify/StreamingGeometrySimplifier.java

### Concurrency Issue (6)
- Line 64: `public void reset() {`
- Line 144: `private void removeAndAdd(int toRemove, PointError pointError) {`
- Line 42: `protected int objCount = 0;`
- Line 44: `protected PointConstructor pointConstructor = new PointConstructor() {`
- Line 46: `protected PointResetter pointResetter = new PointResetter() {`
- Line 187: `private double y;`

### Exception Handling (4)
- Line 297: `throw new IllegalArgumentException("No points have been consumed");`
- Line 350: `throw new IllegalArgumentException("No points have been consumed");`
- Line 353: `throw new IllegalArgumentException("LinearRing cannot have less than 4 points");`
- Line 363: `throw new IllegalArgumentException("LinearRing cannot have first and last points differ: " + inequality);`

### Unused Code (11)
- Line 185: `private int index;`
- Line 186: `private double x;`
- Line 187: `private double y;`
- Line 12: `import org.elasticsearch.geometry.Geometry;`
- Line 13: `import org.elasticsearch.geometry.Line;`
- Line 14: `import org.elasticsearch.geometry.LinearRing;`
- Line 15: `import org.elasticsearch.geometry.Polygon;`
- Line 17: `import java.util.ArrayList;`
- Line 18: `import java.util.Arrays;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.PriorityQueue;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/CircleUtils.java

### Concurrency Issue (1)
- Line 21: `static final int CIRCLE_TO_POLYGON_MAXIMUM_NUMBER_OF_SIDES = 1000;`

### Unused Code (3)
- Line 11: `import org.elasticsearch.geometry.Circle;`
- Line 12: `import org.elasticsearch.geometry.LinearRing;`
- Line 13: `import org.elasticsearch.geometry.Polygon;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/GeographyValidator.java

### Concurrency Issue (2)
- Line 31: `private static final GeometryValidator TRUE = new GeographyValidator(true);`
- Line 52: `private static final double MAX_LAT_INCL = 90.0D;`

### Exception Handling (3)
- Line 69: `throw new IllegalArgumentException(`
- Line 80: `throw new IllegalArgumentException(`
- Line 88: `throw new IllegalArgumentException("found Z value [" + zValue + "] but [ignore_z_value] parameter is [" + ignoreZValue + "]");`

### Unused Code (12)
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.GeometryVisitor;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/Geohash.java

### Concurrency Issue (6)
- Line 66: `private static final short BITS = 32;`
- Line 67: `private static final double LAT_SCALE = (0x1L << (BITS - 1)) / 180.0D;`
- Line 68: `private static final double LAT_DECODE = 180.0D / (0x1L << BITS);`
- Line 69: `private static final double LON_SCALE = (0x1L << (BITS - 1)) / 360.0D;`
- Line 70: `private static final double LON_DECODE = 360.0D / (0x1L << BITS);`
- Line 74: `private static final long MAX_LAT_BITS = (0x1L << (PRECISION * 5 / 2)) - 1;`

### Exception Handling (2)
- Line 324: `throw new IllegalArgumentException("empty geohash");`
- Line 332: `throw new IllegalArgumentException("unsupported symbol [" + c + "] in geohash [" + hash + "]");`

### Unused Code (4)
- Line 11: `import org.elasticsearch.geometry.Point;`
- Line 12: `import org.elasticsearch.geometry.Rectangle;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.Collection;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/GeometryValidator.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Geometry;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/SpatialEnvelopeVisitor.java

### Concurrency Issue (11)
- Line 245: `public void visitRectangle(double minX, double maxX, double maxY, double minY) {`
- Line 129: `private double minX = Double.POSITIVE_INFINITY;`
- Line 130: `private double maxX = Double.NEGATIVE_INFINITY;`
- Line 131: `private double maxY = Double.NEGATIVE_INFINITY;`
- Line 132: `private double minY = Double.POSITIVE_INFINITY;`
- Line 200: `protected double top = Double.NEGATIVE_INFINITY;`
- Line 201: `protected double bottom = Double.POSITIVE_INFINITY;`
- Line 202: `protected double negLeft = Double.POSITIVE_INFINITY;`
- Line 203: `protected double negRight = Double.NEGATIVE_INFINITY;`
- Line 204: `protected double posLeft = Double.POSITIVE_INFINITY;`
- Line 205: `protected double posRight = Double.NEGATIVE_INFINITY;`

### Exception Handling (1)
- Line 321: `throw new UnsupportedOperationException("Circle is not supported");`

### Unused Code (18)
- Line 129: `private double minX = Double.POSITIVE_INFINITY;`
- Line 130: `private double maxX = Double.NEGATIVE_INFINITY;`
- Line 131: `private double maxY = Double.NEGATIVE_INFINITY;`
- Line 132: `private double minY = Double.POSITIVE_INFINITY;`
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.GeometryVisitor;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`
- Line 25: `import java.util.Locale;`
- Line 26: `import java.util.Optional;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/StandardValidator.java

### Concurrency Issue (2)
- Line 30: `private static final GeometryValidator TRUE = new StandardValidator(true);`
- Line 31: `private static final GeometryValidator FALSE = new StandardValidator(false);`

### Exception Handling (1)
- Line 45: `throw new IllegalArgumentException("found Z value [" + zValue + "] but [ignore_z_value] parameter is [" + ignoreZValue + "]");`

### Unused Code (12)
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.GeometryVisitor;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/WellKnownBinary.java

### Exception Handling (3)
- Line 51: `throw new UncheckedIOException(ioe);`
- Line 176: `throw new IllegalArgumentException("Linear ring is not supported by WKB");`
- Line 239: `default -> throw new IllegalArgumentException("Unknown geometry type: " + type);`

### Unused Code (21)
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.GeometryVisitor;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`
- Line 24: `import org.elasticsearch.geometry.ShapeType;`
- Line 26: `import java.io.ByteArrayOutputStream;`
- Line 27: `import java.io.IOException;`
- Line 28: `import java.io.UncheckedIOException;`
- Line 29: `import java.nio.ByteBuffer;`
- Line 30: `import java.nio.ByteOrder;`
- Line 31: `import java.util.ArrayList;`
- Line 32: `import java.util.Collections;`
- Line 33: `import java.util.List;`

## ../libs/geo/src/main/java/org/elasticsearch/geometry/utils/WellKnownText.java

### Concurrency Issue (10)
- Line 41: `public static final String EMPTY = "EMPTY";`
- Line 42: `public static final String SPACE = " ";`
- Line 43: `public static final String LPAREN = "(";`
- Line 44: `public static final String RPAREN = ")";`
- Line 45: `public static final String COMMA = ",";`
- Line 46: `public static final String NAN = "NaN";`
- Line 47: `public static final int MAX_NESTED_DEPTH = 1000;`
- Line 49: `private static final String NUMBER = "<NUMBER>";`
- Line 50: `private static final String EOF = "END-OF-STREAM";`
- Line 51: `private static final String EOL = "END-OF-LINE";`

### Exception Handling (4)
- Line 113: `throw new IllegalArgumentException("Linear ring is not supported by WKT");`
- Line 251: `default -> throw new IllegalArgumentException("Unknown geometry type: " + type);`
- Line 454: `default -> throw new IllegalArgumentException("Unknown geometry type: " + type);`
- Line 769: `throw new UnsupportedOperationException("line ring cannot be serialized using WKT");`

### Unused Code (22)
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.GeometryVisitor;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`
- Line 25: `import java.io.IOException;`
- Line 26: `import java.io.StreamTokenizer;`
- Line 27: `import java.io.StringReader;`
- Line 28: `import java.nio.ByteBuffer;`
- Line 29: `import java.nio.ByteOrder;`
- Line 30: `import java.text.ParseException;`
- Line 31: `import java.util.ArrayList;`
- Line 32: `import java.util.Collections;`
- Line 33: `import java.util.List;`
- Line 34: `import java.util.Locale;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/BaseGeometryTestCase.java

### Exception Handling (1)
- Line 41: `throw new ElasticsearchException(e);`

### Unused Code (8)
- Line 12: `import org.elasticsearch.ElasticsearchException;`
- Line 13: `import org.elasticsearch.TransportVersion;`
- Line 14: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 16: `import org.elasticsearch.test.AbstractWireTestCase;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.concurrent.atomic.AtomicBoolean;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/CircleTests.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 13: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 17: `import java.io.IOException;`
- Line 18: `import java.text.ParseException;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/GeometryCollectionTests.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.Arrays;`
- Line 21: `import java.util.Collections;`
- Line 23: `import static org.hamcrest.Matchers.containsString;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/GeometryValidatorTests.java

### Concurrency Issue (1)
- Line 56: `private static final double MAX_ALT_INCL = 1D;`

### Exception Handling (3)
- Line 65: `throw new IllegalArgumentException(`
- Line 74: `throw new IllegalArgumentException(`
- Line 83: `throw new IllegalArgumentException(`

### Unused Code (4)
- Line 12: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 13: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 15: `import org.elasticsearch.test.ESTestCase;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/LineTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/LinearRingTests.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 13: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 16: `import org.elasticsearch.test.ESTestCase;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/MultiLineTests.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.Collections;`
- Line 22: `import java.util.List;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/MultiPointTests.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.Arrays;`
- Line 22: `import java.util.Collections;`
- Line 23: `import java.util.List;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/MultiPolygonTests.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.ArrayList;`
- Line 21: `import java.util.Collections;`
- Line 22: `import java.util.List;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/PointTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/PolygonTests.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`
- Line 20: `import java.util.Collections;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/RectangleTests.java

### Unused Code (7)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.utils.GeographyValidator;`
- Line 14: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 15: `import org.elasticsearch.geometry.utils.StandardValidator;`
- Line 16: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.text.ParseException;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierCartesianTriangleAreaTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Line;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierHeightAndBackpathDistanceTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Line;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierSphericalHeightAndBackpathDistanceTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Line;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierTests.java

### Resource Leak (1)
- Line 688: `BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));`

### Concurrency Issue (2)
- Line 65: `private int added = 0;`
- Line 66: `private int removed = 0;`

### Exception Handling (1)
- Line 683: `throw new FileNotFoundException("classpath resource not found: " + name);`

### Unused Code (40)
- Line 65: `private int added = 0;`
- Line 66: `private int removed = 0;`
- Line 12: `import org.elasticsearch.geometry.Circle;`
- Line 13: `import org.elasticsearch.geometry.Geometry;`
- Line 14: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 15: `import org.elasticsearch.geometry.Line;`
- Line 16: `import org.elasticsearch.geometry.LinearRing;`
- Line 17: `import org.elasticsearch.geometry.MultiPoint;`
- Line 18: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 19: `import org.elasticsearch.geometry.Point;`
- Line 20: `import org.elasticsearch.geometry.Polygon;`
- Line 21: `import org.elasticsearch.geometry.Rectangle;`
- Line 22: `import org.elasticsearch.geometry.utils.CircleUtils;`
- Line 23: `import org.elasticsearch.geometry.utils.GeometryValidator;`
- Line 24: `import org.elasticsearch.geometry.utils.WellKnownText;`
- Line 25: `import org.elasticsearch.test.ESTestCase;`
- Line 26: `import org.hamcrest.Matcher;`
- Line 27: `import org.hamcrest.Matchers;`
- Line 29: `import java.io.BufferedReader;`
- Line 30: `import java.io.FileNotFoundException;`
- Line 31: `import java.io.IOException;`
- Line 32: `import java.io.InputStream;`
- Line 33: `import java.io.InputStreamReader;`
- Line 34: `import java.nio.charset.StandardCharsets;`
- Line 35: `import java.text.ParseException;`
- Line 36: `import java.util.ArrayList;`
- Line 37: `import java.util.Arrays;`
- Line 38: `import java.util.HashMap;`
- Line 39: `import java.util.List;`
- Line 40: `import java.util.PriorityQueue;`
- Line 41: `import java.util.function.Function;`
- Line 42: `import java.util.zip.GZIPInputStream;`
- Line 44: `import static org.elasticsearch.geometry.simplify.GeometrySimplifier.lengthOf;`
- Line 45: `import static org.hamcrest.Matchers.closeTo;`
- Line 46: `import static org.hamcrest.Matchers.containsString;`
- Line 47: `import static org.hamcrest.Matchers.equalTo;`
- Line 48: `import static org.hamcrest.Matchers.greaterThan;`
- Line 49: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`
- Line 50: `import static org.hamcrest.Matchers.lessThanOrEqualTo;`
- Line 51: `import static org.hamcrest.Matchers.not;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierTriangleAreaTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Line;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/GeometrySimplifierTriangleHeightTests.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.geometry.Line;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/SimplificationErrorCalculatorTests.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import static java.lang.Math.toRadians;`
- Line 15: `import static org.hamcrest.Matchers.closeTo;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/simplify/Vector3DTests.java

### Concurrency Issue (1)
- Line 23: `private static final double sin45 = sin(toRadians(45));`

### Unused Code (8)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.hamcrest.Description;`
- Line 14: `import org.hamcrest.Matcher;`
- Line 15: `import org.hamcrest.TypeSafeMatcher;`
- Line 17: `import static java.lang.Math.toRadians;`
- Line 18: `import static org.elasticsearch.geometry.simplify.SimplificationErrorCalculator.Point3D.from;`
- Line 19: `import static org.elasticsearch.geometry.simplify.SimplificationErrorCalculator.Point3D.sin;`
- Line 20: `import static org.hamcrest.Matchers.closeTo;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/utils/CircleUtilsTests.java

### Unused Code (9)
- Line 11: `import org.apache.lucene.util.SloppyMath;`
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.Circle;`
- Line 14: `import org.elasticsearch.geometry.LinearRing;`
- Line 15: `import org.elasticsearch.geometry.Polygon;`
- Line 16: `import org.elasticsearch.test.ESTestCase;`
- Line 18: `import static org.hamcrest.Matchers.closeTo;`
- Line 19: `import static org.hamcrest.Matchers.containsString;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/utils/GeoHashTests.java

### Unused Code (6)
- Line 11: `import org.elasticsearch.common.geo.GeoPoint;`
- Line 12: `import org.elasticsearch.geometry.Rectangle;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import java.util.ArrayList;`
- Line 17: `import static org.elasticsearch.geometry.utils.Geohash.addNeighbors;`
- Line 18: `import static org.hamcrest.Matchers.containsInAnyOrder;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/utils/SpatialEnvelopeVisitorTests.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geo.ShapeTestUtils;`
- Line 14: `import org.elasticsearch.geometry.Point;`
- Line 15: `import org.elasticsearch.geometry.Rectangle;`
- Line 16: `import org.elasticsearch.geometry.utils.SpatialEnvelopeVisitor.WrapLongitude;`
- Line 17: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import static org.hamcrest.Matchers.equalTo;`
- Line 20: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`
- Line 21: `import static org.hamcrest.Matchers.lessThanOrEqualTo;`

## ../libs/geo/src/test/java/org/elasticsearch/geometry/utils/WKBTests.java

### Unused Code (16)
- Line 12: `import org.elasticsearch.geo.GeometryTestUtils;`
- Line 13: `import org.elasticsearch.geometry.Circle;`
- Line 14: `import org.elasticsearch.geometry.Geometry;`
- Line 15: `import org.elasticsearch.geometry.GeometryCollection;`
- Line 16: `import org.elasticsearch.geometry.Line;`
- Line 17: `import org.elasticsearch.geometry.LinearRing;`
- Line 18: `import org.elasticsearch.geometry.MultiLine;`
- Line 19: `import org.elasticsearch.geometry.MultiPoint;`
- Line 20: `import org.elasticsearch.geometry.MultiPolygon;`
- Line 21: `import org.elasticsearch.geometry.Point;`
- Line 22: `import org.elasticsearch.geometry.Polygon;`
- Line 23: `import org.elasticsearch.geometry.Rectangle;`
- Line 24: `import org.elasticsearch.test.ESTestCase;`
- Line 26: `import java.nio.ByteOrder;`
- Line 27: `import java.util.ArrayList;`
- Line 28: `import java.util.List;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/FloatConsumer.java

### Unused Code (1)
- Line 12: `import java.util.function.Consumer;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/Grok.java

### Concurrency Issue (7)
- Line 31: `private static final String NAME_GROUP = "name";`
- Line 32: `private static final String SUBNAME_GROUP = "subname";`
- Line 33: `private static final String PATTERN_GROUP = "pattern";`
- Line 34: `private static final String DEFINITION_GROUP = "definition";`
- Line 35: `private static final String GROK_PATTERN = "%\\{"`
- Line 45: `private static final Regex GROK_PATTERN_REGEX = new Regex(`
- Line 54: `private static final int MAX_TO_REGEX_ITERATIONS = 100_000; // sanity limit`

### Exception Handling (3)
- Line 148: `throw new IllegalArgumentException("Unable to find pattern [" + patternName + "] in Grok's pattern dictionary");`
- Line 151: `throw new IllegalArgumentException("circular reference in pattern back [" + patternName + "]");`
- Line 166: `throw new IllegalArgumentException("Can not convert grok patterns to regular expression");`

### Unused Code (15)
- Line 12: `import org.jcodings.specific.UTF8Encoding;`
- Line 13: `import org.joni.Matcher;`
- Line 14: `import org.joni.NameEntry;`
- Line 15: `import org.joni.Option;`
- Line 16: `import org.joni.Regex;`
- Line 17: `import org.joni.Region;`
- Line 18: `import org.joni.Syntax;`
- Line 20: `import java.nio.charset.StandardCharsets;`
- Line 21: `import java.util.ArrayList;`
- Line 22: `import java.util.Iterator;`
- Line 23: `import java.util.List;`
- Line 24: `import java.util.Locale;`
- Line 25: `import java.util.Map;`
- Line 26: `import java.util.function.Consumer;`
- Line 27: `import java.util.function.Function;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/GrokBuiltinPatterns.java

### Resource Leak (1)
- Line 141: `BufferedReader br = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));`

### Concurrency Issue (2)
- Line 23: `public static final String ECS_COMPATIBILITY_DISABLED = "disabled";`
- Line 24: `public static final String ECS_COMPATIBILITY_V1 = "v1";`

### Exception Handling (2)
- Line 62: `throw new IllegalArgumentException("unsupported ECS compatibility mode [" + ecsCompatibility + "]");`
- Line 133: `throw new RuntimeException("failed to load built-in patterns", e);`

### Unused Code (8)
- Line 12: `import java.io.BufferedReader;`
- Line 13: `import java.io.IOException;`
- Line 14: `import java.io.InputStream;`
- Line 15: `import java.io.InputStreamReader;`
- Line 16: `import java.nio.charset.StandardCharsets;`
- Line 17: `import java.util.LinkedHashMap;`
- Line 18: `import java.util.List;`
- Line 19: `import java.util.Map;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/GrokCaptureConfig.java

### Unused Code (7)
- Line 12: `import org.joni.NameEntry;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.util.function.Consumer;`
- Line 16: `import java.util.function.DoubleConsumer;`
- Line 17: `import java.util.function.Function;`
- Line 18: `import java.util.function.IntConsumer;`
- Line 19: `import java.util.function.LongConsumer;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/GrokCaptureExtracter.java

### Unused Code (8)
- Line 12: `import org.joni.Region;`
- Line 14: `import java.util.ArrayList;`
- Line 15: `import java.util.LinkedHashMap;`
- Line 16: `import java.util.List;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.function.Consumer;`
- Line 19: `import java.util.function.Function;`
- Line 21: `import static java.util.Collections.emptyMap;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/GrokCaptureType.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.grok.GrokCaptureConfig.NativeExtracterMap;`
- Line 14: `import java.nio.charset.StandardCharsets;`
- Line 15: `import java.util.function.Consumer;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/MatcherWatchdog.java

### Concurrency Issue (2)
- Line 81: `private static final Noop INSTANCE = new Noop();`
- Line 103: `private final AtomicInteger registered = new AtomicInteger(0);`

### Unused Code (7)
- Line 11: `import org.joni.Matcher;`
- Line 13: `import java.util.Map;`
- Line 14: `import java.util.concurrent.ConcurrentHashMap;`
- Line 15: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 16: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 17: `import java.util.function.BiConsumer;`
- Line 18: `import java.util.function.LongSupplier;`

## ../libs/grok/src/main/java/org/elasticsearch/grok/PatternBank.java

### Concurrency Issue (1)
- Line 26: `public static final PatternBank EMPTY = new PatternBank(Map.of());`

### Exception Handling (2)
- Line 174: `throw new IllegalArgumentException("pattern [" + pattern + "] has an invalid syntax");`
- Line 181: `throw new IllegalArgumentException(`

### Unused Code (11)
- Line 12: `import java.util.ArrayDeque;`
- Line 13: `import java.util.ArrayList;`
- Line 14: `import java.util.Collections;`
- Line 15: `import java.util.Deque;`
- Line 16: `import java.util.HashSet;`
- Line 17: `import java.util.LinkedHashMap;`
- Line 18: `import java.util.LinkedHashSet;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Objects;`
- Line 22: `import java.util.Set;`

## ../libs/grok/src/test/java/org/elasticsearch/grok/GrokTests.java

### Exception Handling (6)
- Line 967: `throw new IllegalArgumentException();`
- Line 972: `throw new IllegalArgumentException();`
- Line 977: `throw new IllegalArgumentException();`
- Line 982: `throw new IllegalArgumentException();`
- Line 987: `throw new IllegalArgumentException();`
- Line 992: `throw new IllegalArgumentException();`

### Unused Code (29)
- Line 12: `import org.elasticsearch.core.Tuple;`
- Line 13: `import org.elasticsearch.grok.GrokCaptureConfig.NativeExtracterMap;`
- Line 14: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import java.nio.charset.StandardCharsets;`
- Line 17: `import java.util.ArrayList;`
- Line 18: `import java.util.Arrays;`
- Line 19: `import java.util.HashMap;`
- Line 20: `import java.util.List;`
- Line 21: `import java.util.Map;`
- Line 22: `import java.util.TreeMap;`
- Line 23: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 24: `import java.util.concurrent.atomic.AtomicReference;`
- Line 25: `import java.util.function.BiConsumer;`
- Line 26: `import java.util.function.Consumer;`
- Line 27: `import java.util.function.DoubleConsumer;`
- Line 28: `import java.util.function.Function;`
- Line 29: `import java.util.function.IntConsumer;`
- Line 30: `import java.util.function.LongConsumer;`
- Line 32: `import static org.elasticsearch.core.Tuple.tuple;`
- Line 33: `import static org.elasticsearch.grok.GrokCaptureType.BOOLEAN;`
- Line 34: `import static org.elasticsearch.grok.GrokCaptureType.DOUBLE;`
- Line 35: `import static org.elasticsearch.grok.GrokCaptureType.FLOAT;`
- Line 36: `import static org.elasticsearch.grok.GrokCaptureType.INTEGER;`
- Line 37: `import static org.elasticsearch.grok.GrokCaptureType.LONG;`
- Line 38: `import static org.elasticsearch.grok.GrokCaptureType.STRING;`
- Line 39: `import static org.hamcrest.Matchers.containsString;`
- Line 40: `import static org.hamcrest.Matchers.equalTo;`
- Line 41: `import static org.hamcrest.Matchers.is;`
- Line 42: `import static org.hamcrest.Matchers.nullValue;`

## ../libs/grok/src/test/java/org/elasticsearch/grok/MatcherWatchdogTests.java

### Unused Code (16)
- Line 11: `import org.elasticsearch.action.support.PlainActionFuture;`
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.joni.Matcher;`
- Line 14: `import org.mockito.Mockito;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.concurrent.ScheduledExecutorService;`
- Line 18: `import java.util.concurrent.TimeUnit;`
- Line 19: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 21: `import static org.hamcrest.Matchers.is;`
- Line 22: `import static org.mockito.ArgumentMatchers.any;`
- Line 23: `import static org.mockito.ArgumentMatchers.eq;`
- Line 24: `import static org.mockito.Mockito.doAnswer;`
- Line 25: `import static org.mockito.Mockito.mock;`
- Line 26: `import static org.mockito.Mockito.timeout;`
- Line 27: `import static org.mockito.Mockito.verify;`
- Line 28: `import static org.mockito.Mockito.verifyNoMoreInteractions;`

## ../libs/grok/src/test/java/org/elasticsearch/grok/PatternBankTests.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.util.HashMap;`
- Line 15: `import java.util.HashSet;`
- Line 16: `import java.util.LinkedHashMap;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.Set;`
- Line 20: `import static org.elasticsearch.test.ESTestCase.randomBoolean;`
- Line 21: `import static org.hamcrest.Matchers.containsString;`

## ../libs/h3/src/main/java/org/elasticsearch/h3/BaseCells.java

### Exception Handling (1)
- Line 591: `throw new IllegalArgumentException("Illegal base cell");`

## ../libs/h3/src/main/java/org/elasticsearch/h3/CellBoundary.java

### Unused Code (2)
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.Objects;`

## ../libs/h3/src/main/java/org/elasticsearch/h3/CoordIJK.java

### Concurrency Issue (9)
- Line 101: `*/`
- Line 166: `public void downAp7() {`
- Line 184: `public void downAp7r() {`
- Line 201: `public void downAp3() {`
- Line 219: `public void downAp3r() {`
- Line 237: `public void ijkRotate60cw() {`
- Line 254: `public void ijkRotate60ccw() {`
- Line 284: `public void upAp7r() {`
- Line 298: `public void upAp7() {`

## ../libs/h3/src/main/java/org/elasticsearch/h3/FaceIJK.java

### Exception Handling (2)
- Line 690: `throw new IllegalArgumentException(" out of range input");`
- Line 727: `throw new IllegalArgumentException(" out of range input");`

## ../libs/h3/src/main/java/org/elasticsearch/h3/FastMath.java

### Concurrency Issue (62)
- Line 93: `private static final double ONE_DIV_F2 = 1 / 2.0;`
- Line 94: `private static final double ONE_DIV_F3 = 1 / 6.0;`
- Line 95: `private static final double ONE_DIV_F4 = 1 / 24.0;`
- Line 97: `private static final double TWO_POW_24 = Double.longBitsToDouble(0x4170000000000000L);`
- Line 98: `private static final double TWO_POW_N24 = Double.longBitsToDouble(0x3E70000000000000L);`
- Line 100: `private static final double TWO_POW_66 = Double.longBitsToDouble(0x4410000000000000L);`
- Line 102: `private static final int MIN_DOUBLE_EXPONENT = -1074;`
- Line 175: `private static final double TWOPI_TAB0 = Double.longBitsToDouble(0x401921FB40000000L);`
- Line 176: `private static final double TWOPI_TAB1 = Double.longBitsToDouble(0x3E94442D00000000L);`
- Line 177: `private static final double TWOPI_TAB2 = Double.longBitsToDouble(0x3D18469880000000L);`
- Line 178: `private static final double TWOPI_TAB3 = Double.longBitsToDouble(0x3B98CC5160000000L);`
- Line 179: `private static final double TWOPI_TAB4 = Double.longBitsToDouble(0x3A101B8380000000L);`
- Line 181: `private static final double INVPIO2 = Double.longBitsToDouble(0x3FE45F306DC9C883L); // 6.36619772367581382433e-01 53 bits of 2/pi`
- Line 182: `private static final double PIO2_HI = Double.longBitsToDouble(0x3FF921FB54400000L); // 1.57079632673412561417e+00 first 33 bits of pi/2`
- Line 183: `private static final double PIO2_LO = Double.longBitsToDouble(0x3DD0B4611A626331L); // 6.07710050650619224932e-11 pi/2 - PIO2_HI`
- Line 184: `private static final double INVTWOPI = INVPIO2 / 4;`
- Line 185: `private static final double TWOPI_HI = 4 * PIO2_HI;`
- Line 196: `private static final int SIN_COS_TABS_SIZE = (1 << getTabSizePower(11)) + 1;`
- Line 197: `private static final double SIN_COS_DELTA_HI = TWOPI_HI / (SIN_COS_TABS_SIZE - 1);`
- Line 198: `private static final double SIN_COS_DELTA_LO = TWOPI_LO / (SIN_COS_TABS_SIZE - 1);`
- Line 199: `private static final double SIN_COS_INDEXER = 1 / (SIN_COS_DELTA_HI + SIN_COS_DELTA_LO);`
- Line 225: `private static final double TAN_MAX_VALUE_FOR_TABS = Math.toRadians(77.0);`
- Line 227: `private static final int TAN_TABS_SIZE = (int) ((TAN_MAX_VALUE_FOR_TABS / (Math.PI / 2)) * (TAN_VIRTUAL_TABS_SIZE - 1)) + 1;`
- Line 228: `private static final double TAN_DELTA_HI = PIO2_HI / (TAN_VIRTUAL_TABS_SIZE - 1);`
- Line 229: `private static final double TAN_DELTA_LO = PIO2_LO / (TAN_VIRTUAL_TABS_SIZE - 1);`
- Line 230: `private static final double TAN_INDEXER = 1 / (TAN_DELTA_HI + TAN_DELTA_LO);`
- Line 255: `private static final double ASIN_MAX_VALUE_FOR_TABS = StrictMath.sin(Math.toRadians(73.0));`
- Line 257: `private static final int ASIN_TABS_SIZE = (1 << getTabSizePower(13)) + 1;`
- Line 258: `private static final double ASIN_DELTA = ASIN_MAX_VALUE_FOR_TABS / (ASIN_TABS_SIZE - 1);`
- Line 259: `private static final double ASIN_INDEXER = 1 / ASIN_DELTA;`
- Line 266: `private static final double ASIN_MAX_VALUE_FOR_POWTABS = StrictMath.sin(Math.toRadians(88.6));`
- Line 267: `private static final int ASIN_POWTABS_POWER = 84;`
- Line 269: `private static final double ASIN_POWTABS_ONE_DIV_MAX_VALUE = 1 / ASIN_MAX_VALUE_FOR_POWTABS;`
- Line 270: `private static final int ASIN_POWTABS_SIZE = (1 << getTabSizePower(12)) + 1;`
- Line 271: `private static final int ASIN_POWTABS_SIZE_MINUS_ONE = ASIN_POWTABS_SIZE - 1;`
- Line 279: `private static final double ASIN_PIO2_HI = Double.longBitsToDouble(0x3FF921FB54442D18L); // 1.57079632679489655800e+00`
- Line 280: `private static final double ASIN_PIO2_LO = Double.longBitsToDouble(0x3C91A62633145C07L); // 6.12323399573676603587e-17`
- Line 281: `private static final double ASIN_PS0 = Double.longBitsToDouble(0x3fc5555555555555L); // 1.66666666666666657415e-01`
- Line 282: `private static final double ASIN_PS1 = Double.longBitsToDouble(0xbfd4d61203eb6f7dL); // -3.25565818622400915405e-01`
- Line 283: `private static final double ASIN_PS2 = Double.longBitsToDouble(0x3fc9c1550e884455L); // 2.01212532134862925881e-01`
- Line 284: `private static final double ASIN_PS3 = Double.longBitsToDouble(0xbfa48228b5688f3bL); // -4.00555345006794114027e-02`
- Line 285: `private static final double ASIN_PS4 = Double.longBitsToDouble(0x3f49efe07501b288L); // 7.91534994289814532176e-04`
- Line 286: `private static final double ASIN_PS5 = Double.longBitsToDouble(0x3f023de10dfdf709L); // 3.47933107596021167570e-05`
- Line 287: `private static final double ASIN_QS1 = Double.longBitsToDouble(0xc0033a271c8a2d4bL); // -2.40339491173441421878e+00`
- Line 288: `private static final double ASIN_QS2 = Double.longBitsToDouble(0x40002ae59c598ac8L); // 2.02094576023350569471e+00`
- Line 289: `private static final double ASIN_QS3 = Double.longBitsToDouble(0xbfe6066c1b8d0159L); // -6.88283971605453293030e-01`
- Line 302: `private static final double ATAN_MAX_VALUE_FOR_TABS = StrictMath.tan(Math.toRadians(74.0));`
- Line 304: `private static final int ATAN_TABS_SIZE = (1 << getTabSizePower(12)) + 1;`
- Line 305: `private static final double ATAN_DELTA = ATAN_MAX_VALUE_FOR_TABS / (ATAN_TABS_SIZE - 1);`
- Line 306: `private static final double ATAN_INDEXER = 1 / ATAN_DELTA;`
- Line 313: `private static final double ATAN_HI3 = Double.longBitsToDouble(0x3ff921fb54442d18L); // 1.57079632679489655800e+00 atan(inf)hi`
- Line 314: `private static final double ATAN_LO3 = Double.longBitsToDouble(0x3c91a62633145c07L); // 6.12323399573676603587e-17 atan(inf)lo`
- Line 315: `private static final double ATAN_AT0 = Double.longBitsToDouble(0x3fd555555555550dL); // 3.33333333333329318027e-01`
- Line 316: `private static final double ATAN_AT1 = Double.longBitsToDouble(0xbfc999999998ebc4L); // -1.99999999998764832476e-01`
- Line 317: `private static final double ATAN_AT2 = Double.longBitsToDouble(0x3fc24924920083ffL); // 1.42857142725034663711e-01`
- Line 318: `private static final double ATAN_AT3 = Double.longBitsToDouble(0xbfbc71c6fe231671L); // -1.11111104054623557880e-01`
- Line 319: `private static final double ATAN_AT4 = Double.longBitsToDouble(0x3fb745cdc54c206eL); // 9.09088713343650656196e-02`
- Line 320: `private static final double ATAN_AT5 = Double.longBitsToDouble(0xbfb3b0f2af749a6dL); // -7.69187620504482999495e-02`
- Line 321: `private static final double ATAN_AT6 = Double.longBitsToDouble(0x3fb10d66a0d03d51L); // 6.66107313738753120669e-02`
- Line 322: `private static final double ATAN_AT7 = Double.longBitsToDouble(0xbfadde2d52defd9aL); // -5.83357013379057348645e-02`
- Line 323: `private static final double ATAN_AT8 = Double.longBitsToDouble(0x3fa97b4b24760debL); // 4.97687799461593236017e-02`
- Line 324: `private static final double ATAN_AT9 = Double.longBitsToDouble(0xbfa2b4442c6a6c2fL); // -3.65315727442169155270e-02`

## ../libs/h3/src/main/java/org/elasticsearch/h3/H3.java

### Concurrency Issue (1)
- Line 36: `public static final int MAX_H3_RES = 15;`

### Exception Handling (9)
- Line 225: `throw new IllegalArgumentException("Input is a base cell");`
- Line 264: `throw new IllegalArgumentException("Resolution overflow");`
- Line 273: `throw new IllegalArgumentException("invalid child position");`
- Line 321: `throw new IllegalArgumentException("Resolution overflow");`
- Line 326: `throw new IllegalArgumentException("invalid child position");`
- Line 404: `throw new IllegalArgumentException("invalid ring position");`
- Line 455: `throw new IllegalArgumentException("Invalid child resolution [" + childRes + "]");`
- Line 488: `throw new IllegalArgumentException("Invalid child resolution [" + MAX_H3_RES + "]");`
- Line 514: `throw new IllegalArgumentException("Invalid child resolution [" + MAX_H3_RES + "]");`

### Unused Code (2)
- Line 25: `import java.util.Arrays;`
- Line 27: `import static java.lang.Math.toRadians;`

## ../libs/h3/src/main/java/org/elasticsearch/h3/H3Index.java

### Concurrency Issue (1)
- Line 59: `public static final long H3_MODE_MASK_NEGATIVE = ~H3_MODE_MASK;`

### Exception Handling (1)
- Line 194: `throw new IllegalArgumentException();`

## ../libs/h3/src/main/java/org/elasticsearch/h3/HexRing.java

### Exception Handling (7)
- Line 594: `throw new IllegalArgumentException("Invalid cell: " + origin);`
- Line 598: `throw new IllegalArgumentException("Invalid cell: " + destination);`
- Line 629: `throw new IllegalArgumentException("");`
- Line 638: `throw new IllegalArgumentException("Undefined error checking for neighbors");`
- Line 680: `throw new IllegalArgumentException("Invalid base cell looking for neighbor");`
- Line 708: `throw new IllegalArgumentException();`
- Line 764: `throw new IllegalArgumentException("Undefined error looking for neighbor");  // LCOV_EXCL_LINE`

### Infinite Loop (1)
- Line 686: `while (true) {`

## ../libs/h3/src/main/java/org/elasticsearch/h3/LatLng.java

### Concurrency Issue (1)
- Line 36: `private static final double M_PI_2 = 1.5707963267948966;`

### Unused Code (1)
- Line 25: `import java.util.Objects;`

## ../libs/h3/src/main/java/org/elasticsearch/h3/Vec2d.java

### Concurrency Issue (1)
- Line 39: `private static final double M_ONETHIRD = 1.0 / 3.0;`

### Unused Code (1)
- Line 25: `import java.util.Objects;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/CellBoundaryTests.java

### Resource Leak (1)
- Line 150: `BufferedReader reader = new BufferedReader(new InputStreamReader(new GZIPInputStream(fis), StandardCharsets.UTF_8));`

### Exception Handling (1)
- Line 164: `throw new IllegalArgumentException();`

### Unused Code (14)
- Line 21: `import org.apache.lucene.geo.GeoEncodingUtils;`
- Line 22: `import org.apache.lucene.tests.geo.GeoTestUtil;`
- Line 23: `import org.elasticsearch.test.ESTestCase;`
- Line 25: `import java.io.BufferedReader;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.io.InputStream;`
- Line 28: `import java.io.InputStreamReader;`
- Line 29: `import java.nio.charset.StandardCharsets;`
- Line 30: `import java.util.ArrayList;`
- Line 31: `import java.util.List;`
- Line 32: `import java.util.StringTokenizer;`
- Line 33: `import java.util.zip.GZIPInputStream;`
- Line 35: `import static org.hamcrest.Matchers.either;`
- Line 36: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/CellCenterTests.java

### Resource Leak (1)
- Line 147: `BufferedReader reader = new BufferedReader(new InputStreamReader(new GZIPInputStream(fis), StandardCharsets.UTF_8));`

### Unused Code (8)
- Line 21: `import org.elasticsearch.test.ESTestCase;`
- Line 23: `import java.io.BufferedReader;`
- Line 24: `import java.io.IOException;`
- Line 25: `import java.io.InputStream;`
- Line 26: `import java.io.InputStreamReader;`
- Line 27: `import java.nio.charset.StandardCharsets;`
- Line 28: `import java.util.StringTokenizer;`
- Line 29: `import java.util.zip.GZIPInputStream;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/FastMathTests.java

### Concurrency Issue (1)
- Line 42: `static double ATAN2_DELTA = 1E-14;`

### Unused Code (3)
- Line 22: `import org.elasticsearch.test.ESTestCase;`
- Line 24: `import java.util.function.DoubleSupplier;`
- Line 25: `import java.util.function.DoubleUnaryOperator;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/GeoToH3Tests.java

### Unused Code (8)
- Line 21: `import org.apache.lucene.spatial3d.geom.GeoPoint;`
- Line 22: `import org.apache.lucene.spatial3d.geom.GeoPolygon;`
- Line 23: `import org.apache.lucene.spatial3d.geom.GeoPolygonFactory;`
- Line 24: `import org.apache.lucene.spatial3d.geom.PlanetModel;`
- Line 25: `import org.apache.lucene.tests.geo.GeoTestUtil;`
- Line 26: `import org.elasticsearch.test.ESTestCase;`
- Line 28: `import java.util.ArrayList;`
- Line 29: `import java.util.List;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/HexRingTests.java

### Unused Code (3)
- Line 21: `import org.apache.lucene.tests.geo.GeoTestUtil;`
- Line 22: `import org.elasticsearch.test.ESTestCase;`
- Line 24: `import java.util.Arrays;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/LatLngTests.java

### Unused Code (7)
- Line 21: `import org.apache.lucene.spatial3d.geom.GeoPoint;`
- Line 22: `import org.apache.lucene.spatial3d.geom.LatLonBounds;`
- Line 23: `import org.apache.lucene.spatial3d.geom.Plane;`
- Line 24: `import org.apache.lucene.spatial3d.geom.PlanetModel;`
- Line 25: `import org.apache.lucene.spatial3d.geom.SidedPlane;`
- Line 26: `import org.apache.lucene.tests.geo.GeoTestUtil;`
- Line 27: `import org.elasticsearch.test.ESTestCase;`

## ../libs/h3/src/test/java/org/elasticsearch/h3/ParentChildNavigationTests.java

### Unused Code (13)
- Line 21: `import com.carrotsearch.randomizedtesting.generators.RandomPicks;`
- Line 23: `import org.apache.lucene.geo.Point;`
- Line 24: `import org.apache.lucene.spatial3d.geom.GeoPoint;`
- Line 25: `import org.apache.lucene.spatial3d.geom.GeoPolygon;`
- Line 26: `import org.apache.lucene.spatial3d.geom.GeoPolygonFactory;`
- Line 27: `import org.apache.lucene.spatial3d.geom.PlanetModel;`
- Line 28: `import org.apache.lucene.tests.geo.GeoTestUtil;`
- Line 29: `import org.elasticsearch.common.util.set.Sets;`
- Line 30: `import org.elasticsearch.test.ESTestCase;`
- Line 31: `import org.hamcrest.Matchers;`
- Line 33: `import java.util.ArrayList;`
- Line 34: `import java.util.List;`
- Line 35: `import java.util.Set;`

## ../libs/logging/src/main/java/org/elasticsearch/logging/LogManager.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.logging.internal.spi.LoggerFactory;`

## ../libs/logging/src/main/java/org/elasticsearch/logging/Logger.java

### Unused Code (1)
- Line 12: `import java.util.function.Supplier;`

## ../libs/logging/src/main/java/org/elasticsearch/logging/internal/spi/LoggerFactory.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.logging.Level;`
- Line 13: `import org.elasticsearch.logging.Logger;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/StableBridgeAPI.java

### Unused Code (4)
- Line 11: `import java.util.Map;`
- Line 12: `import java.util.Objects;`
- Line 13: `import java.util.function.Function;`
- Line 14: `import java.util.stream.Collectors;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/common/SettingsBridge.java

### Unused Code (2)
- Line 11: `import org.elasticsearch.common.settings.Settings;`
- Line 12: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/core/IOUtilsBridge.java

### Unused Code (2)
- Line 11: `import org.elasticsearch.core.IOUtils;`
- Line 13: `import java.io.Closeable;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/env/EnvironmentBridge.java

### Unused Code (4)
- Line 11: `import org.elasticsearch.env.Environment;`
- Line 12: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 13: `import org.elasticsearch.logstashbridge.common.SettingsBridge;`
- Line 15: `import java.nio.file.Path;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/ConfigurationUtilsBridge.java

### Unused Code (4)
- Line 11: `import org.elasticsearch.ingest.ConfigurationUtils;`
- Line 12: `import org.elasticsearch.logstashbridge.script.ScriptServiceBridge;`
- Line 13: `import org.elasticsearch.logstashbridge.script.TemplateScriptBridge;`
- Line 15: `import java.util.Map;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/IngestDocumentBridge.java

### Unused Code (8)
- Line 11: `import org.elasticsearch.ingest.IngestDocument;`
- Line 12: `import org.elasticsearch.ingest.LogstashInternalBridge;`
- Line 13: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 14: `import org.elasticsearch.logstashbridge.script.MetadataBridge;`
- Line 15: `import org.elasticsearch.logstashbridge.script.TemplateScriptBridge;`
- Line 17: `import java.util.Map;`
- Line 18: `import java.util.Set;`
- Line 19: `import java.util.function.BiConsumer;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/PipelineBridge.java

### Unused Code (6)
- Line 11: `import org.elasticsearch.core.FixForMultiProject;`
- Line 12: `import org.elasticsearch.ingest.Pipeline;`
- Line 13: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 14: `import org.elasticsearch.logstashbridge.script.ScriptServiceBridge;`
- Line 16: `import java.util.Map;`
- Line 17: `import java.util.function.BiConsumer;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/PipelineConfigurationBridge.java

### Unused Code (5)
- Line 11: `import org.elasticsearch.common.bytes.BytesArray;`
- Line 12: `import org.elasticsearch.ingest.PipelineConfiguration;`
- Line 13: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 14: `import org.elasticsearch.xcontent.XContentType;`
- Line 16: `import java.util.Map;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/ingest/ProcessorBridge.java

### Unused Code (10)
- Line 11: `import org.elasticsearch.core.FixForMultiProject;`
- Line 12: `import org.elasticsearch.core.TimeValue;`
- Line 13: `import org.elasticsearch.ingest.IngestService;`
- Line 14: `import org.elasticsearch.ingest.Processor;`
- Line 15: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 16: `import org.elasticsearch.logstashbridge.env.EnvironmentBridge;`
- Line 17: `import org.elasticsearch.logstashbridge.script.ScriptServiceBridge;`
- Line 18: `import org.elasticsearch.logstashbridge.threadpool.ThreadPoolBridge;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.function.BiConsumer;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/plugins/IngestPluginBridge.java

### Unused Code (6)
- Line 11: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 12: `import org.elasticsearch.logstashbridge.ingest.ProcessorBridge;`
- Line 13: `import org.elasticsearch.plugins.IngestPlugin;`
- Line 15: `import java.io.Closeable;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.util.Map;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/script/MetadataBridge.java

### Unused Code (3)
- Line 11: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 12: `import org.elasticsearch.script.Metadata;`
- Line 14: `import java.time.ZonedDateTime;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/script/ScriptServiceBridge.java

### Unused Code (18)
- Line 11: `import org.elasticsearch.common.settings.Settings;`
- Line 12: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 13: `import org.elasticsearch.logstashbridge.common.SettingsBridge;`
- Line 14: `import org.elasticsearch.painless.PainlessPlugin;`
- Line 15: `import org.elasticsearch.painless.PainlessScriptEngine;`
- Line 16: `import org.elasticsearch.painless.spi.Whitelist;`
- Line 17: `import org.elasticsearch.script.IngestConditionalScript;`
- Line 18: `import org.elasticsearch.script.IngestScript;`
- Line 19: `import org.elasticsearch.script.ScriptContext;`
- Line 20: `import org.elasticsearch.script.ScriptEngine;`
- Line 21: `import org.elasticsearch.script.ScriptModule;`
- Line 22: `import org.elasticsearch.script.ScriptService;`
- Line 23: `import org.elasticsearch.script.mustache.MustacheScriptEngine;`
- Line 25: `import java.io.Closeable;`
- Line 26: `import java.io.IOException;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Map;`
- Line 29: `import java.util.function.LongSupplier;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/script/TemplateScriptBridge.java

### Unused Code (2)
- Line 11: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 12: `import org.elasticsearch.script.TemplateScript;`

## ../libs/logstash-bridge/src/main/java/org/elasticsearch/logstashbridge/threadpool/ThreadPoolBridge.java

### Unused Code (6)
- Line 11: `import org.elasticsearch.logstashbridge.StableBridgeAPI;`
- Line 12: `import org.elasticsearch.logstashbridge.common.SettingsBridge;`
- Line 13: `import org.elasticsearch.telemetry.metric.MeterRegistry;`
- Line 14: `import org.elasticsearch.threadpool.DefaultBuiltInExecutorBuilders;`
- Line 15: `import org.elasticsearch.threadpool.ThreadPool;`
- Line 17: `import java.util.concurrent.TimeUnit;`

## ../libs/lz4/src/main/java/org/elasticsearch/lz4/ESLZ4Compressor.java

### Exception Handling (4)
- Line 84: `throw new LZ4Exception("maxDestLen is too small");`
- Line 104: `throw new LZ4Exception("maxDestLen is too small");`
- Line 182: `throw new LZ4Exception("maxDestLen is too small");`
- Line 201: `throw new LZ4Exception("maxDestLen is too small");`

### Infinite Loop (4)
- Line 97: `while (true) {`
- Line 157: `label63: while (true) {`
- Line 162: `while (true) {`
- Line 195: `while (true) {`

### Unused Code (4)
- Line 21: `import net.jpountz.lz4.LZ4Compressor;`
- Line 22: `import net.jpountz.lz4.LZ4Exception;`
- Line 24: `import java.nio.ByteBuffer;`
- Line 25: `import java.util.Arrays;`

## ../libs/lz4/src/main/java/org/elasticsearch/lz4/ESLZ4Decompressor.java

### Exception Handling (4)
- Line 43: `throw new LZ4Exception("Malformed input at " + srcOff);`
- Line 67: `throw new LZ4Exception("Malformed input at " + sOff);`
- Line 81: `throw new LZ4Exception("Malformed input at " + sOff);`
- Line 97: `throw new LZ4Exception("Malformed input at " + sOff);`

### Infinite Loop (1)
- Line 52: `while (true) {`

### Unused Code (3)
- Line 21: `import net.jpountz.lz4.LZ4Exception;`
- Line 22: `import net.jpountz.lz4.LZ4FastDecompressor;`
- Line 24: `import java.nio.ByteBuffer;`

## ../libs/lz4/src/main/java/org/elasticsearch/lz4/LZ4SafeUtils.java

### Concurrency Issue (1)
- Line 45: `private static final VarHandle intPlatformNative = MethodHandles.byteArrayViewVarHandle(int[].class, Utils.NATIVE_BYTE_ORDER);`

### Exception Handling (4)
- Line 138: `throw new LZ4Exception("Malformed input at offset " + sOff);`
- Line 147: `throw new LZ4Exception("maxDestLen is too small");`
- Line 170: `throw new LZ4Exception("maxDestLen is too small");`
- Line 188: `throw new LZ4Exception();`

### Unused Code (9)
- Line 22: `import net.jpountz.lz4.LZ4Exception;`
- Line 23: `import net.jpountz.util.Utils;`
- Line 25: `import java.lang.invoke.MethodHandles;`
- Line 26: `import java.lang.invoke.VarHandle;`
- Line 27: `import java.util.Arrays;`
- Line 29: `import static org.elasticsearch.lz4.LZ4Constants.LAST_LITERALS;`
- Line 30: `import static org.elasticsearch.lz4.LZ4Constants.ML_BITS;`
- Line 31: `import static org.elasticsearch.lz4.LZ4Constants.ML_MASK;`
- Line 32: `import static org.elasticsearch.lz4.LZ4Constants.RUN_MASK;`

## ../libs/lz4/src/main/java/org/elasticsearch/lz4/LZ4Utils.java

### Exception Handling (2)
- Line 41: `throw new IllegalArgumentException("length must be >= 0, got " + length);`
- Line 43: `throw new IllegalArgumentException("length must be < " + MAX_INPUT_SIZE);`

### Unused Code (4)
- Line 22: `import static org.elasticsearch.lz4.LZ4Constants.HASH_LOG;`
- Line 23: `import static org.elasticsearch.lz4.LZ4Constants.HASH_LOG_64K;`
- Line 24: `import static org.elasticsearch.lz4.LZ4Constants.HASH_LOG_HC;`
- Line 25: `import static org.elasticsearch.lz4.LZ4Constants.MIN_MATCH;`

## ../libs/lz4/src/main/java/org/elasticsearch/lz4/SafeUtils.java

### Concurrency Issue (2)
- Line 38: `private static final VarHandle intPlatformNative = MethodHandles.byteArrayViewVarHandle(int[].class, Utils.NATIVE_BYTE_ORDER);`
- Line 40: `private static final VarHandle shortLittleEndian = MethodHandles.byteArrayViewVarHandle(short[].class, ByteOrder.LITTLE_ENDIAN);`

### Exception Handling (2)
- Line 44: `throw new ArrayIndexOutOfBoundsException(off);`
- Line 58: `throw new IllegalArgumentException("lengths must be >= 0");`

### Unused Code (4)
- Line 21: `import net.jpountz.util.Utils;`
- Line 23: `import java.lang.invoke.MethodHandles;`
- Line 24: `import java.lang.invoke.VarHandle;`
- Line 25: `import java.nio.ByteOrder;`

## ../libs/lz4/src/test/java/org/elasticsearch/lz4/AbstractLZ4TestCase.java

### Exception Handling (1)
- Line 390: `throw new IllegalStateException("Cannot find " + resource);`

### Unused Code (12)
- Line 21: `import net.jpountz.lz4.LZ4Compressor;`
- Line 22: `import net.jpountz.lz4.LZ4CompressorWithLength;`
- Line 23: `import net.jpountz.lz4.LZ4DecompressorWithLength;`
- Line 24: `import net.jpountz.lz4.LZ4FastDecompressor;`
- Line 25: `import net.jpountz.lz4.LZ4SafeDecompressor;`
- Line 27: `import org.elasticsearch.test.ESTestCase;`
- Line 29: `import java.io.ByteArrayOutputStream;`
- Line 30: `import java.io.IOException;`
- Line 31: `import java.io.InputStream;`
- Line 32: `import java.nio.ByteBuffer;`
- Line 33: `import java.nio.ByteOrder;`
- Line 34: `import java.util.Arrays;`

## ../libs/lz4/src/test/java/org/elasticsearch/lz4/ESLZ4CompressorTests.java

### Unused Code (7)
- Line 12: `import net.jpountz.lz4.LZ4Compressor;`
- Line 13: `import net.jpountz.lz4.LZ4Factory;`
- Line 14: `import net.jpountz.lz4.LZ4FastDecompressor;`
- Line 16: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 17: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.charset.StandardCharsets;`

## ../libs/lz4/src/test/java/org/elasticsearch/lz4/ESLZ4DecompressorTests.java

### Unused Code (7)
- Line 12: `import net.jpountz.lz4.LZ4Compressor;`
- Line 13: `import net.jpountz.lz4.LZ4Factory;`
- Line 14: `import net.jpountz.lz4.LZ4FastDecompressor;`
- Line 16: `import org.elasticsearch.common.io.stream.BytesStreamOutput;`
- Line 17: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.charset.StandardCharsets;`

## ../libs/lz4/src/test/java/org/elasticsearch/lz4/ESLZ4Tests.java

### Unused Code (9)
- Line 21: `import net.jpountz.lz4.LZ4Compressor;`
- Line 22: `import net.jpountz.lz4.LZ4Exception;`
- Line 23: `import net.jpountz.lz4.LZ4Factory;`
- Line 24: `import net.jpountz.lz4.LZ4FastDecompressor;`
- Line 25: `import net.jpountz.lz4.LZ4SafeDecompressor;`
- Line 27: `import java.io.ByteArrayOutputStream;`
- Line 28: `import java.io.IOException;`
- Line 29: `import java.nio.ByteBuffer;`
- Line 30: `import java.util.Arrays;`

## ../libs/native/src/main/java/module-info.java

### Unused Code (3)
- Line 10: `import org.elasticsearch.jdk.ModuleQualifiedExportsService;`
- Line 11: `import org.elasticsearch.nativeaccess.exports.NativeAccessModuleExportsService;`
- Line 12: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/AbstractNativeAccess.java

### Concurrency Issue (3)
- Line 20: `protected static final Logger logger = LogManager.getLogger(NativeAccess.class);`
- Line 25: `protected boolean isMemoryLocked = false;`
- Line 26: `protected ExecSandboxState execSandboxState = ExecSandboxState.NONE;`

### Unused Code (5)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.JavaLibrary;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 16: `import org.elasticsearch.nativeaccess.lib.ZstdLibrary;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/CloseableByteBuffer.java

### Unused Code (1)
- Line 12: `import java.nio.ByteBuffer;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/LinuxNativeAccess.java

### Exception Handling (4)
- Line 172: `throw new UnsupportedOperationException("seccomp unavailable: '" + archId + "' architecture unsupported");`
- Line 239: `throw new UnsupportedOperationException(`
- Line 255: `throw new UnsupportedOperationException(`
- Line 270: `throw new UnsupportedOperationException(`

### Unused Code (6)
- Line 12: `import org.elasticsearch.nativeaccess.lib.LinuxCLibrary;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.LinuxCLibrary.SockFProg;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.LinuxCLibrary.SockFilter;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 16: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary;`
- Line 18: `import java.util.Map;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/MacNativeAccess.java

### Concurrency Issue (4)
- Line 26: `private static final int F_PREALLOCATE = 42;`
- Line 27: `private static final int F_ALLOCATECONTIG = 0x2; // allocate contiguous space`
- Line 28: `private static final int F_ALLOCATEALL = 0x4; // allocate all the requested space or no space at all`
- Line 34: `static final String SANDBOX_RULES = "(version 1) (allow default) (deny process-fork) (deny process-exec)";`

### Exception Handling (1)
- Line 112: `throw new UncheckedIOException(e);`

### Unused Code (10)
- Line 12: `import org.elasticsearch.core.IOUtils;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.MacCLibrary;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 16: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary.RLimit;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.io.UncheckedIOException;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.Collections;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/NativeAccess.java

### Unused Code (3)
- Line 12: `import java.nio.file.Path;`
- Line 13: `import java.util.Optional;`
- Line 14: `import java.util.OptionalLong;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/NativeAccessHolder.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/NoopNativeAccess.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 15: `import java.nio.file.Path;`
- Line 16: `import java.util.Optional;`
- Line 17: `import java.util.OptionalLong;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/PosixNativeAccess.java

### Concurrency Issue (4)
- Line 24: `public static final int MCL_CURRENT = 1;`
- Line 25: `public static final int ENOMEM = 12;`
- Line 26: `public static final int O_RDONLY = 0;`
- Line 27: `public static final int O_WRONLY = 1;`

### Unused Code (8)
- Line 12: `import org.elasticsearch.core.SuppressForbidden;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.VectorLibrary;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.nio.file.Path;`
- Line 19: `import java.util.Optional;`
- Line 20: `import java.util.OptionalLong;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/ProcessLimits.java

### Concurrency Issue (1)
- Line 20: `public static final long UNKNOWN = -1;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/Systemd.java

### Concurrency Issue (1)
- Line 26: `private static final Logger logger = LogManager.getLogger(Systemd.class);`

### Exception Handling (1)
- Line 110: `throw new RuntimeException(message);`

### Unused Code (4)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary;`
- Line 16: `import java.nio.charset.StandardCharsets;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/VectorSimilarityFunctions.java

### Unused Code (1)
- Line 12: `import java.lang.invoke.MethodHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/WindowsFunctions.java

### Concurrency Issue (1)
- Line 20: `private static final Logger logger = LogManager.getLogger(Systemd.class);`

### Unused Code (3)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.Kernel32Library;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/WindowsNativeAccess.java

### Concurrency Issue (4)
- Line 31: `public static final int PAGE_NOACCESS = 0x0001;`
- Line 32: `public static final int PAGE_GUARD = 0x0100;`
- Line 33: `public static final int MEM_COMMIT = 0x1000;`
- Line 45: `private static final int JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 8;`

### Unused Code (9)
- Line 12: `import org.elasticsearch.nativeaccess.lib.Kernel32Library;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.Kernel32Library.Handle;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 16: `import java.nio.file.Files;`
- Line 17: `import java.nio.file.Path;`
- Line 18: `import java.util.Optional;`
- Line 19: `import java.util.OptionalLong;`
- Line 20: `import java.util.concurrent.atomic.AtomicInteger;`
- Line 22: `import static java.lang.management.ManagementFactory.getMemoryMXBean;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/Zstd.java

### Exception Handling (2)
- Line 36: `throw new IllegalStateException("Integer overflow? ret=" + ret);`
- Line 52: `throw new IllegalStateException("Integer overflow? ret=" + ret);`

### Unused Code (3)
- Line 12: `import org.elasticsearch.nativeaccess.lib.ZstdLibrary;`
- Line 14: `import java.nio.ByteBuffer;`
- Line 15: `import java.util.Objects;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/exports/NativeAccessModuleExportsService.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.jdk.ModuleQualifiedExportsService;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/ArenaUtil.java

### Unused Code (5)
- Line 12: `import java.lang.foreign.Arena;`
- Line 13: `import java.lang.foreign.MemoryLayout;`
- Line 14: `import java.lang.foreign.MemorySegment;`
- Line 15: `import java.nio.charset.Charset;`
- Line 17: `import static java.lang.foreign.ValueLayout.JAVA_BYTE;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkCloseableByteBuffer.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`
- Line 14: `import java.lang.foreign.Arena;`
- Line 15: `import java.lang.foreign.MemorySegment;`
- Line 16: `import java.nio.ByteBuffer;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkJavaLibrary.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.JavaLibrary;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkKernel32Library.java

### Concurrency Issue (3)
- Line 44: `private static final StructLayout CAPTURE_GETLASTERROR_LAYOUT = Linker.Option.captureStateLayout();`
- Line 124: `private static final MemoryLayout layout = MemoryLayout.structLayout(`
- Line 172: `private static final MemoryLayout layout = MemoryLayout.structLayout(`

### Unused Code (23)
- Line 12: `import org.elasticsearch.nativeaccess.WindowsFunctions.ConsoleCtrlHandler;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.Kernel32Library;`
- Line 15: `import java.lang.foreign.Arena;`
- Line 16: `import java.lang.foreign.FunctionDescriptor;`
- Line 17: `import java.lang.foreign.Linker;`
- Line 18: `import java.lang.foreign.MemoryLayout;`
- Line 19: `import java.lang.foreign.MemorySegment;`
- Line 20: `import java.lang.foreign.StructLayout;`
- Line 21: `import java.lang.invoke.MethodHandle;`
- Line 22: `import java.lang.invoke.VarHandle;`
- Line 23: `import java.nio.charset.StandardCharsets;`
- Line 24: `import java.util.function.IntConsumer;`
- Line 26: `import static java.lang.foreign.MemoryLayout.PathElement.groupElement;`
- Line 27: `import static java.lang.foreign.MemoryLayout.paddingLayout;`
- Line 28: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 29: `import static java.lang.foreign.ValueLayout.JAVA_BOOLEAN;`
- Line 30: `import static java.lang.foreign.ValueLayout.JAVA_CHAR;`
- Line 31: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 32: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 33: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`
- Line 34: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.upcallHandle;`
- Line 35: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.upcallStub;`
- Line 36: `import static org.elasticsearch.nativeaccess.jdk.MemorySegmentUtil.varHandleWithoutOffset;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkLinuxCLibrary.java

### Concurrency Issue (1)
- Line 59: `private static final MemoryLayout layout = MemoryLayout.structLayout(JAVA_SHORT, paddingLayout(6), ADDRESS);`

### Exception Handling (1)
- Line 41: `throw new UnsupportedOperationException(`

### Unused Code (17)
- Line 12: `import org.elasticsearch.nativeaccess.lib.LinuxCLibrary;`
- Line 14: `import java.lang.foreign.Arena;`
- Line 15: `import java.lang.foreign.FunctionDescriptor;`
- Line 16: `import java.lang.foreign.Linker;`
- Line 17: `import java.lang.foreign.MemoryLayout;`
- Line 18: `import java.lang.foreign.MemorySegment;`
- Line 19: `import java.lang.invoke.MethodHandle;`
- Line 21: `import static java.lang.foreign.MemoryLayout.paddingLayout;`
- Line 22: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 23: `import static java.lang.foreign.ValueLayout.JAVA_BYTE;`
- Line 24: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 25: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 26: `import static java.lang.foreign.ValueLayout.JAVA_SHORT;`
- Line 27: `import static org.elasticsearch.nativeaccess.jdk.JdkPosixCLibrary.CAPTURE_ERRNO_OPTION;`
- Line 28: `import static org.elasticsearch.nativeaccess.jdk.JdkPosixCLibrary.downcallHandleWithErrno;`
- Line 29: `import static org.elasticsearch.nativeaccess.jdk.JdkPosixCLibrary.errnoState;`
- Line 30: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkMacCLibrary.java

### Unused Code (10)
- Line 12: `import org.elasticsearch.nativeaccess.lib.MacCLibrary;`
- Line 14: `import java.lang.foreign.Arena;`
- Line 15: `import java.lang.foreign.FunctionDescriptor;`
- Line 16: `import java.lang.foreign.MemorySegment;`
- Line 17: `import java.lang.foreign.ValueLayout;`
- Line 18: `import java.lang.invoke.MethodHandle;`
- Line 20: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 21: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 22: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 23: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkNativeLibraryProvider.java

### Unused Code (9)
- Line 12: `import org.elasticsearch.nativeaccess.lib.JavaLibrary;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.Kernel32Library;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.LinuxCLibrary;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.MacCLibrary;`
- Line 16: `import org.elasticsearch.nativeaccess.lib.NativeLibraryProvider;`
- Line 17: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary;`
- Line 18: `import org.elasticsearch.nativeaccess.lib.VectorLibrary;`
- Line 19: `import org.elasticsearch.nativeaccess.lib.ZstdLibrary;`
- Line 21: `import java.util.Map;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkPosixCLibrary.java

### Concurrency Issue (3)
- Line 38: `private static final Logger logger = LogManager.getLogger(JdkPosixCLibrary.class);`
- Line 284: `private static final MemoryLayout layout = MemoryLayout.structLayout(JAVA_LONG, JAVA_LONG);`
- Line 345: `private static final MemoryLayout layout = MemoryLayout.structLayout(JAVA_INT, JAVA_INT, JAVA_LONG, JAVA_LONG, JAVA_LONG);`

### Unused Code (21)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.PosixCLibrary;`
- Line 17: `import java.lang.foreign.Arena;`
- Line 18: `import java.lang.foreign.FunctionDescriptor;`
- Line 19: `import java.lang.foreign.Linker;`
- Line 20: `import java.lang.foreign.MemoryLayout;`
- Line 21: `import java.lang.foreign.MemorySegment;`
- Line 22: `import java.lang.foreign.StructLayout;`
- Line 23: `import java.lang.invoke.MethodHandle;`
- Line 24: `import java.lang.invoke.MethodHandles;`
- Line 25: `import java.lang.invoke.VarHandle;`
- Line 27: `import static java.lang.foreign.MemoryLayout.PathElement.groupElement;`
- Line 28: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 29: `import static java.lang.foreign.ValueLayout.JAVA_BYTE;`
- Line 30: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 31: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 32: `import static java.lang.foreign.ValueLayout.JAVA_SHORT;`
- Line 33: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`
- Line 34: `import static org.elasticsearch.nativeaccess.jdk.MemorySegmentUtil.varHandleWithoutOffset;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkVectorLibrary.java

### Exception Handling (1)
- Line 153: `throw new RuntimeException(e);`

### Unused Code (13)
- Line 12: `import org.elasticsearch.logging.LogManager;`
- Line 13: `import org.elasticsearch.logging.Logger;`
- Line 14: `import org.elasticsearch.nativeaccess.VectorSimilarityFunctions;`
- Line 15: `import org.elasticsearch.nativeaccess.lib.LoaderHelper;`
- Line 16: `import org.elasticsearch.nativeaccess.lib.VectorLibrary;`
- Line 18: `import java.lang.foreign.FunctionDescriptor;`
- Line 19: `import java.lang.foreign.MemorySegment;`
- Line 20: `import java.lang.invoke.MethodHandle;`
- Line 21: `import java.lang.invoke.MethodHandles;`
- Line 22: `import java.lang.invoke.MethodType;`
- Line 24: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 25: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 26: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/JdkZstdLibrary.java

### Unused Code (11)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`
- Line 13: `import org.elasticsearch.nativeaccess.lib.LoaderHelper;`
- Line 14: `import org.elasticsearch.nativeaccess.lib.ZstdLibrary;`
- Line 16: `import java.lang.foreign.FunctionDescriptor;`
- Line 17: `import java.lang.foreign.MemorySegment;`
- Line 18: `import java.lang.invoke.MethodHandle;`
- Line 20: `import static java.lang.foreign.ValueLayout.ADDRESS;`
- Line 21: `import static java.lang.foreign.ValueLayout.JAVA_BOOLEAN;`
- Line 22: `import static java.lang.foreign.ValueLayout.JAVA_INT;`
- Line 23: `import static java.lang.foreign.ValueLayout.JAVA_LONG;`
- Line 24: `import static org.elasticsearch.nativeaccess.jdk.LinkerHelper.downcallHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/LinkerHelper.java

### Concurrency Issue (1)
- Line 24: `private static final Linker LINKER = Linker.nativeLinker();`

### Unused Code (7)
- Line 12: `import java.lang.foreign.Arena;`
- Line 13: `import java.lang.foreign.FunctionDescriptor;`
- Line 14: `import java.lang.foreign.Linker;`
- Line 15: `import java.lang.foreign.MemorySegment;`
- Line 16: `import java.lang.foreign.SymbolLookup;`
- Line 17: `import java.lang.invoke.MethodHandle;`
- Line 18: `import java.lang.invoke.MethodHandles;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/LinkerHelperUtil.java

### Unused Code (1)
- Line 12: `import java.lang.foreign.Linker;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/jdk/MemorySegmentUtil.java

### Unused Code (4)
- Line 12: `import java.lang.foreign.Arena;`
- Line 13: `import java.lang.foreign.MemoryLayout;`
- Line 14: `import java.lang.foreign.MemorySegment;`
- Line 15: `import java.lang.invoke.VarHandle;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/JavaLibrary.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/Kernel32Library.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.nativeaccess.WindowsFunctions.ConsoleCtrlHandler;`
- Line 14: `import java.util.function.IntConsumer;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/LoaderHelper.java

### Concurrency Issue (1)
- Line 20: `public static final Path platformLibDir = findPlatformLibDir();`

### Unused Code (3)
- Line 12: `import java.nio.file.Files;`
- Line 13: `import java.nio.file.Path;`
- Line 14: `import java.nio.file.Paths;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/NativeLibraryProvider.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.nativeaccess.jdk.JdkNativeLibraryProvider;`
- Line 14: `import java.util.Map;`
- Line 15: `import java.util.function.Supplier;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/PosixCLibrary.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/VectorLibrary.java

### Unused Code (2)
- Line 12: `import org.elasticsearch.core.Nullable;`
- Line 13: `import org.elasticsearch.nativeaccess.VectorSimilarityFunctions;`

## ../libs/native/src/main/java/org/elasticsearch/nativeaccess/lib/ZstdLibrary.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.nativeaccess.CloseableByteBuffer;`

## ../libs/native/src/main22/java/org/elasticsearch/nativeaccess/jdk/ArenaUtil.java

### Unused Code (4)
- Line 12: `import java.lang.foreign.Arena;`
- Line 13: `import java.lang.foreign.MemoryLayout;`
- Line 14: `import java.lang.foreign.MemorySegment;`
- Line 15: `import java.nio.charset.Charset;`

## ../libs/native/src/main22/java/org/elasticsearch/nativeaccess/jdk/LinkerHelperUtil.java

### Unused Code (1)
- Line 12: `import java.lang.foreign.Linker;`

## ../libs/native/src/main22/java/org/elasticsearch/nativeaccess/jdk/MemorySegmentUtil.java

### Unused Code (5)
- Line 12: `import java.lang.foreign.Arena;`
- Line 13: `import java.lang.foreign.MemoryLayout;`
- Line 14: `import java.lang.foreign.MemorySegment;`
- Line 15: `import java.lang.invoke.MethodHandles;`
- Line 16: `import java.lang.invoke.VarHandle;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/PreallocateTests.java

### Unused Code (6)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.junit.Before;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.nio.file.Path;`
- Line 17: `import java.util.OptionalLong;`
- Line 19: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/ProcessLimitsTests.java

### Concurrency Issue (1)
- Line 26: `private static final NativeAccess nativeAccess = NativeAccess.instance();`

### Unused Code (8)
- Line 12: `import org.apache.lucene.util.Constants;`
- Line 13: `import org.elasticsearch.core.PathUtils;`
- Line 14: `import org.elasticsearch.test.ESTestCase;`
- Line 16: `import java.io.IOException;`
- Line 17: `import java.nio.file.Files;`
- Line 18: `import java.util.List;`
- Line 20: `import static org.hamcrest.Matchers.equalTo;`
- Line 21: `import static org.hamcrest.Matchers.greaterThanOrEqualTo;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/SystemCallFilterTests.java

### Exception Handling (1)
- Line 41: `throw new RuntimeException("unable to forcefully apply system call filter to test thread", e);`

### Unused Code (4)
- Line 12: `import org.apache.lucene.util.Constants;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import static org.apache.lucene.tests.util.LuceneTestCase.assumeTrue;`
- Line 16: `import static org.junit.Assert.fail;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/VectorSimilarityFunctionsTests.java

### Unused Code (4)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import java.util.Optional;`
- Line 16: `import static org.elasticsearch.test.hamcrest.OptionalMatchers.isPresent;`
- Line 17: `import static org.hamcrest.Matchers.not;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/VectorSystemPropertyTests.java

### Unused Code (18)
- Line 12: `import org.apache.lucene.util.Constants;`
- Line 13: `import org.elasticsearch.core.SuppressForbidden;`
- Line 14: `import org.elasticsearch.test.ESTestCase;`
- Line 15: `import org.elasticsearch.test.ESTestCase.WithoutSecurityManager;`
- Line 16: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 17: `import org.elasticsearch.test.jar.JarUtils;`
- Line 18: `import org.junit.BeforeClass;`
- Line 20: `import java.io.File;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.HashMap;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.concurrent.TimeUnit;`
- Line 26: `import static java.nio.charset.StandardCharsets.UTF_8;`
- Line 27: `import static org.elasticsearch.nativeaccess.PosixNativeAccess.ENABLE_JDK_VECTOR_LIBRARY;`
- Line 28: `import static org.hamcrest.Matchers.containsString;`
- Line 29: `import static org.hamcrest.Matchers.equalTo;`
- Line 75: `import org.elasticsearch.nativeaccess.NativeAccess;`
- Line 76: `import org.elasticsearch.common.logging.LogConfigurator;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/ZstdTests.java

### Unused Code (5)
- Line 12: `import org.elasticsearch.test.ESTestCase;`
- Line 13: `import org.hamcrest.Matchers;`
- Line 14: `import org.junit.BeforeClass;`
- Line 16: `import java.util.Arrays;`
- Line 18: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/native/src/test/java/org/elasticsearch/nativeaccess/jdk/JDKVectorLibraryTests.java

### Exception Handling (2)
- Line 122: `throw new RuntimeException(e);`
- Line 136: `throw new RuntimeException(e);`

### Unused Code (8)
- Line 12: `import com.carrotsearch.randomizedtesting.annotations.ParametersFactory;`
- Line 14: `import org.elasticsearch.nativeaccess.VectorSimilarityFunctionsTests;`
- Line 15: `import org.junit.AfterClass;`
- Line 16: `import org.junit.BeforeClass;`
- Line 18: `import java.lang.foreign.Arena;`
- Line 19: `import java.lang.foreign.MemorySegment;`
- Line 20: `import java.util.stream.IntStream;`
- Line 22: `import static org.hamcrest.Matchers.containsString;`

## ../libs/plugin-analysis-api/src/main/java/org/elasticsearch/plugin/analysis/AnalysisMode.java

### Exception Handling (2)
- Line 26: `throw new IllegalStateException("Cannot merge SEARCH_TIME and INDEX_TIME analysis mode.");`
- Line 38: `throw new IllegalStateException("Cannot merge SEARCH_TIME and INDEX_TIME analysis mode.");`

## ../libs/plugin-analysis-api/src/main/java/org/elasticsearch/plugin/analysis/AnalyzerFactory.java

### Unused Code (3)
- Line 12: `import org.apache.lucene.analysis.Analyzer;`
- Line 13: `import org.elasticsearch.plugin.Extensible;`
- Line 14: `import org.elasticsearch.plugin.Nameable;`

## ../libs/plugin-analysis-api/src/main/java/org/elasticsearch/plugin/analysis/CharFilterFactory.java

### Unused Code (3)
- Line 12: `import org.elasticsearch.plugin.Extensible;`
- Line 13: `import org.elasticsearch.plugin.Nameable;`
- Line 15: `import java.io.Reader;`

## ../libs/plugin-analysis-api/src/main/java/org/elasticsearch/plugin/analysis/TokenFilterFactory.java

### Unused Code (3)
- Line 12: `import org.apache.lucene.analysis.TokenStream;`
- Line 13: `import org.elasticsearch.plugin.Extensible;`
- Line 14: `import org.elasticsearch.plugin.Nameable;`

## ../libs/plugin-analysis-api/src/main/java/org/elasticsearch/plugin/analysis/TokenizerFactory.java

### Unused Code (3)
- Line 12: `import org.apache.lucene.analysis.Tokenizer;`
- Line 13: `import org.elasticsearch.plugin.Extensible;`
- Line 14: `import org.elasticsearch.plugin.Nameable;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/Extensible.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.Retention;`
- Line 13: `import java.lang.annotation.RetentionPolicy;`
- Line 14: `import java.lang.annotation.Target;`
- Line 16: `import static java.lang.annotation.ElementType.TYPE;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/Inject.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/NamedComponent.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/AnalysisSettings.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.Retention;`
- Line 13: `import java.lang.annotation.RetentionPolicy;`
- Line 14: `import java.lang.annotation.Target;`
- Line 16: `import static java.lang.annotation.ElementType.TYPE;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/BooleanSetting.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/IntSetting.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/ListSetting.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/LongSetting.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-api/src/main/java/org/elasticsearch/plugin/settings/StringSetting.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/plugin-scanner/src/main/java/org/elasticsearch/plugin/scanner/AnnotatedHierarchyVisitor.java

### Unused Code (9)
- Line 26: `private String currentClassName;`
- Line 12: `import org.objectweb.asm.AnnotationVisitor;`
- Line 13: `import org.objectweb.asm.ClassVisitor;`
- Line 14: `import org.objectweb.asm.Opcodes;`
- Line 16: `import java.util.HashMap;`
- Line 17: `import java.util.HashSet;`
- Line 18: `import java.util.Map;`
- Line 19: `import java.util.Set;`
- Line 20: `import java.util.function.Function;`

## ../libs/plugin-scanner/src/main/java/org/elasticsearch/plugin/scanner/ClassReaders.java

### Exception Handling (4)
- Line 51: `throw new UncheckedIOException(e);`
- Line 86: `throw new UncheckedIOException(e);`
- Line 100: `throw new UncheckedIOException(ex);`
- Line 105: `throw new UncheckedIOException(e);`

### Unused Code (18)
- Line 12: `import org.elasticsearch.core.PathUtils;`
- Line 13: `import org.objectweb.asm.ClassReader;`
- Line 15: `import java.io.IOException;`
- Line 16: `import java.io.InputStream;`
- Line 17: `import java.io.UncheckedIOException;`
- Line 18: `import java.net.URISyntaxException;`
- Line 19: `import java.net.URL;`
- Line 20: `import java.nio.file.FileSystem;`
- Line 21: `import java.nio.file.FileSystems;`
- Line 22: `import java.nio.file.Files;`
- Line 23: `import java.nio.file.Path;`
- Line 24: `import java.nio.file.Paths;`
- Line 25: `import java.util.Arrays;`
- Line 26: `import java.util.Collections;`
- Line 27: `import java.util.List;`
- Line 28: `import java.util.Set;`
- Line 29: `import java.util.stream.Collectors;`
- Line 30: `import java.util.stream.Stream;`

## ../libs/plugin-scanner/src/main/java/org/elasticsearch/plugin/scanner/ClassScanner.java

### Unused Code (10)
- Line 12: `import org.objectweb.asm.AnnotationVisitor;`
- Line 13: `import org.objectweb.asm.ClassReader;`
- Line 15: `import java.util.ArrayDeque;`
- Line 16: `import java.util.Deque;`
- Line 17: `import java.util.HashMap;`
- Line 18: `import java.util.HashSet;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`
- Line 21: `import java.util.Set;`
- Line 22: `import java.util.function.BiFunction;`

## ../libs/plugin-scanner/src/main/java/org/elasticsearch/plugin/scanner/NamedComponentScanner.java

### Unused Code (15)
- Line 12: `import org.elasticsearch.plugin.Extensible;`
- Line 13: `import org.elasticsearch.plugin.NamedComponent;`
- Line 14: `import org.elasticsearch.xcontent.XContentBuilder;`
- Line 15: `import org.elasticsearch.xcontent.XContentFactory;`
- Line 16: `import org.objectweb.asm.AnnotationVisitor;`
- Line 17: `import org.objectweb.asm.ClassReader;`
- Line 18: `import org.objectweb.asm.Opcodes;`
- Line 19: `import org.objectweb.asm.Type;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.io.OutputStream;`
- Line 23: `import java.nio.file.Files;`
- Line 24: `import java.nio.file.Path;`
- Line 25: `import java.util.HashMap;`
- Line 26: `import java.util.List;`
- Line 27: `import java.util.Map;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/AnnotatedHierarchyVisitorTests.java

### Unused Code (18)
- Line 12: `import org.elasticsearch.plugin.Extensible;`
- Line 13: `import org.elasticsearch.plugin.NamedComponent;`
- Line 14: `import org.elasticsearch.plugin.scanner.test_model.ExtensibleClass;`
- Line 15: `import org.elasticsearch.plugin.scanner.test_model.ExtensibleInterface;`
- Line 16: `import org.elasticsearch.plugin.scanner.test_model.ImplementingExtensible;`
- Line 17: `import org.elasticsearch.plugin.scanner.test_model.SubClass;`
- Line 18: `import org.elasticsearch.test.ESTestCase;`
- Line 19: `import org.junit.Before;`
- Line 20: `import org.objectweb.asm.ClassReader;`
- Line 21: `import org.objectweb.asm.Type;`
- Line 23: `import java.io.IOException;`
- Line 24: `import java.io.InputStream;`
- Line 25: `import java.net.URISyntaxException;`
- Line 26: `import java.util.HashSet;`
- Line 27: `import java.util.Map;`
- Line 28: `import java.util.Set;`
- Line 30: `import static org.hamcrest.MatcherAssert.assertThat;`
- Line 31: `import static org.hamcrest.Matchers.equalTo;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/ClassReadersTests.java

### Unused Code (13)
- Line 12: `import org.elasticsearch.core.IOUtils;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 15: `import org.elasticsearch.test.jar.JarUtils;`
- Line 16: `import org.hamcrest.Matchers;`
- Line 17: `import org.objectweb.asm.ClassReader;`
- Line 19: `import java.io.IOException;`
- Line 20: `import java.nio.file.Files;`
- Line 21: `import java.nio.file.Path;`
- Line 22: `import java.util.List;`
- Line 23: `import java.util.Map;`
- Line 24: `import java.util.stream.Collectors;`
- Line 25: `import java.util.stream.Stream;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/ClassScannerTests.java

### Unused Code (8)
- Line 12: `import org.elasticsearch.plugin.Extensible;`
- Line 13: `import org.elasticsearch.test.ESTestCase;`
- Line 14: `import org.hamcrest.Matchers;`
- Line 15: `import org.objectweb.asm.ClassReader;`
- Line 16: `import org.objectweb.asm.Type;`
- Line 18: `import java.io.IOException;`
- Line 19: `import java.util.List;`
- Line 20: `import java.util.Map;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/NamedComponentScannerTests.java

### Exception Handling (2)
- Line 214: `throw new UncheckedIOException(e);`
- Line 218: `throw new RuntimeException(e);`

### Unused Code (34)
- Line 12: `import org.elasticsearch.core.IOUtils;`
- Line 13: `import org.elasticsearch.plugin.scanner.test_model.ExtensibleClass;`
- Line 14: `import org.elasticsearch.plugin.scanner.test_model.ExtensibleInterface;`
- Line 15: `import org.elasticsearch.plugin.scanner.test_model.TestNamedComponent;`
- Line 16: `import org.elasticsearch.test.ESTestCase;`
- Line 17: `import org.elasticsearch.test.compiler.InMemoryJavaCompiler;`
- Line 18: `import org.elasticsearch.test.jar.JarUtils;`
- Line 19: `import org.objectweb.asm.ClassReader;`
- Line 21: `import java.io.IOException;`
- Line 22: `import java.io.InputStream;`
- Line 23: `import java.io.UncheckedIOException;`
- Line 24: `import java.net.URISyntaxException;`
- Line 25: `import java.nio.file.Files;`
- Line 26: `import java.nio.file.Path;`
- Line 27: `import java.util.Arrays;`
- Line 28: `import java.util.HashMap;`
- Line 29: `import java.util.LinkedHashMap;`
- Line 30: `import java.util.List;`
- Line 31: `import java.util.Map;`
- Line 32: `import java.util.stream.Collectors;`
- Line 33: `import java.util.stream.Stream;`
- Line 35: `import static org.hamcrest.Matchers.equalTo;`
- Line 67: `import org.elasticsearch.plugin.*;`
- Line 68: `import org.elasticsearch.plugin.scanner.test_model.*;`
- Line 73: `import org.elasticsearch.plugin.*;`
- Line 74: `import org.elasticsearch.plugin.scanner.test_model.*;`
- Line 113: `import org.elasticsearch.plugin.*;`
- Line 114: `import org.elasticsearch.plugin.scanner.test_model.*;`
- Line 121: `import org.elasticsearch.plugin.*;`
- Line 122: `import org.elasticsearch.plugin.scanner.test_model.*;`
- Line 128: `import org.elasticsearch.plugin.*;`
- Line 129: `import org.elasticsearch.plugin.scanner.test_model.*;`
- Line 136: `import org.elasticsearch.plugin.*;`
- Line 137: `import org.elasticsearch.plugin.scanner.test_model.*;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/test_model/ExtensibleClass.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.Extensible;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/test_model/ExtensibleInterface.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.Extensible;`

## ../libs/plugin-scanner/src/test/java/org/elasticsearch/plugin/scanner/test_model/TestNamedComponent.java

### Unused Code (1)
- Line 12: `import org.elasticsearch.plugin.NamedComponent;`

## ../libs/secure-sm/src/main/java/org/elasticsearch/secure_sm/SecureSM.java

### Concurrency Issue (4)
- Line 154: `private static final Permission MODIFY_THREAD_PERMISSION = new RuntimePermission("modifyThread");`
- Line 155: `private static final Permission MODIFY_ARBITRARY_THREAD_PERMISSION = new ThreadPermission("modifyArbitraryThread");`
- Line 186: `private static final Permission MODIFY_THREADGROUP_PERMISSION = new RuntimePermission("modifyThreadGroup");`
- Line 187: `private static final Permission MODIFY_ARBITRARY_THREADGROUP_PERMISSION = new ThreadPermission("modifyArbitraryThreadGroup");`

### Exception Handling (1)
- Line 258: `throw new SecurityException(exitMethodHit + " calls are not allowed");`

### Unused Code (4)
- Line 12: `import java.security.AccessController;`
- Line 13: `import java.security.Permission;`
- Line 14: `import java.security.PrivilegedAction;`
- Line 15: `import java.util.Objects;`

## ../libs/secure-sm/src/main/java/org/elasticsearch/secure_sm/SuppressForbidden.java

### Unused Code (4)
- Line 12: `import java.lang.annotation.ElementType;`
- Line 13: `import java.lang.annotation.Retention;`
- Line 14: `import java.lang.annotation.RetentionPolicy;`
- Line 15: `import java.lang.annotation.Target;`

## ../libs/secure-sm/src/main/java/org/elasticsearch/secure_sm/ThreadPermission.java

### Unused Code (1)
- Line 12: `import java.security.BasicPermission;`

## ../libs/secure-sm/src/test/java/org/elasticsearch/secure_sm/SecureSMTests.java

### Exception Handling (2)
- Line 64: `} catch (SecurityException expected) {}`
- Line 135: `} catch (SecurityException expected2) {}`

### Unused Code (15)
- Line 12: `import com.carrotsearch.randomizedtesting.JUnit3MethodProvider;`
- Line 13: `import com.carrotsearch.randomizedtesting.RandomizedRunner;`
- Line 14: `import com.carrotsearch.randomizedtesting.RandomizedTest;`
- Line 15: `import com.carrotsearch.randomizedtesting.annotations.TestMethodProviders;`
- Line 17: `import org.elasticsearch.jdk.RuntimeVersionFeature;`
- Line 18: `import org.junit.BeforeClass;`
- Line 19: `import org.junit.runner.RunWith;`
- Line 21: `import java.security.Permission;`
- Line 22: `import java.security.Policy;`
- Line 23: `import java.security.ProtectionDomain;`
- Line 24: `import java.util.ArrayList;`
- Line 25: `import java.util.List;`
- Line 26: `import java.util.Set;`
- Line 27: `import java.util.concurrent.atomic.AtomicBoolean;`
- Line 28: `import java.util.stream.Collectors;`

## ../libs/secure-sm/src/test/java/org/elasticsearch/secure_sm/ThreadPermissionTests.java

### Unused Code (2)
- Line 12: `import junit.framework.TestCase;`
- Line 14: `import java.security.AllPermission;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/ESVectorUtil.java

### Concurrency Issue (1)
- Line 42: `private static final ESVectorUtilSupport IMPL = ESVectorizationProvider.getInstance().getVectorUtilSupport();`

### Exception Handling (6)
- Line 46: `throw new IllegalArgumentException("vector dimensions incompatible: " + q.length + "!= " + B_QUERY + " x " + d.length);`
- Line 62: `throw new IllegalArgumentException("vector dimensions incompatible: " + q.length + "!= " + Byte.SIZE + " x " + d.length);`
- Line 78: `throw new IllegalArgumentException("vector dimensions incompatible: " + q.length + "!= " + Byte.SIZE + " x " + d.length);`
- Line 91: `throw new IllegalArgumentException("vector dimensions incompatible: " + q.length + "!= " + d.length);`
- Line 105: `throw new IllegalArgumentException("vector dimensions differ: " + a.length + "!=" + b.length);`
- Line 115: `throw new RuntimeException(e);`

### Unused Code (8)
- Line 12: `import org.apache.lucene.util.BitUtil;`
- Line 13: `import org.apache.lucene.util.Constants;`
- Line 14: `import org.elasticsearch.simdvec.internal.vectorization.ESVectorUtilSupport;`
- Line 15: `import org.elasticsearch.simdvec.internal.vectorization.ESVectorizationProvider;`
- Line 17: `import java.lang.invoke.MethodHandle;`
- Line 18: `import java.lang.invoke.MethodHandles;`
- Line 19: `import java.lang.invoke.MethodType;`
- Line 21: `import static org.elasticsearch.simdvec.internal.vectorization.ESVectorUtilSupport.B_QUERY;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/VectorScorerFactory.java

### Unused Code (6)
- Line 12: `import org.apache.lucene.index.VectorSimilarityFunction;`
- Line 13: `import org.apache.lucene.store.IndexInput;`
- Line 14: `import org.apache.lucene.util.hnsw.RandomVectorScorer;`
- Line 15: `import org.apache.lucene.util.hnsw.RandomVectorScorerSupplier;`
- Line 16: `import org.apache.lucene.util.quantization.QuantizedByteVectorValues;`
- Line 18: `import java.util.Optional;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/VectorScorerFactoryImpl.java

### Exception Handling (2)
- Line 31: `throw new UnsupportedOperationException("should not reach here");`
- Line 40: `throw new UnsupportedOperationException("should not reach here");`

### Unused Code (6)
- Line 12: `import org.apache.lucene.index.VectorSimilarityFunction;`
- Line 13: `import org.apache.lucene.store.IndexInput;`
- Line 14: `import org.apache.lucene.util.hnsw.RandomVectorScorer;`
- Line 15: `import org.apache.lucene.util.hnsw.RandomVectorScorerSupplier;`
- Line 16: `import org.apache.lucene.util.quantization.QuantizedByteVectorValues;`
- Line 18: `import java.util.Optional;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/VectorSimilarityType.java

### Unused Code (1)
- Line 12: `import org.apache.lucene.index.VectorSimilarityFunction;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/vectorization/DefaultESVectorUtilSupport.java

### Unused Code (2)
- Line 12: `import org.apache.lucene.util.BitUtil;`
- Line 13: `import org.apache.lucene.util.Constants;`

## ../libs/simdvec/src/main/java/org/elasticsearch/simdvec/internal/vectorization/ESVectorizationProvider.java

### Unused Code (1)
- Line 12: `import java.util.Objects;`

## ../libs/simdvec/src/main21/java/org/elasticsearch/simdvec/VectorScorerFactoryImpl.java

### Exception Handling (1)
- Line 68: `throw new IllegalArgumentException("input length is less than expected vector data");`

### Unused Code (13)
- Line 12: `import org.apache.lucene.index.VectorSimilarityFunction;`
- Line 13: `import org.apache.lucene.store.FilterIndexInput;`
- Line 14: `import org.apache.lucene.store.IndexInput;`
- Line 15: `import org.apache.lucene.store.MemorySegmentAccessInput;`
- Line 16: `import org.apache.lucene.util.hnsw.RandomVectorScorer;`
- Line 17: `import org.apache.lucene.util.hnsw.RandomVectorScorerSupplier;`
- Line 18: `import org.apache.lucene.util.quantization.QuantizedByteVectorValues;`
- Line 19: `import org.elasticsearch.nativeaccess.NativeAccess;`
- Line 20: `import org.elasticsearch.simdvec.internal.Int7SQVectorScorer;`
- Line 21: `import org.elasticsearch.simdvec.internal.Int7SQVectorScorerSupplier.DotProductSupplier;`
- Line 22: `import org.elasticsearch.simdvec.internal.Int7SQVectorScorerSupplier.EuclideanSupplier;`
- Line 23: `import org.elasticsearch.simdvec.internal.Int7SQVectorScorerSupplier.MaxInnerProductSupplier;`
- Line 25: `import java.util.Optional;`