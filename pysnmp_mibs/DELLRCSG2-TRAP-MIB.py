_o='dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged'
_n='dellrcsg2TrapObjectCurrentScreenResolution'
_m='dellrcsg2TrapObjectPreviousScreenResolution'
_l='dellrcsg2TrapObjectSIPImageUpgradeResult'
_k='dellrcsg2TrapObjectOldTieredSwitchName'
_j='dellrcsg2TrapObjectOldTargetDeviceName'
_i='dellrcsg2TrapObjectOldInputPort'
_h='dellrcsg2TrapObjectInputPort'
_g='dellrcsg2TrapObjectUnlockReason'
_f='dellrcsg2TrapObjectLockReason'
_e='NotificationType'
_d='OctetString'
_c='dellrcsg2TrapObjectPduDeviceCircuit'
_b='dellrcsg2TrapObjectPowerSupply'
_a='dellrcsg2TrapObjectImageFileUpgradeResult'
_Z='dellrcsg2TrapObjectPduDeviceInlet'
_Y='dellrcsg2TrapObjectTieredSwitchName'
_X='dellrcsg2TrapObjectFileName'
_W='dellrcsg2TrapObjectSessionType'
_V='dellrcsg2TrapObjectVirtualMediaDriveAccessMode'
_U='dellrcsg2TrapObjectVirtualMediaDriveType'
_T='dellrcsg2TrapObjectTypeOfImage'
_S='dellrcsg2TrapObjectItemName'
_R='dellrcsg2TrapObjectOldName'
_Q='dellrcsg2TrapObjectImageCurrentVersion'
_P='dellrcsg2TrapObjectImageNewVersion'
_O='Integer32'
_N='DisplayString'
_M='dellrcsg2TrapObjectTargetUserName'
_L='dellrcsg2TrapObjectSessionIdentifier'
_K='dellrcsg2TrapObjectSIPId'
_J='dellrcsg2TrapObjectUserAddress'
_I='dellrcsg2TrapObjectPduOutlet'
_H='UTF8String'
_G='dellrcsg2TrapObjectPduDeviceNumber'
_F='dellrcsg2TrapObjectPduDevicePort'
_E='dellrcsg2TrapObjectTargetDeviceName'
_D='mandatory'
_C='not-accessible'
_B='dellrcsg2TrapObjectUserName'
_A='DELLRCSG2-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_d,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier',_e,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_e,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention')
class UTF8String(OctetString):0
class ImageFileUpgradeResultsEnum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,9999)));namedValues=NamedValues(*(('imageUpgradeTftpNoSocket',1),('imageUpgradeTftpConnectFailure',2),('imageUpgradeTftpRequestDenied',3),('imageUpgradeTftpBadPacket',4),('imageUpgradeTftpOOS',5),('imageUpgradeTftpTooBig',6),('imageUpgradeTftpTimeout',7),('imageUpgradeAlreadyInProgress',8),('imageUpgradeCannotStart',9),('imageUpgradeMemoryError',10),('imageUpgradeTftpProtocolError',11),('imageUpgradeBadType',12),('imageUpgradeInvalidAppDowngrade',13),('imageUpgradeChecksumError',14),('imageUpgradeFlashError',15),('imageUpgradeInternalError',16),('imageUpgradeFileNotFound',17),('imageUpgradeBadHeader',18),('imageUpgradeIncompatibleHeader',19),('imageUpgradeTftpXferFail',20),('imageUpgradeTftpSvrNoResponse',21),('imageUpgradeNetworkUnreachable',22),('imageUpgradeSuccess',9999)))
class SIPUpgradeResultsEnum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,9999)));namedValues=NamedValues(*(('sipUpgradeNoFirmwareImage',1),('sipUpgradeLostContact',2),('sipUpgradeFailedRestart',3),('sipUpgradeFailedVerify',4),('sipUpgradeSuccess',9999)))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,10418))
_Dellrcsg2_ObjectIdentity=ObjectIdentity
dellrcsg2=_Dellrcsg2_ObjectIdentity((1,3,6,1,4,1,10418,18))
_Dellrcsg2Products_ObjectIdentity=ObjectIdentity
dellrcsg2Products=_Dellrcsg2Products_ObjectIdentity((1,3,6,1,4,1,10418,18,21))
_Dellrcs1082ds_ObjectIdentity=ObjectIdentity
dellrcs1082ds=_Dellrcs1082ds_ObjectIdentity((1,3,6,1,4,1,10418,18,21,17))
_Dellrcs2162ds_ObjectIdentity=ObjectIdentity
dellrcs2162ds=_Dellrcs2162ds_ObjectIdentity((1,3,6,1,4,1,10418,18,21,24))
_Dellrcs4322ds_ObjectIdentity=ObjectIdentity
dellrcs4322ds=_Dellrcs4322ds_ObjectIdentity((1,3,6,1,4,1,10418,18,21,26))
_Dellrcsg2Management_ObjectIdentity=ObjectIdentity
dellrcsg2Management=_Dellrcsg2Management_ObjectIdentity((1,3,6,1,4,1,10418,18,22))
_Dellrcsg2TrapObject_ObjectIdentity=ObjectIdentity
dellrcsg2TrapObject=_Dellrcsg2TrapObject_ObjectIdentity((1,3,6,1,4,1,10418,18,22,6))
class _Dellrcsg2TrapObjectUserName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,16))
_Dellrcsg2TrapObjectUserName_Type.__name__=_H
_Dellrcsg2TrapObjectUserName_Object=MibScalar
dellrcsg2TrapObjectUserName=_Dellrcsg2TrapObjectUserName_Object((1,3,6,1,4,1,10418,18,22,6,1),_Dellrcsg2TrapObjectUserName_Type())
dellrcsg2TrapObjectUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectUserName.setStatus(_D)
class _Dellrcsg2TrapObjectTargetUserName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,16))
_Dellrcsg2TrapObjectTargetUserName_Type.__name__=_H
_Dellrcsg2TrapObjectTargetUserName_Object=MibScalar
dellrcsg2TrapObjectTargetUserName=_Dellrcsg2TrapObjectTargetUserName_Object((1,3,6,1,4,1,10418,18,22,6,2),_Dellrcsg2TrapObjectTargetUserName_Type())
dellrcsg2TrapObjectTargetUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectTargetUserName.setStatus(_D)
class _Dellrcsg2TrapObjectImageType_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dellrcsg2TrapObjectImageType_Type.__name__=_H
_Dellrcsg2TrapObjectImageType_Object=MibScalar
dellrcsg2TrapObjectImageType=_Dellrcsg2TrapObjectImageType_Object((1,3,6,1,4,1,10418,18,22,6,3),_Dellrcsg2TrapObjectImageType_Type())
dellrcsg2TrapObjectImageType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectImageType.setStatus(_D)
class _Dellrcsg2TrapObjectImageNewVersion_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectImageNewVersion_Type.__name__=_H
_Dellrcsg2TrapObjectImageNewVersion_Object=MibScalar
dellrcsg2TrapObjectImageNewVersion=_Dellrcsg2TrapObjectImageNewVersion_Object((1,3,6,1,4,1,10418,18,22,6,4),_Dellrcsg2TrapObjectImageNewVersion_Type())
dellrcsg2TrapObjectImageNewVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectImageNewVersion.setStatus(_D)
class _Dellrcsg2TrapObjectImageCurrentVersion_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectImageCurrentVersion_Type.__name__=_H
_Dellrcsg2TrapObjectImageCurrentVersion_Object=MibScalar
dellrcsg2TrapObjectImageCurrentVersion=_Dellrcsg2TrapObjectImageCurrentVersion_Object((1,3,6,1,4,1,10418,18,22,6,5),_Dellrcsg2TrapObjectImageCurrentVersion_Type())
dellrcsg2TrapObjectImageCurrentVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectImageCurrentVersion.setStatus(_D)
class _Dellrcsg2TrapObjectSessionIdentifier_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectSessionIdentifier_Type.__name__=_H
_Dellrcsg2TrapObjectSessionIdentifier_Object=MibScalar
dellrcsg2TrapObjectSessionIdentifier=_Dellrcsg2TrapObjectSessionIdentifier_Object((1,3,6,1,4,1,10418,18,22,6,6),_Dellrcsg2TrapObjectSessionIdentifier_Type())
dellrcsg2TrapObjectSessionIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectSessionIdentifier.setStatus(_D)
class _Dellrcsg2TrapObjectSIPId_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectSIPId_Type.__name__=_H
_Dellrcsg2TrapObjectSIPId_Object=MibScalar
dellrcsg2TrapObjectSIPId=_Dellrcsg2TrapObjectSIPId_Object((1,3,6,1,4,1,10418,18,22,6,7),_Dellrcsg2TrapObjectSIPId_Type())
dellrcsg2TrapObjectSIPId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectSIPId.setStatus(_D)
class _Dellrcsg2TrapObjectTieredSwitchName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Dellrcsg2TrapObjectTieredSwitchName_Type.__name__=_H
_Dellrcsg2TrapObjectTieredSwitchName_Object=MibScalar
dellrcsg2TrapObjectTieredSwitchName=_Dellrcsg2TrapObjectTieredSwitchName_Object((1,3,6,1,4,1,10418,18,22,6,8),_Dellrcsg2TrapObjectTieredSwitchName_Type())
dellrcsg2TrapObjectTieredSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectTieredSwitchName.setStatus(_D)
class _Dellrcsg2TrapObjectOldTieredSwitchName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Dellrcsg2TrapObjectOldTieredSwitchName_Type.__name__=_H
_Dellrcsg2TrapObjectOldTieredSwitchName_Object=MibScalar
dellrcsg2TrapObjectOldTieredSwitchName=_Dellrcsg2TrapObjectOldTieredSwitchName_Object((1,3,6,1,4,1,10418,18,22,6,9),_Dellrcsg2TrapObjectOldTieredSwitchName_Type())
dellrcsg2TrapObjectOldTieredSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectOldTieredSwitchName.setStatus(_D)
class _Dellrcsg2TrapObjectTargetDeviceName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Dellrcsg2TrapObjectTargetDeviceName_Type.__name__=_H
_Dellrcsg2TrapObjectTargetDeviceName_Object=MibScalar
dellrcsg2TrapObjectTargetDeviceName=_Dellrcsg2TrapObjectTargetDeviceName_Object((1,3,6,1,4,1,10418,18,22,6,10),_Dellrcsg2TrapObjectTargetDeviceName_Type())
dellrcsg2TrapObjectTargetDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectTargetDeviceName.setStatus(_D)
class _Dellrcsg2TrapObjectOldTargetDeviceName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Dellrcsg2TrapObjectOldTargetDeviceName_Type.__name__=_H
_Dellrcsg2TrapObjectOldTargetDeviceName_Object=MibScalar
dellrcsg2TrapObjectOldTargetDeviceName=_Dellrcsg2TrapObjectOldTargetDeviceName_Object((1,3,6,1,4,1,10418,18,22,6,11),_Dellrcsg2TrapObjectOldTargetDeviceName_Type())
dellrcsg2TrapObjectOldTargetDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectOldTargetDeviceName.setStatus(_D)
class _Dellrcsg2TrapObjectFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dellrcsg2TrapObjectFileName_Type.__name__=_N
_Dellrcsg2TrapObjectFileName_Object=MibScalar
dellrcsg2TrapObjectFileName=_Dellrcsg2TrapObjectFileName_Object((1,3,6,1,4,1,10418,18,22,6,12),_Dellrcsg2TrapObjectFileName_Type())
dellrcsg2TrapObjectFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectFileName.setStatus(_D)
class _Dellrcsg2TrapObjectLockReason_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dellrcsg2TrapObjectLockReason_Type.__name__=_H
_Dellrcsg2TrapObjectLockReason_Object=MibScalar
dellrcsg2TrapObjectLockReason=_Dellrcsg2TrapObjectLockReason_Object((1,3,6,1,4,1,10418,18,22,6,13),_Dellrcsg2TrapObjectLockReason_Type())
dellrcsg2TrapObjectLockReason.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectLockReason.setStatus(_D)
class _Dellrcsg2TrapObjectUnlockReason_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dellrcsg2TrapObjectUnlockReason_Type.__name__=_H
_Dellrcsg2TrapObjectUnlockReason_Object=MibScalar
dellrcsg2TrapObjectUnlockReason=_Dellrcsg2TrapObjectUnlockReason_Object((1,3,6,1,4,1,10418,18,22,6,14),_Dellrcsg2TrapObjectUnlockReason_Type())
dellrcsg2TrapObjectUnlockReason.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectUnlockReason.setStatus(_D)
class _Dellrcsg2TrapObjectUserAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_Dellrcsg2TrapObjectUserAddress_Type.__name__=_N
_Dellrcsg2TrapObjectUserAddress_Object=MibScalar
dellrcsg2TrapObjectUserAddress=_Dellrcsg2TrapObjectUserAddress_Object((1,3,6,1,4,1,10418,18,22,6,15),_Dellrcsg2TrapObjectUserAddress_Type())
dellrcsg2TrapObjectUserAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectUserAddress.setStatus(_D)
_Dellrcsg2TrapObjectSIPImageUpgradeResult_Type=SIPUpgradeResultsEnum
_Dellrcsg2TrapObjectSIPImageUpgradeResult_Object=MibScalar
dellrcsg2TrapObjectSIPImageUpgradeResult=_Dellrcsg2TrapObjectSIPImageUpgradeResult_Object((1,3,6,1,4,1,10418,18,22,6,16),_Dellrcsg2TrapObjectSIPImageUpgradeResult_Type())
dellrcsg2TrapObjectSIPImageUpgradeResult.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectSIPImageUpgradeResult.setStatus(_D)
class _Dellrcsg2TrapObjectTypeOfImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('boot',1),('app',2)))
_Dellrcsg2TrapObjectTypeOfImage_Type.__name__=_O
_Dellrcsg2TrapObjectTypeOfImage_Object=MibScalar
dellrcsg2TrapObjectTypeOfImage=_Dellrcsg2TrapObjectTypeOfImage_Object((1,3,6,1,4,1,10418,18,22,6,17),_Dellrcsg2TrapObjectTypeOfImage_Type())
dellrcsg2TrapObjectTypeOfImage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectTypeOfImage.setStatus(_D)
class _Dellrcsg2TrapObjectVirtualMediaDriveAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readonly',1),('readwrite',2)))
_Dellrcsg2TrapObjectVirtualMediaDriveAccessMode_Type.__name__=_O
_Dellrcsg2TrapObjectVirtualMediaDriveAccessMode_Object=MibScalar
dellrcsg2TrapObjectVirtualMediaDriveAccessMode=_Dellrcsg2TrapObjectVirtualMediaDriveAccessMode_Object((1,3,6,1,4,1,10418,18,22,6,18),_Dellrcsg2TrapObjectVirtualMediaDriveAccessMode_Type())
dellrcsg2TrapObjectVirtualMediaDriveAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectVirtualMediaDriveAccessMode.setStatus(_D)
class _Dellrcsg2TrapObjectVirtualMediaDriveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('floppyMemoryKey',1),('cdDvdRom',2),('generic',3)))
_Dellrcsg2TrapObjectVirtualMediaDriveType_Type.__name__=_O
_Dellrcsg2TrapObjectVirtualMediaDriveType_Object=MibScalar
dellrcsg2TrapObjectVirtualMediaDriveType=_Dellrcsg2TrapObjectVirtualMediaDriveType_Object((1,3,6,1,4,1,10418,18,22,6,19),_Dellrcsg2TrapObjectVirtualMediaDriveType_Type())
dellrcsg2TrapObjectVirtualMediaDriveType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectVirtualMediaDriveType.setStatus(_D)
_Dellrcsg2TrapObjectImageFileUpgradeResult_Type=ImageFileUpgradeResultsEnum
_Dellrcsg2TrapObjectImageFileUpgradeResult_Object=MibScalar
dellrcsg2TrapObjectImageFileUpgradeResult=_Dellrcsg2TrapObjectImageFileUpgradeResult_Object((1,3,6,1,4,1,10418,18,22,6,20),_Dellrcsg2TrapObjectImageFileUpgradeResult_Type())
dellrcsg2TrapObjectImageFileUpgradeResult.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectImageFileUpgradeResult.setStatus(_D)
class _Dellrcsg2TrapObjectPduDevicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Dellrcsg2TrapObjectPduDevicePort_Type.__name__=_O
_Dellrcsg2TrapObjectPduDevicePort_Object=MibScalar
dellrcsg2TrapObjectPduDevicePort=_Dellrcsg2TrapObjectPduDevicePort_Object((1,3,6,1,4,1,10418,18,22,6,21),_Dellrcsg2TrapObjectPduDevicePort_Type())
dellrcsg2TrapObjectPduDevicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPduDevicePort.setStatus(_D)
class _Dellrcsg2TrapObjectPduOutlet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Dellrcsg2TrapObjectPduOutlet_Type.__name__=_O
_Dellrcsg2TrapObjectPduOutlet_Object=MibScalar
dellrcsg2TrapObjectPduOutlet=_Dellrcsg2TrapObjectPduOutlet_Object((1,3,6,1,4,1,10418,18,22,6,22),_Dellrcsg2TrapObjectPduOutlet_Type())
dellrcsg2TrapObjectPduOutlet.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPduOutlet.setStatus(_D)
class _Dellrcsg2TrapObjectOldName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dellrcsg2TrapObjectOldName_Type.__name__=_H
_Dellrcsg2TrapObjectOldName_Object=MibScalar
dellrcsg2TrapObjectOldName=_Dellrcsg2TrapObjectOldName_Object((1,3,6,1,4,1,10418,18,22,6,23),_Dellrcsg2TrapObjectOldName_Type())
dellrcsg2TrapObjectOldName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectOldName.setStatus(_D)
class _Dellrcsg2TrapObjectItemName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dellrcsg2TrapObjectItemName_Type.__name__=_H
_Dellrcsg2TrapObjectItemName_Object=MibScalar
dellrcsg2TrapObjectItemName=_Dellrcsg2TrapObjectItemName_Object((1,3,6,1,4,1,10418,18,22,6,24),_Dellrcsg2TrapObjectItemName_Type())
dellrcsg2TrapObjectItemName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectItemName.setStatus(_D)
_Dellrcsg2TrapObjectPduDeviceInlet_Type=Integer32
_Dellrcsg2TrapObjectPduDeviceInlet_Object=MibScalar
dellrcsg2TrapObjectPduDeviceInlet=_Dellrcsg2TrapObjectPduDeviceInlet_Object((1,3,6,1,4,1,10418,18,22,6,25),_Dellrcsg2TrapObjectPduDeviceInlet_Type())
dellrcsg2TrapObjectPduDeviceInlet.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPduDeviceInlet.setStatus(_D)
_Dellrcsg2TrapObjectPduDeviceNumber_Type=Integer32
_Dellrcsg2TrapObjectPduDeviceNumber_Object=MibScalar
dellrcsg2TrapObjectPduDeviceNumber=_Dellrcsg2TrapObjectPduDeviceNumber_Object((1,3,6,1,4,1,10418,18,22,6,26),_Dellrcsg2TrapObjectPduDeviceNumber_Type())
dellrcsg2TrapObjectPduDeviceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPduDeviceNumber.setStatus(_D)
_Dellrcsg2TrapObjectInputPort_Type=Integer32
_Dellrcsg2TrapObjectInputPort_Object=MibScalar
dellrcsg2TrapObjectInputPort=_Dellrcsg2TrapObjectInputPort_Object((1,3,6,1,4,1,10418,18,22,6,27),_Dellrcsg2TrapObjectInputPort_Type())
dellrcsg2TrapObjectInputPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectInputPort.setStatus(_D)
_Dellrcsg2TrapObjectOldInputPort_Type=Integer32
_Dellrcsg2TrapObjectOldInputPort_Object=MibScalar
dellrcsg2TrapObjectOldInputPort=_Dellrcsg2TrapObjectOldInputPort_Object((1,3,6,1,4,1,10418,18,22,6,28),_Dellrcsg2TrapObjectOldInputPort_Type())
dellrcsg2TrapObjectOldInputPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectOldInputPort.setStatus(_D)
class _Dellrcsg2TrapObjectPowerSupply_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_Dellrcsg2TrapObjectPowerSupply_Type.__name__=_N
_Dellrcsg2TrapObjectPowerSupply_Object=MibScalar
dellrcsg2TrapObjectPowerSupply=_Dellrcsg2TrapObjectPowerSupply_Object((1,3,6,1,4,1,10418,18,22,6,29),_Dellrcsg2TrapObjectPowerSupply_Type())
dellrcsg2TrapObjectPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPowerSupply.setStatus(_D)
class _Dellrcsg2TrapObjectPreviousScreenResolution_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectPreviousScreenResolution_Type.__name__=_N
_Dellrcsg2TrapObjectPreviousScreenResolution_Object=MibScalar
dellrcsg2TrapObjectPreviousScreenResolution=_Dellrcsg2TrapObjectPreviousScreenResolution_Object((1,3,6,1,4,1,10418,18,22,6,30),_Dellrcsg2TrapObjectPreviousScreenResolution_Type())
dellrcsg2TrapObjectPreviousScreenResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPreviousScreenResolution.setStatus(_D)
class _Dellrcsg2TrapObjectCurrentScreenResolution_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dellrcsg2TrapObjectCurrentScreenResolution_Type.__name__=_N
_Dellrcsg2TrapObjectCurrentScreenResolution_Object=MibScalar
dellrcsg2TrapObjectCurrentScreenResolution=_Dellrcsg2TrapObjectCurrentScreenResolution_Object((1,3,6,1,4,1,10418,18,22,6,31),_Dellrcsg2TrapObjectCurrentScreenResolution_Type())
dellrcsg2TrapObjectCurrentScreenResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectCurrentScreenResolution.setStatus(_D)
class _Dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,5122))
_Dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged_Type.__name__=_d
_Dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged_Object=MibScalar
dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged=_Dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged_Object((1,3,6,1,4,1,10418,18,22,6,32),_Dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged_Type())
dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged.setStatus(_D)
_Dellrcsg2TrapObjectPduDeviceCircuit_Type=Integer32
_Dellrcsg2TrapObjectPduDeviceCircuit_Object=MibScalar
dellrcsg2TrapObjectPduDeviceCircuit=_Dellrcsg2TrapObjectPduDeviceCircuit_Object((1,3,6,1,4,1,10418,18,22,6,33),_Dellrcsg2TrapObjectPduDeviceCircuit_Type())
dellrcsg2TrapObjectPduDeviceCircuit.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectPduDeviceCircuit.setStatus(_D)
class _Dellrcsg2TrapObjectSessionType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Dellrcsg2TrapObjectSessionType_Type.__name__=_N
_Dellrcsg2TrapObjectSessionType_Object=MibScalar
dellrcsg2TrapObjectSessionType=_Dellrcsg2TrapObjectSessionType_Object((1,3,6,1,4,1,10418,18,22,6,34),_Dellrcsg2TrapObjectSessionType_Type())
dellrcsg2TrapObjectSessionType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellrcsg2TrapObjectSessionType.setStatus(_D)
dellrcsg2RebootStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,1))
dellrcsg2RebootStartedTrap.setObjects((_A,_B))
if mibBuilder.loadTexts:dellrcsg2RebootStartedTrap.setStatus('')
dellrcsg2UserLoginTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,2))
dellrcsg2UserLoginTrap.setObjects((_A,_B))
if mibBuilder.loadTexts:dellrcsg2UserLoginTrap.setStatus('')
dellrcsg2UserLogoutTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,3))
dellrcsg2UserLogoutTrap.setObjects((_A,_B))
if mibBuilder.loadTexts:dellrcsg2UserLogoutTrap.setStatus('')
dellrcsg2TargetSessionStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,4))
dellrcsg2TargetSessionStartedTrap.setObjects(*((_A,_B),(_A,_L),(_A,_J),(_A,_W)))
if mibBuilder.loadTexts:dellrcsg2TargetSessionStartedTrap.setStatus('')
dellrcsg2TargetSessionStoppedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,5))
dellrcsg2TargetSessionStoppedTrap.setObjects(*((_A,_B),(_A,_L),(_A,_J),(_A,_W)))
if mibBuilder.loadTexts:dellrcsg2TargetSessionStoppedTrap.setStatus('')
dellrcsg2TargetSessionTerminatedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,6))
dellrcsg2TargetSessionTerminatedTrap.setObjects(*((_A,_B),(_A,_M),(_A,_L),(_A,_J),(_A,_W)))
if mibBuilder.loadTexts:dellrcsg2TargetSessionTerminatedTrap.setStatus('')
dellrcsg2LocalPortSessionStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,7))
dellrcsg2LocalPortSessionStartedTrap.setObjects((_A,_L))
if mibBuilder.loadTexts:dellrcsg2LocalPortSessionStartedTrap.setStatus('')
dellrcsg2LocalPortSessionStoppedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,8))
dellrcsg2LocalPortSessionStoppedTrap.setObjects((_A,_L))
if mibBuilder.loadTexts:dellrcsg2LocalPortSessionStoppedTrap.setStatus('')
dellrcsg2LocalPortSessionTerminatedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,9))
dellrcsg2LocalPortSessionTerminatedTrap.setObjects(*((_A,_B),(_A,_L)))
if mibBuilder.loadTexts:dellrcsg2LocalPortSessionTerminatedTrap.setStatus('')
dellrcsg2ImageFileUpgradeStarted=NotificationType((1,3,6,1,4,1,10418,18,21,0,10))
dellrcsg2ImageFileUpgradeStarted.setObjects(*((_A,_B),(_A,_X),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:dellrcsg2ImageFileUpgradeStarted.setStatus('')
dellrcsg2ImageFileUpgradeResultsTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,11))
dellrcsg2ImageFileUpgradeResultsTrap.setObjects((_A,_a))
if mibBuilder.loadTexts:dellrcsg2ImageFileUpgradeResultsTrap.setStatus('')
dellrcsg2UserAddedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,12))
dellrcsg2UserAddedTrap.setObjects(*((_A,_B),(_A,_M)))
if mibBuilder.loadTexts:dellrcsg2UserAddedTrap.setStatus('')
dellrcsg2UserDeletedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,13))
dellrcsg2UserDeletedTrap.setObjects(*((_A,_B),(_A,_M)))
if mibBuilder.loadTexts:dellrcsg2UserDeletedTrap.setStatus('')
dellrcsg2UserModifiedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,14))
dellrcsg2UserModifiedTrap.setObjects(*((_A,_B),(_A,_M)))
if mibBuilder.loadTexts:dellrcsg2UserModifiedTrap.setStatus('')
dellrcsg2UserLockedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,15))
dellrcsg2UserLockedTrap.setObjects(*((_A,_M),(_A,_f)))
if mibBuilder.loadTexts:dellrcsg2UserLockedTrap.setStatus('')
dellrcsg2UserUnlockedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,16))
dellrcsg2UserUnlockedTrap.setObjects(*((_A,_B),(_A,_M),(_A,_g)))
if mibBuilder.loadTexts:dellrcsg2UserUnlockedTrap.setStatus('')
dellrcsg2UserAuthenticationFailureTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,17))
dellrcsg2UserAuthenticationFailureTrap.setObjects((_A,_B))
if mibBuilder.loadTexts:dellrcsg2UserAuthenticationFailureTrap.setStatus('')
dellrcsg2SIPAddedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,18))
dellrcsg2SIPAddedTrap.setObjects((_A,_K))
if mibBuilder.loadTexts:dellrcsg2SIPAddedTrap.setStatus('')
dellrcsg2SIPRemovedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,19))
dellrcsg2SIPRemovedTrap.setObjects((_A,_K))
if mibBuilder.loadTexts:dellrcsg2SIPRemovedTrap.setStatus('')
dellrcsg2SIPMovedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,20))
dellrcsg2SIPMovedTrap.setObjects(*((_A,_K),(_A,_E),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:dellrcsg2SIPMovedTrap.setStatus('')
dellrcsg2TargetDeviceNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,21))
dellrcsg2TargetDeviceNameChangedTrap.setObjects(*((_A,_j),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2TargetDeviceNameChangedTrap.setStatus('')
dellrcsg2TieredSwitchAddedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,22))
dellrcsg2TieredSwitchAddedTrap.setObjects(*((_A,_Y),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2TieredSwitchAddedTrap.setStatus('')
dellrcsg2TieredSwitchRemovedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,23))
dellrcsg2TieredSwitchRemovedTrap.setObjects(*((_A,_Y),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2TieredSwitchRemovedTrap.setStatus('')
dellrcsg2TieredSwitchNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,24))
dellrcsg2TieredSwitchNameChangedTrap.setObjects(*((_A,_k),(_A,_Y),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2TieredSwitchNameChangedTrap.setStatus('')
dellrcsg2ConfigurationFileLoadedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,25))
dellrcsg2ConfigurationFileLoadedTrap.setObjects(*((_A,_B),(_A,_X)))
if mibBuilder.loadTexts:dellrcsg2ConfigurationFileLoadedTrap.setStatus('')
dellrcsg2UserDatabaseFileLoadedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,26))
dellrcsg2UserDatabaseFileLoadedTrap.setObjects(*((_A,_B),(_A,_X)))
if mibBuilder.loadTexts:dellrcsg2UserDatabaseFileLoadedTrap.setStatus('')
dellrcsg2CaCertificateLoaded=NotificationType((1,3,6,1,4,1,10418,18,21,0,27))
dellrcsg2CaCertificateLoaded.setObjects((_A,_B))
if mibBuilder.loadTexts:dellrcsg2CaCertificateLoaded.setStatus('')
dellrcsg2SIPImageUpgradeStarted=NotificationType((1,3,6,1,4,1,10418,18,21,0,28))
dellrcsg2SIPImageUpgradeStarted.setObjects(*((_A,_B),(_A,_T),(_A,_P),(_A,_Q),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2SIPImageUpgradeStarted.setStatus('')
dellrcsg2SIPImageUpgradeResultTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,29))
dellrcsg2SIPImageUpgradeResultTrap.setObjects(*((_A,_l),(_A,_M),(_A,_T),(_A,_P),(_A,_Q),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2SIPImageUpgradeResultTrap.setStatus('')
dellrcsg2SIPRestartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,30))
dellrcsg2SIPRestartedTrap.setObjects(*((_A,_E),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2SIPRestartedTrap.setStatus('')
dellrcsg2VirtualMediaSessionStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,31))
dellrcsg2VirtualMediaSessionStartedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_K),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaSessionStartedTrap.setStatus('')
dellrcsg2VirtualMediaSessionStoppedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,32))
dellrcsg2VirtualMediaSessionStoppedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaSessionStoppedTrap.setStatus('')
dellrcsg2VirtualMediaSessionTerminatedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,33))
dellrcsg2VirtualMediaSessionTerminatedTrap.setObjects(*((_A,_B),(_A,_M),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaSessionTerminatedTrap.setStatus('')
dellrcsg2VirtualMediaSessionReservedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,34))
dellrcsg2VirtualMediaSessionReservedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaSessionReservedTrap.setStatus('')
dellrcsg2VirtualMediaSessionUnreservedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,35))
dellrcsg2VirtualMediaSessionUnreservedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaSessionUnreservedTrap.setStatus('')
dellrcsg2VirtualMediaDriveMapped=NotificationType((1,3,6,1,4,1,10418,18,21,0,36))
dellrcsg2VirtualMediaDriveMapped.setObjects(*((_A,_B),(_A,_E),(_A,_U),(_A,_V),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaDriveMapped.setStatus('')
dellrcsg2VirtualMediaDriveUnmapped=NotificationType((1,3,6,1,4,1,10418,18,21,0,37))
dellrcsg2VirtualMediaDriveUnmapped.setObjects(*((_A,_B),(_A,_E),(_A,_U),(_A,_V),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2VirtualMediaDriveUnmapped.setStatus('')
dellrcsg2LocalPortVirtualMediaSessionStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,38))
dellrcsg2LocalPortVirtualMediaSessionStartedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaSessionStartedTrap.setStatus('')
dellrcsg2LocalPortVirtualMediaSessionStoppedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,39))
dellrcsg2LocalPortVirtualMediaSessionStoppedTrap.setObjects(*((_A,_B),(_A,_E)))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaSessionStoppedTrap.setStatus('')
dellrcsg2LocalPortVirtualMediaSessionTerminatedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,40))
dellrcsg2LocalPortVirtualMediaSessionTerminatedTrap.setObjects(*((_A,_B),(_A,_E)))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaSessionTerminatedTrap.setStatus('')
dellrcsg2LocalPortVirtualMediaDriveMapped=NotificationType((1,3,6,1,4,1,10418,18,21,0,41))
dellrcsg2LocalPortVirtualMediaDriveMapped.setObjects(*((_A,_L),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaDriveMapped.setStatus('')
dellrcsg2LocalPortVirtualMediaDriveUnmapped=NotificationType((1,3,6,1,4,1,10418,18,21,0,42))
dellrcsg2LocalPortVirtualMediaDriveUnmapped.setObjects(*((_A,_L),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaDriveUnmapped.setStatus('')
dellrcsg2LocalPortVirtualMediaSessionReservedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,43))
dellrcsg2LocalPortVirtualMediaSessionReservedTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaSessionReservedTrap.setStatus('')
dellrcsg2LocalPortVirtualMediaSessionUnreservedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,44))
dellrcsg2LocalPortVirtualMediaSessionUnreservedTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:dellrcsg2LocalPortVirtualMediaSessionUnreservedTrap.setStatus('')
dellrcsg2ScreenResolutionChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,45))
dellrcsg2ScreenResolutionChangedTrap.setObjects(*((_A,_B),(_A,_E),(_A,_m),(_A,_n),(_A,_L)))
if mibBuilder.loadTexts:dellrcsg2ScreenResolutionChangedTrap.setStatus('')
dellrcsg2AggregatedTargetDeviceStatusChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,46))
dellrcsg2AggregatedTargetDeviceStatusChangedTrap.setObjects((_A,_o))
if mibBuilder.loadTexts:dellrcsg2AggregatedTargetDeviceStatusChangedTrap.setStatus('')
dellrcsg2FactoryDefaultsSetTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,47))
if mibBuilder.loadTexts:dellrcsg2FactoryDefaultsSetTrap.setStatus('')
dellrcsg2PowerSupplyFailureTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,48))
dellrcsg2PowerSupplyFailureTrap.setObjects((_A,_b))
if mibBuilder.loadTexts:dellrcsg2PowerSupplyFailureTrap.setStatus('')
dellrcsg2PowerSupplyRestoredTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,49))
dellrcsg2PowerSupplyRestoredTrap.setObjects((_A,_b))
if mibBuilder.loadTexts:dellrcsg2PowerSupplyRestoredTrap.setStatus('')
dellrcsg2PduDeviceOnlineTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,50))
dellrcsg2PduDeviceOnlineTrap.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduDeviceOnlineTrap.setStatus('')
dellrcsg2PduDeviceOfflineTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,51))
dellrcsg2PduDeviceOfflineTrap.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduDeviceOfflineTrap.setStatus('')
dellrcsg2PduOutletOnCommandTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,52))
dellrcsg2PduOutletOnCommandTrap.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletOnCommandTrap.setStatus('')
dellrcsg2PduOutletOffCommandTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,53))
dellrcsg2PduOutletOffCommandTrap.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletOffCommandTrap.setStatus('')
dellrcsg2PduOutletRebootCommandTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,54))
dellrcsg2PduOutletRebootCommandTrap.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletRebootCommandTrap.setStatus('')
dellrcsg2PduOutletOnSenseFailTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,55))
dellrcsg2PduOutletOnSenseFailTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletOnSenseFailTrap.setStatus('')
dellrcsg2PduOutletOffSenseFailTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,56))
dellrcsg2PduOutletOffSenseFailTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletOffSenseFailTrap.setStatus('')
dellrcsg2PduStatusOutletOnTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,57))
dellrcsg2PduStatusOutletOnTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduStatusOutletOnTrap.setStatus('')
dellrcsg2PduStatusOutletOffTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,58))
dellrcsg2PduStatusOutletOffTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduStatusOutletOffTrap.setStatus('')
dellrcsg2PduPortNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,59))
dellrcsg2PduPortNameChangedTrap.setObjects(*((_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduPortNameChangedTrap.setStatus('')
dellrcsg2PduOutletNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,60))
dellrcsg2PduOutletNameChangedTrap.setObjects(*((_A,_R),(_A,_S),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletNameChangedTrap.setStatus('')
dellrcsg2PduInletTotalLoadHighTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,61))
dellrcsg2PduInletTotalLoadHighTrap.setObjects(*((_A,_F),(_A,_G),(_A,_Z)))
if mibBuilder.loadTexts:dellrcsg2PduInletTotalLoadHighTrap.setStatus('')
dellrcsg2PduInletTotalLoadLowTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,62))
dellrcsg2PduInletTotalLoadLowTrap.setObjects(*((_A,_F),(_A,_G),(_A,_Z)))
if mibBuilder.loadTexts:dellrcsg2PduInletTotalLoadLowTrap.setStatus('')
dellrcsg2PduDeviceNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,63))
dellrcsg2PduDeviceNameChangedTrap.setObjects(*((_A,_R),(_A,_S),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduDeviceNameChangedTrap.setStatus('')
dellrcsg2PduInletNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,64))
dellrcsg2PduInletNameChangedTrap.setObjects(*((_A,_R),(_A,_S),(_A,_F),(_A,_G),(_A,_Z)))
if mibBuilder.loadTexts:dellrcsg2PduInletNameChangedTrap.setStatus('')
dellrcsg2PduOutletLockCommandTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,65))
dellrcsg2PduOutletLockCommandTrap.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletLockCommandTrap.setStatus('')
dellrcsg2PduOutletUnlockCommandTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,66))
dellrcsg2PduOutletUnlockCommandTrap.setObjects(*((_A,_B),(_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletUnlockCommandTrap.setStatus('')
dellrcsg2PduStatusOutletLockTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,67))
dellrcsg2PduStatusOutletLockTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduStatusOutletLockTrap.setStatus('')
dellrcsg2PduStatusOutletUnlockTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,68))
dellrcsg2PduStatusOutletUnlockTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduStatusOutletUnlockTrap.setStatus('')
dellrcsg2PduImageFileUpgradeStartedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,69))
dellrcsg2PduImageFileUpgradeStartedTrap.setObjects(*((_A,_B),(_A,_T),(_A,_P),(_A,_Q),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduImageFileUpgradeStartedTrap.setStatus('')
dellrcsg2PduImageFileUpgradeResultTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,70))
dellrcsg2PduImageFileUpgradeResultTrap.setObjects(*((_A,_a),(_A,_B),(_A,_T),(_A,_P),(_A,_Q),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduImageFileUpgradeResultTrap.setStatus('')
dellrcsg2PduCircuitNameChangedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,71))
dellrcsg2PduCircuitNameChangedTrap.setObjects(*((_A,_R),(_A,_S),(_A,_F),(_A,_G),(_A,_c)))
if mibBuilder.loadTexts:dellrcsg2PduCircuitNameChangedTrap.setStatus('')
dellrcsg2PduDeviceTotalLoadHighTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,72))
dellrcsg2PduDeviceTotalLoadHighTrap.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:dellrcsg2PduDeviceTotalLoadHighTrap.setStatus('')
dellrcsg2PduCircuitTotalLoadHighTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,73))
dellrcsg2PduCircuitTotalLoadHighTrap.setObjects(*((_A,_F),(_A,_G),(_A,_c)))
if mibBuilder.loadTexts:dellrcsg2PduCircuitTotalLoadHighTrap.setStatus('')
dellrcsg2PduOutletTotalLoadHighTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,74))
dellrcsg2PduOutletTotalLoadHighTrap.setObjects(*((_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:dellrcsg2PduOutletTotalLoadHighTrap.setStatus('')
dellrcsg2FanFailureTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,75))
if mibBuilder.loadTexts:dellrcsg2FanFailureTrap.setStatus('')
dellrcsg2TemperatureRangeTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,76))
if mibBuilder.loadTexts:dellrcsg2TemperatureRangeTrap.setStatus('')
dellrcsg2SmartCardInsertedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,77))
dellrcsg2SmartCardInsertedTrap.setObjects(*((_A,_B),(_A,_L),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2SmartCardInsertedTrap.setStatus('')
dellrcsg2SmartCardRemovedTrap=NotificationType((1,3,6,1,4,1,10418,18,21,0,78))
dellrcsg2SmartCardRemovedTrap.setObjects(*((_A,_B),(_A,_L),(_A,_J)))
if mibBuilder.loadTexts:dellrcsg2SmartCardRemovedTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{_H:UTF8String,'ImageFileUpgradeResultsEnum':ImageFileUpgradeResultsEnum,'SIPUpgradeResultsEnum':SIPUpgradeResultsEnum,'dell':dell,'dellrcsg2':dellrcsg2,'dellrcsg2Products':dellrcsg2Products,'dellrcsg2RebootStartedTrap':dellrcsg2RebootStartedTrap,'dellrcsg2UserLoginTrap':dellrcsg2UserLoginTrap,'dellrcsg2UserLogoutTrap':dellrcsg2UserLogoutTrap,'dellrcsg2TargetSessionStartedTrap':dellrcsg2TargetSessionStartedTrap,'dellrcsg2TargetSessionStoppedTrap':dellrcsg2TargetSessionStoppedTrap,'dellrcsg2TargetSessionTerminatedTrap':dellrcsg2TargetSessionTerminatedTrap,'dellrcsg2LocalPortSessionStartedTrap':dellrcsg2LocalPortSessionStartedTrap,'dellrcsg2LocalPortSessionStoppedTrap':dellrcsg2LocalPortSessionStoppedTrap,'dellrcsg2LocalPortSessionTerminatedTrap':dellrcsg2LocalPortSessionTerminatedTrap,'dellrcsg2ImageFileUpgradeStarted':dellrcsg2ImageFileUpgradeStarted,'dellrcsg2ImageFileUpgradeResultsTrap':dellrcsg2ImageFileUpgradeResultsTrap,'dellrcsg2UserAddedTrap':dellrcsg2UserAddedTrap,'dellrcsg2UserDeletedTrap':dellrcsg2UserDeletedTrap,'dellrcsg2UserModifiedTrap':dellrcsg2UserModifiedTrap,'dellrcsg2UserLockedTrap':dellrcsg2UserLockedTrap,'dellrcsg2UserUnlockedTrap':dellrcsg2UserUnlockedTrap,'dellrcsg2UserAuthenticationFailureTrap':dellrcsg2UserAuthenticationFailureTrap,'dellrcsg2SIPAddedTrap':dellrcsg2SIPAddedTrap,'dellrcsg2SIPRemovedTrap':dellrcsg2SIPRemovedTrap,'dellrcsg2SIPMovedTrap':dellrcsg2SIPMovedTrap,'dellrcsg2TargetDeviceNameChangedTrap':dellrcsg2TargetDeviceNameChangedTrap,'dellrcsg2TieredSwitchAddedTrap':dellrcsg2TieredSwitchAddedTrap,'dellrcsg2TieredSwitchRemovedTrap':dellrcsg2TieredSwitchRemovedTrap,'dellrcsg2TieredSwitchNameChangedTrap':dellrcsg2TieredSwitchNameChangedTrap,'dellrcsg2ConfigurationFileLoadedTrap':dellrcsg2ConfigurationFileLoadedTrap,'dellrcsg2UserDatabaseFileLoadedTrap':dellrcsg2UserDatabaseFileLoadedTrap,'dellrcsg2CaCertificateLoaded':dellrcsg2CaCertificateLoaded,'dellrcsg2SIPImageUpgradeStarted':dellrcsg2SIPImageUpgradeStarted,'dellrcsg2SIPImageUpgradeResultTrap':dellrcsg2SIPImageUpgradeResultTrap,'dellrcsg2SIPRestartedTrap':dellrcsg2SIPRestartedTrap,'dellrcsg2VirtualMediaSessionStartedTrap':dellrcsg2VirtualMediaSessionStartedTrap,'dellrcsg2VirtualMediaSessionStoppedTrap':dellrcsg2VirtualMediaSessionStoppedTrap,'dellrcsg2VirtualMediaSessionTerminatedTrap':dellrcsg2VirtualMediaSessionTerminatedTrap,'dellrcsg2VirtualMediaSessionReservedTrap':dellrcsg2VirtualMediaSessionReservedTrap,'dellrcsg2VirtualMediaSessionUnreservedTrap':dellrcsg2VirtualMediaSessionUnreservedTrap,'dellrcsg2VirtualMediaDriveMapped':dellrcsg2VirtualMediaDriveMapped,'dellrcsg2VirtualMediaDriveUnmapped':dellrcsg2VirtualMediaDriveUnmapped,'dellrcsg2LocalPortVirtualMediaSessionStartedTrap':dellrcsg2LocalPortVirtualMediaSessionStartedTrap,'dellrcsg2LocalPortVirtualMediaSessionStoppedTrap':dellrcsg2LocalPortVirtualMediaSessionStoppedTrap,'dellrcsg2LocalPortVirtualMediaSessionTerminatedTrap':dellrcsg2LocalPortVirtualMediaSessionTerminatedTrap,'dellrcsg2LocalPortVirtualMediaDriveMapped':dellrcsg2LocalPortVirtualMediaDriveMapped,'dellrcsg2LocalPortVirtualMediaDriveUnmapped':dellrcsg2LocalPortVirtualMediaDriveUnmapped,'dellrcsg2LocalPortVirtualMediaSessionReservedTrap':dellrcsg2LocalPortVirtualMediaSessionReservedTrap,'dellrcsg2LocalPortVirtualMediaSessionUnreservedTrap':dellrcsg2LocalPortVirtualMediaSessionUnreservedTrap,'dellrcsg2ScreenResolutionChangedTrap':dellrcsg2ScreenResolutionChangedTrap,'dellrcsg2AggregatedTargetDeviceStatusChangedTrap':dellrcsg2AggregatedTargetDeviceStatusChangedTrap,'dellrcsg2FactoryDefaultsSetTrap':dellrcsg2FactoryDefaultsSetTrap,'dellrcsg2PowerSupplyFailureTrap':dellrcsg2PowerSupplyFailureTrap,'dellrcsg2PowerSupplyRestoredTrap':dellrcsg2PowerSupplyRestoredTrap,'dellrcsg2PduDeviceOnlineTrap':dellrcsg2PduDeviceOnlineTrap,'dellrcsg2PduDeviceOfflineTrap':dellrcsg2PduDeviceOfflineTrap,'dellrcsg2PduOutletOnCommandTrap':dellrcsg2PduOutletOnCommandTrap,'dellrcsg2PduOutletOffCommandTrap':dellrcsg2PduOutletOffCommandTrap,'dellrcsg2PduOutletRebootCommandTrap':dellrcsg2PduOutletRebootCommandTrap,'dellrcsg2PduOutletOnSenseFailTrap':dellrcsg2PduOutletOnSenseFailTrap,'dellrcsg2PduOutletOffSenseFailTrap':dellrcsg2PduOutletOffSenseFailTrap,'dellrcsg2PduStatusOutletOnTrap':dellrcsg2PduStatusOutletOnTrap,'dellrcsg2PduStatusOutletOffTrap':dellrcsg2PduStatusOutletOffTrap,'dellrcsg2PduPortNameChangedTrap':dellrcsg2PduPortNameChangedTrap,'dellrcsg2PduOutletNameChangedTrap':dellrcsg2PduOutletNameChangedTrap,'dellrcsg2PduInletTotalLoadHighTrap':dellrcsg2PduInletTotalLoadHighTrap,'dellrcsg2PduInletTotalLoadLowTrap':dellrcsg2PduInletTotalLoadLowTrap,'dellrcsg2PduDeviceNameChangedTrap':dellrcsg2PduDeviceNameChangedTrap,'dellrcsg2PduInletNameChangedTrap':dellrcsg2PduInletNameChangedTrap,'dellrcsg2PduOutletLockCommandTrap':dellrcsg2PduOutletLockCommandTrap,'dellrcsg2PduOutletUnlockCommandTrap':dellrcsg2PduOutletUnlockCommandTrap,'dellrcsg2PduStatusOutletLockTrap':dellrcsg2PduStatusOutletLockTrap,'dellrcsg2PduStatusOutletUnlockTrap':dellrcsg2PduStatusOutletUnlockTrap,'dellrcsg2PduImageFileUpgradeStartedTrap':dellrcsg2PduImageFileUpgradeStartedTrap,'dellrcsg2PduImageFileUpgradeResultTrap':dellrcsg2PduImageFileUpgradeResultTrap,'dellrcsg2PduCircuitNameChangedTrap':dellrcsg2PduCircuitNameChangedTrap,'dellrcsg2PduDeviceTotalLoadHighTrap':dellrcsg2PduDeviceTotalLoadHighTrap,'dellrcsg2PduCircuitTotalLoadHighTrap':dellrcsg2PduCircuitTotalLoadHighTrap,'dellrcsg2PduOutletTotalLoadHighTrap':dellrcsg2PduOutletTotalLoadHighTrap,'dellrcsg2FanFailureTrap':dellrcsg2FanFailureTrap,'dellrcsg2TemperatureRangeTrap':dellrcsg2TemperatureRangeTrap,'dellrcsg2SmartCardInsertedTrap':dellrcsg2SmartCardInsertedTrap,'dellrcsg2SmartCardRemovedTrap':dellrcsg2SmartCardRemovedTrap,'dellrcs1082ds':dellrcs1082ds,'dellrcs2162ds':dellrcs2162ds,'dellrcs4322ds':dellrcs4322ds,'dellrcsg2Management':dellrcsg2Management,'dellrcsg2TrapObject':dellrcsg2TrapObject,_B:dellrcsg2TrapObjectUserName,_M:dellrcsg2TrapObjectTargetUserName,'dellrcsg2TrapObjectImageType':dellrcsg2TrapObjectImageType,_P:dellrcsg2TrapObjectImageNewVersion,_Q:dellrcsg2TrapObjectImageCurrentVersion,_L:dellrcsg2TrapObjectSessionIdentifier,_K:dellrcsg2TrapObjectSIPId,_Y:dellrcsg2TrapObjectTieredSwitchName,_k:dellrcsg2TrapObjectOldTieredSwitchName,_E:dellrcsg2TrapObjectTargetDeviceName,_j:dellrcsg2TrapObjectOldTargetDeviceName,_X:dellrcsg2TrapObjectFileName,_f:dellrcsg2TrapObjectLockReason,_g:dellrcsg2TrapObjectUnlockReason,_J:dellrcsg2TrapObjectUserAddress,_l:dellrcsg2TrapObjectSIPImageUpgradeResult,_T:dellrcsg2TrapObjectTypeOfImage,_V:dellrcsg2TrapObjectVirtualMediaDriveAccessMode,_U:dellrcsg2TrapObjectVirtualMediaDriveType,_a:dellrcsg2TrapObjectImageFileUpgradeResult,_F:dellrcsg2TrapObjectPduDevicePort,_I:dellrcsg2TrapObjectPduOutlet,_R:dellrcsg2TrapObjectOldName,_S:dellrcsg2TrapObjectItemName,_Z:dellrcsg2TrapObjectPduDeviceInlet,_G:dellrcsg2TrapObjectPduDeviceNumber,_h:dellrcsg2TrapObjectInputPort,_i:dellrcsg2TrapObjectOldInputPort,_b:dellrcsg2TrapObjectPowerSupply,_m:dellrcsg2TrapObjectPreviousScreenResolution,_n:dellrcsg2TrapObjectCurrentScreenResolution,_o:dellrcsg2TrapObjectAggregatedTargetDeviceStatusChanged,_c:dellrcsg2TrapObjectPduDeviceCircuit,_W:dellrcsg2TrapObjectSessionType})