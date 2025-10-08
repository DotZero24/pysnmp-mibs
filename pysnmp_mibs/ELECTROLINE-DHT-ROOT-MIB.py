#
# PySNMP MIB module ELECTROLINE-DHT-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
electrolineHardwareProducts, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineHardwareProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
electrolineDHT = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2))
electrolineDHT.setRevisions(('2003-03-20 00:00',))
if mibBuilder.loadTexts: electrolineDHT.setLastUpdated('200303200000Z')
if mibBuilder.loadTexts: electrolineDHT.setOrganization('Electroline Equipment Inc')
dhtInventory = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1))
if mibBuilder.loadTexts: dhtInventory.setStatus('current')
dhtConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2))
if mibBuilder.loadTexts: dhtConfiguration.setStatus('current')
dhtStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 3))
if mibBuilder.loadTexts: dhtStatus.setStatus('current')
dhtPrivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 4))
if mibBuilder.loadTexts: dhtPrivate.setStatus('current')
dhtExtensionsMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5))
if mibBuilder.loadTexts: dhtExtensionsMib.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DHT-ROOT-MIB", dhtExtensionsMib=dhtExtensionsMib, dhtInventory=dhtInventory, dhtConfiguration=dhtConfiguration, PYSNMP_MODULE_ID=electrolineDHT, dhtPrivate=dhtPrivate, electrolineDHT=electrolineDHT, dhtStatus=dhtStatus)
