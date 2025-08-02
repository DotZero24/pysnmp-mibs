_V='tpAclCounterNum'
_U='tpPktCntntRuleId'
_T='tpPktCntntAclId'
_S='tpIPv6RuleId'
_R='tpIPv6AclId'
_Q='tpCombRuleId'
_P='tpCombAclId'
_O='tpIpRuleId'
_N='tpIpAclId'
_M='tpMacRuleId'
_L='tpMacAclId'
_K='tpAclCounterRuleId'
_J='tpAclCounterAclId'
_I='deny'
_H='permit'
_G='enable'
_F='disable'
_E='Integer32'
_D='read-only'
_C='TPLINK-ACL-RULE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkAclMIBObjects,=mibBuilder.importSymbols('TPLINK-ACL-MIB','tplinkAclMIBObjects')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
_TpAclRuleConfigure_ObjectIdentity=ObjectIdentity
tpAclRuleConfigure=_TpAclRuleConfigure_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,1))
_TpMacRuleTable_Object=MibTable
tpMacRuleTable=_TpMacRuleTable_Object((1,3,6,1,4,1,11863,6,26,1,1,1))
if mibBuilder.loadTexts:tpMacRuleTable.setStatus(_A)
_TpMacRuleEntry_Object=MibTableRow
tpMacRuleEntry=_TpMacRuleEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1))
tpMacRuleEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:tpMacRuleEntry.setStatus(_A)
_TpMacAclId_Type=Integer32
_TpMacAclId_Object=MibTableColumn
tpMacAclId=_TpMacAclId_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,1),_TpMacAclId_Type())
tpMacAclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMacAclId.setStatus(_A)
_TpMacRuleId_Type=Integer32
_TpMacRuleId_Object=MibTableColumn
tpMacRuleId=_TpMacRuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,2),_TpMacRuleId_Type())
tpMacRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMacRuleId.setStatus(_A)
_TpMacAclName_Type=OctetString
_TpMacAclName_Object=MibTableColumn
tpMacAclName=_TpMacAclName_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,3),_TpMacAclName_Type())
tpMacAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacAclName.setStatus(_A)
class _TpMacSecOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpMacSecOperation_Type.__name__=_E
_TpMacSecOperation_Object=MibTableColumn
tpMacSecOperation=_TpMacSecOperation_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,4),_TpMacSecOperation_Type())
tpMacSecOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacSecOperation.setStatus(_A)
class _TpMacCounterLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpMacCounterLogging_Type.__name__=_E
_TpMacCounterLogging_Object=MibTableColumn
tpMacCounterLogging=_TpMacCounterLogging_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,5),_TpMacCounterLogging_Type())
tpMacCounterLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacCounterLogging.setStatus(_A)
_TpMacSmacAddress_Type=OctetString
_TpMacSmacAddress_Object=MibTableColumn
tpMacSmacAddress=_TpMacSmacAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,6),_TpMacSmacAddress_Type())
tpMacSmacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacSmacAddress.setStatus(_A)
_TpMacSmacMask_Type=OctetString
_TpMacSmacMask_Object=MibTableColumn
tpMacSmacMask=_TpMacSmacMask_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,7),_TpMacSmacMask_Type())
tpMacSmacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacSmacMask.setStatus(_A)
_TpMacDmacAddress_Type=OctetString
_TpMacDmacAddress_Object=MibTableColumn
tpMacDmacAddress=_TpMacDmacAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,8),_TpMacDmacAddress_Type())
tpMacDmacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacDmacAddress.setStatus(_A)
_TpMacDmacMask_Type=OctetString
_TpMacDmacMask_Object=MibTableColumn
tpMacDmacMask=_TpMacDmacMask_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,9),_TpMacDmacMask_Type())
tpMacDmacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacDmacMask.setStatus(_A)
_TpMacVlanId_Type=Integer32
_TpMacVlanId_Object=MibTableColumn
tpMacVlanId=_TpMacVlanId_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,10),_TpMacVlanId_Type())
tpMacVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacVlanId.setStatus(_A)
_TpMacEtherType_Type=Integer32
_TpMacEtherType_Object=MibTableColumn
tpMacEtherType=_TpMacEtherType_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,11),_TpMacEtherType_Type())
tpMacEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacEtherType.setStatus(_A)
_TpMacPri_Type=Integer32
_TpMacPri_Object=MibTableColumn
tpMacPri=_TpMacPri_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,12),_TpMacPri_Type())
tpMacPri.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacPri.setStatus(_A)
_TpMacTimeSegment_Type=OctetString
_TpMacTimeSegment_Object=MibTableColumn
tpMacTimeSegment=_TpMacTimeSegment_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,13),_TpMacTimeSegment_Type())
tpMacTimeSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacTimeSegment.setStatus(_A)
_TpMacRuleStatus_Type=TPRowStatus
_TpMacRuleStatus_Object=MibTableColumn
tpMacRuleStatus=_TpMacRuleStatus_Object((1,3,6,1,4,1,11863,6,26,1,1,1,1,14),_TpMacRuleStatus_Type())
tpMacRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpMacRuleStatus.setStatus(_A)
_TpIpRuleTable_Object=MibTable
tpIpRuleTable=_TpIpRuleTable_Object((1,3,6,1,4,1,11863,6,26,1,1,2))
if mibBuilder.loadTexts:tpIpRuleTable.setStatus(_A)
_TpIpRuleEntry_Object=MibTableRow
tpIpRuleEntry=_TpIpRuleEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1))
tpIpRuleEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:tpIpRuleEntry.setStatus(_A)
_TpIpAclId_Type=Integer32
_TpIpAclId_Object=MibTableColumn
tpIpAclId=_TpIpAclId_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,1),_TpIpAclId_Type())
tpIpAclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIpAclId.setStatus(_A)
_TpIpRuleId_Type=Integer32
_TpIpRuleId_Object=MibTableColumn
tpIpRuleId=_TpIpRuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,2),_TpIpRuleId_Type())
tpIpRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIpRuleId.setStatus(_A)
_TpIpAclName_Type=OctetString
_TpIpAclName_Object=MibTableColumn
tpIpAclName=_TpIpAclName_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,3),_TpIpAclName_Type())
tpIpAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpAclName.setStatus(_A)
class _TpIpSecOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpIpSecOperation_Type.__name__=_E
_TpIpSecOperation_Object=MibTableColumn
tpIpSecOperation=_TpIpSecOperation_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,4),_TpIpSecOperation_Type())
tpIpSecOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpSecOperation.setStatus(_A)
class _TpIpCounterLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIpCounterLogging_Type.__name__=_E
_TpIpCounterLogging_Object=MibTableColumn
tpIpCounterLogging=_TpIpCounterLogging_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,5),_TpIpCounterLogging_Type())
tpIpCounterLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpCounterLogging.setStatus(_A)
class _TpIpFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIpFragment_Type.__name__=_E
_TpIpFragment_Object=MibTableColumn
tpIpFragment=_TpIpFragment_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,6),_TpIpFragment_Type())
tpIpFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpFragment.setStatus(_A)
_TpIpSipAddress_Type=IpAddress
_TpIpSipAddress_Object=MibTableColumn
tpIpSipAddress=_TpIpSipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,7),_TpIpSipAddress_Type())
tpIpSipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpSipAddress.setStatus(_A)
_TpIpSipMask_Type=IpAddress
_TpIpSipMask_Object=MibTableColumn
tpIpSipMask=_TpIpSipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,8),_TpIpSipMask_Type())
tpIpSipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpSipMask.setStatus(_A)
_TpIpDipAddress_Type=IpAddress
_TpIpDipAddress_Object=MibTableColumn
tpIpDipAddress=_TpIpDipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,9),_TpIpDipAddress_Type())
tpIpDipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpDipAddress.setStatus(_A)
_TpIpDipMask_Type=IpAddress
_TpIpDipMask_Object=MibTableColumn
tpIpDipMask=_TpIpDipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,10),_TpIpDipMask_Type())
tpIpDipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpDipMask.setStatus(_A)
_TpIpProtocol_Type=Integer32
_TpIpProtocol_Object=MibTableColumn
tpIpProtocol=_TpIpProtocol_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,11),_TpIpProtocol_Type())
tpIpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpProtocol.setStatus(_A)
_TpIpTcpFlag_Type=Integer32
_TpIpTcpFlag_Object=MibTableColumn
tpIpTcpFlag=_TpIpTcpFlag_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,12),_TpIpTcpFlag_Type())
tpIpTcpFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpTcpFlag.setStatus(_A)
_TpIpSourcePort_Type=Integer32
_TpIpSourcePort_Object=MibTableColumn
tpIpSourcePort=_TpIpSourcePort_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,13),_TpIpSourcePort_Type())
tpIpSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpSourcePort.setStatus(_A)
_TpIpSourcePortMask_Type=OctetString
_TpIpSourcePortMask_Object=MibTableColumn
tpIpSourcePortMask=_TpIpSourcePortMask_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,14),_TpIpSourcePortMask_Type())
tpIpSourcePortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpSourcePortMask.setStatus(_A)
_TpIpDestPort_Type=Integer32
_TpIpDestPort_Object=MibTableColumn
tpIpDestPort=_TpIpDestPort_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,15),_TpIpDestPort_Type())
tpIpDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpDestPort.setStatus(_A)
_TpIpDestPortMask_Type=OctetString
_TpIpDestPortMask_Object=MibTableColumn
tpIpDestPortMask=_TpIpDestPortMask_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,16),_TpIpDestPortMask_Type())
tpIpDestPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpDestPortMask.setStatus(_A)
_TpIpDscp_Type=Integer32
_TpIpDscp_Object=MibTableColumn
tpIpDscp=_TpIpDscp_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,17),_TpIpDscp_Type())
tpIpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpDscp.setStatus(_A)
_TpIpTos_Type=Integer32
_TpIpTos_Object=MibTableColumn
tpIpTos=_TpIpTos_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,18),_TpIpTos_Type())
tpIpTos.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpTos.setStatus(_A)
_TpIpPre_Type=Integer32
_TpIpPre_Object=MibTableColumn
tpIpPre=_TpIpPre_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,19),_TpIpPre_Type())
tpIpPre.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpPre.setStatus(_A)
_TpIpTimeSegment_Type=OctetString
_TpIpTimeSegment_Object=MibTableColumn
tpIpTimeSegment=_TpIpTimeSegment_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,20),_TpIpTimeSegment_Type())
tpIpTimeSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpTimeSegment.setStatus(_A)
_TpIpRuleStatus_Type=TPRowStatus
_TpIpRuleStatus_Object=MibTableColumn
tpIpRuleStatus=_TpIpRuleStatus_Object((1,3,6,1,4,1,11863,6,26,1,1,2,1,21),_TpIpRuleStatus_Type())
tpIpRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIpRuleStatus.setStatus(_A)
_TpCombRuleTable_Object=MibTable
tpCombRuleTable=_TpCombRuleTable_Object((1,3,6,1,4,1,11863,6,26,1,1,3))
if mibBuilder.loadTexts:tpCombRuleTable.setStatus(_A)
_TpCombRuleEntry_Object=MibTableRow
tpCombRuleEntry=_TpCombRuleEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1))
tpCombRuleEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:tpCombRuleEntry.setStatus(_A)
_TpCombAclId_Type=Integer32
_TpCombAclId_Object=MibTableColumn
tpCombAclId=_TpCombAclId_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,1),_TpCombAclId_Type())
tpCombAclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpCombAclId.setStatus(_A)
_TpCombRuleId_Type=Integer32
_TpCombRuleId_Object=MibTableColumn
tpCombRuleId=_TpCombRuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,2),_TpCombRuleId_Type())
tpCombRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpCombRuleId.setStatus(_A)
_TpCombAclName_Type=OctetString
_TpCombAclName_Object=MibTableColumn
tpCombAclName=_TpCombAclName_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,3),_TpCombAclName_Type())
tpCombAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombAclName.setStatus(_A)
class _TpCombSecOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpCombSecOperation_Type.__name__=_E
_TpCombSecOperation_Object=MibTableColumn
tpCombSecOperation=_TpCombSecOperation_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,4),_TpCombSecOperation_Type())
tpCombSecOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSecOperation.setStatus(_A)
class _TpCombCounterLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpCombCounterLogging_Type.__name__=_E
_TpCombCounterLogging_Object=MibTableColumn
tpCombCounterLogging=_TpCombCounterLogging_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,5),_TpCombCounterLogging_Type())
tpCombCounterLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombCounterLogging.setStatus(_A)
_TpCombSmacAddress_Type=OctetString
_TpCombSmacAddress_Object=MibTableColumn
tpCombSmacAddress=_TpCombSmacAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,6),_TpCombSmacAddress_Type())
tpCombSmacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSmacAddress.setStatus(_A)
_TpCombSmacMask_Type=OctetString
_TpCombSmacMask_Object=MibTableColumn
tpCombSmacMask=_TpCombSmacMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,7),_TpCombSmacMask_Type())
tpCombSmacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSmacMask.setStatus(_A)
_TpCombDmacAddress_Type=OctetString
_TpCombDmacAddress_Object=MibTableColumn
tpCombDmacAddress=_TpCombDmacAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,8),_TpCombDmacAddress_Type())
tpCombDmacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDmacAddress.setStatus(_A)
_TpCombDmacMask_Type=OctetString
_TpCombDmacMask_Object=MibTableColumn
tpCombDmacMask=_TpCombDmacMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,9),_TpCombDmacMask_Type())
tpCombDmacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDmacMask.setStatus(_A)
_TpCombVlanId_Type=Integer32
_TpCombVlanId_Object=MibTableColumn
tpCombVlanId=_TpCombVlanId_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,10),_TpCombVlanId_Type())
tpCombVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombVlanId.setStatus(_A)
_TpCombEtherType_Type=Integer32
_TpCombEtherType_Object=MibTableColumn
tpCombEtherType=_TpCombEtherType_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,11),_TpCombEtherType_Type())
tpCombEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombEtherType.setStatus(_A)
_TpCombPri_Type=Integer32
_TpCombPri_Object=MibTableColumn
tpCombPri=_TpCombPri_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,12),_TpCombPri_Type())
tpCombPri.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombPri.setStatus(_A)
_TpCombSipAddress_Type=IpAddress
_TpCombSipAddress_Object=MibTableColumn
tpCombSipAddress=_TpCombSipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,13),_TpCombSipAddress_Type())
tpCombSipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSipAddress.setStatus(_A)
_TpCombSipMask_Type=IpAddress
_TpCombSipMask_Object=MibTableColumn
tpCombSipMask=_TpCombSipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,14),_TpCombSipMask_Type())
tpCombSipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSipMask.setStatus(_A)
_TpCombDipAddress_Type=IpAddress
_TpCombDipAddress_Object=MibTableColumn
tpCombDipAddress=_TpCombDipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,15),_TpCombDipAddress_Type())
tpCombDipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDipAddress.setStatus(_A)
_TpCombDipMask_Type=IpAddress
_TpCombDipMask_Object=MibTableColumn
tpCombDipMask=_TpCombDipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,16),_TpCombDipMask_Type())
tpCombDipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDipMask.setStatus(_A)
_TpCombDscp_Type=Integer32
_TpCombDscp_Object=MibTableColumn
tpCombDscp=_TpCombDscp_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,17),_TpCombDscp_Type())
tpCombDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDscp.setStatus(_A)
_TpCombTos_Type=Integer32
_TpCombTos_Object=MibTableColumn
tpCombTos=_TpCombTos_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,18),_TpCombTos_Type())
tpCombTos.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombTos.setStatus(_A)
_TpCombPre_Type=Integer32
_TpCombPre_Object=MibTableColumn
tpCombPre=_TpCombPre_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,19),_TpCombPre_Type())
tpCombPre.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombPre.setStatus(_A)
class _TpCombFragment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpCombFragment_Type.__name__=_E
_TpCombFragment_Object=MibTableColumn
tpCombFragment=_TpCombFragment_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,20),_TpCombFragment_Type())
tpCombFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombFragment.setStatus(_A)
_TpCombProtocol_Type=Integer32
_TpCombProtocol_Object=MibTableColumn
tpCombProtocol=_TpCombProtocol_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,21),_TpCombProtocol_Type())
tpCombProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombProtocol.setStatus(_A)
_TpCombSourcePort_Type=Integer32
_TpCombSourcePort_Object=MibTableColumn
tpCombSourcePort=_TpCombSourcePort_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,22),_TpCombSourcePort_Type())
tpCombSourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSourcePort.setStatus(_A)
_TpCombSourcePortMask_Type=OctetString
_TpCombSourcePortMask_Object=MibTableColumn
tpCombSourcePortMask=_TpCombSourcePortMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,23),_TpCombSourcePortMask_Type())
tpCombSourcePortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombSourcePortMask.setStatus(_A)
_TpCombDestPort_Type=Integer32
_TpCombDestPort_Object=MibTableColumn
tpCombDestPort=_TpCombDestPort_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,24),_TpCombDestPort_Type())
tpCombDestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDestPort.setStatus(_A)
_TpCombDestPortMask_Type=OctetString
_TpCombDestPortMask_Object=MibTableColumn
tpCombDestPortMask=_TpCombDestPortMask_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,25),_TpCombDestPortMask_Type())
tpCombDestPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombDestPortMask.setStatus(_A)
_TpCombTcpFlag_Type=Integer32
_TpCombTcpFlag_Object=MibTableColumn
tpCombTcpFlag=_TpCombTcpFlag_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,26),_TpCombTcpFlag_Type())
tpCombTcpFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombTcpFlag.setStatus(_A)
_TpCombTimeSegment_Type=OctetString
_TpCombTimeSegment_Object=MibTableColumn
tpCombTimeSegment=_TpCombTimeSegment_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,27),_TpCombTimeSegment_Type())
tpCombTimeSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombTimeSegment.setStatus(_A)
_TpCombRuleStatus_Type=TPRowStatus
_TpCombRuleStatus_Object=MibTableColumn
tpCombRuleStatus=_TpCombRuleStatus_Object((1,3,6,1,4,1,11863,6,26,1,1,3,1,28),_TpCombRuleStatus_Type())
tpCombRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpCombRuleStatus.setStatus(_A)
_TpIPv6RuleTable_Object=MibTable
tpIPv6RuleTable=_TpIPv6RuleTable_Object((1,3,6,1,4,1,11863,6,26,1,1,4))
if mibBuilder.loadTexts:tpIPv6RuleTable.setStatus(_A)
_TpIPv6RuleEntry_Object=MibTableRow
tpIPv6RuleEntry=_TpIPv6RuleEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1))
tpIPv6RuleEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:tpIPv6RuleEntry.setStatus(_A)
_TpIPv6AclId_Type=Integer32
_TpIPv6AclId_Object=MibTableColumn
tpIPv6AclId=_TpIPv6AclId_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,1),_TpIPv6AclId_Type())
tpIPv6AclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIPv6AclId.setStatus(_A)
_TpIPv6RuleId_Type=Integer32
_TpIPv6RuleId_Object=MibTableColumn
tpIPv6RuleId=_TpIPv6RuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,2),_TpIPv6RuleId_Type())
tpIPv6RuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpIPv6RuleId.setStatus(_A)
_TpIPv6AclName_Type=OctetString
_TpIPv6AclName_Object=MibTableColumn
tpIPv6AclName=_TpIPv6AclName_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,3),_TpIPv6AclName_Type())
tpIPv6AclName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6AclName.setStatus(_A)
class _TpIPv6SecOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpIPv6SecOperation_Type.__name__=_E
_TpIPv6SecOperation_Object=MibTableColumn
tpIPv6SecOperation=_TpIPv6SecOperation_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,4),_TpIPv6SecOperation_Type())
tpIPv6SecOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6SecOperation.setStatus(_A)
class _TpIPv6CounterLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpIPv6CounterLogging_Type.__name__=_E
_TpIPv6CounterLogging_Object=MibTableColumn
tpIPv6CounterLogging=_TpIPv6CounterLogging_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,5),_TpIPv6CounterLogging_Type())
tpIPv6CounterLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6CounterLogging.setStatus(_A)
_TpIPv6TrafficClass_Type=Integer32
_TpIPv6TrafficClass_Object=MibTableColumn
tpIPv6TrafficClass=_TpIPv6TrafficClass_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,6),_TpIPv6TrafficClass_Type())
tpIPv6TrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6TrafficClass.setStatus(_A)
_TpIPv6FlowLabel_Type=Integer32
_TpIPv6FlowLabel_Object=MibTableColumn
tpIPv6FlowLabel=_TpIPv6FlowLabel_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,7),_TpIPv6FlowLabel_Type())
tpIPv6FlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6FlowLabel.setStatus(_A)
_TpIPv6SipAddress_Type=OctetString
_TpIPv6SipAddress_Object=MibTableColumn
tpIPv6SipAddress=_TpIPv6SipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,8),_TpIPv6SipAddress_Type())
tpIPv6SipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6SipAddress.setStatus(_A)
_TpIPv6SipMask_Type=OctetString
_TpIPv6SipMask_Object=MibTableColumn
tpIPv6SipMask=_TpIPv6SipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,9),_TpIPv6SipMask_Type())
tpIPv6SipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6SipMask.setStatus(_A)
_TpIPv6DipAddress_Type=OctetString
_TpIPv6DipAddress_Object=MibTableColumn
tpIPv6DipAddress=_TpIPv6DipAddress_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,10),_TpIPv6DipAddress_Type())
tpIPv6DipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6DipAddress.setStatus(_A)
_TpIPv6DipMask_Type=OctetString
_TpIPv6DipMask_Object=MibTableColumn
tpIPv6DipMask=_TpIPv6DipMask_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,11),_TpIPv6DipMask_Type())
tpIPv6DipMask.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6DipMask.setStatus(_A)
_TpIPv6Protocol_Type=Integer32
_TpIPv6Protocol_Object=MibTableColumn
tpIPv6Protocol=_TpIPv6Protocol_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,12),_TpIPv6Protocol_Type())
tpIPv6Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6Protocol.setStatus(_A)
_TpIPv6SourcePort_Type=Integer32
_TpIPv6SourcePort_Object=MibTableColumn
tpIPv6SourcePort=_TpIPv6SourcePort_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,13),_TpIPv6SourcePort_Type())
tpIPv6SourcePort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6SourcePort.setStatus(_A)
_TpIPv6DestPort_Type=Integer32
_TpIPv6DestPort_Object=MibTableColumn
tpIPv6DestPort=_TpIPv6DestPort_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,14),_TpIPv6DestPort_Type())
tpIPv6DestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6DestPort.setStatus(_A)
_TpIPv6TimeSegment_Type=OctetString
_TpIPv6TimeSegment_Object=MibTableColumn
tpIPv6TimeSegment=_TpIPv6TimeSegment_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,15),_TpIPv6TimeSegment_Type())
tpIPv6TimeSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6TimeSegment.setStatus(_A)
_TpIPv6RuleStatus_Type=TPRowStatus
_TpIPv6RuleStatus_Object=MibTableColumn
tpIPv6RuleStatus=_TpIPv6RuleStatus_Object((1,3,6,1,4,1,11863,6,26,1,1,4,1,16),_TpIPv6RuleStatus_Type())
tpIPv6RuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpIPv6RuleStatus.setStatus(_A)
_TpPktCntntOffsetProfile_ObjectIdentity=ObjectIdentity
tpPktCntntOffsetProfile=_TpPktCntntOffsetProfile_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,1,5))
_TpPktCntntOffset0_Type=Integer32
_TpPktCntntOffset0_Object=MibScalar
tpPktCntntOffset0=_TpPktCntntOffset0_Object((1,3,6,1,4,1,11863,6,26,1,1,5,1),_TpPktCntntOffset0_Type())
tpPktCntntOffset0.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntOffset0.setStatus(_A)
_TpPktCntntOffset1_Type=Integer32
_TpPktCntntOffset1_Object=MibScalar
tpPktCntntOffset1=_TpPktCntntOffset1_Object((1,3,6,1,4,1,11863,6,26,1,1,5,2),_TpPktCntntOffset1_Type())
tpPktCntntOffset1.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntOffset1.setStatus(_A)
_TpPktCntntOffset2_Type=Integer32
_TpPktCntntOffset2_Object=MibScalar
tpPktCntntOffset2=_TpPktCntntOffset2_Object((1,3,6,1,4,1,11863,6,26,1,1,5,3),_TpPktCntntOffset2_Type())
tpPktCntntOffset2.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntOffset2.setStatus(_A)
_TpPktCntntOffset3_Type=Integer32
_TpPktCntntOffset3_Object=MibScalar
tpPktCntntOffset3=_TpPktCntntOffset3_Object((1,3,6,1,4,1,11863,6,26,1,1,5,4),_TpPktCntntOffset3_Type())
tpPktCntntOffset3.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntOffset3.setStatus(_A)
_TpPktCntntRuleTable_Object=MibTable
tpPktCntntRuleTable=_TpPktCntntRuleTable_Object((1,3,6,1,4,1,11863,6,26,1,1,6))
if mibBuilder.loadTexts:tpPktCntntRuleTable.setStatus(_A)
_TpPktCntntRuleEntry_Object=MibTableRow
tpPktCntntRuleEntry=_TpPktCntntRuleEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1))
tpPktCntntRuleEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:tpPktCntntRuleEntry.setStatus(_A)
_TpPktCntntAclId_Type=Integer32
_TpPktCntntAclId_Object=MibTableColumn
tpPktCntntAclId=_TpPktCntntAclId_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,1),_TpPktCntntAclId_Type())
tpPktCntntAclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPktCntntAclId.setStatus(_A)
_TpPktCntntRuleId_Type=Integer32
_TpPktCntntRuleId_Object=MibTableColumn
tpPktCntntRuleId=_TpPktCntntRuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,2),_TpPktCntntRuleId_Type())
tpPktCntntRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpPktCntntRuleId.setStatus(_A)
_TpPktCntntAclName_Type=OctetString
_TpPktCntntAclName_Object=MibTableColumn
tpPktCntntAclName=_TpPktCntntAclName_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,3),_TpPktCntntAclName_Type())
tpPktCntntAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntAclName.setStatus(_A)
class _TpPktCntntSecOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_TpPktCntntSecOperation_Type.__name__=_E
_TpPktCntntSecOperation_Object=MibTableColumn
tpPktCntntSecOperation=_TpPktCntntSecOperation_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,4),_TpPktCntntSecOperation_Type())
tpPktCntntSecOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntSecOperation.setStatus(_A)
class _TpPktCntntCounterLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpPktCntntCounterLogging_Type.__name__=_E
_TpPktCntntCounterLogging_Object=MibTableColumn
tpPktCntntCounterLogging=_TpPktCntntCounterLogging_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,5),_TpPktCntntCounterLogging_Type())
tpPktCntntCounterLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntCounterLogging.setStatus(_A)
_TpPktCntntChunkValue0_Type=OctetString
_TpPktCntntChunkValue0_Object=MibTableColumn
tpPktCntntChunkValue0=_TpPktCntntChunkValue0_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,6),_TpPktCntntChunkValue0_Type())
tpPktCntntChunkValue0.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkValue0.setStatus(_A)
_TpPktCntntChunkMask0_Type=OctetString
_TpPktCntntChunkMask0_Object=MibTableColumn
tpPktCntntChunkMask0=_TpPktCntntChunkMask0_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,7),_TpPktCntntChunkMask0_Type())
tpPktCntntChunkMask0.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkMask0.setStatus(_A)
_TpPktCntntChunkValue1_Type=OctetString
_TpPktCntntChunkValue1_Object=MibTableColumn
tpPktCntntChunkValue1=_TpPktCntntChunkValue1_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,8),_TpPktCntntChunkValue1_Type())
tpPktCntntChunkValue1.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkValue1.setStatus(_A)
_TpPktCntntChunkMask1_Type=OctetString
_TpPktCntntChunkMask1_Object=MibTableColumn
tpPktCntntChunkMask1=_TpPktCntntChunkMask1_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,9),_TpPktCntntChunkMask1_Type())
tpPktCntntChunkMask1.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkMask1.setStatus(_A)
_TpPktCntntChunkValue2_Type=OctetString
_TpPktCntntChunkValue2_Object=MibTableColumn
tpPktCntntChunkValue2=_TpPktCntntChunkValue2_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,10),_TpPktCntntChunkValue2_Type())
tpPktCntntChunkValue2.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkValue2.setStatus(_A)
_TpPktCntntChunkMask2_Type=OctetString
_TpPktCntntChunkMask2_Object=MibTableColumn
tpPktCntntChunkMask2=_TpPktCntntChunkMask2_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,11),_TpPktCntntChunkMask2_Type())
tpPktCntntChunkMask2.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkMask2.setStatus(_A)
_TpPktCntntChunkValue3_Type=OctetString
_TpPktCntntChunkValue3_Object=MibTableColumn
tpPktCntntChunkValue3=_TpPktCntntChunkValue3_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,12),_TpPktCntntChunkValue3_Type())
tpPktCntntChunkValue3.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkValue3.setStatus(_A)
_TpPktCntntChunkMask3_Type=OctetString
_TpPktCntntChunkMask3_Object=MibTableColumn
tpPktCntntChunkMask3=_TpPktCntntChunkMask3_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,13),_TpPktCntntChunkMask3_Type())
tpPktCntntChunkMask3.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntChunkMask3.setStatus(_A)
_TpPktCntntTimeSegment_Type=OctetString
_TpPktCntntTimeSegment_Object=MibTableColumn
tpPktCntntTimeSegment=_TpPktCntntTimeSegment_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,14),_TpPktCntntTimeSegment_Type())
tpPktCntntTimeSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntTimeSegment.setStatus(_A)
_TpPktCntntRuleStatus_Type=TPRowStatus
_TpPktCntntRuleStatus_Object=MibTableColumn
tpPktCntntRuleStatus=_TpPktCntntRuleStatus_Object((1,3,6,1,4,1,11863,6,26,1,1,6,1,15),_TpPktCntntRuleStatus_Type())
tpPktCntntRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPktCntntRuleStatus.setStatus(_A)
_TpAclRuleCounterTable_Object=MibTable
tpAclRuleCounterTable=_TpAclRuleCounterTable_Object((1,3,6,1,4,1,11863,6,26,1,1,7))
if mibBuilder.loadTexts:tpAclRuleCounterTable.setStatus(_A)
_TpAclRuleCounterEntry_Object=MibTableRow
tpAclRuleCounterEntry=_TpAclRuleCounterEntry_Object((1,3,6,1,4,1,11863,6,26,1,1,7,1))
tpAclRuleCounterEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:tpAclRuleCounterEntry.setStatus(_A)
_TpAclCounterAclId_Type=Integer32
_TpAclCounterAclId_Object=MibTableColumn
tpAclCounterAclId=_TpAclCounterAclId_Object((1,3,6,1,4,1,11863,6,26,1,1,7,1,1),_TpAclCounterAclId_Type())
tpAclCounterAclId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAclCounterAclId.setStatus(_A)
_TpAclCounterRuleId_Type=Integer32
_TpAclCounterRuleId_Object=MibTableColumn
tpAclCounterRuleId=_TpAclCounterRuleId_Object((1,3,6,1,4,1,11863,6,26,1,1,7,1,2),_TpAclCounterRuleId_Type())
tpAclCounterRuleId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAclCounterRuleId.setStatus(_A)
_TpAclCounterLoggingEnable_Type=Integer32
_TpAclCounterLoggingEnable_Object=MibTableColumn
tpAclCounterLoggingEnable=_TpAclCounterLoggingEnable_Object((1,3,6,1,4,1,11863,6,26,1,1,7,1,3),_TpAclCounterLoggingEnable_Type())
tpAclCounterLoggingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAclCounterLoggingEnable.setStatus(_A)
_TpAclCounterNum_Type=Integer32
_TpAclCounterNum_Object=MibTableColumn
tpAclCounterNum=_TpAclCounterNum_Object((1,3,6,1,4,1,11863,6,26,1,1,7,1,4),_TpAclCounterNum_Type())
tpAclCounterNum.setMaxAccess(_D)
if mibBuilder.loadTexts:tpAclCounterNum.setStatus(_A)
_TplinkAclNotifications_ObjectIdentity=ObjectIdentity
tplinkAclNotifications=_TplinkAclNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,26,1,2))
tpAclLoggingCounter=NotificationType((1,3,6,1,4,1,11863,6,26,1,2,1))
tpAclLoggingCounter.setObjects(*((_C,_J),(_C,_K),(_C,_V)))
if mibBuilder.loadTexts:tpAclLoggingCounter.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tpAclRuleConfigure':tpAclRuleConfigure,'tpMacRuleTable':tpMacRuleTable,'tpMacRuleEntry':tpMacRuleEntry,_L:tpMacAclId,_M:tpMacRuleId,'tpMacAclName':tpMacAclName,'tpMacSecOperation':tpMacSecOperation,'tpMacCounterLogging':tpMacCounterLogging,'tpMacSmacAddress':tpMacSmacAddress,'tpMacSmacMask':tpMacSmacMask,'tpMacDmacAddress':tpMacDmacAddress,'tpMacDmacMask':tpMacDmacMask,'tpMacVlanId':tpMacVlanId,'tpMacEtherType':tpMacEtherType,'tpMacPri':tpMacPri,'tpMacTimeSegment':tpMacTimeSegment,'tpMacRuleStatus':tpMacRuleStatus,'tpIpRuleTable':tpIpRuleTable,'tpIpRuleEntry':tpIpRuleEntry,_N:tpIpAclId,_O:tpIpRuleId,'tpIpAclName':tpIpAclName,'tpIpSecOperation':tpIpSecOperation,'tpIpCounterLogging':tpIpCounterLogging,'tpIpFragment':tpIpFragment,'tpIpSipAddress':tpIpSipAddress,'tpIpSipMask':tpIpSipMask,'tpIpDipAddress':tpIpDipAddress,'tpIpDipMask':tpIpDipMask,'tpIpProtocol':tpIpProtocol,'tpIpTcpFlag':tpIpTcpFlag,'tpIpSourcePort':tpIpSourcePort,'tpIpSourcePortMask':tpIpSourcePortMask,'tpIpDestPort':tpIpDestPort,'tpIpDestPortMask':tpIpDestPortMask,'tpIpDscp':tpIpDscp,'tpIpTos':tpIpTos,'tpIpPre':tpIpPre,'tpIpTimeSegment':tpIpTimeSegment,'tpIpRuleStatus':tpIpRuleStatus,'tpCombRuleTable':tpCombRuleTable,'tpCombRuleEntry':tpCombRuleEntry,_P:tpCombAclId,_Q:tpCombRuleId,'tpCombAclName':tpCombAclName,'tpCombSecOperation':tpCombSecOperation,'tpCombCounterLogging':tpCombCounterLogging,'tpCombSmacAddress':tpCombSmacAddress,'tpCombSmacMask':tpCombSmacMask,'tpCombDmacAddress':tpCombDmacAddress,'tpCombDmacMask':tpCombDmacMask,'tpCombVlanId':tpCombVlanId,'tpCombEtherType':tpCombEtherType,'tpCombPri':tpCombPri,'tpCombSipAddress':tpCombSipAddress,'tpCombSipMask':tpCombSipMask,'tpCombDipAddress':tpCombDipAddress,'tpCombDipMask':tpCombDipMask,'tpCombDscp':tpCombDscp,'tpCombTos':tpCombTos,'tpCombPre':tpCombPre,'tpCombFragment':tpCombFragment,'tpCombProtocol':tpCombProtocol,'tpCombSourcePort':tpCombSourcePort,'tpCombSourcePortMask':tpCombSourcePortMask,'tpCombDestPort':tpCombDestPort,'tpCombDestPortMask':tpCombDestPortMask,'tpCombTcpFlag':tpCombTcpFlag,'tpCombTimeSegment':tpCombTimeSegment,'tpCombRuleStatus':tpCombRuleStatus,'tpIPv6RuleTable':tpIPv6RuleTable,'tpIPv6RuleEntry':tpIPv6RuleEntry,_R:tpIPv6AclId,_S:tpIPv6RuleId,'tpIPv6AclName':tpIPv6AclName,'tpIPv6SecOperation':tpIPv6SecOperation,'tpIPv6CounterLogging':tpIPv6CounterLogging,'tpIPv6TrafficClass':tpIPv6TrafficClass,'tpIPv6FlowLabel':tpIPv6FlowLabel,'tpIPv6SipAddress':tpIPv6SipAddress,'tpIPv6SipMask':tpIPv6SipMask,'tpIPv6DipAddress':tpIPv6DipAddress,'tpIPv6DipMask':tpIPv6DipMask,'tpIPv6Protocol':tpIPv6Protocol,'tpIPv6SourcePort':tpIPv6SourcePort,'tpIPv6DestPort':tpIPv6DestPort,'tpIPv6TimeSegment':tpIPv6TimeSegment,'tpIPv6RuleStatus':tpIPv6RuleStatus,'tpPktCntntOffsetProfile':tpPktCntntOffsetProfile,'tpPktCntntOffset0':tpPktCntntOffset0,'tpPktCntntOffset1':tpPktCntntOffset1,'tpPktCntntOffset2':tpPktCntntOffset2,'tpPktCntntOffset3':tpPktCntntOffset3,'tpPktCntntRuleTable':tpPktCntntRuleTable,'tpPktCntntRuleEntry':tpPktCntntRuleEntry,_T:tpPktCntntAclId,_U:tpPktCntntRuleId,'tpPktCntntAclName':tpPktCntntAclName,'tpPktCntntSecOperation':tpPktCntntSecOperation,'tpPktCntntCounterLogging':tpPktCntntCounterLogging,'tpPktCntntChunkValue0':tpPktCntntChunkValue0,'tpPktCntntChunkMask0':tpPktCntntChunkMask0,'tpPktCntntChunkValue1':tpPktCntntChunkValue1,'tpPktCntntChunkMask1':tpPktCntntChunkMask1,'tpPktCntntChunkValue2':tpPktCntntChunkValue2,'tpPktCntntChunkMask2':tpPktCntntChunkMask2,'tpPktCntntChunkValue3':tpPktCntntChunkValue3,'tpPktCntntChunkMask3':tpPktCntntChunkMask3,'tpPktCntntTimeSegment':tpPktCntntTimeSegment,'tpPktCntntRuleStatus':tpPktCntntRuleStatus,'tpAclRuleCounterTable':tpAclRuleCounterTable,'tpAclRuleCounterEntry':tpAclRuleCounterEntry,_J:tpAclCounterAclId,_K:tpAclCounterRuleId,'tpAclCounterLoggingEnable':tpAclCounterLoggingEnable,_V:tpAclCounterNum,'tplinkAclNotifications':tplinkAclNotifications,'tpAclLoggingCounter':tpAclLoggingCounter})