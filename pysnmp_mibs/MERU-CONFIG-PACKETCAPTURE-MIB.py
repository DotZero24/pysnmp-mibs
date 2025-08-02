_E='mwPacketCaptureProfileTableIndex'
_D='MERU-CONFIG-PACKETCAPTURE-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlEnableDisableOption,MwlEncapsulationType,MwlOnOffSwitch,MwlPacketCaptureMode,MwlRateLimitMode,MwlRxTxOption=mibBuilder.importSymbols('MERU-TC','MwlEnableDisableOption','MwlEncapsulationType','MwlOnOffSwitch','MwlPacketCaptureMode','MwlRateLimitMode','MwlRxTxOption')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigPacketCapture=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,17))
_MwPacketCaptureProfileTable_Object=MibTable
mwPacketCaptureProfileTable=_MwPacketCaptureProfileTable_Object((1,3,6,1,4,1,15983,1,1,4,17,1))
if mibBuilder.loadTexts:mwPacketCaptureProfileTable.setStatus(_A)
_MwPacketCaptureProfileEntry_Object=MibTableRow
mwPacketCaptureProfileEntry=_MwPacketCaptureProfileEntry_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1))
mwPacketCaptureProfileEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mwPacketCaptureProfileEntry.setStatus(_A)
_MwPacketCaptureProfileTableIndex_Type=Integer32
_MwPacketCaptureProfileTableIndex_Object=MibTableColumn
mwPacketCaptureProfileTableIndex=_MwPacketCaptureProfileTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,1),_MwPacketCaptureProfileTableIndex_Type())
mwPacketCaptureProfileTableIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mwPacketCaptureProfileTableIndex.setStatus(_A)
class _MwPacketCaptureProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwPacketCaptureProfileName_Type.__name__=_C
_MwPacketCaptureProfileName_Object=MibTableColumn
mwPacketCaptureProfileName=_MwPacketCaptureProfileName_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,2),_MwPacketCaptureProfileName_Type())
mwPacketCaptureProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileName.setStatus(_A)
_MwPacketCaptureProfileStatus_Type=MwlEnableDisableOption
_MwPacketCaptureProfileStatus_Object=MibTableColumn
mwPacketCaptureProfileStatus=_MwPacketCaptureProfileStatus_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,3),_MwPacketCaptureProfileStatus_Type())
mwPacketCaptureProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileStatus.setStatus(_A)
_MwPacketCaptureProfileConnectivityMode_Type=MwlPacketCaptureMode
_MwPacketCaptureProfileConnectivityMode_Object=MibTableColumn
mwPacketCaptureProfileConnectivityMode=_MwPacketCaptureProfileConnectivityMode_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,4),_MwPacketCaptureProfileConnectivityMode_Type())
mwPacketCaptureProfileConnectivityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileConnectivityMode.setStatus(_A)
_MwPacketCaptureProfileDestinationIp_Type=IpAddress
_MwPacketCaptureProfileDestinationIp_Object=MibTableColumn
mwPacketCaptureProfileDestinationIp=_MwPacketCaptureProfileDestinationIp_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,5),_MwPacketCaptureProfileDestinationIp_Type())
mwPacketCaptureProfileDestinationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileDestinationIp.setStatus(_A)
_MwPacketCaptureProfileUDPPort_Type=Unsigned32
_MwPacketCaptureProfileUDPPort_Object=MibTableColumn
mwPacketCaptureProfileUDPPort=_MwPacketCaptureProfileUDPPort_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,6),_MwPacketCaptureProfileUDPPort_Type())
mwPacketCaptureProfileUDPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileUDPPort.setStatus(_A)
_MwPacketCaptureProfileDestinationMac_Type=MacAddress
_MwPacketCaptureProfileDestinationMac_Object=MibTableColumn
mwPacketCaptureProfileDestinationMac=_MwPacketCaptureProfileDestinationMac_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,7),_MwPacketCaptureProfileDestinationMac_Type())
mwPacketCaptureProfileDestinationMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileDestinationMac.setStatus(_A)
_MwPacketCaptureProfileRxTx_Type=MwlRxTxOption
_MwPacketCaptureProfileRxTx_Object=MibTableColumn
mwPacketCaptureProfileRxTx=_MwPacketCaptureProfileRxTx_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,8),_MwPacketCaptureProfileRxTx_Type())
mwPacketCaptureProfileRxTx.setMaxAccess('read-only')
if mibBuilder.loadTexts:mwPacketCaptureProfileRxTx.setStatus(_A)
_MwPacketCaptureProfileRateLimitMode_Type=MwlRateLimitMode
_MwPacketCaptureProfileRateLimitMode_Object=MibTableColumn
mwPacketCaptureProfileRateLimitMode=_MwPacketCaptureProfileRateLimitMode_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,9),_MwPacketCaptureProfileRateLimitMode_Type())
mwPacketCaptureProfileRateLimitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileRateLimitMode.setStatus(_A)
_MwPacketCaptureProfileTokenBucketRate_Type=Unsigned32
_MwPacketCaptureProfileTokenBucketRate_Object=MibTableColumn
mwPacketCaptureProfileTokenBucketRate=_MwPacketCaptureProfileTokenBucketRate_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,10),_MwPacketCaptureProfileTokenBucketRate_Type())
mwPacketCaptureProfileTokenBucketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileTokenBucketRate.setStatus(_A)
_MwPacketCaptureProfileTokenBucketSize_Type=Unsigned32
_MwPacketCaptureProfileTokenBucketSize_Object=MibTableColumn
mwPacketCaptureProfileTokenBucketSize=_MwPacketCaptureProfileTokenBucketSize_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,11),_MwPacketCaptureProfileTokenBucketSize_Type())
mwPacketCaptureProfileTokenBucketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileTokenBucketSize.setStatus(_A)
class _MwPacketCaptureProfileApList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1000))
_MwPacketCaptureProfileApList_Type.__name__=_C
_MwPacketCaptureProfileApList_Object=MibTableColumn
mwPacketCaptureProfileApList=_MwPacketCaptureProfileApList_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,12),_MwPacketCaptureProfileApList_Type())
mwPacketCaptureProfileApList.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileApList.setStatus(_A)
class _MwPacketCaptureProfileFilter_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MwPacketCaptureProfileFilter_Type.__name__=_C
_MwPacketCaptureProfileFilter_Object=MibTableColumn
mwPacketCaptureProfileFilter=_MwPacketCaptureProfileFilter_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,13),_MwPacketCaptureProfileFilter_Type())
mwPacketCaptureProfileFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileFilter.setStatus(_A)
class _MwPacketCaptureProfileInterfaceList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwPacketCaptureProfileInterfaceList_Type.__name__=_C
_MwPacketCaptureProfileInterfaceList_Object=MibTableColumn
mwPacketCaptureProfileInterfaceList=_MwPacketCaptureProfileInterfaceList_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,14),_MwPacketCaptureProfileInterfaceList_Type())
mwPacketCaptureProfileInterfaceList.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileInterfaceList.setStatus(_A)
_MwPacketCaptureProfilePacketTruncationLength_Type=Unsigned32
_MwPacketCaptureProfilePacketTruncationLength_Object=MibTableColumn
mwPacketCaptureProfilePacketTruncationLength=_MwPacketCaptureProfilePacketTruncationLength_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,15),_MwPacketCaptureProfilePacketTruncationLength_Type())
mwPacketCaptureProfilePacketTruncationLength.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfilePacketTruncationLength.setStatus(_A)
_MwPacketCaptureProfileRateLimiting_Type=MwlOnOffSwitch
_MwPacketCaptureProfileRateLimiting_Object=MibTableColumn
mwPacketCaptureProfileRateLimiting=_MwPacketCaptureProfileRateLimiting_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,16),_MwPacketCaptureProfileRateLimiting_Type())
mwPacketCaptureProfileRateLimiting.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileRateLimiting.setStatus(_A)
_MwPacketCaptureProfileCaptureSiblingFrames_Type=MwlOnOffSwitch
_MwPacketCaptureProfileCaptureSiblingFrames_Object=MibTableColumn
mwPacketCaptureProfileCaptureSiblingFrames=_MwPacketCaptureProfileCaptureSiblingFrames_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,17),_MwPacketCaptureProfileCaptureSiblingFrames_Type())
mwPacketCaptureProfileCaptureSiblingFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileCaptureSiblingFrames.setStatus(_A)
_MwPacketCaptureProfileEncapsulation_Type=MwlEncapsulationType
_MwPacketCaptureProfileEncapsulation_Object=MibTableColumn
mwPacketCaptureProfileEncapsulation=_MwPacketCaptureProfileEncapsulation_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,18),_MwPacketCaptureProfileEncapsulation_Type())
mwPacketCaptureProfileEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileEncapsulation.setStatus(_A)
_MwPacketCaptureProfileRowStatus_Type=RowStatus
_MwPacketCaptureProfileRowStatus_Object=MibTableColumn
mwPacketCaptureProfileRowStatus=_MwPacketCaptureProfileRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,17,1,1,19),_MwPacketCaptureProfileRowStatus_Type())
mwPacketCaptureProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPacketCaptureProfileRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigPacketCapture':mwConfigPacketCapture,'mwPacketCaptureProfileTable':mwPacketCaptureProfileTable,'mwPacketCaptureProfileEntry':mwPacketCaptureProfileEntry,_E:mwPacketCaptureProfileTableIndex,'mwPacketCaptureProfileName':mwPacketCaptureProfileName,'mwPacketCaptureProfileStatus':mwPacketCaptureProfileStatus,'mwPacketCaptureProfileConnectivityMode':mwPacketCaptureProfileConnectivityMode,'mwPacketCaptureProfileDestinationIp':mwPacketCaptureProfileDestinationIp,'mwPacketCaptureProfileUDPPort':mwPacketCaptureProfileUDPPort,'mwPacketCaptureProfileDestinationMac':mwPacketCaptureProfileDestinationMac,'mwPacketCaptureProfileRxTx':mwPacketCaptureProfileRxTx,'mwPacketCaptureProfileRateLimitMode':mwPacketCaptureProfileRateLimitMode,'mwPacketCaptureProfileTokenBucketRate':mwPacketCaptureProfileTokenBucketRate,'mwPacketCaptureProfileTokenBucketSize':mwPacketCaptureProfileTokenBucketSize,'mwPacketCaptureProfileApList':mwPacketCaptureProfileApList,'mwPacketCaptureProfileFilter':mwPacketCaptureProfileFilter,'mwPacketCaptureProfileInterfaceList':mwPacketCaptureProfileInterfaceList,'mwPacketCaptureProfilePacketTruncationLength':mwPacketCaptureProfilePacketTruncationLength,'mwPacketCaptureProfileRateLimiting':mwPacketCaptureProfileRateLimiting,'mwPacketCaptureProfileCaptureSiblingFrames':mwPacketCaptureProfileCaptureSiblingFrames,'mwPacketCaptureProfileEncapsulation':mwPacketCaptureProfileEncapsulation,'mwPacketCaptureProfileRowStatus':mwPacketCaptureProfileRowStatus})