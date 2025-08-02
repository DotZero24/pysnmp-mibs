_A3='mplsBfdSessGroupV2'
_A2='mplsBfdSessGroupV1'
_A1='mplsOamBfdSessTrafficClass'
_A0='mplsOamBfdSessReqMinRxInterval'
_z='mplsOamBfdSessDesiredMinTxInterval'
_y='mplsOamBfdTemplateRowStatus'
_x='mplsOamBfdTemplateCreateNewTemplate'
_w='mplsOamBfdTemplateReqMinRxInterval'
_v='mplsOamBfdTemplateDetectMult'
_u='mplsOamBfdTemplateDesiredMinTxInterval'
_t='mplsOamBfdTemplateIdentifier'
_s='mplsOamBfdTemplateName'
_r='mplsOamBfdTemplateInternalReference'
_q='deprecated'
_p='mplsOamGeneralmplsOamBfdSessTableSize'
_o='mplsOamGeneralStateLastChangeTime'
_n='mplsOamGeneralLastChangeTime'
_m='BfdMultiplierTC'
_l='read-write'
_k='mplsBfdTemplateGroupV1'
_j='mplsIOamGeneralGroupV1'
_i='mplsOamBfdSessRowStatus'
_h='mplsOamBfdSessRemoteAdminDown'
_g='mplsOamBfdSessRemoteTimerExpired'
_f='mplsOamBfdSessRemoteMisConnectivity'
_e='mplsOamBfdSessLocalTimerExpired'
_d='mplsOamBfdSessLocalMisConnectivity'
_c='mplsOamBfdSessLocalNotConnected'
_b='mplsOamBfdSessMepNotConfigured'
_a='mplsOamBfdSessRcvTargetMepId'
_Z='mplsOamBfdSessTargetMepId'
_Y='mplsOamBfdSessSourceMepId'
_X='mplsOamBfdSessTemplateIndex'
_W='mplsOamBfdSessTemplate'
_V='mplsOamBfdSessMonitoringPathIndex'
_U='mplsOamBfdSessMonitoringPathType'
_T='mplsOamBfdSessMonitoringPath'
_S='mplsOamBfdSessNegotiatedRxInterval'
_R='mplsOamBfdSessNegotiatedTxInterval'
_Q='mplsOamBfdSessRemoteDiag'
_P='mplsOamBfdSessDiag'
_O='mplsOamBfdSessRemoteState'
_N='mplsOamBfdSessState'
_M='mplsOamBfdSessAdminStatus'
_L='mplsOamBfdSessName'
_K='mplsOamBfdSessInternalReference'
_J='mplsOamBfdTemplateIndex'
_I='Integer32'
_H='mplsOamBfdSessIndex'
_G='DisplayString'
_F='BfdIntervalTC'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='current'
_A='LUM-MPLSOAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumMplsOamMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumMplsOamMIB')
CommandString,FaultStatus,MgmtNameString=mibBuilder.importSymbols('LUM-TC','CommandString','FaultStatus','MgmtNameString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','RowStatus','TextualConvention')
lumMplsOamMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,44))
if mibBuilder.loadTexts:lumMplsOamMIBModule.setRevisions(('2017-06-15 00:00','2012-12-25 12:00','2012-03-01 12:00'))
class BfdSessStateTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('adminDown',1),('down',2),('init',3),('up',4),('failing',5)))
class BfdMultiplierTC(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class BfdIntervalTC(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
class BfdDiagTC(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDiagnostic',0),('controlDetectionTimeExpired',1),('echoFunctionFailed',2),('neighborSignaledSessionDown',3),('forwardingPlaneReset',4),('pathDown',5),('concatenatedPathDown',6),('administrativelyDown',7),('reverseConcatenatedPathDown',8),('misconnectionDefect',9)))
_LumMplsOamConfs_ObjectIdentity=ObjectIdentity
lumMplsOamConfs=_LumMplsOamConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,44,1))
_LumMplsOamGroups_ObjectIdentity=ObjectIdentity
lumMplsOamGroups=_LumMplsOamGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,44,1,1))
_LumMplsOamCompl_ObjectIdentity=ObjectIdentity
lumMplsOamCompl=_LumMplsOamCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,44,1,2))
_LumMplsOamMIBObjects_ObjectIdentity=ObjectIdentity
lumMplsOamMIBObjects=_LumMplsOamMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,44,2))
_MplsOamGeneral_ObjectIdentity=ObjectIdentity
mplsOamGeneral=_MplsOamGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,44,2,1))
_MplsOamGeneralLastChangeTime_Type=DateAndTime
_MplsOamGeneralLastChangeTime_Object=MibScalar
mplsOamGeneralLastChangeTime=_MplsOamGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,44,2,1,1),_MplsOamGeneralLastChangeTime_Type())
mplsOamGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamGeneralLastChangeTime.setStatus(_B)
_MplsOamGeneralStateLastChangeTime_Type=DateAndTime
_MplsOamGeneralStateLastChangeTime_Object=MibScalar
mplsOamGeneralStateLastChangeTime=_MplsOamGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,44,2,1,2),_MplsOamGeneralStateLastChangeTime_Type())
mplsOamGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamGeneralStateLastChangeTime.setStatus(_B)
_MplsOamGeneralmplsOamBfdSessTableSize_Type=Unsigned32
_MplsOamGeneralmplsOamBfdSessTableSize_Object=MibScalar
mplsOamGeneralmplsOamBfdSessTableSize=_MplsOamGeneralmplsOamBfdSessTableSize_Object((1,3,6,1,4,1,8708,2,44,2,1,3),_MplsOamGeneralmplsOamBfdSessTableSize_Type())
mplsOamGeneralmplsOamBfdSessTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamGeneralmplsOamBfdSessTableSize.setStatus(_B)
_MplsOamGeneralmplsOamBfdTemplateTableSize_Type=Unsigned32
_MplsOamGeneralmplsOamBfdTemplateTableSize_Object=MibScalar
mplsOamGeneralmplsOamBfdTemplateTableSize=_MplsOamGeneralmplsOamBfdTemplateTableSize_Object((1,3,6,1,4,1,8708,2,44,2,1,4),_MplsOamGeneralmplsOamBfdTemplateTableSize_Type())
mplsOamGeneralmplsOamBfdTemplateTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamGeneralmplsOamBfdTemplateTableSize.setStatus(_B)
_MplsOamBfdSess_ObjectIdentity=ObjectIdentity
mplsOamBfdSess=_MplsOamBfdSess_ObjectIdentity((1,3,6,1,4,1,8708,2,44,2,2))
_MplsOamBfdSessTable_Object=MibTable
mplsOamBfdSessTable=_MplsOamBfdSessTable_Object((1,3,6,1,4,1,8708,2,44,2,2,1))
if mibBuilder.loadTexts:mplsOamBfdSessTable.setStatus(_B)
_MplsOamBfdSessEntry_Object=MibTableRow
mplsOamBfdSessEntry=_MplsOamBfdSessEntry_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1))
mplsOamBfdSessEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:mplsOamBfdSessEntry.setStatus(_B)
class _MplsOamBfdSessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsOamBfdSessIndex_Type.__name__=_E
_MplsOamBfdSessIndex_Object=MibTableColumn
mplsOamBfdSessIndex=_MplsOamBfdSessIndex_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,1),_MplsOamBfdSessIndex_Type())
mplsOamBfdSessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessIndex.setStatus(_B)
class _MplsOamBfdSessInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOamBfdSessInternalReference_Type.__name__=_E
_MplsOamBfdSessInternalReference_Object=MibTableColumn
mplsOamBfdSessInternalReference=_MplsOamBfdSessInternalReference_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,2),_MplsOamBfdSessInternalReference_Type())
mplsOamBfdSessInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdSessInternalReference.setStatus(_B)
_MplsOamBfdSessName_Type=MgmtNameString
_MplsOamBfdSessName_Object=MibTableColumn
mplsOamBfdSessName=_MplsOamBfdSessName_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,3),_MplsOamBfdSessName_Type())
mplsOamBfdSessName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessName.setStatus(_B)
class _MplsOamBfdSessAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MplsOamBfdSessAdminStatus_Type.__name__=_I
_MplsOamBfdSessAdminStatus_Object=MibTableColumn
mplsOamBfdSessAdminStatus=_MplsOamBfdSessAdminStatus_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,4),_MplsOamBfdSessAdminStatus_Type())
mplsOamBfdSessAdminStatus.setMaxAccess(_l)
if mibBuilder.loadTexts:mplsOamBfdSessAdminStatus.setStatus(_B)
_MplsOamBfdSessState_Type=BfdSessStateTC
_MplsOamBfdSessState_Object=MibTableColumn
mplsOamBfdSessState=_MplsOamBfdSessState_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,5),_MplsOamBfdSessState_Type())
mplsOamBfdSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessState.setStatus(_B)
_MplsOamBfdSessRemoteState_Type=BfdSessStateTC
_MplsOamBfdSessRemoteState_Object=MibTableColumn
mplsOamBfdSessRemoteState=_MplsOamBfdSessRemoteState_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,6),_MplsOamBfdSessRemoteState_Type())
mplsOamBfdSessRemoteState.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRemoteState.setStatus(_B)
_MplsOamBfdSessDiag_Type=BfdDiagTC
_MplsOamBfdSessDiag_Object=MibTableColumn
mplsOamBfdSessDiag=_MplsOamBfdSessDiag_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,7),_MplsOamBfdSessDiag_Type())
mplsOamBfdSessDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessDiag.setStatus(_B)
_MplsOamBfdSessRemoteDiag_Type=BfdDiagTC
_MplsOamBfdSessRemoteDiag_Object=MibTableColumn
mplsOamBfdSessRemoteDiag=_MplsOamBfdSessRemoteDiag_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,8),_MplsOamBfdSessRemoteDiag_Type())
mplsOamBfdSessRemoteDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRemoteDiag.setStatus(_B)
_MplsOamBfdSessNegotiatedTxInterval_Type=BfdIntervalTC
_MplsOamBfdSessNegotiatedTxInterval_Object=MibTableColumn
mplsOamBfdSessNegotiatedTxInterval=_MplsOamBfdSessNegotiatedTxInterval_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,9),_MplsOamBfdSessNegotiatedTxInterval_Type())
mplsOamBfdSessNegotiatedTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessNegotiatedTxInterval.setStatus(_B)
_MplsOamBfdSessNegotiatedRxInterval_Type=BfdIntervalTC
_MplsOamBfdSessNegotiatedRxInterval_Object=MibTableColumn
mplsOamBfdSessNegotiatedRxInterval=_MplsOamBfdSessNegotiatedRxInterval_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,10),_MplsOamBfdSessNegotiatedRxInterval_Type())
mplsOamBfdSessNegotiatedRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessNegotiatedRxInterval.setStatus(_B)
class _MplsOamBfdSessMonitoringPath_Type(DisplayString):defaultValue=OctetString('')
_MplsOamBfdSessMonitoringPath_Type.__name__=_G
_MplsOamBfdSessMonitoringPath_Object=MibTableColumn
mplsOamBfdSessMonitoringPath=_MplsOamBfdSessMonitoringPath_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,11),_MplsOamBfdSessMonitoringPath_Type())
mplsOamBfdSessMonitoringPath.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdSessMonitoringPath.setStatus(_B)
class _MplsOamBfdSessMonitoringPathType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notSelected',0),('lsp',1)))
_MplsOamBfdSessMonitoringPathType_Type.__name__=_I
_MplsOamBfdSessMonitoringPathType_Object=MibTableColumn
mplsOamBfdSessMonitoringPathType=_MplsOamBfdSessMonitoringPathType_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,12),_MplsOamBfdSessMonitoringPathType_Type())
mplsOamBfdSessMonitoringPathType.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdSessMonitoringPathType.setStatus(_B)
class _MplsOamBfdSessMonitoringPathIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsOamBfdSessMonitoringPathIndex_Type.__name__=_E
_MplsOamBfdSessMonitoringPathIndex_Object=MibTableColumn
mplsOamBfdSessMonitoringPathIndex=_MplsOamBfdSessMonitoringPathIndex_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,13),_MplsOamBfdSessMonitoringPathIndex_Type())
mplsOamBfdSessMonitoringPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessMonitoringPathIndex.setStatus(_B)
class _MplsOamBfdSessTemplate_Type(DisplayString):defaultValue=OctetString('')
_MplsOamBfdSessTemplate_Type.__name__=_G
_MplsOamBfdSessTemplate_Object=MibTableColumn
mplsOamBfdSessTemplate=_MplsOamBfdSessTemplate_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,14),_MplsOamBfdSessTemplate_Type())
mplsOamBfdSessTemplate.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdSessTemplate.setStatus(_B)
class _MplsOamBfdSessTemplateIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsOamBfdSessTemplateIndex_Type.__name__=_E
_MplsOamBfdSessTemplateIndex_Object=MibTableColumn
mplsOamBfdSessTemplateIndex=_MplsOamBfdSessTemplateIndex_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,15),_MplsOamBfdSessTemplateIndex_Type())
mplsOamBfdSessTemplateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessTemplateIndex.setStatus(_B)
_MplsOamBfdSessSourceMepId_Type=DisplayString
_MplsOamBfdSessSourceMepId_Object=MibTableColumn
mplsOamBfdSessSourceMepId=_MplsOamBfdSessSourceMepId_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,16),_MplsOamBfdSessSourceMepId_Type())
mplsOamBfdSessSourceMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessSourceMepId.setStatus(_B)
_MplsOamBfdSessTargetMepId_Type=DisplayString
_MplsOamBfdSessTargetMepId_Object=MibTableColumn
mplsOamBfdSessTargetMepId=_MplsOamBfdSessTargetMepId_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,17),_MplsOamBfdSessTargetMepId_Type())
mplsOamBfdSessTargetMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessTargetMepId.setStatus(_B)
_MplsOamBfdSessRcvTargetMepId_Type=DisplayString
_MplsOamBfdSessRcvTargetMepId_Object=MibTableColumn
mplsOamBfdSessRcvTargetMepId=_MplsOamBfdSessRcvTargetMepId_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,18),_MplsOamBfdSessRcvTargetMepId_Type())
mplsOamBfdSessRcvTargetMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRcvTargetMepId.setStatus(_B)
_MplsOamBfdSessMepNotConfigured_Type=FaultStatus
_MplsOamBfdSessMepNotConfigured_Object=MibTableColumn
mplsOamBfdSessMepNotConfigured=_MplsOamBfdSessMepNotConfigured_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,19),_MplsOamBfdSessMepNotConfigured_Type())
mplsOamBfdSessMepNotConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessMepNotConfigured.setStatus(_B)
_MplsOamBfdSessLocalNotConnected_Type=FaultStatus
_MplsOamBfdSessLocalNotConnected_Object=MibTableColumn
mplsOamBfdSessLocalNotConnected=_MplsOamBfdSessLocalNotConnected_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,20),_MplsOamBfdSessLocalNotConnected_Type())
mplsOamBfdSessLocalNotConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessLocalNotConnected.setStatus(_B)
_MplsOamBfdSessLocalMisConnectivity_Type=FaultStatus
_MplsOamBfdSessLocalMisConnectivity_Object=MibTableColumn
mplsOamBfdSessLocalMisConnectivity=_MplsOamBfdSessLocalMisConnectivity_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,21),_MplsOamBfdSessLocalMisConnectivity_Type())
mplsOamBfdSessLocalMisConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessLocalMisConnectivity.setStatus(_B)
_MplsOamBfdSessLocalTimerExpired_Type=FaultStatus
_MplsOamBfdSessLocalTimerExpired_Object=MibTableColumn
mplsOamBfdSessLocalTimerExpired=_MplsOamBfdSessLocalTimerExpired_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,22),_MplsOamBfdSessLocalTimerExpired_Type())
mplsOamBfdSessLocalTimerExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessLocalTimerExpired.setStatus(_B)
_MplsOamBfdSessRemoteMisConnectivity_Type=FaultStatus
_MplsOamBfdSessRemoteMisConnectivity_Object=MibTableColumn
mplsOamBfdSessRemoteMisConnectivity=_MplsOamBfdSessRemoteMisConnectivity_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,23),_MplsOamBfdSessRemoteMisConnectivity_Type())
mplsOamBfdSessRemoteMisConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRemoteMisConnectivity.setStatus(_B)
_MplsOamBfdSessRemoteTimerExpired_Type=FaultStatus
_MplsOamBfdSessRemoteTimerExpired_Object=MibTableColumn
mplsOamBfdSessRemoteTimerExpired=_MplsOamBfdSessRemoteTimerExpired_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,24),_MplsOamBfdSessRemoteTimerExpired_Type())
mplsOamBfdSessRemoteTimerExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRemoteTimerExpired.setStatus(_B)
_MplsOamBfdSessRemoteAdminDown_Type=FaultStatus
_MplsOamBfdSessRemoteAdminDown_Object=MibTableColumn
mplsOamBfdSessRemoteAdminDown=_MplsOamBfdSessRemoteAdminDown_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,25),_MplsOamBfdSessRemoteAdminDown_Type())
mplsOamBfdSessRemoteAdminDown.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessRemoteAdminDown.setStatus(_B)
_MplsOamBfdSessRowStatus_Type=RowStatus
_MplsOamBfdSessRowStatus_Object=MibTableColumn
mplsOamBfdSessRowStatus=_MplsOamBfdSessRowStatus_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,26),_MplsOamBfdSessRowStatus_Type())
mplsOamBfdSessRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdSessRowStatus.setStatus(_B)
class _MplsOamBfdSessDesiredMinTxInterval_Type(BfdIntervalTC):defaultValue=100000
_MplsOamBfdSessDesiredMinTxInterval_Type.__name__=_F
_MplsOamBfdSessDesiredMinTxInterval_Object=MibTableColumn
mplsOamBfdSessDesiredMinTxInterval=_MplsOamBfdSessDesiredMinTxInterval_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,27),_MplsOamBfdSessDesiredMinTxInterval_Type())
mplsOamBfdSessDesiredMinTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessDesiredMinTxInterval.setStatus(_B)
class _MplsOamBfdSessReqMinRxInterval_Type(BfdIntervalTC):defaultValue=100000
_MplsOamBfdSessReqMinRxInterval_Type.__name__=_F
_MplsOamBfdSessReqMinRxInterval_Object=MibTableColumn
mplsOamBfdSessReqMinRxInterval=_MplsOamBfdSessReqMinRxInterval_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,28),_MplsOamBfdSessReqMinRxInterval_Type())
mplsOamBfdSessReqMinRxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdSessReqMinRxInterval.setStatus(_B)
class _MplsOamBfdSessTrafficClass_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_MplsOamBfdSessTrafficClass_Type.__name__=_E
_MplsOamBfdSessTrafficClass_Object=MibTableColumn
mplsOamBfdSessTrafficClass=_MplsOamBfdSessTrafficClass_Object((1,3,6,1,4,1,8708,2,44,2,2,1,1,29),_MplsOamBfdSessTrafficClass_Type())
mplsOamBfdSessTrafficClass.setMaxAccess(_l)
if mibBuilder.loadTexts:mplsOamBfdSessTrafficClass.setStatus(_B)
_MplsOamBfdTemplate_ObjectIdentity=ObjectIdentity
mplsOamBfdTemplate=_MplsOamBfdTemplate_ObjectIdentity((1,3,6,1,4,1,8708,2,44,2,3))
_MplsOamBfdTemplateTable_Object=MibTable
mplsOamBfdTemplateTable=_MplsOamBfdTemplateTable_Object((1,3,6,1,4,1,8708,2,44,2,3,2))
if mibBuilder.loadTexts:mplsOamBfdTemplateTable.setStatus(_B)
_MplsOamBfdTemplateEntry_Object=MibTableRow
mplsOamBfdTemplateEntry=_MplsOamBfdTemplateEntry_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1))
mplsOamBfdTemplateEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:mplsOamBfdTemplateEntry.setStatus(_B)
class _MplsOamBfdTemplateIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MplsOamBfdTemplateIndex_Type.__name__=_E
_MplsOamBfdTemplateIndex_Object=MibTableColumn
mplsOamBfdTemplateIndex=_MplsOamBfdTemplateIndex_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,1),_MplsOamBfdTemplateIndex_Type())
mplsOamBfdTemplateIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdTemplateIndex.setStatus(_B)
class _MplsOamBfdTemplateInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MplsOamBfdTemplateInternalReference_Type.__name__=_E
_MplsOamBfdTemplateInternalReference_Object=MibTableColumn
mplsOamBfdTemplateInternalReference=_MplsOamBfdTemplateInternalReference_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,2),_MplsOamBfdTemplateInternalReference_Type())
mplsOamBfdTemplateInternalReference.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateInternalReference.setStatus(_B)
_MplsOamBfdTemplateName_Type=MgmtNameString
_MplsOamBfdTemplateName_Object=MibTableColumn
mplsOamBfdTemplateName=_MplsOamBfdTemplateName_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,3),_MplsOamBfdTemplateName_Type())
mplsOamBfdTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdTemplateName.setStatus(_B)
class _MplsOamBfdTemplateIdentifier_Type(DisplayString):defaultValue=OctetString('')
_MplsOamBfdTemplateIdentifier_Type.__name__=_G
_MplsOamBfdTemplateIdentifier_Object=MibTableColumn
mplsOamBfdTemplateIdentifier=_MplsOamBfdTemplateIdentifier_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,4),_MplsOamBfdTemplateIdentifier_Type())
mplsOamBfdTemplateIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateIdentifier.setStatus(_B)
class _MplsOamBfdTemplateDesiredMinTxInterval_Type(BfdIntervalTC):defaultValue=100000
_MplsOamBfdTemplateDesiredMinTxInterval_Type.__name__=_F
_MplsOamBfdTemplateDesiredMinTxInterval_Object=MibTableColumn
mplsOamBfdTemplateDesiredMinTxInterval=_MplsOamBfdTemplateDesiredMinTxInterval_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,5),_MplsOamBfdTemplateDesiredMinTxInterval_Type())
mplsOamBfdTemplateDesiredMinTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateDesiredMinTxInterval.setStatus(_B)
class _MplsOamBfdTemplateDetectMult_Type(BfdMultiplierTC):defaultValue=3
_MplsOamBfdTemplateDetectMult_Type.__name__=_m
_MplsOamBfdTemplateDetectMult_Object=MibTableColumn
mplsOamBfdTemplateDetectMult=_MplsOamBfdTemplateDetectMult_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,6),_MplsOamBfdTemplateDetectMult_Type())
mplsOamBfdTemplateDetectMult.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateDetectMult.setStatus(_B)
class _MplsOamBfdTemplateReqMinRxInterval_Type(BfdIntervalTC):defaultValue=100000
_MplsOamBfdTemplateReqMinRxInterval_Type.__name__=_F
_MplsOamBfdTemplateReqMinRxInterval_Object=MibTableColumn
mplsOamBfdTemplateReqMinRxInterval=_MplsOamBfdTemplateReqMinRxInterval_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,7),_MplsOamBfdTemplateReqMinRxInterval_Type())
mplsOamBfdTemplateReqMinRxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateReqMinRxInterval.setStatus(_B)
_MplsOamBfdTemplateCreateNewTemplate_Type=CommandString
_MplsOamBfdTemplateCreateNewTemplate_Object=MibTableColumn
mplsOamBfdTemplateCreateNewTemplate=_MplsOamBfdTemplateCreateNewTemplate_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,8),_MplsOamBfdTemplateCreateNewTemplate_Type())
mplsOamBfdTemplateCreateNewTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsOamBfdTemplateCreateNewTemplate.setStatus(_B)
_MplsOamBfdTemplateRowStatus_Type=RowStatus
_MplsOamBfdTemplateRowStatus_Object=MibTableColumn
mplsOamBfdTemplateRowStatus=_MplsOamBfdTemplateRowStatus_Object((1,3,6,1,4,1,8708,2,44,2,3,2,1,9),_MplsOamBfdTemplateRowStatus_Type())
mplsOamBfdTemplateRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsOamBfdTemplateRowStatus.setStatus(_B)
mplsIOamGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,44,1,1,1))
mplsIOamGeneralGroupV1.setObjects(*((_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:mplsIOamGeneralGroupV1.setStatus(_B)
mplsBfdSessGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,44,1,1,2))
mplsBfdSessGroupV1.setObjects(*((_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:mplsBfdSessGroupV1.setStatus(_q)
mplsBfdTemplateGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,44,1,1,3))
mplsBfdTemplateGroupV1.setObjects(*((_A,_J),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:mplsBfdTemplateGroupV1.setStatus(_B)
mplsBfdSessGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,44,1,1,4))
mplsBfdSessGroupV2.setObjects(*((_A,_H),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:mplsBfdSessGroupV2.setStatus(_B)
lumMplsBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,44,1,2,1))
lumMplsBasicComplV1.setObjects(*((_A,_j),(_A,_A2),(_A,_k)))
if mibBuilder.loadTexts:lumMplsBasicComplV1.setStatus(_q)
lumMplsBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,44,1,2,2))
lumMplsBasicComplV2.setObjects(*((_A,_j),(_A,_A3),(_A,_k)))
if mibBuilder.loadTexts:lumMplsBasicComplV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'BfdSessStateTC':BfdSessStateTC,_m:BfdMultiplierTC,_F:BfdIntervalTC,'BfdDiagTC':BfdDiagTC,'lumMplsOamMIBModule':lumMplsOamMIBModule,'lumMplsOamConfs':lumMplsOamConfs,'lumMplsOamGroups':lumMplsOamGroups,_j:mplsIOamGeneralGroupV1,_A2:mplsBfdSessGroupV1,_k:mplsBfdTemplateGroupV1,_A3:mplsBfdSessGroupV2,'lumMplsOamCompl':lumMplsOamCompl,'lumMplsBasicComplV1':lumMplsBasicComplV1,'lumMplsBasicComplV2':lumMplsBasicComplV2,'lumMplsOamMIBObjects':lumMplsOamMIBObjects,'mplsOamGeneral':mplsOamGeneral,_n:mplsOamGeneralLastChangeTime,_o:mplsOamGeneralStateLastChangeTime,_p:mplsOamGeneralmplsOamBfdSessTableSize,'mplsOamGeneralmplsOamBfdTemplateTableSize':mplsOamGeneralmplsOamBfdTemplateTableSize,'mplsOamBfdSess':mplsOamBfdSess,'mplsOamBfdSessTable':mplsOamBfdSessTable,'mplsOamBfdSessEntry':mplsOamBfdSessEntry,_H:mplsOamBfdSessIndex,_K:mplsOamBfdSessInternalReference,_L:mplsOamBfdSessName,_M:mplsOamBfdSessAdminStatus,_N:mplsOamBfdSessState,_O:mplsOamBfdSessRemoteState,_P:mplsOamBfdSessDiag,_Q:mplsOamBfdSessRemoteDiag,_R:mplsOamBfdSessNegotiatedTxInterval,_S:mplsOamBfdSessNegotiatedRxInterval,_T:mplsOamBfdSessMonitoringPath,_U:mplsOamBfdSessMonitoringPathType,_V:mplsOamBfdSessMonitoringPathIndex,_W:mplsOamBfdSessTemplate,_X:mplsOamBfdSessTemplateIndex,_Y:mplsOamBfdSessSourceMepId,_Z:mplsOamBfdSessTargetMepId,_a:mplsOamBfdSessRcvTargetMepId,_b:mplsOamBfdSessMepNotConfigured,_c:mplsOamBfdSessLocalNotConnected,_d:mplsOamBfdSessLocalMisConnectivity,_e:mplsOamBfdSessLocalTimerExpired,_f:mplsOamBfdSessRemoteMisConnectivity,_g:mplsOamBfdSessRemoteTimerExpired,_h:mplsOamBfdSessRemoteAdminDown,_i:mplsOamBfdSessRowStatus,_z:mplsOamBfdSessDesiredMinTxInterval,_A0:mplsOamBfdSessReqMinRxInterval,_A1:mplsOamBfdSessTrafficClass,'mplsOamBfdTemplate':mplsOamBfdTemplate,'mplsOamBfdTemplateTable':mplsOamBfdTemplateTable,'mplsOamBfdTemplateEntry':mplsOamBfdTemplateEntry,_J:mplsOamBfdTemplateIndex,_r:mplsOamBfdTemplateInternalReference,_s:mplsOamBfdTemplateName,_t:mplsOamBfdTemplateIdentifier,_u:mplsOamBfdTemplateDesiredMinTxInterval,_v:mplsOamBfdTemplateDetectMult,_w:mplsOamBfdTemplateReqMinRxInterval,_x:mplsOamBfdTemplateCreateNewTemplate,_y:mplsOamBfdTemplateRowStatus})