#
# PySNMP MIB module ELECTROLINE-DHT-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-EXTENSIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
electrolineDHT, = mibBuilder.importSymbols("ELECTROLINE-DHT-ROOT-MIB", "electrolineDHT")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dhtExtensionsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5))
dhtExtensionsMib.setRevisions(('2004-12-09 00:00',))
if mibBuilder.loadTexts: dhtExtensionsMib.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: dhtExtensionsMib.setOrganization('Electroline Equipment Inc')
dhtExtensionsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1))
dhtExtensionsSupported = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtExtensionsSupported.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DHT-EXTENSIONS-MIB", dhtExtensionsMib=dhtExtensionsMib, dhtExtensionsSupported=dhtExtensionsSupported, PYSNMP_MODULE_ID=dhtExtensionsMib, dhtExtensionsMibObjects=dhtExtensionsMibObjects)
