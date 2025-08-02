_I='aclRuleIndex'
_H='aclIfDirection'
_G='aclIfIndex'
_F='not-accessible'
_E='aclIndex'
_D='Integer32'
_C='GSM7324-QOS-ACL-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gsm7324QOS,=mibBuilder.importSymbols('GSM7324-QOS-MIB','gsm7324QOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
gsm7324QOSACL=ModuleIdentity((1,3,6,1,4,1,4526,1,7,3,2))
if mibBuilder.loadTexts:gsm7324QOSACL.setRevisions(('2003-05-06 12:00',))
_AclTable_Object=MibTable
aclTable=_AclTable_Object((1,3,6,1,4,1,4526,1,7,3,2,1))
if mibBuilder.loadTexts:aclTable.setStatus(_A)
_AclEntry_Object=MibTableRow
aclEntry=_AclEntry_Object((1,3,6,1,4,1,4526,1,7,3,2,1,1))
aclEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:aclEntry.setStatus(_A)
_AclIndex_Type=Integer32
_AclIndex_Object=MibTableColumn
aclIndex=_AclIndex_Object((1,3,6,1,4,1,4526,1,7,3,2,1,1,1),_AclIndex_Type())
aclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:aclIndex.setStatus(_A)
_AclStatus_Type=RowStatus
_AclStatus_Object=MibTableColumn
aclStatus=_AclStatus_Object((1,3,6,1,4,1,4526,1,7,3,2,1,1,3),_AclStatus_Type())
aclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclStatus.setStatus(_A)
_AclIfTable_Object=MibTable
aclIfTable=_AclIfTable_Object((1,3,6,1,4,1,4526,1,7,3,2,2))
if mibBuilder.loadTexts:aclIfTable.setStatus(_A)
_AclIfEntry_Object=MibTableRow
aclIfEntry=_AclIfEntry_Object((1,3,6,1,4,1,4526,1,7,3,2,2,1))
aclIfEntry.setIndexNames((0,_C,_E),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:aclIfEntry.setStatus(_A)
_AclIfIndex_Type=Integer32
_AclIfIndex_Object=MibTableColumn
aclIfIndex=_AclIfIndex_Object((1,3,6,1,4,1,4526,1,7,3,2,2,1,1),_AclIfIndex_Type())
aclIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:aclIfIndex.setStatus(_A)
class _AclIfDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_AclIfDirection_Type.__name__=_D
_AclIfDirection_Object=MibTableColumn
aclIfDirection=_AclIfDirection_Object((1,3,6,1,4,1,4526,1,7,3,2,2,1,2),_AclIfDirection_Type())
aclIfDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:aclIfDirection.setStatus(_A)
_AclIfStatus_Type=RowStatus
_AclIfStatus_Object=MibTableColumn
aclIfStatus=_AclIfStatus_Object((1,3,6,1,4,1,4526,1,7,3,2,2,1,3),_AclIfStatus_Type())
aclIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclIfStatus.setStatus(_A)
_AclRuleTable_Object=MibTable
aclRuleTable=_AclRuleTable_Object((1,3,6,1,4,1,4526,1,7,3,2,3))
if mibBuilder.loadTexts:aclRuleTable.setStatus(_A)
_AclRuleEntry_Object=MibTableRow
aclRuleEntry=_AclRuleEntry_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1))
aclRuleEntry.setIndexNames((0,_C,_E),(0,_C,_I))
if mibBuilder.loadTexts:aclRuleEntry.setStatus(_A)
_AclRuleIndex_Type=Integer32
_AclRuleIndex_Object=MibTableColumn
aclRuleIndex=_AclRuleIndex_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,1),_AclRuleIndex_Type())
aclRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:aclRuleIndex.setStatus(_A)
class _AclRuleAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_AclRuleAction_Type.__name__=_D
_AclRuleAction_Object=MibTableColumn
aclRuleAction=_AclRuleAction_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,2),_AclRuleAction_Type())
aclRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleAction.setStatus(_A)
class _AclRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclRuleProtocol_Type.__name__=_D
_AclRuleProtocol_Object=MibTableColumn
aclRuleProtocol=_AclRuleProtocol_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,3),_AclRuleProtocol_Type())
aclRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleProtocol.setStatus(_A)
_AclRuleSrcIpAddress_Type=IpAddress
_AclRuleSrcIpAddress_Object=MibTableColumn
aclRuleSrcIpAddress=_AclRuleSrcIpAddress_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,4),_AclRuleSrcIpAddress_Type())
aclRuleSrcIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcIpAddress.setStatus(_A)
_AclRuleSrcIpMask_Type=IpAddress
_AclRuleSrcIpMask_Object=MibTableColumn
aclRuleSrcIpMask=_AclRuleSrcIpMask_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,5),_AclRuleSrcIpMask_Type())
aclRuleSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcIpMask.setStatus(_A)
_AclRuleSrcL4Port_Type=Integer32
_AclRuleSrcL4Port_Object=MibTableColumn
aclRuleSrcL4Port=_AclRuleSrcL4Port_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,6),_AclRuleSrcL4Port_Type())
aclRuleSrcL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4Port.setStatus(_A)
_AclRuleSrcL4PortRangeStart_Type=Integer32
_AclRuleSrcL4PortRangeStart_Object=MibTableColumn
aclRuleSrcL4PortRangeStart=_AclRuleSrcL4PortRangeStart_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,7),_AclRuleSrcL4PortRangeStart_Type())
aclRuleSrcL4PortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4PortRangeStart.setStatus(_A)
_AclRuleSrcL4PortRangeEnd_Type=Integer32
_AclRuleSrcL4PortRangeEnd_Object=MibTableColumn
aclRuleSrcL4PortRangeEnd=_AclRuleSrcL4PortRangeEnd_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,8),_AclRuleSrcL4PortRangeEnd_Type())
aclRuleSrcL4PortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4PortRangeEnd.setStatus(_A)
_AclRuleDestIpAddress_Type=IpAddress
_AclRuleDestIpAddress_Object=MibTableColumn
aclRuleDestIpAddress=_AclRuleDestIpAddress_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,9),_AclRuleDestIpAddress_Type())
aclRuleDestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestIpAddress.setStatus(_A)
_AclRuleDestIpMask_Type=IpAddress
_AclRuleDestIpMask_Object=MibTableColumn
aclRuleDestIpMask=_AclRuleDestIpMask_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,10),_AclRuleDestIpMask_Type())
aclRuleDestIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestIpMask.setStatus(_A)
_AclRuleDestL4Port_Type=Integer32
_AclRuleDestL4Port_Object=MibTableColumn
aclRuleDestL4Port=_AclRuleDestL4Port_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,11),_AclRuleDestL4Port_Type())
aclRuleDestL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4Port.setStatus(_A)
_AclRuleDestL4PortRangeStart_Type=Integer32
_AclRuleDestL4PortRangeStart_Object=MibTableColumn
aclRuleDestL4PortRangeStart=_AclRuleDestL4PortRangeStart_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,12),_AclRuleDestL4PortRangeStart_Type())
aclRuleDestL4PortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4PortRangeStart.setStatus(_A)
_AclRuleDestL4PortRangeEnd_Type=Integer32
_AclRuleDestL4PortRangeEnd_Object=MibTableColumn
aclRuleDestL4PortRangeEnd=_AclRuleDestL4PortRangeEnd_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,13),_AclRuleDestL4PortRangeEnd_Type())
aclRuleDestL4PortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4PortRangeEnd.setStatus(_A)
_AclRuleIPDSCP_Type=Integer32
_AclRuleIPDSCP_Object=MibTableColumn
aclRuleIPDSCP=_AclRuleIPDSCP_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,14),_AclRuleIPDSCP_Type())
aclRuleIPDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIPDSCP.setStatus(_A)
_AclRuleIpPrecedence_Type=Integer32
_AclRuleIpPrecedence_Object=MibTableColumn
aclRuleIpPrecedence=_AclRuleIpPrecedence_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,15),_AclRuleIpPrecedence_Type())
aclRuleIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpPrecedence.setStatus(_A)
_AclRuleIpTosBits_Type=Integer32
_AclRuleIpTosBits_Object=MibTableColumn
aclRuleIpTosBits=_AclRuleIpTosBits_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,16),_AclRuleIpTosBits_Type())
aclRuleIpTosBits.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpTosBits.setStatus(_A)
_AclRuleIpTosMask_Type=Integer32
_AclRuleIpTosMask_Object=MibTableColumn
aclRuleIpTosMask=_AclRuleIpTosMask_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,17),_AclRuleIpTosMask_Type())
aclRuleIpTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpTosMask.setStatus(_A)
_AclRuleStatus_Type=RowStatus
_AclRuleStatus_Object=MibTableColumn
aclRuleStatus=_AclRuleStatus_Object((1,3,6,1,4,1,4526,1,7,3,2,3,1,18),_AclRuleStatus_Type())
aclRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'gsm7324QOSACL':gsm7324QOSACL,'aclTable':aclTable,'aclEntry':aclEntry,_E:aclIndex,'aclStatus':aclStatus,'aclIfTable':aclIfTable,'aclIfEntry':aclIfEntry,_G:aclIfIndex,_H:aclIfDirection,'aclIfStatus':aclIfStatus,'aclRuleTable':aclRuleTable,'aclRuleEntry':aclRuleEntry,_I:aclRuleIndex,'aclRuleAction':aclRuleAction,'aclRuleProtocol':aclRuleProtocol,'aclRuleSrcIpAddress':aclRuleSrcIpAddress,'aclRuleSrcIpMask':aclRuleSrcIpMask,'aclRuleSrcL4Port':aclRuleSrcL4Port,'aclRuleSrcL4PortRangeStart':aclRuleSrcL4PortRangeStart,'aclRuleSrcL4PortRangeEnd':aclRuleSrcL4PortRangeEnd,'aclRuleDestIpAddress':aclRuleDestIpAddress,'aclRuleDestIpMask':aclRuleDestIpMask,'aclRuleDestL4Port':aclRuleDestL4Port,'aclRuleDestL4PortRangeStart':aclRuleDestL4PortRangeStart,'aclRuleDestL4PortRangeEnd':aclRuleDestL4PortRangeEnd,'aclRuleIPDSCP':aclRuleIPDSCP,'aclRuleIpPrecedence':aclRuleIpPrecedence,'aclRuleIpTosBits':aclRuleIpTosBits,'aclRuleIpTosMask':aclRuleIpTosMask,'aclRuleStatus':aclRuleStatus})