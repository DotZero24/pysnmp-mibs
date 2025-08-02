_K='ipv6AclFilterSequenceNumber'
_J='ipAclFilterSequenceNumber'
_I='macAclFilterSequenceNumber'
_H='ipv6AclNumber'
_G='ipAclNumber'
_F='macAclNumber'
_E='not-accessible'
_D='Unsigned32'
_C='IPI-ACL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipi,=mibBuilder.importSymbols('OCNOS-IPI-MODULE-MIB','ipi')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipiACLMib=ModuleIdentity((1,3,6,1,4,1,36673,106))
_IpiAclObjects_ObjectIdentity=ObjectIdentity
ipiAclObjects=_IpiAclObjects_ObjectIdentity((1,3,6,1,4,1,36673,106,1))
_IpiMacACLTable_Object=MibTable
ipiMacACLTable=_IpiMacACLTable_Object((1,3,6,1,4,1,36673,106,1,1))
if mibBuilder.loadTexts:ipiMacACLTable.setStatus(_A)
_IpiMacACLEntry_Object=MibTableRow
ipiMacACLEntry=_IpiMacACLEntry_Object((1,3,6,1,4,1,36673,106,1,1,1))
ipiMacACLEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ipiMacACLEntry.setStatus(_A)
class _MacAclNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MacAclNumber_Type.__name__=_D
_MacAclNumber_Object=MibTableColumn
macAclNumber=_MacAclNumber_Object((1,3,6,1,4,1,36673,106,1,1,1,1),_MacAclNumber_Type())
macAclNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:macAclNumber.setStatus(_A)
_MacACLName_Type=DisplayString
_MacACLName_Object=MibTableColumn
macACLName=_MacACLName_Object((1,3,6,1,4,1,36673,106,1,1,1,2),_MacACLName_Type())
macACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:macACLName.setStatus(_A)
_MacACLFilterCount_Type=Unsigned32
_MacACLFilterCount_Object=MibTableColumn
macACLFilterCount=_MacACLFilterCount_Object((1,3,6,1,4,1,36673,106,1,1,1,3),_MacACLFilterCount_Type())
macACLFilterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:macACLFilterCount.setStatus(_A)
_MacACLDefaultFilterMatchPkts_Type=Counter64
_MacACLDefaultFilterMatchPkts_Object=MibTableColumn
macACLDefaultFilterMatchPkts=_MacACLDefaultFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,1,1,4),_MacACLDefaultFilterMatchPkts_Type())
macACLDefaultFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:macACLDefaultFilterMatchPkts.setStatus(_A)
_IpiMacACLFilterTable_Object=MibTable
ipiMacACLFilterTable=_IpiMacACLFilterTable_Object((1,3,6,1,4,1,36673,106,1,2))
if mibBuilder.loadTexts:ipiMacACLFilterTable.setStatus(_A)
_IpiMacACLFilterEntry_Object=MibTableRow
ipiMacACLFilterEntry=_IpiMacACLFilterEntry_Object((1,3,6,1,4,1,36673,106,1,2,1))
ipiMacACLFilterEntry.setIndexNames((0,_C,_F),(0,_C,_I))
if mibBuilder.loadTexts:ipiMacACLFilterEntry.setStatus(_A)
class _MacAclFilterSequenceNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MacAclFilterSequenceNumber_Type.__name__=_D
_MacAclFilterSequenceNumber_Object=MibTableColumn
macAclFilterSequenceNumber=_MacAclFilterSequenceNumber_Object((1,3,6,1,4,1,36673,106,1,2,1,1),_MacAclFilterSequenceNumber_Type())
macAclFilterSequenceNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:macAclFilterSequenceNumber.setStatus(_A)
_MacACLFilterMatchPkts_Type=Counter64
_MacACLFilterMatchPkts_Object=MibTableColumn
macACLFilterMatchPkts=_MacACLFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,2,1,2),_MacACLFilterMatchPkts_Type())
macACLFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:macACLFilterMatchPkts.setStatus(_A)
_IpiIpACLTable_Object=MibTable
ipiIpACLTable=_IpiIpACLTable_Object((1,3,6,1,4,1,36673,106,1,3))
if mibBuilder.loadTexts:ipiIpACLTable.setStatus(_A)
_IpiIpACLEntry_Object=MibTableRow
ipiIpACLEntry=_IpiIpACLEntry_Object((1,3,6,1,4,1,36673,106,1,3,1))
ipiIpACLEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:ipiIpACLEntry.setStatus(_A)
class _IpAclNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpAclNumber_Type.__name__=_D
_IpAclNumber_Object=MibTableColumn
ipAclNumber=_IpAclNumber_Object((1,3,6,1,4,1,36673,106,1,3,1,1),_IpAclNumber_Type())
ipAclNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ipAclNumber.setStatus(_A)
_IpACLName_Type=DisplayString
_IpACLName_Object=MibTableColumn
ipACLName=_IpACLName_Object((1,3,6,1,4,1,36673,106,1,3,1,2),_IpACLName_Type())
ipACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipACLName.setStatus(_A)
_IpACLFilterCount_Type=Unsigned32
_IpACLFilterCount_Object=MibTableColumn
ipACLFilterCount=_IpACLFilterCount_Object((1,3,6,1,4,1,36673,106,1,3,1,3),_IpACLFilterCount_Type())
ipACLFilterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipACLFilterCount.setStatus(_A)
_IpACLDefaultFilterMatchPkts_Type=Counter64
_IpACLDefaultFilterMatchPkts_Object=MibTableColumn
ipACLDefaultFilterMatchPkts=_IpACLDefaultFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,3,1,4),_IpACLDefaultFilterMatchPkts_Type())
ipACLDefaultFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipACLDefaultFilterMatchPkts.setStatus(_A)
_IpiIpACLFilterTable_Object=MibTable
ipiIpACLFilterTable=_IpiIpACLFilterTable_Object((1,3,6,1,4,1,36673,106,1,4))
if mibBuilder.loadTexts:ipiIpACLFilterTable.setStatus(_A)
_IpiIpACLFilterEntry_Object=MibTableRow
ipiIpACLFilterEntry=_IpiIpACLFilterEntry_Object((1,3,6,1,4,1,36673,106,1,4,1))
ipiIpACLFilterEntry.setIndexNames((0,_C,_G),(0,_C,_J))
if mibBuilder.loadTexts:ipiIpACLFilterEntry.setStatus(_A)
class _IpAclFilterSequenceNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_IpAclFilterSequenceNumber_Type.__name__=_D
_IpAclFilterSequenceNumber_Object=MibTableColumn
ipAclFilterSequenceNumber=_IpAclFilterSequenceNumber_Object((1,3,6,1,4,1,36673,106,1,4,1,1),_IpAclFilterSequenceNumber_Type())
ipAclFilterSequenceNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ipAclFilterSequenceNumber.setStatus(_A)
_IpACLFilterMatchPkts_Type=Counter64
_IpACLFilterMatchPkts_Object=MibTableColumn
ipACLFilterMatchPkts=_IpACLFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,4,1,2),_IpACLFilterMatchPkts_Type())
ipACLFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipACLFilterMatchPkts.setStatus(_A)
_IpiIpv6ACLTable_Object=MibTable
ipiIpv6ACLTable=_IpiIpv6ACLTable_Object((1,3,6,1,4,1,36673,106,1,5))
if mibBuilder.loadTexts:ipiIpv6ACLTable.setStatus(_A)
_IpiIpv6ACLEntry_Object=MibTableRow
ipiIpv6ACLEntry=_IpiIpv6ACLEntry_Object((1,3,6,1,4,1,36673,106,1,5,1))
ipiIpv6ACLEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:ipiIpv6ACLEntry.setStatus(_A)
class _Ipv6AclNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ipv6AclNumber_Type.__name__=_D
_Ipv6AclNumber_Object=MibTableColumn
ipv6AclNumber=_Ipv6AclNumber_Object((1,3,6,1,4,1,36673,106,1,5,1,1),_Ipv6AclNumber_Type())
ipv6AclNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6AclNumber.setStatus(_A)
_Ipv6ACLName_Type=DisplayString
_Ipv6ACLName_Object=MibTableColumn
ipv6ACLName=_Ipv6ACLName_Object((1,3,6,1,4,1,36673,106,1,5,1,2),_Ipv6ACLName_Type())
ipv6ACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6ACLName.setStatus(_A)
_Ipv6ACLFilterCount_Type=Unsigned32
_Ipv6ACLFilterCount_Object=MibTableColumn
ipv6ACLFilterCount=_Ipv6ACLFilterCount_Object((1,3,6,1,4,1,36673,106,1,5,1,3),_Ipv6ACLFilterCount_Type())
ipv6ACLFilterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6ACLFilterCount.setStatus(_A)
_Ipv6ACLDefaultFilterMatchPkts_Type=Counter64
_Ipv6ACLDefaultFilterMatchPkts_Object=MibTableColumn
ipv6ACLDefaultFilterMatchPkts=_Ipv6ACLDefaultFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,5,1,4),_Ipv6ACLDefaultFilterMatchPkts_Type())
ipv6ACLDefaultFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6ACLDefaultFilterMatchPkts.setStatus(_A)
_IpiIpv6ACLFilterTable_Object=MibTable
ipiIpv6ACLFilterTable=_IpiIpv6ACLFilterTable_Object((1,3,6,1,4,1,36673,106,1,6))
if mibBuilder.loadTexts:ipiIpv6ACLFilterTable.setStatus(_A)
_IpiIpv6ACLFilterEntry_Object=MibTableRow
ipiIpv6ACLFilterEntry=_IpiIpv6ACLFilterEntry_Object((1,3,6,1,4,1,36673,106,1,6,1))
ipiIpv6ACLFilterEntry.setIndexNames((0,_C,_H),(0,_C,_K))
if mibBuilder.loadTexts:ipiIpv6ACLFilterEntry.setStatus(_A)
class _Ipv6AclFilterSequenceNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Ipv6AclFilterSequenceNumber_Type.__name__=_D
_Ipv6AclFilterSequenceNumber_Object=MibTableColumn
ipv6AclFilterSequenceNumber=_Ipv6AclFilterSequenceNumber_Object((1,3,6,1,4,1,36673,106,1,6,1,1),_Ipv6AclFilterSequenceNumber_Type())
ipv6AclFilterSequenceNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ipv6AclFilterSequenceNumber.setStatus(_A)
_Ipv6ACLFilterMatchPkts_Type=Counter64
_Ipv6ACLFilterMatchPkts_Object=MibTableColumn
ipv6ACLFilterMatchPkts=_Ipv6ACLFilterMatchPkts_Object((1,3,6,1,4,1,36673,106,1,6,1,2),_Ipv6ACLFilterMatchPkts_Type())
ipv6ACLFilterMatchPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6ACLFilterMatchPkts.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ipiACLMib':ipiACLMib,'ipiAclObjects':ipiAclObjects,'ipiMacACLTable':ipiMacACLTable,'ipiMacACLEntry':ipiMacACLEntry,_F:macAclNumber,'macACLName':macACLName,'macACLFilterCount':macACLFilterCount,'macACLDefaultFilterMatchPkts':macACLDefaultFilterMatchPkts,'ipiMacACLFilterTable':ipiMacACLFilterTable,'ipiMacACLFilterEntry':ipiMacACLFilterEntry,_I:macAclFilterSequenceNumber,'macACLFilterMatchPkts':macACLFilterMatchPkts,'ipiIpACLTable':ipiIpACLTable,'ipiIpACLEntry':ipiIpACLEntry,_G:ipAclNumber,'ipACLName':ipACLName,'ipACLFilterCount':ipACLFilterCount,'ipACLDefaultFilterMatchPkts':ipACLDefaultFilterMatchPkts,'ipiIpACLFilterTable':ipiIpACLFilterTable,'ipiIpACLFilterEntry':ipiIpACLFilterEntry,_J:ipAclFilterSequenceNumber,'ipACLFilterMatchPkts':ipACLFilterMatchPkts,'ipiIpv6ACLTable':ipiIpv6ACLTable,'ipiIpv6ACLEntry':ipiIpv6ACLEntry,_H:ipv6AclNumber,'ipv6ACLName':ipv6ACLName,'ipv6ACLFilterCount':ipv6ACLFilterCount,'ipv6ACLDefaultFilterMatchPkts':ipv6ACLDefaultFilterMatchPkts,'ipiIpv6ACLFilterTable':ipiIpv6ACLFilterTable,'ipiIpv6ACLFilterEntry':ipiIpv6ACLFilterEntry,_K:ipv6AclFilterSequenceNumber,'ipv6ACLFilterMatchPkts':ipv6ACLFilterMatchPkts})