#
# PySNMP MIB module BAY-STACK-LINK-STATE-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-LINK-STATE-TRACKING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("BAY-STACK-LINK-STATE-TRACKING-MIB", bsLstGroupDownstreamMltList=bsLstGroupDownstreamMltList, bsLstGroupEntry=bsLstGroupEntry, bsLstNotifObjects=bsLstNotifObjects, bsLstGroupIndex=bsLstGroupIndex, PYSNMP_MODULE_ID=bayStackLinkStateTrackingMib, bsLstInterfaceStatus=bsLstInterfaceStatus, IdList=IdList, bsLstGroupOperState=bsLstGroupOperState, bsLstGroupOperStateChanged=bsLstGroupOperStateChanged, bsLstNotifications=bsLstNotifications, bsLstScalars=bsLstScalars, bsLstGroupEnabled=bsLstGroupEnabled, bsLstInterfaceStatusChanged=bsLstInterfaceStatusChanged, bsLstGroupDownstreamPortList=bsLstGroupDownstreamPortList, bsLstGroupTable=bsLstGroupTable, bayStackLinkStateTrackingMib=bayStackLinkStateTrackingMib, bsLstObjects=bsLstObjects, bsLstGroupUpstreamMltList=bsLstGroupUpstreamMltList, PortList=PortList, bsLstGroupUpstreamPortList=bsLstGroupUpstreamPortList)
