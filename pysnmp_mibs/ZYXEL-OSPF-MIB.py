_U='not-accessible'
_T='zyOspfSummaryAddressMaskBits'
_S='zyOspfSummaryAddressIpAddress'
_R='zyOspfRedistributeRouteProtocol'
_Q='ospfVirtIfNeighbor'
_P='ospfVirtIfAreaId'
_O='ospfNbrIpAddr'
_N='ospfNbrAddressLessIndex'
_M='ospfLsdbType'
_L='ospfLsdbRouterId'
_K='ospfLsdbLsid'
_J='ospfLsdbAreaId'
_I='ospfAreaId'
_H='Integer32'
_G='ospfIfIpAddress'
_F='ospfAddressLessIf'
_E='ZYXEL-OSPF-MIB'
_D='read-write'
_C='OSPF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ospfAddressLessIf,ospfAreaId,ospfIfIpAddress,ospfLsdbAreaId,ospfLsdbLsid,ospfLsdbRouterId,ospfLsdbType,ospfNbrAddressLessIndex,ospfNbrIpAddr,ospfVirtIfAreaId,ospfVirtIfNeighbor=mibBuilder.importSymbols(_C,_F,_I,_G,_J,_K,_L,_M,_N,_O,_P,_Q)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelOspf=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,57))
_ZyxelOspfSetup_ObjectIdentity=ObjectIdentity
zyxelOspfSetup=_ZyxelOspfSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,57,1))
_ZyxelOspfIfTable_Object=MibTable
zyxelOspfIfTable=_ZyxelOspfIfTable_Object((1,3,6,1,4,1,890,1,15,3,57,1,1))
if mibBuilder.loadTexts:zyxelOspfIfTable.setStatus(_A)
_ZyxelOspfIfEntry_Object=MibTableRow
zyxelOspfIfEntry=_ZyxelOspfIfEntry_Object((1,3,6,1,4,1,890,1,15,3,57,1,1,1))
zyxelOspfIfEntry.setIndexNames((0,_C,_G),(0,_C,_F))
if mibBuilder.loadTexts:zyxelOspfIfEntry.setStatus(_A)
_ZyOspfIfKeyId_Type=Integer32
_ZyOspfIfKeyId_Object=MibTableColumn
zyOspfIfKeyId=_ZyOspfIfKeyId_Object((1,3,6,1,4,1,890,1,15,3,57,1,1,1,1),_ZyOspfIfKeyId_Type())
zyOspfIfKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfIfKeyId.setStatus(_A)
_ZyxelOspfAreaTable_Object=MibTable
zyxelOspfAreaTable=_ZyxelOspfAreaTable_Object((1,3,6,1,4,1,890,1,15,3,57,1,2))
if mibBuilder.loadTexts:zyxelOspfAreaTable.setStatus(_A)
_ZyxelOspfAreaEntry_Object=MibTableRow
zyxelOspfAreaEntry=_ZyxelOspfAreaEntry_Object((1,3,6,1,4,1,890,1,15,3,57,1,2,1))
zyxelOspfAreaEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:zyxelOspfAreaEntry.setStatus(_A)
_ZyOspfAreaName_Type=DisplayString
_ZyOspfAreaName_Object=MibTableColumn
zyOspfAreaName=_ZyOspfAreaName_Object((1,3,6,1,4,1,890,1,15,3,57,1,2,1,1),_ZyOspfAreaName_Type())
zyOspfAreaName.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfAreaName.setStatus(_A)
_ZyOspfAreaDefaultRouteMetric_Type=Integer32
_ZyOspfAreaDefaultRouteMetric_Object=MibTableColumn
zyOspfAreaDefaultRouteMetric=_ZyOspfAreaDefaultRouteMetric_Object((1,3,6,1,4,1,890,1,15,3,57,1,2,1,2),_ZyOspfAreaDefaultRouteMetric_Type())
zyOspfAreaDefaultRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfAreaDefaultRouteMetric.setStatus(_A)
_ZyxelOspfRedistributeRouteTable_Object=MibTable
zyxelOspfRedistributeRouteTable=_ZyxelOspfRedistributeRouteTable_Object((1,3,6,1,4,1,890,1,15,3,57,1,3))
if mibBuilder.loadTexts:zyxelOspfRedistributeRouteTable.setStatus(_A)
_ZyxelOspfRedistributeRouteEntry_Object=MibTableRow
zyxelOspfRedistributeRouteEntry=_ZyxelOspfRedistributeRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,57,1,3,1))
zyxelOspfRedistributeRouteEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:zyxelOspfRedistributeRouteEntry.setStatus(_A)
class _ZyOspfRedistributeRouteProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rip',1),('static',2)))
_ZyOspfRedistributeRouteProtocol_Type.__name__=_H
_ZyOspfRedistributeRouteProtocol_Object=MibTableColumn
zyOspfRedistributeRouteProtocol=_ZyOspfRedistributeRouteProtocol_Object((1,3,6,1,4,1,890,1,15,3,57,1,3,1,1),_ZyOspfRedistributeRouteProtocol_Type())
zyOspfRedistributeRouteProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfRedistributeRouteProtocol.setStatus(_A)
_ZyOspfRedistributeRouteState_Type=EnabledStatus
_ZyOspfRedistributeRouteState_Object=MibTableColumn
zyOspfRedistributeRouteState=_ZyOspfRedistributeRouteState_Object((1,3,6,1,4,1,890,1,15,3,57,1,3,1,2),_ZyOspfRedistributeRouteState_Type())
zyOspfRedistributeRouteState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfRedistributeRouteState.setStatus(_A)
_ZyOspfRedistributeRouteType_Type=Integer32
_ZyOspfRedistributeRouteType_Object=MibTableColumn
zyOspfRedistributeRouteType=_ZyOspfRedistributeRouteType_Object((1,3,6,1,4,1,890,1,15,3,57,1,3,1,3),_ZyOspfRedistributeRouteType_Type())
zyOspfRedistributeRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfRedistributeRouteType.setStatus(_A)
_ZyOspfRedistributeRouteMetric_Type=Integer32
_ZyOspfRedistributeRouteMetric_Object=MibTableColumn
zyOspfRedistributeRouteMetric=_ZyOspfRedistributeRouteMetric_Object((1,3,6,1,4,1,890,1,15,3,57,1,3,1,4),_ZyOspfRedistributeRouteMetric_Type())
zyOspfRedistributeRouteMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfRedistributeRouteMetric.setStatus(_A)
_ZyxelOspfVirtualLinkTable_Object=MibTable
zyxelOspfVirtualLinkTable=_ZyxelOspfVirtualLinkTable_Object((1,3,6,1,4,1,890,1,15,3,57,1,4))
if mibBuilder.loadTexts:zyxelOspfVirtualLinkTable.setStatus(_A)
_ZyxelOspfVirtualLinkEntry_Object=MibTableRow
zyxelOspfVirtualLinkEntry=_ZyxelOspfVirtualLinkEntry_Object((1,3,6,1,4,1,890,1,15,3,57,1,4,1))
zyxelOspfVirtualLinkEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:zyxelOspfVirtualLinkEntry.setStatus(_A)
_ZyOspfVirtualLinkName_Type=DisplayString
_ZyOspfVirtualLinkName_Object=MibTableColumn
zyOspfVirtualLinkName=_ZyOspfVirtualLinkName_Object((1,3,6,1,4,1,890,1,15,3,57,1,4,1,1),_ZyOspfVirtualLinkName_Type())
zyOspfVirtualLinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfVirtualLinkName.setStatus(_A)
_ZyOspfVirtualLinkKeyId_Type=Integer32
_ZyOspfVirtualLinkKeyId_Object=MibTableColumn
zyOspfVirtualLinkKeyId=_ZyOspfVirtualLinkKeyId_Object((1,3,6,1,4,1,890,1,15,3,57,1,4,1,2),_ZyOspfVirtualLinkKeyId_Type())
zyOspfVirtualLinkKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfVirtualLinkKeyId.setStatus(_A)
_ZyOspfMaxNumberOfSummaryAddress_Type=Integer32
_ZyOspfMaxNumberOfSummaryAddress_Object=MibScalar
zyOspfMaxNumberOfSummaryAddress=_ZyOspfMaxNumberOfSummaryAddress_Object((1,3,6,1,4,1,890,1,15,3,57,1,5),_ZyOspfMaxNumberOfSummaryAddress_Type())
zyOspfMaxNumberOfSummaryAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfMaxNumberOfSummaryAddress.setStatus(_A)
_ZyxelOspfSummaryAddressTable_Object=MibTable
zyxelOspfSummaryAddressTable=_ZyxelOspfSummaryAddressTable_Object((1,3,6,1,4,1,890,1,15,3,57,1,6))
if mibBuilder.loadTexts:zyxelOspfSummaryAddressTable.setStatus(_A)
_ZyxelOspfSummaryAddressEntry_Object=MibTableRow
zyxelOspfSummaryAddressEntry=_ZyxelOspfSummaryAddressEntry_Object((1,3,6,1,4,1,890,1,15,3,57,1,6,1))
zyxelOspfSummaryAddressEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:zyxelOspfSummaryAddressEntry.setStatus(_A)
_ZyOspfSummaryAddressIpAddress_Type=IpAddress
_ZyOspfSummaryAddressIpAddress_Object=MibTableColumn
zyOspfSummaryAddressIpAddress=_ZyOspfSummaryAddressIpAddress_Object((1,3,6,1,4,1,890,1,15,3,57,1,6,1,1),_ZyOspfSummaryAddressIpAddress_Type())
zyOspfSummaryAddressIpAddress.setMaxAccess(_U)
if mibBuilder.loadTexts:zyOspfSummaryAddressIpAddress.setStatus(_A)
_ZyOspfSummaryAddressMaskBits_Type=Integer32
_ZyOspfSummaryAddressMaskBits_Object=MibTableColumn
zyOspfSummaryAddressMaskBits=_ZyOspfSummaryAddressMaskBits_Object((1,3,6,1,4,1,890,1,15,3,57,1,6,1,2),_ZyOspfSummaryAddressMaskBits_Type())
zyOspfSummaryAddressMaskBits.setMaxAccess(_U)
if mibBuilder.loadTexts:zyOspfSummaryAddressMaskBits.setStatus(_A)
_ZyOspfSummaryAddressRowStatus_Type=RowStatus
_ZyOspfSummaryAddressRowStatus_Object=MibTableColumn
zyOspfSummaryAddressRowStatus=_ZyOspfSummaryAddressRowStatus_Object((1,3,6,1,4,1,890,1,15,3,57,1,6,1,3),_ZyOspfSummaryAddressRowStatus_Type())
zyOspfSummaryAddressRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyOspfSummaryAddressRowStatus.setStatus(_A)
_ZyxelOspfGeneralGroup_ObjectIdentity=ObjectIdentity
zyxelOspfGeneralGroup=_ZyxelOspfGeneralGroup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,57,1,7))
_ZyOspfDistance_Type=Integer32
_ZyOspfDistance_Object=MibScalar
zyOspfDistance=_ZyOspfDistance_Object((1,3,6,1,4,1,890,1,15,3,57,1,7,1),_ZyOspfDistance_Type())
zyOspfDistance.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfDistance.setStatus(_A)
_ZyOspfDefaultInformationOriginateState_Type=EnabledStatus
_ZyOspfDefaultInformationOriginateState_Object=MibScalar
zyOspfDefaultInformationOriginateState=_ZyOspfDefaultInformationOriginateState_Object((1,3,6,1,4,1,890,1,15,3,57,1,8),_ZyOspfDefaultInformationOriginateState_Type())
zyOspfDefaultInformationOriginateState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfDefaultInformationOriginateState.setStatus(_A)
_ZyOspfDefaultInformationOriginateAlways_Type=EnabledStatus
_ZyOspfDefaultInformationOriginateAlways_Object=MibScalar
zyOspfDefaultInformationOriginateAlways=_ZyOspfDefaultInformationOriginateAlways_Object((1,3,6,1,4,1,890,1,15,3,57,1,9),_ZyOspfDefaultInformationOriginateAlways_Type())
zyOspfDefaultInformationOriginateAlways.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfDefaultInformationOriginateAlways.setStatus(_A)
_ZyOspfDefaultInformationOriginateMetric_Type=Integer32
_ZyOspfDefaultInformationOriginateMetric_Object=MibScalar
zyOspfDefaultInformationOriginateMetric=_ZyOspfDefaultInformationOriginateMetric_Object((1,3,6,1,4,1,890,1,15,3,57,1,10),_ZyOspfDefaultInformationOriginateMetric_Type())
zyOspfDefaultInformationOriginateMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfDefaultInformationOriginateMetric.setStatus(_A)
_ZyOspfDefaultInformationOriginateMetricType_Type=Integer32
_ZyOspfDefaultInformationOriginateMetricType_Object=MibScalar
zyOspfDefaultInformationOriginateMetricType=_ZyOspfDefaultInformationOriginateMetricType_Object((1,3,6,1,4,1,890,1,15,3,57,1,11),_ZyOspfDefaultInformationOriginateMetricType_Type())
zyOspfDefaultInformationOriginateMetricType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOspfDefaultInformationOriginateMetricType.setStatus(_A)
_ZyxelOspfStatus_ObjectIdentity=ObjectIdentity
zyxelOspfStatus=_ZyxelOspfStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,57,2))
_ZyxelOspfIfInfoTable_Object=MibTable
zyxelOspfIfInfoTable=_ZyxelOspfIfInfoTable_Object((1,3,6,1,4,1,890,1,15,3,57,2,1))
if mibBuilder.loadTexts:zyxelOspfIfInfoTable.setStatus(_A)
_ZyxelOspfIfInfoEntry_Object=MibTableRow
zyxelOspfIfInfoEntry=_ZyxelOspfIfInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1))
zyxelOspfIfInfoEntry.setIndexNames((0,_C,_G),(0,_C,_F))
if mibBuilder.loadTexts:zyxelOspfIfInfoEntry.setStatus(_A)
_ZyOspfIfInfoMaskbits_Type=Integer32
_ZyOspfIfInfoMaskbits_Object=MibTableColumn
zyOspfIfInfoMaskbits=_ZyOspfIfInfoMaskbits_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,1),_ZyOspfIfInfoMaskbits_Type())
zyOspfIfInfoMaskbits.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoMaskbits.setStatus(_A)
_ZyOspfIfInfoDesignatedRouterID_Type=IpAddress
_ZyOspfIfInfoDesignatedRouterID_Object=MibTableColumn
zyOspfIfInfoDesignatedRouterID=_ZyOspfIfInfoDesignatedRouterID_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,2),_ZyOspfIfInfoDesignatedRouterID_Type())
zyOspfIfInfoDesignatedRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoDesignatedRouterID.setStatus(_A)
_ZyOspfIfInfoBackupDesignatedRouterID_Type=IpAddress
_ZyOspfIfInfoBackupDesignatedRouterID_Object=MibTableColumn
zyOspfIfInfoBackupDesignatedRouterID=_ZyOspfIfInfoBackupDesignatedRouterID_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,3),_ZyOspfIfInfoBackupDesignatedRouterID_Type())
zyOspfIfInfoBackupDesignatedRouterID.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoBackupDesignatedRouterID.setStatus(_A)
_ZyOspfIfInfoNbrCount_Type=Integer32
_ZyOspfIfInfoNbrCount_Object=MibTableColumn
zyOspfIfInfoNbrCount=_ZyOspfIfInfoNbrCount_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,4),_ZyOspfIfInfoNbrCount_Type())
zyOspfIfInfoNbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoNbrCount.setStatus(_A)
_ZyOspfIfInfoAdjacentNbrCount_Type=Integer32
_ZyOspfIfInfoAdjacentNbrCount_Object=MibTableColumn
zyOspfIfInfoAdjacentNbrCount=_ZyOspfIfInfoAdjacentNbrCount_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,5),_ZyOspfIfInfoAdjacentNbrCount_Type())
zyOspfIfInfoAdjacentNbrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoAdjacentNbrCount.setStatus(_A)
_ZyOspfIfInfoHelloDueTime_Type=DisplayString
_ZyOspfIfInfoHelloDueTime_Object=MibTableColumn
zyOspfIfInfoHelloDueTime=_ZyOspfIfInfoHelloDueTime_Object((1,3,6,1,4,1,890,1,15,3,57,2,1,1,6),_ZyOspfIfInfoHelloDueTime_Type())
zyOspfIfInfoHelloDueTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfIfInfoHelloDueTime.setStatus(_A)
_ZyxelOspfNbrTable_Object=MibTable
zyxelOspfNbrTable=_ZyxelOspfNbrTable_Object((1,3,6,1,4,1,890,1,15,3,57,2,2))
if mibBuilder.loadTexts:zyxelOspfNbrTable.setStatus(_A)
_ZyxelOspfNbrEntry_Object=MibTableRow
zyxelOspfNbrEntry=_ZyxelOspfNbrEntry_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1))
zyxelOspfNbrEntry.setIndexNames((0,_C,_O),(0,_C,_N))
if mibBuilder.loadTexts:zyxelOspfNbrEntry.setStatus(_A)
class _ZyOspfNbrRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dr',1),('backup',2),('drOther',3)))
_ZyOspfNbrRole_Type.__name__=_H
_ZyOspfNbrRole_Object=MibTableColumn
zyOspfNbrRole=_ZyOspfNbrRole_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,1),_ZyOspfNbrRole_Type())
zyOspfNbrRole.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrRole.setStatus(_A)
_ZyOspfNbrDeadtime_Type=DisplayString
_ZyOspfNbrDeadtime_Object=MibTableColumn
zyOspfNbrDeadtime=_ZyOspfNbrDeadtime_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,2),_ZyOspfNbrDeadtime_Type())
zyOspfNbrDeadtime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrDeadtime.setStatus(_A)
_ZyOspfNbrInterface_Type=IpAddress
_ZyOspfNbrInterface_Object=MibTableColumn
zyOspfNbrInterface=_ZyOspfNbrInterface_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,3),_ZyOspfNbrInterface_Type())
zyOspfNbrInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrInterface.setStatus(_A)
_ZyOspfNbrRetransmitLSA_Type=Integer32
_ZyOspfNbrRetransmitLSA_Object=MibTableColumn
zyOspfNbrRetransmitLSA=_ZyOspfNbrRetransmitLSA_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,4),_ZyOspfNbrRetransmitLSA_Type())
zyOspfNbrRetransmitLSA.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrRetransmitLSA.setStatus(_A)
_ZyOspfNbrRequestLSA_Type=Integer32
_ZyOspfNbrRequestLSA_Object=MibTableColumn
zyOspfNbrRequestLSA=_ZyOspfNbrRequestLSA_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,5),_ZyOspfNbrRequestLSA_Type())
zyOspfNbrRequestLSA.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrRequestLSA.setStatus(_A)
_ZyOspfNbrDatabaseSummaryLSA_Type=Integer32
_ZyOspfNbrDatabaseSummaryLSA_Object=MibTableColumn
zyOspfNbrDatabaseSummaryLSA=_ZyOspfNbrDatabaseSummaryLSA_Object((1,3,6,1,4,1,890,1,15,3,57,2,2,1,6),_ZyOspfNbrDatabaseSummaryLSA_Type())
zyOspfNbrDatabaseSummaryLSA.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfNbrDatabaseSummaryLSA.setStatus(_A)
_ZyxelOspfLsdbTable_Object=MibTable
zyxelOspfLsdbTable=_ZyxelOspfLsdbTable_Object((1,3,6,1,4,1,890,1,15,3,57,2,3))
if mibBuilder.loadTexts:zyxelOspfLsdbTable.setStatus(_A)
_ZyxelOspfLsdbEntry_Object=MibTableRow
zyxelOspfLsdbEntry=_ZyxelOspfLsdbEntry_Object((1,3,6,1,4,1,890,1,15,3,57,2,3,1))
zyxelOspfLsdbEntry.setIndexNames((0,_C,_J),(0,_C,_M),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:zyxelOspfLsdbEntry.setStatus(_A)
_ZyOspfLsdbLinkCount_Type=Integer32
_ZyOspfLsdbLinkCount_Object=MibTableColumn
zyOspfLsdbLinkCount=_ZyOspfLsdbLinkCount_Object((1,3,6,1,4,1,890,1,15,3,57,2,3,1,1),_ZyOspfLsdbLinkCount_Type())
zyOspfLsdbLinkCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfLsdbLinkCount.setStatus(_A)
_ZyOspfLsdbRouteIpAddress_Type=IpAddress
_ZyOspfLsdbRouteIpAddress_Object=MibTableColumn
zyOspfLsdbRouteIpAddress=_ZyOspfLsdbRouteIpAddress_Object((1,3,6,1,4,1,890,1,15,3,57,2,3,1,2),_ZyOspfLsdbRouteIpAddress_Type())
zyOspfLsdbRouteIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfLsdbRouteIpAddress.setStatus(_A)
_ZyOspfLsdbRouteMaskBits_Type=Integer32
_ZyOspfLsdbRouteMaskBits_Object=MibTableColumn
zyOspfLsdbRouteMaskBits=_ZyOspfLsdbRouteMaskBits_Object((1,3,6,1,4,1,890,1,15,3,57,2,3,1,3),_ZyOspfLsdbRouteMaskBits_Type())
zyOspfLsdbRouteMaskBits.setMaxAccess(_B)
if mibBuilder.loadTexts:zyOspfLsdbRouteMaskBits.setStatus(_A)
_ZyxelOspfNotifications_ObjectIdentity=ObjectIdentity
zyxelOspfNotifications=_ZyxelOspfNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,57,3))
zyOspfExceedMaxDynamicRoutePath=NotificationType((1,3,6,1,4,1,890,1,15,3,57,3,1))
if mibBuilder.loadTexts:zyOspfExceedMaxDynamicRoutePath.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxelOspf':zyxelOspf,'zyxelOspfSetup':zyxelOspfSetup,'zyxelOspfIfTable':zyxelOspfIfTable,'zyxelOspfIfEntry':zyxelOspfIfEntry,'zyOspfIfKeyId':zyOspfIfKeyId,'zyxelOspfAreaTable':zyxelOspfAreaTable,'zyxelOspfAreaEntry':zyxelOspfAreaEntry,'zyOspfAreaName':zyOspfAreaName,'zyOspfAreaDefaultRouteMetric':zyOspfAreaDefaultRouteMetric,'zyxelOspfRedistributeRouteTable':zyxelOspfRedistributeRouteTable,'zyxelOspfRedistributeRouteEntry':zyxelOspfRedistributeRouteEntry,_R:zyOspfRedistributeRouteProtocol,'zyOspfRedistributeRouteState':zyOspfRedistributeRouteState,'zyOspfRedistributeRouteType':zyOspfRedistributeRouteType,'zyOspfRedistributeRouteMetric':zyOspfRedistributeRouteMetric,'zyxelOspfVirtualLinkTable':zyxelOspfVirtualLinkTable,'zyxelOspfVirtualLinkEntry':zyxelOspfVirtualLinkEntry,'zyOspfVirtualLinkName':zyOspfVirtualLinkName,'zyOspfVirtualLinkKeyId':zyOspfVirtualLinkKeyId,'zyOspfMaxNumberOfSummaryAddress':zyOspfMaxNumberOfSummaryAddress,'zyxelOspfSummaryAddressTable':zyxelOspfSummaryAddressTable,'zyxelOspfSummaryAddressEntry':zyxelOspfSummaryAddressEntry,_S:zyOspfSummaryAddressIpAddress,_T:zyOspfSummaryAddressMaskBits,'zyOspfSummaryAddressRowStatus':zyOspfSummaryAddressRowStatus,'zyxelOspfGeneralGroup':zyxelOspfGeneralGroup,'zyOspfDistance':zyOspfDistance,'zyOspfDefaultInformationOriginateState':zyOspfDefaultInformationOriginateState,'zyOspfDefaultInformationOriginateAlways':zyOspfDefaultInformationOriginateAlways,'zyOspfDefaultInformationOriginateMetric':zyOspfDefaultInformationOriginateMetric,'zyOspfDefaultInformationOriginateMetricType':zyOspfDefaultInformationOriginateMetricType,'zyxelOspfStatus':zyxelOspfStatus,'zyxelOspfIfInfoTable':zyxelOspfIfInfoTable,'zyxelOspfIfInfoEntry':zyxelOspfIfInfoEntry,'zyOspfIfInfoMaskbits':zyOspfIfInfoMaskbits,'zyOspfIfInfoDesignatedRouterID':zyOspfIfInfoDesignatedRouterID,'zyOspfIfInfoBackupDesignatedRouterID':zyOspfIfInfoBackupDesignatedRouterID,'zyOspfIfInfoNbrCount':zyOspfIfInfoNbrCount,'zyOspfIfInfoAdjacentNbrCount':zyOspfIfInfoAdjacentNbrCount,'zyOspfIfInfoHelloDueTime':zyOspfIfInfoHelloDueTime,'zyxelOspfNbrTable':zyxelOspfNbrTable,'zyxelOspfNbrEntry':zyxelOspfNbrEntry,'zyOspfNbrRole':zyOspfNbrRole,'zyOspfNbrDeadtime':zyOspfNbrDeadtime,'zyOspfNbrInterface':zyOspfNbrInterface,'zyOspfNbrRetransmitLSA':zyOspfNbrRetransmitLSA,'zyOspfNbrRequestLSA':zyOspfNbrRequestLSA,'zyOspfNbrDatabaseSummaryLSA':zyOspfNbrDatabaseSummaryLSA,'zyxelOspfLsdbTable':zyxelOspfLsdbTable,'zyxelOspfLsdbEntry':zyxelOspfLsdbEntry,'zyOspfLsdbLinkCount':zyOspfLsdbLinkCount,'zyOspfLsdbRouteIpAddress':zyOspfLsdbRouteIpAddress,'zyOspfLsdbRouteMaskBits':zyOspfLsdbRouteMaskBits,'zyxelOspfNotifications':zyxelOspfNotifications,'zyOspfExceedMaxDynamicRoutePath':zyOspfExceedMaxDynamicRoutePath})