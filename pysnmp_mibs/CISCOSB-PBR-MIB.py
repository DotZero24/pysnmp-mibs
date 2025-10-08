#
# PySNMP MIB module CISCOSB-PBR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSB-PBR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
rlRouteMapPbrRouteMapName, rlRouteMapPbrRouteMapSectionId = mibBuilder.importSymbols("CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName", "rlRouteMapPbrRouteMapSectionId")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressIPv6, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlPolicyBasedRouting = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228))
rlPolicyBasedRouting.setRevisions(('2015-06-08 00:00',))
if mibBuilder.loadTexts: rlPolicyBasedRouting.setLastUpdated('201506080000Z')
if mibBuilder.loadTexts: rlPolicyBasedRouting.setOrganization('Cisco Systems, Inc.')
class RlPBRInetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class RlPBRStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("noIp", 2), ("interfaceDown", 3))

rlPBRTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1), )
if mibBuilder.loadTexts: rlPBRTable.setStatus('current')
rlPBREntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-PBR-MIB", "rlPBRInetType"))
if mibBuilder.loadTexts: rlPBREntry.setStatus('current')
rlPBRIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlPBRIfIndex.setStatus('current')
rlPBRInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 2), RlPBRInetType())
if mibBuilder.loadTexts: rlPBRInetType.setStatus('current')
rlPBRRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRouteMapName.setStatus('current')
rlPBRStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 4), RlPBRStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRStatus.setStatus('current')
rlPBRRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPBRRowStatus.setStatus('current')
class RlPBRNexthopStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("notReachable", 2), ("notDirect", 3))

rlPBRInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2), )
if mibBuilder.loadTexts: rlPBRInfoTable.setStatus('current')
rlPBRInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1), ).setIndexNames((0, "CISCOSB-PBR-MIB", "rlPBRInetType"), (0, "CISCOSB-PBR-MIB", "rlPBRIfIndex"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "CISCOSB-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"))
if mibBuilder.loadTexts: rlPBRInfoEntry.setStatus('current')
rlPBRInfoAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoAccessListName.setStatus('current')
rlPBRInfoNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddressType.setStatus('current')
rlPBRInfoNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopInetAddress.setStatus('current')
rlPBRInfoNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopIfIndex.setStatus('current')
rlPBRInfoNexthopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 228, 2, 1, 5), RlPBRNexthopStatusType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPBRInfoNexthopStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-PBR-MIB", RlPBRInetType=RlPBRInetType, rlPBRInfoNexthopInetAddress=rlPBRInfoNexthopInetAddress, rlPBRInfoEntry=rlPBRInfoEntry, rlPBRInfoNexthopStatus=rlPBRInfoNexthopStatus, RlPBRStatusType=RlPBRStatusType, rlPBRInfoTable=rlPBRInfoTable, rlPBRInfoNexthopInetAddressType=rlPBRInfoNexthopInetAddressType, rlPBRRouteMapName=rlPBRRouteMapName, rlPBREntry=rlPBREntry, RlPBRNexthopStatusType=RlPBRNexthopStatusType, rlPBRInfoAccessListName=rlPBRInfoAccessListName, rlPBRStatus=rlPBRStatus, rlPBRInfoNexthopIfIndex=rlPBRInfoNexthopIfIndex, rlPBRRowStatus=rlPBRRowStatus, rlPolicyBasedRouting=rlPolicyBasedRouting, rlPBRIfIndex=rlPBRIfIndex, rlPBRInetType=rlPBRInetType, PYSNMP_MODULE_ID=rlPolicyBasedRouting, rlPBRTable=rlPBRTable)
