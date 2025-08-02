_A1='dvmrpSecurityGroup'
_A0='dvmrpTreeGroup'
_z='dvmrpRoutingGroup'
_y='dvmrpNeighborGroup'
_x='dvmrpInterfaceGroup'
_w='dvmrpGeneralGroup'
_v='dvmrpNeighborNotPruning'
_u='dvmrpNeighborLoss'
_t='dvmrpPruneExpiryTime'
_s='dvmrpInterfaceInterfaceKeyVersion'
_r='dvmrpInterfaceInterfaceKey'
_q='dvmrpRouteNextHopType'
_p='dvmrpRouteUpTime'
_o='dvmrpRouteExpiryTime'
_n='dvmrpRouteMetric'
_m='dvmrpRouteIfIndex'
_l='dvmrpRouteUpstreamNeighbor'
_k='dvmrpNeighborRcvBadRoutes'
_j='dvmrpNeighborRcvBadPkts'
_i='dvmrpNeighborRcvRoutes'
_h='dvmrpNeighborMinorVersion'
_g='dvmrpNeighborMajorVersion'
_f='dvmrpNeighborGenerationId'
_e='dvmrpNeighborExpiryTime'
_d='dvmrpNeighborUpTime'
_c='dvmrpInterfaceSentRoutes'
_b='dvmrpInterfaceRcvBadRoutes'
_a='dvmrpInterfaceRcvBadPkts'
_Z='dvmrpInterfaceStatus'
_Y='dvmrpInterfaceMetric'
_X='dvmrpReachableRoutes'
_W='dvmrpNumRoutes'
_V='dvmrpGenerationId'
_U='dvmrpVersionString'
_T='dvmrpPruneSourceMask'
_S='dvmrpPruneSource'
_R='dvmrpPruneGroup'
_Q='dvmrpRouteNextHopIfIndex'
_P='dvmrpRouteNextHopSourceMask'
_O='dvmrpRouteNextHopSource'
_N='dvmrpRouteSourceMask'
_M='dvmrpRouteSource'
_L='dvmrpNeighborAddress'
_K='dvmrpNeighborIfIndex'
_J='dvmrpInterfaceIfIndex'
_I='dvmrpNeighborState'
_H='dvmrpNeighborCapabilities'
_G='dvmrpInterfaceLocalAddress'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='DVMRP-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
dvmrpStdMIB=ModuleIdentity((1,3,6,1,4,1,4413,1,1,10))
if mibBuilder.loadTexts:dvmrpStdMIB.setRevisions(('1999-10-19 12:00',))
_DvmrpMIBObjects_ObjectIdentity=ObjectIdentity
dvmrpMIBObjects=_DvmrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,1))
_Dvmrp_ObjectIdentity=ObjectIdentity
dvmrp=_Dvmrp_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,1,1))
_DvmrpScalar_ObjectIdentity=ObjectIdentity
dvmrpScalar=_DvmrpScalar_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,1,1,1))
_DvmrpVersionString_Type=DisplayString
_DvmrpVersionString_Object=MibScalar
dvmrpVersionString=_DvmrpVersionString_Object((1,3,6,1,4,1,4413,1,1,10,1,1,1,1),_DvmrpVersionString_Type())
dvmrpVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpVersionString.setStatus(_A)
_DvmrpGenerationId_Type=Integer32
_DvmrpGenerationId_Object=MibScalar
dvmrpGenerationId=_DvmrpGenerationId_Object((1,3,6,1,4,1,4413,1,1,10,1,1,1,2),_DvmrpGenerationId_Type())
dvmrpGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpGenerationId.setStatus(_A)
_DvmrpNumRoutes_Type=Gauge32
_DvmrpNumRoutes_Object=MibScalar
dvmrpNumRoutes=_DvmrpNumRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,1,3),_DvmrpNumRoutes_Type())
dvmrpNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNumRoutes.setStatus(_A)
_DvmrpReachableRoutes_Type=Gauge32
_DvmrpReachableRoutes_Object=MibScalar
dvmrpReachableRoutes=_DvmrpReachableRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,1,4),_DvmrpReachableRoutes_Type())
dvmrpReachableRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpReachableRoutes.setStatus(_A)
_DvmrpInterfaceTable_Object=MibTable
dvmrpInterfaceTable=_DvmrpInterfaceTable_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2))
if mibBuilder.loadTexts:dvmrpInterfaceTable.setStatus(_A)
_DvmrpInterfaceEntry_Object=MibTableRow
dvmrpInterfaceEntry=_DvmrpInterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1))
dvmrpInterfaceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:dvmrpInterfaceEntry.setStatus(_A)
_DvmrpInterfaceIfIndex_Type=InterfaceIndex
_DvmrpInterfaceIfIndex_Object=MibTableColumn
dvmrpInterfaceIfIndex=_DvmrpInterfaceIfIndex_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,1),_DvmrpInterfaceIfIndex_Type())
dvmrpInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpInterfaceIfIndex.setStatus(_A)
_DvmrpInterfaceLocalAddress_Type=IpAddress
_DvmrpInterfaceLocalAddress_Object=MibTableColumn
dvmrpInterfaceLocalAddress=_DvmrpInterfaceLocalAddress_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,2),_DvmrpInterfaceLocalAddress_Type())
dvmrpInterfaceLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceLocalAddress.setStatus(_A)
class _DvmrpInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_DvmrpInterfaceMetric_Type.__name__=_E
_DvmrpInterfaceMetric_Object=MibTableColumn
dvmrpInterfaceMetric=_DvmrpInterfaceMetric_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,3),_DvmrpInterfaceMetric_Type())
dvmrpInterfaceMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceMetric.setStatus(_A)
_DvmrpInterfaceStatus_Type=RowStatus
_DvmrpInterfaceStatus_Object=MibTableColumn
dvmrpInterfaceStatus=_DvmrpInterfaceStatus_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,4),_DvmrpInterfaceStatus_Type())
dvmrpInterfaceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceStatus.setStatus(_A)
_DvmrpInterfaceRcvBadPkts_Type=Counter32
_DvmrpInterfaceRcvBadPkts_Object=MibTableColumn
dvmrpInterfaceRcvBadPkts=_DvmrpInterfaceRcvBadPkts_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,5),_DvmrpInterfaceRcvBadPkts_Type())
dvmrpInterfaceRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadPkts.setStatus(_A)
_DvmrpInterfaceRcvBadRoutes_Type=Counter32
_DvmrpInterfaceRcvBadRoutes_Object=MibTableColumn
dvmrpInterfaceRcvBadRoutes=_DvmrpInterfaceRcvBadRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,6),_DvmrpInterfaceRcvBadRoutes_Type())
dvmrpInterfaceRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceRcvBadRoutes.setStatus(_A)
_DvmrpInterfaceSentRoutes_Type=Counter32
_DvmrpInterfaceSentRoutes_Object=MibTableColumn
dvmrpInterfaceSentRoutes=_DvmrpInterfaceSentRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,7),_DvmrpInterfaceSentRoutes_Type())
dvmrpInterfaceSentRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpInterfaceSentRoutes.setStatus(_A)
_DvmrpInterfaceInterfaceKey_Type=SnmpAdminString
_DvmrpInterfaceInterfaceKey_Object=MibTableColumn
dvmrpInterfaceInterfaceKey=_DvmrpInterfaceInterfaceKey_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,8),_DvmrpInterfaceInterfaceKey_Type())
dvmrpInterfaceInterfaceKey.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceInterfaceKey.setStatus(_A)
_DvmrpInterfaceInterfaceKeyVersion_Type=Integer32
_DvmrpInterfaceInterfaceKeyVersion_Object=MibTableColumn
dvmrpInterfaceInterfaceKeyVersion=_DvmrpInterfaceInterfaceKeyVersion_Object((1,3,6,1,4,1,4413,1,1,10,1,1,2,1,9),_DvmrpInterfaceInterfaceKeyVersion_Type())
dvmrpInterfaceInterfaceKeyVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:dvmrpInterfaceInterfaceKeyVersion.setStatus(_A)
_DvmrpNeighborTable_Object=MibTable
dvmrpNeighborTable=_DvmrpNeighborTable_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3))
if mibBuilder.loadTexts:dvmrpNeighborTable.setStatus(_A)
_DvmrpNeighborEntry_Object=MibTableRow
dvmrpNeighborEntry=_DvmrpNeighborEntry_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1))
dvmrpNeighborEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:dvmrpNeighborEntry.setStatus(_A)
_DvmrpNeighborIfIndex_Type=InterfaceIndex
_DvmrpNeighborIfIndex_Object=MibTableColumn
dvmrpNeighborIfIndex=_DvmrpNeighborIfIndex_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,1),_DvmrpNeighborIfIndex_Type())
dvmrpNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpNeighborIfIndex.setStatus(_A)
_DvmrpNeighborAddress_Type=IpAddress
_DvmrpNeighborAddress_Object=MibTableColumn
dvmrpNeighborAddress=_DvmrpNeighborAddress_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,2),_DvmrpNeighborAddress_Type())
dvmrpNeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpNeighborAddress.setStatus(_A)
_DvmrpNeighborUpTime_Type=TimeTicks
_DvmrpNeighborUpTime_Object=MibTableColumn
dvmrpNeighborUpTime=_DvmrpNeighborUpTime_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,3),_DvmrpNeighborUpTime_Type())
dvmrpNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborUpTime.setStatus(_A)
_DvmrpNeighborExpiryTime_Type=TimeTicks
_DvmrpNeighborExpiryTime_Object=MibTableColumn
dvmrpNeighborExpiryTime=_DvmrpNeighborExpiryTime_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,4),_DvmrpNeighborExpiryTime_Type())
dvmrpNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborExpiryTime.setStatus(_A)
_DvmrpNeighborGenerationId_Type=Integer32
_DvmrpNeighborGenerationId_Object=MibTableColumn
dvmrpNeighborGenerationId=_DvmrpNeighborGenerationId_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,5),_DvmrpNeighborGenerationId_Type())
dvmrpNeighborGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborGenerationId.setStatus(_A)
class _DvmrpNeighborMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMajorVersion_Type.__name__=_E
_DvmrpNeighborMajorVersion_Object=MibTableColumn
dvmrpNeighborMajorVersion=_DvmrpNeighborMajorVersion_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,6),_DvmrpNeighborMajorVersion_Type())
dvmrpNeighborMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborMajorVersion.setStatus(_A)
class _DvmrpNeighborMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DvmrpNeighborMinorVersion_Type.__name__=_E
_DvmrpNeighborMinorVersion_Object=MibTableColumn
dvmrpNeighborMinorVersion=_DvmrpNeighborMinorVersion_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,7),_DvmrpNeighborMinorVersion_Type())
dvmrpNeighborMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborMinorVersion.setStatus(_A)
class _DvmrpNeighborCapabilities_Type(Bits):namedValues=NamedValues(*(('leaf',0),('prune',1),('generationID',2),('mtrace',3)))
_DvmrpNeighborCapabilities_Type.__name__='Bits'
_DvmrpNeighborCapabilities_Object=MibTableColumn
dvmrpNeighborCapabilities=_DvmrpNeighborCapabilities_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,8),_DvmrpNeighborCapabilities_Type())
dvmrpNeighborCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborCapabilities.setStatus(_A)
_DvmrpNeighborRcvRoutes_Type=Counter32
_DvmrpNeighborRcvRoutes_Object=MibTableColumn
dvmrpNeighborRcvRoutes=_DvmrpNeighborRcvRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,9),_DvmrpNeighborRcvRoutes_Type())
dvmrpNeighborRcvRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvRoutes.setStatus(_A)
_DvmrpNeighborRcvBadPkts_Type=Counter32
_DvmrpNeighborRcvBadPkts_Object=MibTableColumn
dvmrpNeighborRcvBadPkts=_DvmrpNeighborRcvBadPkts_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,10),_DvmrpNeighborRcvBadPkts_Type())
dvmrpNeighborRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadPkts.setStatus(_A)
_DvmrpNeighborRcvBadRoutes_Type=Counter32
_DvmrpNeighborRcvBadRoutes_Object=MibTableColumn
dvmrpNeighborRcvBadRoutes=_DvmrpNeighborRcvBadRoutes_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,11),_DvmrpNeighborRcvBadRoutes_Type())
dvmrpNeighborRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborRcvBadRoutes.setStatus(_A)
class _DvmrpNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oneway',1),('active',2),('ignoring',3),('down',4)))
_DvmrpNeighborState_Type.__name__=_E
_DvmrpNeighborState_Object=MibTableColumn
dvmrpNeighborState=_DvmrpNeighborState_Object((1,3,6,1,4,1,4413,1,1,10,1,1,3,1,12),_DvmrpNeighborState_Type())
dvmrpNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpNeighborState.setStatus(_A)
_DvmrpRouteTable_Object=MibTable
dvmrpRouteTable=_DvmrpRouteTable_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4))
if mibBuilder.loadTexts:dvmrpRouteTable.setStatus(_A)
_DvmrpRouteEntry_Object=MibTableRow
dvmrpRouteEntry=_DvmrpRouteEntry_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1))
dvmrpRouteEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:dvmrpRouteEntry.setStatus(_A)
_DvmrpRouteSource_Type=IpAddress
_DvmrpRouteSource_Object=MibTableColumn
dvmrpRouteSource=_DvmrpRouteSource_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,1),_DvmrpRouteSource_Type())
dvmrpRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteSource.setStatus(_A)
_DvmrpRouteSourceMask_Type=IpAddress
_DvmrpRouteSourceMask_Object=MibTableColumn
dvmrpRouteSourceMask=_DvmrpRouteSourceMask_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,2),_DvmrpRouteSourceMask_Type())
dvmrpRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteSourceMask.setStatus(_A)
_DvmrpRouteUpstreamNeighbor_Type=IpAddress
_DvmrpRouteUpstreamNeighbor_Object=MibTableColumn
dvmrpRouteUpstreamNeighbor=_DvmrpRouteUpstreamNeighbor_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,3),_DvmrpRouteUpstreamNeighbor_Type())
dvmrpRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteUpstreamNeighbor.setStatus(_A)
_DvmrpRouteIfIndex_Type=InterfaceIndexOrZero
_DvmrpRouteIfIndex_Object=MibTableColumn
dvmrpRouteIfIndex=_DvmrpRouteIfIndex_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,4),_DvmrpRouteIfIndex_Type())
dvmrpRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteIfIndex.setStatus(_A)
class _DvmrpRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_DvmrpRouteMetric_Type.__name__=_E
_DvmrpRouteMetric_Object=MibTableColumn
dvmrpRouteMetric=_DvmrpRouteMetric_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,5),_DvmrpRouteMetric_Type())
dvmrpRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteMetric.setStatus(_A)
_DvmrpRouteExpiryTime_Type=TimeTicks
_DvmrpRouteExpiryTime_Object=MibTableColumn
dvmrpRouteExpiryTime=_DvmrpRouteExpiryTime_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,6),_DvmrpRouteExpiryTime_Type())
dvmrpRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteExpiryTime.setStatus(_A)
_DvmrpRouteUpTime_Type=TimeTicks
_DvmrpRouteUpTime_Object=MibTableColumn
dvmrpRouteUpTime=_DvmrpRouteUpTime_Object((1,3,6,1,4,1,4413,1,1,10,1,1,4,1,7),_DvmrpRouteUpTime_Type())
dvmrpRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteUpTime.setStatus(_A)
_DvmrpRouteNextHopTable_Object=MibTable
dvmrpRouteNextHopTable=_DvmrpRouteNextHopTable_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5))
if mibBuilder.loadTexts:dvmrpRouteNextHopTable.setStatus(_A)
_DvmrpRouteNextHopEntry_Object=MibTableRow
dvmrpRouteNextHopEntry=_DvmrpRouteNextHopEntry_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5,1))
dvmrpRouteNextHopEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:dvmrpRouteNextHopEntry.setStatus(_A)
_DvmrpRouteNextHopSource_Type=IpAddress
_DvmrpRouteNextHopSource_Object=MibTableColumn
dvmrpRouteNextHopSource=_DvmrpRouteNextHopSource_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5,1,1),_DvmrpRouteNextHopSource_Type())
dvmrpRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopSource.setStatus(_A)
_DvmrpRouteNextHopSourceMask_Type=IpAddress
_DvmrpRouteNextHopSourceMask_Object=MibTableColumn
dvmrpRouteNextHopSourceMask=_DvmrpRouteNextHopSourceMask_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5,1,2),_DvmrpRouteNextHopSourceMask_Type())
dvmrpRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopSourceMask.setStatus(_A)
_DvmrpRouteNextHopIfIndex_Type=InterfaceIndex
_DvmrpRouteNextHopIfIndex_Object=MibTableColumn
dvmrpRouteNextHopIfIndex=_DvmrpRouteNextHopIfIndex_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5,1,3),_DvmrpRouteNextHopIfIndex_Type())
dvmrpRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpRouteNextHopIfIndex.setStatus(_A)
class _DvmrpRouteNextHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leaf',1),('branch',2)))
_DvmrpRouteNextHopType_Type.__name__=_E
_DvmrpRouteNextHopType_Object=MibTableColumn
dvmrpRouteNextHopType=_DvmrpRouteNextHopType_Object((1,3,6,1,4,1,4413,1,1,10,1,1,5,1,4),_DvmrpRouteNextHopType_Type())
dvmrpRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpRouteNextHopType.setStatus(_A)
_DvmrpPruneTable_Object=MibTable
dvmrpPruneTable=_DvmrpPruneTable_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6))
if mibBuilder.loadTexts:dvmrpPruneTable.setStatus(_A)
_DvmrpPruneEntry_Object=MibTableRow
dvmrpPruneEntry=_DvmrpPruneEntry_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6,1))
dvmrpPruneEntry.setIndexNames((0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:dvmrpPruneEntry.setStatus(_A)
_DvmrpPruneGroup_Type=IpAddress
_DvmrpPruneGroup_Object=MibTableColumn
dvmrpPruneGroup=_DvmrpPruneGroup_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6,1,1),_DvmrpPruneGroup_Type())
dvmrpPruneGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpPruneGroup.setStatus(_A)
_DvmrpPruneSource_Type=IpAddress
_DvmrpPruneSource_Object=MibTableColumn
dvmrpPruneSource=_DvmrpPruneSource_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6,1,2),_DvmrpPruneSource_Type())
dvmrpPruneSource.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpPruneSource.setStatus(_A)
_DvmrpPruneSourceMask_Type=IpAddress
_DvmrpPruneSourceMask_Object=MibTableColumn
dvmrpPruneSourceMask=_DvmrpPruneSourceMask_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6,1,3),_DvmrpPruneSourceMask_Type())
dvmrpPruneSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:dvmrpPruneSourceMask.setStatus(_A)
_DvmrpPruneExpiryTime_Type=TimeTicks
_DvmrpPruneExpiryTime_Object=MibTableColumn
dvmrpPruneExpiryTime=_DvmrpPruneExpiryTime_Object((1,3,6,1,4,1,4413,1,1,10,1,1,6,1,4),_DvmrpPruneExpiryTime_Type())
dvmrpPruneExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dvmrpPruneExpiryTime.setStatus(_A)
_DvmrpTraps_ObjectIdentity=ObjectIdentity
dvmrpTraps=_DvmrpTraps_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,1,1,7))
_DvmrpMIBConformance_ObjectIdentity=ObjectIdentity
dvmrpMIBConformance=_DvmrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,2))
_DvmrpMIBCompliances_ObjectIdentity=ObjectIdentity
dvmrpMIBCompliances=_DvmrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,2,1))
_DvmrpMIBGroups_ObjectIdentity=ObjectIdentity
dvmrpMIBGroups=_DvmrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,4413,1,1,10,2,2))
dvmrpGeneralGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,2))
dvmrpGeneralGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:dvmrpGeneralGroup.setStatus(_A)
dvmrpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,3))
dvmrpInterfaceGroup.setObjects(*((_B,_G),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:dvmrpInterfaceGroup.setStatus(_A)
dvmrpNeighborGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,4))
dvmrpNeighborGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_H),(_B,_i),(_B,_j),(_B,_k),(_B,_I)))
if mibBuilder.loadTexts:dvmrpNeighborGroup.setStatus(_A)
dvmrpRoutingGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,5))
dvmrpRoutingGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:dvmrpRoutingGroup.setStatus(_A)
dvmrpSecurityGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,6))
dvmrpSecurityGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:dvmrpSecurityGroup.setStatus(_A)
dvmrpTreeGroup=ObjectGroup((1,3,6,1,4,1,4413,1,1,10,2,2,7))
dvmrpTreeGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:dvmrpTreeGroup.setStatus(_A)
dvmrpNeighborLoss=NotificationType((1,3,6,1,4,1,4413,1,1,10,1,1,7,1))
dvmrpNeighborLoss.setObjects(*((_B,_G),(_B,_I)))
if mibBuilder.loadTexts:dvmrpNeighborLoss.setStatus(_A)
dvmrpNeighborNotPruning=NotificationType((1,3,6,1,4,1,4413,1,1,10,1,1,7,2))
dvmrpNeighborNotPruning.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:dvmrpNeighborNotPruning.setStatus(_A)
dvmrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,4413,1,1,10,2,2,8))
dvmrpNotificationGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:dvmrpNotificationGroup.setStatus(_A)
dvmrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4413,1,1,10,2,1,1))
dvmrpMIBCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:dvmrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dvmrpStdMIB':dvmrpStdMIB,'dvmrpMIBObjects':dvmrpMIBObjects,'dvmrp':dvmrp,'dvmrpScalar':dvmrpScalar,_U:dvmrpVersionString,_V:dvmrpGenerationId,_W:dvmrpNumRoutes,_X:dvmrpReachableRoutes,'dvmrpInterfaceTable':dvmrpInterfaceTable,'dvmrpInterfaceEntry':dvmrpInterfaceEntry,_J:dvmrpInterfaceIfIndex,_G:dvmrpInterfaceLocalAddress,_Y:dvmrpInterfaceMetric,_Z:dvmrpInterfaceStatus,_a:dvmrpInterfaceRcvBadPkts,_b:dvmrpInterfaceRcvBadRoutes,_c:dvmrpInterfaceSentRoutes,_r:dvmrpInterfaceInterfaceKey,_s:dvmrpInterfaceInterfaceKeyVersion,'dvmrpNeighborTable':dvmrpNeighborTable,'dvmrpNeighborEntry':dvmrpNeighborEntry,_K:dvmrpNeighborIfIndex,_L:dvmrpNeighborAddress,_d:dvmrpNeighborUpTime,_e:dvmrpNeighborExpiryTime,_f:dvmrpNeighborGenerationId,_g:dvmrpNeighborMajorVersion,_h:dvmrpNeighborMinorVersion,_H:dvmrpNeighborCapabilities,_i:dvmrpNeighborRcvRoutes,_j:dvmrpNeighborRcvBadPkts,_k:dvmrpNeighborRcvBadRoutes,_I:dvmrpNeighborState,'dvmrpRouteTable':dvmrpRouteTable,'dvmrpRouteEntry':dvmrpRouteEntry,_M:dvmrpRouteSource,_N:dvmrpRouteSourceMask,_l:dvmrpRouteUpstreamNeighbor,_m:dvmrpRouteIfIndex,_n:dvmrpRouteMetric,_o:dvmrpRouteExpiryTime,_p:dvmrpRouteUpTime,'dvmrpRouteNextHopTable':dvmrpRouteNextHopTable,'dvmrpRouteNextHopEntry':dvmrpRouteNextHopEntry,_O:dvmrpRouteNextHopSource,_P:dvmrpRouteNextHopSourceMask,_Q:dvmrpRouteNextHopIfIndex,_q:dvmrpRouteNextHopType,'dvmrpPruneTable':dvmrpPruneTable,'dvmrpPruneEntry':dvmrpPruneEntry,_R:dvmrpPruneGroup,_S:dvmrpPruneSource,_T:dvmrpPruneSourceMask,_t:dvmrpPruneExpiryTime,'dvmrpTraps':dvmrpTraps,_u:dvmrpNeighborLoss,_v:dvmrpNeighborNotPruning,'dvmrpMIBConformance':dvmrpMIBConformance,'dvmrpMIBCompliances':dvmrpMIBCompliances,'dvmrpMIBCompliance':dvmrpMIBCompliance,'dvmrpMIBGroups':dvmrpMIBGroups,_w:dvmrpGeneralGroup,_x:dvmrpInterfaceGroup,_y:dvmrpNeighborGroup,_z:dvmrpRoutingGroup,_A1:dvmrpSecurityGroup,_A0:dvmrpTreeGroup,'dvmrpNotificationGroup':dvmrpNotificationGroup})