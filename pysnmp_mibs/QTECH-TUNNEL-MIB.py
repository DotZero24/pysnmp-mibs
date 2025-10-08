#
# PySNMP MIB module QTECH-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechTunnelMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114))
qtechTunnelMib.setRevisions(('2012-06-20 00:00',))
if mibBuilder.loadTexts: qtechTunnelMib.setLastUpdated('201206201634Z')
if mibBuilder.loadTexts: qtechTunnelMib.setOrganization('Qtech Networks Co.,Ltd.')
qtechTunnelObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1))
qtechTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1), )
if mibBuilder.loadTexts: qtechTunnelTable.setStatus('current')
qtechTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1), ).setIndexNames((0, "QTECH-TUNNEL-MIB", "qtechTunnelIp"))
if mibBuilder.loadTexts: qtechTunnelEntry.setStatus('current')
qtechTunnelIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechTunnelIp.setStatus('current')
qtechTunnelOutIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 114, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechTunnelOutIfindex.setStatus('current')
mibBuilder.exportSymbols("QTECH-TUNNEL-MIB", qtechTunnelMib=qtechTunnelMib, qtechTunnelEntry=qtechTunnelEntry, qtechTunnelOutIfindex=qtechTunnelOutIfindex, PYSNMP_MODULE_ID=qtechTunnelMib, qtechTunnelIp=qtechTunnelIp, qtechTunnelObjects=qtechTunnelObjects, qtechTunnelTable=qtechTunnelTable)
