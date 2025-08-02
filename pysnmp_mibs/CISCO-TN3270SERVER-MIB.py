_Ag='ciscoTn3270ServerMIBGroupRev1'
_Af='ciscoTn3270ServerMIBGroupObsolete'
_Ae='tn3270sIpNailLuLast'
_Ad='tn3270sIpNailType'
_Ac='tn3270sIpNailClientIpMask'
_Ab='tn3270sPuNailLuLast'
_Aa='tn3270sPuNailType'
_AZ='tn3270sPuNailClientIpMask'
_AY='tn3270sLuNail'
_AX='tn3270sPuIpTosPrinter'
_AW='tn3270sPuIpTosScreen'
_AV='tn3270sPuIpPrecedencePrinter'
_AU='tn3270sPuIpPrecedenceScreen'
_AT='tn3270sLuLastEvent'
_AS='tn3270sLuEvents'
_AR='tn3270sLuLfsid'
_AQ='tn3270sLuAppnLinkIndex'
_AP='tn3270sLuType'
_AO='tn3270sLuIdleTime'
_AN='tn3270sLuCurOutQsize'
_AM='tn3270sLuCurInbQsize'
_AL='tn3270sLuCurInbPacing'
_AK='tn3270sLuState'
_AJ='tn3270sLuTermModel'
_AI='tn3270sLuTelnetType'
_AH='tn3270sLuClientTcpPort'
_AG='tn3270sLuClientAddr'
_AF='tn3270sIpLuIndex'
_AE='tn3270sIpPuIndex'
_AD='tn3270sRemoteMacAddress'
_AC='tn3270sRemoteSapAddress'
_AB='tn3270sLocalSapAddress'
_AA='tn3270sPuLuSeed'
_A9='tn3270sPuType'
_A8='tn3270sPuState'
_A7='tn3270sPuGenericPool'
_A6='tn3270sPuUnbindAction'
_A5='tn3270sPuKeepAlive'
_A4='tn3270sPuIdleTimeout'
_A3='tn3270sPuTcpPort'
_A2='tn3270sPuIpAddr'
_A1='tn3270sStatsNetSampledClientResponseTime'
_A0='tn3270sStatsSampledClientResponses'
_z='tn3270sStatsNetSampledHostResponseTime'
_y='tn3270sStatsSampledHostResponses'
_x='tn3270sStatsOutboundChains'
_w='tn3270sStatsInboundChains'
_v='tn3270sStatsTN3270ConnectsFailed'
_u='tn3270sStatsDisconnects'
_t='tn3270sStatsConnectsIn'
_s='tn3270sStatsSpareSess'
_r='tn3270sStatsMaxSess'
_q='tn3270sRunningTime'
_p='tn3270sTimingMarkSupported'
_o='tn3270sGlobalGenericPool'
_n='tn3270sGlobalUnbindAction'
_m='tn3270sGlobalKeepAlive'
_l='tn3270sGlobalIdleTimeout'
_k='tn3270sGlobalTcpPort'
_j='tn3270sStartupTime'
_i='tn3270sLusInUse'
_h='tn3270sMaxLus'
_g='tn3270sCpuCard'
_f='printer'
_e='screen'
_d='tn3270sLuIndex'
_c='tn3270sLuPuIndex'
_b='tn3270sIpClientTcpPort'
_a='tn3270sIpClientAddr'
_Z='active'
_Y='inactive'
_X='inherit'
_W='10milliseconds'
_V='tn3270sStatsServerTcpPort'
_U='tn3270sStatsServerAddr'
_T='permit'
_S='disconnect'
_R='Tn3270sUnsigned32'
_Q='Gauge32'
_P='OctetString'
_O='ciscoTn3270ServerMIBGroup'
_N='tn3270sIpNailLuFirst'
_M='tn3270sIpNailClientIpAddr'
_L='tn3270sPuNailLuFirst'
_K='tn3270sPuNailClientIpAddr'
_J='obsolete'
_I='tn3270sPuIndex'
_H='seconds'
_G='DisplayString'
_F='not-accessible'
_E='tn3270sIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-TN3270SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_Q,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoTn3270ServerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,54))
if mibBuilder.loadTexts:ciscoTn3270ServerMIB.setRevisions(('1997-01-22 00:00','1996-09-12 00:00'))
class Tn3270sUnsigned32(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class Tn3270sTCPPort(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class Tn3270sPUIndex(Tn3270sUnsigned32):status=_A
class Tn3270sLUIndex(Tn3270sUnsigned32):status=_A
class Tn3270sCpuCard(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,16))
_Tn3270sObjects_ObjectIdentity=ObjectIdentity
tn3270sObjects=_Tn3270sObjects_ObjectIdentity((1,3,6,1,4,1,9,9,54,1))
_Tn3270sGlobal_ObjectIdentity=ObjectIdentity
tn3270sGlobal=_Tn3270sGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,1))
_Tn3270sGlobalTable_Object=MibTable
tn3270sGlobalTable=_Tn3270sGlobalTable_Object((1,3,6,1,4,1,9,9,54,1,1,1))
if mibBuilder.loadTexts:tn3270sGlobalTable.setStatus(_A)
_Tn3270sGlobalEntry_Object=MibTableRow
tn3270sGlobalEntry=_Tn3270sGlobalEntry_Object((1,3,6,1,4,1,9,9,54,1,1,1,1))
tn3270sGlobalEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:tn3270sGlobalEntry.setStatus(_A)
_Tn3270sIndex_Type=Tn3270sUnsigned32
_Tn3270sIndex_Object=MibTableColumn
tn3270sIndex=_Tn3270sIndex_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,1),_Tn3270sIndex_Type())
tn3270sIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sIndex.setStatus(_A)
_Tn3270sCpuCard_Type=Tn3270sCpuCard
_Tn3270sCpuCard_Object=MibTableColumn
tn3270sCpuCard=_Tn3270sCpuCard_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,2),_Tn3270sCpuCard_Type())
tn3270sCpuCard.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sCpuCard.setStatus(_A)
class _Tn3270sMaxLus_Type(Tn3270sUnsigned32):subtypeSpec=Tn3270sUnsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Tn3270sMaxLus_Type.__name__=_R
_Tn3270sMaxLus_Object=MibTableColumn
tn3270sMaxLus=_Tn3270sMaxLus_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,3),_Tn3270sMaxLus_Type())
tn3270sMaxLus.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sMaxLus.setStatus(_A)
class _Tn3270sLusInUse_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270sLusInUse_Type.__name__=_Q
_Tn3270sLusInUse_Object=MibTableColumn
tn3270sLusInUse=_Tn3270sLusInUse_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,4),_Tn3270sLusInUse_Type())
tn3270sLusInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLusInUse.setStatus(_A)
_Tn3270sStartupTime_Type=TimeStamp
_Tn3270sStartupTime_Object=MibTableColumn
tn3270sStartupTime=_Tn3270sStartupTime_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,5),_Tn3270sStartupTime_Type())
tn3270sStartupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStartupTime.setStatus(_A)
_Tn3270sGlobalTcpPort_Type=Tn3270sTCPPort
_Tn3270sGlobalTcpPort_Object=MibTableColumn
tn3270sGlobalTcpPort=_Tn3270sGlobalTcpPort_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,6),_Tn3270sGlobalTcpPort_Type())
tn3270sGlobalTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sGlobalTcpPort.setStatus(_A)
class _Tn3270sGlobalIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Tn3270sGlobalIdleTimeout_Type.__name__=_D
_Tn3270sGlobalIdleTimeout_Object=MibTableColumn
tn3270sGlobalIdleTimeout=_Tn3270sGlobalIdleTimeout_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,7),_Tn3270sGlobalIdleTimeout_Type())
tn3270sGlobalIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sGlobalIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:tn3270sGlobalIdleTimeout.setUnits(_H)
class _Tn3270sGlobalKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_Tn3270sGlobalKeepAlive_Type.__name__=_D
_Tn3270sGlobalKeepAlive_Object=MibTableColumn
tn3270sGlobalKeepAlive=_Tn3270sGlobalKeepAlive_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,8),_Tn3270sGlobalKeepAlive_Type())
tn3270sGlobalKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sGlobalKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:tn3270sGlobalKeepAlive.setUnits(_H)
class _Tn3270sGlobalUnbindAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keep',1),(_S,2)))
_Tn3270sGlobalUnbindAction_Type.__name__=_D
_Tn3270sGlobalUnbindAction_Object=MibTableColumn
tn3270sGlobalUnbindAction=_Tn3270sGlobalUnbindAction_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,9),_Tn3270sGlobalUnbindAction_Type())
tn3270sGlobalUnbindAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sGlobalUnbindAction.setStatus(_A)
class _Tn3270sGlobalGenericPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('deny',2)))
_Tn3270sGlobalGenericPool_Type.__name__=_D
_Tn3270sGlobalGenericPool_Object=MibTableColumn
tn3270sGlobalGenericPool=_Tn3270sGlobalGenericPool_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,10),_Tn3270sGlobalGenericPool_Type())
tn3270sGlobalGenericPool.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sGlobalGenericPool.setStatus(_A)
_Tn3270sTimingMarkSupported_Type=TruthValue
_Tn3270sTimingMarkSupported_Object=MibTableColumn
tn3270sTimingMarkSupported=_Tn3270sTimingMarkSupported_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,11),_Tn3270sTimingMarkSupported_Type())
tn3270sTimingMarkSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sTimingMarkSupported.setStatus(_A)
_Tn3270sRunningTime_Type=Tn3270sUnsigned32
_Tn3270sRunningTime_Object=MibTableColumn
tn3270sRunningTime=_Tn3270sRunningTime_Object((1,3,6,1,4,1,9,9,54,1,1,1,1,12),_Tn3270sRunningTime_Type())
tn3270sRunningTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sRunningTime.setStatus(_A)
if mibBuilder.loadTexts:tn3270sRunningTime.setUnits(_H)
_Tn3270sStats_ObjectIdentity=ObjectIdentity
tn3270sStats=_Tn3270sStats_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,2))
_Tn3270sStatsTable_Object=MibTable
tn3270sStatsTable=_Tn3270sStatsTable_Object((1,3,6,1,4,1,9,9,54,1,2,1))
if mibBuilder.loadTexts:tn3270sStatsTable.setStatus(_A)
_Tn3270sStatsEntry_Object=MibTableRow
tn3270sStatsEntry=_Tn3270sStatsEntry_Object((1,3,6,1,4,1,9,9,54,1,2,1,1))
tn3270sStatsEntry.setIndexNames((0,_B,_E),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:tn3270sStatsEntry.setStatus(_A)
_Tn3270sStatsServerAddr_Type=IpAddress
_Tn3270sStatsServerAddr_Object=MibTableColumn
tn3270sStatsServerAddr=_Tn3270sStatsServerAddr_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,1),_Tn3270sStatsServerAddr_Type())
tn3270sStatsServerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sStatsServerAddr.setStatus(_A)
_Tn3270sStatsServerTcpPort_Type=Tn3270sTCPPort
_Tn3270sStatsServerTcpPort_Object=MibTableColumn
tn3270sStatsServerTcpPort=_Tn3270sStatsServerTcpPort_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,2),_Tn3270sStatsServerTcpPort_Type())
tn3270sStatsServerTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sStatsServerTcpPort.setStatus(_A)
_Tn3270sStatsMaxSess_Type=Gauge32
_Tn3270sStatsMaxSess_Object=MibTableColumn
tn3270sStatsMaxSess=_Tn3270sStatsMaxSess_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,3),_Tn3270sStatsMaxSess_Type())
tn3270sStatsMaxSess.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsMaxSess.setStatus(_A)
_Tn3270sStatsSpareSess_Type=Gauge32
_Tn3270sStatsSpareSess_Object=MibTableColumn
tn3270sStatsSpareSess=_Tn3270sStatsSpareSess_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,4),_Tn3270sStatsSpareSess_Type())
tn3270sStatsSpareSess.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsSpareSess.setStatus(_A)
_Tn3270sStatsConnectsIn_Type=Counter32
_Tn3270sStatsConnectsIn_Object=MibTableColumn
tn3270sStatsConnectsIn=_Tn3270sStatsConnectsIn_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,5),_Tn3270sStatsConnectsIn_Type())
tn3270sStatsConnectsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsConnectsIn.setStatus(_A)
_Tn3270sStatsDisconnects_Type=Counter32
_Tn3270sStatsDisconnects_Object=MibTableColumn
tn3270sStatsDisconnects=_Tn3270sStatsDisconnects_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,6),_Tn3270sStatsDisconnects_Type())
tn3270sStatsDisconnects.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsDisconnects.setStatus(_A)
_Tn3270sStatsTN3270ConnectsFailed_Type=Counter32
_Tn3270sStatsTN3270ConnectsFailed_Object=MibTableColumn
tn3270sStatsTN3270ConnectsFailed=_Tn3270sStatsTN3270ConnectsFailed_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,7),_Tn3270sStatsTN3270ConnectsFailed_Type())
tn3270sStatsTN3270ConnectsFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsTN3270ConnectsFailed.setStatus(_A)
_Tn3270sStatsInboundChains_Type=Counter32
_Tn3270sStatsInboundChains_Object=MibTableColumn
tn3270sStatsInboundChains=_Tn3270sStatsInboundChains_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,8),_Tn3270sStatsInboundChains_Type())
tn3270sStatsInboundChains.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsInboundChains.setStatus(_A)
_Tn3270sStatsOutboundChains_Type=Counter32
_Tn3270sStatsOutboundChains_Object=MibTableColumn
tn3270sStatsOutboundChains=_Tn3270sStatsOutboundChains_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,9),_Tn3270sStatsOutboundChains_Type())
tn3270sStatsOutboundChains.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsOutboundChains.setStatus(_A)
_Tn3270sStatsSampledHostResponses_Type=Counter32
_Tn3270sStatsSampledHostResponses_Object=MibTableColumn
tn3270sStatsSampledHostResponses=_Tn3270sStatsSampledHostResponses_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,10),_Tn3270sStatsSampledHostResponses_Type())
tn3270sStatsSampledHostResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsSampledHostResponses.setStatus(_A)
_Tn3270sStatsNetSampledHostResponseTime_Type=Tn3270sUnsigned32
_Tn3270sStatsNetSampledHostResponseTime_Object=MibTableColumn
tn3270sStatsNetSampledHostResponseTime=_Tn3270sStatsNetSampledHostResponseTime_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,11),_Tn3270sStatsNetSampledHostResponseTime_Type())
tn3270sStatsNetSampledHostResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsNetSampledHostResponseTime.setStatus(_A)
if mibBuilder.loadTexts:tn3270sStatsNetSampledHostResponseTime.setUnits(_W)
_Tn3270sStatsSampledClientResponses_Type=Counter32
_Tn3270sStatsSampledClientResponses_Object=MibTableColumn
tn3270sStatsSampledClientResponses=_Tn3270sStatsSampledClientResponses_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,12),_Tn3270sStatsSampledClientResponses_Type())
tn3270sStatsSampledClientResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsSampledClientResponses.setStatus(_A)
_Tn3270sStatsNetSampledClientResponseTime_Type=Tn3270sUnsigned32
_Tn3270sStatsNetSampledClientResponseTime_Object=MibTableColumn
tn3270sStatsNetSampledClientResponseTime=_Tn3270sStatsNetSampledClientResponseTime_Object((1,3,6,1,4,1,9,9,54,1,2,1,1,13),_Tn3270sStatsNetSampledClientResponseTime_Type())
tn3270sStatsNetSampledClientResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sStatsNetSampledClientResponseTime.setStatus(_A)
if mibBuilder.loadTexts:tn3270sStatsNetSampledClientResponseTime.setUnits(_W)
_Tn3270sPu_ObjectIdentity=ObjectIdentity
tn3270sPu=_Tn3270sPu_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,3))
_Tn3270sPuTable_Object=MibTable
tn3270sPuTable=_Tn3270sPuTable_Object((1,3,6,1,4,1,9,9,54,1,3,1))
if mibBuilder.loadTexts:tn3270sPuTable.setStatus(_A)
_Tn3270sPuEntry_Object=MibTableRow
tn3270sPuEntry=_Tn3270sPuEntry_Object((1,3,6,1,4,1,9,9,54,1,3,1,1))
tn3270sPuEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:tn3270sPuEntry.setStatus(_A)
_Tn3270sPuIndex_Type=Tn3270sPUIndex
_Tn3270sPuIndex_Object=MibTableColumn
tn3270sPuIndex=_Tn3270sPuIndex_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,1),_Tn3270sPuIndex_Type())
tn3270sPuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sPuIndex.setStatus(_A)
_Tn3270sPuIpAddr_Type=IpAddress
_Tn3270sPuIpAddr_Object=MibTableColumn
tn3270sPuIpAddr=_Tn3270sPuIpAddr_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,2),_Tn3270sPuIpAddr_Type())
tn3270sPuIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIpAddr.setStatus(_A)
_Tn3270sPuTcpPort_Type=Tn3270sTCPPort
_Tn3270sPuTcpPort_Object=MibTableColumn
tn3270sPuTcpPort=_Tn3270sPuTcpPort_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,3),_Tn3270sPuTcpPort_Type())
tn3270sPuTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuTcpPort.setStatus(_A)
class _Tn3270sPuIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270sPuIdleTimeout_Type.__name__=_D
_Tn3270sPuIdleTimeout_Object=MibTableColumn
tn3270sPuIdleTimeout=_Tn3270sPuIdleTimeout_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,4),_Tn3270sPuIdleTimeout_Type())
tn3270sPuIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIdleTimeout.setStatus(_A)
class _Tn3270sPuKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270sPuKeepAlive_Type.__name__=_D
_Tn3270sPuKeepAlive_Object=MibTableColumn
tn3270sPuKeepAlive=_Tn3270sPuKeepAlive_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,5),_Tn3270sPuKeepAlive_Type())
tn3270sPuKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuKeepAlive.setStatus(_A)
class _Tn3270sPuUnbindAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('keep',1),(_S,2),(_X,3)))
_Tn3270sPuUnbindAction_Type.__name__=_D
_Tn3270sPuUnbindAction_Object=MibTableColumn
tn3270sPuUnbindAction=_Tn3270sPuUnbindAction_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,6),_Tn3270sPuUnbindAction_Type())
tn3270sPuUnbindAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuUnbindAction.setStatus(_A)
class _Tn3270sPuGenericPool_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('deny',2),(_X,3)))
_Tn3270sPuGenericPool_Type.__name__=_D
_Tn3270sPuGenericPool_Object=MibTableColumn
tn3270sPuGenericPool=_Tn3270sPuGenericPool_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,7),_Tn3270sPuGenericPool_Type())
tn3270sPuGenericPool.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuGenericPool.setStatus(_A)
class _Tn3270sPuState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('shut',1),('reset',2),(_Y,3),('test',4),('xid',5),('pActpu',6),(_Z,7),('actBusy',8)))
_Tn3270sPuState_Type.__name__=_D
_Tn3270sPuState_Object=MibTableColumn
tn3270sPuState=_Tn3270sPuState_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,8),_Tn3270sPuState_Type())
tn3270sPuState.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuState.setStatus(_A)
class _Tn3270sPuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dlur',1),('direct',2)))
_Tn3270sPuType_Type.__name__=_D
_Tn3270sPuType_Object=MibTableColumn
tn3270sPuType=_Tn3270sPuType_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,9),_Tn3270sPuType_Type())
tn3270sPuType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuType.setStatus(_A)
class _Tn3270sPuLuSeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_Tn3270sPuLuSeed_Type.__name__=_G
_Tn3270sPuLuSeed_Object=MibTableColumn
tn3270sPuLuSeed=_Tn3270sPuLuSeed_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,10),_Tn3270sPuLuSeed_Type())
tn3270sPuLuSeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuLuSeed.setStatus(_A)
class _Tn3270sLocalSapAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_Tn3270sLocalSapAddress_Type.__name__=_D
_Tn3270sLocalSapAddress_Object=MibTableColumn
tn3270sLocalSapAddress=_Tn3270sLocalSapAddress_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,11),_Tn3270sLocalSapAddress_Type())
tn3270sLocalSapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLocalSapAddress.setStatus(_A)
class _Tn3270sRemoteSapAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_Tn3270sRemoteSapAddress_Type.__name__=_D
_Tn3270sRemoteSapAddress_Object=MibTableColumn
tn3270sRemoteSapAddress=_Tn3270sRemoteSapAddress_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,12),_Tn3270sRemoteSapAddress_Type())
tn3270sRemoteSapAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sRemoteSapAddress.setStatus(_A)
_Tn3270sRemoteMacAddress_Type=MacAddress
_Tn3270sRemoteMacAddress_Object=MibTableColumn
tn3270sRemoteMacAddress=_Tn3270sRemoteMacAddress_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,13),_Tn3270sRemoteMacAddress_Type())
tn3270sRemoteMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sRemoteMacAddress.setStatus(_A)
class _Tn3270sPuIpPrecedenceScreen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Tn3270sPuIpPrecedenceScreen_Type.__name__=_D
_Tn3270sPuIpPrecedenceScreen_Object=MibTableColumn
tn3270sPuIpPrecedenceScreen=_Tn3270sPuIpPrecedenceScreen_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,14),_Tn3270sPuIpPrecedenceScreen_Type())
tn3270sPuIpPrecedenceScreen.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIpPrecedenceScreen.setStatus(_A)
class _Tn3270sPuIpPrecedencePrinter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Tn3270sPuIpPrecedencePrinter_Type.__name__=_D
_Tn3270sPuIpPrecedencePrinter_Object=MibTableColumn
tn3270sPuIpPrecedencePrinter=_Tn3270sPuIpPrecedencePrinter_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,15),_Tn3270sPuIpPrecedencePrinter_Type())
tn3270sPuIpPrecedencePrinter.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIpPrecedencePrinter.setStatus(_A)
class _Tn3270sPuIpTosScreen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tn3270sPuIpTosScreen_Type.__name__=_D
_Tn3270sPuIpTosScreen_Object=MibTableColumn
tn3270sPuIpTosScreen=_Tn3270sPuIpTosScreen_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,16),_Tn3270sPuIpTosScreen_Type())
tn3270sPuIpTosScreen.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIpTosScreen.setStatus(_A)
class _Tn3270sPuIpTosPrinter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Tn3270sPuIpTosPrinter_Type.__name__=_D
_Tn3270sPuIpTosPrinter_Object=MibTableColumn
tn3270sPuIpTosPrinter=_Tn3270sPuIpTosPrinter_Object((1,3,6,1,4,1,9,9,54,1,3,1,1,17),_Tn3270sPuIpTosPrinter_Type())
tn3270sPuIpTosPrinter.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuIpTosPrinter.setStatus(_A)
_Tn3270sIp_ObjectIdentity=ObjectIdentity
tn3270sIp=_Tn3270sIp_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,4))
_Tn3270sIpTable_Object=MibTable
tn3270sIpTable=_Tn3270sIpTable_Object((1,3,6,1,4,1,9,9,54,1,4,1))
if mibBuilder.loadTexts:tn3270sIpTable.setStatus(_A)
_Tn3270sIpEntry_Object=MibTableRow
tn3270sIpEntry=_Tn3270sIpEntry_Object((1,3,6,1,4,1,9,9,54,1,4,1,1))
tn3270sIpEntry.setIndexNames((0,_B,_E),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:tn3270sIpEntry.setStatus(_A)
_Tn3270sIpClientAddr_Type=IpAddress
_Tn3270sIpClientAddr_Object=MibTableColumn
tn3270sIpClientAddr=_Tn3270sIpClientAddr_Object((1,3,6,1,4,1,9,9,54,1,4,1,1,1),_Tn3270sIpClientAddr_Type())
tn3270sIpClientAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sIpClientAddr.setStatus(_A)
_Tn3270sIpClientTcpPort_Type=Tn3270sTCPPort
_Tn3270sIpClientTcpPort_Object=MibTableColumn
tn3270sIpClientTcpPort=_Tn3270sIpClientTcpPort_Object((1,3,6,1,4,1,9,9,54,1,4,1,1,2),_Tn3270sIpClientTcpPort_Type())
tn3270sIpClientTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sIpClientTcpPort.setStatus(_A)
_Tn3270sIpPuIndex_Type=Tn3270sPUIndex
_Tn3270sIpPuIndex_Object=MibTableColumn
tn3270sIpPuIndex=_Tn3270sIpPuIndex_Object((1,3,6,1,4,1,9,9,54,1,4,1,1,3),_Tn3270sIpPuIndex_Type())
tn3270sIpPuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpPuIndex.setStatus(_A)
_Tn3270sIpLuIndex_Type=Tn3270sLUIndex
_Tn3270sIpLuIndex_Object=MibTableColumn
tn3270sIpLuIndex=_Tn3270sIpLuIndex_Object((1,3,6,1,4,1,9,9,54,1,4,1,1,4),_Tn3270sIpLuIndex_Type())
tn3270sIpLuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpLuIndex.setStatus(_A)
_Tn3270sLu_ObjectIdentity=ObjectIdentity
tn3270sLu=_Tn3270sLu_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,5))
_Tn3270sLuTable_Object=MibTable
tn3270sLuTable=_Tn3270sLuTable_Object((1,3,6,1,4,1,9,9,54,1,5,1))
if mibBuilder.loadTexts:tn3270sLuTable.setStatus(_A)
_Tn3270sLuEntry_Object=MibTableRow
tn3270sLuEntry=_Tn3270sLuEntry_Object((1,3,6,1,4,1,9,9,54,1,5,1,1))
tn3270sLuEntry.setIndexNames((0,_B,_E),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:tn3270sLuEntry.setStatus(_A)
_Tn3270sLuPuIndex_Type=Tn3270sPUIndex
_Tn3270sLuPuIndex_Object=MibTableColumn
tn3270sLuPuIndex=_Tn3270sLuPuIndex_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,1),_Tn3270sLuPuIndex_Type())
tn3270sLuPuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sLuPuIndex.setStatus(_A)
_Tn3270sLuIndex_Type=Tn3270sLUIndex
_Tn3270sLuIndex_Object=MibTableColumn
tn3270sLuIndex=_Tn3270sLuIndex_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,2),_Tn3270sLuIndex_Type())
tn3270sLuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tn3270sLuIndex.setStatus(_A)
_Tn3270sLuClientAddr_Type=IpAddress
_Tn3270sLuClientAddr_Object=MibTableColumn
tn3270sLuClientAddr=_Tn3270sLuClientAddr_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,3),_Tn3270sLuClientAddr_Type())
tn3270sLuClientAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuClientAddr.setStatus(_A)
_Tn3270sLuClientTcpPort_Type=Tn3270sTCPPort
_Tn3270sLuClientTcpPort_Object=MibTableColumn
tn3270sLuClientTcpPort=_Tn3270sLuClientTcpPort_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,4),_Tn3270sLuClientTcpPort_Type())
tn3270sLuClientTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuClientTcpPort.setStatus(_A)
class _Tn3270sLuTelnetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tn3270',1),('tn3270e',2),('neverConnect',3)))
_Tn3270sLuTelnetType_Type.__name__=_D
_Tn3270sLuTelnetType_Object=MibTableColumn
tn3270sLuTelnetType=_Tn3270sLuTelnetType_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,5),_Tn3270sLuTelnetType_Type())
tn3270sLuTelnetType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuTelnetType.setStatus(_A)
class _Tn3270sLuTermModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_Tn3270sLuTermModel_Type.__name__=_G
_Tn3270sLuTermModel_Object=MibTableColumn
tn3270sLuTermModel=_Tn3270sLuTermModel_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,6),_Tn3270sLuTermModel_Type())
tn3270sLuTermModel.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuTermModel.setStatus(_A)
class _Tn3270sLuState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_Y,1),(_Z,2),('pSdt',3),('actSession',4),('pActlu',5),('pNotifyAv',6),('pNotifyUa',7),('pReset',8),('pPsid',9),('pBind',10),('pUnbind',11),('unbindWt',12),('sdtWt',13)))
_Tn3270sLuState_Type.__name__=_D
_Tn3270sLuState_Object=MibTableColumn
tn3270sLuState=_Tn3270sLuState_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,7),_Tn3270sLuState_Type())
tn3270sLuState.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuState.setStatus(_A)
class _Tn3270sLuCurInbPacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Tn3270sLuCurInbPacing_Type.__name__=_D
_Tn3270sLuCurInbPacing_Object=MibTableColumn
tn3270sLuCurInbPacing=_Tn3270sLuCurInbPacing_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,8),_Tn3270sLuCurInbPacing_Type())
tn3270sLuCurInbPacing.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuCurInbPacing.setStatus(_A)
class _Tn3270sLuCurInbQsize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Tn3270sLuCurInbQsize_Type.__name__=_D
_Tn3270sLuCurInbQsize_Object=MibTableColumn
tn3270sLuCurInbQsize=_Tn3270sLuCurInbQsize_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,9),_Tn3270sLuCurInbQsize_Type())
tn3270sLuCurInbQsize.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuCurInbQsize.setStatus(_A)
class _Tn3270sLuCurOutQsize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Tn3270sLuCurOutQsize_Type.__name__=_D
_Tn3270sLuCurOutQsize_Object=MibTableColumn
tn3270sLuCurOutQsize=_Tn3270sLuCurOutQsize_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,10),_Tn3270sLuCurOutQsize_Type())
tn3270sLuCurOutQsize.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuCurOutQsize.setStatus(_A)
class _Tn3270sLuIdleTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270sLuIdleTime_Type.__name__=_D
_Tn3270sLuIdleTime_Object=MibTableColumn
tn3270sLuIdleTime=_Tn3270sLuIdleTime_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,11),_Tn3270sLuIdleTime_Type())
tn3270sLuIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuIdleTime.setStatus(_A)
if mibBuilder.loadTexts:tn3270sLuIdleTime.setUnits(_H)
class _Tn3270sLuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_Tn3270sLuType_Type.__name__=_D
_Tn3270sLuType_Object=MibTableColumn
tn3270sLuType=_Tn3270sLuType_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,12),_Tn3270sLuType_Type())
tn3270sLuType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuType.setStatus(_A)
class _Tn3270sLuAppnLinkIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_Tn3270sLuAppnLinkIndex_Type.__name__=_G
_Tn3270sLuAppnLinkIndex_Object=MibTableColumn
tn3270sLuAppnLinkIndex=_Tn3270sLuAppnLinkIndex_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,13),_Tn3270sLuAppnLinkIndex_Type())
tn3270sLuAppnLinkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuAppnLinkIndex.setStatus(_A)
class _Tn3270sLuLfsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Tn3270sLuLfsid_Type.__name__=_D
_Tn3270sLuLfsid_Object=MibTableColumn
tn3270sLuLfsid=_Tn3270sLuLfsid_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,14),_Tn3270sLuLfsid_Type())
tn3270sLuLfsid.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuLfsid.setStatus(_A)
_Tn3270sLuLastEvent_Type=TimeStamp
_Tn3270sLuLastEvent_Object=MibTableColumn
tn3270sLuLastEvent=_Tn3270sLuLastEvent_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,15),_Tn3270sLuLastEvent_Type())
tn3270sLuLastEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuLastEvent.setStatus(_J)
class _Tn3270sLuEvents_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Tn3270sLuEvents_Type.__name__=_P
_Tn3270sLuEvents_Object=MibTableColumn
tn3270sLuEvents=_Tn3270sLuEvents_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,16),_Tn3270sLuEvents_Type())
tn3270sLuEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuEvents.setStatus(_A)
_Tn3270sLuNail_Type=TruthValue
_Tn3270sLuNail_Object=MibTableColumn
tn3270sLuNail=_Tn3270sLuNail_Object((1,3,6,1,4,1,9,9,54,1,5,1,1,17),_Tn3270sLuNail_Type())
tn3270sLuNail.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sLuNail.setStatus(_A)
_Tn3270sPuNail_ObjectIdentity=ObjectIdentity
tn3270sPuNail=_Tn3270sPuNail_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,6))
_Tn3270sPuNailTable_Object=MibTable
tn3270sPuNailTable=_Tn3270sPuNailTable_Object((1,3,6,1,4,1,9,9,54,1,6,1))
if mibBuilder.loadTexts:tn3270sPuNailTable.setStatus(_A)
_Tn3270sPuNailEntry_Object=MibTableRow
tn3270sPuNailEntry=_Tn3270sPuNailEntry_Object((1,3,6,1,4,1,9,9,54,1,6,1,1))
tn3270sPuNailEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:tn3270sPuNailEntry.setStatus(_A)
_Tn3270sPuNailClientIpAddr_Type=IpAddress
_Tn3270sPuNailClientIpAddr_Object=MibTableColumn
tn3270sPuNailClientIpAddr=_Tn3270sPuNailClientIpAddr_Object((1,3,6,1,4,1,9,9,54,1,6,1,1,1),_Tn3270sPuNailClientIpAddr_Type())
tn3270sPuNailClientIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuNailClientIpAddr.setStatus(_A)
_Tn3270sPuNailClientIpMask_Type=IpAddress
_Tn3270sPuNailClientIpMask_Object=MibTableColumn
tn3270sPuNailClientIpMask=_Tn3270sPuNailClientIpMask_Object((1,3,6,1,4,1,9,9,54,1,6,1,1,2),_Tn3270sPuNailClientIpMask_Type())
tn3270sPuNailClientIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuNailClientIpMask.setStatus(_A)
class _Tn3270sPuNailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_Tn3270sPuNailType_Type.__name__=_D
_Tn3270sPuNailType_Object=MibTableColumn
tn3270sPuNailType=_Tn3270sPuNailType_Object((1,3,6,1,4,1,9,9,54,1,6,1,1,3),_Tn3270sPuNailType_Type())
tn3270sPuNailType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuNailType.setStatus(_A)
class _Tn3270sPuNailLuFirst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Tn3270sPuNailLuFirst_Type.__name__=_D
_Tn3270sPuNailLuFirst_Object=MibTableColumn
tn3270sPuNailLuFirst=_Tn3270sPuNailLuFirst_Object((1,3,6,1,4,1,9,9,54,1,6,1,1,4),_Tn3270sPuNailLuFirst_Type())
tn3270sPuNailLuFirst.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuNailLuFirst.setStatus(_A)
class _Tn3270sPuNailLuLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Tn3270sPuNailLuLast_Type.__name__=_D
_Tn3270sPuNailLuLast_Object=MibTableColumn
tn3270sPuNailLuLast=_Tn3270sPuNailLuLast_Object((1,3,6,1,4,1,9,9,54,1,6,1,1,5),_Tn3270sPuNailLuLast_Type())
tn3270sPuNailLuLast.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sPuNailLuLast.setStatus(_A)
_Tn3270sIpNail_ObjectIdentity=ObjectIdentity
tn3270sIpNail=_Tn3270sIpNail_ObjectIdentity((1,3,6,1,4,1,9,9,54,1,7))
_Tn3270sIpNailTable_Object=MibTable
tn3270sIpNailTable=_Tn3270sIpNailTable_Object((1,3,6,1,4,1,9,9,54,1,7,1))
if mibBuilder.loadTexts:tn3270sIpNailTable.setStatus(_A)
_Tn3270sIpNailEntry_Object=MibTableRow
tn3270sIpNailEntry=_Tn3270sIpNailEntry_Object((1,3,6,1,4,1,9,9,54,1,7,1,1))
tn3270sIpNailEntry.setIndexNames((0,_B,_E),(0,_B,_M),(0,_B,_I),(0,_B,_N))
if mibBuilder.loadTexts:tn3270sIpNailEntry.setStatus(_A)
_Tn3270sIpNailClientIpAddr_Type=IpAddress
_Tn3270sIpNailClientIpAddr_Object=MibTableColumn
tn3270sIpNailClientIpAddr=_Tn3270sIpNailClientIpAddr_Object((1,3,6,1,4,1,9,9,54,1,7,1,1,1),_Tn3270sIpNailClientIpAddr_Type())
tn3270sIpNailClientIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpNailClientIpAddr.setStatus(_A)
_Tn3270sIpNailClientIpMask_Type=IpAddress
_Tn3270sIpNailClientIpMask_Object=MibTableColumn
tn3270sIpNailClientIpMask=_Tn3270sIpNailClientIpMask_Object((1,3,6,1,4,1,9,9,54,1,7,1,1,2),_Tn3270sIpNailClientIpMask_Type())
tn3270sIpNailClientIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpNailClientIpMask.setStatus(_A)
class _Tn3270sIpNailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),(_f,2)))
_Tn3270sIpNailType_Type.__name__=_D
_Tn3270sIpNailType_Object=MibTableColumn
tn3270sIpNailType=_Tn3270sIpNailType_Object((1,3,6,1,4,1,9,9,54,1,7,1,1,3),_Tn3270sIpNailType_Type())
tn3270sIpNailType.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpNailType.setStatus(_A)
class _Tn3270sIpNailLuFirst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Tn3270sIpNailLuFirst_Type.__name__=_D
_Tn3270sIpNailLuFirst_Object=MibTableColumn
tn3270sIpNailLuFirst=_Tn3270sIpNailLuFirst_Object((1,3,6,1,4,1,9,9,54,1,7,1,1,4),_Tn3270sIpNailLuFirst_Type())
tn3270sIpNailLuFirst.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpNailLuFirst.setStatus(_A)
class _Tn3270sIpNailLuLast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Tn3270sIpNailLuLast_Type.__name__=_D
_Tn3270sIpNailLuLast_Object=MibTableColumn
tn3270sIpNailLuLast=_Tn3270sIpNailLuLast_Object((1,3,6,1,4,1,9,9,54,1,7,1,1,5),_Tn3270sIpNailLuLast_Type())
tn3270sIpNailLuLast.setMaxAccess(_C)
if mibBuilder.loadTexts:tn3270sIpNailLuLast.setStatus(_A)
_CiscoTn3270ServerMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoTn3270ServerMIBNotificationPrefix=_CiscoTn3270ServerMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,54,2))
_CiscoTn3270ServerMIBConformance_ObjectIdentity=ObjectIdentity
ciscoTn3270ServerMIBConformance=_CiscoTn3270ServerMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,54,3))
_CiscoTn3270ServerMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTn3270ServerMIBCompliances=_CiscoTn3270ServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,54,3,1))
_CiscoTn3270ServerMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTn3270ServerMIBGroups=_CiscoTn3270ServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,54,3,2))
ciscoTn3270ServerMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,54,3,2,1))
ciscoTn3270ServerMIBGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBGroup.setStatus(_A)
ciscoTn3270ServerMIBGroupObsolete=ObjectGroup((1,3,6,1,4,1,9,9,54,3,2,2))
ciscoTn3270ServerMIBGroupObsolete.setObjects((_B,_AT))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBGroupObsolete.setStatus(_J)
ciscoTn3270ServerMIBGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,54,3,2,3))
ciscoTn3270ServerMIBGroupRev1.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_K),(_B,_AZ),(_B,_Aa),(_B,_L),(_B,_Ab),(_B,_M),(_B,_Ac),(_B,_Ad),(_B,_N),(_B,_Ae)))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBGroupRev1.setStatus(_A)
ciscoTn3270ServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,54,3,1,1))
ciscoTn3270ServerMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBCompliance.setStatus(_A)
ciscoTn3270ServerMIBComplianceObsolete=ModuleCompliance((1,3,6,1,4,1,9,9,54,3,1,2))
ciscoTn3270ServerMIBComplianceObsolete.setObjects((_B,_Af))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBComplianceObsolete.setStatus(_J)
ciscoTn3270ServerMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,54,3,1,3))
ciscoTn3270ServerMIBComplianceRev1.setObjects(*((_B,_O),(_B,_Ag)))
if mibBuilder.loadTexts:ciscoTn3270ServerMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_R:Tn3270sUnsigned32,'Tn3270sTCPPort':Tn3270sTCPPort,'Tn3270sPUIndex':Tn3270sPUIndex,'Tn3270sLUIndex':Tn3270sLUIndex,'Tn3270sCpuCard':Tn3270sCpuCard,'ciscoTn3270ServerMIB':ciscoTn3270ServerMIB,'tn3270sObjects':tn3270sObjects,'tn3270sGlobal':tn3270sGlobal,'tn3270sGlobalTable':tn3270sGlobalTable,'tn3270sGlobalEntry':tn3270sGlobalEntry,_E:tn3270sIndex,_g:tn3270sCpuCard,_h:tn3270sMaxLus,_i:tn3270sLusInUse,_j:tn3270sStartupTime,_k:tn3270sGlobalTcpPort,_l:tn3270sGlobalIdleTimeout,_m:tn3270sGlobalKeepAlive,_n:tn3270sGlobalUnbindAction,_o:tn3270sGlobalGenericPool,_p:tn3270sTimingMarkSupported,_q:tn3270sRunningTime,'tn3270sStats':tn3270sStats,'tn3270sStatsTable':tn3270sStatsTable,'tn3270sStatsEntry':tn3270sStatsEntry,_U:tn3270sStatsServerAddr,_V:tn3270sStatsServerTcpPort,_r:tn3270sStatsMaxSess,_s:tn3270sStatsSpareSess,_t:tn3270sStatsConnectsIn,_u:tn3270sStatsDisconnects,_v:tn3270sStatsTN3270ConnectsFailed,_w:tn3270sStatsInboundChains,_x:tn3270sStatsOutboundChains,_y:tn3270sStatsSampledHostResponses,_z:tn3270sStatsNetSampledHostResponseTime,_A0:tn3270sStatsSampledClientResponses,_A1:tn3270sStatsNetSampledClientResponseTime,'tn3270sPu':tn3270sPu,'tn3270sPuTable':tn3270sPuTable,'tn3270sPuEntry':tn3270sPuEntry,_I:tn3270sPuIndex,_A2:tn3270sPuIpAddr,_A3:tn3270sPuTcpPort,_A4:tn3270sPuIdleTimeout,_A5:tn3270sPuKeepAlive,_A6:tn3270sPuUnbindAction,_A7:tn3270sPuGenericPool,_A8:tn3270sPuState,_A9:tn3270sPuType,_AA:tn3270sPuLuSeed,_AB:tn3270sLocalSapAddress,_AC:tn3270sRemoteSapAddress,_AD:tn3270sRemoteMacAddress,_AU:tn3270sPuIpPrecedenceScreen,_AV:tn3270sPuIpPrecedencePrinter,_AW:tn3270sPuIpTosScreen,_AX:tn3270sPuIpTosPrinter,'tn3270sIp':tn3270sIp,'tn3270sIpTable':tn3270sIpTable,'tn3270sIpEntry':tn3270sIpEntry,_a:tn3270sIpClientAddr,_b:tn3270sIpClientTcpPort,_AE:tn3270sIpPuIndex,_AF:tn3270sIpLuIndex,'tn3270sLu':tn3270sLu,'tn3270sLuTable':tn3270sLuTable,'tn3270sLuEntry':tn3270sLuEntry,_c:tn3270sLuPuIndex,_d:tn3270sLuIndex,_AG:tn3270sLuClientAddr,_AH:tn3270sLuClientTcpPort,_AI:tn3270sLuTelnetType,_AJ:tn3270sLuTermModel,_AK:tn3270sLuState,_AL:tn3270sLuCurInbPacing,_AM:tn3270sLuCurInbQsize,_AN:tn3270sLuCurOutQsize,_AO:tn3270sLuIdleTime,_AP:tn3270sLuType,_AQ:tn3270sLuAppnLinkIndex,_AR:tn3270sLuLfsid,_AT:tn3270sLuLastEvent,_AS:tn3270sLuEvents,_AY:tn3270sLuNail,'tn3270sPuNail':tn3270sPuNail,'tn3270sPuNailTable':tn3270sPuNailTable,'tn3270sPuNailEntry':tn3270sPuNailEntry,_K:tn3270sPuNailClientIpAddr,_AZ:tn3270sPuNailClientIpMask,_Aa:tn3270sPuNailType,_L:tn3270sPuNailLuFirst,_Ab:tn3270sPuNailLuLast,'tn3270sIpNail':tn3270sIpNail,'tn3270sIpNailTable':tn3270sIpNailTable,'tn3270sIpNailEntry':tn3270sIpNailEntry,_M:tn3270sIpNailClientIpAddr,_Ac:tn3270sIpNailClientIpMask,_Ad:tn3270sIpNailType,_N:tn3270sIpNailLuFirst,_Ae:tn3270sIpNailLuLast,'ciscoTn3270ServerMIBNotificationPrefix':ciscoTn3270ServerMIBNotificationPrefix,'ciscoTn3270ServerMIBConformance':ciscoTn3270ServerMIBConformance,'ciscoTn3270ServerMIBCompliances':ciscoTn3270ServerMIBCompliances,'ciscoTn3270ServerMIBCompliance':ciscoTn3270ServerMIBCompliance,'ciscoTn3270ServerMIBComplianceObsolete':ciscoTn3270ServerMIBComplianceObsolete,'ciscoTn3270ServerMIBComplianceRev1':ciscoTn3270ServerMIBComplianceRev1,'ciscoTn3270ServerMIBGroups':ciscoTn3270ServerMIBGroups,_O:ciscoTn3270ServerMIBGroup,_Af:ciscoTn3270ServerMIBGroupObsolete,_Ag:ciscoTn3270ServerMIBGroupRev1})