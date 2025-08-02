_V='run-diagnostics'
_U='cmmModuleID'
_T='CT-CMMPHYS-MIB'
_S='impaired'
_R='DisplayString'
_Q='ifIndex'
_P='IF-MIB'
_O='out-of-service'
_N='leaving-service'
_M='active'
_L='initializing'
_K='leave-service'
_J='down'
_I='mBusBoardID'
_H='CT-HSIMPHYS-MIB'
_G='faulty'
_F='false'
_E='true'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mBusBoardID,=mibBuilder.importSymbols(_H,_I)
ctCMM,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctCMM')
ifIndex,=mibBuilder.importSymbols(_P,_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','TextualConvention')
_CmmModemInfo_ObjectIdentity=ObjectIdentity
cmmModemInfo=_CmmModemInfo_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,18,1))
_CmmBoardTable_Object=MibTable
cmmBoardTable=_CmmBoardTable_Object((1,3,6,1,4,1,52,4,1,1,18,1,1))
if mibBuilder.loadTexts:cmmBoardTable.setStatus(_A)
_CmmBoardEntry_Object=MibTableRow
cmmBoardEntry=_CmmBoardEntry_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1))
cmmBoardEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cmmBoardEntry.setStatus(_A)
_CmmBoardType_Type=ObjectIdentifier
_CmmBoardType_Object=MibTableColumn
cmmBoardType=_CmmBoardType_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,1),_CmmBoardType_Type())
cmmBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmBoardType.setStatus(_A)
_CmmNumModules_Type=Integer32
_CmmNumModules_Object=MibTableColumn
cmmNumModules=_CmmNumModules_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,2),_CmmNumModules_Type())
cmmNumModules.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmNumModules.setStatus(_A)
_CmmModuleNumModems_Type=Integer32
_CmmModuleNumModems_Object=MibTableColumn
cmmModuleNumModems=_CmmModuleNumModems_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,3),_CmmModuleNumModems_Type())
cmmModuleNumModems.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmModuleNumModems.setStatus(_A)
_CmmTFTPServer_Type=IpAddress
_CmmTFTPServer_Object=MibTableColumn
cmmTFTPServer=_CmmTFTPServer_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,4),_CmmTFTPServer_Type())
cmmTFTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTFTPServer.setStatus(_A)
_CmmUpgradePath_Type=DisplayString
_CmmUpgradePath_Object=MibTableColumn
cmmUpgradePath=_CmmUpgradePath_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,5),_CmmUpgradePath_Type())
cmmUpgradePath.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmUpgradePath.setStatus(_A)
class _CmmUpgradeFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CmmUpgradeFlag_Type.__name__=_D
_CmmUpgradeFlag_Object=MibTableColumn
cmmUpgradeFlag=_CmmUpgradeFlag_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,6),_CmmUpgradeFlag_Type())
cmmUpgradeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmUpgradeFlag.setStatus(_A)
class _CmmCommitFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CmmCommitFlag_Type.__name__=_D
_CmmCommitFlag_Object=MibTableColumn
cmmCommitFlag=_CmmCommitFlag_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,7),_CmmCommitFlag_Type())
cmmCommitFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmCommitFlag.setStatus(_A)
_CmmModemResetLimit_Type=Integer32
_CmmModemResetLimit_Object=MibTableColumn
cmmModemResetLimit=_CmmModemResetLimit_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,8),_CmmModemResetLimit_Type())
cmmModemResetLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmModemResetLimit.setStatus(_A)
_CmmModemResetTime_Type=Integer32
_CmmModemResetTime_Object=MibTableColumn
cmmModemResetTime=_CmmModemResetTime_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,9),_CmmModemResetTime_Type())
cmmModemResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmModemResetTime.setStatus(_A)
_CmmOutgoingInactivityTimeout_Type=Integer32
_CmmOutgoingInactivityTimeout_Object=MibTableColumn
cmmOutgoingInactivityTimeout=_CmmOutgoingInactivityTimeout_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,10),_CmmOutgoingInactivityTimeout_Type())
cmmOutgoingInactivityTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmOutgoingInactivityTimeout.setStatus(_A)
_CmmIncomingInactivityTimeout_Type=Integer32
_CmmIncomingInactivityTimeout_Object=MibTableColumn
cmmIncomingInactivityTimeout=_CmmIncomingInactivityTimeout_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,11),_CmmIncomingInactivityTimeout_Type())
cmmIncomingInactivityTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIncomingInactivityTimeout.setStatus(_A)
_CmmAsyncBaseOrigATCmdStr_Type=DisplayString
_CmmAsyncBaseOrigATCmdStr_Object=MibTableColumn
cmmAsyncBaseOrigATCmdStr=_CmmAsyncBaseOrigATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,12),_CmmAsyncBaseOrigATCmdStr_Type())
cmmAsyncBaseOrigATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmAsyncBaseOrigATCmdStr.setStatus(_A)
_CmmAsyncBaseAnswerATCmdStr_Type=DisplayString
_CmmAsyncBaseAnswerATCmdStr_Object=MibTableColumn
cmmAsyncBaseAnswerATCmdStr=_CmmAsyncBaseAnswerATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,13),_CmmAsyncBaseAnswerATCmdStr_Type())
cmmAsyncBaseAnswerATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmAsyncBaseAnswerATCmdStr.setStatus(_A)
_CmmAsyncOrigStrModifier_Type=DisplayString
_CmmAsyncOrigStrModifier_Object=MibTableColumn
cmmAsyncOrigStrModifier=_CmmAsyncOrigStrModifier_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,14),_CmmAsyncOrigStrModifier_Type())
cmmAsyncOrigStrModifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmAsyncOrigStrModifier.setStatus(_A)
_CmmAsyncAnswerStrModifier_Type=DisplayString
_CmmAsyncAnswerStrModifier_Object=MibTableColumn
cmmAsyncAnswerStrModifier=_CmmAsyncAnswerStrModifier_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,15),_CmmAsyncAnswerStrModifier_Type())
cmmAsyncAnswerStrModifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmAsyncAnswerStrModifier.setStatus(_A)
_CmmAsyncOperOrigATCmdStr_Type=DisplayString
_CmmAsyncOperOrigATCmdStr_Object=MibTableColumn
cmmAsyncOperOrigATCmdStr=_CmmAsyncOperOrigATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,16),_CmmAsyncOperOrigATCmdStr_Type())
cmmAsyncOperOrigATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmAsyncOperOrigATCmdStr.setStatus(_A)
_CmmAsyncOperAnswerATCmdStr_Type=DisplayString
_CmmAsyncOperAnswerATCmdStr_Object=MibTableColumn
cmmAsyncOperAnswerATCmdStr=_CmmAsyncOperAnswerATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,17),_CmmAsyncOperAnswerATCmdStr_Type())
cmmAsyncOperAnswerATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmAsyncOperAnswerATCmdStr.setStatus(_A)
_CmmHdlcBaseOrigATCmdStr_Type=DisplayString
_CmmHdlcBaseOrigATCmdStr_Object=MibTableColumn
cmmHdlcBaseOrigATCmdStr=_CmmHdlcBaseOrigATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,18),_CmmHdlcBaseOrigATCmdStr_Type())
cmmHdlcBaseOrigATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmHdlcBaseOrigATCmdStr.setStatus(_A)
_CmmHdlcBaseAnswerATCmdStr_Type=DisplayString
_CmmHdlcBaseAnswerATCmdStr_Object=MibTableColumn
cmmHdlcBaseAnswerATCmdStr=_CmmHdlcBaseAnswerATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,19),_CmmHdlcBaseAnswerATCmdStr_Type())
cmmHdlcBaseAnswerATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmHdlcBaseAnswerATCmdStr.setStatus(_A)
_CmmHdlcOrigStrModifier_Type=DisplayString
_CmmHdlcOrigStrModifier_Object=MibTableColumn
cmmHdlcOrigStrModifier=_CmmHdlcOrigStrModifier_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,20),_CmmHdlcOrigStrModifier_Type())
cmmHdlcOrigStrModifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmHdlcOrigStrModifier.setStatus(_A)
_CmmHdlcAnswerStrModifier_Type=DisplayString
_CmmHdlcAnswerStrModifier_Object=MibTableColumn
cmmHdlcAnswerStrModifier=_CmmHdlcAnswerStrModifier_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,21),_CmmHdlcAnswerStrModifier_Type())
cmmHdlcAnswerStrModifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmHdlcAnswerStrModifier.setStatus(_A)
_CmmHdlcOperOrigATCmdStr_Type=DisplayString
_CmmHdlcOperOrigATCmdStr_Object=MibTableColumn
cmmHdlcOperOrigATCmdStr=_CmmHdlcOperOrigATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,22),_CmmHdlcOperOrigATCmdStr_Type())
cmmHdlcOperOrigATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmHdlcOperOrigATCmdStr.setStatus(_A)
_CmmHdlcOperAnswerATCmdStr_Type=DisplayString
_CmmHdlcOperAnswerATCmdStr_Object=MibTableColumn
cmmHdlcOperAnswerATCmdStr=_CmmHdlcOperAnswerATCmdStr_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,23),_CmmHdlcOperAnswerATCmdStr_Type())
cmmHdlcOperAnswerATCmdStr.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmHdlcOperAnswerATCmdStr.setStatus(_A)
class _CmmBoardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),('up',3),('upgrade',4)))
_CmmBoardAdminStatus_Type.__name__=_D
_CmmBoardAdminStatus_Object=MibTableColumn
cmmBoardAdminStatus=_CmmBoardAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,24),_CmmBoardAdminStatus_Type())
cmmBoardAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmBoardAdminStatus.setStatus(_A)
class _CmmBoardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_G,5),(_S,6)))
_CmmBoardOperStatus_Type.__name__=_D
_CmmBoardOperStatus_Object=MibTableColumn
cmmBoardOperStatus=_CmmBoardOperStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,1,1,25),_CmmBoardOperStatus_Type())
cmmBoardOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmBoardOperStatus.setStatus(_A)
_CmmModuleTable_Object=MibTable
cmmModuleTable=_CmmModuleTable_Object((1,3,6,1,4,1,52,4,1,1,18,1,2))
if mibBuilder.loadTexts:cmmModuleTable.setStatus(_A)
_CmmModuleEntry_Object=MibTableRow
cmmModuleEntry=_CmmModuleEntry_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1))
cmmModuleEntry.setIndexNames((0,_H,_I),(0,_T,_U))
if mibBuilder.loadTexts:cmmModuleEntry.setStatus(_A)
_CmmModuleID_Type=Integer32
_CmmModuleID_Object=MibTableColumn
cmmModuleID=_CmmModuleID_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,1),_CmmModuleID_Type())
cmmModuleID.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmModuleID.setStatus(_A)
_CmmDpramSize_Type=Integer32
_CmmDpramSize_Object=MibTableColumn
cmmDpramSize=_CmmDpramSize_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,2),_CmmDpramSize_Type())
cmmDpramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmDpramSize.setStatus(_A)
_CmmSdramSize_Type=Integer32
_CmmSdramSize_Object=MibTableColumn
cmmSdramSize=_CmmSdramSize_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,3),_CmmSdramSize_Type())
cmmSdramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmSdramSize.setStatus(_A)
class _CmmCpuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('hitachish3',2),('hitachish4',3)))
_CmmCpuType_Type.__name__=_D
_CmmCpuType_Object=MibTableColumn
cmmCpuType=_CmmCpuType_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,4),_CmmCpuType_Type())
cmmCpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCpuType.setStatus(_A)
_CmmCpuSpeed_Type=Integer32
_CmmCpuSpeed_Object=MibTableColumn
cmmCpuSpeed=_CmmCpuSpeed_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,5),_CmmCpuSpeed_Type())
cmmCpuSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCpuSpeed.setStatus(_A)
_CmmCpuFwRev_Type=DisplayString
_CmmCpuFwRev_Object=MibTableColumn
cmmCpuFwRev=_CmmCpuFwRev_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,6),_CmmCpuFwRev_Type())
cmmCpuFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCpuFwRev.setStatus(_A)
_CmmEpldId_Type=DisplayString
_CmmEpldId_Object=MibTableColumn
cmmEpldId=_CmmEpldId_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,7),_CmmEpldId_Type())
cmmEpldId.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmEpldId.setStatus(_A)
_CmmEpldRev_Type=DisplayString
_CmmEpldRev_Object=MibTableColumn
cmmEpldRev=_CmmEpldRev_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,8),_CmmEpldRev_Type())
cmmEpldRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmEpldRev.setStatus(_A)
_CmmNumBadModems_Type=Integer32
_CmmNumBadModems_Object=MibTableColumn
cmmNumBadModems=_CmmNumBadModems_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,9),_CmmNumBadModems_Type())
cmmNumBadModems.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmNumBadModems.setStatus(_A)
class _CmmModuleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_K,2),('up',3),(_V,4),('reset',5),(_G,6)))
_CmmModuleAdminStatus_Type.__name__=_D
_CmmModuleAdminStatus_Object=MibTableColumn
cmmModuleAdminStatus=_CmmModuleAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,10),_CmmModuleAdminStatus_Type())
cmmModuleAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmModuleAdminStatus.setStatus(_A)
class _CmmModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_G,5),(_S,6)))
_CmmModuleOperStatus_Type.__name__=_D
_CmmModuleOperStatus_Object=MibTableColumn
cmmModuleOperStatus=_CmmModuleOperStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,2,1,11),_CmmModuleOperStatus_Type())
cmmModuleOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmModuleOperStatus.setStatus(_A)
_CmmModemTable_Object=MibTable
cmmModemTable=_CmmModemTable_Object((1,3,6,1,4,1,52,4,1,1,18,1,3))
if mibBuilder.loadTexts:cmmModemTable.setStatus(_A)
_CmmModemEntry_Object=MibTableRow
cmmModemEntry=_CmmModemEntry_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1))
cmmModemEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:cmmModemEntry.setStatus(_A)
_CmmBoardID_Type=Integer32
_CmmBoardID_Object=MibTableColumn
cmmBoardID=_CmmBoardID_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,1),_CmmBoardID_Type())
cmmBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmBoardID.setStatus(_A)
_CmmModemID_Type=Integer32
_CmmModemID_Object=MibTableColumn
cmmModemID=_CmmModemID_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,2),_CmmModemID_Type())
cmmModemID.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmModemID.setStatus(_A)
_CmmIFNum_Type=Integer32
_CmmIFNum_Object=MibTableColumn
cmmIFNum=_CmmIFNum_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,3),_CmmIFNum_Type())
cmmIFNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmIFNum.setStatus(_A)
_CmmSessionNum_Type=Integer32
_CmmSessionNum_Object=MibTableColumn
cmmSessionNum=_CmmSessionNum_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,4),_CmmSessionNum_Type())
cmmSessionNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmSessionNum.setStatus(_A)
_CmmDdpPartNum_Type=DisplayString
_CmmDdpPartNum_Object=MibTableColumn
cmmDdpPartNum=_CmmDdpPartNum_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,5),_CmmDdpPartNum_Type())
cmmDdpPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmDdpPartNum.setStatus(_A)
_CmmDdpRevLevel_Type=DisplayString
_CmmDdpRevLevel_Object=MibTableColumn
cmmDdpRevLevel=_CmmDdpRevLevel_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,6),_CmmDdpRevLevel_Type())
cmmDdpRevLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmDdpRevLevel.setStatus(_A)
_CmmDdpFwRev_Type=DisplayString
_CmmDdpFwRev_Object=MibTableColumn
cmmDdpFwRev=_CmmDdpFwRev_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,7),_CmmDdpFwRev_Type())
cmmDdpFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmDdpFwRev.setStatus(_A)
_CmmDDPInterrupts_Type=Counter32
_CmmDDPInterrupts_Object=MibTableColumn
cmmDDPInterrupts=_CmmDDPInterrupts_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,8),_CmmDDPInterrupts_Type())
cmmDDPInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmDDPInterrupts.setStatus(_A)
_CmmRxFlowCtlEvts_Type=Counter32
_CmmRxFlowCtlEvts_Object=MibTableColumn
cmmRxFlowCtlEvts=_CmmRxFlowCtlEvts_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,9),_CmmRxFlowCtlEvts_Type())
cmmRxFlowCtlEvts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmRxFlowCtlEvts.setStatus(_A)
_CmmTxFlowCtlEvts_Type=Counter32
_CmmTxFlowCtlEvts_Object=MibTableColumn
cmmTxFlowCtlEvts=_CmmTxFlowCtlEvts_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,10),_CmmTxFlowCtlEvts_Type())
cmmTxFlowCtlEvts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmTxFlowCtlEvts.setStatus(_A)
class _CmmCallStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connected',2),('retraining',3),('dropping',4),('local-test',5),('remote-test',6)))
_CmmCallStatus_Type.__name__=_D
_CmmCallStatus_Object=MibTableColumn
cmmCallStatus=_CmmCallStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,11),_CmmCallStatus_Type())
cmmCallStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmCallStatus.setStatus(_A)
class _CmmCallOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('answer',1),('originate',2)))
_CmmCallOrigin_Type.__name__=_D
_CmmCallOrigin_Object=MibTableColumn
cmmCallOrigin=_CmmCallOrigin_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,12),_CmmCallOrigin_Type())
cmmCallOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCallOrigin.setStatus(_A)
_CmmRobbedBitDetected_Type=DisplayString
_CmmRobbedBitDetected_Object=MibTableColumn
cmmRobbedBitDetected=_CmmRobbedBitDetected_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,13),_CmmRobbedBitDetected_Type())
cmmRobbedBitDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmRobbedBitDetected.setStatus(_A)
class _CmmCorrectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('no-ec',1),('detection',2),('mnp',3),('hanging-up',4),('speed-matching',5),('lapm',6),('mnp10',7)))
_CmmCorrectionType_Type.__name__=_D
_CmmCorrectionType_Object=MibTableColumn
cmmCorrectionType=_CmmCorrectionType_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,14),_CmmCorrectionType_Type())
cmmCorrectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCorrectionType.setStatus(_A)
class _CmmCompressionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('mnp-class-5',2),('v42bis-tx-only',3),('v42bis-rx-only',4),('v42bis',5)))
_CmmCompressionType_Type.__name__=_D
_CmmCompressionType_Object=MibTableColumn
cmmCompressionType=_CmmCompressionType_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,15),_CmmCompressionType_Type())
cmmCompressionType.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCompressionType.setStatus(_A)
_CmmRxRate_Type=Integer32
_CmmRxRate_Object=MibTableColumn
cmmRxRate=_CmmRxRate_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,16),_CmmRxRate_Type())
cmmRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmRxRate.setStatus(_A)
_CmmTxRate_Type=Integer32
_CmmTxRate_Object=MibTableColumn
cmmTxRate=_CmmTxRate_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,17),_CmmTxRate_Type())
cmmTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmTxRate.setStatus(_A)
class _CmmEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('u-law',1),('a-law',2)))
_CmmEncoding_Type.__name__=_D
_CmmEncoding_Object=MibTableColumn
cmmEncoding=_CmmEncoding_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,18),_CmmEncoding_Type())
cmmEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmEncoding.setStatus(_A)
class _CmmFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pseudo-framing',1),('hdlc-framing',2),('ppp-async',3)))
_CmmFraming_Type.__name__=_D
_CmmFraming_Object=MibTableColumn
cmmFraming=_CmmFraming_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,19),_CmmFraming_Type())
cmmFraming.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmFraming.setStatus(_A)
_CmmInitialConnectRate_Type=Integer32
_CmmInitialConnectRate_Object=MibTableColumn
cmmInitialConnectRate=_CmmInitialConnectRate_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,20),_CmmInitialConnectRate_Type())
cmmInitialConnectRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmInitialConnectRate.setStatus(_A)
_CmmMaxHostWindows_Type=Integer32
_CmmMaxHostWindows_Object=MibTableColumn
cmmMaxHostWindows=_CmmMaxHostWindows_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,21),_CmmMaxHostWindows_Type())
cmmMaxHostWindows.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmMaxHostWindows.setStatus(_A)
_CmmMaxCmmWindows_Type=Integer32
_CmmMaxCmmWindows_Object=MibTableColumn
cmmMaxCmmWindows=_CmmMaxCmmWindows_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,22),_CmmMaxCmmWindows_Type())
cmmMaxCmmWindows.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmMaxCmmWindows.setStatus(_A)
_CmmNumOutHostAcks_Type=Gauge32
_CmmNumOutHostAcks_Object=MibTableColumn
cmmNumOutHostAcks=_CmmNumOutHostAcks_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,23),_CmmNumOutHostAcks_Type())
cmmNumOutHostAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmNumOutHostAcks.setStatus(_A)
_CmmNumOutCmmAcks_Type=Gauge32
_CmmNumOutCmmAcks_Object=MibTableColumn
cmmNumOutCmmAcks=_CmmNumOutCmmAcks_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,24),_CmmNumOutCmmAcks_Type())
cmmNumOutCmmAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmNumOutCmmAcks.setStatus(_A)
_CmmToNetworkOctets_Type=Counter32
_CmmToNetworkOctets_Object=MibTableColumn
cmmToNetworkOctets=_CmmToNetworkOctets_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,25),_CmmToNetworkOctets_Type())
cmmToNetworkOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmToNetworkOctets.setStatus(_A)
_CmmFromNetworkOctets_Type=Counter32
_CmmFromNetworkOctets_Object=MibTableColumn
cmmFromNetworkOctets=_CmmFromNetworkOctets_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,26),_CmmFromNetworkOctets_Type())
cmmFromNetworkOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmFromNetworkOctets.setStatus(_A)
_CmmToHostOctets_Type=Counter32
_CmmToHostOctets_Object=MibTableColumn
cmmToHostOctets=_CmmToHostOctets_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,27),_CmmToHostOctets_Type())
cmmToHostOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmToHostOctets.setStatus(_A)
_CmmFromHostOctets_Type=Counter32
_CmmFromHostOctets_Object=MibTableColumn
cmmFromHostOctets=_CmmFromHostOctets_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,28),_CmmFromHostOctets_Type())
cmmFromHostOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmFromHostOctets.setStatus(_A)
_CmmToNetworkFrames_Type=Counter32
_CmmToNetworkFrames_Object=MibTableColumn
cmmToNetworkFrames=_CmmToNetworkFrames_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,29),_CmmToNetworkFrames_Type())
cmmToNetworkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmToNetworkFrames.setStatus(_A)
_CmmFromNetworkFrames_Type=Counter32
_CmmFromNetworkFrames_Object=MibTableColumn
cmmFromNetworkFrames=_CmmFromNetworkFrames_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,30),_CmmFromNetworkFrames_Type())
cmmFromNetworkFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmFromNetworkFrames.setStatus(_A)
_CmmOversizeFrames_Type=Counter32
_CmmOversizeFrames_Object=MibTableColumn
cmmOversizeFrames=_CmmOversizeFrames_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,31),_CmmOversizeFrames_Type())
cmmOversizeFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmOversizeFrames.setStatus(_A)
_CmmOverrunErrors_Type=Counter32
_CmmOverrunErrors_Object=MibTableColumn
cmmOverrunErrors=_CmmOverrunErrors_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,32),_CmmOverrunErrors_Type())
cmmOverrunErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmOverrunErrors.setStatus(_A)
_CmmCRCErrors_Type=Counter32
_CmmCRCErrors_Object=MibTableColumn
cmmCRCErrors=_CmmCRCErrors_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,33),_CmmCRCErrors_Type())
cmmCRCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCRCErrors.setStatus(_A)
_CmmAbortedFrames_Type=Counter32
_CmmAbortedFrames_Object=MibTableColumn
cmmAbortedFrames=_CmmAbortedFrames_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,34),_CmmAbortedFrames_Type())
cmmAbortedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmAbortedFrames.setStatus(_A)
_CmmRetrainEvents_Type=Counter32
_CmmRetrainEvents_Object=MibTableColumn
cmmRetrainEvents=_CmmRetrainEvents_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,35),_CmmRetrainEvents_Type())
cmmRetrainEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmRetrainEvents.setStatus(_A)
_CmmARAEvents_Type=Counter32
_CmmARAEvents_Object=MibTableColumn
cmmARAEvents=_CmmARAEvents_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,36),_CmmARAEvents_Type())
cmmARAEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmARAEvents.setStatus(_A)
class _CmmARAFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CmmARAFlag_Type.__name__=_D
_CmmARAFlag_Object=MibTableColumn
cmmARAFlag=_CmmARAFlag_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,37),_CmmARAFlag_Type())
cmmARAFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmARAFlag.setStatus(_A)
_CmmCarrierLossEvents_Type=Counter32
_CmmCarrierLossEvents_Object=MibTableColumn
cmmCarrierLossEvents=_CmmCarrierLossEvents_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,38),_CmmCarrierLossEvents_Type())
cmmCarrierLossEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCarrierLossEvents.setStatus(_A)
class _CmmCarrierLossFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CmmCarrierLossFlag_Type.__name__=_D
_CmmCarrierLossFlag_Object=MibTableColumn
cmmCarrierLossFlag=_CmmCarrierLossFlag_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,39),_CmmCarrierLossFlag_Type())
cmmCarrierLossFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmCarrierLossFlag.setStatus(_A)
_CmmRcvSignalLevel_Type=Integer32
_CmmRcvSignalLevel_Object=MibTableColumn
cmmRcvSignalLevel=_CmmRcvSignalLevel_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,40),_CmmRcvSignalLevel_Type())
cmmRcvSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmRcvSignalLevel.setStatus(_A)
_CmmRcvSignalEQM_Type=Integer32
_CmmRcvSignalEQM_Object=MibTableColumn
cmmRcvSignalEQM=_CmmRcvSignalEQM_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,41),_CmmRcvSignalEQM_Type())
cmmRcvSignalEQM.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmRcvSignalEQM.setStatus(_A)
_CmmTDMSlot_Type=Integer32
_CmmTDMSlot_Object=MibTableColumn
cmmTDMSlot=_CmmTDMSlot_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,42),_CmmTDMSlot_Type())
cmmTDMSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmTDMSlot.setStatus(_A)
class _CmmResetModemStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CmmResetModemStats_Type.__name__=_D
_CmmResetModemStats_Object=MibTableColumn
cmmResetModemStats=_CmmResetModemStats_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,43),_CmmResetModemStats_Type())
cmmResetModemStats.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmResetModemStats.setStatus(_A)
class _CmmModemAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_K,2),('up',3),(_V,4),('reset',5),(_G,6)))
_CmmModemAdminStatus_Type.__name__=_D
_CmmModemAdminStatus_Object=MibTableColumn
cmmModemAdminStatus=_CmmModemAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,44),_CmmModemAdminStatus_Type())
cmmModemAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmModemAdminStatus.setStatus(_A)
class _CmmModemOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('idle',2),(_M,3),(_N,4),(_O,5),('testing',6),(_G,7),('resetting',8)))
_CmmModemOperStatus_Type.__name__=_D
_CmmModemOperStatus_Object=MibTableColumn
cmmModemOperStatus=_CmmModemOperStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,3,1,45),_CmmModemOperStatus_Type())
cmmModemOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmModemOperStatus.setStatus(_A)
_CmmFreeFormAtCmdGroup_ObjectIdentity=ObjectIdentity
cmmFreeFormAtCmdGroup=_CmmFreeFormAtCmdGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,18,1,5))
_CmmATCommand_Type=OctetString
_CmmATCommand_Object=MibScalar
cmmATCommand=_CmmATCommand_Object((1,3,6,1,4,1,52,4,1,1,18,1,5,1),_CmmATCommand_Type())
cmmATCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmATCommand.setStatus(_A)
_CmmSelectedModem_Type=Integer32
_CmmSelectedModem_Object=MibScalar
cmmSelectedModem=_CmmSelectedModem_Object((1,3,6,1,4,1,52,4,1,1,18,1,5,2),_CmmSelectedModem_Type())
cmmSelectedModem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmSelectedModem.setStatus(_A)
class _CmmATCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sending',1),('not-sending',2)))
_CmmATCmdStatus_Type.__name__=_D
_CmmATCmdStatus_Object=MibScalar
cmmATCmdStatus=_CmmATCmdStatus_Object((1,3,6,1,4,1,52,4,1,1,18,1,5,3),_CmmATCmdStatus_Type())
cmmATCmdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmATCmdStatus.setStatus(_A)
class _CmmATCmdResult_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CmmATCmdResult_Type.__name__=_R
_CmmATCmdResult_Object=MibScalar
cmmATCmdResult=_CmmATCmdResult_Object((1,3,6,1,4,1,52,4,1,1,18,1,5,4),_CmmATCmdResult_Type())
cmmATCmdResult.setMaxAccess(_B)
if mibBuilder.loadTexts:cmmATCmdResult.setStatus(_A)
mibBuilder.exportSymbols(_T,**{'cmmModemInfo':cmmModemInfo,'cmmBoardTable':cmmBoardTable,'cmmBoardEntry':cmmBoardEntry,'cmmBoardType':cmmBoardType,'cmmNumModules':cmmNumModules,'cmmModuleNumModems':cmmModuleNumModems,'cmmTFTPServer':cmmTFTPServer,'cmmUpgradePath':cmmUpgradePath,'cmmUpgradeFlag':cmmUpgradeFlag,'cmmCommitFlag':cmmCommitFlag,'cmmModemResetLimit':cmmModemResetLimit,'cmmModemResetTime':cmmModemResetTime,'cmmOutgoingInactivityTimeout':cmmOutgoingInactivityTimeout,'cmmIncomingInactivityTimeout':cmmIncomingInactivityTimeout,'cmmAsyncBaseOrigATCmdStr':cmmAsyncBaseOrigATCmdStr,'cmmAsyncBaseAnswerATCmdStr':cmmAsyncBaseAnswerATCmdStr,'cmmAsyncOrigStrModifier':cmmAsyncOrigStrModifier,'cmmAsyncAnswerStrModifier':cmmAsyncAnswerStrModifier,'cmmAsyncOperOrigATCmdStr':cmmAsyncOperOrigATCmdStr,'cmmAsyncOperAnswerATCmdStr':cmmAsyncOperAnswerATCmdStr,'cmmHdlcBaseOrigATCmdStr':cmmHdlcBaseOrigATCmdStr,'cmmHdlcBaseAnswerATCmdStr':cmmHdlcBaseAnswerATCmdStr,'cmmHdlcOrigStrModifier':cmmHdlcOrigStrModifier,'cmmHdlcAnswerStrModifier':cmmHdlcAnswerStrModifier,'cmmHdlcOperOrigATCmdStr':cmmHdlcOperOrigATCmdStr,'cmmHdlcOperAnswerATCmdStr':cmmHdlcOperAnswerATCmdStr,'cmmBoardAdminStatus':cmmBoardAdminStatus,'cmmBoardOperStatus':cmmBoardOperStatus,'cmmModuleTable':cmmModuleTable,'cmmModuleEntry':cmmModuleEntry,_U:cmmModuleID,'cmmDpramSize':cmmDpramSize,'cmmSdramSize':cmmSdramSize,'cmmCpuType':cmmCpuType,'cmmCpuSpeed':cmmCpuSpeed,'cmmCpuFwRev':cmmCpuFwRev,'cmmEpldId':cmmEpldId,'cmmEpldRev':cmmEpldRev,'cmmNumBadModems':cmmNumBadModems,'cmmModuleAdminStatus':cmmModuleAdminStatus,'cmmModuleOperStatus':cmmModuleOperStatus,'cmmModemTable':cmmModemTable,'cmmModemEntry':cmmModemEntry,'cmmBoardID':cmmBoardID,'cmmModemID':cmmModemID,'cmmIFNum':cmmIFNum,'cmmSessionNum':cmmSessionNum,'cmmDdpPartNum':cmmDdpPartNum,'cmmDdpRevLevel':cmmDdpRevLevel,'cmmDdpFwRev':cmmDdpFwRev,'cmmDDPInterrupts':cmmDDPInterrupts,'cmmRxFlowCtlEvts':cmmRxFlowCtlEvts,'cmmTxFlowCtlEvts':cmmTxFlowCtlEvts,'cmmCallStatus':cmmCallStatus,'cmmCallOrigin':cmmCallOrigin,'cmmRobbedBitDetected':cmmRobbedBitDetected,'cmmCorrectionType':cmmCorrectionType,'cmmCompressionType':cmmCompressionType,'cmmRxRate':cmmRxRate,'cmmTxRate':cmmTxRate,'cmmEncoding':cmmEncoding,'cmmFraming':cmmFraming,'cmmInitialConnectRate':cmmInitialConnectRate,'cmmMaxHostWindows':cmmMaxHostWindows,'cmmMaxCmmWindows':cmmMaxCmmWindows,'cmmNumOutHostAcks':cmmNumOutHostAcks,'cmmNumOutCmmAcks':cmmNumOutCmmAcks,'cmmToNetworkOctets':cmmToNetworkOctets,'cmmFromNetworkOctets':cmmFromNetworkOctets,'cmmToHostOctets':cmmToHostOctets,'cmmFromHostOctets':cmmFromHostOctets,'cmmToNetworkFrames':cmmToNetworkFrames,'cmmFromNetworkFrames':cmmFromNetworkFrames,'cmmOversizeFrames':cmmOversizeFrames,'cmmOverrunErrors':cmmOverrunErrors,'cmmCRCErrors':cmmCRCErrors,'cmmAbortedFrames':cmmAbortedFrames,'cmmRetrainEvents':cmmRetrainEvents,'cmmARAEvents':cmmARAEvents,'cmmARAFlag':cmmARAFlag,'cmmCarrierLossEvents':cmmCarrierLossEvents,'cmmCarrierLossFlag':cmmCarrierLossFlag,'cmmRcvSignalLevel':cmmRcvSignalLevel,'cmmRcvSignalEQM':cmmRcvSignalEQM,'cmmTDMSlot':cmmTDMSlot,'cmmResetModemStats':cmmResetModemStats,'cmmModemAdminStatus':cmmModemAdminStatus,'cmmModemOperStatus':cmmModemOperStatus,'cmmFreeFormAtCmdGroup':cmmFreeFormAtCmdGroup,'cmmATCommand':cmmATCommand,'cmmSelectedModem':cmmSelectedModem,'cmmATCmdStatus':cmmATCmdStatus,'cmmATCmdResult':cmmATCmdResult})