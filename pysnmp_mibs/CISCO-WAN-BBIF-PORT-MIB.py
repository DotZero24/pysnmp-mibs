_k='cwbPortStatsGroup'
_j='cwbPortConfGroup'
_i='bbIfRcvErroredCells'
_h='bbIfCntClrButton'
_g='bbIfXmtClp1Cells'
_f='bbIfXmtClp0Cells'
_e='bbIfXmtRmCells'
_d='bbIfXmtOAMCells'
_c='bbIfRcvClp1DiscCells'
_b='bbIfRcvClp0DiscCells'
_a='bbIfRcvClp1Cells'
_Z='bbIfRcvClp0Cells'
_Y='bbIfRcvRmCells'
_X='bbIfRcvValidOAMCells'
_W='bbIfTotalCells'
_V='bbIfEgrPercentUtil'
_U='bbIfIngrPercentUtil'
_T='bbIfOversubscribed'
_S='bbIfState'
_R='bbIfMaxCellRatePct'
_Q='bbIfSpeed'
_P='bbIfMaxVpi'
_O='bbIfMinVpi'
_N='bbIfEgrPctBandwidth'
_M='bbIfIngrPctBandwidth'
_L='bbIfLineNum'
_K='bbIfAdmin'
_J='bbIfRowStatus'
_I='nextBbIfNumAvailable'
_H='bbCntIfNum'
_G='bbStateIfNum'
_F='bbIfNum'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WAN-BBIF-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bbIfCnf,bbIfCnt,bbIfStateGrp=mibBuilder.importSymbols('BASIS-MIB','bbIfCnf','bbIfCnt','bbIfStateGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanBbifPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,32))
if mibBuilder.loadTexts:ciscoWanBbifPortMIB.setRevisions(('2002-08-30 00:00',))
_BbIfCnfPortGrp_ObjectIdentity=ObjectIdentity
bbIfCnfPortGrp=_BbIfCnfPortGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,6,1,1))
_BbIfCnfPortGrpTable_Object=MibTable
bbIfCnfPortGrpTable=_BbIfCnfPortGrpTable_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1))
if mibBuilder.loadTexts:bbIfCnfPortGrpTable.setStatus(_A)
_BbIfCnfPortGrpEntry_Object=MibTableRow
bbIfCnfPortGrpEntry=_BbIfCnfPortGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1))
bbIfCnfPortGrpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:bbIfCnfPortGrpEntry.setStatus(_A)
class _BbIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BbIfNum_Type.__name__=_D
_BbIfNum_Object=MibTableColumn
bbIfNum=_BbIfNum_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,1),_BbIfNum_Type())
bbIfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfNum.setStatus(_A)
class _BbIfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_BbIfRowStatus_Type.__name__=_D
_BbIfRowStatus_Object=MibTableColumn
bbIfRowStatus=_BbIfRowStatus_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,2),_BbIfRowStatus_Type())
bbIfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfRowStatus.setStatus(_A)
class _BbIfAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('writeOnly',3)))
_BbIfAdmin_Type.__name__=_D
_BbIfAdmin_Object=MibTableColumn
bbIfAdmin=_BbIfAdmin_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,3),_BbIfAdmin_Type())
bbIfAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfAdmin.setStatus(_A)
class _BbIfLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BbIfLineNum_Type.__name__=_D
_BbIfLineNum_Object=MibTableColumn
bbIfLineNum=_BbIfLineNum_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,4),_BbIfLineNum_Type())
bbIfLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfLineNum.setStatus(_A)
class _BbIfIngrPctBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbIfIngrPctBandwidth_Type.__name__=_D
_BbIfIngrPctBandwidth_Object=MibTableColumn
bbIfIngrPctBandwidth=_BbIfIngrPctBandwidth_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,5),_BbIfIngrPctBandwidth_Type())
bbIfIngrPctBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfIngrPctBandwidth.setStatus(_A)
class _BbIfEgrPctBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbIfEgrPctBandwidth_Type.__name__=_D
_BbIfEgrPctBandwidth_Object=MibTableColumn
bbIfEgrPctBandwidth=_BbIfEgrPctBandwidth_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,6),_BbIfEgrPctBandwidth_Type())
bbIfEgrPctBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfEgrPctBandwidth.setStatus(_A)
class _BbIfMinVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbIfMinVpi_Type.__name__=_D
_BbIfMinVpi_Object=MibTableColumn
bbIfMinVpi=_BbIfMinVpi_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,7),_BbIfMinVpi_Type())
bbIfMinVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfMinVpi.setStatus(_A)
class _BbIfMaxVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbIfMaxVpi_Type.__name__=_D
_BbIfMaxVpi_Object=MibTableColumn
bbIfMaxVpi=_BbIfMaxVpi_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,8),_BbIfMaxVpi_Type())
bbIfMaxVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfMaxVpi.setStatus(_A)
_BbIfSpeed_Type=Integer32
_BbIfSpeed_Object=MibTableColumn
bbIfSpeed=_BbIfSpeed_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,9),_BbIfSpeed_Type())
bbIfSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfSpeed.setStatus(_A)
class _BbIfMaxCellRatePct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbIfMaxCellRatePct_Type.__name__=_D
_BbIfMaxCellRatePct_Object=MibTableColumn
bbIfMaxCellRatePct=_BbIfMaxCellRatePct_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,1,1,10),_BbIfMaxCellRatePct_Type())
bbIfMaxCellRatePct.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfMaxCellRatePct.setStatus(_A)
class _NextBbIfNumAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_NextBbIfNumAvailable_Type.__name__=_D
_NextBbIfNumAvailable_Object=MibScalar
nextBbIfNumAvailable=_NextBbIfNumAvailable_Object((1,3,6,1,4,1,351,110,5,2,6,1,1,2),_NextBbIfNumAvailable_Type())
nextBbIfNumAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:nextBbIfNumAvailable.setStatus(_A)
_BbIfStateGrpTable_Object=MibTable
bbIfStateGrpTable=_BbIfStateGrpTable_Object((1,3,6,1,4,1,351,110,5,2,6,3,1))
if mibBuilder.loadTexts:bbIfStateGrpTable.setStatus(_A)
_BbIfStateGrpEntry_Object=MibTableRow
bbIfStateGrpEntry=_BbIfStateGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1))
bbIfStateGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bbIfStateGrpEntry.setStatus(_A)
class _BbStateIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BbStateIfNum_Type.__name__=_D
_BbStateIfNum_Object=MibTableColumn
bbStateIfNum=_BbStateIfNum_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1,1),_BbStateIfNum_Type())
bbStateIfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bbStateIfNum.setStatus(_A)
class _BbIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('linefailure',4),('signallingfailure',5),('inactive',6),('lineinloopback',7)))
_BbIfState_Type.__name__=_D
_BbIfState_Object=MibTableColumn
bbIfState=_BbIfState_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1,2),_BbIfState_Type())
bbIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfState.setStatus(_A)
class _BbIfOversubscribed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_BbIfOversubscribed_Type.__name__=_D
_BbIfOversubscribed_Object=MibTableColumn
bbIfOversubscribed=_BbIfOversubscribed_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1,3),_BbIfOversubscribed_Type())
bbIfOversubscribed.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfOversubscribed.setStatus(_A)
class _BbIfIngrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_BbIfIngrPercentUtil_Type.__name__=_D
_BbIfIngrPercentUtil_Object=MibTableColumn
bbIfIngrPercentUtil=_BbIfIngrPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1,4),_BbIfIngrPercentUtil_Type())
bbIfIngrPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfIngrPercentUtil.setStatus(_A)
class _BbIfEgrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_BbIfEgrPercentUtil_Type.__name__=_D
_BbIfEgrPercentUtil_Object=MibTableColumn
bbIfEgrPercentUtil=_BbIfEgrPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,6,3,1,1,5),_BbIfEgrPercentUtil_Type())
bbIfEgrPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfEgrPercentUtil.setStatus(_A)
_BbIfCntGrp_ObjectIdentity=ObjectIdentity
bbIfCntGrp=_BbIfCntGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,2,6,4,1))
_BbIfCntGrpTable_Object=MibTable
bbIfCntGrpTable=_BbIfCntGrpTable_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1))
if mibBuilder.loadTexts:bbIfCntGrpTable.setStatus(_A)
_BbIfCntGrpEntry_Object=MibTableRow
bbIfCntGrpEntry=_BbIfCntGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1))
bbIfCntGrpEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:bbIfCntGrpEntry.setStatus(_A)
class _BbCntIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BbCntIfNum_Type.__name__=_D
_BbCntIfNum_Object=MibTableColumn
bbCntIfNum=_BbCntIfNum_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,1),_BbCntIfNum_Type())
bbCntIfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bbCntIfNum.setStatus(_A)
_BbIfTotalCells_Type=Counter32
_BbIfTotalCells_Object=MibTableColumn
bbIfTotalCells=_BbIfTotalCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,2),_BbIfTotalCells_Type())
bbIfTotalCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfTotalCells.setStatus(_A)
_BbIfRcvValidOAMCells_Type=Counter32
_BbIfRcvValidOAMCells_Object=MibTableColumn
bbIfRcvValidOAMCells=_BbIfRcvValidOAMCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,3),_BbIfRcvValidOAMCells_Type())
bbIfRcvValidOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvValidOAMCells.setStatus(_A)
_BbIfRcvRmCells_Type=Counter32
_BbIfRcvRmCells_Object=MibTableColumn
bbIfRcvRmCells=_BbIfRcvRmCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,4),_BbIfRcvRmCells_Type())
bbIfRcvRmCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvRmCells.setStatus(_A)
_BbIfRcvClp0Cells_Type=Counter32
_BbIfRcvClp0Cells_Object=MibTableColumn
bbIfRcvClp0Cells=_BbIfRcvClp0Cells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,5),_BbIfRcvClp0Cells_Type())
bbIfRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvClp0Cells.setStatus(_A)
_BbIfRcvClp1Cells_Type=Counter32
_BbIfRcvClp1Cells_Object=MibTableColumn
bbIfRcvClp1Cells=_BbIfRcvClp1Cells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,6),_BbIfRcvClp1Cells_Type())
bbIfRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvClp1Cells.setStatus(_A)
_BbIfRcvClp0DiscCells_Type=Counter32
_BbIfRcvClp0DiscCells_Object=MibTableColumn
bbIfRcvClp0DiscCells=_BbIfRcvClp0DiscCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,7),_BbIfRcvClp0DiscCells_Type())
bbIfRcvClp0DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvClp0DiscCells.setStatus(_A)
_BbIfRcvClp1DiscCells_Type=Counter32
_BbIfRcvClp1DiscCells_Object=MibTableColumn
bbIfRcvClp1DiscCells=_BbIfRcvClp1DiscCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,8),_BbIfRcvClp1DiscCells_Type())
bbIfRcvClp1DiscCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvClp1DiscCells.setStatus(_A)
_BbIfXmtOAMCells_Type=Counter32
_BbIfXmtOAMCells_Object=MibTableColumn
bbIfXmtOAMCells=_BbIfXmtOAMCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,9),_BbIfXmtOAMCells_Type())
bbIfXmtOAMCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfXmtOAMCells.setStatus(_A)
_BbIfXmtRmCells_Type=Counter32
_BbIfXmtRmCells_Object=MibTableColumn
bbIfXmtRmCells=_BbIfXmtRmCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,10),_BbIfXmtRmCells_Type())
bbIfXmtRmCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfXmtRmCells.setStatus(_A)
_BbIfXmtClp0Cells_Type=Counter32
_BbIfXmtClp0Cells_Object=MibTableColumn
bbIfXmtClp0Cells=_BbIfXmtClp0Cells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,11),_BbIfXmtClp0Cells_Type())
bbIfXmtClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfXmtClp0Cells.setStatus(_A)
_BbIfXmtClp1Cells_Type=Counter32
_BbIfXmtClp1Cells_Object=MibTableColumn
bbIfXmtClp1Cells=_BbIfXmtClp1Cells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,12),_BbIfXmtClp1Cells_Type())
bbIfXmtClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfXmtClp1Cells.setStatus(_A)
class _BbIfCntClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('resetCounter32s',2)))
_BbIfCntClrButton_Type.__name__=_D
_BbIfCntClrButton_Object=MibTableColumn
bbIfCntClrButton=_BbIfCntClrButton_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,13),_BbIfCntClrButton_Type())
bbIfCntClrButton.setMaxAccess(_E)
if mibBuilder.loadTexts:bbIfCntClrButton.setStatus(_A)
_BbIfRcvErroredCells_Type=Counter32
_BbIfRcvErroredCells_Object=MibTableColumn
bbIfRcvErroredCells=_BbIfRcvErroredCells_Object((1,3,6,1,4,1,351,110,5,2,6,4,1,1,1,14),_BbIfRcvErroredCells_Type())
bbIfRcvErroredCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbIfRcvErroredCells.setStatus(_A)
_CwbPortMIBConformance_ObjectIdentity=ObjectIdentity
cwbPortMIBConformance=_CwbPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,32,2))
_CwbPortMIBGroups_ObjectIdentity=ObjectIdentity
cwbPortMIBGroups=_CwbPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,32,2,1))
_CwbPortMIBCompliances_ObjectIdentity=ObjectIdentity
cwbPortMIBCompliances=_CwbPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,32,2,2))
cwbPortGenearlGroup=ObjectGroup((1,3,6,1,4,1,351,150,32,2,1,1))
cwbPortGenearlGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:cwbPortGenearlGroup.setStatus(_A)
cwbPortConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,32,2,1,2))
cwbPortConfGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cwbPortConfGroup.setStatus(_A)
cwbPortStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,32,2,1,3))
cwbPortStateGroup.setObjects(*((_B,_G),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cwbPortStateGroup.setStatus(_A)
cwbPortStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,32,2,1,4))
cwbPortStatsGroup.setObjects(*((_B,_H),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cwbPortStatsGroup.setStatus(_A)
cwbPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,32,2,2,1))
cwbPortCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cwbPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bbIfCnfPortGrp':bbIfCnfPortGrp,'bbIfCnfPortGrpTable':bbIfCnfPortGrpTable,'bbIfCnfPortGrpEntry':bbIfCnfPortGrpEntry,_F:bbIfNum,_J:bbIfRowStatus,_K:bbIfAdmin,_L:bbIfLineNum,_M:bbIfIngrPctBandwidth,_N:bbIfEgrPctBandwidth,_O:bbIfMinVpi,_P:bbIfMaxVpi,_Q:bbIfSpeed,_R:bbIfMaxCellRatePct,_I:nextBbIfNumAvailable,'bbIfStateGrpTable':bbIfStateGrpTable,'bbIfStateGrpEntry':bbIfStateGrpEntry,_G:bbStateIfNum,_S:bbIfState,_T:bbIfOversubscribed,_U:bbIfIngrPercentUtil,_V:bbIfEgrPercentUtil,'bbIfCntGrp':bbIfCntGrp,'bbIfCntGrpTable':bbIfCntGrpTable,'bbIfCntGrpEntry':bbIfCntGrpEntry,_H:bbCntIfNum,_W:bbIfTotalCells,_X:bbIfRcvValidOAMCells,_Y:bbIfRcvRmCells,_Z:bbIfRcvClp0Cells,_a:bbIfRcvClp1Cells,_b:bbIfRcvClp0DiscCells,_c:bbIfRcvClp1DiscCells,_d:bbIfXmtOAMCells,_e:bbIfXmtRmCells,_f:bbIfXmtClp0Cells,_g:bbIfXmtClp1Cells,_h:bbIfCntClrButton,_i:bbIfRcvErroredCells,'ciscoWanBbifPortMIB':ciscoWanBbifPortMIB,'cwbPortMIBConformance':cwbPortMIBConformance,'cwbPortMIBGroups':cwbPortMIBGroups,'cwbPortGenearlGroup':cwbPortGenearlGroup,_j:cwbPortConfGroup,'cwbPortStateGroup':cwbPortStateGroup,_k:cwbPortStatsGroup,'cwbPortMIBCompliances':cwbPortMIBCompliances,'cwbPortCompliance':cwbPortCompliance})