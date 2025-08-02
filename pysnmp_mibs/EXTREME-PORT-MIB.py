_Z='extremePortMauRestrict'
_Y='extremePortMauStatus'
_X='extremePortMauType'
_W='extremePortQosIngress'
_V='extremeWiredClientID'
_U='extremePortIngressStatsQueueIndex'
_T='not-accessible'
_S='extremePortLoadshare2SlaveIfIndex'
_R='extremePortLoadshare2MasterIfIndex'
_Q='summitlinkOnly'
_P='ethernetOnly'
_O='extremePortLoadshareSlaveIfIndex'
_N='extremePortLoadshareMasterIfIndex'
_M='Unsigned32'
_L='extremeVlanIfIndex'
_K='EXTREME-VLAN-MIB'
_J='DisplayString'
_I='read-write'
_H='read-create'
_G='EXTREME-PORT-MIB'
_F='deprecated'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ClientAuthType,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','ClientAuthType','extremeAgent')
extremeVlanIfIndex,=mibBuilder.importSymbols(_K,_L)
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention')
extremePort=ModuleIdentity((1,3,6,1,4,1,1916,1,4))
if mibBuilder.loadTexts:extremePort.setRevisions(('2019-03-21 01:00','2018-03-13 00:00'))
class ExtremePortTrafficDirection(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_ExtremePortLoadshareTable_Object=MibTable
extremePortLoadshareTable=_ExtremePortLoadshareTable_Object((1,3,6,1,4,1,1916,1,4,1))
if mibBuilder.loadTexts:extremePortLoadshareTable.setStatus(_F)
_ExtremePortLoadshareEntry_Object=MibTableRow
extremePortLoadshareEntry=_ExtremePortLoadshareEntry_Object((1,3,6,1,4,1,1916,1,4,1,1))
extremePortLoadshareEntry.setIndexNames((0,_G,_N),(0,_G,_O))
if mibBuilder.loadTexts:extremePortLoadshareEntry.setStatus(_F)
class _ExtremePortLoadshareMasterIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremePortLoadshareMasterIfIndex_Type.__name__=_C
_ExtremePortLoadshareMasterIfIndex_Object=MibTableColumn
extremePortLoadshareMasterIfIndex=_ExtremePortLoadshareMasterIfIndex_Object((1,3,6,1,4,1,1916,1,4,1,1,1),_ExtremePortLoadshareMasterIfIndex_Type())
extremePortLoadshareMasterIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshareMasterIfIndex.setStatus(_F)
class _ExtremePortLoadshareSlaveIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremePortLoadshareSlaveIfIndex_Type.__name__=_C
_ExtremePortLoadshareSlaveIfIndex_Object=MibTableColumn
extremePortLoadshareSlaveIfIndex=_ExtremePortLoadshareSlaveIfIndex_Object((1,3,6,1,4,1,1916,1,4,1,1,2),_ExtremePortLoadshareSlaveIfIndex_Type())
extremePortLoadshareSlaveIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshareSlaveIfIndex.setStatus(_F)
class _ExtremePortLoadshareGrouping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('other',1),('pair',2),('quad',4)))
_ExtremePortLoadshareGrouping_Type.__name__=_C
_ExtremePortLoadshareGrouping_Object=MibTableColumn
extremePortLoadshareGrouping=_ExtremePortLoadshareGrouping_Object((1,3,6,1,4,1,1916,1,4,1,1,3),_ExtremePortLoadshareGrouping_Type())
extremePortLoadshareGrouping.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshareGrouping.setStatus(_F)
_ExtremePortLoadshareStatus_Type=RowStatus
_ExtremePortLoadshareStatus_Object=MibTableColumn
extremePortLoadshareStatus=_ExtremePortLoadshareStatus_Object((1,3,6,1,4,1,1916,1,4,1,1,4),_ExtremePortLoadshareStatus_Type())
extremePortLoadshareStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshareStatus.setStatus(_F)
_ExtremePortSummitlinkTable_Object=MibTable
extremePortSummitlinkTable=_ExtremePortSummitlinkTable_Object((1,3,6,1,4,1,1916,1,4,2))
if mibBuilder.loadTexts:extremePortSummitlinkTable.setStatus(_F)
_ExtremePortSummitlinkEntry_Object=MibTableRow
extremePortSummitlinkEntry=_ExtremePortSummitlinkEntry_Object((1,3,6,1,4,1,1916,1,4,2,1))
extremePortSummitlinkEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortSummitlinkEntry.setStatus(_F)
class _ExtremePortSummitlinkAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ExtremePortSummitlinkAdminMode_Type.__name__=_C
_ExtremePortSummitlinkAdminMode_Object=MibTableColumn
extremePortSummitlinkAdminMode=_ExtremePortSummitlinkAdminMode_Object((1,3,6,1,4,1,1916,1,4,2,1,1),_ExtremePortSummitlinkAdminMode_Type())
extremePortSummitlinkAdminMode.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortSummitlinkAdminMode.setStatus(_F)
class _ExtremePortSummitlinkOperMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_ExtremePortSummitlinkOperMode_Type.__name__=_C
_ExtremePortSummitlinkOperMode_Object=MibTableColumn
extremePortSummitlinkOperMode=_ExtremePortSummitlinkOperMode_Object((1,3,6,1,4,1,1916,1,4,2,1,2),_ExtremePortSummitlinkOperMode_Type())
extremePortSummitlinkOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortSummitlinkOperMode.setStatus(_F)
class _ExtremePortSummitlinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ExtremePortSummitlinkState_Type.__name__=_C
_ExtremePortSummitlinkState_Object=MibTableColumn
extremePortSummitlinkState=_ExtremePortSummitlinkState_Object((1,3,6,1,4,1,1916,1,4,2,1,3),_ExtremePortSummitlinkState_Type())
extremePortSummitlinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortSummitlinkState.setStatus(_F)
class _ExtremePortSummitlinkRejectReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('other',2),('stackMisconnected',3)))
_ExtremePortSummitlinkRejectReason_Type.__name__=_C
_ExtremePortSummitlinkRejectReason_Object=MibTableColumn
extremePortSummitlinkRejectReason=_ExtremePortSummitlinkRejectReason_Object((1,3,6,1,4,1,1916,1,4,2,1,4),_ExtremePortSummitlinkRejectReason_Type())
extremePortSummitlinkRejectReason.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortSummitlinkRejectReason.setStatus(_F)
_ExtremePortLoadshare2Table_Object=MibTable
extremePortLoadshare2Table=_ExtremePortLoadshare2Table_Object((1,3,6,1,4,1,1916,1,4,3))
if mibBuilder.loadTexts:extremePortLoadshare2Table.setStatus(_A)
_ExtremePortLoadshare2Entry_Object=MibTableRow
extremePortLoadshare2Entry=_ExtremePortLoadshare2Entry_Object((1,3,6,1,4,1,1916,1,4,3,1))
extremePortLoadshare2Entry.setIndexNames((0,_G,_R),(0,_G,_S))
if mibBuilder.loadTexts:extremePortLoadshare2Entry.setStatus(_A)
class _ExtremePortLoadshare2MasterIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremePortLoadshare2MasterIfIndex_Type.__name__=_C
_ExtremePortLoadshare2MasterIfIndex_Object=MibTableColumn
extremePortLoadshare2MasterIfIndex=_ExtremePortLoadshare2MasterIfIndex_Object((1,3,6,1,4,1,1916,1,4,3,1,1),_ExtremePortLoadshare2MasterIfIndex_Type())
extremePortLoadshare2MasterIfIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:extremePortLoadshare2MasterIfIndex.setStatus(_A)
class _ExtremePortLoadshare2SlaveIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremePortLoadshare2SlaveIfIndex_Type.__name__=_C
_ExtremePortLoadshare2SlaveIfIndex_Object=MibTableColumn
extremePortLoadshare2SlaveIfIndex=_ExtremePortLoadshare2SlaveIfIndex_Object((1,3,6,1,4,1,1916,1,4,3,1,2),_ExtremePortLoadshare2SlaveIfIndex_Type())
extremePortLoadshare2SlaveIfIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:extremePortLoadshare2SlaveIfIndex.setStatus(_A)
class _ExtremePortLoadshare2Algorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ingressPortOffset',1),('hash',2),('roundRobin',3),('l2Address',4),('l3Address',5),('l3l4Address',6),('customAddress',7)))
_ExtremePortLoadshare2Algorithm_Type.__name__=_C
_ExtremePortLoadshare2Algorithm_Object=MibTableColumn
extremePortLoadshare2Algorithm=_ExtremePortLoadshare2Algorithm_Object((1,3,6,1,4,1,1916,1,4,3,1,3),_ExtremePortLoadshare2Algorithm_Type())
extremePortLoadshare2Algorithm.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshare2Algorithm.setStatus(_A)
_ExtremePortLoadshare2Status_Type=RowStatus
_ExtremePortLoadshare2Status_Object=MibTableColumn
extremePortLoadshare2Status=_ExtremePortLoadshare2Status_Object((1,3,6,1,4,1,1916,1,4,3,1,4),_ExtremePortLoadshare2Status_Type())
extremePortLoadshare2Status.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshare2Status.setStatus(_A)
class _ExtremePortLoadshare2MinActiveLinks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremePortLoadshare2MinActiveLinks_Type.__name__=_M
_ExtremePortLoadshare2MinActiveLinks_Object=MibTableColumn
extremePortLoadshare2MinActiveLinks=_ExtremePortLoadshare2MinActiveLinks_Object((1,3,6,1,4,1,1916,1,4,3,1,5),_ExtremePortLoadshare2MinActiveLinks_Type())
extremePortLoadshare2MinActiveLinks.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshare2MinActiveLinks.setStatus(_A)
class _ExtremePortLoadshare2AggControlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('lacp',2),('healthcheck',3)))
_ExtremePortLoadshare2AggControlType_Type.__name__=_C
_ExtremePortLoadshare2AggControlType_Object=MibTableColumn
extremePortLoadshare2AggControlType=_ExtremePortLoadshare2AggControlType_Object((1,3,6,1,4,1,1916,1,4,3,1,6),_ExtremePortLoadshare2AggControlType_Type())
extremePortLoadshare2AggControlType.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortLoadshare2AggControlType.setStatus(_A)
_ExtremePortRateShapeTable_Object=MibTable
extremePortRateShapeTable=_ExtremePortRateShapeTable_Object((1,3,6,1,4,1,1916,1,4,4))
if mibBuilder.loadTexts:extremePortRateShapeTable.setStatus(_A)
_ExtremePortRateShapeEntry_Object=MibTableRow
extremePortRateShapeEntry=_ExtremePortRateShapeEntry_Object((1,3,6,1,4,1,1916,1,4,4,1))
extremePortRateShapeEntry.setIndexNames((0,_D,_E),(0,_K,_L))
if mibBuilder.loadTexts:extremePortRateShapeEntry.setStatus(_A)
class _ExtremePortRateShapePortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rateLimited',1),('loopBack',2)))
_ExtremePortRateShapePortType_Type.__name__=_C
_ExtremePortRateShapePortType_Object=MibTableColumn
extremePortRateShapePortType=_ExtremePortRateShapePortType_Object((1,3,6,1,4,1,1916,1,4,4,1,1),_ExtremePortRateShapePortType_Type())
extremePortRateShapePortType.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortRateShapePortType.setStatus(_A)
class _ExtremePortRateShapeLoopbackTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_ExtremePortRateShapeLoopbackTag_Type.__name__=_C
_ExtremePortRateShapeLoopbackTag_Object=MibTableColumn
extremePortRateShapeLoopbackTag=_ExtremePortRateShapeLoopbackTag_Object((1,3,6,1,4,1,1916,1,4,4,1,2),_ExtremePortRateShapeLoopbackTag_Type())
extremePortRateShapeLoopbackTag.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortRateShapeLoopbackTag.setStatus(_A)
_ExtremePortRateShapeStatus_Type=RowStatus
_ExtremePortRateShapeStatus_Object=MibTableColumn
extremePortRateShapeStatus=_ExtremePortRateShapeStatus_Object((1,3,6,1,4,1,1916,1,4,4,1,3),_ExtremePortRateShapeStatus_Type())
extremePortRateShapeStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremePortRateShapeStatus.setStatus(_A)
_ExtremePortUtilizationTable_Object=MibTable
extremePortUtilizationTable=_ExtremePortUtilizationTable_Object((1,3,6,1,4,1,1916,1,4,5))
if mibBuilder.loadTexts:extremePortUtilizationTable.setStatus(_A)
_ExtremePortUtilizationEntry_Object=MibTableRow
extremePortUtilizationEntry=_ExtremePortUtilizationEntry_Object((1,3,6,1,4,1,1916,1,4,5,1))
extremePortUtilizationEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortUtilizationEntry.setStatus(_A)
_ExtremePortUtilizationAvgTxBw_Type=Integer32
_ExtremePortUtilizationAvgTxBw_Object=MibTableColumn
extremePortUtilizationAvgTxBw=_ExtremePortUtilizationAvgTxBw_Object((1,3,6,1,4,1,1916,1,4,5,1,1),_ExtremePortUtilizationAvgTxBw_Type())
extremePortUtilizationAvgTxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgTxBw.setStatus(_A)
_ExtremePortUtilizationAvgRxBw_Type=Integer32
_ExtremePortUtilizationAvgRxBw_Object=MibTableColumn
extremePortUtilizationAvgRxBw=_ExtremePortUtilizationAvgRxBw_Object((1,3,6,1,4,1,1916,1,4,5,1,2),_ExtremePortUtilizationAvgRxBw_Type())
extremePortUtilizationAvgRxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgRxBw.setStatus(_A)
_ExtremePortUtilizationPeakTxBw_Type=Integer32
_ExtremePortUtilizationPeakTxBw_Object=MibTableColumn
extremePortUtilizationPeakTxBw=_ExtremePortUtilizationPeakTxBw_Object((1,3,6,1,4,1,1916,1,4,5,1,3),_ExtremePortUtilizationPeakTxBw_Type())
extremePortUtilizationPeakTxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakTxBw.setStatus(_A)
_ExtremePortUtilizationPeakRxBw_Type=Integer32
_ExtremePortUtilizationPeakRxBw_Object=MibTableColumn
extremePortUtilizationPeakRxBw=_ExtremePortUtilizationPeakRxBw_Object((1,3,6,1,4,1,1916,1,4,5,1,4),_ExtremePortUtilizationPeakRxBw_Type())
extremePortUtilizationPeakRxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakRxBw.setStatus(_A)
_ExtremePortInfoTable_Object=MibTable
extremePortInfoTable=_ExtremePortInfoTable_Object((1,3,6,1,4,1,1916,1,4,6))
if mibBuilder.loadTexts:extremePortInfoTable.setStatus(_A)
_ExtremePortInfoEntry_Object=MibTableRow
extremePortInfoEntry=_ExtremePortInfoEntry_Object((1,3,6,1,4,1,1916,1,4,6,1))
extremePortInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortInfoEntry.setStatus(_A)
_ExtremePortInfoFilterUpCounter_Type=Counter32
_ExtremePortInfoFilterUpCounter_Object=MibTableColumn
extremePortInfoFilterUpCounter=_ExtremePortInfoFilterUpCounter_Object((1,3,6,1,4,1,1916,1,4,6,1,1),_ExtremePortInfoFilterUpCounter_Type())
extremePortInfoFilterUpCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortInfoFilterUpCounter.setStatus(_A)
_ExtremePortInfoFilterDownCounter_Type=Counter32
_ExtremePortInfoFilterDownCounter_Object=MibTableColumn
extremePortInfoFilterDownCounter=_ExtremePortInfoFilterDownCounter_Object((1,3,6,1,4,1,1916,1,4,6,1,2),_ExtremePortInfoFilterDownCounter_Type())
extremePortInfoFilterDownCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortInfoFilterDownCounter.setStatus(_A)
_ExtremePortXenpakVendorTable_Object=MibTable
extremePortXenpakVendorTable=_ExtremePortXenpakVendorTable_Object((1,3,6,1,4,1,1916,1,4,7))
if mibBuilder.loadTexts:extremePortXenpakVendorTable.setStatus(_A)
_ExtremePortXenpakVendorEntry_Object=MibTableRow
extremePortXenpakVendorEntry=_ExtremePortXenpakVendorEntry_Object((1,3,6,1,4,1,1916,1,4,7,1))
extremePortXenpakVendorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortXenpakVendorEntry.setStatus(_A)
class _ExtremePortXenpakVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_ExtremePortXenpakVendorName_Type.__name__=_J
_ExtremePortXenpakVendorName_Object=MibTableColumn
extremePortXenpakVendorName=_ExtremePortXenpakVendorName_Object((1,3,6,1,4,1,1916,1,4,7,1,1),_ExtremePortXenpakVendorName_Type())
extremePortXenpakVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortXenpakVendorName.setStatus(_A)
_ExtremePortIngressStats_ObjectIdentity=ObjectIdentity
extremePortIngressStats=_ExtremePortIngressStats_ObjectIdentity((1,3,6,1,4,1,1916,1,4,8))
_ExtremePortIngressStatsPortTable_Object=MibTable
extremePortIngressStatsPortTable=_ExtremePortIngressStatsPortTable_Object((1,3,6,1,4,1,1916,1,4,8,1))
if mibBuilder.loadTexts:extremePortIngressStatsPortTable.setStatus(_A)
_ExtremePortIngressPortStatsEntry_Object=MibTableRow
extremePortIngressPortStatsEntry=_ExtremePortIngressPortStatsEntry_Object((1,3,6,1,4,1,1916,1,4,8,1,1))
extremePortIngressPortStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortIngressPortStatsEntry.setStatus(_A)
class _ExtremePortIngressStatsLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('active',2),('disabled',3),('notPresent',4)))
_ExtremePortIngressStatsLinkStatus_Type.__name__=_C
_ExtremePortIngressStatsLinkStatus_Object=MibTableColumn
extremePortIngressStatsLinkStatus=_ExtremePortIngressStatsLinkStatus_Object((1,3,6,1,4,1,1916,1,4,8,1,1,1),_ExtremePortIngressStatsLinkStatus_Type())
extremePortIngressStatsLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsLinkStatus.setStatus(_A)
_ExtremePortIngressStatsPortHighPriBytes_Type=Counter64
_ExtremePortIngressStatsPortHighPriBytes_Object=MibTableColumn
extremePortIngressStatsPortHighPriBytes=_ExtremePortIngressStatsPortHighPriBytes_Object((1,3,6,1,4,1,1916,1,4,8,1,1,2),_ExtremePortIngressStatsPortHighPriBytes_Type())
extremePortIngressStatsPortHighPriBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsPortHighPriBytes.setStatus(_A)
_ExtremePortIngressStatsPortLowPriBytes_Type=Counter64
_ExtremePortIngressStatsPortLowPriBytes_Object=MibTableColumn
extremePortIngressStatsPortLowPriBytes=_ExtremePortIngressStatsPortLowPriBytes_Object((1,3,6,1,4,1,1916,1,4,8,1,1,3),_ExtremePortIngressStatsPortLowPriBytes_Type())
extremePortIngressStatsPortLowPriBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsPortLowPriBytes.setStatus(_A)
_ExtremePortIngressStatsPortDroppedBytes_Type=Counter64
_ExtremePortIngressStatsPortDroppedBytes_Object=MibTableColumn
extremePortIngressStatsPortDroppedBytes=_ExtremePortIngressStatsPortDroppedBytes_Object((1,3,6,1,4,1,1916,1,4,8,1,1,4),_ExtremePortIngressStatsPortDroppedBytes_Type())
extremePortIngressStatsPortDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsPortDroppedBytes.setStatus(_A)
_ExtremePortIngressStatsTxXoff_Type=Counter64
_ExtremePortIngressStatsTxXoff_Object=MibTableColumn
extremePortIngressStatsTxXoff=_ExtremePortIngressStatsTxXoff_Object((1,3,6,1,4,1,1916,1,4,8,1,1,5),_ExtremePortIngressStatsTxXoff_Type())
extremePortIngressStatsTxXoff.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsTxXoff.setStatus(_A)
_ExtremePortIngressStatsQueueTable_Object=MibTable
extremePortIngressStatsQueueTable=_ExtremePortIngressStatsQueueTable_Object((1,3,6,1,4,1,1916,1,4,8,2))
if mibBuilder.loadTexts:extremePortIngressStatsQueueTable.setStatus(_A)
_ExtremePortIngressQueueStatsEntry_Object=MibTableRow
extremePortIngressQueueStatsEntry=_ExtremePortIngressQueueStatsEntry_Object((1,3,6,1,4,1,1916,1,4,8,2,1))
extremePortIngressQueueStatsEntry.setIndexNames((0,_D,_E),(0,_G,_U))
if mibBuilder.loadTexts:extremePortIngressQueueStatsEntry.setStatus(_A)
_ExtremePortIngressStatsQueueIndex_Type=Integer32
_ExtremePortIngressStatsQueueIndex_Object=MibTableColumn
extremePortIngressStatsQueueIndex=_ExtremePortIngressStatsQueueIndex_Object((1,3,6,1,4,1,1916,1,4,8,2,1,1),_ExtremePortIngressStatsQueueIndex_Type())
extremePortIngressStatsQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsQueueIndex.setStatus(_A)
_ExtremePortIngressStatsQueueHighPriBytes_Type=Counter64
_ExtremePortIngressStatsQueueHighPriBytes_Object=MibTableColumn
extremePortIngressStatsQueueHighPriBytes=_ExtremePortIngressStatsQueueHighPriBytes_Object((1,3,6,1,4,1,1916,1,4,8,2,1,2),_ExtremePortIngressStatsQueueHighPriBytes_Type())
extremePortIngressStatsQueueHighPriBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsQueueHighPriBytes.setStatus(_A)
_ExtremePortIngressStatsQueueLowPriBytes_Type=Counter64
_ExtremePortIngressStatsQueueLowPriBytes_Object=MibTableColumn
extremePortIngressStatsQueueLowPriBytes=_ExtremePortIngressStatsQueueLowPriBytes_Object((1,3,6,1,4,1,1916,1,4,8,2,1,3),_ExtremePortIngressStatsQueueLowPriBytes_Type())
extremePortIngressStatsQueueLowPriBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsQueueLowPriBytes.setStatus(_A)
_ExtremePortIngressStatsQueuePercentDropped_Type=Integer32
_ExtremePortIngressStatsQueuePercentDropped_Object=MibTableColumn
extremePortIngressStatsQueuePercentDropped=_ExtremePortIngressStatsQueuePercentDropped_Object((1,3,6,1,4,1,1916,1,4,8,2,1,4),_ExtremePortIngressStatsQueuePercentDropped_Type())
extremePortIngressStatsQueuePercentDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortIngressStatsQueuePercentDropped.setStatus(_A)
_ExtremePortEgressRateLimitTable_Object=MibTable
extremePortEgressRateLimitTable=_ExtremePortEgressRateLimitTable_Object((1,3,6,1,4,1,1916,1,4,9))
if mibBuilder.loadTexts:extremePortEgressRateLimitTable.setStatus(_A)
_ExtremePortEgressRateLimitEntry_Object=MibTableRow
extremePortEgressRateLimitEntry=_ExtremePortEgressRateLimitEntry_Object((1,3,6,1,4,1,1916,1,4,9,1))
extremePortEgressRateLimitEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortEgressRateLimitEntry.setStatus(_A)
class _ExtremePortEgressRateLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('percentage',1),('kbps',2),('mbps',3)))
_ExtremePortEgressRateLimitType_Type.__name__=_C
_ExtremePortEgressRateLimitType_Object=MibTableColumn
extremePortEgressRateLimitType=_ExtremePortEgressRateLimitType_Object((1,3,6,1,4,1,1916,1,4,9,1,1),_ExtremePortEgressRateLimitType_Type())
extremePortEgressRateLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortEgressRateLimitType.setStatus(_A)
_ExtremePortEgressRateLimitValue_Type=Integer32
_ExtremePortEgressRateLimitValue_Object=MibTableColumn
extremePortEgressRateLimitValue=_ExtremePortEgressRateLimitValue_Object((1,3,6,1,4,1,1916,1,4,9,1,2),_ExtremePortEgressRateLimitValue_Type())
extremePortEgressRateLimitValue.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortEgressRateLimitValue.setStatus(_A)
_ExtremeWiredClientTable_Object=MibTable
extremeWiredClientTable=_ExtremeWiredClientTable_Object((1,3,6,1,4,1,1916,1,4,10))
if mibBuilder.loadTexts:extremeWiredClientTable.setStatus(_A)
_ExtremeWiredClientEntry_Object=MibTableRow
extremeWiredClientEntry=_ExtremeWiredClientEntry_Object((1,3,6,1,4,1,1916,1,4,10,1))
extremeWiredClientEntry.setIndexNames((0,_D,_E),(0,_G,_V))
if mibBuilder.loadTexts:extremeWiredClientEntry.setStatus(_A)
_ExtremeWiredClientID_Type=MacAddress
_ExtremeWiredClientID_Object=MibTableColumn
extremeWiredClientID=_ExtremeWiredClientID_Object((1,3,6,1,4,1,1916,1,4,10,1,1),_ExtremeWiredClientID_Type())
extremeWiredClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientID.setStatus(_A)
class _ExtremeWiredClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authenticated',1),('unauthenticated',2)))
_ExtremeWiredClientState_Type.__name__=_C
_ExtremeWiredClientState_Object=MibTableColumn
extremeWiredClientState=_ExtremeWiredClientState_Object((1,3,6,1,4,1,1916,1,4,10,1,2),_ExtremeWiredClientState_Type())
extremeWiredClientState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientState.setStatus(_A)
_ExtremeWiredClientVLAN_Type=Integer32
_ExtremeWiredClientVLAN_Object=MibTableColumn
extremeWiredClientVLAN=_ExtremeWiredClientVLAN_Object((1,3,6,1,4,1,1916,1,4,10,1,3),_ExtremeWiredClientVLAN_Type())
extremeWiredClientVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientVLAN.setStatus(_A)
_ExtremeWiredClientPriority_Type=Integer32
_ExtremeWiredClientPriority_Object=MibTableColumn
extremeWiredClientPriority=_ExtremeWiredClientPriority_Object((1,3,6,1,4,1,1916,1,4,10,1,4),_ExtremeWiredClientPriority_Type())
extremeWiredClientPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientPriority.setStatus(_A)
_ExtremeWiredClientAuthType_Type=ClientAuthType
_ExtremeWiredClientAuthType_Object=MibTableColumn
extremeWiredClientAuthType=_ExtremeWiredClientAuthType_Object((1,3,6,1,4,1,1916,1,4,10,1,5),_ExtremeWiredClientAuthType_Type())
extremeWiredClientAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientAuthType.setStatus(_A)
_ExtremeWiredClientLastStateChangeTime_Type=TimeTicks
_ExtremeWiredClientLastStateChangeTime_Object=MibTableColumn
extremeWiredClientLastStateChangeTime=_ExtremeWiredClientLastStateChangeTime_Object((1,3,6,1,4,1,1916,1,4,10,1,6),_ExtremeWiredClientLastStateChangeTime_Type())
extremeWiredClientLastStateChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientLastStateChangeTime.setStatus(_A)
_ExtremeWiredClientIP_Type=IpAddress
_ExtremeWiredClientIP_Object=MibTableColumn
extremeWiredClientIP=_ExtremeWiredClientIP_Object((1,3,6,1,4,1,1916,1,4,10,1,7),_ExtremeWiredClientIP_Type())
extremeWiredClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeWiredClientIP.setStatus(_A)
_ExtremePortUtilizationExtnTable_Object=MibTable
extremePortUtilizationExtnTable=_ExtremePortUtilizationExtnTable_Object((1,3,6,1,4,1,1916,1,4,11))
if mibBuilder.loadTexts:extremePortUtilizationExtnTable.setStatus(_A)
_ExtremePortUtilizationExtnEntry_Object=MibTableRow
extremePortUtilizationExtnEntry=_ExtremePortUtilizationExtnEntry_Object((1,3,6,1,4,1,1916,1,4,11,1))
extremePortUtilizationExtnEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortUtilizationExtnEntry.setStatus(_A)
_ExtremePortUtilizationAvgTxPkts_Type=Integer32
_ExtremePortUtilizationAvgTxPkts_Object=MibTableColumn
extremePortUtilizationAvgTxPkts=_ExtremePortUtilizationAvgTxPkts_Object((1,3,6,1,4,1,1916,1,4,11,1,1),_ExtremePortUtilizationAvgTxPkts_Type())
extremePortUtilizationAvgTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgTxPkts.setStatus(_A)
_ExtremePortUtilizationAvgRxPkts_Type=Integer32
_ExtremePortUtilizationAvgRxPkts_Object=MibTableColumn
extremePortUtilizationAvgRxPkts=_ExtremePortUtilizationAvgRxPkts_Object((1,3,6,1,4,1,1916,1,4,11,1,2),_ExtremePortUtilizationAvgRxPkts_Type())
extremePortUtilizationAvgRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgRxPkts.setStatus(_A)
_ExtremePortUtilizationPeakTxPkts_Type=Integer32
_ExtremePortUtilizationPeakTxPkts_Object=MibTableColumn
extremePortUtilizationPeakTxPkts=_ExtremePortUtilizationPeakTxPkts_Object((1,3,6,1,4,1,1916,1,4,11,1,3),_ExtremePortUtilizationPeakTxPkts_Type())
extremePortUtilizationPeakTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakTxPkts.setStatus(_A)
_ExtremePortUtilizationPeakRxPkts_Type=Integer32
_ExtremePortUtilizationPeakRxPkts_Object=MibTableColumn
extremePortUtilizationPeakRxPkts=_ExtremePortUtilizationPeakRxPkts_Object((1,3,6,1,4,1,1916,1,4,11,1,4),_ExtremePortUtilizationPeakRxPkts_Type())
extremePortUtilizationPeakRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakRxPkts.setStatus(_A)
_ExtremePortUtilizationAvgTxBytes_Type=Integer32
_ExtremePortUtilizationAvgTxBytes_Object=MibTableColumn
extremePortUtilizationAvgTxBytes=_ExtremePortUtilizationAvgTxBytes_Object((1,3,6,1,4,1,1916,1,4,11,1,5),_ExtremePortUtilizationAvgTxBytes_Type())
extremePortUtilizationAvgTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgTxBytes.setStatus(_A)
_ExtremePortUtilizationAvgRxBytes_Type=Integer32
_ExtremePortUtilizationAvgRxBytes_Object=MibTableColumn
extremePortUtilizationAvgRxBytes=_ExtremePortUtilizationAvgRxBytes_Object((1,3,6,1,4,1,1916,1,4,11,1,6),_ExtremePortUtilizationAvgRxBytes_Type())
extremePortUtilizationAvgRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgRxBytes.setStatus(_A)
_ExtremePortUtilizationPeakTxBytes_Type=Integer32
_ExtremePortUtilizationPeakTxBytes_Object=MibTableColumn
extremePortUtilizationPeakTxBytes=_ExtremePortUtilizationPeakTxBytes_Object((1,3,6,1,4,1,1916,1,4,11,1,7),_ExtremePortUtilizationPeakTxBytes_Type())
extremePortUtilizationPeakTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakTxBytes.setStatus(_A)
_ExtremePortUtilizationPeakRxBytes_Type=Integer32
_ExtremePortUtilizationPeakRxBytes_Object=MibTableColumn
extremePortUtilizationPeakRxBytes=_ExtremePortUtilizationPeakRxBytes_Object((1,3,6,1,4,1,1916,1,4,11,1,8),_ExtremePortUtilizationPeakRxBytes_Type())
extremePortUtilizationPeakRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakRxBytes.setStatus(_A)
_ExtremePortUtilizationAvgTxPkts64_Type=Counter64
_ExtremePortUtilizationAvgTxPkts64_Object=MibTableColumn
extremePortUtilizationAvgTxPkts64=_ExtremePortUtilizationAvgTxPkts64_Object((1,3,6,1,4,1,1916,1,4,11,1,9),_ExtremePortUtilizationAvgTxPkts64_Type())
extremePortUtilizationAvgTxPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgTxPkts64.setStatus(_A)
_ExtremePortUtilizationAvgRxPkts64_Type=Counter64
_ExtremePortUtilizationAvgRxPkts64_Object=MibTableColumn
extremePortUtilizationAvgRxPkts64=_ExtremePortUtilizationAvgRxPkts64_Object((1,3,6,1,4,1,1916,1,4,11,1,10),_ExtremePortUtilizationAvgRxPkts64_Type())
extremePortUtilizationAvgRxPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgRxPkts64.setStatus(_A)
_ExtremePortUtilizationPeakTxPkts64_Type=Counter64
_ExtremePortUtilizationPeakTxPkts64_Object=MibTableColumn
extremePortUtilizationPeakTxPkts64=_ExtremePortUtilizationPeakTxPkts64_Object((1,3,6,1,4,1,1916,1,4,11,1,11),_ExtremePortUtilizationPeakTxPkts64_Type())
extremePortUtilizationPeakTxPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakTxPkts64.setStatus(_A)
_ExtremePortUtilizationPeakRxPkts64_Type=Counter64
_ExtremePortUtilizationPeakRxPkts64_Object=MibTableColumn
extremePortUtilizationPeakRxPkts64=_ExtremePortUtilizationPeakRxPkts64_Object((1,3,6,1,4,1,1916,1,4,11,1,12),_ExtremePortUtilizationPeakRxPkts64_Type())
extremePortUtilizationPeakRxPkts64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakRxPkts64.setStatus(_A)
_ExtremePortUtilizationAvgTxBytes64_Type=Counter64
_ExtremePortUtilizationAvgTxBytes64_Object=MibTableColumn
extremePortUtilizationAvgTxBytes64=_ExtremePortUtilizationAvgTxBytes64_Object((1,3,6,1,4,1,1916,1,4,11,1,13),_ExtremePortUtilizationAvgTxBytes64_Type())
extremePortUtilizationAvgTxBytes64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgTxBytes64.setStatus(_A)
_ExtremePortUtilizationAvgRxBytes64_Type=Counter64
_ExtremePortUtilizationAvgRxBytes64_Object=MibTableColumn
extremePortUtilizationAvgRxBytes64=_ExtremePortUtilizationAvgRxBytes64_Object((1,3,6,1,4,1,1916,1,4,11,1,14),_ExtremePortUtilizationAvgRxBytes64_Type())
extremePortUtilizationAvgRxBytes64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationAvgRxBytes64.setStatus(_A)
_ExtremePortUtilizationPeakTxBytes64_Type=Counter64
_ExtremePortUtilizationPeakTxBytes64_Object=MibTableColumn
extremePortUtilizationPeakTxBytes64=_ExtremePortUtilizationPeakTxBytes64_Object((1,3,6,1,4,1,1916,1,4,11,1,15),_ExtremePortUtilizationPeakTxBytes64_Type())
extremePortUtilizationPeakTxBytes64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakTxBytes64.setStatus(_A)
_ExtremePortUtilizationPeakRxBytes64_Type=Counter64
_ExtremePortUtilizationPeakRxBytes64_Object=MibTableColumn
extremePortUtilizationPeakRxBytes64=_ExtremePortUtilizationPeakRxBytes64_Object((1,3,6,1,4,1,1916,1,4,11,1,16),_ExtremePortUtilizationPeakRxBytes64_Type())
extremePortUtilizationPeakRxBytes64.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortUtilizationPeakRxBytes64.setStatus(_A)
_ExtremePortQosStatsTable_Object=MibTable
extremePortQosStatsTable=_ExtremePortQosStatsTable_Object((1,3,6,1,4,1,1916,1,4,12))
if mibBuilder.loadTexts:extremePortQosStatsTable.setStatus(_A)
_ExtremePortQosStatsEntry_Object=MibTableRow
extremePortQosStatsEntry=_ExtremePortQosStatsEntry_Object((1,3,6,1,4,1,1916,1,4,12,1))
extremePortQosStatsEntry.setIndexNames((0,_D,_E),(0,_G,_W))
if mibBuilder.loadTexts:extremePortQosStatsEntry.setStatus(_A)
_ExtremePortQosIngress_Type=ExtremePortTrafficDirection
_ExtremePortQosIngress_Object=MibTableColumn
extremePortQosIngress=_ExtremePortQosIngress_Object((1,3,6,1,4,1,1916,1,4,12,1,1),_ExtremePortQosIngress_Type())
extremePortQosIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQosIngress.setStatus(_A)
_ExtremePortQP0TxBytes_Type=Counter64
_ExtremePortQP0TxBytes_Object=MibTableColumn
extremePortQP0TxBytes=_ExtremePortQP0TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,2),_ExtremePortQP0TxBytes_Type())
extremePortQP0TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP0TxBytes.setStatus(_A)
_ExtremePortQP0TxPkts_Type=Counter64
_ExtremePortQP0TxPkts_Object=MibTableColumn
extremePortQP0TxPkts=_ExtremePortQP0TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,3),_ExtremePortQP0TxPkts_Type())
extremePortQP0TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP0TxPkts.setStatus(_A)
_ExtremePortQP1TxBytes_Type=Counter64
_ExtremePortQP1TxBytes_Object=MibTableColumn
extremePortQP1TxBytes=_ExtremePortQP1TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,4),_ExtremePortQP1TxBytes_Type())
extremePortQP1TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP1TxBytes.setStatus(_A)
_ExtremePortQP1TxPkts_Type=Counter64
_ExtremePortQP1TxPkts_Object=MibTableColumn
extremePortQP1TxPkts=_ExtremePortQP1TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,5),_ExtremePortQP1TxPkts_Type())
extremePortQP1TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP1TxPkts.setStatus(_A)
_ExtremePortQP2TxBytes_Type=Counter64
_ExtremePortQP2TxBytes_Object=MibTableColumn
extremePortQP2TxBytes=_ExtremePortQP2TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,6),_ExtremePortQP2TxBytes_Type())
extremePortQP2TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP2TxBytes.setStatus(_A)
_ExtremePortQP2TxPkts_Type=Counter64
_ExtremePortQP2TxPkts_Object=MibTableColumn
extremePortQP2TxPkts=_ExtremePortQP2TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,7),_ExtremePortQP2TxPkts_Type())
extremePortQP2TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP2TxPkts.setStatus(_A)
_ExtremePortQP3TxBytes_Type=Counter64
_ExtremePortQP3TxBytes_Object=MibTableColumn
extremePortQP3TxBytes=_ExtremePortQP3TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,8),_ExtremePortQP3TxBytes_Type())
extremePortQP3TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP3TxBytes.setStatus(_A)
_ExtremePortQP3TxPkts_Type=Counter64
_ExtremePortQP3TxPkts_Object=MibTableColumn
extremePortQP3TxPkts=_ExtremePortQP3TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,9),_ExtremePortQP3TxPkts_Type())
extremePortQP3TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP3TxPkts.setStatus(_A)
_ExtremePortQP4TxBytes_Type=Counter64
_ExtremePortQP4TxBytes_Object=MibTableColumn
extremePortQP4TxBytes=_ExtremePortQP4TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,10),_ExtremePortQP4TxBytes_Type())
extremePortQP4TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP4TxBytes.setStatus(_A)
_ExtremePortQP4TxPkts_Type=Counter64
_ExtremePortQP4TxPkts_Object=MibTableColumn
extremePortQP4TxPkts=_ExtremePortQP4TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,11),_ExtremePortQP4TxPkts_Type())
extremePortQP4TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP4TxPkts.setStatus(_A)
_ExtremePortQP5TxBytes_Type=Counter64
_ExtremePortQP5TxBytes_Object=MibTableColumn
extremePortQP5TxBytes=_ExtremePortQP5TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,12),_ExtremePortQP5TxBytes_Type())
extremePortQP5TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP5TxBytes.setStatus(_A)
_ExtremePortQP5TxPkts_Type=Counter64
_ExtremePortQP5TxPkts_Object=MibTableColumn
extremePortQP5TxPkts=_ExtremePortQP5TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,13),_ExtremePortQP5TxPkts_Type())
extremePortQP5TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP5TxPkts.setStatus(_A)
_ExtremePortQP6TxBytes_Type=Counter64
_ExtremePortQP6TxBytes_Object=MibTableColumn
extremePortQP6TxBytes=_ExtremePortQP6TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,14),_ExtremePortQP6TxBytes_Type())
extremePortQP6TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP6TxBytes.setStatus(_A)
_ExtremePortQP6TxPkts_Type=Counter64
_ExtremePortQP6TxPkts_Object=MibTableColumn
extremePortQP6TxPkts=_ExtremePortQP6TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,15),_ExtremePortQP6TxPkts_Type())
extremePortQP6TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP6TxPkts.setStatus(_A)
_ExtremePortQP7TxBytes_Type=Counter64
_ExtremePortQP7TxBytes_Object=MibTableColumn
extremePortQP7TxBytes=_ExtremePortQP7TxBytes_Object((1,3,6,1,4,1,1916,1,4,12,1,16),_ExtremePortQP7TxBytes_Type())
extremePortQP7TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP7TxBytes.setStatus(_A)
_ExtremePortQP7TxPkts_Type=Counter64
_ExtremePortQP7TxPkts_Object=MibTableColumn
extremePortQP7TxPkts=_ExtremePortQP7TxPkts_Object((1,3,6,1,4,1,1916,1,4,12,1,17),_ExtremePortQP7TxPkts_Type())
extremePortQP7TxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP7TxPkts.setStatus(_A)
_ExtremePortMau_ObjectIdentity=ObjectIdentity
extremePortMau=_ExtremePortMau_ObjectIdentity((1,3,6,1,4,1,1916,1,4,13))
_ExtremePortMauTable_Object=MibTable
extremePortMauTable=_ExtremePortMauTable_Object((1,3,6,1,4,1,1916,1,4,13,1))
if mibBuilder.loadTexts:extremePortMauTable.setStatus(_A)
_ExtremePortMauEntry_Object=MibTableRow
extremePortMauEntry=_ExtremePortMauEntry_Object((1,3,6,1,4,1,1916,1,4,13,1,1))
extremePortMauEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortMauEntry.setStatus(_A)
class _ExtremePortMauType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ExtremePortMauType_Type.__name__=_J
_ExtremePortMauType_Object=MibTableColumn
extremePortMauType=_ExtremePortMauType_Object((1,3,6,1,4,1,1916,1,4,13,1,1,1),_ExtremePortMauType_Type())
extremePortMauType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortMauType.setStatus(_A)
class _ExtremePortMauVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ExtremePortMauVendorName_Type.__name__=_J
_ExtremePortMauVendorName_Object=MibTableColumn
extremePortMauVendorName=_ExtremePortMauVendorName_Object((1,3,6,1,4,1,1916,1,4,13,1,1,2),_ExtremePortMauVendorName_Type())
extremePortMauVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortMauVendorName.setStatus(_A)
class _ExtremePortMauStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inserted',1),('empty',2)))
_ExtremePortMauStatus_Type.__name__=_C
_ExtremePortMauStatus_Object=MibTableColumn
extremePortMauStatus=_ExtremePortMauStatus_Object((1,3,6,1,4,1,1916,1,4,13,1,1,3),_ExtremePortMauStatus_Type())
extremePortMauStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortMauStatus.setStatus(_A)
class _ExtremePortMauRestrict_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_ExtremePortMauRestrict_Type.__name__=_J
_ExtremePortMauRestrict_Object=MibTableColumn
extremePortMauRestrict=_ExtremePortMauRestrict_Object((1,3,6,1,4,1,1916,1,4,13,1,1,4),_ExtremePortMauRestrict_Type())
extremePortMauRestrict.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortMauRestrict.setStatus(_A)
_ExtremePortMauTraps_ObjectIdentity=ObjectIdentity
extremePortMauTraps=_ExtremePortMauTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,4,13,2))
_ExtremePortMauTrapsPrefix_ObjectIdentity=ObjectIdentity
extremePortMauTrapsPrefix=_ExtremePortMauTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,4,13,2,0))
_ExtremePortCongestionStatsTable_Object=MibTable
extremePortCongestionStatsTable=_ExtremePortCongestionStatsTable_Object((1,3,6,1,4,1,1916,1,4,14))
if mibBuilder.loadTexts:extremePortCongestionStatsTable.setStatus(_A)
_ExtremePortCongestionStatsEntry_Object=MibTableRow
extremePortCongestionStatsEntry=_ExtremePortCongestionStatsEntry_Object((1,3,6,1,4,1,1916,1,4,14,1))
extremePortCongestionStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortCongestionStatsEntry.setStatus(_A)
_ExtremePortCongDropPkts_Type=Counter64
_ExtremePortCongDropPkts_Object=MibTableColumn
extremePortCongDropPkts=_ExtremePortCongDropPkts_Object((1,3,6,1,4,1,1916,1,4,14,1,1),_ExtremePortCongDropPkts_Type())
extremePortCongDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortCongDropPkts.setStatus(_A)
_ExtremePortQosCongestionStatsTable_Object=MibTable
extremePortQosCongestionStatsTable=_ExtremePortQosCongestionStatsTable_Object((1,3,6,1,4,1,1916,1,4,15))
if mibBuilder.loadTexts:extremePortQosCongestionStatsTable.setStatus(_A)
_ExtremePortQosCongestionStatsEntry_Object=MibTableRow
extremePortQosCongestionStatsEntry=_ExtremePortQosCongestionStatsEntry_Object((1,3,6,1,4,1,1916,1,4,15,1))
extremePortQosCongestionStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortQosCongestionStatsEntry.setStatus(_A)
_ExtremePortQP0CongPkts_Type=Counter64
_ExtremePortQP0CongPkts_Object=MibTableColumn
extremePortQP0CongPkts=_ExtremePortQP0CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,1),_ExtremePortQP0CongPkts_Type())
extremePortQP0CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP0CongPkts.setStatus(_A)
_ExtremePortQP1CongPkts_Type=Counter64
_ExtremePortQP1CongPkts_Object=MibTableColumn
extremePortQP1CongPkts=_ExtremePortQP1CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,2),_ExtremePortQP1CongPkts_Type())
extremePortQP1CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP1CongPkts.setStatus(_A)
_ExtremePortQP2CongPkts_Type=Counter64
_ExtremePortQP2CongPkts_Object=MibTableColumn
extremePortQP2CongPkts=_ExtremePortQP2CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,3),_ExtremePortQP2CongPkts_Type())
extremePortQP2CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP2CongPkts.setStatus(_A)
_ExtremePortQP3CongPkts_Type=Counter64
_ExtremePortQP3CongPkts_Object=MibTableColumn
extremePortQP3CongPkts=_ExtremePortQP3CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,4),_ExtremePortQP3CongPkts_Type())
extremePortQP3CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP3CongPkts.setStatus(_A)
_ExtremePortQP4CongPkts_Type=Counter64
_ExtremePortQP4CongPkts_Object=MibTableColumn
extremePortQP4CongPkts=_ExtremePortQP4CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,5),_ExtremePortQP4CongPkts_Type())
extremePortQP4CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP4CongPkts.setStatus(_A)
_ExtremePortQP5CongPkts_Type=Counter64
_ExtremePortQP5CongPkts_Object=MibTableColumn
extremePortQP5CongPkts=_ExtremePortQP5CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,6),_ExtremePortQP5CongPkts_Type())
extremePortQP5CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP5CongPkts.setStatus(_A)
_ExtremePortQP6CongPkts_Type=Counter64
_ExtremePortQP6CongPkts_Object=MibTableColumn
extremePortQP6CongPkts=_ExtremePortQP6CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,7),_ExtremePortQP6CongPkts_Type())
extremePortQP6CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP6CongPkts.setStatus(_A)
_ExtremePortQP7CongPkts_Type=Counter64
_ExtremePortQP7CongPkts_Object=MibTableColumn
extremePortQP7CongPkts=_ExtremePortQP7CongPkts_Object((1,3,6,1,4,1,1916,1,4,15,1,8),_ExtremePortQP7CongPkts_Type())
extremePortQP7CongPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortQP7CongPkts.setStatus(_A)
_ExtremePortVlanInfoTable_Object=MibTable
extremePortVlanInfoTable=_ExtremePortVlanInfoTable_Object((1,3,6,1,4,1,1916,1,4,17))
if mibBuilder.loadTexts:extremePortVlanInfoTable.setStatus(_A)
_ExtremePortVlanInfoEntry_Object=MibTableRow
extremePortVlanInfoEntry=_ExtremePortVlanInfoEntry_Object((1,3,6,1,4,1,1916,1,4,17,1))
extremePortVlanInfoEntry.setIndexNames((0,_D,_E),(0,_K,_L))
if mibBuilder.loadTexts:extremePortVlanInfoEntry.setStatus(_A)
class _ExtremePortVlanInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremePortVlanInfoDescr_Type.__name__=_J
_ExtremePortVlanInfoDescr_Object=MibTableColumn
extremePortVlanInfoDescr=_ExtremePortVlanInfoDescr_Object((1,3,6,1,4,1,1916,1,4,17,1,1),_ExtremePortVlanInfoDescr_Type())
extremePortVlanInfoDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:extremePortVlanInfoDescr.setStatus(_A)
class _ExtremePortVlanInfoLimitLearningEnabled_Type(Integer32):defaultValue=0
_ExtremePortVlanInfoLimitLearningEnabled_Type.__name__=_C
_ExtremePortVlanInfoLimitLearningEnabled_Object=MibTableColumn
extremePortVlanInfoLimitLearningEnabled=_ExtremePortVlanInfoLimitLearningEnabled_Object((1,3,6,1,4,1,1916,1,4,17,1,2),_ExtremePortVlanInfoLimitLearningEnabled_Type())
extremePortVlanInfoLimitLearningEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortVlanInfoLimitLearningEnabled.setStatus(_A)
class _ExtremePortVlanInfoLimitLearningNumber_Type(Integer32):defaultValue=0
_ExtremePortVlanInfoLimitLearningNumber_Type.__name__=_C
_ExtremePortVlanInfoLimitLearningNumber_Object=MibTableColumn
extremePortVlanInfoLimitLearningNumber=_ExtremePortVlanInfoLimitLearningNumber_Object((1,3,6,1,4,1,1916,1,4,17,1,3),_ExtremePortVlanInfoLimitLearningNumber_Type())
extremePortVlanInfoLimitLearningNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortVlanInfoLimitLearningNumber.setStatus(_A)
class _ExtremePortVlanInfoMacLockDownEnabled_Type(Integer32):defaultValue=0
_ExtremePortVlanInfoMacLockDownEnabled_Type.__name__=_C
_ExtremePortVlanInfoMacLockDownEnabled_Object=MibTableColumn
extremePortVlanInfoMacLockDownEnabled=_ExtremePortVlanInfoMacLockDownEnabled_Object((1,3,6,1,4,1,1916,1,4,17,1,4),_ExtremePortVlanInfoMacLockDownEnabled_Type())
extremePortVlanInfoMacLockDownEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortVlanInfoMacLockDownEnabled.setStatus(_A)
_ExtremePortConfigTable_Object=MibTable
extremePortConfigTable=_ExtremePortConfigTable_Object((1,3,6,1,4,1,1916,1,4,18))
if mibBuilder.loadTexts:extremePortConfigTable.setStatus(_A)
_ExtremePortConfigEntry_Object=MibTableRow
extremePortConfigEntry=_ExtremePortConfigEntry_Object((1,3,6,1,4,1,1916,1,4,18,1))
extremePortConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremePortConfigEntry.setStatus(_A)
class _ExtremePortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_ExtremePortAutoNegotiation_Type.__name__=_C
_ExtremePortAutoNegotiation_Object=MibTableColumn
extremePortAutoNegotiation=_ExtremePortAutoNegotiation_Object((1,3,6,1,4,1,1916,1,4,18,1,1),_ExtremePortAutoNegotiation_Type())
extremePortAutoNegotiation.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortAutoNegotiation.setStatus(_A)
class _ExtremePortAdminSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,10,11,12)));namedValues=NamedValues(*(('auto',0),('s10',1),('s100',2),('s1000',3),('s10000',4),('s25000',5),('s40000',6),('s50000',7),('s100000',10),('s2500',11),('s5000',12)))
_ExtremePortAdminSpeed_Type.__name__=_C
_ExtremePortAdminSpeed_Object=MibTableColumn
extremePortAdminSpeed=_ExtremePortAdminSpeed_Object((1,3,6,1,4,1,1916,1,4,18,1,2),_ExtremePortAdminSpeed_Type())
extremePortAdminSpeed.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortAdminSpeed.setStatus(_A)
class _ExtremePortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('half',0),('full',1),('auto',2)))
_ExtremePortDuplex_Type.__name__=_C
_ExtremePortDuplex_Object=MibTableColumn
extremePortDuplex=_ExtremePortDuplex_Object((1,3,6,1,4,1,1916,1,4,18,1,3),_ExtremePortDuplex_Type())
extremePortDuplex.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortDuplex.setStatus(_A)
class _ExtremePortMedium_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('copper',0),('fiber',1),('nonComboPort',2)))
_ExtremePortMedium_Type.__name__=_C
_ExtremePortMedium_Object=MibTableColumn
extremePortMedium=_ExtremePortMedium_Object((1,3,6,1,4,1,1916,1,4,18,1,4),_ExtremePortMedium_Type())
extremePortMedium.setMaxAccess(_I)
if mibBuilder.loadTexts:extremePortMedium.setStatus(_A)
extremePortMauChangeTrap=NotificationType((1,3,6,1,4,1,1916,1,4,13,2,0,1))
extremePortMauChangeTrap.setObjects(*((_D,_E),(_G,_X),(_G,_Y)))
if mibBuilder.loadTexts:extremePortMauChangeTrap.setStatus(_A)
extremePortMauRestrictionTrap=NotificationType((1,3,6,1,4,1,1916,1,4,13,2,0,2))
extremePortMauRestrictionTrap.setObjects(*((_D,_E),(_G,_Z)))
if mibBuilder.loadTexts:extremePortMauRestrictionTrap.setStatus(_A)
extremeRateLimitExceededAlarm=NotificationType((1,3,6,1,4,1,1916,1,4,16))
extremeRateLimitExceededAlarm.setObjects((_D,_E))
if mibBuilder.loadTexts:extremeRateLimitExceededAlarm.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ExtremePortTrafficDirection':ExtremePortTrafficDirection,'extremePort':extremePort,'extremePortLoadshareTable':extremePortLoadshareTable,'extremePortLoadshareEntry':extremePortLoadshareEntry,_N:extremePortLoadshareMasterIfIndex,_O:extremePortLoadshareSlaveIfIndex,'extremePortLoadshareGrouping':extremePortLoadshareGrouping,'extremePortLoadshareStatus':extremePortLoadshareStatus,'extremePortSummitlinkTable':extremePortSummitlinkTable,'extremePortSummitlinkEntry':extremePortSummitlinkEntry,'extremePortSummitlinkAdminMode':extremePortSummitlinkAdminMode,'extremePortSummitlinkOperMode':extremePortSummitlinkOperMode,'extremePortSummitlinkState':extremePortSummitlinkState,'extremePortSummitlinkRejectReason':extremePortSummitlinkRejectReason,'extremePortLoadshare2Table':extremePortLoadshare2Table,'extremePortLoadshare2Entry':extremePortLoadshare2Entry,_R:extremePortLoadshare2MasterIfIndex,_S:extremePortLoadshare2SlaveIfIndex,'extremePortLoadshare2Algorithm':extremePortLoadshare2Algorithm,'extremePortLoadshare2Status':extremePortLoadshare2Status,'extremePortLoadshare2MinActiveLinks':extremePortLoadshare2MinActiveLinks,'extremePortLoadshare2AggControlType':extremePortLoadshare2AggControlType,'extremePortRateShapeTable':extremePortRateShapeTable,'extremePortRateShapeEntry':extremePortRateShapeEntry,'extremePortRateShapePortType':extremePortRateShapePortType,'extremePortRateShapeLoopbackTag':extremePortRateShapeLoopbackTag,'extremePortRateShapeStatus':extremePortRateShapeStatus,'extremePortUtilizationTable':extremePortUtilizationTable,'extremePortUtilizationEntry':extremePortUtilizationEntry,'extremePortUtilizationAvgTxBw':extremePortUtilizationAvgTxBw,'extremePortUtilizationAvgRxBw':extremePortUtilizationAvgRxBw,'extremePortUtilizationPeakTxBw':extremePortUtilizationPeakTxBw,'extremePortUtilizationPeakRxBw':extremePortUtilizationPeakRxBw,'extremePortInfoTable':extremePortInfoTable,'extremePortInfoEntry':extremePortInfoEntry,'extremePortInfoFilterUpCounter':extremePortInfoFilterUpCounter,'extremePortInfoFilterDownCounter':extremePortInfoFilterDownCounter,'extremePortXenpakVendorTable':extremePortXenpakVendorTable,'extremePortXenpakVendorEntry':extremePortXenpakVendorEntry,'extremePortXenpakVendorName':extremePortXenpakVendorName,'extremePortIngressStats':extremePortIngressStats,'extremePortIngressStatsPortTable':extremePortIngressStatsPortTable,'extremePortIngressPortStatsEntry':extremePortIngressPortStatsEntry,'extremePortIngressStatsLinkStatus':extremePortIngressStatsLinkStatus,'extremePortIngressStatsPortHighPriBytes':extremePortIngressStatsPortHighPriBytes,'extremePortIngressStatsPortLowPriBytes':extremePortIngressStatsPortLowPriBytes,'extremePortIngressStatsPortDroppedBytes':extremePortIngressStatsPortDroppedBytes,'extremePortIngressStatsTxXoff':extremePortIngressStatsTxXoff,'extremePortIngressStatsQueueTable':extremePortIngressStatsQueueTable,'extremePortIngressQueueStatsEntry':extremePortIngressQueueStatsEntry,_U:extremePortIngressStatsQueueIndex,'extremePortIngressStatsQueueHighPriBytes':extremePortIngressStatsQueueHighPriBytes,'extremePortIngressStatsQueueLowPriBytes':extremePortIngressStatsQueueLowPriBytes,'extremePortIngressStatsQueuePercentDropped':extremePortIngressStatsQueuePercentDropped,'extremePortEgressRateLimitTable':extremePortEgressRateLimitTable,'extremePortEgressRateLimitEntry':extremePortEgressRateLimitEntry,'extremePortEgressRateLimitType':extremePortEgressRateLimitType,'extremePortEgressRateLimitValue':extremePortEgressRateLimitValue,'extremeWiredClientTable':extremeWiredClientTable,'extremeWiredClientEntry':extremeWiredClientEntry,_V:extremeWiredClientID,'extremeWiredClientState':extremeWiredClientState,'extremeWiredClientVLAN':extremeWiredClientVLAN,'extremeWiredClientPriority':extremeWiredClientPriority,'extremeWiredClientAuthType':extremeWiredClientAuthType,'extremeWiredClientLastStateChangeTime':extremeWiredClientLastStateChangeTime,'extremeWiredClientIP':extremeWiredClientIP,'extremePortUtilizationExtnTable':extremePortUtilizationExtnTable,'extremePortUtilizationExtnEntry':extremePortUtilizationExtnEntry,'extremePortUtilizationAvgTxPkts':extremePortUtilizationAvgTxPkts,'extremePortUtilizationAvgRxPkts':extremePortUtilizationAvgRxPkts,'extremePortUtilizationPeakTxPkts':extremePortUtilizationPeakTxPkts,'extremePortUtilizationPeakRxPkts':extremePortUtilizationPeakRxPkts,'extremePortUtilizationAvgTxBytes':extremePortUtilizationAvgTxBytes,'extremePortUtilizationAvgRxBytes':extremePortUtilizationAvgRxBytes,'extremePortUtilizationPeakTxBytes':extremePortUtilizationPeakTxBytes,'extremePortUtilizationPeakRxBytes':extremePortUtilizationPeakRxBytes,'extremePortUtilizationAvgTxPkts64':extremePortUtilizationAvgTxPkts64,'extremePortUtilizationAvgRxPkts64':extremePortUtilizationAvgRxPkts64,'extremePortUtilizationPeakTxPkts64':extremePortUtilizationPeakTxPkts64,'extremePortUtilizationPeakRxPkts64':extremePortUtilizationPeakRxPkts64,'extremePortUtilizationAvgTxBytes64':extremePortUtilizationAvgTxBytes64,'extremePortUtilizationAvgRxBytes64':extremePortUtilizationAvgRxBytes64,'extremePortUtilizationPeakTxBytes64':extremePortUtilizationPeakTxBytes64,'extremePortUtilizationPeakRxBytes64':extremePortUtilizationPeakRxBytes64,'extremePortQosStatsTable':extremePortQosStatsTable,'extremePortQosStatsEntry':extremePortQosStatsEntry,_W:extremePortQosIngress,'extremePortQP0TxBytes':extremePortQP0TxBytes,'extremePortQP0TxPkts':extremePortQP0TxPkts,'extremePortQP1TxBytes':extremePortQP1TxBytes,'extremePortQP1TxPkts':extremePortQP1TxPkts,'extremePortQP2TxBytes':extremePortQP2TxBytes,'extremePortQP2TxPkts':extremePortQP2TxPkts,'extremePortQP3TxBytes':extremePortQP3TxBytes,'extremePortQP3TxPkts':extremePortQP3TxPkts,'extremePortQP4TxBytes':extremePortQP4TxBytes,'extremePortQP4TxPkts':extremePortQP4TxPkts,'extremePortQP5TxBytes':extremePortQP5TxBytes,'extremePortQP5TxPkts':extremePortQP5TxPkts,'extremePortQP6TxBytes':extremePortQP6TxBytes,'extremePortQP6TxPkts':extremePortQP6TxPkts,'extremePortQP7TxBytes':extremePortQP7TxBytes,'extremePortQP7TxPkts':extremePortQP7TxPkts,'extremePortMau':extremePortMau,'extremePortMauTable':extremePortMauTable,'extremePortMauEntry':extremePortMauEntry,_X:extremePortMauType,'extremePortMauVendorName':extremePortMauVendorName,_Y:extremePortMauStatus,_Z:extremePortMauRestrict,'extremePortMauTraps':extremePortMauTraps,'extremePortMauTrapsPrefix':extremePortMauTrapsPrefix,'extremePortMauChangeTrap':extremePortMauChangeTrap,'extremePortMauRestrictionTrap':extremePortMauRestrictionTrap,'extremePortCongestionStatsTable':extremePortCongestionStatsTable,'extremePortCongestionStatsEntry':extremePortCongestionStatsEntry,'extremePortCongDropPkts':extremePortCongDropPkts,'extremePortQosCongestionStatsTable':extremePortQosCongestionStatsTable,'extremePortQosCongestionStatsEntry':extremePortQosCongestionStatsEntry,'extremePortQP0CongPkts':extremePortQP0CongPkts,'extremePortQP1CongPkts':extremePortQP1CongPkts,'extremePortQP2CongPkts':extremePortQP2CongPkts,'extremePortQP3CongPkts':extremePortQP3CongPkts,'extremePortQP4CongPkts':extremePortQP4CongPkts,'extremePortQP5CongPkts':extremePortQP5CongPkts,'extremePortQP6CongPkts':extremePortQP6CongPkts,'extremePortQP7CongPkts':extremePortQP7CongPkts,'extremeRateLimitExceededAlarm':extremeRateLimitExceededAlarm,'extremePortVlanInfoTable':extremePortVlanInfoTable,'extremePortVlanInfoEntry':extremePortVlanInfoEntry,'extremePortVlanInfoDescr':extremePortVlanInfoDescr,'extremePortVlanInfoLimitLearningEnabled':extremePortVlanInfoLimitLearningEnabled,'extremePortVlanInfoLimitLearningNumber':extremePortVlanInfoLimitLearningNumber,'extremePortVlanInfoMacLockDownEnabled':extremePortVlanInfoMacLockDownEnabled,'extremePortConfigTable':extremePortConfigTable,'extremePortConfigEntry':extremePortConfigEntry,'extremePortAutoNegotiation':extremePortAutoNegotiation,'extremePortAdminSpeed':extremePortAdminSpeed,'extremePortDuplex':extremePortDuplex,'extremePortMedium':extremePortMedium})