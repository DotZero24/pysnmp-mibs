_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vendor=ModuleIdentity((1,3,6,1,4,1,34592))
if mibBuilder.loadTexts:vendor.setRevisions(('2016-03-02 14:47',))
class DataDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('downstream',2)))
class DeviceOperation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('reset',2),('default',3),('saveConfig',4),('restore',5),('delete',6)))
class DeviceStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notPresent',1),('offline',2),('online',3),('normal',4),('abnormal',5)))
class DeviceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(67174657));namedValues=NamedValues(('fd1508gs',67174657))
class LedStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('blink',3)))
class OperSwitch(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_IpProduct_ObjectIdentity=ObjectIdentity
ipProduct=_IpProduct_ObjectIdentity((1,3,6,1,4,1,34592,1))
if mibBuilder.loadTexts:ipProduct.setStatus(_A)
_MediaConverter_ObjectIdentity=ObjectIdentity
mediaConverter=_MediaConverter_ObjectIdentity((1,3,6,1,4,1,34592,1,1))
if mibBuilder.loadTexts:mediaConverter.setStatus(_A)
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,34592,1,2))
if mibBuilder.loadTexts:switch.setStatus(_A)
_Epon_ObjectIdentity=ObjectIdentity
epon=_Epon_ObjectIdentity((1,3,6,1,4,1,34592,1,3))
if mibBuilder.loadTexts:epon.setStatus(_A)
_Eoc_ObjectIdentity=ObjectIdentity
eoc=_Eoc_ObjectIdentity((1,3,6,1,4,1,34592,1,4))
if mibBuilder.loadTexts:eoc.setStatus(_A)
_Gpon_ObjectIdentity=ObjectIdentity
gpon=_Gpon_ObjectIdentity((1,3,6,1,4,1,34592,1,5))
if mibBuilder.loadTexts:gpon.setStatus(_A)
mibBuilder.exportSymbols('CDATA-COMMON-SMI',**{'DataDirection':DataDirection,'DeviceOperation':DeviceOperation,'DeviceStatus':DeviceStatus,'DeviceType':DeviceType,'LedStatus':LedStatus,'OperSwitch':OperSwitch,'vendor':vendor,'ipProduct':ipProduct,'mediaConverter':mediaConverter,'switch':switch,'epon':epon,'eoc':eoc,'gpon':gpon})