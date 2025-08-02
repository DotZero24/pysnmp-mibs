_a='cwcConnStatsGroup'
_Z='cwcConnGenStatsGroup'
_Y='cesChanStatusBitMap'
_X='cesChanSignalingStatus'
_W='cesChanSecUptime'
_V='counterClrButton'
_U='cesCellSeqMismatchCnt'
_T='cesLostCells'
_S='cesHdrErrors'
_R='cesGenCells'
_Q='cesReassCells'
_P='cesCellLossStatus'
_O='cesRcvATMState'
_N='cesXmtATMState'
_M='cesChanState'
_L='normal'
_K='cesOflowDropBytes'
_J='cesUflowInsCells'
_I='cesIngrDiscardedBytes'
_H='cesBufOverflows'
_G='cesBufUnderflows'
_F='cesPointerReframes'
_E='cesCntChanNum'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-WAN-CES-CONN-STAT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cesmChan,=mibBuilder.importSymbols('BASIS-MIB','cesmChan')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanCesConnStatMIB=ModuleIdentity((1,3,6,1,4,1,351,150,43))
if mibBuilder.loadTexts:ciscoWanCesConnStatMIB.setRevisions(('2002-12-24 00:00',))
_CesmChanCntGrp_ObjectIdentity=ObjectIdentity
cesmChanCntGrp=_CesmChanCntGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,2,2))
_CesmChanCntGrpTable_Object=MibTable
cesmChanCntGrpTable=_CesmChanCntGrpTable_Object((1,3,6,1,4,1,351,110,5,3,2,2,1))
if mibBuilder.loadTexts:cesmChanCntGrpTable.setStatus(_B)
_CesmChanCntGrpEntry_Object=MibTableRow
cesmChanCntGrpEntry=_CesmChanCntGrpEntry_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1))
cesmChanCntGrpEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:cesmChanCntGrpEntry.setStatus(_B)
class _CesCntChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,2064))
_CesCntChanNum_Type.__name__=_D
_CesCntChanNum_Object=MibTableColumn
cesCntChanNum=_CesCntChanNum_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,1),_CesCntChanNum_Type())
cesCntChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cesCntChanNum.setStatus(_B)
class _CesChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notConfigured',1),('okay',2),('alarm',3),('failed',4)))
_CesChanState_Type.__name__=_D
_CesChanState_Object=MibTableColumn
cesChanState=_CesChanState_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,2),_CesChanState_Type())
cesChanState.setMaxAccess(_C)
if mibBuilder.loadTexts:cesChanState.setStatus(_B)
class _CesXmtATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_L,2),('sendingAIS',3),('sendingFERF',4)))
_CesXmtATMState_Type.__name__=_D
_CesXmtATMState_Object=MibTableColumn
cesXmtATMState=_CesXmtATMState_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,3),_CesXmtATMState_Type())
cesXmtATMState.setMaxAccess(_C)
if mibBuilder.loadTexts:cesXmtATMState.setStatus(_B)
class _CesRcvATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_L,2),('receivingAIS',3),('receivingFERF',4)))
_CesRcvATMState_Type.__name__=_D
_CesRcvATMState_Object=MibTableColumn
cesRcvATMState=_CesRcvATMState_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,4),_CesRcvATMState_Type())
cesRcvATMState.setMaxAccess(_C)
if mibBuilder.loadTexts:cesRcvATMState.setStatus(_B)
class _CesCellLossStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLoss',1),('loss',2)))
_CesCellLossStatus_Type.__name__=_D
_CesCellLossStatus_Object=MibTableColumn
cesCellLossStatus=_CesCellLossStatus_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,5),_CesCellLossStatus_Type())
cesCellLossStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cesCellLossStatus.setStatus(_B)
_CesReassCells_Type=Counter32
_CesReassCells_Object=MibTableColumn
cesReassCells=_CesReassCells_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,6),_CesReassCells_Type())
cesReassCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cesReassCells.setStatus(_B)
_CesGenCells_Type=Counter32
_CesGenCells_Object=MibTableColumn
cesGenCells=_CesGenCells_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,7),_CesGenCells_Type())
cesGenCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cesGenCells.setStatus(_B)
_CesHdrErrors_Type=Counter32
_CesHdrErrors_Object=MibTableColumn
cesHdrErrors=_CesHdrErrors_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,8),_CesHdrErrors_Type())
cesHdrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cesHdrErrors.setStatus(_B)
_CesPointerReframes_Type=Counter32
_CesPointerReframes_Object=MibTableColumn
cesPointerReframes=_CesPointerReframes_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,9),_CesPointerReframes_Type())
cesPointerReframes.setMaxAccess(_C)
if mibBuilder.loadTexts:cesPointerReframes.setStatus(_B)
_CesLostCells_Type=Counter32
_CesLostCells_Object=MibTableColumn
cesLostCells=_CesLostCells_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,10),_CesLostCells_Type())
cesLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cesLostCells.setStatus(_B)
_CesBufUnderflows_Type=Counter32
_CesBufUnderflows_Object=MibTableColumn
cesBufUnderflows=_CesBufUnderflows_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,11),_CesBufUnderflows_Type())
cesBufUnderflows.setMaxAccess(_C)
if mibBuilder.loadTexts:cesBufUnderflows.setStatus(_B)
_CesBufOverflows_Type=Counter32
_CesBufOverflows_Object=MibTableColumn
cesBufOverflows=_CesBufOverflows_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,12),_CesBufOverflows_Type())
cesBufOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:cesBufOverflows.setStatus(_B)
_CesIngrDiscardedBytes_Type=Counter32
_CesIngrDiscardedBytes_Object=MibTableColumn
cesIngrDiscardedBytes=_CesIngrDiscardedBytes_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,13),_CesIngrDiscardedBytes_Type())
cesIngrDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cesIngrDiscardedBytes.setStatus(_B)
_CesUflowInsCells_Type=Counter32
_CesUflowInsCells_Object=MibTableColumn
cesUflowInsCells=_CesUflowInsCells_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,14),_CesUflowInsCells_Type())
cesUflowInsCells.setMaxAccess(_C)
if mibBuilder.loadTexts:cesUflowInsCells.setStatus(_B)
_CesOflowDropBytes_Type=Counter32
_CesOflowDropBytes_Object=MibTableColumn
cesOflowDropBytes=_CesOflowDropBytes_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,15),_CesOflowDropBytes_Type())
cesOflowDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cesOflowDropBytes.setStatus(_B)
_CesCellSeqMismatchCnt_Type=Counter32
_CesCellSeqMismatchCnt_Object=MibTableColumn
cesCellSeqMismatchCnt=_CesCellSeqMismatchCnt_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,16),_CesCellSeqMismatchCnt_Type())
cesCellSeqMismatchCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cesCellSeqMismatchCnt.setStatus(_B)
class _CounterClrButton_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('resetCounters',2)))
_CounterClrButton_Type.__name__=_D
_CounterClrButton_Object=MibTableColumn
counterClrButton=_CounterClrButton_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,17),_CounterClrButton_Type())
counterClrButton.setMaxAccess('read-write')
if mibBuilder.loadTexts:counterClrButton.setStatus(_B)
_CesChanSecUptime_Type=Counter32
_CesChanSecUptime_Object=MibTableColumn
cesChanSecUptime=_CesChanSecUptime_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,18),_CesChanSecUptime_Type())
cesChanSecUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:cesChanSecUptime.setStatus(_B)
class _CesChanSignalingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off-hook',1),('on-hook',2)))
_CesChanSignalingStatus_Type.__name__=_D
_CesChanSignalingStatus_Object=MibTableColumn
cesChanSignalingStatus=_CesChanSignalingStatus_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,19),_CesChanSignalingStatus_Type())
cesChanSignalingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cesChanSignalingStatus.setStatus(_B)
class _CesChanStatusBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CesChanStatusBitMap_Type.__name__=_D
_CesChanStatusBitMap_Object=MibTableColumn
cesChanStatusBitMap=_CesChanStatusBitMap_Object((1,3,6,1,4,1,351,110,5,3,2,2,1,1,20),_CesChanStatusBitMap_Type())
cesChanStatusBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:cesChanStatusBitMap.setStatus(_B)
_CwcConnStatMIBConformance_ObjectIdentity=ObjectIdentity
cwcConnStatMIBConformance=_CwcConnStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,43,2))
_CwcConnStatMIBGroups_ObjectIdentity=ObjectIdentity
cwcConnStatMIBGroups=_CwcConnStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,43,2,1))
_CwcConnStatMIBCompliances_ObjectIdentity=ObjectIdentity
cwcConnStatMIBCompliances=_CwcConnStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,43,2,2))
cwcConnGenStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,43,2,1,1))
cwcConnGenStatsGroup.setObjects(*((_A,_E),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_F),(_A,_T),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cwcConnGenStatsGroup.setStatus(_B)
cwcConnStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,43,2,1,2))
cwcConnStatsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cwcConnStatsGroup.setStatus(_B)
cwcConnStatCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,43,2,2,1))
cwcConnStatCompliance.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cwcConnStatCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cesmChanCntGrp':cesmChanCntGrp,'cesmChanCntGrpTable':cesmChanCntGrpTable,'cesmChanCntGrpEntry':cesmChanCntGrpEntry,_E:cesCntChanNum,_M:cesChanState,_N:cesXmtATMState,_O:cesRcvATMState,_P:cesCellLossStatus,_Q:cesReassCells,_R:cesGenCells,_S:cesHdrErrors,_F:cesPointerReframes,_T:cesLostCells,_G:cesBufUnderflows,_H:cesBufOverflows,_I:cesIngrDiscardedBytes,_J:cesUflowInsCells,_K:cesOflowDropBytes,_U:cesCellSeqMismatchCnt,_V:counterClrButton,_W:cesChanSecUptime,_X:cesChanSignalingStatus,_Y:cesChanStatusBitMap,'ciscoWanCesConnStatMIB':ciscoWanCesConnStatMIB,'cwcConnStatMIBConformance':cwcConnStatMIBConformance,'cwcConnStatMIBGroups':cwcConnStatMIBGroups,_Z:cwcConnGenStatsGroup,_a:cwcConnStatsGroup,'cwcConnStatMIBCompliances':cwcConnStatMIBCompliances,'cwcConnStatCompliance':cwcConnStatCompliance})