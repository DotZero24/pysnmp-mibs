#
# PySNMP MIB module NETSCREEN-IPPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-IPPOOL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenVpnMibModule, netscreenVpn = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpnMibModule", "netscreenVpn")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenIppoolMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 9))
netscreenIppoolMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-08-27 00:00',))
if mibBuilder.loadTexts: netscreenIppoolMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenIppoolMibModule.setOrganization('Juniper Networks, Inc.')
nsVpnIpPool = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 9))
nsVpnIpPoolTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1), )
if mibBuilder.loadTexts: nsVpnIpPoolTable.setStatus('current')
nsVpnIpPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1), ).setIndexNames((0, "NETSCREEN-IPPOOL-MIB", "nsVpnIpPoolIndex"))
if mibBuilder.loadTexts: nsVpnIpPoolEntry.setStatus('current')
nsVpnIpPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIpPoolIndex.setStatus('current')
nsVpnIpPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIpPoolName.setStatus('current')
nsVpnIpPoolStartIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIpPoolStartIp.setStatus('current')
nsVpnIpPoolEndIp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIpPoolEndIp.setStatus('current')
nsVpnIpPoolIpUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 9, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnIpPoolIpUsed.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-IPPOOL-MIB", nsVpnIpPoolIpUsed=nsVpnIpPoolIpUsed, nsVpnIpPoolEndIp=nsVpnIpPoolEndIp, nsVpnIpPoolEntry=nsVpnIpPoolEntry, netscreenIppoolMibModule=netscreenIppoolMibModule, nsVpnIpPoolTable=nsVpnIpPoolTable, nsVpnIpPoolName=nsVpnIpPoolName, nsVpnIpPool=nsVpnIpPool, nsVpnIpPoolStartIp=nsVpnIpPoolStartIp, nsVpnIpPoolIndex=nsVpnIpPoolIndex, PYSNMP_MODULE_ID=netscreenIppoolMibModule)
