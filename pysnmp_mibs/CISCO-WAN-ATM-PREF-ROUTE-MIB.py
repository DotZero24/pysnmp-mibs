#
# PySNMP MIB module CISCO-WAN-ATM-PREF-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-WAN-ATM-PREF-ROUTE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PnniNodeId, PnniPortId = mibBuilder.importSymbols("PNNI-MIB", "PnniNodeId", "PnniPortId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoWanATMPrefRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 99996))
ciscoWanATMPrefRouteMIB.setRevisions(('2002-06-25 00:00',))
if mibBuilder.loadTexts: ciscoWanATMPrefRouteMIB.setLastUpdated('200206250000Z')
if mibBuilder.loadTexts: ciscoWanATMPrefRouteMIB.setOrganization('Cisco System Inc.')
ciscoWanATMPrefRouteMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 0))
ciscoWanATMPrefRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1))
cwaPrefRouteConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2))
class RouteId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cwaPrefRouteConfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1), )
if mibBuilder.loadTexts: cwaPrefRouteConfTable.setStatus('current')
cwaPrefRouteConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"))
if mibBuilder.loadTexts: cwaPrefRouteConfEntry.setStatus('current')
cwaPrefRouteId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1), RouteId())
if mibBuilder.loadTexts: cwaPrefRouteId.setStatus('current')
cwaPrefRouteNwElemCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemCount.setStatus('current')
cwaPrefRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteRowStatus.setStatus('current')
cwaPrefRouteNwElemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2), )
if mibBuilder.loadTexts: cwaPrefRouteNwElemTable.setStatus('current')
cwaPrefRouteNwElemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1), ).setIndexNames((0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"), (0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPos"))
if mibBuilder.loadTexts: cwaPrefRouteNwElemEntry.setStatus('current')
cwaPrefRouteNwElemPos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: cwaPrefRouteNwElemPos.setStatus('current')
cwaPrefRouteNwElemNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 2), PnniNodeId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemNodeId.setStatus('current')
cwaPrefRouteNwElemPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 3), PnniPortId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemPortId.setStatus('current')
cwaPrefRouteNwElemRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cwaPrefRouteNwElemRowStatus.setStatus('current')
cwaPrefRouteCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1))
cwaPrefMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2))
cwaPrefMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1, 1)).setObjects(("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaPrefMIBCompliance = cwaPrefMIBCompliance.setStatus('current')
cwaPrefRouteMIBGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2, 1)).setObjects(("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemCount"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteRowStatus"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemNodeId"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPortId"), ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaPrefRouteMIBGroups = cwaPrefRouteMIBGroups.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-PREF-ROUTE-MIB", RouteId=RouteId, cwaPrefRouteNwElemTable=cwaPrefRouteNwElemTable, cwaPrefRouteCompliances=cwaPrefRouteCompliances, PYSNMP_MODULE_ID=ciscoWanATMPrefRouteMIB, cwaPrefRouteRowStatus=cwaPrefRouteRowStatus, cwaPrefRouteNwElemPortId=cwaPrefRouteNwElemPortId, cwaPrefMIBCompliance=cwaPrefMIBCompliance, ciscoWanATMPrefRouteMIB=ciscoWanATMPrefRouteMIB, cwaPrefRouteConfTable=cwaPrefRouteConfTable, cwaPrefMIBGroups=cwaPrefMIBGroups, cwaPrefRouteNwElemNodeId=cwaPrefRouteNwElemNodeId, ciscoWanATMPrefRouteMIBNotifs=ciscoWanATMPrefRouteMIBNotifs, cwaPrefRouteNwElemRowStatus=cwaPrefRouteNwElemRowStatus, cwaPrefRouteConformance=cwaPrefRouteConformance, cwaPrefRouteNwElemEntry=cwaPrefRouteNwElemEntry, cwaPrefRouteId=cwaPrefRouteId, ciscoWanATMPrefRouteMIBObjects=ciscoWanATMPrefRouteMIBObjects, cwaPrefRouteNwElemCount=cwaPrefRouteNwElemCount, cwaPrefRouteMIBGroups=cwaPrefRouteMIBGroups, cwaPrefRouteNwElemPos=cwaPrefRouteNwElemPos, cwaPrefRouteConfEntry=cwaPrefRouteConfEntry)
