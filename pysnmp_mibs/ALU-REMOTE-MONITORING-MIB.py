_AH='aluRMNotificationGroup'
_AG='aluRMGroup'
_AF='aluRMOperStateUpdate'
_AE='aluRMClearingAlarm'
_AD='aluRMWarningAlarm'
_AC='aluRMMinorAlarm'
_AB='aluRMMajorAlarm'
_AA='aluRMCriticalAlarm'
_A9='aluRMTriggerRowStatus'
_A8='aluRMTriggerDigitalNorm'
_A7='aluRMAlarmTHAnalogLevel'
_A6='aluRMAlarmTHAnalogLevelOperation'
_A5='aluRMAlarmAuxRelay'
_A4='aluRMAlarmActionAuxRelay'
_A3='aluRMAlarmActionAlarmRelay'
_A2='aluRMAlarmActionLog'
_A1='aluRMAlarmSeverity'
_A0='aluRMAlarmTrigger8'
_z='aluRMAlarmTrigger7'
_y='aluRMAlarmTrigger6'
_x='aluRMAlarmTrigger5'
_w='aluRMAlarmTrigger4'
_v='aluRMAlarmTrigger3'
_u='aluRMAlarmTrigger2'
_t='aluRMAlarmTrigger1'
_s='aluRMAlarmTriggerRule'
_r='aluRMAlarmDescription'
_q='aluRMAlarmOperStatus'
_p='aluRMAlarmAdminStatus'
_o='aluRMAlarmRowStatus'
_n='aluRMRelayAlias'
_m='aluRMRelayDescription'
_l='aluRMRelayOperStatus'
_k='aluRMRelayAdminStatus'
_j='aluRMRelayMode'
_i='aluRMRelayName'
_h='aluRMTriggerAlias'
_g='aluRMTriggerDigitalState'
_f='aluRMTriggerAnalogVoltage'
_e='aluRMTriggerClearDebounce'
_d='aluRMTriggerDetectDebounce'
_c='aluRMTriggerDescription'
_b='aluRMTriggerOperStatus'
_a='aluRMTriggerAdminStatus'
_Z='aluRMTriggerName'
_Y='aluRMAlarmID'
_X='aluRMRelayID'
_W='seconds'
_V='aluRMTriggerID'
_U='not-monitored'
_T='aluRMNotifyOperState'
_S='aluRMNotifyID'
_R='not-accessible'
_Q='accessible-for-notify'
_P='AluRMAdminStatus'
_O='unknown'
_N='TItemLongDescription'
_M='tmnxChassisIndex'
_L='TIMETRA-CHASSIS-MIB'
_K='TruthValue'
_J='Unsigned32'
_I='aluRMAlarmNotifyDescription'
_H='aluRMAlarmNotifyID'
_G='aluRMAlarmDetectedTriggers'
_F='read-only'
_E='Integer32'
_D='read-write'
_C='read-create'
_B='current'
_A='ALU-REMOTE-MONITORING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_K)
tmnxChassisIndex,=mibBuilder.importSymbols(_L,_M)
TItemLongDescription,TNamedItemOrEmpty=mibBuilder.importSymbols('TIMETRA-TC-MIB',_N,'TNamedItemOrEmpty')
aluRMMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,11))
if mibBuilder.loadTexts:aluRMMIBModule.setRevisions(('1908-01-09 00:00','1921-01-11 00:00','1921-01-21 00:00'))
class AluRMAlias(DisplayString):status=_B;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
class AluRMExtAlarmID(TextualConvention,Unsigned32):status=_B
class AluRMAdminStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('disabled',1),('enabled',2)))
class AluRMOperStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_O,0),('ghost',1),(_U,2),('ok',3),('active',4)))
_AluRMMIBConformance_ObjectIdentity=ObjectIdentity
aluRMMIBConformance=_AluRMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,11))
_AluRMConformance_ObjectIdentity=ObjectIdentity
aluRMConformance=_AluRMConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,11,11))
_AluRMCompliances_ObjectIdentity=ObjectIdentity
aluRMCompliances=_AluRMCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,11,11,1))
_AluRMComp7705_ObjectIdentity=ObjectIdentity
aluRMComp7705=_AluRMComp7705_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,11,11,1,1))
_AluRMGroups_ObjectIdentity=ObjectIdentity
aluRMGroups=_AluRMGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,11,11,2))
_AluRMObjPrefix_ObjectIdentity=ObjectIdentity
aluRMObjPrefix=_AluRMObjPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,11))
_AluRMObjs_ObjectIdentity=ObjectIdentity
aluRMObjs=_AluRMObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,11,1))
_AluRMTriggerTable_Object=MibTable
aluRMTriggerTable=_AluRMTriggerTable_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1))
if mibBuilder.loadTexts:aluRMTriggerTable.setStatus(_B)
_AluRMTriggerEntry_Object=MibTableRow
aluRMTriggerEntry=_AluRMTriggerEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1))
aluRMTriggerEntry.setIndexNames((0,_L,_M),(0,_A,_V))
if mibBuilder.loadTexts:aluRMTriggerEntry.setStatus(_B)
_AluRMTriggerID_Type=AluRMExtAlarmID
_AluRMTriggerID_Object=MibTableColumn
aluRMTriggerID=_AluRMTriggerID_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,1),_AluRMTriggerID_Type())
aluRMTriggerID.setMaxAccess(_R)
if mibBuilder.loadTexts:aluRMTriggerID.setStatus(_B)
_AluRMTriggerName_Type=TNamedItemOrEmpty
_AluRMTriggerName_Object=MibTableColumn
aluRMTriggerName=_AluRMTriggerName_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,2),_AluRMTriggerName_Type())
aluRMTriggerName.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMTriggerName.setStatus(_B)
class _AluRMTriggerAdminStatus_Type(AluRMAdminStatus):defaultValue=2
_AluRMTriggerAdminStatus_Type.__name__=_P
_AluRMTriggerAdminStatus_Object=MibTableColumn
aluRMTriggerAdminStatus=_AluRMTriggerAdminStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,3),_AluRMTriggerAdminStatus_Type())
aluRMTriggerAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerAdminStatus.setStatus(_B)
_AluRMTriggerOperStatus_Type=AluRMOperStatus
_AluRMTriggerOperStatus_Object=MibTableColumn
aluRMTriggerOperStatus=_AluRMTriggerOperStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,4),_AluRMTriggerOperStatus_Type())
aluRMTriggerOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMTriggerOperStatus.setStatus(_B)
class _AluRMTriggerDescription_Type(TItemLongDescription):defaultHexValue=''
_AluRMTriggerDescription_Type.__name__=_N
_AluRMTriggerDescription_Object=MibTableColumn
aluRMTriggerDescription=_AluRMTriggerDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,5),_AluRMTriggerDescription_Type())
aluRMTriggerDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerDescription.setStatus(_B)
class _AluRMTriggerDetectDebounce_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AluRMTriggerDetectDebounce_Type.__name__=_J
_AluRMTriggerDetectDebounce_Object=MibTableColumn
aluRMTriggerDetectDebounce=_AluRMTriggerDetectDebounce_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,6),_AluRMTriggerDetectDebounce_Type())
aluRMTriggerDetectDebounce.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerDetectDebounce.setStatus(_B)
if mibBuilder.loadTexts:aluRMTriggerDetectDebounce.setUnits(_W)
class _AluRMTriggerClearDebounce_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AluRMTriggerClearDebounce_Type.__name__=_J
_AluRMTriggerClearDebounce_Object=MibTableColumn
aluRMTriggerClearDebounce=_AluRMTriggerClearDebounce_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,7),_AluRMTriggerClearDebounce_Type())
aluRMTriggerClearDebounce.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerClearDebounce.setStatus(_B)
if mibBuilder.loadTexts:aluRMTriggerClearDebounce.setUnits(_W)
_AluRMTriggerAnalogVoltage_Type=Integer32
_AluRMTriggerAnalogVoltage_Object=MibTableColumn
aluRMTriggerAnalogVoltage=_AluRMTriggerAnalogVoltage_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,8),_AluRMTriggerAnalogVoltage_Type())
aluRMTriggerAnalogVoltage.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMTriggerAnalogVoltage.setStatus(_B)
if mibBuilder.loadTexts:aluRMTriggerAnalogVoltage.setUnits('millivoltage')
class _AluRMTriggerDigitalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('closed',1),('open',2)))
_AluRMTriggerDigitalState_Type.__name__=_E
_AluRMTriggerDigitalState_Object=MibTableColumn
aluRMTriggerDigitalState=_AluRMTriggerDigitalState_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,9),_AluRMTriggerDigitalState_Type())
aluRMTriggerDigitalState.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMTriggerDigitalState.setStatus(_B)
_AluRMTriggerAlias_Type=AluRMAlias
_AluRMTriggerAlias_Object=MibTableColumn
aluRMTriggerAlias=_AluRMTriggerAlias_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,10),_AluRMTriggerAlias_Type())
aluRMTriggerAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerAlias.setStatus(_B)
class _AluRMTriggerDigitalNorm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('normally-closed',1),('normally-open',2)))
_AluRMTriggerDigitalNorm_Type.__name__=_E
_AluRMTriggerDigitalNorm_Object=MibTableColumn
aluRMTriggerDigitalNorm=_AluRMTriggerDigitalNorm_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,11),_AluRMTriggerDigitalNorm_Type())
aluRMTriggerDigitalNorm.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerDigitalNorm.setStatus(_B)
_AluRMTriggerRowStatus_Type=RowStatus
_AluRMTriggerRowStatus_Object=MibTableColumn
aluRMTriggerRowStatus=_AluRMTriggerRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,1,1,12),_AluRMTriggerRowStatus_Type())
aluRMTriggerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMTriggerRowStatus.setStatus(_B)
_AluRMRelayTable_Object=MibTable
aluRMRelayTable=_AluRMRelayTable_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2))
if mibBuilder.loadTexts:aluRMRelayTable.setStatus(_B)
_AluRMRelayEntry_Object=MibTableRow
aluRMRelayEntry=_AluRMRelayEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1))
aluRMRelayEntry.setIndexNames((0,_L,_M),(0,_A,_X))
if mibBuilder.loadTexts:aluRMRelayEntry.setStatus(_B)
_AluRMRelayID_Type=AluRMExtAlarmID
_AluRMRelayID_Object=MibTableColumn
aluRMRelayID=_AluRMRelayID_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,1),_AluRMRelayID_Type())
aluRMRelayID.setMaxAccess(_R)
if mibBuilder.loadTexts:aluRMRelayID.setStatus(_B)
_AluRMRelayName_Type=TNamedItemOrEmpty
_AluRMRelayName_Object=MibTableColumn
aluRMRelayName=_AluRMRelayName_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,2),_AluRMRelayName_Type())
aluRMRelayName.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMRelayName.setStatus(_B)
class _AluRMRelayMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('continuous',1),('triggered',2)))
_AluRMRelayMode_Type.__name__=_E
_AluRMRelayMode_Object=MibTableColumn
aluRMRelayMode=_AluRMRelayMode_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,3),_AluRMRelayMode_Type())
aluRMRelayMode.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMRelayMode.setStatus(_B)
class _AluRMRelayAdminStatus_Type(AluRMAdminStatus):defaultValue=2
_AluRMRelayAdminStatus_Type.__name__=_P
_AluRMRelayAdminStatus_Object=MibTableColumn
aluRMRelayAdminStatus=_AluRMRelayAdminStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,4),_AluRMRelayAdminStatus_Type())
aluRMRelayAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMRelayAdminStatus.setStatus(_B)
_AluRMRelayOperStatus_Type=AluRMOperStatus
_AluRMRelayOperStatus_Object=MibTableColumn
aluRMRelayOperStatus=_AluRMRelayOperStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,5),_AluRMRelayOperStatus_Type())
aluRMRelayOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMRelayOperStatus.setStatus(_B)
class _AluRMRelayDescription_Type(TItemLongDescription):defaultHexValue=''
_AluRMRelayDescription_Type.__name__=_N
_AluRMRelayDescription_Object=MibTableColumn
aluRMRelayDescription=_AluRMRelayDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,6),_AluRMRelayDescription_Type())
aluRMRelayDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMRelayDescription.setStatus(_B)
_AluRMRelayAlias_Type=AluRMAlias
_AluRMRelayAlias_Object=MibTableColumn
aluRMRelayAlias=_AluRMRelayAlias_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,2,1,7),_AluRMRelayAlias_Type())
aluRMRelayAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:aluRMRelayAlias.setStatus(_B)
_AluRMAlarmTable_Object=MibTable
aluRMAlarmTable=_AluRMAlarmTable_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3))
if mibBuilder.loadTexts:aluRMAlarmTable.setStatus(_B)
_AluRMAlarmEntry_Object=MibTableRow
aluRMAlarmEntry=_AluRMAlarmEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1))
aluRMAlarmEntry.setIndexNames((0,_L,_M),(0,_A,_Y))
if mibBuilder.loadTexts:aluRMAlarmEntry.setStatus(_B)
class _AluRMAlarmID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AluRMAlarmID_Type.__name__=_J
_AluRMAlarmID_Object=MibTableColumn
aluRMAlarmID=_AluRMAlarmID_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,1),_AluRMAlarmID_Type())
aluRMAlarmID.setMaxAccess(_R)
if mibBuilder.loadTexts:aluRMAlarmID.setStatus(_B)
_AluRMAlarmRowStatus_Type=RowStatus
_AluRMAlarmRowStatus_Object=MibTableColumn
aluRMAlarmRowStatus=_AluRMAlarmRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,2),_AluRMAlarmRowStatus_Type())
aluRMAlarmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmRowStatus.setStatus(_B)
class _AluRMAlarmAdminStatus_Type(AluRMAdminStatus):defaultValue=1
_AluRMAlarmAdminStatus_Type.__name__=_P
_AluRMAlarmAdminStatus_Object=MibTableColumn
aluRMAlarmAdminStatus=_AluRMAlarmAdminStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,3),_AluRMAlarmAdminStatus_Type())
aluRMAlarmAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmAdminStatus.setStatus(_B)
_AluRMAlarmOperStatus_Type=AluRMOperStatus
_AluRMAlarmOperStatus_Object=MibTableColumn
aluRMAlarmOperStatus=_AluRMAlarmOperStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,4),_AluRMAlarmOperStatus_Type())
aluRMAlarmOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMAlarmOperStatus.setStatus(_B)
class _AluRMAlarmDescription_Type(TItemLongDescription):defaultHexValue=''
_AluRMAlarmDescription_Type.__name__=_N
_AluRMAlarmDescription_Object=MibTableColumn
aluRMAlarmDescription=_AluRMAlarmDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,5),_AluRMAlarmDescription_Type())
aluRMAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmDescription.setStatus(_B)
class _AluRMAlarmTriggerRule_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('any-trigger',1),('all-triggers',2)))
_AluRMAlarmTriggerRule_Type.__name__=_E
_AluRMAlarmTriggerRule_Object=MibTableColumn
aluRMAlarmTriggerRule=_AluRMAlarmTriggerRule_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,6),_AluRMAlarmTriggerRule_Type())
aluRMAlarmTriggerRule.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTriggerRule.setStatus(_B)
_AluRMAlarmTrigger1_Type=AluRMExtAlarmID
_AluRMAlarmTrigger1_Object=MibTableColumn
aluRMAlarmTrigger1=_AluRMAlarmTrigger1_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,7),_AluRMAlarmTrigger1_Type())
aluRMAlarmTrigger1.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger1.setStatus(_B)
_AluRMAlarmTrigger2_Type=AluRMExtAlarmID
_AluRMAlarmTrigger2_Object=MibTableColumn
aluRMAlarmTrigger2=_AluRMAlarmTrigger2_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,8),_AluRMAlarmTrigger2_Type())
aluRMAlarmTrigger2.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger2.setStatus(_B)
_AluRMAlarmTrigger3_Type=AluRMExtAlarmID
_AluRMAlarmTrigger3_Object=MibTableColumn
aluRMAlarmTrigger3=_AluRMAlarmTrigger3_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,9),_AluRMAlarmTrigger3_Type())
aluRMAlarmTrigger3.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger3.setStatus(_B)
_AluRMAlarmTrigger4_Type=AluRMExtAlarmID
_AluRMAlarmTrigger4_Object=MibTableColumn
aluRMAlarmTrigger4=_AluRMAlarmTrigger4_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,10),_AluRMAlarmTrigger4_Type())
aluRMAlarmTrigger4.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger4.setStatus(_B)
_AluRMAlarmTrigger5_Type=AluRMExtAlarmID
_AluRMAlarmTrigger5_Object=MibTableColumn
aluRMAlarmTrigger5=_AluRMAlarmTrigger5_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,11),_AluRMAlarmTrigger5_Type())
aluRMAlarmTrigger5.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger5.setStatus(_B)
_AluRMAlarmTrigger6_Type=AluRMExtAlarmID
_AluRMAlarmTrigger6_Object=MibTableColumn
aluRMAlarmTrigger6=_AluRMAlarmTrigger6_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,12),_AluRMAlarmTrigger6_Type())
aluRMAlarmTrigger6.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger6.setStatus(_B)
_AluRMAlarmTrigger7_Type=AluRMExtAlarmID
_AluRMAlarmTrigger7_Object=MibTableColumn
aluRMAlarmTrigger7=_AluRMAlarmTrigger7_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,13),_AluRMAlarmTrigger7_Type())
aluRMAlarmTrigger7.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger7.setStatus(_B)
_AluRMAlarmTrigger8_Type=AluRMExtAlarmID
_AluRMAlarmTrigger8_Object=MibTableColumn
aluRMAlarmTrigger8=_AluRMAlarmTrigger8_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,14),_AluRMAlarmTrigger8_Type())
aluRMAlarmTrigger8.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTrigger8.setStatus(_B)
class _AluRMAlarmSeverity_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('critical',3),('major',4),('minor',5),('warning',6)))
_AluRMAlarmSeverity_Type.__name__=_E
_AluRMAlarmSeverity_Object=MibTableColumn
aluRMAlarmSeverity=_AluRMAlarmSeverity_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,15),_AluRMAlarmSeverity_Type())
aluRMAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmSeverity.setStatus(_B)
class _AluRMAlarmActionLog_Type(TruthValue):defaultValue=1
_AluRMAlarmActionLog_Type.__name__=_K
_AluRMAlarmActionLog_Object=MibTableColumn
aluRMAlarmActionLog=_AluRMAlarmActionLog_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,16),_AluRMAlarmActionLog_Type())
aluRMAlarmActionLog.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmActionLog.setStatus(_B)
class _AluRMAlarmActionAlarmRelay_Type(TruthValue):defaultValue=1
_AluRMAlarmActionAlarmRelay_Type.__name__=_K
_AluRMAlarmActionAlarmRelay_Object=MibTableColumn
aluRMAlarmActionAlarmRelay=_AluRMAlarmActionAlarmRelay_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,17),_AluRMAlarmActionAlarmRelay_Type())
aluRMAlarmActionAlarmRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmActionAlarmRelay.setStatus(_B)
class _AluRMAlarmActionAuxRelay_Type(TruthValue):defaultValue=2
_AluRMAlarmActionAuxRelay_Type.__name__=_K
_AluRMAlarmActionAuxRelay_Object=MibTableColumn
aluRMAlarmActionAuxRelay=_AluRMAlarmActionAuxRelay_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,18),_AluRMAlarmActionAuxRelay_Type())
aluRMAlarmActionAuxRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmActionAuxRelay.setStatus(_B)
_AluRMAlarmAuxRelay_Type=AluRMExtAlarmID
_AluRMAlarmAuxRelay_Object=MibTableColumn
aluRMAlarmAuxRelay=_AluRMAlarmAuxRelay_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,19),_AluRMAlarmAuxRelay_Type())
aluRMAlarmAuxRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmAuxRelay.setStatus(_B)
_AluRMAlarmDetectedTriggers_Type=Unsigned32
_AluRMAlarmDetectedTriggers_Object=MibTableColumn
aluRMAlarmDetectedTriggers=_AluRMAlarmDetectedTriggers_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,20),_AluRMAlarmDetectedTriggers_Type())
aluRMAlarmDetectedTriggers.setMaxAccess(_F)
if mibBuilder.loadTexts:aluRMAlarmDetectedTriggers.setStatus(_B)
class _AluRMAlarmTHAnalogLevelOperation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),('greater-than',1),('less-than',2)))
_AluRMAlarmTHAnalogLevelOperation_Type.__name__=_E
_AluRMAlarmTHAnalogLevelOperation_Object=MibTableColumn
aluRMAlarmTHAnalogLevelOperation=_AluRMAlarmTHAnalogLevelOperation_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,21),_AluRMAlarmTHAnalogLevelOperation_Type())
aluRMAlarmTHAnalogLevelOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTHAnalogLevelOperation.setStatus(_B)
class _AluRMAlarmTHAnalogLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,75000))
_AluRMAlarmTHAnalogLevel_Type.__name__=_E
_AluRMAlarmTHAnalogLevel_Object=MibTableColumn
aluRMAlarmTHAnalogLevel=_AluRMAlarmTHAnalogLevel_Object((1,3,6,1,4,1,6527,6,1,2,2,11,1,3,1,22),_AluRMAlarmTHAnalogLevel_Type())
aluRMAlarmTHAnalogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:aluRMAlarmTHAnalogLevel.setStatus(_B)
if mibBuilder.loadTexts:aluRMAlarmTHAnalogLevel.setUnits('millivolts')
_AluRMNotifyObjs_ObjectIdentity=ObjectIdentity
aluRMNotifyObjs=_AluRMNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,11,2))
_AluRMAlarmNotifyID_Type=Unsigned32
_AluRMAlarmNotifyID_Object=MibScalar
aluRMAlarmNotifyID=_AluRMAlarmNotifyID_Object((1,3,6,1,4,1,6527,6,1,2,2,11,2,1),_AluRMAlarmNotifyID_Type())
aluRMAlarmNotifyID.setMaxAccess(_Q)
if mibBuilder.loadTexts:aluRMAlarmNotifyID.setStatus(_B)
_AluRMAlarmNotifyDescription_Type=TItemLongDescription
_AluRMAlarmNotifyDescription_Object=MibScalar
aluRMAlarmNotifyDescription=_AluRMAlarmNotifyDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,11,2,2),_AluRMAlarmNotifyDescription_Type())
aluRMAlarmNotifyDescription.setMaxAccess(_Q)
if mibBuilder.loadTexts:aluRMAlarmNotifyDescription.setStatus(_B)
_AluRMNotifyID_Type=AluRMExtAlarmID
_AluRMNotifyID_Object=MibScalar
aluRMNotifyID=_AluRMNotifyID_Object((1,3,6,1,4,1,6527,6,1,2,2,11,2,3),_AluRMNotifyID_Type())
aluRMNotifyID.setMaxAccess(_Q)
if mibBuilder.loadTexts:aluRMNotifyID.setStatus(_B)
_AluRMNotifyOperState_Type=AluRMOperStatus
_AluRMNotifyOperState_Object=MibScalar
aluRMNotifyOperState=_AluRMNotifyOperState_Object((1,3,6,1,4,1,6527,6,1,2,2,11,2,4),_AluRMNotifyOperState_Type())
aluRMNotifyOperState.setMaxAccess(_Q)
if mibBuilder.loadTexts:aluRMNotifyOperState.setStatus(_B)
_AluRMNotifyPrefix_ObjectIdentity=ObjectIdentity
aluRMNotifyPrefix=_AluRMNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,7))
_AluRMNotification_ObjectIdentity=ObjectIdentity
aluRMNotification=_AluRMNotification_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,7,0))
aluRMGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,11,11,2,1))
aluRMGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_G),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:aluRMGroup.setStatus(_B)
aluRMNotificationObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,11,11,2,3))
aluRMNotificationObjsGroup.setObjects(*((_A,_H),(_A,_I),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:aluRMNotificationObjsGroup.setStatus(_B)
aluRMDigitalGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,11,11,2,4))
aluRMDigitalGroup.setObjects((_A,_A8))
if mibBuilder.loadTexts:aluRMDigitalGroup.setStatus(_B)
aluRMAuxTriggerGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,11,11,2,5))
aluRMAuxTriggerGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:aluRMAuxTriggerGroup.setStatus(_B)
aluRMCriticalAlarm=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,1))
aluRMCriticalAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:aluRMCriticalAlarm.setStatus(_B)
aluRMMajorAlarm=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,2))
aluRMMajorAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:aluRMMajorAlarm.setStatus(_B)
aluRMMinorAlarm=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,3))
aluRMMinorAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:aluRMMinorAlarm.setStatus(_B)
aluRMWarningAlarm=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,4))
aluRMWarningAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:aluRMWarningAlarm.setStatus(_B)
aluRMClearingAlarm=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,5))
aluRMClearingAlarm.setObjects(*((_A,_H),(_A,_I),(_A,_G)))
if mibBuilder.loadTexts:aluRMClearingAlarm.setStatus(_B)
aluRMOperStateUpdate=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,7,0,6))
aluRMOperStateUpdate.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:aluRMOperStateUpdate.setStatus(_B)
aluRMNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,6,1,2,1,11,11,2,2))
aluRMNotificationGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:aluRMNotificationGroup.setStatus(_B)
aluRMComp7705V1v0=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,11,11,1,1,1))
aluRMComp7705V1v0.setObjects(*((_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:aluRMComp7705V1v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AluRMAlias':AluRMAlias,'AluRMExtAlarmID':AluRMExtAlarmID,_P:AluRMAdminStatus,'AluRMOperStatus':AluRMOperStatus,'aluRMMIBModule':aluRMMIBModule,'aluRMMIBConformance':aluRMMIBConformance,'aluRMConformance':aluRMConformance,'aluRMCompliances':aluRMCompliances,'aluRMComp7705':aluRMComp7705,'aluRMComp7705V1v0':aluRMComp7705V1v0,'aluRMGroups':aluRMGroups,_AG:aluRMGroup,_AH:aluRMNotificationGroup,'aluRMNotificationObjsGroup':aluRMNotificationObjsGroup,'aluRMDigitalGroup':aluRMDigitalGroup,'aluRMAuxTriggerGroup':aluRMAuxTriggerGroup,'aluRMObjPrefix':aluRMObjPrefix,'aluRMObjs':aluRMObjs,'aluRMTriggerTable':aluRMTriggerTable,'aluRMTriggerEntry':aluRMTriggerEntry,_V:aluRMTriggerID,_Z:aluRMTriggerName,_a:aluRMTriggerAdminStatus,_b:aluRMTriggerOperStatus,_c:aluRMTriggerDescription,_d:aluRMTriggerDetectDebounce,_e:aluRMTriggerClearDebounce,_f:aluRMTriggerAnalogVoltage,_g:aluRMTriggerDigitalState,_h:aluRMTriggerAlias,_A8:aluRMTriggerDigitalNorm,_A9:aluRMTriggerRowStatus,'aluRMRelayTable':aluRMRelayTable,'aluRMRelayEntry':aluRMRelayEntry,_X:aluRMRelayID,_i:aluRMRelayName,_j:aluRMRelayMode,_k:aluRMRelayAdminStatus,_l:aluRMRelayOperStatus,_m:aluRMRelayDescription,_n:aluRMRelayAlias,'aluRMAlarmTable':aluRMAlarmTable,'aluRMAlarmEntry':aluRMAlarmEntry,_Y:aluRMAlarmID,_o:aluRMAlarmRowStatus,_p:aluRMAlarmAdminStatus,_q:aluRMAlarmOperStatus,_r:aluRMAlarmDescription,_s:aluRMAlarmTriggerRule,_t:aluRMAlarmTrigger1,_u:aluRMAlarmTrigger2,_v:aluRMAlarmTrigger3,_w:aluRMAlarmTrigger4,_x:aluRMAlarmTrigger5,_y:aluRMAlarmTrigger6,_z:aluRMAlarmTrigger7,_A0:aluRMAlarmTrigger8,_A1:aluRMAlarmSeverity,_A2:aluRMAlarmActionLog,_A3:aluRMAlarmActionAlarmRelay,_A4:aluRMAlarmActionAuxRelay,_A5:aluRMAlarmAuxRelay,_G:aluRMAlarmDetectedTriggers,_A6:aluRMAlarmTHAnalogLevelOperation,_A7:aluRMAlarmTHAnalogLevel,'aluRMNotifyObjs':aluRMNotifyObjs,_H:aluRMAlarmNotifyID,_I:aluRMAlarmNotifyDescription,_S:aluRMNotifyID,_T:aluRMNotifyOperState,'aluRMNotifyPrefix':aluRMNotifyPrefix,'aluRMNotification':aluRMNotification,_AA:aluRMCriticalAlarm,_AB:aluRMMajorAlarm,_AC:aluRMMinorAlarm,_AD:aluRMWarningAlarm,_AE:aluRMClearingAlarm,_AF:aluRMOperStateUpdate})