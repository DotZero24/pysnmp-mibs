#
# PySNMP MIB module QTECH-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("QTECH-DHCP-CLIENT-MIB", qtechDhcpClientMIBGroups=qtechDhcpClientMIBGroups, qtechDhcpClientIntfTable=qtechDhcpClientIntfTable, PYSNMP_MODULE_ID=qtechDhcpClientMIB, qtechDhcpClientMIB=qtechDhcpClientMIB, qtechDhcpClientMIBObjects=qtechDhcpClientMIBObjects, qtechDhcpIntfClientIndex=qtechDhcpIntfClientIndex, qtechDhcpClientMIBCompliances=qtechDhcpClientMIBCompliances, qtechDhcpClientIntfConfigGroup=qtechDhcpClientIntfConfigGroup, qtechDhcpClientIpAddrDhcpStatus=qtechDhcpClientIpAddrDhcpStatus, qtechDhcpClientIntfEntry=qtechDhcpClientIntfEntry, qtechDhcpClientMIBCompliance=qtechDhcpClientMIBCompliance, qtechDhcpClientMIBConformance=qtechDhcpClientMIBConformance, qtechDhcpClientConfig=qtechDhcpClientConfig)
