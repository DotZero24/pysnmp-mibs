#
# PySNMP MIB module TRAPEZE-NETWORKS-TRAPLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-TRAPLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
TimeStamp, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "DateAndTime", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzTraplogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 13))
trpzTraplogMib.setRevisions(('2009-03-22 00:09',))
if mibBuilder.loadTexts: trpzTraplogMib.setLastUpdated('200903220009Z')
if mibBuilder.loadTexts: trpzTraplogMib.setOrganization('Trapeze Networks')
class TrpzTraplogTrapOccurrenceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TrpzTraplogTrapOccurrenceIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
trpzTraplogMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1))
trpzTraplogGuideObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2))
trpzTraplogOldestTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 1), TrpzTraplogTrapOccurrenceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogOldestTrapIndex.setStatus('current')
trpzTraplogNewestTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 2), TrpzTraplogTrapOccurrenceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogNewestTrapIndex.setStatus('current')
trpzTraplogNewestTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogNewestTrapTime.setStatus('current')
trpzTraplogNewestTrapDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 2, 4), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogNewestTrapDateAndTime.setStatus('current')
trpzTraplogTrapTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3), )
if mibBuilder.loadTexts: trpzTraplogTrapTable.setStatus('current')
trpzTraplogTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapIndex"))
if mibBuilder.loadTexts: trpzTraplogTrapEntry.setStatus('current')
trpzTraplogTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 1), TrpzTraplogTrapOccurrenceIndex())
if mibBuilder.loadTexts: trpzTraplogTrapIndex.setStatus('current')
trpzTraplogTrapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogTrapTime.setStatus('current')
trpzTraplogTrapDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogTrapDateAndTime.setStatus('current')
trpzTraplogTrapNotificationID = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogTrapNotificationID.setStatus('current')
trpzTraplogTrapNumVars = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogTrapNumVars.setStatus('current')
trpzTraplogVarTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4), )
if mibBuilder.loadTexts: trpzTraplogVarTable.setStatus('current')
trpzTraplogVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarTrapIndex"), (0, "TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarIndex"))
if mibBuilder.loadTexts: trpzTraplogVarEntry.setStatus('current')
trpzTraplogVarTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 1), TrpzTraplogTrapOccurrenceIndex())
if mibBuilder.loadTexts: trpzTraplogVarTrapIndex.setStatus('current')
trpzTraplogVarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: trpzTraplogVarIndex.setStatus('current')
trpzTraplogVarID = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarID.setStatus('current')
trpzTraplogVarValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarValueType.setStatus('current')
trpzTraplogVarCounter32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarCounter32Val.setStatus('current')
trpzTraplogVarUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarUnsigned32Val.setStatus('current')
trpzTraplogVarTimeTicksVal = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarTimeTicksVal.setStatus('current')
trpzTraplogVarInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarInteger32Val.setStatus('current')
trpzTraplogVarOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarOctetStringVal.setStatus('current')
trpzTraplogVarIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarIpAddressVal.setStatus('current')
trpzTraplogVarOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 11), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarOidVal.setStatus('current')
trpzTraplogVarCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 13, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzTraplogVarCounter64Val.setStatus('current')
trpzTraplogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2))
trpzTraplogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 1))
trpzTraplogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2))
trpzTraplogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogGuideGroup"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapGroup"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarGroup"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogGuideDateGroup"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapDateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogCompliance = trpzTraplogCompliance.setStatus('current')
trpzTraplogGuideGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogOldestTrapIndex"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapIndex"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogGuideGroup = trpzTraplogGuideGroup.setStatus('current')
trpzTraplogGuideDateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 2)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogNewestTrapDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogGuideDateGroup = trpzTraplogGuideDateGroup.setStatus('current')
trpzTraplogTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 3)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapTime"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapNotificationID"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapNumVars"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogTrapGroup = trpzTraplogTrapGroup.setStatus('current')
trpzTraplogTrapDateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 4)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogTrapDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogTrapDateGroup = trpzTraplogTrapDateGroup.setStatus('current')
trpzTraplogVarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 13, 2, 2, 5)).setObjects(("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarID"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarValueType"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarCounter32Val"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarUnsigned32Val"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarTimeTicksVal"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarInteger32Val"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarOctetStringVal"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarIpAddressVal"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarOidVal"), ("TRAPEZE-NETWORKS-TRAPLOG-MIB", "trpzTraplogVarCounter64Val"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzTraplogVarGroup = trpzTraplogVarGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-TRAPLOG-MIB", trpzTraplogVarOidVal=trpzTraplogVarOidVal, trpzTraplogVarIpAddressVal=trpzTraplogVarIpAddressVal, TrpzTraplogTrapOccurrenceIndexOrZero=TrpzTraplogTrapOccurrenceIndexOrZero, trpzTraplogVarTable=trpzTraplogVarTable, trpzTraplogVarCounter32Val=trpzTraplogVarCounter32Val, trpzTraplogTrapNumVars=trpzTraplogTrapNumVars, trpzTraplogTrapEntry=trpzTraplogTrapEntry, trpzTraplogMibObjects=trpzTraplogMibObjects, trpzTraplogVarIndex=trpzTraplogVarIndex, trpzTraplogTrapTime=trpzTraplogTrapTime, trpzTraplogGuideGroup=trpzTraplogGuideGroup, trpzTraplogCompliance=trpzTraplogCompliance, trpzTraplogVarTimeTicksVal=trpzTraplogVarTimeTicksVal, trpzTraplogTrapGroup=trpzTraplogTrapGroup, trpzTraplogTrapDateGroup=trpzTraplogTrapDateGroup, trpzTraplogNewestTrapDateAndTime=trpzTraplogNewestTrapDateAndTime, trpzTraplogVarUnsigned32Val=trpzTraplogVarUnsigned32Val, trpzTraplogNewestTrapTime=trpzTraplogNewestTrapTime, trpzTraplogTrapTable=trpzTraplogTrapTable, trpzTraplogTrapNotificationID=trpzTraplogTrapNotificationID, trpzTraplogVarCounter64Val=trpzTraplogVarCounter64Val, trpzTraplogGuideObjects=trpzTraplogGuideObjects, trpzTraplogNewestTrapIndex=trpzTraplogNewestTrapIndex, trpzTraplogMib=trpzTraplogMib, trpzTraplogVarID=trpzTraplogVarID, trpzTraplogVarTrapIndex=trpzTraplogVarTrapIndex, trpzTraplogGroups=trpzTraplogGroups, trpzTraplogConformance=trpzTraplogConformance, trpzTraplogGuideDateGroup=trpzTraplogGuideDateGroup, trpzTraplogVarValueType=trpzTraplogVarValueType, trpzTraplogVarInteger32Val=trpzTraplogVarInteger32Val, trpzTraplogVarGroup=trpzTraplogVarGroup, trpzTraplogOldestTrapIndex=trpzTraplogOldestTrapIndex, TrpzTraplogTrapOccurrenceIndex=TrpzTraplogTrapOccurrenceIndex, trpzTraplogVarEntry=trpzTraplogVarEntry, trpzTraplogTrapDateAndTime=trpzTraplogTrapDateAndTime, PYSNMP_MODULE_ID=trpzTraplogMib, trpzTraplogTrapIndex=trpzTraplogTrapIndex, trpzTraplogCompliances=trpzTraplogCompliances, trpzTraplogVarOctetStringVal=trpzTraplogVarOctetStringVal)
