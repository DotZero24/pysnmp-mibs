_v='ieee8021TeipsV2CandidatePsGroup'
_u='ieee8021TeipsV2IpgConfigOptGroup'
_t='ieee8021TeipsV2NotificationsGroup'
_s='ieee8021TeipsV2IpgConfigManGroup'
_r='ieee8021TeipsV2IpgTesiGroup'
_q='ieee8021TeipsV2IpgGroup'
_p='ieee8021TeipsV2IpgAdminFailure'
_o='ieee8021TeipsV2IpgConfigHoldOff'
_n='ieee8021TeipsV2IpgM1ConfigState'
_m='ieee8021TeipsV2IpgConfigMWTR'
_l='ieee8021TeipsV2IpgConfigWTR'
_k='ieee8021TeipsV2IpgConfigStorageType'
_j='ieee8021TeipsV2IpgConfigNotifyEnable'
_i='ieee8021TeipsV2IpgConfigActiveRequests'
_h='ieee8021TeipsV2IpgConfigCommandAdmin'
_g='ieee8021TeipsV2TesiRowStatus'
_f='ieee8021TeipsV2TesiStorageType'
_e='ieee8021TeipsV2TesiId'
_d='ieee8021TeipsV2CandidatePsRowStatus'
_c='ieee8021TeipsV2CandidatePsStorageType'
_b='ieee8021TeipsV2CandidatePsOper'
_a='ieee8021TeipsV2CandidatePsPort'
_Z='ieee8021TeipsV2CandidatePsMA'
_Y='ieee8021TeipsV2IpgRowStatus'
_X='ieee8021TeipsV2IpgStorageType'
_W='ieee8021TeipsV2IpgProtectionPortNumber'
_V='ieee8021TeipsV2IpgWorkingPortNumber'
_U='ieee8021TeipsV2IpgProtectionMA'
_T='ieee8021TeipsV2IpgWorkingMA'
_S='minutes'
_R='ieee8021TeipsV2CandidatePsIndex'
_Q='ieee8021TeipsV2TesiIndex'
_P='TruthValue'
_O='IEEE8021TeipsIpgConfigAdmin'
_N='ieee8021TeipsV2IpgConfigCommandLast'
_M='ieee8021TeipsV2IpgConfigCommandStatus'
_L='ieee8021TeipsV2IpgConfigState'
_K='not-accessible'
_J='Integer32'
_I='ieee8021BridgeBaseComponentId'
_H='IEEE8021-BRIDGE-MIB'
_G='ieee8021TeipsV2Ipgid'
_F='StorageType'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='IEEE8021-TEIPS-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBaseComponentId,=mibBuilder.importSymbols(_H,_I)
IEEE8021BridgePortNumber,IEEE8021PbbTeTSidId,IEEE8021TeipsIpgConfigActiveRequests,IEEE8021TeipsIpgConfigAdmin,IEEE8021TeipsIpgid,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber','IEEE8021PbbTeTSidId','IEEE8021TeipsIpgConfigActiveRequests',_O,'IEEE8021TeipsIpgid','ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention',_P)
ieee8021TeipsV2Mib=ModuleIdentity((1,3,111,2,802,1,1,27))
if mibBuilder.loadTexts:ieee8021TeipsV2Mib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-08-17 00:00'))
_Ieee8021TeipsV2Notifications_ObjectIdentity=ObjectIdentity
ieee8021TeipsV2Notifications=_Ieee8021TeipsV2Notifications_ObjectIdentity((1,3,111,2,802,1,1,27,0))
_Ieee8021TeipsV2Objects_ObjectIdentity=ObjectIdentity
ieee8021TeipsV2Objects=_Ieee8021TeipsV2Objects_ObjectIdentity((1,3,111,2,802,1,1,27,1))
_Ieee8021TeipsV2IpgTable_Object=MibTable
ieee8021TeipsV2IpgTable=_Ieee8021TeipsV2IpgTable_Object((1,3,111,2,802,1,1,27,1,1))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgTable.setStatus(_A)
_Ieee8021TeipsV2IpgEntry_Object=MibTableRow
ieee8021TeipsV2IpgEntry=_Ieee8021TeipsV2IpgEntry_Object((1,3,111,2,802,1,1,27,1,1,1))
ieee8021TeipsV2IpgEntry.setIndexNames((0,_H,_I),(0,_B,_G))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgEntry.setStatus(_A)
_Ieee8021TeipsV2Ipgid_Type=IEEE8021TeipsIpgid
_Ieee8021TeipsV2Ipgid_Object=MibTableColumn
ieee8021TeipsV2Ipgid=_Ieee8021TeipsV2Ipgid_Object((1,3,111,2,802,1,1,27,1,1,1,1),_Ieee8021TeipsV2Ipgid_Type())
ieee8021TeipsV2Ipgid.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsV2Ipgid.setStatus(_A)
_Ieee8021TeipsV2IpgWorkingMA_Type=Unsigned32
_Ieee8021TeipsV2IpgWorkingMA_Object=MibTableColumn
ieee8021TeipsV2IpgWorkingMA=_Ieee8021TeipsV2IpgWorkingMA_Object((1,3,111,2,802,1,1,27,1,1,1,2),_Ieee8021TeipsV2IpgWorkingMA_Type())
ieee8021TeipsV2IpgWorkingMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgWorkingMA.setStatus(_A)
_Ieee8021TeipsV2IpgProtectionMA_Type=Unsigned32
_Ieee8021TeipsV2IpgProtectionMA_Object=MibTableColumn
ieee8021TeipsV2IpgProtectionMA=_Ieee8021TeipsV2IpgProtectionMA_Object((1,3,111,2,802,1,1,27,1,1,1,3),_Ieee8021TeipsV2IpgProtectionMA_Type())
ieee8021TeipsV2IpgProtectionMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgProtectionMA.setStatus(_A)
_Ieee8021TeipsV2IpgWorkingPortNumber_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsV2IpgWorkingPortNumber_Object=MibTableColumn
ieee8021TeipsV2IpgWorkingPortNumber=_Ieee8021TeipsV2IpgWorkingPortNumber_Object((1,3,111,2,802,1,1,27,1,1,1,4),_Ieee8021TeipsV2IpgWorkingPortNumber_Type())
ieee8021TeipsV2IpgWorkingPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgWorkingPortNumber.setStatus(_A)
_Ieee8021TeipsV2IpgProtectionPortNumber_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsV2IpgProtectionPortNumber_Object=MibTableColumn
ieee8021TeipsV2IpgProtectionPortNumber=_Ieee8021TeipsV2IpgProtectionPortNumber_Object((1,3,111,2,802,1,1,27,1,1,1,5),_Ieee8021TeipsV2IpgProtectionPortNumber_Type())
ieee8021TeipsV2IpgProtectionPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgProtectionPortNumber.setStatus(_A)
class _Ieee8021TeipsV2IpgStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsV2IpgStorageType_Type.__name__=_F
_Ieee8021TeipsV2IpgStorageType_Object=MibTableColumn
ieee8021TeipsV2IpgStorageType=_Ieee8021TeipsV2IpgStorageType_Object((1,3,111,2,802,1,1,27,1,1,1,6),_Ieee8021TeipsV2IpgStorageType_Type())
ieee8021TeipsV2IpgStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgStorageType.setStatus(_A)
_Ieee8021TeipsV2IpgRowStatus_Type=RowStatus
_Ieee8021TeipsV2IpgRowStatus_Object=MibTableColumn
ieee8021TeipsV2IpgRowStatus=_Ieee8021TeipsV2IpgRowStatus_Object((1,3,111,2,802,1,1,27,1,1,1,7),_Ieee8021TeipsV2IpgRowStatus_Type())
ieee8021TeipsV2IpgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgRowStatus.setStatus(_A)
_Ieee8021TeipsV2TesiTable_Object=MibTable
ieee8021TeipsV2TesiTable=_Ieee8021TeipsV2TesiTable_Object((1,3,111,2,802,1,1,27,1,2))
if mibBuilder.loadTexts:ieee8021TeipsV2TesiTable.setStatus(_A)
_Ieee8021TeipsV2TesiEntry_Object=MibTableRow
ieee8021TeipsV2TesiEntry=_Ieee8021TeipsV2TesiEntry_Object((1,3,111,2,802,1,1,27,1,2,1))
ieee8021TeipsV2TesiEntry.setIndexNames((0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:ieee8021TeipsV2TesiEntry.setStatus(_A)
class _Ieee8021TeipsV2TesiIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ieee8021TeipsV2TesiIndex_Type.__name__=_E
_Ieee8021TeipsV2TesiIndex_Object=MibTableColumn
ieee8021TeipsV2TesiIndex=_Ieee8021TeipsV2TesiIndex_Object((1,3,111,2,802,1,1,27,1,2,1,1),_Ieee8021TeipsV2TesiIndex_Type())
ieee8021TeipsV2TesiIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsV2TesiIndex.setStatus(_A)
_Ieee8021TeipsV2TesiId_Type=IEEE8021PbbTeTSidId
_Ieee8021TeipsV2TesiId_Object=MibTableColumn
ieee8021TeipsV2TesiId=_Ieee8021TeipsV2TesiId_Object((1,3,111,2,802,1,1,27,1,2,1,2),_Ieee8021TeipsV2TesiId_Type())
ieee8021TeipsV2TesiId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2TesiId.setStatus(_A)
class _Ieee8021TeipsV2TesiStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsV2TesiStorageType_Type.__name__=_F
_Ieee8021TeipsV2TesiStorageType_Object=MibTableColumn
ieee8021TeipsV2TesiStorageType=_Ieee8021TeipsV2TesiStorageType_Object((1,3,111,2,802,1,1,27,1,2,1,3),_Ieee8021TeipsV2TesiStorageType_Type())
ieee8021TeipsV2TesiStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2TesiStorageType.setStatus(_A)
_Ieee8021TeipsV2TesiRowStatus_Type=RowStatus
_Ieee8021TeipsV2TesiRowStatus_Object=MibTableColumn
ieee8021TeipsV2TesiRowStatus=_Ieee8021TeipsV2TesiRowStatus_Object((1,3,111,2,802,1,1,27,1,2,1,4),_Ieee8021TeipsV2TesiRowStatus_Type())
ieee8021TeipsV2TesiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2TesiRowStatus.setStatus(_A)
_Ieee8021TeipsV2CandidatePsTable_Object=MibTable
ieee8021TeipsV2CandidatePsTable=_Ieee8021TeipsV2CandidatePsTable_Object((1,3,111,2,802,1,1,27,1,3))
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsTable.setStatus(_A)
_Ieee8021TeipsV2CandidatePsEntry_Object=MibTableRow
ieee8021TeipsV2CandidatePsEntry=_Ieee8021TeipsV2CandidatePsEntry_Object((1,3,111,2,802,1,1,27,1,3,1))
ieee8021TeipsV2CandidatePsEntry.setIndexNames((0,_B,_G),(0,_B,_R))
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsEntry.setStatus(_A)
class _Ieee8021TeipsV2CandidatePsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ieee8021TeipsV2CandidatePsIndex_Type.__name__=_E
_Ieee8021TeipsV2CandidatePsIndex_Object=MibTableColumn
ieee8021TeipsV2CandidatePsIndex=_Ieee8021TeipsV2CandidatePsIndex_Object((1,3,111,2,802,1,1,27,1,3,1,1),_Ieee8021TeipsV2CandidatePsIndex_Type())
ieee8021TeipsV2CandidatePsIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsIndex.setStatus(_A)
_Ieee8021TeipsV2CandidatePsMA_Type=Unsigned32
_Ieee8021TeipsV2CandidatePsMA_Object=MibTableColumn
ieee8021TeipsV2CandidatePsMA=_Ieee8021TeipsV2CandidatePsMA_Object((1,3,111,2,802,1,1,27,1,3,1,2),_Ieee8021TeipsV2CandidatePsMA_Type())
ieee8021TeipsV2CandidatePsMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsMA.setStatus(_A)
_Ieee8021TeipsV2CandidatePsPort_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsV2CandidatePsPort_Object=MibTableColumn
ieee8021TeipsV2CandidatePsPort=_Ieee8021TeipsV2CandidatePsPort_Object((1,3,111,2,802,1,1,27,1,3,1,3),_Ieee8021TeipsV2CandidatePsPort_Type())
ieee8021TeipsV2CandidatePsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsPort.setStatus(_A)
_Ieee8021TeipsV2CandidatePsOper_Type=TruthValue
_Ieee8021TeipsV2CandidatePsOper_Object=MibTableColumn
ieee8021TeipsV2CandidatePsOper=_Ieee8021TeipsV2CandidatePsOper_Object((1,3,111,2,802,1,1,27,1,3,1,4),_Ieee8021TeipsV2CandidatePsOper_Type())
ieee8021TeipsV2CandidatePsOper.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsOper.setStatus(_A)
class _Ieee8021TeipsV2CandidatePsStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsV2CandidatePsStorageType_Type.__name__=_F
_Ieee8021TeipsV2CandidatePsStorageType_Object=MibTableColumn
ieee8021TeipsV2CandidatePsStorageType=_Ieee8021TeipsV2CandidatePsStorageType_Object((1,3,111,2,802,1,1,27,1,3,1,5),_Ieee8021TeipsV2CandidatePsStorageType_Type())
ieee8021TeipsV2CandidatePsStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsStorageType.setStatus(_A)
_Ieee8021TeipsV2CandidatePsRowStatus_Type=RowStatus
_Ieee8021TeipsV2CandidatePsRowStatus_Object=MibTableColumn
ieee8021TeipsV2CandidatePsRowStatus=_Ieee8021TeipsV2CandidatePsRowStatus_Object((1,3,111,2,802,1,1,27,1,3,1,6),_Ieee8021TeipsV2CandidatePsRowStatus_Type())
ieee8021TeipsV2CandidatePsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsRowStatus.setStatus(_A)
_Ieee8021TeipsV2IpgConfigTable_Object=MibTable
ieee8021TeipsV2IpgConfigTable=_Ieee8021TeipsV2IpgConfigTable_Object((1,3,111,2,802,1,1,27,1,4))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigTable.setStatus(_A)
_Ieee8021TeipsV2IpgConfigEntry_Object=MibTableRow
ieee8021TeipsV2IpgConfigEntry=_Ieee8021TeipsV2IpgConfigEntry_Object((1,3,111,2,802,1,1,27,1,4,1))
ieee8021TeipsV2IpgConfigEntry.setIndexNames((0,_H,_I),(0,_B,_G))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigEntry.setStatus(_A)
class _Ieee8021TeipsV2IpgConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('workingSegment',1),('protectionSegment',2),('waitToRestore',3),('protAdmin',4)))
_Ieee8021TeipsV2IpgConfigState_Type.__name__=_J
_Ieee8021TeipsV2IpgConfigState_Object=MibTableColumn
ieee8021TeipsV2IpgConfigState=_Ieee8021TeipsV2IpgConfigState_Object((1,3,111,2,802,1,1,27,1,4,1,1),_Ieee8021TeipsV2IpgConfigState_Type())
ieee8021TeipsV2IpgConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigState.setStatus(_A)
_Ieee8021TeipsV2IpgConfigCommandStatus_Type=IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsV2IpgConfigCommandStatus_Object=MibTableColumn
ieee8021TeipsV2IpgConfigCommandStatus=_Ieee8021TeipsV2IpgConfigCommandStatus_Object((1,3,111,2,802,1,1,27,1,4,1,2),_Ieee8021TeipsV2IpgConfigCommandStatus_Type())
ieee8021TeipsV2IpgConfigCommandStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigCommandStatus.setStatus(_A)
_Ieee8021TeipsV2IpgConfigCommandLast_Type=IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsV2IpgConfigCommandLast_Object=MibTableColumn
ieee8021TeipsV2IpgConfigCommandLast=_Ieee8021TeipsV2IpgConfigCommandLast_Object((1,3,111,2,802,1,1,27,1,4,1,3),_Ieee8021TeipsV2IpgConfigCommandLast_Type())
ieee8021TeipsV2IpgConfigCommandLast.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigCommandLast.setStatus(_A)
class _Ieee8021TeipsV2IpgConfigCommandAdmin_Type(IEEE8021TeipsIpgConfigAdmin):defaultValue=1
_Ieee8021TeipsV2IpgConfigCommandAdmin_Type.__name__=_O
_Ieee8021TeipsV2IpgConfigCommandAdmin_Object=MibTableColumn
ieee8021TeipsV2IpgConfigCommandAdmin=_Ieee8021TeipsV2IpgConfigCommandAdmin_Object((1,3,111,2,802,1,1,27,1,4,1,4),_Ieee8021TeipsV2IpgConfigCommandAdmin_Type())
ieee8021TeipsV2IpgConfigCommandAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigCommandAdmin.setStatus(_A)
_Ieee8021TeipsV2IpgConfigActiveRequests_Type=IEEE8021TeipsIpgConfigActiveRequests
_Ieee8021TeipsV2IpgConfigActiveRequests_Object=MibTableColumn
ieee8021TeipsV2IpgConfigActiveRequests=_Ieee8021TeipsV2IpgConfigActiveRequests_Object((1,3,111,2,802,1,1,27,1,4,1,5),_Ieee8021TeipsV2IpgConfigActiveRequests_Type())
ieee8021TeipsV2IpgConfigActiveRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigActiveRequests.setStatus(_A)
class _Ieee8021TeipsV2IpgConfigWTR_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,12))
_Ieee8021TeipsV2IpgConfigWTR_Type.__name__=_E
_Ieee8021TeipsV2IpgConfigWTR_Object=MibTableColumn
ieee8021TeipsV2IpgConfigWTR=_Ieee8021TeipsV2IpgConfigWTR_Object((1,3,111,2,802,1,1,27,1,4,1,6),_Ieee8021TeipsV2IpgConfigWTR_Type())
ieee8021TeipsV2IpgConfigWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigWTR.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigWTR.setUnits(_S)
class _Ieee8021TeipsV2IpgConfigHoldOff_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ieee8021TeipsV2IpgConfigHoldOff_Type.__name__=_E
_Ieee8021TeipsV2IpgConfigHoldOff_Object=MibTableColumn
ieee8021TeipsV2IpgConfigHoldOff=_Ieee8021TeipsV2IpgConfigHoldOff_Object((1,3,111,2,802,1,1,27,1,4,1,7),_Ieee8021TeipsV2IpgConfigHoldOff_Type())
ieee8021TeipsV2IpgConfigHoldOff.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigHoldOff.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigHoldOff.setUnits('deciseconds')
class _Ieee8021TeipsV2IpgM1ConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('psAssigned',1),('segmentOk',2),('segmentFailed',3),('assignNewPs',4),('revertToBetterPs',5)))
_Ieee8021TeipsV2IpgM1ConfigState_Type.__name__=_J
_Ieee8021TeipsV2IpgM1ConfigState_Object=MibTableColumn
ieee8021TeipsV2IpgM1ConfigState=_Ieee8021TeipsV2IpgM1ConfigState_Object((1,3,111,2,802,1,1,27,1,4,1,8),_Ieee8021TeipsV2IpgM1ConfigState_Type())
ieee8021TeipsV2IpgM1ConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgM1ConfigState.setStatus(_A)
class _Ieee8021TeipsV2IpgConfigMWTR_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,12))
_Ieee8021TeipsV2IpgConfigMWTR_Type.__name__=_E
_Ieee8021TeipsV2IpgConfigMWTR_Object=MibTableColumn
ieee8021TeipsV2IpgConfigMWTR=_Ieee8021TeipsV2IpgConfigMWTR_Object((1,3,111,2,802,1,1,27,1,4,1,9),_Ieee8021TeipsV2IpgConfigMWTR_Type())
ieee8021TeipsV2IpgConfigMWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigMWTR.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigMWTR.setUnits(_S)
class _Ieee8021TeipsV2IpgConfigNotifyEnable_Type(TruthValue):defaultValue=2
_Ieee8021TeipsV2IpgConfigNotifyEnable_Type.__name__=_P
_Ieee8021TeipsV2IpgConfigNotifyEnable_Object=MibTableColumn
ieee8021TeipsV2IpgConfigNotifyEnable=_Ieee8021TeipsV2IpgConfigNotifyEnable_Object((1,3,111,2,802,1,1,27,1,4,1,10),_Ieee8021TeipsV2IpgConfigNotifyEnable_Type())
ieee8021TeipsV2IpgConfigNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigNotifyEnable.setStatus(_A)
class _Ieee8021TeipsV2IpgConfigStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsV2IpgConfigStorageType_Type.__name__=_F
_Ieee8021TeipsV2IpgConfigStorageType_Object=MibTableColumn
ieee8021TeipsV2IpgConfigStorageType=_Ieee8021TeipsV2IpgConfigStorageType_Object((1,3,111,2,802,1,1,27,1,4,1,11),_Ieee8021TeipsV2IpgConfigStorageType_Type())
ieee8021TeipsV2IpgConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigStorageType.setStatus(_A)
_Ieee8021TeipsV2Conformance_ObjectIdentity=ObjectIdentity
ieee8021TeipsV2Conformance=_Ieee8021TeipsV2Conformance_ObjectIdentity((1,3,111,2,802,1,1,27,2))
_Ieee8021TeipsV2Compliances_ObjectIdentity=ObjectIdentity
ieee8021TeipsV2Compliances=_Ieee8021TeipsV2Compliances_ObjectIdentity((1,3,111,2,802,1,1,27,2,1))
_Ieee8021TeipsV2Groups_ObjectIdentity=ObjectIdentity
ieee8021TeipsV2Groups=_Ieee8021TeipsV2Groups_ObjectIdentity((1,3,111,2,802,1,1,27,2,2))
ieee8021TeipsV2IpgGroup=ObjectGroup((1,3,111,2,802,1,1,27,2,2,1))
ieee8021TeipsV2IpgGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgGroup.setStatus(_A)
ieee8021TeipsV2CandidatePsGroup=ObjectGroup((1,3,111,2,802,1,1,27,2,2,2))
ieee8021TeipsV2CandidatePsGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ieee8021TeipsV2CandidatePsGroup.setStatus(_A)
ieee8021TeipsV2IpgTesiGroup=ObjectGroup((1,3,111,2,802,1,1,27,2,2,3))
ieee8021TeipsV2IpgTesiGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgTesiGroup.setStatus(_A)
ieee8021TeipsV2IpgConfigManGroup=ObjectGroup((1,3,111,2,802,1,1,27,2,2,4))
ieee8021TeipsV2IpgConfigManGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigManGroup.setStatus(_A)
ieee8021TeipsV2IpgConfigOptGroup=ObjectGroup((1,3,111,2,802,1,1,27,2,2,5))
ieee8021TeipsV2IpgConfigOptGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgConfigOptGroup.setStatus(_A)
ieee8021TeipsV2IpgAdminFailure=NotificationType((1,3,111,2,802,1,1,27,0,1))
ieee8021TeipsV2IpgAdminFailure.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ieee8021TeipsV2IpgAdminFailure.setStatus(_A)
ieee8021TeipsV2NotificationsGroup=NotificationGroup((1,3,111,2,802,1,1,27,2,2,6))
ieee8021TeipsV2NotificationsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:ieee8021TeipsV2NotificationsGroup.setStatus(_A)
ieee8021TeipsV2Compliance=ModuleCompliance((1,3,111,2,802,1,1,27,2,1,1))
ieee8021TeipsV2Compliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ieee8021TeipsV2Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021TeipsV2Mib':ieee8021TeipsV2Mib,'ieee8021TeipsV2Notifications':ieee8021TeipsV2Notifications,_p:ieee8021TeipsV2IpgAdminFailure,'ieee8021TeipsV2Objects':ieee8021TeipsV2Objects,'ieee8021TeipsV2IpgTable':ieee8021TeipsV2IpgTable,'ieee8021TeipsV2IpgEntry':ieee8021TeipsV2IpgEntry,_G:ieee8021TeipsV2Ipgid,_T:ieee8021TeipsV2IpgWorkingMA,_U:ieee8021TeipsV2IpgProtectionMA,_V:ieee8021TeipsV2IpgWorkingPortNumber,_W:ieee8021TeipsV2IpgProtectionPortNumber,_X:ieee8021TeipsV2IpgStorageType,_Y:ieee8021TeipsV2IpgRowStatus,'ieee8021TeipsV2TesiTable':ieee8021TeipsV2TesiTable,'ieee8021TeipsV2TesiEntry':ieee8021TeipsV2TesiEntry,_Q:ieee8021TeipsV2TesiIndex,_e:ieee8021TeipsV2TesiId,_f:ieee8021TeipsV2TesiStorageType,_g:ieee8021TeipsV2TesiRowStatus,'ieee8021TeipsV2CandidatePsTable':ieee8021TeipsV2CandidatePsTable,'ieee8021TeipsV2CandidatePsEntry':ieee8021TeipsV2CandidatePsEntry,_R:ieee8021TeipsV2CandidatePsIndex,_Z:ieee8021TeipsV2CandidatePsMA,_a:ieee8021TeipsV2CandidatePsPort,_b:ieee8021TeipsV2CandidatePsOper,_c:ieee8021TeipsV2CandidatePsStorageType,_d:ieee8021TeipsV2CandidatePsRowStatus,'ieee8021TeipsV2IpgConfigTable':ieee8021TeipsV2IpgConfigTable,'ieee8021TeipsV2IpgConfigEntry':ieee8021TeipsV2IpgConfigEntry,_L:ieee8021TeipsV2IpgConfigState,_M:ieee8021TeipsV2IpgConfigCommandStatus,_N:ieee8021TeipsV2IpgConfigCommandLast,_h:ieee8021TeipsV2IpgConfigCommandAdmin,_i:ieee8021TeipsV2IpgConfigActiveRequests,_l:ieee8021TeipsV2IpgConfigWTR,_o:ieee8021TeipsV2IpgConfigHoldOff,_n:ieee8021TeipsV2IpgM1ConfigState,_m:ieee8021TeipsV2IpgConfigMWTR,_j:ieee8021TeipsV2IpgConfigNotifyEnable,_k:ieee8021TeipsV2IpgConfigStorageType,'ieee8021TeipsV2Conformance':ieee8021TeipsV2Conformance,'ieee8021TeipsV2Compliances':ieee8021TeipsV2Compliances,'ieee8021TeipsV2Compliance':ieee8021TeipsV2Compliance,'ieee8021TeipsV2Groups':ieee8021TeipsV2Groups,_q:ieee8021TeipsV2IpgGroup,_v:ieee8021TeipsV2CandidatePsGroup,_r:ieee8021TeipsV2IpgTesiGroup,_s:ieee8021TeipsV2IpgConfigManGroup,_u:ieee8021TeipsV2IpgConfigOptGroup,_t:ieee8021TeipsV2NotificationsGroup})