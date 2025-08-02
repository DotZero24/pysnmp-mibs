_G='NotificationType'
_F='OctetString'
_E='Integer32'
_D='DisplayString'
_C='UTF8String'
_B='mandatory'
_A='not-accessible'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class UTF8String(OctetString):0
class ImageFileUpgradeResultsEnum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,9999)));namedValues=NamedValues(*(('imageUpgradeTftpNoSocket',1),('imageUpgradeTftpConnectFailure',2),('imageUpgradeTftpRequestDenied',3),('imageUpgradeTftpBadPacket',4),('imageUpgradeTftpOOS',5),('imageUpgradeTftpTooBig',6),('imageUpgradeTftpTimeout',7),('imageUpgradeAlreadyInProgress',8),('imageUpgradeCannotStart',9),('imageUpgradeMemoryError',10),('imageUpgradeTftpProtocolError',11),('imageUpgradeBadType',12),('imageUpgradeInvalidAppDowngrade',13),('imageUpgradeChecksumError',14),('imageUpgradeFlashError',15),('imageUpgradeInternalError',16),('imageUpgradeFileNotFound',17),('imageUpgradeBadHeader',18),('imageUpgradeIncompatibleHeader',19),('imageUpgradeTftpXferFail',20),('imageUpgradeTftpSvrNoResponse',21),('imageUpgradeNetworkUnreachable',22),('imageUpgradeSuccess',9999)))
class IqAdaptorUpgradeResultsEnum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,9999)));namedValues=NamedValues(*(('iqaUpgradeNoFirmwareImage',1),('iqaUpgradeLostContact',2),('iqaUpgradeFailedRestart',3),('iqaUpgradeSuccess',9999)))
_Avocent_ObjectIdentity=ObjectIdentity
avocent=_Avocent_ObjectIdentity((1,3,6,1,4,1,10418))
_Dsr_ObjectIdentity=ObjectIdentity
dsr=_Dsr_ObjectIdentity((1,3,6,1,4,1,10418,7))
_DsrProducts_ObjectIdentity=ObjectIdentity
dsrProducts=_DsrProducts_ObjectIdentity((1,3,6,1,4,1,10418,7,1))
_DsrManagement_ObjectIdentity=ObjectIdentity
dsrManagement=_DsrManagement_ObjectIdentity((1,3,6,1,4,1,10418,7,2))
_DsrTrapObject_ObjectIdentity=ObjectIdentity
dsrTrapObject=_DsrTrapObject_ObjectIdentity((1,3,6,1,4,1,10418,7,2,6))
class _AvctDsrTrapObjectUserName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectUserName_Type.__name__=_C
_AvctDsrTrapObjectUserName_Object=MibScalar
avctDsrTrapObjectUserName=_AvctDsrTrapObjectUserName_Object((1,3,6,1,4,1,10418,7,2,6,1),_AvctDsrTrapObjectUserName_Type())
avctDsrTrapObjectUserName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectUserName.setStatus(_B)
class _AvctDsrTrapObjectTargetUserName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectTargetUserName_Type.__name__=_C
_AvctDsrTrapObjectTargetUserName_Object=MibScalar
avctDsrTrapObjectTargetUserName=_AvctDsrTrapObjectTargetUserName_Object((1,3,6,1,4,1,10418,7,2,6,2),_AvctDsrTrapObjectTargetUserName_Type())
avctDsrTrapObjectTargetUserName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectTargetUserName.setStatus(_B)
class _AvctDsrTrapObjectImageNewVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectImageNewVersion_Type.__name__=_D
_AvctDsrTrapObjectImageNewVersion_Object=MibScalar
avctDsrTrapObjectImageNewVersion=_AvctDsrTrapObjectImageNewVersion_Object((1,3,6,1,4,1,10418,7,2,6,4),_AvctDsrTrapObjectImageNewVersion_Type())
avctDsrTrapObjectImageNewVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectImageNewVersion.setStatus(_B)
class _AvctDsrTrapObjectImageCurrentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectImageCurrentVersion_Type.__name__=_D
_AvctDsrTrapObjectImageCurrentVersion_Object=MibScalar
avctDsrTrapObjectImageCurrentVersion=_AvctDsrTrapObjectImageCurrentVersion_Object((1,3,6,1,4,1,10418,7,2,6,5),_AvctDsrTrapObjectImageCurrentVersion_Type())
avctDsrTrapObjectImageCurrentVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectImageCurrentVersion.setStatus(_B)
class _AvctDsrTrapObjectServerName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectServerName_Type.__name__=_C
_AvctDsrTrapObjectServerName_Object=MibScalar
avctDsrTrapObjectServerName=_AvctDsrTrapObjectServerName_Object((1,3,6,1,4,1,10418,7,2,6,6),_AvctDsrTrapObjectServerName_Type())
avctDsrTrapObjectServerName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectServerName.setStatus(_B)
class _AvctDsrTrapObjectIqAdaptorId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectIqAdaptorId_Type.__name__=_D
_AvctDsrTrapObjectIqAdaptorId_Object=MibScalar
avctDsrTrapObjectIqAdaptorId=_AvctDsrTrapObjectIqAdaptorId_Object((1,3,6,1,4,1,10418,7,2,6,7),_AvctDsrTrapObjectIqAdaptorId_Type())
avctDsrTrapObjectIqAdaptorId.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectIqAdaptorId.setStatus(_B)
class _AvctDsrTrapObjectIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvctDsrTrapObjectIpAddress_Type.__name__=_D
_AvctDsrTrapObjectIpAddress_Object=MibScalar
avctDsrTrapObjectIpAddress=_AvctDsrTrapObjectIpAddress_Object((1,3,6,1,4,1,10418,7,2,6,9),_AvctDsrTrapObjectIpAddress_Type())
avctDsrTrapObjectIpAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectIpAddress.setStatus(_B)
class _AvctDsrTrapObjectPreviousScreenResolution_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectPreviousScreenResolution_Type.__name__=_D
_AvctDsrTrapObjectPreviousScreenResolution_Object=MibScalar
avctDsrTrapObjectPreviousScreenResolution=_AvctDsrTrapObjectPreviousScreenResolution_Object((1,3,6,1,4,1,10418,7,2,6,10),_AvctDsrTrapObjectPreviousScreenResolution_Type())
avctDsrTrapObjectPreviousScreenResolution.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectPreviousScreenResolution.setStatus(_B)
class _AvctDsrTrapObjectCurrentScreenResolution_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectCurrentScreenResolution_Type.__name__=_D
_AvctDsrTrapObjectCurrentScreenResolution_Object=MibScalar
avctDsrTrapObjectCurrentScreenResolution=_AvctDsrTrapObjectCurrentScreenResolution_Object((1,3,6,1,4,1,10418,7,2,6,11),_AvctDsrTrapObjectCurrentScreenResolution_Type())
avctDsrTrapObjectCurrentScreenResolution.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectCurrentScreenResolution.setStatus(_B)
class _AvctDsrTrapObjectAggregatedServerStatusChanged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,5122))
_AvctDsrTrapObjectAggregatedServerStatusChanged_Type.__name__=_F
_AvctDsrTrapObjectAggregatedServerStatusChanged_Object=MibScalar
avctDsrTrapObjectAggregatedServerStatusChanged=_AvctDsrTrapObjectAggregatedServerStatusChanged_Object((1,3,6,1,4,1,10418,7,2,6,12),_AvctDsrTrapObjectAggregatedServerStatusChanged_Type())
avctDsrTrapObjectAggregatedServerStatusChanged.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectAggregatedServerStatusChanged.setStatus(_B)
_AvctDsrTrapObjectImageFileUpgradeResult_Type=ImageFileUpgradeResultsEnum
_AvctDsrTrapObjectImageFileUpgradeResult_Object=MibScalar
avctDsrTrapObjectImageFileUpgradeResult=_AvctDsrTrapObjectImageFileUpgradeResult_Object((1,3,6,1,4,1,10418,7,2,6,13),_AvctDsrTrapObjectImageFileUpgradeResult_Type())
avctDsrTrapObjectImageFileUpgradeResult.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectImageFileUpgradeResult.setStatus(_B)
_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Type=IqAdaptorUpgradeResultsEnum
_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Object=MibScalar
avctDsrTrapObjectIqAdaptorImageUpgradeResult=_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Object((1,3,6,1,4,1,10418,7,2,6,14),_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Type())
avctDsrTrapObjectIqAdaptorImageUpgradeResult.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectIqAdaptorImageUpgradeResult.setStatus(_B)
class _AvctDsrTrapObjectTypeOfImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('boot',1),('app',2)))
_AvctDsrTrapObjectTypeOfImage_Type.__name__=_E
_AvctDsrTrapObjectTypeOfImage_Object=MibScalar
avctDsrTrapObjectTypeOfImage=_AvctDsrTrapObjectTypeOfImage_Object((1,3,6,1,4,1,10418,7,2,6,15),_AvctDsrTrapObjectTypeOfImage_Type())
avctDsrTrapObjectTypeOfImage.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectTypeOfImage.setStatus(_B)
_AvctDsrTrapObjectInputPort_Type=Integer32
_AvctDsrTrapObjectInputPort_Object=MibScalar
avctDsrTrapObjectInputPort=_AvctDsrTrapObjectInputPort_Object((1,3,6,1,4,1,10418,7,2,6,16),_AvctDsrTrapObjectInputPort_Type())
avctDsrTrapObjectInputPort.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectInputPort.setStatus(_B)
_AvctDsrTrapObjectSwitchChannel_Type=Integer32
_AvctDsrTrapObjectSwitchChannel_Object=MibScalar
avctDsrTrapObjectSwitchChannel=_AvctDsrTrapObjectSwitchChannel_Object((1,3,6,1,4,1,10418,7,2,6,17),_AvctDsrTrapObjectSwitchChannel_Type())
avctDsrTrapObjectSwitchChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSwitchChannel.setStatus(_B)
class _AvctDsrTrapObjectFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_AvctDsrTrapObjectFileName_Type.__name__=_D
_AvctDsrTrapObjectFileName_Object=MibScalar
avctDsrTrapObjectFileName=_AvctDsrTrapObjectFileName_Object((1,3,6,1,4,1,10418,7,2,6,18),_AvctDsrTrapObjectFileName_Type())
avctDsrTrapObjectFileName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectFileName.setStatus(_B)
_AvctDsrTrapObjectActiveSessions_Type=Integer32
_AvctDsrTrapObjectActiveSessions_Object=MibScalar
avctDsrTrapObjectActiveSessions=_AvctDsrTrapObjectActiveSessions_Object((1,3,6,1,4,1,10418,7,2,6,19),_AvctDsrTrapObjectActiveSessions_Type())
avctDsrTrapObjectActiveSessions.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectActiveSessions.setStatus(_B)
class _AvctDsrTrapObjectCascadeSwitchName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectCascadeSwitchName_Type.__name__=_C
_AvctDsrTrapObjectCascadeSwitchName_Object=MibScalar
avctDsrTrapObjectCascadeSwitchName=_AvctDsrTrapObjectCascadeSwitchName_Object((1,3,6,1,4,1,10418,7,2,6,20),_AvctDsrTrapObjectCascadeSwitchName_Type())
avctDsrTrapObjectCascadeSwitchName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectCascadeSwitchName.setStatus(_B)
class _AvctDsrTrapObjectOldCascadeSwitchName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectOldCascadeSwitchName_Type.__name__=_C
_AvctDsrTrapObjectOldCascadeSwitchName_Object=MibScalar
avctDsrTrapObjectOldCascadeSwitchName=_AvctDsrTrapObjectOldCascadeSwitchName_Object((1,3,6,1,4,1,10418,7,2,6,21),_AvctDsrTrapObjectOldCascadeSwitchName_Type())
avctDsrTrapObjectOldCascadeSwitchName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectOldCascadeSwitchName.setStatus(_B)
class _AvctDsrTrapObjectOldServerName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectOldServerName_Type.__name__=_C
_AvctDsrTrapObjectOldServerName_Object=MibScalar
avctDsrTrapObjectOldServerName=_AvctDsrTrapObjectOldServerName_Object((1,3,6,1,4,1,10418,7,2,6,22),_AvctDsrTrapObjectOldServerName_Type())
avctDsrTrapObjectOldServerName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectOldServerName.setStatus(_B)
class _AvctDsrTrapObjectSpcDeviceLocation_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectSpcDeviceLocation_Type.__name__=_C
_AvctDsrTrapObjectSpcDeviceLocation_Object=MibScalar
avctDsrTrapObjectSpcDeviceLocation=_AvctDsrTrapObjectSpcDeviceLocation_Object((1,3,6,1,4,1,10418,7,2,6,23),_AvctDsrTrapObjectSpcDeviceLocation_Type())
avctDsrTrapObjectSpcDeviceLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDeviceLocation.setStatus(_B)
class _AvctDsrTrapObjectSpcDevicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AvctDsrTrapObjectSpcDevicePort_Type.__name__=_E
_AvctDsrTrapObjectSpcDevicePort_Object=MibScalar
avctDsrTrapObjectSpcDevicePort=_AvctDsrTrapObjectSpcDevicePort_Object((1,3,6,1,4,1,10418,7,2,6,24),_AvctDsrTrapObjectSpcDevicePort_Type())
avctDsrTrapObjectSpcDevicePort.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDevicePort.setStatus(_B)
class _AvctDsrTrapObjectSpcDeviceLogin_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvctDsrTrapObjectSpcDeviceLogin_Type.__name__=_C
_AvctDsrTrapObjectSpcDeviceLogin_Object=MibScalar
avctDsrTrapObjectSpcDeviceLogin=_AvctDsrTrapObjectSpcDeviceLogin_Object((1,3,6,1,4,1,10418,7,2,6,25),_AvctDsrTrapObjectSpcDeviceLogin_Type())
avctDsrTrapObjectSpcDeviceLogin.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDeviceLogin.setStatus(_B)
class _AvctDsrTrapObjectSpcSocket_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AvctDsrTrapObjectSpcSocket_Type.__name__=_E
_AvctDsrTrapObjectSpcSocket_Object=MibScalar
avctDsrTrapObjectSpcSocket=_AvctDsrTrapObjectSpcSocket_Object((1,3,6,1,4,1,10418,7,2,6,26),_AvctDsrTrapObjectSpcSocket_Type())
avctDsrTrapObjectSpcSocket.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcSocket.setStatus(_B)
class _AvctDsrTrapObjectOldName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectOldName_Type.__name__=_C
_AvctDsrTrapObjectOldName_Object=MibScalar
avctDsrTrapObjectOldName=_AvctDsrTrapObjectOldName_Object((1,3,6,1,4,1,10418,7,2,6,27),_AvctDsrTrapObjectOldName_Type())
avctDsrTrapObjectOldName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectOldName.setStatus(_B)
class _AvctDsrTrapObjectItemName_Type(UTF8String):subtypeSpec=UTF8String.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvctDsrTrapObjectItemName_Type.__name__=_C
_AvctDsrTrapObjectItemName_Object=MibScalar
avctDsrTrapObjectItemName=_AvctDsrTrapObjectItemName_Object((1,3,6,1,4,1,10418,7,2,6,28),_AvctDsrTrapObjectItemName_Type())
avctDsrTrapObjectItemName.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectItemName.setStatus(_B)
_AvctDsrTrapObjectSpcDeviceInlet_Type=Integer32
_AvctDsrTrapObjectSpcDeviceInlet_Object=MibScalar
avctDsrTrapObjectSpcDeviceInlet=_AvctDsrTrapObjectSpcDeviceInlet_Object((1,3,6,1,4,1,10418,7,2,6,29),_AvctDsrTrapObjectSpcDeviceInlet_Type())
avctDsrTrapObjectSpcDeviceInlet.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDeviceInlet.setStatus(_B)
_AvctDsrTrapObjectSpcDeviceNumber_Type=Integer32
_AvctDsrTrapObjectSpcDeviceNumber_Object=MibScalar
avctDsrTrapObjectSpcDeviceNumber=_AvctDsrTrapObjectSpcDeviceNumber_Object((1,3,6,1,4,1,10418,7,2,6,30),_AvctDsrTrapObjectSpcDeviceNumber_Type())
avctDsrTrapObjectSpcDeviceNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDeviceNumber.setStatus(_B)
_AvctDsrTrapObjectOldInputPort_Type=Integer32
_AvctDsrTrapObjectOldInputPort_Object=MibScalar
avctDsrTrapObjectOldInputPort=_AvctDsrTrapObjectOldInputPort_Object((1,3,6,1,4,1,10418,7,2,6,31),_AvctDsrTrapObjectOldInputPort_Type())
avctDsrTrapObjectOldInputPort.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectOldInputPort.setStatus(_B)
_AvctDsrTrapObjectPowerSupply_Type=Integer32
_AvctDsrTrapObjectPowerSupply_Object=MibScalar
avctDsrTrapObjectPowerSupply=_AvctDsrTrapObjectPowerSupply_Object((1,3,6,1,4,1,10418,7,2,6,32),_AvctDsrTrapObjectPowerSupply_Type())
avctDsrTrapObjectPowerSupply.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectPowerSupply.setStatus(_B)
_AvctDsrTrapObjectSpcDeviceCircuit_Type=Integer32
_AvctDsrTrapObjectSpcDeviceCircuit_Object=MibScalar
avctDsrTrapObjectSpcDeviceCircuit=_AvctDsrTrapObjectSpcDeviceCircuit_Object((1,3,6,1,4,1,10418,7,2,6,33),_AvctDsrTrapObjectSpcDeviceCircuit_Type())
avctDsrTrapObjectSpcDeviceCircuit.setMaxAccess(_A)
if mibBuilder.loadTexts:avctDsrTrapObjectSpcDeviceCircuit.setStatus(_B)
mibBuilder.exportSymbols('DSR-TRAP-OBJECTS-MIB',**{_C:UTF8String,'ImageFileUpgradeResultsEnum':ImageFileUpgradeResultsEnum,'IqAdaptorUpgradeResultsEnum':IqAdaptorUpgradeResultsEnum,'avocent':avocent,'dsr':dsr,'dsrProducts':dsrProducts,'dsrManagement':dsrManagement,'dsrTrapObject':dsrTrapObject,'avctDsrTrapObjectUserName':avctDsrTrapObjectUserName,'avctDsrTrapObjectTargetUserName':avctDsrTrapObjectTargetUserName,'avctDsrTrapObjectImageNewVersion':avctDsrTrapObjectImageNewVersion,'avctDsrTrapObjectImageCurrentVersion':avctDsrTrapObjectImageCurrentVersion,'avctDsrTrapObjectServerName':avctDsrTrapObjectServerName,'avctDsrTrapObjectIqAdaptorId':avctDsrTrapObjectIqAdaptorId,'avctDsrTrapObjectIpAddress':avctDsrTrapObjectIpAddress,'avctDsrTrapObjectPreviousScreenResolution':avctDsrTrapObjectPreviousScreenResolution,'avctDsrTrapObjectCurrentScreenResolution':avctDsrTrapObjectCurrentScreenResolution,'avctDsrTrapObjectAggregatedServerStatusChanged':avctDsrTrapObjectAggregatedServerStatusChanged,'avctDsrTrapObjectImageFileUpgradeResult':avctDsrTrapObjectImageFileUpgradeResult,'avctDsrTrapObjectIqAdaptorImageUpgradeResult':avctDsrTrapObjectIqAdaptorImageUpgradeResult,'avctDsrTrapObjectTypeOfImage':avctDsrTrapObjectTypeOfImage,'avctDsrTrapObjectInputPort':avctDsrTrapObjectInputPort,'avctDsrTrapObjectSwitchChannel':avctDsrTrapObjectSwitchChannel,'avctDsrTrapObjectFileName':avctDsrTrapObjectFileName,'avctDsrTrapObjectActiveSessions':avctDsrTrapObjectActiveSessions,'avctDsrTrapObjectCascadeSwitchName':avctDsrTrapObjectCascadeSwitchName,'avctDsrTrapObjectOldCascadeSwitchName':avctDsrTrapObjectOldCascadeSwitchName,'avctDsrTrapObjectOldServerName':avctDsrTrapObjectOldServerName,'avctDsrTrapObjectSpcDeviceLocation':avctDsrTrapObjectSpcDeviceLocation,'avctDsrTrapObjectSpcDevicePort':avctDsrTrapObjectSpcDevicePort,'avctDsrTrapObjectSpcDeviceLogin':avctDsrTrapObjectSpcDeviceLogin,'avctDsrTrapObjectSpcSocket':avctDsrTrapObjectSpcSocket,'avctDsrTrapObjectOldName':avctDsrTrapObjectOldName,'avctDsrTrapObjectItemName':avctDsrTrapObjectItemName,'avctDsrTrapObjectSpcDeviceInlet':avctDsrTrapObjectSpcDeviceInlet,'avctDsrTrapObjectSpcDeviceNumber':avctDsrTrapObjectSpcDeviceNumber,'avctDsrTrapObjectOldInputPort':avctDsrTrapObjectOldInputPort,'avctDsrTrapObjectPowerSupply':avctDsrTrapObjectPowerSupply,'avctDsrTrapObjectSpcDeviceCircuit':avctDsrTrapObjectSpcDeviceCircuit})