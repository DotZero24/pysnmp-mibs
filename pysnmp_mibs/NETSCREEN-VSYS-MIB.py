#
# PySNMP MIB module NETSCREEN-VSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netscreen/NETSCREEN-VSYS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
netscreenVsys, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVsys")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("NETSCREEN-VSYS-MIB", PYSNMP_MODULE_ID=netscreenVsysMibModule, netscreenVsysMibModule=netscreenVsysMibModule, nsVsysCfgId=nsVsysCfgId, nsVsysCfgName=nsVsysCfgName, nsVsysCfg=nsVsysCfg, nsVsysCfgEntry=nsVsysCfgEntry, nsVsysCfgTable=nsVsysCfgTable)
