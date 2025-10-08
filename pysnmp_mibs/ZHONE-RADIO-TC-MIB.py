#
# PySNMP MIB module ZHONE-RADIO-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zhone/ZHONE-RADIO-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
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

mibBuilder.exportSymbols("ZHONE-RADIO-TC-MIB", SkyZhoneScientificNotation=SkyZhoneScientificNotation, SkyZhoneOperatingFrequency=SkyZhoneOperatingFrequency, SinglePrecisionFloatingPoint=SinglePrecisionFloatingPoint, SkyZhoneRadioChannelNumber=SkyZhoneRadioChannelNumber)
