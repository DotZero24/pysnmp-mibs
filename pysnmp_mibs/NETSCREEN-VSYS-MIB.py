#
# PySNMP MIB module NETSCREEN-VSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VSYS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenVsys, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVsys")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenVsysMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 15, 0))
netscreenVsysMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-05-08 00:00',))
if mibBuilder.loadTexts: netscreenVsysMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVsysMibModule.setOrganization('Juniper Networks, Inc.')
nsVsysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 15, 1))
nsVsysCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1), )
if mibBuilder.loadTexts: nsVsysCfgTable.setStatus('current')
nsVsysCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1), ).setIndexNames((0, "NETSCREEN-VSYS-MIB", "nsVsysCfgId"))
if mibBuilder.loadTexts: nsVsysCfgEntry.setStatus('current')
nsVsysCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgId.setStatus('current')
nsVsysCfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgName.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-VSYS-MIB", nsVsysCfgTable=nsVsysCfgTable, nsVsysCfg=nsVsysCfg, nsVsysCfgId=nsVsysCfgId, netscreenVsysMibModule=netscreenVsysMibModule, nsVsysCfgEntry=nsVsysCfgEntry, PYSNMP_MODULE_ID=netscreenVsysMibModule, nsVsysCfgName=nsVsysCfgName)
