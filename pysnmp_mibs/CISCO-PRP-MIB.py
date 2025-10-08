#
# PySNMP MIB module CISCO-PRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-PRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 866))
ciscoPrpMIB.setRevisions(('2019-09-11 00:00',))
if mibBuilder.loadTexts: ciscoPrpMIB.setLastUpdated('201909110000Z')
if mibBuilder.loadTexts: ciscoPrpMIB.setOrganization('Cisco Systems, Inc.')
class PrpStatus(TextualConvention, Integer32):
    reference = 'Prp channel or LAN status'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("stateUp", 1), ("stateDown", 2))

ciscoPrpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 0))
ciscoPrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 1))
ciscoPrpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2))
ciscoPrpChannelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1), )
if mibBuilder.loadTexts: ciscoPrpChannelTable.setStatus('current')
ciscoPrpChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1), ).setIndexNames((0, "CISCO-PRP-MIB", "ciscoPrpChannelIndex"))
if mibBuilder.loadTexts: ciscoPrpChannelEntry.setStatus('current')
ciscoPrpChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ciscoPrpChannelIndex.setStatus('current')
ciscoPrpChannelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelId.setStatus('current')
ciscoPrpChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelName.setStatus('current')
ciscoPrpChannelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 4), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelStatus.setStatus('current')
ciscoPrpChannelLanAStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 5), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanAStatus.setStatus('current')
ciscoPrpChannelLanBStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 866, 1, 1, 1, 6), PrpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPrpChannelLanBStatus.setStatus('current')
ciscoPrpChannelStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"))
if mibBuilder.loadTexts: ciscoPrpChannelStateChange.setStatus('current')
ciscoPrpLanAStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"))
if mibBuilder.loadTexts: ciscoPrpLanAStateChange.setStatus('current')
ciscoPrpLanBStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 866, 0, 3)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"))
if mibBuilder.loadTexts: ciscoPrpLanBStateChange.setStatus('current')
ciscoPrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1))
ciscoPrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2))
ciscoPrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 1, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpMIBMainObjectGroup"), ("CISCO-PRP-MIB", "ciscoPrpMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBCompliance = ciscoPrpMIBCompliance.setStatus('current')
ciscoPrpMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 1)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelId"), ("CISCO-PRP-MIB", "ciscoPrpChannelStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanAStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelLanBStatus"), ("CISCO-PRP-MIB", "ciscoPrpChannelName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBMainObjectGroup = ciscoPrpMIBMainObjectGroup.setStatus('current')
ciscoPrpMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 866, 2, 2, 2)).setObjects(("CISCO-PRP-MIB", "ciscoPrpChannelStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanAStateChange"), ("CISCO-PRP-MIB", "ciscoPrpLanBStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrpMIBNotificationGroup = ciscoPrpMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRP-MIB", PrpStatus=PrpStatus, ciscoPrpLanAStateChange=ciscoPrpLanAStateChange, ciscoPrpMIBConform=ciscoPrpMIBConform, ciscoPrpChannelIndex=ciscoPrpChannelIndex, ciscoPrpMIBNotifs=ciscoPrpMIBNotifs, ciscoPrpMIBGroups=ciscoPrpMIBGroups, ciscoPrpMIBObjects=ciscoPrpMIBObjects, ciscoPrpMIB=ciscoPrpMIB, ciscoPrpChannelTable=ciscoPrpChannelTable, ciscoPrpMIBCompliance=ciscoPrpMIBCompliance, PYSNMP_MODULE_ID=ciscoPrpMIB, ciscoPrpLanBStateChange=ciscoPrpLanBStateChange, ciscoPrpMIBNotificationGroup=ciscoPrpMIBNotificationGroup, ciscoPrpMIBMainObjectGroup=ciscoPrpMIBMainObjectGroup, ciscoPrpChannelName=ciscoPrpChannelName, ciscoPrpMIBCompliances=ciscoPrpMIBCompliances, ciscoPrpChannelId=ciscoPrpChannelId, ciscoPrpChannelStateChange=ciscoPrpChannelStateChange, ciscoPrpChannelStatus=ciscoPrpChannelStatus, ciscoPrpChannelEntry=ciscoPrpChannelEntry, ciscoPrpChannelLanAStatus=ciscoPrpChannelLanAStatus, ciscoPrpChannelLanBStatus=ciscoPrpChannelLanBStatus)
