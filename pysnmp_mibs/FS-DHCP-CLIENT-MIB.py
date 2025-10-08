#
# PySNMP MIB module FS-DHCP-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-DHCP-CLIENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:00:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("FS-DHCP-CLIENT-MIB", fsDhcpClientConfig=fsDhcpClientConfig, fsDhcpClientMIBCompliance=fsDhcpClientMIBCompliance, fsDhcpClientMIBObjects=fsDhcpClientMIBObjects, fsDhcpClientIntfEntry=fsDhcpClientIntfEntry, PYSNMP_MODULE_ID=fsDhcpClientMIB, fsDhcpClientIpAddrDhcpStatus=fsDhcpClientIpAddrDhcpStatus, fsDhcpClientMIBGroups=fsDhcpClientMIBGroups, fsDhcpClientIntfTable=fsDhcpClientIntfTable, fsDhcpClientMIB=fsDhcpClientMIB, fsDhcpClientIntfConfigGroup=fsDhcpClientIntfConfigGroup, fsDhcpIntfClientIndex=fsDhcpIntfClientIndex, fsDhcpClientMIBConformance=fsDhcpClientMIBConformance, fsDhcpClientMIBCompliances=fsDhcpClientMIBCompliances)
