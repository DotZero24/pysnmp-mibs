_P='adGenMgcpEndpointStatusEntryIndex'
_O='adGenMgcpEndpointEntryIndex'
_N='adGenMgcpProfileEntryIndex'
_M='InterfaceIndexOrZero'
_L='not-accessible'
_K='TruthValue'
_J='ifIndex'
_I='IF-MIB'
_H='enbled'
_G='disabled'
_F='ADTRAN-GENMGCP-MIB'
_E='DisplayString'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdGenVoipCodecProfileName,AdGenVoipCodecProfileType,AdGenVoipMediaProfileName=mibBuilder.importSymbols('ADTRAN-GENVOIP-MIB','AdGenVoipCodecProfileName','AdGenVoipCodecProfileType','AdGenVoipMediaProfileName')
adGenMgcp,adGenMgcpID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenMgcp','adGenMgcpID')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,_M,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention',_K)
adGenMgcpEntity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,54,1))
if mibBuilder.loadTexts:adGenMgcpEntity.setRevisions(('2017-02-16 00:00','2014-03-18 00:00','2013-07-18 00:00','2013-05-23 00:00','2013-01-21 00:00'))
class AdGenMgcpProfileName(TextualConvention,OctetString):status=_A;displayHint='40a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AdGenMgcpProvisioning_ObjectIdentity=ObjectIdentity
adGenMgcpProvisioning=_AdGenMgcpProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,1))
_AdGenMgcpProfileProv_ObjectIdentity=ObjectIdentity
adGenMgcpProfileProv=_AdGenMgcpProfileProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,1,1))
_AdGenMgcpProfileProvCurrentNumber_Type=Integer32
_AdGenMgcpProfileProvCurrentNumber_Object=MibScalar
adGenMgcpProfileProvCurrentNumber=_AdGenMgcpProfileProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,54,1,1,1),_AdGenMgcpProfileProvCurrentNumber_Type())
adGenMgcpProfileProvCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpProfileProvCurrentNumber.setStatus(_A)
_AdGenMgcpProfileProvLastCreateError_Type=DisplayString
_AdGenMgcpProfileProvLastCreateError_Object=MibScalar
adGenMgcpProfileProvLastCreateError=_AdGenMgcpProfileProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,54,1,1,2),_AdGenMgcpProfileProvLastCreateError_Type())
adGenMgcpProfileProvLastCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpProfileProvLastCreateError.setStatus(_A)
_AdGenMgcpProfileProvTable_Object=MibTable
adGenMgcpProfileProvTable=_AdGenMgcpProfileProvTable_Object((1,3,6,1,4,1,664,5,70,54,1,1,3))
if mibBuilder.loadTexts:adGenMgcpProfileProvTable.setStatus(_A)
_AdGenMgcpProfileProvEntry_Object=MibTableRow
adGenMgcpProfileProvEntry=_AdGenMgcpProfileProvEntry_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1))
adGenMgcpProfileProvEntry.setIndexNames((1,_F,_N))
if mibBuilder.loadTexts:adGenMgcpProfileProvEntry.setStatus(_A)
_AdGenMgcpProfileEntryIndex_Type=AdGenMgcpProfileName
_AdGenMgcpProfileEntryIndex_Object=MibTableColumn
adGenMgcpProfileEntryIndex=_AdGenMgcpProfileEntryIndex_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,1),_AdGenMgcpProfileEntryIndex_Type())
adGenMgcpProfileEntryIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenMgcpProfileEntryIndex.setStatus(_A)
_AdGenMgcpProfileRowStatus_Type=RowStatus
_AdGenMgcpProfileRowStatus_Object=MibTableColumn
adGenMgcpProfileRowStatus=_AdGenMgcpProfileRowStatus_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,2),_AdGenMgcpProfileRowStatus_Type())
adGenMgcpProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileRowStatus.setStatus(_A)
_AdGenMgcpProfileLastErrorString_Type=DisplayString
_AdGenMgcpProfileLastErrorString_Object=MibTableColumn
adGenMgcpProfileLastErrorString=_AdGenMgcpProfileLastErrorString_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,3),_AdGenMgcpProfileLastErrorString_Type())
adGenMgcpProfileLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpProfileLastErrorString.setStatus(_A)
_AdGenMgcpProfileCallAgentPrimary_Type=DisplayString
_AdGenMgcpProfileCallAgentPrimary_Object=MibTableColumn
adGenMgcpProfileCallAgentPrimary=_AdGenMgcpProfileCallAgentPrimary_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,4),_AdGenMgcpProfileCallAgentPrimary_Type())
adGenMgcpProfileCallAgentPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileCallAgentPrimary.setStatus(_A)
class _AdGenMgcpProfileCallAgentPrimaryUdp_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenMgcpProfileCallAgentPrimaryUdp_Type.__name__=_C
_AdGenMgcpProfileCallAgentPrimaryUdp_Object=MibTableColumn
adGenMgcpProfileCallAgentPrimaryUdp=_AdGenMgcpProfileCallAgentPrimaryUdp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,5),_AdGenMgcpProfileCallAgentPrimaryUdp_Type())
adGenMgcpProfileCallAgentPrimaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileCallAgentPrimaryUdp.setStatus(_A)
_AdGenMgcpProfileCallAgentSecondary_Type=DisplayString
_AdGenMgcpProfileCallAgentSecondary_Object=MibTableColumn
adGenMgcpProfileCallAgentSecondary=_AdGenMgcpProfileCallAgentSecondary_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,6),_AdGenMgcpProfileCallAgentSecondary_Type())
adGenMgcpProfileCallAgentSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileCallAgentSecondary.setStatus(_A)
class _AdGenMgcpProfileCallAgentSecondaryUdp_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenMgcpProfileCallAgentSecondaryUdp_Type.__name__=_C
_AdGenMgcpProfileCallAgentSecondaryUdp_Object=MibTableColumn
adGenMgcpProfileCallAgentSecondaryUdp=_AdGenMgcpProfileCallAgentSecondaryUdp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,7),_AdGenMgcpProfileCallAgentSecondaryUdp_Type())
adGenMgcpProfileCallAgentSecondaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileCallAgentSecondaryUdp.setStatus(_A)
class _AdGenMgcpProfileShutdown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noShutdown',1),('shutdown',2)))
_AdGenMgcpProfileShutdown_Type.__name__=_C
_AdGenMgcpProfileShutdown_Object=MibTableColumn
adGenMgcpProfileShutdown=_AdGenMgcpProfileShutdown_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,8),_AdGenMgcpProfileShutdown_Type())
adGenMgcpProfileShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileShutdown.setStatus(_A)
class _AdGenMgcpProfileBracketedIp_Type(TruthValue):defaultValue=1
_AdGenMgcpProfileBracketedIp_Type.__name__=_K
_AdGenMgcpProfileBracketedIp_Object=MibTableColumn
adGenMgcpProfileBracketedIp=_AdGenMgcpProfileBracketedIp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,9),_AdGenMgcpProfileBracketedIp_Type())
adGenMgcpProfileBracketedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileBracketedIp.setStatus(_A)
class _AdGenMgcpProfileStandard_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rfc3435',1),('ncs',2)))
_AdGenMgcpProfileStandard_Type.__name__=_C
_AdGenMgcpProfileStandard_Object=MibTableColumn
adGenMgcpProfileStandard=_AdGenMgcpProfileStandard_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,10),_AdGenMgcpProfileStandard_Type())
adGenMgcpProfileStandard.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileStandard.setStatus(_A)
class _AdGenMgcpProfileMgcpDscp_Type(Integer32):defaultValue=46;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenMgcpProfileMgcpDscp_Type.__name__=_C
_AdGenMgcpProfileMgcpDscp_Object=MibTableColumn
adGenMgcpProfileMgcpDscp=_AdGenMgcpProfileMgcpDscp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,11),_AdGenMgcpProfileMgcpDscp_Type())
adGenMgcpProfileMgcpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileMgcpDscp.setStatus(_A)
class _AdGenMgcpProfileRtpDscp_Type(Integer32):defaultValue=46;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenMgcpProfileRtpDscp_Type.__name__=_C
_AdGenMgcpProfileRtpDscp_Object=MibTableColumn
adGenMgcpProfileRtpDscp=_AdGenMgcpProfileRtpDscp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,12),_AdGenMgcpProfileRtpDscp_Type())
adGenMgcpProfileRtpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileRtpDscp.setStatus(_A)
class _AdGenMgcpProfileGatewayUdp_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenMgcpProfileGatewayUdp_Type.__name__=_C
_AdGenMgcpProfileGatewayUdp_Object=MibTableColumn
adGenMgcpProfileGatewayUdp=_AdGenMgcpProfileGatewayUdp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,13),_AdGenMgcpProfileGatewayUdp_Type())
adGenMgcpProfileGatewayUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileGatewayUdp.setStatus(_A)
class _AdGenMgcpProfileRtpUdpOffset_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenMgcpProfileRtpUdpOffset_Type.__name__=_C
_AdGenMgcpProfileRtpUdpOffset_Object=MibTableColumn
adGenMgcpProfileRtpUdpOffset=_AdGenMgcpProfileRtpUdpOffset_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,14),_AdGenMgcpProfileRtpUdpOffset_Type())
adGenMgcpProfileRtpUdpOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileRtpUdpOffset.setStatus(_A)
class _AdGenMgcpProfilePersistentNotifyHangDown_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AdGenMgcpProfilePersistentNotifyHangDown_Type.__name__=_C
_AdGenMgcpProfilePersistentNotifyHangDown_Object=MibTableColumn
adGenMgcpProfilePersistentNotifyHangDown=_AdGenMgcpProfilePersistentNotifyHangDown_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,15),_AdGenMgcpProfilePersistentNotifyHangDown_Type())
adGenMgcpProfilePersistentNotifyHangDown.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfilePersistentNotifyHangDown.setStatus(_A)
class _AdGenMgcpProfilePersistentNotifyHangUp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AdGenMgcpProfilePersistentNotifyHangUp_Type.__name__=_C
_AdGenMgcpProfilePersistentNotifyHangUp_Object=MibTableColumn
adGenMgcpProfilePersistentNotifyHangUp=_AdGenMgcpProfilePersistentNotifyHangUp_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,16),_AdGenMgcpProfilePersistentNotifyHangUp_Type())
adGenMgcpProfilePersistentNotifyHangUp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfilePersistentNotifyHangUp.setStatus(_A)
class _AdGenMgcpProfilePersistentNotifyHookFlash_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AdGenMgcpProfilePersistentNotifyHookFlash_Type.__name__=_C
_AdGenMgcpProfilePersistentNotifyHookFlash_Object=MibTableColumn
adGenMgcpProfilePersistentNotifyHookFlash=_AdGenMgcpProfilePersistentNotifyHookFlash_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,17),_AdGenMgcpProfilePersistentNotifyHookFlash_Type())
adGenMgcpProfilePersistentNotifyHookFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfilePersistentNotifyHookFlash.setStatus(_A)
class _AdGenMgcpProfileRetransmitDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('exponentialBackoff',1),('ms100',2),('ms250',3),('ms500',4),('sec1',5),('sec2',6),('sec4',7)))
_AdGenMgcpProfileRetransmitDelay_Type.__name__=_C
_AdGenMgcpProfileRetransmitDelay_Object=MibTableColumn
adGenMgcpProfileRetransmitDelay=_AdGenMgcpProfileRetransmitDelay_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,18),_AdGenMgcpProfileRetransmitDelay_Type())
adGenMgcpProfileRetransmitDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileRetransmitDelay.setStatus(_A)
class _AdGenMgcpProfileMax1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenMgcpProfileMax1_Type.__name__=_C
_AdGenMgcpProfileMax1_Object=MibTableColumn
adGenMgcpProfileMax1=_AdGenMgcpProfileMax1_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,19),_AdGenMgcpProfileMax1_Type())
adGenMgcpProfileMax1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileMax1.setStatus(_A)
class _AdGenMgcpProfileMax2_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AdGenMgcpProfileMax2_Type.__name__=_C
_AdGenMgcpProfileMax2_Object=MibTableColumn
adGenMgcpProfileMax2=_AdGenMgcpProfileMax2_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,20),_AdGenMgcpProfileMax2_Type())
adGenMgcpProfileMax2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileMax2.setStatus(_A)
class _AdGenMgcpProfileLocalDomainType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mediaGateway',1),('userDefined',2)))
_AdGenMgcpProfileLocalDomainType_Type.__name__=_C
_AdGenMgcpProfileLocalDomainType_Object=MibTableColumn
adGenMgcpProfileLocalDomainType=_AdGenMgcpProfileLocalDomainType_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,21),_AdGenMgcpProfileLocalDomainType_Type())
adGenMgcpProfileLocalDomainType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileLocalDomainType.setStatus(_A)
class _AdGenMgcpProfileLocalDomainAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenMgcpProfileLocalDomainAddress_Type.__name__=_E
_AdGenMgcpProfileLocalDomainAddress_Object=MibTableColumn
adGenMgcpProfileLocalDomainAddress=_AdGenMgcpProfileLocalDomainAddress_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,22),_AdGenMgcpProfileLocalDomainAddress_Type())
adGenMgcpProfileLocalDomainAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileLocalDomainAddress.setStatus(_A)
class _AdGenMgcpProfileTerminationIdBase_Type(DisplayString):defaultValue=OctetString('aaln/');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_AdGenMgcpProfileTerminationIdBase_Type.__name__=_E
_AdGenMgcpProfileTerminationIdBase_Object=MibTableColumn
adGenMgcpProfileTerminationIdBase=_AdGenMgcpProfileTerminationIdBase_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,23),_AdGenMgcpProfileTerminationIdBase_Type())
adGenMgcpProfileTerminationIdBase.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileTerminationIdBase.setStatus(_A)
class _AdGenMgcpProfileRFC2833Signaling_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AdGenMgcpProfileRFC2833Signaling_Type.__name__=_C
_AdGenMgcpProfileRFC2833Signaling_Object=MibTableColumn
adGenMgcpProfileRFC2833Signaling=_AdGenMgcpProfileRFC2833Signaling_Object((1,3,6,1,4,1,664,5,70,54,1,1,3,1,24),_AdGenMgcpProfileRFC2833Signaling_Type())
adGenMgcpProfileRFC2833Signaling.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpProfileRFC2833Signaling.setStatus(_A)
_AdGenMgcpEndpointProv_ObjectIdentity=ObjectIdentity
adGenMgcpEndpointProv=_AdGenMgcpEndpointProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,1,2))
_AdGenMgcpEndpointProvCurrentNumber_Type=Integer32
_AdGenMgcpEndpointProvCurrentNumber_Object=MibScalar
adGenMgcpEndpointProvCurrentNumber=_AdGenMgcpEndpointProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,54,1,2,1),_AdGenMgcpEndpointProvCurrentNumber_Type())
adGenMgcpEndpointProvCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointProvCurrentNumber.setStatus(_A)
_AdGenMgcpEndpointProvLastCreateError_Type=DisplayString
_AdGenMgcpEndpointProvLastCreateError_Object=MibScalar
adGenMgcpEndpointProvLastCreateError=_AdGenMgcpEndpointProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,54,1,2,2),_AdGenMgcpEndpointProvLastCreateError_Type())
adGenMgcpEndpointProvLastCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointProvLastCreateError.setStatus(_A)
_AdGenMgcpEndpointProvTable_Object=MibTable
adGenMgcpEndpointProvTable=_AdGenMgcpEndpointProvTable_Object((1,3,6,1,4,1,664,5,70,54,1,2,3))
if mibBuilder.loadTexts:adGenMgcpEndpointProvTable.setStatus(_A)
_AdGenMgcpEndpointProvEntry_Object=MibTableRow
adGenMgcpEndpointProvEntry=_AdGenMgcpEndpointProvEntry_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1))
adGenMgcpEndpointProvEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:adGenMgcpEndpointProvEntry.setStatus(_A)
_AdGenMgcpEndpointEntryIndex_Type=InterfaceIndexOrZero
_AdGenMgcpEndpointEntryIndex_Object=MibTableColumn
adGenMgcpEndpointEntryIndex=_AdGenMgcpEndpointEntryIndex_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,1),_AdGenMgcpEndpointEntryIndex_Type())
adGenMgcpEndpointEntryIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenMgcpEndpointEntryIndex.setStatus(_A)
_AdGenMgcpEndpointRowStatus_Type=RowStatus
_AdGenMgcpEndpointRowStatus_Object=MibTableColumn
adGenMgcpEndpointRowStatus=_AdGenMgcpEndpointRowStatus_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,2),_AdGenMgcpEndpointRowStatus_Type())
adGenMgcpEndpointRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointRowStatus.setStatus(_A)
_AdGenMgcpEndpointLastErrorString_Type=DisplayString
_AdGenMgcpEndpointLastErrorString_Object=MibTableColumn
adGenMgcpEndpointLastErrorString=_AdGenMgcpEndpointLastErrorString_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,3),_AdGenMgcpEndpointLastErrorString_Type())
adGenMgcpEndpointLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointLastErrorString.setStatus(_A)
class _AdGenMgcpEndpointFxsPort_Type(InterfaceIndexOrZero):defaultValue=0
_AdGenMgcpEndpointFxsPort_Type.__name__=_M
_AdGenMgcpEndpointFxsPort_Object=MibTableColumn
adGenMgcpEndpointFxsPort=_AdGenMgcpEndpointFxsPort_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,4),_AdGenMgcpEndpointFxsPort_Type())
adGenMgcpEndpointFxsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointFxsPort.setStatus(_A)
_AdGenMgcpEndpointMgcpProfile_Type=AdGenMgcpProfileName
_AdGenMgcpEndpointMgcpProfile_Object=MibTableColumn
adGenMgcpEndpointMgcpProfile=_AdGenMgcpEndpointMgcpProfile_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,5),_AdGenMgcpEndpointMgcpProfile_Type())
adGenMgcpEndpointMgcpProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointMgcpProfile.setStatus(_A)
class _AdGenMgcpEndpointBlockCallerId_Type(TruthValue):defaultValue=1
_AdGenMgcpEndpointBlockCallerId_Type.__name__=_K
_AdGenMgcpEndpointBlockCallerId_Object=MibTableColumn
adGenMgcpEndpointBlockCallerId=_AdGenMgcpEndpointBlockCallerId_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,6),_AdGenMgcpEndpointBlockCallerId_Type())
adGenMgcpEndpointBlockCallerId.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointBlockCallerId.setStatus(_A)
class _AdGenMgcpEndpointDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenMgcpEndpointDescription_Type.__name__=_E
_AdGenMgcpEndpointDescription_Object=MibTableColumn
adGenMgcpEndpointDescription=_AdGenMgcpEndpointDescription_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,7),_AdGenMgcpEndpointDescription_Type())
adGenMgcpEndpointDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointDescription.setStatus(_A)
class _AdGenMgcpEndpointDisplayString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenMgcpEndpointDisplayString_Type.__name__=_E
_AdGenMgcpEndpointDisplayString_Object=MibTableColumn
adGenMgcpEndpointDisplayString=_AdGenMgcpEndpointDisplayString_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,8),_AdGenMgcpEndpointDisplayString_Type())
adGenMgcpEndpointDisplayString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointDisplayString.setStatus(_A)
class _AdGenMgcpEndpointFwdDisconnect_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('delay250',1),('delay500',2),('delay750',3),('delay900',4),('delay1000',5),('delay2000',6)))
_AdGenMgcpEndpointFwdDisconnect_Type.__name__=_C
_AdGenMgcpEndpointFwdDisconnect_Object=MibTableColumn
adGenMgcpEndpointFwdDisconnect=_AdGenMgcpEndpointFwdDisconnect_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,9),_AdGenMgcpEndpointFwdDisconnect_Type())
adGenMgcpEndpointFwdDisconnect.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointFwdDisconnect.setStatus(_A)
if mibBuilder.loadTexts:adGenMgcpEndpointFwdDisconnect.setUnits('milliseconds')
_AdGenMgcpEndpointMediaProfile_Type=AdGenVoipMediaProfileName
_AdGenMgcpEndpointMediaProfile_Object=MibTableColumn
adGenMgcpEndpointMediaProfile=_AdGenMgcpEndpointMediaProfile_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,10),_AdGenMgcpEndpointMediaProfile_Type())
adGenMgcpEndpointMediaProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointMediaProfile.setStatus(_A)
_AdGenMgcpEndpointCodecListProfile_Type=AdGenVoipCodecProfileName
_AdGenMgcpEndpointCodecListProfile_Object=MibTableColumn
adGenMgcpEndpointCodecListProfile=_AdGenMgcpEndpointCodecListProfile_Object((1,3,6,1,4,1,664,5,70,54,1,2,3,1,11),_AdGenMgcpEndpointCodecListProfile_Type())
adGenMgcpEndpointCodecListProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenMgcpEndpointCodecListProfile.setStatus(_A)
_AdGenMgcpStatus_ObjectIdentity=ObjectIdentity
adGenMgcpStatus=_AdGenMgcpStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,2))
_AdGenMgcpEndpointStatus_ObjectIdentity=ObjectIdentity
adGenMgcpEndpointStatus=_AdGenMgcpEndpointStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,2,1))
_AdGenMgcpEndpointStatusTable_Object=MibTable
adGenMgcpEndpointStatusTable=_AdGenMgcpEndpointStatusTable_Object((1,3,6,1,4,1,664,5,70,54,2,1,1))
if mibBuilder.loadTexts:adGenMgcpEndpointStatusTable.setStatus(_A)
_AdGenMgcpEndpointStatusEntry_Object=MibTableRow
adGenMgcpEndpointStatusEntry=_AdGenMgcpEndpointStatusEntry_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1))
adGenMgcpEndpointStatusEntry.setIndexNames((0,_I,_J),(0,_F,_P))
if mibBuilder.loadTexts:adGenMgcpEndpointStatusEntry.setStatus(_A)
_AdGenMgcpEndpointStatusEntryIndex_Type=InterfaceIndexOrZero
_AdGenMgcpEndpointStatusEntryIndex_Object=MibTableColumn
adGenMgcpEndpointStatusEntryIndex=_AdGenMgcpEndpointStatusEntryIndex_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,1),_AdGenMgcpEndpointStatusEntryIndex_Type())
adGenMgcpEndpointStatusEntryIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusEntryIndex.setStatus(_A)
_AdGenMgcpEndpointStatusFXSPort_Type=InterfaceIndexOrZero
_AdGenMgcpEndpointStatusFXSPort_Object=MibTableColumn
adGenMgcpEndpointStatusFXSPort=_AdGenMgcpEndpointStatusFXSPort_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,2),_AdGenMgcpEndpointStatusFXSPort_Type())
adGenMgcpEndpointStatusFXSPort.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusFXSPort.setStatus(_A)
_AdGenMgcpEndpointStatusName_Type=DisplayString
_AdGenMgcpEndpointStatusName_Object=MibTableColumn
adGenMgcpEndpointStatusName=_AdGenMgcpEndpointStatusName_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,3),_AdGenMgcpEndpointStatusName_Type())
adGenMgcpEndpointStatusName.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusName.setStatus(_A)
_AdGenMgcpEndpointStatusConnectedProfile_Type=DisplayString
_AdGenMgcpEndpointStatusConnectedProfile_Object=MibTableColumn
adGenMgcpEndpointStatusConnectedProfile=_AdGenMgcpEndpointStatusConnectedProfile_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,4),_AdGenMgcpEndpointStatusConnectedProfile_Type())
adGenMgcpEndpointStatusConnectedProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusConnectedProfile.setStatus(_A)
class _AdGenMgcpEndpointStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('connected',1),('disconnected',2),('reconnecting',3),('connectedNoRqnt',4)))
_AdGenMgcpEndpointStatusState_Type.__name__=_C
_AdGenMgcpEndpointStatusState_Object=MibTableColumn
adGenMgcpEndpointStatusState=_AdGenMgcpEndpointStatusState_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,5),_AdGenMgcpEndpointStatusState_Type())
adGenMgcpEndpointStatusState.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusState.setStatus(_A)
_AdGenMgcpEndpointStatusStateDetail_Type=DisplayString
_AdGenMgcpEndpointStatusStateDetail_Object=MibTableColumn
adGenMgcpEndpointStatusStateDetail=_AdGenMgcpEndpointStatusStateDetail_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,6),_AdGenMgcpEndpointStatusStateDetail_Type())
adGenMgcpEndpointStatusStateDetail.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusStateDetail.setStatus(_A)
class _AdGenMgcpEndpointOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4)))
_AdGenMgcpEndpointOperStatus_Type.__name__=_C
_AdGenMgcpEndpointOperStatus_Object=MibTableColumn
adGenMgcpEndpointOperStatus=_AdGenMgcpEndpointOperStatus_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,7),_AdGenMgcpEndpointOperStatus_Type())
adGenMgcpEndpointOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointOperStatus.setStatus(_A)
_AdGenMgcpEndpointStatusCodecInUse_Type=AdGenVoipCodecProfileType
_AdGenMgcpEndpointStatusCodecInUse_Object=MibTableColumn
adGenMgcpEndpointStatusCodecInUse=_AdGenMgcpEndpointStatusCodecInUse_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,8),_AdGenMgcpEndpointStatusCodecInUse_Type())
adGenMgcpEndpointStatusCodecInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointStatusCodecInUse.setStatus(_A)
_AdGenMgcpEndpointLastError_Type=DisplayString
_AdGenMgcpEndpointLastError_Object=MibTableColumn
adGenMgcpEndpointLastError=_AdGenMgcpEndpointLastError_Object((1,3,6,1,4,1,664,5,70,54,2,1,1,1,9),_AdGenMgcpEndpointLastError_Type())
adGenMgcpEndpointLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpEndpointLastError.setStatus(_A)
_AdGenMgcpActions_ObjectIdentity=ObjectIdentity
adGenMgcpActions=_AdGenMgcpActions_ObjectIdentity((1,3,6,1,4,1,664,5,70,54,3))
_AdGenMgcpActionsTable_Object=MibTable
adGenMgcpActionsTable=_AdGenMgcpActionsTable_Object((1,3,6,1,4,1,664,5,70,54,3,1))
if mibBuilder.loadTexts:adGenMgcpActionsTable.setStatus(_A)
_AdGenMgcpActionsEntry_Object=MibTableRow
adGenMgcpActionsEntry=_AdGenMgcpActionsEntry_Object((1,3,6,1,4,1,664,5,70,54,3,1,1))
adGenMgcpActionsEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:adGenMgcpActionsEntry.setStatus(_A)
_AdGenMgcpActionsLastError_Type=DisplayString
_AdGenMgcpActionsLastError_Object=MibTableColumn
adGenMgcpActionsLastError=_AdGenMgcpActionsLastError_Object((1,3,6,1,4,1,664,5,70,54,3,1,1,1),_AdGenMgcpActionsLastError_Type())
adGenMgcpActionsLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenMgcpActionsLastError.setStatus(_A)
class _AdGenMgcpActionsRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_AdGenMgcpActionsRestart_Type.__name__=_C
_AdGenMgcpActionsRestart_Object=MibTableColumn
adGenMgcpActionsRestart=_AdGenMgcpActionsRestart_Object((1,3,6,1,4,1,664,5,70,54,3,1,1,2),_AdGenMgcpActionsRestart_Type())
adGenMgcpActionsRestart.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenMgcpActionsRestart.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'AdGenMgcpProfileName':AdGenMgcpProfileName,'adGenMgcpProvisioning':adGenMgcpProvisioning,'adGenMgcpProfileProv':adGenMgcpProfileProv,'adGenMgcpProfileProvCurrentNumber':adGenMgcpProfileProvCurrentNumber,'adGenMgcpProfileProvLastCreateError':adGenMgcpProfileProvLastCreateError,'adGenMgcpProfileProvTable':adGenMgcpProfileProvTable,'adGenMgcpProfileProvEntry':adGenMgcpProfileProvEntry,_N:adGenMgcpProfileEntryIndex,'adGenMgcpProfileRowStatus':adGenMgcpProfileRowStatus,'adGenMgcpProfileLastErrorString':adGenMgcpProfileLastErrorString,'adGenMgcpProfileCallAgentPrimary':adGenMgcpProfileCallAgentPrimary,'adGenMgcpProfileCallAgentPrimaryUdp':adGenMgcpProfileCallAgentPrimaryUdp,'adGenMgcpProfileCallAgentSecondary':adGenMgcpProfileCallAgentSecondary,'adGenMgcpProfileCallAgentSecondaryUdp':adGenMgcpProfileCallAgentSecondaryUdp,'adGenMgcpProfileShutdown':adGenMgcpProfileShutdown,'adGenMgcpProfileBracketedIp':adGenMgcpProfileBracketedIp,'adGenMgcpProfileStandard':adGenMgcpProfileStandard,'adGenMgcpProfileMgcpDscp':adGenMgcpProfileMgcpDscp,'adGenMgcpProfileRtpDscp':adGenMgcpProfileRtpDscp,'adGenMgcpProfileGatewayUdp':adGenMgcpProfileGatewayUdp,'adGenMgcpProfileRtpUdpOffset':adGenMgcpProfileRtpUdpOffset,'adGenMgcpProfilePersistentNotifyHangDown':adGenMgcpProfilePersistentNotifyHangDown,'adGenMgcpProfilePersistentNotifyHangUp':adGenMgcpProfilePersistentNotifyHangUp,'adGenMgcpProfilePersistentNotifyHookFlash':adGenMgcpProfilePersistentNotifyHookFlash,'adGenMgcpProfileRetransmitDelay':adGenMgcpProfileRetransmitDelay,'adGenMgcpProfileMax1':adGenMgcpProfileMax1,'adGenMgcpProfileMax2':adGenMgcpProfileMax2,'adGenMgcpProfileLocalDomainType':adGenMgcpProfileLocalDomainType,'adGenMgcpProfileLocalDomainAddress':adGenMgcpProfileLocalDomainAddress,'adGenMgcpProfileTerminationIdBase':adGenMgcpProfileTerminationIdBase,'adGenMgcpProfileRFC2833Signaling':adGenMgcpProfileRFC2833Signaling,'adGenMgcpEndpointProv':adGenMgcpEndpointProv,'adGenMgcpEndpointProvCurrentNumber':adGenMgcpEndpointProvCurrentNumber,'adGenMgcpEndpointProvLastCreateError':adGenMgcpEndpointProvLastCreateError,'adGenMgcpEndpointProvTable':adGenMgcpEndpointProvTable,'adGenMgcpEndpointProvEntry':adGenMgcpEndpointProvEntry,_O:adGenMgcpEndpointEntryIndex,'adGenMgcpEndpointRowStatus':adGenMgcpEndpointRowStatus,'adGenMgcpEndpointLastErrorString':adGenMgcpEndpointLastErrorString,'adGenMgcpEndpointFxsPort':adGenMgcpEndpointFxsPort,'adGenMgcpEndpointMgcpProfile':adGenMgcpEndpointMgcpProfile,'adGenMgcpEndpointBlockCallerId':adGenMgcpEndpointBlockCallerId,'adGenMgcpEndpointDescription':adGenMgcpEndpointDescription,'adGenMgcpEndpointDisplayString':adGenMgcpEndpointDisplayString,'adGenMgcpEndpointFwdDisconnect':adGenMgcpEndpointFwdDisconnect,'adGenMgcpEndpointMediaProfile':adGenMgcpEndpointMediaProfile,'adGenMgcpEndpointCodecListProfile':adGenMgcpEndpointCodecListProfile,'adGenMgcpStatus':adGenMgcpStatus,'adGenMgcpEndpointStatus':adGenMgcpEndpointStatus,'adGenMgcpEndpointStatusTable':adGenMgcpEndpointStatusTable,'adGenMgcpEndpointStatusEntry':adGenMgcpEndpointStatusEntry,_P:adGenMgcpEndpointStatusEntryIndex,'adGenMgcpEndpointStatusFXSPort':adGenMgcpEndpointStatusFXSPort,'adGenMgcpEndpointStatusName':adGenMgcpEndpointStatusName,'adGenMgcpEndpointStatusConnectedProfile':adGenMgcpEndpointStatusConnectedProfile,'adGenMgcpEndpointStatusState':adGenMgcpEndpointStatusState,'adGenMgcpEndpointStatusStateDetail':adGenMgcpEndpointStatusStateDetail,'adGenMgcpEndpointOperStatus':adGenMgcpEndpointOperStatus,'adGenMgcpEndpointStatusCodecInUse':adGenMgcpEndpointStatusCodecInUse,'adGenMgcpEndpointLastError':adGenMgcpEndpointLastError,'adGenMgcpActions':adGenMgcpActions,'adGenMgcpActionsTable':adGenMgcpActionsTable,'adGenMgcpActionsEntry':adGenMgcpActionsEntry,'adGenMgcpActionsLastError':adGenMgcpActionsLastError,'adGenMgcpActionsRestart':adGenMgcpActionsRestart,'adGenMgcpEntity':adGenMgcpEntity})