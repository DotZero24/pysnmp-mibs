#
# PySNMP MIB module CIE1000-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CIE1000-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class CIE1000Integer8(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class CIE1000Integer16(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class CIE1000Integer64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CIE1000Unsigned8(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class CIE1000Unsigned16(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CIE1000Unsigned64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CIE1000TimeStamp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class CIE1000EtherType(TextualConvention, Gauge32):
    status = 'current'
    displayHint = '2x'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CIE1000InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CIE1000RowEditorState(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class CIE1000Percent(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class CIE1000PortList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CIE1000Vlan(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 4095)

class CIE1000VlanOrZero(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 4095)

class CIE1000VlanListQuarter(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(128, 128)
    fixedLength = 128

class CIE1000DisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CIE1000InetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 253)

class CIE1000IpAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 46)

class CIE1000VclProtoEncap(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 6)

class CIE1000BitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("any", 0), ("zero", 1), ("one", 2))

class CIE1000DestMacType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("any", 0), ("unicast", 1), ("multicast", 2), ("broadcast", 3))

class CIE1000VcapKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("normal", 0), ("doubleTag", 1), ("ipAddr", 2), ("macIpAddr", 3))

class CIE1000VlanTagPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("any", 0), ("value0", 1), ("value1", 2), ("value2", 3), ("value3", 4), ("value4", 5), ("value5", 6), ("value6", 7), ("value7", 8), ("range0to1", 9), ("range2to3", 10), ("range4to5", 11), ("range6to7", 12), ("range0to3", 13), ("range4to7", 14))

class CIE1000VlanTagType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("any", 0), ("untagged", 1), ("tagged", 2), ("cTagged", 3), ("sTagged", 4))

class CIE1000ASRType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("any", 0), ("specific", 1), ("range", 2))

class CIE1000AdvDestMacType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("any", 0), ("unicast", 1), ("multicast", 2), ("broadcast", 3), ("specific", 4))

class CIE1000ASType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("any", 0), ("specific", 1))

class CIE1000SfpTransceiver(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("none", 0), ("notSupported", 1), ("sfp100FX", 2), ("sfp1000BaseT", 7), ("sfp1000BaseCx", 8), ("sfp1000BaseSx", 9), ("sfp1000BaseLx", 10), ("sfp1000BaseX", 11), ("sfp2G5", 12), ("sfp5G", 13), ("sfp10G", 14))

class CIE1000MepDmTimeUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("microSeconds", 0), ("nanoSeconds", 1))

class CIE1000MepInstanceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class CIE1000MepTxRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("invalid", 0), ("frames300PerSecond", 1), ("frames100PerSecond", 2), ("frames10PerSecond", 3), ("frames1PerSecond", 4), ("frames6PerMinute", 5), ("frames1PerMinute", 6), ("frames6PerHour", 7))

class CIE1000PortStatusSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("speed10M", 1), ("speed100M", 2), ("speed1G", 3), ("speed2G5", 4), ("speed5G", 5), ("speed10G", 6), ("speed12G", 7))

mibBuilder.exportSymbols("CIE1000-TC", CIE1000EtherType=CIE1000EtherType, CIE1000Unsigned8=CIE1000Unsigned8, CIE1000VlanTagPriority=CIE1000VlanTagPriority, CIE1000ASRType=CIE1000ASRType, CIE1000BitType=CIE1000BitType, CIE1000AdvDestMacType=CIE1000AdvDestMacType, CIE1000Unsigned16=CIE1000Unsigned16, CIE1000PortStatusSpeed=CIE1000PortStatusSpeed, CIE1000VlanOrZero=CIE1000VlanOrZero, CIE1000RowEditorState=CIE1000RowEditorState, CIE1000Percent=CIE1000Percent, CIE1000IpAddress=CIE1000IpAddress, CIE1000MepTxRate=CIE1000MepTxRate, CIE1000SfpTransceiver=CIE1000SfpTransceiver, CIE1000Integer8=CIE1000Integer8, CIE1000TimeStamp=CIE1000TimeStamp, CIE1000Vlan=CIE1000Vlan, CIE1000Integer16=CIE1000Integer16, CIE1000Unsigned64=CIE1000Unsigned64, CIE1000DestMacType=CIE1000DestMacType, CIE1000VlanTagType=CIE1000VlanTagType, CIE1000InetAddress=CIE1000InetAddress, CIE1000Integer64=CIE1000Integer64, CIE1000MepInstanceDirection=CIE1000MepInstanceDirection, CIE1000DisplayString=CIE1000DisplayString, CIE1000VlanListQuarter=CIE1000VlanListQuarter, CIE1000MepDmTimeUnit=CIE1000MepDmTimeUnit, CIE1000VclProtoEncap=CIE1000VclProtoEncap, CIE1000ASType=CIE1000ASType, CIE1000InterfaceIndex=CIE1000InterfaceIndex, CIE1000PortList=CIE1000PortList, CIE1000VcapKeyType=CIE1000VcapKeyType)
