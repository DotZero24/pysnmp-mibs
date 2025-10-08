#
# PySNMP MIB module XEDIA-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/XEDIA-REG
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xedia = ObjectIdentity((1, 3, 6, 1, 4, 1, 838))
if mibBuilder.loadTexts: xedia.setStatus('current')
xediaRegistrations = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 2))
if mibBuilder.loadTexts: xediaRegistrations.setLastUpdated('9612202155Z')
if mibBuilder.loadTexts: xediaRegistrations.setOrganization('Xedia Corp.')
xediaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 3))
if mibBuilder.loadTexts: xediaMibs.setStatus('current')
xediaClasses = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 4))
if mibBuilder.loadTexts: xediaClasses.setStatus('current')
xediaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 5))
if mibBuilder.loadTexts: xediaProducts.setStatus('current')
class LongDisplayString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("XEDIA-REG", xediaRegistrations=xediaRegistrations, PYSNMP_MODULE_ID=xediaRegistrations, xediaClasses=xediaClasses, xediaMibs=xediaMibs, xedia=xedia, LongDisplayString=LongDisplayString, xediaProducts=xediaProducts)
