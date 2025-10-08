#
# PySNMP MIB module NETSCREEN-ZONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netscreen/NETSCREEN-ZONE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
netscreenZone, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenZone")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenZoneMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 8, 0))
netscreenZoneMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-05-08 00:00',))
if mibBuilder.loadTexts: netscreenZoneMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenZoneMibModule.setOrganization('Juniper Networks, Inc.')
nsZoneCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 8, 1))
nsZoneCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1), )
if mibBuilder.loadTexts: nsZoneCfgTable.setStatus('current')
nsZoneCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1), ).setIndexNames((0, "NETSCREEN-ZONE-MIB", "nsZoneCfgId"))
if mibBuilder.loadTexts: nsZoneCfgEntry.setStatus('current')
nsZoneCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgId.setStatus('current')
nsZoneCfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgName.setStatus('current')
nsZoneCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("regular", 0), ("layer2", 1), ("tunnel", 2), ("null", 3), ("func", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgType.setStatus('current')
nsZoneCfgVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgVsys.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-ZONE-MIB", nsZoneCfg=nsZoneCfg, nsZoneCfgName=nsZoneCfgName, netscreenZoneMibModule=netscreenZoneMibModule, nsZoneCfgTable=nsZoneCfgTable, nsZoneCfgEntry=nsZoneCfgEntry, PYSNMP_MODULE_ID=netscreenZoneMibModule, nsZoneCfgType=nsZoneCfgType, nsZoneCfgId=nsZoneCfgId, nsZoneCfgVsys=nsZoneCfgVsys)
