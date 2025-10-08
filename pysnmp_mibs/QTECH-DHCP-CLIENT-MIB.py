#
# PySNMP MIB module QTECH-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
qtechDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135))
qtechDhcpClientMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: qtechDhcpClientMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: qtechDhcpClientMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechDhcpClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0))
qtechDhcpClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1))
qtechDhcpClientIntfTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2), )
if mibBuilder.loadTexts: qtechDhcpClientIntfTable.setStatus('current')
qtechDhcpClientIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1), ).setIndexNames((0, "QTECH-DHCP-CLIENT-MIB", "qtechDhcpIntfClientIndex"))
if mibBuilder.loadTexts: qtechDhcpClientIntfEntry.setStatus('current')
qtechDhcpIntfClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechDhcpIntfClientIndex.setStatus('current')
qtechDhcpClientIpAddrDhcpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: qtechDhcpClientIpAddrDhcpStatus.setStatus('current')
qtechDhcpClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2))
qtechDhcpClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 1))
qtechDhcpClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 2))
qtechDhcpClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 1, 1)).setObjects(("QTECH-DHCP-CLIENT-MIB", "qtechDhcpClientIntfConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechDhcpClientMIBCompliance = qtechDhcpClientMIBCompliance.setStatus('current')
qtechDhcpClientIntfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 2, 1)).setObjects(("QTECH-DHCP-CLIENT-MIB", "qtechDhcpClientIpAddrDhcpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechDhcpClientIntfConfigGroup = qtechDhcpClientIntfConfigGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-DHCP-CLIENT-MIB", qtechDhcpClientMIBGroups=qtechDhcpClientMIBGroups, qtechDhcpClientIpAddrDhcpStatus=qtechDhcpClientIpAddrDhcpStatus, qtechDhcpClientIntfConfigGroup=qtechDhcpClientIntfConfigGroup, qtechDhcpClientMIBCompliances=qtechDhcpClientMIBCompliances, qtechDhcpClientConfig=qtechDhcpClientConfig, qtechDhcpClientIntfEntry=qtechDhcpClientIntfEntry, qtechDhcpClientMIBCompliance=qtechDhcpClientMIBCompliance, PYSNMP_MODULE_ID=qtechDhcpClientMIB, qtechDhcpClientMIB=qtechDhcpClientMIB, qtechDhcpClientIntfTable=qtechDhcpClientIntfTable, qtechDhcpClientMIBObjects=qtechDhcpClientMIBObjects, qtechDhcpIntfClientIndex=qtechDhcpIntfClientIndex, qtechDhcpClientMIBConformance=qtechDhcpClientMIBConformance)
