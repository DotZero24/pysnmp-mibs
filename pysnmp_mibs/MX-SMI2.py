#
# PySNMP MIB module MX-SMI2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SMI2
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrix, = mibBuilder.importSymbols("MX-SMI", "mediatrix")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mediatrixSystem = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000))
if mibBuilder.loadTexts: mediatrixSystem.setStatus('current')
gen5 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100))
if mibBuilder.loadTexts: gen5.setStatus('current')
mediatrixProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100))
if mibBuilder.loadTexts: mediatrixProducts.setStatus('current')
mediatrixCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200))
if mibBuilder.loadTexts: mediatrixCommon.setStatus('current')
mediatrixServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100))
if mibBuilder.loadTexts: mediatrixServices.setStatus('current')
mediatrixHardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500))
if mibBuilder.loadTexts: mediatrixHardware.setStatus('current')
mibBuilder.exportSymbols("MX-SMI2", mediatrixHardware=mediatrixHardware, mediatrixServices=mediatrixServices, mediatrixSystem=mediatrixSystem, gen5=gen5, mediatrixProducts=mediatrixProducts, mediatrixCommon=mediatrixCommon)
