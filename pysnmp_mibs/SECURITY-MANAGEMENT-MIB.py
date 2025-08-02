_A8='avASGAFDownloadSuccess'
_A7='avASGAFDownloadFailure'
_A6='avConfigurationMasterKeyChange'
_A5='avConfigurationEncKeyMismatchFault'
_A4='avMSSDenialOfService'
_A3='avDuplicatedMACAddress'
_A2='avDuplicatedInetAddress'
_A1='avDuplicatedInetAddressType'
_A0='avASGAuthFileRelease'
_z='avASGAuthFileGenTime'
_y='avASGAuthFileGenDate'
_x='avMSSVarbindsDescription'
_w='avMSSNotificationRate'
_v='lsgLicMngLastError'
_u='lsgLicMngCountedValue'
_t='lsgLicMngOperStatus'
_s='lsgLicMngAdminStatus'
_r='lsgLicMngFeatureType'
_q='fipsEnhancedSecurityFlg'
_p='secTcpSynCkiCfgState'
_o='secTcpSynCkiOpState'
_n='secMngProtoStatus'
_m='secMode'
_l='PhysAddress'
_k='OctetString'
_j='avUnauthProtocol'
_i='avUnauthInetAddress'
_h='avUnauthInetAddressType'
_g='avUnauthUserName'
_f='secMngNumOfDays2Expire'
_e='avMSSVarbindsSrcMACAddr'
_d='avMSSVarbindsCount'
_c='avMSSVarbindsDoSType'
_b='avMSSVarbindsIpProtocol'
_a='avMSSVarbindsDstPort'
_Z='avMSSVarbindsDstAddr'
_Y='avMSSVarbindsSrcAddr'
_X='lsgLicMngFeatureKeyword'
_W='secMngProtoId'
_V='read-write'
_U='DisplayString'
_T='genOpLastFailureDisplay'
_S='ifName'
_R='ifIndex'
_Q='genAppFileVersionNumber'
_P='genAppFileName'
_O='genAppFileId'
_N='avEntPhySeverity'
_M='AVAYA-ENTITY-MIB'
_L='IF-MIB'
_K='avASGAuthFileAFID'
_J='Integer32'
_I='cmgTrapSubsystem'
_H='cmgTrapOnBoard'
_G='cmgTrapLocation'
_F='LOAD-MIB'
_E='read-only'
_D='accessible-for-notify'
_C='G700-MG-MIB'
_B='SECURITY-MANAGEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_k,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
avEntPhySeverity,=mibBuilder.importSymbols(_M,_N)
lsg,=mibBuilder.importSymbols('AVAYAGEN-MIB','lsg')
cmgTrapLocation,cmgTrapModule,cmgTrapOnBoard,cmgTrapOnIccMissing,cmgTrapSubsystem=mibBuilder.importSymbols(_C,_G,'cmgTrapModule',_H,'cmgTrapOnIccMissing',_I)
ifIndex,ifName,ifPhysAddress,ifType=mibBuilder.importSymbols(_L,_R,_S,'ifPhysAddress','ifType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
genAppFileId,genAppFileName,genAppFileVersionNumber,genOpLastFailureDisplay=mibBuilder.importSymbols(_F,_O,_P,_Q,_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_U,_l,'TextualConvention')
secMngModule=ModuleIdentity((1,3,6,1,4,1,6889,2,1,14,1))
if mibBuilder.loadTexts:secMngModule.setRevisions(('2006-03-13 18:49','2005-11-23 13:21','2005-01-11 16:54','2005-03-02 16:02','2005-04-20 16:06','2006-02-27 19:16','2010-03-23 10:45'))
class OnOffType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class ServiceStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('notSupported',3)))
_AvayaSecurity_ObjectIdentity=ObjectIdentity
avayaSecurity=_AvayaSecurity_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14))
_SecMode_Type=OnOffType
_SecMode_Object=MibScalar
secMode=_SecMode_Object((1,3,6,1,4,1,6889,2,1,14,1,1),_SecMode_Type())
secMode.setMaxAccess(_E)
if mibBuilder.loadTexts:secMode.setStatus(_A)
_SecTcpSynCookies_ObjectIdentity=ObjectIdentity
secTcpSynCookies=_SecTcpSynCookies_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,2))
_SecTcpSynCkiOpState_Type=OnOffType
_SecTcpSynCkiOpState_Object=MibScalar
secTcpSynCkiOpState=_SecTcpSynCkiOpState_Object((1,3,6,1,4,1,6889,2,1,14,1,2,1),_SecTcpSynCkiOpState_Type())
secTcpSynCkiOpState.setMaxAccess(_E)
if mibBuilder.loadTexts:secTcpSynCkiOpState.setStatus(_A)
_SecTcpSynCkiCfgState_Type=OnOffType
_SecTcpSynCkiCfgState_Object=MibScalar
secTcpSynCkiCfgState=_SecTcpSynCkiCfgState_Object((1,3,6,1,4,1,6889,2,1,14,1,2,2),_SecTcpSynCkiCfgState_Type())
secTcpSynCkiCfgState.setMaxAccess(_V)
if mibBuilder.loadTexts:secTcpSynCkiCfgState.setStatus(_A)
_SecMngProtoTable_Object=MibTable
secMngProtoTable=_SecMngProtoTable_Object((1,3,6,1,4,1,6889,2,1,14,1,3))
if mibBuilder.loadTexts:secMngProtoTable.setStatus(_A)
_SecMngProtoEntry_Object=MibTableRow
secMngProtoEntry=_SecMngProtoEntry_Object((1,3,6,1,4,1,6889,2,1,14,1,3,1))
secMngProtoEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:secMngProtoEntry.setStatus(_A)
class _SecMngProtoId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('scpConfigFiles',1),('scpImageFiles',2),('ssh',3),('telnet',4),('snmpv3',5),('http',6),('https',7),('telnetClient',8),('icmpRedirection',9),('icmp',10),('recoveryPassword',11),('sshClient',12),('snmpv1',13),('icmpEcho',14),('ftpClient',15),('tftp',16),('dhcp',17),('dnsResolver',18),('scpClient',19),('tftpClient',20),('telnetServices',21),('dnsRelay',22),('arpInspection',23)))
_SecMngProtoId_Type.__name__=_J
_SecMngProtoId_Object=MibTableColumn
secMngProtoId=_SecMngProtoId_Object((1,3,6,1,4,1,6889,2,1,14,1,3,1,1),_SecMngProtoId_Type())
secMngProtoId.setMaxAccess(_E)
if mibBuilder.loadTexts:secMngProtoId.setStatus(_A)
_SecMngProtoStatus_Type=ServiceStateType
_SecMngProtoStatus_Object=MibTableColumn
secMngProtoStatus=_SecMngProtoStatus_Object((1,3,6,1,4,1,6889,2,1,14,1,3,1,2),_SecMngProtoStatus_Type())
secMngProtoStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:secMngProtoStatus.setStatus(_A)
_SecMngConformance_ObjectIdentity=ObjectIdentity
secMngConformance=_SecMngConformance_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,4))
_SecMngGroups_ObjectIdentity=ObjectIdentity
secMngGroups=_SecMngGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,4,1))
_SecMngCompliance_ObjectIdentity=ObjectIdentity
secMngCompliance=_SecMngCompliance_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,4,2))
_LsgLicManagement_ObjectIdentity=ObjectIdentity
lsgLicManagement=_LsgLicManagement_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,5))
if mibBuilder.loadTexts:lsgLicManagement.setStatus(_A)
_LsgLicMngTable_Object=MibTable
lsgLicMngTable=_LsgLicMngTable_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1))
if mibBuilder.loadTexts:lsgLicMngTable.setStatus(_A)
_LsgLicMngEntry_Object=MibTableRow
lsgLicMngEntry=_LsgLicMngEntry_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1))
lsgLicMngEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:lsgLicMngEntry.setStatus(_A)
_LsgLicMngFeatureKeyword_Type=OctetString
_LsgLicMngFeatureKeyword_Object=MibTableColumn
lsgLicMngFeatureKeyword=_LsgLicMngFeatureKeyword_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,1),_LsgLicMngFeatureKeyword_Type())
lsgLicMngFeatureKeyword.setMaxAccess('read-create')
if mibBuilder.loadTexts:lsgLicMngFeatureKeyword.setStatus(_A)
class _LsgLicMngFeatureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onOffFeature',1),('quantifiableFeature',2)))
_LsgLicMngFeatureType_Type.__name__=_J
_LsgLicMngFeatureType_Object=MibTableColumn
lsgLicMngFeatureType=_LsgLicMngFeatureType_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,2),_LsgLicMngFeatureType_Type())
lsgLicMngFeatureType.setMaxAccess(_E)
if mibBuilder.loadTexts:lsgLicMngFeatureType.setStatus(_A)
_LsgLicMngAdminStatus_Type=OnOffType
_LsgLicMngAdminStatus_Object=MibTableColumn
lsgLicMngAdminStatus=_LsgLicMngAdminStatus_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,3),_LsgLicMngAdminStatus_Type())
lsgLicMngAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lsgLicMngAdminStatus.setStatus(_A)
_LsgLicMngOperStatus_Type=OnOffType
_LsgLicMngOperStatus_Object=MibTableColumn
lsgLicMngOperStatus=_LsgLicMngOperStatus_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,4),_LsgLicMngOperStatus_Type())
lsgLicMngOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:lsgLicMngOperStatus.setStatus(_A)
_LsgLicMngCountedValue_Type=Unsigned32
_LsgLicMngCountedValue_Object=MibTableColumn
lsgLicMngCountedValue=_LsgLicMngCountedValue_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,5),_LsgLicMngCountedValue_Type())
lsgLicMngCountedValue.setMaxAccess(_E)
if mibBuilder.loadTexts:lsgLicMngCountedValue.setStatus(_A)
class _LsgLicMngLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('licNoError',2))
_LsgLicMngLastError_Type.__name__=_J
_LsgLicMngLastError_Object=MibTableColumn
lsgLicMngLastError=_LsgLicMngLastError_Object((1,3,6,1,4,1,6889,2,1,14,1,5,1,1,6),_LsgLicMngLastError_Type())
lsgLicMngLastError.setMaxAccess(_E)
if mibBuilder.loadTexts:lsgLicMngLastError.setStatus(_A)
_LsgLicMngConformance_ObjectIdentity=ObjectIdentity
lsgLicMngConformance=_LsgLicMngConformance_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,5,20))
if mibBuilder.loadTexts:lsgLicMngConformance.setStatus(_A)
_LsgLicMngGroups_ObjectIdentity=ObjectIdentity
lsgLicMngGroups=_LsgLicMngGroups_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,5,20,1))
if mibBuilder.loadTexts:lsgLicMngGroups.setStatus(_A)
_Fips140_ObjectIdentity=ObjectIdentity
fips140=_Fips140_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,6))
if mibBuilder.loadTexts:fips140.setStatus(_A)
_FipsEnhancedSecurityFlg_Type=OnOffType
_FipsEnhancedSecurityFlg_Object=MibScalar
fipsEnhancedSecurityFlg=_FipsEnhancedSecurityFlg_Object((1,3,6,1,4,1,6889,2,1,14,1,6,1),_FipsEnhancedSecurityFlg_Type())
fipsEnhancedSecurityFlg.setMaxAccess(_E)
if mibBuilder.loadTexts:fipsEnhancedSecurityFlg.setStatus(_A)
_AvMssNotifications_ObjectIdentity=ObjectIdentity
avMssNotifications=_AvMssNotifications_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,7))
if mibBuilder.loadTexts:avMssNotifications.setStatus(_A)
_AvMssNotificationPrefix_ObjectIdentity=ObjectIdentity
avMssNotificationPrefix=_AvMssNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,7,0))
if mibBuilder.loadTexts:avMssNotificationPrefix.setStatus(_A)
class _AvMSSNotificationRate_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,28800))
_AvMSSNotificationRate_Type.__name__=_J
_AvMSSNotificationRate_Object=MibScalar
avMSSNotificationRate=_AvMSSNotificationRate_Object((1,3,6,1,4,1,6889,2,1,14,1,7,2),_AvMSSNotificationRate_Type())
avMSSNotificationRate.setMaxAccess(_V)
if mibBuilder.loadTexts:avMSSNotificationRate.setStatus(_A)
if mibBuilder.loadTexts:avMSSNotificationRate.setUnits('Second')
_AvMSSVarbinds_ObjectIdentity=ObjectIdentity
avMSSVarbinds=_AvMSSVarbinds_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,7,4))
if mibBuilder.loadTexts:avMSSVarbinds.setStatus(_A)
class _AvMSSVarbindsDoSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,100,101,102,103,104,105)));namedValues=NamedValues(*(('avMSSDoSMalformedARPs',1),('avMSSDoSLandAttack',2),('avMSSDoSICMPReflectAttack',3),('avMSSDoSUknownPort',4),('avMSSDoSUrgTCPOption',5),('avMSSDoSMalformedIP',6),('avMSSDoSSynFlood',7),('avMSSDoSSmurfAttack',8),('avMSSDoSFraggleAttack',9),('avMSSDoSMalFragmentIP',10),('avMSSSpoofedIP',11),('avMSSUnknownL4Protocol',12),('avMSSunAuthenticatedAccess',13),('avMSSUserDefinedDoSAttack100',100),('avMSSUserDefinedDoSAttack101',101),('avMSSUserDefinedDoSAttack102',102),('avMSSUserDefinedDoSAttack103',103),('avMSSUserDefinedDoSAttack104',104),('avMSSUserDefinedDoSAttack105',105)))
_AvMSSVarbindsDoSType_Type.__name__=_J
_AvMSSVarbindsDoSType_Object=MibScalar
avMSSVarbindsDoSType=_AvMSSVarbindsDoSType_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,1),_AvMSSVarbindsDoSType_Type())
avMSSVarbindsDoSType.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsDoSType.setStatus(_A)
_AvMSSVarbindsDescription_Type=DisplayString
_AvMSSVarbindsDescription_Object=MibScalar
avMSSVarbindsDescription=_AvMSSVarbindsDescription_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,2),_AvMSSVarbindsDescription_Type())
avMSSVarbindsDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsDescription.setStatus(_A)
_AvMSSVarbindsSrcAddr_Type=IpAddress
_AvMSSVarbindsSrcAddr_Object=MibScalar
avMSSVarbindsSrcAddr=_AvMSSVarbindsSrcAddr_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,3),_AvMSSVarbindsSrcAddr_Type())
avMSSVarbindsSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsSrcAddr.setStatus(_A)
_AvMSSVarbindsDstAddr_Type=IpAddress
_AvMSSVarbindsDstAddr_Object=MibScalar
avMSSVarbindsDstAddr=_AvMSSVarbindsDstAddr_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,4),_AvMSSVarbindsDstAddr_Type())
avMSSVarbindsDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsDstAddr.setStatus(_A)
class _AvMSSVarbindsDstPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvMSSVarbindsDstPort_Type.__name__=_J
_AvMSSVarbindsDstPort_Object=MibScalar
avMSSVarbindsDstPort=_AvMSSVarbindsDstPort_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,5),_AvMSSVarbindsDstPort_Type())
avMSSVarbindsDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsDstPort.setStatus(_A)
class _AvMSSVarbindsIpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvMSSVarbindsIpProtocol_Type.__name__=_J
_AvMSSVarbindsIpProtocol_Object=MibScalar
avMSSVarbindsIpProtocol=_AvMSSVarbindsIpProtocol_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,6),_AvMSSVarbindsIpProtocol_Type())
avMSSVarbindsIpProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsIpProtocol.setStatus(_A)
_AvMSSVarbindsCount_Type=Counter64
_AvMSSVarbindsCount_Object=MibScalar
avMSSVarbindsCount=_AvMSSVarbindsCount_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,7),_AvMSSVarbindsCount_Type())
avMSSVarbindsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsCount.setStatus(_A)
class _AvMSSVarbindsSrcMACAddr_Type(PhysAddress):defaultValue=OctetString('00:00:00:00:00:00')
_AvMSSVarbindsSrcMACAddr_Type.__name__=_l
_AvMSSVarbindsSrcMACAddr_Object=MibScalar
avMSSVarbindsSrcMACAddr=_AvMSSVarbindsSrcMACAddr_Object((1,3,6,1,4,1,6889,2,1,14,1,7,4,8),_AvMSSVarbindsSrcMACAddr_Type())
avMSSVarbindsSrcMACAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:avMSSVarbindsSrcMACAddr.setStatus(_A)
_SecMngNotifications_ObjectIdentity=ObjectIdentity
secMngNotifications=_SecMngNotifications_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,10))
if mibBuilder.loadTexts:secMngNotifications.setStatus(_A)
_SecMngNotificationsPrefix_ObjectIdentity=ObjectIdentity
secMngNotificationsPrefix=_SecMngNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,10,0))
if mibBuilder.loadTexts:secMngNotificationsPrefix.setStatus(_A)
_SecMngVarbinds_ObjectIdentity=ObjectIdentity
secMngVarbinds=_SecMngVarbinds_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,10,1))
if mibBuilder.loadTexts:secMngVarbinds.setStatus(_A)
_SecMngNumOfDays2Expire_Type=Unsigned32
_SecMngNumOfDays2Expire_Object=MibScalar
secMngNumOfDays2Expire=_SecMngNumOfDays2Expire_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,1),_SecMngNumOfDays2Expire_Type())
secMngNumOfDays2Expire.setMaxAccess(_D)
if mibBuilder.loadTexts:secMngNumOfDays2Expire.setStatus(_A)
if mibBuilder.loadTexts:secMngNumOfDays2Expire.setUnits('Days')
class _AvUnauthUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvUnauthUserName_Type.__name__=_k
_AvUnauthUserName_Object=MibScalar
avUnauthUserName=_AvUnauthUserName_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,3),_AvUnauthUserName_Type())
avUnauthUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:avUnauthUserName.setStatus(_A)
class _AvUnauthProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(22,23,80,161,443,500,6889,6890,6891)));namedValues=NamedValues(*(('avSSHAccess',22),('avTELNETAccess',23),('avHTTPAccess',80),('avSNMPAccess',161),('avHTTPSAccess',443),('avIKEAccess',500),('avRASAccess',6889),('avConsoleAccess',6890),('avPPPAccess',6891)))
_AvUnauthProtocol_Type.__name__=_J
_AvUnauthProtocol_Object=MibScalar
avUnauthProtocol=_AvUnauthProtocol_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,5),_AvUnauthProtocol_Type())
avUnauthProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:avUnauthProtocol.setStatus(_A)
_AvUnauthInetAddressType_Type=InetAddressType
_AvUnauthInetAddressType_Object=MibScalar
avUnauthInetAddressType=_AvUnauthInetAddressType_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,9),_AvUnauthInetAddressType_Type())
avUnauthInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:avUnauthInetAddressType.setStatus(_A)
_AvUnauthInetAddress_Type=InetAddress
_AvUnauthInetAddress_Object=MibScalar
avUnauthInetAddress=_AvUnauthInetAddress_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,10),_AvUnauthInetAddress_Type())
avUnauthInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:avUnauthInetAddress.setStatus(_A)
_AvDuplicatedInetAddressType_Type=InetAddressType
_AvDuplicatedInetAddressType_Object=MibScalar
avDuplicatedInetAddressType=_AvDuplicatedInetAddressType_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,11),_AvDuplicatedInetAddressType_Type())
avDuplicatedInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:avDuplicatedInetAddressType.setStatus(_A)
_AvDuplicatedInetAddress_Type=InetAddress
_AvDuplicatedInetAddress_Object=MibScalar
avDuplicatedInetAddress=_AvDuplicatedInetAddress_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,12),_AvDuplicatedInetAddress_Type())
avDuplicatedInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:avDuplicatedInetAddress.setStatus(_A)
_AvDuplicatedMACAddress_Type=PhysAddress
_AvDuplicatedMACAddress_Object=MibScalar
avDuplicatedMACAddress=_AvDuplicatedMACAddress_Object((1,3,6,1,4,1,6889,2,1,14,1,10,1,13),_AvDuplicatedMACAddress_Type())
avDuplicatedMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:avDuplicatedMACAddress.setStatus(_A)
_AvASGAuthenticationFiles_ObjectIdentity=ObjectIdentity
avASGAuthenticationFiles=_AvASGAuthenticationFiles_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,12))
if mibBuilder.loadTexts:avASGAuthenticationFiles.setStatus(_A)
_AvASGAuthFileHeader_ObjectIdentity=ObjectIdentity
avASGAuthFileHeader=_AvASGAuthFileHeader_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,12,3))
if mibBuilder.loadTexts:avASGAuthFileHeader.setStatus(_A)
class _AvASGAuthFileAFID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_AvASGAuthFileAFID_Type.__name__=_U
_AvASGAuthFileAFID_Object=MibScalar
avASGAuthFileAFID=_AvASGAuthFileAFID_Object((1,3,6,1,4,1,6889,2,1,14,1,12,3,1),_AvASGAuthFileAFID_Type())
avASGAuthFileAFID.setMaxAccess(_E)
if mibBuilder.loadTexts:avASGAuthFileAFID.setStatus(_A)
_AvASGAuthFileGenDate_Type=DisplayString
_AvASGAuthFileGenDate_Object=MibScalar
avASGAuthFileGenDate=_AvASGAuthFileGenDate_Object((1,3,6,1,4,1,6889,2,1,14,1,12,3,2),_AvASGAuthFileGenDate_Type())
avASGAuthFileGenDate.setMaxAccess(_E)
if mibBuilder.loadTexts:avASGAuthFileGenDate.setStatus(_A)
if mibBuilder.loadTexts:avASGAuthFileGenDate.setUnits('YYYY/MM/DD')
class _AvASGAuthFileGenTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_AvASGAuthFileGenTime_Type.__name__=_U
_AvASGAuthFileGenTime_Object=MibScalar
avASGAuthFileGenTime=_AvASGAuthFileGenTime_Object((1,3,6,1,4,1,6889,2,1,14,1,12,3,3),_AvASGAuthFileGenTime_Type())
avASGAuthFileGenTime.setMaxAccess(_E)
if mibBuilder.loadTexts:avASGAuthFileGenTime.setStatus(_A)
if mibBuilder.loadTexts:avASGAuthFileGenTime.setUnits('HH:MM:SS')
_AvASGAuthFileRelease_Type=DisplayString
_AvASGAuthFileRelease_Object=MibScalar
avASGAuthFileRelease=_AvASGAuthFileRelease_Object((1,3,6,1,4,1,6889,2,1,14,1,12,3,4),_AvASGAuthFileRelease_Type())
avASGAuthFileRelease.setMaxAccess(_E)
if mibBuilder.loadTexts:avASGAuthFileRelease.setStatus(_A)
_AvASGNotifications_ObjectIdentity=ObjectIdentity
avASGNotifications=_AvASGNotifications_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,12,3,5))
if mibBuilder.loadTexts:avASGNotifications.setStatus(_A)
_AvASGNotificationsPrefix_ObjectIdentity=ObjectIdentity
avASGNotificationsPrefix=_AvASGNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6889,2,1,14,1,12,3,5,0))
if mibBuilder.loadTexts:avASGNotificationsPrefix.setStatus(_A)
_AvSecLocalDateAndTime_Type=DateAndTime
_AvSecLocalDateAndTime_Object=MibScalar
avSecLocalDateAndTime=_AvSecLocalDateAndTime_Object((1,3,6,1,4,1,6889,2,1,14,1,13),_AvSecLocalDateAndTime_Type())
avSecLocalDateAndTime.setMaxAccess(_V)
if mibBuilder.loadTexts:avSecLocalDateAndTime.setStatus(_A)
secMngBasicGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,14,1,4,1,1))
secMngBasicGroup.setObjects(*((_B,_m),(_B,_W),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:secMngBasicGroup.setStatus(_A)
lsgLicMngBasicGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,14,1,5,20,1,1))
lsgLicMngBasicGroup.setObjects(*((_B,_X),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:lsgLicMngBasicGroup.setStatus(_A)
avMSSgroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,14,1,8))
avMSSgroup.setObjects(*((_B,_w),(_B,_Y),(_B,_Z),(_B,_a),(_B,_x),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:avMSSgroup.setStatus(_A)
avMngNotificationCompliance=ObjectGroup((1,3,6,1,4,1,6889,2,1,14,1,10,2))
avMngNotificationCompliance.setObjects((_B,_f))
if mibBuilder.loadTexts:avMngNotificationCompliance.setStatus(_A)
avASGAuthFileGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,14,1,12,1000))
avASGAuthFileGroup.setObjects(*((_B,_K),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:avASGAuthFileGroup.setStatus(_A)
avMSSDenialOfService=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,7,0,1))
avMSSDenialOfService.setObjects(*((_B,_c),(_B,_Y),(_B,_Z),(_B,_a),(_B,_d),(_B,_b),(_L,_R),(_L,_S),(_B,_e)))
if mibBuilder.loadTexts:avMSSDenialOfService.setStatus(_A)
avConfigurationEncKeyMismatchFault=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,1))
avConfigurationEncKeyMismatchFault.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_F,_O),(_F,_P),(_F,_Q),(_F,_T)))
if mibBuilder.loadTexts:avConfigurationEncKeyMismatchFault.setStatus(_A)
avConfigurationMasterKeyChange=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,2))
avConfigurationMasterKeyChange.setObjects(*((_C,_I),(_C,_H),(_C,_G)))
if mibBuilder.loadTexts:avConfigurationMasterKeyChange.setStatus(_A)
avPasswordToExpireAlert=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,3))
avPasswordToExpireAlert.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_B,_f)))
if mibBuilder.loadTexts:avPasswordToExpireAlert.setStatus(_A)
avUnAuthAccessEvent=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,200))
avUnAuthAccessEvent.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_K),(_M,_N)))
if mibBuilder.loadTexts:avUnAuthAccessEvent.setStatus(_A)
avAccountLockoutEvent=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,201))
avAccountLockoutEvent.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_K),(_M,_N)))
if mibBuilder.loadTexts:avAccountLockoutEvent.setStatus(_A)
avIPv6AddressDuplicationEvent=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,10,0,202))
avIPv6AddressDuplicationEvent.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_B,_A1),(_B,_A2),(_B,_A3),(_L,_R),(_L,_S),(_B,_K),(_M,_N)))
if mibBuilder.loadTexts:avIPv6AddressDuplicationEvent.setStatus(_A)
avASGAFDownloadSuccess=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,12,3,5,0,1))
avASGAFDownloadSuccess.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_F,_O),(_F,_P),(_F,_Q),(_B,_K)))
if mibBuilder.loadTexts:avASGAFDownloadSuccess.setStatus(_A)
avASGAFDownloadFailure=NotificationType((1,3,6,1,4,1,6889,2,1,14,1,12,3,5,0,2))
avASGAFDownloadFailure.setObjects(*((_C,_I),(_C,_H),(_C,_G),(_F,_O),(_F,_P),(_F,_Q),(_F,_T),(_B,_K)))
if mibBuilder.loadTexts:avASGAFDownloadFailure.setStatus(_A)
mssNotificationGroup=NotificationGroup((1,3,6,1,4,1,6889,2,1,14,1,9))
mssNotificationGroup.setObjects((_B,_A4))
if mibBuilder.loadTexts:mssNotificationGroup.setStatus(_A)
secMngNotificationGroup=NotificationGroup((1,3,6,1,4,1,6889,2,1,14,1,11))
secMngNotificationGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:secMngNotificationGroup.setStatus(_A)
avASGAuthFileNotificationGroup=NotificationGroup((1,3,6,1,4,1,6889,2,1,14,1,12,1001))
avASGAuthFileNotificationGroup.setObjects(*((_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:avASGAuthFileNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OnOffType':OnOffType,'ServiceStateType':ServiceStateType,'avayaSecurity':avayaSecurity,'secMngModule':secMngModule,_m:secMode,'secTcpSynCookies':secTcpSynCookies,_o:secTcpSynCkiOpState,_p:secTcpSynCkiCfgState,'secMngProtoTable':secMngProtoTable,'secMngProtoEntry':secMngProtoEntry,_W:secMngProtoId,_n:secMngProtoStatus,'secMngConformance':secMngConformance,'secMngGroups':secMngGroups,'secMngBasicGroup':secMngBasicGroup,'secMngCompliance':secMngCompliance,'lsgLicManagement':lsgLicManagement,'lsgLicMngTable':lsgLicMngTable,'lsgLicMngEntry':lsgLicMngEntry,_X:lsgLicMngFeatureKeyword,_r:lsgLicMngFeatureType,_s:lsgLicMngAdminStatus,_t:lsgLicMngOperStatus,_u:lsgLicMngCountedValue,_v:lsgLicMngLastError,'lsgLicMngConformance':lsgLicMngConformance,'lsgLicMngGroups':lsgLicMngGroups,'lsgLicMngBasicGroup':lsgLicMngBasicGroup,'fips140':fips140,_q:fipsEnhancedSecurityFlg,'avMssNotifications':avMssNotifications,'avMssNotificationPrefix':avMssNotificationPrefix,_A4:avMSSDenialOfService,_w:avMSSNotificationRate,'avMSSVarbinds':avMSSVarbinds,_c:avMSSVarbindsDoSType,_x:avMSSVarbindsDescription,_Y:avMSSVarbindsSrcAddr,_Z:avMSSVarbindsDstAddr,_a:avMSSVarbindsDstPort,_b:avMSSVarbindsIpProtocol,_d:avMSSVarbindsCount,_e:avMSSVarbindsSrcMACAddr,'avMSSgroup':avMSSgroup,'mssNotificationGroup':mssNotificationGroup,'secMngNotifications':secMngNotifications,'secMngNotificationsPrefix':secMngNotificationsPrefix,_A5:avConfigurationEncKeyMismatchFault,_A6:avConfigurationMasterKeyChange,'avPasswordToExpireAlert':avPasswordToExpireAlert,'avUnAuthAccessEvent':avUnAuthAccessEvent,'avAccountLockoutEvent':avAccountLockoutEvent,'avIPv6AddressDuplicationEvent':avIPv6AddressDuplicationEvent,'secMngVarbinds':secMngVarbinds,_f:secMngNumOfDays2Expire,_g:avUnauthUserName,_j:avUnauthProtocol,_h:avUnauthInetAddressType,_i:avUnauthInetAddress,_A1:avDuplicatedInetAddressType,_A2:avDuplicatedInetAddress,_A3:avDuplicatedMACAddress,'avMngNotificationCompliance':avMngNotificationCompliance,'secMngNotificationGroup':secMngNotificationGroup,'avASGAuthenticationFiles':avASGAuthenticationFiles,'avASGAuthFileHeader':avASGAuthFileHeader,_K:avASGAuthFileAFID,_y:avASGAuthFileGenDate,_z:avASGAuthFileGenTime,_A0:avASGAuthFileRelease,'avASGNotifications':avASGNotifications,'avASGNotificationsPrefix':avASGNotificationsPrefix,_A8:avASGAFDownloadSuccess,_A7:avASGAFDownloadFailure,'avASGAuthFileGroup':avASGAuthFileGroup,'avASGAuthFileNotificationGroup':avASGAuthFileNotificationGroup,'avSecLocalDateAndTime':avSecLocalDateAndTime})