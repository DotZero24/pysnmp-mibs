_C='8x'
_B='d'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class ME1200Integer8(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,127))
class ME1200Integer16(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32768,32767))
class ME1200Integer64(TextualConvention,OctetString):status=_A;displayHint=_C;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class ME1200Unsigned8(TextualConvention,Gauge32):status=_A;displayHint=_B;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class ME1200Unsigned16(TextualConvention,Gauge32):status=_A;displayHint=_B;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class ME1200Unsigned64(TextualConvention,OctetString):status=_A;displayHint=_C;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class ME1200TimeStamp(TextualConvention,OctetString):status=_A;displayHint=_C;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class ME1200EtherType(TextualConvention,Gauge32):status=_A;displayHint='x';subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class ME1200InterfaceIndex(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class ME1200RowEditorState(TextualConvention,Gauge32):status=_A;displayHint=_B
class ME1200Percent(TextualConvention,Gauge32):status=_A;displayHint=_B;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class ME1200PortList(TextualConvention,OctetString):status=_A;displayHint=_C;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class ME1200PortListStackable(TextualConvention,OctetString):status=_A;displayHint='128x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
class ME1200Vlan(TextualConvention,Gauge32):status=_A;displayHint=_B;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class ME1200VlanOrZero(TextualConvention,Gauge32):status=_A;displayHint=_B;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
class ME1200VlanListQuarter(TextualConvention,OctetString):status=_A;displayHint='128x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
class ME1200DisplayString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ME1200InetAddress(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,253))
class ME1200VclProtoEncap(TextualConvention,OctetString):status=_A;displayHint='6x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,6))
class ME1200MepDmTimeUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('microSeconds',0),('nanoSeconds',1)))
class ME1200MepInstanceDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
class ME1200MepTxRate(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('invalid',0),('frames300PerSecond',1),('frames100PerSecond',2),('frames10PerSecond',3),('frames1PerSecond',4),('frames6PerMinute',5),('frames1PerMinute',6),('frames6PerHour',7)))
mibBuilder.exportSymbols('ME1200-TC',**{'ME1200Integer8':ME1200Integer8,'ME1200Integer16':ME1200Integer16,'ME1200Integer64':ME1200Integer64,'ME1200Unsigned8':ME1200Unsigned8,'ME1200Unsigned16':ME1200Unsigned16,'ME1200Unsigned64':ME1200Unsigned64,'ME1200TimeStamp':ME1200TimeStamp,'ME1200EtherType':ME1200EtherType,'ME1200InterfaceIndex':ME1200InterfaceIndex,'ME1200RowEditorState':ME1200RowEditorState,'ME1200Percent':ME1200Percent,'ME1200PortList':ME1200PortList,'ME1200PortListStackable':ME1200PortListStackable,'ME1200Vlan':ME1200Vlan,'ME1200VlanOrZero':ME1200VlanOrZero,'ME1200VlanListQuarter':ME1200VlanListQuarter,'ME1200DisplayString':ME1200DisplayString,'ME1200InetAddress':ME1200InetAddress,'ME1200VclProtoEncap':ME1200VclProtoEncap,'ME1200MepDmTimeUnit':ME1200MepDmTimeUnit,'ME1200MepInstanceDirection':ME1200MepInstanceDirection,'ME1200MepTxRate':ME1200MepTxRate})