_S='cwbAtmConnStatsGroup'
_R='bbChanCntClrButton'
_Q='bbChanDscdClpOneCellsToPort'
_P='bbChanDscdClpZeroCellsToPort'
_O='bbChanXmtClp1Cells'
_N='bbChanXmtClp0Cells'
_M='bbChanRcvCellsSent'
_L='bbChanDscdClp1Cells'
_K='bbChanDscdClp0Cells'
_J='bbChanRcvEOFCells'
_I='bbChanNonConformCellsAtGcra2Policer'
_H='bbChanNonConformCellsAtGcra1Policer'
_G='bbChanRcvClp1Cells'
_F='bbChanRcvClp0Cells'
_E='bbChanCntNum'
_D='Integer32'
_C='read-only'
_B='CISCO-WAN-BBIF-ATM-CONN-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bbChanCntGrp,=mibBuilder.importSymbols('BASIS-MIB','bbChanCntGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanBbifAtmConnStatMIB=ModuleIdentity((1,3,6,1,4,1,351,150,36))
if mibBuilder.loadTexts:ciscoWanBbifAtmConnStatMIB.setRevisions(('2002-10-18 00:00',))
_BbChanCntGrpTable_Object=MibTable
bbChanCntGrpTable=_BbChanCntGrpTable_Object((1,3,6,1,4,1,351,110,5,2,7,3,1))
if mibBuilder.loadTexts:bbChanCntGrpTable.setStatus(_A)
_BbChanCntGrpEntry_Object=MibTableRow
bbChanCntGrpEntry=_BbChanCntGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1))
bbChanCntGrpEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:bbChanCntGrpEntry.setStatus(_A)
class _BbChanCntNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4111))
_BbChanCntNum_Type.__name__=_D
_BbChanCntNum_Object=MibTableColumn
bbChanCntNum=_BbChanCntNum_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,1),_BbChanCntNum_Type())
bbChanCntNum.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanCntNum.setStatus(_A)
_BbChanRcvClp0Cells_Type=Counter32
_BbChanRcvClp0Cells_Object=MibTableColumn
bbChanRcvClp0Cells=_BbChanRcvClp0Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,2),_BbChanRcvClp0Cells_Type())
bbChanRcvClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanRcvClp0Cells.setStatus(_A)
_BbChanRcvClp1Cells_Type=Counter32
_BbChanRcvClp1Cells_Object=MibTableColumn
bbChanRcvClp1Cells=_BbChanRcvClp1Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,3),_BbChanRcvClp1Cells_Type())
bbChanRcvClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanRcvClp1Cells.setStatus(_A)
_BbChanNonConformCellsAtGcra1Policer_Type=Counter32
_BbChanNonConformCellsAtGcra1Policer_Object=MibTableColumn
bbChanNonConformCellsAtGcra1Policer=_BbChanNonConformCellsAtGcra1Policer_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,4),_BbChanNonConformCellsAtGcra1Policer_Type())
bbChanNonConformCellsAtGcra1Policer.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanNonConformCellsAtGcra1Policer.setStatus(_A)
_BbChanNonConformCellsAtGcra2Policer_Type=Counter32
_BbChanNonConformCellsAtGcra2Policer_Object=MibTableColumn
bbChanNonConformCellsAtGcra2Policer=_BbChanNonConformCellsAtGcra2Policer_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,5),_BbChanNonConformCellsAtGcra2Policer_Type())
bbChanNonConformCellsAtGcra2Policer.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanNonConformCellsAtGcra2Policer.setStatus(_A)
_BbChanRcvEOFCells_Type=Counter32
_BbChanRcvEOFCells_Object=MibTableColumn
bbChanRcvEOFCells=_BbChanRcvEOFCells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,6),_BbChanRcvEOFCells_Type())
bbChanRcvEOFCells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanRcvEOFCells.setStatus(_A)
_BbChanDscdClp0Cells_Type=Counter32
_BbChanDscdClp0Cells_Object=MibTableColumn
bbChanDscdClp0Cells=_BbChanDscdClp0Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,7),_BbChanDscdClp0Cells_Type())
bbChanDscdClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanDscdClp0Cells.setStatus(_A)
_BbChanDscdClp1Cells_Type=Counter32
_BbChanDscdClp1Cells_Object=MibTableColumn
bbChanDscdClp1Cells=_BbChanDscdClp1Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,8),_BbChanDscdClp1Cells_Type())
bbChanDscdClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanDscdClp1Cells.setStatus(_A)
_BbChanRcvCellsSent_Type=Counter32
_BbChanRcvCellsSent_Object=MibTableColumn
bbChanRcvCellsSent=_BbChanRcvCellsSent_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,9),_BbChanRcvCellsSent_Type())
bbChanRcvCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanRcvCellsSent.setStatus(_A)
_BbChanXmtClp0Cells_Type=Counter32
_BbChanXmtClp0Cells_Object=MibTableColumn
bbChanXmtClp0Cells=_BbChanXmtClp0Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,10),_BbChanXmtClp0Cells_Type())
bbChanXmtClp0Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanXmtClp0Cells.setStatus(_A)
_BbChanXmtClp1Cells_Type=Counter32
_BbChanXmtClp1Cells_Object=MibTableColumn
bbChanXmtClp1Cells=_BbChanXmtClp1Cells_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,11),_BbChanXmtClp1Cells_Type())
bbChanXmtClp1Cells.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanXmtClp1Cells.setStatus(_A)
_BbChanDscdClpZeroCellsToPort_Type=Counter32
_BbChanDscdClpZeroCellsToPort_Object=MibTableColumn
bbChanDscdClpZeroCellsToPort=_BbChanDscdClpZeroCellsToPort_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,12),_BbChanDscdClpZeroCellsToPort_Type())
bbChanDscdClpZeroCellsToPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanDscdClpZeroCellsToPort.setStatus(_A)
_BbChanDscdClpOneCellsToPort_Type=Counter32
_BbChanDscdClpOneCellsToPort_Object=MibTableColumn
bbChanDscdClpOneCellsToPort=_BbChanDscdClpOneCellsToPort_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,13),_BbChanDscdClpOneCellsToPort_Type())
bbChanDscdClpOneCellsToPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bbChanDscdClpOneCellsToPort.setStatus(_A)
class _BbChanCntClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('resetCounters',2)))
_BbChanCntClrButton_Type.__name__=_D
_BbChanCntClrButton_Object=MibTableColumn
bbChanCntClrButton=_BbChanCntClrButton_Object((1,3,6,1,4,1,351,110,5,2,7,3,1,1,14),_BbChanCntClrButton_Type())
bbChanCntClrButton.setMaxAccess('read-write')
if mibBuilder.loadTexts:bbChanCntClrButton.setStatus(_A)
_CwbAtmConnStatMIBConformance_ObjectIdentity=ObjectIdentity
cwbAtmConnStatMIBConformance=_CwbAtmConnStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,36,2))
_CwbAtmConnStatMIBGroups_ObjectIdentity=ObjectIdentity
cwbAtmConnStatMIBGroups=_CwbAtmConnStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,36,2,1))
_CwbAtmConnStatMIBCompliances_ObjectIdentity=ObjectIdentity
cwbAtmConnStatMIBCompliances=_CwbAtmConnStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,36,2,2))
cwbAtmConnStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,36,2,1,1))
cwbAtmConnStatsGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:cwbAtmConnStatsGroup.setStatus(_A)
cwbAtmConnStatCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,36,2,2,1))
cwbAtmConnStatCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:cwbAtmConnStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bbChanCntGrpTable':bbChanCntGrpTable,'bbChanCntGrpEntry':bbChanCntGrpEntry,_E:bbChanCntNum,_F:bbChanRcvClp0Cells,_G:bbChanRcvClp1Cells,_H:bbChanNonConformCellsAtGcra1Policer,_I:bbChanNonConformCellsAtGcra2Policer,_J:bbChanRcvEOFCells,_K:bbChanDscdClp0Cells,_L:bbChanDscdClp1Cells,_M:bbChanRcvCellsSent,_N:bbChanXmtClp0Cells,_O:bbChanXmtClp1Cells,_P:bbChanDscdClpZeroCellsToPort,_Q:bbChanDscdClpOneCellsToPort,_R:bbChanCntClrButton,'ciscoWanBbifAtmConnStatMIB':ciscoWanBbifAtmConnStatMIB,'cwbAtmConnStatMIBConformance':cwbAtmConnStatMIBConformance,'cwbAtmConnStatMIBGroups':cwbAtmConnStatMIBGroups,_S:cwbAtmConnStatsGroup,'cwbAtmConnStatMIBCompliances':cwbAtmConnStatMIBCompliances,'cwbAtmConnStatCompliance':cwbAtmConnStatCompliance})