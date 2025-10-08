#
# PySNMP MIB module SUPERMICRO-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-ARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
fsarp = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109))
fsarp.setRevisions(('2012-09-04 00:00',))
if mibBuilder.loadTexts: fsarp.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: fsarp.setOrganization('Super Micro Computer Inc.')
arp = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 1))
arptest = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 2))
fsArpCacheTimeout = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsArpCacheTimeout.setStatus('current')
fsArpCachePendTime = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 3000)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsArpCachePendTime.setStatus('current')
fsArpMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsArpMaxRetries.setStatus('current')
fsArpPendingEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsArpPendingEntryCount.setStatus('current')
fsArpCacheEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsArpCacheEntryCount.setStatus('current')
fsArpRedEntryTime = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsArpRedEntryTime.setStatus('current')
fsArpRedExitTime = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 109, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsArpRedExitTime.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-ARP-MIB", PYSNMP_MODULE_ID=fsarp, fsArpPendingEntryCount=fsArpPendingEntryCount, fsarp=fsarp, arp=arp, fsArpCachePendTime=fsArpCachePendTime, fsArpMaxRetries=fsArpMaxRetries, fsArpRedEntryTime=fsArpRedEntryTime, fsArpRedExitTime=fsArpRedExitTime, arptest=arptest, fsArpCacheEntryCount=fsArpCacheEntryCount, fsArpCacheTimeout=fsArpCacheTimeout)
