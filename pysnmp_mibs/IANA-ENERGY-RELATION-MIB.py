#
# PySNMP MIB module IANA-ENERGY-RELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/IANA-ENERGY-RELATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaEnergyRelationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 232))
ianaEnergyRelationMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setOrganization('IANA')
class IANAEnergyRelationship(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("poweredBy", 1), ("powering", 2), ("meteredBy", 3), ("metering", 4), ("aggregatedBy", 5), ("aggregating", 6))

mibBuilder.exportSymbols("IANA-ENERGY-RELATION-MIB", ianaEnergyRelationMIB=ianaEnergyRelationMIB, PYSNMP_MODULE_ID=ianaEnergyRelationMIB, IANAEnergyRelationship=IANAEnergyRelationship)
