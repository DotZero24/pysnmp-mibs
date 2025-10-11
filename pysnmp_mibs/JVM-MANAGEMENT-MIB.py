# SNMP MIB module (JVM-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/oracle/JVM-MANAGEMENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:31 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

jvmMgtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1)
)
if mibBuilder.loadTexts:
    jvmMgtMIB.setRevisions(
        ("2004-03-04 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JvmUnsigned64TC(TextualConvention, Counter64):
    status = "current"


class JvmJavaObjectNameTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class JvmPathElementTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class JvmArgValueTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class JvmVerboseLevelTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("silent", 1),
          ("verbose", 2))
    )



class JvmImplSupportStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("supported", 2))
    )



class JvmImplOptFeatureStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("enabled", 3),
          ("disabled", 4))
    )



class JvmTimeMillis64TC(TextualConvention, Counter64):
    status = "current"


class JvmTimeNanos64TC(TextualConvention, Counter64):
    status = "current"


class JvmPositive32TC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class JvmManagedMemoryTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonheap", 1),
          ("heap", 2))
    )



class JvmValidityStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )



class JvmThreadStateTC(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("inNative", 1),
          ("suspended", 2),
          ("newThread", 3),
          ("runnable", 4),
          ("blocked", 5),
          ("terminated", 6),
          ("waiting", 7),
          ("timedWaiting", 8),
          ("other", 9))
    )


class JvmIndex64TC(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Jmgt_ObjectIdentity = ObjectIdentity
jmgt = _Jmgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145)
)
_Standard_ObjectIdentity = ObjectIdentity
standard = _Standard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3)
)
_JvmMgtMIBObjects_ObjectIdentity = ObjectIdentity
jvmMgtMIBObjects = _JvmMgtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1)
)
_JvmClassLoading_ObjectIdentity = ObjectIdentity
jvmClassLoading = _JvmClassLoading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1)
)
_JvmClassesLoadedCount_Type = Gauge32
_JvmClassesLoadedCount_Object = MibScalar
jvmClassesLoadedCount = _JvmClassesLoadedCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 1),
    _JvmClassesLoadedCount_Type()
)
jvmClassesLoadedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmClassesLoadedCount.setStatus("current")
_JvmClassesTotalLoadedCount_Type = Counter64
_JvmClassesTotalLoadedCount_Object = MibScalar
jvmClassesTotalLoadedCount = _JvmClassesTotalLoadedCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 2),
    _JvmClassesTotalLoadedCount_Type()
)
jvmClassesTotalLoadedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmClassesTotalLoadedCount.setStatus("current")
_JvmClassesUnloadedCount_Type = Counter64
_JvmClassesUnloadedCount_Object = MibScalar
jvmClassesUnloadedCount = _JvmClassesUnloadedCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 3),
    _JvmClassesUnloadedCount_Type()
)
jvmClassesUnloadedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmClassesUnloadedCount.setStatus("current")


class _JvmClassesVerboseLevel_Type(JvmVerboseLevelTC):
    """Custom type jvmClassesVerboseLevel based on JvmVerboseLevelTC"""
    defaultValue = 1


_JvmClassesVerboseLevel_Type.__name__ = "JvmVerboseLevelTC"
_JvmClassesVerboseLevel_Object = MibScalar
jvmClassesVerboseLevel = _JvmClassesVerboseLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 4),
    _JvmClassesVerboseLevel_Type()
)
jvmClassesVerboseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmClassesVerboseLevel.setStatus("current")
_JvmMemory_ObjectIdentity = ObjectIdentity
jvmMemory = _JvmMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2)
)
_JvmMemoryPendingFinalCount_Type = Gauge32
_JvmMemoryPendingFinalCount_Object = MibScalar
jvmMemoryPendingFinalCount = _JvmMemoryPendingFinalCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 1),
    _JvmMemoryPendingFinalCount_Type()
)
jvmMemoryPendingFinalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryPendingFinalCount.setStatus("current")
_JvmMemoryGCVerboseLevel_Type = JvmVerboseLevelTC
_JvmMemoryGCVerboseLevel_Object = MibScalar
jvmMemoryGCVerboseLevel = _JvmMemoryGCVerboseLevel_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 2),
    _JvmMemoryGCVerboseLevel_Type()
)
jvmMemoryGCVerboseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmMemoryGCVerboseLevel.setStatus("current")


