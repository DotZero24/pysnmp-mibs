_H='sensIndex'
_G='not-accessible'
_F='inpIndex'
_E='normal'
_D='DisplayString'
_C='STE-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class UnitType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('none',0),('celsius',1),('fahrenheit',2),('kelvin',3),('percent',4)))
class OnOff(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
class InputAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('alarm',1)))
class IOName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid',0),(_E,1),('outofrangelo',2),('outofrangehi',3),('alarmlo',4),('alarmhi',5)))
class SensorSN(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorValue(Integer32):0
class SensorID(Integer32):0
class SensorString(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Hwgroup_ObjectIdentity=ObjectIdentity
hwgroup=_Hwgroup_ObjectIdentity((1,3,6,1,4,1,21796))
_X390_ObjectIdentity=ObjectIdentity
x390=_X390_ObjectIdentity((1,3,6,1,4,1,21796,4))
_Ste_ObjectIdentity=ObjectIdentity
ste=_Ste_ObjectIdentity((1,3,6,1,4,1,21796,4,1))
_InpTable_Object=MibTable
inpTable=_InpTable_Object((1,3,6,1,4,1,21796,4,1,1))
if mibBuilder.loadTexts:inpTable.setStatus(_A)
_InpEntry_Object=MibTableRow
inpEntry=_InpEntry_Object((1,3,6,1,4,1,21796,4,1,1,1))
inpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:inpEntry.setStatus(_A)
_InpIndex_Type=PositiveInteger
_InpIndex_Object=MibTableColumn
inpIndex=_InpIndex_Object((1,3,6,1,4,1,21796,4,1,1,1,1),_InpIndex_Type())
inpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:inpIndex.setStatus(_A)
_InpValue_Type=OnOff
_InpValue_Object=MibTableColumn
inpValue=_InpValue_Object((1,3,6,1,4,1,21796,4,1,1,1,2),_InpValue_Type())
inpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:inpValue.setStatus(_A)
_InpName_Type=IOName
_InpName_Object=MibTableColumn
inpName=_InpName_Object((1,3,6,1,4,1,21796,4,1,1,1,3),_InpName_Type())
inpName.setMaxAccess(_B)
if mibBuilder.loadTexts:inpName.setStatus(_A)
_InpAlarmState_Type=InputAlarmState
_InpAlarmState_Object=MibTableColumn
inpAlarmState=_InpAlarmState_Object((1,3,6,1,4,1,21796,4,1,1,1,4),_InpAlarmState_Type())
inpAlarmState.setMaxAccess(_B)
if mibBuilder.loadTexts:inpAlarmState.setStatus(_A)
_SensTable_Object=MibTable
sensTable=_SensTable_Object((1,3,6,1,4,1,21796,4,1,3))
if mibBuilder.loadTexts:sensTable.setStatus(_A)
_SensEntry_Object=MibTableRow
sensEntry=_SensEntry_Object((1,3,6,1,4,1,21796,4,1,3,1))
sensEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:sensEntry.setStatus(_A)
_SensIndex_Type=PositiveInteger
_SensIndex_Object=MibTableColumn
sensIndex=_SensIndex_Object((1,3,6,1,4,1,21796,4,1,3,1,1),_SensIndex_Type())
sensIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:sensIndex.setStatus(_A)
_SensName_Type=SensorName
_SensName_Object=MibTableColumn
sensName=_SensName_Object((1,3,6,1,4,1,21796,4,1,3,1,2),_SensName_Type())
sensName.setMaxAccess(_B)
if mibBuilder.loadTexts:sensName.setStatus(_A)
_SensState_Type=SensorState
_SensState_Object=MibTableColumn
sensState=_SensState_Object((1,3,6,1,4,1,21796,4,1,3,1,3),_SensState_Type())
sensState.setMaxAccess(_B)
if mibBuilder.loadTexts:sensState.setStatus(_A)
_SensString_Type=SensorString
_SensString_Object=MibTableColumn
sensString=_SensString_Object((1,3,6,1,4,1,21796,4,1,3,1,4),_SensString_Type())
sensString.setMaxAccess(_B)
if mibBuilder.loadTexts:sensString.setStatus(_A)
_SensValue_Type=SensorValue
_SensValue_Object=MibTableColumn
sensValue=_SensValue_Object((1,3,6,1,4,1,21796,4,1,3,1,5),_SensValue_Type())
sensValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sensValue.setStatus(_A)
_SensSN_Type=SensorSN
_SensSN_Object=MibTableColumn
sensSN=_SensSN_Object((1,3,6,1,4,1,21796,4,1,3,1,6),_SensSN_Type())
sensSN.setMaxAccess(_B)
if mibBuilder.loadTexts:sensSN.setStatus(_A)
_SensUnit_Type=UnitType
_SensUnit_Object=MibTableColumn
sensUnit=_SensUnit_Object((1,3,6,1,4,1,21796,4,1,3,1,7),_SensUnit_Type())
sensUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:sensUnit.setStatus(_A)
_SensID_Type=UnitType
_SensID_Object=MibTableColumn
sensID=_SensID_Object((1,3,6,1,4,1,21796,4,1,3,1,8),_SensID_Type())
sensID.setMaxAccess(_B)
if mibBuilder.loadTexts:sensID.setStatus(_A)
_Info_ObjectIdentity=ObjectIdentity
info=_Info_ObjectIdentity((1,3,6,1,4,1,21796,4,1,70))
class _InfoAddressMAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_InfoAddressMAC_Type.__name__=_D
_InfoAddressMAC_Object=MibScalar
infoAddressMAC=_InfoAddressMAC_Object((1,3,6,1,4,1,21796,4,1,70,1),_InfoAddressMAC_Type())
infoAddressMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:infoAddressMAC.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PositiveInteger':PositiveInteger,'UnitType':UnitType,'OnOff':OnOff,'InputAlarmState':InputAlarmState,'IOName':IOName,'SensorState':SensorState,'SensorSN':SensorSN,'SensorName':SensorName,'SensorValue':SensorValue,'SensorID':SensorID,'SensorString':SensorString,'hwgroup':hwgroup,'x390':x390,'ste':ste,'inpTable':inpTable,'inpEntry':inpEntry,_F:inpIndex,'inpValue':inpValue,'inpName':inpName,'inpAlarmState':inpAlarmState,'sensTable':sensTable,'sensEntry':sensEntry,_H:sensIndex,'sensName':sensName,'sensState':sensState,'sensString':sensString,'sensValue':sensValue,'sensSN':sensSN,'sensUnit':sensUnit,'sensID':sensID,'info':info,'infoAddressMAC':infoAddressMAC})