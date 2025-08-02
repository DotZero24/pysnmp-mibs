_v='hpSntpBroadcastServerGroup'
_u='hpSntpAuthenticationKeyIdConfigGroup1'
_t='hpSntpInetServerOobmGroup'
_s='hpSntpAuthenticationKeyIdConfigGroup'
_r='hpSntpServerConfigGroup'
_q='hpSntpBroadcastServerStatisticsAuthFailedPkts'
_p='hpSntpAuthenticationKeyEncrypted'
_o='hpSntpInetServerIsOobm'
_n='hpSntpInetServerRowStatus'
_m='hpSntpInetServerVersion'
_l='hpTimeSyncMethod'
_k='hpSntpServerRowStatus'
_j='hpSntpServerPriority'
_i='hpSntpServerVersion'
_h='hpSntpConfigPollInterval'
_g='hpSntpConfigMode'
_f='hpSntpServerStatisticsEntry'
_e='hpSntpBroadcastServerAddress'
_d='hpSntpAuthenticationKeyId'
_c='hpSntpInetServerAddress'
_b='hpSntpInetServerAddressType'
_a='hpSntpInetServerPriority'
_Z='hpSntpServerAddress'
_Y='disabled'
_X='TruthValue'
_W='hpTimeSyncMethodGroup'
_V='hpSntpConfigGroup'
_U='hpSntpInetServerAuthKeyId'
_T='hpSntpAuthentication'
_S='hpSntpStatsRcvdPkts'
_R='hpSntpStatsSentPkts'
_Q='hpSntpStatsDroppedPkts'
_P='hpSntpServerStatisticsAuthFailedPkts'
_O='hpSntpAuthenticationKeyRowStatus'
_N='hpSntpAuthenticationKeyTrusted'
_M='hpSntpAuthenticationKeyValue'
_L='hpSntpAuthenticationKeyAuthMode'
_K='Unsigned32'
_J='OctetString'
_I='hpSntpInetServerConfigGroup'
_H='read-write'
_G='read-only'
_F='not-accessible'
_E='deprecated'
_D='Integer32'
_C='read-create'
_B='current'
_A='HP-SNTPclientConfiguration-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfCommon,=mibBuilder.importSymbols('HP-ICF-OID','hpicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_X)
hpSntpConfigMod=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,1,8))
if mibBuilder.loadTexts:hpSntpConfigMod.setRevisions(('2015-05-24 00:00','2014-01-13 00:00','2011-02-12 00:00','2009-02-13 12:30','2009-02-10 15:39','2008-11-26 02:39','2000-11-03 02:39'))
_HpSntpConfig_ObjectIdentity=ObjectIdentity
hpSntpConfig=_HpSntpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,1))
class _HpSntpConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),('unicast',2),('broadcast',3),('dhcp',4)))
_HpSntpConfigMode_Type.__name__=_D
_HpSntpConfigMode_Object=MibScalar
hpSntpConfigMode=_HpSntpConfigMode_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,1),_HpSntpConfigMode_Type())
hpSntpConfigMode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpSntpConfigMode.setStatus(_B)
class _HpSntpConfigPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_HpSntpConfigPollInterval_Type.__name__=_D
_HpSntpConfigPollInterval_Object=MibScalar
hpSntpConfigPollInterval=_HpSntpConfigPollInterval_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,2),_HpSntpConfigPollInterval_Type())
hpSntpConfigPollInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:hpSntpConfigPollInterval.setStatus(_B)
_HpSntpConfigServerTable_Object=MibTable
hpSntpConfigServerTable=_HpSntpConfigServerTable_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3))
if mibBuilder.loadTexts:hpSntpConfigServerTable.setStatus(_E)
_HpSntpServerEntry_Object=MibTableRow
hpSntpServerEntry=_HpSntpServerEntry_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3,1))
hpSntpServerEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:hpSntpServerEntry.setStatus(_E)
_HpSntpServerAddress_Type=IpAddress
_HpSntpServerAddress_Object=MibTableColumn
hpSntpServerAddress=_HpSntpServerAddress_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3,1,1),_HpSntpServerAddress_Type())
hpSntpServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpServerAddress.setStatus(_E)
class _HpSntpServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HpSntpServerVersion_Type.__name__=_D
_HpSntpServerVersion_Object=MibTableColumn
hpSntpServerVersion=_HpSntpServerVersion_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3,1,2),_HpSntpServerVersion_Type())
hpSntpServerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpServerVersion.setStatus(_E)
class _HpSntpServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSntpServerPriority_Type.__name__=_D
_HpSntpServerPriority_Object=MibTableColumn
hpSntpServerPriority=_HpSntpServerPriority_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3,1,3),_HpSntpServerPriority_Type())
hpSntpServerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpServerPriority.setStatus(_E)
_HpSntpServerRowStatus_Type=RowStatus
_HpSntpServerRowStatus_Object=MibTableColumn
hpSntpServerRowStatus=_HpSntpServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,3,1,4),_HpSntpServerRowStatus_Type())
hpSntpServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpServerRowStatus.setStatus(_E)
_HpSntpInetConfigServerTable_Object=MibTable
hpSntpInetConfigServerTable=_HpSntpInetConfigServerTable_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4))
if mibBuilder.loadTexts:hpSntpInetConfigServerTable.setStatus(_B)
_HpSntpInetServerEntry_Object=MibTableRow
hpSntpInetServerEntry=_HpSntpInetServerEntry_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1))
hpSntpInetServerEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:hpSntpInetServerEntry.setStatus(_B)
class _HpSntpInetServerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSntpInetServerPriority_Type.__name__=_D
_HpSntpInetServerPriority_Object=MibTableColumn
hpSntpInetServerPriority=_HpSntpInetServerPriority_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,1),_HpSntpInetServerPriority_Type())
hpSntpInetServerPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpInetServerPriority.setStatus(_B)
_HpSntpInetServerAddressType_Type=InetAddressType
_HpSntpInetServerAddressType_Object=MibTableColumn
hpSntpInetServerAddressType=_HpSntpInetServerAddressType_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,2),_HpSntpInetServerAddressType_Type())
hpSntpInetServerAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpInetServerAddressType.setStatus(_B)
_HpSntpInetServerAddress_Type=InetAddress
_HpSntpInetServerAddress_Object=MibTableColumn
hpSntpInetServerAddress=_HpSntpInetServerAddress_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,3),_HpSntpInetServerAddress_Type())
hpSntpInetServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpInetServerAddress.setStatus(_B)
class _HpSntpInetServerVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HpSntpInetServerVersion_Type.__name__=_D
_HpSntpInetServerVersion_Object=MibTableColumn
hpSntpInetServerVersion=_HpSntpInetServerVersion_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,4),_HpSntpInetServerVersion_Type())
hpSntpInetServerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpInetServerVersion.setStatus(_B)
_HpSntpInetServerRowStatus_Type=RowStatus
_HpSntpInetServerRowStatus_Object=MibTableColumn
hpSntpInetServerRowStatus=_HpSntpInetServerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,5),_HpSntpInetServerRowStatus_Type())
hpSntpInetServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpInetServerRowStatus.setStatus(_B)
class _HpSntpInetServerIsOobm_Type(TruthValue):defaultValue=2
_HpSntpInetServerIsOobm_Type.__name__=_X
_HpSntpInetServerIsOobm_Object=MibTableColumn
hpSntpInetServerIsOobm=_HpSntpInetServerIsOobm_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,6),_HpSntpInetServerIsOobm_Type())
hpSntpInetServerIsOobm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpInetServerIsOobm.setStatus(_B)
class _HpSntpInetServerAuthKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpSntpInetServerAuthKeyId_Type.__name__=_K
_HpSntpInetServerAuthKeyId_Object=MibTableColumn
hpSntpInetServerAuthKeyId=_HpSntpInetServerAuthKeyId_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,4,1,7),_HpSntpInetServerAuthKeyId_Type())
hpSntpInetServerAuthKeyId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpInetServerAuthKeyId.setStatus(_B)
class _HpSntpAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_Y,2)))
_HpSntpAuthentication_Type.__name__=_D
_HpSntpAuthentication_Object=MibScalar
hpSntpAuthentication=_HpSntpAuthentication_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,5),_HpSntpAuthentication_Type())
hpSntpAuthentication.setMaxAccess(_H)
if mibBuilder.loadTexts:hpSntpAuthentication.setStatus(_B)
_HpSntpAuthenticationKeyTable_Object=MibTable
hpSntpAuthenticationKeyTable=_HpSntpAuthenticationKeyTable_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6))
if mibBuilder.loadTexts:hpSntpAuthenticationKeyTable.setStatus(_B)
_HpSntpAuthenticationKeyEntry_Object=MibTableRow
hpSntpAuthenticationKeyEntry=_HpSntpAuthenticationKeyEntry_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1))
hpSntpAuthenticationKeyEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:hpSntpAuthenticationKeyEntry.setStatus(_B)
class _HpSntpAuthenticationKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpSntpAuthenticationKeyId_Type.__name__=_K
_HpSntpAuthenticationKeyId_Object=MibTableColumn
hpSntpAuthenticationKeyId=_HpSntpAuthenticationKeyId_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,1),_HpSntpAuthenticationKeyId_Type())
hpSntpAuthenticationKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyId.setStatus(_B)
class _HpSntpAuthenticationKeyAuthMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('md5',2)))
_HpSntpAuthenticationKeyAuthMode_Type.__name__=_D
_HpSntpAuthenticationKeyAuthMode_Object=MibTableColumn
hpSntpAuthenticationKeyAuthMode=_HpSntpAuthenticationKeyAuthMode_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,2),_HpSntpAuthenticationKeyAuthMode_Type())
hpSntpAuthenticationKeyAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyAuthMode.setStatus(_B)
class _HpSntpAuthenticationKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpSntpAuthenticationKeyValue_Type.__name__=_J
_HpSntpAuthenticationKeyValue_Object=MibTableColumn
hpSntpAuthenticationKeyValue=_HpSntpAuthenticationKeyValue_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,3),_HpSntpAuthenticationKeyValue_Type())
hpSntpAuthenticationKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyValue.setStatus(_B)
_HpSntpAuthenticationKeyTrusted_Type=TruthValue
_HpSntpAuthenticationKeyTrusted_Object=MibTableColumn
hpSntpAuthenticationKeyTrusted=_HpSntpAuthenticationKeyTrusted_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,4),_HpSntpAuthenticationKeyTrusted_Type())
hpSntpAuthenticationKeyTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyTrusted.setStatus(_B)
_HpSntpAuthenticationKeyRowStatus_Type=RowStatus
_HpSntpAuthenticationKeyRowStatus_Object=MibTableColumn
hpSntpAuthenticationKeyRowStatus=_HpSntpAuthenticationKeyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,5),_HpSntpAuthenticationKeyRowStatus_Type())
hpSntpAuthenticationKeyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyRowStatus.setStatus(_B)
class _HpSntpAuthenticationKeyEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpSntpAuthenticationKeyEncrypted_Type.__name__=_J
_HpSntpAuthenticationKeyEncrypted_Object=MibTableColumn
hpSntpAuthenticationKeyEncrypted=_HpSntpAuthenticationKeyEncrypted_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,6,1,6),_HpSntpAuthenticationKeyEncrypted_Type())
hpSntpAuthenticationKeyEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSntpAuthenticationKeyEncrypted.setStatus(_B)
_HpSntpServerStatisticsTable_Object=MibTable
hpSntpServerStatisticsTable=_HpSntpServerStatisticsTable_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,7))
if mibBuilder.loadTexts:hpSntpServerStatisticsTable.setStatus(_B)
_HpSntpServerStatisticsEntry_Object=MibTableRow
hpSntpServerStatisticsEntry=_HpSntpServerStatisticsEntry_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,7,1))
if mibBuilder.loadTexts:hpSntpServerStatisticsEntry.setStatus(_B)
_HpSntpServerStatisticsAuthFailedPkts_Type=Counter32
_HpSntpServerStatisticsAuthFailedPkts_Object=MibTableColumn
hpSntpServerStatisticsAuthFailedPkts=_HpSntpServerStatisticsAuthFailedPkts_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,7,1,1),_HpSntpServerStatisticsAuthFailedPkts_Type())
hpSntpServerStatisticsAuthFailedPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSntpServerStatisticsAuthFailedPkts.setStatus(_B)
_HpSntpBroadcastServerTable_Object=MibTable
hpSntpBroadcastServerTable=_HpSntpBroadcastServerTable_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,8))
if mibBuilder.loadTexts:hpSntpBroadcastServerTable.setStatus(_B)
_HpSntpBroadcastServerEntry_Object=MibTableRow
hpSntpBroadcastServerEntry=_HpSntpBroadcastServerEntry_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,8,1))
hpSntpBroadcastServerEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:hpSntpBroadcastServerEntry.setStatus(_B)
_HpSntpBroadcastServerAddress_Type=IpAddress
_HpSntpBroadcastServerAddress_Object=MibTableColumn
hpSntpBroadcastServerAddress=_HpSntpBroadcastServerAddress_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,8,1,1),_HpSntpBroadcastServerAddress_Type())
hpSntpBroadcastServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpSntpBroadcastServerAddress.setStatus(_B)
_HpSntpBroadcastServerStatisticsAuthFailedPkts_Type=Counter32
_HpSntpBroadcastServerStatisticsAuthFailedPkts_Object=MibTableColumn
hpSntpBroadcastServerStatisticsAuthFailedPkts=_HpSntpBroadcastServerStatisticsAuthFailedPkts_Object((1,3,6,1,4,1,11,2,14,11,1,8,1,8,1,2),_HpSntpBroadcastServerStatisticsAuthFailedPkts_Type())
hpSntpBroadcastServerStatisticsAuthFailedPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSntpBroadcastServerStatisticsAuthFailedPkts.setStatus(_B)
_HpTimeSyncMethodMod_ObjectIdentity=ObjectIdentity
hpTimeSyncMethodMod=_HpTimeSyncMethodMod_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,2))
class _HpTimeSyncMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('sntp',2),('timep',3),('timepOrSntp',4),('ntp',5)))
_HpTimeSyncMethod_Type.__name__=_D
_HpTimeSyncMethod_Object=MibScalar
hpTimeSyncMethod=_HpTimeSyncMethod_Object((1,3,6,1,4,1,11,2,14,11,1,8,2,1),_HpTimeSyncMethod_Type())
hpTimeSyncMethod.setMaxAccess(_H)
if mibBuilder.loadTexts:hpTimeSyncMethod.setStatus(_B)
_HpSntpConfigConformance_ObjectIdentity=ObjectIdentity
hpSntpConfigConformance=_HpSntpConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,3))
_HpSntpConfigCompliances_ObjectIdentity=ObjectIdentity
hpSntpConfigCompliances=_HpSntpConfigCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,3,1))
_HpSntpConfigGroups_ObjectIdentity=ObjectIdentity
hpSntpConfigGroups=_HpSntpConfigGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,3,2))
_HpSntpStatistics_ObjectIdentity=ObjectIdentity
hpSntpStatistics=_HpSntpStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,1,8,4))
_HpSntpStatsRcvdPkts_Type=Counter32
_HpSntpStatsRcvdPkts_Object=MibScalar
hpSntpStatsRcvdPkts=_HpSntpStatsRcvdPkts_Object((1,3,6,1,4,1,11,2,14,11,1,8,4,1),_HpSntpStatsRcvdPkts_Type())
hpSntpStatsRcvdPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSntpStatsRcvdPkts.setStatus(_B)
_HpSntpStatsSentPkts_Type=Counter32
_HpSntpStatsSentPkts_Object=MibScalar
hpSntpStatsSentPkts=_HpSntpStatsSentPkts_Object((1,3,6,1,4,1,11,2,14,11,1,8,4,2),_HpSntpStatsSentPkts_Type())
hpSntpStatsSentPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSntpStatsSentPkts.setStatus(_B)
_HpSntpStatsDroppedPkts_Type=Counter32
_HpSntpStatsDroppedPkts_Object=MibScalar
hpSntpStatsDroppedPkts=_HpSntpStatsDroppedPkts_Object((1,3,6,1,4,1,11,2,14,11,1,8,4,3),_HpSntpStatsDroppedPkts_Type())
hpSntpStatsDroppedPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:hpSntpStatsDroppedPkts.setStatus(_B)
hpSntpInetServerEntry.registerAugmentions((_A,_f))
hpSntpServerStatisticsEntry.setIndexNames(*hpSntpInetServerEntry.getIndexNames())
hpSntpConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,1))
hpSntpConfigGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpSntpConfigGroup.setStatus(_B)
hpSntpServerConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,2))
hpSntpServerConfigGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:hpSntpServerConfigGroup.setStatus(_E)
hpTimeSyncMethodGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,3))
hpTimeSyncMethodGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:hpTimeSyncMethodGroup.setStatus(_B)
hpSntpInetServerConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,4))
hpSntpInetServerConfigGroup.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hpSntpInetServerConfigGroup.setStatus(_B)
hpSntpAuthenticationKeyIdConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,5))
hpSntpAuthenticationKeyIdConfigGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hpSntpAuthenticationKeyIdConfigGroup.setStatus(_E)
hpSntpInetServerOobmGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,6))
hpSntpInetServerOobmGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:hpSntpInetServerOobmGroup.setStatus(_B)
hpSntpAuthenticationKeyIdConfigGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,7))
hpSntpAuthenticationKeyIdConfigGroup1.setObjects(*((_A,_L),(_A,_M),(_A,_p),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hpSntpAuthenticationKeyIdConfigGroup1.setStatus(_B)
hpSntpBroadcastServerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,1,8,3,2,8))
hpSntpBroadcastServerGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:hpSntpBroadcastServerGroup.setStatus(_B)
hpSntpConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,1))
hpSntpConfigCompliance.setObjects(*((_A,_V),(_A,_r),(_A,_W)))
if mibBuilder.loadTexts:hpSntpConfigCompliance.setStatus(_E)
hpSntpInetConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,2))
hpSntpInetConfigCompliance.setObjects(*((_A,_V),(_A,_I),(_A,_W)))
if mibBuilder.loadTexts:hpSntpInetConfigCompliance.setStatus(_B)
hpSntpAuthenticationConfigCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,3))
hpSntpAuthenticationConfigCompliance.setObjects(*((_A,_I),(_A,_s)))
if mibBuilder.loadTexts:hpSntpAuthenticationConfigCompliance.setStatus(_E)
hpSntpInetConfigComplianceOobm=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,4))
hpSntpInetConfigComplianceOobm.setObjects((_A,_t))
if mibBuilder.loadTexts:hpSntpInetConfigComplianceOobm.setStatus(_B)
hpSntpAuthenticationConfigCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,5))
hpSntpAuthenticationConfigCompliance1.setObjects(*((_A,_I),(_A,_u)))
if mibBuilder.loadTexts:hpSntpAuthenticationConfigCompliance1.setStatus(_B)
hpSntpBroadcastServerCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,1,8,3,1,6))
hpSntpBroadcastServerCompliance.setObjects((_A,_v))
if mibBuilder.loadTexts:hpSntpBroadcastServerCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpSntpConfigMod':hpSntpConfigMod,'hpSntpConfig':hpSntpConfig,_g:hpSntpConfigMode,_h:hpSntpConfigPollInterval,'hpSntpConfigServerTable':hpSntpConfigServerTable,'hpSntpServerEntry':hpSntpServerEntry,_Z:hpSntpServerAddress,_i:hpSntpServerVersion,_j:hpSntpServerPriority,_k:hpSntpServerRowStatus,'hpSntpInetConfigServerTable':hpSntpInetConfigServerTable,'hpSntpInetServerEntry':hpSntpInetServerEntry,_a:hpSntpInetServerPriority,_b:hpSntpInetServerAddressType,_c:hpSntpInetServerAddress,_m:hpSntpInetServerVersion,_n:hpSntpInetServerRowStatus,_o:hpSntpInetServerIsOobm,_U:hpSntpInetServerAuthKeyId,_T:hpSntpAuthentication,'hpSntpAuthenticationKeyTable':hpSntpAuthenticationKeyTable,'hpSntpAuthenticationKeyEntry':hpSntpAuthenticationKeyEntry,_d:hpSntpAuthenticationKeyId,_L:hpSntpAuthenticationKeyAuthMode,_M:hpSntpAuthenticationKeyValue,_N:hpSntpAuthenticationKeyTrusted,_O:hpSntpAuthenticationKeyRowStatus,_p:hpSntpAuthenticationKeyEncrypted,'hpSntpServerStatisticsTable':hpSntpServerStatisticsTable,_f:hpSntpServerStatisticsEntry,_P:hpSntpServerStatisticsAuthFailedPkts,'hpSntpBroadcastServerTable':hpSntpBroadcastServerTable,'hpSntpBroadcastServerEntry':hpSntpBroadcastServerEntry,_e:hpSntpBroadcastServerAddress,_q:hpSntpBroadcastServerStatisticsAuthFailedPkts,'hpTimeSyncMethodMod':hpTimeSyncMethodMod,_l:hpTimeSyncMethod,'hpSntpConfigConformance':hpSntpConfigConformance,'hpSntpConfigCompliances':hpSntpConfigCompliances,'hpSntpConfigCompliance':hpSntpConfigCompliance,'hpSntpInetConfigCompliance':hpSntpInetConfigCompliance,'hpSntpAuthenticationConfigCompliance':hpSntpAuthenticationConfigCompliance,'hpSntpInetConfigComplianceOobm':hpSntpInetConfigComplianceOobm,'hpSntpAuthenticationConfigCompliance1':hpSntpAuthenticationConfigCompliance1,'hpSntpBroadcastServerCompliance':hpSntpBroadcastServerCompliance,'hpSntpConfigGroups':hpSntpConfigGroups,_V:hpSntpConfigGroup,_r:hpSntpServerConfigGroup,_W:hpTimeSyncMethodGroup,_I:hpSntpInetServerConfigGroup,_s:hpSntpAuthenticationKeyIdConfigGroup,_t:hpSntpInetServerOobmGroup,_u:hpSntpAuthenticationKeyIdConfigGroup1,_v:hpSntpBroadcastServerGroup,'hpSntpStatistics':hpSntpStatistics,_S:hpSntpStatsRcvdPkts,_R:hpSntpStatsSentPkts,_Q:hpSntpStatsDroppedPkts})