_AB='ciscoImaVerFallbackSupportGroup'
_AA='ciscoImaAutoRestartGroup'
_A9='ciscoImaFeatureGroup'
_A8='ciscoImaLinkMappingGroup'
_A7='cimaGrpVerFallbackEnable'
_A6='cimaGrpAutoRestartSyncState'
_A5='cimaGrpRxImaIdExpected'
_A4='cimaGrpAutoRestartMode'
_A3='cimaAutoRestartEnable'
_A2='cimaVerFallbackEnable'
_A1='cimaMaxGrpTxImaId'
_A0='cimaMinGrpTxImaId'
_z='cimaConfiguredImaGroups'
_y='cimaMaxImaGroupsSupported'
_x='cimaLinkAlarmType'
_w='cimaGrpAlarmType'
_v='cimaLinkState'
_u='cimaLinkNumTxMissingIcpCells'
_t='cimaLinkNumRxMissingIcpCells'
_s='cimaLinkNumRxInvalidIcpCells'
_r='cimaLinkNumRxErrIcpCells'
_q='cimaLinkNumRxIcpCells'
_p='cimaLinkNumTxIcpCells'
_o='cimaLinkLodsIntDownTime'
_n='cimaLinkLifIntDownTime'
_m='cimaLinkLodsIntUpTime'
_l='cimaLinkLifIntUpTime'
_k='cimaGrpMaxCellRate'
_j='cimaGrpNeVersion'
_i='cimaGrpRestarting'
_h='cimaGrpNumTxMissingIcpCells'
_g='cimaGrpNumRxMissingIcpCells'
_f='cimaGrpNumRxInvalidIcpCells'
_e='cimaGrpNumRxErrIcpCells'
_d='cimaGrpNumRxIcpCells'
_c='cimaGrpNumTxIcpCells'
_b='cimaGrpIntegrationDownTime'
_a='cimaGrpIntegrationUpTime'
_Z='cimaStuffAndCellIndication'
_Y='cimaGroupClearAccDelay'
_X='cimaGroupAccumulatedDelay'
_W='cimaLinkEntry'
_V='cimaGroupEntry'
_U='disable'
_T='Gauge32'
_S='imaLinkIfIndex'
_R='imaGroupIndex'
_Q='entPhysicalIndex'
_P='ENTITY-MIB'
_O='ciscoImaLinkGroup'
_N='ciscoImaGroupGroup'
_M='IMA-MIB'
_L='read-write'
_K='deprecated'
_J='Unsigned32'
_I='TruthValue'
_H='Integer32'
_G='millisecond'
_F='MilliSeconds'
_E='cells'
_D='read-create'
_C='read-only'
_B='CISCO-IMA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_P,_Q)
MilliSeconds,imaGroupEntry,imaGroupIndex,imaLinkEntry,imaLinkIfIndex=mibBuilder.importSymbols(_M,_F,'imaGroupEntry',_R,'imaLinkEntry',_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_T,_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
ciscoImaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,235))
if mibBuilder.loadTexts:ciscoImaMIB.setRevisions(('2003-03-26 00:00','2002-05-02 00:00'))
class CiscoImaGrpAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cimaAlarmGroupStartupFe',1),('cimaAlarmGroupCfgAbort',2),('cimaAlarmGroupCfgAbortFe',3),('cimaAlarmGroupInsuffLinks',4),('cimaAlarmGroupInsuffLinksFe',5),('cimaAlarmGroupBlockedFe',6),('cimaAlarmGroupTimingSynch',7)))
class CiscoImaLinkAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('cimaAlarmLinkLif',1),('cimaAlarmLinkLods',2),('cimaAlarmLinkRfi',3),('cimaAlarmLinkTxMisConnect',4),('cimaAlarmLinkRxMisConnect',5),('cimaAlarmLinkTxFault',6),('cimaAlarmLinkRxFault',7),('cimaAlarmLinkTxUnusableFe',8),('cimaAlarmLinkRxUnusableFe',9)))
_CiscoImaMIBObjects_ObjectIdentity=ObjectIdentity
ciscoImaMIBObjects=_CiscoImaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,235,1))
_CimaGrpAlarmType_Type=CiscoImaGrpAlarmType
_CimaGrpAlarmType_Object=MibScalar
cimaGrpAlarmType=_CimaGrpAlarmType_Object((1,3,6,1,4,1,9,9,235,1,1),_CimaGrpAlarmType_Type())
cimaGrpAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpAlarmType.setStatus(_K)
_CimaLinkAlarmType_Type=CiscoImaLinkAlarmType
_CimaLinkAlarmType_Object=MibScalar
cimaLinkAlarmType=_CimaLinkAlarmType_Object((1,3,6,1,4,1,9,9,235,1,2),_CimaLinkAlarmType_Type())
cimaLinkAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkAlarmType.setStatus(_K)
_CimaGroupTable_Object=MibTable
cimaGroupTable=_CimaGroupTable_Object((1,3,6,1,4,1,9,9,235,1,3))
if mibBuilder.loadTexts:cimaGroupTable.setStatus(_A)
_CimaGroupEntry_Object=MibTableRow
cimaGroupEntry=_CimaGroupEntry_Object((1,3,6,1,4,1,9,9,235,1,3,1))
if mibBuilder.loadTexts:cimaGroupEntry.setStatus(_A)
_CimaGroupAccumulatedDelay_Type=MilliSeconds
_CimaGroupAccumulatedDelay_Object=MibTableColumn
cimaGroupAccumulatedDelay=_CimaGroupAccumulatedDelay_Object((1,3,6,1,4,1,9,9,235,1,3,1,1),_CimaGroupAccumulatedDelay_Type())
cimaGroupAccumulatedDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGroupAccumulatedDelay.setStatus(_A)
if mibBuilder.loadTexts:cimaGroupAccumulatedDelay.setUnits(_G)
class _CimaGroupClearAccDelay_Type(TruthValue):defaultValue=2
_CimaGroupClearAccDelay_Type.__name__=_I
_CimaGroupClearAccDelay_Object=MibTableColumn
cimaGroupClearAccDelay=_CimaGroupClearAccDelay_Object((1,3,6,1,4,1,9,9,235,1,3,1,2),_CimaGroupClearAccDelay_Type())
cimaGroupClearAccDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGroupClearAccDelay.setStatus(_A)
class _CimaStuffAndCellIndication_Type(Bits):namedValues=NamedValues(*(('lsibit0',0),('lsibit1',1),('lsibit2',2)))
_CimaStuffAndCellIndication_Type.__name__='Bits'
_CimaStuffAndCellIndication_Object=MibTableColumn
cimaStuffAndCellIndication=_CimaStuffAndCellIndication_Object((1,3,6,1,4,1,9,9,235,1,3,1,3),_CimaStuffAndCellIndication_Type())
cimaStuffAndCellIndication.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaStuffAndCellIndication.setStatus(_A)
class _CimaGrpIntegrationUpTime_Type(MilliSeconds):defaultValue=10000;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400000))
_CimaGrpIntegrationUpTime_Type.__name__=_F
_CimaGrpIntegrationUpTime_Object=MibTableColumn
cimaGrpIntegrationUpTime=_CimaGrpIntegrationUpTime_Object((1,3,6,1,4,1,9,9,235,1,3,1,4),_CimaGrpIntegrationUpTime_Type())
cimaGrpIntegrationUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpIntegrationUpTime.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpIntegrationUpTime.setUnits(_G)
class _CimaGrpIntegrationDownTime_Type(MilliSeconds):defaultValue=2500;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CimaGrpIntegrationDownTime_Type.__name__=_F
_CimaGrpIntegrationDownTime_Object=MibTableColumn
cimaGrpIntegrationDownTime=_CimaGrpIntegrationDownTime_Object((1,3,6,1,4,1,9,9,235,1,3,1,5),_CimaGrpIntegrationDownTime_Type())
cimaGrpIntegrationDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpIntegrationDownTime.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpIntegrationDownTime.setUnits(_G)
_CimaGrpNumTxIcpCells_Type=Counter32
_CimaGrpNumTxIcpCells_Object=MibTableColumn
cimaGrpNumTxIcpCells=_CimaGrpNumTxIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,6),_CimaGrpNumTxIcpCells_Type())
cimaGrpNumTxIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumTxIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumTxIcpCells.setUnits(_E)
_CimaGrpNumRxIcpCells_Type=Counter32
_CimaGrpNumRxIcpCells_Object=MibTableColumn
cimaGrpNumRxIcpCells=_CimaGrpNumRxIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,7),_CimaGrpNumRxIcpCells_Type())
cimaGrpNumRxIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumRxIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumRxIcpCells.setUnits(_E)
_CimaGrpNumRxErrIcpCells_Type=Counter32
_CimaGrpNumRxErrIcpCells_Object=MibTableColumn
cimaGrpNumRxErrIcpCells=_CimaGrpNumRxErrIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,8),_CimaGrpNumRxErrIcpCells_Type())
cimaGrpNumRxErrIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumRxErrIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumRxErrIcpCells.setUnits(_E)
_CimaGrpNumRxInvalidIcpCells_Type=Counter32
_CimaGrpNumRxInvalidIcpCells_Object=MibTableColumn
cimaGrpNumRxInvalidIcpCells=_CimaGrpNumRxInvalidIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,9),_CimaGrpNumRxInvalidIcpCells_Type())
cimaGrpNumRxInvalidIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumRxInvalidIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumRxInvalidIcpCells.setUnits(_E)
_CimaGrpNumRxMissingIcpCells_Type=Counter32
_CimaGrpNumRxMissingIcpCells_Object=MibTableColumn
cimaGrpNumRxMissingIcpCells=_CimaGrpNumRxMissingIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,10),_CimaGrpNumRxMissingIcpCells_Type())
cimaGrpNumRxMissingIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumRxMissingIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumRxMissingIcpCells.setUnits(_E)
_CimaGrpNumTxMissingIcpCells_Type=Counter32
_CimaGrpNumTxMissingIcpCells_Object=MibTableColumn
cimaGrpNumTxMissingIcpCells=_CimaGrpNumTxMissingIcpCells_Object((1,3,6,1,4,1,9,9,235,1,3,1,11),_CimaGrpNumTxMissingIcpCells_Type())
cimaGrpNumTxMissingIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpNumTxMissingIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpNumTxMissingIcpCells.setUnits(_E)
class _CimaGrpRestarting_Type(TruthValue):defaultValue=2
_CimaGrpRestarting_Type.__name__=_I
_CimaGrpRestarting_Object=MibTableColumn
cimaGrpRestarting=_CimaGrpRestarting_Object((1,3,6,1,4,1,9,9,235,1,3,1,12),_CimaGrpRestarting_Type())
cimaGrpRestarting.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpRestarting.setStatus(_A)
class _CimaGrpNeVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('others',1),('version10',2),('version11',3)))
_CimaGrpNeVersion_Type.__name__=_H
_CimaGrpNeVersion_Object=MibTableColumn
cimaGrpNeVersion=_CimaGrpNeVersion_Object((1,3,6,1,4,1,9,9,235,1,3,1,13),_CimaGrpNeVersion_Type())
cimaGrpNeVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpNeVersion.setStatus(_A)
_CimaGrpMaxCellRate_Type=Gauge32
_CimaGrpMaxCellRate_Object=MibTableColumn
cimaGrpMaxCellRate=_CimaGrpMaxCellRate_Object((1,3,6,1,4,1,9,9,235,1,3,1,14),_CimaGrpMaxCellRate_Type())
cimaGrpMaxCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpMaxCellRate.setStatus(_A)
if mibBuilder.loadTexts:cimaGrpMaxCellRate.setUnits('cells per second')
class _CimaGrpVerFallbackEnable_Type(TruthValue):defaultValue=1
_CimaGrpVerFallbackEnable_Type.__name__=_I
_CimaGrpVerFallbackEnable_Object=MibTableColumn
cimaGrpVerFallbackEnable=_CimaGrpVerFallbackEnable_Object((1,3,6,1,4,1,9,9,235,1,3,1,15),_CimaGrpVerFallbackEnable_Type())
cimaGrpVerFallbackEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpVerFallbackEnable.setStatus(_A)
class _CimaGrpAutoRestartMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('relearn',2),('reuse',3)))
_CimaGrpAutoRestartMode_Type.__name__=_H
_CimaGrpAutoRestartMode_Object=MibTableColumn
cimaGrpAutoRestartMode=_CimaGrpAutoRestartMode_Object((1,3,6,1,4,1,9,9,235,1,3,1,16),_CimaGrpAutoRestartMode_Type())
cimaGrpAutoRestartMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpAutoRestartMode.setStatus(_A)
class _CimaGrpRxImaIdExpected_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_CimaGrpRxImaIdExpected_Type.__name__=_H
_CimaGrpRxImaIdExpected_Object=MibTableColumn
cimaGrpRxImaIdExpected=_CimaGrpRxImaIdExpected_Object((1,3,6,1,4,1,9,9,235,1,3,1,17),_CimaGrpRxImaIdExpected_Type())
cimaGrpRxImaIdExpected.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaGrpRxImaIdExpected.setStatus(_A)
class _CimaGrpAutoRestartSyncState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),('inProgress',2),('loopbackSync',3),('tempSync',4),('feSync',5)))
_CimaGrpAutoRestartSyncState_Type.__name__=_H
_CimaGrpAutoRestartSyncState_Object=MibTableColumn
cimaGrpAutoRestartSyncState=_CimaGrpAutoRestartSyncState_Object((1,3,6,1,4,1,9,9,235,1,3,1,18),_CimaGrpAutoRestartSyncState_Type())
cimaGrpAutoRestartSyncState.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaGrpAutoRestartSyncState.setStatus(_A)
_CimaLinkMappingTable_Object=MibTable
cimaLinkMappingTable=_CimaLinkMappingTable_Object((1,3,6,1,4,1,9,9,235,1,4))
if mibBuilder.loadTexts:cimaLinkMappingTable.setStatus(_A)
_CimaLinkMappingEntry_Object=MibTableRow
cimaLinkMappingEntry=_CimaLinkMappingEntry_Object((1,3,6,1,4,1,9,9,235,1,4,1))
cimaLinkMappingEntry.setIndexNames((0,_M,_R),(0,_M,_S))
if mibBuilder.loadTexts:cimaLinkMappingEntry.setStatus(_A)
class _CimaLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('nonactive',2)))
_CimaLinkState_Type.__name__=_H
_CimaLinkState_Object=MibTableColumn
cimaLinkState=_CimaLinkState_Object((1,3,6,1,4,1,9,9,235,1,4,1,1),_CimaLinkState_Type())
cimaLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkState.setStatus(_A)
_CimaLinkTable_Object=MibTable
cimaLinkTable=_CimaLinkTable_Object((1,3,6,1,4,1,9,9,235,1,5))
if mibBuilder.loadTexts:cimaLinkTable.setStatus(_A)
_CimaLinkEntry_Object=MibTableRow
cimaLinkEntry=_CimaLinkEntry_Object((1,3,6,1,4,1,9,9,235,1,5,1))
if mibBuilder.loadTexts:cimaLinkEntry.setStatus(_A)
class _CimaLinkLifIntUpTime_Type(MilliSeconds):defaultValue=2500;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000))
_CimaLinkLifIntUpTime_Type.__name__=_F
_CimaLinkLifIntUpTime_Object=MibTableColumn
cimaLinkLifIntUpTime=_CimaLinkLifIntUpTime_Object((1,3,6,1,4,1,9,9,235,1,5,1,1),_CimaLinkLifIntUpTime_Type())
cimaLinkLifIntUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaLinkLifIntUpTime.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkLifIntUpTime.setUnits(_G)
class _CimaLinkLifIntDownTime_Type(MilliSeconds):defaultValue=10000;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000))
_CimaLinkLifIntDownTime_Type.__name__=_F
_CimaLinkLifIntDownTime_Object=MibTableColumn
cimaLinkLifIntDownTime=_CimaLinkLifIntDownTime_Object((1,3,6,1,4,1,9,9,235,1,5,1,2),_CimaLinkLifIntDownTime_Type())
cimaLinkLifIntDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaLinkLifIntDownTime.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkLifIntDownTime.setUnits(_G)
class _CimaLinkLodsIntUpTime_Type(MilliSeconds):defaultValue=2500;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000))
_CimaLinkLodsIntUpTime_Type.__name__=_F
_CimaLinkLodsIntUpTime_Object=MibTableColumn
cimaLinkLodsIntUpTime=_CimaLinkLodsIntUpTime_Object((1,3,6,1,4,1,9,9,235,1,5,1,3),_CimaLinkLodsIntUpTime_Type())
cimaLinkLodsIntUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaLinkLodsIntUpTime.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkLodsIntUpTime.setUnits(_G)
class _CimaLinkLodsIntDownTime_Type(MilliSeconds):defaultValue=10000;subtypeSpec=MilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000))
_CimaLinkLodsIntDownTime_Type.__name__=_F
_CimaLinkLodsIntDownTime_Object=MibTableColumn
cimaLinkLodsIntDownTime=_CimaLinkLodsIntDownTime_Object((1,3,6,1,4,1,9,9,235,1,5,1,4),_CimaLinkLodsIntDownTime_Type())
cimaLinkLodsIntDownTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cimaLinkLodsIntDownTime.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkLodsIntDownTime.setUnits(_G)
_CimaLinkNumTxIcpCells_Type=Counter32
_CimaLinkNumTxIcpCells_Object=MibTableColumn
cimaLinkNumTxIcpCells=_CimaLinkNumTxIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,5),_CimaLinkNumTxIcpCells_Type())
cimaLinkNumTxIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumTxIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumTxIcpCells.setUnits(_E)
_CimaLinkNumRxIcpCells_Type=Counter32
_CimaLinkNumRxIcpCells_Object=MibTableColumn
cimaLinkNumRxIcpCells=_CimaLinkNumRxIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,6),_CimaLinkNumRxIcpCells_Type())
cimaLinkNumRxIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumRxIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumRxIcpCells.setUnits(_E)
_CimaLinkNumRxErrIcpCells_Type=Counter32
_CimaLinkNumRxErrIcpCells_Object=MibTableColumn
cimaLinkNumRxErrIcpCells=_CimaLinkNumRxErrIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,7),_CimaLinkNumRxErrIcpCells_Type())
cimaLinkNumRxErrIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumRxErrIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumRxErrIcpCells.setUnits(_E)
_CimaLinkNumRxInvalidIcpCells_Type=Counter32
_CimaLinkNumRxInvalidIcpCells_Object=MibTableColumn
cimaLinkNumRxInvalidIcpCells=_CimaLinkNumRxInvalidIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,8),_CimaLinkNumRxInvalidIcpCells_Type())
cimaLinkNumRxInvalidIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumRxInvalidIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumRxInvalidIcpCells.setUnits(_E)
_CimaLinkNumRxMissingIcpCells_Type=Counter32
_CimaLinkNumRxMissingIcpCells_Object=MibTableColumn
cimaLinkNumRxMissingIcpCells=_CimaLinkNumRxMissingIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,9),_CimaLinkNumRxMissingIcpCells_Type())
cimaLinkNumRxMissingIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumRxMissingIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumRxMissingIcpCells.setUnits(_E)
_CimaLinkNumTxMissingIcpCells_Type=Counter32
_CimaLinkNumTxMissingIcpCells_Object=MibTableColumn
cimaLinkNumTxMissingIcpCells=_CimaLinkNumTxMissingIcpCells_Object((1,3,6,1,4,1,9,9,235,1,5,1,10),_CimaLinkNumTxMissingIcpCells_Type())
cimaLinkNumTxMissingIcpCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaLinkNumTxMissingIcpCells.setStatus(_A)
if mibBuilder.loadTexts:cimaLinkNumTxMissingIcpCells.setUnits(_E)
_CimaFeatureTable_Object=MibTable
cimaFeatureTable=_CimaFeatureTable_Object((1,3,6,1,4,1,9,9,235,1,6))
if mibBuilder.loadTexts:cimaFeatureTable.setStatus(_A)
_CimaFeatureEntry_Object=MibTableRow
cimaFeatureEntry=_CimaFeatureEntry_Object((1,3,6,1,4,1,9,9,235,1,6,1))
cimaFeatureEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:cimaFeatureEntry.setStatus(_A)
class _CimaMaxImaGroupsSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CimaMaxImaGroupsSupported_Type.__name__=_J
_CimaMaxImaGroupsSupported_Object=MibTableColumn
cimaMaxImaGroupsSupported=_CimaMaxImaGroupsSupported_Object((1,3,6,1,4,1,9,9,235,1,6,1,1),_CimaMaxImaGroupsSupported_Type())
cimaMaxImaGroupsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaMaxImaGroupsSupported.setStatus(_A)
class _CimaConfiguredImaGroups_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CimaConfiguredImaGroups_Type.__name__=_T
_CimaConfiguredImaGroups_Object=MibTableColumn
cimaConfiguredImaGroups=_CimaConfiguredImaGroups_Object((1,3,6,1,4,1,9,9,235,1,6,1,2),_CimaConfiguredImaGroups_Type())
cimaConfiguredImaGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:cimaConfiguredImaGroups.setStatus(_A)
class _CimaMinGrpTxImaId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CimaMinGrpTxImaId_Type.__name__=_J
_CimaMinGrpTxImaId_Object=MibTableColumn
cimaMinGrpTxImaId=_CimaMinGrpTxImaId_Object((1,3,6,1,4,1,9,9,235,1,6,1,3),_CimaMinGrpTxImaId_Type())
cimaMinGrpTxImaId.setMaxAccess(_L)
if mibBuilder.loadTexts:cimaMinGrpTxImaId.setStatus(_A)
class _CimaMaxGrpTxImaId_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CimaMaxGrpTxImaId_Type.__name__=_J
_CimaMaxGrpTxImaId_Object=MibTableColumn
cimaMaxGrpTxImaId=_CimaMaxGrpTxImaId_Object((1,3,6,1,4,1,9,9,235,1,6,1,4),_CimaMaxGrpTxImaId_Type())
cimaMaxGrpTxImaId.setMaxAccess(_L)
if mibBuilder.loadTexts:cimaMaxGrpTxImaId.setStatus(_A)
class _CimaVerFallbackEnable_Type(TruthValue):defaultValue=1
_CimaVerFallbackEnable_Type.__name__=_I
_CimaVerFallbackEnable_Object=MibTableColumn
cimaVerFallbackEnable=_CimaVerFallbackEnable_Object((1,3,6,1,4,1,9,9,235,1,6,1,5),_CimaVerFallbackEnable_Type())
cimaVerFallbackEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:cimaVerFallbackEnable.setStatus(_A)
class _CimaAutoRestartEnable_Type(TruthValue):defaultValue=2
_CimaAutoRestartEnable_Type.__name__=_I
_CimaAutoRestartEnable_Object=MibTableColumn
cimaAutoRestartEnable=_CimaAutoRestartEnable_Object((1,3,6,1,4,1,9,9,235,1,6,1,6),_CimaAutoRestartEnable_Type())
cimaAutoRestartEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:cimaAutoRestartEnable.setStatus(_A)
_CiscoImaMIBConformance_ObjectIdentity=ObjectIdentity
ciscoImaMIBConformance=_CiscoImaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,235,2))
_CiscoImaMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoImaMIBCompliances=_CiscoImaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,235,2,1))
_CiscoImaMIBGroups_ObjectIdentity=ObjectIdentity
ciscoImaMIBGroups=_CiscoImaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,235,2,2))
imaGroupEntry.registerAugmentions((_B,_V))
cimaGroupEntry.setIndexNames(*imaGroupEntry.getIndexNames())
imaLinkEntry.registerAugmentions((_B,_W))
cimaLinkEntry.setIndexNames(*imaLinkEntry.getIndexNames())
ciscoImaGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,1))
ciscoImaGroupGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ciscoImaGroupGroup.setStatus(_A)
ciscoImaLinkGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,2))
ciscoImaLinkGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoImaLinkGroup.setStatus(_A)
ciscoImaLinkMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,3))
ciscoImaLinkMappingGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:ciscoImaLinkMappingGroup.setStatus(_A)
ciscoImaAlarmGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,4))
ciscoImaAlarmGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoImaAlarmGroup.setStatus(_K)
ciscoImaFeatureGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,5))
ciscoImaFeatureGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoImaFeatureGroup.setStatus(_A)
ciscoImaAutoRestartGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,6))
ciscoImaAutoRestartGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoImaAutoRestartGroup.setStatus(_A)
ciscoImaVerFallbackSupportGroup=ObjectGroup((1,3,6,1,4,1,9,9,235,2,2,7))
ciscoImaVerFallbackSupportGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:ciscoImaVerFallbackSupportGroup.setStatus(_A)
ciscoImaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,235,2,1,1))
ciscoImaMIBCompliance.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ciscoImaMIBCompliance.setStatus(_K)
ciscoImaMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,235,2,1,2))
ciscoImaMIBCompliance1.setObjects(*((_B,_N),(_B,_O),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoImaMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoImaGrpAlarmType':CiscoImaGrpAlarmType,'CiscoImaLinkAlarmType':CiscoImaLinkAlarmType,'ciscoImaMIB':ciscoImaMIB,'ciscoImaMIBObjects':ciscoImaMIBObjects,_w:cimaGrpAlarmType,_x:cimaLinkAlarmType,'cimaGroupTable':cimaGroupTable,_V:cimaGroupEntry,_X:cimaGroupAccumulatedDelay,_Y:cimaGroupClearAccDelay,_Z:cimaStuffAndCellIndication,_a:cimaGrpIntegrationUpTime,_b:cimaGrpIntegrationDownTime,_c:cimaGrpNumTxIcpCells,_d:cimaGrpNumRxIcpCells,_e:cimaGrpNumRxErrIcpCells,_f:cimaGrpNumRxInvalidIcpCells,_g:cimaGrpNumRxMissingIcpCells,_h:cimaGrpNumTxMissingIcpCells,_i:cimaGrpRestarting,_j:cimaGrpNeVersion,_k:cimaGrpMaxCellRate,_A7:cimaGrpVerFallbackEnable,_A4:cimaGrpAutoRestartMode,_A5:cimaGrpRxImaIdExpected,_A6:cimaGrpAutoRestartSyncState,'cimaLinkMappingTable':cimaLinkMappingTable,'cimaLinkMappingEntry':cimaLinkMappingEntry,_v:cimaLinkState,'cimaLinkTable':cimaLinkTable,_W:cimaLinkEntry,_l:cimaLinkLifIntUpTime,_n:cimaLinkLifIntDownTime,_m:cimaLinkLodsIntUpTime,_o:cimaLinkLodsIntDownTime,_p:cimaLinkNumTxIcpCells,_q:cimaLinkNumRxIcpCells,_r:cimaLinkNumRxErrIcpCells,_s:cimaLinkNumRxInvalidIcpCells,_t:cimaLinkNumRxMissingIcpCells,_u:cimaLinkNumTxMissingIcpCells,'cimaFeatureTable':cimaFeatureTable,'cimaFeatureEntry':cimaFeatureEntry,_y:cimaMaxImaGroupsSupported,_z:cimaConfiguredImaGroups,_A0:cimaMinGrpTxImaId,_A1:cimaMaxGrpTxImaId,_A2:cimaVerFallbackEnable,_A3:cimaAutoRestartEnable,'ciscoImaMIBConformance':ciscoImaMIBConformance,'ciscoImaMIBCompliances':ciscoImaMIBCompliances,'ciscoImaMIBCompliance':ciscoImaMIBCompliance,'ciscoImaMIBCompliance1':ciscoImaMIBCompliance1,'ciscoImaMIBGroups':ciscoImaMIBGroups,_N:ciscoImaGroupGroup,_O:ciscoImaLinkGroup,_A8:ciscoImaLinkMappingGroup,'ciscoImaAlarmGroup':ciscoImaAlarmGroup,_A9:ciscoImaFeatureGroup,_AA:ciscoImaAutoRestartGroup,_AB:ciscoImaVerFallbackSupportGroup})