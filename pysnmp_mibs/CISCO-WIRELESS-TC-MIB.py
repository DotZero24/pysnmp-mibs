#
# PySNMP MIB module CISCO-WIRELESS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-WIRELESS-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWirelessTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 137))
ciscoWirelessTextualConventions.setRevisions(('2000-04-03 00:00',))
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setLastUpdated('200004030000Z')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setOrganization('Cisco Systems, Inc.')
class CwrRFZeroIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2)

class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedMinute(TextualConvention, Gauge32):
    status = 'current'

class CwrCollectionAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("actionStop", 1), ("actionStart", 2), ("actionClear", 3), ("actionRestart", 4))

class CwrCollectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("statusIdle", 1), ("statusInProgress", 2), ("statusStopped", 3), ("statusCaptured", 4))

class CwrdBm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-80, 33)

class CwrdB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

class CwrThreshLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("upChange", 1), ("downChange", 2), ("highThresh", 3), ("lowThresh", 4), ("upLimit", 5), ("lowLimit", 6))

class CwrRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rsaIN", 1), ("rsaINR", 2), ("rsaConstellationVariance", 3), ("rsaTimingOffset", 4), ("rsaReceivedPower", 5), ("rsaGainSettingsIF", 6), ("rsaGainSettingsRF", 7), ("rsaFreqOffset", 8), ("rsaTotalGain", 9), ("rsaSyncStatus", 10))

class CwrOscState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oscillatorOk", 1), ("osccillatorBad", 2))

class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("rsaSinrMainAnt", 1), ("rsaSinrDiversityAnt", 2), ("rsaSinrRatio", 3), ("rsaTimingOffset", 4), ("rsaRxPowerMainAnt", 5), ("rsaRxPowerDiversityAnt", 6), ("rsaChDelaySpreadMainAnt", 7), ("rsaChDelaySpreadDiversityAnt", 8), ("rsaHeAmbientNoise", 9), ("rsaSuRxPowerDeltaMainAnt", 10), ("rsaSuRxPowerDeltaDiversityAnt", 11), ("rsaSuTotalTxPower", 12))

class CwrRfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("main", 0), ("diversity", 1))

class CwrFixedPointScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class CwrFixedPointPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

class CwrFixedPointValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class P2mpSnapshotAttribute(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class CwrPercentageValue(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000000)

class CwrUpdateTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CwrRfFreqRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60000000)

class WirelessGauge64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("CISCO-WIRELESS-TC-MIB", CwrFixedPointScale=CwrFixedPointScale, CwrRfType=CwrRfType, CwrRFZeroIndex=CwrRFZeroIndex, P2mpRadioSignalAttribute=P2mpRadioSignalAttribute, CwrRadioSignalAttribute=CwrRadioSignalAttribute, ciscoWirelessTextualConventions=ciscoWirelessTextualConventions, CwrCollectionStatus=CwrCollectionStatus, P2mpSnapshotAttribute=P2mpSnapshotAttribute, CwrCwDegradedMinute=CwrCwDegradedMinute, CwrFixedPointPrecision=CwrFixedPointPrecision, CwrdB=CwrdB, CwrCollectionAction=CwrCollectionAction, CwrUpdateTime=CwrUpdateTime, CwrPercentageValue=CwrPercentageValue, WirelessGauge64=WirelessGauge64, PYSNMP_MODULE_ID=ciscoWirelessTextualConventions, CwrCwDegradedSecond=CwrCwDegradedSecond, CwrFixedPointValue=CwrFixedPointValue, CwrCwErrorFreeSecond=CwrCwErrorFreeSecond, CwrCwErroredSecond=CwrCwErroredSecond, CwrOscState=CwrOscState, CwrRfFreqRange=CwrRfFreqRange, CwrCwConsecutiveSevErrSecond=CwrCwConsecutiveSevErrSecond, CwrThreshLimitType=CwrThreshLimitType, CwrdBm=CwrdBm, CwrCwSeverelyErroredSecond=CwrCwSeverelyErroredSecond)
