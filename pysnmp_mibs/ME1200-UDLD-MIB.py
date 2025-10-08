#
# PySNMP MIB module ME1200-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/ME1200-UDLD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200DisplayString, ME1200InterfaceIndex = mibBuilder.importSymbols("ME1200-TC", "ME1200DisplayString", "ME1200InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
me1200UdldMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123))
me1200UdldMib.setRevisions(('2014-03-11 00:00',))
if mibBuilder.loadTexts: me1200UdldMib.setLastUpdated('201403110000Z')
if mibBuilder.loadTexts: me1200UdldMib.setOrganization('Cisco Systems, Inc')
class ME1200UdldDetectionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("inDeterminant", 0), ("uniDirectional", 1), ("biDirectional", 2), ("neighborMismatch", 3), ("loopback", 4), ("multipleNeighbor", 5))

class ME1200UdldMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disable", 0), ("normal", 1), ("aggressive", 2))

me1200UdldMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1))
me1200UdldConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2))
me1200UdldConfigInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1))
me1200UdldConfigInterfaceParamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1), )
if mibBuilder.loadTexts: me1200UdldConfigInterfaceParamTable.setStatus('current')
me1200UdldConfigInterfaceParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1), ).setIndexNames((0, "ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamIfIndex"))
if mibBuilder.loadTexts: me1200UdldConfigInterfaceParamEntry.setStatus('current')
me1200UdldConfigInterfaceParamIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 1), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200UdldConfigInterfaceParamIfIndex.setStatus('current')
me1200UdldConfigInterfaceParamUdldMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 2), ME1200UdldMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200UdldConfigInterfaceParamUdldMode.setStatus('current')
me1200UdldConfigInterfaceParamProbeMsgInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 2, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(7, 90))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200UdldConfigInterfaceParamProbeMsgInterval.setStatus('current')
me1200UdldStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3))
me1200UdldStatusInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1))
me1200UdldStatusInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1), )
if mibBuilder.loadTexts: me1200UdldStatusInterfaceTable.setStatus('current')
me1200UdldStatusInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1), ).setIndexNames((0, "ME1200-UDLD-MIB", "me1200UdldStatusInterfaceIfIndex"))
if mibBuilder.loadTexts: me1200UdldStatusInterfaceEntry.setStatus('current')
me1200UdldStatusInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 1), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200UdldStatusInterfaceIfIndex.setStatus('current')
me1200UdldStatusInterfaceDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceDeviceID.setStatus('current')
me1200UdldStatusInterfaceDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceDeviceName.setStatus('current')
me1200UdldStatusInterfaceLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 1, 1, 4), ME1200UdldDetectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceLinkState.setStatus('current')
me1200UdldStatusInterfaceNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2), )
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborTable.setStatus('current')
me1200UdldStatusInterfaceNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1), ).setIndexNames((0, "ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborIfIndex"))
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborEntry.setStatus('current')
me1200UdldStatusInterfaceNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 1), ME1200InterfaceIndex())
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborIfIndex.setStatus('current')
me1200UdldStatusInterfaceNeighborNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 2), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborNeighborDeviceID.setStatus('current')
me1200UdldStatusInterfaceNeighborNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 3), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborNeighborPortID.setStatus('current')
me1200UdldStatusInterfaceNeighborNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 4), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborNeighborDeviceName.setStatus('current')
me1200UdldStatusInterfaceNeighborLinkDetectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 1, 3, 1, 2, 1, 5), ME1200UdldDetectionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: me1200UdldStatusInterfaceNeighborLinkDetectionState.setStatus('current')
me1200UdldMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2))
me1200UdldMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 1))
me1200UdldMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2))
me1200UdldConfigInterfaceParamTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 1)).setObjects(("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamUdldMode"), ("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamProbeMsgInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UdldConfigInterfaceParamTableInfoGroup = me1200UdldConfigInterfaceParamTableInfoGroup.setStatus('current')
me1200UdldStatusInterfaceTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 2)).setObjects(("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceDeviceID"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceDeviceName"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceLinkState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UdldStatusInterfaceTableInfoGroup = me1200UdldStatusInterfaceTableInfoGroup.setStatus('current')
me1200UdldStatusInterfaceNeighborTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 2, 3)).setObjects(("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborDeviceID"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborPortID"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborNeighborDeviceName"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborLinkDetectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UdldStatusInterfaceNeighborTableInfoGroup = me1200UdldStatusInterfaceNeighborTableInfoGroup.setStatus('current')
me1200UdldMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 123, 2, 1, 1)).setObjects(("ME1200-UDLD-MIB", "me1200UdldConfigInterfaceParamTableInfoGroup"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceTableInfoGroup"), ("ME1200-UDLD-MIB", "me1200UdldStatusInterfaceNeighborTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UdldMibCompliance = me1200UdldMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-UDLD-MIB", me1200UdldConfigInterfaceParamIfIndex=me1200UdldConfigInterfaceParamIfIndex, me1200UdldConfigInterfaceParamTable=me1200UdldConfigInterfaceParamTable, me1200UdldConfig=me1200UdldConfig, me1200UdldConfigInterfaceParamEntry=me1200UdldConfigInterfaceParamEntry, me1200UdldStatusInterfaceLinkState=me1200UdldStatusInterfaceLinkState, me1200UdldMibObjects=me1200UdldMibObjects, me1200UdldStatusInterfaceNeighborNeighborDeviceName=me1200UdldStatusInterfaceNeighborNeighborDeviceName, me1200UdldStatusInterfaceIfIndex=me1200UdldStatusInterfaceIfIndex, me1200UdldStatusInterfaceNeighborNeighborDeviceID=me1200UdldStatusInterfaceNeighborNeighborDeviceID, me1200UdldStatusInterface=me1200UdldStatusInterface, me1200UdldStatusInterfaceDeviceName=me1200UdldStatusInterfaceDeviceName, me1200UdldMibCompliances=me1200UdldMibCompliances, me1200UdldStatusInterfaceNeighborIfIndex=me1200UdldStatusInterfaceNeighborIfIndex, me1200UdldStatusInterfaceNeighborTable=me1200UdldStatusInterfaceNeighborTable, PYSNMP_MODULE_ID=me1200UdldMib, me1200UdldStatusInterfaceNeighborEntry=me1200UdldStatusInterfaceNeighborEntry, me1200UdldStatusInterfaceNeighborLinkDetectionState=me1200UdldStatusInterfaceNeighborLinkDetectionState, me1200UdldMib=me1200UdldMib, me1200UdldStatusInterfaceNeighborNeighborPortID=me1200UdldStatusInterfaceNeighborNeighborPortID, me1200UdldStatus=me1200UdldStatus, me1200UdldStatusInterfaceNeighborTableInfoGroup=me1200UdldStatusInterfaceNeighborTableInfoGroup, ME1200UdldMode=ME1200UdldMode, me1200UdldConfigInterfaceParamUdldMode=me1200UdldConfigInterfaceParamUdldMode, me1200UdldMibGroups=me1200UdldMibGroups, me1200UdldMibConformance=me1200UdldMibConformance, me1200UdldMibCompliance=me1200UdldMibCompliance, me1200UdldConfigInterfaceParamProbeMsgInterval=me1200UdldConfigInterfaceParamProbeMsgInterval, me1200UdldStatusInterfaceEntry=me1200UdldStatusInterfaceEntry, me1200UdldStatusInterfaceTableInfoGroup=me1200UdldStatusInterfaceTableInfoGroup, me1200UdldStatusInterfaceTable=me1200UdldStatusInterfaceTable, me1200UdldStatusInterfaceDeviceID=me1200UdldStatusInterfaceDeviceID, ME1200UdldDetectionState=ME1200UdldDetectionState, me1200UdldConfigInterface=me1200UdldConfigInterface, me1200UdldConfigInterfaceParamTableInfoGroup=me1200UdldConfigInterfaceParamTableInfoGroup)
