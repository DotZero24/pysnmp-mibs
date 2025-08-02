_G='mwVoiceStatusTableIndex'
_F='mwPhoneCallTableIndex'
_E='mwPhoneTableIndex'
_D='not-accessible'
_C='MERU-VOICE-STATISTICS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwStatistics,=mibBuilder.importSymbols('MERU-SMI','mwStatistics')
MwlDeviceType,MwlNetProtocol,MwlOnOffSwitch,MwlQosCallState,MwlQosProtocol=mibBuilder.importSymbols('MERU-TC','MwlDeviceType','MwlNetProtocol','MwlOnOffSwitch','MwlQosCallState','MwlQosProtocol')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwVoiceStatistics=ModuleIdentity((1,3,6,1,4,1,15983,1,1,3,3))
_MwPhoneTable_Object=MibTable
mwPhoneTable=_MwPhoneTable_Object((1,3,6,1,4,1,15983,1,1,3,3,1))
if mibBuilder.loadTexts:mwPhoneTable.setStatus(_A)
_MwPhoneEntry_Object=MibTableRow
mwPhoneEntry=_MwPhoneEntry_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1))
mwPhoneEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:mwPhoneEntry.setStatus(_A)
_MwPhoneTableIndex_Type=Integer32
_MwPhoneTableIndex_Object=MibTableColumn
mwPhoneTableIndex=_MwPhoneTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,1),_MwPhoneTableIndex_Type())
mwPhoneTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwPhoneTableIndex.setStatus(_A)
_MwPhoneIp_Type=IpAddress
_MwPhoneIp_Object=MibTableColumn
mwPhoneIp=_MwPhoneIp_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,2),_MwPhoneIp_Type())
mwPhoneIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneIp.setStatus(_A)
_MwPhoneAp_Type=Integer32
_MwPhoneAp_Object=MibTableColumn
mwPhoneAp=_MwPhoneAp_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,3),_MwPhoneAp_Type())
mwPhoneAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneAp.setStatus(_A)
_MwPhoneMac_Type=MacAddress
_MwPhoneMac_Object=MibTableColumn
mwPhoneMac=_MwPhoneMac_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,4),_MwPhoneMac_Type())
mwPhoneMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneMac.setStatus(_A)
_MwPhoneType_Type=MwlQosProtocol
_MwPhoneType_Object=MibTableColumn
mwPhoneType=_MwPhoneType_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,5),_MwPhoneType_Type())
mwPhoneType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneType.setStatus(_A)
_MwPhoneApName_Type=DisplayString
_MwPhoneApName_Object=MibTableColumn
mwPhoneApName=_MwPhoneApName_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,6),_MwPhoneApName_Type())
mwPhoneApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneApName.setStatus(_A)
_MwPhoneServer_Type=DisplayString
_MwPhoneServer_Object=MibTableColumn
mwPhoneServer=_MwPhoneServer_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,7),_MwPhoneServer_Type())
mwPhoneServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneServer.setStatus(_A)
_MwPhoneUsername_Type=DisplayString
_MwPhoneUsername_Object=MibTableColumn
mwPhoneUsername=_MwPhoneUsername_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,8),_MwPhoneUsername_Type())
mwPhoneUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneUsername.setStatus(_A)
_MwPhoneTransport_Type=MwlNetProtocol
_MwPhoneTransport_Object=MibTableColumn
mwPhoneTransport=_MwPhoneTransport_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,9),_MwPhoneTransport_Type())
mwPhoneTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneTransport.setStatus(_A)
_MwPhoneDeviceType_Type=MwlDeviceType
_MwPhoneDeviceType_Object=MibTableColumn
mwPhoneDeviceType=_MwPhoneDeviceType_Object((1,3,6,1,4,1,15983,1,1,3,3,1,1,10),_MwPhoneDeviceType_Type())
mwPhoneDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneDeviceType.setStatus(_A)
_MwPhoneCallTable_Object=MibTable
mwPhoneCallTable=_MwPhoneCallTable_Object((1,3,6,1,4,1,15983,1,1,3,3,2))
if mibBuilder.loadTexts:mwPhoneCallTable.setStatus(_A)
_MwPhoneCallEntry_Object=MibTableRow
mwPhoneCallEntry=_MwPhoneCallEntry_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1))
mwPhoneCallEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mwPhoneCallEntry.setStatus(_A)
_MwPhoneCallTableIndex_Type=Integer32
_MwPhoneCallTableIndex_Object=MibTableColumn
mwPhoneCallTableIndex=_MwPhoneCallTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,1),_MwPhoneCallTableIndex_Type())
mwPhoneCallTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwPhoneCallTableIndex.setStatus(_A)
_MwPhoneCallToIp_Type=IpAddress
_MwPhoneCallToIp_Object=MibTableColumn
mwPhoneCallToIp=_MwPhoneCallToIp_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,2),_MwPhoneCallToIp_Type())
mwPhoneCallToIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToIp.setStatus(_A)
_MwPhoneCallToAp_Type=Integer32
_MwPhoneCallToAp_Object=MibTableColumn
mwPhoneCallToAp=_MwPhoneCallToAp_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,3),_MwPhoneCallToAp_Type())
mwPhoneCallToAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToAp.setStatus(_A)
_MwPhoneCallType_Type=MwlQosProtocol
_MwPhoneCallType_Object=MibTableColumn
mwPhoneCallType=_MwPhoneCallType_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,4),_MwPhoneCallType_Type())
mwPhoneCallType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallType.setStatus(_A)
_MwPhoneCallToMac_Type=MacAddress
_MwPhoneCallToMac_Object=MibTableColumn
mwPhoneCallToMac=_MwPhoneCallToMac_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,5),_MwPhoneCallToMac_Type())
mwPhoneCallToMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToMac.setStatus(_A)
_MwPhoneCallState_Type=MwlQosCallState
_MwPhoneCallState_Object=MibTableColumn
mwPhoneCallState=_MwPhoneCallState_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,6),_MwPhoneCallState_Type())
mwPhoneCallState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallState.setStatus(_A)
_MwPhoneCallFromIp_Type=IpAddress
_MwPhoneCallFromIp_Object=MibTableColumn
mwPhoneCallFromIp=_MwPhoneCallFromIp_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,7),_MwPhoneCallFromIp_Type())
mwPhoneCallFromIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromIp.setStatus(_A)
_MwPhoneCallFromAp_Type=Integer32
_MwPhoneCallFromAp_Object=MibTableColumn
mwPhoneCallFromAp=_MwPhoneCallFromAp_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,8),_MwPhoneCallFromAp_Type())
mwPhoneCallFromAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromAp.setStatus(_A)
_MwPhoneCallFromMac_Type=MacAddress
_MwPhoneCallFromMac_Object=MibTableColumn
mwPhoneCallFromMac=_MwPhoneCallFromMac_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,9),_MwPhoneCallFromMac_Type())
mwPhoneCallFromMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromMac.setStatus(_A)
_MwPhoneCallToApName_Type=DisplayString
_MwPhoneCallToApName_Object=MibTableColumn
mwPhoneCallToApName=_MwPhoneCallToApName_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,10),_MwPhoneCallToApName_Type())
mwPhoneCallToApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToApName.setStatus(_A)
_MwPhoneCallToFlowtag_Type=Integer32
_MwPhoneCallToFlowtag_Object=MibTableColumn
mwPhoneCallToFlowtag=_MwPhoneCallToFlowtag_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,11),_MwPhoneCallToFlowtag_Type())
mwPhoneCallToFlowtag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToFlowtag.setStatus(_A)
_MwPhoneCallToPending_Type=MwlOnOffSwitch
_MwPhoneCallToPending_Object=MibTableColumn
mwPhoneCallToPending=_MwPhoneCallToPending_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,12),_MwPhoneCallToPending_Type())
mwPhoneCallToPending.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToPending.setStatus(_A)
_MwPhoneCallFromApName_Type=DisplayString
_MwPhoneCallFromApName_Object=MibTableColumn
mwPhoneCallFromApName=_MwPhoneCallFromApName_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,13),_MwPhoneCallFromApName_Type())
mwPhoneCallFromApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromApName.setStatus(_A)
_MwPhoneCallToUsername_Type=DisplayString
_MwPhoneCallToUsername_Object=MibTableColumn
mwPhoneCallToUsername=_MwPhoneCallToUsername_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,14),_MwPhoneCallToUsername_Type())
mwPhoneCallToUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallToUsername.setStatus(_A)
_MwPhoneCallFromFlowtag_Type=Integer32
_MwPhoneCallFromFlowtag_Object=MibTableColumn
mwPhoneCallFromFlowtag=_MwPhoneCallFromFlowtag_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,15),_MwPhoneCallFromFlowtag_Type())
mwPhoneCallFromFlowtag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromFlowtag.setStatus(_A)
_MwPhoneCallFromPending_Type=MwlOnOffSwitch
_MwPhoneCallFromPending_Object=MibTableColumn
mwPhoneCallFromPending=_MwPhoneCallFromPending_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,16),_MwPhoneCallFromPending_Type())
mwPhoneCallFromPending.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromPending.setStatus(_A)
_MwPhoneCallFromUsername_Type=DisplayString
_MwPhoneCallFromUsername_Object=MibTableColumn
mwPhoneCallFromUsername=_MwPhoneCallFromUsername_Object((1,3,6,1,4,1,15983,1,1,3,3,2,1,17),_MwPhoneCallFromUsername_Type())
mwPhoneCallFromUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:mwPhoneCallFromUsername.setStatus(_A)
_MwVoiceStatusTable_Object=MibTable
mwVoiceStatusTable=_MwVoiceStatusTable_Object((1,3,6,1,4,1,15983,1,1,3,3,3))
if mibBuilder.loadTexts:mwVoiceStatusTable.setStatus(_A)
_MwVoiceStatusEntry_Object=MibTableRow
mwVoiceStatusEntry=_MwVoiceStatusEntry_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1))
mwVoiceStatusEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mwVoiceStatusEntry.setStatus(_A)
_MwVoiceStatusTableIndex_Type=Integer32
_MwVoiceStatusTableIndex_Object=MibTableColumn
mwVoiceStatusTableIndex=_MwVoiceStatusTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,1),_MwVoiceStatusTableIndex_Type())
mwVoiceStatusTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwVoiceStatusTableIndex.setStatus(_A)
_MwVoiceStatusAp_Type=Integer32
_MwVoiceStatusAp_Object=MibTableColumn
mwVoiceStatusAp=_MwVoiceStatusAp_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,2),_MwVoiceStatusAp_Type())
mwVoiceStatusAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusAp.setStatus(_A)
_MwVoiceStatusApName_Type=DisplayString
_MwVoiceStatusApName_Object=MibTableColumn
mwVoiceStatusApName=_MwVoiceStatusApName_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,3),_MwVoiceStatusApName_Type())
mwVoiceStatusApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusApName.setStatus(_A)
_MwVoiceStatusPhoneCount_Type=Unsigned32
_MwVoiceStatusPhoneCount_Object=MibTableColumn
mwVoiceStatusPhoneCount=_MwVoiceStatusPhoneCount_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,4),_MwVoiceStatusPhoneCount_Type())
mwVoiceStatusPhoneCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusPhoneCount.setStatus(_A)
_MwVoiceStatusRejectCount_Type=Counter64
_MwVoiceStatusRejectCount_Object=MibTableColumn
mwVoiceStatusRejectCount=_MwVoiceStatusRejectCount_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,5),_MwVoiceStatusRejectCount_Type())
mwVoiceStatusRejectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusRejectCount.setStatus(_A)
_MwVoiceStatusActiveCallCount_Type=Unsigned32
_MwVoiceStatusActiveCallCount_Object=MibTableColumn
mwVoiceStatusActiveCallCount=_MwVoiceStatusActiveCallCount_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,6),_MwVoiceStatusActiveCallCount_Type())
mwVoiceStatusActiveCallCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusActiveCallCount.setStatus(_A)
_MwVoiceStatusPendingCallCount_Type=Unsigned32
_MwVoiceStatusPendingCallCount_Object=MibTableColumn
mwVoiceStatusPendingCallCount=_MwVoiceStatusPendingCallCount_Object((1,3,6,1,4,1,15983,1,1,3,3,3,1,7),_MwVoiceStatusPendingCallCount_Type())
mwVoiceStatusPendingCallCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVoiceStatusPendingCallCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwVoiceStatistics':mwVoiceStatistics,'mwPhoneTable':mwPhoneTable,'mwPhoneEntry':mwPhoneEntry,_E:mwPhoneTableIndex,'mwPhoneIp':mwPhoneIp,'mwPhoneAp':mwPhoneAp,'mwPhoneMac':mwPhoneMac,'mwPhoneType':mwPhoneType,'mwPhoneApName':mwPhoneApName,'mwPhoneServer':mwPhoneServer,'mwPhoneUsername':mwPhoneUsername,'mwPhoneTransport':mwPhoneTransport,'mwPhoneDeviceType':mwPhoneDeviceType,'mwPhoneCallTable':mwPhoneCallTable,'mwPhoneCallEntry':mwPhoneCallEntry,_F:mwPhoneCallTableIndex,'mwPhoneCallToIp':mwPhoneCallToIp,'mwPhoneCallToAp':mwPhoneCallToAp,'mwPhoneCallType':mwPhoneCallType,'mwPhoneCallToMac':mwPhoneCallToMac,'mwPhoneCallState':mwPhoneCallState,'mwPhoneCallFromIp':mwPhoneCallFromIp,'mwPhoneCallFromAp':mwPhoneCallFromAp,'mwPhoneCallFromMac':mwPhoneCallFromMac,'mwPhoneCallToApName':mwPhoneCallToApName,'mwPhoneCallToFlowtag':mwPhoneCallToFlowtag,'mwPhoneCallToPending':mwPhoneCallToPending,'mwPhoneCallFromApName':mwPhoneCallFromApName,'mwPhoneCallToUsername':mwPhoneCallToUsername,'mwPhoneCallFromFlowtag':mwPhoneCallFromFlowtag,'mwPhoneCallFromPending':mwPhoneCallFromPending,'mwPhoneCallFromUsername':mwPhoneCallFromUsername,'mwVoiceStatusTable':mwVoiceStatusTable,'mwVoiceStatusEntry':mwVoiceStatusEntry,_G:mwVoiceStatusTableIndex,'mwVoiceStatusAp':mwVoiceStatusAp,'mwVoiceStatusApName':mwVoiceStatusApName,'mwVoiceStatusPhoneCount':mwVoiceStatusPhoneCount,'mwVoiceStatusRejectCount':mwVoiceStatusRejectCount,'mwVoiceStatusActiveCallCount':mwVoiceStatusActiveCallCount,'mwVoiceStatusPendingCallCount':mwVoiceStatusPendingCallCount})