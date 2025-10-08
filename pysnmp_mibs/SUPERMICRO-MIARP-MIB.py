#
# PySNMP MIB module SUPERMICRO-MIARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-MIARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SUPERMICRO-MIARP-MIB", fsMIArpCachePendTime=fsMIArpCachePendTime, PYSNMP_MODULE_ID=fsMiArp, fsMIArpPendingEntryCount=fsMIArpPendingEntryCount, fsMIArpCacheEntryCount=fsMIArpCacheEntryCount, fsMIArpCacheTimeout=fsMIArpCacheTimeout, fsMIArpEntry=fsMIArpEntry, fsMIArpTable=fsMIArpTable, fsMiArp=fsMiArp, fsMIArpMaxRetries=fsMIArpMaxRetries)
