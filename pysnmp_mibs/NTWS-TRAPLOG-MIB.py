#
# PySNMP MIB module NTWS-TRAPLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-TRAPLOG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
TimeStamp, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "DateAndTime", "TextualConvention")
ntwsTraplogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13))
ntwsTraplogMib.setRevisions(('2009-03-22 00:09',))
if mibBuilder.loadTexts: ntwsTraplogMib.setLastUpdated('200903220009Z')
if mibBuilder.loadTexts: ntwsTraplogMib.setOrganization('Nortel Networks')
class NtwsTraplogTrapOccurrenceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NtwsTraplogTrapOccurrenceIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
ntwsTraplogMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1))
ntwsTraplogGuideObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2))
ntwsTraplogOldestTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 1), NtwsTraplogTrapOccurrenceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogOldestTrapIndex.setStatus('current')
ntwsTraplogNewestTrapIndex = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 2), NtwsTraplogTrapOccurrenceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogNewestTrapIndex.setStatus('current')
ntwsTraplogNewestTrapTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogNewestTrapTime.setStatus('current')
ntwsTraplogNewestTrapDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 4), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogNewestTrapDateAndTime.setStatus('current')
ntwsTraplogTrapTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3), )
if mibBuilder.loadTexts: ntwsTraplogTrapTable.setStatus('current')
ntwsTraplogTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1), ).setIndexNames((0, "NTWS-TRAPLOG-MIB", "ntwsTraplogTrapIndex"))
if mibBuilder.loadTexts: ntwsTraplogTrapEntry.setStatus('current')
ntwsTraplogTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 1), NtwsTraplogTrapOccurrenceIndex())
if mibBuilder.loadTexts: ntwsTraplogTrapIndex.setStatus('current')
ntwsTraplogTrapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogTrapTime.setStatus('current')
ntwsTraplogTrapDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogTrapDateAndTime.setStatus('current')
ntwsTraplogTrapNotificationID = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogTrapNotificationID.setStatus('current')
ntwsTraplogTrapNumVars = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogTrapNumVars.setStatus('current')
ntwsTraplogVarTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4), )
if mibBuilder.loadTexts: ntwsTraplogVarTable.setStatus('current')
ntwsTraplogVarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1), ).setIndexNames((0, "NTWS-TRAPLOG-MIB", "ntwsTraplogVarTrapIndex"), (0, "NTWS-TRAPLOG-MIB", "ntwsTraplogVarIndex"))
if mibBuilder.loadTexts: ntwsTraplogVarEntry.setStatus('current')
ntwsTraplogVarTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 1), NtwsTraplogTrapOccurrenceIndex())
if mibBuilder.loadTexts: ntwsTraplogVarTrapIndex.setStatus('current')
ntwsTraplogVarIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ntwsTraplogVarIndex.setStatus('current')
ntwsTraplogVarID = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarID.setStatus('current')
ntwsTraplogVarValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarValueType.setStatus('current')
ntwsTraplogVarCounter32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarCounter32Val.setStatus('current')
ntwsTraplogVarUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarUnsigned32Val.setStatus('current')
ntwsTraplogVarTimeTicksVal = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarTimeTicksVal.setStatus('current')
ntwsTraplogVarInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarInteger32Val.setStatus('current')
ntwsTraplogVarOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarOctetStringVal.setStatus('current')
ntwsTraplogVarIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarIpAddressVal.setStatus('current')
ntwsTraplogVarOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 11), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarOidVal.setStatus('current')
ntwsTraplogVarCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsTraplogVarCounter64Val.setStatus('current')
ntwsTraplogConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2))
ntwsTraplogCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 1))
ntwsTraplogGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2))
ntwsTraplogCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 1, 1)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogGuideGroup"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapGroup"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarGroup"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogGuideDateGroup"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapDateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogCompliance = ntwsTraplogCompliance.setStatus('current')
ntwsTraplogGuideGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 1)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogOldestTrapIndex"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapIndex"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogGuideGroup = ntwsTraplogGuideGroup.setStatus('current')
ntwsTraplogGuideDateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 2)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogGuideDateGroup = ntwsTraplogGuideDateGroup.setStatus('current')
ntwsTraplogTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 3)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapTime"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapNotificationID"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapNumVars"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogTrapGroup = ntwsTraplogTrapGroup.setStatus('current')
ntwsTraplogTrapDateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 4)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapDateAndTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogTrapDateGroup = ntwsTraplogTrapDateGroup.setStatus('current')
ntwsTraplogVarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 5)).setObjects(("NTWS-TRAPLOG-MIB", "ntwsTraplogVarID"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarValueType"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarCounter32Val"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarUnsigned32Val"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarTimeTicksVal"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarInteger32Val"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarOctetStringVal"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarIpAddressVal"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarOidVal"), ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarCounter64Val"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsTraplogVarGroup = ntwsTraplogVarGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-TRAPLOG-MIB", ntwsTraplogTrapDateGroup=ntwsTraplogTrapDateGroup, ntwsTraplogVarInteger32Val=ntwsTraplogVarInteger32Val, ntwsTraplogVarGroup=ntwsTraplogVarGroup, ntwsTraplogMibObjects=ntwsTraplogMibObjects, ntwsTraplogTrapDateAndTime=ntwsTraplogTrapDateAndTime, ntwsTraplogTrapTime=ntwsTraplogTrapTime, ntwsTraplogOldestTrapIndex=ntwsTraplogOldestTrapIndex, ntwsTraplogTrapGroup=ntwsTraplogTrapGroup, ntwsTraplogNewestTrapIndex=ntwsTraplogNewestTrapIndex, ntwsTraplogConformance=ntwsTraplogConformance, ntwsTraplogVarEntry=ntwsTraplogVarEntry, ntwsTraplogTrapNumVars=ntwsTraplogTrapNumVars, ntwsTraplogVarUnsigned32Val=ntwsTraplogVarUnsigned32Val, ntwsTraplogCompliances=ntwsTraplogCompliances, ntwsTraplogNewestTrapTime=ntwsTraplogNewestTrapTime, ntwsTraplogTrapNotificationID=ntwsTraplogTrapNotificationID, ntwsTraplogGuideObjects=ntwsTraplogGuideObjects, ntwsTraplogVarCounter32Val=ntwsTraplogVarCounter32Val, ntwsTraplogVarID=ntwsTraplogVarID, ntwsTraplogVarTimeTicksVal=ntwsTraplogVarTimeTicksVal, ntwsTraplogVarValueType=ntwsTraplogVarValueType, ntwsTraplogVarCounter64Val=ntwsTraplogVarCounter64Val, ntwsTraplogGroups=ntwsTraplogGroups, ntwsTraplogVarTable=ntwsTraplogVarTable, ntwsTraplogVarIpAddressVal=ntwsTraplogVarIpAddressVal, ntwsTraplogVarIndex=ntwsTraplogVarIndex, NtwsTraplogTrapOccurrenceIndex=NtwsTraplogTrapOccurrenceIndex, ntwsTraplogGuideDateGroup=ntwsTraplogGuideDateGroup, ntwsTraplogNewestTrapDateAndTime=ntwsTraplogNewestTrapDateAndTime, ntwsTraplogVarOctetStringVal=ntwsTraplogVarOctetStringVal, ntwsTraplogMib=ntwsTraplogMib, ntwsTraplogCompliance=ntwsTraplogCompliance, ntwsTraplogTrapTable=ntwsTraplogTrapTable, ntwsTraplogTrapIndex=ntwsTraplogTrapIndex, ntwsTraplogGuideGroup=ntwsTraplogGuideGroup, NtwsTraplogTrapOccurrenceIndexOrZero=NtwsTraplogTrapOccurrenceIndexOrZero, ntwsTraplogVarOidVal=ntwsTraplogVarOidVal, ntwsTraplogVarTrapIndex=ntwsTraplogVarTrapIndex, ntwsTraplogTrapEntry=ntwsTraplogTrapEntry, PYSNMP_MODULE_ID=ntwsTraplogMib)
