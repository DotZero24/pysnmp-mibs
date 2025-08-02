_z='channelStatisticsEpChannelId'
_y='lastPeriodsStatsPeriodIndex'
_x='lastConnectionsStatsConnectionsIndex'
_w='epSpecificSecurityEpId'
_v='aesCm128'
_u='secureWithFallback'
_t='secure'
_s='unsecure'
_r='defaultCodecVsBearerCapabilitiesMappingIndex'
_q='epSpecificDtmfTransportEpId'
_p='signalingProtocolDependent'
_o='outOfBandUsingSignalingProtocol'
_n='outOfBandUsingRtp'
_m='inBand'
_l='epSpecificJitterBufferEpId'
_k='adaptiveSilence'
_j='adaptiveImmediately'
_i='custom'
_h='faxModem'
_g='optimizeQuality'
_f='normal'
_e='optimizeLatency'
_d='epSpecificCodecXCCDEpId'
_c='epSpecificCodecClearChannelEpId'
_b='epSpecificCodecClearModeEpId'
_a='epSpecificCodecT38EpId'
_Z='lowest'
_Y='default'
_X='epSpecificCodecG729EpId'
_W='epSpecificCodecG726r40kbpsEpId'
_V='epSpecificCodecG726r32kbpsEpId'
_U='epSpecificCodecG726r24kbpsEpId'
_T='epSpecificCodecG726r16kbpsEpId'
_S='epSpecificCodecG723EpId'
_R='rate63kbps'
_Q='rate53kbps'
_P='epSpecificCodecG722EpId'
_O='epSpecificCodecG711AlawEpId'
_N='epSpecificCodecG711MulawEpId'
_M='epSpecificCodecEpId'
_L='conservative'
_K='transparent'
_J='MxIpAddress'
_I='OctetString'
_H='disable'
_G='MX-MIPT-MIB'
_F='Integer32'
_E='read-only'
_D='MxEnableState'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_D,_J,'MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
miptMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600))
_MiptMIBObjects_ObjectIdentity=ObjectIdentity
miptMIBObjects=_MiptMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1))
_CodecGroup_ObjectIdentity=ObjectIdentity
codecGroup=_CodecGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100))
class _DefaultCodecGenericVoiceActivityDetection_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),(_K,200),(_L,300)))
_DefaultCodecGenericVoiceActivityDetection_Type.__name__=_F
_DefaultCodecGenericVoiceActivityDetection_Object=MibScalar
defaultCodecGenericVoiceActivityDetection=_DefaultCodecGenericVoiceActivityDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,100),_DefaultCodecGenericVoiceActivityDetection_Type())
defaultCodecGenericVoiceActivityDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecGenericVoiceActivityDetection.setStatus(_A)
_EpSpecificCodecTable_Object=MibTable
epSpecificCodecTable=_EpSpecificCodecTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,200))
if mibBuilder.loadTexts:epSpecificCodecTable.setStatus(_A)
_EpSpecificCodecEntry_Object=MibTableRow
epSpecificCodecEntry=_EpSpecificCodecEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,200,1))
epSpecificCodecEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:epSpecificCodecEntry.setStatus(_A)
_EpSpecificCodecEpId_Type=OctetString
_EpSpecificCodecEpId_Object=MibTableColumn
epSpecificCodecEpId=_EpSpecificCodecEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,200,1,100),_EpSpecificCodecEpId_Type())
epSpecificCodecEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecEpId.setStatus(_A)
class _EpSpecificCodecEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecEnableConfig_Type.__name__=_D
_EpSpecificCodecEnableConfig_Object=MibTableColumn
epSpecificCodecEnableConfig=_EpSpecificCodecEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,200,1,200),_EpSpecificCodecEnableConfig_Type())
epSpecificCodecEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecEnableConfig.setStatus(_A)
class _EpSpecificCodecGenericVoiceActivityDetection_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_H,100),(_K,200),(_L,300)))
_EpSpecificCodecGenericVoiceActivityDetection_Type.__name__=_F
_EpSpecificCodecGenericVoiceActivityDetection_Object=MibTableColumn
epSpecificCodecGenericVoiceActivityDetection=_EpSpecificCodecGenericVoiceActivityDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,200,1,300),_EpSpecificCodecGenericVoiceActivityDetection_Type())
epSpecificCodecGenericVoiceActivityDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecGenericVoiceActivityDetection.setStatus(_A)
_CodecG711Group_ObjectIdentity=ObjectIdentity
codecG711Group=_CodecG711Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300))
_CodecG711MulawGroup_ObjectIdentity=ObjectIdentity
codecG711MulawGroup=_CodecG711MulawGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100))
class _DefaultCodecG711MulawVoiceEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG711MulawVoiceEnable_Type.__name__=_D
_DefaultCodecG711MulawVoiceEnable_Object=MibScalar
defaultCodecG711MulawVoiceEnable=_DefaultCodecG711MulawVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,100),_DefaultCodecG711MulawVoiceEnable_Type())
defaultCodecG711MulawVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawVoiceEnable.setStatus(_A)
class _DefaultCodecG711MulawVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG711MulawVoicePriority_Type.__name__=_C
_DefaultCodecG711MulawVoicePriority_Object=MibScalar
defaultCodecG711MulawVoicePriority=_DefaultCodecG711MulawVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,200),_DefaultCodecG711MulawVoicePriority_Type())
defaultCodecG711MulawVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawVoicePriority.setStatus(_A)
class _DefaultCodecG711MulawDataEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG711MulawDataEnable_Type.__name__=_D
_DefaultCodecG711MulawDataEnable_Object=MibScalar
defaultCodecG711MulawDataEnable=_DefaultCodecG711MulawDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,300),_DefaultCodecG711MulawDataEnable_Type())
defaultCodecG711MulawDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawDataEnable.setStatus(_A)
class _DefaultCodecG711MulawDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG711MulawDataPriority_Type.__name__=_C
_DefaultCodecG711MulawDataPriority_Object=MibScalar
defaultCodecG711MulawDataPriority=_DefaultCodecG711MulawDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,400),_DefaultCodecG711MulawDataPriority_Type())
defaultCodecG711MulawDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawDataPriority.setStatus(_A)
class _DefaultCodecG711MulawMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG711MulawMinPTime_Type.__name__=_C
_DefaultCodecG711MulawMinPTime_Object=MibScalar
defaultCodecG711MulawMinPTime=_DefaultCodecG711MulawMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,500),_DefaultCodecG711MulawMinPTime_Type())
defaultCodecG711MulawMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawMinPTime.setStatus(_A)
class _DefaultCodecG711MulawMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG711MulawMaxPTime_Type.__name__=_C
_DefaultCodecG711MulawMaxPTime_Object=MibScalar
defaultCodecG711MulawMaxPTime=_DefaultCodecG711MulawMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,600),_DefaultCodecG711MulawMaxPTime_Type())
defaultCodecG711MulawMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711MulawMaxPTime.setStatus(_A)
_EpSpecificCodecG711MulawTable_Object=MibTable
epSpecificCodecG711MulawTable=_EpSpecificCodecG711MulawTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700))
if mibBuilder.loadTexts:epSpecificCodecG711MulawTable.setStatus(_A)
_EpSpecificCodecG711MulawEntry_Object=MibTableRow
epSpecificCodecG711MulawEntry=_EpSpecificCodecG711MulawEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1))
epSpecificCodecG711MulawEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:epSpecificCodecG711MulawEntry.setStatus(_A)
_EpSpecificCodecG711MulawEpId_Type=OctetString
_EpSpecificCodecG711MulawEpId_Object=MibTableColumn
epSpecificCodecG711MulawEpId=_EpSpecificCodecG711MulawEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,100),_EpSpecificCodecG711MulawEpId_Type())
epSpecificCodecG711MulawEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG711MulawEpId.setStatus(_A)
class _EpSpecificCodecG711MulawEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG711MulawEnableConfig_Type.__name__=_D
_EpSpecificCodecG711MulawEnableConfig_Object=MibTableColumn
epSpecificCodecG711MulawEnableConfig=_EpSpecificCodecG711MulawEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,200),_EpSpecificCodecG711MulawEnableConfig_Type())
epSpecificCodecG711MulawEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawEnableConfig.setStatus(_A)
class _EpSpecificCodecG711MulawVoiceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG711MulawVoiceEnable_Type.__name__=_D
_EpSpecificCodecG711MulawVoiceEnable_Object=MibTableColumn
epSpecificCodecG711MulawVoiceEnable=_EpSpecificCodecG711MulawVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,300),_EpSpecificCodecG711MulawVoiceEnable_Type())
epSpecificCodecG711MulawVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawVoiceEnable.setStatus(_A)
class _EpSpecificCodecG711MulawVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG711MulawVoicePriority_Type.__name__=_C
_EpSpecificCodecG711MulawVoicePriority_Object=MibTableColumn
epSpecificCodecG711MulawVoicePriority=_EpSpecificCodecG711MulawVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,400),_EpSpecificCodecG711MulawVoicePriority_Type())
epSpecificCodecG711MulawVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawVoicePriority.setStatus(_A)
class _EpSpecificCodecG711MulawDataEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG711MulawDataEnable_Type.__name__=_D
_EpSpecificCodecG711MulawDataEnable_Object=MibTableColumn
epSpecificCodecG711MulawDataEnable=_EpSpecificCodecG711MulawDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,500),_EpSpecificCodecG711MulawDataEnable_Type())
epSpecificCodecG711MulawDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawDataEnable.setStatus(_A)
class _EpSpecificCodecG711MulawDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG711MulawDataPriority_Type.__name__=_C
_EpSpecificCodecG711MulawDataPriority_Object=MibTableColumn
epSpecificCodecG711MulawDataPriority=_EpSpecificCodecG711MulawDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,600),_EpSpecificCodecG711MulawDataPriority_Type())
epSpecificCodecG711MulawDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawDataPriority.setStatus(_A)
class _EpSpecificCodecG711MulawMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG711MulawMinPTime_Type.__name__=_C
_EpSpecificCodecG711MulawMinPTime_Object=MibTableColumn
epSpecificCodecG711MulawMinPTime=_EpSpecificCodecG711MulawMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,700),_EpSpecificCodecG711MulawMinPTime_Type())
epSpecificCodecG711MulawMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawMinPTime.setStatus(_A)
class _EpSpecificCodecG711MulawMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG711MulawMaxPTime_Type.__name__=_C
_EpSpecificCodecG711MulawMaxPTime_Object=MibTableColumn
epSpecificCodecG711MulawMaxPTime=_EpSpecificCodecG711MulawMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,100,700,1,800),_EpSpecificCodecG711MulawMaxPTime_Type())
epSpecificCodecG711MulawMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711MulawMaxPTime.setStatus(_A)
_CodecG711AlawGroup_ObjectIdentity=ObjectIdentity
codecG711AlawGroup=_CodecG711AlawGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200))
class _DefaultCodecG711AlawVoiceEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG711AlawVoiceEnable_Type.__name__=_D
_DefaultCodecG711AlawVoiceEnable_Object=MibScalar
defaultCodecG711AlawVoiceEnable=_DefaultCodecG711AlawVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,100),_DefaultCodecG711AlawVoiceEnable_Type())
defaultCodecG711AlawVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawVoiceEnable.setStatus(_A)
class _DefaultCodecG711AlawVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG711AlawVoicePriority_Type.__name__=_C
_DefaultCodecG711AlawVoicePriority_Object=MibScalar
defaultCodecG711AlawVoicePriority=_DefaultCodecG711AlawVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,200),_DefaultCodecG711AlawVoicePriority_Type())
defaultCodecG711AlawVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawVoicePriority.setStatus(_A)
class _DefaultCodecG711AlawDataEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG711AlawDataEnable_Type.__name__=_D
_DefaultCodecG711AlawDataEnable_Object=MibScalar
defaultCodecG711AlawDataEnable=_DefaultCodecG711AlawDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,300),_DefaultCodecG711AlawDataEnable_Type())
defaultCodecG711AlawDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawDataEnable.setStatus(_A)
class _DefaultCodecG711AlawDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG711AlawDataPriority_Type.__name__=_C
_DefaultCodecG711AlawDataPriority_Object=MibScalar
defaultCodecG711AlawDataPriority=_DefaultCodecG711AlawDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,400),_DefaultCodecG711AlawDataPriority_Type())
defaultCodecG711AlawDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawDataPriority.setStatus(_A)
class _DefaultCodecG711AlawMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG711AlawMinPTime_Type.__name__=_C
_DefaultCodecG711AlawMinPTime_Object=MibScalar
defaultCodecG711AlawMinPTime=_DefaultCodecG711AlawMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,500),_DefaultCodecG711AlawMinPTime_Type())
defaultCodecG711AlawMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawMinPTime.setStatus(_A)
class _DefaultCodecG711AlawMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG711AlawMaxPTime_Type.__name__=_C
_DefaultCodecG711AlawMaxPTime_Object=MibScalar
defaultCodecG711AlawMaxPTime=_DefaultCodecG711AlawMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,600),_DefaultCodecG711AlawMaxPTime_Type())
defaultCodecG711AlawMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG711AlawMaxPTime.setStatus(_A)
_EpSpecificCodecG711AlawTable_Object=MibTable
epSpecificCodecG711AlawTable=_EpSpecificCodecG711AlawTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700))
if mibBuilder.loadTexts:epSpecificCodecG711AlawTable.setStatus(_A)
_EpSpecificCodecG711AlawEntry_Object=MibTableRow
epSpecificCodecG711AlawEntry=_EpSpecificCodecG711AlawEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1))
epSpecificCodecG711AlawEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:epSpecificCodecG711AlawEntry.setStatus(_A)
_EpSpecificCodecG711AlawEpId_Type=OctetString
_EpSpecificCodecG711AlawEpId_Object=MibTableColumn
epSpecificCodecG711AlawEpId=_EpSpecificCodecG711AlawEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,100),_EpSpecificCodecG711AlawEpId_Type())
epSpecificCodecG711AlawEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG711AlawEpId.setStatus(_A)
class _EpSpecificCodecG711AlawEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG711AlawEnableConfig_Type.__name__=_D
_EpSpecificCodecG711AlawEnableConfig_Object=MibTableColumn
epSpecificCodecG711AlawEnableConfig=_EpSpecificCodecG711AlawEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,200),_EpSpecificCodecG711AlawEnableConfig_Type())
epSpecificCodecG711AlawEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawEnableConfig.setStatus(_A)
class _EpSpecificCodecG711AlawVoiceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG711AlawVoiceEnable_Type.__name__=_D
_EpSpecificCodecG711AlawVoiceEnable_Object=MibTableColumn
epSpecificCodecG711AlawVoiceEnable=_EpSpecificCodecG711AlawVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,300),_EpSpecificCodecG711AlawVoiceEnable_Type())
epSpecificCodecG711AlawVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawVoiceEnable.setStatus(_A)
class _EpSpecificCodecG711AlawVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG711AlawVoicePriority_Type.__name__=_C
_EpSpecificCodecG711AlawVoicePriority_Object=MibTableColumn
epSpecificCodecG711AlawVoicePriority=_EpSpecificCodecG711AlawVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,400),_EpSpecificCodecG711AlawVoicePriority_Type())
epSpecificCodecG711AlawVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawVoicePriority.setStatus(_A)
class _EpSpecificCodecG711AlawDataEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG711AlawDataEnable_Type.__name__=_D
_EpSpecificCodecG711AlawDataEnable_Object=MibTableColumn
epSpecificCodecG711AlawDataEnable=_EpSpecificCodecG711AlawDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,500),_EpSpecificCodecG711AlawDataEnable_Type())
epSpecificCodecG711AlawDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawDataEnable.setStatus(_A)
class _EpSpecificCodecG711AlawDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG711AlawDataPriority_Type.__name__=_C
_EpSpecificCodecG711AlawDataPriority_Object=MibTableColumn
epSpecificCodecG711AlawDataPriority=_EpSpecificCodecG711AlawDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,600),_EpSpecificCodecG711AlawDataPriority_Type())
epSpecificCodecG711AlawDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawDataPriority.setStatus(_A)
class _EpSpecificCodecG711AlawMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG711AlawMinPTime_Type.__name__=_C
_EpSpecificCodecG711AlawMinPTime_Object=MibTableColumn
epSpecificCodecG711AlawMinPTime=_EpSpecificCodecG711AlawMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,700),_EpSpecificCodecG711AlawMinPTime_Type())
epSpecificCodecG711AlawMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawMinPTime.setStatus(_A)
class _EpSpecificCodecG711AlawMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG711AlawMaxPTime_Type.__name__=_C
_EpSpecificCodecG711AlawMaxPTime_Object=MibTableColumn
epSpecificCodecG711AlawMaxPTime=_EpSpecificCodecG711AlawMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,300,200,700,1,800),_EpSpecificCodecG711AlawMaxPTime_Type())
epSpecificCodecG711AlawMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG711AlawMaxPTime.setStatus(_A)
_CodecG722Group_ObjectIdentity=ObjectIdentity
codecG722Group=_CodecG722Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350))
class _DefaultCodecG722VoiceEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG722VoiceEnable_Type.__name__=_D
_DefaultCodecG722VoiceEnable_Object=MibScalar
defaultCodecG722VoiceEnable=_DefaultCodecG722VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,100),_DefaultCodecG722VoiceEnable_Type())
defaultCodecG722VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG722VoiceEnable.setStatus(_A)
class _DefaultCodecG722VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG722VoicePriority_Type.__name__=_C
_DefaultCodecG722VoicePriority_Object=MibScalar
defaultCodecG722VoicePriority=_DefaultCodecG722VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,200),_DefaultCodecG722VoicePriority_Type())
defaultCodecG722VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG722VoicePriority.setStatus(_A)
class _DefaultCodecG722MinPTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20))
_DefaultCodecG722MinPTime_Type.__name__=_C
_DefaultCodecG722MinPTime_Object=MibScalar
defaultCodecG722MinPTime=_DefaultCodecG722MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,300),_DefaultCodecG722MinPTime_Type())
defaultCodecG722MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG722MinPTime.setStatus(_A)
class _DefaultCodecG722MaxPTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20))
_DefaultCodecG722MaxPTime_Type.__name__=_C
_DefaultCodecG722MaxPTime_Object=MibScalar
defaultCodecG722MaxPTime=_DefaultCodecG722MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,400),_DefaultCodecG722MaxPTime_Type())
defaultCodecG722MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG722MaxPTime.setStatus(_A)
_EpSpecificCodecG722Table_Object=MibTable
epSpecificCodecG722Table=_EpSpecificCodecG722Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500))
if mibBuilder.loadTexts:epSpecificCodecG722Table.setStatus(_A)
_EpSpecificCodecG722Entry_Object=MibTableRow
epSpecificCodecG722Entry=_EpSpecificCodecG722Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1))
epSpecificCodecG722Entry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:epSpecificCodecG722Entry.setStatus(_A)
_EpSpecificCodecG722EpId_Type=OctetString
_EpSpecificCodecG722EpId_Object=MibTableColumn
epSpecificCodecG722EpId=_EpSpecificCodecG722EpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,100),_EpSpecificCodecG722EpId_Type())
epSpecificCodecG722EpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG722EpId.setStatus(_A)
class _EpSpecificCodecG722EnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG722EnableConfig_Type.__name__=_D
_EpSpecificCodecG722EnableConfig_Object=MibTableColumn
epSpecificCodecG722EnableConfig=_EpSpecificCodecG722EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,200),_EpSpecificCodecG722EnableConfig_Type())
epSpecificCodecG722EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG722EnableConfig.setStatus(_A)
class _EpSpecificCodecG722VoiceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG722VoiceEnable_Type.__name__=_D
_EpSpecificCodecG722VoiceEnable_Object=MibTableColumn
epSpecificCodecG722VoiceEnable=_EpSpecificCodecG722VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,300),_EpSpecificCodecG722VoiceEnable_Type())
epSpecificCodecG722VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG722VoiceEnable.setStatus(_A)
class _EpSpecificCodecG722VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG722VoicePriority_Type.__name__=_C
_EpSpecificCodecG722VoicePriority_Object=MibTableColumn
epSpecificCodecG722VoicePriority=_EpSpecificCodecG722VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,400),_EpSpecificCodecG722VoicePriority_Type())
epSpecificCodecG722VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG722VoicePriority.setStatus(_A)
class _EpSpecificCodecG722MinPTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20))
_EpSpecificCodecG722MinPTime_Type.__name__=_C
_EpSpecificCodecG722MinPTime_Object=MibTableColumn
epSpecificCodecG722MinPTime=_EpSpecificCodecG722MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,500),_EpSpecificCodecG722MinPTime_Type())
epSpecificCodecG722MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG722MinPTime.setStatus(_A)
class _EpSpecificCodecG722MaxPTime_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20))
_EpSpecificCodecG722MaxPTime_Type.__name__=_C
_EpSpecificCodecG722MaxPTime_Object=MibTableColumn
epSpecificCodecG722MaxPTime=_EpSpecificCodecG722MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,350,500,1,600),_EpSpecificCodecG722MaxPTime_Type())
epSpecificCodecG722MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG722MaxPTime.setStatus(_A)
_CodecG723Group_ObjectIdentity=ObjectIdentity
codecG723Group=_CodecG723Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400))
class _DefaultCodecG723VoiceEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG723VoiceEnable_Type.__name__=_D
_DefaultCodecG723VoiceEnable_Object=MibScalar
defaultCodecG723VoiceEnable=_DefaultCodecG723VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,100),_DefaultCodecG723VoiceEnable_Type())
defaultCodecG723VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG723VoiceEnable.setStatus(_A)
class _DefaultCodecG723VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG723VoicePriority_Type.__name__=_C
_DefaultCodecG723VoicePriority_Object=MibScalar
defaultCodecG723VoicePriority=_DefaultCodecG723VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,200),_DefaultCodecG723VoicePriority_Type())
defaultCodecG723VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG723VoicePriority.setStatus(_A)
class _DefaultCodecG723Bitrate_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_Q,100),(_R,200)))
_DefaultCodecG723Bitrate_Type.__name__=_F
_DefaultCodecG723Bitrate_Object=MibScalar
defaultCodecG723Bitrate=_DefaultCodecG723Bitrate_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,300),_DefaultCodecG723Bitrate_Type())
defaultCodecG723Bitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG723Bitrate.setStatus(_A)
class _DefaultCodecG723MinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60))
_DefaultCodecG723MinPTime_Type.__name__=_C
_DefaultCodecG723MinPTime_Object=MibScalar
defaultCodecG723MinPTime=_DefaultCodecG723MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,400),_DefaultCodecG723MinPTime_Type())
defaultCodecG723MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG723MinPTime.setStatus(_A)
class _DefaultCodecG723MaxPTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60))
_DefaultCodecG723MaxPTime_Type.__name__=_C
_DefaultCodecG723MaxPTime_Object=MibScalar
defaultCodecG723MaxPTime=_DefaultCodecG723MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,500),_DefaultCodecG723MaxPTime_Type())
defaultCodecG723MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG723MaxPTime.setStatus(_A)
_EpSpecificCodecG723Table_Object=MibTable
epSpecificCodecG723Table=_EpSpecificCodecG723Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700))
if mibBuilder.loadTexts:epSpecificCodecG723Table.setStatus(_A)
_EpSpecificCodecG723Entry_Object=MibTableRow
epSpecificCodecG723Entry=_EpSpecificCodecG723Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1))
epSpecificCodecG723Entry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:epSpecificCodecG723Entry.setStatus(_A)
_EpSpecificCodecG723EpId_Type=OctetString
_EpSpecificCodecG723EpId_Object=MibTableColumn
epSpecificCodecG723EpId=_EpSpecificCodecG723EpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,100),_EpSpecificCodecG723EpId_Type())
epSpecificCodecG723EpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG723EpId.setStatus(_A)
class _EpSpecificCodecG723EnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG723EnableConfig_Type.__name__=_D
_EpSpecificCodecG723EnableConfig_Object=MibTableColumn
epSpecificCodecG723EnableConfig=_EpSpecificCodecG723EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,200),_EpSpecificCodecG723EnableConfig_Type())
epSpecificCodecG723EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723EnableConfig.setStatus(_A)
class _EpSpecificCodecG723VoiceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG723VoiceEnable_Type.__name__=_D
_EpSpecificCodecG723VoiceEnable_Object=MibTableColumn
epSpecificCodecG723VoiceEnable=_EpSpecificCodecG723VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,300),_EpSpecificCodecG723VoiceEnable_Type())
epSpecificCodecG723VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723VoiceEnable.setStatus(_A)
class _EpSpecificCodecG723VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG723VoicePriority_Type.__name__=_C
_EpSpecificCodecG723VoicePriority_Object=MibTableColumn
epSpecificCodecG723VoicePriority=_EpSpecificCodecG723VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,400),_EpSpecificCodecG723VoicePriority_Type())
epSpecificCodecG723VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723VoicePriority.setStatus(_A)
class _EpSpecificCodecG723Bitrate_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_Q,100),(_R,200)))
_EpSpecificCodecG723Bitrate_Type.__name__=_F
_EpSpecificCodecG723Bitrate_Object=MibTableColumn
epSpecificCodecG723Bitrate=_EpSpecificCodecG723Bitrate_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,500),_EpSpecificCodecG723Bitrate_Type())
epSpecificCodecG723Bitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723Bitrate.setStatus(_A)
class _EpSpecificCodecG723MinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60))
_EpSpecificCodecG723MinPTime_Type.__name__=_C
_EpSpecificCodecG723MinPTime_Object=MibTableColumn
epSpecificCodecG723MinPTime=_EpSpecificCodecG723MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,600),_EpSpecificCodecG723MinPTime_Type())
epSpecificCodecG723MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723MinPTime.setStatus(_A)
class _EpSpecificCodecG723MaxPTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,30),ValueRangeConstraint(60,60))
_EpSpecificCodecG723MaxPTime_Type.__name__=_C
_EpSpecificCodecG723MaxPTime_Object=MibTableColumn
epSpecificCodecG723MaxPTime=_EpSpecificCodecG723MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,400,700,1,700),_EpSpecificCodecG723MaxPTime_Type())
epSpecificCodecG723MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG723MaxPTime.setStatus(_A)
_CodecG726Group_ObjectIdentity=ObjectIdentity
codecG726Group=_CodecG726Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500))
_CodecG726r16kbpsGroup_ObjectIdentity=ObjectIdentity
codecG726r16kbpsGroup=_CodecG726r16kbpsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100))
class _DefaultCodecG726r16kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r16kbpsVoiceEnable_Type.__name__=_D
_DefaultCodecG726r16kbpsVoiceEnable_Object=MibScalar
defaultCodecG726r16kbpsVoiceEnable=_DefaultCodecG726r16kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,100),_DefaultCodecG726r16kbpsVoiceEnable_Type())
defaultCodecG726r16kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r16kbpsVoiceEnable.setStatus(_A)
class _DefaultCodecG726r16kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r16kbpsVoicePriority_Type.__name__=_C
_DefaultCodecG726r16kbpsVoicePriority_Object=MibScalar
defaultCodecG726r16kbpsVoicePriority=_DefaultCodecG726r16kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,200),_DefaultCodecG726r16kbpsVoicePriority_Type())
defaultCodecG726r16kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r16kbpsVoicePriority.setStatus(_A)
class _DefaultCodecG726r16kbpsPayloadType_Type(Unsigned32):defaultValue=97;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecG726r16kbpsPayloadType_Type.__name__=_C
_DefaultCodecG726r16kbpsPayloadType_Object=MibScalar
defaultCodecG726r16kbpsPayloadType=_DefaultCodecG726r16kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,300),_DefaultCodecG726r16kbpsPayloadType_Type())
defaultCodecG726r16kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r16kbpsPayloadType.setStatus(_A)
class _DefaultCodecG726r16kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r16kbpsMinPTime_Type.__name__=_C
_DefaultCodecG726r16kbpsMinPTime_Object=MibScalar
defaultCodecG726r16kbpsMinPTime=_DefaultCodecG726r16kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,400),_DefaultCodecG726r16kbpsMinPTime_Type())
defaultCodecG726r16kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r16kbpsMinPTime.setStatus(_A)
class _DefaultCodecG726r16kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r16kbpsMaxPTime_Type.__name__=_C
_DefaultCodecG726r16kbpsMaxPTime_Object=MibScalar
defaultCodecG726r16kbpsMaxPTime=_DefaultCodecG726r16kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,500),_DefaultCodecG726r16kbpsMaxPTime_Type())
defaultCodecG726r16kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r16kbpsMaxPTime.setStatus(_A)
_EpSpecificCodecG726r16kbpsTable_Object=MibTable
epSpecificCodecG726r16kbpsTable=_EpSpecificCodecG726r16kbpsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600))
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsTable.setStatus(_A)
_EpSpecificCodecG726r16kbpsEntry_Object=MibTableRow
epSpecificCodecG726r16kbpsEntry=_EpSpecificCodecG726r16kbpsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1))
epSpecificCodecG726r16kbpsEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsEntry.setStatus(_A)
_EpSpecificCodecG726r16kbpsEpId_Type=OctetString
_EpSpecificCodecG726r16kbpsEpId_Object=MibTableColumn
epSpecificCodecG726r16kbpsEpId=_EpSpecificCodecG726r16kbpsEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,100),_EpSpecificCodecG726r16kbpsEpId_Type())
epSpecificCodecG726r16kbpsEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsEpId.setStatus(_A)
class _EpSpecificCodecG726r16kbpsEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r16kbpsEnableConfig_Type.__name__=_D
_EpSpecificCodecG726r16kbpsEnableConfig_Object=MibTableColumn
epSpecificCodecG726r16kbpsEnableConfig=_EpSpecificCodecG726r16kbpsEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,200),_EpSpecificCodecG726r16kbpsEnableConfig_Type())
epSpecificCodecG726r16kbpsEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsEnableConfig.setStatus(_A)
class _EpSpecificCodecG726r16kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r16kbpsVoiceEnable_Type.__name__=_D
_EpSpecificCodecG726r16kbpsVoiceEnable_Object=MibTableColumn
epSpecificCodecG726r16kbpsVoiceEnable=_EpSpecificCodecG726r16kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,300),_EpSpecificCodecG726r16kbpsVoiceEnable_Type())
epSpecificCodecG726r16kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsVoiceEnable.setStatus(_A)
class _EpSpecificCodecG726r16kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r16kbpsVoicePriority_Type.__name__=_C
_EpSpecificCodecG726r16kbpsVoicePriority_Object=MibTableColumn
epSpecificCodecG726r16kbpsVoicePriority=_EpSpecificCodecG726r16kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,400),_EpSpecificCodecG726r16kbpsVoicePriority_Type())
epSpecificCodecG726r16kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsVoicePriority.setStatus(_A)
class _EpSpecificCodecG726r16kbpsPayloadType_Type(Unsigned32):defaultValue=97;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecG726r16kbpsPayloadType_Type.__name__=_C
_EpSpecificCodecG726r16kbpsPayloadType_Object=MibTableColumn
epSpecificCodecG726r16kbpsPayloadType=_EpSpecificCodecG726r16kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,500),_EpSpecificCodecG726r16kbpsPayloadType_Type())
epSpecificCodecG726r16kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsPayloadType.setStatus(_A)
class _EpSpecificCodecG726r16kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r16kbpsMinPTime_Type.__name__=_C
_EpSpecificCodecG726r16kbpsMinPTime_Object=MibTableColumn
epSpecificCodecG726r16kbpsMinPTime=_EpSpecificCodecG726r16kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,600),_EpSpecificCodecG726r16kbpsMinPTime_Type())
epSpecificCodecG726r16kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsMinPTime.setStatus(_A)
class _EpSpecificCodecG726r16kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r16kbpsMaxPTime_Type.__name__=_C
_EpSpecificCodecG726r16kbpsMaxPTime_Object=MibTableColumn
epSpecificCodecG726r16kbpsMaxPTime=_EpSpecificCodecG726r16kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,100,600,1,700),_EpSpecificCodecG726r16kbpsMaxPTime_Type())
epSpecificCodecG726r16kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r16kbpsMaxPTime.setStatus(_A)
_CodecG726r24kbpsGroup_ObjectIdentity=ObjectIdentity
codecG726r24kbpsGroup=_CodecG726r24kbpsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200))
class _DefaultCodecG726r24kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r24kbpsVoiceEnable_Type.__name__=_D
_DefaultCodecG726r24kbpsVoiceEnable_Object=MibScalar
defaultCodecG726r24kbpsVoiceEnable=_DefaultCodecG726r24kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,100),_DefaultCodecG726r24kbpsVoiceEnable_Type())
defaultCodecG726r24kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r24kbpsVoiceEnable.setStatus(_A)
class _DefaultCodecG726r24kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r24kbpsVoicePriority_Type.__name__=_C
_DefaultCodecG726r24kbpsVoicePriority_Object=MibScalar
defaultCodecG726r24kbpsVoicePriority=_DefaultCodecG726r24kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,200),_DefaultCodecG726r24kbpsVoicePriority_Type())
defaultCodecG726r24kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r24kbpsVoicePriority.setStatus(_A)
class _DefaultCodecG726r24kbpsPayloadType_Type(Unsigned32):defaultValue=98;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecG726r24kbpsPayloadType_Type.__name__=_C
_DefaultCodecG726r24kbpsPayloadType_Object=MibScalar
defaultCodecG726r24kbpsPayloadType=_DefaultCodecG726r24kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,300),_DefaultCodecG726r24kbpsPayloadType_Type())
defaultCodecG726r24kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r24kbpsPayloadType.setStatus(_A)
class _DefaultCodecG726r24kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r24kbpsMinPTime_Type.__name__=_C
_DefaultCodecG726r24kbpsMinPTime_Object=MibScalar
defaultCodecG726r24kbpsMinPTime=_DefaultCodecG726r24kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,400),_DefaultCodecG726r24kbpsMinPTime_Type())
defaultCodecG726r24kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r24kbpsMinPTime.setStatus(_A)
class _DefaultCodecG726r24kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r24kbpsMaxPTime_Type.__name__=_C
_DefaultCodecG726r24kbpsMaxPTime_Object=MibScalar
defaultCodecG726r24kbpsMaxPTime=_DefaultCodecG726r24kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,500),_DefaultCodecG726r24kbpsMaxPTime_Type())
defaultCodecG726r24kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r24kbpsMaxPTime.setStatus(_A)
_EpSpecificCodecG726r24kbpsTable_Object=MibTable
epSpecificCodecG726r24kbpsTable=_EpSpecificCodecG726r24kbpsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600))
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsTable.setStatus(_A)
_EpSpecificCodecG726r24kbpsEntry_Object=MibTableRow
epSpecificCodecG726r24kbpsEntry=_EpSpecificCodecG726r24kbpsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1))
epSpecificCodecG726r24kbpsEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsEntry.setStatus(_A)
_EpSpecificCodecG726r24kbpsEpId_Type=OctetString
_EpSpecificCodecG726r24kbpsEpId_Object=MibTableColumn
epSpecificCodecG726r24kbpsEpId=_EpSpecificCodecG726r24kbpsEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,100),_EpSpecificCodecG726r24kbpsEpId_Type())
epSpecificCodecG726r24kbpsEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsEpId.setStatus(_A)
class _EpSpecificCodecG726r24kbpsEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r24kbpsEnableConfig_Type.__name__=_D
_EpSpecificCodecG726r24kbpsEnableConfig_Object=MibTableColumn
epSpecificCodecG726r24kbpsEnableConfig=_EpSpecificCodecG726r24kbpsEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,200),_EpSpecificCodecG726r24kbpsEnableConfig_Type())
epSpecificCodecG726r24kbpsEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsEnableConfig.setStatus(_A)
class _EpSpecificCodecG726r24kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r24kbpsVoiceEnable_Type.__name__=_D
_EpSpecificCodecG726r24kbpsVoiceEnable_Object=MibTableColumn
epSpecificCodecG726r24kbpsVoiceEnable=_EpSpecificCodecG726r24kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,300),_EpSpecificCodecG726r24kbpsVoiceEnable_Type())
epSpecificCodecG726r24kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsVoiceEnable.setStatus(_A)
class _EpSpecificCodecG726r24kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r24kbpsVoicePriority_Type.__name__=_C
_EpSpecificCodecG726r24kbpsVoicePriority_Object=MibTableColumn
epSpecificCodecG726r24kbpsVoicePriority=_EpSpecificCodecG726r24kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,400),_EpSpecificCodecG726r24kbpsVoicePriority_Type())
epSpecificCodecG726r24kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsVoicePriority.setStatus(_A)
class _EpSpecificCodecG726r24kbpsPayloadType_Type(Unsigned32):defaultValue=98;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecG726r24kbpsPayloadType_Type.__name__=_C
_EpSpecificCodecG726r24kbpsPayloadType_Object=MibTableColumn
epSpecificCodecG726r24kbpsPayloadType=_EpSpecificCodecG726r24kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,500),_EpSpecificCodecG726r24kbpsPayloadType_Type())
epSpecificCodecG726r24kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsPayloadType.setStatus(_A)
class _EpSpecificCodecG726r24kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r24kbpsMinPTime_Type.__name__=_C
_EpSpecificCodecG726r24kbpsMinPTime_Object=MibTableColumn
epSpecificCodecG726r24kbpsMinPTime=_EpSpecificCodecG726r24kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,600),_EpSpecificCodecG726r24kbpsMinPTime_Type())
epSpecificCodecG726r24kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsMinPTime.setStatus(_A)
class _EpSpecificCodecG726r24kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r24kbpsMaxPTime_Type.__name__=_C
_EpSpecificCodecG726r24kbpsMaxPTime_Object=MibTableColumn
epSpecificCodecG726r24kbpsMaxPTime=_EpSpecificCodecG726r24kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,200,600,1,700),_EpSpecificCodecG726r24kbpsMaxPTime_Type())
epSpecificCodecG726r24kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r24kbpsMaxPTime.setStatus(_A)
_CodecG726r32kbpsGroup_ObjectIdentity=ObjectIdentity
codecG726r32kbpsGroup=_CodecG726r32kbpsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300))
class _DefaultCodecG726r32kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r32kbpsVoiceEnable_Type.__name__=_D
_DefaultCodecG726r32kbpsVoiceEnable_Object=MibScalar
defaultCodecG726r32kbpsVoiceEnable=_DefaultCodecG726r32kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,100),_DefaultCodecG726r32kbpsVoiceEnable_Type())
defaultCodecG726r32kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsVoiceEnable.setStatus(_A)
class _DefaultCodecG726r32kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r32kbpsVoicePriority_Type.__name__=_C
_DefaultCodecG726r32kbpsVoicePriority_Object=MibScalar
defaultCodecG726r32kbpsVoicePriority=_DefaultCodecG726r32kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,200),_DefaultCodecG726r32kbpsVoicePriority_Type())
defaultCodecG726r32kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsVoicePriority.setStatus(_A)
class _DefaultCodecG726r32kbpsDataEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r32kbpsDataEnable_Type.__name__=_D
_DefaultCodecG726r32kbpsDataEnable_Object=MibScalar
defaultCodecG726r32kbpsDataEnable=_DefaultCodecG726r32kbpsDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,300),_DefaultCodecG726r32kbpsDataEnable_Type())
defaultCodecG726r32kbpsDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsDataEnable.setStatus(_A)
class _DefaultCodecG726r32kbpsDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r32kbpsDataPriority_Type.__name__=_C
_DefaultCodecG726r32kbpsDataPriority_Object=MibScalar
defaultCodecG726r32kbpsDataPriority=_DefaultCodecG726r32kbpsDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,400),_DefaultCodecG726r32kbpsDataPriority_Type())
defaultCodecG726r32kbpsDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsDataPriority.setStatus(_A)
class _DefaultCodecG726r32kbpsPayloadType_Type(Unsigned32):defaultValue=99;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecG726r32kbpsPayloadType_Type.__name__=_C
_DefaultCodecG726r32kbpsPayloadType_Object=MibScalar
defaultCodecG726r32kbpsPayloadType=_DefaultCodecG726r32kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,500),_DefaultCodecG726r32kbpsPayloadType_Type())
defaultCodecG726r32kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsPayloadType.setStatus(_A)
class _DefaultCodecG726r32kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r32kbpsMinPTime_Type.__name__=_C
_DefaultCodecG726r32kbpsMinPTime_Object=MibScalar
defaultCodecG726r32kbpsMinPTime=_DefaultCodecG726r32kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,600),_DefaultCodecG726r32kbpsMinPTime_Type())
defaultCodecG726r32kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsMinPTime.setStatus(_A)
class _DefaultCodecG726r32kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r32kbpsMaxPTime_Type.__name__=_C
_DefaultCodecG726r32kbpsMaxPTime_Object=MibScalar
defaultCodecG726r32kbpsMaxPTime=_DefaultCodecG726r32kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,700),_DefaultCodecG726r32kbpsMaxPTime_Type())
defaultCodecG726r32kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r32kbpsMaxPTime.setStatus(_A)
_EpSpecificCodecG726r32kbpsTable_Object=MibTable
epSpecificCodecG726r32kbpsTable=_EpSpecificCodecG726r32kbpsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800))
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsTable.setStatus(_A)
_EpSpecificCodecG726r32kbpsEntry_Object=MibTableRow
epSpecificCodecG726r32kbpsEntry=_EpSpecificCodecG726r32kbpsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1))
epSpecificCodecG726r32kbpsEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsEntry.setStatus(_A)
_EpSpecificCodecG726r32kbpsEpId_Type=OctetString
_EpSpecificCodecG726r32kbpsEpId_Object=MibTableColumn
epSpecificCodecG726r32kbpsEpId=_EpSpecificCodecG726r32kbpsEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,100),_EpSpecificCodecG726r32kbpsEpId_Type())
epSpecificCodecG726r32kbpsEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsEpId.setStatus(_A)
class _EpSpecificCodecG726r32kbpsEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r32kbpsEnableConfig_Type.__name__=_D
_EpSpecificCodecG726r32kbpsEnableConfig_Object=MibTableColumn
epSpecificCodecG726r32kbpsEnableConfig=_EpSpecificCodecG726r32kbpsEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,200),_EpSpecificCodecG726r32kbpsEnableConfig_Type())
epSpecificCodecG726r32kbpsEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsEnableConfig.setStatus(_A)
class _EpSpecificCodecG726r32kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r32kbpsVoiceEnable_Type.__name__=_D
_EpSpecificCodecG726r32kbpsVoiceEnable_Object=MibTableColumn
epSpecificCodecG726r32kbpsVoiceEnable=_EpSpecificCodecG726r32kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,300),_EpSpecificCodecG726r32kbpsVoiceEnable_Type())
epSpecificCodecG726r32kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsVoiceEnable.setStatus(_A)
class _EpSpecificCodecG726r32kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r32kbpsVoicePriority_Type.__name__=_C
_EpSpecificCodecG726r32kbpsVoicePriority_Object=MibTableColumn
epSpecificCodecG726r32kbpsVoicePriority=_EpSpecificCodecG726r32kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,400),_EpSpecificCodecG726r32kbpsVoicePriority_Type())
epSpecificCodecG726r32kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsVoicePriority.setStatus(_A)
class _EpSpecificCodecG726r32kbpsDataEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r32kbpsDataEnable_Type.__name__=_D
_EpSpecificCodecG726r32kbpsDataEnable_Object=MibTableColumn
epSpecificCodecG726r32kbpsDataEnable=_EpSpecificCodecG726r32kbpsDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,500),_EpSpecificCodecG726r32kbpsDataEnable_Type())
epSpecificCodecG726r32kbpsDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsDataEnable.setStatus(_A)
class _EpSpecificCodecG726r32kbpsDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r32kbpsDataPriority_Type.__name__=_C
_EpSpecificCodecG726r32kbpsDataPriority_Object=MibTableColumn
epSpecificCodecG726r32kbpsDataPriority=_EpSpecificCodecG726r32kbpsDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,600),_EpSpecificCodecG726r32kbpsDataPriority_Type())
epSpecificCodecG726r32kbpsDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsDataPriority.setStatus(_A)
class _EpSpecificCodecG726r32kbpsPayloadType_Type(Unsigned32):defaultValue=99;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecG726r32kbpsPayloadType_Type.__name__=_C
_EpSpecificCodecG726r32kbpsPayloadType_Object=MibTableColumn
epSpecificCodecG726r32kbpsPayloadType=_EpSpecificCodecG726r32kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,700),_EpSpecificCodecG726r32kbpsPayloadType_Type())
epSpecificCodecG726r32kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsPayloadType.setStatus(_A)
class _EpSpecificCodecG726r32kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r32kbpsMinPTime_Type.__name__=_C
_EpSpecificCodecG726r32kbpsMinPTime_Object=MibTableColumn
epSpecificCodecG726r32kbpsMinPTime=_EpSpecificCodecG726r32kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,800),_EpSpecificCodecG726r32kbpsMinPTime_Type())
epSpecificCodecG726r32kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsMinPTime.setStatus(_A)
class _EpSpecificCodecG726r32kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r32kbpsMaxPTime_Type.__name__=_C
_EpSpecificCodecG726r32kbpsMaxPTime_Object=MibTableColumn
epSpecificCodecG726r32kbpsMaxPTime=_EpSpecificCodecG726r32kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,300,800,1,900),_EpSpecificCodecG726r32kbpsMaxPTime_Type())
epSpecificCodecG726r32kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r32kbpsMaxPTime.setStatus(_A)
_CodecG726r40kbpsGroup_ObjectIdentity=ObjectIdentity
codecG726r40kbpsGroup=_CodecG726r40kbpsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400))
class _DefaultCodecG726r40kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r40kbpsVoiceEnable_Type.__name__=_D
_DefaultCodecG726r40kbpsVoiceEnable_Object=MibScalar
defaultCodecG726r40kbpsVoiceEnable=_DefaultCodecG726r40kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,100),_DefaultCodecG726r40kbpsVoiceEnable_Type())
defaultCodecG726r40kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsVoiceEnable.setStatus(_A)
class _DefaultCodecG726r40kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r40kbpsVoicePriority_Type.__name__=_C
_DefaultCodecG726r40kbpsVoicePriority_Object=MibScalar
defaultCodecG726r40kbpsVoicePriority=_DefaultCodecG726r40kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,200),_DefaultCodecG726r40kbpsVoicePriority_Type())
defaultCodecG726r40kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsVoicePriority.setStatus(_A)
class _DefaultCodecG726r40kbpsDataEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecG726r40kbpsDataEnable_Type.__name__=_D
_DefaultCodecG726r40kbpsDataEnable_Object=MibScalar
defaultCodecG726r40kbpsDataEnable=_DefaultCodecG726r40kbpsDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,300),_DefaultCodecG726r40kbpsDataEnable_Type())
defaultCodecG726r40kbpsDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsDataEnable.setStatus(_A)
class _DefaultCodecG726r40kbpsDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG726r40kbpsDataPriority_Type.__name__=_C
_DefaultCodecG726r40kbpsDataPriority_Object=MibScalar
defaultCodecG726r40kbpsDataPriority=_DefaultCodecG726r40kbpsDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,400),_DefaultCodecG726r40kbpsDataPriority_Type())
defaultCodecG726r40kbpsDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsDataPriority.setStatus(_A)
class _DefaultCodecG726r40kbpsPayloadType_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecG726r40kbpsPayloadType_Type.__name__=_C
_DefaultCodecG726r40kbpsPayloadType_Object=MibScalar
defaultCodecG726r40kbpsPayloadType=_DefaultCodecG726r40kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,500),_DefaultCodecG726r40kbpsPayloadType_Type())
defaultCodecG726r40kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsPayloadType.setStatus(_A)
class _DefaultCodecG726r40kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r40kbpsMinPTime_Type.__name__=_C
_DefaultCodecG726r40kbpsMinPTime_Object=MibScalar
defaultCodecG726r40kbpsMinPTime=_DefaultCodecG726r40kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,600),_DefaultCodecG726r40kbpsMinPTime_Type())
defaultCodecG726r40kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsMinPTime.setStatus(_A)
class _DefaultCodecG726r40kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecG726r40kbpsMaxPTime_Type.__name__=_C
_DefaultCodecG726r40kbpsMaxPTime_Object=MibScalar
defaultCodecG726r40kbpsMaxPTime=_DefaultCodecG726r40kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,700),_DefaultCodecG726r40kbpsMaxPTime_Type())
defaultCodecG726r40kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG726r40kbpsMaxPTime.setStatus(_A)
_EpSpecificCodecG726r40kbpsTable_Object=MibTable
epSpecificCodecG726r40kbpsTable=_EpSpecificCodecG726r40kbpsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800))
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsTable.setStatus(_A)
_EpSpecificCodecG726r40kbpsEntry_Object=MibTableRow
epSpecificCodecG726r40kbpsEntry=_EpSpecificCodecG726r40kbpsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1))
epSpecificCodecG726r40kbpsEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsEntry.setStatus(_A)
_EpSpecificCodecG726r40kbpsEpId_Type=OctetString
_EpSpecificCodecG726r40kbpsEpId_Object=MibTableColumn
epSpecificCodecG726r40kbpsEpId=_EpSpecificCodecG726r40kbpsEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,100),_EpSpecificCodecG726r40kbpsEpId_Type())
epSpecificCodecG726r40kbpsEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsEpId.setStatus(_A)
class _EpSpecificCodecG726r40kbpsEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r40kbpsEnableConfig_Type.__name__=_D
_EpSpecificCodecG726r40kbpsEnableConfig_Object=MibTableColumn
epSpecificCodecG726r40kbpsEnableConfig=_EpSpecificCodecG726r40kbpsEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,200),_EpSpecificCodecG726r40kbpsEnableConfig_Type())
epSpecificCodecG726r40kbpsEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsEnableConfig.setStatus(_A)
class _EpSpecificCodecG726r40kbpsVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r40kbpsVoiceEnable_Type.__name__=_D
_EpSpecificCodecG726r40kbpsVoiceEnable_Object=MibTableColumn
epSpecificCodecG726r40kbpsVoiceEnable=_EpSpecificCodecG726r40kbpsVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,300),_EpSpecificCodecG726r40kbpsVoiceEnable_Type())
epSpecificCodecG726r40kbpsVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsVoiceEnable.setStatus(_A)
class _EpSpecificCodecG726r40kbpsVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r40kbpsVoicePriority_Type.__name__=_C
_EpSpecificCodecG726r40kbpsVoicePriority_Object=MibTableColumn
epSpecificCodecG726r40kbpsVoicePriority=_EpSpecificCodecG726r40kbpsVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,400),_EpSpecificCodecG726r40kbpsVoicePriority_Type())
epSpecificCodecG726r40kbpsVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsVoicePriority.setStatus(_A)
class _EpSpecificCodecG726r40kbpsDataEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG726r40kbpsDataEnable_Type.__name__=_D
_EpSpecificCodecG726r40kbpsDataEnable_Object=MibTableColumn
epSpecificCodecG726r40kbpsDataEnable=_EpSpecificCodecG726r40kbpsDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,500),_EpSpecificCodecG726r40kbpsDataEnable_Type())
epSpecificCodecG726r40kbpsDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsDataEnable.setStatus(_A)
class _EpSpecificCodecG726r40kbpsDataPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG726r40kbpsDataPriority_Type.__name__=_C
_EpSpecificCodecG726r40kbpsDataPriority_Object=MibTableColumn
epSpecificCodecG726r40kbpsDataPriority=_EpSpecificCodecG726r40kbpsDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,600),_EpSpecificCodecG726r40kbpsDataPriority_Type())
epSpecificCodecG726r40kbpsDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsDataPriority.setStatus(_A)
class _EpSpecificCodecG726r40kbpsPayloadType_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecG726r40kbpsPayloadType_Type.__name__=_C
_EpSpecificCodecG726r40kbpsPayloadType_Object=MibTableColumn
epSpecificCodecG726r40kbpsPayloadType=_EpSpecificCodecG726r40kbpsPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,700),_EpSpecificCodecG726r40kbpsPayloadType_Type())
epSpecificCodecG726r40kbpsPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsPayloadType.setStatus(_A)
class _EpSpecificCodecG726r40kbpsMinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r40kbpsMinPTime_Type.__name__=_C
_EpSpecificCodecG726r40kbpsMinPTime_Object=MibTableColumn
epSpecificCodecG726r40kbpsMinPTime=_EpSpecificCodecG726r40kbpsMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,800),_EpSpecificCodecG726r40kbpsMinPTime_Type())
epSpecificCodecG726r40kbpsMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsMinPTime.setStatus(_A)
class _EpSpecificCodecG726r40kbpsMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecG726r40kbpsMaxPTime_Type.__name__=_C
_EpSpecificCodecG726r40kbpsMaxPTime_Object=MibTableColumn
epSpecificCodecG726r40kbpsMaxPTime=_EpSpecificCodecG726r40kbpsMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,500,400,800,1,900),_EpSpecificCodecG726r40kbpsMaxPTime_Type())
epSpecificCodecG726r40kbpsMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG726r40kbpsMaxPTime.setStatus(_A)
_CodecG729Group_ObjectIdentity=ObjectIdentity
codecG729Group=_CodecG729Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600))
class _DefaultCodecG729VoiceEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecG729VoiceEnable_Type.__name__=_D
_DefaultCodecG729VoiceEnable_Object=MibScalar
defaultCodecG729VoiceEnable=_DefaultCodecG729VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,100),_DefaultCodecG729VoiceEnable_Type())
defaultCodecG729VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG729VoiceEnable.setStatus(_A)
class _DefaultCodecG729VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecG729VoicePriority_Type.__name__=_C
_DefaultCodecG729VoicePriority_Object=MibScalar
defaultCodecG729VoicePriority=_DefaultCodecG729VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,200),_DefaultCodecG729VoicePriority_Type())
defaultCodecG729VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG729VoicePriority.setStatus(_A)
class _DefaultCodecG729MinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80))
_DefaultCodecG729MinPTime_Type.__name__=_C
_DefaultCodecG729MinPTime_Object=MibScalar
defaultCodecG729MinPTime=_DefaultCodecG729MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,300),_DefaultCodecG729MinPTime_Type())
defaultCodecG729MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG729MinPTime.setStatus(_A)
class _DefaultCodecG729MaxPTime_Type(Unsigned32):defaultValue=80;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80))
_DefaultCodecG729MaxPTime_Type.__name__=_C
_DefaultCodecG729MaxPTime_Object=MibScalar
defaultCodecG729MaxPTime=_DefaultCodecG729MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,400),_DefaultCodecG729MaxPTime_Type())
defaultCodecG729MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG729MaxPTime.setStatus(_A)
class _DefaultCodecG729VoiceActivityDetection_Type(MxEnableState):defaultValue=1
_DefaultCodecG729VoiceActivityDetection_Type.__name__=_D
_DefaultCodecG729VoiceActivityDetection_Object=MibScalar
defaultCodecG729VoiceActivityDetection=_DefaultCodecG729VoiceActivityDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,500),_DefaultCodecG729VoiceActivityDetection_Type())
defaultCodecG729VoiceActivityDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecG729VoiceActivityDetection.setStatus(_A)
_EpSpecificCodecG729Table_Object=MibTable
epSpecificCodecG729Table=_EpSpecificCodecG729Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600))
if mibBuilder.loadTexts:epSpecificCodecG729Table.setStatus(_A)
_EpSpecificCodecG729Entry_Object=MibTableRow
epSpecificCodecG729Entry=_EpSpecificCodecG729Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1))
epSpecificCodecG729Entry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:epSpecificCodecG729Entry.setStatus(_A)
_EpSpecificCodecG729EpId_Type=OctetString
_EpSpecificCodecG729EpId_Object=MibTableColumn
epSpecificCodecG729EpId=_EpSpecificCodecG729EpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,100),_EpSpecificCodecG729EpId_Type())
epSpecificCodecG729EpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecG729EpId.setStatus(_A)
class _EpSpecificCodecG729EnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecG729EnableConfig_Type.__name__=_D
_EpSpecificCodecG729EnableConfig_Object=MibTableColumn
epSpecificCodecG729EnableConfig=_EpSpecificCodecG729EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,200),_EpSpecificCodecG729EnableConfig_Type())
epSpecificCodecG729EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729EnableConfig.setStatus(_A)
class _EpSpecificCodecG729VoiceEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG729VoiceEnable_Type.__name__=_D
_EpSpecificCodecG729VoiceEnable_Object=MibTableColumn
epSpecificCodecG729VoiceEnable=_EpSpecificCodecG729VoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,300),_EpSpecificCodecG729VoiceEnable_Type())
epSpecificCodecG729VoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729VoiceEnable.setStatus(_A)
class _EpSpecificCodecG729VoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecG729VoicePriority_Type.__name__=_C
_EpSpecificCodecG729VoicePriority_Object=MibTableColumn
epSpecificCodecG729VoicePriority=_EpSpecificCodecG729VoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,400),_EpSpecificCodecG729VoicePriority_Type())
epSpecificCodecG729VoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729VoicePriority.setStatus(_A)
class _EpSpecificCodecG729MinPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80))
_EpSpecificCodecG729MinPTime_Type.__name__=_C
_EpSpecificCodecG729MinPTime_Object=MibTableColumn
epSpecificCodecG729MinPTime=_EpSpecificCodecG729MinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,500),_EpSpecificCodecG729MinPTime_Type())
epSpecificCodecG729MinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729MinPTime.setStatus(_A)
class _EpSpecificCodecG729MaxPTime_Type(Unsigned32):defaultValue=80;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,20),ValueRangeConstraint(30,30),ValueRangeConstraint(40,40),ValueRangeConstraint(50,50),ValueRangeConstraint(60,60),ValueRangeConstraint(70,70),ValueRangeConstraint(80,80))
_EpSpecificCodecG729MaxPTime_Type.__name__=_C
_EpSpecificCodecG729MaxPTime_Object=MibTableColumn
epSpecificCodecG729MaxPTime=_EpSpecificCodecG729MaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,600),_EpSpecificCodecG729MaxPTime_Type())
epSpecificCodecG729MaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729MaxPTime.setStatus(_A)
class _EpSpecificCodecG729VoiceActivityDetection_Type(MxEnableState):defaultValue=1
_EpSpecificCodecG729VoiceActivityDetection_Type.__name__=_D
_EpSpecificCodecG729VoiceActivityDetection_Object=MibTableColumn
epSpecificCodecG729VoiceActivityDetection=_EpSpecificCodecG729VoiceActivityDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,600,600,1,700),_EpSpecificCodecG729VoiceActivityDetection_Type())
epSpecificCodecG729VoiceActivityDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecG729VoiceActivityDetection.setStatus(_A)
_CodecT38Group_ObjectIdentity=ObjectIdentity
codecT38Group=_CodecT38Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700))
class _DefaultCodecT38DataEnable_Type(MxEnableState):defaultValue=1
_DefaultCodecT38DataEnable_Type.__name__=_D
_DefaultCodecT38DataEnable_Object=MibScalar
defaultCodecT38DataEnable=_DefaultCodecT38DataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,100),_DefaultCodecT38DataEnable_Type())
defaultCodecT38DataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38DataEnable.setStatus(_A)
class _DefaultCodecT38DataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10))
_DefaultCodecT38DataPriority_Type.__name__=_C
_DefaultCodecT38DataPriority_Object=MibScalar
defaultCodecT38DataPriority=_DefaultCodecT38DataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,200),_DefaultCodecT38DataPriority_Type())
defaultCodecT38DataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38DataPriority.setStatus(_A)
class _DefaultCodecT38RedundancyLevel_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_DefaultCodecT38RedundancyLevel_Type.__name__=_C
_DefaultCodecT38RedundancyLevel_Object=MibScalar
defaultCodecT38RedundancyLevel=_DefaultCodecT38RedundancyLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,400),_DefaultCodecT38RedundancyLevel_Type())
defaultCodecT38RedundancyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38RedundancyLevel.setStatus(_A)
class _DefaultCodecT38FinalFramesRedundancy_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_DefaultCodecT38FinalFramesRedundancy_Type.__name__=_C
_DefaultCodecT38FinalFramesRedundancy_Object=MibScalar
defaultCodecT38FinalFramesRedundancy=_DefaultCodecT38FinalFramesRedundancy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,500),_DefaultCodecT38FinalFramesRedundancy_Type())
defaultCodecT38FinalFramesRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38FinalFramesRedundancy.setStatus(_A)
class _DefaultCodecT38NoSignalEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecT38NoSignalEnable_Type.__name__=_D
_DefaultCodecT38NoSignalEnable_Object=MibScalar
defaultCodecT38NoSignalEnable=_DefaultCodecT38NoSignalEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,600),_DefaultCodecT38NoSignalEnable_Type())
defaultCodecT38NoSignalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38NoSignalEnable.setStatus(_A)
class _DefaultCodecT38NoSignalTimeout_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DefaultCodecT38NoSignalTimeout_Type.__name__=_C
_DefaultCodecT38NoSignalTimeout_Object=MibScalar
defaultCodecT38NoSignalTimeout=_DefaultCodecT38NoSignalTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,700),_DefaultCodecT38NoSignalTimeout_Type())
defaultCodecT38NoSignalTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38NoSignalTimeout.setStatus(_A)
class _DefaultCodecT38DetectionThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_Y,100),('low',200),(_Z,300)))
_DefaultCodecT38DetectionThreshold_Type.__name__=_F
_DefaultCodecT38DetectionThreshold_Object=MibScalar
defaultCodecT38DetectionThreshold=_DefaultCodecT38DetectionThreshold_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,750),_DefaultCodecT38DetectionThreshold_Type())
defaultCodecT38DetectionThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecT38DetectionThreshold.setStatus(_A)
_EpSpecificCodecT38Table_Object=MibTable
epSpecificCodecT38Table=_EpSpecificCodecT38Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800))
if mibBuilder.loadTexts:epSpecificCodecT38Table.setStatus(_A)
_EpSpecificCodecT38Entry_Object=MibTableRow
epSpecificCodecT38Entry=_EpSpecificCodecT38Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1))
epSpecificCodecT38Entry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:epSpecificCodecT38Entry.setStatus(_A)
_EpSpecificCodecT38EpId_Type=OctetString
_EpSpecificCodecT38EpId_Object=MibTableColumn
epSpecificCodecT38EpId=_EpSpecificCodecT38EpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,100),_EpSpecificCodecT38EpId_Type())
epSpecificCodecT38EpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecT38EpId.setStatus(_A)
class _EpSpecificCodecT38EnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecT38EnableConfig_Type.__name__=_D
_EpSpecificCodecT38EnableConfig_Object=MibTableColumn
epSpecificCodecT38EnableConfig=_EpSpecificCodecT38EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,200),_EpSpecificCodecT38EnableConfig_Type())
epSpecificCodecT38EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecT38EnableConfig.setStatus(_A)
class _EpSpecificCodecT38DataEnable_Type(MxEnableState):defaultValue=1
_EpSpecificCodecT38DataEnable_Type.__name__=_D
_EpSpecificCodecT38DataEnable_Object=MibTableColumn
epSpecificCodecT38DataEnable=_EpSpecificCodecT38DataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,300),_EpSpecificCodecT38DataEnable_Type())
epSpecificCodecT38DataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecT38DataEnable.setStatus(_A)
class _EpSpecificCodecT38DataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10))
_EpSpecificCodecT38DataPriority_Type.__name__=_C
_EpSpecificCodecT38DataPriority_Object=MibTableColumn
epSpecificCodecT38DataPriority=_EpSpecificCodecT38DataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,400),_EpSpecificCodecT38DataPriority_Type())
epSpecificCodecT38DataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecT38DataPriority.setStatus(_A)
class _EpSpecificCodecT38RedundancyLevel_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_EpSpecificCodecT38RedundancyLevel_Type.__name__=_C
_EpSpecificCodecT38RedundancyLevel_Object=MibTableColumn
epSpecificCodecT38RedundancyLevel=_EpSpecificCodecT38RedundancyLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,600),_EpSpecificCodecT38RedundancyLevel_Type())
epSpecificCodecT38RedundancyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecT38RedundancyLevel.setStatus(_A)
class _EpSpecificCodecT38DetectionThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_Y,100),('low',200),(_Z,300)))
_EpSpecificCodecT38DetectionThreshold_Type.__name__=_F
_EpSpecificCodecT38DetectionThreshold_Object=MibTableColumn
epSpecificCodecT38DetectionThreshold=_EpSpecificCodecT38DetectionThreshold_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,700,800,1,700),_EpSpecificCodecT38DetectionThreshold_Type())
epSpecificCodecT38DetectionThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecT38DetectionThreshold.setStatus(_A)
_CodecClearModeGroup_ObjectIdentity=ObjectIdentity
codecClearModeGroup=_CodecClearModeGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800))
class _DefaultCodecClearModeVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecClearModeVoiceEnable_Type.__name__=_D
_DefaultCodecClearModeVoiceEnable_Object=MibScalar
defaultCodecClearModeVoiceEnable=_DefaultCodecClearModeVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,100),_DefaultCodecClearModeVoiceEnable_Type())
defaultCodecClearModeVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeVoiceEnable.setStatus(_A)
class _DefaultCodecClearModeVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecClearModeVoicePriority_Type.__name__=_C
_DefaultCodecClearModeVoicePriority_Object=MibScalar
defaultCodecClearModeVoicePriority=_DefaultCodecClearModeVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,200),_DefaultCodecClearModeVoicePriority_Type())
defaultCodecClearModeVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeVoicePriority.setStatus(_A)
class _DefaultCodecClearModeDataEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecClearModeDataEnable_Type.__name__=_D
_DefaultCodecClearModeDataEnable_Object=MibScalar
defaultCodecClearModeDataEnable=_DefaultCodecClearModeDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,300),_DefaultCodecClearModeDataEnable_Type())
defaultCodecClearModeDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeDataEnable.setStatus(_A)
class _DefaultCodecClearModeDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecClearModeDataPriority_Type.__name__=_C
_DefaultCodecClearModeDataPriority_Object=MibScalar
defaultCodecClearModeDataPriority=_DefaultCodecClearModeDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,400),_DefaultCodecClearModeDataPriority_Type())
defaultCodecClearModeDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeDataPriority.setStatus(_A)
class _DefaultCodecClearModePayloadType_Type(Unsigned32):defaultValue=124;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecClearModePayloadType_Type.__name__=_C
_DefaultCodecClearModePayloadType_Object=MibScalar
defaultCodecClearModePayloadType=_DefaultCodecClearModePayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,500),_DefaultCodecClearModePayloadType_Type())
defaultCodecClearModePayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModePayloadType.setStatus(_A)
class _DefaultCodecClearModeMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecClearModeMinPTime_Type.__name__=_C
_DefaultCodecClearModeMinPTime_Object=MibScalar
defaultCodecClearModeMinPTime=_DefaultCodecClearModeMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,600),_DefaultCodecClearModeMinPTime_Type())
defaultCodecClearModeMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeMinPTime.setStatus(_A)
class _DefaultCodecClearModeMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecClearModeMaxPTime_Type.__name__=_C
_DefaultCodecClearModeMaxPTime_Object=MibScalar
defaultCodecClearModeMaxPTime=_DefaultCodecClearModeMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,700),_DefaultCodecClearModeMaxPTime_Type())
defaultCodecClearModeMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearModeMaxPTime.setStatus(_A)
_EpSpecificCodecClearModeTable_Object=MibTable
epSpecificCodecClearModeTable=_EpSpecificCodecClearModeTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800))
if mibBuilder.loadTexts:epSpecificCodecClearModeTable.setStatus(_A)
_EpSpecificCodecClearModeEntry_Object=MibTableRow
epSpecificCodecClearModeEntry=_EpSpecificCodecClearModeEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1))
epSpecificCodecClearModeEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:epSpecificCodecClearModeEntry.setStatus(_A)
_EpSpecificCodecClearModeEpId_Type=OctetString
_EpSpecificCodecClearModeEpId_Object=MibTableColumn
epSpecificCodecClearModeEpId=_EpSpecificCodecClearModeEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,100),_EpSpecificCodecClearModeEpId_Type())
epSpecificCodecClearModeEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecClearModeEpId.setStatus(_A)
class _EpSpecificCodecClearModeEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearModeEnableConfig_Type.__name__=_D
_EpSpecificCodecClearModeEnableConfig_Object=MibTableColumn
epSpecificCodecClearModeEnableConfig=_EpSpecificCodecClearModeEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,200),_EpSpecificCodecClearModeEnableConfig_Type())
epSpecificCodecClearModeEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeEnableConfig.setStatus(_A)
class _EpSpecificCodecClearModeVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearModeVoiceEnable_Type.__name__=_D
_EpSpecificCodecClearModeVoiceEnable_Object=MibTableColumn
epSpecificCodecClearModeVoiceEnable=_EpSpecificCodecClearModeVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,300),_EpSpecificCodecClearModeVoiceEnable_Type())
epSpecificCodecClearModeVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeVoiceEnable.setStatus(_A)
class _EpSpecificCodecClearModeVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecClearModeVoicePriority_Type.__name__=_C
_EpSpecificCodecClearModeVoicePriority_Object=MibTableColumn
epSpecificCodecClearModeVoicePriority=_EpSpecificCodecClearModeVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,400),_EpSpecificCodecClearModeVoicePriority_Type())
epSpecificCodecClearModeVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeVoicePriority.setStatus(_A)
class _EpSpecificCodecClearModeDataEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearModeDataEnable_Type.__name__=_D
_EpSpecificCodecClearModeDataEnable_Object=MibTableColumn
epSpecificCodecClearModeDataEnable=_EpSpecificCodecClearModeDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,500),_EpSpecificCodecClearModeDataEnable_Type())
epSpecificCodecClearModeDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeDataEnable.setStatus(_A)
class _EpSpecificCodecClearModeDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecClearModeDataPriority_Type.__name__=_C
_EpSpecificCodecClearModeDataPriority_Object=MibTableColumn
epSpecificCodecClearModeDataPriority=_EpSpecificCodecClearModeDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,600),_EpSpecificCodecClearModeDataPriority_Type())
epSpecificCodecClearModeDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeDataPriority.setStatus(_A)
class _EpSpecificCodecClearModePayloadType_Type(Unsigned32):defaultValue=124;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecClearModePayloadType_Type.__name__=_C
_EpSpecificCodecClearModePayloadType_Object=MibTableColumn
epSpecificCodecClearModePayloadType=_EpSpecificCodecClearModePayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,700),_EpSpecificCodecClearModePayloadType_Type())
epSpecificCodecClearModePayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModePayloadType.setStatus(_A)
class _EpSpecificCodecClearModeMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecClearModeMinPTime_Type.__name__=_C
_EpSpecificCodecClearModeMinPTime_Object=MibTableColumn
epSpecificCodecClearModeMinPTime=_EpSpecificCodecClearModeMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,800),_EpSpecificCodecClearModeMinPTime_Type())
epSpecificCodecClearModeMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeMinPTime.setStatus(_A)
class _EpSpecificCodecClearModeMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecClearModeMaxPTime_Type.__name__=_C
_EpSpecificCodecClearModeMaxPTime_Object=MibTableColumn
epSpecificCodecClearModeMaxPTime=_EpSpecificCodecClearModeMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,800,800,1,900),_EpSpecificCodecClearModeMaxPTime_Type())
epSpecificCodecClearModeMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearModeMaxPTime.setStatus(_A)
_CodecClearChannelGroup_ObjectIdentity=ObjectIdentity
codecClearChannelGroup=_CodecClearChannelGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900))
class _DefaultCodecClearChannelVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecClearChannelVoiceEnable_Type.__name__=_D
_DefaultCodecClearChannelVoiceEnable_Object=MibScalar
defaultCodecClearChannelVoiceEnable=_DefaultCodecClearChannelVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,100),_DefaultCodecClearChannelVoiceEnable_Type())
defaultCodecClearChannelVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelVoiceEnable.setStatus(_A)
class _DefaultCodecClearChannelVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecClearChannelVoicePriority_Type.__name__=_C
_DefaultCodecClearChannelVoicePriority_Object=MibScalar
defaultCodecClearChannelVoicePriority=_DefaultCodecClearChannelVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,200),_DefaultCodecClearChannelVoicePriority_Type())
defaultCodecClearChannelVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelVoicePriority.setStatus(_A)
class _DefaultCodecClearChannelDataEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecClearChannelDataEnable_Type.__name__=_D
_DefaultCodecClearChannelDataEnable_Object=MibScalar
defaultCodecClearChannelDataEnable=_DefaultCodecClearChannelDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,300),_DefaultCodecClearChannelDataEnable_Type())
defaultCodecClearChannelDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelDataEnable.setStatus(_A)
class _DefaultCodecClearChannelDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecClearChannelDataPriority_Type.__name__=_C
_DefaultCodecClearChannelDataPriority_Object=MibScalar
defaultCodecClearChannelDataPriority=_DefaultCodecClearChannelDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,400),_DefaultCodecClearChannelDataPriority_Type())
defaultCodecClearChannelDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelDataPriority.setStatus(_A)
class _DefaultCodecClearChannelPayloadType_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecClearChannelPayloadType_Type.__name__=_C
_DefaultCodecClearChannelPayloadType_Object=MibScalar
defaultCodecClearChannelPayloadType=_DefaultCodecClearChannelPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,500),_DefaultCodecClearChannelPayloadType_Type())
defaultCodecClearChannelPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelPayloadType.setStatus(_A)
class _DefaultCodecClearChannelMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecClearChannelMinPTime_Type.__name__=_C
_DefaultCodecClearChannelMinPTime_Object=MibScalar
defaultCodecClearChannelMinPTime=_DefaultCodecClearChannelMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,600),_DefaultCodecClearChannelMinPTime_Type())
defaultCodecClearChannelMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelMinPTime.setStatus(_A)
class _DefaultCodecClearChannelMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecClearChannelMaxPTime_Type.__name__=_C
_DefaultCodecClearChannelMaxPTime_Object=MibScalar
defaultCodecClearChannelMaxPTime=_DefaultCodecClearChannelMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,700),_DefaultCodecClearChannelMaxPTime_Type())
defaultCodecClearChannelMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecClearChannelMaxPTime.setStatus(_A)
_EpSpecificCodecClearChannelTable_Object=MibTable
epSpecificCodecClearChannelTable=_EpSpecificCodecClearChannelTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800))
if mibBuilder.loadTexts:epSpecificCodecClearChannelTable.setStatus(_A)
_EpSpecificCodecClearChannelEntry_Object=MibTableRow
epSpecificCodecClearChannelEntry=_EpSpecificCodecClearChannelEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1))
epSpecificCodecClearChannelEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:epSpecificCodecClearChannelEntry.setStatus(_A)
_EpSpecificCodecClearChannelEpId_Type=OctetString
_EpSpecificCodecClearChannelEpId_Object=MibTableColumn
epSpecificCodecClearChannelEpId=_EpSpecificCodecClearChannelEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,100),_EpSpecificCodecClearChannelEpId_Type())
epSpecificCodecClearChannelEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecClearChannelEpId.setStatus(_A)
class _EpSpecificCodecClearChannelEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearChannelEnableConfig_Type.__name__=_D
_EpSpecificCodecClearChannelEnableConfig_Object=MibTableColumn
epSpecificCodecClearChannelEnableConfig=_EpSpecificCodecClearChannelEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,200),_EpSpecificCodecClearChannelEnableConfig_Type())
epSpecificCodecClearChannelEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelEnableConfig.setStatus(_A)
class _EpSpecificCodecClearChannelVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearChannelVoiceEnable_Type.__name__=_D
_EpSpecificCodecClearChannelVoiceEnable_Object=MibTableColumn
epSpecificCodecClearChannelVoiceEnable=_EpSpecificCodecClearChannelVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,300),_EpSpecificCodecClearChannelVoiceEnable_Type())
epSpecificCodecClearChannelVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelVoiceEnable.setStatus(_A)
class _EpSpecificCodecClearChannelVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecClearChannelVoicePriority_Type.__name__=_C
_EpSpecificCodecClearChannelVoicePriority_Object=MibTableColumn
epSpecificCodecClearChannelVoicePriority=_EpSpecificCodecClearChannelVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,400),_EpSpecificCodecClearChannelVoicePriority_Type())
epSpecificCodecClearChannelVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelVoicePriority.setStatus(_A)
class _EpSpecificCodecClearChannelDataEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecClearChannelDataEnable_Type.__name__=_D
_EpSpecificCodecClearChannelDataEnable_Object=MibTableColumn
epSpecificCodecClearChannelDataEnable=_EpSpecificCodecClearChannelDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,500),_EpSpecificCodecClearChannelDataEnable_Type())
epSpecificCodecClearChannelDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelDataEnable.setStatus(_A)
class _EpSpecificCodecClearChannelDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecClearChannelDataPriority_Type.__name__=_C
_EpSpecificCodecClearChannelDataPriority_Object=MibTableColumn
epSpecificCodecClearChannelDataPriority=_EpSpecificCodecClearChannelDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,600),_EpSpecificCodecClearChannelDataPriority_Type())
epSpecificCodecClearChannelDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelDataPriority.setStatus(_A)
class _EpSpecificCodecClearChannelPayloadType_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecClearChannelPayloadType_Type.__name__=_C
_EpSpecificCodecClearChannelPayloadType_Object=MibTableColumn
epSpecificCodecClearChannelPayloadType=_EpSpecificCodecClearChannelPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,700),_EpSpecificCodecClearChannelPayloadType_Type())
epSpecificCodecClearChannelPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelPayloadType.setStatus(_A)
class _EpSpecificCodecClearChannelMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecClearChannelMinPTime_Type.__name__=_C
_EpSpecificCodecClearChannelMinPTime_Object=MibTableColumn
epSpecificCodecClearChannelMinPTime=_EpSpecificCodecClearChannelMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,800),_EpSpecificCodecClearChannelMinPTime_Type())
epSpecificCodecClearChannelMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelMinPTime.setStatus(_A)
class _EpSpecificCodecClearChannelMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecClearChannelMaxPTime_Type.__name__=_C
_EpSpecificCodecClearChannelMaxPTime_Object=MibTableColumn
epSpecificCodecClearChannelMaxPTime=_EpSpecificCodecClearChannelMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,900,800,1,900),_EpSpecificCodecClearChannelMaxPTime_Type())
epSpecificCodecClearChannelMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecClearChannelMaxPTime.setStatus(_A)
_CodecXCCDGroup_ObjectIdentity=ObjectIdentity
codecXCCDGroup=_CodecXCCDGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000))
class _DefaultCodecXCCDVoiceEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecXCCDVoiceEnable_Type.__name__=_D
_DefaultCodecXCCDVoiceEnable_Object=MibScalar
defaultCodecXCCDVoiceEnable=_DefaultCodecXCCDVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,100),_DefaultCodecXCCDVoiceEnable_Type())
defaultCodecXCCDVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDVoiceEnable.setStatus(_A)
class _DefaultCodecXCCDVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecXCCDVoicePriority_Type.__name__=_C
_DefaultCodecXCCDVoicePriority_Object=MibScalar
defaultCodecXCCDVoicePriority=_DefaultCodecXCCDVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,200),_DefaultCodecXCCDVoicePriority_Type())
defaultCodecXCCDVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDVoicePriority.setStatus(_A)
class _DefaultCodecXCCDDataEnable_Type(MxEnableState):defaultValue=0
_DefaultCodecXCCDDataEnable_Type.__name__=_D
_DefaultCodecXCCDDataEnable_Object=MibScalar
defaultCodecXCCDDataEnable=_DefaultCodecXCCDDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,300),_DefaultCodecXCCDDataEnable_Type())
defaultCodecXCCDDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDDataEnable.setStatus(_A)
class _DefaultCodecXCCDDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DefaultCodecXCCDDataPriority_Type.__name__=_C
_DefaultCodecXCCDDataPriority_Object=MibScalar
defaultCodecXCCDDataPriority=_DefaultCodecXCCDDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,400),_DefaultCodecXCCDDataPriority_Type())
defaultCodecXCCDDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDDataPriority.setStatus(_A)
class _DefaultCodecXCCDPayloadType_Type(Unsigned32):defaultValue=126;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultCodecXCCDPayloadType_Type.__name__=_C
_DefaultCodecXCCDPayloadType_Object=MibScalar
defaultCodecXCCDPayloadType=_DefaultCodecXCCDPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,500),_DefaultCodecXCCDPayloadType_Type())
defaultCodecXCCDPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDPayloadType.setStatus(_A)
class _DefaultCodecXCCDMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecXCCDMinPTime_Type.__name__=_C
_DefaultCodecXCCDMinPTime_Object=MibScalar
defaultCodecXCCDMinPTime=_DefaultCodecXCCDMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,600),_DefaultCodecXCCDMinPTime_Type())
defaultCodecXCCDMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDMinPTime.setStatus(_A)
class _DefaultCodecXCCDMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_DefaultCodecXCCDMaxPTime_Type.__name__=_C
_DefaultCodecXCCDMaxPTime_Object=MibScalar
defaultCodecXCCDMaxPTime=_DefaultCodecXCCDMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,700),_DefaultCodecXCCDMaxPTime_Type())
defaultCodecXCCDMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecXCCDMaxPTime.setStatus(_A)
_EpSpecificCodecXCCDTable_Object=MibTable
epSpecificCodecXCCDTable=_EpSpecificCodecXCCDTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800))
if mibBuilder.loadTexts:epSpecificCodecXCCDTable.setStatus(_A)
_EpSpecificCodecXCCDEntry_Object=MibTableRow
epSpecificCodecXCCDEntry=_EpSpecificCodecXCCDEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1))
epSpecificCodecXCCDEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:epSpecificCodecXCCDEntry.setStatus(_A)
_EpSpecificCodecXCCDEpId_Type=OctetString
_EpSpecificCodecXCCDEpId_Object=MibTableColumn
epSpecificCodecXCCDEpId=_EpSpecificCodecXCCDEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,100),_EpSpecificCodecXCCDEpId_Type())
epSpecificCodecXCCDEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificCodecXCCDEpId.setStatus(_A)
class _EpSpecificCodecXCCDEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificCodecXCCDEnableConfig_Type.__name__=_D
_EpSpecificCodecXCCDEnableConfig_Object=MibTableColumn
epSpecificCodecXCCDEnableConfig=_EpSpecificCodecXCCDEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,200),_EpSpecificCodecXCCDEnableConfig_Type())
epSpecificCodecXCCDEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDEnableConfig.setStatus(_A)
class _EpSpecificCodecXCCDVoiceEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecXCCDVoiceEnable_Type.__name__=_D
_EpSpecificCodecXCCDVoiceEnable_Object=MibTableColumn
epSpecificCodecXCCDVoiceEnable=_EpSpecificCodecXCCDVoiceEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,300),_EpSpecificCodecXCCDVoiceEnable_Type())
epSpecificCodecXCCDVoiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDVoiceEnable.setStatus(_A)
class _EpSpecificCodecXCCDVoicePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecXCCDVoicePriority_Type.__name__=_C
_EpSpecificCodecXCCDVoicePriority_Object=MibTableColumn
epSpecificCodecXCCDVoicePriority=_EpSpecificCodecXCCDVoicePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,400),_EpSpecificCodecXCCDVoicePriority_Type())
epSpecificCodecXCCDVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDVoicePriority.setStatus(_A)
class _EpSpecificCodecXCCDDataEnable_Type(MxEnableState):defaultValue=0
_EpSpecificCodecXCCDDataEnable_Type.__name__=_D
_EpSpecificCodecXCCDDataEnable_Object=MibTableColumn
epSpecificCodecXCCDDataEnable=_EpSpecificCodecXCCDDataEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,500),_EpSpecificCodecXCCDDataEnable_Type())
epSpecificCodecXCCDDataEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDDataEnable.setStatus(_A)
class _EpSpecificCodecXCCDDataPriority_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EpSpecificCodecXCCDDataPriority_Type.__name__=_C
_EpSpecificCodecXCCDDataPriority_Object=MibTableColumn
epSpecificCodecXCCDDataPriority=_EpSpecificCodecXCCDDataPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,600),_EpSpecificCodecXCCDDataPriority_Type())
epSpecificCodecXCCDDataPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDDataPriority.setStatus(_A)
class _EpSpecificCodecXCCDPayloadType_Type(Unsigned32):defaultValue=126;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificCodecXCCDPayloadType_Type.__name__=_C
_EpSpecificCodecXCCDPayloadType_Object=MibTableColumn
epSpecificCodecXCCDPayloadType=_EpSpecificCodecXCCDPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,700),_EpSpecificCodecXCCDPayloadType_Type())
epSpecificCodecXCCDPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDPayloadType.setStatus(_A)
class _EpSpecificCodecXCCDMinPTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecXCCDMinPTime_Type.__name__=_C
_EpSpecificCodecXCCDMinPTime_Object=MibTableColumn
epSpecificCodecXCCDMinPTime=_EpSpecificCodecXCCDMinPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,800),_EpSpecificCodecXCCDMinPTime_Type())
epSpecificCodecXCCDMinPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDMinPTime.setStatus(_A)
class _EpSpecificCodecXCCDMaxPTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_EpSpecificCodecXCCDMaxPTime_Type.__name__=_C
_EpSpecificCodecXCCDMaxPTime_Object=MibTableColumn
epSpecificCodecXCCDMaxPTime=_EpSpecificCodecXCCDMaxPTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,100,1000,800,1,900),_EpSpecificCodecXCCDMaxPTime_Type())
epSpecificCodecXCCDMaxPTime.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificCodecXCCDMaxPTime.setStatus(_A)
_JitterBufferGroup_ObjectIdentity=ObjectIdentity
jitterBufferGroup=_JitterBufferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200))
class _DefaultJitterBufferLevel_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*((_e,100),(_f,200),(_g,300),(_h,400),(_i,500)))
_DefaultJitterBufferLevel_Type.__name__=_F
_DefaultJitterBufferLevel_Object=MibScalar
defaultJitterBufferLevel=_DefaultJitterBufferLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,100),_DefaultJitterBufferLevel_Type())
defaultJitterBufferLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultJitterBufferLevel.setStatus(_A)
class _DefaultJitterBufferCustomMinLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultJitterBufferCustomMinLength_Type.__name__=_C
_DefaultJitterBufferCustomMinLength_Object=MibScalar
defaultJitterBufferCustomMinLength=_DefaultJitterBufferCustomMinLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,200),_DefaultJitterBufferCustomMinLength_Type())
defaultJitterBufferCustomMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultJitterBufferCustomMinLength.setStatus(_A)
class _DefaultJitterBufferCustomNomLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultJitterBufferCustomNomLength_Type.__name__=_C
_DefaultJitterBufferCustomNomLength_Object=MibScalar
defaultJitterBufferCustomNomLength=_DefaultJitterBufferCustomNomLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,210),_DefaultJitterBufferCustomNomLength_Type())
defaultJitterBufferCustomNomLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultJitterBufferCustomNomLength.setStatus(_A)
class _DefaultJitterBufferCustomMaxLength_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultJitterBufferCustomMaxLength_Type.__name__=_C
_DefaultJitterBufferCustomMaxLength_Object=MibScalar
defaultJitterBufferCustomMaxLength=_DefaultJitterBufferCustomMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,300),_DefaultJitterBufferCustomMaxLength_Type())
defaultJitterBufferCustomMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultJitterBufferCustomMaxLength.setStatus(_A)
class _DefaultVbdJitterBufferCustomMinLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultVbdJitterBufferCustomMinLength_Type.__name__=_C
_DefaultVbdJitterBufferCustomMinLength_Object=MibScalar
defaultVbdJitterBufferCustomMinLength=_DefaultVbdJitterBufferCustomMinLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,310),_DefaultVbdJitterBufferCustomMinLength_Type())
defaultVbdJitterBufferCustomMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultVbdJitterBufferCustomMinLength.setStatus(_A)
class _DefaultVbdJitterBufferCustomNomLength_Type(Unsigned32):defaultValue=67;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultVbdJitterBufferCustomNomLength_Type.__name__=_C
_DefaultVbdJitterBufferCustomNomLength_Object=MibScalar
defaultVbdJitterBufferCustomNomLength=_DefaultVbdJitterBufferCustomNomLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,320),_DefaultVbdJitterBufferCustomNomLength_Type())
defaultVbdJitterBufferCustomNomLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultVbdJitterBufferCustomNomLength.setStatus(_A)
class _DefaultVbdJitterBufferCustomMaxLength_Type(Unsigned32):defaultValue=135;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_DefaultVbdJitterBufferCustomMaxLength_Type.__name__=_C
_DefaultVbdJitterBufferCustomMaxLength_Object=MibScalar
defaultVbdJitterBufferCustomMaxLength=_DefaultVbdJitterBufferCustomMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,330),_DefaultVbdJitterBufferCustomMaxLength_Type())
defaultVbdJitterBufferCustomMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultVbdJitterBufferCustomMaxLength.setStatus(_A)
class _DefaultVbdJitterBufferType_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_j,100),(_k,200),('fixed',300)))
_DefaultVbdJitterBufferType_Type.__name__=_F
_DefaultVbdJitterBufferType_Object=MibScalar
defaultVbdJitterBufferType=_DefaultVbdJitterBufferType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,340),_DefaultVbdJitterBufferType_Type())
defaultVbdJitterBufferType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultVbdJitterBufferType.setStatus(_A)
_EpSpecificJitterBufferTable_Object=MibTable
epSpecificJitterBufferTable=_EpSpecificJitterBufferTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400))
if mibBuilder.loadTexts:epSpecificJitterBufferTable.setStatus(_A)
_EpSpecificJitterBufferEntry_Object=MibTableRow
epSpecificJitterBufferEntry=_EpSpecificJitterBufferEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1))
epSpecificJitterBufferEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:epSpecificJitterBufferEntry.setStatus(_A)
_EpSpecificJitterBufferEpId_Type=OctetString
_EpSpecificJitterBufferEpId_Object=MibTableColumn
epSpecificJitterBufferEpId=_EpSpecificJitterBufferEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,100),_EpSpecificJitterBufferEpId_Type())
epSpecificJitterBufferEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificJitterBufferEpId.setStatus(_A)
class _EpSpecificJitterBufferEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificJitterBufferEnableConfig_Type.__name__=_D
_EpSpecificJitterBufferEnableConfig_Object=MibTableColumn
epSpecificJitterBufferEnableConfig=_EpSpecificJitterBufferEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,200),_EpSpecificJitterBufferEnableConfig_Type())
epSpecificJitterBufferEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferEnableConfig.setStatus(_A)
class _EpSpecificJitterBufferLevel_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*((_e,100),(_f,200),(_g,300),(_h,400),(_i,500)))
_EpSpecificJitterBufferLevel_Type.__name__=_F
_EpSpecificJitterBufferLevel_Object=MibTableColumn
epSpecificJitterBufferLevel=_EpSpecificJitterBufferLevel_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,300),_EpSpecificJitterBufferLevel_Type())
epSpecificJitterBufferLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferLevel.setStatus(_A)
class _EpSpecificJitterBufferCustomMinLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomMinLength_Type.__name__=_C
_EpSpecificJitterBufferCustomMinLength_Object=MibTableColumn
epSpecificJitterBufferCustomMinLength=_EpSpecificJitterBufferCustomMinLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,400),_EpSpecificJitterBufferCustomMinLength_Type())
epSpecificJitterBufferCustomMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomMinLength.setStatus(_A)
class _EpSpecificJitterBufferCustomNomLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomNomLength_Type.__name__=_C
_EpSpecificJitterBufferCustomNomLength_Object=MibTableColumn
epSpecificJitterBufferCustomNomLength=_EpSpecificJitterBufferCustomNomLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,410),_EpSpecificJitterBufferCustomNomLength_Type())
epSpecificJitterBufferCustomNomLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomNomLength.setStatus(_A)
class _EpSpecificJitterBufferCustomMaxLength_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomMaxLength_Type.__name__=_C
_EpSpecificJitterBufferCustomMaxLength_Object=MibTableColumn
epSpecificJitterBufferCustomMaxLength=_EpSpecificJitterBufferCustomMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,500),_EpSpecificJitterBufferCustomMaxLength_Type())
epSpecificJitterBufferCustomMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomMaxLength.setStatus(_A)
class _EpSpecificJitterBufferCustomVbdMinLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomVbdMinLength_Type.__name__=_C
_EpSpecificJitterBufferCustomVbdMinLength_Object=MibTableColumn
epSpecificJitterBufferCustomVbdMinLength=_EpSpecificJitterBufferCustomVbdMinLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,600),_EpSpecificJitterBufferCustomVbdMinLength_Type())
epSpecificJitterBufferCustomVbdMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomVbdMinLength.setStatus(_A)
class _EpSpecificJitterBufferCustomVbdNomLength_Type(Unsigned32):defaultValue=67;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomVbdNomLength_Type.__name__=_C
_EpSpecificJitterBufferCustomVbdNomLength_Object=MibTableColumn
epSpecificJitterBufferCustomVbdNomLength=_EpSpecificJitterBufferCustomVbdNomLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,700),_EpSpecificJitterBufferCustomVbdNomLength_Type())
epSpecificJitterBufferCustomVbdNomLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomVbdNomLength.setStatus(_A)
class _EpSpecificJitterBufferCustomVbdMaxLength_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EpSpecificJitterBufferCustomVbdMaxLength_Type.__name__=_C
_EpSpecificJitterBufferCustomVbdMaxLength_Object=MibTableColumn
epSpecificJitterBufferCustomVbdMaxLength=_EpSpecificJitterBufferCustomVbdMaxLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,800),_EpSpecificJitterBufferCustomVbdMaxLength_Type())
epSpecificJitterBufferCustomVbdMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomVbdMaxLength.setStatus(_A)
class _EpSpecificJitterBufferCustomVbdJitterBufferType_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_j,100),(_k,200),('fixed',300)))
_EpSpecificJitterBufferCustomVbdJitterBufferType_Type.__name__=_F
_EpSpecificJitterBufferCustomVbdJitterBufferType_Object=MibTableColumn
epSpecificJitterBufferCustomVbdJitterBufferType=_EpSpecificJitterBufferCustomVbdJitterBufferType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,200,400,1,900),_EpSpecificJitterBufferCustomVbdJitterBufferType_Type())
epSpecificJitterBufferCustomVbdJitterBufferType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificJitterBufferCustomVbdJitterBufferType.setStatus(_A)
_DtmfTransportGroup_ObjectIdentity=ObjectIdentity
dtmfTransportGroup=_DtmfTransportGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300))
class _DefaultDtmfTransportMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_m,100),(_n,200),(_o,300),(_p,400)))
_DefaultDtmfTransportMethod_Type.__name__=_F
_DefaultDtmfTransportMethod_Object=MibScalar
defaultDtmfTransportMethod=_DefaultDtmfTransportMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,100),_DefaultDtmfTransportMethod_Type())
defaultDtmfTransportMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDtmfTransportMethod.setStatus(_A)
class _DefaultDtmfTransportPayloadType_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_DefaultDtmfTransportPayloadType_Type.__name__=_C
_DefaultDtmfTransportPayloadType_Object=MibScalar
defaultDtmfTransportPayloadType=_DefaultDtmfTransportPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,200),_DefaultDtmfTransportPayloadType_Type())
defaultDtmfTransportPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDtmfTransportPayloadType.setStatus(_A)
_EpSpecificDtmfTransportTable_Object=MibTable
epSpecificDtmfTransportTable=_EpSpecificDtmfTransportTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300))
if mibBuilder.loadTexts:epSpecificDtmfTransportTable.setStatus(_A)
_EpSpecificDtmfTransportEntry_Object=MibTableRow
epSpecificDtmfTransportEntry=_EpSpecificDtmfTransportEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300,1))
epSpecificDtmfTransportEntry.setIndexNames((0,_G,_q))
if mibBuilder.loadTexts:epSpecificDtmfTransportEntry.setStatus(_A)
_EpSpecificDtmfTransportEpId_Type=OctetString
_EpSpecificDtmfTransportEpId_Object=MibTableColumn
epSpecificDtmfTransportEpId=_EpSpecificDtmfTransportEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300,1,100),_EpSpecificDtmfTransportEpId_Type())
epSpecificDtmfTransportEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificDtmfTransportEpId.setStatus(_A)
class _EpSpecificDtmfTransportEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificDtmfTransportEnableConfig_Type.__name__=_D
_EpSpecificDtmfTransportEnableConfig_Object=MibTableColumn
epSpecificDtmfTransportEnableConfig=_EpSpecificDtmfTransportEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300,1,200),_EpSpecificDtmfTransportEnableConfig_Type())
epSpecificDtmfTransportEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfTransportEnableConfig.setStatus(_A)
class _EpSpecificDtmfTransportMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_m,100),(_n,200),(_o,300),(_p,400)))
_EpSpecificDtmfTransportMethod_Type.__name__=_F
_EpSpecificDtmfTransportMethod_Object=MibTableColumn
epSpecificDtmfTransportMethod=_EpSpecificDtmfTransportMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300,1,300),_EpSpecificDtmfTransportMethod_Type())
epSpecificDtmfTransportMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfTransportMethod.setStatus(_A)
class _EpSpecificDtmfTransportPayloadType_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_EpSpecificDtmfTransportPayloadType_Type.__name__=_C
_EpSpecificDtmfTransportPayloadType_Object=MibTableColumn
epSpecificDtmfTransportPayloadType=_EpSpecificDtmfTransportPayloadType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,300,300,1,400),_EpSpecificDtmfTransportPayloadType_Type())
epSpecificDtmfTransportPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificDtmfTransportPayloadType.setStatus(_A)
_IpTransportGroup_ObjectIdentity=ObjectIdentity
ipTransportGroup=_IpTransportGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400))
_IpTransportRtpGroup_ObjectIdentity=ObjectIdentity
ipTransportRtpGroup=_IpTransportRtpGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400,100))
class _IpTransportRtpBasePort_Type(Unsigned32):defaultValue=5004;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65435))
_IpTransportRtpBasePort_Type.__name__=_C
_IpTransportRtpBasePort_Object=MibScalar
ipTransportRtpBasePort=_IpTransportRtpBasePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400,100,100),_IpTransportRtpBasePort_Type())
ipTransportRtpBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipTransportRtpBasePort.setStatus(_A)
class _IpTransportSrtpBasePort_Type(Unsigned32):defaultValue=5004;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1025,65435))
_IpTransportSrtpBasePort_Type.__name__=_C
_IpTransportSrtpBasePort_Object=MibScalar
ipTransportSrtpBasePort=_IpTransportSrtpBasePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400,100,200),_IpTransportSrtpBasePort_Type())
ipTransportSrtpBasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipTransportSrtpBasePort.setStatus(_A)
_IpTransportT38Group_ObjectIdentity=ObjectIdentity
ipTransportT38Group=_IpTransportT38Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400,200))
class _IpTransportT38BasePort_Type(Unsigned32):defaultValue=6004;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65435))
_IpTransportT38BasePort_Type.__name__=_C
_IpTransportT38BasePort_Object=MibScalar
ipTransportT38BasePort=_IpTransportT38BasePort_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,400,200,100),_IpTransportT38BasePort_Type())
ipTransportT38BasePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipTransportT38BasePort.setStatus(_A)
_CodecVsBearerCapabilitiesMapping_ObjectIdentity=ObjectIdentity
codecVsBearerCapabilitiesMapping=_CodecVsBearerCapabilitiesMapping_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500))
_DefaultCodecVsBearerCapabilitiesMappingTable_Object=MibTable
defaultCodecVsBearerCapabilitiesMappingTable=_DefaultCodecVsBearerCapabilitiesMappingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100))
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingTable.setStatus(_A)
_DefaultCodecVsBearerCapabilitiesMappingEntry_Object=MibTableRow
defaultCodecVsBearerCapabilitiesMappingEntry=_DefaultCodecVsBearerCapabilitiesMappingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1))
defaultCodecVsBearerCapabilitiesMappingEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingEntry.setStatus(_A)
class _DefaultCodecVsBearerCapabilitiesMappingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_DefaultCodecVsBearerCapabilitiesMappingIndex_Type.__name__=_C
_DefaultCodecVsBearerCapabilitiesMappingIndex_Object=MibTableColumn
defaultCodecVsBearerCapabilitiesMappingIndex=_DefaultCodecVsBearerCapabilitiesMappingIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1,100),_DefaultCodecVsBearerCapabilitiesMappingIndex_Type())
defaultCodecVsBearerCapabilitiesMappingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingIndex.setStatus(_A)
class _DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type(MxEnableState):defaultValue=0
_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type.__name__=_D
_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Object=MibTableColumn
defaultCodecVsBearerCapabilitiesMappingEnableMap=_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1,200),_DefaultCodecVsBearerCapabilitiesMappingEnableMap_Type())
defaultCodecVsBearerCapabilitiesMappingEnableMap.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingEnableMap.setStatus(_A)
class _DefaultCodecVsBearerCapabilitiesMappingCodec_Type(Integer32):defaultValue=800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,250,300,400,500,600,700,800,900,1000,1100)));namedValues=NamedValues(*(('g711alaw',100),('g711ulaw',200),('g722',250),('g723',300),('g72616kbps',400),('g72624kbps',500),('g72632kbps',600),('g72640kbps',700),('g729',800),('clearMode',900),('clearChannel',1000),('xCCD',1100)))
_DefaultCodecVsBearerCapabilitiesMappingCodec_Type.__name__=_F
_DefaultCodecVsBearerCapabilitiesMappingCodec_Object=MibTableColumn
defaultCodecVsBearerCapabilitiesMappingCodec=_DefaultCodecVsBearerCapabilitiesMappingCodec_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1,300),_DefaultCodecVsBearerCapabilitiesMappingCodec_Type())
defaultCodecVsBearerCapabilitiesMappingCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingCodec.setStatus(_A)
class _DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('audio31kHz',100),('speech',200),('unrestricted',300)))
_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type.__name__=_F
_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Object=MibTableColumn
defaultCodecVsBearerCapabilitiesMappingInformationTransferCap=_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1,400),_DefaultCodecVsBearerCapabilitiesMappingInformationTransferCap_Type())
defaultCodecVsBearerCapabilitiesMappingInformationTransferCap.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingInformationTransferCap.setStatus(_A)
class _DefaultCodecVsBearerCapabilitiesMappingMappingType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('prioritize',100),('select',200)))
_DefaultCodecVsBearerCapabilitiesMappingMappingType_Type.__name__=_F
_DefaultCodecVsBearerCapabilitiesMappingMappingType_Object=MibTableColumn
defaultCodecVsBearerCapabilitiesMappingMappingType=_DefaultCodecVsBearerCapabilitiesMappingMappingType_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,500,100,1,500),_DefaultCodecVsBearerCapabilitiesMappingMappingType_Type())
defaultCodecVsBearerCapabilitiesMappingMappingType.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCodecVsBearerCapabilitiesMappingMappingType.setStatus(_A)
_SecurityGroup_ObjectIdentity=ObjectIdentity
securityGroup=_SecurityGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600))
class _DefaultSecurityRtpMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_s,100),(_t,200),(_u,300)))
_DefaultSecurityRtpMode_Type.__name__=_F
_DefaultSecurityRtpMode_Object=MibScalar
defaultSecurityRtpMode=_DefaultSecurityRtpMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,100),_DefaultSecurityRtpMode_Type())
defaultSecurityRtpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSecurityRtpMode.setStatus(_A)
class _DefaultSecurityKeyManagement_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mikey',100),('sdes',200)))
_DefaultSecurityKeyManagement_Type.__name__=_F
_DefaultSecurityKeyManagement_Object=MibScalar
defaultSecurityKeyManagement=_DefaultSecurityKeyManagement_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,150),_DefaultSecurityKeyManagement_Type())
defaultSecurityKeyManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSecurityKeyManagement.setStatus(_A)
class _DefaultSecurityRtpEncryption_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('null',100),(_v,200)))
_DefaultSecurityRtpEncryption_Type.__name__=_F
_DefaultSecurityRtpEncryption_Object=MibScalar
defaultSecurityRtpEncryption=_DefaultSecurityRtpEncryption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,200),_DefaultSecurityRtpEncryption_Type())
defaultSecurityRtpEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultSecurityRtpEncryption.setStatus(_A)
class _AllowUnsecureT38WithSrtp_Type(MxEnableState):defaultValue=0
_AllowUnsecureT38WithSrtp_Type.__name__=_D
_AllowUnsecureT38WithSrtp_Object=MibScalar
allowUnsecureT38WithSrtp=_AllowUnsecureT38WithSrtp_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,300),_AllowUnsecureT38WithSrtp_Type())
allowUnsecureT38WithSrtp.setMaxAccess(_B)
if mibBuilder.loadTexts:allowUnsecureT38WithSrtp.setStatus(_A)
class _SessionUpdateCryptoMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('regenerate',100),('keep',200)))
_SessionUpdateCryptoMode_Type.__name__=_F
_SessionUpdateCryptoMode_Object=MibScalar
sessionUpdateCryptoMode=_SessionUpdateCryptoMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,350),_SessionUpdateCryptoMode_Type())
sessionUpdateCryptoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:sessionUpdateCryptoMode.setStatus(_A)
_EpSpecificSecurityTable_Object=MibTable
epSpecificSecurityTable=_EpSpecificSecurityTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400))
if mibBuilder.loadTexts:epSpecificSecurityTable.setStatus(_A)
_EpSpecificSecurityEntry_Object=MibTableRow
epSpecificSecurityEntry=_EpSpecificSecurityEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1))
epSpecificSecurityEntry.setIndexNames((0,_G,_w))
if mibBuilder.loadTexts:epSpecificSecurityEntry.setStatus(_A)
_EpSpecificSecurityEpId_Type=OctetString
_EpSpecificSecurityEpId_Object=MibTableColumn
epSpecificSecurityEpId=_EpSpecificSecurityEpId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1,100),_EpSpecificSecurityEpId_Type())
epSpecificSecurityEpId.setMaxAccess(_E)
if mibBuilder.loadTexts:epSpecificSecurityEpId.setStatus(_A)
class _EpSpecificSecurityEnableConfig_Type(MxEnableState):defaultValue=0
_EpSpecificSecurityEnableConfig_Type.__name__=_D
_EpSpecificSecurityEnableConfig_Object=MibTableColumn
epSpecificSecurityEnableConfig=_EpSpecificSecurityEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1,200),_EpSpecificSecurityEnableConfig_Type())
epSpecificSecurityEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecurityEnableConfig.setStatus(_A)
class _EpSpecificSecurityRtpMode_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*((_s,100),(_t,200),(_u,300)))
_EpSpecificSecurityRtpMode_Type.__name__=_F
_EpSpecificSecurityRtpMode_Object=MibTableColumn
epSpecificSecurityRtpMode=_EpSpecificSecurityRtpMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1,300),_EpSpecificSecurityRtpMode_Type())
epSpecificSecurityRtpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecurityRtpMode.setStatus(_A)
class _EpSpecificSecurityKeyManagement_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mikey',100),('sdes',200)))
_EpSpecificSecurityKeyManagement_Type.__name__=_F
_EpSpecificSecurityKeyManagement_Object=MibTableColumn
epSpecificSecurityKeyManagement=_EpSpecificSecurityKeyManagement_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1,350),_EpSpecificSecurityKeyManagement_Type())
epSpecificSecurityKeyManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecurityKeyManagement.setStatus(_A)
class _EpSpecificSecurityRtpEncryption_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('null',100),(_v,200)))
_EpSpecificSecurityRtpEncryption_Type.__name__=_F
_EpSpecificSecurityRtpEncryption_Object=MibTableColumn
epSpecificSecurityRtpEncryption=_EpSpecificSecurityRtpEncryption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,600,400,1,400),_EpSpecificSecurityRtpEncryption_Type())
epSpecificSecurityRtpEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:epSpecificSecurityRtpEncryption.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700))
_LastConnectionsStatsTable_Object=MibTable
lastConnectionsStatsTable=_LastConnectionsStatsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100))
if mibBuilder.loadTexts:lastConnectionsStatsTable.setStatus(_A)
_LastConnectionsStatsEntry_Object=MibTableRow
lastConnectionsStatsEntry=_LastConnectionsStatsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1))
lastConnectionsStatsEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:lastConnectionsStatsEntry.setStatus(_A)
class _LastConnectionsStatsConnectionsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LastConnectionsStatsConnectionsIndex_Type.__name__=_C
_LastConnectionsStatsConnectionsIndex_Object=MibTableColumn
lastConnectionsStatsConnectionsIndex=_LastConnectionsStatsConnectionsIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,100),_LastConnectionsStatsConnectionsIndex_Type())
lastConnectionsStatsConnectionsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsConnectionsIndex.setStatus(_A)
_LastConnectionsStatsOctetsTransmitted_Type=MxUInt64
_LastConnectionsStatsOctetsTransmitted_Object=MibTableColumn
lastConnectionsStatsOctetsTransmitted=_LastConnectionsStatsOctetsTransmitted_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,200),_LastConnectionsStatsOctetsTransmitted_Type())
lastConnectionsStatsOctetsTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsOctetsTransmitted.setStatus(_A)
_LastConnectionsStatsOctetsReceived_Type=MxUInt64
_LastConnectionsStatsOctetsReceived_Object=MibTableColumn
lastConnectionsStatsOctetsReceived=_LastConnectionsStatsOctetsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,300),_LastConnectionsStatsOctetsReceived_Type())
lastConnectionsStatsOctetsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsOctetsReceived.setStatus(_A)
_LastConnectionsStatsPacketsTransmitted_Type=MxUInt64
_LastConnectionsStatsPacketsTransmitted_Object=MibTableColumn
lastConnectionsStatsPacketsTransmitted=_LastConnectionsStatsPacketsTransmitted_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,400),_LastConnectionsStatsPacketsTransmitted_Type())
lastConnectionsStatsPacketsTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsPacketsTransmitted.setStatus(_A)
_LastConnectionsStatsPacketsReceived_Type=MxUInt64
_LastConnectionsStatsPacketsReceived_Object=MibTableColumn
lastConnectionsStatsPacketsReceived=_LastConnectionsStatsPacketsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,500),_LastConnectionsStatsPacketsReceived_Type())
lastConnectionsStatsPacketsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsPacketsReceived.setStatus(_A)
_LastConnectionsStatsPacketsLost_Type=Unsigned32
_LastConnectionsStatsPacketsLost_Object=MibTableColumn
lastConnectionsStatsPacketsLost=_LastConnectionsStatsPacketsLost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,600),_LastConnectionsStatsPacketsLost_Type())
lastConnectionsStatsPacketsLost.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsPacketsLost.setStatus(_A)
_LastConnectionsStatsMinimumInterarrivalJitter_Type=Unsigned32
_LastConnectionsStatsMinimumInterarrivalJitter_Object=MibTableColumn
lastConnectionsStatsMinimumInterarrivalJitter=_LastConnectionsStatsMinimumInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,700),_LastConnectionsStatsMinimumInterarrivalJitter_Type())
lastConnectionsStatsMinimumInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsMinimumInterarrivalJitter.setStatus(_A)
_LastConnectionsStatsMaximumInterarrivalJitter_Type=Unsigned32
_LastConnectionsStatsMaximumInterarrivalJitter_Object=MibTableColumn
lastConnectionsStatsMaximumInterarrivalJitter=_LastConnectionsStatsMaximumInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,800),_LastConnectionsStatsMaximumInterarrivalJitter_Type())
lastConnectionsStatsMaximumInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsMaximumInterarrivalJitter.setStatus(_A)
_LastConnectionsStatsAverageInterarrivalJitter_Type=Unsigned32
_LastConnectionsStatsAverageInterarrivalJitter_Object=MibTableColumn
lastConnectionsStatsAverageInterarrivalJitter=_LastConnectionsStatsAverageInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,900),_LastConnectionsStatsAverageInterarrivalJitter_Type())
lastConnectionsStatsAverageInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsAverageInterarrivalJitter.setStatus(_A)
_LastConnectionsStatsMinimumLatency_Type=Unsigned32
_LastConnectionsStatsMinimumLatency_Object=MibTableColumn
lastConnectionsStatsMinimumLatency=_LastConnectionsStatsMinimumLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,1000),_LastConnectionsStatsMinimumLatency_Type())
lastConnectionsStatsMinimumLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsMinimumLatency.setStatus(_A)
_LastConnectionsStatsMaximumLatency_Type=Unsigned32
_LastConnectionsStatsMaximumLatency_Object=MibTableColumn
lastConnectionsStatsMaximumLatency=_LastConnectionsStatsMaximumLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,1100),_LastConnectionsStatsMaximumLatency_Type())
lastConnectionsStatsMaximumLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsMaximumLatency.setStatus(_A)
_LastConnectionsStatsAverageLatency_Type=Unsigned32
_LastConnectionsStatsAverageLatency_Object=MibTableColumn
lastConnectionsStatsAverageLatency=_LastConnectionsStatsAverageLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,100,1,1200),_LastConnectionsStatsAverageLatency_Type())
lastConnectionsStatsAverageLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastConnectionsStatsAverageLatency.setStatus(_A)
_LastPeriodsStatsTable_Object=MibTable
lastPeriodsStatsTable=_LastPeriodsStatsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200))
if mibBuilder.loadTexts:lastPeriodsStatsTable.setStatus(_A)
_LastPeriodsStatsEntry_Object=MibTableRow
lastPeriodsStatsEntry=_LastPeriodsStatsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1))
lastPeriodsStatsEntry.setIndexNames((0,_G,_y))
if mibBuilder.loadTexts:lastPeriodsStatsEntry.setStatus(_A)
class _LastPeriodsStatsPeriodIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LastPeriodsStatsPeriodIndex_Type.__name__=_C
_LastPeriodsStatsPeriodIndex_Object=MibTableColumn
lastPeriodsStatsPeriodIndex=_LastPeriodsStatsPeriodIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,100),_LastPeriodsStatsPeriodIndex_Type())
lastPeriodsStatsPeriodIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPeriodIndex.setStatus(_A)
_LastPeriodsStatsOctetsTransmitted_Type=MxUInt64
_LastPeriodsStatsOctetsTransmitted_Object=MibTableColumn
lastPeriodsStatsOctetsTransmitted=_LastPeriodsStatsOctetsTransmitted_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,200),_LastPeriodsStatsOctetsTransmitted_Type())
lastPeriodsStatsOctetsTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsOctetsTransmitted.setStatus(_A)
_LastPeriodsStatsOctetsReceived_Type=MxUInt64
_LastPeriodsStatsOctetsReceived_Object=MibTableColumn
lastPeriodsStatsOctetsReceived=_LastPeriodsStatsOctetsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,300),_LastPeriodsStatsOctetsReceived_Type())
lastPeriodsStatsOctetsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsOctetsReceived.setStatus(_A)
_LastPeriodsStatsPacketsTransmitted_Type=MxUInt64
_LastPeriodsStatsPacketsTransmitted_Object=MibTableColumn
lastPeriodsStatsPacketsTransmitted=_LastPeriodsStatsPacketsTransmitted_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,400),_LastPeriodsStatsPacketsTransmitted_Type())
lastPeriodsStatsPacketsTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPacketsTransmitted.setStatus(_A)
_LastPeriodsStatsPacketsReceived_Type=MxUInt64
_LastPeriodsStatsPacketsReceived_Object=MibTableColumn
lastPeriodsStatsPacketsReceived=_LastPeriodsStatsPacketsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,500),_LastPeriodsStatsPacketsReceived_Type())
lastPeriodsStatsPacketsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPacketsReceived.setStatus(_A)
_LastPeriodsStatsPacketsLost_Type=Unsigned32
_LastPeriodsStatsPacketsLost_Object=MibTableColumn
lastPeriodsStatsPacketsLost=_LastPeriodsStatsPacketsLost_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,600),_LastPeriodsStatsPacketsLost_Type())
lastPeriodsStatsPacketsLost.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPacketsLost.setStatus(_A)
_LastPeriodsStatsMinimumInterarrivalJitter_Type=Unsigned32
_LastPeriodsStatsMinimumInterarrivalJitter_Object=MibTableColumn
lastPeriodsStatsMinimumInterarrivalJitter=_LastPeriodsStatsMinimumInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,700),_LastPeriodsStatsMinimumInterarrivalJitter_Type())
lastPeriodsStatsMinimumInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsMinimumInterarrivalJitter.setStatus(_A)
_LastPeriodsStatsMaximumInterarrivalJitter_Type=Unsigned32
_LastPeriodsStatsMaximumInterarrivalJitter_Object=MibTableColumn
lastPeriodsStatsMaximumInterarrivalJitter=_LastPeriodsStatsMaximumInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,800),_LastPeriodsStatsMaximumInterarrivalJitter_Type())
lastPeriodsStatsMaximumInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsMaximumInterarrivalJitter.setStatus(_A)
_LastPeriodsStatsAverageInterarrivalJitter_Type=Unsigned32
_LastPeriodsStatsAverageInterarrivalJitter_Object=MibTableColumn
lastPeriodsStatsAverageInterarrivalJitter=_LastPeriodsStatsAverageInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,900),_LastPeriodsStatsAverageInterarrivalJitter_Type())
lastPeriodsStatsAverageInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsAverageInterarrivalJitter.setStatus(_A)
_LastPeriodsStatsMinimumLatency_Type=Unsigned32
_LastPeriodsStatsMinimumLatency_Object=MibTableColumn
lastPeriodsStatsMinimumLatency=_LastPeriodsStatsMinimumLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,1000),_LastPeriodsStatsMinimumLatency_Type())
lastPeriodsStatsMinimumLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsMinimumLatency.setStatus(_A)
_LastPeriodsStatsMaximumLatency_Type=Unsigned32
_LastPeriodsStatsMaximumLatency_Object=MibTableColumn
lastPeriodsStatsMaximumLatency=_LastPeriodsStatsMaximumLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,1100),_LastPeriodsStatsMaximumLatency_Type())
lastPeriodsStatsMaximumLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsMaximumLatency.setStatus(_A)
_LastPeriodsStatsAverageLatency_Type=Unsigned32
_LastPeriodsStatsAverageLatency_Object=MibTableColumn
lastPeriodsStatsAverageLatency=_LastPeriodsStatsAverageLatency_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,1200),_LastPeriodsStatsAverageLatency_Type())
lastPeriodsStatsAverageLatency.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsAverageLatency.setStatus(_A)
_LastPeriodsStatsPeriodBeginning_Type=OctetString
_LastPeriodsStatsPeriodBeginning_Object=MibTableColumn
lastPeriodsStatsPeriodBeginning=_LastPeriodsStatsPeriodBeginning_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,1300),_LastPeriodsStatsPeriodBeginning_Type())
lastPeriodsStatsPeriodBeginning.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPeriodBeginning.setStatus(_A)
_LastPeriodsStatsPeriodEnd_Type=OctetString
_LastPeriodsStatsPeriodEnd_Object=MibTableColumn
lastPeriodsStatsPeriodEnd=_LastPeriodsStatsPeriodEnd_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,200,1,1400),_LastPeriodsStatsPeriodEnd_Type())
lastPeriodsStatsPeriodEnd.setMaxAccess(_E)
if mibBuilder.loadTexts:lastPeriodsStatsPeriodEnd.setStatus(_A)
_ChannelStatisticsTable_Object=MibTable
channelStatisticsTable=_ChannelStatisticsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250))
if mibBuilder.loadTexts:channelStatisticsTable.setStatus(_A)
_ChannelStatisticsEntry_Object=MibTableRow
channelStatisticsEntry=_ChannelStatisticsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1))
channelStatisticsEntry.setIndexNames((0,_G,_z))
if mibBuilder.loadTexts:channelStatisticsEntry.setStatus(_A)
_ChannelStatisticsEpChannelId_Type=OctetString
_ChannelStatisticsEpChannelId_Object=MibTableColumn
channelStatisticsEpChannelId=_ChannelStatisticsEpChannelId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,100),_ChannelStatisticsEpChannelId_Type())
channelStatisticsEpChannelId.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsEpChannelId.setStatus(_A)
_ChannelStatisticsPacketsSent_Type=Unsigned32
_ChannelStatisticsPacketsSent_Object=MibTableColumn
channelStatisticsPacketsSent=_ChannelStatisticsPacketsSent_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,200),_ChannelStatisticsPacketsSent_Type())
channelStatisticsPacketsSent.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsPacketsSent.setStatus(_A)
_ChannelStatisticsPacketsReceived_Type=Unsigned32
_ChannelStatisticsPacketsReceived_Object=MibTableColumn
channelStatisticsPacketsReceived=_ChannelStatisticsPacketsReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,300),_ChannelStatisticsPacketsReceived_Type())
channelStatisticsPacketsReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsPacketsReceived.setStatus(_A)
_ChannelStatisticsBytesSent_Type=Unsigned32
_ChannelStatisticsBytesSent_Object=MibTableColumn
channelStatisticsBytesSent=_ChannelStatisticsBytesSent_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,400),_ChannelStatisticsBytesSent_Type())
channelStatisticsBytesSent.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsBytesSent.setStatus(_A)
_ChannelStatisticsBytesReceived_Type=Unsigned32
_ChannelStatisticsBytesReceived_Object=MibTableColumn
channelStatisticsBytesReceived=_ChannelStatisticsBytesReceived_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,500),_ChannelStatisticsBytesReceived_Type())
channelStatisticsBytesReceived.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsBytesReceived.setStatus(_A)
_ChannelStatisticsAverageReceiveInterarrivalJitter_Type=Unsigned32
_ChannelStatisticsAverageReceiveInterarrivalJitter_Object=MibTableColumn
channelStatisticsAverageReceiveInterarrivalJitter=_ChannelStatisticsAverageReceiveInterarrivalJitter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,600),_ChannelStatisticsAverageReceiveInterarrivalJitter_Type())
channelStatisticsAverageReceiveInterarrivalJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:channelStatisticsAverageReceiveInterarrivalJitter.setStatus(_A)
class _ChannelStatisticsReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('reset',10)))
_ChannelStatisticsReset_Type.__name__=_F
_ChannelStatisticsReset_Object=MibTableColumn
channelStatisticsReset=_ChannelStatisticsReset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,250,1,900),_ChannelStatisticsReset_Type())
channelStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:channelStatisticsReset.setStatus(_A)
class _StatsCollectionPeriodDuration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,44640))
_StatsCollectionPeriodDuration_Type.__name__=_C
_StatsCollectionPeriodDuration_Object=MibScalar
statsCollectionPeriodDuration=_StatsCollectionPeriodDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,300),_StatsCollectionPeriodDuration_Type())
statsCollectionPeriodDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:statsCollectionPeriodDuration.setStatus(_A)
class _StatsPerConnectionNotificationEnable_Type(MxEnableState):defaultValue=0
_StatsPerConnectionNotificationEnable_Type.__name__=_D
_StatsPerConnectionNotificationEnable_Object=MibScalar
statsPerConnectionNotificationEnable=_StatsPerConnectionNotificationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,400),_StatsPerConnectionNotificationEnable_Type())
statsPerConnectionNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:statsPerConnectionNotificationEnable.setStatus(_A)
class _StatsPerPeriodNotificationEnable_Type(MxEnableState):defaultValue=0
_StatsPerPeriodNotificationEnable_Type.__name__=_D
_StatsPerPeriodNotificationEnable_Object=MibScalar
statsPerPeriodNotificationEnable=_StatsPerPeriodNotificationEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,700,500),_StatsPerPeriodNotificationEnable_Type())
statsPerPeriodNotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:statsPerPeriodNotificationEnable.setStatus(_A)
_InteropGroup_ObjectIdentity=ObjectIdentity
interopGroup=_InteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,40000))
class _EnforceSymmetricRtpEnable_Type(MxEnableState):defaultValue=0
_EnforceSymmetricRtpEnable_Type.__name__=_D
_EnforceSymmetricRtpEnable_Object=MibScalar
enforceSymmetricRtpEnable=_EnforceSymmetricRtpEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,40000,100),_EnforceSymmetricRtpEnable_Type())
enforceSymmetricRtpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:enforceSymmetricRtpEnable.setStatus(_A)
class _InteropDtmfRtpInitialPacketQty_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_InteropDtmfRtpInitialPacketQty_Type.__name__=_C
_InteropDtmfRtpInitialPacketQty_Object=MibScalar
interopDtmfRtpInitialPacketQty=_InteropDtmfRtpInitialPacketQty_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,40000,200),_InteropDtmfRtpInitialPacketQty_Type())
interopDtmfRtpInitialPacketQty.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfRtpInitialPacketQty.setStatus(_A)
class _InteropPacketReceptionMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mode0',100),('mode1',200)))
_InteropPacketReceptionMode_Type.__name__=_F
_InteropPacketReceptionMode_Object=MibScalar
interopPacketReceptionMode=_InteropPacketReceptionMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,40000,300),_InteropPacketReceptionMode_Type())
interopPacketReceptionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:interopPacketReceptionMode.setStatus(_A)
_DebugGroup_ObjectIdentity=ObjectIdentity
debugGroup=_DebugGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000))
_PcmCaptureGroup_ObjectIdentity=ObjectIdentity
pcmCaptureGroup=_PcmCaptureGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,100))
class _PcmCaptureEnable_Type(MxEnableState):defaultValue=0
_PcmCaptureEnable_Type.__name__=_D
_PcmCaptureEnable_Object=MibScalar
pcmCaptureEnable=_PcmCaptureEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,100,100),_PcmCaptureEnable_Type())
pcmCaptureEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pcmCaptureEnable.setStatus(_A)
class _PcmCaptureEndpoint_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PcmCaptureEndpoint_Type.__name__=_I
_PcmCaptureEndpoint_Object=MibScalar
pcmCaptureEndpoint=_PcmCaptureEndpoint_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,100,200),_PcmCaptureEndpoint_Type())
pcmCaptureEndpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:pcmCaptureEndpoint.setStatus(_A)
class _PcmCaptureIpAddr_Type(MxIpAddress):defaultValue=OctetString('')
_PcmCaptureIpAddr_Type.__name__=_J
_PcmCaptureIpAddr_Object=MibScalar
pcmCaptureIpAddr=_PcmCaptureIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,100,300),_PcmCaptureIpAddr_Type())
pcmCaptureIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcmCaptureIpAddr.setStatus(_A)
_DspTracingGroup_ObjectIdentity=ObjectIdentity
dspTracingGroup=_DspTracingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,200))
class _DspTracingEnable_Type(MxEnableState):defaultValue=0
_DspTracingEnable_Type.__name__=_D
_DspTracingEnable_Object=MibScalar
dspTracingEnable=_DspTracingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,200,100),_DspTracingEnable_Type())
dspTracingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dspTracingEnable.setStatus(_A)
_DspStatsGroup_ObjectIdentity=ObjectIdentity
dspStatsGroup=_DspStatsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,300))
class _DspStatsEnable_Type(MxEnableState):defaultValue=0
_DspStatsEnable_Type.__name__=_D
_DspStatsEnable_Object=MibScalar
dspStatsEnable=_DspStatsEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,300,100),_DspStatsEnable_Type())
dspStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dspStatsEnable.setStatus(_A)
class _DspStatsInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DspStatsInterval_Type.__name__=_C
_DspStatsInterval_Object=MibScalar
dspStatsInterval=_DspStatsInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,300,200),_DspStatsInterval_Type())
dspStatsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:dspStatsInterval.setStatus(_A)
class _DspStatsFilter_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DspStatsFilter_Type.__name__=_C
_DspStatsFilter_Object=MibScalar
dspStatsFilter=_DspStatsFilter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,50000,300,300),_DspStatsFilter_Type())
dspStatsFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:dspStatsFilter.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_H,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_F
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_F
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1600,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'miptMIB':miptMIB,'miptMIBObjects':miptMIBObjects,'codecGroup':codecGroup,'defaultCodecGenericVoiceActivityDetection':defaultCodecGenericVoiceActivityDetection,'epSpecificCodecTable':epSpecificCodecTable,'epSpecificCodecEntry':epSpecificCodecEntry,_M:epSpecificCodecEpId,'epSpecificCodecEnableConfig':epSpecificCodecEnableConfig,'epSpecificCodecGenericVoiceActivityDetection':epSpecificCodecGenericVoiceActivityDetection,'codecG711Group':codecG711Group,'codecG711MulawGroup':codecG711MulawGroup,'defaultCodecG711MulawVoiceEnable':defaultCodecG711MulawVoiceEnable,'defaultCodecG711MulawVoicePriority':defaultCodecG711MulawVoicePriority,'defaultCodecG711MulawDataEnable':defaultCodecG711MulawDataEnable,'defaultCodecG711MulawDataPriority':defaultCodecG711MulawDataPriority,'defaultCodecG711MulawMinPTime':defaultCodecG711MulawMinPTime,'defaultCodecG711MulawMaxPTime':defaultCodecG711MulawMaxPTime,'epSpecificCodecG711MulawTable':epSpecificCodecG711MulawTable,'epSpecificCodecG711MulawEntry':epSpecificCodecG711MulawEntry,_N:epSpecificCodecG711MulawEpId,'epSpecificCodecG711MulawEnableConfig':epSpecificCodecG711MulawEnableConfig,'epSpecificCodecG711MulawVoiceEnable':epSpecificCodecG711MulawVoiceEnable,'epSpecificCodecG711MulawVoicePriority':epSpecificCodecG711MulawVoicePriority,'epSpecificCodecG711MulawDataEnable':epSpecificCodecG711MulawDataEnable,'epSpecificCodecG711MulawDataPriority':epSpecificCodecG711MulawDataPriority,'epSpecificCodecG711MulawMinPTime':epSpecificCodecG711MulawMinPTime,'epSpecificCodecG711MulawMaxPTime':epSpecificCodecG711MulawMaxPTime,'codecG711AlawGroup':codecG711AlawGroup,'defaultCodecG711AlawVoiceEnable':defaultCodecG711AlawVoiceEnable,'defaultCodecG711AlawVoicePriority':defaultCodecG711AlawVoicePriority,'defaultCodecG711AlawDataEnable':defaultCodecG711AlawDataEnable,'defaultCodecG711AlawDataPriority':defaultCodecG711AlawDataPriority,'defaultCodecG711AlawMinPTime':defaultCodecG711AlawMinPTime,'defaultCodecG711AlawMaxPTime':defaultCodecG711AlawMaxPTime,'epSpecificCodecG711AlawTable':epSpecificCodecG711AlawTable,'epSpecificCodecG711AlawEntry':epSpecificCodecG711AlawEntry,_O:epSpecificCodecG711AlawEpId,'epSpecificCodecG711AlawEnableConfig':epSpecificCodecG711AlawEnableConfig,'epSpecificCodecG711AlawVoiceEnable':epSpecificCodecG711AlawVoiceEnable,'epSpecificCodecG711AlawVoicePriority':epSpecificCodecG711AlawVoicePriority,'epSpecificCodecG711AlawDataEnable':epSpecificCodecG711AlawDataEnable,'epSpecificCodecG711AlawDataPriority':epSpecificCodecG711AlawDataPriority,'epSpecificCodecG711AlawMinPTime':epSpecificCodecG711AlawMinPTime,'epSpecificCodecG711AlawMaxPTime':epSpecificCodecG711AlawMaxPTime,'codecG722Group':codecG722Group,'defaultCodecG722VoiceEnable':defaultCodecG722VoiceEnable,'defaultCodecG722VoicePriority':defaultCodecG722VoicePriority,'defaultCodecG722MinPTime':defaultCodecG722MinPTime,'defaultCodecG722MaxPTime':defaultCodecG722MaxPTime,'epSpecificCodecG722Table':epSpecificCodecG722Table,'epSpecificCodecG722Entry':epSpecificCodecG722Entry,_P:epSpecificCodecG722EpId,'epSpecificCodecG722EnableConfig':epSpecificCodecG722EnableConfig,'epSpecificCodecG722VoiceEnable':epSpecificCodecG722VoiceEnable,'epSpecificCodecG722VoicePriority':epSpecificCodecG722VoicePriority,'epSpecificCodecG722MinPTime':epSpecificCodecG722MinPTime,'epSpecificCodecG722MaxPTime':epSpecificCodecG722MaxPTime,'codecG723Group':codecG723Group,'defaultCodecG723VoiceEnable':defaultCodecG723VoiceEnable,'defaultCodecG723VoicePriority':defaultCodecG723VoicePriority,'defaultCodecG723Bitrate':defaultCodecG723Bitrate,'defaultCodecG723MinPTime':defaultCodecG723MinPTime,'defaultCodecG723MaxPTime':defaultCodecG723MaxPTime,'epSpecificCodecG723Table':epSpecificCodecG723Table,'epSpecificCodecG723Entry':epSpecificCodecG723Entry,_S:epSpecificCodecG723EpId,'epSpecificCodecG723EnableConfig':epSpecificCodecG723EnableConfig,'epSpecificCodecG723VoiceEnable':epSpecificCodecG723VoiceEnable,'epSpecificCodecG723VoicePriority':epSpecificCodecG723VoicePriority,'epSpecificCodecG723Bitrate':epSpecificCodecG723Bitrate,'epSpecificCodecG723MinPTime':epSpecificCodecG723MinPTime,'epSpecificCodecG723MaxPTime':epSpecificCodecG723MaxPTime,'codecG726Group':codecG726Group,'codecG726r16kbpsGroup':codecG726r16kbpsGroup,'defaultCodecG726r16kbpsVoiceEnable':defaultCodecG726r16kbpsVoiceEnable,'defaultCodecG726r16kbpsVoicePriority':defaultCodecG726r16kbpsVoicePriority,'defaultCodecG726r16kbpsPayloadType':defaultCodecG726r16kbpsPayloadType,'defaultCodecG726r16kbpsMinPTime':defaultCodecG726r16kbpsMinPTime,'defaultCodecG726r16kbpsMaxPTime':defaultCodecG726r16kbpsMaxPTime,'epSpecificCodecG726r16kbpsTable':epSpecificCodecG726r16kbpsTable,'epSpecificCodecG726r16kbpsEntry':epSpecificCodecG726r16kbpsEntry,_T:epSpecificCodecG726r16kbpsEpId,'epSpecificCodecG726r16kbpsEnableConfig':epSpecificCodecG726r16kbpsEnableConfig,'epSpecificCodecG726r16kbpsVoiceEnable':epSpecificCodecG726r16kbpsVoiceEnable,'epSpecificCodecG726r16kbpsVoicePriority':epSpecificCodecG726r16kbpsVoicePriority,'epSpecificCodecG726r16kbpsPayloadType':epSpecificCodecG726r16kbpsPayloadType,'epSpecificCodecG726r16kbpsMinPTime':epSpecificCodecG726r16kbpsMinPTime,'epSpecificCodecG726r16kbpsMaxPTime':epSpecificCodecG726r16kbpsMaxPTime,'codecG726r24kbpsGroup':codecG726r24kbpsGroup,'defaultCodecG726r24kbpsVoiceEnable':defaultCodecG726r24kbpsVoiceEnable,'defaultCodecG726r24kbpsVoicePriority':defaultCodecG726r24kbpsVoicePriority,'defaultCodecG726r24kbpsPayloadType':defaultCodecG726r24kbpsPayloadType,'defaultCodecG726r24kbpsMinPTime':defaultCodecG726r24kbpsMinPTime,'defaultCodecG726r24kbpsMaxPTime':defaultCodecG726r24kbpsMaxPTime,'epSpecificCodecG726r24kbpsTable':epSpecificCodecG726r24kbpsTable,'epSpecificCodecG726r24kbpsEntry':epSpecificCodecG726r24kbpsEntry,_U:epSpecificCodecG726r24kbpsEpId,'epSpecificCodecG726r24kbpsEnableConfig':epSpecificCodecG726r24kbpsEnableConfig,'epSpecificCodecG726r24kbpsVoiceEnable':epSpecificCodecG726r24kbpsVoiceEnable,'epSpecificCodecG726r24kbpsVoicePriority':epSpecificCodecG726r24kbpsVoicePriority,'epSpecificCodecG726r24kbpsPayloadType':epSpecificCodecG726r24kbpsPayloadType,'epSpecificCodecG726r24kbpsMinPTime':epSpecificCodecG726r24kbpsMinPTime,'epSpecificCodecG726r24kbpsMaxPTime':epSpecificCodecG726r24kbpsMaxPTime,'codecG726r32kbpsGroup':codecG726r32kbpsGroup,'defaultCodecG726r32kbpsVoiceEnable':defaultCodecG726r32kbpsVoiceEnable,'defaultCodecG726r32kbpsVoicePriority':defaultCodecG726r32kbpsVoicePriority,'defaultCodecG726r32kbpsDataEnable':defaultCodecG726r32kbpsDataEnable,'defaultCodecG726r32kbpsDataPriority':defaultCodecG726r32kbpsDataPriority,'defaultCodecG726r32kbpsPayloadType':defaultCodecG726r32kbpsPayloadType,'defaultCodecG726r32kbpsMinPTime':defaultCodecG726r32kbpsMinPTime,'defaultCodecG726r32kbpsMaxPTime':defaultCodecG726r32kbpsMaxPTime,'epSpecificCodecG726r32kbpsTable':epSpecificCodecG726r32kbpsTable,'epSpecificCodecG726r32kbpsEntry':epSpecificCodecG726r32kbpsEntry,_V:epSpecificCodecG726r32kbpsEpId,'epSpecificCodecG726r32kbpsEnableConfig':epSpecificCodecG726r32kbpsEnableConfig,'epSpecificCodecG726r32kbpsVoiceEnable':epSpecificCodecG726r32kbpsVoiceEnable,'epSpecificCodecG726r32kbpsVoicePriority':epSpecificCodecG726r32kbpsVoicePriority,'epSpecificCodecG726r32kbpsDataEnable':epSpecificCodecG726r32kbpsDataEnable,'epSpecificCodecG726r32kbpsDataPriority':epSpecificCodecG726r32kbpsDataPriority,'epSpecificCodecG726r32kbpsPayloadType':epSpecificCodecG726r32kbpsPayloadType,'epSpecificCodecG726r32kbpsMinPTime':epSpecificCodecG726r32kbpsMinPTime,'epSpecificCodecG726r32kbpsMaxPTime':epSpecificCodecG726r32kbpsMaxPTime,'codecG726r40kbpsGroup':codecG726r40kbpsGroup,'defaultCodecG726r40kbpsVoiceEnable':defaultCodecG726r40kbpsVoiceEnable,'defaultCodecG726r40kbpsVoicePriority':defaultCodecG726r40kbpsVoicePriority,'defaultCodecG726r40kbpsDataEnable':defaultCodecG726r40kbpsDataEnable,'defaultCodecG726r40kbpsDataPriority':defaultCodecG726r40kbpsDataPriority,'defaultCodecG726r40kbpsPayloadType':defaultCodecG726r40kbpsPayloadType,'defaultCodecG726r40kbpsMinPTime':defaultCodecG726r40kbpsMinPTime,'defaultCodecG726r40kbpsMaxPTime':defaultCodecG726r40kbpsMaxPTime,'epSpecificCodecG726r40kbpsTable':epSpecificCodecG726r40kbpsTable,'epSpecificCodecG726r40kbpsEntry':epSpecificCodecG726r40kbpsEntry,_W:epSpecificCodecG726r40kbpsEpId,'epSpecificCodecG726r40kbpsEnableConfig':epSpecificCodecG726r40kbpsEnableConfig,'epSpecificCodecG726r40kbpsVoiceEnable':epSpecificCodecG726r40kbpsVoiceEnable,'epSpecificCodecG726r40kbpsVoicePriority':epSpecificCodecG726r40kbpsVoicePriority,'epSpecificCodecG726r40kbpsDataEnable':epSpecificCodecG726r40kbpsDataEnable,'epSpecificCodecG726r40kbpsDataPriority':epSpecificCodecG726r40kbpsDataPriority,'epSpecificCodecG726r40kbpsPayloadType':epSpecificCodecG726r40kbpsPayloadType,'epSpecificCodecG726r40kbpsMinPTime':epSpecificCodecG726r40kbpsMinPTime,'epSpecificCodecG726r40kbpsMaxPTime':epSpecificCodecG726r40kbpsMaxPTime,'codecG729Group':codecG729Group,'defaultCodecG729VoiceEnable':defaultCodecG729VoiceEnable,'defaultCodecG729VoicePriority':defaultCodecG729VoicePriority,'defaultCodecG729MinPTime':defaultCodecG729MinPTime,'defaultCodecG729MaxPTime':defaultCodecG729MaxPTime,'defaultCodecG729VoiceActivityDetection':defaultCodecG729VoiceActivityDetection,'epSpecificCodecG729Table':epSpecificCodecG729Table,'epSpecificCodecG729Entry':epSpecificCodecG729Entry,_X:epSpecificCodecG729EpId,'epSpecificCodecG729EnableConfig':epSpecificCodecG729EnableConfig,'epSpecificCodecG729VoiceEnable':epSpecificCodecG729VoiceEnable,'epSpecificCodecG729VoicePriority':epSpecificCodecG729VoicePriority,'epSpecificCodecG729MinPTime':epSpecificCodecG729MinPTime,'epSpecificCodecG729MaxPTime':epSpecificCodecG729MaxPTime,'epSpecificCodecG729VoiceActivityDetection':epSpecificCodecG729VoiceActivityDetection,'codecT38Group':codecT38Group,'defaultCodecT38DataEnable':defaultCodecT38DataEnable,'defaultCodecT38DataPriority':defaultCodecT38DataPriority,'defaultCodecT38RedundancyLevel':defaultCodecT38RedundancyLevel,'defaultCodecT38FinalFramesRedundancy':defaultCodecT38FinalFramesRedundancy,'defaultCodecT38NoSignalEnable':defaultCodecT38NoSignalEnable,'defaultCodecT38NoSignalTimeout':defaultCodecT38NoSignalTimeout,'defaultCodecT38DetectionThreshold':defaultCodecT38DetectionThreshold,'epSpecificCodecT38Table':epSpecificCodecT38Table,'epSpecificCodecT38Entry':epSpecificCodecT38Entry,_a:epSpecificCodecT38EpId,'epSpecificCodecT38EnableConfig':epSpecificCodecT38EnableConfig,'epSpecificCodecT38DataEnable':epSpecificCodecT38DataEnable,'epSpecificCodecT38DataPriority':epSpecificCodecT38DataPriority,'epSpecificCodecT38RedundancyLevel':epSpecificCodecT38RedundancyLevel,'epSpecificCodecT38DetectionThreshold':epSpecificCodecT38DetectionThreshold,'codecClearModeGroup':codecClearModeGroup,'defaultCodecClearModeVoiceEnable':defaultCodecClearModeVoiceEnable,'defaultCodecClearModeVoicePriority':defaultCodecClearModeVoicePriority,'defaultCodecClearModeDataEnable':defaultCodecClearModeDataEnable,'defaultCodecClearModeDataPriority':defaultCodecClearModeDataPriority,'defaultCodecClearModePayloadType':defaultCodecClearModePayloadType,'defaultCodecClearModeMinPTime':defaultCodecClearModeMinPTime,'defaultCodecClearModeMaxPTime':defaultCodecClearModeMaxPTime,'epSpecificCodecClearModeTable':epSpecificCodecClearModeTable,'epSpecificCodecClearModeEntry':epSpecificCodecClearModeEntry,_b:epSpecificCodecClearModeEpId,'epSpecificCodecClearModeEnableConfig':epSpecificCodecClearModeEnableConfig,'epSpecificCodecClearModeVoiceEnable':epSpecificCodecClearModeVoiceEnable,'epSpecificCodecClearModeVoicePriority':epSpecificCodecClearModeVoicePriority,'epSpecificCodecClearModeDataEnable':epSpecificCodecClearModeDataEnable,'epSpecificCodecClearModeDataPriority':epSpecificCodecClearModeDataPriority,'epSpecificCodecClearModePayloadType':epSpecificCodecClearModePayloadType,'epSpecificCodecClearModeMinPTime':epSpecificCodecClearModeMinPTime,'epSpecificCodecClearModeMaxPTime':epSpecificCodecClearModeMaxPTime,'codecClearChannelGroup':codecClearChannelGroup,'defaultCodecClearChannelVoiceEnable':defaultCodecClearChannelVoiceEnable,'defaultCodecClearChannelVoicePriority':defaultCodecClearChannelVoicePriority,'defaultCodecClearChannelDataEnable':defaultCodecClearChannelDataEnable,'defaultCodecClearChannelDataPriority':defaultCodecClearChannelDataPriority,'defaultCodecClearChannelPayloadType':defaultCodecClearChannelPayloadType,'defaultCodecClearChannelMinPTime':defaultCodecClearChannelMinPTime,'defaultCodecClearChannelMaxPTime':defaultCodecClearChannelMaxPTime,'epSpecificCodecClearChannelTable':epSpecificCodecClearChannelTable,'epSpecificCodecClearChannelEntry':epSpecificCodecClearChannelEntry,_c:epSpecificCodecClearChannelEpId,'epSpecificCodecClearChannelEnableConfig':epSpecificCodecClearChannelEnableConfig,'epSpecificCodecClearChannelVoiceEnable':epSpecificCodecClearChannelVoiceEnable,'epSpecificCodecClearChannelVoicePriority':epSpecificCodecClearChannelVoicePriority,'epSpecificCodecClearChannelDataEnable':epSpecificCodecClearChannelDataEnable,'epSpecificCodecClearChannelDataPriority':epSpecificCodecClearChannelDataPriority,'epSpecificCodecClearChannelPayloadType':epSpecificCodecClearChannelPayloadType,'epSpecificCodecClearChannelMinPTime':epSpecificCodecClearChannelMinPTime,'epSpecificCodecClearChannelMaxPTime':epSpecificCodecClearChannelMaxPTime,'codecXCCDGroup':codecXCCDGroup,'defaultCodecXCCDVoiceEnable':defaultCodecXCCDVoiceEnable,'defaultCodecXCCDVoicePriority':defaultCodecXCCDVoicePriority,'defaultCodecXCCDDataEnable':defaultCodecXCCDDataEnable,'defaultCodecXCCDDataPriority':defaultCodecXCCDDataPriority,'defaultCodecXCCDPayloadType':defaultCodecXCCDPayloadType,'defaultCodecXCCDMinPTime':defaultCodecXCCDMinPTime,'defaultCodecXCCDMaxPTime':defaultCodecXCCDMaxPTime,'epSpecificCodecXCCDTable':epSpecificCodecXCCDTable,'epSpecificCodecXCCDEntry':epSpecificCodecXCCDEntry,_d:epSpecificCodecXCCDEpId,'epSpecificCodecXCCDEnableConfig':epSpecificCodecXCCDEnableConfig,'epSpecificCodecXCCDVoiceEnable':epSpecificCodecXCCDVoiceEnable,'epSpecificCodecXCCDVoicePriority':epSpecificCodecXCCDVoicePriority,'epSpecificCodecXCCDDataEnable':epSpecificCodecXCCDDataEnable,'epSpecificCodecXCCDDataPriority':epSpecificCodecXCCDDataPriority,'epSpecificCodecXCCDPayloadType':epSpecificCodecXCCDPayloadType,'epSpecificCodecXCCDMinPTime':epSpecificCodecXCCDMinPTime,'epSpecificCodecXCCDMaxPTime':epSpecificCodecXCCDMaxPTime,'jitterBufferGroup':jitterBufferGroup,'defaultJitterBufferLevel':defaultJitterBufferLevel,'defaultJitterBufferCustomMinLength':defaultJitterBufferCustomMinLength,'defaultJitterBufferCustomNomLength':defaultJitterBufferCustomNomLength,'defaultJitterBufferCustomMaxLength':defaultJitterBufferCustomMaxLength,'defaultVbdJitterBufferCustomMinLength':defaultVbdJitterBufferCustomMinLength,'defaultVbdJitterBufferCustomNomLength':defaultVbdJitterBufferCustomNomLength,'defaultVbdJitterBufferCustomMaxLength':defaultVbdJitterBufferCustomMaxLength,'defaultVbdJitterBufferType':defaultVbdJitterBufferType,'epSpecificJitterBufferTable':epSpecificJitterBufferTable,'epSpecificJitterBufferEntry':epSpecificJitterBufferEntry,_l:epSpecificJitterBufferEpId,'epSpecificJitterBufferEnableConfig':epSpecificJitterBufferEnableConfig,'epSpecificJitterBufferLevel':epSpecificJitterBufferLevel,'epSpecificJitterBufferCustomMinLength':epSpecificJitterBufferCustomMinLength,'epSpecificJitterBufferCustomNomLength':epSpecificJitterBufferCustomNomLength,'epSpecificJitterBufferCustomMaxLength':epSpecificJitterBufferCustomMaxLength,'epSpecificJitterBufferCustomVbdMinLength':epSpecificJitterBufferCustomVbdMinLength,'epSpecificJitterBufferCustomVbdNomLength':epSpecificJitterBufferCustomVbdNomLength,'epSpecificJitterBufferCustomVbdMaxLength':epSpecificJitterBufferCustomVbdMaxLength,'epSpecificJitterBufferCustomVbdJitterBufferType':epSpecificJitterBufferCustomVbdJitterBufferType,'dtmfTransportGroup':dtmfTransportGroup,'defaultDtmfTransportMethod':defaultDtmfTransportMethod,'defaultDtmfTransportPayloadType':defaultDtmfTransportPayloadType,'epSpecificDtmfTransportTable':epSpecificDtmfTransportTable,'epSpecificDtmfTransportEntry':epSpecificDtmfTransportEntry,_q:epSpecificDtmfTransportEpId,'epSpecificDtmfTransportEnableConfig':epSpecificDtmfTransportEnableConfig,'epSpecificDtmfTransportMethod':epSpecificDtmfTransportMethod,'epSpecificDtmfTransportPayloadType':epSpecificDtmfTransportPayloadType,'ipTransportGroup':ipTransportGroup,'ipTransportRtpGroup':ipTransportRtpGroup,'ipTransportRtpBasePort':ipTransportRtpBasePort,'ipTransportSrtpBasePort':ipTransportSrtpBasePort,'ipTransportT38Group':ipTransportT38Group,'ipTransportT38BasePort':ipTransportT38BasePort,'codecVsBearerCapabilitiesMapping':codecVsBearerCapabilitiesMapping,'defaultCodecVsBearerCapabilitiesMappingTable':defaultCodecVsBearerCapabilitiesMappingTable,'defaultCodecVsBearerCapabilitiesMappingEntry':defaultCodecVsBearerCapabilitiesMappingEntry,_r:defaultCodecVsBearerCapabilitiesMappingIndex,'defaultCodecVsBearerCapabilitiesMappingEnableMap':defaultCodecVsBearerCapabilitiesMappingEnableMap,'defaultCodecVsBearerCapabilitiesMappingCodec':defaultCodecVsBearerCapabilitiesMappingCodec,'defaultCodecVsBearerCapabilitiesMappingInformationTransferCap':defaultCodecVsBearerCapabilitiesMappingInformationTransferCap,'defaultCodecVsBearerCapabilitiesMappingMappingType':defaultCodecVsBearerCapabilitiesMappingMappingType,'securityGroup':securityGroup,'defaultSecurityRtpMode':defaultSecurityRtpMode,'defaultSecurityKeyManagement':defaultSecurityKeyManagement,'defaultSecurityRtpEncryption':defaultSecurityRtpEncryption,'allowUnsecureT38WithSrtp':allowUnsecureT38WithSrtp,'sessionUpdateCryptoMode':sessionUpdateCryptoMode,'epSpecificSecurityTable':epSpecificSecurityTable,'epSpecificSecurityEntry':epSpecificSecurityEntry,_w:epSpecificSecurityEpId,'epSpecificSecurityEnableConfig':epSpecificSecurityEnableConfig,'epSpecificSecurityRtpMode':epSpecificSecurityRtpMode,'epSpecificSecurityKeyManagement':epSpecificSecurityKeyManagement,'epSpecificSecurityRtpEncryption':epSpecificSecurityRtpEncryption,'statisticsGroup':statisticsGroup,'lastConnectionsStatsTable':lastConnectionsStatsTable,'lastConnectionsStatsEntry':lastConnectionsStatsEntry,_x:lastConnectionsStatsConnectionsIndex,'lastConnectionsStatsOctetsTransmitted':lastConnectionsStatsOctetsTransmitted,'lastConnectionsStatsOctetsReceived':lastConnectionsStatsOctetsReceived,'lastConnectionsStatsPacketsTransmitted':lastConnectionsStatsPacketsTransmitted,'lastConnectionsStatsPacketsReceived':lastConnectionsStatsPacketsReceived,'lastConnectionsStatsPacketsLost':lastConnectionsStatsPacketsLost,'lastConnectionsStatsMinimumInterarrivalJitter':lastConnectionsStatsMinimumInterarrivalJitter,'lastConnectionsStatsMaximumInterarrivalJitter':lastConnectionsStatsMaximumInterarrivalJitter,'lastConnectionsStatsAverageInterarrivalJitter':lastConnectionsStatsAverageInterarrivalJitter,'lastConnectionsStatsMinimumLatency':lastConnectionsStatsMinimumLatency,'lastConnectionsStatsMaximumLatency':lastConnectionsStatsMaximumLatency,'lastConnectionsStatsAverageLatency':lastConnectionsStatsAverageLatency,'lastPeriodsStatsTable':lastPeriodsStatsTable,'lastPeriodsStatsEntry':lastPeriodsStatsEntry,_y:lastPeriodsStatsPeriodIndex,'lastPeriodsStatsOctetsTransmitted':lastPeriodsStatsOctetsTransmitted,'lastPeriodsStatsOctetsReceived':lastPeriodsStatsOctetsReceived,'lastPeriodsStatsPacketsTransmitted':lastPeriodsStatsPacketsTransmitted,'lastPeriodsStatsPacketsReceived':lastPeriodsStatsPacketsReceived,'lastPeriodsStatsPacketsLost':lastPeriodsStatsPacketsLost,'lastPeriodsStatsMinimumInterarrivalJitter':lastPeriodsStatsMinimumInterarrivalJitter,'lastPeriodsStatsMaximumInterarrivalJitter':lastPeriodsStatsMaximumInterarrivalJitter,'lastPeriodsStatsAverageInterarrivalJitter':lastPeriodsStatsAverageInterarrivalJitter,'lastPeriodsStatsMinimumLatency':lastPeriodsStatsMinimumLatency,'lastPeriodsStatsMaximumLatency':lastPeriodsStatsMaximumLatency,'lastPeriodsStatsAverageLatency':lastPeriodsStatsAverageLatency,'lastPeriodsStatsPeriodBeginning':lastPeriodsStatsPeriodBeginning,'lastPeriodsStatsPeriodEnd':lastPeriodsStatsPeriodEnd,'channelStatisticsTable':channelStatisticsTable,'channelStatisticsEntry':channelStatisticsEntry,_z:channelStatisticsEpChannelId,'channelStatisticsPacketsSent':channelStatisticsPacketsSent,'channelStatisticsPacketsReceived':channelStatisticsPacketsReceived,'channelStatisticsBytesSent':channelStatisticsBytesSent,'channelStatisticsBytesReceived':channelStatisticsBytesReceived,'channelStatisticsAverageReceiveInterarrivalJitter':channelStatisticsAverageReceiveInterarrivalJitter,'channelStatisticsReset':channelStatisticsReset,'statsCollectionPeriodDuration':statsCollectionPeriodDuration,'statsPerConnectionNotificationEnable':statsPerConnectionNotificationEnable,'statsPerPeriodNotificationEnable':statsPerPeriodNotificationEnable,'interopGroup':interopGroup,'enforceSymmetricRtpEnable':enforceSymmetricRtpEnable,'interopDtmfRtpInitialPacketQty':interopDtmfRtpInitialPacketQty,'interopPacketReceptionMode':interopPacketReceptionMode,'debugGroup':debugGroup,'pcmCaptureGroup':pcmCaptureGroup,'pcmCaptureEnable':pcmCaptureEnable,'pcmCaptureEndpoint':pcmCaptureEndpoint,'pcmCaptureIpAddr':pcmCaptureIpAddr,'dspTracingGroup':dspTracingGroup,'dspTracingEnable':dspTracingEnable,'dspStatsGroup':dspStatsGroup,'dspStatsEnable':dspStatsEnable,'dspStatsInterval':dspStatsInterval,'dspStatsFilter':dspStatsFilter,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})