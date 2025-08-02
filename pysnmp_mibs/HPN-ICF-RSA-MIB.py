_M='hpnicfRSAPeerKeyConfigFailReason'
_L='hpnicfRSALocalKeyFailReason'
_K='accessible-for-notify'
_J='hpnicfRSALocalKeyIndex'
_I='read-write'
_H='not-accessible'
_G='hpnicfRSAPeerPublicKeyName'
_F='Integer32'
_E='read-create'
_D='HPN-ICF-RSA-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfRSA=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,23))
if mibBuilder.loadTexts:hpnicfRSA.setRevisions(('2004-10-10 00:00',))
class RSAKeyErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('rsaSuccess',1),('rsaFailure',2),('rsaErrNoMemory',3),('rsaErrKeyNotReplaced',4),('rsaErrKeyBackup',5),('rsaErrKeySaved',6),('rsaErrKeyGenerate',7),('rsaErrKeyDestroy',8),('rsaErrHostEncKeyBackup',9),('rsaErrHostEncKeySave',10),('rsaErrHostEncKeyGenerate',11),('rsaErrHostEncKeyDestroy',12),('rsaErrHostSigKeyBackup',13),('rsaErrHostSigKeySave',14),('rsaErrHostSigKeyGenerate',15),('rsaErrHostSigKeyDestroy',16),('rsaErrServerKeyBackup',17),('rsaErrServerKeySave',18),('rsaErrServerKeyGenerate',19),('rsaErrServerKeyDestroy',20),('rsaErrPeerKeyNotReplaced',21),('rsaErrPeerKeyNumArriveMax',22),('rsaErrPeerKeyNotRemoved',23),('rsaErrPeerKeyNotExist',24),('rsaStatusKeyExist',25),('rsaStatusKeyNotExist',26),('rsaStatusKeyInvalid',27),('rsaStatusHostEncKeyExist',28),('rsaStatusHostEncKeyNotExist',29),('rsaStatusHostEncKeyInvalid',30),('rsaStatusHostSigKeyExist',31),('rsaStatusHostSigKeyNotExist',32),('rsaStatusHostSigKeyInvalid',33),('rsaStatusServerKeyExist',34),('rsaStatusServerKeyNotExist',35),('rsaStatusServerKeyInvalid',36)))
_HpnicfRSAMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfRSAMIBObjects=_HpnicfRSAMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,23,1))
_HpnicfRSAPeerPublicKeyTable_Object=MibTable
hpnicfRSAPeerPublicKeyTable=_HpnicfRSAPeerPublicKeyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1))
if mibBuilder.loadTexts:hpnicfRSAPeerPublicKeyTable.setStatus(_A)
_HpnicfRSAPeerPublicKeyEntry_Object=MibTableRow
hpnicfRSAPeerPublicKeyEntry=_HpnicfRSAPeerPublicKeyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1))
hpnicfRSAPeerPublicKeyEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfRSAPeerPublicKeyEntry.setStatus(_A)
class _HpnicfRSAPeerPublicKeyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfRSAPeerPublicKeyName_Type.__name__=_C
_HpnicfRSAPeerPublicKeyName_Object=MibTableColumn
hpnicfRSAPeerPublicKeyName=_HpnicfRSAPeerPublicKeyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1,1),_HpnicfRSAPeerPublicKeyName_Type())
hpnicfRSAPeerPublicKeyName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfRSAPeerPublicKeyName.setStatus(_A)
_HpnicfRSAPeerIpAddress_Type=IpAddress
_HpnicfRSAPeerIpAddress_Object=MibTableColumn
hpnicfRSAPeerIpAddress=_HpnicfRSAPeerIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1,2),_HpnicfRSAPeerIpAddress_Type())
hpnicfRSAPeerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRSAPeerIpAddress.setStatus(_A)
_HpnicfRSAPeerFQDN_Type=DisplayString
_HpnicfRSAPeerFQDN_Object=MibTableColumn
hpnicfRSAPeerFQDN=_HpnicfRSAPeerFQDN_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1,3),_HpnicfRSAPeerFQDN_Type())
hpnicfRSAPeerFQDN.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRSAPeerFQDN.setStatus(_A)
class _HpnicfRSAPeerPublicKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_HpnicfRSAPeerPublicKeyCode_Type.__name__=_C
_HpnicfRSAPeerPublicKeyCode_Object=MibTableColumn
hpnicfRSAPeerPublicKeyCode=_HpnicfRSAPeerPublicKeyCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1,4),_HpnicfRSAPeerPublicKeyCode_Type())
hpnicfRSAPeerPublicKeyCode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRSAPeerPublicKeyCode.setStatus(_A)
_HpnicfRSAPeerPublicKeyStatus_Type=RowStatus
_HpnicfRSAPeerPublicKeyStatus_Object=MibTableColumn
hpnicfRSAPeerPublicKeyStatus=_HpnicfRSAPeerPublicKeyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,1,1,5),_HpnicfRSAPeerPublicKeyStatus_Type())
hpnicfRSAPeerPublicKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRSAPeerPublicKeyStatus.setStatus(_A)
_HpnicfRSALocalKeyPairTable_Object=MibTable
hpnicfRSALocalKeyPairTable=_HpnicfRSALocalKeyPairTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2))
if mibBuilder.loadTexts:hpnicfRSALocalKeyPairTable.setStatus(_A)
_HpnicfRSALocalKeyPairEntry_Object=MibTableRow
hpnicfRSALocalKeyPairEntry=_HpnicfRSALocalKeyPairEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1))
hpnicfRSALocalKeyPairEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfRSALocalKeyPairEntry.setStatus(_A)
class _HpnicfRSALocalKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_HpnicfRSALocalKeyIndex_Type.__name__=_F
_HpnicfRSALocalKeyIndex_Object=MibTableColumn
hpnicfRSALocalKeyIndex=_HpnicfRSALocalKeyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,1),_HpnicfRSALocalKeyIndex_Type())
hpnicfRSALocalKeyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfRSALocalKeyIndex.setStatus(_A)
_HpnicfRSALocalHostKeyName_Type=DisplayString
_HpnicfRSALocalHostKeyName_Object=MibTableColumn
hpnicfRSALocalHostKeyName=_HpnicfRSALocalHostKeyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,2),_HpnicfRSALocalHostKeyName_Type())
hpnicfRSALocalHostKeyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalHostKeyName.setStatus(_A)
class _HpnicfRSALocalHostKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,1024))
_HpnicfRSALocalHostKeyCode_Type.__name__=_C
_HpnicfRSALocalHostKeyCode_Object=MibTableColumn
hpnicfRSALocalHostKeyCode=_HpnicfRSALocalHostKeyCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,3),_HpnicfRSALocalHostKeyCode_Type())
hpnicfRSALocalHostKeyCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalHostKeyCode.setStatus(_A)
_HpnicfRSALocalHostKeyCreatedTime_Type=DateAndTime
_HpnicfRSALocalHostKeyCreatedTime_Object=MibTableColumn
hpnicfRSALocalHostKeyCreatedTime=_HpnicfRSALocalHostKeyCreatedTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,4),_HpnicfRSALocalHostKeyCreatedTime_Type())
hpnicfRSALocalHostKeyCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalHostKeyCreatedTime.setStatus(_A)
_HpnicfRSALocalServerKeyName_Type=DisplayString
_HpnicfRSALocalServerKeyName_Object=MibTableColumn
hpnicfRSALocalServerKeyName=_HpnicfRSALocalServerKeyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,5),_HpnicfRSALocalServerKeyName_Type())
hpnicfRSALocalServerKeyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalServerKeyName.setStatus(_A)
class _HpnicfRSALocalServerKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,1024))
_HpnicfRSALocalServerKeyCode_Type.__name__=_C
_HpnicfRSALocalServerKeyCode_Object=MibTableColumn
hpnicfRSALocalServerKeyCode=_HpnicfRSALocalServerKeyCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,6),_HpnicfRSALocalServerKeyCode_Type())
hpnicfRSALocalServerKeyCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalServerKeyCode.setStatus(_A)
_HpnicfRSALocalServerKeyCreatedTime_Type=DateAndTime
_HpnicfRSALocalServerKeyCreatedTime_Object=MibTableColumn
hpnicfRSALocalServerKeyCreatedTime=_HpnicfRSALocalServerKeyCreatedTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,7),_HpnicfRSALocalServerKeyCreatedTime_Type())
hpnicfRSALocalServerKeyCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRSALocalServerKeyCreatedTime.setStatus(_A)
class _HpnicfRSALocalKeyPairBits_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,2048))
_HpnicfRSALocalKeyPairBits_Type.__name__=_F
_HpnicfRSALocalKeyPairBits_Object=MibTableColumn
hpnicfRSALocalKeyPairBits=_HpnicfRSALocalKeyPairBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,8),_HpnicfRSALocalKeyPairBits_Type())
hpnicfRSALocalKeyPairBits.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRSALocalKeyPairBits.setStatus(_A)
_HpnicfRSALocalKeyStatus_Type=RowStatus
_HpnicfRSALocalKeyStatus_Object=MibTableColumn
hpnicfRSALocalKeyStatus=_HpnicfRSALocalKeyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,2,1,9),_HpnicfRSALocalKeyStatus_Type())
hpnicfRSALocalKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRSALocalKeyStatus.setStatus(_A)
_HpnicfRSAPeerKeyConfigFailReason_Type=RSAKeyErrorCode
_HpnicfRSAPeerKeyConfigFailReason_Object=MibScalar
hpnicfRSAPeerKeyConfigFailReason=_HpnicfRSAPeerKeyConfigFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,3),_HpnicfRSAPeerKeyConfigFailReason_Type())
hpnicfRSAPeerKeyConfigFailReason.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfRSAPeerKeyConfigFailReason.setStatus(_A)
_HpnicfRSALocalKeyFailReason_Type=RSAKeyErrorCode
_HpnicfRSALocalKeyFailReason_Object=MibScalar
hpnicfRSALocalKeyFailReason=_HpnicfRSALocalKeyFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,23,1,4),_HpnicfRSALocalKeyFailReason_Type())
hpnicfRSALocalKeyFailReason.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfRSALocalKeyFailReason.setStatus(_A)
_HpnicfRSANotifications_ObjectIdentity=ObjectIdentity
hpnicfRSANotifications=_HpnicfRSANotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,23,2))
hpnicfRSALocalKeyPairOpeFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,23,2,1))
hpnicfRSALocalKeyPairOpeFail.setObjects((_D,_L))
if mibBuilder.loadTexts:hpnicfRSALocalKeyPairOpeFail.setStatus(_A)
hpnicfRSAPeerKeyConfigFail=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,23,2,2))
hpnicfRSAPeerKeyConfigFail.setObjects((_D,_M))
if mibBuilder.loadTexts:hpnicfRSAPeerKeyConfigFail.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RSAKeyErrorCode':RSAKeyErrorCode,'hpnicfRSA':hpnicfRSA,'hpnicfRSAMIBObjects':hpnicfRSAMIBObjects,'hpnicfRSAPeerPublicKeyTable':hpnicfRSAPeerPublicKeyTable,'hpnicfRSAPeerPublicKeyEntry':hpnicfRSAPeerPublicKeyEntry,_G:hpnicfRSAPeerPublicKeyName,'hpnicfRSAPeerIpAddress':hpnicfRSAPeerIpAddress,'hpnicfRSAPeerFQDN':hpnicfRSAPeerFQDN,'hpnicfRSAPeerPublicKeyCode':hpnicfRSAPeerPublicKeyCode,'hpnicfRSAPeerPublicKeyStatus':hpnicfRSAPeerPublicKeyStatus,'hpnicfRSALocalKeyPairTable':hpnicfRSALocalKeyPairTable,'hpnicfRSALocalKeyPairEntry':hpnicfRSALocalKeyPairEntry,_J:hpnicfRSALocalKeyIndex,'hpnicfRSALocalHostKeyName':hpnicfRSALocalHostKeyName,'hpnicfRSALocalHostKeyCode':hpnicfRSALocalHostKeyCode,'hpnicfRSALocalHostKeyCreatedTime':hpnicfRSALocalHostKeyCreatedTime,'hpnicfRSALocalServerKeyName':hpnicfRSALocalServerKeyName,'hpnicfRSALocalServerKeyCode':hpnicfRSALocalServerKeyCode,'hpnicfRSALocalServerKeyCreatedTime':hpnicfRSALocalServerKeyCreatedTime,'hpnicfRSALocalKeyPairBits':hpnicfRSALocalKeyPairBits,'hpnicfRSALocalKeyStatus':hpnicfRSALocalKeyStatus,_M:hpnicfRSAPeerKeyConfigFailReason,_L:hpnicfRSALocalKeyFailReason,'hpnicfRSANotifications':hpnicfRSANotifications,'hpnicfRSALocalKeyPairOpeFail':hpnicfRSALocalKeyPairOpeFail,'hpnicfRSAPeerKeyConfigFail':hpnicfRSAPeerKeyConfigFail})