#
# PySNMP MIB module FUTURESOFT-OSPF-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aricent/FUTURESOFT-OSPF-TEST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
futOspfTestGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 2076, 10, 100))
futOspfTestGroup.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: futOspfTestGroup.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: futOspfTestGroup.setOrganization('Future Software Private Limited')
futOspfGrTestGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2076, 10, 100, 100))
class BigMetric(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16777215)

class InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TOSType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 30)

futOspfBRRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1), )
if mibBuilder.loadTexts: futOspfBRRouteTable.setStatus('current')
futOspfBRRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1), ).setIndexNames((0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfBRRouteIpAddr"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfBRRouteIpAddrMask"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfBRRouteIpTos"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfBRRouteIpNextHop"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfBRRouteDestType"))
if mibBuilder.loadTexts: futOspfBRRouteEntry.setStatus('current')
futOspfBRRouteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: futOspfBRRouteIpAddr.setStatus('current')
futOspfBRRouteIpAddrMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: futOspfBRRouteIpAddrMask.setStatus('current')
futOspfBRRouteIpTos = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: futOspfBRRouteIpTos.setStatus('current')
futOspfBRRouteIpNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 4), IpAddress())
if mibBuilder.loadTexts: futOspfBRRouteIpNextHop.setStatus('current')
futOspfBRRouteDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("areaBorder", 2), ("asBoundary", 3))))
if mibBuilder.loadTexts: futOspfBRRouteDestType.setStatus('current')
futOspfBRRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("intraArea", 1), ("interArea", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: futOspfBRRouteType.setStatus('current')
futOspfBRRouteAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: futOspfBRRouteAreaId.setStatus('current')
futOspfBRRouteCost = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 8), BigMetric()).setMaxAccess("readonly")
if mibBuilder.loadTexts: futOspfBRRouteCost.setStatus('current')
futOspfBRRouteInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 1, 1, 9), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: futOspfBRRouteInterfaceIndex.setStatus('current')
futOspfExtRouteTable = MibTable((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2), )
if mibBuilder.loadTexts: futOspfExtRouteTable.setStatus('current')
futOspfExtRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1), ).setIndexNames((0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfExtRouteDest"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfExtRouteMask"), (0, "FUTURESOFT-OSPF-TEST-MIB", "futOspfExtRouteTOS"))
if mibBuilder.loadTexts: futOspfExtRouteEntry.setStatus('current')
futOspfExtRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: futOspfExtRouteDest.setStatus('current')
futOspfExtRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: futOspfExtRouteMask.setStatus('current')
futOspfExtRouteTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 3), TOSType())
if mibBuilder.loadTexts: futOspfExtRouteTOS.setStatus('current')
futOspfExtRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 4), BigMetric()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteMetric.setStatus('current')
futOspfExtRouteMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("asexttype1", 1), ("asexttype2", 2))).clone('asexttype2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteMetricType.setStatus('current')
futOspfExtRouteTag = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteTag.setStatus('current')
futOspfExtRouteFwdAdr = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 7), IpAddress().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteFwdAdr.setStatus('current')
futOspfExtRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 8), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteIfIndex.setStatus('current')
futOspfExtRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 9), IpAddress().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteNextHop.setStatus('current')
futOspfExtRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2076, 10, 100, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: futOspfExtRouteStatus.setStatus('current')
futOspfGrShutdown = MibScalar((1, 3, 6, 1, 4, 1, 2076, 10, 100, 100, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("unplanned", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: futOspfGrShutdown.setStatus('current')
mibBuilder.exportSymbols("FUTURESOFT-OSPF-TEST-MIB", futOspfExtRouteIfIndex=futOspfExtRouteIfIndex, futOspfBRRouteAreaId=futOspfBRRouteAreaId, PYSNMP_MODULE_ID=futOspfTestGroup, futOspfBRRouteIpNextHop=futOspfBRRouteIpNextHop, TOSType=TOSType, futOspfExtRouteMetricType=futOspfExtRouteMetricType, futOspfBRRouteIpTos=futOspfBRRouteIpTos, futOspfBRRouteIpAddr=futOspfBRRouteIpAddr, futOspfBRRouteCost=futOspfBRRouteCost, futOspfExtRouteEntry=futOspfExtRouteEntry, InterfaceIndex=InterfaceIndex, futOspfExtRouteStatus=futOspfExtRouteStatus, futOspfTestGroup=futOspfTestGroup, futOspfBRRouteInterfaceIndex=futOspfBRRouteInterfaceIndex, futOspfGrTestGroup=futOspfGrTestGroup, futOspfBRRouteIpAddrMask=futOspfBRRouteIpAddrMask, futOspfExtRouteNextHop=futOspfExtRouteNextHop, futOspfGrShutdown=futOspfGrShutdown, futOspfExtRouteFwdAdr=futOspfExtRouteFwdAdr, futOspfExtRouteDest=futOspfExtRouteDest, futOspfBRRouteTable=futOspfBRRouteTable, futOspfExtRouteMask=futOspfExtRouteMask, futOspfBRRouteEntry=futOspfBRRouteEntry, futOspfExtRouteTable=futOspfExtRouteTable, futOspfExtRouteTag=futOspfExtRouteTag, BigMetric=BigMetric, futOspfBRRouteDestType=futOspfBRRouteDestType, futOspfBRRouteType=futOspfBRRouteType, futOspfExtRouteTOS=futOspfExtRouteTOS, futOspfExtRouteMetric=futOspfExtRouteMetric)
