#
# PySNMP MIB module WATCHGUARD-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/watchguard/WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
watchguard, = mibBuilder.importSymbols("WATCHGUARD-SMI", "watchguard")
wgInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097, 6))
wgInfoModule.setRevisions(('2007-01-25 12:00',))
if mibBuilder.loadTexts: wgInfoModule.setLastUpdated('200701251200Z')
if mibBuilder.loadTexts: wgInfoModule.setOrganization('WatchGuard Technologies, Inc.')
wgInfoSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 6, 1))
if mibBuilder.loadTexts: wgInfoSystem.setStatus('current')
wgInfoSystemCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoSystemCurrentTime.setStatus('current')
wgInfoGavService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoGavService.setStatus('current')
wgInfoIpsService = MibScalar((1, 3, 6, 1, 4, 1, 3097, 6, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wgInfoIpsService.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-INFO-SYSTEM-MIB", wgInfoModule=wgInfoModule, wgInfoGavService=wgInfoGavService, wgInfoSystemCurrentTime=wgInfoSystemCurrentTime, wgInfoSystem=wgInfoSystem, wgInfoIpsService=wgInfoIpsService, PYSNMP_MODULE_ID=wgInfoModule)
