_P='normal'
_O='invalid'
_N='DisplayString'
_M='NotificationType'
_L='wldValue'
_K='wldID'
_J='wldSN'
_I='wldState'
_H='wldName'
_G='infoAddressMAC'
_F='sysName'
_E='SNMPv2-MIB'
_D='wldIndex'
_C='read-only'
_B='mandatory'
_A='HWg-WLD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_M,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_M,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class SensorState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*((_O,0),(_P,1),('alarm',3)))
class SensorValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('flooded',1),('disconnect',2),(_O,3)))
class SensorSN(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorID(Integer32):0
_Hwgroup_ObjectIdentity=ObjectIdentity
hwgroup=_Hwgroup_ObjectIdentity((1,3,6,1,4,1,21796))
_X390_ObjectIdentity=ObjectIdentity
x390=_X390_ObjectIdentity((1,3,6,1,4,1,21796,4))
_Hwgwld_ObjectIdentity=ObjectIdentity
hwgwld=_Hwgwld_ObjectIdentity((1,3,6,1,4,1,21796,4,5))
_SensTable_Object=MibTable
sensTable=_SensTable_Object((1,3,6,1,4,1,21796,4,5,4))
if mibBuilder.loadTexts:sensTable.setStatus(_B)
_WldEntry_Object=MibTableRow
wldEntry=_WldEntry_Object((1,3,6,1,4,1,21796,4,5,4,1))
wldEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:wldEntry.setStatus(_B)
_WldIndex_Type=PositiveInteger
_WldIndex_Object=MibTableColumn
wldIndex=_WldIndex_Object((1,3,6,1,4,1,21796,4,5,4,1,1),_WldIndex_Type())
wldIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wldIndex.setStatus(_B)
_WldName_Type=SensorName
_WldName_Object=MibTableColumn
wldName=_WldName_Object((1,3,6,1,4,1,21796,4,5,4,1,2),_WldName_Type())
wldName.setMaxAccess(_C)
if mibBuilder.loadTexts:wldName.setStatus(_B)
_WldState_Type=SensorState
_WldState_Object=MibTableColumn
wldState=_WldState_Object((1,3,6,1,4,1,21796,4,5,4,1,3),_WldState_Type())
wldState.setMaxAccess(_C)
if mibBuilder.loadTexts:wldState.setStatus(_B)
_WldSN_Type=SensorSN
_WldSN_Object=MibTableColumn
wldSN=_WldSN_Object((1,3,6,1,4,1,21796,4,5,4,1,4),_WldSN_Type())
wldSN.setMaxAccess(_C)
if mibBuilder.loadTexts:wldSN.setStatus(_B)
_WldID_Type=SensorID
_WldID_Object=MibTableColumn
wldID=_WldID_Object((1,3,6,1,4,1,21796,4,5,4,1,5),_WldID_Type())
wldID.setMaxAccess(_C)
if mibBuilder.loadTexts:wldID.setStatus(_B)
_WldValue_Type=SensorValue
_WldValue_Object=MibTableColumn
wldValue=_WldValue_Object((1,3,6,1,4,1,21796,4,5,4,1,6),_WldValue_Type())
wldValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wldValue.setStatus(_B)
_Info_ObjectIdentity=ObjectIdentity
info=_Info_ObjectIdentity((1,3,6,1,4,1,21796,4,5,70))
class _InfoAddressMAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_InfoAddressMAC_Type.__name__=_N
_InfoAddressMAC_Object=MibScalar
infoAddressMAC=_InfoAddressMAC_Object((1,3,6,1,4,1,21796,4,5,70,1),_InfoAddressMAC_Type())
infoAddressMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:infoAddressMAC.setStatus(_B)
wldStateToAlarm=NotificationType((1,3,6,1,4,1,21796,4,5,0,1))
wldStateToAlarm.setObjects(*((_E,_F),(_A,_G),(_A,_D),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:wldStateToAlarm.setStatus('')
wldStateToNormal=NotificationType((1,3,6,1,4,1,21796,4,5,0,2))
wldStateToNormal.setObjects(*((_E,_F),(_A,_G),(_A,_D),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:wldStateToNormal.setStatus('')
wldPeriodicAlarm=NotificationType((1,3,6,1,4,1,21796,4,5,0,3))
wldPeriodicAlarm.setObjects(*((_E,_F),(_A,_G),(_A,_D),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:wldPeriodicAlarm.setStatus('')
mibBuilder.exportSymbols(_A,**{'PositiveInteger':PositiveInteger,'SensorState':SensorState,'SensorValue':SensorValue,'SensorSN':SensorSN,'SensorName':SensorName,'SensorID':SensorID,'hwgroup':hwgroup,'x390':x390,'hwgwld':hwgwld,'wldStateToAlarm':wldStateToAlarm,'wldStateToNormal':wldStateToNormal,'wldPeriodicAlarm':wldPeriodicAlarm,'sensTable':sensTable,'wldEntry':wldEntry,_D:wldIndex,_H:wldName,_I:wldState,_J:wldSN,_K:wldID,_L:wldValue,'info':info,_G:infoAddressMAC})