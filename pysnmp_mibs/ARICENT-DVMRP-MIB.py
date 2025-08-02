_A2='dvmrpRoutingGroup'
_A1='dvmrpNeighborGroup'
_A0='dvmrpInterfaceGroup'
_z='dvmrpGeneralGroup'
_y='dvmrpRouteNextHopType'
_x='dvmrpRouteUpTime'
_w='dvmrpRouteExpiryTime'
_v='dvmrpRouteMetric'
_u='dvmrpRouteIfIndex'
_t='dvmrpRouteUpstreamNeighbor'
_s='dvmrpNeighborRcvBadRoutes'
_r='dvmrpNeighborRcvBadPkts'
_q='dvmrpNeighborRcvRoutes'
_p='dvmrpNeighborCapabilities'
_o='dvmrpNeighborMinorVersion'
_n='dvmrpNeighborMajorVersion'
_m='dvmrpNeighborGenerationId'
_l='dvmrpNeighborExpiryTime'
_k='dvmrpNeighborUpTime'
_j='dvmrpInterfaceRcvBadRoutes'
_i='dvmrpInterfaceRcvBadPkts'
_h='dvmrpInterfaceMetric'
_g='dvmrpInterfaceLocalAddress'
_f='dvmrpReachableRoutes'
_e='dvmrpNumRoutes'
_d='dvmrpGenerationId'
_c='dvmrpVersionString'
_b='dvmrpIpMNextHopAddress'
_a='dvmrpIpMNextHopIfIndex'
_Z='dvmrpIpMNextHopSourceMask'
_Y='dvmrpIpMNextHopSource'
_X='dvmrpIpMNextHopGroup'
_W='dvmrpIpMRSourceMask'
_V='dvmrpIpMRSource'
_U='dvmrpIpMRGroup'
_T='dvmrpForwardPruneNeighbor'
_S='dvmrpForwardIfIndex'
_R='dvmrpForwardGroupAddress'
_Q='dvmrpForwardSourceNetwork'
_P='pruned'
_O='dvmrpGroupAddress'
_N='dvmrpSourceNetwork'
_M='dvmrpRouteNextHopIfIndex'
_L='dvmrpRouteNextHopSourceMask'
_K='dvmrpRouteNextHopSource'
_J='dvmrpRouteSourceMask'
_I='dvmrpRouteSource'
_H='dvmrpNeighborAddress'
_G='dvmrpInterfaceIfIndex'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='ARICENT-DVMRP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dvmrpMIB=ModuleIdentity((1,3,6,1,4,1,2076,60))
if mibBuilder.loadTexts:dvmrpMIB.setRevisions(('2012-09-05 00:00',))
class Integer8(TextualConvention,Integer32):status=_A;displayHint='d1';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
class Integer16(TextualConvention,Integer32):status=_A;displayHint='d2';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_DvmrpScalar_ObjectIdentity=ObjectIdentity
dvmrpScalar=_DvmrpScalar_ObjectIdentity((1,3,6,1,4,1,2076,60,1))
_DvmrpVersionString_Type=DisplayString
_DvmrpVersionString_Object=MibScalar
dvmrpVersionString=_DvmrpVersionString_Object((1,3,6,1,4,1,2076,60,1,1),_DvmrpVersionString_Type())
dvmrpVersionString.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpVersionString.setStatus(_A)
_DvmrpGenerationId_Type=Integer32
_DvmrpGenerationId_Object=MibScalar
dvmrpGenerationId=_DvmrpGenerationId_Object((1,3,6,1,4,1,2076,60,1,2),_DvmrpGenerationId_Type())
dvmrpGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpGenerationId.setStatus(_A)
_DvmrpNumRoutes_Type=Gauge32
_DvmrpNumRoutes_Object=MibScalar
dvmrpNumRoutes=_DvmrpNumRoutes_Object((1,3,6,1,4,1,2076,60,1,3),_DvmrpNumRoutes_Type())
dvmrpNumRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNumRoutes.setStatus(_A)
_DvmrpReachableRoutes_Type=Gauge32
_DvmrpReachableRoutes_Object=MibScalar
dvmrpReachableRoutes=_DvmrpReachableRoutes_Object((1,3,6,1,4,1,2076,60,1,4),_DvmrpReachableRoutes_Type())
dvmrpReachableRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpReachableRoutes.setStatus(_A)
class _DvmrpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_DvmrpStatus_Type.__name__=_E
_DvmrpStatus_Object=MibScalar
dvmrpStatus=_DvmrpStatus_Object((1,3,6,1,4,1,2076,60,1,5),_DvmrpStatus_Type())
dvmrpStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpStatus.setStatus(_A)
class _DvmrpLogEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DvmrpLogEnabled_Type.__name__=_E
_DvmrpLogEnabled_Object=MibScalar
dvmrpLogEnabled=_DvmrpLogEnabled_Object((1,3,6,1,4,1,2076,60,1,6),_DvmrpLogEnabled_Type())
dvmrpLogEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpLogEnabled.setStatus(_A)
class _DvmrpLogMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_DvmrpLogMask_Type.__name__=_E
_DvmrpLogMask_Object=MibScalar
dvmrpLogMask=_DvmrpLogMask_Object((1,3,6,1,4,1,2076,60,1,7),_DvmrpLogMask_Type())
dvmrpLogMask.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpLogMask.setStatus(_A)
class _DvmrpPruneLifeTime_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_DvmrpPruneLifeTime_Type.__name__=_E
_DvmrpPruneLifeTime_Object=MibScalar
dvmrpPruneLifeTime=_DvmrpPruneLifeTime_Object((1,3,6,1,4,1,2076,60,1,8),_DvmrpPruneLifeTime_Type())
dvmrpPruneLifeTime.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpPruneLifeTime.setStatus(_A)
_Dvmrp_ObjectIdentity=ObjectIdentity
dvmrp=_Dvmrp_ObjectIdentity((1,3,6,1,4,1,2076,60,2))
_DvmrpInterfaceTable_Object=MibTable
dvmrpInterfaceTable=_DvmrpInterfaceTable_Object((1,3,6,1,4,1,2076,60,2,9))
if mibBuilder.loadTexts:dvmrpInterfaceTable.setStatus(_A)
_DvmrpInterfaceEntry_Object=MibTableRow
dvmrpInterfaceEntry=_DvmrpInterfaceEntry_Object((1,3,6,1,4,1,2076,60,2,9,1))
dvmrpInterfaceEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:dvmrpInterfaceEntry.setStatus(_A)
_DvmrpInterfaceIfIndex_Type=InterfaceIndex
_DvmrpInterfaceIfIndex_Object=MibTableColumn
dvmrpInterfaceIfIndex=_DvmrpInterfaceIfIndex_Object((1,3,6,1,4,1,2076,60,2,9,1,1),_DvmrpInterfaceIfIndex_Type())
dvmrpInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpInterfaceIfIndex.setStatus(_A)
_DvmrpInterfaceStatus_Type=RowStatus
_DvmrpInterfaceStatus_Object=MibTableColumn
dvmrpInterfaceStatus=_DvmrpInterfaceStatus_Object((1,3,6,1,4,1,2076,60,2,9,1,2),_DvmrpInterfaceStatus_Type())
dvmrpInterfaceStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:dvmrpInterfaceStatus.setStatus(_A)
_DvmrpInterfaceLocalAddress_Type=IpAddress
_DvmrpInterfaceLocalAddress_Object=MibTableColumn
dvmrpInterfaceLocalAddress=_DvmrpInterfaceLocalAddress_Object((1,3,6,1,4,1,2076,60,2,9,1,3),_DvmrpInterfaceLocalAddress_Type())
dvmrpInterfaceLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceLocalAddress.setStatus(_A)
class _DvmrpInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_DvmrpInterfaceMetric_Type.__name__=_E
_DvmrpInterfaceMetric_Object=MibTableColumn
dvmrpInterfaceMetric=_DvmrpInterfaceMetric_Object((1,3,6,1,4,1,2076,60,2,9,1,4),_DvmrpInterfaceMetric_Type())
dvmrpInterfaceMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceMetric.setStatus(_A)
_DvmrpInterfaceRcvBadPkts_Type=Counter32
_DvmrpInterfaceRcvBadPkts_Object=MibTableColumn
dvmrpInterfaceRcvBadPkts=_DvmrpInterfaceRcvBadPkts_Object((1,3,6,1,4,1,2076,60,2,9,1,5),_DvmrpInterfaceRcvBadPkts_Type())
dvmrpInterfaceRcvBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadPkts.setStatus(_A)
_DvmrpInterfaceRcvBadRoutes_Type=Counter32
_DvmrpInterfaceRcvBadRoutes_Object=MibTableColumn
dvmrpInterfaceRcvBadRoutes=_DvmrpInterfaceRcvBadRoutes_Object((1,3,6,1,4,1,2076,60,2,9,1,6),_DvmrpInterfaceRcvBadRoutes_Type())
dvmrpInterfaceRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadRoutes.setStatus(_A)
class _DvmrpInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpInterfaceTtl_Type.__name__=_E
_DvmrpInterfaceTtl_Object=MibTableColumn
dvmrpInterfaceTtl=_DvmrpInterfaceTtl_Object((1,3,6,1,4,1,2076,60,2,9,1,7),_DvmrpInterfaceTtl_Type())
dvmrpInterfaceTtl.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceTtl.setStatus(_A)
_DvmrpInterfaceProtocol_Type=IANAipMRouteProtocol
_DvmrpInterfaceProtocol_Object=MibTableColumn
dvmrpInterfaceProtocol=_DvmrpInterfaceProtocol_Object((1,3,6,1,4,1,2076,60,2,9,1,8),_DvmrpInterfaceProtocol_Type())
dvmrpInterfaceProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceProtocol.setStatus(_A)
class _DvmrpInterfaceRateLimit_Type(Integer32):defaultValue=0
_DvmrpInterfaceRateLimit_Type.__name__=_E
_DvmrpInterfaceRateLimit_Object=MibTableColumn
dvmrpInterfaceRateLimit=_DvmrpInterfaceRateLimit_Object((1,3,6,1,4,1,2076,60,2,9,1,9),_DvmrpInterfaceRateLimit_Type())
dvmrpInterfaceRateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceRateLimit.setStatus(_A)
_DvmrpInterfaceInMcastOctets_Type=Counter32
_DvmrpInterfaceInMcastOctets_Object=MibTableColumn
dvmrpInterfaceInMcastOctets=_DvmrpInterfaceInMcastOctets_Object((1,3,6,1,4,1,2076,60,2,9,1,10),_DvmrpInterfaceInMcastOctets_Type())
dvmrpInterfaceInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceInMcastOctets.setStatus(_A)
_DvmrpInterfaceOutMcastOctets_Type=Counter32
_DvmrpInterfaceOutMcastOctets_Object=MibTableColumn
dvmrpInterfaceOutMcastOctets=_DvmrpInterfaceOutMcastOctets_Object((1,3,6,1,4,1,2076,60,2,9,1,11),_DvmrpInterfaceOutMcastOctets_Type())
dvmrpInterfaceOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceOutMcastOctets.setStatus(_A)
_DvmrpInterfaceHCInMcastOctets_Type=Counter64
_DvmrpInterfaceHCInMcastOctets_Object=MibTableColumn
dvmrpInterfaceHCInMcastOctets=_DvmrpInterfaceHCInMcastOctets_Object((1,3,6,1,4,1,2076,60,2,9,1,12),_DvmrpInterfaceHCInMcastOctets_Type())
dvmrpInterfaceHCInMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceHCInMcastOctets.setStatus(_A)
_DvmrpInterfaceHCOutMcastOctets_Type=Counter64
_DvmrpInterfaceHCOutMcastOctets_Object=MibTableColumn
dvmrpInterfaceHCOutMcastOctets=_DvmrpInterfaceHCOutMcastOctets_Object((1,3,6,1,4,1,2076,60,2,9,1,13),_DvmrpInterfaceHCOutMcastOctets_Type())
dvmrpInterfaceHCOutMcastOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpInterfaceHCOutMcastOctets.setStatus(_A)
_DvmrpNeighborTable_Object=MibTable
dvmrpNeighborTable=_DvmrpNeighborTable_Object((1,3,6,1,4,1,2076,60,2,10))
if mibBuilder.loadTexts:dvmrpNeighborTable.setStatus(_A)
_DvmrpNeighborEntry_Object=MibTableRow
dvmrpNeighborEntry=_DvmrpNeighborEntry_Object((1,3,6,1,4,1,2076,60,2,10,1))
dvmrpNeighborEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dvmrpNeighborEntry.setStatus(_A)
_DvmrpNeighborIfIndex_Type=InterfaceIndex
_DvmrpNeighborIfIndex_Object=MibTableColumn
dvmrpNeighborIfIndex=_DvmrpNeighborIfIndex_Object((1,3,6,1,4,1,2076,60,2,10,1,1),_DvmrpNeighborIfIndex_Type())
dvmrpNeighborIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborIfIndex.setStatus(_A)
_DvmrpNeighborAddress_Type=IpAddress
_DvmrpNeighborAddress_Object=MibTableColumn
dvmrpNeighborAddress=_DvmrpNeighborAddress_Object((1,3,6,1,4,1,2076,60,2,10,1,2),_DvmrpNeighborAddress_Type())
dvmrpNeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpNeighborAddress.setStatus(_A)
_DvmrpNeighborUpTime_Type=TimeTicks
_DvmrpNeighborUpTime_Object=MibTableColumn
dvmrpNeighborUpTime=_DvmrpNeighborUpTime_Object((1,3,6,1,4,1,2076,60,2,10,1,3),_DvmrpNeighborUpTime_Type())
dvmrpNeighborUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborUpTime.setStatus(_A)
_DvmrpNeighborExpiryTime_Type=TimeTicks
_DvmrpNeighborExpiryTime_Object=MibTableColumn
dvmrpNeighborExpiryTime=_DvmrpNeighborExpiryTime_Object((1,3,6,1,4,1,2076,60,2,10,1,4),_DvmrpNeighborExpiryTime_Type())
dvmrpNeighborExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborExpiryTime.setStatus(_A)
_DvmrpNeighborGenerationId_Type=Integer32
_DvmrpNeighborGenerationId_Object=MibTableColumn
dvmrpNeighborGenerationId=_DvmrpNeighborGenerationId_Object((1,3,6,1,4,1,2076,60,2,10,1,5),_DvmrpNeighborGenerationId_Type())
dvmrpNeighborGenerationId.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborGenerationId.setStatus(_A)
class _DvmrpNeighborMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMajorVersion_Type.__name__=_E
_DvmrpNeighborMajorVersion_Object=MibTableColumn
dvmrpNeighborMajorVersion=_DvmrpNeighborMajorVersion_Object((1,3,6,1,4,1,2076,60,2,10,1,6),_DvmrpNeighborMajorVersion_Type())
dvmrpNeighborMajorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborMajorVersion.setStatus(_A)
class _DvmrpNeighborMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMinorVersion_Type.__name__=_E
_DvmrpNeighborMinorVersion_Object=MibTableColumn
dvmrpNeighborMinorVersion=_DvmrpNeighborMinorVersion_Object((1,3,6,1,4,1,2076,60,2,10,1,7),_DvmrpNeighborMinorVersion_Type())
dvmrpNeighborMinorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborMinorVersion.setStatus(_A)
class _DvmrpNeighborCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_DvmrpNeighborCapabilities_Type.__name__=_E
_DvmrpNeighborCapabilities_Object=MibTableColumn
dvmrpNeighborCapabilities=_DvmrpNeighborCapabilities_Object((1,3,6,1,4,1,2076,60,2,10,1,8),_DvmrpNeighborCapabilities_Type())
dvmrpNeighborCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborCapabilities.setStatus(_A)
_DvmrpNeighborRcvRoutes_Type=Counter32
_DvmrpNeighborRcvRoutes_Object=MibTableColumn
dvmrpNeighborRcvRoutes=_DvmrpNeighborRcvRoutes_Object((1,3,6,1,4,1,2076,60,2,10,1,9),_DvmrpNeighborRcvRoutes_Type())
dvmrpNeighborRcvRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborRcvRoutes.setStatus(_A)
_DvmrpNeighborRcvBadPkts_Type=Counter32
_DvmrpNeighborRcvBadPkts_Object=MibTableColumn
dvmrpNeighborRcvBadPkts=_DvmrpNeighborRcvBadPkts_Object((1,3,6,1,4,1,2076,60,2,10,1,10),_DvmrpNeighborRcvBadPkts_Type())
dvmrpNeighborRcvBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadPkts.setStatus(_A)
_DvmrpNeighborRcvBadRoutes_Type=Counter32
_DvmrpNeighborRcvBadRoutes_Object=MibTableColumn
dvmrpNeighborRcvBadRoutes=_DvmrpNeighborRcvBadRoutes_Object((1,3,6,1,4,1,2076,60,2,10,1,11),_DvmrpNeighborRcvBadRoutes_Type())
dvmrpNeighborRcvBadRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadRoutes.setStatus(_A)
class _DvmrpNeighborAdjFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('established',0),('notEstablished',1)))
_DvmrpNeighborAdjFlag_Type.__name__=_E
_DvmrpNeighborAdjFlag_Object=MibTableColumn
dvmrpNeighborAdjFlag=_DvmrpNeighborAdjFlag_Object((1,3,6,1,4,1,2076,60,2,10,1,12),_DvmrpNeighborAdjFlag_Type())
dvmrpNeighborAdjFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpNeighborAdjFlag.setStatus(_A)
_DvmrpRouteTable_Object=MibTable
dvmrpRouteTable=_DvmrpRouteTable_Object((1,3,6,1,4,1,2076,60,2,11))
if mibBuilder.loadTexts:dvmrpRouteTable.setStatus(_A)
_DvmrpRouteEntry_Object=MibTableRow
dvmrpRouteEntry=_DvmrpRouteEntry_Object((1,3,6,1,4,1,2076,60,2,11,1))
dvmrpRouteEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:dvmrpRouteEntry.setStatus(_A)
_DvmrpRouteSource_Type=IpAddress
_DvmrpRouteSource_Object=MibTableColumn
dvmrpRouteSource=_DvmrpRouteSource_Object((1,3,6,1,4,1,2076,60,2,11,1,1),_DvmrpRouteSource_Type())
dvmrpRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteSource.setStatus(_A)
_DvmrpRouteSourceMask_Type=IpAddress
_DvmrpRouteSourceMask_Object=MibTableColumn
dvmrpRouteSourceMask=_DvmrpRouteSourceMask_Object((1,3,6,1,4,1,2076,60,2,11,1,2),_DvmrpRouteSourceMask_Type())
dvmrpRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteSourceMask.setStatus(_A)
_DvmrpRouteUpstreamNeighbor_Type=IpAddress
_DvmrpRouteUpstreamNeighbor_Object=MibTableColumn
dvmrpRouteUpstreamNeighbor=_DvmrpRouteUpstreamNeighbor_Object((1,3,6,1,4,1,2076,60,2,11,1,3),_DvmrpRouteUpstreamNeighbor_Type())
dvmrpRouteUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteUpstreamNeighbor.setStatus(_A)
_DvmrpRouteIfIndex_Type=InterfaceIndex
_DvmrpRouteIfIndex_Object=MibTableColumn
dvmrpRouteIfIndex=_DvmrpRouteIfIndex_Object((1,3,6,1,4,1,2076,60,2,11,1,4),_DvmrpRouteIfIndex_Type())
dvmrpRouteIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteIfIndex.setStatus(_A)
class _DvmrpRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DvmrpRouteMetric_Type.__name__=_E
_DvmrpRouteMetric_Object=MibTableColumn
dvmrpRouteMetric=_DvmrpRouteMetric_Object((1,3,6,1,4,1,2076,60,2,11,1,5),_DvmrpRouteMetric_Type())
dvmrpRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteMetric.setStatus(_A)
_DvmrpRouteExpiryTime_Type=TimeTicks
_DvmrpRouteExpiryTime_Object=MibTableColumn
dvmrpRouteExpiryTime=_DvmrpRouteExpiryTime_Object((1,3,6,1,4,1,2076,60,2,11,1,6),_DvmrpRouteExpiryTime_Type())
dvmrpRouteExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteExpiryTime.setStatus(_A)
_DvmrpRouteUpTime_Type=TimeTicks
_DvmrpRouteUpTime_Object=MibTableColumn
dvmrpRouteUpTime=_DvmrpRouteUpTime_Object((1,3,6,1,4,1,2076,60,2,11,1,7),_DvmrpRouteUpTime_Type())
dvmrpRouteUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteUpTime.setStatus(_A)
_DvmrpRouteStatus_Type=Integer32
_DvmrpRouteStatus_Object=MibTableColumn
dvmrpRouteStatus=_DvmrpRouteStatus_Object((1,3,6,1,4,1,2076,60,2,11,1,8),_DvmrpRouteStatus_Type())
dvmrpRouteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteStatus.setStatus(_A)
_DvmrpRouteNextHopTable_Object=MibTable
dvmrpRouteNextHopTable=_DvmrpRouteNextHopTable_Object((1,3,6,1,4,1,2076,60,2,12))
if mibBuilder.loadTexts:dvmrpRouteNextHopTable.setStatus(_A)
_DvmrpRouteNextHopEntry_Object=MibTableRow
dvmrpRouteNextHopEntry=_DvmrpRouteNextHopEntry_Object((1,3,6,1,4,1,2076,60,2,12,1))
dvmrpRouteNextHopEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:dvmrpRouteNextHopEntry.setStatus(_A)
_DvmrpRouteNextHopSource_Type=IpAddress
_DvmrpRouteNextHopSource_Object=MibTableColumn
dvmrpRouteNextHopSource=_DvmrpRouteNextHopSource_Object((1,3,6,1,4,1,2076,60,2,12,1,1),_DvmrpRouteNextHopSource_Type())
dvmrpRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopSource.setStatus(_A)
_DvmrpRouteNextHopSourceMask_Type=IpAddress
_DvmrpRouteNextHopSourceMask_Object=MibTableColumn
dvmrpRouteNextHopSourceMask=_DvmrpRouteNextHopSourceMask_Object((1,3,6,1,4,1,2076,60,2,12,1,2),_DvmrpRouteNextHopSourceMask_Type())
dvmrpRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopSourceMask.setStatus(_A)
_DvmrpRouteNextHopIfIndex_Type=InterfaceIndex
_DvmrpRouteNextHopIfIndex_Object=MibTableColumn
dvmrpRouteNextHopIfIndex=_DvmrpRouteNextHopIfIndex_Object((1,3,6,1,4,1,2076,60,2,12,1,3),_DvmrpRouteNextHopIfIndex_Type())
dvmrpRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopIfIndex.setStatus(_A)
class _DvmrpRouteNextHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leaf',1),('branch',2)))
_DvmrpRouteNextHopType_Type.__name__=_E
_DvmrpRouteNextHopType_Object=MibTableColumn
dvmrpRouteNextHopType=_DvmrpRouteNextHopType_Object((1,3,6,1,4,1,2076,60,2,12,1,4),_DvmrpRouteNextHopType_Type())
dvmrpRouteNextHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteNextHopType.setStatus(_A)
class _DvmrpRouteNextHopDesigForw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('true',0),('false',1)))
_DvmrpRouteNextHopDesigForw_Type.__name__=_E
_DvmrpRouteNextHopDesigForw_Object=MibTableColumn
dvmrpRouteNextHopDesigForw=_DvmrpRouteNextHopDesigForw_Object((1,3,6,1,4,1,2076,60,2,12,1,5),_DvmrpRouteNextHopDesigForw_Type())
dvmrpRouteNextHopDesigForw.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteNextHopDesigForw.setStatus(_A)
_DvmrpRouteNextHopDepNbrs_Type=DisplayString
_DvmrpRouteNextHopDepNbrs_Object=MibTableColumn
dvmrpRouteNextHopDepNbrs=_DvmrpRouteNextHopDepNbrs_Object((1,3,6,1,4,1,2076,60,2,12,1,6),_DvmrpRouteNextHopDepNbrs_Type())
dvmrpRouteNextHopDepNbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpRouteNextHopDepNbrs.setStatus(_A)
_DvmrpForwardTable_Object=MibTable
dvmrpForwardTable=_DvmrpForwardTable_Object((1,3,6,1,4,1,2076,60,2,13))
if mibBuilder.loadTexts:dvmrpForwardTable.setStatus(_A)
_DvmrpForwardEntry_Object=MibTableRow
dvmrpForwardEntry=_DvmrpForwardEntry_Object((1,3,6,1,4,1,2076,60,2,13,1))
dvmrpForwardEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:dvmrpForwardEntry.setStatus(_A)
_DvmrpSourceNetwork_Type=IpAddress
_DvmrpSourceNetwork_Object=MibTableColumn
dvmrpSourceNetwork=_DvmrpSourceNetwork_Object((1,3,6,1,4,1,2076,60,2,13,1,1),_DvmrpSourceNetwork_Type())
dvmrpSourceNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpSourceNetwork.setStatus(_A)
_DvmrpGroupAddress_Type=IpAddress
_DvmrpGroupAddress_Object=MibTableColumn
dvmrpGroupAddress=_DvmrpGroupAddress_Object((1,3,6,1,4,1,2076,60,2,13,1,2),_DvmrpGroupAddress_Type())
dvmrpGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpGroupAddress.setStatus(_A)
_DvmrpForwardUpstreamNeighbor_Type=IpAddress
_DvmrpForwardUpstreamNeighbor_Object=MibTableColumn
dvmrpForwardUpstreamNeighbor=_DvmrpForwardUpstreamNeighbor_Object((1,3,6,1,4,1,2076,60,2,13,1,3),_DvmrpForwardUpstreamNeighbor_Type())
dvmrpForwardUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardUpstreamNeighbor.setStatus(_A)
_DvmrpForwardInIfIndex_Type=InterfaceIndex
_DvmrpForwardInIfIndex_Object=MibTableColumn
dvmrpForwardInIfIndex=_DvmrpForwardInIfIndex_Object((1,3,6,1,4,1,2076,60,2,13,1,4),_DvmrpForwardInIfIndex_Type())
dvmrpForwardInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardInIfIndex.setStatus(_A)
class _DvmrpForwardInIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10)));namedValues=NamedValues(*(('graftAckReceived',5),('waitingGraftAck',6),('normal',7),(_P,8),('dataOnPrunedIface',9),('localNetwork',10)))
_DvmrpForwardInIfState_Type.__name__=_E
_DvmrpForwardInIfState_Object=MibTableColumn
dvmrpForwardInIfState=_DvmrpForwardInIfState_Object((1,3,6,1,4,1,2076,60,2,13,1,5),_DvmrpForwardInIfState_Type())
dvmrpForwardInIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardInIfState.setStatus(_A)
_DvmrpForwardExpiryTime_Type=TimeTicks
_DvmrpForwardExpiryTime_Object=MibTableColumn
dvmrpForwardExpiryTime=_DvmrpForwardExpiryTime_Object((1,3,6,1,4,1,2076,60,2,13,1,6),_DvmrpForwardExpiryTime_Type())
dvmrpForwardExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardExpiryTime.setStatus(_A)
class _DvmrpForwardTblStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_DvmrpForwardTblStatus_Type.__name__=_E
_DvmrpForwardTblStatus_Object=MibTableColumn
dvmrpForwardTblStatus=_DvmrpForwardTblStatus_Object((1,3,6,1,4,1,2076,60,2,13,1,7),_DvmrpForwardTblStatus_Type())
dvmrpForwardTblStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardTblStatus.setStatus(_A)
_DvmrpForwardPruneNbrTable_Object=MibTable
dvmrpForwardPruneNbrTable=_DvmrpForwardPruneNbrTable_Object((1,3,6,1,4,1,2076,60,2,14))
if mibBuilder.loadTexts:dvmrpForwardPruneNbrTable.setStatus(_A)
_DvmrpForwardPruneNbrEntry_Object=MibTableRow
dvmrpForwardPruneNbrEntry=_DvmrpForwardPruneNbrEntry_Object((1,3,6,1,4,1,2076,60,2,14,1))
dvmrpForwardPruneNbrEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:dvmrpForwardPruneNbrEntry.setStatus(_A)
_DvmrpForwardSourceNetwork_Type=IpAddress
_DvmrpForwardSourceNetwork_Object=MibTableColumn
dvmrpForwardSourceNetwork=_DvmrpForwardSourceNetwork_Object((1,3,6,1,4,1,2076,60,2,14,1,1),_DvmrpForwardSourceNetwork_Type())
dvmrpForwardSourceNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpForwardSourceNetwork.setStatus(_A)
_DvmrpForwardGroupAddress_Type=IpAddress
_DvmrpForwardGroupAddress_Object=MibTableColumn
dvmrpForwardGroupAddress=_DvmrpForwardGroupAddress_Object((1,3,6,1,4,1,2076,60,2,14,1,2),_DvmrpForwardGroupAddress_Type())
dvmrpForwardGroupAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpForwardGroupAddress.setStatus(_A)
_DvmrpForwardIfIndex_Type=InterfaceIndex
_DvmrpForwardIfIndex_Object=MibTableColumn
dvmrpForwardIfIndex=_DvmrpForwardIfIndex_Object((1,3,6,1,4,1,2076,60,2,14,1,3),_DvmrpForwardIfIndex_Type())
dvmrpForwardIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpForwardIfIndex.setStatus(_A)
_DvmrpForwardPruneNeighbor_Type=IpAddress
_DvmrpForwardPruneNeighbor_Object=MibTableColumn
dvmrpForwardPruneNeighbor=_DvmrpForwardPruneNeighbor_Object((1,3,6,1,4,1,2076,60,2,14,1,4),_DvmrpForwardPruneNeighbor_Type())
dvmrpForwardPruneNeighbor.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpForwardPruneNeighbor.setStatus(_A)
_DvmrpForwardNbrPruneTime_Type=TimeTicks
_DvmrpForwardNbrPruneTime_Object=MibTableColumn
dvmrpForwardNbrPruneTime=_DvmrpForwardNbrPruneTime_Object((1,3,6,1,4,1,2076,60,2,14,1,5),_DvmrpForwardNbrPruneTime_Type())
dvmrpForwardNbrPruneTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpForwardNbrPruneTime.setStatus(_A)
_DvmrpIpMRTable_Object=MibTable
dvmrpIpMRTable=_DvmrpIpMRTable_Object((1,3,6,1,4,1,2076,60,2,15))
if mibBuilder.loadTexts:dvmrpIpMRTable.setStatus(_A)
_DvmrpIpMREntry_Object=MibTableRow
dvmrpIpMREntry=_DvmrpIpMREntry_Object((1,3,6,1,4,1,2076,60,2,15,1))
dvmrpIpMREntry.setIndexNames((0,_C,_U),(0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:dvmrpIpMREntry.setStatus(_A)
_DvmrpIpMRGroup_Type=IpAddress
_DvmrpIpMRGroup_Object=MibTableColumn
dvmrpIpMRGroup=_DvmrpIpMRGroup_Object((1,3,6,1,4,1,2076,60,2,15,1,1),_DvmrpIpMRGroup_Type())
dvmrpIpMRGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMRGroup.setStatus(_A)
_DvmrpIpMRSource_Type=IpAddress
_DvmrpIpMRSource_Object=MibTableColumn
dvmrpIpMRSource=_DvmrpIpMRSource_Object((1,3,6,1,4,1,2076,60,2,15,1,2),_DvmrpIpMRSource_Type())
dvmrpIpMRSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMRSource.setStatus(_A)
_DvmrpIpMRSourceMask_Type=IpAddress
_DvmrpIpMRSourceMask_Object=MibTableColumn
dvmrpIpMRSourceMask=_DvmrpIpMRSourceMask_Object((1,3,6,1,4,1,2076,60,2,15,1,3),_DvmrpIpMRSourceMask_Type())
dvmrpIpMRSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMRSourceMask.setStatus(_A)
_DvmrpIpMRUpstreamNeighbor_Type=IpAddress
_DvmrpIpMRUpstreamNeighbor_Object=MibTableColumn
dvmrpIpMRUpstreamNeighbor=_DvmrpIpMRUpstreamNeighbor_Object((1,3,6,1,4,1,2076,60,2,15,1,4),_DvmrpIpMRUpstreamNeighbor_Type())
dvmrpIpMRUpstreamNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRUpstreamNeighbor.setStatus(_A)
_DvmrpIpMRInIfIndex_Type=InterfaceIndexOrZero
_DvmrpIpMRInIfIndex_Object=MibTableColumn
dvmrpIpMRInIfIndex=_DvmrpIpMRInIfIndex_Object((1,3,6,1,4,1,2076,60,2,15,1,5),_DvmrpIpMRInIfIndex_Type())
dvmrpIpMRInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRInIfIndex.setStatus(_A)
_DvmrpIpMRUpTime_Type=TimeTicks
_DvmrpIpMRUpTime_Object=MibTableColumn
dvmrpIpMRUpTime=_DvmrpIpMRUpTime_Object((1,3,6,1,4,1,2076,60,2,15,1,6),_DvmrpIpMRUpTime_Type())
dvmrpIpMRUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRUpTime.setStatus(_A)
_DvmrpIpMRExpiryTime_Type=TimeTicks
_DvmrpIpMRExpiryTime_Object=MibTableColumn
dvmrpIpMRExpiryTime=_DvmrpIpMRExpiryTime_Object((1,3,6,1,4,1,2076,60,2,15,1,7),_DvmrpIpMRExpiryTime_Type())
dvmrpIpMRExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRExpiryTime.setStatus(_A)
_DvmrpIpMRPkts_Type=Counter32
_DvmrpIpMRPkts_Object=MibTableColumn
dvmrpIpMRPkts=_DvmrpIpMRPkts_Object((1,3,6,1,4,1,2076,60,2,15,1,8),_DvmrpIpMRPkts_Type())
dvmrpIpMRPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRPkts.setStatus(_A)
_DvmrpIpMRDifferentInIfPackets_Type=Counter32
_DvmrpIpMRDifferentInIfPackets_Object=MibTableColumn
dvmrpIpMRDifferentInIfPackets=_DvmrpIpMRDifferentInIfPackets_Object((1,3,6,1,4,1,2076,60,2,15,1,9),_DvmrpIpMRDifferentInIfPackets_Type())
dvmrpIpMRDifferentInIfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRDifferentInIfPackets.setStatus(_A)
_DvmrpIpMROctets_Type=Counter32
_DvmrpIpMROctets_Object=MibTableColumn
dvmrpIpMROctets=_DvmrpIpMROctets_Object((1,3,6,1,4,1,2076,60,2,15,1,10),_DvmrpIpMROctets_Type())
dvmrpIpMROctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMROctets.setStatus(_A)
_DvmrpIpMRProtocol_Type=IANAipMRouteProtocol
_DvmrpIpMRProtocol_Object=MibTableColumn
dvmrpIpMRProtocol=_DvmrpIpMRProtocol_Object((1,3,6,1,4,1,2076,60,2,15,1,11),_DvmrpIpMRProtocol_Type())
dvmrpIpMRProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRProtocol.setStatus(_A)
_DvmrpIpMRRtProto_Type=IANAipRouteProtocol
_DvmrpIpMRRtProto_Object=MibTableColumn
dvmrpIpMRRtProto=_DvmrpIpMRRtProto_Object((1,3,6,1,4,1,2076,60,2,15,1,12),_DvmrpIpMRRtProto_Type())
dvmrpIpMRRtProto.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRRtProto.setStatus(_A)
_DvmrpIpMRRtAddress_Type=IpAddress
_DvmrpIpMRRtAddress_Object=MibTableColumn
dvmrpIpMRRtAddress=_DvmrpIpMRRtAddress_Object((1,3,6,1,4,1,2076,60,2,15,1,13),_DvmrpIpMRRtAddress_Type())
dvmrpIpMRRtAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRRtAddress.setStatus(_A)
_DvmrpIpMRRtMask_Type=IpAddress
_DvmrpIpMRRtMask_Object=MibTableColumn
dvmrpIpMRRtMask=_DvmrpIpMRRtMask_Object((1,3,6,1,4,1,2076,60,2,15,1,14),_DvmrpIpMRRtMask_Type())
dvmrpIpMRRtMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRRtMask.setStatus(_A)
class _DvmrpIpMRRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_DvmrpIpMRRtType_Type.__name__=_E
_DvmrpIpMRRtType_Object=MibTableColumn
dvmrpIpMRRtType=_DvmrpIpMRRtType_Object((1,3,6,1,4,1,2076,60,2,15,1,15),_DvmrpIpMRRtType_Type())
dvmrpIpMRRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRRtType.setStatus(_A)
_DvmrpIpMRHCOctets_Type=Counter64
_DvmrpIpMRHCOctets_Object=MibTableColumn
dvmrpIpMRHCOctets=_DvmrpIpMRHCOctets_Object((1,3,6,1,4,1,2076,60,2,15,1,16),_DvmrpIpMRHCOctets_Type())
dvmrpIpMRHCOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMRHCOctets.setStatus(_A)
_DvmrpIpMNextHopTable_Object=MibTable
dvmrpIpMNextHopTable=_DvmrpIpMNextHopTable_Object((1,3,6,1,4,1,2076,60,2,16))
if mibBuilder.loadTexts:dvmrpIpMNextHopTable.setStatus(_A)
_DvmrpIpMNextHopEntry_Object=MibTableRow
dvmrpIpMNextHopEntry=_DvmrpIpMNextHopEntry_Object((1,3,6,1,4,1,2076,60,2,16,1))
dvmrpIpMNextHopEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:dvmrpIpMNextHopEntry.setStatus(_A)
_DvmrpIpMNextHopGroup_Type=IpAddress
_DvmrpIpMNextHopGroup_Object=MibTableColumn
dvmrpIpMNextHopGroup=_DvmrpIpMNextHopGroup_Object((1,3,6,1,4,1,2076,60,2,16,1,1),_DvmrpIpMNextHopGroup_Type())
dvmrpIpMNextHopGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMNextHopGroup.setStatus(_A)
_DvmrpIpMNextHopSource_Type=IpAddress
_DvmrpIpMNextHopSource_Object=MibTableColumn
dvmrpIpMNextHopSource=_DvmrpIpMNextHopSource_Object((1,3,6,1,4,1,2076,60,2,16,1,2),_DvmrpIpMNextHopSource_Type())
dvmrpIpMNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMNextHopSource.setStatus(_A)
_DvmrpIpMNextHopSourceMask_Type=IpAddress
_DvmrpIpMNextHopSourceMask_Object=MibTableColumn
dvmrpIpMNextHopSourceMask=_DvmrpIpMNextHopSourceMask_Object((1,3,6,1,4,1,2076,60,2,16,1,3),_DvmrpIpMNextHopSourceMask_Type())
dvmrpIpMNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMNextHopSourceMask.setStatus(_A)
_DvmrpIpMNextHopIfIndex_Type=InterfaceIndex
_DvmrpIpMNextHopIfIndex_Object=MibTableColumn
dvmrpIpMNextHopIfIndex=_DvmrpIpMNextHopIfIndex_Object((1,3,6,1,4,1,2076,60,2,16,1,4),_DvmrpIpMNextHopIfIndex_Type())
dvmrpIpMNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMNextHopIfIndex.setStatus(_A)
_DvmrpIpMNextHopAddress_Type=IpAddress
_DvmrpIpMNextHopAddress_Object=MibTableColumn
dvmrpIpMNextHopAddress=_DvmrpIpMNextHopAddress_Object((1,3,6,1,4,1,2076,60,2,16,1,5),_DvmrpIpMNextHopAddress_Type())
dvmrpIpMNextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpIpMNextHopAddress.setStatus(_A)
class _DvmrpIpMNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('forwarding',2)))
_DvmrpIpMNextHopState_Type.__name__=_E
_DvmrpIpMNextHopState_Object=MibTableColumn
dvmrpIpMNextHopState=_DvmrpIpMNextHopState_Object((1,3,6,1,4,1,2076,60,2,16,1,6),_DvmrpIpMNextHopState_Type())
dvmrpIpMNextHopState.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMNextHopState.setStatus(_A)
_DvmrpIpMNextHopUpTime_Type=TimeTicks
_DvmrpIpMNextHopUpTime_Object=MibTableColumn
dvmrpIpMNextHopUpTime=_DvmrpIpMNextHopUpTime_Object((1,3,6,1,4,1,2076,60,2,16,1,7),_DvmrpIpMNextHopUpTime_Type())
dvmrpIpMNextHopUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMNextHopUpTime.setStatus(_A)
_DvmrpIpMNextHopExpiryTime_Type=TimeTicks
_DvmrpIpMNextHopExpiryTime_Object=MibTableColumn
dvmrpIpMNextHopExpiryTime=_DvmrpIpMNextHopExpiryTime_Object((1,3,6,1,4,1,2076,60,2,16,1,8),_DvmrpIpMNextHopExpiryTime_Type())
dvmrpIpMNextHopExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMNextHopExpiryTime.setStatus(_A)
_DvmrpIpMNextHopProtocol_Type=IANAipMRouteProtocol
_DvmrpIpMNextHopProtocol_Object=MibTableColumn
dvmrpIpMNextHopProtocol=_DvmrpIpMNextHopProtocol_Object((1,3,6,1,4,1,2076,60,2,16,1,9),_DvmrpIpMNextHopProtocol_Type())
dvmrpIpMNextHopProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMNextHopProtocol.setStatus(_A)
_DvmrpIpMNextHopPkts_Type=Counter32
_DvmrpIpMNextHopPkts_Object=MibTableColumn
dvmrpIpMNextHopPkts=_DvmrpIpMNextHopPkts_Object((1,3,6,1,4,1,2076,60,2,16,1,10),_DvmrpIpMNextHopPkts_Type())
dvmrpIpMNextHopPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dvmrpIpMNextHopPkts.setStatus(_A)
_DvmrpMIBConformance_ObjectIdentity=ObjectIdentity
dvmrpMIBConformance=_DvmrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,2076,60,3))
_DvmrpMIBCompliances_ObjectIdentity=ObjectIdentity
dvmrpMIBCompliances=_DvmrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2076,60,3,1))
_DvmrpMIBGroups_ObjectIdentity=ObjectIdentity
dvmrpMIBGroups=_DvmrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,2076,60,3,2))
dvmrpGeneralGroup=ObjectGroup((1,3,6,1,4,1,2076,60,3,2,2))
dvmrpGeneralGroup.setObjects(*((_C,_c),(_C,_d),(_C,_e),(_C,_f)))
if mibBuilder.loadTexts:dvmrpGeneralGroup.setStatus(_A)
dvmrpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,2076,60,3,2,3))
dvmrpInterfaceGroup.setObjects(*((_C,_g),(_C,_h),(_C,_i),(_C,_j)))
if mibBuilder.loadTexts:dvmrpInterfaceGroup.setStatus(_A)
dvmrpNeighborGroup=ObjectGroup((1,3,6,1,4,1,2076,60,3,2,4))
dvmrpNeighborGroup.setObjects(*((_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p),(_C,_q),(_C,_r),(_C,_s)))
if mibBuilder.loadTexts:dvmrpNeighborGroup.setStatus(_A)
dvmrpRoutingGroup=ObjectGroup((1,3,6,1,4,1,2076,60,3,2,5))
dvmrpRoutingGroup.setObjects(*((_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y)))
if mibBuilder.loadTexts:dvmrpRoutingGroup.setStatus(_A)
dvmrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2076,60,3,1,1))
dvmrpMIBCompliance.setObjects(*((_C,_z),(_C,_A0),(_C,_A1),(_C,_A2)))
if mibBuilder.loadTexts:dvmrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Integer8':Integer8,'Integer16':Integer16,'dvmrpMIB':dvmrpMIB,'dvmrpScalar':dvmrpScalar,_c:dvmrpVersionString,_d:dvmrpGenerationId,_e:dvmrpNumRoutes,_f:dvmrpReachableRoutes,'dvmrpStatus':dvmrpStatus,'dvmrpLogEnabled':dvmrpLogEnabled,'dvmrpLogMask':dvmrpLogMask,'dvmrpPruneLifeTime':dvmrpPruneLifeTime,'dvmrp':dvmrp,'dvmrpInterfaceTable':dvmrpInterfaceTable,'dvmrpInterfaceEntry':dvmrpInterfaceEntry,_G:dvmrpInterfaceIfIndex,'dvmrpInterfaceStatus':dvmrpInterfaceStatus,_g:dvmrpInterfaceLocalAddress,_h:dvmrpInterfaceMetric,_i:dvmrpInterfaceRcvBadPkts,_j:dvmrpInterfaceRcvBadRoutes,'dvmrpInterfaceTtl':dvmrpInterfaceTtl,'dvmrpInterfaceProtocol':dvmrpInterfaceProtocol,'dvmrpInterfaceRateLimit':dvmrpInterfaceRateLimit,'dvmrpInterfaceInMcastOctets':dvmrpInterfaceInMcastOctets,'dvmrpInterfaceOutMcastOctets':dvmrpInterfaceOutMcastOctets,'dvmrpInterfaceHCInMcastOctets':dvmrpInterfaceHCInMcastOctets,'dvmrpInterfaceHCOutMcastOctets':dvmrpInterfaceHCOutMcastOctets,'dvmrpNeighborTable':dvmrpNeighborTable,'dvmrpNeighborEntry':dvmrpNeighborEntry,'dvmrpNeighborIfIndex':dvmrpNeighborIfIndex,_H:dvmrpNeighborAddress,_k:dvmrpNeighborUpTime,_l:dvmrpNeighborExpiryTime,_m:dvmrpNeighborGenerationId,_n:dvmrpNeighborMajorVersion,_o:dvmrpNeighborMinorVersion,_p:dvmrpNeighborCapabilities,_q:dvmrpNeighborRcvRoutes,_r:dvmrpNeighborRcvBadPkts,_s:dvmrpNeighborRcvBadRoutes,'dvmrpNeighborAdjFlag':dvmrpNeighborAdjFlag,'dvmrpRouteTable':dvmrpRouteTable,'dvmrpRouteEntry':dvmrpRouteEntry,_I:dvmrpRouteSource,_J:dvmrpRouteSourceMask,_t:dvmrpRouteUpstreamNeighbor,_u:dvmrpRouteIfIndex,_v:dvmrpRouteMetric,_w:dvmrpRouteExpiryTime,_x:dvmrpRouteUpTime,'dvmrpRouteStatus':dvmrpRouteStatus,'dvmrpRouteNextHopTable':dvmrpRouteNextHopTable,'dvmrpRouteNextHopEntry':dvmrpRouteNextHopEntry,_K:dvmrpRouteNextHopSource,_L:dvmrpRouteNextHopSourceMask,_M:dvmrpRouteNextHopIfIndex,_y:dvmrpRouteNextHopType,'dvmrpRouteNextHopDesigForw':dvmrpRouteNextHopDesigForw,'dvmrpRouteNextHopDepNbrs':dvmrpRouteNextHopDepNbrs,'dvmrpForwardTable':dvmrpForwardTable,'dvmrpForwardEntry':dvmrpForwardEntry,_N:dvmrpSourceNetwork,_O:dvmrpGroupAddress,'dvmrpForwardUpstreamNeighbor':dvmrpForwardUpstreamNeighbor,'dvmrpForwardInIfIndex':dvmrpForwardInIfIndex,'dvmrpForwardInIfState':dvmrpForwardInIfState,'dvmrpForwardExpiryTime':dvmrpForwardExpiryTime,'dvmrpForwardTblStatus':dvmrpForwardTblStatus,'dvmrpForwardPruneNbrTable':dvmrpForwardPruneNbrTable,'dvmrpForwardPruneNbrEntry':dvmrpForwardPruneNbrEntry,_Q:dvmrpForwardSourceNetwork,_R:dvmrpForwardGroupAddress,_S:dvmrpForwardIfIndex,_T:dvmrpForwardPruneNeighbor,'dvmrpForwardNbrPruneTime':dvmrpForwardNbrPruneTime,'dvmrpIpMRTable':dvmrpIpMRTable,'dvmrpIpMREntry':dvmrpIpMREntry,_U:dvmrpIpMRGroup,_V:dvmrpIpMRSource,_W:dvmrpIpMRSourceMask,'dvmrpIpMRUpstreamNeighbor':dvmrpIpMRUpstreamNeighbor,'dvmrpIpMRInIfIndex':dvmrpIpMRInIfIndex,'dvmrpIpMRUpTime':dvmrpIpMRUpTime,'dvmrpIpMRExpiryTime':dvmrpIpMRExpiryTime,'dvmrpIpMRPkts':dvmrpIpMRPkts,'dvmrpIpMRDifferentInIfPackets':dvmrpIpMRDifferentInIfPackets,'dvmrpIpMROctets':dvmrpIpMROctets,'dvmrpIpMRProtocol':dvmrpIpMRProtocol,'dvmrpIpMRRtProto':dvmrpIpMRRtProto,'dvmrpIpMRRtAddress':dvmrpIpMRRtAddress,'dvmrpIpMRRtMask':dvmrpIpMRRtMask,'dvmrpIpMRRtType':dvmrpIpMRRtType,'dvmrpIpMRHCOctets':dvmrpIpMRHCOctets,'dvmrpIpMNextHopTable':dvmrpIpMNextHopTable,'dvmrpIpMNextHopEntry':dvmrpIpMNextHopEntry,_X:dvmrpIpMNextHopGroup,_Y:dvmrpIpMNextHopSource,_Z:dvmrpIpMNextHopSourceMask,_a:dvmrpIpMNextHopIfIndex,_b:dvmrpIpMNextHopAddress,'dvmrpIpMNextHopState':dvmrpIpMNextHopState,'dvmrpIpMNextHopUpTime':dvmrpIpMNextHopUpTime,'dvmrpIpMNextHopExpiryTime':dvmrpIpMNextHopExpiryTime,'dvmrpIpMNextHopProtocol':dvmrpIpMNextHopProtocol,'dvmrpIpMNextHopPkts':dvmrpIpMNextHopPkts,'dvmrpMIBConformance':dvmrpMIBConformance,'dvmrpMIBCompliances':dvmrpMIBCompliances,'dvmrpMIBCompliance':dvmrpMIBCompliance,'dvmrpMIBGroups':dvmrpMIBGroups,_z:dvmrpGeneralGroup,_A0:dvmrpInterfaceGroup,_A1:dvmrpNeighborGroup,_A2:dvmrpRoutingGroup})