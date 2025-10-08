#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-NOISE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-RF-NOISE-TC-MIB
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
trpzRFNoiseTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 22))
trpzRFNoiseTc.setRevisions(('2011-01-10 00:00',))
if mibBuilder.loadTexts: trpzRFNoiseTc.setLastUpdated('201101100000Z')
if mibBuilder.loadTexts: trpzRFNoiseTc.setOrganization('Trapeze Networks')
class TrpzRFNoiseSourceID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TrpzRFNoiseSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 16, 33, 49, 50, 64, 65, 66))
    namedValues = NamedValues(("nsUnknown", 0), ("nsContinuousWave", 1), ("nsVideo", 16), ("nsMicrowaveOven", 33), ("nsPhoneDECT", 49), ("nsPhoneFHSS", 50), ("nsBluetoothAny", 64), ("nsBluetoothHeadset", 65), ("nsBluetoothHandsfree", 66))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-NOISE-TC-MIB", trpzRFNoiseTc=trpzRFNoiseTc, TrpzRFNoiseSourceID=TrpzRFNoiseSourceID, PYSNMP_MODULE_ID=trpzRFNoiseTc, TrpzRFNoiseSourceType=TrpzRFNoiseSourceType)
