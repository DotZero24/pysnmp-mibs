#
# PySNMP MIB module ZHONE-RADIO-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/ZHONE-RADIO-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SinglePrecisionFloatingPoint(TextualConvention, Integer32):
    status = 'current'

class SkyZhoneRadioChannelNumber(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'Optimally, the customer should be allowed to use channel numbers\r\n                or frequencies for channel selection. (A ZMS/NMS preference.)\r\n                Minimally the user should use channel numbers and be able to see\r\n                a table of channel to frequency assignments appropriate to\r\n                the node they are configuring.'

class SkyZhoneOperatingFrequency(TextualConvention, Integer32):
    status = 'current'

class SkyZhoneScientificNotation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

mibBuilder.exportSymbols("ZHONE-RADIO-TC-MIB", SkyZhoneScientificNotation=SkyZhoneScientificNotation, SkyZhoneOperatingFrequency=SkyZhoneOperatingFrequency, SkyZhoneRadioChannelNumber=SkyZhoneRadioChannelNumber, SinglePrecisionFloatingPoint=SinglePrecisionFloatingPoint)
