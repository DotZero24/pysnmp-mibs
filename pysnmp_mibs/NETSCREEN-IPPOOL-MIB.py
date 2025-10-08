#
# PySNMP MIB module NETSCREEN-IPPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-IPPOOL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenVpnMibModule, netscreenVpn = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpnMibModule", "netscreenVpn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NETSCREEN-IPPOOL-MIB", netscreenIppoolMibModule=netscreenIppoolMibModule, nsVpnIpPool=nsVpnIpPool, nsVpnIpPoolEndIp=nsVpnIpPoolEndIp, nsVpnIpPoolName=nsVpnIpPoolName, nsVpnIpPoolIpUsed=nsVpnIpPoolIpUsed, nsVpnIpPoolStartIp=nsVpnIpPoolStartIp, nsVpnIpPoolIndex=nsVpnIpPoolIndex, PYSNMP_MODULE_ID=netscreenIppoolMibModule, nsVpnIpPoolEntry=nsVpnIpPoolEntry, nsVpnIpPoolTable=nsVpnIpPoolTable)
