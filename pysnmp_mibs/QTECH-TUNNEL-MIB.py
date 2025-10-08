#
# PySNMP MIB module QTECH-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-TUNNEL-MIB", qtechTunnelOutIfindex=qtechTunnelOutIfindex, qtechTunnelTable=qtechTunnelTable, qtechTunnelIp=qtechTunnelIp, qtechTunnelEntry=qtechTunnelEntry, qtechTunnelObjects=qtechTunnelObjects, PYSNMP_MODULE_ID=qtechTunnelMib, qtechTunnelMib=qtechTunnelMib)
