#
# PySNMP MIB module ME1200-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class ME1200Integer8(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-128, 127)

class ME1200Integer16(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-32768, 32767)

class ME1200Integer64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ME1200Unsigned8(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class ME1200Unsigned16(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ME1200Unsigned64(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ME1200TimeStamp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ME1200EtherType(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ME1200InterfaceIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ME1200RowEditorState(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class ME1200Percent(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class ME1200PortList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '8x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ME1200PortListStackable(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(128, 128)
    fixedLength = 128

class ME1200Vlan(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 4095)

class ME1200VlanOrZero(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 4095)

class ME1200VlanListQuarter(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(128, 128)
    fixedLength = 128

class ME1200DisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ME1200InetAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 253)

class ME1200VclProtoEncap(TextualConvention, OctetString):
    status = 'current'
    displayHint = '6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 6)

class ME1200MepDmTimeUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("microSeconds", 0), ("nanoSeconds", 1))

class ME1200MepInstanceDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("down", 0), ("up", 1))

class ME1200MepTxRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("invalid", 0), ("frames300PerSecond", 1), ("frames100PerSecond", 2), ("frames10PerSecond", 3), ("frames1PerSecond", 4), ("frames6PerMinute", 5), ("frames1PerMinute", 6), ("frames6PerHour", 7))

mibBuilder.exportSymbols("ME1200-TC", ME1200Percent=ME1200Percent, ME1200MepDmTimeUnit=ME1200MepDmTimeUnit, ME1200MepTxRate=ME1200MepTxRate, ME1200Integer8=ME1200Integer8, ME1200Integer16=ME1200Integer16, ME1200PortList=ME1200PortList, ME1200Integer64=ME1200Integer64, ME1200InetAddress=ME1200InetAddress, ME1200Unsigned64=ME1200Unsigned64, ME1200VclProtoEncap=ME1200VclProtoEncap, ME1200InterfaceIndex=ME1200InterfaceIndex, ME1200RowEditorState=ME1200RowEditorState, ME1200VlanListQuarter=ME1200VlanListQuarter, ME1200DisplayString=ME1200DisplayString, ME1200Unsigned16=ME1200Unsigned16, ME1200Vlan=ME1200Vlan, ME1200VlanOrZero=ME1200VlanOrZero, ME1200Unsigned8=ME1200Unsigned8, ME1200TimeStamp=ME1200TimeStamp, ME1200MepInstanceDirection=ME1200MepInstanceDirection, ME1200PortListStackable=ME1200PortListStackable, ME1200EtherType=ME1200EtherType)
