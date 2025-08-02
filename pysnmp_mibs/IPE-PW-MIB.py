_M='provPwOverEthPwIndex'
_L='provPwTdmPwIndex'
_K='provPwTdmLineIfIndex'
_J='DisplayString'
_I='OctetString'
_H='IPE-PW-MIB'
_G='invalid'
_F='read-write'
_E='IpeEnableDisableValue'
_D='not-accessible'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention')
class IpeEnableDisableValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('disabled',1),('enabled',2)))
class IpePwIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
class IpeVlanIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_RadioEquipment_ObjectIdentity=ObjectIdentity
radioEquipment=_RadioEquipment_ObjectIdentity((1,3,6,1,4,1,119,2,3,69))
_PasoNeoIpe_common_ObjectIdentity=ObjectIdentity
pasoNeoIpe_common=_PasoNeoIpe_common_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501))
_ProvisioningGroup_ObjectIdentity=ObjectIdentity
provisioningGroup=_ProvisioningGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5))
_ProvPwGroup_ObjectIdentity=ObjectIdentity
provPwGroup=_ProvPwGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5,42))
_ProvPwTdmLineTable_Object=MibTable
provPwTdmLineTable=_ProvPwTdmLineTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4))
if mibBuilder.loadTexts:provPwTdmLineTable.setStatus(_A)
_ProvPwTdmLineEntry_Object=MibTableRow
provPwTdmLineEntry=_ProvPwTdmLineEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1))
provPwTdmLineEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:provPwTdmLineEntry.setStatus(_A)
_ProvPwTdmLineIfIndex_Type=InterfaceIndex
_ProvPwTdmLineIfIndex_Object=MibTableColumn
provPwTdmLineIfIndex=_ProvPwTdmLineIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,1),_ProvPwTdmLineIfIndex_Type())
provPwTdmLineIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwTdmLineIfIndex.setStatus(_A)
_ProvPwTdmLineNEAddress_Type=IpAddress
_ProvPwTdmLineNEAddress_Object=MibTableColumn
provPwTdmLineNEAddress=_ProvPwTdmLineNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,2),_ProvPwTdmLineNEAddress_Type())
provPwTdmLineNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwTdmLineNEAddress.setStatus(_A)
class _ProvPwTdmLineFrameMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('unframed',1)))
_ProvPwTdmLineFrameMode_Type.__name__=_C
_ProvPwTdmLineFrameMode_Object=MibTableColumn
provPwTdmLineFrameMode=_ProvPwTdmLineFrameMode_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,3),_ProvPwTdmLineFrameMode_Type())
provPwTdmLineFrameMode.setMaxAccess(_F)
if mibBuilder.loadTexts:provPwTdmLineFrameMode.setStatus(_A)
class _ProvPwTdmLineCasMode_Type(IpeEnableDisableValue):defaultValue=1
_ProvPwTdmLineCasMode_Type.__name__=_E
_ProvPwTdmLineCasMode_Object=MibTableColumn
provPwTdmLineCasMode=_ProvPwTdmLineCasMode_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,4),_ProvPwTdmLineCasMode_Type())
provPwTdmLineCasMode.setMaxAccess(_F)
if mibBuilder.loadTexts:provPwTdmLineCasMode.setStatus(_A)
class _ProvPwTdmLineCrc4Mode_Type(IpeEnableDisableValue):defaultValue=1
_ProvPwTdmLineCrc4Mode_Type.__name__=_E
_ProvPwTdmLineCrc4Mode_Object=MibTableColumn
provPwTdmLineCrc4Mode=_ProvPwTdmLineCrc4Mode_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,5),_ProvPwTdmLineCrc4Mode_Type())
provPwTdmLineCrc4Mode.setMaxAccess(_F)
if mibBuilder.loadTexts:provPwTdmLineCrc4Mode.setStatus(_A)
class _ProvPwTdmLineJtrBfrDepth_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),('jtr2ms',1),('jtr4ms',2),('jtr8ms',3),('jtr16ms',4),('jtr32ms',5),('jtr64ms',6),('jtr128ms',7)))
_ProvPwTdmLineJtrBfrDepth_Type.__name__=_C
_ProvPwTdmLineJtrBfrDepth_Object=MibTableColumn
provPwTdmLineJtrBfrDepth=_ProvPwTdmLineJtrBfrDepth_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,6),_ProvPwTdmLineJtrBfrDepth_Type())
provPwTdmLineJtrBfrDepth.setMaxAccess(_F)
if mibBuilder.loadTexts:provPwTdmLineJtrBfrDepth.setStatus(_A)
class _ProvPwTdmLineDstMacCheck_Type(IpeEnableDisableValue):defaultValue=2
_ProvPwTdmLineDstMacCheck_Type.__name__=_E
_ProvPwTdmLineDstMacCheck_Object=MibTableColumn
provPwTdmLineDstMacCheck=_ProvPwTdmLineDstMacCheck_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,4,1,7),_ProvPwTdmLineDstMacCheck_Type())
provPwTdmLineDstMacCheck.setMaxAccess(_F)
if mibBuilder.loadTexts:provPwTdmLineDstMacCheck.setStatus(_A)
_ProvPwTdmTable_Object=MibTable
provPwTdmTable=_ProvPwTdmTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5))
if mibBuilder.loadTexts:provPwTdmTable.setStatus(_A)
_ProvPwTdmEntry_Object=MibTableRow
provPwTdmEntry=_ProvPwTdmEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1))
provPwTdmEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:provPwTdmEntry.setStatus(_A)
_ProvPwTdmPwIndex_Type=IpePwIndex
_ProvPwTdmPwIndex_Object=MibTableColumn
provPwTdmPwIndex=_ProvPwTdmPwIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,1),_ProvPwTdmPwIndex_Type())
provPwTdmPwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwTdmPwIndex.setStatus(_A)
_ProvPwTdmNEAddress_Type=IpAddress
_ProvPwTdmNEAddress_Object=MibTableColumn
provPwTdmNEAddress=_ProvPwTdmNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,2),_ProvPwTdmNEAddress_Type())
provPwTdmNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwTdmNEAddress.setStatus(_A)
_ProvPwTdmIfIndex_Type=InterfaceIndex
_ProvPwTdmIfIndex_Object=MibTableColumn
provPwTdmIfIndex=_ProvPwTdmIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,3),_ProvPwTdmIfIndex_Type())
provPwTdmIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmIfIndex.setStatus(_A)
class _ProvPwTdmRtpHdrUsed_Type(IpeEnableDisableValue):defaultValue=1
_ProvPwTdmRtpHdrUsed_Type.__name__=_E
_ProvPwTdmRtpHdrUsed_Object=MibTableColumn
provPwTdmRtpHdrUsed=_ProvPwTdmRtpHdrUsed_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,4),_ProvPwTdmRtpHdrUsed_Type())
provPwTdmRtpHdrUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmRtpHdrUsed.setStatus(_A)
class _ProvPwTdmFrameLength_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ProvPwTdmFrameLength_Type.__name__=_C
_ProvPwTdmFrameLength_Object=MibTableColumn
provPwTdmFrameLength=_ProvPwTdmFrameLength_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,5),_ProvPwTdmFrameLength_Type())
provPwTdmFrameLength.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmFrameLength.setStatus(_A)
class _ProvPwTdmEncapMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('tdmOverEther',1)))
_ProvPwTdmEncapMode_Type.__name__=_C
_ProvPwTdmEncapMode_Object=MibTableColumn
provPwTdmEncapMode=_ProvPwTdmEncapMode_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,6),_ProvPwTdmEncapMode_Type())
provPwTdmEncapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmEncapMode.setStatus(_A)
_ProvPwTdmRowStatus_Type=RowStatus
_ProvPwTdmRowStatus_Object=MibTableColumn
provPwTdmRowStatus=_ProvPwTdmRowStatus_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,7),_ProvPwTdmRowStatus_Type())
provPwTdmRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmRowStatus.setStatus(_A)
class _ProvPwTdmAdaptiveClkSource_Type(IpeEnableDisableValue):defaultValue=1
_ProvPwTdmAdaptiveClkSource_Type.__name__=_E
_ProvPwTdmAdaptiveClkSource_Object=MibTableColumn
provPwTdmAdaptiveClkSource=_ProvPwTdmAdaptiveClkSource_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,5,1,8),_ProvPwTdmAdaptiveClkSource_Type())
provPwTdmAdaptiveClkSource.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwTdmAdaptiveClkSource.setStatus(_A)
_ProvPwOverEthTable_Object=MibTable
provPwOverEthTable=_ProvPwOverEthTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11))
if mibBuilder.loadTexts:provPwOverEthTable.setStatus(_A)
_ProvPwOverEthEntry_Object=MibTableRow
provPwOverEthEntry=_ProvPwOverEthEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1))
provPwOverEthEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:provPwOverEthEntry.setStatus(_A)
_ProvPwOverEthPwIndex_Type=IpePwIndex
_ProvPwOverEthPwIndex_Object=MibTableColumn
provPwOverEthPwIndex=_ProvPwOverEthPwIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,1),_ProvPwOverEthPwIndex_Type())
provPwOverEthPwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwOverEthPwIndex.setStatus(_A)
_ProvPwOverEthNEAddress_Type=IpAddress
_ProvPwOverEthNEAddress_Object=MibTableColumn
provPwOverEthNEAddress=_ProvPwOverEthNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,2),_ProvPwOverEthNEAddress_Type())
provPwOverEthNEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:provPwOverEthNEAddress.setStatus(_A)
_ProvPwOverEthVlanId_Type=IpeVlanIndex
_ProvPwOverEthVlanId_Object=MibTableColumn
provPwOverEthVlanId=_ProvPwOverEthVlanId_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,3),_ProvPwOverEthVlanId_Type())
provPwOverEthVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthVlanId.setStatus(_A)
class _ProvPwOverEthTpid_Type(OctetString):defaultHexValue='ff00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ProvPwOverEthTpid_Type.__name__=_I
_ProvPwOverEthTpid_Object=MibTableColumn
provPwOverEthTpid=_ProvPwOverEthTpid_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,4),_ProvPwOverEthTpid_Type())
provPwOverEthTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthTpid.setStatus('obsolete')
class _ProvPwOverEthCosValue_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ProvPwOverEthCosValue_Type.__name__=_C
_ProvPwOverEthCosValue_Object=MibTableColumn
provPwOverEthCosValue=_ProvPwOverEthCosValue_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,5),_ProvPwOverEthCosValue_Type())
provPwOverEthCosValue.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthCosValue.setStatus(_A)
class _ProvPwOverEthEcid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048575))
_ProvPwOverEthEcid_Type.__name__=_C
_ProvPwOverEthEcid_Object=MibTableColumn
provPwOverEthEcid=_ProvPwOverEthEcid_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,6),_ProvPwOverEthEcid_Type())
provPwOverEthEcid.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthEcid.setStatus(_A)
class _ProvPwOverEthName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProvPwOverEthName_Type.__name__=_J
_ProvPwOverEthName_Object=MibTableColumn
provPwOverEthName=_ProvPwOverEthName_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,7),_ProvPwOverEthName_Type())
provPwOverEthName.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthName.setStatus(_A)
_ProvPwOverEthDstMacAddress_Type=MacAddress
_ProvPwOverEthDstMacAddress_Object=MibTableColumn
provPwOverEthDstMacAddress=_ProvPwOverEthDstMacAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,42,11,1,8),_ProvPwOverEthDstMacAddress_Type())
provPwOverEthDstMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provPwOverEthDstMacAddress.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_E:IpeEnableDisableValue,'IpePwIndex':IpePwIndex,'IpeVlanIndex':IpeVlanIndex,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'pasoNeoIpe-common':pasoNeoIpe_common,'provisioningGroup':provisioningGroup,'provPwGroup':provPwGroup,'provPwTdmLineTable':provPwTdmLineTable,'provPwTdmLineEntry':provPwTdmLineEntry,_K:provPwTdmLineIfIndex,'provPwTdmLineNEAddress':provPwTdmLineNEAddress,'provPwTdmLineFrameMode':provPwTdmLineFrameMode,'provPwTdmLineCasMode':provPwTdmLineCasMode,'provPwTdmLineCrc4Mode':provPwTdmLineCrc4Mode,'provPwTdmLineJtrBfrDepth':provPwTdmLineJtrBfrDepth,'provPwTdmLineDstMacCheck':provPwTdmLineDstMacCheck,'provPwTdmTable':provPwTdmTable,'provPwTdmEntry':provPwTdmEntry,_L:provPwTdmPwIndex,'provPwTdmNEAddress':provPwTdmNEAddress,'provPwTdmIfIndex':provPwTdmIfIndex,'provPwTdmRtpHdrUsed':provPwTdmRtpHdrUsed,'provPwTdmFrameLength':provPwTdmFrameLength,'provPwTdmEncapMode':provPwTdmEncapMode,'provPwTdmRowStatus':provPwTdmRowStatus,'provPwTdmAdaptiveClkSource':provPwTdmAdaptiveClkSource,'provPwOverEthTable':provPwOverEthTable,'provPwOverEthEntry':provPwOverEthEntry,_M:provPwOverEthPwIndex,'provPwOverEthNEAddress':provPwOverEthNEAddress,'provPwOverEthVlanId':provPwOverEthVlanId,'provPwOverEthTpid':provPwOverEthTpid,'provPwOverEthCosValue':provPwOverEthCosValue,'provPwOverEthEcid':provPwOverEthEcid,'provPwOverEthName':provPwOverEthName,'provPwOverEthDstMacAddress':provPwOverEthDstMacAddress})