#
# PySNMP MIB module SUBNETVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SUBNETVLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
swSubnetVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 75))
if mibBuilder.loadTexts: swSubnetVlanMIB.setLastUpdated('0812020000Z')
if mibBuilder.loadTexts: swSubnetVlanMIB.setOrganization('D-Link Corp.')
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

swSubnetVlanCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 1))
swSubnetVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 2))
swSubnetVlanMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 75, 3))
swVlanPrecedenceTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1), )
if mibBuilder.loadTexts: swVlanPrecedenceTable.setStatus('current')
swVlanPrecedenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swVlanPrecedencePortIndex"))
if mibBuilder.loadTexts: swVlanPrecedenceEntry.setStatus('current')
swVlanPrecedencePortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVlanPrecedencePortIndex.setStatus('current')
swVlanPrecedenceClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("macBased", 1), ("subnetBased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swVlanPrecedenceClassification.setStatus('current')
swSubnetVLANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2), )
if mibBuilder.loadTexts: swSubnetVLANTable.setStatus('current')
swSubnetVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swSubnetVLANIPAddress"), (0, "SUBNETVLAN-MIB", "swSubnetVLANIPMask"))
if mibBuilder.loadTexts: swSubnetVLANEntry.setStatus('current')
swSubnetVLANIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPAddress.setStatus('current')
swSubnetVLANIPMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPMask.setStatus('current')
swSubnetVLANID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANID.setStatus('current')
swSubnetVLANPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANPriority.setStatus('current')
swSubnetVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANRowStatus.setStatus('current')
swSubnetVLANIPv6Table = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3), )
if mibBuilder.loadTexts: swSubnetVLANIPv6Table.setStatus('current')
swSubnetVLANIPv6Entry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1), ).setIndexNames((0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6Address"), (0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6PrefixLength"))
if mibBuilder.loadTexts: swSubnetVLANIPv6Entry.setStatus('current')
swSubnetVLANIPv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 1), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPv6Address.setStatus('current')
swSubnetVLANIPv6PrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSubnetVLANIPv6PrefixLength.setStatus('current')
swSubnetVLANIPv6VID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 3), VlanId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6VID.setStatus('current')
swSubnetVLANIPv6Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6Priority.setStatus('current')
swSubnetVLANIPv6RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSubnetVLANIPv6RowStatus.setStatus('current')
mibBuilder.exportSymbols("SUBNETVLAN-MIB", swSubnetVLANIPv6VID=swSubnetVLANIPv6VID, swSubnetVLANIPv6RowStatus=swSubnetVLANIPv6RowStatus, swSubnetVlanInfo=swSubnetVlanInfo, swSubnetVLANIPMask=swSubnetVLANIPMask, swSubnetVLANIPv6Address=swSubnetVLANIPv6Address, swSubnetVLANRowStatus=swSubnetVLANRowStatus, VlanId=VlanId, swVlanPrecedenceEntry=swVlanPrecedenceEntry, swSubnetVLANTable=swSubnetVLANTable, swSubnetVLANEntry=swSubnetVLANEntry, swVlanPrecedenceClassification=swVlanPrecedenceClassification, swSubnetVLANID=swSubnetVLANID, swSubnetVLANIPv6Table=swSubnetVLANIPv6Table, Ipv6Address=Ipv6Address, swVlanPrecedencePortIndex=swVlanPrecedencePortIndex, swSubnetVlanMgmt=swSubnetVlanMgmt, swSubnetVlanMIB=swSubnetVlanMIB, swVlanPrecedenceTable=swVlanPrecedenceTable, swSubnetVlanCtrl=swSubnetVlanCtrl, swSubnetVLANIPAddress=swSubnetVLANIPAddress, swSubnetVLANPriority=swSubnetVLANPriority, swSubnetVLANIPv6PrefixLength=swSubnetVLANIPv6PrefixLength, swSubnetVLANIPv6Priority=swSubnetVLANIPv6Priority, swSubnetVLANIPv6Entry=swSubnetVLANIPv6Entry, PYSNMP_MODULE_ID=swSubnetVlanMIB)
