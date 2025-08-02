_A5='ifPhysicalTrxGroupV7'
_A4='ifPhysicalTrxGroupV6'
_A3='ifPhysicalTrxGroupV5'
_A2='ifPhysicalTrxGroupV3'
_A1='ifPhysicalTrxGroupV2'
_A0='ifPhysicalTrxGroupV1'
_z='ifPhysicalTrxCommunicationFailure'
_y='ifPhysicalTrxLowTemp'
_x='ifPhysicalCageUId'
_w='ifPhysicalCageEquipped'
_v='ifPhysicalCagePhysicalLocation'
_u='ifPhysicalCageAid'
_t='ifPhysicalCageSlot'
_s='ifPhysicalCageSubrack'
_r='ifPhysicalCageConnIfBasicIfIndex'
_q='ifPhysicalCageName'
_p='ifPhysicalGeneralIfPhysicalCageStateLastChangeTime'
_o='ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime'
_n='ifPhysicalGeneralIfPhysicalCageTableSize'
_m='TruthValueWithNA'
_l='ResetWithNA'
_k='ifPhysicalCageGroupV1'
_j='ifPhysicalGeneralGroupV2'
_i='ifPhysicalTrxPowerOutOfRange'
_h='ifPhysicalTrxPhysicalLocation'
_g='ifPhysicalTrxAid'
_f='ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime'
_e='ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime'
_d='ifPhysicalGeneralIfPhysicalTrxTableSize'
_c='ifPhysicalGeneralStateLastChangeTime'
_b='ifPhysicalGeneralConfigLastChangeTime'
_a='ifPhysicalCageIndex'
_Z='TrxMediaWithNA'
_Y='ifPhysicalTrxUId'
_X='DisplayStringWithNA'
_W='ifPhysicalGeneralGroupV1'
_V='ifPhysicalTrxPowerCycleReset'
_U='ifPhysicalTrxOpticalLayerMappingMismatch'
_T='ifPhysicalTrxTrxTxState'
_S='ifPhysicalTrxTrxRxState'
_R='ifPhysicalTrxTrxMediaMismatch'
_Q='ifPhysicalTrxTrxMissing'
_P='ifPhysicalTrxNonQualifiedTrx'
_O='ifPhysicalTrxTransmitterFailed'
_N='ifPhysicalTrxRxSignalStatus'
_M='ifPhysicalTrxTxSignalStatus'
_L='ifPhysicalTrxActualTrxMedia'
_K='ifPhysicalTrxTrxMedia'
_J='ifPhysicalTrxTrxClass'
_I='ifPhysicalTrxLaserTemp'
_H='ifPhysicalTrxLaserBias'
_G='ifPhysicalTrxConnIfBasicIfIndex'
_F='ifPhysicalTrxName'
_E='ifPhysicalTrxIndex'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFPHYSICAL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfPhysicalMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfPhysicalMIB','lumModules')
CommandString,DisplayStringWithNA,FaultStatusWithNA,Integer32WithNA,MgmtNameString,ResetWithNA,SignalStatusWithNA,SubrackNumber,TruthValueWithNA,TrxMediaWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','CommandString',_X,'FaultStatusWithNA','Integer32WithNA','MgmtNameString',_l,'SignalStatusWithNA','SubrackNumber',_m,_Z,'Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfPhysicalMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,47))
if mibBuilder.loadTexts:lumIfPhysicalMIBModule.setRevisions(('2017-06-15 00:00','2017-04-21 00:00','2016-12-12 00:00','2016-11-30 00:00','2015-12-22 00:00','2015-10-30 00:00','2015-01-23 00:00','2014-10-30 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2012-11-20 00:00'))
_LumIfPhysicalConfs_ObjectIdentity=ObjectIdentity
lumIfPhysicalConfs=_LumIfPhysicalConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,47,1))
_LumIfPhysicalGroups_ObjectIdentity=ObjectIdentity
lumIfPhysicalGroups=_LumIfPhysicalGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,47,1,1))
_LumIfPhysicalCompl_ObjectIdentity=ObjectIdentity
lumIfPhysicalCompl=_LumIfPhysicalCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,47,1,2))
_LumIfPhysicalMIBObjects_ObjectIdentity=ObjectIdentity
lumIfPhysicalMIBObjects=_LumIfPhysicalMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,47,2))
_IfPhysicalGeneral_ObjectIdentity=ObjectIdentity
ifPhysicalGeneral=_IfPhysicalGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,47,2,1))
_IfPhysicalGeneralConfigLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralConfigLastChangeTime_Object=MibScalar
ifPhysicalGeneralConfigLastChangeTime=_IfPhysicalGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,1),_IfPhysicalGeneralConfigLastChangeTime_Type())
ifPhysicalGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralConfigLastChangeTime.setStatus(_B)
_IfPhysicalGeneralStateLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralStateLastChangeTime_Object=MibScalar
ifPhysicalGeneralStateLastChangeTime=_IfPhysicalGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,2),_IfPhysicalGeneralStateLastChangeTime_Type())
ifPhysicalGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralStateLastChangeTime.setStatus(_B)
_IfPhysicalGeneralIfPhysicalTrxTableSize_Type=Unsigned32
_IfPhysicalGeneralIfPhysicalTrxTableSize_Object=MibScalar
ifPhysicalGeneralIfPhysicalTrxTableSize=_IfPhysicalGeneralIfPhysicalTrxTableSize_Object((1,3,6,1,4,1,8708,2,47,2,1,3),_IfPhysicalGeneralIfPhysicalTrxTableSize_Type())
ifPhysicalGeneralIfPhysicalTrxTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalTrxTableSize.setStatus(_B)
_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Object=MibScalar
ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime=_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,4),_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Type())
ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime.setStatus(_B)
_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Object=MibScalar
ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime=_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,5),_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Type())
ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime.setStatus(_B)
_IfPhysicalGeneralIfPhysicalCageTableSize_Type=Unsigned32
_IfPhysicalGeneralIfPhysicalCageTableSize_Object=MibScalar
ifPhysicalGeneralIfPhysicalCageTableSize=_IfPhysicalGeneralIfPhysicalCageTableSize_Object((1,3,6,1,4,1,8708,2,47,2,1,6),_IfPhysicalGeneralIfPhysicalCageTableSize_Type())
ifPhysicalGeneralIfPhysicalCageTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalCageTableSize.setStatus(_B)
_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Object=MibScalar
ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime=_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,7),_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Type())
ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime.setStatus(_B)
_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Type=DateAndTime
_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Object=MibScalar
ifPhysicalGeneralIfPhysicalCageStateLastChangeTime=_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,47,2,1,8),_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Type())
ifPhysicalGeneralIfPhysicalCageStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalGeneralIfPhysicalCageStateLastChangeTime.setStatus(_B)
_IfPhysicalTrxList_ObjectIdentity=ObjectIdentity
ifPhysicalTrxList=_IfPhysicalTrxList_ObjectIdentity((1,3,6,1,4,1,8708,2,47,2,2))
_IfPhysicalTrxTable_Object=MibTable
ifPhysicalTrxTable=_IfPhysicalTrxTable_Object((1,3,6,1,4,1,8708,2,47,2,2,1))
if mibBuilder.loadTexts:ifPhysicalTrxTable.setStatus(_B)
_IfPhysicalTrxEntry_Object=MibTableRow
ifPhysicalTrxEntry=_IfPhysicalTrxEntry_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1))
ifPhysicalTrxEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:ifPhysicalTrxEntry.setStatus(_B)
_IfPhysicalTrxIndex_Type=Unsigned32
_IfPhysicalTrxIndex_Object=MibTableColumn
ifPhysicalTrxIndex=_IfPhysicalTrxIndex_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,1),_IfPhysicalTrxIndex_Type())
ifPhysicalTrxIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxIndex.setStatus(_B)
_IfPhysicalTrxName_Type=MgmtNameString
_IfPhysicalTrxName_Object=MibTableColumn
ifPhysicalTrxName=_IfPhysicalTrxName_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,2),_IfPhysicalTrxName_Type())
ifPhysicalTrxName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxName.setStatus(_B)
_IfPhysicalTrxConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfPhysicalTrxConnIfBasicIfIndex_Object=MibTableColumn
ifPhysicalTrxConnIfBasicIfIndex=_IfPhysicalTrxConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,3),_IfPhysicalTrxConnIfBasicIfIndex_Type())
ifPhysicalTrxConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxConnIfBasicIfIndex.setStatus(_B)
_IfPhysicalTrxLaserBias_Type=Unsigned32WithNA
_IfPhysicalTrxLaserBias_Object=MibTableColumn
ifPhysicalTrxLaserBias=_IfPhysicalTrxLaserBias_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,4),_IfPhysicalTrxLaserBias_Type())
ifPhysicalTrxLaserBias.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxLaserBias.setStatus(_B)
_IfPhysicalTrxLaserTemp_Type=Integer32WithNA
_IfPhysicalTrxLaserTemp_Object=MibTableColumn
ifPhysicalTrxLaserTemp=_IfPhysicalTrxLaserTemp_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,5),_IfPhysicalTrxLaserTemp_Type())
ifPhysicalTrxLaserTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxLaserTemp.setStatus(_B)
class _IfPhysicalTrxTrxClass_Type(DisplayStringWithNA):defaultValue=OctetString('')
_IfPhysicalTrxTrxClass_Type.__name__=_X
_IfPhysicalTrxTrxClass_Object=MibTableColumn
ifPhysicalTrxTrxClass=_IfPhysicalTrxTrxClass_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,6),_IfPhysicalTrxTrxClass_Type())
ifPhysicalTrxTrxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTrxClass.setStatus(_B)
class _IfPhysicalTrxTrxMedia_Type(TrxMediaWithNA):defaultValue=1
_IfPhysicalTrxTrxMedia_Type.__name__=_Z
_IfPhysicalTrxTrxMedia_Object=MibTableColumn
ifPhysicalTrxTrxMedia=_IfPhysicalTrxTrxMedia_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,7),_IfPhysicalTrxTrxMedia_Type())
ifPhysicalTrxTrxMedia.setMaxAccess('read-write')
if mibBuilder.loadTexts:ifPhysicalTrxTrxMedia.setStatus(_B)
class _IfPhysicalTrxActualTrxMedia_Type(TrxMediaWithNA):defaultValue=1
_IfPhysicalTrxActualTrxMedia_Type.__name__=_Z
_IfPhysicalTrxActualTrxMedia_Object=MibTableColumn
ifPhysicalTrxActualTrxMedia=_IfPhysicalTrxActualTrxMedia_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,8),_IfPhysicalTrxActualTrxMedia_Type())
ifPhysicalTrxActualTrxMedia.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxActualTrxMedia.setStatus(_B)
_IfPhysicalTrxTxSignalStatus_Type=SignalStatusWithNA
_IfPhysicalTrxTxSignalStatus_Object=MibTableColumn
ifPhysicalTrxTxSignalStatus=_IfPhysicalTrxTxSignalStatus_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,9),_IfPhysicalTrxTxSignalStatus_Type())
ifPhysicalTrxTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTxSignalStatus.setStatus(_B)
_IfPhysicalTrxRxSignalStatus_Type=SignalStatusWithNA
_IfPhysicalTrxRxSignalStatus_Object=MibTableColumn
ifPhysicalTrxRxSignalStatus=_IfPhysicalTrxRxSignalStatus_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,10),_IfPhysicalTrxRxSignalStatus_Type())
ifPhysicalTrxRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxRxSignalStatus.setStatus(_B)
_IfPhysicalTrxTransmitterFailed_Type=FaultStatusWithNA
_IfPhysicalTrxTransmitterFailed_Object=MibTableColumn
ifPhysicalTrxTransmitterFailed=_IfPhysicalTrxTransmitterFailed_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,11),_IfPhysicalTrxTransmitterFailed_Type())
ifPhysicalTrxTransmitterFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTransmitterFailed.setStatus(_B)
_IfPhysicalTrxNonQualifiedTrx_Type=FaultStatusWithNA
_IfPhysicalTrxNonQualifiedTrx_Object=MibTableColumn
ifPhysicalTrxNonQualifiedTrx=_IfPhysicalTrxNonQualifiedTrx_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,12),_IfPhysicalTrxNonQualifiedTrx_Type())
ifPhysicalTrxNonQualifiedTrx.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxNonQualifiedTrx.setStatus(_B)
_IfPhysicalTrxTrxMissing_Type=FaultStatusWithNA
_IfPhysicalTrxTrxMissing_Object=MibTableColumn
ifPhysicalTrxTrxMissing=_IfPhysicalTrxTrxMissing_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,13),_IfPhysicalTrxTrxMissing_Type())
ifPhysicalTrxTrxMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTrxMissing.setStatus(_B)
_IfPhysicalTrxTrxMediaMismatch_Type=FaultStatusWithNA
_IfPhysicalTrxTrxMediaMismatch_Object=MibTableColumn
ifPhysicalTrxTrxMediaMismatch=_IfPhysicalTrxTrxMediaMismatch_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,14),_IfPhysicalTrxTrxMediaMismatch_Type())
ifPhysicalTrxTrxMediaMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTrxMediaMismatch.setStatus(_B)
class _IfPhysicalTrxTrxRxState_Type(DisplayStringWithNA):defaultValue=OctetString('')
_IfPhysicalTrxTrxRxState_Type.__name__=_X
_IfPhysicalTrxTrxRxState_Object=MibTableColumn
ifPhysicalTrxTrxRxState=_IfPhysicalTrxTrxRxState_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,15),_IfPhysicalTrxTrxRxState_Type())
ifPhysicalTrxTrxRxState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTrxRxState.setStatus(_B)
class _IfPhysicalTrxTrxTxState_Type(DisplayStringWithNA):defaultValue=OctetString('')
_IfPhysicalTrxTrxTxState_Type.__name__=_X
_IfPhysicalTrxTrxTxState_Object=MibTableColumn
ifPhysicalTrxTrxTxState=_IfPhysicalTrxTrxTxState_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,16),_IfPhysicalTrxTrxTxState_Type())
ifPhysicalTrxTrxTxState.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxTrxTxState.setStatus(_B)
_IfPhysicalTrxOpticalLayerMappingMismatch_Type=FaultStatusWithNA
_IfPhysicalTrxOpticalLayerMappingMismatch_Object=MibTableColumn
ifPhysicalTrxOpticalLayerMappingMismatch=_IfPhysicalTrxOpticalLayerMappingMismatch_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,17),_IfPhysicalTrxOpticalLayerMappingMismatch_Type())
ifPhysicalTrxOpticalLayerMappingMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxOpticalLayerMappingMismatch.setStatus(_B)
class _IfPhysicalTrxPowerCycleReset_Type(ResetWithNA):defaultValue=2
_IfPhysicalTrxPowerCycleReset_Type.__name__=_l
_IfPhysicalTrxPowerCycleReset_Object=MibTableColumn
ifPhysicalTrxPowerCycleReset=_IfPhysicalTrxPowerCycleReset_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,18),_IfPhysicalTrxPowerCycleReset_Type())
ifPhysicalTrxPowerCycleReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxPowerCycleReset.setStatus(_B)
_IfPhysicalTrxUId_Type=Unsigned32
_IfPhysicalTrxUId_Object=MibTableColumn
ifPhysicalTrxUId=_IfPhysicalTrxUId_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,19),_IfPhysicalTrxUId_Type())
ifPhysicalTrxUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxUId.setStatus(_B)
_IfPhysicalTrxAid_Type=DisplayString
_IfPhysicalTrxAid_Object=MibTableColumn
ifPhysicalTrxAid=_IfPhysicalTrxAid_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,20),_IfPhysicalTrxAid_Type())
ifPhysicalTrxAid.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxAid.setStatus(_B)
_IfPhysicalTrxPhysicalLocation_Type=DisplayString
_IfPhysicalTrxPhysicalLocation_Object=MibTableColumn
ifPhysicalTrxPhysicalLocation=_IfPhysicalTrxPhysicalLocation_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,21),_IfPhysicalTrxPhysicalLocation_Type())
ifPhysicalTrxPhysicalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxPhysicalLocation.setStatus(_B)
_IfPhysicalTrxPowerOutOfRange_Type=FaultStatusWithNA
_IfPhysicalTrxPowerOutOfRange_Object=MibTableColumn
ifPhysicalTrxPowerOutOfRange=_IfPhysicalTrxPowerOutOfRange_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,22),_IfPhysicalTrxPowerOutOfRange_Type())
ifPhysicalTrxPowerOutOfRange.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxPowerOutOfRange.setStatus(_B)
_IfPhysicalTrxLowTemp_Type=FaultStatusWithNA
_IfPhysicalTrxLowTemp_Object=MibTableColumn
ifPhysicalTrxLowTemp=_IfPhysicalTrxLowTemp_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,23),_IfPhysicalTrxLowTemp_Type())
ifPhysicalTrxLowTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxLowTemp.setStatus(_B)
_IfPhysicalTrxCommunicationFailure_Type=FaultStatusWithNA
_IfPhysicalTrxCommunicationFailure_Object=MibTableColumn
ifPhysicalTrxCommunicationFailure=_IfPhysicalTrxCommunicationFailure_Object((1,3,6,1,4,1,8708,2,47,2,2,1,1,24),_IfPhysicalTrxCommunicationFailure_Type())
ifPhysicalTrxCommunicationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalTrxCommunicationFailure.setStatus(_B)
_IfPhysicalCageList_ObjectIdentity=ObjectIdentity
ifPhysicalCageList=_IfPhysicalCageList_ObjectIdentity((1,3,6,1,4,1,8708,2,47,2,3))
_IfPhysicalCageTable_Object=MibTable
ifPhysicalCageTable=_IfPhysicalCageTable_Object((1,3,6,1,4,1,8708,2,47,2,3,1))
if mibBuilder.loadTexts:ifPhysicalCageTable.setStatus(_B)
_IfPhysicalCageEntry_Object=MibTableRow
ifPhysicalCageEntry=_IfPhysicalCageEntry_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1))
ifPhysicalCageEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:ifPhysicalCageEntry.setStatus(_B)
_IfPhysicalCageIndex_Type=Unsigned32
_IfPhysicalCageIndex_Object=MibTableColumn
ifPhysicalCageIndex=_IfPhysicalCageIndex_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,1),_IfPhysicalCageIndex_Type())
ifPhysicalCageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageIndex.setStatus(_B)
_IfPhysicalCageName_Type=MgmtNameString
_IfPhysicalCageName_Object=MibTableColumn
ifPhysicalCageName=_IfPhysicalCageName_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,2),_IfPhysicalCageName_Type())
ifPhysicalCageName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageName.setStatus(_B)
_IfPhysicalCageConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfPhysicalCageConnIfBasicIfIndex_Object=MibTableColumn
ifPhysicalCageConnIfBasicIfIndex=_IfPhysicalCageConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,3),_IfPhysicalCageConnIfBasicIfIndex_Type())
ifPhysicalCageConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageConnIfBasicIfIndex.setStatus(_B)
_IfPhysicalCageSubrack_Type=SubrackNumber
_IfPhysicalCageSubrack_Object=MibTableColumn
ifPhysicalCageSubrack=_IfPhysicalCageSubrack_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,4),_IfPhysicalCageSubrack_Type())
ifPhysicalCageSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageSubrack.setStatus(_B)
_IfPhysicalCageSlot_Type=Unsigned32
_IfPhysicalCageSlot_Object=MibTableColumn
ifPhysicalCageSlot=_IfPhysicalCageSlot_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,5),_IfPhysicalCageSlot_Type())
ifPhysicalCageSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageSlot.setStatus(_B)
_IfPhysicalCageAid_Type=DisplayString
_IfPhysicalCageAid_Object=MibTableColumn
ifPhysicalCageAid=_IfPhysicalCageAid_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,6),_IfPhysicalCageAid_Type())
ifPhysicalCageAid.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageAid.setStatus(_B)
_IfPhysicalCagePhysicalLocation_Type=DisplayString
_IfPhysicalCagePhysicalLocation_Object=MibTableColumn
ifPhysicalCagePhysicalLocation=_IfPhysicalCagePhysicalLocation_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,7),_IfPhysicalCagePhysicalLocation_Type())
ifPhysicalCagePhysicalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCagePhysicalLocation.setStatus(_B)
class _IfPhysicalCageEquipped_Type(TruthValueWithNA):defaultValue=2147483647
_IfPhysicalCageEquipped_Type.__name__=_m
_IfPhysicalCageEquipped_Object=MibTableColumn
ifPhysicalCageEquipped=_IfPhysicalCageEquipped_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,8),_IfPhysicalCageEquipped_Type())
ifPhysicalCageEquipped.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageEquipped.setStatus(_B)
_IfPhysicalCageUId_Type=Unsigned32
_IfPhysicalCageUId_Object=MibTableColumn
ifPhysicalCageUId=_IfPhysicalCageUId_Object((1,3,6,1,4,1,8708,2,47,2,3,1,1,9),_IfPhysicalCageUId_Type())
ifPhysicalCageUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifPhysicalCageUId.setStatus(_B)
ifPhysicalGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,1))
ifPhysicalGeneralGroupV1.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ifPhysicalGeneralGroupV1.setStatus(_D)
ifPhysicalTrxGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,2))
ifPhysicalTrxGroupV1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV1.setStatus(_D)
ifPhysicalTrxGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,3))
ifPhysicalTrxGroupV2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV2.setStatus(_D)
ifPhysicalTrxGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,4))
ifPhysicalTrxGroupV3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV3.setStatus(_D)
ifPhysicalTrxGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,5))
ifPhysicalTrxGroupV4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV4.setStatus(_D)
ifPhysicalTrxGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,6))
ifPhysicalTrxGroupV5.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_Y)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV5.setStatus(_D)
ifPhysicalGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,7))
ifPhysicalGeneralGroupV2.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ifPhysicalGeneralGroupV2.setStatus(_B)
ifPhysicalCageGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,8))
ifPhysicalCageGroupV1.setObjects(*((_A,_a),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ifPhysicalCageGroupV1.setStatus(_B)
ifPhysicalTrxGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,9))
ifPhysicalTrxGroupV6.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_Y),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV6.setStatus(_D)
ifPhysicalTrxGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,47,1,1,10))
ifPhysicalTrxGroupV7.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_Y),(_A,_g),(_A,_h),(_A,_i),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ifPhysicalTrxGroupV7.setStatus(_B)
lumIfPhysicalComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,1))
lumIfPhysicalComplV1.setObjects(*((_A,_W),(_A,_A0)))
if mibBuilder.loadTexts:lumIfPhysicalComplV1.setStatus(_D)
lumIfPhysicalComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,2))
lumIfPhysicalComplV2.setObjects(*((_A,_W),(_A,_A1)))
if mibBuilder.loadTexts:lumIfPhysicalComplV2.setStatus(_D)
lumIfPhysicalComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,3))
lumIfPhysicalComplV3.setObjects(*((_A,_W),(_A,_A2)))
if mibBuilder.loadTexts:lumIfPhysicalComplV3.setStatus(_D)
lumIfPhysicalComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,4))
lumIfPhysicalComplV4.setObjects(*((_A,_W),(_A,_A3)))
if mibBuilder.loadTexts:lumIfPhysicalComplV4.setStatus(_D)
lumIfPhysicalComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,5))
lumIfPhysicalComplV5.setObjects(*((_A,_j),(_A,_A4),(_A,_k)))
if mibBuilder.loadTexts:lumIfPhysicalComplV5.setStatus(_D)
lumIfPhysicalComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,47,1,2,6))
lumIfPhysicalComplV6.setObjects(*((_A,_j),(_A,_A5),(_A,_k)))
if mibBuilder.loadTexts:lumIfPhysicalComplV6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfPhysicalMIBModule':lumIfPhysicalMIBModule,'lumIfPhysicalConfs':lumIfPhysicalConfs,'lumIfPhysicalGroups':lumIfPhysicalGroups,_W:ifPhysicalGeneralGroupV1,_A0:ifPhysicalTrxGroupV1,_A1:ifPhysicalTrxGroupV2,_A2:ifPhysicalTrxGroupV3,'ifPhysicalTrxGroupV4':ifPhysicalTrxGroupV4,_A3:ifPhysicalTrxGroupV5,_j:ifPhysicalGeneralGroupV2,_k:ifPhysicalCageGroupV1,_A4:ifPhysicalTrxGroupV6,_A5:ifPhysicalTrxGroupV7,'lumIfPhysicalCompl':lumIfPhysicalCompl,'lumIfPhysicalComplV1':lumIfPhysicalComplV1,'lumIfPhysicalComplV2':lumIfPhysicalComplV2,'lumIfPhysicalComplV3':lumIfPhysicalComplV3,'lumIfPhysicalComplV4':lumIfPhysicalComplV4,'lumIfPhysicalComplV5':lumIfPhysicalComplV5,'lumIfPhysicalComplV6':lumIfPhysicalComplV6,'lumIfPhysicalMIBObjects':lumIfPhysicalMIBObjects,'ifPhysicalGeneral':ifPhysicalGeneral,_b:ifPhysicalGeneralConfigLastChangeTime,_c:ifPhysicalGeneralStateLastChangeTime,_d:ifPhysicalGeneralIfPhysicalTrxTableSize,_e:ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime,_f:ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime,_n:ifPhysicalGeneralIfPhysicalCageTableSize,_o:ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime,_p:ifPhysicalGeneralIfPhysicalCageStateLastChangeTime,'ifPhysicalTrxList':ifPhysicalTrxList,'ifPhysicalTrxTable':ifPhysicalTrxTable,'ifPhysicalTrxEntry':ifPhysicalTrxEntry,_E:ifPhysicalTrxIndex,_F:ifPhysicalTrxName,_G:ifPhysicalTrxConnIfBasicIfIndex,_H:ifPhysicalTrxLaserBias,_I:ifPhysicalTrxLaserTemp,_J:ifPhysicalTrxTrxClass,_K:ifPhysicalTrxTrxMedia,_L:ifPhysicalTrxActualTrxMedia,_M:ifPhysicalTrxTxSignalStatus,_N:ifPhysicalTrxRxSignalStatus,_O:ifPhysicalTrxTransmitterFailed,_P:ifPhysicalTrxNonQualifiedTrx,_Q:ifPhysicalTrxTrxMissing,_R:ifPhysicalTrxTrxMediaMismatch,_S:ifPhysicalTrxTrxRxState,_T:ifPhysicalTrxTrxTxState,_U:ifPhysicalTrxOpticalLayerMappingMismatch,_V:ifPhysicalTrxPowerCycleReset,_Y:ifPhysicalTrxUId,_g:ifPhysicalTrxAid,_h:ifPhysicalTrxPhysicalLocation,_i:ifPhysicalTrxPowerOutOfRange,_y:ifPhysicalTrxLowTemp,_z:ifPhysicalTrxCommunicationFailure,'ifPhysicalCageList':ifPhysicalCageList,'ifPhysicalCageTable':ifPhysicalCageTable,'ifPhysicalCageEntry':ifPhysicalCageEntry,_a:ifPhysicalCageIndex,_q:ifPhysicalCageName,_r:ifPhysicalCageConnIfBasicIfIndex,_s:ifPhysicalCageSubrack,_t:ifPhysicalCageSlot,_u:ifPhysicalCageAid,_v:ifPhysicalCagePhysicalLocation,_w:ifPhysicalCageEquipped,_x:ifPhysicalCageUId})