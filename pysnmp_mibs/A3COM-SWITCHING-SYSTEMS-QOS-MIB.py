_k='a3ComQosFlowClassDestAddr'
_j='a3ComQosFlowClassSrcAddr'
_i='a3ComQosFlowClassIpProtoType'
_h='a3ComQosXmtHmStatsQindex'
_g='reserved'
_f='a3ComQosXmtStatsQindex'
_e='a3ComQosCtrlRateLimitIndex'
_d='a3ComQosCtrlRateLimitCtrlIndex'
_c='ieee8021pTag7'
_b='ieee8021pTag6'
_a='ieee8021pTag5'
_Z='ieee8021pTag4'
_Y='ieee8021pTag3'
_X='ieee8021pTag2'
_W='ieee8021pTag1'
_V='ieee8021pTag0'
_U='nonEligible'
_T='eligible'
_S='a3ComQosCtrlIndex'
_R='a3ComQosNonFlowClassIndex'
_Q='a3ComQosFlowClassFilterIndex'
_P='a3ComQosGenClassIndex'
_O='NotificationType'
_N='none'
_M='a3ComQosFlowClassIndex'
_L='DisplayString'
_K='highPriority'
_J='ifIndex'
_I='IF-MIB'
_H='lowPriority'
_G='bestEffort'
_F='OctetString'
_E='A3COM-SWITCHING-SYSTEMS-QOS-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComQos_ObjectIdentity=ObjectIdentity
a3ComQos=_A3ComQos_ObjectIdentity((1,3,6,1,4,1,43,29,4,21))
_A3ComQosClass_ObjectIdentity=ObjectIdentity
a3ComQosClass=_A3ComQosClass_ObjectIdentity((1,3,6,1,4,1,43,29,4,21,1))
_A3ComQosGenClassTable_Object=MibTable
a3ComQosGenClassTable=_A3ComQosGenClassTable_Object((1,3,6,1,4,1,43,29,4,21,1,1))
if mibBuilder.loadTexts:a3ComQosGenClassTable.setStatus(_A)
_A3ComQosGenClassEntry_Object=MibTableRow
a3ComQosGenClassEntry=_A3ComQosGenClassEntry_Object((1,3,6,1,4,1,43,29,4,21,1,1,1))
a3ComQosGenClassEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:a3ComQosGenClassEntry.setStatus(_A)
class _A3ComQosGenClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65532))
_A3ComQosGenClassIndex_Type.__name__=_C
_A3ComQosGenClassIndex_Object=MibTableColumn
a3ComQosGenClassIndex=_A3ComQosGenClassIndex_Object((1,3,6,1,4,1,43,29,4,21,1,1,1,1),_A3ComQosGenClassIndex_Type())
a3ComQosGenClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosGenClassIndex.setStatus(_A)
class _A3ComQosGenClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A3ComQosGenClassName_Type.__name__=_L
_A3ComQosGenClassName_Object=MibTableColumn
a3ComQosGenClassName=_A3ComQosGenClassName_Object((1,3,6,1,4,1,43,29,4,21,1,1,1,2),_A3ComQosGenClassName_Type())
a3ComQosGenClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosGenClassName.setStatus(_A)
_A3ComQosGenClassControlId_Type=Integer32
_A3ComQosGenClassControlId_Object=MibTableColumn
a3ComQosGenClassControlId=_A3ComQosGenClassControlId_Object((1,3,6,1,4,1,43,29,4,21,1,1,1,3),_A3ComQosGenClassControlId_Type())
a3ComQosGenClassControlId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosGenClassControlId.setStatus(_A)
_A3ComQosFlowClassTable_Object=MibTable
a3ComQosFlowClassTable=_A3ComQosFlowClassTable_Object((1,3,6,1,4,1,43,29,4,21,1,2))
if mibBuilder.loadTexts:a3ComQosFlowClassTable.setStatus(_A)
_A3ComQosFlowClassEntry_Object=MibTableRow
a3ComQosFlowClassEntry=_A3ComQosFlowClassEntry_Object((1,3,6,1,4,1,43,29,4,21,1,2,1))
a3ComQosFlowClassEntry.setIndexNames((0,_E,_M),(0,_E,_Q))
if mibBuilder.loadTexts:a3ComQosFlowClassEntry.setStatus(_A)
class _A3ComQosFlowClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65532))
_A3ComQosFlowClassIndex_Type.__name__=_C
_A3ComQosFlowClassIndex_Object=MibTableColumn
a3ComQosFlowClassIndex=_A3ComQosFlowClassIndex_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,1),_A3ComQosFlowClassIndex_Type())
a3ComQosFlowClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosFlowClassIndex.setStatus(_A)
class _A3ComQosFlowClassFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_A3ComQosFlowClassFilterIndex_Type.__name__=_C
_A3ComQosFlowClassFilterIndex_Object=MibTableColumn
a3ComQosFlowClassFilterIndex=_A3ComQosFlowClassFilterIndex_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,2),_A3ComQosFlowClassFilterIndex_Type())
a3ComQosFlowClassFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosFlowClassFilterIndex.setStatus(_A)
class _A3ComQosFlowClassCastType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('both',3)))
_A3ComQosFlowClassCastType_Type.__name__=_C
_A3ComQosFlowClassCastType_Object=MibTableColumn
a3ComQosFlowClassCastType=_A3ComQosFlowClassCastType_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,3),_A3ComQosFlowClassCastType_Type())
a3ComQosFlowClassCastType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassCastType.setStatus(_A)
class _A3ComQosFlowClassIpProtoType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcp',2),('both',3)))
_A3ComQosFlowClassIpProtoType_Type.__name__=_C
_A3ComQosFlowClassIpProtoType_Object=MibTableColumn
a3ComQosFlowClassIpProtoType=_A3ComQosFlowClassIpProtoType_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,4),_A3ComQosFlowClassIpProtoType_Type())
a3ComQosFlowClassIpProtoType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassIpProtoType.setStatus(_A)
_A3ComQosFlowClassSrcAddr_Type=IpAddress
_A3ComQosFlowClassSrcAddr_Object=MibTableColumn
a3ComQosFlowClassSrcAddr=_A3ComQosFlowClassSrcAddr_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,5),_A3ComQosFlowClassSrcAddr_Type())
a3ComQosFlowClassSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassSrcAddr.setStatus(_A)
_A3ComQosFlowClassSrcSubnetMask_Type=IpAddress
_A3ComQosFlowClassSrcSubnetMask_Object=MibTableColumn
a3ComQosFlowClassSrcSubnetMask=_A3ComQosFlowClassSrcSubnetMask_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,6),_A3ComQosFlowClassSrcSubnetMask_Type())
a3ComQosFlowClassSrcSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassSrcSubnetMask.setStatus(_A)
_A3ComQosFlowClassDestAddr_Type=IpAddress
_A3ComQosFlowClassDestAddr_Object=MibTableColumn
a3ComQosFlowClassDestAddr=_A3ComQosFlowClassDestAddr_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,7),_A3ComQosFlowClassDestAddr_Type())
a3ComQosFlowClassDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassDestAddr.setStatus(_A)
_A3ComQosFlowClassDestSubnetMask_Type=IpAddress
_A3ComQosFlowClassDestSubnetMask_Object=MibTableColumn
a3ComQosFlowClassDestSubnetMask=_A3ComQosFlowClassDestSubnetMask_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,8),_A3ComQosFlowClassDestSubnetMask_Type())
a3ComQosFlowClassDestSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassDestSubnetMask.setStatus(_A)
class _A3ComQosFlowClassPortStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComQosFlowClassPortStart_Type.__name__=_C
_A3ComQosFlowClassPortStart_Object=MibTableColumn
a3ComQosFlowClassPortStart=_A3ComQosFlowClassPortStart_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,9),_A3ComQosFlowClassPortStart_Type())
a3ComQosFlowClassPortStart.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassPortStart.setStatus(_A)
class _A3ComQosFlowClassPortEnd_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_A3ComQosFlowClassPortEnd_Type.__name__=_C
_A3ComQosFlowClassPortEnd_Object=MibTableColumn
a3ComQosFlowClassPortEnd=_A3ComQosFlowClassPortEnd_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,10),_A3ComQosFlowClassPortEnd_Type())
a3ComQosFlowClassPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassPortEnd.setStatus(_A)
_A3ComQosFlowClassRowStatus_Type=RowStatus
_A3ComQosFlowClassRowStatus_Object=MibTableColumn
a3ComQosFlowClassRowStatus=_A3ComQosFlowClassRowStatus_Object((1,3,6,1,4,1,43,29,4,21,1,2,1,11),_A3ComQosFlowClassRowStatus_Type())
a3ComQosFlowClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosFlowClassRowStatus.setStatus(_A)
_A3ComQosNonFlowClassTable_Object=MibTable
a3ComQosNonFlowClassTable=_A3ComQosNonFlowClassTable_Object((1,3,6,1,4,1,43,29,4,21,1,3))
if mibBuilder.loadTexts:a3ComQosNonFlowClassTable.setStatus(_A)
_A3ComQosNonFlowClassEntry_Object=MibTableRow
a3ComQosNonFlowClassEntry=_A3ComQosNonFlowClassEntry_Object((1,3,6,1,4,1,43,29,4,21,1,3,1))
a3ComQosNonFlowClassEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:a3ComQosNonFlowClassEntry.setStatus(_A)
class _A3ComQosNonFlowClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65532))
_A3ComQosNonFlowClassIndex_Type.__name__=_C
_A3ComQosNonFlowClassIndex_Object=MibTableColumn
a3ComQosNonFlowClassIndex=_A3ComQosNonFlowClassIndex_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,1),_A3ComQosNonFlowClassIndex_Type())
a3ComQosNonFlowClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosNonFlowClassIndex.setStatus(_A)
class _A3ComQosNonFlowClassCastType_Type(OctetString):defaultHexValue='07';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_A3ComQosNonFlowClassCastType_Type.__name__=_F
_A3ComQosNonFlowClassCastType_Object=MibTableColumn
a3ComQosNonFlowClassCastType=_A3ComQosNonFlowClassCastType_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,2),_A3ComQosNonFlowClassCastType_Type())
a3ComQosNonFlowClassCastType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClassCastType.setStatus(_A)
class _A3ComQosNonFlowClassProtos_Type(OctetString):defaultHexValue='0f';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_A3ComQosNonFlowClassProtos_Type.__name__=_F
_A3ComQosNonFlowClassProtos_Object=MibTableColumn
a3ComQosNonFlowClassProtos=_A3ComQosNonFlowClassProtos_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,3),_A3ComQosNonFlowClassProtos_Type())
a3ComQosNonFlowClassProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClassProtos.setStatus(_A)
class _A3ComQosNonFlowClass8021pTags_Type(OctetString):defaultHexValue='ff';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_A3ComQosNonFlowClass8021pTags_Type.__name__=_F
_A3ComQosNonFlowClass8021pTags_Object=MibTableColumn
a3ComQosNonFlowClass8021pTags=_A3ComQosNonFlowClass8021pTags_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,4),_A3ComQosNonFlowClass8021pTags_Type())
a3ComQosNonFlowClass8021pTags.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClass8021pTags.setStatus(_A)
_A3ComQosNonFlowClassRowStatus_Type=RowStatus
_A3ComQosNonFlowClassRowStatus_Object=MibTableColumn
a3ComQosNonFlowClassRowStatus=_A3ComQosNonFlowClassRowStatus_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,5),_A3ComQosNonFlowClassRowStatus_Type())
a3ComQosNonFlowClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClassRowStatus.setStatus(_A)
class _A3ComQosNonFlowClassProtoDescriptor_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('name',1),('ethertype',2),('dsap-ssap',3)))
_A3ComQosNonFlowClassProtoDescriptor_Type.__name__=_C
_A3ComQosNonFlowClassProtoDescriptor_Object=MibTableColumn
a3ComQosNonFlowClassProtoDescriptor=_A3ComQosNonFlowClassProtoDescriptor_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,6),_A3ComQosNonFlowClassProtoDescriptor_Type())
a3ComQosNonFlowClassProtoDescriptor.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClassProtoDescriptor.setStatus(_A)
class _A3ComQosNonFlowClassCustomProto_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_A3ComQosNonFlowClassCustomProto_Type.__name__=_F
_A3ComQosNonFlowClassCustomProto_Object=MibTableColumn
a3ComQosNonFlowClassCustomProto=_A3ComQosNonFlowClassCustomProto_Object((1,3,6,1,4,1,43,29,4,21,1,3,1,7),_A3ComQosNonFlowClassCustomProto_Type())
a3ComQosNonFlowClassCustomProto.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosNonFlowClassCustomProto.setStatus(_A)
_A3ComQosCtrl_ObjectIdentity=ObjectIdentity
a3ComQosCtrl=_A3ComQosCtrl_ObjectIdentity((1,3,6,1,4,1,43,29,4,21,2))
_A3ComQosCtrlTable_Object=MibTable
a3ComQosCtrlTable=_A3ComQosCtrlTable_Object((1,3,6,1,4,1,43,29,4,21,2,1))
if mibBuilder.loadTexts:a3ComQosCtrlTable.setStatus(_A)
_A3ComQosCtrlEntry_Object=MibTableRow
a3ComQosCtrlEntry=_A3ComQosCtrlEntry_Object((1,3,6,1,4,1,43,29,4,21,2,1,1))
a3ComQosCtrlEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:a3ComQosCtrlEntry.setStatus(_A)
class _A3ComQosCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65532))
_A3ComQosCtrlIndex_Type.__name__=_C
_A3ComQosCtrlIndex_Object=MibTableColumn
a3ComQosCtrlIndex=_A3ComQosCtrlIndex_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,1),_A3ComQosCtrlIndex_Type())
a3ComQosCtrlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosCtrlIndex.setStatus(_A)
class _A3ComQosCtrlName_Type(DisplayString):defaultHexValue='00';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_A3ComQosCtrlName_Type.__name__=_L
_A3ComQosCtrlName_Object=MibTableColumn
a3ComQosCtrlName=_A3ComQosCtrlName_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,2),_A3ComQosCtrlName_Type())
a3ComQosCtrlName.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlName.setStatus(_A)
class _A3ComQosCtrlServiceLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_G,2),(_H,3),('drop',4)))
_A3ComQosCtrlServiceLevel_Type.__name__=_C
_A3ComQosCtrlServiceLevel_Object=MibTableColumn
a3ComQosCtrlServiceLevel=_A3ComQosCtrlServiceLevel_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,3),_A3ComQosCtrlServiceLevel_Type())
a3ComQosCtrlServiceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlServiceLevel.setStatus(_A)
class _A3ComQosCtrlConformPktsLossEligible_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_A3ComQosCtrlConformPktsLossEligible_Type.__name__=_C
_A3ComQosCtrlConformPktsLossEligible_Object=MibTableColumn
a3ComQosCtrlConformPktsLossEligible=_A3ComQosCtrlConformPktsLossEligible_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,4),_A3ComQosCtrlConformPktsLossEligible_Type())
a3ComQosCtrlConformPktsLossEligible.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlConformPktsLossEligible.setStatus(_A)
class _A3ComQosCtrlExcessPktsServiceLevel_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_G,2),(_H,3),('drop',4)))
_A3ComQosCtrlExcessPktsServiceLevel_Type.__name__=_C
_A3ComQosCtrlExcessPktsServiceLevel_Object=MibTableColumn
a3ComQosCtrlExcessPktsServiceLevel=_A3ComQosCtrlExcessPktsServiceLevel_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,5),_A3ComQosCtrlExcessPktsServiceLevel_Type())
a3ComQosCtrlExcessPktsServiceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlExcessPktsServiceLevel.setStatus(_A)
class _A3ComQosCtrlExcessPktsLossEligible_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_A3ComQosCtrlExcessPktsLossEligible_Type.__name__=_C
_A3ComQosCtrlExcessPktsLossEligible_Object=MibTableColumn
a3ComQosCtrlExcessPktsLossEligible=_A3ComQosCtrlExcessPktsLossEligible_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,6),_A3ComQosCtrlExcessPktsLossEligible_Type())
a3ComQosCtrlExcessPktsLossEligible.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlExcessPktsLossEligible.setStatus(_A)
class _A3ComQosCtrl8021pTag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9)))
_A3ComQosCtrl8021pTag_Type.__name__=_C
_A3ComQosCtrl8021pTag_Object=MibTableColumn
a3ComQosCtrl8021pTag=_A3ComQosCtrl8021pTag_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,7),_A3ComQosCtrl8021pTag_Type())
a3ComQosCtrl8021pTag.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrl8021pTag.setStatus(_A)
class _A3ComQosCtrlRateLimitType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('receivePort',2),('aggregate',3)))
_A3ComQosCtrlRateLimitType_Type.__name__=_C
_A3ComQosCtrlRateLimitType_Object=MibTableColumn
a3ComQosCtrlRateLimitType=_A3ComQosCtrlRateLimitType_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,8),_A3ComQosCtrlRateLimitType_Type())
a3ComQosCtrlRateLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitType.setStatus(_A)
_A3ComQosCtrlRowStatus_Type=RowStatus
_A3ComQosCtrlRowStatus_Object=MibTableColumn
a3ComQosCtrlRowStatus=_A3ComQosCtrlRowStatus_Object((1,3,6,1,4,1,43,29,4,21,2,1,1,9),_A3ComQosCtrlRowStatus_Type())
a3ComQosCtrlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRowStatus.setStatus(_A)
_A3ComQosCtrlRateLimitTable_Object=MibTable
a3ComQosCtrlRateLimitTable=_A3ComQosCtrlRateLimitTable_Object((1,3,6,1,4,1,43,29,4,21,2,2))
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitTable.setStatus(_A)
_A3ComQosCtrlRateLimitEntry_Object=MibTableRow
a3ComQosCtrlRateLimitEntry=_A3ComQosCtrlRateLimitEntry_Object((1,3,6,1,4,1,43,29,4,21,2,2,1))
a3ComQosCtrlRateLimitEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitEntry.setStatus(_A)
class _A3ComQosCtrlRateLimitCtrlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65532))
_A3ComQosCtrlRateLimitCtrlIndex_Type.__name__=_C
_A3ComQosCtrlRateLimitCtrlIndex_Object=MibTableColumn
a3ComQosCtrlRateLimitCtrlIndex=_A3ComQosCtrlRateLimitCtrlIndex_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,1),_A3ComQosCtrlRateLimitCtrlIndex_Type())
a3ComQosCtrlRateLimitCtrlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitCtrlIndex.setStatus(_A)
class _A3ComQosCtrlRateLimitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_A3ComQosCtrlRateLimitIndex_Type.__name__=_C
_A3ComQosCtrlRateLimitIndex_Object=MibTableColumn
a3ComQosCtrlRateLimitIndex=_A3ComQosCtrlRateLimitIndex_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,2),_A3ComQosCtrlRateLimitIndex_Type())
a3ComQosCtrlRateLimitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitIndex.setStatus(_A)
class _A3ComQosCtrlRateLimitPercent_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,101))
_A3ComQosCtrlRateLimitPercent_Type.__name__=_C
_A3ComQosCtrlRateLimitPercent_Object=MibTableColumn
a3ComQosCtrlRateLimitPercent=_A3ComQosCtrlRateLimitPercent_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,3),_A3ComQosCtrlRateLimitPercent_Type())
a3ComQosCtrlRateLimitPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitPercent.setStatus(_A)
class _A3ComQosCtrlRateLimitKbps_Type(Integer32):defaultValue=-1
_A3ComQosCtrlRateLimitKbps_Type.__name__=_C
_A3ComQosCtrlRateLimitKbps_Object=MibTableColumn
a3ComQosCtrlRateLimitKbps=_A3ComQosCtrlRateLimitKbps_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,4),_A3ComQosCtrlRateLimitKbps_Type())
a3ComQosCtrlRateLimitKbps.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitKbps.setStatus(_A)
class _A3ComQosCtrlRateLimitPorts_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_A3ComQosCtrlRateLimitPorts_Type.__name__=_F
_A3ComQosCtrlRateLimitPorts_Object=MibTableColumn
a3ComQosCtrlRateLimitPorts=_A3ComQosCtrlRateLimitPorts_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,5),_A3ComQosCtrlRateLimitPorts_Type())
a3ComQosCtrlRateLimitPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitPorts.setStatus(_A)
_A3ComQosCtrlRateLimitRowStatus_Type=RowStatus
_A3ComQosCtrlRateLimitRowStatus_Object=MibTableColumn
a3ComQosCtrlRateLimitRowStatus=_A3ComQosCtrlRateLimitRowStatus_Object((1,3,6,1,4,1,43,29,4,21,2,2,1,6),_A3ComQosCtrlRateLimitRowStatus_Type())
a3ComQosCtrlRateLimitRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosCtrlRateLimitRowStatus.setStatus(_A)
_A3ComQosRsvp_ObjectIdentity=ObjectIdentity
a3ComQosRsvp=_A3ComQosRsvp_ObjectIdentity((1,3,6,1,4,1,43,29,4,21,3))
class _A3ComQosRsvpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rsvpEnabled',1),('rsvpDisabled',2)))
_A3ComQosRsvpStatus_Type.__name__=_C
_A3ComQosRsvpStatus_Object=MibScalar
a3ComQosRsvpStatus=_A3ComQosRsvpStatus_Object((1,3,6,1,4,1,43,29,4,21,3,1),_A3ComQosRsvpStatus_Type())
a3ComQosRsvpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpStatus.setStatus(_A)
class _A3ComQosRsvpMaxTotalResvdBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_A3ComQosRsvpMaxTotalResvdBandwidth_Type.__name__=_C
_A3ComQosRsvpMaxTotalResvdBandwidth_Object=MibScalar
a3ComQosRsvpMaxTotalResvdBandwidth=_A3ComQosRsvpMaxTotalResvdBandwidth_Object((1,3,6,1,4,1,43,29,4,21,3,2),_A3ComQosRsvpMaxTotalResvdBandwidth_Type())
a3ComQosRsvpMaxTotalResvdBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpMaxTotalResvdBandwidth.setStatus(_A)
class _A3ComQosRsvpMaxPerResvBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_A3ComQosRsvpMaxPerResvBandwidth_Type.__name__=_C
_A3ComQosRsvpMaxPerResvBandwidth_Object=MibScalar
a3ComQosRsvpMaxPerResvBandwidth=_A3ComQosRsvpMaxPerResvBandwidth_Object((1,3,6,1,4,1,43,29,4,21,3,3),_A3ComQosRsvpMaxPerResvBandwidth_Type())
a3ComQosRsvpMaxPerResvBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpMaxPerResvBandwidth.setStatus(_A)
class _A3ComQosRsvpPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('edge',1),('always',2),('never',3)))
_A3ComQosRsvpPolicy_Type.__name__=_C
_A3ComQosRsvpPolicy_Object=MibScalar
a3ComQosRsvpPolicy=_A3ComQosRsvpPolicy_Object((1,3,6,1,4,1,43,29,4,21,3,4),_A3ComQosRsvpPolicy_Type())
a3ComQosRsvpPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpPolicy.setStatus(_A)
class _A3ComQosRsvpExcessTrafficPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComQosRsvpExcessTrafficPolicy_Type.__name__=_C
_A3ComQosRsvpExcessTrafficPolicy_Object=MibScalar
a3ComQosRsvpExcessTrafficPolicy=_A3ComQosRsvpExcessTrafficPolicy_Object((1,3,6,1,4,1,43,29,4,21,3,5),_A3ComQosRsvpExcessTrafficPolicy_Type())
a3ComQosRsvpExcessTrafficPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpExcessTrafficPolicy.setStatus(_A)
class _A3ComQosRsvpExcessPktsLossEligible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_A3ComQosRsvpExcessPktsLossEligible_Type.__name__=_C
_A3ComQosRsvpExcessPktsLossEligible_Object=MibScalar
a3ComQosRsvpExcessPktsLossEligible=_A3ComQosRsvpExcessPktsLossEligible_Object((1,3,6,1,4,1,43,29,4,21,3,6),_A3ComQosRsvpExcessPktsLossEligible_Type())
a3ComQosRsvpExcessPktsLossEligible.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpExcessPktsLossEligible.setStatus(_A)
class _A3ComQosRsvpAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_A3ComQosRsvpAuthentication_Type.__name__=_C
_A3ComQosRsvpAuthentication_Object=MibScalar
a3ComQosRsvpAuthentication=_A3ComQosRsvpAuthentication_Object((1,3,6,1,4,1,43,29,4,21,3,7),_A3ComQosRsvpAuthentication_Type())
a3ComQosRsvpAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpAuthentication.setStatus(_A)
class _A3ComQosRsvpMd5Key_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_A3ComQosRsvpMd5Key_Type.__name__=_F
_A3ComQosRsvpMd5Key_Object=MibScalar
a3ComQosRsvpMd5Key=_A3ComQosRsvpMd5Key_Object((1,3,6,1,4,1,43,29,4,21,3,8),_A3ComQosRsvpMd5Key_Type())
a3ComQosRsvpMd5Key.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosRsvpMd5Key.setStatus(_A)
_A3ComQosStats_ObjectIdentity=ObjectIdentity
a3ComQosStats=_A3ComQosStats_ObjectIdentity((1,3,6,1,4,1,43,29,4,21,4))
class _A3ComQosStatsInterval_Type(Integer32):defaultValue=1
_A3ComQosStatsInterval_Type.__name__=_C
_A3ComQosStatsInterval_Object=MibScalar
a3ComQosStatsInterval=_A3ComQosStatsInterval_Object((1,3,6,1,4,1,43,29,4,21,4,1),_A3ComQosStatsInterval_Type())
a3ComQosStatsInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosStatsInterval.setStatus(_A)
_A3ComQosXmtStatsTable_Object=MibTable
a3ComQosXmtStatsTable=_A3ComQosXmtStatsTable_Object((1,3,6,1,4,1,43,29,4,21,4,2))
if mibBuilder.loadTexts:a3ComQosXmtStatsTable.setStatus(_A)
_A3ComQosXmtStatsEntry_Object=MibTableRow
a3ComQosXmtStatsEntry=_A3ComQosXmtStatsEntry_Object((1,3,6,1,4,1,43,29,4,21,4,2,1))
a3ComQosXmtStatsEntry.setIndexNames((0,_I,_J),(0,_E,_f))
if mibBuilder.loadTexts:a3ComQosXmtStatsEntry.setStatus(_A)
class _A3ComQosXmtStatsQindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_g,1),(_K,2),(_G,3),(_H,4)))
_A3ComQosXmtStatsQindex_Type.__name__=_C
_A3ComQosXmtStatsQindex_Object=MibTableColumn
a3ComQosXmtStatsQindex=_A3ComQosXmtStatsQindex_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,1),_A3ComQosXmtStatsQindex_Type())
a3ComQosXmtStatsQindex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsQindex.setStatus(_A)
_A3ComQosXmtStatsLowLossPkts_Type=Gauge32
_A3ComQosXmtStatsLowLossPkts_Object=MibTableColumn
a3ComQosXmtStatsLowLossPkts=_A3ComQosXmtStatsLowLossPkts_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,2),_A3ComQosXmtStatsLowLossPkts_Type())
a3ComQosXmtStatsLowLossPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsLowLossPkts.setStatus(_A)
_A3ComQosXmtStatsLowLossDelayedPkts_Type=Gauge32
_A3ComQosXmtStatsLowLossDelayedPkts_Object=MibTableColumn
a3ComQosXmtStatsLowLossDelayedPkts=_A3ComQosXmtStatsLowLossDelayedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,3),_A3ComQosXmtStatsLowLossDelayedPkts_Type())
a3ComQosXmtStatsLowLossDelayedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsLowLossDelayedPkts.setStatus(_A)
_A3ComQosXmtStatsLowLossDiscardedPkts_Type=Gauge32
_A3ComQosXmtStatsLowLossDiscardedPkts_Object=MibTableColumn
a3ComQosXmtStatsLowLossDiscardedPkts=_A3ComQosXmtStatsLowLossDiscardedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,4),_A3ComQosXmtStatsLowLossDiscardedPkts_Type())
a3ComQosXmtStatsLowLossDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsLowLossDiscardedPkts.setStatus(_A)
_A3ComQosXmtStatsHighLossPkts_Type=Gauge32
_A3ComQosXmtStatsHighLossPkts_Object=MibTableColumn
a3ComQosXmtStatsHighLossPkts=_A3ComQosXmtStatsHighLossPkts_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,5),_A3ComQosXmtStatsHighLossPkts_Type())
a3ComQosXmtStatsHighLossPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsHighLossPkts.setStatus(_A)
_A3ComQosXmtStatsHighLossDiscardedPkts_Type=Gauge32
_A3ComQosXmtStatsHighLossDiscardedPkts_Object=MibTableColumn
a3ComQosXmtStatsHighLossDiscardedPkts=_A3ComQosXmtStatsHighLossDiscardedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,2,1,6),_A3ComQosXmtStatsHighLossDiscardedPkts_Type())
a3ComQosXmtStatsHighLossDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtStatsHighLossDiscardedPkts.setStatus(_A)
_A3ComQosXmtHmStatsTable_Object=MibTable
a3ComQosXmtHmStatsTable=_A3ComQosXmtHmStatsTable_Object((1,3,6,1,4,1,43,29,4,21,4,3))
if mibBuilder.loadTexts:a3ComQosXmtHmStatsTable.setStatus(_A)
_A3ComQosXmtHmStatsEntry_Object=MibTableRow
a3ComQosXmtHmStatsEntry=_A3ComQosXmtHmStatsEntry_Object((1,3,6,1,4,1,43,29,4,21,4,3,1))
a3ComQosXmtHmStatsEntry.setIndexNames((0,_I,_J),(0,_E,_h))
if mibBuilder.loadTexts:a3ComQosXmtHmStatsEntry.setStatus(_A)
class _A3ComQosXmtHmStatsQindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_g,1),(_K,2),(_G,3),(_H,4)))
_A3ComQosXmtHmStatsQindex_Type.__name__=_C
_A3ComQosXmtHmStatsQindex_Object=MibTableColumn
a3ComQosXmtHmStatsQindex=_A3ComQosXmtHmStatsQindex_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,1),_A3ComQosXmtHmStatsQindex_Type())
a3ComQosXmtHmStatsQindex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsQindex.setStatus(_A)
_A3ComQosXmtHmStatsLowLossPkts_Type=Gauge32
_A3ComQosXmtHmStatsLowLossPkts_Object=MibTableColumn
a3ComQosXmtHmStatsLowLossPkts=_A3ComQosXmtHmStatsLowLossPkts_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,2),_A3ComQosXmtHmStatsLowLossPkts_Type())
a3ComQosXmtHmStatsLowLossPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsLowLossPkts.setStatus(_A)
_A3ComQosXmtHmStatsLowLossDelayedPkts_Type=Gauge32
_A3ComQosXmtHmStatsLowLossDelayedPkts_Object=MibTableColumn
a3ComQosXmtHmStatsLowLossDelayedPkts=_A3ComQosXmtHmStatsLowLossDelayedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,3),_A3ComQosXmtHmStatsLowLossDelayedPkts_Type())
a3ComQosXmtHmStatsLowLossDelayedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsLowLossDelayedPkts.setStatus(_A)
_A3ComQosXmtHmStatsLowLossDiscardedPkts_Type=Gauge32
_A3ComQosXmtHmStatsLowLossDiscardedPkts_Object=MibTableColumn
a3ComQosXmtHmStatsLowLossDiscardedPkts=_A3ComQosXmtHmStatsLowLossDiscardedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,4),_A3ComQosXmtHmStatsLowLossDiscardedPkts_Type())
a3ComQosXmtHmStatsLowLossDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsLowLossDiscardedPkts.setStatus(_A)
_A3ComQosXmtHmStatsHighLossPkts_Type=Gauge32
_A3ComQosXmtHmStatsHighLossPkts_Object=MibTableColumn
a3ComQosXmtHmStatsHighLossPkts=_A3ComQosXmtHmStatsHighLossPkts_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,5),_A3ComQosXmtHmStatsHighLossPkts_Type())
a3ComQosXmtHmStatsHighLossPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsHighLossPkts.setStatus(_A)
_A3ComQosXmtHmStatsHighLossDiscardedPkts_Type=Gauge32
_A3ComQosXmtHmStatsHighLossDiscardedPkts_Object=MibTableColumn
a3ComQosXmtHmStatsHighLossDiscardedPkts=_A3ComQosXmtHmStatsHighLossDiscardedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,3,1,6),_A3ComQosXmtHmStatsHighLossDiscardedPkts_Type())
a3ComQosXmtHmStatsHighLossDiscardedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosXmtHmStatsHighLossDiscardedPkts.setStatus(_A)
_A3ComQosRcvStatsTable_Object=MibTable
a3ComQosRcvStatsTable=_A3ComQosRcvStatsTable_Object((1,3,6,1,4,1,43,29,4,21,4,4))
if mibBuilder.loadTexts:a3ComQosRcvStatsTable.setStatus(_A)
_A3ComQosRcvStatsEntry_Object=MibTableRow
a3ComQosRcvStatsEntry=_A3ComQosRcvStatsEntry_Object((1,3,6,1,4,1,43,29,4,21,4,4,1))
a3ComQosRcvStatsEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:a3ComQosRcvStatsEntry.setStatus(_A)
_A3ComQosRcvStatsConformBytesTotal_Type=Gauge32
_A3ComQosRcvStatsConformBytesTotal_Object=MibTableColumn
a3ComQosRcvStatsConformBytesTotal=_A3ComQosRcvStatsConformBytesTotal_Object((1,3,6,1,4,1,43,29,4,21,4,4,1,1),_A3ComQosRcvStatsConformBytesTotal_Type())
a3ComQosRcvStatsConformBytesTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosRcvStatsConformBytesTotal.setStatus(_A)
_A3ComQosRcvStatsNonConformBytesForFlows_Type=Gauge32
_A3ComQosRcvStatsNonConformBytesForFlows_Object=MibTableColumn
a3ComQosRcvStatsNonConformBytesForFlows=_A3ComQosRcvStatsNonConformBytesForFlows_Object((1,3,6,1,4,1,43,29,4,21,4,4,1,2),_A3ComQosRcvStatsNonConformBytesForFlows_Type())
a3ComQosRcvStatsNonConformBytesForFlows.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosRcvStatsNonConformBytesForFlows.setStatus(_A)
_A3ComQosRcvStatsNonConformBytesForNonFlows_Type=Gauge32
_A3ComQosRcvStatsNonConformBytesForNonFlows_Object=MibTableColumn
a3ComQosRcvStatsNonConformBytesForNonFlows=_A3ComQosRcvStatsNonConformBytesForNonFlows_Object((1,3,6,1,4,1,43,29,4,21,4,4,1,3),_A3ComQosRcvStatsNonConformBytesForNonFlows_Type())
a3ComQosRcvStatsNonConformBytesForNonFlows.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosRcvStatsNonConformBytesForNonFlows.setStatus(_A)
_A3ComQosRcvStatsDroppedPkts_Type=Gauge32
_A3ComQosRcvStatsDroppedPkts_Object=MibTableColumn
a3ComQosRcvStatsDroppedPkts=_A3ComQosRcvStatsDroppedPkts_Object((1,3,6,1,4,1,43,29,4,21,4,4,1,4),_A3ComQosRcvStatsDroppedPkts_Type())
a3ComQosRcvStatsDroppedPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComQosRcvStatsDroppedPkts.setStatus(_A)
_A3ComQosMisc_ObjectIdentity=ObjectIdentity
a3ComQosMisc=_A3ComQosMisc_ObjectIdentity((1,3,6,1,4,1,43,29,4,21,5))
class _A3ComQosBandwidthRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_A3ComQosBandwidthRatio_Type.__name__=_C
_A3ComQosBandwidthRatio_Object=MibScalar
a3ComQosBandwidthRatio=_A3ComQosBandwidthRatio_Object((1,3,6,1,4,1,43,29,4,21,5,1),_A3ComQosBandwidthRatio_Type())
a3ComQosBandwidthRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosBandwidthRatio.setStatus(_A)
class _A3ComQosExcessTrafficClassTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_N,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9)))
_A3ComQosExcessTrafficClassTag_Type.__name__=_C
_A3ComQosExcessTrafficClassTag_Object=MibScalar
a3ComQosExcessTrafficClassTag=_A3ComQosExcessTrafficClassTag_Object((1,3,6,1,4,1,43,29,4,21,5,2),_A3ComQosExcessTrafficClassTag_Type())
a3ComQosExcessTrafficClassTag.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComQosExcessTrafficClassTag.setStatus(_A)
a3ComQosFlowClassIntrudingEvent=NotificationType((1,3,6,1,4,1,43,29,4,0,88))
a3ComQosFlowClassIntrudingEvent.setObjects(*((_E,_M),(_E,_i),(_E,_j),(_E,_k)))
if mibBuilder.loadTexts:a3ComQosFlowClassIntrudingEvent.setStatus('')
mibBuilder.exportSymbols(_E,**{'RowStatus':RowStatus,'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComQosFlowClassIntrudingEvent':a3ComQosFlowClassIntrudingEvent,'a3ComQos':a3ComQos,'a3ComQosClass':a3ComQosClass,'a3ComQosGenClassTable':a3ComQosGenClassTable,'a3ComQosGenClassEntry':a3ComQosGenClassEntry,_P:a3ComQosGenClassIndex,'a3ComQosGenClassName':a3ComQosGenClassName,'a3ComQosGenClassControlId':a3ComQosGenClassControlId,'a3ComQosFlowClassTable':a3ComQosFlowClassTable,'a3ComQosFlowClassEntry':a3ComQosFlowClassEntry,_M:a3ComQosFlowClassIndex,_Q:a3ComQosFlowClassFilterIndex,'a3ComQosFlowClassCastType':a3ComQosFlowClassCastType,_i:a3ComQosFlowClassIpProtoType,_j:a3ComQosFlowClassSrcAddr,'a3ComQosFlowClassSrcSubnetMask':a3ComQosFlowClassSrcSubnetMask,_k:a3ComQosFlowClassDestAddr,'a3ComQosFlowClassDestSubnetMask':a3ComQosFlowClassDestSubnetMask,'a3ComQosFlowClassPortStart':a3ComQosFlowClassPortStart,'a3ComQosFlowClassPortEnd':a3ComQosFlowClassPortEnd,'a3ComQosFlowClassRowStatus':a3ComQosFlowClassRowStatus,'a3ComQosNonFlowClassTable':a3ComQosNonFlowClassTable,'a3ComQosNonFlowClassEntry':a3ComQosNonFlowClassEntry,_R:a3ComQosNonFlowClassIndex,'a3ComQosNonFlowClassCastType':a3ComQosNonFlowClassCastType,'a3ComQosNonFlowClassProtos':a3ComQosNonFlowClassProtos,'a3ComQosNonFlowClass8021pTags':a3ComQosNonFlowClass8021pTags,'a3ComQosNonFlowClassRowStatus':a3ComQosNonFlowClassRowStatus,'a3ComQosNonFlowClassProtoDescriptor':a3ComQosNonFlowClassProtoDescriptor,'a3ComQosNonFlowClassCustomProto':a3ComQosNonFlowClassCustomProto,'a3ComQosCtrl':a3ComQosCtrl,'a3ComQosCtrlTable':a3ComQosCtrlTable,'a3ComQosCtrlEntry':a3ComQosCtrlEntry,_S:a3ComQosCtrlIndex,'a3ComQosCtrlName':a3ComQosCtrlName,'a3ComQosCtrlServiceLevel':a3ComQosCtrlServiceLevel,'a3ComQosCtrlConformPktsLossEligible':a3ComQosCtrlConformPktsLossEligible,'a3ComQosCtrlExcessPktsServiceLevel':a3ComQosCtrlExcessPktsServiceLevel,'a3ComQosCtrlExcessPktsLossEligible':a3ComQosCtrlExcessPktsLossEligible,'a3ComQosCtrl8021pTag':a3ComQosCtrl8021pTag,'a3ComQosCtrlRateLimitType':a3ComQosCtrlRateLimitType,'a3ComQosCtrlRowStatus':a3ComQosCtrlRowStatus,'a3ComQosCtrlRateLimitTable':a3ComQosCtrlRateLimitTable,'a3ComQosCtrlRateLimitEntry':a3ComQosCtrlRateLimitEntry,_d:a3ComQosCtrlRateLimitCtrlIndex,_e:a3ComQosCtrlRateLimitIndex,'a3ComQosCtrlRateLimitPercent':a3ComQosCtrlRateLimitPercent,'a3ComQosCtrlRateLimitKbps':a3ComQosCtrlRateLimitKbps,'a3ComQosCtrlRateLimitPorts':a3ComQosCtrlRateLimitPorts,'a3ComQosCtrlRateLimitRowStatus':a3ComQosCtrlRateLimitRowStatus,'a3ComQosRsvp':a3ComQosRsvp,'a3ComQosRsvpStatus':a3ComQosRsvpStatus,'a3ComQosRsvpMaxTotalResvdBandwidth':a3ComQosRsvpMaxTotalResvdBandwidth,'a3ComQosRsvpMaxPerResvBandwidth':a3ComQosRsvpMaxPerResvBandwidth,'a3ComQosRsvpPolicy':a3ComQosRsvpPolicy,'a3ComQosRsvpExcessTrafficPolicy':a3ComQosRsvpExcessTrafficPolicy,'a3ComQosRsvpExcessPktsLossEligible':a3ComQosRsvpExcessPktsLossEligible,'a3ComQosRsvpAuthentication':a3ComQosRsvpAuthentication,'a3ComQosRsvpMd5Key':a3ComQosRsvpMd5Key,'a3ComQosStats':a3ComQosStats,'a3ComQosStatsInterval':a3ComQosStatsInterval,'a3ComQosXmtStatsTable':a3ComQosXmtStatsTable,'a3ComQosXmtStatsEntry':a3ComQosXmtStatsEntry,_f:a3ComQosXmtStatsQindex,'a3ComQosXmtStatsLowLossPkts':a3ComQosXmtStatsLowLossPkts,'a3ComQosXmtStatsLowLossDelayedPkts':a3ComQosXmtStatsLowLossDelayedPkts,'a3ComQosXmtStatsLowLossDiscardedPkts':a3ComQosXmtStatsLowLossDiscardedPkts,'a3ComQosXmtStatsHighLossPkts':a3ComQosXmtStatsHighLossPkts,'a3ComQosXmtStatsHighLossDiscardedPkts':a3ComQosXmtStatsHighLossDiscardedPkts,'a3ComQosXmtHmStatsTable':a3ComQosXmtHmStatsTable,'a3ComQosXmtHmStatsEntry':a3ComQosXmtHmStatsEntry,_h:a3ComQosXmtHmStatsQindex,'a3ComQosXmtHmStatsLowLossPkts':a3ComQosXmtHmStatsLowLossPkts,'a3ComQosXmtHmStatsLowLossDelayedPkts':a3ComQosXmtHmStatsLowLossDelayedPkts,'a3ComQosXmtHmStatsLowLossDiscardedPkts':a3ComQosXmtHmStatsLowLossDiscardedPkts,'a3ComQosXmtHmStatsHighLossPkts':a3ComQosXmtHmStatsHighLossPkts,'a3ComQosXmtHmStatsHighLossDiscardedPkts':a3ComQosXmtHmStatsHighLossDiscardedPkts,'a3ComQosRcvStatsTable':a3ComQosRcvStatsTable,'a3ComQosRcvStatsEntry':a3ComQosRcvStatsEntry,'a3ComQosRcvStatsConformBytesTotal':a3ComQosRcvStatsConformBytesTotal,'a3ComQosRcvStatsNonConformBytesForFlows':a3ComQosRcvStatsNonConformBytesForFlows,'a3ComQosRcvStatsNonConformBytesForNonFlows':a3ComQosRcvStatsNonConformBytesForNonFlows,'a3ComQosRcvStatsDroppedPkts':a3ComQosRcvStatsDroppedPkts,'a3ComQosMisc':a3ComQosMisc,'a3ComQosBandwidthRatio':a3ComQosBandwidthRatio,'a3ComQosExcessTrafficClassTag':a3ComQosExcessTrafficClassTag})