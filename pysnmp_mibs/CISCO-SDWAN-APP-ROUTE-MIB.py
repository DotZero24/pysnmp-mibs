_z='cSdwanAppRouteSlaClassGroup'
_y='cSdwanAppRouteStatisticsAppProbeClassIntervalGroup'
_x='cSdwanAppRouteStatisticsAppProbeClassGroup'
_w='cSdwanAppRouteStatisticsGroup'
_v='appRouteSlaClassJitter'
_u='appRouteSlaClassLatency'
_t='appRouteSlaClassLoss'
_s='appRouteSlaClassName'
_r='appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts'
_q='appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts'
_p='appRouteStatisticsAppProbeClassIntervalRxDataPkts'
_o='appRouteStatisticsAppProbeClassIntervalTxDataPkts'
_n='appRouteStatisticsAppProbeClassIntervalAverageJitter'
_m='appRouteStatisticsAppProbeClassIntervalAverageLatency'
_l='appRouteStatisticsAppProbeClassIntervalLoss'
_k='appRouteStatisticsAppProbeClassIntervalTotalPackets'
_j='appRouteStatisticsAppProbeClassMeanJitter'
_i='appRouteStatisticsAppProbeClassMeanLatency'
_h='appRouteStatisticsAppProbeClassMeanLoss'
_g='appRouteStatisticsRemoteColor'
_f='appRouteStatisticsLocalColor'
_e='appRouteStatisticsRemoteSystemIp'
_d='appRouteStatisticsAppProbeClassIntervalIndex'
_c='String'
_b='appRouteSlaClassIndex'
_a='private6'
_Z='private5'
_Y='private4'
_X='private3'
_W='private2'
_V='private1'
_U='custom3'
_T='custom2'
_S='custom1'
_R='bronze'
_Q='silver'
_P='threeG'
_O='publicInternet'
_N='bizInternet'
_M='metroEthernet'
_L='default'
_K='appRouteStatisticsAppProbeClassName'
_J='appRouteStatisticsDstPort'
_I='appRouteStatisticsSrcPort'
_H='appRouteStatisticsProto'
_G='appRouteStatisticsDstIp'
_F='appRouteStatisticsSrcIp'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CISCO-SDWAN-APP-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoSdwanAppRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1001))
if mibBuilder.loadTexts:ciscoSdwanAppRouteMIB.setRevisions(('2021-01-26 00:00',))
class UnsignedByte(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class UnsignedShort(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class ConfdString(TextualConvention,OctetString):status=_A;displayHint='1t'
class String(TextualConvention,OctetString):status=_A;displayHint='1t'
class InetAddressIP(TextualConvention,OctetString):status=_A;displayHint='1d.';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CiscoSdwanAppRouteMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSdwanAppRouteMIBObjects=_CiscoSdwanAppRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1001,1))
_AppRouteStatisticsTable_Object=MibTable
appRouteStatisticsTable=_AppRouteStatisticsTable_Object((1,3,6,1,4,1,9,9,1001,1,2))
if mibBuilder.loadTexts:appRouteStatisticsTable.setStatus(_A)
_AppRouteStatisticsEntry_Object=MibTableRow
appRouteStatisticsEntry=_AppRouteStatisticsEntry_Object((1,3,6,1,4,1,9,9,1001,1,2,1))
appRouteStatisticsEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:appRouteStatisticsEntry.setStatus(_A)
_AppRouteStatisticsSrcIp_Type=InetAddressIP
_AppRouteStatisticsSrcIp_Object=MibTableColumn
appRouteStatisticsSrcIp=_AppRouteStatisticsSrcIp_Object((1,3,6,1,4,1,9,9,1001,1,2,1,1),_AppRouteStatisticsSrcIp_Type())
appRouteStatisticsSrcIp.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsSrcIp.setStatus(_A)
_AppRouteStatisticsDstIp_Type=InetAddressIP
_AppRouteStatisticsDstIp_Object=MibTableColumn
appRouteStatisticsDstIp=_AppRouteStatisticsDstIp_Object((1,3,6,1,4,1,9,9,1001,1,2,1,2),_AppRouteStatisticsDstIp_Type())
appRouteStatisticsDstIp.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsDstIp.setStatus(_A)
class _AppRouteStatisticsProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gre',1),('ipsec',2)))
_AppRouteStatisticsProto_Type.__name__=_E
_AppRouteStatisticsProto_Object=MibTableColumn
appRouteStatisticsProto=_AppRouteStatisticsProto_Object((1,3,6,1,4,1,9,9,1001,1,2,1,3),_AppRouteStatisticsProto_Type())
appRouteStatisticsProto.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsProto.setStatus(_A)
_AppRouteStatisticsSrcPort_Type=UnsignedShort
_AppRouteStatisticsSrcPort_Object=MibTableColumn
appRouteStatisticsSrcPort=_AppRouteStatisticsSrcPort_Object((1,3,6,1,4,1,9,9,1001,1,2,1,4),_AppRouteStatisticsSrcPort_Type())
appRouteStatisticsSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsSrcPort.setStatus(_A)
_AppRouteStatisticsDstPort_Type=UnsignedShort
_AppRouteStatisticsDstPort_Object=MibTableColumn
appRouteStatisticsDstPort=_AppRouteStatisticsDstPort_Object((1,3,6,1,4,1,9,9,1001,1,2,1,5),_AppRouteStatisticsDstPort_Type())
appRouteStatisticsDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsDstPort.setStatus(_A)
_AppRouteStatisticsRemoteSystemIp_Type=InetAddressIP
_AppRouteStatisticsRemoteSystemIp_Object=MibTableColumn
appRouteStatisticsRemoteSystemIp=_AppRouteStatisticsRemoteSystemIp_Object((1,3,6,1,4,1,9,9,1001,1,2,1,6),_AppRouteStatisticsRemoteSystemIp_Type())
appRouteStatisticsRemoteSystemIp.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsRemoteSystemIp.setStatus(_A)
class _AppRouteStatisticsLocalColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_L,1),('mpls',2),(_M,3),(_N,4),(_O,5),('lte',6),(_P,7),('red',8),('green',9),('blue',10),('gold',11),(_Q,12),(_R,13),(_S,14),(_T,15),(_U,16),(_V,17),(_W,18),(_X,19),(_Y,20),(_Z,21),(_a,22)))
_AppRouteStatisticsLocalColor_Type.__name__=_E
_AppRouteStatisticsLocalColor_Object=MibTableColumn
appRouteStatisticsLocalColor=_AppRouteStatisticsLocalColor_Object((1,3,6,1,4,1,9,9,1001,1,2,1,7),_AppRouteStatisticsLocalColor_Type())
appRouteStatisticsLocalColor.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsLocalColor.setStatus(_A)
class _AppRouteStatisticsRemoteColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_L,1),('mpls',2),(_M,3),(_N,4),(_O,5),('lte',6),(_P,7),('red',8),('green',9),('blue',10),('gold',11),(_Q,12),(_R,13),(_S,14),(_T,15),(_U,16),(_V,17),(_W,18),(_X,19),(_Y,20),(_Z,21),(_a,22)))
_AppRouteStatisticsRemoteColor_Type.__name__=_E
_AppRouteStatisticsRemoteColor_Object=MibTableColumn
appRouteStatisticsRemoteColor=_AppRouteStatisticsRemoteColor_Object((1,3,6,1,4,1,9,9,1001,1,2,1,8),_AppRouteStatisticsRemoteColor_Type())
appRouteStatisticsRemoteColor.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsRemoteColor.setStatus(_A)
_AppRouteSlaClassTable_Object=MibTable
appRouteSlaClassTable=_AppRouteSlaClassTable_Object((1,3,6,1,4,1,9,9,1001,1,4))
if mibBuilder.loadTexts:appRouteSlaClassTable.setStatus(_A)
_AppRouteSlaClassEntry_Object=MibTableRow
appRouteSlaClassEntry=_AppRouteSlaClassEntry_Object((1,3,6,1,4,1,9,9,1001,1,4,1))
appRouteSlaClassEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:appRouteSlaClassEntry.setStatus(_A)
_AppRouteSlaClassIndex_Type=UnsignedByte
_AppRouteSlaClassIndex_Object=MibTableColumn
appRouteSlaClassIndex=_AppRouteSlaClassIndex_Object((1,3,6,1,4,1,9,9,1001,1,4,1,1),_AppRouteSlaClassIndex_Type())
appRouteSlaClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteSlaClassIndex.setStatus(_A)
_AppRouteSlaClassName_Type=String
_AppRouteSlaClassName_Object=MibTableColumn
appRouteSlaClassName=_AppRouteSlaClassName_Object((1,3,6,1,4,1,9,9,1001,1,4,1,2),_AppRouteSlaClassName_Type())
appRouteSlaClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteSlaClassName.setStatus(_A)
_AppRouteSlaClassLoss_Type=UnsignedByte
_AppRouteSlaClassLoss_Object=MibTableColumn
appRouteSlaClassLoss=_AppRouteSlaClassLoss_Object((1,3,6,1,4,1,9,9,1001,1,4,1,3),_AppRouteSlaClassLoss_Type())
appRouteSlaClassLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteSlaClassLoss.setStatus(_A)
_AppRouteSlaClassLatency_Type=Unsigned32
_AppRouteSlaClassLatency_Object=MibTableColumn
appRouteSlaClassLatency=_AppRouteSlaClassLatency_Object((1,3,6,1,4,1,9,9,1001,1,4,1,4),_AppRouteSlaClassLatency_Type())
appRouteSlaClassLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteSlaClassLatency.setStatus(_A)
_AppRouteSlaClassJitter_Type=Unsigned32
_AppRouteSlaClassJitter_Object=MibTableColumn
appRouteSlaClassJitter=_AppRouteSlaClassJitter_Object((1,3,6,1,4,1,9,9,1001,1,4,1,5),_AppRouteSlaClassJitter_Type())
appRouteSlaClassJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteSlaClassJitter.setStatus(_A)
_AppRouteStatisticsAppProbeClassTable_Object=MibTable
appRouteStatisticsAppProbeClassTable=_AppRouteStatisticsAppProbeClassTable_Object((1,3,6,1,4,1,9,9,1001,1,5))
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassTable.setStatus(_A)
_AppRouteStatisticsAppProbeClassEntry_Object=MibTableRow
appRouteStatisticsAppProbeClassEntry=_AppRouteStatisticsAppProbeClassEntry_Object((1,3,6,1,4,1,9,9,1001,1,5,1))
appRouteStatisticsAppProbeClassEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassEntry.setStatus(_A)
class _AppRouteStatisticsAppProbeClassName_Type(String):subtypeSpec=String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AppRouteStatisticsAppProbeClassName_Type.__name__=_c
_AppRouteStatisticsAppProbeClassName_Object=MibTableColumn
appRouteStatisticsAppProbeClassName=_AppRouteStatisticsAppProbeClassName_Object((1,3,6,1,4,1,9,9,1001,1,5,1,1),_AppRouteStatisticsAppProbeClassName_Type())
appRouteStatisticsAppProbeClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassName.setStatus(_A)
_AppRouteStatisticsAppProbeClassMeanLoss_Type=UnsignedByte
_AppRouteStatisticsAppProbeClassMeanLoss_Object=MibTableColumn
appRouteStatisticsAppProbeClassMeanLoss=_AppRouteStatisticsAppProbeClassMeanLoss_Object((1,3,6,1,4,1,9,9,1001,1,5,1,2),_AppRouteStatisticsAppProbeClassMeanLoss_Type())
appRouteStatisticsAppProbeClassMeanLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassMeanLoss.setStatus(_A)
_AppRouteStatisticsAppProbeClassMeanLatency_Type=Unsigned32
_AppRouteStatisticsAppProbeClassMeanLatency_Object=MibTableColumn
appRouteStatisticsAppProbeClassMeanLatency=_AppRouteStatisticsAppProbeClassMeanLatency_Object((1,3,6,1,4,1,9,9,1001,1,5,1,3),_AppRouteStatisticsAppProbeClassMeanLatency_Type())
appRouteStatisticsAppProbeClassMeanLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassMeanLatency.setStatus(_A)
_AppRouteStatisticsAppProbeClassMeanJitter_Type=Unsigned32
_AppRouteStatisticsAppProbeClassMeanJitter_Object=MibTableColumn
appRouteStatisticsAppProbeClassMeanJitter=_AppRouteStatisticsAppProbeClassMeanJitter_Object((1,3,6,1,4,1,9,9,1001,1,5,1,4),_AppRouteStatisticsAppProbeClassMeanJitter_Type())
appRouteStatisticsAppProbeClassMeanJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassMeanJitter.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalTable_Object=MibTable
appRouteStatisticsAppProbeClassIntervalTable=_AppRouteStatisticsAppProbeClassIntervalTable_Object((1,3,6,1,4,1,9,9,1001,1,6))
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalTable.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalEntry_Object=MibTableRow
appRouteStatisticsAppProbeClassIntervalEntry=_AppRouteStatisticsAppProbeClassIntervalEntry_Object((1,3,6,1,4,1,9,9,1001,1,6,1))
appRouteStatisticsAppProbeClassIntervalEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_d))
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalEntry.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalIndex_Type=UnsignedByte
_AppRouteStatisticsAppProbeClassIntervalIndex_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalIndex=_AppRouteStatisticsAppProbeClassIntervalIndex_Object((1,3,6,1,4,1,9,9,1001,1,6,1,1),_AppRouteStatisticsAppProbeClassIntervalIndex_Type())
appRouteStatisticsAppProbeClassIntervalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalIndex.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Type=Integer32
_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalTotalPackets=_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Object((1,3,6,1,4,1,9,9,1001,1,6,1,2),_AppRouteStatisticsAppProbeClassIntervalTotalPackets_Type())
appRouteStatisticsAppProbeClassIntervalTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalTotalPackets.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalLoss_Type=Integer32
_AppRouteStatisticsAppProbeClassIntervalLoss_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalLoss=_AppRouteStatisticsAppProbeClassIntervalLoss_Object((1,3,6,1,4,1,9,9,1001,1,6,1,3),_AppRouteStatisticsAppProbeClassIntervalLoss_Type())
appRouteStatisticsAppProbeClassIntervalLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalLoss.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalAverageLatency=_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Object((1,3,6,1,4,1,9,9,1001,1,6,1,4),_AppRouteStatisticsAppProbeClassIntervalAverageLatency_Type())
appRouteStatisticsAppProbeClassIntervalAverageLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalAverageLatency.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalAverageJitter=_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Object((1,3,6,1,4,1,9,9,1001,1,6,1,5),_AppRouteStatisticsAppProbeClassIntervalAverageJitter_Type())
appRouteStatisticsAppProbeClassIntervalAverageJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalAverageJitter.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalTxDataPkts=_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Object((1,3,6,1,4,1,9,9,1001,1,6,1,6),_AppRouteStatisticsAppProbeClassIntervalTxDataPkts_Type())
appRouteStatisticsAppProbeClassIntervalTxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalTxDataPkts.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalRxDataPkts=_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Object((1,3,6,1,4,1,9,9,1001,1,6,1,7),_AppRouteStatisticsAppProbeClassIntervalRxDataPkts_Type())
appRouteStatisticsAppProbeClassIntervalRxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalRxDataPkts.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts=_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Object((1,3,6,1,4,1,9,9,1001,1,6,1,8),_AppRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts_Type())
appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts.setStatus(_A)
_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Type=Counter64
_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Object=MibTableColumn
appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts=_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Object((1,3,6,1,4,1,9,9,1001,1,6,1,9),_AppRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts_Type())
appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts.setStatus(_A)
_CiscoSdwanAppRouteMIBConform_ObjectIdentity=ObjectIdentity
ciscoSdwanAppRouteMIBConform=_CiscoSdwanAppRouteMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1001,3))
_CiscoSdwanAppRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSdwanAppRouteMIBCompliances=_CiscoSdwanAppRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1001,3,1))
_CiscoSdwanAppRouteMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSdwanAppRouteMIBGroups=_CiscoSdwanAppRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1001,3,2))
cSdwanAppRouteStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,1001,3,2,1))
cSdwanAppRouteStatisticsGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cSdwanAppRouteStatisticsGroup.setStatus(_A)
cSdwanAppRouteStatisticsAppProbeClassGroup=ObjectGroup((1,3,6,1,4,1,9,9,1001,3,2,2))
cSdwanAppRouteStatisticsAppProbeClassGroup.setObjects(*((_B,_K),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cSdwanAppRouteStatisticsAppProbeClassGroup.setStatus(_A)
cSdwanAppRouteStatisticsAppProbeClassIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,9,1001,3,2,3))
cSdwanAppRouteStatisticsAppProbeClassIntervalGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cSdwanAppRouteStatisticsAppProbeClassIntervalGroup.setStatus(_A)
cSdwanAppRouteSlaClassGroup=ObjectGroup((1,3,6,1,4,1,9,9,1001,3,2,4))
cSdwanAppRouteSlaClassGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cSdwanAppRouteSlaClassGroup.setStatus(_A)
ciscoSdwanAppRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1001,3,1,1))
ciscoSdwanAppRouteMIBCompliance.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoSdwanAppRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'UnsignedByte':UnsignedByte,'UnsignedShort':UnsignedShort,'ConfdString':ConfdString,_c:String,'InetAddressIP':InetAddressIP,'ciscoSdwanAppRouteMIB':ciscoSdwanAppRouteMIB,'ciscoSdwanAppRouteMIBObjects':ciscoSdwanAppRouteMIBObjects,'appRouteStatisticsTable':appRouteStatisticsTable,'appRouteStatisticsEntry':appRouteStatisticsEntry,_F:appRouteStatisticsSrcIp,_G:appRouteStatisticsDstIp,_H:appRouteStatisticsProto,_I:appRouteStatisticsSrcPort,_J:appRouteStatisticsDstPort,_e:appRouteStatisticsRemoteSystemIp,_f:appRouteStatisticsLocalColor,_g:appRouteStatisticsRemoteColor,'appRouteSlaClassTable':appRouteSlaClassTable,'appRouteSlaClassEntry':appRouteSlaClassEntry,_b:appRouteSlaClassIndex,_s:appRouteSlaClassName,_t:appRouteSlaClassLoss,_u:appRouteSlaClassLatency,_v:appRouteSlaClassJitter,'appRouteStatisticsAppProbeClassTable':appRouteStatisticsAppProbeClassTable,'appRouteStatisticsAppProbeClassEntry':appRouteStatisticsAppProbeClassEntry,_K:appRouteStatisticsAppProbeClassName,_h:appRouteStatisticsAppProbeClassMeanLoss,_i:appRouteStatisticsAppProbeClassMeanLatency,_j:appRouteStatisticsAppProbeClassMeanJitter,'appRouteStatisticsAppProbeClassIntervalTable':appRouteStatisticsAppProbeClassIntervalTable,'appRouteStatisticsAppProbeClassIntervalEntry':appRouteStatisticsAppProbeClassIntervalEntry,_d:appRouteStatisticsAppProbeClassIntervalIndex,_k:appRouteStatisticsAppProbeClassIntervalTotalPackets,_l:appRouteStatisticsAppProbeClassIntervalLoss,_m:appRouteStatisticsAppProbeClassIntervalAverageLatency,_n:appRouteStatisticsAppProbeClassIntervalAverageJitter,_o:appRouteStatisticsAppProbeClassIntervalTxDataPkts,_p:appRouteStatisticsAppProbeClassIntervalRxDataPkts,_q:appRouteStatisticsAppProbeClassIntervalIpv6TxDataPkts,_r:appRouteStatisticsAppProbeClassIntervalIpv6RxDataPkts,'ciscoSdwanAppRouteMIBConform':ciscoSdwanAppRouteMIBConform,'ciscoSdwanAppRouteMIBCompliances':ciscoSdwanAppRouteMIBCompliances,'ciscoSdwanAppRouteMIBCompliance':ciscoSdwanAppRouteMIBCompliance,'ciscoSdwanAppRouteMIBGroups':ciscoSdwanAppRouteMIBGroups,_w:cSdwanAppRouteStatisticsGroup,_x:cSdwanAppRouteStatisticsAppProbeClassGroup,_y:cSdwanAppRouteStatisticsAppProbeClassIntervalGroup,_z:cSdwanAppRouteSlaClassGroup})