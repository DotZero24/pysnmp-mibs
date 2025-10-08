#
# PySNMP MIB module AOS-CORE-CONDITION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adva/AOS-CORE-CONDITION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:02:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
aosCommon, = mibBuilder.importSymbols("ADVA-MIB", "aosCommon")
ConditionEntityTranslation, ConditionDescr, ConditionType = mibBuilder.importSymbols("AOS-CORE-ALARM-MIB", "ConditionEntityTranslation", "ConditionDescr", "ConditionType")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, RowPointer, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "TruthValue", "TimeStamp", "DisplayString")
aosCoreConditionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2))
aosCoreConditionMIB.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: aosCoreConditionMIB.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: aosCoreConditionMIB.setOrganization('ADVA Optical Networking')
conditionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1))
conditionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2))
aosCoreConditionTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1), )
if mibBuilder.loadTexts: aosCoreConditionTable.setStatus('current')
aosCoreConditionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1), ).setIndexNames((0, "AOS-CORE-CONDITION-MIB", "aosCoreConditionIndex"))
if mibBuilder.loadTexts: aosCoreConditionEntry.setStatus('current')
aosCoreConditionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aosCoreConditionIndex.setStatus('current')
aosCoreConditionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 2), ConditionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreConditionType.setStatus('current')
aosCoreConditionEntityTranslation = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 3), ConditionEntityTranslation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreConditionEntityTranslation.setStatus('current')
aosCoreConditionEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 4), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreConditionEntity.setStatus('current')
aosCoreConditionDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 5), ConditionDescr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreConditionDescr.setStatus('current')
aosCoreConditionTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aosCoreConditionTimestamp.setStatus('current')
aosCoreConditionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 1))
aosCoreConditionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 2))
aosCoreConditionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 1, 1)).setObjects(("AOS-CORE-CONDITION-MIB", "aosCoreConditionObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aosCoreConditionCompliance = aosCoreConditionCompliance.setStatus('current')
aosCoreConditionObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 2, 2, 2, 1)).setObjects(("AOS-CORE-CONDITION-MIB", "aosCoreConditionIndex"), ("AOS-CORE-CONDITION-MIB", "aosCoreConditionType"), ("AOS-CORE-CONDITION-MIB", "aosCoreConditionEntityTranslation"), ("AOS-CORE-CONDITION-MIB", "aosCoreConditionEntity"), ("AOS-CORE-CONDITION-MIB", "aosCoreConditionDescr"), ("AOS-CORE-CONDITION-MIB", "aosCoreConditionTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aosCoreConditionObjectGroup = aosCoreConditionObjectGroup.setStatus('current')
mibBuilder.exportSymbols("AOS-CORE-CONDITION-MIB", PYSNMP_MODULE_ID=aosCoreConditionMIB, aosCoreConditionEntry=aosCoreConditionEntry, aosCoreConditionDescr=aosCoreConditionDescr, aosCoreConditionType=aosCoreConditionType, aosCoreConditionCompliances=aosCoreConditionCompliances, aosCoreConditionMIB=aosCoreConditionMIB, aosCoreConditionTimestamp=aosCoreConditionTimestamp, aosCoreConditionGroups=aosCoreConditionGroups, aosCoreConditionObjectGroup=aosCoreConditionObjectGroup, aosCoreConditionEntityTranslation=aosCoreConditionEntityTranslation, aosCoreConditionIndex=aosCoreConditionIndex, aosCoreConditionTable=aosCoreConditionTable, aosCoreConditionCompliance=aosCoreConditionCompliance, aosCoreConditionEntity=aosCoreConditionEntity, conditionObjects=conditionObjects, conditionConformance=conditionConformance)
