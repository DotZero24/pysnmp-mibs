_o='psrMplsLinearProtGroupV1'
_n='psrGeneralGroupV1'
_m='psrMplsLinearProtConfigMismatch'
_l='psrMplsLinearProtCommunicationFailure'
_k='psrMplsLinearProtProtectionDegraded'
_j='psrMplsLinearProtProtectionFailed'
_i='psrMplsLinearProtHoldoffTimer'
_h='psrMplsLinearProtOperatorCommand'
_g='psrMplsLinearProtActivePath'
_f='psrMplsLinearProtPpathSupvType'
_e='psrMplsLinearProtProtectionPathState'
_d='psrMplsLinearProtProtectionPathIndex'
_c='psrMplsLinearProtProtectionPathId'
_b='psrMplsLinearProtWpathSupvType'
_a='psrMplsLinearProtWorkingPathState'
_Z='psrMplsLinearProtWorkingPathIndex'
_Y='psrMplsLinearProtWorkingPathId'
_X='psrMplsLinearProtRemoteEvent'
_W='psrMplsLinearProtLocalEvent'
_V='psrMplsLinearProtState'
_U='psrMplsLinearProtAdminStatus'
_T='psrMplsLinearProtTunnelId'
_S='psrMplsLinearProtName'
_R='psrMplsLinearProtInternalReference'
_Q='psrGeneralPsrMplsLinearProtTableSize'
_P='psrGeneralStateLastChangeTime'
_O='psrGeneralLastChangeTime'
_N='doNotRevert'
_M='waitToRestore'
_L='lockOut'
_K='noRequest'
_J='read-write'
_I='psrMplsLinearProtIndex'
_H='read-create'
_G='unknown'
_F='DisplayString'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='LUM-PSR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumPsrMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumPsrMIB')
FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC','FaultStatus','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','TextualConvention')
lumPsrMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,43))
if mibBuilder.loadTexts:lumPsrMIBModule.setRevisions(('2017-06-15 00:00','2012-12-20 00:00','2012-03-01 00:00'))
class InputRequest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),(_K,2),(_L,3),('forcedSwitch',4),('signalFailProtecting',5),('signalFailWorking',6),('manualSwitch',7),(_M,8),(_N,9),('noConnection',10)))
class PathState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),(_G,3)))
class SupvType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer1',1),('bfd',2)))
_LumPsrConfs_ObjectIdentity=ObjectIdentity
lumPsrConfs=_LumPsrConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,43,1))
_LumPsrGroups_ObjectIdentity=ObjectIdentity
lumPsrGroups=_LumPsrGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,43,1,1))
_LumPsrCompl_ObjectIdentity=ObjectIdentity
lumPsrCompl=_LumPsrCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,43,1,2))
_LumPsrMIBObjects_ObjectIdentity=ObjectIdentity
lumPsrMIBObjects=_LumPsrMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,43,2))
_PsrGeneral_ObjectIdentity=ObjectIdentity
psrGeneral=_PsrGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,43,2,1))
_PsrGeneralLastChangeTime_Type=DateAndTime
_PsrGeneralLastChangeTime_Object=MibScalar
psrGeneralLastChangeTime=_PsrGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,43,2,1,1),_PsrGeneralLastChangeTime_Type())
psrGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:psrGeneralLastChangeTime.setStatus(_A)
_PsrGeneralStateLastChangeTime_Type=DateAndTime
_PsrGeneralStateLastChangeTime_Object=MibScalar
psrGeneralStateLastChangeTime=_PsrGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,43,2,1,2),_PsrGeneralStateLastChangeTime_Type())
psrGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:psrGeneralStateLastChangeTime.setStatus(_A)
_PsrGeneralPsrMplsLinearProtTableSize_Type=Unsigned32
_PsrGeneralPsrMplsLinearProtTableSize_Object=MibScalar
psrGeneralPsrMplsLinearProtTableSize=_PsrGeneralPsrMplsLinearProtTableSize_Object((1,3,6,1,4,1,8708,2,43,2,1,9),_PsrGeneralPsrMplsLinearProtTableSize_Type())
psrGeneralPsrMplsLinearProtTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:psrGeneralPsrMplsLinearProtTableSize.setStatus(_A)
_PsrMplsLinearProtList_ObjectIdentity=ObjectIdentity
psrMplsLinearProtList=_PsrMplsLinearProtList_ObjectIdentity((1,3,6,1,4,1,8708,2,43,2,2))
_PsrMplsLinearProtTable_Object=MibTable
psrMplsLinearProtTable=_PsrMplsLinearProtTable_Object((1,3,6,1,4,1,8708,2,43,2,2,1))
if mibBuilder.loadTexts:psrMplsLinearProtTable.setStatus(_A)
_PsrMplsLinearProtEntry_Object=MibTableRow
psrMplsLinearProtEntry=_PsrMplsLinearProtEntry_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1))
psrMplsLinearProtEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:psrMplsLinearProtEntry.setStatus(_A)
class _PsrMplsLinearProtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsrMplsLinearProtIndex_Type.__name__=_D
_PsrMplsLinearProtIndex_Object=MibTableColumn
psrMplsLinearProtIndex=_PsrMplsLinearProtIndex_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,1),_PsrMplsLinearProtIndex_Type())
psrMplsLinearProtIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtIndex.setStatus(_A)
class _PsrMplsLinearProtInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PsrMplsLinearProtInternalReference_Type.__name__=_D
_PsrMplsLinearProtInternalReference_Object=MibTableColumn
psrMplsLinearProtInternalReference=_PsrMplsLinearProtInternalReference_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,2),_PsrMplsLinearProtInternalReference_Type())
psrMplsLinearProtInternalReference.setMaxAccess(_H)
if mibBuilder.loadTexts:psrMplsLinearProtInternalReference.setStatus(_A)
_PsrMplsLinearProtName_Type=MgmtNameString
_PsrMplsLinearProtName_Object=MibTableColumn
psrMplsLinearProtName=_PsrMplsLinearProtName_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,3),_PsrMplsLinearProtName_Type())
psrMplsLinearProtName.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtName.setStatus(_A)
class _PsrMplsLinearProtTunnelId_Type(DisplayString):defaultValue=OctetString('')
_PsrMplsLinearProtTunnelId_Type.__name__=_F
_PsrMplsLinearProtTunnelId_Object=MibTableColumn
psrMplsLinearProtTunnelId=_PsrMplsLinearProtTunnelId_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,4),_PsrMplsLinearProtTunnelId_Type())
psrMplsLinearProtTunnelId.setMaxAccess(_H)
if mibBuilder.loadTexts:psrMplsLinearProtTunnelId.setStatus(_A)
class _PsrMplsLinearProtAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_PsrMplsLinearProtAdminStatus_Type.__name__=_E
_PsrMplsLinearProtAdminStatus_Object=MibTableColumn
psrMplsLinearProtAdminStatus=_PsrMplsLinearProtAdminStatus_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,5),_PsrMplsLinearProtAdminStatus_Type())
psrMplsLinearProtAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:psrMplsLinearProtAdminStatus.setStatus(_A)
class _PsrMplsLinearProtState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('normal',1),('protectionPathUnavailable',2),('workingPathFailure',3),('administrative',4),(_M,5),(_N,6),(_G,7)))
_PsrMplsLinearProtState_Type.__name__=_E
_PsrMplsLinearProtState_Object=MibTableColumn
psrMplsLinearProtState=_PsrMplsLinearProtState_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,6),_PsrMplsLinearProtState_Type())
psrMplsLinearProtState.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtState.setStatus(_A)
_PsrMplsLinearProtLocalEvent_Type=InputRequest
_PsrMplsLinearProtLocalEvent_Object=MibTableColumn
psrMplsLinearProtLocalEvent=_PsrMplsLinearProtLocalEvent_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,7),_PsrMplsLinearProtLocalEvent_Type())
psrMplsLinearProtLocalEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtLocalEvent.setStatus(_A)
_PsrMplsLinearProtRemoteEvent_Type=InputRequest
_PsrMplsLinearProtRemoteEvent_Object=MibTableColumn
psrMplsLinearProtRemoteEvent=_PsrMplsLinearProtRemoteEvent_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,8),_PsrMplsLinearProtRemoteEvent_Type())
psrMplsLinearProtRemoteEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtRemoteEvent.setStatus(_A)
class _PsrMplsLinearProtWorkingPathId_Type(DisplayString):defaultValue=OctetString('')
_PsrMplsLinearProtWorkingPathId_Type.__name__=_F
_PsrMplsLinearProtWorkingPathId_Object=MibTableColumn
psrMplsLinearProtWorkingPathId=_PsrMplsLinearProtWorkingPathId_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,9),_PsrMplsLinearProtWorkingPathId_Type())
psrMplsLinearProtWorkingPathId.setMaxAccess(_H)
if mibBuilder.loadTexts:psrMplsLinearProtWorkingPathId.setStatus(_A)
class _PsrMplsLinearProtWorkingPathIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsrMplsLinearProtWorkingPathIndex_Type.__name__=_D
_PsrMplsLinearProtWorkingPathIndex_Object=MibTableColumn
psrMplsLinearProtWorkingPathIndex=_PsrMplsLinearProtWorkingPathIndex_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,10),_PsrMplsLinearProtWorkingPathIndex_Type())
psrMplsLinearProtWorkingPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtWorkingPathIndex.setStatus(_A)
_PsrMplsLinearProtWorkingPathState_Type=PathState
_PsrMplsLinearProtWorkingPathState_Object=MibTableColumn
psrMplsLinearProtWorkingPathState=_PsrMplsLinearProtWorkingPathState_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,11),_PsrMplsLinearProtWorkingPathState_Type())
psrMplsLinearProtWorkingPathState.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtWorkingPathState.setStatus(_A)
_PsrMplsLinearProtWpathSupvType_Type=SupvType
_PsrMplsLinearProtWpathSupvType_Object=MibTableColumn
psrMplsLinearProtWpathSupvType=_PsrMplsLinearProtWpathSupvType_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,12),_PsrMplsLinearProtWpathSupvType_Type())
psrMplsLinearProtWpathSupvType.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtWpathSupvType.setStatus(_A)
class _PsrMplsLinearProtProtectionPathId_Type(DisplayString):defaultValue=OctetString('')
_PsrMplsLinearProtProtectionPathId_Type.__name__=_F
_PsrMplsLinearProtProtectionPathId_Object=MibTableColumn
psrMplsLinearProtProtectionPathId=_PsrMplsLinearProtProtectionPathId_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,13),_PsrMplsLinearProtProtectionPathId_Type())
psrMplsLinearProtProtectionPathId.setMaxAccess(_H)
if mibBuilder.loadTexts:psrMplsLinearProtProtectionPathId.setStatus(_A)
class _PsrMplsLinearProtProtectionPathIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PsrMplsLinearProtProtectionPathIndex_Type.__name__=_D
_PsrMplsLinearProtProtectionPathIndex_Object=MibTableColumn
psrMplsLinearProtProtectionPathIndex=_PsrMplsLinearProtProtectionPathIndex_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,14),_PsrMplsLinearProtProtectionPathIndex_Type())
psrMplsLinearProtProtectionPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtProtectionPathIndex.setStatus(_A)
_PsrMplsLinearProtProtectionPathState_Type=PathState
_PsrMplsLinearProtProtectionPathState_Object=MibTableColumn
psrMplsLinearProtProtectionPathState=_PsrMplsLinearProtProtectionPathState_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,15),_PsrMplsLinearProtProtectionPathState_Type())
psrMplsLinearProtProtectionPathState.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtProtectionPathState.setStatus(_A)
_PsrMplsLinearProtPpathSupvType_Type=SupvType
_PsrMplsLinearProtPpathSupvType_Object=MibTableColumn
psrMplsLinearProtPpathSupvType=_PsrMplsLinearProtPpathSupvType_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,16),_PsrMplsLinearProtPpathSupvType_Type())
psrMplsLinearProtPpathSupvType.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtPpathSupvType.setStatus(_A)
class _PsrMplsLinearProtActivePath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('workingPath',1),('protectionPath',2),('none',3),(_G,4)))
_PsrMplsLinearProtActivePath_Type.__name__=_E
_PsrMplsLinearProtActivePath_Object=MibTableColumn
psrMplsLinearProtActivePath=_PsrMplsLinearProtActivePath_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,17),_PsrMplsLinearProtActivePath_Type())
psrMplsLinearProtActivePath.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtActivePath.setStatus(_A)
class _PsrMplsLinearProtOperatorCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),('forced',3),('manual',4)))
_PsrMplsLinearProtOperatorCommand_Type.__name__=_E
_PsrMplsLinearProtOperatorCommand_Object=MibTableColumn
psrMplsLinearProtOperatorCommand=_PsrMplsLinearProtOperatorCommand_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,18),_PsrMplsLinearProtOperatorCommand_Type())
psrMplsLinearProtOperatorCommand.setMaxAccess(_J)
if mibBuilder.loadTexts:psrMplsLinearProtOperatorCommand.setStatus(_A)
class _PsrMplsLinearProtHoldoffTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_PsrMplsLinearProtHoldoffTimer_Type.__name__=_D
_PsrMplsLinearProtHoldoffTimer_Object=MibTableColumn
psrMplsLinearProtHoldoffTimer=_PsrMplsLinearProtHoldoffTimer_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,19),_PsrMplsLinearProtHoldoffTimer_Type())
psrMplsLinearProtHoldoffTimer.setMaxAccess(_J)
if mibBuilder.loadTexts:psrMplsLinearProtHoldoffTimer.setStatus(_A)
_PsrMplsLinearProtProtectionFailed_Type=FaultStatus
_PsrMplsLinearProtProtectionFailed_Object=MibTableColumn
psrMplsLinearProtProtectionFailed=_PsrMplsLinearProtProtectionFailed_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,20),_PsrMplsLinearProtProtectionFailed_Type())
psrMplsLinearProtProtectionFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtProtectionFailed.setStatus(_A)
_PsrMplsLinearProtProtectionDegraded_Type=FaultStatus
_PsrMplsLinearProtProtectionDegraded_Object=MibTableColumn
psrMplsLinearProtProtectionDegraded=_PsrMplsLinearProtProtectionDegraded_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,21),_PsrMplsLinearProtProtectionDegraded_Type())
psrMplsLinearProtProtectionDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtProtectionDegraded.setStatus(_A)
_PsrMplsLinearProtCommunicationFailure_Type=FaultStatus
_PsrMplsLinearProtCommunicationFailure_Object=MibTableColumn
psrMplsLinearProtCommunicationFailure=_PsrMplsLinearProtCommunicationFailure_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,22),_PsrMplsLinearProtCommunicationFailure_Type())
psrMplsLinearProtCommunicationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtCommunicationFailure.setStatus(_A)
_PsrMplsLinearProtConfigMismatch_Type=FaultStatus
_PsrMplsLinearProtConfigMismatch_Object=MibTableColumn
psrMplsLinearProtConfigMismatch=_PsrMplsLinearProtConfigMismatch_Object((1,3,6,1,4,1,8708,2,43,2,2,1,1,23),_PsrMplsLinearProtConfigMismatch_Type())
psrMplsLinearProtConfigMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:psrMplsLinearProtConfigMismatch.setStatus(_A)
psrGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,43,1,1,1))
psrGeneralGroupV1.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:psrGeneralGroupV1.setStatus(_A)
psrMplsLinearProtGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,43,1,1,2))
psrMplsLinearProtGroupV1.setObjects(*((_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:psrMplsLinearProtGroupV1.setStatus(_A)
lumPsrBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,43,1,2,1))
lumPsrBasicComplV1.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:lumPsrBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'InputRequest':InputRequest,'PathState':PathState,'SupvType':SupvType,'lumPsrMIBModule':lumPsrMIBModule,'lumPsrConfs':lumPsrConfs,'lumPsrGroups':lumPsrGroups,_n:psrGeneralGroupV1,_o:psrMplsLinearProtGroupV1,'lumPsrCompl':lumPsrCompl,'lumPsrBasicComplV1':lumPsrBasicComplV1,'lumPsrMIBObjects':lumPsrMIBObjects,'psrGeneral':psrGeneral,_O:psrGeneralLastChangeTime,_P:psrGeneralStateLastChangeTime,_Q:psrGeneralPsrMplsLinearProtTableSize,'psrMplsLinearProtList':psrMplsLinearProtList,'psrMplsLinearProtTable':psrMplsLinearProtTable,'psrMplsLinearProtEntry':psrMplsLinearProtEntry,_I:psrMplsLinearProtIndex,_R:psrMplsLinearProtInternalReference,_S:psrMplsLinearProtName,_T:psrMplsLinearProtTunnelId,_U:psrMplsLinearProtAdminStatus,_V:psrMplsLinearProtState,_W:psrMplsLinearProtLocalEvent,_X:psrMplsLinearProtRemoteEvent,_Y:psrMplsLinearProtWorkingPathId,_Z:psrMplsLinearProtWorkingPathIndex,_a:psrMplsLinearProtWorkingPathState,_b:psrMplsLinearProtWpathSupvType,_c:psrMplsLinearProtProtectionPathId,_d:psrMplsLinearProtProtectionPathIndex,_e:psrMplsLinearProtProtectionPathState,_f:psrMplsLinearProtPpathSupvType,_g:psrMplsLinearProtActivePath,_h:psrMplsLinearProtOperatorCommand,_i:psrMplsLinearProtHoldoffTimer,_j:psrMplsLinearProtProtectionFailed,_k:psrMplsLinearProtProtectionDegraded,_l:psrMplsLinearProtCommunicationFailure,_m:psrMplsLinearProtConfigMismatch})