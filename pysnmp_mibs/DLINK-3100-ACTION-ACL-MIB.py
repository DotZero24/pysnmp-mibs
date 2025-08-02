_H='read-only'
_G='rlPorts2AclsMappingPortIndex'
_F='not-accessible'
_E='rlActionAclAclIndex'
_D='DLINK-3100-ACTION-ACL-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rlActionAcl=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,130))
if mibBuilder.loadTexts:rlActionAcl.setRevisions(('2007-11-18 00:00',))
class ClassMapAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('none',1),('setIP-Precedence',2),('setDSCP',3),('setQueue',4),('setCos',5),('trustCos',6),('trustDSCP',7),('trustTCP-UDPport',8),('trustCosDscp',9)))
_RlActionAclTable_Object=MibTable
rlActionAclTable=_RlActionAclTable_Object((1,3,6,1,4,1,171,10,94,89,89,130,1))
if mibBuilder.loadTexts:rlActionAclTable.setStatus(_A)
_RlActionAclEntry_Object=MibTableRow
rlActionAclEntry=_RlActionAclEntry_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1))
rlActionAclEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlActionAclEntry.setStatus(_A)
class _RlActionAclAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_RlActionAclAclIndex_Type.__name__=_C
_RlActionAclAclIndex_Object=MibTableColumn
rlActionAclAclIndex=_RlActionAclAclIndex_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,1),_RlActionAclAclIndex_Type())
rlActionAclAclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlActionAclAclIndex.setStatus(_A)
_RlActionAclPorts_Type=PortList
_RlActionAclPorts_Object=MibTableColumn
rlActionAclPorts=_RlActionAclPorts_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,2),_RlActionAclPorts_Type())
rlActionAclPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclPorts.setStatus(_A)
_RlActionAclClassMapAction_Type=ClassMapAction
_RlActionAclClassMapAction_Object=MibTableColumn
rlActionAclClassMapAction=_RlActionAclClassMapAction_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,3),_RlActionAclClassMapAction_Type())
rlActionAclClassMapAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclClassMapAction.setStatus(_A)
_RlActionAclClassMapMarkValue_Type=Integer32
_RlActionAclClassMapMarkValue_Object=MibTableColumn
rlActionAclClassMapMarkValue=_RlActionAclClassMapMarkValue_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,4),_RlActionAclClassMapMarkValue_Type())
rlActionAclClassMapMarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclClassMapMarkValue.setStatus(_A)
_RlActionAclPolicerIndex_Type=Integer32
_RlActionAclPolicerIndex_Object=MibTableColumn
rlActionAclPolicerIndex=_RlActionAclPolicerIndex_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,5),_RlActionAclPolicerIndex_Type())
rlActionAclPolicerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclPolicerIndex.setStatus(_A)
_RlActionAclStatus_Type=RowStatus
_RlActionAclStatus_Object=MibTableColumn
rlActionAclStatus=_RlActionAclStatus_Object((1,3,6,1,4,1,171,10,94,89,89,130,1,1,6),_RlActionAclStatus_Type())
rlActionAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclStatus.setStatus(_A)
_RlPort2AclsMappingTable_Object=MibTable
rlPort2AclsMappingTable=_RlPort2AclsMappingTable_Object((1,3,6,1,4,1,171,10,94,89,89,130,2))
if mibBuilder.loadTexts:rlPort2AclsMappingTable.setStatus(_A)
_RlPort2AclsMappingEntry_Object=MibTableRow
rlPort2AclsMappingEntry=_RlPort2AclsMappingEntry_Object((1,3,6,1,4,1,171,10,94,89,89,130,2,1))
rlPort2AclsMappingEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:rlPort2AclsMappingEntry.setStatus(_A)
_RlPorts2AclsMappingPortIndex_Type=Integer32
_RlPorts2AclsMappingPortIndex_Object=MibTableColumn
rlPorts2AclsMappingPortIndex=_RlPorts2AclsMappingPortIndex_Object((1,3,6,1,4,1,171,10,94,89,89,130,2,1,1),_RlPorts2AclsMappingPortIndex_Type())
rlPorts2AclsMappingPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlPorts2AclsMappingPortIndex.setStatus(_A)
_RlPorts2AclsMappingPortAcls_Type=PortList
_RlPorts2AclsMappingPortAcls_Object=MibTableColumn
rlPorts2AclsMappingPortAcls=_RlPorts2AclsMappingPortAcls_Object((1,3,6,1,4,1,171,10,94,89,89,130,2,1,2),_RlPorts2AclsMappingPortAcls_Type())
rlPorts2AclsMappingPortAcls.setMaxAccess(_H)
if mibBuilder.loadTexts:rlPorts2AclsMappingPortAcls.setStatus(_A)
class _RlActionAclDeleteProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RlActionAclDeleteProfileIndex_Type.__name__=_C
_RlActionAclDeleteProfileIndex_Object=MibScalar
rlActionAclDeleteProfileIndex=_RlActionAclDeleteProfileIndex_Object((1,3,6,1,4,1,171,10,94,89,89,130,3),_RlActionAclDeleteProfileIndex_Type())
rlActionAclDeleteProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlActionAclDeleteProfileIndex.setStatus(_A)
_RlNumOfUsedTcamAces_Type=Integer32
_RlNumOfUsedTcamAces_Object=MibScalar
rlNumOfUsedTcamAces=_RlNumOfUsedTcamAces_Object((1,3,6,1,4,1,171,10,94,89,89,130,4),_RlNumOfUsedTcamAces_Type())
rlNumOfUsedTcamAces.setMaxAccess(_H)
if mibBuilder.loadTexts:rlNumOfUsedTcamAces.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ClassMapAction':ClassMapAction,'rlActionAcl':rlActionAcl,'rlActionAclTable':rlActionAclTable,'rlActionAclEntry':rlActionAclEntry,_E:rlActionAclAclIndex,'rlActionAclPorts':rlActionAclPorts,'rlActionAclClassMapAction':rlActionAclClassMapAction,'rlActionAclClassMapMarkValue':rlActionAclClassMapMarkValue,'rlActionAclPolicerIndex':rlActionAclPolicerIndex,'rlActionAclStatus':rlActionAclStatus,'rlPort2AclsMappingTable':rlPort2AclsMappingTable,'rlPort2AclsMappingEntry':rlPort2AclsMappingEntry,_G:rlPorts2AclsMappingPortIndex,'rlPorts2AclsMappingPortAcls':rlPorts2AclsMappingPortAcls,'rlActionAclDeleteProfileIndex':rlActionAclDeleteProfileIndex,'rlNumOfUsedTcamAces':rlNumOfUsedTcamAces})