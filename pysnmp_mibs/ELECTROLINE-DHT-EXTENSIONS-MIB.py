#
# PySNMP MIB module ELECTROLINE-DHT-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-EXTENSIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
electrolineDHT, = mibBuilder.importSymbols("ELECTROLINE-DHT-ROOT-MIB", "electrolineDHT")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dhtExtensionsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5))
dhtExtensionsMib.setRevisions(('2004-12-09 00:00',))
if mibBuilder.loadTexts: dhtExtensionsMib.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: dhtExtensionsMib.setOrganization('Electroline Equipment Inc')
dhtExtensionsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1))
dhtExtensionsSupported = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtExtensionsSupported.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DHT-EXTENSIONS-MIB", dhtExtensionsMibObjects=dhtExtensionsMibObjects, PYSNMP_MODULE_ID=dhtExtensionsMib, dhtExtensionsMib=dhtExtensionsMib, dhtExtensionsSupported=dhtExtensionsSupported)
