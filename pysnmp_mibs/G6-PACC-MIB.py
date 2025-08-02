_Z='userStatusIndex'
_Y='port8021xStatusPortIndex'
_X='portMacStatusPortIndex'
_W='viaMacEventOnly'
_V='portStatusPortIndex'
_U='supplicantIndex'
_T='authorizedMacsIndex'
_S='portConfigPortIndex'
_R='edge8021xViaRadius'
_Q='ms8021xViaRadius'
_P='macViaRadius'
_O='viaMacTable'
_N='rejected'
_M='authorized'
_L='processing'
_K='unauthorized'
_J='undefined'
_I='none'
_H='enabled'
_G='not-accessible'
_F='G6-PACC-MIB'
_E='disabled'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Pacc_ObjectIdentity=ObjectIdentity
pacc=_Pacc_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,46))
class _PaccEnablePortAccessControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PaccEnablePortAccessControl_Type.__name__=_B
_PaccEnablePortAccessControl_Object=MibScalar
paccEnablePortAccessControl=_PaccEnablePortAccessControl_Object((1,3,6,1,4,1,3181,10,6,2,46,1),_PaccEnablePortAccessControl_Type())
paccEnablePortAccessControl.setMaxAccess(_C)
if mibBuilder.loadTexts:paccEnablePortAccessControl.setStatus(_A)
_PaccReauthenticationPeriod_Type=Unsigned32
_PaccReauthenticationPeriod_Object=MibScalar
paccReauthenticationPeriod=_PaccReauthenticationPeriod_Object((1,3,6,1,4,1,3181,10,6,2,46,2),_PaccReauthenticationPeriod_Type())
paccReauthenticationPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:paccReauthenticationPeriod.setStatus(_A)
_PaccNasIdentifier_Type=DisplayString
_PaccNasIdentifier_Object=MibScalar
paccNasIdentifier=_PaccNasIdentifier_Object((1,3,6,1,4,1,3181,10,6,2,46,3),_PaccNasIdentifier_Type())
paccNasIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:paccNasIdentifier.setStatus(_A)
_PaccMacSeparatorChar_Type=DisplayString
_PaccMacSeparatorChar_Object=MibScalar
paccMacSeparatorChar=_PaccMacSeparatorChar_Object((1,3,6,1,4,1,3181,10,6,2,46,4),_PaccMacSeparatorChar_Type())
paccMacSeparatorChar.setMaxAccess(_C)
if mibBuilder.loadTexts:paccMacSeparatorChar.setStatus(_A)
class _PaccMacSpelling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('lowerCase',0),('upperCase',1)))
_PaccMacSpelling_Type.__name__=_B
_PaccMacSpelling_Object=MibScalar
paccMacSpelling=_PaccMacSpelling_Object((1,3,6,1,4,1,3181,10,6,2,46,5),_PaccMacSpelling_Type())
paccMacSpelling.setMaxAccess(_C)
if mibBuilder.loadTexts:paccMacSpelling.setStatus(_A)
class _PaccMacPasswordSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('useMac',0),('usePassword',1)))
_PaccMacPasswordSource_Type.__name__=_B
_PaccMacPasswordSource_Object=MibScalar
paccMacPasswordSource=_PaccMacPasswordSource_Object((1,3,6,1,4,1,3181,10,6,2,46,6),_PaccMacPasswordSource_Type())
paccMacPasswordSource.setMaxAccess(_C)
if mibBuilder.loadTexts:paccMacPasswordSource.setStatus(_A)
_PaccMacPasswordString_Type=DisplayString
_PaccMacPasswordString_Object=MibScalar
paccMacPasswordString=_PaccMacPasswordString_Object((1,3,6,1,4,1,3181,10,6,2,46,7),_PaccMacPasswordString_Type())
paccMacPasswordString.setMaxAccess(_C)
if mibBuilder.loadTexts:paccMacPasswordString.setStatus(_A)
_PaccPrimaryAuthServerName_Type=DisplayString
_PaccPrimaryAuthServerName_Object=MibScalar
paccPrimaryAuthServerName=_PaccPrimaryAuthServerName_Object((1,3,6,1,4,1,3181,10,6,2,46,8),_PaccPrimaryAuthServerName_Type())
paccPrimaryAuthServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:paccPrimaryAuthServerName.setStatus(_A)
_PaccPrimaryAcctServerName_Type=DisplayString
_PaccPrimaryAcctServerName_Object=MibScalar
paccPrimaryAcctServerName=_PaccPrimaryAcctServerName_Object((1,3,6,1,4,1,3181,10,6,2,46,9),_PaccPrimaryAcctServerName_Type())
paccPrimaryAcctServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:paccPrimaryAcctServerName.setStatus(_A)
_PaccFallbackAuthServerName_Type=DisplayString
_PaccFallbackAuthServerName_Object=MibScalar
paccFallbackAuthServerName=_PaccFallbackAuthServerName_Object((1,3,6,1,4,1,3181,10,6,2,46,10),_PaccFallbackAuthServerName_Type())
paccFallbackAuthServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:paccFallbackAuthServerName.setStatus(_A)
_PaccFallbackAcctServerName_Type=DisplayString
_PaccFallbackAcctServerName_Object=MibScalar
paccFallbackAcctServerName=_PaccFallbackAcctServerName_Object((1,3,6,1,4,1,3181,10,6,2,46,11),_PaccFallbackAcctServerName_Type())
paccFallbackAcctServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:paccFallbackAcctServerName.setStatus(_A)
class _PaccServerDownTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PaccServerDownTimeout_Type.__name__=_B
_PaccServerDownTimeout_Object=MibScalar
paccServerDownTimeout=_PaccServerDownTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,12),_PaccServerDownTimeout_Type())
paccServerDownTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:paccServerDownTimeout.setStatus(_A)
_PaccFilterAuthorizedMac_Type=DisplayString
_PaccFilterAuthorizedMac_Object=MibScalar
paccFilterAuthorizedMac=_PaccFilterAuthorizedMac_Object((1,3,6,1,4,1,3181,10,6,2,46,13),_PaccFilterAuthorizedMac_Type())
paccFilterAuthorizedMac.setMaxAccess(_C)
if mibBuilder.loadTexts:paccFilterAuthorizedMac.setStatus(_A)
_PaccFilterAuthorizedPort_Type=DisplayString
_PaccFilterAuthorizedPort_Object=MibScalar
paccFilterAuthorizedPort=_PaccFilterAuthorizedPort_Object((1,3,6,1,4,1,3181,10,6,2,46,14),_PaccFilterAuthorizedPort_Type())
paccFilterAuthorizedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:paccFilterAuthorizedPort.setStatus(_A)
_PaccFilterAuthorizedUser_Type=DisplayString
_PaccFilterAuthorizedUser_Object=MibScalar
paccFilterAuthorizedUser=_PaccFilterAuthorizedUser_Object((1,3,6,1,4,1,3181,10,6,2,46,15),_PaccFilterAuthorizedUser_Type())
paccFilterAuthorizedUser.setMaxAccess(_C)
if mibBuilder.loadTexts:paccFilterAuthorizedUser.setStatus(_A)
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,46,16))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigEntry_Object=MibTableRow
portConfigEntry=_PortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1))
portConfigEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:portConfigEntry.setStatus(_A)
class _PortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortConfigPortIndex_Type.__name__=_B
_PortConfigPortIndex_Object=MibTableColumn
portConfigPortIndex=_PortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,1),_PortConfigPortIndex_Type())
portConfigPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portConfigPortIndex.setStatus(_A)
class _PortConfigAuthorizeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('alwaysAuthorized',0),(_O,1),(_P,2),(_Q,3),('macOr8021xViaRadius',4),('forceUnauthorized',5),('macEventOnly',6),(_R,7)))
_PortConfigAuthorizeMode_Type.__name__=_B
_PortConfigAuthorizeMode_Object=MibTableColumn
portConfigAuthorizeMode=_PortConfigAuthorizeMode_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,2),_PortConfigAuthorizeMode_Type())
portConfigAuthorizeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAuthorizeMode.setStatus(_A)
class _PortConfigAuthorizePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('prefer8021x',0),('preferMac',1)))
_PortConfigAuthorizePriority_Type.__name__=_B
_PortConfigAuthorizePriority_Object=MibTableColumn
portConfigAuthorizePriority=_PortConfigAuthorizePriority_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,3),_PortConfigAuthorizePriority_Type())
portConfigAuthorizePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAuthorizePriority.setStatus(_A)
class _PortConfigUnauthorizedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('blocked',0),('useUnauthorizedVlan',1),('incomingBlocked',2)))
_PortConfigUnauthorizedMode_Type.__name__=_B
_PortConfigUnauthorizedMode_Object=MibTableColumn
portConfigUnauthorizedMode=_PortConfigUnauthorizedMode_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,4),_PortConfigUnauthorizedMode_Type())
portConfigUnauthorizedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigUnauthorizedMode.setStatus(_A)
_PortConfigAuthFailRetryTimer_Type=Unsigned32
_PortConfigAuthFailRetryTimer_Object=MibTableColumn
portConfigAuthFailRetryTimer=_PortConfigAuthFailRetryTimer_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,5),_PortConfigAuthFailRetryTimer_Type())
portConfigAuthFailRetryTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigAuthFailRetryTimer.setStatus(_A)
class _PortConfigMacTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('slow',1),('fast',2)))
_PortConfigMacTimeout_Type.__name__=_B
_PortConfigMacTimeout_Object=MibTableColumn
portConfigMacTimeout=_PortConfigMacTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,6),_PortConfigMacTimeout_Type())
portConfigMacTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigMacTimeout.setStatus(_A)
class _PortConfigLimitedNumberOfMacs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortConfigLimitedNumberOfMacs_Type.__name__=_B
_PortConfigLimitedNumberOfMacs_Object=MibTableColumn
portConfigLimitedNumberOfMacs=_PortConfigLimitedNumberOfMacs_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,7),_PortConfigLimitedNumberOfMacs_Type())
portConfigLimitedNumberOfMacs.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigLimitedNumberOfMacs.setStatus(_A)
class _PortConfigDropUnknownUnicasts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigDropUnknownUnicasts_Type.__name__=_B
_PortConfigDropUnknownUnicasts_Object=MibTableColumn
portConfigDropUnknownUnicasts=_PortConfigDropUnknownUnicasts_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,8),_PortConfigDropUnknownUnicasts_Type())
portConfigDropUnknownUnicasts.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigDropUnknownUnicasts.setStatus(_A)
class _PortConfigDropEgressBroadcasts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigDropEgressBroadcasts_Type.__name__=_B
_PortConfigDropEgressBroadcasts_Object=MibTableColumn
portConfigDropEgressBroadcasts=_PortConfigDropEgressBroadcasts_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,9),_PortConfigDropEgressBroadcasts_Type())
portConfigDropEgressBroadcasts.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigDropEgressBroadcasts.setStatus(_A)
_PortConfigLearnMacNow_Type=DisplayString
_PortConfigLearnMacNow_Object=MibTableColumn
portConfigLearnMacNow=_PortConfigLearnMacNow_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,10),_PortConfigLearnMacNow_Type())
portConfigLearnMacNow.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigLearnMacNow.setStatus(_A)
_PortConfigReauthenticate_Type=DisplayString
_PortConfigReauthenticate_Object=MibTableColumn
portConfigReauthenticate=_PortConfigReauthenticate_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,11),_PortConfigReauthenticate_Type())
portConfigReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigReauthenticate.setStatus(_A)
_PortConfigUnauthorizeMac_Type=DisplayString
_PortConfigUnauthorizeMac_Object=MibTableColumn
portConfigUnauthorizeMac=_PortConfigUnauthorizeMac_Object((1,3,6,1,4,1,3181,10,6,2,46,16,1,12),_PortConfigUnauthorizeMac_Type())
portConfigUnauthorizeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:portConfigUnauthorizeMac.setStatus(_A)
_AuthorizedMacsTable_Object=MibTable
authorizedMacsTable=_AuthorizedMacsTable_Object((1,3,6,1,4,1,3181,10,6,2,46,17))
if mibBuilder.loadTexts:authorizedMacsTable.setStatus(_A)
_AuthorizedMacsEntry_Object=MibTableRow
authorizedMacsEntry=_AuthorizedMacsEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1))
authorizedMacsEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:authorizedMacsEntry.setStatus(_A)
class _AuthorizedMacsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AuthorizedMacsIndex_Type.__name__=_B
_AuthorizedMacsIndex_Object=MibTableColumn
authorizedMacsIndex=_AuthorizedMacsIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1,1),_AuthorizedMacsIndex_Type())
authorizedMacsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:authorizedMacsIndex.setStatus(_A)
_AuthorizedMacsName_Type=DisplayString
_AuthorizedMacsName_Object=MibTableColumn
authorizedMacsName=_AuthorizedMacsName_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1,2),_AuthorizedMacsName_Type())
authorizedMacsName.setMaxAccess(_C)
if mibBuilder.loadTexts:authorizedMacsName.setStatus(_A)
_AuthorizedMacsMacAddress_Type=MacAddress
_AuthorizedMacsMacAddress_Object=MibTableColumn
authorizedMacsMacAddress=_AuthorizedMacsMacAddress_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1,3),_AuthorizedMacsMacAddress_Type())
authorizedMacsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:authorizedMacsMacAddress.setStatus(_A)
_AuthorizedMacsPermittedPorts_Type=Integer32
_AuthorizedMacsPermittedPorts_Object=MibTableColumn
authorizedMacsPermittedPorts=_AuthorizedMacsPermittedPorts_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1,4),_AuthorizedMacsPermittedPorts_Type())
authorizedMacsPermittedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:authorizedMacsPermittedPorts.setStatus(_A)
class _AuthorizedMacsTreatAsVendorMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_AuthorizedMacsTreatAsVendorMac_Type.__name__=_B
_AuthorizedMacsTreatAsVendorMac_Object=MibTableColumn
authorizedMacsTreatAsVendorMac=_AuthorizedMacsTreatAsVendorMac_Object((1,3,6,1,4,1,3181,10,6,2,46,17,1,5),_AuthorizedMacsTreatAsVendorMac_Type())
authorizedMacsTreatAsVendorMac.setMaxAccess(_C)
if mibBuilder.loadTexts:authorizedMacsTreatAsVendorMac.setStatus(_A)
_SupplicantTable_Object=MibTable
supplicantTable=_SupplicantTable_Object((1,3,6,1,4,1,3181,10,6,2,46,18))
if mibBuilder.loadTexts:supplicantTable.setStatus(_A)
_SupplicantEntry_Object=MibTableRow
supplicantEntry=_SupplicantEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1))
supplicantEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:supplicantEntry.setStatus(_A)
class _SupplicantIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_SupplicantIndex_Type.__name__=_B
_SupplicantIndex_Object=MibTableColumn
supplicantIndex=_SupplicantIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,1),_SupplicantIndex_Type())
supplicantIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:supplicantIndex.setStatus(_A)
class _SupplicantEnableSupplicant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_SupplicantEnableSupplicant_Type.__name__=_B
_SupplicantEnableSupplicant_Object=MibTableColumn
supplicantEnableSupplicant=_SupplicantEnableSupplicant_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,2),_SupplicantEnableSupplicant_Type())
supplicantEnableSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantEnableSupplicant.setStatus(_A)
class _SupplicantPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SupplicantPort_Type.__name__=_B
_SupplicantPort_Object=MibTableColumn
supplicantPort=_SupplicantPort_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,3),_SupplicantPort_Type())
supplicantPort.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantPort.setStatus(_A)
class _SupplicantActionOnLinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),('deauthenticate',1)))
_SupplicantActionOnLinkDown_Type.__name__=_B
_SupplicantActionOnLinkDown_Object=MibTableColumn
supplicantActionOnLinkDown=_SupplicantActionOnLinkDown_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,4),_SupplicantActionOnLinkDown_Type())
supplicantActionOnLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantActionOnLinkDown.setStatus(_A)
_SupplicantIdentity_Type=DisplayString
_SupplicantIdentity_Object=MibTableColumn
supplicantIdentity=_SupplicantIdentity_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,5),_SupplicantIdentity_Type())
supplicantIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantIdentity.setStatus(_A)
_SupplicantAnonymousIdentity_Type=DisplayString
_SupplicantAnonymousIdentity_Object=MibTableColumn
supplicantAnonymousIdentity=_SupplicantAnonymousIdentity_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,6),_SupplicantAnonymousIdentity_Type())
supplicantAnonymousIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantAnonymousIdentity.setStatus(_A)
_SupplicantAuthenticationProtocol_Type=DisplayString
_SupplicantAuthenticationProtocol_Object=MibTableColumn
supplicantAuthenticationProtocol=_SupplicantAuthenticationProtocol_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,7),_SupplicantAuthenticationProtocol_Type())
supplicantAuthenticationProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantAuthenticationProtocol.setStatus(_A)
_SupplicantEnterPassword_Type=DisplayString
_SupplicantEnterPassword_Object=MibTableColumn
supplicantEnterPassword=_SupplicantEnterPassword_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,8),_SupplicantEnterPassword_Type())
supplicantEnterPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantEnterPassword.setStatus(_A)
_SupplicantEncryptedAuthPassword_Type=DisplayString
_SupplicantEncryptedAuthPassword_Object=MibTableColumn
supplicantEncryptedAuthPassword=_SupplicantEncryptedAuthPassword_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,9),_SupplicantEncryptedAuthPassword_Type())
supplicantEncryptedAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantEncryptedAuthPassword.setStatus(_A)
_SupplicantReauthenticate_Type=DisplayString
_SupplicantReauthenticate_Object=MibTableColumn
supplicantReauthenticate=_SupplicantReauthenticate_Object((1,3,6,1,4,1,3181,10,6,2,46,18,1,10),_SupplicantReauthenticate_Type())
supplicantReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:supplicantReauthenticate.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,46,100))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusEntry_Object=MibTableRow
portStatusEntry=_PortStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1))
portStatusEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:portStatusEntry.setStatus(_A)
class _PortStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortStatusPortIndex_Type.__name__=_B
_PortStatusPortIndex_Object=MibTableColumn
portStatusPortIndex=_PortStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,1),_PortStatusPortIndex_Type())
portStatusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portStatusPortIndex.setStatus(_A)
class _PortStatusAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),(_E,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_PortStatusAuthorizationState_Type.__name__=_B
_PortStatusAuthorizationState_Object=MibTableColumn
portStatusAuthorizationState=_PortStatusAuthorizationState_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,2),_PortStatusAuthorizationState_Type())
portStatusAuthorizationState.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusAuthorizationState.setStatus(_A)
class _PortStatusAuthorizationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,7)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3),(_W,6),(_R,7)))
_PortStatusAuthorizationMode_Type.__name__=_B
_PortStatusAuthorizationMode_Object=MibTableColumn
portStatusAuthorizationMode=_PortStatusAuthorizationMode_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,3),_PortStatusAuthorizationMode_Type())
portStatusAuthorizationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusAuthorizationMode.setStatus(_A)
_PortStatusLastStateChange_Type=DisplayString
_PortStatusLastStateChange_Object=MibTableColumn
portStatusLastStateChange=_PortStatusLastStateChange_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,4),_PortStatusLastStateChange_Type())
portStatusLastStateChange.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusLastStateChange.setStatus(_A)
class _PortStatusNumberOfMacsToLearn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortStatusNumberOfMacsToLearn_Type.__name__=_B
_PortStatusNumberOfMacsToLearn_Object=MibTableColumn
portStatusNumberOfMacsToLearn=_PortStatusNumberOfMacsToLearn_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,5),_PortStatusNumberOfMacsToLearn_Type())
portStatusNumberOfMacsToLearn.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusNumberOfMacsToLearn.setStatus(_A)
class _PortStatusNumberOfLearnedMacs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortStatusNumberOfLearnedMacs_Type.__name__=_B
_PortStatusNumberOfLearnedMacs_Object=MibTableColumn
portStatusNumberOfLearnedMacs=_PortStatusNumberOfLearnedMacs_Object((1,3,6,1,4,1,3181,10,6,2,46,100,1,6),_PortStatusNumberOfLearnedMacs_Type())
portStatusNumberOfLearnedMacs.setMaxAccess(_D)
if mibBuilder.loadTexts:portStatusNumberOfLearnedMacs.setStatus(_A)
_PortMacStatusTable_Object=MibTable
portMacStatusTable=_PortMacStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,46,101))
if mibBuilder.loadTexts:portMacStatusTable.setStatus(_A)
_PortMacStatusEntry_Object=MibTableRow
portMacStatusEntry=_PortMacStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1))
portMacStatusEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:portMacStatusEntry.setStatus(_A)
class _PortMacStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortMacStatusPortIndex_Type.__name__=_B
_PortMacStatusPortIndex_Object=MibTableColumn
portMacStatusPortIndex=_PortMacStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,1),_PortMacStatusPortIndex_Type())
portMacStatusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portMacStatusPortIndex.setStatus(_A)
class _PortMacStatusAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),(_E,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_PortMacStatusAuthorizationState_Type.__name__=_B
_PortMacStatusAuthorizationState_Object=MibTableColumn
portMacStatusAuthorizationState=_PortMacStatusAuthorizationState_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,2),_PortMacStatusAuthorizationState_Type())
portMacStatusAuthorizationState.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusAuthorizationState.setStatus(_A)
_PortMacStatusUserMac_Type=MacAddress
_PortMacStatusUserMac_Object=MibTableColumn
portMacStatusUserMac=_PortMacStatusUserMac_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,3),_PortMacStatusUserMac_Type())
portMacStatusUserMac.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusUserMac.setStatus(_A)
_PortMacStatusUserName_Type=DisplayString
_PortMacStatusUserName_Object=MibTableColumn
portMacStatusUserName=_PortMacStatusUserName_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,4),_PortMacStatusUserName_Type())
portMacStatusUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusUserName.setStatus(_A)
_PortMacStatusVlanAlias_Type=DisplayString
_PortMacStatusVlanAlias_Object=MibTableColumn
portMacStatusVlanAlias=_PortMacStatusVlanAlias_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,5),_PortMacStatusVlanAlias_Type())
portMacStatusVlanAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusVlanAlias.setStatus(_A)
class _PortMacStatusVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortMacStatusVlanId_Type.__name__=_B
_PortMacStatusVlanId_Object=MibTableColumn
portMacStatusVlanId=_PortMacStatusVlanId_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,6),_PortMacStatusVlanId_Type())
portMacStatusVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusVlanId.setStatus(_A)
class _PortMacStatusIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortMacStatusIdleTimeout_Type.__name__=_B
_PortMacStatusIdleTimeout_Object=MibTableColumn
portMacStatusIdleTimeout=_PortMacStatusIdleTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,7),_PortMacStatusIdleTimeout_Type())
portMacStatusIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusIdleTimeout.setStatus(_A)
class _PortMacStatusSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortMacStatusSessionTimeout_Type.__name__=_B
_PortMacStatusSessionTimeout_Object=MibTableColumn
portMacStatusSessionTimeout=_PortMacStatusSessionTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,8),_PortMacStatusSessionTimeout_Type())
portMacStatusSessionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusSessionTimeout.setStatus(_A)
_PortMacStatusFilterId_Type=DisplayString
_PortMacStatusFilterId_Object=MibTableColumn
portMacStatusFilterId=_PortMacStatusFilterId_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,9),_PortMacStatusFilterId_Type())
portMacStatusFilterId.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusFilterId.setStatus(_A)
_PortMacStatusLastStateChange_Type=DisplayString
_PortMacStatusLastStateChange_Object=MibTableColumn
portMacStatusLastStateChange=_PortMacStatusLastStateChange_Object((1,3,6,1,4,1,3181,10,6,2,46,101,1,10),_PortMacStatusLastStateChange_Type())
portMacStatusLastStateChange.setMaxAccess(_D)
if mibBuilder.loadTexts:portMacStatusLastStateChange.setStatus(_A)
_Port8021xStatusTable_Object=MibTable
port8021xStatusTable=_Port8021xStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,46,102))
if mibBuilder.loadTexts:port8021xStatusTable.setStatus(_A)
_Port8021xStatusEntry_Object=MibTableRow
port8021xStatusEntry=_Port8021xStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1))
port8021xStatusEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:port8021xStatusEntry.setStatus(_A)
class _Port8021xStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Port8021xStatusPortIndex_Type.__name__=_B
_Port8021xStatusPortIndex_Object=MibTableColumn
port8021xStatusPortIndex=_Port8021xStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,1),_Port8021xStatusPortIndex_Type())
port8021xStatusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:port8021xStatusPortIndex.setStatus(_A)
class _Port8021xStatusAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),(_E,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_Port8021xStatusAuthorizationState_Type.__name__=_B
_Port8021xStatusAuthorizationState_Object=MibTableColumn
port8021xStatusAuthorizationState=_Port8021xStatusAuthorizationState_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,2),_Port8021xStatusAuthorizationState_Type())
port8021xStatusAuthorizationState.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusAuthorizationState.setStatus(_A)
_Port8021xStatusUserMac_Type=MacAddress
_Port8021xStatusUserMac_Object=MibTableColumn
port8021xStatusUserMac=_Port8021xStatusUserMac_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,3),_Port8021xStatusUserMac_Type())
port8021xStatusUserMac.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusUserMac.setStatus(_A)
_Port8021xStatusUserName_Type=DisplayString
_Port8021xStatusUserName_Object=MibTableColumn
port8021xStatusUserName=_Port8021xStatusUserName_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,4),_Port8021xStatusUserName_Type())
port8021xStatusUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusUserName.setStatus(_A)
_Port8021xStatusVlanAlias_Type=DisplayString
_Port8021xStatusVlanAlias_Object=MibTableColumn
port8021xStatusVlanAlias=_Port8021xStatusVlanAlias_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,5),_Port8021xStatusVlanAlias_Type())
port8021xStatusVlanAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusVlanAlias.setStatus(_A)
class _Port8021xStatusVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Port8021xStatusVlanId_Type.__name__=_B
_Port8021xStatusVlanId_Object=MibTableColumn
port8021xStatusVlanId=_Port8021xStatusVlanId_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,6),_Port8021xStatusVlanId_Type())
port8021xStatusVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusVlanId.setStatus(_A)
class _Port8021xStatusIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Port8021xStatusIdleTimeout_Type.__name__=_B
_Port8021xStatusIdleTimeout_Object=MibTableColumn
port8021xStatusIdleTimeout=_Port8021xStatusIdleTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,7),_Port8021xStatusIdleTimeout_Type())
port8021xStatusIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusIdleTimeout.setStatus(_A)
class _Port8021xStatusSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Port8021xStatusSessionTimeout_Type.__name__=_B
_Port8021xStatusSessionTimeout_Object=MibTableColumn
port8021xStatusSessionTimeout=_Port8021xStatusSessionTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,8),_Port8021xStatusSessionTimeout_Type())
port8021xStatusSessionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusSessionTimeout.setStatus(_A)
_Port8021xStatusFilterId_Type=DisplayString
_Port8021xStatusFilterId_Object=MibTableColumn
port8021xStatusFilterId=_Port8021xStatusFilterId_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,9),_Port8021xStatusFilterId_Type())
port8021xStatusFilterId.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusFilterId.setStatus(_A)
_Port8021xStatusLastStateChange_Type=DisplayString
_Port8021xStatusLastStateChange_Object=MibTableColumn
port8021xStatusLastStateChange=_Port8021xStatusLastStateChange_Object((1,3,6,1,4,1,3181,10,6,2,46,102,1,10),_Port8021xStatusLastStateChange_Type())
port8021xStatusLastStateChange.setMaxAccess(_D)
if mibBuilder.loadTexts:port8021xStatusLastStateChange.setStatus(_A)
_UserStatusTable_Object=MibTable
userStatusTable=_UserStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,46,103))
if mibBuilder.loadTexts:userStatusTable.setStatus(_A)
_UserStatusEntry_Object=MibTableRow
userStatusEntry=_UserStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1))
userStatusEntry.setIndexNames((0,_F,_Z))
if mibBuilder.loadTexts:userStatusEntry.setStatus(_A)
class _UserStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,249))
_UserStatusIndex_Type.__name__=_B
_UserStatusIndex_Object=MibTableColumn
userStatusIndex=_UserStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,1),_UserStatusIndex_Type())
userStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:userStatusIndex.setStatus(_A)
class _UserStatusEntryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unused',0),('inactive',1),('active',2)))
_UserStatusEntryState_Type.__name__=_B
_UserStatusEntryState_Object=MibTableColumn
userStatusEntryState=_UserStatusEntryState_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,2),_UserStatusEntryState_Type())
userStatusEntryState.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusEntryState.setStatus(_A)
class _UserStatusAuthorizationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),(_E,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_UserStatusAuthorizationState_Type.__name__=_B
_UserStatusAuthorizationState_Object=MibTableColumn
userStatusAuthorizationState=_UserStatusAuthorizationState_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,3),_UserStatusAuthorizationState_Type())
userStatusAuthorizationState.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusAuthorizationState.setStatus(_A)
class _UserStatusAuthorizationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,7)));namedValues=NamedValues(*((_I,0),(_O,1),(_P,2),(_Q,3),(_W,6),(_R,7)))
_UserStatusAuthorizationMode_Type.__name__=_B
_UserStatusAuthorizationMode_Object=MibTableColumn
userStatusAuthorizationMode=_UserStatusAuthorizationMode_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,4),_UserStatusAuthorizationMode_Type())
userStatusAuthorizationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusAuthorizationMode.setStatus(_A)
class _UserStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UserStatusPort_Type.__name__=_B
_UserStatusPort_Object=MibTableColumn
userStatusPort=_UserStatusPort_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,5),_UserStatusPort_Type())
userStatusPort.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusPort.setStatus(_A)
_UserStatusUserMac_Type=MacAddress
_UserStatusUserMac_Object=MibTableColumn
userStatusUserMac=_UserStatusUserMac_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,6),_UserStatusUserMac_Type())
userStatusUserMac.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusUserMac.setStatus(_A)
_UserStatusUserName_Type=DisplayString
_UserStatusUserName_Object=MibTableColumn
userStatusUserName=_UserStatusUserName_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,7),_UserStatusUserName_Type())
userStatusUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusUserName.setStatus(_A)
_UserStatusVlanAlias_Type=DisplayString
_UserStatusVlanAlias_Object=MibTableColumn
userStatusVlanAlias=_UserStatusVlanAlias_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,8),_UserStatusVlanAlias_Type())
userStatusVlanAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusVlanAlias.setStatus(_A)
class _UserStatusVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UserStatusVlanId_Type.__name__=_B
_UserStatusVlanId_Object=MibTableColumn
userStatusVlanId=_UserStatusVlanId_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,9),_UserStatusVlanId_Type())
userStatusVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusVlanId.setStatus(_A)
class _UserStatusIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UserStatusIdleTimeout_Type.__name__=_B
_UserStatusIdleTimeout_Object=MibTableColumn
userStatusIdleTimeout=_UserStatusIdleTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,10),_UserStatusIdleTimeout_Type())
userStatusIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusIdleTimeout.setStatus(_A)
class _UserStatusSessionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_UserStatusSessionTimeout_Type.__name__=_B
_UserStatusSessionTimeout_Object=MibTableColumn
userStatusSessionTimeout=_UserStatusSessionTimeout_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,11),_UserStatusSessionTimeout_Type())
userStatusSessionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusSessionTimeout.setStatus(_A)
_UserStatusFilterId_Type=DisplayString
_UserStatusFilterId_Object=MibTableColumn
userStatusFilterId=_UserStatusFilterId_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,12),_UserStatusFilterId_Type())
userStatusFilterId.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusFilterId.setStatus(_A)
_UserStatusLoginTimeStamp_Type=DisplayString
_UserStatusLoginTimeStamp_Object=MibTableColumn
userStatusLoginTimeStamp=_UserStatusLoginTimeStamp_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,13),_UserStatusLoginTimeStamp_Type())
userStatusLoginTimeStamp.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusLoginTimeStamp.setStatus(_A)
_UserStatusLoginEpoch_Type=Unsigned32
_UserStatusLoginEpoch_Object=MibTableColumn
userStatusLoginEpoch=_UserStatusLoginEpoch_Object((1,3,6,1,4,1,3181,10,6,2,46,103,1,14),_UserStatusLoginEpoch_Type())
userStatusLoginEpoch.setMaxAccess(_D)
if mibBuilder.loadTexts:userStatusLoginEpoch.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'protocol':protocol,'pacc':pacc,'paccEnablePortAccessControl':paccEnablePortAccessControl,'paccReauthenticationPeriod':paccReauthenticationPeriod,'paccNasIdentifier':paccNasIdentifier,'paccMacSeparatorChar':paccMacSeparatorChar,'paccMacSpelling':paccMacSpelling,'paccMacPasswordSource':paccMacPasswordSource,'paccMacPasswordString':paccMacPasswordString,'paccPrimaryAuthServerName':paccPrimaryAuthServerName,'paccPrimaryAcctServerName':paccPrimaryAcctServerName,'paccFallbackAuthServerName':paccFallbackAuthServerName,'paccFallbackAcctServerName':paccFallbackAcctServerName,'paccServerDownTimeout':paccServerDownTimeout,'paccFilterAuthorizedMac':paccFilterAuthorizedMac,'paccFilterAuthorizedPort':paccFilterAuthorizedPort,'paccFilterAuthorizedUser':paccFilterAuthorizedUser,'portConfigTable':portConfigTable,'portConfigEntry':portConfigEntry,_S:portConfigPortIndex,'portConfigAuthorizeMode':portConfigAuthorizeMode,'portConfigAuthorizePriority':portConfigAuthorizePriority,'portConfigUnauthorizedMode':portConfigUnauthorizedMode,'portConfigAuthFailRetryTimer':portConfigAuthFailRetryTimer,'portConfigMacTimeout':portConfigMacTimeout,'portConfigLimitedNumberOfMacs':portConfigLimitedNumberOfMacs,'portConfigDropUnknownUnicasts':portConfigDropUnknownUnicasts,'portConfigDropEgressBroadcasts':portConfigDropEgressBroadcasts,'portConfigLearnMacNow':portConfigLearnMacNow,'portConfigReauthenticate':portConfigReauthenticate,'portConfigUnauthorizeMac':portConfigUnauthorizeMac,'authorizedMacsTable':authorizedMacsTable,'authorizedMacsEntry':authorizedMacsEntry,_T:authorizedMacsIndex,'authorizedMacsName':authorizedMacsName,'authorizedMacsMacAddress':authorizedMacsMacAddress,'authorizedMacsPermittedPorts':authorizedMacsPermittedPorts,'authorizedMacsTreatAsVendorMac':authorizedMacsTreatAsVendorMac,'supplicantTable':supplicantTable,'supplicantEntry':supplicantEntry,_U:supplicantIndex,'supplicantEnableSupplicant':supplicantEnableSupplicant,'supplicantPort':supplicantPort,'supplicantActionOnLinkDown':supplicantActionOnLinkDown,'supplicantIdentity':supplicantIdentity,'supplicantAnonymousIdentity':supplicantAnonymousIdentity,'supplicantAuthenticationProtocol':supplicantAuthenticationProtocol,'supplicantEnterPassword':supplicantEnterPassword,'supplicantEncryptedAuthPassword':supplicantEncryptedAuthPassword,'supplicantReauthenticate':supplicantReauthenticate,'portStatusTable':portStatusTable,'portStatusEntry':portStatusEntry,_V:portStatusPortIndex,'portStatusAuthorizationState':portStatusAuthorizationState,'portStatusAuthorizationMode':portStatusAuthorizationMode,'portStatusLastStateChange':portStatusLastStateChange,'portStatusNumberOfMacsToLearn':portStatusNumberOfMacsToLearn,'portStatusNumberOfLearnedMacs':portStatusNumberOfLearnedMacs,'portMacStatusTable':portMacStatusTable,'portMacStatusEntry':portMacStatusEntry,_X:portMacStatusPortIndex,'portMacStatusAuthorizationState':portMacStatusAuthorizationState,'portMacStatusUserMac':portMacStatusUserMac,'portMacStatusUserName':portMacStatusUserName,'portMacStatusVlanAlias':portMacStatusVlanAlias,'portMacStatusVlanId':portMacStatusVlanId,'portMacStatusIdleTimeout':portMacStatusIdleTimeout,'portMacStatusSessionTimeout':portMacStatusSessionTimeout,'portMacStatusFilterId':portMacStatusFilterId,'portMacStatusLastStateChange':portMacStatusLastStateChange,'port8021xStatusTable':port8021xStatusTable,'port8021xStatusEntry':port8021xStatusEntry,_Y:port8021xStatusPortIndex,'port8021xStatusAuthorizationState':port8021xStatusAuthorizationState,'port8021xStatusUserMac':port8021xStatusUserMac,'port8021xStatusUserName':port8021xStatusUserName,'port8021xStatusVlanAlias':port8021xStatusVlanAlias,'port8021xStatusVlanId':port8021xStatusVlanId,'port8021xStatusIdleTimeout':port8021xStatusIdleTimeout,'port8021xStatusSessionTimeout':port8021xStatusSessionTimeout,'port8021xStatusFilterId':port8021xStatusFilterId,'port8021xStatusLastStateChange':port8021xStatusLastStateChange,'userStatusTable':userStatusTable,'userStatusEntry':userStatusEntry,_Z:userStatusIndex,'userStatusEntryState':userStatusEntryState,'userStatusAuthorizationState':userStatusAuthorizationState,'userStatusAuthorizationMode':userStatusAuthorizationMode,'userStatusPort':userStatusPort,'userStatusUserMac':userStatusUserMac,'userStatusUserName':userStatusUserName,'userStatusVlanAlias':userStatusVlanAlias,'userStatusVlanId':userStatusVlanId,'userStatusIdleTimeout':userStatusIdleTimeout,'userStatusSessionTimeout':userStatusSessionTimeout,'userStatusFilterId':userStatusFilterId,'userStatusLoginTimeStamp':userStatusLoginTimeStamp,'userStatusLoginEpoch':userStatusLoginEpoch})