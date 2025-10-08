#
# PySNMP MIB module ELECTROLINE-DHT-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-ROOT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
electrolineHardwareProducts, = mibBuilder.importSymbols("ELECTROLINE-GLOBAL-REG", "electrolineHardwareProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELECTROLINE-DHT-ROOT-MIB", dhtStatus=dhtStatus, dhtConfiguration=dhtConfiguration, dhtInventory=dhtInventory, dhtPrivate=dhtPrivate, electrolineDHT=electrolineDHT, PYSNMP_MODULE_ID=electrolineDHT, dhtExtensionsMib=dhtExtensionsMib)
