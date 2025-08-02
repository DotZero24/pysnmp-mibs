_AG='ifEthGeneralGroupV2'
_AF='ifEthPhysicalGroupV4'
_AE='ifEthPhysicalGroupV3'
_AD='ifEthPhysicalGroupV2'
_AC='ifEthPhysicalGroupV1'
_AB='ifEthGeneralIfEthRsFecStateLastChangeTime'
_AA='ifEthGeneralIfEthRsFecConfigLastChangeTime'
_A9='ifEthGeneralIfEthRsFecTableSize'
_A8='ifEthRsFecLanesAlignmentError'
_A7='ifEthRsFecActualRsFec'
_A6='ifEthRsFecMode'
_A5='ifEthRsFecRxSignalStatus'
_A4='ifEthRsFecTxSignalStatus'
_A3='ifEthRsFecConnIfBasicIfIndex'
_A2='ifEthRsFecName'
_A1='ifEthPhysicalTxPcsLossOfSync'
_A0='ifEthPhysicalRxPcsLossOfSync'
_z='ifEthPhysicalUId'
_y='ifEthMacRxSignalStatus'
_x='ifEthMacTxSignalStatus'
_w='ifEthMacFlowControlMode'
_v='ifEthMacInterPacketGap'
_u='ifEthMacMaxMtuSize'
_t='ifEthMacTxUtilization'
_s='ifEthMacRxUtilization'
_r='ifEthMacConnIfBasicIfIndex'
_q='ifEthMacName'
_p='read-create'
_o='RsFecOnOff'
_n='RsFecMode'
_m='FlowControlMode'
_l='ifEthRsFecGroupV1'
_k='ifEthPhysicalTxPcsLossOfFrame'
_j='ifEthGeneralIfEthMacStateLastChangeTime'
_i='ifEthGeneralIfEthMacConfigLastChangeTime'
_h='ifEthGeneralIfEthMacTableSize'
_g='ifEthGeneralIfEthPhysicalStateLastChangeTime'
_f='ifEthGeneralIfEthPhysicalConfigLastChangeTime'
_e='ifEthGeneralIfEthPhysicalTableSize'
_d='ifEthGeneralStateLastChangeTime'
_c='ifEthGeneralConfigLastChangeTime'
_b='ifEthRsFecIndex'
_a='ifEthMacIndex'
_Z='ifEthPhysicalGroupV5'
_Y='ifEthPhysicalTxHighBitErrorRate'
_X='ifEthPhysicalRxHighBitErrorRate'
_W='ifEthPhysicalTxLocalLinkFault'
_V='ifEthPhysicalRxLocalLinkFault'
_U='ifEthPhysicalPcsLossOfFrame'
_T='ifEthPhysicalHighBitErrorRate'
_S='ifEthPhysicalLinkDown'
_R='ifEthPhysicalLocalLinkFault'
_Q='ifEthPhysicalRemoteLinkFault'
_P='ifEthPhysicalRxSignalStatus'
_O='ifEthPhysicalTxSignalStatus'
_N='ifEthPhysicalTxUtilization'
_M='ifEthPhysicalRxUtilization'
_L='ifEthPhysicalAutoNegotiationStatus'
_K='ifEthPhysicalAutoNegotiationMode'
_J='ifEthPhysicalConnIfBasicIfIndex'
_I='ifEthPhysicalName'
_H='ifEthGeneralGroupV1'
_G='ifEthPhysicalIndex'
_F='Unsigned32WithNA'
_E='ifEthMacGroupV1'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFETH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfEthMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfEthMIB','lumModules')
AutoNegotiationStatus,FaultStatusWithNA,FlowControlMode,MgmtNameString,OnOff,RsFecMode,RsFecOnOff,SignalStatusWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','AutoNegotiationStatus','FaultStatusWithNA',_m,'MgmtNameString','OnOff',_n,_o,'SignalStatusWithNA',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfEthMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,54))
if mibBuilder.loadTexts:lumIfEthMIBModule.setRevisions(('2017-06-15 00:00','2016-11-30 00:00','2015-12-22 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2012-11-20 00:00'))
_LumIfEthConfs_ObjectIdentity=ObjectIdentity
lumIfEthConfs=_LumIfEthConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,54,1))
_LumIfEthGroups_ObjectIdentity=ObjectIdentity
lumIfEthGroups=_LumIfEthGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,54,1,1))
_LumIfEthCompl_ObjectIdentity=ObjectIdentity
lumIfEthCompl=_LumIfEthCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,54,1,2))
_LumIfEthMIBObjects_ObjectIdentity=ObjectIdentity
lumIfEthMIBObjects=_LumIfEthMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,54,2))
_IfEthGeneral_ObjectIdentity=ObjectIdentity
ifEthGeneral=_IfEthGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,54,2,1))
_IfEthGeneralConfigLastChangeTime_Type=DateAndTime
_IfEthGeneralConfigLastChangeTime_Object=MibScalar
ifEthGeneralConfigLastChangeTime=_IfEthGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,1),_IfEthGeneralConfigLastChangeTime_Type())
ifEthGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralConfigLastChangeTime.setStatus(_B)
_IfEthGeneralStateLastChangeTime_Type=DateAndTime
_IfEthGeneralStateLastChangeTime_Object=MibScalar
ifEthGeneralStateLastChangeTime=_IfEthGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,2),_IfEthGeneralStateLastChangeTime_Type())
ifEthGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralStateLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthPhysicalTableSize_Type=Unsigned32
_IfEthGeneralIfEthPhysicalTableSize_Object=MibScalar
ifEthGeneralIfEthPhysicalTableSize=_IfEthGeneralIfEthPhysicalTableSize_Object((1,3,6,1,4,1,8708,2,54,2,1,3),_IfEthGeneralIfEthPhysicalTableSize_Type())
ifEthGeneralIfEthPhysicalTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthPhysicalTableSize.setStatus(_B)
_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Object=MibScalar
ifEthGeneralIfEthPhysicalConfigLastChangeTime=_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,4),_IfEthGeneralIfEthPhysicalConfigLastChangeTime_Type())
ifEthGeneralIfEthPhysicalConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthPhysicalConfigLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthPhysicalStateLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthPhysicalStateLastChangeTime_Object=MibScalar
ifEthGeneralIfEthPhysicalStateLastChangeTime=_IfEthGeneralIfEthPhysicalStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,5),_IfEthGeneralIfEthPhysicalStateLastChangeTime_Type())
ifEthGeneralIfEthPhysicalStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthPhysicalStateLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthMacTableSize_Type=Unsigned32
_IfEthGeneralIfEthMacTableSize_Object=MibScalar
ifEthGeneralIfEthMacTableSize=_IfEthGeneralIfEthMacTableSize_Object((1,3,6,1,4,1,8708,2,54,2,1,6),_IfEthGeneralIfEthMacTableSize_Type())
ifEthGeneralIfEthMacTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthMacTableSize.setStatus(_B)
_IfEthGeneralIfEthMacConfigLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthMacConfigLastChangeTime_Object=MibScalar
ifEthGeneralIfEthMacConfigLastChangeTime=_IfEthGeneralIfEthMacConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,7),_IfEthGeneralIfEthMacConfigLastChangeTime_Type())
ifEthGeneralIfEthMacConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthMacConfigLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthMacStateLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthMacStateLastChangeTime_Object=MibScalar
ifEthGeneralIfEthMacStateLastChangeTime=_IfEthGeneralIfEthMacStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,8),_IfEthGeneralIfEthMacStateLastChangeTime_Type())
ifEthGeneralIfEthMacStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthMacStateLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthRsFecTableSize_Type=Unsigned32
_IfEthGeneralIfEthRsFecTableSize_Object=MibScalar
ifEthGeneralIfEthRsFecTableSize=_IfEthGeneralIfEthRsFecTableSize_Object((1,3,6,1,4,1,8708,2,54,2,1,9),_IfEthGeneralIfEthRsFecTableSize_Type())
ifEthGeneralIfEthRsFecTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthRsFecTableSize.setStatus(_B)
_IfEthGeneralIfEthRsFecConfigLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthRsFecConfigLastChangeTime_Object=MibScalar
ifEthGeneralIfEthRsFecConfigLastChangeTime=_IfEthGeneralIfEthRsFecConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,10),_IfEthGeneralIfEthRsFecConfigLastChangeTime_Type())
ifEthGeneralIfEthRsFecConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthRsFecConfigLastChangeTime.setStatus(_B)
_IfEthGeneralIfEthRsFecStateLastChangeTime_Type=DateAndTime
_IfEthGeneralIfEthRsFecStateLastChangeTime_Object=MibScalar
ifEthGeneralIfEthRsFecStateLastChangeTime=_IfEthGeneralIfEthRsFecStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,54,2,1,11),_IfEthGeneralIfEthRsFecStateLastChangeTime_Type())
ifEthGeneralIfEthRsFecStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthGeneralIfEthRsFecStateLastChangeTime.setStatus(_B)
_IfEthPhysicalList_ObjectIdentity=ObjectIdentity
ifEthPhysicalList=_IfEthPhysicalList_ObjectIdentity((1,3,6,1,4,1,8708,2,54,2,2))
_IfEthPhysicalTable_Object=MibTable
ifEthPhysicalTable=_IfEthPhysicalTable_Object((1,3,6,1,4,1,8708,2,54,2,2,1))
if mibBuilder.loadTexts:ifEthPhysicalTable.setStatus(_B)
_IfEthPhysicalEntry_Object=MibTableRow
ifEthPhysicalEntry=_IfEthPhysicalEntry_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1))
ifEthPhysicalEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:ifEthPhysicalEntry.setStatus(_B)
_IfEthPhysicalIndex_Type=Unsigned32
_IfEthPhysicalIndex_Object=MibTableColumn
ifEthPhysicalIndex=_IfEthPhysicalIndex_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,1),_IfEthPhysicalIndex_Type())
ifEthPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalIndex.setStatus(_B)
_IfEthPhysicalName_Type=MgmtNameString
_IfEthPhysicalName_Object=MibTableColumn
ifEthPhysicalName=_IfEthPhysicalName_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,2),_IfEthPhysicalName_Type())
ifEthPhysicalName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalName.setStatus(_B)
_IfEthPhysicalConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfEthPhysicalConnIfBasicIfIndex_Object=MibTableColumn
ifEthPhysicalConnIfBasicIfIndex=_IfEthPhysicalConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,3),_IfEthPhysicalConnIfBasicIfIndex_Type())
ifEthPhysicalConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalConnIfBasicIfIndex.setStatus(_B)
class _IfEthPhysicalAutoNegotiationMode_Type(OnOff):defaultValue=2
_IfEthPhysicalAutoNegotiationMode_Type.__name__='OnOff'
_IfEthPhysicalAutoNegotiationMode_Object=MibTableColumn
ifEthPhysicalAutoNegotiationMode=_IfEthPhysicalAutoNegotiationMode_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,4),_IfEthPhysicalAutoNegotiationMode_Type())
ifEthPhysicalAutoNegotiationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalAutoNegotiationMode.setStatus(_B)
_IfEthPhysicalAutoNegotiationStatus_Type=AutoNegotiationStatus
_IfEthPhysicalAutoNegotiationStatus_Object=MibTableColumn
ifEthPhysicalAutoNegotiationStatus=_IfEthPhysicalAutoNegotiationStatus_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,5),_IfEthPhysicalAutoNegotiationStatus_Type())
ifEthPhysicalAutoNegotiationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalAutoNegotiationStatus.setStatus(_B)
class _IfEthPhysicalRxUtilization_Type(Unsigned32WithNA):subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
_IfEthPhysicalRxUtilization_Type.__name__=_F
_IfEthPhysicalRxUtilization_Object=MibTableColumn
ifEthPhysicalRxUtilization=_IfEthPhysicalRxUtilization_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,6),_IfEthPhysicalRxUtilization_Type())
ifEthPhysicalRxUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRxUtilization.setStatus(_B)
class _IfEthPhysicalTxUtilization_Type(Unsigned32WithNA):subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
_IfEthPhysicalTxUtilization_Type.__name__=_F
_IfEthPhysicalTxUtilization_Object=MibTableColumn
ifEthPhysicalTxUtilization=_IfEthPhysicalTxUtilization_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,7),_IfEthPhysicalTxUtilization_Type())
ifEthPhysicalTxUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxUtilization.setStatus(_B)
_IfEthPhysicalTxSignalStatus_Type=SignalStatusWithNA
_IfEthPhysicalTxSignalStatus_Object=MibTableColumn
ifEthPhysicalTxSignalStatus=_IfEthPhysicalTxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,8),_IfEthPhysicalTxSignalStatus_Type())
ifEthPhysicalTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxSignalStatus.setStatus(_B)
_IfEthPhysicalRxSignalStatus_Type=SignalStatusWithNA
_IfEthPhysicalRxSignalStatus_Object=MibTableColumn
ifEthPhysicalRxSignalStatus=_IfEthPhysicalRxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,9),_IfEthPhysicalRxSignalStatus_Type())
ifEthPhysicalRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRxSignalStatus.setStatus(_B)
_IfEthPhysicalRemoteLinkFault_Type=FaultStatusWithNA
_IfEthPhysicalRemoteLinkFault_Object=MibTableColumn
ifEthPhysicalRemoteLinkFault=_IfEthPhysicalRemoteLinkFault_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,10),_IfEthPhysicalRemoteLinkFault_Type())
ifEthPhysicalRemoteLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRemoteLinkFault.setStatus(_B)
_IfEthPhysicalLocalLinkFault_Type=FaultStatusWithNA
_IfEthPhysicalLocalLinkFault_Object=MibTableColumn
ifEthPhysicalLocalLinkFault=_IfEthPhysicalLocalLinkFault_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,11),_IfEthPhysicalLocalLinkFault_Type())
ifEthPhysicalLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalLocalLinkFault.setStatus(_B)
_IfEthPhysicalLinkDown_Type=FaultStatusWithNA
_IfEthPhysicalLinkDown_Object=MibTableColumn
ifEthPhysicalLinkDown=_IfEthPhysicalLinkDown_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,12),_IfEthPhysicalLinkDown_Type())
ifEthPhysicalLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalLinkDown.setStatus(_B)
_IfEthPhysicalHighBitErrorRate_Type=FaultStatusWithNA
_IfEthPhysicalHighBitErrorRate_Object=MibTableColumn
ifEthPhysicalHighBitErrorRate=_IfEthPhysicalHighBitErrorRate_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,13),_IfEthPhysicalHighBitErrorRate_Type())
ifEthPhysicalHighBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalHighBitErrorRate.setStatus(_B)
_IfEthPhysicalPcsLossOfFrame_Type=FaultStatusWithNA
_IfEthPhysicalPcsLossOfFrame_Object=MibTableColumn
ifEthPhysicalPcsLossOfFrame=_IfEthPhysicalPcsLossOfFrame_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,14),_IfEthPhysicalPcsLossOfFrame_Type())
ifEthPhysicalPcsLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalPcsLossOfFrame.setStatus(_B)
_IfEthPhysicalRxLocalLinkFault_Type=FaultStatusWithNA
_IfEthPhysicalRxLocalLinkFault_Object=MibTableColumn
ifEthPhysicalRxLocalLinkFault=_IfEthPhysicalRxLocalLinkFault_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,15),_IfEthPhysicalRxLocalLinkFault_Type())
ifEthPhysicalRxLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRxLocalLinkFault.setStatus(_B)
_IfEthPhysicalTxLocalLinkFault_Type=FaultStatusWithNA
_IfEthPhysicalTxLocalLinkFault_Object=MibTableColumn
ifEthPhysicalTxLocalLinkFault=_IfEthPhysicalTxLocalLinkFault_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,16),_IfEthPhysicalTxLocalLinkFault_Type())
ifEthPhysicalTxLocalLinkFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxLocalLinkFault.setStatus(_B)
_IfEthPhysicalRxHighBitErrorRate_Type=FaultStatusWithNA
_IfEthPhysicalRxHighBitErrorRate_Object=MibTableColumn
ifEthPhysicalRxHighBitErrorRate=_IfEthPhysicalRxHighBitErrorRate_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,17),_IfEthPhysicalRxHighBitErrorRate_Type())
ifEthPhysicalRxHighBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRxHighBitErrorRate.setStatus(_B)
_IfEthPhysicalTxHighBitErrorRate_Type=FaultStatusWithNA
_IfEthPhysicalTxHighBitErrorRate_Object=MibTableColumn
ifEthPhysicalTxHighBitErrorRate=_IfEthPhysicalTxHighBitErrorRate_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,18),_IfEthPhysicalTxHighBitErrorRate_Type())
ifEthPhysicalTxHighBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxHighBitErrorRate.setStatus(_B)
_IfEthPhysicalTxPcsLossOfFrame_Type=FaultStatusWithNA
_IfEthPhysicalTxPcsLossOfFrame_Object=MibTableColumn
ifEthPhysicalTxPcsLossOfFrame=_IfEthPhysicalTxPcsLossOfFrame_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,19),_IfEthPhysicalTxPcsLossOfFrame_Type())
ifEthPhysicalTxPcsLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxPcsLossOfFrame.setStatus(_B)
_IfEthPhysicalUId_Type=Unsigned32
_IfEthPhysicalUId_Object=MibTableColumn
ifEthPhysicalUId=_IfEthPhysicalUId_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,20),_IfEthPhysicalUId_Type())
ifEthPhysicalUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalUId.setStatus(_B)
_IfEthPhysicalRxPcsLossOfSync_Type=FaultStatusWithNA
_IfEthPhysicalRxPcsLossOfSync_Object=MibTableColumn
ifEthPhysicalRxPcsLossOfSync=_IfEthPhysicalRxPcsLossOfSync_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,21),_IfEthPhysicalRxPcsLossOfSync_Type())
ifEthPhysicalRxPcsLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalRxPcsLossOfSync.setStatus(_B)
_IfEthPhysicalTxPcsLossOfSync_Type=FaultStatusWithNA
_IfEthPhysicalTxPcsLossOfSync_Object=MibTableColumn
ifEthPhysicalTxPcsLossOfSync=_IfEthPhysicalTxPcsLossOfSync_Object((1,3,6,1,4,1,8708,2,54,2,2,1,1,22),_IfEthPhysicalTxPcsLossOfSync_Type())
ifEthPhysicalTxPcsLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthPhysicalTxPcsLossOfSync.setStatus(_B)
_IfEthMacList_ObjectIdentity=ObjectIdentity
ifEthMacList=_IfEthMacList_ObjectIdentity((1,3,6,1,4,1,8708,2,54,2,3))
_IfEthMacTable_Object=MibTable
ifEthMacTable=_IfEthMacTable_Object((1,3,6,1,4,1,8708,2,54,2,3,1))
if mibBuilder.loadTexts:ifEthMacTable.setStatus(_B)
_IfEthMacEntry_Object=MibTableRow
ifEthMacEntry=_IfEthMacEntry_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1))
ifEthMacEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:ifEthMacEntry.setStatus(_B)
_IfEthMacIndex_Type=Unsigned32
_IfEthMacIndex_Object=MibTableColumn
ifEthMacIndex=_IfEthMacIndex_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,1),_IfEthMacIndex_Type())
ifEthMacIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacIndex.setStatus(_B)
_IfEthMacName_Type=MgmtNameString
_IfEthMacName_Object=MibTableColumn
ifEthMacName=_IfEthMacName_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,2),_IfEthMacName_Type())
ifEthMacName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacName.setStatus(_B)
_IfEthMacConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfEthMacConnIfBasicIfIndex_Object=MibTableColumn
ifEthMacConnIfBasicIfIndex=_IfEthMacConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,3),_IfEthMacConnIfBasicIfIndex_Type())
ifEthMacConnIfBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacConnIfBasicIfIndex.setStatus(_B)
class _IfEthMacRxUtilization_Type(Unsigned32WithNA):subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
_IfEthMacRxUtilization_Type.__name__=_F
_IfEthMacRxUtilization_Object=MibTableColumn
ifEthMacRxUtilization=_IfEthMacRxUtilization_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,4),_IfEthMacRxUtilization_Type())
ifEthMacRxUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacRxUtilization.setStatus(_B)
class _IfEthMacTxUtilization_Type(Unsigned32WithNA):subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000),ValueRangeConstraint(2147483646,2147483646),ValueRangeConstraint(2147483647,2147483647))
_IfEthMacTxUtilization_Type.__name__=_F
_IfEthMacTxUtilization_Object=MibTableColumn
ifEthMacTxUtilization=_IfEthMacTxUtilization_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,5),_IfEthMacTxUtilization_Type())
ifEthMacTxUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacTxUtilization.setStatus(_B)
class _IfEthMacMaxMtuSize_Type(Unsigned32WithNA):defaultValue=9600;subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600),ValueRangeConstraint(2147483647,2147483647))
_IfEthMacMaxMtuSize_Type.__name__=_F
_IfEthMacMaxMtuSize_Object=MibTableColumn
ifEthMacMaxMtuSize=_IfEthMacMaxMtuSize_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,6),_IfEthMacMaxMtuSize_Type())
ifEthMacMaxMtuSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacMaxMtuSize.setStatus(_B)
class _IfEthMacInterPacketGap_Type(Unsigned32WithNA):defaultValue=96;subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,456),ValueRangeConstraint(2147483647,2147483647))
_IfEthMacInterPacketGap_Type.__name__=_F
_IfEthMacInterPacketGap_Object=MibTableColumn
ifEthMacInterPacketGap=_IfEthMacInterPacketGap_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,7),_IfEthMacInterPacketGap_Type())
ifEthMacInterPacketGap.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacInterPacketGap.setStatus(_B)
class _IfEthMacFlowControlMode_Type(FlowControlMode):defaultValue=1
_IfEthMacFlowControlMode_Type.__name__=_m
_IfEthMacFlowControlMode_Object=MibTableColumn
ifEthMacFlowControlMode=_IfEthMacFlowControlMode_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,8),_IfEthMacFlowControlMode_Type())
ifEthMacFlowControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacFlowControlMode.setStatus(_B)
_IfEthMacTxSignalStatus_Type=SignalStatusWithNA
_IfEthMacTxSignalStatus_Object=MibTableColumn
ifEthMacTxSignalStatus=_IfEthMacTxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,9),_IfEthMacTxSignalStatus_Type())
ifEthMacTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacTxSignalStatus.setStatus(_B)
_IfEthMacRxSignalStatus_Type=SignalStatusWithNA
_IfEthMacRxSignalStatus_Object=MibTableColumn
ifEthMacRxSignalStatus=_IfEthMacRxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,3,1,1,10),_IfEthMacRxSignalStatus_Type())
ifEthMacRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthMacRxSignalStatus.setStatus(_B)
_IfEthRsFecList_ObjectIdentity=ObjectIdentity
ifEthRsFecList=_IfEthRsFecList_ObjectIdentity((1,3,6,1,4,1,8708,2,54,2,4))
_IfEthRsFecTable_Object=MibTable
ifEthRsFecTable=_IfEthRsFecTable_Object((1,3,6,1,4,1,8708,2,54,2,4,1))
if mibBuilder.loadTexts:ifEthRsFecTable.setStatus(_B)
_IfEthRsFecEntry_Object=MibTableRow
ifEthRsFecEntry=_IfEthRsFecEntry_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1))
ifEthRsFecEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:ifEthRsFecEntry.setStatus(_B)
_IfEthRsFecIndex_Type=Unsigned32
_IfEthRsFecIndex_Object=MibTableColumn
ifEthRsFecIndex=_IfEthRsFecIndex_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,1),_IfEthRsFecIndex_Type())
ifEthRsFecIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthRsFecIndex.setStatus(_B)
_IfEthRsFecName_Type=MgmtNameString
_IfEthRsFecName_Object=MibTableColumn
ifEthRsFecName=_IfEthRsFecName_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,2),_IfEthRsFecName_Type())
ifEthRsFecName.setMaxAccess(_p)
if mibBuilder.loadTexts:ifEthRsFecName.setStatus(_B)
_IfEthRsFecConnIfBasicIfIndex_Type=Unsigned32WithNA
_IfEthRsFecConnIfBasicIfIndex_Object=MibTableColumn
ifEthRsFecConnIfBasicIfIndex=_IfEthRsFecConnIfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,3),_IfEthRsFecConnIfBasicIfIndex_Type())
ifEthRsFecConnIfBasicIfIndex.setMaxAccess(_p)
if mibBuilder.loadTexts:ifEthRsFecConnIfBasicIfIndex.setStatus(_B)
_IfEthRsFecTxSignalStatus_Type=SignalStatusWithNA
_IfEthRsFecTxSignalStatus_Object=MibTableColumn
ifEthRsFecTxSignalStatus=_IfEthRsFecTxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,4),_IfEthRsFecTxSignalStatus_Type())
ifEthRsFecTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthRsFecTxSignalStatus.setStatus(_B)
_IfEthRsFecRxSignalStatus_Type=SignalStatusWithNA
_IfEthRsFecRxSignalStatus_Object=MibTableColumn
ifEthRsFecRxSignalStatus=_IfEthRsFecRxSignalStatus_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,5),_IfEthRsFecRxSignalStatus_Type())
ifEthRsFecRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthRsFecRxSignalStatus.setStatus(_B)
class _IfEthRsFecMode_Type(RsFecMode):defaultValue=2
_IfEthRsFecMode_Type.__name__=_n
_IfEthRsFecMode_Object=MibTableColumn
ifEthRsFecMode=_IfEthRsFecMode_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,6),_IfEthRsFecMode_Type())
ifEthRsFecMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:ifEthRsFecMode.setStatus(_B)
class _IfEthRsFecActualRsFec_Type(RsFecOnOff):defaultValue=2
_IfEthRsFecActualRsFec_Type.__name__=_o
_IfEthRsFecActualRsFec_Object=MibTableColumn
ifEthRsFecActualRsFec=_IfEthRsFecActualRsFec_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,7),_IfEthRsFecActualRsFec_Type())
ifEthRsFecActualRsFec.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthRsFecActualRsFec.setStatus(_B)
_IfEthRsFecLanesAlignmentError_Type=FaultStatusWithNA
_IfEthRsFecLanesAlignmentError_Object=MibTableColumn
ifEthRsFecLanesAlignmentError=_IfEthRsFecLanesAlignmentError_Object((1,3,6,1,4,1,8708,2,54,2,4,1,1,8),_IfEthRsFecLanesAlignmentError_Type())
ifEthRsFecLanesAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:ifEthRsFecLanesAlignmentError.setStatus(_B)
ifEthGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,1))
ifEthGeneralGroupV1.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ifEthGeneralGroupV1.setStatus(_D)
ifEthPhysicalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,2))
ifEthPhysicalGroupV1.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ifEthPhysicalGroupV1.setStatus(_D)
ifEthMacGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,3))
ifEthMacGroupV1.setObjects(*((_A,_a),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ifEthMacGroupV1.setStatus(_B)
ifEthPhysicalGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,4))
ifEthPhysicalGroupV2.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ifEthPhysicalGroupV2.setStatus(_D)
ifEthPhysicalGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,5))
ifEthPhysicalGroupV3.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:ifEthPhysicalGroupV3.setStatus(_D)
ifEthPhysicalGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,6))
ifEthPhysicalGroupV4.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_k)))
if mibBuilder.loadTexts:ifEthPhysicalGroupV4.setStatus(_D)
ifEthPhysicalGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,7))
ifEthPhysicalGroupV5.setObjects(*((_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_k),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ifEthPhysicalGroupV5.setStatus(_B)
ifEthRsFecGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,8))
ifEthRsFecGroupV1.setObjects(*((_A,_b),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ifEthRsFecGroupV1.setStatus(_B)
ifEthGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,54,1,1,9))
ifEthGeneralGroupV2.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ifEthGeneralGroupV2.setStatus(_B)
lumIfEthComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,1))
lumIfEthComplV1.setObjects(*((_A,_H),(_A,_AC),(_A,_E)))
if mibBuilder.loadTexts:lumIfEthComplV1.setStatus(_D)
lumIfEthComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,2))
lumIfEthComplV2.setObjects(*((_A,_H),(_A,_AD),(_A,_E)))
if mibBuilder.loadTexts:lumIfEthComplV2.setStatus(_D)
lumIfEthComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,3))
lumIfEthComplV3.setObjects(*((_A,_H),(_A,_AE),(_A,_E)))
if mibBuilder.loadTexts:lumIfEthComplV3.setStatus(_D)
lumIfEthComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,4))
lumIfEthComplV4.setObjects(*((_A,_H),(_A,_AF),(_A,_E)))
if mibBuilder.loadTexts:lumIfEthComplV4.setStatus(_D)
lumIfEthComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,5))
lumIfEthComplV5.setObjects(*((_A,_H),(_A,_Z),(_A,_E)))
if mibBuilder.loadTexts:lumIfEthComplV5.setStatus(_D)
lumIfEthComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,6))
lumIfEthComplV6.setObjects(*((_A,_H),(_A,_Z),(_A,_E),(_A,_l)))
if mibBuilder.loadTexts:lumIfEthComplV6.setStatus(_D)
lumIfEthComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,54,1,2,7))
lumIfEthComplV7.setObjects(*((_A,_AG),(_A,_Z),(_A,_E),(_A,_l)))
if mibBuilder.loadTexts:lumIfEthComplV7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfEthMIBModule':lumIfEthMIBModule,'lumIfEthConfs':lumIfEthConfs,'lumIfEthGroups':lumIfEthGroups,_H:ifEthGeneralGroupV1,_AC:ifEthPhysicalGroupV1,_E:ifEthMacGroupV1,_AD:ifEthPhysicalGroupV2,_AE:ifEthPhysicalGroupV3,_AF:ifEthPhysicalGroupV4,_Z:ifEthPhysicalGroupV5,_l:ifEthRsFecGroupV1,_AG:ifEthGeneralGroupV2,'lumIfEthCompl':lumIfEthCompl,'lumIfEthComplV1':lumIfEthComplV1,'lumIfEthComplV2':lumIfEthComplV2,'lumIfEthComplV3':lumIfEthComplV3,'lumIfEthComplV4':lumIfEthComplV4,'lumIfEthComplV5':lumIfEthComplV5,'lumIfEthComplV6':lumIfEthComplV6,'lumIfEthComplV7':lumIfEthComplV7,'lumIfEthMIBObjects':lumIfEthMIBObjects,'ifEthGeneral':ifEthGeneral,_c:ifEthGeneralConfigLastChangeTime,_d:ifEthGeneralStateLastChangeTime,_e:ifEthGeneralIfEthPhysicalTableSize,_f:ifEthGeneralIfEthPhysicalConfigLastChangeTime,_g:ifEthGeneralIfEthPhysicalStateLastChangeTime,_h:ifEthGeneralIfEthMacTableSize,_i:ifEthGeneralIfEthMacConfigLastChangeTime,_j:ifEthGeneralIfEthMacStateLastChangeTime,_A9:ifEthGeneralIfEthRsFecTableSize,_AA:ifEthGeneralIfEthRsFecConfigLastChangeTime,_AB:ifEthGeneralIfEthRsFecStateLastChangeTime,'ifEthPhysicalList':ifEthPhysicalList,'ifEthPhysicalTable':ifEthPhysicalTable,'ifEthPhysicalEntry':ifEthPhysicalEntry,_G:ifEthPhysicalIndex,_I:ifEthPhysicalName,_J:ifEthPhysicalConnIfBasicIfIndex,_K:ifEthPhysicalAutoNegotiationMode,_L:ifEthPhysicalAutoNegotiationStatus,_M:ifEthPhysicalRxUtilization,_N:ifEthPhysicalTxUtilization,_O:ifEthPhysicalTxSignalStatus,_P:ifEthPhysicalRxSignalStatus,_Q:ifEthPhysicalRemoteLinkFault,_R:ifEthPhysicalLocalLinkFault,_S:ifEthPhysicalLinkDown,_T:ifEthPhysicalHighBitErrorRate,_U:ifEthPhysicalPcsLossOfFrame,_V:ifEthPhysicalRxLocalLinkFault,_W:ifEthPhysicalTxLocalLinkFault,_X:ifEthPhysicalRxHighBitErrorRate,_Y:ifEthPhysicalTxHighBitErrorRate,_k:ifEthPhysicalTxPcsLossOfFrame,_z:ifEthPhysicalUId,_A0:ifEthPhysicalRxPcsLossOfSync,_A1:ifEthPhysicalTxPcsLossOfSync,'ifEthMacList':ifEthMacList,'ifEthMacTable':ifEthMacTable,'ifEthMacEntry':ifEthMacEntry,_a:ifEthMacIndex,_q:ifEthMacName,_r:ifEthMacConnIfBasicIfIndex,_s:ifEthMacRxUtilization,_t:ifEthMacTxUtilization,_u:ifEthMacMaxMtuSize,_v:ifEthMacInterPacketGap,_w:ifEthMacFlowControlMode,_x:ifEthMacTxSignalStatus,_y:ifEthMacRxSignalStatus,'ifEthRsFecList':ifEthRsFecList,'ifEthRsFecTable':ifEthRsFecTable,'ifEthRsFecEntry':ifEthRsFecEntry,_b:ifEthRsFecIndex,_A2:ifEthRsFecName,_A3:ifEthRsFecConnIfBasicIfIndex,_A4:ifEthRsFecTxSignalStatus,_A5:ifEthRsFecRxSignalStatus,_A6:ifEthRsFecMode,_A7:ifEthRsFecActualRsFec,_A8:ifEthRsFecLanesAlignmentError})