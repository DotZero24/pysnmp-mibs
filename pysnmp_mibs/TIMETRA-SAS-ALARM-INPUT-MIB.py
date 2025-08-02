_g='tmnxAlInpV13v0NotificationGroup'
_f='tmnxAlarmInputNotificationV2v0Group'
_e='tmnxAlmInpV2v0NotifyObjsGroup'
_d='tmnxSASAlarmInputV2v0Group'
_c='tmnxAlarmInputVoltageFailure'
_b='tmnxSasAlarminput4StateChanged'
_a='tmnxSasAlarminput3StateChanged'
_Z='tmnxSasAlarminput2StateChanged'
_Y='tmnxSasAlarminput1StateChanged'
_X='tmnxSasAlarmInputClearMessage'
_W='tmnxSasAlarmInputTriggerMessage'
_V='tmnxSasAlarmInputLastChange'
_U='tmnxSasAlarmInputPolarity'
_T='tmnxSasAlarmInputAdminState'
_S='accessible-for-notify'
_R='read-only'
_Q='tmnxHwID'
_P='tmnxChassisNotifyHwIndex'
_O='tmnxSasAlarmInputPowerStatus'
_N='tmnxSasAlarmInputId'
_M='TItemLongDescription'
_L='OctetString'
_K='tmnxSasAlarmInputNotifyMessage'
_J='tmnxSasAlarmInputNotifyId'
_I='tmnxSasAlarmInputStatus'
_H='tmnxSasAlarmOutputSeverity'
_G='tmnxSasAlarmInputDescription'
_F='tmnxHwClass'
_E='read-write'
_D='Integer32'
_C='TIMETRA-CHASSIS-MIB'
_B='current'
_A='TIMETRA-SAS-ALARM-INPUT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tmnxChassisNotifyHwIndex,tmnxHwClass,tmnxHwID=mibBuilder.importSymbols(_C,_P,_F,_Q)
tmnxBasedProducts,=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','tmnxBasedProducts')
TItemLongDescription,=mibBuilder.importSymbols('TIMETRA-TC-MIB',_M)
tmnxSasAlarmInputMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,10))
if mibBuilder.loadTexts:tmnxSasAlarmInputMIBModule.setRevisions(('2015-07-08 00:00','2010-04-08 00:00'))
_TimetraServiceAccessSwitches_ObjectIdentity=ObjectIdentity
timetraServiceAccessSwitches=_TimetraServiceAccessSwitches_ObjectIdentity((1,3,6,1,4,1,6527,6,2))
_TimetraSASRegistry_ObjectIdentity=ObjectIdentity
timetraSASRegistry=_TimetraSASRegistry_ObjectIdentity((1,3,6,1,4,1,6527,6,2,1))
_TimetraSASModules_ObjectIdentity=ObjectIdentity
timetraSASModules=_TimetraSASModules_ObjectIdentity((1,3,6,1,4,1,6527,6,2,1,1))
_TimetraSASMIB_ObjectIdentity=ObjectIdentity
timetraSASMIB=_TimetraSASMIB_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2))
_TimetraSASConfs_ObjectIdentity=ObjectIdentity
timetraSASConfs=_TimetraSASConfs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1))
_TmnxSASAlarmInputConformance_ObjectIdentity=ObjectIdentity
tmnxSASAlarmInputConformance=_TmnxSASAlarmInputConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,6))
_TmnxSASAlarmInputCompliances_ObjectIdentity=ObjectIdentity
tmnxSASAlarmInputCompliances=_TmnxSASAlarmInputCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,6,1))
_TmnxSASAlarmInputGroups_ObjectIdentity=ObjectIdentity
tmnxSASAlarmInputGroups=_TmnxSASAlarmInputGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,6,2))
_TimetraSASObjs_ObjectIdentity=ObjectIdentity
timetraSASObjs=_TimetraSASObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2))
_TmnxSASChassisObjs_ObjectIdentity=ObjectIdentity
tmnxSASChassisObjs=_TmnxSASChassisObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,6))
_TmnxSASChassisNotification_ObjectIdentity=ObjectIdentity
tmnxSASChassisNotification=_TmnxSASChassisNotification_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,6,2))
_TmnxSasAlarmInputObjs_ObjectIdentity=ObjectIdentity
tmnxSasAlarmInputObjs=_TmnxSasAlarmInputObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,9))
_TmnxSasAlarmInputInfoTable_Object=MibTable
tmnxSasAlarmInputInfoTable=_TmnxSasAlarmInputInfoTable_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1))
if mibBuilder.loadTexts:tmnxSasAlarmInputInfoTable.setStatus(_B)
_TmnxSasAlarmInputInfoEntry_Object=MibTableRow
tmnxSasAlarmInputInfoEntry=_TmnxSasAlarmInputInfoEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1))
tmnxSasAlarmInputInfoEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:tmnxSasAlarmInputInfoEntry.setStatus(_B)
class _TmnxSasAlarmInputId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TmnxSasAlarmInputId_Type.__name__=_D
_TmnxSasAlarmInputId_Object=MibTableColumn
tmnxSasAlarmInputId=_TmnxSasAlarmInputId_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,1),_TmnxSasAlarmInputId_Type())
tmnxSasAlarmInputId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxSasAlarmInputId.setStatus(_B)
class _TmnxSasAlarmInputDescription_Type(TItemLongDescription):defaultValue=OctetString('');subtypeSpec=TItemLongDescription.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_TmnxSasAlarmInputDescription_Type.__name__=_M
_TmnxSasAlarmInputDescription_Object=MibTableColumn
tmnxSasAlarmInputDescription=_TmnxSasAlarmInputDescription_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,2),_TmnxSasAlarmInputDescription_Type())
tmnxSasAlarmInputDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputDescription.setStatus(_B)
class _TmnxSasAlarmInputAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TmnxSasAlarmInputAdminState_Type.__name__=_D
_TmnxSasAlarmInputAdminState_Object=MibTableColumn
tmnxSasAlarmInputAdminState=_TmnxSasAlarmInputAdminState_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,3),_TmnxSasAlarmInputAdminState_Type())
tmnxSasAlarmInputAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputAdminState.setStatus(_B)
class _TmnxSasAlarmInputPolarity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normallyOpen',1),('normallyClosed',2)))
_TmnxSasAlarmInputPolarity_Type.__name__=_D
_TmnxSasAlarmInputPolarity_Object=MibTableColumn
tmnxSasAlarmInputPolarity=_TmnxSasAlarmInputPolarity_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,4),_TmnxSasAlarmInputPolarity_Type())
tmnxSasAlarmInputPolarity.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputPolarity.setStatus(_B)
class _TmnxSasAlarmOutputSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('minor',2),('major',3),('critical',4)))
_TmnxSasAlarmOutputSeverity_Type.__name__=_D
_TmnxSasAlarmOutputSeverity_Object=MibTableColumn
tmnxSasAlarmOutputSeverity=_TmnxSasAlarmOutputSeverity_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,5),_TmnxSasAlarmOutputSeverity_Type())
tmnxSasAlarmOutputSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmOutputSeverity.setStatus(_B)
class _TmnxSasAlarmInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAlarm',1),('alarm',2)))
_TmnxSasAlarmInputStatus_Type.__name__=_D
_TmnxSasAlarmInputStatus_Object=MibTableColumn
tmnxSasAlarmInputStatus=_TmnxSasAlarmInputStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,6),_TmnxSasAlarmInputStatus_Type())
tmnxSasAlarmInputStatus.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxSasAlarmInputStatus.setStatus(_B)
_TmnxSasAlarmInputLastChange_Type=TimeTicks
_TmnxSasAlarmInputLastChange_Object=MibTableColumn
tmnxSasAlarmInputLastChange=_TmnxSasAlarmInputLastChange_Object((1,3,6,1,4,1,6527,6,2,2,2,9,1,1,7),_TmnxSasAlarmInputLastChange_Type())
tmnxSasAlarmInputLastChange.setMaxAccess(_R)
if mibBuilder.loadTexts:tmnxSasAlarmInputLastChange.setStatus(_B)
_TmnxSasAlarmInputMessageTable_Object=MibTable
tmnxSasAlarmInputMessageTable=_TmnxSasAlarmInputMessageTable_Object((1,3,6,1,4,1,6527,6,2,2,2,9,2))
if mibBuilder.loadTexts:tmnxSasAlarmInputMessageTable.setStatus(_B)
_TmnxSasAlarmInputMessageEntry_Object=MibTableRow
tmnxSasAlarmInputMessageEntry=_TmnxSasAlarmInputMessageEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,9,2,1))
tmnxSasAlarmInputMessageEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:tmnxSasAlarmInputMessageEntry.setStatus(_B)
class _TmnxSasAlarmInputTriggerMessage_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TmnxSasAlarmInputTriggerMessage_Type.__name__=_L
_TmnxSasAlarmInputTriggerMessage_Object=MibTableColumn
tmnxSasAlarmInputTriggerMessage=_TmnxSasAlarmInputTriggerMessage_Object((1,3,6,1,4,1,6527,6,2,2,2,9,2,1,1),_TmnxSasAlarmInputTriggerMessage_Type())
tmnxSasAlarmInputTriggerMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputTriggerMessage.setStatus(_B)
class _TmnxSasAlarmInputClearMessage_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TmnxSasAlarmInputClearMessage_Type.__name__=_L
_TmnxSasAlarmInputClearMessage_Object=MibTableColumn
tmnxSasAlarmInputClearMessage=_TmnxSasAlarmInputClearMessage_Object((1,3,6,1,4,1,6527,6,2,2,2,9,2,1,2),_TmnxSasAlarmInputClearMessage_Type())
tmnxSasAlarmInputClearMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputClearMessage.setStatus(_B)
class _TmnxSasAlarmInputPowerStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_TmnxSasAlarmInputPowerStatus_Type.__name__=_D
_TmnxSasAlarmInputPowerStatus_Object=MibScalar
tmnxSasAlarmInputPowerStatus=_TmnxSasAlarmInputPowerStatus_Object((1,3,6,1,4,1,6527,6,2,2,2,9,3),_TmnxSasAlarmInputPowerStatus_Type())
tmnxSasAlarmInputPowerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSasAlarmInputPowerStatus.setStatus(_B)
_TmnxSasAlarmInputNotifyObjs_ObjectIdentity=ObjectIdentity
tmnxSasAlarmInputNotifyObjs=_TmnxSasAlarmInputNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,10))
_TmnxSasAlarmInputNotifyId_Type=Integer32
_TmnxSasAlarmInputNotifyId_Object=MibScalar
tmnxSasAlarmInputNotifyId=_TmnxSasAlarmInputNotifyId_Object((1,3,6,1,4,1,6527,6,2,2,2,10,1),_TmnxSasAlarmInputNotifyId_Type())
tmnxSasAlarmInputNotifyId.setMaxAccess(_S)
if mibBuilder.loadTexts:tmnxSasAlarmInputNotifyId.setStatus(_B)
class _TmnxSasAlarmInputNotifyMessage_Type(TItemLongDescription):subtypeSpec=TItemLongDescription.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_TmnxSasAlarmInputNotifyMessage_Type.__name__=_M
_TmnxSasAlarmInputNotifyMessage_Object=MibScalar
tmnxSasAlarmInputNotifyMessage=_TmnxSasAlarmInputNotifyMessage_Object((1,3,6,1,4,1,6527,6,2,2,2,10,2),_TmnxSasAlarmInputNotifyMessage_Type())
tmnxSasAlarmInputNotifyMessage.setMaxAccess(_S)
if mibBuilder.loadTexts:tmnxSasAlarmInputNotifyMessage.setStatus(_B)
_TimetraSASNotifyPrefix_ObjectIdentity=ObjectIdentity
timetraSASNotifyPrefix=_TimetraSASNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,3))
_TmnxSasAlarmInputNotifications_ObjectIdentity=ObjectIdentity
tmnxSasAlarmInputNotifications=_TmnxSasAlarmInputNotifications_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,3,10))
tmnxSASAlarmInputV2v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,6,2,1))
tmnxSASAlarmInputV2v0Group.setObjects(*((_A,_G),(_A,_T),(_A,_U),(_A,_H),(_A,_I),(_A,_V),(_A,_W),(_A,_X),(_A,_O)))
if mibBuilder.loadTexts:tmnxSASAlarmInputV2v0Group.setStatus(_B)
tmnxAlmInpV2v0NotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,6,2,3))
tmnxAlmInpV2v0NotifyObjsGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:tmnxAlmInpV2v0NotifyObjsGroup.setStatus(_B)
tmnxAlarmInputVoltageFailure=NotificationType((1,3,6,1,4,1,6527,6,2,2,2,6,2,10))
tmnxAlarmInputVoltageFailure.setObjects(*((_C,_P),(_C,_Q),(_C,_F),(_A,_O)))
if mibBuilder.loadTexts:tmnxAlarmInputVoltageFailure.setStatus(_B)
tmnxSasAlarminput1StateChanged=NotificationType((1,3,6,1,4,1,6527,6,2,2,3,10,1))
tmnxSasAlarminput1StateChanged.setObjects(*((_A,_J),(_A,_G),(_A,_I),(_A,_H),(_A,_K),(_C,_F)))
if mibBuilder.loadTexts:tmnxSasAlarminput1StateChanged.setStatus(_B)
tmnxSasAlarminput2StateChanged=NotificationType((1,3,6,1,4,1,6527,6,2,2,3,10,2))
tmnxSasAlarminput2StateChanged.setObjects(*((_A,_J),(_A,_G),(_A,_I),(_A,_H),(_A,_K),(_C,_F)))
if mibBuilder.loadTexts:tmnxSasAlarminput2StateChanged.setStatus(_B)
tmnxSasAlarminput3StateChanged=NotificationType((1,3,6,1,4,1,6527,6,2,2,3,10,3))
tmnxSasAlarminput3StateChanged.setObjects(*((_A,_J),(_A,_G),(_A,_I),(_A,_H),(_A,_K),(_C,_F)))
if mibBuilder.loadTexts:tmnxSasAlarminput3StateChanged.setStatus(_B)
tmnxSasAlarminput4StateChanged=NotificationType((1,3,6,1,4,1,6527,6,2,2,3,10,4))
tmnxSasAlarminput4StateChanged.setObjects(*((_A,_J),(_A,_G),(_A,_I),(_A,_H),(_A,_K),(_C,_F)))
if mibBuilder.loadTexts:tmnxSasAlarminput4StateChanged.setStatus(_B)
tmnxAlarmInputNotificationV2v0Group=NotificationGroup((1,3,6,1,4,1,6527,6,2,2,1,6,2,2))
tmnxAlarmInputNotificationV2v0Group.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:tmnxAlarmInputNotificationV2v0Group.setStatus(_B)
tmnxAlInpV13v0NotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,6,2,2,1,6,2,5))
tmnxAlInpV13v0NotificationGroup.setObjects((_A,_c))
if mibBuilder.loadTexts:tmnxAlInpV13v0NotificationGroup.setStatus(_B)
tmnxSASAlarmInputComp7210V2v0=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,6,1,1))
tmnxSASAlarmInputComp7210V2v0.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:tmnxSASAlarmInputComp7210V2v0.setStatus(_B)
tmnxSASAlarmInputComp7X50V13v0=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,6,1,2))
tmnxSASAlarmInputComp7X50V13v0.setObjects((_A,_g))
if mibBuilder.loadTexts:tmnxSASAlarmInputComp7X50V13v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'timetraServiceAccessSwitches':timetraServiceAccessSwitches,'timetraSASRegistry':timetraSASRegistry,'timetraSASModules':timetraSASModules,'tmnxSasAlarmInputMIBModule':tmnxSasAlarmInputMIBModule,'timetraSASMIB':timetraSASMIB,'timetraSASConfs':timetraSASConfs,'tmnxSASAlarmInputConformance':tmnxSASAlarmInputConformance,'tmnxSASAlarmInputCompliances':tmnxSASAlarmInputCompliances,'tmnxSASAlarmInputComp7210V2v0':tmnxSASAlarmInputComp7210V2v0,'tmnxSASAlarmInputComp7X50V13v0':tmnxSASAlarmInputComp7X50V13v0,'tmnxSASAlarmInputGroups':tmnxSASAlarmInputGroups,_d:tmnxSASAlarmInputV2v0Group,_f:tmnxAlarmInputNotificationV2v0Group,_e:tmnxAlmInpV2v0NotifyObjsGroup,_g:tmnxAlInpV13v0NotificationGroup,'timetraSASObjs':timetraSASObjs,'tmnxSASChassisObjs':tmnxSASChassisObjs,'tmnxSASChassisNotification':tmnxSASChassisNotification,_c:tmnxAlarmInputVoltageFailure,'tmnxSasAlarmInputObjs':tmnxSasAlarmInputObjs,'tmnxSasAlarmInputInfoTable':tmnxSasAlarmInputInfoTable,'tmnxSasAlarmInputInfoEntry':tmnxSasAlarmInputInfoEntry,_N:tmnxSasAlarmInputId,_G:tmnxSasAlarmInputDescription,_T:tmnxSasAlarmInputAdminState,_U:tmnxSasAlarmInputPolarity,_H:tmnxSasAlarmOutputSeverity,_I:tmnxSasAlarmInputStatus,_V:tmnxSasAlarmInputLastChange,'tmnxSasAlarmInputMessageTable':tmnxSasAlarmInputMessageTable,'tmnxSasAlarmInputMessageEntry':tmnxSasAlarmInputMessageEntry,_W:tmnxSasAlarmInputTriggerMessage,_X:tmnxSasAlarmInputClearMessage,_O:tmnxSasAlarmInputPowerStatus,'tmnxSasAlarmInputNotifyObjs':tmnxSasAlarmInputNotifyObjs,_J:tmnxSasAlarmInputNotifyId,_K:tmnxSasAlarmInputNotifyMessage,'timetraSASNotifyPrefix':timetraSASNotifyPrefix,'tmnxSasAlarmInputNotifications':tmnxSasAlarmInputNotifications,_Y:tmnxSasAlarminput1StateChanged,_Z:tmnxSasAlarminput2StateChanged,_a:tmnxSasAlarminput3StateChanged,_b:tmnxSasAlarminput4StateChanged})