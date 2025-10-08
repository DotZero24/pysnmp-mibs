#
# PySNMP MIB module INFINERA-TP-IFCOMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-IFCOMMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
commonTerminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "commonTerminationPoint")
InfnOpsQualifierList, InfnAvailabilityState = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnOpsQualifierList", "InfnAvailabilityState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ifCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1))
ifCommonMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: ifCommonMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: ifCommonMIB.setOrganization('Infinera')
ifCommonTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1), )
if mibBuilder.loadTexts: ifCommonTable.setStatus('current')
ifCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifCommonEntry.setStatus('current')
ifCommonMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCommonMoId.setStatus('current')
ifCommonAvailabilityState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 2), InfnAvailabilityState().clone('unavailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCommonAvailabilityState.setStatus('current')
ifCommonAlarmReportControl = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("inhibited", 2))).clone('allowed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifCommonAlarmReportControl.setStatus('current')
ifCommonOpStateQualifierList = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 4), InfnOpsQualifierList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCommonOpStateQualifierList.setStatus('current')
ifCommonAlarmInhibitState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("inhibited", 2))).clone('allowed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifCommonAlarmInhibitState.setStatus('current')
ifCommonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3))
ifCommonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 1))
ifCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 2))
ifCommonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 1, 1)).setObjects(("INFINERA-TP-IFCOMMON-MIB", "ifCommonGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCommonCompliance = ifCommonCompliance.setStatus('current')
ifCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 1, 3, 2, 1)).setObjects(("INFINERA-TP-IFCOMMON-MIB", "ifCommonMoId"), ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAvailabilityState"), ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAlarmReportControl"), ("INFINERA-TP-IFCOMMON-MIB", "ifCommonOpStateQualifierList"), ("INFINERA-TP-IFCOMMON-MIB", "ifCommonAlarmInhibitState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifCommonGroup = ifCommonGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-IFCOMMON-MIB", ifCommonAlarmReportControl=ifCommonAlarmReportControl, ifCommonConformance=ifCommonConformance, ifCommonGroup=ifCommonGroup, ifCommonTable=ifCommonTable, ifCommonGroups=ifCommonGroups, ifCommonAvailabilityState=ifCommonAvailabilityState, ifCommonEntry=ifCommonEntry, ifCommonMIB=ifCommonMIB, PYSNMP_MODULE_ID=ifCommonMIB, ifCommonOpStateQualifierList=ifCommonOpStateQualifierList, ifCommonAlarmInhibitState=ifCommonAlarmInhibitState, ifCommonCompliances=ifCommonCompliances, ifCommonCompliance=ifCommonCompliance, ifCommonMoId=ifCommonMoId)
