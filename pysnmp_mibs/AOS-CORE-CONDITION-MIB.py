#
# PySNMP MIB module AOS-CORE-CONDITION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adva/AOS-CORE-CONDITION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aosCommon, = mibBuilder.importSymbols("ADVA-MIB", "aosCommon")
ConditionType, ConditionEntityTranslation, ConditionDescr = mibBuilder.importSymbols("AOS-CORE-ALARM-MIB", "ConditionType", "ConditionEntityTranslation", "ConditionDescr")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, TruthValue, RowPointer, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TruthValue", "RowPointer", "TextualConvention")
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
mibBuilder.exportSymbols("AOS-CORE-CONDITION-MIB", aosCoreConditionGroups=aosCoreConditionGroups, aosCoreConditionObjectGroup=aosCoreConditionObjectGroup, aosCoreConditionEntry=aosCoreConditionEntry, aosCoreConditionEntityTranslation=aosCoreConditionEntityTranslation, aosCoreConditionDescr=aosCoreConditionDescr, conditionObjects=conditionObjects, aosCoreConditionMIB=aosCoreConditionMIB, aosCoreConditionTable=aosCoreConditionTable, PYSNMP_MODULE_ID=aosCoreConditionMIB, aosCoreConditionIndex=aosCoreConditionIndex, aosCoreConditionCompliance=aosCoreConditionCompliance, aosCoreConditionType=aosCoreConditionType, aosCoreConditionEntity=aosCoreConditionEntity, aosCoreConditionTimestamp=aosCoreConditionTimestamp, aosCoreConditionCompliances=aosCoreConditionCompliances, conditionConformance=conditionConformance)
