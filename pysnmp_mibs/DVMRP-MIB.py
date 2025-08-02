_A8='dvmrpSecurityGroup'
_A7='dvmrpRoutingGroup'
_A6='dvmrpNeighborGroup'
_A5='dvmrpInterfaceGroup'
_A4='dvmrpGeneralGroup'
_A3='dvmrpInterfaceMasterKeyVersion'
_A2='dvmrpInterfaceMasterKey'
_A1='dvmrpRouteUpTime'
_A0='dvmrpNeighborRcvBadRoutes'
_z='dvmrpNeighborRcvBadPkts'
_y='dvmrpNeighborRcvRoutes'
_x='dvmrpInterfaceSentRoutes'
_w='dvmrpInterfaceRcvBadRoutes'
_v='dvmrpInterfaceRcvBadPkts'
_u='dvmrpAltNetStatus'
_t='dvmrpInterfaceOutOctets'
_s='dvmrpInterfaceInOctets'
_r='dvmrpInterfaceOutPkts'
_q='dvmrpInterfaceInPkts'
_p='dvmrpInterfaceRateLimit'
_o='dvmrpInterfaceRemoteSubnetMask'
_n='dvmrpInterfaceRemoteAddress'
_m='dvmrpInterfaceOperState'
_l='dvmrpInterfaceType'
_k='dvmrpAltNetMask'
_j='dvmrpAltNetAddress'
_i='dvmrpAltNetIfIndex'
_h='dvmrpRouteNextHopIfIndex'
_g='dvmrpRouteNextHopSourceMask'
_f='dvmrpRouteNextHopSource'
_e='dvmrpRouteSourceMask'
_d='dvmrpRouteSource'
_c='dvmrpInterfaceIfIndex'
_b='dvmrpNeighborState'
_a='dvmrpRouteNextHopType'
_Z='dvmrpRouteExpiryTime'
_Y='dvmrpRouteMetric'
_X='dvmrpRouteIfIndex'
_W='dvmrpRouteUpstreamNeighbor'
_V='dvmrpNeighborCapabilities'
_U='dvmrpNeighborMinorVersion'
_T='dvmrpNeighborMajorVersion'
_S='dvmrpNeighborGenerationId'
_R='dvmrpNeighborExpiryTime'
_Q='dvmrpNeighborUpTime'
_P='dvmrpInterfaceStatus'
_O='dvmrpInterfaceMetric'
_N='dvmrpReachableRoutes'
_M='dvmrpNumRoutes'
_L='dvmrpGenerationId'
_K='dvmrpVersionString'
_J='dvmrpNeighborAddress'
_I='dvmrpNeighborIfIndex'
_H='dvmrpInterfaceLocalAddress'
_G='read-create'
_F='Integer32'
_E='not-accessible'
_D='deprecated'
_C='read-only'
_B='current'
_A='DVMRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dvmrpMIB=ModuleIdentity((1,3,6,1,3,62))
_DvmrpMIBObjects_ObjectIdentity=ObjectIdentity
dvmrpMIBObjects=_DvmrpMIBObjects_ObjectIdentity((1,3,6,1,3,62,1))
_Dvmrp_ObjectIdentity=ObjectIdentity
dvmrp=_Dvmrp_ObjectIdentity((1,3,6,1,3,62,1,1))
_DvmrpVersionString_Type=DisplayString
_DvmrpVersionString_Object=MibScalar
dvmrpVersionString=_DvmrpVersionString_Object((1,3,6,1,3,62,1,1,1),_DvmrpVersionString_Type())
dvmrpVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpVersionString.setStatus(_B)
_DvmrpGenerationId_Type=Integer32
_DvmrpGenerationId_Object=MibScalar
dvmrpGenerationId=_DvmrpGenerationId_Object((1,3,6,1,3,62,1,1,2),_DvmrpGenerationId_Type())
dvmrpGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpGenerationId.setStatus(_B)
_DvmrpInterfaceTable_Object=MibTable
dvmrpInterfaceTable=_DvmrpInterfaceTable_Object((1,3,6,1,3,62,1,1,3))
if mibBuilder.loadTexts:dvmrpInterfaceTable.setStatus(_B)
_DvmrpInterfaceEntry_Object=MibTableRow
dvmrpInterfaceEntry=_DvmrpInterfaceEntry_Object((1,3,6,1,3,62,1,1,3,1))
dvmrpInterfaceEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:dvmrpInterfaceEntry.setStatus(_B)
_DvmrpInterfaceIfIndex_Type=Integer32
_DvmrpInterfaceIfIndex_Object=MibTableColumn
dvmrpInterfaceIfIndex=_DvmrpInterfaceIfIndex_Object((1,3,6,1,3,62,1,1,3,1,1),_DvmrpInterfaceIfIndex_Type())
dvmrpInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpInterfaceIfIndex.setStatus(_B)
class _DvmrpInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tunnel',1),('srcrt',2),('querier',3),('subnet',4)))
_DvmrpInterfaceType_Type.__name__=_F
_DvmrpInterfaceType_Object=MibTableColumn
dvmrpInterfaceType=_DvmrpInterfaceType_Object((1,3,6,1,3,62,1,1,3,1,2),_DvmrpInterfaceType_Type())
dvmrpInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceType.setStatus(_D)
class _DvmrpInterfaceOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_DvmrpInterfaceOperState_Type.__name__=_F
_DvmrpInterfaceOperState_Object=MibTableColumn
dvmrpInterfaceOperState=_DvmrpInterfaceOperState_Object((1,3,6,1,3,62,1,1,3,1,3),_DvmrpInterfaceOperState_Type())
dvmrpInterfaceOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceOperState.setStatus(_D)
_DvmrpInterfaceLocalAddress_Type=IpAddress
_DvmrpInterfaceLocalAddress_Object=MibTableColumn
dvmrpInterfaceLocalAddress=_DvmrpInterfaceLocalAddress_Object((1,3,6,1,3,62,1,1,3,1,4),_DvmrpInterfaceLocalAddress_Type())
dvmrpInterfaceLocalAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceLocalAddress.setStatus(_B)
_DvmrpInterfaceRemoteAddress_Type=IpAddress
_DvmrpInterfaceRemoteAddress_Object=MibTableColumn
dvmrpInterfaceRemoteAddress=_DvmrpInterfaceRemoteAddress_Object((1,3,6,1,3,62,1,1,3,1,5),_DvmrpInterfaceRemoteAddress_Type())
dvmrpInterfaceRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceRemoteAddress.setStatus(_D)
_DvmrpInterfaceRemoteSubnetMask_Type=IpAddress
_DvmrpInterfaceRemoteSubnetMask_Object=MibTableColumn
dvmrpInterfaceRemoteSubnetMask=_DvmrpInterfaceRemoteSubnetMask_Object((1,3,6,1,3,62,1,1,3,1,6),_DvmrpInterfaceRemoteSubnetMask_Type())
dvmrpInterfaceRemoteSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceRemoteSubnetMask.setStatus(_D)
class _DvmrpInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_DvmrpInterfaceMetric_Type.__name__=_F
_DvmrpInterfaceMetric_Object=MibTableColumn
dvmrpInterfaceMetric=_DvmrpInterfaceMetric_Object((1,3,6,1,3,62,1,1,3,1,7),_DvmrpInterfaceMetric_Type())
dvmrpInterfaceMetric.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceMetric.setStatus(_B)
class _DvmrpInterfaceRateLimit_Type(Integer32):defaultValue=0
_DvmrpInterfaceRateLimit_Type.__name__=_F
_DvmrpInterfaceRateLimit_Object=MibTableColumn
dvmrpInterfaceRateLimit=_DvmrpInterfaceRateLimit_Object((1,3,6,1,3,62,1,1,3,1,8),_DvmrpInterfaceRateLimit_Type())
dvmrpInterfaceRateLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceRateLimit.setStatus(_D)
_DvmrpInterfaceInPkts_Type=Counter32
_DvmrpInterfaceInPkts_Object=MibTableColumn
dvmrpInterfaceInPkts=_DvmrpInterfaceInPkts_Object((1,3,6,1,3,62,1,1,3,1,9),_DvmrpInterfaceInPkts_Type())
dvmrpInterfaceInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceInPkts.setStatus(_D)
_DvmrpInterfaceOutPkts_Type=Counter32
_DvmrpInterfaceOutPkts_Object=MibTableColumn
dvmrpInterfaceOutPkts=_DvmrpInterfaceOutPkts_Object((1,3,6,1,3,62,1,1,3,1,10),_DvmrpInterfaceOutPkts_Type())
dvmrpInterfaceOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceOutPkts.setStatus(_D)
_DvmrpInterfaceInOctets_Type=Counter32
_DvmrpInterfaceInOctets_Object=MibTableColumn
dvmrpInterfaceInOctets=_DvmrpInterfaceInOctets_Object((1,3,6,1,3,62,1,1,3,1,11),_DvmrpInterfaceInOctets_Type())
dvmrpInterfaceInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceInOctets.setStatus(_D)
_DvmrpInterfaceOutOctets_Type=Counter32
_DvmrpInterfaceOutOctets_Object=MibTableColumn
dvmrpInterfaceOutOctets=_DvmrpInterfaceOutOctets_Object((1,3,6,1,3,62,1,1,3,1,12),_DvmrpInterfaceOutOctets_Type())
dvmrpInterfaceOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceOutOctets.setStatus(_D)
_DvmrpInterfaceStatus_Type=RowStatus
_DvmrpInterfaceStatus_Object=MibTableColumn
dvmrpInterfaceStatus=_DvmrpInterfaceStatus_Object((1,3,6,1,3,62,1,1,3,1,13),_DvmrpInterfaceStatus_Type())
dvmrpInterfaceStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceStatus.setStatus(_B)
_DvmrpInterfaceRcvBadPkts_Type=Counter32
_DvmrpInterfaceRcvBadPkts_Object=MibTableColumn
dvmrpInterfaceRcvBadPkts=_DvmrpInterfaceRcvBadPkts_Object((1,3,6,1,3,62,1,1,3,1,14),_DvmrpInterfaceRcvBadPkts_Type())
dvmrpInterfaceRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadPkts.setStatus(_B)
_DvmrpInterfaceRcvBadRoutes_Type=Counter32
_DvmrpInterfaceRcvBadRoutes_Object=MibTableColumn
dvmrpInterfaceRcvBadRoutes=_DvmrpInterfaceRcvBadRoutes_Object((1,3,6,1,3,62,1,1,3,1,15),_DvmrpInterfaceRcvBadRoutes_Type())
dvmrpInterfaceRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadRoutes.setStatus(_B)
_DvmrpInterfaceSentRoutes_Type=Counter32
_DvmrpInterfaceSentRoutes_Object=MibTableColumn
dvmrpInterfaceSentRoutes=_DvmrpInterfaceSentRoutes_Object((1,3,6,1,3,62,1,1,3,1,16),_DvmrpInterfaceSentRoutes_Type())
dvmrpInterfaceSentRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceSentRoutes.setStatus(_B)
_DvmrpInterfaceMasterKey_Type=DisplayString
_DvmrpInterfaceMasterKey_Object=MibTableColumn
dvmrpInterfaceMasterKey=_DvmrpInterfaceMasterKey_Object((1,3,6,1,3,62,1,1,3,1,17),_DvmrpInterfaceMasterKey_Type())
dvmrpInterfaceMasterKey.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceMasterKey.setStatus(_B)
_DvmrpInterfaceMasterKeyVersion_Type=Integer32
_DvmrpInterfaceMasterKeyVersion_Object=MibTableColumn
dvmrpInterfaceMasterKeyVersion=_DvmrpInterfaceMasterKeyVersion_Object((1,3,6,1,3,62,1,1,3,1,18),_DvmrpInterfaceMasterKeyVersion_Type())
dvmrpInterfaceMasterKeyVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpInterfaceMasterKeyVersion.setStatus(_B)
_DvmrpNeighborTable_Object=MibTable
dvmrpNeighborTable=_DvmrpNeighborTable_Object((1,3,6,1,3,62,1,1,4))
if mibBuilder.loadTexts:dvmrpNeighborTable.setStatus(_B)
_DvmrpNeighborEntry_Object=MibTableRow
dvmrpNeighborEntry=_DvmrpNeighborEntry_Object((1,3,6,1,3,62,1,1,4,1))
dvmrpNeighborEntry.setIndexNames((0,_A,_I),(0,_A,_J))
if mibBuilder.loadTexts:dvmrpNeighborEntry.setStatus(_B)
_DvmrpNeighborIfIndex_Type=Integer32
_DvmrpNeighborIfIndex_Object=MibTableColumn
dvmrpNeighborIfIndex=_DvmrpNeighborIfIndex_Object((1,3,6,1,3,62,1,1,4,1,1),_DvmrpNeighborIfIndex_Type())
dvmrpNeighborIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpNeighborIfIndex.setStatus(_B)
_DvmrpNeighborAddress_Type=IpAddress
_DvmrpNeighborAddress_Object=MibTableColumn
dvmrpNeighborAddress=_DvmrpNeighborAddress_Object((1,3,6,1,3,62,1,1,4,1,2),_DvmrpNeighborAddress_Type())
dvmrpNeighborAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpNeighborAddress.setStatus(_B)
_DvmrpNeighborUpTime_Type=TimeTicks
_DvmrpNeighborUpTime_Object=MibTableColumn
dvmrpNeighborUpTime=_DvmrpNeighborUpTime_Object((1,3,6,1,3,62,1,1,4,1,3),_DvmrpNeighborUpTime_Type())
dvmrpNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborUpTime.setStatus(_B)
_DvmrpNeighborExpiryTime_Type=TimeTicks
_DvmrpNeighborExpiryTime_Object=MibTableColumn
dvmrpNeighborExpiryTime=_DvmrpNeighborExpiryTime_Object((1,3,6,1,3,62,1,1,4,1,4),_DvmrpNeighborExpiryTime_Type())
dvmrpNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborExpiryTime.setStatus(_B)
_DvmrpNeighborGenerationId_Type=Integer32
_DvmrpNeighborGenerationId_Object=MibTableColumn
dvmrpNeighborGenerationId=_DvmrpNeighborGenerationId_Object((1,3,6,1,3,62,1,1,4,1,6),_DvmrpNeighborGenerationId_Type())
dvmrpNeighborGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborGenerationId.setStatus(_B)
class _DvmrpNeighborMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMajorVersion_Type.__name__=_F
_DvmrpNeighborMajorVersion_Object=MibTableColumn
dvmrpNeighborMajorVersion=_DvmrpNeighborMajorVersion_Object((1,3,6,1,3,62,1,1,4,1,7),_DvmrpNeighborMajorVersion_Type())
dvmrpNeighborMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborMajorVersion.setStatus(_B)
class _DvmrpNeighborMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMinorVersion_Type.__name__=_F
_DvmrpNeighborMinorVersion_Object=MibTableColumn
dvmrpNeighborMinorVersion=_DvmrpNeighborMinorVersion_Object((1,3,6,1,3,62,1,1,4,1,8),_DvmrpNeighborMinorVersion_Type())
dvmrpNeighborMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborMinorVersion.setStatus(_B)
class _DvmrpNeighborCapabilities_Type(Bits):namedValues=NamedValues(*(('leaf',0),('prune',1),('generationID',2),('mtrace',3)))
_DvmrpNeighborCapabilities_Type.__name__='Bits'
_DvmrpNeighborCapabilities_Object=MibTableColumn
dvmrpNeighborCapabilities=_DvmrpNeighborCapabilities_Object((1,3,6,1,3,62,1,1,4,1,9),_DvmrpNeighborCapabilities_Type())
dvmrpNeighborCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborCapabilities.setStatus(_B)
_DvmrpNeighborRcvRoutes_Type=Counter32
_DvmrpNeighborRcvRoutes_Object=MibTableColumn
dvmrpNeighborRcvRoutes=_DvmrpNeighborRcvRoutes_Object((1,3,6,1,3,62,1,1,4,1,10),_DvmrpNeighborRcvRoutes_Type())
dvmrpNeighborRcvRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvRoutes.setStatus(_B)
_DvmrpNeighborRcvBadPkts_Type=Counter32
_DvmrpNeighborRcvBadPkts_Object=MibTableColumn
dvmrpNeighborRcvBadPkts=_DvmrpNeighborRcvBadPkts_Object((1,3,6,1,3,62,1,1,4,1,11),_DvmrpNeighborRcvBadPkts_Type())
dvmrpNeighborRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadPkts.setStatus(_B)
_DvmrpNeighborRcvBadRoutes_Type=Counter32
_DvmrpNeighborRcvBadRoutes_Object=MibTableColumn
dvmrpNeighborRcvBadRoutes=_DvmrpNeighborRcvBadRoutes_Object((1,3,6,1,3,62,1,1,4,1,12),_DvmrpNeighborRcvBadRoutes_Type())
dvmrpNeighborRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadRoutes.setStatus(_B)
class _DvmrpNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oneway',1),('active',2),('ignoring',3),('down',4)))
_DvmrpNeighborState_Type.__name__=_F
_DvmrpNeighborState_Object=MibTableColumn
dvmrpNeighborState=_DvmrpNeighborState_Object((1,3,6,1,3,62,1,1,4,1,13),_DvmrpNeighborState_Type())
dvmrpNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborState.setStatus(_B)
_DvmrpRouteTable_Object=MibTable
dvmrpRouteTable=_DvmrpRouteTable_Object((1,3,6,1,3,62,1,1,5))
if mibBuilder.loadTexts:dvmrpRouteTable.setStatus(_B)
_DvmrpRouteEntry_Object=MibTableRow
dvmrpRouteEntry=_DvmrpRouteEntry_Object((1,3,6,1,3,62,1,1,5,1))
dvmrpRouteEntry.setIndexNames((0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:dvmrpRouteEntry.setStatus(_B)
_DvmrpRouteSource_Type=IpAddress
_DvmrpRouteSource_Object=MibTableColumn
dvmrpRouteSource=_DvmrpRouteSource_Object((1,3,6,1,3,62,1,1,5,1,1),_DvmrpRouteSource_Type())
dvmrpRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpRouteSource.setStatus(_B)
_DvmrpRouteSourceMask_Type=IpAddress
_DvmrpRouteSourceMask_Object=MibTableColumn
dvmrpRouteSourceMask=_DvmrpRouteSourceMask_Object((1,3,6,1,3,62,1,1,5,1,2),_DvmrpRouteSourceMask_Type())
dvmrpRouteSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpRouteSourceMask.setStatus(_B)
_DvmrpRouteUpstreamNeighbor_Type=IpAddress
_DvmrpRouteUpstreamNeighbor_Object=MibTableColumn
dvmrpRouteUpstreamNeighbor=_DvmrpRouteUpstreamNeighbor_Object((1,3,6,1,3,62,1,1,5,1,3),_DvmrpRouteUpstreamNeighbor_Type())
dvmrpRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteUpstreamNeighbor.setStatus(_B)
_DvmrpRouteIfIndex_Type=Integer32
_DvmrpRouteIfIndex_Object=MibTableColumn
dvmrpRouteIfIndex=_DvmrpRouteIfIndex_Object((1,3,6,1,3,62,1,1,5,1,4),_DvmrpRouteIfIndex_Type())
dvmrpRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteIfIndex.setStatus(_B)
class _DvmrpRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DvmrpRouteMetric_Type.__name__=_F
_DvmrpRouteMetric_Object=MibTableColumn
dvmrpRouteMetric=_DvmrpRouteMetric_Object((1,3,6,1,3,62,1,1,5,1,5),_DvmrpRouteMetric_Type())
dvmrpRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteMetric.setStatus(_B)
_DvmrpRouteExpiryTime_Type=TimeTicks
_DvmrpRouteExpiryTime_Object=MibTableColumn
dvmrpRouteExpiryTime=_DvmrpRouteExpiryTime_Object((1,3,6,1,3,62,1,1,5,1,6),_DvmrpRouteExpiryTime_Type())
dvmrpRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteExpiryTime.setStatus(_B)
_DvmrpRouteUpTime_Type=TimeTicks
_DvmrpRouteUpTime_Object=MibTableColumn
dvmrpRouteUpTime=_DvmrpRouteUpTime_Object((1,3,6,1,3,62,1,1,5,1,7),_DvmrpRouteUpTime_Type())
dvmrpRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteUpTime.setStatus(_B)
_DvmrpRouteNextHopTable_Object=MibTable
dvmrpRouteNextHopTable=_DvmrpRouteNextHopTable_Object((1,3,6,1,3,62,1,1,6))
if mibBuilder.loadTexts:dvmrpRouteNextHopTable.setStatus(_B)
_DvmrpRouteNextHopEntry_Object=MibTableRow
dvmrpRouteNextHopEntry=_DvmrpRouteNextHopEntry_Object((1,3,6,1,3,62,1,1,6,1))
dvmrpRouteNextHopEntry.setIndexNames((0,_A,_f),(0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:dvmrpRouteNextHopEntry.setStatus(_B)
_DvmrpRouteNextHopSource_Type=IpAddress
_DvmrpRouteNextHopSource_Object=MibTableColumn
dvmrpRouteNextHopSource=_DvmrpRouteNextHopSource_Object((1,3,6,1,3,62,1,1,6,1,1),_DvmrpRouteNextHopSource_Type())
dvmrpRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpRouteNextHopSource.setStatus(_B)
_DvmrpRouteNextHopSourceMask_Type=IpAddress
_DvmrpRouteNextHopSourceMask_Object=MibTableColumn
dvmrpRouteNextHopSourceMask=_DvmrpRouteNextHopSourceMask_Object((1,3,6,1,3,62,1,1,6,1,2),_DvmrpRouteNextHopSourceMask_Type())
dvmrpRouteNextHopSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpRouteNextHopSourceMask.setStatus(_B)
_DvmrpRouteNextHopIfIndex_Type=Integer32
_DvmrpRouteNextHopIfIndex_Object=MibTableColumn
dvmrpRouteNextHopIfIndex=_DvmrpRouteNextHopIfIndex_Object((1,3,6,1,3,62,1,1,6,1,3),_DvmrpRouteNextHopIfIndex_Type())
dvmrpRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpRouteNextHopIfIndex.setStatus(_B)
class _DvmrpRouteNextHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leaf',1),('branch',2)))
_DvmrpRouteNextHopType_Type.__name__=_F
_DvmrpRouteNextHopType_Object=MibTableColumn
dvmrpRouteNextHopType=_DvmrpRouteNextHopType_Object((1,3,6,1,3,62,1,1,6,1,4),_DvmrpRouteNextHopType_Type())
dvmrpRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteNextHopType.setStatus(_B)
_DvmrpAltNetTable_Object=MibTable
dvmrpAltNetTable=_DvmrpAltNetTable_Object((1,3,6,1,3,62,1,1,8))
if mibBuilder.loadTexts:dvmrpAltNetTable.setStatus(_D)
_DvmrpAltNetEntry_Object=MibTableRow
dvmrpAltNetEntry=_DvmrpAltNetEntry_Object((1,3,6,1,3,62,1,1,8,1))
dvmrpAltNetEntry.setIndexNames((0,_A,_i),(0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:dvmrpAltNetEntry.setStatus(_D)
_DvmrpAltNetIfIndex_Type=Integer32
_DvmrpAltNetIfIndex_Object=MibTableColumn
dvmrpAltNetIfIndex=_DvmrpAltNetIfIndex_Object((1,3,6,1,3,62,1,1,8,1,1),_DvmrpAltNetIfIndex_Type())
dvmrpAltNetIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpAltNetIfIndex.setStatus(_D)
_DvmrpAltNetAddress_Type=IpAddress
_DvmrpAltNetAddress_Object=MibTableColumn
dvmrpAltNetAddress=_DvmrpAltNetAddress_Object((1,3,6,1,3,62,1,1,8,1,2),_DvmrpAltNetAddress_Type())
dvmrpAltNetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpAltNetAddress.setStatus(_D)
_DvmrpAltNetMask_Type=IpAddress
_DvmrpAltNetMask_Object=MibTableColumn
dvmrpAltNetMask=_DvmrpAltNetMask_Object((1,3,6,1,3,62,1,1,8,1,3),_DvmrpAltNetMask_Type())
dvmrpAltNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:dvmrpAltNetMask.setStatus(_D)
_DvmrpAltNetStatus_Type=RowStatus
_DvmrpAltNetStatus_Object=MibTableColumn
dvmrpAltNetStatus=_DvmrpAltNetStatus_Object((1,3,6,1,3,62,1,1,8,1,4),_DvmrpAltNetStatus_Type())
dvmrpAltNetStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dvmrpAltNetStatus.setStatus(_D)
_DvmrpNumRoutes_Type=Gauge32
_DvmrpNumRoutes_Object=MibScalar
dvmrpNumRoutes=_DvmrpNumRoutes_Object((1,3,6,1,3,62,1,1,9),_DvmrpNumRoutes_Type())
dvmrpNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNumRoutes.setStatus(_B)
_DvmrpReachableRoutes_Type=Gauge32
_DvmrpReachableRoutes_Object=MibScalar
dvmrpReachableRoutes=_DvmrpReachableRoutes_Object((1,3,6,1,3,62,1,1,10),_DvmrpReachableRoutes_Type())
dvmrpReachableRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpReachableRoutes.setStatus(_B)
_DvmrpTraps_ObjectIdentity=ObjectIdentity
dvmrpTraps=_DvmrpTraps_ObjectIdentity((1,3,6,1,3,62,1,1,11))
_DvmrpMIBConformance_ObjectIdentity=ObjectIdentity
dvmrpMIBConformance=_DvmrpMIBConformance_ObjectIdentity((1,3,6,1,3,62,2))
_DvmrpMIBCompliances_ObjectIdentity=ObjectIdentity
dvmrpMIBCompliances=_DvmrpMIBCompliances_ObjectIdentity((1,3,6,1,3,62,2,1))
_DvmrpMIBGroups_ObjectIdentity=ObjectIdentity
dvmrpMIBGroups=_DvmrpMIBGroups_ObjectIdentity((1,3,6,1,3,62,2,2))
dvmrpMIBGroup=ObjectGroup((1,3,6,1,3,62,2,2,1))
dvmrpMIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_l),(_A,_m),(_A,_H),(_A,_n),(_A,_o),(_A,_O),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_u)))
if mibBuilder.loadTexts:dvmrpMIBGroup.setStatus(_D)
dvmrpGeneralGroup=ObjectGroup((1,3,6,1,3,62,2,2,2))
dvmrpGeneralGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:dvmrpGeneralGroup.setStatus(_B)
dvmrpInterfaceGroup=ObjectGroup((1,3,6,1,3,62,2,2,3))
dvmrpInterfaceGroup.setObjects(*((_A,_H),(_A,_O),(_A,_P),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:dvmrpInterfaceGroup.setStatus(_B)
dvmrpNeighborGroup=ObjectGroup((1,3,6,1,3,62,2,2,4))
dvmrpNeighborGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_y),(_A,_z),(_A,_A0),(_A,_b)))
if mibBuilder.loadTexts:dvmrpNeighborGroup.setStatus(_B)
dvmrpRoutingGroup=ObjectGroup((1,3,6,1,3,62,2,2,5))
dvmrpRoutingGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A1),(_A,_a)))
if mibBuilder.loadTexts:dvmrpRoutingGroup.setStatus(_B)
dvmrpSecurityGroup=ObjectGroup((1,3,6,1,3,62,2,2,6))
dvmrpSecurityGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:dvmrpSecurityGroup.setStatus(_B)
dvmrpNeighborLoss=NotificationType((1,3,6,1,3,62,1,1,11,1))
dvmrpNeighborLoss.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_b)))
if mibBuilder.loadTexts:dvmrpNeighborLoss.setStatus(_B)
dvmrpNeighborNotPruning=NotificationType((1,3,6,1,3,62,1,1,11,2))
dvmrpNeighborNotPruning.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:dvmrpNeighborNotPruning.setStatus(_B)
dvmrpMIBCompliance=ModuleCompliance((1,3,6,1,3,62,2,1,1))
dvmrpMIBCompliance.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:dvmrpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dvmrpMIB':dvmrpMIB,'dvmrpMIBObjects':dvmrpMIBObjects,'dvmrp':dvmrp,_K:dvmrpVersionString,_L:dvmrpGenerationId,'dvmrpInterfaceTable':dvmrpInterfaceTable,'dvmrpInterfaceEntry':dvmrpInterfaceEntry,_c:dvmrpInterfaceIfIndex,_l:dvmrpInterfaceType,_m:dvmrpInterfaceOperState,_H:dvmrpInterfaceLocalAddress,_n:dvmrpInterfaceRemoteAddress,_o:dvmrpInterfaceRemoteSubnetMask,_O:dvmrpInterfaceMetric,_p:dvmrpInterfaceRateLimit,_q:dvmrpInterfaceInPkts,_r:dvmrpInterfaceOutPkts,_s:dvmrpInterfaceInOctets,_t:dvmrpInterfaceOutOctets,_P:dvmrpInterfaceStatus,_v:dvmrpInterfaceRcvBadPkts,_w:dvmrpInterfaceRcvBadRoutes,_x:dvmrpInterfaceSentRoutes,_A2:dvmrpInterfaceMasterKey,_A3:dvmrpInterfaceMasterKeyVersion,'dvmrpNeighborTable':dvmrpNeighborTable,'dvmrpNeighborEntry':dvmrpNeighborEntry,_I:dvmrpNeighborIfIndex,_J:dvmrpNeighborAddress,_Q:dvmrpNeighborUpTime,_R:dvmrpNeighborExpiryTime,_S:dvmrpNeighborGenerationId,_T:dvmrpNeighborMajorVersion,_U:dvmrpNeighborMinorVersion,_V:dvmrpNeighborCapabilities,_y:dvmrpNeighborRcvRoutes,_z:dvmrpNeighborRcvBadPkts,_A0:dvmrpNeighborRcvBadRoutes,_b:dvmrpNeighborState,'dvmrpRouteTable':dvmrpRouteTable,'dvmrpRouteEntry':dvmrpRouteEntry,_d:dvmrpRouteSource,_e:dvmrpRouteSourceMask,_W:dvmrpRouteUpstreamNeighbor,_X:dvmrpRouteIfIndex,_Y:dvmrpRouteMetric,_Z:dvmrpRouteExpiryTime,_A1:dvmrpRouteUpTime,'dvmrpRouteNextHopTable':dvmrpRouteNextHopTable,'dvmrpRouteNextHopEntry':dvmrpRouteNextHopEntry,_f:dvmrpRouteNextHopSource,_g:dvmrpRouteNextHopSourceMask,_h:dvmrpRouteNextHopIfIndex,_a:dvmrpRouteNextHopType,'dvmrpAltNetTable':dvmrpAltNetTable,'dvmrpAltNetEntry':dvmrpAltNetEntry,_i:dvmrpAltNetIfIndex,_j:dvmrpAltNetAddress,_k:dvmrpAltNetMask,_u:dvmrpAltNetStatus,_M:dvmrpNumRoutes,_N:dvmrpReachableRoutes,'dvmrpTraps':dvmrpTraps,'dvmrpNeighborLoss':dvmrpNeighborLoss,'dvmrpNeighborNotPruning':dvmrpNeighborNotPruning,'dvmrpMIBConformance':dvmrpMIBConformance,'dvmrpMIBCompliances':dvmrpMIBCompliances,'dvmrpMIBCompliance':dvmrpMIBCompliance,'dvmrpMIBGroups':dvmrpMIBGroups,'dvmrpMIBGroup':dvmrpMIBGroup,_A4:dvmrpGeneralGroup,_A5:dvmrpInterfaceGroup,_A6:dvmrpNeighborGroup,_A7:dvmrpRoutingGroup,_A8:dvmrpSecurityGroup})