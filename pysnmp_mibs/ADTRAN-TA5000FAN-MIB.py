_P='critical'
_O='adTA5kMultiFansInAlarm'
_N='ADTRAN-TA5000FAN-MIB'
_M='TruthValue'
_L='Integer32'
_K='adTAeSCUTrapAlarmLevel'
_J='ADTRAN-TAeSCUEXT1-MIB'
_I='read-write'
_H='sysName'
_G='SNMPv2-MIB'
_F='adTrapInformSeqNum'
_E='ADTRAN-GENTRAPINFORM-MIB'
_D='adGenSlotInfoIndex'
_C='ADTRAN-GENSLOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_C,_D)
adTrapInformSeqNum,=mibBuilder.importSymbols(_E,_F)
adIdentity,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adMgmt','adProducts')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_M)
adTa5kFanModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,751))
if mibBuilder.loadTexts:adTa5kFanModuleIdentity.setRevisions(('2014-10-22 21:00','2011-10-28 21:00','2011-06-20 18:00'))
_AdTA5kFanModule_ObjectIdentity=ObjectIdentity
adTA5kFanModule=_AdTA5kFanModule_ObjectIdentity((1,3,6,1,4,1,664,1,751))
_AdTa5kFanModuleEvents_ObjectIdentity=ObjectIdentity
adTa5kFanModuleEvents=_AdTa5kFanModuleEvents_ObjectIdentity((1,3,6,1,4,1,664,1,751,0))
_AdTA5kFanModule19_ObjectIdentity=ObjectIdentity
adTA5kFanModule19=_AdTA5kFanModule19_ObjectIdentity((1,3,6,1,4,1,664,1,860))
_AdTA5kFanmg_ObjectIdentity=ObjectIdentity
adTA5kFanmg=_AdTA5kFanmg_ObjectIdentity((1,3,6,1,4,1,664,2,751))
_AdTA5kFanProvisioning_ObjectIdentity=ObjectIdentity
adTA5kFanProvisioning=_AdTA5kFanProvisioning_ObjectIdentity((1,3,6,1,4,1,664,2,751,1))
_AdTA5kFanProvTable_Object=MibTable
adTA5kFanProvTable=_AdTA5kFanProvTable_Object((1,3,6,1,4,1,664,2,751,1,1))
if mibBuilder.loadTexts:adTA5kFanProvTable.setStatus(_A)
_AdTA5kFanProvEntry_Object=MibTableRow
adTA5kFanProvEntry=_AdTA5kFanProvEntry_Object((1,3,6,1,4,1,664,2,751,1,1,1))
adTA5kFanProvEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adTA5kFanProvEntry.setStatus(_A)
class _AdTA5kFanProvFanSpeedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('max',2)))
_AdTA5kFanProvFanSpeedMode_Type.__name__=_L
_AdTA5kFanProvFanSpeedMode_Object=MibTableColumn
adTA5kFanProvFanSpeedMode=_AdTA5kFanProvFanSpeedMode_Object((1,3,6,1,4,1,664,2,751,1,1,1,1),_AdTA5kFanProvFanSpeedMode_Type())
adTA5kFanProvFanSpeedMode.setMaxAccess(_I)
if mibBuilder.loadTexts:adTA5kFanProvFanSpeedMode.setStatus(_A)
class _AdTA5kFanProvTempThres_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_AdTA5kFanProvTempThres_Type.__name__=_L
_AdTA5kFanProvTempThres_Object=MibTableColumn
adTA5kFanProvTempThres=_AdTA5kFanProvTempThres_Object((1,3,6,1,4,1,664,2,751,1,1,1,2),_AdTA5kFanProvTempThres_Type())
adTA5kFanProvTempThres.setMaxAccess(_I)
if mibBuilder.loadTexts:adTA5kFanProvTempThres.setStatus(_A)
class _AdTA5kFanProvYellowAlarmEnable_Type(TruthValue):defaultValue=1
_AdTA5kFanProvYellowAlarmEnable_Type.__name__=_M
_AdTA5kFanProvYellowAlarmEnable_Object=MibTableColumn
adTA5kFanProvYellowAlarmEnable=_AdTA5kFanProvYellowAlarmEnable_Object((1,3,6,1,4,1,664,2,751,1,1,1,3),_AdTA5kFanProvYellowAlarmEnable_Type())
adTA5kFanProvYellowAlarmEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:adTA5kFanProvYellowAlarmEnable.setStatus(_A)
class _AdTA5kFanProvRedAlarmEnable_Type(TruthValue):defaultValue=1
_AdTA5kFanProvRedAlarmEnable_Type.__name__=_M
_AdTA5kFanProvRedAlarmEnable_Object=MibTableColumn
adTA5kFanProvRedAlarmEnable=_AdTA5kFanProvRedAlarmEnable_Object((1,3,6,1,4,1,664,2,751,1,1,1,4),_AdTA5kFanProvRedAlarmEnable_Type())
adTA5kFanProvRedAlarmEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:adTA5kFanProvRedAlarmEnable.setStatus(_A)
class _AdMultiFanAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6)));namedValues=NamedValues(*(('major',5),(_P,6)))
_AdMultiFanAlarmSeverity_Type.__name__=_L
_AdMultiFanAlarmSeverity_Object=MibTableColumn
adMultiFanAlarmSeverity=_AdMultiFanAlarmSeverity_Object((1,3,6,1,4,1,664,2,751,1,1,1,5),_AdMultiFanAlarmSeverity_Type())
adMultiFanAlarmSeverity.setMaxAccess(_I)
if mibBuilder.loadTexts:adMultiFanAlarmSeverity.setStatus(_A)
class _AdFanTempThreshAlarmSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6)));namedValues=NamedValues(*(('major',5),(_P,6)))
_AdFanTempThreshAlarmSeverity_Type.__name__=_L
_AdFanTempThreshAlarmSeverity_Object=MibTableColumn
adFanTempThreshAlarmSeverity=_AdFanTempThreshAlarmSeverity_Object((1,3,6,1,4,1,664,2,751,1,1,1,6),_AdFanTempThreshAlarmSeverity_Type())
adFanTempThreshAlarmSeverity.setMaxAccess(_I)
if mibBuilder.loadTexts:adFanTempThreshAlarmSeverity.setStatus(_A)
_AdTA5kFanStatus_ObjectIdentity=ObjectIdentity
adTA5kFanStatus=_AdTA5kFanStatus_ObjectIdentity((1,3,6,1,4,1,664,2,751,2))
_AdTA5kFanStatusTable_Object=MibTable
adTA5kFanStatusTable=_AdTA5kFanStatusTable_Object((1,3,6,1,4,1,664,2,751,2,1))
if mibBuilder.loadTexts:adTA5kFanStatusTable.setStatus(_A)
_AdTA5kFanStatusEntry_Object=MibTableRow
adTA5kFanStatusEntry=_AdTA5kFanStatusEntry_Object((1,3,6,1,4,1,664,2,751,2,1,1))
adTA5kFanStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adTA5kFanStatusEntry.setStatus(_A)
_AdTA5kFanStatusFan1Speed_Type=DisplayString
_AdTA5kFanStatusFan1Speed_Object=MibTableColumn
adTA5kFanStatusFan1Speed=_AdTA5kFanStatusFan1Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,1),_AdTA5kFanStatusFan1Speed_Type())
adTA5kFanStatusFan1Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan1Speed.setStatus(_A)
_AdTA5kFanStatusFan2Speed_Type=DisplayString
_AdTA5kFanStatusFan2Speed_Object=MibTableColumn
adTA5kFanStatusFan2Speed=_AdTA5kFanStatusFan2Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,2),_AdTA5kFanStatusFan2Speed_Type())
adTA5kFanStatusFan2Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan2Speed.setStatus(_A)
_AdTA5kFanStatusFan3Speed_Type=DisplayString
_AdTA5kFanStatusFan3Speed_Object=MibTableColumn
adTA5kFanStatusFan3Speed=_AdTA5kFanStatusFan3Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,3),_AdTA5kFanStatusFan3Speed_Type())
adTA5kFanStatusFan3Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan3Speed.setStatus(_A)
_AdTA5kFanStatusFan4Speed_Type=DisplayString
_AdTA5kFanStatusFan4Speed_Object=MibTableColumn
adTA5kFanStatusFan4Speed=_AdTA5kFanStatusFan4Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,4),_AdTA5kFanStatusFan4Speed_Type())
adTA5kFanStatusFan4Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan4Speed.setStatus(_A)
_AdTA5kFanStatusVoltage_Type=DisplayString
_AdTA5kFanStatusVoltage_Object=MibTableColumn
adTA5kFanStatusVoltage=_AdTA5kFanStatusVoltage_Object((1,3,6,1,4,1,664,2,751,2,1,1,5),_AdTA5kFanStatusVoltage_Type())
adTA5kFanStatusVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusVoltage.setStatus(_A)
_AdTA5kFanStatusTemp_Type=DisplayString
_AdTA5kFanStatusTemp_Object=MibTableColumn
adTA5kFanStatusTemp=_AdTA5kFanStatusTemp_Object((1,3,6,1,4,1,664,2,751,2,1,1,6),_AdTA5kFanStatusTemp_Type())
adTA5kFanStatusTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusTemp.setStatus(_A)
_AdTA5kFanStatusVoltageAux_Type=DisplayString
_AdTA5kFanStatusVoltageAux_Object=MibTableColumn
adTA5kFanStatusVoltageAux=_AdTA5kFanStatusVoltageAux_Object((1,3,6,1,4,1,664,2,751,2,1,1,7),_AdTA5kFanStatusVoltageAux_Type())
adTA5kFanStatusVoltageAux.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusVoltageAux.setStatus(_A)
_AdTA5kFanStatusFan5Speed_Type=DisplayString
_AdTA5kFanStatusFan5Speed_Object=MibTableColumn
adTA5kFanStatusFan5Speed=_AdTA5kFanStatusFan5Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,8),_AdTA5kFanStatusFan5Speed_Type())
adTA5kFanStatusFan5Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan5Speed.setStatus(_A)
_AdTA5kFanStatusFan6Speed_Type=DisplayString
_AdTA5kFanStatusFan6Speed_Object=MibTableColumn
adTA5kFanStatusFan6Speed=_AdTA5kFanStatusFan6Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,9),_AdTA5kFanStatusFan6Speed_Type())
adTA5kFanStatusFan6Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan6Speed.setStatus(_A)
_AdTA5kFanStatusFan7Speed_Type=DisplayString
_AdTA5kFanStatusFan7Speed_Object=MibTableColumn
adTA5kFanStatusFan7Speed=_AdTA5kFanStatusFan7Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,10),_AdTA5kFanStatusFan7Speed_Type())
adTA5kFanStatusFan7Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan7Speed.setStatus(_A)
_AdTA5kFanStatusFan8Speed_Type=DisplayString
_AdTA5kFanStatusFan8Speed_Object=MibTableColumn
adTA5kFanStatusFan8Speed=_AdTA5kFanStatusFan8Speed_Object((1,3,6,1,4,1,664,2,751,2,1,1,11),_AdTA5kFanStatusFan8Speed_Type())
adTA5kFanStatusFan8Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kFanStatusFan8Speed.setStatus(_A)
_AdTA5kMultiFansInAlarm_Type=Integer32
_AdTA5kMultiFansInAlarm_Object=MibTableColumn
adTA5kMultiFansInAlarm=_AdTA5kMultiFansInAlarm_Object((1,3,6,1,4,1,664,2,751,2,1,1,12),_AdTA5kMultiFansInAlarm_Type())
adTA5kMultiFansInAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:adTA5kMultiFansInAlarm.setStatus(_A)
adTA5kFanYellowActive=NotificationType((1,3,6,1,4,1,664,1,751,0,1))
adTA5kFanYellowActive.setObjects(*((_E,_F),(_G,_H),(_C,_D)))
if mibBuilder.loadTexts:adTA5kFanYellowActive.setStatus(_A)
adTA5kFanYellowInActive=NotificationType((1,3,6,1,4,1,664,1,751,0,2))
adTA5kFanYellowInActive.setObjects(*((_E,_F),(_G,_H),(_C,_D)))
if mibBuilder.loadTexts:adTA5kFanYellowInActive.setStatus(_A)
adTA5kFanRedActive=NotificationType((1,3,6,1,4,1,664,1,751,0,3))
adTA5kFanRedActive.setObjects(*((_E,_F),(_G,_H),(_C,_D),(_J,_K),(_N,_O)))
if mibBuilder.loadTexts:adTA5kFanRedActive.setStatus(_A)
adTA5kFanRedInActive=NotificationType((1,3,6,1,4,1,664,1,751,0,4))
adTA5kFanRedInActive.setObjects(*((_E,_F),(_G,_H),(_C,_D),(_J,_K),(_N,_O)))
if mibBuilder.loadTexts:adTA5kFanRedInActive.setStatus(_A)
adTA5kFanTempThresExceedActive=NotificationType((1,3,6,1,4,1,664,1,751,0,5))
adTA5kFanTempThresExceedActive.setObjects(*((_E,_F),(_G,_H),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adTA5kFanTempThresExceedActive.setStatus(_A)
adTA5kFanTempThresExceedInactive=NotificationType((1,3,6,1,4,1,664,1,751,0,6))
adTA5kFanTempThresExceedInactive.setObjects(*((_E,_F),(_G,_H),(_C,_D),(_J,_K)))
if mibBuilder.loadTexts:adTA5kFanTempThresExceedInactive.setStatus(_A)
mibBuilder.exportSymbols(_N,**{'adTA5kFanModule':adTA5kFanModule,'adTa5kFanModuleEvents':adTa5kFanModuleEvents,'adTA5kFanYellowActive':adTA5kFanYellowActive,'adTA5kFanYellowInActive':adTA5kFanYellowInActive,'adTA5kFanRedActive':adTA5kFanRedActive,'adTA5kFanRedInActive':adTA5kFanRedInActive,'adTA5kFanTempThresExceedActive':adTA5kFanTempThresExceedActive,'adTA5kFanTempThresExceedInactive':adTA5kFanTempThresExceedInactive,'adTA5kFanModule19':adTA5kFanModule19,'adTA5kFanmg':adTA5kFanmg,'adTA5kFanProvisioning':adTA5kFanProvisioning,'adTA5kFanProvTable':adTA5kFanProvTable,'adTA5kFanProvEntry':adTA5kFanProvEntry,'adTA5kFanProvFanSpeedMode':adTA5kFanProvFanSpeedMode,'adTA5kFanProvTempThres':adTA5kFanProvTempThres,'adTA5kFanProvYellowAlarmEnable':adTA5kFanProvYellowAlarmEnable,'adTA5kFanProvRedAlarmEnable':adTA5kFanProvRedAlarmEnable,'adMultiFanAlarmSeverity':adMultiFanAlarmSeverity,'adFanTempThreshAlarmSeverity':adFanTempThreshAlarmSeverity,'adTA5kFanStatus':adTA5kFanStatus,'adTA5kFanStatusTable':adTA5kFanStatusTable,'adTA5kFanStatusEntry':adTA5kFanStatusEntry,'adTA5kFanStatusFan1Speed':adTA5kFanStatusFan1Speed,'adTA5kFanStatusFan2Speed':adTA5kFanStatusFan2Speed,'adTA5kFanStatusFan3Speed':adTA5kFanStatusFan3Speed,'adTA5kFanStatusFan4Speed':adTA5kFanStatusFan4Speed,'adTA5kFanStatusVoltage':adTA5kFanStatusVoltage,'adTA5kFanStatusTemp':adTA5kFanStatusTemp,'adTA5kFanStatusVoltageAux':adTA5kFanStatusVoltageAux,'adTA5kFanStatusFan5Speed':adTA5kFanStatusFan5Speed,'adTA5kFanStatusFan6Speed':adTA5kFanStatusFan6Speed,'adTA5kFanStatusFan7Speed':adTA5kFanStatusFan7Speed,'adTA5kFanStatusFan8Speed':adTA5kFanStatusFan8Speed,_O:adTA5kMultiFansInAlarm,'adTa5kFanModuleIdentity':adTa5kFanModuleIdentity})