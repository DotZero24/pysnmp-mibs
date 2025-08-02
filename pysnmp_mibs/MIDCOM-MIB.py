_AV='midcomResourceGroup'
_AU='midcomConfigFirewallGroup'
_AT='midcomStatisticsGroup'
_AS='midcomCapabilitiesGroup'
_AR='midcomNotificationsGroup'
_AQ='midcomRuleGroup'
_AP='midcomSolicitedGroupEvent'
_AO='midcomSolicitedRuleEvent'
_AN='midcomUnsolicitedRuleEvent'
_AM='midcomTotalTerminatedEnableRules'
_AL='midcomTotalTerminatedOnRqEnableRules'
_AK='midcomTotalExpiredEnableRules'
_AJ='midcomCurrentActiveEnableRules'
_AI='midcomTotalRejectedEnableRules'
_AH='midcomTotalIncorrectEnableRules'
_AG='midcomTotalTerminatedReserveRules'
_AF='midcomTotalTerminatedOnRqReserveRules'
_AE='midcomTotalExpiredReserveRules'
_AD='midcomCurrentActiveReserveRules'
_AC='midcomTotalRejectedReserveRules'
_AB='midcomTotalIncorrectReserveRules'
_AA='midcomCurrentRulesIncomplete'
_A9='midcomTotalRejectedRuleEntries'
_A8='midcomCurrentOwners'
_A7='midcomRscFirewallRuleId'
_A6='midcomRscNatSessionId2'
_A5='midcomRscNatSessionId1'
_A4='midcomRscNatInsideAddrBindId'
_A3='midcomRscNatInsideAddrBindMode'
_A2='midcomRscNatInternalAddrBindId'
_A1='midcomRscNatInternalAddrBindMode'
_A0='midcomConfigFirewallPriority'
_z='midcomConfigFirewallGroupId'
_y='midcomConfigIfEnabled'
_x='midcomConfigIfBits'
_w='midcomConfigPersistentRules'
_v='midcomConfigMaxLifetime'
_u='midcomRuleRowStatus'
_t='midcomRuleOutsidePort'
_s='midcomRuleOutsideIpAddr'
_r='midcomRuleInsidePort'
_q='midcomRuleInsideIpAddr'
_p='midcomRuleExternalPort'
_o='midcomRuleExternalIpPrefixLength'
_n='midcomRuleExternalIpAddr'
_m='midcomRuleInternalPort'
_l='midcomRuleInternalIpPrefixLength'
_k='midcomRuleInternalIpAddr'
_j='midcomRuleExternalIpVersion'
_i='midcomRuleInternalIpVersion'
_h='midcomRulePortRange'
_g='midcomRuleTransportProtocol'
_f='midcomRuleMaxIdleTime'
_e='midcomRuleFlowDirection'
_d='midcomRuleInterface'
_c='midcomRuleError'
_b='midcomRuleStorageTime'
_a='midcomRuleStorageType'
_Z='midcomRuleAdminStatus'
_Y='midcomResourceEntry'
_X='midcomConfigFirewallIndex'
_W='midcomConfigIfIndex'
_V='midcomRuleIndex'
_U='TruthValue'
_T='StorageType'
_S='InterfaceIndexOrZero'
_R='midcomGroupLifetime'
_Q='midcomGroupIndex'
_P='midcomRuleOwner'
_O='SnmpAdminString'
_N='InetPortNumber'
_M='InetAddressType'
_L='InetAddressPrefixLength'
_K='midcomRuleLifetime'
_J='midcomRuleOperStatus'
_I='seconds'
_H='not-accessible'
_G='Integer32'
_F='read-write'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='MIDCOM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_S)
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L,_M,_N)
NatBindIdOrZero,=mibBuilder.importSymbols('NAT-MIB','NatBindIdOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_T,'TextualConvention',_U)
midcomMIB=ModuleIdentity((1,3,6,1,2,1,171))
if mibBuilder.loadTexts:midcomMIB.setRevisions(('2007-08-09 10:11',))
class MidcomNatBindMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('addressBind',1),('addressPortBind',2),('none',3)))
class MidcomNatSessionIdOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d'
_MidcomNotifications_ObjectIdentity=ObjectIdentity
midcomNotifications=_MidcomNotifications_ObjectIdentity((1,3,6,1,2,1,171,0))
_MidcomObjects_ObjectIdentity=ObjectIdentity
midcomObjects=_MidcomObjects_ObjectIdentity((1,3,6,1,2,1,171,1))
_MidcomTransaction_ObjectIdentity=ObjectIdentity
midcomTransaction=_MidcomTransaction_ObjectIdentity((1,3,6,1,2,1,171,1,1))
_MidcomRuleTable_Object=MibTable
midcomRuleTable=_MidcomRuleTable_Object((1,3,6,1,2,1,171,1,1,3))
if mibBuilder.loadTexts:midcomRuleTable.setStatus(_A)
_MidcomRuleEntry_Object=MibTableRow
midcomRuleEntry=_MidcomRuleEntry_Object((1,3,6,1,2,1,171,1,1,3,1))
midcomRuleEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_V))
if mibBuilder.loadTexts:midcomRuleEntry.setStatus(_A)
class _MidcomRuleOwner_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MidcomRuleOwner_Type.__name__=_O
_MidcomRuleOwner_Object=MibTableColumn
midcomRuleOwner=_MidcomRuleOwner_Object((1,3,6,1,2,1,171,1,1,3,1,1),_MidcomRuleOwner_Type())
midcomRuleOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:midcomRuleOwner.setStatus(_A)
class _MidcomRuleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MidcomRuleIndex_Type.__name__=_E
_MidcomRuleIndex_Object=MibTableColumn
midcomRuleIndex=_MidcomRuleIndex_Object((1,3,6,1,2,1,171,1,1,3,1,3),_MidcomRuleIndex_Type())
midcomRuleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:midcomRuleIndex.setStatus(_A)
class _MidcomRuleAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('reserve',1),('enable',2),('notSet',3)))
_MidcomRuleAdminStatus_Type.__name__=_G
_MidcomRuleAdminStatus_Object=MibTableColumn
midcomRuleAdminStatus=_MidcomRuleAdminStatus_Object((1,3,6,1,2,1,171,1,1,3,1,4),_MidcomRuleAdminStatus_Type())
midcomRuleAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleAdminStatus.setStatus(_A)
class _MidcomRuleOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('newEntry',1),('setting',2),('checkingRequest',3),('incorrectRequest',4),('processingRequest',5),('requestRejected',6),('reserved',7),('enabled',8),('timedOut',9),('terminatedOnRequest',10),('terminated',11),('genericError',12)))
_MidcomRuleOperStatus_Type.__name__=_G
_MidcomRuleOperStatus_Object=MibTableColumn
midcomRuleOperStatus=_MidcomRuleOperStatus_Object((1,3,6,1,2,1,171,1,1,3,1,5),_MidcomRuleOperStatus_Type())
midcomRuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleOperStatus.setStatus(_A)
class _MidcomRuleStorageType_Type(StorageType):defaultValue=2
_MidcomRuleStorageType_Type.__name__=_T
_MidcomRuleStorageType_Object=MibTableColumn
midcomRuleStorageType=_MidcomRuleStorageType_Object((1,3,6,1,2,1,171,1,1,3,1,6),_MidcomRuleStorageType_Type())
midcomRuleStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleStorageType.setStatus(_A)
class _MidcomRuleStorageTime_Type(Unsigned32):defaultValue=0
_MidcomRuleStorageTime_Type.__name__=_E
_MidcomRuleStorageTime_Object=MibTableColumn
midcomRuleStorageTime=_MidcomRuleStorageTime_Object((1,3,6,1,2,1,171,1,1,3,1,7),_MidcomRuleStorageTime_Type())
midcomRuleStorageTime.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleStorageTime.setStatus(_A)
if mibBuilder.loadTexts:midcomRuleStorageTime.setUnits(_I)
class _MidcomRuleError_Type(SnmpAdminString):defaultHexValue=''
_MidcomRuleError_Type.__name__=_O
_MidcomRuleError_Object=MibTableColumn
midcomRuleError=_MidcomRuleError_Object((1,3,6,1,2,1,171,1,1,3,1,8),_MidcomRuleError_Type())
midcomRuleError.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleError.setStatus(_A)
class _MidcomRuleInterface_Type(InterfaceIndexOrZero):defaultValue=0
_MidcomRuleInterface_Type.__name__=_S
_MidcomRuleInterface_Object=MibTableColumn
midcomRuleInterface=_MidcomRuleInterface_Object((1,3,6,1,2,1,171,1,1,3,1,9),_MidcomRuleInterface_Type())
midcomRuleInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleInterface.setStatus(_A)
class _MidcomRuleFlowDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('biDirectional',3)))
_MidcomRuleFlowDirection_Type.__name__=_G
_MidcomRuleFlowDirection_Object=MibTableColumn
midcomRuleFlowDirection=_MidcomRuleFlowDirection_Object((1,3,6,1,2,1,171,1,1,3,1,10),_MidcomRuleFlowDirection_Type())
midcomRuleFlowDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleFlowDirection.setStatus(_A)
class _MidcomRuleMaxIdleTime_Type(Unsigned32):defaultValue=0
_MidcomRuleMaxIdleTime_Type.__name__=_E
_MidcomRuleMaxIdleTime_Object=MibTableColumn
midcomRuleMaxIdleTime=_MidcomRuleMaxIdleTime_Object((1,3,6,1,2,1,171,1,1,3,1,11),_MidcomRuleMaxIdleTime_Type())
midcomRuleMaxIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleMaxIdleTime.setStatus(_A)
if mibBuilder.loadTexts:midcomRuleMaxIdleTime.setUnits(_I)
class _MidcomRuleTransportProtocol_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MidcomRuleTransportProtocol_Type.__name__=_E
_MidcomRuleTransportProtocol_Object=MibTableColumn
midcomRuleTransportProtocol=_MidcomRuleTransportProtocol_Object((1,3,6,1,2,1,171,1,1,3,1,12),_MidcomRuleTransportProtocol_Type())
midcomRuleTransportProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleTransportProtocol.setStatus(_A)
class _MidcomRulePortRange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single',1),('pair',2)))
_MidcomRulePortRange_Type.__name__=_G
_MidcomRulePortRange_Object=MibTableColumn
midcomRulePortRange=_MidcomRulePortRange_Object((1,3,6,1,2,1,171,1,1,3,1,13),_MidcomRulePortRange_Type())
midcomRulePortRange.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRulePortRange.setStatus(_A)
class _MidcomRuleInternalIpVersion_Type(InetAddressType):defaultValue=1
_MidcomRuleInternalIpVersion_Type.__name__=_M
_MidcomRuleInternalIpVersion_Object=MibTableColumn
midcomRuleInternalIpVersion=_MidcomRuleInternalIpVersion_Object((1,3,6,1,2,1,171,1,1,3,1,14),_MidcomRuleInternalIpVersion_Type())
midcomRuleInternalIpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleInternalIpVersion.setStatus(_A)
class _MidcomRuleExternalIpVersion_Type(InetAddressType):defaultValue=1
_MidcomRuleExternalIpVersion_Type.__name__=_M
_MidcomRuleExternalIpVersion_Object=MibTableColumn
midcomRuleExternalIpVersion=_MidcomRuleExternalIpVersion_Object((1,3,6,1,2,1,171,1,1,3,1,15),_MidcomRuleExternalIpVersion_Type())
midcomRuleExternalIpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleExternalIpVersion.setStatus(_A)
_MidcomRuleInternalIpAddr_Type=InetAddress
_MidcomRuleInternalIpAddr_Object=MibTableColumn
midcomRuleInternalIpAddr=_MidcomRuleInternalIpAddr_Object((1,3,6,1,2,1,171,1,1,3,1,16),_MidcomRuleInternalIpAddr_Type())
midcomRuleInternalIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleInternalIpAddr.setStatus(_A)
class _MidcomRuleInternalIpPrefixLength_Type(InetAddressPrefixLength):defaultValue=128
_MidcomRuleInternalIpPrefixLength_Type.__name__=_L
_MidcomRuleInternalIpPrefixLength_Object=MibTableColumn
midcomRuleInternalIpPrefixLength=_MidcomRuleInternalIpPrefixLength_Object((1,3,6,1,2,1,171,1,1,3,1,17),_MidcomRuleInternalIpPrefixLength_Type())
midcomRuleInternalIpPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleInternalIpPrefixLength.setStatus(_A)
class _MidcomRuleInternalPort_Type(InetPortNumber):defaultValue=0
_MidcomRuleInternalPort_Type.__name__=_N
_MidcomRuleInternalPort_Object=MibTableColumn
midcomRuleInternalPort=_MidcomRuleInternalPort_Object((1,3,6,1,2,1,171,1,1,3,1,18),_MidcomRuleInternalPort_Type())
midcomRuleInternalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleInternalPort.setStatus(_A)
_MidcomRuleExternalIpAddr_Type=InetAddress
_MidcomRuleExternalIpAddr_Object=MibTableColumn
midcomRuleExternalIpAddr=_MidcomRuleExternalIpAddr_Object((1,3,6,1,2,1,171,1,1,3,1,19),_MidcomRuleExternalIpAddr_Type())
midcomRuleExternalIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleExternalIpAddr.setStatus(_A)
class _MidcomRuleExternalIpPrefixLength_Type(InetAddressPrefixLength):defaultValue=128
_MidcomRuleExternalIpPrefixLength_Type.__name__=_L
_MidcomRuleExternalIpPrefixLength_Object=MibTableColumn
midcomRuleExternalIpPrefixLength=_MidcomRuleExternalIpPrefixLength_Object((1,3,6,1,2,1,171,1,1,3,1,20),_MidcomRuleExternalIpPrefixLength_Type())
midcomRuleExternalIpPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleExternalIpPrefixLength.setStatus(_A)
class _MidcomRuleExternalPort_Type(InetPortNumber):defaultValue=0
_MidcomRuleExternalPort_Type.__name__=_N
_MidcomRuleExternalPort_Object=MibTableColumn
midcomRuleExternalPort=_MidcomRuleExternalPort_Object((1,3,6,1,2,1,171,1,1,3,1,21),_MidcomRuleExternalPort_Type())
midcomRuleExternalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleExternalPort.setStatus(_A)
_MidcomRuleInsideIpAddr_Type=InetAddress
_MidcomRuleInsideIpAddr_Object=MibTableColumn
midcomRuleInsideIpAddr=_MidcomRuleInsideIpAddr_Object((1,3,6,1,2,1,171,1,1,3,1,22),_MidcomRuleInsideIpAddr_Type())
midcomRuleInsideIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleInsideIpAddr.setStatus(_A)
_MidcomRuleInsidePort_Type=InetPortNumber
_MidcomRuleInsidePort_Object=MibTableColumn
midcomRuleInsidePort=_MidcomRuleInsidePort_Object((1,3,6,1,2,1,171,1,1,3,1,23),_MidcomRuleInsidePort_Type())
midcomRuleInsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleInsidePort.setStatus(_A)
_MidcomRuleOutsideIpAddr_Type=InetAddress
_MidcomRuleOutsideIpAddr_Object=MibTableColumn
midcomRuleOutsideIpAddr=_MidcomRuleOutsideIpAddr_Object((1,3,6,1,2,1,171,1,1,3,1,24),_MidcomRuleOutsideIpAddr_Type())
midcomRuleOutsideIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleOutsideIpAddr.setStatus(_A)
_MidcomRuleOutsidePort_Type=InetPortNumber
_MidcomRuleOutsidePort_Object=MibTableColumn
midcomRuleOutsidePort=_MidcomRuleOutsidePort_Object((1,3,6,1,2,1,171,1,1,3,1,25),_MidcomRuleOutsidePort_Type())
midcomRuleOutsidePort.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRuleOutsidePort.setStatus(_A)
class _MidcomRuleLifetime_Type(Unsigned32):defaultValue=180
_MidcomRuleLifetime_Type.__name__=_E
_MidcomRuleLifetime_Object=MibTableColumn
midcomRuleLifetime=_MidcomRuleLifetime_Object((1,3,6,1,2,1,171,1,1,3,1,26),_MidcomRuleLifetime_Type())
midcomRuleLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleLifetime.setStatus(_A)
if mibBuilder.loadTexts:midcomRuleLifetime.setUnits(_I)
_MidcomRuleRowStatus_Type=RowStatus
_MidcomRuleRowStatus_Object=MibTableColumn
midcomRuleRowStatus=_MidcomRuleRowStatus_Object((1,3,6,1,2,1,171,1,1,3,1,27),_MidcomRuleRowStatus_Type())
midcomRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:midcomRuleRowStatus.setStatus(_A)
_MidcomGroupTable_Object=MibTable
midcomGroupTable=_MidcomGroupTable_Object((1,3,6,1,2,1,171,1,1,4))
if mibBuilder.loadTexts:midcomGroupTable.setStatus(_A)
_MidcomGroupEntry_Object=MibTableRow
midcomGroupEntry=_MidcomGroupEntry_Object((1,3,6,1,2,1,171,1,1,4,1))
midcomGroupEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:midcomGroupEntry.setStatus(_A)
class _MidcomGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MidcomGroupIndex_Type.__name__=_E
_MidcomGroupIndex_Object=MibTableColumn
midcomGroupIndex=_MidcomGroupIndex_Object((1,3,6,1,2,1,171,1,1,4,1,2),_MidcomGroupIndex_Type())
midcomGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:midcomGroupIndex.setStatus(_A)
_MidcomGroupLifetime_Type=Unsigned32
_MidcomGroupLifetime_Object=MibTableColumn
midcomGroupLifetime=_MidcomGroupLifetime_Object((1,3,6,1,2,1,171,1,1,4,1,3),_MidcomGroupLifetime_Type())
midcomGroupLifetime.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomGroupLifetime.setStatus(_A)
if mibBuilder.loadTexts:midcomGroupLifetime.setUnits(_I)
_MidcomConfig_ObjectIdentity=ObjectIdentity
midcomConfig=_MidcomConfig_ObjectIdentity((1,3,6,1,2,1,171,1,2))
_MidcomConfigMaxLifetime_Type=Unsigned32
_MidcomConfigMaxLifetime_Object=MibScalar
midcomConfigMaxLifetime=_MidcomConfigMaxLifetime_Object((1,3,6,1,2,1,171,1,2,1),_MidcomConfigMaxLifetime_Type())
midcomConfigMaxLifetime.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomConfigMaxLifetime.setStatus(_A)
if mibBuilder.loadTexts:midcomConfigMaxLifetime.setUnits(_I)
_MidcomConfigPersistentRules_Type=TruthValue
_MidcomConfigPersistentRules_Object=MibScalar
midcomConfigPersistentRules=_MidcomConfigPersistentRules_Object((1,3,6,1,2,1,171,1,2,2),_MidcomConfigPersistentRules_Type())
midcomConfigPersistentRules.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomConfigPersistentRules.setStatus(_A)
_MidcomConfigIfTable_Object=MibTable
midcomConfigIfTable=_MidcomConfigIfTable_Object((1,3,6,1,2,1,171,1,2,3))
if mibBuilder.loadTexts:midcomConfigIfTable.setStatus(_A)
_MidcomConfigIfEntry_Object=MibTableRow
midcomConfigIfEntry=_MidcomConfigIfEntry_Object((1,3,6,1,2,1,171,1,2,3,1))
midcomConfigIfEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:midcomConfigIfEntry.setStatus(_A)
_MidcomConfigIfIndex_Type=InterfaceIndexOrZero
_MidcomConfigIfIndex_Object=MibTableColumn
midcomConfigIfIndex=_MidcomConfigIfIndex_Object((1,3,6,1,2,1,171,1,2,3,1,1),_MidcomConfigIfIndex_Type())
midcomConfigIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:midcomConfigIfIndex.setStatus(_A)
class _MidcomConfigIfBits_Type(Bits):namedValues=NamedValues(*(('ipv4',0),('ipv6',1),('addressWildcards',2),('portWildcards',3),('firewall',4),('nat',5),('portTranslation',6),('protocolTranslation',7),('twiceNat',8),('inside',9)))
_MidcomConfigIfBits_Type.__name__='Bits'
_MidcomConfigIfBits_Object=MibTableColumn
midcomConfigIfBits=_MidcomConfigIfBits_Object((1,3,6,1,2,1,171,1,2,3,1,2),_MidcomConfigIfBits_Type())
midcomConfigIfBits.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomConfigIfBits.setStatus(_A)
class _MidcomConfigIfEnabled_Type(TruthValue):defaultValue=1
_MidcomConfigIfEnabled_Type.__name__=_U
_MidcomConfigIfEnabled_Object=MibTableColumn
midcomConfigIfEnabled=_MidcomConfigIfEnabled_Object((1,3,6,1,2,1,171,1,2,3,1,3),_MidcomConfigIfEnabled_Type())
midcomConfigIfEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomConfigIfEnabled.setStatus(_A)
_MidcomConfigFirewallTable_Object=MibTable
midcomConfigFirewallTable=_MidcomConfigFirewallTable_Object((1,3,6,1,2,1,171,1,2,4))
if mibBuilder.loadTexts:midcomConfigFirewallTable.setStatus(_A)
_MidcomConfigFirewallEntry_Object=MibTableRow
midcomConfigFirewallEntry=_MidcomConfigFirewallEntry_Object((1,3,6,1,2,1,171,1,2,4,1))
midcomConfigFirewallEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:midcomConfigFirewallEntry.setStatus(_A)
_MidcomConfigFirewallIndex_Type=InterfaceIndexOrZero
_MidcomConfigFirewallIndex_Object=MibTableColumn
midcomConfigFirewallIndex=_MidcomConfigFirewallIndex_Object((1,3,6,1,2,1,171,1,2,4,1,1),_MidcomConfigFirewallIndex_Type())
midcomConfigFirewallIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:midcomConfigFirewallIndex.setStatus(_A)
_MidcomConfigFirewallGroupId_Type=SnmpAdminString
_MidcomConfigFirewallGroupId_Object=MibTableColumn
midcomConfigFirewallGroupId=_MidcomConfigFirewallGroupId_Object((1,3,6,1,2,1,171,1,2,4,1,2),_MidcomConfigFirewallGroupId_Type())
midcomConfigFirewallGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomConfigFirewallGroupId.setStatus(_A)
_MidcomConfigFirewallPriority_Type=Unsigned32
_MidcomConfigFirewallPriority_Object=MibTableColumn
midcomConfigFirewallPriority=_MidcomConfigFirewallPriority_Object((1,3,6,1,2,1,171,1,2,4,1,3),_MidcomConfigFirewallPriority_Type())
midcomConfigFirewallPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:midcomConfigFirewallPriority.setStatus(_A)
_MidcomMonitoring_ObjectIdentity=ObjectIdentity
midcomMonitoring=_MidcomMonitoring_ObjectIdentity((1,3,6,1,2,1,171,1,3))
_MidcomResourceTable_Object=MibTable
midcomResourceTable=_MidcomResourceTable_Object((1,3,6,1,2,1,171,1,3,1))
if mibBuilder.loadTexts:midcomResourceTable.setStatus(_A)
_MidcomResourceEntry_Object=MibTableRow
midcomResourceEntry=_MidcomResourceEntry_Object((1,3,6,1,2,1,171,1,3,1,1))
if mibBuilder.loadTexts:midcomResourceEntry.setStatus(_A)
_MidcomRscNatInternalAddrBindMode_Type=MidcomNatBindMode
_MidcomRscNatInternalAddrBindMode_Object=MibTableColumn
midcomRscNatInternalAddrBindMode=_MidcomRscNatInternalAddrBindMode_Object((1,3,6,1,2,1,171,1,3,1,1,4),_MidcomRscNatInternalAddrBindMode_Type())
midcomRscNatInternalAddrBindMode.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatInternalAddrBindMode.setStatus(_A)
_MidcomRscNatInternalAddrBindId_Type=NatBindIdOrZero
_MidcomRscNatInternalAddrBindId_Object=MibTableColumn
midcomRscNatInternalAddrBindId=_MidcomRscNatInternalAddrBindId_Object((1,3,6,1,2,1,171,1,3,1,1,5),_MidcomRscNatInternalAddrBindId_Type())
midcomRscNatInternalAddrBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatInternalAddrBindId.setStatus(_A)
_MidcomRscNatInsideAddrBindMode_Type=MidcomNatBindMode
_MidcomRscNatInsideAddrBindMode_Object=MibTableColumn
midcomRscNatInsideAddrBindMode=_MidcomRscNatInsideAddrBindMode_Object((1,3,6,1,2,1,171,1,3,1,1,6),_MidcomRscNatInsideAddrBindMode_Type())
midcomRscNatInsideAddrBindMode.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatInsideAddrBindMode.setStatus(_A)
_MidcomRscNatInsideAddrBindId_Type=NatBindIdOrZero
_MidcomRscNatInsideAddrBindId_Object=MibTableColumn
midcomRscNatInsideAddrBindId=_MidcomRscNatInsideAddrBindId_Object((1,3,6,1,2,1,171,1,3,1,1,7),_MidcomRscNatInsideAddrBindId_Type())
midcomRscNatInsideAddrBindId.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatInsideAddrBindId.setStatus(_A)
_MidcomRscNatSessionId1_Type=MidcomNatSessionIdOrZero
_MidcomRscNatSessionId1_Object=MibTableColumn
midcomRscNatSessionId1=_MidcomRscNatSessionId1_Object((1,3,6,1,2,1,171,1,3,1,1,8),_MidcomRscNatSessionId1_Type())
midcomRscNatSessionId1.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatSessionId1.setStatus(_A)
_MidcomRscNatSessionId2_Type=MidcomNatSessionIdOrZero
_MidcomRscNatSessionId2_Object=MibTableColumn
midcomRscNatSessionId2=_MidcomRscNatSessionId2_Object((1,3,6,1,2,1,171,1,3,1,1,9),_MidcomRscNatSessionId2_Type())
midcomRscNatSessionId2.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscNatSessionId2.setStatus(_A)
_MidcomRscFirewallRuleId_Type=Unsigned32
_MidcomRscFirewallRuleId_Object=MibTableColumn
midcomRscFirewallRuleId=_MidcomRscFirewallRuleId_Object((1,3,6,1,2,1,171,1,3,1,1,10),_MidcomRscFirewallRuleId_Type())
midcomRscFirewallRuleId.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomRscFirewallRuleId.setStatus(_A)
_MidcomStatistics_ObjectIdentity=ObjectIdentity
midcomStatistics=_MidcomStatistics_ObjectIdentity((1,3,6,1,2,1,171,1,3,2))
_MidcomCurrentOwners_Type=Gauge32
_MidcomCurrentOwners_Object=MibScalar
midcomCurrentOwners=_MidcomCurrentOwners_Object((1,3,6,1,2,1,171,1,3,2,1),_MidcomCurrentOwners_Type())
midcomCurrentOwners.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomCurrentOwners.setStatus(_A)
_MidcomTotalRejectedRuleEntries_Type=Counter32
_MidcomTotalRejectedRuleEntries_Object=MibScalar
midcomTotalRejectedRuleEntries=_MidcomTotalRejectedRuleEntries_Object((1,3,6,1,2,1,171,1,3,2,2),_MidcomTotalRejectedRuleEntries_Type())
midcomTotalRejectedRuleEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalRejectedRuleEntries.setStatus(_A)
_MidcomCurrentRulesIncomplete_Type=Gauge32
_MidcomCurrentRulesIncomplete_Object=MibScalar
midcomCurrentRulesIncomplete=_MidcomCurrentRulesIncomplete_Object((1,3,6,1,2,1,171,1,3,2,3),_MidcomCurrentRulesIncomplete_Type())
midcomCurrentRulesIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomCurrentRulesIncomplete.setStatus(_A)
_MidcomTotalIncorrectReserveRules_Type=Counter32
_MidcomTotalIncorrectReserveRules_Object=MibScalar
midcomTotalIncorrectReserveRules=_MidcomTotalIncorrectReserveRules_Object((1,3,6,1,2,1,171,1,3,2,4),_MidcomTotalIncorrectReserveRules_Type())
midcomTotalIncorrectReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalIncorrectReserveRules.setStatus(_A)
_MidcomTotalRejectedReserveRules_Type=Counter32
_MidcomTotalRejectedReserveRules_Object=MibScalar
midcomTotalRejectedReserveRules=_MidcomTotalRejectedReserveRules_Object((1,3,6,1,2,1,171,1,3,2,5),_MidcomTotalRejectedReserveRules_Type())
midcomTotalRejectedReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalRejectedReserveRules.setStatus(_A)
_MidcomCurrentActiveReserveRules_Type=Gauge32
_MidcomCurrentActiveReserveRules_Object=MibScalar
midcomCurrentActiveReserveRules=_MidcomCurrentActiveReserveRules_Object((1,3,6,1,2,1,171,1,3,2,6),_MidcomCurrentActiveReserveRules_Type())
midcomCurrentActiveReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomCurrentActiveReserveRules.setStatus(_A)
_MidcomTotalExpiredReserveRules_Type=Counter32
_MidcomTotalExpiredReserveRules_Object=MibScalar
midcomTotalExpiredReserveRules=_MidcomTotalExpiredReserveRules_Object((1,3,6,1,2,1,171,1,3,2,7),_MidcomTotalExpiredReserveRules_Type())
midcomTotalExpiredReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalExpiredReserveRules.setStatus(_A)
_MidcomTotalTerminatedOnRqReserveRules_Type=Counter32
_MidcomTotalTerminatedOnRqReserveRules_Object=MibScalar
midcomTotalTerminatedOnRqReserveRules=_MidcomTotalTerminatedOnRqReserveRules_Object((1,3,6,1,2,1,171,1,3,2,8),_MidcomTotalTerminatedOnRqReserveRules_Type())
midcomTotalTerminatedOnRqReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalTerminatedOnRqReserveRules.setStatus(_A)
_MidcomTotalTerminatedReserveRules_Type=Counter32
_MidcomTotalTerminatedReserveRules_Object=MibScalar
midcomTotalTerminatedReserveRules=_MidcomTotalTerminatedReserveRules_Object((1,3,6,1,2,1,171,1,3,2,9),_MidcomTotalTerminatedReserveRules_Type())
midcomTotalTerminatedReserveRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalTerminatedReserveRules.setStatus(_A)
_MidcomTotalIncorrectEnableRules_Type=Counter32
_MidcomTotalIncorrectEnableRules_Object=MibScalar
midcomTotalIncorrectEnableRules=_MidcomTotalIncorrectEnableRules_Object((1,3,6,1,2,1,171,1,3,2,10),_MidcomTotalIncorrectEnableRules_Type())
midcomTotalIncorrectEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalIncorrectEnableRules.setStatus(_A)
_MidcomTotalRejectedEnableRules_Type=Counter32
_MidcomTotalRejectedEnableRules_Object=MibScalar
midcomTotalRejectedEnableRules=_MidcomTotalRejectedEnableRules_Object((1,3,6,1,2,1,171,1,3,2,11),_MidcomTotalRejectedEnableRules_Type())
midcomTotalRejectedEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalRejectedEnableRules.setStatus(_A)
_MidcomCurrentActiveEnableRules_Type=Gauge32
_MidcomCurrentActiveEnableRules_Object=MibScalar
midcomCurrentActiveEnableRules=_MidcomCurrentActiveEnableRules_Object((1,3,6,1,2,1,171,1,3,2,12),_MidcomCurrentActiveEnableRules_Type())
midcomCurrentActiveEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomCurrentActiveEnableRules.setStatus(_A)
_MidcomTotalExpiredEnableRules_Type=Counter32
_MidcomTotalExpiredEnableRules_Object=MibScalar
midcomTotalExpiredEnableRules=_MidcomTotalExpiredEnableRules_Object((1,3,6,1,2,1,171,1,3,2,13),_MidcomTotalExpiredEnableRules_Type())
midcomTotalExpiredEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalExpiredEnableRules.setStatus(_A)
_MidcomTotalTerminatedOnRqEnableRules_Type=Counter32
_MidcomTotalTerminatedOnRqEnableRules_Object=MibScalar
midcomTotalTerminatedOnRqEnableRules=_MidcomTotalTerminatedOnRqEnableRules_Object((1,3,6,1,2,1,171,1,3,2,14),_MidcomTotalTerminatedOnRqEnableRules_Type())
midcomTotalTerminatedOnRqEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalTerminatedOnRqEnableRules.setStatus(_A)
_MidcomTotalTerminatedEnableRules_Type=Counter32
_MidcomTotalTerminatedEnableRules_Object=MibScalar
midcomTotalTerminatedEnableRules=_MidcomTotalTerminatedEnableRules_Object((1,3,6,1,2,1,171,1,3,2,15),_MidcomTotalTerminatedEnableRules_Type())
midcomTotalTerminatedEnableRules.setMaxAccess(_C)
if mibBuilder.loadTexts:midcomTotalTerminatedEnableRules.setStatus(_A)
_MidcomConformance_ObjectIdentity=ObjectIdentity
midcomConformance=_MidcomConformance_ObjectIdentity((1,3,6,1,2,1,171,2))
_MidcomCompliances_ObjectIdentity=ObjectIdentity
midcomCompliances=_MidcomCompliances_ObjectIdentity((1,3,6,1,2,1,171,2,1))
_MidcomGroups_ObjectIdentity=ObjectIdentity
midcomGroups=_MidcomGroups_ObjectIdentity((1,3,6,1,2,1,171,2,2))
midcomRuleEntry.registerAugmentions((_B,_Y))
midcomResourceEntry.setIndexNames(*midcomRuleEntry.getIndexNames())
midcomRuleGroup=ObjectGroup((1,3,6,1,2,1,171,2,2,1))
midcomRuleGroup.setObjects(*((_B,_Z),(_B,_J),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_K),(_B,_u),(_B,_R)))
if mibBuilder.loadTexts:midcomRuleGroup.setStatus(_A)
midcomCapabilitiesGroup=ObjectGroup((1,3,6,1,2,1,171,2,2,2))
midcomCapabilitiesGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:midcomCapabilitiesGroup.setStatus(_A)
midcomConfigFirewallGroup=ObjectGroup((1,3,6,1,2,1,171,2,2,3))
midcomConfigFirewallGroup.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:midcomConfigFirewallGroup.setStatus(_A)
midcomResourceGroup=ObjectGroup((1,3,6,1,2,1,171,2,2,4))
midcomResourceGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:midcomResourceGroup.setStatus(_A)
midcomStatisticsGroup=ObjectGroup((1,3,6,1,2,1,171,2,2,5))
midcomStatisticsGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:midcomStatisticsGroup.setStatus(_A)
midcomUnsolicitedRuleEvent=NotificationType((1,3,6,1,2,1,171,0,1))
midcomUnsolicitedRuleEvent.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:midcomUnsolicitedRuleEvent.setStatus(_A)
midcomSolicitedRuleEvent=NotificationType((1,3,6,1,2,1,171,0,2))
midcomSolicitedRuleEvent.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:midcomSolicitedRuleEvent.setStatus(_A)
midcomSolicitedGroupEvent=NotificationType((1,3,6,1,2,1,171,0,3))
midcomSolicitedGroupEvent.setObjects((_B,_R))
if mibBuilder.loadTexts:midcomSolicitedGroupEvent.setStatus(_A)
midcomNotificationsGroup=NotificationGroup((1,3,6,1,2,1,171,2,2,6))
midcomNotificationsGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:midcomNotificationsGroup.setStatus(_A)
midcomCompliance=ModuleCompliance((1,3,6,1,2,1,171,2,1,1))
midcomCompliance.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:midcomCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MidcomNatBindMode':MidcomNatBindMode,'MidcomNatSessionIdOrZero':MidcomNatSessionIdOrZero,'midcomMIB':midcomMIB,'midcomNotifications':midcomNotifications,_AN:midcomUnsolicitedRuleEvent,_AO:midcomSolicitedRuleEvent,_AP:midcomSolicitedGroupEvent,'midcomObjects':midcomObjects,'midcomTransaction':midcomTransaction,'midcomRuleTable':midcomRuleTable,'midcomRuleEntry':midcomRuleEntry,_P:midcomRuleOwner,_V:midcomRuleIndex,_Z:midcomRuleAdminStatus,_J:midcomRuleOperStatus,_a:midcomRuleStorageType,_b:midcomRuleStorageTime,_c:midcomRuleError,_d:midcomRuleInterface,_e:midcomRuleFlowDirection,_f:midcomRuleMaxIdleTime,_g:midcomRuleTransportProtocol,_h:midcomRulePortRange,_i:midcomRuleInternalIpVersion,_j:midcomRuleExternalIpVersion,_k:midcomRuleInternalIpAddr,_l:midcomRuleInternalIpPrefixLength,_m:midcomRuleInternalPort,_n:midcomRuleExternalIpAddr,_o:midcomRuleExternalIpPrefixLength,_p:midcomRuleExternalPort,_q:midcomRuleInsideIpAddr,_r:midcomRuleInsidePort,_s:midcomRuleOutsideIpAddr,_t:midcomRuleOutsidePort,_K:midcomRuleLifetime,_u:midcomRuleRowStatus,'midcomGroupTable':midcomGroupTable,'midcomGroupEntry':midcomGroupEntry,_Q:midcomGroupIndex,_R:midcomGroupLifetime,'midcomConfig':midcomConfig,_v:midcomConfigMaxLifetime,_w:midcomConfigPersistentRules,'midcomConfigIfTable':midcomConfigIfTable,'midcomConfigIfEntry':midcomConfigIfEntry,_W:midcomConfigIfIndex,_x:midcomConfigIfBits,_y:midcomConfigIfEnabled,'midcomConfigFirewallTable':midcomConfigFirewallTable,'midcomConfigFirewallEntry':midcomConfigFirewallEntry,_X:midcomConfigFirewallIndex,_z:midcomConfigFirewallGroupId,_A0:midcomConfigFirewallPriority,'midcomMonitoring':midcomMonitoring,'midcomResourceTable':midcomResourceTable,_Y:midcomResourceEntry,_A1:midcomRscNatInternalAddrBindMode,_A2:midcomRscNatInternalAddrBindId,_A3:midcomRscNatInsideAddrBindMode,_A4:midcomRscNatInsideAddrBindId,_A5:midcomRscNatSessionId1,_A6:midcomRscNatSessionId2,_A7:midcomRscFirewallRuleId,'midcomStatistics':midcomStatistics,_A8:midcomCurrentOwners,_A9:midcomTotalRejectedRuleEntries,_AA:midcomCurrentRulesIncomplete,_AB:midcomTotalIncorrectReserveRules,_AC:midcomTotalRejectedReserveRules,_AD:midcomCurrentActiveReserveRules,_AE:midcomTotalExpiredReserveRules,_AF:midcomTotalTerminatedOnRqReserveRules,_AG:midcomTotalTerminatedReserveRules,_AH:midcomTotalIncorrectEnableRules,_AI:midcomTotalRejectedEnableRules,_AJ:midcomCurrentActiveEnableRules,_AK:midcomTotalExpiredEnableRules,_AL:midcomTotalTerminatedOnRqEnableRules,_AM:midcomTotalTerminatedEnableRules,'midcomConformance':midcomConformance,'midcomCompliances':midcomCompliances,'midcomCompliance':midcomCompliance,'midcomGroups':midcomGroups,_AQ:midcomRuleGroup,_AS:midcomCapabilitiesGroup,_AU:midcomConfigFirewallGroup,_AV:midcomResourceGroup,_AT:midcomStatisticsGroup,_AR:midcomNotificationsGroup})