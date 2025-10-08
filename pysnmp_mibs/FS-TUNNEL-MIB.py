#
# PySNMP MIB module FS-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsTunnelMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114))
fsTunnelMib.setRevisions(('2012-06-20 00:00',))
if mibBuilder.loadTexts: fsTunnelMib.setLastUpdated('201206201634Z')
if mibBuilder.loadTexts: fsTunnelMib.setOrganization('FS.COM Inc..')
fsTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1))
fsTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: fsTunnelTable.setStatus('current')
fsTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "FS-TUNNEL-MIB", "fsTunnelIp"))
if mibBuilder.loadTexts: fsTunnelEntry.setStatus('current')
fsTunnelIp = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsTunnelIp.setStatus('current')
fsTunnelOutIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 114, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsTunnelOutIfindex.setStatus('current')
mibBuilder.exportSymbols("FS-TUNNEL-MIB", fsTunnelMib=fsTunnelMib, fsTunnelIp=fsTunnelIp, fsTunnelEntry=fsTunnelEntry, fsTunnelTable=fsTunnelTable, PYSNMP_MODULE_ID=fsTunnelMib, fsTunnelOutIfindex=fsTunnelOutIfindex, fsTunnelObjects=fsTunnelObjects)
