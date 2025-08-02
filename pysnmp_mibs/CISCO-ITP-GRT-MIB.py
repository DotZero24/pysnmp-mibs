_B8='ciscoGrtInstGroupSup1'
_B7='ciscoGrtNotificationsGroupRev1'
_B6='ciscoGrtOrigSIGroup'
_B5='ciscoGrtDestSIGroup'
_B4='ciscoGrtOrigGroup'
_B3='ciscoGrtRouteGroupRev1'
_B2='ciscoGrtDestGroupRev1'
_B1='ciscoGrtScalarsGroup'
_B0='ciscoGrtNotificationsGroup'
_A_='ciscoGrtRouteGroup'
_Az='ciscoGrtDestGroup'
_Ay='ciscoGrtNoRouteMSUDiscards'
_Ax='ciscoGrtMgmtStateChangeRev1'
_Aw='ciscoGrtDestStateChangeRev1'
_Av='ciscoGrtMgmtStateChange'
_Au='ciscoGrtDestStateChange'
_At='cgrtInstNoRouteDrops'
_As='cgrtInstUnknownOrigPCs'
_Ar='cgrtNoRouteMSUsNotifWindowTime'
_Aq='cgrtNoRouteMSUsNotifEnabled'
_Ap='cgrtOrigSIDisplay'
_Ao='cgrtOrigSIOctets'
_An='cgrtOrigSIMSUs'
_Am='cgrtDestSIDisplay'
_Al='cgrtDestSIOctetsIn'
_Ak='cgrtDestSIMSUsIn'
_Aj='cgrtDestSIOctetsOut'
_Ai='cgrtDestSIMSUsOut'
_Ah='cgrtOrigDisplay'
_Ag='cgrtOrigOctets'
_Af='cgrtOrigMSUs'
_Ae='cgrtOrigTableEnabled'
_Ad='cgrtRouteProhibitedSeconds'
_Ac='cgrtRouteRestrictedSeconds'
_Ab='cgrtRouteAllowedSeconds'
_Aa='cgrtMgmtNotifEnabledRev1'
_AZ='cgrtMgmtNotifMaxPerWindowRev1'
_AY='cgrtMgmtNotifWindowTimeRev1'
_AX='cgrtDestCongestionDrops'
_AW='cgrtDestInaccessibleDrops'
_AV='cgrtDestRestrictedMSUs'
_AU='cgrtDestOctetsIn'
_AT='cgrtDestMSUsIn'
_AS='cgrtDestOctetsOut'
_AR='cgrtDestMSUsOut'
_AQ='cgrtDestRestrictedSeconds'
_AP='cgrtDestInaccessibleSeconds'
_AO='cgrtDestAccessibleSeconds'
_AN='cgrtDestNotifEnabledRev1'
_AM='cgrtDestNotifMaxPerWindowRev1'
_AL='cgrtDestNotifWindowTimeRev1'
_AK='cgrtPCStatsInterval'
_AJ='cgrtMgmtNotifEnabled'
_AI='cgrtMgmtNotifMaxPerWindow'
_AH='cgrtMgmtNotifWindowTime'
_AG='cgrtMgmtNotifDelayTime'
_AF='cgrtDestNotifEnabled'
_AE='cgrtDestNotifMaxPerWindow'
_AD='cgrtDestNotifWindowTime'
_AC='cgrtDestNotifDelayTime'
_AB='cgrtRouteTableLoadNotifEnabled'
_AA='cgrtInstNumberRoutes'
_A9='cgrtInstNumberDestinations'
_A8='cgrtInstLastLoadTime'
_A7='cgrtInstLastChanged'
_A6='occurrences'
_A5='unavailable'
_A4='available'
_A3='cgrtRouteDestLinkset'
_A2='cgrtRouteDestLsCost'
_A1='cgspInstDisplayName'
_A0='ciscoGrtInstGroup'
_z='ciscoGrtRouteTableLoad'
_y='cgrtIntervalNoRouteMSUs'
_x='cgrtNoRouteMSUsInterval'
_w='cgrtRouteDisplay'
_v='cgrtRouteNotifSuppressed'
_u='cgrtDestDisplay'
_t='cgrtDestNotifSuppressed'
_s='cgrtRouteRowStatus'
_r='cgrtRouteType'
_q='cgrtRouteQos'
_p='cgrtDynamicRoutesDropped'
_o='cgrtDynamicRoutes'
_n='cgrtMgmtNotifChanges'
_m='cgrtMgmtNotifSupFlag'
_l='cgrtRouteMaxDynamic'
_k='cgrtDestNotifChanges'
_j='cgrtDestNotifSupFlag'
_i='cgrtInstLastURL'
_h='cgrtInstTableName'
_g='cgrtInstLoadStatus'
_f='cgrtMtp3SI'
_e='cgrtOrigPC'
_d='deleted'
_c='OctetString'
_b='cgrtRouteAdminStatus'
_a='cgrtRouteDynamic'
_Z='cgrtRouteMgmtStatus'
_Y='cgrtRouteStatus'
_X='cgrtDestCongestion'
_W='cgrtDestStatus'
_V='restricted'
_U='cgrtRouteDpc'
_T='read-create'
_S='unknown'
_R='not-accessible'
_Q='octets'
_P='cgrtRouteMask'
_O='Unsigned32'
_N='cgspInstNetwork'
_M='cgspEventSequenceNumber'
_L='cgspCLLICode'
_K='accessible-for-notify'
_J='TruthValue'
_I='MSUs'
_H='seconds'
_G='Integer32'
_F='deprecated'
_E='read-write'
_D='CISCO-ITP-GSP-MIB'
_C='read-only'
_B='current'
_A='CISCO-ITP-GRT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_c,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgspCLLICode,cgspEventSequenceNumber,cgspInstDisplayName,cgspInstNetwork=mibBuilder.importSymbols(_D,_L,_M,_A1,_N)
CItpTcDisplayPC,CItpTcLinksetId,CItpTcPointCode,CItpTcQos,CItpTcRouteTableName,CItpTcServiceIndicator,CItpTcTableLoadStatus,CItpTcURL=mibBuilder.importSymbols('CISCO-ITP-TC-MIB','CItpTcDisplayPC','CItpTcLinksetId','CItpTcPointCode','CItpTcQos','CItpTcRouteTableName','CItpTcServiceIndicator','CItpTcTableLoadStatus','CItpTcURL')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_J)
ciscoGrtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,334))
if mibBuilder.loadTexts:ciscoGrtMIB.setRevisions(('2008-05-01 00:00','2003-03-03 00:00'))
class CgrtDisplayPCSI(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CiscoGrtNotifications_ObjectIdentity=ObjectIdentity
ciscoGrtNotifications=_CiscoGrtNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,334,0))
_CiscoGrtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGrtMIBObjects=_CiscoGrtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,334,1))
_CgrtScalars_ObjectIdentity=ObjectIdentity
cgrtScalars=_CgrtScalars_ObjectIdentity((1,3,6,1,4,1,9,9,334,1,1))
class _CgrtRouteMaxDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CgrtRouteMaxDynamic_Type.__name__=_G
_CgrtRouteMaxDynamic_Object=MibScalar
cgrtRouteMaxDynamic=_CgrtRouteMaxDynamic_Object((1,3,6,1,4,1,9,9,334,1,1,7),_CgrtRouteMaxDynamic_Type())
cgrtRouteMaxDynamic.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtRouteMaxDynamic.setStatus(_B)
class _CgrtDestNotifDelayTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CgrtDestNotifDelayTime_Type.__name__=_O
_CgrtDestNotifDelayTime_Object=MibScalar
cgrtDestNotifDelayTime=_CgrtDestNotifDelayTime_Object((1,3,6,1,4,1,9,9,334,1,1,11),_CgrtDestNotifDelayTime_Type())
cgrtDestNotifDelayTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifDelayTime.setStatus(_F)
if mibBuilder.loadTexts:cgrtDestNotifDelayTime.setUnits(_H)
class _CgrtDestNotifWindowTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,900))
_CgrtDestNotifWindowTime_Type.__name__=_G
_CgrtDestNotifWindowTime_Object=MibScalar
cgrtDestNotifWindowTime=_CgrtDestNotifWindowTime_Object((1,3,6,1,4,1,9,9,334,1,1,12),_CgrtDestNotifWindowTime_Type())
cgrtDestNotifWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifWindowTime.setStatus(_F)
if mibBuilder.loadTexts:cgrtDestNotifWindowTime.setUnits(_H)
class _CgrtDestNotifMaxPerWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,9000))
_CgrtDestNotifMaxPerWindow_Type.__name__=_G
_CgrtDestNotifMaxPerWindow_Object=MibScalar
cgrtDestNotifMaxPerWindow=_CgrtDestNotifMaxPerWindow_Object((1,3,6,1,4,1,9,9,334,1,1,13),_CgrtDestNotifMaxPerWindow_Type())
cgrtDestNotifMaxPerWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifMaxPerWindow.setStatus(_F)
class _CgrtDestNotifEnabled_Type(TruthValue):defaultValue=2
_CgrtDestNotifEnabled_Type.__name__=_J
_CgrtDestNotifEnabled_Object=MibScalar
cgrtDestNotifEnabled=_CgrtDestNotifEnabled_Object((1,3,6,1,4,1,9,9,334,1,1,14),_CgrtDestNotifEnabled_Type())
cgrtDestNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifEnabled.setStatus(_F)
class _CgrtMgmtNotifDelayTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CgrtMgmtNotifDelayTime_Type.__name__=_O
_CgrtMgmtNotifDelayTime_Object=MibScalar
cgrtMgmtNotifDelayTime=_CgrtMgmtNotifDelayTime_Object((1,3,6,1,4,1,9,9,334,1,1,16),_CgrtMgmtNotifDelayTime_Type())
cgrtMgmtNotifDelayTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifDelayTime.setStatus(_F)
if mibBuilder.loadTexts:cgrtMgmtNotifDelayTime.setUnits(_H)
class _CgrtMgmtNotifWindowTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,900))
_CgrtMgmtNotifWindowTime_Type.__name__=_G
_CgrtMgmtNotifWindowTime_Object=MibScalar
cgrtMgmtNotifWindowTime=_CgrtMgmtNotifWindowTime_Object((1,3,6,1,4,1,9,9,334,1,1,17),_CgrtMgmtNotifWindowTime_Type())
cgrtMgmtNotifWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifWindowTime.setStatus(_F)
if mibBuilder.loadTexts:cgrtMgmtNotifWindowTime.setUnits(_H)
class _CgrtMgmtNotifMaxPerWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,9000))
_CgrtMgmtNotifMaxPerWindow_Type.__name__=_G
_CgrtMgmtNotifMaxPerWindow_Object=MibScalar
cgrtMgmtNotifMaxPerWindow=_CgrtMgmtNotifMaxPerWindow_Object((1,3,6,1,4,1,9,9,334,1,1,18),_CgrtMgmtNotifMaxPerWindow_Type())
cgrtMgmtNotifMaxPerWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifMaxPerWindow.setStatus(_F)
class _CgrtMgmtNotifEnabled_Type(TruthValue):defaultValue=2
_CgrtMgmtNotifEnabled_Type.__name__=_J
_CgrtMgmtNotifEnabled_Object=MibScalar
cgrtMgmtNotifEnabled=_CgrtMgmtNotifEnabled_Object((1,3,6,1,4,1,9,9,334,1,1,19),_CgrtMgmtNotifEnabled_Type())
cgrtMgmtNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifEnabled.setStatus(_F)
class _CgrtRouteTableLoadNotifEnabled_Type(TruthValue):defaultValue=2
_CgrtRouteTableLoadNotifEnabled_Type.__name__=_J
_CgrtRouteTableLoadNotifEnabled_Object=MibScalar
cgrtRouteTableLoadNotifEnabled=_CgrtRouteTableLoadNotifEnabled_Object((1,3,6,1,4,1,9,9,334,1,1,20),_CgrtRouteTableLoadNotifEnabled_Type())
cgrtRouteTableLoadNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtRouteTableLoadNotifEnabled.setStatus(_B)
_CgrtDynamicRoutes_Type=Gauge32
_CgrtDynamicRoutes_Object=MibScalar
cgrtDynamicRoutes=_CgrtDynamicRoutes_Object((1,3,6,1,4,1,9,9,334,1,1,21),_CgrtDynamicRoutes_Type())
cgrtDynamicRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDynamicRoutes.setStatus(_B)
_CgrtDynamicRoutesDropped_Type=Counter32
_CgrtDynamicRoutesDropped_Object=MibScalar
cgrtDynamicRoutesDropped=_CgrtDynamicRoutesDropped_Object((1,3,6,1,4,1,9,9,334,1,1,22),_CgrtDynamicRoutesDropped_Type())
cgrtDynamicRoutesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDynamicRoutesDropped.setStatus(_B)
class _CgrtDestNotifWindowTimeRev1_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,86400))
_CgrtDestNotifWindowTimeRev1_Type.__name__=_G
_CgrtDestNotifWindowTimeRev1_Object=MibScalar
cgrtDestNotifWindowTimeRev1=_CgrtDestNotifWindowTimeRev1_Object((1,3,6,1,4,1,9,9,334,1,1,23),_CgrtDestNotifWindowTimeRev1_Type())
cgrtDestNotifWindowTimeRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifWindowTimeRev1.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestNotifWindowTimeRev1.setUnits(_H)
class _CgrtDestNotifMaxPerWindowRev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,9000))
_CgrtDestNotifMaxPerWindowRev1_Type.__name__=_G
_CgrtDestNotifMaxPerWindowRev1_Object=MibScalar
cgrtDestNotifMaxPerWindowRev1=_CgrtDestNotifMaxPerWindowRev1_Object((1,3,6,1,4,1,9,9,334,1,1,24),_CgrtDestNotifMaxPerWindowRev1_Type())
cgrtDestNotifMaxPerWindowRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifMaxPerWindowRev1.setStatus(_B)
class _CgrtDestNotifEnabledRev1_Type(TruthValue):defaultValue=2
_CgrtDestNotifEnabledRev1_Type.__name__=_J
_CgrtDestNotifEnabledRev1_Object=MibScalar
cgrtDestNotifEnabledRev1=_CgrtDestNotifEnabledRev1_Object((1,3,6,1,4,1,9,9,334,1,1,25),_CgrtDestNotifEnabledRev1_Type())
cgrtDestNotifEnabledRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtDestNotifEnabledRev1.setStatus(_B)
class _CgrtMgmtNotifWindowTimeRev1_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,86400))
_CgrtMgmtNotifWindowTimeRev1_Type.__name__=_G
_CgrtMgmtNotifWindowTimeRev1_Object=MibScalar
cgrtMgmtNotifWindowTimeRev1=_CgrtMgmtNotifWindowTimeRev1_Object((1,3,6,1,4,1,9,9,334,1,1,26),_CgrtMgmtNotifWindowTimeRev1_Type())
cgrtMgmtNotifWindowTimeRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifWindowTimeRev1.setStatus(_B)
if mibBuilder.loadTexts:cgrtMgmtNotifWindowTimeRev1.setUnits(_H)
class _CgrtMgmtNotifMaxPerWindowRev1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,9000))
_CgrtMgmtNotifMaxPerWindowRev1_Type.__name__=_G
_CgrtMgmtNotifMaxPerWindowRev1_Object=MibScalar
cgrtMgmtNotifMaxPerWindowRev1=_CgrtMgmtNotifMaxPerWindowRev1_Object((1,3,6,1,4,1,9,9,334,1,1,27),_CgrtMgmtNotifMaxPerWindowRev1_Type())
cgrtMgmtNotifMaxPerWindowRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifMaxPerWindowRev1.setStatus(_B)
class _CgrtMgmtNotifEnabledRev1_Type(TruthValue):defaultValue=2
_CgrtMgmtNotifEnabledRev1_Type.__name__=_J
_CgrtMgmtNotifEnabledRev1_Object=MibScalar
cgrtMgmtNotifEnabledRev1=_CgrtMgmtNotifEnabledRev1_Object((1,3,6,1,4,1,9,9,334,1,1,28),_CgrtMgmtNotifEnabledRev1_Type())
cgrtMgmtNotifEnabledRev1.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtMgmtNotifEnabledRev1.setStatus(_B)
class _CgrtOrigTableEnabled_Type(TruthValue):defaultValue=2
_CgrtOrigTableEnabled_Type.__name__=_J
_CgrtOrigTableEnabled_Object=MibScalar
cgrtOrigTableEnabled=_CgrtOrigTableEnabled_Object((1,3,6,1,4,1,9,9,334,1,1,29),_CgrtOrigTableEnabled_Type())
cgrtOrigTableEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtOrigTableEnabled.setStatus(_B)
class _CgrtPCStatsInterval_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(900,3600))
_CgrtPCStatsInterval_Type.__name__=_O
_CgrtPCStatsInterval_Object=MibScalar
cgrtPCStatsInterval=_CgrtPCStatsInterval_Object((1,3,6,1,4,1,9,9,334,1,1,30),_CgrtPCStatsInterval_Type())
cgrtPCStatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtPCStatsInterval.setStatus(_B)
if mibBuilder.loadTexts:cgrtPCStatsInterval.setUnits(_H)
class _CgrtNoRouteMSUsNotifEnabled_Type(TruthValue):defaultValue=2
_CgrtNoRouteMSUsNotifEnabled_Type.__name__=_J
_CgrtNoRouteMSUsNotifEnabled_Object=MibScalar
cgrtNoRouteMSUsNotifEnabled=_CgrtNoRouteMSUsNotifEnabled_Object((1,3,6,1,4,1,9,9,334,1,1,31),_CgrtNoRouteMSUsNotifEnabled_Type())
cgrtNoRouteMSUsNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtNoRouteMSUsNotifEnabled.setStatus(_B)
class _CgrtNoRouteMSUsNotifWindowTime_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_CgrtNoRouteMSUsNotifWindowTime_Type.__name__=_G
_CgrtNoRouteMSUsNotifWindowTime_Object=MibScalar
cgrtNoRouteMSUsNotifWindowTime=_CgrtNoRouteMSUsNotifWindowTime_Object((1,3,6,1,4,1,9,9,334,1,1,32),_CgrtNoRouteMSUsNotifWindowTime_Type())
cgrtNoRouteMSUsNotifWindowTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cgrtNoRouteMSUsNotifWindowTime.setStatus(_B)
if mibBuilder.loadTexts:cgrtNoRouteMSUsNotifWindowTime.setUnits(_H)
_CgrtObjects_ObjectIdentity=ObjectIdentity
cgrtObjects=_CgrtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,334,1,2))
_CgrtInstTable_Object=MibTable
cgrtInstTable=_CgrtInstTable_Object((1,3,6,1,4,1,9,9,334,1,2,1))
if mibBuilder.loadTexts:cgrtInstTable.setStatus(_B)
_CgrtInstEntry_Object=MibTableRow
cgrtInstEntry=_CgrtInstEntry_Object((1,3,6,1,4,1,9,9,334,1,2,1,1))
cgrtInstEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:cgrtInstEntry.setStatus(_B)
_CgrtInstLastChanged_Type=TimeStamp
_CgrtInstLastChanged_Object=MibTableColumn
cgrtInstLastChanged=_CgrtInstLastChanged_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,1),_CgrtInstLastChanged_Type())
cgrtInstLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstLastChanged.setStatus(_B)
_CgrtInstLastLoadTime_Type=TimeStamp
_CgrtInstLastLoadTime_Object=MibTableColumn
cgrtInstLastLoadTime=_CgrtInstLastLoadTime_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,2),_CgrtInstLastLoadTime_Type())
cgrtInstLastLoadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstLastLoadTime.setStatus(_B)
_CgrtInstLoadStatus_Type=CItpTcTableLoadStatus
_CgrtInstLoadStatus_Object=MibTableColumn
cgrtInstLoadStatus=_CgrtInstLoadStatus_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,3),_CgrtInstLoadStatus_Type())
cgrtInstLoadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstLoadStatus.setStatus(_B)
_CgrtInstTableName_Type=CItpTcRouteTableName
_CgrtInstTableName_Object=MibTableColumn
cgrtInstTableName=_CgrtInstTableName_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,4),_CgrtInstTableName_Type())
cgrtInstTableName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstTableName.setStatus(_B)
_CgrtInstLastURL_Type=CItpTcURL
_CgrtInstLastURL_Object=MibTableColumn
cgrtInstLastURL=_CgrtInstLastURL_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,5),_CgrtInstLastURL_Type())
cgrtInstLastURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstLastURL.setStatus(_B)
_CgrtInstNumberDestinations_Type=Gauge32
_CgrtInstNumberDestinations_Object=MibTableColumn
cgrtInstNumberDestinations=_CgrtInstNumberDestinations_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,6),_CgrtInstNumberDestinations_Type())
cgrtInstNumberDestinations.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstNumberDestinations.setStatus(_B)
if mibBuilder.loadTexts:cgrtInstNumberDestinations.setUnits('entries')
_CgrtInstNumberRoutes_Type=Gauge32
_CgrtInstNumberRoutes_Object=MibTableColumn
cgrtInstNumberRoutes=_CgrtInstNumberRoutes_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,7),_CgrtInstNumberRoutes_Type())
cgrtInstNumberRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstNumberRoutes.setStatus(_B)
if mibBuilder.loadTexts:cgrtInstNumberRoutes.setUnits('entries')
_CgrtInstUnknownOrigPCs_Type=Counter32
_CgrtInstUnknownOrigPCs_Object=MibTableColumn
cgrtInstUnknownOrigPCs=_CgrtInstUnknownOrigPCs_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,8),_CgrtInstUnknownOrigPCs_Type())
cgrtInstUnknownOrigPCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstUnknownOrigPCs.setStatus(_B)
if mibBuilder.loadTexts:cgrtInstUnknownOrigPCs.setUnits(_I)
_CgrtInstNoRouteDrops_Type=Counter32
_CgrtInstNoRouteDrops_Object=MibTableColumn
cgrtInstNoRouteDrops=_CgrtInstNoRouteDrops_Object((1,3,6,1,4,1,9,9,334,1,2,1,1,9),_CgrtInstNoRouteDrops_Type())
cgrtInstNoRouteDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtInstNoRouteDrops.setStatus(_B)
if mibBuilder.loadTexts:cgrtInstNoRouteDrops.setUnits(_I)
_CgrtDestTable_Object=MibTable
cgrtDestTable=_CgrtDestTable_Object((1,3,6,1,4,1,9,9,334,1,2,2))
if mibBuilder.loadTexts:cgrtDestTable.setStatus(_B)
_CgrtDestEntry_Object=MibTableRow
cgrtDestEntry=_CgrtDestEntry_Object((1,3,6,1,4,1,9,9,334,1,2,2,1))
cgrtDestEntry.setIndexNames((0,_D,_N),(0,_A,_U),(0,_A,_P))
if mibBuilder.loadTexts:cgrtDestEntry.setStatus(_B)
class _CgrtDestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('accessible',2),('inaccessible',3),(_V,4)))
_CgrtDestStatus_Type.__name__=_G
_CgrtDestStatus_Object=MibTableColumn
cgrtDestStatus=_CgrtDestStatus_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,1),_CgrtDestStatus_Type())
cgrtDestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestStatus.setStatus(_B)
class _CgrtDestCongestion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CgrtDestCongestion_Type.__name__=_O
_CgrtDestCongestion_Object=MibTableColumn
cgrtDestCongestion=_CgrtDestCongestion_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,2),_CgrtDestCongestion_Type())
cgrtDestCongestion.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestCongestion.setStatus(_B)
_CgrtDestAccessibleSeconds_Type=Counter32
_CgrtDestAccessibleSeconds_Object=MibTableColumn
cgrtDestAccessibleSeconds=_CgrtDestAccessibleSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,3),_CgrtDestAccessibleSeconds_Type())
cgrtDestAccessibleSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestAccessibleSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestAccessibleSeconds.setUnits(_H)
_CgrtDestInaccessibleSeconds_Type=Counter32
_CgrtDestInaccessibleSeconds_Object=MibTableColumn
cgrtDestInaccessibleSeconds=_CgrtDestInaccessibleSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,4),_CgrtDestInaccessibleSeconds_Type())
cgrtDestInaccessibleSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestInaccessibleSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestInaccessibleSeconds.setUnits(_H)
_CgrtDestRestrictedSeconds_Type=Counter32
_CgrtDestRestrictedSeconds_Object=MibTableColumn
cgrtDestRestrictedSeconds=_CgrtDestRestrictedSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,5),_CgrtDestRestrictedSeconds_Type())
cgrtDestRestrictedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestRestrictedSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestRestrictedSeconds.setUnits(_H)
_CgrtDestMSUsOut_Type=Counter32
_CgrtDestMSUsOut_Object=MibTableColumn
cgrtDestMSUsOut=_CgrtDestMSUsOut_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,6),_CgrtDestMSUsOut_Type())
cgrtDestMSUsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestMSUsOut.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestMSUsOut.setUnits(_I)
_CgrtDestOctetsOut_Type=Counter64
_CgrtDestOctetsOut_Object=MibTableColumn
cgrtDestOctetsOut=_CgrtDestOctetsOut_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,7),_CgrtDestOctetsOut_Type())
cgrtDestOctetsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestOctetsOut.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestOctetsOut.setUnits(_Q)
_CgrtDestMSUsIn_Type=Counter32
_CgrtDestMSUsIn_Object=MibTableColumn
cgrtDestMSUsIn=_CgrtDestMSUsIn_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,8),_CgrtDestMSUsIn_Type())
cgrtDestMSUsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestMSUsIn.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestMSUsIn.setUnits(_I)
_CgrtDestOctetsIn_Type=Counter64
_CgrtDestOctetsIn_Object=MibTableColumn
cgrtDestOctetsIn=_CgrtDestOctetsIn_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,9),_CgrtDestOctetsIn_Type())
cgrtDestOctetsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestOctetsIn.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestOctetsIn.setUnits(_Q)
_CgrtDestInaccessibleDrops_Type=Counter32
_CgrtDestInaccessibleDrops_Object=MibTableColumn
cgrtDestInaccessibleDrops=_CgrtDestInaccessibleDrops_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,10),_CgrtDestInaccessibleDrops_Type())
cgrtDestInaccessibleDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestInaccessibleDrops.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestInaccessibleDrops.setUnits(_I)
_CgrtDestRestrictedMSUs_Type=Counter32
_CgrtDestRestrictedMSUs_Object=MibTableColumn
cgrtDestRestrictedMSUs=_CgrtDestRestrictedMSUs_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,11),_CgrtDestRestrictedMSUs_Type())
cgrtDestRestrictedMSUs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestRestrictedMSUs.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestRestrictedMSUs.setUnits(_I)
_CgrtDestCongestionDrops_Type=Counter32
_CgrtDestCongestionDrops_Object=MibTableColumn
cgrtDestCongestionDrops=_CgrtDestCongestionDrops_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,12),_CgrtDestCongestionDrops_Type())
cgrtDestCongestionDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestCongestionDrops.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestCongestionDrops.setUnits(_I)
_CgrtDestDisplay_Type=CItpTcDisplayPC
_CgrtDestDisplay_Object=MibTableColumn
cgrtDestDisplay=_CgrtDestDisplay_Object((1,3,6,1,4,1,9,9,334,1,2,2,1,13),_CgrtDestDisplay_Type())
cgrtDestDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestDisplay.setStatus(_B)
_CgrtRouteTable_Object=MibTable
cgrtRouteTable=_CgrtRouteTable_Object((1,3,6,1,4,1,9,9,334,1,2,3))
if mibBuilder.loadTexts:cgrtRouteTable.setStatus(_B)
_CgrtRouteEntry_Object=MibTableRow
cgrtRouteEntry=_CgrtRouteEntry_Object((1,3,6,1,4,1,9,9,334,1,2,3,1))
cgrtRouteEntry.setIndexNames((0,_D,_N),(0,_A,_U),(0,_A,_P),(0,_A,_A2),(0,_A,_A3))
if mibBuilder.loadTexts:cgrtRouteEntry.setStatus(_B)
_CgrtRouteDpc_Type=CItpTcPointCode
_CgrtRouteDpc_Object=MibTableColumn
cgrtRouteDpc=_CgrtRouteDpc_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,1),_CgrtRouteDpc_Type())
cgrtRouteDpc.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtRouteDpc.setStatus(_B)
class _CgrtRouteMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CgrtRouteMask_Type.__name__=_O
_CgrtRouteMask_Object=MibTableColumn
cgrtRouteMask=_CgrtRouteMask_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,2),_CgrtRouteMask_Type())
cgrtRouteMask.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtRouteMask.setStatus(_B)
class _CgrtRouteDestLsCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CgrtRouteDestLsCost_Type.__name__=_O
_CgrtRouteDestLsCost_Object=MibTableColumn
cgrtRouteDestLsCost=_CgrtRouteDestLsCost_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,3),_CgrtRouteDestLsCost_Type())
cgrtRouteDestLsCost.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtRouteDestLsCost.setStatus(_B)
_CgrtRouteDestLinkset_Type=CItpTcLinksetId
_CgrtRouteDestLinkset_Object=MibTableColumn
cgrtRouteDestLinkset=_CgrtRouteDestLinkset_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,4),_CgrtRouteDestLinkset_Type())
cgrtRouteDestLinkset.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtRouteDestLinkset.setStatus(_B)
_CgrtRouteQos_Type=CItpTcQos
_CgrtRouteQos_Object=MibTableColumn
cgrtRouteQos=_CgrtRouteQos_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,5),_CgrtRouteQos_Type())
cgrtRouteQos.setMaxAccess(_T)
if mibBuilder.loadTexts:cgrtRouteQos.setStatus(_B)
class _CgrtRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),(_A4,2),(_V,3),(_A5,4),(_d,5)))
_CgrtRouteStatus_Type.__name__=_G
_CgrtRouteStatus_Object=MibTableColumn
cgrtRouteStatus=_CgrtRouteStatus_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,6),_CgrtRouteStatus_Type())
cgrtRouteStatus.setMaxAccess(_T)
if mibBuilder.loadTexts:cgrtRouteStatus.setStatus(_B)
class _CgrtRouteMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('allowed',2),(_V,3),('prohibited',4),(_d,5)))
_CgrtRouteMgmtStatus_Type.__name__=_G
_CgrtRouteMgmtStatus_Object=MibTableColumn
cgrtRouteMgmtStatus=_CgrtRouteMgmtStatus_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,7),_CgrtRouteMgmtStatus_Type())
cgrtRouteMgmtStatus.setMaxAccess(_T)
if mibBuilder.loadTexts:cgrtRouteMgmtStatus.setStatus(_B)
_CgrtRouteDynamic_Type=TruthValue
_CgrtRouteDynamic_Object=MibTableColumn
cgrtRouteDynamic=_CgrtRouteDynamic_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,8),_CgrtRouteDynamic_Type())
cgrtRouteDynamic.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteDynamic.setStatus(_B)
class _CgrtRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),('static',1),('cluster',2),('summary',3),('xlist',4),('shadow',5),('management',6),('alias',7)))
_CgrtRouteType_Type.__name__=_G
_CgrtRouteType_Object=MibTableColumn
cgrtRouteType=_CgrtRouteType_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,9),_CgrtRouteType_Type())
cgrtRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteType.setStatus(_B)
class _CgrtRouteAdminStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),(_S,1),(_A4,2),(_V,3),(_A5,4),(_d,5)))
_CgrtRouteAdminStatus_Type.__name__=_G
_CgrtRouteAdminStatus_Object=MibTableColumn
cgrtRouteAdminStatus=_CgrtRouteAdminStatus_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,10),_CgrtRouteAdminStatus_Type())
cgrtRouteAdminStatus.setMaxAccess(_T)
if mibBuilder.loadTexts:cgrtRouteAdminStatus.setStatus(_B)
_CgrtRouteRowStatus_Type=RowStatus
_CgrtRouteRowStatus_Object=MibTableColumn
cgrtRouteRowStatus=_CgrtRouteRowStatus_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,11),_CgrtRouteRowStatus_Type())
cgrtRouteRowStatus.setMaxAccess(_T)
if mibBuilder.loadTexts:cgrtRouteRowStatus.setStatus(_B)
_CgrtRouteAllowedSeconds_Type=Counter32
_CgrtRouteAllowedSeconds_Object=MibTableColumn
cgrtRouteAllowedSeconds=_CgrtRouteAllowedSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,12),_CgrtRouteAllowedSeconds_Type())
cgrtRouteAllowedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteAllowedSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtRouteAllowedSeconds.setUnits(_H)
_CgrtRouteRestrictedSeconds_Type=Counter32
_CgrtRouteRestrictedSeconds_Object=MibTableColumn
cgrtRouteRestrictedSeconds=_CgrtRouteRestrictedSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,13),_CgrtRouteRestrictedSeconds_Type())
cgrtRouteRestrictedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteRestrictedSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtRouteRestrictedSeconds.setUnits(_H)
_CgrtRouteProhibitedSeconds_Type=Counter32
_CgrtRouteProhibitedSeconds_Object=MibTableColumn
cgrtRouteProhibitedSeconds=_CgrtRouteProhibitedSeconds_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,14),_CgrtRouteProhibitedSeconds_Type())
cgrtRouteProhibitedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteProhibitedSeconds.setStatus(_B)
if mibBuilder.loadTexts:cgrtRouteProhibitedSeconds.setUnits(_H)
_CgrtRouteDisplay_Type=CItpTcDisplayPC
_CgrtRouteDisplay_Object=MibTableColumn
cgrtRouteDisplay=_CgrtRouteDisplay_Object((1,3,6,1,4,1,9,9,334,1,2,3,1,15),_CgrtRouteDisplay_Type())
cgrtRouteDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtRouteDisplay.setStatus(_B)
_CgrtNotificationsInfo_ObjectIdentity=ObjectIdentity
cgrtNotificationsInfo=_CgrtNotificationsInfo_ObjectIdentity((1,3,6,1,4,1,9,9,334,1,2,4))
_CgrtDestNotifSupFlag_Type=TruthValue
_CgrtDestNotifSupFlag_Object=MibScalar
cgrtDestNotifSupFlag=_CgrtDestNotifSupFlag_Object((1,3,6,1,4,1,9,9,334,1,2,4,1),_CgrtDestNotifSupFlag_Type())
cgrtDestNotifSupFlag.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtDestNotifSupFlag.setStatus(_F)
class _CgrtDestNotifChanges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CgrtDestNotifChanges_Type.__name__=_c
_CgrtDestNotifChanges_Object=MibScalar
cgrtDestNotifChanges=_CgrtDestNotifChanges_Object((1,3,6,1,4,1,9,9,334,1,2,4,2),_CgrtDestNotifChanges_Type())
cgrtDestNotifChanges.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtDestNotifChanges.setStatus(_F)
_CgrtMgmtNotifSupFlag_Type=TruthValue
_CgrtMgmtNotifSupFlag_Object=MibScalar
cgrtMgmtNotifSupFlag=_CgrtMgmtNotifSupFlag_Object((1,3,6,1,4,1,9,9,334,1,2,4,3),_CgrtMgmtNotifSupFlag_Type())
cgrtMgmtNotifSupFlag.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtMgmtNotifSupFlag.setStatus(_F)
class _CgrtMgmtNotifChanges_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CgrtMgmtNotifChanges_Type.__name__=_c
_CgrtMgmtNotifChanges_Object=MibScalar
cgrtMgmtNotifChanges=_CgrtMgmtNotifChanges_Object((1,3,6,1,4,1,9,9,334,1,2,4,4),_CgrtMgmtNotifChanges_Type())
cgrtMgmtNotifChanges.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtMgmtNotifChanges.setStatus(_F)
_CgrtDestNotifSuppressed_Type=Counter32
_CgrtDestNotifSuppressed_Object=MibScalar
cgrtDestNotifSuppressed=_CgrtDestNotifSuppressed_Object((1,3,6,1,4,1,9,9,334,1,2,4,5),_CgrtDestNotifSuppressed_Type())
cgrtDestNotifSuppressed.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtDestNotifSuppressed.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestNotifSuppressed.setUnits(_A6)
_CgrtRouteNotifSuppressed_Type=Counter32
_CgrtRouteNotifSuppressed_Object=MibScalar
cgrtRouteNotifSuppressed=_CgrtRouteNotifSuppressed_Object((1,3,6,1,4,1,9,9,334,1,2,4,6),_CgrtRouteNotifSuppressed_Type())
cgrtRouteNotifSuppressed.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtRouteNotifSuppressed.setStatus(_B)
if mibBuilder.loadTexts:cgrtRouteNotifSuppressed.setUnits(_A6)
_CgrtNoRouteMSUsInterval_Type=Unsigned32
_CgrtNoRouteMSUsInterval_Object=MibScalar
cgrtNoRouteMSUsInterval=_CgrtNoRouteMSUsInterval_Object((1,3,6,1,4,1,9,9,334,1,2,4,7),_CgrtNoRouteMSUsInterval_Type())
cgrtNoRouteMSUsInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtNoRouteMSUsInterval.setStatus(_B)
if mibBuilder.loadTexts:cgrtNoRouteMSUsInterval.setUnits(_H)
_CgrtIntervalNoRouteMSUs_Type=Unsigned32
_CgrtIntervalNoRouteMSUs_Object=MibScalar
cgrtIntervalNoRouteMSUs=_CgrtIntervalNoRouteMSUs_Object((1,3,6,1,4,1,9,9,334,1,2,4,8),_CgrtIntervalNoRouteMSUs_Type())
cgrtIntervalNoRouteMSUs.setMaxAccess(_K)
if mibBuilder.loadTexts:cgrtIntervalNoRouteMSUs.setStatus(_B)
if mibBuilder.loadTexts:cgrtIntervalNoRouteMSUs.setUnits(_I)
_CgrtOrigTable_Object=MibTable
cgrtOrigTable=_CgrtOrigTable_Object((1,3,6,1,4,1,9,9,334,1,2,5))
if mibBuilder.loadTexts:cgrtOrigTable.setStatus(_B)
_CgrtOrigEntry_Object=MibTableRow
cgrtOrigEntry=_CgrtOrigEntry_Object((1,3,6,1,4,1,9,9,334,1,2,5,1))
cgrtOrigEntry.setIndexNames((0,_D,_N),(0,_A,_e),(0,_A,_P))
if mibBuilder.loadTexts:cgrtOrigEntry.setStatus(_B)
_CgrtOrigPC_Type=CItpTcPointCode
_CgrtOrigPC_Object=MibTableColumn
cgrtOrigPC=_CgrtOrigPC_Object((1,3,6,1,4,1,9,9,334,1,2,5,1,1),_CgrtOrigPC_Type())
cgrtOrigPC.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtOrigPC.setStatus(_B)
_CgrtOrigMSUs_Type=Counter32
_CgrtOrigMSUs_Object=MibTableColumn
cgrtOrigMSUs=_CgrtOrigMSUs_Object((1,3,6,1,4,1,9,9,334,1,2,5,1,2),_CgrtOrigMSUs_Type())
cgrtOrigMSUs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigMSUs.setStatus(_B)
if mibBuilder.loadTexts:cgrtOrigMSUs.setUnits(_I)
_CgrtOrigOctets_Type=Counter64
_CgrtOrigOctets_Object=MibTableColumn
cgrtOrigOctets=_CgrtOrigOctets_Object((1,3,6,1,4,1,9,9,334,1,2,5,1,3),_CgrtOrigOctets_Type())
cgrtOrigOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigOctets.setStatus(_B)
if mibBuilder.loadTexts:cgrtOrigOctets.setUnits(_Q)
_CgrtOrigDisplay_Type=CItpTcDisplayPC
_CgrtOrigDisplay_Object=MibTableColumn
cgrtOrigDisplay=_CgrtOrigDisplay_Object((1,3,6,1,4,1,9,9,334,1,2,5,1,4),_CgrtOrigDisplay_Type())
cgrtOrigDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigDisplay.setStatus(_B)
_CgrtDestSITable_Object=MibTable
cgrtDestSITable=_CgrtDestSITable_Object((1,3,6,1,4,1,9,9,334,1,2,6))
if mibBuilder.loadTexts:cgrtDestSITable.setStatus(_B)
_CgrtDestSIEntry_Object=MibTableRow
cgrtDestSIEntry=_CgrtDestSIEntry_Object((1,3,6,1,4,1,9,9,334,1,2,6,1))
cgrtDestSIEntry.setIndexNames((0,_D,_N),(0,_A,_U),(0,_A,_P),(0,_A,_f))
if mibBuilder.loadTexts:cgrtDestSIEntry.setStatus(_B)
_CgrtMtp3SI_Type=CItpTcServiceIndicator
_CgrtMtp3SI_Object=MibTableColumn
cgrtMtp3SI=_CgrtMtp3SI_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,1),_CgrtMtp3SI_Type())
cgrtMtp3SI.setMaxAccess(_R)
if mibBuilder.loadTexts:cgrtMtp3SI.setStatus(_B)
_CgrtDestSIMSUsOut_Type=Counter32
_CgrtDestSIMSUsOut_Object=MibTableColumn
cgrtDestSIMSUsOut=_CgrtDestSIMSUsOut_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,2),_CgrtDestSIMSUsOut_Type())
cgrtDestSIMSUsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestSIMSUsOut.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestSIMSUsOut.setUnits(_I)
_CgrtDestSIOctetsOut_Type=Counter64
_CgrtDestSIOctetsOut_Object=MibTableColumn
cgrtDestSIOctetsOut=_CgrtDestSIOctetsOut_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,3),_CgrtDestSIOctetsOut_Type())
cgrtDestSIOctetsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestSIOctetsOut.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestSIOctetsOut.setUnits(_Q)
_CgrtDestSIMSUsIn_Type=Counter32
_CgrtDestSIMSUsIn_Object=MibTableColumn
cgrtDestSIMSUsIn=_CgrtDestSIMSUsIn_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,4),_CgrtDestSIMSUsIn_Type())
cgrtDestSIMSUsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestSIMSUsIn.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestSIMSUsIn.setUnits(_I)
_CgrtDestSIOctetsIn_Type=Counter64
_CgrtDestSIOctetsIn_Object=MibTableColumn
cgrtDestSIOctetsIn=_CgrtDestSIOctetsIn_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,5),_CgrtDestSIOctetsIn_Type())
cgrtDestSIOctetsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestSIOctetsIn.setStatus(_B)
if mibBuilder.loadTexts:cgrtDestSIOctetsIn.setUnits(_Q)
_CgrtDestSIDisplay_Type=CgrtDisplayPCSI
_CgrtDestSIDisplay_Object=MibTableColumn
cgrtDestSIDisplay=_CgrtDestSIDisplay_Object((1,3,6,1,4,1,9,9,334,1,2,6,1,6),_CgrtDestSIDisplay_Type())
cgrtDestSIDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtDestSIDisplay.setStatus(_B)
_CgrtOrigSITable_Object=MibTable
cgrtOrigSITable=_CgrtOrigSITable_Object((1,3,6,1,4,1,9,9,334,1,2,7))
if mibBuilder.loadTexts:cgrtOrigSITable.setStatus(_B)
_CgrtOrigSIEntry_Object=MibTableRow
cgrtOrigSIEntry=_CgrtOrigSIEntry_Object((1,3,6,1,4,1,9,9,334,1,2,7,1))
cgrtOrigSIEntry.setIndexNames((0,_D,_N),(0,_A,_e),(0,_A,_P),(0,_A,_f))
if mibBuilder.loadTexts:cgrtOrigSIEntry.setStatus(_B)
_CgrtOrigSIMSUs_Type=Counter32
_CgrtOrigSIMSUs_Object=MibTableColumn
cgrtOrigSIMSUs=_CgrtOrigSIMSUs_Object((1,3,6,1,4,1,9,9,334,1,2,7,1,1),_CgrtOrigSIMSUs_Type())
cgrtOrigSIMSUs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigSIMSUs.setStatus(_B)
if mibBuilder.loadTexts:cgrtOrigSIMSUs.setUnits(_I)
_CgrtOrigSIOctets_Type=Counter64
_CgrtOrigSIOctets_Object=MibTableColumn
cgrtOrigSIOctets=_CgrtOrigSIOctets_Object((1,3,6,1,4,1,9,9,334,1,2,7,1,2),_CgrtOrigSIOctets_Type())
cgrtOrigSIOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigSIOctets.setStatus(_B)
if mibBuilder.loadTexts:cgrtOrigSIOctets.setUnits(_Q)
_CgrtOrigSIDisplay_Type=CgrtDisplayPCSI
_CgrtOrigSIDisplay_Object=MibTableColumn
cgrtOrigSIDisplay=_CgrtOrigSIDisplay_Object((1,3,6,1,4,1,9,9,334,1,2,7,1,3),_CgrtOrigSIDisplay_Type())
cgrtOrigSIDisplay.setMaxAccess(_C)
if mibBuilder.loadTexts:cgrtOrigSIDisplay.setStatus(_B)
_CiscoGrtMIBConform_ObjectIdentity=ObjectIdentity
ciscoGrtMIBConform=_CiscoGrtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,334,2))
_CiscoGrtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGrtMIBCompliances=_CiscoGrtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,334,2,1))
_CiscoGrtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGrtMIBGroups=_CiscoGrtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,334,2,2))
ciscoGrtInstGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,1))
ciscoGrtInstGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_g),(_A,_h),(_A,_i),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciscoGrtInstGroup.setStatus(_B)
ciscoGrtDestGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,2))
ciscoGrtDestGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_j),(_A,_k),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoGrtDestGroup.setStatus(_F)
ciscoGrtRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,3))
ciscoGrtRouteGroup.setObjects(*((_A,_l),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_Y),(_A,_Z),(_A,_a),(_A,_r),(_A,_b),(_A,_s)))
if mibBuilder.loadTexts:ciscoGrtRouteGroup.setStatus(_F)
ciscoGrtScalarsGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,5))
ciscoGrtScalarsGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:ciscoGrtScalarsGroup.setStatus(_B)
ciscoGrtDestGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,6))
ciscoGrtDestGroupRev1.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_t),(_A,_W),(_A,_X),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_u)))
if mibBuilder.loadTexts:ciscoGrtDestGroupRev1.setStatus(_B)
ciscoGrtRouteGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,7))
ciscoGrtRouteGroupRev1.setObjects(*((_A,_l),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_v),(_A,_o),(_A,_p),(_A,_q),(_A,_Y),(_A,_Z),(_A,_a),(_A,_r),(_A,_b),(_A,_s),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_w)))
if mibBuilder.loadTexts:ciscoGrtRouteGroupRev1.setStatus(_B)
ciscoGrtOrigGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,8))
ciscoGrtOrigGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:ciscoGrtOrigGroup.setStatus(_B)
ciscoGrtDestSIGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,9))
ciscoGrtDestSIGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:ciscoGrtDestSIGroup.setStatus(_B)
ciscoGrtOrigSIGroup=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,10))
ciscoGrtOrigSIGroup.setObjects(*((_A,_An),(_A,_Ao),(_A,_Ap)))
if mibBuilder.loadTexts:ciscoGrtOrigSIGroup.setStatus(_B)
ciscoGrtInstGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,334,2,2,12))
ciscoGrtInstGroupSup1.setObjects(*((_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoGrtInstGroupSup1.setStatus(_B)
ciscoGrtDestStateChange=NotificationType((1,3,6,1,4,1,9,9,334,0,1))
ciscoGrtDestStateChange.setObjects(*((_D,_M),(_D,_L),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoGrtDestStateChange.setStatus(_F)
ciscoGrtMgmtStateChange=NotificationType((1,3,6,1,4,1,9,9,334,0,2))
ciscoGrtMgmtStateChange.setObjects(*((_D,_M),(_D,_L),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoGrtMgmtStateChange.setStatus(_F)
ciscoGrtRouteTableLoad=NotificationType((1,3,6,1,4,1,9,9,334,0,3))
ciscoGrtRouteTableLoad.setObjects(*((_D,_M),(_D,_L),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ciscoGrtRouteTableLoad.setStatus(_B)
ciscoGrtDestStateChangeRev1=NotificationType((1,3,6,1,4,1,9,9,334,0,4))
ciscoGrtDestStateChangeRev1.setObjects(*((_D,_M),(_D,_L),(_A,_t),(_A,_u),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoGrtDestStateChangeRev1.setStatus(_B)
ciscoGrtMgmtStateChangeRev1=NotificationType((1,3,6,1,4,1,9,9,334,0,5))
ciscoGrtMgmtStateChangeRev1.setObjects(*((_D,_M),(_D,_L),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:ciscoGrtMgmtStateChangeRev1.setStatus(_B)
ciscoGrtNoRouteMSUDiscards=NotificationType((1,3,6,1,4,1,9,9,334,0,6))
ciscoGrtNoRouteMSUDiscards.setObjects(*((_D,_M),(_D,_L),(_D,_A1),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:ciscoGrtNoRouteMSUDiscards.setStatus(_B)
ciscoGrtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,334,2,2,4))
ciscoGrtNotificationsGroup.setObjects(*((_A,_Au),(_A,_Av),(_A,_z)))
if mibBuilder.loadTexts:ciscoGrtNotificationsGroup.setStatus(_F)
ciscoGrtNotificationsGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,334,2,2,11))
ciscoGrtNotificationsGroupRev1.setObjects(*((_A,_z),(_A,_Aw),(_A,_Ax),(_A,_Ay)))
if mibBuilder.loadTexts:ciscoGrtNotificationsGroupRev1.setStatus(_B)
ciscoGrtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,334,2,1,1))
ciscoGrtMIBCompliance.setObjects(*((_A,_A0),(_A,_Az),(_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:ciscoGrtMIBCompliance.setStatus(_F)
ciscoGrtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,334,2,1,2))
ciscoGrtMIBComplianceRev1.setObjects(*((_A,_A0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8)))
if mibBuilder.loadTexts:ciscoGrtMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CgrtDisplayPCSI':CgrtDisplayPCSI,'ciscoGrtMIB':ciscoGrtMIB,'ciscoGrtNotifications':ciscoGrtNotifications,_Au:ciscoGrtDestStateChange,_Av:ciscoGrtMgmtStateChange,_z:ciscoGrtRouteTableLoad,_Aw:ciscoGrtDestStateChangeRev1,_Ax:ciscoGrtMgmtStateChangeRev1,_Ay:ciscoGrtNoRouteMSUDiscards,'ciscoGrtMIBObjects':ciscoGrtMIBObjects,'cgrtScalars':cgrtScalars,_l:cgrtRouteMaxDynamic,_AC:cgrtDestNotifDelayTime,_AD:cgrtDestNotifWindowTime,_AE:cgrtDestNotifMaxPerWindow,_AF:cgrtDestNotifEnabled,_AG:cgrtMgmtNotifDelayTime,_AH:cgrtMgmtNotifWindowTime,_AI:cgrtMgmtNotifMaxPerWindow,_AJ:cgrtMgmtNotifEnabled,_AB:cgrtRouteTableLoadNotifEnabled,_o:cgrtDynamicRoutes,_p:cgrtDynamicRoutesDropped,_AL:cgrtDestNotifWindowTimeRev1,_AM:cgrtDestNotifMaxPerWindowRev1,_AN:cgrtDestNotifEnabledRev1,_AY:cgrtMgmtNotifWindowTimeRev1,_AZ:cgrtMgmtNotifMaxPerWindowRev1,_Aa:cgrtMgmtNotifEnabledRev1,_Ae:cgrtOrigTableEnabled,_AK:cgrtPCStatsInterval,_Aq:cgrtNoRouteMSUsNotifEnabled,_Ar:cgrtNoRouteMSUsNotifWindowTime,'cgrtObjects':cgrtObjects,'cgrtInstTable':cgrtInstTable,'cgrtInstEntry':cgrtInstEntry,_A7:cgrtInstLastChanged,_A8:cgrtInstLastLoadTime,_g:cgrtInstLoadStatus,_h:cgrtInstTableName,_i:cgrtInstLastURL,_A9:cgrtInstNumberDestinations,_AA:cgrtInstNumberRoutes,_As:cgrtInstUnknownOrigPCs,_At:cgrtInstNoRouteDrops,'cgrtDestTable':cgrtDestTable,'cgrtDestEntry':cgrtDestEntry,_W:cgrtDestStatus,_X:cgrtDestCongestion,_AO:cgrtDestAccessibleSeconds,_AP:cgrtDestInaccessibleSeconds,_AQ:cgrtDestRestrictedSeconds,_AR:cgrtDestMSUsOut,_AS:cgrtDestOctetsOut,_AT:cgrtDestMSUsIn,_AU:cgrtDestOctetsIn,_AW:cgrtDestInaccessibleDrops,_AV:cgrtDestRestrictedMSUs,_AX:cgrtDestCongestionDrops,_u:cgrtDestDisplay,'cgrtRouteTable':cgrtRouteTable,'cgrtRouteEntry':cgrtRouteEntry,_U:cgrtRouteDpc,_P:cgrtRouteMask,_A2:cgrtRouteDestLsCost,_A3:cgrtRouteDestLinkset,_q:cgrtRouteQos,_Y:cgrtRouteStatus,_Z:cgrtRouteMgmtStatus,_a:cgrtRouteDynamic,_r:cgrtRouteType,_b:cgrtRouteAdminStatus,_s:cgrtRouteRowStatus,_Ab:cgrtRouteAllowedSeconds,_Ac:cgrtRouteRestrictedSeconds,_Ad:cgrtRouteProhibitedSeconds,_w:cgrtRouteDisplay,'cgrtNotificationsInfo':cgrtNotificationsInfo,_j:cgrtDestNotifSupFlag,_k:cgrtDestNotifChanges,_m:cgrtMgmtNotifSupFlag,_n:cgrtMgmtNotifChanges,_t:cgrtDestNotifSuppressed,_v:cgrtRouteNotifSuppressed,_x:cgrtNoRouteMSUsInterval,_y:cgrtIntervalNoRouteMSUs,'cgrtOrigTable':cgrtOrigTable,'cgrtOrigEntry':cgrtOrigEntry,_e:cgrtOrigPC,_Af:cgrtOrigMSUs,_Ag:cgrtOrigOctets,_Ah:cgrtOrigDisplay,'cgrtDestSITable':cgrtDestSITable,'cgrtDestSIEntry':cgrtDestSIEntry,_f:cgrtMtp3SI,_Ai:cgrtDestSIMSUsOut,_Aj:cgrtDestSIOctetsOut,_Ak:cgrtDestSIMSUsIn,_Al:cgrtDestSIOctetsIn,_Am:cgrtDestSIDisplay,'cgrtOrigSITable':cgrtOrigSITable,'cgrtOrigSIEntry':cgrtOrigSIEntry,_An:cgrtOrigSIMSUs,_Ao:cgrtOrigSIOctets,_Ap:cgrtOrigSIDisplay,'ciscoGrtMIBConform':ciscoGrtMIBConform,'ciscoGrtMIBCompliances':ciscoGrtMIBCompliances,'ciscoGrtMIBCompliance':ciscoGrtMIBCompliance,'ciscoGrtMIBComplianceRev1':ciscoGrtMIBComplianceRev1,'ciscoGrtMIBGroups':ciscoGrtMIBGroups,_A0:ciscoGrtInstGroup,_Az:ciscoGrtDestGroup,_A_:ciscoGrtRouteGroup,_B0:ciscoGrtNotificationsGroup,_B1:ciscoGrtScalarsGroup,_B2:ciscoGrtDestGroupRev1,_B3:ciscoGrtRouteGroupRev1,_B4:ciscoGrtOrigGroup,_B5:ciscoGrtDestSIGroup,_B6:ciscoGrtOrigSIGroup,_B7:ciscoGrtNotificationsGroupRev1,_B8:ciscoGrtInstGroupSup1})