_A0='ciscoVismLapdDlcTable'
_z='ciscoVismLapdStatsGroup'
_y='ciscoVismLapdGroup'
_x='vismLapdTrunkGroup'
_w='vismLapdDlcLinkState'
_v='vismLapdRxInvalidFrames'
_u='vismLapdTxRejectFrames'
_t='vismLapdRxRejectFrames'
_s='vismLapdTxUnumInfoFrames'
_r='vismLapdRxUnumInfoFrames'
_q='vismLapdTxExchIdFrames'
_p='vismLapdRxExchIdFrames'
_o='vismLapdTxFrmRejectFrames'
_n='vismLapdRxFrmRejectFrames'
_m='vismLapdTxDiscModeFrames'
_l='vismLapdRxDiscModeFrames'
_k='vismLapdTxUAFrames'
_j='vismLapdRxUAFrames'
_i='vismLapdTxDisconFrames'
_h='vismLapdRxDisconFrames'
_g='vismLapdTxSABMFrames'
_f='vismLapdRxSABMFrames'
_e='vismLapdTxNotReadyFrames'
_d='vismLapdRxNotReadyFrames'
_c='vismLapdTxReadyFrames'
_b='vismLapdRxReadyFrames'
_a='vismLapdTxInfoFrames'
_Z='vismLapdRxInfoFrames'
_Y='vismLapdTrunkType'
_X='vismLapdSide'
_W='vismLapdRowStatus'
_V='vismLapdType'
_U='vismLapdT203'
_T='vismLapdT200'
_S='vismLapdN200'
_R='vismLapdWinSize'
_Q='vismLapdAppType'
_P='vismLapdTrunkRowStatus'
_O='vismLapdTrunkRudpIndex'
_N='vismLapdTrunkState'
_M='vismLapdTrunkNum'
_L='unknown'
_K='milliseconds'
_J='vismLapdDlcTei'
_I='vismLapdDlcSapi'
_H='vismLapdDlcIndex'
_G='vismLapdStatsIndex'
_F='vismLapdIndex'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-WAN-LAPD-TRUNK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoWanLapdTrunkMIB=ModuleIdentity((1,3,6,1,4,1,351,150,23))
if mibBuilder.loadTexts:ciscoWanLapdTrunkMIB.setRevisions(('2003-12-11 00:00','2003-07-17 00:00','2003-07-11 00:00'))
_VismLapdGrp_ObjectIdentity=ObjectIdentity
vismLapdGrp=_VismLapdGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,12))
_VismLapdTable_Object=MibTable
vismLapdTable=_VismLapdTable_Object((1,3,6,1,4,1,351,110,5,5,12,1))
if mibBuilder.loadTexts:vismLapdTable.setStatus(_A)
_VismLapdEntry_Object=MibTableRow
vismLapdEntry=_VismLapdEntry_Object((1,3,6,1,4,1,351,110,5,5,12,1,1))
vismLapdEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vismLapdEntry.setStatus(_A)
class _VismLapdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismLapdIndex_Type.__name__=_D
_VismLapdIndex_Object=MibTableColumn
vismLapdIndex=_VismLapdIndex_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,1),_VismLapdIndex_Type())
vismLapdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdIndex.setStatus(_A)
class _VismLapdAppType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pri',1),('gr-303',2)))
_VismLapdAppType_Type.__name__=_D
_VismLapdAppType_Object=MibTableColumn
vismLapdAppType=_VismLapdAppType_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,2),_VismLapdAppType_Type())
vismLapdAppType.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdAppType.setStatus(_A)
class _VismLapdWinSize_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_VismLapdWinSize_Type.__name__=_D
_VismLapdWinSize_Object=MibTableColumn
vismLapdWinSize=_VismLapdWinSize_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,3),_VismLapdWinSize_Type())
vismLapdWinSize.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdWinSize.setStatus(_A)
class _VismLapdN200_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VismLapdN200_Type.__name__=_D
_VismLapdN200_Object=MibTableColumn
vismLapdN200=_VismLapdN200_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,4),_VismLapdN200_Type())
vismLapdN200.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdN200.setStatus(_A)
class _VismLapdT200_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1023000))
_VismLapdT200_Type.__name__=_D
_VismLapdT200_Object=MibTableColumn
vismLapdT200=_VismLapdT200_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,5),_VismLapdT200_Type())
vismLapdT200.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdT200.setStatus(_A)
if mibBuilder.loadTexts:vismLapdT200.setUnits(_K)
class _VismLapdT203_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1023000))
_VismLapdT203_Type.__name__=_D
_VismLapdT203_Object=MibTableColumn
vismLapdT203=_VismLapdT203_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,6),_VismLapdT203_Type())
vismLapdT203.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdT203.setStatus(_A)
if mibBuilder.loadTexts:vismLapdT203.setUnits(_K)
class _VismLapdType_Type(Integer32):defaultValue=19;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,6,7,8,9,10,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('ccitt',1),('att5EssPRA',3),('att4Ess',4),('ntDMS100PRA',6),('vn2or3',7),('insNet',8),('tr6MPC',9),('tr6PBX',10),('ausp',12),('ni1',13),('etsi',14),('bc303TMC',15),('bc303CSC',16),('ntDMS250',17),('bellcore',18),('ni2',19)))
_VismLapdType_Type.__name__=_D
_VismLapdType_Object=MibTableColumn
vismLapdType=_VismLapdType_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,7),_VismLapdType_Type())
vismLapdType.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdType.setStatus(_A)
_VismLapdRowStatus_Type=RowStatus
_VismLapdRowStatus_Object=MibTableColumn
vismLapdRowStatus=_VismLapdRowStatus_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,8),_VismLapdRowStatus_Type())
vismLapdRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdRowStatus.setStatus(_A)
class _VismLapdSide_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('network',1),('user',2)))
_VismLapdSide_Type.__name__=_D
_VismLapdSide_Object=MibTableColumn
vismLapdSide=_VismLapdSide_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,9),_VismLapdSide_Type())
vismLapdSide.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdSide.setStatus(_A)
class _VismLapdTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backhaul',1),('lapdTrunking',2)))
_VismLapdTrunkType_Type.__name__=_D
_VismLapdTrunkType_Object=MibTableColumn
vismLapdTrunkType=_VismLapdTrunkType_Object((1,3,6,1,4,1,351,110,5,5,12,1,1,10),_VismLapdTrunkType_Type())
vismLapdTrunkType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTrunkType.setStatus(_A)
_VismLapdStatsTable_Object=MibTable
vismLapdStatsTable=_VismLapdStatsTable_Object((1,3,6,1,4,1,351,110,5,5,12,2))
if mibBuilder.loadTexts:vismLapdStatsTable.setStatus(_A)
_VismLapdStatsEntry_Object=MibTableRow
vismLapdStatsEntry=_VismLapdStatsEntry_Object((1,3,6,1,4,1,351,110,5,5,12,2,1))
vismLapdStatsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vismLapdStatsEntry.setStatus(_A)
class _VismLapdStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismLapdStatsIndex_Type.__name__=_D
_VismLapdStatsIndex_Object=MibTableColumn
vismLapdStatsIndex=_VismLapdStatsIndex_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,1),_VismLapdStatsIndex_Type())
vismLapdStatsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdStatsIndex.setStatus(_A)
_VismLapdRxInfoFrames_Type=Counter32
_VismLapdRxInfoFrames_Object=MibTableColumn
vismLapdRxInfoFrames=_VismLapdRxInfoFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,2),_VismLapdRxInfoFrames_Type())
vismLapdRxInfoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxInfoFrames.setStatus(_A)
_VismLapdTxInfoFrames_Type=Counter32
_VismLapdTxInfoFrames_Object=MibTableColumn
vismLapdTxInfoFrames=_VismLapdTxInfoFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,3),_VismLapdTxInfoFrames_Type())
vismLapdTxInfoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxInfoFrames.setStatus(_A)
_VismLapdRxReadyFrames_Type=Counter32
_VismLapdRxReadyFrames_Object=MibTableColumn
vismLapdRxReadyFrames=_VismLapdRxReadyFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,4),_VismLapdRxReadyFrames_Type())
vismLapdRxReadyFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxReadyFrames.setStatus(_A)
_VismLapdTxReadyFrames_Type=Counter32
_VismLapdTxReadyFrames_Object=MibTableColumn
vismLapdTxReadyFrames=_VismLapdTxReadyFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,5),_VismLapdTxReadyFrames_Type())
vismLapdTxReadyFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxReadyFrames.setStatus(_A)
_VismLapdRxNotReadyFrames_Type=Counter32
_VismLapdRxNotReadyFrames_Object=MibTableColumn
vismLapdRxNotReadyFrames=_VismLapdRxNotReadyFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,6),_VismLapdRxNotReadyFrames_Type())
vismLapdRxNotReadyFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxNotReadyFrames.setStatus(_A)
_VismLapdTxNotReadyFrames_Type=Counter32
_VismLapdTxNotReadyFrames_Object=MibTableColumn
vismLapdTxNotReadyFrames=_VismLapdTxNotReadyFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,7),_VismLapdTxNotReadyFrames_Type())
vismLapdTxNotReadyFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxNotReadyFrames.setStatus(_A)
_VismLapdRxSABMFrames_Type=Counter32
_VismLapdRxSABMFrames_Object=MibTableColumn
vismLapdRxSABMFrames=_VismLapdRxSABMFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,8),_VismLapdRxSABMFrames_Type())
vismLapdRxSABMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxSABMFrames.setStatus(_A)
_VismLapdTxSABMFrames_Type=Counter32
_VismLapdTxSABMFrames_Object=MibTableColumn
vismLapdTxSABMFrames=_VismLapdTxSABMFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,9),_VismLapdTxSABMFrames_Type())
vismLapdTxSABMFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxSABMFrames.setStatus(_A)
_VismLapdRxDisconFrames_Type=Counter32
_VismLapdRxDisconFrames_Object=MibTableColumn
vismLapdRxDisconFrames=_VismLapdRxDisconFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,10),_VismLapdRxDisconFrames_Type())
vismLapdRxDisconFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxDisconFrames.setStatus(_A)
_VismLapdTxDisconFrames_Type=Counter32
_VismLapdTxDisconFrames_Object=MibTableColumn
vismLapdTxDisconFrames=_VismLapdTxDisconFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,11),_VismLapdTxDisconFrames_Type())
vismLapdTxDisconFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxDisconFrames.setStatus(_A)
_VismLapdRxUAFrames_Type=Counter32
_VismLapdRxUAFrames_Object=MibTableColumn
vismLapdRxUAFrames=_VismLapdRxUAFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,12),_VismLapdRxUAFrames_Type())
vismLapdRxUAFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxUAFrames.setStatus(_A)
_VismLapdTxUAFrames_Type=Counter32
_VismLapdTxUAFrames_Object=MibTableColumn
vismLapdTxUAFrames=_VismLapdTxUAFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,13),_VismLapdTxUAFrames_Type())
vismLapdTxUAFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxUAFrames.setStatus(_A)
_VismLapdRxDiscModeFrames_Type=Counter32
_VismLapdRxDiscModeFrames_Object=MibTableColumn
vismLapdRxDiscModeFrames=_VismLapdRxDiscModeFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,14),_VismLapdRxDiscModeFrames_Type())
vismLapdRxDiscModeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxDiscModeFrames.setStatus(_A)
_VismLapdTxDiscModeFrames_Type=Counter32
_VismLapdTxDiscModeFrames_Object=MibTableColumn
vismLapdTxDiscModeFrames=_VismLapdTxDiscModeFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,15),_VismLapdTxDiscModeFrames_Type())
vismLapdTxDiscModeFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxDiscModeFrames.setStatus(_A)
_VismLapdRxFrmRejectFrames_Type=Counter32
_VismLapdRxFrmRejectFrames_Object=MibTableColumn
vismLapdRxFrmRejectFrames=_VismLapdRxFrmRejectFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,16),_VismLapdRxFrmRejectFrames_Type())
vismLapdRxFrmRejectFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxFrmRejectFrames.setStatus(_A)
_VismLapdTxFrmRejectFrames_Type=Counter32
_VismLapdTxFrmRejectFrames_Object=MibTableColumn
vismLapdTxFrmRejectFrames=_VismLapdTxFrmRejectFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,17),_VismLapdTxFrmRejectFrames_Type())
vismLapdTxFrmRejectFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxFrmRejectFrames.setStatus(_A)
_VismLapdRxExchIdFrames_Type=Counter32
_VismLapdRxExchIdFrames_Object=MibTableColumn
vismLapdRxExchIdFrames=_VismLapdRxExchIdFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,18),_VismLapdRxExchIdFrames_Type())
vismLapdRxExchIdFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxExchIdFrames.setStatus(_A)
_VismLapdTxExchIdFrames_Type=Counter32
_VismLapdTxExchIdFrames_Object=MibTableColumn
vismLapdTxExchIdFrames=_VismLapdTxExchIdFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,19),_VismLapdTxExchIdFrames_Type())
vismLapdTxExchIdFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxExchIdFrames.setStatus(_A)
_VismLapdRxUnumInfoFrames_Type=Counter32
_VismLapdRxUnumInfoFrames_Object=MibTableColumn
vismLapdRxUnumInfoFrames=_VismLapdRxUnumInfoFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,20),_VismLapdRxUnumInfoFrames_Type())
vismLapdRxUnumInfoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxUnumInfoFrames.setStatus(_A)
_VismLapdTxUnumInfoFrames_Type=Counter32
_VismLapdTxUnumInfoFrames_Object=MibTableColumn
vismLapdTxUnumInfoFrames=_VismLapdTxUnumInfoFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,21),_VismLapdTxUnumInfoFrames_Type())
vismLapdTxUnumInfoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxUnumInfoFrames.setStatus(_A)
_VismLapdRxRejectFrames_Type=Counter32
_VismLapdRxRejectFrames_Object=MibTableColumn
vismLapdRxRejectFrames=_VismLapdRxRejectFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,22),_VismLapdRxRejectFrames_Type())
vismLapdRxRejectFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxRejectFrames.setStatus(_A)
_VismLapdTxRejectFrames_Type=Counter32
_VismLapdTxRejectFrames_Object=MibTableColumn
vismLapdTxRejectFrames=_VismLapdTxRejectFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,23),_VismLapdTxRejectFrames_Type())
vismLapdTxRejectFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTxRejectFrames.setStatus(_A)
_VismLapdRxInvalidFrames_Type=Counter32
_VismLapdRxInvalidFrames_Object=MibTableColumn
vismLapdRxInvalidFrames=_VismLapdRxInvalidFrames_Object((1,3,6,1,4,1,351,110,5,5,12,2,1,24),_VismLapdRxInvalidFrames_Type())
vismLapdRxInvalidFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdRxInvalidFrames.setStatus(_A)
_VismLapdDlcTable_Object=MibTable
vismLapdDlcTable=_VismLapdDlcTable_Object((1,3,6,1,4,1,351,110,5,5,12,3))
if mibBuilder.loadTexts:vismLapdDlcTable.setStatus(_A)
_VismLapdDlcEntry_Object=MibTableRow
vismLapdDlcEntry=_VismLapdDlcEntry_Object((1,3,6,1,4,1,351,110,5,5,12,3,1))
vismLapdDlcEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:vismLapdDlcEntry.setStatus(_A)
class _VismLapdDlcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismLapdDlcIndex_Type.__name__=_D
_VismLapdDlcIndex_Object=MibTableColumn
vismLapdDlcIndex=_VismLapdDlcIndex_Object((1,3,6,1,4,1,351,110,5,5,12,3,1,1),_VismLapdDlcIndex_Type())
vismLapdDlcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdDlcIndex.setStatus(_A)
class _VismLapdDlcSapi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismLapdDlcSapi_Type.__name__=_D
_VismLapdDlcSapi_Object=MibTableColumn
vismLapdDlcSapi=_VismLapdDlcSapi_Object((1,3,6,1,4,1,351,110,5,5,12,3,1,2),_VismLapdDlcSapi_Type())
vismLapdDlcSapi.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdDlcSapi.setStatus(_A)
class _VismLapdDlcTei_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismLapdDlcTei_Type.__name__=_D
_VismLapdDlcTei_Object=MibTableColumn
vismLapdDlcTei=_VismLapdDlcTei_Object((1,3,6,1,4,1,351,110,5,5,12,3,1,3),_VismLapdDlcTei_Type())
vismLapdDlcTei.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdDlcTei.setStatus(_A)
class _VismLapdDlcLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_L,3)))
_VismLapdDlcLinkState_Type.__name__=_D
_VismLapdDlcLinkState_Object=MibTableColumn
vismLapdDlcLinkState=_VismLapdDlcLinkState_Object((1,3,6,1,4,1,351,110,5,5,12,3,1,4),_VismLapdDlcLinkState_Type())
vismLapdDlcLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdDlcLinkState.setStatus(_A)
_CiscoWanLapdTrunkMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanLapdTrunkMIBObjects=_CiscoWanLapdTrunkMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,23,1))
_VismLapdTrunkGrp_ObjectIdentity=ObjectIdentity
vismLapdTrunkGrp=_VismLapdTrunkGrp_ObjectIdentity((1,3,6,1,4,1,351,150,23,1,1))
_VismLapdTrunkGrpTable_Object=MibTable
vismLapdTrunkGrpTable=_VismLapdTrunkGrpTable_Object((1,3,6,1,4,1,351,150,23,1,1,1))
if mibBuilder.loadTexts:vismLapdTrunkGrpTable.setStatus(_A)
_VismLapdTrunkGrpEntry_Object=MibTableRow
vismLapdTrunkGrpEntry=_VismLapdTrunkGrpEntry_Object((1,3,6,1,4,1,351,150,23,1,1,1,1))
vismLapdTrunkGrpEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:vismLapdTrunkGrpEntry.setStatus(_A)
class _VismLapdTrunkNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismLapdTrunkNum_Type.__name__=_D
_VismLapdTrunkNum_Object=MibTableColumn
vismLapdTrunkNum=_VismLapdTrunkNum_Object((1,3,6,1,4,1,351,150,23,1,1,1,1,1),_VismLapdTrunkNum_Type())
vismLapdTrunkNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vismLapdTrunkNum.setStatus(_A)
class _VismLapdTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oos',1),('is',2),(_L,3)))
_VismLapdTrunkState_Type.__name__=_D
_VismLapdTrunkState_Object=MibTableColumn
vismLapdTrunkState=_VismLapdTrunkState_Object((1,3,6,1,4,1,351,150,23,1,1,1,1,2),_VismLapdTrunkState_Type())
vismLapdTrunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLapdTrunkState.setStatus(_A)
class _VismLapdTrunkRudpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismLapdTrunkRudpIndex_Type.__name__=_D
_VismLapdTrunkRudpIndex_Object=MibTableColumn
vismLapdTrunkRudpIndex=_VismLapdTrunkRudpIndex_Object((1,3,6,1,4,1,351,150,23,1,1,1,1,3),_VismLapdTrunkRudpIndex_Type())
vismLapdTrunkRudpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdTrunkRudpIndex.setStatus(_A)
_VismLapdTrunkRowStatus_Type=RowStatus
_VismLapdTrunkRowStatus_Object=MibTableColumn
vismLapdTrunkRowStatus=_VismLapdTrunkRowStatus_Object((1,3,6,1,4,1,351,150,23,1,1,1,1,4),_VismLapdTrunkRowStatus_Type())
vismLapdTrunkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLapdTrunkRowStatus.setStatus(_A)
_VismLapdTrunkNotificationPrefix_ObjectIdentity=ObjectIdentity
vismLapdTrunkNotificationPrefix=_VismLapdTrunkNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,23,2))
_VismLapdTrunkNotifications_ObjectIdentity=ObjectIdentity
vismLapdTrunkNotifications=_VismLapdTrunkNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,23,2,0))
_VismLapdTrunkMIBConformance_ObjectIdentity=ObjectIdentity
vismLapdTrunkMIBConformance=_VismLapdTrunkMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,23,3))
_VismLapdTrunkMIBCompliances_ObjectIdentity=ObjectIdentity
vismLapdTrunkMIBCompliances=_VismLapdTrunkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,23,3,1))
_VismLapdTrunkMIBGroups_ObjectIdentity=ObjectIdentity
vismLapdTrunkMIBGroups=_VismLapdTrunkMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,23,3,2))
vismLapdTrunkGroup=ObjectGroup((1,3,6,1,4,1,351,150,23,3,2,1))
vismLapdTrunkGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:vismLapdTrunkGroup.setStatus(_A)
ciscoVismLapdGroup=ObjectGroup((1,3,6,1,4,1,351,150,23,3,2,2))
ciscoVismLapdGroup.setObjects(*((_B,_F),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoVismLapdGroup.setStatus(_A)
ciscoVismLapdStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,23,3,2,3))
ciscoVismLapdStatsGroup.setObjects(*((_B,_G),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoVismLapdStatsGroup.setStatus(_A)
ciscoVismLapdDlcTable=ObjectGroup((1,3,6,1,4,1,351,150,23,3,2,4))
ciscoVismLapdDlcTable.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_w)))
if mibBuilder.loadTexts:ciscoVismLapdDlcTable.setStatus(_A)
vismLapdTrunkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,23,3,1,1))
vismLapdTrunkMIBCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:vismLapdTrunkMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismLapdGrp':vismLapdGrp,'vismLapdTable':vismLapdTable,'vismLapdEntry':vismLapdEntry,_F:vismLapdIndex,_Q:vismLapdAppType,_R:vismLapdWinSize,_S:vismLapdN200,_T:vismLapdT200,_U:vismLapdT203,_V:vismLapdType,_W:vismLapdRowStatus,_X:vismLapdSide,_Y:vismLapdTrunkType,'vismLapdStatsTable':vismLapdStatsTable,'vismLapdStatsEntry':vismLapdStatsEntry,_G:vismLapdStatsIndex,_Z:vismLapdRxInfoFrames,_a:vismLapdTxInfoFrames,_b:vismLapdRxReadyFrames,_c:vismLapdTxReadyFrames,_d:vismLapdRxNotReadyFrames,_e:vismLapdTxNotReadyFrames,_f:vismLapdRxSABMFrames,_g:vismLapdTxSABMFrames,_h:vismLapdRxDisconFrames,_i:vismLapdTxDisconFrames,_j:vismLapdRxUAFrames,_k:vismLapdTxUAFrames,_l:vismLapdRxDiscModeFrames,_m:vismLapdTxDiscModeFrames,_n:vismLapdRxFrmRejectFrames,_o:vismLapdTxFrmRejectFrames,_p:vismLapdRxExchIdFrames,_q:vismLapdTxExchIdFrames,_r:vismLapdRxUnumInfoFrames,_s:vismLapdTxUnumInfoFrames,_t:vismLapdRxRejectFrames,_u:vismLapdTxRejectFrames,_v:vismLapdRxInvalidFrames,'vismLapdDlcTable':vismLapdDlcTable,'vismLapdDlcEntry':vismLapdDlcEntry,_H:vismLapdDlcIndex,_I:vismLapdDlcSapi,_J:vismLapdDlcTei,_w:vismLapdDlcLinkState,'ciscoWanLapdTrunkMIB':ciscoWanLapdTrunkMIB,'ciscoWanLapdTrunkMIBObjects':ciscoWanLapdTrunkMIBObjects,'vismLapdTrunkGrp':vismLapdTrunkGrp,'vismLapdTrunkGrpTable':vismLapdTrunkGrpTable,'vismLapdTrunkGrpEntry':vismLapdTrunkGrpEntry,_M:vismLapdTrunkNum,_N:vismLapdTrunkState,_O:vismLapdTrunkRudpIndex,_P:vismLapdTrunkRowStatus,'vismLapdTrunkNotificationPrefix':vismLapdTrunkNotificationPrefix,'vismLapdTrunkNotifications':vismLapdTrunkNotifications,'vismLapdTrunkMIBConformance':vismLapdTrunkMIBConformance,'vismLapdTrunkMIBCompliances':vismLapdTrunkMIBCompliances,'vismLapdTrunkMIBCompliance':vismLapdTrunkMIBCompliance,'vismLapdTrunkMIBGroups':vismLapdTrunkMIBGroups,_x:vismLapdTrunkGroup,_y:ciscoVismLapdGroup,_z:ciscoVismLapdStatsGroup,_A0:ciscoVismLapdDlcTable})