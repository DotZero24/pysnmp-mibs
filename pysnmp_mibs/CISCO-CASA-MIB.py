_AC='ciscoCasaNotifGroup'
_AB='ciscoCasaStatsGroup'
_AA='ciscoCasaAffinityCacheGroup'
_A9='ciscoCasaAdminGroup'
_A8='ciscoCasaGroup'
_A7='ciscoCasaStateChange'
_A6='cCasaAddressMask'
_A5='cCasaCfgAddressMask'
_A4='cCasaInterestTickles'
_A3='cCasaInterestPackets'
_A2='cCasaAffinityCacheDispProtocol'
_A1='cCasaAffinityCacheDispSourcePort'
_A0='cCasaAffinityCacheDispSourceAddr'
_z='cCasaAffinityCacheDispDestPort'
_y='cCasaAffinityCacheDispDestAddr'
_x='cCasaAffinityCacheDestDispAddr'
_w='cCasaAffinityCacheDestProtocol'
_v='cCasaAffinityCacheDestSourcePort'
_u='cCasaAffinityCacheDestSourceAddr'
_t='cCasaAffinityCacheDestDestPort'
_s='cCasaAffinityCacheSrcDispAddr'
_r='cCasaAffinityCacheSrcProtocol'
_q='cCasaAffinityCacheSrcDestPort'
_p='cCasaAffinityCacheSrcDestAddr'
_o='cCasaAffinityCacheSrcSourcePort'
_n='cCasaAffinityCacheIntrTimeouts'
_m='cCasaAffinityCacheHCMisses'
_l='cCasaAffinityCacheMisses'
_k='cCasaAffinityCacheHCHits'
_j='cCasaAffinityCacheHits'
_i='cCasaAffinityCacheNoStorageDrops'
_h='cCasaAffinityCacheHiWtrMrkReset'
_g='cCasaAffinityCacheHiWtrMrk'
_f='cCasaAffinityCacheNumOf'
_e='cCasaAdminRowStatus'
_d='cCasaAdminMcastPasswdFailures'
_c='cCasaAdminMcastPasswdTimeout'
_b='cCasaAdminMcastPasswd'
_a='cCasaMcastAddress'
_Z='cCasaAddress'
_Y='cCasaCfgMcastAddress'
_X='cCasaCfgAddress'
_W='cCasaStateNotificationEnabled'
_V='cCasaAffinityCacheDispatchIndex'
_U='cCasaAffinityCacheDispDispAddr'
_T='cCasaAffinityCacheDestIndex'
_S='cCasaAffinityCacheDestDestAddr'
_R='cCasaAffinityCacheSrcIndex'
_Q='cCasaAffinityCacheSrcSourceAddr'
_P='cCasaAdminMcastPort'
_O='TruthValue'
_N='DisplayString'
_M='Unsigned32'
_L='cCasaState'
_K='read-create'
_J='obsolete'
_I='Integer32'
_H='affinities'
_G='packets'
_F='read-write'
_E='not-accessible'
_D='cCasaEntity'
_C='read-only'
_B='CISCO-CASA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoIpProtocol,CiscoPort=mibBuilder.importSymbols('CISCO-TC','CiscoIpProtocol','CiscoPort')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_O)
ciscoCasaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,122))
if mibBuilder.loadTexts:ciscoCasaMIB.setRevisions(('2002-09-18 00:00',))
class CasaFixedAffinityIndex(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CiscoCasaMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCasaMIBObjects=_CiscoCasaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,122,1))
_CCasaGlobal_ObjectIdentity=ObjectIdentity
cCasaGlobal=_CCasaGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,122,1,1))
_CCasaTable_Object=MibTable
cCasaTable=_CCasaTable_Object((1,3,6,1,4,1,9,9,122,1,1,1))
if mibBuilder.loadTexts:cCasaTable.setStatus(_A)
_CCasaEntry_Object=MibTableRow
cCasaEntry=_CCasaEntry_Object((1,3,6,1,4,1,9,9,122,1,1,1,1))
cCasaEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cCasaEntry.setStatus(_A)
class _CCasaEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('casaForwardingAgent',1),('casaGLoBalManager',2),('casaUnknownManager',3)))
_CCasaEntity_Type.__name__=_I
_CCasaEntity_Object=MibTableColumn
cCasaEntity=_CCasaEntity_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,1),_CCasaEntity_Type())
cCasaEntity.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaEntity.setStatus(_A)
class _CCasaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('casaNotEnabled',1),('casaEnabled',2),('casaActive',3)))
_CCasaState_Type.__name__=_I
_CCasaState_Object=MibTableColumn
cCasaState=_CCasaState_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,2),_CCasaState_Type())
cCasaState.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaState.setStatus(_A)
class _CCasaStateNotificationEnabled_Type(TruthValue):defaultValue=2
_CCasaStateNotificationEnabled_Type.__name__=_O
_CCasaStateNotificationEnabled_Object=MibTableColumn
cCasaStateNotificationEnabled=_CCasaStateNotificationEnabled_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,3),_CCasaStateNotificationEnabled_Type())
cCasaStateNotificationEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaStateNotificationEnabled.setStatus(_A)
_CCasaCfgAddress_Type=IpAddress
_CCasaCfgAddress_Object=MibTableColumn
cCasaCfgAddress=_CCasaCfgAddress_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,4),_CCasaCfgAddress_Type())
cCasaCfgAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaCfgAddress.setStatus(_A)
_CCasaCfgAddressMask_Type=IpAddress
_CCasaCfgAddressMask_Object=MibTableColumn
cCasaCfgAddressMask=_CCasaCfgAddressMask_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,5),_CCasaCfgAddressMask_Type())
cCasaCfgAddressMask.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaCfgAddressMask.setStatus(_J)
_CCasaCfgMcastAddress_Type=IpAddress
_CCasaCfgMcastAddress_Object=MibTableColumn
cCasaCfgMcastAddress=_CCasaCfgMcastAddress_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,6),_CCasaCfgMcastAddress_Type())
cCasaCfgMcastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaCfgMcastAddress.setStatus(_A)
_CCasaAddress_Type=IpAddress
_CCasaAddress_Object=MibTableColumn
cCasaAddress=_CCasaAddress_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,7),_CCasaAddress_Type())
cCasaAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAddress.setStatus(_A)
_CCasaAddressMask_Type=IpAddress
_CCasaAddressMask_Object=MibTableColumn
cCasaAddressMask=_CCasaAddressMask_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,8),_CCasaAddressMask_Type())
cCasaAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAddressMask.setStatus(_J)
_CCasaMcastAddress_Type=IpAddress
_CCasaMcastAddress_Object=MibTableColumn
cCasaMcastAddress=_CCasaMcastAddress_Object((1,3,6,1,4,1,9,9,122,1,1,1,1,9),_CCasaMcastAddress_Type())
cCasaMcastAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaMcastAddress.setStatus(_A)
_CCasaStats_ObjectIdentity=ObjectIdentity
cCasaStats=_CCasaStats_ObjectIdentity((1,3,6,1,4,1,9,9,122,1,2))
_CCasaAffinityCacheStatsTable_Object=MibTable
cCasaAffinityCacheStatsTable=_CCasaAffinityCacheStatsTable_Object((1,3,6,1,4,1,9,9,122,1,2,1))
if mibBuilder.loadTexts:cCasaAffinityCacheStatsTable.setStatus(_A)
_CCasaAffinityCacheStatsEntry_Object=MibTableRow
cCasaAffinityCacheStatsEntry=_CCasaAffinityCacheStatsEntry_Object((1,3,6,1,4,1,9,9,122,1,2,1,1))
cCasaAffinityCacheStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cCasaAffinityCacheStatsEntry.setStatus(_A)
_CCasaAffinityCacheNumOf_Type=Gauge32
_CCasaAffinityCacheNumOf_Object=MibTableColumn
cCasaAffinityCacheNumOf=_CCasaAffinityCacheNumOf_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,1),_CCasaAffinityCacheNumOf_Type())
cCasaAffinityCacheNumOf.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheNumOf.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheNumOf.setUnits(_H)
_CCasaAffinityCacheHiWtrMrk_Type=Unsigned32
_CCasaAffinityCacheHiWtrMrk_Object=MibTableColumn
cCasaAffinityCacheHiWtrMrk=_CCasaAffinityCacheHiWtrMrk_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,2),_CCasaAffinityCacheHiWtrMrk_Type())
cCasaAffinityCacheHiWtrMrk.setMaxAccess(_F)
if mibBuilder.loadTexts:cCasaAffinityCacheHiWtrMrk.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheHiWtrMrk.setUnits(_H)
_CCasaAffinityCacheHiWtrMrkReset_Type=TimeStamp
_CCasaAffinityCacheHiWtrMrkReset_Object=MibTableColumn
cCasaAffinityCacheHiWtrMrkReset=_CCasaAffinityCacheHiWtrMrkReset_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,3),_CCasaAffinityCacheHiWtrMrkReset_Type())
cCasaAffinityCacheHiWtrMrkReset.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheHiWtrMrkReset.setStatus(_A)
_CCasaAffinityCacheNoStorageDrops_Type=Counter32
_CCasaAffinityCacheNoStorageDrops_Object=MibTableColumn
cCasaAffinityCacheNoStorageDrops=_CCasaAffinityCacheNoStorageDrops_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,4),_CCasaAffinityCacheNoStorageDrops_Type())
cCasaAffinityCacheNoStorageDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheNoStorageDrops.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheNoStorageDrops.setUnits(_H)
_CCasaAffinityCacheHits_Type=Counter32
_CCasaAffinityCacheHits_Object=MibTableColumn
cCasaAffinityCacheHits=_CCasaAffinityCacheHits_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,5),_CCasaAffinityCacheHits_Type())
cCasaAffinityCacheHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheHits.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheHits.setUnits(_G)
_CCasaAffinityCacheHCHits_Type=Counter64
_CCasaAffinityCacheHCHits_Object=MibTableColumn
cCasaAffinityCacheHCHits=_CCasaAffinityCacheHCHits_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,6),_CCasaAffinityCacheHCHits_Type())
cCasaAffinityCacheHCHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheHCHits.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheHCHits.setUnits(_G)
_CCasaAffinityCacheMisses_Type=Counter32
_CCasaAffinityCacheMisses_Object=MibTableColumn
cCasaAffinityCacheMisses=_CCasaAffinityCacheMisses_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,7),_CCasaAffinityCacheMisses_Type())
cCasaAffinityCacheMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheMisses.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheMisses.setUnits(_G)
_CCasaAffinityCacheHCMisses_Type=Counter64
_CCasaAffinityCacheHCMisses_Object=MibTableColumn
cCasaAffinityCacheHCMisses=_CCasaAffinityCacheHCMisses_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,8),_CCasaAffinityCacheHCMisses_Type())
cCasaAffinityCacheHCMisses.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheHCMisses.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheHCMisses.setUnits(_G)
_CCasaAffinityCacheIntrTimeouts_Type=Counter32
_CCasaAffinityCacheIntrTimeouts_Object=MibTableColumn
cCasaAffinityCacheIntrTimeouts=_CCasaAffinityCacheIntrTimeouts_Object((1,3,6,1,4,1,9,9,122,1,2,1,1,9),_CCasaAffinityCacheIntrTimeouts_Type())
cCasaAffinityCacheIntrTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheIntrTimeouts.setStatus(_A)
if mibBuilder.loadTexts:cCasaAffinityCacheIntrTimeouts.setUnits(_H)
_CCasaStatsTable_Object=MibTable
cCasaStatsTable=_CCasaStatsTable_Object((1,3,6,1,4,1,9,9,122,1,2,2))
if mibBuilder.loadTexts:cCasaStatsTable.setStatus(_A)
_CCasaStatsEntry_Object=MibTableRow
cCasaStatsEntry=_CCasaStatsEntry_Object((1,3,6,1,4,1,9,9,122,1,2,2,1))
cCasaStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cCasaStatsEntry.setStatus(_A)
_CCasaInterestPackets_Type=Counter32
_CCasaInterestPackets_Object=MibTableColumn
cCasaInterestPackets=_CCasaInterestPackets_Object((1,3,6,1,4,1,9,9,122,1,2,2,1,1),_CCasaInterestPackets_Type())
cCasaInterestPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaInterestPackets.setStatus(_A)
if mibBuilder.loadTexts:cCasaInterestPackets.setUnits(_G)
_CCasaInterestTickles_Type=Counter32
_CCasaInterestTickles_Object=MibTableColumn
cCasaInterestTickles=_CCasaInterestTickles_Object((1,3,6,1,4,1,9,9,122,1,2,2,1,2),_CCasaInterestTickles_Type())
cCasaInterestTickles.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaInterestTickles.setStatus(_A)
if mibBuilder.loadTexts:cCasaInterestTickles.setUnits(_G)
_CCasaAdmin_ObjectIdentity=ObjectIdentity
cCasaAdmin=_CCasaAdmin_ObjectIdentity((1,3,6,1,4,1,9,9,122,1,3))
_CCasaAdminTable_Object=MibTable
cCasaAdminTable=_CCasaAdminTable_Object((1,3,6,1,4,1,9,9,122,1,3,1))
if mibBuilder.loadTexts:cCasaAdminTable.setStatus(_A)
_CCasaAdminEntry_Object=MibTableRow
cCasaAdminEntry=_CCasaAdminEntry_Object((1,3,6,1,4,1,9,9,122,1,3,1,1))
cCasaAdminEntry.setIndexNames((0,_B,_D),(0,_B,_P))
if mibBuilder.loadTexts:cCasaAdminEntry.setStatus(_A)
_CCasaAdminMcastPort_Type=CiscoPort
_CCasaAdminMcastPort_Object=MibTableColumn
cCasaAdminMcastPort=_CCasaAdminMcastPort_Object((1,3,6,1,4,1,9,9,122,1,3,1,1,1),_CCasaAdminMcastPort_Type())
cCasaAdminMcastPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAdminMcastPort.setStatus(_A)
class _CCasaAdminMcastPasswd_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CCasaAdminMcastPasswd_Type.__name__=_N
_CCasaAdminMcastPasswd_Object=MibTableColumn
cCasaAdminMcastPasswd=_CCasaAdminMcastPasswd_Object((1,3,6,1,4,1,9,9,122,1,3,1,1,2),_CCasaAdminMcastPasswd_Type())
cCasaAdminMcastPasswd.setMaxAccess(_K)
if mibBuilder.loadTexts:cCasaAdminMcastPasswd.setStatus(_A)
class _CCasaAdminMcastPasswdTimeout_Type(Unsigned32):defaultValue=12;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CCasaAdminMcastPasswdTimeout_Type.__name__=_M
_CCasaAdminMcastPasswdTimeout_Object=MibTableColumn
cCasaAdminMcastPasswdTimeout=_CCasaAdminMcastPasswdTimeout_Object((1,3,6,1,4,1,9,9,122,1,3,1,1,3),_CCasaAdminMcastPasswdTimeout_Type())
cCasaAdminMcastPasswdTimeout.setMaxAccess(_K)
if mibBuilder.loadTexts:cCasaAdminMcastPasswdTimeout.setStatus(_A)
if mibBuilder.loadTexts:cCasaAdminMcastPasswdTimeout.setUnits('seconds')
_CCasaAdminMcastPasswdFailures_Type=Counter32
_CCasaAdminMcastPasswdFailures_Object=MibTableColumn
cCasaAdminMcastPasswdFailures=_CCasaAdminMcastPasswdFailures_Object((1,3,6,1,4,1,9,9,122,1,3,1,1,4),_CCasaAdminMcastPasswdFailures_Type())
cCasaAdminMcastPasswdFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAdminMcastPasswdFailures.setStatus(_A)
if mibBuilder.loadTexts:cCasaAdminMcastPasswdFailures.setUnits('failures')
_CCasaAdminRowStatus_Type=RowStatus
_CCasaAdminRowStatus_Object=MibTableColumn
cCasaAdminRowStatus=_CCasaAdminRowStatus_Object((1,3,6,1,4,1,9,9,122,1,3,1,1,5),_CCasaAdminRowStatus_Type())
cCasaAdminRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cCasaAdminRowStatus.setStatus(_A)
_CCasaAffinityCache_ObjectIdentity=ObjectIdentity
cCasaAffinityCache=_CCasaAffinityCache_ObjectIdentity((1,3,6,1,4,1,9,9,122,1,4))
_CCasaAffinityCacheSrcTable_Object=MibTable
cCasaAffinityCacheSrcTable=_CCasaAffinityCacheSrcTable_Object((1,3,6,1,4,1,9,9,122,1,4,1))
if mibBuilder.loadTexts:cCasaAffinityCacheSrcTable.setStatus(_A)
_CCasaAffinityCacheSrcEntry_Object=MibTableRow
cCasaAffinityCacheSrcEntry=_CCasaAffinityCacheSrcEntry_Object((1,3,6,1,4,1,9,9,122,1,4,1,1))
cCasaAffinityCacheSrcEntry.setIndexNames((0,_B,_D),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:cCasaAffinityCacheSrcEntry.setStatus(_A)
_CCasaAffinityCacheSrcSourceAddr_Type=IpAddress
_CCasaAffinityCacheSrcSourceAddr_Object=MibTableColumn
cCasaAffinityCacheSrcSourceAddr=_CCasaAffinityCacheSrcSourceAddr_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,1),_CCasaAffinityCacheSrcSourceAddr_Type())
cCasaAffinityCacheSrcSourceAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcSourceAddr.setStatus(_A)
_CCasaAffinityCacheSrcIndex_Type=CasaFixedAffinityIndex
_CCasaAffinityCacheSrcIndex_Object=MibTableColumn
cCasaAffinityCacheSrcIndex=_CCasaAffinityCacheSrcIndex_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,2),_CCasaAffinityCacheSrcIndex_Type())
cCasaAffinityCacheSrcIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcIndex.setStatus(_A)
_CCasaAffinityCacheSrcSourcePort_Type=CiscoPort
_CCasaAffinityCacheSrcSourcePort_Object=MibTableColumn
cCasaAffinityCacheSrcSourcePort=_CCasaAffinityCacheSrcSourcePort_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,3),_CCasaAffinityCacheSrcSourcePort_Type())
cCasaAffinityCacheSrcSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcSourcePort.setStatus(_A)
_CCasaAffinityCacheSrcDestAddr_Type=IpAddress
_CCasaAffinityCacheSrcDestAddr_Object=MibTableColumn
cCasaAffinityCacheSrcDestAddr=_CCasaAffinityCacheSrcDestAddr_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,4),_CCasaAffinityCacheSrcDestAddr_Type())
cCasaAffinityCacheSrcDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcDestAddr.setStatus(_A)
_CCasaAffinityCacheSrcDestPort_Type=CiscoPort
_CCasaAffinityCacheSrcDestPort_Object=MibTableColumn
cCasaAffinityCacheSrcDestPort=_CCasaAffinityCacheSrcDestPort_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,5),_CCasaAffinityCacheSrcDestPort_Type())
cCasaAffinityCacheSrcDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcDestPort.setStatus(_A)
_CCasaAffinityCacheSrcProtocol_Type=CiscoIpProtocol
_CCasaAffinityCacheSrcProtocol_Object=MibTableColumn
cCasaAffinityCacheSrcProtocol=_CCasaAffinityCacheSrcProtocol_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,6),_CCasaAffinityCacheSrcProtocol_Type())
cCasaAffinityCacheSrcProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcProtocol.setStatus(_A)
_CCasaAffinityCacheSrcDispAddr_Type=IpAddress
_CCasaAffinityCacheSrcDispAddr_Object=MibTableColumn
cCasaAffinityCacheSrcDispAddr=_CCasaAffinityCacheSrcDispAddr_Object((1,3,6,1,4,1,9,9,122,1,4,1,1,7),_CCasaAffinityCacheSrcDispAddr_Type())
cCasaAffinityCacheSrcDispAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheSrcDispAddr.setStatus(_A)
_CCasaAffinityCacheDestTable_Object=MibTable
cCasaAffinityCacheDestTable=_CCasaAffinityCacheDestTable_Object((1,3,6,1,4,1,9,9,122,1,4,2))
if mibBuilder.loadTexts:cCasaAffinityCacheDestTable.setStatus(_A)
_CCasaAffinityCacheDestEntry_Object=MibTableRow
cCasaAffinityCacheDestEntry=_CCasaAffinityCacheDestEntry_Object((1,3,6,1,4,1,9,9,122,1,4,2,1))
cCasaAffinityCacheDestEntry.setIndexNames((0,_B,_D),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cCasaAffinityCacheDestEntry.setStatus(_A)
_CCasaAffinityCacheDestDestAddr_Type=IpAddress
_CCasaAffinityCacheDestDestAddr_Object=MibTableColumn
cCasaAffinityCacheDestDestAddr=_CCasaAffinityCacheDestDestAddr_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,1),_CCasaAffinityCacheDestDestAddr_Type())
cCasaAffinityCacheDestDestAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheDestDestAddr.setStatus(_A)
_CCasaAffinityCacheDestIndex_Type=CasaFixedAffinityIndex
_CCasaAffinityCacheDestIndex_Object=MibTableColumn
cCasaAffinityCacheDestIndex=_CCasaAffinityCacheDestIndex_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,2),_CCasaAffinityCacheDestIndex_Type())
cCasaAffinityCacheDestIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheDestIndex.setStatus(_A)
_CCasaAffinityCacheDestDestPort_Type=CiscoPort
_CCasaAffinityCacheDestDestPort_Object=MibTableColumn
cCasaAffinityCacheDestDestPort=_CCasaAffinityCacheDestDestPort_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,3),_CCasaAffinityCacheDestDestPort_Type())
cCasaAffinityCacheDestDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDestDestPort.setStatus(_A)
_CCasaAffinityCacheDestSourceAddr_Type=IpAddress
_CCasaAffinityCacheDestSourceAddr_Object=MibTableColumn
cCasaAffinityCacheDestSourceAddr=_CCasaAffinityCacheDestSourceAddr_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,4),_CCasaAffinityCacheDestSourceAddr_Type())
cCasaAffinityCacheDestSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDestSourceAddr.setStatus(_A)
_CCasaAffinityCacheDestSourcePort_Type=CiscoPort
_CCasaAffinityCacheDestSourcePort_Object=MibTableColumn
cCasaAffinityCacheDestSourcePort=_CCasaAffinityCacheDestSourcePort_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,5),_CCasaAffinityCacheDestSourcePort_Type())
cCasaAffinityCacheDestSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDestSourcePort.setStatus(_A)
_CCasaAffinityCacheDestProtocol_Type=CiscoIpProtocol
_CCasaAffinityCacheDestProtocol_Object=MibTableColumn
cCasaAffinityCacheDestProtocol=_CCasaAffinityCacheDestProtocol_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,6),_CCasaAffinityCacheDestProtocol_Type())
cCasaAffinityCacheDestProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDestProtocol.setStatus(_A)
_CCasaAffinityCacheDestDispAddr_Type=IpAddress
_CCasaAffinityCacheDestDispAddr_Object=MibTableColumn
cCasaAffinityCacheDestDispAddr=_CCasaAffinityCacheDestDispAddr_Object((1,3,6,1,4,1,9,9,122,1,4,2,1,7),_CCasaAffinityCacheDestDispAddr_Type())
cCasaAffinityCacheDestDispAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDestDispAddr.setStatus(_A)
_CCasaAffinityCacheDispatchTable_Object=MibTable
cCasaAffinityCacheDispatchTable=_CCasaAffinityCacheDispatchTable_Object((1,3,6,1,4,1,9,9,122,1,4,3))
if mibBuilder.loadTexts:cCasaAffinityCacheDispatchTable.setStatus(_A)
_CCasaAffinityCacheDispatchEntry_Object=MibTableRow
cCasaAffinityCacheDispatchEntry=_CCasaAffinityCacheDispatchEntry_Object((1,3,6,1,4,1,9,9,122,1,4,3,1))
cCasaAffinityCacheDispatchEntry.setIndexNames((0,_B,_D),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:cCasaAffinityCacheDispatchEntry.setStatus(_A)
_CCasaAffinityCacheDispDispAddr_Type=IpAddress
_CCasaAffinityCacheDispDispAddr_Object=MibTableColumn
cCasaAffinityCacheDispDispAddr=_CCasaAffinityCacheDispDispAddr_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,1),_CCasaAffinityCacheDispDispAddr_Type())
cCasaAffinityCacheDispDispAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheDispDispAddr.setStatus(_A)
_CCasaAffinityCacheDispatchIndex_Type=CasaFixedAffinityIndex
_CCasaAffinityCacheDispatchIndex_Object=MibTableColumn
cCasaAffinityCacheDispatchIndex=_CCasaAffinityCacheDispatchIndex_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,2),_CCasaAffinityCacheDispatchIndex_Type())
cCasaAffinityCacheDispatchIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cCasaAffinityCacheDispatchIndex.setStatus(_A)
_CCasaAffinityCacheDispDestAddr_Type=IpAddress
_CCasaAffinityCacheDispDestAddr_Object=MibTableColumn
cCasaAffinityCacheDispDestAddr=_CCasaAffinityCacheDispDestAddr_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,3),_CCasaAffinityCacheDispDestAddr_Type())
cCasaAffinityCacheDispDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDispDestAddr.setStatus(_A)
_CCasaAffinityCacheDispDestPort_Type=CiscoPort
_CCasaAffinityCacheDispDestPort_Object=MibTableColumn
cCasaAffinityCacheDispDestPort=_CCasaAffinityCacheDispDestPort_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,4),_CCasaAffinityCacheDispDestPort_Type())
cCasaAffinityCacheDispDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDispDestPort.setStatus(_A)
_CCasaAffinityCacheDispSourceAddr_Type=IpAddress
_CCasaAffinityCacheDispSourceAddr_Object=MibTableColumn
cCasaAffinityCacheDispSourceAddr=_CCasaAffinityCacheDispSourceAddr_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,5),_CCasaAffinityCacheDispSourceAddr_Type())
cCasaAffinityCacheDispSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDispSourceAddr.setStatus(_A)
_CCasaAffinityCacheDispSourcePort_Type=CiscoPort
_CCasaAffinityCacheDispSourcePort_Object=MibTableColumn
cCasaAffinityCacheDispSourcePort=_CCasaAffinityCacheDispSourcePort_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,6),_CCasaAffinityCacheDispSourcePort_Type())
cCasaAffinityCacheDispSourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDispSourcePort.setStatus(_A)
_CCasaAffinityCacheDispProtocol_Type=CiscoIpProtocol
_CCasaAffinityCacheDispProtocol_Object=MibTableColumn
cCasaAffinityCacheDispProtocol=_CCasaAffinityCacheDispProtocol_Object((1,3,6,1,4,1,9,9,122,1,4,3,1,7),_CCasaAffinityCacheDispProtocol_Type())
cCasaAffinityCacheDispProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cCasaAffinityCacheDispProtocol.setStatus(_A)
_CiscoCasaMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoCasaMIBNotificationPrefix=_CiscoCasaMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,122,2))
_CiscoCasaMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoCasaMIBNotifications=_CiscoCasaMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,122,2,0))
_CiscoCasaMIBConformance_ObjectIdentity=ObjectIdentity
ciscoCasaMIBConformance=_CiscoCasaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,122,3))
_CiscoCasaMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCasaMIBCompliances=_CiscoCasaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,122,3,1))
_CiscoCasaMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCasaMIBGroups=_CiscoCasaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,122,3,2))
ciscoCasaGroup=ObjectGroup((1,3,6,1,4,1,9,9,122,3,2,1))
ciscoCasaGroup.setObjects(*((_B,_L),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoCasaGroup.setStatus(_A)
ciscoCasaAdminGroup=ObjectGroup((1,3,6,1,4,1,9,9,122,3,2,2))
ciscoCasaAdminGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciscoCasaAdminGroup.setStatus(_A)
ciscoCasaAffinityCacheGroup=ObjectGroup((1,3,6,1,4,1,9,9,122,3,2,3))
ciscoCasaAffinityCacheGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoCasaAffinityCacheGroup.setStatus(_A)
ciscoCasaStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,122,3,2,4))
ciscoCasaStatsGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoCasaStatsGroup.setStatus(_A)
ciscoCasaObsoleteGroup=ObjectGroup((1,3,6,1,4,1,9,9,122,3,2,5))
ciscoCasaObsoleteGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoCasaObsoleteGroup.setStatus(_J)
ciscoCasaStateChange=NotificationType((1,3,6,1,4,1,9,9,122,2,1))
ciscoCasaStateChange.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoCasaStateChange.setStatus(_A)
ciscoCasaNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,122,3,2,6))
ciscoCasaNotifGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:ciscoCasaNotifGroup.setStatus(_A)
ciscoCasaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,122,3,1,1))
ciscoCasaMIBCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ciscoCasaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CasaFixedAffinityIndex':CasaFixedAffinityIndex,'ciscoCasaMIB':ciscoCasaMIB,'ciscoCasaMIBObjects':ciscoCasaMIBObjects,'cCasaGlobal':cCasaGlobal,'cCasaTable':cCasaTable,'cCasaEntry':cCasaEntry,_D:cCasaEntity,_L:cCasaState,_W:cCasaStateNotificationEnabled,_X:cCasaCfgAddress,_A5:cCasaCfgAddressMask,_Y:cCasaCfgMcastAddress,_Z:cCasaAddress,_A6:cCasaAddressMask,_a:cCasaMcastAddress,'cCasaStats':cCasaStats,'cCasaAffinityCacheStatsTable':cCasaAffinityCacheStatsTable,'cCasaAffinityCacheStatsEntry':cCasaAffinityCacheStatsEntry,_f:cCasaAffinityCacheNumOf,_g:cCasaAffinityCacheHiWtrMrk,_h:cCasaAffinityCacheHiWtrMrkReset,_i:cCasaAffinityCacheNoStorageDrops,_j:cCasaAffinityCacheHits,_k:cCasaAffinityCacheHCHits,_l:cCasaAffinityCacheMisses,_m:cCasaAffinityCacheHCMisses,_n:cCasaAffinityCacheIntrTimeouts,'cCasaStatsTable':cCasaStatsTable,'cCasaStatsEntry':cCasaStatsEntry,_A3:cCasaInterestPackets,_A4:cCasaInterestTickles,'cCasaAdmin':cCasaAdmin,'cCasaAdminTable':cCasaAdminTable,'cCasaAdminEntry':cCasaAdminEntry,_P:cCasaAdminMcastPort,_b:cCasaAdminMcastPasswd,_c:cCasaAdminMcastPasswdTimeout,_d:cCasaAdminMcastPasswdFailures,_e:cCasaAdminRowStatus,'cCasaAffinityCache':cCasaAffinityCache,'cCasaAffinityCacheSrcTable':cCasaAffinityCacheSrcTable,'cCasaAffinityCacheSrcEntry':cCasaAffinityCacheSrcEntry,_Q:cCasaAffinityCacheSrcSourceAddr,_R:cCasaAffinityCacheSrcIndex,_o:cCasaAffinityCacheSrcSourcePort,_p:cCasaAffinityCacheSrcDestAddr,_q:cCasaAffinityCacheSrcDestPort,_r:cCasaAffinityCacheSrcProtocol,_s:cCasaAffinityCacheSrcDispAddr,'cCasaAffinityCacheDestTable':cCasaAffinityCacheDestTable,'cCasaAffinityCacheDestEntry':cCasaAffinityCacheDestEntry,_S:cCasaAffinityCacheDestDestAddr,_T:cCasaAffinityCacheDestIndex,_t:cCasaAffinityCacheDestDestPort,_u:cCasaAffinityCacheDestSourceAddr,_v:cCasaAffinityCacheDestSourcePort,_w:cCasaAffinityCacheDestProtocol,_x:cCasaAffinityCacheDestDispAddr,'cCasaAffinityCacheDispatchTable':cCasaAffinityCacheDispatchTable,'cCasaAffinityCacheDispatchEntry':cCasaAffinityCacheDispatchEntry,_U:cCasaAffinityCacheDispDispAddr,_V:cCasaAffinityCacheDispatchIndex,_y:cCasaAffinityCacheDispDestAddr,_z:cCasaAffinityCacheDispDestPort,_A0:cCasaAffinityCacheDispSourceAddr,_A1:cCasaAffinityCacheDispSourcePort,_A2:cCasaAffinityCacheDispProtocol,'ciscoCasaMIBNotificationPrefix':ciscoCasaMIBNotificationPrefix,'ciscoCasaMIBNotifications':ciscoCasaMIBNotifications,_A7:ciscoCasaStateChange,'ciscoCasaMIBConformance':ciscoCasaMIBConformance,'ciscoCasaMIBCompliances':ciscoCasaMIBCompliances,'ciscoCasaMIBCompliance':ciscoCasaMIBCompliance,'ciscoCasaMIBGroups':ciscoCasaMIBGroups,_A8:ciscoCasaGroup,_A9:ciscoCasaAdminGroup,_AA:ciscoCasaAffinityCacheGroup,_AB:ciscoCasaStatsGroup,'ciscoCasaObsoleteGroup':ciscoCasaObsoleteGroup,_AC:ciscoCasaNotifGroup})