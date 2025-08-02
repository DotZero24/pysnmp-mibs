_J='snAgAclPortBindDirection'
_I='snAgAclPortNum'
_H='snAgAclIndex'
_G='DisplayString'
_F='undefined'
_E='HP-SN-IP-ACL-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snIp,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','snIp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
class RtrStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
class SnRowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('valid',2),('delete',3),('create',4)))
class Action(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deny',0),('permit',1)))
class TruthVal(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
class AclNumber(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,199))
class Operator(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,7)));namedValues=NamedValues(*(('eq',0),('neq',1),('lt',2),('gt',3),('range',4),(_F,7)))
class IpProtocol(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class PrecedenceValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('routine',0),('priority',1),('immediate',2),('flash',3),('flashoverride',4),('critical',5),('internet',6),('network',7),(_F,8)))
class TosValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('normal',0),('minMonetaryCost',1),('maxReliability',2),('tosValue3',3),('maxThroughput',4),('tosValue5',5),('tosValue6',6),('tosValue7',7),('minDelay',8),('tosValue9',9),('tosValue10',10),('tosValue11',11),('tosValue12',12),('tosValue13',13),('tosValue14',14),('tosValue15',15),(_F,16)))
class Direction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inbound',0),('outbound',1)))
_SnAgAcl_ObjectIdentity=ObjectIdentity
snAgAcl=_SnAgAcl_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15))
_SnAgAclGlobal_ObjectIdentity=ObjectIdentity
snAgAclGlobal=_SnAgAclGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,1))
_SnAgAclGblCurRowIndex_Type=Integer32
_SnAgAclGblCurRowIndex_Object=MibScalar
snAgAclGblCurRowIndex=_SnAgAclGblCurRowIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,1,1),_SnAgAclGblCurRowIndex_Type())
snAgAclGblCurRowIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclGblCurRowIndex.setStatus(_A)
_SnAgAclTable_Object=MibTable
snAgAclTable=_SnAgAclTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2))
if mibBuilder.loadTexts:snAgAclTable.setStatus(_A)
_SnAgAclEntry_Object=MibTableRow
snAgAclEntry=_SnAgAclEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1))
snAgAclEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:snAgAclEntry.setStatus(_A)
_SnAgAclIndex_Type=Integer32
_SnAgAclIndex_Object=MibTableColumn
snAgAclIndex=_SnAgAclIndex_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,1),_SnAgAclIndex_Type())
snAgAclIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclIndex.setStatus(_A)
_SnAgAclNumber_Type=AclNumber
_SnAgAclNumber_Object=MibTableColumn
snAgAclNumber=_SnAgAclNumber_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,2),_SnAgAclNumber_Type())
snAgAclNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclNumber.setStatus(_A)
_SnAgAclName_Type=DisplayString
_SnAgAclName_Object=MibTableColumn
snAgAclName=_SnAgAclName_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,3),_SnAgAclName_Type())
snAgAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclName.setStatus(_A)
_SnAgAclAction_Type=Action
_SnAgAclAction_Object=MibTableColumn
snAgAclAction=_SnAgAclAction_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,4),_SnAgAclAction_Type())
snAgAclAction.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclAction.setStatus(_A)
_SnAgAclProtocol_Type=IpProtocol
_SnAgAclProtocol_Object=MibTableColumn
snAgAclProtocol=_SnAgAclProtocol_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,5),_SnAgAclProtocol_Type())
snAgAclProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclProtocol.setStatus(_A)
_SnAgAclSourceIp_Type=IpAddress
_SnAgAclSourceIp_Object=MibTableColumn
snAgAclSourceIp=_SnAgAclSourceIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,6),_SnAgAclSourceIp_Type())
snAgAclSourceIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclSourceIp.setStatus(_A)
_SnAgAclSourceMask_Type=IpAddress
_SnAgAclSourceMask_Object=MibTableColumn
snAgAclSourceMask=_SnAgAclSourceMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,7),_SnAgAclSourceMask_Type())
snAgAclSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclSourceMask.setStatus(_A)
_SnAgAclSourceOperator_Type=Operator
_SnAgAclSourceOperator_Object=MibTableColumn
snAgAclSourceOperator=_SnAgAclSourceOperator_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,8),_SnAgAclSourceOperator_Type())
snAgAclSourceOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclSourceOperator.setStatus(_A)
class _SnAgAclSourceOperand1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnAgAclSourceOperand1_Type.__name__=_C
_SnAgAclSourceOperand1_Object=MibTableColumn
snAgAclSourceOperand1=_SnAgAclSourceOperand1_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,9),_SnAgAclSourceOperand1_Type())
snAgAclSourceOperand1.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclSourceOperand1.setStatus(_A)
class _SnAgAclSourceOperand2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnAgAclSourceOperand2_Type.__name__=_C
_SnAgAclSourceOperand2_Object=MibTableColumn
snAgAclSourceOperand2=_SnAgAclSourceOperand2_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,10),_SnAgAclSourceOperand2_Type())
snAgAclSourceOperand2.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclSourceOperand2.setStatus(_A)
_SnAgAclDestinationIp_Type=IpAddress
_SnAgAclDestinationIp_Object=MibTableColumn
snAgAclDestinationIp=_SnAgAclDestinationIp_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,11),_SnAgAclDestinationIp_Type())
snAgAclDestinationIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDestinationIp.setStatus(_A)
_SnAgAclDestinationMask_Type=IpAddress
_SnAgAclDestinationMask_Object=MibTableColumn
snAgAclDestinationMask=_SnAgAclDestinationMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,12),_SnAgAclDestinationMask_Type())
snAgAclDestinationMask.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDestinationMask.setStatus(_A)
_SnAgAclDestinationOperator_Type=Operator
_SnAgAclDestinationOperator_Object=MibTableColumn
snAgAclDestinationOperator=_SnAgAclDestinationOperator_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,13),_SnAgAclDestinationOperator_Type())
snAgAclDestinationOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDestinationOperator.setStatus(_A)
class _SnAgAclDestinationOperand1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnAgAclDestinationOperand1_Type.__name__=_C
_SnAgAclDestinationOperand1_Object=MibTableColumn
snAgAclDestinationOperand1=_SnAgAclDestinationOperand1_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,14),_SnAgAclDestinationOperand1_Type())
snAgAclDestinationOperand1.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDestinationOperand1.setStatus(_A)
class _SnAgAclDestinationOperand2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnAgAclDestinationOperand2_Type.__name__=_C
_SnAgAclDestinationOperand2_Object=MibTableColumn
snAgAclDestinationOperand2=_SnAgAclDestinationOperand2_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,15),_SnAgAclDestinationOperand2_Type())
snAgAclDestinationOperand2.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDestinationOperand2.setStatus(_A)
_SnAgAclPrecedence_Type=PrecedenceValue
_SnAgAclPrecedence_Object=MibTableColumn
snAgAclPrecedence=_SnAgAclPrecedence_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,16),_SnAgAclPrecedence_Type())
snAgAclPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclPrecedence.setStatus(_A)
_SnAgAclTos_Type=TosValue
_SnAgAclTos_Object=MibTableColumn
snAgAclTos=_SnAgAclTos_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,17),_SnAgAclTos_Type())
snAgAclTos.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclTos.setStatus(_A)
_SnAgAclEstablished_Type=RtrStatus
_SnAgAclEstablished_Object=MibTableColumn
snAgAclEstablished=_SnAgAclEstablished_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,18),_SnAgAclEstablished_Type())
snAgAclEstablished.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclEstablished.setStatus(_A)
_SnAgAclLogOption_Type=TruthVal
_SnAgAclLogOption_Object=MibTableColumn
snAgAclLogOption=_SnAgAclLogOption_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,19),_SnAgAclLogOption_Type())
snAgAclLogOption.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclLogOption.setStatus(_A)
_SnAgAclStandardFlag_Type=TruthVal
_SnAgAclStandardFlag_Object=MibTableColumn
snAgAclStandardFlag=_SnAgAclStandardFlag_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,20),_SnAgAclStandardFlag_Type())
snAgAclStandardFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclStandardFlag.setStatus(_A)
_SnAgAclRowStatus_Type=SnRowStatus
_SnAgAclRowStatus_Object=MibTableColumn
snAgAclRowStatus=_SnAgAclRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,21),_SnAgAclRowStatus_Type())
snAgAclRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclRowStatus.setStatus(_A)
_SnAgAclFlowCounter_Type=Counter64
_SnAgAclFlowCounter_Object=MibTableColumn
snAgAclFlowCounter=_SnAgAclFlowCounter_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,22),_SnAgAclFlowCounter_Type())
snAgAclFlowCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclFlowCounter.setStatus(_A)
_SnAgAclPacketCounter_Type=Counter64
_SnAgAclPacketCounter_Object=MibTableColumn
snAgAclPacketCounter=_SnAgAclPacketCounter_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,23),_SnAgAclPacketCounter_Type())
snAgAclPacketCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclPacketCounter.setStatus(_A)
_SnAgAclComments_Type=DisplayString
_SnAgAclComments_Object=MibTableColumn
snAgAclComments=_SnAgAclComments_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,24),_SnAgAclComments_Type())
snAgAclComments.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclComments.setStatus(_A)
class _SnAgAclIpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SnAgAclIpPriority_Type.__name__=_C
_SnAgAclIpPriority_Object=MibTableColumn
snAgAclIpPriority=_SnAgAclIpPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,25),_SnAgAclIpPriority_Type())
snAgAclIpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclIpPriority.setStatus(_A)
class _SnAgAclPriorityForce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_SnAgAclPriorityForce_Type.__name__=_C
_SnAgAclPriorityForce_Object=MibTableColumn
snAgAclPriorityForce=_SnAgAclPriorityForce_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,26),_SnAgAclPriorityForce_Type())
snAgAclPriorityForce.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclPriorityForce.setStatus(_A)
class _SnAgAclPriorityMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SnAgAclPriorityMapping_Type.__name__=_C
_SnAgAclPriorityMapping_Object=MibTableColumn
snAgAclPriorityMapping=_SnAgAclPriorityMapping_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,27),_SnAgAclPriorityMapping_Type())
snAgAclPriorityMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclPriorityMapping.setStatus(_A)
class _SnAgAclDscpMarking_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SnAgAclDscpMarking_Type.__name__=_C
_SnAgAclDscpMarking_Object=MibTableColumn
snAgAclDscpMarking=_SnAgAclDscpMarking_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,28),_SnAgAclDscpMarking_Type())
snAgAclDscpMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDscpMarking.setStatus(_A)
class _SnAgAclDscpMapping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SnAgAclDscpMapping_Type.__name__=_C
_SnAgAclDscpMapping_Object=MibTableColumn
snAgAclDscpMapping=_SnAgAclDscpMapping_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,2,1,29),_SnAgAclDscpMapping_Type())
snAgAclDscpMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclDscpMapping.setStatus(_A)
_SnAgAclBindToPortTable_Object=MibTable
snAgAclBindToPortTable=_SnAgAclBindToPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3))
if mibBuilder.loadTexts:snAgAclBindToPortTable.setStatus(_A)
_SnAgAclBindToPortEntry_Object=MibTableRow
snAgAclBindToPortEntry=_SnAgAclBindToPortEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1))
snAgAclBindToPortEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:snAgAclBindToPortEntry.setStatus(_A)
_SnAgAclPortNum_Type=Integer32
_SnAgAclPortNum_Object=MibTableColumn
snAgAclPortNum=_SnAgAclPortNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,1),_SnAgAclPortNum_Type())
snAgAclPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclPortNum.setStatus(_A)
_SnAgAclPortBindDirection_Type=Direction
_SnAgAclPortBindDirection_Object=MibTableColumn
snAgAclPortBindDirection=_SnAgAclPortBindDirection_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,2),_SnAgAclPortBindDirection_Type())
snAgAclPortBindDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:snAgAclPortBindDirection.setStatus(_A)
_SnAgAclNum_Type=Integer32
_SnAgAclNum_Object=MibTableColumn
snAgAclNum=_SnAgAclNum_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,3),_SnAgAclNum_Type())
snAgAclNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclNum.setStatus(_A)
_SnAgAclNameString_Type=DisplayString
_SnAgAclNameString_Object=MibTableColumn
snAgAclNameString=_SnAgAclNameString_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,4),_SnAgAclNameString_Type())
snAgAclNameString.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclNameString.setStatus(_A)
_SnAgBindPortListInVirtualInterface_Type=OctetString
_SnAgBindPortListInVirtualInterface_Object=MibTableColumn
snAgBindPortListInVirtualInterface=_SnAgBindPortListInVirtualInterface_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,5),_SnAgBindPortListInVirtualInterface_Type())
snAgBindPortListInVirtualInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgBindPortListInVirtualInterface.setStatus(_A)
_SnAgAclPortRowStatus_Type=SnRowStatus
_SnAgAclPortRowStatus_Object=MibTableColumn
snAgAclPortRowStatus=_SnAgAclPortRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,2,15,3,1,6),_SnAgAclPortRowStatus_Type())
snAgAclPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snAgAclPortRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:DisplayString,'RtrStatus':RtrStatus,'SnRowStatus':SnRowStatus,'Action':Action,'TruthVal':TruthVal,'AclNumber':AclNumber,'Operator':Operator,'IpProtocol':IpProtocol,'PrecedenceValue':PrecedenceValue,'TosValue':TosValue,'Direction':Direction,'snAgAcl':snAgAcl,'snAgAclGlobal':snAgAclGlobal,'snAgAclGblCurRowIndex':snAgAclGblCurRowIndex,'snAgAclTable':snAgAclTable,'snAgAclEntry':snAgAclEntry,_H:snAgAclIndex,'snAgAclNumber':snAgAclNumber,'snAgAclName':snAgAclName,'snAgAclAction':snAgAclAction,'snAgAclProtocol':snAgAclProtocol,'snAgAclSourceIp':snAgAclSourceIp,'snAgAclSourceMask':snAgAclSourceMask,'snAgAclSourceOperator':snAgAclSourceOperator,'snAgAclSourceOperand1':snAgAclSourceOperand1,'snAgAclSourceOperand2':snAgAclSourceOperand2,'snAgAclDestinationIp':snAgAclDestinationIp,'snAgAclDestinationMask':snAgAclDestinationMask,'snAgAclDestinationOperator':snAgAclDestinationOperator,'snAgAclDestinationOperand1':snAgAclDestinationOperand1,'snAgAclDestinationOperand2':snAgAclDestinationOperand2,'snAgAclPrecedence':snAgAclPrecedence,'snAgAclTos':snAgAclTos,'snAgAclEstablished':snAgAclEstablished,'snAgAclLogOption':snAgAclLogOption,'snAgAclStandardFlag':snAgAclStandardFlag,'snAgAclRowStatus':snAgAclRowStatus,'snAgAclFlowCounter':snAgAclFlowCounter,'snAgAclPacketCounter':snAgAclPacketCounter,'snAgAclComments':snAgAclComments,'snAgAclIpPriority':snAgAclIpPriority,'snAgAclPriorityForce':snAgAclPriorityForce,'snAgAclPriorityMapping':snAgAclPriorityMapping,'snAgAclDscpMarking':snAgAclDscpMarking,'snAgAclDscpMapping':snAgAclDscpMapping,'snAgAclBindToPortTable':snAgAclBindToPortTable,'snAgAclBindToPortEntry':snAgAclBindToPortEntry,_I:snAgAclPortNum,_J:snAgAclPortBindDirection,'snAgAclNum':snAgAclNum,'snAgAclNameString':snAgAclNameString,'snAgBindPortListInVirtualInterface':snAgBindPortListInVirtualInterface,'snAgAclPortRowStatus':snAgAclPortRowStatus})