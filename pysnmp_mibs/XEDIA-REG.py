#
# PySNMP MIB module XEDIA-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/XEDIA-REG
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("XEDIA-REG", LongDisplayString=LongDisplayString, xediaProducts=xediaProducts, xedia=xedia, xediaMibs=xediaMibs, xediaClasses=xediaClasses, PYSNMP_MODULE_ID=xediaRegistrations, xediaRegistrations=xediaRegistrations)
