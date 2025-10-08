#
# PySNMP MIB module SUPERMICRO-MIARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-MIARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsMIStdIpContextId, = mibBuilder.importSymbols("SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId")
fsMiArp = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33))
fsMiArp.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsMiArp.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsMiArp.setOrganization('Super Micro Computer Inc.')
fsMIArpTable = MibTable((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1), )
if mibBuilder.loadTexts: fsMIArpTable.setStatus('current')
fsMIArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1), ).setIndexNames((0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"))
if mibBuilder.loadTexts: fsMIArpEntry.setStatus('current')
fsMIArpCacheTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400)).clone(7200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMIArpCacheTimeout.setStatus('current')
fsMIArpCachePendTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 3000)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMIArpCachePendTime.setStatus('current')
fsMIArpMaxRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMIArpMaxRetries.setStatus('current')
fsMIArpPendingEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsMIArpPendingEntryCount.setStatus('current')
fsMIArpCacheEntryCount = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 33, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsMIArpCacheEntryCount.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-MIARP-MIB", PYSNMP_MODULE_ID=fsMiArp, fsMiArp=fsMiArp, fsMIArpCacheTimeout=fsMIArpCacheTimeout, fsMIArpCachePendTime=fsMIArpCachePendTime, fsMIArpCacheEntryCount=fsMIArpCacheEntryCount, fsMIArpMaxRetries=fsMIArpMaxRetries, fsMIArpTable=fsMIArpTable, fsMIArpEntry=fsMIArpEntry, fsMIArpPendingEntryCount=fsMIArpPendingEntryCount)
