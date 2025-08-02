_M='h3cRSAPeerKeyConfigFailReason'
_L='h3cRSALocalKeyFailReason'
_K='accessible-for-notify'
_J='h3cRSALocalKeyIndex'
_I='read-write'
_H='not-accessible'
_G='h3cRSAPeerPublicKeyName'
_F='Integer32'
_E='read-create'
_D='H3C-RSA-MIB'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cRSA=ModuleIdentity((1,3,6,1,4,1,2011,10,2,23))
if mibBuilder.loadTexts:h3cRSA.setRevisions(('2004-10-10 00:00',))
class RSAKeyErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('rsaSuccess',1),('rsaFailure',2),('rsaErrNoMemory',3),('rsaErrKeyNotReplaced',4),('rsaErrKeyBackup',5),('rsaErrKeySaved',6),('rsaErrKeyGenerate',7),('rsaErrKeyDestroy',8),('rsaErrHostEncKeyBackup',9),('rsaErrHostEncKeySave',10),('rsaErrHostEncKeyGenerate',11),('rsaErrHostEncKeyDestroy',12),('rsaErrHostSigKeyBackup',13),('rsaErrHostSigKeySave',14),('rsaErrHostSigKeyGenerate',15),('rsaErrHostSigKeyDestroy',16),('rsaErrServerKeyBackup',17),('rsaErrServerKeySave',18),('rsaErrServerKeyGenerate',19),('rsaErrServerKeyDestroy',20),('rsaErrPeerKeyNotReplaced',21),('rsaErrPeerKeyNumArriveMax',22),('rsaErrPeerKeyNotRemoved',23),('rsaErrPeerKeyNotExist',24),('rsaStatusKeyExist',25),('rsaStatusKeyNotExist',26),('rsaStatusKeyInvalid',27),('rsaStatusHostEncKeyExist',28),('rsaStatusHostEncKeyNotExist',29),('rsaStatusHostEncKeyInvalid',30),('rsaStatusHostSigKeyExist',31),('rsaStatusHostSigKeyNotExist',32),('rsaStatusHostSigKeyInvalid',33),('rsaStatusServerKeyExist',34),('rsaStatusServerKeyNotExist',35),('rsaStatusServerKeyInvalid',36)))
_H3cRSAMIBObjects_ObjectIdentity=ObjectIdentity
h3cRSAMIBObjects=_H3cRSAMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,23,1))
_H3cRSAPeerPublicKeyTable_Object=MibTable
h3cRSAPeerPublicKeyTable=_H3cRSAPeerPublicKeyTable_Object((1,3,6,1,4,1,2011,10,2,23,1,1))
if mibBuilder.loadTexts:h3cRSAPeerPublicKeyTable.setStatus(_A)
_H3cRSAPeerPublicKeyEntry_Object=MibTableRow
h3cRSAPeerPublicKeyEntry=_H3cRSAPeerPublicKeyEntry_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1))
h3cRSAPeerPublicKeyEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:h3cRSAPeerPublicKeyEntry.setStatus(_A)
class _H3cRSAPeerPublicKeyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cRSAPeerPublicKeyName_Type.__name__=_C
_H3cRSAPeerPublicKeyName_Object=MibTableColumn
h3cRSAPeerPublicKeyName=_H3cRSAPeerPublicKeyName_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1,1),_H3cRSAPeerPublicKeyName_Type())
h3cRSAPeerPublicKeyName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cRSAPeerPublicKeyName.setStatus(_A)
_H3cRSAPeerIpAddress_Type=IpAddress
_H3cRSAPeerIpAddress_Object=MibTableColumn
h3cRSAPeerIpAddress=_H3cRSAPeerIpAddress_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1,2),_H3cRSAPeerIpAddress_Type())
h3cRSAPeerIpAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRSAPeerIpAddress.setStatus(_A)
_H3cRSAPeerFQDN_Type=DisplayString
_H3cRSAPeerFQDN_Object=MibTableColumn
h3cRSAPeerFQDN=_H3cRSAPeerFQDN_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1,3),_H3cRSAPeerFQDN_Type())
h3cRSAPeerFQDN.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRSAPeerFQDN.setStatus(_A)
class _H3cRSAPeerPublicKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_H3cRSAPeerPublicKeyCode_Type.__name__=_C
_H3cRSAPeerPublicKeyCode_Object=MibTableColumn
h3cRSAPeerPublicKeyCode=_H3cRSAPeerPublicKeyCode_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1,4),_H3cRSAPeerPublicKeyCode_Type())
h3cRSAPeerPublicKeyCode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRSAPeerPublicKeyCode.setStatus(_A)
_H3cRSAPeerPublicKeyStatus_Type=RowStatus
_H3cRSAPeerPublicKeyStatus_Object=MibTableColumn
h3cRSAPeerPublicKeyStatus=_H3cRSAPeerPublicKeyStatus_Object((1,3,6,1,4,1,2011,10,2,23,1,1,1,5),_H3cRSAPeerPublicKeyStatus_Type())
h3cRSAPeerPublicKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRSAPeerPublicKeyStatus.setStatus(_A)
_H3cRSALocalKeyPairTable_Object=MibTable
h3cRSALocalKeyPairTable=_H3cRSALocalKeyPairTable_Object((1,3,6,1,4,1,2011,10,2,23,1,2))
if mibBuilder.loadTexts:h3cRSALocalKeyPairTable.setStatus(_A)
_H3cRSALocalKeyPairEntry_Object=MibTableRow
h3cRSALocalKeyPairEntry=_H3cRSALocalKeyPairEntry_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1))
h3cRSALocalKeyPairEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:h3cRSALocalKeyPairEntry.setStatus(_A)
class _H3cRSALocalKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_H3cRSALocalKeyIndex_Type.__name__=_F
_H3cRSALocalKeyIndex_Object=MibTableColumn
h3cRSALocalKeyIndex=_H3cRSALocalKeyIndex_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,1),_H3cRSALocalKeyIndex_Type())
h3cRSALocalKeyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cRSALocalKeyIndex.setStatus(_A)
_H3cRSALocalHostKeyName_Type=DisplayString
_H3cRSALocalHostKeyName_Object=MibTableColumn
h3cRSALocalHostKeyName=_H3cRSALocalHostKeyName_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,2),_H3cRSALocalHostKeyName_Type())
h3cRSALocalHostKeyName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalHostKeyName.setStatus(_A)
class _H3cRSALocalHostKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,1024))
_H3cRSALocalHostKeyCode_Type.__name__=_C
_H3cRSALocalHostKeyCode_Object=MibTableColumn
h3cRSALocalHostKeyCode=_H3cRSALocalHostKeyCode_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,3),_H3cRSALocalHostKeyCode_Type())
h3cRSALocalHostKeyCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalHostKeyCode.setStatus(_A)
_H3cRSALocalHostKeyCreatedTime_Type=DateAndTime
_H3cRSALocalHostKeyCreatedTime_Object=MibTableColumn
h3cRSALocalHostKeyCreatedTime=_H3cRSALocalHostKeyCreatedTime_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,4),_H3cRSALocalHostKeyCreatedTime_Type())
h3cRSALocalHostKeyCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalHostKeyCreatedTime.setStatus(_A)
_H3cRSALocalServerKeyName_Type=DisplayString
_H3cRSALocalServerKeyName_Object=MibTableColumn
h3cRSALocalServerKeyName=_H3cRSALocalServerKeyName_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,5),_H3cRSALocalServerKeyName_Type())
h3cRSALocalServerKeyName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalServerKeyName.setStatus(_A)
class _H3cRSALocalServerKeyCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,1024))
_H3cRSALocalServerKeyCode_Type.__name__=_C
_H3cRSALocalServerKeyCode_Object=MibTableColumn
h3cRSALocalServerKeyCode=_H3cRSALocalServerKeyCode_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,6),_H3cRSALocalServerKeyCode_Type())
h3cRSALocalServerKeyCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalServerKeyCode.setStatus(_A)
_H3cRSALocalServerKeyCreatedTime_Type=DateAndTime
_H3cRSALocalServerKeyCreatedTime_Object=MibTableColumn
h3cRSALocalServerKeyCreatedTime=_H3cRSALocalServerKeyCreatedTime_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,7),_H3cRSALocalServerKeyCreatedTime_Type())
h3cRSALocalServerKeyCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRSALocalServerKeyCreatedTime.setStatus(_A)
class _H3cRSALocalKeyPairBits_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,2048))
_H3cRSALocalKeyPairBits_Type.__name__=_F
_H3cRSALocalKeyPairBits_Object=MibTableColumn
h3cRSALocalKeyPairBits=_H3cRSALocalKeyPairBits_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,8),_H3cRSALocalKeyPairBits_Type())
h3cRSALocalKeyPairBits.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRSALocalKeyPairBits.setStatus(_A)
_H3cRSALocalKeyStatus_Type=RowStatus
_H3cRSALocalKeyStatus_Object=MibTableColumn
h3cRSALocalKeyStatus=_H3cRSALocalKeyStatus_Object((1,3,6,1,4,1,2011,10,2,23,1,2,1,9),_H3cRSALocalKeyStatus_Type())
h3cRSALocalKeyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRSALocalKeyStatus.setStatus(_A)
_H3cRSAPeerKeyConfigFailReason_Type=RSAKeyErrorCode
_H3cRSAPeerKeyConfigFailReason_Object=MibScalar
h3cRSAPeerKeyConfigFailReason=_H3cRSAPeerKeyConfigFailReason_Object((1,3,6,1,4,1,2011,10,2,23,1,3),_H3cRSAPeerKeyConfigFailReason_Type())
h3cRSAPeerKeyConfigFailReason.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRSAPeerKeyConfigFailReason.setStatus(_A)
_H3cRSALocalKeyFailReason_Type=RSAKeyErrorCode
_H3cRSALocalKeyFailReason_Object=MibScalar
h3cRSALocalKeyFailReason=_H3cRSALocalKeyFailReason_Object((1,3,6,1,4,1,2011,10,2,23,1,4),_H3cRSALocalKeyFailReason_Type())
h3cRSALocalKeyFailReason.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRSALocalKeyFailReason.setStatus(_A)
_H3cRSANotifications_ObjectIdentity=ObjectIdentity
h3cRSANotifications=_H3cRSANotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,23,2))
h3cRSALocalKeyPairOpeFail=NotificationType((1,3,6,1,4,1,2011,10,2,23,2,1))
h3cRSALocalKeyPairOpeFail.setObjects((_D,_L))
if mibBuilder.loadTexts:h3cRSALocalKeyPairOpeFail.setStatus(_A)
h3cRSAPeerKeyConfigFail=NotificationType((1,3,6,1,4,1,2011,10,2,23,2,2))
h3cRSAPeerKeyConfigFail.setObjects((_D,_M))
if mibBuilder.loadTexts:h3cRSAPeerKeyConfigFail.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RSAKeyErrorCode':RSAKeyErrorCode,'h3cRSA':h3cRSA,'h3cRSAMIBObjects':h3cRSAMIBObjects,'h3cRSAPeerPublicKeyTable':h3cRSAPeerPublicKeyTable,'h3cRSAPeerPublicKeyEntry':h3cRSAPeerPublicKeyEntry,_G:h3cRSAPeerPublicKeyName,'h3cRSAPeerIpAddress':h3cRSAPeerIpAddress,'h3cRSAPeerFQDN':h3cRSAPeerFQDN,'h3cRSAPeerPublicKeyCode':h3cRSAPeerPublicKeyCode,'h3cRSAPeerPublicKeyStatus':h3cRSAPeerPublicKeyStatus,'h3cRSALocalKeyPairTable':h3cRSALocalKeyPairTable,'h3cRSALocalKeyPairEntry':h3cRSALocalKeyPairEntry,_J:h3cRSALocalKeyIndex,'h3cRSALocalHostKeyName':h3cRSALocalHostKeyName,'h3cRSALocalHostKeyCode':h3cRSALocalHostKeyCode,'h3cRSALocalHostKeyCreatedTime':h3cRSALocalHostKeyCreatedTime,'h3cRSALocalServerKeyName':h3cRSALocalServerKeyName,'h3cRSALocalServerKeyCode':h3cRSALocalServerKeyCode,'h3cRSALocalServerKeyCreatedTime':h3cRSALocalServerKeyCreatedTime,'h3cRSALocalKeyPairBits':h3cRSALocalKeyPairBits,'h3cRSALocalKeyStatus':h3cRSALocalKeyStatus,_M:h3cRSAPeerKeyConfigFailReason,_L:h3cRSALocalKeyFailReason,'h3cRSANotifications':h3cRSANotifications,'h3cRSALocalKeyPairOpeFail':h3cRSALocalKeyPairOpeFail,'h3cRSAPeerKeyConfigFail':h3cRSAPeerKeyConfigFail})