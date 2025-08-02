_R='dot1adMIPcpEncodingDropEligible'
_Q='dot1adMIPcpEncodingPriority'
_P='dot1adMIPcpEncodingPcpSelRow'
_O='dot1adMIPcpDecodingPcpValue'
_N='dot1adMIPcpDecodingPcpSelRow'
_M='dot1adMIServicePriorityRegenReceivedPriority'
_L='dot1adMICVidRegistrationCVid'
_K='read-create'
_J='dot1adMIVidTranslationLocalVid'
_I='PriorityCodePoint'
_H='dot1adMICVidRegistrationSVid'
_G='TruthValue'
_F='dot1adMIPortNum'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='SUPERMICRO-MIDOT1AD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
EnabledStatus,=mibBuilder.importSymbols('SUPERMICROP-BRIDGE-MIB','EnabledStatus')
dot1adMIMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,133))
if mibBuilder.loadTexts:dot1adMIMIB.setRevisions(('2012-09-05 00:00',))
class PriorityCodePoint(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('codePoint8p0d',1),('codePoint7p1d',2),('codePoint6p2d',3),('codePoint5p3d',4)))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1adMIProviderBridge_ObjectIdentity=ObjectIdentity
dot1adMIProviderBridge=_Dot1adMIProviderBridge_ObjectIdentity((1,3,6,1,4,1,10876,101,1,133,1))
_Dot1adMIPortTable_Object=MibTable
dot1adMIPortTable=_Dot1adMIPortTable_Object((1,3,6,1,4,1,10876,101,1,133,1,1))
if mibBuilder.loadTexts:dot1adMIPortTable.setStatus(_A)
_Dot1adMIPortEntry_Object=MibTableRow
dot1adMIPortEntry=_Dot1adMIPortEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,1,1))
dot1adMIPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dot1adMIPortEntry.setStatus(_A)
class _Dot1adMIPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1adMIPortNum_Type.__name__=_D
_Dot1adMIPortNum_Object=MibTableColumn
dot1adMIPortNum=_Dot1adMIPortNum_Object((1,3,6,1,4,1,10876,101,1,133,1,1,1,1),_Dot1adMIPortNum_Type())
dot1adMIPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPortNum.setStatus(_A)
class _Dot1adMIPortPcpSelectionRow_Type(PriorityCodePoint):defaultValue=1
_Dot1adMIPortPcpSelectionRow_Type.__name__=_I
_Dot1adMIPortPcpSelectionRow_Object=MibTableColumn
dot1adMIPortPcpSelectionRow=_Dot1adMIPortPcpSelectionRow_Object((1,3,6,1,4,1,10876,101,1,133,1,1,1,2),_Dot1adMIPortPcpSelectionRow_Type())
dot1adMIPortPcpSelectionRow.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPortPcpSelectionRow.setStatus(_A)
class _Dot1adMIPortUseDei_Type(TruthValue):defaultValue=2
_Dot1adMIPortUseDei_Type.__name__=_G
_Dot1adMIPortUseDei_Object=MibTableColumn
dot1adMIPortUseDei=_Dot1adMIPortUseDei_Object((1,3,6,1,4,1,10876,101,1,133,1,1,1,3),_Dot1adMIPortUseDei_Type())
dot1adMIPortUseDei.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPortUseDei.setStatus(_A)
class _Dot1adMIPortReqDropEncoding_Type(TruthValue):defaultValue=2
_Dot1adMIPortReqDropEncoding_Type.__name__=_G
_Dot1adMIPortReqDropEncoding_Object=MibTableColumn
dot1adMIPortReqDropEncoding=_Dot1adMIPortReqDropEncoding_Object((1,3,6,1,4,1,10876,101,1,133,1,1,1,4),_Dot1adMIPortReqDropEncoding_Type())
dot1adMIPortReqDropEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPortReqDropEncoding.setStatus(_A)
_Dot1adMIVidTranslationTable_Object=MibTable
dot1adMIVidTranslationTable=_Dot1adMIVidTranslationTable_Object((1,3,6,1,4,1,10876,101,1,133,1,2))
if mibBuilder.loadTexts:dot1adMIVidTranslationTable.setStatus(_A)
_Dot1adMIVidTranslationEntry_Object=MibTableRow
dot1adMIVidTranslationEntry=_Dot1adMIVidTranslationEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,2,1))
dot1adMIVidTranslationEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:dot1adMIVidTranslationEntry.setStatus(_A)
_Dot1adMIVidTranslationLocalVid_Type=VlanId
_Dot1adMIVidTranslationLocalVid_Object=MibTableColumn
dot1adMIVidTranslationLocalVid=_Dot1adMIVidTranslationLocalVid_Object((1,3,6,1,4,1,10876,101,1,133,1,2,1,1),_Dot1adMIVidTranslationLocalVid_Type())
dot1adMIVidTranslationLocalVid.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIVidTranslationLocalVid.setStatus(_A)
_Dot1adMIVidTranslationRelayVid_Type=VlanId
_Dot1adMIVidTranslationRelayVid_Object=MibTableColumn
dot1adMIVidTranslationRelayVid=_Dot1adMIVidTranslationRelayVid_Object((1,3,6,1,4,1,10876,101,1,133,1,2,1,2),_Dot1adMIVidTranslationRelayVid_Type())
dot1adMIVidTranslationRelayVid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIVidTranslationRelayVid.setStatus(_A)
_Dot1adMIVidTranslationRowStatus_Type=RowStatus
_Dot1adMIVidTranslationRowStatus_Object=MibTableColumn
dot1adMIVidTranslationRowStatus=_Dot1adMIVidTranslationRowStatus_Object((1,3,6,1,4,1,10876,101,1,133,1,2,1,3),_Dot1adMIVidTranslationRowStatus_Type())
dot1adMIVidTranslationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dot1adMIVidTranslationRowStatus.setStatus(_A)
_Dot1adMICVidRegistrationTable_Object=MibTable
dot1adMICVidRegistrationTable=_Dot1adMICVidRegistrationTable_Object((1,3,6,1,4,1,10876,101,1,133,1,3))
if mibBuilder.loadTexts:dot1adMICVidRegistrationTable.setStatus(_A)
_Dot1adMICVidRegistrationEntry_Object=MibTableRow
dot1adMICVidRegistrationEntry=_Dot1adMICVidRegistrationEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1))
dot1adMICVidRegistrationEntry.setIndexNames((0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:dot1adMICVidRegistrationEntry.setStatus(_A)
_Dot1adMICVidRegistrationCVid_Type=VlanId
_Dot1adMICVidRegistrationCVid_Object=MibTableColumn
dot1adMICVidRegistrationCVid=_Dot1adMICVidRegistrationCVid_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1,1),_Dot1adMICVidRegistrationCVid_Type())
dot1adMICVidRegistrationCVid.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMICVidRegistrationCVid.setStatus(_A)
_Dot1adMICVidRegistrationSVid_Type=VlanId
_Dot1adMICVidRegistrationSVid_Object=MibTableColumn
dot1adMICVidRegistrationSVid=_Dot1adMICVidRegistrationSVid_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1,2),_Dot1adMICVidRegistrationSVid_Type())
dot1adMICVidRegistrationSVid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMICVidRegistrationSVid.setStatus(_A)
class _Dot1adMICVidRegistrationUntaggedPep_Type(TruthValue):defaultValue=2
_Dot1adMICVidRegistrationUntaggedPep_Type.__name__=_G
_Dot1adMICVidRegistrationUntaggedPep_Object=MibTableColumn
dot1adMICVidRegistrationUntaggedPep=_Dot1adMICVidRegistrationUntaggedPep_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1,3),_Dot1adMICVidRegistrationUntaggedPep_Type())
dot1adMICVidRegistrationUntaggedPep.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMICVidRegistrationUntaggedPep.setStatus(_A)
class _Dot1adMICVidRegistrationUntaggedCep_Type(TruthValue):defaultValue=2
_Dot1adMICVidRegistrationUntaggedCep_Type.__name__=_G
_Dot1adMICVidRegistrationUntaggedCep_Object=MibTableColumn
dot1adMICVidRegistrationUntaggedCep=_Dot1adMICVidRegistrationUntaggedCep_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1,4),_Dot1adMICVidRegistrationUntaggedCep_Type())
dot1adMICVidRegistrationUntaggedCep.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMICVidRegistrationUntaggedCep.setStatus(_A)
_Dot1adMICVidRegistrationRowStatus_Type=RowStatus
_Dot1adMICVidRegistrationRowStatus_Object=MibTableColumn
dot1adMICVidRegistrationRowStatus=_Dot1adMICVidRegistrationRowStatus_Object((1,3,6,1,4,1,10876,101,1,133,1,3,1,5),_Dot1adMICVidRegistrationRowStatus_Type())
dot1adMICVidRegistrationRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dot1adMICVidRegistrationRowStatus.setStatus(_A)
_Dot1adMIPepTable_Object=MibTable
dot1adMIPepTable=_Dot1adMIPepTable_Object((1,3,6,1,4,1,10876,101,1,133,1,4))
if mibBuilder.loadTexts:dot1adMIPepTable.setStatus(_A)
_Dot1adMIPepEntry_Object=MibTableRow
dot1adMIPepEntry=_Dot1adMIPepEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,4,1))
dot1adMIPepEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:dot1adMIPepEntry.setStatus(_A)
_Dot1adMIPepPvid_Type=VlanId
_Dot1adMIPepPvid_Object=MibTableColumn
dot1adMIPepPvid=_Dot1adMIPepPvid_Object((1,3,6,1,4,1,10876,101,1,133,1,4,1,1),_Dot1adMIPepPvid_Type())
dot1adMIPepPvid.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPepPvid.setStatus(_A)
class _Dot1adMIPepDefaultUserPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIPepDefaultUserPriority_Type.__name__=_D
_Dot1adMIPepDefaultUserPriority_Object=MibTableColumn
dot1adMIPepDefaultUserPriority=_Dot1adMIPepDefaultUserPriority_Object((1,3,6,1,4,1,10876,101,1,133,1,4,1,2),_Dot1adMIPepDefaultUserPriority_Type())
dot1adMIPepDefaultUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPepDefaultUserPriority.setStatus(_A)
class _Dot1adMIPepAccptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2),('admitOnlyUntaggedAndPriorityTagged',3)))
_Dot1adMIPepAccptableFrameTypes_Type.__name__=_D
_Dot1adMIPepAccptableFrameTypes_Object=MibTableColumn
dot1adMIPepAccptableFrameTypes=_Dot1adMIPepAccptableFrameTypes_Object((1,3,6,1,4,1,10876,101,1,133,1,4,1,3),_Dot1adMIPepAccptableFrameTypes_Type())
dot1adMIPepAccptableFrameTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPepAccptableFrameTypes.setStatus(_A)
class _Dot1adMIPepIngressFiltering_Type(TruthValue):defaultValue=2
_Dot1adMIPepIngressFiltering_Type.__name__=_G
_Dot1adMIPepIngressFiltering_Object=MibTableColumn
dot1adMIPepIngressFiltering=_Dot1adMIPepIngressFiltering_Object((1,3,6,1,4,1,10876,101,1,133,1,4,1,4),_Dot1adMIPepIngressFiltering_Type())
dot1adMIPepIngressFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPepIngressFiltering.setStatus(_A)
_Dot1adMIServicePriorityRegenerationTable_Object=MibTable
dot1adMIServicePriorityRegenerationTable=_Dot1adMIServicePriorityRegenerationTable_Object((1,3,6,1,4,1,10876,101,1,133,1,5))
if mibBuilder.loadTexts:dot1adMIServicePriorityRegenerationTable.setStatus(_A)
_Dot1adMIServicePriorityRegenerationEntry_Object=MibTableRow
dot1adMIServicePriorityRegenerationEntry=_Dot1adMIServicePriorityRegenerationEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,5,1))
dot1adMIServicePriorityRegenerationEntry.setIndexNames((0,_B,_F),(0,_B,_H),(0,_B,_M))
if mibBuilder.loadTexts:dot1adMIServicePriorityRegenerationEntry.setStatus(_A)
class _Dot1adMIServicePriorityRegenReceivedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIServicePriorityRegenReceivedPriority_Type.__name__=_D
_Dot1adMIServicePriorityRegenReceivedPriority_Object=MibTableColumn
dot1adMIServicePriorityRegenReceivedPriority=_Dot1adMIServicePriorityRegenReceivedPriority_Object((1,3,6,1,4,1,10876,101,1,133,1,5,1,1),_Dot1adMIServicePriorityRegenReceivedPriority_Type())
dot1adMIServicePriorityRegenReceivedPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIServicePriorityRegenReceivedPriority.setStatus(_A)
class _Dot1adMIServicePriorityRegenRegeneratedPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIServicePriorityRegenRegeneratedPriority_Type.__name__=_D
_Dot1adMIServicePriorityRegenRegeneratedPriority_Object=MibTableColumn
dot1adMIServicePriorityRegenRegeneratedPriority=_Dot1adMIServicePriorityRegenRegeneratedPriority_Object((1,3,6,1,4,1,10876,101,1,133,1,5,1,2),_Dot1adMIServicePriorityRegenRegeneratedPriority_Type())
dot1adMIServicePriorityRegenRegeneratedPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIServicePriorityRegenRegeneratedPriority.setStatus(_A)
_Dot1adMIPcpDecodingTable_Object=MibTable
dot1adMIPcpDecodingTable=_Dot1adMIPcpDecodingTable_Object((1,3,6,1,4,1,10876,101,1,133,1,6))
if mibBuilder.loadTexts:dot1adMIPcpDecodingTable.setStatus(_A)
_Dot1adMIPcpDecodingEntry_Object=MibTableRow
dot1adMIPcpDecodingEntry=_Dot1adMIPcpDecodingEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,6,1))
dot1adMIPcpDecodingEntry.setIndexNames((0,_B,_F),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:dot1adMIPcpDecodingEntry.setStatus(_A)
_Dot1adMIPcpDecodingPcpSelRow_Type=PriorityCodePoint
_Dot1adMIPcpDecodingPcpSelRow_Object=MibTableColumn
dot1adMIPcpDecodingPcpSelRow=_Dot1adMIPcpDecodingPcpSelRow_Object((1,3,6,1,4,1,10876,101,1,133,1,6,1,1),_Dot1adMIPcpDecodingPcpSelRow_Type())
dot1adMIPcpDecodingPcpSelRow.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPcpDecodingPcpSelRow.setStatus(_A)
class _Dot1adMIPcpDecodingPcpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIPcpDecodingPcpValue_Type.__name__=_D
_Dot1adMIPcpDecodingPcpValue_Object=MibTableColumn
dot1adMIPcpDecodingPcpValue=_Dot1adMIPcpDecodingPcpValue_Object((1,3,6,1,4,1,10876,101,1,133,1,6,1,2),_Dot1adMIPcpDecodingPcpValue_Type())
dot1adMIPcpDecodingPcpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPcpDecodingPcpValue.setStatus(_A)
class _Dot1adMIPcpDecodingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIPcpDecodingPriority_Type.__name__=_D
_Dot1adMIPcpDecodingPriority_Object=MibTableColumn
dot1adMIPcpDecodingPriority=_Dot1adMIPcpDecodingPriority_Object((1,3,6,1,4,1,10876,101,1,133,1,6,1,3),_Dot1adMIPcpDecodingPriority_Type())
dot1adMIPcpDecodingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPcpDecodingPriority.setStatus(_A)
_Dot1adMIPcpDecodingDropEligible_Type=TruthValue
_Dot1adMIPcpDecodingDropEligible_Object=MibTableColumn
dot1adMIPcpDecodingDropEligible=_Dot1adMIPcpDecodingDropEligible_Object((1,3,6,1,4,1,10876,101,1,133,1,6,1,4),_Dot1adMIPcpDecodingDropEligible_Type())
dot1adMIPcpDecodingDropEligible.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPcpDecodingDropEligible.setStatus(_A)
_Dot1adMIPcpEncodingTable_Object=MibTable
dot1adMIPcpEncodingTable=_Dot1adMIPcpEncodingTable_Object((1,3,6,1,4,1,10876,101,1,133,1,7))
if mibBuilder.loadTexts:dot1adMIPcpEncodingTable.setStatus(_A)
_Dot1adMIPcpEncodingEntry_Object=MibTableRow
dot1adMIPcpEncodingEntry=_Dot1adMIPcpEncodingEntry_Object((1,3,6,1,4,1,10876,101,1,133,1,7,1))
dot1adMIPcpEncodingEntry.setIndexNames((0,_B,_F),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:dot1adMIPcpEncodingEntry.setStatus(_A)
_Dot1adMIPcpEncodingPcpSelRow_Type=PriorityCodePoint
_Dot1adMIPcpEncodingPcpSelRow_Object=MibTableColumn
dot1adMIPcpEncodingPcpSelRow=_Dot1adMIPcpEncodingPcpSelRow_Object((1,3,6,1,4,1,10876,101,1,133,1,7,1,1),_Dot1adMIPcpEncodingPcpSelRow_Type())
dot1adMIPcpEncodingPcpSelRow.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPcpEncodingPcpSelRow.setStatus(_A)
class _Dot1adMIPcpEncodingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIPcpEncodingPriority_Type.__name__=_D
_Dot1adMIPcpEncodingPriority_Object=MibTableColumn
dot1adMIPcpEncodingPriority=_Dot1adMIPcpEncodingPriority_Object((1,3,6,1,4,1,10876,101,1,133,1,7,1,2),_Dot1adMIPcpEncodingPriority_Type())
dot1adMIPcpEncodingPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPcpEncodingPriority.setStatus(_A)
_Dot1adMIPcpEncodingDropEligible_Type=TruthValue
_Dot1adMIPcpEncodingDropEligible_Object=MibTableColumn
dot1adMIPcpEncodingDropEligible=_Dot1adMIPcpEncodingDropEligible_Object((1,3,6,1,4,1,10876,101,1,133,1,7,1,3),_Dot1adMIPcpEncodingDropEligible_Type())
dot1adMIPcpEncodingDropEligible.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1adMIPcpEncodingDropEligible.setStatus(_A)
class _Dot1adMIPcpEncodingPcpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1adMIPcpEncodingPcpValue_Type.__name__=_D
_Dot1adMIPcpEncodingPcpValue_Object=MibTableColumn
dot1adMIPcpEncodingPcpValue=_Dot1adMIPcpEncodingPcpValue_Object((1,3,6,1,4,1,10876,101,1,133,1,7,1,4),_Dot1adMIPcpEncodingPcpValue_Type())
dot1adMIPcpEncodingPcpValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1adMIPcpEncodingPcpValue.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_I:PriorityCodePoint,'VlanId':VlanId,'dot1adMIMIB':dot1adMIMIB,'dot1adMIProviderBridge':dot1adMIProviderBridge,'dot1adMIPortTable':dot1adMIPortTable,'dot1adMIPortEntry':dot1adMIPortEntry,_F:dot1adMIPortNum,'dot1adMIPortPcpSelectionRow':dot1adMIPortPcpSelectionRow,'dot1adMIPortUseDei':dot1adMIPortUseDei,'dot1adMIPortReqDropEncoding':dot1adMIPortReqDropEncoding,'dot1adMIVidTranslationTable':dot1adMIVidTranslationTable,'dot1adMIVidTranslationEntry':dot1adMIVidTranslationEntry,_J:dot1adMIVidTranslationLocalVid,'dot1adMIVidTranslationRelayVid':dot1adMIVidTranslationRelayVid,'dot1adMIVidTranslationRowStatus':dot1adMIVidTranslationRowStatus,'dot1adMICVidRegistrationTable':dot1adMICVidRegistrationTable,'dot1adMICVidRegistrationEntry':dot1adMICVidRegistrationEntry,_L:dot1adMICVidRegistrationCVid,_H:dot1adMICVidRegistrationSVid,'dot1adMICVidRegistrationUntaggedPep':dot1adMICVidRegistrationUntaggedPep,'dot1adMICVidRegistrationUntaggedCep':dot1adMICVidRegistrationUntaggedCep,'dot1adMICVidRegistrationRowStatus':dot1adMICVidRegistrationRowStatus,'dot1adMIPepTable':dot1adMIPepTable,'dot1adMIPepEntry':dot1adMIPepEntry,'dot1adMIPepPvid':dot1adMIPepPvid,'dot1adMIPepDefaultUserPriority':dot1adMIPepDefaultUserPriority,'dot1adMIPepAccptableFrameTypes':dot1adMIPepAccptableFrameTypes,'dot1adMIPepIngressFiltering':dot1adMIPepIngressFiltering,'dot1adMIServicePriorityRegenerationTable':dot1adMIServicePriorityRegenerationTable,'dot1adMIServicePriorityRegenerationEntry':dot1adMIServicePriorityRegenerationEntry,_M:dot1adMIServicePriorityRegenReceivedPriority,'dot1adMIServicePriorityRegenRegeneratedPriority':dot1adMIServicePriorityRegenRegeneratedPriority,'dot1adMIPcpDecodingTable':dot1adMIPcpDecodingTable,'dot1adMIPcpDecodingEntry':dot1adMIPcpDecodingEntry,_N:dot1adMIPcpDecodingPcpSelRow,_O:dot1adMIPcpDecodingPcpValue,'dot1adMIPcpDecodingPriority':dot1adMIPcpDecodingPriority,'dot1adMIPcpDecodingDropEligible':dot1adMIPcpDecodingDropEligible,'dot1adMIPcpEncodingTable':dot1adMIPcpEncodingTable,'dot1adMIPcpEncodingEntry':dot1adMIPcpEncodingEntry,_P:dot1adMIPcpEncodingPcpSelRow,_Q:dot1adMIPcpEncodingPriority,_R:dot1adMIPcpEncodingDropEligible,'dot1adMIPcpEncodingPcpValue':dot1adMIPcpEncodingPcpValue})