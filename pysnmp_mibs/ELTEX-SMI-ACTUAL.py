#
# PySNMP MIB module ELTEX-SMI-ACTUAL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-SMI-ACTUAL
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
eltexLtd = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265))
eltexLtd.setRevisions(('2012-05-29 00:00',))
if mibBuilder.loadTexts: eltexLtd.setLastUpdated('201205290000Z')
if mibBuilder.loadTexts: eltexLtd.setOrganization('Eltex Enterprise, Ltd.')
elHardware = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 1))
if mibBuilder.loadTexts: elHardware.setStatus('current')
elSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 2))
if mibBuilder.loadTexts: elSoftware.setStatus('current')
eltrapGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 35265, 3))
if mibBuilder.loadTexts: eltrapGroup.setStatus('current')
mibBuilder.exportSymbols("ELTEX-SMI-ACTUAL", eltexLtd=eltexLtd, eltrapGroup=eltrapGroup, elSoftware=elSoftware, PYSNMP_MODULE_ID=eltexLtd, elHardware=elHardware)
