#
# PySNMP MIB module ELTEX-SMI-ACTUAL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-SMI-ACTUAL
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-SMI-ACTUAL", eltexLtd=eltexLtd, elSoftware=elSoftware, eltrapGroup=eltrapGroup, PYSNMP_MODULE_ID=eltexLtd, elHardware=elHardware)
