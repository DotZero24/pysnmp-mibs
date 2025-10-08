#
# PySNMP MIB module IANA-GBOND-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/IANA-GBOND-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaGBondTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 215))
ianaGBondTcMIB.setRevisions(('2013-02-20 00:00',))
if mibBuilder.loadTexts: ianaGBondTcMIB.setLastUpdated('201302200000Z')
if mibBuilder.loadTexts: ianaGBondTcMIB.setOrganization('IANA')
class IANAgBondSchemeList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

class IANAgBondScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

mibBuilder.exportSymbols("IANA-GBOND-TC-MIB", IANAgBondSchemeList=IANAgBondSchemeList, ianaGBondTcMIB=ianaGBondTcMIB, IANAgBondScheme=IANAgBondScheme, PYSNMP_MODULE_ID=ianaGBondTcMIB)
