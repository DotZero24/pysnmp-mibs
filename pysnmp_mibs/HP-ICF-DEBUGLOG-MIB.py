#
# PySNMP MIB module HP-ICF-DEBUGLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-DEBUGLOG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpicfDebugLog, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfDebugLog")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hpicfDebugLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1))
hpicfDebugLogMib.setRevisions(('2017-07-04 00:00', '2016-03-18 00:00', '2016-02-17 00:00', '2009-09-22 00:00',))
if mibBuilder.loadTexts: hpicfDebugLogMib.setLastUpdated('201707040000Z')
if mibBuilder.loadTexts: hpicfDebugLogMib.setOrganization('HP Networking')
class HpicfDebugDestType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("syslog", 1), ("buffer", 2))

class HpicfDebugLogLevels(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("quiet", 0), ("fatal", 1), ("error", 2), ("info", 3), ("verbose", 4), ("debug", 5), ("debug2", 6), ("debug3", 7))

hpicfDebugLogObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1))
hpicfDebugLogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2))
hpicfDebugLogControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfDebugLogControlTable.setStatus('current')
hpicfDebugLogControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogIndex"))
if mibBuilder.loadTexts: hpicfDebugLogControlEntry.setStatus('current')
hpicfDebugLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpicfDebugLogIndex.setStatus('current')
hpicfDebugLogDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogDescr.setStatus('current')
hpicfDebugLogContainedIn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDebugLogContainedIn.setStatus('current')
hpicfDebugLogStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogStatus.setStatus('current')
hpicfDebugLogPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogPersistent.setStatus('current')
hpicfDebugLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 2), HpicfDebugLogLevels().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugLogLevel.setStatus('current')
hpicfDebugDestControlTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3), )
if mibBuilder.loadTexts: hpicfDebugDestControlTable.setStatus('current')
hpicfDebugDestControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1), ).setIndexNames((0, "HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestIndex"))
if mibBuilder.loadTexts: hpicfDebugDestControlEntry.setStatus('current')
hpicfDebugDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 1), HpicfDebugDestType())
if mibBuilder.loadTexts: hpicfDebugDestIndex.setStatus('current')
hpicfDebugDestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestStatus.setStatus('current')
hpicfDebugDestPersistent = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugDestPersistent.setStatus('current')
hpicfDebugTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDebugTimeStamp.setStatus('current')
hpicfDebugLogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1))
hpicfDebugLogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2))
hpicfDebugDestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3))
hpicfDebugTimeStampGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4))
hpicfDebugLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 2, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogDescr"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogContainedIn"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogLevel"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogGroup = hpicfDebugLogGroup.setStatus('current')
hpicfDebugDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 3, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestStatus"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestPersistent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugDestGroup = hpicfDebugDestGroup.setStatus('current')
hpicfDebugTimeStampGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 4, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugTimeStampGroup = hpicfDebugTimeStampGroup.setStatus('current')
hpicfDebugLogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 1)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance = hpicfDebugLogCompliance.setStatus('deprecated')
hpicfDebugLogCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64, 1, 2, 1, 2)).setObjects(("HP-ICF-DEBUGLOG-MIB", "hpicfDebugLogGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugDestGroup"), ("HP-ICF-DEBUGLOG-MIB", "hpicfDebugTimeStampGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDebugLogCompliance1 = hpicfDebugLogCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DEBUGLOG-MIB", hpicfDebugTimeStamp=hpicfDebugTimeStamp, hpicfDebugTimeStampGroups=hpicfDebugTimeStampGroups, hpicfDebugLogControlEntry=hpicfDebugLogControlEntry, hpicfDebugDestIndex=hpicfDebugDestIndex, HpicfDebugDestType=HpicfDebugDestType, hpicfDebugLogPersistent=hpicfDebugLogPersistent, hpicfDebugLogCompliances=hpicfDebugLogCompliances, hpicfDebugDestControlTable=hpicfDebugDestControlTable, hpicfDebugLogCompliance=hpicfDebugLogCompliance, hpicfDebugLogContainedIn=hpicfDebugLogContainedIn, hpicfDebugDestControlEntry=hpicfDebugDestControlEntry, hpicfDebugLogGroup=hpicfDebugLogGroup, hpicfDebugLogObjects=hpicfDebugLogObjects, hpicfDebugLogCompliance1=hpicfDebugLogCompliance1, hpicfDebugLogDescr=hpicfDebugLogDescr, hpicfDebugDestGroup=hpicfDebugDestGroup, hpicfDebugLogMib=hpicfDebugLogMib, hpicfDebugDestGroups=hpicfDebugDestGroups, hpicfDebugTimeStampGroup=hpicfDebugTimeStampGroup, hpicfDebugLogIndex=hpicfDebugLogIndex, PYSNMP_MODULE_ID=hpicfDebugLogMib, hpicfDebugLogControlTable=hpicfDebugLogControlTable, HpicfDebugLogLevels=HpicfDebugLogLevels, hpicfDebugLogLevel=hpicfDebugLogLevel, hpicfDebugLogStatus=hpicfDebugLogStatus, hpicfDebugLogGroups=hpicfDebugLogGroups, hpicfDebugDestPersistent=hpicfDebugDestPersistent, hpicfDebugDestStatus=hpicfDebugDestStatus, hpicfDebugLogConformance=hpicfDebugLogConformance)
