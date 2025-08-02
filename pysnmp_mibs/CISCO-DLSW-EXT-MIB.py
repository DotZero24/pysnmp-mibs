_Aq='cdeTrapControlGroup'
_Ap='cdeMIBFastGroup'
_Ao='cdeMIBCircuitGroup'
_An='cdeMIBInterfaceGroup'
_Am='cdeMIBTConnDirectConfigGroup'
_Al='cdeMIBTConnTcpConfigGroup'
_Ak='cdeMIBTConnOperGroup'
_Aj='cdeMIBTConnConfigGroup'
_Ai='cdeMIBNodeGroup'
_Ah='cdeTrapCntlCircuit'
_Ag='cdeTrapCntlTConn'
_Af='cdeFastTimeToLive'
_Ae='cdeFastOrigin'
_Ad='cdeFastS2CacheId'
_Ac='cdeFastS2TAddress'
_Ab='cdeFastS2TDomain'
_Aa='cdeFastS1CacheId'
_AZ='cdeFastS1RouteInfo'
_AY='cdeFastS1IfIndex'
_AX='cdeCircuitS1IdNum'
_AW='cdeCircuitS1IdBlock'
_AV='cdeCircuitS2Name'
_AU='cdeCircuitS1Name'
_AT='cdeIfType'
_AS='cdeTConnDirectConfigFrameRelayDlci'
_AR='cdeTConnDirectConfigMediaEncap'
_AQ='cdeTConnDirectConfigIfIndex'
_AP='cdeTConnTcpConfigQueueMax'
_AO='cdeTConnOperTDomainType'
_AN='cdeTConnOperPartnerGroupNum'
_AM='cdeTConnOperPartnerBorderPeer'
_AL='cdeTConnOperPartnerPriority'
_AK='cdeTConnOperPartnerCost'
_AJ='cdeTConnConfigDynamicInactivityInterval'
_AI='cdeTConnConfigDynamicNoLlc'
_AH='cdeTConnConfigDynamic'
_AG='cdeTConnConfigDestMac'
_AF='cdeTConnConfigPriority'
_AE='cdeTConnConfigBackupLingerInterval'
_AD='cdeTConnConfigBackupLinger'
_AC='cdeTConnConfigBackupTAddr'
_AB='cdeTConnConfigBackup'
_AA='cdeTConnConfigKeepaliveInterval'
_A9='cdeTConnConfigLFSize'
_A8='cdeTConnConfigCost'
_A7='cdeTConnConfigLocalAck'
_A6='cdeTConnConfigTDomainType'
_A5='cdeNodePeerOnDemandDefaultsTCPQueueMax'
_A4='cdeNodePeerOnDemandDefaultsPriority'
_A3='cdeNodePeerOnDemandDefaultsLFSize'
_A2='cdeNodePeerOnDemandDefaultsKeepaliveInterval'
_A1='cdeNodePeerOnDemandDefaultsInactivityInterval'
_A0='cdeNodePeerOnDemandDefaultsFst'
_z='cdeNodePeerOnDemandDefaultsCost'
_y='cdeNodePromPeerDefaultsTCPQueueMax'
_x='cdeNodePromPeerDefaultsLFSize'
_w='cdeNodePromPeerDefaultsKeepaliveInterval'
_v='cdeNodePromPeerDefaultsDestMac'
_u='cdeNodePromPeerDefaultsCost'
_t='cdeNodePromiscuous'
_s='cdeNodeMaxPacingWindow'
_r='cdeNodeInitPacingWindow'
_q='cdeNodeBiuSegment'
_p='cdeNodePassiveConnect'
_o='cdeNodeKeepaliveInterval'
_n='cdeNodeCost'
_m='cdeNodeBorder'
_l='cdeNodeGroup'
_k='cdeNodeTAddr'
_j='cdeCircuitEntry'
_i='cdeIfEntry'
_h='cdeTConnTcpConfigEntry'
_g='cdeTConnOperEntry'
_f='cdeTConnConfigEntry'
_e='cdeFastS2Sap'
_d='cdeFastS2Mac'
_c='cdeFastS1Sap'
_b='cdeFastS1Mac'
_a='TDomainType'
_Z='directFrameRelay'
_Y='directHdlc'
_X='dlswTConnOperState'
_W='dlswTConnConfigIndex'
_V='dlswCircuitState'
_U='DlciNumber'
_T='TAddress'
_S='MacAddressNC'
_R='not-accessible'
_Q='Minutes'
_P='TCPQueueMax'
_O='Seconds'
_N='LFSize'
_M='DLSW-MIB'
_L='OctetString'
_K='packets'
_J='KeepaliveInterval'
_I='DisplayString'
_H='Cost'
_G='Integer32'
_F='TruthValue'
_E='read-only'
_D='read-create'
_C='read-write'
_B='CISCO-DLSW-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DlciNumber,=mibBuilder.importSymbols('CISCO-FRAME-RELAY-MIB',_U)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SAPType,=mibBuilder.importSymbols('CISCO-TC','SAPType')
DlcType,LFSize,MacAddressNC,TAddress,dlswCircuitEntry,dlswCircuitState,dlswIfEntry,dlswTConnConfigEntry,dlswTConnConfigIndex,dlswTConnOperEntry,dlswTConnOperState,dlswTConnTcpConfigEntry=mibBuilder.importSymbols(_M,'DlcType',_N,_S,_T,'dlswCircuitEntry',_V,'dlswIfEntry','dlswTConnConfigEntry',_W,'dlswTConnOperEntry',_X,'dlswTConnTcpConfigEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention',_F)
ciscoDlswExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,74))
if mibBuilder.loadTexts:ciscoDlswExtMIB.setRevisions(('1997-03-11 00:00',))
class TDomainType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tcp',1),('fst',2),(_Y,3),(_Z,4),('llc2',5)))
class Cost(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
class KeepaliveInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1200))
class TCPQueueMax(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,2000))
_CiscoDlswExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDlswExtMIBObjects=_CiscoDlswExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,74,1))
_CdeDomains_ObjectIdentity=ObjectIdentity
cdeDomains=_CdeDomains_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,1))
_CdeFSTDomain_ObjectIdentity=ObjectIdentity
cdeFSTDomain=_CdeFSTDomain_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,1,1))
_CdeDirectHdlcDomain_ObjectIdentity=ObjectIdentity
cdeDirectHdlcDomain=_CdeDirectHdlcDomain_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,1,2))
_CdeDirectFrameRelayDomain_ObjectIdentity=ObjectIdentity
cdeDirectFrameRelayDomain=_CdeDirectFrameRelayDomain_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,1,3))
_CdeLlc2Domain_ObjectIdentity=ObjectIdentity
cdeLlc2Domain=_CdeLlc2Domain_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,1,4))
_CdeNode_ObjectIdentity=ObjectIdentity
cdeNode=_CdeNode_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,2))
class _CdeNodeTAddr_Type(TAddress):defaultHexValue=''
_CdeNodeTAddr_Type.__name__=_T
_CdeNodeTAddr_Object=MibScalar
cdeNodeTAddr=_CdeNodeTAddr_Object((1,3,6,1,4,1,9,9,74,1,2,1),_CdeNodeTAddr_Type())
cdeNodeTAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeTAddr.setStatus(_A)
class _CdeNodeGroup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CdeNodeGroup_Type.__name__=_G
_CdeNodeGroup_Object=MibScalar
cdeNodeGroup=_CdeNodeGroup_Object((1,3,6,1,4,1,9,9,74,1,2,2),_CdeNodeGroup_Type())
cdeNodeGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeGroup.setStatus(_A)
class _CdeNodeBorder_Type(TruthValue):defaultValue=2
_CdeNodeBorder_Type.__name__=_F
_CdeNodeBorder_Object=MibScalar
cdeNodeBorder=_CdeNodeBorder_Object((1,3,6,1,4,1,9,9,74,1,2,3),_CdeNodeBorder_Type())
cdeNodeBorder.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeBorder.setStatus(_A)
class _CdeNodeCost_Type(Cost):defaultValue=3
_CdeNodeCost_Type.__name__=_H
_CdeNodeCost_Object=MibScalar
cdeNodeCost=_CdeNodeCost_Object((1,3,6,1,4,1,9,9,74,1,2,4),_CdeNodeCost_Type())
cdeNodeCost.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeCost.setStatus(_A)
class _CdeNodeKeepaliveInterval_Type(KeepaliveInterval):defaultValue=30
_CdeNodeKeepaliveInterval_Type.__name__=_J
_CdeNodeKeepaliveInterval_Object=MibScalar
cdeNodeKeepaliveInterval=_CdeNodeKeepaliveInterval_Object((1,3,6,1,4,1,9,9,74,1,2,5),_CdeNodeKeepaliveInterval_Type())
cdeNodeKeepaliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeKeepaliveInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeNodeKeepaliveInterval.setUnits(_O)
class _CdeNodePassiveConnect_Type(TruthValue):defaultValue=2
_CdeNodePassiveConnect_Type.__name__=_F
_CdeNodePassiveConnect_Object=MibScalar
cdeNodePassiveConnect=_CdeNodePassiveConnect_Object((1,3,6,1,4,1,9,9,74,1,2,6),_CdeNodePassiveConnect_Type())
cdeNodePassiveConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePassiveConnect.setStatus(_A)
class _CdeNodeBiuSegment_Type(TruthValue):defaultValue=2
_CdeNodeBiuSegment_Type.__name__=_F
_CdeNodeBiuSegment_Object=MibScalar
cdeNodeBiuSegment=_CdeNodeBiuSegment_Object((1,3,6,1,4,1,9,9,74,1,2,7),_CdeNodeBiuSegment_Type())
cdeNodeBiuSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeBiuSegment.setStatus(_A)
class _CdeNodeInitPacingWindow_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_CdeNodeInitPacingWindow_Type.__name__=_G
_CdeNodeInitPacingWindow_Object=MibScalar
cdeNodeInitPacingWindow=_CdeNodeInitPacingWindow_Object((1,3,6,1,4,1,9,9,74,1,2,8),_CdeNodeInitPacingWindow_Type())
cdeNodeInitPacingWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeInitPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:cdeNodeInitPacingWindow.setUnits(_K)
class _CdeNodeMaxPacingWindow_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_CdeNodeMaxPacingWindow_Type.__name__=_G
_CdeNodeMaxPacingWindow_Object=MibScalar
cdeNodeMaxPacingWindow=_CdeNodeMaxPacingWindow_Object((1,3,6,1,4,1,9,9,74,1,2,9),_CdeNodeMaxPacingWindow_Type())
cdeNodeMaxPacingWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodeMaxPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:cdeNodeMaxPacingWindow.setUnits(_K)
class _CdeNodePromiscuous_Type(TruthValue):defaultValue=2
_CdeNodePromiscuous_Type.__name__=_F
_CdeNodePromiscuous_Object=MibScalar
cdeNodePromiscuous=_CdeNodePromiscuous_Object((1,3,6,1,4,1,9,9,74,1,2,10),_CdeNodePromiscuous_Type())
cdeNodePromiscuous.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromiscuous.setStatus(_A)
class _CdeNodePromPeerDefaultsCost_Type(Cost):defaultValue=3
_CdeNodePromPeerDefaultsCost_Type.__name__=_H
_CdeNodePromPeerDefaultsCost_Object=MibScalar
cdeNodePromPeerDefaultsCost=_CdeNodePromPeerDefaultsCost_Object((1,3,6,1,4,1,9,9,74,1,2,11),_CdeNodePromPeerDefaultsCost_Type())
cdeNodePromPeerDefaultsCost.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsCost.setStatus(_A)
class _CdeNodePromPeerDefaultsDestMac_Type(MacAddressNC):defaultHexValue=''
_CdeNodePromPeerDefaultsDestMac_Type.__name__=_S
_CdeNodePromPeerDefaultsDestMac_Object=MibScalar
cdeNodePromPeerDefaultsDestMac=_CdeNodePromPeerDefaultsDestMac_Object((1,3,6,1,4,1,9,9,74,1,2,12),_CdeNodePromPeerDefaultsDestMac_Type())
cdeNodePromPeerDefaultsDestMac.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsDestMac.setStatus(_A)
class _CdeNodePromPeerDefaultsKeepaliveInterval_Type(KeepaliveInterval):defaultValue=30
_CdeNodePromPeerDefaultsKeepaliveInterval_Type.__name__=_J
_CdeNodePromPeerDefaultsKeepaliveInterval_Object=MibScalar
cdeNodePromPeerDefaultsKeepaliveInterval=_CdeNodePromPeerDefaultsKeepaliveInterval_Object((1,3,6,1,4,1,9,9,74,1,2,13),_CdeNodePromPeerDefaultsKeepaliveInterval_Type())
cdeNodePromPeerDefaultsKeepaliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsKeepaliveInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsKeepaliveInterval.setUnits(_O)
class _CdeNodePromPeerDefaultsLFSize_Type(LFSize):defaultValue=17749
_CdeNodePromPeerDefaultsLFSize_Type.__name__=_N
_CdeNodePromPeerDefaultsLFSize_Object=MibScalar
cdeNodePromPeerDefaultsLFSize=_CdeNodePromPeerDefaultsLFSize_Object((1,3,6,1,4,1,9,9,74,1,2,14),_CdeNodePromPeerDefaultsLFSize_Type())
cdeNodePromPeerDefaultsLFSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsLFSize.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsLFSize.setUnits('bytes')
class _CdeNodePromPeerDefaultsTCPQueueMax_Type(TCPQueueMax):defaultValue=200
_CdeNodePromPeerDefaultsTCPQueueMax_Type.__name__=_P
_CdeNodePromPeerDefaultsTCPQueueMax_Object=MibScalar
cdeNodePromPeerDefaultsTCPQueueMax=_CdeNodePromPeerDefaultsTCPQueueMax_Object((1,3,6,1,4,1,9,9,74,1,2,15),_CdeNodePromPeerDefaultsTCPQueueMax_Type())
cdeNodePromPeerDefaultsTCPQueueMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsTCPQueueMax.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePromPeerDefaultsTCPQueueMax.setUnits(_K)
class _CdeNodePeerOnDemandDefaultsCost_Type(Cost):defaultValue=3
_CdeNodePeerOnDemandDefaultsCost_Type.__name__=_H
_CdeNodePeerOnDemandDefaultsCost_Object=MibScalar
cdeNodePeerOnDemandDefaultsCost=_CdeNodePeerOnDemandDefaultsCost_Object((1,3,6,1,4,1,9,9,74,1,2,16),_CdeNodePeerOnDemandDefaultsCost_Type())
cdeNodePeerOnDemandDefaultsCost.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsCost.setStatus(_A)
class _CdeNodePeerOnDemandDefaultsFst_Type(TruthValue):defaultValue=2
_CdeNodePeerOnDemandDefaultsFst_Type.__name__=_F
_CdeNodePeerOnDemandDefaultsFst_Object=MibScalar
cdeNodePeerOnDemandDefaultsFst=_CdeNodePeerOnDemandDefaultsFst_Object((1,3,6,1,4,1,9,9,74,1,2,17),_CdeNodePeerOnDemandDefaultsFst_Type())
cdeNodePeerOnDemandDefaultsFst.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsFst.setStatus(_A)
class _CdeNodePeerOnDemandDefaultsInactivityInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CdeNodePeerOnDemandDefaultsInactivityInterval_Type.__name__=_G
_CdeNodePeerOnDemandDefaultsInactivityInterval_Object=MibScalar
cdeNodePeerOnDemandDefaultsInactivityInterval=_CdeNodePeerOnDemandDefaultsInactivityInterval_Object((1,3,6,1,4,1,9,9,74,1,2,18),_CdeNodePeerOnDemandDefaultsInactivityInterval_Type())
cdeNodePeerOnDemandDefaultsInactivityInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsInactivityInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsInactivityInterval.setUnits(_Q)
class _CdeNodePeerOnDemandDefaultsKeepaliveInterval_Type(KeepaliveInterval):defaultValue=30
_CdeNodePeerOnDemandDefaultsKeepaliveInterval_Type.__name__=_J
_CdeNodePeerOnDemandDefaultsKeepaliveInterval_Object=MibScalar
cdeNodePeerOnDemandDefaultsKeepaliveInterval=_CdeNodePeerOnDemandDefaultsKeepaliveInterval_Object((1,3,6,1,4,1,9,9,74,1,2,19),_CdeNodePeerOnDemandDefaultsKeepaliveInterval_Type())
cdeNodePeerOnDemandDefaultsKeepaliveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsKeepaliveInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsKeepaliveInterval.setUnits(_O)
class _CdeNodePeerOnDemandDefaultsLFSize_Type(LFSize):defaultValue=17749
_CdeNodePeerOnDemandDefaultsLFSize_Type.__name__=_N
_CdeNodePeerOnDemandDefaultsLFSize_Object=MibScalar
cdeNodePeerOnDemandDefaultsLFSize=_CdeNodePeerOnDemandDefaultsLFSize_Object((1,3,6,1,4,1,9,9,74,1,2,20),_CdeNodePeerOnDemandDefaultsLFSize_Type())
cdeNodePeerOnDemandDefaultsLFSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsLFSize.setStatus(_A)
class _CdeNodePeerOnDemandDefaultsPriority_Type(TruthValue):defaultValue=2
_CdeNodePeerOnDemandDefaultsPriority_Type.__name__=_F
_CdeNodePeerOnDemandDefaultsPriority_Object=MibScalar
cdeNodePeerOnDemandDefaultsPriority=_CdeNodePeerOnDemandDefaultsPriority_Object((1,3,6,1,4,1,9,9,74,1,2,21),_CdeNodePeerOnDemandDefaultsPriority_Type())
cdeNodePeerOnDemandDefaultsPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsPriority.setStatus(_A)
class _CdeNodePeerOnDemandDefaultsTCPQueueMax_Type(TCPQueueMax):defaultValue=200
_CdeNodePeerOnDemandDefaultsTCPQueueMax_Type.__name__=_P
_CdeNodePeerOnDemandDefaultsTCPQueueMax_Object=MibScalar
cdeNodePeerOnDemandDefaultsTCPQueueMax=_CdeNodePeerOnDemandDefaultsTCPQueueMax_Object((1,3,6,1,4,1,9,9,74,1,2,22),_CdeNodePeerOnDemandDefaultsTCPQueueMax_Type())
cdeNodePeerOnDemandDefaultsTCPQueueMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsTCPQueueMax.setStatus(_A)
if mibBuilder.loadTexts:cdeNodePeerOnDemandDefaultsTCPQueueMax.setUnits(_K)
_CdeTConn_ObjectIdentity=ObjectIdentity
cdeTConn=_CdeTConn_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,3))
_CdeTConnConfigTable_Object=MibTable
cdeTConnConfigTable=_CdeTConnConfigTable_Object((1,3,6,1,4,1,9,9,74,1,3,1))
if mibBuilder.loadTexts:cdeTConnConfigTable.setStatus(_A)
_CdeTConnConfigEntry_Object=MibTableRow
cdeTConnConfigEntry=_CdeTConnConfigEntry_Object((1,3,6,1,4,1,9,9,74,1,3,1,1))
if mibBuilder.loadTexts:cdeTConnConfigEntry.setStatus(_A)
class _CdeTConnConfigTDomainType_Type(TDomainType):defaultValue=1
_CdeTConnConfigTDomainType_Type.__name__=_a
_CdeTConnConfigTDomainType_Object=MibTableColumn
cdeTConnConfigTDomainType=_CdeTConnConfigTDomainType_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,1),_CdeTConnConfigTDomainType_Type())
cdeTConnConfigTDomainType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigTDomainType.setStatus(_A)
class _CdeTConnConfigLocalAck_Type(TruthValue):defaultValue=1
_CdeTConnConfigLocalAck_Type.__name__=_F
_CdeTConnConfigLocalAck_Object=MibTableColumn
cdeTConnConfigLocalAck=_CdeTConnConfigLocalAck_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,2),_CdeTConnConfigLocalAck_Type())
cdeTConnConfigLocalAck.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigLocalAck.setStatus(_A)
class _CdeTConnConfigCost_Type(Cost):defaultValue=3
_CdeTConnConfigCost_Type.__name__=_H
_CdeTConnConfigCost_Object=MibTableColumn
cdeTConnConfigCost=_CdeTConnConfigCost_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,3),_CdeTConnConfigCost_Type())
cdeTConnConfigCost.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigCost.setStatus(_A)
class _CdeTConnConfigLFSize_Type(LFSize):defaultValue=17749
_CdeTConnConfigLFSize_Type.__name__=_N
_CdeTConnConfigLFSize_Object=MibTableColumn
cdeTConnConfigLFSize=_CdeTConnConfigLFSize_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,4),_CdeTConnConfigLFSize_Type())
cdeTConnConfigLFSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigLFSize.setStatus(_A)
class _CdeTConnConfigKeepaliveInterval_Type(KeepaliveInterval):defaultValue=30
_CdeTConnConfigKeepaliveInterval_Type.__name__=_J
_CdeTConnConfigKeepaliveInterval_Object=MibTableColumn
cdeTConnConfigKeepaliveInterval=_CdeTConnConfigKeepaliveInterval_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,5),_CdeTConnConfigKeepaliveInterval_Type())
cdeTConnConfigKeepaliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigKeepaliveInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeTConnConfigKeepaliveInterval.setUnits(_O)
class _CdeTConnConfigBackup_Type(TruthValue):defaultValue=2
_CdeTConnConfigBackup_Type.__name__=_F
_CdeTConnConfigBackup_Object=MibTableColumn
cdeTConnConfigBackup=_CdeTConnConfigBackup_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,6),_CdeTConnConfigBackup_Type())
cdeTConnConfigBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigBackup.setStatus(_A)
class _CdeTConnConfigBackupTAddr_Type(TAddress):defaultHexValue=''
_CdeTConnConfigBackupTAddr_Type.__name__=_T
_CdeTConnConfigBackupTAddr_Object=MibTableColumn
cdeTConnConfigBackupTAddr=_CdeTConnConfigBackupTAddr_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,7),_CdeTConnConfigBackupTAddr_Type())
cdeTConnConfigBackupTAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigBackupTAddr.setStatus(_A)
class _CdeTConnConfigBackupLinger_Type(TruthValue):defaultValue=2
_CdeTConnConfigBackupLinger_Type.__name__=_F
_CdeTConnConfigBackupLinger_Object=MibTableColumn
cdeTConnConfigBackupLinger=_CdeTConnConfigBackupLinger_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,8),_CdeTConnConfigBackupLinger_Type())
cdeTConnConfigBackupLinger.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigBackupLinger.setStatus(_A)
class _CdeTConnConfigBackupLingerInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CdeTConnConfigBackupLingerInterval_Type.__name__=_G
_CdeTConnConfigBackupLingerInterval_Object=MibTableColumn
cdeTConnConfigBackupLingerInterval=_CdeTConnConfigBackupLingerInterval_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,9),_CdeTConnConfigBackupLingerInterval_Type())
cdeTConnConfigBackupLingerInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigBackupLingerInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeTConnConfigBackupLingerInterval.setUnits(_Q)
class _CdeTConnConfigPriority_Type(TruthValue):defaultValue=2
_CdeTConnConfigPriority_Type.__name__=_F
_CdeTConnConfigPriority_Object=MibTableColumn
cdeTConnConfigPriority=_CdeTConnConfigPriority_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,10),_CdeTConnConfigPriority_Type())
cdeTConnConfigPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigPriority.setStatus(_A)
class _CdeTConnConfigDestMac_Type(MacAddressNC):defaultHexValue=''
_CdeTConnConfigDestMac_Type.__name__=_S
_CdeTConnConfigDestMac_Object=MibTableColumn
cdeTConnConfigDestMac=_CdeTConnConfigDestMac_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,11),_CdeTConnConfigDestMac_Type())
cdeTConnConfigDestMac.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigDestMac.setStatus(_A)
class _CdeTConnConfigDynamic_Type(TruthValue):defaultValue=2
_CdeTConnConfigDynamic_Type.__name__=_F
_CdeTConnConfigDynamic_Object=MibTableColumn
cdeTConnConfigDynamic=_CdeTConnConfigDynamic_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,12),_CdeTConnConfigDynamic_Type())
cdeTConnConfigDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigDynamic.setStatus(_A)
class _CdeTConnConfigDynamicNoLlc_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CdeTConnConfigDynamicNoLlc_Type.__name__=_G
_CdeTConnConfigDynamicNoLlc_Object=MibTableColumn
cdeTConnConfigDynamicNoLlc=_CdeTConnConfigDynamicNoLlc_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,13),_CdeTConnConfigDynamicNoLlc_Type())
cdeTConnConfigDynamicNoLlc.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigDynamicNoLlc.setStatus(_A)
if mibBuilder.loadTexts:cdeTConnConfigDynamicNoLlc.setUnits(_Q)
class _CdeTConnConfigDynamicInactivityInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_CdeTConnConfigDynamicInactivityInterval_Type.__name__=_G
_CdeTConnConfigDynamicInactivityInterval_Object=MibTableColumn
cdeTConnConfigDynamicInactivityInterval=_CdeTConnConfigDynamicInactivityInterval_Object((1,3,6,1,4,1,9,9,74,1,3,1,1,14),_CdeTConnConfigDynamicInactivityInterval_Type())
cdeTConnConfigDynamicInactivityInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnConfigDynamicInactivityInterval.setStatus(_A)
if mibBuilder.loadTexts:cdeTConnConfigDynamicInactivityInterval.setUnits(_Q)
_CdeTConnOperTable_Object=MibTable
cdeTConnOperTable=_CdeTConnOperTable_Object((1,3,6,1,4,1,9,9,74,1,3,2))
if mibBuilder.loadTexts:cdeTConnOperTable.setStatus(_A)
_CdeTConnOperEntry_Object=MibTableRow
cdeTConnOperEntry=_CdeTConnOperEntry_Object((1,3,6,1,4,1,9,9,74,1,3,2,1))
if mibBuilder.loadTexts:cdeTConnOperEntry.setStatus(_A)
class _CdeTConnOperPartnerCost_Type(Cost):defaultValue=3
_CdeTConnOperPartnerCost_Type.__name__=_H
_CdeTConnOperPartnerCost_Object=MibTableColumn
cdeTConnOperPartnerCost=_CdeTConnOperPartnerCost_Object((1,3,6,1,4,1,9,9,74,1,3,2,1,1),_CdeTConnOperPartnerCost_Type())
cdeTConnOperPartnerCost.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeTConnOperPartnerCost.setStatus(_A)
_CdeTConnOperPartnerPriority_Type=TruthValue
_CdeTConnOperPartnerPriority_Object=MibTableColumn
cdeTConnOperPartnerPriority=_CdeTConnOperPartnerPriority_Object((1,3,6,1,4,1,9,9,74,1,3,2,1,2),_CdeTConnOperPartnerPriority_Type())
cdeTConnOperPartnerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeTConnOperPartnerPriority.setStatus(_A)
_CdeTConnOperPartnerBorderPeer_Type=TruthValue
_CdeTConnOperPartnerBorderPeer_Object=MibTableColumn
cdeTConnOperPartnerBorderPeer=_CdeTConnOperPartnerBorderPeer_Object((1,3,6,1,4,1,9,9,74,1,3,2,1,3),_CdeTConnOperPartnerBorderPeer_Type())
cdeTConnOperPartnerBorderPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeTConnOperPartnerBorderPeer.setStatus(_A)
class _CdeTConnOperPartnerGroupNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CdeTConnOperPartnerGroupNum_Type.__name__=_G
_CdeTConnOperPartnerGroupNum_Object=MibTableColumn
cdeTConnOperPartnerGroupNum=_CdeTConnOperPartnerGroupNum_Object((1,3,6,1,4,1,9,9,74,1,3,2,1,4),_CdeTConnOperPartnerGroupNum_Type())
cdeTConnOperPartnerGroupNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeTConnOperPartnerGroupNum.setStatus(_A)
_CdeTConnOperTDomainType_Type=TDomainType
_CdeTConnOperTDomainType_Object=MibTableColumn
cdeTConnOperTDomainType=_CdeTConnOperTDomainType_Object((1,3,6,1,4,1,9,9,74,1,3,2,1,5),_CdeTConnOperTDomainType_Type())
cdeTConnOperTDomainType.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeTConnOperTDomainType.setStatus(_A)
_CdeTConnSpecific_ObjectIdentity=ObjectIdentity
cdeTConnSpecific=_CdeTConnSpecific_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,3,3))
_CdeTConnTcp_ObjectIdentity=ObjectIdentity
cdeTConnTcp=_CdeTConnTcp_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,3,3,1))
_CdeTConnTcpConfigTable_Object=MibTable
cdeTConnTcpConfigTable=_CdeTConnTcpConfigTable_Object((1,3,6,1,4,1,9,9,74,1,3,3,1,1))
if mibBuilder.loadTexts:cdeTConnTcpConfigTable.setStatus(_A)
_CdeTConnTcpConfigEntry_Object=MibTableRow
cdeTConnTcpConfigEntry=_CdeTConnTcpConfigEntry_Object((1,3,6,1,4,1,9,9,74,1,3,3,1,1,1))
if mibBuilder.loadTexts:cdeTConnTcpConfigEntry.setStatus(_A)
class _CdeTConnTcpConfigQueueMax_Type(TCPQueueMax):defaultValue=200
_CdeTConnTcpConfigQueueMax_Type.__name__=_P
_CdeTConnTcpConfigQueueMax_Object=MibTableColumn
cdeTConnTcpConfigQueueMax=_CdeTConnTcpConfigQueueMax_Object((1,3,6,1,4,1,9,9,74,1,3,3,1,1,1,1),_CdeTConnTcpConfigQueueMax_Type())
cdeTConnTcpConfigQueueMax.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnTcpConfigQueueMax.setStatus(_A)
if mibBuilder.loadTexts:cdeTConnTcpConfigQueueMax.setUnits(_K)
_CdeTConnDirect_ObjectIdentity=ObjectIdentity
cdeTConnDirect=_CdeTConnDirect_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,3,3,2))
_CdeTConnDirectConfigTable_Object=MibTable
cdeTConnDirectConfigTable=_CdeTConnDirectConfigTable_Object((1,3,6,1,4,1,9,9,74,1,3,3,2,1))
if mibBuilder.loadTexts:cdeTConnDirectConfigTable.setStatus(_A)
_CdeTConnDirectConfigEntry_Object=MibTableRow
cdeTConnDirectConfigEntry=_CdeTConnDirectConfigEntry_Object((1,3,6,1,4,1,9,9,74,1,3,3,2,1,1))
cdeTConnDirectConfigEntry.setIndexNames((0,_M,_W))
if mibBuilder.loadTexts:cdeTConnDirectConfigEntry.setStatus(_A)
_CdeTConnDirectConfigIfIndex_Type=InterfaceIndex
_CdeTConnDirectConfigIfIndex_Object=MibTableColumn
cdeTConnDirectConfigIfIndex=_CdeTConnDirectConfigIfIndex_Object((1,3,6,1,4,1,9,9,74,1,3,3,2,1,1,1),_CdeTConnDirectConfigIfIndex_Type())
cdeTConnDirectConfigIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnDirectConfigIfIndex.setStatus(_A)
class _CdeTConnDirectConfigMediaEncap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),('llc2',3)))
_CdeTConnDirectConfigMediaEncap_Type.__name__=_G
_CdeTConnDirectConfigMediaEncap_Object=MibTableColumn
cdeTConnDirectConfigMediaEncap=_CdeTConnDirectConfigMediaEncap_Object((1,3,6,1,4,1,9,9,74,1,3,3,2,1,1,2),_CdeTConnDirectConfigMediaEncap_Type())
cdeTConnDirectConfigMediaEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnDirectConfigMediaEncap.setStatus(_A)
class _CdeTConnDirectConfigFrameRelayDlci_Type(DlciNumber):defaultValue=0
_CdeTConnDirectConfigFrameRelayDlci_Type.__name__=_U
_CdeTConnDirectConfigFrameRelayDlci_Object=MibTableColumn
cdeTConnDirectConfigFrameRelayDlci=_CdeTConnDirectConfigFrameRelayDlci_Object((1,3,6,1,4,1,9,9,74,1,3,3,2,1,1,3),_CdeTConnDirectConfigFrameRelayDlci_Type())
cdeTConnDirectConfigFrameRelayDlci.setMaxAccess(_D)
if mibBuilder.loadTexts:cdeTConnDirectConfigFrameRelayDlci.setStatus(_A)
_CdeInterface_ObjectIdentity=ObjectIdentity
cdeInterface=_CdeInterface_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,4))
_CdeIfTable_Object=MibTable
cdeIfTable=_CdeIfTable_Object((1,3,6,1,4,1,9,9,74,1,4,1))
if mibBuilder.loadTexts:cdeIfTable.setStatus(_A)
_CdeIfEntry_Object=MibTableRow
cdeIfEntry=_CdeIfEntry_Object((1,3,6,1,4,1,9,9,74,1,4,1,1))
if mibBuilder.loadTexts:cdeIfEntry.setStatus(_A)
_CdeIfType_Type=DlcType
_CdeIfType_Object=MibTableColumn
cdeIfType=_CdeIfType_Object((1,3,6,1,4,1,9,9,74,1,4,1,1,1),_CdeIfType_Type())
cdeIfType.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeIfType.setStatus(_A)
_CdeCircuit_ObjectIdentity=ObjectIdentity
cdeCircuit=_CdeCircuit_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,5))
_CdeCircuitTable_Object=MibTable
cdeCircuitTable=_CdeCircuitTable_Object((1,3,6,1,4,1,9,9,74,1,5,1))
if mibBuilder.loadTexts:cdeCircuitTable.setStatus(_A)
_CdeCircuitEntry_Object=MibTableRow
cdeCircuitEntry=_CdeCircuitEntry_Object((1,3,6,1,4,1,9,9,74,1,5,1,1))
if mibBuilder.loadTexts:cdeCircuitEntry.setStatus(_A)
class _CdeCircuitS1Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CdeCircuitS1Name_Type.__name__=_I
_CdeCircuitS1Name_Object=MibTableColumn
cdeCircuitS1Name=_CdeCircuitS1Name_Object((1,3,6,1,4,1,9,9,74,1,5,1,1,1),_CdeCircuitS1Name_Type())
cdeCircuitS1Name.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeCircuitS1Name.setStatus(_A)
class _CdeCircuitS2Name_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CdeCircuitS2Name_Type.__name__=_I
_CdeCircuitS2Name_Object=MibTableColumn
cdeCircuitS2Name=_CdeCircuitS2Name_Object((1,3,6,1,4,1,9,9,74,1,5,1,1,2),_CdeCircuitS2Name_Type())
cdeCircuitS2Name.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeCircuitS2Name.setStatus(_A)
class _CdeCircuitS1IdBlock_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_CdeCircuitS1IdBlock_Type.__name__=_I
_CdeCircuitS1IdBlock_Object=MibTableColumn
cdeCircuitS1IdBlock=_CdeCircuitS1IdBlock_Object((1,3,6,1,4,1,9,9,74,1,5,1,1,3),_CdeCircuitS1IdBlock_Type())
cdeCircuitS1IdBlock.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeCircuitS1IdBlock.setStatus(_A)
class _CdeCircuitS1IdNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CdeCircuitS1IdNum_Type.__name__=_I
_CdeCircuitS1IdNum_Object=MibTableColumn
cdeCircuitS1IdNum=_CdeCircuitS1IdNum_Object((1,3,6,1,4,1,9,9,74,1,5,1,1,4),_CdeCircuitS1IdNum_Type())
cdeCircuitS1IdNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeCircuitS1IdNum.setStatus(_A)
_CdeFast_ObjectIdentity=ObjectIdentity
cdeFast=_CdeFast_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,6))
_CdeFastTable_Object=MibTable
cdeFastTable=_CdeFastTable_Object((1,3,6,1,4,1,9,9,74,1,6,1))
if mibBuilder.loadTexts:cdeFastTable.setStatus(_A)
_CdeFastEntry_Object=MibTableRow
cdeFastEntry=_CdeFastEntry_Object((1,3,6,1,4,1,9,9,74,1,6,1,1))
cdeFastEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:cdeFastEntry.setStatus(_A)
_CdeFastS1Mac_Type=MacAddressNC
_CdeFastS1Mac_Object=MibTableColumn
cdeFastS1Mac=_CdeFastS1Mac_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,1),_CdeFastS1Mac_Type())
cdeFastS1Mac.setMaxAccess(_R)
if mibBuilder.loadTexts:cdeFastS1Mac.setStatus(_A)
_CdeFastS1Sap_Type=SAPType
_CdeFastS1Sap_Object=MibTableColumn
cdeFastS1Sap=_CdeFastS1Sap_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,2),_CdeFastS1Sap_Type())
cdeFastS1Sap.setMaxAccess(_R)
if mibBuilder.loadTexts:cdeFastS1Sap.setStatus(_A)
_CdeFastS2Mac_Type=MacAddressNC
_CdeFastS2Mac_Object=MibTableColumn
cdeFastS2Mac=_CdeFastS2Mac_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,3),_CdeFastS2Mac_Type())
cdeFastS2Mac.setMaxAccess(_R)
if mibBuilder.loadTexts:cdeFastS2Mac.setStatus(_A)
_CdeFastS2Sap_Type=SAPType
_CdeFastS2Sap_Object=MibTableColumn
cdeFastS2Sap=_CdeFastS2Sap_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,4),_CdeFastS2Sap_Type())
cdeFastS2Sap.setMaxAccess(_R)
if mibBuilder.loadTexts:cdeFastS2Sap.setStatus(_A)
_CdeFastS1IfIndex_Type=InterfaceIndex
_CdeFastS1IfIndex_Object=MibTableColumn
cdeFastS1IfIndex=_CdeFastS1IfIndex_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,5),_CdeFastS1IfIndex_Type())
cdeFastS1IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS1IfIndex.setStatus(_A)
class _CdeFastS1RouteInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_CdeFastS1RouteInfo_Type.__name__=_L
_CdeFastS1RouteInfo_Object=MibTableColumn
cdeFastS1RouteInfo=_CdeFastS1RouteInfo_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,6),_CdeFastS1RouteInfo_Type())
cdeFastS1RouteInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS1RouteInfo.setStatus(_A)
class _CdeFastS1CacheId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CdeFastS1CacheId_Type.__name__=_L
_CdeFastS1CacheId_Object=MibTableColumn
cdeFastS1CacheId=_CdeFastS1CacheId_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,7),_CdeFastS1CacheId_Type())
cdeFastS1CacheId.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS1CacheId.setStatus(_A)
_CdeFastS2TDomain_Type=ObjectIdentifier
_CdeFastS2TDomain_Object=MibTableColumn
cdeFastS2TDomain=_CdeFastS2TDomain_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,8),_CdeFastS2TDomain_Type())
cdeFastS2TDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS2TDomain.setStatus(_A)
_CdeFastS2TAddress_Type=TAddress
_CdeFastS2TAddress_Object=MibTableColumn
cdeFastS2TAddress=_CdeFastS2TAddress_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,9),_CdeFastS2TAddress_Type())
cdeFastS2TAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS2TAddress.setStatus(_A)
class _CdeFastS2CacheId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CdeFastS2CacheId_Type.__name__=_L
_CdeFastS2CacheId_Object=MibTableColumn
cdeFastS2CacheId=_CdeFastS2CacheId_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,10),_CdeFastS2CacheId_Type())
cdeFastS2CacheId.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastS2CacheId.setStatus(_A)
class _CdeFastOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('s1',1),('s2',2)))
_CdeFastOrigin_Type.__name__=_G
_CdeFastOrigin_Object=MibTableColumn
cdeFastOrigin=_CdeFastOrigin_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,11),_CdeFastOrigin_Type())
cdeFastOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastOrigin.setStatus(_A)
_CdeFastTimeToLive_Type=TimeTicks
_CdeFastTimeToLive_Object=MibTableColumn
cdeFastTimeToLive=_CdeFastTimeToLive_Object((1,3,6,1,4,1,9,9,74,1,6,1,1,12),_CdeFastTimeToLive_Type())
cdeFastTimeToLive.setMaxAccess(_E)
if mibBuilder.loadTexts:cdeFastTimeToLive.setStatus(_A)
if mibBuilder.loadTexts:cdeFastTimeToLive.setUnits('hundredths of a second')
_CdeTrapControl_ObjectIdentity=ObjectIdentity
cdeTrapControl=_CdeTrapControl_ObjectIdentity((1,3,6,1,4,1,9,9,74,1,7))
class _CdeTrapCntlTConn_Type(TruthValue):defaultValue=2
_CdeTrapCntlTConn_Type.__name__=_F
_CdeTrapCntlTConn_Object=MibScalar
cdeTrapCntlTConn=_CdeTrapCntlTConn_Object((1,3,6,1,4,1,9,9,74,1,7,1),_CdeTrapCntlTConn_Type())
cdeTrapCntlTConn.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeTrapCntlTConn.setStatus(_A)
class _CdeTrapCntlCircuit_Type(TruthValue):defaultValue=2
_CdeTrapCntlCircuit_Type.__name__=_F
_CdeTrapCntlCircuit_Object=MibScalar
cdeTrapCntlCircuit=_CdeTrapCntlCircuit_Object((1,3,6,1,4,1,9,9,74,1,7,2),_CdeTrapCntlCircuit_Type())
cdeTrapCntlCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:cdeTrapCntlCircuit.setStatus(_A)
_CdeTrapsPrefix_ObjectIdentity=ObjectIdentity
cdeTrapsPrefix=_CdeTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,74,2))
_CdeTraps_ObjectIdentity=ObjectIdentity
cdeTraps=_CdeTraps_ObjectIdentity((1,3,6,1,4,1,9,9,74,2,0))
_CdeMIBConformance_ObjectIdentity=ObjectIdentity
cdeMIBConformance=_CdeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,74,3))
_CdeMIBCompliances_ObjectIdentity=ObjectIdentity
cdeMIBCompliances=_CdeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,74,3,1))
_CdeMIBGroups_ObjectIdentity=ObjectIdentity
cdeMIBGroups=_CdeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,74,3,2))
dlswTConnConfigEntry.registerAugmentions((_B,_f))
cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions((_B,_g))
cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions((_B,_h))
cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
dlswIfEntry.registerAugmentions((_B,_i))
cdeIfEntry.setIndexNames(*dlswIfEntry.getIndexNames())
dlswCircuitEntry.registerAugmentions((_B,_j))
cdeCircuitEntry.setIndexNames(*dlswCircuitEntry.getIndexNames())
cdeMIBNodeGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,1))
cdeMIBNodeGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:cdeMIBNodeGroup.setStatus(_A)
cdeMIBTConnConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,2))
cdeMIBTConnConfigGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cdeMIBTConnConfigGroup.setStatus(_A)
cdeMIBTConnOperGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,3))
cdeMIBTConnOperGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:cdeMIBTConnOperGroup.setStatus(_A)
cdeMIBTConnTcpConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,4))
cdeMIBTConnTcpConfigGroup.setObjects((_B,_AP))
if mibBuilder.loadTexts:cdeMIBTConnTcpConfigGroup.setStatus(_A)
cdeMIBTConnDirectConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,5))
cdeMIBTConnDirectConfigGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:cdeMIBTConnDirectConfigGroup.setStatus(_A)
cdeMIBInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,6))
cdeMIBInterfaceGroup.setObjects((_B,_AT))
if mibBuilder.loadTexts:cdeMIBInterfaceGroup.setStatus(_A)
cdeMIBCircuitGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,7))
cdeMIBCircuitGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:cdeMIBCircuitGroup.setStatus(_A)
cdeMIBFastGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,8))
cdeMIBFastGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:cdeMIBFastGroup.setStatus(_A)
cdeTrapControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,74,3,2,9))
cdeTrapControlGroup.setObjects(*((_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:cdeTrapControlGroup.setStatus(_A)
cdeTrapTConnUpDown=NotificationType((1,3,6,1,4,1,9,9,74,2,0,1))
cdeTrapTConnUpDown.setObjects((_M,_X))
if mibBuilder.loadTexts:cdeTrapTConnUpDown.setStatus(_A)
cdeTrapCircuitUpDown=NotificationType((1,3,6,1,4,1,9,9,74,2,0,2))
cdeTrapCircuitUpDown.setObjects((_M,_V))
if mibBuilder.loadTexts:cdeTrapCircuitUpDown.setStatus(_A)
cdeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,74,3,1,1))
cdeMIBCompliance.setObjects(*((_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:cdeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_a:TDomainType,_H:Cost,_J:KeepaliveInterval,_P:TCPQueueMax,'ciscoDlswExtMIB':ciscoDlswExtMIB,'ciscoDlswExtMIBObjects':ciscoDlswExtMIBObjects,'cdeDomains':cdeDomains,'cdeFSTDomain':cdeFSTDomain,'cdeDirectHdlcDomain':cdeDirectHdlcDomain,'cdeDirectFrameRelayDomain':cdeDirectFrameRelayDomain,'cdeLlc2Domain':cdeLlc2Domain,'cdeNode':cdeNode,_k:cdeNodeTAddr,_l:cdeNodeGroup,_m:cdeNodeBorder,_n:cdeNodeCost,_o:cdeNodeKeepaliveInterval,_p:cdeNodePassiveConnect,_q:cdeNodeBiuSegment,_r:cdeNodeInitPacingWindow,_s:cdeNodeMaxPacingWindow,_t:cdeNodePromiscuous,_u:cdeNodePromPeerDefaultsCost,_v:cdeNodePromPeerDefaultsDestMac,_w:cdeNodePromPeerDefaultsKeepaliveInterval,_x:cdeNodePromPeerDefaultsLFSize,_y:cdeNodePromPeerDefaultsTCPQueueMax,_z:cdeNodePeerOnDemandDefaultsCost,_A0:cdeNodePeerOnDemandDefaultsFst,_A1:cdeNodePeerOnDemandDefaultsInactivityInterval,_A2:cdeNodePeerOnDemandDefaultsKeepaliveInterval,_A3:cdeNodePeerOnDemandDefaultsLFSize,_A4:cdeNodePeerOnDemandDefaultsPriority,_A5:cdeNodePeerOnDemandDefaultsTCPQueueMax,'cdeTConn':cdeTConn,'cdeTConnConfigTable':cdeTConnConfigTable,_f:cdeTConnConfigEntry,_A6:cdeTConnConfigTDomainType,_A7:cdeTConnConfigLocalAck,_A8:cdeTConnConfigCost,_A9:cdeTConnConfigLFSize,_AA:cdeTConnConfigKeepaliveInterval,_AB:cdeTConnConfigBackup,_AC:cdeTConnConfigBackupTAddr,_AD:cdeTConnConfigBackupLinger,_AE:cdeTConnConfigBackupLingerInterval,_AF:cdeTConnConfigPriority,_AG:cdeTConnConfigDestMac,_AH:cdeTConnConfigDynamic,_AI:cdeTConnConfigDynamicNoLlc,_AJ:cdeTConnConfigDynamicInactivityInterval,'cdeTConnOperTable':cdeTConnOperTable,_g:cdeTConnOperEntry,_AK:cdeTConnOperPartnerCost,_AL:cdeTConnOperPartnerPriority,_AM:cdeTConnOperPartnerBorderPeer,_AN:cdeTConnOperPartnerGroupNum,_AO:cdeTConnOperTDomainType,'cdeTConnSpecific':cdeTConnSpecific,'cdeTConnTcp':cdeTConnTcp,'cdeTConnTcpConfigTable':cdeTConnTcpConfigTable,_h:cdeTConnTcpConfigEntry,_AP:cdeTConnTcpConfigQueueMax,'cdeTConnDirect':cdeTConnDirect,'cdeTConnDirectConfigTable':cdeTConnDirectConfigTable,'cdeTConnDirectConfigEntry':cdeTConnDirectConfigEntry,_AQ:cdeTConnDirectConfigIfIndex,_AR:cdeTConnDirectConfigMediaEncap,_AS:cdeTConnDirectConfigFrameRelayDlci,'cdeInterface':cdeInterface,'cdeIfTable':cdeIfTable,_i:cdeIfEntry,_AT:cdeIfType,'cdeCircuit':cdeCircuit,'cdeCircuitTable':cdeCircuitTable,_j:cdeCircuitEntry,_AU:cdeCircuitS1Name,_AV:cdeCircuitS2Name,_AW:cdeCircuitS1IdBlock,_AX:cdeCircuitS1IdNum,'cdeFast':cdeFast,'cdeFastTable':cdeFastTable,'cdeFastEntry':cdeFastEntry,_b:cdeFastS1Mac,_c:cdeFastS1Sap,_d:cdeFastS2Mac,_e:cdeFastS2Sap,_AY:cdeFastS1IfIndex,_AZ:cdeFastS1RouteInfo,_Aa:cdeFastS1CacheId,_Ab:cdeFastS2TDomain,_Ac:cdeFastS2TAddress,_Ad:cdeFastS2CacheId,_Ae:cdeFastOrigin,_Af:cdeFastTimeToLive,'cdeTrapControl':cdeTrapControl,_Ag:cdeTrapCntlTConn,_Ah:cdeTrapCntlCircuit,'cdeTrapsPrefix':cdeTrapsPrefix,'cdeTraps':cdeTraps,'cdeTrapTConnUpDown':cdeTrapTConnUpDown,'cdeTrapCircuitUpDown':cdeTrapCircuitUpDown,'cdeMIBConformance':cdeMIBConformance,'cdeMIBCompliances':cdeMIBCompliances,'cdeMIBCompliance':cdeMIBCompliance,'cdeMIBGroups':cdeMIBGroups,_Ai:cdeMIBNodeGroup,_Aj:cdeMIBTConnConfigGroup,_Ak:cdeMIBTConnOperGroup,_Al:cdeMIBTConnTcpConfigGroup,_Am:cdeMIBTConnDirectConfigGroup,_An:cdeMIBInterfaceGroup,_Ao:cdeMIBCircuitGroup,_Ap:cdeMIBFastGroup,_Aq:cdeTrapControlGroup})