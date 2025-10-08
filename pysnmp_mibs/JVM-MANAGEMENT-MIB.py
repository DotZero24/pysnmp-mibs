#
# PySNMP MIB module JVM-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oracle/JVM-MANAGEMENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowPointer, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TextualConvention", "DisplayString")
jvmMgtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1))
jvmMgtMIB.setRevisions(('2004-03-04 18:00',))
if mibBuilder.loadTexts: jvmMgtMIB.setLastUpdated('200403041800Z')
if mibBuilder.loadTexts: jvmMgtMIB.setOrganization('Oracle and/or its affiliates.')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
jmgt = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145))
standard = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3))
class JvmUnsigned64TC(TextualConvention, Counter64):
    reference = 'RFC 2564 - APPLICATION-MIB, Unsigned64TC.'
    status = 'current'

class JvmJavaObjectNameTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class JvmPathElementTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class JvmArgValueTC(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class JvmVerboseLevelTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("silent", 1), ("verbose", 2))

class JvmImplSupportStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unsupported", 1), ("supported", 2))

class JvmImplOptFeatureStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3, 4))
    namedValues = NamedValues(("unsupported", 1), ("enabled", 3), ("disabled", 4))

class JvmTimeMillis64TC(TextualConvention, Counter64):
    status = 'current'

class JvmTimeNanos64TC(TextualConvention, Counter64):
    status = 'current'

class JvmPositive32TC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class JvmManagedMemoryTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nonheap", 1), ("heap", 2))

class JvmValidityStateTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("invalid", 1), ("valid", 2))

