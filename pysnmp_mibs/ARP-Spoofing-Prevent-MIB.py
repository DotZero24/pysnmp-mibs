#
# PySNMP MIB module ARP-Spoofing-Prevent-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/ARP-Spoofing-Prevent-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
swARPSpoofingPreventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 62))
if mibBuilder.loadTexts: swARPSpoofingPreventMIB.setLastUpdated('0805120000Z')
if mibBuilder.loadTexts: swARPSpoofingPreventMIB.setOrganization('D-Link Corp.')
class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swARPSpoofingPreventCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 1))
swARPSpoofingPreventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 2))
swARPSpoofingPreventMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 62, 3))
swARPSpoofingPreventMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1), )
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtTable.setStatus('current')
swARPSpoofingPreventMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1), ).setIndexNames((0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayIP"), (0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayMAC"))
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtEntry.setStatus('current')
swARPSpoofingPreventMgmtGatewayIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtGatewayIP.setStatus('current')
swARPSpoofingPreventMgmtGatewayMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtGatewayMAC.setStatus('current')
swARPSpoofingPreventMgmtPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 3), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtPorts.setStatus('current')
swARPSpoofingPreventMgmtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swARPSpoofingPreventMgmtStatus.setStatus('current')
mibBuilder.exportSymbols("ARP-Spoofing-Prevent-MIB", swARPSpoofingPreventCtrl=swARPSpoofingPreventCtrl, swARPSpoofingPreventInfo=swARPSpoofingPreventInfo, swARPSpoofingPreventMgmtPorts=swARPSpoofingPreventMgmtPorts, swARPSpoofingPreventMIB=swARPSpoofingPreventMIB, swARPSpoofingPreventMgmt=swARPSpoofingPreventMgmt, PortList=PortList, swARPSpoofingPreventMgmtEntry=swARPSpoofingPreventMgmtEntry, PYSNMP_MODULE_ID=swARPSpoofingPreventMIB, swARPSpoofingPreventMgmtGatewayIP=swARPSpoofingPreventMgmtGatewayIP, swARPSpoofingPreventMgmtStatus=swARPSpoofingPreventMgmtStatus, swARPSpoofingPreventMgmtGatewayMAC=swARPSpoofingPreventMgmtGatewayMAC, swARPSpoofingPreventMgmtTable=swARPSpoofingPreventMgmtTable)
