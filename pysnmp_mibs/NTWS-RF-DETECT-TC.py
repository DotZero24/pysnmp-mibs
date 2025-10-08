#
# PySNMP MIB module NTWS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-RF-DETECT-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 11))
ntwsRFDetectTc.setRevisions(('2008-05-15 00:03', '2007-04-18 00:02', '2007-03-28 00:01',))
if mibBuilder.loadTexts: ntwsRFDetectTc.setLastUpdated('200805150003Z')
if mibBuilder.loadTexts: ntwsRFDetectTc.setOrganization('Nortel Networks')
class NtwsRFDetectClassificationReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class NtwsRFDetectClassification(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6))

class NtwsRFDetectNetworkingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

mibBuilder.exportSymbols("NTWS-RF-DETECT-TC", PYSNMP_MODULE_ID=ntwsRFDetectTc, NtwsRFDetectClassificationReason=NtwsRFDetectClassificationReason, ntwsRFDetectTc=ntwsRFDetectTc, NtwsRFDetectClassification=NtwsRFDetectClassification, NtwsRFDetectNetworkingMode=NtwsRFDetectNetworkingMode)
