_b='hmAgentCosQueueIndex'
_a='taildrop'
_Z='hmAgentCosMapIntfTrustIntfIndex'
_Y='hmAgentCosMapIpDscpValue'
_X='hmAgentCosMapIpDscpIntfIndex'
_W='hmAgentCosMapIpPrecValue'
_V='hmAgentCosMapIpPrecIntfIndex'
_U='aclIfAclId'
_T='aclIfAclType'
_S='aclIfSequence'
_R='aclIfDirection'
_Q='aclIfIndex'
_P='aclMacRuleIndex'
_O='permit'
_N='aclRuleIndex'
_M='DisplayString'
_L='hmAgentCosQueueIntfIndex'
_K='aclMacIndex'
_J='aclIndex'
_I='InterfaceIndexOrZero'
_H='read-only'
_G='read-write'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='HIRSCHMANN-MMP4-QOS-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmPlatform4,=mibBuilder.importSymbols('HIRSCHMANN-MMP4-BASICL2-MIB','hmPlatform4')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hmPlatform4QOS=ModuleIdentity((1,3,6,1,4,1,248,15,3))
if mibBuilder.loadTexts:hmPlatform4QOS.setRevisions(('2005-08-18 12:00',))
class EtypeValue(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
class PercentByFives(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,5),ValueRangeConstraint(10,10),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20),ValueRangeConstraint(25,25),ValueRangeConstraint(30,30),ValueRangeConstraint(35,35),ValueRangeConstraint(40,40),ValueRangeConstraint(45,45),ValueRangeConstraint(50,50),ValueRangeConstraint(55,55),ValueRangeConstraint(60,60),ValueRangeConstraint(65,65),ValueRangeConstraint(70,70),ValueRangeConstraint(75,75),ValueRangeConstraint(80,80),ValueRangeConstraint(85,85),ValueRangeConstraint(90,90),ValueRangeConstraint(95,95),ValueRangeConstraint(100,100))
class Sixteenths(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_HmAgentQOSACL_ObjectIdentity=ObjectIdentity
hmAgentQOSACL=_HmAgentQOSACL_ObjectIdentity((1,3,6,1,4,1,248,15,3,2))
_AclTable_Object=MibTable
aclTable=_AclTable_Object((1,3,6,1,4,1,248,15,3,2,1))
if mibBuilder.loadTexts:aclTable.setStatus(_A)
_AclEntry_Object=MibTableRow
aclEntry=_AclEntry_Object((1,3,6,1,4,1,248,15,3,2,1,1))
aclEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:aclEntry.setStatus(_A)
_AclIndex_Type=Integer32
_AclIndex_Object=MibTableColumn
aclIndex=_AclIndex_Object((1,3,6,1,4,1,248,15,3,2,1,1,1),_AclIndex_Type())
aclIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIndex.setStatus(_A)
_AclStatus_Type=RowStatus
_AclStatus_Object=MibTableColumn
aclStatus=_AclStatus_Object((1,3,6,1,4,1,248,15,3,2,1,1,3),_AclStatus_Type())
aclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclStatus.setStatus(_A)
_AclRuleTable_Object=MibTable
aclRuleTable=_AclRuleTable_Object((1,3,6,1,4,1,248,15,3,2,4))
if mibBuilder.loadTexts:aclRuleTable.setStatus(_A)
_AclRuleEntry_Object=MibTableRow
aclRuleEntry=_AclRuleEntry_Object((1,3,6,1,4,1,248,15,3,2,4,1))
aclRuleEntry.setIndexNames((0,_C,_J),(0,_C,_N))
if mibBuilder.loadTexts:aclRuleEntry.setStatus(_A)
_AclRuleIndex_Type=Integer32
_AclRuleIndex_Object=MibTableColumn
aclRuleIndex=_AclRuleIndex_Object((1,3,6,1,4,1,248,15,3,2,4,1,1),_AclRuleIndex_Type())
aclRuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aclRuleIndex.setStatus(_A)
class _AclRuleAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('deny',2)))
_AclRuleAction_Type.__name__=_F
_AclRuleAction_Object=MibTableColumn
aclRuleAction=_AclRuleAction_Object((1,3,6,1,4,1,248,15,3,2,4,1,2),_AclRuleAction_Type())
aclRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleAction.setStatus(_A)
class _AclRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AclRuleProtocol_Type.__name__=_F
_AclRuleProtocol_Object=MibTableColumn
aclRuleProtocol=_AclRuleProtocol_Object((1,3,6,1,4,1,248,15,3,2,4,1,3),_AclRuleProtocol_Type())
aclRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleProtocol.setStatus(_A)
_AclRuleSrcIpAddress_Type=IpAddress
_AclRuleSrcIpAddress_Object=MibTableColumn
aclRuleSrcIpAddress=_AclRuleSrcIpAddress_Object((1,3,6,1,4,1,248,15,3,2,4,1,4),_AclRuleSrcIpAddress_Type())
aclRuleSrcIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcIpAddress.setStatus(_A)
_AclRuleSrcIpMask_Type=IpAddress
_AclRuleSrcIpMask_Object=MibTableColumn
aclRuleSrcIpMask=_AclRuleSrcIpMask_Object((1,3,6,1,4,1,248,15,3,2,4,1,5),_AclRuleSrcIpMask_Type())
aclRuleSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcIpMask.setStatus(_A)
_AclRuleSrcL4Port_Type=Integer32
_AclRuleSrcL4Port_Object=MibTableColumn
aclRuleSrcL4Port=_AclRuleSrcL4Port_Object((1,3,6,1,4,1,248,15,3,2,4,1,6),_AclRuleSrcL4Port_Type())
aclRuleSrcL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4Port.setStatus(_A)
_AclRuleSrcL4PortRangeStart_Type=Integer32
_AclRuleSrcL4PortRangeStart_Object=MibTableColumn
aclRuleSrcL4PortRangeStart=_AclRuleSrcL4PortRangeStart_Object((1,3,6,1,4,1,248,15,3,2,4,1,7),_AclRuleSrcL4PortRangeStart_Type())
aclRuleSrcL4PortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4PortRangeStart.setStatus(_A)
_AclRuleSrcL4PortRangeEnd_Type=Integer32
_AclRuleSrcL4PortRangeEnd_Object=MibTableColumn
aclRuleSrcL4PortRangeEnd=_AclRuleSrcL4PortRangeEnd_Object((1,3,6,1,4,1,248,15,3,2,4,1,8),_AclRuleSrcL4PortRangeEnd_Type())
aclRuleSrcL4PortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleSrcL4PortRangeEnd.setStatus(_A)
_AclRuleDestIpAddress_Type=IpAddress
_AclRuleDestIpAddress_Object=MibTableColumn
aclRuleDestIpAddress=_AclRuleDestIpAddress_Object((1,3,6,1,4,1,248,15,3,2,4,1,9),_AclRuleDestIpAddress_Type())
aclRuleDestIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestIpAddress.setStatus(_A)
_AclRuleDestIpMask_Type=IpAddress
_AclRuleDestIpMask_Object=MibTableColumn
aclRuleDestIpMask=_AclRuleDestIpMask_Object((1,3,6,1,4,1,248,15,3,2,4,1,10),_AclRuleDestIpMask_Type())
aclRuleDestIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestIpMask.setStatus(_A)
_AclRuleDestL4Port_Type=Integer32
_AclRuleDestL4Port_Object=MibTableColumn
aclRuleDestL4Port=_AclRuleDestL4Port_Object((1,3,6,1,4,1,248,15,3,2,4,1,11),_AclRuleDestL4Port_Type())
aclRuleDestL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4Port.setStatus(_A)
_AclRuleDestL4PortRangeStart_Type=Integer32
_AclRuleDestL4PortRangeStart_Object=MibTableColumn
aclRuleDestL4PortRangeStart=_AclRuleDestL4PortRangeStart_Object((1,3,6,1,4,1,248,15,3,2,4,1,12),_AclRuleDestL4PortRangeStart_Type())
aclRuleDestL4PortRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4PortRangeStart.setStatus(_A)
_AclRuleDestL4PortRangeEnd_Type=Integer32
_AclRuleDestL4PortRangeEnd_Object=MibTableColumn
aclRuleDestL4PortRangeEnd=_AclRuleDestL4PortRangeEnd_Object((1,3,6,1,4,1,248,15,3,2,4,1,13),_AclRuleDestL4PortRangeEnd_Type())
aclRuleDestL4PortRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleDestL4PortRangeEnd.setStatus(_A)
_AclRuleIPDSCP_Type=Integer32
_AclRuleIPDSCP_Object=MibTableColumn
aclRuleIPDSCP=_AclRuleIPDSCP_Object((1,3,6,1,4,1,248,15,3,2,4,1,14),_AclRuleIPDSCP_Type())
aclRuleIPDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIPDSCP.setStatus(_A)
_AclRuleIpPrecedence_Type=Integer32
_AclRuleIpPrecedence_Object=MibTableColumn
aclRuleIpPrecedence=_AclRuleIpPrecedence_Object((1,3,6,1,4,1,248,15,3,2,4,1,15),_AclRuleIpPrecedence_Type())
aclRuleIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpPrecedence.setStatus(_A)
_AclRuleIpTosBits_Type=Integer32
_AclRuleIpTosBits_Object=MibTableColumn
aclRuleIpTosBits=_AclRuleIpTosBits_Object((1,3,6,1,4,1,248,15,3,2,4,1,16),_AclRuleIpTosBits_Type())
aclRuleIpTosBits.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpTosBits.setStatus(_A)
_AclRuleIpTosMask_Type=Integer32
_AclRuleIpTosMask_Object=MibTableColumn
aclRuleIpTosMask=_AclRuleIpTosMask_Object((1,3,6,1,4,1,248,15,3,2,4,1,17),_AclRuleIpTosMask_Type())
aclRuleIpTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleIpTosMask.setStatus(_A)
_AclRuleStatus_Type=RowStatus
_AclRuleStatus_Object=MibTableColumn
aclRuleStatus=_AclRuleStatus_Object((1,3,6,1,4,1,248,15,3,2,4,1,18),_AclRuleStatus_Type())
aclRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleStatus.setStatus(_A)
_AclRuleAssignQueueId_Type=Unsigned32
_AclRuleAssignQueueId_Object=MibTableColumn
aclRuleAssignQueueId=_AclRuleAssignQueueId_Object((1,3,6,1,4,1,248,15,3,2,4,1,19),_AclRuleAssignQueueId_Type())
aclRuleAssignQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleAssignQueueId.setStatus(_A)
class _AclRuleRedirectIntf_Type(InterfaceIndexOrZero):defaultValue=0
_AclRuleRedirectIntf_Type.__name__=_I
_AclRuleRedirectIntf_Object=MibTableColumn
aclRuleRedirectIntf=_AclRuleRedirectIntf_Object((1,3,6,1,4,1,248,15,3,2,4,1,20),_AclRuleRedirectIntf_Type())
aclRuleRedirectIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleRedirectIntf.setStatus(_A)
_AclRuleMatchEvery_Type=TruthValue
_AclRuleMatchEvery_Object=MibTableColumn
aclRuleMatchEvery=_AclRuleMatchEvery_Object((1,3,6,1,4,1,248,15,3,2,4,1,21),_AclRuleMatchEvery_Type())
aclRuleMatchEvery.setMaxAccess(_B)
if mibBuilder.loadTexts:aclRuleMatchEvery.setStatus(_A)
_AclMacIndexNextFree_Type=Integer32
_AclMacIndexNextFree_Object=MibScalar
aclMacIndexNextFree=_AclMacIndexNextFree_Object((1,3,6,1,4,1,248,15,3,2,5),_AclMacIndexNextFree_Type())
aclMacIndexNextFree.setMaxAccess(_H)
if mibBuilder.loadTexts:aclMacIndexNextFree.setStatus(_A)
_AclMacTable_Object=MibTable
aclMacTable=_AclMacTable_Object((1,3,6,1,4,1,248,15,3,2,6))
if mibBuilder.loadTexts:aclMacTable.setStatus(_A)
_AclMacEntry_Object=MibTableRow
aclMacEntry=_AclMacEntry_Object((1,3,6,1,4,1,248,15,3,2,6,1))
aclMacEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:aclMacEntry.setStatus(_A)
_AclMacIndex_Type=Integer32
_AclMacIndex_Object=MibTableColumn
aclMacIndex=_AclMacIndex_Object((1,3,6,1,4,1,248,15,3,2,6,1,1),_AclMacIndex_Type())
aclMacIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aclMacIndex.setStatus(_A)
class _AclMacName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AclMacName_Type.__name__=_M
_AclMacName_Object=MibTableColumn
aclMacName=_AclMacName_Object((1,3,6,1,4,1,248,15,3,2,6,1,2),_AclMacName_Type())
aclMacName.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacName.setStatus(_A)
_AclMacStatus_Type=RowStatus
_AclMacStatus_Object=MibTableColumn
aclMacStatus=_AclMacStatus_Object((1,3,6,1,4,1,248,15,3,2,6,1,3),_AclMacStatus_Type())
aclMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacStatus.setStatus(_A)
_AclMacRuleTable_Object=MibTable
aclMacRuleTable=_AclMacRuleTable_Object((1,3,6,1,4,1,248,15,3,2,7))
if mibBuilder.loadTexts:aclMacRuleTable.setStatus(_A)
_AclMacRuleEntry_Object=MibTableRow
aclMacRuleEntry=_AclMacRuleEntry_Object((1,3,6,1,4,1,248,15,3,2,7,1))
aclMacRuleEntry.setIndexNames((0,_C,_K),(0,_C,_P))
if mibBuilder.loadTexts:aclMacRuleEntry.setStatus(_A)
_AclMacRuleIndex_Type=Integer32
_AclMacRuleIndex_Object=MibTableColumn
aclMacRuleIndex=_AclMacRuleIndex_Object((1,3,6,1,4,1,248,15,3,2,7,1,1),_AclMacRuleIndex_Type())
aclMacRuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aclMacRuleIndex.setStatus(_A)
class _AclMacRuleAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('deny',2)))
_AclMacRuleAction_Type.__name__=_F
_AclMacRuleAction_Object=MibTableColumn
aclMacRuleAction=_AclMacRuleAction_Object((1,3,6,1,4,1,248,15,3,2,7,1,2),_AclMacRuleAction_Type())
aclMacRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleAction.setStatus(_A)
class _AclMacRuleCos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclMacRuleCos_Type.__name__=_D
_AclMacRuleCos_Object=MibTableColumn
aclMacRuleCos=_AclMacRuleCos_Object((1,3,6,1,4,1,248,15,3,2,7,1,3),_AclMacRuleCos_Type())
aclMacRuleCos.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleCos.setStatus(_A)
class _AclMacRuleCos2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclMacRuleCos2_Type.__name__=_D
_AclMacRuleCos2_Object=MibTableColumn
aclMacRuleCos2=_AclMacRuleCos2_Object((1,3,6,1,4,1,248,15,3,2,7,1,4),_AclMacRuleCos2_Type())
aclMacRuleCos2.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleCos2.setStatus(_A)
_AclMacRuleDestMacAddr_Type=MacAddress
_AclMacRuleDestMacAddr_Object=MibTableColumn
aclMacRuleDestMacAddr=_AclMacRuleDestMacAddr_Object((1,3,6,1,4,1,248,15,3,2,7,1,5),_AclMacRuleDestMacAddr_Type())
aclMacRuleDestMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleDestMacAddr.setStatus(_A)
_AclMacRuleDestMacMask_Type=MacAddress
_AclMacRuleDestMacMask_Object=MibTableColumn
aclMacRuleDestMacMask=_AclMacRuleDestMacMask_Object((1,3,6,1,4,1,248,15,3,2,7,1,6),_AclMacRuleDestMacMask_Type())
aclMacRuleDestMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleDestMacMask.setStatus(_A)
class _AclMacRuleEtypeKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('custom',1),('appletalk',2),('arp',3),('ibmsna',4),('ipv4',5),('ipv6',6),('ipx',7),('mplsmcast',8),('mplsucast',9),('netbios',10),('novell',11),('pppoe',12),('rarp',13)))
_AclMacRuleEtypeKey_Type.__name__=_F
_AclMacRuleEtypeKey_Object=MibTableColumn
aclMacRuleEtypeKey=_AclMacRuleEtypeKey_Object((1,3,6,1,4,1,248,15,3,2,7,1,7),_AclMacRuleEtypeKey_Type())
aclMacRuleEtypeKey.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleEtypeKey.setStatus(_A)
_AclMacRuleEtypeValue_Type=EtypeValue
_AclMacRuleEtypeValue_Object=MibTableColumn
aclMacRuleEtypeValue=_AclMacRuleEtypeValue_Object((1,3,6,1,4,1,248,15,3,2,7,1,8),_AclMacRuleEtypeValue_Type())
aclMacRuleEtypeValue.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleEtypeValue.setStatus(_A)
_AclMacRuleSrcMacAddr_Type=MacAddress
_AclMacRuleSrcMacAddr_Object=MibTableColumn
aclMacRuleSrcMacAddr=_AclMacRuleSrcMacAddr_Object((1,3,6,1,4,1,248,15,3,2,7,1,9),_AclMacRuleSrcMacAddr_Type())
aclMacRuleSrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleSrcMacAddr.setStatus(_A)
_AclMacRuleSrcMacMask_Type=MacAddress
_AclMacRuleSrcMacMask_Object=MibTableColumn
aclMacRuleSrcMacMask=_AclMacRuleSrcMacMask_Object((1,3,6,1,4,1,248,15,3,2,7,1,10),_AclMacRuleSrcMacMask_Type())
aclMacRuleSrcMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleSrcMacMask.setStatus(_A)
class _AclMacRuleVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanId_Type.__name__=_D
_AclMacRuleVlanId_Object=MibTableColumn
aclMacRuleVlanId=_AclMacRuleVlanId_Object((1,3,6,1,4,1,248,15,3,2,7,1,11),_AclMacRuleVlanId_Type())
aclMacRuleVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanId.setStatus(_A)
class _AclMacRuleVlanIdRangeStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanIdRangeStart_Type.__name__=_D
_AclMacRuleVlanIdRangeStart_Object=MibTableColumn
aclMacRuleVlanIdRangeStart=_AclMacRuleVlanIdRangeStart_Object((1,3,6,1,4,1,248,15,3,2,7,1,12),_AclMacRuleVlanIdRangeStart_Type())
aclMacRuleVlanIdRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanIdRangeStart.setStatus(_A)
class _AclMacRuleVlanIdRangeEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanIdRangeEnd_Type.__name__=_D
_AclMacRuleVlanIdRangeEnd_Object=MibTableColumn
aclMacRuleVlanIdRangeEnd=_AclMacRuleVlanIdRangeEnd_Object((1,3,6,1,4,1,248,15,3,2,7,1,13),_AclMacRuleVlanIdRangeEnd_Type())
aclMacRuleVlanIdRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanIdRangeEnd.setStatus(_A)
class _AclMacRuleVlanId2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanId2_Type.__name__=_D
_AclMacRuleVlanId2_Object=MibTableColumn
aclMacRuleVlanId2=_AclMacRuleVlanId2_Object((1,3,6,1,4,1,248,15,3,2,7,1,14),_AclMacRuleVlanId2_Type())
aclMacRuleVlanId2.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanId2.setStatus(_A)
class _AclMacRuleVlanId2RangeStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanId2RangeStart_Type.__name__=_D
_AclMacRuleVlanId2RangeStart_Object=MibTableColumn
aclMacRuleVlanId2RangeStart=_AclMacRuleVlanId2RangeStart_Object((1,3,6,1,4,1,248,15,3,2,7,1,15),_AclMacRuleVlanId2RangeStart_Type())
aclMacRuleVlanId2RangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanId2RangeStart.setStatus(_A)
class _AclMacRuleVlanId2RangeEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AclMacRuleVlanId2RangeEnd_Type.__name__=_D
_AclMacRuleVlanId2RangeEnd_Object=MibTableColumn
aclMacRuleVlanId2RangeEnd=_AclMacRuleVlanId2RangeEnd_Object((1,3,6,1,4,1,248,15,3,2,7,1,16),_AclMacRuleVlanId2RangeEnd_Type())
aclMacRuleVlanId2RangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleVlanId2RangeEnd.setStatus(_A)
_AclMacRuleStatus_Type=RowStatus
_AclMacRuleStatus_Object=MibTableColumn
aclMacRuleStatus=_AclMacRuleStatus_Object((1,3,6,1,4,1,248,15,3,2,7,1,17),_AclMacRuleStatus_Type())
aclMacRuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleStatus.setStatus(_A)
_AclMacRuleAssignQueueId_Type=Unsigned32
_AclMacRuleAssignQueueId_Object=MibTableColumn
aclMacRuleAssignQueueId=_AclMacRuleAssignQueueId_Object((1,3,6,1,4,1,248,15,3,2,7,1,18),_AclMacRuleAssignQueueId_Type())
aclMacRuleAssignQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleAssignQueueId.setStatus(_A)
class _AclMacRuleRedirectIntf_Type(InterfaceIndexOrZero):defaultValue=0
_AclMacRuleRedirectIntf_Type.__name__=_I
_AclMacRuleRedirectIntf_Object=MibTableColumn
aclMacRuleRedirectIntf=_AclMacRuleRedirectIntf_Object((1,3,6,1,4,1,248,15,3,2,7,1,19),_AclMacRuleRedirectIntf_Type())
aclMacRuleRedirectIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleRedirectIntf.setStatus(_A)
_AclMacRuleMatchEvery_Type=TruthValue
_AclMacRuleMatchEvery_Object=MibTableColumn
aclMacRuleMatchEvery=_AclMacRuleMatchEvery_Object((1,3,6,1,4,1,248,15,3,2,7,1,20),_AclMacRuleMatchEvery_Type())
aclMacRuleMatchEvery.setMaxAccess(_B)
if mibBuilder.loadTexts:aclMacRuleMatchEvery.setStatus(_A)
_AclIfTable_Object=MibTable
aclIfTable=_AclIfTable_Object((1,3,6,1,4,1,248,15,3,2,8))
if mibBuilder.loadTexts:aclIfTable.setStatus(_A)
_AclIfEntry_Object=MibTableRow
aclIfEntry=_AclIfEntry_Object((1,3,6,1,4,1,248,15,3,2,8,1))
aclIfEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:aclIfEntry.setStatus(_A)
_AclIfIndex_Type=Integer32
_AclIfIndex_Object=MibTableColumn
aclIfIndex=_AclIfIndex_Object((1,3,6,1,4,1,248,15,3,2,8,1,1),_AclIfIndex_Type())
aclIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIfIndex.setStatus(_A)
class _AclIfDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_AclIfDirection_Type.__name__=_F
_AclIfDirection_Object=MibTableColumn
aclIfDirection=_AclIfDirection_Object((1,3,6,1,4,1,248,15,3,2,8,1,2),_AclIfDirection_Type())
aclIfDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIfDirection.setStatus(_A)
class _AclIfSequence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AclIfSequence_Type.__name__=_D
_AclIfSequence_Object=MibTableColumn
aclIfSequence=_AclIfSequence_Object((1,3,6,1,4,1,248,15,3,2,8,1,3),_AclIfSequence_Type())
aclIfSequence.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIfSequence.setStatus(_A)
class _AclIfAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('mac',2)))
_AclIfAclType_Type.__name__=_F
_AclIfAclType_Object=MibTableColumn
aclIfAclType=_AclIfAclType_Object((1,3,6,1,4,1,248,15,3,2,8,1,4),_AclIfAclType_Type())
aclIfAclType.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIfAclType.setStatus(_A)
_AclIfAclId_Type=Integer32
_AclIfAclId_Object=MibTableColumn
aclIfAclId=_AclIfAclId_Object((1,3,6,1,4,1,248,15,3,2,8,1,5),_AclIfAclId_Type())
aclIfAclId.setMaxAccess(_E)
if mibBuilder.loadTexts:aclIfAclId.setStatus(_A)
_AclIfStatus_Type=RowStatus
_AclIfStatus_Object=MibTableColumn
aclIfStatus=_AclIfStatus_Object((1,3,6,1,4,1,248,15,3,2,8,1,6),_AclIfStatus_Type())
aclIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclIfStatus.setStatus(_A)
_HmAgentQOSCOS_ObjectIdentity=ObjectIdentity
hmAgentQOSCOS=_HmAgentQOSCOS_ObjectIdentity((1,3,6,1,4,1,248,15,3,3))
_HmAgentCosMapCfgGroup_ObjectIdentity=ObjectIdentity
hmAgentCosMapCfgGroup=_HmAgentCosMapCfgGroup_ObjectIdentity((1,3,6,1,4,1,248,15,3,3,1))
_HmAgentCosMapIpPrecTable_Object=MibTable
hmAgentCosMapIpPrecTable=_HmAgentCosMapIpPrecTable_Object((1,3,6,1,4,1,248,15,3,3,1,1))
if mibBuilder.loadTexts:hmAgentCosMapIpPrecTable.setStatus(_A)
_HmAgentCosMapIpPrecEntry_Object=MibTableRow
hmAgentCosMapIpPrecEntry=_HmAgentCosMapIpPrecEntry_Object((1,3,6,1,4,1,248,15,3,3,1,1,1))
hmAgentCosMapIpPrecEntry.setIndexNames((0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:hmAgentCosMapIpPrecEntry.setStatus(_A)
_HmAgentCosMapIpPrecIntfIndex_Type=InterfaceIndexOrZero
_HmAgentCosMapIpPrecIntfIndex_Object=MibTableColumn
hmAgentCosMapIpPrecIntfIndex=_HmAgentCosMapIpPrecIntfIndex_Object((1,3,6,1,4,1,248,15,3,3,1,1,1,1),_HmAgentCosMapIpPrecIntfIndex_Type())
hmAgentCosMapIpPrecIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosMapIpPrecIntfIndex.setStatus(_A)
class _HmAgentCosMapIpPrecValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HmAgentCosMapIpPrecValue_Type.__name__=_D
_HmAgentCosMapIpPrecValue_Object=MibTableColumn
hmAgentCosMapIpPrecValue=_HmAgentCosMapIpPrecValue_Object((1,3,6,1,4,1,248,15,3,3,1,1,1,2),_HmAgentCosMapIpPrecValue_Type())
hmAgentCosMapIpPrecValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosMapIpPrecValue.setStatus(_A)
class _HmAgentCosMapIpPrecTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HmAgentCosMapIpPrecTrafficClass_Type.__name__=_D
_HmAgentCosMapIpPrecTrafficClass_Object=MibTableColumn
hmAgentCosMapIpPrecTrafficClass=_HmAgentCosMapIpPrecTrafficClass_Object((1,3,6,1,4,1,248,15,3,3,1,1,1,3),_HmAgentCosMapIpPrecTrafficClass_Type())
hmAgentCosMapIpPrecTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosMapIpPrecTrafficClass.setStatus(_A)
_HmAgentCosMapIpDscpTable_Object=MibTable
hmAgentCosMapIpDscpTable=_HmAgentCosMapIpDscpTable_Object((1,3,6,1,4,1,248,15,3,3,1,2))
if mibBuilder.loadTexts:hmAgentCosMapIpDscpTable.setStatus(_A)
_HmAgentCosMapIpDscpEntry_Object=MibTableRow
hmAgentCosMapIpDscpEntry=_HmAgentCosMapIpDscpEntry_Object((1,3,6,1,4,1,248,15,3,3,1,2,1))
hmAgentCosMapIpDscpEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:hmAgentCosMapIpDscpEntry.setStatus(_A)
_HmAgentCosMapIpDscpIntfIndex_Type=InterfaceIndexOrZero
_HmAgentCosMapIpDscpIntfIndex_Object=MibTableColumn
hmAgentCosMapIpDscpIntfIndex=_HmAgentCosMapIpDscpIntfIndex_Object((1,3,6,1,4,1,248,15,3,3,1,2,1,1),_HmAgentCosMapIpDscpIntfIndex_Type())
hmAgentCosMapIpDscpIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosMapIpDscpIntfIndex.setStatus(_A)
class _HmAgentCosMapIpDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HmAgentCosMapIpDscpValue_Type.__name__=_D
_HmAgentCosMapIpDscpValue_Object=MibTableColumn
hmAgentCosMapIpDscpValue=_HmAgentCosMapIpDscpValue_Object((1,3,6,1,4,1,248,15,3,3,1,2,1,2),_HmAgentCosMapIpDscpValue_Type())
hmAgentCosMapIpDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosMapIpDscpValue.setStatus(_A)
class _HmAgentCosMapIpDscpTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HmAgentCosMapIpDscpTrafficClass_Type.__name__=_D
_HmAgentCosMapIpDscpTrafficClass_Object=MibTableColumn
hmAgentCosMapIpDscpTrafficClass=_HmAgentCosMapIpDscpTrafficClass_Object((1,3,6,1,4,1,248,15,3,3,1,2,1,3),_HmAgentCosMapIpDscpTrafficClass_Type())
hmAgentCosMapIpDscpTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosMapIpDscpTrafficClass.setStatus(_A)
_HmAgentCosMapIntfTrustTable_Object=MibTable
hmAgentCosMapIntfTrustTable=_HmAgentCosMapIntfTrustTable_Object((1,3,6,1,4,1,248,15,3,3,1,3))
if mibBuilder.loadTexts:hmAgentCosMapIntfTrustTable.setStatus(_A)
_HmAgentCosMapIntfTrustEntry_Object=MibTableRow
hmAgentCosMapIntfTrustEntry=_HmAgentCosMapIntfTrustEntry_Object((1,3,6,1,4,1,248,15,3,3,1,3,1))
hmAgentCosMapIntfTrustEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:hmAgentCosMapIntfTrustEntry.setStatus(_A)
_HmAgentCosMapIntfTrustIntfIndex_Type=InterfaceIndexOrZero
_HmAgentCosMapIntfTrustIntfIndex_Object=MibTableColumn
hmAgentCosMapIntfTrustIntfIndex=_HmAgentCosMapIntfTrustIntfIndex_Object((1,3,6,1,4,1,248,15,3,3,1,3,1,1),_HmAgentCosMapIntfTrustIntfIndex_Type())
hmAgentCosMapIntfTrustIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosMapIntfTrustIntfIndex.setStatus(_A)
class _HmAgentCosMapIntfTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('untrusted',1),('trustDot1p',2),('trustIpPrecedence',3),('trustIpDscp',4)))
_HmAgentCosMapIntfTrustMode_Type.__name__=_F
_HmAgentCosMapIntfTrustMode_Object=MibTableColumn
hmAgentCosMapIntfTrustMode=_HmAgentCosMapIntfTrustMode_Object((1,3,6,1,4,1,248,15,3,3,1,3,1,2),_HmAgentCosMapIntfTrustMode_Type())
hmAgentCosMapIntfTrustMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosMapIntfTrustMode.setStatus(_A)
_HmAgentCosMapUntrustedTrafficClass_Type=Unsigned32
_HmAgentCosMapUntrustedTrafficClass_Object=MibTableColumn
hmAgentCosMapUntrustedTrafficClass=_HmAgentCosMapUntrustedTrafficClass_Object((1,3,6,1,4,1,248,15,3,3,1,3,1,3),_HmAgentCosMapUntrustedTrafficClass_Type())
hmAgentCosMapUntrustedTrafficClass.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentCosMapUntrustedTrafficClass.setStatus(_A)
_HmAgentCosQueueCfgGroup_ObjectIdentity=ObjectIdentity
hmAgentCosQueueCfgGroup=_HmAgentCosQueueCfgGroup_ObjectIdentity((1,3,6,1,4,1,248,15,3,3,2))
_HmAgentCosQueueNumQueuesPerPort_Type=Unsigned32
_HmAgentCosQueueNumQueuesPerPort_Object=MibScalar
hmAgentCosQueueNumQueuesPerPort=_HmAgentCosQueueNumQueuesPerPort_Object((1,3,6,1,4,1,248,15,3,3,2,1),_HmAgentCosQueueNumQueuesPerPort_Type())
hmAgentCosQueueNumQueuesPerPort.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentCosQueueNumQueuesPerPort.setStatus(_A)
_HmAgentCosQueueNumDropPrecedenceLevels_Type=Unsigned32
_HmAgentCosQueueNumDropPrecedenceLevels_Object=MibScalar
hmAgentCosQueueNumDropPrecedenceLevels=_HmAgentCosQueueNumDropPrecedenceLevels_Object((1,3,6,1,4,1,248,15,3,3,2,2),_HmAgentCosQueueNumDropPrecedenceLevels_Type())
hmAgentCosQueueNumDropPrecedenceLevels.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentCosQueueNumDropPrecedenceLevels.setStatus(_A)
_HmAgentCosQueueControlTable_Object=MibTable
hmAgentCosQueueControlTable=_HmAgentCosQueueControlTable_Object((1,3,6,1,4,1,248,15,3,3,2,3))
if mibBuilder.loadTexts:hmAgentCosQueueControlTable.setStatus(_A)
_HmAgentCosQueueControlEntry_Object=MibTableRow
hmAgentCosQueueControlEntry=_HmAgentCosQueueControlEntry_Object((1,3,6,1,4,1,248,15,3,3,2,3,1))
hmAgentCosQueueControlEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:hmAgentCosQueueControlEntry.setStatus(_A)
_HmAgentCosQueueIntfIndex_Type=InterfaceIndexOrZero
_HmAgentCosQueueIntfIndex_Object=MibTableColumn
hmAgentCosQueueIntfIndex=_HmAgentCosQueueIntfIndex_Object((1,3,6,1,4,1,248,15,3,3,2,3,1,1),_HmAgentCosQueueIntfIndex_Type())
hmAgentCosQueueIntfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosQueueIntfIndex.setStatus(_A)
class _HmAgentCosQueueIntfShapingRate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HmAgentCosQueueIntfShapingRate_Type.__name__=_D
_HmAgentCosQueueIntfShapingRate_Object=MibTableColumn
hmAgentCosQueueIntfShapingRate=_HmAgentCosQueueIntfShapingRate_Object((1,3,6,1,4,1,248,15,3,3,2,3,1,2),_HmAgentCosQueueIntfShapingRate_Type())
hmAgentCosQueueIntfShapingRate.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueIntfShapingRate.setStatus(_A)
class _HmAgentCosQueueMgmtTypeIntf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('wred',2)))
_HmAgentCosQueueMgmtTypeIntf_Type.__name__=_F
_HmAgentCosQueueMgmtTypeIntf_Object=MibTableColumn
hmAgentCosQueueMgmtTypeIntf=_HmAgentCosQueueMgmtTypeIntf_Object((1,3,6,1,4,1,248,15,3,3,2,3,1,3),_HmAgentCosQueueMgmtTypeIntf_Type())
hmAgentCosQueueMgmtTypeIntf.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueMgmtTypeIntf.setStatus(_A)
class _HmAgentCosQueueWredDecayExponent_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HmAgentCosQueueWredDecayExponent_Type.__name__=_D
_HmAgentCosQueueWredDecayExponent_Object=MibTableColumn
hmAgentCosQueueWredDecayExponent=_HmAgentCosQueueWredDecayExponent_Object((1,3,6,1,4,1,248,15,3,3,2,3,1,4),_HmAgentCosQueueWredDecayExponent_Type())
hmAgentCosQueueWredDecayExponent.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueWredDecayExponent.setStatus(_A)
class _HmAgentCosQueueDefaultsRestore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmAgentCosQueueDefaultsRestore_Type.__name__=_F
_HmAgentCosQueueDefaultsRestore_Object=MibTableColumn
hmAgentCosQueueDefaultsRestore=_HmAgentCosQueueDefaultsRestore_Object((1,3,6,1,4,1,248,15,3,3,2,3,1,5),_HmAgentCosQueueDefaultsRestore_Type())
hmAgentCosQueueDefaultsRestore.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueDefaultsRestore.setStatus(_A)
_HmAgentCosQueueTable_Object=MibTable
hmAgentCosQueueTable=_HmAgentCosQueueTable_Object((1,3,6,1,4,1,248,15,3,3,2,4))
if mibBuilder.loadTexts:hmAgentCosQueueTable.setStatus(_A)
_HmAgentCosQueueEntry_Object=MibTableRow
hmAgentCosQueueEntry=_HmAgentCosQueueEntry_Object((1,3,6,1,4,1,248,15,3,3,2,4,1))
hmAgentCosQueueEntry.setIndexNames((0,_C,_L),(0,_C,_b))
if mibBuilder.loadTexts:hmAgentCosQueueEntry.setStatus(_A)
_HmAgentCosQueueIndex_Type=Unsigned32
_HmAgentCosQueueIndex_Object=MibTableColumn
hmAgentCosQueueIndex=_HmAgentCosQueueIndex_Object((1,3,6,1,4,1,248,15,3,3,2,4,1,1),_HmAgentCosQueueIndex_Type())
hmAgentCosQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hmAgentCosQueueIndex.setStatus(_A)
class _HmAgentCosQueueSchedulerType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('weighted',2)))
_HmAgentCosQueueSchedulerType_Type.__name__=_F
_HmAgentCosQueueSchedulerType_Object=MibTableColumn
hmAgentCosQueueSchedulerType=_HmAgentCosQueueSchedulerType_Object((1,3,6,1,4,1,248,15,3,3,2,4,1,2),_HmAgentCosQueueSchedulerType_Type())
hmAgentCosQueueSchedulerType.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueSchedulerType.setStatus(_A)
class _HmAgentCosQueueMinBandwidth_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HmAgentCosQueueMinBandwidth_Type.__name__=_D
_HmAgentCosQueueMinBandwidth_Object=MibTableColumn
hmAgentCosQueueMinBandwidth=_HmAgentCosQueueMinBandwidth_Object((1,3,6,1,4,1,248,15,3,3,2,4,1,3),_HmAgentCosQueueMinBandwidth_Type())
hmAgentCosQueueMinBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueMinBandwidth.setStatus(_A)
class _HmAgentCosQueueMaxBandwidth_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HmAgentCosQueueMaxBandwidth_Type.__name__=_D
_HmAgentCosQueueMaxBandwidth_Object=MibTableColumn
hmAgentCosQueueMaxBandwidth=_HmAgentCosQueueMaxBandwidth_Object((1,3,6,1,4,1,248,15,3,3,2,4,1,4),_HmAgentCosQueueMaxBandwidth_Type())
hmAgentCosQueueMaxBandwidth.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueMaxBandwidth.setStatus(_A)
class _HmAgentCosQueueMgmtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('wred',2)))
_HmAgentCosQueueMgmtType_Type.__name__=_F
_HmAgentCosQueueMgmtType_Object=MibTableColumn
hmAgentCosQueueMgmtType=_HmAgentCosQueueMgmtType_Object((1,3,6,1,4,1,248,15,3,3,2,4,1,5),_HmAgentCosQueueMgmtType_Type())
hmAgentCosQueueMgmtType.setMaxAccess(_G)
if mibBuilder.loadTexts:hmAgentCosQueueMgmtType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EtypeValue':EtypeValue,'PercentByFives':PercentByFives,'Sixteenths':Sixteenths,'hmPlatform4QOS':hmPlatform4QOS,'hmAgentQOSACL':hmAgentQOSACL,'aclTable':aclTable,'aclEntry':aclEntry,_J:aclIndex,'aclStatus':aclStatus,'aclRuleTable':aclRuleTable,'aclRuleEntry':aclRuleEntry,_N:aclRuleIndex,'aclRuleAction':aclRuleAction,'aclRuleProtocol':aclRuleProtocol,'aclRuleSrcIpAddress':aclRuleSrcIpAddress,'aclRuleSrcIpMask':aclRuleSrcIpMask,'aclRuleSrcL4Port':aclRuleSrcL4Port,'aclRuleSrcL4PortRangeStart':aclRuleSrcL4PortRangeStart,'aclRuleSrcL4PortRangeEnd':aclRuleSrcL4PortRangeEnd,'aclRuleDestIpAddress':aclRuleDestIpAddress,'aclRuleDestIpMask':aclRuleDestIpMask,'aclRuleDestL4Port':aclRuleDestL4Port,'aclRuleDestL4PortRangeStart':aclRuleDestL4PortRangeStart,'aclRuleDestL4PortRangeEnd':aclRuleDestL4PortRangeEnd,'aclRuleIPDSCP':aclRuleIPDSCP,'aclRuleIpPrecedence':aclRuleIpPrecedence,'aclRuleIpTosBits':aclRuleIpTosBits,'aclRuleIpTosMask':aclRuleIpTosMask,'aclRuleStatus':aclRuleStatus,'aclRuleAssignQueueId':aclRuleAssignQueueId,'aclRuleRedirectIntf':aclRuleRedirectIntf,'aclRuleMatchEvery':aclRuleMatchEvery,'aclMacIndexNextFree':aclMacIndexNextFree,'aclMacTable':aclMacTable,'aclMacEntry':aclMacEntry,_K:aclMacIndex,'aclMacName':aclMacName,'aclMacStatus':aclMacStatus,'aclMacRuleTable':aclMacRuleTable,'aclMacRuleEntry':aclMacRuleEntry,_P:aclMacRuleIndex,'aclMacRuleAction':aclMacRuleAction,'aclMacRuleCos':aclMacRuleCos,'aclMacRuleCos2':aclMacRuleCos2,'aclMacRuleDestMacAddr':aclMacRuleDestMacAddr,'aclMacRuleDestMacMask':aclMacRuleDestMacMask,'aclMacRuleEtypeKey':aclMacRuleEtypeKey,'aclMacRuleEtypeValue':aclMacRuleEtypeValue,'aclMacRuleSrcMacAddr':aclMacRuleSrcMacAddr,'aclMacRuleSrcMacMask':aclMacRuleSrcMacMask,'aclMacRuleVlanId':aclMacRuleVlanId,'aclMacRuleVlanIdRangeStart':aclMacRuleVlanIdRangeStart,'aclMacRuleVlanIdRangeEnd':aclMacRuleVlanIdRangeEnd,'aclMacRuleVlanId2':aclMacRuleVlanId2,'aclMacRuleVlanId2RangeStart':aclMacRuleVlanId2RangeStart,'aclMacRuleVlanId2RangeEnd':aclMacRuleVlanId2RangeEnd,'aclMacRuleStatus':aclMacRuleStatus,'aclMacRuleAssignQueueId':aclMacRuleAssignQueueId,'aclMacRuleRedirectIntf':aclMacRuleRedirectIntf,'aclMacRuleMatchEvery':aclMacRuleMatchEvery,'aclIfTable':aclIfTable,'aclIfEntry':aclIfEntry,_Q:aclIfIndex,_R:aclIfDirection,_S:aclIfSequence,_T:aclIfAclType,_U:aclIfAclId,'aclIfStatus':aclIfStatus,'hmAgentQOSCOS':hmAgentQOSCOS,'hmAgentCosMapCfgGroup':hmAgentCosMapCfgGroup,'hmAgentCosMapIpPrecTable':hmAgentCosMapIpPrecTable,'hmAgentCosMapIpPrecEntry':hmAgentCosMapIpPrecEntry,_V:hmAgentCosMapIpPrecIntfIndex,_W:hmAgentCosMapIpPrecValue,'hmAgentCosMapIpPrecTrafficClass':hmAgentCosMapIpPrecTrafficClass,'hmAgentCosMapIpDscpTable':hmAgentCosMapIpDscpTable,'hmAgentCosMapIpDscpEntry':hmAgentCosMapIpDscpEntry,_X:hmAgentCosMapIpDscpIntfIndex,_Y:hmAgentCosMapIpDscpValue,'hmAgentCosMapIpDscpTrafficClass':hmAgentCosMapIpDscpTrafficClass,'hmAgentCosMapIntfTrustTable':hmAgentCosMapIntfTrustTable,'hmAgentCosMapIntfTrustEntry':hmAgentCosMapIntfTrustEntry,_Z:hmAgentCosMapIntfTrustIntfIndex,'hmAgentCosMapIntfTrustMode':hmAgentCosMapIntfTrustMode,'hmAgentCosMapUntrustedTrafficClass':hmAgentCosMapUntrustedTrafficClass,'hmAgentCosQueueCfgGroup':hmAgentCosQueueCfgGroup,'hmAgentCosQueueNumQueuesPerPort':hmAgentCosQueueNumQueuesPerPort,'hmAgentCosQueueNumDropPrecedenceLevels':hmAgentCosQueueNumDropPrecedenceLevels,'hmAgentCosQueueControlTable':hmAgentCosQueueControlTable,'hmAgentCosQueueControlEntry':hmAgentCosQueueControlEntry,_L:hmAgentCosQueueIntfIndex,'hmAgentCosQueueIntfShapingRate':hmAgentCosQueueIntfShapingRate,'hmAgentCosQueueMgmtTypeIntf':hmAgentCosQueueMgmtTypeIntf,'hmAgentCosQueueWredDecayExponent':hmAgentCosQueueWredDecayExponent,'hmAgentCosQueueDefaultsRestore':hmAgentCosQueueDefaultsRestore,'hmAgentCosQueueTable':hmAgentCosQueueTable,'hmAgentCosQueueEntry':hmAgentCosQueueEntry,_b:hmAgentCosQueueIndex,'hmAgentCosQueueSchedulerType':hmAgentCosQueueSchedulerType,'hmAgentCosQueueMinBandwidth':hmAgentCosQueueMinBandwidth,'hmAgentCosQueueMaxBandwidth':hmAgentCosQueueMaxBandwidth,'hmAgentCosQueueMgmtType':hmAgentCosQueueMgmtType})