#
# PySNMP MIB module DGS-3700-12-L3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DGS-3700-12-L3MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:37 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, PhysAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "PhysAddress", "TruthValue", "TimeStamp", "DisplayString")
dgs3712, = mibBuilder.importSymbols("SW3700PRIMGMT-MIB", "dgs3712")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('200811190000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization(' ')
class NodeAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1))
class Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class VrId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1), ).setIndexNames((0, "DGS-3700-12-L3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
swL3IpCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setStatus('current')
swL3IpCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setStatus('current')
swL3IpCtrlIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setStatus('current')
swL3IpCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setStatus('current')
swL3IpCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlMode.setStatus('current')
swL3IpCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setStatus('current')
swL3IpCtrlIpv6LinkLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 14), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setStatus('current')
swL3IpCtrlIpv6LinkLocalPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus('current')
swL3IpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpCtrlState.setStatus('current')
swL3IpCtrlIpv6LinkLocalAutoState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setStatus('current')
swL3Ipv6CtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 4), )
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setStatus('current')
swL3Ipv6CtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 4, 1), ).setIndexNames((0, "DGS-3700-12-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"))
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setStatus('current')
swL3Ipv6CtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setStatus('current')
swL3Ipv6CtrlNsRetransTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setStatus('current')
swL3Ipv6AddressCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5), )
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setStatus('current')
swL3Ipv6AddressCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5, 1), ).setIndexNames((0, "DGS-3700-12-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"), (0, "DGS-3700-12-L3MGMT-MIB", "swL3Ipv6Address"), (0, "DGS-3700-12-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"))
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setStatus('current')
swL3Ipv6AddressCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setStatus('current')
swL3Ipv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6Address.setStatus('current')
swL3Ipv6AddressCtrlPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setStatus('current')
swL3Ipv6AddressCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setStatus('current')
swL3IpCtrlAllIpIfState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 102, 1, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setStatus('current')
mibBuilder.exportSymbols("DGS-3700-12-L3MGMT-MIB", swL3Ipv6CtrlInterfaceName=swL3Ipv6CtrlInterfaceName, swL3MgmtMIB=swL3MgmtMIB, swL3IpCtrlVlanName=swL3IpCtrlVlanName, swL3IpCtrlIpAddr=swL3IpCtrlIpAddr, swL3IpMgmt=swL3IpMgmt, swL3Ipv6CtrlTable=swL3Ipv6CtrlTable, swL3IpCtrlAllIpIfState=swL3IpCtrlAllIpIfState, NodeAddress=NodeAddress, swL3IpCtrlIpv6LinkLocalAutoState=swL3IpCtrlIpv6LinkLocalAutoState, swL3Ipv6AddressCtrlTable=swL3Ipv6AddressCtrlTable, swL3IpCtrlTable=swL3IpCtrlTable, swL3IpCtrlState=swL3IpCtrlState, VrId=VrId, swL3IpCtrlMode=swL3IpCtrlMode, swL3IpCtrlIfIndex=swL3IpCtrlIfIndex, swL3Ipv6CtrlEntry=swL3Ipv6CtrlEntry, swL3IpCtrlIpv6LinkLocalAddress=swL3IpCtrlIpv6LinkLocalAddress, swL3Ipv6AddressCtrlPrefixLen=swL3Ipv6AddressCtrlPrefixLen, swL3IpCtrlAdminState=swL3IpCtrlAdminState, swL3IpCtrlIpSubnetMask=swL3IpCtrlIpSubnetMask, swL3Ipv6CtrlNsRetransTimer=swL3Ipv6CtrlNsRetransTimer, swL3IpCtrlEntry=swL3IpCtrlEntry, swL3Ipv6Address=swL3Ipv6Address, PYSNMP_MODULE_ID=swL3MgmtMIB, Ipv6Address=Ipv6Address, swL3Ipv6AddressCtrlEntry=swL3Ipv6AddressCtrlEntry, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3IpCtrlIpv6LinkLocalPrefixLen=swL3IpCtrlIpv6LinkLocalPrefixLen, NetAddress=NetAddress, swL3IpCtrlMgmt=swL3IpCtrlMgmt, swL3Ipv6AddressCtrlInterfaceName=swL3Ipv6AddressCtrlInterfaceName, swL3Ipv6AddressCtrlState=swL3Ipv6AddressCtrlState)
