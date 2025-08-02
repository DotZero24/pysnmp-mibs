_Aj='extremeNMSDeviceAddress'
_Ai='extremeArpSecurityMacAddress'
_Ah='extremeArpSecurityIpAddr'
_Ag='extremeArpSecurityPortIfIndex'
_Af='extremeArpSecurityVlanDescr'
_Ae='extremeArpSecurityVlanIfIndex'
_Ad='extremeNetloginAuthDataBase'
_Ac='extremeExceededByteCount'
_Ab='extremeRateLimitExceededTrapIndicator'
_Aa='extremeRateLimitExceededTrapType'
_AZ='extremeVlanIfIndex'
_AY='extremeSlotModuleState'
_AX='extremeSlotModuleInsertedType'
_AW='extremeSlotModuleConfiguredType'
_AV='extremeMsmFailoverCause'
_AU='extremeMasterMSMSlot'
_AT='extremeHealthCheckMaxRetries'
_AS='extremeHealthCheckErrorType'
_AR='extremeHealthCheckAction'
_AQ='extremeIQosProfileIndex'
_AP='EXTREME-QOS-MIB'
_AO='extremePethSlotPSUActive'
_AN='extremePethSlotMainPseIndex'
_AM='extremeNPModuleProcessorState'
_AL='EXTREME-NP-MIB'
_AK='extremeEsrpState'
_AJ='EXTREME-ESRP-MIB'
_AI='extremeEapsStatusTrapCount'
_AH='extremeEapsSharedPortState'
_AG='extremeEapsSharedPortRootBlockerId'
_AF='extremeEapsSharedPortNbrStatus'
_AE='extremeEapsSharedPortLinkId'
_AD='extremeEapsLastConfigurationChange'
_AC='extremeSharedPort'
_AB='extremeSegmentPort'
_AA='ifDescr'
_A9='ifAlias'
_A8='extremeVlanIfDescr'
_A7='extremePowerSupplyNumber'
_A6='extremeFanNumber'
_A5='extremeCurrentTemperature'
_A4='extremeCpuUtilRisingThreshold'
_A3='extremeCpuTaskUtilPair'
_A2='extremeCpuAggregateUtilization'
_A1='EXTREME-POE-MIB'
_A0='extremeLacpMemberPort'
_z='extremeLacpGroup'
_y='extremeEdpPortIfIndex'
_x='extremeEdpNeighborId'
_w='extremeEdpEntryAge'
_v='extremeEapsSharedPortRootBlockerStatus'
_u='extremeEapsSharedPortIfIndex'
_t='extremeBgp4V2PeerRemoteAddrType'
_s='extremeBgp4V2PeerRemoteAddr'
_r='extremeBgp4V2PeerLocalAddrType'
_q='extremeBgp4V2PeerLocalAddr'
_p='bgpPeerRemoteAddr'
_o='BGP4-MIB'
_n='extremeNetloginMoveToVlanList'
_m='extremeNetloginMoveFromVlanList'
_l='extremeNetloginSessionStatus'
_k='extremeNetloginDestVlan'
_j='extremeNetloginSrcVlan'
_i='extremeNetloginUser'
_h='extremeNetloginSystemTime'
_g='extremeNetloginAuthType'
_f='extremeNetloginPortIfIndex'
_e='extremeNetloginStationAddr'
_d='extremeNetloginStationMac'
_c='extremeMacSecurityVlanId'
_b='extremeMacSecurityPortIfIndex'
_a='extremeMacSecurityMacAddress'
_Z='extremeMacSecurityVlanDescr'
_Y='extremeMacSecurityVlanIfIndex'
_X='Integer32'
_W='EXTREME-VLAN-MIB'
_V='extremeSlotNumber'
_U='extremeEapsFailedFlag'
_T='EXTREME-LACP-MIB'
_S='extremeEapsState'
_R='extremeEapsSecondaryStatus'
_Q='extremeEapsPrimaryStatus'
_P='extremeEapsPrevState'
_O='extremeEapsMode'
_N='extremeEapsLastStatusChange'
_M='IF-MIB'
_L='extremeEapsName'
_K='EXTREME-EDP-MIB'
_J='DisplayString'
_I='EXTREME-BGP4V2-MIB'
_H='sysUpTime'
_G='sysDescr'
_F='SNMPv2-MIB'
_E='EXTREME-SYSTEM-MIB'
_D='accessible-for-notify'
_C='EXTREME-EAPS-MIB'
_B='EXTREME-V2TRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bgpPeerRemoteAddr,=mibBuilder.importSymbols(_o,_p)
ClientAuthType,extremenetworks=mibBuilder.importSymbols('EXTREME-BASE-MIB','ClientAuthType','extremenetworks')
extremeBgp4V2PeerLocalAddr,extremeBgp4V2PeerLocalAddrType,extremeBgp4V2PeerRemoteAddr,extremeBgp4V2PeerRemoteAddrType=mibBuilder.importSymbols(_I,_q,_r,_s,_t)
EapsRingPort,extremeEapsFailedFlag,extremeEapsLastConfigurationChange,extremeEapsLastStatusChange,extremeEapsMode,extremeEapsName,extremeEapsPrevState,extremeEapsPrimaryStatus,extremeEapsSecondaryStatus,extremeEapsSharedPortIfIndex,extremeEapsSharedPortLinkId,extremeEapsSharedPortNbrStatus,extremeEapsSharedPortRootBlockerId,extremeEapsSharedPortRootBlockerStatus,extremeEapsSharedPortState,extremeEapsState,extremeEapsStatusTrapCount=mibBuilder.importSymbols(_C,'EapsRingPort',_U,_AD,_N,_O,_L,_P,_Q,_R,_u,_AE,_AF,_AG,_v,_AH,_S,_AI)
extremeEdpEntryAge,extremeEdpNeighborId,extremeEdpPortIfIndex=mibBuilder.importSymbols(_K,_w,_x,_y)
extremeEsrpGroup,extremeEsrpState=mibBuilder.importSymbols(_AJ,'extremeEsrpGroup',_AK)
extremeLacpGroup,extremeLacpMemberPort=mibBuilder.importSymbols(_T,_z,_A0)
extremeNPModuleProcessorState,=mibBuilder.importSymbols(_AL,_AM)
extremePethSlotMainPseIndex,extremePethSlotPSUActive=mibBuilder.importSymbols(_A1,_AN,_AO)
extremeIQosProfileIndex,=mibBuilder.importSymbols(_AP,_AQ)
extremeCpuAggregateUtilization,extremeCpuTaskUtilPair,extremeCpuUtilRisingThreshold,extremeCurrentTemperature,extremeFanNumber,extremeHealthCheckAction,extremeHealthCheckErrorType,extremeHealthCheckMaxRetries,extremeMasterMSMSlot,extremeMsmFailoverCause,extremePowerSupplyNumber,extremeSlotModuleConfiguredType,extremeSlotModuleInsertedType,extremeSlotModuleState,extremeSlotNumber=mibBuilder.importSymbols(_E,_A2,_A3,_A4,_A5,_A6,_AR,_AS,_AT,_AU,_AV,_A7,_AW,_AX,_AY,_V)
extremeVlanIfDescr,extremeVlanIfIndex=mibBuilder.importSymbols(_W,_A8,_AZ)
ifAlias,ifDescr,ifIndex=mibBuilder.importSymbols(_M,_A9,_AA,'ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_F,_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_X,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','TextualConvention','TimeStamp')
extremeV2Traps=ModuleIdentity((1,3,6,1,4,1,1916,4))
_ExtremeV1Traps_ObjectIdentity=ObjectIdentity
extremeV1Traps=_ExtremeV1Traps_ObjectIdentity((1,3,6,1,4,1,1916,0))
_ExtremeCoreSCTraps_ObjectIdentity=ObjectIdentity
extremeCoreSCTraps=_ExtremeCoreSCTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,1))
_ExtremeCoreSCTrapPrefix_ObjectIdentity=ObjectIdentity
extremeCoreSCTrapPrefix=_ExtremeCoreSCTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,1,0))
class _ExtremeRateLimitExceededTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exceededCIR',1),('droppedBytes',2)))
_ExtremeRateLimitExceededTrapType_Type.__name__=_X
_ExtremeRateLimitExceededTrapType_Object=MibScalar
extremeRateLimitExceededTrapType=_ExtremeRateLimitExceededTrapType_Object((1,3,6,1,4,1,1916,4,1,0,7,1),_ExtremeRateLimitExceededTrapType_Type())
extremeRateLimitExceededTrapType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRateLimitExceededTrapType.setStatus(_A)
class _ExtremeRateLimitExceededTrapIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('clear',0),('set',1)))
_ExtremeRateLimitExceededTrapIndicator_Type.__name__=_X
_ExtremeRateLimitExceededTrapIndicator_Object=MibScalar
extremeRateLimitExceededTrapIndicator=_ExtremeRateLimitExceededTrapIndicator_Object((1,3,6,1,4,1,1916,4,1,0,7,2),_ExtremeRateLimitExceededTrapIndicator_Type())
extremeRateLimitExceededTrapIndicator.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeRateLimitExceededTrapIndicator.setStatus(_A)
_ExtremeExceededByteCount_Type=Integer32
_ExtremeExceededByteCount_Object=MibScalar
extremeExceededByteCount=_ExtremeExceededByteCount_Object((1,3,6,1,4,1,1916,4,1,0,7,4),_ExtremeExceededByteCount_Type())
extremeExceededByteCount.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeExceededByteCount.setStatus(_A)
_ExtremeBgpTraps_ObjectIdentity=ObjectIdentity
extremeBgpTraps=_ExtremeBgpTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,2))
_ExtremeBgpTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeBgpTrapsPrefix=_ExtremeBgpTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,2,0))
_ExtremeSecurityTraps_ObjectIdentity=ObjectIdentity
extremeSecurityTraps=_ExtremeSecurityTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,3))
_ExtremeSecurityTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeSecurityTrapsPrefix=_ExtremeSecurityTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,3,0))
_ExtremeMacSecurityVlanIfIndex_Type=Integer32
_ExtremeMacSecurityVlanIfIndex_Object=MibScalar
extremeMacSecurityVlanIfIndex=_ExtremeMacSecurityVlanIfIndex_Object((1,3,6,1,4,1,1916,4,3,1),_ExtremeMacSecurityVlanIfIndex_Type())
extremeMacSecurityVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacSecurityVlanIfIndex.setStatus(_A)
class _ExtremeMacSecurityVlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeMacSecurityVlanDescr_Type.__name__=_J
_ExtremeMacSecurityVlanDescr_Object=MibScalar
extremeMacSecurityVlanDescr=_ExtremeMacSecurityVlanDescr_Object((1,3,6,1,4,1,1916,4,3,2),_ExtremeMacSecurityVlanDescr_Type())
extremeMacSecurityVlanDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacSecurityVlanDescr.setStatus(_A)
_ExtremeMacSecurityMacAddress_Type=MacAddress
_ExtremeMacSecurityMacAddress_Object=MibScalar
extremeMacSecurityMacAddress=_ExtremeMacSecurityMacAddress_Object((1,3,6,1,4,1,1916,4,3,3),_ExtremeMacSecurityMacAddress_Type())
extremeMacSecurityMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacSecurityMacAddress.setStatus(_A)
_ExtremeMacSecurityPortIfIndex_Type=Integer32
_ExtremeMacSecurityPortIfIndex_Object=MibScalar
extremeMacSecurityPortIfIndex=_ExtremeMacSecurityPortIfIndex_Object((1,3,6,1,4,1,1916,4,3,4),_ExtremeMacSecurityPortIfIndex_Type())
extremeMacSecurityPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacSecurityPortIfIndex.setStatus(_A)
_ExtremeMacSecurityVlanId_Type=Integer32
_ExtremeMacSecurityVlanId_Object=MibScalar
extremeMacSecurityVlanId=_ExtremeMacSecurityVlanId_Object((1,3,6,1,4,1,1916,4,3,5),_ExtremeMacSecurityVlanId_Type())
extremeMacSecurityVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMacSecurityVlanId.setStatus(_A)
_ExtremeNetloginStationMac_Type=MacAddress
_ExtremeNetloginStationMac_Object=MibScalar
extremeNetloginStationMac=_ExtremeNetloginStationMac_Object((1,3,6,1,4,1,1916,4,3,6),_ExtremeNetloginStationMac_Type())
extremeNetloginStationMac.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginStationMac.setStatus(_A)
_ExtremeNetloginStationAddr_Type=IpAddress
_ExtremeNetloginStationAddr_Object=MibScalar
extremeNetloginStationAddr=_ExtremeNetloginStationAddr_Object((1,3,6,1,4,1,1916,4,3,7),_ExtremeNetloginStationAddr_Type())
extremeNetloginStationAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginStationAddr.setStatus(_A)
_ExtremeNetloginPortIfIndex_Type=Integer32
_ExtremeNetloginPortIfIndex_Object=MibScalar
extremeNetloginPortIfIndex=_ExtremeNetloginPortIfIndex_Object((1,3,6,1,4,1,1916,4,3,8),_ExtremeNetloginPortIfIndex_Type())
extremeNetloginPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginPortIfIndex.setStatus(_A)
_ExtremeNetloginAuthType_Type=ClientAuthType
_ExtremeNetloginAuthType_Object=MibScalar
extremeNetloginAuthType=_ExtremeNetloginAuthType_Object((1,3,6,1,4,1,1916,4,3,9),_ExtremeNetloginAuthType_Type())
extremeNetloginAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginAuthType.setStatus(_A)
_ExtremeNetloginSystemTime_Type=TimeStamp
_ExtremeNetloginSystemTime_Object=MibScalar
extremeNetloginSystemTime=_ExtremeNetloginSystemTime_Object((1,3,6,1,4,1,1916,4,3,10),_ExtremeNetloginSystemTime_Type())
extremeNetloginSystemTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginSystemTime.setStatus(_A)
class _ExtremeNetloginUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ExtremeNetloginUser_Type.__name__=_J
_ExtremeNetloginUser_Object=MibScalar
extremeNetloginUser=_ExtremeNetloginUser_Object((1,3,6,1,4,1,1916,4,3,11),_ExtremeNetloginUser_Type())
extremeNetloginUser.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginUser.setStatus(_A)
class _ExtremeNetloginSrcVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ExtremeNetloginSrcVlan_Type.__name__=_J
_ExtremeNetloginSrcVlan_Object=MibScalar
extremeNetloginSrcVlan=_ExtremeNetloginSrcVlan_Object((1,3,6,1,4,1,1916,4,3,12),_ExtremeNetloginSrcVlan_Type())
extremeNetloginSrcVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginSrcVlan.setStatus(_A)
class _ExtremeNetloginDestVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ExtremeNetloginDestVlan_Type.__name__=_J
_ExtremeNetloginDestVlan_Object=MibScalar
extremeNetloginDestVlan=_ExtremeNetloginDestVlan_Object((1,3,6,1,4,1,1916,4,3,13),_ExtremeNetloginDestVlan_Type())
extremeNetloginDestVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginDestVlan.setStatus(_A)
class _ExtremeNetloginSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('success',1),('sessionReset',2),('fDBAgingInitiatedLogout',3),('userInitiatedLogout',4),('sessionRefreshInitiatedLogout',5),('authenticationFailure',6),('remoteAuthenticationServerFailure',7),('fDBDeleteInitiatedLogout',8),('linkDownInitiatedLogout',9),('reauthenticationFailure',10),('successWithRestrictedAccess',11),('successWithTimeLimitedAccess',12),('frameworkInitiatedLogout',13),('l2ProtoInitiatedLogout',14),('preferredProtocolInitiatedLogout',15)))
_ExtremeNetloginSessionStatus_Type.__name__=_X
_ExtremeNetloginSessionStatus_Object=MibScalar
extremeNetloginSessionStatus=_ExtremeNetloginSessionStatus_Object((1,3,6,1,4,1,1916,4,3,14),_ExtremeNetloginSessionStatus_Type())
extremeNetloginSessionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginSessionStatus.setStatus(_A)
_ExtremeArpSecurityVlanIfIndex_Type=Integer32
_ExtremeArpSecurityVlanIfIndex_Object=MibScalar
extremeArpSecurityVlanIfIndex=_ExtremeArpSecurityVlanIfIndex_Object((1,3,6,1,4,1,1916,4,3,15),_ExtremeArpSecurityVlanIfIndex_Type())
extremeArpSecurityVlanIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeArpSecurityVlanIfIndex.setStatus(_A)
class _ExtremeArpSecurityVlanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeArpSecurityVlanDescr_Type.__name__=_J
_ExtremeArpSecurityVlanDescr_Object=MibScalar
extremeArpSecurityVlanDescr=_ExtremeArpSecurityVlanDescr_Object((1,3,6,1,4,1,1916,4,3,16),_ExtremeArpSecurityVlanDescr_Type())
extremeArpSecurityVlanDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeArpSecurityVlanDescr.setStatus(_A)
_ExtremeArpSecurityPortIfIndex_Type=Integer32
_ExtremeArpSecurityPortIfIndex_Object=MibScalar
extremeArpSecurityPortIfIndex=_ExtremeArpSecurityPortIfIndex_Object((1,3,6,1,4,1,1916,4,3,17),_ExtremeArpSecurityPortIfIndex_Type())
extremeArpSecurityPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeArpSecurityPortIfIndex.setStatus(_A)
_ExtremeArpSecurityIpAddr_Type=IpAddress
_ExtremeArpSecurityIpAddr_Object=MibScalar
extremeArpSecurityIpAddr=_ExtremeArpSecurityIpAddr_Object((1,3,6,1,4,1,1916,4,3,18),_ExtremeArpSecurityIpAddr_Type())
extremeArpSecurityIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeArpSecurityIpAddr.setStatus(_A)
_ExtremeArpSecurityMacAddress_Type=MacAddress
_ExtremeArpSecurityMacAddress_Object=MibScalar
extremeArpSecurityMacAddress=_ExtremeArpSecurityMacAddress_Object((1,3,6,1,4,1,1916,4,3,19),_ExtremeArpSecurityMacAddress_Type())
extremeArpSecurityMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeArpSecurityMacAddress.setStatus(_A)
class _ExtremeNetloginAuthDataBase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ExtremeNetloginAuthDataBase_Type.__name__=_J
_ExtremeNetloginAuthDataBase_Object=MibScalar
extremeNetloginAuthDataBase=_ExtremeNetloginAuthDataBase_Object((1,3,6,1,4,1,1916,4,3,20),_ExtremeNetloginAuthDataBase_Type())
extremeNetloginAuthDataBase.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginAuthDataBase.setStatus(_A)
class _ExtremeNetloginMoveFromVlanList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ExtremeNetloginMoveFromVlanList_Type.__name__=_J
_ExtremeNetloginMoveFromVlanList_Object=MibScalar
extremeNetloginMoveFromVlanList=_ExtremeNetloginMoveFromVlanList_Object((1,3,6,1,4,1,1916,4,3,21),_ExtremeNetloginMoveFromVlanList_Type())
extremeNetloginMoveFromVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginMoveFromVlanList.setStatus(_A)
class _ExtremeNetloginMoveToVlanList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ExtremeNetloginMoveToVlanList_Type.__name__=_J
_ExtremeNetloginMoveToVlanList_Object=MibScalar
extremeNetloginMoveToVlanList=_ExtremeNetloginMoveToVlanList_Object((1,3,6,1,4,1,1916,4,3,22),_ExtremeNetloginMoveToVlanList_Type())
extremeNetloginMoveToVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNetloginMoveToVlanList.setStatus(_A)
_ExtremeNMSTraps_ObjectIdentity=ObjectIdentity
extremeNMSTraps=_ExtremeNMSTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,4))
_ExtremeNMSTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeNMSTrapsPrefix=_ExtremeNMSTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,4,0))
_ExtremeNMSDeviceAddress_Type=IpAddress
_ExtremeNMSDeviceAddress_Object=MibScalar
extremeNMSDeviceAddress=_ExtremeNMSDeviceAddress_Object((1,3,6,1,4,1,1916,4,4,1),_ExtremeNMSDeviceAddress_Type())
extremeNMSDeviceAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeNMSDeviceAddress.setStatus(_A)
_ExtremeElrpTraps_ObjectIdentity=ObjectIdentity
extremeElrpTraps=_ExtremeElrpTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,6))
_ExtremeElrpTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeElrpTrapsPrefix=_ExtremeElrpTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,6,0))
_ExtremeEapsTraps_ObjectIdentity=ObjectIdentity
extremeEapsTraps=_ExtremeEapsTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,7))
_ExtremeEapsTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeEapsTrapsPrefix=_ExtremeEapsTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,7,0))
_ExtremeBgpM2Traps_ObjectIdentity=ObjectIdentity
extremeBgpM2Traps=_ExtremeBgpM2Traps_ObjectIdentity((1,3,6,1,4,1,1916,4,8))
_ExtremeBgpM2TrapsPrefix_ObjectIdentity=ObjectIdentity
extremeBgpM2TrapsPrefix=_ExtremeBgpM2TrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,8,0))
_ExtremeEapsSharedLinkTraps_ObjectIdentity=ObjectIdentity
extremeEapsSharedLinkTraps=_ExtremeEapsSharedLinkTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,9))
_ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeEapsSharedLinkTrapsPrefix=_ExtremeEapsSharedLinkTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,9,0))
_ExtremeSegmentPort_Type=EapsRingPort
_ExtremeSegmentPort_Object=MibScalar
extremeSegmentPort=_ExtremeSegmentPort_Object((1,3,6,1,4,1,1916,4,9,1),_ExtremeSegmentPort_Type())
extremeSegmentPort.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSegmentPort.setStatus(_A)
_ExtremeSharedPort_Type=EapsRingPort
_ExtremeSharedPort_Object=MibScalar
extremeSharedPort=_ExtremeSharedPort_Object((1,3,6,1,4,1,1916,4,9,2),_ExtremeSharedPort_Type())
extremeSharedPort.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeSharedPort.setStatus(_A)
_ExtremePethTraps_ObjectIdentity=ObjectIdentity
extremePethTraps=_ExtremePethTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,12))
_ExtremePethNotificationPrefix_ObjectIdentity=ObjectIdentity
extremePethNotificationPrefix=_ExtremePethNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,12,0))
_ExtremeLacpTraps_ObjectIdentity=ObjectIdentity
extremeLacpTraps=_ExtremeLacpTraps_ObjectIdentity((1,3,6,1,4,1,1916,4,13))
_ExtremeLacpNotificationPrefix_ObjectIdentity=ObjectIdentity
extremeLacpNotificationPrefix=_ExtremeLacpNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1916,4,13,0))
extremeOverheat=NotificationType((1,3,6,1,4,1,1916,0,6))
extremeOverheat.setObjects(*((_F,_H),(_F,_G),(_E,_A5)))
if mibBuilder.loadTexts:extremeOverheat.setStatus(_A)
extremeFanfailed=NotificationType((1,3,6,1,4,1,1916,0,7))
extremeFanfailed.setObjects(*((_F,_H),(_F,_G),(_E,_A6)))
if mibBuilder.loadTexts:extremeFanfailed.setStatus(_A)
extremeFanOK=NotificationType((1,3,6,1,4,1,1916,0,8))
extremeFanOK.setObjects(*((_F,_H),(_F,_G),(_E,_A6)))
if mibBuilder.loadTexts:extremeFanOK.setStatus(_A)
extremeInvalidLoginAttempt=NotificationType((1,3,6,1,4,1,1916,0,9))
extremeInvalidLoginAttempt.setObjects(*((_F,_H),(_F,_G)))
if mibBuilder.loadTexts:extremeInvalidLoginAttempt.setStatus(_A)
extremePowerSupplyFail=NotificationType((1,3,6,1,4,1,1916,0,10))
extremePowerSupplyFail.setObjects(*((_F,_H),(_F,_G),(_E,_A7)))
if mibBuilder.loadTexts:extremePowerSupplyFail.setStatus(_A)
extremePowerSupplyGood=NotificationType((1,3,6,1,4,1,1916,0,11))
extremePowerSupplyGood.setObjects(*((_F,_H),(_F,_G),(_E,_A7)))
if mibBuilder.loadTexts:extremePowerSupplyGood.setStatus(_A)
extremeSmartTrap=NotificationType((1,3,6,1,4,1,1916,0,14))
extremeSmartTrap.setObjects(*((_F,_H),(_F,_G)))
if mibBuilder.loadTexts:extremeSmartTrap.setStatus(_A)
extremeModuleStateChanged=NotificationType((1,3,6,1,4,1,1916,0,15))
extremeModuleStateChanged.setObjects(*((_F,_H),(_E,_V),(_E,_AW),(_E,_AX),(_E,_AY)))
if mibBuilder.loadTexts:extremeModuleStateChanged.setStatus(_A)
extremeEdpNeighborAdded=NotificationType((1,3,6,1,4,1,1916,0,20))
extremeEdpNeighborAdded.setObjects(*((_F,_H),(_K,_y),(_K,_x),(_K,_w),(_M,_A9),(_M,_AA)))
if mibBuilder.loadTexts:extremeEdpNeighborAdded.setStatus(_A)
extremeEdpNeighborRemoved=NotificationType((1,3,6,1,4,1,1916,0,21))
extremeEdpNeighborRemoved.setObjects(*((_F,_H),(_K,_y),(_K,_x),(_K,_w),(_M,_A9),(_M,_AA)))
if mibBuilder.loadTexts:extremeEdpNeighborRemoved.setStatus(_A)
extremeHealthCheckFailed=NotificationType((1,3,6,1,4,1,1916,4,1,0,1))
extremeHealthCheckFailed.setObjects(*((_F,_G),(_E,_V),(_E,_AS),(_E,_AR),(_E,_AT)))
if mibBuilder.loadTexts:extremeHealthCheckFailed.setStatus(_A)
extremeCpuUtilizationRisingTrap=NotificationType((1,3,6,1,4,1,1916,4,1,0,2))
extremeCpuUtilizationRisingTrap.setObjects(*((_E,_A3),(_E,_A2),(_E,_A4)))
if mibBuilder.loadTexts:extremeCpuUtilizationRisingTrap.setStatus(_A)
extremeCpuUtilizationFallingTrap=NotificationType((1,3,6,1,4,1,1916,4,1,0,3))
extremeCpuUtilizationFallingTrap.setObjects(*((_E,_A3),(_E,_A2),(_E,_A4)))
if mibBuilder.loadTexts:extremeCpuUtilizationFallingTrap.setStatus(_A)
extremeProcessorStateChangeTrap=NotificationType((1,3,6,1,4,1,1916,4,1,0,4))
extremeProcessorStateChangeTrap.setObjects(*((_F,_G),(_E,_V),(_AL,_AM)))
if mibBuilder.loadTexts:extremeProcessorStateChangeTrap.setStatus(_A)
extremeMsmFailoverTrap=NotificationType((1,3,6,1,4,1,1916,4,1,0,5))
extremeMsmFailoverTrap.setObjects(*((_F,_G),(_E,_AU),(_E,_AV)))
if mibBuilder.loadTexts:extremeMsmFailoverTrap.setStatus(_A)
extremeEsrpTimedOutFailedOverMaster=NotificationType((1,3,6,1,4,1,1916,4,1,0,6))
extremeEsrpTimedOutFailedOverMaster.setObjects(*((_F,_G),(_W,_AZ),(_W,_A8),(_AJ,_AK)))
if mibBuilder.loadTexts:extremeEsrpTimedOutFailedOverMaster.setStatus(_A)
extremeRateLimitExceededTrap=NotificationType((1,3,6,1,4,1,1916,4,1,0,7))
extremeRateLimitExceededTrap.setObjects(*((_B,_Aa),(_B,_Ab),(_M,'ifIndex'),(_AP,_AQ),(_B,_Ac)))
if mibBuilder.loadTexts:extremeRateLimitExceededTrap.setStatus(_A)
extremeOverheatNormal=NotificationType((1,3,6,1,4,1,1916,4,1,0,8))
extremeOverheatNormal.setObjects(*((_F,_G),(_E,_A5)))
if mibBuilder.loadTexts:extremeOverheatNormal.setStatus(_A)
extremeBgpPrefixReachedThreshold=NotificationType((1,3,6,1,4,1,1916,4,2,0,1))
extremeBgpPrefixReachedThreshold.setObjects((_o,_p))
if mibBuilder.loadTexts:extremeBgpPrefixReachedThreshold.setStatus(_A)
extremeBgpPrefixMaxExceeded=NotificationType((1,3,6,1,4,1,1916,4,2,0,2))
extremeBgpPrefixMaxExceeded.setObjects((_o,_p))
if mibBuilder.loadTexts:extremeBgpPrefixMaxExceeded.setStatus(_A)
extremeMacLimitExceeded=NotificationType((1,3,6,1,4,1,1916,4,3,0,1))
extremeMacLimitExceeded.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:extremeMacLimitExceeded.setStatus(_A)
extremeUnauthorizedPortForMacDetected=NotificationType((1,3,6,1,4,1,1916,4,3,0,2))
extremeUnauthorizedPortForMacDetected.setObjects(*((_B,_Y),(_B,_Z),(_B,_c),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:extremeUnauthorizedPortForMacDetected.setStatus(_A)
extremeMacDetectedOnLockedPort=NotificationType((1,3,6,1,4,1,1916,4,3,0,3))
extremeMacDetectedOnLockedPort.setObjects(*((_B,_Y),(_B,_Z),(_B,_c),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:extremeMacDetectedOnLockedPort.setStatus(_A)
extremeNetloginUserLogin=NotificationType((1,3,6,1,4,1,1916,4,3,0,4))
extremeNetloginUserLogin.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_Ad),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:extremeNetloginUserLogin.setStatus(_A)
extremeNetloginUserLogout=NotificationType((1,3,6,1,4,1,1916,4,3,0,5))
extremeNetloginUserLogout.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:extremeNetloginUserLogout.setStatus(_A)
extremeNetloginAuthFailure=NotificationType((1,3,6,1,4,1,1916,4,3,0,6))
extremeNetloginAuthFailure.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:extremeNetloginAuthFailure.setStatus(_A)
extremeGratuitousArpViolation=NotificationType((1,3,6,1,4,1,1916,4,3,0,7))
extremeGratuitousArpViolation.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:extremeGratuitousArpViolation.setStatus(_A)
extremeNMSInventoryChanged=NotificationType((1,3,6,1,4,1,1916,4,4,0,1))
extremeNMSInventoryChanged.setObjects((_B,_Aj))
if mibBuilder.loadTexts:extremeNMSInventoryChanged.setStatus(_A)
extremeNMSTopologyChanged=NotificationType((1,3,6,1,4,1,1916,4,4,0,2))
if mibBuilder.loadTexts:extremeNMSTopologyChanged.setStatus(_A)
extremeElrpVlanLoopDetected=NotificationType((1,3,6,1,4,1,1916,4,6,0,1))
extremeElrpVlanLoopDetected.setObjects((_W,_A8))
if mibBuilder.loadTexts:extremeElrpVlanLoopDetected.setStatus(_A)
extremeEapsStateChange=NotificationType((1,3,6,1,4,1,1916,4,7,0,1))
extremeEapsStateChange.setObjects(*((_C,_L),(_C,_O),(_C,_P),(_C,_S),(_C,_U),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:extremeEapsStateChange.setStatus(_A)
extremeEapsFailTimerExpFlagSet=NotificationType((1,3,6,1,4,1,1916,4,7,0,2))
extremeEapsFailTimerExpFlagSet.setObjects(*((_C,_L),(_C,_O),(_C,_P),(_C,_S)))
if mibBuilder.loadTexts:extremeEapsFailTimerExpFlagSet.setStatus(_A)
extremeEapsFailTimerExpFlagClear=NotificationType((1,3,6,1,4,1,1916,4,7,0,3))
extremeEapsFailTimerExpFlagClear.setObjects(*((_C,_L),(_C,_O),(_C,_P),(_C,_S),(_C,_U),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:extremeEapsFailTimerExpFlagClear.setStatus(_A)
extremeEapsLinkDownRingComplete=NotificationType((1,3,6,1,4,1,1916,4,7,0,4))
extremeEapsLinkDownRingComplete.setObjects(*((_C,_L),(_C,_O),(_C,_P),(_C,_S),(_C,_U),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:extremeEapsLinkDownRingComplete.setStatus(_A)
extremeEapsPortStatusChange=NotificationType((1,3,6,1,4,1,1916,4,7,0,5))
extremeEapsPortStatusChange.setObjects(*((_C,_L),(_C,_Q),(_C,_R),(_C,_N)))
if mibBuilder.loadTexts:extremeEapsPortStatusChange.setStatus(_A)
extremeEapsConfigChange=NotificationType((1,3,6,1,4,1,1916,4,7,0,6))
extremeEapsConfigChange.setObjects((_C,_AD))
if mibBuilder.loadTexts:extremeEapsConfigChange.setStatus(_A)
extremeEapsLastStatusChangeTime=NotificationType((1,3,6,1,4,1,1916,4,7,0,7))
extremeEapsLastStatusChangeTime.setObjects(*((_C,_N),(_C,_AI)))
if mibBuilder.loadTexts:extremeEapsLastStatusChangeTime.setStatus(_A)
extremeBgpM2PrefixReachedThreshold=NotificationType((1,3,6,1,4,1,1916,4,8,0,1))
extremeBgpM2PrefixReachedThreshold.setObjects(*((_I,_s),(_I,_t),(_I,_q),(_I,_r)))
if mibBuilder.loadTexts:extremeBgpM2PrefixReachedThreshold.setStatus(_A)
extremeBgpM2PrefixMaxExceeded=NotificationType((1,3,6,1,4,1,1916,4,8,0,2))
extremeBgpM2PrefixMaxExceeded.setObjects(*((_I,_s),(_I,_t),(_I,_q),(_I,_r)))
if mibBuilder.loadTexts:extremeBgpM2PrefixMaxExceeded.setStatus(_A)
extremeEapsSegmentTimerExpFlagSet=NotificationType((1,3,6,1,4,1,1916,4,9,0,1))
extremeEapsSegmentTimerExpFlagSet.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:extremeEapsSegmentTimerExpFlagSet.setStatus(_A)
extremeEapsSegmentTimerExpFlagClear=NotificationType((1,3,6,1,4,1,1916,4,9,0,2))
extremeEapsSegmentTimerExpFlagClear.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:extremeEapsSegmentTimerExpFlagClear.setStatus(_A)
extremeEapsSharedPortStateChange=NotificationType((1,3,6,1,4,1,1916,4,9,0,3))
extremeEapsSharedPortStateChange.setObjects(*((_C,_u),(_C,_AE),(_C,_AH),(_C,_AF),(_C,_v),(_C,_N)))
if mibBuilder.loadTexts:extremeEapsSharedPortStateChange.setStatus(_A)
extremeEapsRootBlockerStatusChange=NotificationType((1,3,6,1,4,1,1916,4,9,0,4))
extremeEapsRootBlockerStatusChange.setObjects(*((_C,_u),(_C,_v),(_C,_AG),(_C,_N)))
if mibBuilder.loadTexts:extremeEapsRootBlockerStatusChange.setStatus(_A)
extremePethPSUStatusNotification=NotificationType((1,3,6,1,4,1,1916,4,12,0,1))
extremePethPSUStatusNotification.setObjects(*((_A1,_AO),(_A1,_AN)))
if mibBuilder.loadTexts:extremePethPSUStatusNotification.setStatus(_A)
extremeLacpAddPortToAggregator=NotificationType((1,3,6,1,4,1,1916,4,13,0,1))
extremeLacpAddPortToAggregator.setObjects(*((_T,_z),(_T,_A0)))
if mibBuilder.loadTexts:extremeLacpAddPortToAggregator.setStatus(_A)
extremeLacpDeletePortFromAggregator=NotificationType((1,3,6,1,4,1,1916,4,13,0,2))
extremeLacpDeletePortFromAggregator.setObjects(*((_T,_z),(_T,_A0)))
if mibBuilder.loadTexts:extremeLacpDeletePortFromAggregator.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'extremeV1Traps':extremeV1Traps,'extremeOverheat':extremeOverheat,'extremeFanfailed':extremeFanfailed,'extremeFanOK':extremeFanOK,'extremeInvalidLoginAttempt':extremeInvalidLoginAttempt,'extremePowerSupplyFail':extremePowerSupplyFail,'extremePowerSupplyGood':extremePowerSupplyGood,'extremeSmartTrap':extremeSmartTrap,'extremeModuleStateChanged':extremeModuleStateChanged,'extremeEdpNeighborAdded':extremeEdpNeighborAdded,'extremeEdpNeighborRemoved':extremeEdpNeighborRemoved,'extremeV2Traps':extremeV2Traps,'extremeCoreSCTraps':extremeCoreSCTraps,'extremeCoreSCTrapPrefix':extremeCoreSCTrapPrefix,'extremeHealthCheckFailed':extremeHealthCheckFailed,'extremeCpuUtilizationRisingTrap':extremeCpuUtilizationRisingTrap,'extremeCpuUtilizationFallingTrap':extremeCpuUtilizationFallingTrap,'extremeProcessorStateChangeTrap':extremeProcessorStateChangeTrap,'extremeMsmFailoverTrap':extremeMsmFailoverTrap,'extremeEsrpTimedOutFailedOverMaster':extremeEsrpTimedOutFailedOverMaster,'extremeRateLimitExceededTrap':extremeRateLimitExceededTrap,_Aa:extremeRateLimitExceededTrapType,_Ab:extremeRateLimitExceededTrapIndicator,_Ac:extremeExceededByteCount,'extremeOverheatNormal':extremeOverheatNormal,'extremeBgpTraps':extremeBgpTraps,'extremeBgpTrapsPrefix':extremeBgpTrapsPrefix,'extremeBgpPrefixReachedThreshold':extremeBgpPrefixReachedThreshold,'extremeBgpPrefixMaxExceeded':extremeBgpPrefixMaxExceeded,'extremeSecurityTraps':extremeSecurityTraps,'extremeSecurityTrapsPrefix':extremeSecurityTrapsPrefix,'extremeMacLimitExceeded':extremeMacLimitExceeded,'extremeUnauthorizedPortForMacDetected':extremeUnauthorizedPortForMacDetected,'extremeMacDetectedOnLockedPort':extremeMacDetectedOnLockedPort,'extremeNetloginUserLogin':extremeNetloginUserLogin,'extremeNetloginUserLogout':extremeNetloginUserLogout,'extremeNetloginAuthFailure':extremeNetloginAuthFailure,'extremeGratuitousArpViolation':extremeGratuitousArpViolation,_Y:extremeMacSecurityVlanIfIndex,_Z:extremeMacSecurityVlanDescr,_a:extremeMacSecurityMacAddress,_b:extremeMacSecurityPortIfIndex,_c:extremeMacSecurityVlanId,_d:extremeNetloginStationMac,_e:extremeNetloginStationAddr,_f:extremeNetloginPortIfIndex,_g:extremeNetloginAuthType,_h:extremeNetloginSystemTime,_i:extremeNetloginUser,_j:extremeNetloginSrcVlan,_k:extremeNetloginDestVlan,_l:extremeNetloginSessionStatus,_Ae:extremeArpSecurityVlanIfIndex,_Af:extremeArpSecurityVlanDescr,_Ag:extremeArpSecurityPortIfIndex,_Ah:extremeArpSecurityIpAddr,_Ai:extremeArpSecurityMacAddress,_Ad:extremeNetloginAuthDataBase,_m:extremeNetloginMoveFromVlanList,_n:extremeNetloginMoveToVlanList,'extremeNMSTraps':extremeNMSTraps,'extremeNMSTrapsPrefix':extremeNMSTrapsPrefix,'extremeNMSInventoryChanged':extremeNMSInventoryChanged,'extremeNMSTopologyChanged':extremeNMSTopologyChanged,_Aj:extremeNMSDeviceAddress,'extremeElrpTraps':extremeElrpTraps,'extremeElrpTrapsPrefix':extremeElrpTrapsPrefix,'extremeElrpVlanLoopDetected':extremeElrpVlanLoopDetected,'extremeEapsTraps':extremeEapsTraps,'extremeEapsTrapsPrefix':extremeEapsTrapsPrefix,'extremeEapsStateChange':extremeEapsStateChange,'extremeEapsFailTimerExpFlagSet':extremeEapsFailTimerExpFlagSet,'extremeEapsFailTimerExpFlagClear':extremeEapsFailTimerExpFlagClear,'extremeEapsLinkDownRingComplete':extremeEapsLinkDownRingComplete,'extremeEapsPortStatusChange':extremeEapsPortStatusChange,'extremeEapsConfigChange':extremeEapsConfigChange,'extremeEapsLastStatusChangeTime':extremeEapsLastStatusChangeTime,'extremeBgpM2Traps':extremeBgpM2Traps,'extremeBgpM2TrapsPrefix':extremeBgpM2TrapsPrefix,'extremeBgpM2PrefixReachedThreshold':extremeBgpM2PrefixReachedThreshold,'extremeBgpM2PrefixMaxExceeded':extremeBgpM2PrefixMaxExceeded,'extremeEapsSharedLinkTraps':extremeEapsSharedLinkTraps,'extremeEapsSharedLinkTrapsPrefix':extremeEapsSharedLinkTrapsPrefix,'extremeEapsSegmentTimerExpFlagSet':extremeEapsSegmentTimerExpFlagSet,'extremeEapsSegmentTimerExpFlagClear':extremeEapsSegmentTimerExpFlagClear,'extremeEapsSharedPortStateChange':extremeEapsSharedPortStateChange,'extremeEapsRootBlockerStatusChange':extremeEapsRootBlockerStatusChange,_AB:extremeSegmentPort,_AC:extremeSharedPort,'extremePethTraps':extremePethTraps,'extremePethNotificationPrefix':extremePethNotificationPrefix,'extremePethPSUStatusNotification':extremePethPSUStatusNotification,'extremeLacpTraps':extremeLacpTraps,'extremeLacpNotificationPrefix':extremeLacpNotificationPrefix,'extremeLacpAddPortToAggregator':extremeLacpAddPortToAggregator,'extremeLacpDeletePortFromAggregator':extremeLacpDeletePortFromAggregator})