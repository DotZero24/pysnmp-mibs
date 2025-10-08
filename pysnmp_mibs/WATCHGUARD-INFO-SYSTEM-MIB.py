#
# PySNMP MIB module WATCHGUARD-INFO-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/watchguard/WATCHGUARD-INFO-SYSTEM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
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
mibBuilder.exportSymbols("WATCHGUARD-INFO-SYSTEM-MIB", wgInfoIpsService=wgInfoIpsService, wgInfoGavService=wgInfoGavService, PYSNMP_MODULE_ID=wgInfoModule, wgInfoSystemCurrentTime=wgInfoSystemCurrentTime, wgInfoModule=wgInfoModule, wgInfoSystem=wgInfoSystem)
