_A1='junidDvmrpSecurityGroup'
_A0='junidDvmrpTreeGroup'
_z='junidDvmrpRoutingGroup'
_y='junidDvmrpNeighborGroup'
_x='junidDvmrpInterfaceGroup'
_w='junidDvmrpGeneralGroup'
_v='junidDvmrpNeighborNotPruning'
_u='junidDvmrpNeighborLoss'
_t='junidDvmrpPruneExpiryTime'
_s='junidDvmrpInterfaceInterfaceKeyVersion'
_r='junidDvmrpInterfaceInterfaceKey'
_q='junidDvmrpRouteNextHopType'
_p='junidDvmrpRouteUpTime'
_o='junidDvmrpRouteExpiryTime'
_n='junidDvmrpRouteMetric'
_m='junidDvmrpRouteIfIndex'
_l='junidDvmrpRouteUpstreamNeighbor'
_k='junidDvmrpNeighborRcvBadRoutes'
_j='junidDvmrpNeighborRcvBadPkts'
_i='junidDvmrpNeighborRcvRoutes'
_h='junidDvmrpNeighborMinorVersion'
_g='junidDvmrpNeighborMajorVersion'
_f='junidDvmrpNeighborGenerationId'
_e='junidDvmrpNeighborExpiryTime'
_d='junidDvmrpNeighborUpTime'
_c='junidDvmrpInterfaceSentRoutes'
_b='junidDvmrpInterfaceRcvBadRoutes'
_a='junidDvmrpInterfaceRcvBadPkts'
_Z='junidDvmrpInterfaceStatus'
_Y='junidDvmrpInterfaceMetric'
_X='junidDvmrpReachableRoutes'
_W='junidDvmrpNumRoutes'
_V='junidDvmrpGenerationId'
_U='junidDvmrpVersionString'
_T='junidDvmrpPruneSourceMask'
_S='junidDvmrpPruneSource'
_R='junidDvmrpPruneGroup'
_Q='junidDvmrpRouteNextHopIfIndex'
_P='junidDvmrpRouteNextHopSourceMask'
_O='junidDvmrpRouteNextHopSource'
_N='junidDvmrpRouteSourceMask'
_M='junidDvmrpRouteSource'
_L='junidDvmrpNeighborAddress'
_K='junidDvmrpNeighborIfIndex'
_J='junidDvmrpInterfaceIfIndex'
_I='junidDvmrpNeighborState'
_H='junidDvmrpNeighborCapabilities'
_G='junidDvmrpInterfaceLocalAddress'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='DVMRP-STD-MIB-JUNI'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniDvmrpExperiment,=mibBuilder.importSymbols('Juniper-Experiment','juniDvmrpExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
junidDvmrpStdMIB=ModuleIdentity((1,3,6,1,4,1,4874,3,2,1,1))
if mibBuilder.loadTexts:junidDvmrpStdMIB.setRevisions(('1999-10-19 12:00',))
_JunidDvmrpMIBObjects_ObjectIdentity=ObjectIdentity
junidDvmrpMIBObjects=_JunidDvmrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,1))
_JunidDvmrp_ObjectIdentity=ObjectIdentity
junidDvmrp=_JunidDvmrp_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,1,1))
_JunidDvmrpTraps_ObjectIdentity=ObjectIdentity
junidDvmrpTraps=_JunidDvmrpTraps_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,1,1,0))
_JunidDvmrpScalar_ObjectIdentity=ObjectIdentity
junidDvmrpScalar=_JunidDvmrpScalar_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,1,1,1))
_JunidDvmrpVersionString_Type=DisplayString
_JunidDvmrpVersionString_Object=MibScalar
junidDvmrpVersionString=_JunidDvmrpVersionString_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,1,1),_JunidDvmrpVersionString_Type())
junidDvmrpVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpVersionString.setStatus(_A)
_JunidDvmrpGenerationId_Type=Integer32
_JunidDvmrpGenerationId_Object=MibScalar
junidDvmrpGenerationId=_JunidDvmrpGenerationId_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,1,2),_JunidDvmrpGenerationId_Type())
junidDvmrpGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpGenerationId.setStatus(_A)
_JunidDvmrpNumRoutes_Type=Gauge32
_JunidDvmrpNumRoutes_Object=MibScalar
junidDvmrpNumRoutes=_JunidDvmrpNumRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,1,3),_JunidDvmrpNumRoutes_Type())
junidDvmrpNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNumRoutes.setStatus(_A)
_JunidDvmrpReachableRoutes_Type=Gauge32
_JunidDvmrpReachableRoutes_Object=MibScalar
junidDvmrpReachableRoutes=_JunidDvmrpReachableRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,1,4),_JunidDvmrpReachableRoutes_Type())
junidDvmrpReachableRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpReachableRoutes.setStatus(_A)
_JunidDvmrpInterfaceTable_Object=MibTable
junidDvmrpInterfaceTable=_JunidDvmrpInterfaceTable_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2))
if mibBuilder.loadTexts:junidDvmrpInterfaceTable.setStatus(_A)
_JunidDvmrpInterfaceEntry_Object=MibTableRow
junidDvmrpInterfaceEntry=_JunidDvmrpInterfaceEntry_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1))
junidDvmrpInterfaceEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:junidDvmrpInterfaceEntry.setStatus(_A)
_JunidDvmrpInterfaceIfIndex_Type=InterfaceIndex
_JunidDvmrpInterfaceIfIndex_Object=MibTableColumn
junidDvmrpInterfaceIfIndex=_JunidDvmrpInterfaceIfIndex_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,1),_JunidDvmrpInterfaceIfIndex_Type())
junidDvmrpInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpInterfaceIfIndex.setStatus(_A)
_JunidDvmrpInterfaceLocalAddress_Type=IpAddress
_JunidDvmrpInterfaceLocalAddress_Object=MibTableColumn
junidDvmrpInterfaceLocalAddress=_JunidDvmrpInterfaceLocalAddress_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,2),_JunidDvmrpInterfaceLocalAddress_Type())
junidDvmrpInterfaceLocalAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:junidDvmrpInterfaceLocalAddress.setStatus(_A)
class _JunidDvmrpInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_JunidDvmrpInterfaceMetric_Type.__name__=_E
_JunidDvmrpInterfaceMetric_Object=MibTableColumn
junidDvmrpInterfaceMetric=_JunidDvmrpInterfaceMetric_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,3),_JunidDvmrpInterfaceMetric_Type())
junidDvmrpInterfaceMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:junidDvmrpInterfaceMetric.setStatus(_A)
_JunidDvmrpInterfaceStatus_Type=RowStatus
_JunidDvmrpInterfaceStatus_Object=MibTableColumn
junidDvmrpInterfaceStatus=_JunidDvmrpInterfaceStatus_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,4),_JunidDvmrpInterfaceStatus_Type())
junidDvmrpInterfaceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:junidDvmrpInterfaceStatus.setStatus(_A)
_JunidDvmrpInterfaceRcvBadPkts_Type=Counter32
_JunidDvmrpInterfaceRcvBadPkts_Object=MibTableColumn
junidDvmrpInterfaceRcvBadPkts=_JunidDvmrpInterfaceRcvBadPkts_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,5),_JunidDvmrpInterfaceRcvBadPkts_Type())
junidDvmrpInterfaceRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpInterfaceRcvBadPkts.setStatus(_A)
_JunidDvmrpInterfaceRcvBadRoutes_Type=Counter32
_JunidDvmrpInterfaceRcvBadRoutes_Object=MibTableColumn
junidDvmrpInterfaceRcvBadRoutes=_JunidDvmrpInterfaceRcvBadRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,6),_JunidDvmrpInterfaceRcvBadRoutes_Type())
junidDvmrpInterfaceRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpInterfaceRcvBadRoutes.setStatus(_A)
_JunidDvmrpInterfaceSentRoutes_Type=Counter32
_JunidDvmrpInterfaceSentRoutes_Object=MibTableColumn
junidDvmrpInterfaceSentRoutes=_JunidDvmrpInterfaceSentRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,7),_JunidDvmrpInterfaceSentRoutes_Type())
junidDvmrpInterfaceSentRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpInterfaceSentRoutes.setStatus(_A)
_JunidDvmrpInterfaceInterfaceKey_Type=SnmpAdminString
_JunidDvmrpInterfaceInterfaceKey_Object=MibTableColumn
junidDvmrpInterfaceInterfaceKey=_JunidDvmrpInterfaceInterfaceKey_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,8),_JunidDvmrpInterfaceInterfaceKey_Type())
junidDvmrpInterfaceInterfaceKey.setMaxAccess(_F)
if mibBuilder.loadTexts:junidDvmrpInterfaceInterfaceKey.setStatus(_A)
_JunidDvmrpInterfaceInterfaceKeyVersion_Type=Integer32
_JunidDvmrpInterfaceInterfaceKeyVersion_Object=MibTableColumn
junidDvmrpInterfaceInterfaceKeyVersion=_JunidDvmrpInterfaceInterfaceKeyVersion_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,2,1,9),_JunidDvmrpInterfaceInterfaceKeyVersion_Type())
junidDvmrpInterfaceInterfaceKeyVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:junidDvmrpInterfaceInterfaceKeyVersion.setStatus(_A)
_JunidDvmrpNeighborTable_Object=MibTable
junidDvmrpNeighborTable=_JunidDvmrpNeighborTable_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3))
if mibBuilder.loadTexts:junidDvmrpNeighborTable.setStatus(_A)
_JunidDvmrpNeighborEntry_Object=MibTableRow
junidDvmrpNeighborEntry=_JunidDvmrpNeighborEntry_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1))
junidDvmrpNeighborEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:junidDvmrpNeighborEntry.setStatus(_A)
_JunidDvmrpNeighborIfIndex_Type=InterfaceIndex
_JunidDvmrpNeighborIfIndex_Object=MibTableColumn
junidDvmrpNeighborIfIndex=_JunidDvmrpNeighborIfIndex_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,1),_JunidDvmrpNeighborIfIndex_Type())
junidDvmrpNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpNeighborIfIndex.setStatus(_A)
_JunidDvmrpNeighborAddress_Type=IpAddress
_JunidDvmrpNeighborAddress_Object=MibTableColumn
junidDvmrpNeighborAddress=_JunidDvmrpNeighborAddress_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,2),_JunidDvmrpNeighborAddress_Type())
junidDvmrpNeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpNeighborAddress.setStatus(_A)
_JunidDvmrpNeighborUpTime_Type=TimeTicks
_JunidDvmrpNeighborUpTime_Object=MibTableColumn
junidDvmrpNeighborUpTime=_JunidDvmrpNeighborUpTime_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,3),_JunidDvmrpNeighborUpTime_Type())
junidDvmrpNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborUpTime.setStatus(_A)
_JunidDvmrpNeighborExpiryTime_Type=TimeTicks
_JunidDvmrpNeighborExpiryTime_Object=MibTableColumn
junidDvmrpNeighborExpiryTime=_JunidDvmrpNeighborExpiryTime_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,4),_JunidDvmrpNeighborExpiryTime_Type())
junidDvmrpNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborExpiryTime.setStatus(_A)
_JunidDvmrpNeighborGenerationId_Type=Integer32
_JunidDvmrpNeighborGenerationId_Object=MibTableColumn
junidDvmrpNeighborGenerationId=_JunidDvmrpNeighborGenerationId_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,5),_JunidDvmrpNeighborGenerationId_Type())
junidDvmrpNeighborGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborGenerationId.setStatus(_A)
class _JunidDvmrpNeighborMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JunidDvmrpNeighborMajorVersion_Type.__name__=_E
_JunidDvmrpNeighborMajorVersion_Object=MibTableColumn
junidDvmrpNeighborMajorVersion=_JunidDvmrpNeighborMajorVersion_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,6),_JunidDvmrpNeighborMajorVersion_Type())
junidDvmrpNeighborMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborMajorVersion.setStatus(_A)
class _JunidDvmrpNeighborMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JunidDvmrpNeighborMinorVersion_Type.__name__=_E
_JunidDvmrpNeighborMinorVersion_Object=MibTableColumn
junidDvmrpNeighborMinorVersion=_JunidDvmrpNeighborMinorVersion_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,7),_JunidDvmrpNeighborMinorVersion_Type())
junidDvmrpNeighborMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborMinorVersion.setStatus(_A)
class _JunidDvmrpNeighborCapabilities_Type(Bits):namedValues=NamedValues(*(('leaf',0),('prune',1),('generationID',2),('mtrace',3)))
_JunidDvmrpNeighborCapabilities_Type.__name__='Bits'
_JunidDvmrpNeighborCapabilities_Object=MibTableColumn
junidDvmrpNeighborCapabilities=_JunidDvmrpNeighborCapabilities_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,8),_JunidDvmrpNeighborCapabilities_Type())
junidDvmrpNeighborCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborCapabilities.setStatus(_A)
_JunidDvmrpNeighborRcvRoutes_Type=Counter32
_JunidDvmrpNeighborRcvRoutes_Object=MibTableColumn
junidDvmrpNeighborRcvRoutes=_JunidDvmrpNeighborRcvRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,9),_JunidDvmrpNeighborRcvRoutes_Type())
junidDvmrpNeighborRcvRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborRcvRoutes.setStatus(_A)
_JunidDvmrpNeighborRcvBadPkts_Type=Counter32
_JunidDvmrpNeighborRcvBadPkts_Object=MibTableColumn
junidDvmrpNeighborRcvBadPkts=_JunidDvmrpNeighborRcvBadPkts_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,10),_JunidDvmrpNeighborRcvBadPkts_Type())
junidDvmrpNeighborRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborRcvBadPkts.setStatus(_A)
_JunidDvmrpNeighborRcvBadRoutes_Type=Counter32
_JunidDvmrpNeighborRcvBadRoutes_Object=MibTableColumn
junidDvmrpNeighborRcvBadRoutes=_JunidDvmrpNeighborRcvBadRoutes_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,11),_JunidDvmrpNeighborRcvBadRoutes_Type())
junidDvmrpNeighborRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborRcvBadRoutes.setStatus(_A)
class _JunidDvmrpNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oneway',1),('active',2),('ignoring',3),('down',4)))
_JunidDvmrpNeighborState_Type.__name__=_E
_JunidDvmrpNeighborState_Object=MibTableColumn
junidDvmrpNeighborState=_JunidDvmrpNeighborState_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,3,1,12),_JunidDvmrpNeighborState_Type())
junidDvmrpNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpNeighborState.setStatus(_A)
_JunidDvmrpRouteTable_Object=MibTable
junidDvmrpRouteTable=_JunidDvmrpRouteTable_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4))
if mibBuilder.loadTexts:junidDvmrpRouteTable.setStatus(_A)
_JunidDvmrpRouteEntry_Object=MibTableRow
junidDvmrpRouteEntry=_JunidDvmrpRouteEntry_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1))
junidDvmrpRouteEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:junidDvmrpRouteEntry.setStatus(_A)
_JunidDvmrpRouteSource_Type=IpAddress
_JunidDvmrpRouteSource_Object=MibTableColumn
junidDvmrpRouteSource=_JunidDvmrpRouteSource_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,1),_JunidDvmrpRouteSource_Type())
junidDvmrpRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpRouteSource.setStatus(_A)
_JunidDvmrpRouteSourceMask_Type=IpAddress
_JunidDvmrpRouteSourceMask_Object=MibTableColumn
junidDvmrpRouteSourceMask=_JunidDvmrpRouteSourceMask_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,2),_JunidDvmrpRouteSourceMask_Type())
junidDvmrpRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpRouteSourceMask.setStatus(_A)
_JunidDvmrpRouteUpstreamNeighbor_Type=IpAddress
_JunidDvmrpRouteUpstreamNeighbor_Object=MibTableColumn
junidDvmrpRouteUpstreamNeighbor=_JunidDvmrpRouteUpstreamNeighbor_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,3),_JunidDvmrpRouteUpstreamNeighbor_Type())
junidDvmrpRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteUpstreamNeighbor.setStatus(_A)
_JunidDvmrpRouteIfIndex_Type=InterfaceIndexOrZero
_JunidDvmrpRouteIfIndex_Object=MibTableColumn
junidDvmrpRouteIfIndex=_JunidDvmrpRouteIfIndex_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,4),_JunidDvmrpRouteIfIndex_Type())
junidDvmrpRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteIfIndex.setStatus(_A)
class _JunidDvmrpRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_JunidDvmrpRouteMetric_Type.__name__=_E
_JunidDvmrpRouteMetric_Object=MibTableColumn
junidDvmrpRouteMetric=_JunidDvmrpRouteMetric_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,5),_JunidDvmrpRouteMetric_Type())
junidDvmrpRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteMetric.setStatus(_A)
_JunidDvmrpRouteExpiryTime_Type=TimeTicks
_JunidDvmrpRouteExpiryTime_Object=MibTableColumn
junidDvmrpRouteExpiryTime=_JunidDvmrpRouteExpiryTime_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,6),_JunidDvmrpRouteExpiryTime_Type())
junidDvmrpRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteExpiryTime.setStatus(_A)
_JunidDvmrpRouteUpTime_Type=TimeTicks
_JunidDvmrpRouteUpTime_Object=MibTableColumn
junidDvmrpRouteUpTime=_JunidDvmrpRouteUpTime_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,4,1,7),_JunidDvmrpRouteUpTime_Type())
junidDvmrpRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteUpTime.setStatus(_A)
_JunidDvmrpRouteNextHopTable_Object=MibTable
junidDvmrpRouteNextHopTable=_JunidDvmrpRouteNextHopTable_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5))
if mibBuilder.loadTexts:junidDvmrpRouteNextHopTable.setStatus(_A)
_JunidDvmrpRouteNextHopEntry_Object=MibTableRow
junidDvmrpRouteNextHopEntry=_JunidDvmrpRouteNextHopEntry_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5,1))
junidDvmrpRouteNextHopEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:junidDvmrpRouteNextHopEntry.setStatus(_A)
_JunidDvmrpRouteNextHopSource_Type=IpAddress
_JunidDvmrpRouteNextHopSource_Object=MibTableColumn
junidDvmrpRouteNextHopSource=_JunidDvmrpRouteNextHopSource_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5,1,1),_JunidDvmrpRouteNextHopSource_Type())
junidDvmrpRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpRouteNextHopSource.setStatus(_A)
_JunidDvmrpRouteNextHopSourceMask_Type=IpAddress
_JunidDvmrpRouteNextHopSourceMask_Object=MibTableColumn
junidDvmrpRouteNextHopSourceMask=_JunidDvmrpRouteNextHopSourceMask_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5,1,2),_JunidDvmrpRouteNextHopSourceMask_Type())
junidDvmrpRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpRouteNextHopSourceMask.setStatus(_A)
_JunidDvmrpRouteNextHopIfIndex_Type=InterfaceIndex
_JunidDvmrpRouteNextHopIfIndex_Object=MibTableColumn
junidDvmrpRouteNextHopIfIndex=_JunidDvmrpRouteNextHopIfIndex_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5,1,3),_JunidDvmrpRouteNextHopIfIndex_Type())
junidDvmrpRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpRouteNextHopIfIndex.setStatus(_A)
class _JunidDvmrpRouteNextHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leaf',1),('branch',2)))
_JunidDvmrpRouteNextHopType_Type.__name__=_E
_JunidDvmrpRouteNextHopType_Object=MibTableColumn
junidDvmrpRouteNextHopType=_JunidDvmrpRouteNextHopType_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,5,1,4),_JunidDvmrpRouteNextHopType_Type())
junidDvmrpRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpRouteNextHopType.setStatus(_A)
_JunidDvmrpPruneTable_Object=MibTable
junidDvmrpPruneTable=_JunidDvmrpPruneTable_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6))
if mibBuilder.loadTexts:junidDvmrpPruneTable.setStatus(_A)
_JunidDvmrpPruneEntry_Object=MibTableRow
junidDvmrpPruneEntry=_JunidDvmrpPruneEntry_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6,1))
junidDvmrpPruneEntry.setIndexNames((0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:junidDvmrpPruneEntry.setStatus(_A)
_JunidDvmrpPruneGroup_Type=IpAddress
_JunidDvmrpPruneGroup_Object=MibTableColumn
junidDvmrpPruneGroup=_JunidDvmrpPruneGroup_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6,1,1),_JunidDvmrpPruneGroup_Type())
junidDvmrpPruneGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpPruneGroup.setStatus(_A)
_JunidDvmrpPruneSource_Type=IpAddress
_JunidDvmrpPruneSource_Object=MibTableColumn
junidDvmrpPruneSource=_JunidDvmrpPruneSource_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6,1,2),_JunidDvmrpPruneSource_Type())
junidDvmrpPruneSource.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpPruneSource.setStatus(_A)
_JunidDvmrpPruneSourceMask_Type=IpAddress
_JunidDvmrpPruneSourceMask_Object=MibTableColumn
junidDvmrpPruneSourceMask=_JunidDvmrpPruneSourceMask_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6,1,3),_JunidDvmrpPruneSourceMask_Type())
junidDvmrpPruneSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:junidDvmrpPruneSourceMask.setStatus(_A)
_JunidDvmrpPruneExpiryTime_Type=TimeTicks
_JunidDvmrpPruneExpiryTime_Object=MibTableColumn
junidDvmrpPruneExpiryTime=_JunidDvmrpPruneExpiryTime_Object((1,3,6,1,4,1,4874,3,2,1,1,1,1,6,1,4),_JunidDvmrpPruneExpiryTime_Type())
junidDvmrpPruneExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidDvmrpPruneExpiryTime.setStatus(_A)
_JunidDvmrpMIBConformance_ObjectIdentity=ObjectIdentity
junidDvmrpMIBConformance=_JunidDvmrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,2))
_JunidDvmrpMIBCompliances_ObjectIdentity=ObjectIdentity
junidDvmrpMIBCompliances=_JunidDvmrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,2,1))
_JunidDvmrpMIBGroups_ObjectIdentity=ObjectIdentity
junidDvmrpMIBGroups=_JunidDvmrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,3,2,1,1,2,2))
junidDvmrpGeneralGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,2))
junidDvmrpGeneralGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:junidDvmrpGeneralGroup.setStatus(_A)
junidDvmrpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,3))
junidDvmrpInterfaceGroup.setObjects(*((_B,_G),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:junidDvmrpInterfaceGroup.setStatus(_A)
junidDvmrpNeighborGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,4))
junidDvmrpNeighborGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_H),(_B,_i),(_B,_j),(_B,_k),(_B,_I)))
if mibBuilder.loadTexts:junidDvmrpNeighborGroup.setStatus(_A)
junidDvmrpRoutingGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,5))
junidDvmrpRoutingGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:junidDvmrpRoutingGroup.setStatus(_A)
junidDvmrpSecurityGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,6))
junidDvmrpSecurityGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:junidDvmrpSecurityGroup.setStatus(_A)
junidDvmrpTreeGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,7))
junidDvmrpTreeGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:junidDvmrpTreeGroup.setStatus(_A)
junidDvmrpNeighborLoss=NotificationType((1,3,6,1,4,1,4874,3,2,1,1,1,1,0,1))
junidDvmrpNeighborLoss.setObjects(*((_B,_G),(_B,_I)))
if mibBuilder.loadTexts:junidDvmrpNeighborLoss.setStatus(_A)
junidDvmrpNeighborNotPruning=NotificationType((1,3,6,1,4,1,4874,3,2,1,1,1,1,0,2))
junidDvmrpNeighborNotPruning.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:junidDvmrpNeighborNotPruning.setStatus(_A)
junidDvmrpNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,3,2,1,1,2,2,8))
junidDvmrpNotificationGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:junidDvmrpNotificationGroup.setStatus(_A)
junidDvmrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4874,3,2,1,1,2,1,1))
junidDvmrpMIBCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:junidDvmrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'junidDvmrpStdMIB':junidDvmrpStdMIB,'junidDvmrpMIBObjects':junidDvmrpMIBObjects,'junidDvmrp':junidDvmrp,'junidDvmrpTraps':junidDvmrpTraps,_u:junidDvmrpNeighborLoss,_v:junidDvmrpNeighborNotPruning,'junidDvmrpScalar':junidDvmrpScalar,_U:junidDvmrpVersionString,_V:junidDvmrpGenerationId,_W:junidDvmrpNumRoutes,_X:junidDvmrpReachableRoutes,'junidDvmrpInterfaceTable':junidDvmrpInterfaceTable,'junidDvmrpInterfaceEntry':junidDvmrpInterfaceEntry,_J:junidDvmrpInterfaceIfIndex,_G:junidDvmrpInterfaceLocalAddress,_Y:junidDvmrpInterfaceMetric,_Z:junidDvmrpInterfaceStatus,_a:junidDvmrpInterfaceRcvBadPkts,_b:junidDvmrpInterfaceRcvBadRoutes,_c:junidDvmrpInterfaceSentRoutes,_r:junidDvmrpInterfaceInterfaceKey,_s:junidDvmrpInterfaceInterfaceKeyVersion,'junidDvmrpNeighborTable':junidDvmrpNeighborTable,'junidDvmrpNeighborEntry':junidDvmrpNeighborEntry,_K:junidDvmrpNeighborIfIndex,_L:junidDvmrpNeighborAddress,_d:junidDvmrpNeighborUpTime,_e:junidDvmrpNeighborExpiryTime,_f:junidDvmrpNeighborGenerationId,_g:junidDvmrpNeighborMajorVersion,_h:junidDvmrpNeighborMinorVersion,_H:junidDvmrpNeighborCapabilities,_i:junidDvmrpNeighborRcvRoutes,_j:junidDvmrpNeighborRcvBadPkts,_k:junidDvmrpNeighborRcvBadRoutes,_I:junidDvmrpNeighborState,'junidDvmrpRouteTable':junidDvmrpRouteTable,'junidDvmrpRouteEntry':junidDvmrpRouteEntry,_M:junidDvmrpRouteSource,_N:junidDvmrpRouteSourceMask,_l:junidDvmrpRouteUpstreamNeighbor,_m:junidDvmrpRouteIfIndex,_n:junidDvmrpRouteMetric,_o:junidDvmrpRouteExpiryTime,_p:junidDvmrpRouteUpTime,'junidDvmrpRouteNextHopTable':junidDvmrpRouteNextHopTable,'junidDvmrpRouteNextHopEntry':junidDvmrpRouteNextHopEntry,_O:junidDvmrpRouteNextHopSource,_P:junidDvmrpRouteNextHopSourceMask,_Q:junidDvmrpRouteNextHopIfIndex,_q:junidDvmrpRouteNextHopType,'junidDvmrpPruneTable':junidDvmrpPruneTable,'junidDvmrpPruneEntry':junidDvmrpPruneEntry,_R:junidDvmrpPruneGroup,_S:junidDvmrpPruneSource,_T:junidDvmrpPruneSourceMask,_t:junidDvmrpPruneExpiryTime,'junidDvmrpMIBConformance':junidDvmrpMIBConformance,'junidDvmrpMIBCompliances':junidDvmrpMIBCompliances,'junidDvmrpMIBCompliance':junidDvmrpMIBCompliance,'junidDvmrpMIBGroups':junidDvmrpMIBGroups,_w:junidDvmrpGeneralGroup,_x:junidDvmrpInterfaceGroup,_y:junidDvmrpNeighborGroup,_z:junidDvmrpRoutingGroup,_A1:junidDvmrpSecurityGroup,_A0:junidDvmrpTreeGroup,'junidDvmrpNotificationGroup':junidDvmrpNotificationGroup})