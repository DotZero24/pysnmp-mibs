_A0='ciscoIPExtCtrlGroupRev2'
_z='cipslaPercentileLatestSum2'
_y='cipslaPercentileLatestSum'
_x='cipslaPercentileLatestNum'
_w='cipslaPercentileLatestAvg'
_v='cipslaPercentileLatestMax'
_u='cipslaPercentileLatestMin'
_t='cipslaPercentileJitterAvg'
_s='cipslaPercentileJitterDS'
_r='cipslaPercentileJitterSD'
_q='cipslaPercentileOWDS'
_p='cipslaPercentileOWSD'
_o='cipslaPercentileRTT'
_n='crttMonIPHistoryCollectionAddress'
_m='crttMonIPHistoryCollectionAddrType'
_l='crttMonIPLpdGrpStatsTargetPEAddr'
_k='crttMonIPLpdGrpStatsTargetPEAddrType'
_j='crttMonIPStatsCollectAddress'
_i='crttMonIPStatsCollectAddressType'
_h='crttMonIPEchoPathAdminHopAddress'
_g='crttMonIPEchoPathAdminHopAddrType'
_f='crttMonIPLatestRttOperAddress'
_e='crttMonIPLatestRttOperAddressType'
_d='crttMonIPEchoAdminFlowLabel'
_c='crttMonIPEchoAdminDscp'
_b='crttMonIPEchoAdminLSPSelAddress'
_a='crttMonIPEchoAdminLSPSelAddrType'
_Z='crttMonIPEchoAdminNameServerAddress'
_Y='crttMonIPEchoAdminNameServerAddrType'
_X='crttMonIPEchoAdminSourceAddress'
_W='crttMonIPEchoAdminSourceAddrType'
_V='crttMonIPEchoAdminTargetAddress'
_U='crttMonIPEchoAdminTargetAddrType'
_T='crttMonIPHistoryCollectionEntry'
_S='crttMonIPLpdGrpStatsEntry'
_R='crttMonIPStatsCollectEntry'
_Q='crttMonIPEchoPathAdminEntry'
_P='crttMonIPEchoAdminEntry'
_O='cipslaPercentileTypeVar'
_N='DscpOrAny'
_M='CipslaPercentileVar'
_L='ciscoIPExtCtrlGroupRev1'
_K='rttMonCtrlAdminIndex'
_J='CISCO-RTTMON-MIB'
_I='percent'
_H='Integer32'
_G='read-create'
_F='InetAddressType'
_E='InetAddress'
_D='read-only'
_C='read-write'
_B='CISCO-RTTMON-IP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rttMonCtrlAdminEntry,rttMonCtrlAdminIndex,rttMonCtrlOperEntry,rttMonEchoAdminEntry,rttMonEchoPathAdminEntry,rttMonHistoryCollectionEntry,rttMonLpdGrpStatsEntry,rttMonStatsCollectEntry=mibBuilder.importSymbols(_J,'rttMonCtrlAdminEntry',_K,'rttMonCtrlOperEntry','rttMonEchoAdminEntry','rttMonEchoPathAdminEntry','rttMonHistoryCollectionEntry','rttMonLpdGrpStatsEntry','rttMonStatsCollectEntry')
CipslaPercentileVar,=mibBuilder.importSymbols('CISCO-RTTMON-TC-MIB',_M)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
DscpOrAny,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC',_N)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,_F)
IPv6FlowLabelOrAny,=mibBuilder.importSymbols('IPV6-FLOW-LABEL-MIB','IPv6FlowLabelOrAny')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoRttMonIPExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,572))
if mibBuilder.loadTexts:ciscoRttMonIPExtMIB.setRevisions(('2018-04-09 00:00','2017-09-06 00:00','2006-08-02 00:00'))
_CrttMonIPExtObjects_ObjectIdentity=ObjectIdentity
crttMonIPExtObjects=_CrttMonIPExtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,572,1))
_CrttMonIPEchoAdminTable_Object=MibTable
crttMonIPEchoAdminTable=_CrttMonIPEchoAdminTable_Object((1,3,6,1,4,1,9,9,572,1,1))
if mibBuilder.loadTexts:crttMonIPEchoAdminTable.setStatus(_A)
_CrttMonIPEchoAdminEntry_Object=MibTableRow
crttMonIPEchoAdminEntry=_CrttMonIPEchoAdminEntry_Object((1,3,6,1,4,1,9,9,572,1,1,1))
if mibBuilder.loadTexts:crttMonIPEchoAdminEntry.setStatus(_A)
class _CrttMonIPEchoAdminTargetAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPEchoAdminTargetAddrType_Type.__name__=_F
_CrttMonIPEchoAdminTargetAddrType_Object=MibTableColumn
crttMonIPEchoAdminTargetAddrType=_CrttMonIPEchoAdminTargetAddrType_Object((1,3,6,1,4,1,9,9,572,1,1,1,1),_CrttMonIPEchoAdminTargetAddrType_Type())
crttMonIPEchoAdminTargetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminTargetAddrType.setStatus(_A)
class _CrttMonIPEchoAdminTargetAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPEchoAdminTargetAddress_Type.__name__=_E
_CrttMonIPEchoAdminTargetAddress_Object=MibTableColumn
crttMonIPEchoAdminTargetAddress=_CrttMonIPEchoAdminTargetAddress_Object((1,3,6,1,4,1,9,9,572,1,1,1,2),_CrttMonIPEchoAdminTargetAddress_Type())
crttMonIPEchoAdminTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminTargetAddress.setStatus(_A)
class _CrttMonIPEchoAdminSourceAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPEchoAdminSourceAddrType_Type.__name__=_F
_CrttMonIPEchoAdminSourceAddrType_Object=MibTableColumn
crttMonIPEchoAdminSourceAddrType=_CrttMonIPEchoAdminSourceAddrType_Object((1,3,6,1,4,1,9,9,572,1,1,1,3),_CrttMonIPEchoAdminSourceAddrType_Type())
crttMonIPEchoAdminSourceAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminSourceAddrType.setStatus(_A)
class _CrttMonIPEchoAdminSourceAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPEchoAdminSourceAddress_Type.__name__=_E
_CrttMonIPEchoAdminSourceAddress_Object=MibTableColumn
crttMonIPEchoAdminSourceAddress=_CrttMonIPEchoAdminSourceAddress_Object((1,3,6,1,4,1,9,9,572,1,1,1,4),_CrttMonIPEchoAdminSourceAddress_Type())
crttMonIPEchoAdminSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminSourceAddress.setStatus(_A)
class _CrttMonIPEchoAdminNameServerAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPEchoAdminNameServerAddrType_Type.__name__=_F
_CrttMonIPEchoAdminNameServerAddrType_Object=MibTableColumn
crttMonIPEchoAdminNameServerAddrType=_CrttMonIPEchoAdminNameServerAddrType_Object((1,3,6,1,4,1,9,9,572,1,1,1,5),_CrttMonIPEchoAdminNameServerAddrType_Type())
crttMonIPEchoAdminNameServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminNameServerAddrType.setStatus(_A)
class _CrttMonIPEchoAdminNameServerAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPEchoAdminNameServerAddress_Type.__name__=_E
_CrttMonIPEchoAdminNameServerAddress_Object=MibTableColumn
crttMonIPEchoAdminNameServerAddress=_CrttMonIPEchoAdminNameServerAddress_Object((1,3,6,1,4,1,9,9,572,1,1,1,6),_CrttMonIPEchoAdminNameServerAddress_Type())
crttMonIPEchoAdminNameServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminNameServerAddress.setStatus(_A)
class _CrttMonIPEchoAdminLSPSelAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPEchoAdminLSPSelAddrType_Type.__name__=_F
_CrttMonIPEchoAdminLSPSelAddrType_Object=MibTableColumn
crttMonIPEchoAdminLSPSelAddrType=_CrttMonIPEchoAdminLSPSelAddrType_Object((1,3,6,1,4,1,9,9,572,1,1,1,7),_CrttMonIPEchoAdminLSPSelAddrType_Type())
crttMonIPEchoAdminLSPSelAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminLSPSelAddrType.setStatus(_A)
class _CrttMonIPEchoAdminLSPSelAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPEchoAdminLSPSelAddress_Type.__name__=_E
_CrttMonIPEchoAdminLSPSelAddress_Object=MibTableColumn
crttMonIPEchoAdminLSPSelAddress=_CrttMonIPEchoAdminLSPSelAddress_Object((1,3,6,1,4,1,9,9,572,1,1,1,8),_CrttMonIPEchoAdminLSPSelAddress_Type())
crttMonIPEchoAdminLSPSelAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminLSPSelAddress.setStatus(_A)
class _CrttMonIPEchoAdminDscp_Type(DscpOrAny):defaultValue=-1
_CrttMonIPEchoAdminDscp_Type.__name__=_N
_CrttMonIPEchoAdminDscp_Object=MibTableColumn
crttMonIPEchoAdminDscp=_CrttMonIPEchoAdminDscp_Object((1,3,6,1,4,1,9,9,572,1,1,1,9),_CrttMonIPEchoAdminDscp_Type())
crttMonIPEchoAdminDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminDscp.setStatus(_A)
_CrttMonIPEchoAdminFlowLabel_Type=IPv6FlowLabelOrAny
_CrttMonIPEchoAdminFlowLabel_Object=MibTableColumn
crttMonIPEchoAdminFlowLabel=_CrttMonIPEchoAdminFlowLabel_Object((1,3,6,1,4,1,9,9,572,1,1,1,10),_CrttMonIPEchoAdminFlowLabel_Type())
crttMonIPEchoAdminFlowLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoAdminFlowLabel.setStatus(_A)
_CrttMonIPLatestRttOperTable_Object=MibTable
crttMonIPLatestRttOperTable=_CrttMonIPLatestRttOperTable_Object((1,3,6,1,4,1,9,9,572,1,2))
if mibBuilder.loadTexts:crttMonIPLatestRttOperTable.setStatus(_A)
_CrttMonIPLatestRttOperEntry_Object=MibTableRow
crttMonIPLatestRttOperEntry=_CrttMonIPLatestRttOperEntry_Object((1,3,6,1,4,1,9,9,572,1,2,1))
crttMonIPLatestRttOperEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:crttMonIPLatestRttOperEntry.setStatus(_A)
class _CrttMonIPLatestRttOperAddressType_Type(InetAddressType):defaultValue=0
_CrttMonIPLatestRttOperAddressType_Type.__name__=_F
_CrttMonIPLatestRttOperAddressType_Object=MibTableColumn
crttMonIPLatestRttOperAddressType=_CrttMonIPLatestRttOperAddressType_Object((1,3,6,1,4,1,9,9,572,1,2,1,1),_CrttMonIPLatestRttOperAddressType_Type())
crttMonIPLatestRttOperAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:crttMonIPLatestRttOperAddressType.setStatus(_A)
class _CrttMonIPLatestRttOperAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPLatestRttOperAddress_Type.__name__=_E
_CrttMonIPLatestRttOperAddress_Object=MibTableColumn
crttMonIPLatestRttOperAddress=_CrttMonIPLatestRttOperAddress_Object((1,3,6,1,4,1,9,9,572,1,2,1,2),_CrttMonIPLatestRttOperAddress_Type())
crttMonIPLatestRttOperAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:crttMonIPLatestRttOperAddress.setStatus(_A)
_CrttMonIPEchoPathAdminTable_Object=MibTable
crttMonIPEchoPathAdminTable=_CrttMonIPEchoPathAdminTable_Object((1,3,6,1,4,1,9,9,572,1,3))
if mibBuilder.loadTexts:crttMonIPEchoPathAdminTable.setStatus(_A)
_CrttMonIPEchoPathAdminEntry_Object=MibTableRow
crttMonIPEchoPathAdminEntry=_CrttMonIPEchoPathAdminEntry_Object((1,3,6,1,4,1,9,9,572,1,3,1))
if mibBuilder.loadTexts:crttMonIPEchoPathAdminEntry.setStatus(_A)
class _CrttMonIPEchoPathAdminHopAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPEchoPathAdminHopAddrType_Type.__name__=_F
_CrttMonIPEchoPathAdminHopAddrType_Object=MibTableColumn
crttMonIPEchoPathAdminHopAddrType=_CrttMonIPEchoPathAdminHopAddrType_Object((1,3,6,1,4,1,9,9,572,1,3,1,1),_CrttMonIPEchoPathAdminHopAddrType_Type())
crttMonIPEchoPathAdminHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoPathAdminHopAddrType.setStatus(_A)
class _CrttMonIPEchoPathAdminHopAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPEchoPathAdminHopAddress_Type.__name__=_E
_CrttMonIPEchoPathAdminHopAddress_Object=MibTableColumn
crttMonIPEchoPathAdminHopAddress=_CrttMonIPEchoPathAdminHopAddress_Object((1,3,6,1,4,1,9,9,572,1,3,1,2),_CrttMonIPEchoPathAdminHopAddress_Type())
crttMonIPEchoPathAdminHopAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:crttMonIPEchoPathAdminHopAddress.setStatus(_A)
_CrttMonIPStatsCollectTable_Object=MibTable
crttMonIPStatsCollectTable=_CrttMonIPStatsCollectTable_Object((1,3,6,1,4,1,9,9,572,1,4))
if mibBuilder.loadTexts:crttMonIPStatsCollectTable.setStatus(_A)
_CrttMonIPStatsCollectEntry_Object=MibTableRow
crttMonIPStatsCollectEntry=_CrttMonIPStatsCollectEntry_Object((1,3,6,1,4,1,9,9,572,1,4,1))
if mibBuilder.loadTexts:crttMonIPStatsCollectEntry.setStatus(_A)
class _CrttMonIPStatsCollectAddressType_Type(InetAddressType):defaultValue=0
_CrttMonIPStatsCollectAddressType_Type.__name__=_F
_CrttMonIPStatsCollectAddressType_Object=MibTableColumn
crttMonIPStatsCollectAddressType=_CrttMonIPStatsCollectAddressType_Object((1,3,6,1,4,1,9,9,572,1,4,1,1),_CrttMonIPStatsCollectAddressType_Type())
crttMonIPStatsCollectAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPStatsCollectAddressType.setStatus(_A)
class _CrttMonIPStatsCollectAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPStatsCollectAddress_Type.__name__=_E
_CrttMonIPStatsCollectAddress_Object=MibTableColumn
crttMonIPStatsCollectAddress=_CrttMonIPStatsCollectAddress_Object((1,3,6,1,4,1,9,9,572,1,4,1,2),_CrttMonIPStatsCollectAddress_Type())
crttMonIPStatsCollectAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPStatsCollectAddress.setStatus(_A)
_CrttMonIPLpdGrpStatsTable_Object=MibTable
crttMonIPLpdGrpStatsTable=_CrttMonIPLpdGrpStatsTable_Object((1,3,6,1,4,1,9,9,572,1,5))
if mibBuilder.loadTexts:crttMonIPLpdGrpStatsTable.setStatus(_A)
_CrttMonIPLpdGrpStatsEntry_Object=MibTableRow
crttMonIPLpdGrpStatsEntry=_CrttMonIPLpdGrpStatsEntry_Object((1,3,6,1,4,1,9,9,572,1,5,1))
if mibBuilder.loadTexts:crttMonIPLpdGrpStatsEntry.setStatus(_A)
class _CrttMonIPLpdGrpStatsTargetPEAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPLpdGrpStatsTargetPEAddrType_Type.__name__=_F
_CrttMonIPLpdGrpStatsTargetPEAddrType_Object=MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddrType=_CrttMonIPLpdGrpStatsTargetPEAddrType_Object((1,3,6,1,4,1,9,9,572,1,5,1,1),_CrttMonIPLpdGrpStatsTargetPEAddrType_Type())
crttMonIPLpdGrpStatsTargetPEAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPLpdGrpStatsTargetPEAddrType.setStatus(_A)
class _CrttMonIPLpdGrpStatsTargetPEAddr_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPLpdGrpStatsTargetPEAddr_Type.__name__=_E
_CrttMonIPLpdGrpStatsTargetPEAddr_Object=MibTableColumn
crttMonIPLpdGrpStatsTargetPEAddr=_CrttMonIPLpdGrpStatsTargetPEAddr_Object((1,3,6,1,4,1,9,9,572,1,5,1,2),_CrttMonIPLpdGrpStatsTargetPEAddr_Type())
crttMonIPLpdGrpStatsTargetPEAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPLpdGrpStatsTargetPEAddr.setStatus(_A)
_CrttMonIPHistoryCollectionTable_Object=MibTable
crttMonIPHistoryCollectionTable=_CrttMonIPHistoryCollectionTable_Object((1,3,6,1,4,1,9,9,572,1,6))
if mibBuilder.loadTexts:crttMonIPHistoryCollectionTable.setStatus(_A)
_CrttMonIPHistoryCollectionEntry_Object=MibTableRow
crttMonIPHistoryCollectionEntry=_CrttMonIPHistoryCollectionEntry_Object((1,3,6,1,4,1,9,9,572,1,6,1))
if mibBuilder.loadTexts:crttMonIPHistoryCollectionEntry.setStatus(_A)
class _CrttMonIPHistoryCollectionAddrType_Type(InetAddressType):defaultValue=0
_CrttMonIPHistoryCollectionAddrType_Type.__name__=_F
_CrttMonIPHistoryCollectionAddrType_Object=MibTableColumn
crttMonIPHistoryCollectionAddrType=_CrttMonIPHistoryCollectionAddrType_Object((1,3,6,1,4,1,9,9,572,1,6,1,1),_CrttMonIPHistoryCollectionAddrType_Type())
crttMonIPHistoryCollectionAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPHistoryCollectionAddrType.setStatus(_A)
class _CrttMonIPHistoryCollectionAddress_Type(InetAddress):defaultValue=OctetString('')
_CrttMonIPHistoryCollectionAddress_Type.__name__=_E
_CrttMonIPHistoryCollectionAddress_Object=MibTableColumn
crttMonIPHistoryCollectionAddress=_CrttMonIPHistoryCollectionAddress_Object((1,3,6,1,4,1,9,9,572,1,6,1,2),_CrttMonIPHistoryCollectionAddress_Type())
crttMonIPHistoryCollectionAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:crttMonIPHistoryCollectionAddress.setStatus(_A)
_CipslaPercentileConfigTable_Object=MibTable
cipslaPercentileConfigTable=_CipslaPercentileConfigTable_Object((1,3,6,1,4,1,9,9,572,1,7))
if mibBuilder.loadTexts:cipslaPercentileConfigTable.setStatus(_A)
_CipslaPercentileConfigEntry_Object=MibTableRow
cipslaPercentileConfigEntry=_CipslaPercentileConfigEntry_Object((1,3,6,1,4,1,9,9,572,1,7,1))
cipslaPercentileConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cipslaPercentileConfigEntry.setStatus(_A)
class _CipslaPercentileRTT_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileRTT_Type.__name__=_H
_CipslaPercentileRTT_Object=MibTableColumn
cipslaPercentileRTT=_CipslaPercentileRTT_Object((1,3,6,1,4,1,9,9,572,1,7,1,1),_CipslaPercentileRTT_Type())
cipslaPercentileRTT.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileRTT.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileRTT.setUnits(_I)
class _CipslaPercentileOWSD_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileOWSD_Type.__name__=_H
_CipslaPercentileOWSD_Object=MibTableColumn
cipslaPercentileOWSD=_CipslaPercentileOWSD_Object((1,3,6,1,4,1,9,9,572,1,7,1,2),_CipslaPercentileOWSD_Type())
cipslaPercentileOWSD.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileOWSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileOWSD.setUnits(_I)
class _CipslaPercentileOWDS_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileOWDS_Type.__name__=_H
_CipslaPercentileOWDS_Object=MibTableColumn
cipslaPercentileOWDS=_CipslaPercentileOWDS_Object((1,3,6,1,4,1,9,9,572,1,7,1,3),_CipslaPercentileOWDS_Type())
cipslaPercentileOWDS.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileOWDS.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileOWDS.setUnits(_I)
class _CipslaPercentileJitterSD_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileJitterSD_Type.__name__=_H
_CipslaPercentileJitterSD_Object=MibTableColumn
cipslaPercentileJitterSD=_CipslaPercentileJitterSD_Object((1,3,6,1,4,1,9,9,572,1,7,1,4),_CipslaPercentileJitterSD_Type())
cipslaPercentileJitterSD.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileJitterSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileJitterSD.setUnits(_I)
class _CipslaPercentileJitterDS_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileJitterDS_Type.__name__=_H
_CipslaPercentileJitterDS_Object=MibTableColumn
cipslaPercentileJitterDS=_CipslaPercentileJitterDS_Object((1,3,6,1,4,1,9,9,572,1,7,1,5),_CipslaPercentileJitterDS_Type())
cipslaPercentileJitterDS.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileJitterDS.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileJitterDS.setUnits(_I)
class _CipslaPercentileJitterAvg_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,100))
_CipslaPercentileJitterAvg_Type.__name__=_H
_CipslaPercentileJitterAvg_Object=MibTableColumn
cipslaPercentileJitterAvg=_CipslaPercentileJitterAvg_Object((1,3,6,1,4,1,9,9,572,1,7,1,6),_CipslaPercentileJitterAvg_Type())
cipslaPercentileJitterAvg.setMaxAccess(_G)
if mibBuilder.loadTexts:cipslaPercentileJitterAvg.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileJitterAvg.setUnits(_I)
_CipslaPercentileLatestStatsTable_Object=MibTable
cipslaPercentileLatestStatsTable=_CipslaPercentileLatestStatsTable_Object((1,3,6,1,4,1,9,9,572,1,8))
if mibBuilder.loadTexts:cipslaPercentileLatestStatsTable.setStatus(_A)
_CipslaPercentileLatestStatsEntry_Object=MibTableRow
cipslaPercentileLatestStatsEntry=_CipslaPercentileLatestStatsEntry_Object((1,3,6,1,4,1,9,9,572,1,8,1))
cipslaPercentileLatestStatsEntry.setIndexNames((0,_B,_O),(0,_J,_K))
if mibBuilder.loadTexts:cipslaPercentileLatestStatsEntry.setStatus(_A)
class _CipslaPercentileTypeVar_Type(CipslaPercentileVar):subtypeSpec=CipslaPercentileVar.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('rtt',1),('owsd',2),('owds',3),('jittersd',4),('jitterds',5),('jitteravg',6)))
_CipslaPercentileTypeVar_Type.__name__=_M
_CipslaPercentileTypeVar_Object=MibTableColumn
cipslaPercentileTypeVar=_CipslaPercentileTypeVar_Object((1,3,6,1,4,1,9,9,572,1,8,1,1),_CipslaPercentileTypeVar_Type())
cipslaPercentileTypeVar.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cipslaPercentileTypeVar.setStatus(_A)
_CipslaPercentileLatestMin_Type=Gauge32
_CipslaPercentileLatestMin_Object=MibTableColumn
cipslaPercentileLatestMin=_CipslaPercentileLatestMin_Object((1,3,6,1,4,1,9,9,572,1,8,1,2),_CipslaPercentileLatestMin_Type())
cipslaPercentileLatestMin.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestMin.setStatus(_A)
_CipslaPercentileLatestMax_Type=Gauge32
_CipslaPercentileLatestMax_Object=MibTableColumn
cipslaPercentileLatestMax=_CipslaPercentileLatestMax_Object((1,3,6,1,4,1,9,9,572,1,8,1,3),_CipslaPercentileLatestMax_Type())
cipslaPercentileLatestMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestMax.setStatus(_A)
_CipslaPercentileLatestAvg_Type=Gauge32
_CipslaPercentileLatestAvg_Object=MibTableColumn
cipslaPercentileLatestAvg=_CipslaPercentileLatestAvg_Object((1,3,6,1,4,1,9,9,572,1,8,1,4),_CipslaPercentileLatestAvg_Type())
cipslaPercentileLatestAvg.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestAvg.setStatus(_A)
_CipslaPercentileLatestNum_Type=Gauge32
_CipslaPercentileLatestNum_Object=MibTableColumn
cipslaPercentileLatestNum=_CipslaPercentileLatestNum_Object((1,3,6,1,4,1,9,9,572,1,8,1,5),_CipslaPercentileLatestNum_Type())
cipslaPercentileLatestNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestNum.setStatus(_A)
if mibBuilder.loadTexts:cipslaPercentileLatestNum.setUnits('packets')
_CipslaPercentileLatestSum_Type=Gauge32
_CipslaPercentileLatestSum_Object=MibTableColumn
cipslaPercentileLatestSum=_CipslaPercentileLatestSum_Object((1,3,6,1,4,1,9,9,572,1,8,1,6),_CipslaPercentileLatestSum_Type())
cipslaPercentileLatestSum.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestSum.setStatus(_A)
_CipslaPercentileLatestSum2_Type=Gauge32
_CipslaPercentileLatestSum2_Object=MibTableColumn
cipslaPercentileLatestSum2=_CipslaPercentileLatestSum2_Object((1,3,6,1,4,1,9,9,572,1,8,1,7),_CipslaPercentileLatestSum2_Type())
cipslaPercentileLatestSum2.setMaxAccess(_D)
if mibBuilder.loadTexts:cipslaPercentileLatestSum2.setStatus(_A)
_CiscoRttMonIPExtMibConformance_ObjectIdentity=ObjectIdentity
ciscoRttMonIPExtMibConformance=_CiscoRttMonIPExtMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,572,2))
_CiscoRttMonIPExtMibCompliances_ObjectIdentity=ObjectIdentity
ciscoRttMonIPExtMibCompliances=_CiscoRttMonIPExtMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,572,2,1))
_CiscoRttMonIPExtMibGroups_ObjectIdentity=ObjectIdentity
ciscoRttMonIPExtMibGroups=_CiscoRttMonIPExtMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,572,2,2))
rttMonEchoAdminEntry.registerAugmentions((_B,_P))
crttMonIPEchoAdminEntry.setIndexNames(*rttMonEchoAdminEntry.getIndexNames())
rttMonEchoPathAdminEntry.registerAugmentions((_B,_Q))
crttMonIPEchoPathAdminEntry.setIndexNames(*rttMonEchoPathAdminEntry.getIndexNames())
rttMonStatsCollectEntry.registerAugmentions((_B,_R))
crttMonIPStatsCollectEntry.setIndexNames(*rttMonStatsCollectEntry.getIndexNames())
rttMonLpdGrpStatsEntry.registerAugmentions((_B,_S))
crttMonIPLpdGrpStatsEntry.setIndexNames(*rttMonLpdGrpStatsEntry.getIndexNames())
rttMonHistoryCollectionEntry.registerAugmentions((_B,_T))
crttMonIPHistoryCollectionEntry.setIndexNames(*rttMonHistoryCollectionEntry.getIndexNames())
ciscoIPExtCtrlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,572,2,2,1))
ciscoIPExtCtrlGroupRev1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoIPExtCtrlGroupRev1.setStatus(_A)
ciscoIPExtCtrlGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,572,2,2,2))
ciscoIPExtCtrlGroupRev2.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoIPExtCtrlGroupRev2.setStatus(_A)
ciscoRttMonIPExtMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,572,2,1,1))
ciscoRttMonIPExtMibComplianceRev1.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoRttMonIPExtMibComplianceRev1.setStatus('deprecated')
ciscoRttMonIPExtMibComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,572,2,1,2))
ciscoRttMonIPExtMibComplianceRev2.setObjects(*((_B,_L),(_B,_A0)))
if mibBuilder.loadTexts:ciscoRttMonIPExtMibComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoRttMonIPExtMIB':ciscoRttMonIPExtMIB,'crttMonIPExtObjects':crttMonIPExtObjects,'crttMonIPEchoAdminTable':crttMonIPEchoAdminTable,_P:crttMonIPEchoAdminEntry,_U:crttMonIPEchoAdminTargetAddrType,_V:crttMonIPEchoAdminTargetAddress,_W:crttMonIPEchoAdminSourceAddrType,_X:crttMonIPEchoAdminSourceAddress,_Y:crttMonIPEchoAdminNameServerAddrType,_Z:crttMonIPEchoAdminNameServerAddress,_a:crttMonIPEchoAdminLSPSelAddrType,_b:crttMonIPEchoAdminLSPSelAddress,_c:crttMonIPEchoAdminDscp,_d:crttMonIPEchoAdminFlowLabel,'crttMonIPLatestRttOperTable':crttMonIPLatestRttOperTable,'crttMonIPLatestRttOperEntry':crttMonIPLatestRttOperEntry,_e:crttMonIPLatestRttOperAddressType,_f:crttMonIPLatestRttOperAddress,'crttMonIPEchoPathAdminTable':crttMonIPEchoPathAdminTable,_Q:crttMonIPEchoPathAdminEntry,_g:crttMonIPEchoPathAdminHopAddrType,_h:crttMonIPEchoPathAdminHopAddress,'crttMonIPStatsCollectTable':crttMonIPStatsCollectTable,_R:crttMonIPStatsCollectEntry,_i:crttMonIPStatsCollectAddressType,_j:crttMonIPStatsCollectAddress,'crttMonIPLpdGrpStatsTable':crttMonIPLpdGrpStatsTable,_S:crttMonIPLpdGrpStatsEntry,_k:crttMonIPLpdGrpStatsTargetPEAddrType,_l:crttMonIPLpdGrpStatsTargetPEAddr,'crttMonIPHistoryCollectionTable':crttMonIPHistoryCollectionTable,_T:crttMonIPHistoryCollectionEntry,_m:crttMonIPHistoryCollectionAddrType,_n:crttMonIPHistoryCollectionAddress,'cipslaPercentileConfigTable':cipslaPercentileConfigTable,'cipslaPercentileConfigEntry':cipslaPercentileConfigEntry,_o:cipslaPercentileRTT,_p:cipslaPercentileOWSD,_q:cipslaPercentileOWDS,_r:cipslaPercentileJitterSD,_s:cipslaPercentileJitterDS,_t:cipslaPercentileJitterAvg,'cipslaPercentileLatestStatsTable':cipslaPercentileLatestStatsTable,'cipslaPercentileLatestStatsEntry':cipslaPercentileLatestStatsEntry,_O:cipslaPercentileTypeVar,_u:cipslaPercentileLatestMin,_v:cipslaPercentileLatestMax,_w:cipslaPercentileLatestAvg,_x:cipslaPercentileLatestNum,_y:cipslaPercentileLatestSum,_z:cipslaPercentileLatestSum2,'ciscoRttMonIPExtMibConformance':ciscoRttMonIPExtMibConformance,'ciscoRttMonIPExtMibCompliances':ciscoRttMonIPExtMibCompliances,'ciscoRttMonIPExtMibComplianceRev1':ciscoRttMonIPExtMibComplianceRev1,'ciscoRttMonIPExtMibComplianceRev2':ciscoRttMonIPExtMibComplianceRev2,'ciscoRttMonIPExtMibGroups':ciscoRttMonIPExtMibGroups,_L:ciscoIPExtCtrlGroupRev1,_A0:ciscoIPExtCtrlGroupRev2})