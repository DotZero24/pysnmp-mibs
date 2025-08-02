_H='outputName'
_G='inputName'
_F='accountNumber'
_E='not-accessible'
_D='COMMEND-SIP-MIB'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
commend=ModuleIdentity((1,3,6,1,4,1,37568))
if mibBuilder.loadTexts:commend.setRevisions(('2012-05-16 00:00',))
_CommendStationObjects_ObjectIdentity=ObjectIdentity
commendStationObjects=_CommendStationObjects_ObjectIdentity((1,3,6,1,4,1,37568,2))
_CommendStationObjectEntry_ObjectIdentity=ObjectIdentity
commendStationObjectEntry=_CommendStationObjectEntry_ObjectIdentity((1,3,6,1,4,1,37568,2,1))
_CommendStationCommon_ObjectIdentity=ObjectIdentity
commendStationCommon=_CommendStationCommon_ObjectIdentity((1,3,6,1,4,1,37568,2,1,1))
class _CommendStationCommonStationType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationType_Type.__name__=_B
_CommendStationCommonStationType_Object=MibScalar
commendStationCommonStationType=_CommendStationCommonStationType_Object((1,3,6,1,4,1,37568,2,1,1,1),_CommendStationCommonStationType_Type())
commendStationCommonStationType.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationType.setStatus(_A)
class _CommendStationCommonStationSubType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationSubType_Type.__name__=_B
_CommendStationCommonStationSubType_Object=MibScalar
commendStationCommonStationSubType=_CommendStationCommonStationSubType_Object((1,3,6,1,4,1,37568,2,1,1,2),_CommendStationCommonStationSubType_Type())
commendStationCommonStationSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationSubType.setStatus(_A)
class _CommendStationCommonStationSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationSoftwareVersion_Type.__name__=_B
_CommendStationCommonStationSoftwareVersion_Object=MibScalar
commendStationCommonStationSoftwareVersion=_CommendStationCommonStationSoftwareVersion_Object((1,3,6,1,4,1,37568,2,1,1,3),_CommendStationCommonStationSoftwareVersion_Type())
commendStationCommonStationSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationSoftwareVersion.setStatus(_A)
class _CommendStationCommonStationHardwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationHardwareVersion_Type.__name__=_B
_CommendStationCommonStationHardwareVersion_Object=MibScalar
commendStationCommonStationHardwareVersion=_CommendStationCommonStationHardwareVersion_Object((1,3,6,1,4,1,37568,2,1,1,4),_CommendStationCommonStationHardwareVersion_Type())
commendStationCommonStationHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationHardwareVersion.setStatus(_A)
class _CommendStationCommonStationCallNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationCallNumber_Type.__name__=_B
_CommendStationCommonStationCallNumber_Object=MibScalar
commendStationCommonStationCallNumber=_CommendStationCommonStationCallNumber_Object((1,3,6,1,4,1,37568,2,1,1,10),_CommendStationCommonStationCallNumber_Type())
commendStationCommonStationCallNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationCallNumber.setStatus(_A)
class _CommendStationCommonStationStationName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationStationName_Type.__name__=_B
_CommendStationCommonStationStationName_Object=MibScalar
commendStationCommonStationStationName=_CommendStationCommonStationStationName_Object((1,3,6,1,4,1,37568,2,1,1,11),_CommendStationCommonStationStationName_Type())
commendStationCommonStationStationName.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationStationName.setStatus(_A)
class _CommendStationCommonStationLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationLocation_Type.__name__=_B
_CommendStationCommonStationLocation_Object=MibScalar
commendStationCommonStationLocation=_CommendStationCommonStationLocation_Object((1,3,6,1,4,1,37568,2,1,1,12),_CommendStationCommonStationLocation_Type())
commendStationCommonStationLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationLocation.setStatus(_A)
class _CommendStationCommonStationSystemState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationSystemState_Type.__name__=_B
_CommendStationCommonStationSystemState_Object=MibScalar
commendStationCommonStationSystemState=_CommendStationCommonStationSystemState_Object((1,3,6,1,4,1,37568,2,1,1,20),_CommendStationCommonStationSystemState_Type())
commendStationCommonStationSystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationSystemState.setStatus(_A)
class _CommendStationCommonStationNtpState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationNtpState_Type.__name__=_B
_CommendStationCommonStationNtpState_Object=MibScalar
commendStationCommonStationNtpState=_CommendStationCommonStationNtpState_Object((1,3,6,1,4,1,37568,2,1,1,25),_CommendStationCommonStationNtpState_Type())
commendStationCommonStationNtpState.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationNtpState.setStatus(_A)
class _CommendStationCommonStationSequenceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationSequenceName_Type.__name__=_B
_CommendStationCommonStationSequenceName_Object=MibScalar
commendStationCommonStationSequenceName=_CommendStationCommonStationSequenceName_Object((1,3,6,1,4,1,37568,2,1,1,30),_CommendStationCommonStationSequenceName_Type())
commendStationCommonStationSequenceName.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationSequenceName.setStatus(_A)
class _CommendStationCommonStationCallState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationCommonStationCallState_Type.__name__=_B
_CommendStationCommonStationCallState_Object=MibScalar
commendStationCommonStationCallState=_CommendStationCommonStationCallState_Object((1,3,6,1,4,1,37568,2,1,1,80),_CommendStationCommonStationCallState_Type())
commendStationCommonStationCallState.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationCommonStationCallState.setStatus(_A)
_CommendStationConnectivity_ObjectIdentity=ObjectIdentity
commendStationConnectivity=_CommendStationConnectivity_ObjectIdentity((1,3,6,1,4,1,37568,2,1,2))
_CommendStationConnectivityType_Type=Integer32
_CommendStationConnectivityType_Object=MibScalar
commendStationConnectivityType=_CommendStationConnectivityType_Object((1,3,6,1,4,1,37568,2,1,2,1),_CommendStationConnectivityType_Type())
commendStationConnectivityType.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivityType.setStatus(_A)
_CommendStationConnectivityAnalog_ObjectIdentity=ObjectIdentity
commendStationConnectivityAnalog=_CommendStationConnectivityAnalog_ObjectIdentity((1,3,6,1,4,1,37568,2,1,2,2))
_CommendStationConnectivityDigital_ObjectIdentity=ObjectIdentity
commendStationConnectivityDigital=_CommendStationConnectivityDigital_ObjectIdentity((1,3,6,1,4,1,37568,2,1,2,3))
_CommendStationConnectivityIp_ObjectIdentity=ObjectIdentity
commendStationConnectivityIp=_CommendStationConnectivityIp_ObjectIdentity((1,3,6,1,4,1,37568,2,1,2,4))
_CommendStationConnectivitySip_ObjectIdentity=ObjectIdentity
commendStationConnectivitySip=_CommendStationConnectivitySip_ObjectIdentity((1,3,6,1,4,1,37568,2,1,2,5))
class _CommendStationConnectivitySipPrimaryRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipPrimaryRegistration_Type.__name__=_B
_CommendStationConnectivitySipPrimaryRegistration_Object=MibScalar
commendStationConnectivitySipPrimaryRegistration=_CommendStationConnectivitySipPrimaryRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,1),_CommendStationConnectivitySipPrimaryRegistration_Type())
commendStationConnectivitySipPrimaryRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipPrimaryRegistration.setStatus(_A)
class _CommendStationConnectivitySipPrimaryLastRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipPrimaryLastRegistration_Type.__name__=_B
_CommendStationConnectivitySipPrimaryLastRegistration_Object=MibScalar
commendStationConnectivitySipPrimaryLastRegistration=_CommendStationConnectivitySipPrimaryLastRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,2),_CommendStationConnectivitySipPrimaryLastRegistration_Type())
commendStationConnectivitySipPrimaryLastRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipPrimaryLastRegistration.setStatus(_A)
class _CommendStationConnectivitySipDhcp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipDhcp_Type.__name__=_B
_CommendStationConnectivitySipDhcp_Object=MibScalar
commendStationConnectivitySipDhcp=_CommendStationConnectivitySipDhcp_Object((1,3,6,1,4,1,37568,2,1,2,5,3),_CommendStationConnectivitySipDhcp_Type())
commendStationConnectivitySipDhcp.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipDhcp.setStatus(_A)
class _CommendStationConnectivitySipDns_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipDns_Type.__name__=_B
_CommendStationConnectivitySipDns_Object=MibScalar
commendStationConnectivitySipDns=_CommendStationConnectivitySipDns_Object((1,3,6,1,4,1,37568,2,1,2,5,4),_CommendStationConnectivitySipDns_Type())
commendStationConnectivitySipDns.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipDns.setStatus(_A)
class _CommendStationConnectivitySipAccount_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipAccount_Type.__name__=_B
_CommendStationConnectivitySipAccount_Object=MibScalar
commendStationConnectivitySipAccount=_CommendStationConnectivitySipAccount_Object((1,3,6,1,4,1,37568,2,1,2,5,5),_CommendStationConnectivitySipAccount_Type())
commendStationConnectivitySipAccount.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipAccount.setStatus(_A)
class _CommendStationConnectivitySipSecondaryRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipSecondaryRegistration_Type.__name__=_B
_CommendStationConnectivitySipSecondaryRegistration_Object=MibScalar
commendStationConnectivitySipSecondaryRegistration=_CommendStationConnectivitySipSecondaryRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,10),_CommendStationConnectivitySipSecondaryRegistration_Type())
commendStationConnectivitySipSecondaryRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipSecondaryRegistration.setStatus(_A)
class _CommendStationConnectivitySipSecondaryLastRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipSecondaryLastRegistration_Type.__name__=_B
_CommendStationConnectivitySipSecondaryLastRegistration_Object=MibScalar
commendStationConnectivitySipSecondaryLastRegistration=_CommendStationConnectivitySipSecondaryLastRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,11),_CommendStationConnectivitySipSecondaryLastRegistration_Type())
commendStationConnectivitySipSecondaryLastRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipSecondaryLastRegistration.setStatus(_A)
class _CommendStationConnectivitySipTertiaryRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipTertiaryRegistration_Type.__name__=_B
_CommendStationConnectivitySipTertiaryRegistration_Object=MibScalar
commendStationConnectivitySipTertiaryRegistration=_CommendStationConnectivitySipTertiaryRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,20),_CommendStationConnectivitySipTertiaryRegistration_Type())
commendStationConnectivitySipTertiaryRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipTertiaryRegistration.setStatus(_A)
class _CommendStationConnectivitySipTertiaryLastRegistration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationConnectivitySipTertiaryLastRegistration_Type.__name__=_B
_CommendStationConnectivitySipTertiaryLastRegistration_Object=MibScalar
commendStationConnectivitySipTertiaryLastRegistration=_CommendStationConnectivitySipTertiaryLastRegistration_Object((1,3,6,1,4,1,37568,2,1,2,5,21),_CommendStationConnectivitySipTertiaryLastRegistration_Type())
commendStationConnectivitySipTertiaryLastRegistration.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationConnectivitySipTertiaryLastRegistration.setStatus(_A)
_CommendStationConnectivitySipAccountTable_Object=MibTable
commendStationConnectivitySipAccountTable=_CommendStationConnectivitySipAccountTable_Object((1,3,6,1,4,1,37568,2,1,2,5,40))
if mibBuilder.loadTexts:commendStationConnectivitySipAccountTable.setStatus(_A)
_AccountTableEntry_Object=MibTableRow
accountTableEntry=_AccountTableEntry_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1))
accountTableEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:accountTableEntry.setStatus(_A)
class _AccountNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AccountNumber_Type.__name__=_B
_AccountNumber_Object=MibTableColumn
accountNumber=_AccountNumber_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1,1),_AccountNumber_Type())
accountNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:accountNumber.setStatus(_A)
class _AccountDisplayName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AccountDisplayName_Type.__name__=_B
_AccountDisplayName_Object=MibTableColumn
accountDisplayName=_AccountDisplayName_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1,2),_AccountDisplayName_Type())
accountDisplayName.setMaxAccess(_C)
if mibBuilder.loadTexts:accountDisplayName.setStatus(_A)
_AccountUserId_Type=OctetString
_AccountUserId_Object=MibTableColumn
accountUserId=_AccountUserId_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1,3),_AccountUserId_Type())
accountUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:accountUserId.setStatus(_A)
_AccountServer_Type=OctetString
_AccountServer_Object=MibTableColumn
accountServer=_AccountServer_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1,4),_AccountServer_Type())
accountServer.setMaxAccess(_C)
if mibBuilder.loadTexts:accountServer.setStatus(_A)
_AccountState_Type=OctetString
_AccountState_Object=MibTableColumn
accountState=_AccountState_Object((1,3,6,1,4,1,37568,2,1,2,5,40,1,5),_AccountState_Type())
accountState.setMaxAccess(_C)
if mibBuilder.loadTexts:accountState.setStatus(_A)
_CommendStationAudio_ObjectIdentity=ObjectIdentity
commendStationAudio=_CommendStationAudio_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3))
_CommendStationAudioMic1_ObjectIdentity=ObjectIdentity
commendStationAudioMic1=_CommendStationAudioMic1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,1))
class _CommendStationAudioMic1Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioMic1Type_Type.__name__=_B
_CommendStationAudioMic1Type_Object=MibScalar
commendStationAudioMic1Type=_CommendStationAudioMic1Type_Object((1,3,6,1,4,1,37568,2,1,3,1,1),_CommendStationAudioMic1Type_Type())
commendStationAudioMic1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioMic1Type.setStatus(_A)
class _CommendStationAudioMic1Sensitivity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioMic1Sensitivity_Type.__name__=_B
_CommendStationAudioMic1Sensitivity_Object=MibScalar
commendStationAudioMic1Sensitivity=_CommendStationAudioMic1Sensitivity_Object((1,3,6,1,4,1,37568,2,1,3,1,2),_CommendStationAudioMic1Sensitivity_Type())
commendStationAudioMic1Sensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioMic1Sensitivity.setStatus(_A)
_CommendStationAudioMic2_ObjectIdentity=ObjectIdentity
commendStationAudioMic2=_CommendStationAudioMic2_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,2))
_CommendStationAudioMic3_ObjectIdentity=ObjectIdentity
commendStationAudioMic3=_CommendStationAudioMic3_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,3))
_CommendStationAudioLsMic_ObjectIdentity=ObjectIdentity
commendStationAudioLsMic=_CommendStationAudioLsMic_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,4))
class _CommendStationAudioLsMicStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioLsMicStatus_Type.__name__=_B
_CommendStationAudioLsMicStatus_Object=MibScalar
commendStationAudioLsMicStatus=_CommendStationAudioLsMicStatus_Object((1,3,6,1,4,1,37568,2,1,3,4,1),_CommendStationAudioLsMicStatus_Type())
commendStationAudioLsMicStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioLsMicStatus.setStatus(_A)
_CommendStationAudiomonitoring_ObjectIdentity=ObjectIdentity
commendStationAudiomonitoring=_CommendStationAudiomonitoring_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,5))
class _CommendStationAudiomonitoringStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudiomonitoringStatus_Type.__name__=_B
_CommendStationAudiomonitoringStatus_Object=MibScalar
commendStationAudiomonitoringStatus=_CommendStationAudiomonitoringStatus_Object((1,3,6,1,4,1,37568,2,1,3,5,1),_CommendStationAudiomonitoringStatus_Type())
commendStationAudiomonitoringStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudiomonitoringStatus.setStatus(_A)
_CommendStationAudioAmp1_ObjectIdentity=ObjectIdentity
commendStationAudioAmp1=_CommendStationAudioAmp1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,10))
class _CommendStationAudioAmp1Type_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioAmp1Type_Type.__name__=_B
_CommendStationAudioAmp1Type_Object=MibScalar
commendStationAudioAmp1Type=_CommendStationAudioAmp1Type_Object((1,3,6,1,4,1,37568,2,1,3,10,1),_CommendStationAudioAmp1Type_Type())
commendStationAudioAmp1Type.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioAmp1Type.setStatus(_A)
class _CommendStationAudioAmp1Sensitivity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioAmp1Sensitivity_Type.__name__=_B
_CommendStationAudioAmp1Sensitivity_Object=MibScalar
commendStationAudioAmp1Sensitivity=_CommendStationAudioAmp1Sensitivity_Object((1,3,6,1,4,1,37568,2,1,3,10,2),_CommendStationAudioAmp1Sensitivity_Type())
commendStationAudioAmp1Sensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioAmp1Sensitivity.setStatus(_A)
class _CommendStationAudioSpeakerCompressor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioSpeakerCompressor_Type.__name__=_B
_CommendStationAudioSpeakerCompressor_Object=MibScalar
commendStationAudioSpeakerCompressor=_CommendStationAudioSpeakerCompressor_Object((1,3,6,1,4,1,37568,2,1,3,10,3),_CommendStationAudioSpeakerCompressor_Type())
commendStationAudioSpeakerCompressor.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioSpeakerCompressor.setStatus(_A)
_CommendStationAudioAEC_ObjectIdentity=ObjectIdentity
commendStationAudioAEC=_CommendStationAudioAEC_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,50))
class _CommendStationAudioAECMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioAECMode_Type.__name__=_B
_CommendStationAudioAECMode_Object=MibScalar
commendStationAudioAECMode=_CommendStationAudioAECMode_Object((1,3,6,1,4,1,37568,2,1,3,50,1),_CommendStationAudioAECMode_Type())
commendStationAudioAECMode.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioAECMode.setStatus(_A)
class _CommendStationAudioNgClosedGain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioNgClosedGain_Type.__name__=_B
_CommendStationAudioNgClosedGain_Object=MibScalar
commendStationAudioNgClosedGain=_CommendStationAudioNgClosedGain_Object((1,3,6,1,4,1,37568,2,1,3,50,2),_CommendStationAudioNgClosedGain_Type())
commendStationAudioNgClosedGain.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioNgClosedGain.setStatus(_A)
class _CommendStationAudioPgClosedGain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioPgClosedGain_Type.__name__=_B
_CommendStationAudioPgClosedGain_Object=MibScalar
commendStationAudioPgClosedGain=_CommendStationAudioPgClosedGain_Object((1,3,6,1,4,1,37568,2,1,3,50,3),_CommendStationAudioPgClosedGain_Type())
commendStationAudioPgClosedGain.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioPgClosedGain.setStatus(_A)
class _CommendStationAudioNgEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioNgEnabled_Type.__name__=_B
_CommendStationAudioNgEnabled_Object=MibScalar
commendStationAudioNgEnabled=_CommendStationAudioNgEnabled_Object((1,3,6,1,4,1,37568,2,1,3,50,4),_CommendStationAudioNgEnabled_Type())
commendStationAudioNgEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioNgEnabled.setStatus(_A)
class _CommendStationAudioPgEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioPgEnabled_Type.__name__=_B
_CommendStationAudioPgEnabled_Object=MibScalar
commendStationAudioPgEnabled=_CommendStationAudioPgEnabled_Object((1,3,6,1,4,1,37568,2,1,3,50,5),_CommendStationAudioPgEnabled_Type())
commendStationAudioPgEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioPgEnabled.setStatus(_A)
_CommendStationAudioNC_ObjectIdentity=ObjectIdentity
commendStationAudioNC=_CommendStationAudioNC_ObjectIdentity((1,3,6,1,4,1,37568,2,1,3,51))
class _CommendStationAudioNCMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationAudioNCMode_Type.__name__=_B
_CommendStationAudioNCMode_Object=MibScalar
commendStationAudioNCMode=_CommendStationAudioNCMode_Object((1,3,6,1,4,1,37568,2,1,3,51,1),_CommendStationAudioNCMode_Type())
commendStationAudioNCMode.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationAudioNCMode.setStatus(_A)
_CommendStationInputs_ObjectIdentity=ObjectIdentity
commendStationInputs=_CommendStationInputs_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4))
_CommendStationInput1_ObjectIdentity=ObjectIdentity
commendStationInput1=_CommendStationInput1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,1))
class _CommendStationInputType1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputType1_Type.__name__=_B
_CommendStationInputType1_Object=MibScalar
commendStationInputType1=_CommendStationInputType1_Object((1,3,6,1,4,1,37568,2,1,4,1,1),_CommendStationInputType1_Type())
commendStationInputType1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputType1.setStatus(_A)
class _CommendStationInputState1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputState1_Type.__name__=_B
_CommendStationInputState1_Object=MibScalar
commendStationInputState1=_CommendStationInputState1_Object((1,3,6,1,4,1,37568,2,1,4,1,2),_CommendStationInputState1_Type())
commendStationInputState1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputState1.setStatus(_A)
_CommendStationInput2_ObjectIdentity=ObjectIdentity
commendStationInput2=_CommendStationInput2_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,2))
class _CommendStationInputType2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputType2_Type.__name__=_B
_CommendStationInputType2_Object=MibScalar
commendStationInputType2=_CommendStationInputType2_Object((1,3,6,1,4,1,37568,2,1,4,2,1),_CommendStationInputType2_Type())
commendStationInputType2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputType2.setStatus(_A)
class _CommendStationInputState2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputState2_Type.__name__=_B
_CommendStationInputState2_Object=MibScalar
commendStationInputState2=_CommendStationInputState2_Object((1,3,6,1,4,1,37568,2,1,4,2,2),_CommendStationInputState2_Type())
commendStationInputState2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputState2.setStatus(_A)
_CommendStationInput3_ObjectIdentity=ObjectIdentity
commendStationInput3=_CommendStationInput3_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,3))
class _CommendStationInputType3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputType3_Type.__name__=_B
_CommendStationInputType3_Object=MibScalar
commendStationInputType3=_CommendStationInputType3_Object((1,3,6,1,4,1,37568,2,1,4,3,1),_CommendStationInputType3_Type())
commendStationInputType3.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputType3.setStatus(_A)
class _CommendStationInputState3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputState3_Type.__name__=_B
_CommendStationInputState3_Object=MibScalar
commendStationInputState3=_CommendStationInputState3_Object((1,3,6,1,4,1,37568,2,1,4,3,2),_CommendStationInputState3_Type())
commendStationInputState3.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputState3.setStatus(_A)
_CommendStationEB2E2AInput1_ObjectIdentity=ObjectIdentity
commendStationEB2E2AInput1=_CommendStationEB2E2AInput1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,4))
class _CommendStationEB2E2AInputType1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AInputType1_Type.__name__=_B
_CommendStationEB2E2AInputType1_Object=MibScalar
commendStationEB2E2AInputType1=_CommendStationEB2E2AInputType1_Object((1,3,6,1,4,1,37568,2,1,4,4,1),_CommendStationEB2E2AInputType1_Type())
commendStationEB2E2AInputType1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AInputType1.setStatus(_A)
class _CommendStationEB2E2AInputState1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AInputState1_Type.__name__=_B
_CommendStationEB2E2AInputState1_Object=MibScalar
commendStationEB2E2AInputState1=_CommendStationEB2E2AInputState1_Object((1,3,6,1,4,1,37568,2,1,4,4,2),_CommendStationEB2E2AInputState1_Type())
commendStationEB2E2AInputState1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AInputState1.setStatus(_A)
_CommendStationEB2E2AInput2_ObjectIdentity=ObjectIdentity
commendStationEB2E2AInput2=_CommendStationEB2E2AInput2_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,5))
class _CommendStationEB2E2AInputType2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AInputType2_Type.__name__=_B
_CommendStationEB2E2AInputType2_Object=MibScalar
commendStationEB2E2AInputType2=_CommendStationEB2E2AInputType2_Object((1,3,6,1,4,1,37568,2,1,4,5,1),_CommendStationEB2E2AInputType2_Type())
commendStationEB2E2AInputType2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AInputType2.setStatus(_A)
class _CommendStationEB2E2AInputState2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AInputState2_Type.__name__=_B
_CommendStationEB2E2AInputState2_Object=MibScalar
commendStationEB2E2AInputState2=_CommendStationEB2E2AInputState2_Object((1,3,6,1,4,1,37568,2,1,4,5,2),_CommendStationEB2E2AInputState2_Type())
commendStationEB2E2AInputState2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AInputState2.setStatus(_A)
_CommendStationInputKeyboard_ObjectIdentity=ObjectIdentity
commendStationInputKeyboard=_CommendStationInputKeyboard_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,10))
class _CommendStationInputKeyboardButton1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputKeyboardButton1_Type.__name__=_B
_CommendStationInputKeyboardButton1_Object=MibScalar
commendStationInputKeyboardButton1=_CommendStationInputKeyboardButton1_Object((1,3,6,1,4,1,37568,2,1,4,10,1),_CommendStationInputKeyboardButton1_Type())
commendStationInputKeyboardButton1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputKeyboardButton1.setStatus(_A)
class _CommendStationInputKeyboardButton2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputKeyboardButton2_Type.__name__=_B
_CommendStationInputKeyboardButton2_Object=MibScalar
commendStationInputKeyboardButton2=_CommendStationInputKeyboardButton2_Object((1,3,6,1,4,1,37568,2,1,4,10,2),_CommendStationInputKeyboardButton2_Type())
commendStationInputKeyboardButton2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputKeyboardButton2.setStatus(_A)
class _CommendStationInputKeyboardButton3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputKeyboardButton3_Type.__name__=_B
_CommendStationInputKeyboardButton3_Object=MibScalar
commendStationInputKeyboardButton3=_CommendStationInputKeyboardButton3_Object((1,3,6,1,4,1,37568,2,1,4,10,3),_CommendStationInputKeyboardButton3_Type())
commendStationInputKeyboardButton3.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputKeyboardButton3.setStatus(_A)
_CommendStationInputFullKeyboard_ObjectIdentity=ObjectIdentity
commendStationInputFullKeyboard=_CommendStationInputFullKeyboard_ObjectIdentity((1,3,6,1,4,1,37568,2,1,4,11))
class _CommendStationInputFullKeyboardButton1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton1_Type.__name__=_B
_CommendStationInputFullKeyboardButton1_Object=MibScalar
commendStationInputFullKeyboardButton1=_CommendStationInputFullKeyboardButton1_Object((1,3,6,1,4,1,37568,2,1,4,11,1),_CommendStationInputFullKeyboardButton1_Type())
commendStationInputFullKeyboardButton1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton1.setStatus(_A)
class _CommendStationInputFullKeyboardButton2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton2_Type.__name__=_B
_CommendStationInputFullKeyboardButton2_Object=MibScalar
commendStationInputFullKeyboardButton2=_CommendStationInputFullKeyboardButton2_Object((1,3,6,1,4,1,37568,2,1,4,11,2),_CommendStationInputFullKeyboardButton2_Type())
commendStationInputFullKeyboardButton2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton2.setStatus(_A)
class _CommendStationInputFullKeyboardButton3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton3_Type.__name__=_B
_CommendStationInputFullKeyboardButton3_Object=MibScalar
commendStationInputFullKeyboardButton3=_CommendStationInputFullKeyboardButton3_Object((1,3,6,1,4,1,37568,2,1,4,11,3),_CommendStationInputFullKeyboardButton3_Type())
commendStationInputFullKeyboardButton3.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton3.setStatus(_A)
class _CommendStationInputFullKeyboardButton4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton4_Type.__name__=_B
_CommendStationInputFullKeyboardButton4_Object=MibScalar
commendStationInputFullKeyboardButton4=_CommendStationInputFullKeyboardButton4_Object((1,3,6,1,4,1,37568,2,1,4,11,4),_CommendStationInputFullKeyboardButton4_Type())
commendStationInputFullKeyboardButton4.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton4.setStatus(_A)
class _CommendStationInputFullKeyboardButton5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton5_Type.__name__=_B
_CommendStationInputFullKeyboardButton5_Object=MibScalar
commendStationInputFullKeyboardButton5=_CommendStationInputFullKeyboardButton5_Object((1,3,6,1,4,1,37568,2,1,4,11,5),_CommendStationInputFullKeyboardButton5_Type())
commendStationInputFullKeyboardButton5.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton5.setStatus(_A)
class _CommendStationInputFullKeyboardButton6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton6_Type.__name__=_B
_CommendStationInputFullKeyboardButton6_Object=MibScalar
commendStationInputFullKeyboardButton6=_CommendStationInputFullKeyboardButton6_Object((1,3,6,1,4,1,37568,2,1,4,11,6),_CommendStationInputFullKeyboardButton6_Type())
commendStationInputFullKeyboardButton6.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton6.setStatus(_A)
class _CommendStationInputFullKeyboardButton7_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton7_Type.__name__=_B
_CommendStationInputFullKeyboardButton7_Object=MibScalar
commendStationInputFullKeyboardButton7=_CommendStationInputFullKeyboardButton7_Object((1,3,6,1,4,1,37568,2,1,4,11,7),_CommendStationInputFullKeyboardButton7_Type())
commendStationInputFullKeyboardButton7.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton7.setStatus(_A)
class _CommendStationInputFullKeyboardButton8_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton8_Type.__name__=_B
_CommendStationInputFullKeyboardButton8_Object=MibScalar
commendStationInputFullKeyboardButton8=_CommendStationInputFullKeyboardButton8_Object((1,3,6,1,4,1,37568,2,1,4,11,8),_CommendStationInputFullKeyboardButton8_Type())
commendStationInputFullKeyboardButton8.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton8.setStatus(_A)
class _CommendStationInputFullKeyboardButton9_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton9_Type.__name__=_B
_CommendStationInputFullKeyboardButton9_Object=MibScalar
commendStationInputFullKeyboardButton9=_CommendStationInputFullKeyboardButton9_Object((1,3,6,1,4,1,37568,2,1,4,11,9),_CommendStationInputFullKeyboardButton9_Type())
commendStationInputFullKeyboardButton9.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton9.setStatus(_A)
class _CommendStationInputFullKeyboardButton0_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButton0_Type.__name__=_B
_CommendStationInputFullKeyboardButton0_Object=MibScalar
commendStationInputFullKeyboardButton0=_CommendStationInputFullKeyboardButton0_Object((1,3,6,1,4,1,37568,2,1,4,11,10),_CommendStationInputFullKeyboardButton0_Type())
commendStationInputFullKeyboardButton0.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButton0.setStatus(_A)
class _CommendStationInputFullKeyboardButtonX_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonX_Type.__name__=_B
_CommendStationInputFullKeyboardButtonX_Object=MibScalar
commendStationInputFullKeyboardButtonX=_CommendStationInputFullKeyboardButtonX_Object((1,3,6,1,4,1,37568,2,1,4,11,11),_CommendStationInputFullKeyboardButtonX_Type())
commendStationInputFullKeyboardButtonX.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonX.setStatus(_A)
class _CommendStationInputFullKeyboardButtonT_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonT_Type.__name__=_B
_CommendStationInputFullKeyboardButtonT_Object=MibScalar
commendStationInputFullKeyboardButtonT=_CommendStationInputFullKeyboardButtonT_Object((1,3,6,1,4,1,37568,2,1,4,11,12),_CommendStationInputFullKeyboardButtonT_Type())
commendStationInputFullKeyboardButtonT.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonT.setStatus(_A)
class _CommendStationInputFullKeyboardButtonUP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonUP_Type.__name__=_B
_CommendStationInputFullKeyboardButtonUP_Object=MibScalar
commendStationInputFullKeyboardButtonUP=_CommendStationInputFullKeyboardButtonUP_Object((1,3,6,1,4,1,37568,2,1,4,11,13),_CommendStationInputFullKeyboardButtonUP_Type())
commendStationInputFullKeyboardButtonUP.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonUP.setStatus(_A)
class _CommendStationInputFullKeyboardButtonDOWN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonDOWN_Type.__name__=_B
_CommendStationInputFullKeyboardButtonDOWN_Object=MibScalar
commendStationInputFullKeyboardButtonDOWN=_CommendStationInputFullKeyboardButtonDOWN_Object((1,3,6,1,4,1,37568,2,1,4,11,14),_CommendStationInputFullKeyboardButtonDOWN_Type())
commendStationInputFullKeyboardButtonDOWN.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonDOWN.setStatus(_A)
class _CommendStationInputFullKeyboardButtonMENU_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonMENU_Type.__name__=_B
_CommendStationInputFullKeyboardButtonMENU_Object=MibScalar
commendStationInputFullKeyboardButtonMENU=_CommendStationInputFullKeyboardButtonMENU_Object((1,3,6,1,4,1,37568,2,1,4,11,15),_CommendStationInputFullKeyboardButtonMENU_Type())
commendStationInputFullKeyboardButtonMENU.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonMENU.setStatus(_A)
class _CommendStationInputFullKeyboardButtonENTER_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationInputFullKeyboardButtonENTER_Type.__name__=_B
_CommendStationInputFullKeyboardButtonENTER_Object=MibScalar
commendStationInputFullKeyboardButtonENTER=_CommendStationInputFullKeyboardButtonENTER_Object((1,3,6,1,4,1,37568,2,1,4,11,16),_CommendStationInputFullKeyboardButtonENTER_Type())
commendStationInputFullKeyboardButtonENTER.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationInputFullKeyboardButtonENTER.setStatus(_A)
_CommendStationInputTable_Object=MibTable
commendStationInputTable=_CommendStationInputTable_Object((1,3,6,1,4,1,37568,2,1,4,20))
if mibBuilder.loadTexts:commendStationInputTable.setStatus(_A)
_InputTableEntry_Object=MibTableRow
inputTableEntry=_InputTableEntry_Object((1,3,6,1,4,1,37568,2,1,4,20,1))
inputTableEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:inputTableEntry.setStatus(_A)
class _InputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_InputName_Type.__name__=_B
_InputName_Object=MibTableColumn
inputName=_InputName_Object((1,3,6,1,4,1,37568,2,1,4,20,1,1),_InputName_Type())
inputName.setMaxAccess(_E)
if mibBuilder.loadTexts:inputName.setStatus(_A)
class _InputState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_InputState_Type.__name__=_B
_InputState_Object=MibTableColumn
inputState=_InputState_Object((1,3,6,1,4,1,37568,2,1,4,20,1,2),_InputState_Type())
inputState.setMaxAccess(_E)
if mibBuilder.loadTexts:inputState.setStatus(_A)
_CommendStationInputStatus_ObjectIdentity=ObjectIdentity
commendStationInputStatus=_CommendStationInputStatus_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5))
_CommendStationOutputs_ObjectIdentity=ObjectIdentity
commendStationOutputs=_CommendStationOutputs_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5))
class _CommendStationLastInputChange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationLastInputChange_Type.__name__=_B
_CommendStationLastInputChange_Object=MibScalar
commendStationLastInputChange=_CommendStationLastInputChange_Object((1,3,6,1,4,1,37568,2,1,5,1),_CommendStationLastInputChange_Type())
commendStationLastInputChange.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationLastInputChange.setStatus(_A)
_CommendStationOutput1_ObjectIdentity=ObjectIdentity
commendStationOutput1=_CommendStationOutput1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5,1))
class _CommendStationOutputName1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationOutputName1_Type.__name__=_B
_CommendStationOutputName1_Object=MibScalar
commendStationOutputName1=_CommendStationOutputName1_Object((1,3,6,1,4,1,37568,2,1,5,1,1),_CommendStationOutputName1_Type())
commendStationOutputName1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationOutputName1.setStatus(_A)
class _CommendStationOutputState1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationOutputState1_Type.__name__=_B
_CommendStationOutputState1_Object=MibScalar
commendStationOutputState1=_CommendStationOutputState1_Object((1,3,6,1,4,1,37568,2,1,5,1,2),_CommendStationOutputState1_Type())
commendStationOutputState1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationOutputState1.setStatus(_A)
class _CommendStationLastButtonStuck_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationLastButtonStuck_Type.__name__=_B
_CommendStationLastButtonStuck_Object=MibScalar
commendStationLastButtonStuck=_CommendStationLastButtonStuck_Object((1,3,6,1,4,1,37568,2,1,5,2),_CommendStationLastButtonStuck_Type())
commendStationLastButtonStuck.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationLastButtonStuck.setStatus(_A)
_CommendStationOutput2_ObjectIdentity=ObjectIdentity
commendStationOutput2=_CommendStationOutput2_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5,2))
class _CommendStationOutputName2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationOutputName2_Type.__name__=_B
_CommendStationOutputName2_Object=MibScalar
commendStationOutputName2=_CommendStationOutputName2_Object((1,3,6,1,4,1,37568,2,1,5,2,1),_CommendStationOutputName2_Type())
commendStationOutputName2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationOutputName2.setStatus(_A)
class _CommendStationOutputState2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationOutputState2_Type.__name__=_B
_CommendStationOutputState2_Object=MibScalar
commendStationOutputState2=_CommendStationOutputState2_Object((1,3,6,1,4,1,37568,2,1,5,2,2),_CommendStationOutputState2_Type())
commendStationOutputState2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationOutputState2.setStatus(_A)
_CommendStationEB2E2AOutput1_ObjectIdentity=ObjectIdentity
commendStationEB2E2AOutput1=_CommendStationEB2E2AOutput1_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5,3))
class _CommendStationEB2E2AOutputName1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AOutputName1_Type.__name__=_B
_CommendStationEB2E2AOutputName1_Object=MibScalar
commendStationEB2E2AOutputName1=_CommendStationEB2E2AOutputName1_Object((1,3,6,1,4,1,37568,2,1,5,3,1),_CommendStationEB2E2AOutputName1_Type())
commendStationEB2E2AOutputName1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AOutputName1.setStatus(_A)
class _CommendStationEB2E2AOutputState1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AOutputState1_Type.__name__=_B
_CommendStationEB2E2AOutputState1_Object=MibScalar
commendStationEB2E2AOutputState1=_CommendStationEB2E2AOutputState1_Object((1,3,6,1,4,1,37568,2,1,5,3,2),_CommendStationEB2E2AOutputState1_Type())
commendStationEB2E2AOutputState1.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AOutputState1.setStatus(_A)
_CommendStationEB2E2AOutput2_ObjectIdentity=ObjectIdentity
commendStationEB2E2AOutput2=_CommendStationEB2E2AOutput2_ObjectIdentity((1,3,6,1,4,1,37568,2,1,5,4))
class _CommendStationEB2E2AOutputName2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AOutputName2_Type.__name__=_B
_CommendStationEB2E2AOutputName2_Object=MibScalar
commendStationEB2E2AOutputName2=_CommendStationEB2E2AOutputName2_Object((1,3,6,1,4,1,37568,2,1,5,4,1),_CommendStationEB2E2AOutputName2_Type())
commendStationEB2E2AOutputName2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AOutputName2.setStatus(_A)
class _CommendStationEB2E2AOutputState2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationEB2E2AOutputState2_Type.__name__=_B
_CommendStationEB2E2AOutputState2_Object=MibScalar
commendStationEB2E2AOutputState2=_CommendStationEB2E2AOutputState2_Object((1,3,6,1,4,1,37568,2,1,5,4,2),_CommendStationEB2E2AOutputState2_Type())
commendStationEB2E2AOutputState2.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationEB2E2AOutputState2.setStatus(_A)
_CommendStationOutputTable_Object=MibTable
commendStationOutputTable=_CommendStationOutputTable_Object((1,3,6,1,4,1,37568,2,1,5,20))
if mibBuilder.loadTexts:commendStationOutputTable.setStatus(_A)
_OutputTableEntry_Object=MibTableRow
outputTableEntry=_OutputTableEntry_Object((1,3,6,1,4,1,37568,2,1,5,20,1))
outputTableEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:outputTableEntry.setStatus(_A)
class _OutputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OutputName_Type.__name__=_B
_OutputName_Object=MibTableColumn
outputName=_OutputName_Object((1,3,6,1,4,1,37568,2,1,5,20,1,1),_OutputName_Type())
outputName.setMaxAccess(_E)
if mibBuilder.loadTexts:outputName.setStatus(_A)
class _OutputState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OutputState_Type.__name__=_B
_OutputState_Object=MibTableColumn
outputState=_OutputState_Object((1,3,6,1,4,1,37568,2,1,5,20,1,2),_OutputState_Type())
outputState.setMaxAccess(_E)
if mibBuilder.loadTexts:outputState.setStatus(_A)
_CommendStationOutputStatus_ObjectIdentity=ObjectIdentity
commendStationOutputStatus=_CommendStationOutputStatus_ObjectIdentity((1,3,6,1,4,1,37568,2,1,7))
class _CommendStationLastOutputChange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CommendStationLastOutputChange_Type.__name__=_B
_CommendStationLastOutputChange_Object=MibScalar
commendStationLastOutputChange=_CommendStationLastOutputChange_Object((1,3,6,1,4,1,37568,2,1,7,1),_CommendStationLastOutputChange_Type())
commendStationLastOutputChange.setMaxAccess(_C)
if mibBuilder.loadTexts:commendStationLastOutputChange.setStatus(_A)
commendStationCommonStationNtpNotification=NotificationType((1,3,6,1,4,1,37568,2,1,1,26))
if mibBuilder.loadTexts:commendStationCommonStationNtpNotification.setStatus(_A)
commendStationAudioLsMicSurveillanceNotification=NotificationType((1,3,6,1,4,1,37568,2,1,3,11))
if mibBuilder.loadTexts:commendStationAudioLsMicSurveillanceNotification.setStatus(_A)
commendStationAudioMonitoringAlarmNotification=NotificationType((1,3,6,1,4,1,37568,2,1,3,12))
if mibBuilder.loadTexts:commendStationAudioMonitoringAlarmNotification.setStatus(_A)
commendStationInputNotifications=NotificationType((1,3,6,1,4,1,37568,2,1,4,9))
if mibBuilder.loadTexts:commendStationInputNotifications.setStatus(_A)
commendStationInputButtonStuckNotification=NotificationType((1,3,6,1,4,1,37568,2,1,4,9,1))
if mibBuilder.loadTexts:commendStationInputButtonStuckNotification.setStatus(_A)
commendStationInputHandsetOffhookNotification=NotificationType((1,3,6,1,4,1,37568,2,1,4,9,2))
if mibBuilder.loadTexts:commendStationInputHandsetOffhookNotification.setStatus(_A)
commendStationInputChangedNotification=NotificationType((1,3,6,1,4,1,37568,2,1,4,9,3))
if mibBuilder.loadTexts:commendStationInputChangedNotification.setStatus(_A)
commendStationOutput1Notifications=NotificationType((1,3,6,1,4,1,37568,2,1,5,1,10))
if mibBuilder.loadTexts:commendStationOutput1Notifications.setStatus(_A)
commendStationOutput2Notifications=NotificationType((1,3,6,1,4,1,37568,2,1,5,2,10))
if mibBuilder.loadTexts:commendStationOutput2Notifications.setStatus(_A)
commendStationEB2E2AOutput1Notifications=NotificationType((1,3,6,1,4,1,37568,2,1,5,3,10))
if mibBuilder.loadTexts:commendStationEB2E2AOutput1Notifications.setStatus(_A)
commendStationEB2E2AOutput2Notifications=NotificationType((1,3,6,1,4,1,37568,2,1,5,4,10))
if mibBuilder.loadTexts:commendStationEB2E2AOutput2Notifications.setStatus(_A)
commendStationOutputNotifications=NotificationType((1,3,6,1,4,1,37568,2,1,5,9))
if mibBuilder.loadTexts:commendStationOutputNotifications.setStatus(_A)
commendStationOutputChangedNotification=NotificationType((1,3,6,1,4,1,37568,2,1,5,9,1))
if mibBuilder.loadTexts:commendStationOutputChangedNotification.setStatus(_A)
commendStationObjectStatusNotifications=NotificationType((1,3,6,1,4,1,37568,2,10))
if mibBuilder.loadTexts:commendStationObjectStatusNotifications.setStatus(_A)
commendStationApplicationStart=NotificationType((1,3,6,1,4,1,37568,2,20))
if mibBuilder.loadTexts:commendStationApplicationStart.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'commend':commend,'commendStationObjects':commendStationObjects,'commendStationObjectEntry':commendStationObjectEntry,'commendStationCommon':commendStationCommon,'commendStationCommonStationType':commendStationCommonStationType,'commendStationCommonStationSubType':commendStationCommonStationSubType,'commendStationCommonStationSoftwareVersion':commendStationCommonStationSoftwareVersion,'commendStationCommonStationHardwareVersion':commendStationCommonStationHardwareVersion,'commendStationCommonStationCallNumber':commendStationCommonStationCallNumber,'commendStationCommonStationStationName':commendStationCommonStationStationName,'commendStationCommonStationLocation':commendStationCommonStationLocation,'commendStationCommonStationSystemState':commendStationCommonStationSystemState,'commendStationCommonStationNtpState':commendStationCommonStationNtpState,'commendStationCommonStationNtpNotification':commendStationCommonStationNtpNotification,'commendStationCommonStationSequenceName':commendStationCommonStationSequenceName,'commendStationCommonStationCallState':commendStationCommonStationCallState,'commendStationConnectivity':commendStationConnectivity,'commendStationConnectivityType':commendStationConnectivityType,'commendStationConnectivityAnalog':commendStationConnectivityAnalog,'commendStationConnectivityDigital':commendStationConnectivityDigital,'commendStationConnectivityIp':commendStationConnectivityIp,'commendStationConnectivitySip':commendStationConnectivitySip,'commendStationConnectivitySipPrimaryRegistration':commendStationConnectivitySipPrimaryRegistration,'commendStationConnectivitySipPrimaryLastRegistration':commendStationConnectivitySipPrimaryLastRegistration,'commendStationConnectivitySipDhcp':commendStationConnectivitySipDhcp,'commendStationConnectivitySipDns':commendStationConnectivitySipDns,'commendStationConnectivitySipAccount':commendStationConnectivitySipAccount,'commendStationConnectivitySipSecondaryRegistration':commendStationConnectivitySipSecondaryRegistration,'commendStationConnectivitySipSecondaryLastRegistration':commendStationConnectivitySipSecondaryLastRegistration,'commendStationConnectivitySipTertiaryRegistration':commendStationConnectivitySipTertiaryRegistration,'commendStationConnectivitySipTertiaryLastRegistration':commendStationConnectivitySipTertiaryLastRegistration,'commendStationConnectivitySipAccountTable':commendStationConnectivitySipAccountTable,'accountTableEntry':accountTableEntry,_F:accountNumber,'accountDisplayName':accountDisplayName,'accountUserId':accountUserId,'accountServer':accountServer,'accountState':accountState,'commendStationAudio':commendStationAudio,'commendStationAudioMic1':commendStationAudioMic1,'commendStationAudioMic1Type':commendStationAudioMic1Type,'commendStationAudioMic1Sensitivity':commendStationAudioMic1Sensitivity,'commendStationAudioMic2':commendStationAudioMic2,'commendStationAudioMic3':commendStationAudioMic3,'commendStationAudioLsMic':commendStationAudioLsMic,'commendStationAudioLsMicStatus':commendStationAudioLsMicStatus,'commendStationAudiomonitoring':commendStationAudiomonitoring,'commendStationAudiomonitoringStatus':commendStationAudiomonitoringStatus,'commendStationAudioAmp1':commendStationAudioAmp1,'commendStationAudioAmp1Type':commendStationAudioAmp1Type,'commendStationAudioAmp1Sensitivity':commendStationAudioAmp1Sensitivity,'commendStationAudioSpeakerCompressor':commendStationAudioSpeakerCompressor,'commendStationAudioLsMicSurveillanceNotification':commendStationAudioLsMicSurveillanceNotification,'commendStationAudioMonitoringAlarmNotification':commendStationAudioMonitoringAlarmNotification,'commendStationAudioAEC':commendStationAudioAEC,'commendStationAudioAECMode':commendStationAudioAECMode,'commendStationAudioNgClosedGain':commendStationAudioNgClosedGain,'commendStationAudioPgClosedGain':commendStationAudioPgClosedGain,'commendStationAudioNgEnabled':commendStationAudioNgEnabled,'commendStationAudioPgEnabled':commendStationAudioPgEnabled,'commendStationAudioNC':commendStationAudioNC,'commendStationAudioNCMode':commendStationAudioNCMode,'commendStationInputs':commendStationInputs,'commendStationInput1':commendStationInput1,'commendStationInputType1':commendStationInputType1,'commendStationInputState1':commendStationInputState1,'commendStationInput2':commendStationInput2,'commendStationInputType2':commendStationInputType2,'commendStationInputState2':commendStationInputState2,'commendStationInput3':commendStationInput3,'commendStationInputType3':commendStationInputType3,'commendStationInputState3':commendStationInputState3,'commendStationEB2E2AInput1':commendStationEB2E2AInput1,'commendStationEB2E2AInputType1':commendStationEB2E2AInputType1,'commendStationEB2E2AInputState1':commendStationEB2E2AInputState1,'commendStationEB2E2AInput2':commendStationEB2E2AInput2,'commendStationEB2E2AInputType2':commendStationEB2E2AInputType2,'commendStationEB2E2AInputState2':commendStationEB2E2AInputState2,'commendStationInputNotifications':commendStationInputNotifications,'commendStationInputButtonStuckNotification':commendStationInputButtonStuckNotification,'commendStationInputHandsetOffhookNotification':commendStationInputHandsetOffhookNotification,'commendStationInputChangedNotification':commendStationInputChangedNotification,'commendStationInputKeyboard':commendStationInputKeyboard,'commendStationInputKeyboardButton1':commendStationInputKeyboardButton1,'commendStationInputKeyboardButton2':commendStationInputKeyboardButton2,'commendStationInputKeyboardButton3':commendStationInputKeyboardButton3,'commendStationInputFullKeyboard':commendStationInputFullKeyboard,'commendStationInputFullKeyboardButton1':commendStationInputFullKeyboardButton1,'commendStationInputFullKeyboardButton2':commendStationInputFullKeyboardButton2,'commendStationInputFullKeyboardButton3':commendStationInputFullKeyboardButton3,'commendStationInputFullKeyboardButton4':commendStationInputFullKeyboardButton4,'commendStationInputFullKeyboardButton5':commendStationInputFullKeyboardButton5,'commendStationInputFullKeyboardButton6':commendStationInputFullKeyboardButton6,'commendStationInputFullKeyboardButton7':commendStationInputFullKeyboardButton7,'commendStationInputFullKeyboardButton8':commendStationInputFullKeyboardButton8,'commendStationInputFullKeyboardButton9':commendStationInputFullKeyboardButton9,'commendStationInputFullKeyboardButton0':commendStationInputFullKeyboardButton0,'commendStationInputFullKeyboardButtonX':commendStationInputFullKeyboardButtonX,'commendStationInputFullKeyboardButtonT':commendStationInputFullKeyboardButtonT,'commendStationInputFullKeyboardButtonUP':commendStationInputFullKeyboardButtonUP,'commendStationInputFullKeyboardButtonDOWN':commendStationInputFullKeyboardButtonDOWN,'commendStationInputFullKeyboardButtonMENU':commendStationInputFullKeyboardButtonMENU,'commendStationInputFullKeyboardButtonENTER':commendStationInputFullKeyboardButtonENTER,'commendStationInputTable':commendStationInputTable,'inputTableEntry':inputTableEntry,_G:inputName,'inputState':inputState,'commendStationInputStatus':commendStationInputStatus,'commendStationOutputs':commendStationOutputs,'commendStationLastInputChange':commendStationLastInputChange,'commendStationOutput1':commendStationOutput1,'commendStationOutputName1':commendStationOutputName1,'commendStationOutputState1':commendStationOutputState1,'commendStationOutput1Notifications':commendStationOutput1Notifications,'commendStationLastButtonStuck':commendStationLastButtonStuck,'commendStationOutput2':commendStationOutput2,'commendStationOutputName2':commendStationOutputName2,'commendStationOutputState2':commendStationOutputState2,'commendStationOutput2Notifications':commendStationOutput2Notifications,'commendStationEB2E2AOutput1':commendStationEB2E2AOutput1,'commendStationEB2E2AOutputName1':commendStationEB2E2AOutputName1,'commendStationEB2E2AOutputState1':commendStationEB2E2AOutputState1,'commendStationEB2E2AOutput1Notifications':commendStationEB2E2AOutput1Notifications,'commendStationEB2E2AOutput2':commendStationEB2E2AOutput2,'commendStationEB2E2AOutputName2':commendStationEB2E2AOutputName2,'commendStationEB2E2AOutputState2':commendStationEB2E2AOutputState2,'commendStationEB2E2AOutput2Notifications':commendStationEB2E2AOutput2Notifications,'commendStationOutputNotifications':commendStationOutputNotifications,'commendStationOutputChangedNotification':commendStationOutputChangedNotification,'commendStationOutputTable':commendStationOutputTable,'outputTableEntry':outputTableEntry,_H:outputName,'outputState':outputState,'commendStationOutputStatus':commendStationOutputStatus,'commendStationLastOutputChange':commendStationLastOutputChange,'commendStationObjectStatusNotifications':commendStationObjectStatusNotifications,'commendStationApplicationStart':commendStationApplicationStart})