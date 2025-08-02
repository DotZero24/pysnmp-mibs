_A7='sspmSinkStatus'
_A6='sspmSinkStorageType'
_A5='sspmSinkLastSequenceInvalid'
_A4='sspmSinkLastSequenceNumber'
_A3='sspmSinkExpectedFirstSequenceNum'
_A2='sspmSinkEnable'
_A1='sspmSinkExpectedRate'
_A0='sspmSinkSourceAddress'
_z='sspmSinkSourceAddressType'
_y='sspmSinkType'
_x='sspmSourceControlStatus'
_w='sspmSourceControlStorageType'
_v='sspmSourceControlOwner'
_u='sspmSourceControlLastSeqNum'
_t='sspmSourceControlFirstSeqNum'
_s='sspmSourceControlFrequency'
_r='sspmSourceControlSamplingDist'
_q='sspmSourceControlTimeOut'
_p='sspmSourceControlEnabled'
_o='sspmSourceControlDestAddr'
_n='sspmSourceControlDestAddrType'
_m='sspmSourceControlSrc'
_l='sspmSourceControlProfile'
_k='sspmSourceProfileStatus'
_j='sspmSourceProfileStorageType'
_i='sspmSourceProfileOwner'
_h='sspmSourceProfileParameter'
_g='sspmSourceProfile8021Tagging'
_f='sspmSourceProfileNoFrag'
_e='sspmSourceProfileTTL'
_d='sspmSourceProfileLooseSrcRteLen'
_c='sspmSourceProfileLooseSrcRteFill'
_b='sspmSourceProfileFlowLabel'
_a='sspmSourceProfileTOS'
_Z='sspmSourceProfilePacketFillValue'
_Y='sspmSourceProfilePacketFillType'
_X='sspmSourceProfilePacketSize'
_W='sspmSourceProfileType'
_V='sspmGeneralMinFrequency'
_U='sspmGeneralClockSource'
_T='sspmGeneralClockMaxSkew'
_S='sspmGeneralClockResolution'
_R='sspmSinkInstance'
_Q='sspmSourceControlInstance'
_P='sspmSourceProfileInstance'
_O='sspmUserPassGroup'
_N='sspmSinkGroup'
_M='sspmSourceGroup'
_L='sspmSourceProfilePassword'
_K='sspmSourceProfileUsername'
_J='not-accessible'
_I='sspmCapabilitiesInstance'
_H='sspmGeneralGroup'
_G='Unsigned32'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='SSPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AppLocalIndex,=mibBuilder.importSymbols('APM-MIB','AppLocalIndex')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
OwnerString,rmon=mibBuilder.importSymbols('RMON-MIB','OwnerString','rmon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue')
Utf8String,=mibBuilder.importSymbols('SYSAPPL-MIB','Utf8String')
sspmMIB=ModuleIdentity((1,3,6,1,2,1,16,28))
if mibBuilder.loadTexts:sspmMIB.setRevisions(('2005-07-28 00:00',))
class SspmMicroSeconds(TextualConvention,Unsigned32):status=_A;displayHint='d'
class SspmClockSource(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class SspmClockMaxSkew(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SspmMIBObjects_ObjectIdentity=ObjectIdentity
sspmMIBObjects=_SspmMIBObjects_ObjectIdentity((1,3,6,1,2,1,16,28,1))
_SspmGeneral_ObjectIdentity=ObjectIdentity
sspmGeneral=_SspmGeneral_ObjectIdentity((1,3,6,1,2,1,16,28,1,1))
_SspmGeneralClockResolution_Type=SspmMicroSeconds
_SspmGeneralClockResolution_Object=MibScalar
sspmGeneralClockResolution=_SspmGeneralClockResolution_Object((1,3,6,1,2,1,16,28,1,1,1),_SspmGeneralClockResolution_Type())
sspmGeneralClockResolution.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmGeneralClockResolution.setStatus(_A)
_SspmGeneralClockMaxSkew_Type=SspmClockMaxSkew
_SspmGeneralClockMaxSkew_Object=MibScalar
sspmGeneralClockMaxSkew=_SspmGeneralClockMaxSkew_Object((1,3,6,1,2,1,16,28,1,1,2),_SspmGeneralClockMaxSkew_Type())
sspmGeneralClockMaxSkew.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmGeneralClockMaxSkew.setStatus(_A)
_SspmGeneralClockSource_Type=SspmClockSource
_SspmGeneralClockSource_Object=MibScalar
sspmGeneralClockSource=_SspmGeneralClockSource_Object((1,3,6,1,2,1,16,28,1,1,3),_SspmGeneralClockSource_Type())
sspmGeneralClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmGeneralClockSource.setStatus(_A)
_SspmGeneralMinFrequency_Type=SspmMicroSeconds
_SspmGeneralMinFrequency_Object=MibScalar
sspmGeneralMinFrequency=_SspmGeneralMinFrequency_Object((1,3,6,1,2,1,16,28,1,1,4),_SspmGeneralMinFrequency_Type())
sspmGeneralMinFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmGeneralMinFrequency.setStatus(_A)
_SspmCapabilitiesTable_Object=MibTable
sspmCapabilitiesTable=_SspmCapabilitiesTable_Object((1,3,6,1,2,1,16,28,1,1,5))
if mibBuilder.loadTexts:sspmCapabilitiesTable.setStatus(_A)
_SspmCapabilitiesEntry_Object=MibTableRow
sspmCapabilitiesEntry=_SspmCapabilitiesEntry_Object((1,3,6,1,2,1,16,28,1,1,5,1))
sspmCapabilitiesEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:sspmCapabilitiesEntry.setStatus(_A)
_SspmCapabilitiesInstance_Type=AppLocalIndex
_SspmCapabilitiesInstance_Object=MibTableColumn
sspmCapabilitiesInstance=_SspmCapabilitiesInstance_Object((1,3,6,1,2,1,16,28,1,1,5,1,1),_SspmCapabilitiesInstance_Type())
sspmCapabilitiesInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmCapabilitiesInstance.setStatus(_A)
_SspmSource_ObjectIdentity=ObjectIdentity
sspmSource=_SspmSource_ObjectIdentity((1,3,6,1,2,1,16,28,1,2))
_SspmSourceProfileTable_Object=MibTable
sspmSourceProfileTable=_SspmSourceProfileTable_Object((1,3,6,1,2,1,16,28,1,2,1))
if mibBuilder.loadTexts:sspmSourceProfileTable.setStatus(_A)
_SspmSourceProfileEntry_Object=MibTableRow
sspmSourceProfileEntry=_SspmSourceProfileEntry_Object((1,3,6,1,2,1,16,28,1,2,1,1))
sspmSourceProfileEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:sspmSourceProfileEntry.setStatus(_A)
class _SspmSourceProfileInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SspmSourceProfileInstance_Type.__name__=_G
_SspmSourceProfileInstance_Object=MibTableColumn
sspmSourceProfileInstance=_SspmSourceProfileInstance_Object((1,3,6,1,2,1,16,28,1,2,1,1,1),_SspmSourceProfileInstance_Type())
sspmSourceProfileInstance.setMaxAccess(_J)
if mibBuilder.loadTexts:sspmSourceProfileInstance.setStatus(_A)
_SspmSourceProfileType_Type=AppLocalIndex
_SspmSourceProfileType_Object=MibTableColumn
sspmSourceProfileType=_SspmSourceProfileType_Object((1,3,6,1,2,1,16,28,1,2,1,1,2),_SspmSourceProfileType_Type())
sspmSourceProfileType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileType.setStatus(_A)
_SspmSourceProfilePacketSize_Type=Unsigned32
_SspmSourceProfilePacketSize_Object=MibTableColumn
sspmSourceProfilePacketSize=_SspmSourceProfilePacketSize_Object((1,3,6,1,2,1,16,28,1,2,1,1,3),_SspmSourceProfilePacketSize_Type())
sspmSourceProfilePacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfilePacketSize.setStatus(_A)
class _SspmSourceProfilePacketFillType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('random',1),('pattern',2),('url',3)))
_SspmSourceProfilePacketFillType_Type.__name__=_D
_SspmSourceProfilePacketFillType_Object=MibTableColumn
sspmSourceProfilePacketFillType=_SspmSourceProfilePacketFillType_Object((1,3,6,1,2,1,16,28,1,2,1,1,4),_SspmSourceProfilePacketFillType_Type())
sspmSourceProfilePacketFillType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfilePacketFillType.setStatus(_A)
class _SspmSourceProfilePacketFillValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SspmSourceProfilePacketFillValue_Type.__name__=_F
_SspmSourceProfilePacketFillValue_Object=MibTableColumn
sspmSourceProfilePacketFillValue=_SspmSourceProfilePacketFillValue_Object((1,3,6,1,2,1,16,28,1,2,1,1,5),_SspmSourceProfilePacketFillValue_Type())
sspmSourceProfilePacketFillValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfilePacketFillValue.setStatus(_A)
class _SspmSourceProfileTOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SspmSourceProfileTOS_Type.__name__=_D
_SspmSourceProfileTOS_Object=MibTableColumn
sspmSourceProfileTOS=_SspmSourceProfileTOS_Object((1,3,6,1,2,1,16,28,1,2,1,1,6),_SspmSourceProfileTOS_Type())
sspmSourceProfileTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileTOS.setStatus(_A)
class _SspmSourceProfileFlowLabel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_SspmSourceProfileFlowLabel_Type.__name__=_D
_SspmSourceProfileFlowLabel_Object=MibTableColumn
sspmSourceProfileFlowLabel=_SspmSourceProfileFlowLabel_Object((1,3,6,1,2,1,16,28,1,2,1,1,7),_SspmSourceProfileFlowLabel_Type())
sspmSourceProfileFlowLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileFlowLabel.setStatus(_A)
class _SspmSourceProfileLooseSrcRteFill_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_SspmSourceProfileLooseSrcRteFill_Type.__name__=_F
_SspmSourceProfileLooseSrcRteFill_Object=MibTableColumn
sspmSourceProfileLooseSrcRteFill=_SspmSourceProfileLooseSrcRteFill_Object((1,3,6,1,2,1,16,28,1,2,1,1,8),_SspmSourceProfileLooseSrcRteFill_Type())
sspmSourceProfileLooseSrcRteFill.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileLooseSrcRteFill.setStatus(_A)
class _SspmSourceProfileLooseSrcRteLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_SspmSourceProfileLooseSrcRteLen_Type.__name__=_D
_SspmSourceProfileLooseSrcRteLen_Object=MibTableColumn
sspmSourceProfileLooseSrcRteLen=_SspmSourceProfileLooseSrcRteLen_Object((1,3,6,1,2,1,16,28,1,2,1,1,9),_SspmSourceProfileLooseSrcRteLen_Type())
sspmSourceProfileLooseSrcRteLen.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileLooseSrcRteLen.setStatus(_A)
class _SspmSourceProfileTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SspmSourceProfileTTL_Type.__name__=_D
_SspmSourceProfileTTL_Object=MibTableColumn
sspmSourceProfileTTL=_SspmSourceProfileTTL_Object((1,3,6,1,2,1,16,28,1,2,1,1,10),_SspmSourceProfileTTL_Type())
sspmSourceProfileTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileTTL.setStatus(_A)
_SspmSourceProfileNoFrag_Type=TruthValue
_SspmSourceProfileNoFrag_Object=MibTableColumn
sspmSourceProfileNoFrag=_SspmSourceProfileNoFrag_Object((1,3,6,1,2,1,16,28,1,2,1,1,11),_SspmSourceProfileNoFrag_Type())
sspmSourceProfileNoFrag.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileNoFrag.setStatus(_A)
class _SspmSourceProfile8021Tagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_SspmSourceProfile8021Tagging_Type.__name__=_D
_SspmSourceProfile8021Tagging_Object=MibTableColumn
sspmSourceProfile8021Tagging=_SspmSourceProfile8021Tagging_Object((1,3,6,1,2,1,16,28,1,2,1,1,12),_SspmSourceProfile8021Tagging_Type())
sspmSourceProfile8021Tagging.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfile8021Tagging.setStatus(_A)
_SspmSourceProfileUsername_Type=Utf8String
_SspmSourceProfileUsername_Object=MibTableColumn
sspmSourceProfileUsername=_SspmSourceProfileUsername_Object((1,3,6,1,2,1,16,28,1,2,1,1,13),_SspmSourceProfileUsername_Type())
sspmSourceProfileUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileUsername.setStatus(_A)
_SspmSourceProfilePassword_Type=Utf8String
_SspmSourceProfilePassword_Object=MibTableColumn
sspmSourceProfilePassword=_SspmSourceProfilePassword_Object((1,3,6,1,2,1,16,28,1,2,1,1,14),_SspmSourceProfilePassword_Type())
sspmSourceProfilePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfilePassword.setStatus(_A)
class _SspmSourceProfileParameter_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_SspmSourceProfileParameter_Type.__name__=_F
_SspmSourceProfileParameter_Object=MibTableColumn
sspmSourceProfileParameter=_SspmSourceProfileParameter_Object((1,3,6,1,2,1,16,28,1,2,1,1,15),_SspmSourceProfileParameter_Type())
sspmSourceProfileParameter.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileParameter.setStatus(_A)
_SspmSourceProfileOwner_Type=OwnerString
_SspmSourceProfileOwner_Object=MibTableColumn
sspmSourceProfileOwner=_SspmSourceProfileOwner_Object((1,3,6,1,2,1,16,28,1,2,1,1,16),_SspmSourceProfileOwner_Type())
sspmSourceProfileOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileOwner.setStatus(_A)
_SspmSourceProfileStorageType_Type=StorageType
_SspmSourceProfileStorageType_Object=MibTableColumn
sspmSourceProfileStorageType=_SspmSourceProfileStorageType_Object((1,3,6,1,2,1,16,28,1,2,1,1,17),_SspmSourceProfileStorageType_Type())
sspmSourceProfileStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileStorageType.setStatus(_A)
_SspmSourceProfileStatus_Type=RowStatus
_SspmSourceProfileStatus_Object=MibTableColumn
sspmSourceProfileStatus=_SspmSourceProfileStatus_Object((1,3,6,1,2,1,16,28,1,2,1,1,18),_SspmSourceProfileStatus_Type())
sspmSourceProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceProfileStatus.setStatus(_A)
_SspmSourceControlTable_Object=MibTable
sspmSourceControlTable=_SspmSourceControlTable_Object((1,3,6,1,2,1,16,28,1,2,2))
if mibBuilder.loadTexts:sspmSourceControlTable.setStatus(_A)
_SspmSourceControlEntry_Object=MibTableRow
sspmSourceControlEntry=_SspmSourceControlEntry_Object((1,3,6,1,2,1,16,28,1,2,2,1))
sspmSourceControlEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:sspmSourceControlEntry.setStatus(_A)
class _SspmSourceControlInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SspmSourceControlInstance_Type.__name__=_G
_SspmSourceControlInstance_Object=MibTableColumn
sspmSourceControlInstance=_SspmSourceControlInstance_Object((1,3,6,1,2,1,16,28,1,2,2,1,1),_SspmSourceControlInstance_Type())
sspmSourceControlInstance.setMaxAccess(_J)
if mibBuilder.loadTexts:sspmSourceControlInstance.setStatus(_A)
class _SspmSourceControlProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SspmSourceControlProfile_Type.__name__=_D
_SspmSourceControlProfile_Object=MibTableColumn
sspmSourceControlProfile=_SspmSourceControlProfile_Object((1,3,6,1,2,1,16,28,1,2,2,1,2),_SspmSourceControlProfile_Type())
sspmSourceControlProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlProfile.setStatus(_A)
_SspmSourceControlSrc_Type=InterfaceIndexOrZero
_SspmSourceControlSrc_Object=MibTableColumn
sspmSourceControlSrc=_SspmSourceControlSrc_Object((1,3,6,1,2,1,16,28,1,2,2,1,3),_SspmSourceControlSrc_Type())
sspmSourceControlSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlSrc.setStatus(_A)
_SspmSourceControlDestAddrType_Type=InetAddressType
_SspmSourceControlDestAddrType_Object=MibTableColumn
sspmSourceControlDestAddrType=_SspmSourceControlDestAddrType_Object((1,3,6,1,2,1,16,28,1,2,2,1,4),_SspmSourceControlDestAddrType_Type())
sspmSourceControlDestAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlDestAddrType.setStatus(_A)
_SspmSourceControlDestAddr_Type=InetAddress
_SspmSourceControlDestAddr_Object=MibTableColumn
sspmSourceControlDestAddr=_SspmSourceControlDestAddr_Object((1,3,6,1,2,1,16,28,1,2,2,1,5),_SspmSourceControlDestAddr_Type())
sspmSourceControlDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlDestAddr.setStatus(_A)
_SspmSourceControlEnabled_Type=TruthValue
_SspmSourceControlEnabled_Object=MibTableColumn
sspmSourceControlEnabled=_SspmSourceControlEnabled_Object((1,3,6,1,2,1,16,28,1,2,2,1,6),_SspmSourceControlEnabled_Type())
sspmSourceControlEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlEnabled.setStatus(_A)
_SspmSourceControlTimeOut_Type=SspmMicroSeconds
_SspmSourceControlTimeOut_Object=MibTableColumn
sspmSourceControlTimeOut=_SspmSourceControlTimeOut_Object((1,3,6,1,2,1,16,28,1,2,2,1,7),_SspmSourceControlTimeOut_Type())
sspmSourceControlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlTimeOut.setStatus(_A)
class _SspmSourceControlSamplingDist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deterministic',1),('poisson',2)))
_SspmSourceControlSamplingDist_Type.__name__=_D
_SspmSourceControlSamplingDist_Object=MibTableColumn
sspmSourceControlSamplingDist=_SspmSourceControlSamplingDist_Object((1,3,6,1,2,1,16,28,1,2,2,1,8),_SspmSourceControlSamplingDist_Type())
sspmSourceControlSamplingDist.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlSamplingDist.setStatus(_A)
_SspmSourceControlFrequency_Type=SspmMicroSeconds
_SspmSourceControlFrequency_Object=MibTableColumn
sspmSourceControlFrequency=_SspmSourceControlFrequency_Object((1,3,6,1,2,1,16,28,1,2,2,1,9),_SspmSourceControlFrequency_Type())
sspmSourceControlFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlFrequency.setStatus(_A)
_SspmSourceControlFirstSeqNum_Type=Unsigned32
_SspmSourceControlFirstSeqNum_Object=MibTableColumn
sspmSourceControlFirstSeqNum=_SspmSourceControlFirstSeqNum_Object((1,3,6,1,2,1,16,28,1,2,2,1,10),_SspmSourceControlFirstSeqNum_Type())
sspmSourceControlFirstSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlFirstSeqNum.setStatus(_A)
_SspmSourceControlLastSeqNum_Type=Unsigned32
_SspmSourceControlLastSeqNum_Object=MibTableColumn
sspmSourceControlLastSeqNum=_SspmSourceControlLastSeqNum_Object((1,3,6,1,2,1,16,28,1,2,2,1,11),_SspmSourceControlLastSeqNum_Type())
sspmSourceControlLastSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmSourceControlLastSeqNum.setStatus(_A)
_SspmSourceControlOwner_Type=OwnerString
_SspmSourceControlOwner_Object=MibTableColumn
sspmSourceControlOwner=_SspmSourceControlOwner_Object((1,3,6,1,2,1,16,28,1,2,2,1,12),_SspmSourceControlOwner_Type())
sspmSourceControlOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlOwner.setStatus(_A)
_SspmSourceControlStorageType_Type=StorageType
_SspmSourceControlStorageType_Object=MibTableColumn
sspmSourceControlStorageType=_SspmSourceControlStorageType_Object((1,3,6,1,2,1,16,28,1,2,2,1,13),_SspmSourceControlStorageType_Type())
sspmSourceControlStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlStorageType.setStatus(_A)
_SspmSourceControlStatus_Type=RowStatus
_SspmSourceControlStatus_Object=MibTableColumn
sspmSourceControlStatus=_SspmSourceControlStatus_Object((1,3,6,1,2,1,16,28,1,2,2,1,14),_SspmSourceControlStatus_Type())
sspmSourceControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSourceControlStatus.setStatus(_A)
_SspmSink_ObjectIdentity=ObjectIdentity
sspmSink=_SspmSink_ObjectIdentity((1,3,6,1,2,1,16,28,1,5))
_SspmSinkTable_Object=MibTable
sspmSinkTable=_SspmSinkTable_Object((1,3,6,1,2,1,16,28,1,5,1))
if mibBuilder.loadTexts:sspmSinkTable.setStatus(_A)
_SspmSinkEntry_Object=MibTableRow
sspmSinkEntry=_SspmSinkEntry_Object((1,3,6,1,2,1,16,28,1,5,1,1))
sspmSinkEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:sspmSinkEntry.setStatus(_A)
class _SspmSinkInstance_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SspmSinkInstance_Type.__name__=_G
_SspmSinkInstance_Object=MibTableColumn
sspmSinkInstance=_SspmSinkInstance_Object((1,3,6,1,2,1,16,28,1,5,1,1,1),_SspmSinkInstance_Type())
sspmSinkInstance.setMaxAccess(_J)
if mibBuilder.loadTexts:sspmSinkInstance.setStatus(_A)
_SspmSinkType_Type=AppLocalIndex
_SspmSinkType_Object=MibTableColumn
sspmSinkType=_SspmSinkType_Object((1,3,6,1,2,1,16,28,1,5,1,1,2),_SspmSinkType_Type())
sspmSinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkType.setStatus(_A)
_SspmSinkSourceAddressType_Type=InetAddressType
_SspmSinkSourceAddressType_Object=MibTableColumn
sspmSinkSourceAddressType=_SspmSinkSourceAddressType_Object((1,3,6,1,2,1,16,28,1,5,1,1,3),_SspmSinkSourceAddressType_Type())
sspmSinkSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkSourceAddressType.setStatus(_A)
_SspmSinkSourceAddress_Type=InetAddress
_SspmSinkSourceAddress_Object=MibTableColumn
sspmSinkSourceAddress=_SspmSinkSourceAddress_Object((1,3,6,1,2,1,16,28,1,5,1,1,4),_SspmSinkSourceAddress_Type())
sspmSinkSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkSourceAddress.setStatus(_A)
_SspmSinkExpectedRate_Type=SspmMicroSeconds
_SspmSinkExpectedRate_Object=MibTableColumn
sspmSinkExpectedRate=_SspmSinkExpectedRate_Object((1,3,6,1,2,1,16,28,1,5,1,1,5),_SspmSinkExpectedRate_Type())
sspmSinkExpectedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkExpectedRate.setStatus(_A)
_SspmSinkEnable_Type=TruthValue
_SspmSinkEnable_Object=MibTableColumn
sspmSinkEnable=_SspmSinkEnable_Object((1,3,6,1,2,1,16,28,1,5,1,1,6),_SspmSinkEnable_Type())
sspmSinkEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkEnable.setStatus(_A)
_SspmSinkExpectedFirstSequenceNum_Type=Unsigned32
_SspmSinkExpectedFirstSequenceNum_Object=MibTableColumn
sspmSinkExpectedFirstSequenceNum=_SspmSinkExpectedFirstSequenceNum_Object((1,3,6,1,2,1,16,28,1,5,1,1,7),_SspmSinkExpectedFirstSequenceNum_Type())
sspmSinkExpectedFirstSequenceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkExpectedFirstSequenceNum.setStatus(_A)
_SspmSinkLastSequenceNumber_Type=Unsigned32
_SspmSinkLastSequenceNumber_Object=MibTableColumn
sspmSinkLastSequenceNumber=_SspmSinkLastSequenceNumber_Object((1,3,6,1,2,1,16,28,1,5,1,1,8),_SspmSinkLastSequenceNumber_Type())
sspmSinkLastSequenceNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmSinkLastSequenceNumber.setStatus(_A)
_SspmSinkLastSequenceInvalid_Type=Counter32
_SspmSinkLastSequenceInvalid_Object=MibTableColumn
sspmSinkLastSequenceInvalid=_SspmSinkLastSequenceInvalid_Object((1,3,6,1,2,1,16,28,1,5,1,1,9),_SspmSinkLastSequenceInvalid_Type())
sspmSinkLastSequenceInvalid.setMaxAccess(_E)
if mibBuilder.loadTexts:sspmSinkLastSequenceInvalid.setStatus(_A)
_SspmSinkStorageType_Type=StorageType
_SspmSinkStorageType_Object=MibTableColumn
sspmSinkStorageType=_SspmSinkStorageType_Object((1,3,6,1,2,1,16,28,1,5,1,1,10),_SspmSinkStorageType_Type())
sspmSinkStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkStorageType.setStatus(_A)
_SspmSinkStatus_Type=RowStatus
_SspmSinkStatus_Object=MibTableColumn
sspmSinkStatus=_SspmSinkStatus_Object((1,3,6,1,2,1,16,28,1,5,1,1,11),_SspmSinkStatus_Type())
sspmSinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sspmSinkStatus.setStatus(_A)
_SspmMIBNotifications_ObjectIdentity=ObjectIdentity
sspmMIBNotifications=_SspmMIBNotifications_ObjectIdentity((1,3,6,1,2,1,16,28,2))
_SspmMIBConformance_ObjectIdentity=ObjectIdentity
sspmMIBConformance=_SspmMIBConformance_ObjectIdentity((1,3,6,1,2,1,16,28,3))
_SspmCompliances_ObjectIdentity=ObjectIdentity
sspmCompliances=_SspmCompliances_ObjectIdentity((1,3,6,1,2,1,16,28,3,1))
_SspmGroups_ObjectIdentity=ObjectIdentity
sspmGroups=_SspmGroups_ObjectIdentity((1,3,6,1,2,1,16,28,3,2))
sspmGeneralGroup=ObjectGroup((1,3,6,1,2,1,16,28,3,2,1))
sspmGeneralGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_I)))
if mibBuilder.loadTexts:sspmGeneralGroup.setStatus(_A)
sspmSourceGroup=ObjectGroup((1,3,6,1,2,1,16,28,3,2,2))
sspmSourceGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_K),(_B,_L),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:sspmSourceGroup.setStatus(_A)
sspmUserPassGroup=ObjectGroup((1,3,6,1,2,1,16,28,3,2,3))
sspmUserPassGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:sspmUserPassGroup.setStatus(_A)
sspmSinkGroup=ObjectGroup((1,3,6,1,2,1,16,28,3,2,4))
sspmSinkGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:sspmSinkGroup.setStatus(_A)
sspmGeneralCompliance=ModuleCompliance((1,3,6,1,2,1,16,28,3,1,1))
sspmGeneralCompliance.setObjects(*((_B,_H),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:sspmGeneralCompliance.setStatus(_A)
sspmSourceFullCompliance=ModuleCompliance((1,3,6,1,2,1,16,28,3,1,2))
sspmSourceFullCompliance.setObjects(*((_B,_H),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:sspmSourceFullCompliance.setStatus(_A)
sspmSinkFullCompliance=ModuleCompliance((1,3,6,1,2,1,16,28,3,1,3))
sspmSinkFullCompliance.setObjects(*((_B,_H),(_B,_N)))
if mibBuilder.loadTexts:sspmSinkFullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SspmMicroSeconds':SspmMicroSeconds,'SspmClockSource':SspmClockSource,'SspmClockMaxSkew':SspmClockMaxSkew,'sspmMIB':sspmMIB,'sspmMIBObjects':sspmMIBObjects,'sspmGeneral':sspmGeneral,_S:sspmGeneralClockResolution,_T:sspmGeneralClockMaxSkew,_U:sspmGeneralClockSource,_V:sspmGeneralMinFrequency,'sspmCapabilitiesTable':sspmCapabilitiesTable,'sspmCapabilitiesEntry':sspmCapabilitiesEntry,_I:sspmCapabilitiesInstance,'sspmSource':sspmSource,'sspmSourceProfileTable':sspmSourceProfileTable,'sspmSourceProfileEntry':sspmSourceProfileEntry,_P:sspmSourceProfileInstance,_W:sspmSourceProfileType,_X:sspmSourceProfilePacketSize,_Y:sspmSourceProfilePacketFillType,_Z:sspmSourceProfilePacketFillValue,_a:sspmSourceProfileTOS,_b:sspmSourceProfileFlowLabel,_c:sspmSourceProfileLooseSrcRteFill,_d:sspmSourceProfileLooseSrcRteLen,_e:sspmSourceProfileTTL,_f:sspmSourceProfileNoFrag,_g:sspmSourceProfile8021Tagging,_K:sspmSourceProfileUsername,_L:sspmSourceProfilePassword,_h:sspmSourceProfileParameter,_i:sspmSourceProfileOwner,_j:sspmSourceProfileStorageType,_k:sspmSourceProfileStatus,'sspmSourceControlTable':sspmSourceControlTable,'sspmSourceControlEntry':sspmSourceControlEntry,_Q:sspmSourceControlInstance,_l:sspmSourceControlProfile,_m:sspmSourceControlSrc,_n:sspmSourceControlDestAddrType,_o:sspmSourceControlDestAddr,_p:sspmSourceControlEnabled,_q:sspmSourceControlTimeOut,_r:sspmSourceControlSamplingDist,_s:sspmSourceControlFrequency,_t:sspmSourceControlFirstSeqNum,_u:sspmSourceControlLastSeqNum,_v:sspmSourceControlOwner,_w:sspmSourceControlStorageType,_x:sspmSourceControlStatus,'sspmSink':sspmSink,'sspmSinkTable':sspmSinkTable,'sspmSinkEntry':sspmSinkEntry,_R:sspmSinkInstance,_y:sspmSinkType,_z:sspmSinkSourceAddressType,_A0:sspmSinkSourceAddress,_A1:sspmSinkExpectedRate,_A2:sspmSinkEnable,_A3:sspmSinkExpectedFirstSequenceNum,_A4:sspmSinkLastSequenceNumber,_A5:sspmSinkLastSequenceInvalid,_A6:sspmSinkStorageType,_A7:sspmSinkStatus,'sspmMIBNotifications':sspmMIBNotifications,'sspmMIBConformance':sspmMIBConformance,'sspmCompliances':sspmCompliances,'sspmGeneralCompliance':sspmGeneralCompliance,'sspmSourceFullCompliance':sspmSourceFullCompliance,'sspmSinkFullCompliance':sspmSinkFullCompliance,'sspmGroups':sspmGroups,_H:sspmGeneralGroup,_M:sspmSourceGroup,_O:sspmUserPassGroup,_N:sspmSinkGroup})