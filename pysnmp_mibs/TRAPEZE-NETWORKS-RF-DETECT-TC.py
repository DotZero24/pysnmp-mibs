#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-DETECT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-RF-DETECT-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFDetectTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 11))
trpzRFDetectTc.setRevisions(('2011-07-27 00:11', '2009-08-13 00:10', '2007-04-18 00:02', '2007-03-28 00:01',))
if mibBuilder.loadTexts: trpzRFDetectTc.setLastUpdated('201107270011Z')
if mibBuilder.loadTexts: trpzRFDetectTc.setOrganization('Trapeze Networks')
class TrpzRFDetectClassificationReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("other", 1), ("default-classification", 2), ("rogue-list", 3), ("ap-in-modo", 4), ("neighbor-list", 5), ("ssid-masquerade", 6), ("seen-in-network", 7), ("ad-hoc", 8), ("ssid-list", 9), ("pass-fingerprint", 10), ("fail-fingerprint", 11))

class TrpzRFDetectClassification(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("not-classified", 2), ("member", 3), ("neighbor", 4), ("suspect", 5), ("rogue", 6), ("tag", 7))

class TrpzRFDetectNetworkingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ad-hoc", 1), ("infrastructure", 2))

class TrpzRFDetectDot11ModulationStandard(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("dot11Unknown", 1), ("dot11Other", 2), ("dot11A", 3), ("dot11B", 4), ("dot11G", 5), ("dot11NA", 6), ("dot11NG", 7))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-DETECT-TC", trpzRFDetectTc=trpzRFDetectTc, TrpzRFDetectDot11ModulationStandard=TrpzRFDetectDot11ModulationStandard, TrpzRFDetectClassification=TrpzRFDetectClassification, TrpzRFDetectClassificationReason=TrpzRFDetectClassificationReason, TrpzRFDetectNetworkingMode=TrpzRFDetectNetworkingMode, PYSNMP_MODULE_ID=trpzRFDetectTc)
