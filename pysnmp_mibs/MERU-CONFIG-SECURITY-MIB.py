_O='mwCaptivePortalExemptionTableIndex'
_N='mwCaptivePortalProfileTableIndex'
_M='mwAuthModeTableIndex'
_L='mwGuestUserTableIndex'
_K='mwRadiusProfileTableIndex'
_J='mwSslVarsTableIndex'
_I='mwSecurityProfileTableIndex'
_H='read-only'
_G='not-accessible'
_F='MERU-CONFIG-SECURITY-MIB'
_E='Integer32'
_D='read-write'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAclEnvState,MwlAuthenticationType,MwlCaptivePortalAuthMethod,MwlCaptivePortalAuthenticationType,MwlCaptivePortalExternalServerType,MwlCaptivePortalMode,MwlCypherSuiteBits,MwlFirewallCapability,MwlKDDI,MwlL2SecurityModeBits,MwlManagementFrameProtection,MwlOnOffSwitch,MwlProfileOwner,MwlRadiusCalledStationIdType,MwlRadiusMacDelimiter,MwlRadiusPasswordType,MwlTunnelTerminationModeBits=mibBuilder.importSymbols('MERU-TC','MwlAclEnvState','MwlAuthenticationType','MwlCaptivePortalAuthMethod','MwlCaptivePortalAuthenticationType','MwlCaptivePortalExternalServerType','MwlCaptivePortalMode','MwlCypherSuiteBits','MwlFirewallCapability','MwlKDDI','MwlL2SecurityModeBits','MwlManagementFrameProtection','MwlOnOffSwitch','MwlProfileOwner','MwlRadiusCalledStationIdType','MwlRadiusMacDelimiter','MwlRadiusPasswordType','MwlTunnelTerminationModeBits')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigSecurity=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,9))
_MwSecurityProfileTable_Object=MibTable
mwSecurityProfileTable=_MwSecurityProfileTable_Object((1,3,6,1,4,1,15983,1,1,4,9,1))
if mibBuilder.loadTexts:mwSecurityProfileTable.setStatus(_A)
_MwSecurityProfileEntry_Object=MibTableRow
mwSecurityProfileEntry=_MwSecurityProfileEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1))
mwSecurityProfileEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:mwSecurityProfileEntry.setStatus(_A)
_MwSecurityProfileTableIndex_Type=Integer32
_MwSecurityProfileTableIndex_Object=MibTableColumn
mwSecurityProfileTableIndex=_MwSecurityProfileTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,1),_MwSecurityProfileTableIndex_Type())
mwSecurityProfileTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwSecurityProfileTableIndex.setStatus(_A)
class _MwSecurityProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwSecurityProfileName_Type.__name__=_C
_MwSecurityProfileName_Object=MibTableColumn
mwSecurityProfileName=_MwSecurityProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,2),_MwSecurityProfileName_Type())
mwSecurityProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileName.setStatus(_A)
_MwSecurityProfileKDDI_Type=MwlKDDI
_MwSecurityProfileKDDI_Object=MibTableColumn
mwSecurityProfileKDDI=_MwSecurityProfileKDDI_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,3),_MwSecurityProfileKDDI_Type())
mwSecurityProfileKDDI.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileKDDI.setStatus(_A)
_MwSecurityProfileReKeyPeriod_Type=Unsigned32
_MwSecurityProfileReKeyPeriod_Object=MibTableColumn
mwSecurityProfileReKeyPeriod=_MwSecurityProfileReKeyPeriod_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,5),_MwSecurityProfileReKeyPeriod_Type())
mwSecurityProfileReKeyPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileReKeyPeriod.setStatus(_A)
_MwSecurityProfileCypherSuites_Type=MwlCypherSuiteBits
_MwSecurityProfileCypherSuites_Object=MibTableColumn
mwSecurityProfileCypherSuites=_MwSecurityProfileCypherSuites_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,6),_MwSecurityProfileCypherSuites_Type())
mwSecurityProfileCypherSuites.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileCypherSuites.setStatus(_A)
_MwSecurityProfileReAuthEnable_Type=MwlOnOffSwitch
_MwSecurityProfileReAuthEnable_Object=MibTableColumn
mwSecurityProfileReAuthEnable=_MwSecurityProfileReAuthEnable_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,7),_MwSecurityProfileReAuthEnable_Type())
mwSecurityProfileReAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileReAuthEnable.setStatus(_A)
_MwSecurityProfileL2ModesAllowed_Type=MwlL2SecurityModeBits
_MwSecurityProfileL2ModesAllowed_Object=MibTableColumn
mwSecurityProfileL2ModesAllowed=_MwSecurityProfileL2ModesAllowed_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,8),_MwSecurityProfileL2ModesAllowed_Type())
mwSecurityProfileL2ModesAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileL2ModesAllowed.setStatus(_A)
class _MwSecurityProfileStaticWepKeyPos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_MwSecurityProfileStaticWepKeyPos_Type.__name__=_E
_MwSecurityProfileStaticWepKeyPos_Object=MibTableColumn
mwSecurityProfileStaticWepKeyPos=_MwSecurityProfileStaticWepKeyPos_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,10),_MwSecurityProfileStaticWepKeyPos_Type())
mwSecurityProfileStaticWepKeyPos.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileStaticWepKeyPos.setStatus(_A)
_MwSecurityProfileSecurityLogging_Type=MwlOnOffSwitch
_MwSecurityProfileSecurityLogging_Object=MibTableColumn
mwSecurityProfileSecurityLogging=_MwSecurityProfileSecurityLogging_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,11),_MwSecurityProfileSecurityLogging_Type())
mwSecurityProfileSecurityLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileSecurityLogging.setStatus(_A)
_MwSecurityProfileGroupKeyInterval_Type=Unsigned32
_MwSecurityProfileGroupKeyInterval_Object=MibTableColumn
mwSecurityProfileGroupKeyInterval=_MwSecurityProfileGroupKeyInterval_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,12),_MwSecurityProfileGroupKeyInterval_Type())
mwSecurityProfileGroupKeyInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileGroupKeyInterval.setStatus(_A)
class _MwSecurityProfileFirewallFilterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwSecurityProfileFirewallFilterId_Type.__name__=_C
_MwSecurityProfileFirewallFilterId_Object=MibTableColumn
mwSecurityProfileFirewallFilterId=_MwSecurityProfileFirewallFilterId_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,13),_MwSecurityProfileFirewallFilterId_Type())
mwSecurityProfileFirewallFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileFirewallFilterId.setStatus(_A)
_MwSecurityProfileSharedAuthEnabled_Type=MwlOnOffSwitch
_MwSecurityProfileSharedAuthEnabled_Object=MibTableColumn
mwSecurityProfileSharedAuthEnabled=_MwSecurityProfileSharedAuthEnabled_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,14),_MwSecurityProfileSharedAuthEnabled_Type())
mwSecurityProfileSharedAuthEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileSharedAuthEnabled.setStatus(_A)
_MwSecurityProfileEnableMacFiltering_Type=MwlOnOffSwitch
_MwSecurityProfileEnableMacFiltering_Object=MibTableColumn
mwSecurityProfileEnableMacFiltering=_MwSecurityProfileEnableMacFiltering_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,15),_MwSecurityProfileEnableMacFiltering_Type())
mwSecurityProfileEnableMacFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileEnableMacFiltering.setStatus(_A)
_MwSecurityProfileFirewallCapability_Type=MwlFirewallCapability
_MwSecurityProfileFirewallCapability_Object=MibTableColumn
mwSecurityProfileFirewallCapability=_MwSecurityProfileFirewallCapability_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,16),_MwSecurityProfileFirewallCapability_Type())
mwSecurityProfileFirewallCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileFirewallCapability.setStatus(_A)
_MwSecurityProfileCaptivePortalEnabled_Type=MwlCaptivePortalMode
_MwSecurityProfileCaptivePortalEnabled_Object=MibTableColumn
mwSecurityProfileCaptivePortalEnabled=_MwSecurityProfileCaptivePortalEnabled_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,17),_MwSecurityProfileCaptivePortalEnabled_Type())
mwSecurityProfileCaptivePortalEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileCaptivePortalEnabled.setStatus(_A)
_MwSecurityProfileNetworkInitiation8021x_Type=MwlOnOffSwitch
_MwSecurityProfileNetworkInitiation8021x_Object=MibTableColumn
mwSecurityProfileNetworkInitiation8021x=_MwSecurityProfileNetworkInitiation8021x_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,18),_MwSecurityProfileNetworkInitiation8021x_Type())
mwSecurityProfileNetworkInitiation8021x.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileNetworkInitiation8021x.setStatus(_A)
class _MwSecurityProfilePrimaryRadiusProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwSecurityProfilePrimaryRadiusProfileName_Type.__name__=_C
_MwSecurityProfilePrimaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfilePrimaryRadiusProfileName=_MwSecurityProfilePrimaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,19),_MwSecurityProfilePrimaryRadiusProfileName_Type())
mwSecurityProfilePrimaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfilePrimaryRadiusProfileName.setStatus(_A)
class _MwSecurityProfileSecondaryRadiusProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwSecurityProfileSecondaryRadiusProfileName_Type.__name__=_C
_MwSecurityProfileSecondaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfileSecondaryRadiusProfileName=_MwSecurityProfileSecondaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,20),_MwSecurityProfileSecondaryRadiusProfileName_Type())
mwSecurityProfileSecondaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileSecondaryRadiusProfileName.setStatus(_A)
class _MwSecurityProfilePskKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,66))
_MwSecurityProfilePskKey_Type.__name__=_C
_MwSecurityProfilePskKey_Object=MibTableColumn
mwSecurityProfilePskKey=_MwSecurityProfilePskKey_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,21),_MwSecurityProfilePskKey_Type())
mwSecurityProfilePskKey.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfilePskKey.setStatus(_A)
class _MwSecurityProfileStaticWepKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,28))
_MwSecurityProfileStaticWepKey_Type.__name__=_C
_MwSecurityProfileStaticWepKey_Object=MibTableColumn
mwSecurityProfileStaticWepKey=_MwSecurityProfileStaticWepKey_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,22),_MwSecurityProfileStaticWepKey_Type())
mwSecurityProfileStaticWepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileStaticWepKey.setStatus(_A)
class _MwSecurityProfilePassthroughFirewallFilterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwSecurityProfilePassthroughFirewallFilterId_Type.__name__=_C
_MwSecurityProfilePassthroughFirewallFilterId_Object=MibTableColumn
mwSecurityProfilePassthroughFirewallFilterId=_MwSecurityProfilePassthroughFirewallFilterId_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,23),_MwSecurityProfilePassthroughFirewallFilterId_Type())
mwSecurityProfilePassthroughFirewallFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfilePassthroughFirewallFilterId.setStatus(_A)
_MwSecurityProfileOwner_Type=MwlProfileOwner
_MwSecurityProfileOwner_Object=MibTableColumn
mwSecurityProfileOwner=_MwSecurityProfileOwner_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,25),_MwSecurityProfileOwner_Type())
mwSecurityProfileOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:mwSecurityProfileOwner.setStatus(_A)
_MwSecurityProfileCaptivePortalAuthenticationMethod_Type=MwlCaptivePortalAuthMethod
_MwSecurityProfileCaptivePortalAuthenticationMethod_Object=MibTableColumn
mwSecurityProfileCaptivePortalAuthenticationMethod=_MwSecurityProfileCaptivePortalAuthenticationMethod_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,27),_MwSecurityProfileCaptivePortalAuthenticationMethod_Type())
mwSecurityProfileCaptivePortalAuthenticationMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileCaptivePortalAuthenticationMethod.setStatus(_A)
_MwSecurityProfileTunnelTermination_Type=MwlTunnelTerminationModeBits
_MwSecurityProfileTunnelTermination_Object=MibTableColumn
mwSecurityProfileTunnelTermination=_MwSecurityProfileTunnelTermination_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,31),_MwSecurityProfileTunnelTermination_Type())
mwSecurityProfileTunnelTermination.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileTunnelTermination.setStatus(_A)
_MwSecurityProfileBKSACachingPeriod_Type=Unsigned32
_MwSecurityProfileBKSACachingPeriod_Object=MibTableColumn
mwSecurityProfileBKSACachingPeriod=_MwSecurityProfileBKSACachingPeriod_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,32),_MwSecurityProfileBKSACachingPeriod_Type())
mwSecurityProfileBKSACachingPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileBKSACachingPeriod.setStatus(_A)
_MwSecurityProfilePMKCachingStatus_Type=MwlOnOffSwitch
_MwSecurityProfilePMKCachingStatus_Object=MibTableColumn
mwSecurityProfilePMKCachingStatus=_MwSecurityProfilePMKCachingStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,33),_MwSecurityProfilePMKCachingStatus_Type())
mwSecurityProfilePMKCachingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfilePMKCachingStatus.setStatus(_A)
_MwSecurityProfileEnvState_Type=MwlAclEnvState
_MwSecurityProfileEnvState_Object=MibTableColumn
mwSecurityProfileEnvState=_MwSecurityProfileEnvState_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,47),_MwSecurityProfileEnvState_Type())
mwSecurityProfileEnvState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileEnvState.setStatus(_A)
_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Type=DisplayString
_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfileMACAuthPrimaryRadiusProfileName=_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,48),_MwSecurityProfileMACAuthPrimaryRadiusProfileName_Type())
mwSecurityProfileMACAuthPrimaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileMACAuthPrimaryRadiusProfileName.setStatus(_A)
_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Type=DisplayString
_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfileMACAuthSecondaryRadiusProfileName=_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,49),_MwSecurityProfileMACAuthSecondaryRadiusProfileName_Type())
mwSecurityProfileMACAuthSecondaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileMACAuthSecondaryRadiusProfileName.setStatus(_A)
class _MwSecurityProfileCaptivePortalProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwSecurityProfileCaptivePortalProfile_Type.__name__=_C
_MwSecurityProfileCaptivePortalProfile_Object=MibTableColumn
mwSecurityProfileCaptivePortalProfile=_MwSecurityProfileCaptivePortalProfile_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,50),_MwSecurityProfileCaptivePortalProfile_Type())
mwSecurityProfileCaptivePortalProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileCaptivePortalProfile.setStatus(_A)
_MwSecurityProfileMFP11wSupport_Type=MwlManagementFrameProtection
_MwSecurityProfileMFP11wSupport_Object=MibTableColumn
mwSecurityProfileMFP11wSupport=_MwSecurityProfileMFP11wSupport_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,51),_MwSecurityProfileMFP11wSupport_Type())
mwSecurityProfileMFP11wSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileMFP11wSupport.setStatus(_A)
_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Type=DisplayString
_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfileMACAccountingPrimaryRadiusProfileName=_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,52),_MwSecurityProfileMACAccountingPrimaryRadiusProfileName_Type())
mwSecurityProfileMACAccountingPrimaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileMACAccountingPrimaryRadiusProfileName.setStatus(_A)
_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Type=DisplayString
_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Object=MibTableColumn
mwSecurityProfileMACAccountingSecondaryRadiusProfileName=_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,53),_MwSecurityProfileMACAccountingSecondaryRadiusProfileName_Type())
mwSecurityProfileMACAccountingSecondaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileMACAccountingSecondaryRadiusProfileName.setStatus(_A)
_MwSecurityProfileCaptivePortalBypassForMAC_Type=MwlOnOffSwitch
_MwSecurityProfileCaptivePortalBypassForMAC_Object=MibTableColumn
mwSecurityProfileCaptivePortalBypassForMAC=_MwSecurityProfileCaptivePortalBypassForMAC_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,54),_MwSecurityProfileCaptivePortalBypassForMAC_Type())
mwSecurityProfileCaptivePortalBypassForMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileCaptivePortalBypassForMAC.setStatus(_A)
_MwSecurityProfileRowStatus_Type=RowStatus
_MwSecurityProfileRowStatus_Object=MibTableColumn
mwSecurityProfileRowStatus=_MwSecurityProfileRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,1,1,61),_MwSecurityProfileRowStatus_Type())
mwSecurityProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwSecurityProfileRowStatus.setStatus(_A)
_MwSslVarsTable_Object=MibTable
mwSslVarsTable=_MwSslVarsTable_Object((1,3,6,1,4,1,15983,1,1,4,9,2))
if mibBuilder.loadTexts:mwSslVarsTable.setStatus(_A)
_MwSslVarsEntry_Object=MibTableRow
mwSslVarsEntry=_MwSslVarsEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,2,1))
mwSslVarsEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:mwSslVarsEntry.setStatus(_A)
_MwSslVarsTableIndex_Type=Integer32
_MwSslVarsTableIndex_Object=MibTableColumn
mwSslVarsTableIndex=_MwSslVarsTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,2,1,1),_MwSslVarsTableIndex_Type())
mwSslVarsTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwSslVarsTableIndex.setStatus(_A)
_MwSslVarsSslLifeTime_Type=Unsigned32
_MwSslVarsSslLifeTime_Object=MibTableColumn
mwSslVarsSslLifeTime=_MwSslVarsSslLifeTime_Object((1,3,6,1,4,1,15983,1,1,4,9,2,1,12),_MwSslVarsSslLifeTime_Type())
mwSslVarsSslLifeTime.setMaxAccess(_H)
if mibBuilder.loadTexts:mwSslVarsSslLifeTime.setStatus(_A)
class _MwSslVarsCertificateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MwSslVarsCertificateFileName_Type.__name__=_C
_MwSslVarsCertificateFileName_Object=MibTableColumn
mwSslVarsCertificateFileName=_MwSslVarsCertificateFileName_Object((1,3,6,1,4,1,15983,1,1,4,9,2,1,15),_MwSslVarsCertificateFileName_Type())
mwSslVarsCertificateFileName.setMaxAccess(_H)
if mibBuilder.loadTexts:mwSslVarsCertificateFileName.setStatus(_A)
class _MwSslVarsCPCertificate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MwSslVarsCPCertificate_Type.__name__=_C
_MwSslVarsCPCertificate_Object=MibTableColumn
mwSslVarsCPCertificate=_MwSslVarsCPCertificate_Object((1,3,6,1,4,1,15983,1,1,4,9,2,1,26),_MwSslVarsCPCertificate_Type())
mwSslVarsCPCertificate.setMaxAccess(_H)
if mibBuilder.loadTexts:mwSslVarsCPCertificate.setStatus(_A)
_MwRadiusProfileTable_Object=MibTable
mwRadiusProfileTable=_MwRadiusProfileTable_Object((1,3,6,1,4,1,15983,1,1,4,9,3))
if mibBuilder.loadTexts:mwRadiusProfileTable.setStatus(_A)
_MwRadiusProfileEntry_Object=MibTableRow
mwRadiusProfileEntry=_MwRadiusProfileEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1))
mwRadiusProfileEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:mwRadiusProfileEntry.setStatus(_A)
_MwRadiusProfileTableIndex_Type=Integer32
_MwRadiusProfileTableIndex_Object=MibTableColumn
mwRadiusProfileTableIndex=_MwRadiusProfileTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,1),_MwRadiusProfileTableIndex_Type())
mwRadiusProfileTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwRadiusProfileTableIndex.setStatus(_A)
class _MwRadiusProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MwRadiusProfileName_Type.__name__=_C
_MwRadiusProfileName_Object=MibTableColumn
mwRadiusProfileName=_MwRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,2),_MwRadiusProfileName_Type())
mwRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileName.setStatus(_A)
class _MwRadiusProfileDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MwRadiusProfileDescr_Type.__name__=_C
_MwRadiusProfileDescr_Object=MibTableColumn
mwRadiusProfileDescr=_MwRadiusProfileDescr_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,3),_MwRadiusProfileDescr_Type())
mwRadiusProfileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileDescr.setStatus(_A)
_MwRadiusProfileRadiusIp_Type=IpAddress
_MwRadiusProfileRadiusIp_Object=MibTableColumn
mwRadiusProfileRadiusIp=_MwRadiusProfileRadiusIp_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,4),_MwRadiusProfileRadiusIp_Type())
mwRadiusProfileRadiusIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusIp.setStatus(_A)
_MwRadiusProfileRadiusPort_Type=Unsigned32
_MwRadiusProfileRadiusPort_Object=MibTableColumn
mwRadiusProfileRadiusPort=_MwRadiusProfileRadiusPort_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,5),_MwRadiusProfileRadiusPort_Type())
mwRadiusProfileRadiusPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusPort.setStatus(_A)
_MwRadiusProfileRadiusMacDelimiter_Type=MwlRadiusMacDelimiter
_MwRadiusProfileRadiusMacDelimiter_Object=MibTableColumn
mwRadiusProfileRadiusMacDelimiter=_MwRadiusProfileRadiusMacDelimiter_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,6),_MwRadiusProfileRadiusMacDelimiter_Type())
mwRadiusProfileRadiusMacDelimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusMacDelimiter.setStatus(_A)
_MwRadiusProfileRadiusPasswordType_Type=MwlRadiusPasswordType
_MwRadiusProfileRadiusPasswordType_Object=MibTableColumn
mwRadiusProfileRadiusPasswordType=_MwRadiusProfileRadiusPasswordType_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,7),_MwRadiusProfileRadiusPasswordType_Type())
mwRadiusProfileRadiusPasswordType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusPasswordType.setStatus(_A)
class _MwRadiusProfileRadiusSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MwRadiusProfileRadiusSecret_Type.__name__=_C
_MwRadiusProfileRadiusSecret_Object=MibTableColumn
mwRadiusProfileRadiusSecret=_MwRadiusProfileRadiusSecret_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,8),_MwRadiusProfileRadiusSecret_Type())
mwRadiusProfileRadiusSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusSecret.setStatus(_A)
_MwRadiusProfileOwner_Type=MwlProfileOwner
_MwRadiusProfileOwner_Object=MibTableColumn
mwRadiusProfileOwner=_MwRadiusProfileOwner_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,9),_MwRadiusProfileOwner_Type())
mwRadiusProfileOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:mwRadiusProfileOwner.setStatus(_A)
_MwRadiusProfileCalledStationIdType_Type=MwlRadiusCalledStationIdType
_MwRadiusProfileCalledStationIdType_Object=MibTableColumn
mwRadiusProfileCalledStationIdType=_MwRadiusProfileCalledStationIdType_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,10),_MwRadiusProfileCalledStationIdType_Type())
mwRadiusProfileCalledStationIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileCalledStationIdType.setStatus(_A)
_MwRadiusProfileCoaFlag_Type=MwlOnOffSwitch
_MwRadiusProfileCoaFlag_Object=MibTableColumn
mwRadiusProfileCoaFlag=_MwRadiusProfileCoaFlag_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,11),_MwRadiusProfileCoaFlag_Type())
mwRadiusProfileCoaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileCoaFlag.setStatus(_A)
_MwRadiusProfileRadiusRelayApId_Type=Unsigned32
_MwRadiusProfileRadiusRelayApId_Object=MibTableColumn
mwRadiusProfileRadiusRelayApId=_MwRadiusProfileRadiusRelayApId_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,12),_MwRadiusProfileRadiusRelayApId_Type())
mwRadiusProfileRadiusRelayApId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusRelayApId.setStatus(_A)
_MwRadiusProfileRemoteRadiusServerFlag_Type=MwlOnOffSwitch
_MwRadiusProfileRemoteRadiusServerFlag_Object=MibTableColumn
mwRadiusProfileRemoteRadiusServerFlag=_MwRadiusProfileRemoteRadiusServerFlag_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,13),_MwRadiusProfileRemoteRadiusServerFlag_Type())
mwRadiusProfileRemoteRadiusServerFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRemoteRadiusServerFlag.setStatus(_A)
class _MwRadiusProfileRadiusServerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_MwRadiusProfileRadiusServerTimeout_Type.__name__=_E
_MwRadiusProfileRadiusServerTimeout_Object=MibTableColumn
mwRadiusProfileRadiusServerTimeout=_MwRadiusProfileRadiusServerTimeout_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,14),_MwRadiusProfileRadiusServerTimeout_Type())
mwRadiusProfileRadiusServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusServerTimeout.setStatus(_A)
class _MwRadiusProfileRadiusServerRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MwRadiusProfileRadiusServerRetries_Type.__name__=_E
_MwRadiusProfileRadiusServerRetries_Object=MibTableColumn
mwRadiusProfileRadiusServerRetries=_MwRadiusProfileRadiusServerRetries_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,15),_MwRadiusProfileRadiusServerRetries_Type())
mwRadiusProfileRadiusServerRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRadiusServerRetries.setStatus(_A)
_MwRadiusProfileRowStatus_Type=RowStatus
_MwRadiusProfileRowStatus_Object=MibTableColumn
mwRadiusProfileRowStatus=_MwRadiusProfileRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,3,1,19),_MwRadiusProfileRowStatus_Type())
mwRadiusProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwRadiusProfileRowStatus.setStatus(_A)
_MwGuestUserTable_Object=MibTable
mwGuestUserTable=_MwGuestUserTable_Object((1,3,6,1,4,1,15983,1,1,4,9,4))
if mibBuilder.loadTexts:mwGuestUserTable.setStatus(_A)
_MwGuestUserEntry_Object=MibTableRow
mwGuestUserEntry=_MwGuestUserEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1))
mwGuestUserEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:mwGuestUserEntry.setStatus(_A)
_MwGuestUserTableIndex_Type=Integer32
_MwGuestUserTableIndex_Object=MibTableColumn
mwGuestUserTableIndex=_MwGuestUserTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,1),_MwGuestUserTableIndex_Type())
mwGuestUserTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwGuestUserTableIndex.setStatus(_A)
class _MwGuestUserGuestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MwGuestUserGuestName_Type.__name__=_C
_MwGuestUserGuestName_Object=MibTableColumn
mwGuestUserGuestName=_MwGuestUserGuestName_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,2),_MwGuestUserGuestName_Type())
mwGuestUserGuestName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGuestUserGuestName.setStatus(_A)
_MwGuestUserEndTimestamp_Type=DateAndTime
_MwGuestUserEndTimestamp_Object=MibTableColumn
mwGuestUserEndTimestamp=_MwGuestUserEndTimestamp_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,3),_MwGuestUserEndTimestamp_Type())
mwGuestUserEndTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGuestUserEndTimestamp.setStatus(_A)
_MwGuestUserStartTimestamp_Type=DateAndTime
_MwGuestUserStartTimestamp_Object=MibTableColumn
mwGuestUserStartTimestamp=_MwGuestUserStartTimestamp_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,4),_MwGuestUserStartTimestamp_Type())
mwGuestUserStartTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGuestUserStartTimestamp.setStatus(_A)
class _MwGuestUserGuestPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MwGuestUserGuestPasswd_Type.__name__=_C
_MwGuestUserGuestPasswd_Object=MibTableColumn
mwGuestUserGuestPasswd=_MwGuestUserGuestPasswd_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,5),_MwGuestUserGuestPasswd_Type())
mwGuestUserGuestPasswd.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGuestUserGuestPasswd.setStatus(_A)
_MwGuestUserRowStatus_Type=RowStatus
_MwGuestUserRowStatus_Object=MibTableColumn
mwGuestUserRowStatus=_MwGuestUserRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,4,1,6),_MwGuestUserRowStatus_Type())
mwGuestUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwGuestUserRowStatus.setStatus(_A)
_MwAuthModeTable_Object=MibTable
mwAuthModeTable=_MwAuthModeTable_Object((1,3,6,1,4,1,15983,1,1,4,9,5))
if mibBuilder.loadTexts:mwAuthModeTable.setStatus(_A)
_MwAuthModeEntry_Object=MibTableRow
mwAuthModeEntry=_MwAuthModeEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1))
mwAuthModeEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:mwAuthModeEntry.setStatus(_A)
_MwAuthModeTableIndex_Type=Integer32
_MwAuthModeTableIndex_Object=MibTableColumn
mwAuthModeTableIndex=_MwAuthModeTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,1),_MwAuthModeTableIndex_Type())
mwAuthModeTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwAuthModeTableIndex.setStatus(_A)
_MwAuthModeAuthType_Type=MwlAuthenticationType
_MwAuthModeAuthType_Object=MibTableColumn
mwAuthModeAuthType=_MwAuthModeAuthType_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,2),_MwAuthModeAuthType_Type())
mwAuthModeAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeAuthType.setStatus(_A)
_MwAuthModePrimaryRadiusIp_Type=IpAddress
_MwAuthModePrimaryRadiusIp_Object=MibTableColumn
mwAuthModePrimaryRadiusIp=_MwAuthModePrimaryRadiusIp_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,5),_MwAuthModePrimaryRadiusIp_Type())
mwAuthModePrimaryRadiusIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryRadiusIp.setStatus(_A)
_MwAuthModePrimaryRadiusPort_Type=Unsigned32
_MwAuthModePrimaryRadiusPort_Object=MibTableColumn
mwAuthModePrimaryRadiusPort=_MwAuthModePrimaryRadiusPort_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,6),_MwAuthModePrimaryRadiusPort_Type())
mwAuthModePrimaryRadiusPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryRadiusPort.setStatus(_A)
class _MwAuthModePrimaryRadiusSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwAuthModePrimaryRadiusSecret_Type.__name__=_C
_MwAuthModePrimaryRadiusSecret_Object=MibTableColumn
mwAuthModePrimaryRadiusSecret=_MwAuthModePrimaryRadiusSecret_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,7),_MwAuthModePrimaryRadiusSecret_Type())
mwAuthModePrimaryRadiusSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryRadiusSecret.setStatus(_A)
_MwAuthModeSecondaryRadiusIp_Type=IpAddress
_MwAuthModeSecondaryRadiusIp_Object=MibTableColumn
mwAuthModeSecondaryRadiusIp=_MwAuthModeSecondaryRadiusIp_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,8),_MwAuthModeSecondaryRadiusIp_Type())
mwAuthModeSecondaryRadiusIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryRadiusIp.setStatus(_A)
_MwAuthModeSecondaryRadiusPort_Type=Unsigned32
_MwAuthModeSecondaryRadiusPort_Object=MibTableColumn
mwAuthModeSecondaryRadiusPort=_MwAuthModeSecondaryRadiusPort_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,9),_MwAuthModeSecondaryRadiusPort_Type())
mwAuthModeSecondaryRadiusPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryRadiusPort.setStatus(_A)
class _MwAuthModeSecondaryRadiusSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwAuthModeSecondaryRadiusSecret_Type.__name__=_C
_MwAuthModeSecondaryRadiusSecret_Object=MibTableColumn
mwAuthModeSecondaryRadiusSecret=_MwAuthModeSecondaryRadiusSecret_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,10),_MwAuthModeSecondaryRadiusSecret_Type())
mwAuthModeSecondaryRadiusSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryRadiusSecret.setStatus(_A)
_MwAuthModePrimaryTacacsIp_Type=IpAddress
_MwAuthModePrimaryTacacsIp_Object=MibTableColumn
mwAuthModePrimaryTacacsIp=_MwAuthModePrimaryTacacsIp_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,11),_MwAuthModePrimaryTacacsIp_Type())
mwAuthModePrimaryTacacsIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryTacacsIp.setStatus(_A)
_MwAuthModePrimaryTacacsPort_Type=Unsigned32
_MwAuthModePrimaryTacacsPort_Object=MibTableColumn
mwAuthModePrimaryTacacsPort=_MwAuthModePrimaryTacacsPort_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,12),_MwAuthModePrimaryTacacsPort_Type())
mwAuthModePrimaryTacacsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryTacacsPort.setStatus(_A)
class _MwAuthModePrimaryTacacsSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwAuthModePrimaryTacacsSecret_Type.__name__=_C
_MwAuthModePrimaryTacacsSecret_Object=MibTableColumn
mwAuthModePrimaryTacacsSecret=_MwAuthModePrimaryTacacsSecret_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,13),_MwAuthModePrimaryTacacsSecret_Type())
mwAuthModePrimaryTacacsSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModePrimaryTacacsSecret.setStatus(_A)
_MwAuthModeSecondaryTacacsIp_Type=IpAddress
_MwAuthModeSecondaryTacacsIp_Object=MibTableColumn
mwAuthModeSecondaryTacacsIp=_MwAuthModeSecondaryTacacsIp_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,14),_MwAuthModeSecondaryTacacsIp_Type())
mwAuthModeSecondaryTacacsIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryTacacsIp.setStatus(_A)
_MwAuthModeSecondaryTacacsPort_Type=Unsigned32
_MwAuthModeSecondaryTacacsPort_Object=MibTableColumn
mwAuthModeSecondaryTacacsPort=_MwAuthModeSecondaryTacacsPort_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,15),_MwAuthModeSecondaryTacacsPort_Type())
mwAuthModeSecondaryTacacsPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryTacacsPort.setStatus(_A)
class _MwAuthModeSecondaryTacacsSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MwAuthModeSecondaryTacacsSecret_Type.__name__=_C
_MwAuthModeSecondaryTacacsSecret_Object=MibTableColumn
mwAuthModeSecondaryTacacsSecret=_MwAuthModeSecondaryTacacsSecret_Object((1,3,6,1,4,1,15983,1,1,4,9,5,1,16),_MwAuthModeSecondaryTacacsSecret_Type())
mwAuthModeSecondaryTacacsSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:mwAuthModeSecondaryTacacsSecret.setStatus(_A)
_MwWapiServer_ObjectIdentity=ObjectIdentity
mwWapiServer=_MwWapiServer_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,9,6))
_MwWapiServerServerIp_Type=IpAddress
_MwWapiServerServerIp_Object=MibScalar
mwWapiServerServerIp=_MwWapiServerServerIp_Object((1,3,6,1,4,1,15983,1,1,4,9,6,1),_MwWapiServerServerIp_Type())
mwWapiServerServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWapiServerServerIp.setStatus(_A)
class _MwWapiServerServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_MwWapiServerServerPort_Type.__name__=_E
_MwWapiServerServerPort_Object=MibScalar
mwWapiServerServerPort=_MwWapiServerServerPort_Object((1,3,6,1,4,1,15983,1,1,4,9,6,2),_MwWapiServerServerPort_Type())
mwWapiServerServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mwWapiServerServerPort.setStatus(_A)
_MwCaptivePortalProfileTable_Object=MibTable
mwCaptivePortalProfileTable=_MwCaptivePortalProfileTable_Object((1,3,6,1,4,1,15983,1,1,4,9,7))
if mibBuilder.loadTexts:mwCaptivePortalProfileTable.setStatus(_A)
_MwCaptivePortalProfileEntry_Object=MibTableRow
mwCaptivePortalProfileEntry=_MwCaptivePortalProfileEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1))
mwCaptivePortalProfileEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:mwCaptivePortalProfileEntry.setStatus(_A)
_MwCaptivePortalProfileTableIndex_Type=Integer32
_MwCaptivePortalProfileTableIndex_Object=MibTableColumn
mwCaptivePortalProfileTableIndex=_MwCaptivePortalProfileTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,1),_MwCaptivePortalProfileTableIndex_Type())
mwCaptivePortalProfileTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwCaptivePortalProfileTableIndex.setStatus(_A)
class _MwCaptivePortalProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwCaptivePortalProfileName_Type.__name__=_C
_MwCaptivePortalProfileName_Object=MibTableColumn
mwCaptivePortalProfileName=_MwCaptivePortalProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,2),_MwCaptivePortalProfileName_Type())
mwCaptivePortalProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileName.setStatus(_A)
class _MwCaptivePortalProfileRadiusProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwCaptivePortalProfileRadiusProfileName_Type.__name__=_C
_MwCaptivePortalProfileRadiusProfileName_Object=MibTableColumn
mwCaptivePortalProfileRadiusProfileName=_MwCaptivePortalProfileRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,3),_MwCaptivePortalProfileRadiusProfileName_Type())
mwCaptivePortalProfileRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileRadiusProfileName.setStatus(_A)
class _MwCaptivePortalProfileSecondaryRadiusProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwCaptivePortalProfileSecondaryRadiusProfileName_Type.__name__=_C
_MwCaptivePortalProfileSecondaryRadiusProfileName_Object=MibTableColumn
mwCaptivePortalProfileSecondaryRadiusProfileName=_MwCaptivePortalProfileSecondaryRadiusProfileName_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,4),_MwCaptivePortalProfileSecondaryRadiusProfileName_Type())
mwCaptivePortalProfileSecondaryRadiusProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileSecondaryRadiusProfileName.setStatus(_A)
class _MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type.__name__=_C
_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Object=MibTableColumn
mwCaptivePortalProfilePrimaryAccountingRadiusServer=_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,5),_MwCaptivePortalProfilePrimaryAccountingRadiusServer_Type())
mwCaptivePortalProfilePrimaryAccountingRadiusServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfilePrimaryAccountingRadiusServer.setStatus(_A)
class _MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type.__name__=_C
_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Object=MibTableColumn
mwCaptivePortalProfileSecondaryAccountingRadiusServer=_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,6),_MwCaptivePortalProfileSecondaryAccountingRadiusServer_Type())
mwCaptivePortalProfileSecondaryAccountingRadiusServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileSecondaryAccountingRadiusServer.setStatus(_A)
_MwCaptivePortalProfileAccountingInterimInterval_Type=Unsigned32
_MwCaptivePortalProfileAccountingInterimInterval_Object=MibTableColumn
mwCaptivePortalProfileAccountingInterimInterval=_MwCaptivePortalProfileAccountingInterimInterval_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,7),_MwCaptivePortalProfileAccountingInterimInterval_Type())
mwCaptivePortalProfileAccountingInterimInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileAccountingInterimInterval.setStatus(_A)
_MwCaptivePortalProfileOverrideRadius_Type=MwlCaptivePortalAuthenticationType
_MwCaptivePortalProfileOverrideRadius_Object=MibTableColumn
mwCaptivePortalProfileOverrideRadius=_MwCaptivePortalProfileOverrideRadius_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,8),_MwCaptivePortalProfileOverrideRadius_Type())
mwCaptivePortalProfileOverrideRadius.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileOverrideRadius.setStatus(_A)
class _MwCaptivePortalProfileExternalCPURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MwCaptivePortalProfileExternalCPURL_Type.__name__=_C
_MwCaptivePortalProfileExternalCPURL_Object=MibTableColumn
mwCaptivePortalProfileExternalCPURL=_MwCaptivePortalProfileExternalCPURL_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,9),_MwCaptivePortalProfileExternalCPURL_Type())
mwCaptivePortalProfileExternalCPURL.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileExternalCPURL.setStatus(_A)
_MwCaptivePortalProfileExternalCPIP_Type=IpAddress
_MwCaptivePortalProfileExternalCPIP_Object=MibTableColumn
mwCaptivePortalProfileExternalCPIP=_MwCaptivePortalProfileExternalCPIP_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,10),_MwCaptivePortalProfileExternalCPIP_Type())
mwCaptivePortalProfileExternalCPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileExternalCPIP.setStatus(_A)
class _MwCaptivePortalProfileCaptivePortalSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_MwCaptivePortalProfileCaptivePortalSessionTimeout_Type.__name__=_E
_MwCaptivePortalProfileCaptivePortalSessionTimeout_Object=MibTableColumn
mwCaptivePortalProfileCaptivePortalSessionTimeout=_MwCaptivePortalProfileCaptivePortalSessionTimeout_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,15),_MwCaptivePortalProfileCaptivePortalSessionTimeout_Type())
mwCaptivePortalProfileCaptivePortalSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileCaptivePortalSessionTimeout.setStatus(_A)
class _MwCaptivePortalProfileCaptivePortalActivityTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_MwCaptivePortalProfileCaptivePortalActivityTimeout_Type.__name__=_E
_MwCaptivePortalProfileCaptivePortalActivityTimeout_Object=MibTableColumn
mwCaptivePortalProfileCaptivePortalActivityTimeout=_MwCaptivePortalProfileCaptivePortalActivityTimeout_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,16),_MwCaptivePortalProfileCaptivePortalActivityTimeout_Type())
mwCaptivePortalProfileCaptivePortalActivityTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileCaptivePortalActivityTimeout.setStatus(_A)
class _MwCaptivePortalProfileL3UserSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_MwCaptivePortalProfileL3UserSessionTimeout_Type.__name__=_E
_MwCaptivePortalProfileL3UserSessionTimeout_Object=MibTableColumn
mwCaptivePortalProfileL3UserSessionTimeout=_MwCaptivePortalProfileL3UserSessionTimeout_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,17),_MwCaptivePortalProfileL3UserSessionTimeout_Type())
mwCaptivePortalProfileL3UserSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileL3UserSessionTimeout.setStatus(_A)
_MwCaptivePortalProfileAutoLogin_Type=MwlOnOffSwitch
_MwCaptivePortalProfileAutoLogin_Object=MibTableColumn
mwCaptivePortalProfileAutoLogin=_MwCaptivePortalProfileAutoLogin_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,18),_MwCaptivePortalProfileAutoLogin_Type())
mwCaptivePortalProfileAutoLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileAutoLogin.setStatus(_A)
_MwCaptivePortalProfileOwner_Type=MwlProfileOwner
_MwCaptivePortalProfileOwner_Object=MibTableColumn
mwCaptivePortalProfileOwner=_MwCaptivePortalProfileOwner_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,19),_MwCaptivePortalProfileOwner_Type())
mwCaptivePortalProfileOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:mwCaptivePortalProfileOwner.setStatus(_A)
_MwCaptivePortalProfileExternalServer_Type=MwlCaptivePortalExternalServerType
_MwCaptivePortalProfileExternalServer_Object=MibTableColumn
mwCaptivePortalProfileExternalServer=_MwCaptivePortalProfileExternalServer_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,20),_MwCaptivePortalProfileExternalServer_Type())
mwCaptivePortalProfileExternalServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileExternalServer.setStatus(_A)
class _MwCaptivePortalProfileCpExemptionProfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwCaptivePortalProfileCpExemptionProfile_Type.__name__=_C
_MwCaptivePortalProfileCpExemptionProfile_Object=MibTableColumn
mwCaptivePortalProfileCpExemptionProfile=_MwCaptivePortalProfileCpExemptionProfile_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,21),_MwCaptivePortalProfileCpExemptionProfile_Type())
mwCaptivePortalProfileCpExemptionProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileCpExemptionProfile.setStatus(_A)
_MwCaptivePortalProfileRowStatus_Type=RowStatus
_MwCaptivePortalProfileRowStatus_Object=MibTableColumn
mwCaptivePortalProfileRowStatus=_MwCaptivePortalProfileRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,7,1,58),_MwCaptivePortalProfileRowStatus_Type())
mwCaptivePortalProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalProfileRowStatus.setStatus(_A)
_MwCaptivePortalExemptionTable_Object=MibTable
mwCaptivePortalExemptionTable=_MwCaptivePortalExemptionTable_Object((1,3,6,1,4,1,15983,1,1,4,9,8))
if mibBuilder.loadTexts:mwCaptivePortalExemptionTable.setStatus(_A)
_MwCaptivePortalExemptionEntry_Object=MibTableRow
mwCaptivePortalExemptionEntry=_MwCaptivePortalExemptionEntry_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1))
mwCaptivePortalExemptionEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:mwCaptivePortalExemptionEntry.setStatus(_A)
_MwCaptivePortalExemptionTableIndex_Type=Integer32
_MwCaptivePortalExemptionTableIndex_Object=MibTableColumn
mwCaptivePortalExemptionTableIndex=_MwCaptivePortalExemptionTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,1),_MwCaptivePortalExemptionTableIndex_Type())
mwCaptivePortalExemptionTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mwCaptivePortalExemptionTableIndex.setStatus(_A)
class _MwCaptivePortalExemptionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwCaptivePortalExemptionName_Type.__name__=_C
_MwCaptivePortalExemptionName_Object=MibTableColumn
mwCaptivePortalExemptionName=_MwCaptivePortalExemptionName_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,2),_MwCaptivePortalExemptionName_Type())
mwCaptivePortalExemptionName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalExemptionName.setStatus(_A)
class _MwCaptivePortalExemptionDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MwCaptivePortalExemptionDescr_Type.__name__=_C
_MwCaptivePortalExemptionDescr_Object=MibTableColumn
mwCaptivePortalExemptionDescr=_MwCaptivePortalExemptionDescr_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,3),_MwCaptivePortalExemptionDescr_Type())
mwCaptivePortalExemptionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalExemptionDescr.setStatus(_A)
_MwCaptivePortalExemptionFqdn_Type=DisplayString
_MwCaptivePortalExemptionFqdn_Object=MibTableColumn
mwCaptivePortalExemptionFqdn=_MwCaptivePortalExemptionFqdn_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,4),_MwCaptivePortalExemptionFqdn_Type())
mwCaptivePortalExemptionFqdn.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalExemptionFqdn.setStatus(_A)
_MwCaptivePortalExemptionOwner_Type=MwlProfileOwner
_MwCaptivePortalExemptionOwner_Object=MibTableColumn
mwCaptivePortalExemptionOwner=_MwCaptivePortalExemptionOwner_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,5),_MwCaptivePortalExemptionOwner_Type())
mwCaptivePortalExemptionOwner.setMaxAccess(_H)
if mibBuilder.loadTexts:mwCaptivePortalExemptionOwner.setStatus(_A)
_MwCaptivePortalExemptionRowStatus_Type=RowStatus
_MwCaptivePortalExemptionRowStatus_Object=MibTableColumn
mwCaptivePortalExemptionRowStatus=_MwCaptivePortalExemptionRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,9,8,1,7),_MwCaptivePortalExemptionRowStatus_Type())
mwCaptivePortalExemptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwCaptivePortalExemptionRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'mwConfigSecurity':mwConfigSecurity,'mwSecurityProfileTable':mwSecurityProfileTable,'mwSecurityProfileEntry':mwSecurityProfileEntry,_I:mwSecurityProfileTableIndex,'mwSecurityProfileName':mwSecurityProfileName,'mwSecurityProfileKDDI':mwSecurityProfileKDDI,'mwSecurityProfileReKeyPeriod':mwSecurityProfileReKeyPeriod,'mwSecurityProfileCypherSuites':mwSecurityProfileCypherSuites,'mwSecurityProfileReAuthEnable':mwSecurityProfileReAuthEnable,'mwSecurityProfileL2ModesAllowed':mwSecurityProfileL2ModesAllowed,'mwSecurityProfileStaticWepKeyPos':mwSecurityProfileStaticWepKeyPos,'mwSecurityProfileSecurityLogging':mwSecurityProfileSecurityLogging,'mwSecurityProfileGroupKeyInterval':mwSecurityProfileGroupKeyInterval,'mwSecurityProfileFirewallFilterId':mwSecurityProfileFirewallFilterId,'mwSecurityProfileSharedAuthEnabled':mwSecurityProfileSharedAuthEnabled,'mwSecurityProfileEnableMacFiltering':mwSecurityProfileEnableMacFiltering,'mwSecurityProfileFirewallCapability':mwSecurityProfileFirewallCapability,'mwSecurityProfileCaptivePortalEnabled':mwSecurityProfileCaptivePortalEnabled,'mwSecurityProfileNetworkInitiation8021x':mwSecurityProfileNetworkInitiation8021x,'mwSecurityProfilePrimaryRadiusProfileName':mwSecurityProfilePrimaryRadiusProfileName,'mwSecurityProfileSecondaryRadiusProfileName':mwSecurityProfileSecondaryRadiusProfileName,'mwSecurityProfilePskKey':mwSecurityProfilePskKey,'mwSecurityProfileStaticWepKey':mwSecurityProfileStaticWepKey,'mwSecurityProfilePassthroughFirewallFilterId':mwSecurityProfilePassthroughFirewallFilterId,'mwSecurityProfileOwner':mwSecurityProfileOwner,'mwSecurityProfileCaptivePortalAuthenticationMethod':mwSecurityProfileCaptivePortalAuthenticationMethod,'mwSecurityProfileTunnelTermination':mwSecurityProfileTunnelTermination,'mwSecurityProfileBKSACachingPeriod':mwSecurityProfileBKSACachingPeriod,'mwSecurityProfilePMKCachingStatus':mwSecurityProfilePMKCachingStatus,'mwSecurityProfileEnvState':mwSecurityProfileEnvState,'mwSecurityProfileMACAuthPrimaryRadiusProfileName':mwSecurityProfileMACAuthPrimaryRadiusProfileName,'mwSecurityProfileMACAuthSecondaryRadiusProfileName':mwSecurityProfileMACAuthSecondaryRadiusProfileName,'mwSecurityProfileCaptivePortalProfile':mwSecurityProfileCaptivePortalProfile,'mwSecurityProfileMFP11wSupport':mwSecurityProfileMFP11wSupport,'mwSecurityProfileMACAccountingPrimaryRadiusProfileName':mwSecurityProfileMACAccountingPrimaryRadiusProfileName,'mwSecurityProfileMACAccountingSecondaryRadiusProfileName':mwSecurityProfileMACAccountingSecondaryRadiusProfileName,'mwSecurityProfileCaptivePortalBypassForMAC':mwSecurityProfileCaptivePortalBypassForMAC,'mwSecurityProfileRowStatus':mwSecurityProfileRowStatus,'mwSslVarsTable':mwSslVarsTable,'mwSslVarsEntry':mwSslVarsEntry,_J:mwSslVarsTableIndex,'mwSslVarsSslLifeTime':mwSslVarsSslLifeTime,'mwSslVarsCertificateFileName':mwSslVarsCertificateFileName,'mwSslVarsCPCertificate':mwSslVarsCPCertificate,'mwRadiusProfileTable':mwRadiusProfileTable,'mwRadiusProfileEntry':mwRadiusProfileEntry,_K:mwRadiusProfileTableIndex,'mwRadiusProfileName':mwRadiusProfileName,'mwRadiusProfileDescr':mwRadiusProfileDescr,'mwRadiusProfileRadiusIp':mwRadiusProfileRadiusIp,'mwRadiusProfileRadiusPort':mwRadiusProfileRadiusPort,'mwRadiusProfileRadiusMacDelimiter':mwRadiusProfileRadiusMacDelimiter,'mwRadiusProfileRadiusPasswordType':mwRadiusProfileRadiusPasswordType,'mwRadiusProfileRadiusSecret':mwRadiusProfileRadiusSecret,'mwRadiusProfileOwner':mwRadiusProfileOwner,'mwRadiusProfileCalledStationIdType':mwRadiusProfileCalledStationIdType,'mwRadiusProfileCoaFlag':mwRadiusProfileCoaFlag,'mwRadiusProfileRadiusRelayApId':mwRadiusProfileRadiusRelayApId,'mwRadiusProfileRemoteRadiusServerFlag':mwRadiusProfileRemoteRadiusServerFlag,'mwRadiusProfileRadiusServerTimeout':mwRadiusProfileRadiusServerTimeout,'mwRadiusProfileRadiusServerRetries':mwRadiusProfileRadiusServerRetries,'mwRadiusProfileRowStatus':mwRadiusProfileRowStatus,'mwGuestUserTable':mwGuestUserTable,'mwGuestUserEntry':mwGuestUserEntry,_L:mwGuestUserTableIndex,'mwGuestUserGuestName':mwGuestUserGuestName,'mwGuestUserEndTimestamp':mwGuestUserEndTimestamp,'mwGuestUserStartTimestamp':mwGuestUserStartTimestamp,'mwGuestUserGuestPasswd':mwGuestUserGuestPasswd,'mwGuestUserRowStatus':mwGuestUserRowStatus,'mwAuthModeTable':mwAuthModeTable,'mwAuthModeEntry':mwAuthModeEntry,_M:mwAuthModeTableIndex,'mwAuthModeAuthType':mwAuthModeAuthType,'mwAuthModePrimaryRadiusIp':mwAuthModePrimaryRadiusIp,'mwAuthModePrimaryRadiusPort':mwAuthModePrimaryRadiusPort,'mwAuthModePrimaryRadiusSecret':mwAuthModePrimaryRadiusSecret,'mwAuthModeSecondaryRadiusIp':mwAuthModeSecondaryRadiusIp,'mwAuthModeSecondaryRadiusPort':mwAuthModeSecondaryRadiusPort,'mwAuthModeSecondaryRadiusSecret':mwAuthModeSecondaryRadiusSecret,'mwAuthModePrimaryTacacsIp':mwAuthModePrimaryTacacsIp,'mwAuthModePrimaryTacacsPort':mwAuthModePrimaryTacacsPort,'mwAuthModePrimaryTacacsSecret':mwAuthModePrimaryTacacsSecret,'mwAuthModeSecondaryTacacsIp':mwAuthModeSecondaryTacacsIp,'mwAuthModeSecondaryTacacsPort':mwAuthModeSecondaryTacacsPort,'mwAuthModeSecondaryTacacsSecret':mwAuthModeSecondaryTacacsSecret,'mwWapiServer':mwWapiServer,'mwWapiServerServerIp':mwWapiServerServerIp,'mwWapiServerServerPort':mwWapiServerServerPort,'mwCaptivePortalProfileTable':mwCaptivePortalProfileTable,'mwCaptivePortalProfileEntry':mwCaptivePortalProfileEntry,_N:mwCaptivePortalProfileTableIndex,'mwCaptivePortalProfileName':mwCaptivePortalProfileName,'mwCaptivePortalProfileRadiusProfileName':mwCaptivePortalProfileRadiusProfileName,'mwCaptivePortalProfileSecondaryRadiusProfileName':mwCaptivePortalProfileSecondaryRadiusProfileName,'mwCaptivePortalProfilePrimaryAccountingRadiusServer':mwCaptivePortalProfilePrimaryAccountingRadiusServer,'mwCaptivePortalProfileSecondaryAccountingRadiusServer':mwCaptivePortalProfileSecondaryAccountingRadiusServer,'mwCaptivePortalProfileAccountingInterimInterval':mwCaptivePortalProfileAccountingInterimInterval,'mwCaptivePortalProfileOverrideRadius':mwCaptivePortalProfileOverrideRadius,'mwCaptivePortalProfileExternalCPURL':mwCaptivePortalProfileExternalCPURL,'mwCaptivePortalProfileExternalCPIP':mwCaptivePortalProfileExternalCPIP,'mwCaptivePortalProfileCaptivePortalSessionTimeout':mwCaptivePortalProfileCaptivePortalSessionTimeout,'mwCaptivePortalProfileCaptivePortalActivityTimeout':mwCaptivePortalProfileCaptivePortalActivityTimeout,'mwCaptivePortalProfileL3UserSessionTimeout':mwCaptivePortalProfileL3UserSessionTimeout,'mwCaptivePortalProfileAutoLogin':mwCaptivePortalProfileAutoLogin,'mwCaptivePortalProfileOwner':mwCaptivePortalProfileOwner,'mwCaptivePortalProfileExternalServer':mwCaptivePortalProfileExternalServer,'mwCaptivePortalProfileCpExemptionProfile':mwCaptivePortalProfileCpExemptionProfile,'mwCaptivePortalProfileRowStatus':mwCaptivePortalProfileRowStatus,'mwCaptivePortalExemptionTable':mwCaptivePortalExemptionTable,'mwCaptivePortalExemptionEntry':mwCaptivePortalExemptionEntry,_O:mwCaptivePortalExemptionTableIndex,'mwCaptivePortalExemptionName':mwCaptivePortalExemptionName,'mwCaptivePortalExemptionDescr':mwCaptivePortalExemptionDescr,'mwCaptivePortalExemptionFqdn':mwCaptivePortalExemptionFqdn,'mwCaptivePortalExemptionOwner':mwCaptivePortalExemptionOwner,'mwCaptivePortalExemptionRowStatus':mwCaptivePortalExemptionRowStatus})