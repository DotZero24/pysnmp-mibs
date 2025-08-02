_B0='natPacketDiscard'
_A_='natAddrMapAddrUsed'
_Az='natAddrMapDiscards'
_Ay='natAddrMapOutTranslates'
_Ax='natAddrMapInTranslates'
_Aw='natProtocolDiscards'
_Av='natProtocolOutTranslates'
_Au='natProtocolInTranslates'
_At='natInterfaceDiscards'
_As='natInterfaceOutTranslates'
_Ar='natInterfaceInTranslates'
_Aq='natSessionOutTranslates'
_Ap='natSessionInTranslates'
_Ao='natSessionCurrentIdleTime'
_An='natSessionMaxIdleTime'
_Am='natSessionPublicDstPort'
_Al='natSessionPublicDstAddr'
_Ak='natSessionPublicSrcPort'
_Aj='natSessionPublicSrcAddr'
_Ai='natSessionPublicAddrType'
_Ah='natSessionPrivateDstPort'
_Ag='natSessionPrivateDstAddr'
_Af='natSessionPrivateSrcPort'
_Ae='natSessionPrivateSrcAddr'
_Ad='natSessionPrivateAddrType'
_Ac='natSessionProtocolType'
_Ab='natSessionAddrMapIndex'
_Aa='natSessionUpTime'
_AZ='natSessionDirection'
_AY='natSessionPrivateDstEPBindMode'
_AX='natSessionPrivateDstEPBindId'
_AW='natSessionPrivateSrcEPBindMode'
_AV='natSessionPrivateSrcEPBindId'
_AU='natAddrPortBindOutTranslates'
_AT='natAddrPortBindInTranslates'
_AS='natAddrPortBindCurrentIdleTime'
_AR='natAddrPortBindMaxIdleTime'
_AQ='natAddrPortBindSessions'
_AP='natAddrPortBindMapIndex'
_AO='natAddrPortBindType'
_AN='natAddrPortBindTranslationEntity'
_AM='natAddrPortBindId'
_AL='natAddrPortBindGlobalPort'
_AK='natAddrPortBindGlobalAddr'
_AJ='natAddrPortBindGlobalAddrType'
_AI='natAddrPortBindNumberOfEntries'
_AH='natAddrBindOutTranslates'
_AG='natAddrBindInTranslates'
_AF='natAddrBindCurrentIdleTime'
_AE='natAddrBindMaxIdleTime'
_AD='natAddrBindSessions'
_AC='natAddrBindMapIndex'
_AB='natAddrBindType'
_AA='natAddrBindTranslationEntity'
_A9='natAddrBindId'
_A8='natAddrBindGlobalAddr'
_A7='natAddrBindGlobalAddrType'
_A6='natAddrBindNumberOfEntries'
_A5='natNotifThrottlingInterval'
_A4='natTcpDefNegTimeout'
_A3='natTcpDefIdleTimeout'
_A2='natOtherDefIdleTimeout'
_A1='natIcmpDefIdleTimeout'
_A0='natUdpDefIdleTimeout'
_z='natBindDefIdleTimeout'
_y='natAddrMapRowStatus'
_x='natAddrMapStorageType'
_w='natAddrMapProtocol'
_v='natAddrMapGlobalPortTo'
_u='natAddrMapGlobalPortFrom'
_t='natAddrMapGlobalAddrTo'
_s='natAddrMapGlobalAddrFrom'
_r='natAddrMapGlobalAddrType'
_q='natAddrMapLocalPortTo'
_p='natAddrMapLocalPortFrom'
_o='natAddrMapLocalAddrTo'
_n='natAddrMapLocalAddrFrom'
_m='natAddrMapLocalAddrType'
_l='natAddrMapTranslationEntity'
_k='natAddrMapEntryType'
_j='natAddrMapName'
_i='natInterfaceRowStatus'
_h='natInterfaceStorageType'
_g='natInterfaceServiceType'
_f='natInterfaceRealm'
_e='natProtocol'
_d='natSessionIndex'
_c='natAddrPortBindProtocol'
_b='natAddrPortBindLocalPort'
_a='natAddrPortBindLocalAddr'
_Z='natAddrPortBindLocalAddrType'
_Y='natAddrBindLocalAddr'
_X='natAddrBindLocalAddrType'
_W='natAddrMapIndex'
_V='SnmpAdminString'
_U='natMIBNotificationGroup'
_T='natStatsAddrMapGroup'
_S='natStatsProtocolGroup'
_R='natStatsInterfaceGroup'
_Q='natTranslationGroup'
_P='natConfigGroup'
_O='StorageType'
_N='InetAddress'
_M='ifCounterDiscontinuityGroup'
_L='Integer32'
_K='InetPortNumber'
_J='seconds'
_I='read-write'
_H='Unsigned32'
_G='ifIndex'
_F='not-accessible'
_E='IF-MIB'
_D='read-create'
_C='read-only'
_B='NAT-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifCounterDiscontinuityGroup,ifIndex=mibBuilder.importSymbols(_E,_M,_G)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType',_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_O,'TextualConvention')
natMIB=ModuleIdentity((1,3,6,1,2,1,123))
if mibBuilder.loadTexts:natMIB.setRevisions(('2015-10-02 00:00','2005-03-21 00:00'))
class NatProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('other',2),('icmp',3),('udp',4),('tcp',5)))
class NatProtocolMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('icmp',1),('udp',2),('tcp',3)))
class NatAddrMapId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NatBindIdOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class NatBindId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NatSessionId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NatBindMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('addressBind',1),('addressPortBind',2)))
class NatAssociationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
class NatTranslationEntity(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('inboundSrcEndPoint',0),('outboundDstEndPoint',1),('inboundDstEndPoint',2),('outboundSrcEndPoint',3)))
_NatMIBNotifications_ObjectIdentity=ObjectIdentity
natMIBNotifications=_NatMIBNotifications_ObjectIdentity((1,3,6,1,2,1,123,0))
_NatMIBObjects_ObjectIdentity=ObjectIdentity
natMIBObjects=_NatMIBObjects_ObjectIdentity((1,3,6,1,2,1,123,1))
_NatDefTimeouts_ObjectIdentity=ObjectIdentity
natDefTimeouts=_NatDefTimeouts_ObjectIdentity((1,3,6,1,2,1,123,1,1))
class _NatBindDefIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_NatBindDefIdleTimeout_Type.__name__=_H
_NatBindDefIdleTimeout_Object=MibScalar
natBindDefIdleTimeout=_NatBindDefIdleTimeout_Object((1,3,6,1,2,1,123,1,1,1),_NatBindDefIdleTimeout_Type())
natBindDefIdleTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natBindDefIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:natBindDefIdleTimeout.setUnits(_J)
class _NatUdpDefIdleTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NatUdpDefIdleTimeout_Type.__name__=_H
_NatUdpDefIdleTimeout_Object=MibScalar
natUdpDefIdleTimeout=_NatUdpDefIdleTimeout_Object((1,3,6,1,2,1,123,1,1,2),_NatUdpDefIdleTimeout_Type())
natUdpDefIdleTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natUdpDefIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:natUdpDefIdleTimeout.setUnits(_J)
class _NatIcmpDefIdleTimeout_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NatIcmpDefIdleTimeout_Type.__name__=_H
_NatIcmpDefIdleTimeout_Object=MibScalar
natIcmpDefIdleTimeout=_NatIcmpDefIdleTimeout_Object((1,3,6,1,2,1,123,1,1,3),_NatIcmpDefIdleTimeout_Type())
natIcmpDefIdleTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natIcmpDefIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:natIcmpDefIdleTimeout.setUnits(_J)
class _NatOtherDefIdleTimeout_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NatOtherDefIdleTimeout_Type.__name__=_H
_NatOtherDefIdleTimeout_Object=MibScalar
natOtherDefIdleTimeout=_NatOtherDefIdleTimeout_Object((1,3,6,1,2,1,123,1,1,4),_NatOtherDefIdleTimeout_Type())
natOtherDefIdleTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natOtherDefIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:natOtherDefIdleTimeout.setUnits(_J)
class _NatTcpDefIdleTimeout_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NatTcpDefIdleTimeout_Type.__name__=_H
_NatTcpDefIdleTimeout_Object=MibScalar
natTcpDefIdleTimeout=_NatTcpDefIdleTimeout_Object((1,3,6,1,2,1,123,1,1,5),_NatTcpDefIdleTimeout_Type())
natTcpDefIdleTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natTcpDefIdleTimeout.setStatus(_A)
if mibBuilder.loadTexts:natTcpDefIdleTimeout.setUnits(_J)
class _NatTcpDefNegTimeout_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NatTcpDefNegTimeout_Type.__name__=_H
_NatTcpDefNegTimeout_Object=MibScalar
natTcpDefNegTimeout=_NatTcpDefNegTimeout_Object((1,3,6,1,2,1,123,1,1,6),_NatTcpDefNegTimeout_Type())
natTcpDefNegTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:natTcpDefNegTimeout.setStatus(_A)
if mibBuilder.loadTexts:natTcpDefNegTimeout.setUnits(_J)
_NatNotifCtrl_ObjectIdentity=ObjectIdentity
natNotifCtrl=_NatNotifCtrl_ObjectIdentity((1,3,6,1,2,1,123,1,2))
class _NatNotifThrottlingInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,3600))
_NatNotifThrottlingInterval_Type.__name__=_L
_NatNotifThrottlingInterval_Object=MibScalar
natNotifThrottlingInterval=_NatNotifThrottlingInterval_Object((1,3,6,1,2,1,123,1,2,1),_NatNotifThrottlingInterval_Type())
natNotifThrottlingInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:natNotifThrottlingInterval.setStatus(_A)
if mibBuilder.loadTexts:natNotifThrottlingInterval.setUnits(_J)
_NatInterfaceTable_Object=MibTable
natInterfaceTable=_NatInterfaceTable_Object((1,3,6,1,2,1,123,1,3))
if mibBuilder.loadTexts:natInterfaceTable.setStatus(_A)
_NatInterfaceEntry_Object=MibTableRow
natInterfaceEntry=_NatInterfaceEntry_Object((1,3,6,1,2,1,123,1,3,1))
natInterfaceEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:natInterfaceEntry.setStatus(_A)
class _NatInterfaceRealm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('private',1),('public',2)))
_NatInterfaceRealm_Type.__name__=_L
_NatInterfaceRealm_Object=MibTableColumn
natInterfaceRealm=_NatInterfaceRealm_Object((1,3,6,1,2,1,123,1,3,1,1),_NatInterfaceRealm_Type())
natInterfaceRealm.setMaxAccess(_D)
if mibBuilder.loadTexts:natInterfaceRealm.setStatus(_A)
class _NatInterfaceServiceType_Type(Bits):namedValues=NamedValues(*(('basicNat',0),('napt',1),('bidirectionalNat',2),('twiceNat',3)))
_NatInterfaceServiceType_Type.__name__='Bits'
_NatInterfaceServiceType_Object=MibTableColumn
natInterfaceServiceType=_NatInterfaceServiceType_Object((1,3,6,1,2,1,123,1,3,1,2),_NatInterfaceServiceType_Type())
natInterfaceServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:natInterfaceServiceType.setStatus(_A)
_NatInterfaceInTranslates_Type=Counter64
_NatInterfaceInTranslates_Object=MibTableColumn
natInterfaceInTranslates=_NatInterfaceInTranslates_Object((1,3,6,1,2,1,123,1,3,1,3),_NatInterfaceInTranslates_Type())
natInterfaceInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natInterfaceInTranslates.setStatus(_A)
_NatInterfaceOutTranslates_Type=Counter64
_NatInterfaceOutTranslates_Object=MibTableColumn
natInterfaceOutTranslates=_NatInterfaceOutTranslates_Object((1,3,6,1,2,1,123,1,3,1,4),_NatInterfaceOutTranslates_Type())
natInterfaceOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natInterfaceOutTranslates.setStatus(_A)
_NatInterfaceDiscards_Type=Counter64
_NatInterfaceDiscards_Object=MibTableColumn
natInterfaceDiscards=_NatInterfaceDiscards_Object((1,3,6,1,2,1,123,1,3,1,5),_NatInterfaceDiscards_Type())
natInterfaceDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:natInterfaceDiscards.setStatus(_A)
class _NatInterfaceStorageType_Type(StorageType):defaultValue=3
_NatInterfaceStorageType_Type.__name__=_O
_NatInterfaceStorageType_Object=MibTableColumn
natInterfaceStorageType=_NatInterfaceStorageType_Object((1,3,6,1,2,1,123,1,3,1,6),_NatInterfaceStorageType_Type())
natInterfaceStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:natInterfaceStorageType.setStatus(_A)
_NatInterfaceRowStatus_Type=RowStatus
_NatInterfaceRowStatus_Object=MibTableColumn
natInterfaceRowStatus=_NatInterfaceRowStatus_Object((1,3,6,1,2,1,123,1,3,1,7),_NatInterfaceRowStatus_Type())
natInterfaceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:natInterfaceRowStatus.setStatus(_A)
_NatAddrMapTable_Object=MibTable
natAddrMapTable=_NatAddrMapTable_Object((1,3,6,1,2,1,123,1,4))
if mibBuilder.loadTexts:natAddrMapTable.setStatus(_A)
_NatAddrMapEntry_Object=MibTableRow
natAddrMapEntry=_NatAddrMapEntry_Object((1,3,6,1,2,1,123,1,4,1))
natAddrMapEntry.setIndexNames((0,_E,_G),(0,_B,_W))
if mibBuilder.loadTexts:natAddrMapEntry.setStatus(_A)
_NatAddrMapIndex_Type=NatAddrMapId
_NatAddrMapIndex_Object=MibTableColumn
natAddrMapIndex=_NatAddrMapIndex_Object((1,3,6,1,2,1,123,1,4,1,1),_NatAddrMapIndex_Type())
natAddrMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrMapIndex.setStatus(_A)
class _NatAddrMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NatAddrMapName_Type.__name__=_V
_NatAddrMapName_Object=MibTableColumn
natAddrMapName=_NatAddrMapName_Object((1,3,6,1,2,1,123,1,4,1,2),_NatAddrMapName_Type())
natAddrMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapName.setStatus(_A)
_NatAddrMapEntryType_Type=NatAssociationType
_NatAddrMapEntryType_Object=MibTableColumn
natAddrMapEntryType=_NatAddrMapEntryType_Object((1,3,6,1,2,1,123,1,4,1,3),_NatAddrMapEntryType_Type())
natAddrMapEntryType.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapEntryType.setStatus(_A)
_NatAddrMapTranslationEntity_Type=NatTranslationEntity
_NatAddrMapTranslationEntity_Object=MibTableColumn
natAddrMapTranslationEntity=_NatAddrMapTranslationEntity_Object((1,3,6,1,2,1,123,1,4,1,4),_NatAddrMapTranslationEntity_Type())
natAddrMapTranslationEntity.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapTranslationEntity.setStatus(_A)
_NatAddrMapLocalAddrType_Type=InetAddressType
_NatAddrMapLocalAddrType_Object=MibTableColumn
natAddrMapLocalAddrType=_NatAddrMapLocalAddrType_Object((1,3,6,1,2,1,123,1,4,1,5),_NatAddrMapLocalAddrType_Type())
natAddrMapLocalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapLocalAddrType.setStatus(_A)
_NatAddrMapLocalAddrFrom_Type=InetAddress
_NatAddrMapLocalAddrFrom_Object=MibTableColumn
natAddrMapLocalAddrFrom=_NatAddrMapLocalAddrFrom_Object((1,3,6,1,2,1,123,1,4,1,6),_NatAddrMapLocalAddrFrom_Type())
natAddrMapLocalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapLocalAddrFrom.setStatus(_A)
_NatAddrMapLocalAddrTo_Type=InetAddress
_NatAddrMapLocalAddrTo_Object=MibTableColumn
natAddrMapLocalAddrTo=_NatAddrMapLocalAddrTo_Object((1,3,6,1,2,1,123,1,4,1,7),_NatAddrMapLocalAddrTo_Type())
natAddrMapLocalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapLocalAddrTo.setStatus(_A)
class _NatAddrMapLocalPortFrom_Type(InetPortNumber):defaultValue=0
_NatAddrMapLocalPortFrom_Type.__name__=_K
_NatAddrMapLocalPortFrom_Object=MibTableColumn
natAddrMapLocalPortFrom=_NatAddrMapLocalPortFrom_Object((1,3,6,1,2,1,123,1,4,1,8),_NatAddrMapLocalPortFrom_Type())
natAddrMapLocalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapLocalPortFrom.setStatus(_A)
class _NatAddrMapLocalPortTo_Type(InetPortNumber):defaultValue=0
_NatAddrMapLocalPortTo_Type.__name__=_K
_NatAddrMapLocalPortTo_Object=MibTableColumn
natAddrMapLocalPortTo=_NatAddrMapLocalPortTo_Object((1,3,6,1,2,1,123,1,4,1,9),_NatAddrMapLocalPortTo_Type())
natAddrMapLocalPortTo.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapLocalPortTo.setStatus(_A)
_NatAddrMapGlobalAddrType_Type=InetAddressType
_NatAddrMapGlobalAddrType_Object=MibTableColumn
natAddrMapGlobalAddrType=_NatAddrMapGlobalAddrType_Object((1,3,6,1,2,1,123,1,4,1,10),_NatAddrMapGlobalAddrType_Type())
natAddrMapGlobalAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapGlobalAddrType.setStatus(_A)
_NatAddrMapGlobalAddrFrom_Type=InetAddress
_NatAddrMapGlobalAddrFrom_Object=MibTableColumn
natAddrMapGlobalAddrFrom=_NatAddrMapGlobalAddrFrom_Object((1,3,6,1,2,1,123,1,4,1,11),_NatAddrMapGlobalAddrFrom_Type())
natAddrMapGlobalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapGlobalAddrFrom.setStatus(_A)
_NatAddrMapGlobalAddrTo_Type=InetAddress
_NatAddrMapGlobalAddrTo_Object=MibTableColumn
natAddrMapGlobalAddrTo=_NatAddrMapGlobalAddrTo_Object((1,3,6,1,2,1,123,1,4,1,12),_NatAddrMapGlobalAddrTo_Type())
natAddrMapGlobalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapGlobalAddrTo.setStatus(_A)
class _NatAddrMapGlobalPortFrom_Type(InetPortNumber):defaultValue=0
_NatAddrMapGlobalPortFrom_Type.__name__=_K
_NatAddrMapGlobalPortFrom_Object=MibTableColumn
natAddrMapGlobalPortFrom=_NatAddrMapGlobalPortFrom_Object((1,3,6,1,2,1,123,1,4,1,13),_NatAddrMapGlobalPortFrom_Type())
natAddrMapGlobalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapGlobalPortFrom.setStatus(_A)
class _NatAddrMapGlobalPortTo_Type(InetPortNumber):defaultValue=0
_NatAddrMapGlobalPortTo_Type.__name__=_K
_NatAddrMapGlobalPortTo_Object=MibTableColumn
natAddrMapGlobalPortTo=_NatAddrMapGlobalPortTo_Object((1,3,6,1,2,1,123,1,4,1,14),_NatAddrMapGlobalPortTo_Type())
natAddrMapGlobalPortTo.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapGlobalPortTo.setStatus(_A)
_NatAddrMapProtocol_Type=NatProtocolMap
_NatAddrMapProtocol_Object=MibTableColumn
natAddrMapProtocol=_NatAddrMapProtocol_Object((1,3,6,1,2,1,123,1,4,1,15),_NatAddrMapProtocol_Type())
natAddrMapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapProtocol.setStatus(_A)
_NatAddrMapInTranslates_Type=Counter64
_NatAddrMapInTranslates_Object=MibTableColumn
natAddrMapInTranslates=_NatAddrMapInTranslates_Object((1,3,6,1,2,1,123,1,4,1,16),_NatAddrMapInTranslates_Type())
natAddrMapInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrMapInTranslates.setStatus(_A)
_NatAddrMapOutTranslates_Type=Counter64
_NatAddrMapOutTranslates_Object=MibTableColumn
natAddrMapOutTranslates=_NatAddrMapOutTranslates_Object((1,3,6,1,2,1,123,1,4,1,17),_NatAddrMapOutTranslates_Type())
natAddrMapOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrMapOutTranslates.setStatus(_A)
_NatAddrMapDiscards_Type=Counter64
_NatAddrMapDiscards_Object=MibTableColumn
natAddrMapDiscards=_NatAddrMapDiscards_Object((1,3,6,1,2,1,123,1,4,1,18),_NatAddrMapDiscards_Type())
natAddrMapDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrMapDiscards.setStatus(_A)
_NatAddrMapAddrUsed_Type=Gauge32
_NatAddrMapAddrUsed_Object=MibTableColumn
natAddrMapAddrUsed=_NatAddrMapAddrUsed_Object((1,3,6,1,2,1,123,1,4,1,19),_NatAddrMapAddrUsed_Type())
natAddrMapAddrUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrMapAddrUsed.setStatus(_A)
class _NatAddrMapStorageType_Type(StorageType):defaultValue=3
_NatAddrMapStorageType_Type.__name__=_O
_NatAddrMapStorageType_Object=MibTableColumn
natAddrMapStorageType=_NatAddrMapStorageType_Object((1,3,6,1,2,1,123,1,4,1,20),_NatAddrMapStorageType_Type())
natAddrMapStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapStorageType.setStatus(_A)
_NatAddrMapRowStatus_Type=RowStatus
_NatAddrMapRowStatus_Object=MibTableColumn
natAddrMapRowStatus=_NatAddrMapRowStatus_Object((1,3,6,1,2,1,123,1,4,1,21),_NatAddrMapRowStatus_Type())
natAddrMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:natAddrMapRowStatus.setStatus(_A)
_NatAddrBindNumberOfEntries_Type=Gauge32
_NatAddrBindNumberOfEntries_Object=MibScalar
natAddrBindNumberOfEntries=_NatAddrBindNumberOfEntries_Object((1,3,6,1,2,1,123,1,5),_NatAddrBindNumberOfEntries_Type())
natAddrBindNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindNumberOfEntries.setStatus(_A)
_NatAddrBindTable_Object=MibTable
natAddrBindTable=_NatAddrBindTable_Object((1,3,6,1,2,1,123,1,6))
if mibBuilder.loadTexts:natAddrBindTable.setStatus(_A)
_NatAddrBindEntry_Object=MibTableRow
natAddrBindEntry=_NatAddrBindEntry_Object((1,3,6,1,2,1,123,1,6,1))
natAddrBindEntry.setIndexNames((0,_E,_G),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:natAddrBindEntry.setStatus(_A)
_NatAddrBindLocalAddrType_Type=InetAddressType
_NatAddrBindLocalAddrType_Object=MibTableColumn
natAddrBindLocalAddrType=_NatAddrBindLocalAddrType_Object((1,3,6,1,2,1,123,1,6,1,1),_NatAddrBindLocalAddrType_Type())
natAddrBindLocalAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrBindLocalAddrType.setStatus(_A)
class _NatAddrBindLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NatAddrBindLocalAddr_Type.__name__=_N
_NatAddrBindLocalAddr_Object=MibTableColumn
natAddrBindLocalAddr=_NatAddrBindLocalAddr_Object((1,3,6,1,2,1,123,1,6,1,2),_NatAddrBindLocalAddr_Type())
natAddrBindLocalAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrBindLocalAddr.setStatus(_A)
_NatAddrBindGlobalAddrType_Type=InetAddressType
_NatAddrBindGlobalAddrType_Object=MibTableColumn
natAddrBindGlobalAddrType=_NatAddrBindGlobalAddrType_Object((1,3,6,1,2,1,123,1,6,1,3),_NatAddrBindGlobalAddrType_Type())
natAddrBindGlobalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindGlobalAddrType.setStatus(_A)
_NatAddrBindGlobalAddr_Type=InetAddress
_NatAddrBindGlobalAddr_Object=MibTableColumn
natAddrBindGlobalAddr=_NatAddrBindGlobalAddr_Object((1,3,6,1,2,1,123,1,6,1,4),_NatAddrBindGlobalAddr_Type())
natAddrBindGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindGlobalAddr.setStatus(_A)
_NatAddrBindId_Type=NatBindId
_NatAddrBindId_Object=MibTableColumn
natAddrBindId=_NatAddrBindId_Object((1,3,6,1,2,1,123,1,6,1,5),_NatAddrBindId_Type())
natAddrBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindId.setStatus(_A)
_NatAddrBindTranslationEntity_Type=NatTranslationEntity
_NatAddrBindTranslationEntity_Object=MibTableColumn
natAddrBindTranslationEntity=_NatAddrBindTranslationEntity_Object((1,3,6,1,2,1,123,1,6,1,6),_NatAddrBindTranslationEntity_Type())
natAddrBindTranslationEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindTranslationEntity.setStatus(_A)
_NatAddrBindType_Type=NatAssociationType
_NatAddrBindType_Object=MibTableColumn
natAddrBindType=_NatAddrBindType_Object((1,3,6,1,2,1,123,1,6,1,7),_NatAddrBindType_Type())
natAddrBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindType.setStatus(_A)
_NatAddrBindMapIndex_Type=NatAddrMapId
_NatAddrBindMapIndex_Object=MibTableColumn
natAddrBindMapIndex=_NatAddrBindMapIndex_Object((1,3,6,1,2,1,123,1,6,1,8),_NatAddrBindMapIndex_Type())
natAddrBindMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindMapIndex.setStatus(_A)
_NatAddrBindSessions_Type=Gauge32
_NatAddrBindSessions_Object=MibTableColumn
natAddrBindSessions=_NatAddrBindSessions_Object((1,3,6,1,2,1,123,1,6,1,9),_NatAddrBindSessions_Type())
natAddrBindSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindSessions.setStatus(_A)
_NatAddrBindMaxIdleTime_Type=TimeTicks
_NatAddrBindMaxIdleTime_Object=MibTableColumn
natAddrBindMaxIdleTime=_NatAddrBindMaxIdleTime_Object((1,3,6,1,2,1,123,1,6,1,10),_NatAddrBindMaxIdleTime_Type())
natAddrBindMaxIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindMaxIdleTime.setStatus(_A)
_NatAddrBindCurrentIdleTime_Type=TimeTicks
_NatAddrBindCurrentIdleTime_Object=MibTableColumn
natAddrBindCurrentIdleTime=_NatAddrBindCurrentIdleTime_Object((1,3,6,1,2,1,123,1,6,1,11),_NatAddrBindCurrentIdleTime_Type())
natAddrBindCurrentIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindCurrentIdleTime.setStatus(_A)
_NatAddrBindInTranslates_Type=Counter64
_NatAddrBindInTranslates_Object=MibTableColumn
natAddrBindInTranslates=_NatAddrBindInTranslates_Object((1,3,6,1,2,1,123,1,6,1,12),_NatAddrBindInTranslates_Type())
natAddrBindInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindInTranslates.setStatus(_A)
_NatAddrBindOutTranslates_Type=Counter64
_NatAddrBindOutTranslates_Object=MibTableColumn
natAddrBindOutTranslates=_NatAddrBindOutTranslates_Object((1,3,6,1,2,1,123,1,6,1,13),_NatAddrBindOutTranslates_Type())
natAddrBindOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrBindOutTranslates.setStatus(_A)
_NatAddrPortBindNumberOfEntries_Type=Gauge32
_NatAddrPortBindNumberOfEntries_Object=MibScalar
natAddrPortBindNumberOfEntries=_NatAddrPortBindNumberOfEntries_Object((1,3,6,1,2,1,123,1,7),_NatAddrPortBindNumberOfEntries_Type())
natAddrPortBindNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindNumberOfEntries.setStatus(_A)
_NatAddrPortBindTable_Object=MibTable
natAddrPortBindTable=_NatAddrPortBindTable_Object((1,3,6,1,2,1,123,1,8))
if mibBuilder.loadTexts:natAddrPortBindTable.setStatus(_A)
_NatAddrPortBindEntry_Object=MibTableRow
natAddrPortBindEntry=_NatAddrPortBindEntry_Object((1,3,6,1,2,1,123,1,8,1))
natAddrPortBindEntry.setIndexNames((0,_E,_G),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:natAddrPortBindEntry.setStatus(_A)
_NatAddrPortBindLocalAddrType_Type=InetAddressType
_NatAddrPortBindLocalAddrType_Object=MibTableColumn
natAddrPortBindLocalAddrType=_NatAddrPortBindLocalAddrType_Object((1,3,6,1,2,1,123,1,8,1,1),_NatAddrPortBindLocalAddrType_Type())
natAddrPortBindLocalAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrPortBindLocalAddrType.setStatus(_A)
class _NatAddrPortBindLocalAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_NatAddrPortBindLocalAddr_Type.__name__=_N
_NatAddrPortBindLocalAddr_Object=MibTableColumn
natAddrPortBindLocalAddr=_NatAddrPortBindLocalAddr_Object((1,3,6,1,2,1,123,1,8,1,2),_NatAddrPortBindLocalAddr_Type())
natAddrPortBindLocalAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrPortBindLocalAddr.setStatus(_A)
_NatAddrPortBindLocalPort_Type=InetPortNumber
_NatAddrPortBindLocalPort_Object=MibTableColumn
natAddrPortBindLocalPort=_NatAddrPortBindLocalPort_Object((1,3,6,1,2,1,123,1,8,1,3),_NatAddrPortBindLocalPort_Type())
natAddrPortBindLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrPortBindLocalPort.setStatus(_A)
_NatAddrPortBindProtocol_Type=NatProtocolType
_NatAddrPortBindProtocol_Object=MibTableColumn
natAddrPortBindProtocol=_NatAddrPortBindProtocol_Object((1,3,6,1,2,1,123,1,8,1,4),_NatAddrPortBindProtocol_Type())
natAddrPortBindProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:natAddrPortBindProtocol.setStatus(_A)
_NatAddrPortBindGlobalAddrType_Type=InetAddressType
_NatAddrPortBindGlobalAddrType_Object=MibTableColumn
natAddrPortBindGlobalAddrType=_NatAddrPortBindGlobalAddrType_Object((1,3,6,1,2,1,123,1,8,1,5),_NatAddrPortBindGlobalAddrType_Type())
natAddrPortBindGlobalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindGlobalAddrType.setStatus(_A)
_NatAddrPortBindGlobalAddr_Type=InetAddress
_NatAddrPortBindGlobalAddr_Object=MibTableColumn
natAddrPortBindGlobalAddr=_NatAddrPortBindGlobalAddr_Object((1,3,6,1,2,1,123,1,8,1,6),_NatAddrPortBindGlobalAddr_Type())
natAddrPortBindGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindGlobalAddr.setStatus(_A)
_NatAddrPortBindGlobalPort_Type=InetPortNumber
_NatAddrPortBindGlobalPort_Object=MibTableColumn
natAddrPortBindGlobalPort=_NatAddrPortBindGlobalPort_Object((1,3,6,1,2,1,123,1,8,1,7),_NatAddrPortBindGlobalPort_Type())
natAddrPortBindGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindGlobalPort.setStatus(_A)
_NatAddrPortBindId_Type=NatBindId
_NatAddrPortBindId_Object=MibTableColumn
natAddrPortBindId=_NatAddrPortBindId_Object((1,3,6,1,2,1,123,1,8,1,8),_NatAddrPortBindId_Type())
natAddrPortBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindId.setStatus(_A)
_NatAddrPortBindTranslationEntity_Type=NatTranslationEntity
_NatAddrPortBindTranslationEntity_Object=MibTableColumn
natAddrPortBindTranslationEntity=_NatAddrPortBindTranslationEntity_Object((1,3,6,1,2,1,123,1,8,1,9),_NatAddrPortBindTranslationEntity_Type())
natAddrPortBindTranslationEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindTranslationEntity.setStatus(_A)
_NatAddrPortBindType_Type=NatAssociationType
_NatAddrPortBindType_Object=MibTableColumn
natAddrPortBindType=_NatAddrPortBindType_Object((1,3,6,1,2,1,123,1,8,1,10),_NatAddrPortBindType_Type())
natAddrPortBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindType.setStatus(_A)
_NatAddrPortBindMapIndex_Type=NatAddrMapId
_NatAddrPortBindMapIndex_Object=MibTableColumn
natAddrPortBindMapIndex=_NatAddrPortBindMapIndex_Object((1,3,6,1,2,1,123,1,8,1,11),_NatAddrPortBindMapIndex_Type())
natAddrPortBindMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindMapIndex.setStatus(_A)
_NatAddrPortBindSessions_Type=Gauge32
_NatAddrPortBindSessions_Object=MibTableColumn
natAddrPortBindSessions=_NatAddrPortBindSessions_Object((1,3,6,1,2,1,123,1,8,1,12),_NatAddrPortBindSessions_Type())
natAddrPortBindSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindSessions.setStatus(_A)
_NatAddrPortBindMaxIdleTime_Type=TimeTicks
_NatAddrPortBindMaxIdleTime_Object=MibTableColumn
natAddrPortBindMaxIdleTime=_NatAddrPortBindMaxIdleTime_Object((1,3,6,1,2,1,123,1,8,1,13),_NatAddrPortBindMaxIdleTime_Type())
natAddrPortBindMaxIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindMaxIdleTime.setStatus(_A)
_NatAddrPortBindCurrentIdleTime_Type=TimeTicks
_NatAddrPortBindCurrentIdleTime_Object=MibTableColumn
natAddrPortBindCurrentIdleTime=_NatAddrPortBindCurrentIdleTime_Object((1,3,6,1,2,1,123,1,8,1,14),_NatAddrPortBindCurrentIdleTime_Type())
natAddrPortBindCurrentIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindCurrentIdleTime.setStatus(_A)
_NatAddrPortBindInTranslates_Type=Counter64
_NatAddrPortBindInTranslates_Object=MibTableColumn
natAddrPortBindInTranslates=_NatAddrPortBindInTranslates_Object((1,3,6,1,2,1,123,1,8,1,15),_NatAddrPortBindInTranslates_Type())
natAddrPortBindInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindInTranslates.setStatus(_A)
_NatAddrPortBindOutTranslates_Type=Counter64
_NatAddrPortBindOutTranslates_Object=MibTableColumn
natAddrPortBindOutTranslates=_NatAddrPortBindOutTranslates_Object((1,3,6,1,2,1,123,1,8,1,16),_NatAddrPortBindOutTranslates_Type())
natAddrPortBindOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natAddrPortBindOutTranslates.setStatus(_A)
_NatSessionTable_Object=MibTable
natSessionTable=_NatSessionTable_Object((1,3,6,1,2,1,123,1,9))
if mibBuilder.loadTexts:natSessionTable.setStatus(_A)
_NatSessionEntry_Object=MibTableRow
natSessionEntry=_NatSessionEntry_Object((1,3,6,1,2,1,123,1,9,1))
natSessionEntry.setIndexNames((0,_E,_G),(0,_B,_d))
if mibBuilder.loadTexts:natSessionEntry.setStatus(_A)
_NatSessionIndex_Type=NatSessionId
_NatSessionIndex_Object=MibTableColumn
natSessionIndex=_NatSessionIndex_Object((1,3,6,1,2,1,123,1,9,1,1),_NatSessionIndex_Type())
natSessionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:natSessionIndex.setStatus(_A)
_NatSessionPrivateSrcEPBindId_Type=NatBindIdOrZero
_NatSessionPrivateSrcEPBindId_Object=MibTableColumn
natSessionPrivateSrcEPBindId=_NatSessionPrivateSrcEPBindId_Object((1,3,6,1,2,1,123,1,9,1,2),_NatSessionPrivateSrcEPBindId_Type())
natSessionPrivateSrcEPBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateSrcEPBindId.setStatus(_A)
_NatSessionPrivateSrcEPBindMode_Type=NatBindMode
_NatSessionPrivateSrcEPBindMode_Object=MibTableColumn
natSessionPrivateSrcEPBindMode=_NatSessionPrivateSrcEPBindMode_Object((1,3,6,1,2,1,123,1,9,1,3),_NatSessionPrivateSrcEPBindMode_Type())
natSessionPrivateSrcEPBindMode.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateSrcEPBindMode.setStatus(_A)
_NatSessionPrivateDstEPBindId_Type=NatBindIdOrZero
_NatSessionPrivateDstEPBindId_Object=MibTableColumn
natSessionPrivateDstEPBindId=_NatSessionPrivateDstEPBindId_Object((1,3,6,1,2,1,123,1,9,1,4),_NatSessionPrivateDstEPBindId_Type())
natSessionPrivateDstEPBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateDstEPBindId.setStatus(_A)
_NatSessionPrivateDstEPBindMode_Type=NatBindMode
_NatSessionPrivateDstEPBindMode_Object=MibTableColumn
natSessionPrivateDstEPBindMode=_NatSessionPrivateDstEPBindMode_Object((1,3,6,1,2,1,123,1,9,1,5),_NatSessionPrivateDstEPBindMode_Type())
natSessionPrivateDstEPBindMode.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateDstEPBindMode.setStatus(_A)
class _NatSessionDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_NatSessionDirection_Type.__name__=_L
_NatSessionDirection_Object=MibTableColumn
natSessionDirection=_NatSessionDirection_Object((1,3,6,1,2,1,123,1,9,1,6),_NatSessionDirection_Type())
natSessionDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionDirection.setStatus(_A)
_NatSessionUpTime_Type=TimeTicks
_NatSessionUpTime_Object=MibTableColumn
natSessionUpTime=_NatSessionUpTime_Object((1,3,6,1,2,1,123,1,9,1,7),_NatSessionUpTime_Type())
natSessionUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionUpTime.setStatus(_A)
_NatSessionAddrMapIndex_Type=NatAddrMapId
_NatSessionAddrMapIndex_Object=MibTableColumn
natSessionAddrMapIndex=_NatSessionAddrMapIndex_Object((1,3,6,1,2,1,123,1,9,1,8),_NatSessionAddrMapIndex_Type())
natSessionAddrMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionAddrMapIndex.setStatus(_A)
_NatSessionProtocolType_Type=NatProtocolType
_NatSessionProtocolType_Object=MibTableColumn
natSessionProtocolType=_NatSessionProtocolType_Object((1,3,6,1,2,1,123,1,9,1,9),_NatSessionProtocolType_Type())
natSessionProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionProtocolType.setStatus(_A)
_NatSessionPrivateAddrType_Type=InetAddressType
_NatSessionPrivateAddrType_Object=MibTableColumn
natSessionPrivateAddrType=_NatSessionPrivateAddrType_Object((1,3,6,1,2,1,123,1,9,1,10),_NatSessionPrivateAddrType_Type())
natSessionPrivateAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateAddrType.setStatus(_A)
_NatSessionPrivateSrcAddr_Type=InetAddress
_NatSessionPrivateSrcAddr_Object=MibTableColumn
natSessionPrivateSrcAddr=_NatSessionPrivateSrcAddr_Object((1,3,6,1,2,1,123,1,9,1,11),_NatSessionPrivateSrcAddr_Type())
natSessionPrivateSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateSrcAddr.setStatus(_A)
_NatSessionPrivateSrcPort_Type=InetPortNumber
_NatSessionPrivateSrcPort_Object=MibTableColumn
natSessionPrivateSrcPort=_NatSessionPrivateSrcPort_Object((1,3,6,1,2,1,123,1,9,1,12),_NatSessionPrivateSrcPort_Type())
natSessionPrivateSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateSrcPort.setStatus(_A)
_NatSessionPrivateDstAddr_Type=InetAddress
_NatSessionPrivateDstAddr_Object=MibTableColumn
natSessionPrivateDstAddr=_NatSessionPrivateDstAddr_Object((1,3,6,1,2,1,123,1,9,1,13),_NatSessionPrivateDstAddr_Type())
natSessionPrivateDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateDstAddr.setStatus(_A)
_NatSessionPrivateDstPort_Type=InetPortNumber
_NatSessionPrivateDstPort_Object=MibTableColumn
natSessionPrivateDstPort=_NatSessionPrivateDstPort_Object((1,3,6,1,2,1,123,1,9,1,14),_NatSessionPrivateDstPort_Type())
natSessionPrivateDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPrivateDstPort.setStatus(_A)
_NatSessionPublicAddrType_Type=InetAddressType
_NatSessionPublicAddrType_Object=MibTableColumn
natSessionPublicAddrType=_NatSessionPublicAddrType_Object((1,3,6,1,2,1,123,1,9,1,15),_NatSessionPublicAddrType_Type())
natSessionPublicAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPublicAddrType.setStatus(_A)
_NatSessionPublicSrcAddr_Type=InetAddress
_NatSessionPublicSrcAddr_Object=MibTableColumn
natSessionPublicSrcAddr=_NatSessionPublicSrcAddr_Object((1,3,6,1,2,1,123,1,9,1,16),_NatSessionPublicSrcAddr_Type())
natSessionPublicSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPublicSrcAddr.setStatus(_A)
_NatSessionPublicSrcPort_Type=InetPortNumber
_NatSessionPublicSrcPort_Object=MibTableColumn
natSessionPublicSrcPort=_NatSessionPublicSrcPort_Object((1,3,6,1,2,1,123,1,9,1,17),_NatSessionPublicSrcPort_Type())
natSessionPublicSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPublicSrcPort.setStatus(_A)
_NatSessionPublicDstAddr_Type=InetAddress
_NatSessionPublicDstAddr_Object=MibTableColumn
natSessionPublicDstAddr=_NatSessionPublicDstAddr_Object((1,3,6,1,2,1,123,1,9,1,18),_NatSessionPublicDstAddr_Type())
natSessionPublicDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPublicDstAddr.setStatus(_A)
_NatSessionPublicDstPort_Type=InetPortNumber
_NatSessionPublicDstPort_Object=MibTableColumn
natSessionPublicDstPort=_NatSessionPublicDstPort_Object((1,3,6,1,2,1,123,1,9,1,19),_NatSessionPublicDstPort_Type())
natSessionPublicDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionPublicDstPort.setStatus(_A)
_NatSessionMaxIdleTime_Type=TimeTicks
_NatSessionMaxIdleTime_Object=MibTableColumn
natSessionMaxIdleTime=_NatSessionMaxIdleTime_Object((1,3,6,1,2,1,123,1,9,1,20),_NatSessionMaxIdleTime_Type())
natSessionMaxIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionMaxIdleTime.setStatus(_A)
_NatSessionCurrentIdleTime_Type=TimeTicks
_NatSessionCurrentIdleTime_Object=MibTableColumn
natSessionCurrentIdleTime=_NatSessionCurrentIdleTime_Object((1,3,6,1,2,1,123,1,9,1,21),_NatSessionCurrentIdleTime_Type())
natSessionCurrentIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionCurrentIdleTime.setStatus(_A)
_NatSessionInTranslates_Type=Counter64
_NatSessionInTranslates_Object=MibTableColumn
natSessionInTranslates=_NatSessionInTranslates_Object((1,3,6,1,2,1,123,1,9,1,22),_NatSessionInTranslates_Type())
natSessionInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionInTranslates.setStatus(_A)
_NatSessionOutTranslates_Type=Counter64
_NatSessionOutTranslates_Object=MibTableColumn
natSessionOutTranslates=_NatSessionOutTranslates_Object((1,3,6,1,2,1,123,1,9,1,23),_NatSessionOutTranslates_Type())
natSessionOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natSessionOutTranslates.setStatus(_A)
_NatProtocolTable_Object=MibTable
natProtocolTable=_NatProtocolTable_Object((1,3,6,1,2,1,123,1,10))
if mibBuilder.loadTexts:natProtocolTable.setStatus(_A)
_NatProtocolEntry_Object=MibTableRow
natProtocolEntry=_NatProtocolEntry_Object((1,3,6,1,2,1,123,1,10,1))
natProtocolEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:natProtocolEntry.setStatus(_A)
_NatProtocol_Type=NatProtocolType
_NatProtocol_Object=MibTableColumn
natProtocol=_NatProtocol_Object((1,3,6,1,2,1,123,1,10,1,1),_NatProtocol_Type())
natProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:natProtocol.setStatus(_A)
_NatProtocolInTranslates_Type=Counter64
_NatProtocolInTranslates_Object=MibTableColumn
natProtocolInTranslates=_NatProtocolInTranslates_Object((1,3,6,1,2,1,123,1,10,1,2),_NatProtocolInTranslates_Type())
natProtocolInTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natProtocolInTranslates.setStatus(_A)
_NatProtocolOutTranslates_Type=Counter64
_NatProtocolOutTranslates_Object=MibTableColumn
natProtocolOutTranslates=_NatProtocolOutTranslates_Object((1,3,6,1,2,1,123,1,10,1,3),_NatProtocolOutTranslates_Type())
natProtocolOutTranslates.setMaxAccess(_C)
if mibBuilder.loadTexts:natProtocolOutTranslates.setStatus(_A)
_NatProtocolDiscards_Type=Counter64
_NatProtocolDiscards_Object=MibTableColumn
natProtocolDiscards=_NatProtocolDiscards_Object((1,3,6,1,2,1,123,1,10,1,4),_NatProtocolDiscards_Type())
natProtocolDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:natProtocolDiscards.setStatus(_A)
_NatMIBConformance_ObjectIdentity=ObjectIdentity
natMIBConformance=_NatMIBConformance_ObjectIdentity((1,3,6,1,2,1,123,2))
_NatMIBGroups_ObjectIdentity=ObjectIdentity
natMIBGroups=_NatMIBGroups_ObjectIdentity((1,3,6,1,2,1,123,2,1))
_NatMIBCompliances_ObjectIdentity=ObjectIdentity
natMIBCompliances=_NatMIBCompliances_ObjectIdentity((1,3,6,1,2,1,123,2,2))
natConfigGroup=ObjectGroup((1,3,6,1,2,1,123,2,1,1))
natConfigGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:natConfigGroup.setStatus(_A)
natTranslationGroup=ObjectGroup((1,3,6,1,2,1,123,2,1,2))
natTranslationGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:natTranslationGroup.setStatus(_A)
natStatsInterfaceGroup=ObjectGroup((1,3,6,1,2,1,123,2,1,3))
natStatsInterfaceGroup.setObjects(*((_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:natStatsInterfaceGroup.setStatus(_A)
natStatsProtocolGroup=ObjectGroup((1,3,6,1,2,1,123,2,1,4))
natStatsProtocolGroup.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:natStatsProtocolGroup.setStatus(_A)
natStatsAddrMapGroup=ObjectGroup((1,3,6,1,2,1,123,2,1,5))
natStatsAddrMapGroup.setObjects(*((_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:natStatsAddrMapGroup.setStatus(_A)
natPacketDiscard=NotificationType((1,3,6,1,2,1,123,0,1))
natPacketDiscard.setObjects((_E,_G))
if mibBuilder.loadTexts:natPacketDiscard.setStatus(_A)
natMIBNotificationGroup=NotificationGroup((1,3,6,1,2,1,123,2,1,6))
natMIBNotificationGroup.setObjects((_B,_B0))
if mibBuilder.loadTexts:natMIBNotificationGroup.setStatus(_A)
natMIBFullCompliance=ModuleCompliance((1,3,6,1,2,1,123,2,2,1))
natMIBFullCompliance.setObjects(*((_E,_M),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:natMIBFullCompliance.setStatus(_A)
natMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,123,2,2,2))
natMIBReadOnlyCompliance.setObjects(*((_E,_M),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:natMIBReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NatProtocolType':NatProtocolType,'NatProtocolMap':NatProtocolMap,'NatAddrMapId':NatAddrMapId,'NatBindIdOrZero':NatBindIdOrZero,'NatBindId':NatBindId,'NatSessionId':NatSessionId,'NatBindMode':NatBindMode,'NatAssociationType':NatAssociationType,'NatTranslationEntity':NatTranslationEntity,'natMIB':natMIB,'natMIBNotifications':natMIBNotifications,_B0:natPacketDiscard,'natMIBObjects':natMIBObjects,'natDefTimeouts':natDefTimeouts,_z:natBindDefIdleTimeout,_A0:natUdpDefIdleTimeout,_A1:natIcmpDefIdleTimeout,_A2:natOtherDefIdleTimeout,_A3:natTcpDefIdleTimeout,_A4:natTcpDefNegTimeout,'natNotifCtrl':natNotifCtrl,_A5:natNotifThrottlingInterval,'natInterfaceTable':natInterfaceTable,'natInterfaceEntry':natInterfaceEntry,_f:natInterfaceRealm,_g:natInterfaceServiceType,_Ar:natInterfaceInTranslates,_As:natInterfaceOutTranslates,_At:natInterfaceDiscards,_h:natInterfaceStorageType,_i:natInterfaceRowStatus,'natAddrMapTable':natAddrMapTable,'natAddrMapEntry':natAddrMapEntry,_W:natAddrMapIndex,_j:natAddrMapName,_k:natAddrMapEntryType,_l:natAddrMapTranslationEntity,_m:natAddrMapLocalAddrType,_n:natAddrMapLocalAddrFrom,_o:natAddrMapLocalAddrTo,_p:natAddrMapLocalPortFrom,_q:natAddrMapLocalPortTo,_r:natAddrMapGlobalAddrType,_s:natAddrMapGlobalAddrFrom,_t:natAddrMapGlobalAddrTo,_u:natAddrMapGlobalPortFrom,_v:natAddrMapGlobalPortTo,_w:natAddrMapProtocol,_Ax:natAddrMapInTranslates,_Ay:natAddrMapOutTranslates,_Az:natAddrMapDiscards,_A_:natAddrMapAddrUsed,_x:natAddrMapStorageType,_y:natAddrMapRowStatus,_A6:natAddrBindNumberOfEntries,'natAddrBindTable':natAddrBindTable,'natAddrBindEntry':natAddrBindEntry,_X:natAddrBindLocalAddrType,_Y:natAddrBindLocalAddr,_A7:natAddrBindGlobalAddrType,_A8:natAddrBindGlobalAddr,_A9:natAddrBindId,_AA:natAddrBindTranslationEntity,_AB:natAddrBindType,_AC:natAddrBindMapIndex,_AD:natAddrBindSessions,_AE:natAddrBindMaxIdleTime,_AF:natAddrBindCurrentIdleTime,_AG:natAddrBindInTranslates,_AH:natAddrBindOutTranslates,_AI:natAddrPortBindNumberOfEntries,'natAddrPortBindTable':natAddrPortBindTable,'natAddrPortBindEntry':natAddrPortBindEntry,_Z:natAddrPortBindLocalAddrType,_a:natAddrPortBindLocalAddr,_b:natAddrPortBindLocalPort,_c:natAddrPortBindProtocol,_AJ:natAddrPortBindGlobalAddrType,_AK:natAddrPortBindGlobalAddr,_AL:natAddrPortBindGlobalPort,_AM:natAddrPortBindId,_AN:natAddrPortBindTranslationEntity,_AO:natAddrPortBindType,_AP:natAddrPortBindMapIndex,_AQ:natAddrPortBindSessions,_AR:natAddrPortBindMaxIdleTime,_AS:natAddrPortBindCurrentIdleTime,_AT:natAddrPortBindInTranslates,_AU:natAddrPortBindOutTranslates,'natSessionTable':natSessionTable,'natSessionEntry':natSessionEntry,_d:natSessionIndex,_AV:natSessionPrivateSrcEPBindId,_AW:natSessionPrivateSrcEPBindMode,_AX:natSessionPrivateDstEPBindId,_AY:natSessionPrivateDstEPBindMode,_AZ:natSessionDirection,_Aa:natSessionUpTime,_Ab:natSessionAddrMapIndex,_Ac:natSessionProtocolType,_Ad:natSessionPrivateAddrType,_Ae:natSessionPrivateSrcAddr,_Af:natSessionPrivateSrcPort,_Ag:natSessionPrivateDstAddr,_Ah:natSessionPrivateDstPort,_Ai:natSessionPublicAddrType,_Aj:natSessionPublicSrcAddr,_Ak:natSessionPublicSrcPort,_Al:natSessionPublicDstAddr,_Am:natSessionPublicDstPort,_An:natSessionMaxIdleTime,_Ao:natSessionCurrentIdleTime,_Ap:natSessionInTranslates,_Aq:natSessionOutTranslates,'natProtocolTable':natProtocolTable,'natProtocolEntry':natProtocolEntry,_e:natProtocol,_Au:natProtocolInTranslates,_Av:natProtocolOutTranslates,_Aw:natProtocolDiscards,'natMIBConformance':natMIBConformance,'natMIBGroups':natMIBGroups,_P:natConfigGroup,_Q:natTranslationGroup,_R:natStatsInterfaceGroup,_S:natStatsProtocolGroup,_T:natStatsAddrMapGroup,_U:natMIBNotificationGroup,'natMIBCompliances':natMIBCompliances,'natMIBFullCompliance':natMIBFullCompliance,'natMIBReadOnlyCompliance':natMIBReadOnlyCompliance})