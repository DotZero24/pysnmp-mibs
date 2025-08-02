_B3='cnatBindGroup'
_B2='cnatConfigGroup'
_B1='cnatInterfacePktsOut'
_B0='cnatInterfacePktsIn'
_A_='cnatAddrMapStatsAddrUsed'
_Az='cnatAddrMapStatsNoResource'
_Ay='cnatAddrMapStatsOutTranslate'
_Ax='cnatAddrMapStatsInTranslate'
_Aw='cnatProtocolStatsRejectCount'
_Av='cnatProtocolStatsOutTranslate'
_Au='cnatProtocolStatsInTranslate'
_At='cnatSessionOutTranslate'
_As='cnatSessionInTranslate'
_Ar='cnatSessionSecondBindId'
_Aq='cnatSessionCurrentIdletime'
_Ap='cnatSessionTransPublicPort'
_Ao='cnatSessionOrigPublicPort'
_An='cnatSessionTransPublicAddr'
_Am='cnatSessionOrigPublicAddr'
_Al='cnatSessionTransPrivatePort'
_Ak='cnatSessionOrigPrivatePort'
_Aj='cnatSessionTransPrivateAddr'
_Ai='cnatSessionOrigPrivateAddr'
_Ah='cnatSessionProtocolType'
_Ag='cnatSessionUpTime'
_Af='cnatSessionDirection'
_Ae='cnatAddrPortBindOutTranslate'
_Ad='cnatAddrPortBindInTranslate'
_Ac='cnatAddrPortBindCurrentIdleTime'
_Ab='cnatAddrPortBindSessionCount'
_Aa='cnatAddrPortBindConfName'
_AZ='cnatAddrPortBindType'
_AY='cnatAddrPortBindDirection'
_AX='cnatAddrPortBindId'
_AW='cnatAddrPortBindGlobalPort'
_AV='cnatAddrPortBindGlobalAddr'
_AU='cnatAddrPortBindNumberOfEntries'
_AT='cnatAddrBindOutTranslate'
_AS='cnatAddrBindInTranslate'
_AR='cnatAddrBindCurrentIdleTime'
_AQ='cnatAddrBindSessionCount'
_AP='cnatAddrBindConfName'
_AO='cnatAddrBindType'
_AN='cnatAddrBindDirection'
_AM='cnatAddrBindId'
_AL='cnatAddrBindGlobalAddr'
_AK='cnatAddrBindNumberOfEntries'
_AJ='cnatInterfaceStatus'
_AI='cnatInterfaceStorageType'
_AH='cnatInterfaceRealm'
_AG='cnatConfDynAddrMapStatus'
_AF='cnatConfDynAddrMapStorageType'
_AE='cnatConfDynProtocol'
_AD='cnatConfDynGlobalPortTo'
_AC='cnatConfDynGlobalPortFrom'
_AB='cnatConfDynGlobalAddrTo'
_AA='cnatConfDynGlobalAddrFrom'
_A9='cnatConfDynLocalPortTo'
_A8='cnatConfDynLocalPortFrom'
_A7='cnatConfDynLocalAddrTo'
_A6='cnatConfDynLocalAddrFrom'
_A5='cnatConfDynAddressMapType'
_A4='cnatConfStaticAddrMapStatus'
_A3='cnatConfStaticAddrMapStorageType'
_A2='cnatConfStaticProtocol'
_A1='cnatConfStaticGlobalPortTo'
_A0='cnatConfStaticGlobalPortFrom'
_z='cnatConfStaticGlobalAddrTo'
_y='cnatConfStaticGlobalAddrFrom'
_x='cnatConfStaticLocalPortTo'
_w='cnatConfStaticLocalPortFrom'
_v='cnatConfStaticLocalAddrTo'
_u='cnatConfStaticLocalAddrFrom'
_t='cnatConfStaticAddrMapType'
_s='cnatConfStatus'
_r='cnatConfStorageType'
_q='cnatConfMaxBindIdleTime'
_p='cnatConfMaxBindLeaseTime'
_o='cnatConfTimeoutOther'
_n='cnatConfTimeoutTcpNeg'
_m='cnatConfTimeoutTcpIdle'
_l='cnatConfTimeoutUdpIdle'
_k='cnatConfTimeoutIcmpIdle'
_j='cnatConfServiceType'
_i='cnatInterfaceStatsEntry'
_h='cnatAddrMapStatsMapName'
_g='cnatAddrMapStatsConfName'
_f='cnatProtocolStatsName'
_e='cnatSessionId'
_d='cnatSessionBindId'
_c='cnatAddrPortBindProtocol'
_b='cnatAddrPortBindLocalPort'
_a='cnatAddrPortBindLocalAddr'
_Z='dynamic'
_Y='static'
_X='biDirectional'
_W='uniDirectional'
_V='cnatAddrBindLocalAddr'
_U='cnatInterfaceIndex'
_T='cnatConfDynAddrMapName'
_S='cnatConfStaticAddrMapName'
_R='all'
_Q='outbound'
_P='inbound'
_O='cnatConfName'
_N='tcp'
_M='udp'
_L='icmp'
_K='other'
_J='Bits'
_I='StorageType'
_H='seconds'
_G='SnmpAdminString'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-IETF-NAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention')
ciscoIetfNatMIB=ModuleIdentity((1,3,6,1,4,1,9,10,77))
if mibBuilder.loadTexts:ciscoIetfNatMIB.setRevisions(('2001-03-01 00:00',))
class NATProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_CiscoNatMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNatMIBObjects=_CiscoNatMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,77,1))
_CnatConfig_ObjectIdentity=ObjectIdentity
cnatConfig=_CnatConfig_ObjectIdentity((1,3,6,1,4,1,9,10,77,1,1))
_CnatConfTable_Object=MibTable
cnatConfTable=_CnatConfTable_Object((1,3,6,1,4,1,9,10,77,1,1,1))
if mibBuilder.loadTexts:cnatConfTable.setStatus(_A)
_CnatConfEntry_Object=MibTableRow
cnatConfEntry=_CnatConfEntry_Object((1,3,6,1,4,1,9,10,77,1,1,1,1))
cnatConfEntry.setIndexNames((1,_B,_O))
if mibBuilder.loadTexts:cnatConfEntry.setStatus(_A)
class _CnatConfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatConfName_Type.__name__=_G
_CnatConfName_Object=MibTableColumn
cnatConfName=_CnatConfName_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,1),_CnatConfName_Type())
cnatConfName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatConfName.setStatus(_A)
class _CnatConfServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('basicNat',1),('napt',2),('bidirectionalNat',3),('twiceNat',4),('multihomedNat',5)))
_CnatConfServiceType_Type.__name__=_E
_CnatConfServiceType_Object=MibTableColumn
cnatConfServiceType=_CnatConfServiceType_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,2),_CnatConfServiceType_Type())
cnatConfServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfServiceType.setStatus(_A)
class _CnatConfTimeoutIcmpIdle_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfTimeoutIcmpIdle_Type.__name__=_E
_CnatConfTimeoutIcmpIdle_Object=MibTableColumn
cnatConfTimeoutIcmpIdle=_CnatConfTimeoutIcmpIdle_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,3),_CnatConfTimeoutIcmpIdle_Type())
cnatConfTimeoutIcmpIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfTimeoutIcmpIdle.setStatus(_A)
if mibBuilder.loadTexts:cnatConfTimeoutIcmpIdle.setUnits(_H)
class _CnatConfTimeoutUdpIdle_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfTimeoutUdpIdle_Type.__name__=_E
_CnatConfTimeoutUdpIdle_Object=MibTableColumn
cnatConfTimeoutUdpIdle=_CnatConfTimeoutUdpIdle_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,4),_CnatConfTimeoutUdpIdle_Type())
cnatConfTimeoutUdpIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfTimeoutUdpIdle.setStatus(_A)
if mibBuilder.loadTexts:cnatConfTimeoutUdpIdle.setUnits(_H)
class _CnatConfTimeoutTcpIdle_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfTimeoutTcpIdle_Type.__name__=_E
_CnatConfTimeoutTcpIdle_Object=MibTableColumn
cnatConfTimeoutTcpIdle=_CnatConfTimeoutTcpIdle_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,5),_CnatConfTimeoutTcpIdle_Type())
cnatConfTimeoutTcpIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfTimeoutTcpIdle.setStatus(_A)
if mibBuilder.loadTexts:cnatConfTimeoutTcpIdle.setUnits(_H)
class _CnatConfTimeoutTcpNeg_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfTimeoutTcpNeg_Type.__name__=_E
_CnatConfTimeoutTcpNeg_Object=MibTableColumn
cnatConfTimeoutTcpNeg=_CnatConfTimeoutTcpNeg_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,6),_CnatConfTimeoutTcpNeg_Type())
cnatConfTimeoutTcpNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfTimeoutTcpNeg.setStatus(_A)
if mibBuilder.loadTexts:cnatConfTimeoutTcpNeg.setUnits(_H)
class _CnatConfTimeoutOther_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfTimeoutOther_Type.__name__=_E
_CnatConfTimeoutOther_Object=MibTableColumn
cnatConfTimeoutOther=_CnatConfTimeoutOther_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,7),_CnatConfTimeoutOther_Type())
cnatConfTimeoutOther.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfTimeoutOther.setStatus(_A)
if mibBuilder.loadTexts:cnatConfTimeoutOther.setUnits(_H)
class _CnatConfMaxBindLeaseTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfMaxBindLeaseTime_Type.__name__=_E
_CnatConfMaxBindLeaseTime_Object=MibTableColumn
cnatConfMaxBindLeaseTime=_CnatConfMaxBindLeaseTime_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,8),_CnatConfMaxBindLeaseTime_Type())
cnatConfMaxBindLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfMaxBindLeaseTime.setStatus(_A)
if mibBuilder.loadTexts:cnatConfMaxBindLeaseTime.setUnits(_H)
class _CnatConfMaxBindIdleTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CnatConfMaxBindIdleTime_Type.__name__=_E
_CnatConfMaxBindIdleTime_Object=MibTableColumn
cnatConfMaxBindIdleTime=_CnatConfMaxBindIdleTime_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,9),_CnatConfMaxBindIdleTime_Type())
cnatConfMaxBindIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfMaxBindIdleTime.setStatus(_A)
if mibBuilder.loadTexts:cnatConfMaxBindIdleTime.setUnits(_H)
class _CnatConfStorageType_Type(StorageType):defaultValue=3
_CnatConfStorageType_Type.__name__=_I
_CnatConfStorageType_Object=MibTableColumn
cnatConfStorageType=_CnatConfStorageType_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,10),_CnatConfStorageType_Type())
cnatConfStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStorageType.setStatus(_A)
_CnatConfStatus_Type=RowStatus
_CnatConfStatus_Object=MibTableColumn
cnatConfStatus=_CnatConfStatus_Object((1,3,6,1,4,1,9,10,77,1,1,1,1,11),_CnatConfStatus_Type())
cnatConfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStatus.setStatus(_A)
_CnatConfStaticAddrMapTable_Object=MibTable
cnatConfStaticAddrMapTable=_CnatConfStaticAddrMapTable_Object((1,3,6,1,4,1,9,10,77,1,1,2))
if mibBuilder.loadTexts:cnatConfStaticAddrMapTable.setStatus(_A)
_CnatConfStaticAddrMapEntry_Object=MibTableRow
cnatConfStaticAddrMapEntry=_CnatConfStaticAddrMapEntry_Object((1,3,6,1,4,1,9,10,77,1,1,2,1))
cnatConfStaticAddrMapEntry.setIndexNames((0,_B,_O),(0,_B,_S))
if mibBuilder.loadTexts:cnatConfStaticAddrMapEntry.setStatus(_A)
class _CnatConfStaticAddrMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatConfStaticAddrMapName_Type.__name__=_G
_CnatConfStaticAddrMapName_Object=MibTableColumn
cnatConfStaticAddrMapName=_CnatConfStaticAddrMapName_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,1),_CnatConfStaticAddrMapName_Type())
cnatConfStaticAddrMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatConfStaticAddrMapName.setStatus(_A)
class _CnatConfStaticAddrMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('both',3)))
_CnatConfStaticAddrMapType_Type.__name__=_E
_CnatConfStaticAddrMapType_Object=MibTableColumn
cnatConfStaticAddrMapType=_CnatConfStaticAddrMapType_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,2),_CnatConfStaticAddrMapType_Type())
cnatConfStaticAddrMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticAddrMapType.setStatus(_A)
_CnatConfStaticLocalAddrFrom_Type=IpAddress
_CnatConfStaticLocalAddrFrom_Object=MibTableColumn
cnatConfStaticLocalAddrFrom=_CnatConfStaticLocalAddrFrom_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,3),_CnatConfStaticLocalAddrFrom_Type())
cnatConfStaticLocalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticLocalAddrFrom.setStatus(_A)
_CnatConfStaticLocalAddrTo_Type=IpAddress
_CnatConfStaticLocalAddrTo_Object=MibTableColumn
cnatConfStaticLocalAddrTo=_CnatConfStaticLocalAddrTo_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,4),_CnatConfStaticLocalAddrTo_Type())
cnatConfStaticLocalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticLocalAddrTo.setStatus(_A)
class _CnatConfStaticLocalPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfStaticLocalPortFrom_Type.__name__=_E
_CnatConfStaticLocalPortFrom_Object=MibTableColumn
cnatConfStaticLocalPortFrom=_CnatConfStaticLocalPortFrom_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,5),_CnatConfStaticLocalPortFrom_Type())
cnatConfStaticLocalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticLocalPortFrom.setStatus(_A)
class _CnatConfStaticLocalPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfStaticLocalPortTo_Type.__name__=_E
_CnatConfStaticLocalPortTo_Object=MibTableColumn
cnatConfStaticLocalPortTo=_CnatConfStaticLocalPortTo_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,6),_CnatConfStaticLocalPortTo_Type())
cnatConfStaticLocalPortTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticLocalPortTo.setStatus(_A)
_CnatConfStaticGlobalAddrFrom_Type=IpAddress
_CnatConfStaticGlobalAddrFrom_Object=MibTableColumn
cnatConfStaticGlobalAddrFrom=_CnatConfStaticGlobalAddrFrom_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,7),_CnatConfStaticGlobalAddrFrom_Type())
cnatConfStaticGlobalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticGlobalAddrFrom.setStatus(_A)
_CnatConfStaticGlobalAddrTo_Type=IpAddress
_CnatConfStaticGlobalAddrTo_Object=MibTableColumn
cnatConfStaticGlobalAddrTo=_CnatConfStaticGlobalAddrTo_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,8),_CnatConfStaticGlobalAddrTo_Type())
cnatConfStaticGlobalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticGlobalAddrTo.setStatus(_A)
class _CnatConfStaticGlobalPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfStaticGlobalPortFrom_Type.__name__=_E
_CnatConfStaticGlobalPortFrom_Object=MibTableColumn
cnatConfStaticGlobalPortFrom=_CnatConfStaticGlobalPortFrom_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,9),_CnatConfStaticGlobalPortFrom_Type())
cnatConfStaticGlobalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticGlobalPortFrom.setStatus(_A)
class _CnatConfStaticGlobalPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfStaticGlobalPortTo_Type.__name__=_E
_CnatConfStaticGlobalPortTo_Object=MibTableColumn
cnatConfStaticGlobalPortTo=_CnatConfStaticGlobalPortTo_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,10),_CnatConfStaticGlobalPortTo_Type())
cnatConfStaticGlobalPortTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticGlobalPortTo.setStatus(_A)
class _CnatConfStaticProtocol_Type(Bits):namedValues=NamedValues(*((_R,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_CnatConfStaticProtocol_Type.__name__=_J
_CnatConfStaticProtocol_Object=MibTableColumn
cnatConfStaticProtocol=_CnatConfStaticProtocol_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,11),_CnatConfStaticProtocol_Type())
cnatConfStaticProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticProtocol.setStatus(_A)
class _CnatConfStaticAddrMapStorageType_Type(StorageType):defaultValue=3
_CnatConfStaticAddrMapStorageType_Type.__name__=_I
_CnatConfStaticAddrMapStorageType_Object=MibTableColumn
cnatConfStaticAddrMapStorageType=_CnatConfStaticAddrMapStorageType_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,12),_CnatConfStaticAddrMapStorageType_Type())
cnatConfStaticAddrMapStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticAddrMapStorageType.setStatus(_A)
_CnatConfStaticAddrMapStatus_Type=RowStatus
_CnatConfStaticAddrMapStatus_Object=MibTableColumn
cnatConfStaticAddrMapStatus=_CnatConfStaticAddrMapStatus_Object((1,3,6,1,4,1,9,10,77,1,1,2,1,13),_CnatConfStaticAddrMapStatus_Type())
cnatConfStaticAddrMapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfStaticAddrMapStatus.setStatus(_A)
_CnatConfDynAddrMapTable_Object=MibTable
cnatConfDynAddrMapTable=_CnatConfDynAddrMapTable_Object((1,3,6,1,4,1,9,10,77,1,1,3))
if mibBuilder.loadTexts:cnatConfDynAddrMapTable.setStatus(_A)
_CnatConfDynAddrMapEntry_Object=MibTableRow
cnatConfDynAddrMapEntry=_CnatConfDynAddrMapEntry_Object((1,3,6,1,4,1,9,10,77,1,1,3,1))
cnatConfDynAddrMapEntry.setIndexNames((0,_B,_O),(0,_B,_T))
if mibBuilder.loadTexts:cnatConfDynAddrMapEntry.setStatus(_A)
class _CnatConfDynAddrMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatConfDynAddrMapName_Type.__name__=_G
_CnatConfDynAddrMapName_Object=MibTableColumn
cnatConfDynAddrMapName=_CnatConfDynAddrMapName_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,1),_CnatConfDynAddrMapName_Type())
cnatConfDynAddrMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatConfDynAddrMapName.setStatus(_A)
class _CnatConfDynAddressMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('both',3)))
_CnatConfDynAddressMapType_Type.__name__=_E
_CnatConfDynAddressMapType_Object=MibTableColumn
cnatConfDynAddressMapType=_CnatConfDynAddressMapType_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,2),_CnatConfDynAddressMapType_Type())
cnatConfDynAddressMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynAddressMapType.setStatus(_A)
_CnatConfDynLocalAddrFrom_Type=IpAddress
_CnatConfDynLocalAddrFrom_Object=MibTableColumn
cnatConfDynLocalAddrFrom=_CnatConfDynLocalAddrFrom_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,3),_CnatConfDynLocalAddrFrom_Type())
cnatConfDynLocalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynLocalAddrFrom.setStatus(_A)
_CnatConfDynLocalAddrTo_Type=IpAddress
_CnatConfDynLocalAddrTo_Object=MibTableColumn
cnatConfDynLocalAddrTo=_CnatConfDynLocalAddrTo_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,4),_CnatConfDynLocalAddrTo_Type())
cnatConfDynLocalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynLocalAddrTo.setStatus(_A)
class _CnatConfDynLocalPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfDynLocalPortFrom_Type.__name__=_E
_CnatConfDynLocalPortFrom_Object=MibTableColumn
cnatConfDynLocalPortFrom=_CnatConfDynLocalPortFrom_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,5),_CnatConfDynLocalPortFrom_Type())
cnatConfDynLocalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynLocalPortFrom.setStatus(_A)
class _CnatConfDynLocalPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfDynLocalPortTo_Type.__name__=_E
_CnatConfDynLocalPortTo_Object=MibTableColumn
cnatConfDynLocalPortTo=_CnatConfDynLocalPortTo_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,6),_CnatConfDynLocalPortTo_Type())
cnatConfDynLocalPortTo.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatConfDynLocalPortTo.setStatus(_A)
_CnatConfDynGlobalAddrFrom_Type=IpAddress
_CnatConfDynGlobalAddrFrom_Object=MibTableColumn
cnatConfDynGlobalAddrFrom=_CnatConfDynGlobalAddrFrom_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,7),_CnatConfDynGlobalAddrFrom_Type())
cnatConfDynGlobalAddrFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynGlobalAddrFrom.setStatus(_A)
_CnatConfDynGlobalAddrTo_Type=IpAddress
_CnatConfDynGlobalAddrTo_Object=MibTableColumn
cnatConfDynGlobalAddrTo=_CnatConfDynGlobalAddrTo_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,8),_CnatConfDynGlobalAddrTo_Type())
cnatConfDynGlobalAddrTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynGlobalAddrTo.setStatus(_A)
class _CnatConfDynGlobalPortFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfDynGlobalPortFrom_Type.__name__=_E
_CnatConfDynGlobalPortFrom_Object=MibTableColumn
cnatConfDynGlobalPortFrom=_CnatConfDynGlobalPortFrom_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,9),_CnatConfDynGlobalPortFrom_Type())
cnatConfDynGlobalPortFrom.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynGlobalPortFrom.setStatus(_A)
class _CnatConfDynGlobalPortTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatConfDynGlobalPortTo_Type.__name__=_E
_CnatConfDynGlobalPortTo_Object=MibTableColumn
cnatConfDynGlobalPortTo=_CnatConfDynGlobalPortTo_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,10),_CnatConfDynGlobalPortTo_Type())
cnatConfDynGlobalPortTo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynGlobalPortTo.setStatus(_A)
class _CnatConfDynProtocol_Type(Bits):namedValues=NamedValues(*((_R,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_CnatConfDynProtocol_Type.__name__=_J
_CnatConfDynProtocol_Object=MibTableColumn
cnatConfDynProtocol=_CnatConfDynProtocol_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,11),_CnatConfDynProtocol_Type())
cnatConfDynProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynProtocol.setStatus(_A)
class _CnatConfDynAddrMapStorageType_Type(StorageType):defaultValue=3
_CnatConfDynAddrMapStorageType_Type.__name__=_I
_CnatConfDynAddrMapStorageType_Object=MibTableColumn
cnatConfDynAddrMapStorageType=_CnatConfDynAddrMapStorageType_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,12),_CnatConfDynAddrMapStorageType_Type())
cnatConfDynAddrMapStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynAddrMapStorageType.setStatus(_A)
_CnatConfDynAddrMapStatus_Type=RowStatus
_CnatConfDynAddrMapStatus_Object=MibTableColumn
cnatConfDynAddrMapStatus=_CnatConfDynAddrMapStatus_Object((1,3,6,1,4,1,9,10,77,1,1,3,1,13),_CnatConfDynAddrMapStatus_Type())
cnatConfDynAddrMapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatConfDynAddrMapStatus.setStatus(_A)
_CnatInterfaceTable_Object=MibTable
cnatInterfaceTable=_CnatInterfaceTable_Object((1,3,6,1,4,1,9,10,77,1,1,4))
if mibBuilder.loadTexts:cnatInterfaceTable.setStatus(_A)
_CnatInterfaceEntry_Object=MibTableRow
cnatInterfaceEntry=_CnatInterfaceEntry_Object((1,3,6,1,4,1,9,10,77,1,1,4,1))
cnatInterfaceEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:cnatInterfaceEntry.setStatus(_A)
_CnatInterfaceIndex_Type=InterfaceIndex
_CnatInterfaceIndex_Object=MibTableColumn
cnatInterfaceIndex=_CnatInterfaceIndex_Object((1,3,6,1,4,1,9,10,77,1,1,4,1,1),_CnatInterfaceIndex_Type())
cnatInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatInterfaceIndex.setStatus(_A)
class _CnatInterfaceRealm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('private',1),('public',2)))
_CnatInterfaceRealm_Type.__name__=_E
_CnatInterfaceRealm_Object=MibTableColumn
cnatInterfaceRealm=_CnatInterfaceRealm_Object((1,3,6,1,4,1,9,10,77,1,1,4,1,2),_CnatInterfaceRealm_Type())
cnatInterfaceRealm.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatInterfaceRealm.setStatus(_A)
class _CnatInterfaceStorageType_Type(StorageType):defaultValue=3
_CnatInterfaceStorageType_Type.__name__=_I
_CnatInterfaceStorageType_Object=MibTableColumn
cnatInterfaceStorageType=_CnatInterfaceStorageType_Object((1,3,6,1,4,1,9,10,77,1,1,4,1,3),_CnatInterfaceStorageType_Type())
cnatInterfaceStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatInterfaceStorageType.setStatus(_A)
_CnatInterfaceStatus_Type=RowStatus
_CnatInterfaceStatus_Object=MibTableColumn
cnatInterfaceStatus=_CnatInterfaceStatus_Object((1,3,6,1,4,1,9,10,77,1,1,4,1,4),_CnatInterfaceStatus_Type())
cnatInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cnatInterfaceStatus.setStatus(_A)
_CnatBind_ObjectIdentity=ObjectIdentity
cnatBind=_CnatBind_ObjectIdentity((1,3,6,1,4,1,9,10,77,1,2))
_CnatAddrBindNumberOfEntries_Type=Gauge32
_CnatAddrBindNumberOfEntries_Object=MibScalar
cnatAddrBindNumberOfEntries=_CnatAddrBindNumberOfEntries_Object((1,3,6,1,4,1,9,10,77,1,2,1),_CnatAddrBindNumberOfEntries_Type())
cnatAddrBindNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindNumberOfEntries.setStatus(_A)
_CnatAddrBindTable_Object=MibTable
cnatAddrBindTable=_CnatAddrBindTable_Object((1,3,6,1,4,1,9,10,77,1,2,2))
if mibBuilder.loadTexts:cnatAddrBindTable.setStatus(_A)
_CnatAddrBindEntry_Object=MibTableRow
cnatAddrBindEntry=_CnatAddrBindEntry_Object((1,3,6,1,4,1,9,10,77,1,2,2,1))
cnatAddrBindEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:cnatAddrBindEntry.setStatus(_A)
_CnatAddrBindLocalAddr_Type=IpAddress
_CnatAddrBindLocalAddr_Object=MibTableColumn
cnatAddrBindLocalAddr=_CnatAddrBindLocalAddr_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,1),_CnatAddrBindLocalAddr_Type())
cnatAddrBindLocalAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrBindLocalAddr.setStatus(_A)
_CnatAddrBindGlobalAddr_Type=IpAddress
_CnatAddrBindGlobalAddr_Object=MibTableColumn
cnatAddrBindGlobalAddr=_CnatAddrBindGlobalAddr_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,2),_CnatAddrBindGlobalAddr_Type())
cnatAddrBindGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindGlobalAddr.setStatus(_A)
_CnatAddrBindId_Type=Unsigned32
_CnatAddrBindId_Object=MibTableColumn
cnatAddrBindId=_CnatAddrBindId_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,3),_CnatAddrBindId_Type())
cnatAddrBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindId.setStatus(_A)
class _CnatAddrBindDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CnatAddrBindDirection_Type.__name__=_E
_CnatAddrBindDirection_Object=MibTableColumn
cnatAddrBindDirection=_CnatAddrBindDirection_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,4),_CnatAddrBindDirection_Type())
cnatAddrBindDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindDirection.setStatus(_A)
class _CnatAddrBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_CnatAddrBindType_Type.__name__=_E
_CnatAddrBindType_Object=MibTableColumn
cnatAddrBindType=_CnatAddrBindType_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,5),_CnatAddrBindType_Type())
cnatAddrBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindType.setStatus(_A)
class _CnatAddrBindConfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatAddrBindConfName_Type.__name__=_G
_CnatAddrBindConfName_Object=MibTableColumn
cnatAddrBindConfName=_CnatAddrBindConfName_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,6),_CnatAddrBindConfName_Type())
cnatAddrBindConfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindConfName.setStatus(_A)
_CnatAddrBindSessionCount_Type=Gauge32
_CnatAddrBindSessionCount_Object=MibTableColumn
cnatAddrBindSessionCount=_CnatAddrBindSessionCount_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,7),_CnatAddrBindSessionCount_Type())
cnatAddrBindSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindSessionCount.setStatus(_A)
_CnatAddrBindCurrentIdleTime_Type=TimeTicks
_CnatAddrBindCurrentIdleTime_Object=MibTableColumn
cnatAddrBindCurrentIdleTime=_CnatAddrBindCurrentIdleTime_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,8),_CnatAddrBindCurrentIdleTime_Type())
cnatAddrBindCurrentIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindCurrentIdleTime.setStatus(_A)
_CnatAddrBindInTranslate_Type=Counter32
_CnatAddrBindInTranslate_Object=MibTableColumn
cnatAddrBindInTranslate=_CnatAddrBindInTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,9),_CnatAddrBindInTranslate_Type())
cnatAddrBindInTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindInTranslate.setStatus(_A)
_CnatAddrBindOutTranslate_Type=Counter32
_CnatAddrBindOutTranslate_Object=MibTableColumn
cnatAddrBindOutTranslate=_CnatAddrBindOutTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,2,1,10),_CnatAddrBindOutTranslate_Type())
cnatAddrBindOutTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrBindOutTranslate.setStatus(_A)
_CnatAddrPortBindNumberOfEntries_Type=Gauge32
_CnatAddrPortBindNumberOfEntries_Object=MibScalar
cnatAddrPortBindNumberOfEntries=_CnatAddrPortBindNumberOfEntries_Object((1,3,6,1,4,1,9,10,77,1,2,3),_CnatAddrPortBindNumberOfEntries_Type())
cnatAddrPortBindNumberOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindNumberOfEntries.setStatus(_A)
_CnatAddrPortBindTable_Object=MibTable
cnatAddrPortBindTable=_CnatAddrPortBindTable_Object((1,3,6,1,4,1,9,10,77,1,2,4))
if mibBuilder.loadTexts:cnatAddrPortBindTable.setStatus(_A)
_CnatAddrPortBindEntry_Object=MibTableRow
cnatAddrPortBindEntry=_CnatAddrPortBindEntry_Object((1,3,6,1,4,1,9,10,77,1,2,4,1))
cnatAddrPortBindEntry.setIndexNames((0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:cnatAddrPortBindEntry.setStatus(_A)
_CnatAddrPortBindLocalAddr_Type=IpAddress
_CnatAddrPortBindLocalAddr_Object=MibTableColumn
cnatAddrPortBindLocalAddr=_CnatAddrPortBindLocalAddr_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,1),_CnatAddrPortBindLocalAddr_Type())
cnatAddrPortBindLocalAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrPortBindLocalAddr.setStatus(_A)
class _CnatAddrPortBindLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatAddrPortBindLocalPort_Type.__name__=_E
_CnatAddrPortBindLocalPort_Object=MibTableColumn
cnatAddrPortBindLocalPort=_CnatAddrPortBindLocalPort_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,2),_CnatAddrPortBindLocalPort_Type())
cnatAddrPortBindLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrPortBindLocalPort.setStatus(_A)
class _CnatAddrPortBindProtocol_Type(Bits):namedValues=NamedValues(*((_R,0),(_K,1),(_L,2),(_M,3),(_N,4)))
_CnatAddrPortBindProtocol_Type.__name__=_J
_CnatAddrPortBindProtocol_Object=MibTableColumn
cnatAddrPortBindProtocol=_CnatAddrPortBindProtocol_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,3),_CnatAddrPortBindProtocol_Type())
cnatAddrPortBindProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrPortBindProtocol.setStatus(_A)
_CnatAddrPortBindGlobalAddr_Type=IpAddress
_CnatAddrPortBindGlobalAddr_Object=MibTableColumn
cnatAddrPortBindGlobalAddr=_CnatAddrPortBindGlobalAddr_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,4),_CnatAddrPortBindGlobalAddr_Type())
cnatAddrPortBindGlobalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindGlobalAddr.setStatus(_A)
class _CnatAddrPortBindGlobalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatAddrPortBindGlobalPort_Type.__name__=_E
_CnatAddrPortBindGlobalPort_Object=MibTableColumn
cnatAddrPortBindGlobalPort=_CnatAddrPortBindGlobalPort_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,5),_CnatAddrPortBindGlobalPort_Type())
cnatAddrPortBindGlobalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindGlobalPort.setStatus(_A)
_CnatAddrPortBindId_Type=Unsigned32
_CnatAddrPortBindId_Object=MibTableColumn
cnatAddrPortBindId=_CnatAddrPortBindId_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,6),_CnatAddrPortBindId_Type())
cnatAddrPortBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindId.setStatus(_A)
class _CnatAddrPortBindDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_CnatAddrPortBindDirection_Type.__name__=_E
_CnatAddrPortBindDirection_Object=MibTableColumn
cnatAddrPortBindDirection=_CnatAddrPortBindDirection_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,7),_CnatAddrPortBindDirection_Type())
cnatAddrPortBindDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindDirection.setStatus(_A)
class _CnatAddrPortBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_CnatAddrPortBindType_Type.__name__=_E
_CnatAddrPortBindType_Object=MibTableColumn
cnatAddrPortBindType=_CnatAddrPortBindType_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,8),_CnatAddrPortBindType_Type())
cnatAddrPortBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindType.setStatus(_A)
_CnatAddrPortBindConfName_Type=SnmpAdminString
_CnatAddrPortBindConfName_Object=MibTableColumn
cnatAddrPortBindConfName=_CnatAddrPortBindConfName_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,9),_CnatAddrPortBindConfName_Type())
cnatAddrPortBindConfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindConfName.setStatus(_A)
_CnatAddrPortBindSessionCount_Type=Gauge32
_CnatAddrPortBindSessionCount_Object=MibTableColumn
cnatAddrPortBindSessionCount=_CnatAddrPortBindSessionCount_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,10),_CnatAddrPortBindSessionCount_Type())
cnatAddrPortBindSessionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindSessionCount.setStatus(_A)
_CnatAddrPortBindCurrentIdleTime_Type=TimeTicks
_CnatAddrPortBindCurrentIdleTime_Object=MibTableColumn
cnatAddrPortBindCurrentIdleTime=_CnatAddrPortBindCurrentIdleTime_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,11),_CnatAddrPortBindCurrentIdleTime_Type())
cnatAddrPortBindCurrentIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindCurrentIdleTime.setStatus(_A)
_CnatAddrPortBindInTranslate_Type=Counter32
_CnatAddrPortBindInTranslate_Object=MibTableColumn
cnatAddrPortBindInTranslate=_CnatAddrPortBindInTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,12),_CnatAddrPortBindInTranslate_Type())
cnatAddrPortBindInTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindInTranslate.setStatus(_A)
_CnatAddrPortBindOutTranslate_Type=Counter32
_CnatAddrPortBindOutTranslate_Object=MibTableColumn
cnatAddrPortBindOutTranslate=_CnatAddrPortBindOutTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,4,1,13),_CnatAddrPortBindOutTranslate_Type())
cnatAddrPortBindOutTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrPortBindOutTranslate.setStatus(_A)
_CnatSessionTable_Object=MibTable
cnatSessionTable=_CnatSessionTable_Object((1,3,6,1,4,1,9,10,77,1,2,5))
if mibBuilder.loadTexts:cnatSessionTable.setStatus(_A)
_CnatSessionEntry_Object=MibTableRow
cnatSessionEntry=_CnatSessionEntry_Object((1,3,6,1,4,1,9,10,77,1,2,5,1))
cnatSessionEntry.setIndexNames((0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:cnatSessionEntry.setStatus(_A)
_CnatSessionBindId_Type=Unsigned32
_CnatSessionBindId_Object=MibTableColumn
cnatSessionBindId=_CnatSessionBindId_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,1),_CnatSessionBindId_Type())
cnatSessionBindId.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatSessionBindId.setStatus(_A)
_CnatSessionId_Type=Unsigned32
_CnatSessionId_Object=MibTableColumn
cnatSessionId=_CnatSessionId_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,2),_CnatSessionId_Type())
cnatSessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatSessionId.setStatus(_A)
class _CnatSessionDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_CnatSessionDirection_Type.__name__=_E
_CnatSessionDirection_Object=MibTableColumn
cnatSessionDirection=_CnatSessionDirection_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,3),_CnatSessionDirection_Type())
cnatSessionDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionDirection.setStatus(_A)
_CnatSessionUpTime_Type=TimeTicks
_CnatSessionUpTime_Object=MibTableColumn
cnatSessionUpTime=_CnatSessionUpTime_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,4),_CnatSessionUpTime_Type())
cnatSessionUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionUpTime.setStatus(_A)
_CnatSessionProtocolType_Type=NATProtocolType
_CnatSessionProtocolType_Object=MibTableColumn
cnatSessionProtocolType=_CnatSessionProtocolType_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,5),_CnatSessionProtocolType_Type())
cnatSessionProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionProtocolType.setStatus(_A)
_CnatSessionOrigPrivateAddr_Type=IpAddress
_CnatSessionOrigPrivateAddr_Object=MibTableColumn
cnatSessionOrigPrivateAddr=_CnatSessionOrigPrivateAddr_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,6),_CnatSessionOrigPrivateAddr_Type())
cnatSessionOrigPrivateAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionOrigPrivateAddr.setStatus(_A)
_CnatSessionTransPrivateAddr_Type=IpAddress
_CnatSessionTransPrivateAddr_Object=MibTableColumn
cnatSessionTransPrivateAddr=_CnatSessionTransPrivateAddr_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,7),_CnatSessionTransPrivateAddr_Type())
cnatSessionTransPrivateAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionTransPrivateAddr.setStatus(_A)
class _CnatSessionOrigPrivatePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatSessionOrigPrivatePort_Type.__name__=_E
_CnatSessionOrigPrivatePort_Object=MibTableColumn
cnatSessionOrigPrivatePort=_CnatSessionOrigPrivatePort_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,8),_CnatSessionOrigPrivatePort_Type())
cnatSessionOrigPrivatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionOrigPrivatePort.setStatus(_A)
class _CnatSessionTransPrivatePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatSessionTransPrivatePort_Type.__name__=_E
_CnatSessionTransPrivatePort_Object=MibTableColumn
cnatSessionTransPrivatePort=_CnatSessionTransPrivatePort_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,9),_CnatSessionTransPrivatePort_Type())
cnatSessionTransPrivatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionTransPrivatePort.setStatus(_A)
_CnatSessionOrigPublicAddr_Type=IpAddress
_CnatSessionOrigPublicAddr_Object=MibTableColumn
cnatSessionOrigPublicAddr=_CnatSessionOrigPublicAddr_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,10),_CnatSessionOrigPublicAddr_Type())
cnatSessionOrigPublicAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionOrigPublicAddr.setStatus(_A)
_CnatSessionTransPublicAddr_Type=IpAddress
_CnatSessionTransPublicAddr_Object=MibTableColumn
cnatSessionTransPublicAddr=_CnatSessionTransPublicAddr_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,11),_CnatSessionTransPublicAddr_Type())
cnatSessionTransPublicAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionTransPublicAddr.setStatus(_A)
class _CnatSessionOrigPublicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatSessionOrigPublicPort_Type.__name__=_E
_CnatSessionOrigPublicPort_Object=MibTableColumn
cnatSessionOrigPublicPort=_CnatSessionOrigPublicPort_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,12),_CnatSessionOrigPublicPort_Type())
cnatSessionOrigPublicPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionOrigPublicPort.setStatus(_A)
class _CnatSessionTransPublicPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CnatSessionTransPublicPort_Type.__name__=_E
_CnatSessionTransPublicPort_Object=MibTableColumn
cnatSessionTransPublicPort=_CnatSessionTransPublicPort_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,13),_CnatSessionTransPublicPort_Type())
cnatSessionTransPublicPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionTransPublicPort.setStatus(_A)
_CnatSessionCurrentIdletime_Type=TimeTicks
_CnatSessionCurrentIdletime_Object=MibTableColumn
cnatSessionCurrentIdletime=_CnatSessionCurrentIdletime_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,14),_CnatSessionCurrentIdletime_Type())
cnatSessionCurrentIdletime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionCurrentIdletime.setStatus(_A)
_CnatSessionSecondBindId_Type=Unsigned32
_CnatSessionSecondBindId_Object=MibTableColumn
cnatSessionSecondBindId=_CnatSessionSecondBindId_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,15),_CnatSessionSecondBindId_Type())
cnatSessionSecondBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionSecondBindId.setStatus(_A)
_CnatSessionInTranslate_Type=Counter32
_CnatSessionInTranslate_Object=MibTableColumn
cnatSessionInTranslate=_CnatSessionInTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,16),_CnatSessionInTranslate_Type())
cnatSessionInTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionInTranslate.setStatus(_A)
_CnatSessionOutTranslate_Type=Counter32
_CnatSessionOutTranslate_Object=MibTableColumn
cnatSessionOutTranslate=_CnatSessionOutTranslate_Object((1,3,6,1,4,1,9,10,77,1,2,5,1,17),_CnatSessionOutTranslate_Type())
cnatSessionOutTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatSessionOutTranslate.setStatus(_A)
_CnatStatistics_ObjectIdentity=ObjectIdentity
cnatStatistics=_CnatStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,77,1,3))
_CnatProtocolStatsTable_Object=MibTable
cnatProtocolStatsTable=_CnatProtocolStatsTable_Object((1,3,6,1,4,1,9,10,77,1,3,1))
if mibBuilder.loadTexts:cnatProtocolStatsTable.setStatus(_A)
_CnatProtocolStatsEntry_Object=MibTableRow
cnatProtocolStatsEntry=_CnatProtocolStatsEntry_Object((1,3,6,1,4,1,9,10,77,1,3,1,1))
cnatProtocolStatsEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:cnatProtocolStatsEntry.setStatus(_A)
_CnatProtocolStatsName_Type=NATProtocolType
_CnatProtocolStatsName_Object=MibTableColumn
cnatProtocolStatsName=_CnatProtocolStatsName_Object((1,3,6,1,4,1,9,10,77,1,3,1,1,1),_CnatProtocolStatsName_Type())
cnatProtocolStatsName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatProtocolStatsName.setStatus(_A)
_CnatProtocolStatsInTranslate_Type=Counter32
_CnatProtocolStatsInTranslate_Object=MibTableColumn
cnatProtocolStatsInTranslate=_CnatProtocolStatsInTranslate_Object((1,3,6,1,4,1,9,10,77,1,3,1,1,2),_CnatProtocolStatsInTranslate_Type())
cnatProtocolStatsInTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatProtocolStatsInTranslate.setStatus(_A)
_CnatProtocolStatsOutTranslate_Type=Counter32
_CnatProtocolStatsOutTranslate_Object=MibTableColumn
cnatProtocolStatsOutTranslate=_CnatProtocolStatsOutTranslate_Object((1,3,6,1,4,1,9,10,77,1,3,1,1,3),_CnatProtocolStatsOutTranslate_Type())
cnatProtocolStatsOutTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatProtocolStatsOutTranslate.setStatus(_A)
_CnatProtocolStatsRejectCount_Type=Counter32
_CnatProtocolStatsRejectCount_Object=MibTableColumn
cnatProtocolStatsRejectCount=_CnatProtocolStatsRejectCount_Object((1,3,6,1,4,1,9,10,77,1,3,1,1,4),_CnatProtocolStatsRejectCount_Type())
cnatProtocolStatsRejectCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatProtocolStatsRejectCount.setStatus(_A)
_CnatAddrMapStatsTable_Object=MibTable
cnatAddrMapStatsTable=_CnatAddrMapStatsTable_Object((1,3,6,1,4,1,9,10,77,1,3,2))
if mibBuilder.loadTexts:cnatAddrMapStatsTable.setStatus(_A)
_CnatAddrMapStatsEntry_Object=MibTableRow
cnatAddrMapStatsEntry=_CnatAddrMapStatsEntry_Object((1,3,6,1,4,1,9,10,77,1,3,2,1))
cnatAddrMapStatsEntry.setIndexNames((0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:cnatAddrMapStatsEntry.setStatus(_A)
class _CnatAddrMapStatsConfName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatAddrMapStatsConfName_Type.__name__=_G
_CnatAddrMapStatsConfName_Object=MibTableColumn
cnatAddrMapStatsConfName=_CnatAddrMapStatsConfName_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,1),_CnatAddrMapStatsConfName_Type())
cnatAddrMapStatsConfName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrMapStatsConfName.setStatus(_A)
class _CnatAddrMapStatsMapName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CnatAddrMapStatsMapName_Type.__name__=_G
_CnatAddrMapStatsMapName_Object=MibTableColumn
cnatAddrMapStatsMapName=_CnatAddrMapStatsMapName_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,2),_CnatAddrMapStatsMapName_Type())
cnatAddrMapStatsMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:cnatAddrMapStatsMapName.setStatus(_A)
_CnatAddrMapStatsInTranslate_Type=Counter32
_CnatAddrMapStatsInTranslate_Object=MibTableColumn
cnatAddrMapStatsInTranslate=_CnatAddrMapStatsInTranslate_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,3),_CnatAddrMapStatsInTranslate_Type())
cnatAddrMapStatsInTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrMapStatsInTranslate.setStatus(_A)
_CnatAddrMapStatsOutTranslate_Type=Counter32
_CnatAddrMapStatsOutTranslate_Object=MibTableColumn
cnatAddrMapStatsOutTranslate=_CnatAddrMapStatsOutTranslate_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,4),_CnatAddrMapStatsOutTranslate_Type())
cnatAddrMapStatsOutTranslate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrMapStatsOutTranslate.setStatus(_A)
_CnatAddrMapStatsNoResource_Type=Counter32
_CnatAddrMapStatsNoResource_Object=MibTableColumn
cnatAddrMapStatsNoResource=_CnatAddrMapStatsNoResource_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,5),_CnatAddrMapStatsNoResource_Type())
cnatAddrMapStatsNoResource.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrMapStatsNoResource.setStatus(_A)
_CnatAddrMapStatsAddrUsed_Type=Gauge32
_CnatAddrMapStatsAddrUsed_Object=MibTableColumn
cnatAddrMapStatsAddrUsed=_CnatAddrMapStatsAddrUsed_Object((1,3,6,1,4,1,9,10,77,1,3,2,1,6),_CnatAddrMapStatsAddrUsed_Type())
cnatAddrMapStatsAddrUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatAddrMapStatsAddrUsed.setStatus(_A)
_CnatInterfaceStatsTable_Object=MibTable
cnatInterfaceStatsTable=_CnatInterfaceStatsTable_Object((1,3,6,1,4,1,9,10,77,1,3,3))
if mibBuilder.loadTexts:cnatInterfaceStatsTable.setStatus(_A)
_CnatInterfaceStatsEntry_Object=MibTableRow
cnatInterfaceStatsEntry=_CnatInterfaceStatsEntry_Object((1,3,6,1,4,1,9,10,77,1,3,3,1))
if mibBuilder.loadTexts:cnatInterfaceStatsEntry.setStatus(_A)
_CnatInterfacePktsIn_Type=Counter32
_CnatInterfacePktsIn_Object=MibTableColumn
cnatInterfacePktsIn=_CnatInterfacePktsIn_Object((1,3,6,1,4,1,9,10,77,1,3,3,1,1),_CnatInterfacePktsIn_Type())
cnatInterfacePktsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatInterfacePktsIn.setStatus(_A)
_CnatInterfacePktsOut_Type=Counter32
_CnatInterfacePktsOut_Object=MibTableColumn
cnatInterfacePktsOut=_CnatInterfacePktsOut_Object((1,3,6,1,4,1,9,10,77,1,3,3,1,2),_CnatInterfacePktsOut_Type())
cnatInterfacePktsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cnatInterfacePktsOut.setStatus(_A)
_CiscoNatMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoNatMIBNotificationPrefix=_CiscoNatMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,77,2))
_CiscoNatMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoNatMIBNotifications=_CiscoNatMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,77,2,0))
_CiscoNatMIBConformance_ObjectIdentity=ObjectIdentity
ciscoNatMIBConformance=_CiscoNatMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,77,3))
_CiscoNatMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoNatMIBCompliances=_CiscoNatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,77,3,1))
_CiscoNatMIBGroups_ObjectIdentity=ObjectIdentity
ciscoNatMIBGroups=_CiscoNatMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,77,3,2))
cnatInterfaceEntry.registerAugmentions((_B,_i))
cnatInterfaceStatsEntry.setIndexNames(*cnatInterfaceEntry.getIndexNames())
cnatConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,77,3,2,1))
cnatConfigGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cnatConfigGroup.setStatus(_A)
cnatBindGroup=ObjectGroup((1,3,6,1,4,1,9,10,77,3,2,2))
cnatBindGroup.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:cnatBindGroup.setStatus(_A)
cnatStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,77,3,2,3))
cnatStatsGroup.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:cnatStatsGroup.setStatus(_A)
ciscoNatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,77,3,1,1))
ciscoNatMIBCompliance.setObjects(*((_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:ciscoNatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NATProtocolType':NATProtocolType,'ciscoIetfNatMIB':ciscoIetfNatMIB,'ciscoNatMIBObjects':ciscoNatMIBObjects,'cnatConfig':cnatConfig,'cnatConfTable':cnatConfTable,'cnatConfEntry':cnatConfEntry,_O:cnatConfName,_j:cnatConfServiceType,_k:cnatConfTimeoutIcmpIdle,_l:cnatConfTimeoutUdpIdle,_m:cnatConfTimeoutTcpIdle,_n:cnatConfTimeoutTcpNeg,_o:cnatConfTimeoutOther,_p:cnatConfMaxBindLeaseTime,_q:cnatConfMaxBindIdleTime,_r:cnatConfStorageType,_s:cnatConfStatus,'cnatConfStaticAddrMapTable':cnatConfStaticAddrMapTable,'cnatConfStaticAddrMapEntry':cnatConfStaticAddrMapEntry,_S:cnatConfStaticAddrMapName,_t:cnatConfStaticAddrMapType,_u:cnatConfStaticLocalAddrFrom,_v:cnatConfStaticLocalAddrTo,_w:cnatConfStaticLocalPortFrom,_x:cnatConfStaticLocalPortTo,_y:cnatConfStaticGlobalAddrFrom,_z:cnatConfStaticGlobalAddrTo,_A0:cnatConfStaticGlobalPortFrom,_A1:cnatConfStaticGlobalPortTo,_A2:cnatConfStaticProtocol,_A3:cnatConfStaticAddrMapStorageType,_A4:cnatConfStaticAddrMapStatus,'cnatConfDynAddrMapTable':cnatConfDynAddrMapTable,'cnatConfDynAddrMapEntry':cnatConfDynAddrMapEntry,_T:cnatConfDynAddrMapName,_A5:cnatConfDynAddressMapType,_A6:cnatConfDynLocalAddrFrom,_A7:cnatConfDynLocalAddrTo,_A8:cnatConfDynLocalPortFrom,_A9:cnatConfDynLocalPortTo,_AA:cnatConfDynGlobalAddrFrom,_AB:cnatConfDynGlobalAddrTo,_AC:cnatConfDynGlobalPortFrom,_AD:cnatConfDynGlobalPortTo,_AE:cnatConfDynProtocol,_AF:cnatConfDynAddrMapStorageType,_AG:cnatConfDynAddrMapStatus,'cnatInterfaceTable':cnatInterfaceTable,'cnatInterfaceEntry':cnatInterfaceEntry,_U:cnatInterfaceIndex,_AH:cnatInterfaceRealm,_AI:cnatInterfaceStorageType,_AJ:cnatInterfaceStatus,'cnatBind':cnatBind,_AK:cnatAddrBindNumberOfEntries,'cnatAddrBindTable':cnatAddrBindTable,'cnatAddrBindEntry':cnatAddrBindEntry,_V:cnatAddrBindLocalAddr,_AL:cnatAddrBindGlobalAddr,_AM:cnatAddrBindId,_AN:cnatAddrBindDirection,_AO:cnatAddrBindType,_AP:cnatAddrBindConfName,_AQ:cnatAddrBindSessionCount,_AR:cnatAddrBindCurrentIdleTime,_AS:cnatAddrBindInTranslate,_AT:cnatAddrBindOutTranslate,_AU:cnatAddrPortBindNumberOfEntries,'cnatAddrPortBindTable':cnatAddrPortBindTable,'cnatAddrPortBindEntry':cnatAddrPortBindEntry,_a:cnatAddrPortBindLocalAddr,_b:cnatAddrPortBindLocalPort,_c:cnatAddrPortBindProtocol,_AV:cnatAddrPortBindGlobalAddr,_AW:cnatAddrPortBindGlobalPort,_AX:cnatAddrPortBindId,_AY:cnatAddrPortBindDirection,_AZ:cnatAddrPortBindType,_Aa:cnatAddrPortBindConfName,_Ab:cnatAddrPortBindSessionCount,_Ac:cnatAddrPortBindCurrentIdleTime,_Ad:cnatAddrPortBindInTranslate,_Ae:cnatAddrPortBindOutTranslate,'cnatSessionTable':cnatSessionTable,'cnatSessionEntry':cnatSessionEntry,_d:cnatSessionBindId,_e:cnatSessionId,_Af:cnatSessionDirection,_Ag:cnatSessionUpTime,_Ah:cnatSessionProtocolType,_Ai:cnatSessionOrigPrivateAddr,_Aj:cnatSessionTransPrivateAddr,_Ak:cnatSessionOrigPrivatePort,_Al:cnatSessionTransPrivatePort,_Am:cnatSessionOrigPublicAddr,_An:cnatSessionTransPublicAddr,_Ao:cnatSessionOrigPublicPort,_Ap:cnatSessionTransPublicPort,_Aq:cnatSessionCurrentIdletime,_Ar:cnatSessionSecondBindId,_As:cnatSessionInTranslate,_At:cnatSessionOutTranslate,'cnatStatistics':cnatStatistics,'cnatProtocolStatsTable':cnatProtocolStatsTable,'cnatProtocolStatsEntry':cnatProtocolStatsEntry,_f:cnatProtocolStatsName,_Au:cnatProtocolStatsInTranslate,_Av:cnatProtocolStatsOutTranslate,_Aw:cnatProtocolStatsRejectCount,'cnatAddrMapStatsTable':cnatAddrMapStatsTable,'cnatAddrMapStatsEntry':cnatAddrMapStatsEntry,_g:cnatAddrMapStatsConfName,_h:cnatAddrMapStatsMapName,_Ax:cnatAddrMapStatsInTranslate,_Ay:cnatAddrMapStatsOutTranslate,_Az:cnatAddrMapStatsNoResource,_A_:cnatAddrMapStatsAddrUsed,'cnatInterfaceStatsTable':cnatInterfaceStatsTable,_i:cnatInterfaceStatsEntry,_B0:cnatInterfacePktsIn,_B1:cnatInterfacePktsOut,'ciscoNatMIBNotificationPrefix':ciscoNatMIBNotificationPrefix,'ciscoNatMIBNotifications':ciscoNatMIBNotifications,'ciscoNatMIBConformance':ciscoNatMIBConformance,'ciscoNatMIBCompliances':ciscoNatMIBCompliances,'ciscoNatMIBCompliance':ciscoNatMIBCompliance,'ciscoNatMIBGroups':ciscoNatMIBGroups,_B2:cnatConfigGroup,_B3:cnatBindGroup,'cnatStatsGroup':cnatStatsGroup})