#
# PySNMP MIB module WATCHGUARD-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/watchguard/WATCHGUARD-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
watchguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 3097))
watchguard.setRevisions(('2008-11-10 00:00',))
if mibBuilder.loadTexts: watchguard.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: watchguard.setOrganization('WatchGuard Technologies, Inc.')
wgProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 1))
if mibBuilder.loadTexts: wgProducts.setStatus('current')
wgSystemConfigMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3097, 2))
if mibBuilder.loadTexts: wgSystemConfigMIB.setStatus('current')
mibBuilder.exportSymbols("WATCHGUARD-SMI", watchguard=watchguard, wgProducts=wgProducts, PYSNMP_MODULE_ID=watchguard, wgSystemConfigMIB=wgSystemConfigMIB)
