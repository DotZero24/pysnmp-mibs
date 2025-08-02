_AV='ciscoGslbGeneralConfigRateLimitGroup'
_AU='ciscoGslbKalNotificationGroup'
_AT='ciscoGslbKalNotifObjectsGroup'
_AS='ciscoGslbKalNotifControlGroup'
_AR='ciscoGslbKalStatsGroup'
_AQ='ciscoGslbKalConfigGroup'
_AP='ciscoGslbKalParameterGroup'
_AO='ciscoGslbGeneralConfigGroup'
_AN='ciscoGslbKalEventStatus'
_AM='cghMonKalNotifEnable'
_AL='cghMonKalVIPFailovers'
_AK='cghMonKalDynamicLoad'
_AJ='cghMonKalStatusTransitions'
_AI='cghMonKalNegativeProbes'
_AH='cghMonKalPositiveProbes'
_AG='cghMonKalReceivedProbes'
_AF='cghMonKalSentProbes'
_AE='cghMonKalShAnsRowStatus'
_AD='cghMonKalShAnsStoragetype'
_AC='cghMonKalRowStatus'
_AB='cghMonKalStorageType'
_AA='cghMonKalFastSuccessfulProbes'
_A9='cghMonKalFastRetries'
_A8='cghMonKalSecondaryTarget'
_A7='cghMonKalSecondaryTargetType'
_A6='cghMonKalHostTag'
_A5='cghMonKalPath'
_A4='cghMonKalQueryDomainName'
_A3='cghMonKalCappHash'
_A2='cghMonKalCappSecure'
_A1='cghMonKalDestPort'
_A0='cghMonKalTagName'
_z='cghMonKalKalapType'
_y='cghMonKalDelay'
_x='cghMonKalEnable'
_w='cghMonKalAnswerId'
_v='cghMonKalTargetType'
_u='cghMonKalParameterRowStatus'
_t='cghMonKalParameterStorageType'
_s='cghMonKalParameterDestPort'
_r='cghMonKalParameterFastSuccessfulProbes'
_q='cghMonKalParameterFastRetries'
_p='cghMonKalParameterResponseTimeout'
_o='cghMonKalParameterMinimumFrequency'
_n='cghMonKalParameterRate'
_m='cghMonTotalConfiguredProbes'
_l='cghMonTcpConnTermMethod'
_k='cghMonCraDecay'
_j='cghMonHttpHeadConnTermMethod'
_i='cghMonHttpHeadPath'
_h='cghMonCappHash'
_g='cghMonNsQueryDomainName'
_f='cghMonKalStatsEntry'
_e='retries'
_d='seconds'
_c='not-accessible'
_b='cghMonKalParameterMethod'
_a='sysName'
_Z='SNMPv2-MIB'
_Y='CiscoGslbKalapType'
_X='cgdAnswerId'
_W='CISCO-GSLB-DNS-MIB'
_V='cghMonKalPrevStatus'
_U='cghMonKalStatus'
_T='cghMonKalPrimaryTarget'
_S='cghMonKalPrimaryTargetType'
_R='cghMonKalMethod'
_Q='cghMonKalTrapRateLimit'
_P='cghMonKalId'
_O='InetPortNumber'
_N='InetAddressType'
_M='InetAddress'
_L='CiscoGslbTerminationMethod'
_K='cghMonDroppedKalNotifs'
_J='TruthValue'
_I='StorageType'
_H='probes'
_G='SnmpAdminString'
_F='read-write'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='current'
_A='CISCO-GSLB-HEALTH-MON-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cgdAnswerId,=mibBuilder.importSymbols(_W,_X)
CiscoGslbKalapType,CiscoGslbKeepaliveMethod,CiscoGslbKeepaliveRate,CiscoGslbKeepaliveStatus,CiscoGslbKeepaliveTargetType,CiscoGslbTerminationMethod=mibBuilder.importSymbols('CISCO-GSLB-TC-MIB',_Y,'CiscoGslbKeepaliveMethod','CiscoGslbKeepaliveRate','CiscoGslbKeepaliveStatus','CiscoGslbKeepaliveTargetType',_L)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_M,_N,_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_Z,_a)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention',_J)
ciscoGslbHealthMonMIB=ModuleIdentity((1,3,6,1,4,1,9,9,600))
if mibBuilder.loadTexts:ciscoGslbHealthMonMIB.setRevisions(('2007-04-09 00:00','2006-12-04 00:00'))
_CiscoGslbHealthMonMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoGslbHealthMonMIBNotifs=_CiscoGslbHealthMonMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,600,0))
_CiscoGslbHealthMonMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGslbHealthMonMIBObjects=_CiscoGslbHealthMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,600,1))
_CghMonNotifControl_ObjectIdentity=ObjectIdentity
cghMonNotifControl=_CghMonNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,600,1,1))
class _CghMonKalNotifEnable_Type(TruthValue):defaultValue=2
_CghMonKalNotifEnable_Type.__name__=_J
_CghMonKalNotifEnable_Object=MibScalar
cghMonKalNotifEnable=_CghMonKalNotifEnable_Object((1,3,6,1,4,1,9,9,600,1,1,1),_CghMonKalNotifEnable_Type())
cghMonKalNotifEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonKalNotifEnable.setStatus(_B)
_CghMonNotifObjects_ObjectIdentity=ObjectIdentity
cghMonNotifObjects=_CghMonNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,600,1,2))
_CghMonKalPrevStatus_Type=CiscoGslbKeepaliveStatus
_CghMonKalPrevStatus_Object=MibScalar
cghMonKalPrevStatus=_CghMonKalPrevStatus_Object((1,3,6,1,4,1,9,9,600,1,2,1),_CghMonKalPrevStatus_Type())
cghMonKalPrevStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cghMonKalPrevStatus.setStatus(_B)
_CghMonKalGeneralConfig_ObjectIdentity=ObjectIdentity
cghMonKalGeneralConfig=_CghMonKalGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,9,600,1,3))
class _CghMonNsQueryDomainName_Type(SnmpAdminString):defaultValue=OctetString('.')
_CghMonNsQueryDomainName_Type.__name__=_G
_CghMonNsQueryDomainName_Object=MibScalar
cghMonNsQueryDomainName=_CghMonNsQueryDomainName_Object((1,3,6,1,4,1,9,9,600,1,3,1),_CghMonNsQueryDomainName_Type())
cghMonNsQueryDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonNsQueryDomainName.setStatus(_B)
class _CghMonCappHash_Type(SnmpAdminString):defaultValue=OctetString('hash-not-set')
_CghMonCappHash_Type.__name__=_G
_CghMonCappHash_Object=MibScalar
cghMonCappHash=_CghMonCappHash_Object((1,3,6,1,4,1,9,9,600,1,3,2),_CghMonCappHash_Type())
cghMonCappHash.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonCappHash.setStatus(_B)
class _CghMonHttpHeadPath_Type(SnmpAdminString):defaultValue=OctetString('/')
_CghMonHttpHeadPath_Type.__name__=_G
_CghMonHttpHeadPath_Object=MibScalar
cghMonHttpHeadPath=_CghMonHttpHeadPath_Object((1,3,6,1,4,1,9,9,600,1,3,3),_CghMonHttpHeadPath_Type())
cghMonHttpHeadPath.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonHttpHeadPath.setStatus(_B)
class _CghMonHttpHeadConnTermMethod_Type(CiscoGslbTerminationMethod):defaultValue=2
_CghMonHttpHeadConnTermMethod_Type.__name__=_L
_CghMonHttpHeadConnTermMethod_Object=MibScalar
cghMonHttpHeadConnTermMethod=_CghMonHttpHeadConnTermMethod_Object((1,3,6,1,4,1,9,9,600,1,3,4),_CghMonHttpHeadConnTermMethod_Type())
cghMonHttpHeadConnTermMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonHttpHeadConnTermMethod.setStatus(_B)
class _CghMonTcpConnTermMethod_Type(CiscoGslbTerminationMethod):defaultValue=2
_CghMonTcpConnTermMethod_Type.__name__=_L
_CghMonTcpConnTermMethod_Object=MibScalar
cghMonTcpConnTermMethod=_CghMonTcpConnTermMethod_Object((1,3,6,1,4,1,9,9,600,1,3,5),_CghMonTcpConnTermMethod_Type())
cghMonTcpConnTermMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonTcpConnTermMethod.setStatus(_B)
class _CghMonCraDecay_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonCraDecay_Type.__name__=_E
_CghMonCraDecay_Object=MibScalar
cghMonCraDecay=_CghMonCraDecay_Object((1,3,6,1,4,1,9,9,600,1,3,6),_CghMonCraDecay_Type())
cghMonCraDecay.setMaxAccess(_F)
if mibBuilder.loadTexts:cghMonCraDecay.setStatus(_B)
_CghMonTotalConfiguredProbes_Type=Unsigned32
_CghMonTotalConfiguredProbes_Object=MibScalar
cghMonTotalConfiguredProbes=_CghMonTotalConfiguredProbes_Object((1,3,6,1,4,1,9,9,600,1,3,7),_CghMonTotalConfiguredProbes_Type())
cghMonTotalConfiguredProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonTotalConfiguredProbes.setStatus(_B)
_CghMonDroppedKalNotifs_Type=Unsigned32
_CghMonDroppedKalNotifs_Object=MibScalar
cghMonDroppedKalNotifs=_CghMonDroppedKalNotifs_Object((1,3,6,1,4,1,9,9,600,1,3,8),_CghMonDroppedKalNotifs_Type())
cghMonDroppedKalNotifs.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonDroppedKalNotifs.setStatus(_B)
if mibBuilder.loadTexts:cghMonDroppedKalNotifs.setUnits('traps')
class _CghMonKalTrapRateLimit_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalTrapRateLimit_Type.__name__=_E
_CghMonKalTrapRateLimit_Object=MibScalar
cghMonKalTrapRateLimit=_CghMonKalTrapRateLimit_Object((1,3,6,1,4,1,9,9,600,1,3,9),_CghMonKalTrapRateLimit_Type())
cghMonKalTrapRateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalTrapRateLimit.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalTrapRateLimit.setUnits('traps per minute')
_CghMonKalParameterTable_Object=MibTable
cghMonKalParameterTable=_CghMonKalParameterTable_Object((1,3,6,1,4,1,9,9,600,1,3,10))
if mibBuilder.loadTexts:cghMonKalParameterTable.setStatus(_B)
_CghMonKalParameterEntry_Object=MibTableRow
cghMonKalParameterEntry=_CghMonKalParameterEntry_Object((1,3,6,1,4,1,9,9,600,1,3,10,1))
cghMonKalParameterEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:cghMonKalParameterEntry.setStatus(_B)
_CghMonKalParameterMethod_Type=CiscoGslbKeepaliveMethod
_CghMonKalParameterMethod_Object=MibTableColumn
cghMonKalParameterMethod=_CghMonKalParameterMethod_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,1),_CghMonKalParameterMethod_Type())
cghMonKalParameterMethod.setMaxAccess(_c)
if mibBuilder.loadTexts:cghMonKalParameterMethod.setStatus(_B)
_CghMonKalParameterRate_Type=CiscoGslbKeepaliveRate
_CghMonKalParameterRate_Object=MibTableColumn
cghMonKalParameterRate=_CghMonKalParameterRate_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,2),_CghMonKalParameterRate_Type())
cghMonKalParameterRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterRate.setStatus(_B)
class _CghMonKalParameterMinimumFrequency_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalParameterMinimumFrequency_Type.__name__=_E
_CghMonKalParameterMinimumFrequency_Object=MibTableColumn
cghMonKalParameterMinimumFrequency=_CghMonKalParameterMinimumFrequency_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,3),_CghMonKalParameterMinimumFrequency_Type())
cghMonKalParameterMinimumFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterMinimumFrequency.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalParameterMinimumFrequency.setUnits(_d)
class _CghMonKalParameterResponseTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalParameterResponseTimeout_Type.__name__=_E
_CghMonKalParameterResponseTimeout_Object=MibTableColumn
cghMonKalParameterResponseTimeout=_CghMonKalParameterResponseTimeout_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,4),_CghMonKalParameterResponseTimeout_Type())
cghMonKalParameterResponseTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterResponseTimeout.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalParameterResponseTimeout.setUnits(_d)
class _CghMonKalParameterFastRetries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalParameterFastRetries_Type.__name__=_E
_CghMonKalParameterFastRetries_Object=MibTableColumn
cghMonKalParameterFastRetries=_CghMonKalParameterFastRetries_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,5),_CghMonKalParameterFastRetries_Type())
cghMonKalParameterFastRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterFastRetries.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalParameterFastRetries.setUnits(_e)
class _CghMonKalParameterFastSuccessfulProbes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalParameterFastSuccessfulProbes_Type.__name__=_E
_CghMonKalParameterFastSuccessfulProbes_Object=MibTableColumn
cghMonKalParameterFastSuccessfulProbes=_CghMonKalParameterFastSuccessfulProbes_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,6),_CghMonKalParameterFastSuccessfulProbes_Type())
cghMonKalParameterFastSuccessfulProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterFastSuccessfulProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalParameterFastSuccessfulProbes.setUnits(_H)
class _CghMonKalParameterDestPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalParameterDestPort_Type.__name__=_O
_CghMonKalParameterDestPort_Object=MibTableColumn
cghMonKalParameterDestPort=_CghMonKalParameterDestPort_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,7),_CghMonKalParameterDestPort_Type())
cghMonKalParameterDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterDestPort.setStatus(_B)
class _CghMonKalParameterStorageType_Type(StorageType):defaultValue=3
_CghMonKalParameterStorageType_Type.__name__=_I
_CghMonKalParameterStorageType_Object=MibTableColumn
cghMonKalParameterStorageType=_CghMonKalParameterStorageType_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,8),_CghMonKalParameterStorageType_Type())
cghMonKalParameterStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterStorageType.setStatus(_B)
_CghMonKalParameterRowStatus_Type=RowStatus
_CghMonKalParameterRowStatus_Object=MibTableColumn
cghMonKalParameterRowStatus=_CghMonKalParameterRowStatus_Object((1,3,6,1,4,1,9,9,600,1,3,10,1,9),_CghMonKalParameterRowStatus_Type())
cghMonKalParameterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalParameterRowStatus.setStatus(_B)
_CghMonKal_ObjectIdentity=ObjectIdentity
cghMonKal=_CghMonKal_ObjectIdentity((1,3,6,1,4,1,9,9,600,1,4))
_CghMonKalConfigTable_Object=MibTable
cghMonKalConfigTable=_CghMonKalConfigTable_Object((1,3,6,1,4,1,9,9,600,1,4,1))
if mibBuilder.loadTexts:cghMonKalConfigTable.setStatus(_B)
_CghMonKalConfigEntry_Object=MibTableRow
cghMonKalConfigEntry=_CghMonKalConfigEntry_Object((1,3,6,1,4,1,9,9,600,1,4,1,1))
cghMonKalConfigEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:cghMonKalConfigEntry.setStatus(_B)
class _CghMonKalId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalId_Type.__name__=_E
_CghMonKalId_Object=MibTableColumn
cghMonKalId=_CghMonKalId_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,1),_CghMonKalId_Type())
cghMonKalId.setMaxAccess(_c)
if mibBuilder.loadTexts:cghMonKalId.setStatus(_B)
_CghMonKalTargetType_Type=CiscoGslbKeepaliveTargetType
_CghMonKalTargetType_Object=MibTableColumn
cghMonKalTargetType=_CghMonKalTargetType_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,2),_CghMonKalTargetType_Type())
cghMonKalTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalTargetType.setStatus(_B)
_CghMonKalMethod_Type=CiscoGslbKeepaliveMethod
_CghMonKalMethod_Object=MibTableColumn
cghMonKalMethod=_CghMonKalMethod_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,3),_CghMonKalMethod_Type())
cghMonKalMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalMethod.setStatus(_B)
_CghMonKalAnswerId_Type=Unsigned32
_CghMonKalAnswerId_Object=MibTableColumn
cghMonKalAnswerId=_CghMonKalAnswerId_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,4),_CghMonKalAnswerId_Type())
cghMonKalAnswerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalAnswerId.setStatus(_B)
class _CghMonKalPrimaryTargetType_Type(InetAddressType):defaultValue=1
_CghMonKalPrimaryTargetType_Type.__name__=_N
_CghMonKalPrimaryTargetType_Object=MibTableColumn
cghMonKalPrimaryTargetType=_CghMonKalPrimaryTargetType_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,5),_CghMonKalPrimaryTargetType_Type())
cghMonKalPrimaryTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalPrimaryTargetType.setStatus(_B)
class _CghMonKalPrimaryTarget_Type(InetAddress):defaultValue=OctetString('')
_CghMonKalPrimaryTarget_Type.__name__=_M
_CghMonKalPrimaryTarget_Object=MibTableColumn
cghMonKalPrimaryTarget=_CghMonKalPrimaryTarget_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,6),_CghMonKalPrimaryTarget_Type())
cghMonKalPrimaryTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalPrimaryTarget.setStatus(_B)
class _CghMonKalEnable_Type(TruthValue):defaultValue=2
_CghMonKalEnable_Type.__name__=_J
_CghMonKalEnable_Object=MibTableColumn
cghMonKalEnable=_CghMonKalEnable_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,7),_CghMonKalEnable_Type())
cghMonKalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalEnable.setStatus(_B)
class _CghMonKalDelay_Type(Unsigned32):defaultValue=0
_CghMonKalDelay_Type.__name__=_E
_CghMonKalDelay_Object=MibTableColumn
cghMonKalDelay=_CghMonKalDelay_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,8),_CghMonKalDelay_Type())
cghMonKalDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalDelay.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalDelay.setUnits('milliseconds')
class _CghMonKalKalapType_Type(CiscoGslbKalapType):defaultValue=2
_CghMonKalKalapType_Type.__name__=_Y
_CghMonKalKalapType_Object=MibTableColumn
cghMonKalKalapType=_CghMonKalKalapType_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,9),_CghMonKalKalapType_Type())
cghMonKalKalapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalKalapType.setStatus(_B)
class _CghMonKalTagName_Type(SnmpAdminString):defaultValue=OctetString('')
_CghMonKalTagName_Type.__name__=_G
_CghMonKalTagName_Object=MibTableColumn
cghMonKalTagName=_CghMonKalTagName_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,10),_CghMonKalTagName_Type())
cghMonKalTagName.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalTagName.setStatus(_B)
class _CghMonKalDestPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CghMonKalDestPort_Type.__name__=_O
_CghMonKalDestPort_Object=MibTableColumn
cghMonKalDestPort=_CghMonKalDestPort_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,11),_CghMonKalDestPort_Type())
cghMonKalDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalDestPort.setStatus(_B)
class _CghMonKalCappSecure_Type(TruthValue):defaultValue=2
_CghMonKalCappSecure_Type.__name__=_J
_CghMonKalCappSecure_Object=MibTableColumn
cghMonKalCappSecure=_CghMonKalCappSecure_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,12),_CghMonKalCappSecure_Type())
cghMonKalCappSecure.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalCappSecure.setStatus(_B)
_CghMonKalCappHash_Type=SnmpAdminString
_CghMonKalCappHash_Object=MibTableColumn
cghMonKalCappHash=_CghMonKalCappHash_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,13),_CghMonKalCappHash_Type())
cghMonKalCappHash.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalCappHash.setStatus(_B)
_CghMonKalQueryDomainName_Type=SnmpAdminString
_CghMonKalQueryDomainName_Object=MibTableColumn
cghMonKalQueryDomainName=_CghMonKalQueryDomainName_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,14),_CghMonKalQueryDomainName_Type())
cghMonKalQueryDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalQueryDomainName.setStatus(_B)
_CghMonKalPath_Type=SnmpAdminString
_CghMonKalPath_Object=MibTableColumn
cghMonKalPath=_CghMonKalPath_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,15),_CghMonKalPath_Type())
cghMonKalPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalPath.setStatus(_B)
class _CghMonKalHostTag_Type(SnmpAdminString):defaultValue=OctetString('')
_CghMonKalHostTag_Type.__name__=_G
_CghMonKalHostTag_Object=MibTableColumn
cghMonKalHostTag=_CghMonKalHostTag_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,16),_CghMonKalHostTag_Type())
cghMonKalHostTag.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalHostTag.setStatus(_B)
class _CghMonKalSecondaryTargetType_Type(InetAddressType):defaultValue=1
_CghMonKalSecondaryTargetType_Type.__name__=_N
_CghMonKalSecondaryTargetType_Object=MibTableColumn
cghMonKalSecondaryTargetType=_CghMonKalSecondaryTargetType_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,17),_CghMonKalSecondaryTargetType_Type())
cghMonKalSecondaryTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalSecondaryTargetType.setStatus(_B)
class _CghMonKalSecondaryTarget_Type(InetAddress):defaultValue=OctetString('')
_CghMonKalSecondaryTarget_Type.__name__=_M
_CghMonKalSecondaryTarget_Object=MibTableColumn
cghMonKalSecondaryTarget=_CghMonKalSecondaryTarget_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,18),_CghMonKalSecondaryTarget_Type())
cghMonKalSecondaryTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalSecondaryTarget.setStatus(_B)
_CghMonKalFastRetries_Type=Unsigned32
_CghMonKalFastRetries_Object=MibTableColumn
cghMonKalFastRetries=_CghMonKalFastRetries_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,19),_CghMonKalFastRetries_Type())
cghMonKalFastRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalFastRetries.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalFastRetries.setUnits(_e)
_CghMonKalFastSuccessfulProbes_Type=Unsigned32
_CghMonKalFastSuccessfulProbes_Object=MibTableColumn
cghMonKalFastSuccessfulProbes=_CghMonKalFastSuccessfulProbes_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,20),_CghMonKalFastSuccessfulProbes_Type())
cghMonKalFastSuccessfulProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalFastSuccessfulProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalFastSuccessfulProbes.setUnits(_H)
class _CghMonKalStorageType_Type(StorageType):defaultValue=3
_CghMonKalStorageType_Type.__name__=_I
_CghMonKalStorageType_Object=MibTableColumn
cghMonKalStorageType=_CghMonKalStorageType_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,21),_CghMonKalStorageType_Type())
cghMonKalStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalStorageType.setStatus(_B)
_CghMonKalRowStatus_Type=RowStatus
_CghMonKalRowStatus_Object=MibTableColumn
cghMonKalRowStatus=_CghMonKalRowStatus_Object((1,3,6,1,4,1,9,9,600,1,4,1,1,22),_CghMonKalRowStatus_Type())
cghMonKalRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalRowStatus.setStatus(_B)
_CghMonKalSharedAnswerTable_Object=MibTable
cghMonKalSharedAnswerTable=_CghMonKalSharedAnswerTable_Object((1,3,6,1,4,1,9,9,600,1,4,2))
if mibBuilder.loadTexts:cghMonKalSharedAnswerTable.setStatus(_B)
_CghMonKalSharedAnswerEntry_Object=MibTableRow
cghMonKalSharedAnswerEntry=_CghMonKalSharedAnswerEntry_Object((1,3,6,1,4,1,9,9,600,1,4,2,1))
cghMonKalSharedAnswerEntry.setIndexNames((0,_W,_X),(0,_A,_P))
if mibBuilder.loadTexts:cghMonKalSharedAnswerEntry.setStatus(_B)
class _CghMonKalShAnsStoragetype_Type(StorageType):defaultValue=3
_CghMonKalShAnsStoragetype_Type.__name__=_I
_CghMonKalShAnsStoragetype_Object=MibTableColumn
cghMonKalShAnsStoragetype=_CghMonKalShAnsStoragetype_Object((1,3,6,1,4,1,9,9,600,1,4,2,1,1),_CghMonKalShAnsStoragetype_Type())
cghMonKalShAnsStoragetype.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalShAnsStoragetype.setStatus(_B)
_CghMonKalShAnsRowStatus_Type=RowStatus
_CghMonKalShAnsRowStatus_Object=MibTableColumn
cghMonKalShAnsRowStatus=_CghMonKalShAnsRowStatus_Object((1,3,6,1,4,1,9,9,600,1,4,2,1,2),_CghMonKalShAnsRowStatus_Type())
cghMonKalShAnsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cghMonKalShAnsRowStatus.setStatus(_B)
_CghMonKalStatsTable_Object=MibTable
cghMonKalStatsTable=_CghMonKalStatsTable_Object((1,3,6,1,4,1,9,9,600,1,4,3))
if mibBuilder.loadTexts:cghMonKalStatsTable.setStatus(_B)
_CghMonKalStatsEntry_Object=MibTableRow
cghMonKalStatsEntry=_CghMonKalStatsEntry_Object((1,3,6,1,4,1,9,9,600,1,4,3,1))
if mibBuilder.loadTexts:cghMonKalStatsEntry.setStatus(_B)
_CghMonKalStatus_Type=CiscoGslbKeepaliveStatus
_CghMonKalStatus_Object=MibTableColumn
cghMonKalStatus=_CghMonKalStatus_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,1),_CghMonKalStatus_Type())
cghMonKalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalStatus.setStatus(_B)
_CghMonKalSentProbes_Type=Counter32
_CghMonKalSentProbes_Object=MibTableColumn
cghMonKalSentProbes=_CghMonKalSentProbes_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,2),_CghMonKalSentProbes_Type())
cghMonKalSentProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalSentProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalSentProbes.setUnits(_H)
_CghMonKalReceivedProbes_Type=Counter32
_CghMonKalReceivedProbes_Object=MibTableColumn
cghMonKalReceivedProbes=_CghMonKalReceivedProbes_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,3),_CghMonKalReceivedProbes_Type())
cghMonKalReceivedProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalReceivedProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalReceivedProbes.setUnits(_H)
_CghMonKalPositiveProbes_Type=Counter32
_CghMonKalPositiveProbes_Object=MibTableColumn
cghMonKalPositiveProbes=_CghMonKalPositiveProbes_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,4),_CghMonKalPositiveProbes_Type())
cghMonKalPositiveProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalPositiveProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalPositiveProbes.setUnits(_H)
_CghMonKalNegativeProbes_Type=Counter32
_CghMonKalNegativeProbes_Object=MibTableColumn
cghMonKalNegativeProbes=_CghMonKalNegativeProbes_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,5),_CghMonKalNegativeProbes_Type())
cghMonKalNegativeProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalNegativeProbes.setStatus(_B)
if mibBuilder.loadTexts:cghMonKalNegativeProbes.setUnits(_H)
_CghMonKalStatusTransitions_Type=Counter32
_CghMonKalStatusTransitions_Object=MibTableColumn
cghMonKalStatusTransitions=_CghMonKalStatusTransitions_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,6),_CghMonKalStatusTransitions_Type())
cghMonKalStatusTransitions.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalStatusTransitions.setStatus(_B)
_CghMonKalDynamicLoad_Type=Unsigned32
_CghMonKalDynamicLoad_Object=MibTableColumn
cghMonKalDynamicLoad=_CghMonKalDynamicLoad_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,7),_CghMonKalDynamicLoad_Type())
cghMonKalDynamicLoad.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalDynamicLoad.setStatus(_B)
_CghMonKalVIPFailovers_Type=Counter32
_CghMonKalVIPFailovers_Object=MibTableColumn
cghMonKalVIPFailovers=_CghMonKalVIPFailovers_Object((1,3,6,1,4,1,9,9,600,1,4,3,1,8),_CghMonKalVIPFailovers_Type())
cghMonKalVIPFailovers.setMaxAccess(_D)
if mibBuilder.loadTexts:cghMonKalVIPFailovers.setStatus(_B)
_CiscoGslbHealthMonMIBConform_ObjectIdentity=ObjectIdentity
ciscoGslbHealthMonMIBConform=_CiscoGslbHealthMonMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,600,2))
_CiscoGslbHealthMonMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGslbHealthMonMIBCompliances=_CiscoGslbHealthMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,600,2,1))
_CiscoGslbHealthMonMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGslbHealthMonMIBGroups=_CiscoGslbHealthMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,600,2,2))
cghMonKalConfigEntry.registerAugmentions((_A,_f))
cghMonKalStatsEntry.setIndexNames(*cghMonKalConfigEntry.getIndexNames())
ciscoGslbGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,1))
ciscoGslbGeneralConfigGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_K),(_A,_Q)))
if mibBuilder.loadTexts:ciscoGslbGeneralConfigGroup.setStatus(_B)
ciscoGslbKalParameterGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,2))
ciscoGslbKalParameterGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:ciscoGslbKalParameterGroup.setStatus(_B)
ciscoGslbKalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,3))
ciscoGslbKalConfigGroup.setObjects(*((_A,_v),(_A,_R),(_A,_w),(_A,_S),(_A,_T),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoGslbKalConfigGroup.setStatus(_B)
ciscoGslbKalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,4))
ciscoGslbKalStatsGroup.setObjects(*((_A,_U),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:ciscoGslbKalStatsGroup.setStatus(_B)
ciscoGslbKalNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,5))
ciscoGslbKalNotifControlGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:ciscoGslbKalNotifControlGroup.setStatus(_B)
ciscoGslbKalNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,6))
ciscoGslbKalNotifObjectsGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:ciscoGslbKalNotifObjectsGroup.setStatus(_B)
ciscoGslbGeneralConfigRateLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,600,2,2,8))
ciscoGslbGeneralConfigRateLimitGroup.setObjects(*((_A,_K),(_A,_Q)))
if mibBuilder.loadTexts:ciscoGslbGeneralConfigRateLimitGroup.setStatus(_B)
ciscoGslbKalEventStatus=NotificationType((1,3,6,1,4,1,9,9,600,0,1))
ciscoGslbKalEventStatus.setObjects(*((_Z,_a),(_A,_S),(_A,_T),(_A,_R),(_A,_V),(_A,_U),(_A,_K)))
if mibBuilder.loadTexts:ciscoGslbKalEventStatus.setStatus(_B)
ciscoGslbKalNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,600,2,2,7))
ciscoGslbKalNotificationGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:ciscoGslbKalNotificationGroup.setStatus(_B)
ciscoGslbHealthMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,600,2,1,1))
ciscoGslbHealthMonMIBCompliance.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:ciscoGslbHealthMonMIBCompliance.setStatus('deprecated')
mibBuilder.exportSymbols(_A,**{'ciscoGslbHealthMonMIB':ciscoGslbHealthMonMIB,'ciscoGslbHealthMonMIBNotifs':ciscoGslbHealthMonMIBNotifs,_AN:ciscoGslbKalEventStatus,'ciscoGslbHealthMonMIBObjects':ciscoGslbHealthMonMIBObjects,'cghMonNotifControl':cghMonNotifControl,_AM:cghMonKalNotifEnable,'cghMonNotifObjects':cghMonNotifObjects,_V:cghMonKalPrevStatus,'cghMonKalGeneralConfig':cghMonKalGeneralConfig,_g:cghMonNsQueryDomainName,_h:cghMonCappHash,_i:cghMonHttpHeadPath,_j:cghMonHttpHeadConnTermMethod,_l:cghMonTcpConnTermMethod,_k:cghMonCraDecay,_m:cghMonTotalConfiguredProbes,_K:cghMonDroppedKalNotifs,_Q:cghMonKalTrapRateLimit,'cghMonKalParameterTable':cghMonKalParameterTable,'cghMonKalParameterEntry':cghMonKalParameterEntry,_b:cghMonKalParameterMethod,_n:cghMonKalParameterRate,_o:cghMonKalParameterMinimumFrequency,_p:cghMonKalParameterResponseTimeout,_q:cghMonKalParameterFastRetries,_r:cghMonKalParameterFastSuccessfulProbes,_s:cghMonKalParameterDestPort,_t:cghMonKalParameterStorageType,_u:cghMonKalParameterRowStatus,'cghMonKal':cghMonKal,'cghMonKalConfigTable':cghMonKalConfigTable,'cghMonKalConfigEntry':cghMonKalConfigEntry,_P:cghMonKalId,_v:cghMonKalTargetType,_R:cghMonKalMethod,_w:cghMonKalAnswerId,_S:cghMonKalPrimaryTargetType,_T:cghMonKalPrimaryTarget,_x:cghMonKalEnable,_y:cghMonKalDelay,_z:cghMonKalKalapType,_A0:cghMonKalTagName,_A1:cghMonKalDestPort,_A2:cghMonKalCappSecure,_A3:cghMonKalCappHash,_A4:cghMonKalQueryDomainName,_A5:cghMonKalPath,_A6:cghMonKalHostTag,_A7:cghMonKalSecondaryTargetType,_A8:cghMonKalSecondaryTarget,_A9:cghMonKalFastRetries,_AA:cghMonKalFastSuccessfulProbes,_AB:cghMonKalStorageType,_AC:cghMonKalRowStatus,'cghMonKalSharedAnswerTable':cghMonKalSharedAnswerTable,'cghMonKalSharedAnswerEntry':cghMonKalSharedAnswerEntry,_AD:cghMonKalShAnsStoragetype,_AE:cghMonKalShAnsRowStatus,'cghMonKalStatsTable':cghMonKalStatsTable,_f:cghMonKalStatsEntry,_U:cghMonKalStatus,_AF:cghMonKalSentProbes,_AG:cghMonKalReceivedProbes,_AH:cghMonKalPositiveProbes,_AI:cghMonKalNegativeProbes,_AJ:cghMonKalStatusTransitions,_AK:cghMonKalDynamicLoad,_AL:cghMonKalVIPFailovers,'ciscoGslbHealthMonMIBConform':ciscoGslbHealthMonMIBConform,'ciscoGslbHealthMonMIBCompliances':ciscoGslbHealthMonMIBCompliances,'ciscoGslbHealthMonMIBCompliance':ciscoGslbHealthMonMIBCompliance,'ciscoGslbHealthMonMIBGroups':ciscoGslbHealthMonMIBGroups,_AO:ciscoGslbGeneralConfigGroup,_AP:ciscoGslbKalParameterGroup,_AQ:ciscoGslbKalConfigGroup,_AR:ciscoGslbKalStatsGroup,_AS:ciscoGslbKalNotifControlGroup,_AT:ciscoGslbKalNotifObjectsGroup,_AU:ciscoGslbKalNotificationGroup,_AV:ciscoGslbGeneralConfigRateLimitGroup})