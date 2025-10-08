#
# PySNMP MIB module SUPERMICRO-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-ARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SUPERMICRO-ARP-MIB", arp=arp, fsArpCacheTimeout=fsArpCacheTimeout, fsArpRedEntryTime=fsArpRedEntryTime, fsarp=fsarp, arptest=arptest, fsArpMaxRetries=fsArpMaxRetries, fsArpPendingEntryCount=fsArpPendingEntryCount, fsArpCacheEntryCount=fsArpCacheEntryCount, PYSNMP_MODULE_ID=fsarp, fsArpRedExitTime=fsArpRedExitTime, fsArpCachePendTime=fsArpCachePendTime)
