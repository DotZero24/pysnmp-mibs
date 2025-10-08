#
# PySNMP MIB module IANA-ENERGY-RELATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IANA-ENERGY-RELATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaEnergyRelationMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 232))
ianaEnergyRelationMIB.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaEnergyRelationMIB.setOrganization('IANA')
class IANAEnergyRelationship(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("poweredBy", 1), ("powering", 2), ("meteredBy", 3), ("metering", 4), ("aggregatedBy", 5), ("aggregating", 6))

mibBuilder.exportSymbols("IANA-ENERGY-RELATION-MIB", ianaEnergyRelationMIB=ianaEnergyRelationMIB, IANAEnergyRelationship=IANAEnergyRelationship, PYSNMP_MODULE_ID=ianaEnergyRelationMIB)
