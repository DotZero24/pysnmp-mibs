_I='FanPosition'
_H='FANS-POWER-MIB'
_G='abnormal'
_F='online'
_E='offline'
_D='null'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
class FanPosition(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cabinet-fan-top',1),('trunk-fan-top',2),('trunk-fan-bottom',3)))
class FanStat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
class FanType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('newfan',1),('oldfan',2)))
class PowerType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('oldpower',2),('newpower',3)))
class PowerAvailStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_D,2)))
class PowerOperStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),(_G,1),(_D,2)))
class NewFanStat(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('full-speed',1),('half-speed',2),(_D,3)))
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Fan_ObjectIdentity=ObjectIdentity
fan=_Fan_ObjectIdentity((1,3,6,1,4,1,3902,3,4998))
_FanType_Type=FanType
_FanType_Object=MibScalar
fanType=_FanType_Object((1,3,6,1,4,1,3902,3,4998,1),_FanType_Type())
fanType.setMaxAccess(_B)
if mibBuilder.loadTexts:fanType.setStatus(_A)
_Power_ObjectIdentity=ObjectIdentity
power=_Power_ObjectIdentity((1,3,6,1,4,1,3902,3,4999))
_PowerType_Type=PowerType
_PowerType_Object=MibScalar
powerType=_PowerType_Object((1,3,6,1,4,1,3902,3,4999,1),_PowerType_Type())
powerType.setMaxAccess(_B)
if mibBuilder.loadTexts:powerType.setStatus(_A)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,3902,3,5000))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FansEntry_Object=MibTableRow
fansEntry=_FansEntry_Object((1,3,6,1,4,1,3902,3,5000,1))
fansEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fansEntry.setStatus(_A)
_FansPositon_Type=FanPosition
_FansPositon_Object=MibTableColumn
fansPositon=_FansPositon_Object((1,3,6,1,4,1,3902,3,5000,1,1),_FansPositon_Type())
fansPositon.setMaxAccess(_B)
if mibBuilder.loadTexts:fansPositon.setStatus(_A)
_FansNumber_Type=Integer32
_FansNumber_Object=MibTableColumn
fansNumber=_FansNumber_Object((1,3,6,1,4,1,3902,3,5000,1,2),_FansNumber_Type())
fansNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fansNumber.setStatus(_A)
_FansStatOfFan1_Type=FanStat
_FansStatOfFan1_Object=MibTableColumn
fansStatOfFan1=_FansStatOfFan1_Object((1,3,6,1,4,1,3902,3,5000,1,3),_FansStatOfFan1_Type())
fansStatOfFan1.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan1.setStatus(_A)
_FansStatOfFan2_Type=FanStat
_FansStatOfFan2_Object=MibTableColumn
fansStatOfFan2=_FansStatOfFan2_Object((1,3,6,1,4,1,3902,3,5000,1,4),_FansStatOfFan2_Type())
fansStatOfFan2.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan2.setStatus(_A)
_FansStatOfFan3_Type=FanStat
_FansStatOfFan3_Object=MibTableColumn
fansStatOfFan3=_FansStatOfFan3_Object((1,3,6,1,4,1,3902,3,5000,1,5),_FansStatOfFan3_Type())
fansStatOfFan3.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan3.setStatus(_A)
_FansStatOfFan4_Type=FanStat
_FansStatOfFan4_Object=MibTableColumn
fansStatOfFan4=_FansStatOfFan4_Object((1,3,6,1,4,1,3902,3,5000,1,6),_FansStatOfFan4_Type())
fansStatOfFan4.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan4.setStatus(_A)
_FansStatOfFan5_Type=FanStat
_FansStatOfFan5_Object=MibTableColumn
fansStatOfFan5=_FansStatOfFan5_Object((1,3,6,1,4,1,3902,3,5000,1,7),_FansStatOfFan5_Type())
fansStatOfFan5.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan5.setStatus(_A)
_FansStatOfFan6_Type=FanStat
_FansStatOfFan6_Object=MibTableColumn
fansStatOfFan6=_FansStatOfFan6_Object((1,3,6,1,4,1,3902,3,5000,1,8),_FansStatOfFan6_Type())
fansStatOfFan6.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan6.setStatus(_A)
_FansStatOfFan7_Type=FanStat
_FansStatOfFan7_Object=MibTableColumn
fansStatOfFan7=_FansStatOfFan7_Object((1,3,6,1,4,1,3902,3,5000,1,9),_FansStatOfFan7_Type())
fansStatOfFan7.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan7.setStatus(_A)
_FansStatOfFan8_Type=FanStat
_FansStatOfFan8_Object=MibTableColumn
fansStatOfFan8=_FansStatOfFan8_Object((1,3,6,1,4,1,3902,3,5000,1,10),_FansStatOfFan8_Type())
fansStatOfFan8.setMaxAccess(_B)
if mibBuilder.loadTexts:fansStatOfFan8.setStatus(_A)
_PowerStatInfo_ObjectIdentity=ObjectIdentity
powerStatInfo=_PowerStatInfo_ObjectIdentity((1,3,6,1,4,1,3902,3,5001))
_PowerStatACVoltage_Type=DisplayString
_PowerStatACVoltage_Object=MibScalar
powerStatACVoltage=_PowerStatACVoltage_Object((1,3,6,1,4,1,3902,3,5001,1),_PowerStatACVoltage_Type())
powerStatACVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatACVoltage.setStatus(_A)
_PowerStatACCurrent_Type=DisplayString
_PowerStatACCurrent_Object=MibScalar
powerStatACCurrent=_PowerStatACCurrent_Object((1,3,6,1,4,1,3902,3,5001,2),_PowerStatACCurrent_Type())
powerStatACCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatACCurrent.setStatus(_A)
_PowerStatDCVoltage_Type=DisplayString
_PowerStatDCVoltage_Object=MibScalar
powerStatDCVoltage=_PowerStatDCVoltage_Object((1,3,6,1,4,1,3902,3,5001,3),_PowerStatDCVoltage_Type())
powerStatDCVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatDCVoltage.setStatus(_A)
_PowerStatDCCurrent_Type=DisplayString
_PowerStatDCCurrent_Object=MibScalar
powerStatDCCurrent=_PowerStatDCCurrent_Object((1,3,6,1,4,1,3902,3,5001,4),_PowerStatDCCurrent_Type())
powerStatDCCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatDCCurrent.setStatus(_A)
class _PowerStatACError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PowerStatACError_Type.__name__=_C
_PowerStatACError_Object=MibScalar
powerStatACError=_PowerStatACError_Object((1,3,6,1,4,1,3902,3,5001,5),_PowerStatACError_Type())
powerStatACError.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatACError.setStatus(_A)
class _PowerStatRectifyError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PowerStatRectifyError_Type.__name__=_C
_PowerStatRectifyError_Object=MibScalar
powerStatRectifyError=_PowerStatRectifyError_Object((1,3,6,1,4,1,3902,3,5001,6),_PowerStatRectifyError_Type())
powerStatRectifyError.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatRectifyError.setStatus(_A)
_PowerStatMod1AvailStatus_Type=PowerAvailStatus
_PowerStatMod1AvailStatus_Object=MibScalar
powerStatMod1AvailStatus=_PowerStatMod1AvailStatus_Object((1,3,6,1,4,1,3902,3,5001,7),_PowerStatMod1AvailStatus_Type())
powerStatMod1AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod1AvailStatus.setStatus(_A)
_PowerStatMod2AvailStatus_Type=PowerAvailStatus
_PowerStatMod2AvailStatus_Object=MibScalar
powerStatMod2AvailStatus=_PowerStatMod2AvailStatus_Object((1,3,6,1,4,1,3902,3,5001,8),_PowerStatMod2AvailStatus_Type())
powerStatMod2AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod2AvailStatus.setStatus(_A)
_PowerStatMod3AvailStatus_Type=PowerAvailStatus
_PowerStatMod3AvailStatus_Object=MibScalar
powerStatMod3AvailStatus=_PowerStatMod3AvailStatus_Object((1,3,6,1,4,1,3902,3,5001,9),_PowerStatMod3AvailStatus_Type())
powerStatMod3AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod3AvailStatus.setStatus(_A)
_PowerStatMod1OperStatus_Type=PowerOperStatus
_PowerStatMod1OperStatus_Object=MibScalar
powerStatMod1OperStatus=_PowerStatMod1OperStatus_Object((1,3,6,1,4,1,3902,3,5001,10),_PowerStatMod1OperStatus_Type())
powerStatMod1OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod1OperStatus.setStatus(_A)
_PowerStatMod2OperStatus_Type=PowerOperStatus
_PowerStatMod2OperStatus_Object=MibScalar
powerStatMod2OperStatus=_PowerStatMod2OperStatus_Object((1,3,6,1,4,1,3902,3,5001,11),_PowerStatMod2OperStatus_Type())
powerStatMod2OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod2OperStatus.setStatus(_A)
_PowerStatMod3OperStatus_Type=PowerOperStatus
_PowerStatMod3OperStatus_Object=MibScalar
powerStatMod3OperStatus=_PowerStatMod3OperStatus_Object((1,3,6,1,4,1,3902,3,5001,12),_PowerStatMod3OperStatus_Type())
powerStatMod3OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerStatMod3OperStatus.setStatus(_A)
_NewFanStatInfo_ObjectIdentity=ObjectIdentity
newFanStatInfo=_NewFanStatInfo_ObjectIdentity((1,3,6,1,4,1,3902,3,5002))
_NewFanTopFanStatus_Type=NewFanStat
_NewFanTopFanStatus_Object=MibScalar
newFanTopFanStatus=_NewFanTopFanStatus_Object((1,3,6,1,4,1,3902,3,5002,1),_NewFanTopFanStatus_Type())
newFanTopFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newFanTopFanStatus.setStatus(_A)
_NewFanBottomFanStatus_Type=NewFanStat
_NewFanBottomFanStatus_Object=MibScalar
newFanBottomFanStatus=_NewFanBottomFanStatus_Object((1,3,6,1,4,1,3902,3,5002,2),_NewFanBottomFanStatus_Type())
newFanBottomFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newFanBottomFanStatus.setStatus(_A)
_NewPowerStatInfo_ObjectIdentity=ObjectIdentity
newPowerStatInfo=_NewPowerStatInfo_ObjectIdentity((1,3,6,1,4,1,3902,3,5003))
_NewPowerStatMod1AvailStatus_Type=PowerAvailStatus
_NewPowerStatMod1AvailStatus_Object=MibScalar
newPowerStatMod1AvailStatus=_NewPowerStatMod1AvailStatus_Object((1,3,6,1,4,1,3902,3,5003,1),_NewPowerStatMod1AvailStatus_Type())
newPowerStatMod1AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod1AvailStatus.setStatus(_A)
_NewPowerStatMod2AvailStatus_Type=PowerAvailStatus
_NewPowerStatMod2AvailStatus_Object=MibScalar
newPowerStatMod2AvailStatus=_NewPowerStatMod2AvailStatus_Object((1,3,6,1,4,1,3902,3,5003,2),_NewPowerStatMod2AvailStatus_Type())
newPowerStatMod2AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod2AvailStatus.setStatus(_A)
_NewPowerStatMod3AvailStatus_Type=PowerAvailStatus
_NewPowerStatMod3AvailStatus_Object=MibScalar
newPowerStatMod3AvailStatus=_NewPowerStatMod3AvailStatus_Object((1,3,6,1,4,1,3902,3,5003,3),_NewPowerStatMod3AvailStatus_Type())
newPowerStatMod3AvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod3AvailStatus.setStatus(_A)
_NewPowerStatMod1OperStatus_Type=PowerOperStatus
_NewPowerStatMod1OperStatus_Object=MibScalar
newPowerStatMod1OperStatus=_NewPowerStatMod1OperStatus_Object((1,3,6,1,4,1,3902,3,5003,4),_NewPowerStatMod1OperStatus_Type())
newPowerStatMod1OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod1OperStatus.setStatus(_A)
_NewPowerStatMod2OperStatus_Type=PowerOperStatus
_NewPowerStatMod2OperStatus_Object=MibScalar
newPowerStatMod2OperStatus=_NewPowerStatMod2OperStatus_Object((1,3,6,1,4,1,3902,3,5003,5),_NewPowerStatMod2OperStatus_Type())
newPowerStatMod2OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod2OperStatus.setStatus(_A)
_NewPowerStatMod3OperStatus_Type=PowerOperStatus
_NewPowerStatMod3OperStatus_Object=MibScalar
newPowerStatMod3OperStatus=_NewPowerStatMod3OperStatus_Object((1,3,6,1,4,1,3902,3,5003,6),_NewPowerStatMod3OperStatus_Type())
newPowerStatMod3OperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:newPowerStatMod3OperStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_I:FanPosition,'FanStat':FanStat,'FanType':FanType,'PowerType':PowerType,'PowerAvailStatus':PowerAvailStatus,'PowerOperStatus':PowerOperStatus,'NewFanStat':NewFanStat,_C:DisplayString,'zte':zte,'zxr10':zxr10,'fan':fan,'fanType':fanType,'power':power,'powerType':powerType,'fanTable':fanTable,'fansEntry':fansEntry,'fansPositon':fansPositon,'fansNumber':fansNumber,'fansStatOfFan1':fansStatOfFan1,'fansStatOfFan2':fansStatOfFan2,'fansStatOfFan3':fansStatOfFan3,'fansStatOfFan4':fansStatOfFan4,'fansStatOfFan5':fansStatOfFan5,'fansStatOfFan6':fansStatOfFan6,'fansStatOfFan7':fansStatOfFan7,'fansStatOfFan8':fansStatOfFan8,'powerStatInfo':powerStatInfo,'powerStatACVoltage':powerStatACVoltage,'powerStatACCurrent':powerStatACCurrent,'powerStatDCVoltage':powerStatDCVoltage,'powerStatDCCurrent':powerStatDCCurrent,'powerStatACError':powerStatACError,'powerStatRectifyError':powerStatRectifyError,'powerStatMod1AvailStatus':powerStatMod1AvailStatus,'powerStatMod2AvailStatus':powerStatMod2AvailStatus,'powerStatMod3AvailStatus':powerStatMod3AvailStatus,'powerStatMod1OperStatus':powerStatMod1OperStatus,'powerStatMod2OperStatus':powerStatMod2OperStatus,'powerStatMod3OperStatus':powerStatMod3OperStatus,'newFanStatInfo':newFanStatInfo,'newFanTopFanStatus':newFanTopFanStatus,'newFanBottomFanStatus':newFanBottomFanStatus,'newPowerStatInfo':newPowerStatInfo,'newPowerStatMod1AvailStatus':newPowerStatMod1AvailStatus,'newPowerStatMod2AvailStatus':newPowerStatMod2AvailStatus,'newPowerStatMod3AvailStatus':newPowerStatMod3AvailStatus,'newPowerStatMod1OperStatus':newPowerStatMod1OperStatus,'newPowerStatMod2OperStatus':newPowerStatMod2OperStatus,'newPowerStatMod3OperStatus':newPowerStatMod3OperStatus})