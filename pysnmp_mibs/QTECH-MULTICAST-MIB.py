_AG='qtechMultVidMIBGroup'
_AF='qtechMrinfoMIBGroup'
_AE='qtechIpMRouteMIBGroup'
_AD='qtechMPingMIBGroup'
_AC='qtechIpRpfMIBGroup'
_AB='qtechIpMRouteInterfaceMIBGroup'
_AA='qtechMultVlan'
_A9='qtechMrinfoLeaf'
_A8='qtechMrinfoDown'
_A7='qtechMrinfoQuerier'
_A6='qtechMrinfoMetricOffset'
_A5='qtechMrinfoTtlThreshold'
_A4='qtechMrinfoNeighbor'
_A3='qtechIpMrouteSouceKilobitsPerSec'
_A2='qtechIpMrouteSouceAvgPktsSize'
_A1='qtechIpMrouteSoucePktsPerSec'
_A0='qtechIpMrouteSoucePkts'
_z='qtechIpMrouteRpKilobitsPerSec'
_y='qtechIpMrouteRpAvgPktsSize'
_x='qtechIpMrouteRpPktsPerSec'
_w='qtechIpMrouteRpPkts'
_v='qtechIpMrouteSouceCount'
_u='qtechIpMrouteGroupPktsCount'
_t='qtechIpMRouteLifeAvg'
_s='qtechIpMRouteInLimit'
_r='qtechIpMRouteSptFlag'
_q='qtechIpMRouteRpFlag'
_p='qtechIpMRouteRegisterFlag'
_o='qtechIpMRouteLocalFlag'
_n='qtechIpMRouteConnectedFlag'
_m='qtechIpMRouteSparseFlag'
_l='qtechIpMRoutePruneFlag'
_k='qtechIpMRouteRP'
_j='qtechMPingEntryStauts'
_i='qtechMPingCompleted'
_h='qtechMPingTimeOuts'
_g='qtechMPingDataLength'
_f='qtechMPingResponseTime'
_e='qtechIpRpfType'
_d='qtechIpRpfRouteMask'
_c='qtechIpRpfRouteAddress'
_b='qtechIpRpfNeighborAddress'
_a='qtechIpRpfInterface'
_Z='qtechIpMRouteBoundaryAclName'
_Y='qtechIpMRouteInterfaceHCOutMcastOctets'
_X='qtechIpMRouteInterfaceHCInMcastOctets'
_W='qtechIpMRouteInterfaceOutMcastOctets'
_V='qtechIpMRouteInterfaceInMcastOctets'
_U='qtechIpMRouteInterfaceRateLimit'
_T='qtechIpMRouteInterfaceProtocol'
_S='qtechIpMRouteInterfaceTtl'
_R='qtechMultInterfaceIfIndex'
_Q='qtechMrinfoIfAddress'
_P='qtechIpMRouteSourceMask'
_O='qtechIpMRouteSource'
_N='qtechIpMRouteGroup'
_M='qtechMPingGroupMember'
_L='qtechMPingGroupAddress'
_K='qtechMPingIndex'
_J='qtechIpRpfSourceAddress'
_I='qtechIpMRouteInterfaceIfIndex'
_H='read-create'
_G='Unsigned32'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='QTECH-MULTICAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechMultMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,28))
if mibBuilder.loadTexts:qtechMultMIB.setRevisions(('2003-01-20 00:00',))
_QtechMultMIBObjects_ObjectIdentity=ObjectIdentity
qtechMultMIBObjects=_QtechMultMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,28,1))
_QtechIpMRouteInterfaceTable_Object=MibTable
qtechIpMRouteInterfaceTable=_QtechIpMRouteInterfaceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1))
if mibBuilder.loadTexts:qtechIpMRouteInterfaceTable.setStatus(_A)
_QtechIpMRouteInterfaceEntry_Object=MibTableRow
qtechIpMRouteInterfaceEntry=_QtechIpMRouteInterfaceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1))
qtechIpMRouteInterfaceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechIpMRouteInterfaceEntry.setStatus(_A)
_QtechIpMRouteInterfaceIfIndex_Type=InterfaceIndex
_QtechIpMRouteInterfaceIfIndex_Object=MibTableColumn
qtechIpMRouteInterfaceIfIndex=_QtechIpMRouteInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,1),_QtechIpMRouteInterfaceIfIndex_Type())
qtechIpMRouteInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceIfIndex.setStatus(_A)
class _QtechIpMRouteInterfaceTtl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechIpMRouteInterfaceTtl_Type.__name__=_E
_QtechIpMRouteInterfaceTtl_Object=MibTableColumn
qtechIpMRouteInterfaceTtl=_QtechIpMRouteInterfaceTtl_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,2),_QtechIpMRouteInterfaceTtl_Type())
qtechIpMRouteInterfaceTtl.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceTtl.setStatus(_A)
_QtechIpMRouteInterfaceProtocol_Type=IANAipMRouteProtocol
_QtechIpMRouteInterfaceProtocol_Object=MibTableColumn
qtechIpMRouteInterfaceProtocol=_QtechIpMRouteInterfaceProtocol_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,3),_QtechIpMRouteInterfaceProtocol_Type())
qtechIpMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceProtocol.setStatus(_A)
class _QtechIpMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0
_QtechIpMRouteInterfaceRateLimit_Type.__name__=_E
_QtechIpMRouteInterfaceRateLimit_Object=MibTableColumn
qtechIpMRouteInterfaceRateLimit=_QtechIpMRouteInterfaceRateLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,4),_QtechIpMRouteInterfaceRateLimit_Type())
qtechIpMRouteInterfaceRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceRateLimit.setStatus(_A)
_QtechIpMRouteInterfaceInMcastOctets_Type=Counter32
_QtechIpMRouteInterfaceInMcastOctets_Object=MibTableColumn
qtechIpMRouteInterfaceInMcastOctets=_QtechIpMRouteInterfaceInMcastOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,5),_QtechIpMRouteInterfaceInMcastOctets_Type())
qtechIpMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceInMcastOctets.setStatus(_A)
_QtechIpMRouteInterfaceOutMcastOctets_Type=Counter32
_QtechIpMRouteInterfaceOutMcastOctets_Object=MibTableColumn
qtechIpMRouteInterfaceOutMcastOctets=_QtechIpMRouteInterfaceOutMcastOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,6),_QtechIpMRouteInterfaceOutMcastOctets_Type())
qtechIpMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceOutMcastOctets.setStatus(_A)
_QtechIpMRouteInterfaceHCInMcastOctets_Type=Counter64
_QtechIpMRouteInterfaceHCInMcastOctets_Object=MibTableColumn
qtechIpMRouteInterfaceHCInMcastOctets=_QtechIpMRouteInterfaceHCInMcastOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,7),_QtechIpMRouteInterfaceHCInMcastOctets_Type())
qtechIpMRouteInterfaceHCInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceHCInMcastOctets.setStatus(_A)
_QtechIpMRouteInterfaceHCOutMcastOctets_Type=Counter64
_QtechIpMRouteInterfaceHCOutMcastOctets_Object=MibTableColumn
qtechIpMRouteInterfaceHCOutMcastOctets=_QtechIpMRouteInterfaceHCOutMcastOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,8),_QtechIpMRouteInterfaceHCOutMcastOctets_Type())
qtechIpMRouteInterfaceHCOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInterfaceHCOutMcastOctets.setStatus(_A)
_QtechIpMRouteBoundaryAclName_Type=DisplayString
_QtechIpMRouteBoundaryAclName_Object=MibTableColumn
qtechIpMRouteBoundaryAclName=_QtechIpMRouteBoundaryAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,1,1,9),_QtechIpMRouteBoundaryAclName_Type())
qtechIpMRouteBoundaryAclName.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechIpMRouteBoundaryAclName.setStatus(_A)
_QtechIpRpfTable_Object=MibTable
qtechIpRpfTable=_QtechIpRpfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2))
if mibBuilder.loadTexts:qtechIpRpfTable.setStatus(_A)
_QtechIpRpfEntry_Object=MibTableRow
qtechIpRpfEntry=_QtechIpRpfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1))
qtechIpRpfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechIpRpfEntry.setStatus(_A)
_QtechIpRpfSourceAddress_Type=IpAddress
_QtechIpRpfSourceAddress_Object=MibTableColumn
qtechIpRpfSourceAddress=_QtechIpRpfSourceAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,1),_QtechIpRpfSourceAddress_Type())
qtechIpRpfSourceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpRpfSourceAddress.setStatus(_A)
_QtechIpRpfInterface_Type=InterfaceIndex
_QtechIpRpfInterface_Object=MibTableColumn
qtechIpRpfInterface=_QtechIpRpfInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,2),_QtechIpRpfInterface_Type())
qtechIpRpfInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpRpfInterface.setStatus(_A)
_QtechIpRpfNeighborAddress_Type=IpAddress
_QtechIpRpfNeighborAddress_Object=MibTableColumn
qtechIpRpfNeighborAddress=_QtechIpRpfNeighborAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,3),_QtechIpRpfNeighborAddress_Type())
qtechIpRpfNeighborAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpRpfNeighborAddress.setStatus(_A)
_QtechIpRpfRouteAddress_Type=IpAddress
_QtechIpRpfRouteAddress_Object=MibTableColumn
qtechIpRpfRouteAddress=_QtechIpRpfRouteAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,4),_QtechIpRpfRouteAddress_Type())
qtechIpRpfRouteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpRpfRouteAddress.setStatus(_A)
_QtechIpRpfRouteMask_Type=IpAddress
_QtechIpRpfRouteMask_Object=MibTableColumn
qtechIpRpfRouteMask=_QtechIpRpfRouteMask_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,5),_QtechIpRpfRouteMask_Type())
qtechIpRpfRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpRpfRouteMask.setStatus(_A)
class _QtechIpRpfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('dvmrp',2)))
_QtechIpRpfType_Type.__name__=_E
_QtechIpRpfType_Object=MibTableColumn
qtechIpRpfType=_QtechIpRpfType_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,2,1,6),_QtechIpRpfType_Type())
qtechIpRpfType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpRpfType.setStatus(_A)
_QtechMPingTable_Object=MibTable
qtechMPingTable=_QtechMPingTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3))
if mibBuilder.loadTexts:qtechMPingTable.setStatus(_A)
_QtechMPingEntry_Object=MibTableRow
qtechMPingEntry=_QtechMPingEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1))
qtechMPingEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechMPingEntry.setStatus(_A)
class _QtechMPingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechMPingIndex_Type.__name__=_E
_QtechMPingIndex_Object=MibTableColumn
qtechMPingIndex=_QtechMPingIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,1),_QtechMPingIndex_Type())
qtechMPingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMPingIndex.setStatus(_A)
_QtechMPingGroupAddress_Type=IpAddress
_QtechMPingGroupAddress_Object=MibTableColumn
qtechMPingGroupAddress=_QtechMPingGroupAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,2),_QtechMPingGroupAddress_Type())
qtechMPingGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMPingGroupAddress.setStatus(_A)
_QtechMPingGroupMember_Type=IpAddress
_QtechMPingGroupMember_Object=MibTableColumn
qtechMPingGroupMember=_QtechMPingGroupMember_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,3),_QtechMPingGroupMember_Type())
qtechMPingGroupMember.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMPingGroupMember.setStatus(_A)
_QtechMPingResponseTime_Type=TimeTicks
_QtechMPingResponseTime_Object=MibTableColumn
qtechMPingResponseTime=_QtechMPingResponseTime_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,4),_QtechMPingResponseTime_Type())
qtechMPingResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMPingResponseTime.setStatus(_A)
class _QtechMPingDataLength_Type(Unsigned32):defaultValue=1500
_QtechMPingDataLength_Type.__name__=_G
_QtechMPingDataLength_Object=MibTableColumn
qtechMPingDataLength=_QtechMPingDataLength_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,5),_QtechMPingDataLength_Type())
qtechMPingDataLength.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechMPingDataLength.setStatus(_A)
class _QtechMPingTimeOuts_Type(Unsigned32):defaultValue=1000
_QtechMPingTimeOuts_Type.__name__=_G
_QtechMPingTimeOuts_Object=MibTableColumn
qtechMPingTimeOuts=_QtechMPingTimeOuts_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,6),_QtechMPingTimeOuts_Type())
qtechMPingTimeOuts.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechMPingTimeOuts.setStatus(_A)
_QtechMPingCompleted_Type=TruthValue
_QtechMPingCompleted_Object=MibTableColumn
qtechMPingCompleted=_QtechMPingCompleted_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,7),_QtechMPingCompleted_Type())
qtechMPingCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMPingCompleted.setStatus(_A)
_QtechMPingEntryStauts_Type=RowStatus
_QtechMPingEntryStauts_Object=MibTableColumn
qtechMPingEntryStauts=_QtechMPingEntryStauts_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,3,1,8),_QtechMPingEntryStauts_Type())
qtechMPingEntryStauts.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechMPingEntryStauts.setStatus(_A)
_QtechIpMRouteTable_Object=MibTable
qtechIpMRouteTable=_QtechIpMRouteTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4))
if mibBuilder.loadTexts:qtechIpMRouteTable.setStatus(_A)
_QtechIpMRouteEntry_Object=MibTableRow
qtechIpMRouteEntry=_QtechIpMRouteEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1))
qtechIpMRouteEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:qtechIpMRouteEntry.setStatus(_A)
_QtechIpMRouteGroup_Type=IpAddress
_QtechIpMRouteGroup_Object=MibTableColumn
qtechIpMRouteGroup=_QtechIpMRouteGroup_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,1),_QtechIpMRouteGroup_Type())
qtechIpMRouteGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpMRouteGroup.setStatus(_A)
_QtechIpMRouteSource_Type=IpAddress
_QtechIpMRouteSource_Object=MibTableColumn
qtechIpMRouteSource=_QtechIpMRouteSource_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,2),_QtechIpMRouteSource_Type())
qtechIpMRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpMRouteSource.setStatus(_A)
_QtechIpMRouteSourceMask_Type=IpAddress
_QtechIpMRouteSourceMask_Object=MibTableColumn
qtechIpMRouteSourceMask=_QtechIpMRouteSourceMask_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,3),_QtechIpMRouteSourceMask_Type())
qtechIpMRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIpMRouteSourceMask.setStatus(_A)
_QtechIpMRouteRP_Type=IpAddress
_QtechIpMRouteRP_Object=MibTableColumn
qtechIpMRouteRP=_QtechIpMRouteRP_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,4),_QtechIpMRouteRP_Type())
qtechIpMRouteRP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteRP.setStatus(_A)
_QtechIpMRoutePruneFlag_Type=TruthValue
_QtechIpMRoutePruneFlag_Object=MibTableColumn
qtechIpMRoutePruneFlag=_QtechIpMRoutePruneFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,5),_QtechIpMRoutePruneFlag_Type())
qtechIpMRoutePruneFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRoutePruneFlag.setStatus(_A)
_QtechIpMRouteSparseFlag_Type=TruthValue
_QtechIpMRouteSparseFlag_Object=MibTableColumn
qtechIpMRouteSparseFlag=_QtechIpMRouteSparseFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,6),_QtechIpMRouteSparseFlag_Type())
qtechIpMRouteSparseFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteSparseFlag.setStatus(_A)
_QtechIpMRouteConnectedFlag_Type=TruthValue
_QtechIpMRouteConnectedFlag_Object=MibTableColumn
qtechIpMRouteConnectedFlag=_QtechIpMRouteConnectedFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,7),_QtechIpMRouteConnectedFlag_Type())
qtechIpMRouteConnectedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteConnectedFlag.setStatus(_A)
_QtechIpMRouteLocalFlag_Type=TruthValue
_QtechIpMRouteLocalFlag_Object=MibTableColumn
qtechIpMRouteLocalFlag=_QtechIpMRouteLocalFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,8),_QtechIpMRouteLocalFlag_Type())
qtechIpMRouteLocalFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteLocalFlag.setStatus(_A)
_QtechIpMRouteRegisterFlag_Type=TruthValue
_QtechIpMRouteRegisterFlag_Object=MibTableColumn
qtechIpMRouteRegisterFlag=_QtechIpMRouteRegisterFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,9),_QtechIpMRouteRegisterFlag_Type())
qtechIpMRouteRegisterFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteRegisterFlag.setStatus(_A)
_QtechIpMRouteRpFlag_Type=TruthValue
_QtechIpMRouteRpFlag_Object=MibTableColumn
qtechIpMRouteRpFlag=_QtechIpMRouteRpFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,10),_QtechIpMRouteRpFlag_Type())
qtechIpMRouteRpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteRpFlag.setStatus(_A)
_QtechIpMRouteSptFlag_Type=TruthValue
_QtechIpMRouteSptFlag_Object=MibTableColumn
qtechIpMRouteSptFlag=_QtechIpMRouteSptFlag_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,11),_QtechIpMRouteSptFlag_Type())
qtechIpMRouteSptFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteSptFlag.setStatus(_A)
class _QtechIpMRouteInLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechIpMRouteInLimit_Type.__name__=_E
_QtechIpMRouteInLimit_Object=MibTableColumn
qtechIpMRouteInLimit=_QtechIpMRouteInLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,12),_QtechIpMRouteInLimit_Type())
qtechIpMRouteInLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteInLimit.setStatus('obsolete')
if mibBuilder.loadTexts:qtechIpMRouteInLimit.setUnits('Kbits/second')
_QtechIpMRouteLifeAvg_Type=Integer32
_QtechIpMRouteLifeAvg_Object=MibTableColumn
qtechIpMRouteLifeAvg=_QtechIpMRouteLifeAvg_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,13),_QtechIpMRouteLifeAvg_Type())
qtechIpMRouteLifeAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMRouteLifeAvg.setStatus(_A)
_QtechIpMrouteGroupPktsCount_Type=Integer32
_QtechIpMrouteGroupPktsCount_Object=MibTableColumn
qtechIpMrouteGroupPktsCount=_QtechIpMrouteGroupPktsCount_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,14),_QtechIpMrouteGroupPktsCount_Type())
qtechIpMrouteGroupPktsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteGroupPktsCount.setStatus(_A)
_QtechIpMrouteSouceCount_Type=Integer32
_QtechIpMrouteSouceCount_Object=MibTableColumn
qtechIpMrouteSouceCount=_QtechIpMrouteSouceCount_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,15),_QtechIpMrouteSouceCount_Type())
qtechIpMrouteSouceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteSouceCount.setStatus(_A)
_QtechIpMrouteRpPkts_Type=Integer32
_QtechIpMrouteRpPkts_Object=MibTableColumn
qtechIpMrouteRpPkts=_QtechIpMrouteRpPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,16),_QtechIpMrouteRpPkts_Type())
qtechIpMrouteRpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteRpPkts.setStatus(_A)
_QtechIpMrouteRpPktsPerSec_Type=Integer32
_QtechIpMrouteRpPktsPerSec_Object=MibTableColumn
qtechIpMrouteRpPktsPerSec=_QtechIpMrouteRpPktsPerSec_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,17),_QtechIpMrouteRpPktsPerSec_Type())
qtechIpMrouteRpPktsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteRpPktsPerSec.setStatus(_A)
_QtechIpMrouteRpAvgPktsSize_Type=Integer32
_QtechIpMrouteRpAvgPktsSize_Object=MibTableColumn
qtechIpMrouteRpAvgPktsSize=_QtechIpMrouteRpAvgPktsSize_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,18),_QtechIpMrouteRpAvgPktsSize_Type())
qtechIpMrouteRpAvgPktsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteRpAvgPktsSize.setStatus(_A)
_QtechIpMrouteRpKilobitsPerSec_Type=Integer32
_QtechIpMrouteRpKilobitsPerSec_Object=MibTableColumn
qtechIpMrouteRpKilobitsPerSec=_QtechIpMrouteRpKilobitsPerSec_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,19),_QtechIpMrouteRpKilobitsPerSec_Type())
qtechIpMrouteRpKilobitsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteRpKilobitsPerSec.setStatus(_A)
_QtechIpMrouteSoucePkts_Type=Integer32
_QtechIpMrouteSoucePkts_Object=MibTableColumn
qtechIpMrouteSoucePkts=_QtechIpMrouteSoucePkts_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,20),_QtechIpMrouteSoucePkts_Type())
qtechIpMrouteSoucePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteSoucePkts.setStatus(_A)
_QtechIpMrouteSoucePktsPerSec_Type=Integer32
_QtechIpMrouteSoucePktsPerSec_Object=MibTableColumn
qtechIpMrouteSoucePktsPerSec=_QtechIpMrouteSoucePktsPerSec_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,21),_QtechIpMrouteSoucePktsPerSec_Type())
qtechIpMrouteSoucePktsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteSoucePktsPerSec.setStatus(_A)
_QtechIpMrouteSouceAvgPktsSize_Type=Integer32
_QtechIpMrouteSouceAvgPktsSize_Object=MibTableColumn
qtechIpMrouteSouceAvgPktsSize=_QtechIpMrouteSouceAvgPktsSize_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,22),_QtechIpMrouteSouceAvgPktsSize_Type())
qtechIpMrouteSouceAvgPktsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteSouceAvgPktsSize.setStatus(_A)
_QtechIpMrouteSouceKilobitsPerSec_Type=Integer32
_QtechIpMrouteSouceKilobitsPerSec_Object=MibTableColumn
qtechIpMrouteSouceKilobitsPerSec=_QtechIpMrouteSouceKilobitsPerSec_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,4,1,23),_QtechIpMrouteSouceKilobitsPerSec_Type())
qtechIpMrouteSouceKilobitsPerSec.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIpMrouteSouceKilobitsPerSec.setStatus(_A)
_QtechMrinfoTable_Object=MibTable
qtechMrinfoTable=_QtechMrinfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5))
if mibBuilder.loadTexts:qtechMrinfoTable.setStatus(_A)
_QtechMrinfoEntry_Object=MibTableRow
qtechMrinfoEntry=_QtechMrinfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1))
qtechMrinfoEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qtechMrinfoEntry.setStatus(_A)
_QtechMrinfoIfAddress_Type=IpAddress
_QtechMrinfoIfAddress_Object=MibTableColumn
qtechMrinfoIfAddress=_QtechMrinfoIfAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,1),_QtechMrinfoIfAddress_Type())
qtechMrinfoIfAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMrinfoIfAddress.setStatus(_A)
_QtechMrinfoNeighbor_Type=IpAddress
_QtechMrinfoNeighbor_Object=MibTableColumn
qtechMrinfoNeighbor=_QtechMrinfoNeighbor_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,2),_QtechMrinfoNeighbor_Type())
qtechMrinfoNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoNeighbor.setStatus(_A)
_QtechMrinfoTtlThreshold_Type=Integer32
_QtechMrinfoTtlThreshold_Object=MibTableColumn
qtechMrinfoTtlThreshold=_QtechMrinfoTtlThreshold_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,3),_QtechMrinfoTtlThreshold_Type())
qtechMrinfoTtlThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoTtlThreshold.setStatus(_A)
_QtechMrinfoMetricOffset_Type=Integer32
_QtechMrinfoMetricOffset_Object=MibTableColumn
qtechMrinfoMetricOffset=_QtechMrinfoMetricOffset_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,4),_QtechMrinfoMetricOffset_Type())
qtechMrinfoMetricOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoMetricOffset.setStatus(_A)
_QtechMrinfoQuerier_Type=TruthValue
_QtechMrinfoQuerier_Object=MibTableColumn
qtechMrinfoQuerier=_QtechMrinfoQuerier_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,5),_QtechMrinfoQuerier_Type())
qtechMrinfoQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoQuerier.setStatus(_A)
_QtechMrinfoDown_Type=TruthValue
_QtechMrinfoDown_Object=MibTableColumn
qtechMrinfoDown=_QtechMrinfoDown_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,6),_QtechMrinfoDown_Type())
qtechMrinfoDown.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoDown.setStatus(_A)
_QtechMrinfoLeaf_Type=TruthValue
_QtechMrinfoLeaf_Object=MibTableColumn
qtechMrinfoLeaf=_QtechMrinfoLeaf_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,5,1,7),_QtechMrinfoLeaf_Type())
qtechMrinfoLeaf.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechMrinfoLeaf.setStatus(_A)
_QtechMultVidTable_Object=MibTable
qtechMultVidTable=_QtechMultVidTable_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,6))
if mibBuilder.loadTexts:qtechMultVidTable.setStatus(_A)
_QtechMultVidEntry_Object=MibTableRow
qtechMultVidEntry=_QtechMultVidEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,6,1))
qtechMultVidEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:qtechMultVidEntry.setStatus(_A)
_QtechMultInterfaceIfIndex_Type=IfIndex
_QtechMultInterfaceIfIndex_Object=MibTableColumn
qtechMultInterfaceIfIndex=_QtechMultInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,6,1,1),_QtechMultInterfaceIfIndex_Type())
qtechMultInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMultInterfaceIfIndex.setStatus(_A)
_QtechMultVlan_Type=VlanId
_QtechMultVlan_Object=MibTableColumn
qtechMultVlan=_QtechMultVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,28,1,6,1,2),_QtechMultVlan_Type())
qtechMultVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechMultVlan.setStatus(_A)
_QtechMultMIBConformance_ObjectIdentity=ObjectIdentity
qtechMultMIBConformance=_QtechMultMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,28,2))
_QtechMultMIBCompliances_ObjectIdentity=ObjectIdentity
qtechMultMIBCompliances=_QtechMultMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,28,2,1))
_QtechMultMIBGroups_ObjectIdentity=ObjectIdentity
qtechMultMIBGroups=_QtechMultMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,28,2,2))
qtechIpMRouteInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,1))
qtechIpMRouteInterfaceMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:qtechIpMRouteInterfaceMIBGroup.setStatus(_A)
qtechIpRpfMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,2))
qtechIpRpfMIBGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:qtechIpRpfMIBGroup.setStatus(_A)
qtechMPingMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,3))
qtechMPingMIBGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:qtechMPingMIBGroup.setStatus(_A)
qtechIpMRouteMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,4))
qtechIpMRouteMIBGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:qtechIpMRouteMIBGroup.setStatus(_A)
qtechMrinfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,5))
qtechMrinfoMIBGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:qtechMrinfoMIBGroup.setStatus(_A)
qtechMultVidMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,28,2,2,6))
qtechMultVidMIBGroup.setObjects((_B,_AA))
if mibBuilder.loadTexts:qtechMultVidMIBGroup.setStatus(_A)
qtechMultMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,28,2,1,1))
qtechMultMIBCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:qtechMultMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechMultMIB':qtechMultMIB,'qtechMultMIBObjects':qtechMultMIBObjects,'qtechIpMRouteInterfaceTable':qtechIpMRouteInterfaceTable,'qtechIpMRouteInterfaceEntry':qtechIpMRouteInterfaceEntry,_I:qtechIpMRouteInterfaceIfIndex,_S:qtechIpMRouteInterfaceTtl,_T:qtechIpMRouteInterfaceProtocol,_U:qtechIpMRouteInterfaceRateLimit,_V:qtechIpMRouteInterfaceInMcastOctets,_W:qtechIpMRouteInterfaceOutMcastOctets,_X:qtechIpMRouteInterfaceHCInMcastOctets,_Y:qtechIpMRouteInterfaceHCOutMcastOctets,_Z:qtechIpMRouteBoundaryAclName,'qtechIpRpfTable':qtechIpRpfTable,'qtechIpRpfEntry':qtechIpRpfEntry,_J:qtechIpRpfSourceAddress,_a:qtechIpRpfInterface,_b:qtechIpRpfNeighborAddress,_c:qtechIpRpfRouteAddress,_d:qtechIpRpfRouteMask,_e:qtechIpRpfType,'qtechMPingTable':qtechMPingTable,'qtechMPingEntry':qtechMPingEntry,_K:qtechMPingIndex,_L:qtechMPingGroupAddress,_M:qtechMPingGroupMember,_f:qtechMPingResponseTime,_g:qtechMPingDataLength,_h:qtechMPingTimeOuts,_i:qtechMPingCompleted,_j:qtechMPingEntryStauts,'qtechIpMRouteTable':qtechIpMRouteTable,'qtechIpMRouteEntry':qtechIpMRouteEntry,_N:qtechIpMRouteGroup,_O:qtechIpMRouteSource,_P:qtechIpMRouteSourceMask,_k:qtechIpMRouteRP,_l:qtechIpMRoutePruneFlag,_m:qtechIpMRouteSparseFlag,_n:qtechIpMRouteConnectedFlag,_o:qtechIpMRouteLocalFlag,_p:qtechIpMRouteRegisterFlag,_q:qtechIpMRouteRpFlag,_r:qtechIpMRouteSptFlag,_s:qtechIpMRouteInLimit,_t:qtechIpMRouteLifeAvg,_u:qtechIpMrouteGroupPktsCount,_v:qtechIpMrouteSouceCount,_w:qtechIpMrouteRpPkts,_x:qtechIpMrouteRpPktsPerSec,_y:qtechIpMrouteRpAvgPktsSize,_z:qtechIpMrouteRpKilobitsPerSec,_A0:qtechIpMrouteSoucePkts,_A1:qtechIpMrouteSoucePktsPerSec,_A2:qtechIpMrouteSouceAvgPktsSize,_A3:qtechIpMrouteSouceKilobitsPerSec,'qtechMrinfoTable':qtechMrinfoTable,'qtechMrinfoEntry':qtechMrinfoEntry,_Q:qtechMrinfoIfAddress,_A4:qtechMrinfoNeighbor,_A5:qtechMrinfoTtlThreshold,_A6:qtechMrinfoMetricOffset,_A7:qtechMrinfoQuerier,_A8:qtechMrinfoDown,_A9:qtechMrinfoLeaf,'qtechMultVidTable':qtechMultVidTable,'qtechMultVidEntry':qtechMultVidEntry,_R:qtechMultInterfaceIfIndex,_AA:qtechMultVlan,'qtechMultMIBConformance':qtechMultMIBConformance,'qtechMultMIBCompliances':qtechMultMIBCompliances,'qtechMultMIBCompliance':qtechMultMIBCompliance,'qtechMultMIBGroups':qtechMultMIBGroups,_AB:qtechIpMRouteInterfaceMIBGroup,_AC:qtechIpRpfMIBGroup,_AD:qtechMPingMIBGroup,_AE:qtechIpMRouteMIBGroup,_AF:qtechMrinfoMIBGroup,_AG:qtechMultVidMIBGroup})