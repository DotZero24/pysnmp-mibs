_u='fcIfGroupV2'
_t='fcGeneralGroup'
_s='fcIfTxSignalStatusDegraded'
_r='fcIfTxSignalStatusUp'
_q='fcIfTxSignalStatusDown'
_p='fcIfObjectProperty'
_o='fcGeneralFcIfTableSize'
_n='FcSignalFormat'
_m='DisplayString'
_l='Gauge32'
_k='BoardOrInterfaceOperStatus'
_j='BoardOrInterfaceAdminStatus'
_i='fcGeneralGroupV2'
_h='fcIfGroup'
_g='fcIfFarEndLoopback'
_f='fcIfSuppressRemoteAlarms'
_e='fcIfForwardAls'
_d='fcIfAuAlarmIndicationSignalW2C'
_c='fcIfLossOfSync'
_b='fcIfLossOfSignal'
_a='fcIfOperStatus'
_Z='fcIfAdminStatus'
_Y='fcIfLaserStatus'
_X='fcIfHighSpeed'
_W='fcIfFormat'
_V='fcIfInvPhysIndexOrZero'
_U='fcIfDescr'
_T='fcGeneralStateLastChangeTime'
_S='fcGeneralLastChangeTime'
_R='enabled'
_Q='disabled'
_P='fcNotificationGroup'
_O='deprecated'
_N='Unsigned32'
_M='fcIfEntityId'
_L='read-write'
_K='fcIfTxSignalStatus'
_J='fcIfRxPort'
_I='fcIfTxPort'
_H='fcIfSlot'
_G='fcIfSubrack'
_F='fcIfName'
_E='Integer32'
_D='fcIfIndex'
_C='read-only'
_B='current'
_A='LUM-FC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumFcMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumFcMIB','lumModules')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,FaultStatus,MgmtNameString,ObjectProperty,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_j,_k,'FaultStatus','MgmtNameString','ObjectProperty','PortNumber','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_l,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_m,'PhysAddress','TextualConvention')
lumFcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,23))
if mibBuilder.loadTexts:lumFcMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2002-12-06 00:00','2002-11-19 00:00','2002-11-13 00:00','2002-06-25 00:00'))
class FcSignalFormat(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('undefined',0),('fc1Gb',1)))
_LumFcConfs_ObjectIdentity=ObjectIdentity
lumFcConfs=_LumFcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,22,1))
_LumFcGroups_ObjectIdentity=ObjectIdentity
lumFcGroups=_LumFcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,22,1,1))
_LumFcCompl_ObjectIdentity=ObjectIdentity
lumFcCompl=_LumFcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,22,1,2))
_LumFcMIBObjects_ObjectIdentity=ObjectIdentity
lumFcMIBObjects=_LumFcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,22,2))
_FcGeneral_ObjectIdentity=ObjectIdentity
fcGeneral=_FcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,22,2,1))
_FcGeneralLastChangeTime_Type=DateAndTime
_FcGeneralLastChangeTime_Object=MibScalar
fcGeneralLastChangeTime=_FcGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,22,2,1,1),_FcGeneralLastChangeTime_Type())
fcGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fcGeneralLastChangeTime.setStatus(_B)
_FcGeneralStateLastChangeTime_Type=DateAndTime
_FcGeneralStateLastChangeTime_Object=MibScalar
fcGeneralStateLastChangeTime=_FcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,22,2,1,2),_FcGeneralStateLastChangeTime_Type())
fcGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fcGeneralStateLastChangeTime.setStatus(_B)
_FcGeneralFcIfTableSize_Type=Unsigned32
_FcGeneralFcIfTableSize_Object=MibScalar
fcGeneralFcIfTableSize=_FcGeneralFcIfTableSize_Object((1,3,6,1,4,1,8708,2,22,2,1,3),_FcGeneralFcIfTableSize_Type())
fcGeneralFcIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:fcGeneralFcIfTableSize.setStatus(_B)
_FcIfList_ObjectIdentity=ObjectIdentity
fcIfList=_FcIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,22,2,2))
_FcIfTable_Object=MibTable
fcIfTable=_FcIfTable_Object((1,3,6,1,4,1,8708,2,22,2,2,1))
if mibBuilder.loadTexts:fcIfTable.setStatus(_B)
_FcIfEntry_Object=MibTableRow
fcIfEntry=_FcIfEntry_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1))
fcIfEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:fcIfEntry.setStatus(_B)
class _FcIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcIfIndex_Type.__name__=_N
_FcIfIndex_Object=MibTableColumn
fcIfIndex=_FcIfIndex_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,1),_FcIfIndex_Type())
fcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfIndex.setStatus(_B)
_FcIfName_Type=MgmtNameString
_FcIfName_Object=MibTableColumn
fcIfName=_FcIfName_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,2),_FcIfName_Type())
fcIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfName.setStatus(_B)
class _FcIfDescr_Type(DisplayString):defaultValue=OctetString('')
_FcIfDescr_Type.__name__=_m
_FcIfDescr_Object=MibTableColumn
fcIfDescr=_FcIfDescr_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,3),_FcIfDescr_Type())
fcIfDescr.setMaxAccess(_L)
if mibBuilder.loadTexts:fcIfDescr.setStatus(_B)
_FcIfSubrack_Type=SubrackNumber
_FcIfSubrack_Object=MibTableColumn
fcIfSubrack=_FcIfSubrack_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,4),_FcIfSubrack_Type())
fcIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfSubrack.setStatus(_B)
_FcIfSlot_Type=SlotNumber
_FcIfSlot_Object=MibTableColumn
fcIfSlot=_FcIfSlot_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,5),_FcIfSlot_Type())
fcIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfSlot.setStatus(_B)
_FcIfTxPort_Type=PortNumber
_FcIfTxPort_Object=MibTableColumn
fcIfTxPort=_FcIfTxPort_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,6),_FcIfTxPort_Type())
fcIfTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfTxPort.setStatus(_B)
_FcIfRxPort_Type=PortNumber
_FcIfRxPort_Object=MibTableColumn
fcIfRxPort=_FcIfRxPort_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,7),_FcIfRxPort_Type())
fcIfRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfRxPort.setStatus(_B)
class _FcIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FcIfInvPhysIndexOrZero_Type.__name__=_N
_FcIfInvPhysIndexOrZero_Object=MibTableColumn
fcIfInvPhysIndexOrZero=_FcIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,8),_FcIfInvPhysIndexOrZero_Type())
fcIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfInvPhysIndexOrZero.setStatus(_B)
class _FcIfFormat_Type(FcSignalFormat):defaultValue=1
_FcIfFormat_Type.__name__=_n
_FcIfFormat_Object=MibTableColumn
fcIfFormat=_FcIfFormat_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,9),_FcIfFormat_Type())
fcIfFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfFormat.setStatus(_B)
class _FcIfHighSpeed_Type(Gauge32):defaultValue=1000;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,2000))
_FcIfHighSpeed_Type.__name__=_l
_FcIfHighSpeed_Object=MibTableColumn
fcIfHighSpeed=_FcIfHighSpeed_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,10),_FcIfHighSpeed_Type())
fcIfHighSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfHighSpeed.setStatus(_B)
class _FcIfAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_FcIfAdminStatus_Type.__name__=_j
_FcIfAdminStatus_Object=MibTableColumn
fcIfAdminStatus=_FcIfAdminStatus_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,11),_FcIfAdminStatus_Type())
fcIfAdminStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fcIfAdminStatus.setStatus(_B)
class _FcIfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_FcIfOperStatus_Type.__name__=_k
_FcIfOperStatus_Object=MibTableColumn
fcIfOperStatus=_FcIfOperStatus_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,12),_FcIfOperStatus_Type())
fcIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfOperStatus.setStatus(_B)
class _FcIfLaserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_FcIfLaserStatus_Type.__name__=_E
_FcIfLaserStatus_Object=MibTableColumn
fcIfLaserStatus=_FcIfLaserStatus_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,13),_FcIfLaserStatus_Type())
fcIfLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfLaserStatus.setStatus(_B)
class _FcIfTxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('degraded',2),('up',3)))
_FcIfTxSignalStatus_Type.__name__=_E
_FcIfTxSignalStatus_Object=MibTableColumn
fcIfTxSignalStatus=_FcIfTxSignalStatus_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,14),_FcIfTxSignalStatus_Type())
fcIfTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfTxSignalStatus.setStatus(_B)
_FcIfLossOfSignal_Type=FaultStatus
_FcIfLossOfSignal_Object=MibTableColumn
fcIfLossOfSignal=_FcIfLossOfSignal_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,15),_FcIfLossOfSignal_Type())
fcIfLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfLossOfSignal.setStatus(_B)
_FcIfLossOfSync_Type=FaultStatus
_FcIfLossOfSync_Object=MibTableColumn
fcIfLossOfSync=_FcIfLossOfSync_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,16),_FcIfLossOfSync_Type())
fcIfLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfLossOfSync.setStatus(_B)
_FcIfAuAlarmIndicationSignalW2C_Type=FaultStatus
_FcIfAuAlarmIndicationSignalW2C_Object=MibTableColumn
fcIfAuAlarmIndicationSignalW2C=_FcIfAuAlarmIndicationSignalW2C_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,17),_FcIfAuAlarmIndicationSignalW2C_Type())
fcIfAuAlarmIndicationSignalW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfAuAlarmIndicationSignalW2C.setStatus(_B)
class _FcIfForwardAls_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FcIfForwardAls_Type.__name__=_E
_FcIfForwardAls_Object=MibTableColumn
fcIfForwardAls=_FcIfForwardAls_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,18),_FcIfForwardAls_Type())
fcIfForwardAls.setMaxAccess(_L)
if mibBuilder.loadTexts:fcIfForwardAls.setStatus(_B)
class _FcIfSuppressRemoteAlarms_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FcIfSuppressRemoteAlarms_Type.__name__=_E
_FcIfSuppressRemoteAlarms_Object=MibTableColumn
fcIfSuppressRemoteAlarms=_FcIfSuppressRemoteAlarms_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,19),_FcIfSuppressRemoteAlarms_Type())
fcIfSuppressRemoteAlarms.setMaxAccess(_L)
if mibBuilder.loadTexts:fcIfSuppressRemoteAlarms.setStatus(_B)
class _FcIfFarEndLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FcIfFarEndLoopback_Type.__name__=_E
_FcIfFarEndLoopback_Object=MibTableColumn
fcIfFarEndLoopback=_FcIfFarEndLoopback_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,20),_FcIfFarEndLoopback_Type())
fcIfFarEndLoopback.setMaxAccess(_L)
if mibBuilder.loadTexts:fcIfFarEndLoopback.setStatus(_B)
class _FcIfEntityId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FcIfEntityId_Type.__name__=_N
_FcIfEntityId_Object=MibTableColumn
fcIfEntityId=_FcIfEntityId_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,21),_FcIfEntityId_Type())
fcIfEntityId.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfEntityId.setStatus(_B)
_FcIfObjectProperty_Type=ObjectProperty
_FcIfObjectProperty_Object=MibTableColumn
fcIfObjectProperty=_FcIfObjectProperty_Object((1,3,6,1,4,1,8708,2,22,2,2,1,1,22),_FcIfObjectProperty_Type())
fcIfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:fcIfObjectProperty.setStatus(_B)
_LumentisFcNotifications_ObjectIdentity=ObjectIdentity
lumentisFcNotifications=_LumentisFcNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,22,2,3))
_FcNotifyPrefix_ObjectIdentity=ObjectIdentity
fcNotifyPrefix=_FcNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,22,2,3,0))
fcGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,22,1,1,1))
fcGeneralGroup.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:fcGeneralGroup.setStatus(_O)
fcIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,22,1,1,2))
fcIfGroup.setObjects(*((_A,_D),(_A,_F),(_A,_U),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_K),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:fcIfGroup.setStatus(_O)
fcGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,22,1,1,4))
fcGeneralGroupV2.setObjects(*((_A,_S),(_A,_T),(_A,_o)))
if mibBuilder.loadTexts:fcGeneralGroupV2.setStatus(_B)
fcIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,22,1,1,5))
fcIfGroupV2.setObjects(*((_A,_D),(_A,_F),(_A,_U),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_K),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_M),(_A,_p)))
if mibBuilder.loadTexts:fcIfGroupV2.setStatus(_B)
fcIfTxSignalStatusDown=NotificationType((1,3,6,1,4,1,8708,2,22,2,3,0,1))
fcIfTxSignalStatusDown.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:fcIfTxSignalStatusDown.setStatus(_B)
fcIfTxSignalStatusUp=NotificationType((1,3,6,1,4,1,8708,2,22,2,3,0,2))
fcIfTxSignalStatusUp.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:fcIfTxSignalStatusUp.setStatus(_B)
fcIfTxSignalStatusDegraded=NotificationType((1,3,6,1,4,1,8708,2,22,2,3,0,3))
fcIfTxSignalStatusDegraded.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:fcIfTxSignalStatusDegraded.setStatus(_B)
fcNotificationGroup=NotificationGroup((1,3,6,1,4,1,8708,2,22,1,1,3))
fcNotificationGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:fcNotificationGroup.setStatus(_B)
lumFcBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,22,1,2,1))
lumFcBasicComplV1.setObjects(*((_A,_t),(_A,_h),(_A,_P)))
if mibBuilder.loadTexts:lumFcBasicComplV1.setStatus(_O)
lumFcBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,22,1,2,2))
lumFcBasicComplV2.setObjects(*((_A,_i),(_A,_h),(_A,_P)))
if mibBuilder.loadTexts:lumFcBasicComplV2.setStatus(_O)
lumFcBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,22,1,2,3))
lumFcBasicComplV3.setObjects(*((_A,_i),(_A,_u),(_A,_P)))
if mibBuilder.loadTexts:lumFcBasicComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_n:FcSignalFormat,'lumFcMIBModule':lumFcMIBModule,'lumFcConfs':lumFcConfs,'lumFcGroups':lumFcGroups,_t:fcGeneralGroup,_h:fcIfGroup,_P:fcNotificationGroup,_i:fcGeneralGroupV2,_u:fcIfGroupV2,'lumFcCompl':lumFcCompl,'lumFcBasicComplV1':lumFcBasicComplV1,'lumFcBasicComplV2':lumFcBasicComplV2,'lumFcBasicComplV3':lumFcBasicComplV3,'lumFcMIBObjects':lumFcMIBObjects,'fcGeneral':fcGeneral,_S:fcGeneralLastChangeTime,_T:fcGeneralStateLastChangeTime,_o:fcGeneralFcIfTableSize,'fcIfList':fcIfList,'fcIfTable':fcIfTable,'fcIfEntry':fcIfEntry,_D:fcIfIndex,_F:fcIfName,_U:fcIfDescr,_G:fcIfSubrack,_H:fcIfSlot,_I:fcIfTxPort,_J:fcIfRxPort,_V:fcIfInvPhysIndexOrZero,_W:fcIfFormat,_X:fcIfHighSpeed,_Z:fcIfAdminStatus,_a:fcIfOperStatus,_Y:fcIfLaserStatus,_K:fcIfTxSignalStatus,_b:fcIfLossOfSignal,_c:fcIfLossOfSync,_d:fcIfAuAlarmIndicationSignalW2C,_e:fcIfForwardAls,_f:fcIfSuppressRemoteAlarms,_g:fcIfFarEndLoopback,_M:fcIfEntityId,_p:fcIfObjectProperty,'lumentisFcNotifications':lumentisFcNotifications,'fcNotifyPrefix':fcNotifyPrefix,_q:fcIfTxSignalStatusDown,_r:fcIfTxSignalStatusUp,_s:fcIfTxSignalStatusDegraded})