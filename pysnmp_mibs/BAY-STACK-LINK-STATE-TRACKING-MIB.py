#
# PySNMP MIB module BAY-STACK-LINK-STATE-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-LINK-STATE-TRACKING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackLinkStateTrackingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 43))
bayStackLinkStateTrackingMib.setRevisions(('2018-09-28 00:00', '2017-08-31 00:00', '2013-10-11 00:00', '2013-02-13 00:00', '2012-11-15 00:00', '2012-10-17 00:00', '2012-09-03 00:00',))
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setLastUpdated('201809280000Z')
if mibBuilder.loadTexts: bayStackLinkStateTrackingMib.setOrganization('Avaya')
bsLstNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 0))
bsLstObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1))
bsLstScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 1))
bsLstNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3))
class PortList(TextualConvention, OctetString):
    status = 'current'

class IdList(TextualConvention, OctetString):
    status = 'current'

bsLstInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bsLstInterfaceStatus.setStatus('current')
bsLstGroupTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2), )
if mibBuilder.loadTexts: bsLstGroupTable.setStatus('current')
bsLstGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"))
if mibBuilder.loadTexts: bsLstGroupEntry.setStatus('current')
bsLstGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLstGroupIndex.setStatus('current')
bsLstGroupEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupEnabled.setStatus('current')
bsLstGroupUpstreamPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 3), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupUpstreamPortList.setStatus('current')
bsLstGroupDownstreamPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 4), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupDownstreamPortList.setStatus('current')
bsLstGroupUpstreamMltList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 5), IdList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupUpstreamMltList.setStatus('current')
bsLstGroupDownstreamMltList = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 6), IdList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsLstGroupDownstreamMltList.setStatus('current')
bsLstGroupOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 43, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("notConfigured", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsLstGroupOperState.setStatus('current')
bsLstInterfaceStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupIndex"))
if mibBuilder.loadTexts: bsLstInterfaceStatusChanged.setStatus('current')
bsLstGroupOperStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 45, 5, 43, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstInterfaceStatus"), ("BAY-STACK-LINK-STATE-TRACKING-MIB", "bsLstGroupOperState"))
if mibBuilder.loadTexts: bsLstGroupOperStateChanged.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-LINK-STATE-TRACKING-MIB", bsLstGroupUpstreamPortList=bsLstGroupUpstreamPortList, bsLstNotifications=bsLstNotifications, PYSNMP_MODULE_ID=bayStackLinkStateTrackingMib, bsLstGroupUpstreamMltList=bsLstGroupUpstreamMltList, bsLstGroupTable=bsLstGroupTable, bsLstInterfaceStatusChanged=bsLstInterfaceStatusChanged, bsLstGroupEntry=bsLstGroupEntry, bsLstGroupDownstreamMltList=bsLstGroupDownstreamMltList, bsLstGroupDownstreamPortList=bsLstGroupDownstreamPortList, IdList=IdList, bsLstGroupOperState=bsLstGroupOperState, bsLstNotifObjects=bsLstNotifObjects, bsLstObjects=bsLstObjects, bayStackLinkStateTrackingMib=bayStackLinkStateTrackingMib, bsLstGroupIndex=bsLstGroupIndex, bsLstGroupEnabled=bsLstGroupEnabled, bsLstGroupOperStateChanged=bsLstGroupOperStateChanged, bsLstInterfaceStatus=bsLstInterfaceStatus, PortList=PortList, bsLstScalars=bsLstScalars)
