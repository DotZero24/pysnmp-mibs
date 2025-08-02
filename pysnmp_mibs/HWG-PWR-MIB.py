_W='mtIndex'
_V='DisplayString'
_U='NotificationType'
_T='inpAlarmState'
_S='inpValueName'
_R='inpValue'
_Q='inpName'
_P='infoAddressMAC'
_O='mtvalAlarmState'
_N='mtvalTxtValue'
_M='mtvalMbusValue'
_L='mtvalExp'
_K='mtvalTarif'
_J='mtvalUnit'
_I='mtvalName'
_H='sysName'
_G='SNMPv2-MIB'
_F='inpIndex'
_E='mtvalIndex'
_D='read-write'
_C='read-only'
_B='mandatory'
_A='HWG-PWR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_U,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_U,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_V,'PhysAddress','TextualConvention')
class PositiveInteger(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class Txt8(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class Txt16(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class SensorValue(Integer32):0
class SensorID(Integer32):0
class OpenClose(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('open',0),('close',1)))
class AlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('invalid',0),('normal',1),('alarm',2)))
_Hwgroup_ObjectIdentity=ObjectIdentity
hwgroup=_Hwgroup_ObjectIdentity((1,3,6,1,4,1,21796))
_X390_ObjectIdentity=ObjectIdentity
x390=_X390_ObjectIdentity((1,3,6,1,4,1,21796,4))
_Hwgpwr_ObjectIdentity=ObjectIdentity
hwgpwr=_Hwgpwr_ObjectIdentity((1,3,6,1,4,1,21796,4,6))
_Meters_ObjectIdentity=ObjectIdentity
meters=_Meters_ObjectIdentity((1,3,6,1,4,1,21796,4,6,1))
_MtNumber_Type=PositiveInteger
_MtNumber_Object=MibScalar
mtNumber=_MtNumber_Object((1,3,6,1,4,1,21796,4,6,1,1),_MtNumber_Type())
mtNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mtNumber.setStatus(_B)
_MtTableMeters_Object=MibTable
mtTableMeters=_MtTableMeters_Object((1,3,6,1,4,1,21796,4,6,1,2))
if mibBuilder.loadTexts:mtTableMeters.setStatus(_B)
_MtEntry_Object=MibTableRow
mtEntry=_MtEntry_Object((1,3,6,1,4,1,21796,4,6,1,2,1))
mtEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:mtEntry.setStatus(_B)
_MtIndex_Type=PositiveInteger
_MtIndex_Object=MibTableColumn
mtIndex=_MtIndex_Object((1,3,6,1,4,1,21796,4,6,1,2,1,1),_MtIndex_Type())
mtIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mtIndex.setStatus(_B)
_MtName_Type=Txt16
_MtName_Object=MibTableColumn
mtName=_MtName_Object((1,3,6,1,4,1,21796,4,6,1,2,1,2),_MtName_Type())
mtName.setMaxAccess(_D)
if mibBuilder.loadTexts:mtName.setStatus(_B)
_MtAddr_Type=PositiveInteger
_MtAddr_Object=MibTableColumn
mtAddr=_MtAddr_Object((1,3,6,1,4,1,21796,4,6,1,2,1,3),_MtAddr_Type())
mtAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mtAddr.setStatus(_B)
_MtSecAddr_Type=PositiveInteger
_MtSecAddr_Object=MibTableColumn
mtSecAddr=_MtSecAddr_Object((1,3,6,1,4,1,21796,4,6,1,2,1,4),_MtSecAddr_Type())
mtSecAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mtSecAddr.setStatus(_B)
_MtValNumber_Type=PositiveInteger
_MtValNumber_Object=MibTableColumn
mtValNumber=_MtValNumber_Object((1,3,6,1,4,1,21796,4,6,1,2,1,5),_MtValNumber_Type())
mtValNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:mtValNumber.setStatus(_B)
_MtSecAddrTxt_Type=Txt8
_MtSecAddrTxt_Object=MibTableColumn
mtSecAddrTxt=_MtSecAddrTxt_Object((1,3,6,1,4,1,21796,4,6,1,2,1,6),_MtSecAddrTxt_Type())
mtSecAddrTxt.setMaxAccess(_C)
if mibBuilder.loadTexts:mtSecAddrTxt.setStatus(_B)
_MtvalTableValues_Object=MibTable
mtvalTableValues=_MtvalTableValues_Object((1,3,6,1,4,1,21796,4,6,1,3))
if mibBuilder.loadTexts:mtvalTableValues.setStatus(_B)
_MtvalEntry_Object=MibTableRow
mtvalEntry=_MtvalEntry_Object((1,3,6,1,4,1,21796,4,6,1,3,1))
mtvalEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:mtvalEntry.setStatus(_B)
_MtvalIndex_Type=PositiveInteger
_MtvalIndex_Object=MibTableColumn
mtvalIndex=_MtvalIndex_Object((1,3,6,1,4,1,21796,4,6,1,3,1,1),_MtvalIndex_Type())
mtvalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mtvalIndex.setStatus(_B)
_MtvalName_Type=Txt16
_MtvalName_Object=MibTableColumn
mtvalName=_MtvalName_Object((1,3,6,1,4,1,21796,4,6,1,3,1,2),_MtvalName_Type())
mtvalName.setMaxAccess(_D)
if mibBuilder.loadTexts:mtvalName.setStatus(_B)
_MtvalUnit_Type=Txt8
_MtvalUnit_Object=MibTableColumn
mtvalUnit=_MtvalUnit_Object((1,3,6,1,4,1,21796,4,6,1,3,1,3),_MtvalUnit_Type())
mtvalUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:mtvalUnit.setStatus(_B)
_MtvalTarif_Type=PositiveInteger
_MtvalTarif_Object=MibTableColumn
mtvalTarif=_MtvalTarif_Object((1,3,6,1,4,1,21796,4,6,1,3,1,4),_MtvalTarif_Type())
mtvalTarif.setMaxAccess(_C)
if mibBuilder.loadTexts:mtvalTarif.setStatus(_B)
_MtvalExp_Type=PositiveInteger
_MtvalExp_Object=MibTableColumn
mtvalExp=_MtvalExp_Object((1,3,6,1,4,1,21796,4,6,1,3,1,5),_MtvalExp_Type())
mtvalExp.setMaxAccess(_D)
if mibBuilder.loadTexts:mtvalExp.setStatus(_B)
_MtvalMbusValue_Type=PositiveInteger
_MtvalMbusValue_Object=MibTableColumn
mtvalMbusValue=_MtvalMbusValue_Object((1,3,6,1,4,1,21796,4,6,1,3,1,6),_MtvalMbusValue_Type())
mtvalMbusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:mtvalMbusValue.setStatus(_B)
_MtvalTxtValue_Type=Txt8
_MtvalTxtValue_Object=MibTableColumn
mtvalTxtValue=_MtvalTxtValue_Object((1,3,6,1,4,1,21796,4,6,1,3,1,7),_MtvalTxtValue_Type())
mtvalTxtValue.setMaxAccess(_C)
if mibBuilder.loadTexts:mtvalTxtValue.setStatus(_B)
_MtvalAlarmState_Type=AlarmState
_MtvalAlarmState_Object=MibTableColumn
mtvalAlarmState=_MtvalAlarmState_Object((1,3,6,1,4,1,21796,4,6,1,3,1,8),_MtvalAlarmState_Type())
mtvalAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:mtvalAlarmState.setStatus(_B)
_MtvalZeroOffset_Type=Integer32
_MtvalZeroOffset_Object=MibTableColumn
mtvalZeroOffset=_MtvalZeroOffset_Object((1,3,6,1,4,1,21796,4,6,1,3,1,9),_MtvalZeroOffset_Type())
mtvalZeroOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:mtvalZeroOffset.setStatus(_B)
_Input_ObjectIdentity=ObjectIdentity
input=_Input_ObjectIdentity((1,3,6,1,4,1,21796,4,6,2))
_InpNumber_Type=PositiveInteger
_InpNumber_Object=MibScalar
inpNumber=_InpNumber_Object((1,3,6,1,4,1,21796,4,6,2,1),_InpNumber_Type())
inpNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:inpNumber.setStatus(_B)
_InpTable_Object=MibTable
inpTable=_InpTable_Object((1,3,6,1,4,1,21796,4,6,2,2))
if mibBuilder.loadTexts:inpTable.setStatus(_B)
_InpEntry_Object=MibTableRow
inpEntry=_InpEntry_Object((1,3,6,1,4,1,21796,4,6,2,2,1))
inpEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:inpEntry.setStatus(_B)
_InpIndex_Type=PositiveInteger
_InpIndex_Object=MibTableColumn
inpIndex=_InpIndex_Object((1,3,6,1,4,1,21796,4,6,2,2,1,1),_InpIndex_Type())
inpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:inpIndex.setStatus(_B)
_InpName_Type=Txt16
_InpName_Object=MibTableColumn
inpName=_InpName_Object((1,3,6,1,4,1,21796,4,6,2,2,1,2),_InpName_Type())
inpName.setMaxAccess(_D)
if mibBuilder.loadTexts:inpName.setStatus(_B)
_InpValue_Type=OpenClose
_InpValue_Object=MibTableColumn
inpValue=_InpValue_Object((1,3,6,1,4,1,21796,4,6,2,2,1,3),_InpValue_Type())
inpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:inpValue.setStatus(_B)
_InpValueName_Type=Txt8
_InpValueName_Object=MibTableColumn
inpValueName=_InpValueName_Object((1,3,6,1,4,1,21796,4,6,2,2,1,4),_InpValueName_Type())
inpValueName.setMaxAccess(_C)
if mibBuilder.loadTexts:inpValueName.setStatus(_B)
_InpAlarmState_Type=AlarmState
_InpAlarmState_Object=MibTableColumn
inpAlarmState=_InpAlarmState_Object((1,3,6,1,4,1,21796,4,6,2,2,1,5),_InpAlarmState_Type())
inpAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:inpAlarmState.setStatus(_B)
_Info_ObjectIdentity=ObjectIdentity
info=_Info_ObjectIdentity((1,3,6,1,4,1,21796,4,6,70))
class _InfoAddressMAC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_InfoAddressMAC_Type.__name__=_V
_InfoAddressMAC_Object=MibScalar
infoAddressMAC=_InfoAddressMAC_Object((1,3,6,1,4,1,21796,4,6,70,1),_InfoAddressMAC_Type())
infoAddressMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:infoAddressMAC.setStatus(_B)
pwrStateToAlarm=NotificationType((1,3,6,1,4,1,21796,4,6,0,1))
pwrStateToAlarm.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pwrStateToAlarm.setStatus('')
pwrStateToNormal=NotificationType((1,3,6,1,4,1,21796,4,6,0,2))
pwrStateToNormal.setObjects(*((_A,_E),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pwrStateToNormal.setStatus('')
inContactStateToAlarm=NotificationType((1,3,6,1,4,1,21796,4,6,0,3))
inContactStateToAlarm.setObjects(*((_G,_H),(_A,_P),(_A,_F),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:inContactStateToAlarm.setStatus('')
inContactStateToNormal=NotificationType((1,3,6,1,4,1,21796,4,6,0,4))
inContactStateToNormal.setObjects(*((_G,_H),(_A,_P),(_A,_F),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:inContactStateToNormal.setStatus('')
mibBuilder.exportSymbols(_A,**{'PositiveInteger':PositiveInteger,'Txt8':Txt8,'Txt16':Txt16,'SensorValue':SensorValue,'SensorID':SensorID,'OpenClose':OpenClose,'AlarmState':AlarmState,'hwgroup':hwgroup,'x390':x390,'hwgpwr':hwgpwr,'pwrStateToAlarm':pwrStateToAlarm,'pwrStateToNormal':pwrStateToNormal,'inContactStateToAlarm':inContactStateToAlarm,'inContactStateToNormal':inContactStateToNormal,'meters':meters,'mtNumber':mtNumber,'mtTableMeters':mtTableMeters,'mtEntry':mtEntry,_W:mtIndex,'mtName':mtName,'mtAddr':mtAddr,'mtSecAddr':mtSecAddr,'mtValNumber':mtValNumber,'mtSecAddrTxt':mtSecAddrTxt,'mtvalTableValues':mtvalTableValues,'mtvalEntry':mtvalEntry,_E:mtvalIndex,_I:mtvalName,_J:mtvalUnit,_K:mtvalTarif,_L:mtvalExp,_M:mtvalMbusValue,_N:mtvalTxtValue,_O:mtvalAlarmState,'mtvalZeroOffset':mtvalZeroOffset,'input':input,'inpNumber':inpNumber,'inpTable':inpTable,'inpEntry':inpEntry,_F:inpIndex,_Q:inpName,_R:inpValue,_S:inpValueName,_T:inpAlarmState,'info':info,_P:infoAddressMAC})