#
# PySNMP MIB module ARP-Spoofing-Prevent-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/ARP-Spoofing-Prevent-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ARP-Spoofing-Prevent-MIB", swARPSpoofingPreventInfo=swARPSpoofingPreventInfo, swARPSpoofingPreventMgmt=swARPSpoofingPreventMgmt, swARPSpoofingPreventMIB=swARPSpoofingPreventMIB, PYSNMP_MODULE_ID=swARPSpoofingPreventMIB, swARPSpoofingPreventMgmtGatewayMAC=swARPSpoofingPreventMgmtGatewayMAC, swARPSpoofingPreventMgmtEntry=swARPSpoofingPreventMgmtEntry, swARPSpoofingPreventCtrl=swARPSpoofingPreventCtrl, PortList=PortList, swARPSpoofingPreventMgmtTable=swARPSpoofingPreventMgmtTable, swARPSpoofingPreventMgmtGatewayIP=swARPSpoofingPreventMgmtGatewayIP, swARPSpoofingPreventMgmtStatus=swARPSpoofingPreventMgmtStatus, swARPSpoofingPreventMgmtPorts=swARPSpoofingPreventMgmtPorts)
