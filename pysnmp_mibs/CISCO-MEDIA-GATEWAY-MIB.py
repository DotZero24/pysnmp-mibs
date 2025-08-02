_Ai='cMediaGwGroupRev2'
_Ah='cmgwSignalProtocolGroupRev1'
_Ag='cmgwCallControlGroup'
_Af='cmgwSignalProtocolGroup'
_Ae='cMediaGwGroup'
_Ad='cmgwV23Enabled'
_Ac='cMediaGwCcCfgDefRtpNamePrefix'
_Ab='cmgwLawInterceptEnabled'
_Aa='cmgwSrcFilterEnabled'
_AZ='cmgwRscSinceLastReset'
_AY='cmgwRscAverageUtilization'
_AX='cmgwRscMinimumUtilization'
_AW='cmgwRscMaximumUtilization'
_AV='cmgwSignalProtocolConfigVer'
_AU='cmgwSignalProtocolPreference'
_AT='cmgwLifVoiceIfCount'
_AS='cmgwLifPvcCount'
_AR='cmgwDnsIpRowStatus'
_AQ='cmgwDnsIpType'
_AP='cmgwDnsIp'
_AO='cmgwDnsDomainName'
_AN='cmgwIpConfigRowStatus'
_AM='cmgwIpConfigForRemoteMapping'
_AL='cmgwIpConfigDefaultGwIp'
_AK='cmgwIpConfigSubnetMask'
_AJ='cmgwIpConfigAddress'
_AI='cmgwIpConfigAddrType'
_AH='cmgwIpConfigVci'
_AG='cmgwIpConfigVpi'
_AF='cmgwIpConfigIfIndex'
_AE='cmgwConfigDomainNameRowStatus'
_AD='cmgwConfigDomainName'
_AC='cmgwConfigDomainNameEntity'
_AB='cmgwRscStatsIndex'
_AA='CVoiceTonePlanIndex'
_A9='CCallControlJitterDelayMode'
_A8='cmgwLifNumber'
_A7='cmgwDnsIpIndex'
_A6='cmgwConfigDomainNameIndex'
_A5='cmgwIpConfigIndex'
_A4='cmgwSignalProtocolIndex'
_A3='gracefulOutOfService'
_A2='forcedOutOfService'
_A1='inService'
_A0='cmgwCallControlGroupRev2'
_z='cmgwSignalMgcProtocolPort'
_y='cMediaGwCcCfgDefBearerTraffic'
_x='cmgwVtMappingMode'
_w='Gauge32'
_v='InetAddressType'
_u='cMediaGwRscStatsGroup'
_t='cmgwSignalProtocolGroupRev3'
_s='cMediaGwGroupExtra'
_r='cmgwCallControlGroupRev1'
_q='cMediaGwCcCfgClusterEnabled'
_p='cMediaGwCcCfgAal2SvcNamePrefix'
_o='cMediaGwCcCfgAal1SvcNamePrefix'
_n='cMediaGwCcCfgRtpNamePrefix'
_m='cMediaGwCcCfgDsNamePrefix'
_l='cMediaGwCcCfgDescrInfoEnabled'
_k='cMediaGwCcCfgDefaultTonePlanId'
_j='cMediaGwCcCfgVbdJitterMinDelay'
_i='cMediaGwCcCfgVbdJitterNomDelay'
_h='cMediaGwCcCfgVbdJitterMaxDelay'
_g='cMediaGwCcCfgVbdJitterDelayMode'
_f='cMediaGwCcCfgNseRespTimer'
_e='cMediaGwCcCfgNsePayload'
_d='cMediaGwCcCfgNtePayload'
_c='cMediaGwCcCfgBearerTos'
_b='cMediaGwCcCfgControlTos'
_a='cmgwSignalProtocolPort'
_Z='cmgwSignalProtocolVersion'
_Y='cmgwSignalProtocol'
_X='cmgwGraceTime'
_W='cmgwAdminState'
_V='cmgwServiceState'
_U='cmgwPhysicalIndex'
_T='cmgwDomainName'
_S='milliseconds'
_R='cmgwSignalProtocolGroupRev2'
_Q='cMediaGwGroupRev1'
_P='cmgwLifGroup'
_O='cmgwDnsIpGroup'
_N='cMediaGwIpGroup'
_M='cmgwDomainNameGroup'
_L='not-accessible'
_K='TruthValue'
_J='deprecated'
_I='cmgwIndex'
_H='Unsigned32'
_G='SnmpAdminString'
_F='read-only'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-MEDIA-GATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,EntPhysicalIndexOrZero=mibBuilder.importSymbols('CISCO-TC','CiscoPort','EntPhysicalIndexOrZero')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength',_v,'InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_w,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
ciscoMediaGatewayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,324))
if mibBuilder.loadTexts:ciscoMediaGatewayMIB.setRevisions(('2009-02-25 00:00','2006-06-15 00:00','2005-09-01 00:00','2004-11-19 00:00','2004-07-30 00:00','2003-04-07 00:00'))
class CGwServiceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),(_A2,2),(_A3,3)))
class CGwAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A1,1),(_A2,2),(_A3,3)))
class GatewayLifNumber(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
class CVoiceTonePlanIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CVoiceTonePlanIndexOrZero(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class CCallControlProfileIndex(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CCallControlProfileIndexOrZero(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class CCallControlJitterDelayMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adaptive',1),('fixed',2)))
_CiscoMediaGatewayMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoMediaGatewayMIBNotifs=_CiscoMediaGatewayMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,324,0))
_CiscoMediaGatewayMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMediaGatewayMIBObjects=_CiscoMediaGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,324,1))
_CMediaGwConfig_ObjectIdentity=ObjectIdentity
cMediaGwConfig=_CMediaGwConfig_ObjectIdentity((1,3,6,1,4,1,9,9,324,1,1))
_CMediaGwTable_Object=MibTable
cMediaGwTable=_CMediaGwTable_Object((1,3,6,1,4,1,9,9,324,1,1,1))
if mibBuilder.loadTexts:cMediaGwTable.setStatus(_B)
_CMediaGwEntry_Object=MibTableRow
cMediaGwEntry=_CMediaGwEntry_Object((1,3,6,1,4,1,9,9,324,1,1,1,1))
cMediaGwEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cMediaGwEntry.setStatus(_B)
class _CmgwIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CmgwIndex_Type.__name__=_D
_CmgwIndex_Object=MibTableColumn
cmgwIndex=_CmgwIndex_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,1),_CmgwIndex_Type())
cmgwIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwIndex.setStatus(_B)
class _CmgwDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmgwDomainName_Type.__name__=_G
_CmgwDomainName_Object=MibTableColumn
cmgwDomainName=_CmgwDomainName_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,2),_CmgwDomainName_Type())
cmgwDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwDomainName.setStatus(_B)
_CmgwPhysicalIndex_Type=EntPhysicalIndexOrZero
_CmgwPhysicalIndex_Object=MibTableColumn
cmgwPhysicalIndex=_CmgwPhysicalIndex_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,3),_CmgwPhysicalIndex_Type())
cmgwPhysicalIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwPhysicalIndex.setStatus(_B)
_CmgwServiceState_Type=CGwServiceState
_CmgwServiceState_Object=MibTableColumn
cmgwServiceState=_CmgwServiceState_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,4),_CmgwServiceState_Type())
cmgwServiceState.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwServiceState.setStatus(_B)
_CmgwAdminState_Type=CGwAdminState
_CmgwAdminState_Object=MibTableColumn
cmgwAdminState=_CmgwAdminState_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,5),_CmgwAdminState_Type())
cmgwAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwAdminState.setStatus(_B)
class _CmgwGraceTime_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CmgwGraceTime_Type.__name__=_D
_CmgwGraceTime_Object=MibTableColumn
cmgwGraceTime=_CmgwGraceTime_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,6),_CmgwGraceTime_Type())
cmgwGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwGraceTime.setStatus(_B)
if mibBuilder.loadTexts:cmgwGraceTime.setUnits('seconds')
class _CmgwVtMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('titan',2)))
_CmgwVtMappingMode_Type.__name__=_D
_CmgwVtMappingMode_Object=MibTableColumn
cmgwVtMappingMode=_CmgwVtMappingMode_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,7),_CmgwVtMappingMode_Type())
cmgwVtMappingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwVtMappingMode.setStatus(_B)
class _CmgwSrcFilterEnabled_Type(TruthValue):defaultValue=2
_CmgwSrcFilterEnabled_Type.__name__=_K
_CmgwSrcFilterEnabled_Object=MibTableColumn
cmgwSrcFilterEnabled=_CmgwSrcFilterEnabled_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,8),_CmgwSrcFilterEnabled_Type())
cmgwSrcFilterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwSrcFilterEnabled.setStatus(_B)
class _CmgwLawInterceptEnabled_Type(TruthValue):defaultValue=2
_CmgwLawInterceptEnabled_Type.__name__=_K
_CmgwLawInterceptEnabled_Object=MibTableColumn
cmgwLawInterceptEnabled=_CmgwLawInterceptEnabled_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,9),_CmgwLawInterceptEnabled_Type())
cmgwLawInterceptEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwLawInterceptEnabled.setStatus(_B)
class _CmgwV23Enabled_Type(TruthValue):defaultValue=2
_CmgwV23Enabled_Type.__name__=_K
_CmgwV23Enabled_Object=MibTableColumn
cmgwV23Enabled=_CmgwV23Enabled_Object((1,3,6,1,4,1,9,9,324,1,1,1,1,10),_CmgwV23Enabled_Type())
cmgwV23Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwV23Enabled.setStatus(_B)
_CmgwSignalProtocolTable_Object=MibTable
cmgwSignalProtocolTable=_CmgwSignalProtocolTable_Object((1,3,6,1,4,1,9,9,324,1,1,2))
if mibBuilder.loadTexts:cmgwSignalProtocolTable.setStatus(_B)
_CmgwSignalProtocolEntry_Object=MibTableRow
cmgwSignalProtocolEntry=_CmgwSignalProtocolEntry_Object((1,3,6,1,4,1,9,9,324,1,1,2,1))
cmgwSignalProtocolEntry.setIndexNames((0,_A,_I),(0,_A,_A4))
if mibBuilder.loadTexts:cmgwSignalProtocolEntry.setStatus(_B)
class _CmgwSignalProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmgwSignalProtocolIndex_Type.__name__=_D
_CmgwSignalProtocolIndex_Object=MibTableColumn
cmgwSignalProtocolIndex=_CmgwSignalProtocolIndex_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,1),_CmgwSignalProtocolIndex_Type())
cmgwSignalProtocolIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwSignalProtocolIndex.setStatus(_B)
class _CmgwSignalProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('mgcp',2),('h248',3),('tgcp',4)))
_CmgwSignalProtocol_Type.__name__=_D
_CmgwSignalProtocol_Object=MibTableColumn
cmgwSignalProtocol=_CmgwSignalProtocol_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,2),_CmgwSignalProtocol_Type())
cmgwSignalProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwSignalProtocol.setStatus(_B)
class _CmgwSignalProtocolVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CmgwSignalProtocolVersion_Type.__name__=_G
_CmgwSignalProtocolVersion_Object=MibTableColumn
cmgwSignalProtocolVersion=_CmgwSignalProtocolVersion_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,3),_CmgwSignalProtocolVersion_Type())
cmgwSignalProtocolVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwSignalProtocolVersion.setStatus(_B)
_CmgwSignalProtocolPort_Type=CiscoPort
_CmgwSignalProtocolPort_Object=MibTableColumn
cmgwSignalProtocolPort=_CmgwSignalProtocolPort_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,4),_CmgwSignalProtocolPort_Type())
cmgwSignalProtocolPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwSignalProtocolPort.setStatus(_B)
_CmgwSignalMgcProtocolPort_Type=InetPortNumber
_CmgwSignalMgcProtocolPort_Object=MibTableColumn
cmgwSignalMgcProtocolPort=_CmgwSignalMgcProtocolPort_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,5),_CmgwSignalMgcProtocolPort_Type())
cmgwSignalMgcProtocolPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwSignalMgcProtocolPort.setStatus(_B)
class _CmgwSignalProtocolPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CmgwSignalProtocolPreference_Type.__name__=_D
_CmgwSignalProtocolPreference_Object=MibTableColumn
cmgwSignalProtocolPreference=_CmgwSignalProtocolPreference_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,6),_CmgwSignalProtocolPreference_Type())
cmgwSignalProtocolPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwSignalProtocolPreference.setStatus(_B)
class _CmgwSignalProtocolConfigVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CmgwSignalProtocolConfigVer_Type.__name__=_G
_CmgwSignalProtocolConfigVer_Object=MibTableColumn
cmgwSignalProtocolConfigVer=_CmgwSignalProtocolConfigVer_Object((1,3,6,1,4,1,9,9,324,1,1,2,1,7),_CmgwSignalProtocolConfigVer_Type())
cmgwSignalProtocolConfigVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cmgwSignalProtocolConfigVer.setStatus(_B)
_CMediaGwIpConfigTable_Object=MibTable
cMediaGwIpConfigTable=_CMediaGwIpConfigTable_Object((1,3,6,1,4,1,9,9,324,1,1,3))
if mibBuilder.loadTexts:cMediaGwIpConfigTable.setStatus(_B)
_CMediaGwIpConfigEntry_Object=MibTableRow
cMediaGwIpConfigEntry=_CMediaGwIpConfigEntry_Object((1,3,6,1,4,1,9,9,324,1,1,3,1))
cMediaGwIpConfigEntry.setIndexNames((0,_A,_I),(0,_A,_A5))
if mibBuilder.loadTexts:cMediaGwIpConfigEntry.setStatus(_B)
class _CmgwIpConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CmgwIpConfigIndex_Type.__name__=_D
_CmgwIpConfigIndex_Object=MibTableColumn
cmgwIpConfigIndex=_CmgwIpConfigIndex_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,1),_CmgwIpConfigIndex_Type())
cmgwIpConfigIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwIpConfigIndex.setStatus(_B)
_CmgwIpConfigIfIndex_Type=InterfaceIndexOrZero
_CmgwIpConfigIfIndex_Object=MibTableColumn
cmgwIpConfigIfIndex=_CmgwIpConfigIfIndex_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,2),_CmgwIpConfigIfIndex_Type())
cmgwIpConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigIfIndex.setStatus(_B)
class _CmgwIpConfigVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_CmgwIpConfigVpi_Type.__name__=_D
_CmgwIpConfigVpi_Object=MibTableColumn
cmgwIpConfigVpi=_CmgwIpConfigVpi_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,3),_CmgwIpConfigVpi_Type())
cmgwIpConfigVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigVpi.setStatus(_B)
class _CmgwIpConfigVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CmgwIpConfigVci_Type.__name__=_D
_CmgwIpConfigVci_Object=MibTableColumn
cmgwIpConfigVci=_CmgwIpConfigVci_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,4),_CmgwIpConfigVci_Type())
cmgwIpConfigVci.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigVci.setStatus(_B)
class _CmgwIpConfigAddrType_Type(InetAddressType):defaultValue=1
_CmgwIpConfigAddrType_Type.__name__=_v
_CmgwIpConfigAddrType_Object=MibTableColumn
cmgwIpConfigAddrType=_CmgwIpConfigAddrType_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,5),_CmgwIpConfigAddrType_Type())
cmgwIpConfigAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigAddrType.setStatus(_B)
_CmgwIpConfigAddress_Type=InetAddress
_CmgwIpConfigAddress_Object=MibTableColumn
cmgwIpConfigAddress=_CmgwIpConfigAddress_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,6),_CmgwIpConfigAddress_Type())
cmgwIpConfigAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigAddress.setStatus(_B)
_CmgwIpConfigSubnetMask_Type=InetAddressPrefixLength
_CmgwIpConfigSubnetMask_Object=MibTableColumn
cmgwIpConfigSubnetMask=_CmgwIpConfigSubnetMask_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,7),_CmgwIpConfigSubnetMask_Type())
cmgwIpConfigSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigSubnetMask.setStatus(_B)
class _CmgwIpConfigDefaultGwIp_Type(TruthValue):defaultValue=2
_CmgwIpConfigDefaultGwIp_Type.__name__=_K
_CmgwIpConfigDefaultGwIp_Object=MibTableColumn
cmgwIpConfigDefaultGwIp=_CmgwIpConfigDefaultGwIp_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,8),_CmgwIpConfigDefaultGwIp_Type())
cmgwIpConfigDefaultGwIp.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigDefaultGwIp.setStatus(_B)
class _CmgwIpConfigForRemoteMapping_Type(TruthValue):defaultValue=2
_CmgwIpConfigForRemoteMapping_Type.__name__=_K
_CmgwIpConfigForRemoteMapping_Object=MibTableColumn
cmgwIpConfigForRemoteMapping=_CmgwIpConfigForRemoteMapping_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,9),_CmgwIpConfigForRemoteMapping_Type())
cmgwIpConfigForRemoteMapping.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigForRemoteMapping.setStatus(_B)
_CmgwIpConfigRowStatus_Type=RowStatus
_CmgwIpConfigRowStatus_Object=MibTableColumn
cmgwIpConfigRowStatus=_CmgwIpConfigRowStatus_Object((1,3,6,1,4,1,9,9,324,1,1,3,1,10),_CmgwIpConfigRowStatus_Type())
cmgwIpConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwIpConfigRowStatus.setStatus(_B)
_CMediaGwDomainNameConfigTable_Object=MibTable
cMediaGwDomainNameConfigTable=_CMediaGwDomainNameConfigTable_Object((1,3,6,1,4,1,9,9,324,1,1,4))
if mibBuilder.loadTexts:cMediaGwDomainNameConfigTable.setStatus(_B)
_CMediaGwDomainNameConfigEntry_Object=MibTableRow
cMediaGwDomainNameConfigEntry=_CMediaGwDomainNameConfigEntry_Object((1,3,6,1,4,1,9,9,324,1,1,4,1))
cMediaGwDomainNameConfigEntry.setIndexNames((0,_A,_I),(0,_A,_A6))
if mibBuilder.loadTexts:cMediaGwDomainNameConfigEntry.setStatus(_B)
class _CmgwConfigDomainNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CmgwConfigDomainNameIndex_Type.__name__=_D
_CmgwConfigDomainNameIndex_Object=MibTableColumn
cmgwConfigDomainNameIndex=_CmgwConfigDomainNameIndex_Object((1,3,6,1,4,1,9,9,324,1,1,4,1,1),_CmgwConfigDomainNameIndex_Type())
cmgwConfigDomainNameIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwConfigDomainNameIndex.setStatus(_B)
class _CmgwConfigDomainNameEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('gateway',1),('dnsServer',2),('mgc',3)))
_CmgwConfigDomainNameEntity_Type.__name__=_D
_CmgwConfigDomainNameEntity_Object=MibTableColumn
cmgwConfigDomainNameEntity=_CmgwConfigDomainNameEntity_Object((1,3,6,1,4,1,9,9,324,1,1,4,1,2),_CmgwConfigDomainNameEntity_Type())
cmgwConfigDomainNameEntity.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwConfigDomainNameEntity.setStatus(_B)
class _CmgwConfigDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CmgwConfigDomainName_Type.__name__=_G
_CmgwConfigDomainName_Object=MibTableColumn
cmgwConfigDomainName=_CmgwConfigDomainName_Object((1,3,6,1,4,1,9,9,324,1,1,4,1,3),_CmgwConfigDomainName_Type())
cmgwConfigDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwConfigDomainName.setStatus(_B)
_CmgwConfigDomainNameRowStatus_Type=RowStatus
_CmgwConfigDomainNameRowStatus_Object=MibTableColumn
cmgwConfigDomainNameRowStatus=_CmgwConfigDomainNameRowStatus_Object((1,3,6,1,4,1,9,9,324,1,1,4,1,4),_CmgwConfigDomainNameRowStatus_Type())
cmgwConfigDomainNameRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwConfigDomainNameRowStatus.setStatus(_B)
_CMediaGwDnsIpConfigTable_Object=MibTable
cMediaGwDnsIpConfigTable=_CMediaGwDnsIpConfigTable_Object((1,3,6,1,4,1,9,9,324,1,1,5))
if mibBuilder.loadTexts:cMediaGwDnsIpConfigTable.setStatus(_B)
_CMediaGwDnsIpConfigEntry_Object=MibTableRow
cMediaGwDnsIpConfigEntry=_CMediaGwDnsIpConfigEntry_Object((1,3,6,1,4,1,9,9,324,1,1,5,1))
cMediaGwDnsIpConfigEntry.setIndexNames((0,_A,_I),(0,_A,_A7))
if mibBuilder.loadTexts:cMediaGwDnsIpConfigEntry.setStatus(_B)
class _CmgwDnsIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CmgwDnsIpIndex_Type.__name__=_D
_CmgwDnsIpIndex_Object=MibTableColumn
cmgwDnsIpIndex=_CmgwDnsIpIndex_Object((1,3,6,1,4,1,9,9,324,1,1,5,1,1),_CmgwDnsIpIndex_Type())
cmgwDnsIpIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwDnsIpIndex.setStatus(_B)
class _CmgwDnsDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CmgwDnsDomainName_Type.__name__=_G
_CmgwDnsDomainName_Object=MibTableColumn
cmgwDnsDomainName=_CmgwDnsDomainName_Object((1,3,6,1,4,1,9,9,324,1,1,5,1,2),_CmgwDnsDomainName_Type())
cmgwDnsDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwDnsDomainName.setStatus(_B)
class _CmgwDnsIpType_Type(InetAddressType):defaultValue=1
_CmgwDnsIpType_Type.__name__=_v
_CmgwDnsIpType_Object=MibTableColumn
cmgwDnsIpType=_CmgwDnsIpType_Object((1,3,6,1,4,1,9,9,324,1,1,5,1,3),_CmgwDnsIpType_Type())
cmgwDnsIpType.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwDnsIpType.setStatus(_B)
_CmgwDnsIp_Type=InetAddress
_CmgwDnsIp_Object=MibTableColumn
cmgwDnsIp=_CmgwDnsIp_Object((1,3,6,1,4,1,9,9,324,1,1,5,1,4),_CmgwDnsIp_Type())
cmgwDnsIp.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwDnsIp.setStatus(_B)
_CmgwDnsIpRowStatus_Type=RowStatus
_CmgwDnsIpRowStatus_Object=MibTableColumn
cmgwDnsIpRowStatus=_CmgwDnsIpRowStatus_Object((1,3,6,1,4,1,9,9,324,1,1,5,1,5),_CmgwDnsIpRowStatus_Type())
cmgwDnsIpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cmgwDnsIpRowStatus.setStatus(_B)
_CmgwLifTable_Object=MibTable
cmgwLifTable=_CmgwLifTable_Object((1,3,6,1,4,1,9,9,324,1,1,6))
if mibBuilder.loadTexts:cmgwLifTable.setStatus(_B)
_CmgwLifEntry_Object=MibTableRow
cmgwLifEntry=_CmgwLifEntry_Object((1,3,6,1,4,1,9,9,324,1,1,6,1))
cmgwLifEntry.setIndexNames((0,_A,_I),(0,_A,_A8))
if mibBuilder.loadTexts:cmgwLifEntry.setStatus(_B)
_CmgwLifNumber_Type=GatewayLifNumber
_CmgwLifNumber_Object=MibTableColumn
cmgwLifNumber=_CmgwLifNumber_Object((1,3,6,1,4,1,9,9,324,1,1,6,1,1),_CmgwLifNumber_Type())
cmgwLifNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwLifNumber.setStatus(_B)
class _CmgwLifPvcCount_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CmgwLifPvcCount_Type.__name__=_w
_CmgwLifPvcCount_Object=MibTableColumn
cmgwLifPvcCount=_CmgwLifPvcCount_Object((1,3,6,1,4,1,9,9,324,1,1,6,1,2),_CmgwLifPvcCount_Type())
cmgwLifPvcCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwLifPvcCount.setStatus(_B)
class _CmgwLifVoiceIfCount_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CmgwLifVoiceIfCount_Type.__name__=_w
_CmgwLifVoiceIfCount_Object=MibTableColumn
cmgwLifVoiceIfCount=_CmgwLifVoiceIfCount_Object((1,3,6,1,4,1,9,9,324,1,1,6,1,3),_CmgwLifVoiceIfCount_Type())
cmgwLifVoiceIfCount.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwLifVoiceIfCount.setStatus(_B)
_CMediaGwCallControlConfigTable_Object=MibTable
cMediaGwCallControlConfigTable=_CMediaGwCallControlConfigTable_Object((1,3,6,1,4,1,9,9,324,1,1,7))
if mibBuilder.loadTexts:cMediaGwCallControlConfigTable.setStatus(_B)
_CMediaGwCallControlConfigEntry_Object=MibTableRow
cMediaGwCallControlConfigEntry=_CMediaGwCallControlConfigEntry_Object((1,3,6,1,4,1,9,9,324,1,1,7,1))
cMediaGwCallControlConfigEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:cMediaGwCallControlConfigEntry.setStatus(_B)
class _CMediaGwCcCfgControlTos_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CMediaGwCcCfgControlTos_Type.__name__=_H
_CMediaGwCcCfgControlTos_Object=MibTableColumn
cMediaGwCcCfgControlTos=_CMediaGwCcCfgControlTos_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,1),_CMediaGwCcCfgControlTos_Type())
cMediaGwCcCfgControlTos.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgControlTos.setStatus(_B)
class _CMediaGwCcCfgBearerTos_Type(Unsigned32):defaultValue=160;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CMediaGwCcCfgBearerTos_Type.__name__=_H
_CMediaGwCcCfgBearerTos_Object=MibTableColumn
cMediaGwCcCfgBearerTos=_CMediaGwCcCfgBearerTos_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,2),_CMediaGwCcCfgBearerTos_Type())
cMediaGwCcCfgBearerTos.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgBearerTos.setStatus(_B)
class _CMediaGwCcCfgNtePayload_Type(Unsigned32):defaultValue=101;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_CMediaGwCcCfgNtePayload_Type.__name__=_H
_CMediaGwCcCfgNtePayload_Object=MibTableColumn
cMediaGwCcCfgNtePayload=_CMediaGwCcCfgNtePayload_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,3),_CMediaGwCcCfgNtePayload_Type())
cMediaGwCcCfgNtePayload.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgNtePayload.setStatus(_B)
class _CMediaGwCcCfgNsePayload_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(98,117))
_CMediaGwCcCfgNsePayload_Type.__name__=_H
_CMediaGwCcCfgNsePayload_Object=MibTableColumn
cMediaGwCcCfgNsePayload=_CMediaGwCcCfgNsePayload_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,4),_CMediaGwCcCfgNsePayload_Type())
cMediaGwCcCfgNsePayload.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgNsePayload.setStatus(_B)
class _CMediaGwCcCfgNseRespTimer_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,10000))
_CMediaGwCcCfgNseRespTimer_Type.__name__=_H
_CMediaGwCcCfgNseRespTimer_Object=MibTableColumn
cMediaGwCcCfgNseRespTimer=_CMediaGwCcCfgNseRespTimer_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,5),_CMediaGwCcCfgNseRespTimer_Type())
cMediaGwCcCfgNseRespTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgNseRespTimer.setStatus(_B)
if mibBuilder.loadTexts:cMediaGwCcCfgNseRespTimer.setUnits(_S)
class _CMediaGwCcCfgVbdJitterDelayMode_Type(CCallControlJitterDelayMode):defaultValue=2
_CMediaGwCcCfgVbdJitterDelayMode_Type.__name__=_A9
_CMediaGwCcCfgVbdJitterDelayMode_Object=MibTableColumn
cMediaGwCcCfgVbdJitterDelayMode=_CMediaGwCcCfgVbdJitterDelayMode_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,6),_CMediaGwCcCfgVbdJitterDelayMode_Type())
cMediaGwCcCfgVbdJitterDelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterDelayMode.setStatus(_B)
class _CMediaGwCcCfgVbdJitterMaxDelay_Type(Unsigned32):defaultValue=135;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,135))
_CMediaGwCcCfgVbdJitterMaxDelay_Type.__name__=_H
_CMediaGwCcCfgVbdJitterMaxDelay_Object=MibTableColumn
cMediaGwCcCfgVbdJitterMaxDelay=_CMediaGwCcCfgVbdJitterMaxDelay_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,7),_CMediaGwCcCfgVbdJitterMaxDelay_Type())
cMediaGwCcCfgVbdJitterMaxDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterMaxDelay.setStatus(_B)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterMaxDelay.setUnits(_S)
class _CMediaGwCcCfgVbdJitterNomDelay_Type(Unsigned32):defaultValue=70;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,135))
_CMediaGwCcCfgVbdJitterNomDelay_Type.__name__=_H
_CMediaGwCcCfgVbdJitterNomDelay_Object=MibTableColumn
cMediaGwCcCfgVbdJitterNomDelay=_CMediaGwCcCfgVbdJitterNomDelay_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,8),_CMediaGwCcCfgVbdJitterNomDelay_Type())
cMediaGwCcCfgVbdJitterNomDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterNomDelay.setStatus(_B)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterNomDelay.setUnits(_S)
class _CMediaGwCcCfgVbdJitterMinDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,135))
_CMediaGwCcCfgVbdJitterMinDelay_Type.__name__=_H
_CMediaGwCcCfgVbdJitterMinDelay_Object=MibTableColumn
cMediaGwCcCfgVbdJitterMinDelay=_CMediaGwCcCfgVbdJitterMinDelay_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,9),_CMediaGwCcCfgVbdJitterMinDelay_Type())
cMediaGwCcCfgVbdJitterMinDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterMinDelay.setStatus(_B)
if mibBuilder.loadTexts:cMediaGwCcCfgVbdJitterMinDelay.setUnits(_S)
class _CMediaGwCcCfgDefaultTonePlanId_Type(CVoiceTonePlanIndex):defaultValue=1
_CMediaGwCcCfgDefaultTonePlanId_Type.__name__=_AA
_CMediaGwCcCfgDefaultTonePlanId_Object=MibTableColumn
cMediaGwCcCfgDefaultTonePlanId=_CMediaGwCcCfgDefaultTonePlanId_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,10),_CMediaGwCcCfgDefaultTonePlanId_Type())
cMediaGwCcCfgDefaultTonePlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgDefaultTonePlanId.setStatus(_B)
class _CMediaGwCcCfgDescrInfoEnabled_Type(TruthValue):defaultValue=2
_CMediaGwCcCfgDescrInfoEnabled_Type.__name__=_K
_CMediaGwCcCfgDescrInfoEnabled_Object=MibTableColumn
cMediaGwCcCfgDescrInfoEnabled=_CMediaGwCcCfgDescrInfoEnabled_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,11),_CMediaGwCcCfgDescrInfoEnabled_Type())
cMediaGwCcCfgDescrInfoEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgDescrInfoEnabled.setStatus(_B)
class _CMediaGwCcCfgDsNamePrefix_Type(SnmpAdminString):defaultHexValue='4453';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CMediaGwCcCfgDsNamePrefix_Type.__name__=_G
_CMediaGwCcCfgDsNamePrefix_Object=MibTableColumn
cMediaGwCcCfgDsNamePrefix=_CMediaGwCcCfgDsNamePrefix_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,12),_CMediaGwCcCfgDsNamePrefix_Type())
cMediaGwCcCfgDsNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgDsNamePrefix.setStatus(_B)
class _CMediaGwCcCfgRtpNamePrefix_Type(SnmpAdminString):defaultHexValue='525450';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CMediaGwCcCfgRtpNamePrefix_Type.__name__=_G
_CMediaGwCcCfgRtpNamePrefix_Object=MibTableColumn
cMediaGwCcCfgRtpNamePrefix=_CMediaGwCcCfgRtpNamePrefix_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,13),_CMediaGwCcCfgRtpNamePrefix_Type())
cMediaGwCcCfgRtpNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgRtpNamePrefix.setStatus(_B)
class _CMediaGwCcCfgAal1SvcNamePrefix_Type(SnmpAdminString):defaultHexValue='41414C312F535643';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CMediaGwCcCfgAal1SvcNamePrefix_Type.__name__=_G
_CMediaGwCcCfgAal1SvcNamePrefix_Object=MibTableColumn
cMediaGwCcCfgAal1SvcNamePrefix=_CMediaGwCcCfgAal1SvcNamePrefix_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,14),_CMediaGwCcCfgAal1SvcNamePrefix_Type())
cMediaGwCcCfgAal1SvcNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgAal1SvcNamePrefix.setStatus(_B)
class _CMediaGwCcCfgAal2SvcNamePrefix_Type(SnmpAdminString):defaultHexValue='41414C322F535643';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CMediaGwCcCfgAal2SvcNamePrefix_Type.__name__=_G
_CMediaGwCcCfgAal2SvcNamePrefix_Object=MibTableColumn
cMediaGwCcCfgAal2SvcNamePrefix=_CMediaGwCcCfgAal2SvcNamePrefix_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,15),_CMediaGwCcCfgAal2SvcNamePrefix_Type())
cMediaGwCcCfgAal2SvcNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgAal2SvcNamePrefix.setStatus(_B)
class _CMediaGwCcCfgClusterEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('enabled',2),('conditionalEnabled',3)))
_CMediaGwCcCfgClusterEnabled_Type.__name__=_D
_CMediaGwCcCfgClusterEnabled_Object=MibTableColumn
cMediaGwCcCfgClusterEnabled=_CMediaGwCcCfgClusterEnabled_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,16),_CMediaGwCcCfgClusterEnabled_Type())
cMediaGwCcCfgClusterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgClusterEnabled.setStatus(_B)
class _CMediaGwCcCfgDefBearerTraffic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipPvcAal5',1),('atmPvcAal2',2),('atmSvcAal2',3),('atmSvcAal1',4)))
_CMediaGwCcCfgDefBearerTraffic_Type.__name__=_D
_CMediaGwCcCfgDefBearerTraffic_Object=MibTableColumn
cMediaGwCcCfgDefBearerTraffic=_CMediaGwCcCfgDefBearerTraffic_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,17),_CMediaGwCcCfgDefBearerTraffic_Type())
cMediaGwCcCfgDefBearerTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgDefBearerTraffic.setStatus(_B)
class _CMediaGwCcCfgDefRtpNamePrefix_Type(SnmpAdminString):defaultHexValue='544757525450';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CMediaGwCcCfgDefRtpNamePrefix_Type.__name__=_G
_CMediaGwCcCfgDefRtpNamePrefix_Object=MibTableColumn
cMediaGwCcCfgDefRtpNamePrefix=_CMediaGwCcCfgDefRtpNamePrefix_Object((1,3,6,1,4,1,9,9,324,1,1,7,1,18),_CMediaGwCcCfgDefRtpNamePrefix_Type())
cMediaGwCcCfgDefRtpNamePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:cMediaGwCcCfgDefRtpNamePrefix.setStatus(_B)
_CMediaGwStats_ObjectIdentity=ObjectIdentity
cMediaGwStats=_CMediaGwStats_ObjectIdentity((1,3,6,1,4,1,9,9,324,1,2))
_CMediaGwRscStatsTable_Object=MibTable
cMediaGwRscStatsTable=_CMediaGwRscStatsTable_Object((1,3,6,1,4,1,9,9,324,1,2,1))
if mibBuilder.loadTexts:cMediaGwRscStatsTable.setStatus(_B)
_CMediaGwRscStatsEntry_Object=MibTableRow
cMediaGwRscStatsEntry=_CMediaGwRscStatsEntry_Object((1,3,6,1,4,1,9,9,324,1,2,1,1))
cMediaGwRscStatsEntry.setIndexNames((0,_A,_I),(0,_A,_AB))
if mibBuilder.loadTexts:cMediaGwRscStatsEntry.setStatus(_B)
class _CmgwRscStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('cpu',1),('staticmemory',2),('dynamicmemory',3),('sysmemory',4),('commbuffer',5),('msgq',6),('atmq',7),('svccongestion',8),('rsvpq',9),('dspq',10),('h248congestion',11),('callpersec',12),('smallipcbuffer',13),('mediumipcbuffer',14),('largeipcbuffer',15),('hugeipcbuffer',16),('mblkipcbuffer',17)))
_CmgwRscStatsIndex_Type.__name__=_D
_CmgwRscStatsIndex_Object=MibTableColumn
cmgwRscStatsIndex=_CmgwRscStatsIndex_Object((1,3,6,1,4,1,9,9,324,1,2,1,1,1),_CmgwRscStatsIndex_Type())
cmgwRscStatsIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cmgwRscStatsIndex.setStatus(_B)
_CmgwRscMaximumUtilization_Type=Gauge32
_CmgwRscMaximumUtilization_Object=MibTableColumn
cmgwRscMaximumUtilization=_CmgwRscMaximumUtilization_Object((1,3,6,1,4,1,9,9,324,1,2,1,1,2),_CmgwRscMaximumUtilization_Type())
cmgwRscMaximumUtilization.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwRscMaximumUtilization.setStatus(_B)
_CmgwRscMinimumUtilization_Type=Gauge32
_CmgwRscMinimumUtilization_Object=MibTableColumn
cmgwRscMinimumUtilization=_CmgwRscMinimumUtilization_Object((1,3,6,1,4,1,9,9,324,1,2,1,1,3),_CmgwRscMinimumUtilization_Type())
cmgwRscMinimumUtilization.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwRscMinimumUtilization.setStatus(_B)
_CmgwRscAverageUtilization_Type=Gauge32
_CmgwRscAverageUtilization_Object=MibTableColumn
cmgwRscAverageUtilization=_CmgwRscAverageUtilization_Object((1,3,6,1,4,1,9,9,324,1,2,1,1,4),_CmgwRscAverageUtilization_Type())
cmgwRscAverageUtilization.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwRscAverageUtilization.setStatus(_B)
_CmgwRscSinceLastReset_Type=Unsigned32
_CmgwRscSinceLastReset_Object=MibTableColumn
cmgwRscSinceLastReset=_CmgwRscSinceLastReset_Object((1,3,6,1,4,1,9,9,324,1,2,1,1,5),_CmgwRscSinceLastReset_Type())
cmgwRscSinceLastReset.setMaxAccess(_F)
if mibBuilder.loadTexts:cmgwRscSinceLastReset.setStatus(_B)
if mibBuilder.loadTexts:cmgwRscSinceLastReset.setUnits('seconds')
_CMediaGwMIBConformance_ObjectIdentity=ObjectIdentity
cMediaGwMIBConformance=_CMediaGwMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,324,2))
_CMediaGwMIBCompliances_ObjectIdentity=ObjectIdentity
cMediaGwMIBCompliances=_CMediaGwMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,324,2,1))
_CMediaGwMIBGroups_ObjectIdentity=ObjectIdentity
cMediaGwMIBGroups=_CMediaGwMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,324,2,2))
cMediaGwGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,1))
cMediaGwGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cMediaGwGroup.setStatus(_J)
cmgwSignalProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,2))
cmgwSignalProtocolGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cmgwSignalProtocolGroup.setStatus(_J)
cmgwDomainNameGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,3))
cmgwDomainNameGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:cmgwDomainNameGroup.setStatus(_B)
cMediaGwIpGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,4))
cMediaGwIpGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cMediaGwIpGroup.setStatus(_B)
cmgwDnsIpGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,5))
cmgwDnsIpGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cmgwDnsIpGroup.setStatus(_B)
cmgwLifGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,6))
cmgwLifGroup.setObjects(*((_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:cmgwLifGroup.setStatus(_B)
cmgwCallControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,7))
cmgwCallControlGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cmgwCallControlGroup.setStatus(_J)
cMediaGwGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,8))
cMediaGwGroupRev1.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_x)))
if mibBuilder.loadTexts:cMediaGwGroupRev1.setStatus(_B)
cmgwCallControlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,9))
cmgwCallControlGroupRev1.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_y)))
if mibBuilder.loadTexts:cmgwCallControlGroupRev1.setStatus(_B)
cmgwSignalProtocolGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,10))
cmgwSignalProtocolGroupRev1.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_z)))
if mibBuilder.loadTexts:cmgwSignalProtocolGroupRev1.setStatus(_J)
cmgwSignalProtocolGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,11))
cmgwSignalProtocolGroupRev2.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_z),(_A,_AU)))
if mibBuilder.loadTexts:cmgwSignalProtocolGroupRev2.setStatus(_B)
cmgwSignalProtocolGroupRev3=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,12))
cmgwSignalProtocolGroupRev3.setObjects((_A,_AV))
if mibBuilder.loadTexts:cmgwSignalProtocolGroupRev3.setStatus(_B)
cMediaGwRscStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,13))
cMediaGwRscStatsGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:cMediaGwRscStatsGroup.setStatus(_B)
cMediaGwGroupExtra=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,14))
cMediaGwGroupExtra.setObjects(*((_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:cMediaGwGroupExtra.setStatus(_B)
cmgwCallControlGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,15))
cmgwCallControlGroupRev2.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_y),(_A,_Ac)))
if mibBuilder.loadTexts:cmgwCallControlGroupRev2.setStatus(_B)
cMediaGwGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,324,2,2,16))
cMediaGwGroupRev2.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_x),(_A,_Ad)))
if mibBuilder.loadTexts:cMediaGwGroupRev2.setStatus(_B)
cMediaGwMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,1))
cMediaGwMIBCompliance.setObjects(*((_A,_Ae),(_A,_Af),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Ag)))
if mibBuilder.loadTexts:cMediaGwMIBCompliance.setStatus(_J)
cMediaGwMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,2))
cMediaGwMIBComplianceRev1.setObjects(*((_A,_Q),(_A,_Ah),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_r)))
if mibBuilder.loadTexts:cMediaGwMIBComplianceRev1.setStatus(_J)
cMediaGwMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,3))
cMediaGwMIBComplianceRev2.setObjects(*((_A,_Q),(_A,_R),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_r)))
if mibBuilder.loadTexts:cMediaGwMIBComplianceRev2.setStatus(_J)
cMediaGwMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,4))
cMediaGwMIBComplianceRev3.setObjects(*((_A,_Q),(_A,_s),(_A,_R),(_A,_t),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_r),(_A,_u)))
if mibBuilder.loadTexts:cMediaGwMIBComplianceRev3.setStatus(_B)
cMediaGwMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,5))
cMediaGwMIBComplianceRev4.setObjects(*((_A,_Q),(_A,_s),(_A,_R),(_A,_t),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_A0),(_A,_u)))
if mibBuilder.loadTexts:cMediaGwMIBComplianceRev4.setStatus(_J)
cMediaGwMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,324,2,1,6))
cMediaGwMIBComplianceRev5.setObjects(*((_A,_Q),(_A,_s),(_A,_Ai),(_A,_R),(_A,_t),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_A0),(_A,_u)))
if mibBuilder.loadTexts:cMediaGwMIBComplianceRev5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CGwServiceState':CGwServiceState,'CGwAdminState':CGwAdminState,'GatewayLifNumber':GatewayLifNumber,_AA:CVoiceTonePlanIndex,'CVoiceTonePlanIndexOrZero':CVoiceTonePlanIndexOrZero,'CCallControlProfileIndex':CCallControlProfileIndex,'CCallControlProfileIndexOrZero':CCallControlProfileIndexOrZero,_A9:CCallControlJitterDelayMode,'ciscoMediaGatewayMIB':ciscoMediaGatewayMIB,'ciscoMediaGatewayMIBNotifs':ciscoMediaGatewayMIBNotifs,'ciscoMediaGatewayMIBObjects':ciscoMediaGatewayMIBObjects,'cMediaGwConfig':cMediaGwConfig,'cMediaGwTable':cMediaGwTable,'cMediaGwEntry':cMediaGwEntry,_I:cmgwIndex,_T:cmgwDomainName,_U:cmgwPhysicalIndex,_V:cmgwServiceState,_W:cmgwAdminState,_X:cmgwGraceTime,_x:cmgwVtMappingMode,_Aa:cmgwSrcFilterEnabled,_Ab:cmgwLawInterceptEnabled,_Ad:cmgwV23Enabled,'cmgwSignalProtocolTable':cmgwSignalProtocolTable,'cmgwSignalProtocolEntry':cmgwSignalProtocolEntry,_A4:cmgwSignalProtocolIndex,_Y:cmgwSignalProtocol,_Z:cmgwSignalProtocolVersion,_a:cmgwSignalProtocolPort,_z:cmgwSignalMgcProtocolPort,_AU:cmgwSignalProtocolPreference,_AV:cmgwSignalProtocolConfigVer,'cMediaGwIpConfigTable':cMediaGwIpConfigTable,'cMediaGwIpConfigEntry':cMediaGwIpConfigEntry,_A5:cmgwIpConfigIndex,_AF:cmgwIpConfigIfIndex,_AG:cmgwIpConfigVpi,_AH:cmgwIpConfigVci,_AI:cmgwIpConfigAddrType,_AJ:cmgwIpConfigAddress,_AK:cmgwIpConfigSubnetMask,_AL:cmgwIpConfigDefaultGwIp,_AM:cmgwIpConfigForRemoteMapping,_AN:cmgwIpConfigRowStatus,'cMediaGwDomainNameConfigTable':cMediaGwDomainNameConfigTable,'cMediaGwDomainNameConfigEntry':cMediaGwDomainNameConfigEntry,_A6:cmgwConfigDomainNameIndex,_AC:cmgwConfigDomainNameEntity,_AD:cmgwConfigDomainName,_AE:cmgwConfigDomainNameRowStatus,'cMediaGwDnsIpConfigTable':cMediaGwDnsIpConfigTable,'cMediaGwDnsIpConfigEntry':cMediaGwDnsIpConfigEntry,_A7:cmgwDnsIpIndex,_AO:cmgwDnsDomainName,_AQ:cmgwDnsIpType,_AP:cmgwDnsIp,_AR:cmgwDnsIpRowStatus,'cmgwLifTable':cmgwLifTable,'cmgwLifEntry':cmgwLifEntry,_A8:cmgwLifNumber,_AS:cmgwLifPvcCount,_AT:cmgwLifVoiceIfCount,'cMediaGwCallControlConfigTable':cMediaGwCallControlConfigTable,'cMediaGwCallControlConfigEntry':cMediaGwCallControlConfigEntry,_b:cMediaGwCcCfgControlTos,_c:cMediaGwCcCfgBearerTos,_d:cMediaGwCcCfgNtePayload,_e:cMediaGwCcCfgNsePayload,_f:cMediaGwCcCfgNseRespTimer,_g:cMediaGwCcCfgVbdJitterDelayMode,_h:cMediaGwCcCfgVbdJitterMaxDelay,_i:cMediaGwCcCfgVbdJitterNomDelay,_j:cMediaGwCcCfgVbdJitterMinDelay,_k:cMediaGwCcCfgDefaultTonePlanId,_l:cMediaGwCcCfgDescrInfoEnabled,_m:cMediaGwCcCfgDsNamePrefix,_n:cMediaGwCcCfgRtpNamePrefix,_o:cMediaGwCcCfgAal1SvcNamePrefix,_p:cMediaGwCcCfgAal2SvcNamePrefix,_q:cMediaGwCcCfgClusterEnabled,_y:cMediaGwCcCfgDefBearerTraffic,_Ac:cMediaGwCcCfgDefRtpNamePrefix,'cMediaGwStats':cMediaGwStats,'cMediaGwRscStatsTable':cMediaGwRscStatsTable,'cMediaGwRscStatsEntry':cMediaGwRscStatsEntry,_AB:cmgwRscStatsIndex,_AW:cmgwRscMaximumUtilization,_AX:cmgwRscMinimumUtilization,_AY:cmgwRscAverageUtilization,_AZ:cmgwRscSinceLastReset,'cMediaGwMIBConformance':cMediaGwMIBConformance,'cMediaGwMIBCompliances':cMediaGwMIBCompliances,'cMediaGwMIBCompliance':cMediaGwMIBCompliance,'cMediaGwMIBComplianceRev1':cMediaGwMIBComplianceRev1,'cMediaGwMIBComplianceRev2':cMediaGwMIBComplianceRev2,'cMediaGwMIBComplianceRev3':cMediaGwMIBComplianceRev3,'cMediaGwMIBComplianceRev4':cMediaGwMIBComplianceRev4,'cMediaGwMIBComplianceRev5':cMediaGwMIBComplianceRev5,'cMediaGwMIBGroups':cMediaGwMIBGroups,_Ae:cMediaGwGroup,_Af:cmgwSignalProtocolGroup,_M:cmgwDomainNameGroup,_N:cMediaGwIpGroup,_O:cmgwDnsIpGroup,_P:cmgwLifGroup,_Ag:cmgwCallControlGroup,_Q:cMediaGwGroupRev1,_r:cmgwCallControlGroupRev1,_Ah:cmgwSignalProtocolGroupRev1,_R:cmgwSignalProtocolGroupRev2,_t:cmgwSignalProtocolGroupRev3,_u:cMediaGwRscStatsGroup,_s:cMediaGwGroupExtra,_A0:cmgwCallControlGroupRev2,_Ai:cMediaGwGroupRev2})