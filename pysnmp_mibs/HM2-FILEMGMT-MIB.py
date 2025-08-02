_a='hm2FMEnvmState'
_Z='server'
_Y='system'
_X='runningConfig'
_W='hm2FMActionDestinationType'
_V='hm2FMActionSourceType'
_U='hm2FMActionItemType'
_T='hm2FMActionType'
_S='hm2FMProfileIndex'
_R='hm2FMProfileStorageType'
_Q='TruthValue'
_P='hm2FMNvmState'
_O='outOfSync'
_N='envm'
_M='nvm'
_L='InterfaceIndexOrZero'
_K='HmEnabledStatus'
_J='none'
_I='not-accessible'
_H='SnmpAdminString'
_G='ok'
_F='DisplayString'
_E='HM2-FILEMGMT-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,HmTimeSeconds1970,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_K,'HmTimeSeconds1970','hm2ConfigurationMibs')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_L)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention',_Q)
hm2FileMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,21))
if mibBuilder.loadTexts:hm2FileMgmtMib.setRevisions(('2017-01-31 00:00',))
_Hm2FileMgmtNotifications_ObjectIdentity=ObjectIdentity
hm2FileMgmtNotifications=_Hm2FileMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,21,0))
_Hm2FileMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2FileMgmtMibObjects=_Hm2FileMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,21,1))
_Hm2FileMgmtProfileGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtProfileGroup=_Hm2FileMgmtProfileGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,1))
_Hm2FMProfileTable_Object=MibTable
hm2FMProfileTable=_Hm2FMProfileTable_Object((1,3,6,1,4,1,248,11,21,1,1,1))
if mibBuilder.loadTexts:hm2FMProfileTable.setStatus(_A)
_Hm2FMProfileEntry_Object=MibTableRow
hm2FMProfileEntry=_Hm2FMProfileEntry_Object((1,3,6,1,4,1,248,11,21,1,1,1,1))
hm2FMProfileEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:hm2FMProfileEntry.setStatus(_A)
class _Hm2FMProfileStorageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_Hm2FMProfileStorageType_Type.__name__=_C
_Hm2FMProfileStorageType_Object=MibTableColumn
hm2FMProfileStorageType=_Hm2FMProfileStorageType_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,1),_Hm2FMProfileStorageType_Type())
hm2FMProfileStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileStorageType.setStatus(_A)
class _Hm2FMProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Hm2FMProfileIndex_Type.__name__=_C
_Hm2FMProfileIndex_Object=MibTableColumn
hm2FMProfileIndex=_Hm2FMProfileIndex_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,2),_Hm2FMProfileIndex_Type())
hm2FMProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileIndex.setStatus(_A)
class _Hm2FMProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2FMProfileName_Type.__name__=_F
_Hm2FMProfileName_Object=MibTableColumn
hm2FMProfileName=_Hm2FMProfileName_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,3),_Hm2FMProfileName_Type())
hm2FMProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileName.setStatus(_A)
_Hm2FMProfileDateTime_Type=HmTimeSeconds1970
_Hm2FMProfileDateTime_Object=MibTableColumn
hm2FMProfileDateTime=_Hm2FMProfileDateTime_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,4),_Hm2FMProfileDateTime_Type())
hm2FMProfileDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileDateTime.setStatus(_A)
class _Hm2FMProfileActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_Hm2FMProfileActive_Type.__name__=_C
_Hm2FMProfileActive_Object=MibTableColumn
hm2FMProfileActive=_Hm2FMProfileActive_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,5),_Hm2FMProfileActive_Type())
hm2FMProfileActive.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMProfileActive.setStatus(_A)
class _Hm2FMProfileAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('delete',2)))
_Hm2FMProfileAction_Type.__name__=_C
_Hm2FMProfileAction_Object=MibTableColumn
hm2FMProfileAction=_Hm2FMProfileAction_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,6),_Hm2FMProfileAction_Type())
hm2FMProfileAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMProfileAction.setStatus(_A)
_Hm2FMProfileDeviceType_Type=ObjectIdentifier
_Hm2FMProfileDeviceType_Object=MibTableColumn
hm2FMProfileDeviceType=_Hm2FMProfileDeviceType_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,7),_Hm2FMProfileDeviceType_Type())
hm2FMProfileDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileDeviceType.setStatus(_A)
_Hm2FMProfileEncryptionActive_Type=TruthValue
_Hm2FMProfileEncryptionActive_Object=MibTableColumn
hm2FMProfileEncryptionActive=_Hm2FMProfileEncryptionActive_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,8),_Hm2FMProfileEncryptionActive_Type())
hm2FMProfileEncryptionActive.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileEncryptionActive.setStatus(_A)
_Hm2FMProfileEncryptionVerified_Type=TruthValue
_Hm2FMProfileEncryptionVerified_Object=MibTableColumn
hm2FMProfileEncryptionVerified=_Hm2FMProfileEncryptionVerified_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,9),_Hm2FMProfileEncryptionVerified_Type())
hm2FMProfileEncryptionVerified.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileEncryptionVerified.setStatus(_A)
_Hm2FMProfileSwMajorRelNum_Type=Integer32
_Hm2FMProfileSwMajorRelNum_Object=MibTableColumn
hm2FMProfileSwMajorRelNum=_Hm2FMProfileSwMajorRelNum_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,10),_Hm2FMProfileSwMajorRelNum_Type())
hm2FMProfileSwMajorRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileSwMajorRelNum.setStatus(_A)
_Hm2FMProfileSwMinorRelNum_Type=Integer32
_Hm2FMProfileSwMinorRelNum_Object=MibTableColumn
hm2FMProfileSwMinorRelNum=_Hm2FMProfileSwMinorRelNum_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,11),_Hm2FMProfileSwMinorRelNum_Type())
hm2FMProfileSwMinorRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileSwMinorRelNum.setStatus(_A)
_Hm2FMProfileSwBugfixRelNum_Type=Integer32
_Hm2FMProfileSwBugfixRelNum_Object=MibTableColumn
hm2FMProfileSwBugfixRelNum=_Hm2FMProfileSwBugfixRelNum_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,12),_Hm2FMProfileSwBugfixRelNum_Type())
hm2FMProfileSwBugfixRelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileSwBugfixRelNum.setStatus(_A)
class _Hm2FMProfileFingerprint_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_Hm2FMProfileFingerprint_Type.__name__=_F
_Hm2FMProfileFingerprint_Object=MibTableColumn
hm2FMProfileFingerprint=_Hm2FMProfileFingerprint_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,13),_Hm2FMProfileFingerprint_Type())
hm2FMProfileFingerprint.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileFingerprint.setStatus(_A)
_Hm2FMProfileFingerprintVerified_Type=TruthValue
_Hm2FMProfileFingerprintVerified_Object=MibTableColumn
hm2FMProfileFingerprintVerified=_Hm2FMProfileFingerprintVerified_Object((1,3,6,1,4,1,248,11,21,1,1,1,1,14),_Hm2FMProfileFingerprintVerified_Type())
hm2FMProfileFingerprintVerified.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMProfileFingerprintVerified.setStatus(_A)
_Hm2FileMgmtActionGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtActionGroup=_Hm2FileMgmtActionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,2))
_Hm2FMActionTable_Object=MibTable
hm2FMActionTable=_Hm2FMActionTable_Object((1,3,6,1,4,1,248,11,21,1,2,1))
if mibBuilder.loadTexts:hm2FMActionTable.setStatus(_A)
_Hm2FMActionEntry_Object=MibTableRow
hm2FMActionEntry=_Hm2FMActionEntry_Object((1,3,6,1,4,1,248,11,21,1,2,1,1))
hm2FMActionEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:hm2FMActionEntry.setStatus(_A)
class _Hm2FMActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nop',1),('copy',2),('clear',3),('swap',4)))
_Hm2FMActionType_Type.__name__=_C
_Hm2FMActionType_Object=MibTableColumn
hm2FMActionType=_Hm2FMActionType_Object((1,3,6,1,4,1,248,11,21,1,2,1,1,1),_Hm2FMActionType_Type())
hm2FMActionType.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2FMActionType.setStatus(_A)
class _Hm2FMActionItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,15,20,30,31,40,41,42,50,51,52,53,60,65,70,71,80,81,82,83,84,90,100)));namedValues=NamedValues(*((_J,1),('config',10),('filesystem',15),('script',20),('firmware',30),('bootcode',31),('eventlog',40),('audittrail',41),('traplog',42),('sysinfo',50),('sfpWhiteList',51),('cliBanner',52),('sysinfoall',53),('sshkey',60),('httpsServerCert',65),('tcpdumpcap',70),('tcpdumpfilter',71),('camcert',80),('ldapCacert',81),('mailCacert',82),('syslogCacert',83),('camcertPEM',84),('edsFile',90),('gsdmlFile',100)))
_Hm2FMActionItemType_Type.__name__=_C
_Hm2FMActionItemType_Object=MibTableColumn
hm2FMActionItemType=_Hm2FMActionItemType_Object((1,3,6,1,4,1,248,11,21,1,2,1,1,2),_Hm2FMActionItemType_Type())
hm2FMActionItemType.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2FMActionItemType.setStatus(_A)
class _Hm2FMActionSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6,7,10,11,20)));namedValues=NamedValues(*((_J,1),(_M,2),(_N,3),('buffered',6),('persistent',7),(_X,10),(_Y,11),(_Z,20)))
_Hm2FMActionSourceType_Type.__name__=_C
_Hm2FMActionSourceType_Object=MibTableColumn
hm2FMActionSourceType=_Hm2FMActionSourceType_Object((1,3,6,1,4,1,248,11,21,1,2,1,1,3),_Hm2FMActionSourceType_Type())
hm2FMActionSourceType.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2FMActionSourceType.setStatus(_A)
class _Hm2FMActionDestinationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,10,11,20)));namedValues=NamedValues(*((_J,1),(_M,2),(_N,3),(_X,10),(_Y,11),(_Z,20)))
_Hm2FMActionDestinationType_Type.__name__=_C
_Hm2FMActionDestinationType_Object=MibTableColumn
hm2FMActionDestinationType=_Hm2FMActionDestinationType_Object((1,3,6,1,4,1,248,11,21,1,2,1,1,4),_Hm2FMActionDestinationType_Type())
hm2FMActionDestinationType.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2FMActionDestinationType.setStatus(_A)
_Hm2FMActionActivate_Type=Integer32
_Hm2FMActionActivate_Object=MibTableColumn
hm2FMActionActivate=_Hm2FMActionActivate_Object((1,3,6,1,4,1,248,11,21,1,2,1,1,5),_Hm2FMActionActivate_Type())
hm2FMActionActivate.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionActivate.setStatus(_A)
class _Hm2FMActionSourceData_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2FMActionSourceData_Type.__name__=_F
_Hm2FMActionSourceData_Object=MibScalar
hm2FMActionSourceData=_Hm2FMActionSourceData_Object((1,3,6,1,4,1,248,11,21,1,2,10),_Hm2FMActionSourceData_Type())
hm2FMActionSourceData.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionSourceData.setStatus(_A)
class _Hm2FMActionDestinationData_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2FMActionDestinationData_Type.__name__=_F
_Hm2FMActionDestinationData_Object=MibScalar
hm2FMActionDestinationData=_Hm2FMActionDestinationData_Object((1,3,6,1,4,1,248,11,21,1,2,11),_Hm2FMActionDestinationData_Type())
hm2FMActionDestinationData.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionDestinationData.setStatus(_A)
class _Hm2FMActionActivateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('paramError',2),('busy',3)))
_Hm2FMActionActivateResult_Type.__name__=_C
_Hm2FMActionActivateResult_Object=MibScalar
hm2FMActionActivateResult=_Hm2FMActionActivateResult_Object((1,3,6,1,4,1,248,11,21,1,2,12),_Hm2FMActionActivateResult_Type())
hm2FMActionActivateResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionActivateResult.setStatus(_A)
_Hm2FMActionActivateResultText_Type=DisplayString
_Hm2FMActionActivateResultText_Object=MibScalar
hm2FMActionActivateResultText=_Hm2FMActionActivateResultText_Object((1,3,6,1,4,1,248,11,21,1,2,13),_Hm2FMActionActivateResultText_Type())
hm2FMActionActivateResultText.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionActivateResultText.setStatus(_A)
class _Hm2FMActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('running',2)))
_Hm2FMActionStatus_Type.__name__=_C
_Hm2FMActionStatus_Object=MibScalar
hm2FMActionStatus=_Hm2FMActionStatus_Object((1,3,6,1,4,1,248,11,21,1,2,14),_Hm2FMActionStatus_Type())
hm2FMActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionStatus.setStatus(_A)
class _Hm2FMActionPercentReady_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Hm2FMActionPercentReady_Type.__name__=_C
_Hm2FMActionPercentReady_Object=MibScalar
hm2FMActionPercentReady=_Hm2FMActionPercentReady_Object((1,3,6,1,4,1,248,11,21,1,2,15),_Hm2FMActionPercentReady_Type())
hm2FMActionPercentReady.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionPercentReady.setStatus(_A)
class _Hm2FMActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('error',2)))
_Hm2FMActionResult_Type.__name__=_C
_Hm2FMActionResult_Object=MibScalar
hm2FMActionResult=_Hm2FMActionResult_Object((1,3,6,1,4,1,248,11,21,1,2,16),_Hm2FMActionResult_Type())
hm2FMActionResult.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionResult.setStatus(_A)
_Hm2FMActionResultText_Type=DisplayString
_Hm2FMActionResultText_Object=MibScalar
hm2FMActionResultText=_Hm2FMActionResultText_Object((1,3,6,1,4,1,248,11,21,1,2,17),_Hm2FMActionResultText_Type())
hm2FMActionResultText.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionResultText.setStatus(_A)
_Hm2FMActionActivateKey_Type=Integer32
_Hm2FMActionActivateKey_Object=MibScalar
hm2FMActionActivateKey=_Hm2FMActionActivateKey_Object((1,3,6,1,4,1,248,11,21,1,2,18),_Hm2FMActionActivateKey_Type())
hm2FMActionActivateKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMActionActivateKey.setStatus(_A)
class _Hm2FMActionContainerPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2FMActionContainerPassword_Type.__name__=_F
_Hm2FMActionContainerPassword_Object=MibScalar
hm2FMActionContainerPassword=_Hm2FMActionContainerPassword_Object((1,3,6,1,4,1,248,11,21,1,2,19),_Hm2FMActionContainerPassword_Type())
hm2FMActionContainerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionContainerPassword.setStatus(_A)
class _Hm2FMActionParameter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,11)));namedValues=NamedValues(*((_J,1),('all',2),('keep-ip',11)))
_Hm2FMActionParameter_Type.__name__=_C
_Hm2FMActionParameter_Object=MibScalar
hm2FMActionParameter=_Hm2FMActionParameter_Object((1,3,6,1,4,1,248,11,21,1,2,20),_Hm2FMActionParameter_Type())
hm2FMActionParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionParameter.setStatus(_A)
class _Hm2FMActionSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2FMActionSourceInterface_Type.__name__=_L
_Hm2FMActionSourceInterface_Object=MibScalar
hm2FMActionSourceInterface=_Hm2FMActionSourceInterface_Object((1,3,6,1,4,1,248,11,21,1,2,21),_Hm2FMActionSourceInterface_Type())
hm2FMActionSourceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMActionSourceInterface.setStatus(_A)
_Hm2FileMgmtStatusGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtStatusGroup=_Hm2FileMgmtStatusGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,3))
class _Hm2FMNvmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_O,2),('busy',3)))
_Hm2FMNvmState_Type.__name__=_C
_Hm2FMNvmState_Object=MibScalar
hm2FMNvmState=_Hm2FMNvmState_Object((1,3,6,1,4,1,248,11,21,1,3,1),_Hm2FMNvmState_Type())
hm2FMNvmState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMNvmState.setStatus(_A)
class _Hm2FMEnvmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_O,2),('absent',3)))
_Hm2FMEnvmState_Type.__name__=_C
_Hm2FMEnvmState_Object=MibScalar
hm2FMEnvmState=_Hm2FMEnvmState_Object((1,3,6,1,4,1,248,11,21,1,3,2),_Hm2FMEnvmState_Type())
hm2FMEnvmState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMEnvmState.setStatus(_A)
class _Hm2FMBootParamState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_O,2)))
_Hm2FMBootParamState_Type.__name__=_C
_Hm2FMBootParamState_Object=MibScalar
hm2FMBootParamState=_Hm2FMBootParamState_Object((1,3,6,1,4,1,248,11,21,1,3,3),_Hm2FMBootParamState_Type())
hm2FMBootParamState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FMBootParamState.setStatus(_A)
_Hm2FileMgmtConfigGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtConfigGroup=_Hm2FileMgmtConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,4))
_Hm2FileMgmtConfigWatchdogControl_ObjectIdentity=ObjectIdentity
hm2FileMgmtConfigWatchdogControl=_Hm2FileMgmtConfigWatchdogControl_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,4,1))
class _Hm2ConfigWatchdogAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2ConfigWatchdogAdminStatus_Type.__name__=_K
_Hm2ConfigWatchdogAdminStatus_Object=MibScalar
hm2ConfigWatchdogAdminStatus=_Hm2ConfigWatchdogAdminStatus_Object((1,3,6,1,4,1,248,11,21,1,4,1,1),_Hm2ConfigWatchdogAdminStatus_Type())
hm2ConfigWatchdogAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ConfigWatchdogAdminStatus.setStatus(_A)
_Hm2ConfigWatchdogOperStatus_Type=HmEnabledStatus
_Hm2ConfigWatchdogOperStatus_Object=MibScalar
hm2ConfigWatchdogOperStatus=_Hm2ConfigWatchdogOperStatus_Object((1,3,6,1,4,1,248,11,21,1,4,1,2),_Hm2ConfigWatchdogOperStatus_Type())
hm2ConfigWatchdogOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ConfigWatchdogOperStatus.setStatus(_A)
class _Hm2ConfigWatchdogTimeInterval_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_Hm2ConfigWatchdogTimeInterval_Type.__name__=_C
_Hm2ConfigWatchdogTimeInterval_Object=MibScalar
hm2ConfigWatchdogTimeInterval=_Hm2ConfigWatchdogTimeInterval_Object((1,3,6,1,4,1,248,11,21,1,4,1,3),_Hm2ConfigWatchdogTimeInterval_Type())
hm2ConfigWatchdogTimeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2ConfigWatchdogTimeInterval.setStatus(_A)
_Hm2ConfigWatchdogTimerValue_Type=Integer32
_Hm2ConfigWatchdogTimerValue_Object=MibScalar
hm2ConfigWatchdogTimerValue=_Hm2ConfigWatchdogTimerValue_Object((1,3,6,1,4,1,248,11,21,1,4,1,4),_Hm2ConfigWatchdogTimerValue_Type())
hm2ConfigWatchdogTimerValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ConfigWatchdogTimerValue.setStatus(_A)
_Hm2ConfigWatchdogIPAddressType_Type=InetAddressType
_Hm2ConfigWatchdogIPAddressType_Object=MibScalar
hm2ConfigWatchdogIPAddressType=_Hm2ConfigWatchdogIPAddressType_Object((1,3,6,1,4,1,248,11,21,1,4,1,5),_Hm2ConfigWatchdogIPAddressType_Type())
hm2ConfigWatchdogIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ConfigWatchdogIPAddressType.setStatus(_A)
_Hm2ConfigWatchdogIPAddress_Type=InetAddress
_Hm2ConfigWatchdogIPAddress_Object=MibScalar
hm2ConfigWatchdogIPAddress=_Hm2ConfigWatchdogIPAddress_Object((1,3,6,1,4,1,248,11,21,1,4,1,6),_Hm2ConfigWatchdogIPAddress_Type())
hm2ConfigWatchdogIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2ConfigWatchdogIPAddress.setStatus(_A)
_Hm2FileMgmtServerAccessGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtServerAccessGroup=_Hm2FileMgmtServerAccessGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,4,2))
class _Hm2FMServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2FMServerUserName_Type.__name__=_F
_Hm2FMServerUserName_Object=MibScalar
hm2FMServerUserName=_Hm2FMServerUserName_Object((1,3,6,1,4,1,248,11,21,1,4,2,1),_Hm2FMServerUserName_Type())
hm2FMServerUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMServerUserName.setStatus(_A)
class _Hm2FMServerPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hm2FMServerPassword_Type.__name__=_F
_Hm2FMServerPassword_Object=MibScalar
hm2FMServerPassword=_Hm2FMServerPassword_Object((1,3,6,1,4,1,248,11,21,1,4,2,2),_Hm2FMServerPassword_Type())
hm2FMServerPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMServerPassword.setStatus(_A)
_Hm2FileMgmtSecurityGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtSecurityGroup=_Hm2FileMgmtSecurityGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,4,4))
class _Hm2FileMgmtConfigPasswordStatus_Type(TruthValue):defaultValue=2
_Hm2FileMgmtConfigPasswordStatus_Type.__name__=_Q
_Hm2FileMgmtConfigPasswordStatus_Object=MibScalar
hm2FileMgmtConfigPasswordStatus=_Hm2FileMgmtConfigPasswordStatus_Object((1,3,6,1,4,1,248,11,21,1,4,4,1),_Hm2FileMgmtConfigPasswordStatus_Type())
hm2FileMgmtConfigPasswordStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2FileMgmtConfigPasswordStatus.setStatus(_A)
class _Hm2FileMgmtConfigPasswordChange_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hm2FileMgmtConfigPasswordChange_Type.__name__=_F
_Hm2FileMgmtConfigPasswordChange_Object=MibScalar
hm2FileMgmtConfigPasswordChange=_Hm2FileMgmtConfigPasswordChange_Object((1,3,6,1,4,1,248,11,21,1,4,4,2),_Hm2FileMgmtConfigPasswordChange_Type())
hm2FileMgmtConfigPasswordChange.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FileMgmtConfigPasswordChange.setStatus(_A)
_Hm2FileMgmtConfigRemoteSaveGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtConfigRemoteSaveGroup=_Hm2FileMgmtConfigRemoteSaveGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,1,4,5))
class _Hm2FMConfigRemoteSaveAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2FMConfigRemoteSaveAdminStatus_Type.__name__=_K
_Hm2FMConfigRemoteSaveAdminStatus_Object=MibScalar
hm2FMConfigRemoteSaveAdminStatus=_Hm2FMConfigRemoteSaveAdminStatus_Object((1,3,6,1,4,1,248,11,21,1,4,5,1),_Hm2FMConfigRemoteSaveAdminStatus_Type())
hm2FMConfigRemoteSaveAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMConfigRemoteSaveAdminStatus.setStatus(_A)
class _Hm2FMConfigRemoteSaveDestination_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2FMConfigRemoteSaveDestination_Type.__name__=_H
_Hm2FMConfigRemoteSaveDestination_Object=MibScalar
hm2FMConfigRemoteSaveDestination=_Hm2FMConfigRemoteSaveDestination_Object((1,3,6,1,4,1,248,11,21,1,4,5,2),_Hm2FMConfigRemoteSaveDestination_Type())
hm2FMConfigRemoteSaveDestination.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMConfigRemoteSaveDestination.setStatus(_A)
class _Hm2FMConfigRemoteSaveUsername_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2FMConfigRemoteSaveUsername_Type.__name__=_H
_Hm2FMConfigRemoteSaveUsername_Object=MibScalar
hm2FMConfigRemoteSaveUsername=_Hm2FMConfigRemoteSaveUsername_Object((1,3,6,1,4,1,248,11,21,1,4,5,3),_Hm2FMConfigRemoteSaveUsername_Type())
hm2FMConfigRemoteSaveUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMConfigRemoteSaveUsername.setStatus(_A)
class _Hm2FMConfigRemoteSavePassword_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Hm2FMConfigRemoteSavePassword_Type.__name__=_H
_Hm2FMConfigRemoteSavePassword_Object=MibScalar
hm2FMConfigRemoteSavePassword=_Hm2FMConfigRemoteSavePassword_Object((1,3,6,1,4,1,248,11,21,1,4,5,4),_Hm2FMConfigRemoteSavePassword_Type())
hm2FMConfigRemoteSavePassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FMConfigRemoteSavePassword.setStatus(_A)
class _Hm2FileMgmtGlobalSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2FileMgmtGlobalSourceInterface_Type.__name__=_L
_Hm2FileMgmtGlobalSourceInterface_Object=MibScalar
hm2FileMgmtGlobalSourceInterface=_Hm2FileMgmtGlobalSourceInterface_Object((1,3,6,1,4,1,248,11,21,1,4,9),_Hm2FileMgmtGlobalSourceInterface_Type())
hm2FileMgmtGlobalSourceInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FileMgmtGlobalSourceInterface.setStatus(_A)
class _Hm2FileMgmtConfigCompatibilityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('hiosV1V2',2)))
_Hm2FileMgmtConfigCompatibilityMode_Type.__name__=_C
_Hm2FileMgmtConfigCompatibilityMode_Object=MibScalar
hm2FileMgmtConfigCompatibilityMode=_Hm2FileMgmtConfigCompatibilityMode_Object((1,3,6,1,4,1,248,11,21,1,4,10),_Hm2FileMgmtConfigCompatibilityMode_Type())
hm2FileMgmtConfigCompatibilityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2FileMgmtConfigCompatibilityMode.setStatus(_A)
_Hm2FileMgmtSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2FileMgmtSNMPExtensionGroup=_Hm2FileMgmtSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,21,3))
_Hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn=_Hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,1))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn.setStatus(_A)
_Hm2FileMgmtSESCfgActivateErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgActivateErrorReturn=_Hm2FileMgmtSESCfgActivateErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,2))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgActivateErrorReturn.setStatus(_A)
_Hm2FileMgmtSESCfgActivateIncomlpeteReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgActivateIncomlpeteReturn=_Hm2FileMgmtSESCfgActivateIncomlpeteReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,3))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgActivateIncomlpeteReturn.setStatus(_A)
_Hm2FileMgmtSESCfgMgrCopyCommandErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgMgrCopyCommandErrorReturn=_Hm2FileMgmtSESCfgMgrCopyCommandErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,4))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgMgrCopyCommandErrorReturn.setStatus(_A)
_Hm2FileMgmtSESCfgMgrClearCommandErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgMgrClearCommandErrorReturn=_Hm2FileMgmtSESCfgMgrClearCommandErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,5))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgMgrClearCommandErrorReturn.setStatus(_A)
_Hm2FileMgmtSESCfgMgrSwapCommandErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgMgrSwapCommandErrorReturn=_Hm2FileMgmtSESCfgMgrSwapCommandErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,6))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgMgrSwapCommandErrorReturn.setStatus(_A)
_Hm2FileMgmtSESCfgErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgErrorReturn=_Hm2FileMgmtSESCfgErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,7))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgErrorReturn.setStatus(_A)
_Hm2FileMgmtSESCfgMgrCommandActivateErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtSESCfgMgrCommandActivateErrorReturn=_Hm2FileMgmtSESCfgMgrCommandActivateErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,8))
if mibBuilder.loadTexts:hm2FileMgmtSESCfgMgrCommandActivateErrorReturn.setStatus(_A)
_Hm2FileMgmtActionStatusErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtActionStatusErrorReturn=_Hm2FileMgmtActionStatusErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,9))
if mibBuilder.loadTexts:hm2FileMgmtActionStatusErrorReturn.setStatus(_A)
_Hm2FileMgmtConfigRemoteSaveDestinationErrorReturn_ObjectIdentity=ObjectIdentity
hm2FileMgmtConfigRemoteSaveDestinationErrorReturn=_Hm2FileMgmtConfigRemoteSaveDestinationErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,10))
if mibBuilder.loadTexts:hm2FileMgmtConfigRemoteSaveDestinationErrorReturn.setStatus(_A)
_Hm2FileMgmtConfigCannotDeleteActiveProfile_ObjectIdentity=ObjectIdentity
hm2FileMgmtConfigCannotDeleteActiveProfile=_Hm2FileMgmtConfigCannotDeleteActiveProfile_ObjectIdentity((1,3,6,1,4,1,248,11,21,3,11))
if mibBuilder.loadTexts:hm2FileMgmtConfigCannotDeleteActiveProfile.setStatus(_A)
hm2ConfigurationSavedTrap=NotificationType((1,3,6,1,4,1,248,11,21,0,1))
hm2ConfigurationSavedTrap.setObjects(*((_E,_P),(_E,_a)))
if mibBuilder.loadTexts:hm2ConfigurationSavedTrap.setStatus(_A)
hm2ConfigurationChangedTrap=NotificationType((1,3,6,1,4,1,248,11,21,0,2))
hm2ConfigurationChangedTrap.setObjects((_E,_P))
if mibBuilder.loadTexts:hm2ConfigurationChangedTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hm2FileMgmtMib':hm2FileMgmtMib,'hm2FileMgmtNotifications':hm2FileMgmtNotifications,'hm2ConfigurationSavedTrap':hm2ConfigurationSavedTrap,'hm2ConfigurationChangedTrap':hm2ConfigurationChangedTrap,'hm2FileMgmtMibObjects':hm2FileMgmtMibObjects,'hm2FileMgmtProfileGroup':hm2FileMgmtProfileGroup,'hm2FMProfileTable':hm2FMProfileTable,'hm2FMProfileEntry':hm2FMProfileEntry,_R:hm2FMProfileStorageType,_S:hm2FMProfileIndex,'hm2FMProfileName':hm2FMProfileName,'hm2FMProfileDateTime':hm2FMProfileDateTime,'hm2FMProfileActive':hm2FMProfileActive,'hm2FMProfileAction':hm2FMProfileAction,'hm2FMProfileDeviceType':hm2FMProfileDeviceType,'hm2FMProfileEncryptionActive':hm2FMProfileEncryptionActive,'hm2FMProfileEncryptionVerified':hm2FMProfileEncryptionVerified,'hm2FMProfileSwMajorRelNum':hm2FMProfileSwMajorRelNum,'hm2FMProfileSwMinorRelNum':hm2FMProfileSwMinorRelNum,'hm2FMProfileSwBugfixRelNum':hm2FMProfileSwBugfixRelNum,'hm2FMProfileFingerprint':hm2FMProfileFingerprint,'hm2FMProfileFingerprintVerified':hm2FMProfileFingerprintVerified,'hm2FileMgmtActionGroup':hm2FileMgmtActionGroup,'hm2FMActionTable':hm2FMActionTable,'hm2FMActionEntry':hm2FMActionEntry,_T:hm2FMActionType,_U:hm2FMActionItemType,_V:hm2FMActionSourceType,_W:hm2FMActionDestinationType,'hm2FMActionActivate':hm2FMActionActivate,'hm2FMActionSourceData':hm2FMActionSourceData,'hm2FMActionDestinationData':hm2FMActionDestinationData,'hm2FMActionActivateResult':hm2FMActionActivateResult,'hm2FMActionActivateResultText':hm2FMActionActivateResultText,'hm2FMActionStatus':hm2FMActionStatus,'hm2FMActionPercentReady':hm2FMActionPercentReady,'hm2FMActionResult':hm2FMActionResult,'hm2FMActionResultText':hm2FMActionResultText,'hm2FMActionActivateKey':hm2FMActionActivateKey,'hm2FMActionContainerPassword':hm2FMActionContainerPassword,'hm2FMActionParameter':hm2FMActionParameter,'hm2FMActionSourceInterface':hm2FMActionSourceInterface,'hm2FileMgmtStatusGroup':hm2FileMgmtStatusGroup,_P:hm2FMNvmState,_a:hm2FMEnvmState,'hm2FMBootParamState':hm2FMBootParamState,'hm2FileMgmtConfigGroup':hm2FileMgmtConfigGroup,'hm2FileMgmtConfigWatchdogControl':hm2FileMgmtConfigWatchdogControl,'hm2ConfigWatchdogAdminStatus':hm2ConfigWatchdogAdminStatus,'hm2ConfigWatchdogOperStatus':hm2ConfigWatchdogOperStatus,'hm2ConfigWatchdogTimeInterval':hm2ConfigWatchdogTimeInterval,'hm2ConfigWatchdogTimerValue':hm2ConfigWatchdogTimerValue,'hm2ConfigWatchdogIPAddressType':hm2ConfigWatchdogIPAddressType,'hm2ConfigWatchdogIPAddress':hm2ConfigWatchdogIPAddress,'hm2FileMgmtServerAccessGroup':hm2FileMgmtServerAccessGroup,'hm2FMServerUserName':hm2FMServerUserName,'hm2FMServerPassword':hm2FMServerPassword,'hm2FileMgmtSecurityGroup':hm2FileMgmtSecurityGroup,'hm2FileMgmtConfigPasswordStatus':hm2FileMgmtConfigPasswordStatus,'hm2FileMgmtConfigPasswordChange':hm2FileMgmtConfigPasswordChange,'hm2FileMgmtConfigRemoteSaveGroup':hm2FileMgmtConfigRemoteSaveGroup,'hm2FMConfigRemoteSaveAdminStatus':hm2FMConfigRemoteSaveAdminStatus,'hm2FMConfigRemoteSaveDestination':hm2FMConfigRemoteSaveDestination,'hm2FMConfigRemoteSaveUsername':hm2FMConfigRemoteSaveUsername,'hm2FMConfigRemoteSavePassword':hm2FMConfigRemoteSavePassword,'hm2FileMgmtGlobalSourceInterface':hm2FileMgmtGlobalSourceInterface,'hm2FileMgmtConfigCompatibilityMode':hm2FileMgmtConfigCompatibilityMode,'hm2FileMgmtSNMPExtensionGroup':hm2FileMgmtSNMPExtensionGroup,'hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn':hm2FileMgmtSESCfgActivateSuccessSetFailuresReturn,'hm2FileMgmtSESCfgActivateErrorReturn':hm2FileMgmtSESCfgActivateErrorReturn,'hm2FileMgmtSESCfgActivateIncomlpeteReturn':hm2FileMgmtSESCfgActivateIncomlpeteReturn,'hm2FileMgmtSESCfgMgrCopyCommandErrorReturn':hm2FileMgmtSESCfgMgrCopyCommandErrorReturn,'hm2FileMgmtSESCfgMgrClearCommandErrorReturn':hm2FileMgmtSESCfgMgrClearCommandErrorReturn,'hm2FileMgmtSESCfgMgrSwapCommandErrorReturn':hm2FileMgmtSESCfgMgrSwapCommandErrorReturn,'hm2FileMgmtSESCfgErrorReturn':hm2FileMgmtSESCfgErrorReturn,'hm2FileMgmtSESCfgMgrCommandActivateErrorReturn':hm2FileMgmtSESCfgMgrCommandActivateErrorReturn,'hm2FileMgmtActionStatusErrorReturn':hm2FileMgmtActionStatusErrorReturn,'hm2FileMgmtConfigRemoteSaveDestinationErrorReturn':hm2FileMgmtConfigRemoteSaveDestinationErrorReturn,'hm2FileMgmtConfigCannotDeleteActiveProfile':hm2FileMgmtConfigCannotDeleteActiveProfile})