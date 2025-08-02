_e='fsMmuIfSliceIndexPriorityGroup'
_d='fsMmuIfPriorityGroupIdIndex'
_c='fsMmuIfIndexPriorityGroup'
_b='fsMmuIfSliceIndexMulticast'
_a='fsMmuIfMulticastQueueIndex'
_Z='fsMmuIfIndexMulticast'
_Y='fsMmuIfSliceIndex'
_X='fsMmuIfQueueIndex'
_W='fsMmuIfIndex'
_V='fsVoqWarnPgId'
_U='fsVoqWarnSlotId'
_T='fsVoqWarnDevId'
_S='fsVoqWarnQueueId'
_R='fsVoqWarnIfxId'
_Q='fsWarnPgId'
_P='fsWarnSlotId'
_O='fsWarnDevId'
_N='fsWarnIfxId'
_M='fsOutPgId'
_L='fsOutSlotId'
_K='fsOutDevId'
_J='fsOutQueueId'
_I='fsOutIfxId'
_H='fsInPgId'
_G='fsInSlotId'
_F='fsInDevId'
_E='fsInQueueId'
_D='fsInIfxId'
_C='FS-MMU-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsMMUMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,141))
if mibBuilder.loadTexts:fsMMUMIB.setRevisions(('2015-06-24 00:00',))
_FsMmuIfVoqInTable_Object=MibTable
fsMmuIfVoqInTable=_FsMmuIfVoqInTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1))
if mibBuilder.loadTexts:fsMmuIfVoqInTable.setStatus(_A)
_FsMmuIfVoqInEntry_Object=MibTableRow
fsMmuIfVoqInEntry=_FsMmuIfVoqInEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1))
fsMmuIfVoqInEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsMmuIfVoqInEntry.setStatus(_A)
_FsInIfxId_Type=IfIndex
_FsInIfxId_Object=MibTableColumn
fsInIfxId=_FsInIfxId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,1),_FsInIfxId_Type())
fsInIfxId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInIfxId.setStatus(_A)
_FsInQueueId_Type=Integer32
_FsInQueueId_Object=MibTableColumn
fsInQueueId=_FsInQueueId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,2),_FsInQueueId_Type())
fsInQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInQueueId.setStatus(_A)
_FsInDevId_Type=Integer32
_FsInDevId_Object=MibTableColumn
fsInDevId=_FsInDevId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,3),_FsInDevId_Type())
fsInDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInDevId.setStatus(_A)
_FsInSlotId_Type=Integer32
_FsInSlotId_Object=MibTableColumn
fsInSlotId=_FsInSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,4),_FsInSlotId_Type())
fsInSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInSlotId.setStatus(_A)
_FsInPgId_Type=Integer32
_FsInPgId_Object=MibTableColumn
fsInPgId=_FsInPgId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,5),_FsInPgId_Type())
fsInPgId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInPgId.setStatus(_A)
_FsInTransmitPackets_Type=Counter64
_FsInTransmitPackets_Object=MibTableColumn
fsInTransmitPackets=_FsInTransmitPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,6),_FsInTransmitPackets_Type())
fsInTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInTransmitPackets.setStatus(_A)
_FsInTransmitBytes_Type=Counter64
_FsInTransmitBytes_Object=MibTableColumn
fsInTransmitBytes=_FsInTransmitBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,7),_FsInTransmitBytes_Type())
fsInTransmitBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInTransmitBytes.setStatus(_A)
_FsInDropPackets_Type=Counter64
_FsInDropPackets_Object=MibTableColumn
fsInDropPackets=_FsInDropPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,8),_FsInDropPackets_Type())
fsInDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInDropPackets.setStatus(_A)
_FsInDropBytes_Type=Counter64
_FsInDropBytes_Object=MibTableColumn
fsInDropBytes=_FsInDropBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,141,1,1,9),_FsInDropBytes_Type())
fsInDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsInDropBytes.setStatus(_A)
_FsMmuIfVoqOutTable_Object=MibTable
fsMmuIfVoqOutTable=_FsMmuIfVoqOutTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2))
if mibBuilder.loadTexts:fsMmuIfVoqOutTable.setStatus(_A)
_FsMmuIfVoqOutEntry_Object=MibTableRow
fsMmuIfVoqOutEntry=_FsMmuIfVoqOutEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1))
fsMmuIfVoqOutEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsMmuIfVoqOutEntry.setStatus(_A)
_FsOutIfxId_Type=IfIndex
_FsOutIfxId_Object=MibTableColumn
fsOutIfxId=_FsOutIfxId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,1),_FsOutIfxId_Type())
fsOutIfxId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutIfxId.setStatus(_A)
_FsOutQueueId_Type=Integer32
_FsOutQueueId_Object=MibTableColumn
fsOutQueueId=_FsOutQueueId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,2),_FsOutQueueId_Type())
fsOutQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutQueueId.setStatus(_A)
_FsOutDevId_Type=Integer32
_FsOutDevId_Object=MibTableColumn
fsOutDevId=_FsOutDevId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,3),_FsOutDevId_Type())
fsOutDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutDevId.setStatus(_A)
_FsOutSlotId_Type=Integer32
_FsOutSlotId_Object=MibTableColumn
fsOutSlotId=_FsOutSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,4),_FsOutSlotId_Type())
fsOutSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutSlotId.setStatus(_A)
_FsOutPgId_Type=Integer32
_FsOutPgId_Object=MibTableColumn
fsOutPgId=_FsOutPgId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,5),_FsOutPgId_Type())
fsOutPgId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutPgId.setStatus(_A)
_FsOutTransmitPackets_Type=Counter64
_FsOutTransmitPackets_Object=MibTableColumn
fsOutTransmitPackets=_FsOutTransmitPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,6),_FsOutTransmitPackets_Type())
fsOutTransmitPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutTransmitPackets.setStatus(_A)
_FsOutTransmitBytes_Type=Counter64
_FsOutTransmitBytes_Object=MibTableColumn
fsOutTransmitBytes=_FsOutTransmitBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,7),_FsOutTransmitBytes_Type())
fsOutTransmitBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutTransmitBytes.setStatus(_A)
_FsOutDropPackets_Type=Counter64
_FsOutDropPackets_Object=MibTableColumn
fsOutDropPackets=_FsOutDropPackets_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,8),_FsOutDropPackets_Type())
fsOutDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutDropPackets.setStatus(_A)
_FsOutDropBytes_Type=Counter64
_FsOutDropBytes_Object=MibTableColumn
fsOutDropBytes=_FsOutDropBytes_Object((1,3,6,1,4,1,52642,1,1,10,2,141,2,1,9),_FsOutDropBytes_Type())
fsOutDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fsOutDropBytes.setStatus(_A)
_FsMmuIfWarnTable_Object=MibTable
fsMmuIfWarnTable=_FsMmuIfWarnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3))
if mibBuilder.loadTexts:fsMmuIfWarnTable.setStatus(_A)
_FsMmuIfWarnEntry_Object=MibTableRow
fsMmuIfWarnEntry=_FsMmuIfWarnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1))
fsMmuIfWarnEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsMmuIfWarnEntry.setStatus(_A)
_FsWarnIfxId_Type=IfIndex
_FsWarnIfxId_Object=MibTableColumn
fsWarnIfxId=_FsWarnIfxId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,1),_FsWarnIfxId_Type())
fsWarnIfxId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnIfxId.setStatus(_A)
_FsWarnDevId_Type=Integer32
_FsWarnDevId_Object=MibTableColumn
fsWarnDevId=_FsWarnDevId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,2),_FsWarnDevId_Type())
fsWarnDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnDevId.setStatus(_A)
_FsWarnSlotId_Type=Integer32
_FsWarnSlotId_Object=MibTableColumn
fsWarnSlotId=_FsWarnSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,3),_FsWarnSlotId_Type())
fsWarnSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnSlotId.setStatus(_A)
_FsWarnPgId_Type=Integer32
_FsWarnPgId_Object=MibTableColumn
fsWarnPgId=_FsWarnPgId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,4),_FsWarnPgId_Type())
fsWarnPgId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnPgId.setStatus(_A)
_FsWarnUsedCell_Type=Integer32
_FsWarnUsedCell_Object=MibTableColumn
fsWarnUsedCell=_FsWarnUsedCell_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,5),_FsWarnUsedCell_Type())
fsWarnUsedCell.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnUsedCell.setStatus(_A)
_FsWarnTotalCell_Type=Integer32
_FsWarnTotalCell_Object=MibTableColumn
fsWarnTotalCell=_FsWarnTotalCell_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,6),_FsWarnTotalCell_Type())
fsWarnTotalCell.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnTotalCell.setStatus(_A)
_FsWarnLimit_Type=Integer32
_FsWarnLimit_Object=MibTableColumn
fsWarnLimit=_FsWarnLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,7),_FsWarnLimit_Type())
fsWarnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnLimit.setStatus(_A)
_FsWarnCount_Type=Integer32
_FsWarnCount_Object=MibTableColumn
fsWarnCount=_FsWarnCount_Object((1,3,6,1,4,1,52642,1,1,10,2,141,3,1,8),_FsWarnCount_Type())
fsWarnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWarnCount.setStatus(_A)
_FsMmuIfVoqWarnTable_Object=MibTable
fsMmuIfVoqWarnTable=_FsMmuIfVoqWarnTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4))
if mibBuilder.loadTexts:fsMmuIfVoqWarnTable.setStatus(_A)
_FsMmuIfVoqWarnEntry_Object=MibTableRow
fsMmuIfVoqWarnEntry=_FsMmuIfVoqWarnEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1))
fsMmuIfVoqWarnEntry.setIndexNames((0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:fsMmuIfVoqWarnEntry.setStatus(_A)
_FsVoqWarnIfxId_Type=IfIndex
_FsVoqWarnIfxId_Object=MibTableColumn
fsVoqWarnIfxId=_FsVoqWarnIfxId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,1),_FsVoqWarnIfxId_Type())
fsVoqWarnIfxId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnIfxId.setStatus(_A)
_FsVoqWarnQueueId_Type=Integer32
_FsVoqWarnQueueId_Object=MibTableColumn
fsVoqWarnQueueId=_FsVoqWarnQueueId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,2),_FsVoqWarnQueueId_Type())
fsVoqWarnQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnQueueId.setStatus(_A)
_FsVoqWarnDevId_Type=Integer32
_FsVoqWarnDevId_Object=MibTableColumn
fsVoqWarnDevId=_FsVoqWarnDevId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,3),_FsVoqWarnDevId_Type())
fsVoqWarnDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnDevId.setStatus(_A)
_FsVoqWarnSlotId_Type=Integer32
_FsVoqWarnSlotId_Object=MibTableColumn
fsVoqWarnSlotId=_FsVoqWarnSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,4),_FsVoqWarnSlotId_Type())
fsVoqWarnSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnSlotId.setStatus(_A)
_FsVoqWarnPgId_Type=Integer32
_FsVoqWarnPgId_Object=MibTableColumn
fsVoqWarnPgId=_FsVoqWarnPgId_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,5),_FsVoqWarnPgId_Type())
fsVoqWarnPgId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnPgId.setStatus(_A)
_FsVoqWarnUsedcells_Type=Counter64
_FsVoqWarnUsedcells_Object=MibTableColumn
fsVoqWarnUsedcells=_FsVoqWarnUsedcells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,6),_FsVoqWarnUsedcells_Type())
fsVoqWarnUsedcells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnUsedcells.setStatus(_A)
_FsVoqWarnAvailablecells_Type=Counter64
_FsVoqWarnAvailablecells_Object=MibTableColumn
fsVoqWarnAvailablecells=_FsVoqWarnAvailablecells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,7),_FsVoqWarnAvailablecells_Type())
fsVoqWarnAvailablecells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnAvailablecells.setStatus(_A)
_FsVoqWarnTotalcells_Type=Counter64
_FsVoqWarnTotalcells_Object=MibTableColumn
fsVoqWarnTotalcells=_FsVoqWarnTotalcells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,8),_FsVoqWarnTotalcells_Type())
fsVoqWarnTotalcells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnTotalcells.setStatus(_A)
_FsVoqWarnUsage_Type=Counter64
_FsVoqWarnUsage_Object=MibTableColumn
fsVoqWarnUsage=_FsVoqWarnUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,9),_FsVoqWarnUsage_Type())
fsVoqWarnUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnUsage.setStatus(_A)
_FsVoqWarnUsagewarnlimit_Type=Counter64
_FsVoqWarnUsagewarnlimit_Object=MibTableColumn
fsVoqWarnUsagewarnlimit=_FsVoqWarnUsagewarnlimit_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,10),_FsVoqWarnUsagewarnlimit_Type())
fsVoqWarnUsagewarnlimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnUsagewarnlimit.setStatus(_A)
_FsVoqWarnUsagewarncount_Type=Counter64
_FsVoqWarnUsagewarncount_Object=MibTableColumn
fsVoqWarnUsagewarncount=_FsVoqWarnUsagewarncount_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,11),_FsVoqWarnUsagewarncount_Type())
fsVoqWarnUsagewarncount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnUsagewarncount.setStatus(_A)
_FsVoqWarnPeakedcells_Type=Counter64
_FsVoqWarnPeakedcells_Object=MibTableColumn
fsVoqWarnPeakedcells=_FsVoqWarnPeakedcells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,4,1,12),_FsVoqWarnPeakedcells_Type())
fsVoqWarnPeakedcells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVoqWarnPeakedcells.setStatus(_A)
_FsMmuIfQueueSupportTable_Object=MibTable
fsMmuIfQueueSupportTable=_FsMmuIfQueueSupportTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5))
if mibBuilder.loadTexts:fsMmuIfQueueSupportTable.setStatus(_A)
_FsMmuIfQueueSupportEntry_Object=MibTableRow
fsMmuIfQueueSupportEntry=_FsMmuIfQueueSupportEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1))
fsMmuIfQueueSupportEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:fsMmuIfQueueSupportEntry.setStatus(_A)
_FsMmuIfIndex_Type=IfIndex
_FsMmuIfIndex_Object=MibTableColumn
fsMmuIfIndex=_FsMmuIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,1),_FsMmuIfIndex_Type())
fsMmuIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfIndex.setStatus(_A)
_FsMmuIfQueueIndex_Type=Integer32
_FsMmuIfQueueIndex_Object=MibTableColumn
fsMmuIfQueueIndex=_FsMmuIfQueueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,2),_FsMmuIfQueueIndex_Type())
fsMmuIfQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueIndex.setStatus(_A)
_FsMmuIfSliceIndex_Type=Integer32
_FsMmuIfSliceIndex_Object=MibTableColumn
fsMmuIfSliceIndex=_FsMmuIfSliceIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,3),_FsMmuIfSliceIndex_Type())
fsMmuIfSliceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfSliceIndex.setStatus(_A)
_FsMmuIfQueueSupportUsedCells_Type=Counter64
_FsMmuIfQueueSupportUsedCells_Object=MibTableColumn
fsMmuIfQueueSupportUsedCells=_FsMmuIfQueueSupportUsedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,4),_FsMmuIfQueueSupportUsedCells_Type())
fsMmuIfQueueSupportUsedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportUsedCells.setStatus(_A)
_FsMmuIfQueueSupportAvailableCells_Type=Counter64
_FsMmuIfQueueSupportAvailableCells_Object=MibTableColumn
fsMmuIfQueueSupportAvailableCells=_FsMmuIfQueueSupportAvailableCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,5),_FsMmuIfQueueSupportAvailableCells_Type())
fsMmuIfQueueSupportAvailableCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportAvailableCells.setStatus(_A)
_FsMmuIfQueueSupportTotalCells_Type=Counter64
_FsMmuIfQueueSupportTotalCells_Object=MibTableColumn
fsMmuIfQueueSupportTotalCells=_FsMmuIfQueueSupportTotalCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,6),_FsMmuIfQueueSupportTotalCells_Type())
fsMmuIfQueueSupportTotalCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportTotalCells.setStatus(_A)
_FsMmuIfQueueSupportUsage_Type=Counter64
_FsMmuIfQueueSupportUsage_Object=MibTableColumn
fsMmuIfQueueSupportUsage=_FsMmuIfQueueSupportUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,7),_FsMmuIfQueueSupportUsage_Type())
fsMmuIfQueueSupportUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportUsage.setStatus(_A)
_FsMmuIfQueueSupportUsageWarnLimit_Type=Counter64
_FsMmuIfQueueSupportUsageWarnLimit_Object=MibTableColumn
fsMmuIfQueueSupportUsageWarnLimit=_FsMmuIfQueueSupportUsageWarnLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,8),_FsMmuIfQueueSupportUsageWarnLimit_Type())
fsMmuIfQueueSupportUsageWarnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportUsageWarnLimit.setStatus(_A)
_FsMmuIfQueueSupportUsageWarnCount_Type=Counter64
_FsMmuIfQueueSupportUsageWarnCount_Object=MibTableColumn
fsMmuIfQueueSupportUsageWarnCount=_FsMmuIfQueueSupportUsageWarnCount_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,9),_FsMmuIfQueueSupportUsageWarnCount_Type())
fsMmuIfQueueSupportUsageWarnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportUsageWarnCount.setStatus(_A)
_FsMmuIfQueueSupportPeakedCells_Type=Counter64
_FsMmuIfQueueSupportPeakedCells_Object=MibTableColumn
fsMmuIfQueueSupportPeakedCells=_FsMmuIfQueueSupportPeakedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,5,1,10),_FsMmuIfQueueSupportPeakedCells_Type())
fsMmuIfQueueSupportPeakedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfQueueSupportPeakedCells.setStatus(_A)
_FsMmuIfMulticastQueueSupportTable_Object=MibTable
fsMmuIfMulticastQueueSupportTable=_FsMmuIfMulticastQueueSupportTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6))
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportTable.setStatus(_A)
_FsMmuIfMulticastQueueSupportEntry_Object=MibTableRow
fsMmuIfMulticastQueueSupportEntry=_FsMmuIfMulticastQueueSupportEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1))
fsMmuIfMulticastQueueSupportEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportEntry.setStatus(_A)
_FsMmuIfIndexMulticast_Type=IfIndex
_FsMmuIfIndexMulticast_Object=MibTableColumn
fsMmuIfIndexMulticast=_FsMmuIfIndexMulticast_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,1),_FsMmuIfIndexMulticast_Type())
fsMmuIfIndexMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfIndexMulticast.setStatus(_A)
_FsMmuIfMulticastQueueIndex_Type=Integer32
_FsMmuIfMulticastQueueIndex_Object=MibTableColumn
fsMmuIfMulticastQueueIndex=_FsMmuIfMulticastQueueIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,2),_FsMmuIfMulticastQueueIndex_Type())
fsMmuIfMulticastQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueIndex.setStatus(_A)
_FsMmuIfSliceIndexMulticast_Type=Integer32
_FsMmuIfSliceIndexMulticast_Object=MibTableColumn
fsMmuIfSliceIndexMulticast=_FsMmuIfSliceIndexMulticast_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,3),_FsMmuIfSliceIndexMulticast_Type())
fsMmuIfSliceIndexMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfSliceIndexMulticast.setStatus(_A)
_FsMmuIfMulticastQueueSupportUsedCells_Type=Counter64
_FsMmuIfMulticastQueueSupportUsedCells_Object=MibTableColumn
fsMmuIfMulticastQueueSupportUsedCells=_FsMmuIfMulticastQueueSupportUsedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,4),_FsMmuIfMulticastQueueSupportUsedCells_Type())
fsMmuIfMulticastQueueSupportUsedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportUsedCells.setStatus(_A)
_FsMmuIfMulticastQueueSupportAvailableCells_Type=Counter64
_FsMmuIfMulticastQueueSupportAvailableCells_Object=MibTableColumn
fsMmuIfMulticastQueueSupportAvailableCells=_FsMmuIfMulticastQueueSupportAvailableCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,5),_FsMmuIfMulticastQueueSupportAvailableCells_Type())
fsMmuIfMulticastQueueSupportAvailableCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportAvailableCells.setStatus(_A)
_FsMmuIfMulticastQueueSupportTotalCells_Type=Counter64
_FsMmuIfMulticastQueueSupportTotalCells_Object=MibTableColumn
fsMmuIfMulticastQueueSupportTotalCells=_FsMmuIfMulticastQueueSupportTotalCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,6),_FsMmuIfMulticastQueueSupportTotalCells_Type())
fsMmuIfMulticastQueueSupportTotalCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportTotalCells.setStatus(_A)
_FsMmuIfMulticastQueueSupportUsage_Type=Counter64
_FsMmuIfMulticastQueueSupportUsage_Object=MibTableColumn
fsMmuIfMulticastQueueSupportUsage=_FsMmuIfMulticastQueueSupportUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,7),_FsMmuIfMulticastQueueSupportUsage_Type())
fsMmuIfMulticastQueueSupportUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportUsage.setStatus(_A)
_FsMmuIfMulticastQueueSupportUsageWarnLimit_Type=Counter64
_FsMmuIfMulticastQueueSupportUsageWarnLimit_Object=MibTableColumn
fsMmuIfMulticastQueueSupportUsageWarnLimit=_FsMmuIfMulticastQueueSupportUsageWarnLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,8),_FsMmuIfMulticastQueueSupportUsageWarnLimit_Type())
fsMmuIfMulticastQueueSupportUsageWarnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportUsageWarnLimit.setStatus(_A)
_FsMmuIfMulticastQueueSupportUsageWarnCount_Type=Counter64
_FsMmuIfMulticastQueueSupportUsageWarnCount_Object=MibTableColumn
fsMmuIfMulticastQueueSupportUsageWarnCount=_FsMmuIfMulticastQueueSupportUsageWarnCount_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,9),_FsMmuIfMulticastQueueSupportUsageWarnCount_Type())
fsMmuIfMulticastQueueSupportUsageWarnCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportUsageWarnCount.setStatus(_A)
_FsMmuIfMulticastQueueSupportPeakedCells_Type=Counter64
_FsMmuIfMulticastQueueSupportPeakedCells_Object=MibTableColumn
fsMmuIfMulticastQueueSupportPeakedCells=_FsMmuIfMulticastQueueSupportPeakedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,6,1,10),_FsMmuIfMulticastQueueSupportPeakedCells_Type())
fsMmuIfMulticastQueueSupportPeakedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfMulticastQueueSupportPeakedCells.setStatus(_A)
_FsMmuIfPriorityGroupSupportTable_Object=MibTable
fsMmuIfPriorityGroupSupportTable=_FsMmuIfPriorityGroupSupportTable_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7))
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportTable.setStatus(_A)
_FsMmuIfPriorityGroupSupportEntry_Object=MibTableRow
fsMmuIfPriorityGroupSupportEntry=_FsMmuIfPriorityGroupSupportEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1))
fsMmuIfPriorityGroupSupportEntry.setIndexNames((0,_C,_c),(0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportEntry.setStatus(_A)
_FsMmuIfIndexPriorityGroup_Type=IfIndex
_FsMmuIfIndexPriorityGroup_Object=MibTableColumn
fsMmuIfIndexPriorityGroup=_FsMmuIfIndexPriorityGroup_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,1),_FsMmuIfIndexPriorityGroup_Type())
fsMmuIfIndexPriorityGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfIndexPriorityGroup.setStatus(_A)
_FsMmuIfPriorityGroupIdIndex_Type=Integer32
_FsMmuIfPriorityGroupIdIndex_Object=MibTableColumn
fsMmuIfPriorityGroupIdIndex=_FsMmuIfPriorityGroupIdIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,2),_FsMmuIfPriorityGroupIdIndex_Type())
fsMmuIfPriorityGroupIdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupIdIndex.setStatus(_A)
_FsMmuIfSliceIndexPriorityGroup_Type=Integer32
_FsMmuIfSliceIndexPriorityGroup_Object=MibTableColumn
fsMmuIfSliceIndexPriorityGroup=_FsMmuIfSliceIndexPriorityGroup_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,3),_FsMmuIfSliceIndexPriorityGroup_Type())
fsMmuIfSliceIndexPriorityGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfSliceIndexPriorityGroup.setStatus(_A)
_FsMmuIfPriorityGroupSupportUsedCells_Type=Counter64
_FsMmuIfPriorityGroupSupportUsedCells_Object=MibTableColumn
fsMmuIfPriorityGroupSupportUsedCells=_FsMmuIfPriorityGroupSupportUsedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,4),_FsMmuIfPriorityGroupSupportUsedCells_Type())
fsMmuIfPriorityGroupSupportUsedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportUsedCells.setStatus(_A)
_FsMmuIfPriorityGroupSupportAvailableCells_Type=Counter64
_FsMmuIfPriorityGroupSupportAvailableCells_Object=MibTableColumn
fsMmuIfPriorityGroupSupportAvailableCells=_FsMmuIfPriorityGroupSupportAvailableCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,5),_FsMmuIfPriorityGroupSupportAvailableCells_Type())
fsMmuIfPriorityGroupSupportAvailableCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportAvailableCells.setStatus(_A)
_FsMmuIfPriorityGroupSupportTotalCells_Type=Counter64
_FsMmuIfPriorityGroupSupportTotalCells_Object=MibTableColumn
fsMmuIfPriorityGroupSupportTotalCells=_FsMmuIfPriorityGroupSupportTotalCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,6),_FsMmuIfPriorityGroupSupportTotalCells_Type())
fsMmuIfPriorityGroupSupportTotalCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportTotalCells.setStatus(_A)
_FsMmuIfPriorityGroupSupportUsage_Type=Counter64
_FsMmuIfPriorityGroupSupportUsage_Object=MibTableColumn
fsMmuIfPriorityGroupSupportUsage=_FsMmuIfPriorityGroupSupportUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,7),_FsMmuIfPriorityGroupSupportUsage_Type())
fsMmuIfPriorityGroupSupportUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportUsage.setStatus(_A)
_FsMmuIfPriorityGroupSupportPeakedCells_Type=Counter64
_FsMmuIfPriorityGroupSupportPeakedCells_Object=MibTableColumn
fsMmuIfPriorityGroupSupportPeakedCells=_FsMmuIfPriorityGroupSupportPeakedCells_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,8),_FsMmuIfPriorityGroupSupportPeakedCells_Type())
fsMmuIfPriorityGroupSupportPeakedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportPeakedCells.setStatus(_A)
_FsMmuIfPriorityGroupSupportUsedHeadroom_Type=Counter64
_FsMmuIfPriorityGroupSupportUsedHeadroom_Object=MibTableColumn
fsMmuIfPriorityGroupSupportUsedHeadroom=_FsMmuIfPriorityGroupSupportUsedHeadroom_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,9),_FsMmuIfPriorityGroupSupportUsedHeadroom_Type())
fsMmuIfPriorityGroupSupportUsedHeadroom.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportUsedHeadroom.setStatus(_A)
_FsMmuIfPriorityGroupSupportAvailableHeadroom_Type=Counter64
_FsMmuIfPriorityGroupSupportAvailableHeadroom_Object=MibTableColumn
fsMmuIfPriorityGroupSupportAvailableHeadroom=_FsMmuIfPriorityGroupSupportAvailableHeadroom_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,10),_FsMmuIfPriorityGroupSupportAvailableHeadroom_Type())
fsMmuIfPriorityGroupSupportAvailableHeadroom.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportAvailableHeadroom.setStatus(_A)
_FsMmuIfPriorityGroupSupportPeakedHeadroom_Type=Counter64
_FsMmuIfPriorityGroupSupportPeakedHeadroom_Object=MibTableColumn
fsMmuIfPriorityGroupSupportPeakedHeadroom=_FsMmuIfPriorityGroupSupportPeakedHeadroom_Object((1,3,6,1,4,1,52642,1,1,10,2,141,7,1,11),_FsMmuIfPriorityGroupSupportPeakedHeadroom_Type())
fsMmuIfPriorityGroupSupportPeakedHeadroom.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMmuIfPriorityGroupSupportPeakedHeadroom.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsMMUMIB':fsMMUMIB,'fsMmuIfVoqInTable':fsMmuIfVoqInTable,'fsMmuIfVoqInEntry':fsMmuIfVoqInEntry,_D:fsInIfxId,_E:fsInQueueId,_F:fsInDevId,_G:fsInSlotId,_H:fsInPgId,'fsInTransmitPackets':fsInTransmitPackets,'fsInTransmitBytes':fsInTransmitBytes,'fsInDropPackets':fsInDropPackets,'fsInDropBytes':fsInDropBytes,'fsMmuIfVoqOutTable':fsMmuIfVoqOutTable,'fsMmuIfVoqOutEntry':fsMmuIfVoqOutEntry,_I:fsOutIfxId,_J:fsOutQueueId,_K:fsOutDevId,_L:fsOutSlotId,_M:fsOutPgId,'fsOutTransmitPackets':fsOutTransmitPackets,'fsOutTransmitBytes':fsOutTransmitBytes,'fsOutDropPackets':fsOutDropPackets,'fsOutDropBytes':fsOutDropBytes,'fsMmuIfWarnTable':fsMmuIfWarnTable,'fsMmuIfWarnEntry':fsMmuIfWarnEntry,_N:fsWarnIfxId,_O:fsWarnDevId,_P:fsWarnSlotId,_Q:fsWarnPgId,'fsWarnUsedCell':fsWarnUsedCell,'fsWarnTotalCell':fsWarnTotalCell,'fsWarnLimit':fsWarnLimit,'fsWarnCount':fsWarnCount,'fsMmuIfVoqWarnTable':fsMmuIfVoqWarnTable,'fsMmuIfVoqWarnEntry':fsMmuIfVoqWarnEntry,_R:fsVoqWarnIfxId,_S:fsVoqWarnQueueId,_T:fsVoqWarnDevId,_U:fsVoqWarnSlotId,_V:fsVoqWarnPgId,'fsVoqWarnUsedcells':fsVoqWarnUsedcells,'fsVoqWarnAvailablecells':fsVoqWarnAvailablecells,'fsVoqWarnTotalcells':fsVoqWarnTotalcells,'fsVoqWarnUsage':fsVoqWarnUsage,'fsVoqWarnUsagewarnlimit':fsVoqWarnUsagewarnlimit,'fsVoqWarnUsagewarncount':fsVoqWarnUsagewarncount,'fsVoqWarnPeakedcells':fsVoqWarnPeakedcells,'fsMmuIfQueueSupportTable':fsMmuIfQueueSupportTable,'fsMmuIfQueueSupportEntry':fsMmuIfQueueSupportEntry,_W:fsMmuIfIndex,_X:fsMmuIfQueueIndex,_Y:fsMmuIfSliceIndex,'fsMmuIfQueueSupportUsedCells':fsMmuIfQueueSupportUsedCells,'fsMmuIfQueueSupportAvailableCells':fsMmuIfQueueSupportAvailableCells,'fsMmuIfQueueSupportTotalCells':fsMmuIfQueueSupportTotalCells,'fsMmuIfQueueSupportUsage':fsMmuIfQueueSupportUsage,'fsMmuIfQueueSupportUsageWarnLimit':fsMmuIfQueueSupportUsageWarnLimit,'fsMmuIfQueueSupportUsageWarnCount':fsMmuIfQueueSupportUsageWarnCount,'fsMmuIfQueueSupportPeakedCells':fsMmuIfQueueSupportPeakedCells,'fsMmuIfMulticastQueueSupportTable':fsMmuIfMulticastQueueSupportTable,'fsMmuIfMulticastQueueSupportEntry':fsMmuIfMulticastQueueSupportEntry,_Z:fsMmuIfIndexMulticast,_a:fsMmuIfMulticastQueueIndex,_b:fsMmuIfSliceIndexMulticast,'fsMmuIfMulticastQueueSupportUsedCells':fsMmuIfMulticastQueueSupportUsedCells,'fsMmuIfMulticastQueueSupportAvailableCells':fsMmuIfMulticastQueueSupportAvailableCells,'fsMmuIfMulticastQueueSupportTotalCells':fsMmuIfMulticastQueueSupportTotalCells,'fsMmuIfMulticastQueueSupportUsage':fsMmuIfMulticastQueueSupportUsage,'fsMmuIfMulticastQueueSupportUsageWarnLimit':fsMmuIfMulticastQueueSupportUsageWarnLimit,'fsMmuIfMulticastQueueSupportUsageWarnCount':fsMmuIfMulticastQueueSupportUsageWarnCount,'fsMmuIfMulticastQueueSupportPeakedCells':fsMmuIfMulticastQueueSupportPeakedCells,'fsMmuIfPriorityGroupSupportTable':fsMmuIfPriorityGroupSupportTable,'fsMmuIfPriorityGroupSupportEntry':fsMmuIfPriorityGroupSupportEntry,_c:fsMmuIfIndexPriorityGroup,_d:fsMmuIfPriorityGroupIdIndex,_e:fsMmuIfSliceIndexPriorityGroup,'fsMmuIfPriorityGroupSupportUsedCells':fsMmuIfPriorityGroupSupportUsedCells,'fsMmuIfPriorityGroupSupportAvailableCells':fsMmuIfPriorityGroupSupportAvailableCells,'fsMmuIfPriorityGroupSupportTotalCells':fsMmuIfPriorityGroupSupportTotalCells,'fsMmuIfPriorityGroupSupportUsage':fsMmuIfPriorityGroupSupportUsage,'fsMmuIfPriorityGroupSupportPeakedCells':fsMmuIfPriorityGroupSupportPeakedCells,'fsMmuIfPriorityGroupSupportUsedHeadroom':fsMmuIfPriorityGroupSupportUsedHeadroom,'fsMmuIfPriorityGroupSupportAvailableHeadroom':fsMmuIfPriorityGroupSupportAvailableHeadroom,'fsMmuIfPriorityGroupSupportPeakedHeadroom':fsMmuIfPriorityGroupSupportPeakedHeadroom})