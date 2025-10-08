#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-NOISE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-RF-NOISE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-NOISE-TC-MIB", trpzRFNoiseTc=trpzRFNoiseTc, TrpzRFNoiseSourceID=TrpzRFNoiseSourceID, TrpzRFNoiseSourceType=TrpzRFNoiseSourceType, PYSNMP_MODULE_ID=trpzRFNoiseTc)
