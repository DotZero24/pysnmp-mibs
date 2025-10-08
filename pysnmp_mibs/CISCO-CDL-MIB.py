#
# PySNMP MIB module CISCO-CDL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-CDL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention")
ciscoCdlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 88))
ciscoCdlMIB.setRevisions(('2002-10-02 00:00', '2002-05-30 00:00',))
if mibBuilder.loadTexts: ciscoCdlMIB.setLastUpdated('200210020000Z')
if mibBuilder.loadTexts: ciscoCdlMIB.setOrganization('Cisco Systems, Inc.')
coCdlMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 0))
coCdlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 1))
coCdlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 3))
class CoCdlAggDefectIndStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("hopByHopForwardDefect", 0), ("hopByHopBackwardDefect", 1), ("endToEndAggPathForwardDefect", 2))

class CoCdlFlowDefectIndStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("endToEndPathImplicitFwdDefect", 0), ("endToEndPathBackwardDefect", 1))

class CoCdlNodeBehavior(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("endOfAggPath", 1), ("endOfHop", 2), ("cdlRegenerator", 3))

class CoCdlFlowIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

coCdlBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1))
coCdlFlowTermGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2))
coCdlIntfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1), )
if mibBuilder.loadTexts: coCdlIntfTable.setStatus('current')
coCdlIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: coCdlIntfEntry.setStatus('current')
coCdlAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlAdminStatus.setStatus('current')
coCdlForceEndOfHop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlForceEndOfHop.setStatus('current')
coCdlNodeBehavior = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 3), CoCdlNodeBehavior()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlNodeBehavior.setStatus('current')
coCdlRxAggDefectIndCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 4), CoCdlAggDefectIndStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxAggDefectIndCurrStatus.setStatus('current')
coCdlRxAggDefectIndLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxAggDefectIndLastChange.setStatus('current')
coCdlTxAggDefectIndCurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 6), CoCdlAggDefectIndStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlTxAggDefectIndCurrStatus.setStatus('current')
coCdlTxAggDefectIndLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlTxAggDefectIndLastChange.setStatus('current')
coCdlTransmitMaxFlowIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 8), CoCdlFlowIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlTransmitMaxFlowIdentifier.setStatus('current')
coCdlReceiveMaxFlowIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 9), CoCdlFlowIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlReceiveMaxFlowIdentifier.setStatus('current')
coCdlRxHeaderCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxHeaderCRCError.setStatus('current')
coCdlRxHeaderCRCErrorOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxHeaderCRCErrorOverflow.setStatus('current')
coCdlHCRxHeaderCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlHCRxHeaderCRCError.setStatus('current')
coCdlRxInvalidFlowID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxInvalidFlowID.setStatus('current')
coCdlRxInvalidFlowIDOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxInvalidFlowIDOverflow.setStatus('current')
coCdlHCRxInvalidFlowID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlHCRxInvalidFlowID.setStatus('current')
coCdlRxNonCdlPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxNonCdlPackets.setStatus('current')
coCdlRxNonCdlPacketsOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlRxNonCdlPacketsOverflow.setStatus('current')
coCdlHCRxNonCdlPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlHCRxNonCdlPackets.setStatus('current')
coCdlDefectIndNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledAtTerminatingInterfaces", 2), ("enabledAtAllInterfaces", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlDefectIndNotifyEnable.setStatus('current')
coCdlDefectIndSetSoakInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 60000)).clone(2500)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlDefectIndSetSoakInterval.setStatus('current')
coCdlDefectIndClearSoakInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 60000)).clone(10000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlDefectIndClearSoakInterval.setStatus('current')
coCdlDINotifyThrottleInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 60000)).clone(1000)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlDINotifyThrottleInterval.setStatus('current')
coCdlFlowTermTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1), )
if mibBuilder.loadTexts: coCdlFlowTermTable.setStatus('current')
coCdlFlowTermEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: coCdlFlowTermEntry.setStatus('current')
coCdlFromCdlNetFlowIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 1), CoCdlFlowIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlFromCdlNetFlowIdentifier.setStatus('current')
coCdlToCdlNetFlowIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 2), CoCdlFlowIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdlToCdlNetFlowIdentifier.setStatus('current')
coCdlFromCdlNetFlowDICurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 3), CoCdlFlowDefectIndStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlFromCdlNetFlowDICurrStatus.setStatus('current')
coCdlFromCdlNetFlowDILastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlFromCdlNetFlowDILastChange.setStatus('current')
coCdlToCdlNetFlowDICurrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 5), CoCdlFlowDefectIndStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlToCdlNetFlowDICurrStatus.setStatus('current')
coCdlToCdlNetFlowDILastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlToCdlNetFlowDILastChange.setStatus('current')
coCdlFromCdlNetEthernetCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlFromCdlNetEthernetCRC.setStatus('current')
coCdlFromCdlNetEthernetCRCOvrflw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlFromCdlNetEthernetCRCOvrflw.setStatus('current')
coCdlFromCdlNetHCEthernetCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 88, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdlFromCdlNetHCEthernetCRC.setStatus('current')
coCdlRxAggDefectIndChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 88, 0, 1)).setObjects(("CISCO-CDL-MIB", "coCdlRxAggDefectIndCurrStatus"), ("CISCO-CDL-MIB", "coCdlRxAggDefectIndLastChange"))
if mibBuilder.loadTexts: coCdlRxAggDefectIndChange.setStatus('current')
coCdlFromCdlNetFlowDIChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 88, 0, 2)).setObjects(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"), ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"))
if mibBuilder.loadTexts: coCdlFromCdlNetFlowDIChange.setStatus('current')
coCdlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1))
coCdlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2))
coCdlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1, 1)).setObjects(("CISCO-CDL-MIB", "coCdlMIBBaseGroup"), ("CISCO-CDL-MIB", "coCdlDIAggMandatoryGroup"), ("CISCO-CDL-MIB", "coCdlDIAggNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBCompliance = coCdlMIBCompliance.setStatus('deprecated')
coCdlMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 1, 2)).setObjects(("CISCO-CDL-MIB", "coCdlMIBBaseGroup"), ("CISCO-CDL-MIB", "coCdlDIAggMandatoryGroup"), ("CISCO-CDL-MIB", "coCdlDIAggNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBCompliance2 = coCdlMIBCompliance2.setStatus('current')
coCdlMIBBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 1)).setObjects(("CISCO-CDL-MIB", "coCdlAdminStatus"), ("CISCO-CDL-MIB", "coCdlNodeBehavior"), ("CISCO-CDL-MIB", "coCdlRxHeaderCRCError"), ("CISCO-CDL-MIB", "coCdlRxHeaderCRCErrorOverflow"), ("CISCO-CDL-MIB", "coCdlHCRxHeaderCRCError"), ("CISCO-CDL-MIB", "coCdlRxNonCdlPackets"), ("CISCO-CDL-MIB", "coCdlRxNonCdlPacketsOverflow"), ("CISCO-CDL-MIB", "coCdlHCRxNonCdlPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBBaseGroup = coCdlMIBBaseGroup.setStatus('current')
coCdlMIBFlowIdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 2)).setObjects(("CISCO-CDL-MIB", "coCdlTransmitMaxFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlReceiveMaxFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlRxInvalidFlowID"), ("CISCO-CDL-MIB", "coCdlRxInvalidFlowIDOverflow"), ("CISCO-CDL-MIB", "coCdlHCRxInvalidFlowID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBFlowIdGroup = coCdlMIBFlowIdGroup.setStatus('current')
coCdlMIBFlowTermGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 3)).setObjects(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"), ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDICurrStatus"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDILastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBFlowTermGroup = coCdlMIBFlowTermGroup.setStatus('deprecated')
coCdlDIConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 4)).setObjects(("CISCO-CDL-MIB", "coCdlForceEndOfHop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlDIConfigGroup = coCdlDIConfigGroup.setStatus('current')
coCdlDIAggMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 5)).setObjects(("CISCO-CDL-MIB", "coCdlRxAggDefectIndCurrStatus"), ("CISCO-CDL-MIB", "coCdlRxAggDefectIndLastChange"), ("CISCO-CDL-MIB", "coCdlTxAggDefectIndCurrStatus"), ("CISCO-CDL-MIB", "coCdlTxAggDefectIndLastChange"), ("CISCO-CDL-MIB", "coCdlDefectIndNotifyEnable"), ("CISCO-CDL-MIB", "coCdlDefectIndSetSoakInterval"), ("CISCO-CDL-MIB", "coCdlDefectIndClearSoakInterval"), ("CISCO-CDL-MIB", "coCdlDINotifyThrottleInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlDIAggMandatoryGroup = coCdlDIAggMandatoryGroup.setStatus('current')
coCdlDIAggNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 6)).setObjects(("CISCO-CDL-MIB", "coCdlRxAggDefectIndChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlDIAggNotifGroup = coCdlDIAggNotifGroup.setStatus('current')
coCdlDIFlowNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 7)).setObjects(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDIChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlDIFlowNotifGroup = coCdlDIFlowNotifGroup.setStatus('current')
coCdlMIBFlowTerm2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 88, 3, 2, 8)).setObjects(("CISCO-CDL-MIB", "coCdlFromCdlNetFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowIdentifier"), ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDICurrStatus"), ("CISCO-CDL-MIB", "coCdlFromCdlNetFlowDILastChange"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDICurrStatus"), ("CISCO-CDL-MIB", "coCdlToCdlNetFlowDILastChange"), ("CISCO-CDL-MIB", "coCdlFromCdlNetEthernetCRC"), ("CISCO-CDL-MIB", "coCdlFromCdlNetEthernetCRCOvrflw"), ("CISCO-CDL-MIB", "coCdlFromCdlNetHCEthernetCRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    coCdlMIBFlowTerm2Group = coCdlMIBFlowTerm2Group.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDL-MIB", coCdlHCRxInvalidFlowID=coCdlHCRxInvalidFlowID, CoCdlAggDefectIndStatus=CoCdlAggDefectIndStatus, coCdlTxAggDefectIndLastChange=coCdlTxAggDefectIndLastChange, coCdlTxAggDefectIndCurrStatus=coCdlTxAggDefectIndCurrStatus, coCdlHCRxHeaderCRCError=coCdlHCRxHeaderCRCError, coCdlMIBNotifications=coCdlMIBNotifications, coCdlFlowTermTable=coCdlFlowTermTable, coCdlToCdlNetFlowDILastChange=coCdlToCdlNetFlowDILastChange, coCdlMIBCompliance=coCdlMIBCompliance, coCdlMIBConformance=coCdlMIBConformance, coCdlAdminStatus=coCdlAdminStatus, coCdlFromCdlNetFlowIdentifier=coCdlFromCdlNetFlowIdentifier, coCdlRxInvalidFlowIDOverflow=coCdlRxInvalidFlowIDOverflow, coCdlForceEndOfHop=coCdlForceEndOfHop, coCdlMIBFlowIdGroup=coCdlMIBFlowIdGroup, coCdlFromCdlNetEthernetCRCOvrflw=coCdlFromCdlNetEthernetCRCOvrflw, coCdlFromCdlNetEthernetCRC=coCdlFromCdlNetEthernetCRC, coCdlFlowTermGroup=coCdlFlowTermGroup, coCdlMIBFlowTerm2Group=coCdlMIBFlowTerm2Group, coCdlRxNonCdlPacketsOverflow=coCdlRxNonCdlPacketsOverflow, CoCdlFlowIdentifier=CoCdlFlowIdentifier, coCdlToCdlNetFlowIdentifier=coCdlToCdlNetFlowIdentifier, coCdlReceiveMaxFlowIdentifier=coCdlReceiveMaxFlowIdentifier, coCdlFromCdlNetFlowDIChange=coCdlFromCdlNetFlowDIChange, coCdlDIAggNotifGroup=coCdlDIAggNotifGroup, coCdlRxNonCdlPackets=coCdlRxNonCdlPackets, coCdlMIBCompliance2=coCdlMIBCompliance2, coCdlDIConfigGroup=coCdlDIConfigGroup, coCdlMIBGroups=coCdlMIBGroups, coCdlDefectIndSetSoakInterval=coCdlDefectIndSetSoakInterval, coCdlNodeBehavior=coCdlNodeBehavior, ciscoCdlMIB=ciscoCdlMIB, coCdlMIBBaseGroup=coCdlMIBBaseGroup, coCdlIntfTable=coCdlIntfTable, coCdlDefectIndNotifyEnable=coCdlDefectIndNotifyEnable, coCdlRxAggDefectIndChange=coCdlRxAggDefectIndChange, CoCdlNodeBehavior=CoCdlNodeBehavior, coCdlDIFlowNotifGroup=coCdlDIFlowNotifGroup, coCdlBaseGroup=coCdlBaseGroup, coCdlRxAggDefectIndLastChange=coCdlRxAggDefectIndLastChange, coCdlRxInvalidFlowID=coCdlRxInvalidFlowID, coCdlTransmitMaxFlowIdentifier=coCdlTransmitMaxFlowIdentifier, coCdlDIAggMandatoryGroup=coCdlDIAggMandatoryGroup, coCdlRxAggDefectIndCurrStatus=coCdlRxAggDefectIndCurrStatus, coCdlDefectIndClearSoakInterval=coCdlDefectIndClearSoakInterval, coCdlMIBFlowTermGroup=coCdlMIBFlowTermGroup, coCdlHCRxNonCdlPackets=coCdlHCRxNonCdlPackets, coCdlRxHeaderCRCError=coCdlRxHeaderCRCError, coCdlFlowTermEntry=coCdlFlowTermEntry, coCdlToCdlNetFlowDICurrStatus=coCdlToCdlNetFlowDICurrStatus, coCdlRxHeaderCRCErrorOverflow=coCdlRxHeaderCRCErrorOverflow, coCdlFromCdlNetFlowDILastChange=coCdlFromCdlNetFlowDILastChange, coCdlFromCdlNetFlowDICurrStatus=coCdlFromCdlNetFlowDICurrStatus, coCdlMIBObjects=coCdlMIBObjects, PYSNMP_MODULE_ID=ciscoCdlMIB, coCdlFromCdlNetHCEthernetCRC=coCdlFromCdlNetHCEthernetCRC, coCdlIntfEntry=coCdlIntfEntry, CoCdlFlowDefectIndStatus=CoCdlFlowDefectIndStatus, coCdlDINotifyThrottleInterval=coCdlDINotifyThrottleInterval, coCdlMIBCompliances=coCdlMIBCompliances)
