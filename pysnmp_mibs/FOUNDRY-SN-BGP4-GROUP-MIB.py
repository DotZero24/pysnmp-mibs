_A6='snBgp4NeighPrefixGroupDir'
_A5='snBgp4NeighPrefixGroupNeighIp'
_A4='snBgp4ClearNeighborCmdIp'
_A3='snBgp4AttributeIndex'
_A2='snBgp4NeighborSummaryIndex'
_A1='snBgp4RouteOperStatusIndex'
_A0='established'
_z='openConfirm'
_y='openSent'
_x='active'
_w='connect'
_v='noState'
_u='snBgp4NeighOperStatusIndex'
_t='snBgp4RouteMapSetSequenceNum'
_s='snBgp4RouteMapSetMapName'
_r='snBgp4RouteMapMatchSequenceNum'
_q='snBgp4RouteMapMatchMapName'
_p='snBgp4RouteMapFilterSequenceNum'
_o='snBgp4RouteMapFilterMapName'
_n='snBgp4RedisProtocol'
_m='snBgp4NetworkSubnetMask'
_l='snBgp4NetworkIp'
_k='snBgp4NeighRouteMapDir'
_j='snBgp4NeighRouteMapNeighIp'
_i='snBgp4NeighFilterGroupDir'
_h='snBgp4NeighFilterGroupNeighIp'
_g='snBgp4NeighDistGroupDir'
_f='snBgp4NeighDistGroupNeighIp'
_e='snBgp4NeighGenCfgNeighIp'
_d='snBgp4CommunityFilterIndex'
_c='snBgp4AsPathFilterIndex'
_b='snBgp4AggregateAddrOption'
_a='snBgp4AggregateAddrMask'
_Z='snBgp4AggregateAddrIp'
_Y='snBgp4AddrFilterIndex'
_X='incomplete'
_W='egp'
_V='igp'
_U='none'
_T='deprecated'
_S='in'
_R='out'
_Q='true'
_P='false'
_O='permit'
_N='deny'
_M='modify'
_L='create'
_K='delete'
_J='invalid'
_I='valid'
_H='enabled'
_G='disabled'
_F='FOUNDRY-SN-BGP4-GROUP-MIB'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
router,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','router')
InetAutonomousSystemNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAutonomousSystemNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snBgp4=ModuleIdentity((1,3,6,1,4,1,1991,1,2,11))
if mibBuilder.loadTexts:snBgp4.setRevisions(('2009-09-30 00:00','2017-08-07 00:00'))
_SnBgp4Gen_ObjectIdentity=ObjectIdentity
snBgp4Gen=_SnBgp4Gen_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,1))
class _SnBgp4GenAlwaysCompareMed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenAlwaysCompareMed_Type.__name__=_D
_SnBgp4GenAlwaysCompareMed_Object=MibScalar
snBgp4GenAlwaysCompareMed=_SnBgp4GenAlwaysCompareMed_Object((1,3,6,1,4,1,1991,1,2,11,1,1),_SnBgp4GenAlwaysCompareMed_Type())
snBgp4GenAlwaysCompareMed.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenAlwaysCompareMed.setStatus(_A)
class _SnBgp4GenAutoSummary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenAutoSummary_Type.__name__=_D
_SnBgp4GenAutoSummary_Object=MibScalar
snBgp4GenAutoSummary=_SnBgp4GenAutoSummary_Object((1,3,6,1,4,1,1991,1,2,11,1,2),_SnBgp4GenAutoSummary_Type())
snBgp4GenAutoSummary.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenAutoSummary.setStatus(_A)
_SnBgp4GenDefaultLocalPreference_Type=Integer32
_SnBgp4GenDefaultLocalPreference_Object=MibScalar
snBgp4GenDefaultLocalPreference=_SnBgp4GenDefaultLocalPreference_Object((1,3,6,1,4,1,1991,1,2,11,1,3),_SnBgp4GenDefaultLocalPreference_Type())
snBgp4GenDefaultLocalPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDefaultLocalPreference.setStatus(_T)
class _SnBgp4GenDefaultInfoOriginate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenDefaultInfoOriginate_Type.__name__=_D
_SnBgp4GenDefaultInfoOriginate_Object=MibScalar
snBgp4GenDefaultInfoOriginate=_SnBgp4GenDefaultInfoOriginate_Object((1,3,6,1,4,1,1991,1,2,11,1,4),_SnBgp4GenDefaultInfoOriginate_Type())
snBgp4GenDefaultInfoOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDefaultInfoOriginate.setStatus(_A)
class _SnBgp4GenFastExternalFallover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenFastExternalFallover_Type.__name__=_D
_SnBgp4GenFastExternalFallover_Object=MibScalar
snBgp4GenFastExternalFallover=_SnBgp4GenFastExternalFallover_Object((1,3,6,1,4,1,1991,1,2,11,1,5),_SnBgp4GenFastExternalFallover_Type())
snBgp4GenFastExternalFallover.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenFastExternalFallover.setStatus(_A)
_SnBgp4GenNextBootNeighbors_Type=Integer32
_SnBgp4GenNextBootNeighbors_Object=MibScalar
snBgp4GenNextBootNeighbors=_SnBgp4GenNextBootNeighbors_Object((1,3,6,1,4,1,1991,1,2,11,1,6),_SnBgp4GenNextBootNeighbors_Type())
snBgp4GenNextBootNeighbors.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenNextBootNeighbors.setStatus(_A)
_SnBgp4GenNextBootRoutes_Type=Integer32
_SnBgp4GenNextBootRoutes_Object=MibScalar
snBgp4GenNextBootRoutes=_SnBgp4GenNextBootRoutes_Object((1,3,6,1,4,1,1991,1,2,11,1,7),_SnBgp4GenNextBootRoutes_Type())
snBgp4GenNextBootRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenNextBootRoutes.setStatus(_A)
class _SnBgp4GenSynchronization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenSynchronization_Type.__name__=_D
_SnBgp4GenSynchronization_Object=MibScalar
snBgp4GenSynchronization=_SnBgp4GenSynchronization_Object((1,3,6,1,4,1,1991,1,2,11,1,8),_SnBgp4GenSynchronization_Type())
snBgp4GenSynchronization.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenSynchronization.setStatus(_A)
class _SnBgp4GenKeepAliveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4GenKeepAliveTime_Type.__name__=_D
_SnBgp4GenKeepAliveTime_Object=MibScalar
snBgp4GenKeepAliveTime=_SnBgp4GenKeepAliveTime_Object((1,3,6,1,4,1,1991,1,2,11,1,9),_SnBgp4GenKeepAliveTime_Type())
snBgp4GenKeepAliveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenKeepAliveTime.setStatus(_A)
class _SnBgp4GenHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4GenHoldTime_Type.__name__=_D
_SnBgp4GenHoldTime_Object=MibScalar
snBgp4GenHoldTime=_SnBgp4GenHoldTime_Object((1,3,6,1,4,1,1991,1,2,11,1,10),_SnBgp4GenHoldTime_Type())
snBgp4GenHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenHoldTime.setStatus(_A)
_SnBgp4GenRouterId_Type=IpAddress
_SnBgp4GenRouterId_Object=MibScalar
snBgp4GenRouterId=_SnBgp4GenRouterId_Object((1,3,6,1,4,1,1991,1,2,11,1,11),_SnBgp4GenRouterId_Type())
snBgp4GenRouterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenRouterId.setStatus(_A)
class _SnBgp4GenTableMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4GenTableMap_Type.__name__=_E
_SnBgp4GenTableMap_Object=MibScalar
snBgp4GenTableMap=_SnBgp4GenTableMap_Object((1,3,6,1,4,1,1991,1,2,11,1,12),_SnBgp4GenTableMap_Type())
snBgp4GenTableMap.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenTableMap.setStatus(_A)
class _SnBgp4GenAdminStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4GenAdminStat_Type.__name__=_D
_SnBgp4GenAdminStat_Object=MibScalar
snBgp4GenAdminStat=_SnBgp4GenAdminStat_Object((1,3,6,1,4,1,1991,1,2,11,1,13),_SnBgp4GenAdminStat_Type())
snBgp4GenAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenAdminStat.setStatus(_A)
_SnBgp4GenDefaultMetric_Type=Integer32
_SnBgp4GenDefaultMetric_Object=MibScalar
snBgp4GenDefaultMetric=_SnBgp4GenDefaultMetric_Object((1,3,6,1,4,1,1991,1,2,11,1,14),_SnBgp4GenDefaultMetric_Type())
snBgp4GenDefaultMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDefaultMetric.setStatus(_T)
_SnBgp4GenMaxNeighbors_Type=Integer32
_SnBgp4GenMaxNeighbors_Object=MibScalar
snBgp4GenMaxNeighbors=_SnBgp4GenMaxNeighbors_Object((1,3,6,1,4,1,1991,1,2,11,1,15),_SnBgp4GenMaxNeighbors_Type())
snBgp4GenMaxNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxNeighbors.setStatus(_A)
_SnBgp4GenMinNeighbors_Type=Integer32
_SnBgp4GenMinNeighbors_Object=MibScalar
snBgp4GenMinNeighbors=_SnBgp4GenMinNeighbors_Object((1,3,6,1,4,1,1991,1,2,11,1,16),_SnBgp4GenMinNeighbors_Type())
snBgp4GenMinNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMinNeighbors.setStatus(_A)
_SnBgp4GenMaxRoutes_Type=Integer32
_SnBgp4GenMaxRoutes_Object=MibScalar
snBgp4GenMaxRoutes=_SnBgp4GenMaxRoutes_Object((1,3,6,1,4,1,1991,1,2,11,1,17),_SnBgp4GenMaxRoutes_Type())
snBgp4GenMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxRoutes.setStatus(_A)
_SnBgp4GenMinRoutes_Type=Integer32
_SnBgp4GenMinRoutes_Object=MibScalar
snBgp4GenMinRoutes=_SnBgp4GenMinRoutes_Object((1,3,6,1,4,1,1991,1,2,11,1,18),_SnBgp4GenMinRoutes_Type())
snBgp4GenMinRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMinRoutes.setStatus(_A)
_SnBgp4GenMaxAddrFilters_Type=Integer32
_SnBgp4GenMaxAddrFilters_Object=MibScalar
snBgp4GenMaxAddrFilters=_SnBgp4GenMaxAddrFilters_Object((1,3,6,1,4,1,1991,1,2,11,1,19),_SnBgp4GenMaxAddrFilters_Type())
snBgp4GenMaxAddrFilters.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxAddrFilters.setStatus(_A)
_SnBgp4GenMaxAggregateAddresses_Type=Integer32
_SnBgp4GenMaxAggregateAddresses_Object=MibScalar
snBgp4GenMaxAggregateAddresses=_SnBgp4GenMaxAggregateAddresses_Object((1,3,6,1,4,1,1991,1,2,11,1,20),_SnBgp4GenMaxAggregateAddresses_Type())
snBgp4GenMaxAggregateAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxAggregateAddresses.setStatus(_A)
_SnBgp4GenMaxAsPathFilters_Type=Integer32
_SnBgp4GenMaxAsPathFilters_Object=MibScalar
snBgp4GenMaxAsPathFilters=_SnBgp4GenMaxAsPathFilters_Object((1,3,6,1,4,1,1991,1,2,11,1,21),_SnBgp4GenMaxAsPathFilters_Type())
snBgp4GenMaxAsPathFilters.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxAsPathFilters.setStatus(_A)
_SnBgp4GenMaxCommunityFilters_Type=Integer32
_SnBgp4GenMaxCommunityFilters_Object=MibScalar
snBgp4GenMaxCommunityFilters=_SnBgp4GenMaxCommunityFilters_Object((1,3,6,1,4,1,1991,1,2,11,1,22),_SnBgp4GenMaxCommunityFilters_Type())
snBgp4GenMaxCommunityFilters.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxCommunityFilters.setStatus(_A)
_SnBgp4GenMaxNetworks_Type=Integer32
_SnBgp4GenMaxNetworks_Object=MibScalar
snBgp4GenMaxNetworks=_SnBgp4GenMaxNetworks_Object((1,3,6,1,4,1,1991,1,2,11,1,23),_SnBgp4GenMaxNetworks_Type())
snBgp4GenMaxNetworks.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxNetworks.setStatus(_A)
_SnBgp4GenMaxRouteMapFilters_Type=Integer32
_SnBgp4GenMaxRouteMapFilters_Object=MibScalar
snBgp4GenMaxRouteMapFilters=_SnBgp4GenMaxRouteMapFilters_Object((1,3,6,1,4,1,1991,1,2,11,1,24),_SnBgp4GenMaxRouteMapFilters_Type())
snBgp4GenMaxRouteMapFilters.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenMaxRouteMapFilters.setStatus(_A)
_SnBgp4GenNeighPrefixMinValue_Type=Integer32
_SnBgp4GenNeighPrefixMinValue_Object=MibScalar
snBgp4GenNeighPrefixMinValue=_SnBgp4GenNeighPrefixMinValue_Object((1,3,6,1,4,1,1991,1,2,11,1,25),_SnBgp4GenNeighPrefixMinValue_Type())
snBgp4GenNeighPrefixMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenNeighPrefixMinValue.setStatus(_A)
_SnBgp4GenOperNeighbors_Type=Integer32
_SnBgp4GenOperNeighbors_Object=MibScalar
snBgp4GenOperNeighbors=_SnBgp4GenOperNeighbors_Object((1,3,6,1,4,1,1991,1,2,11,1,26),_SnBgp4GenOperNeighbors_Type())
snBgp4GenOperNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenOperNeighbors.setStatus(_A)
_SnBgp4GenOperRoutes_Type=Integer32
_SnBgp4GenOperRoutes_Object=MibScalar
snBgp4GenOperRoutes=_SnBgp4GenOperRoutes_Object((1,3,6,1,4,1,1991,1,2,11,1,27),_SnBgp4GenOperRoutes_Type())
snBgp4GenOperRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenOperRoutes.setStatus(_A)
class _SnBgp4GenLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnBgp4GenLocalAs_Type.__name__=_D
_SnBgp4GenLocalAs_Object=MibScalar
snBgp4GenLocalAs=_SnBgp4GenLocalAs_Object((1,3,6,1,4,1,1991,1,2,11,1,28),_SnBgp4GenLocalAs_Type())
snBgp4GenLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenLocalAs.setStatus(_A)
_SnBgp4GenRoutesInstalled_Type=Integer32
_SnBgp4GenRoutesInstalled_Object=MibScalar
snBgp4GenRoutesInstalled=_SnBgp4GenRoutesInstalled_Object((1,3,6,1,4,1,1991,1,2,11,1,29),_SnBgp4GenRoutesInstalled_Type())
snBgp4GenRoutesInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenRoutesInstalled.setStatus(_A)
_SnBgp4GenAsPathInstalled_Type=Integer32
_SnBgp4GenAsPathInstalled_Object=MibScalar
snBgp4GenAsPathInstalled=_SnBgp4GenAsPathInstalled_Object((1,3,6,1,4,1,1991,1,2,11,1,30),_SnBgp4GenAsPathInstalled_Type())
snBgp4GenAsPathInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenAsPathInstalled.setStatus(_A)
class _SnBgp4ExternalDistance_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnBgp4ExternalDistance_Type.__name__=_D
_SnBgp4ExternalDistance_Object=MibScalar
snBgp4ExternalDistance=_SnBgp4ExternalDistance_Object((1,3,6,1,4,1,1991,1,2,11,1,31),_SnBgp4ExternalDistance_Type())
snBgp4ExternalDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4ExternalDistance.setStatus(_A)
class _SnBgp4InternalDistance_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnBgp4InternalDistance_Type.__name__=_D
_SnBgp4InternalDistance_Object=MibScalar
snBgp4InternalDistance=_SnBgp4InternalDistance_Object((1,3,6,1,4,1,1991,1,2,11,1,32),_SnBgp4InternalDistance_Type())
snBgp4InternalDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4InternalDistance.setStatus(_A)
class _SnBgp4LocalDistance_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnBgp4LocalDistance_Type.__name__=_D
_SnBgp4LocalDistance_Object=MibScalar
snBgp4LocalDistance=_SnBgp4LocalDistance_Object((1,3,6,1,4,1,1991,1,2,11,1,33),_SnBgp4LocalDistance_Type())
snBgp4LocalDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4LocalDistance.setStatus(_A)
_SnBgp4OperNumOfAttributes_Type=Integer32
_SnBgp4OperNumOfAttributes_Object=MibScalar
snBgp4OperNumOfAttributes=_SnBgp4OperNumOfAttributes_Object((1,3,6,1,4,1,1991,1,2,11,1,34),_SnBgp4OperNumOfAttributes_Type())
snBgp4OperNumOfAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4OperNumOfAttributes.setStatus(_A)
class _SnBgp4NextBootMaxAttributes_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,30000))
_SnBgp4NextBootMaxAttributes_Type.__name__=_D
_SnBgp4NextBootMaxAttributes_Object=MibScalar
snBgp4NextBootMaxAttributes=_SnBgp4NextBootMaxAttributes_Object((1,3,6,1,4,1,1991,1,2,11,1,35),_SnBgp4NextBootMaxAttributes_Type())
snBgp4NextBootMaxAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NextBootMaxAttributes.setStatus(_A)
_SnBgp4ClusterId_Type=Integer32
_SnBgp4ClusterId_Object=MibScalar
snBgp4ClusterId=_SnBgp4ClusterId_Object((1,3,6,1,4,1,1991,1,2,11,1,36),_SnBgp4ClusterId_Type())
snBgp4ClusterId.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4ClusterId.setStatus(_A)
class _SnBgp4ClientToClientReflection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4ClientToClientReflection_Type.__name__=_D
_SnBgp4ClientToClientReflection_Object=MibScalar
snBgp4ClientToClientReflection=_SnBgp4ClientToClientReflection_Object((1,3,6,1,4,1,1991,1,2,11,1,37),_SnBgp4ClientToClientReflection_Type())
snBgp4ClientToClientReflection.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4ClientToClientReflection.setStatus(_A)
_SnBgp4GenTotalNeighbors_Type=Integer32
_SnBgp4GenTotalNeighbors_Object=MibScalar
snBgp4GenTotalNeighbors=_SnBgp4GenTotalNeighbors_Object((1,3,6,1,4,1,1991,1,2,11,1,38),_SnBgp4GenTotalNeighbors_Type())
snBgp4GenTotalNeighbors.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4GenTotalNeighbors.setStatus(_A)
class _SnBgp4GenMaxPaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnBgp4GenMaxPaths_Type.__name__=_D
_SnBgp4GenMaxPaths_Object=MibScalar
snBgp4GenMaxPaths=_SnBgp4GenMaxPaths_Object((1,3,6,1,4,1,1991,1,2,11,1,39),_SnBgp4GenMaxPaths_Type())
snBgp4GenMaxPaths.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenMaxPaths.setStatus(_A)
class _SnBgp4GenConfedId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnBgp4GenConfedId_Type.__name__=_D
_SnBgp4GenConfedId_Object=MibScalar
snBgp4GenConfedId=_SnBgp4GenConfedId_Object((1,3,6,1,4,1,1991,1,2,11,1,40),_SnBgp4GenConfedId_Type())
snBgp4GenConfedId.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenConfedId.setStatus(_A)
class _SnBgp4GenConfedPeers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SnBgp4GenConfedPeers_Type.__name__=_E
_SnBgp4GenConfedPeers_Object=MibScalar
snBgp4GenConfedPeers=_SnBgp4GenConfedPeers_Object((1,3,6,1,4,1,1991,1,2,11,1,41),_SnBgp4GenConfedPeers_Type())
snBgp4GenConfedPeers.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenConfedPeers.setStatus(_A)
class _SnBgp4GenDampening_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),('parameters',1),('routeMap',2)))
_SnBgp4GenDampening_Type.__name__=_D
_SnBgp4GenDampening_Object=MibScalar
snBgp4GenDampening=_SnBgp4GenDampening_Object((1,3,6,1,4,1,1991,1,2,11,1,42),_SnBgp4GenDampening_Type())
snBgp4GenDampening.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampening.setStatus(_A)
class _SnBgp4GenDampenHalfLife_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45))
_SnBgp4GenDampenHalfLife_Type.__name__=_D
_SnBgp4GenDampenHalfLife_Object=MibScalar
snBgp4GenDampenHalfLife=_SnBgp4GenDampenHalfLife_Object((1,3,6,1,4,1,1991,1,2,11,1,43),_SnBgp4GenDampenHalfLife_Type())
snBgp4GenDampenHalfLife.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampenHalfLife.setStatus(_A)
class _SnBgp4GenDampenReuse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4GenDampenReuse_Type.__name__=_D
_SnBgp4GenDampenReuse_Object=MibScalar
snBgp4GenDampenReuse=_SnBgp4GenDampenReuse_Object((1,3,6,1,4,1,1991,1,2,11,1,44),_SnBgp4GenDampenReuse_Type())
snBgp4GenDampenReuse.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampenReuse.setStatus(_A)
class _SnBgp4GenDampenSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4GenDampenSuppress_Type.__name__=_D
_SnBgp4GenDampenSuppress_Object=MibScalar
snBgp4GenDampenSuppress=_SnBgp4GenDampenSuppress_Object((1,3,6,1,4,1,1991,1,2,11,1,45),_SnBgp4GenDampenSuppress_Type())
snBgp4GenDampenSuppress.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampenSuppress.setStatus(_A)
class _SnBgp4GenDampenMaxSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4GenDampenMaxSuppress_Type.__name__=_D
_SnBgp4GenDampenMaxSuppress_Object=MibScalar
snBgp4GenDampenMaxSuppress=_SnBgp4GenDampenMaxSuppress_Object((1,3,6,1,4,1,1991,1,2,11,1,46),_SnBgp4GenDampenMaxSuppress_Type())
snBgp4GenDampenMaxSuppress.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampenMaxSuppress.setStatus(_A)
class _SnBgp4GenDampenMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4GenDampenMap_Type.__name__=_E
_SnBgp4GenDampenMap_Object=MibScalar
snBgp4GenDampenMap=_SnBgp4GenDampenMap_Object((1,3,6,1,4,1,1991,1,2,11,1,47),_SnBgp4GenDampenMap_Type())
snBgp4GenDampenMap.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDampenMap.setStatus(_A)
_SnBgp4GenLocalAs4_Type=InetAutonomousSystemNumber
_SnBgp4GenLocalAs4_Object=MibScalar
snBgp4GenLocalAs4=_SnBgp4GenLocalAs4_Object((1,3,6,1,4,1,1991,1,2,11,1,48),_SnBgp4GenLocalAs4_Type())
snBgp4GenLocalAs4.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenLocalAs4.setStatus(_A)
_SnBgp4GenDefaultMetric1_Type=Unsigned32
_SnBgp4GenDefaultMetric1_Object=MibScalar
snBgp4GenDefaultMetric1=_SnBgp4GenDefaultMetric1_Object((1,3,6,1,4,1,1991,1,2,11,1,49),_SnBgp4GenDefaultMetric1_Type())
snBgp4GenDefaultMetric1.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDefaultMetric1.setStatus(_A)
_SnBgp4GenDefaultLocalPreference1_Type=Unsigned32
_SnBgp4GenDefaultLocalPreference1_Object=MibScalar
snBgp4GenDefaultLocalPreference1=_SnBgp4GenDefaultLocalPreference1_Object((1,3,6,1,4,1,1991,1,2,11,1,50),_SnBgp4GenDefaultLocalPreference1_Type())
snBgp4GenDefaultLocalPreference1.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4GenDefaultLocalPreference1.setStatus(_A)
_SnBgp4AddrFilter_ObjectIdentity=ObjectIdentity
snBgp4AddrFilter=_SnBgp4AddrFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,2))
_SnBgp4AddrFilterTable_Object=MibTable
snBgp4AddrFilterTable=_SnBgp4AddrFilterTable_Object((1,3,6,1,4,1,1991,1,2,11,2,1))
if mibBuilder.loadTexts:snBgp4AddrFilterTable.setStatus(_A)
_SnBgp4AddrFilterEntry_Object=MibTableRow
snBgp4AddrFilterEntry=_SnBgp4AddrFilterEntry_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1))
snBgp4AddrFilterEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:snBgp4AddrFilterEntry.setStatus(_A)
_SnBgp4AddrFilterIndex_Type=Integer32
_SnBgp4AddrFilterIndex_Object=MibTableColumn
snBgp4AddrFilterIndex=_SnBgp4AddrFilterIndex_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,1),_SnBgp4AddrFilterIndex_Type())
snBgp4AddrFilterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AddrFilterIndex.setStatus(_A)
class _SnBgp4AddrFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_SnBgp4AddrFilterAction_Type.__name__=_D
_SnBgp4AddrFilterAction_Object=MibTableColumn
snBgp4AddrFilterAction=_SnBgp4AddrFilterAction_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,2),_SnBgp4AddrFilterAction_Type())
snBgp4AddrFilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterAction.setStatus(_A)
_SnBgp4AddrFilterSourceIp_Type=IpAddress
_SnBgp4AddrFilterSourceIp_Object=MibTableColumn
snBgp4AddrFilterSourceIp=_SnBgp4AddrFilterSourceIp_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,3),_SnBgp4AddrFilterSourceIp_Type())
snBgp4AddrFilterSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterSourceIp.setStatus(_A)
_SnBgp4AddrFilterSourceMask_Type=IpAddress
_SnBgp4AddrFilterSourceMask_Object=MibTableColumn
snBgp4AddrFilterSourceMask=_SnBgp4AddrFilterSourceMask_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,4),_SnBgp4AddrFilterSourceMask_Type())
snBgp4AddrFilterSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterSourceMask.setStatus(_A)
_SnBgp4AddrFilterDestIp_Type=IpAddress
_SnBgp4AddrFilterDestIp_Object=MibTableColumn
snBgp4AddrFilterDestIp=_SnBgp4AddrFilterDestIp_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,5),_SnBgp4AddrFilterDestIp_Type())
snBgp4AddrFilterDestIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterDestIp.setStatus(_A)
_SnBgp4AddrFilterDestMask_Type=IpAddress
_SnBgp4AddrFilterDestMask_Object=MibTableColumn
snBgp4AddrFilterDestMask=_SnBgp4AddrFilterDestMask_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,6),_SnBgp4AddrFilterDestMask_Type())
snBgp4AddrFilterDestMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterDestMask.setStatus(_A)
class _SnBgp4AddrFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4AddrFilterRowStatus_Type.__name__=_D
_SnBgp4AddrFilterRowStatus_Object=MibTableColumn
snBgp4AddrFilterRowStatus=_SnBgp4AddrFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,2,1,1,7),_SnBgp4AddrFilterRowStatus_Type())
snBgp4AddrFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AddrFilterRowStatus.setStatus(_A)
_SnBgp4AggregateAddr_ObjectIdentity=ObjectIdentity
snBgp4AggregateAddr=_SnBgp4AggregateAddr_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,3))
_SnBgp4AggregateAddrTable_Object=MibTable
snBgp4AggregateAddrTable=_SnBgp4AggregateAddrTable_Object((1,3,6,1,4,1,1991,1,2,11,3,1))
if mibBuilder.loadTexts:snBgp4AggregateAddrTable.setStatus(_A)
_SnBgp4AggregateAddrEntry_Object=MibTableRow
snBgp4AggregateAddrEntry=_SnBgp4AggregateAddrEntry_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1))
snBgp4AggregateAddrEntry.setIndexNames((0,_F,_Z),(0,_F,_a),(0,_F,_b))
if mibBuilder.loadTexts:snBgp4AggregateAddrEntry.setStatus(_A)
_SnBgp4AggregateAddrIp_Type=IpAddress
_SnBgp4AggregateAddrIp_Object=MibTableColumn
snBgp4AggregateAddrIp=_SnBgp4AggregateAddrIp_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1,1),_SnBgp4AggregateAddrIp_Type())
snBgp4AggregateAddrIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AggregateAddrIp.setStatus(_A)
_SnBgp4AggregateAddrMask_Type=IpAddress
_SnBgp4AggregateAddrMask_Object=MibTableColumn
snBgp4AggregateAddrMask=_SnBgp4AggregateAddrMask_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1,2),_SnBgp4AggregateAddrMask_Type())
snBgp4AggregateAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AggregateAddrMask.setStatus(_A)
class _SnBgp4AggregateAddrOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('address',1),('asSet',2),('summaryOnly',3),('suppressMap',4),('advertiseMap',5),('attributeMap',6)))
_SnBgp4AggregateAddrOption_Type.__name__=_D
_SnBgp4AggregateAddrOption_Object=MibTableColumn
snBgp4AggregateAddrOption=_SnBgp4AggregateAddrOption_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1,3),_SnBgp4AggregateAddrOption_Type())
snBgp4AggregateAddrOption.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AggregateAddrOption.setStatus(_A)
class _SnBgp4AggregateAddrMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4AggregateAddrMap_Type.__name__=_E
_SnBgp4AggregateAddrMap_Object=MibTableColumn
snBgp4AggregateAddrMap=_SnBgp4AggregateAddrMap_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1,4),_SnBgp4AggregateAddrMap_Type())
snBgp4AggregateAddrMap.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AggregateAddrMap.setStatus(_A)
class _SnBgp4AggregateAddrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4AggregateAddrRowStatus_Type.__name__=_D
_SnBgp4AggregateAddrRowStatus_Object=MibTableColumn
snBgp4AggregateAddrRowStatus=_SnBgp4AggregateAddrRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,3,1,1,5),_SnBgp4AggregateAddrRowStatus_Type())
snBgp4AggregateAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AggregateAddrRowStatus.setStatus(_A)
_SnBgp4AsPathFilter_ObjectIdentity=ObjectIdentity
snBgp4AsPathFilter=_SnBgp4AsPathFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,4))
_SnBgp4AsPathFilterTable_Object=MibTable
snBgp4AsPathFilterTable=_SnBgp4AsPathFilterTable_Object((1,3,6,1,4,1,1991,1,2,11,4,1))
if mibBuilder.loadTexts:snBgp4AsPathFilterTable.setStatus(_A)
_SnBgp4AsPathFilterEntry_Object=MibTableRow
snBgp4AsPathFilterEntry=_SnBgp4AsPathFilterEntry_Object((1,3,6,1,4,1,1991,1,2,11,4,1,1))
snBgp4AsPathFilterEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:snBgp4AsPathFilterEntry.setStatus(_A)
_SnBgp4AsPathFilterIndex_Type=Integer32
_SnBgp4AsPathFilterIndex_Object=MibTableColumn
snBgp4AsPathFilterIndex=_SnBgp4AsPathFilterIndex_Object((1,3,6,1,4,1,1991,1,2,11,4,1,1,1),_SnBgp4AsPathFilterIndex_Type())
snBgp4AsPathFilterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AsPathFilterIndex.setStatus(_A)
class _SnBgp4AsPathFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_SnBgp4AsPathFilterAction_Type.__name__=_D
_SnBgp4AsPathFilterAction_Object=MibTableColumn
snBgp4AsPathFilterAction=_SnBgp4AsPathFilterAction_Object((1,3,6,1,4,1,1991,1,2,11,4,1,1,2),_SnBgp4AsPathFilterAction_Type())
snBgp4AsPathFilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AsPathFilterAction.setStatus(_A)
class _SnBgp4AsPathFilterRegExpression_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SnBgp4AsPathFilterRegExpression_Type.__name__=_E
_SnBgp4AsPathFilterRegExpression_Object=MibTableColumn
snBgp4AsPathFilterRegExpression=_SnBgp4AsPathFilterRegExpression_Object((1,3,6,1,4,1,1991,1,2,11,4,1,1,3),_SnBgp4AsPathFilterRegExpression_Type())
snBgp4AsPathFilterRegExpression.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AsPathFilterRegExpression.setStatus(_A)
class _SnBgp4AsPathFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4AsPathFilterRowStatus_Type.__name__=_D
_SnBgp4AsPathFilterRowStatus_Object=MibTableColumn
snBgp4AsPathFilterRowStatus=_SnBgp4AsPathFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,4,1,1,4),_SnBgp4AsPathFilterRowStatus_Type())
snBgp4AsPathFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4AsPathFilterRowStatus.setStatus(_A)
_SnBgp4CommunityFilter_ObjectIdentity=ObjectIdentity
snBgp4CommunityFilter=_SnBgp4CommunityFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,5))
_SnBgp4CommunityFilterTable_Object=MibTable
snBgp4CommunityFilterTable=_SnBgp4CommunityFilterTable_Object((1,3,6,1,4,1,1991,1,2,11,5,1))
if mibBuilder.loadTexts:snBgp4CommunityFilterTable.setStatus(_A)
_SnBgp4CommunityFilterEntry_Object=MibTableRow
snBgp4CommunityFilterEntry=_SnBgp4CommunityFilterEntry_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1))
snBgp4CommunityFilterEntry.setIndexNames((0,_F,_d))
if mibBuilder.loadTexts:snBgp4CommunityFilterEntry.setStatus(_A)
_SnBgp4CommunityFilterIndex_Type=Integer32
_SnBgp4CommunityFilterIndex_Object=MibTableColumn
snBgp4CommunityFilterIndex=_SnBgp4CommunityFilterIndex_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,1),_SnBgp4CommunityFilterIndex_Type())
snBgp4CommunityFilterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4CommunityFilterIndex.setStatus(_A)
class _SnBgp4CommunityFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_SnBgp4CommunityFilterAction_Type.__name__=_D
_SnBgp4CommunityFilterAction_Object=MibTableColumn
snBgp4CommunityFilterAction=_SnBgp4CommunityFilterAction_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,2),_SnBgp4CommunityFilterAction_Type())
snBgp4CommunityFilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterAction.setStatus(_A)
class _SnBgp4CommunityFilterCommNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SnBgp4CommunityFilterCommNum_Type.__name__=_E
_SnBgp4CommunityFilterCommNum_Object=MibTableColumn
snBgp4CommunityFilterCommNum=_SnBgp4CommunityFilterCommNum_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,3),_SnBgp4CommunityFilterCommNum_Type())
snBgp4CommunityFilterCommNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterCommNum.setStatus(_A)
class _SnBgp4CommunityFilterInternet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4CommunityFilterInternet_Type.__name__=_D
_SnBgp4CommunityFilterInternet_Object=MibTableColumn
snBgp4CommunityFilterInternet=_SnBgp4CommunityFilterInternet_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,4),_SnBgp4CommunityFilterInternet_Type())
snBgp4CommunityFilterInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterInternet.setStatus(_A)
class _SnBgp4CommunityFilterNoAdvertise_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_SnBgp4CommunityFilterNoAdvertise_Type.__name__=_D
_SnBgp4CommunityFilterNoAdvertise_Object=MibTableColumn
snBgp4CommunityFilterNoAdvertise=_SnBgp4CommunityFilterNoAdvertise_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,5),_SnBgp4CommunityFilterNoAdvertise_Type())
snBgp4CommunityFilterNoAdvertise.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterNoAdvertise.setStatus(_A)
class _SnBgp4CommunityFilterNoExport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_SnBgp4CommunityFilterNoExport_Type.__name__=_D
_SnBgp4CommunityFilterNoExport_Object=MibTableColumn
snBgp4CommunityFilterNoExport=_SnBgp4CommunityFilterNoExport_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,6),_SnBgp4CommunityFilterNoExport_Type())
snBgp4CommunityFilterNoExport.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterNoExport.setStatus(_A)
class _SnBgp4CommunityFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4CommunityFilterRowStatus_Type.__name__=_D
_SnBgp4CommunityFilterRowStatus_Object=MibTableColumn
snBgp4CommunityFilterRowStatus=_SnBgp4CommunityFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,7),_SnBgp4CommunityFilterRowStatus_Type())
snBgp4CommunityFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterRowStatus.setStatus(_A)
class _SnBgp4CommunityFilterLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_SnBgp4CommunityFilterLocalAs_Type.__name__=_D
_SnBgp4CommunityFilterLocalAs_Object=MibTableColumn
snBgp4CommunityFilterLocalAs=_SnBgp4CommunityFilterLocalAs_Object((1,3,6,1,4,1,1991,1,2,11,5,1,1,8),_SnBgp4CommunityFilterLocalAs_Type())
snBgp4CommunityFilterLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4CommunityFilterLocalAs.setStatus(_A)
_SnBgp4NeighGenCfg_ObjectIdentity=ObjectIdentity
snBgp4NeighGenCfg=_SnBgp4NeighGenCfg_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,6))
_SnBgp4NeighGenCfgTable_Object=MibTable
snBgp4NeighGenCfgTable=_SnBgp4NeighGenCfgTable_Object((1,3,6,1,4,1,1991,1,2,11,6,1))
if mibBuilder.loadTexts:snBgp4NeighGenCfgTable.setStatus(_A)
_SnBgp4NeighGenCfgEntry_Object=MibTableRow
snBgp4NeighGenCfgEntry=_SnBgp4NeighGenCfgEntry_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1))
snBgp4NeighGenCfgEntry.setIndexNames((0,_F,_e))
if mibBuilder.loadTexts:snBgp4NeighGenCfgEntry.setStatus(_A)
_SnBgp4NeighGenCfgNeighIp_Type=IpAddress
_SnBgp4NeighGenCfgNeighIp_Object=MibTableColumn
snBgp4NeighGenCfgNeighIp=_SnBgp4NeighGenCfgNeighIp_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,1),_SnBgp4NeighGenCfgNeighIp_Type())
snBgp4NeighGenCfgNeighIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighGenCfgNeighIp.setStatus(_A)
class _SnBgp4NeighGenCfgAdvertlevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_SnBgp4NeighGenCfgAdvertlevel_Type.__name__=_D
_SnBgp4NeighGenCfgAdvertlevel_Object=MibTableColumn
snBgp4NeighGenCfgAdvertlevel=_SnBgp4NeighGenCfgAdvertlevel_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,2),_SnBgp4NeighGenCfgAdvertlevel_Type())
snBgp4NeighGenCfgAdvertlevel.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgAdvertlevel.setStatus(_A)
class _SnBgp4NeighGenCfgDefOriginate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgDefOriginate_Type.__name__=_D
_SnBgp4NeighGenCfgDefOriginate_Object=MibTableColumn
snBgp4NeighGenCfgDefOriginate=_SnBgp4NeighGenCfgDefOriginate_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,3),_SnBgp4NeighGenCfgDefOriginate_Type())
snBgp4NeighGenCfgDefOriginate.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgDefOriginate.setStatus(_A)
class _SnBgp4NeighGenCfgEbgpMultihop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgEbgpMultihop_Type.__name__=_D
_SnBgp4NeighGenCfgEbgpMultihop_Object=MibTableColumn
snBgp4NeighGenCfgEbgpMultihop=_SnBgp4NeighGenCfgEbgpMultihop_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,4),_SnBgp4NeighGenCfgEbgpMultihop_Type())
snBgp4NeighGenCfgEbgpMultihop.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgEbgpMultihop.setStatus(_A)
_SnBgp4NeighGenCfgMaxPrefix_Type=Integer32
_SnBgp4NeighGenCfgMaxPrefix_Object=MibTableColumn
snBgp4NeighGenCfgMaxPrefix=_SnBgp4NeighGenCfgMaxPrefix_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,5),_SnBgp4NeighGenCfgMaxPrefix_Type())
snBgp4NeighGenCfgMaxPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgMaxPrefix.setStatus(_A)
class _SnBgp4NeighGenCfgNextHopSelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgNextHopSelf_Type.__name__=_D
_SnBgp4NeighGenCfgNextHopSelf_Object=MibTableColumn
snBgp4NeighGenCfgNextHopSelf=_SnBgp4NeighGenCfgNextHopSelf_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,6),_SnBgp4NeighGenCfgNextHopSelf_Type())
snBgp4NeighGenCfgNextHopSelf.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgNextHopSelf.setStatus(_A)
class _SnBgp4NeighGenCfgRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnBgp4NeighGenCfgRemoteAs_Type.__name__=_D
_SnBgp4NeighGenCfgRemoteAs_Object=MibTableColumn
snBgp4NeighGenCfgRemoteAs=_SnBgp4NeighGenCfgRemoteAs_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,7),_SnBgp4NeighGenCfgRemoteAs_Type())
snBgp4NeighGenCfgRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgRemoteAs.setStatus(_A)
class _SnBgp4NeighGenCfgSendComm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgSendComm_Type.__name__=_D
_SnBgp4NeighGenCfgSendComm_Object=MibTableColumn
snBgp4NeighGenCfgSendComm=_SnBgp4NeighGenCfgSendComm_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,8),_SnBgp4NeighGenCfgSendComm_Type())
snBgp4NeighGenCfgSendComm.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgSendComm.setStatus(_A)
class _SnBgp4NeighGenCfgWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4NeighGenCfgWeight_Type.__name__=_D
_SnBgp4NeighGenCfgWeight_Object=MibTableColumn
snBgp4NeighGenCfgWeight=_SnBgp4NeighGenCfgWeight_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,9),_SnBgp4NeighGenCfgWeight_Type())
snBgp4NeighGenCfgWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgWeight.setStatus(_A)
class _SnBgp4NeighGenCfgWeightFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighGenCfgWeightFilterList_Type.__name__=_E
_SnBgp4NeighGenCfgWeightFilterList_Object=MibTableColumn
snBgp4NeighGenCfgWeightFilterList=_SnBgp4NeighGenCfgWeightFilterList_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,10),_SnBgp4NeighGenCfgWeightFilterList_Type())
snBgp4NeighGenCfgWeightFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgWeightFilterList.setStatus(_A)
class _SnBgp4NeighGenCfgRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5),('applyDefault',6)))
_SnBgp4NeighGenCfgRowStatus_Type.__name__=_D
_SnBgp4NeighGenCfgRowStatus_Object=MibTableColumn
snBgp4NeighGenCfgRowStatus=_SnBgp4NeighGenCfgRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,11),_SnBgp4NeighGenCfgRowStatus_Type())
snBgp4NeighGenCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgRowStatus.setStatus(_A)
class _SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type.__name__=_D
_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Object=MibTableColumn
snBgp4NeighGenCfgUpdateSrcLpbIntf=_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,12),_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type())
snBgp4NeighGenCfgUpdateSrcLpbIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgUpdateSrcLpbIntf.setStatus(_A)
class _SnBgp4NeighGenCfgRouteRefClient_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgRouteRefClient_Type.__name__=_D
_SnBgp4NeighGenCfgRouteRefClient_Object=MibTableColumn
snBgp4NeighGenCfgRouteRefClient=_SnBgp4NeighGenCfgRouteRefClient_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,13),_SnBgp4NeighGenCfgRouteRefClient_Type())
snBgp4NeighGenCfgRouteRefClient.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgRouteRefClient.setStatus(_A)
class _SnBgp4NeighGenCfgRemovePrivateAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgRemovePrivateAs_Type.__name__=_D
_SnBgp4NeighGenCfgRemovePrivateAs_Object=MibTableColumn
snBgp4NeighGenCfgRemovePrivateAs=_SnBgp4NeighGenCfgRemovePrivateAs_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,14),_SnBgp4NeighGenCfgRemovePrivateAs_Type())
snBgp4NeighGenCfgRemovePrivateAs.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgRemovePrivateAs.setStatus(_A)
class _SnBgp4NeighGenCfgEbgpMultihopTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnBgp4NeighGenCfgEbgpMultihopTtl_Type.__name__=_D
_SnBgp4NeighGenCfgEbgpMultihopTtl_Object=MibTableColumn
snBgp4NeighGenCfgEbgpMultihopTtl=_SnBgp4NeighGenCfgEbgpMultihopTtl_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,15),_SnBgp4NeighGenCfgEbgpMultihopTtl_Type())
snBgp4NeighGenCfgEbgpMultihopTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgEbgpMultihopTtl.setStatus(_A)
class _SnBgp4NeighGenCfgShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NeighGenCfgShutdown_Type.__name__=_D
_SnBgp4NeighGenCfgShutdown_Object=MibTableColumn
snBgp4NeighGenCfgShutdown=_SnBgp4NeighGenCfgShutdown_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,16),_SnBgp4NeighGenCfgShutdown_Type())
snBgp4NeighGenCfgShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgShutdown.setStatus(_A)
class _SnBgp4NeighGenCfgKeepAliveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4NeighGenCfgKeepAliveTime_Type.__name__=_D
_SnBgp4NeighGenCfgKeepAliveTime_Object=MibTableColumn
snBgp4NeighGenCfgKeepAliveTime=_SnBgp4NeighGenCfgKeepAliveTime_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,17),_SnBgp4NeighGenCfgKeepAliveTime_Type())
snBgp4NeighGenCfgKeepAliveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgKeepAliveTime.setStatus(_A)
class _SnBgp4NeighGenCfgHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4NeighGenCfgHoldTime_Type.__name__=_D
_SnBgp4NeighGenCfgHoldTime_Object=MibTableColumn
snBgp4NeighGenCfgHoldTime=_SnBgp4NeighGenCfgHoldTime_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,18),_SnBgp4NeighGenCfgHoldTime_Type())
snBgp4NeighGenCfgHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgHoldTime.setStatus(_A)
class _SnBgp4NeighGenCfgDefOrigMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighGenCfgDefOrigMap_Type.__name__=_E
_SnBgp4NeighGenCfgDefOrigMap_Object=MibTableColumn
snBgp4NeighGenCfgDefOrigMap=_SnBgp4NeighGenCfgDefOrigMap_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,19),_SnBgp4NeighGenCfgDefOrigMap_Type())
snBgp4NeighGenCfgDefOrigMap.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgDefOrigMap.setStatus(_A)
class _SnBgp4NeighGenCfgDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SnBgp4NeighGenCfgDesc_Type.__name__=_E
_SnBgp4NeighGenCfgDesc_Object=MibTableColumn
snBgp4NeighGenCfgDesc=_SnBgp4NeighGenCfgDesc_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,20),_SnBgp4NeighGenCfgDesc_Type())
snBgp4NeighGenCfgDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgDesc.setStatus(_A)
class _SnBgp4NeighGenCfgPass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SnBgp4NeighGenCfgPass_Type.__name__=_E
_SnBgp4NeighGenCfgPass_Object=MibTableColumn
snBgp4NeighGenCfgPass=_SnBgp4NeighGenCfgPass_Object((1,3,6,1,4,1,1991,1,2,11,6,1,1,21),_SnBgp4NeighGenCfgPass_Type())
snBgp4NeighGenCfgPass.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighGenCfgPass.setStatus(_A)
_SnBgp4NeighDistGroup_ObjectIdentity=ObjectIdentity
snBgp4NeighDistGroup=_SnBgp4NeighDistGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,7))
_SnBgp4NeighDistGroupTable_Object=MibTable
snBgp4NeighDistGroupTable=_SnBgp4NeighDistGroupTable_Object((1,3,6,1,4,1,1991,1,2,11,7,1))
if mibBuilder.loadTexts:snBgp4NeighDistGroupTable.setStatus(_A)
_SnBgp4NeighDistGroupEntry_Object=MibTableRow
snBgp4NeighDistGroupEntry=_SnBgp4NeighDistGroupEntry_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1))
snBgp4NeighDistGroupEntry.setIndexNames((0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:snBgp4NeighDistGroupEntry.setStatus(_A)
_SnBgp4NeighDistGroupNeighIp_Type=IpAddress
_SnBgp4NeighDistGroupNeighIp_Object=MibTableColumn
snBgp4NeighDistGroupNeighIp=_SnBgp4NeighDistGroupNeighIp_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,1),_SnBgp4NeighDistGroupNeighIp_Type())
snBgp4NeighDistGroupNeighIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighDistGroupNeighIp.setStatus(_A)
class _SnBgp4NeighDistGroupDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_SnBgp4NeighDistGroupDir_Type.__name__=_D
_SnBgp4NeighDistGroupDir_Object=MibTableColumn
snBgp4NeighDistGroupDir=_SnBgp4NeighDistGroupDir_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,2),_SnBgp4NeighDistGroupDir_Type())
snBgp4NeighDistGroupDir.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighDistGroupDir.setStatus(_A)
class _SnBgp4NeighDistGroupAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighDistGroupAccessList_Type.__name__=_E
_SnBgp4NeighDistGroupAccessList_Object=MibTableColumn
snBgp4NeighDistGroupAccessList=_SnBgp4NeighDistGroupAccessList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,3),_SnBgp4NeighDistGroupAccessList_Type())
snBgp4NeighDistGroupAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupAccessList.setStatus(_A)
class _SnBgp4NeighDistGroupRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4NeighDistGroupRowStatus_Type.__name__=_D
_SnBgp4NeighDistGroupRowStatus_Object=MibTableColumn
snBgp4NeighDistGroupRowStatus=_SnBgp4NeighDistGroupRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,4),_SnBgp4NeighDistGroupRowStatus_Type())
snBgp4NeighDistGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupRowStatus.setStatus(_A)
class _SnBgp4NeighDistGroupInFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighDistGroupInFilterList_Type.__name__=_E
_SnBgp4NeighDistGroupInFilterList_Object=MibTableColumn
snBgp4NeighDistGroupInFilterList=_SnBgp4NeighDistGroupInFilterList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,5),_SnBgp4NeighDistGroupInFilterList_Type())
snBgp4NeighDistGroupInFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupInFilterList.setStatus(_A)
class _SnBgp4NeighDistGroupOutFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighDistGroupOutFilterList_Type.__name__=_E
_SnBgp4NeighDistGroupOutFilterList_Object=MibTableColumn
snBgp4NeighDistGroupOutFilterList=_SnBgp4NeighDistGroupOutFilterList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,6),_SnBgp4NeighDistGroupOutFilterList_Type())
snBgp4NeighDistGroupOutFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupOutFilterList.setStatus(_A)
class _SnBgp4NeighDistGroupInIpAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SnBgp4NeighDistGroupInIpAccessList_Type.__name__=_E
_SnBgp4NeighDistGroupInIpAccessList_Object=MibTableColumn
snBgp4NeighDistGroupInIpAccessList=_SnBgp4NeighDistGroupInIpAccessList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,7),_SnBgp4NeighDistGroupInIpAccessList_Type())
snBgp4NeighDistGroupInIpAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupInIpAccessList.setStatus(_A)
class _SnBgp4NeighDistGroupOutIpAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SnBgp4NeighDistGroupOutIpAccessList_Type.__name__=_E
_SnBgp4NeighDistGroupOutIpAccessList_Object=MibTableColumn
snBgp4NeighDistGroupOutIpAccessList=_SnBgp4NeighDistGroupOutIpAccessList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,8),_SnBgp4NeighDistGroupOutIpAccessList_Type())
snBgp4NeighDistGroupOutIpAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupOutIpAccessList.setStatus(_A)
class _SnBgp4NeighDistGroupInPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighDistGroupInPrefixList_Type.__name__=_E
_SnBgp4NeighDistGroupInPrefixList_Object=MibTableColumn
snBgp4NeighDistGroupInPrefixList=_SnBgp4NeighDistGroupInPrefixList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,9),_SnBgp4NeighDistGroupInPrefixList_Type())
snBgp4NeighDistGroupInPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupInPrefixList.setStatus(_A)
class _SnBgp4NeighDistGroupOutPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighDistGroupOutPrefixList_Type.__name__=_E
_SnBgp4NeighDistGroupOutPrefixList_Object=MibTableColumn
snBgp4NeighDistGroupOutPrefixList=_SnBgp4NeighDistGroupOutPrefixList_Object((1,3,6,1,4,1,1991,1,2,11,7,1,1,10),_SnBgp4NeighDistGroupOutPrefixList_Type())
snBgp4NeighDistGroupOutPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighDistGroupOutPrefixList.setStatus(_A)
_SnBgp4NeighFilterGroup_ObjectIdentity=ObjectIdentity
snBgp4NeighFilterGroup=_SnBgp4NeighFilterGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,8))
_SnBgp4NeighFilterGroupTable_Object=MibTable
snBgp4NeighFilterGroupTable=_SnBgp4NeighFilterGroupTable_Object((1,3,6,1,4,1,1991,1,2,11,8,1))
if mibBuilder.loadTexts:snBgp4NeighFilterGroupTable.setStatus(_A)
_SnBgp4NeighFilterGroupEntry_Object=MibTableRow
snBgp4NeighFilterGroupEntry=_SnBgp4NeighFilterGroupEntry_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1))
snBgp4NeighFilterGroupEntry.setIndexNames((0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:snBgp4NeighFilterGroupEntry.setStatus(_A)
_SnBgp4NeighFilterGroupNeighIp_Type=IpAddress
_SnBgp4NeighFilterGroupNeighIp_Object=MibTableColumn
snBgp4NeighFilterGroupNeighIp=_SnBgp4NeighFilterGroupNeighIp_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,1),_SnBgp4NeighFilterGroupNeighIp_Type())
snBgp4NeighFilterGroupNeighIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupNeighIp.setStatus(_A)
class _SnBgp4NeighFilterGroupDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_SnBgp4NeighFilterGroupDir_Type.__name__=_D
_SnBgp4NeighFilterGroupDir_Object=MibTableColumn
snBgp4NeighFilterGroupDir=_SnBgp4NeighFilterGroupDir_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,2),_SnBgp4NeighFilterGroupDir_Type())
snBgp4NeighFilterGroupDir.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupDir.setStatus(_A)
class _SnBgp4NeighFilterGroupAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighFilterGroupAccessList_Type.__name__=_E
_SnBgp4NeighFilterGroupAccessList_Object=MibTableColumn
snBgp4NeighFilterGroupAccessList=_SnBgp4NeighFilterGroupAccessList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,3),_SnBgp4NeighFilterGroupAccessList_Type())
snBgp4NeighFilterGroupAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupAccessList.setStatus(_A)
class _SnBgp4NeighFilterGroupRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4NeighFilterGroupRowStatus_Type.__name__=_D
_SnBgp4NeighFilterGroupRowStatus_Object=MibTableColumn
snBgp4NeighFilterGroupRowStatus=_SnBgp4NeighFilterGroupRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,4),_SnBgp4NeighFilterGroupRowStatus_Type())
snBgp4NeighFilterGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupRowStatus.setStatus(_A)
class _SnBgp4NeighFilterGroupInFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighFilterGroupInFilterList_Type.__name__=_E
_SnBgp4NeighFilterGroupInFilterList_Object=MibTableColumn
snBgp4NeighFilterGroupInFilterList=_SnBgp4NeighFilterGroupInFilterList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,5),_SnBgp4NeighFilterGroupInFilterList_Type())
snBgp4NeighFilterGroupInFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupInFilterList.setStatus(_A)
class _SnBgp4NeighFilterGroupOutFilterList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighFilterGroupOutFilterList_Type.__name__=_E
_SnBgp4NeighFilterGroupOutFilterList_Object=MibTableColumn
snBgp4NeighFilterGroupOutFilterList=_SnBgp4NeighFilterGroupOutFilterList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,6),_SnBgp4NeighFilterGroupOutFilterList_Type())
snBgp4NeighFilterGroupOutFilterList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupOutFilterList.setStatus(_A)
class _SnBgp4NeighFilterGroupInAsPathAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SnBgp4NeighFilterGroupInAsPathAccessList_Type.__name__=_E
_SnBgp4NeighFilterGroupInAsPathAccessList_Object=MibTableColumn
snBgp4NeighFilterGroupInAsPathAccessList=_SnBgp4NeighFilterGroupInAsPathAccessList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,7),_SnBgp4NeighFilterGroupInAsPathAccessList_Type())
snBgp4NeighFilterGroupInAsPathAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupInAsPathAccessList.setStatus(_A)
class _SnBgp4NeighFilterGroupOutAsPathAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SnBgp4NeighFilterGroupOutAsPathAccessList_Type.__name__=_E
_SnBgp4NeighFilterGroupOutAsPathAccessList_Object=MibTableColumn
snBgp4NeighFilterGroupOutAsPathAccessList=_SnBgp4NeighFilterGroupOutAsPathAccessList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,8),_SnBgp4NeighFilterGroupOutAsPathAccessList_Type())
snBgp4NeighFilterGroupOutAsPathAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupOutAsPathAccessList.setStatus(_A)
class _SnBgp4NeighFilterGroupWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4NeighFilterGroupWeight_Type.__name__=_D
_SnBgp4NeighFilterGroupWeight_Object=MibTableColumn
snBgp4NeighFilterGroupWeight=_SnBgp4NeighFilterGroupWeight_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,9),_SnBgp4NeighFilterGroupWeight_Type())
snBgp4NeighFilterGroupWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupWeight.setStatus(_A)
class _SnBgp4NeighFilterGroupWeightAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_SnBgp4NeighFilterGroupWeightAccessList_Type.__name__=_E
_SnBgp4NeighFilterGroupWeightAccessList_Object=MibTableColumn
snBgp4NeighFilterGroupWeightAccessList=_SnBgp4NeighFilterGroupWeightAccessList_Object((1,3,6,1,4,1,1991,1,2,11,8,1,1,10),_SnBgp4NeighFilterGroupWeightAccessList_Type())
snBgp4NeighFilterGroupWeightAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighFilterGroupWeightAccessList.setStatus(_A)
_SnBgp4NeighRouteMap_ObjectIdentity=ObjectIdentity
snBgp4NeighRouteMap=_SnBgp4NeighRouteMap_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,9))
_SnBgp4NeighRouteMapTable_Object=MibTable
snBgp4NeighRouteMapTable=_SnBgp4NeighRouteMapTable_Object((1,3,6,1,4,1,1991,1,2,11,9,1))
if mibBuilder.loadTexts:snBgp4NeighRouteMapTable.setStatus(_A)
_SnBgp4NeighRouteMapEntry_Object=MibTableRow
snBgp4NeighRouteMapEntry=_SnBgp4NeighRouteMapEntry_Object((1,3,6,1,4,1,1991,1,2,11,9,1,1))
snBgp4NeighRouteMapEntry.setIndexNames((0,_F,_j),(0,_F,_k))
if mibBuilder.loadTexts:snBgp4NeighRouteMapEntry.setStatus(_A)
_SnBgp4NeighRouteMapNeighIp_Type=IpAddress
_SnBgp4NeighRouteMapNeighIp_Object=MibTableColumn
snBgp4NeighRouteMapNeighIp=_SnBgp4NeighRouteMapNeighIp_Object((1,3,6,1,4,1,1991,1,2,11,9,1,1,1),_SnBgp4NeighRouteMapNeighIp_Type())
snBgp4NeighRouteMapNeighIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighRouteMapNeighIp.setStatus(_A)
class _SnBgp4NeighRouteMapDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_SnBgp4NeighRouteMapDir_Type.__name__=_D
_SnBgp4NeighRouteMapDir_Object=MibTableColumn
snBgp4NeighRouteMapDir=_SnBgp4NeighRouteMapDir_Object((1,3,6,1,4,1,1991,1,2,11,9,1,1,2),_SnBgp4NeighRouteMapDir_Type())
snBgp4NeighRouteMapDir.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighRouteMapDir.setStatus(_A)
class _SnBgp4NeighRouteMapMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighRouteMapMapName_Type.__name__=_E
_SnBgp4NeighRouteMapMapName_Object=MibTableColumn
snBgp4NeighRouteMapMapName=_SnBgp4NeighRouteMapMapName_Object((1,3,6,1,4,1,1991,1,2,11,9,1,1,3),_SnBgp4NeighRouteMapMapName_Type())
snBgp4NeighRouteMapMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighRouteMapMapName.setStatus(_A)
class _SnBgp4NeighRouteMapRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4NeighRouteMapRowStatus_Type.__name__=_D
_SnBgp4NeighRouteMapRowStatus_Object=MibTableColumn
snBgp4NeighRouteMapRowStatus=_SnBgp4NeighRouteMapRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,9,1,1,4),_SnBgp4NeighRouteMapRowStatus_Type())
snBgp4NeighRouteMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighRouteMapRowStatus.setStatus(_A)
_SnBgp4Network_ObjectIdentity=ObjectIdentity
snBgp4Network=_SnBgp4Network_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,10))
_SnBgp4NetworkTable_Object=MibTable
snBgp4NetworkTable=_SnBgp4NetworkTable_Object((1,3,6,1,4,1,1991,1,2,11,10,1))
if mibBuilder.loadTexts:snBgp4NetworkTable.setStatus(_A)
_SnBgp4NetworkEntry_Object=MibTableRow
snBgp4NetworkEntry=_SnBgp4NetworkEntry_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1))
snBgp4NetworkEntry.setIndexNames((0,_F,_l),(0,_F,_m))
if mibBuilder.loadTexts:snBgp4NetworkEntry.setStatus(_A)
_SnBgp4NetworkIp_Type=IpAddress
_SnBgp4NetworkIp_Object=MibTableColumn
snBgp4NetworkIp=_SnBgp4NetworkIp_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1,1),_SnBgp4NetworkIp_Type())
snBgp4NetworkIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NetworkIp.setStatus(_A)
_SnBgp4NetworkSubnetMask_Type=IpAddress
_SnBgp4NetworkSubnetMask_Object=MibTableColumn
snBgp4NetworkSubnetMask=_SnBgp4NetworkSubnetMask_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1,2),_SnBgp4NetworkSubnetMask_Type())
snBgp4NetworkSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NetworkSubnetMask.setStatus(_A)
class _SnBgp4NetworkWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4NetworkWeight_Type.__name__=_D
_SnBgp4NetworkWeight_Object=MibTableColumn
snBgp4NetworkWeight=_SnBgp4NetworkWeight_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1,3),_SnBgp4NetworkWeight_Type())
snBgp4NetworkWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NetworkWeight.setStatus(_A)
class _SnBgp4NetworkBackdoor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4NetworkBackdoor_Type.__name__=_D
_SnBgp4NetworkBackdoor_Object=MibTableColumn
snBgp4NetworkBackdoor=_SnBgp4NetworkBackdoor_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1,4),_SnBgp4NetworkBackdoor_Type())
snBgp4NetworkBackdoor.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NetworkBackdoor.setStatus(_A)
class _SnBgp4NetworkRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4NetworkRowStatus_Type.__name__=_D
_SnBgp4NetworkRowStatus_Object=MibTableColumn
snBgp4NetworkRowStatus=_SnBgp4NetworkRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,10,1,1,5),_SnBgp4NetworkRowStatus_Type())
snBgp4NetworkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NetworkRowStatus.setStatus(_A)
_SnBgp4Redis_ObjectIdentity=ObjectIdentity
snBgp4Redis=_SnBgp4Redis_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,11))
_SnBgp4RedisTable_Object=MibTable
snBgp4RedisTable=_SnBgp4RedisTable_Object((1,3,6,1,4,1,1991,1,2,11,11,1))
if mibBuilder.loadTexts:snBgp4RedisTable.setStatus(_A)
_SnBgp4RedisEntry_Object=MibTableRow
snBgp4RedisEntry=_SnBgp4RedisEntry_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1))
snBgp4RedisEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:snBgp4RedisEntry.setStatus(_A)
class _SnBgp4RedisProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rip',1),('ospf',2),('static',3),('connected',4),('isis',5)))
_SnBgp4RedisProtocol_Type.__name__=_D
_SnBgp4RedisProtocol_Object=MibTableColumn
snBgp4RedisProtocol=_SnBgp4RedisProtocol_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,1),_SnBgp4RedisProtocol_Type())
snBgp4RedisProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RedisProtocol.setStatus(_A)
_SnBgp4RedisMetric_Type=Integer32
_SnBgp4RedisMetric_Object=MibTableColumn
snBgp4RedisMetric=_SnBgp4RedisMetric_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,2),_SnBgp4RedisMetric_Type())
snBgp4RedisMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisMetric.setStatus(_A)
class _SnBgp4RedisRouteMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RedisRouteMap_Type.__name__=_E
_SnBgp4RedisRouteMap_Object=MibTableColumn
snBgp4RedisRouteMap=_SnBgp4RedisRouteMap_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,3),_SnBgp4RedisRouteMap_Type())
snBgp4RedisRouteMap.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisRouteMap.setStatus(_A)
class _SnBgp4RedisWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4RedisWeight_Type.__name__=_D
_SnBgp4RedisWeight_Object=MibTableColumn
snBgp4RedisWeight=_SnBgp4RedisWeight_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,4),_SnBgp4RedisWeight_Type())
snBgp4RedisWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisWeight.setStatus(_A)
class _SnBgp4RedisMatchInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4RedisMatchInternal_Type.__name__=_D
_SnBgp4RedisMatchInternal_Object=MibTableColumn
snBgp4RedisMatchInternal=_SnBgp4RedisMatchInternal_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,5),_SnBgp4RedisMatchInternal_Type())
snBgp4RedisMatchInternal.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisMatchInternal.setStatus(_A)
class _SnBgp4RedisMatchExternal1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4RedisMatchExternal1_Type.__name__=_D
_SnBgp4RedisMatchExternal1_Object=MibTableColumn
snBgp4RedisMatchExternal1=_SnBgp4RedisMatchExternal1_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,6),_SnBgp4RedisMatchExternal1_Type())
snBgp4RedisMatchExternal1.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisMatchExternal1.setStatus(_A)
class _SnBgp4RedisMatchExternal2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4RedisMatchExternal2_Type.__name__=_D
_SnBgp4RedisMatchExternal2_Object=MibTableColumn
snBgp4RedisMatchExternal2=_SnBgp4RedisMatchExternal2_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,7),_SnBgp4RedisMatchExternal2_Type())
snBgp4RedisMatchExternal2.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisMatchExternal2.setStatus(_A)
class _SnBgp4RedisRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4RedisRowStatus_Type.__name__=_D
_SnBgp4RedisRowStatus_Object=MibTableColumn
snBgp4RedisRowStatus=_SnBgp4RedisRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,11,1,1,8),_SnBgp4RedisRowStatus_Type())
snBgp4RedisRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RedisRowStatus.setStatus(_A)
_SnBgp4RouteMapFilter_ObjectIdentity=ObjectIdentity
snBgp4RouteMapFilter=_SnBgp4RouteMapFilter_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,12))
_SnBgp4RouteMapFilterTable_Object=MibTable
snBgp4RouteMapFilterTable=_SnBgp4RouteMapFilterTable_Object((1,3,6,1,4,1,1991,1,2,11,12,1))
if mibBuilder.loadTexts:snBgp4RouteMapFilterTable.setStatus(_A)
_SnBgp4RouteMapFilterEntry_Object=MibTableRow
snBgp4RouteMapFilterEntry=_SnBgp4RouteMapFilterEntry_Object((1,3,6,1,4,1,1991,1,2,11,12,1,1))
snBgp4RouteMapFilterEntry.setIndexNames((0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:snBgp4RouteMapFilterEntry.setStatus(_A)
class _SnBgp4RouteMapFilterMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapFilterMapName_Type.__name__=_E
_SnBgp4RouteMapFilterMapName_Object=MibTableColumn
snBgp4RouteMapFilterMapName=_SnBgp4RouteMapFilterMapName_Object((1,3,6,1,4,1,1991,1,2,11,12,1,1,1),_SnBgp4RouteMapFilterMapName_Type())
snBgp4RouteMapFilterMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapFilterMapName.setStatus(_A)
_SnBgp4RouteMapFilterSequenceNum_Type=Integer32
_SnBgp4RouteMapFilterSequenceNum_Object=MibTableColumn
snBgp4RouteMapFilterSequenceNum=_SnBgp4RouteMapFilterSequenceNum_Object((1,3,6,1,4,1,1991,1,2,11,12,1,1,2),_SnBgp4RouteMapFilterSequenceNum_Type())
snBgp4RouteMapFilterSequenceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapFilterSequenceNum.setStatus(_A)
class _SnBgp4RouteMapFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_SnBgp4RouteMapFilterAction_Type.__name__=_D
_SnBgp4RouteMapFilterAction_Object=MibTableColumn
snBgp4RouteMapFilterAction=_SnBgp4RouteMapFilterAction_Object((1,3,6,1,4,1,1991,1,2,11,12,1,1,3),_SnBgp4RouteMapFilterAction_Type())
snBgp4RouteMapFilterAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapFilterAction.setStatus(_A)
class _SnBgp4RouteMapFilterRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4RouteMapFilterRowStatus_Type.__name__=_D
_SnBgp4RouteMapFilterRowStatus_Object=MibTableColumn
snBgp4RouteMapFilterRowStatus=_SnBgp4RouteMapFilterRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,12,1,1,4),_SnBgp4RouteMapFilterRowStatus_Type())
snBgp4RouteMapFilterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapFilterRowStatus.setStatus(_A)
_SnBgp4RouteMapMatch_ObjectIdentity=ObjectIdentity
snBgp4RouteMapMatch=_SnBgp4RouteMapMatch_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,13))
_SnBgp4RouteMapMatchTable_Object=MibTable
snBgp4RouteMapMatchTable=_SnBgp4RouteMapMatchTable_Object((1,3,6,1,4,1,1991,1,2,11,13,1))
if mibBuilder.loadTexts:snBgp4RouteMapMatchTable.setStatus(_A)
_SnBgp4RouteMapMatchEntry_Object=MibTableRow
snBgp4RouteMapMatchEntry=_SnBgp4RouteMapMatchEntry_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1))
snBgp4RouteMapMatchEntry.setIndexNames((0,_F,_q),(0,_F,_r))
if mibBuilder.loadTexts:snBgp4RouteMapMatchEntry.setStatus(_A)
class _SnBgp4RouteMapMatchMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapMatchMapName_Type.__name__=_E
_SnBgp4RouteMapMatchMapName_Object=MibTableColumn
snBgp4RouteMapMatchMapName=_SnBgp4RouteMapMatchMapName_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,1),_SnBgp4RouteMapMatchMapName_Type())
snBgp4RouteMapMatchMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapMatchMapName.setStatus(_A)
_SnBgp4RouteMapMatchSequenceNum_Type=Integer32
_SnBgp4RouteMapMatchSequenceNum_Object=MibTableColumn
snBgp4RouteMapMatchSequenceNum=_SnBgp4RouteMapMatchSequenceNum_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,2),_SnBgp4RouteMapMatchSequenceNum_Type())
snBgp4RouteMapMatchSequenceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapMatchSequenceNum.setStatus(_A)
class _SnBgp4RouteMapMatchAsPathFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnBgp4RouteMapMatchAsPathFilter_Type.__name__=_E
_SnBgp4RouteMapMatchAsPathFilter_Object=MibTableColumn
snBgp4RouteMapMatchAsPathFilter=_SnBgp4RouteMapMatchAsPathFilter_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,3),_SnBgp4RouteMapMatchAsPathFilter_Type())
snBgp4RouteMapMatchAsPathFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchAsPathFilter.setStatus(_A)
class _SnBgp4RouteMapMatchCommunityFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnBgp4RouteMapMatchCommunityFilter_Type.__name__=_E
_SnBgp4RouteMapMatchCommunityFilter_Object=MibTableColumn
snBgp4RouteMapMatchCommunityFilter=_SnBgp4RouteMapMatchCommunityFilter_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,4),_SnBgp4RouteMapMatchCommunityFilter_Type())
snBgp4RouteMapMatchCommunityFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchCommunityFilter.setStatus(_A)
class _SnBgp4RouteMapMatchAddressFilter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnBgp4RouteMapMatchAddressFilter_Type.__name__=_E
_SnBgp4RouteMapMatchAddressFilter_Object=MibTableColumn
snBgp4RouteMapMatchAddressFilter=_SnBgp4RouteMapMatchAddressFilter_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,5),_SnBgp4RouteMapMatchAddressFilter_Type())
snBgp4RouteMapMatchAddressFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchAddressFilter.setStatus(_A)
_SnBgp4RouteMapMatchMetric_Type=Integer32
_SnBgp4RouteMapMatchMetric_Object=MibTableColumn
snBgp4RouteMapMatchMetric=_SnBgp4RouteMapMatchMetric_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,6),_SnBgp4RouteMapMatchMetric_Type())
snBgp4RouteMapMatchMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchMetric.setStatus(_A)
class _SnBgp4RouteMapMatchNextHopList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapMatchNextHopList_Type.__name__=_E
_SnBgp4RouteMapMatchNextHopList_Object=MibTableColumn
snBgp4RouteMapMatchNextHopList=_SnBgp4RouteMapMatchNextHopList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,7),_SnBgp4RouteMapMatchNextHopList_Type())
snBgp4RouteMapMatchNextHopList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchNextHopList.setStatus(_A)
class _SnBgp4RouteMapMatchRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_U,0),('external',1),('externalType1',2),('externalType2',3),('internal',4),('local',5)))
_SnBgp4RouteMapMatchRouteType_Type.__name__=_D
_SnBgp4RouteMapMatchRouteType_Object=MibTableColumn
snBgp4RouteMapMatchRouteType=_SnBgp4RouteMapMatchRouteType_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,8),_SnBgp4RouteMapMatchRouteType_Type())
snBgp4RouteMapMatchRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchRouteType.setStatus(_A)
class _SnBgp4RouteMapMatchTagList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapMatchTagList_Type.__name__=_E
_SnBgp4RouteMapMatchTagList_Object=MibTableColumn
snBgp4RouteMapMatchTagList=_SnBgp4RouteMapMatchTagList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,9),_SnBgp4RouteMapMatchTagList_Type())
snBgp4RouteMapMatchTagList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchTagList.setStatus(_A)
_SnBgp4RouteMapMatchRowMask_Type=Integer32
_SnBgp4RouteMapMatchRowMask_Object=MibTableColumn
snBgp4RouteMapMatchRowMask=_SnBgp4RouteMapMatchRowMask_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,10),_SnBgp4RouteMapMatchRowMask_Type())
snBgp4RouteMapMatchRowMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchRowMask.setStatus(_A)
class _SnBgp4RouteMapMatchAsPathAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnBgp4RouteMapMatchAsPathAccessList_Type.__name__=_E
_SnBgp4RouteMapMatchAsPathAccessList_Object=MibTableColumn
snBgp4RouteMapMatchAsPathAccessList=_SnBgp4RouteMapMatchAsPathAccessList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,11),_SnBgp4RouteMapMatchAsPathAccessList_Type())
snBgp4RouteMapMatchAsPathAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchAsPathAccessList.setStatus(_A)
class _SnBgp4RouteMapMatchCommunityList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnBgp4RouteMapMatchCommunityList_Type.__name__=_E
_SnBgp4RouteMapMatchCommunityList_Object=MibTableColumn
snBgp4RouteMapMatchCommunityList=_SnBgp4RouteMapMatchCommunityList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,12),_SnBgp4RouteMapMatchCommunityList_Type())
snBgp4RouteMapMatchCommunityList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchCommunityList.setStatus(_A)
class _SnBgp4RouteMapMatchAddressAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_SnBgp4RouteMapMatchAddressAccessList_Type.__name__=_E
_SnBgp4RouteMapMatchAddressAccessList_Object=MibTableColumn
snBgp4RouteMapMatchAddressAccessList=_SnBgp4RouteMapMatchAddressAccessList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,13),_SnBgp4RouteMapMatchAddressAccessList_Type())
snBgp4RouteMapMatchAddressAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchAddressAccessList.setStatus(_A)
class _SnBgp4RouteMapMatchAddressPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,170))
_SnBgp4RouteMapMatchAddressPrefixList_Type.__name__=_E
_SnBgp4RouteMapMatchAddressPrefixList_Object=MibTableColumn
snBgp4RouteMapMatchAddressPrefixList=_SnBgp4RouteMapMatchAddressPrefixList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,14),_SnBgp4RouteMapMatchAddressPrefixList_Type())
snBgp4RouteMapMatchAddressPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchAddressPrefixList.setStatus(_A)
class _SnBgp4RouteMapMatchNextHopAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_SnBgp4RouteMapMatchNextHopAccessList_Type.__name__=_E
_SnBgp4RouteMapMatchNextHopAccessList_Object=MibTableColumn
snBgp4RouteMapMatchNextHopAccessList=_SnBgp4RouteMapMatchNextHopAccessList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,15),_SnBgp4RouteMapMatchNextHopAccessList_Type())
snBgp4RouteMapMatchNextHopAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchNextHopAccessList.setStatus(_A)
class _SnBgp4RouteMapMatchNextHopPrefixList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,170))
_SnBgp4RouteMapMatchNextHopPrefixList_Type.__name__=_E
_SnBgp4RouteMapMatchNextHopPrefixList_Object=MibTableColumn
snBgp4RouteMapMatchNextHopPrefixList=_SnBgp4RouteMapMatchNextHopPrefixList_Object((1,3,6,1,4,1,1991,1,2,11,13,1,1,16),_SnBgp4RouteMapMatchNextHopPrefixList_Type())
snBgp4RouteMapMatchNextHopPrefixList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapMatchNextHopPrefixList.setStatus(_A)
_SnBgp4RouteMapSet_ObjectIdentity=ObjectIdentity
snBgp4RouteMapSet=_SnBgp4RouteMapSet_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,14))
_SnBgp4RouteMapSetTable_Object=MibTable
snBgp4RouteMapSetTable=_SnBgp4RouteMapSetTable_Object((1,3,6,1,4,1,1991,1,2,11,14,1))
if mibBuilder.loadTexts:snBgp4RouteMapSetTable.setStatus(_A)
_SnBgp4RouteMapSetEntry_Object=MibTableRow
snBgp4RouteMapSetEntry=_SnBgp4RouteMapSetEntry_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1))
snBgp4RouteMapSetEntry.setIndexNames((0,_F,_s),(0,_F,_t))
if mibBuilder.loadTexts:snBgp4RouteMapSetEntry.setStatus(_A)
class _SnBgp4RouteMapSetMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapSetMapName_Type.__name__=_E
_SnBgp4RouteMapSetMapName_Object=MibTableColumn
snBgp4RouteMapSetMapName=_SnBgp4RouteMapSetMapName_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,1),_SnBgp4RouteMapSetMapName_Type())
snBgp4RouteMapSetMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapSetMapName.setStatus(_A)
_SnBgp4RouteMapSetSequenceNum_Type=Integer32
_SnBgp4RouteMapSetSequenceNum_Object=MibTableColumn
snBgp4RouteMapSetSequenceNum=_SnBgp4RouteMapSetSequenceNum_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,2),_SnBgp4RouteMapSetSequenceNum_Type())
snBgp4RouteMapSetSequenceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteMapSetSequenceNum.setStatus(_A)
class _SnBgp4RouteMapSetAsPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tag',0),('prepend',1)))
_SnBgp4RouteMapSetAsPathType_Type.__name__=_D
_SnBgp4RouteMapSetAsPathType_Object=MibTableColumn
snBgp4RouteMapSetAsPathType=_SnBgp4RouteMapSetAsPathType_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,3),_SnBgp4RouteMapSetAsPathType_Type())
snBgp4RouteMapSetAsPathType.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetAsPathType.setStatus(_A)
class _SnBgp4RouteMapSetAsPathString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4RouteMapSetAsPathString_Type.__name__=_E
_SnBgp4RouteMapSetAsPathString_Object=MibTableColumn
snBgp4RouteMapSetAsPathString=_SnBgp4RouteMapSetAsPathString_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,4),_SnBgp4RouteMapSetAsPathString_Type())
snBgp4RouteMapSetAsPathString.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetAsPathString.setStatus(_A)
class _SnBgp4RouteMapSetAutoTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4RouteMapSetAutoTag_Type.__name__=_D
_SnBgp4RouteMapSetAutoTag_Object=MibTableColumn
snBgp4RouteMapSetAutoTag=_SnBgp4RouteMapSetAutoTag_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,5),_SnBgp4RouteMapSetAutoTag_Type())
snBgp4RouteMapSetAutoTag.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetAutoTag.setStatus(_A)
class _SnBgp4RouteMapSetCommunityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3)));namedValues=NamedValues(*(('nums',0),(_U,3)))
_SnBgp4RouteMapSetCommunityType_Type.__name__=_D
_SnBgp4RouteMapSetCommunityType_Object=MibTableColumn
snBgp4RouteMapSetCommunityType=_SnBgp4RouteMapSetCommunityType_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,6),_SnBgp4RouteMapSetCommunityType_Type())
snBgp4RouteMapSetCommunityType.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetCommunityType.setStatus(_A)
_SnBgp4RouteMapSetCommunityNum_Type=Integer32
_SnBgp4RouteMapSetCommunityNum_Object=MibTableColumn
snBgp4RouteMapSetCommunityNum=_SnBgp4RouteMapSetCommunityNum_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,7),_SnBgp4RouteMapSetCommunityNum_Type())
snBgp4RouteMapSetCommunityNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetCommunityNum.setStatus(_T)
class _SnBgp4RouteMapSetCommunityAdditive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnBgp4RouteMapSetCommunityAdditive_Type.__name__=_D
_SnBgp4RouteMapSetCommunityAdditive_Object=MibTableColumn
snBgp4RouteMapSetCommunityAdditive=_SnBgp4RouteMapSetCommunityAdditive_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,8),_SnBgp4RouteMapSetCommunityAdditive_Type())
snBgp4RouteMapSetCommunityAdditive.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetCommunityAdditive.setStatus(_A)
_SnBgp4RouteMapSetLocalPreference_Type=Integer32
_SnBgp4RouteMapSetLocalPreference_Object=MibTableColumn
snBgp4RouteMapSetLocalPreference=_SnBgp4RouteMapSetLocalPreference_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,9),_SnBgp4RouteMapSetLocalPreference_Type())
snBgp4RouteMapSetLocalPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetLocalPreference.setStatus(_A)
_SnBgp4RouteMapSetMetric_Type=Integer32
_SnBgp4RouteMapSetMetric_Object=MibTableColumn
snBgp4RouteMapSetMetric=_SnBgp4RouteMapSetMetric_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,10),_SnBgp4RouteMapSetMetric_Type())
snBgp4RouteMapSetMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetMetric.setStatus(_A)
_SnBgp4RouteMapSetNextHop_Type=IpAddress
_SnBgp4RouteMapSetNextHop_Object=MibTableColumn
snBgp4RouteMapSetNextHop=_SnBgp4RouteMapSetNextHop_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,11),_SnBgp4RouteMapSetNextHop_Type())
snBgp4RouteMapSetNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetNextHop.setStatus(_A)
class _SnBgp4RouteMapSetOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2)))
_SnBgp4RouteMapSetOrigin_Type.__name__=_D
_SnBgp4RouteMapSetOrigin_Object=MibTableColumn
snBgp4RouteMapSetOrigin=_SnBgp4RouteMapSetOrigin_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,12),_SnBgp4RouteMapSetOrigin_Type())
snBgp4RouteMapSetOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetOrigin.setStatus(_A)
_SnBgp4RouteMapSetTag_Type=Integer32
_SnBgp4RouteMapSetTag_Object=MibTableColumn
snBgp4RouteMapSetTag=_SnBgp4RouteMapSetTag_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,13),_SnBgp4RouteMapSetTag_Type())
snBgp4RouteMapSetTag.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetTag.setStatus(_A)
class _SnBgp4RouteMapSetWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnBgp4RouteMapSetWeight_Type.__name__=_D
_SnBgp4RouteMapSetWeight_Object=MibTableColumn
snBgp4RouteMapSetWeight=_SnBgp4RouteMapSetWeight_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,14),_SnBgp4RouteMapSetWeight_Type())
snBgp4RouteMapSetWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetWeight.setStatus(_A)
_SnBgp4RouteMapSetRowMask_Type=Integer32
_SnBgp4RouteMapSetRowMask_Object=MibTableColumn
snBgp4RouteMapSetRowMask=_SnBgp4RouteMapSetRowMask_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,15),_SnBgp4RouteMapSetRowMask_Type())
snBgp4RouteMapSetRowMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetRowMask.setStatus(_A)
class _SnBgp4RouteMapSetCommunityNums_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_SnBgp4RouteMapSetCommunityNums_Type.__name__=_E
_SnBgp4RouteMapSetCommunityNums_Object=MibTableColumn
snBgp4RouteMapSetCommunityNums=_SnBgp4RouteMapSetCommunityNums_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,16),_SnBgp4RouteMapSetCommunityNums_Type())
snBgp4RouteMapSetCommunityNums.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetCommunityNums.setStatus(_A)
class _SnBgp4RouteMapSetDampenHalfLife_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45))
_SnBgp4RouteMapSetDampenHalfLife_Type.__name__=_D
_SnBgp4RouteMapSetDampenHalfLife_Object=MibTableColumn
snBgp4RouteMapSetDampenHalfLife=_SnBgp4RouteMapSetDampenHalfLife_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,17),_SnBgp4RouteMapSetDampenHalfLife_Type())
snBgp4RouteMapSetDampenHalfLife.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetDampenHalfLife.setStatus(_A)
class _SnBgp4RouteMapSetDampenReuse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4RouteMapSetDampenReuse_Type.__name__=_D
_SnBgp4RouteMapSetDampenReuse_Object=MibTableColumn
snBgp4RouteMapSetDampenReuse=_SnBgp4RouteMapSetDampenReuse_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,18),_SnBgp4RouteMapSetDampenReuse_Type())
snBgp4RouteMapSetDampenReuse.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetDampenReuse.setStatus(_A)
class _SnBgp4RouteMapSetDampenSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4RouteMapSetDampenSuppress_Type.__name__=_D
_SnBgp4RouteMapSetDampenSuppress_Object=MibTableColumn
snBgp4RouteMapSetDampenSuppress=_SnBgp4RouteMapSetDampenSuppress_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,19),_SnBgp4RouteMapSetDampenSuppress_Type())
snBgp4RouteMapSetDampenSuppress.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetDampenSuppress.setStatus(_A)
class _SnBgp4RouteMapSetDampenMaxSuppress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_SnBgp4RouteMapSetDampenMaxSuppress_Type.__name__=_D
_SnBgp4RouteMapSetDampenMaxSuppress_Object=MibTableColumn
snBgp4RouteMapSetDampenMaxSuppress=_SnBgp4RouteMapSetDampenMaxSuppress_Object((1,3,6,1,4,1,1991,1,2,11,14,1,1,20),_SnBgp4RouteMapSetDampenMaxSuppress_Type())
snBgp4RouteMapSetDampenMaxSuppress.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4RouteMapSetDampenMaxSuppress.setStatus(_A)
_SnBgp4NeighOperStatus_ObjectIdentity=ObjectIdentity
snBgp4NeighOperStatus=_SnBgp4NeighOperStatus_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,15))
_SnBgp4NeighOperStatusTable_Object=MibTable
snBgp4NeighOperStatusTable=_SnBgp4NeighOperStatusTable_Object((1,3,6,1,4,1,1991,1,2,11,15,1))
if mibBuilder.loadTexts:snBgp4NeighOperStatusTable.setStatus(_A)
_SnBgp4NeighOperStatusEntry_Object=MibTableRow
snBgp4NeighOperStatusEntry=_SnBgp4NeighOperStatusEntry_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1))
snBgp4NeighOperStatusEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:snBgp4NeighOperStatusEntry.setStatus(_A)
_SnBgp4NeighOperStatusIndex_Type=Integer32
_SnBgp4NeighOperStatusIndex_Object=MibTableColumn
snBgp4NeighOperStatusIndex=_SnBgp4NeighOperStatusIndex_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,1),_SnBgp4NeighOperStatusIndex_Type())
snBgp4NeighOperStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusIndex.setStatus(_A)
_SnBgp4NeighOperStatusIp_Type=IpAddress
_SnBgp4NeighOperStatusIp_Object=MibTableColumn
snBgp4NeighOperStatusIp=_SnBgp4NeighOperStatusIp_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,2),_SnBgp4NeighOperStatusIp_Type())
snBgp4NeighOperStatusIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusIp.setStatus(_A)
_SnBgp4NeighOperStatusRemoteAs_Type=Integer32
_SnBgp4NeighOperStatusRemoteAs_Object=MibTableColumn
snBgp4NeighOperStatusRemoteAs=_SnBgp4NeighOperStatusRemoteAs_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,3),_SnBgp4NeighOperStatusRemoteAs_Type())
snBgp4NeighOperStatusRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusRemoteAs.setStatus(_A)
class _SnBgp4NeighOperStatusBgpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ebgp',0),('ibgp',1)))
_SnBgp4NeighOperStatusBgpType_Type.__name__=_D
_SnBgp4NeighOperStatusBgpType_Object=MibTableColumn
snBgp4NeighOperStatusBgpType=_SnBgp4NeighOperStatusBgpType_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,4),_SnBgp4NeighOperStatusBgpType_Type())
snBgp4NeighOperStatusBgpType.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusBgpType.setStatus(_A)
class _SnBgp4NeighOperStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_v,0),('idle',1),(_w,2),(_x,3),(_y,4),(_z,5),(_A0,6)))
_SnBgp4NeighOperStatusState_Type.__name__=_D
_SnBgp4NeighOperStatusState_Object=MibTableColumn
snBgp4NeighOperStatusState=_SnBgp4NeighOperStatusState_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,5),_SnBgp4NeighOperStatusState_Type())
snBgp4NeighOperStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusState.setStatus(_A)
_SnBgp4NeighOperStatusKeepAliveTime_Type=Integer32
_SnBgp4NeighOperStatusKeepAliveTime_Object=MibTableColumn
snBgp4NeighOperStatusKeepAliveTime=_SnBgp4NeighOperStatusKeepAliveTime_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,6),_SnBgp4NeighOperStatusKeepAliveTime_Type())
snBgp4NeighOperStatusKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusKeepAliveTime.setStatus(_A)
_SnBgp4NeighOperStatusHoldTime_Type=Integer32
_SnBgp4NeighOperStatusHoldTime_Object=MibTableColumn
snBgp4NeighOperStatusHoldTime=_SnBgp4NeighOperStatusHoldTime_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,7),_SnBgp4NeighOperStatusHoldTime_Type())
snBgp4NeighOperStatusHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusHoldTime.setStatus(_A)
_SnBgp4NeighOperStatusAdvertlevel_Type=Integer32
_SnBgp4NeighOperStatusAdvertlevel_Object=MibTableColumn
snBgp4NeighOperStatusAdvertlevel=_SnBgp4NeighOperStatusAdvertlevel_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,8),_SnBgp4NeighOperStatusAdvertlevel_Type())
snBgp4NeighOperStatusAdvertlevel.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusAdvertlevel.setStatus(_A)
_SnBgp4NeighOperStatusKeepAliveTxCounts_Type=Counter32
_SnBgp4NeighOperStatusKeepAliveTxCounts_Object=MibTableColumn
snBgp4NeighOperStatusKeepAliveTxCounts=_SnBgp4NeighOperStatusKeepAliveTxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,9),_SnBgp4NeighOperStatusKeepAliveTxCounts_Type())
snBgp4NeighOperStatusKeepAliveTxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusKeepAliveTxCounts.setStatus(_A)
_SnBgp4NeighOperStatusKeepAliveRxCounts_Type=Counter32
_SnBgp4NeighOperStatusKeepAliveRxCounts_Object=MibTableColumn
snBgp4NeighOperStatusKeepAliveRxCounts=_SnBgp4NeighOperStatusKeepAliveRxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,10),_SnBgp4NeighOperStatusKeepAliveRxCounts_Type())
snBgp4NeighOperStatusKeepAliveRxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusKeepAliveRxCounts.setStatus(_A)
_SnBgp4NeighOperStatusUpdateTxCounts_Type=Counter32
_SnBgp4NeighOperStatusUpdateTxCounts_Object=MibTableColumn
snBgp4NeighOperStatusUpdateTxCounts=_SnBgp4NeighOperStatusUpdateTxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,11),_SnBgp4NeighOperStatusUpdateTxCounts_Type())
snBgp4NeighOperStatusUpdateTxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusUpdateTxCounts.setStatus(_A)
_SnBgp4NeighOperStatusUpdateRxCounts_Type=Counter32
_SnBgp4NeighOperStatusUpdateRxCounts_Object=MibTableColumn
snBgp4NeighOperStatusUpdateRxCounts=_SnBgp4NeighOperStatusUpdateRxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,12),_SnBgp4NeighOperStatusUpdateRxCounts_Type())
snBgp4NeighOperStatusUpdateRxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusUpdateRxCounts.setStatus(_A)
_SnBgp4NeighOperStatusNotifTxCounts_Type=Counter32
_SnBgp4NeighOperStatusNotifTxCounts_Object=MibTableColumn
snBgp4NeighOperStatusNotifTxCounts=_SnBgp4NeighOperStatusNotifTxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,13),_SnBgp4NeighOperStatusNotifTxCounts_Type())
snBgp4NeighOperStatusNotifTxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusNotifTxCounts.setStatus(_A)
_SnBgp4NeighOperStatusNotifRxCounts_Type=Counter32
_SnBgp4NeighOperStatusNotifRxCounts_Object=MibTableColumn
snBgp4NeighOperStatusNotifRxCounts=_SnBgp4NeighOperStatusNotifRxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,14),_SnBgp4NeighOperStatusNotifRxCounts_Type())
snBgp4NeighOperStatusNotifRxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusNotifRxCounts.setStatus(_A)
_SnBgp4NeighOperStatusOpenTxCounts_Type=Counter32
_SnBgp4NeighOperStatusOpenTxCounts_Object=MibTableColumn
snBgp4NeighOperStatusOpenTxCounts=_SnBgp4NeighOperStatusOpenTxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,15),_SnBgp4NeighOperStatusOpenTxCounts_Type())
snBgp4NeighOperStatusOpenTxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusOpenTxCounts.setStatus(_A)
_SnBgp4NeighOperStatusOpenRxCounts_Type=Counter32
_SnBgp4NeighOperStatusOpenRxCounts_Object=MibTableColumn
snBgp4NeighOperStatusOpenRxCounts=_SnBgp4NeighOperStatusOpenRxCounts_Object((1,3,6,1,4,1,1991,1,2,11,15,1,1,16),_SnBgp4NeighOperStatusOpenRxCounts_Type())
snBgp4NeighOperStatusOpenRxCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighOperStatusOpenRxCounts.setStatus(_A)
_SnBgp4RouteOperStatus_ObjectIdentity=ObjectIdentity
snBgp4RouteOperStatus=_SnBgp4RouteOperStatus_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,16))
_SnBgp4RouteOperStatusTable_Object=MibTable
snBgp4RouteOperStatusTable=_SnBgp4RouteOperStatusTable_Object((1,3,6,1,4,1,1991,1,2,11,16,1))
if mibBuilder.loadTexts:snBgp4RouteOperStatusTable.setStatus(_A)
_SnBgp4RouteOperStatusEntry_Object=MibTableRow
snBgp4RouteOperStatusEntry=_SnBgp4RouteOperStatusEntry_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1))
snBgp4RouteOperStatusEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:snBgp4RouteOperStatusEntry.setStatus(_A)
_SnBgp4RouteOperStatusIndex_Type=Integer32
_SnBgp4RouteOperStatusIndex_Object=MibTableColumn
snBgp4RouteOperStatusIndex=_SnBgp4RouteOperStatusIndex_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,1),_SnBgp4RouteOperStatusIndex_Type())
snBgp4RouteOperStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusIndex.setStatus(_A)
_SnBgp4RouteOperStatusIp_Type=IpAddress
_SnBgp4RouteOperStatusIp_Object=MibTableColumn
snBgp4RouteOperStatusIp=_SnBgp4RouteOperStatusIp_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,2),_SnBgp4RouteOperStatusIp_Type())
snBgp4RouteOperStatusIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusIp.setStatus(_A)
_SnBgp4RouteOperStatusSubnetMask_Type=IpAddress
_SnBgp4RouteOperStatusSubnetMask_Object=MibTableColumn
snBgp4RouteOperStatusSubnetMask=_SnBgp4RouteOperStatusSubnetMask_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,3),_SnBgp4RouteOperStatusSubnetMask_Type())
snBgp4RouteOperStatusSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusSubnetMask.setStatus(_A)
_SnBgp4RouteOperStatusNextHop_Type=IpAddress
_SnBgp4RouteOperStatusNextHop_Object=MibTableColumn
snBgp4RouteOperStatusNextHop=_SnBgp4RouteOperStatusNextHop_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,4),_SnBgp4RouteOperStatusNextHop_Type())
snBgp4RouteOperStatusNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusNextHop.setStatus(_A)
_SnBgp4RouteOperStatusMetric_Type=Integer32
_SnBgp4RouteOperStatusMetric_Object=MibTableColumn
snBgp4RouteOperStatusMetric=_SnBgp4RouteOperStatusMetric_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,5),_SnBgp4RouteOperStatusMetric_Type())
snBgp4RouteOperStatusMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusMetric.setStatus(_A)
_SnBgp4RouteOperStatusLocalPreference_Type=Integer32
_SnBgp4RouteOperStatusLocalPreference_Object=MibTableColumn
snBgp4RouteOperStatusLocalPreference=_SnBgp4RouteOperStatusLocalPreference_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,6),_SnBgp4RouteOperStatusLocalPreference_Type())
snBgp4RouteOperStatusLocalPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusLocalPreference.setStatus(_A)
_SnBgp4RouteOperStatusWeight_Type=Integer32
_SnBgp4RouteOperStatusWeight_Object=MibTableColumn
snBgp4RouteOperStatusWeight=_SnBgp4RouteOperStatusWeight_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,7),_SnBgp4RouteOperStatusWeight_Type())
snBgp4RouteOperStatusWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusWeight.setStatus(_A)
class _SnBgp4RouteOperStatusOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2)))
_SnBgp4RouteOperStatusOrigin_Type.__name__=_D
_SnBgp4RouteOperStatusOrigin_Object=MibTableColumn
snBgp4RouteOperStatusOrigin=_SnBgp4RouteOperStatusOrigin_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,8),_SnBgp4RouteOperStatusOrigin_Type())
snBgp4RouteOperStatusOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusOrigin.setStatus(_A)
_SnBgp4RouteOperStatusStatus_Type=Integer32
_SnBgp4RouteOperStatusStatus_Object=MibTableColumn
snBgp4RouteOperStatusStatus=_SnBgp4RouteOperStatusStatus_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,9),_SnBgp4RouteOperStatusStatus_Type())
snBgp4RouteOperStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusStatus.setStatus(_A)
_SnBgp4RouteOperStatusRouteTag_Type=Integer32
_SnBgp4RouteOperStatusRouteTag_Object=MibTableColumn
snBgp4RouteOperStatusRouteTag=_SnBgp4RouteOperStatusRouteTag_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,10),_SnBgp4RouteOperStatusRouteTag_Type())
snBgp4RouteOperStatusRouteTag.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusRouteTag.setStatus(_A)
_SnBgp4RouteOperStatusCommunityList_Type=OctetString
_SnBgp4RouteOperStatusCommunityList_Object=MibTableColumn
snBgp4RouteOperStatusCommunityList=_SnBgp4RouteOperStatusCommunityList_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,11),_SnBgp4RouteOperStatusCommunityList_Type())
snBgp4RouteOperStatusCommunityList.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusCommunityList.setStatus(_A)
_SnBgp4RouteOperStatusAsPathList_Type=OctetString
_SnBgp4RouteOperStatusAsPathList_Object=MibTableColumn
snBgp4RouteOperStatusAsPathList=_SnBgp4RouteOperStatusAsPathList_Object((1,3,6,1,4,1,1991,1,2,11,16,1,1,12),_SnBgp4RouteOperStatusAsPathList_Type())
snBgp4RouteOperStatusAsPathList.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4RouteOperStatusAsPathList.setStatus(_A)
_SnBgp4NeighborSummary_ObjectIdentity=ObjectIdentity
snBgp4NeighborSummary=_SnBgp4NeighborSummary_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,17))
_SnBgp4NeighborSummaryTable_Object=MibTable
snBgp4NeighborSummaryTable=_SnBgp4NeighborSummaryTable_Object((1,3,6,1,4,1,1991,1,2,11,17,1))
if mibBuilder.loadTexts:snBgp4NeighborSummaryTable.setStatus(_A)
_SnBgp4NeighborSummaryEntry_Object=MibTableRow
snBgp4NeighborSummaryEntry=_SnBgp4NeighborSummaryEntry_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1))
snBgp4NeighborSummaryEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:snBgp4NeighborSummaryEntry.setStatus(_A)
_SnBgp4NeighborSummaryIndex_Type=Integer32
_SnBgp4NeighborSummaryIndex_Object=MibTableColumn
snBgp4NeighborSummaryIndex=_SnBgp4NeighborSummaryIndex_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,1),_SnBgp4NeighborSummaryIndex_Type())
snBgp4NeighborSummaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryIndex.setStatus(_A)
_SnBgp4NeighborSummaryIp_Type=IpAddress
_SnBgp4NeighborSummaryIp_Object=MibTableColumn
snBgp4NeighborSummaryIp=_SnBgp4NeighborSummaryIp_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,2),_SnBgp4NeighborSummaryIp_Type())
snBgp4NeighborSummaryIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryIp.setStatus(_A)
class _SnBgp4NeighborSummaryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_v,0),('idle',1),(_w,2),(_x,3),(_y,4),(_z,5),(_A0,6)))
_SnBgp4NeighborSummaryState_Type.__name__=_D
_SnBgp4NeighborSummaryState_Object=MibTableColumn
snBgp4NeighborSummaryState=_SnBgp4NeighborSummaryState_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,3),_SnBgp4NeighborSummaryState_Type())
snBgp4NeighborSummaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryState.setStatus(_A)
_SnBgp4NeighborSummaryStateChgTime_Type=Integer32
_SnBgp4NeighborSummaryStateChgTime_Object=MibTableColumn
snBgp4NeighborSummaryStateChgTime=_SnBgp4NeighborSummaryStateChgTime_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,4),_SnBgp4NeighborSummaryStateChgTime_Type())
snBgp4NeighborSummaryStateChgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryStateChgTime.setStatus(_A)
_SnBgp4NeighborSummaryRouteReceived_Type=Integer32
_SnBgp4NeighborSummaryRouteReceived_Object=MibTableColumn
snBgp4NeighborSummaryRouteReceived=_SnBgp4NeighborSummaryRouteReceived_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,5),_SnBgp4NeighborSummaryRouteReceived_Type())
snBgp4NeighborSummaryRouteReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryRouteReceived.setStatus(_A)
_SnBgp4NeighborSummaryRouteInstalled_Type=Integer32
_SnBgp4NeighborSummaryRouteInstalled_Object=MibTableColumn
snBgp4NeighborSummaryRouteInstalled=_SnBgp4NeighborSummaryRouteInstalled_Object((1,3,6,1,4,1,1991,1,2,11,17,1,1,6),_SnBgp4NeighborSummaryRouteInstalled_Type())
snBgp4NeighborSummaryRouteInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighborSummaryRouteInstalled.setStatus(_A)
_SnBgp4Attribute_ObjectIdentity=ObjectIdentity
snBgp4Attribute=_SnBgp4Attribute_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,18))
_SnBgp4AttributeTable_Object=MibTable
snBgp4AttributeTable=_SnBgp4AttributeTable_Object((1,3,6,1,4,1,1991,1,2,11,18,1))
if mibBuilder.loadTexts:snBgp4AttributeTable.setStatus(_A)
_SnBgp4AttributeEntry_Object=MibTableRow
snBgp4AttributeEntry=_SnBgp4AttributeEntry_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1))
snBgp4AttributeEntry.setIndexNames((0,_F,_A3))
if mibBuilder.loadTexts:snBgp4AttributeEntry.setStatus(_A)
_SnBgp4AttributeIndex_Type=Integer32
_SnBgp4AttributeIndex_Object=MibTableColumn
snBgp4AttributeIndex=_SnBgp4AttributeIndex_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,1),_SnBgp4AttributeIndex_Type())
snBgp4AttributeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeIndex.setStatus(_A)
_SnBgp4AttributeNextHop_Type=IpAddress
_SnBgp4AttributeNextHop_Object=MibTableColumn
snBgp4AttributeNextHop=_SnBgp4AttributeNextHop_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,2),_SnBgp4AttributeNextHop_Type())
snBgp4AttributeNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeNextHop.setStatus(_A)
_SnBgp4AttributeMetric_Type=Integer32
_SnBgp4AttributeMetric_Object=MibTableColumn
snBgp4AttributeMetric=_SnBgp4AttributeMetric_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,3),_SnBgp4AttributeMetric_Type())
snBgp4AttributeMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeMetric.setStatus(_A)
class _SnBgp4AttributeOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),(_W,1),(_X,2)))
_SnBgp4AttributeOrigin_Type.__name__=_D
_SnBgp4AttributeOrigin_Object=MibTableColumn
snBgp4AttributeOrigin=_SnBgp4AttributeOrigin_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,4),_SnBgp4AttributeOrigin_Type())
snBgp4AttributeOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeOrigin.setStatus(_A)
_SnBgp4AttributeAggregatorAs_Type=Integer32
_SnBgp4AttributeAggregatorAs_Object=MibTableColumn
snBgp4AttributeAggregatorAs=_SnBgp4AttributeAggregatorAs_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,5),_SnBgp4AttributeAggregatorAs_Type())
snBgp4AttributeAggregatorAs.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeAggregatorAs.setStatus(_A)
_SnBgp4AttributeRouterId_Type=IpAddress
_SnBgp4AttributeRouterId_Object=MibTableColumn
snBgp4AttributeRouterId=_SnBgp4AttributeRouterId_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,6),_SnBgp4AttributeRouterId_Type())
snBgp4AttributeRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeRouterId.setStatus(_A)
class _SnBgp4AttributeAtomicAggregatePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_SnBgp4AttributeAtomicAggregatePresent_Type.__name__=_D
_SnBgp4AttributeAtomicAggregatePresent_Object=MibTableColumn
snBgp4AttributeAtomicAggregatePresent=_SnBgp4AttributeAtomicAggregatePresent_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,7),_SnBgp4AttributeAtomicAggregatePresent_Type())
snBgp4AttributeAtomicAggregatePresent.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeAtomicAggregatePresent.setStatus(_A)
_SnBgp4AttributeLocalPreference_Type=Integer32
_SnBgp4AttributeLocalPreference_Object=MibTableColumn
snBgp4AttributeLocalPreference=_SnBgp4AttributeLocalPreference_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,8),_SnBgp4AttributeLocalPreference_Type())
snBgp4AttributeLocalPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeLocalPreference.setStatus(_A)
_SnBgp4AttributeCommunityList_Type=OctetString
_SnBgp4AttributeCommunityList_Object=MibTableColumn
snBgp4AttributeCommunityList=_SnBgp4AttributeCommunityList_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,9),_SnBgp4AttributeCommunityList_Type())
snBgp4AttributeCommunityList.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeCommunityList.setStatus(_A)
_SnBgp4AttributeAsPathList_Type=OctetString
_SnBgp4AttributeAsPathList_Object=MibTableColumn
snBgp4AttributeAsPathList=_SnBgp4AttributeAsPathList_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,10),_SnBgp4AttributeAsPathList_Type())
snBgp4AttributeAsPathList.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeAsPathList.setStatus(_A)
_SnBgp4AttributeOriginator_Type=IpAddress
_SnBgp4AttributeOriginator_Object=MibTableColumn
snBgp4AttributeOriginator=_SnBgp4AttributeOriginator_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,11),_SnBgp4AttributeOriginator_Type())
snBgp4AttributeOriginator.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeOriginator.setStatus(_A)
_SnBgp4AttributeClusterList_Type=OctetString
_SnBgp4AttributeClusterList_Object=MibTableColumn
snBgp4AttributeClusterList=_SnBgp4AttributeClusterList_Object((1,3,6,1,4,1,1991,1,2,11,18,1,1,12),_SnBgp4AttributeClusterList_Type())
snBgp4AttributeClusterList.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4AttributeClusterList.setStatus(_A)
_SnBgp4ClearNeighborCmd_ObjectIdentity=ObjectIdentity
snBgp4ClearNeighborCmd=_SnBgp4ClearNeighborCmd_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,19))
_SnBgp4ClearNeighborCmdTable_Object=MibTable
snBgp4ClearNeighborCmdTable=_SnBgp4ClearNeighborCmdTable_Object((1,3,6,1,4,1,1991,1,2,11,19,1))
if mibBuilder.loadTexts:snBgp4ClearNeighborCmdTable.setStatus(_A)
_SnBgp4ClearNeighborCmdEntry_Object=MibTableRow
snBgp4ClearNeighborCmdEntry=_SnBgp4ClearNeighborCmdEntry_Object((1,3,6,1,4,1,1991,1,2,11,19,1,1))
snBgp4ClearNeighborCmdEntry.setIndexNames((0,_F,_A4))
if mibBuilder.loadTexts:snBgp4ClearNeighborCmdEntry.setStatus(_A)
_SnBgp4ClearNeighborCmdIp_Type=IpAddress
_SnBgp4ClearNeighborCmdIp_Object=MibTableColumn
snBgp4ClearNeighborCmdIp=_SnBgp4ClearNeighborCmdIp_Object((1,3,6,1,4,1,1991,1,2,11,19,1,1,1),_SnBgp4ClearNeighborCmdIp_Type())
snBgp4ClearNeighborCmdIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4ClearNeighborCmdIp.setStatus(_A)
class _SnBgp4ClearNeighborCmdElement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),('lastPacketWithError',1),('notificationErrors',2),('softOutbound',3),('traffic',4),('neighbor',5)))
_SnBgp4ClearNeighborCmdElement_Type.__name__=_D
_SnBgp4ClearNeighborCmdElement_Object=MibTableColumn
snBgp4ClearNeighborCmdElement=_SnBgp4ClearNeighborCmdElement_Object((1,3,6,1,4,1,1991,1,2,11,19,1,1,2),_SnBgp4ClearNeighborCmdElement_Type())
snBgp4ClearNeighborCmdElement.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4ClearNeighborCmdElement.setStatus(_A)
_SnBgp4NeighPrefixGroup_ObjectIdentity=ObjectIdentity
snBgp4NeighPrefixGroup=_SnBgp4NeighPrefixGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,2,11,20))
_SnBgp4NeighPrefixGroupTable_Object=MibTable
snBgp4NeighPrefixGroupTable=_SnBgp4NeighPrefixGroupTable_Object((1,3,6,1,4,1,1991,1,2,11,20,1))
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupTable.setStatus(_A)
_SnBgp4NeighPrefixGroupEntry_Object=MibTableRow
snBgp4NeighPrefixGroupEntry=_SnBgp4NeighPrefixGroupEntry_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1))
snBgp4NeighPrefixGroupEntry.setIndexNames((0,_F,_A5),(0,_F,_A6))
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupEntry.setStatus(_A)
_SnBgp4NeighPrefixGroupNeighIp_Type=IpAddress
_SnBgp4NeighPrefixGroupNeighIp_Object=MibTableColumn
snBgp4NeighPrefixGroupNeighIp=_SnBgp4NeighPrefixGroupNeighIp_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1,1),_SnBgp4NeighPrefixGroupNeighIp_Type())
snBgp4NeighPrefixGroupNeighIp.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupNeighIp.setStatus(_A)
class _SnBgp4NeighPrefixGroupDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_SnBgp4NeighPrefixGroupDir_Type.__name__=_D
_SnBgp4NeighPrefixGroupDir_Object=MibTableColumn
snBgp4NeighPrefixGroupDir=_SnBgp4NeighPrefixGroupDir_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1,2),_SnBgp4NeighPrefixGroupDir_Type())
snBgp4NeighPrefixGroupDir.setMaxAccess(_C)
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupDir.setStatus(_A)
class _SnBgp4NeighPrefixGroupInAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighPrefixGroupInAccessList_Type.__name__=_E
_SnBgp4NeighPrefixGroupInAccessList_Object=MibTableColumn
snBgp4NeighPrefixGroupInAccessList=_SnBgp4NeighPrefixGroupInAccessList_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1,3),_SnBgp4NeighPrefixGroupInAccessList_Type())
snBgp4NeighPrefixGroupInAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupInAccessList.setStatus(_A)
class _SnBgp4NeighPrefixGroupOutAccessList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnBgp4NeighPrefixGroupOutAccessList_Type.__name__=_E
_SnBgp4NeighPrefixGroupOutAccessList_Object=MibTableColumn
snBgp4NeighPrefixGroupOutAccessList=_SnBgp4NeighPrefixGroupOutAccessList_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1,4),_SnBgp4NeighPrefixGroupOutAccessList_Type())
snBgp4NeighPrefixGroupOutAccessList.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupOutAccessList.setStatus(_A)
class _SnBgp4NeighPrefixGroupRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_I,2),(_K,3),(_L,4),(_M,5)))
_SnBgp4NeighPrefixGroupRowStatus_Type.__name__=_D
_SnBgp4NeighPrefixGroupRowStatus_Object=MibTableColumn
snBgp4NeighPrefixGroupRowStatus=_SnBgp4NeighPrefixGroupRowStatus_Object((1,3,6,1,4,1,1991,1,2,11,20,1,1,5),_SnBgp4NeighPrefixGroupRowStatus_Type())
snBgp4NeighPrefixGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snBgp4NeighPrefixGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'snBgp4':snBgp4,'snBgp4Gen':snBgp4Gen,'snBgp4GenAlwaysCompareMed':snBgp4GenAlwaysCompareMed,'snBgp4GenAutoSummary':snBgp4GenAutoSummary,'snBgp4GenDefaultLocalPreference':snBgp4GenDefaultLocalPreference,'snBgp4GenDefaultInfoOriginate':snBgp4GenDefaultInfoOriginate,'snBgp4GenFastExternalFallover':snBgp4GenFastExternalFallover,'snBgp4GenNextBootNeighbors':snBgp4GenNextBootNeighbors,'snBgp4GenNextBootRoutes':snBgp4GenNextBootRoutes,'snBgp4GenSynchronization':snBgp4GenSynchronization,'snBgp4GenKeepAliveTime':snBgp4GenKeepAliveTime,'snBgp4GenHoldTime':snBgp4GenHoldTime,'snBgp4GenRouterId':snBgp4GenRouterId,'snBgp4GenTableMap':snBgp4GenTableMap,'snBgp4GenAdminStat':snBgp4GenAdminStat,'snBgp4GenDefaultMetric':snBgp4GenDefaultMetric,'snBgp4GenMaxNeighbors':snBgp4GenMaxNeighbors,'snBgp4GenMinNeighbors':snBgp4GenMinNeighbors,'snBgp4GenMaxRoutes':snBgp4GenMaxRoutes,'snBgp4GenMinRoutes':snBgp4GenMinRoutes,'snBgp4GenMaxAddrFilters':snBgp4GenMaxAddrFilters,'snBgp4GenMaxAggregateAddresses':snBgp4GenMaxAggregateAddresses,'snBgp4GenMaxAsPathFilters':snBgp4GenMaxAsPathFilters,'snBgp4GenMaxCommunityFilters':snBgp4GenMaxCommunityFilters,'snBgp4GenMaxNetworks':snBgp4GenMaxNetworks,'snBgp4GenMaxRouteMapFilters':snBgp4GenMaxRouteMapFilters,'snBgp4GenNeighPrefixMinValue':snBgp4GenNeighPrefixMinValue,'snBgp4GenOperNeighbors':snBgp4GenOperNeighbors,'snBgp4GenOperRoutes':snBgp4GenOperRoutes,'snBgp4GenLocalAs':snBgp4GenLocalAs,'snBgp4GenRoutesInstalled':snBgp4GenRoutesInstalled,'snBgp4GenAsPathInstalled':snBgp4GenAsPathInstalled,'snBgp4ExternalDistance':snBgp4ExternalDistance,'snBgp4InternalDistance':snBgp4InternalDistance,'snBgp4LocalDistance':snBgp4LocalDistance,'snBgp4OperNumOfAttributes':snBgp4OperNumOfAttributes,'snBgp4NextBootMaxAttributes':snBgp4NextBootMaxAttributes,'snBgp4ClusterId':snBgp4ClusterId,'snBgp4ClientToClientReflection':snBgp4ClientToClientReflection,'snBgp4GenTotalNeighbors':snBgp4GenTotalNeighbors,'snBgp4GenMaxPaths':snBgp4GenMaxPaths,'snBgp4GenConfedId':snBgp4GenConfedId,'snBgp4GenConfedPeers':snBgp4GenConfedPeers,'snBgp4GenDampening':snBgp4GenDampening,'snBgp4GenDampenHalfLife':snBgp4GenDampenHalfLife,'snBgp4GenDampenReuse':snBgp4GenDampenReuse,'snBgp4GenDampenSuppress':snBgp4GenDampenSuppress,'snBgp4GenDampenMaxSuppress':snBgp4GenDampenMaxSuppress,'snBgp4GenDampenMap':snBgp4GenDampenMap,'snBgp4GenLocalAs4':snBgp4GenLocalAs4,'snBgp4GenDefaultMetric1':snBgp4GenDefaultMetric1,'snBgp4GenDefaultLocalPreference1':snBgp4GenDefaultLocalPreference1,'snBgp4AddrFilter':snBgp4AddrFilter,'snBgp4AddrFilterTable':snBgp4AddrFilterTable,'snBgp4AddrFilterEntry':snBgp4AddrFilterEntry,_Y:snBgp4AddrFilterIndex,'snBgp4AddrFilterAction':snBgp4AddrFilterAction,'snBgp4AddrFilterSourceIp':snBgp4AddrFilterSourceIp,'snBgp4AddrFilterSourceMask':snBgp4AddrFilterSourceMask,'snBgp4AddrFilterDestIp':snBgp4AddrFilterDestIp,'snBgp4AddrFilterDestMask':snBgp4AddrFilterDestMask,'snBgp4AddrFilterRowStatus':snBgp4AddrFilterRowStatus,'snBgp4AggregateAddr':snBgp4AggregateAddr,'snBgp4AggregateAddrTable':snBgp4AggregateAddrTable,'snBgp4AggregateAddrEntry':snBgp4AggregateAddrEntry,_Z:snBgp4AggregateAddrIp,_a:snBgp4AggregateAddrMask,_b:snBgp4AggregateAddrOption,'snBgp4AggregateAddrMap':snBgp4AggregateAddrMap,'snBgp4AggregateAddrRowStatus':snBgp4AggregateAddrRowStatus,'snBgp4AsPathFilter':snBgp4AsPathFilter,'snBgp4AsPathFilterTable':snBgp4AsPathFilterTable,'snBgp4AsPathFilterEntry':snBgp4AsPathFilterEntry,_c:snBgp4AsPathFilterIndex,'snBgp4AsPathFilterAction':snBgp4AsPathFilterAction,'snBgp4AsPathFilterRegExpression':snBgp4AsPathFilterRegExpression,'snBgp4AsPathFilterRowStatus':snBgp4AsPathFilterRowStatus,'snBgp4CommunityFilter':snBgp4CommunityFilter,'snBgp4CommunityFilterTable':snBgp4CommunityFilterTable,'snBgp4CommunityFilterEntry':snBgp4CommunityFilterEntry,_d:snBgp4CommunityFilterIndex,'snBgp4CommunityFilterAction':snBgp4CommunityFilterAction,'snBgp4CommunityFilterCommNum':snBgp4CommunityFilterCommNum,'snBgp4CommunityFilterInternet':snBgp4CommunityFilterInternet,'snBgp4CommunityFilterNoAdvertise':snBgp4CommunityFilterNoAdvertise,'snBgp4CommunityFilterNoExport':snBgp4CommunityFilterNoExport,'snBgp4CommunityFilterRowStatus':snBgp4CommunityFilterRowStatus,'snBgp4CommunityFilterLocalAs':snBgp4CommunityFilterLocalAs,'snBgp4NeighGenCfg':snBgp4NeighGenCfg,'snBgp4NeighGenCfgTable':snBgp4NeighGenCfgTable,'snBgp4NeighGenCfgEntry':snBgp4NeighGenCfgEntry,_e:snBgp4NeighGenCfgNeighIp,'snBgp4NeighGenCfgAdvertlevel':snBgp4NeighGenCfgAdvertlevel,'snBgp4NeighGenCfgDefOriginate':snBgp4NeighGenCfgDefOriginate,'snBgp4NeighGenCfgEbgpMultihop':snBgp4NeighGenCfgEbgpMultihop,'snBgp4NeighGenCfgMaxPrefix':snBgp4NeighGenCfgMaxPrefix,'snBgp4NeighGenCfgNextHopSelf':snBgp4NeighGenCfgNextHopSelf,'snBgp4NeighGenCfgRemoteAs':snBgp4NeighGenCfgRemoteAs,'snBgp4NeighGenCfgSendComm':snBgp4NeighGenCfgSendComm,'snBgp4NeighGenCfgWeight':snBgp4NeighGenCfgWeight,'snBgp4NeighGenCfgWeightFilterList':snBgp4NeighGenCfgWeightFilterList,'snBgp4NeighGenCfgRowStatus':snBgp4NeighGenCfgRowStatus,'snBgp4NeighGenCfgUpdateSrcLpbIntf':snBgp4NeighGenCfgUpdateSrcLpbIntf,'snBgp4NeighGenCfgRouteRefClient':snBgp4NeighGenCfgRouteRefClient,'snBgp4NeighGenCfgRemovePrivateAs':snBgp4NeighGenCfgRemovePrivateAs,'snBgp4NeighGenCfgEbgpMultihopTtl':snBgp4NeighGenCfgEbgpMultihopTtl,'snBgp4NeighGenCfgShutdown':snBgp4NeighGenCfgShutdown,'snBgp4NeighGenCfgKeepAliveTime':snBgp4NeighGenCfgKeepAliveTime,'snBgp4NeighGenCfgHoldTime':snBgp4NeighGenCfgHoldTime,'snBgp4NeighGenCfgDefOrigMap':snBgp4NeighGenCfgDefOrigMap,'snBgp4NeighGenCfgDesc':snBgp4NeighGenCfgDesc,'snBgp4NeighGenCfgPass':snBgp4NeighGenCfgPass,'snBgp4NeighDistGroup':snBgp4NeighDistGroup,'snBgp4NeighDistGroupTable':snBgp4NeighDistGroupTable,'snBgp4NeighDistGroupEntry':snBgp4NeighDistGroupEntry,_f:snBgp4NeighDistGroupNeighIp,_g:snBgp4NeighDistGroupDir,'snBgp4NeighDistGroupAccessList':snBgp4NeighDistGroupAccessList,'snBgp4NeighDistGroupRowStatus':snBgp4NeighDistGroupRowStatus,'snBgp4NeighDistGroupInFilterList':snBgp4NeighDistGroupInFilterList,'snBgp4NeighDistGroupOutFilterList':snBgp4NeighDistGroupOutFilterList,'snBgp4NeighDistGroupInIpAccessList':snBgp4NeighDistGroupInIpAccessList,'snBgp4NeighDistGroupOutIpAccessList':snBgp4NeighDistGroupOutIpAccessList,'snBgp4NeighDistGroupInPrefixList':snBgp4NeighDistGroupInPrefixList,'snBgp4NeighDistGroupOutPrefixList':snBgp4NeighDistGroupOutPrefixList,'snBgp4NeighFilterGroup':snBgp4NeighFilterGroup,'snBgp4NeighFilterGroupTable':snBgp4NeighFilterGroupTable,'snBgp4NeighFilterGroupEntry':snBgp4NeighFilterGroupEntry,_h:snBgp4NeighFilterGroupNeighIp,_i:snBgp4NeighFilterGroupDir,'snBgp4NeighFilterGroupAccessList':snBgp4NeighFilterGroupAccessList,'snBgp4NeighFilterGroupRowStatus':snBgp4NeighFilterGroupRowStatus,'snBgp4NeighFilterGroupInFilterList':snBgp4NeighFilterGroupInFilterList,'snBgp4NeighFilterGroupOutFilterList':snBgp4NeighFilterGroupOutFilterList,'snBgp4NeighFilterGroupInAsPathAccessList':snBgp4NeighFilterGroupInAsPathAccessList,'snBgp4NeighFilterGroupOutAsPathAccessList':snBgp4NeighFilterGroupOutAsPathAccessList,'snBgp4NeighFilterGroupWeight':snBgp4NeighFilterGroupWeight,'snBgp4NeighFilterGroupWeightAccessList':snBgp4NeighFilterGroupWeightAccessList,'snBgp4NeighRouteMap':snBgp4NeighRouteMap,'snBgp4NeighRouteMapTable':snBgp4NeighRouteMapTable,'snBgp4NeighRouteMapEntry':snBgp4NeighRouteMapEntry,_j:snBgp4NeighRouteMapNeighIp,_k:snBgp4NeighRouteMapDir,'snBgp4NeighRouteMapMapName':snBgp4NeighRouteMapMapName,'snBgp4NeighRouteMapRowStatus':snBgp4NeighRouteMapRowStatus,'snBgp4Network':snBgp4Network,'snBgp4NetworkTable':snBgp4NetworkTable,'snBgp4NetworkEntry':snBgp4NetworkEntry,_l:snBgp4NetworkIp,_m:snBgp4NetworkSubnetMask,'snBgp4NetworkWeight':snBgp4NetworkWeight,'snBgp4NetworkBackdoor':snBgp4NetworkBackdoor,'snBgp4NetworkRowStatus':snBgp4NetworkRowStatus,'snBgp4Redis':snBgp4Redis,'snBgp4RedisTable':snBgp4RedisTable,'snBgp4RedisEntry':snBgp4RedisEntry,_n:snBgp4RedisProtocol,'snBgp4RedisMetric':snBgp4RedisMetric,'snBgp4RedisRouteMap':snBgp4RedisRouteMap,'snBgp4RedisWeight':snBgp4RedisWeight,'snBgp4RedisMatchInternal':snBgp4RedisMatchInternal,'snBgp4RedisMatchExternal1':snBgp4RedisMatchExternal1,'snBgp4RedisMatchExternal2':snBgp4RedisMatchExternal2,'snBgp4RedisRowStatus':snBgp4RedisRowStatus,'snBgp4RouteMapFilter':snBgp4RouteMapFilter,'snBgp4RouteMapFilterTable':snBgp4RouteMapFilterTable,'snBgp4RouteMapFilterEntry':snBgp4RouteMapFilterEntry,_o:snBgp4RouteMapFilterMapName,_p:snBgp4RouteMapFilterSequenceNum,'snBgp4RouteMapFilterAction':snBgp4RouteMapFilterAction,'snBgp4RouteMapFilterRowStatus':snBgp4RouteMapFilterRowStatus,'snBgp4RouteMapMatch':snBgp4RouteMapMatch,'snBgp4RouteMapMatchTable':snBgp4RouteMapMatchTable,'snBgp4RouteMapMatchEntry':snBgp4RouteMapMatchEntry,_q:snBgp4RouteMapMatchMapName,_r:snBgp4RouteMapMatchSequenceNum,'snBgp4RouteMapMatchAsPathFilter':snBgp4RouteMapMatchAsPathFilter,'snBgp4RouteMapMatchCommunityFilter':snBgp4RouteMapMatchCommunityFilter,'snBgp4RouteMapMatchAddressFilter':snBgp4RouteMapMatchAddressFilter,'snBgp4RouteMapMatchMetric':snBgp4RouteMapMatchMetric,'snBgp4RouteMapMatchNextHopList':snBgp4RouteMapMatchNextHopList,'snBgp4RouteMapMatchRouteType':snBgp4RouteMapMatchRouteType,'snBgp4RouteMapMatchTagList':snBgp4RouteMapMatchTagList,'snBgp4RouteMapMatchRowMask':snBgp4RouteMapMatchRowMask,'snBgp4RouteMapMatchAsPathAccessList':snBgp4RouteMapMatchAsPathAccessList,'snBgp4RouteMapMatchCommunityList':snBgp4RouteMapMatchCommunityList,'snBgp4RouteMapMatchAddressAccessList':snBgp4RouteMapMatchAddressAccessList,'snBgp4RouteMapMatchAddressPrefixList':snBgp4RouteMapMatchAddressPrefixList,'snBgp4RouteMapMatchNextHopAccessList':snBgp4RouteMapMatchNextHopAccessList,'snBgp4RouteMapMatchNextHopPrefixList':snBgp4RouteMapMatchNextHopPrefixList,'snBgp4RouteMapSet':snBgp4RouteMapSet,'snBgp4RouteMapSetTable':snBgp4RouteMapSetTable,'snBgp4RouteMapSetEntry':snBgp4RouteMapSetEntry,_s:snBgp4RouteMapSetMapName,_t:snBgp4RouteMapSetSequenceNum,'snBgp4RouteMapSetAsPathType':snBgp4RouteMapSetAsPathType,'snBgp4RouteMapSetAsPathString':snBgp4RouteMapSetAsPathString,'snBgp4RouteMapSetAutoTag':snBgp4RouteMapSetAutoTag,'snBgp4RouteMapSetCommunityType':snBgp4RouteMapSetCommunityType,'snBgp4RouteMapSetCommunityNum':snBgp4RouteMapSetCommunityNum,'snBgp4RouteMapSetCommunityAdditive':snBgp4RouteMapSetCommunityAdditive,'snBgp4RouteMapSetLocalPreference':snBgp4RouteMapSetLocalPreference,'snBgp4RouteMapSetMetric':snBgp4RouteMapSetMetric,'snBgp4RouteMapSetNextHop':snBgp4RouteMapSetNextHop,'snBgp4RouteMapSetOrigin':snBgp4RouteMapSetOrigin,'snBgp4RouteMapSetTag':snBgp4RouteMapSetTag,'snBgp4RouteMapSetWeight':snBgp4RouteMapSetWeight,'snBgp4RouteMapSetRowMask':snBgp4RouteMapSetRowMask,'snBgp4RouteMapSetCommunityNums':snBgp4RouteMapSetCommunityNums,'snBgp4RouteMapSetDampenHalfLife':snBgp4RouteMapSetDampenHalfLife,'snBgp4RouteMapSetDampenReuse':snBgp4RouteMapSetDampenReuse,'snBgp4RouteMapSetDampenSuppress':snBgp4RouteMapSetDampenSuppress,'snBgp4RouteMapSetDampenMaxSuppress':snBgp4RouteMapSetDampenMaxSuppress,'snBgp4NeighOperStatus':snBgp4NeighOperStatus,'snBgp4NeighOperStatusTable':snBgp4NeighOperStatusTable,'snBgp4NeighOperStatusEntry':snBgp4NeighOperStatusEntry,_u:snBgp4NeighOperStatusIndex,'snBgp4NeighOperStatusIp':snBgp4NeighOperStatusIp,'snBgp4NeighOperStatusRemoteAs':snBgp4NeighOperStatusRemoteAs,'snBgp4NeighOperStatusBgpType':snBgp4NeighOperStatusBgpType,'snBgp4NeighOperStatusState':snBgp4NeighOperStatusState,'snBgp4NeighOperStatusKeepAliveTime':snBgp4NeighOperStatusKeepAliveTime,'snBgp4NeighOperStatusHoldTime':snBgp4NeighOperStatusHoldTime,'snBgp4NeighOperStatusAdvertlevel':snBgp4NeighOperStatusAdvertlevel,'snBgp4NeighOperStatusKeepAliveTxCounts':snBgp4NeighOperStatusKeepAliveTxCounts,'snBgp4NeighOperStatusKeepAliveRxCounts':snBgp4NeighOperStatusKeepAliveRxCounts,'snBgp4NeighOperStatusUpdateTxCounts':snBgp4NeighOperStatusUpdateTxCounts,'snBgp4NeighOperStatusUpdateRxCounts':snBgp4NeighOperStatusUpdateRxCounts,'snBgp4NeighOperStatusNotifTxCounts':snBgp4NeighOperStatusNotifTxCounts,'snBgp4NeighOperStatusNotifRxCounts':snBgp4NeighOperStatusNotifRxCounts,'snBgp4NeighOperStatusOpenTxCounts':snBgp4NeighOperStatusOpenTxCounts,'snBgp4NeighOperStatusOpenRxCounts':snBgp4NeighOperStatusOpenRxCounts,'snBgp4RouteOperStatus':snBgp4RouteOperStatus,'snBgp4RouteOperStatusTable':snBgp4RouteOperStatusTable,'snBgp4RouteOperStatusEntry':snBgp4RouteOperStatusEntry,_A1:snBgp4RouteOperStatusIndex,'snBgp4RouteOperStatusIp':snBgp4RouteOperStatusIp,'snBgp4RouteOperStatusSubnetMask':snBgp4RouteOperStatusSubnetMask,'snBgp4RouteOperStatusNextHop':snBgp4RouteOperStatusNextHop,'snBgp4RouteOperStatusMetric':snBgp4RouteOperStatusMetric,'snBgp4RouteOperStatusLocalPreference':snBgp4RouteOperStatusLocalPreference,'snBgp4RouteOperStatusWeight':snBgp4RouteOperStatusWeight,'snBgp4RouteOperStatusOrigin':snBgp4RouteOperStatusOrigin,'snBgp4RouteOperStatusStatus':snBgp4RouteOperStatusStatus,'snBgp4RouteOperStatusRouteTag':snBgp4RouteOperStatusRouteTag,'snBgp4RouteOperStatusCommunityList':snBgp4RouteOperStatusCommunityList,'snBgp4RouteOperStatusAsPathList':snBgp4RouteOperStatusAsPathList,'snBgp4NeighborSummary':snBgp4NeighborSummary,'snBgp4NeighborSummaryTable':snBgp4NeighborSummaryTable,'snBgp4NeighborSummaryEntry':snBgp4NeighborSummaryEntry,_A2:snBgp4NeighborSummaryIndex,'snBgp4NeighborSummaryIp':snBgp4NeighborSummaryIp,'snBgp4NeighborSummaryState':snBgp4NeighborSummaryState,'snBgp4NeighborSummaryStateChgTime':snBgp4NeighborSummaryStateChgTime,'snBgp4NeighborSummaryRouteReceived':snBgp4NeighborSummaryRouteReceived,'snBgp4NeighborSummaryRouteInstalled':snBgp4NeighborSummaryRouteInstalled,'snBgp4Attribute':snBgp4Attribute,'snBgp4AttributeTable':snBgp4AttributeTable,'snBgp4AttributeEntry':snBgp4AttributeEntry,_A3:snBgp4AttributeIndex,'snBgp4AttributeNextHop':snBgp4AttributeNextHop,'snBgp4AttributeMetric':snBgp4AttributeMetric,'snBgp4AttributeOrigin':snBgp4AttributeOrigin,'snBgp4AttributeAggregatorAs':snBgp4AttributeAggregatorAs,'snBgp4AttributeRouterId':snBgp4AttributeRouterId,'snBgp4AttributeAtomicAggregatePresent':snBgp4AttributeAtomicAggregatePresent,'snBgp4AttributeLocalPreference':snBgp4AttributeLocalPreference,'snBgp4AttributeCommunityList':snBgp4AttributeCommunityList,'snBgp4AttributeAsPathList':snBgp4AttributeAsPathList,'snBgp4AttributeOriginator':snBgp4AttributeOriginator,'snBgp4AttributeClusterList':snBgp4AttributeClusterList,'snBgp4ClearNeighborCmd':snBgp4ClearNeighborCmd,'snBgp4ClearNeighborCmdTable':snBgp4ClearNeighborCmdTable,'snBgp4ClearNeighborCmdEntry':snBgp4ClearNeighborCmdEntry,_A4:snBgp4ClearNeighborCmdIp,'snBgp4ClearNeighborCmdElement':snBgp4ClearNeighborCmdElement,'snBgp4NeighPrefixGroup':snBgp4NeighPrefixGroup,'snBgp4NeighPrefixGroupTable':snBgp4NeighPrefixGroupTable,'snBgp4NeighPrefixGroupEntry':snBgp4NeighPrefixGroupEntry,_A5:snBgp4NeighPrefixGroupNeighIp,_A6:snBgp4NeighPrefixGroupDir,'snBgp4NeighPrefixGroupInAccessList':snBgp4NeighPrefixGroupInAccessList,'snBgp4NeighPrefixGroupOutAccessList':snBgp4NeighPrefixGroupOutAccessList,'snBgp4NeighPrefixGroupRowStatus':snBgp4NeighPrefixGroupRowStatus})