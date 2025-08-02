_K='sshKeyPairGenerationStatus'
_J='sshSessionId'
_I='not-accessible'
_H='sshKeyPairName'
_G='read-create'
_F='RAISECOM-SSH-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomSsh=ModuleIdentity((1,3,6,1,4,1,8886,1,15))
_RaisecomSshObjects_ObjectIdentity=ObjectIdentity
raisecomSshObjects=_RaisecomSshObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,15,1))
_RaisecomSshSvrConfiguration_ObjectIdentity=ObjectIdentity
raisecomSshSvrConfiguration=_RaisecomSshSvrConfiguration_ObjectIdentity((1,3,6,1,4,1,8886,1,15,1,1))
class _SshServerVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ssh-1',1),('ssh-2',2),('both',3)))
_SshServerVersion_Type.__name__=_C
_SshServerVersion_Object=MibScalar
sshServerVersion=_SshServerVersion_Object((1,3,6,1,4,1,8886,1,15,1,1,1),_SshServerVersion_Type())
sshServerVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerVersion.setStatus(_A)
class _SshServerAuthenTimeout_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_SshServerAuthenTimeout_Type.__name__=_C
_SshServerAuthenTimeout_Object=MibScalar
sshServerAuthenTimeout=_SshServerAuthenTimeout_Object((1,3,6,1,4,1,8886,1,15,1,1,2),_SshServerAuthenTimeout_Type())
sshServerAuthenTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerAuthenTimeout.setStatus(_A)
class _SshServerAuthenRetries_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_SshServerAuthenRetries_Type.__name__=_C
_SshServerAuthenRetries_Object=MibScalar
sshServerAuthenRetries=_SshServerAuthenRetries_Object((1,3,6,1,4,1,8886,1,15,1,1,3),_SshServerAuthenRetries_Type())
sshServerAuthenRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerAuthenRetries.setStatus(_A)
class _SshServerHostKeyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SshServerHostKeyName_Type.__name__=_B
_SshServerHostKeyName_Object=MibScalar
sshServerHostKeyName=_SshServerHostKeyName_Object((1,3,6,1,4,1,8886,1,15,1,1,4),_SshServerHostKeyName_Type())
sshServerHostKeyName.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerHostKeyName.setStatus(_A)
_SshServerEnable_Type=EnableVar
_SshServerEnable_Object=MibScalar
sshServerEnable=_SshServerEnable_Object((1,3,6,1,4,1,8886,1,15,1,1,5),_SshServerEnable_Type())
sshServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerEnable.setStatus(_A)
class _SshServerAuthenType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('public_key',2),('pass_word',3)))
_SshServerAuthenType_Type.__name__=_C
_SshServerAuthenType_Object=MibScalar
sshServerAuthenType=_SshServerAuthenType_Object((1,3,6,1,4,1,8886,1,15,1,1,6),_SshServerAuthenType_Type())
sshServerAuthenType.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerAuthenType.setStatus(_A)
class _SshServerPort_Type(Integer32):defaultValue=22;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SshServerPort_Type.__name__=_C
_SshServerPort_Object=MibScalar
sshServerPort=_SshServerPort_Object((1,3,6,1,4,1,8886,1,15,1,1,7),_SshServerPort_Type())
sshServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:sshServerPort.setStatus(_A)
_RaisecomSshKeyPairMgnt_ObjectIdentity=ObjectIdentity
raisecomSshKeyPairMgnt=_RaisecomSshKeyPairMgnt_ObjectIdentity((1,3,6,1,4,1,8886,1,15,1,2))
class _SshKeyPairGenerationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('keyGenerationSuccess',1),('keyGenerationInProgress',2),('keyGenerationInvalidName',3),('keyGenerationInvalidModulus',4),('keyGenerationKeyExist',5),('keyGenerationNumLimit',6),('keyGenerationKeySavingError',7)))
_SshKeyPairGenerationStatus_Type.__name__=_C
_SshKeyPairGenerationStatus_Object=MibScalar
sshKeyPairGenerationStatus=_SshKeyPairGenerationStatus_Object((1,3,6,1,4,1,8886,1,15,1,2,1),_SshKeyPairGenerationStatus_Type())
sshKeyPairGenerationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sshKeyPairGenerationStatus.setStatus(_A)
_SshKeyPairTable_Object=MibTable
sshKeyPairTable=_SshKeyPairTable_Object((1,3,6,1,4,1,8886,1,15,1,2,2))
if mibBuilder.loadTexts:sshKeyPairTable.setStatus(_A)
_SshKeyPairEntry_Object=MibTableRow
sshKeyPairEntry=_SshKeyPairEntry_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1))
sshKeyPairEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:sshKeyPairEntry.setStatus(_A)
class _SshKeyPairName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SshKeyPairName_Type.__name__=_B
_SshKeyPairName_Object=MibTableColumn
sshKeyPairName=_SshKeyPairName_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,1),_SshKeyPairName_Type())
sshKeyPairName.setMaxAccess(_I)
if mibBuilder.loadTexts:sshKeyPairName.setStatus(_A)
class _SshKeyPairType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsa',1),('dsa',2)))
_SshKeyPairType_Type.__name__=_C
_SshKeyPairType_Object=MibTableColumn
sshKeyPairType=_SshKeyPairType_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,2),_SshKeyPairType_Type())
sshKeyPairType.setMaxAccess(_G)
if mibBuilder.loadTexts:sshKeyPairType.setStatus(_A)
class _SshKeyPairModulusSz_Type(Integer32):defaultValue=512;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,2048))
_SshKeyPairModulusSz_Type.__name__=_C
_SshKeyPairModulusSz_Object=MibTableColumn
sshKeyPairModulusSz=_SshKeyPairModulusSz_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,3),_SshKeyPairModulusSz_Type())
sshKeyPairModulusSz.setMaxAccess(_G)
if mibBuilder.loadTexts:sshKeyPairModulusSz.setStatus(_A)
class _SshKeyPairComment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SshKeyPairComment_Type.__name__=_B
_SshKeyPairComment_Object=MibTableColumn
sshKeyPairComment=_SshKeyPairComment_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,4),_SshKeyPairComment_Type())
sshKeyPairComment.setMaxAccess(_G)
if mibBuilder.loadTexts:sshKeyPairComment.setStatus(_A)
_SshKeyPairTrapOnComplete_Type=TruthValue
_SshKeyPairTrapOnComplete_Object=MibTableColumn
sshKeyPairTrapOnComplete=_SshKeyPairTrapOnComplete_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,5),_SshKeyPairTrapOnComplete_Type())
sshKeyPairTrapOnComplete.setMaxAccess(_G)
if mibBuilder.loadTexts:sshKeyPairTrapOnComplete.setStatus(_A)
class _SshKeyPairPubData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SshKeyPairPubData_Type.__name__=_B
_SshKeyPairPubData_Object=MibTableColumn
sshKeyPairPubData=_SshKeyPairPubData_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,6),_SshKeyPairPubData_Type())
sshKeyPairPubData.setMaxAccess(_D)
if mibBuilder.loadTexts:sshKeyPairPubData.setStatus(_A)
_SshKeyPairStatus_Type=RowStatus
_SshKeyPairStatus_Object=MibTableColumn
sshKeyPairStatus=_SshKeyPairStatus_Object((1,3,6,1,4,1,8886,1,15,1,2,2,1,7),_SshKeyPairStatus_Type())
sshKeyPairStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:sshKeyPairStatus.setStatus(_A)
_RaisecomSshSessionInfo_ObjectIdentity=ObjectIdentity
raisecomSshSessionInfo=_RaisecomSshSessionInfo_ObjectIdentity((1,3,6,1,4,1,8886,1,15,1,3))
_SshSessionTable_Object=MibTable
sshSessionTable=_SshSessionTable_Object((1,3,6,1,4,1,8886,1,15,1,3,1))
if mibBuilder.loadTexts:sshSessionTable.setStatus(_A)
_SshSessionEntry_Object=MibTableRow
sshSessionEntry=_SshSessionEntry_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1))
sshSessionEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:sshSessionEntry.setStatus(_A)
_SshSessionId_Type=Gauge32
_SshSessionId_Object=MibTableColumn
sshSessionId=_SshSessionId_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,1),_SshSessionId_Type())
sshSessionId.setMaxAccess(_I)
if mibBuilder.loadTexts:sshSessionId.setStatus(_A)
class _SshSessionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ssh-1',1),('ssh-2',2)))
_SshSessionVersion_Type.__name__=_C
_SshSessionVersion_Object=MibTableColumn
sshSessionVersion=_SshSessionVersion_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,2),_SshSessionVersion_Type())
sshSessionVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionVersion.setStatus(_A)
class _SshSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sessionVersionOk',1),('sessionKeysExchanged',2),('sessionAuthenticated',3),('sessionOpen',4),('sessionDisconnecting',5),('sessionDisconnected',6),('sessionClosed',7)))
_SshSessionState_Type.__name__=_C
_SshSessionState_Object=MibTableColumn
sshSessionState=_SshSessionState_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,3),_SshSessionState_Type())
sshSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionState.setStatus(_A)
class _SshSessionUserId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SshSessionUserId_Type.__name__=_B
_SshSessionUserId_Object=MibTableColumn
sshSessionUserId=_SshSessionUserId_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,4),_SshSessionUserId_Type())
sshSessionUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionUserId.setStatus(_A)
_SshSessionHostAddr_Type=IpAddress
_SshSessionHostAddr_Object=MibTableColumn
sshSessionHostAddr=_SshSessionHostAddr_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,5),_SshSessionHostAddr_Type())
sshSessionHostAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionHostAddr.setStatus(_A)
class _SshSessionInEncrypt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SshSessionInEncrypt_Type.__name__=_B
_SshSessionInEncrypt_Object=MibTableColumn
sshSessionInEncrypt=_SshSessionInEncrypt_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,6),_SshSessionInEncrypt_Type())
sshSessionInEncrypt.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionInEncrypt.setStatus(_A)
class _SshSessionOutEncrypt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SshSessionOutEncrypt_Type.__name__=_B
_SshSessionOutEncrypt_Object=MibTableColumn
sshSessionOutEncrypt=_SshSessionOutEncrypt_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,7),_SshSessionOutEncrypt_Type())
sshSessionOutEncrypt.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionOutEncrypt.setStatus(_A)
class _SshSessionInHmac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SshSessionInHmac_Type.__name__=_B
_SshSessionInHmac_Object=MibTableColumn
sshSessionInHmac=_SshSessionInHmac_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,8),_SshSessionInHmac_Type())
sshSessionInHmac.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionInHmac.setStatus(_A)
class _SshSessionOutHmac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_SshSessionOutHmac_Type.__name__=_B
_SshSessionOutHmac_Object=MibTableColumn
sshSessionOutHmac=_SshSessionOutHmac_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,9),_SshSessionOutHmac_Type())
sshSessionOutHmac.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionOutHmac.setStatus(_A)
class _SshSessionConnectTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,65535))
_SshSessionConnectTime_Type.__name__=_B
_SshSessionConnectTime_Object=MibTableColumn
sshSessionConnectTime=_SshSessionConnectTime_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,10),_SshSessionConnectTime_Type())
sshSessionConnectTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sshSessionConnectTime.setStatus(_A)
_SshSessionEnable_Type=EnableVar
_SshSessionEnable_Object=MibTableColumn
sshSessionEnable=_SshSessionEnable_Object((1,3,6,1,4,1,8886,1,15,1,3,1,1,11),_SshSessionEnable_Type())
sshSessionEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sshSessionEnable.setStatus(_A)
_RaisecomSshTraps_ObjectIdentity=ObjectIdentity
raisecomSshTraps=_RaisecomSshTraps_ObjectIdentity((1,3,6,1,4,1,8886,1,15,2))
sshKeyPairGenerationCompletion=NotificationGroup((1,3,6,1,4,1,8886,1,15,2,1))
sshKeyPairGenerationCompletion.setObjects(*((_F,_K),(_F,_H)))
if mibBuilder.loadTexts:sshKeyPairGenerationCompletion.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'raisecomSsh':raisecomSsh,'raisecomSshObjects':raisecomSshObjects,'raisecomSshSvrConfiguration':raisecomSshSvrConfiguration,'sshServerVersion':sshServerVersion,'sshServerAuthenTimeout':sshServerAuthenTimeout,'sshServerAuthenRetries':sshServerAuthenRetries,'sshServerHostKeyName':sshServerHostKeyName,'sshServerEnable':sshServerEnable,'sshServerAuthenType':sshServerAuthenType,'sshServerPort':sshServerPort,'raisecomSshKeyPairMgnt':raisecomSshKeyPairMgnt,_K:sshKeyPairGenerationStatus,'sshKeyPairTable':sshKeyPairTable,'sshKeyPairEntry':sshKeyPairEntry,_H:sshKeyPairName,'sshKeyPairType':sshKeyPairType,'sshKeyPairModulusSz':sshKeyPairModulusSz,'sshKeyPairComment':sshKeyPairComment,'sshKeyPairTrapOnComplete':sshKeyPairTrapOnComplete,'sshKeyPairPubData':sshKeyPairPubData,'sshKeyPairStatus':sshKeyPairStatus,'raisecomSshSessionInfo':raisecomSshSessionInfo,'sshSessionTable':sshSessionTable,'sshSessionEntry':sshSessionEntry,_J:sshSessionId,'sshSessionVersion':sshSessionVersion,'sshSessionState':sshSessionState,'sshSessionUserId':sshSessionUserId,'sshSessionHostAddr':sshSessionHostAddr,'sshSessionInEncrypt':sshSessionInEncrypt,'sshSessionOutEncrypt':sshSessionOutEncrypt,'sshSessionInHmac':sshSessionInHmac,'sshSessionOutHmac':sshSessionOutHmac,'sshSessionConnectTime':sshSessionConnectTime,'sshSessionEnable':sshSessionEnable,'raisecomSshTraps':raisecomSshTraps,'sshKeyPairGenerationCompletion':sshKeyPairGenerationCompletion})