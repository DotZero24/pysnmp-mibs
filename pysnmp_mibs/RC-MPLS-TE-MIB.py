_d='rcMplsLspDown'
_c='rcMplsLspUp'
_b='rcMplsTETunnelGroupCfgPrimaryTunnelID'
_a='rcMplsTEHotStandbyCfgProtOptNo'
_Z='rcMplsTEHotStandbyCfgTunnelID'
_Y='rcMplsTEExplicitRouteIDCfgIndex'
_X='rcMplsTEExplicitRouteIDCfgIdentifer'
_W='routerid'
_V='interface'
_U='strict'
_T='exclude'
_S='include'
_R='rcMplsTEExplicitRouteNameCfgIndex'
_Q='rcMplsTEExplicitRouteNameCfgName'
_P='rcMplsTEExplicitPathIDCfgIdentifer'
_O='rcMplsTEExplicitPathNameCfgName'
_N='explicitName'
_M='explicitId'
_L='dynamic'
_K='rcMplsTEPathOptCfgNumber'
_J='rcMplsTEPathOptCfgTunnelID'
_I='rcMplsTETunnelCfgTunnelID'
_H='rcMplsTunnelOperStatus'
_G='DisplayString'
_F='not-accessible'
_E='Integer32'
_D='Unsigned32'
_C='RC-MPLS-TE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rc,=mibBuilder.importSymbols('RC-SMI','rc')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention')
rcMplsTeMIB=ModuleIdentity((1,3,6,1,4,1,65000,1))
if mibBuilder.loadTexts:rcMplsTeMIB.setRevisions(('2012-12-11 00:00',))
_RcMplsTeNotifications_ObjectIdentity=ObjectIdentity
rcMplsTeNotifications=_RcMplsTeNotifications_ObjectIdentity((1,3,6,1,4,1,65000,1,0))
_RcMplsTETunnelCfgTable_Object=MibTable
rcMplsTETunnelCfgTable=_RcMplsTETunnelCfgTable_Object((1,3,6,1,4,1,65000,1,1))
if mibBuilder.loadTexts:rcMplsTETunnelCfgTable.setStatus(_A)
_RcMplsTETunnelCfgEntry_Object=MibTableRow
rcMplsTETunnelCfgEntry=_RcMplsTETunnelCfgEntry_Object((1,3,6,1,4,1,65000,1,1,1))
rcMplsTETunnelCfgEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:rcMplsTETunnelCfgEntry.setStatus(_A)
class _RcMplsTETunnelCfgTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcMplsTETunnelCfgTunnelID_Type.__name__=_D
_RcMplsTETunnelCfgTunnelID_Object=MibTableColumn
rcMplsTETunnelCfgTunnelID=_RcMplsTETunnelCfgTunnelID_Object((1,3,6,1,4,1,65000,1,1,1,1),_RcMplsTETunnelCfgTunnelID_Type())
rcMplsTETunnelCfgTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTETunnelCfgTunnelID.setStatus(_A)
_RcMplsTETunnelCfgEgressLSRId_Type=IpAddress
_RcMplsTETunnelCfgEgressLSRId_Object=MibTableColumn
rcMplsTETunnelCfgEgressLSRId=_RcMplsTETunnelCfgEgressLSRId_Object((1,3,6,1,4,1,65000,1,1,1,2),_RcMplsTETunnelCfgEgressLSRId_Type())
rcMplsTETunnelCfgEgressLSRId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgEgressLSRId.setStatus(_A)
class _RcMplsTETunnelCfgSetupPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcMplsTETunnelCfgSetupPrio_Type.__name__=_E
_RcMplsTETunnelCfgSetupPrio_Object=MibTableColumn
rcMplsTETunnelCfgSetupPrio=_RcMplsTETunnelCfgSetupPrio_Object((1,3,6,1,4,1,65000,1,1,1,3),_RcMplsTETunnelCfgSetupPrio_Type())
rcMplsTETunnelCfgSetupPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgSetupPrio.setStatus(_A)
class _RcMplsTETunnelCfgHoldingPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcMplsTETunnelCfgHoldingPrio_Type.__name__=_E
_RcMplsTETunnelCfgHoldingPrio_Object=MibTableColumn
rcMplsTETunnelCfgHoldingPrio=_RcMplsTETunnelCfgHoldingPrio_Object((1,3,6,1,4,1,65000,1,1,1,4),_RcMplsTETunnelCfgHoldingPrio_Type())
rcMplsTETunnelCfgHoldingPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgHoldingPrio.setStatus(_A)
class _RcMplsTETunnelCfgRecordRoute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_RcMplsTETunnelCfgRecordRoute_Type.__name__=_E
_RcMplsTETunnelCfgRecordRoute_Object=MibTableColumn
rcMplsTETunnelCfgRecordRoute=_RcMplsTETunnelCfgRecordRoute_Object((1,3,6,1,4,1,65000,1,1,1,5),_RcMplsTETunnelCfgRecordRoute_Type())
rcMplsTETunnelCfgRecordRoute.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgRecordRoute.setStatus(_A)
_RcMplsTETunnelCfgBandwidth_Type=Unsigned32
_RcMplsTETunnelCfgBandwidth_Object=MibTableColumn
rcMplsTETunnelCfgBandwidth=_RcMplsTETunnelCfgBandwidth_Object((1,3,6,1,4,1,65000,1,1,1,6),_RcMplsTETunnelCfgBandwidth_Type())
rcMplsTETunnelCfgBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgBandwidth.setStatus(_A)
class _RcMplsTETunnelCfgExplicitPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_RcMplsTETunnelCfgExplicitPathName_Type.__name__=_G
_RcMplsTETunnelCfgExplicitPathName_Object=MibTableColumn
rcMplsTETunnelCfgExplicitPathName=_RcMplsTETunnelCfgExplicitPathName_Object((1,3,6,1,4,1,65000,1,1,1,7),_RcMplsTETunnelCfgExplicitPathName_Type())
rcMplsTETunnelCfgExplicitPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgExplicitPathName.setStatus(_A)
class _RcMplsTETunnelCfgExplicitPathID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcMplsTETunnelCfgExplicitPathID_Type.__name__=_D
_RcMplsTETunnelCfgExplicitPathID_Object=MibTableColumn
rcMplsTETunnelCfgExplicitPathID=_RcMplsTETunnelCfgExplicitPathID_Object((1,3,6,1,4,1,65000,1,1,1,8),_RcMplsTETunnelCfgExplicitPathID_Type())
rcMplsTETunnelCfgExplicitPathID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgExplicitPathID.setStatus(_A)
class _RcMplsTETunnelCfgHSB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_RcMplsTETunnelCfgHSB_Type.__name__=_E
_RcMplsTETunnelCfgHSB_Object=MibTableColumn
rcMplsTETunnelCfgHSB=_RcMplsTETunnelCfgHSB_Object((1,3,6,1,4,1,65000,1,1,1,9),_RcMplsTETunnelCfgHSB_Type())
rcMplsTETunnelCfgHSB.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgHSB.setStatus(_A)
class _RcMplsTETunnelCfgHSBExplicitPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,129))
_RcMplsTETunnelCfgHSBExplicitPathName_Type.__name__=_G
_RcMplsTETunnelCfgHSBExplicitPathName_Object=MibTableColumn
rcMplsTETunnelCfgHSBExplicitPathName=_RcMplsTETunnelCfgHSBExplicitPathName_Object((1,3,6,1,4,1,65000,1,1,1,10),_RcMplsTETunnelCfgHSBExplicitPathName_Type())
rcMplsTETunnelCfgHSBExplicitPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgHSBExplicitPathName.setStatus(_A)
class _RcMplsTETunnelCfgHSBExplicitPathID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcMplsTETunnelCfgHSBExplicitPathID_Type.__name__=_D
_RcMplsTETunnelCfgHSBExplicitPathID_Object=MibTableColumn
rcMplsTETunnelCfgHSBExplicitPathID=_RcMplsTETunnelCfgHSBExplicitPathID_Object((1,3,6,1,4,1,65000,1,1,1,11),_RcMplsTETunnelCfgHSBExplicitPathID_Type())
rcMplsTETunnelCfgHSBExplicitPathID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgHSBExplicitPathID.setStatus(_A)
_RcMplsTETunnelCfgRowSta_Type=RowStatus
_RcMplsTETunnelCfgRowSta_Object=MibTableColumn
rcMplsTETunnelCfgRowSta=_RcMplsTETunnelCfgRowSta_Object((1,3,6,1,4,1,65000,1,1,1,12),_RcMplsTETunnelCfgRowSta_Type())
rcMplsTETunnelCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelCfgRowSta.setStatus(_A)
class _RcMplsTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_RcMplsTunnelOperStatus_Type.__name__=_E
_RcMplsTunnelOperStatus_Object=MibTableColumn
rcMplsTunnelOperStatus=_RcMplsTunnelOperStatus_Object((1,3,6,1,4,1,65000,1,1,1,13),_RcMplsTunnelOperStatus_Type())
rcMplsTunnelOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rcMplsTunnelOperStatus.setStatus(_A)
_RcMplsTEPathOptCfgTable_Object=MibTable
rcMplsTEPathOptCfgTable=_RcMplsTEPathOptCfgTable_Object((1,3,6,1,4,1,65000,1,2))
if mibBuilder.loadTexts:rcMplsTEPathOptCfgTable.setStatus(_A)
_RcMplsTEPathOptCfgEntry_Object=MibTableRow
rcMplsTEPathOptCfgEntry=_RcMplsTEPathOptCfgEntry_Object((1,3,6,1,4,1,65000,1,2,1))
rcMplsTEPathOptCfgEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:rcMplsTEPathOptCfgEntry.setStatus(_A)
class _RcMplsTEPathOptCfgTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcMplsTEPathOptCfgTunnelID_Type.__name__=_D
_RcMplsTEPathOptCfgTunnelID_Object=MibTableColumn
rcMplsTEPathOptCfgTunnelID=_RcMplsTEPathOptCfgTunnelID_Object((1,3,6,1,4,1,65000,1,2,1,1),_RcMplsTEPathOptCfgTunnelID_Type())
rcMplsTEPathOptCfgTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgTunnelID.setStatus(_A)
class _RcMplsTEPathOptCfgNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RcMplsTEPathOptCfgNumber_Type.__name__=_D
_RcMplsTEPathOptCfgNumber_Object=MibTableColumn
rcMplsTEPathOptCfgNumber=_RcMplsTEPathOptCfgNumber_Object((1,3,6,1,4,1,65000,1,2,1,2),_RcMplsTEPathOptCfgNumber_Type())
rcMplsTEPathOptCfgNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgNumber.setStatus(_A)
class _RcMplsTEPathOptCfgPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_RcMplsTEPathOptCfgPathType_Type.__name__=_E
_RcMplsTEPathOptCfgPathType_Object=MibTableColumn
rcMplsTEPathOptCfgPathType=_RcMplsTEPathOptCfgPathType_Object((1,3,6,1,4,1,65000,1,2,1,3),_RcMplsTEPathOptCfgPathType_Type())
rcMplsTEPathOptCfgPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgPathType.setStatus(_A)
class _RcMplsTEPathOptCfgExpPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,129))
_RcMplsTEPathOptCfgExpPathName_Type.__name__=_G
_RcMplsTEPathOptCfgExpPathName_Object=MibTableColumn
rcMplsTEPathOptCfgExpPathName=_RcMplsTEPathOptCfgExpPathName_Object((1,3,6,1,4,1,65000,1,2,1,4),_RcMplsTEPathOptCfgExpPathName_Type())
rcMplsTEPathOptCfgExpPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgExpPathName.setStatus(_A)
class _RcMplsTEPathOptCfgExpPathID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_RcMplsTEPathOptCfgExpPathID_Type.__name__=_D
_RcMplsTEPathOptCfgExpPathID_Object=MibTableColumn
rcMplsTEPathOptCfgExpPathID=_RcMplsTEPathOptCfgExpPathID_Object((1,3,6,1,4,1,65000,1,2,1,5),_RcMplsTEPathOptCfgExpPathID_Type())
rcMplsTEPathOptCfgExpPathID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgExpPathID.setStatus(_A)
_RcMplsTEPathOptCfgRowSta_Type=RowStatus
_RcMplsTEPathOptCfgRowSta_Object=MibTableColumn
rcMplsTEPathOptCfgRowSta=_RcMplsTEPathOptCfgRowSta_Object((1,3,6,1,4,1,65000,1,2,1,6),_RcMplsTEPathOptCfgRowSta_Type())
rcMplsTEPathOptCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEPathOptCfgRowSta.setStatus(_A)
_RcMplsTEExplicitPathNameCfgTable_Object=MibTable
rcMplsTEExplicitPathNameCfgTable=_RcMplsTEExplicitPathNameCfgTable_Object((1,3,6,1,4,1,65000,1,3))
if mibBuilder.loadTexts:rcMplsTEExplicitPathNameCfgTable.setStatus(_A)
_RcMplsTEExplicitPathNameCfgEntry_Object=MibTableRow
rcMplsTEExplicitPathNameCfgEntry=_RcMplsTEExplicitPathNameCfgEntry_Object((1,3,6,1,4,1,65000,1,3,1))
rcMplsTEExplicitPathNameCfgEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:rcMplsTEExplicitPathNameCfgEntry.setStatus(_A)
class _RcMplsTEExplicitPathNameCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,129))
_RcMplsTEExplicitPathNameCfgName_Type.__name__=_G
_RcMplsTEExplicitPathNameCfgName_Object=MibTableColumn
rcMplsTEExplicitPathNameCfgName=_RcMplsTEExplicitPathNameCfgName_Object((1,3,6,1,4,1,65000,1,3,1,1),_RcMplsTEExplicitPathNameCfgName_Type())
rcMplsTEExplicitPathNameCfgName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitPathNameCfgName.setStatus(_A)
_RcMplsTEExplicitPathNameCfgRowSta_Type=RowStatus
_RcMplsTEExplicitPathNameCfgRowSta_Object=MibTableColumn
rcMplsTEExplicitPathNameCfgRowSta=_RcMplsTEExplicitPathNameCfgRowSta_Object((1,3,6,1,4,1,65000,1,3,1,2),_RcMplsTEExplicitPathNameCfgRowSta_Type())
rcMplsTEExplicitPathNameCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitPathNameCfgRowSta.setStatus(_A)
_RcMplsTEExplicitPathIDCfgTable_Object=MibTable
rcMplsTEExplicitPathIDCfgTable=_RcMplsTEExplicitPathIDCfgTable_Object((1,3,6,1,4,1,65000,1,4))
if mibBuilder.loadTexts:rcMplsTEExplicitPathIDCfgTable.setStatus(_A)
_RcMplsTEExplicitPathIDCfgEntry_Object=MibTableRow
rcMplsTEExplicitPathIDCfgEntry=_RcMplsTEExplicitPathIDCfgEntry_Object((1,3,6,1,4,1,65000,1,4,1))
rcMplsTEExplicitPathIDCfgEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:rcMplsTEExplicitPathIDCfgEntry.setStatus(_A)
class _RcMplsTEExplicitPathIDCfgIdentifer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcMplsTEExplicitPathIDCfgIdentifer_Type.__name__=_D
_RcMplsTEExplicitPathIDCfgIdentifer_Object=MibTableColumn
rcMplsTEExplicitPathIDCfgIdentifer=_RcMplsTEExplicitPathIDCfgIdentifer_Object((1,3,6,1,4,1,65000,1,4,1,1),_RcMplsTEExplicitPathIDCfgIdentifer_Type())
rcMplsTEExplicitPathIDCfgIdentifer.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitPathIDCfgIdentifer.setStatus(_A)
_RcMplsTEExplicitPathIDCfgRowSta_Type=RowStatus
_RcMplsTEExplicitPathIDCfgRowSta_Object=MibTableColumn
rcMplsTEExplicitPathIDCfgRowSta=_RcMplsTEExplicitPathIDCfgRowSta_Object((1,3,6,1,4,1,65000,1,4,1,2),_RcMplsTEExplicitPathIDCfgRowSta_Type())
rcMplsTEExplicitPathIDCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitPathIDCfgRowSta.setStatus(_A)
_RcMplsTEExplicitRouteNameCfgTable_Object=MibTable
rcMplsTEExplicitRouteNameCfgTable=_RcMplsTEExplicitRouteNameCfgTable_Object((1,3,6,1,4,1,65000,1,5))
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgTable.setStatus(_A)
_RcMplsTEExplicitRouteNameCfgEntry_Object=MibTableRow
rcMplsTEExplicitRouteNameCfgEntry=_RcMplsTEExplicitRouteNameCfgEntry_Object((1,3,6,1,4,1,65000,1,5,1))
rcMplsTEExplicitRouteNameCfgEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgEntry.setStatus(_A)
class _RcMplsTEExplicitRouteNameCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,129))
_RcMplsTEExplicitRouteNameCfgName_Type.__name__=_G
_RcMplsTEExplicitRouteNameCfgName_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgName=_RcMplsTEExplicitRouteNameCfgName_Object((1,3,6,1,4,1,65000,1,5,1,1),_RcMplsTEExplicitRouteNameCfgName_Type())
rcMplsTEExplicitRouteNameCfgName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgName.setStatus(_A)
class _RcMplsTEExplicitRouteNameCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_RcMplsTEExplicitRouteNameCfgIndex_Type.__name__=_D
_RcMplsTEExplicitRouteNameCfgIndex_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgIndex=_RcMplsTEExplicitRouteNameCfgIndex_Object((1,3,6,1,4,1,65000,1,5,1,2),_RcMplsTEExplicitRouteNameCfgIndex_Type())
rcMplsTEExplicitRouteNameCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgIndex.setStatus(_A)
_RcMplsTEExplicitRouteNameCfgNextIP_Type=IpAddress
_RcMplsTEExplicitRouteNameCfgNextIP_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgNextIP=_RcMplsTEExplicitRouteNameCfgNextIP_Object((1,3,6,1,4,1,65000,1,5,1,3),_RcMplsTEExplicitRouteNameCfgNextIP_Type())
rcMplsTEExplicitRouteNameCfgNextIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgNextIP.setStatus(_A)
class _RcMplsTEExplicitRouteNameCfgHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_RcMplsTEExplicitRouteNameCfgHopType_Type.__name__=_E
_RcMplsTEExplicitRouteNameCfgHopType_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgHopType=_RcMplsTEExplicitRouteNameCfgHopType_Object((1,3,6,1,4,1,65000,1,5,1,4),_RcMplsTEExplicitRouteNameCfgHopType_Type())
rcMplsTEExplicitRouteNameCfgHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgHopType.setStatus(_A)
class _RcMplsTEExplicitRouteNameCfgHopAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('loose',2),(_V,3),(_W,4)))
_RcMplsTEExplicitRouteNameCfgHopAttribute_Type.__name__=_E
_RcMplsTEExplicitRouteNameCfgHopAttribute_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgHopAttribute=_RcMplsTEExplicitRouteNameCfgHopAttribute_Object((1,3,6,1,4,1,65000,1,5,1,5),_RcMplsTEExplicitRouteNameCfgHopAttribute_Type())
rcMplsTEExplicitRouteNameCfgHopAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgHopAttribute.setStatus(_A)
_RcMplsTEExplicitRouteNameCfgRowSta_Type=RowStatus
_RcMplsTEExplicitRouteNameCfgRowSta_Object=MibTableColumn
rcMplsTEExplicitRouteNameCfgRowSta=_RcMplsTEExplicitRouteNameCfgRowSta_Object((1,3,6,1,4,1,65000,1,5,1,6),_RcMplsTEExplicitRouteNameCfgRowSta_Type())
rcMplsTEExplicitRouteNameCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteNameCfgRowSta.setStatus(_A)
_RcMplsTEExplicitRouteIDCfgTable_Object=MibTable
rcMplsTEExplicitRouteIDCfgTable=_RcMplsTEExplicitRouteIDCfgTable_Object((1,3,6,1,4,1,65000,1,6))
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgTable.setStatus(_A)
_RcMplsTEExplicitRouteIDCfgEntry_Object=MibTableRow
rcMplsTEExplicitRouteIDCfgEntry=_RcMplsTEExplicitRouteIDCfgEntry_Object((1,3,6,1,4,1,65000,1,6,1))
rcMplsTEExplicitRouteIDCfgEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgEntry.setStatus(_A)
class _RcMplsTEExplicitRouteIDCfgIdentifer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcMplsTEExplicitRouteIDCfgIdentifer_Type.__name__=_D
_RcMplsTEExplicitRouteIDCfgIdentifer_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgIdentifer=_RcMplsTEExplicitRouteIDCfgIdentifer_Object((1,3,6,1,4,1,65000,1,6,1,1),_RcMplsTEExplicitRouteIDCfgIdentifer_Type())
rcMplsTEExplicitRouteIDCfgIdentifer.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgIdentifer.setStatus(_A)
class _RcMplsTEExplicitRouteIDCfgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_RcMplsTEExplicitRouteIDCfgIndex_Type.__name__=_D
_RcMplsTEExplicitRouteIDCfgIndex_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgIndex=_RcMplsTEExplicitRouteIDCfgIndex_Object((1,3,6,1,4,1,65000,1,6,1,2),_RcMplsTEExplicitRouteIDCfgIndex_Type())
rcMplsTEExplicitRouteIDCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgIndex.setStatus(_A)
_RcMplsTEExplicitRouteIDCfgNextIP_Type=IpAddress
_RcMplsTEExplicitRouteIDCfgNextIP_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgNextIP=_RcMplsTEExplicitRouteIDCfgNextIP_Object((1,3,6,1,4,1,65000,1,6,1,3),_RcMplsTEExplicitRouteIDCfgNextIP_Type())
rcMplsTEExplicitRouteIDCfgNextIP.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgNextIP.setStatus(_A)
class _RcMplsTEExplicitRouteIDCfgHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_RcMplsTEExplicitRouteIDCfgHopType_Type.__name__=_E
_RcMplsTEExplicitRouteIDCfgHopType_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgHopType=_RcMplsTEExplicitRouteIDCfgHopType_Object((1,3,6,1,4,1,65000,1,6,1,4),_RcMplsTEExplicitRouteIDCfgHopType_Type())
rcMplsTEExplicitRouteIDCfgHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgHopType.setStatus(_A)
class _RcMplsTEExplicitRouteIDCfgHopAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),('loose',2),(_V,3),(_W,4)))
_RcMplsTEExplicitRouteIDCfgHopAttribute_Type.__name__=_E
_RcMplsTEExplicitRouteIDCfgHopAttribute_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgHopAttribute=_RcMplsTEExplicitRouteIDCfgHopAttribute_Object((1,3,6,1,4,1,65000,1,6,1,5),_RcMplsTEExplicitRouteIDCfgHopAttribute_Type())
rcMplsTEExplicitRouteIDCfgHopAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgHopAttribute.setStatus(_A)
_RcMplsTEExplicitRouteIDCfgRowSta_Type=RowStatus
_RcMplsTEExplicitRouteIDCfgRowSta_Object=MibTableColumn
rcMplsTEExplicitRouteIDCfgRowSta=_RcMplsTEExplicitRouteIDCfgRowSta_Object((1,3,6,1,4,1,65000,1,6,1,6),_RcMplsTEExplicitRouteIDCfgRowSta_Type())
rcMplsTEExplicitRouteIDCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEExplicitRouteIDCfgRowSta.setStatus(_A)
_RcMplsTEHotStandbyCfgTable_Object=MibTable
rcMplsTEHotStandbyCfgTable=_RcMplsTEHotStandbyCfgTable_Object((1,3,6,1,4,1,65000,1,7))
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgTable.setStatus(_A)
_RcMplsTEHotStandbyCfgEntry_Object=MibTableRow
rcMplsTEHotStandbyCfgEntry=_RcMplsTEHotStandbyCfgEntry_Object((1,3,6,1,4,1,65000,1,7,1))
rcMplsTEHotStandbyCfgEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgEntry.setStatus(_A)
class _RcMplsTEHotStandbyCfgTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcMplsTEHotStandbyCfgTunnelID_Type.__name__=_D
_RcMplsTEHotStandbyCfgTunnelID_Object=MibTableColumn
rcMplsTEHotStandbyCfgTunnelID=_RcMplsTEHotStandbyCfgTunnelID_Object((1,3,6,1,4,1,65000,1,7,1,1),_RcMplsTEHotStandbyCfgTunnelID_Type())
rcMplsTEHotStandbyCfgTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgTunnelID.setStatus(_A)
class _RcMplsTEHotStandbyCfgProtOptNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_RcMplsTEHotStandbyCfgProtOptNo_Type.__name__=_D
_RcMplsTEHotStandbyCfgProtOptNo_Object=MibTableColumn
rcMplsTEHotStandbyCfgProtOptNo=_RcMplsTEHotStandbyCfgProtOptNo_Object((1,3,6,1,4,1,65000,1,7,1,2),_RcMplsTEHotStandbyCfgProtOptNo_Type())
rcMplsTEHotStandbyCfgProtOptNo.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgProtOptNo.setStatus(_A)
class _RcMplsTEHotStandbyCfgPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_RcMplsTEHotStandbyCfgPathType_Type.__name__=_E
_RcMplsTEHotStandbyCfgPathType_Object=MibTableColumn
rcMplsTEHotStandbyCfgPathType=_RcMplsTEHotStandbyCfgPathType_Object((1,3,6,1,4,1,65000,1,7,1,3),_RcMplsTEHotStandbyCfgPathType_Type())
rcMplsTEHotStandbyCfgPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgPathType.setStatus(_A)
class _RcMplsTEHotStandbyCfgExpPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,129))
_RcMplsTEHotStandbyCfgExpPathName_Type.__name__=_G
_RcMplsTEHotStandbyCfgExpPathName_Object=MibTableColumn
rcMplsTEHotStandbyCfgExpPathName=_RcMplsTEHotStandbyCfgExpPathName_Object((1,3,6,1,4,1,65000,1,7,1,4),_RcMplsTEHotStandbyCfgExpPathName_Type())
rcMplsTEHotStandbyCfgExpPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgExpPathName.setStatus(_A)
class _RcMplsTEHotStandbyCfgExpPathID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcMplsTEHotStandbyCfgExpPathID_Type.__name__=_D
_RcMplsTEHotStandbyCfgExpPathID_Object=MibTableColumn
rcMplsTEHotStandbyCfgExpPathID=_RcMplsTEHotStandbyCfgExpPathID_Object((1,3,6,1,4,1,65000,1,7,1,5),_RcMplsTEHotStandbyCfgExpPathID_Type())
rcMplsTEHotStandbyCfgExpPathID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgExpPathID.setStatus(_A)
_RcMplsTEHotStandbyCfgRowSta_Type=RowStatus
_RcMplsTEHotStandbyCfgRowSta_Object=MibTableColumn
rcMplsTEHotStandbyCfgRowSta=_RcMplsTEHotStandbyCfgRowSta_Object((1,3,6,1,4,1,65000,1,7,1,6),_RcMplsTEHotStandbyCfgRowSta_Type())
rcMplsTEHotStandbyCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTEHotStandbyCfgRowSta.setStatus(_A)
_RcMplsTETunnelGroupCfgTable_Object=MibTable
rcMplsTETunnelGroupCfgTable=_RcMplsTETunnelGroupCfgTable_Object((1,3,6,1,4,1,65000,1,8))
if mibBuilder.loadTexts:rcMplsTETunnelGroupCfgTable.setStatus(_A)
_RcMplsTETunnelGroupCfgEntry_Object=MibTableRow
rcMplsTETunnelGroupCfgEntry=_RcMplsTETunnelGroupCfgEntry_Object((1,3,6,1,4,1,65000,1,8,1))
rcMplsTETunnelGroupCfgEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:rcMplsTETunnelGroupCfgEntry.setStatus(_A)
class _RcMplsTETunnelGroupCfgPrimaryTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcMplsTETunnelGroupCfgPrimaryTunnelID_Type.__name__=_D
_RcMplsTETunnelGroupCfgPrimaryTunnelID_Object=MibTableColumn
rcMplsTETunnelGroupCfgPrimaryTunnelID=_RcMplsTETunnelGroupCfgPrimaryTunnelID_Object((1,3,6,1,4,1,65000,1,8,1,1),_RcMplsTETunnelGroupCfgPrimaryTunnelID_Type())
rcMplsTETunnelGroupCfgPrimaryTunnelID.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMplsTETunnelGroupCfgPrimaryTunnelID.setStatus(_A)
class _RcMplsTETunnelGroupCfgSecondaryTunnelID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_RcMplsTETunnelGroupCfgSecondaryTunnelID_Type.__name__=_D
_RcMplsTETunnelGroupCfgSecondaryTunnelID_Object=MibTableColumn
rcMplsTETunnelGroupCfgSecondaryTunnelID=_RcMplsTETunnelGroupCfgSecondaryTunnelID_Object((1,3,6,1,4,1,65000,1,8,1,2),_RcMplsTETunnelGroupCfgSecondaryTunnelID_Type())
rcMplsTETunnelGroupCfgSecondaryTunnelID.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelGroupCfgSecondaryTunnelID.setStatus(_A)
_RcMplsTETunnelGroupCfgRowSta_Type=RowStatus
_RcMplsTETunnelGroupCfgRowSta_Object=MibTableColumn
rcMplsTETunnelGroupCfgRowSta=_RcMplsTETunnelGroupCfgRowSta_Object((1,3,6,1,4,1,65000,1,8,1,3),_RcMplsTETunnelGroupCfgRowSta_Type())
rcMplsTETunnelGroupCfgRowSta.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMplsTETunnelGroupCfgRowSta.setStatus(_A)
_RcMplsTeConformance_ObjectIdentity=ObjectIdentity
rcMplsTeConformance=_RcMplsTeConformance_ObjectIdentity((1,3,6,1,4,1,65000,1,9))
_RcMplsTeGroups_ObjectIdentity=ObjectIdentity
rcMplsTeGroups=_RcMplsTeGroups_ObjectIdentity((1,3,6,1,4,1,65000,1,9,1))
rcMplsLspUp=NotificationType((1,3,6,1,4,1,65000,1,0,1))
rcMplsLspUp.setObjects((_C,_H))
if mibBuilder.loadTexts:rcMplsLspUp.setStatus(_A)
rcMplsLspDown=NotificationType((1,3,6,1,4,1,65000,1,0,2))
rcMplsLspDown.setObjects((_C,_H))
if mibBuilder.loadTexts:rcMplsLspDown.setStatus(_A)
rcMplsTeNotificationGroup=NotificationGroup((1,3,6,1,4,1,65000,1,9,1,8))
rcMplsTeNotificationGroup.setObjects(*((_C,_c),(_C,_d)))
if mibBuilder.loadTexts:rcMplsTeNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcMplsTeMIB':rcMplsTeMIB,'rcMplsTeNotifications':rcMplsTeNotifications,_c:rcMplsLspUp,_d:rcMplsLspDown,'rcMplsTETunnelCfgTable':rcMplsTETunnelCfgTable,'rcMplsTETunnelCfgEntry':rcMplsTETunnelCfgEntry,_I:rcMplsTETunnelCfgTunnelID,'rcMplsTETunnelCfgEgressLSRId':rcMplsTETunnelCfgEgressLSRId,'rcMplsTETunnelCfgSetupPrio':rcMplsTETunnelCfgSetupPrio,'rcMplsTETunnelCfgHoldingPrio':rcMplsTETunnelCfgHoldingPrio,'rcMplsTETunnelCfgRecordRoute':rcMplsTETunnelCfgRecordRoute,'rcMplsTETunnelCfgBandwidth':rcMplsTETunnelCfgBandwidth,'rcMplsTETunnelCfgExplicitPathName':rcMplsTETunnelCfgExplicitPathName,'rcMplsTETunnelCfgExplicitPathID':rcMplsTETunnelCfgExplicitPathID,'rcMplsTETunnelCfgHSB':rcMplsTETunnelCfgHSB,'rcMplsTETunnelCfgHSBExplicitPathName':rcMplsTETunnelCfgHSBExplicitPathName,'rcMplsTETunnelCfgHSBExplicitPathID':rcMplsTETunnelCfgHSBExplicitPathID,'rcMplsTETunnelCfgRowSta':rcMplsTETunnelCfgRowSta,_H:rcMplsTunnelOperStatus,'rcMplsTEPathOptCfgTable':rcMplsTEPathOptCfgTable,'rcMplsTEPathOptCfgEntry':rcMplsTEPathOptCfgEntry,_J:rcMplsTEPathOptCfgTunnelID,_K:rcMplsTEPathOptCfgNumber,'rcMplsTEPathOptCfgPathType':rcMplsTEPathOptCfgPathType,'rcMplsTEPathOptCfgExpPathName':rcMplsTEPathOptCfgExpPathName,'rcMplsTEPathOptCfgExpPathID':rcMplsTEPathOptCfgExpPathID,'rcMplsTEPathOptCfgRowSta':rcMplsTEPathOptCfgRowSta,'rcMplsTEExplicitPathNameCfgTable':rcMplsTEExplicitPathNameCfgTable,'rcMplsTEExplicitPathNameCfgEntry':rcMplsTEExplicitPathNameCfgEntry,_O:rcMplsTEExplicitPathNameCfgName,'rcMplsTEExplicitPathNameCfgRowSta':rcMplsTEExplicitPathNameCfgRowSta,'rcMplsTEExplicitPathIDCfgTable':rcMplsTEExplicitPathIDCfgTable,'rcMplsTEExplicitPathIDCfgEntry':rcMplsTEExplicitPathIDCfgEntry,_P:rcMplsTEExplicitPathIDCfgIdentifer,'rcMplsTEExplicitPathIDCfgRowSta':rcMplsTEExplicitPathIDCfgRowSta,'rcMplsTEExplicitRouteNameCfgTable':rcMplsTEExplicitRouteNameCfgTable,'rcMplsTEExplicitRouteNameCfgEntry':rcMplsTEExplicitRouteNameCfgEntry,_Q:rcMplsTEExplicitRouteNameCfgName,_R:rcMplsTEExplicitRouteNameCfgIndex,'rcMplsTEExplicitRouteNameCfgNextIP':rcMplsTEExplicitRouteNameCfgNextIP,'rcMplsTEExplicitRouteNameCfgHopType':rcMplsTEExplicitRouteNameCfgHopType,'rcMplsTEExplicitRouteNameCfgHopAttribute':rcMplsTEExplicitRouteNameCfgHopAttribute,'rcMplsTEExplicitRouteNameCfgRowSta':rcMplsTEExplicitRouteNameCfgRowSta,'rcMplsTEExplicitRouteIDCfgTable':rcMplsTEExplicitRouteIDCfgTable,'rcMplsTEExplicitRouteIDCfgEntry':rcMplsTEExplicitRouteIDCfgEntry,_X:rcMplsTEExplicitRouteIDCfgIdentifer,_Y:rcMplsTEExplicitRouteIDCfgIndex,'rcMplsTEExplicitRouteIDCfgNextIP':rcMplsTEExplicitRouteIDCfgNextIP,'rcMplsTEExplicitRouteIDCfgHopType':rcMplsTEExplicitRouteIDCfgHopType,'rcMplsTEExplicitRouteIDCfgHopAttribute':rcMplsTEExplicitRouteIDCfgHopAttribute,'rcMplsTEExplicitRouteIDCfgRowSta':rcMplsTEExplicitRouteIDCfgRowSta,'rcMplsTEHotStandbyCfgTable':rcMplsTEHotStandbyCfgTable,'rcMplsTEHotStandbyCfgEntry':rcMplsTEHotStandbyCfgEntry,_Z:rcMplsTEHotStandbyCfgTunnelID,_a:rcMplsTEHotStandbyCfgProtOptNo,'rcMplsTEHotStandbyCfgPathType':rcMplsTEHotStandbyCfgPathType,'rcMplsTEHotStandbyCfgExpPathName':rcMplsTEHotStandbyCfgExpPathName,'rcMplsTEHotStandbyCfgExpPathID':rcMplsTEHotStandbyCfgExpPathID,'rcMplsTEHotStandbyCfgRowSta':rcMplsTEHotStandbyCfgRowSta,'rcMplsTETunnelGroupCfgTable':rcMplsTETunnelGroupCfgTable,'rcMplsTETunnelGroupCfgEntry':rcMplsTETunnelGroupCfgEntry,_b:rcMplsTETunnelGroupCfgPrimaryTunnelID,'rcMplsTETunnelGroupCfgSecondaryTunnelID':rcMplsTETunnelGroupCfgSecondaryTunnelID,'rcMplsTETunnelGroupCfgRowSta':rcMplsTETunnelGroupCfgRowSta,'rcMplsTeConformance':rcMplsTeConformance,'rcMplsTeGroups':rcMplsTeGroups,'rcMplsTeNotificationGroup':rcMplsTeNotificationGroup})