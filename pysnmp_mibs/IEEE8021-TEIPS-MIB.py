_v='ieee8021TeipsCandidatePsGroup'
_u='ieee8021TeipsIpgConfigOptGroup'
_t='ieee8021TeipsNotificationsGroup'
_s='ieee8021TeipsIpgConfigManGroup'
_r='ieee8021TeipsIpgTesiGroup'
_q='ieee8021TeipsIpgGroup'
_p='ieee8021TeipsIpgAdminFailure'
_o='ieee8021TeipsIpgConfigHoldOff'
_n='ieee8021TeipsIpgM1ConfigState'
_m='ieee8021TeipsIpgConfigMWTR'
_l='ieee8021TeipsIpgConfigWTR'
_k='ieee8021TeipsIpgConfigStorageType'
_j='ieee8021TeipsIpgConfigNotifyEnable'
_i='ieee8021TeipsIpgConfigActiveRequests'
_h='ieee8021TeipsIpgConfigCommandAdmin'
_g='ieee8021TeipsTesiRowStatus'
_f='ieee8021TeipsTesiStorageType'
_e='ieee8021TeipsTesiId'
_d='ieee8021TeipsCandidatePsRowStatus'
_c='ieee8021TeipsCandidatePsStorageType'
_b='ieee8021TeipsCandidatePsOper'
_a='ieee8021TeipsCandidatePsPort'
_Z='ieee8021TeipsCandidatePsMA'
_Y='ieee8021TeipsIpgRowStatus'
_X='ieee8021TeipsIpgStorageType'
_W='ieee8021TeipsIpgProtectionPortNumber'
_V='ieee8021TeipsIpgWorkingPortNumber'
_U='ieee8021TeipsIpgProtectionMA'
_T='ieee8021TeipsIpgWorkingMA'
_S='minutes'
_R='ieee8021TeipsCandidatePsIndex'
_Q='ieee8021TeipsTesiIndex'
_P='TruthValue'
_O='IEEE8021TeipsIpgConfigAdmin'
_N='ieee8021TeipsIpgConfigCommandLast'
_M='ieee8021TeipsIpgConfigCommandStatus'
_L='ieee8021TeipsIpgConfigState'
_K='not-accessible'
_J='Integer32'
_I='ieee8021BridgeBaseComponentId'
_H='IEEE8021-BRIDGE-MIB'
_G='ieee8021TeipsIpgid'
_F='StorageType'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='IEEE8021-TEIPS-MIB'
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
ieee8021TeipsMib=ModuleIdentity((1,3,111,2,802,1,1,24))
if mibBuilder.loadTexts:ieee8021TeipsMib.setRevisions(('2011-08-17 00:00',))
_Ieee8021TeipsNotifications_ObjectIdentity=ObjectIdentity
ieee8021TeipsNotifications=_Ieee8021TeipsNotifications_ObjectIdentity((1,3,111,2,802,1,1,24,0))
_Ieee8021TeipsObjects_ObjectIdentity=ObjectIdentity
ieee8021TeipsObjects=_Ieee8021TeipsObjects_ObjectIdentity((1,3,111,2,802,1,1,24,1))
_Ieee8021TeipsIpgTable_Object=MibTable
ieee8021TeipsIpgTable=_Ieee8021TeipsIpgTable_Object((1,3,111,2,802,1,1,24,1,1))
if mibBuilder.loadTexts:ieee8021TeipsIpgTable.setStatus(_A)
_Ieee8021TeipsIpgEntry_Object=MibTableRow
ieee8021TeipsIpgEntry=_Ieee8021TeipsIpgEntry_Object((1,3,111,2,802,1,1,24,1,1,1))
ieee8021TeipsIpgEntry.setIndexNames((0,_H,_I),(0,_B,_G))
if mibBuilder.loadTexts:ieee8021TeipsIpgEntry.setStatus(_A)
_Ieee8021TeipsIpgid_Type=IEEE8021TeipsIpgid
_Ieee8021TeipsIpgid_Object=MibTableColumn
ieee8021TeipsIpgid=_Ieee8021TeipsIpgid_Object((1,3,111,2,802,1,1,24,1,1,1,1),_Ieee8021TeipsIpgid_Type())
ieee8021TeipsIpgid.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsIpgid.setStatus(_A)
_Ieee8021TeipsIpgWorkingMA_Type=Unsigned32
_Ieee8021TeipsIpgWorkingMA_Object=MibTableColumn
ieee8021TeipsIpgWorkingMA=_Ieee8021TeipsIpgWorkingMA_Object((1,3,111,2,802,1,1,24,1,1,1,2),_Ieee8021TeipsIpgWorkingMA_Type())
ieee8021TeipsIpgWorkingMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgWorkingMA.setStatus(_A)
_Ieee8021TeipsIpgProtectionMA_Type=Unsigned32
_Ieee8021TeipsIpgProtectionMA_Object=MibTableColumn
ieee8021TeipsIpgProtectionMA=_Ieee8021TeipsIpgProtectionMA_Object((1,3,111,2,802,1,1,24,1,1,1,3),_Ieee8021TeipsIpgProtectionMA_Type())
ieee8021TeipsIpgProtectionMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgProtectionMA.setStatus(_A)
_Ieee8021TeipsIpgWorkingPortNumber_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsIpgWorkingPortNumber_Object=MibTableColumn
ieee8021TeipsIpgWorkingPortNumber=_Ieee8021TeipsIpgWorkingPortNumber_Object((1,3,111,2,802,1,1,24,1,1,1,4),_Ieee8021TeipsIpgWorkingPortNumber_Type())
ieee8021TeipsIpgWorkingPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgWorkingPortNumber.setStatus(_A)
_Ieee8021TeipsIpgProtectionPortNumber_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsIpgProtectionPortNumber_Object=MibTableColumn
ieee8021TeipsIpgProtectionPortNumber=_Ieee8021TeipsIpgProtectionPortNumber_Object((1,3,111,2,802,1,1,24,1,1,1,5),_Ieee8021TeipsIpgProtectionPortNumber_Type())
ieee8021TeipsIpgProtectionPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgProtectionPortNumber.setStatus(_A)
class _Ieee8021TeipsIpgStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsIpgStorageType_Type.__name__=_F
_Ieee8021TeipsIpgStorageType_Object=MibTableColumn
ieee8021TeipsIpgStorageType=_Ieee8021TeipsIpgStorageType_Object((1,3,111,2,802,1,1,24,1,1,1,6),_Ieee8021TeipsIpgStorageType_Type())
ieee8021TeipsIpgStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgStorageType.setStatus(_A)
_Ieee8021TeipsIpgRowStatus_Type=RowStatus
_Ieee8021TeipsIpgRowStatus_Object=MibTableColumn
ieee8021TeipsIpgRowStatus=_Ieee8021TeipsIpgRowStatus_Object((1,3,111,2,802,1,1,24,1,1,1,7),_Ieee8021TeipsIpgRowStatus_Type())
ieee8021TeipsIpgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgRowStatus.setStatus(_A)
_Ieee8021TeipsTesiTable_Object=MibTable
ieee8021TeipsTesiTable=_Ieee8021TeipsTesiTable_Object((1,3,111,2,802,1,1,24,1,2))
if mibBuilder.loadTexts:ieee8021TeipsTesiTable.setStatus(_A)
_Ieee8021TeipsTesiEntry_Object=MibTableRow
ieee8021TeipsTesiEntry=_Ieee8021TeipsTesiEntry_Object((1,3,111,2,802,1,1,24,1,2,1))
ieee8021TeipsTesiEntry.setIndexNames((0,_B,_G),(0,_B,_Q))
if mibBuilder.loadTexts:ieee8021TeipsTesiEntry.setStatus(_A)
class _Ieee8021TeipsTesiIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ieee8021TeipsTesiIndex_Type.__name__=_E
_Ieee8021TeipsTesiIndex_Object=MibTableColumn
ieee8021TeipsTesiIndex=_Ieee8021TeipsTesiIndex_Object((1,3,111,2,802,1,1,24,1,2,1,1),_Ieee8021TeipsTesiIndex_Type())
ieee8021TeipsTesiIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsTesiIndex.setStatus(_A)
_Ieee8021TeipsTesiId_Type=IEEE8021PbbTeTSidId
_Ieee8021TeipsTesiId_Object=MibTableColumn
ieee8021TeipsTesiId=_Ieee8021TeipsTesiId_Object((1,3,111,2,802,1,1,24,1,2,1,2),_Ieee8021TeipsTesiId_Type())
ieee8021TeipsTesiId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsTesiId.setStatus(_A)
class _Ieee8021TeipsTesiStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsTesiStorageType_Type.__name__=_F
_Ieee8021TeipsTesiStorageType_Object=MibTableColumn
ieee8021TeipsTesiStorageType=_Ieee8021TeipsTesiStorageType_Object((1,3,111,2,802,1,1,24,1,2,1,3),_Ieee8021TeipsTesiStorageType_Type())
ieee8021TeipsTesiStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsTesiStorageType.setStatus(_A)
_Ieee8021TeipsTesiRowStatus_Type=RowStatus
_Ieee8021TeipsTesiRowStatus_Object=MibTableColumn
ieee8021TeipsTesiRowStatus=_Ieee8021TeipsTesiRowStatus_Object((1,3,111,2,802,1,1,24,1,2,1,4),_Ieee8021TeipsTesiRowStatus_Type())
ieee8021TeipsTesiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsTesiRowStatus.setStatus(_A)
_Ieee8021TeipsCandidatePsTable_Object=MibTable
ieee8021TeipsCandidatePsTable=_Ieee8021TeipsCandidatePsTable_Object((1,3,111,2,802,1,1,24,1,3))
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsTable.setStatus(_A)
_Ieee8021TeipsCandidatePsEntry_Object=MibTableRow
ieee8021TeipsCandidatePsEntry=_Ieee8021TeipsCandidatePsEntry_Object((1,3,111,2,802,1,1,24,1,3,1))
ieee8021TeipsCandidatePsEntry.setIndexNames((0,_B,_G),(0,_B,_R))
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsEntry.setStatus(_A)
class _Ieee8021TeipsCandidatePsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ieee8021TeipsCandidatePsIndex_Type.__name__=_E
_Ieee8021TeipsCandidatePsIndex_Object=MibTableColumn
ieee8021TeipsCandidatePsIndex=_Ieee8021TeipsCandidatePsIndex_Object((1,3,111,2,802,1,1,24,1,3,1,1),_Ieee8021TeipsCandidatePsIndex_Type())
ieee8021TeipsCandidatePsIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsIndex.setStatus(_A)
_Ieee8021TeipsCandidatePsMA_Type=Unsigned32
_Ieee8021TeipsCandidatePsMA_Object=MibTableColumn
ieee8021TeipsCandidatePsMA=_Ieee8021TeipsCandidatePsMA_Object((1,3,111,2,802,1,1,24,1,3,1,2),_Ieee8021TeipsCandidatePsMA_Type())
ieee8021TeipsCandidatePsMA.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsMA.setStatus(_A)
_Ieee8021TeipsCandidatePsPort_Type=IEEE8021BridgePortNumber
_Ieee8021TeipsCandidatePsPort_Object=MibTableColumn
ieee8021TeipsCandidatePsPort=_Ieee8021TeipsCandidatePsPort_Object((1,3,111,2,802,1,1,24,1,3,1,3),_Ieee8021TeipsCandidatePsPort_Type())
ieee8021TeipsCandidatePsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsPort.setStatus(_A)
_Ieee8021TeipsCandidatePsOper_Type=TruthValue
_Ieee8021TeipsCandidatePsOper_Object=MibTableColumn
ieee8021TeipsCandidatePsOper=_Ieee8021TeipsCandidatePsOper_Object((1,3,111,2,802,1,1,24,1,3,1,4),_Ieee8021TeipsCandidatePsOper_Type())
ieee8021TeipsCandidatePsOper.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsOper.setStatus(_A)
class _Ieee8021TeipsCandidatePsStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsCandidatePsStorageType_Type.__name__=_F
_Ieee8021TeipsCandidatePsStorageType_Object=MibTableColumn
ieee8021TeipsCandidatePsStorageType=_Ieee8021TeipsCandidatePsStorageType_Object((1,3,111,2,802,1,1,24,1,3,1,5),_Ieee8021TeipsCandidatePsStorageType_Type())
ieee8021TeipsCandidatePsStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsStorageType.setStatus(_A)
_Ieee8021TeipsCandidatePsRowStatus_Type=RowStatus
_Ieee8021TeipsCandidatePsRowStatus_Object=MibTableColumn
ieee8021TeipsCandidatePsRowStatus=_Ieee8021TeipsCandidatePsRowStatus_Object((1,3,111,2,802,1,1,24,1,3,1,6),_Ieee8021TeipsCandidatePsRowStatus_Type())
ieee8021TeipsCandidatePsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsRowStatus.setStatus(_A)
_Ieee8021TeipsIpgConfigTable_Object=MibTable
ieee8021TeipsIpgConfigTable=_Ieee8021TeipsIpgConfigTable_Object((1,3,111,2,802,1,1,24,1,4))
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigTable.setStatus(_A)
_Ieee8021TeipsIpgConfigEntry_Object=MibTableRow
ieee8021TeipsIpgConfigEntry=_Ieee8021TeipsIpgConfigEntry_Object((1,3,111,2,802,1,1,24,1,4,1))
ieee8021TeipsIpgConfigEntry.setIndexNames((0,_H,_I),(0,_B,_G))
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigEntry.setStatus(_A)
class _Ieee8021TeipsIpgConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('workingSegment',1),('protectionSegment',2),('waitToRestore',3),('protAdmin',4)))
_Ieee8021TeipsIpgConfigState_Type.__name__=_J
_Ieee8021TeipsIpgConfigState_Object=MibTableColumn
ieee8021TeipsIpgConfigState=_Ieee8021TeipsIpgConfigState_Object((1,3,111,2,802,1,1,24,1,4,1,1),_Ieee8021TeipsIpgConfigState_Type())
ieee8021TeipsIpgConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigState.setStatus(_A)
_Ieee8021TeipsIpgConfigCommandStatus_Type=IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsIpgConfigCommandStatus_Object=MibTableColumn
ieee8021TeipsIpgConfigCommandStatus=_Ieee8021TeipsIpgConfigCommandStatus_Object((1,3,111,2,802,1,1,24,1,4,1,2),_Ieee8021TeipsIpgConfigCommandStatus_Type())
ieee8021TeipsIpgConfigCommandStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigCommandStatus.setStatus(_A)
_Ieee8021TeipsIpgConfigCommandLast_Type=IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsIpgConfigCommandLast_Object=MibTableColumn
ieee8021TeipsIpgConfigCommandLast=_Ieee8021TeipsIpgConfigCommandLast_Object((1,3,111,2,802,1,1,24,1,4,1,3),_Ieee8021TeipsIpgConfigCommandLast_Type())
ieee8021TeipsIpgConfigCommandLast.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigCommandLast.setStatus(_A)
class _Ieee8021TeipsIpgConfigCommandAdmin_Type(IEEE8021TeipsIpgConfigAdmin):defaultValue=1
_Ieee8021TeipsIpgConfigCommandAdmin_Type.__name__=_O
_Ieee8021TeipsIpgConfigCommandAdmin_Object=MibTableColumn
ieee8021TeipsIpgConfigCommandAdmin=_Ieee8021TeipsIpgConfigCommandAdmin_Object((1,3,111,2,802,1,1,24,1,4,1,4),_Ieee8021TeipsIpgConfigCommandAdmin_Type())
ieee8021TeipsIpgConfigCommandAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigCommandAdmin.setStatus(_A)
_Ieee8021TeipsIpgConfigActiveRequests_Type=IEEE8021TeipsIpgConfigActiveRequests
_Ieee8021TeipsIpgConfigActiveRequests_Object=MibTableColumn
ieee8021TeipsIpgConfigActiveRequests=_Ieee8021TeipsIpgConfigActiveRequests_Object((1,3,111,2,802,1,1,24,1,4,1,5),_Ieee8021TeipsIpgConfigActiveRequests_Type())
ieee8021TeipsIpgConfigActiveRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigActiveRequests.setStatus(_A)
class _Ieee8021TeipsIpgConfigWTR_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,12))
_Ieee8021TeipsIpgConfigWTR_Type.__name__=_E
_Ieee8021TeipsIpgConfigWTR_Object=MibTableColumn
ieee8021TeipsIpgConfigWTR=_Ieee8021TeipsIpgConfigWTR_Object((1,3,111,2,802,1,1,24,1,4,1,6),_Ieee8021TeipsIpgConfigWTR_Type())
ieee8021TeipsIpgConfigWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigWTR.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigWTR.setUnits(_S)
class _Ieee8021TeipsIpgConfigHoldOff_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Ieee8021TeipsIpgConfigHoldOff_Type.__name__=_E
_Ieee8021TeipsIpgConfigHoldOff_Object=MibTableColumn
ieee8021TeipsIpgConfigHoldOff=_Ieee8021TeipsIpgConfigHoldOff_Object((1,3,111,2,802,1,1,24,1,4,1,7),_Ieee8021TeipsIpgConfigHoldOff_Type())
ieee8021TeipsIpgConfigHoldOff.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigHoldOff.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigHoldOff.setUnits('deciseconds')
class _Ieee8021TeipsIpgM1ConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('psAssigned',1),('segmentOk',2),('segmentFailed',3),('assignNewPs',4),('revertToBetterPs',5)))
_Ieee8021TeipsIpgM1ConfigState_Type.__name__=_J
_Ieee8021TeipsIpgM1ConfigState_Object=MibTableColumn
ieee8021TeipsIpgM1ConfigState=_Ieee8021TeipsIpgM1ConfigState_Object((1,3,111,2,802,1,1,24,1,4,1,8),_Ieee8021TeipsIpgM1ConfigState_Type())
ieee8021TeipsIpgM1ConfigState.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021TeipsIpgM1ConfigState.setStatus(_A)
class _Ieee8021TeipsIpgConfigMWTR_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,12))
_Ieee8021TeipsIpgConfigMWTR_Type.__name__=_E
_Ieee8021TeipsIpgConfigMWTR_Object=MibTableColumn
ieee8021TeipsIpgConfigMWTR=_Ieee8021TeipsIpgConfigMWTR_Object((1,3,111,2,802,1,1,24,1,4,1,9),_Ieee8021TeipsIpgConfigMWTR_Type())
ieee8021TeipsIpgConfigMWTR.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigMWTR.setStatus(_A)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigMWTR.setUnits(_S)
class _Ieee8021TeipsIpgConfigNotifyEnable_Type(TruthValue):defaultValue=2
_Ieee8021TeipsIpgConfigNotifyEnable_Type.__name__=_P
_Ieee8021TeipsIpgConfigNotifyEnable_Object=MibTableColumn
ieee8021TeipsIpgConfigNotifyEnable=_Ieee8021TeipsIpgConfigNotifyEnable_Object((1,3,111,2,802,1,1,24,1,4,1,10),_Ieee8021TeipsIpgConfigNotifyEnable_Type())
ieee8021TeipsIpgConfigNotifyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigNotifyEnable.setStatus(_A)
class _Ieee8021TeipsIpgConfigStorageType_Type(StorageType):defaultValue=3
_Ieee8021TeipsIpgConfigStorageType_Type.__name__=_F
_Ieee8021TeipsIpgConfigStorageType_Object=MibTableColumn
ieee8021TeipsIpgConfigStorageType=_Ieee8021TeipsIpgConfigStorageType_Object((1,3,111,2,802,1,1,24,1,4,1,11),_Ieee8021TeipsIpgConfigStorageType_Type())
ieee8021TeipsIpgConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigStorageType.setStatus(_A)
_Ieee8021TeipsConformance_ObjectIdentity=ObjectIdentity
ieee8021TeipsConformance=_Ieee8021TeipsConformance_ObjectIdentity((1,3,111,2,802,1,1,24,2))
_Ieee8021TeipsCompliances_ObjectIdentity=ObjectIdentity
ieee8021TeipsCompliances=_Ieee8021TeipsCompliances_ObjectIdentity((1,3,111,2,802,1,1,24,2,1))
_Ieee8021TeipsGroups_ObjectIdentity=ObjectIdentity
ieee8021TeipsGroups=_Ieee8021TeipsGroups_ObjectIdentity((1,3,111,2,802,1,1,24,2,2))
ieee8021TeipsIpgGroup=ObjectGroup((1,3,111,2,802,1,1,24,2,2,1))
ieee8021TeipsIpgGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ieee8021TeipsIpgGroup.setStatus(_A)
ieee8021TeipsCandidatePsGroup=ObjectGroup((1,3,111,2,802,1,1,24,2,2,2))
ieee8021TeipsCandidatePsGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ieee8021TeipsCandidatePsGroup.setStatus(_A)
ieee8021TeipsIpgTesiGroup=ObjectGroup((1,3,111,2,802,1,1,24,2,2,3))
ieee8021TeipsIpgTesiGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ieee8021TeipsIpgTesiGroup.setStatus(_A)
ieee8021TeipsIpgConfigManGroup=ObjectGroup((1,3,111,2,802,1,1,24,2,2,4))
ieee8021TeipsIpgConfigManGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigManGroup.setStatus(_A)
ieee8021TeipsIpgConfigOptGroup=ObjectGroup((1,3,111,2,802,1,1,24,2,2,5))
ieee8021TeipsIpgConfigOptGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ieee8021TeipsIpgConfigOptGroup.setStatus(_A)
ieee8021TeipsIpgAdminFailure=NotificationType((1,3,111,2,802,1,1,24,0,1))
ieee8021TeipsIpgAdminFailure.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ieee8021TeipsIpgAdminFailure.setStatus(_A)
ieee8021TeipsNotificationsGroup=NotificationGroup((1,3,111,2,802,1,1,24,2,2,6))
ieee8021TeipsNotificationsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:ieee8021TeipsNotificationsGroup.setStatus(_A)
ieee8021TeipsCompliance=ModuleCompliance((1,3,111,2,802,1,1,24,2,1,1))
ieee8021TeipsCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ieee8021TeipsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021TeipsMib':ieee8021TeipsMib,'ieee8021TeipsNotifications':ieee8021TeipsNotifications,_p:ieee8021TeipsIpgAdminFailure,'ieee8021TeipsObjects':ieee8021TeipsObjects,'ieee8021TeipsIpgTable':ieee8021TeipsIpgTable,'ieee8021TeipsIpgEntry':ieee8021TeipsIpgEntry,_G:ieee8021TeipsIpgid,_T:ieee8021TeipsIpgWorkingMA,_U:ieee8021TeipsIpgProtectionMA,_V:ieee8021TeipsIpgWorkingPortNumber,_W:ieee8021TeipsIpgProtectionPortNumber,_X:ieee8021TeipsIpgStorageType,_Y:ieee8021TeipsIpgRowStatus,'ieee8021TeipsTesiTable':ieee8021TeipsTesiTable,'ieee8021TeipsTesiEntry':ieee8021TeipsTesiEntry,_Q:ieee8021TeipsTesiIndex,_e:ieee8021TeipsTesiId,_f:ieee8021TeipsTesiStorageType,_g:ieee8021TeipsTesiRowStatus,'ieee8021TeipsCandidatePsTable':ieee8021TeipsCandidatePsTable,'ieee8021TeipsCandidatePsEntry':ieee8021TeipsCandidatePsEntry,_R:ieee8021TeipsCandidatePsIndex,_Z:ieee8021TeipsCandidatePsMA,_a:ieee8021TeipsCandidatePsPort,_b:ieee8021TeipsCandidatePsOper,_c:ieee8021TeipsCandidatePsStorageType,_d:ieee8021TeipsCandidatePsRowStatus,'ieee8021TeipsIpgConfigTable':ieee8021TeipsIpgConfigTable,'ieee8021TeipsIpgConfigEntry':ieee8021TeipsIpgConfigEntry,_L:ieee8021TeipsIpgConfigState,_M:ieee8021TeipsIpgConfigCommandStatus,_N:ieee8021TeipsIpgConfigCommandLast,_h:ieee8021TeipsIpgConfigCommandAdmin,_i:ieee8021TeipsIpgConfigActiveRequests,_l:ieee8021TeipsIpgConfigWTR,_o:ieee8021TeipsIpgConfigHoldOff,_n:ieee8021TeipsIpgM1ConfigState,_m:ieee8021TeipsIpgConfigMWTR,_j:ieee8021TeipsIpgConfigNotifyEnable,_k:ieee8021TeipsIpgConfigStorageType,'ieee8021TeipsConformance':ieee8021TeipsConformance,'ieee8021TeipsCompliances':ieee8021TeipsCompliances,'ieee8021TeipsCompliance':ieee8021TeipsCompliance,'ieee8021TeipsGroups':ieee8021TeipsGroups,_q:ieee8021TeipsIpgGroup,_v:ieee8021TeipsCandidatePsGroup,_r:ieee8021TeipsIpgTesiGroup,_s:ieee8021TeipsIpgConfigManGroup,_u:ieee8021TeipsIpgConfigOptGroup,_t:ieee8021TeipsNotificationsGroup})