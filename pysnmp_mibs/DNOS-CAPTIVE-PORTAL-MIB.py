_l='cpCaptivePortalClientUserName'
_k='cpCaptivePortalClientStatisticsEntry'
_j='cpCaptivePortalConfigWebWebId'
_i='cpCaptivePortalConfigWebInstanceId'
_h='cpCaptivePortalInstanceClientAssocMacAddress'
_g='cpCaptivePortalInstanceClientAssocInstanceId'
_f='cpCaptivePortalIntfClientAssocMacAddress'
_e='cpCaptivePortalIntfClientIfIndex'
_d='notBlocked'
_c='blocked'
_b='cpIntfAssociationIfIndex'
_a='cpIntfAssociationCPID'
_Z='cpLocalUserGroupAssociationGroupIndex'
_Y='cpLocalUserGroupAssociationUserIndex'
_X='cpLocalUserIndex'
_W='cpLocalUserGroupIndex'
_V='radius'
_U='cpCaptivePortalIntfIfIndex'
_T='adminDisabled'
_S='local'
_R='cpCaptivePortalClientSwitchMacAddress'
_Q='cpCaptivePortalClientAssocIfIndex'
_P='cpCaptivePortalClientCPID'
_O='cpCaptivePortalClientIpAddress'
_N='none'
_M='cpCaptivePortalInstanceId'
_L='cpCaptivePortalClientMacAddress'
_K='read-create'
_J='not-accessible'
_I='DisplayString'
_H='disable'
_G='enable'
_F='Unsigned32'
_E='DNOS-CAPTIVE-PORTAL-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathCaptivePortal=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38))
if mibBuilder.loadTexts:fastPathCaptivePortal.setRevisions(('2011-01-26 00:00','2007-07-09 00:00'))
class CpCaptivePortalIntfCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('sessionTimeout',1),('idleTimeout',2),('maxBytesReceivedCounter',3),('maxBytesTransmittedCounter',4),('maxPacketsReceivedCounter',5),('maxPacketsTransmittedCounter',6),('clientRoaming',7)))
_CpConfigGroup_ObjectIdentity=ObjectIdentity
cpConfigGroup=_CpConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1))
_CpGlobalConfigGroup_ObjectIdentity=ObjectIdentity
cpGlobalConfigGroup=_CpGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1))
class _CpAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpAdminMode_Type.__name__=_D
_CpAdminMode_Object=MibScalar
cpAdminMode=_CpAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1,1),_CpAdminMode_Type())
cpAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAdminMode.setStatus(_A)
class _CpAdditionalHttpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpAdditionalHttpPort_Type.__name__=_D
_CpAdditionalHttpPort_Object=MibScalar
cpAdditionalHttpPort=_CpAdditionalHttpPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1,2),_CpAdditionalHttpPort_Type())
cpAdditionalHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAdditionalHttpPort.setStatus(_A)
class _CpAdditionalHttpSecurePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpAdditionalHttpSecurePort_Type.__name__=_D
_CpAdditionalHttpSecurePort_Object=MibScalar
cpAdditionalHttpSecurePort=_CpAdditionalHttpSecurePort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1,3),_CpAdditionalHttpSecurePort_Type())
cpAdditionalHttpSecurePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAdditionalHttpSecurePort.setStatus(_A)
class _CpPeerStatsReportingInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(15,3600))
_CpPeerStatsReportingInterval_Type.__name__=_D
_CpPeerStatsReportingInterval_Object=MibScalar
cpPeerStatsReportingInterval=_CpPeerStatsReportingInterval_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1,4),_CpPeerStatsReportingInterval_Type())
cpPeerStatsReportingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cpPeerStatsReportingInterval.setStatus(_A)
class _CpAuthTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_CpAuthTimeout_Type.__name__=_D
_CpAuthTimeout_Object=MibScalar
cpAuthTimeout=_CpAuthTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,1,5),_CpAuthTimeout_Type())
cpAuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpAuthTimeout.setStatus(_A)
_CpCaptivePortalConfigGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalConfigGroup=_CpCaptivePortalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2))
_CpCaptivePortalTable_Object=MibTable
cpCaptivePortalTable=_CpCaptivePortalTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1))
if mibBuilder.loadTexts:cpCaptivePortalTable.setStatus(_A)
_CpCaptivePortalEntry_Object=MibTableRow
cpCaptivePortalEntry=_CpCaptivePortalEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1))
cpCaptivePortalEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:cpCaptivePortalEntry.setStatus(_A)
_CpCaptivePortalInstanceId_Type=Unsigned32
_CpCaptivePortalInstanceId_Object=MibTableColumn
cpCaptivePortalInstanceId=_CpCaptivePortalInstanceId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,1),_CpCaptivePortalInstanceId_Type())
cpCaptivePortalInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceId.setStatus(_A)
class _CpCaptivePortalConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpCaptivePortalConfigName_Type.__name__=_I
_CpCaptivePortalConfigName_Object=MibTableColumn
cpCaptivePortalConfigName=_CpCaptivePortalConfigName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,2),_CpCaptivePortalConfigName_Type())
cpCaptivePortalConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalConfigName.setStatus(_A)
class _CpCaptivePortalAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpCaptivePortalAdminMode_Type.__name__=_D
_CpCaptivePortalAdminMode_Object=MibTableColumn
cpCaptivePortalAdminMode=_CpCaptivePortalAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,3),_CpCaptivePortalAdminMode_Type())
cpCaptivePortalAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalAdminMode.setStatus(_A)
class _CpCaptivePortalProtocolMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('https',0),('http',1)))
_CpCaptivePortalProtocolMode_Type.__name__=_D
_CpCaptivePortalProtocolMode_Object=MibTableColumn
cpCaptivePortalProtocolMode=_CpCaptivePortalProtocolMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,4),_CpCaptivePortalProtocolMode_Type())
cpCaptivePortalProtocolMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalProtocolMode.setStatus(_A)
class _CpCaptivePortalVerificationMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('guest',0),(_S,1),(_V,2)))
_CpCaptivePortalVerificationMode_Type.__name__=_D
_CpCaptivePortalVerificationMode_Object=MibTableColumn
cpCaptivePortalVerificationMode=_CpCaptivePortalVerificationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,5),_CpCaptivePortalVerificationMode_Type())
cpCaptivePortalVerificationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalVerificationMode.setStatus(_A)
class _CpCaptivePortalUserGroup_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CpCaptivePortalUserGroup_Type.__name__=_F
_CpCaptivePortalUserGroup_Object=MibTableColumn
cpCaptivePortalUserGroup=_CpCaptivePortalUserGroup_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,6),_CpCaptivePortalUserGroup_Type())
cpCaptivePortalUserGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalUserGroup.setStatus(_A)
class _CpCaptivePortalURLRedirectMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpCaptivePortalURLRedirectMode_Type.__name__=_D
_CpCaptivePortalURLRedirectMode_Object=MibTableColumn
cpCaptivePortalURLRedirectMode=_CpCaptivePortalURLRedirectMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,7),_CpCaptivePortalURLRedirectMode_Type())
cpCaptivePortalURLRedirectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalURLRedirectMode.setStatus(_A)
class _CpCaptivePortalRedirectURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CpCaptivePortalRedirectURL_Type.__name__=_I
_CpCaptivePortalRedirectURL_Object=MibTableColumn
cpCaptivePortalRedirectURL=_CpCaptivePortalRedirectURL_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,8),_CpCaptivePortalRedirectURL_Type())
cpCaptivePortalRedirectURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalRedirectURL.setStatus(_A)
class _CpCaptivePortalSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_CpCaptivePortalSessionTimeout_Type.__name__=_F
_CpCaptivePortalSessionTimeout_Object=MibTableColumn
cpCaptivePortalSessionTimeout=_CpCaptivePortalSessionTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,9),_CpCaptivePortalSessionTimeout_Type())
cpCaptivePortalSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalSessionTimeout.setStatus(_A)
class _CpCaptivePortalIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_CpCaptivePortalIdleTimeout_Type.__name__=_F
_CpCaptivePortalIdleTimeout_Object=MibTableColumn
cpCaptivePortalIdleTimeout=_CpCaptivePortalIdleTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,10),_CpCaptivePortalIdleTimeout_Type())
cpCaptivePortalIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalIdleTimeout.setStatus(_A)
class _CpCaptivePortalRadiusAuthServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpCaptivePortalRadiusAuthServer_Type.__name__=_I
_CpCaptivePortalRadiusAuthServer_Object=MibTableColumn
cpCaptivePortalRadiusAuthServer=_CpCaptivePortalRadiusAuthServer_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,11),_CpCaptivePortalRadiusAuthServer_Type())
cpCaptivePortalRadiusAuthServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalRadiusAuthServer.setStatus(_A)
class _CpCaptivePortalMaxBandwidthUp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,536870911))
_CpCaptivePortalMaxBandwidthUp_Type.__name__=_F
_CpCaptivePortalMaxBandwidthUp_Object=MibTableColumn
cpCaptivePortalMaxBandwidthUp=_CpCaptivePortalMaxBandwidthUp_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,12),_CpCaptivePortalMaxBandwidthUp_Type())
cpCaptivePortalMaxBandwidthUp.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalMaxBandwidthUp.setStatus(_A)
class _CpCaptivePortalMaxBandwidthDown_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,536870911))
_CpCaptivePortalMaxBandwidthDown_Type.__name__=_F
_CpCaptivePortalMaxBandwidthDown_Object=MibTableColumn
cpCaptivePortalMaxBandwidthDown=_CpCaptivePortalMaxBandwidthDown_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,13),_CpCaptivePortalMaxBandwidthDown_Type())
cpCaptivePortalMaxBandwidthDown.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalMaxBandwidthDown.setStatus(_A)
class _CpCaptivePortalMaxInputOctets_Type(Unsigned32):defaultValue=0
_CpCaptivePortalMaxInputOctets_Type.__name__=_F
_CpCaptivePortalMaxInputOctets_Object=MibTableColumn
cpCaptivePortalMaxInputOctets=_CpCaptivePortalMaxInputOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,14),_CpCaptivePortalMaxInputOctets_Type())
cpCaptivePortalMaxInputOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalMaxInputOctets.setStatus(_A)
class _CpCaptivePortalMaxOutputOctets_Type(Unsigned32):defaultValue=0
_CpCaptivePortalMaxOutputOctets_Type.__name__=_F
_CpCaptivePortalMaxOutputOctets_Object=MibTableColumn
cpCaptivePortalMaxOutputOctets=_CpCaptivePortalMaxOutputOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,15),_CpCaptivePortalMaxOutputOctets_Type())
cpCaptivePortalMaxOutputOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalMaxOutputOctets.setStatus(_A)
class _CpCaptivePortalMaxTotalOctets_Type(Unsigned32):defaultValue=0
_CpCaptivePortalMaxTotalOctets_Type.__name__=_F
_CpCaptivePortalMaxTotalOctets_Object=MibTableColumn
cpCaptivePortalMaxTotalOctets=_CpCaptivePortalMaxTotalOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,16),_CpCaptivePortalMaxTotalOctets_Type())
cpCaptivePortalMaxTotalOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalMaxTotalOctets.setStatus(_A)
class _CpCaptivePortalUserLogoutMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpCaptivePortalUserLogoutMode_Type.__name__=_D
_CpCaptivePortalUserLogoutMode_Object=MibTableColumn
cpCaptivePortalUserLogoutMode=_CpCaptivePortalUserLogoutMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,17),_CpCaptivePortalUserLogoutMode_Type())
cpCaptivePortalUserLogoutMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalUserLogoutMode.setStatus(_A)
_CpCaptivePortalRowStatus_Type=RowStatus
_CpCaptivePortalRowStatus_Object=MibTableColumn
cpCaptivePortalRowStatus=_CpCaptivePortalRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,2,1,1,18),_CpCaptivePortalRowStatus_Type())
cpCaptivePortalRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpCaptivePortalRowStatus.setStatus(_A)
_CpLocalUserDatabaseGroup_ObjectIdentity=ObjectIdentity
cpLocalUserDatabaseGroup=_CpLocalUserDatabaseGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3))
_CpLocalUserGroupTable_Object=MibTable
cpLocalUserGroupTable=_CpLocalUserGroupTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,1))
if mibBuilder.loadTexts:cpLocalUserGroupTable.setStatus(_A)
_CpLocalUserGroupEntry_Object=MibTableRow
cpLocalUserGroupEntry=_CpLocalUserGroupEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,1,1))
cpLocalUserGroupEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:cpLocalUserGroupEntry.setStatus(_A)
class _CpLocalUserGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupIndex_Type.__name__=_D
_CpLocalUserGroupIndex_Object=MibTableColumn
cpLocalUserGroupIndex=_CpLocalUserGroupIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,1,1,1),_CpLocalUserGroupIndex_Type())
cpLocalUserGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpLocalUserGroupIndex.setStatus(_A)
class _CpLocalUserGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CpLocalUserGroupName_Type.__name__=_I
_CpLocalUserGroupName_Object=MibTableColumn
cpLocalUserGroupName=_CpLocalUserGroupName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,1,1,2),_CpLocalUserGroupName_Type())
cpLocalUserGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserGroupName.setStatus(_A)
_CpLocalUserGroupRowStatus_Type=RowStatus
_CpLocalUserGroupRowStatus_Object=MibTableColumn
cpLocalUserGroupRowStatus=_CpLocalUserGroupRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,1,1,3),_CpLocalUserGroupRowStatus_Type())
cpLocalUserGroupRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserGroupRowStatus.setStatus(_A)
_CpLocalUserTable_Object=MibTable
cpLocalUserTable=_CpLocalUserTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2))
if mibBuilder.loadTexts:cpLocalUserTable.setStatus(_A)
_CpLocalUserEntry_Object=MibTableRow
cpLocalUserEntry=_CpLocalUserEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1))
cpLocalUserEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:cpLocalUserEntry.setStatus(_A)
class _CpLocalUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserIndex_Type.__name__=_D
_CpLocalUserIndex_Object=MibTableColumn
cpLocalUserIndex=_CpLocalUserIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,1),_CpLocalUserIndex_Type())
cpLocalUserIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpLocalUserIndex.setStatus(_A)
class _CpLocalUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CpLocalUserName_Type.__name__=_I
_CpLocalUserName_Object=MibTableColumn
cpLocalUserName=_CpLocalUserName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,2),_CpLocalUserName_Type())
cpLocalUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserName.setStatus(_A)
class _CpLocalUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_CpLocalUserPassword_Type.__name__=_I
_CpLocalUserPassword_Object=MibTableColumn
cpLocalUserPassword=_CpLocalUserPassword_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,3),_CpLocalUserPassword_Type())
cpLocalUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserPassword.setStatus(_A)
class _CpLocalUserSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_CpLocalUserSessionTimeout_Type.__name__=_F
_CpLocalUserSessionTimeout_Object=MibTableColumn
cpLocalUserSessionTimeout=_CpLocalUserSessionTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,4),_CpLocalUserSessionTimeout_Type())
cpLocalUserSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserSessionTimeout.setStatus(_A)
class _CpLocalUserIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_CpLocalUserIdleTimeout_Type.__name__=_F
_CpLocalUserIdleTimeout_Object=MibTableColumn
cpLocalUserIdleTimeout=_CpLocalUserIdleTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,5),_CpLocalUserIdleTimeout_Type())
cpLocalUserIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserIdleTimeout.setStatus(_A)
class _CpLocalUserMaxBandwidthUp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,536870911))
_CpLocalUserMaxBandwidthUp_Type.__name__=_F
_CpLocalUserMaxBandwidthUp_Object=MibTableColumn
cpLocalUserMaxBandwidthUp=_CpLocalUserMaxBandwidthUp_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,6),_CpLocalUserMaxBandwidthUp_Type())
cpLocalUserMaxBandwidthUp.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserMaxBandwidthUp.setStatus(_A)
class _CpLocalUserMaxBandwidthDown_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,536870911))
_CpLocalUserMaxBandwidthDown_Type.__name__=_F
_CpLocalUserMaxBandwidthDown_Object=MibTableColumn
cpLocalUserMaxBandwidthDown=_CpLocalUserMaxBandwidthDown_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,7),_CpLocalUserMaxBandwidthDown_Type())
cpLocalUserMaxBandwidthDown.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserMaxBandwidthDown.setStatus(_A)
class _CpLocalUserMaxInputOctets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpLocalUserMaxInputOctets_Type.__name__=_F
_CpLocalUserMaxInputOctets_Object=MibTableColumn
cpLocalUserMaxInputOctets=_CpLocalUserMaxInputOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,8),_CpLocalUserMaxInputOctets_Type())
cpLocalUserMaxInputOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserMaxInputOctets.setStatus(_A)
class _CpLocalUserMaxOutputOctets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpLocalUserMaxOutputOctets_Type.__name__=_F
_CpLocalUserMaxOutputOctets_Object=MibTableColumn
cpLocalUserMaxOutputOctets=_CpLocalUserMaxOutputOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,9),_CpLocalUserMaxOutputOctets_Type())
cpLocalUserMaxOutputOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserMaxOutputOctets.setStatus(_A)
class _CpLocalUserMaxTotalOctets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpLocalUserMaxTotalOctets_Type.__name__=_F
_CpLocalUserMaxTotalOctets_Object=MibTableColumn
cpLocalUserMaxTotalOctets=_CpLocalUserMaxTotalOctets_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,10),_CpLocalUserMaxTotalOctets_Type())
cpLocalUserMaxTotalOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpLocalUserMaxTotalOctets.setStatus(_A)
_CpLocalUserRowStatus_Type=RowStatus
_CpLocalUserRowStatus_Object=MibTableColumn
cpLocalUserRowStatus=_CpLocalUserRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,2,1,11),_CpLocalUserRowStatus_Type())
cpLocalUserRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserRowStatus.setStatus(_A)
_CpLocalUserGroupAssociationTable_Object=MibTable
cpLocalUserGroupAssociationTable=_CpLocalUserGroupAssociationTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,3))
if mibBuilder.loadTexts:cpLocalUserGroupAssociationTable.setStatus(_A)
_CpLocalUserGroupAssociationEntry_Object=MibTableRow
cpLocalUserGroupAssociationEntry=_CpLocalUserGroupAssociationEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,3,1))
cpLocalUserGroupAssociationEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:cpLocalUserGroupAssociationEntry.setStatus(_A)
class _CpLocalUserGroupAssociationUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupAssociationUserIndex_Type.__name__=_D
_CpLocalUserGroupAssociationUserIndex_Object=MibTableColumn
cpLocalUserGroupAssociationUserIndex=_CpLocalUserGroupAssociationUserIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,3,1,1),_CpLocalUserGroupAssociationUserIndex_Type())
cpLocalUserGroupAssociationUserIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationUserIndex.setStatus(_A)
class _CpLocalUserGroupAssociationGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupAssociationGroupIndex_Type.__name__=_D
_CpLocalUserGroupAssociationGroupIndex_Object=MibTableColumn
cpLocalUserGroupAssociationGroupIndex=_CpLocalUserGroupAssociationGroupIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,3,1,2),_CpLocalUserGroupAssociationGroupIndex_Type())
cpLocalUserGroupAssociationGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationGroupIndex.setStatus(_A)
_CpLocalUserGroupAssociationRowStatus_Type=RowStatus
_CpLocalUserGroupAssociationRowStatus_Object=MibTableColumn
cpLocalUserGroupAssociationRowStatus=_CpLocalUserGroupAssociationRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,3,3,1,3),_CpLocalUserGroupAssociationRowStatus_Type())
cpLocalUserGroupAssociationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationRowStatus.setStatus(_A)
_CpInterfaceAssociationGroup_ObjectIdentity=ObjectIdentity
cpInterfaceAssociationGroup=_CpInterfaceAssociationGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4))
_CpInterfaceAssociationTable_Object=MibTable
cpInterfaceAssociationTable=_CpInterfaceAssociationTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4,1))
if mibBuilder.loadTexts:cpInterfaceAssociationTable.setStatus(_A)
_CpInterfaceAssociationEntry_Object=MibTableRow
cpInterfaceAssociationEntry=_CpInterfaceAssociationEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4,1,1))
cpInterfaceAssociationEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:cpInterfaceAssociationEntry.setStatus(_A)
_CpIntfAssociationCPID_Type=Unsigned32
_CpIntfAssociationCPID_Object=MibTableColumn
cpIntfAssociationCPID=_CpIntfAssociationCPID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4,1,1,1),_CpIntfAssociationCPID_Type())
cpIntfAssociationCPID.setMaxAccess(_J)
if mibBuilder.loadTexts:cpIntfAssociationCPID.setStatus(_A)
_CpIntfAssociationIfIndex_Type=InterfaceIndex
_CpIntfAssociationIfIndex_Object=MibTableColumn
cpIntfAssociationIfIndex=_CpIntfAssociationIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4,1,1,2),_CpIntfAssociationIfIndex_Type())
cpIntfAssociationIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cpIntfAssociationIfIndex.setStatus(_A)
_CpIntfAssociationRowStatus_Type=RowStatus
_CpIntfAssociationRowStatus_Object=MibTableColumn
cpIntfAssociationRowStatus=_CpIntfAssociationRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,1,4,1,1,3),_CpIntfAssociationRowStatus_Type())
cpIntfAssociationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpIntfAssociationRowStatus.setStatus(_A)
_CpStatusGroup_ObjectIdentity=ObjectIdentity
cpStatusGroup=_CpStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2))
_CpCaptivePortalGlobalStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalGlobalStatusGroup=_CpCaptivePortalGlobalStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1))
class _CpCaptivePortalOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('enablePending',0),('enabled',1),('disablePending',2),('disabled',3)))
_CpCaptivePortalOperStatus_Type.__name__=_D
_CpCaptivePortalOperStatus_Object=MibScalar
cpCaptivePortalOperStatus=_CpCaptivePortalOperStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,1),_CpCaptivePortalOperStatus_Type())
cpCaptivePortalOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalOperStatus.setStatus(_A)
class _CpCaptivePortalOperDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),(_T,1),('noIPAddress',2),('noIPRoutingIntf',3),('routingDisabled',4)))
_CpCaptivePortalOperDisabledReason_Type.__name__=_D
_CpCaptivePortalOperDisabledReason_Object=MibScalar
cpCaptivePortalOperDisabledReason=_CpCaptivePortalOperDisabledReason_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,2),_CpCaptivePortalOperDisabledReason_Type())
cpCaptivePortalOperDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalOperDisabledReason.setStatus(_A)
_CpCaptivePortalIpv4Address_Type=IpAddress
_CpCaptivePortalIpv4Address_Object=MibScalar
cpCaptivePortalIpv4Address=_CpCaptivePortalIpv4Address_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,3),_CpCaptivePortalIpv4Address_Type())
cpCaptivePortalIpv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIpv4Address.setStatus(_A)
class _CpCaptivePortalInstanceMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CpCaptivePortalInstanceMaxCount_Type.__name__=_D
_CpCaptivePortalInstanceMaxCount_Object=MibScalar
cpCaptivePortalInstanceMaxCount=_CpCaptivePortalInstanceMaxCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,4),_CpCaptivePortalInstanceMaxCount_Type())
cpCaptivePortalInstanceMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceMaxCount.setStatus(_A)
_CpCaptivePortalInstanceConfiguredCount_Type=Integer32
_CpCaptivePortalInstanceConfiguredCount_Object=MibScalar
cpCaptivePortalInstanceConfiguredCount=_CpCaptivePortalInstanceConfiguredCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,5),_CpCaptivePortalInstanceConfiguredCount_Type())
cpCaptivePortalInstanceConfiguredCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceConfiguredCount.setStatus(_A)
_CpCaptivePortalInstanceActiveCount_Type=Integer32
_CpCaptivePortalInstanceActiveCount_Object=MibScalar
cpCaptivePortalInstanceActiveCount=_CpCaptivePortalInstanceActiveCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,6),_CpCaptivePortalInstanceActiveCount_Type())
cpCaptivePortalInstanceActiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceActiveCount.setStatus(_A)
class _CpCaptivePortalAuthenUserMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CpCaptivePortalAuthenUserMaxCount_Type.__name__=_D
_CpCaptivePortalAuthenUserMaxCount_Object=MibScalar
cpCaptivePortalAuthenUserMaxCount=_CpCaptivePortalAuthenUserMaxCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,7),_CpCaptivePortalAuthenUserMaxCount_Type())
cpCaptivePortalAuthenUserMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalAuthenUserMaxCount.setStatus(_A)
class _CpCaptivePortalLocalUserMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CpCaptivePortalLocalUserMaxCount_Type.__name__=_D
_CpCaptivePortalLocalUserMaxCount_Object=MibScalar
cpCaptivePortalLocalUserMaxCount=_CpCaptivePortalLocalUserMaxCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,8),_CpCaptivePortalLocalUserMaxCount_Type())
cpCaptivePortalLocalUserMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalLocalUserMaxCount.setStatus(_A)
_CpCaptivePortalConfiguredLocalUserCount_Type=Integer32
_CpCaptivePortalConfiguredLocalUserCount_Object=MibScalar
cpCaptivePortalConfiguredLocalUserCount=_CpCaptivePortalConfiguredLocalUserCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,9),_CpCaptivePortalConfiguredLocalUserCount_Type())
cpCaptivePortalConfiguredLocalUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalConfiguredLocalUserCount.setStatus(_A)
_CpCaptivePortalAuthenUserCurrentCount_Type=Integer32
_CpCaptivePortalAuthenUserCurrentCount_Object=MibScalar
cpCaptivePortalAuthenUserCurrentCount=_CpCaptivePortalAuthenUserCurrentCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,1,10),_CpCaptivePortalAuthenUserCurrentCount_Type())
cpCaptivePortalAuthenUserCurrentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalAuthenUserCurrentCount.setStatus(_A)
_CpCaptivePortalInstanceStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalInstanceStatusGroup=_CpCaptivePortalInstanceStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2))
_CpCaptivePortalInstanceStatusTable_Object=MibTable
cpCaptivePortalInstanceStatusTable=_CpCaptivePortalInstanceStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1))
if mibBuilder.loadTexts:cpCaptivePortalInstanceStatusTable.setStatus(_A)
_CpCaptivePortalInstanceStatusEntry_Object=MibTableRow
cpCaptivePortalInstanceStatusEntry=_CpCaptivePortalInstanceStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1,1))
cpCaptivePortalInstanceStatusEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:cpCaptivePortalInstanceStatusEntry.setStatus(_A)
class _CpCaptivePortalInstanceOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpCaptivePortalInstanceOperStatus_Type.__name__=_D
_CpCaptivePortalInstanceOperStatus_Object=MibTableColumn
cpCaptivePortalInstanceOperStatus=_CpCaptivePortalInstanceOperStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1,1,1),_CpCaptivePortalInstanceOperStatus_Type())
cpCaptivePortalInstanceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceOperStatus.setStatus(_A)
class _CpCaptivePortalInstanceOperDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_N,0),(_T,1),('noRadiusServer',2),('noAccountingServer',3),('noIntfAssociation',4),('noActiveIntf',5),('noValidCert',6)))
_CpCaptivePortalInstanceOperDisabledReason_Type.__name__=_D
_CpCaptivePortalInstanceOperDisabledReason_Object=MibTableColumn
cpCaptivePortalInstanceOperDisabledReason=_CpCaptivePortalInstanceOperDisabledReason_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1,1,2),_CpCaptivePortalInstanceOperDisabledReason_Type())
cpCaptivePortalInstanceOperDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceOperDisabledReason.setStatus(_A)
class _CpCaptivePortalInstanceBlockStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('blockPending',0),(_c,1),('notBlockPending',2),(_d,3)))
_CpCaptivePortalInstanceBlockStatus_Type.__name__=_D
_CpCaptivePortalInstanceBlockStatus_Object=MibTableColumn
cpCaptivePortalInstanceBlockStatus=_CpCaptivePortalInstanceBlockStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1,1,3),_CpCaptivePortalInstanceBlockStatus_Type())
cpCaptivePortalInstanceBlockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalInstanceBlockStatus.setStatus(_A)
_CpCaptivePortalInstanceAuthUserCount_Type=Integer32
_CpCaptivePortalInstanceAuthUserCount_Object=MibTableColumn
cpCaptivePortalInstanceAuthUserCount=_CpCaptivePortalInstanceAuthUserCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,2,1,1,4),_CpCaptivePortalInstanceAuthUserCount_Type())
cpCaptivePortalInstanceAuthUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceAuthUserCount.setStatus(_A)
_CpCaptivePortalIntfStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfStatusGroup=_CpCaptivePortalIntfStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3))
_CpCaptivePortalIntfStatusTable_Object=MibTable
cpCaptivePortalIntfStatusTable=_CpCaptivePortalIntfStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfStatusTable.setStatus(_A)
_CpCaptivePortalIntfStatusEntry_Object=MibTableRow
cpCaptivePortalIntfStatusEntry=_CpCaptivePortalIntfStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1))
cpCaptivePortalIntfStatusEntry.setIndexNames((0,_E,_M),(0,_E,_U))
if mibBuilder.loadTexts:cpCaptivePortalIntfStatusEntry.setStatus(_A)
_CpCaptivePortalIntfIfIndex_Type=InterfaceIndex
_CpCaptivePortalIntfIfIndex_Object=MibTableColumn
cpCaptivePortalIntfIfIndex=_CpCaptivePortalIntfIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1,1),_CpCaptivePortalIntfIfIndex_Type())
cpCaptivePortalIntfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfIfIndex.setStatus(_A)
class _CpCaptivePortalIntfActivationStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpCaptivePortalIntfActivationStatus_Type.__name__=_D
_CpCaptivePortalIntfActivationStatus_Object=MibTableColumn
cpCaptivePortalIntfActivationStatus=_CpCaptivePortalIntfActivationStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1,2),_CpCaptivePortalIntfActivationStatus_Type())
cpCaptivePortalIntfActivationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfActivationStatus.setStatus(_A)
class _CpCaptivePortalIntfActivationDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('intfNotAttached',1),(_T,2)))
_CpCaptivePortalIntfActivationDisabledReason_Type.__name__=_D
_CpCaptivePortalIntfActivationDisabledReason_Object=MibTableColumn
cpCaptivePortalIntfActivationDisabledReason=_CpCaptivePortalIntfActivationDisabledReason_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1,3),_CpCaptivePortalIntfActivationDisabledReason_Type())
cpCaptivePortalIntfActivationDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfActivationDisabledReason.setStatus(_A)
class _CpCaptivePortalIntfBlockStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_CpCaptivePortalIntfBlockStatus_Type.__name__=_D
_CpCaptivePortalIntfBlockStatus_Object=MibTableColumn
cpCaptivePortalIntfBlockStatus=_CpCaptivePortalIntfBlockStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1,4),_CpCaptivePortalIntfBlockStatus_Type())
cpCaptivePortalIntfBlockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfBlockStatus.setStatus(_A)
_CpCaptivePortalIntfAuthUserCount_Type=Integer32
_CpCaptivePortalIntfAuthUserCount_Object=MibTableColumn
cpCaptivePortalIntfAuthUserCount=_CpCaptivePortalIntfAuthUserCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,3,1,1,5),_CpCaptivePortalIntfAuthUserCount_Type())
cpCaptivePortalIntfAuthUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfAuthUserCount.setStatus(_A)
_CpCaptivePortalIntfDatabaseGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfDatabaseGroup=_CpCaptivePortalIntfDatabaseGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,4))
_CpCaptivePortalIntfDatabaseTable_Object=MibTable
cpCaptivePortalIntfDatabaseTable=_CpCaptivePortalIntfDatabaseTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,4,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfDatabaseTable.setStatus(_A)
_CpCaptivePortalIntfDatabaseEntry_Object=MibTableRow
cpCaptivePortalIntfDatabaseEntry=_CpCaptivePortalIntfDatabaseEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,4,1,1))
cpCaptivePortalIntfDatabaseEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:cpCaptivePortalIntfDatabaseEntry.setStatus(_A)
_CpCaptivePortalIntfCapabilities_Type=CpCaptivePortalIntfCapabilitiesMap
_CpCaptivePortalIntfCapabilities_Object=MibTableColumn
cpCaptivePortalIntfCapabilities=_CpCaptivePortalIntfCapabilities_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,4,1,1,1),_CpCaptivePortalIntfCapabilities_Type())
cpCaptivePortalIntfCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfCapabilities.setStatus(_A)
_CpCaptivePortalClientStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalClientStatusGroup=_CpCaptivePortalClientStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5))
_CpCaptivePortalClientStatusTable_Object=MibTable
cpCaptivePortalClientStatusTable=_CpCaptivePortalClientStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1))
if mibBuilder.loadTexts:cpCaptivePortalClientStatusTable.setStatus(_A)
_CpCaptivePortalClientStatusEntry_Object=MibTableRow
cpCaptivePortalClientStatusEntry=_CpCaptivePortalClientStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1))
cpCaptivePortalClientStatusEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:cpCaptivePortalClientStatusEntry.setStatus(_A)
_CpCaptivePortalClientMacAddress_Type=MacAddress
_CpCaptivePortalClientMacAddress_Object=MibTableColumn
cpCaptivePortalClientMacAddress=_CpCaptivePortalClientMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,1),_CpCaptivePortalClientMacAddress_Type())
cpCaptivePortalClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientMacAddress.setStatus(_A)
_CpCaptivePortalClientIpAddress_Type=IpAddress
_CpCaptivePortalClientIpAddress_Object=MibTableColumn
cpCaptivePortalClientIpAddress=_CpCaptivePortalClientIpAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,2),_CpCaptivePortalClientIpAddress_Type())
cpCaptivePortalClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientIpAddress.setStatus(_A)
class _CpCaptivePortalClientUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpCaptivePortalClientUserName_Type.__name__=_I
_CpCaptivePortalClientUserName_Object=MibTableColumn
cpCaptivePortalClientUserName=_CpCaptivePortalClientUserName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,3),_CpCaptivePortalClientUserName_Type())
cpCaptivePortalClientUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientUserName.setStatus(_A)
class _CpCaptivePortalClientProtocolMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('https',0),('http',1)))
_CpCaptivePortalClientProtocolMode_Type.__name__=_D
_CpCaptivePortalClientProtocolMode_Object=MibTableColumn
cpCaptivePortalClientProtocolMode=_CpCaptivePortalClientProtocolMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,4),_CpCaptivePortalClientProtocolMode_Type())
cpCaptivePortalClientProtocolMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientProtocolMode.setStatus(_A)
class _CpCaptivePortalClientVerificationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('guest',0),(_S,1),(_V,2)))
_CpCaptivePortalClientVerificationMode_Type.__name__=_D
_CpCaptivePortalClientVerificationMode_Object=MibTableColumn
cpCaptivePortalClientVerificationMode=_CpCaptivePortalClientVerificationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,5),_CpCaptivePortalClientVerificationMode_Type())
cpCaptivePortalClientVerificationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientVerificationMode.setStatus(_A)
_CpCaptivePortalClientAssocIfIndex_Type=InterfaceIndex
_CpCaptivePortalClientAssocIfIndex_Object=MibTableColumn
cpCaptivePortalClientAssocIfIndex=_CpCaptivePortalClientAssocIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,6),_CpCaptivePortalClientAssocIfIndex_Type())
cpCaptivePortalClientAssocIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientAssocIfIndex.setStatus(_A)
_CpCaptivePortalClientCPID_Type=Integer32
_CpCaptivePortalClientCPID_Object=MibTableColumn
cpCaptivePortalClientCPID=_CpCaptivePortalClientCPID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,7),_CpCaptivePortalClientCPID_Type())
cpCaptivePortalClientCPID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientCPID.setStatus(_A)
_CpCaptivePortalClientSessionTime_Type=TimeTicks
_CpCaptivePortalClientSessionTime_Object=MibTableColumn
cpCaptivePortalClientSessionTime=_CpCaptivePortalClientSessionTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,8),_CpCaptivePortalClientSessionTime_Type())
cpCaptivePortalClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientSessionTime.setStatus(_A)
_CpCaptivePortalClientSwitchMacAddress_Type=MacAddress
_CpCaptivePortalClientSwitchMacAddress_Object=MibTableColumn
cpCaptivePortalClientSwitchMacAddress=_CpCaptivePortalClientSwitchMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,9),_CpCaptivePortalClientSwitchMacAddress_Type())
cpCaptivePortalClientSwitchMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientSwitchMacAddress.setStatus(_A)
_CpCaptivePortalClientSwitchIpAddress_Type=IpAddress
_CpCaptivePortalClientSwitchIpAddress_Object=MibTableColumn
cpCaptivePortalClientSwitchIpAddress=_CpCaptivePortalClientSwitchIpAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,10),_CpCaptivePortalClientSwitchIpAddress_Type())
cpCaptivePortalClientSwitchIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientSwitchIpAddress.setStatus(_A)
class _CpCaptivePortalClientSwitchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('peer',1),(_S,2)))
_CpCaptivePortalClientSwitchType_Type.__name__=_D
_CpCaptivePortalClientSwitchType_Object=MibTableColumn
cpCaptivePortalClientSwitchType=_CpCaptivePortalClientSwitchType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,11),_CpCaptivePortalClientSwitchType_Type())
cpCaptivePortalClientSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientSwitchType.setStatus(_A)
class _CpCaptivePortalClientDeauthAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('start',2)))
_CpCaptivePortalClientDeauthAction_Type.__name__=_D
_CpCaptivePortalClientDeauthAction_Object=MibTableColumn
cpCaptivePortalClientDeauthAction=_CpCaptivePortalClientDeauthAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,1,1,12),_CpCaptivePortalClientDeauthAction_Type())
cpCaptivePortalClientDeauthAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cpCaptivePortalClientDeauthAction.setStatus(_A)
_CpCaptivePortalClientStatisticsTable_Object=MibTable
cpCaptivePortalClientStatisticsTable=_CpCaptivePortalClientStatisticsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2))
if mibBuilder.loadTexts:cpCaptivePortalClientStatisticsTable.setStatus(_A)
_CpCaptivePortalClientStatisticsEntry_Object=MibTableRow
cpCaptivePortalClientStatisticsEntry=_CpCaptivePortalClientStatisticsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2,1))
if mibBuilder.loadTexts:cpCaptivePortalClientStatisticsEntry.setStatus(_A)
_CpCaptivePortalClientBytesReceived_Type=Counter64
_CpCaptivePortalClientBytesReceived_Object=MibTableColumn
cpCaptivePortalClientBytesReceived=_CpCaptivePortalClientBytesReceived_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2,1,1),_CpCaptivePortalClientBytesReceived_Type())
cpCaptivePortalClientBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientBytesReceived.setStatus(_A)
_CpCaptivePortalClientBytesTransmitted_Type=Counter64
_CpCaptivePortalClientBytesTransmitted_Object=MibTableColumn
cpCaptivePortalClientBytesTransmitted=_CpCaptivePortalClientBytesTransmitted_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2,1,2),_CpCaptivePortalClientBytesTransmitted_Type())
cpCaptivePortalClientBytesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientBytesTransmitted.setStatus(_A)
_CpCaptivePortalClientPacketsReceived_Type=Counter64
_CpCaptivePortalClientPacketsReceived_Object=MibTableColumn
cpCaptivePortalClientPacketsReceived=_CpCaptivePortalClientPacketsReceived_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2,1,3),_CpCaptivePortalClientPacketsReceived_Type())
cpCaptivePortalClientPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientPacketsReceived.setStatus(_A)
_CpCaptivePortalClientPacketsTransmitted_Type=Counter64
_CpCaptivePortalClientPacketsTransmitted_Object=MibTableColumn
cpCaptivePortalClientPacketsTransmitted=_CpCaptivePortalClientPacketsTransmitted_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,5,2,1,4),_CpCaptivePortalClientPacketsTransmitted_Type())
cpCaptivePortalClientPacketsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientPacketsTransmitted.setStatus(_A)
_CpCaptivePortalIntfClientAssocGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfClientAssocGroup=_CpCaptivePortalIntfClientAssocGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6))
_CpCaptivePortalIntfClientAssocTable_Object=MibTable
cpCaptivePortalIntfClientAssocTable=_CpCaptivePortalIntfClientAssocTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocTable.setStatus(_A)
_CpCaptivePortalIntfClientAssocEntry_Object=MibTableRow
cpCaptivePortalIntfClientAssocEntry=_CpCaptivePortalIntfClientAssocEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6,1,1))
cpCaptivePortalIntfClientAssocEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocEntry.setStatus(_A)
_CpCaptivePortalIntfClientIfIndex_Type=InterfaceIndex
_CpCaptivePortalIntfClientIfIndex_Object=MibTableColumn
cpCaptivePortalIntfClientIfIndex=_CpCaptivePortalIntfClientIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6,1,1,1),_CpCaptivePortalIntfClientIfIndex_Type())
cpCaptivePortalIntfClientIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientIfIndex.setStatus(_A)
_CpCaptivePortalIntfClientAssocMacAddress_Type=MacAddress
_CpCaptivePortalIntfClientAssocMacAddress_Object=MibTableColumn
cpCaptivePortalIntfClientAssocMacAddress=_CpCaptivePortalIntfClientAssocMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6,1,1,2),_CpCaptivePortalIntfClientAssocMacAddress_Type())
cpCaptivePortalIntfClientAssocMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocMacAddress.setStatus(_A)
_CpCaptivePortalIntfClientAssocRowStatus_Type=RowStatus
_CpCaptivePortalIntfClientAssocRowStatus_Object=MibTableColumn
cpCaptivePortalIntfClientAssocRowStatus=_CpCaptivePortalIntfClientAssocRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,6,1,1,3),_CpCaptivePortalIntfClientAssocRowStatus_Type())
cpCaptivePortalIntfClientAssocRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocRowStatus.setStatus(_A)
_CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalInstanceClientAssocGroup=_CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7))
_CpCaptivePortalInstanceClientAssocTable_Object=MibTable
cpCaptivePortalInstanceClientAssocTable=_CpCaptivePortalInstanceClientAssocTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7,1))
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocTable.setStatus(_A)
_CpCaptivePortalInstanceClientAssocEntry_Object=MibTableRow
cpCaptivePortalInstanceClientAssocEntry=_CpCaptivePortalInstanceClientAssocEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7,1,1))
cpCaptivePortalInstanceClientAssocEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocEntry.setStatus(_A)
class _CpCaptivePortalInstanceClientAssocInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CpCaptivePortalInstanceClientAssocInstanceId_Type.__name__=_D
_CpCaptivePortalInstanceClientAssocInstanceId_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocInstanceId=_CpCaptivePortalInstanceClientAssocInstanceId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7,1,1,1),_CpCaptivePortalInstanceClientAssocInstanceId_Type())
cpCaptivePortalInstanceClientAssocInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocInstanceId.setStatus(_A)
_CpCaptivePortalInstanceClientAssocMacAddress_Type=MacAddress
_CpCaptivePortalInstanceClientAssocMacAddress_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocMacAddress=_CpCaptivePortalInstanceClientAssocMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7,1,1,2),_CpCaptivePortalInstanceClientAssocMacAddress_Type())
cpCaptivePortalInstanceClientAssocMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocMacAddress.setStatus(_A)
_CpCaptivePortalInstanceClientAssocRowStatus_Type=RowStatus
_CpCaptivePortalInstanceClientAssocRowStatus_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocRowStatus=_CpCaptivePortalInstanceClientAssocRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,2,7,1,1,3),_CpCaptivePortalInstanceClientAssocRowStatus_Type())
cpCaptivePortalInstanceClientAssocRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocRowStatus.setStatus(_A)
_CpTrapsConfig_ObjectIdentity=ObjectIdentity
cpTrapsConfig=_CpTrapsConfig_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3))
class _CpTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpTrapMode_Type.__name__=_D
_CpTrapMode_Object=MibScalar
cpTrapMode=_CpTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3,1),_CpTrapMode_Type())
cpTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpTrapMode.setStatus(_A)
class _CpClientAuthenticationFailureTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpClientAuthenticationFailureTrapMode_Type.__name__=_D
_CpClientAuthenticationFailureTrapMode_Object=MibScalar
cpClientAuthenticationFailureTrapMode=_CpClientAuthenticationFailureTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3,2),_CpClientAuthenticationFailureTrapMode_Type())
cpClientAuthenticationFailureTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpClientAuthenticationFailureTrapMode.setStatus(_A)
class _CpClientConnectTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpClientConnectTrapMode_Type.__name__=_D
_CpClientConnectTrapMode_Object=MibScalar
cpClientConnectTrapMode=_CpClientConnectTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3,3),_CpClientConnectTrapMode_Type())
cpClientConnectTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpClientConnectTrapMode.setStatus(_A)
class _CpClientDatabaseFullTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpClientDatabaseFullTrapMode_Type.__name__=_D
_CpClientDatabaseFullTrapMode_Object=MibScalar
cpClientDatabaseFullTrapMode=_CpClientDatabaseFullTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3,4),_CpClientDatabaseFullTrapMode_Type())
cpClientDatabaseFullTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpClientDatabaseFullTrapMode.setStatus(_A)
class _CpClientDisconnectTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CpClientDisconnectTrapMode_Type.__name__=_D
_CpClientDisconnectTrapMode_Object=MibScalar
cpClientDisconnectTrapMode=_CpClientDisconnectTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,3,5),_CpClientDisconnectTrapMode_Type())
cpClientDisconnectTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpClientDisconnectTrapMode.setStatus(_A)
_CpTraps_ObjectIdentity=ObjectIdentity
cpTraps=_CpTraps_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,4))
_CpCaptivePortalConfigWebGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalConfigWebGroup=_CpCaptivePortalConfigWebGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,5))
_CpCaptivePortalConfigWebTable_Object=MibTable
cpCaptivePortalConfigWebTable=_CpCaptivePortalConfigWebTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,5,1))
if mibBuilder.loadTexts:cpCaptivePortalConfigWebTable.setStatus(_A)
_CpCaptivePortalConfigWebEntry_Object=MibTableRow
cpCaptivePortalConfigWebEntry=_CpCaptivePortalConfigWebEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,5,1,1))
cpCaptivePortalConfigWebEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:cpCaptivePortalConfigWebEntry.setStatus(_A)
_CpCaptivePortalConfigWebInstanceId_Type=Unsigned32
_CpCaptivePortalConfigWebInstanceId_Object=MibTableColumn
cpCaptivePortalConfigWebInstanceId=_CpCaptivePortalConfigWebInstanceId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,5,1,1,1),_CpCaptivePortalConfigWebInstanceId_Type())
cpCaptivePortalConfigWebInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalConfigWebInstanceId.setStatus(_A)
_CpCaptivePortalConfigWebWebId_Type=Unsigned32
_CpCaptivePortalConfigWebWebId_Object=MibTableColumn
cpCaptivePortalConfigWebWebId=_CpCaptivePortalConfigWebWebId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,5,1,1,2),_CpCaptivePortalConfigWebWebId_Type())
cpCaptivePortalConfigWebWebId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalConfigWebWebId.setStatus(_A)
cpCaptivePortalClientStatusEntry.registerAugmentions((_E,_k))
cpCaptivePortalClientStatisticsEntry.setIndexNames(*cpCaptivePortalClientStatusEntry.getIndexNames())
cpClientAuthenticationFailure=NotificationType((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,4,1))
cpClientAuthenticationFailure.setObjects(*((_E,_L),(_E,_O),(_E,_P),(_E,_Q),(_E,_R),(_E,_l)))
if mibBuilder.loadTexts:cpClientAuthenticationFailure.setStatus(_A)
cpClientConnect=NotificationType((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,4,2))
cpClientConnect.setObjects(*((_E,_L),(_E,_Q),(_E,_O),(_E,_P),(_E,_R)))
if mibBuilder.loadTexts:cpClientConnect.setStatus(_A)
cpClientDatabaseFull=NotificationType((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,4,3))
if mibBuilder.loadTexts:cpClientDatabaseFull.setStatus(_A)
cpClientDisconnect=NotificationType((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,38,4,4))
cpClientDisconnect.setObjects(*((_E,_L),(_E,_Q),(_E,_O),(_E,_P),(_E,_R)))
if mibBuilder.loadTexts:cpClientDisconnect.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'CpCaptivePortalIntfCapabilitiesMap':CpCaptivePortalIntfCapabilitiesMap,'fastPathCaptivePortal':fastPathCaptivePortal,'cpConfigGroup':cpConfigGroup,'cpGlobalConfigGroup':cpGlobalConfigGroup,'cpAdminMode':cpAdminMode,'cpAdditionalHttpPort':cpAdditionalHttpPort,'cpAdditionalHttpSecurePort':cpAdditionalHttpSecurePort,'cpPeerStatsReportingInterval':cpPeerStatsReportingInterval,'cpAuthTimeout':cpAuthTimeout,'cpCaptivePortalConfigGroup':cpCaptivePortalConfigGroup,'cpCaptivePortalTable':cpCaptivePortalTable,'cpCaptivePortalEntry':cpCaptivePortalEntry,_M:cpCaptivePortalInstanceId,'cpCaptivePortalConfigName':cpCaptivePortalConfigName,'cpCaptivePortalAdminMode':cpCaptivePortalAdminMode,'cpCaptivePortalProtocolMode':cpCaptivePortalProtocolMode,'cpCaptivePortalVerificationMode':cpCaptivePortalVerificationMode,'cpCaptivePortalUserGroup':cpCaptivePortalUserGroup,'cpCaptivePortalURLRedirectMode':cpCaptivePortalURLRedirectMode,'cpCaptivePortalRedirectURL':cpCaptivePortalRedirectURL,'cpCaptivePortalSessionTimeout':cpCaptivePortalSessionTimeout,'cpCaptivePortalIdleTimeout':cpCaptivePortalIdleTimeout,'cpCaptivePortalRadiusAuthServer':cpCaptivePortalRadiusAuthServer,'cpCaptivePortalMaxBandwidthUp':cpCaptivePortalMaxBandwidthUp,'cpCaptivePortalMaxBandwidthDown':cpCaptivePortalMaxBandwidthDown,'cpCaptivePortalMaxInputOctets':cpCaptivePortalMaxInputOctets,'cpCaptivePortalMaxOutputOctets':cpCaptivePortalMaxOutputOctets,'cpCaptivePortalMaxTotalOctets':cpCaptivePortalMaxTotalOctets,'cpCaptivePortalUserLogoutMode':cpCaptivePortalUserLogoutMode,'cpCaptivePortalRowStatus':cpCaptivePortalRowStatus,'cpLocalUserDatabaseGroup':cpLocalUserDatabaseGroup,'cpLocalUserGroupTable':cpLocalUserGroupTable,'cpLocalUserGroupEntry':cpLocalUserGroupEntry,_W:cpLocalUserGroupIndex,'cpLocalUserGroupName':cpLocalUserGroupName,'cpLocalUserGroupRowStatus':cpLocalUserGroupRowStatus,'cpLocalUserTable':cpLocalUserTable,'cpLocalUserEntry':cpLocalUserEntry,_X:cpLocalUserIndex,'cpLocalUserName':cpLocalUserName,'cpLocalUserPassword':cpLocalUserPassword,'cpLocalUserSessionTimeout':cpLocalUserSessionTimeout,'cpLocalUserIdleTimeout':cpLocalUserIdleTimeout,'cpLocalUserMaxBandwidthUp':cpLocalUserMaxBandwidthUp,'cpLocalUserMaxBandwidthDown':cpLocalUserMaxBandwidthDown,'cpLocalUserMaxInputOctets':cpLocalUserMaxInputOctets,'cpLocalUserMaxOutputOctets':cpLocalUserMaxOutputOctets,'cpLocalUserMaxTotalOctets':cpLocalUserMaxTotalOctets,'cpLocalUserRowStatus':cpLocalUserRowStatus,'cpLocalUserGroupAssociationTable':cpLocalUserGroupAssociationTable,'cpLocalUserGroupAssociationEntry':cpLocalUserGroupAssociationEntry,_Y:cpLocalUserGroupAssociationUserIndex,_Z:cpLocalUserGroupAssociationGroupIndex,'cpLocalUserGroupAssociationRowStatus':cpLocalUserGroupAssociationRowStatus,'cpInterfaceAssociationGroup':cpInterfaceAssociationGroup,'cpInterfaceAssociationTable':cpInterfaceAssociationTable,'cpInterfaceAssociationEntry':cpInterfaceAssociationEntry,_a:cpIntfAssociationCPID,_b:cpIntfAssociationIfIndex,'cpIntfAssociationRowStatus':cpIntfAssociationRowStatus,'cpStatusGroup':cpStatusGroup,'cpCaptivePortalGlobalStatusGroup':cpCaptivePortalGlobalStatusGroup,'cpCaptivePortalOperStatus':cpCaptivePortalOperStatus,'cpCaptivePortalOperDisabledReason':cpCaptivePortalOperDisabledReason,'cpCaptivePortalIpv4Address':cpCaptivePortalIpv4Address,'cpCaptivePortalInstanceMaxCount':cpCaptivePortalInstanceMaxCount,'cpCaptivePortalInstanceConfiguredCount':cpCaptivePortalInstanceConfiguredCount,'cpCaptivePortalInstanceActiveCount':cpCaptivePortalInstanceActiveCount,'cpCaptivePortalAuthenUserMaxCount':cpCaptivePortalAuthenUserMaxCount,'cpCaptivePortalLocalUserMaxCount':cpCaptivePortalLocalUserMaxCount,'cpCaptivePortalConfiguredLocalUserCount':cpCaptivePortalConfiguredLocalUserCount,'cpCaptivePortalAuthenUserCurrentCount':cpCaptivePortalAuthenUserCurrentCount,'cpCaptivePortalInstanceStatusGroup':cpCaptivePortalInstanceStatusGroup,'cpCaptivePortalInstanceStatusTable':cpCaptivePortalInstanceStatusTable,'cpCaptivePortalInstanceStatusEntry':cpCaptivePortalInstanceStatusEntry,'cpCaptivePortalInstanceOperStatus':cpCaptivePortalInstanceOperStatus,'cpCaptivePortalInstanceOperDisabledReason':cpCaptivePortalInstanceOperDisabledReason,'cpCaptivePortalInstanceBlockStatus':cpCaptivePortalInstanceBlockStatus,'cpCaptivePortalInstanceAuthUserCount':cpCaptivePortalInstanceAuthUserCount,'cpCaptivePortalIntfStatusGroup':cpCaptivePortalIntfStatusGroup,'cpCaptivePortalIntfStatusTable':cpCaptivePortalIntfStatusTable,'cpCaptivePortalIntfStatusEntry':cpCaptivePortalIntfStatusEntry,_U:cpCaptivePortalIntfIfIndex,'cpCaptivePortalIntfActivationStatus':cpCaptivePortalIntfActivationStatus,'cpCaptivePortalIntfActivationDisabledReason':cpCaptivePortalIntfActivationDisabledReason,'cpCaptivePortalIntfBlockStatus':cpCaptivePortalIntfBlockStatus,'cpCaptivePortalIntfAuthUserCount':cpCaptivePortalIntfAuthUserCount,'cpCaptivePortalIntfDatabaseGroup':cpCaptivePortalIntfDatabaseGroup,'cpCaptivePortalIntfDatabaseTable':cpCaptivePortalIntfDatabaseTable,'cpCaptivePortalIntfDatabaseEntry':cpCaptivePortalIntfDatabaseEntry,'cpCaptivePortalIntfCapabilities':cpCaptivePortalIntfCapabilities,'cpCaptivePortalClientStatusGroup':cpCaptivePortalClientStatusGroup,'cpCaptivePortalClientStatusTable':cpCaptivePortalClientStatusTable,'cpCaptivePortalClientStatusEntry':cpCaptivePortalClientStatusEntry,_L:cpCaptivePortalClientMacAddress,_O:cpCaptivePortalClientIpAddress,_l:cpCaptivePortalClientUserName,'cpCaptivePortalClientProtocolMode':cpCaptivePortalClientProtocolMode,'cpCaptivePortalClientVerificationMode':cpCaptivePortalClientVerificationMode,_Q:cpCaptivePortalClientAssocIfIndex,_P:cpCaptivePortalClientCPID,'cpCaptivePortalClientSessionTime':cpCaptivePortalClientSessionTime,_R:cpCaptivePortalClientSwitchMacAddress,'cpCaptivePortalClientSwitchIpAddress':cpCaptivePortalClientSwitchIpAddress,'cpCaptivePortalClientSwitchType':cpCaptivePortalClientSwitchType,'cpCaptivePortalClientDeauthAction':cpCaptivePortalClientDeauthAction,'cpCaptivePortalClientStatisticsTable':cpCaptivePortalClientStatisticsTable,_k:cpCaptivePortalClientStatisticsEntry,'cpCaptivePortalClientBytesReceived':cpCaptivePortalClientBytesReceived,'cpCaptivePortalClientBytesTransmitted':cpCaptivePortalClientBytesTransmitted,'cpCaptivePortalClientPacketsReceived':cpCaptivePortalClientPacketsReceived,'cpCaptivePortalClientPacketsTransmitted':cpCaptivePortalClientPacketsTransmitted,'cpCaptivePortalIntfClientAssocGroup':cpCaptivePortalIntfClientAssocGroup,'cpCaptivePortalIntfClientAssocTable':cpCaptivePortalIntfClientAssocTable,'cpCaptivePortalIntfClientAssocEntry':cpCaptivePortalIntfClientAssocEntry,_e:cpCaptivePortalIntfClientIfIndex,_f:cpCaptivePortalIntfClientAssocMacAddress,'cpCaptivePortalIntfClientAssocRowStatus':cpCaptivePortalIntfClientAssocRowStatus,'cpCaptivePortalInstanceClientAssocGroup':cpCaptivePortalInstanceClientAssocGroup,'cpCaptivePortalInstanceClientAssocTable':cpCaptivePortalInstanceClientAssocTable,'cpCaptivePortalInstanceClientAssocEntry':cpCaptivePortalInstanceClientAssocEntry,_g:cpCaptivePortalInstanceClientAssocInstanceId,_h:cpCaptivePortalInstanceClientAssocMacAddress,'cpCaptivePortalInstanceClientAssocRowStatus':cpCaptivePortalInstanceClientAssocRowStatus,'cpTrapsConfig':cpTrapsConfig,'cpTrapMode':cpTrapMode,'cpClientAuthenticationFailureTrapMode':cpClientAuthenticationFailureTrapMode,'cpClientConnectTrapMode':cpClientConnectTrapMode,'cpClientDatabaseFullTrapMode':cpClientDatabaseFullTrapMode,'cpClientDisconnectTrapMode':cpClientDisconnectTrapMode,'cpTraps':cpTraps,'cpClientAuthenticationFailure':cpClientAuthenticationFailure,'cpClientConnect':cpClientConnect,'cpClientDatabaseFull':cpClientDatabaseFull,'cpClientDisconnect':cpClientDisconnect,'cpCaptivePortalConfigWebGroup':cpCaptivePortalConfigWebGroup,'cpCaptivePortalConfigWebTable':cpCaptivePortalConfigWebTable,'cpCaptivePortalConfigWebEntry':cpCaptivePortalConfigWebEntry,_i:cpCaptivePortalConfigWebInstanceId,_j:cpCaptivePortalConfigWebWebId})