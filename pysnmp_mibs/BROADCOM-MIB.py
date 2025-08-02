_m='rlBcmAclPortsDirection'
_l='rlBcmAclPortsIfIndex'
_k='rlBcmAclRowIndex'
_j='rlBcmAclID'
_i='rlBcmACLNamesName'
_h='rlTosOverwriteMapRange'
_g='rlTosOverwriteMapName'
_f='rlBcmQoSRateLimitOutIfindex'
_e='rlBcmQoSRateLimitInIfindex'
_d='rlBcmQoSRateLimitIPflowDstPort'
_c='rlBcmQoSRateLimitIPflowSrcPort'
_b='rlBcmQoSRateLimitIPflowDstIpMask'
_a='rlBcmQoSRateLimitIPflowDstIp'
_Z='rlBcmQoSRateLimitIPflowSrcIpMask'
_Y='rlBcmQoSRateLimitIPflowSrcIp'
_X='rlBcmQoSRateLimitIPflowProtocol'
_W='rlBcmQoSRateLimitIPflowTosMask'
_V='rlBcmQoSRateLimitIPflowTos'
_U='rlBcmQoSRateLimitAclApplliedIfIndex'
_T='rlBcmQoSRateLimitAclName'
_S='rlBcmQoSRateLimitIndex'
_R='rlBcmQoSRateLimitName'
_Q='rlBcmQoSRateLimitType'
_P='permit'
_O='rlPolicySimpleBcmMibRulesIndex'
_N='rlPolicySimpleBcmMibIndex'
_M='current'
_L='disable'
_K='enable'
_J='TruthValue'
_I='00000000'
_H='IpAddress'
_G='OctetString'
_F='DisplayString'
_E='read-only'
_D='BROADCOM-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rlBroadcom,=mibBuilder.importSymbols('RADLAN-MIB','rlBroadcom')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_H,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention',_J)
class RlPolicySimpleBcmMibProfileType(TextualConvention,Integer32):status=_M;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bandwidthGuarantee',1),('minDelay',2),('bestEffort',3)))
class RlBcmQoSRateLimitType(TextualConvention,Integer32):status=_M;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('aggregate',1),('flowAggregate',2),('perFlow',3),('multiField',4),('inPort',5),('outPort',6),('qosIP',7),('qosIPAcl',8)))
_RlBcmMibVersion_Type=Integer32
_RlBcmMibVersion_Object=MibScalar
rlBcmMibVersion=_RlBcmMibVersion_Object((1,3,6,1,4,1,89,68,1),_RlBcmMibVersion_Type())
rlBcmMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlBcmMibVersion.setStatus(_A)
_RlPolicySimpleBcmMib_ObjectIdentity=ObjectIdentity
rlPolicySimpleBcmMib=_RlPolicySimpleBcmMib_ObjectIdentity((1,3,6,1,4,1,89,68,2))
_RlPolicySimpleBcmMibVersion_Type=Integer32
_RlPolicySimpleBcmMibVersion_Object=MibScalar
rlPolicySimpleBcmMibVersion=_RlPolicySimpleBcmMibVersion_Object((1,3,6,1,4,1,89,68,2,1),_RlPolicySimpleBcmMibVersion_Type())
rlPolicySimpleBcmMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibVersion.setStatus(_A)
class _RlPolicySimpleBcmMibReservedBW_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlPolicySimpleBcmMibReservedBW_Type.__name__=_C
_RlPolicySimpleBcmMibReservedBW_Object=MibScalar
rlPolicySimpleBcmMibReservedBW=_RlPolicySimpleBcmMibReservedBW_Object((1,3,6,1,4,1,89,68,2,2),_RlPolicySimpleBcmMibReservedBW_Type())
rlPolicySimpleBcmMibReservedBW.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibReservedBW.setStatus(_A)
class _RlPolicySimpleBcmMibPolicyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RlPolicySimpleBcmMibPolicyEnable_Type.__name__=_C
_RlPolicySimpleBcmMibPolicyEnable_Object=MibScalar
rlPolicySimpleBcmMibPolicyEnable=_RlPolicySimpleBcmMibPolicyEnable_Object((1,3,6,1,4,1,89,68,2,3),_RlPolicySimpleBcmMibPolicyEnable_Type())
rlPolicySimpleBcmMibPolicyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibPolicyEnable.setStatus(_A)
_RlPolicySimpleBcmMibProfileTable_Object=MibTable
rlPolicySimpleBcmMibProfileTable=_RlPolicySimpleBcmMibProfileTable_Object((1,3,6,1,4,1,89,68,2,4))
if mibBuilder.loadTexts:rlPolicySimpleBcmMibProfileTable.setStatus(_A)
_RlPolicySimpleBcmMibProfileEntry_Object=MibTableRow
rlPolicySimpleBcmMibProfileEntry=_RlPolicySimpleBcmMibProfileEntry_Object((1,3,6,1,4,1,89,68,2,4,1))
rlPolicySimpleBcmMibProfileEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:rlPolicySimpleBcmMibProfileEntry.setStatus(_A)
class _RlPolicySimpleBcmMibIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048576))
_RlPolicySimpleBcmMibIndex_Type.__name__=_C
_RlPolicySimpleBcmMibIndex_Object=MibTableColumn
rlPolicySimpleBcmMibIndex=_RlPolicySimpleBcmMibIndex_Object((1,3,6,1,4,1,89,68,2,4,1,1),_RlPolicySimpleBcmMibIndex_Type())
rlPolicySimpleBcmMibIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibIndex.setStatus(_A)
class _RlPolicySimpleBcmMibDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RlPolicySimpleBcmMibDescription_Type.__name__=_F
_RlPolicySimpleBcmMibDescription_Object=MibTableColumn
rlPolicySimpleBcmMibDescription=_RlPolicySimpleBcmMibDescription_Object((1,3,6,1,4,1,89,68,2,4,1,2),_RlPolicySimpleBcmMibDescription_Type())
rlPolicySimpleBcmMibDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibDescription.setStatus(_A)
_RlPolicySimpleBcmMibProfileType_Type=RlPolicySimpleBcmMibProfileType
_RlPolicySimpleBcmMibProfileType_Object=MibTableColumn
rlPolicySimpleBcmMibProfileType=_RlPolicySimpleBcmMibProfileType_Object((1,3,6,1,4,1,89,68,2,4,1,3),_RlPolicySimpleBcmMibProfileType_Type())
rlPolicySimpleBcmMibProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibProfileType.setStatus(_A)
class _RlPolicySimpleBcmMibRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPolicySimpleBcmMibRate_Type.__name__=_C
_RlPolicySimpleBcmMibRate_Object=MibTableColumn
rlPolicySimpleBcmMibRate=_RlPolicySimpleBcmMibRate_Object((1,3,6,1,4,1,89,68,2,4,1,4),_RlPolicySimpleBcmMibRate_Type())
rlPolicySimpleBcmMibRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRate.setStatus(_A)
class _RlPolicySimpleBcmMibBurstSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPolicySimpleBcmMibBurstSize_Type.__name__=_C
_RlPolicySimpleBcmMibBurstSize_Object=MibTableColumn
rlPolicySimpleBcmMibBurstSize=_RlPolicySimpleBcmMibBurstSize_Object((1,3,6,1,4,1,89,68,2,4,1,5),_RlPolicySimpleBcmMibBurstSize_Type())
rlPolicySimpleBcmMibBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibBurstSize.setStatus(_A)
class _RlPolicySimpleBcmMibChangeTosOrDscp_Type(TruthValue):defaultValue=2
_RlPolicySimpleBcmMibChangeTosOrDscp_Type.__name__=_J
_RlPolicySimpleBcmMibChangeTosOrDscp_Object=MibTableColumn
rlPolicySimpleBcmMibChangeTosOrDscp=_RlPolicySimpleBcmMibChangeTosOrDscp_Object((1,3,6,1,4,1,89,68,2,4,1,6),_RlPolicySimpleBcmMibChangeTosOrDscp_Type())
rlPolicySimpleBcmMibChangeTosOrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibChangeTosOrDscp.setStatus(_A)
class _RlPolicySimpleBcmMibNewTosOrDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlPolicySimpleBcmMibNewTosOrDscp_Type.__name__=_C
_RlPolicySimpleBcmMibNewTosOrDscp_Object=MibTableColumn
rlPolicySimpleBcmMibNewTosOrDscp=_RlPolicySimpleBcmMibNewTosOrDscp_Object((1,3,6,1,4,1,89,68,2,4,1,7),_RlPolicySimpleBcmMibNewTosOrDscp_Type())
rlPolicySimpleBcmMibNewTosOrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibNewTosOrDscp.setStatus(_A)
_RlPolicySimpleBcmMibStatus_Type=RowStatus
_RlPolicySimpleBcmMibStatus_Object=MibTableColumn
rlPolicySimpleBcmMibStatus=_RlPolicySimpleBcmMibStatus_Object((1,3,6,1,4,1,89,68,2,4,1,8),_RlPolicySimpleBcmMibStatus_Type())
rlPolicySimpleBcmMibStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibStatus.setStatus(_A)
_RlPolicySimpleBcmMibRulesTable_Object=MibTable
rlPolicySimpleBcmMibRulesTable=_RlPolicySimpleBcmMibRulesTable_Object((1,3,6,1,4,1,89,68,2,5))
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesTable.setStatus(_A)
_RlPolicySimpleBcmMibRulesEntry_Object=MibTableRow
rlPolicySimpleBcmMibRulesEntry=_RlPolicySimpleBcmMibRulesEntry_Object((1,3,6,1,4,1,89,68,2,5,1))
rlPolicySimpleBcmMibRulesEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesEntry.setStatus(_A)
class _RlPolicySimpleBcmMibRulesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048576))
_RlPolicySimpleBcmMibRulesIndex_Type.__name__=_C
_RlPolicySimpleBcmMibRulesIndex_Object=MibTableColumn
rlPolicySimpleBcmMibRulesIndex=_RlPolicySimpleBcmMibRulesIndex_Object((1,3,6,1,4,1,89,68,2,5,1,1),_RlPolicySimpleBcmMibRulesIndex_Type())
rlPolicySimpleBcmMibRulesIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesIndex.setStatus(_A)
class _RlPolicySimpleBcmMibRulesDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RlPolicySimpleBcmMibRulesDescription_Type.__name__=_F
_RlPolicySimpleBcmMibRulesDescription_Object=MibTableColumn
rlPolicySimpleBcmMibRulesDescription=_RlPolicySimpleBcmMibRulesDescription_Object((1,3,6,1,4,1,89,68,2,5,1,2),_RlPolicySimpleBcmMibRulesDescription_Type())
rlPolicySimpleBcmMibRulesDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesDescription.setStatus(_A)
class _RlPolicySimpleBcmMibRulesDstMac_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_RlPolicySimpleBcmMibRulesDstMac_Type.__name__=_G
_RlPolicySimpleBcmMibRulesDstMac_Object=MibTableColumn
rlPolicySimpleBcmMibRulesDstMac=_RlPolicySimpleBcmMibRulesDstMac_Object((1,3,6,1,4,1,89,68,2,5,1,3),_RlPolicySimpleBcmMibRulesDstMac_Type())
rlPolicySimpleBcmMibRulesDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesDstMac.setStatus(_A)
class _RlPolicySimpleBcmMibRulesSrcMac_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_RlPolicySimpleBcmMibRulesSrcMac_Type.__name__=_G
_RlPolicySimpleBcmMibRulesSrcMac_Object=MibTableColumn
rlPolicySimpleBcmMibRulesSrcMac=_RlPolicySimpleBcmMibRulesSrcMac_Object((1,3,6,1,4,1,89,68,2,5,1,4),_RlPolicySimpleBcmMibRulesSrcMac_Type())
rlPolicySimpleBcmMibRulesSrcMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesSrcMac.setStatus(_A)
class _RlPolicySimpleBcmMibRulesVpt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlPolicySimpleBcmMibRulesVpt_Type.__name__=_C
_RlPolicySimpleBcmMibRulesVpt_Object=MibTableColumn
rlPolicySimpleBcmMibRulesVpt=_RlPolicySimpleBcmMibRulesVpt_Object((1,3,6,1,4,1,89,68,2,5,1,5),_RlPolicySimpleBcmMibRulesVpt_Type())
rlPolicySimpleBcmMibRulesVpt.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesVpt.setStatus(_A)
class _RlPolicySimpleBcmMibRulesVid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RlPolicySimpleBcmMibRulesVid_Type.__name__=_C
_RlPolicySimpleBcmMibRulesVid_Object=MibTableColumn
rlPolicySimpleBcmMibRulesVid=_RlPolicySimpleBcmMibRulesVid_Object((1,3,6,1,4,1,89,68,2,5,1,6),_RlPolicySimpleBcmMibRulesVid_Type())
rlPolicySimpleBcmMibRulesVid.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesVid.setStatus(_A)
class _RlPolicySimpleBcmMibRulesEthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPolicySimpleBcmMibRulesEthType_Type.__name__=_C
_RlPolicySimpleBcmMibRulesEthType_Object=MibTableColumn
rlPolicySimpleBcmMibRulesEthType=_RlPolicySimpleBcmMibRulesEthType_Object((1,3,6,1,4,1,89,68,2,5,1,7),_RlPolicySimpleBcmMibRulesEthType_Type())
rlPolicySimpleBcmMibRulesEthType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesEthType.setStatus(_A)
class _RlPolicySimpleBcmMibRulesTosOrDscp_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlPolicySimpleBcmMibRulesTosOrDscp_Type.__name__=_C
_RlPolicySimpleBcmMibRulesTosOrDscp_Object=MibTableColumn
rlPolicySimpleBcmMibRulesTosOrDscp=_RlPolicySimpleBcmMibRulesTosOrDscp_Object((1,3,6,1,4,1,89,68,2,5,1,8),_RlPolicySimpleBcmMibRulesTosOrDscp_Type())
rlPolicySimpleBcmMibRulesTosOrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesTosOrDscp.setStatus(_A)
class _RlPolicySimpleBcmMibRulesProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlPolicySimpleBcmMibRulesProtocol_Type.__name__=_C
_RlPolicySimpleBcmMibRulesProtocol_Object=MibTableColumn
rlPolicySimpleBcmMibRulesProtocol=_RlPolicySimpleBcmMibRulesProtocol_Object((1,3,6,1,4,1,89,68,2,5,1,9),_RlPolicySimpleBcmMibRulesProtocol_Type())
rlPolicySimpleBcmMibRulesProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesProtocol.setStatus(_A)
class _RlPolicySimpleBcmMibRulesSrcIp_Type(IpAddress):defaultHexValue=_I
_RlPolicySimpleBcmMibRulesSrcIp_Type.__name__=_H
_RlPolicySimpleBcmMibRulesSrcIp_Object=MibTableColumn
rlPolicySimpleBcmMibRulesSrcIp=_RlPolicySimpleBcmMibRulesSrcIp_Object((1,3,6,1,4,1,89,68,2,5,1,10),_RlPolicySimpleBcmMibRulesSrcIp_Type())
rlPolicySimpleBcmMibRulesSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesSrcIp.setStatus(_A)
class _RlPolicySimpleBcmMibRulesSrcIpMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RlPolicySimpleBcmMibRulesSrcIpMask_Type.__name__=_C
_RlPolicySimpleBcmMibRulesSrcIpMask_Object=MibTableColumn
rlPolicySimpleBcmMibRulesSrcIpMask=_RlPolicySimpleBcmMibRulesSrcIpMask_Object((1,3,6,1,4,1,89,68,2,5,1,11),_RlPolicySimpleBcmMibRulesSrcIpMask_Type())
rlPolicySimpleBcmMibRulesSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesSrcIpMask.setStatus(_A)
class _RlPolicySimpleBcmMibRulesDstIp_Type(IpAddress):defaultHexValue=_I
_RlPolicySimpleBcmMibRulesDstIp_Type.__name__=_H
_RlPolicySimpleBcmMibRulesDstIp_Object=MibTableColumn
rlPolicySimpleBcmMibRulesDstIp=_RlPolicySimpleBcmMibRulesDstIp_Object((1,3,6,1,4,1,89,68,2,5,1,12),_RlPolicySimpleBcmMibRulesDstIp_Type())
rlPolicySimpleBcmMibRulesDstIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesDstIp.setStatus(_A)
class _RlPolicySimpleBcmMibRulesDstIpMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RlPolicySimpleBcmMibRulesDstIpMask_Type.__name__=_C
_RlPolicySimpleBcmMibRulesDstIpMask_Object=MibTableColumn
rlPolicySimpleBcmMibRulesDstIpMask=_RlPolicySimpleBcmMibRulesDstIpMask_Object((1,3,6,1,4,1,89,68,2,5,1,13),_RlPolicySimpleBcmMibRulesDstIpMask_Type())
rlPolicySimpleBcmMibRulesDstIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesDstIpMask.setStatus(_A)
class _RlPolicySimpleBcmMibRulesSrcPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPolicySimpleBcmMibRulesSrcPort_Type.__name__=_C
_RlPolicySimpleBcmMibRulesSrcPort_Object=MibTableColumn
rlPolicySimpleBcmMibRulesSrcPort=_RlPolicySimpleBcmMibRulesSrcPort_Object((1,3,6,1,4,1,89,68,2,5,1,14),_RlPolicySimpleBcmMibRulesSrcPort_Type())
rlPolicySimpleBcmMibRulesSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesSrcPort.setStatus(_A)
class _RlPolicySimpleBcmMibRulesDstPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPolicySimpleBcmMibRulesDstPort_Type.__name__=_C
_RlPolicySimpleBcmMibRulesDstPort_Object=MibTableColumn
rlPolicySimpleBcmMibRulesDstPort=_RlPolicySimpleBcmMibRulesDstPort_Object((1,3,6,1,4,1,89,68,2,5,1,15),_RlPolicySimpleBcmMibRulesDstPort_Type())
rlPolicySimpleBcmMibRulesDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesDstPort.setStatus(_A)
_RlPolicySimpleBcmMibRulesInIfIndexList_Type=PortList
_RlPolicySimpleBcmMibRulesInIfIndexList_Object=MibTableColumn
rlPolicySimpleBcmMibRulesInIfIndexList=_RlPolicySimpleBcmMibRulesInIfIndexList_Object((1,3,6,1,4,1,89,68,2,5,1,16),_RlPolicySimpleBcmMibRulesInIfIndexList_Type())
rlPolicySimpleBcmMibRulesInIfIndexList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesInIfIndexList.setStatus(_A)
_RlPolicySimpleBcmMibRulesOutIfIndexList_Type=PortList
_RlPolicySimpleBcmMibRulesOutIfIndexList_Object=MibTableColumn
rlPolicySimpleBcmMibRulesOutIfIndexList=_RlPolicySimpleBcmMibRulesOutIfIndexList_Object((1,3,6,1,4,1,89,68,2,5,1,17),_RlPolicySimpleBcmMibRulesOutIfIndexList_Type())
rlPolicySimpleBcmMibRulesOutIfIndexList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesOutIfIndexList.setStatus(_A)
class _RlPolicySimpleBcmMibRulesAction_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('block',1),('blockAndTrap',2),('permitAndTrap',3),(_P,4)))
_RlPolicySimpleBcmMibRulesAction_Type.__name__=_C
_RlPolicySimpleBcmMibRulesAction_Object=MibTableColumn
rlPolicySimpleBcmMibRulesAction=_RlPolicySimpleBcmMibRulesAction_Object((1,3,6,1,4,1,89,68,2,5,1,18),_RlPolicySimpleBcmMibRulesAction_Type())
rlPolicySimpleBcmMibRulesAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesAction.setStatus(_A)
class _RlPolicySimpleBcmMibRulesProfilePointer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RlPolicySimpleBcmMibRulesProfilePointer_Type.__name__=_C
_RlPolicySimpleBcmMibRulesProfilePointer_Object=MibTableColumn
rlPolicySimpleBcmMibRulesProfilePointer=_RlPolicySimpleBcmMibRulesProfilePointer_Object((1,3,6,1,4,1,89,68,2,5,1,19),_RlPolicySimpleBcmMibRulesProfilePointer_Type())
rlPolicySimpleBcmMibRulesProfilePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesProfilePointer.setStatus(_A)
class _RlPolicySimpleBcmMibRulesBitsUsed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_RlPolicySimpleBcmMibRulesBitsUsed_Type.__name__=_G
_RlPolicySimpleBcmMibRulesBitsUsed_Object=MibTableColumn
rlPolicySimpleBcmMibRulesBitsUsed=_RlPolicySimpleBcmMibRulesBitsUsed_Object((1,3,6,1,4,1,89,68,2,5,1,20),_RlPolicySimpleBcmMibRulesBitsUsed_Type())
rlPolicySimpleBcmMibRulesBitsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesBitsUsed.setStatus(_A)
_RlPolicySimpleBcmMibRulesStatus_Type=RowStatus
_RlPolicySimpleBcmMibRulesStatus_Object=MibTableColumn
rlPolicySimpleBcmMibRulesStatus=_RlPolicySimpleBcmMibRulesStatus_Object((1,3,6,1,4,1,89,68,2,5,1,21),_RlPolicySimpleBcmMibRulesStatus_Type())
rlPolicySimpleBcmMibRulesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPolicySimpleBcmMibRulesStatus.setStatus(_A)
_RlBcmRateLimit_ObjectIdentity=ObjectIdentity
rlBcmRateLimit=_RlBcmRateLimit_ObjectIdentity((1,3,6,1,4,1,89,68,3))
_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Type=Integer32
_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Object=MibScalar
rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown=_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Object((1,3,6,1,4,1,89,68,3,1),_RlBcmPacketRateLimitBroadcstMulticastUnicastUnknown_Type())
rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown.setStatus(_A)
class _RlBcmPacketRateLimitMulticastEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlBcmPacketRateLimitMulticastEnable_Type.__name__=_C
_RlBcmPacketRateLimitMulticastEnable_Object=MibScalar
rlBcmPacketRateLimitMulticastEnable=_RlBcmPacketRateLimitMulticastEnable_Object((1,3,6,1,4,1,89,68,3,2),_RlBcmPacketRateLimitMulticastEnable_Type())
rlBcmPacketRateLimitMulticastEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmPacketRateLimitMulticastEnable.setStatus(_A)
class _RlBcmPacketRateLimitBroadcstEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlBcmPacketRateLimitBroadcstEnable_Type.__name__=_C
_RlBcmPacketRateLimitBroadcstEnable_Object=MibScalar
rlBcmPacketRateLimitBroadcstEnable=_RlBcmPacketRateLimitBroadcstEnable_Object((1,3,6,1,4,1,89,68,3,3),_RlBcmPacketRateLimitBroadcstEnable_Type())
rlBcmPacketRateLimitBroadcstEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmPacketRateLimitBroadcstEnable.setStatus(_A)
class _RlBcmPacketRateLimitUnicastUnknownEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlBcmPacketRateLimitUnicastUnknownEnable_Type.__name__=_C
_RlBcmPacketRateLimitUnicastUnknownEnable_Object=MibScalar
rlBcmPacketRateLimitUnicastUnknownEnable=_RlBcmPacketRateLimitUnicastUnknownEnable_Object((1,3,6,1,4,1,89,68,3,4),_RlBcmPacketRateLimitUnicastUnknownEnable_Type())
rlBcmPacketRateLimitUnicastUnknownEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmPacketRateLimitUnicastUnknownEnable.setStatus(_A)
_RlBcmQoSRateLimit_ObjectIdentity=ObjectIdentity
rlBcmQoSRateLimit=_RlBcmQoSRateLimit_ObjectIdentity((1,3,6,1,4,1,89,68,4))
_RlBcmQoSRateLimitIndexCounter_Type=Integer32
_RlBcmQoSRateLimitIndexCounter_Object=MibScalar
rlBcmQoSRateLimitIndexCounter=_RlBcmQoSRateLimitIndexCounter_Object((1,3,6,1,4,1,89,68,4,1),_RlBcmQoSRateLimitIndexCounter_Type())
rlBcmQoSRateLimitIndexCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIndexCounter.setStatus(_A)
_RlBcmQoSRateLimitTable_Object=MibTable
rlBcmQoSRateLimitTable=_RlBcmQoSRateLimitTable_Object((1,3,6,1,4,1,89,68,4,2))
if mibBuilder.loadTexts:rlBcmQoSRateLimitTable.setStatus(_A)
_RlBcmQoSRateLimitEntry_Object=MibTableRow
rlBcmQoSRateLimitEntry=_RlBcmQoSRateLimitEntry_Object((1,3,6,1,4,1,89,68,4,2,1))
rlBcmQoSRateLimitEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:rlBcmQoSRateLimitEntry.setStatus(_A)
_RlBcmQoSRateLimitType_Type=RlBcmQoSRateLimitType
_RlBcmQoSRateLimitType_Object=MibTableColumn
rlBcmQoSRateLimitType=_RlBcmQoSRateLimitType_Object((1,3,6,1,4,1,89,68,4,2,1,1),_RlBcmQoSRateLimitType_Type())
rlBcmQoSRateLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitType.setStatus(_A)
class _RlBcmQoSRateLimitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RlBcmQoSRateLimitName_Type.__name__=_F
_RlBcmQoSRateLimitName_Object=MibTableColumn
rlBcmQoSRateLimitName=_RlBcmQoSRateLimitName_Object((1,3,6,1,4,1,89,68,4,2,1,2),_RlBcmQoSRateLimitName_Type())
rlBcmQoSRateLimitName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitName.setStatus(_A)
_RlBcmQoSRateLimitIndex_Type=Integer32
_RlBcmQoSRateLimitIndex_Object=MibTableColumn
rlBcmQoSRateLimitIndex=_RlBcmQoSRateLimitIndex_Object((1,3,6,1,4,1,89,68,4,2,1,3),_RlBcmQoSRateLimitIndex_Type())
rlBcmQoSRateLimitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIndex.setStatus(_A)
class _RlBcmQoSRateLimitAclsNameOrFlow_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RlBcmQoSRateLimitAclsNameOrFlow_Type.__name__=_G
_RlBcmQoSRateLimitAclsNameOrFlow_Object=MibTableColumn
rlBcmQoSRateLimitAclsNameOrFlow=_RlBcmQoSRateLimitAclsNameOrFlow_Object((1,3,6,1,4,1,89,68,4,2,1,4),_RlBcmQoSRateLimitAclsNameOrFlow_Type())
rlBcmQoSRateLimitAclsNameOrFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclsNameOrFlow.setStatus(_A)
class _RlBcmQoSRateLimitPortsOrInterfaces_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_RlBcmQoSRateLimitPortsOrInterfaces_Type.__name__=_F
_RlBcmQoSRateLimitPortsOrInterfaces_Object=MibTableColumn
rlBcmQoSRateLimitPortsOrInterfaces=_RlBcmQoSRateLimitPortsOrInterfaces_Object((1,3,6,1,4,1,89,68,4,2,1,5),_RlBcmQoSRateLimitPortsOrInterfaces_Type())
rlBcmQoSRateLimitPortsOrInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitPortsOrInterfaces.setStatus(_A)
class _RlBcmQoSRateLimitRatePriority_Type(Integer32):defaultValue=0
_RlBcmQoSRateLimitRatePriority_Type.__name__=_C
_RlBcmQoSRateLimitRatePriority_Object=MibTableColumn
rlBcmQoSRateLimitRatePriority=_RlBcmQoSRateLimitRatePriority_Object((1,3,6,1,4,1,89,68,4,2,1,6),_RlBcmQoSRateLimitRatePriority_Type())
rlBcmQoSRateLimitRatePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitRatePriority.setStatus(_A)
class _RlBcmQoSRateLimitBurstSizeTosMask_Type(Integer32):defaultValue=0
_RlBcmQoSRateLimitBurstSizeTosMask_Type.__name__=_C
_RlBcmQoSRateLimitBurstSizeTosMask_Object=MibTableColumn
rlBcmQoSRateLimitBurstSizeTosMask=_RlBcmQoSRateLimitBurstSizeTosMask_Object((1,3,6,1,4,1,89,68,4,2,1,7),_RlBcmQoSRateLimitBurstSizeTosMask_Type())
rlBcmQoSRateLimitBurstSizeTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitBurstSizeTosMask.setStatus(_A)
class _RlBcmQoSRateLimitDropOutProfile_Type(TruthValue):defaultValue=2
_RlBcmQoSRateLimitDropOutProfile_Type.__name__=_J
_RlBcmQoSRateLimitDropOutProfile_Object=MibTableColumn
rlBcmQoSRateLimitDropOutProfile=_RlBcmQoSRateLimitDropOutProfile_Object((1,3,6,1,4,1,89,68,4,2,1,8),_RlBcmQoSRateLimitDropOutProfile_Type())
rlBcmQoSRateLimitDropOutProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitDropOutProfile.setStatus(_A)
class _RlBcmQoSRateLimitNewTos_Type(Integer32):defaultValue=64
_RlBcmQoSRateLimitNewTos_Type.__name__=_C
_RlBcmQoSRateLimitNewTos_Object=MibTableColumn
rlBcmQoSRateLimitNewTos=_RlBcmQoSRateLimitNewTos_Object((1,3,6,1,4,1,89,68,4,2,1,9),_RlBcmQoSRateLimitNewTos_Type())
rlBcmQoSRateLimitNewTos.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitNewTos.setStatus(_A)
class _RlBcmQoSRateLimitNewTosPrecedence_Type(Integer32):defaultValue=16
_RlBcmQoSRateLimitNewTosPrecedence_Type.__name__=_C
_RlBcmQoSRateLimitNewTosPrecedence_Object=MibTableColumn
rlBcmQoSRateLimitNewTosPrecedence=_RlBcmQoSRateLimitNewTosPrecedence_Object((1,3,6,1,4,1,89,68,4,2,1,10),_RlBcmQoSRateLimitNewTosPrecedence_Type())
rlBcmQoSRateLimitNewTosPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitNewTosPrecedence.setStatus(_A)
_RlBcmQoSRateLimitStatus_Type=RowStatus
_RlBcmQoSRateLimitStatus_Object=MibTableColumn
rlBcmQoSRateLimitStatus=_RlBcmQoSRateLimitStatus_Object((1,3,6,1,4,1,89,68,4,2,1,11),_RlBcmQoSRateLimitStatus_Type())
rlBcmQoSRateLimitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitStatus.setStatus(_A)
_RlBcmQoSRateLimitAclApplliedTable_Object=MibTable
rlBcmQoSRateLimitAclApplliedTable=_RlBcmQoSRateLimitAclApplliedTable_Object((1,3,6,1,4,1,89,68,4,3))
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclApplliedTable.setStatus(_A)
_RlBcmQoSRateLimitAclApplliedEntry_Object=MibTableRow
rlBcmQoSRateLimitAclApplliedEntry=_RlBcmQoSRateLimitAclApplliedEntry_Object((1,3,6,1,4,1,89,68,4,3,1))
rlBcmQoSRateLimitAclApplliedEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclApplliedEntry.setStatus(_A)
class _RlBcmQoSRateLimitAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RlBcmQoSRateLimitAclName_Type.__name__=_F
_RlBcmQoSRateLimitAclName_Object=MibTableColumn
rlBcmQoSRateLimitAclName=_RlBcmQoSRateLimitAclName_Object((1,3,6,1,4,1,89,68,4,3,1,1),_RlBcmQoSRateLimitAclName_Type())
rlBcmQoSRateLimitAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclName.setStatus(_A)
_RlBcmQoSRateLimitAclApplliedIfIndex_Type=Integer32
_RlBcmQoSRateLimitAclApplliedIfIndex_Object=MibTableColumn
rlBcmQoSRateLimitAclApplliedIfIndex=_RlBcmQoSRateLimitAclApplliedIfIndex_Object((1,3,6,1,4,1,89,68,4,3,1,2),_RlBcmQoSRateLimitAclApplliedIfIndex_Type())
rlBcmQoSRateLimitAclApplliedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclApplliedIfIndex.setStatus(_A)
_RlBcmQoSRateLimitAclApplliedType_Type=Integer32
_RlBcmQoSRateLimitAclApplliedType_Object=MibTableColumn
rlBcmQoSRateLimitAclApplliedType=_RlBcmQoSRateLimitAclApplliedType_Object((1,3,6,1,4,1,89,68,4,3,1,3),_RlBcmQoSRateLimitAclApplliedType_Type())
rlBcmQoSRateLimitAclApplliedType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclApplliedType.setStatus(_A)
_RlBcmQoSRateLimitAclApplliedStatus_Type=RowStatus
_RlBcmQoSRateLimitAclApplliedStatus_Object=MibTableColumn
rlBcmQoSRateLimitAclApplliedStatus=_RlBcmQoSRateLimitAclApplliedStatus_Object((1,3,6,1,4,1,89,68,4,3,1,4),_RlBcmQoSRateLimitAclApplliedStatus_Type())
rlBcmQoSRateLimitAclApplliedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitAclApplliedStatus.setStatus(_A)
_RlBcmQoSRateLimitIPflowTable_Object=MibTable
rlBcmQoSRateLimitIPflowTable=_RlBcmQoSRateLimitIPflowTable_Object((1,3,6,1,4,1,89,68,4,4))
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowTable.setStatus(_A)
_RlBcmQoSRateLimitIPflowEntry_Object=MibTableRow
rlBcmQoSRateLimitIPflowEntry=_RlBcmQoSRateLimitIPflowEntry_Object((1,3,6,1,4,1,89,68,4,4,1))
rlBcmQoSRateLimitIPflowEntry.setIndexNames((0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowEntry.setStatus(_A)
_RlBcmQoSRateLimitIPflowTos_Type=Integer32
_RlBcmQoSRateLimitIPflowTos_Object=MibTableColumn
rlBcmQoSRateLimitIPflowTos=_RlBcmQoSRateLimitIPflowTos_Object((1,3,6,1,4,1,89,68,4,4,1,1),_RlBcmQoSRateLimitIPflowTos_Type())
rlBcmQoSRateLimitIPflowTos.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowTos.setStatus(_A)
_RlBcmQoSRateLimitIPflowTosMask_Type=Integer32
_RlBcmQoSRateLimitIPflowTosMask_Object=MibTableColumn
rlBcmQoSRateLimitIPflowTosMask=_RlBcmQoSRateLimitIPflowTosMask_Object((1,3,6,1,4,1,89,68,4,4,1,2),_RlBcmQoSRateLimitIPflowTosMask_Type())
rlBcmQoSRateLimitIPflowTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowTosMask.setStatus(_A)
_RlBcmQoSRateLimitIPflowProtocol_Type=Integer32
_RlBcmQoSRateLimitIPflowProtocol_Object=MibTableColumn
rlBcmQoSRateLimitIPflowProtocol=_RlBcmQoSRateLimitIPflowProtocol_Object((1,3,6,1,4,1,89,68,4,4,1,3),_RlBcmQoSRateLimitIPflowProtocol_Type())
rlBcmQoSRateLimitIPflowProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowProtocol.setStatus(_A)
_RlBcmQoSRateLimitIPflowSrcIp_Type=IpAddress
_RlBcmQoSRateLimitIPflowSrcIp_Object=MibTableColumn
rlBcmQoSRateLimitIPflowSrcIp=_RlBcmQoSRateLimitIPflowSrcIp_Object((1,3,6,1,4,1,89,68,4,4,1,4),_RlBcmQoSRateLimitIPflowSrcIp_Type())
rlBcmQoSRateLimitIPflowSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowSrcIp.setStatus(_A)
_RlBcmQoSRateLimitIPflowSrcIpMask_Type=IpAddress
_RlBcmQoSRateLimitIPflowSrcIpMask_Object=MibTableColumn
rlBcmQoSRateLimitIPflowSrcIpMask=_RlBcmQoSRateLimitIPflowSrcIpMask_Object((1,3,6,1,4,1,89,68,4,4,1,5),_RlBcmQoSRateLimitIPflowSrcIpMask_Type())
rlBcmQoSRateLimitIPflowSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowSrcIpMask.setStatus(_A)
_RlBcmQoSRateLimitIPflowDstIp_Type=IpAddress
_RlBcmQoSRateLimitIPflowDstIp_Object=MibTableColumn
rlBcmQoSRateLimitIPflowDstIp=_RlBcmQoSRateLimitIPflowDstIp_Object((1,3,6,1,4,1,89,68,4,4,1,6),_RlBcmQoSRateLimitIPflowDstIp_Type())
rlBcmQoSRateLimitIPflowDstIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowDstIp.setStatus(_A)
_RlBcmQoSRateLimitIPflowDstIpMask_Type=IpAddress
_RlBcmQoSRateLimitIPflowDstIpMask_Object=MibTableColumn
rlBcmQoSRateLimitIPflowDstIpMask=_RlBcmQoSRateLimitIPflowDstIpMask_Object((1,3,6,1,4,1,89,68,4,4,1,7),_RlBcmQoSRateLimitIPflowDstIpMask_Type())
rlBcmQoSRateLimitIPflowDstIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowDstIpMask.setStatus(_A)
_RlBcmQoSRateLimitIPflowSrcPort_Type=Integer32
_RlBcmQoSRateLimitIPflowSrcPort_Object=MibTableColumn
rlBcmQoSRateLimitIPflowSrcPort=_RlBcmQoSRateLimitIPflowSrcPort_Object((1,3,6,1,4,1,89,68,4,4,1,8),_RlBcmQoSRateLimitIPflowSrcPort_Type())
rlBcmQoSRateLimitIPflowSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowSrcPort.setStatus(_A)
_RlBcmQoSRateLimitIPflowDstPort_Type=Integer32
_RlBcmQoSRateLimitIPflowDstPort_Object=MibTableColumn
rlBcmQoSRateLimitIPflowDstPort=_RlBcmQoSRateLimitIPflowDstPort_Object((1,3,6,1,4,1,89,68,4,4,1,9),_RlBcmQoSRateLimitIPflowDstPort_Type())
rlBcmQoSRateLimitIPflowDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowDstPort.setStatus(_A)
_RlBcmQoSRateLimitInIfindex_Type=Integer32
_RlBcmQoSRateLimitInIfindex_Object=MibTableColumn
rlBcmQoSRateLimitInIfindex=_RlBcmQoSRateLimitInIfindex_Object((1,3,6,1,4,1,89,68,4,4,1,10),_RlBcmQoSRateLimitInIfindex_Type())
rlBcmQoSRateLimitInIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitInIfindex.setStatus(_A)
_RlBcmQoSRateLimitOutIfindex_Type=Integer32
_RlBcmQoSRateLimitOutIfindex_Object=MibTableColumn
rlBcmQoSRateLimitOutIfindex=_RlBcmQoSRateLimitOutIfindex_Object((1,3,6,1,4,1,89,68,4,4,1,11),_RlBcmQoSRateLimitOutIfindex_Type())
rlBcmQoSRateLimitOutIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitOutIfindex.setStatus(_A)
class _RlBcmQoSRateLimitIPFlowType_Type(Integer32):defaultValue=0
_RlBcmQoSRateLimitIPFlowType_Type.__name__=_C
_RlBcmQoSRateLimitIPFlowType_Object=MibTableColumn
rlBcmQoSRateLimitIPFlowType=_RlBcmQoSRateLimitIPFlowType_Object((1,3,6,1,4,1,89,68,4,4,1,12),_RlBcmQoSRateLimitIPFlowType_Type())
rlBcmQoSRateLimitIPFlowType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPFlowType.setStatus(_A)
class _RlBcmQoSRateLimitIPFlowRule_Type(Integer32):defaultValue=0
_RlBcmQoSRateLimitIPFlowRule_Type.__name__=_C
_RlBcmQoSRateLimitIPFlowRule_Object=MibTableColumn
rlBcmQoSRateLimitIPFlowRule=_RlBcmQoSRateLimitIPFlowRule_Object((1,3,6,1,4,1,89,68,4,4,1,13),_RlBcmQoSRateLimitIPFlowRule_Type())
rlBcmQoSRateLimitIPFlowRule.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPFlowRule.setStatus(_A)
_RlBcmQoSRateLimitIPflowStatus_Type=RowStatus
_RlBcmQoSRateLimitIPflowStatus_Object=MibTableColumn
rlBcmQoSRateLimitIPflowStatus=_RlBcmQoSRateLimitIPflowStatus_Object((1,3,6,1,4,1,89,68,4,4,1,14),_RlBcmQoSRateLimitIPflowStatus_Type())
rlBcmQoSRateLimitIPflowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitIPflowStatus.setStatus(_A)
class _RlBcmQoSRateLimitQoSprecedenceMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_RlBcmQoSRateLimitQoSprecedenceMap_Type.__name__=_G
_RlBcmQoSRateLimitQoSprecedenceMap_Object=MibScalar
rlBcmQoSRateLimitQoSprecedenceMap=_RlBcmQoSRateLimitQoSprecedenceMap_Object((1,3,6,1,4,1,89,68,4,5),_RlBcmQoSRateLimitQoSprecedenceMap_Type())
rlBcmQoSRateLimitQoSprecedenceMap.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmQoSRateLimitQoSprecedenceMap.setStatus(_A)
_RlTosOverwriteMapMib_ObjectIdentity=ObjectIdentity
rlTosOverwriteMapMib=_RlTosOverwriteMapMib_ObjectIdentity((1,3,6,1,4,1,89,68,5))
_RlTosOverwriteMapTable_Object=MibTable
rlTosOverwriteMapTable=_RlTosOverwriteMapTable_Object((1,3,6,1,4,1,89,68,5,1))
if mibBuilder.loadTexts:rlTosOverwriteMapTable.setStatus(_A)
_RlTosOverwriteMapEntry_Object=MibTableRow
rlTosOverwriteMapEntry=_RlTosOverwriteMapEntry_Object((1,3,6,1,4,1,89,68,5,1,1))
rlTosOverwriteMapEntry.setIndexNames((0,_D,_g),(0,_D,_h))
if mibBuilder.loadTexts:rlTosOverwriteMapEntry.setStatus(_A)
class _RlTosOverwriteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_RlTosOverwriteMapName_Type.__name__=_F
_RlTosOverwriteMapName_Object=MibTableColumn
rlTosOverwriteMapName=_RlTosOverwriteMapName_Object((1,3,6,1,4,1,89,68,5,1,1,1),_RlTosOverwriteMapName_Type())
rlTosOverwriteMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlTosOverwriteMapName.setStatus(_A)
class _RlTosOverwriteMapRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(7,63,255)));namedValues=NamedValues(*(('bits',7),('tos',63),('byte',255)))
_RlTosOverwriteMapRange_Type.__name__=_C
_RlTosOverwriteMapRange_Object=MibTableColumn
rlTosOverwriteMapRange=_RlTosOverwriteMapRange_Object((1,3,6,1,4,1,89,68,5,1,1,2),_RlTosOverwriteMapRange_Type())
rlTosOverwriteMapRange.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTosOverwriteMapRange.setStatus(_A)
class _RlTosOverwriteMapMapping_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_RlTosOverwriteMapMapping_Type.__name__=_G
_RlTosOverwriteMapMapping_Object=MibTableColumn
rlTosOverwriteMapMapping=_RlTosOverwriteMapMapping_Object((1,3,6,1,4,1,89,68,5,1,1,3),_RlTosOverwriteMapMapping_Type())
rlTosOverwriteMapMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTosOverwriteMapMapping.setStatus(_A)
_RlTosOverwriteMapPortList_Type=PortList
_RlTosOverwriteMapPortList_Object=MibTableColumn
rlTosOverwriteMapPortList=_RlTosOverwriteMapPortList_Object((1,3,6,1,4,1,89,68,5,1,1,4),_RlTosOverwriteMapPortList_Type())
rlTosOverwriteMapPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTosOverwriteMapPortList.setStatus(_A)
_RlTosOverwriteMapStatus_Type=RowStatus
_RlTosOverwriteMapStatus_Object=MibTableColumn
rlTosOverwriteMapStatus=_RlTosOverwriteMapStatus_Object((1,3,6,1,4,1,89,68,5,1,1,5),_RlTosOverwriteMapStatus_Type())
rlTosOverwriteMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTosOverwriteMapStatus.setStatus(_A)
_RlBcmACLMib_ObjectIdentity=ObjectIdentity
rlBcmACLMib=_RlBcmACLMib_ObjectIdentity((1,3,6,1,4,1,89,68,6))
_RlBcmACLMibVersion_Type=Integer32
_RlBcmACLMibVersion_Object=MibScalar
rlBcmACLMibVersion=_RlBcmACLMibVersion_Object((1,3,6,1,4,1,89,68,6,1),_RlBcmACLMibVersion_Type())
rlBcmACLMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlBcmACLMibVersion.setStatus(_A)
_RlBcmACLMaxNumberOfEntries_Type=Integer32
_RlBcmACLMaxNumberOfEntries_Object=MibScalar
rlBcmACLMaxNumberOfEntries=_RlBcmACLMaxNumberOfEntries_Object((1,3,6,1,4,1,89,68,6,2),_RlBcmACLMaxNumberOfEntries_Type())
rlBcmACLMaxNumberOfEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:rlBcmACLMaxNumberOfEntries.setStatus(_A)
_RlBcmACLNamesTable_Object=MibTable
rlBcmACLNamesTable=_RlBcmACLNamesTable_Object((1,3,6,1,4,1,89,68,6,3))
if mibBuilder.loadTexts:rlBcmACLNamesTable.setStatus(_A)
_RlBcmACLNamesEntry_Object=MibTableRow
rlBcmACLNamesEntry=_RlBcmACLNamesEntry_Object((1,3,6,1,4,1,89,68,6,3,1))
rlBcmACLNamesEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:rlBcmACLNamesEntry.setStatus(_A)
class _RlBcmACLNamesName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,25))
_RlBcmACLNamesName_Type.__name__=_F
_RlBcmACLNamesName_Object=MibTableColumn
rlBcmACLNamesName=_RlBcmACLNamesName_Object((1,3,6,1,4,1,89,68,6,3,1,1),_RlBcmACLNamesName_Type())
rlBcmACLNamesName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlBcmACLNamesName.setStatus(_A)
_RlBcmACLNamesID_Type=Integer32
_RlBcmACLNamesID_Object=MibTableColumn
rlBcmACLNamesID=_RlBcmACLNamesID_Object((1,3,6,1,4,1,89,68,6,3,1,2),_RlBcmACLNamesID_Type())
rlBcmACLNamesID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmACLNamesID.setStatus(_A)
_RlBcmACLNamesStatus_Type=RowStatus
_RlBcmACLNamesStatus_Object=MibTableColumn
rlBcmACLNamesStatus=_RlBcmACLNamesStatus_Object((1,3,6,1,4,1,89,68,6,3,1,3),_RlBcmACLNamesStatus_Type())
rlBcmACLNamesStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmACLNamesStatus.setStatus(_A)
_RlBcmACLTable_Object=MibTable
rlBcmACLTable=_RlBcmACLTable_Object((1,3,6,1,4,1,89,68,6,4))
if mibBuilder.loadTexts:rlBcmACLTable.setStatus(_A)
_RlBcmACLEntry_Object=MibTableRow
rlBcmACLEntry=_RlBcmACLEntry_Object((1,3,6,1,4,1,89,68,6,4,1))
rlBcmACLEntry.setIndexNames((0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:rlBcmACLEntry.setStatus(_A)
_RlBcmAclID_Type=Integer32
_RlBcmAclID_Object=MibTableColumn
rlBcmAclID=_RlBcmAclID_Object((1,3,6,1,4,1,89,68,6,4,1,1),_RlBcmAclID_Type())
rlBcmAclID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclID.setStatus(_A)
_RlBcmAclRowIndex_Type=Integer32
_RlBcmAclRowIndex_Object=MibTableColumn
rlBcmAclRowIndex=_RlBcmAclRowIndex_Object((1,3,6,1,4,1,89,68,6,4,1,2),_RlBcmAclRowIndex_Type())
rlBcmAclRowIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclRowIndex.setStatus(_A)
class _RlBcmAclAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('permitAndLog',2),('deny',3),('denyAndLog',4),('logAndContinue',5)))
_RlBcmAclAction_Type.__name__=_C
_RlBcmAclAction_Object=MibTableColumn
rlBcmAclAction=_RlBcmAclAction_Object((1,3,6,1,4,1,89,68,6,4,1,3),_RlBcmAclAction_Type())
rlBcmAclAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclAction.setStatus(_A)
class _RlBcmAclIPflags_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlBcmAclIPflags_Type.__name__=_C
_RlBcmAclIPflags_Object=MibTableColumn
rlBcmAclIPflags=_RlBcmAclIPflags_Object((1,3,6,1,4,1,89,68,6,4,1,4),_RlBcmAclIPflags_Type())
rlBcmAclIPflags.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclIPflags.setStatus(_A)
class _RlBcmAclIPflagsMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlBcmAclIPflagsMask_Type.__name__=_C
_RlBcmAclIPflagsMask_Object=MibTableColumn
rlBcmAclIPflagsMask=_RlBcmAclIPflagsMask_Object((1,3,6,1,4,1,89,68,6,4,1,5),_RlBcmAclIPflagsMask_Type())
rlBcmAclIPflagsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclIPflagsMask.setStatus(_A)
class _RlBcmAclIPfragOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_RlBcmAclIPfragOffset_Type.__name__=_C
_RlBcmAclIPfragOffset_Object=MibTableColumn
rlBcmAclIPfragOffset=_RlBcmAclIPfragOffset_Object((1,3,6,1,4,1,89,68,6,4,1,6),_RlBcmAclIPfragOffset_Type())
rlBcmAclIPfragOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclIPfragOffset.setStatus(_A)
class _RlBcmAclIPfragOffsetMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_RlBcmAclIPfragOffsetMask_Type.__name__=_C
_RlBcmAclIPfragOffsetMask_Object=MibTableColumn
rlBcmAclIPfragOffsetMask=_RlBcmAclIPfragOffsetMask_Object((1,3,6,1,4,1,89,68,6,4,1,7),_RlBcmAclIPfragOffsetMask_Type())
rlBcmAclIPfragOffsetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclIPfragOffsetMask.setStatus(_A)
class _RlBcmAclIPprotocol_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_RlBcmAclIPprotocol_Type.__name__=_C
_RlBcmAclIPprotocol_Object=MibTableColumn
rlBcmAclIPprotocol=_RlBcmAclIPprotocol_Object((1,3,6,1,4,1,89,68,6,4,1,8),_RlBcmAclIPprotocol_Type())
rlBcmAclIPprotocol.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclIPprotocol.setStatus(_A)
class _RlBcmAclSrcIp_Type(IpAddress):defaultHexValue=_I
_RlBcmAclSrcIp_Type.__name__=_H
_RlBcmAclSrcIp_Object=MibTableColumn
rlBcmAclSrcIp=_RlBcmAclSrcIp_Object((1,3,6,1,4,1,89,68,6,4,1,9),_RlBcmAclSrcIp_Type())
rlBcmAclSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclSrcIp.setStatus(_A)
class _RlBcmAclSrcIpMask_Type(IpAddress):defaultHexValue=_I
_RlBcmAclSrcIpMask_Type.__name__=_H
_RlBcmAclSrcIpMask_Object=MibTableColumn
rlBcmAclSrcIpMask=_RlBcmAclSrcIpMask_Object((1,3,6,1,4,1,89,68,6,4,1,10),_RlBcmAclSrcIpMask_Type())
rlBcmAclSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclSrcIpMask.setStatus(_A)
class _RlBcmAclDstIp_Type(IpAddress):defaultHexValue=_I
_RlBcmAclDstIp_Type.__name__=_H
_RlBcmAclDstIp_Object=MibTableColumn
rlBcmAclDstIp=_RlBcmAclDstIp_Object((1,3,6,1,4,1,89,68,6,4,1,11),_RlBcmAclDstIp_Type())
rlBcmAclDstIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclDstIp.setStatus(_A)
class _RlBcmAclDstIpMask_Type(IpAddress):defaultHexValue=_I
_RlBcmAclDstIpMask_Type.__name__=_H
_RlBcmAclDstIpMask_Object=MibTableColumn
rlBcmAclDstIpMask=_RlBcmAclDstIpMask_Object((1,3,6,1,4,1,89,68,6,4,1,12),_RlBcmAclDstIpMask_Type())
rlBcmAclDstIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclDstIpMask.setStatus(_A)
class _RlBcmAclSrcL4Port_Type(Integer32):defaultValue=65536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_RlBcmAclSrcL4Port_Type.__name__=_C
_RlBcmAclSrcL4Port_Object=MibTableColumn
rlBcmAclSrcL4Port=_RlBcmAclSrcL4Port_Object((1,3,6,1,4,1,89,68,6,4,1,13),_RlBcmAclSrcL4Port_Type())
rlBcmAclSrcL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclSrcL4Port.setStatus(_A)
class _RlBcmAclDstL4Port_Type(Integer32):defaultValue=65536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_RlBcmAclDstL4Port_Type.__name__=_C
_RlBcmAclDstL4Port_Object=MibTableColumn
rlBcmAclDstL4Port=_RlBcmAclDstL4Port_Object((1,3,6,1,4,1,89,68,6,4,1,14),_RlBcmAclDstL4Port_Type())
rlBcmAclDstL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclDstL4Port.setStatus(_A)
class _RlBcmAclTCPbits_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlBcmAclTCPbits_Type.__name__=_C
_RlBcmAclTCPbits_Object=MibTableColumn
rlBcmAclTCPbits=_RlBcmAclTCPbits_Object((1,3,6,1,4,1,89,68,6,4,1,15),_RlBcmAclTCPbits_Type())
rlBcmAclTCPbits.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclTCPbits.setStatus(_A)
class _RlBcmAclTCPbitsMask_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlBcmAclTCPbitsMask_Type.__name__=_C
_RlBcmAclTCPbitsMask_Object=MibTableColumn
rlBcmAclTCPbitsMask=_RlBcmAclTCPbitsMask_Object((1,3,6,1,4,1,89,68,6,4,1,16),_RlBcmAclTCPbitsMask_Type())
rlBcmAclTCPbitsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclTCPbitsMask.setStatus(_A)
_RlBcmAclStatus_Type=RowStatus
_RlBcmAclStatus_Object=MibTableColumn
rlBcmAclStatus=_RlBcmAclStatus_Object((1,3,6,1,4,1,89,68,6,4,1,17),_RlBcmAclStatus_Type())
rlBcmAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclStatus.setStatus(_A)
_RlBcmACLPortsTable_Object=MibTable
rlBcmACLPortsTable=_RlBcmACLPortsTable_Object((1,3,6,1,4,1,89,68,6,5))
if mibBuilder.loadTexts:rlBcmACLPortsTable.setStatus(_A)
_RlBcmACLPortsEntry_Object=MibTableRow
rlBcmACLPortsEntry=_RlBcmACLPortsEntry_Object((1,3,6,1,4,1,89,68,6,5,1))
rlBcmACLPortsEntry.setIndexNames((0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:rlBcmACLPortsEntry.setStatus(_A)
_RlBcmAclPortsIfIndex_Type=Integer32
_RlBcmAclPortsIfIndex_Object=MibTableColumn
rlBcmAclPortsIfIndex=_RlBcmAclPortsIfIndex_Object((1,3,6,1,4,1,89,68,6,5,1,1),_RlBcmAclPortsIfIndex_Type())
rlBcmAclPortsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclPortsIfIndex.setStatus(_A)
class _RlBcmAclPortsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('egress',2),('both',3)))
_RlBcmAclPortsDirection_Type.__name__=_C
_RlBcmAclPortsDirection_Object=MibTableColumn
rlBcmAclPortsDirection=_RlBcmAclPortsDirection_Object((1,3,6,1,4,1,89,68,6,5,1,2),_RlBcmAclPortsDirection_Type())
rlBcmAclPortsDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclPortsDirection.setStatus(_A)
_RlBcmAclPortsAclID_Type=Integer32
_RlBcmAclPortsAclID_Object=MibTableColumn
rlBcmAclPortsAclID=_RlBcmAclPortsAclID_Object((1,3,6,1,4,1,89,68,6,5,1,3),_RlBcmAclPortsAclID_Type())
rlBcmAclPortsAclID.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclPortsAclID.setStatus(_A)
_RlBcmAclPortsStatus_Type=RowStatus
_RlBcmAclPortsStatus_Object=MibTableColumn
rlBcmAclPortsStatus=_RlBcmAclPortsStatus_Object((1,3,6,1,4,1,89,68,6,5,1,4),_RlBcmAclPortsStatus_Type())
rlBcmAclPortsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBcmAclPortsStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RlPolicySimpleBcmMibProfileType':RlPolicySimpleBcmMibProfileType,'RlBcmQoSRateLimitType':RlBcmQoSRateLimitType,'rlBcmMibVersion':rlBcmMibVersion,'rlPolicySimpleBcmMib':rlPolicySimpleBcmMib,'rlPolicySimpleBcmMibVersion':rlPolicySimpleBcmMibVersion,'rlPolicySimpleBcmMibReservedBW':rlPolicySimpleBcmMibReservedBW,'rlPolicySimpleBcmMibPolicyEnable':rlPolicySimpleBcmMibPolicyEnable,'rlPolicySimpleBcmMibProfileTable':rlPolicySimpleBcmMibProfileTable,'rlPolicySimpleBcmMibProfileEntry':rlPolicySimpleBcmMibProfileEntry,_N:rlPolicySimpleBcmMibIndex,'rlPolicySimpleBcmMibDescription':rlPolicySimpleBcmMibDescription,'rlPolicySimpleBcmMibProfileType':rlPolicySimpleBcmMibProfileType,'rlPolicySimpleBcmMibRate':rlPolicySimpleBcmMibRate,'rlPolicySimpleBcmMibBurstSize':rlPolicySimpleBcmMibBurstSize,'rlPolicySimpleBcmMibChangeTosOrDscp':rlPolicySimpleBcmMibChangeTosOrDscp,'rlPolicySimpleBcmMibNewTosOrDscp':rlPolicySimpleBcmMibNewTosOrDscp,'rlPolicySimpleBcmMibStatus':rlPolicySimpleBcmMibStatus,'rlPolicySimpleBcmMibRulesTable':rlPolicySimpleBcmMibRulesTable,'rlPolicySimpleBcmMibRulesEntry':rlPolicySimpleBcmMibRulesEntry,_O:rlPolicySimpleBcmMibRulesIndex,'rlPolicySimpleBcmMibRulesDescription':rlPolicySimpleBcmMibRulesDescription,'rlPolicySimpleBcmMibRulesDstMac':rlPolicySimpleBcmMibRulesDstMac,'rlPolicySimpleBcmMibRulesSrcMac':rlPolicySimpleBcmMibRulesSrcMac,'rlPolicySimpleBcmMibRulesVpt':rlPolicySimpleBcmMibRulesVpt,'rlPolicySimpleBcmMibRulesVid':rlPolicySimpleBcmMibRulesVid,'rlPolicySimpleBcmMibRulesEthType':rlPolicySimpleBcmMibRulesEthType,'rlPolicySimpleBcmMibRulesTosOrDscp':rlPolicySimpleBcmMibRulesTosOrDscp,'rlPolicySimpleBcmMibRulesProtocol':rlPolicySimpleBcmMibRulesProtocol,'rlPolicySimpleBcmMibRulesSrcIp':rlPolicySimpleBcmMibRulesSrcIp,'rlPolicySimpleBcmMibRulesSrcIpMask':rlPolicySimpleBcmMibRulesSrcIpMask,'rlPolicySimpleBcmMibRulesDstIp':rlPolicySimpleBcmMibRulesDstIp,'rlPolicySimpleBcmMibRulesDstIpMask':rlPolicySimpleBcmMibRulesDstIpMask,'rlPolicySimpleBcmMibRulesSrcPort':rlPolicySimpleBcmMibRulesSrcPort,'rlPolicySimpleBcmMibRulesDstPort':rlPolicySimpleBcmMibRulesDstPort,'rlPolicySimpleBcmMibRulesInIfIndexList':rlPolicySimpleBcmMibRulesInIfIndexList,'rlPolicySimpleBcmMibRulesOutIfIndexList':rlPolicySimpleBcmMibRulesOutIfIndexList,'rlPolicySimpleBcmMibRulesAction':rlPolicySimpleBcmMibRulesAction,'rlPolicySimpleBcmMibRulesProfilePointer':rlPolicySimpleBcmMibRulesProfilePointer,'rlPolicySimpleBcmMibRulesBitsUsed':rlPolicySimpleBcmMibRulesBitsUsed,'rlPolicySimpleBcmMibRulesStatus':rlPolicySimpleBcmMibRulesStatus,'rlBcmRateLimit':rlBcmRateLimit,'rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown':rlBcmPacketRateLimitBroadcstMulticastUnicastUnknown,'rlBcmPacketRateLimitMulticastEnable':rlBcmPacketRateLimitMulticastEnable,'rlBcmPacketRateLimitBroadcstEnable':rlBcmPacketRateLimitBroadcstEnable,'rlBcmPacketRateLimitUnicastUnknownEnable':rlBcmPacketRateLimitUnicastUnknownEnable,'rlBcmQoSRateLimit':rlBcmQoSRateLimit,'rlBcmQoSRateLimitIndexCounter':rlBcmQoSRateLimitIndexCounter,'rlBcmQoSRateLimitTable':rlBcmQoSRateLimitTable,'rlBcmQoSRateLimitEntry':rlBcmQoSRateLimitEntry,_Q:rlBcmQoSRateLimitType,_R:rlBcmQoSRateLimitName,_S:rlBcmQoSRateLimitIndex,'rlBcmQoSRateLimitAclsNameOrFlow':rlBcmQoSRateLimitAclsNameOrFlow,'rlBcmQoSRateLimitPortsOrInterfaces':rlBcmQoSRateLimitPortsOrInterfaces,'rlBcmQoSRateLimitRatePriority':rlBcmQoSRateLimitRatePriority,'rlBcmQoSRateLimitBurstSizeTosMask':rlBcmQoSRateLimitBurstSizeTosMask,'rlBcmQoSRateLimitDropOutProfile':rlBcmQoSRateLimitDropOutProfile,'rlBcmQoSRateLimitNewTos':rlBcmQoSRateLimitNewTos,'rlBcmQoSRateLimitNewTosPrecedence':rlBcmQoSRateLimitNewTosPrecedence,'rlBcmQoSRateLimitStatus':rlBcmQoSRateLimitStatus,'rlBcmQoSRateLimitAclApplliedTable':rlBcmQoSRateLimitAclApplliedTable,'rlBcmQoSRateLimitAclApplliedEntry':rlBcmQoSRateLimitAclApplliedEntry,_T:rlBcmQoSRateLimitAclName,_U:rlBcmQoSRateLimitAclApplliedIfIndex,'rlBcmQoSRateLimitAclApplliedType':rlBcmQoSRateLimitAclApplliedType,'rlBcmQoSRateLimitAclApplliedStatus':rlBcmQoSRateLimitAclApplliedStatus,'rlBcmQoSRateLimitIPflowTable':rlBcmQoSRateLimitIPflowTable,'rlBcmQoSRateLimitIPflowEntry':rlBcmQoSRateLimitIPflowEntry,_V:rlBcmQoSRateLimitIPflowTos,_W:rlBcmQoSRateLimitIPflowTosMask,_X:rlBcmQoSRateLimitIPflowProtocol,_Y:rlBcmQoSRateLimitIPflowSrcIp,_Z:rlBcmQoSRateLimitIPflowSrcIpMask,_a:rlBcmQoSRateLimitIPflowDstIp,_b:rlBcmQoSRateLimitIPflowDstIpMask,_c:rlBcmQoSRateLimitIPflowSrcPort,_d:rlBcmQoSRateLimitIPflowDstPort,_e:rlBcmQoSRateLimitInIfindex,_f:rlBcmQoSRateLimitOutIfindex,'rlBcmQoSRateLimitIPFlowType':rlBcmQoSRateLimitIPFlowType,'rlBcmQoSRateLimitIPFlowRule':rlBcmQoSRateLimitIPFlowRule,'rlBcmQoSRateLimitIPflowStatus':rlBcmQoSRateLimitIPflowStatus,'rlBcmQoSRateLimitQoSprecedenceMap':rlBcmQoSRateLimitQoSprecedenceMap,'rlTosOverwriteMapMib':rlTosOverwriteMapMib,'rlTosOverwriteMapTable':rlTosOverwriteMapTable,'rlTosOverwriteMapEntry':rlTosOverwriteMapEntry,_g:rlTosOverwriteMapName,_h:rlTosOverwriteMapRange,'rlTosOverwriteMapMapping':rlTosOverwriteMapMapping,'rlTosOverwriteMapPortList':rlTosOverwriteMapPortList,'rlTosOverwriteMapStatus':rlTosOverwriteMapStatus,'rlBcmACLMib':rlBcmACLMib,'rlBcmACLMibVersion':rlBcmACLMibVersion,'rlBcmACLMaxNumberOfEntries':rlBcmACLMaxNumberOfEntries,'rlBcmACLNamesTable':rlBcmACLNamesTable,'rlBcmACLNamesEntry':rlBcmACLNamesEntry,_i:rlBcmACLNamesName,'rlBcmACLNamesID':rlBcmACLNamesID,'rlBcmACLNamesStatus':rlBcmACLNamesStatus,'rlBcmACLTable':rlBcmACLTable,'rlBcmACLEntry':rlBcmACLEntry,_j:rlBcmAclID,_k:rlBcmAclRowIndex,'rlBcmAclAction':rlBcmAclAction,'rlBcmAclIPflags':rlBcmAclIPflags,'rlBcmAclIPflagsMask':rlBcmAclIPflagsMask,'rlBcmAclIPfragOffset':rlBcmAclIPfragOffset,'rlBcmAclIPfragOffsetMask':rlBcmAclIPfragOffsetMask,'rlBcmAclIPprotocol':rlBcmAclIPprotocol,'rlBcmAclSrcIp':rlBcmAclSrcIp,'rlBcmAclSrcIpMask':rlBcmAclSrcIpMask,'rlBcmAclDstIp':rlBcmAclDstIp,'rlBcmAclDstIpMask':rlBcmAclDstIpMask,'rlBcmAclSrcL4Port':rlBcmAclSrcL4Port,'rlBcmAclDstL4Port':rlBcmAclDstL4Port,'rlBcmAclTCPbits':rlBcmAclTCPbits,'rlBcmAclTCPbitsMask':rlBcmAclTCPbitsMask,'rlBcmAclStatus':rlBcmAclStatus,'rlBcmACLPortsTable':rlBcmACLPortsTable,'rlBcmACLPortsEntry':rlBcmACLPortsEntry,_l:rlBcmAclPortsIfIndex,_m:rlBcmAclPortsDirection,'rlBcmAclPortsAclID':rlBcmAclPortsAclID,'rlBcmAclPortsStatus':rlBcmAclPortsStatus})