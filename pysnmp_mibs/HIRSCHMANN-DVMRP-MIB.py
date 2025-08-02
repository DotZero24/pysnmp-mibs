_A3='hmDVMRPSecurityGroup'
_A2='hmDVMRPTreeGroup'
_A1='hmDVMRPRoutingGroup'
_A0='hmDVMRPNeighborGroup'
_z='hmDVMRPInterfaceGroup'
_y='hmDVMRPGeneralGroup'
_x='hmDVMRPNeighborNotPruning'
_w='hmDVMRPNeighborLoss'
_v='hmDVMRPPruneExpiryTime'
_u='hmDVMRPInterfaceInterfaceKeyVersion'
_t='hmDVMRPInterfaceInterfaceKey'
_s='hmDVMRPRouteNextHopType'
_r='hmDVMRPRouteUpTime'
_q='hmDVMRPRouteExpiryTime'
_p='hmDVMRPRouteMetric'
_o='hmDVMRPRouteIfIndex'
_n='hmDVMRPRouteUpstreamNeighbor'
_m='hmDVMRPNeighborRcvBadRoutes'
_l='hmDVMRPNeighborRcvBadPkts'
_k='hmDVMRPNeighborRcvRoutes'
_j='hmDVMRPNeighborMinorVersion'
_i='hmDVMRPNeighborMajorVersion'
_h='hmDVMRPNeighborGenerationId'
_g='hmDVMRPNeighborExpiryTime'
_f='hmDVMRPNeighborUpTime'
_e='hmDVMRPInterfaceGenerationId'
_d='hmDVMRPInterfaceSentRoutes'
_c='hmDVMRPInterfaceRcvBadRoutes'
_b='hmDVMRPInterfaceRcvBadPkts'
_a='hmDVMRPInterfaceStatus'
_Z='hmDVMRPInterfaceMetric'
_Y='hmDVMRPReachableRoutes'
_X='hmDVMRPNumRoutes'
_W='hmDVMRPGenerationId'
_V='hmDVMRPVersionString'
_U='hmDVMRPPruneSourceMask'
_T='hmDVMRPPruneSource'
_S='hmDVMRPPruneGroup'
_R='hmDVMRPRouteNextHopIfIndex'
_Q='hmDVMRPRouteNextHopSourceMask'
_P='hmDVMRPRouteNextHopSource'
_O='hmDVMRPRouteSourceMask'
_N='hmDVMRPRouteSource'
_M='hmDVMRPNeighborAddress'
_L='hmDVMRPNeighborIfIndex'
_K='hmDVMRPInterfaceIfIndex'
_J='read-write'
_I='hmDVMRPNeighborState'
_H='hmDVMRPNeighborCapabilities'
_G='hmDVMRPInterfaceLocalAddress'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='HIRSCHMANN-DVMRP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmPlatform4Multicast,=mibBuilder.importSymbols('HIRSCHMANN-MULTICAST-MIB','hmPlatform4Multicast')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hmDVMRPMIB=ModuleIdentity((1,3,6,1,4,1,248,15,4,100))
if mibBuilder.loadTexts:hmDVMRPMIB.setRevisions(('2010-04-12 12:00',))
_HmDVMRPMIBObjects_ObjectIdentity=ObjectIdentity
hmDVMRPMIBObjects=_HmDVMRPMIBObjects_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,1))
_HmDVMRP_ObjectIdentity=ObjectIdentity
hmDVMRP=_HmDVMRP_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,1,1))
_HmDVMRPScalar_ObjectIdentity=ObjectIdentity
hmDVMRPScalar=_HmDVMRPScalar_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,1,1,1))
_HmDVMRPVersionString_Type=DisplayString
_HmDVMRPVersionString_Object=MibScalar
hmDVMRPVersionString=_HmDVMRPVersionString_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,1),_HmDVMRPVersionString_Type())
hmDVMRPVersionString.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPVersionString.setStatus(_A)
_HmDVMRPGenerationId_Type=Integer32
_HmDVMRPGenerationId_Object=MibScalar
hmDVMRPGenerationId=_HmDVMRPGenerationId_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,2),_HmDVMRPGenerationId_Type())
hmDVMRPGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPGenerationId.setStatus('obsolete')
_HmDVMRPNumRoutes_Type=Gauge32
_HmDVMRPNumRoutes_Object=MibScalar
hmDVMRPNumRoutes=_HmDVMRPNumRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,3),_HmDVMRPNumRoutes_Type())
hmDVMRPNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNumRoutes.setStatus(_A)
_HmDVMRPReachableRoutes_Type=Gauge32
_HmDVMRPReachableRoutes_Object=MibScalar
hmDVMRPReachableRoutes=_HmDVMRPReachableRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,4),_HmDVMRPReachableRoutes_Type())
hmDVMRPReachableRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPReachableRoutes.setStatus(_A)
class _HmDVMRPUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,240))
_HmDVMRPUpdateInterval_Type.__name__=_E
_HmDVMRPUpdateInterval_Object=MibScalar
hmDVMRPUpdateInterval=_HmDVMRPUpdateInterval_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,10),_HmDVMRPUpdateInterval_Type())
hmDVMRPUpdateInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:hmDVMRPUpdateInterval.setStatus(_A)
class _HmDVMRPPruneLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,64800))
_HmDVMRPPruneLifetime_Type.__name__=_E
_HmDVMRPPruneLifetime_Object=MibScalar
hmDVMRPPruneLifetime=_HmDVMRPPruneLifetime_Object((1,3,6,1,4,1,248,15,4,100,1,1,1,11),_HmDVMRPPruneLifetime_Type())
hmDVMRPPruneLifetime.setMaxAccess(_J)
if mibBuilder.loadTexts:hmDVMRPPruneLifetime.setStatus(_A)
_HmDVMRPInterfaceTable_Object=MibTable
hmDVMRPInterfaceTable=_HmDVMRPInterfaceTable_Object((1,3,6,1,4,1,248,15,4,100,1,1,2))
if mibBuilder.loadTexts:hmDVMRPInterfaceTable.setStatus(_A)
_HmDVMRPInterfaceEntry_Object=MibTableRow
hmDVMRPInterfaceEntry=_HmDVMRPInterfaceEntry_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1))
hmDVMRPInterfaceEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hmDVMRPInterfaceEntry.setStatus(_A)
_HmDVMRPInterfaceIfIndex_Type=InterfaceIndex
_HmDVMRPInterfaceIfIndex_Object=MibTableColumn
hmDVMRPInterfaceIfIndex=_HmDVMRPInterfaceIfIndex_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,1),_HmDVMRPInterfaceIfIndex_Type())
hmDVMRPInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPInterfaceIfIndex.setStatus(_A)
_HmDVMRPInterfaceLocalAddress_Type=IpAddress
_HmDVMRPInterfaceLocalAddress_Object=MibTableColumn
hmDVMRPInterfaceLocalAddress=_HmDVMRPInterfaceLocalAddress_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,2),_HmDVMRPInterfaceLocalAddress_Type())
hmDVMRPInterfaceLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPInterfaceLocalAddress.setStatus(_A)
class _HmDVMRPInterfaceMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_HmDVMRPInterfaceMetric_Type.__name__=_E
_HmDVMRPInterfaceMetric_Object=MibTableColumn
hmDVMRPInterfaceMetric=_HmDVMRPInterfaceMetric_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,3),_HmDVMRPInterfaceMetric_Type())
hmDVMRPInterfaceMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:hmDVMRPInterfaceMetric.setStatus(_A)
class _HmDVMRPInterfaceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HmDVMRPInterfaceStatus_Type.__name__=_E
_HmDVMRPInterfaceStatus_Object=MibTableColumn
hmDVMRPInterfaceStatus=_HmDVMRPInterfaceStatus_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,4),_HmDVMRPInterfaceStatus_Type())
hmDVMRPInterfaceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hmDVMRPInterfaceStatus.setStatus(_A)
_HmDVMRPInterfaceRcvBadPkts_Type=Counter32
_HmDVMRPInterfaceRcvBadPkts_Object=MibTableColumn
hmDVMRPInterfaceRcvBadPkts=_HmDVMRPInterfaceRcvBadPkts_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,5),_HmDVMRPInterfaceRcvBadPkts_Type())
hmDVMRPInterfaceRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPInterfaceRcvBadPkts.setStatus(_A)
_HmDVMRPInterfaceRcvBadRoutes_Type=Counter32
_HmDVMRPInterfaceRcvBadRoutes_Object=MibTableColumn
hmDVMRPInterfaceRcvBadRoutes=_HmDVMRPInterfaceRcvBadRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,6),_HmDVMRPInterfaceRcvBadRoutes_Type())
hmDVMRPInterfaceRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPInterfaceRcvBadRoutes.setStatus(_A)
_HmDVMRPInterfaceSentRoutes_Type=Counter32
_HmDVMRPInterfaceSentRoutes_Object=MibTableColumn
hmDVMRPInterfaceSentRoutes=_HmDVMRPInterfaceSentRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,7),_HmDVMRPInterfaceSentRoutes_Type())
hmDVMRPInterfaceSentRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPInterfaceSentRoutes.setStatus(_A)
_HmDVMRPInterfaceInterfaceKey_Type=SnmpAdminString
_HmDVMRPInterfaceInterfaceKey_Object=MibTableColumn
hmDVMRPInterfaceInterfaceKey=_HmDVMRPInterfaceInterfaceKey_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,8),_HmDVMRPInterfaceInterfaceKey_Type())
hmDVMRPInterfaceInterfaceKey.setMaxAccess(_F)
if mibBuilder.loadTexts:hmDVMRPInterfaceInterfaceKey.setStatus(_A)
_HmDVMRPInterfaceInterfaceKeyVersion_Type=Integer32
_HmDVMRPInterfaceInterfaceKeyVersion_Object=MibTableColumn
hmDVMRPInterfaceInterfaceKeyVersion=_HmDVMRPInterfaceInterfaceKeyVersion_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,9),_HmDVMRPInterfaceInterfaceKeyVersion_Type())
hmDVMRPInterfaceInterfaceKeyVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:hmDVMRPInterfaceInterfaceKeyVersion.setStatus(_A)
_HmDVMRPInterfaceGenerationId_Type=Unsigned32
_HmDVMRPInterfaceGenerationId_Object=MibTableColumn
hmDVMRPInterfaceGenerationId=_HmDVMRPInterfaceGenerationId_Object((1,3,6,1,4,1,248,15,4,100,1,1,2,1,20),_HmDVMRPInterfaceGenerationId_Type())
hmDVMRPInterfaceGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPInterfaceGenerationId.setStatus(_A)
_HmDVMRPNeighborTable_Object=MibTable
hmDVMRPNeighborTable=_HmDVMRPNeighborTable_Object((1,3,6,1,4,1,248,15,4,100,1,1,3))
if mibBuilder.loadTexts:hmDVMRPNeighborTable.setStatus(_A)
_HmDVMRPNeighborEntry_Object=MibTableRow
hmDVMRPNeighborEntry=_HmDVMRPNeighborEntry_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1))
hmDVMRPNeighborEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:hmDVMRPNeighborEntry.setStatus(_A)
_HmDVMRPNeighborIfIndex_Type=InterfaceIndex
_HmDVMRPNeighborIfIndex_Object=MibTableColumn
hmDVMRPNeighborIfIndex=_HmDVMRPNeighborIfIndex_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,1),_HmDVMRPNeighborIfIndex_Type())
hmDVMRPNeighborIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPNeighborIfIndex.setStatus(_A)
_HmDVMRPNeighborAddress_Type=IpAddress
_HmDVMRPNeighborAddress_Object=MibTableColumn
hmDVMRPNeighborAddress=_HmDVMRPNeighborAddress_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,2),_HmDVMRPNeighborAddress_Type())
hmDVMRPNeighborAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPNeighborAddress.setStatus(_A)
_HmDVMRPNeighborUpTime_Type=TimeTicks
_HmDVMRPNeighborUpTime_Object=MibTableColumn
hmDVMRPNeighborUpTime=_HmDVMRPNeighborUpTime_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,3),_HmDVMRPNeighborUpTime_Type())
hmDVMRPNeighborUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborUpTime.setStatus(_A)
_HmDVMRPNeighborExpiryTime_Type=TimeTicks
_HmDVMRPNeighborExpiryTime_Object=MibTableColumn
hmDVMRPNeighborExpiryTime=_HmDVMRPNeighborExpiryTime_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,4),_HmDVMRPNeighborExpiryTime_Type())
hmDVMRPNeighborExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborExpiryTime.setStatus(_A)
_HmDVMRPNeighborGenerationId_Type=Integer32
_HmDVMRPNeighborGenerationId_Object=MibTableColumn
hmDVMRPNeighborGenerationId=_HmDVMRPNeighborGenerationId_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,5),_HmDVMRPNeighborGenerationId_Type())
hmDVMRPNeighborGenerationId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborGenerationId.setStatus(_A)
class _HmDVMRPNeighborMajorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmDVMRPNeighborMajorVersion_Type.__name__=_E
_HmDVMRPNeighborMajorVersion_Object=MibTableColumn
hmDVMRPNeighborMajorVersion=_HmDVMRPNeighborMajorVersion_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,6),_HmDVMRPNeighborMajorVersion_Type())
hmDVMRPNeighborMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborMajorVersion.setStatus(_A)
class _HmDVMRPNeighborMinorVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmDVMRPNeighborMinorVersion_Type.__name__=_E
_HmDVMRPNeighborMinorVersion_Object=MibTableColumn
hmDVMRPNeighborMinorVersion=_HmDVMRPNeighborMinorVersion_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,7),_HmDVMRPNeighborMinorVersion_Type())
hmDVMRPNeighborMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborMinorVersion.setStatus(_A)
class _HmDVMRPNeighborCapabilities_Type(Bits):namedValues=NamedValues(*(('leaf',0),('prune',1),('generationID',2),('mtrace',3)))
_HmDVMRPNeighborCapabilities_Type.__name__='Bits'
_HmDVMRPNeighborCapabilities_Object=MibTableColumn
hmDVMRPNeighborCapabilities=_HmDVMRPNeighborCapabilities_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,8),_HmDVMRPNeighborCapabilities_Type())
hmDVMRPNeighborCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborCapabilities.setStatus(_A)
_HmDVMRPNeighborRcvRoutes_Type=Counter32
_HmDVMRPNeighborRcvRoutes_Object=MibTableColumn
hmDVMRPNeighborRcvRoutes=_HmDVMRPNeighborRcvRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,9),_HmDVMRPNeighborRcvRoutes_Type())
hmDVMRPNeighborRcvRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborRcvRoutes.setStatus(_A)
_HmDVMRPNeighborRcvBadPkts_Type=Counter32
_HmDVMRPNeighborRcvBadPkts_Object=MibTableColumn
hmDVMRPNeighborRcvBadPkts=_HmDVMRPNeighborRcvBadPkts_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,10),_HmDVMRPNeighborRcvBadPkts_Type())
hmDVMRPNeighborRcvBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborRcvBadPkts.setStatus(_A)
_HmDVMRPNeighborRcvBadRoutes_Type=Counter32
_HmDVMRPNeighborRcvBadRoutes_Object=MibTableColumn
hmDVMRPNeighborRcvBadRoutes=_HmDVMRPNeighborRcvBadRoutes_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,11),_HmDVMRPNeighborRcvBadRoutes_Type())
hmDVMRPNeighborRcvBadRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborRcvBadRoutes.setStatus(_A)
class _HmDVMRPNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oneway',1),('active',2),('ignoring',3),('down',4)))
_HmDVMRPNeighborState_Type.__name__=_E
_HmDVMRPNeighborState_Object=MibTableColumn
hmDVMRPNeighborState=_HmDVMRPNeighborState_Object((1,3,6,1,4,1,248,15,4,100,1,1,3,1,12),_HmDVMRPNeighborState_Type())
hmDVMRPNeighborState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPNeighborState.setStatus(_A)
_HmDVMRPRouteTable_Object=MibTable
hmDVMRPRouteTable=_HmDVMRPRouteTable_Object((1,3,6,1,4,1,248,15,4,100,1,1,4))
if mibBuilder.loadTexts:hmDVMRPRouteTable.setStatus(_A)
_HmDVMRPRouteEntry_Object=MibTableRow
hmDVMRPRouteEntry=_HmDVMRPRouteEntry_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1))
hmDVMRPRouteEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:hmDVMRPRouteEntry.setStatus(_A)
_HmDVMRPRouteSource_Type=IpAddress
_HmDVMRPRouteSource_Object=MibTableColumn
hmDVMRPRouteSource=_HmDVMRPRouteSource_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,1),_HmDVMRPRouteSource_Type())
hmDVMRPRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPRouteSource.setStatus(_A)
_HmDVMRPRouteSourceMask_Type=IpAddress
_HmDVMRPRouteSourceMask_Object=MibTableColumn
hmDVMRPRouteSourceMask=_HmDVMRPRouteSourceMask_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,2),_HmDVMRPRouteSourceMask_Type())
hmDVMRPRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPRouteSourceMask.setStatus(_A)
_HmDVMRPRouteUpstreamNeighbor_Type=IpAddress
_HmDVMRPRouteUpstreamNeighbor_Object=MibTableColumn
hmDVMRPRouteUpstreamNeighbor=_HmDVMRPRouteUpstreamNeighbor_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,3),_HmDVMRPRouteUpstreamNeighbor_Type())
hmDVMRPRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteUpstreamNeighbor.setStatus(_A)
_HmDVMRPRouteIfIndex_Type=InterfaceIndexOrZero
_HmDVMRPRouteIfIndex_Object=MibTableColumn
hmDVMRPRouteIfIndex=_HmDVMRPRouteIfIndex_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,4),_HmDVMRPRouteIfIndex_Type())
hmDVMRPRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteIfIndex.setStatus(_A)
class _HmDVMRPRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmDVMRPRouteMetric_Type.__name__=_E
_HmDVMRPRouteMetric_Object=MibTableColumn
hmDVMRPRouteMetric=_HmDVMRPRouteMetric_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,5),_HmDVMRPRouteMetric_Type())
hmDVMRPRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteMetric.setStatus(_A)
_HmDVMRPRouteExpiryTime_Type=TimeTicks
_HmDVMRPRouteExpiryTime_Object=MibTableColumn
hmDVMRPRouteExpiryTime=_HmDVMRPRouteExpiryTime_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,6),_HmDVMRPRouteExpiryTime_Type())
hmDVMRPRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteExpiryTime.setStatus(_A)
_HmDVMRPRouteUpTime_Type=TimeTicks
_HmDVMRPRouteUpTime_Object=MibTableColumn
hmDVMRPRouteUpTime=_HmDVMRPRouteUpTime_Object((1,3,6,1,4,1,248,15,4,100,1,1,4,1,7),_HmDVMRPRouteUpTime_Type())
hmDVMRPRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteUpTime.setStatus(_A)
_HmDVMRPRouteNextHopTable_Object=MibTable
hmDVMRPRouteNextHopTable=_HmDVMRPRouteNextHopTable_Object((1,3,6,1,4,1,248,15,4,100,1,1,5))
if mibBuilder.loadTexts:hmDVMRPRouteNextHopTable.setStatus(_A)
_HmDVMRPRouteNextHopEntry_Object=MibTableRow
hmDVMRPRouteNextHopEntry=_HmDVMRPRouteNextHopEntry_Object((1,3,6,1,4,1,248,15,4,100,1,1,5,1))
hmDVMRPRouteNextHopEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:hmDVMRPRouteNextHopEntry.setStatus(_A)
_HmDVMRPRouteNextHopSource_Type=IpAddress
_HmDVMRPRouteNextHopSource_Object=MibTableColumn
hmDVMRPRouteNextHopSource=_HmDVMRPRouteNextHopSource_Object((1,3,6,1,4,1,248,15,4,100,1,1,5,1,1),_HmDVMRPRouteNextHopSource_Type())
hmDVMRPRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPRouteNextHopSource.setStatus(_A)
_HmDVMRPRouteNextHopSourceMask_Type=IpAddress
_HmDVMRPRouteNextHopSourceMask_Object=MibTableColumn
hmDVMRPRouteNextHopSourceMask=_HmDVMRPRouteNextHopSourceMask_Object((1,3,6,1,4,1,248,15,4,100,1,1,5,1,2),_HmDVMRPRouteNextHopSourceMask_Type())
hmDVMRPRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPRouteNextHopSourceMask.setStatus(_A)
_HmDVMRPRouteNextHopIfIndex_Type=InterfaceIndex
_HmDVMRPRouteNextHopIfIndex_Object=MibTableColumn
hmDVMRPRouteNextHopIfIndex=_HmDVMRPRouteNextHopIfIndex_Object((1,3,6,1,4,1,248,15,4,100,1,1,5,1,3),_HmDVMRPRouteNextHopIfIndex_Type())
hmDVMRPRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPRouteNextHopIfIndex.setStatus(_A)
class _HmDVMRPRouteNextHopType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('leaf',1),('branch',2)))
_HmDVMRPRouteNextHopType_Type.__name__=_E
_HmDVMRPRouteNextHopType_Object=MibTableColumn
hmDVMRPRouteNextHopType=_HmDVMRPRouteNextHopType_Object((1,3,6,1,4,1,248,15,4,100,1,1,5,1,4),_HmDVMRPRouteNextHopType_Type())
hmDVMRPRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPRouteNextHopType.setStatus(_A)
_HmDVMRPPruneTable_Object=MibTable
hmDVMRPPruneTable=_HmDVMRPPruneTable_Object((1,3,6,1,4,1,248,15,4,100,1,1,6))
if mibBuilder.loadTexts:hmDVMRPPruneTable.setStatus(_A)
_HmDVMRPPruneEntry_Object=MibTableRow
hmDVMRPPruneEntry=_HmDVMRPPruneEntry_Object((1,3,6,1,4,1,248,15,4,100,1,1,6,1))
hmDVMRPPruneEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:hmDVMRPPruneEntry.setStatus(_A)
_HmDVMRPPruneGroup_Type=IpAddress
_HmDVMRPPruneGroup_Object=MibTableColumn
hmDVMRPPruneGroup=_HmDVMRPPruneGroup_Object((1,3,6,1,4,1,248,15,4,100,1,1,6,1,1),_HmDVMRPPruneGroup_Type())
hmDVMRPPruneGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPPruneGroup.setStatus(_A)
_HmDVMRPPruneSource_Type=IpAddress
_HmDVMRPPruneSource_Object=MibTableColumn
hmDVMRPPruneSource=_HmDVMRPPruneSource_Object((1,3,6,1,4,1,248,15,4,100,1,1,6,1,2),_HmDVMRPPruneSource_Type())
hmDVMRPPruneSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPPruneSource.setStatus(_A)
_HmDVMRPPruneSourceMask_Type=IpAddress
_HmDVMRPPruneSourceMask_Object=MibTableColumn
hmDVMRPPruneSourceMask=_HmDVMRPPruneSourceMask_Object((1,3,6,1,4,1,248,15,4,100,1,1,6,1,3),_HmDVMRPPruneSourceMask_Type())
hmDVMRPPruneSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmDVMRPPruneSourceMask.setStatus(_A)
_HmDVMRPPruneExpiryTime_Type=TimeTicks
_HmDVMRPPruneExpiryTime_Object=MibTableColumn
hmDVMRPPruneExpiryTime=_HmDVMRPPruneExpiryTime_Object((1,3,6,1,4,1,248,15,4,100,1,1,6,1,4),_HmDVMRPPruneExpiryTime_Type())
hmDVMRPPruneExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmDVMRPPruneExpiryTime.setStatus(_A)
_HmDVMRPTraps_ObjectIdentity=ObjectIdentity
hmDVMRPTraps=_HmDVMRPTraps_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,1,1,7))
_HmDVMRPMIBConformance_ObjectIdentity=ObjectIdentity
hmDVMRPMIBConformance=_HmDVMRPMIBConformance_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,2))
_HmDVMRPMIBCompliances_ObjectIdentity=ObjectIdentity
hmDVMRPMIBCompliances=_HmDVMRPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,2,1))
_HmDVMRPMIBGroups_ObjectIdentity=ObjectIdentity
hmDVMRPMIBGroups=_HmDVMRPMIBGroups_ObjectIdentity((1,3,6,1,4,1,248,15,4,100,2,2))
hmDVMRPGeneralGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,2))
hmDVMRPGeneralGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hmDVMRPGeneralGroup.setStatus(_A)
hmDVMRPInterfaceGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,3))
hmDVMRPInterfaceGroup.setObjects(*((_B,_G),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:hmDVMRPInterfaceGroup.setStatus(_A)
hmDVMRPNeighborGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,4))
hmDVMRPNeighborGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_H),(_B,_k),(_B,_l),(_B,_m),(_B,_I)))
if mibBuilder.loadTexts:hmDVMRPNeighborGroup.setStatus(_A)
hmDVMRPRoutingGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,5))
hmDVMRPRoutingGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:hmDVMRPRoutingGroup.setStatus(_A)
hmDVMRPSecurityGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,6))
hmDVMRPSecurityGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:hmDVMRPSecurityGroup.setStatus(_A)
hmDVMRPTreeGroup=ObjectGroup((1,3,6,1,4,1,248,15,4,100,2,2,7))
hmDVMRPTreeGroup.setObjects((_B,_v))
if mibBuilder.loadTexts:hmDVMRPTreeGroup.setStatus(_A)
hmDVMRPNeighborLoss=NotificationType((1,3,6,1,4,1,248,15,4,100,1,1,7,1))
hmDVMRPNeighborLoss.setObjects(*((_B,_G),(_B,_I)))
if mibBuilder.loadTexts:hmDVMRPNeighborLoss.setStatus(_A)
hmDVMRPNeighborNotPruning=NotificationType((1,3,6,1,4,1,248,15,4,100,1,1,7,2))
hmDVMRPNeighborNotPruning.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:hmDVMRPNeighborNotPruning.setStatus(_A)
hmDVMRPNotificationGroup=NotificationGroup((1,3,6,1,4,1,248,15,4,100,2,2,8))
hmDVMRPNotificationGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:hmDVMRPNotificationGroup.setStatus(_A)
hmDVMRPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,248,15,4,100,2,1,1))
hmDVMRPMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:hmDVMRPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hmDVMRPMIB':hmDVMRPMIB,'hmDVMRPMIBObjects':hmDVMRPMIBObjects,'hmDVMRP':hmDVMRP,'hmDVMRPScalar':hmDVMRPScalar,_V:hmDVMRPVersionString,_W:hmDVMRPGenerationId,_X:hmDVMRPNumRoutes,_Y:hmDVMRPReachableRoutes,'hmDVMRPUpdateInterval':hmDVMRPUpdateInterval,'hmDVMRPPruneLifetime':hmDVMRPPruneLifetime,'hmDVMRPInterfaceTable':hmDVMRPInterfaceTable,'hmDVMRPInterfaceEntry':hmDVMRPInterfaceEntry,_K:hmDVMRPInterfaceIfIndex,_G:hmDVMRPInterfaceLocalAddress,_Z:hmDVMRPInterfaceMetric,_a:hmDVMRPInterfaceStatus,_b:hmDVMRPInterfaceRcvBadPkts,_c:hmDVMRPInterfaceRcvBadRoutes,_d:hmDVMRPInterfaceSentRoutes,_t:hmDVMRPInterfaceInterfaceKey,_u:hmDVMRPInterfaceInterfaceKeyVersion,_e:hmDVMRPInterfaceGenerationId,'hmDVMRPNeighborTable':hmDVMRPNeighborTable,'hmDVMRPNeighborEntry':hmDVMRPNeighborEntry,_L:hmDVMRPNeighborIfIndex,_M:hmDVMRPNeighborAddress,_f:hmDVMRPNeighborUpTime,_g:hmDVMRPNeighborExpiryTime,_h:hmDVMRPNeighborGenerationId,_i:hmDVMRPNeighborMajorVersion,_j:hmDVMRPNeighborMinorVersion,_H:hmDVMRPNeighborCapabilities,_k:hmDVMRPNeighborRcvRoutes,_l:hmDVMRPNeighborRcvBadPkts,_m:hmDVMRPNeighborRcvBadRoutes,_I:hmDVMRPNeighborState,'hmDVMRPRouteTable':hmDVMRPRouteTable,'hmDVMRPRouteEntry':hmDVMRPRouteEntry,_N:hmDVMRPRouteSource,_O:hmDVMRPRouteSourceMask,_n:hmDVMRPRouteUpstreamNeighbor,_o:hmDVMRPRouteIfIndex,_p:hmDVMRPRouteMetric,_q:hmDVMRPRouteExpiryTime,_r:hmDVMRPRouteUpTime,'hmDVMRPRouteNextHopTable':hmDVMRPRouteNextHopTable,'hmDVMRPRouteNextHopEntry':hmDVMRPRouteNextHopEntry,_P:hmDVMRPRouteNextHopSource,_Q:hmDVMRPRouteNextHopSourceMask,_R:hmDVMRPRouteNextHopIfIndex,_s:hmDVMRPRouteNextHopType,'hmDVMRPPruneTable':hmDVMRPPruneTable,'hmDVMRPPruneEntry':hmDVMRPPruneEntry,_S:hmDVMRPPruneGroup,_T:hmDVMRPPruneSource,_U:hmDVMRPPruneSourceMask,_v:hmDVMRPPruneExpiryTime,'hmDVMRPTraps':hmDVMRPTraps,_w:hmDVMRPNeighborLoss,_x:hmDVMRPNeighborNotPruning,'hmDVMRPMIBConformance':hmDVMRPMIBConformance,'hmDVMRPMIBCompliances':hmDVMRPMIBCompliances,'hmDVMRPMIBCompliance':hmDVMRPMIBCompliance,'hmDVMRPMIBGroups':hmDVMRPMIBGroups,_y:hmDVMRPGeneralGroup,_z:hmDVMRPInterfaceGroup,_A0:hmDVMRPNeighborGroup,_A1:hmDVMRPRoutingGroup,_A3:hmDVMRPSecurityGroup,_A2:hmDVMRPTreeGroup,'hmDVMRPNotificationGroup':hmDVMRPNotificationGroup})