class _JvmMemoryGCCall_Type(Integer32):
    """Custom type jvmMemoryGCCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("supported", 2),
          ("start", 3),
          ("started", 4),
          ("failed", 5))
    )


_JvmMemoryGCCall_Type.__name__ = "Integer32"
_JvmMemoryGCCall_Object = MibScalar
jvmMemoryGCCall = _JvmMemoryGCCall_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 3),
    _JvmMemoryGCCall_Type()
)
jvmMemoryGCCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmMemoryGCCall.setStatus("current")
_JvmMemoryHeapInitSize_Type = JvmUnsigned64TC
_JvmMemoryHeapInitSize_Object = MibScalar
jvmMemoryHeapInitSize = _JvmMemoryHeapInitSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 10),
    _JvmMemoryHeapInitSize_Type()
)
jvmMemoryHeapInitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryHeapInitSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryHeapInitSize.setUnits("bytes")
_JvmMemoryHeapUsed_Type = JvmUnsigned64TC
_JvmMemoryHeapUsed_Object = MibScalar
jvmMemoryHeapUsed = _JvmMemoryHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 11),
    _JvmMemoryHeapUsed_Type()
)
jvmMemoryHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryHeapUsed.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryHeapUsed.setUnits("bytes")
_JvmMemoryHeapCommitted_Type = JvmUnsigned64TC
_JvmMemoryHeapCommitted_Object = MibScalar
jvmMemoryHeapCommitted = _JvmMemoryHeapCommitted_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 12),
    _JvmMemoryHeapCommitted_Type()
)
jvmMemoryHeapCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryHeapCommitted.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryHeapCommitted.setUnits("bytes")
_JvmMemoryHeapMaxSize_Type = JvmUnsigned64TC
_JvmMemoryHeapMaxSize_Object = MibScalar
jvmMemoryHeapMaxSize = _JvmMemoryHeapMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 13),
    _JvmMemoryHeapMaxSize_Type()
)
jvmMemoryHeapMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryHeapMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryHeapMaxSize.setUnits("bytes")
_JvmMemoryNonHeapInitSize_Type = JvmUnsigned64TC
_JvmMemoryNonHeapInitSize_Object = MibScalar
jvmMemoryNonHeapInitSize = _JvmMemoryNonHeapInitSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 20),
    _JvmMemoryNonHeapInitSize_Type()
)
jvmMemoryNonHeapInitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapInitSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapInitSize.setUnits("bytes")
_JvmMemoryNonHeapUsed_Type = JvmUnsigned64TC
_JvmMemoryNonHeapUsed_Object = MibScalar
jvmMemoryNonHeapUsed = _JvmMemoryNonHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 21),
    _JvmMemoryNonHeapUsed_Type()
)
jvmMemoryNonHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapUsed.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapUsed.setUnits("bytes")
_JvmMemoryNonHeapCommitted_Type = JvmUnsigned64TC
_JvmMemoryNonHeapCommitted_Object = MibScalar
jvmMemoryNonHeapCommitted = _JvmMemoryNonHeapCommitted_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 22),
    _JvmMemoryNonHeapCommitted_Type()
)
jvmMemoryNonHeapCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapCommitted.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapCommitted.setUnits("bytes")
_JvmMemoryNonHeapMaxSize_Type = JvmUnsigned64TC
_JvmMemoryNonHeapMaxSize_Object = MibScalar
jvmMemoryNonHeapMaxSize = _JvmMemoryNonHeapMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 23),
    _JvmMemoryNonHeapMaxSize_Type()
)
jvmMemoryNonHeapMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemoryNonHeapMaxSize.setUnits("bytes")
_JvmMemManagerTable_Object = MibTable
jvmMemManagerTable = _JvmMemManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100)
)
if mibBuilder.loadTexts:
    jvmMemManagerTable.setStatus("current")
_JvmMemManagerEntry_Object = MibTableRow
jvmMemManagerEntry = _JvmMemManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1)
)
jvmMemManagerEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"),
)
if mibBuilder.loadTexts:
    jvmMemManagerEntry.setStatus("current")
_JvmMemManagerIndex_Type = JvmPositive32TC
_JvmMemManagerIndex_Object = MibTableColumn
jvmMemManagerIndex = _JvmMemManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 1),
    _JvmMemManagerIndex_Type()
)
jvmMemManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmMemManagerIndex.setStatus("current")
_JvmMemManagerName_Type = JvmJavaObjectNameTC
_JvmMemManagerName_Object = MibTableColumn
jvmMemManagerName = _JvmMemManagerName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 2),
    _JvmMemManagerName_Type()
)
jvmMemManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemManagerName.setStatus("current")
_JvmMemManagerState_Type = JvmValidityStateTC
_JvmMemManagerState_Object = MibTableColumn
jvmMemManagerState = _JvmMemManagerState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 3),
    _JvmMemManagerState_Type()
)
jvmMemManagerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemManagerState.setStatus("current")
_JvmMemGCTable_Object = MibTable
jvmMemGCTable = _JvmMemGCTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101)
)
if mibBuilder.loadTexts:
    jvmMemGCTable.setStatus("current")
_JvmMemGCEntry_Object = MibTableRow
jvmMemGCEntry = _JvmMemGCEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1)
)
jvmMemGCEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"),
)
if mibBuilder.loadTexts:
    jvmMemGCEntry.setStatus("current")
_JvmMemGCCount_Type = Counter64
_JvmMemGCCount_Object = MibTableColumn
jvmMemGCCount = _JvmMemGCCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1, 2),
    _JvmMemGCCount_Type()
)
jvmMemGCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemGCCount.setStatus("current")


class _JvmMemGCTimeMs_Type(JvmTimeMillis64TC):
    """Custom type jvmMemGCTimeMs based on JvmTimeMillis64TC"""
    defaultValue = 0


_JvmMemGCTimeMs_Type.__name__ = "JvmTimeMillis64TC"
_JvmMemGCTimeMs_Object = MibTableColumn
jvmMemGCTimeMs = _JvmMemGCTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1, 3),
    _JvmMemGCTimeMs_Type()
)
jvmMemGCTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemGCTimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemGCTimeMs.setUnits("milliseconds")
_JvmMemPoolTable_Object = MibTable
jvmMemPoolTable = _JvmMemPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110)
)
if mibBuilder.loadTexts:
    jvmMemPoolTable.setStatus("current")
_JvmMemPoolEntry_Object = MibTableRow
jvmMemPoolEntry = _JvmMemPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1)
)
jvmMemPoolEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmMemPoolIndex"),
)
if mibBuilder.loadTexts:
    jvmMemPoolEntry.setStatus("current")
_JvmMemPoolIndex_Type = JvmPositive32TC
_JvmMemPoolIndex_Object = MibTableColumn
jvmMemPoolIndex = _JvmMemPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 1),
    _JvmMemPoolIndex_Type()
)
jvmMemPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmMemPoolIndex.setStatus("current")
_JvmMemPoolName_Type = JvmJavaObjectNameTC
_JvmMemPoolName_Object = MibTableColumn
jvmMemPoolName = _JvmMemPoolName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 2),
    _JvmMemPoolName_Type()
)
jvmMemPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolName.setStatus("current")
_JvmMemPoolType_Type = JvmManagedMemoryTypeTC
_JvmMemPoolType_Object = MibTableColumn
jvmMemPoolType = _JvmMemPoolType_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 3),
    _JvmMemPoolType_Type()
)
jvmMemPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolType.setStatus("current")
_JvmMemPoolState_Type = JvmValidityStateTC
_JvmMemPoolState_Object = MibTableColumn
jvmMemPoolState = _JvmMemPoolState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 4),
    _JvmMemPoolState_Type()
)
jvmMemPoolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolState.setStatus("current")
_JvmMemPoolPeakReset_Type = JvmTimeMillis64TC
_JvmMemPoolPeakReset_Object = MibTableColumn
jvmMemPoolPeakReset = _JvmMemPoolPeakReset_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 5),
    _JvmMemPoolPeakReset_Type()
)
jvmMemPoolPeakReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmMemPoolPeakReset.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolPeakReset.setUnits("milliseconds")
_JvmMemPoolInitSize_Type = JvmUnsigned64TC
_JvmMemPoolInitSize_Object = MibTableColumn
jvmMemPoolInitSize = _JvmMemPoolInitSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 10),
    _JvmMemPoolInitSize_Type()
)
jvmMemPoolInitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolInitSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolInitSize.setUnits("bytes")
_JvmMemPoolUsed_Type = JvmUnsigned64TC
_JvmMemPoolUsed_Object = MibTableColumn
jvmMemPoolUsed = _JvmMemPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 11),
    _JvmMemPoolUsed_Type()
)
jvmMemPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolUsed.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolUsed.setUnits("bytes")
_JvmMemPoolCommitted_Type = JvmUnsigned64TC
_JvmMemPoolCommitted_Object = MibTableColumn
jvmMemPoolCommitted = _JvmMemPoolCommitted_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 12),
    _JvmMemPoolCommitted_Type()
)
jvmMemPoolCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCommitted.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolCommitted.setUnits("bytes")
_JvmMemPoolMaxSize_Type = JvmUnsigned64TC
_JvmMemPoolMaxSize_Object = MibTableColumn
jvmMemPoolMaxSize = _JvmMemPoolMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 13),
    _JvmMemPoolMaxSize_Type()
)
jvmMemPoolMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolMaxSize.setUnits("bytes")
_JvmMemPoolPeakUsed_Type = JvmUnsigned64TC
_JvmMemPoolPeakUsed_Object = MibTableColumn
jvmMemPoolPeakUsed = _JvmMemPoolPeakUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 21),
    _JvmMemPoolPeakUsed_Type()
)
jvmMemPoolPeakUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolPeakUsed.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolPeakUsed.setUnits("bytes")
_JvmMemPoolPeakCommitted_Type = JvmUnsigned64TC
_JvmMemPoolPeakCommitted_Object = MibTableColumn
jvmMemPoolPeakCommitted = _JvmMemPoolPeakCommitted_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 22),
    _JvmMemPoolPeakCommitted_Type()
)
jvmMemPoolPeakCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolPeakCommitted.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolPeakCommitted.setUnits("bytes")
_JvmMemPoolPeakMaxSize_Type = JvmUnsigned64TC
_JvmMemPoolPeakMaxSize_Object = MibTableColumn
jvmMemPoolPeakMaxSize = _JvmMemPoolPeakMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 23),
    _JvmMemPoolPeakMaxSize_Type()
)
jvmMemPoolPeakMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolPeakMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolPeakMaxSize.setUnits("bytes")
_JvmMemPoolCollectUsed_Type = JvmUnsigned64TC
_JvmMemPoolCollectUsed_Object = MibTableColumn
jvmMemPoolCollectUsed = _JvmMemPoolCollectUsed_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 31),
    _JvmMemPoolCollectUsed_Type()
)
jvmMemPoolCollectUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCollectUsed.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolCollectUsed.setUnits("bytes")
_JvmMemPoolCollectCommitted_Type = JvmUnsigned64TC
_JvmMemPoolCollectCommitted_Object = MibTableColumn
jvmMemPoolCollectCommitted = _JvmMemPoolCollectCommitted_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 32),
    _JvmMemPoolCollectCommitted_Type()
)
jvmMemPoolCollectCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCollectCommitted.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolCollectCommitted.setUnits("bytes")
_JvmMemPoolCollectMaxSize_Type = JvmUnsigned64TC
_JvmMemPoolCollectMaxSize_Object = MibTableColumn
jvmMemPoolCollectMaxSize = _JvmMemPoolCollectMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 33),
    _JvmMemPoolCollectMaxSize_Type()
)
jvmMemPoolCollectMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCollectMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolCollectMaxSize.setUnits("bytes")


class _JvmMemPoolThreshold_Type(JvmUnsigned64TC):
    """Custom type jvmMemPoolThreshold based on JvmUnsigned64TC"""
    defaultValue = 0


_JvmMemPoolThreshold_Type.__name__ = "JvmUnsigned64TC"
_JvmMemPoolThreshold_Object = MibTableColumn
jvmMemPoolThreshold = _JvmMemPoolThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 110),
    _JvmMemPoolThreshold_Type()
)
jvmMemPoolThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmMemPoolThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolThreshold.setUnits("bytes")
_JvmMemPoolThreshdCount_Type = Counter64
_JvmMemPoolThreshdCount_Object = MibTableColumn
jvmMemPoolThreshdCount = _JvmMemPoolThreshdCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 111),
    _JvmMemPoolThreshdCount_Type()
)
jvmMemPoolThreshdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolThreshdCount.setStatus("current")
_JvmMemPoolThreshdSupport_Type = JvmImplSupportStateTC
_JvmMemPoolThreshdSupport_Object = MibTableColumn
jvmMemPoolThreshdSupport = _JvmMemPoolThreshdSupport_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 112),
    _JvmMemPoolThreshdSupport_Type()
)
jvmMemPoolThreshdSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolThreshdSupport.setStatus("current")


class _JvmMemPoolCollectThreshold_Type(JvmUnsigned64TC):
    """Custom type jvmMemPoolCollectThreshold based on JvmUnsigned64TC"""
    defaultValue = 0


_JvmMemPoolCollectThreshold_Type.__name__ = "JvmUnsigned64TC"
_JvmMemPoolCollectThreshold_Object = MibTableColumn
jvmMemPoolCollectThreshold = _JvmMemPoolCollectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 131),
    _JvmMemPoolCollectThreshold_Type()
)
jvmMemPoolCollectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmMemPoolCollectThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jvmMemPoolCollectThreshold.setUnits("bytes")
_JvmMemPoolCollectThreshdCount_Type = Counter64
_JvmMemPoolCollectThreshdCount_Object = MibTableColumn
jvmMemPoolCollectThreshdCount = _JvmMemPoolCollectThreshdCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 132),
    _JvmMemPoolCollectThreshdCount_Type()
)
jvmMemPoolCollectThreshdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCollectThreshdCount.setStatus("current")
_JvmMemPoolCollectThreshdSupport_Type = JvmImplSupportStateTC
_JvmMemPoolCollectThreshdSupport_Object = MibTableColumn
jvmMemPoolCollectThreshdSupport = _JvmMemPoolCollectThreshdSupport_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 133),
    _JvmMemPoolCollectThreshdSupport_Type()
)
jvmMemPoolCollectThreshdSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemPoolCollectThreshdSupport.setStatus("current")
_JvmMemMgrPoolRelTable_Object = MibTable
jvmMemMgrPoolRelTable = _JvmMemMgrPoolRelTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120)
)
if mibBuilder.loadTexts:
    jvmMemMgrPoolRelTable.setStatus("current")
_JvmMemMgrPoolRelEntry_Object = MibTableRow
jvmMemMgrPoolRelEntry = _JvmMemMgrPoolRelEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1)
)
jvmMemMgrPoolRelEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"),
    (0, "JVM-MANAGEMENT-MIB", "jvmMemPoolIndex"),
)
if mibBuilder.loadTexts:
    jvmMemMgrPoolRelEntry.setStatus("current")
_JvmMemMgrRelManagerName_Type = JvmJavaObjectNameTC
_JvmMemMgrRelManagerName_Object = MibTableColumn
jvmMemMgrRelManagerName = _JvmMemMgrRelManagerName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1, 2),
    _JvmMemMgrRelManagerName_Type()
)
jvmMemMgrRelManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemMgrRelManagerName.setStatus("current")
_JvmMemMgrRelPoolName_Type = JvmJavaObjectNameTC
_JvmMemMgrRelPoolName_Object = MibTableColumn
jvmMemMgrRelPoolName = _JvmMemMgrRelPoolName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1, 3),
    _JvmMemMgrRelPoolName_Type()
)
jvmMemMgrRelPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmMemMgrRelPoolName.setStatus("current")
_JvmThreading_ObjectIdentity = ObjectIdentity
jvmThreading = _JvmThreading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3)
)
_JvmThreadCount_Type = Gauge32
_JvmThreadCount_Object = MibScalar
jvmThreadCount = _JvmThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 1),
    _JvmThreadCount_Type()
)
jvmThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadCount.setStatus("current")
_JvmThreadDaemonCount_Type = Gauge32
_JvmThreadDaemonCount_Object = MibScalar
jvmThreadDaemonCount = _JvmThreadDaemonCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 2),
    _JvmThreadDaemonCount_Type()
)
jvmThreadDaemonCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadDaemonCount.setStatus("current")
_JvmThreadPeakCount_Type = Counter32
_JvmThreadPeakCount_Object = MibScalar
jvmThreadPeakCount = _JvmThreadPeakCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 3),
    _JvmThreadPeakCount_Type()
)
jvmThreadPeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadPeakCount.setStatus("current")
_JvmThreadTotalStartedCount_Type = Counter64
_JvmThreadTotalStartedCount_Object = MibScalar
jvmThreadTotalStartedCount = _JvmThreadTotalStartedCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 4),
    _JvmThreadTotalStartedCount_Type()
)
jvmThreadTotalStartedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadTotalStartedCount.setStatus("current")
_JvmThreadContentionMonitoring_Type = JvmImplOptFeatureStateTC
_JvmThreadContentionMonitoring_Object = MibScalar
jvmThreadContentionMonitoring = _JvmThreadContentionMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 5),
    _JvmThreadContentionMonitoring_Type()
)
jvmThreadContentionMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmThreadContentionMonitoring.setStatus("current")
_JvmThreadCpuTimeMonitoring_Type = JvmImplOptFeatureStateTC
_JvmThreadCpuTimeMonitoring_Object = MibScalar
jvmThreadCpuTimeMonitoring = _JvmThreadCpuTimeMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 6),
    _JvmThreadCpuTimeMonitoring_Type()
)
jvmThreadCpuTimeMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmThreadCpuTimeMonitoring.setStatus("current")
_JvmThreadPeakCountReset_Type = JvmTimeMillis64TC
_JvmThreadPeakCountReset_Object = MibScalar
jvmThreadPeakCountReset = _JvmThreadPeakCountReset_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 7),
    _JvmThreadPeakCountReset_Type()
)
jvmThreadPeakCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jvmThreadPeakCountReset.setStatus("current")
if mibBuilder.loadTexts:
    jvmThreadPeakCountReset.setUnits("milliseconds")
_JvmThreadInstanceTable_Object = MibTable
jvmThreadInstanceTable = _JvmThreadInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    jvmThreadInstanceTable.setStatus("current")
_JvmThreadInstanceEntry_Object = MibTableRow
jvmThreadInstanceEntry = _JvmThreadInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1)
)
jvmThreadInstanceEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmThreadInstIndex"),
)
if mibBuilder.loadTexts:
    jvmThreadInstanceEntry.setStatus("current")
_JvmThreadInstIndex_Type = JvmIndex64TC
_JvmThreadInstIndex_Object = MibTableColumn
jvmThreadInstIndex = _JvmThreadInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 1),
    _JvmThreadInstIndex_Type()
)
jvmThreadInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmThreadInstIndex.setStatus("current")
_JvmThreadInstId_Type = JvmUnsigned64TC
_JvmThreadInstId_Object = MibTableColumn
jvmThreadInstId = _JvmThreadInstId_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 2),
    _JvmThreadInstId_Type()
)
jvmThreadInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstId.setStatus("current")
_JvmThreadInstState_Type = JvmThreadStateTC
_JvmThreadInstState_Object = MibTableColumn
jvmThreadInstState = _JvmThreadInstState_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 3),
    _JvmThreadInstState_Type()
)
jvmThreadInstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstState.setStatus("current")
_JvmThreadInstBlockCount_Type = Counter64
_JvmThreadInstBlockCount_Object = MibTableColumn
jvmThreadInstBlockCount = _JvmThreadInstBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 4),
    _JvmThreadInstBlockCount_Type()
)
jvmThreadInstBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstBlockCount.setStatus("current")
_JvmThreadInstBlockTimeMs_Type = JvmTimeMillis64TC
_JvmThreadInstBlockTimeMs_Object = MibTableColumn
jvmThreadInstBlockTimeMs = _JvmThreadInstBlockTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 5),
    _JvmThreadInstBlockTimeMs_Type()
)
jvmThreadInstBlockTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstBlockTimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmThreadInstBlockTimeMs.setUnits("milliseconds")
_JvmThreadInstWaitCount_Type = Counter64
_JvmThreadInstWaitCount_Object = MibTableColumn
jvmThreadInstWaitCount = _JvmThreadInstWaitCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 6),
    _JvmThreadInstWaitCount_Type()
)
jvmThreadInstWaitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstWaitCount.setStatus("current")
_JvmThreadInstWaitTimeMs_Type = JvmTimeMillis64TC
_JvmThreadInstWaitTimeMs_Object = MibTableColumn
jvmThreadInstWaitTimeMs = _JvmThreadInstWaitTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 7),
    _JvmThreadInstWaitTimeMs_Type()
)
jvmThreadInstWaitTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstWaitTimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmThreadInstWaitTimeMs.setUnits("milliseconds")
_JvmThreadInstCpuTimeNs_Type = JvmTimeNanos64TC
_JvmThreadInstCpuTimeNs_Object = MibTableColumn
jvmThreadInstCpuTimeNs = _JvmThreadInstCpuTimeNs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 8),
    _JvmThreadInstCpuTimeNs_Type()
)
jvmThreadInstCpuTimeNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstCpuTimeNs.setStatus("current")
if mibBuilder.loadTexts:
    jvmThreadInstCpuTimeNs.setUnits("nanoseconds")
_JvmThreadInstName_Type = JvmJavaObjectNameTC
_JvmThreadInstName_Object = MibTableColumn
jvmThreadInstName = _JvmThreadInstName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 9),
    _JvmThreadInstName_Type()
)
jvmThreadInstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstName.setStatus("current")
_JvmThreadInstLockName_Type = JvmJavaObjectNameTC
_JvmThreadInstLockName_Object = MibTableColumn
jvmThreadInstLockName = _JvmThreadInstLockName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 10),
    _JvmThreadInstLockName_Type()
)
jvmThreadInstLockName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstLockName.setStatus("current")
_JvmThreadInstLockOwnerPtr_Type = RowPointer
_JvmThreadInstLockOwnerPtr_Object = MibTableColumn
jvmThreadInstLockOwnerPtr = _JvmThreadInstLockOwnerPtr_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 11),
    _JvmThreadInstLockOwnerPtr_Type()
)
jvmThreadInstLockOwnerPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmThreadInstLockOwnerPtr.setStatus("current")
_JvmRuntime_ObjectIdentity = ObjectIdentity
jvmRuntime = _JvmRuntime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4)
)
_JvmRTName_Type = DisplayString
_JvmRTName_Object = MibScalar
jvmRTName = _JvmRTName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 1),
    _JvmRTName_Type()
)
jvmRTName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTName.setStatus("current")
_JvmRTVMName_Type = JvmJavaObjectNameTC
_JvmRTVMName_Object = MibScalar
jvmRTVMName = _JvmRTVMName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 2),
    _JvmRTVMName_Type()
)
jvmRTVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTVMName.setStatus("current")
_JvmRTVMVendor_Type = DisplayString
_JvmRTVMVendor_Object = MibScalar
jvmRTVMVendor = _JvmRTVMVendor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 3),
    _JvmRTVMVendor_Type()
)
jvmRTVMVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTVMVendor.setStatus("current")
_JvmRTVMVersion_Type = DisplayString
_JvmRTVMVersion_Object = MibScalar
jvmRTVMVersion = _JvmRTVMVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 4),
    _JvmRTVMVersion_Type()
)
jvmRTVMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTVMVersion.setStatus("current")
_JvmRTSpecName_Type = DisplayString
_JvmRTSpecName_Object = MibScalar
jvmRTSpecName = _JvmRTSpecName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 5),
    _JvmRTSpecName_Type()
)
jvmRTSpecName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTSpecName.setStatus("current")
_JvmRTSpecVendor_Type = DisplayString
_JvmRTSpecVendor_Object = MibScalar
jvmRTSpecVendor = _JvmRTSpecVendor_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 6),
    _JvmRTSpecVendor_Type()
)
jvmRTSpecVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTSpecVendor.setStatus("current")
_JvmRTSpecVersion_Type = DisplayString
_JvmRTSpecVersion_Object = MibScalar
jvmRTSpecVersion = _JvmRTSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 7),
    _JvmRTSpecVersion_Type()
)
jvmRTSpecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTSpecVersion.setStatus("current")
_JvmRTManagementSpecVersion_Type = DisplayString
_JvmRTManagementSpecVersion_Object = MibScalar
jvmRTManagementSpecVersion = _JvmRTManagementSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 8),
    _JvmRTManagementSpecVersion_Type()
)
jvmRTManagementSpecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTManagementSpecVersion.setStatus("current")
_JvmRTBootClassPathSupport_Type = JvmImplSupportStateTC
_JvmRTBootClassPathSupport_Object = MibScalar
jvmRTBootClassPathSupport = _JvmRTBootClassPathSupport_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 9),
    _JvmRTBootClassPathSupport_Type()
)
jvmRTBootClassPathSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTBootClassPathSupport.setStatus("current")
_JvmRTInputArgsCount_Type = JvmPositive32TC
_JvmRTInputArgsCount_Object = MibScalar
jvmRTInputArgsCount = _JvmRTInputArgsCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 10),
    _JvmRTInputArgsCount_Type()
)
jvmRTInputArgsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTInputArgsCount.setStatus("current")
_JvmRTUptimeMs_Type = JvmTimeMillis64TC
_JvmRTUptimeMs_Object = MibScalar
jvmRTUptimeMs = _JvmRTUptimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 11),
    _JvmRTUptimeMs_Type()
)
jvmRTUptimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTUptimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmRTUptimeMs.setUnits("milliseconds")
_JvmRTStartTimeMs_Type = JvmTimeMillis64TC
_JvmRTStartTimeMs_Object = MibScalar
jvmRTStartTimeMs = _JvmRTStartTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 12),
    _JvmRTStartTimeMs_Type()
)
jvmRTStartTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTStartTimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmRTStartTimeMs.setUnits("milliseconds")
_JvmRTInputArgsTable_Object = MibTable
jvmRTInputArgsTable = _JvmRTInputArgsTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20)
)
if mibBuilder.loadTexts:
    jvmRTInputArgsTable.setStatus("current")
_JvmRTInputArgsEntry_Object = MibTableRow
jvmRTInputArgsEntry = _JvmRTInputArgsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1)
)
jvmRTInputArgsEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmRTInputArgsIndex"),
)
if mibBuilder.loadTexts:
    jvmRTInputArgsEntry.setStatus("current")
_JvmRTInputArgsIndex_Type = JvmPositive32TC
_JvmRTInputArgsIndex_Object = MibTableColumn
jvmRTInputArgsIndex = _JvmRTInputArgsIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1, 1),
    _JvmRTInputArgsIndex_Type()
)
jvmRTInputArgsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmRTInputArgsIndex.setStatus("current")
_JvmRTInputArgsItem_Type = JvmArgValueTC
_JvmRTInputArgsItem_Object = MibTableColumn
jvmRTInputArgsItem = _JvmRTInputArgsItem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1, 2),
    _JvmRTInputArgsItem_Type()
)
jvmRTInputArgsItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTInputArgsItem.setStatus("current")
_JvmRTBootClassPathTable_Object = MibTable
jvmRTBootClassPathTable = _JvmRTBootClassPathTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21)
)
if mibBuilder.loadTexts:
    jvmRTBootClassPathTable.setStatus("current")
_JvmRTBootClassPathEntry_Object = MibTableRow
jvmRTBootClassPathEntry = _JvmRTBootClassPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1)
)
jvmRTBootClassPathEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmRTBootClassPathIndex"),
)
if mibBuilder.loadTexts:
    jvmRTBootClassPathEntry.setStatus("current")
_JvmRTBootClassPathIndex_Type = JvmPositive32TC
_JvmRTBootClassPathIndex_Object = MibTableColumn
jvmRTBootClassPathIndex = _JvmRTBootClassPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1, 1),
    _JvmRTBootClassPathIndex_Type()
)
jvmRTBootClassPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmRTBootClassPathIndex.setStatus("current")
_JvmRTBootClassPathItem_Type = JvmPathElementTC
_JvmRTBootClassPathItem_Object = MibTableColumn
jvmRTBootClassPathItem = _JvmRTBootClassPathItem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1, 2),
    _JvmRTBootClassPathItem_Type()
)
jvmRTBootClassPathItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTBootClassPathItem.setStatus("current")
_JvmRTClassPathTable_Object = MibTable
jvmRTClassPathTable = _JvmRTClassPathTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22)
)
if mibBuilder.loadTexts:
    jvmRTClassPathTable.setStatus("current")
_JvmRTClassPathEntry_Object = MibTableRow
jvmRTClassPathEntry = _JvmRTClassPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1)
)
jvmRTClassPathEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmRTClassPathIndex"),
)
if mibBuilder.loadTexts:
    jvmRTClassPathEntry.setStatus("current")
_JvmRTClassPathIndex_Type = JvmPositive32TC
_JvmRTClassPathIndex_Object = MibTableColumn
jvmRTClassPathIndex = _JvmRTClassPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1, 1),
    _JvmRTClassPathIndex_Type()
)
jvmRTClassPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmRTClassPathIndex.setStatus("current")
_JvmRTClassPathItem_Type = JvmPathElementTC
_JvmRTClassPathItem_Object = MibTableColumn
jvmRTClassPathItem = _JvmRTClassPathItem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1, 2),
    _JvmRTClassPathItem_Type()
)
jvmRTClassPathItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTClassPathItem.setStatus("current")
_JvmRTLibraryPathTable_Object = MibTable
jvmRTLibraryPathTable = _JvmRTLibraryPathTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23)
)
if mibBuilder.loadTexts:
    jvmRTLibraryPathTable.setStatus("current")
_JvmRTLibraryPathEntry_Object = MibTableRow
jvmRTLibraryPathEntry = _JvmRTLibraryPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1)
)
jvmRTLibraryPathEntry.setIndexNames(
    (0, "JVM-MANAGEMENT-MIB", "jvmRTLibraryPathIndex"),
)
if mibBuilder.loadTexts:
    jvmRTLibraryPathEntry.setStatus("current")
_JvmRTLibraryPathIndex_Type = JvmPositive32TC
_JvmRTLibraryPathIndex_Object = MibTableColumn
jvmRTLibraryPathIndex = _JvmRTLibraryPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1, 1),
    _JvmRTLibraryPathIndex_Type()
)
jvmRTLibraryPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jvmRTLibraryPathIndex.setStatus("current")
_JvmRTLibraryPathItem_Type = JvmPathElementTC
_JvmRTLibraryPathItem_Object = MibTableColumn
jvmRTLibraryPathItem = _JvmRTLibraryPathItem_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1, 2),
    _JvmRTLibraryPathItem_Type()
)
jvmRTLibraryPathItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmRTLibraryPathItem.setStatus("current")
_JvmCompilation_ObjectIdentity = ObjectIdentity
jvmCompilation = _JvmCompilation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5)
)
_JvmJITCompilerName_Type = JvmJavaObjectNameTC
_JvmJITCompilerName_Object = MibScalar
jvmJITCompilerName = _JvmJITCompilerName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 1),
    _JvmJITCompilerName_Type()
)
jvmJITCompilerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmJITCompilerName.setStatus("current")
_JvmJITCompilerTimeMs_Type = JvmTimeMillis64TC
_JvmJITCompilerTimeMs_Object = MibScalar
jvmJITCompilerTimeMs = _JvmJITCompilerTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 2),
    _JvmJITCompilerTimeMs_Type()
)
jvmJITCompilerTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmJITCompilerTimeMs.setStatus("current")
if mibBuilder.loadTexts:
    jvmJITCompilerTimeMs.setUnits("milliseconds")
_JvmJITCompilerTimeMonitoring_Type = JvmImplSupportStateTC
_JvmJITCompilerTimeMonitoring_Object = MibScalar
jvmJITCompilerTimeMonitoring = _JvmJITCompilerTimeMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 3),
    _JvmJITCompilerTimeMonitoring_Type()
)
jvmJITCompilerTimeMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmJITCompilerTimeMonitoring.setStatus("current")
_JvmOS_ObjectIdentity = ObjectIdentity
jvmOS = _JvmOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6)
)
_JvmOSName_Type = JvmJavaObjectNameTC
_JvmOSName_Object = MibScalar
jvmOSName = _JvmOSName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 1),
    _JvmOSName_Type()
)
jvmOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmOSName.setStatus("current")
_JvmOSArch_Type = DisplayString
_JvmOSArch_Object = MibScalar
jvmOSArch = _JvmOSArch_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 2),
    _JvmOSArch_Type()
)
jvmOSArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmOSArch.setStatus("current")
_JvmOSVersion_Type = DisplayString
_JvmOSVersion_Object = MibScalar
jvmOSVersion = _JvmOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 3),
    _JvmOSVersion_Type()
)
jvmOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmOSVersion.setStatus("current")
_JvmOSProcessorCount_Type = Integer32
_JvmOSProcessorCount_Object = MibScalar
jvmOSProcessorCount = _JvmOSProcessorCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 4),
    _JvmOSProcessorCount_Type()
)
jvmOSProcessorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jvmOSProcessorCount.setStatus("current")
_JvmMgtMIBNotifications_ObjectIdentity = ObjectIdentity
jvmMgtMIBNotifications = _JvmMgtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2)
)
_JvmMgtMIBMemoryNotifs_ObjectIdentity = ObjectIdentity
jvmMgtMIBMemoryNotifs = _JvmMgtMIBMemoryNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2)
)
_JvmMgtMIBLowMemoryNotifs_ObjectIdentity = ObjectIdentity
jvmMgtMIBLowMemoryNotifs = _JvmMgtMIBLowMemoryNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1)
)
_JvmLowMemoryPrefix_ObjectIdentity = ObjectIdentity
jvmLowMemoryPrefix = _JvmLowMemoryPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0)
)
_JvmMgtMIBConformance_ObjectIdentity = ObjectIdentity
jvmMgtMIBConformance = _JvmMgtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3)
)
_JvmMgtMIBCompliances_ObjectIdentity = ObjectIdentity
jvmMgtMIBCompliances = _JvmMgtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 1)
)
_JvmMgtMIBGroups_ObjectIdentity = ObjectIdentity
jvmMgtMIBGroups = _JvmMgtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2)
)
_JvmClassLoadingGroups_ObjectIdentity = ObjectIdentity
jvmClassLoadingGroups = _JvmClassLoadingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1)
)
_JvmMemoryGroups_ObjectIdentity = ObjectIdentity
jvmMemoryGroups = _JvmMemoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2)
)
_JvmMemPoolGroups_ObjectIdentity = ObjectIdentity
jvmMemPoolGroups = _JvmMemPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7)
)
_JvmThreadGroups_ObjectIdentity = ObjectIdentity
jvmThreadGroups = _JvmThreadGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3)
)
_JvmThreadInstanceGroups_ObjectIdentity = ObjectIdentity
jvmThreadInstanceGroups = _JvmThreadInstanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2)
)
_JvmRuntimeGroups_ObjectIdentity = ObjectIdentity
jvmRuntimeGroups = _JvmRuntimeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4)
)
_JvmJITCompilerGroups_ObjectIdentity = ObjectIdentity
jvmJITCompilerGroups = _JvmJITCompilerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5)
)

# Managed Objects groups

jvmClassLoadingBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1, 1)
)
jvmClassLoadingBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmClassesLoadedCount"),
        ("JVM-MANAGEMENT-MIB", "jvmClassesTotalLoadedCount"),
        ("JVM-MANAGEMENT-MIB", "jvmClassesUnloadedCount"))
)
if mibBuilder.loadTexts:
    jvmClassLoadingBasicGroup.setStatus("current")

jvmClassLoadingSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1, 2)
)
jvmClassLoadingSetGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmClassesVerboseLevel")
)
if mibBuilder.loadTexts:
    jvmClassLoadingSetGroup.setStatus("current")

jvmMemoryBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 1)
)
jvmMemoryBasicGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmMemoryPendingFinalCount")
)
if mibBuilder.loadTexts:
    jvmMemoryBasicGroup.setStatus("current")

jvmMemoryHeapUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 2)
)
jvmMemoryHeapUsageGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemoryHeapInitSize"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapCommitted"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapMaxSize"))
)
if mibBuilder.loadTexts:
    jvmMemoryHeapUsageGroup.setStatus("current")

jvmMemoryNonHeapUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 3)
)
jvmMemoryNonHeapUsageGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapInitSize"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapCommitted"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapMaxSize"))
)
if mibBuilder.loadTexts:
    jvmMemoryNonHeapUsageGroup.setStatus("current")

jvmMemorySetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 4)
)
jvmMemorySetGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemoryGCVerboseLevel"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryGCCall"))
)
if mibBuilder.loadTexts:
    jvmMemorySetGroup.setStatus("current")

jvmMemManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 5)
)
jvmMemManagerGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemManagerName"),
        ("JVM-MANAGEMENT-MIB", "jvmMemManagerState"))
)
if mibBuilder.loadTexts:
    jvmMemManagerGroup.setStatus("current")

jvmMemGCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 6)
)
jvmMemGCGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemGCCount"),
        ("JVM-MANAGEMENT-MIB", "jvmMemGCTimeMs"))
)
if mibBuilder.loadTexts:
    jvmMemGCGroup.setStatus("current")

jvmMemPoolBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 1)
)
jvmMemPoolBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolType"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolState"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakReset"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdSupport"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdSupport"))
)
if mibBuilder.loadTexts:
    jvmMemPoolBasicGroup.setStatus("current")

jvmMemPoolMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 2)
)
jvmMemPoolMonitoringGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshold"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdCount"))
)
if mibBuilder.loadTexts:
    jvmMemPoolMonitoringGroup.setStatus("current")

jvmMemPoolUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 3)
)
jvmMemPoolUsageGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolInitSize"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCommitted"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolMaxSize"))
)
if mibBuilder.loadTexts:
    jvmMemPoolUsageGroup.setStatus("current")

jvmMemPoolPeakUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 4)
)
jvmMemPoolPeakUsageGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakCommitted"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakMaxSize"))
)
if mibBuilder.loadTexts:
    jvmMemPoolPeakUsageGroup.setStatus("current")

jvmMemPoolCollectUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 5)
)
jvmMemPoolCollectUsageGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectCommitted"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectMaxSize"))
)
if mibBuilder.loadTexts:
    jvmMemPoolCollectUsageGroup.setStatus("current")

jvmMemPoolCollectMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 6)
)
jvmMemPoolCollectMonitoringGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshold"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdCount"))
)
if mibBuilder.loadTexts:
    jvmMemPoolCollectMonitoringGroup.setStatus("current")

jvmMemMgrPoolRelationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 8)
)
jvmMemMgrPoolRelationGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemMgrRelManagerName"),
        ("JVM-MANAGEMENT-MIB", "jvmMemMgrRelPoolName"))
)
if mibBuilder.loadTexts:
    jvmMemMgrPoolRelationGroup.setStatus("current")

jvmThreadBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 1)
)
jvmThreadBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmThreadCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadDaemonCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadPeakCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadTotalStartedCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadContentionMonitoring"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadCpuTimeMonitoring"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadPeakCountReset"))
)
if mibBuilder.loadTexts:
    jvmThreadBasicGroup.setStatus("current")

jvmThreadInstanceBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 1)
)
jvmThreadInstanceBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmThreadInstId"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstState"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstName"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstLockName"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstLockOwnerPtr"))
)
if mibBuilder.loadTexts:
    jvmThreadInstanceBasicGroup.setStatus("current")

jvmThreadInstanceCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 2)
)
jvmThreadInstanceCpuGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmThreadInstCpuTimeNs")
)
if mibBuilder.loadTexts:
    jvmThreadInstanceCpuGroup.setStatus("current")

jvmThreadInstanceBlockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 3)
)
jvmThreadInstanceBlockGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmThreadInstBlockCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstBlockTimeMs"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstWaitCount"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstWaitTimeMs"))
)
if mibBuilder.loadTexts:
    jvmThreadInstanceBlockGroup.setStatus("current")

jvmRuntimeBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4, 1)
)
jvmRuntimeBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmRTName"),
        ("JVM-MANAGEMENT-MIB", "jvmRTVMName"),
        ("JVM-MANAGEMENT-MIB", "jvmRTVMVendor"),
        ("JVM-MANAGEMENT-MIB", "jvmRTVMVersion"),
        ("JVM-MANAGEMENT-MIB", "jvmRTSpecName"),
        ("JVM-MANAGEMENT-MIB", "jvmRTSpecVendor"),
        ("JVM-MANAGEMENT-MIB", "jvmRTSpecVersion"),
        ("JVM-MANAGEMENT-MIB", "jvmRTManagementSpecVersion"),
        ("JVM-MANAGEMENT-MIB", "jvmRTUptimeMs"),
        ("JVM-MANAGEMENT-MIB", "jvmRTStartTimeMs"),
        ("JVM-MANAGEMENT-MIB", "jvmRTBootClassPathSupport"),
        ("JVM-MANAGEMENT-MIB", "jvmRTInputArgsCount"),
        ("JVM-MANAGEMENT-MIB", "jvmRTInputArgsItem"),
        ("JVM-MANAGEMENT-MIB", "jvmRTClassPathItem"),
        ("JVM-MANAGEMENT-MIB", "jvmRTLibraryPathItem"))
)
if mibBuilder.loadTexts:
    jvmRuntimeBasicGroup.setStatus("current")

jvmRuntimeBootCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4, 2)
)
jvmRuntimeBootCPGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmRTBootClassPathItem")
)
if mibBuilder.loadTexts:
    jvmRuntimeBootCPGroup.setStatus("current")

jvmJITCompilerBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5, 1)
)
jvmJITCompilerBasicGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmJITCompilerName"),
        ("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeMonitoring"))
)
if mibBuilder.loadTexts:
    jvmJITCompilerBasicGroup.setStatus("current")

jvmJITCompilerTimeStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5, 2)
)
jvmJITCompilerTimeStatGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeMs")
)
if mibBuilder.loadTexts:
    jvmJITCompilerTimeStatGroup.setStatus("current")

jvmOSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 6)
)
jvmOSGroup.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmOSName"),
        ("JVM-MANAGEMENT-MIB", "jvmOSArch"),
        ("JVM-MANAGEMENT-MIB", "jvmOSVersion"),
        ("JVM-MANAGEMENT-MIB", "jvmOSProcessorCount"))
)
if mibBuilder.loadTexts:
    jvmOSGroup.setStatus("current")


# Notification objects

jvmLowMemoryPoolUsageNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0, 1)
)
jvmLowMemoryPoolUsageNotif.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdCount"))
)
if mibBuilder.loadTexts:
    jvmLowMemoryPoolUsageNotif.setStatus(
        "current"
    )

jvmLowMemoryPoolCollectNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0, 2)
)
jvmLowMemoryPoolCollectNotif.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsed"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdCount"))
)
if mibBuilder.loadTexts:
    jvmLowMemoryPoolCollectNotif.setStatus(
        "current"
    )


# Notifications groups

jvmLowMemoryUsageNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 7)
)
jvmLowMemoryUsageNotifGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmLowMemoryPoolUsageNotif")
)
if mibBuilder.loadTexts:
    jvmLowMemoryUsageNotifGroup.setStatus(
        "current"
    )

jvmLowMemoryCollectNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 8)
)
jvmLowMemoryCollectNotifGroup.setObjects(
    ("JVM-MANAGEMENT-MIB", "jvmLowMemoryPoolCollectNotif")
)
if mibBuilder.loadTexts:
    jvmLowMemoryCollectNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jvmManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 1, 1)
)
jvmManagementCompliance.setObjects(
      *(("JVM-MANAGEMENT-MIB", "jvmClassLoadingBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmClassLoadingSetGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapUsageGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapUsageGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemorySetGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemManagerGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemGCGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsageGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakUsageGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsageGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemMgrPoolRelationGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmRuntimeBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmOSGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolMonitoringGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectMonitoringGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmLowMemoryUsageNotifGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmLowMemoryCollectNotifGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceCpuGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceBlockGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmRuntimeBootCPGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmJITCompilerBasicGroup"),
        ("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeStatGroup"))
)
if mibBuilder.loadTexts:
    jvmManagementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JVM-MANAGEMENT-MIB",
    **{"JvmUnsigned64TC": JvmUnsigned64TC,
       "JvmJavaObjectNameTC": JvmJavaObjectNameTC,
       "JvmPathElementTC": JvmPathElementTC,
       "JvmArgValueTC": JvmArgValueTC,
       "JvmVerboseLevelTC": JvmVerboseLevelTC,
       "JvmImplSupportStateTC": JvmImplSupportStateTC,
       "JvmImplOptFeatureStateTC": JvmImplOptFeatureStateTC,
       "JvmTimeMillis64TC": JvmTimeMillis64TC,
       "JvmTimeNanos64TC": JvmTimeNanos64TC,
       "JvmPositive32TC": JvmPositive32TC,
       "JvmManagedMemoryTypeTC": JvmManagedMemoryTypeTC,
       "JvmValidityStateTC": JvmValidityStateTC,
       "JvmThreadStateTC": JvmThreadStateTC,
       "JvmIndex64TC": JvmIndex64TC,
       "sun": sun,
       "jmgt": jmgt,
       "standard": standard,
       "jvmMgtMIB": jvmMgtMIB,
       "jvmMgtMIBObjects": jvmMgtMIBObjects,
       "jvmClassLoading": jvmClassLoading,
       "jvmClassesLoadedCount": jvmClassesLoadedCount,
       "jvmClassesTotalLoadedCount": jvmClassesTotalLoadedCount,
       "jvmClassesUnloadedCount": jvmClassesUnloadedCount,
       "jvmClassesVerboseLevel": jvmClassesVerboseLevel,
       "jvmMemory": jvmMemory,
       "jvmMemoryPendingFinalCount": jvmMemoryPendingFinalCount,
       "jvmMemoryGCVerboseLevel": jvmMemoryGCVerboseLevel,
       "jvmMemoryGCCall": jvmMemoryGCCall,
       "jvmMemoryHeapInitSize": jvmMemoryHeapInitSize,
       "jvmMemoryHeapUsed": jvmMemoryHeapUsed,
       "jvmMemoryHeapCommitted": jvmMemoryHeapCommitted,
       "jvmMemoryHeapMaxSize": jvmMemoryHeapMaxSize,
       "jvmMemoryNonHeapInitSize": jvmMemoryNonHeapInitSize,
       "jvmMemoryNonHeapUsed": jvmMemoryNonHeapUsed,
       "jvmMemoryNonHeapCommitted": jvmMemoryNonHeapCommitted,
       "jvmMemoryNonHeapMaxSize": jvmMemoryNonHeapMaxSize,
       "jvmMemManagerTable": jvmMemManagerTable,
       "jvmMemManagerEntry": jvmMemManagerEntry,
       "jvmMemManagerIndex": jvmMemManagerIndex,
       "jvmMemManagerName": jvmMemManagerName,
       "jvmMemManagerState": jvmMemManagerState,
       "jvmMemGCTable": jvmMemGCTable,
       "jvmMemGCEntry": jvmMemGCEntry,
       "jvmMemGCCount": jvmMemGCCount,
       "jvmMemGCTimeMs": jvmMemGCTimeMs,
       "jvmMemPoolTable": jvmMemPoolTable,
       "jvmMemPoolEntry": jvmMemPoolEntry,
       "jvmMemPoolIndex": jvmMemPoolIndex,
       "jvmMemPoolName": jvmMemPoolName,
       "jvmMemPoolType": jvmMemPoolType,
       "jvmMemPoolState": jvmMemPoolState,
       "jvmMemPoolPeakReset": jvmMemPoolPeakReset,
       "jvmMemPoolInitSize": jvmMemPoolInitSize,
       "jvmMemPoolUsed": jvmMemPoolUsed,
       "jvmMemPoolCommitted": jvmMemPoolCommitted,
       "jvmMemPoolMaxSize": jvmMemPoolMaxSize,
       "jvmMemPoolPeakUsed": jvmMemPoolPeakUsed,
       "jvmMemPoolPeakCommitted": jvmMemPoolPeakCommitted,
       "jvmMemPoolPeakMaxSize": jvmMemPoolPeakMaxSize,
       "jvmMemPoolCollectUsed": jvmMemPoolCollectUsed,
       "jvmMemPoolCollectCommitted": jvmMemPoolCollectCommitted,
       "jvmMemPoolCollectMaxSize": jvmMemPoolCollectMaxSize,
       "jvmMemPoolThreshold": jvmMemPoolThreshold,
       "jvmMemPoolThreshdCount": jvmMemPoolThreshdCount,
       "jvmMemPoolThreshdSupport": jvmMemPoolThreshdSupport,
       "jvmMemPoolCollectThreshold": jvmMemPoolCollectThreshold,
       "jvmMemPoolCollectThreshdCount": jvmMemPoolCollectThreshdCount,
       "jvmMemPoolCollectThreshdSupport": jvmMemPoolCollectThreshdSupport,
       "jvmMemMgrPoolRelTable": jvmMemMgrPoolRelTable,
       "jvmMemMgrPoolRelEntry": jvmMemMgrPoolRelEntry,
       "jvmMemMgrRelManagerName": jvmMemMgrRelManagerName,
       "jvmMemMgrRelPoolName": jvmMemMgrRelPoolName,
       "jvmThreading": jvmThreading,
       "jvmThreadCount": jvmThreadCount,
       "jvmThreadDaemonCount": jvmThreadDaemonCount,
       "jvmThreadPeakCount": jvmThreadPeakCount,
       "jvmThreadTotalStartedCount": jvmThreadTotalStartedCount,
       "jvmThreadContentionMonitoring": jvmThreadContentionMonitoring,
       "jvmThreadCpuTimeMonitoring": jvmThreadCpuTimeMonitoring,
       "jvmThreadPeakCountReset": jvmThreadPeakCountReset,
       "jvmThreadInstanceTable": jvmThreadInstanceTable,
       "jvmThreadInstanceEntry": jvmThreadInstanceEntry,
       "jvmThreadInstIndex": jvmThreadInstIndex,
       "jvmThreadInstId": jvmThreadInstId,
       "jvmThreadInstState": jvmThreadInstState,
       "jvmThreadInstBlockCount": jvmThreadInstBlockCount,
       "jvmThreadInstBlockTimeMs": jvmThreadInstBlockTimeMs,
       "jvmThreadInstWaitCount": jvmThreadInstWaitCount,
       "jvmThreadInstWaitTimeMs": jvmThreadInstWaitTimeMs,
       "jvmThreadInstCpuTimeNs": jvmThreadInstCpuTimeNs,
       "jvmThreadInstName": jvmThreadInstName,
       "jvmThreadInstLockName": jvmThreadInstLockName,
       "jvmThreadInstLockOwnerPtr": jvmThreadInstLockOwnerPtr,
       "jvmRuntime": jvmRuntime,
       "jvmRTName": jvmRTName,
       "jvmRTVMName": jvmRTVMName,
       "jvmRTVMVendor": jvmRTVMVendor,
       "jvmRTVMVersion": jvmRTVMVersion,
       "jvmRTSpecName": jvmRTSpecName,
       "jvmRTSpecVendor": jvmRTSpecVendor,
       "jvmRTSpecVersion": jvmRTSpecVersion,
       "jvmRTManagementSpecVersion": jvmRTManagementSpecVersion,
       "jvmRTBootClassPathSupport": jvmRTBootClassPathSupport,
       "jvmRTInputArgsCount": jvmRTInputArgsCount,
       "jvmRTUptimeMs": jvmRTUptimeMs,
       "jvmRTStartTimeMs": jvmRTStartTimeMs,
       "jvmRTInputArgsTable": jvmRTInputArgsTable,
       "jvmRTInputArgsEntry": jvmRTInputArgsEntry,
       "jvmRTInputArgsIndex": jvmRTInputArgsIndex,
       "jvmRTInputArgsItem": jvmRTInputArgsItem,
       "jvmRTBootClassPathTable": jvmRTBootClassPathTable,
       "jvmRTBootClassPathEntry": jvmRTBootClassPathEntry,
       "jvmRTBootClassPathIndex": jvmRTBootClassPathIndex,
       "jvmRTBootClassPathItem": jvmRTBootClassPathItem,
       "jvmRTClassPathTable": jvmRTClassPathTable,
       "jvmRTClassPathEntry": jvmRTClassPathEntry,
       "jvmRTClassPathIndex": jvmRTClassPathIndex,
       "jvmRTClassPathItem": jvmRTClassPathItem,
       "jvmRTLibraryPathTable": jvmRTLibraryPathTable,
       "jvmRTLibraryPathEntry": jvmRTLibraryPathEntry,
       "jvmRTLibraryPathIndex": jvmRTLibraryPathIndex,
       "jvmRTLibraryPathItem": jvmRTLibraryPathItem,
       "jvmCompilation": jvmCompilation,
       "jvmJITCompilerName": jvmJITCompilerName,
       "jvmJITCompilerTimeMs": jvmJITCompilerTimeMs,
       "jvmJITCompilerTimeMonitoring": jvmJITCompilerTimeMonitoring,
       "jvmOS": jvmOS,
       "jvmOSName": jvmOSName,
       "jvmOSArch": jvmOSArch,
       "jvmOSVersion": jvmOSVersion,
       "jvmOSProcessorCount": jvmOSProcessorCount,
       "jvmMgtMIBNotifications": jvmMgtMIBNotifications,
       "jvmMgtMIBMemoryNotifs": jvmMgtMIBMemoryNotifs,
       "jvmMgtMIBLowMemoryNotifs": jvmMgtMIBLowMemoryNotifs,
       "jvmLowMemoryPrefix": jvmLowMemoryPrefix,
       "jvmLowMemoryPoolUsageNotif": jvmLowMemoryPoolUsageNotif,
       "jvmLowMemoryPoolCollectNotif": jvmLowMemoryPoolCollectNotif,
       "jvmMgtMIBConformance": jvmMgtMIBConformance,
       "jvmMgtMIBCompliances": jvmMgtMIBCompliances,
       "jvmManagementCompliance": jvmManagementCompliance,
       "jvmMgtMIBGroups": jvmMgtMIBGroups,
       "jvmClassLoadingGroups": jvmClassLoadingGroups,
       "jvmClassLoadingBasicGroup": jvmClassLoadingBasicGroup,
       "jvmClassLoadingSetGroup": jvmClassLoadingSetGroup,
       "jvmMemoryGroups": jvmMemoryGroups,
       "jvmMemoryBasicGroup": jvmMemoryBasicGroup,
       "jvmMemoryHeapUsageGroup": jvmMemoryHeapUsageGroup,
       "jvmMemoryNonHeapUsageGroup": jvmMemoryNonHeapUsageGroup,
       "jvmMemorySetGroup": jvmMemorySetGroup,
       "jvmMemManagerGroup": jvmMemManagerGroup,
       "jvmMemGCGroup": jvmMemGCGroup,
       "jvmMemPoolGroups": jvmMemPoolGroups,
       "jvmMemPoolBasicGroup": jvmMemPoolBasicGroup,
       "jvmMemPoolMonitoringGroup": jvmMemPoolMonitoringGroup,
       "jvmMemPoolUsageGroup": jvmMemPoolUsageGroup,
       "jvmMemPoolPeakUsageGroup": jvmMemPoolPeakUsageGroup,
       "jvmMemPoolCollectUsageGroup": jvmMemPoolCollectUsageGroup,
       "jvmMemPoolCollectMonitoringGroup": jvmMemPoolCollectMonitoringGroup,
       "jvmMemMgrPoolRelationGroup": jvmMemMgrPoolRelationGroup,
       "jvmThreadGroups": jvmThreadGroups,
       "jvmThreadBasicGroup": jvmThreadBasicGroup,
       "jvmThreadInstanceGroups": jvmThreadInstanceGroups,
       "jvmThreadInstanceBasicGroup": jvmThreadInstanceBasicGroup,
       "jvmThreadInstanceCpuGroup": jvmThreadInstanceCpuGroup,
       "jvmThreadInstanceBlockGroup": jvmThreadInstanceBlockGroup,
       "jvmRuntimeGroups": jvmRuntimeGroups,
       "jvmRuntimeBasicGroup": jvmRuntimeBasicGroup,
       "jvmRuntimeBootCPGroup": jvmRuntimeBootCPGroup,
       "jvmJITCompilerGroups": jvmJITCompilerGroups,
       "jvmJITCompilerBasicGroup": jvmJITCompilerBasicGroup,
       "jvmJITCompilerTimeStatGroup": jvmJITCompilerTimeStatGroup,
       "jvmOSGroup": jvmOSGroup,
       "jvmLowMemoryUsageNotifGroup": jvmLowMemoryUsageNotifGroup,
       "jvmLowMemoryCollectNotifGroup": jvmLowMemoryCollectNotifGroup}
)
