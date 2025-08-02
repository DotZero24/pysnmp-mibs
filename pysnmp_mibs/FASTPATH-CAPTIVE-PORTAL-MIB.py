_h='cpCaptivePortalClientAuthFailureConnectionAttempts'
_g='cpCaptivePortalClientUserName'
_f='cpCaptivePortalClientAssocIfIndex'
_e='cpCaptivePortalClientCPID'
_d='cpCaptivePortalClientIpAddress'
_c='cpCaptivePortalInstanceClientAssocMacAddress'
_b='cpCaptivePortalIntfClientAssocMacAddress'
_a='notBlocked'
_Z='blocked'
_Y='cpIntfAssociationIfIndex'
_X='cpIntfAssociationCPID'
_W='cpLocalUserGroupAssociationGroupIndex'
_V='cpLocalUserGroupAssociationUserIndex'
_U='cpLocalUserIndex'
_T='cpLocalUserGroupIndex'
_S='radius'
_R='cpCaptivePortalIntfIfIndex'
_Q='adminDisabled'
_P='cpCaptivePortalInstanceClientAssocInstanceId'
_O='cpCaptivePortalIntfClientIfIndex'
_N='none'
_M='cpCaptivePortalInstanceId'
_L='Unsigned32'
_K='read-create'
_J='cpCaptivePortalClientMacAddress'
_I='not-accessible'
_H='DisplayString'
_G='disable'
_F='enable'
_E='read-write'
_D='FASTPATH-CAPTIVE-PORTAL-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathCaptivePortal=ModuleIdentity((1,3,6,1,4,1,4413,1,1,38))
if mibBuilder.loadTexts:fastPathCaptivePortal.setRevisions(('2007-07-09 00:00',))
class CpCaptivePortalIntfCapabilitiesMap(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('other',0),('sessionTimeout',1)))
_CpConfigGroup_ObjectIdentity=ObjectIdentity
cpConfigGroup=_CpConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,1))
_CpGlobalConfigGroup_ObjectIdentity=ObjectIdentity
cpGlobalConfigGroup=_CpGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,1,1))
class _CpAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpAdminMode_Type.__name__=_C
_CpAdminMode_Object=MibScalar
cpAdminMode=_CpAdminMode_Object((1,3,6,1,4,1,4413,1,1,38,1,1,1),_CpAdminMode_Type())
cpAdminMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpAdminMode.setStatus(_A)
class _CpAdditionalHttpPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpAdditionalHttpPort_Type.__name__=_C
_CpAdditionalHttpPort_Object=MibScalar
cpAdditionalHttpPort=_CpAdditionalHttpPort_Object((1,3,6,1,4,1,4413,1,1,38,1,1,2),_CpAdditionalHttpPort_Type())
cpAdditionalHttpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cpAdditionalHttpPort.setStatus(_A)
class _CpAdditionalHttpSecurePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpAdditionalHttpSecurePort_Type.__name__=_C
_CpAdditionalHttpSecurePort_Object=MibScalar
cpAdditionalHttpSecurePort=_CpAdditionalHttpSecurePort_Object((1,3,6,1,4,1,4413,1,1,38,1,1,3),_CpAdditionalHttpSecurePort_Type())
cpAdditionalHttpSecurePort.setMaxAccess(_E)
if mibBuilder.loadTexts:cpAdditionalHttpSecurePort.setStatus(_A)
class _CpAuthTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_CpAuthTimeout_Type.__name__=_C
_CpAuthTimeout_Object=MibScalar
cpAuthTimeout=_CpAuthTimeout_Object((1,3,6,1,4,1,4413,1,1,38,1,1,5),_CpAuthTimeout_Type())
cpAuthTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cpAuthTimeout.setStatus(_A)
_CpCaptivePortalConfigGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalConfigGroup=_CpCaptivePortalConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,1,2))
_CpCaptivePortalTable_Object=MibTable
cpCaptivePortalTable=_CpCaptivePortalTable_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1))
if mibBuilder.loadTexts:cpCaptivePortalTable.setStatus(_A)
_CpCaptivePortalEntry_Object=MibTableRow
cpCaptivePortalEntry=_CpCaptivePortalEntry_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1))
cpCaptivePortalEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:cpCaptivePortalEntry.setStatus(_A)
_CpCaptivePortalInstanceId_Type=Unsigned32
_CpCaptivePortalInstanceId_Object=MibTableColumn
cpCaptivePortalInstanceId=_CpCaptivePortalInstanceId_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,1),_CpCaptivePortalInstanceId_Type())
cpCaptivePortalInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceId.setStatus(_A)
class _CpCaptivePortalConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpCaptivePortalConfigName_Type.__name__=_H
_CpCaptivePortalConfigName_Object=MibTableColumn
cpCaptivePortalConfigName=_CpCaptivePortalConfigName_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,2),_CpCaptivePortalConfigName_Type())
cpCaptivePortalConfigName.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalConfigName.setStatus(_A)
class _CpCaptivePortalAdminMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpCaptivePortalAdminMode_Type.__name__=_C
_CpCaptivePortalAdminMode_Object=MibTableColumn
cpCaptivePortalAdminMode=_CpCaptivePortalAdminMode_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,3),_CpCaptivePortalAdminMode_Type())
cpCaptivePortalAdminMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalAdminMode.setStatus(_A)
class _CpCaptivePortalProtocolMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('https',0),('http',1)))
_CpCaptivePortalProtocolMode_Type.__name__=_C
_CpCaptivePortalProtocolMode_Object=MibTableColumn
cpCaptivePortalProtocolMode=_CpCaptivePortalProtocolMode_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,4),_CpCaptivePortalProtocolMode_Type())
cpCaptivePortalProtocolMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalProtocolMode.setStatus(_A)
class _CpCaptivePortalVerificationMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('guest',0),('local',1),(_S,2)))
_CpCaptivePortalVerificationMode_Type.__name__=_C
_CpCaptivePortalVerificationMode_Object=MibTableColumn
cpCaptivePortalVerificationMode=_CpCaptivePortalVerificationMode_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,5),_CpCaptivePortalVerificationMode_Type())
cpCaptivePortalVerificationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalVerificationMode.setStatus(_A)
class _CpCaptivePortalUserGroup_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CpCaptivePortalUserGroup_Type.__name__=_L
_CpCaptivePortalUserGroup_Object=MibTableColumn
cpCaptivePortalUserGroup=_CpCaptivePortalUserGroup_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,6),_CpCaptivePortalUserGroup_Type())
cpCaptivePortalUserGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalUserGroup.setStatus(_A)
class _CpCaptivePortalURLRedirectMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpCaptivePortalURLRedirectMode_Type.__name__=_C
_CpCaptivePortalURLRedirectMode_Object=MibTableColumn
cpCaptivePortalURLRedirectMode=_CpCaptivePortalURLRedirectMode_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,7),_CpCaptivePortalURLRedirectMode_Type())
cpCaptivePortalURLRedirectMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalURLRedirectMode.setStatus(_A)
class _CpCaptivePortalRedirectURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CpCaptivePortalRedirectURL_Type.__name__=_H
_CpCaptivePortalRedirectURL_Object=MibTableColumn
cpCaptivePortalRedirectURL=_CpCaptivePortalRedirectURL_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,8),_CpCaptivePortalRedirectURL_Type())
cpCaptivePortalRedirectURL.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalRedirectURL.setStatus(_A)
class _CpCaptivePortalSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_CpCaptivePortalSessionTimeout_Type.__name__=_L
_CpCaptivePortalSessionTimeout_Object=MibTableColumn
cpCaptivePortalSessionTimeout=_CpCaptivePortalSessionTimeout_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,9),_CpCaptivePortalSessionTimeout_Type())
cpCaptivePortalSessionTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalSessionTimeout.setStatus(_A)
class _CpCaptivePortalRadiusAuthServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpCaptivePortalRadiusAuthServer_Type.__name__=_H
_CpCaptivePortalRadiusAuthServer_Object=MibTableColumn
cpCaptivePortalRadiusAuthServer=_CpCaptivePortalRadiusAuthServer_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,11),_CpCaptivePortalRadiusAuthServer_Type())
cpCaptivePortalRadiusAuthServer.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalRadiusAuthServer.setStatus(_A)
_CpCaptivePortalRowStatus_Type=RowStatus
_CpCaptivePortalRowStatus_Object=MibTableColumn
cpCaptivePortalRowStatus=_CpCaptivePortalRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,1,2,1,1,18),_CpCaptivePortalRowStatus_Type())
cpCaptivePortalRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpCaptivePortalRowStatus.setStatus(_A)
_CpLocalUserDatabaseGroup_ObjectIdentity=ObjectIdentity
cpLocalUserDatabaseGroup=_CpLocalUserDatabaseGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,1,3))
_CpLocalUserGroupTable_Object=MibTable
cpLocalUserGroupTable=_CpLocalUserGroupTable_Object((1,3,6,1,4,1,4413,1,1,38,1,3,1))
if mibBuilder.loadTexts:cpLocalUserGroupTable.setStatus(_A)
_CpLocalUserGroupEntry_Object=MibTableRow
cpLocalUserGroupEntry=_CpLocalUserGroupEntry_Object((1,3,6,1,4,1,4413,1,1,38,1,3,1,1))
cpLocalUserGroupEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:cpLocalUserGroupEntry.setStatus(_A)
class _CpLocalUserGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupIndex_Type.__name__=_C
_CpLocalUserGroupIndex_Object=MibTableColumn
cpLocalUserGroupIndex=_CpLocalUserGroupIndex_Object((1,3,6,1,4,1,4413,1,1,38,1,3,1,1,1),_CpLocalUserGroupIndex_Type())
cpLocalUserGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpLocalUserGroupIndex.setStatus(_A)
class _CpLocalUserGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CpLocalUserGroupName_Type.__name__=_H
_CpLocalUserGroupName_Object=MibTableColumn
cpLocalUserGroupName=_CpLocalUserGroupName_Object((1,3,6,1,4,1,4413,1,1,38,1,3,1,1,2),_CpLocalUserGroupName_Type())
cpLocalUserGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:cpLocalUserGroupName.setStatus(_A)
_CpLocalUserGroupRowStatus_Type=RowStatus
_CpLocalUserGroupRowStatus_Object=MibTableColumn
cpLocalUserGroupRowStatus=_CpLocalUserGroupRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,1,3,1,1,3),_CpLocalUserGroupRowStatus_Type())
cpLocalUserGroupRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserGroupRowStatus.setStatus(_A)
_CpLocalUserTable_Object=MibTable
cpLocalUserTable=_CpLocalUserTable_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2))
if mibBuilder.loadTexts:cpLocalUserTable.setStatus(_A)
_CpLocalUserEntry_Object=MibTableRow
cpLocalUserEntry=_CpLocalUserEntry_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1))
cpLocalUserEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:cpLocalUserEntry.setStatus(_A)
class _CpLocalUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserIndex_Type.__name__=_C
_CpLocalUserIndex_Object=MibTableColumn
cpLocalUserIndex=_CpLocalUserIndex_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1,1),_CpLocalUserIndex_Type())
cpLocalUserIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpLocalUserIndex.setStatus(_A)
class _CpLocalUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CpLocalUserName_Type.__name__=_H
_CpLocalUserName_Object=MibTableColumn
cpLocalUserName=_CpLocalUserName_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1,2),_CpLocalUserName_Type())
cpLocalUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:cpLocalUserName.setStatus(_A)
class _CpLocalUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,64))
_CpLocalUserPassword_Type.__name__=_H
_CpLocalUserPassword_Object=MibTableColumn
cpLocalUserPassword=_CpLocalUserPassword_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1,3),_CpLocalUserPassword_Type())
cpLocalUserPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:cpLocalUserPassword.setStatus(_A)
class _CpLocalUserSessionTimeout_Type(Unsigned32):defaultValue=0
_CpLocalUserSessionTimeout_Type.__name__=_L
_CpLocalUserSessionTimeout_Object=MibTableColumn
cpLocalUserSessionTimeout=_CpLocalUserSessionTimeout_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1,4),_CpLocalUserSessionTimeout_Type())
cpLocalUserSessionTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cpLocalUserSessionTimeout.setStatus(_A)
_CpLocalUserRowStatus_Type=RowStatus
_CpLocalUserRowStatus_Object=MibTableColumn
cpLocalUserRowStatus=_CpLocalUserRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,1,3,2,1,11),_CpLocalUserRowStatus_Type())
cpLocalUserRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserRowStatus.setStatus(_A)
_CpLocalUserGroupAssociationTable_Object=MibTable
cpLocalUserGroupAssociationTable=_CpLocalUserGroupAssociationTable_Object((1,3,6,1,4,1,4413,1,1,38,1,3,3))
if mibBuilder.loadTexts:cpLocalUserGroupAssociationTable.setStatus(_A)
_CpLocalUserGroupAssociationEntry_Object=MibTableRow
cpLocalUserGroupAssociationEntry=_CpLocalUserGroupAssociationEntry_Object((1,3,6,1,4,1,4413,1,1,38,1,3,3,1))
cpLocalUserGroupAssociationEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:cpLocalUserGroupAssociationEntry.setStatus(_A)
class _CpLocalUserGroupAssociationUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupAssociationUserIndex_Type.__name__=_C
_CpLocalUserGroupAssociationUserIndex_Object=MibTableColumn
cpLocalUserGroupAssociationUserIndex=_CpLocalUserGroupAssociationUserIndex_Object((1,3,6,1,4,1,4413,1,1,38,1,3,3,1,1),_CpLocalUserGroupAssociationUserIndex_Type())
cpLocalUserGroupAssociationUserIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationUserIndex.setStatus(_A)
class _CpLocalUserGroupAssociationGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpLocalUserGroupAssociationGroupIndex_Type.__name__=_C
_CpLocalUserGroupAssociationGroupIndex_Object=MibTableColumn
cpLocalUserGroupAssociationGroupIndex=_CpLocalUserGroupAssociationGroupIndex_Object((1,3,6,1,4,1,4413,1,1,38,1,3,3,1,2),_CpLocalUserGroupAssociationGroupIndex_Type())
cpLocalUserGroupAssociationGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationGroupIndex.setStatus(_A)
_CpLocalUserGroupAssociationRowStatus_Type=RowStatus
_CpLocalUserGroupAssociationRowStatus_Object=MibTableColumn
cpLocalUserGroupAssociationRowStatus=_CpLocalUserGroupAssociationRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,1,3,3,1,3),_CpLocalUserGroupAssociationRowStatus_Type())
cpLocalUserGroupAssociationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpLocalUserGroupAssociationRowStatus.setStatus(_A)
_CpInterfaceAssociationGroup_ObjectIdentity=ObjectIdentity
cpInterfaceAssociationGroup=_CpInterfaceAssociationGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,1,4))
_CpInterfaceAssociationTable_Object=MibTable
cpInterfaceAssociationTable=_CpInterfaceAssociationTable_Object((1,3,6,1,4,1,4413,1,1,38,1,4,1))
if mibBuilder.loadTexts:cpInterfaceAssociationTable.setStatus(_A)
_CpInterfaceAssociationEntry_Object=MibTableRow
cpInterfaceAssociationEntry=_CpInterfaceAssociationEntry_Object((1,3,6,1,4,1,4413,1,1,38,1,4,1,1))
cpInterfaceAssociationEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:cpInterfaceAssociationEntry.setStatus(_A)
_CpIntfAssociationCPID_Type=Unsigned32
_CpIntfAssociationCPID_Object=MibTableColumn
cpIntfAssociationCPID=_CpIntfAssociationCPID_Object((1,3,6,1,4,1,4413,1,1,38,1,4,1,1,1),_CpIntfAssociationCPID_Type())
cpIntfAssociationCPID.setMaxAccess(_I)
if mibBuilder.loadTexts:cpIntfAssociationCPID.setStatus(_A)
_CpIntfAssociationIfIndex_Type=InterfaceIndex
_CpIntfAssociationIfIndex_Object=MibTableColumn
cpIntfAssociationIfIndex=_CpIntfAssociationIfIndex_Object((1,3,6,1,4,1,4413,1,1,38,1,4,1,1,2),_CpIntfAssociationIfIndex_Type())
cpIntfAssociationIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cpIntfAssociationIfIndex.setStatus(_A)
_CpIntfAssociationRowStatus_Type=RowStatus
_CpIntfAssociationRowStatus_Object=MibTableColumn
cpIntfAssociationRowStatus=_CpIntfAssociationRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,1,4,1,1,3),_CpIntfAssociationRowStatus_Type())
cpIntfAssociationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:cpIntfAssociationRowStatus.setStatus(_A)
_CpStatusGroup_ObjectIdentity=ObjectIdentity
cpStatusGroup=_CpStatusGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2))
_CpCaptivePortalGlobalStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalGlobalStatusGroup=_CpCaptivePortalGlobalStatusGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,1))
class _CpCaptivePortalOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('enablePending',0),('enabled',1),('disablePending',2),('disabled',3)))
_CpCaptivePortalOperStatus_Type.__name__=_C
_CpCaptivePortalOperStatus_Object=MibScalar
cpCaptivePortalOperStatus=_CpCaptivePortalOperStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,1,1),_CpCaptivePortalOperStatus_Type())
cpCaptivePortalOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalOperStatus.setStatus(_A)
class _CpCaptivePortalOperDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),(_Q,1),('noIPAddress',2),('noIPRoutingIntf',3),('routingDisabled',4)))
_CpCaptivePortalOperDisabledReason_Type.__name__=_C
_CpCaptivePortalOperDisabledReason_Object=MibScalar
cpCaptivePortalOperDisabledReason=_CpCaptivePortalOperDisabledReason_Object((1,3,6,1,4,1,4413,1,1,38,2,1,2),_CpCaptivePortalOperDisabledReason_Type())
cpCaptivePortalOperDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalOperDisabledReason.setStatus(_A)
_CpCaptivePortalIpv4Address_Type=IpAddress
_CpCaptivePortalIpv4Address_Object=MibScalar
cpCaptivePortalIpv4Address=_CpCaptivePortalIpv4Address_Object((1,3,6,1,4,1,4413,1,1,38,2,1,3),_CpCaptivePortalIpv4Address_Type())
cpCaptivePortalIpv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIpv4Address.setStatus(_A)
class _CpCaptivePortalInstanceMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CpCaptivePortalInstanceMaxCount_Type.__name__=_C
_CpCaptivePortalInstanceMaxCount_Object=MibScalar
cpCaptivePortalInstanceMaxCount=_CpCaptivePortalInstanceMaxCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,4),_CpCaptivePortalInstanceMaxCount_Type())
cpCaptivePortalInstanceMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceMaxCount.setStatus(_A)
_CpCaptivePortalInstanceConfiguredCount_Type=Integer32
_CpCaptivePortalInstanceConfiguredCount_Object=MibScalar
cpCaptivePortalInstanceConfiguredCount=_CpCaptivePortalInstanceConfiguredCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,5),_CpCaptivePortalInstanceConfiguredCount_Type())
cpCaptivePortalInstanceConfiguredCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceConfiguredCount.setStatus(_A)
_CpCaptivePortalInstanceActiveCount_Type=Integer32
_CpCaptivePortalInstanceActiveCount_Object=MibScalar
cpCaptivePortalInstanceActiveCount=_CpCaptivePortalInstanceActiveCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,6),_CpCaptivePortalInstanceActiveCount_Type())
cpCaptivePortalInstanceActiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceActiveCount.setStatus(_A)
class _CpCaptivePortalAuthenUserMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CpCaptivePortalAuthenUserMaxCount_Type.__name__=_C
_CpCaptivePortalAuthenUserMaxCount_Object=MibScalar
cpCaptivePortalAuthenUserMaxCount=_CpCaptivePortalAuthenUserMaxCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,7),_CpCaptivePortalAuthenUserMaxCount_Type())
cpCaptivePortalAuthenUserMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalAuthenUserMaxCount.setStatus(_A)
class _CpCaptivePortalLocalUserMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CpCaptivePortalLocalUserMaxCount_Type.__name__=_C
_CpCaptivePortalLocalUserMaxCount_Object=MibScalar
cpCaptivePortalLocalUserMaxCount=_CpCaptivePortalLocalUserMaxCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,8),_CpCaptivePortalLocalUserMaxCount_Type())
cpCaptivePortalLocalUserMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalLocalUserMaxCount.setStatus(_A)
_CpCaptivePortalConfiguredLocalUserCount_Type=Integer32
_CpCaptivePortalConfiguredLocalUserCount_Object=MibScalar
cpCaptivePortalConfiguredLocalUserCount=_CpCaptivePortalConfiguredLocalUserCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,9),_CpCaptivePortalConfiguredLocalUserCount_Type())
cpCaptivePortalConfiguredLocalUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalConfiguredLocalUserCount.setStatus(_A)
_CpCaptivePortalAuthenUserCurrentCount_Type=Integer32
_CpCaptivePortalAuthenUserCurrentCount_Object=MibScalar
cpCaptivePortalAuthenUserCurrentCount=_CpCaptivePortalAuthenUserCurrentCount_Object((1,3,6,1,4,1,4413,1,1,38,2,1,10),_CpCaptivePortalAuthenUserCurrentCount_Type())
cpCaptivePortalAuthenUserCurrentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalAuthenUserCurrentCount.setStatus(_A)
_CpCaptivePortalInstanceStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalInstanceStatusGroup=_CpCaptivePortalInstanceStatusGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,2))
_CpCaptivePortalInstanceStatusTable_Object=MibTable
cpCaptivePortalInstanceStatusTable=_CpCaptivePortalInstanceStatusTable_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1))
if mibBuilder.loadTexts:cpCaptivePortalInstanceStatusTable.setStatus(_A)
_CpCaptivePortalInstanceStatusEntry_Object=MibTableRow
cpCaptivePortalInstanceStatusEntry=_CpCaptivePortalInstanceStatusEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1,1))
cpCaptivePortalInstanceStatusEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:cpCaptivePortalInstanceStatusEntry.setStatus(_A)
class _CpCaptivePortalInstanceOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpCaptivePortalInstanceOperStatus_Type.__name__=_C
_CpCaptivePortalInstanceOperStatus_Object=MibTableColumn
cpCaptivePortalInstanceOperStatus=_CpCaptivePortalInstanceOperStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1,1,1),_CpCaptivePortalInstanceOperStatus_Type())
cpCaptivePortalInstanceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceOperStatus.setStatus(_A)
class _CpCaptivePortalInstanceOperDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_N,0),(_Q,1),('noRadiusServer',2),('noAccountingServer',3),('noIntfAssociation',4),('noActiveIntf',5),('noValidCert',6)))
_CpCaptivePortalInstanceOperDisabledReason_Type.__name__=_C
_CpCaptivePortalInstanceOperDisabledReason_Object=MibTableColumn
cpCaptivePortalInstanceOperDisabledReason=_CpCaptivePortalInstanceOperDisabledReason_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1,1,2),_CpCaptivePortalInstanceOperDisabledReason_Type())
cpCaptivePortalInstanceOperDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceOperDisabledReason.setStatus(_A)
class _CpCaptivePortalInstanceBlockStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('blockPending',0),(_Z,1),('notBlockPending',2),(_a,3)))
_CpCaptivePortalInstanceBlockStatus_Type.__name__=_C
_CpCaptivePortalInstanceBlockStatus_Object=MibTableColumn
cpCaptivePortalInstanceBlockStatus=_CpCaptivePortalInstanceBlockStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1,1,3),_CpCaptivePortalInstanceBlockStatus_Type())
cpCaptivePortalInstanceBlockStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalInstanceBlockStatus.setStatus(_A)
_CpCaptivePortalInstanceAuthUserCount_Type=Integer32
_CpCaptivePortalInstanceAuthUserCount_Object=MibTableColumn
cpCaptivePortalInstanceAuthUserCount=_CpCaptivePortalInstanceAuthUserCount_Object((1,3,6,1,4,1,4413,1,1,38,2,2,1,1,4),_CpCaptivePortalInstanceAuthUserCount_Type())
cpCaptivePortalInstanceAuthUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceAuthUserCount.setStatus(_A)
_CpCaptivePortalIntfStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfStatusGroup=_CpCaptivePortalIntfStatusGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,3))
_CpCaptivePortalIntfStatusTable_Object=MibTable
cpCaptivePortalIntfStatusTable=_CpCaptivePortalIntfStatusTable_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfStatusTable.setStatus(_A)
_CpCaptivePortalIntfStatusEntry_Object=MibTableRow
cpCaptivePortalIntfStatusEntry=_CpCaptivePortalIntfStatusEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1))
cpCaptivePortalIntfStatusEntry.setIndexNames((0,_D,_M),(0,_D,_R))
if mibBuilder.loadTexts:cpCaptivePortalIntfStatusEntry.setStatus(_A)
_CpCaptivePortalIntfIfIndex_Type=InterfaceIndex
_CpCaptivePortalIntfIfIndex_Object=MibTableColumn
cpCaptivePortalIntfIfIndex=_CpCaptivePortalIntfIfIndex_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1,1),_CpCaptivePortalIntfIfIndex_Type())
cpCaptivePortalIntfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfIfIndex.setStatus(_A)
class _CpCaptivePortalIntfOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpCaptivePortalIntfOperStatus_Type.__name__=_C
_CpCaptivePortalIntfOperStatus_Object=MibTableColumn
cpCaptivePortalIntfOperStatus=_CpCaptivePortalIntfOperStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1,2),_CpCaptivePortalIntfOperStatus_Type())
cpCaptivePortalIntfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfOperStatus.setStatus(_A)
class _CpCaptivePortalIntfOperDisabledReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('intfNotAttached',1),(_Q,2)))
_CpCaptivePortalIntfOperDisabledReason_Type.__name__=_C
_CpCaptivePortalIntfOperDisabledReason_Object=MibTableColumn
cpCaptivePortalIntfOperDisabledReason=_CpCaptivePortalIntfOperDisabledReason_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1,3),_CpCaptivePortalIntfOperDisabledReason_Type())
cpCaptivePortalIntfOperDisabledReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfOperDisabledReason.setStatus(_A)
class _CpCaptivePortalIntfBlockStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Z,0),(_a,1)))
_CpCaptivePortalIntfBlockStatus_Type.__name__=_C
_CpCaptivePortalIntfBlockStatus_Object=MibTableColumn
cpCaptivePortalIntfBlockStatus=_CpCaptivePortalIntfBlockStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1,4),_CpCaptivePortalIntfBlockStatus_Type())
cpCaptivePortalIntfBlockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfBlockStatus.setStatus(_A)
_CpCaptivePortalIntfAuthUserCount_Type=Integer32
_CpCaptivePortalIntfAuthUserCount_Object=MibTableColumn
cpCaptivePortalIntfAuthUserCount=_CpCaptivePortalIntfAuthUserCount_Object((1,3,6,1,4,1,4413,1,1,38,2,3,1,1,5),_CpCaptivePortalIntfAuthUserCount_Type())
cpCaptivePortalIntfAuthUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfAuthUserCount.setStatus(_A)
_CpCaptivePortalIntfDatabaseGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfDatabaseGroup=_CpCaptivePortalIntfDatabaseGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,4))
_CpCaptivePortalIntfDatabaseTable_Object=MibTable
cpCaptivePortalIntfDatabaseTable=_CpCaptivePortalIntfDatabaseTable_Object((1,3,6,1,4,1,4413,1,1,38,2,4,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfDatabaseTable.setStatus(_A)
_CpCaptivePortalIntfDatabaseEntry_Object=MibTableRow
cpCaptivePortalIntfDatabaseEntry=_CpCaptivePortalIntfDatabaseEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,4,1,1))
cpCaptivePortalIntfDatabaseEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:cpCaptivePortalIntfDatabaseEntry.setStatus(_A)
_CpCaptivePortalIntfCapabilities_Type=CpCaptivePortalIntfCapabilitiesMap
_CpCaptivePortalIntfCapabilities_Object=MibTableColumn
cpCaptivePortalIntfCapabilities=_CpCaptivePortalIntfCapabilities_Object((1,3,6,1,4,1,4413,1,1,38,2,4,1,1,1),_CpCaptivePortalIntfCapabilities_Type())
cpCaptivePortalIntfCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfCapabilities.setStatus(_A)
_CpCaptivePortalClientStatusGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalClientStatusGroup=_CpCaptivePortalClientStatusGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,5))
_CpCaptivePortalClientStatusTable_Object=MibTable
cpCaptivePortalClientStatusTable=_CpCaptivePortalClientStatusTable_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1))
if mibBuilder.loadTexts:cpCaptivePortalClientStatusTable.setStatus(_A)
_CpCaptivePortalClientStatusEntry_Object=MibTableRow
cpCaptivePortalClientStatusEntry=_CpCaptivePortalClientStatusEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1))
cpCaptivePortalClientStatusEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cpCaptivePortalClientStatusEntry.setStatus(_A)
_CpCaptivePortalClientMacAddress_Type=MacAddress
_CpCaptivePortalClientMacAddress_Object=MibTableColumn
cpCaptivePortalClientMacAddress=_CpCaptivePortalClientMacAddress_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,1),_CpCaptivePortalClientMacAddress_Type())
cpCaptivePortalClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientMacAddress.setStatus(_A)
_CpCaptivePortalClientIpAddress_Type=IpAddress
_CpCaptivePortalClientIpAddress_Object=MibTableColumn
cpCaptivePortalClientIpAddress=_CpCaptivePortalClientIpAddress_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,2),_CpCaptivePortalClientIpAddress_Type())
cpCaptivePortalClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientIpAddress.setStatus(_A)
class _CpCaptivePortalClientUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpCaptivePortalClientUserName_Type.__name__=_H
_CpCaptivePortalClientUserName_Object=MibTableColumn
cpCaptivePortalClientUserName=_CpCaptivePortalClientUserName_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,3),_CpCaptivePortalClientUserName_Type())
cpCaptivePortalClientUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientUserName.setStatus(_A)
class _CpCaptivePortalClientProtocolMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('https',0),('http',1)))
_CpCaptivePortalClientProtocolMode_Type.__name__=_C
_CpCaptivePortalClientProtocolMode_Object=MibTableColumn
cpCaptivePortalClientProtocolMode=_CpCaptivePortalClientProtocolMode_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,4),_CpCaptivePortalClientProtocolMode_Type())
cpCaptivePortalClientProtocolMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientProtocolMode.setStatus(_A)
class _CpCaptivePortalClientVerificationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('guest',0),('local',1),(_S,2)))
_CpCaptivePortalClientVerificationMode_Type.__name__=_C
_CpCaptivePortalClientVerificationMode_Object=MibTableColumn
cpCaptivePortalClientVerificationMode=_CpCaptivePortalClientVerificationMode_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,5),_CpCaptivePortalClientVerificationMode_Type())
cpCaptivePortalClientVerificationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientVerificationMode.setStatus(_A)
_CpCaptivePortalClientAssocIfIndex_Type=InterfaceIndex
_CpCaptivePortalClientAssocIfIndex_Object=MibTableColumn
cpCaptivePortalClientAssocIfIndex=_CpCaptivePortalClientAssocIfIndex_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,6),_CpCaptivePortalClientAssocIfIndex_Type())
cpCaptivePortalClientAssocIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientAssocIfIndex.setStatus(_A)
_CpCaptivePortalClientCPID_Type=Integer32
_CpCaptivePortalClientCPID_Object=MibTableColumn
cpCaptivePortalClientCPID=_CpCaptivePortalClientCPID_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,7),_CpCaptivePortalClientCPID_Type())
cpCaptivePortalClientCPID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientCPID.setStatus(_A)
_CpCaptivePortalClientSessionTime_Type=TimeTicks
_CpCaptivePortalClientSessionTime_Object=MibTableColumn
cpCaptivePortalClientSessionTime=_CpCaptivePortalClientSessionTime_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,8),_CpCaptivePortalClientSessionTime_Type())
cpCaptivePortalClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientSessionTime.setStatus(_A)
class _CpCaptivePortalClientDeauthAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('start',2)))
_CpCaptivePortalClientDeauthAction_Type.__name__=_C
_CpCaptivePortalClientDeauthAction_Object=MibTableColumn
cpCaptivePortalClientDeauthAction=_CpCaptivePortalClientDeauthAction_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,12),_CpCaptivePortalClientDeauthAction_Type())
cpCaptivePortalClientDeauthAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cpCaptivePortalClientDeauthAction.setStatus(_A)
_CpCaptivePortalClientAuthFailureConnectionAttempts_Type=Integer32
_CpCaptivePortalClientAuthFailureConnectionAttempts_Object=MibTableColumn
cpCaptivePortalClientAuthFailureConnectionAttempts=_CpCaptivePortalClientAuthFailureConnectionAttempts_Object((1,3,6,1,4,1,4413,1,1,38,2,5,1,1,13),_CpCaptivePortalClientAuthFailureConnectionAttempts_Type())
cpCaptivePortalClientAuthFailureConnectionAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalClientAuthFailureConnectionAttempts.setStatus(_A)
_CpCaptivePortalIntfClientAssocGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalIntfClientAssocGroup=_CpCaptivePortalIntfClientAssocGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,6))
_CpCaptivePortalIntfClientAssocTable_Object=MibTable
cpCaptivePortalIntfClientAssocTable=_CpCaptivePortalIntfClientAssocTable_Object((1,3,6,1,4,1,4413,1,1,38,2,6,1))
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocTable.setStatus(_A)
_CpCaptivePortalIntfClientAssocEntry_Object=MibTableRow
cpCaptivePortalIntfClientAssocEntry=_CpCaptivePortalIntfClientAssocEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,6,1,1))
cpCaptivePortalIntfClientAssocEntry.setIndexNames((0,_D,_O),(0,_D,_b))
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocEntry.setStatus(_A)
_CpCaptivePortalIntfClientIfIndex_Type=InterfaceIndex
_CpCaptivePortalIntfClientIfIndex_Object=MibTableColumn
cpCaptivePortalIntfClientIfIndex=_CpCaptivePortalIntfClientIfIndex_Object((1,3,6,1,4,1,4413,1,1,38,2,6,1,1,1),_CpCaptivePortalIntfClientIfIndex_Type())
cpCaptivePortalIntfClientIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientIfIndex.setStatus(_A)
_CpCaptivePortalIntfClientAssocMacAddress_Type=MacAddress
_CpCaptivePortalIntfClientAssocMacAddress_Object=MibTableColumn
cpCaptivePortalIntfClientAssocMacAddress=_CpCaptivePortalIntfClientAssocMacAddress_Object((1,3,6,1,4,1,4413,1,1,38,2,6,1,1,2),_CpCaptivePortalIntfClientAssocMacAddress_Type())
cpCaptivePortalIntfClientAssocMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocMacAddress.setStatus(_A)
_CpCaptivePortalIntfClientAssocRowStatus_Type=RowStatus
_CpCaptivePortalIntfClientAssocRowStatus_Object=MibTableColumn
cpCaptivePortalIntfClientAssocRowStatus=_CpCaptivePortalIntfClientAssocRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,6,1,1,3),_CpCaptivePortalIntfClientAssocRowStatus_Type())
cpCaptivePortalIntfClientAssocRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalIntfClientAssocRowStatus.setStatus(_A)
_CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity=ObjectIdentity
cpCaptivePortalInstanceClientAssocGroup=_CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,2,7))
_CpCaptivePortalInstanceClientAssocTable_Object=MibTable
cpCaptivePortalInstanceClientAssocTable=_CpCaptivePortalInstanceClientAssocTable_Object((1,3,6,1,4,1,4413,1,1,38,2,7,1))
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocTable.setStatus(_A)
_CpCaptivePortalInstanceClientAssocEntry_Object=MibTableRow
cpCaptivePortalInstanceClientAssocEntry=_CpCaptivePortalInstanceClientAssocEntry_Object((1,3,6,1,4,1,4413,1,1,38,2,7,1,1))
cpCaptivePortalInstanceClientAssocEntry.setIndexNames((0,_D,_P),(0,_D,_c))
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocEntry.setStatus(_A)
class _CpCaptivePortalInstanceClientAssocInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CpCaptivePortalInstanceClientAssocInstanceId_Type.__name__=_C
_CpCaptivePortalInstanceClientAssocInstanceId_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocInstanceId=_CpCaptivePortalInstanceClientAssocInstanceId_Object((1,3,6,1,4,1,4413,1,1,38,2,7,1,1,1),_CpCaptivePortalInstanceClientAssocInstanceId_Type())
cpCaptivePortalInstanceClientAssocInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocInstanceId.setStatus(_A)
_CpCaptivePortalInstanceClientAssocMacAddress_Type=MacAddress
_CpCaptivePortalInstanceClientAssocMacAddress_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocMacAddress=_CpCaptivePortalInstanceClientAssocMacAddress_Object((1,3,6,1,4,1,4413,1,1,38,2,7,1,1,2),_CpCaptivePortalInstanceClientAssocMacAddress_Type())
cpCaptivePortalInstanceClientAssocMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocMacAddress.setStatus(_A)
_CpCaptivePortalInstanceClientAssocRowStatus_Type=RowStatus
_CpCaptivePortalInstanceClientAssocRowStatus_Object=MibTableColumn
cpCaptivePortalInstanceClientAssocRowStatus=_CpCaptivePortalInstanceClientAssocRowStatus_Object((1,3,6,1,4,1,4413,1,1,38,2,7,1,1,3),_CpCaptivePortalInstanceClientAssocRowStatus_Type())
cpCaptivePortalInstanceClientAssocRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpCaptivePortalInstanceClientAssocRowStatus.setStatus(_A)
_CpTrapsConfig_ObjectIdentity=ObjectIdentity
cpTrapsConfig=_CpTrapsConfig_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,3))
class _CpTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpTrapMode_Type.__name__=_C
_CpTrapMode_Object=MibScalar
cpTrapMode=_CpTrapMode_Object((1,3,6,1,4,1,4413,1,1,38,3,1),_CpTrapMode_Type())
cpTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpTrapMode.setStatus(_A)
class _CpClientAuthenticationFailureTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpClientAuthenticationFailureTrapMode_Type.__name__=_C
_CpClientAuthenticationFailureTrapMode_Object=MibScalar
cpClientAuthenticationFailureTrapMode=_CpClientAuthenticationFailureTrapMode_Object((1,3,6,1,4,1,4413,1,1,38,3,2),_CpClientAuthenticationFailureTrapMode_Type())
cpClientAuthenticationFailureTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpClientAuthenticationFailureTrapMode.setStatus(_A)
class _CpClientConnectTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpClientConnectTrapMode_Type.__name__=_C
_CpClientConnectTrapMode_Object=MibScalar
cpClientConnectTrapMode=_CpClientConnectTrapMode_Object((1,3,6,1,4,1,4413,1,1,38,3,3),_CpClientConnectTrapMode_Type())
cpClientConnectTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpClientConnectTrapMode.setStatus(_A)
class _CpClientDatabaseFullTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpClientDatabaseFullTrapMode_Type.__name__=_C
_CpClientDatabaseFullTrapMode_Object=MibScalar
cpClientDatabaseFullTrapMode=_CpClientDatabaseFullTrapMode_Object((1,3,6,1,4,1,4413,1,1,38,3,4),_CpClientDatabaseFullTrapMode_Type())
cpClientDatabaseFullTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpClientDatabaseFullTrapMode.setStatus(_A)
class _CpClientDisconnectTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_CpClientDisconnectTrapMode_Type.__name__=_C
_CpClientDisconnectTrapMode_Object=MibScalar
cpClientDisconnectTrapMode=_CpClientDisconnectTrapMode_Object((1,3,6,1,4,1,4413,1,1,38,3,5),_CpClientDisconnectTrapMode_Type())
cpClientDisconnectTrapMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cpClientDisconnectTrapMode.setStatus(_A)
_CpTraps_ObjectIdentity=ObjectIdentity
cpTraps=_CpTraps_ObjectIdentity((1,3,6,1,4,1,4413,1,1,38,4))
cpClientAuthenticationFailure=NotificationType((1,3,6,1,4,1,4413,1,1,38,4,1))
cpClientAuthenticationFailure.setObjects(*((_D,_J),(_D,_d),(_D,_e),(_D,_f),(_D,_g),(_D,_h)))
if mibBuilder.loadTexts:cpClientAuthenticationFailure.setStatus(_A)
cpClientConnect=NotificationType((1,3,6,1,4,1,4413,1,1,38,4,2))
cpClientConnect.setObjects(*((_D,_J),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:cpClientConnect.setStatus(_A)
cpClientDatabaseFull=NotificationType((1,3,6,1,4,1,4413,1,1,38,4,3))
cpClientDatabaseFull.setObjects((_D,_J))
if mibBuilder.loadTexts:cpClientDatabaseFull.setStatus(_A)
cpClientDisconnect=NotificationType((1,3,6,1,4,1,4413,1,1,38,4,4))
cpClientDisconnect.setObjects(*((_D,_J),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:cpClientDisconnect.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'CpCaptivePortalIntfCapabilitiesMap':CpCaptivePortalIntfCapabilitiesMap,'fastPathCaptivePortal':fastPathCaptivePortal,'cpConfigGroup':cpConfigGroup,'cpGlobalConfigGroup':cpGlobalConfigGroup,'cpAdminMode':cpAdminMode,'cpAdditionalHttpPort':cpAdditionalHttpPort,'cpAdditionalHttpSecurePort':cpAdditionalHttpSecurePort,'cpAuthTimeout':cpAuthTimeout,'cpCaptivePortalConfigGroup':cpCaptivePortalConfigGroup,'cpCaptivePortalTable':cpCaptivePortalTable,'cpCaptivePortalEntry':cpCaptivePortalEntry,_M:cpCaptivePortalInstanceId,'cpCaptivePortalConfigName':cpCaptivePortalConfigName,'cpCaptivePortalAdminMode':cpCaptivePortalAdminMode,'cpCaptivePortalProtocolMode':cpCaptivePortalProtocolMode,'cpCaptivePortalVerificationMode':cpCaptivePortalVerificationMode,'cpCaptivePortalUserGroup':cpCaptivePortalUserGroup,'cpCaptivePortalURLRedirectMode':cpCaptivePortalURLRedirectMode,'cpCaptivePortalRedirectURL':cpCaptivePortalRedirectURL,'cpCaptivePortalSessionTimeout':cpCaptivePortalSessionTimeout,'cpCaptivePortalRadiusAuthServer':cpCaptivePortalRadiusAuthServer,'cpCaptivePortalRowStatus':cpCaptivePortalRowStatus,'cpLocalUserDatabaseGroup':cpLocalUserDatabaseGroup,'cpLocalUserGroupTable':cpLocalUserGroupTable,'cpLocalUserGroupEntry':cpLocalUserGroupEntry,_T:cpLocalUserGroupIndex,'cpLocalUserGroupName':cpLocalUserGroupName,'cpLocalUserGroupRowStatus':cpLocalUserGroupRowStatus,'cpLocalUserTable':cpLocalUserTable,'cpLocalUserEntry':cpLocalUserEntry,_U:cpLocalUserIndex,'cpLocalUserName':cpLocalUserName,'cpLocalUserPassword':cpLocalUserPassword,'cpLocalUserSessionTimeout':cpLocalUserSessionTimeout,'cpLocalUserRowStatus':cpLocalUserRowStatus,'cpLocalUserGroupAssociationTable':cpLocalUserGroupAssociationTable,'cpLocalUserGroupAssociationEntry':cpLocalUserGroupAssociationEntry,_V:cpLocalUserGroupAssociationUserIndex,_W:cpLocalUserGroupAssociationGroupIndex,'cpLocalUserGroupAssociationRowStatus':cpLocalUserGroupAssociationRowStatus,'cpInterfaceAssociationGroup':cpInterfaceAssociationGroup,'cpInterfaceAssociationTable':cpInterfaceAssociationTable,'cpInterfaceAssociationEntry':cpInterfaceAssociationEntry,_X:cpIntfAssociationCPID,_Y:cpIntfAssociationIfIndex,'cpIntfAssociationRowStatus':cpIntfAssociationRowStatus,'cpStatusGroup':cpStatusGroup,'cpCaptivePortalGlobalStatusGroup':cpCaptivePortalGlobalStatusGroup,'cpCaptivePortalOperStatus':cpCaptivePortalOperStatus,'cpCaptivePortalOperDisabledReason':cpCaptivePortalOperDisabledReason,'cpCaptivePortalIpv4Address':cpCaptivePortalIpv4Address,'cpCaptivePortalInstanceMaxCount':cpCaptivePortalInstanceMaxCount,'cpCaptivePortalInstanceConfiguredCount':cpCaptivePortalInstanceConfiguredCount,'cpCaptivePortalInstanceActiveCount':cpCaptivePortalInstanceActiveCount,'cpCaptivePortalAuthenUserMaxCount':cpCaptivePortalAuthenUserMaxCount,'cpCaptivePortalLocalUserMaxCount':cpCaptivePortalLocalUserMaxCount,'cpCaptivePortalConfiguredLocalUserCount':cpCaptivePortalConfiguredLocalUserCount,'cpCaptivePortalAuthenUserCurrentCount':cpCaptivePortalAuthenUserCurrentCount,'cpCaptivePortalInstanceStatusGroup':cpCaptivePortalInstanceStatusGroup,'cpCaptivePortalInstanceStatusTable':cpCaptivePortalInstanceStatusTable,'cpCaptivePortalInstanceStatusEntry':cpCaptivePortalInstanceStatusEntry,'cpCaptivePortalInstanceOperStatus':cpCaptivePortalInstanceOperStatus,'cpCaptivePortalInstanceOperDisabledReason':cpCaptivePortalInstanceOperDisabledReason,'cpCaptivePortalInstanceBlockStatus':cpCaptivePortalInstanceBlockStatus,'cpCaptivePortalInstanceAuthUserCount':cpCaptivePortalInstanceAuthUserCount,'cpCaptivePortalIntfStatusGroup':cpCaptivePortalIntfStatusGroup,'cpCaptivePortalIntfStatusTable':cpCaptivePortalIntfStatusTable,'cpCaptivePortalIntfStatusEntry':cpCaptivePortalIntfStatusEntry,_R:cpCaptivePortalIntfIfIndex,'cpCaptivePortalIntfOperStatus':cpCaptivePortalIntfOperStatus,'cpCaptivePortalIntfOperDisabledReason':cpCaptivePortalIntfOperDisabledReason,'cpCaptivePortalIntfBlockStatus':cpCaptivePortalIntfBlockStatus,'cpCaptivePortalIntfAuthUserCount':cpCaptivePortalIntfAuthUserCount,'cpCaptivePortalIntfDatabaseGroup':cpCaptivePortalIntfDatabaseGroup,'cpCaptivePortalIntfDatabaseTable':cpCaptivePortalIntfDatabaseTable,'cpCaptivePortalIntfDatabaseEntry':cpCaptivePortalIntfDatabaseEntry,'cpCaptivePortalIntfCapabilities':cpCaptivePortalIntfCapabilities,'cpCaptivePortalClientStatusGroup':cpCaptivePortalClientStatusGroup,'cpCaptivePortalClientStatusTable':cpCaptivePortalClientStatusTable,'cpCaptivePortalClientStatusEntry':cpCaptivePortalClientStatusEntry,_J:cpCaptivePortalClientMacAddress,_d:cpCaptivePortalClientIpAddress,_g:cpCaptivePortalClientUserName,'cpCaptivePortalClientProtocolMode':cpCaptivePortalClientProtocolMode,'cpCaptivePortalClientVerificationMode':cpCaptivePortalClientVerificationMode,_f:cpCaptivePortalClientAssocIfIndex,_e:cpCaptivePortalClientCPID,'cpCaptivePortalClientSessionTime':cpCaptivePortalClientSessionTime,'cpCaptivePortalClientDeauthAction':cpCaptivePortalClientDeauthAction,_h:cpCaptivePortalClientAuthFailureConnectionAttempts,'cpCaptivePortalIntfClientAssocGroup':cpCaptivePortalIntfClientAssocGroup,'cpCaptivePortalIntfClientAssocTable':cpCaptivePortalIntfClientAssocTable,'cpCaptivePortalIntfClientAssocEntry':cpCaptivePortalIntfClientAssocEntry,_O:cpCaptivePortalIntfClientIfIndex,_b:cpCaptivePortalIntfClientAssocMacAddress,'cpCaptivePortalIntfClientAssocRowStatus':cpCaptivePortalIntfClientAssocRowStatus,'cpCaptivePortalInstanceClientAssocGroup':cpCaptivePortalInstanceClientAssocGroup,'cpCaptivePortalInstanceClientAssocTable':cpCaptivePortalInstanceClientAssocTable,'cpCaptivePortalInstanceClientAssocEntry':cpCaptivePortalInstanceClientAssocEntry,_P:cpCaptivePortalInstanceClientAssocInstanceId,_c:cpCaptivePortalInstanceClientAssocMacAddress,'cpCaptivePortalInstanceClientAssocRowStatus':cpCaptivePortalInstanceClientAssocRowStatus,'cpTrapsConfig':cpTrapsConfig,'cpTrapMode':cpTrapMode,'cpClientAuthenticationFailureTrapMode':cpClientAuthenticationFailureTrapMode,'cpClientConnectTrapMode':cpClientConnectTrapMode,'cpClientDatabaseFullTrapMode':cpClientDatabaseFullTrapMode,'cpClientDisconnectTrapMode':cpClientDisconnectTrapMode,'cpTraps':cpTraps,'cpClientAuthenticationFailure':cpClientAuthenticationFailure,'cpClientConnect':cpClientConnect,'cpClientDatabaseFull':cpClientDatabaseFull,'cpClientDisconnect':cpClientDisconnect})