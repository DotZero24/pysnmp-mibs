#
# PySNMP MIB module FS-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
fsDhcpClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135))
fsDhcpClientMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: fsDhcpClientMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: fsDhcpClientMIB.setOrganization('FS.COM Inc..')
fsDhcpClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0))
fsDhcpClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1))
fsDhcpClientIntfTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2), )
if mibBuilder.loadTexts: fsDhcpClientIntfTable.setStatus('current')
fsDhcpClientIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1), ).setIndexNames((0, "FS-DHCP-CLIENT-MIB", "fsDhcpIntfClientIndex"))
if mibBuilder.loadTexts: fsDhcpClientIntfEntry.setStatus('current')
fsDhcpIntfClientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsDhcpIntfClientIndex.setStatus('current')
fsDhcpClientIpAddrDhcpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsDhcpClientIpAddrDhcpStatus.setStatus('current')
fsDhcpClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2))
fsDhcpClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 1))
fsDhcpClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 2))
fsDhcpClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 1, 1)).setObjects(("FS-DHCP-CLIENT-MIB", "fsDhcpClientIntfConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsDhcpClientMIBCompliance = fsDhcpClientMIBCompliance.setStatus('current')
fsDhcpClientIntfConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 2, 1)).setObjects(("FS-DHCP-CLIENT-MIB", "fsDhcpClientIpAddrDhcpStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsDhcpClientIntfConfigGroup = fsDhcpClientIntfConfigGroup.setStatus('current')
mibBuilder.exportSymbols("FS-DHCP-CLIENT-MIB", fsDhcpClientMIB=fsDhcpClientMIB, PYSNMP_MODULE_ID=fsDhcpClientMIB, fsDhcpClientConfig=fsDhcpClientConfig, fsDhcpIntfClientIndex=fsDhcpIntfClientIndex, fsDhcpClientIntfTable=fsDhcpClientIntfTable, fsDhcpClientIpAddrDhcpStatus=fsDhcpClientIpAddrDhcpStatus, fsDhcpClientMIBObjects=fsDhcpClientMIBObjects, fsDhcpClientMIBGroups=fsDhcpClientMIBGroups, fsDhcpClientMIBCompliance=fsDhcpClientMIBCompliance, fsDhcpClientMIBConformance=fsDhcpClientMIBConformance, fsDhcpClientMIBCompliances=fsDhcpClientMIBCompliances, fsDhcpClientIntfEntry=fsDhcpClientIntfEntry, fsDhcpClientIntfConfigGroup=fsDhcpClientIntfConfigGroup)
