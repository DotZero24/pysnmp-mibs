_A9='hpSwitchStpErrantBpduDetector'
_A8='hpSwitchStpErrantBpduSrcMac'
_A7='hpSwitchStpPortErrantBpduCounter'
_A6='hpSwitchTrunkIndex'
_A5='hpSwitchDSCPRateLimitIndex'
_A4='hpSwitchRateLimitPortIndex'
_A3='hpSwitchBWMinEgressPortIndex'
_A2='hpSwitchPortIsolationPort'
_A1='hpSwitchQueueWatchPort'
_A0='hpSwitchCosAppTypeConfigIndex'
_z='hpSwitchCosDSCPPolicyIndex'
_y='hpSwitchCosTosIndex'
_x='hpSwitchCosAddressIndex'
_w='hpSwitchCosProtocolType'
_v='hpSwitchCosVlanIndex'
_u='noPolicyOverride'
_t='hpSwitchCosPortIndex'
_s='hpSwitchIgmpPortIndex2'
_r='hpSwitchIgmpPortVlanIndex2'
_q='forward'
_p='blocked'
_o='hpSwitchIgmpPortIndex'
_n='hpSwitchIgmpVlanIndex'
_m='uplink'
_l='hpSwitchStpVlan'
_k='hpSwitchABCConfigVlan'
_j='hpSwitchFddiIpFragConfigIndex'
_i='hpSwitchFilterIndex'
_h='inactive'
_g='notSupported'
_f='automdix'
_e='not-applicable'
_d='passive'
_c='accessible-for-notify'
_b='DisplayString'
_a='Unsigned32'
_Z='NotificationType'
_Y='dot1dStpPortState'
_X='dot1dStpPortDesignatedPort'
_W='dot1dStpPortDesignatedBridge'
_V='enabled'
_U='hpSwitchStpPort'
_T='hpSwitchPortIndex'
_S='not-accessible'
_R='active'
_Q='BRIDGE-MIB'
_P='none'
_O='Bits'
_N='microseconds'
_M='TruthValue'
_L='disabled'
_K='OctetString'
_J='obsolete'
_I='optional'
_H='deprecated'
_G='CONFIG-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPortDesignatedBridge,dot1dStpPortDesignatedPort,dot1dStpPortState=mibBuilder.importSymbols(_Q,_W,_X,_Y)
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
HpPartnerDeviceType,HpPartnerDeviceTypeList=mibBuilder.importSymbols('HP-ICF-DEV-CONF-MIB','HpPartnerDeviceType','HpPartnerDeviceTypeList')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ConfigStatus,HpSwitchIfMauAutoNegCapAdvertisedBits,HpSwitchIfMauAutoNegCapReceivedBits,HpSwitchIfMauAutoNegCapabilityBits,HpSwitchIfMauTypeListBits,HpSwitchPortType=mibBuilder.importSymbols('HP-ICF-TC','ConfigStatus','HpSwitchIfMauAutoNegCapAdvertisedBits','HpSwitchIfMauAutoNegCapReceivedBits','HpSwitchIfMauAutoNegCapabilityBits','HpSwitchIfMauTypeListBits','HpSwitchPortType')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_Z,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'TimeTicks',_a,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_M)
class VlanID(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class Timeout(Integer32):0
class HpicfUsrProfilePortSpeed(TextualConvention,Integer32):status='current';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('speed10HDX',1),('speed100HDX',2),('speed10FDx',3),('speed100FDx',4),('speedAuto',5),('speed1000FDx',6),('speedAuto10Mbits',7),('speedAuto100Mbits',8),('speedAuto1000Mbits',9),('speedAuto-10Gbits',10),('speedAuto10or100Mbits',11)))
_HpConfig_ObjectIdentity=ObjectIdentity
hpConfig=_HpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7))
_HpSwitchConfig_ObjectIdentity=ObjectIdentity
hpSwitchConfig=_HpSwitchConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1))
_HpSwitchTraps_ObjectIdentity=ObjectIdentity
hpSwitchTraps=_HpSwitchTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,0))
_HpSwitchTrapsObjects_ObjectIdentity=ObjectIdentity
hpSwitchTrapsObjects=_HpSwitchTrapsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,0,1))
class _HpSwitchStpErrantBpduDetector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bpduFilter',1),('bpduProtection',2),('pvstFilter',3),('pvstProtection',4)))
_HpSwitchStpErrantBpduDetector_Type.__name__=_B
_HpSwitchStpErrantBpduDetector_Object=MibScalar
hpSwitchStpErrantBpduDetector=_HpSwitchStpErrantBpduDetector_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,0,1,1),_HpSwitchStpErrantBpduDetector_Type())
hpSwitchStpErrantBpduDetector.setMaxAccess(_c)
if mibBuilder.loadTexts:hpSwitchStpErrantBpduDetector.setStatus(_I)
_HpSwitchStpErrantBpduSrcMac_Type=MacAddress
_HpSwitchStpErrantBpduSrcMac_Object=MibScalar
hpSwitchStpErrantBpduSrcMac=_HpSwitchStpErrantBpduSrcMac_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,0,1,2),_HpSwitchStpErrantBpduSrcMac_Type())
hpSwitchStpErrantBpduSrcMac.setMaxAccess(_c)
if mibBuilder.loadTexts:hpSwitchStpErrantBpduSrcMac.setStatus(_I)
_HpSwitchSystemConfig_ObjectIdentity=ObjectIdentity
hpSwitchSystemConfig=_HpSwitchSystemConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1))
class _HpSwitchAutoReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('yes',1),('no',2),('useHw',3)))
_HpSwitchAutoReboot_Type.__name__=_B
_HpSwitchAutoReboot_Object=MibScalar
hpSwitchAutoReboot=_HpSwitchAutoReboot_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,1),_HpSwitchAutoReboot_Type())
hpSwitchAutoReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAutoReboot.setStatus(_A)
class _HpSwitchTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,840))
_HpSwitchTimeZone_Type.__name__=_B
_HpSwitchTimeZone_Object=MibScalar
hpSwitchTimeZone=_HpSwitchTimeZone_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,2),_HpSwitchTimeZone_Type())
hpSwitchTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTimeZone.setStatus(_A)
class _HpSwitchDaylightTimeRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,1),('alaska',2),('canadaAndContinentalUS',3),('middleEuropeAndPortugal',4),('southernHemisphere',5),('westernEurop',6),('userDefined',7)))
_HpSwitchDaylightTimeRule_Type.__name__=_B
_HpSwitchDaylightTimeRule_Object=MibScalar
hpSwitchDaylightTimeRule=_HpSwitchDaylightTimeRule_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,3),_HpSwitchDaylightTimeRule_Type())
hpSwitchDaylightTimeRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDaylightTimeRule.setStatus(_A)
class _HpSwitchDaylightBeginningMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HpSwitchDaylightBeginningMonth_Type.__name__=_B
_HpSwitchDaylightBeginningMonth_Object=MibScalar
hpSwitchDaylightBeginningMonth=_HpSwitchDaylightBeginningMonth_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,4),_HpSwitchDaylightBeginningMonth_Type())
hpSwitchDaylightBeginningMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDaylightBeginningMonth.setStatus(_A)
class _HpSwitchDaylightBeginningDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_HpSwitchDaylightBeginningDay_Type.__name__=_B
_HpSwitchDaylightBeginningDay_Object=MibScalar
hpSwitchDaylightBeginningDay=_HpSwitchDaylightBeginningDay_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,5),_HpSwitchDaylightBeginningDay_Type())
hpSwitchDaylightBeginningDay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDaylightBeginningDay.setStatus(_A)
class _HpSwitchDaylightEndingMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HpSwitchDaylightEndingMonth_Type.__name__=_B
_HpSwitchDaylightEndingMonth_Object=MibScalar
hpSwitchDaylightEndingMonth=_HpSwitchDaylightEndingMonth_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,6),_HpSwitchDaylightEndingMonth_Type())
hpSwitchDaylightEndingMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDaylightEndingMonth.setStatus(_A)
class _HpSwitchDaylightEndingDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_HpSwitchDaylightEndingDay_Type.__name__=_B
_HpSwitchDaylightEndingDay_Object=MibScalar
hpSwitchDaylightEndingDay=_HpSwitchDaylightEndingDay_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,7),_HpSwitchDaylightEndingDay_Type())
hpSwitchDaylightEndingDay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDaylightEndingDay.setStatus(_A)
_HpSwitchSystemConfigStatus_Type=ConfigStatus
_HpSwitchSystemConfigStatus_Object=MibScalar
hpSwitchSystemConfigStatus=_HpSwitchSystemConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,8),_HpSwitchSystemConfigStatus_Type())
hpSwitchSystemConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSystemConfigStatus.setStatus(_A)
class _HpSwitchSystemPortLEDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link-activity',1),('link-only',2)))
_HpSwitchSystemPortLEDMode_Type.__name__=_B
_HpSwitchSystemPortLEDMode_Object=MibScalar
hpSwitchSystemPortLEDMode=_HpSwitchSystemPortLEDMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,9),_HpSwitchSystemPortLEDMode_Type())
hpSwitchSystemPortLEDMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSystemPortLEDMode.setStatus(_A)
class _HpSwitchControlUnknownIPMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchControlUnknownIPMulticast_Type.__name__=_B
_HpSwitchControlUnknownIPMulticast_Object=MibScalar
hpSwitchControlUnknownIPMulticast=_HpSwitchControlUnknownIPMulticast_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,10),_HpSwitchControlUnknownIPMulticast_Type())
hpSwitchControlUnknownIPMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchControlUnknownIPMulticast.setStatus(_A)
class _HpSwitchIgmpDelayedGroupFlushTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchIgmpDelayedGroupFlushTimer_Type.__name__=_B
_HpSwitchIgmpDelayedGroupFlushTimer_Object=MibScalar
hpSwitchIgmpDelayedGroupFlushTimer=_HpSwitchIgmpDelayedGroupFlushTimer_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,11),_HpSwitchIgmpDelayedGroupFlushTimer_Type())
hpSwitchIgmpDelayedGroupFlushTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpDelayedGroupFlushTimer.setStatus(_A)
class _HpSwitchMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchMaxFrameSize_Type.__name__=_B
_HpSwitchMaxFrameSize_Object=MibScalar
hpSwitchMaxFrameSize=_HpSwitchMaxFrameSize_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,12),_HpSwitchMaxFrameSize_Type())
hpSwitchMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMaxFrameSize.setStatus(_A)
class _HpSwitchIpMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIpMTU_Type.__name__=_B
_HpSwitchIpMTU_Object=MibScalar
hpSwitchIpMTU=_HpSwitchIpMTU_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,13),_HpSwitchIpMTU_Type())
hpSwitchIpMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpMTU.setStatus(_A)
class _HpSwitchAllowV1Modules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchAllowV1Modules_Type.__name__=_B
_HpSwitchAllowV1Modules_Object=MibScalar
hpSwitchAllowV1Modules=_HpSwitchAllowV1Modules_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,14),_HpSwitchAllowV1Modules_Type())
hpSwitchAllowV1Modules.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAllowV1Modules.setStatus(_A)
class _HpSwitchAllowV2Modules_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_E,2),('erase',3)))
_HpSwitchAllowV2Modules_Type.__name__=_B
_HpSwitchAllowV2Modules_Object=MibScalar
hpSwitchAllowV2Modules=_HpSwitchAllowV2Modules_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,15),_HpSwitchAllowV2Modules_Type())
hpSwitchAllowV2Modules.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchAllowV2Modules.setStatus(_A)
_HpicfPrivateVlanPromiscuousPorts_Type=PortList
_HpicfPrivateVlanPromiscuousPorts_Object=MibScalar
hpicfPrivateVlanPromiscuousPorts=_HpicfPrivateVlanPromiscuousPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,16),_HpicfPrivateVlanPromiscuousPorts_Type())
hpicfPrivateVlanPromiscuousPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPrivateVlanPromiscuousPorts.setStatus(_I)
class _HpSwitchPreviewMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPreviewMode_Type.__name__=_B
_HpSwitchPreviewMode_Object=MibScalar
hpSwitchPreviewMode=_HpSwitchPreviewMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,17),_HpSwitchPreviewMode_Type())
hpSwitchPreviewMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPreviewMode.setStatus(_A)
class _HpSwitchHibernate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpSwitchHibernate_Type.__name__=_B
_HpSwitchHibernate_Object=MibScalar
hpSwitchHibernate=_HpSwitchHibernate_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,18),_HpSwitchHibernate_Type())
hpSwitchHibernate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchHibernate.setStatus(_A)
class _HpSwitchMacDelimiter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('default',1),('colon',2),('hyphen',3),('ouinic',4),(_P,5)))
_HpSwitchMacDelimiter_Type.__name__=_B
_HpSwitchMacDelimiter_Object=MibScalar
hpSwitchMacDelimiter=_HpSwitchMacDelimiter_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,19),_HpSwitchMacDelimiter_Type())
hpSwitchMacDelimiter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMacDelimiter.setStatus(_A)
class _HpicfSwitchCLIOptimization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpicfSwitchCLIOptimization_Type.__name__=_B
_HpicfSwitchCLIOptimization_Object=MibScalar
hpicfSwitchCLIOptimization=_HpicfSwitchCLIOptimization_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,20),_HpicfSwitchCLIOptimization_Type())
hpicfSwitchCLIOptimization.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSwitchCLIOptimization.setStatus(_A)
class _HpicfSwitchRMONLogThreshold_Type(Unsigned32):defaultValue=80;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpicfSwitchRMONLogThreshold_Type.__name__=_a
_HpicfSwitchRMONLogThreshold_Object=MibScalar
hpicfSwitchRMONLogThreshold=_HpicfSwitchRMONLogThreshold_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,1,21),_HpicfSwitchRMONLogThreshold_Type())
hpicfSwitchRMONLogThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSwitchRMONLogThreshold.setStatus(_A)
_HpSwitchConsoleConfig_ObjectIdentity=ObjectIdentity
hpSwitchConsoleConfig=_HpSwitchConsoleConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2))
class _HpSwitchTelnetAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchTelnetAdminStatus_Type.__name__=_B
_HpSwitchTelnetAdminStatus_Object=MibScalar
hpSwitchTelnetAdminStatus=_HpSwitchTelnetAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,1),_HpSwitchTelnetAdminStatus_Type())
hpSwitchTelnetAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTelnetAdminStatus.setStatus(_J)
class _HpSwitchTerminalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('vt100',2),('ansi',4)))
_HpSwitchTerminalType_Type.__name__=_B
_HpSwitchTerminalType_Object=MibScalar
hpSwitchTerminalType=_HpSwitchTerminalType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,2),_HpSwitchTerminalType_Type())
hpSwitchTerminalType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTerminalType.setStatus(_A)
class _HpSwitchConsoleRefRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,10,20,30,45,60)));namedValues=NamedValues(*(('refRate1',1),('refRate3',3),('refRate5',5),('refRate10',10),('refRate20',20),('refRate30',30),('refRate45',45),('refRate',60)))
_HpSwitchConsoleRefRate_Type.__name__=_B
_HpSwitchConsoleRefRate_Object=MibScalar
hpSwitchConsoleRefRate=_HpSwitchConsoleRefRate_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,3),_HpSwitchConsoleRefRate_Type())
hpSwitchConsoleRefRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchConsoleRefRate.setStatus(_A)
class _HpSwitchDisplayedEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('major',2),('notInfo',3),('all',4),('debug',5)))
_HpSwitchDisplayedEvent_Type.__name__=_B
_HpSwitchDisplayedEvent_Object=MibScalar
hpSwitchDisplayedEvent=_HpSwitchDisplayedEvent_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,4),_HpSwitchDisplayedEvent_Type())
hpSwitchDisplayedEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDisplayedEvent.setStatus(_A)
_HpSwitchConsoleConfigStatus_Type=ConfigStatus
_HpSwitchConsoleConfigStatus_Object=MibScalar
hpSwitchConsoleConfigStatus=_HpSwitchConsoleConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,5),_HpSwitchConsoleConfigStatus_Type())
hpSwitchConsoleConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchConsoleConfigStatus.setStatus(_A)
class _HpSwitchConsoleConfigLogoutPrompt_Type(TruthValue):defaultValue=1
_HpSwitchConsoleConfigLogoutPrompt_Type.__name__=_M
_HpSwitchConsoleConfigLogoutPrompt_Object=MibScalar
hpSwitchConsoleConfigLogoutPrompt=_HpSwitchConsoleConfigLogoutPrompt_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,6),_HpSwitchConsoleConfigLogoutPrompt_Type())
hpSwitchConsoleConfigLogoutPrompt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchConsoleConfigLogoutPrompt.setStatus(_A)
class _HpSwitchUsbConsoleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchUsbConsoleAdminStatus_Type.__name__=_B
_HpSwitchUsbConsoleAdminStatus_Object=MibScalar
hpSwitchUsbConsoleAdminStatus=_HpSwitchUsbConsoleAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,7),_HpSwitchUsbConsoleAdminStatus_Type())
hpSwitchUsbConsoleAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchUsbConsoleAdminStatus.setStatus(_I)
class _HpSwitchSessionGlobalIdleTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_HpSwitchSessionGlobalIdleTimeout_Type.__name__=_B
_HpSwitchSessionGlobalIdleTimeout_Object=MibScalar
hpSwitchSessionGlobalIdleTimeout=_HpSwitchSessionGlobalIdleTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,8),_HpSwitchSessionGlobalIdleTimeout_Type())
hpSwitchSessionGlobalIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSessionGlobalIdleTimeout.setStatus(_A)
class _HpSwitchSessionConsoleIdleTimeout_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7200))
_HpSwitchSessionConsoleIdleTimeout_Type.__name__=_B
_HpSwitchSessionConsoleIdleTimeout_Object=MibScalar
hpSwitchSessionConsoleIdleTimeout=_HpSwitchSessionConsoleIdleTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,9),_HpSwitchSessionConsoleIdleTimeout_Type())
hpSwitchSessionConsoleIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSessionConsoleIdleTimeout.setStatus(_A)
class _HpSwitchMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_HpSwitchMaxSessions_Type.__name__=_B
_HpSwitchMaxSessions_Object=MibScalar
hpSwitchMaxSessions=_HpSwitchMaxSessions_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,10),_HpSwitchMaxSessions_Type())
hpSwitchMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMaxSessions.setStatus(_A)
class _HpSwitchMaxUserSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_HpSwitchMaxUserSessions_Type.__name__=_B
_HpSwitchMaxUserSessions_Object=MibScalar
hpSwitchMaxUserSessions=_HpSwitchMaxUserSessions_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,2,11),_HpSwitchMaxUserSessions_Type())
hpSwitchMaxUserSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMaxUserSessions.setStatus(_A)
_HpSwitchPortConfig_ObjectIdentity=ObjectIdentity
hpSwitchPortConfig=_HpSwitchPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3))
_HpSwitchPortTable_Object=MibTable
hpSwitchPortTable=_HpSwitchPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1))
if mibBuilder.loadTexts:hpSwitchPortTable.setStatus(_A)
_HpSwitchPortEntry_Object=MibTableRow
hpSwitchPortEntry=_HpSwitchPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1))
hpSwitchPortEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:hpSwitchPortEntry.setStatus(_A)
class _HpSwitchPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortIndex_Type.__name__=_B
_HpSwitchPortIndex_Object=MibTableColumn
hpSwitchPortIndex=_HpSwitchPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,1),_HpSwitchPortIndex_Type())
hpSwitchPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortIndex.setStatus(_A)
_HpSwitchPortType_Type=HpSwitchPortType
_HpSwitchPortType_Object=MibTableColumn
hpSwitchPortType=_HpSwitchPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,2),_HpSwitchPortType_Type())
hpSwitchPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortType.setStatus(_A)
class _HpSwitchPortDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchPortDescr_Type.__name__=_b
_HpSwitchPortDescr_Object=MibTableColumn
hpSwitchPortDescr=_HpSwitchPortDescr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,3),_HpSwitchPortDescr_Type())
hpSwitchPortDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortDescr.setStatus(_A)
class _HpSwitchPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortAdminStatus_Type.__name__=_B
_HpSwitchPortAdminStatus_Object=MibTableColumn
hpSwitchPortAdminStatus=_HpSwitchPortAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,4),_HpSwitchPortAdminStatus_Type())
hpSwitchPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortAdminStatus.setStatus(_J)
class _HpSwitchPortEtherMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half-duplex',1),('full-duplex',2)))
_HpSwitchPortEtherMode_Type.__name__=_B
_HpSwitchPortEtherMode_Object=MibTableColumn
hpSwitchPortEtherMode=_HpSwitchPortEtherMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,5),_HpSwitchPortEtherMode_Type())
hpSwitchPortEtherMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortEtherMode.setStatus(_A)
class _HpSwitchPortVgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('main',1),('endNode',2),('autoDetect',3)))
_HpSwitchPortVgMode_Type.__name__=_B
_HpSwitchPortVgMode_Object=MibTableColumn
hpSwitchPortVgMode=_HpSwitchPortVgMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,6),_HpSwitchPortVgMode_Type())
hpSwitchPortVgMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortVgMode.setStatus(_A)
class _HpSwitchPortLinkbeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortLinkbeat_Type.__name__=_B
_HpSwitchPortLinkbeat_Object=MibTableColumn
hpSwitchPortLinkbeat=_HpSwitchPortLinkbeat_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,7),_HpSwitchPortLinkbeat_Type())
hpSwitchPortLinkbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortLinkbeat.setStatus(_A)
class _HpSwitchPortTrunkGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchPortTrunkGroup_Type.__name__=_B
_HpSwitchPortTrunkGroup_Object=MibTableColumn
hpSwitchPortTrunkGroup=_HpSwitchPortTrunkGroup_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,8),_HpSwitchPortTrunkGroup_Type())
hpSwitchPortTrunkGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortTrunkGroup.setStatus(_A)
class _HpSwitchPortBcastLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_HpSwitchPortBcastLimit_Type.__name__=_B
_HpSwitchPortBcastLimit_Object=MibTableColumn
hpSwitchPortBcastLimit=_HpSwitchPortBcastLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,9),_HpSwitchPortBcastLimit_Type())
hpSwitchPortBcastLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortBcastLimit.setStatus(_A)
class _HpSwitchPortFastEtherMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('half-duplex-10Mbits',1),('half-duplex-100Mbits',2),('full-duplex-10Mbits',3),('full-duplex-100Mbits',4),('auto-neg',5),('full-duplex-1000Mbits',6),('auto-10Mbits',7),('auto-100Mbits',8),('auto-1000Mbits',9),('auto-10Gbits',10),('auto-10-100Mbits',11),('auto-40Gbits',12),('auto-2500Mbits',13),('auto-5000Mbits',14),('auto-2500-5000Mbits',15),('auto-1000-2500Mbits',16),('auto-1000-2500-5000Mbits',17)))
_HpSwitchPortFastEtherMode_Type.__name__=_B
_HpSwitchPortFastEtherMode_Object=MibTableColumn
hpSwitchPortFastEtherMode=_HpSwitchPortFastEtherMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,10),_HpSwitchPortFastEtherMode_Type())
hpSwitchPortFastEtherMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortFastEtherMode.setStatus(_A)
class _HpSwitchPortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_HpSwitchPortFlowControl_Type.__name__=_B
_HpSwitchPortFlowControl_Object=MibTableColumn
hpSwitchPortFlowControl=_HpSwitchPortFlowControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,11),_HpSwitchPortFlowControl_Type())
hpSwitchPortFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortFlowControl.setStatus(_A)
class _HpSwitchPortTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('trunk',1),('fecAuto',2),('saTrunk',3),('lacpTrk',4),(_P,5),('dtLacpTrk',6),('dtTrunk',7)))
_HpSwitchPortTrunkType_Type.__name__=_B
_HpSwitchPortTrunkType_Object=MibTableColumn
hpSwitchPortTrunkType=_HpSwitchPortTrunkType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,13),_HpSwitchPortTrunkType_Type())
hpSwitchPortTrunkType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortTrunkType.setStatus(_A)
class _HpSwitchPortTrunkLACPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_R,2),(_d,3)))
_HpSwitchPortTrunkLACPStatus_Type.__name__=_B
_HpSwitchPortTrunkLACPStatus_Object=MibTableColumn
hpSwitchPortTrunkLACPStatus=_HpSwitchPortTrunkLACPStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,14),_HpSwitchPortTrunkLACPStatus_Type())
hpSwitchPortTrunkLACPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortTrunkLACPStatus.setStatus(_A)
class _HpSwitchPortMDIXStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('mdi',2),('mdix',3),(_f,4)))
_HpSwitchPortMDIXStatus_Type.__name__=_B
_HpSwitchPortMDIXStatus_Object=MibTableColumn
hpSwitchPortMDIXStatus=_HpSwitchPortMDIXStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,15),_HpSwitchPortMDIXStatus_Type())
hpSwitchPortMDIXStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortMDIXStatus.setStatus(_A)
class _HpSwitchPortAutoMDIX_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),('mdi',2),('mdix',3),(_f,4)))
_HpSwitchPortAutoMDIX_Type.__name__=_B
_HpSwitchPortAutoMDIX_Object=MibTableColumn
hpSwitchPortAutoMDIX=_HpSwitchPortAutoMDIX_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,16),_HpSwitchPortAutoMDIX_Type())
hpSwitchPortAutoMDIX.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortAutoMDIX.setStatus(_A)
class _HpSwitchPortLACPKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchPortLACPKey_Type.__name__=_B
_HpSwitchPortLACPKey_Object=MibTableColumn
hpSwitchPortLACPKey=_HpSwitchPortLACPKey_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,17),_HpSwitchPortLACPKey_Type())
hpSwitchPortLACPKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortLACPKey.setStatus(_A)
class _HpSwitchPortTrafficTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchPortTrafficTemplateName_Type.__name__=_K
_HpSwitchPortTrafficTemplateName_Object=MibTableColumn
hpSwitchPortTrafficTemplateName=_HpSwitchPortTrafficTemplateName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,18),_HpSwitchPortTrafficTemplateName_Type())
hpSwitchPortTrafficTemplateName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortTrafficTemplateName.setStatus(_A)
class _HpSwitchPortEEEAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortEEEAdminStatus_Type.__name__=_B
_HpSwitchPortEEEAdminStatus_Object=MibTableColumn
hpSwitchPortEEEAdminStatus=_HpSwitchPortEEEAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,19),_HpSwitchPortEEEAdminStatus_Type())
hpSwitchPortEEEAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortEEEAdminStatus.setStatus(_A)
class _HpSwitchPortEEEOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_R,2),(_h,3)))
_HpSwitchPortEEEOperStatus_Type.__name__=_B
_HpSwitchPortEEEOperStatus_Object=MibTableColumn
hpSwitchPortEEEOperStatus=_HpSwitchPortEEEOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,20),_HpSwitchPortEEEOperStatus_Type())
hpSwitchPortEEEOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEEOperStatus.setStatus(_A)
class _HpSwitchPortEEECurrentTwSysTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortEEECurrentTwSysTx_Type.__name__=_B
_HpSwitchPortEEECurrentTwSysTx_Object=MibTableColumn
hpSwitchPortEEECurrentTwSysTx=_HpSwitchPortEEECurrentTwSysTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,21),_HpSwitchPortEEECurrentTwSysTx_Type())
hpSwitchPortEEECurrentTwSysTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEECurrentTwSysTx.setStatus(_H)
if mibBuilder.loadTexts:hpSwitchPortEEECurrentTwSysTx.setUnits(_N)
class _HpSwitchPortEEEMinTwSysTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortEEEMinTwSysTx_Type.__name__=_B
_HpSwitchPortEEEMinTwSysTx_Object=MibTableColumn
hpSwitchPortEEEMinTwSysTx=_HpSwitchPortEEEMinTwSysTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,22),_HpSwitchPortEEEMinTwSysTx_Type())
hpSwitchPortEEEMinTwSysTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEEMinTwSysTx.setStatus(_H)
if mibBuilder.loadTexts:hpSwitchPortEEEMinTwSysTx.setUnits(_N)
class _HpSwitchPortEEEMaxTwSysTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortEEEMaxTwSysTx_Type.__name__=_B
_HpSwitchPortEEEMaxTwSysTx_Object=MibTableColumn
hpSwitchPortEEEMaxTwSysTx=_HpSwitchPortEEEMaxTwSysTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,23),_HpSwitchPortEEEMaxTwSysTx_Type())
hpSwitchPortEEEMaxTwSysTx.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEEMaxTwSysTx.setStatus(_H)
if mibBuilder.loadTexts:hpSwitchPortEEEMaxTwSysTx.setUnits(_N)
class _HpSwitchPortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_HpSwitchPortPvid_Type.__name__=_B
_HpSwitchPortPvid_Object=MibTableColumn
hpSwitchPortPvid=_HpSwitchPortPvid_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,25),_HpSwitchPortPvid_Type())
hpSwitchPortPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortPvid.setStatus(_A)
class _HpSwitchPortTaggedVlanMap1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpSwitchPortTaggedVlanMap1k_Type.__name__=_K
_HpSwitchPortTaggedVlanMap1k_Object=MibTableColumn
hpSwitchPortTaggedVlanMap1k=_HpSwitchPortTaggedVlanMap1k_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,26),_HpSwitchPortTaggedVlanMap1k_Type())
hpSwitchPortTaggedVlanMap1k.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortTaggedVlanMap1k.setStatus(_A)
class _HpSwitchPortTaggedVlanMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpSwitchPortTaggedVlanMap2k_Type.__name__=_K
_HpSwitchPortTaggedVlanMap2k_Object=MibTableColumn
hpSwitchPortTaggedVlanMap2k=_HpSwitchPortTaggedVlanMap2k_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,27),_HpSwitchPortTaggedVlanMap2k_Type())
hpSwitchPortTaggedVlanMap2k.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortTaggedVlanMap2k.setStatus(_A)
class _HpSwitchPortTaggedVlanMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpSwitchPortTaggedVlanMap3k_Type.__name__=_K
_HpSwitchPortTaggedVlanMap3k_Object=MibTableColumn
hpSwitchPortTaggedVlanMap3k=_HpSwitchPortTaggedVlanMap3k_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,28),_HpSwitchPortTaggedVlanMap3k_Type())
hpSwitchPortTaggedVlanMap3k.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortTaggedVlanMap3k.setStatus(_A)
class _HpSwitchPortTaggedVlanMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_HpSwitchPortTaggedVlanMap4k_Type.__name__=_K
_HpSwitchPortTaggedVlanMap4k_Object=MibTableColumn
hpSwitchPortTaggedVlanMap4k=_HpSwitchPortTaggedVlanMap4k_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,29),_HpSwitchPortTaggedVlanMap4k_Type())
hpSwitchPortTaggedVlanMap4k.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortTaggedVlanMap4k.setStatus(_A)
class _HpSwitchPortEEECurrentTwSysTx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchPortEEECurrentTwSysTx1_Type.__name__=_B
_HpSwitchPortEEECurrentTwSysTx1_Object=MibTableColumn
hpSwitchPortEEECurrentTwSysTx1=_HpSwitchPortEEECurrentTwSysTx1_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,30),_HpSwitchPortEEECurrentTwSysTx1_Type())
hpSwitchPortEEECurrentTwSysTx1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEECurrentTwSysTx1.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchPortEEECurrentTwSysTx1.setUnits(_N)
class _HpSwitchPortEEEMinTwSysTx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchPortEEEMinTwSysTx1_Type.__name__=_B
_HpSwitchPortEEEMinTwSysTx1_Object=MibTableColumn
hpSwitchPortEEEMinTwSysTx1=_HpSwitchPortEEEMinTwSysTx1_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,31),_HpSwitchPortEEEMinTwSysTx1_Type())
hpSwitchPortEEEMinTwSysTx1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEEMinTwSysTx1.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchPortEEEMinTwSysTx1.setUnits(_N)
class _HpSwitchPortEEEMaxTwSysTx1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchPortEEEMaxTwSysTx1_Type.__name__=_B
_HpSwitchPortEEEMaxTwSysTx1_Object=MibTableColumn
hpSwitchPortEEEMaxTwSysTx1=_HpSwitchPortEEEMaxTwSysTx1_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,32),_HpSwitchPortEEEMaxTwSysTx1_Type())
hpSwitchPortEEEMaxTwSysTx1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortEEEMaxTwSysTx1.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchPortEEEMaxTwSysTx1.setUnits(_N)
class _HpSwitchPortPtpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortPtpAdminStatus_Type.__name__=_B
_HpSwitchPortPtpAdminStatus_Object=MibTableColumn
hpSwitchPortPtpAdminStatus=_HpSwitchPortPtpAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,35),_HpSwitchPortPtpAdminStatus_Type())
hpSwitchPortPtpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortPtpAdminStatus.setStatus(_A)
class _HpSwitchPortPtpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_R,2),(_h,3)))
_HpSwitchPortPtpOperStatus_Type.__name__=_B
_HpSwitchPortPtpOperStatus_Object=MibTableColumn
hpSwitchPortPtpOperStatus=_HpSwitchPortPtpOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,36),_HpSwitchPortPtpOperStatus_Type())
hpSwitchPortPtpOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortPtpOperStatus.setStatus(_A)
_HpSwitchPortPtpRxCount_Type=Counter32
_HpSwitchPortPtpRxCount_Object=MibTableColumn
hpSwitchPortPtpRxCount=_HpSwitchPortPtpRxCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,37),_HpSwitchPortPtpRxCount_Type())
hpSwitchPortPtpRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortPtpRxCount.setStatus(_A)
_HpSwitchPortPtpTxCount_Type=Counter32
_HpSwitchPortPtpTxCount_Object=MibTableColumn
hpSwitchPortPtpTxCount=_HpSwitchPortPtpTxCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,1,1,38),_HpSwitchPortPtpTxCount_Type())
hpSwitchPortPtpTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortPtpTxCount.setStatus(_A)
_HpSwitchPortConfigStatus_Type=ConfigStatus
_HpSwitchPortConfigStatus_Object=MibScalar
hpSwitchPortConfigStatus=_HpSwitchPortConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,2),_HpSwitchPortConfigStatus_Type())
hpSwitchPortConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchPortConfigStatus.setStatus(_A)
class _HpSwitchLinkUpDownTrapAllPortsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchLinkUpDownTrapAllPortsStatus_Type.__name__=_B
_HpSwitchLinkUpDownTrapAllPortsStatus_Object=MibScalar
hpSwitchLinkUpDownTrapAllPortsStatus=_HpSwitchLinkUpDownTrapAllPortsStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,3),_HpSwitchLinkUpDownTrapAllPortsStatus_Type())
hpSwitchLinkUpDownTrapAllPortsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLinkUpDownTrapAllPortsStatus.setStatus(_A)
_HpSwitchPortDevTypeTable_Object=MibTable
hpSwitchPortDevTypeTable=_HpSwitchPortDevTypeTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,4))
if mibBuilder.loadTexts:hpSwitchPortDevTypeTable.setStatus(_A)
_HpSwitchPortDevTypeEntry_Object=MibTableRow
hpSwitchPortDevTypeEntry=_HpSwitchPortDevTypeEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,4,1))
hpSwitchPortDevTypeEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:hpSwitchPortDevTypeEntry.setStatus(_A)
class _HpSwitchPortDevTypeNetworkDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortDevTypeNetworkDevice_Type.__name__=_B
_HpSwitchPortDevTypeNetworkDevice_Object=MibTableColumn
hpSwitchPortDevTypeNetworkDevice=_HpSwitchPortDevTypeNetworkDevice_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,3,4,1,2),_HpSwitchPortDevTypeNetworkDevice_Type())
hpSwitchPortDevTypeNetworkDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortDevTypeNetworkDevice.setStatus(_A)
_HpSwitchIpxConfig_ObjectIdentity=ObjectIdentity
hpSwitchIpxConfig=_HpSwitchIpxConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,4))
_HpSwitchIpxConfigStatus_Type=ConfigStatus
_HpSwitchIpxConfigStatus_Object=MibScalar
hpSwitchIpxConfigStatus=_HpSwitchIpxConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,4,2),_HpSwitchIpxConfigStatus_Type())
hpSwitchIpxConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIpxConfigStatus.setStatus(_A)
_HpSwitchIpConfig_ObjectIdentity=ObjectIdentity
hpSwitchIpConfig=_HpSwitchIpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5))
class _HpSwitchIpTimepAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),(_E,2),('dhcp',3)))
_HpSwitchIpTimepAdminStatus_Type.__name__=_B
_HpSwitchIpTimepAdminStatus_Object=MibScalar
hpSwitchIpTimepAdminStatus=_HpSwitchIpTimepAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,1),_HpSwitchIpTimepAdminStatus_Type())
hpSwitchIpTimepAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepAdminStatus.setStatus(_A)
_HpSwitchIpTimepServerAddr_Type=IpAddress
_HpSwitchIpTimepServerAddr_Object=MibScalar
hpSwitchIpTimepServerAddr=_HpSwitchIpTimepServerAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,2),_HpSwitchIpTimepServerAddr_Type())
hpSwitchIpTimepServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepServerAddr.setStatus(_H)
class _HpSwitchIpTimepPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIpTimepPollInterval_Type.__name__=_B
_HpSwitchIpTimepPollInterval_Object=MibScalar
hpSwitchIpTimepPollInterval=_HpSwitchIpTimepPollInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,3),_HpSwitchIpTimepPollInterval_Type())
hpSwitchIpTimepPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepPollInterval.setStatus(_A)
_HpSwitchIpConfigStatus_Type=ConfigStatus
_HpSwitchIpConfigStatus_Object=MibScalar
hpSwitchIpConfigStatus=_HpSwitchIpConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,5),_HpSwitchIpConfigStatus_Type())
hpSwitchIpConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIpConfigStatus.setStatus(_J)
class _HpSwitchIpTftpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('secure',1),('unsecure',2)))
_HpSwitchIpTftpMode_Type.__name__=_B
_HpSwitchIpTftpMode_Object=MibScalar
hpSwitchIpTftpMode=_HpSwitchIpTftpMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,6),_HpSwitchIpTftpMode_Type())
hpSwitchIpTftpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTftpMode.setStatus(_J)
_HpSwitchIpTimepInetServerAddrType_Type=InetAddressType
_HpSwitchIpTimepInetServerAddrType_Object=MibScalar
hpSwitchIpTimepInetServerAddrType=_HpSwitchIpTimepInetServerAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,7),_HpSwitchIpTimepInetServerAddrType_Type())
hpSwitchIpTimepInetServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepInetServerAddrType.setStatus(_A)
_HpSwitchIpTimepInetServerAddr_Type=InetAddress
_HpSwitchIpTimepInetServerAddr_Object=MibScalar
hpSwitchIpTimepInetServerAddr=_HpSwitchIpTimepInetServerAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,8),_HpSwitchIpTimepInetServerAddr_Type())
hpSwitchIpTimepInetServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepInetServerAddr.setStatus(_A)
class _HpSwitchIpTimepIsOobm_Type(TruthValue):defaultValue=2
_HpSwitchIpTimepIsOobm_Type.__name__=_M
_HpSwitchIpTimepIsOobm_Object=MibScalar
hpSwitchIpTimepIsOobm=_HpSwitchIpTimepIsOobm_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,5,9),_HpSwitchIpTimepIsOobm_Type())
hpSwitchIpTimepIsOobm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIpTimepIsOobm.setStatus(_A)
_HpSwitchSerialLinkConfig_ObjectIdentity=ObjectIdentity
hpSwitchSerialLinkConfig=_HpSwitchSerialLinkConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6))
class _HpSwitchSLinkBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('speedSense',1),('baudRate300',2),('baudRate600',3),('baudRate1200',4),('baudRate2400',5),('baudRate4800',6),('baudRate9600',7),('baudRate19200',8),('baudRate38400',9),('baudRate57600',10),('baudRate115200',11)))
_HpSwitchSLinkBaudRate_Type.__name__=_B
_HpSwitchSLinkBaudRate_Object=MibScalar
hpSwitchSLinkBaudRate=_HpSwitchSLinkBaudRate_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,1),_HpSwitchSLinkBaudRate_Type())
hpSwitchSLinkBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkBaudRate.setStatus(_A)
class _HpSwitchSLinkFlowCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('xonXoff',2),('robustXonXoff',3)))
_HpSwitchSLinkFlowCtrl_Type.__name__=_B
_HpSwitchSLinkFlowCtrl_Object=MibScalar
hpSwitchSLinkFlowCtrl=_HpSwitchSLinkFlowCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,2),_HpSwitchSLinkFlowCtrl_Type())
hpSwitchSLinkFlowCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkFlowCtrl.setStatus(_A)
class _HpSwitchSLinkConnInactTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_HpSwitchSLinkConnInactTime_Type.__name__=_B
_HpSwitchSLinkConnInactTime_Object=MibScalar
hpSwitchSLinkConnInactTime=_HpSwitchSLinkConnInactTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,3),_HpSwitchSLinkConnInactTime_Type())
hpSwitchSLinkConnInactTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkConnInactTime.setStatus(_H)
class _HpSwitchSLinkModemConnTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HpSwitchSLinkModemConnTime_Type.__name__=_B
_HpSwitchSLinkModemConnTime_Object=MibScalar
hpSwitchSLinkModemConnTime=_HpSwitchSLinkModemConnTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,4),_HpSwitchSLinkModemConnTime_Type())
hpSwitchSLinkModemConnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkModemConnTime.setStatus(_A)
class _HpSwitchSLinkModemLostRecvTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_HpSwitchSLinkModemLostRecvTime_Type.__name__=_B
_HpSwitchSLinkModemLostRecvTime_Object=MibScalar
hpSwitchSLinkModemLostRecvTime=_HpSwitchSLinkModemLostRecvTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,5),_HpSwitchSLinkModemLostRecvTime_Type())
hpSwitchSLinkModemLostRecvTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkModemLostRecvTime.setStatus(_A)
class _HpSwitchSLinkModemDisConnTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HpSwitchSLinkModemDisConnTime_Type.__name__=_B
_HpSwitchSLinkModemDisConnTime_Object=MibScalar
hpSwitchSLinkModemDisConnTime=_HpSwitchSLinkModemDisConnTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,6),_HpSwitchSLinkModemDisConnTime_Type())
hpSwitchSLinkModemDisConnTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSLinkModemDisConnTime.setStatus(_A)
class _HpSwitchSLinkParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('parityNone',1),('parityOdd',2),('parityEven',3)))
_HpSwitchSLinkParity_Type.__name__=_B
_HpSwitchSLinkParity_Object=MibScalar
hpSwitchSLinkParity=_HpSwitchSLinkParity_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,7),_HpSwitchSLinkParity_Type())
hpSwitchSLinkParity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSLinkParity.setStatus(_A)
class _HpSwitchSLinkCharBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('char8Bits',1),('char7Bits',2)))
_HpSwitchSLinkCharBits_Type.__name__=_B
_HpSwitchSLinkCharBits_Object=MibScalar
hpSwitchSLinkCharBits=_HpSwitchSLinkCharBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,8),_HpSwitchSLinkCharBits_Type())
hpSwitchSLinkCharBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSLinkCharBits.setStatus(_A)
class _HpSwitchSLinkStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stop1Bits',1),('stop1andHalfBits',2),('stop2Bits',3)))
_HpSwitchSLinkStopBits_Type.__name__=_B
_HpSwitchSLinkStopBits_Object=MibScalar
hpSwitchSLinkStopBits=_HpSwitchSLinkStopBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,9),_HpSwitchSLinkStopBits_Type())
hpSwitchSLinkStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSLinkStopBits.setStatus(_A)
_HpSwitchSLinkConfigStatus_Type=ConfigStatus
_HpSwitchSLinkConfigStatus_Object=MibScalar
hpSwitchSLinkConfigStatus=_HpSwitchSLinkConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,6,10),_HpSwitchSLinkConfigStatus_Type())
hpSwitchSLinkConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchSLinkConfigStatus.setStatus(_A)
_HpSwitchFilterConfig_ObjectIdentity=ObjectIdentity
hpSwitchFilterConfig=_HpSwitchFilterConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8))
_HpSwitchFilterConfigTable_Object=MibTable
hpSwitchFilterConfigTable=_HpSwitchFilterConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1))
if mibBuilder.loadTexts:hpSwitchFilterConfigTable.setStatus(_A)
_HpSwitchFilterConfigEntry_Object=MibTableRow
hpSwitchFilterConfigEntry=_HpSwitchFilterConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1))
hpSwitchFilterConfigEntry.setIndexNames((0,_G,_i))
if mibBuilder.loadTexts:hpSwitchFilterConfigEntry.setStatus(_A)
class _HpSwitchFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFilterIndex_Type.__name__=_B
_HpSwitchFilterIndex_Object=MibTableColumn
hpSwitchFilterIndex=_HpSwitchFilterIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,1),_HpSwitchFilterIndex_Type())
hpSwitchFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchFilterIndex.setStatus(_A)
class _HpSwitchFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('multicast',1),('level-3',2),('port',3),('unicast',4)))
_HpSwitchFilterType_Type.__name__=_B
_HpSwitchFilterType_Object=MibTableColumn
hpSwitchFilterType=_HpSwitchFilterType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,2),_HpSwitchFilterType_Type())
hpSwitchFilterType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterType.setStatus(_A)
class _HpSwitchFilterSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFilterSrcPort_Type.__name__=_B
_HpSwitchFilterSrcPort_Object=MibTableColumn
hpSwitchFilterSrcPort=_HpSwitchFilterSrcPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,3),_HpSwitchFilterSrcPort_Type())
hpSwitchFilterSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterSrcPort.setStatus(_A)
_HpSwitchFilterMacAddr_Type=MacAddress
_HpSwitchFilterMacAddr_Object=MibTableColumn
hpSwitchFilterMacAddr=_HpSwitchFilterMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,4),_HpSwitchFilterMacAddr_Type())
hpSwitchFilterMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterMacAddr.setStatus(_A)
class _HpSwitchFilterProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFilterProtocolType_Type.__name__=_B
_HpSwitchFilterProtocolType_Object=MibTableColumn
hpSwitchFilterProtocolType=_HpSwitchFilterProtocolType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,5),_HpSwitchFilterProtocolType_Type())
hpSwitchFilterProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterProtocolType.setStatus(_A)
_HpSwitchFilterPortMask_Type=OctetString
_HpSwitchFilterPortMask_Object=MibTableColumn
hpSwitchFilterPortMask=_HpSwitchFilterPortMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,6),_HpSwitchFilterPortMask_Type())
hpSwitchFilterPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterPortMask.setStatus(_A)
_HpSwitchFilterEntryStatus_Type=RowStatus
_HpSwitchFilterEntryStatus_Object=MibTableColumn
hpSwitchFilterEntryStatus=_HpSwitchFilterEntryStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,7),_HpSwitchFilterEntryStatus_Type())
hpSwitchFilterEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterEntryStatus.setStatus(_A)
_HpSwitchFilterName_Type=DisplayString
_HpSwitchFilterName_Object=MibTableColumn
hpSwitchFilterName=_HpSwitchFilterName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,8,1,1,8),_HpSwitchFilterName_Type())
hpSwitchFilterName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFilterName.setStatus(_A)
_HpSwitchProbeConfig_ObjectIdentity=ObjectIdentity
hpSwitchProbeConfig=_HpSwitchProbeConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9))
class _HpSwitchProbeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ports',1),('vlan',2)))
_HpSwitchProbeType_Type.__name__=_B
_HpSwitchProbeType_Object=MibScalar
hpSwitchProbeType=_HpSwitchProbeType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9,1),_HpSwitchProbeType_Type())
hpSwitchProbeType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProbeType.setStatus(_J)
_HpSwitchProbedVlanId_Type=VlanID
_HpSwitchProbedVlanId_Object=MibScalar
hpSwitchProbedVlanId=_HpSwitchProbedVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9,2),_HpSwitchProbedVlanId_Type())
hpSwitchProbedVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProbedVlanId.setStatus(_J)
class _HpSwitchProbePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchProbePort_Type.__name__=_B
_HpSwitchProbePort_Object=MibScalar
hpSwitchProbePort=_HpSwitchProbePort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9,3),_HpSwitchProbePort_Type())
hpSwitchProbePort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProbePort.setStatus(_J)
class _HpSwitchProbeAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchProbeAdminStatus_Type.__name__=_B
_HpSwitchProbeAdminStatus_Object=MibScalar
hpSwitchProbeAdminStatus=_HpSwitchProbeAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9,4),_HpSwitchProbeAdminStatus_Type())
hpSwitchProbeAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProbeAdminStatus.setStatus(_J)
_HpSwitchProbedPortMask_Type=OctetString
_HpSwitchProbedPortMask_Object=MibScalar
hpSwitchProbedPortMask=_HpSwitchProbedPortMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,9,5),_HpSwitchProbedPortMask_Type())
hpSwitchProbedPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProbedPortMask.setStatus(_J)
_HpSwitchFddiIpFragConfig_ObjectIdentity=ObjectIdentity
hpSwitchFddiIpFragConfig=_HpSwitchFddiIpFragConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,11))
_HpSwitchFddiIpFragConfigTable_Object=MibTable
hpSwitchFddiIpFragConfigTable=_HpSwitchFddiIpFragConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,11,1))
if mibBuilder.loadTexts:hpSwitchFddiIpFragConfigTable.setStatus(_A)
_HpSwitchFddiIpFragConfigEntry_Object=MibTableRow
hpSwitchFddiIpFragConfigEntry=_HpSwitchFddiIpFragConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,11,1,1))
hpSwitchFddiIpFragConfigEntry.setIndexNames((0,_G,_j))
if mibBuilder.loadTexts:hpSwitchFddiIpFragConfigEntry.setStatus(_A)
class _HpSwitchFddiIpFragConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFddiIpFragConfigIndex_Type.__name__=_B
_HpSwitchFddiIpFragConfigIndex_Object=MibTableColumn
hpSwitchFddiIpFragConfigIndex=_HpSwitchFddiIpFragConfigIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,11,1,1,1),_HpSwitchFddiIpFragConfigIndex_Type())
hpSwitchFddiIpFragConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchFddiIpFragConfigIndex.setStatus(_A)
class _HpSwitchFddiIpFragConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchFddiIpFragConfigStatus_Type.__name__=_B
_HpSwitchFddiIpFragConfigStatus_Object=MibTableColumn
hpSwitchFddiIpFragConfigStatus=_HpSwitchFddiIpFragConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,11,1,1,2),_HpSwitchFddiIpFragConfigStatus_Type())
hpSwitchFddiIpFragConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFddiIpFragConfigStatus.setStatus(_A)
_HpSwitchABCConfig_ObjectIdentity=ObjectIdentity
hpSwitchABCConfig=_HpSwitchABCConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12))
_HpSwitchABCConfigTable_Object=MibTable
hpSwitchABCConfigTable=_HpSwitchABCConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1))
if mibBuilder.loadTexts:hpSwitchABCConfigTable.setStatus(_A)
_HpSwitchABCConfigEntry_Object=MibTableRow
hpSwitchABCConfigEntry=_HpSwitchABCConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1))
hpSwitchABCConfigEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:hpSwitchABCConfigEntry.setStatus(_A)
_HpSwitchABCConfigVlan_Type=VlanID
_HpSwitchABCConfigVlan_Object=MibTableColumn
hpSwitchABCConfigVlan=_HpSwitchABCConfigVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,1),_HpSwitchABCConfigVlan_Type())
hpSwitchABCConfigVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchABCConfigVlan.setStatus(_A)
class _HpSwitchABCConfigControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipipx',1),('ip',2),('ipx',3),(_E,4)))
_HpSwitchABCConfigControl_Type.__name__=_B
_HpSwitchABCConfigControl_Object=MibTableColumn
hpSwitchABCConfigControl=_HpSwitchABCConfigControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,2),_HpSwitchABCConfigControl_Type())
hpSwitchABCConfigControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchABCConfigControl.setStatus(_A)
class _HpSwitchABCConfigIpRipControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchABCConfigIpRipControl_Type.__name__=_B
_HpSwitchABCConfigIpRipControl_Object=MibTableColumn
hpSwitchABCConfigIpRipControl=_HpSwitchABCConfigIpRipControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,3),_HpSwitchABCConfigIpRipControl_Type())
hpSwitchABCConfigIpRipControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchABCConfigIpRipControl.setStatus(_A)
class _HpSwitchABCConfigIpxRipSapControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchABCConfigIpxRipSapControl_Type.__name__=_B
_HpSwitchABCConfigIpxRipSapControl_Object=MibTableColumn
hpSwitchABCConfigIpxRipSapControl=_HpSwitchABCConfigIpxRipSapControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,4),_HpSwitchABCConfigIpxRipSapControl_Type())
hpSwitchABCConfigIpxRipSapControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchABCConfigIpxRipSapControl.setStatus(_A)
class _HpSwitchABCConfigVlanBcastLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_HpSwitchABCConfigVlanBcastLimit_Type.__name__=_B
_HpSwitchABCConfigVlanBcastLimit_Object=MibTableColumn
hpSwitchABCConfigVlanBcastLimit=_HpSwitchABCConfigVlanBcastLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,5),_HpSwitchABCConfigVlanBcastLimit_Type())
hpSwitchABCConfigVlanBcastLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchABCConfigVlanBcastLimit.setStatus(_A)
class _HpSwitchABCConfigAutoGatewayConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchABCConfigAutoGatewayConfig_Type.__name__=_B
_HpSwitchABCConfigAutoGatewayConfig_Object=MibTableColumn
hpSwitchABCConfigAutoGatewayConfig=_HpSwitchABCConfigAutoGatewayConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,12,1,1,7),_HpSwitchABCConfigAutoGatewayConfig_Type())
hpSwitchABCConfigAutoGatewayConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchABCConfigAutoGatewayConfig.setStatus(_A)
_HpSwitchStpConfig_ObjectIdentity=ObjectIdentity
hpSwitchStpConfig=_HpSwitchStpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14))
_HpSwitchStpVlanTable_Object=MibTable
hpSwitchStpVlanTable=_HpSwitchStpVlanTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1))
if mibBuilder.loadTexts:hpSwitchStpVlanTable.setStatus(_A)
_HpSwitchStpVlanEntry_Object=MibTableRow
hpSwitchStpVlanEntry=_HpSwitchStpVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1))
hpSwitchStpVlanEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:hpSwitchStpVlanEntry.setStatus(_A)
_HpSwitchStpVlan_Type=VlanID
_HpSwitchStpVlan_Object=MibTableColumn
hpSwitchStpVlan=_HpSwitchStpVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,1),_HpSwitchStpVlan_Type())
hpSwitchStpVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchStpVlan.setStatus(_A)
class _HpSwitchStpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchStpAdminStatus_Type.__name__=_B
_HpSwitchStpAdminStatus_Object=MibTableColumn
hpSwitchStpAdminStatus=_HpSwitchStpAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,2),_HpSwitchStpAdminStatus_Type())
hpSwitchStpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpAdminStatus.setStatus(_A)
class _HpSwitchStpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchStpPriority_Type.__name__=_B
_HpSwitchStpPriority_Object=MibTableColumn
hpSwitchStpPriority=_HpSwitchStpPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,3),_HpSwitchStpPriority_Type())
hpSwitchStpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPriority.setStatus(_A)
_HpSwitchStpMaxAge_Type=Timeout
_HpSwitchStpMaxAge_Object=MibTableColumn
hpSwitchStpMaxAge=_HpSwitchStpMaxAge_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,4),_HpSwitchStpMaxAge_Type())
hpSwitchStpMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpMaxAge.setStatus(_A)
_HpSwitchStpHelloTime_Type=Timeout
_HpSwitchStpHelloTime_Object=MibTableColumn
hpSwitchStpHelloTime=_HpSwitchStpHelloTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,5),_HpSwitchStpHelloTime_Type())
hpSwitchStpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpHelloTime.setStatus(_A)
_HpSwitchStpForwardDelay_Type=Timeout
_HpSwitchStpForwardDelay_Object=MibTableColumn
hpSwitchStpForwardDelay=_HpSwitchStpForwardDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,1,1,6),_HpSwitchStpForwardDelay_Type())
hpSwitchStpForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpForwardDelay.setStatus(_A)
_HpSwitchStpPortTable_Object=MibTable
hpSwitchStpPortTable=_HpSwitchStpPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2))
if mibBuilder.loadTexts:hpSwitchStpPortTable.setStatus(_A)
_HpSwitchStpPortEntry_Object=MibTableRow
hpSwitchStpPortEntry=_HpSwitchStpPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1))
hpSwitchStpPortEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:hpSwitchStpPortEntry.setStatus(_A)
class _HpSwitchStpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchStpPort_Type.__name__=_B
_HpSwitchStpPort_Object=MibTableColumn
hpSwitchStpPort=_HpSwitchStpPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,1),_HpSwitchStpPort_Type())
hpSwitchStpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchStpPort.setStatus(_A)
_HpSwitchStpPortType_Type=HpSwitchPortType
_HpSwitchStpPortType_Object=MibTableColumn
hpSwitchStpPortType=_HpSwitchStpPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,2),_HpSwitchStpPortType_Type())
hpSwitchStpPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchStpPortType.setStatus(_A)
_HpSwitchStpPortSrcMac_Type=MacAddress
_HpSwitchStpPortSrcMac_Object=MibTableColumn
hpSwitchStpPortSrcMac=_HpSwitchStpPortSrcMac_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,3),_HpSwitchStpPortSrcMac_Type())
hpSwitchStpPortSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchStpPortSrcMac.setStatus(_A)
class _HpSwitchStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchStpPortPriority_Type.__name__=_B
_HpSwitchStpPortPriority_Object=MibTableColumn
hpSwitchStpPortPriority=_HpSwitchStpPortPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,4),_HpSwitchStpPortPriority_Type())
hpSwitchStpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortPriority.setStatus(_A)
class _HpSwitchStpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchStpPortPathCost_Type.__name__=_B
_HpSwitchStpPortPathCost_Object=MibTableColumn
hpSwitchStpPortPathCost=_HpSwitchStpPortPathCost_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,5),_HpSwitchStpPortPathCost_Type())
hpSwitchStpPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortPathCost.setStatus(_A)
class _HpSwitchStpPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('fast',2),(_m,3)))
_HpSwitchStpPortMode_Type.__name__=_B
_HpSwitchStpPortMode_Object=MibTableColumn
hpSwitchStpPortMode=_HpSwitchStpPortMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,6),_HpSwitchStpPortMode_Type())
hpSwitchStpPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortMode.setStatus(_A)
class _HpSwitchStpPortBpduFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HpSwitchStpPortBpduFilter_Type.__name__=_B
_HpSwitchStpPortBpduFilter_Object=MibTableColumn
hpSwitchStpPortBpduFilter=_HpSwitchStpPortBpduFilter_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,7),_HpSwitchStpPortBpduFilter_Type())
hpSwitchStpPortBpduFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortBpduFilter.setStatus(_I)
class _HpSwitchStpPortBpduProtection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HpSwitchStpPortBpduProtection_Type.__name__=_B
_HpSwitchStpPortBpduProtection_Object=MibTableColumn
hpSwitchStpPortBpduProtection=_HpSwitchStpPortBpduProtection_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,8),_HpSwitchStpPortBpduProtection_Type())
hpSwitchStpPortBpduProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortBpduProtection.setStatus(_I)
_HpSwitchStpPortErrantBpduCounter_Type=Counter32
_HpSwitchStpPortErrantBpduCounter_Object=MibTableColumn
hpSwitchStpPortErrantBpduCounter=_HpSwitchStpPortErrantBpduCounter_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,9),_HpSwitchStpPortErrantBpduCounter_Type())
hpSwitchStpPortErrantBpduCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchStpPortErrantBpduCounter.setStatus(_I)
class _HpSwitchStpPortPvstFilter_Type(TruthValue):defaultValue=2
_HpSwitchStpPortPvstFilter_Type.__name__=_M
_HpSwitchStpPortPvstFilter_Object=MibTableColumn
hpSwitchStpPortPvstFilter=_HpSwitchStpPortPvstFilter_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,10),_HpSwitchStpPortPvstFilter_Type())
hpSwitchStpPortPvstFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortPvstFilter.setStatus(_I)
class _HpSwitchStpPortPvstProtection_Type(TruthValue):defaultValue=2
_HpSwitchStpPortPvstProtection_Type.__name__=_M
_HpSwitchStpPortPvstProtection_Object=MibTableColumn
hpSwitchStpPortPvstProtection=_HpSwitchStpPortPvstProtection_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,2,1,11),_HpSwitchStpPortPvstProtection_Type())
hpSwitchStpPortPvstProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpPortPvstProtection.setStatus(_I)
class _HpSwitchStpTrapCntl_Type(Bits):namedValues=NamedValues(*(('errantBpdu',0),('newRoot',1),('rootGuard',2),('loopGuard',3)))
_HpSwitchStpTrapCntl_Type.__name__=_O
_HpSwitchStpTrapCntl_Object=MibScalar
hpSwitchStpTrapCntl=_HpSwitchStpTrapCntl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,3),_HpSwitchStpTrapCntl_Type())
hpSwitchStpTrapCntl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpTrapCntl.setStatus(_I)
class _HpSwitchStpBpduProtectionTimeout_Type(Integer32):defaultValue=0
_HpSwitchStpBpduProtectionTimeout_Type.__name__=_B
_HpSwitchStpBpduProtectionTimeout_Object=MibScalar
hpSwitchStpBpduProtectionTimeout=_HpSwitchStpBpduProtectionTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,4),_HpSwitchStpBpduProtectionTimeout_Type())
hpSwitchStpBpduProtectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchStpBpduProtectionTimeout.setStatus(_I)
class _HpSwitchSTPAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_L,2)))
_HpSwitchSTPAdminStatus_Type.__name__=_B
_HpSwitchSTPAdminStatus_Object=MibScalar
hpSwitchSTPAdminStatus=_HpSwitchSTPAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,5),_HpSwitchSTPAdminStatus_Type())
hpSwitchSTPAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSTPAdminStatus.setStatus(_A)
class _HpicfSwitchSTPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('mstp',3),('rapidPvst',4)))
_HpicfSwitchSTPVersion_Type.__name__=_B
_HpicfSwitchSTPVersion_Object=MibScalar
hpicfSwitchSTPVersion=_HpicfSwitchSTPVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,14,6),_HpicfSwitchSTPVersion_Type())
hpicfSwitchSTPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSwitchSTPVersion.setStatus(_A)
_HpSwitchIgmpConfig_ObjectIdentity=ObjectIdentity
hpSwitchIgmpConfig=_HpSwitchIgmpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15))
_HpSwitchIgmpConfigTable_Object=MibTable
hpSwitchIgmpConfigTable=_HpSwitchIgmpConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1))
if mibBuilder.loadTexts:hpSwitchIgmpConfigTable.setStatus(_A)
_HpSwitchIgmpConfigEntry_Object=MibTableRow
hpSwitchIgmpConfigEntry=_HpSwitchIgmpConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1))
hpSwitchIgmpConfigEntry.setIndexNames((0,_G,_n))
if mibBuilder.loadTexts:hpSwitchIgmpConfigEntry.setStatus(_A)
_HpSwitchIgmpVlanIndex_Type=VlanID
_HpSwitchIgmpVlanIndex_Object=MibTableColumn
hpSwitchIgmpVlanIndex=_HpSwitchIgmpVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,1),_HpSwitchIgmpVlanIndex_Type())
hpSwitchIgmpVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpVlanIndex.setStatus(_A)
class _HpSwitchIgmpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchIgmpState_Type.__name__=_B
_HpSwitchIgmpState_Object=MibTableColumn
hpSwitchIgmpState=_HpSwitchIgmpState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,2),_HpSwitchIgmpState_Type())
hpSwitchIgmpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpState.setStatus(_A)
class _HpSwitchIgmpQuerierState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchIgmpQuerierState_Type.__name__=_B
_HpSwitchIgmpQuerierState_Object=MibTableColumn
hpSwitchIgmpQuerierState=_HpSwitchIgmpQuerierState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,3),_HpSwitchIgmpQuerierState_Type())
hpSwitchIgmpQuerierState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpQuerierState.setStatus(_A)
class _HpSwitchIgmpPriorityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchIgmpPriorityState_Type.__name__=_B
_HpSwitchIgmpPriorityState_Object=MibTableColumn
hpSwitchIgmpPriorityState=_HpSwitchIgmpPriorityState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,4),_HpSwitchIgmpPriorityState_Type())
hpSwitchIgmpPriorityState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpPriorityState.setStatus(_H)
class _HpSwitchIgmpQuerierInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_HpSwitchIgmpQuerierInterval_Type.__name__=_B
_HpSwitchIgmpQuerierInterval_Object=MibTableColumn
hpSwitchIgmpQuerierInterval=_HpSwitchIgmpQuerierInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,5),_HpSwitchIgmpQuerierInterval_Type())
hpSwitchIgmpQuerierInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpQuerierInterval.setStatus(_A)
_HpSwitchIgmpProxyDomainMap_Type=Integer32
_HpSwitchIgmpProxyDomainMap_Object=MibTableColumn
hpSwitchIgmpProxyDomainMap=_HpSwitchIgmpProxyDomainMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,1,1,6),_HpSwitchIgmpProxyDomainMap_Type())
hpSwitchIgmpProxyDomainMap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpProxyDomainMap.setStatus(_A)
_HpSwitchIgmpPortConfigTable_Object=MibTable
hpSwitchIgmpPortConfigTable=_HpSwitchIgmpPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,2))
if mibBuilder.loadTexts:hpSwitchIgmpPortConfigTable.setStatus(_A)
_HpSwitchIgmpPortConfigEntry_Object=MibTableRow
hpSwitchIgmpPortConfigEntry=_HpSwitchIgmpPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,2,1))
hpSwitchIgmpPortConfigEntry.setIndexNames((0,_G,_o))
if mibBuilder.loadTexts:hpSwitchIgmpPortConfigEntry.setStatus(_A)
class _HpSwitchIgmpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIgmpPortIndex_Type.__name__=_B
_HpSwitchIgmpPortIndex_Object=MibTableColumn
hpSwitchIgmpPortIndex=_HpSwitchIgmpPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,2,1,1),_HpSwitchIgmpPortIndex_Type())
hpSwitchIgmpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpPortIndex.setStatus(_A)
_HpSwitchIgmpPortType_Type=HpSwitchPortType
_HpSwitchIgmpPortType_Object=MibTableColumn
hpSwitchIgmpPortType=_HpSwitchIgmpPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,2,1,2),_HpSwitchIgmpPortType_Type())
hpSwitchIgmpPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpPortType.setStatus(_A)
class _HpSwitchIgmpIpMcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),(_p,2),(_q,3)))
_HpSwitchIgmpIpMcastState_Type.__name__=_B
_HpSwitchIgmpIpMcastState_Object=MibTableColumn
hpSwitchIgmpIpMcastState=_HpSwitchIgmpIpMcastState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,2,1,3),_HpSwitchIgmpIpMcastState_Type())
hpSwitchIgmpIpMcastState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpIpMcastState.setStatus(_A)
_HpSwitchIgmpPortConfigTable2_Object=MibTable
hpSwitchIgmpPortConfigTable2=_HpSwitchIgmpPortConfigTable2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3))
if mibBuilder.loadTexts:hpSwitchIgmpPortConfigTable2.setStatus(_A)
_HpSwitchIgmpPortConfigEntry2_Object=MibTableRow
hpSwitchIgmpPortConfigEntry2=_HpSwitchIgmpPortConfigEntry2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1))
hpSwitchIgmpPortConfigEntry2.setIndexNames((0,_G,_r),(0,_G,_s))
if mibBuilder.loadTexts:hpSwitchIgmpPortConfigEntry2.setStatus(_A)
class _HpSwitchIgmpPortVlanIndex2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIgmpPortVlanIndex2_Type.__name__=_B
_HpSwitchIgmpPortVlanIndex2_Object=MibTableColumn
hpSwitchIgmpPortVlanIndex2=_HpSwitchIgmpPortVlanIndex2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,1),_HpSwitchIgmpPortVlanIndex2_Type())
hpSwitchIgmpPortVlanIndex2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpPortVlanIndex2.setStatus(_A)
class _HpSwitchIgmpPortIndex2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIgmpPortIndex2_Type.__name__=_B
_HpSwitchIgmpPortIndex2_Object=MibTableColumn
hpSwitchIgmpPortIndex2=_HpSwitchIgmpPortIndex2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,2),_HpSwitchIgmpPortIndex2_Type())
hpSwitchIgmpPortIndex2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpPortIndex2.setStatus(_A)
_HpSwitchIgmpPortType2_Type=HpSwitchPortType
_HpSwitchIgmpPortType2_Object=MibTableColumn
hpSwitchIgmpPortType2=_HpSwitchIgmpPortType2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,3),_HpSwitchIgmpPortType2_Type())
hpSwitchIgmpPortType2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIgmpPortType2.setStatus(_A)
class _HpSwitchIgmpIpMcastState2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),(_p,2),(_q,3)))
_HpSwitchIgmpIpMcastState2_Type.__name__=_B
_HpSwitchIgmpIpMcastState2_Object=MibTableColumn
hpSwitchIgmpIpMcastState2=_HpSwitchIgmpIpMcastState2_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,4),_HpSwitchIgmpIpMcastState2_Type())
hpSwitchIgmpIpMcastState2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpIpMcastState2.setStatus(_A)
class _HpSwitchIgmpPortForcedLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_L,2)))
_HpSwitchIgmpPortForcedLeaveState_Type.__name__=_B
_HpSwitchIgmpPortForcedLeaveState_Object=MibTableColumn
hpSwitchIgmpPortForcedLeaveState=_HpSwitchIgmpPortForcedLeaveState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,5),_HpSwitchIgmpPortForcedLeaveState_Type())
hpSwitchIgmpPortForcedLeaveState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpPortForcedLeaveState.setStatus(_A)
class _HpSwitchIgmpPortFastLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_L,2)))
_HpSwitchIgmpPortFastLeaveState_Type.__name__=_B
_HpSwitchIgmpPortFastLeaveState_Object=MibTableColumn
hpSwitchIgmpPortFastLeaveState=_HpSwitchIgmpPortFastLeaveState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,3,1,6),_HpSwitchIgmpPortFastLeaveState_Type())
hpSwitchIgmpPortFastLeaveState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpPortFastLeaveState.setStatus(_A)
class _HpSwitchIgmpForcedLeaveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIgmpForcedLeaveInterval_Type.__name__=_B
_HpSwitchIgmpForcedLeaveInterval_Object=MibScalar
hpSwitchIgmpForcedLeaveInterval=_HpSwitchIgmpForcedLeaveInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,15,4),_HpSwitchIgmpForcedLeaveInterval_Type())
hpSwitchIgmpForcedLeaveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchIgmpForcedLeaveInterval.setStatus(_A)
_HpSwitchCosConfig_ObjectIdentity=ObjectIdentity
hpSwitchCosConfig=_HpSwitchCosConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17))
_HpSwitchCosPortConfigTable_Object=MibTable
hpSwitchCosPortConfigTable=_HpSwitchCosPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1))
if mibBuilder.loadTexts:hpSwitchCosPortConfigTable.setStatus(_A)
_HpSwitchCosPortConfigEntry_Object=MibTableRow
hpSwitchCosPortConfigEntry=_HpSwitchCosPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1))
hpSwitchCosPortConfigEntry.setIndexNames((0,_G,_t))
if mibBuilder.loadTexts:hpSwitchCosPortConfigEntry.setStatus(_A)
class _HpSwitchCosPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchCosPortIndex_Type.__name__=_B
_HpSwitchCosPortIndex_Object=MibTableColumn
hpSwitchCosPortIndex=_HpSwitchCosPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,1),_HpSwitchCosPortIndex_Type())
hpSwitchCosPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosPortIndex.setStatus(_A)
_HpSwitchCosPortType_Type=HpSwitchPortType
_HpSwitchCosPortType_Object=MibTableColumn
hpSwitchCosPortType=_HpSwitchCosPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,2),_HpSwitchCosPortType_Type())
hpSwitchCosPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosPortType.setStatus(_H)
class _HpSwitchCosPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchCosPortPriority_Type.__name__=_B
_HpSwitchCosPortPriority_Object=MibTableColumn
hpSwitchCosPortPriority=_HpSwitchCosPortPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,3),_HpSwitchCosPortPriority_Type())
hpSwitchCosPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosPortPriority.setStatus(_A)
class _HpSwitchCosPortDSCPPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpSwitchCosPortDSCPPolicy_Type.__name__=_B
_HpSwitchCosPortDSCPPolicy_Object=MibTableColumn
hpSwitchCosPortDSCPPolicy=_HpSwitchCosPortDSCPPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,4),_HpSwitchCosPortDSCPPolicy_Type())
hpSwitchCosPortDSCPPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosPortDSCPPolicy.setStatus(_A)
class _HpSwitchCosPortResolvedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosPortResolvedPriority_Type.__name__=_B
_HpSwitchCosPortResolvedPriority_Object=MibTableColumn
hpSwitchCosPortResolvedPriority=_HpSwitchCosPortResolvedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,5),_HpSwitchCosPortResolvedPriority_Type())
hpSwitchCosPortResolvedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosPortResolvedPriority.setStatus(_A)
class _HpSwitchCosPortApplyPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),('applyHpSwitchCosPortPriority',2),('applyHpSwitchCosPortDSCPPolicy',3)))
_HpSwitchCosPortApplyPolicy_Type.__name__=_B
_HpSwitchCosPortApplyPolicy_Object=MibTableColumn
hpSwitchCosPortApplyPolicy=_HpSwitchCosPortApplyPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,6),_HpSwitchCosPortApplyPolicy_Type())
hpSwitchCosPortApplyPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosPortApplyPolicy.setStatus(_A)
class _HpSwitchCosPortTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('trustNone',1),('trust8021pCos',2),('trustTosIpPrecedence',3),('trustTosDiffserv',4),('trustAll',5),('trustPartnerDevice',6)))
_HpSwitchCosPortTrustMode_Type.__name__=_B
_HpSwitchCosPortTrustMode_Object=MibTableColumn
hpSwitchCosPortTrustMode=_HpSwitchCosPortTrustMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,7),_HpSwitchCosPortTrustMode_Type())
hpSwitchCosPortTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosPortTrustMode.setStatus(_A)
_HpSwitchCosPortPartnerDevice_Type=HpPartnerDeviceTypeList
_HpSwitchCosPortPartnerDevice_Object=MibTableColumn
hpSwitchCosPortPartnerDevice=_HpSwitchCosPortPartnerDevice_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,8),_HpSwitchCosPortPartnerDevice_Type())
hpSwitchCosPortPartnerDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosPortPartnerDevice.setStatus(_A)
class _HpSwitchCosPortTrustedPartnerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('untrusted',1),('trusted',2)))
_HpSwitchCosPortTrustedPartnerState_Type.__name__=_B
_HpSwitchCosPortTrustedPartnerState_Object=MibTableColumn
hpSwitchCosPortTrustedPartnerState=_HpSwitchCosPortTrustedPartnerState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,1,1,9),_HpSwitchCosPortTrustedPartnerState_Type())
hpSwitchCosPortTrustedPartnerState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosPortTrustedPartnerState.setStatus(_A)
_HpSwitchCosVlanConfigTable_Object=MibTable
hpSwitchCosVlanConfigTable=_HpSwitchCosVlanConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2))
if mibBuilder.loadTexts:hpSwitchCosVlanConfigTable.setStatus(_A)
_HpSwitchCosVlanConfigEntry_Object=MibTableRow
hpSwitchCosVlanConfigEntry=_HpSwitchCosVlanConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1))
hpSwitchCosVlanConfigEntry.setIndexNames((0,_G,_v))
if mibBuilder.loadTexts:hpSwitchCosVlanConfigEntry.setStatus(_A)
_HpSwitchCosVlanIndex_Type=VlanID
_HpSwitchCosVlanIndex_Object=MibTableColumn
hpSwitchCosVlanIndex=_HpSwitchCosVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1,1),_HpSwitchCosVlanIndex_Type())
hpSwitchCosVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosVlanIndex.setStatus(_A)
class _HpSwitchCosVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchCosVlanPriority_Type.__name__=_B
_HpSwitchCosVlanPriority_Object=MibTableColumn
hpSwitchCosVlanPriority=_HpSwitchCosVlanPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1,2),_HpSwitchCosVlanPriority_Type())
hpSwitchCosVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosVlanPriority.setStatus(_A)
class _HpSwitchCosVlanDSCPPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpSwitchCosVlanDSCPPolicy_Type.__name__=_B
_HpSwitchCosVlanDSCPPolicy_Object=MibTableColumn
hpSwitchCosVlanDSCPPolicy=_HpSwitchCosVlanDSCPPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1,3),_HpSwitchCosVlanDSCPPolicy_Type())
hpSwitchCosVlanDSCPPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosVlanDSCPPolicy.setStatus(_A)
class _HpSwitchCosVlanResolvedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosVlanResolvedPriority_Type.__name__=_B
_HpSwitchCosVlanResolvedPriority_Object=MibTableColumn
hpSwitchCosVlanResolvedPriority=_HpSwitchCosVlanResolvedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1,4),_HpSwitchCosVlanResolvedPriority_Type())
hpSwitchCosVlanResolvedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosVlanResolvedPriority.setStatus(_A)
class _HpSwitchCosVlanApplyPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),('applyHpSwitchCosVlanPriority',2),('applyHpSwitchCosVlanDSCPPolicy',3)))
_HpSwitchCosVlanApplyPolicy_Type.__name__=_B
_HpSwitchCosVlanApplyPolicy_Object=MibTableColumn
hpSwitchCosVlanApplyPolicy=_HpSwitchCosVlanApplyPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,2,1,5),_HpSwitchCosVlanApplyPolicy_Type())
hpSwitchCosVlanApplyPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosVlanApplyPolicy.setStatus(_A)
_HpSwitchCosProtocolConfigTable_Object=MibTable
hpSwitchCosProtocolConfigTable=_HpSwitchCosProtocolConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,3))
if mibBuilder.loadTexts:hpSwitchCosProtocolConfigTable.setStatus(_A)
_HpSwitchCosProtocolConfigEntry_Object=MibTableRow
hpSwitchCosProtocolConfigEntry=_HpSwitchCosProtocolConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,3,1))
hpSwitchCosProtocolConfigEntry.setIndexNames((0,_G,_w))
if mibBuilder.loadTexts:hpSwitchCosProtocolConfigEntry.setStatus(_A)
class _HpSwitchCosProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ip',1),('ipx',2),('arp',3),('decnet',4),('appletalk',5),('sna',6),('netbios',7)))
_HpSwitchCosProtocolType_Type.__name__=_B
_HpSwitchCosProtocolType_Object=MibTableColumn
hpSwitchCosProtocolType=_HpSwitchCosProtocolType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,3,1,1),_HpSwitchCosProtocolType_Type())
hpSwitchCosProtocolType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosProtocolType.setStatus(_A)
class _HpSwitchCosProtocolPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchCosProtocolPriority_Type.__name__=_B
_HpSwitchCosProtocolPriority_Object=MibTableColumn
hpSwitchCosProtocolPriority=_HpSwitchCosProtocolPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,3,1,2),_HpSwitchCosProtocolPriority_Type())
hpSwitchCosProtocolPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosProtocolPriority.setStatus(_A)
_HpSwitchCosAddressConfigTable_Object=MibTable
hpSwitchCosAddressConfigTable=_HpSwitchCosAddressConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4))
if mibBuilder.loadTexts:hpSwitchCosAddressConfigTable.setStatus(_A)
_HpSwitchCosAddressConfigEntry_Object=MibTableRow
hpSwitchCosAddressConfigEntry=_HpSwitchCosAddressConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1))
hpSwitchCosAddressConfigEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:hpSwitchCosAddressConfigEntry.setStatus(_A)
class _HpSwitchCosAddressIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchCosAddressIndex_Type.__name__=_B
_HpSwitchCosAddressIndex_Object=MibTableColumn
hpSwitchCosAddressIndex=_HpSwitchCosAddressIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,1),_HpSwitchCosAddressIndex_Type())
hpSwitchCosAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosAddressIndex.setStatus(_A)
class _HpSwitchCosAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('ipv6',2)))
_HpSwitchCosAddressType_Type.__name__=_B
_HpSwitchCosAddressType_Object=MibTableColumn
hpSwitchCosAddressType=_HpSwitchCosAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,2),_HpSwitchCosAddressType_Type())
hpSwitchCosAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressType.setStatus(_A)
_HpSwitchCosAddressIp_Type=IpAddress
_HpSwitchCosAddressIp_Object=MibTableColumn
hpSwitchCosAddressIp=_HpSwitchCosAddressIp_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,3),_HpSwitchCosAddressIp_Type())
hpSwitchCosAddressIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressIp.setStatus(_A)
class _HpSwitchCosAddressPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchCosAddressPriority_Type.__name__=_B
_HpSwitchCosAddressPriority_Object=MibTableColumn
hpSwitchCosAddressPriority=_HpSwitchCosAddressPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,4),_HpSwitchCosAddressPriority_Type())
hpSwitchCosAddressPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressPriority.setStatus(_A)
_HpSwitchCosAddressStatus_Type=RowStatus
_HpSwitchCosAddressStatus_Object=MibTableColumn
hpSwitchCosAddressStatus=_HpSwitchCosAddressStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,5),_HpSwitchCosAddressStatus_Type())
hpSwitchCosAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressStatus.setStatus(_A)
class _HpSwitchCosAddressDSCPPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpSwitchCosAddressDSCPPolicy_Type.__name__=_B
_HpSwitchCosAddressDSCPPolicy_Object=MibTableColumn
hpSwitchCosAddressDSCPPolicy=_HpSwitchCosAddressDSCPPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,6),_HpSwitchCosAddressDSCPPolicy_Type())
hpSwitchCosAddressDSCPPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressDSCPPolicy.setStatus(_A)
class _HpSwitchCosAddressResolvedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosAddressResolvedPriority_Type.__name__=_B
_HpSwitchCosAddressResolvedPriority_Object=MibTableColumn
hpSwitchCosAddressResolvedPriority=_HpSwitchCosAddressResolvedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,7),_HpSwitchCosAddressResolvedPriority_Type())
hpSwitchCosAddressResolvedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosAddressResolvedPriority.setStatus(_A)
class _HpSwitchCosAddressApplyPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('applyHpSwitchCosAddressPriority',1),('applyHpSwitchCosAddressDSCPPolicy',2)))
_HpSwitchCosAddressApplyPolicy_Type.__name__=_B
_HpSwitchCosAddressApplyPolicy_Object=MibTableColumn
hpSwitchCosAddressApplyPolicy=_HpSwitchCosAddressApplyPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,8),_HpSwitchCosAddressApplyPolicy_Type())
hpSwitchCosAddressApplyPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressApplyPolicy.setStatus(_A)
_HpSwitchCosIpv4AddressMask_Type=IpAddress
_HpSwitchCosIpv4AddressMask_Object=MibTableColumn
hpSwitchCosIpv4AddressMask=_HpSwitchCosIpv4AddressMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,9),_HpSwitchCosIpv4AddressMask_Type())
hpSwitchCosIpv4AddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosIpv4AddressMask.setStatus(_A)
_HpSwitchCosAddressIpv6_Type=InetAddress
_HpSwitchCosAddressIpv6_Object=MibTableColumn
hpSwitchCosAddressIpv6=_HpSwitchCosAddressIpv6_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,10),_HpSwitchCosAddressIpv6_Type())
hpSwitchCosAddressIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressIpv6.setStatus(_A)
_HpSwitchCosAddressIpv6PrefixLength_Type=InetAddressPrefixLength
_HpSwitchCosAddressIpv6PrefixLength_Object=MibTableColumn
hpSwitchCosAddressIpv6PrefixLength=_HpSwitchCosAddressIpv6PrefixLength_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,4,1,11),_HpSwitchCosAddressIpv6PrefixLength_Type())
hpSwitchCosAddressIpv6PrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAddressIpv6PrefixLength.setStatus(_A)
_HpSwitchCosTosConfig_ObjectIdentity=ObjectIdentity
hpSwitchCosTosConfig=_HpSwitchCosTosConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5))
class _HpSwitchCosTosConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('ipprecedence',2),('diffserv',3)))
_HpSwitchCosTosConfigMode_Type.__name__=_B
_HpSwitchCosTosConfigMode_Object=MibScalar
hpSwitchCosTosConfigMode=_HpSwitchCosTosConfigMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,1),_HpSwitchCosTosConfigMode_Type())
hpSwitchCosTosConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosTosConfigMode.setStatus(_A)
_HpSwitchCosTosConfigTable_Object=MibTable
hpSwitchCosTosConfigTable=_HpSwitchCosTosConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2))
if mibBuilder.loadTexts:hpSwitchCosTosConfigTable.setStatus(_A)
_HpSwitchCosTosConfigEntry_Object=MibTableRow
hpSwitchCosTosConfigEntry=_HpSwitchCosTosConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1))
hpSwitchCosTosConfigEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:hpSwitchCosTosConfigEntry.setStatus(_A)
_HpSwitchCosTosIndex_Type=Integer32
_HpSwitchCosTosIndex_Object=MibTableColumn
hpSwitchCosTosIndex=_HpSwitchCosTosIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1,1),_HpSwitchCosTosIndex_Type())
hpSwitchCosTosIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosTosIndex.setStatus(_A)
class _HpSwitchCosTosPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpSwitchCosTosPriority_Type.__name__=_B
_HpSwitchCosTosPriority_Object=MibTableColumn
hpSwitchCosTosPriority=_HpSwitchCosTosPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1,2),_HpSwitchCosTosPriority_Type())
hpSwitchCosTosPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosTosPriority.setStatus(_H)
class _HpSwitchCosTosDSCPPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpSwitchCosTosDSCPPolicy_Type.__name__=_B
_HpSwitchCosTosDSCPPolicy_Object=MibTableColumn
hpSwitchCosTosDSCPPolicy=_HpSwitchCosTosDSCPPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1,3),_HpSwitchCosTosDSCPPolicy_Type())
hpSwitchCosTosDSCPPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosTosDSCPPolicy.setStatus(_A)
class _HpSwitchCosTosResolvedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosTosResolvedPriority_Type.__name__=_B
_HpSwitchCosTosResolvedPriority_Object=MibTableColumn
hpSwitchCosTosResolvedPriority=_HpSwitchCosTosResolvedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1,4),_HpSwitchCosTosResolvedPriority_Type())
hpSwitchCosTosResolvedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosTosResolvedPriority.setStatus(_A)
class _HpSwitchCosTosApplyPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('applyInheritedPriority',1),('applyHpSwitchCosTosDSCPPolicy',2)))
_HpSwitchCosTosApplyPolicy_Type.__name__=_B
_HpSwitchCosTosApplyPolicy_Object=MibTableColumn
hpSwitchCosTosApplyPolicy=_HpSwitchCosTosApplyPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,5,2,1,5),_HpSwitchCosTosApplyPolicy_Type())
hpSwitchCosTosApplyPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosTosApplyPolicy.setStatus(_A)
_HpSwitchCosDSCPPolicyConfigTable_Object=MibTable
hpSwitchCosDSCPPolicyConfigTable=_HpSwitchCosDSCPPolicyConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,6))
if mibBuilder.loadTexts:hpSwitchCosDSCPPolicyConfigTable.setStatus(_A)
_HpSwitchCosDSCPPolicyConfigEntry_Object=MibTableRow
hpSwitchCosDSCPPolicyConfigEntry=_HpSwitchCosDSCPPolicyConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,6,1))
hpSwitchCosDSCPPolicyConfigEntry.setIndexNames((0,_G,_z))
if mibBuilder.loadTexts:hpSwitchCosDSCPPolicyConfigEntry.setStatus(_A)
class _HpSwitchCosDSCPPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpSwitchCosDSCPPolicyIndex_Type.__name__=_B
_HpSwitchCosDSCPPolicyIndex_Object=MibTableColumn
hpSwitchCosDSCPPolicyIndex=_HpSwitchCosDSCPPolicyIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,6,1,1),_HpSwitchCosDSCPPolicyIndex_Type())
hpSwitchCosDSCPPolicyIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpSwitchCosDSCPPolicyIndex.setStatus(_A)
class _HpSwitchCosDSCPPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosDSCPPolicyPriority_Type.__name__=_B
_HpSwitchCosDSCPPolicyPriority_Object=MibTableColumn
hpSwitchCosDSCPPolicyPriority=_HpSwitchCosDSCPPolicyPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,6,1,2),_HpSwitchCosDSCPPolicyPriority_Type())
hpSwitchCosDSCPPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosDSCPPolicyPriority.setStatus(_A)
class _HpSwitchCosDSCPPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpSwitchCosDSCPPolicyName_Type.__name__=_K
_HpSwitchCosDSCPPolicyName_Object=MibTableColumn
hpSwitchCosDSCPPolicyName=_HpSwitchCosDSCPPolicyName_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,6,1,3),_HpSwitchCosDSCPPolicyName_Type())
hpSwitchCosDSCPPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosDSCPPolicyName.setStatus(_A)
_HpSwitchCosAppTypeConfigTable_Object=MibTable
hpSwitchCosAppTypeConfigTable=_HpSwitchCosAppTypeConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7))
if mibBuilder.loadTexts:hpSwitchCosAppTypeConfigTable.setStatus(_A)
_HpSwitchCosAppTypeConfigEntry_Object=MibTableRow
hpSwitchCosAppTypeConfigEntry=_HpSwitchCosAppTypeConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1))
hpSwitchCosAppTypeConfigEntry.setIndexNames((0,_G,_A0))
if mibBuilder.loadTexts:hpSwitchCosAppTypeConfigEntry.setStatus(_A)
class _HpSwitchCosAppTypeConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchCosAppTypeConfigIndex_Type.__name__=_B
_HpSwitchCosAppTypeConfigIndex_Object=MibTableColumn
hpSwitchCosAppTypeConfigIndex=_HpSwitchCosAppTypeConfigIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,1),_HpSwitchCosAppTypeConfigIndex_Type())
hpSwitchCosAppTypeConfigIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpSwitchCosAppTypeConfigIndex.setStatus(_A)
class _HpSwitchCosAppTypeConfigType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('udpSrcPortConfig',1),('udpDestPortConfig',2),('udpBothPortsConfig',3),('tcpSrcPortConfig',4),('tcpDestPortConfig',5),('tcpBothPortsConfig',6)))
_HpSwitchCosAppTypeConfigType_Type.__name__=_B
_HpSwitchCosAppTypeConfigType_Object=MibTableColumn
hpSwitchCosAppTypeConfigType=_HpSwitchCosAppTypeConfigType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,2),_HpSwitchCosAppTypeConfigType_Type())
hpSwitchCosAppTypeConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeConfigType.setStatus(_A)
class _HpSwitchCosAppTypeSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchCosAppTypeSrcPort_Type.__name__=_B
_HpSwitchCosAppTypeSrcPort_Object=MibTableColumn
hpSwitchCosAppTypeSrcPort=_HpSwitchCosAppTypeSrcPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,3),_HpSwitchCosAppTypeSrcPort_Type())
hpSwitchCosAppTypeSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeSrcPort.setStatus(_A)
class _HpSwitchCosAppTypeDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchCosAppTypeDestPort_Type.__name__=_B
_HpSwitchCosAppTypeDestPort_Object=MibTableColumn
hpSwitchCosAppTypeDestPort=_HpSwitchCosAppTypeDestPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,4),_HpSwitchCosAppTypeDestPort_Type())
hpSwitchCosAppTypeDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeDestPort.setStatus(_A)
class _HpSwitchCosAppTypePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosAppTypePriority_Type.__name__=_B
_HpSwitchCosAppTypePriority_Object=MibTableColumn
hpSwitchCosAppTypePriority=_HpSwitchCosAppTypePriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,5),_HpSwitchCosAppTypePriority_Type())
hpSwitchCosAppTypePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypePriority.setStatus(_A)
class _HpSwitchCosAppTypeDSCPPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpSwitchCosAppTypeDSCPPolicy_Type.__name__=_B
_HpSwitchCosAppTypeDSCPPolicy_Object=MibTableColumn
hpSwitchCosAppTypeDSCPPolicy=_HpSwitchCosAppTypeDSCPPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,6),_HpSwitchCosAppTypeDSCPPolicy_Type())
hpSwitchCosAppTypeDSCPPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeDSCPPolicy.setStatus(_A)
class _HpSwitchCosAppTypeResolvedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpSwitchCosAppTypeResolvedPriority_Type.__name__=_B
_HpSwitchCosAppTypeResolvedPriority_Object=MibTableColumn
hpSwitchCosAppTypeResolvedPriority=_HpSwitchCosAppTypeResolvedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,7),_HpSwitchCosAppTypeResolvedPriority_Type())
hpSwitchCosAppTypeResolvedPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosAppTypeResolvedPriority.setStatus(_A)
class _HpSwitchCosAppTypeApplyPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('applyHpSwitchCosAppTypePriority',1),('applyHpSwitchCosAppTypeDSCPPolicy',2)))
_HpSwitchCosAppTypeApplyPolicy_Type.__name__=_B
_HpSwitchCosAppTypeApplyPolicy_Object=MibTableColumn
hpSwitchCosAppTypeApplyPolicy=_HpSwitchCosAppTypeApplyPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,8),_HpSwitchCosAppTypeApplyPolicy_Type())
hpSwitchCosAppTypeApplyPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeApplyPolicy.setStatus(_A)
_HpSwitchCosAppTypeStatus_Type=RowStatus
_HpSwitchCosAppTypeStatus_Object=MibTableColumn
hpSwitchCosAppTypeStatus=_HpSwitchCosAppTypeStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,9),_HpSwitchCosAppTypeStatus_Type())
hpSwitchCosAppTypeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeStatus.setStatus(_A)
class _HpSwitchCosAppTypeMaxSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchCosAppTypeMaxSrcPort_Type.__name__=_B
_HpSwitchCosAppTypeMaxSrcPort_Object=MibTableColumn
hpSwitchCosAppTypeMaxSrcPort=_HpSwitchCosAppTypeMaxSrcPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,10),_HpSwitchCosAppTypeMaxSrcPort_Type())
hpSwitchCosAppTypeMaxSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeMaxSrcPort.setStatus(_A)
class _HpSwitchCosAppTypeMaxDestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpSwitchCosAppTypeMaxDestPort_Type.__name__=_B
_HpSwitchCosAppTypeMaxDestPort_Object=MibTableColumn
hpSwitchCosAppTypeMaxDestPort=_HpSwitchCosAppTypeMaxDestPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,11),_HpSwitchCosAppTypeMaxDestPort_Type())
hpSwitchCosAppTypeMaxDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeMaxDestPort.setStatus(_A)
class _HpSwitchCosAppTypeIpPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4PacketsOnly',1),('ipv6PacketsOnly',2),('ipv4AndIpv6Packets',3)))
_HpSwitchCosAppTypeIpPacketType_Type.__name__=_B
_HpSwitchCosAppTypeIpPacketType_Object=MibTableColumn
hpSwitchCosAppTypeIpPacketType=_HpSwitchCosAppTypeIpPacketType_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,7,1,12),_HpSwitchCosAppTypeIpPacketType_Type())
hpSwitchCosAppTypeIpPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchCosAppTypeIpPacketType.setStatus(_A)
_HpSwitchCosLastChange_Type=TimeStamp
_HpSwitchCosLastChange_Object=MibScalar
hpSwitchCosLastChange=_HpSwitchCosLastChange_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,8),_HpSwitchCosLastChange_Type())
hpSwitchCosLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchCosLastChange.setStatus(_A)
class _HpSwitchConfigCosLastConfigError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('aclQosNoError',1),('aclQosTooManyRulesError',2),('aclQosTooManyMasksError',3),('aclQosTooManyRangesError',4),('aclQosTooManyMetersError',5),('aclQosTooManyLookupsError',6)))
_HpSwitchConfigCosLastConfigError_Type.__name__=_B
_HpSwitchConfigCosLastConfigError_Object=MibScalar
hpSwitchConfigCosLastConfigError=_HpSwitchConfigCosLastConfigError_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,9),_HpSwitchConfigCosLastConfigError_Type())
hpSwitchConfigCosLastConfigError.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchConfigCosLastConfigError.setStatus(_A)
_HpSwitchQueueWatchTable_Object=MibTable
hpSwitchQueueWatchTable=_HpSwitchQueueWatchTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,10))
if mibBuilder.loadTexts:hpSwitchQueueWatchTable.setStatus(_A)
_HpSwitchQueueWatchEntry_Object=MibTableRow
hpSwitchQueueWatchEntry=_HpSwitchQueueWatchEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,10,1))
hpSwitchQueueWatchEntry.setIndexNames((0,_G,_A1))
if mibBuilder.loadTexts:hpSwitchQueueWatchEntry.setStatus(_A)
class _HpSwitchQueueWatchPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchQueueWatchPort_Type.__name__=_B
_HpSwitchQueueWatchPort_Object=MibTableColumn
hpSwitchQueueWatchPort=_HpSwitchQueueWatchPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,10,1,1),_HpSwitchQueueWatchPort_Type())
hpSwitchQueueWatchPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchQueueWatchPort.setStatus(_A)
class _HpSwitchQueueWatchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('outbound',2)))
_HpSwitchQueueWatchState_Type.__name__=_B
_HpSwitchQueueWatchState_Object=MibTableColumn
hpSwitchQueueWatchState=_HpSwitchQueueWatchState_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,17,10,1,2),_HpSwitchQueueWatchState_Type())
hpSwitchQueueWatchState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchQueueWatchState.setStatus(_A)
_HpSwitchMeshConfig_ObjectIdentity=ObjectIdentity
hpSwitchMeshConfig=_HpSwitchMeshConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,18))
class _HpSwitchMeshMulticastAgingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aging',1),('nonaging',2)))
_HpSwitchMeshMulticastAgingMode_Type.__name__=_B
_HpSwitchMeshMulticastAgingMode_Object=MibScalar
hpSwitchMeshMulticastAgingMode=_HpSwitchMeshMulticastAgingMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,18,1),_HpSwitchMeshMulticastAgingMode_Type())
hpSwitchMeshMulticastAgingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMeshMulticastAgingMode.setStatus(_H)
class _HpSwitchMeshBackwardCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchMeshBackwardCompatibility_Type.__name__=_B
_HpSwitchMeshBackwardCompatibility_Object=MibScalar
hpSwitchMeshBackwardCompatibility=_HpSwitchMeshBackwardCompatibility_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,18,2),_HpSwitchMeshBackwardCompatibility_Type())
hpSwitchMeshBackwardCompatibility.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMeshBackwardCompatibility.setStatus(_A)
class _HpSwitchMeshConfiguredId_Type(Integer32):defaultValue=0
_HpSwitchMeshConfiguredId_Type.__name__=_B
_HpSwitchMeshConfiguredId_Object=MibScalar
hpSwitchMeshConfiguredId=_HpSwitchMeshConfiguredId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,18,3),_HpSwitchMeshConfiguredId_Type())
hpSwitchMeshConfiguredId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMeshConfiguredId.setStatus(_A)
_HpSwitchMeshActualId_Type=Integer32
_HpSwitchMeshActualId_Object=MibScalar
hpSwitchMeshActualId=_HpSwitchMeshActualId_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,18,4),_HpSwitchMeshActualId_Type())
hpSwitchMeshActualId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchMeshActualId.setStatus(_A)
_HpSwitchPortIsolationConfig_ObjectIdentity=ObjectIdentity
hpSwitchPortIsolationConfig=_HpSwitchPortIsolationConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19))
class _HpSwitchPortIsolationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchPortIsolationMode_Type.__name__=_B
_HpSwitchPortIsolationMode_Object=MibScalar
hpSwitchPortIsolationMode=_HpSwitchPortIsolationMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19,1),_HpSwitchPortIsolationMode_Type())
hpSwitchPortIsolationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortIsolationMode.setStatus(_A)
_HpSwitchPortIsolationConfigTable_Object=MibTable
hpSwitchPortIsolationConfigTable=_HpSwitchPortIsolationConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19,2))
if mibBuilder.loadTexts:hpSwitchPortIsolationConfigTable.setStatus(_A)
_HpSwitchPortIsolationConfigEntry_Object=MibTableRow
hpSwitchPortIsolationConfigEntry=_HpSwitchPortIsolationConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19,2,1))
hpSwitchPortIsolationConfigEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:hpSwitchPortIsolationConfigEntry.setStatus(_A)
class _HpSwitchPortIsolationPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortIsolationPort_Type.__name__=_B
_HpSwitchPortIsolationPort_Object=MibTableColumn
hpSwitchPortIsolationPort=_HpSwitchPortIsolationPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19,2,1,1),_HpSwitchPortIsolationPort_Type())
hpSwitchPortIsolationPort.setMaxAccess(_S)
if mibBuilder.loadTexts:hpSwitchPortIsolationPort.setStatus(_A)
class _HpSwitchPortIsolationPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_m,1),('public',2),('private',3),('local',4),('group1',5),('group2',6)))
_HpSwitchPortIsolationPortMode_Type.__name__=_B
_HpSwitchPortIsolationPortMode_Object=MibTableColumn
hpSwitchPortIsolationPortMode=_HpSwitchPortIsolationPortMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,19,2,1,2),_HpSwitchPortIsolationPortMode_Type())
hpSwitchPortIsolationPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPortIsolationPortMode.setStatus(_A)
_HpSwitchSshConfig_ObjectIdentity=ObjectIdentity
hpSwitchSshConfig=_HpSwitchSshConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20))
class _HpSwitchSshAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchSshAdminStatus_Type.__name__=_B
_HpSwitchSshAdminStatus_Object=MibScalar
hpSwitchSshAdminStatus=_HpSwitchSshAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,1),_HpSwitchSshAdminStatus_Type())
hpSwitchSshAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshAdminStatus.setStatus(_A)
class _HpSwitchSshVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version2',2),('version1or2',3)))
_HpSwitchSshVersion_Type.__name__=_B
_HpSwitchSshVersion_Object=MibScalar
hpSwitchSshVersion=_HpSwitchSshVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,2),_HpSwitchSshVersion_Type())
hpSwitchSshVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshVersion.setStatus(_A)
class _HpSwitchSshTimeout_Type(Timeout):defaultValue=120;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_HpSwitchSshTimeout_Type.__name__='Timeout'
_HpSwitchSshTimeout_Object=MibScalar
hpSwitchSshTimeout=_HpSwitchSshTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,3),_HpSwitchSshTimeout_Type())
hpSwitchSshTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshTimeout.setStatus(_A)
class _HpSwitchSshPortNumber_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchSshPortNumber_Type.__name__=_B
_HpSwitchSshPortNumber_Object=MibScalar
hpSwitchSshPortNumber=_HpSwitchSshPortNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,4),_HpSwitchSshPortNumber_Type())
hpSwitchSshPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshPortNumber.setStatus(_A)
class _HpSwitchSshServerKeySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bits512',1),('bits768',2),('bits1024',3)))
_HpSwitchSshServerKeySize_Type.__name__=_B
_HpSwitchSshServerKeySize_Object=MibScalar
hpSwitchSshServerKeySize=_HpSwitchSshServerKeySize_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,5),_HpSwitchSshServerKeySize_Type())
hpSwitchSshServerKeySize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshServerKeySize.setStatus(_A)
class _HpSwitchSshFileServerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchSshFileServerAdminStatus_Type.__name__=_B
_HpSwitchSshFileServerAdminStatus_Object=MibScalar
hpSwitchSshFileServerAdminStatus=_HpSwitchSshFileServerAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,6),_HpSwitchSshFileServerAdminStatus_Type())
hpSwitchSshFileServerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshFileServerAdminStatus.setStatus(_A)
class _HpSwitchSshIpVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('ipv4or6',3)))
_HpSwitchSshIpVersion_Type.__name__=_B
_HpSwitchSshIpVersion_Object=MibScalar
hpSwitchSshIpVersion=_HpSwitchSshIpVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,7),_HpSwitchSshIpVersion_Type())
hpSwitchSshIpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshIpVersion.setStatus(_H)
class _HpSwitchSshReKeyStatus_Type(TruthValue):defaultValue=2
_HpSwitchSshReKeyStatus_Type.__name__=_M
_HpSwitchSshReKeyStatus_Object=MibScalar
hpSwitchSshReKeyStatus=_HpSwitchSshReKeyStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,8),_HpSwitchSshReKeyStatus_Type())
hpSwitchSshReKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshReKeyStatus.setStatus(_A)
class _HpSwitchSshReKeyTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_HpSwitchSshReKeyTime_Type.__name__=_B
_HpSwitchSshReKeyTime_Object=MibScalar
hpSwitchSshReKeyTime=_HpSwitchSshReKeyTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,9),_HpSwitchSshReKeyTime_Type())
hpSwitchSshReKeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshReKeyTime.setStatus(_A)
class _HpSwitchSshReKeyVolume_Type(Integer32):defaultValue=1048576;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1048576))
_HpSwitchSshReKeyVolume_Type.__name__=_B
_HpSwitchSshReKeyVolume_Object=MibScalar
hpSwitchSshReKeyVolume=_HpSwitchSshReKeyVolume_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,10),_HpSwitchSshReKeyVolume_Type())
hpSwitchSshReKeyVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshReKeyVolume.setStatus(_A)
class _HpSwitchSshCipher_Type(Bits):defaultHexValue='03ff';namedValues=NamedValues(*(('aes128-cbc',0),('three-des-cbc',1),('aes192-cbc',2),('aes256-cbc',3),('rijndael-cbc',4),('aes128-ctr',5),('aes192-ctr',6),('aes256-ctr',7)))
_HpSwitchSshCipher_Type.__name__=_O
_HpSwitchSshCipher_Object=MibScalar
hpSwitchSshCipher=_HpSwitchSshCipher_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,11),_HpSwitchSshCipher_Type())
hpSwitchSshCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshCipher.setStatus(_A)
class _HpSwitchSshMAC_Type(Bits):defaultHexValue='3f';namedValues=NamedValues(*(('hmac-md5',0),('hmac-sha1',1),('hmac-sha1-96',2),('hmac-md5-96',3),('hmac-sha2-256',4)))
_HpSwitchSshMAC_Type.__name__=_O
_HpSwitchSshMAC_Object=MibScalar
hpSwitchSshMAC=_HpSwitchSshMAC_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,12),_HpSwitchSshMAC_Type())
hpSwitchSshMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshMAC.setStatus(_A)
class _HpSwitchSshKex_Type(Bits):defaultHexValue='ffffff';namedValues=NamedValues(*(('ecdh-sha2-nistp256',0),('ecdh-sha2-nistp384',1),('ecdh-sha2-nistp521',2),('diffie-hellman-group-exchange-sha256',3),('diffie-hellman-group14-sha1',4)))
_HpSwitchSshKex_Type.__name__=_O
_HpSwitchSshKex_Object=MibScalar
hpSwitchSshKex=_HpSwitchSshKex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,20,13),_HpSwitchSshKex_Type())
hpSwitchSshKex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchSshKex.setStatus(_A)
_HpSwitchPendingConfig_ObjectIdentity=ObjectIdentity
hpSwitchPendingConfig=_HpSwitchPendingConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,21))
class _HpSwitchPendingConfigControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('applyMstp',1),('resetMstp',2),('noAction',3)))
_HpSwitchPendingConfigControl_Type.__name__=_B
_HpSwitchPendingConfigControl_Object=MibScalar
hpSwitchPendingConfigControl=_HpSwitchPendingConfigControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,21,1),_HpSwitchPendingConfigControl_Type())
hpSwitchPendingConfigControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchPendingConfigControl.setStatus(_A)
_HpSwitchBWMinConfig_ObjectIdentity=ObjectIdentity
hpSwitchBWMinConfig=_HpSwitchBWMinConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22))
_HpSwitchBWMinEgressPortConfigTable_Object=MibTable
hpSwitchBWMinEgressPortConfigTable=_HpSwitchBWMinEgressPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1))
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortConfigTable.setStatus(_H)
_HpSwitchBWMinEgressPortConfigEntry_Object=MibTableRow
hpSwitchBWMinEgressPortConfigEntry=_HpSwitchBWMinEgressPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1))
hpSwitchBWMinEgressPortConfigEntry.setIndexNames((0,_G,_A3))
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortConfigEntry.setStatus(_H)
class _HpSwitchBWMinEgressPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchBWMinEgressPortIndex_Type.__name__=_B
_HpSwitchBWMinEgressPortIndex_Object=MibTableColumn
hpSwitchBWMinEgressPortIndex=_HpSwitchBWMinEgressPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1,1),_HpSwitchBWMinEgressPortIndex_Type())
hpSwitchBWMinEgressPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortIndex.setStatus(_H)
class _HpSwitchBWMinEgressPortPrctLowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchBWMinEgressPortPrctLowPriority_Type.__name__=_B
_HpSwitchBWMinEgressPortPrctLowPriority_Object=MibTableColumn
hpSwitchBWMinEgressPortPrctLowPriority=_HpSwitchBWMinEgressPortPrctLowPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1,2),_HpSwitchBWMinEgressPortPrctLowPriority_Type())
hpSwitchBWMinEgressPortPrctLowPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortPrctLowPriority.setStatus(_H)
class _HpSwitchBWMinEgressPortPrctNormalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchBWMinEgressPortPrctNormalPriority_Type.__name__=_B
_HpSwitchBWMinEgressPortPrctNormalPriority_Object=MibTableColumn
hpSwitchBWMinEgressPortPrctNormalPriority=_HpSwitchBWMinEgressPortPrctNormalPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1,3),_HpSwitchBWMinEgressPortPrctNormalPriority_Type())
hpSwitchBWMinEgressPortPrctNormalPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortPrctNormalPriority.setStatus(_H)
class _HpSwitchBWMinEgressPortPrctMedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchBWMinEgressPortPrctMedPriority_Type.__name__=_B
_HpSwitchBWMinEgressPortPrctMedPriority_Object=MibTableColumn
hpSwitchBWMinEgressPortPrctMedPriority=_HpSwitchBWMinEgressPortPrctMedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1,4),_HpSwitchBWMinEgressPortPrctMedPriority_Type())
hpSwitchBWMinEgressPortPrctMedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortPrctMedPriority.setStatus(_H)
class _HpSwitchBWMinEgressPortPrctHighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchBWMinEgressPortPrctHighPriority_Type.__name__=_B
_HpSwitchBWMinEgressPortPrctHighPriority_Object=MibTableColumn
hpSwitchBWMinEgressPortPrctHighPriority=_HpSwitchBWMinEgressPortPrctHighPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,22,1,1,5),_HpSwitchBWMinEgressPortPrctHighPriority_Type())
hpSwitchBWMinEgressPortPrctHighPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchBWMinEgressPortPrctHighPriority.setStatus(_H)
_HpSwitchRateLimitPortConfig_ObjectIdentity=ObjectIdentity
hpSwitchRateLimitPortConfig=_HpSwitchRateLimitPortConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23))
_HpSwitchRateLimitPortConfigTable_Object=MibTable
hpSwitchRateLimitPortConfigTable=_HpSwitchRateLimitPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1))
if mibBuilder.loadTexts:hpSwitchRateLimitPortConfigTable.setStatus(_A)
_HpSwitchRateLimitPortConfigEntry_Object=MibTableRow
hpSwitchRateLimitPortConfigEntry=_HpSwitchRateLimitPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1))
hpSwitchRateLimitPortConfigEntry.setIndexNames((0,_G,_A4))
if mibBuilder.loadTexts:hpSwitchRateLimitPortConfigEntry.setStatus(_A)
class _HpSwitchRateLimitPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchRateLimitPortIndex_Type.__name__=_B
_HpSwitchRateLimitPortIndex_Object=MibTableColumn
hpSwitchRateLimitPortIndex=_HpSwitchRateLimitPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,1),_HpSwitchRateLimitPortIndex_Type())
hpSwitchRateLimitPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchRateLimitPortIndex.setStatus(_A)
class _HpSwitchRateLimitPortControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('rateLimitPerPortOnly',2),('rateLimitPerQueue',3)))
_HpSwitchRateLimitPortControlMode_Type.__name__=_B
_HpSwitchRateLimitPortControlMode_Object=MibTableColumn
hpSwitchRateLimitPortControlMode=_HpSwitchRateLimitPortControlMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,2),_HpSwitchRateLimitPortControlMode_Type())
hpSwitchRateLimitPortControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortControlMode.setStatus(_A)
class _HpSwitchRateLimitPortSingleControlPrct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchRateLimitPortSingleControlPrct_Type.__name__=_B
_HpSwitchRateLimitPortSingleControlPrct_Object=MibTableColumn
hpSwitchRateLimitPortSingleControlPrct=_HpSwitchRateLimitPortSingleControlPrct_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,3),_HpSwitchRateLimitPortSingleControlPrct_Type())
hpSwitchRateLimitPortSingleControlPrct.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortSingleControlPrct.setStatus(_A)
class _HpSwitchRateLimitPortPrctLowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchRateLimitPortPrctLowPriority_Type.__name__=_B
_HpSwitchRateLimitPortPrctLowPriority_Object=MibTableColumn
hpSwitchRateLimitPortPrctLowPriority=_HpSwitchRateLimitPortPrctLowPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,4),_HpSwitchRateLimitPortPrctLowPriority_Type())
hpSwitchRateLimitPortPrctLowPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortPrctLowPriority.setStatus(_A)
class _HpSwitchRateLimitPortPrctNormalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchRateLimitPortPrctNormalPriority_Type.__name__=_B
_HpSwitchRateLimitPortPrctNormalPriority_Object=MibTableColumn
hpSwitchRateLimitPortPrctNormalPriority=_HpSwitchRateLimitPortPrctNormalPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,5),_HpSwitchRateLimitPortPrctNormalPriority_Type())
hpSwitchRateLimitPortPrctNormalPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortPrctNormalPriority.setStatus(_A)
class _HpSwitchRateLimitPortPrctMedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchRateLimitPortPrctMedPriority_Type.__name__=_B
_HpSwitchRateLimitPortPrctMedPriority_Object=MibTableColumn
hpSwitchRateLimitPortPrctMedPriority=_HpSwitchRateLimitPortPrctMedPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,6),_HpSwitchRateLimitPortPrctMedPriority_Type())
hpSwitchRateLimitPortPrctMedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortPrctMedPriority.setStatus(_A)
class _HpSwitchRateLimitPortPrctHighPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchRateLimitPortPrctHighPriority_Type.__name__=_B
_HpSwitchRateLimitPortPrctHighPriority_Object=MibTableColumn
hpSwitchRateLimitPortPrctHighPriority=_HpSwitchRateLimitPortPrctHighPriority_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,23,1,1,7),_HpSwitchRateLimitPortPrctHighPriority_Type())
hpSwitchRateLimitPortPrctHighPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRateLimitPortPrctHighPriority.setStatus(_A)
_HpSwitchQosPassThroughMode_ObjectIdentity=ObjectIdentity
hpSwitchQosPassThroughMode=_HpSwitchQosPassThroughMode_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,24))
class _HpSwitchQosPassThroughModeConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('optimized',1),('typical',2),('balanced',3),('onequeue',4)))
_HpSwitchQosPassThroughModeConfig_Type.__name__=_B
_HpSwitchQosPassThroughModeConfig_Object=MibScalar
hpSwitchQosPassThroughModeConfig=_HpSwitchQosPassThroughModeConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,24,1),_HpSwitchQosPassThroughModeConfig_Type())
hpSwitchQosPassThroughModeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchQosPassThroughModeConfig.setStatus(_A)
_HpSwitchReboot_ObjectIdentity=ObjectIdentity
hpSwitchReboot=_HpSwitchReboot_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,25))
class _HpSwitchRebootConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpSwitchRebootConfig_Type.__name__=_B
_HpSwitchRebootConfig_Object=MibScalar
hpSwitchRebootConfig=_HpSwitchRebootConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,25,1),_HpSwitchRebootConfig_Type())
hpSwitchRebootConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchRebootConfig.setStatus(_A)
class _HpSwitchRebootFastBoot_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchRebootFastBoot_Type.__name__=_B
_HpSwitchRebootFastBoot_Object=MibScalar
hpSwitchRebootFastBoot=_HpSwitchRebootFastBoot_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,25,2),_HpSwitchRebootFastBoot_Type())
hpSwitchRebootFastBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchRebootFastBoot.setStatus(_A)
_HpSwitchProtectedPortsConfig_ObjectIdentity=ObjectIdentity
hpSwitchProtectedPortsConfig=_HpSwitchProtectedPortsConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,26))
_HpSwitchProtectedPortsMask_Type=OctetString
_HpSwitchProtectedPortsMask_Object=MibScalar
hpSwitchProtectedPortsMask=_HpSwitchProtectedPortsMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,26,1),_HpSwitchProtectedPortsMask_Type())
hpSwitchProtectedPortsMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchProtectedPortsMask.setStatus(_A)
_HpSwitchLACPConfig_ObjectIdentity=ObjectIdentity
hpSwitchLACPConfig=_HpSwitchLACPConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,28))
class _HpSwitchLACPAllPortsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_R,2),(_d,3)))
_HpSwitchLACPAllPortsStatus_Type.__name__=_B
_HpSwitchLACPAllPortsStatus_Object=MibScalar
hpSwitchLACPAllPortsStatus=_HpSwitchLACPAllPortsStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,28,1),_HpSwitchLACPAllPortsStatus_Type())
hpSwitchLACPAllPortsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchLACPAllPortsStatus.setStatus(_A)
_HpSwitchDSCPRateLimitConfig_ObjectIdentity=ObjectIdentity
hpSwitchDSCPRateLimitConfig=_HpSwitchDSCPRateLimitConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31))
_HpSwitchDSCPRateLimitConfigTable_Object=MibTable
hpSwitchDSCPRateLimitConfigTable=_HpSwitchDSCPRateLimitConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31,1))
if mibBuilder.loadTexts:hpSwitchDSCPRateLimitConfigTable.setStatus(_A)
_HpSwitchDSCPRateLimitConfigEntry_Object=MibTableRow
hpSwitchDSCPRateLimitConfigEntry=_HpSwitchDSCPRateLimitConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31,1,1))
hpSwitchDSCPRateLimitConfigEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:hpSwitchDSCPRateLimitConfigEntry.setStatus(_A)
_HpSwitchDSCPRateLimitIndex_Type=Dscp
_HpSwitchDSCPRateLimitIndex_Object=MibTableColumn
hpSwitchDSCPRateLimitIndex=_HpSwitchDSCPRateLimitIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31,1,1,1),_HpSwitchDSCPRateLimitIndex_Type())
hpSwitchDSCPRateLimitIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:hpSwitchDSCPRateLimitIndex.setStatus(_A)
class _HpSwitchDSCPRateLimitKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,10000000))
_HpSwitchDSCPRateLimitKbps_Type.__name__=_B
_HpSwitchDSCPRateLimitKbps_Object=MibTableColumn
hpSwitchDSCPRateLimitKbps=_HpSwitchDSCPRateLimitKbps_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31,1,1,2),_HpSwitchDSCPRateLimitKbps_Type())
hpSwitchDSCPRateLimitKbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDSCPRateLimitKbps.setStatus(_A)
_HpSwitchDSCPRateLimitPorts_Type=PortList
_HpSwitchDSCPRateLimitPorts_Object=MibTableColumn
hpSwitchDSCPRateLimitPorts=_HpSwitchDSCPRateLimitPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,31,1,1,3),_HpSwitchDSCPRateLimitPorts_Type())
hpSwitchDSCPRateLimitPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDSCPRateLimitPorts.setStatus(_A)
_HpSwitchTcpPushPreserve_ObjectIdentity=ObjectIdentity
hpSwitchTcpPushPreserve=_HpSwitchTcpPushPreserve_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,33))
class _HpSwitchTcpPushPreserveConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_HpSwitchTcpPushPreserveConfig_Type.__name__=_B
_HpSwitchTcpPushPreserveConfig_Object=MibScalar
hpSwitchTcpPushPreserveConfig=_HpSwitchTcpPushPreserveConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,33,1),_HpSwitchTcpPushPreserveConfig_Type())
hpSwitchTcpPushPreserveConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTcpPushPreserveConfig.setStatus(_A)
_HpSwitchIfMau_ObjectIdentity=ObjectIdentity
hpSwitchIfMau=_HpSwitchIfMau_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,34))
_HpSwitchIfMauTypeListBits_Type=HpSwitchIfMauTypeListBits
_HpSwitchIfMauTypeListBits_Object=MibScalar
hpSwitchIfMauTypeListBits=_HpSwitchIfMauTypeListBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,34,1),_HpSwitchIfMauTypeListBits_Type())
hpSwitchIfMauTypeListBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIfMauTypeListBits.setStatus(_A)
_HpSwitchIfMauAutoNegCapabilityBits_Type=HpSwitchIfMauAutoNegCapabilityBits
_HpSwitchIfMauAutoNegCapabilityBits_Object=MibScalar
hpSwitchIfMauAutoNegCapabilityBits=_HpSwitchIfMauAutoNegCapabilityBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,34,2),_HpSwitchIfMauAutoNegCapabilityBits_Type())
hpSwitchIfMauAutoNegCapabilityBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIfMauAutoNegCapabilityBits.setStatus(_A)
_HpSwitchIfMauAutoNegCapAdvertisedBits_Type=HpSwitchIfMauAutoNegCapAdvertisedBits
_HpSwitchIfMauAutoNegCapAdvertisedBits_Object=MibScalar
hpSwitchIfMauAutoNegCapAdvertisedBits=_HpSwitchIfMauAutoNegCapAdvertisedBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,34,3),_HpSwitchIfMauAutoNegCapAdvertisedBits_Type())
hpSwitchIfMauAutoNegCapAdvertisedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIfMauAutoNegCapAdvertisedBits.setStatus(_A)
_HpSwitchIfMauAutoNegCapReceivedBits_Type=HpSwitchIfMauAutoNegCapReceivedBits
_HpSwitchIfMauAutoNegCapReceivedBits_Object=MibScalar
hpSwitchIfMauAutoNegCapReceivedBits=_HpSwitchIfMauAutoNegCapReceivedBits_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,34,4),_HpSwitchIfMauAutoNegCapReceivedBits_Type())
hpSwitchIfMauAutoNegCapReceivedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchIfMauAutoNegCapReceivedBits.setStatus(_A)
_HpSwitchTrunkConfig_ObjectIdentity=ObjectIdentity
hpSwitchTrunkConfig=_HpSwitchTrunkConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35))
_HpSwitchTrunkTable_Object=MibTable
hpSwitchTrunkTable=_HpSwitchTrunkTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35,1))
if mibBuilder.loadTexts:hpSwitchTrunkTable.setStatus(_A)
_HpSwitchTrunkEntry_Object=MibTableRow
hpSwitchTrunkEntry=_HpSwitchTrunkEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35,1,1))
hpSwitchTrunkEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:hpSwitchTrunkEntry.setStatus(_A)
class _HpSwitchTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchTrunkIndex_Type.__name__=_B
_HpSwitchTrunkIndex_Object=MibTableColumn
hpSwitchTrunkIndex=_HpSwitchTrunkIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35,1,1,1),_HpSwitchTrunkIndex_Type())
hpSwitchTrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpSwitchTrunkIndex.setStatus(_A)
class _HpSwitchTrunkMinActiveLinks_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HpSwitchTrunkMinActiveLinks_Type.__name__=_B
_HpSwitchTrunkMinActiveLinks_Object=MibTableColumn
hpSwitchTrunkMinActiveLinks=_HpSwitchTrunkMinActiveLinks_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35,1,1,2),_HpSwitchTrunkMinActiveLinks_Type())
hpSwitchTrunkMinActiveLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrunkMinActiveLinks.setStatus(_I)
class _HpSwitchTrunkLacpEnableTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_HpSwitchTrunkLacpEnableTimer_Type.__name__=_B
_HpSwitchTrunkLacpEnableTimer_Object=MibTableColumn
hpSwitchTrunkLacpEnableTimer=_HpSwitchTrunkLacpEnableTimer_Object((1,3,6,1,4,1,11,2,14,11,5,1,7,1,35,1,1,3),_HpSwitchTrunkLacpEnableTimer_Type())
hpSwitchTrunkLacpEnableTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrunkLacpEnableTimer.setStatus(_I)
hpSwitchStpErrantBpduReceived=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,7,1,0,0,1))
hpSwitchStpErrantBpduReceived.setObjects(*((_G,_U),(_G,_A7),(_Q,_Y),(_Q,_W),(_Q,_X),(_G,_A8),(_G,_A9)))
if mibBuilder.loadTexts:hpSwitchStpErrantBpduReceived.setStatus('')
mibBuilder.exportSymbols(_G,**{'VlanID':VlanID,'Timeout':Timeout,'HpicfUsrProfilePortSpeed':HpicfUsrProfilePortSpeed,'hpConfig':hpConfig,'hpSwitchConfig':hpSwitchConfig,'hpSwitchTraps':hpSwitchTraps,'hpSwitchStpErrantBpduReceived':hpSwitchStpErrantBpduReceived,'hpSwitchTrapsObjects':hpSwitchTrapsObjects,_A9:hpSwitchStpErrantBpduDetector,_A8:hpSwitchStpErrantBpduSrcMac,'hpSwitchSystemConfig':hpSwitchSystemConfig,'hpSwitchAutoReboot':hpSwitchAutoReboot,'hpSwitchTimeZone':hpSwitchTimeZone,'hpSwitchDaylightTimeRule':hpSwitchDaylightTimeRule,'hpSwitchDaylightBeginningMonth':hpSwitchDaylightBeginningMonth,'hpSwitchDaylightBeginningDay':hpSwitchDaylightBeginningDay,'hpSwitchDaylightEndingMonth':hpSwitchDaylightEndingMonth,'hpSwitchDaylightEndingDay':hpSwitchDaylightEndingDay,'hpSwitchSystemConfigStatus':hpSwitchSystemConfigStatus,'hpSwitchSystemPortLEDMode':hpSwitchSystemPortLEDMode,'hpSwitchControlUnknownIPMulticast':hpSwitchControlUnknownIPMulticast,'hpSwitchIgmpDelayedGroupFlushTimer':hpSwitchIgmpDelayedGroupFlushTimer,'hpSwitchMaxFrameSize':hpSwitchMaxFrameSize,'hpSwitchIpMTU':hpSwitchIpMTU,'hpSwitchAllowV1Modules':hpSwitchAllowV1Modules,'hpSwitchAllowV2Modules':hpSwitchAllowV2Modules,'hpicfPrivateVlanPromiscuousPorts':hpicfPrivateVlanPromiscuousPorts,'hpSwitchPreviewMode':hpSwitchPreviewMode,'hpSwitchHibernate':hpSwitchHibernate,'hpSwitchMacDelimiter':hpSwitchMacDelimiter,'hpicfSwitchCLIOptimization':hpicfSwitchCLIOptimization,'hpicfSwitchRMONLogThreshold':hpicfSwitchRMONLogThreshold,'hpSwitchConsoleConfig':hpSwitchConsoleConfig,'hpSwitchTelnetAdminStatus':hpSwitchTelnetAdminStatus,'hpSwitchTerminalType':hpSwitchTerminalType,'hpSwitchConsoleRefRate':hpSwitchConsoleRefRate,'hpSwitchDisplayedEvent':hpSwitchDisplayedEvent,'hpSwitchConsoleConfigStatus':hpSwitchConsoleConfigStatus,'hpSwitchConsoleConfigLogoutPrompt':hpSwitchConsoleConfigLogoutPrompt,'hpSwitchUsbConsoleAdminStatus':hpSwitchUsbConsoleAdminStatus,'hpSwitchSessionGlobalIdleTimeout':hpSwitchSessionGlobalIdleTimeout,'hpSwitchSessionConsoleIdleTimeout':hpSwitchSessionConsoleIdleTimeout,'hpSwitchMaxSessions':hpSwitchMaxSessions,'hpSwitchMaxUserSessions':hpSwitchMaxUserSessions,'hpSwitchPortConfig':hpSwitchPortConfig,'hpSwitchPortTable':hpSwitchPortTable,'hpSwitchPortEntry':hpSwitchPortEntry,_T:hpSwitchPortIndex,'hpSwitchPortType':hpSwitchPortType,'hpSwitchPortDescr':hpSwitchPortDescr,'hpSwitchPortAdminStatus':hpSwitchPortAdminStatus,'hpSwitchPortEtherMode':hpSwitchPortEtherMode,'hpSwitchPortVgMode':hpSwitchPortVgMode,'hpSwitchPortLinkbeat':hpSwitchPortLinkbeat,'hpSwitchPortTrunkGroup':hpSwitchPortTrunkGroup,'hpSwitchPortBcastLimit':hpSwitchPortBcastLimit,'hpSwitchPortFastEtherMode':hpSwitchPortFastEtherMode,'hpSwitchPortFlowControl':hpSwitchPortFlowControl,'hpSwitchPortTrunkType':hpSwitchPortTrunkType,'hpSwitchPortTrunkLACPStatus':hpSwitchPortTrunkLACPStatus,'hpSwitchPortMDIXStatus':hpSwitchPortMDIXStatus,'hpSwitchPortAutoMDIX':hpSwitchPortAutoMDIX,'hpSwitchPortLACPKey':hpSwitchPortLACPKey,'hpSwitchPortTrafficTemplateName':hpSwitchPortTrafficTemplateName,'hpSwitchPortEEEAdminStatus':hpSwitchPortEEEAdminStatus,'hpSwitchPortEEEOperStatus':hpSwitchPortEEEOperStatus,'hpSwitchPortEEECurrentTwSysTx':hpSwitchPortEEECurrentTwSysTx,'hpSwitchPortEEEMinTwSysTx':hpSwitchPortEEEMinTwSysTx,'hpSwitchPortEEEMaxTwSysTx':hpSwitchPortEEEMaxTwSysTx,'hpSwitchPortPvid':hpSwitchPortPvid,'hpSwitchPortTaggedVlanMap1k':hpSwitchPortTaggedVlanMap1k,'hpSwitchPortTaggedVlanMap2k':hpSwitchPortTaggedVlanMap2k,'hpSwitchPortTaggedVlanMap3k':hpSwitchPortTaggedVlanMap3k,'hpSwitchPortTaggedVlanMap4k':hpSwitchPortTaggedVlanMap4k,'hpSwitchPortEEECurrentTwSysTx1':hpSwitchPortEEECurrentTwSysTx1,'hpSwitchPortEEEMinTwSysTx1':hpSwitchPortEEEMinTwSysTx1,'hpSwitchPortEEEMaxTwSysTx1':hpSwitchPortEEEMaxTwSysTx1,'hpSwitchPortPtpAdminStatus':hpSwitchPortPtpAdminStatus,'hpSwitchPortPtpOperStatus':hpSwitchPortPtpOperStatus,'hpSwitchPortPtpRxCount':hpSwitchPortPtpRxCount,'hpSwitchPortPtpTxCount':hpSwitchPortPtpTxCount,'hpSwitchPortConfigStatus':hpSwitchPortConfigStatus,'hpSwitchLinkUpDownTrapAllPortsStatus':hpSwitchLinkUpDownTrapAllPortsStatus,'hpSwitchPortDevTypeTable':hpSwitchPortDevTypeTable,'hpSwitchPortDevTypeEntry':hpSwitchPortDevTypeEntry,'hpSwitchPortDevTypeNetworkDevice':hpSwitchPortDevTypeNetworkDevice,'hpSwitchIpxConfig':hpSwitchIpxConfig,'hpSwitchIpxConfigStatus':hpSwitchIpxConfigStatus,'hpSwitchIpConfig':hpSwitchIpConfig,'hpSwitchIpTimepAdminStatus':hpSwitchIpTimepAdminStatus,'hpSwitchIpTimepServerAddr':hpSwitchIpTimepServerAddr,'hpSwitchIpTimepPollInterval':hpSwitchIpTimepPollInterval,'hpSwitchIpConfigStatus':hpSwitchIpConfigStatus,'hpSwitchIpTftpMode':hpSwitchIpTftpMode,'hpSwitchIpTimepInetServerAddrType':hpSwitchIpTimepInetServerAddrType,'hpSwitchIpTimepInetServerAddr':hpSwitchIpTimepInetServerAddr,'hpSwitchIpTimepIsOobm':hpSwitchIpTimepIsOobm,'hpSwitchSerialLinkConfig':hpSwitchSerialLinkConfig,'hpSwitchSLinkBaudRate':hpSwitchSLinkBaudRate,'hpSwitchSLinkFlowCtrl':hpSwitchSLinkFlowCtrl,'hpSwitchSLinkConnInactTime':hpSwitchSLinkConnInactTime,'hpSwitchSLinkModemConnTime':hpSwitchSLinkModemConnTime,'hpSwitchSLinkModemLostRecvTime':hpSwitchSLinkModemLostRecvTime,'hpSwitchSLinkModemDisConnTime':hpSwitchSLinkModemDisConnTime,'hpSwitchSLinkParity':hpSwitchSLinkParity,'hpSwitchSLinkCharBits':hpSwitchSLinkCharBits,'hpSwitchSLinkStopBits':hpSwitchSLinkStopBits,'hpSwitchSLinkConfigStatus':hpSwitchSLinkConfigStatus,'hpSwitchFilterConfig':hpSwitchFilterConfig,'hpSwitchFilterConfigTable':hpSwitchFilterConfigTable,'hpSwitchFilterConfigEntry':hpSwitchFilterConfigEntry,_i:hpSwitchFilterIndex,'hpSwitchFilterType':hpSwitchFilterType,'hpSwitchFilterSrcPort':hpSwitchFilterSrcPort,'hpSwitchFilterMacAddr':hpSwitchFilterMacAddr,'hpSwitchFilterProtocolType':hpSwitchFilterProtocolType,'hpSwitchFilterPortMask':hpSwitchFilterPortMask,'hpSwitchFilterEntryStatus':hpSwitchFilterEntryStatus,'hpSwitchFilterName':hpSwitchFilterName,'hpSwitchProbeConfig':hpSwitchProbeConfig,'hpSwitchProbeType':hpSwitchProbeType,'hpSwitchProbedVlanId':hpSwitchProbedVlanId,'hpSwitchProbePort':hpSwitchProbePort,'hpSwitchProbeAdminStatus':hpSwitchProbeAdminStatus,'hpSwitchProbedPortMask':hpSwitchProbedPortMask,'hpSwitchFddiIpFragConfig':hpSwitchFddiIpFragConfig,'hpSwitchFddiIpFragConfigTable':hpSwitchFddiIpFragConfigTable,'hpSwitchFddiIpFragConfigEntry':hpSwitchFddiIpFragConfigEntry,_j:hpSwitchFddiIpFragConfigIndex,'hpSwitchFddiIpFragConfigStatus':hpSwitchFddiIpFragConfigStatus,'hpSwitchABCConfig':hpSwitchABCConfig,'hpSwitchABCConfigTable':hpSwitchABCConfigTable,'hpSwitchABCConfigEntry':hpSwitchABCConfigEntry,_k:hpSwitchABCConfigVlan,'hpSwitchABCConfigControl':hpSwitchABCConfigControl,'hpSwitchABCConfigIpRipControl':hpSwitchABCConfigIpRipControl,'hpSwitchABCConfigIpxRipSapControl':hpSwitchABCConfigIpxRipSapControl,'hpSwitchABCConfigVlanBcastLimit':hpSwitchABCConfigVlanBcastLimit,'hpSwitchABCConfigAutoGatewayConfig':hpSwitchABCConfigAutoGatewayConfig,'hpSwitchStpConfig':hpSwitchStpConfig,'hpSwitchStpVlanTable':hpSwitchStpVlanTable,'hpSwitchStpVlanEntry':hpSwitchStpVlanEntry,_l:hpSwitchStpVlan,'hpSwitchStpAdminStatus':hpSwitchStpAdminStatus,'hpSwitchStpPriority':hpSwitchStpPriority,'hpSwitchStpMaxAge':hpSwitchStpMaxAge,'hpSwitchStpHelloTime':hpSwitchStpHelloTime,'hpSwitchStpForwardDelay':hpSwitchStpForwardDelay,'hpSwitchStpPortTable':hpSwitchStpPortTable,'hpSwitchStpPortEntry':hpSwitchStpPortEntry,_U:hpSwitchStpPort,'hpSwitchStpPortType':hpSwitchStpPortType,'hpSwitchStpPortSrcMac':hpSwitchStpPortSrcMac,'hpSwitchStpPortPriority':hpSwitchStpPortPriority,'hpSwitchStpPortPathCost':hpSwitchStpPortPathCost,'hpSwitchStpPortMode':hpSwitchStpPortMode,'hpSwitchStpPortBpduFilter':hpSwitchStpPortBpduFilter,'hpSwitchStpPortBpduProtection':hpSwitchStpPortBpduProtection,_A7:hpSwitchStpPortErrantBpduCounter,'hpSwitchStpPortPvstFilter':hpSwitchStpPortPvstFilter,'hpSwitchStpPortPvstProtection':hpSwitchStpPortPvstProtection,'hpSwitchStpTrapCntl':hpSwitchStpTrapCntl,'hpSwitchStpBpduProtectionTimeout':hpSwitchStpBpduProtectionTimeout,'hpSwitchSTPAdminStatus':hpSwitchSTPAdminStatus,'hpicfSwitchSTPVersion':hpicfSwitchSTPVersion,'hpSwitchIgmpConfig':hpSwitchIgmpConfig,'hpSwitchIgmpConfigTable':hpSwitchIgmpConfigTable,'hpSwitchIgmpConfigEntry':hpSwitchIgmpConfigEntry,_n:hpSwitchIgmpVlanIndex,'hpSwitchIgmpState':hpSwitchIgmpState,'hpSwitchIgmpQuerierState':hpSwitchIgmpQuerierState,'hpSwitchIgmpPriorityState':hpSwitchIgmpPriorityState,'hpSwitchIgmpQuerierInterval':hpSwitchIgmpQuerierInterval,'hpSwitchIgmpProxyDomainMap':hpSwitchIgmpProxyDomainMap,'hpSwitchIgmpPortConfigTable':hpSwitchIgmpPortConfigTable,'hpSwitchIgmpPortConfigEntry':hpSwitchIgmpPortConfigEntry,_o:hpSwitchIgmpPortIndex,'hpSwitchIgmpPortType':hpSwitchIgmpPortType,'hpSwitchIgmpIpMcastState':hpSwitchIgmpIpMcastState,'hpSwitchIgmpPortConfigTable2':hpSwitchIgmpPortConfigTable2,'hpSwitchIgmpPortConfigEntry2':hpSwitchIgmpPortConfigEntry2,_r:hpSwitchIgmpPortVlanIndex2,_s:hpSwitchIgmpPortIndex2,'hpSwitchIgmpPortType2':hpSwitchIgmpPortType2,'hpSwitchIgmpIpMcastState2':hpSwitchIgmpIpMcastState2,'hpSwitchIgmpPortForcedLeaveState':hpSwitchIgmpPortForcedLeaveState,'hpSwitchIgmpPortFastLeaveState':hpSwitchIgmpPortFastLeaveState,'hpSwitchIgmpForcedLeaveInterval':hpSwitchIgmpForcedLeaveInterval,'hpSwitchCosConfig':hpSwitchCosConfig,'hpSwitchCosPortConfigTable':hpSwitchCosPortConfigTable,'hpSwitchCosPortConfigEntry':hpSwitchCosPortConfigEntry,_t:hpSwitchCosPortIndex,'hpSwitchCosPortType':hpSwitchCosPortType,'hpSwitchCosPortPriority':hpSwitchCosPortPriority,'hpSwitchCosPortDSCPPolicy':hpSwitchCosPortDSCPPolicy,'hpSwitchCosPortResolvedPriority':hpSwitchCosPortResolvedPriority,'hpSwitchCosPortApplyPolicy':hpSwitchCosPortApplyPolicy,'hpSwitchCosPortTrustMode':hpSwitchCosPortTrustMode,'hpSwitchCosPortPartnerDevice':hpSwitchCosPortPartnerDevice,'hpSwitchCosPortTrustedPartnerState':hpSwitchCosPortTrustedPartnerState,'hpSwitchCosVlanConfigTable':hpSwitchCosVlanConfigTable,'hpSwitchCosVlanConfigEntry':hpSwitchCosVlanConfigEntry,_v:hpSwitchCosVlanIndex,'hpSwitchCosVlanPriority':hpSwitchCosVlanPriority,'hpSwitchCosVlanDSCPPolicy':hpSwitchCosVlanDSCPPolicy,'hpSwitchCosVlanResolvedPriority':hpSwitchCosVlanResolvedPriority,'hpSwitchCosVlanApplyPolicy':hpSwitchCosVlanApplyPolicy,'hpSwitchCosProtocolConfigTable':hpSwitchCosProtocolConfigTable,'hpSwitchCosProtocolConfigEntry':hpSwitchCosProtocolConfigEntry,_w:hpSwitchCosProtocolType,'hpSwitchCosProtocolPriority':hpSwitchCosProtocolPriority,'hpSwitchCosAddressConfigTable':hpSwitchCosAddressConfigTable,'hpSwitchCosAddressConfigEntry':hpSwitchCosAddressConfigEntry,_x:hpSwitchCosAddressIndex,'hpSwitchCosAddressType':hpSwitchCosAddressType,'hpSwitchCosAddressIp':hpSwitchCosAddressIp,'hpSwitchCosAddressPriority':hpSwitchCosAddressPriority,'hpSwitchCosAddressStatus':hpSwitchCosAddressStatus,'hpSwitchCosAddressDSCPPolicy':hpSwitchCosAddressDSCPPolicy,'hpSwitchCosAddressResolvedPriority':hpSwitchCosAddressResolvedPriority,'hpSwitchCosAddressApplyPolicy':hpSwitchCosAddressApplyPolicy,'hpSwitchCosIpv4AddressMask':hpSwitchCosIpv4AddressMask,'hpSwitchCosAddressIpv6':hpSwitchCosAddressIpv6,'hpSwitchCosAddressIpv6PrefixLength':hpSwitchCosAddressIpv6PrefixLength,'hpSwitchCosTosConfig':hpSwitchCosTosConfig,'hpSwitchCosTosConfigMode':hpSwitchCosTosConfigMode,'hpSwitchCosTosConfigTable':hpSwitchCosTosConfigTable,'hpSwitchCosTosConfigEntry':hpSwitchCosTosConfigEntry,_y:hpSwitchCosTosIndex,'hpSwitchCosTosPriority':hpSwitchCosTosPriority,'hpSwitchCosTosDSCPPolicy':hpSwitchCosTosDSCPPolicy,'hpSwitchCosTosResolvedPriority':hpSwitchCosTosResolvedPriority,'hpSwitchCosTosApplyPolicy':hpSwitchCosTosApplyPolicy,'hpSwitchCosDSCPPolicyConfigTable':hpSwitchCosDSCPPolicyConfigTable,'hpSwitchCosDSCPPolicyConfigEntry':hpSwitchCosDSCPPolicyConfigEntry,_z:hpSwitchCosDSCPPolicyIndex,'hpSwitchCosDSCPPolicyPriority':hpSwitchCosDSCPPolicyPriority,'hpSwitchCosDSCPPolicyName':hpSwitchCosDSCPPolicyName,'hpSwitchCosAppTypeConfigTable':hpSwitchCosAppTypeConfigTable,'hpSwitchCosAppTypeConfigEntry':hpSwitchCosAppTypeConfigEntry,_A0:hpSwitchCosAppTypeConfigIndex,'hpSwitchCosAppTypeConfigType':hpSwitchCosAppTypeConfigType,'hpSwitchCosAppTypeSrcPort':hpSwitchCosAppTypeSrcPort,'hpSwitchCosAppTypeDestPort':hpSwitchCosAppTypeDestPort,'hpSwitchCosAppTypePriority':hpSwitchCosAppTypePriority,'hpSwitchCosAppTypeDSCPPolicy':hpSwitchCosAppTypeDSCPPolicy,'hpSwitchCosAppTypeResolvedPriority':hpSwitchCosAppTypeResolvedPriority,'hpSwitchCosAppTypeApplyPolicy':hpSwitchCosAppTypeApplyPolicy,'hpSwitchCosAppTypeStatus':hpSwitchCosAppTypeStatus,'hpSwitchCosAppTypeMaxSrcPort':hpSwitchCosAppTypeMaxSrcPort,'hpSwitchCosAppTypeMaxDestPort':hpSwitchCosAppTypeMaxDestPort,'hpSwitchCosAppTypeIpPacketType':hpSwitchCosAppTypeIpPacketType,'hpSwitchCosLastChange':hpSwitchCosLastChange,'hpSwitchConfigCosLastConfigError':hpSwitchConfigCosLastConfigError,'hpSwitchQueueWatchTable':hpSwitchQueueWatchTable,'hpSwitchQueueWatchEntry':hpSwitchQueueWatchEntry,_A1:hpSwitchQueueWatchPort,'hpSwitchQueueWatchState':hpSwitchQueueWatchState,'hpSwitchMeshConfig':hpSwitchMeshConfig,'hpSwitchMeshMulticastAgingMode':hpSwitchMeshMulticastAgingMode,'hpSwitchMeshBackwardCompatibility':hpSwitchMeshBackwardCompatibility,'hpSwitchMeshConfiguredId':hpSwitchMeshConfiguredId,'hpSwitchMeshActualId':hpSwitchMeshActualId,'hpSwitchPortIsolationConfig':hpSwitchPortIsolationConfig,'hpSwitchPortIsolationMode':hpSwitchPortIsolationMode,'hpSwitchPortIsolationConfigTable':hpSwitchPortIsolationConfigTable,'hpSwitchPortIsolationConfigEntry':hpSwitchPortIsolationConfigEntry,_A2:hpSwitchPortIsolationPort,'hpSwitchPortIsolationPortMode':hpSwitchPortIsolationPortMode,'hpSwitchSshConfig':hpSwitchSshConfig,'hpSwitchSshAdminStatus':hpSwitchSshAdminStatus,'hpSwitchSshVersion':hpSwitchSshVersion,'hpSwitchSshTimeout':hpSwitchSshTimeout,'hpSwitchSshPortNumber':hpSwitchSshPortNumber,'hpSwitchSshServerKeySize':hpSwitchSshServerKeySize,'hpSwitchSshFileServerAdminStatus':hpSwitchSshFileServerAdminStatus,'hpSwitchSshIpVersion':hpSwitchSshIpVersion,'hpSwitchSshReKeyStatus':hpSwitchSshReKeyStatus,'hpSwitchSshReKeyTime':hpSwitchSshReKeyTime,'hpSwitchSshReKeyVolume':hpSwitchSshReKeyVolume,'hpSwitchSshCipher':hpSwitchSshCipher,'hpSwitchSshMAC':hpSwitchSshMAC,'hpSwitchSshKex':hpSwitchSshKex,'hpSwitchPendingConfig':hpSwitchPendingConfig,'hpSwitchPendingConfigControl':hpSwitchPendingConfigControl,'hpSwitchBWMinConfig':hpSwitchBWMinConfig,'hpSwitchBWMinEgressPortConfigTable':hpSwitchBWMinEgressPortConfigTable,'hpSwitchBWMinEgressPortConfigEntry':hpSwitchBWMinEgressPortConfigEntry,_A3:hpSwitchBWMinEgressPortIndex,'hpSwitchBWMinEgressPortPrctLowPriority':hpSwitchBWMinEgressPortPrctLowPriority,'hpSwitchBWMinEgressPortPrctNormalPriority':hpSwitchBWMinEgressPortPrctNormalPriority,'hpSwitchBWMinEgressPortPrctMedPriority':hpSwitchBWMinEgressPortPrctMedPriority,'hpSwitchBWMinEgressPortPrctHighPriority':hpSwitchBWMinEgressPortPrctHighPriority,'hpSwitchRateLimitPortConfig':hpSwitchRateLimitPortConfig,'hpSwitchRateLimitPortConfigTable':hpSwitchRateLimitPortConfigTable,'hpSwitchRateLimitPortConfigEntry':hpSwitchRateLimitPortConfigEntry,_A4:hpSwitchRateLimitPortIndex,'hpSwitchRateLimitPortControlMode':hpSwitchRateLimitPortControlMode,'hpSwitchRateLimitPortSingleControlPrct':hpSwitchRateLimitPortSingleControlPrct,'hpSwitchRateLimitPortPrctLowPriority':hpSwitchRateLimitPortPrctLowPriority,'hpSwitchRateLimitPortPrctNormalPriority':hpSwitchRateLimitPortPrctNormalPriority,'hpSwitchRateLimitPortPrctMedPriority':hpSwitchRateLimitPortPrctMedPriority,'hpSwitchRateLimitPortPrctHighPriority':hpSwitchRateLimitPortPrctHighPriority,'hpSwitchQosPassThroughMode':hpSwitchQosPassThroughMode,'hpSwitchQosPassThroughModeConfig':hpSwitchQosPassThroughModeConfig,'hpSwitchReboot':hpSwitchReboot,'hpSwitchRebootConfig':hpSwitchRebootConfig,'hpSwitchRebootFastBoot':hpSwitchRebootFastBoot,'hpSwitchProtectedPortsConfig':hpSwitchProtectedPortsConfig,'hpSwitchProtectedPortsMask':hpSwitchProtectedPortsMask,'hpSwitchLACPConfig':hpSwitchLACPConfig,'hpSwitchLACPAllPortsStatus':hpSwitchLACPAllPortsStatus,'hpSwitchDSCPRateLimitConfig':hpSwitchDSCPRateLimitConfig,'hpSwitchDSCPRateLimitConfigTable':hpSwitchDSCPRateLimitConfigTable,'hpSwitchDSCPRateLimitConfigEntry':hpSwitchDSCPRateLimitConfigEntry,_A5:hpSwitchDSCPRateLimitIndex,'hpSwitchDSCPRateLimitKbps':hpSwitchDSCPRateLimitKbps,'hpSwitchDSCPRateLimitPorts':hpSwitchDSCPRateLimitPorts,'hpSwitchTcpPushPreserve':hpSwitchTcpPushPreserve,'hpSwitchTcpPushPreserveConfig':hpSwitchTcpPushPreserveConfig,'hpSwitchIfMau':hpSwitchIfMau,'hpSwitchIfMauTypeListBits':hpSwitchIfMauTypeListBits,'hpSwitchIfMauAutoNegCapabilityBits':hpSwitchIfMauAutoNegCapabilityBits,'hpSwitchIfMauAutoNegCapAdvertisedBits':hpSwitchIfMauAutoNegCapAdvertisedBits,'hpSwitchIfMauAutoNegCapReceivedBits':hpSwitchIfMauAutoNegCapReceivedBits,'hpSwitchTrunkConfig':hpSwitchTrunkConfig,'hpSwitchTrunkTable':hpSwitchTrunkTable,'hpSwitchTrunkEntry':hpSwitchTrunkEntry,_A6:hpSwitchTrunkIndex,'hpSwitchTrunkMinActiveLinks':hpSwitchTrunkMinActiveLinks,'hpSwitchTrunkLacpEnableTimer':hpSwitchTrunkLacpEnableTimer})