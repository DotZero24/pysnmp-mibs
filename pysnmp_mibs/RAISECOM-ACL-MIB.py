_M='raisecomIpv6AclNumber'
_L='raisecomUserAclNumber'
_K='raisecomMacAclNumber'
_J='raisecomIpAclNumber'
_I='not-accessible'
_H='deny'
_G='permit'
_F='OctetString'
_E='RAISECOM-ACL-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
raisecomAcl=ModuleIdentity((1,3,6,1,4,1,8886,1,3))
_RaisecomIpAccessList_ObjectIdentity=ObjectIdentity
raisecomIpAccessList=_RaisecomIpAccessList_ObjectIdentity((1,3,6,1,4,1,8886,1,3,1))
_RaisecomIpAclTable_Object=MibTable
raisecomIpAclTable=_RaisecomIpAclTable_Object((1,3,6,1,4,1,8886,1,3,1,1))
if mibBuilder.loadTexts:raisecomIpAclTable.setStatus(_A)
_RaisecomIpAclEntry_Object=MibTableRow
raisecomIpAclEntry=_RaisecomIpAclEntry_Object((1,3,6,1,4,1,8886,1,3,1,1,1))
raisecomIpAclEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:raisecomIpAclEntry.setStatus(_A)
class _RaisecomIpAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_RaisecomIpAclNumber_Type.__name__=_C
_RaisecomIpAclNumber_Object=MibTableColumn
raisecomIpAclNumber=_RaisecomIpAclNumber_Object((1,3,6,1,4,1,8886,1,3,1,1,1,1),_RaisecomIpAclNumber_Type())
raisecomIpAclNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomIpAclNumber.setStatus(_A)
class _RaisecomIpAclAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RaisecomIpAclAccessType_Type.__name__=_C
_RaisecomIpAclAccessType_Object=MibTableColumn
raisecomIpAclAccessType=_RaisecomIpAclAccessType_Object((1,3,6,1,4,1,8886,1,3,1,1,1,2),_RaisecomIpAclAccessType_Type())
raisecomIpAclAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclAccessType.setStatus(_A)
class _RaisecomIpAclProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomIpAclProtocol_Type.__name__=_C
_RaisecomIpAclProtocol_Object=MibTableColumn
raisecomIpAclProtocol=_RaisecomIpAclProtocol_Object((1,3,6,1,4,1,8886,1,3,1,1,1,3),_RaisecomIpAclProtocol_Type())
raisecomIpAclProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclProtocol.setStatus(_A)
_RaisecomIpAclSourceAddress_Type=IpAddress
_RaisecomIpAclSourceAddress_Object=MibTableColumn
raisecomIpAclSourceAddress=_RaisecomIpAclSourceAddress_Object((1,3,6,1,4,1,8886,1,3,1,1,1,4),_RaisecomIpAclSourceAddress_Type())
raisecomIpAclSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclSourceAddress.setStatus(_A)
_RaisecomIpAclSourceMask_Type=IpAddress
_RaisecomIpAclSourceMask_Object=MibTableColumn
raisecomIpAclSourceMask=_RaisecomIpAclSourceMask_Object((1,3,6,1,4,1,8886,1,3,1,1,1,5),_RaisecomIpAclSourceMask_Type())
raisecomIpAclSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclSourceMask.setStatus(_A)
class _RaisecomIpAclSourceProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomIpAclSourceProtocolPort_Type.__name__=_C
_RaisecomIpAclSourceProtocolPort_Object=MibTableColumn
raisecomIpAclSourceProtocolPort=_RaisecomIpAclSourceProtocolPort_Object((1,3,6,1,4,1,8886,1,3,1,1,1,6),_RaisecomIpAclSourceProtocolPort_Type())
raisecomIpAclSourceProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclSourceProtocolPort.setStatus(_A)
_RaisecomIpAclDestinationAddress_Type=IpAddress
_RaisecomIpAclDestinationAddress_Object=MibTableColumn
raisecomIpAclDestinationAddress=_RaisecomIpAclDestinationAddress_Object((1,3,6,1,4,1,8886,1,3,1,1,1,7),_RaisecomIpAclDestinationAddress_Type())
raisecomIpAclDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclDestinationAddress.setStatus(_A)
_RaisecomIpAclDestinationMask_Type=IpAddress
_RaisecomIpAclDestinationMask_Object=MibTableColumn
raisecomIpAclDestinationMask=_RaisecomIpAclDestinationMask_Object((1,3,6,1,4,1,8886,1,3,1,1,1,8),_RaisecomIpAclDestinationMask_Type())
raisecomIpAclDestinationMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclDestinationMask.setStatus(_A)
class _RaisecomIpAclDestinationProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomIpAclDestinationProtocolPort_Type.__name__=_C
_RaisecomIpAclDestinationProtocolPort_Object=MibTableColumn
raisecomIpAclDestinationProtocolPort=_RaisecomIpAclDestinationProtocolPort_Object((1,3,6,1,4,1,8886,1,3,1,1,1,9),_RaisecomIpAclDestinationProtocolPort_Type())
raisecomIpAclDestinationProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclDestinationProtocolPort.setStatus(_A)
_RaisecomIpAclRef_Type=Gauge32
_RaisecomIpAclRef_Object=MibTableColumn
raisecomIpAclRef=_RaisecomIpAclRef_Object((1,3,6,1,4,1,8886,1,3,1,1,1,10),_RaisecomIpAclRef_Type())
raisecomIpAclRef.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIpAclRef.setStatus(_A)
_RaisecomIpAclStatus_Type=RowStatus
_RaisecomIpAclStatus_Object=MibTableColumn
raisecomIpAclStatus=_RaisecomIpAclStatus_Object((1,3,6,1,4,1,8886,1,3,1,1,1,11),_RaisecomIpAclStatus_Type())
raisecomIpAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclStatus.setStatus(_A)
_RaisecomIpAclSetFlag_Type=Unsigned32
_RaisecomIpAclSetFlag_Object=MibTableColumn
raisecomIpAclSetFlag=_RaisecomIpAclSetFlag_Object((1,3,6,1,4,1,8886,1,3,1,1,1,12),_RaisecomIpAclSetFlag_Type())
raisecomIpAclSetFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpAclSetFlag.setStatus(_A)
_RaisecomMacAccessList_ObjectIdentity=ObjectIdentity
raisecomMacAccessList=_RaisecomMacAccessList_ObjectIdentity((1,3,6,1,4,1,8886,1,3,2))
_RaisecomMacAclTable_Object=MibTable
raisecomMacAclTable=_RaisecomMacAclTable_Object((1,3,6,1,4,1,8886,1,3,2,1))
if mibBuilder.loadTexts:raisecomMacAclTable.setStatus(_A)
_RaisecomMacAclEntry_Object=MibTableRow
raisecomMacAclEntry=_RaisecomMacAclEntry_Object((1,3,6,1,4,1,8886,1,3,2,1,1))
raisecomMacAclEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:raisecomMacAclEntry.setStatus(_A)
class _RaisecomMacAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_RaisecomMacAclNumber_Type.__name__=_C
_RaisecomMacAclNumber_Object=MibTableColumn
raisecomMacAclNumber=_RaisecomMacAclNumber_Object((1,3,6,1,4,1,8886,1,3,2,1,1,1),_RaisecomMacAclNumber_Type())
raisecomMacAclNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomMacAclNumber.setStatus(_A)
class _RaisecomMacAclAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RaisecomMacAclAccessType_Type.__name__=_C
_RaisecomMacAclAccessType_Object=MibTableColumn
raisecomMacAclAccessType=_RaisecomMacAclAccessType_Object((1,3,6,1,4,1,8886,1,3,2,1,1,2),_RaisecomMacAclAccessType_Type())
raisecomMacAclAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclAccessType.setStatus(_A)
_RaisecomMacAclProtocol_Type=Integer32
_RaisecomMacAclProtocol_Object=MibTableColumn
raisecomMacAclProtocol=_RaisecomMacAclProtocol_Object((1,3,6,1,4,1,8886,1,3,2,1,1,3),_RaisecomMacAclProtocol_Type())
raisecomMacAclProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclProtocol.setStatus(_A)
_RaisecomMacAclSourceAddress_Type=MacAddress
_RaisecomMacAclSourceAddress_Object=MibTableColumn
raisecomMacAclSourceAddress=_RaisecomMacAclSourceAddress_Object((1,3,6,1,4,1,8886,1,3,2,1,1,4),_RaisecomMacAclSourceAddress_Type())
raisecomMacAclSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclSourceAddress.setStatus(_A)
_RaisecomMacAclSourceMask_Type=MacAddress
_RaisecomMacAclSourceMask_Object=MibTableColumn
raisecomMacAclSourceMask=_RaisecomMacAclSourceMask_Object((1,3,6,1,4,1,8886,1,3,2,1,1,5),_RaisecomMacAclSourceMask_Type())
raisecomMacAclSourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclSourceMask.setStatus(_A)
_RaisecomMacAclDestinationAddress_Type=MacAddress
_RaisecomMacAclDestinationAddress_Object=MibTableColumn
raisecomMacAclDestinationAddress=_RaisecomMacAclDestinationAddress_Object((1,3,6,1,4,1,8886,1,3,2,1,1,6),_RaisecomMacAclDestinationAddress_Type())
raisecomMacAclDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclDestinationAddress.setStatus(_A)
_RaisecomMacAclDestinationMask_Type=MacAddress
_RaisecomMacAclDestinationMask_Object=MibTableColumn
raisecomMacAclDestinationMask=_RaisecomMacAclDestinationMask_Object((1,3,6,1,4,1,8886,1,3,2,1,1,7),_RaisecomMacAclDestinationMask_Type())
raisecomMacAclDestinationMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclDestinationMask.setStatus(_A)
_RaisecomMacAclRef_Type=Gauge32
_RaisecomMacAclRef_Object=MibTableColumn
raisecomMacAclRef=_RaisecomMacAclRef_Object((1,3,6,1,4,1,8886,1,3,2,1,1,8),_RaisecomMacAclRef_Type())
raisecomMacAclRef.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomMacAclRef.setStatus(_A)
_RaisecomMacAclStatus_Type=RowStatus
_RaisecomMacAclStatus_Object=MibTableColumn
raisecomMacAclStatus=_RaisecomMacAclStatus_Object((1,3,6,1,4,1,8886,1,3,2,1,1,9),_RaisecomMacAclStatus_Type())
raisecomMacAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclStatus.setStatus(_A)
_RaisecomMacAclSetFlag_Type=Unsigned32
_RaisecomMacAclSetFlag_Object=MibTableColumn
raisecomMacAclSetFlag=_RaisecomMacAclSetFlag_Object((1,3,6,1,4,1,8886,1,3,2,1,1,10),_RaisecomMacAclSetFlag_Type())
raisecomMacAclSetFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomMacAclSetFlag.setStatus(_A)
_RaisecomUserAccessList_ObjectIdentity=ObjectIdentity
raisecomUserAccessList=_RaisecomUserAccessList_ObjectIdentity((1,3,6,1,4,1,8886,1,3,3))
_RaisecomUserAclTable_Object=MibTable
raisecomUserAclTable=_RaisecomUserAclTable_Object((1,3,6,1,4,1,8886,1,3,3,1))
if mibBuilder.loadTexts:raisecomUserAclTable.setStatus(_A)
_RaisecomUserAclEntry_Object=MibTableRow
raisecomUserAclEntry=_RaisecomUserAclEntry_Object((1,3,6,1,4,1,8886,1,3,3,1,1))
raisecomUserAclEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:raisecomUserAclEntry.setStatus(_A)
class _RaisecomUserAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_RaisecomUserAclNumber_Type.__name__=_C
_RaisecomUserAclNumber_Object=MibTableColumn
raisecomUserAclNumber=_RaisecomUserAclNumber_Object((1,3,6,1,4,1,8886,1,3,3,1,1,1),_RaisecomUserAclNumber_Type())
raisecomUserAclNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomUserAclNumber.setStatus(_A)
class _RaisecomUserAclAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RaisecomUserAclAccessType_Type.__name__=_C
_RaisecomUserAclAccessType_Object=MibTableColumn
raisecomUserAclAccessType=_RaisecomUserAclAccessType_Object((1,3,6,1,4,1,8886,1,3,3,1,1,2),_RaisecomUserAclAccessType_Type())
raisecomUserAclAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclAccessType.setStatus(_A)
class _RaisecomUserAclRuleString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RaisecomUserAclRuleString_Type.__name__=_F
_RaisecomUserAclRuleString_Object=MibTableColumn
raisecomUserAclRuleString=_RaisecomUserAclRuleString_Object((1,3,6,1,4,1,8886,1,3,3,1,1,3),_RaisecomUserAclRuleString_Type())
raisecomUserAclRuleString.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclRuleString.setStatus(_A)
class _RaisecomUserAclRuleMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RaisecomUserAclRuleMask_Type.__name__=_F
_RaisecomUserAclRuleMask_Object=MibTableColumn
raisecomUserAclRuleMask=_RaisecomUserAclRuleMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,4),_RaisecomUserAclRuleMask_Type())
raisecomUserAclRuleMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclRuleMask.setStatus(_A)
class _RaisecomUserAclOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RaisecomUserAclOffset_Type.__name__=_C
_RaisecomUserAclOffset_Object=MibTableColumn
raisecomUserAclOffset=_RaisecomUserAclOffset_Object((1,3,6,1,4,1,8886,1,3,3,1,1,5),_RaisecomUserAclOffset_Type())
raisecomUserAclOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclOffset.setStatus(_A)
_RaisecomUserAclRef_Type=Gauge32
_RaisecomUserAclRef_Object=MibTableColumn
raisecomUserAclRef=_RaisecomUserAclRef_Object((1,3,6,1,4,1,8886,1,3,3,1,1,6),_RaisecomUserAclRef_Type())
raisecomUserAclRef.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomUserAclRef.setStatus(_A)
_RaisecomUserAclStatus_Type=RowStatus
_RaisecomUserAclStatus_Object=MibTableColumn
raisecomUserAclStatus=_RaisecomUserAclStatus_Object((1,3,6,1,4,1,8886,1,3,3,1,1,7),_RaisecomUserAclStatus_Type())
raisecomUserAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclStatus.setStatus(_A)
_RaisecomUserAclSourceMacAddress_Type=MacAddress
_RaisecomUserAclSourceMacAddress_Object=MibTableColumn
raisecomUserAclSourceMacAddress=_RaisecomUserAclSourceMacAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,8),_RaisecomUserAclSourceMacAddress_Type())
raisecomUserAclSourceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSourceMacAddress.setStatus(_A)
_RaisecomUserAclDestinationMacAddress_Type=MacAddress
_RaisecomUserAclDestinationMacAddress_Object=MibTableColumn
raisecomUserAclDestinationMacAddress=_RaisecomUserAclDestinationMacAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,9),_RaisecomUserAclDestinationMacAddress_Type())
raisecomUserAclDestinationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclDestinationMacAddress.setStatus(_A)
_RaisecomUserAclEtherType_Type=Integer32
_RaisecomUserAclEtherType_Object=MibTableColumn
raisecomUserAclEtherType=_RaisecomUserAclEtherType_Object((1,3,6,1,4,1,8886,1,3,3,1,1,10),_RaisecomUserAclEtherType_Type())
raisecomUserAclEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclEtherType.setStatus(_A)
_RaisecomUserAclEtherTypeMask_Type=Integer32
_RaisecomUserAclEtherTypeMask_Object=MibTableColumn
raisecomUserAclEtherTypeMask=_RaisecomUserAclEtherTypeMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,11),_RaisecomUserAclEtherTypeMask_Type())
raisecomUserAclEtherTypeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclEtherTypeMask.setStatus(_A)
_RaisecomUserAclSourceIpAddress_Type=IpAddress
_RaisecomUserAclSourceIpAddress_Object=MibTableColumn
raisecomUserAclSourceIpAddress=_RaisecomUserAclSourceIpAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,12),_RaisecomUserAclSourceIpAddress_Type())
raisecomUserAclSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSourceIpAddress.setStatus(_A)
_RaisecomUserAclSourceIpMask_Type=IpAddress
_RaisecomUserAclSourceIpMask_Object=MibTableColumn
raisecomUserAclSourceIpMask=_RaisecomUserAclSourceIpMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,13),_RaisecomUserAclSourceIpMask_Type())
raisecomUserAclSourceIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSourceIpMask.setStatus(_A)
_RaisecomUserAclDestinationIpAddress_Type=IpAddress
_RaisecomUserAclDestinationIpAddress_Object=MibTableColumn
raisecomUserAclDestinationIpAddress=_RaisecomUserAclDestinationIpAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,14),_RaisecomUserAclDestinationIpAddress_Type())
raisecomUserAclDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclDestinationIpAddress.setStatus(_A)
_RaisecomUserAclDestinationIpMask_Type=IpAddress
_RaisecomUserAclDestinationIpMask_Object=MibTableColumn
raisecomUserAclDestinationIpMask=_RaisecomUserAclDestinationIpMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,15),_RaisecomUserAclDestinationIpMask_Type())
raisecomUserAclDestinationIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclDestinationIpMask.setStatus(_A)
class _RaisecomUserAclIpPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routine',0),('priority',1),('immediate',2),('flash',3),('flash-override',4),('critical',5),('internet',6),('network',7)))
_RaisecomUserAclIpPrecedence_Type.__name__=_C
_RaisecomUserAclIpPrecedence_Object=MibTableColumn
raisecomUserAclIpPrecedence=_RaisecomUserAclIpPrecedence_Object((1,3,6,1,4,1,8886,1,3,3,1,1,16),_RaisecomUserAclIpPrecedence_Type())
raisecomUserAclIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpPrecedence.setStatus(_A)
class _RaisecomUserAclIpTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_RaisecomUserAclIpTos_Type.__name__=_C
_RaisecomUserAclIpTos_Object=MibTableColumn
raisecomUserAclIpTos=_RaisecomUserAclIpTos_Object((1,3,6,1,4,1,8886,1,3,3,1,1,17),_RaisecomUserAclIpTos_Type())
raisecomUserAclIpTos.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpTos.setStatus(_A)
class _RaisecomUserAclIpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RaisecomUserAclIpDscp_Type.__name__=_C
_RaisecomUserAclIpDscp_Object=MibTableColumn
raisecomUserAclIpDscp=_RaisecomUserAclIpDscp_Object((1,3,6,1,4,1,8886,1,3,3,1,1,18),_RaisecomUserAclIpDscp_Type())
raisecomUserAclIpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpDscp.setStatus(_A)
class _RaisecomUserAclIpFragmentsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nofragments',0),('fragments',1)))
_RaisecomUserAclIpFragmentsFlag_Type.__name__=_C
_RaisecomUserAclIpFragmentsFlag_Object=MibTableColumn
raisecomUserAclIpFragmentsFlag=_RaisecomUserAclIpFragmentsFlag_Object((1,3,6,1,4,1,8886,1,3,3,1,1,19),_RaisecomUserAclIpFragmentsFlag_Type())
raisecomUserAclIpFragmentsFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpFragmentsFlag.setStatus(_A)
class _RaisecomUserAclIpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomUserAclIpProtocol_Type.__name__=_C
_RaisecomUserAclIpProtocol_Object=MibTableColumn
raisecomUserAclIpProtocol=_RaisecomUserAclIpProtocol_Object((1,3,6,1,4,1,8886,1,3,3,1,1,20),_RaisecomUserAclIpProtocol_Type())
raisecomUserAclIpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpProtocol.setStatus(_A)
class _RaisecomUserAclSourceProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomUserAclSourceProtocolPort_Type.__name__=_C
_RaisecomUserAclSourceProtocolPort_Object=MibTableColumn
raisecomUserAclSourceProtocolPort=_RaisecomUserAclSourceProtocolPort_Object((1,3,6,1,4,1,8886,1,3,3,1,1,21),_RaisecomUserAclSourceProtocolPort_Type())
raisecomUserAclSourceProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSourceProtocolPort.setStatus(_A)
class _RaisecomUserAclDestinationProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomUserAclDestinationProtocolPort_Type.__name__=_C
_RaisecomUserAclDestinationProtocolPort_Object=MibTableColumn
raisecomUserAclDestinationProtocolPort=_RaisecomUserAclDestinationProtocolPort_Object((1,3,6,1,4,1,8886,1,3,3,1,1,22),_RaisecomUserAclDestinationProtocolPort_Type())
raisecomUserAclDestinationProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclDestinationProtocolPort.setStatus(_A)
class _RaisecomUserAclTcpProtocolFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RaisecomUserAclTcpProtocolFlag_Type.__name__=_C
_RaisecomUserAclTcpProtocolFlag_Object=MibTableColumn
raisecomUserAclTcpProtocolFlag=_RaisecomUserAclTcpProtocolFlag_Object((1,3,6,1,4,1,8886,1,3,3,1,1,23),_RaisecomUserAclTcpProtocolFlag_Type())
raisecomUserAclTcpProtocolFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclTcpProtocolFlag.setStatus(_A)
class _RaisecomUserAclCvlanCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomUserAclCvlanCos_Type.__name__=_C
_RaisecomUserAclCvlanCos_Object=MibTableColumn
raisecomUserAclCvlanCos=_RaisecomUserAclCvlanCos_Object((1,3,6,1,4,1,8886,1,3,3,1,1,24),_RaisecomUserAclCvlanCos_Type())
raisecomUserAclCvlanCos.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclCvlanCos.setStatus(_A)
class _RaisecomUserAclSvlanCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomUserAclSvlanCos_Type.__name__=_C
_RaisecomUserAclSvlanCos_Object=MibTableColumn
raisecomUserAclSvlanCos=_RaisecomUserAclSvlanCos_Object((1,3,6,1,4,1,8886,1,3,3,1,1,25),_RaisecomUserAclSvlanCos_Type())
raisecomUserAclSvlanCos.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSvlanCos.setStatus(_A)
class _RaisecomUserAclCvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomUserAclCvlan_Type.__name__=_C
_RaisecomUserAclCvlan_Object=MibTableColumn
raisecomUserAclCvlan=_RaisecomUserAclCvlan_Object((1,3,6,1,4,1,8886,1,3,3,1,1,26),_RaisecomUserAclCvlan_Type())
raisecomUserAclCvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclCvlan.setStatus(_A)
class _RaisecomUserAclSvlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RaisecomUserAclSvlan_Type.__name__=_C
_RaisecomUserAclSvlan_Object=MibTableColumn
raisecomUserAclSvlan=_RaisecomUserAclSvlan_Object((1,3,6,1,4,1,8886,1,3,3,1,1,27),_RaisecomUserAclSvlan_Type())
raisecomUserAclSvlan.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSvlan.setStatus(_A)
_RaisecomUserAclSetFlag_Type=Unsigned32
_RaisecomUserAclSetFlag_Object=MibTableColumn
raisecomUserAclSetFlag=_RaisecomUserAclSetFlag_Object((1,3,6,1,4,1,8886,1,3,3,1,1,28),_RaisecomUserAclSetFlag_Type())
raisecomUserAclSetFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSetFlag.setStatus(_A)
_RaisecomUserAclSourceMacMask_Type=MacAddress
_RaisecomUserAclSourceMacMask_Object=MibTableColumn
raisecomUserAclSourceMacMask=_RaisecomUserAclSourceMacMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,29),_RaisecomUserAclSourceMacMask_Type())
raisecomUserAclSourceMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclSourceMacMask.setStatus(_A)
_RaisecomUserAclDestinationMacMask_Type=MacAddress
_RaisecomUserAclDestinationMacMask_Object=MibTableColumn
raisecomUserAclDestinationMacMask=_RaisecomUserAclDestinationMacMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,30),_RaisecomUserAclDestinationMacMask_Type())
raisecomUserAclDestinationMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclDestinationMacMask.setStatus(_A)
class _RaisecomUserAclCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomUserAclCos_Type.__name__=_C
_RaisecomUserAclCos_Object=MibTableColumn
raisecomUserAclCos=_RaisecomUserAclCos_Object((1,3,6,1,4,1,8886,1,3,3,1,1,31),_RaisecomUserAclCos_Type())
raisecomUserAclCos.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclCos.setStatus(_A)
class _RaisecomUserAclArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('request',1),('reply',2)))
_RaisecomUserAclArpType_Type.__name__=_C
_RaisecomUserAclArpType_Object=MibTableColumn
raisecomUserAclArpType=_RaisecomUserAclArpType_Object((1,3,6,1,4,1,8886,1,3,3,1,1,32),_RaisecomUserAclArpType_Type())
raisecomUserAclArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclArpType.setStatus(_A)
_RaisecomUserAclArpSenderMac_Type=MacAddress
_RaisecomUserAclArpSenderMac_Object=MibTableColumn
raisecomUserAclArpSenderMac=_RaisecomUserAclArpSenderMac_Object((1,3,6,1,4,1,8886,1,3,3,1,1,33),_RaisecomUserAclArpSenderMac_Type())
raisecomUserAclArpSenderMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclArpSenderMac.setStatus(_A)
_RaisecomUserAclArpTargetMac_Type=MacAddress
_RaisecomUserAclArpTargetMac_Object=MibTableColumn
raisecomUserAclArpTargetMac=_RaisecomUserAclArpTargetMac_Object((1,3,6,1,4,1,8886,1,3,3,1,1,34),_RaisecomUserAclArpTargetMac_Type())
raisecomUserAclArpTargetMac.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclArpTargetMac.setStatus(_A)
class _RaisecomUserAclIcmpIgmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomUserAclIcmpIgmpType_Type.__name__=_C
_RaisecomUserAclIcmpIgmpType_Object=MibTableColumn
raisecomUserAclIcmpIgmpType=_RaisecomUserAclIcmpIgmpType_Object((1,3,6,1,4,1,8886,1,3,3,1,1,35),_RaisecomUserAclIcmpIgmpType_Type())
raisecomUserAclIcmpIgmpType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIcmpIgmpType.setStatus(_A)
class _RaisecomUserAclIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomUserAclIcmpCode_Type.__name__=_C
_RaisecomUserAclIcmpCode_Object=MibTableColumn
raisecomUserAclIcmpCode=_RaisecomUserAclIcmpCode_Object((1,3,6,1,4,1,8886,1,3,3,1,1,36),_RaisecomUserAclIcmpCode_Type())
raisecomUserAclIcmpCode.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIcmpCode.setStatus(_A)
_RaisecomUserAclIpv6SourceAddress_Type=Ipv6Address
_RaisecomUserAclIpv6SourceAddress_Object=MibTableColumn
raisecomUserAclIpv6SourceAddress=_RaisecomUserAclIpv6SourceAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,37),_RaisecomUserAclIpv6SourceAddress_Type())
raisecomUserAclIpv6SourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6SourceAddress.setStatus(_A)
_RaisecomUserAclIpv6SourceMask_Type=Ipv6Address
_RaisecomUserAclIpv6SourceMask_Object=MibTableColumn
raisecomUserAclIpv6SourceMask=_RaisecomUserAclIpv6SourceMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,38),_RaisecomUserAclIpv6SourceMask_Type())
raisecomUserAclIpv6SourceMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6SourceMask.setStatus(_A)
_RaisecomUserAclIpv6DestinationAddress_Type=Ipv6Address
_RaisecomUserAclIpv6DestinationAddress_Object=MibTableColumn
raisecomUserAclIpv6DestinationAddress=_RaisecomUserAclIpv6DestinationAddress_Object((1,3,6,1,4,1,8886,1,3,3,1,1,39),_RaisecomUserAclIpv6DestinationAddress_Type())
raisecomUserAclIpv6DestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6DestinationAddress.setStatus(_A)
_RaisecomUserAclIpv6DestinationMask_Type=Ipv6Address
_RaisecomUserAclIpv6DestinationMask_Object=MibTableColumn
raisecomUserAclIpv6DestinationMask=_RaisecomUserAclIpv6DestinationMask_Object((1,3,6,1,4,1,8886,1,3,3,1,1,40),_RaisecomUserAclIpv6DestinationMask_Type())
raisecomUserAclIpv6DestinationMask.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6DestinationMask.setStatus(_A)
_RaisecomUserAclIpv6SourceMaskLen_Type=Integer32
_RaisecomUserAclIpv6SourceMaskLen_Object=MibTableColumn
raisecomUserAclIpv6SourceMaskLen=_RaisecomUserAclIpv6SourceMaskLen_Object((1,3,6,1,4,1,8886,1,3,3,1,1,41),_RaisecomUserAclIpv6SourceMaskLen_Type())
raisecomUserAclIpv6SourceMaskLen.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6SourceMaskLen.setStatus(_A)
_RaisecomUserAclIpv6DestinationMaskLen_Type=Integer32
_RaisecomUserAclIpv6DestinationMaskLen_Object=MibTableColumn
raisecomUserAclIpv6DestinationMaskLen=_RaisecomUserAclIpv6DestinationMaskLen_Object((1,3,6,1,4,1,8886,1,3,3,1,1,42),_RaisecomUserAclIpv6DestinationMaskLen_Type())
raisecomUserAclIpv6DestinationMaskLen.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6DestinationMaskLen.setStatus(_A)
class _RaisecomUserAclIpv6Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomUserAclIpv6Protocol_Type.__name__=_C
_RaisecomUserAclIpv6Protocol_Object=MibTableColumn
raisecomUserAclIpv6Protocol=_RaisecomUserAclIpv6Protocol_Object((1,3,6,1,4,1,8886,1,3,3,1,1,43),_RaisecomUserAclIpv6Protocol_Type())
raisecomUserAclIpv6Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6Protocol.setStatus(_A)
_RaisecomUserAclIpv6FlowLabel_Type=Integer32
_RaisecomUserAclIpv6FlowLabel_Object=MibTableColumn
raisecomUserAclIpv6FlowLabel=_RaisecomUserAclIpv6FlowLabel_Object((1,3,6,1,4,1,8886,1,3,3,1,1,44),_RaisecomUserAclIpv6FlowLabel_Type())
raisecomUserAclIpv6FlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6FlowLabel.setStatus(_A)
class _RaisecomUserAclIpv6TrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(130,131,132)));namedValues=NamedValues(*(('mld-query',130),('mld-report',131),('mld-done',132)))
_RaisecomUserAclIpv6TrafficClass_Type.__name__=_C
_RaisecomUserAclIpv6TrafficClass_Object=MibTableColumn
raisecomUserAclIpv6TrafficClass=_RaisecomUserAclIpv6TrafficClass_Object((1,3,6,1,4,1,8886,1,3,3,1,1,45),_RaisecomUserAclIpv6TrafficClass_Type())
raisecomUserAclIpv6TrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIpv6TrafficClass.setStatus(_A)
class _RaisecomUserAclIcmpv6Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomUserAclIcmpv6Type_Type.__name__=_C
_RaisecomUserAclIcmpv6Type_Object=MibTableColumn
raisecomUserAclIcmpv6Type=_RaisecomUserAclIcmpv6Type_Object((1,3,6,1,4,1,8886,1,3,3,1,1,46),_RaisecomUserAclIcmpv6Type_Type())
raisecomUserAclIcmpv6Type.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclIcmpv6Type.setStatus(_A)
_RaisecomUserAclUserLen_Type=Integer32
_RaisecomUserAclUserLen_Object=MibTableColumn
raisecomUserAclUserLen=_RaisecomUserAclUserLen_Object((1,3,6,1,4,1,8886,1,3,3,1,1,47),_RaisecomUserAclUserLen_Type())
raisecomUserAclUserLen.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomUserAclUserLen.setStatus(_A)
class _RaisecomUserAclExtensionSetFlag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_RaisecomUserAclExtensionSetFlag_Type.__name__=_F
_RaisecomUserAclExtensionSetFlag_Object=MibTableColumn
raisecomUserAclExtensionSetFlag=_RaisecomUserAclExtensionSetFlag_Object((1,3,6,1,4,1,8886,1,3,3,1,1,48),_RaisecomUserAclExtensionSetFlag_Type())
raisecomUserAclExtensionSetFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclExtensionSetFlag.setStatus(_A)
class _RaisecomUserAclTunnelLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_RaisecomUserAclTunnelLabel_Type.__name__=_C
_RaisecomUserAclTunnelLabel_Object=MibTableColumn
raisecomUserAclTunnelLabel=_RaisecomUserAclTunnelLabel_Object((1,3,6,1,4,1,8886,1,3,3,1,1,49),_RaisecomUserAclTunnelLabel_Type())
raisecomUserAclTunnelLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclTunnelLabel.setStatus(_A)
class _RaisecomUserAclTunnelExp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomUserAclTunnelExp_Type.__name__=_C
_RaisecomUserAclTunnelExp_Object=MibTableColumn
raisecomUserAclTunnelExp=_RaisecomUserAclTunnelExp_Object((1,3,6,1,4,1,8886,1,3,3,1,1,50),_RaisecomUserAclTunnelExp_Type())
raisecomUserAclTunnelExp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclTunnelExp.setStatus(_A)
class _RaisecomUserAclVcLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_RaisecomUserAclVcLabel_Type.__name__=_C
_RaisecomUserAclVcLabel_Object=MibTableColumn
raisecomUserAclVcLabel=_RaisecomUserAclVcLabel_Object((1,3,6,1,4,1,8886,1,3,3,1,1,51),_RaisecomUserAclVcLabel_Type())
raisecomUserAclVcLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclVcLabel.setStatus(_A)
class _RaisecomUserAclVcExp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RaisecomUserAclVcExp_Type.__name__=_C
_RaisecomUserAclVcExp_Object=MibTableColumn
raisecomUserAclVcExp=_RaisecomUserAclVcExp_Object((1,3,6,1,4,1,8886,1,3,3,1,1,52),_RaisecomUserAclVcExp_Type())
raisecomUserAclVcExp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomUserAclVcExp.setStatus(_A)
_RaisecomIpv6AccessList_ObjectIdentity=ObjectIdentity
raisecomIpv6AccessList=_RaisecomIpv6AccessList_ObjectIdentity((1,3,6,1,4,1,8886,1,3,4))
_RaisecomIpv6AclTable_Object=MibTable
raisecomIpv6AclTable=_RaisecomIpv6AclTable_Object((1,3,6,1,4,1,8886,1,3,4,1))
if mibBuilder.loadTexts:raisecomIpv6AclTable.setStatus(_A)
_RaisecomIpv6AclEntry_Object=MibTableRow
raisecomIpv6AclEntry=_RaisecomIpv6AclEntry_Object((1,3,6,1,4,1,8886,1,3,4,1,1))
raisecomIpv6AclEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:raisecomIpv6AclEntry.setStatus(_A)
class _RaisecomIpv6AclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_RaisecomIpv6AclNumber_Type.__name__=_C
_RaisecomIpv6AclNumber_Object=MibTableColumn
raisecomIpv6AclNumber=_RaisecomIpv6AclNumber_Object((1,3,6,1,4,1,8886,1,3,4,1,1,1),_RaisecomIpv6AclNumber_Type())
raisecomIpv6AclNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomIpv6AclNumber.setStatus(_A)
class _RaisecomIpv6AclAccessType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RaisecomIpv6AclAccessType_Type.__name__=_C
_RaisecomIpv6AclAccessType_Object=MibTableColumn
raisecomIpv6AclAccessType=_RaisecomIpv6AclAccessType_Object((1,3,6,1,4,1,8886,1,3,4,1,1,2),_RaisecomIpv6AclAccessType_Type())
raisecomIpv6AclAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclAccessType.setStatus(_A)
class _RaisecomIpv6AclProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RaisecomIpv6AclProtocol_Type.__name__=_C
_RaisecomIpv6AclProtocol_Object=MibTableColumn
raisecomIpv6AclProtocol=_RaisecomIpv6AclProtocol_Object((1,3,6,1,4,1,8886,1,3,4,1,1,3),_RaisecomIpv6AclProtocol_Type())
raisecomIpv6AclProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclProtocol.setStatus(_A)
_RaisecomIpv6AclSourceAddress_Type=Ipv6Address
_RaisecomIpv6AclSourceAddress_Object=MibTableColumn
raisecomIpv6AclSourceAddress=_RaisecomIpv6AclSourceAddress_Object((1,3,6,1,4,1,8886,1,3,4,1,1,4),_RaisecomIpv6AclSourceAddress_Type())
raisecomIpv6AclSourceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclSourceAddress.setStatus(_A)
class _RaisecomIpv6AclSourcePrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RaisecomIpv6AclSourcePrefixLen_Type.__name__=_C
_RaisecomIpv6AclSourcePrefixLen_Object=MibTableColumn
raisecomIpv6AclSourcePrefixLen=_RaisecomIpv6AclSourcePrefixLen_Object((1,3,6,1,4,1,8886,1,3,4,1,1,5),_RaisecomIpv6AclSourcePrefixLen_Type())
raisecomIpv6AclSourcePrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclSourcePrefixLen.setStatus(_A)
_RaisecomIpv6AclDestinationAddress_Type=Ipv6Address
_RaisecomIpv6AclDestinationAddress_Object=MibTableColumn
raisecomIpv6AclDestinationAddress=_RaisecomIpv6AclDestinationAddress_Object((1,3,6,1,4,1,8886,1,3,4,1,1,6),_RaisecomIpv6AclDestinationAddress_Type())
raisecomIpv6AclDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclDestinationAddress.setStatus(_A)
class _RaisecomIpv6AclDestinationPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RaisecomIpv6AclDestinationPrefixLen_Type.__name__=_C
_RaisecomIpv6AclDestinationPrefixLen_Object=MibTableColumn
raisecomIpv6AclDestinationPrefixLen=_RaisecomIpv6AclDestinationPrefixLen_Object((1,3,6,1,4,1,8886,1,3,4,1,1,7),_RaisecomIpv6AclDestinationPrefixLen_Type())
raisecomIpv6AclDestinationPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclDestinationPrefixLen.setStatus(_A)
class _RaisecomIpv6AclTrafficClass_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_RaisecomIpv6AclTrafficClass_Type.__name__=_C
_RaisecomIpv6AclTrafficClass_Object=MibTableColumn
raisecomIpv6AclTrafficClass=_RaisecomIpv6AclTrafficClass_Object((1,3,6,1,4,1,8886,1,3,4,1,1,8),_RaisecomIpv6AclTrafficClass_Type())
raisecomIpv6AclTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclTrafficClass.setStatus(_A)
class _RaisecomIpv6AclFlowLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_RaisecomIpv6AclFlowLabel_Type.__name__=_C
_RaisecomIpv6AclFlowLabel_Object=MibTableColumn
raisecomIpv6AclFlowLabel=_RaisecomIpv6AclFlowLabel_Object((1,3,6,1,4,1,8886,1,3,4,1,1,9),_RaisecomIpv6AclFlowLabel_Type())
raisecomIpv6AclFlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclFlowLabel.setStatus(_A)
_RaisecomIpv6AclRef_Type=Gauge32
_RaisecomIpv6AclRef_Object=MibTableColumn
raisecomIpv6AclRef=_RaisecomIpv6AclRef_Object((1,3,6,1,4,1,8886,1,3,4,1,1,10),_RaisecomIpv6AclRef_Type())
raisecomIpv6AclRef.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIpv6AclRef.setStatus(_A)
_RaisecomIpv6AclStatus_Type=RowStatus
_RaisecomIpv6AclStatus_Object=MibTableColumn
raisecomIpv6AclStatus=_RaisecomIpv6AclStatus_Object((1,3,6,1,4,1,8886,1,3,4,1,1,11),_RaisecomIpv6AclStatus_Type())
raisecomIpv6AclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclStatus.setStatus(_A)
class _RaisecomIpv6AclSourceProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomIpv6AclSourceProtocolPort_Type.__name__=_C
_RaisecomIpv6AclSourceProtocolPort_Object=MibTableColumn
raisecomIpv6AclSourceProtocolPort=_RaisecomIpv6AclSourceProtocolPort_Object((1,3,6,1,4,1,8886,1,3,4,1,1,12),_RaisecomIpv6AclSourceProtocolPort_Type())
raisecomIpv6AclSourceProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclSourceProtocolPort.setStatus(_A)
class _RaisecomIpv6AclDestinationProtocolPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RaisecomIpv6AclDestinationProtocolPort_Type.__name__=_C
_RaisecomIpv6AclDestinationProtocolPort_Object=MibTableColumn
raisecomIpv6AclDestinationProtocolPort=_RaisecomIpv6AclDestinationProtocolPort_Object((1,3,6,1,4,1,8886,1,3,4,1,1,13),_RaisecomIpv6AclDestinationProtocolPort_Type())
raisecomIpv6AclDestinationProtocolPort.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclDestinationProtocolPort.setStatus(_A)
_RaisecomIpv6AclSetFlag_Type=Unsigned32
_RaisecomIpv6AclSetFlag_Object=MibTableColumn
raisecomIpv6AclSetFlag=_RaisecomIpv6AclSetFlag_Object((1,3,6,1,4,1,8886,1,3,4,1,1,14),_RaisecomIpv6AclSetFlag_Type())
raisecomIpv6AclSetFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomIpv6AclSetFlag.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'raisecomAcl':raisecomAcl,'raisecomIpAccessList':raisecomIpAccessList,'raisecomIpAclTable':raisecomIpAclTable,'raisecomIpAclEntry':raisecomIpAclEntry,_J:raisecomIpAclNumber,'raisecomIpAclAccessType':raisecomIpAclAccessType,'raisecomIpAclProtocol':raisecomIpAclProtocol,'raisecomIpAclSourceAddress':raisecomIpAclSourceAddress,'raisecomIpAclSourceMask':raisecomIpAclSourceMask,'raisecomIpAclSourceProtocolPort':raisecomIpAclSourceProtocolPort,'raisecomIpAclDestinationAddress':raisecomIpAclDestinationAddress,'raisecomIpAclDestinationMask':raisecomIpAclDestinationMask,'raisecomIpAclDestinationProtocolPort':raisecomIpAclDestinationProtocolPort,'raisecomIpAclRef':raisecomIpAclRef,'raisecomIpAclStatus':raisecomIpAclStatus,'raisecomIpAclSetFlag':raisecomIpAclSetFlag,'raisecomMacAccessList':raisecomMacAccessList,'raisecomMacAclTable':raisecomMacAclTable,'raisecomMacAclEntry':raisecomMacAclEntry,_K:raisecomMacAclNumber,'raisecomMacAclAccessType':raisecomMacAclAccessType,'raisecomMacAclProtocol':raisecomMacAclProtocol,'raisecomMacAclSourceAddress':raisecomMacAclSourceAddress,'raisecomMacAclSourceMask':raisecomMacAclSourceMask,'raisecomMacAclDestinationAddress':raisecomMacAclDestinationAddress,'raisecomMacAclDestinationMask':raisecomMacAclDestinationMask,'raisecomMacAclRef':raisecomMacAclRef,'raisecomMacAclStatus':raisecomMacAclStatus,'raisecomMacAclSetFlag':raisecomMacAclSetFlag,'raisecomUserAccessList':raisecomUserAccessList,'raisecomUserAclTable':raisecomUserAclTable,'raisecomUserAclEntry':raisecomUserAclEntry,_L:raisecomUserAclNumber,'raisecomUserAclAccessType':raisecomUserAclAccessType,'raisecomUserAclRuleString':raisecomUserAclRuleString,'raisecomUserAclRuleMask':raisecomUserAclRuleMask,'raisecomUserAclOffset':raisecomUserAclOffset,'raisecomUserAclRef':raisecomUserAclRef,'raisecomUserAclStatus':raisecomUserAclStatus,'raisecomUserAclSourceMacAddress':raisecomUserAclSourceMacAddress,'raisecomUserAclDestinationMacAddress':raisecomUserAclDestinationMacAddress,'raisecomUserAclEtherType':raisecomUserAclEtherType,'raisecomUserAclEtherTypeMask':raisecomUserAclEtherTypeMask,'raisecomUserAclSourceIpAddress':raisecomUserAclSourceIpAddress,'raisecomUserAclSourceIpMask':raisecomUserAclSourceIpMask,'raisecomUserAclDestinationIpAddress':raisecomUserAclDestinationIpAddress,'raisecomUserAclDestinationIpMask':raisecomUserAclDestinationIpMask,'raisecomUserAclIpPrecedence':raisecomUserAclIpPrecedence,'raisecomUserAclIpTos':raisecomUserAclIpTos,'raisecomUserAclIpDscp':raisecomUserAclIpDscp,'raisecomUserAclIpFragmentsFlag':raisecomUserAclIpFragmentsFlag,'raisecomUserAclIpProtocol':raisecomUserAclIpProtocol,'raisecomUserAclSourceProtocolPort':raisecomUserAclSourceProtocolPort,'raisecomUserAclDestinationProtocolPort':raisecomUserAclDestinationProtocolPort,'raisecomUserAclTcpProtocolFlag':raisecomUserAclTcpProtocolFlag,'raisecomUserAclCvlanCos':raisecomUserAclCvlanCos,'raisecomUserAclSvlanCos':raisecomUserAclSvlanCos,'raisecomUserAclCvlan':raisecomUserAclCvlan,'raisecomUserAclSvlan':raisecomUserAclSvlan,'raisecomUserAclSetFlag':raisecomUserAclSetFlag,'raisecomUserAclSourceMacMask':raisecomUserAclSourceMacMask,'raisecomUserAclDestinationMacMask':raisecomUserAclDestinationMacMask,'raisecomUserAclCos':raisecomUserAclCos,'raisecomUserAclArpType':raisecomUserAclArpType,'raisecomUserAclArpSenderMac':raisecomUserAclArpSenderMac,'raisecomUserAclArpTargetMac':raisecomUserAclArpTargetMac,'raisecomUserAclIcmpIgmpType':raisecomUserAclIcmpIgmpType,'raisecomUserAclIcmpCode':raisecomUserAclIcmpCode,'raisecomUserAclIpv6SourceAddress':raisecomUserAclIpv6SourceAddress,'raisecomUserAclIpv6SourceMask':raisecomUserAclIpv6SourceMask,'raisecomUserAclIpv6DestinationAddress':raisecomUserAclIpv6DestinationAddress,'raisecomUserAclIpv6DestinationMask':raisecomUserAclIpv6DestinationMask,'raisecomUserAclIpv6SourceMaskLen':raisecomUserAclIpv6SourceMaskLen,'raisecomUserAclIpv6DestinationMaskLen':raisecomUserAclIpv6DestinationMaskLen,'raisecomUserAclIpv6Protocol':raisecomUserAclIpv6Protocol,'raisecomUserAclIpv6FlowLabel':raisecomUserAclIpv6FlowLabel,'raisecomUserAclIpv6TrafficClass':raisecomUserAclIpv6TrafficClass,'raisecomUserAclIcmpv6Type':raisecomUserAclIcmpv6Type,'raisecomUserAclUserLen':raisecomUserAclUserLen,'raisecomUserAclExtensionSetFlag':raisecomUserAclExtensionSetFlag,'raisecomUserAclTunnelLabel':raisecomUserAclTunnelLabel,'raisecomUserAclTunnelExp':raisecomUserAclTunnelExp,'raisecomUserAclVcLabel':raisecomUserAclVcLabel,'raisecomUserAclVcExp':raisecomUserAclVcExp,'raisecomIpv6AccessList':raisecomIpv6AccessList,'raisecomIpv6AclTable':raisecomIpv6AclTable,'raisecomIpv6AclEntry':raisecomIpv6AclEntry,_M:raisecomIpv6AclNumber,'raisecomIpv6AclAccessType':raisecomIpv6AclAccessType,'raisecomIpv6AclProtocol':raisecomIpv6AclProtocol,'raisecomIpv6AclSourceAddress':raisecomIpv6AclSourceAddress,'raisecomIpv6AclSourcePrefixLen':raisecomIpv6AclSourcePrefixLen,'raisecomIpv6AclDestinationAddress':raisecomIpv6AclDestinationAddress,'raisecomIpv6AclDestinationPrefixLen':raisecomIpv6AclDestinationPrefixLen,'raisecomIpv6AclTrafficClass':raisecomIpv6AclTrafficClass,'raisecomIpv6AclFlowLabel':raisecomIpv6AclFlowLabel,'raisecomIpv6AclRef':raisecomIpv6AclRef,'raisecomIpv6AclStatus':raisecomIpv6AclStatus,'raisecomIpv6AclSourceProtocolPort':raisecomIpv6AclSourceProtocolPort,'raisecomIpv6AclDestinationProtocolPort':raisecomIpv6AclDestinationProtocolPort,'raisecomIpv6AclSetFlag':raisecomIpv6AclSetFlag})