#
# PySNMP MIB module SUBNETVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SUBNETVLAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("SUBNETVLAN-MIB", swSubnetVLANIPv6Address=swSubnetVLANIPv6Address, PYSNMP_MODULE_ID=swSubnetVlanMIB, swVlanPrecedenceClassification=swVlanPrecedenceClassification, swSubnetVLANID=swSubnetVLANID, swSubnetVLANIPv6RowStatus=swSubnetVLANIPv6RowStatus, swSubnetVLANIPv6PrefixLength=swSubnetVLANIPv6PrefixLength, swSubnetVLANPriority=swSubnetVLANPriority, swVlanPrecedenceTable=swVlanPrecedenceTable, swSubnetVLANRowStatus=swSubnetVLANRowStatus, swSubnetVlanMgmt=swSubnetVlanMgmt, swSubnetVLANIPAddress=swSubnetVLANIPAddress, swSubnetVLANEntry=swSubnetVLANEntry, swVlanPrecedenceEntry=swVlanPrecedenceEntry, Ipv6Address=Ipv6Address, swSubnetVLANIPMask=swSubnetVLANIPMask, swSubnetVLANIPv6VID=swSubnetVLANIPv6VID, swSubnetVlanMIB=swSubnetVlanMIB, swSubnetVlanCtrl=swSubnetVlanCtrl, swVlanPrecedencePortIndex=swVlanPrecedencePortIndex, swSubnetVLANTable=swSubnetVLANTable, swSubnetVlanInfo=swSubnetVlanInfo, swSubnetVLANIPv6Table=swSubnetVLANIPv6Table, VlanId=VlanId, swSubnetVLANIPv6Entry=swSubnetVLANIPv6Entry, swSubnetVLANIPv6Priority=swSubnetVLANIPv6Priority)
