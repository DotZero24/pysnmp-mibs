_AH='tmnxInterChassisLinkV16v0Group'
_AG='tmnxSfmIcPortNotifV12v0Group'
_AF='tmnxSfmIcPortV12v0Group'
_AE='tmnxCpmIcPortNotifV12v0Group'
_AD='tmnxCpmIcPortV12v0Group'
_AC='tmnxChassIcNotifyObjsV12v0Group'
_AB='tmnxChassIcNotifV12v0Group'
_AA='tmnxSfmIcPortDegradedClear'
_A9='tmnxSfmIcPortDegraded'
_A8='tmnxSfmIcPortDDMClear'
_A7='tmnxSfmIcPortDDMFailure'
_A6='tmnxSfmIcPortSFFStatusFailure'
_A5='tmnxSfmIcPortSFFRemoved'
_A4='tmnxSfmIcPortSFFInserted'
_A3='tmnxSfmIcPortUp'
_A2='tmnxSfmIcPortDown'
_A1='tmnxCpmIcPortDDMClear'
_A0='tmnxCpmIcPortDDMFailure'
_z='tmnxCpmIcPortSFFStatusFailure'
_y='tmnxCpmLocalIcPortAvail'
_x='tmnxCpmNoLocalIcPort'
_w='tmnxCpmIcPortSFFRemoved'
_v='tmnxCpmIcPortSFFInserted'
_u='tmnxCpmIcPortUp'
_t='tmnxCpmIcPortDown'
_s='tmnxInterChassisCommsUp'
_r='tmnxInterChassisCommsDown'
_q='tmnxICLNum'
_p='tmnxSfmIcPortNum'
_o='tmnxCpmIcPortNum'
_n='indeterminate'
_m='noLink'
_l='invalidConnection'
_k='TmnxAdminState'
_j='tmnxFabricSlotNum'
_i='tmnxCpmCardSlotNum'
_h='Integer32'
_g='tmnxICLOperState'
_f='tmnxICLSecondaryChassisPortId'
_e='tmnxICLPrimaryChassisPortId'
_d='tmnxICLAdminState'
_c='tmnxICLLastChanged'
_b='tmnxICLRowStatus'
_a='tmnxICLTableLastChange'
_Z='tmnxSfmIcPortMisconSfmIcPort'
_Y='tmnxSfmIcPortMisconSfm'
_X='tmnxSfmIcPortSFFStatus'
_W='tmnxCpmIcPortSFFStatus'
_V='not-accessible'
_U='TmnxPortID'
_T='tmnxChassisNotifyFabricSlotNum'
_S='tmnxChassisIndex'
_R='tmnxSfmIcPortDegradeState'
_Q='tmnxSfmIcPortSFFEquipped'
_P='tmnxSfmIcPortOperState'
_O='tmnxCpmIcPortSFFEquipped'
_N='tmnxCpmIcPortOperState'
_M='read-create'
_L='Unsigned32'
_K='tmnxDDMLaneIdOrModule'
_J='tmnxDDMFailedObject'
_I='tmnxChassisNotifyCpmCardSlotNum'
_H='tmnxNotifyIcPortNum'
_G='TIMETRA-PORT-MIB'
_F='tmnxHwClass'
_E='read-only'
_D='obsolete'
_C='TIMETRA-CHASSIS-MIB'
_B='current'
_A='TIMETRA-CHASSIS-INTERCONNECT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_h,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
tmnxChassisIndex,tmnxChassisNotifyCpmCardSlotNum,tmnxChassisNotifyFabricSlotNum,tmnxCpmCardSlotNum,tmnxFabricSlotNum,tmnxHwClass=mibBuilder.importSymbols(_C,_S,_I,_T,_i,_j,_F)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxSFFStatus,tmnxDDMFailedObject,tmnxDDMLaneIdOrModule=mibBuilder.importSymbols(_G,'TmnxSFFStatus',_J,_K)
TmnxAdminState,TmnxPortID=mibBuilder.importSymbols('TIMETRA-TC-MIB',_k,_U)
timetraChassisInterconMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,94))
if mibBuilder.loadTexts:timetraChassisInterconMIBModule.setRevisions(('2013-10-31 00:00',))
class TmnxIcPortState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),(_l,2),(_m,3),(_n,4),('unsupportedSff',5)))
class TmnxICLState(TextualConvention,Integer32):status=_D;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),(_l,2),(_m,3),(_n,4)))
_TmnxChassisInterconConformance_ObjectIdentity=ObjectIdentity
tmnxChassisInterconConformance=_TmnxChassisInterconConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94))
_TmnxChassisInterconCompliances_ObjectIdentity=ObjectIdentity
tmnxChassisInterconCompliances=_TmnxChassisInterconCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94,1))
_TmnxChassisInterconGroups_ObjectIdentity=ObjectIdentity
tmnxChassisInterconGroups=_TmnxChassisInterconGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94,2))
_TmnxChassIcV12v0Groups_ObjectIdentity=ObjectIdentity
tmnxChassIcV12v0Groups=_TmnxChassIcV12v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94,2,1))
_TmnxChassIcV16v0Groups_ObjectIdentity=ObjectIdentity
tmnxChassIcV16v0Groups=_TmnxChassIcV16v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94,2,2))
_TmnxChassIcV20v0Groups_ObjectIdentity=ObjectIdentity
tmnxChassIcV20v0Groups=_TmnxChassIcV20v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,94,2,3))
_TmnxChassisInterconObjs_ObjectIdentity=ObjectIdentity
tmnxChassisInterconObjs=_TmnxChassisInterconObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,94))
_TmnxIcPortObjs_ObjectIdentity=ObjectIdentity
tmnxIcPortObjs=_TmnxIcPortObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,94,1))
_TmnxCpmIcPortTable_Object=MibTable
tmnxCpmIcPortTable=_TmnxCpmIcPortTable_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1))
if mibBuilder.loadTexts:tmnxCpmIcPortTable.setStatus(_B)
_TmnxCpmIcPortEntry_Object=MibTableRow
tmnxCpmIcPortEntry=_TmnxCpmIcPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1,1))
tmnxCpmIcPortEntry.setIndexNames((0,_C,_S),(0,_C,_i),(0,_A,_o))
if mibBuilder.loadTexts:tmnxCpmIcPortEntry.setStatus(_B)
class _TmnxCpmIcPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_TmnxCpmIcPortNum_Type.__name__=_L
_TmnxCpmIcPortNum_Object=MibTableColumn
tmnxCpmIcPortNum=_TmnxCpmIcPortNum_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1,1,1),_TmnxCpmIcPortNum_Type())
tmnxCpmIcPortNum.setMaxAccess(_V)
if mibBuilder.loadTexts:tmnxCpmIcPortNum.setStatus(_B)
_TmnxCpmIcPortOperState_Type=TmnxIcPortState
_TmnxCpmIcPortOperState_Object=MibTableColumn
tmnxCpmIcPortOperState=_TmnxCpmIcPortOperState_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1,1,2),_TmnxCpmIcPortOperState_Type())
tmnxCpmIcPortOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxCpmIcPortOperState.setStatus(_B)
_TmnxCpmIcPortSFFEquipped_Type=TruthValue
_TmnxCpmIcPortSFFEquipped_Object=MibTableColumn
tmnxCpmIcPortSFFEquipped=_TmnxCpmIcPortSFFEquipped_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1,1,3),_TmnxCpmIcPortSFFEquipped_Type())
tmnxCpmIcPortSFFEquipped.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxCpmIcPortSFFEquipped.setStatus(_B)
_TmnxCpmIcPortSFFStatus_Type=TmnxSFFStatus
_TmnxCpmIcPortSFFStatus_Object=MibTableColumn
tmnxCpmIcPortSFFStatus=_TmnxCpmIcPortSFFStatus_Object((1,3,6,1,4,1,6527,3,1,2,94,1,1,1,4),_TmnxCpmIcPortSFFStatus_Type())
tmnxCpmIcPortSFFStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxCpmIcPortSFFStatus.setStatus(_B)
_TmnxSfmIcPortTable_Object=MibTable
tmnxSfmIcPortTable=_TmnxSfmIcPortTable_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2))
if mibBuilder.loadTexts:tmnxSfmIcPortTable.setStatus(_B)
_TmnxSfmIcPortEntry_Object=MibTableRow
tmnxSfmIcPortEntry=_TmnxSfmIcPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1))
tmnxSfmIcPortEntry.setIndexNames((0,_C,_S),(0,_C,_j),(0,_A,_p))
if mibBuilder.loadTexts:tmnxSfmIcPortEntry.setStatus(_B)
class _TmnxSfmIcPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_TmnxSfmIcPortNum_Type.__name__=_L
_TmnxSfmIcPortNum_Object=MibTableColumn
tmnxSfmIcPortNum=_TmnxSfmIcPortNum_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,1),_TmnxSfmIcPortNum_Type())
tmnxSfmIcPortNum.setMaxAccess(_V)
if mibBuilder.loadTexts:tmnxSfmIcPortNum.setStatus(_B)
_TmnxSfmIcPortOperState_Type=TmnxIcPortState
_TmnxSfmIcPortOperState_Object=MibTableColumn
tmnxSfmIcPortOperState=_TmnxSfmIcPortOperState_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,2),_TmnxSfmIcPortOperState_Type())
tmnxSfmIcPortOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortOperState.setStatus(_B)
_TmnxSfmIcPortSFFEquipped_Type=TruthValue
_TmnxSfmIcPortSFFEquipped_Object=MibTableColumn
tmnxSfmIcPortSFFEquipped=_TmnxSfmIcPortSFFEquipped_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,3),_TmnxSfmIcPortSFFEquipped_Type())
tmnxSfmIcPortSFFEquipped.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortSFFEquipped.setStatus(_B)
_TmnxSfmIcPortSFFStatus_Type=TmnxSFFStatus
_TmnxSfmIcPortSFFStatus_Object=MibTableColumn
tmnxSfmIcPortSFFStatus=_TmnxSfmIcPortSFFStatus_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,4),_TmnxSfmIcPortSFFStatus_Type())
tmnxSfmIcPortSFFStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortSFFStatus.setStatus(_B)
class _TmnxSfmIcPortDegradeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('degraded',2)))
_TmnxSfmIcPortDegradeState_Type.__name__=_h
_TmnxSfmIcPortDegradeState_Object=MibTableColumn
tmnxSfmIcPortDegradeState=_TmnxSfmIcPortDegradeState_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,5),_TmnxSfmIcPortDegradeState_Type())
tmnxSfmIcPortDegradeState.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortDegradeState.setStatus(_B)
_TmnxSfmIcPortMisconSfm_Type=Unsigned32
_TmnxSfmIcPortMisconSfm_Object=MibTableColumn
tmnxSfmIcPortMisconSfm=_TmnxSfmIcPortMisconSfm_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,6),_TmnxSfmIcPortMisconSfm_Type())
tmnxSfmIcPortMisconSfm.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortMisconSfm.setStatus(_B)
_TmnxSfmIcPortMisconSfmIcPort_Type=Unsigned32
_TmnxSfmIcPortMisconSfmIcPort_Object=MibTableColumn
tmnxSfmIcPortMisconSfmIcPort=_TmnxSfmIcPortMisconSfmIcPort_Object((1,3,6,1,4,1,6527,3,1,2,94,1,2,1,7),_TmnxSfmIcPortMisconSfmIcPort_Type())
tmnxSfmIcPortMisconSfmIcPort.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxSfmIcPortMisconSfmIcPort.setStatus(_B)
_TmnxChassIcNotifObjs_ObjectIdentity=ObjectIdentity
tmnxChassIcNotifObjs=_TmnxChassIcNotifObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,94,2))
_TmnxNotifyIcPortNum_Type=Unsigned32
_TmnxNotifyIcPortNum_Object=MibScalar
tmnxNotifyIcPortNum=_TmnxNotifyIcPortNum_Object((1,3,6,1,4,1,6527,3,1,2,94,2,1),_TmnxNotifyIcPortNum_Type())
tmnxNotifyIcPortNum.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:tmnxNotifyIcPortNum.setStatus(_B)
_TmnxInterChassisLinkObjs_ObjectIdentity=ObjectIdentity
tmnxInterChassisLinkObjs=_TmnxInterChassisLinkObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,94,3))
_TmnxICLTableLastChange_Type=TimeStamp
_TmnxICLTableLastChange_Object=MibScalar
tmnxICLTableLastChange=_TmnxICLTableLastChange_Object((1,3,6,1,4,1,6527,3,1,2,94,3,1),_TmnxICLTableLastChange_Type())
tmnxICLTableLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxICLTableLastChange.setStatus(_D)
_TmnxICLTable_Object=MibTable
tmnxICLTable=_TmnxICLTable_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2))
if mibBuilder.loadTexts:tmnxICLTable.setStatus(_D)
_TmnxICLEntry_Object=MibTableRow
tmnxICLEntry=_TmnxICLEntry_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1))
tmnxICLEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:tmnxICLEntry.setStatus(_D)
class _TmnxICLNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TmnxICLNum_Type.__name__=_L
_TmnxICLNum_Object=MibTableColumn
tmnxICLNum=_TmnxICLNum_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,1),_TmnxICLNum_Type())
tmnxICLNum.setMaxAccess(_V)
if mibBuilder.loadTexts:tmnxICLNum.setStatus(_D)
_TmnxICLRowStatus_Type=RowStatus
_TmnxICLRowStatus_Object=MibTableColumn
tmnxICLRowStatus=_TmnxICLRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,2),_TmnxICLRowStatus_Type())
tmnxICLRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxICLRowStatus.setStatus(_D)
_TmnxICLLastChanged_Type=TimeStamp
_TmnxICLLastChanged_Object=MibTableColumn
tmnxICLLastChanged=_TmnxICLLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,3),_TmnxICLLastChanged_Type())
tmnxICLLastChanged.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxICLLastChanged.setStatus(_D)
class _TmnxICLAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxICLAdminState_Type.__name__=_k
_TmnxICLAdminState_Object=MibTableColumn
tmnxICLAdminState=_TmnxICLAdminState_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,4),_TmnxICLAdminState_Type())
tmnxICLAdminState.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxICLAdminState.setStatus(_D)
class _TmnxICLPrimaryChassisPortId_Type(TmnxPortID):defaultValue=503316480
_TmnxICLPrimaryChassisPortId_Type.__name__=_U
_TmnxICLPrimaryChassisPortId_Object=MibTableColumn
tmnxICLPrimaryChassisPortId=_TmnxICLPrimaryChassisPortId_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,5),_TmnxICLPrimaryChassisPortId_Type())
tmnxICLPrimaryChassisPortId.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxICLPrimaryChassisPortId.setStatus(_D)
class _TmnxICLSecondaryChassisPortId_Type(TmnxPortID):defaultValue=503316480
_TmnxICLSecondaryChassisPortId_Type.__name__=_U
_TmnxICLSecondaryChassisPortId_Object=MibTableColumn
tmnxICLSecondaryChassisPortId=_TmnxICLSecondaryChassisPortId_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,6),_TmnxICLSecondaryChassisPortId_Type())
tmnxICLSecondaryChassisPortId.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxICLSecondaryChassisPortId.setStatus(_D)
_TmnxICLOperState_Type=TmnxICLState
_TmnxICLOperState_Object=MibTableColumn
tmnxICLOperState=_TmnxICLOperState_Object((1,3,6,1,4,1,6527,3,1,2,94,3,2,1,7),_TmnxICLOperState_Type())
tmnxICLOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxICLOperState.setStatus(_D)
_TmnxChassisInterconNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxChassisInterconNotifyPrefix=_TmnxChassisInterconNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,94))
_TmnxChassisInterconNotification_ObjectIdentity=ObjectIdentity
tmnxChassisInterconNotification=_TmnxChassisInterconNotification_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,94,0))
_TmnxInterChassisNotifications_ObjectIdentity=ObjectIdentity
tmnxInterChassisNotifications=_TmnxInterChassisNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,94,0,1))
_TmnxCpmIcPortNotifications_ObjectIdentity=ObjectIdentity
tmnxCpmIcPortNotifications=_TmnxCpmIcPortNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,94,0,2))
_TmnxSfmIcPortNotifications_ObjectIdentity=ObjectIdentity
tmnxSfmIcPortNotifications=_TmnxSfmIcPortNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,94,0,3))
tmnxChassIcNotifyObjsV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,2))
tmnxChassIcNotifyObjsV12v0Group.setObjects((_A,_H))
if mibBuilder.loadTexts:tmnxChassIcNotifyObjsV12v0Group.setStatus(_B)
tmnxCpmIcPortV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,3))
tmnxCpmIcPortV12v0Group.setObjects(*((_A,_N),(_A,_O),(_A,_W)))
if mibBuilder.loadTexts:tmnxCpmIcPortV12v0Group.setStatus(_B)
tmnxSfmIcPortV12v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,5))
tmnxSfmIcPortV12v0Group.setObjects(*((_A,_P),(_A,_Q),(_A,_X),(_A,_R),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tmnxSfmIcPortV12v0Group.setStatus(_B)
tmnxInterChassisLinkV16v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,94,2,2,1))
tmnxInterChassisLinkV16v0Group.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:tmnxInterChassisLinkV16v0Group.setStatus(_D)
tmnxICLv20v0ObsoleteGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,94,2,3,1))
tmnxICLv20v0ObsoleteGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:tmnxICLv20v0ObsoleteGroup.setStatus(_B)
tmnxInterChassisCommsDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,1,1))
tmnxInterChassisCommsDown.setObjects((_C,_F))
if mibBuilder.loadTexts:tmnxInterChassisCommsDown.setStatus(_B)
tmnxInterChassisCommsUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,1,2))
tmnxInterChassisCommsUp.setObjects((_C,_F))
if mibBuilder.loadTexts:tmnxInterChassisCommsUp.setStatus(_B)
tmnxCpmIcPortDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,1))
tmnxCpmIcPortDown.setObjects(*((_C,_F),(_A,_N)))
if mibBuilder.loadTexts:tmnxCpmIcPortDown.setStatus(_B)
tmnxCpmIcPortUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,2))
tmnxCpmIcPortUp.setObjects(*((_C,_F),(_A,_N)))
if mibBuilder.loadTexts:tmnxCpmIcPortUp.setStatus(_B)
tmnxCpmIcPortSFFInserted=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,3))
tmnxCpmIcPortSFFInserted.setObjects((_A,_O))
if mibBuilder.loadTexts:tmnxCpmIcPortSFFInserted.setStatus(_B)
tmnxCpmIcPortSFFRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,4))
tmnxCpmIcPortSFFRemoved.setObjects((_A,_O))
if mibBuilder.loadTexts:tmnxCpmIcPortSFFRemoved.setStatus(_B)
tmnxCpmNoLocalIcPort=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,5))
tmnxCpmNoLocalIcPort.setObjects(*((_C,_F),(_C,_I)))
if mibBuilder.loadTexts:tmnxCpmNoLocalIcPort.setStatus(_B)
tmnxCpmLocalIcPortAvail=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,6))
tmnxCpmLocalIcPortAvail.setObjects(*((_C,_F),(_C,_I)))
if mibBuilder.loadTexts:tmnxCpmLocalIcPortAvail.setStatus(_B)
tmnxCpmIcPortSFFStatusFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,7))
tmnxCpmIcPortSFFStatusFailure.setObjects((_A,_W))
if mibBuilder.loadTexts:tmnxCpmIcPortSFFStatusFailure.setStatus(_B)
tmnxCpmIcPortDDMFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,8))
tmnxCpmIcPortDDMFailure.setObjects(*((_C,_I),(_A,_H),(_G,_J),(_G,_K)))
if mibBuilder.loadTexts:tmnxCpmIcPortDDMFailure.setStatus(_B)
tmnxCpmIcPortDDMClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,2,9))
tmnxCpmIcPortDDMClear.setObjects(*((_C,_I),(_A,_H),(_G,_J),(_G,_K)))
if mibBuilder.loadTexts:tmnxCpmIcPortDDMClear.setStatus(_B)
tmnxSfmIcPortDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,1))
tmnxSfmIcPortDown.setObjects(*((_C,_F),(_A,_P),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tmnxSfmIcPortDown.setStatus(_B)
tmnxSfmIcPortUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,2))
tmnxSfmIcPortUp.setObjects(*((_C,_F),(_A,_P)))
if mibBuilder.loadTexts:tmnxSfmIcPortUp.setStatus(_B)
tmnxSfmIcPortSFFInserted=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,3))
tmnxSfmIcPortSFFInserted.setObjects((_A,_Q))
if mibBuilder.loadTexts:tmnxSfmIcPortSFFInserted.setStatus(_B)
tmnxSfmIcPortSFFRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,4))
tmnxSfmIcPortSFFRemoved.setObjects((_A,_Q))
if mibBuilder.loadTexts:tmnxSfmIcPortSFFRemoved.setStatus(_B)
tmnxSfmIcPortSFFStatusFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,5))
tmnxSfmIcPortSFFStatusFailure.setObjects((_A,_X))
if mibBuilder.loadTexts:tmnxSfmIcPortSFFStatusFailure.setStatus(_B)
tmnxSfmIcPortDDMFailure=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,6))
tmnxSfmIcPortDDMFailure.setObjects(*((_C,_T),(_A,_H),(_G,_J),(_G,_K)))
if mibBuilder.loadTexts:tmnxSfmIcPortDDMFailure.setStatus(_B)
tmnxSfmIcPortDDMClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,7))
tmnxSfmIcPortDDMClear.setObjects(*((_C,_T),(_A,_H),(_G,_J),(_G,_K)))
if mibBuilder.loadTexts:tmnxSfmIcPortDDMClear.setStatus(_B)
tmnxSfmIcPortDegraded=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,8))
tmnxSfmIcPortDegraded.setObjects((_A,_R))
if mibBuilder.loadTexts:tmnxSfmIcPortDegraded.setStatus(_B)
tmnxSfmIcPortDegradedClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,94,0,3,9))
tmnxSfmIcPortDegradedClear.setObjects((_A,_R))
if mibBuilder.loadTexts:tmnxSfmIcPortDegradedClear.setStatus(_B)
tmnxChassIcNotifV12v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,1))
tmnxChassIcNotifV12v0Group.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:tmnxChassIcNotifV12v0Group.setStatus(_B)
tmnxCpmIcPortNotifV12v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,4))
tmnxCpmIcPortNotifV12v0Group.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:tmnxCpmIcPortNotifV12v0Group.setStatus(_B)
tmnxSfmIcPortNotifV12v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,94,2,1,6))
tmnxSfmIcPortNotifV12v0Group.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:tmnxSfmIcPortNotifV12v0Group.setStatus(_B)
tmnxChassisInterconCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,94,1,1))
tmnxChassisInterconCompliance.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:tmnxChassisInterconCompliance.setStatus(_B)
tmnxChassInterconComplianceV16v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,94,1,2))
tmnxChassInterconComplianceV16v0.setObjects((_A,_AH))
if mibBuilder.loadTexts:tmnxChassInterconComplianceV16v0.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'TmnxIcPortState':TmnxIcPortState,'TmnxICLState':TmnxICLState,'timetraChassisInterconMIBModule':timetraChassisInterconMIBModule,'tmnxChassisInterconConformance':tmnxChassisInterconConformance,'tmnxChassisInterconCompliances':tmnxChassisInterconCompliances,'tmnxChassisInterconCompliance':tmnxChassisInterconCompliance,'tmnxChassInterconComplianceV16v0':tmnxChassInterconComplianceV16v0,'tmnxChassisInterconGroups':tmnxChassisInterconGroups,'tmnxChassIcV12v0Groups':tmnxChassIcV12v0Groups,_AB:tmnxChassIcNotifV12v0Group,_AC:tmnxChassIcNotifyObjsV12v0Group,_AD:tmnxCpmIcPortV12v0Group,_AE:tmnxCpmIcPortNotifV12v0Group,_AF:tmnxSfmIcPortV12v0Group,_AG:tmnxSfmIcPortNotifV12v0Group,'tmnxChassIcV16v0Groups':tmnxChassIcV16v0Groups,_AH:tmnxInterChassisLinkV16v0Group,'tmnxChassIcV20v0Groups':tmnxChassIcV20v0Groups,'tmnxICLv20v0ObsoleteGroup':tmnxICLv20v0ObsoleteGroup,'tmnxChassisInterconObjs':tmnxChassisInterconObjs,'tmnxIcPortObjs':tmnxIcPortObjs,'tmnxCpmIcPortTable':tmnxCpmIcPortTable,'tmnxCpmIcPortEntry':tmnxCpmIcPortEntry,_o:tmnxCpmIcPortNum,_N:tmnxCpmIcPortOperState,_O:tmnxCpmIcPortSFFEquipped,_W:tmnxCpmIcPortSFFStatus,'tmnxSfmIcPortTable':tmnxSfmIcPortTable,'tmnxSfmIcPortEntry':tmnxSfmIcPortEntry,_p:tmnxSfmIcPortNum,_P:tmnxSfmIcPortOperState,_Q:tmnxSfmIcPortSFFEquipped,_X:tmnxSfmIcPortSFFStatus,_R:tmnxSfmIcPortDegradeState,_Y:tmnxSfmIcPortMisconSfm,_Z:tmnxSfmIcPortMisconSfmIcPort,'tmnxChassIcNotifObjs':tmnxChassIcNotifObjs,_H:tmnxNotifyIcPortNum,'tmnxInterChassisLinkObjs':tmnxInterChassisLinkObjs,_a:tmnxICLTableLastChange,'tmnxICLTable':tmnxICLTable,'tmnxICLEntry':tmnxICLEntry,_q:tmnxICLNum,_b:tmnxICLRowStatus,_c:tmnxICLLastChanged,_d:tmnxICLAdminState,_e:tmnxICLPrimaryChassisPortId,_f:tmnxICLSecondaryChassisPortId,_g:tmnxICLOperState,'tmnxChassisInterconNotifyPrefix':tmnxChassisInterconNotifyPrefix,'tmnxChassisInterconNotification':tmnxChassisInterconNotification,'tmnxInterChassisNotifications':tmnxInterChassisNotifications,_r:tmnxInterChassisCommsDown,_s:tmnxInterChassisCommsUp,'tmnxCpmIcPortNotifications':tmnxCpmIcPortNotifications,_t:tmnxCpmIcPortDown,_u:tmnxCpmIcPortUp,_v:tmnxCpmIcPortSFFInserted,_w:tmnxCpmIcPortSFFRemoved,_x:tmnxCpmNoLocalIcPort,_y:tmnxCpmLocalIcPortAvail,_z:tmnxCpmIcPortSFFStatusFailure,_A0:tmnxCpmIcPortDDMFailure,_A1:tmnxCpmIcPortDDMClear,'tmnxSfmIcPortNotifications':tmnxSfmIcPortNotifications,_A2:tmnxSfmIcPortDown,_A3:tmnxSfmIcPortUp,_A4:tmnxSfmIcPortSFFInserted,_A5:tmnxSfmIcPortSFFRemoved,_A6:tmnxSfmIcPortSFFStatusFailure,_A7:tmnxSfmIcPortDDMFailure,_A8:tmnxSfmIcPortDDMClear,_A9:tmnxSfmIcPortDegraded,_AA:tmnxSfmIcPortDegradedClear})