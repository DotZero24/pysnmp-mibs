#
# PySNMP MIB module FS-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("FS-TUNNEL-MIB", fsTunnelObjects=fsTunnelObjects, fsTunnelTable=fsTunnelTable, fsTunnelEntry=fsTunnelEntry, fsTunnelIp=fsTunnelIp, fsTunnelOutIfindex=fsTunnelOutIfindex, fsTunnelMib=fsTunnelMib, PYSNMP_MODULE_ID=fsTunnelMib)
