#
# PySNMP MIB module ARC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/ARC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
ResourceId, = mibBuilder.importSymbols("ALARM-MIB", "ResourceId")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, RowStatus, TextualConvention, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "StorageType")
arcMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 117))
arcMibModule.setRevisions(('2004-09-09 00:00',))
if mibBuilder.loadTexts: arcMibModule.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: arcMibModule.setOrganization('IETF Distributed Management Working Group')
class IANAItuProbableCauseOrZero(TextualConvention, Integer32):
    reference = 'IANA-ITU-ALARM-TC MIB module as maintained at the IANA web site. The initial module was also published in RFC 3877.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

arcTimeIntervals = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 1))
arcObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 2))
arcTITimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcTITimeInterval.setStatus('current')
arcCDTimeInterval = MibScalar((1, 3, 6, 1, 2, 1, 117, 1, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: arcCDTimeInterval.setStatus('current')
arcTable = MibTable((1, 3, 6, 1, 2, 1, 117, 2, 1), )
if mibBuilder.loadTexts: arcTable.setStatus('current')
arcEntry = MibTableRow((1, 3, 6, 1, 2, 1, 117, 2, 1, 1), ).setIndexNames((0, "ARC-MIB", "arcIndex"), (0, "ARC-MIB", "arcAlarmType"), (0, "ARC-MIB", "arcNotificationId"))
if mibBuilder.loadTexts: arcEntry.setStatus('current')
arcIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 1), ResourceId())
if mibBuilder.loadTexts: arcIndex.setStatus('current')
arcAlarmType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 2), IANAItuProbableCauseOrZero())
if mibBuilder.loadTexts: arcAlarmType.setStatus('current')
arcNotificationId = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arcNotificationId.setStatus('current')
arcState = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nalm", 1), ("nalmQI", 2), ("nalmTI", 3), ("nalmQICD", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcState.setStatus('current')
arcNalmTimeRemaining = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcNalmTimeRemaining.setStatus('current')
arcRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcRowStatus.setStatus('current')
arcStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 117, 2, 1, 1, 7), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: arcStorageType.setStatus('current')
arcConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3))
arcCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 1))
arcCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 117, 3, 1, 1)).setObjects(("ARC-MIB", "arcSettingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcCompliance = arcCompliance.setStatus('current')
arcGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 117, 3, 2))
arcSettingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 1)).setObjects(("ARC-MIB", "arcState"), ("ARC-MIB", "arcRowStatus"), ("ARC-MIB", "arcStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcSettingGroup = arcSettingGroup.setStatus('current')
arcTIGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 2)).setObjects(("ARC-MIB", "arcTITimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcTIGroup = arcTIGroup.setStatus('current')
arcQICDGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 117, 3, 2, 3)).setObjects(("ARC-MIB", "arcCDTimeInterval"), ("ARC-MIB", "arcNalmTimeRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    arcQICDGroup = arcQICDGroup.setStatus('current')
mibBuilder.exportSymbols("ARC-MIB", arcQICDGroup=arcQICDGroup, arcAlarmType=arcAlarmType, PYSNMP_MODULE_ID=arcMibModule, arcTimeIntervals=arcTimeIntervals, arcRowStatus=arcRowStatus, arcSettingGroup=arcSettingGroup, arcNalmTimeRemaining=arcNalmTimeRemaining, IANAItuProbableCauseOrZero=IANAItuProbableCauseOrZero, arcEntry=arcEntry, arcCDTimeInterval=arcCDTimeInterval, arcCompliance=arcCompliance, arcNotificationId=arcNotificationId, arcTIGroup=arcTIGroup, arcIndex=arcIndex, arcObjects=arcObjects, arcState=arcState, arcCompliances=arcCompliances, arcConformance=arcConformance, arcTITimeInterval=arcTITimeInterval, arcStorageType=arcStorageType, arcGroups=arcGroups, arcTable=arcTable, arcMibModule=arcMibModule)