class JvmThreadStateTC(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inNative", 1), ("suspended", 2), ("newThread", 3), ("runnable", 4), ("blocked", 5), ("terminated", 6), ("waiting", 7), ("timedWaiting", 8), ("other", 9))

class JvmIndex64TC(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

jvmMgtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1))
jvmMgtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2))
jvmMgtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3))
jvmClassLoading = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1))
jvmClassesLoadedCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmClassesLoadedCount.setStatus('current')
jvmClassesTotalLoadedCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmClassesTotalLoadedCount.setStatus('current')
jvmClassesUnloadedCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmClassesUnloadedCount.setStatus('current')
jvmClassesVerboseLevel = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 1, 4), JvmVerboseLevelTC().clone('silent')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmClassesVerboseLevel.setStatus('current')
jvmMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2))
jvmMemoryPendingFinalCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryPendingFinalCount.setStatus('current')
jvmMemoryGCVerboseLevel = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 2), JvmVerboseLevelTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmMemoryGCVerboseLevel.setStatus('current')
jvmMemoryGCCall = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unsupported", 1), ("supported", 2), ("start", 3), ("started", 4), ("failed", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmMemoryGCCall.setStatus('current')
jvmMemoryHeapInitSize = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 10), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryHeapInitSize.setStatus('current')
jvmMemoryHeapUsed = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 11), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryHeapUsed.setStatus('current')
jvmMemoryHeapCommitted = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 12), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryHeapCommitted.setStatus('current')
jvmMemoryHeapMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 13), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryHeapMaxSize.setStatus('current')
jvmMemoryNonHeapInitSize = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 20), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryNonHeapInitSize.setStatus('current')
jvmMemoryNonHeapUsed = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 21), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryNonHeapUsed.setStatus('current')
jvmMemoryNonHeapCommitted = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 22), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryNonHeapCommitted.setStatus('current')
jvmMemoryNonHeapMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 23), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemoryNonHeapMaxSize.setStatus('current')
jvmMemManagerTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100), )
if mibBuilder.loadTexts: jvmMemManagerTable.setStatus('current')
jvmMemManagerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"))
if mibBuilder.loadTexts: jvmMemManagerEntry.setStatus('current')
jvmMemManagerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmMemManagerIndex.setStatus('current')
jvmMemManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 2), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemManagerName.setStatus('current')
jvmMemManagerState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 100, 1, 3), JvmValidityStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemManagerState.setStatus('current')
jvmMemGCTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101), )
if mibBuilder.loadTexts: jvmMemGCTable.setStatus('current')
jvmMemGCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"))
if mibBuilder.loadTexts: jvmMemGCEntry.setStatus('current')
jvmMemGCCount = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemGCCount.setStatus('current')
jvmMemGCTimeMs = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 101, 1, 3), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemGCTimeMs.setStatus('current')
jvmMemPoolTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110), )
if mibBuilder.loadTexts: jvmMemPoolTable.setStatus('current')
jvmMemPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmMemPoolIndex"))
if mibBuilder.loadTexts: jvmMemPoolEntry.setStatus('current')
jvmMemPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmMemPoolIndex.setStatus('current')
jvmMemPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 2), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolName.setStatus('current')
jvmMemPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 3), JvmManagedMemoryTypeTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolType.setStatus('current')
jvmMemPoolState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 4), JvmValidityStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolState.setStatus('current')
jvmMemPoolPeakReset = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 5), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmMemPoolPeakReset.setStatus('current')
jvmMemPoolInitSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 10), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolInitSize.setStatus('current')
jvmMemPoolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 11), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolUsed.setStatus('current')
jvmMemPoolCommitted = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 12), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCommitted.setStatus('current')
jvmMemPoolMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 13), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolMaxSize.setStatus('current')
jvmMemPoolPeakUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 21), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolPeakUsed.setStatus('current')
jvmMemPoolPeakCommitted = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 22), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolPeakCommitted.setStatus('current')
jvmMemPoolPeakMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 23), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolPeakMaxSize.setStatus('current')
jvmMemPoolCollectUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 31), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCollectUsed.setStatus('current')
jvmMemPoolCollectCommitted = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 32), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCollectCommitted.setStatus('current')
jvmMemPoolCollectMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 33), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCollectMaxSize.setStatus('current')
jvmMemPoolThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 110), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmMemPoolThreshold.setStatus('current')
jvmMemPoolThreshdCount = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 111), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolThreshdCount.setStatus('current')
jvmMemPoolThreshdSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 112), JvmImplSupportStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolThreshdSupport.setStatus('current')
jvmMemPoolCollectThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 131), JvmUnsigned64TC()).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmMemPoolCollectThreshold.setStatus('current')
jvmMemPoolCollectThreshdCount = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 132), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCollectThreshdCount.setStatus('current')
jvmMemPoolCollectThreshdSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 110, 1, 133), JvmImplSupportStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemPoolCollectThreshdSupport.setStatus('current')
jvmMemMgrPoolRelTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120), )
if mibBuilder.loadTexts: jvmMemMgrPoolRelTable.setStatus('current')
jvmMemMgrPoolRelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmMemManagerIndex"), (0, "JVM-MANAGEMENT-MIB", "jvmMemPoolIndex"))
if mibBuilder.loadTexts: jvmMemMgrPoolRelEntry.setStatus('current')
jvmMemMgrRelManagerName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1, 2), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemMgrRelManagerName.setStatus('current')
jvmMemMgrRelPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 2, 120, 1, 3), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmMemMgrRelPoolName.setStatus('current')
jvmThreading = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3))
jvmThreadCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadCount.setStatus('current')
jvmThreadDaemonCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadDaemonCount.setStatus('current')
jvmThreadPeakCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadPeakCount.setStatus('current')
jvmThreadTotalStartedCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadTotalStartedCount.setStatus('current')
jvmThreadContentionMonitoring = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 5), JvmImplOptFeatureStateTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmThreadContentionMonitoring.setStatus('current')
jvmThreadCpuTimeMonitoring = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 6), JvmImplOptFeatureStateTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmThreadCpuTimeMonitoring.setStatus('current')
jvmThreadPeakCountReset = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 7), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: jvmThreadPeakCountReset.setStatus('current')
jvmThreadInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10), )
if mibBuilder.loadTexts: jvmThreadInstanceTable.setStatus('current')
jvmThreadInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmThreadInstIndex"))
if mibBuilder.loadTexts: jvmThreadInstanceEntry.setStatus('current')
jvmThreadInstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 1), JvmIndex64TC())
if mibBuilder.loadTexts: jvmThreadInstIndex.setStatus('current')
jvmThreadInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 2), JvmUnsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstId.setStatus('current')
jvmThreadInstState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 3), JvmThreadStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstState.setStatus('current')
jvmThreadInstBlockCount = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstBlockCount.setStatus('current')
jvmThreadInstBlockTimeMs = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 5), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstBlockTimeMs.setStatus('current')
jvmThreadInstWaitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstWaitCount.setStatus('current')
jvmThreadInstWaitTimeMs = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 7), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstWaitTimeMs.setStatus('current')
jvmThreadInstCpuTimeNs = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 8), JvmTimeNanos64TC()).setUnits('nanoseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstCpuTimeNs.setStatus('current')
jvmThreadInstName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 9), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstName.setStatus('current')
jvmThreadInstLockName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 10), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstLockName.setStatus('current')
jvmThreadInstLockOwnerPtr = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 3, 10, 1, 11), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmThreadInstLockOwnerPtr.setStatus('current')
jvmRuntime = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4))
jvmRTName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTName.setStatus('current')
jvmRTVMName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 2), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTVMName.setStatus('current')
jvmRTVMVendor = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTVMVendor.setStatus('current')
jvmRTVMVersion = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTVMVersion.setStatus('current')
jvmRTSpecName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTSpecName.setStatus('current')
jvmRTSpecVendor = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTSpecVendor.setStatus('current')
jvmRTSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTSpecVersion.setStatus('current')
jvmRTManagementSpecVersion = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTManagementSpecVersion.setStatus('current')
jvmRTBootClassPathSupport = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 9), JvmImplSupportStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTBootClassPathSupport.setStatus('current')
jvmRTInputArgsCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 10), JvmPositive32TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTInputArgsCount.setStatus('current')
jvmRTUptimeMs = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 11), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTUptimeMs.setStatus('current')
jvmRTStartTimeMs = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 12), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTStartTimeMs.setStatus('current')
jvmRTInputArgsTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20), )
if mibBuilder.loadTexts: jvmRTInputArgsTable.setStatus('current')
jvmRTInputArgsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmRTInputArgsIndex"))
if mibBuilder.loadTexts: jvmRTInputArgsEntry.setStatus('current')
jvmRTInputArgsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmRTInputArgsIndex.setStatus('current')
jvmRTInputArgsItem = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 20, 1, 2), JvmArgValueTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTInputArgsItem.setStatus('current')
jvmRTBootClassPathTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21), )
if mibBuilder.loadTexts: jvmRTBootClassPathTable.setStatus('current')
jvmRTBootClassPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmRTBootClassPathIndex"))
if mibBuilder.loadTexts: jvmRTBootClassPathEntry.setStatus('current')
jvmRTBootClassPathIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmRTBootClassPathIndex.setStatus('current')
jvmRTBootClassPathItem = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 21, 1, 2), JvmPathElementTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTBootClassPathItem.setStatus('current')
jvmRTClassPathTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22), )
if mibBuilder.loadTexts: jvmRTClassPathTable.setStatus('current')
jvmRTClassPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmRTClassPathIndex"))
if mibBuilder.loadTexts: jvmRTClassPathEntry.setStatus('current')
jvmRTClassPathIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmRTClassPathIndex.setStatus('current')
jvmRTClassPathItem = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 22, 1, 2), JvmPathElementTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTClassPathItem.setStatus('current')
jvmRTLibraryPathTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23), )
if mibBuilder.loadTexts: jvmRTLibraryPathTable.setStatus('current')
jvmRTLibraryPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1), ).setIndexNames((0, "JVM-MANAGEMENT-MIB", "jvmRTLibraryPathIndex"))
if mibBuilder.loadTexts: jvmRTLibraryPathEntry.setStatus('current')
jvmRTLibraryPathIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1, 1), JvmPositive32TC())
if mibBuilder.loadTexts: jvmRTLibraryPathIndex.setStatus('current')
jvmRTLibraryPathItem = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 4, 23, 1, 2), JvmPathElementTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmRTLibraryPathItem.setStatus('current')
jvmCompilation = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5))
jvmJITCompilerName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 1), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmJITCompilerName.setStatus('current')
jvmJITCompilerTimeMs = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 2), JvmTimeMillis64TC()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmJITCompilerTimeMs.setStatus('current')
jvmJITCompilerTimeMonitoring = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 5, 3), JvmImplSupportStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmJITCompilerTimeMonitoring.setStatus('current')
jvmOS = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6))
jvmOSName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 1), JvmJavaObjectNameTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmOSName.setStatus('current')
jvmOSArch = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmOSArch.setStatus('current')
jvmOSVersion = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmOSVersion.setStatus('current')
jvmOSProcessorCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jvmOSProcessorCount.setStatus('current')
jvmMgtMIBMemoryNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2))
jvmMgtMIBLowMemoryNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1))
jvmLowMemoryPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0))
jvmLowMemoryPoolUsageNotif = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdCount"))
if mibBuilder.loadTexts: jvmLowMemoryPoolUsageNotif.setStatus('current')
jvmLowMemoryPoolCollectNotif = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 2, 2, 1, 0, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdCount"))
if mibBuilder.loadTexts: jvmLowMemoryPoolCollectNotif.setStatus('current')
jvmMgtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 1))
jvmMgtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2))
jvmManagementCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 1, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmClassLoadingBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmClassLoadingSetGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemoryBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapUsageGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapUsageGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemorySetGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemManagerGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemGCGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsageGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakUsageGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsageGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemMgrPoolRelationGroup"), ("JVM-MANAGEMENT-MIB", "jvmThreadBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmRuntimeBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmOSGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolMonitoringGroup"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectMonitoringGroup"), ("JVM-MANAGEMENT-MIB", "jvmLowMemoryUsageNotifGroup"), ("JVM-MANAGEMENT-MIB", "jvmLowMemoryCollectNotifGroup"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceCpuGroup"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstanceBlockGroup"), ("JVM-MANAGEMENT-MIB", "jvmRuntimeBootCPGroup"), ("JVM-MANAGEMENT-MIB", "jvmJITCompilerBasicGroup"), ("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmManagementCompliance = jvmManagementCompliance.setStatus('current')
jvmClassLoadingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1))
jvmClassLoadingBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmClassesLoadedCount"), ("JVM-MANAGEMENT-MIB", "jvmClassesTotalLoadedCount"), ("JVM-MANAGEMENT-MIB", "jvmClassesUnloadedCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmClassLoadingBasicGroup = jvmClassLoadingBasicGroup.setStatus('current')
jvmClassLoadingSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 1, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmClassesVerboseLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmClassLoadingSetGroup = jvmClassLoadingSetGroup.setStatus('current')
jvmMemoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2))
jvmMemoryBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemoryPendingFinalCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemoryBasicGroup = jvmMemoryBasicGroup.setStatus('current')
jvmMemoryHeapUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemoryHeapInitSize"), ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapCommitted"), ("JVM-MANAGEMENT-MIB", "jvmMemoryHeapMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemoryHeapUsageGroup = jvmMemoryHeapUsageGroup.setStatus('current')
jvmMemoryNonHeapUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 3)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapInitSize"), ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapCommitted"), ("JVM-MANAGEMENT-MIB", "jvmMemoryNonHeapMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemoryNonHeapUsageGroup = jvmMemoryNonHeapUsageGroup.setStatus('current')
jvmMemorySetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 4)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemoryGCVerboseLevel"), ("JVM-MANAGEMENT-MIB", "jvmMemoryGCCall"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemorySetGroup = jvmMemorySetGroup.setStatus('current')
jvmMemManagerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 5)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemManagerName"), ("JVM-MANAGEMENT-MIB", "jvmMemManagerState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemManagerGroup = jvmMemManagerGroup.setStatus('current')
jvmMemGCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 6)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemGCCount"), ("JVM-MANAGEMENT-MIB", "jvmMemGCTimeMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemGCGroup = jvmMemGCGroup.setStatus('current')
jvmMemPoolGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7))
jvmMemPoolBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolName"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolType"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolState"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakReset"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdSupport"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdSupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolBasicGroup = jvmMemPoolBasicGroup.setStatus('current')
jvmMemPoolMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshold"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolThreshdCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolMonitoringGroup = jvmMemPoolMonitoringGroup.setStatus('current')
jvmMemPoolUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 3)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolInitSize"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCommitted"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolUsageGroup = jvmMemPoolUsageGroup.setStatus('current')
jvmMemPoolPeakUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 4)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakCommitted"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolPeakMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolPeakUsageGroup = jvmMemPoolPeakUsageGroup.setStatus('current')
jvmMemPoolCollectUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 5)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectUsed"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectCommitted"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectMaxSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolCollectUsageGroup = jvmMemPoolCollectUsageGroup.setStatus('current')
jvmMemPoolCollectMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 7, 6)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshold"), ("JVM-MANAGEMENT-MIB", "jvmMemPoolCollectThreshdCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemPoolCollectMonitoringGroup = jvmMemPoolCollectMonitoringGroup.setStatus('current')
jvmMemMgrPoolRelationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 2, 8)).setObjects(("JVM-MANAGEMENT-MIB", "jvmMemMgrRelManagerName"), ("JVM-MANAGEMENT-MIB", "jvmMemMgrRelPoolName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmMemMgrPoolRelationGroup = jvmMemMgrPoolRelationGroup.setStatus('current')
jvmThreadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3))
jvmThreadBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmThreadCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadDaemonCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadPeakCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadTotalStartedCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadContentionMonitoring"), ("JVM-MANAGEMENT-MIB", "jvmThreadCpuTimeMonitoring"), ("JVM-MANAGEMENT-MIB", "jvmThreadPeakCountReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmThreadBasicGroup = jvmThreadBasicGroup.setStatus('current')
jvmThreadInstanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2))
jvmThreadInstanceBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmThreadInstId"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstState"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstName"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstLockName"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstLockOwnerPtr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmThreadInstanceBasicGroup = jvmThreadInstanceBasicGroup.setStatus('current')
jvmThreadInstanceCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmThreadInstCpuTimeNs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmThreadInstanceCpuGroup = jvmThreadInstanceCpuGroup.setStatus('current')
jvmThreadInstanceBlockGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 3, 2, 3)).setObjects(("JVM-MANAGEMENT-MIB", "jvmThreadInstBlockCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstBlockTimeMs"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstWaitCount"), ("JVM-MANAGEMENT-MIB", "jvmThreadInstWaitTimeMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmThreadInstanceBlockGroup = jvmThreadInstanceBlockGroup.setStatus('current')
jvmRuntimeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4))
jvmRuntimeBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmRTName"), ("JVM-MANAGEMENT-MIB", "jvmRTVMName"), ("JVM-MANAGEMENT-MIB", "jvmRTVMVendor"), ("JVM-MANAGEMENT-MIB", "jvmRTVMVersion"), ("JVM-MANAGEMENT-MIB", "jvmRTSpecName"), ("JVM-MANAGEMENT-MIB", "jvmRTSpecVendor"), ("JVM-MANAGEMENT-MIB", "jvmRTSpecVersion"), ("JVM-MANAGEMENT-MIB", "jvmRTManagementSpecVersion"), ("JVM-MANAGEMENT-MIB", "jvmRTUptimeMs"), ("JVM-MANAGEMENT-MIB", "jvmRTStartTimeMs"), ("JVM-MANAGEMENT-MIB", "jvmRTBootClassPathSupport"), ("JVM-MANAGEMENT-MIB", "jvmRTInputArgsCount"), ("JVM-MANAGEMENT-MIB", "jvmRTInputArgsItem"), ("JVM-MANAGEMENT-MIB", "jvmRTClassPathItem"), ("JVM-MANAGEMENT-MIB", "jvmRTLibraryPathItem"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmRuntimeBasicGroup = jvmRuntimeBasicGroup.setStatus('current')
jvmRuntimeBootCPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 4, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmRTBootClassPathItem"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmRuntimeBootCPGroup = jvmRuntimeBootCPGroup.setStatus('current')
jvmJITCompilerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5))
jvmJITCompilerBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5, 1)).setObjects(("JVM-MANAGEMENT-MIB", "jvmJITCompilerName"), ("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeMonitoring"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmJITCompilerBasicGroup = jvmJITCompilerBasicGroup.setStatus('current')
jvmJITCompilerTimeStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 5, 2)).setObjects(("JVM-MANAGEMENT-MIB", "jvmJITCompilerTimeMs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmJITCompilerTimeStatGroup = jvmJITCompilerTimeStatGroup.setStatus('current')
jvmOSGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 6)).setObjects(("JVM-MANAGEMENT-MIB", "jvmOSName"), ("JVM-MANAGEMENT-MIB", "jvmOSArch"), ("JVM-MANAGEMENT-MIB", "jvmOSVersion"), ("JVM-MANAGEMENT-MIB", "jvmOSProcessorCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmOSGroup = jvmOSGroup.setStatus('current')
jvmLowMemoryUsageNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 7)).setObjects(("JVM-MANAGEMENT-MIB", "jvmLowMemoryPoolUsageNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmLowMemoryUsageNotifGroup = jvmLowMemoryUsageNotifGroup.setStatus('current')
jvmLowMemoryCollectNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 42, 2, 145, 3, 163, 1, 3, 2, 8)).setObjects(("JVM-MANAGEMENT-MIB", "jvmLowMemoryPoolCollectNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    jvmLowMemoryCollectNotifGroup = jvmLowMemoryCollectNotifGroup.setStatus('current')
mibBuilder.exportSymbols("JVM-MANAGEMENT-MIB", JvmJavaObjectNameTC=JvmJavaObjectNameTC, jvmMemPoolUsed=jvmMemPoolUsed, jvmRTSpecVendor=jvmRTSpecVendor, jvmRuntimeBootCPGroup=jvmRuntimeBootCPGroup, jvmThreadInstName=jvmThreadInstName, jvmMemPoolCollectUsed=jvmMemPoolCollectUsed, jvmMemMgrPoolRelationGroup=jvmMemMgrPoolRelationGroup, jvmMemManagerGroup=jvmMemManagerGroup, jvmRTInputArgsItem=jvmRTInputArgsItem, jvmOSName=jvmOSName, jvmMemPoolMonitoringGroup=jvmMemPoolMonitoringGroup, jvmClassLoadingSetGroup=jvmClassLoadingSetGroup, jvmThreading=jvmThreading, jvmThreadInstanceEntry=jvmThreadInstanceEntry, jvmRTName=jvmRTName, jvmRTBootClassPathEntry=jvmRTBootClassPathEntry, jvmThreadInstBlockCount=jvmThreadInstBlockCount, jvmJITCompilerTimeMs=jvmJITCompilerTimeMs, jvmLowMemoryPoolCollectNotif=jvmLowMemoryPoolCollectNotif, jvmOS=jvmOS, jvmMgtMIBMemoryNotifs=jvmMgtMIBMemoryNotifs, jvmThreadInstanceBlockGroup=jvmThreadInstanceBlockGroup, jmgt=jmgt, jvmMemoryPendingFinalCount=jvmMemoryPendingFinalCount, jvmRTBootClassPathSupport=jvmRTBootClassPathSupport, jvmMemPoolThreshdSupport=jvmMemPoolThreshdSupport, jvmMemPoolBasicGroup=jvmMemPoolBasicGroup, jvmClassesUnloadedCount=jvmClassesUnloadedCount, jvmMemMgrRelManagerName=jvmMemMgrRelManagerName, jvmRTClassPathIndex=jvmRTClassPathIndex, jvmRTVMVersion=jvmRTVMVersion, jvmClassLoading=jvmClassLoading, jvmThreadInstLockName=jvmThreadInstLockName, jvmOSArch=jvmOSArch, jvmMemPoolCollectMaxSize=jvmMemPoolCollectMaxSize, jvmMemPoolTable=jvmMemPoolTable, jvmRTLibraryPathEntry=jvmRTLibraryPathEntry, jvmMemPoolCollectCommitted=jvmMemPoolCollectCommitted, jvmThreadPeakCount=jvmThreadPeakCount, jvmThreadDaemonCount=jvmThreadDaemonCount, jvmThreadInstanceGroups=jvmThreadInstanceGroups, jvmThreadInstanceBasicGroup=jvmThreadInstanceBasicGroup, JvmUnsigned64TC=JvmUnsigned64TC, jvmMemoryHeapMaxSize=jvmMemoryHeapMaxSize, jvmThreadInstState=jvmThreadInstState, jvmMemPoolCollectThreshdSupport=jvmMemPoolCollectThreshdSupport, jvmRTInputArgsEntry=jvmRTInputArgsEntry, JvmPositive32TC=JvmPositive32TC, jvmMemGCEntry=jvmMemGCEntry, jvmRuntimeBasicGroup=jvmRuntimeBasicGroup, jvmRTLibraryPathIndex=jvmRTLibraryPathIndex, jvmJITCompilerGroups=jvmJITCompilerGroups, JvmImplSupportStateTC=JvmImplSupportStateTC, jvmManagementCompliance=jvmManagementCompliance, jvmMemGCTimeMs=jvmMemGCTimeMs, jvmClassesTotalLoadedCount=jvmClassesTotalLoadedCount, jvmRTSpecName=jvmRTSpecName, jvmClassLoadingBasicGroup=jvmClassLoadingBasicGroup, jvmMemorySetGroup=jvmMemorySetGroup, jvmMemGCGroup=jvmMemGCGroup, jvmMemPoolName=jvmMemPoolName, JvmImplOptFeatureStateTC=JvmImplOptFeatureStateTC, jvmLowMemoryCollectNotifGroup=jvmLowMemoryCollectNotifGroup, jvmThreadInstIndex=jvmThreadInstIndex, jvmMgtMIBCompliances=jvmMgtMIBCompliances, jvmMemMgrPoolRelTable=jvmMemMgrPoolRelTable, sun=sun, jvmThreadInstLockOwnerPtr=jvmThreadInstLockOwnerPtr, jvmThreadTotalStartedCount=jvmThreadTotalStartedCount, jvmOSVersion=jvmOSVersion, jvmMemManagerTable=jvmMemManagerTable, jvmThreadPeakCountReset=jvmThreadPeakCountReset, jvmMemPoolCollectThreshdCount=jvmMemPoolCollectThreshdCount, jvmMemMgrPoolRelEntry=jvmMemMgrPoolRelEntry, jvmMemGCCount=jvmMemGCCount, JvmVerboseLevelTC=JvmVerboseLevelTC, jvmMemoryHeapCommitted=jvmMemoryHeapCommitted, JvmIndex64TC=JvmIndex64TC, jvmRTUptimeMs=jvmRTUptimeMs, jvmMemMgrRelPoolName=jvmMemMgrRelPoolName, jvmRuntimeGroups=jvmRuntimeGroups, jvmMemManagerEntry=jvmMemManagerEntry, jvmMgtMIBNotifications=jvmMgtMIBNotifications, jvmThreadCount=jvmThreadCount, jvmRTManagementSpecVersion=jvmRTManagementSpecVersion, jvmMemPoolThreshdCount=jvmMemPoolThreshdCount, jvmMemManagerName=jvmMemManagerName, jvmMemPoolCommitted=jvmMemPoolCommitted, jvmMgtMIBConformance=jvmMgtMIBConformance, jvmMemoryNonHeapUsed=jvmMemoryNonHeapUsed, jvmRTClassPathTable=jvmRTClassPathTable, jvmRTInputArgsCount=jvmRTInputArgsCount, jvmMemPoolUsageGroup=jvmMemPoolUsageGroup, jvmMemPoolCollectUsageGroup=jvmMemPoolCollectUsageGroup, JvmThreadStateTC=JvmThreadStateTC, jvmThreadInstWaitCount=jvmThreadInstWaitCount, jvmOSProcessorCount=jvmOSProcessorCount, jvmMemoryGroups=jvmMemoryGroups, jvmClassesLoadedCount=jvmClassesLoadedCount, jvmRTInputArgsTable=jvmRTInputArgsTable, jvmLowMemoryUsageNotifGroup=jvmLowMemoryUsageNotifGroup, jvmJITCompilerBasicGroup=jvmJITCompilerBasicGroup, jvmMemManagerIndex=jvmMemManagerIndex, jvmRTVMVendor=jvmRTVMVendor, jvmMemPoolPeakReset=jvmMemPoolPeakReset, JvmPathElementTC=JvmPathElementTC, jvmMemPoolThreshold=jvmMemPoolThreshold, jvmRTStartTimeMs=jvmRTStartTimeMs, jvmRTLibraryPathItem=jvmRTLibraryPathItem, jvmMemPoolPeakUsageGroup=jvmMemPoolPeakUsageGroup, jvmMemory=jvmMemory, jvmThreadBasicGroup=jvmThreadBasicGroup, jvmMemPoolCollectThreshold=jvmMemPoolCollectThreshold, jvmMgtMIBLowMemoryNotifs=jvmMgtMIBLowMemoryNotifs, jvmMemoryHeapInitSize=jvmMemoryHeapInitSize, jvmMemPoolPeakUsed=jvmMemPoolPeakUsed, jvmRTInputArgsIndex=jvmRTInputArgsIndex, jvmMemPoolEntry=jvmMemPoolEntry, jvmMemoryNonHeapInitSize=jvmMemoryNonHeapInitSize, jvmJITCompilerTimeStatGroup=jvmJITCompilerTimeStatGroup, jvmCompilation=jvmCompilation, jvmClassLoadingGroups=jvmClassLoadingGroups, jvmThreadGroups=jvmThreadGroups, jvmLowMemoryPrefix=jvmLowMemoryPrefix, jvmMemPoolIndex=jvmMemPoolIndex, jvmRTBootClassPathItem=jvmRTBootClassPathItem, jvmRuntime=jvmRuntime, jvmClassesVerboseLevel=jvmClassesVerboseLevel, jvmMemGCTable=jvmMemGCTable, JvmTimeNanos64TC=JvmTimeNanos64TC, jvmThreadContentionMonitoring=jvmThreadContentionMonitoring, JvmArgValueTC=JvmArgValueTC, jvmMemPoolCollectMonitoringGroup=jvmMemPoolCollectMonitoringGroup, jvmMemPoolPeakCommitted=jvmMemPoolPeakCommitted, jvmMemoryNonHeapMaxSize=jvmMemoryNonHeapMaxSize, jvmThreadCpuTimeMonitoring=jvmThreadCpuTimeMonitoring, jvmMgtMIBObjects=jvmMgtMIBObjects, jvmMemPoolType=jvmMemPoolType, jvmMemPoolPeakMaxSize=jvmMemPoolPeakMaxSize, jvmThreadInstBlockTimeMs=jvmThreadInstBlockTimeMs, jvmRTSpecVersion=jvmRTSpecVersion, jvmJITCompilerTimeMonitoring=jvmJITCompilerTimeMonitoring, standard=standard, jvmMemManagerState=jvmMemManagerState, jvmThreadInstWaitTimeMs=jvmThreadInstWaitTimeMs, jvmMemoryBasicGroup=jvmMemoryBasicGroup, jvmMemPoolGroups=jvmMemPoolGroups, jvmThreadInstId=jvmThreadInstId, jvmMemoryNonHeapUsageGroup=jvmMemoryNonHeapUsageGroup, jvmMemoryHeapUsed=jvmMemoryHeapUsed, jvmMemPoolState=jvmMemPoolState, jvmMemoryGCVerboseLevel=jvmMemoryGCVerboseLevel, jvmThreadInstCpuTimeNs=jvmThreadInstCpuTimeNs, jvmRTBootClassPathIndex=jvmRTBootClassPathIndex, jvmMemoryHeapUsageGroup=jvmMemoryHeapUsageGroup, jvmMgtMIB=jvmMgtMIB, jvmMemPoolInitSize=jvmMemPoolInitSize, jvmMemoryGCCall=jvmMemoryGCCall, jvmMgtMIBGroups=jvmMgtMIBGroups, jvmMemoryNonHeapCommitted=jvmMemoryNonHeapCommitted, jvmLowMemoryPoolUsageNotif=jvmLowMemoryPoolUsageNotif, jvmRTVMName=jvmRTVMName, JvmValidityStateTC=JvmValidityStateTC, jvmThreadInstanceTable=jvmThreadInstanceTable, jvmThreadInstanceCpuGroup=jvmThreadInstanceCpuGroup, jvmRTClassPathItem=jvmRTClassPathItem, jvmRTClassPathEntry=jvmRTClassPathEntry, PYSNMP_MODULE_ID=jvmMgtMIB, jvmOSGroup=jvmOSGroup, jvmRTLibraryPathTable=jvmRTLibraryPathTable, JvmManagedMemoryTypeTC=JvmManagedMemoryTypeTC, jvmMemPoolMaxSize=jvmMemPoolMaxSize, jvmJITCompilerName=jvmJITCompilerName, JvmTimeMillis64TC=JvmTimeMillis64TC, jvmRTBootClassPathTable=jvmRTBootClassPathTable)
