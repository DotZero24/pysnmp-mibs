#
# PySNMP MIB module WATCHGUARD-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/watchguard/WATCHGUARD-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
watchguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097))
watchguard.setRevisions(('2008-11-10 00:00',))
if mibBuilder.loadTexts: watchguard.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: watchguard.setOrganization('WatchGuard Technologies, Inc.')
wgProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 1))
if mibBuilder.loadTexts: wgProducts.setStatus('current')
wgSystemConfigMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2))
if mibBuilder.loadTexts: wgSystemConfigMIB.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-SMI", PYSNMP_MODULE_ID=watchguard, wgSystemConfigMIB=wgSystemConfigMIB, watchguard=watchguard, wgProducts=wgProducts)
