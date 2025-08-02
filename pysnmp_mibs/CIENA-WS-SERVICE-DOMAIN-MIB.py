_N='cienaWsServiceDomainGroup'
_M='cwsServiceDomainServiceDomainIdDescription'
_L='cwsServiceDomainServiceDomainIdName'
_K='cwsServiceDomainServiceMembersTableSnmpKey'
_J='cwsServiceDomainPortMembersTableSnmpKey'
_I='read-write'
_H='cwsServiceDomainServiceDomainIdTableSnmpKey'
_G='not-accessible'
_F='cwsServiceDomainLinkedReferencesTableSnmpKey'
_E='read-only'
_D='cwsServiceDomainServiceDomainsServiceDomainIndex'
_C='Integer32'
_B='CIENA-WS-SERVICE-DOMAIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
DescriptionString,NameString,PortId,ServiceDomainIdx,ServiceIdx=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','DescriptionString','NameString','PortId','ServiceDomainIdx','ServiceIdx')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaWsServiceDomainMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,11))
if mibBuilder.loadTexts:cienaWsServiceDomainMIB.setRevisions(('2017-03-02 00:00','2016-12-12 00:00','2015-06-17 00:00','2015-04-15 00:00'))
_CienaWsServiceDomainObjects_ObjectIdentity=ObjectIdentity
cienaWsServiceDomainObjects=_CienaWsServiceDomainObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,11,1))
_CienaWsServiceDomainConformance_ObjectIdentity=ObjectIdentity
cienaWsServiceDomainConformance=_CienaWsServiceDomainConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,11,2))
_CienaWsServiceDomainGroups_ObjectIdentity=ObjectIdentity
cienaWsServiceDomainGroups=_CienaWsServiceDomainGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,11,2,1))
_CienaWsServiceDomainCompliances_ObjectIdentity=ObjectIdentity
cienaWsServiceDomainCompliances=_CienaWsServiceDomainCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,11,2,2))
_CwsServiceDomainServiceDomainsTable_Object=MibTable
cwsServiceDomainServiceDomainsTable=_CwsServiceDomainServiceDomainsTable_Object((1,3,6,1,4,1,1271,3,4,11,3))
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainsTable.setStatus(_A)
_CwsServiceDomainServiceDomainsEntry_Object=MibTableRow
cwsServiceDomainServiceDomainsEntry=_CwsServiceDomainServiceDomainsEntry_Object((1,3,6,1,4,1,1271,3,4,11,3,1))
cwsServiceDomainServiceDomainsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainsEntry.setStatus(_A)
class _CwsServiceDomainServiceDomainsServiceDomainIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceDomainServiceDomainsServiceDomainIndex_Type.__name__=_C
_CwsServiceDomainServiceDomainsServiceDomainIndex_Object=MibTableColumn
cwsServiceDomainServiceDomainsServiceDomainIndex=_CwsServiceDomainServiceDomainsServiceDomainIndex_Object((1,3,6,1,4,1,1271,3,4,11,3,1,1),_CwsServiceDomainServiceDomainsServiceDomainIndex_Type())
cwsServiceDomainServiceDomainsServiceDomainIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainsServiceDomainIndex.setStatus(_A)
_CwsServiceDomainServiceDomainIdTable_Object=MibTable
cwsServiceDomainServiceDomainIdTable=_CwsServiceDomainServiceDomainIdTable_Object((1,3,6,1,4,1,1271,3,4,11,4))
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainIdTable.setStatus(_A)
_CwsServiceDomainServiceDomainIdEntry_Object=MibTableRow
cwsServiceDomainServiceDomainIdEntry=_CwsServiceDomainServiceDomainIdEntry_Object((1,3,6,1,4,1,1271,3,4,11,4,1))
cwsServiceDomainServiceDomainIdEntry.setIndexNames((0,_B,_D),(0,_B,_H))
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainIdEntry.setStatus(_A)
class _CwsServiceDomainServiceDomainIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceDomainServiceDomainIdTableSnmpKey_Type.__name__=_C
_CwsServiceDomainServiceDomainIdTableSnmpKey_Object=MibTableColumn
cwsServiceDomainServiceDomainIdTableSnmpKey=_CwsServiceDomainServiceDomainIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,11,4,1,1),_CwsServiceDomainServiceDomainIdTableSnmpKey_Type())
cwsServiceDomainServiceDomainIdTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainIdTableSnmpKey.setStatus(_A)
_CwsServiceDomainServiceDomainIdName_Type=NameString
_CwsServiceDomainServiceDomainIdName_Object=MibTableColumn
cwsServiceDomainServiceDomainIdName=_CwsServiceDomainServiceDomainIdName_Object((1,3,6,1,4,1,1271,3,4,11,4,1,2),_CwsServiceDomainServiceDomainIdName_Type())
cwsServiceDomainServiceDomainIdName.setMaxAccess(_I)
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainIdName.setStatus(_A)
_CwsServiceDomainServiceDomainIdDescription_Type=DescriptionString
_CwsServiceDomainServiceDomainIdDescription_Object=MibTableColumn
cwsServiceDomainServiceDomainIdDescription=_CwsServiceDomainServiceDomainIdDescription_Object((1,3,6,1,4,1,1271,3,4,11,4,1,3),_CwsServiceDomainServiceDomainIdDescription_Type())
cwsServiceDomainServiceDomainIdDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:cwsServiceDomainServiceDomainIdDescription.setStatus(_A)
_CwsServiceDomainPortMembersTable_Object=MibTable
cwsServiceDomainPortMembersTable=_CwsServiceDomainPortMembersTable_Object((1,3,6,1,4,1,1271,3,4,11,5))
if mibBuilder.loadTexts:cwsServiceDomainPortMembersTable.setStatus(_A)
_CwsServiceDomainPortMembersEntry_Object=MibTableRow
cwsServiceDomainPortMembersEntry=_CwsServiceDomainPortMembersEntry_Object((1,3,6,1,4,1,1271,3,4,11,5,1))
cwsServiceDomainPortMembersEntry.setIndexNames((0,_B,_D),(0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:cwsServiceDomainPortMembersEntry.setStatus(_A)
class _CwsServiceDomainPortMembersTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceDomainPortMembersTableSnmpKey_Type.__name__=_C
_CwsServiceDomainPortMembersTableSnmpKey_Object=MibTableColumn
cwsServiceDomainPortMembersTableSnmpKey=_CwsServiceDomainPortMembersTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,11,5,1,1),_CwsServiceDomainPortMembersTableSnmpKey_Type())
cwsServiceDomainPortMembersTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServiceDomainPortMembersTableSnmpKey.setStatus(_A)
_CwsServiceDomainPortMembers_Type=PortId
_CwsServiceDomainPortMembers_Object=MibTableColumn
cwsServiceDomainPortMembers=_CwsServiceDomainPortMembers_Object((1,3,6,1,4,1,1271,3,4,11,5,1,2),_CwsServiceDomainPortMembers_Type())
cwsServiceDomainPortMembers.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsServiceDomainPortMembers.setStatus(_A)
_CwsServiceDomainLinkedReferencesTable_Object=MibTable
cwsServiceDomainLinkedReferencesTable=_CwsServiceDomainLinkedReferencesTable_Object((1,3,6,1,4,1,1271,3,4,11,6))
if mibBuilder.loadTexts:cwsServiceDomainLinkedReferencesTable.setStatus(_A)
_CwsServiceDomainLinkedReferencesEntry_Object=MibTableRow
cwsServiceDomainLinkedReferencesEntry=_CwsServiceDomainLinkedReferencesEntry_Object((1,3,6,1,4,1,1271,3,4,11,6,1))
cwsServiceDomainLinkedReferencesEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cwsServiceDomainLinkedReferencesEntry.setStatus(_A)
class _CwsServiceDomainLinkedReferencesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceDomainLinkedReferencesTableSnmpKey_Type.__name__=_C
_CwsServiceDomainLinkedReferencesTableSnmpKey_Object=MibTableColumn
cwsServiceDomainLinkedReferencesTableSnmpKey=_CwsServiceDomainLinkedReferencesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,11,6,1,1),_CwsServiceDomainLinkedReferencesTableSnmpKey_Type())
cwsServiceDomainLinkedReferencesTableSnmpKey.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsServiceDomainLinkedReferencesTableSnmpKey.setStatus(_A)
_CwsServiceDomainServiceMembersTable_Object=MibTable
cwsServiceDomainServiceMembersTable=_CwsServiceDomainServiceMembersTable_Object((1,3,6,1,4,1,1271,3,4,11,7))
if mibBuilder.loadTexts:cwsServiceDomainServiceMembersTable.setStatus(_A)
_CwsServiceDomainServiceMembersEntry_Object=MibTableRow
cwsServiceDomainServiceMembersEntry=_CwsServiceDomainServiceMembersEntry_Object((1,3,6,1,4,1,1271,3,4,11,7,1))
cwsServiceDomainServiceMembersEntry.setIndexNames((0,_B,_D),(0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:cwsServiceDomainServiceMembersEntry.setStatus(_A)
class _CwsServiceDomainServiceMembersTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsServiceDomainServiceMembersTableSnmpKey_Type.__name__=_C
_CwsServiceDomainServiceMembersTableSnmpKey_Object=MibTableColumn
cwsServiceDomainServiceMembersTableSnmpKey=_CwsServiceDomainServiceMembersTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,11,7,1,1),_CwsServiceDomainServiceMembersTableSnmpKey_Type())
cwsServiceDomainServiceMembersTableSnmpKey.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsServiceDomainServiceMembersTableSnmpKey.setStatus(_A)
_CwsServiceDomainServiceMembers_Type=ServiceIdx
_CwsServiceDomainServiceMembers_Object=MibTableColumn
cwsServiceDomainServiceMembers=_CwsServiceDomainServiceMembers_Object((1,3,6,1,4,1,1271,3,4,11,7,1,2),_CwsServiceDomainServiceMembers_Type())
cwsServiceDomainServiceMembers.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsServiceDomainServiceMembers.setStatus(_A)
cienaWsServiceDomainGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,11,2,1,1))
cienaWsServiceDomainGroup.setObjects(*((_B,_D),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cienaWsServiceDomainGroup.setStatus(_A)
cienaWsServiceDomainCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,11,2,2,1))
cienaWsServiceDomainCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:cienaWsServiceDomainCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaWsServiceDomainMIB':cienaWsServiceDomainMIB,'cienaWsServiceDomainObjects':cienaWsServiceDomainObjects,'cienaWsServiceDomainConformance':cienaWsServiceDomainConformance,'cienaWsServiceDomainGroups':cienaWsServiceDomainGroups,_N:cienaWsServiceDomainGroup,'cienaWsServiceDomainCompliances':cienaWsServiceDomainCompliances,'cienaWsServiceDomainCompliance':cienaWsServiceDomainCompliance,'cwsServiceDomainServiceDomainsTable':cwsServiceDomainServiceDomainsTable,'cwsServiceDomainServiceDomainsEntry':cwsServiceDomainServiceDomainsEntry,_D:cwsServiceDomainServiceDomainsServiceDomainIndex,'cwsServiceDomainServiceDomainIdTable':cwsServiceDomainServiceDomainIdTable,'cwsServiceDomainServiceDomainIdEntry':cwsServiceDomainServiceDomainIdEntry,_H:cwsServiceDomainServiceDomainIdTableSnmpKey,_L:cwsServiceDomainServiceDomainIdName,_M:cwsServiceDomainServiceDomainIdDescription,'cwsServiceDomainPortMembersTable':cwsServiceDomainPortMembersTable,'cwsServiceDomainPortMembersEntry':cwsServiceDomainPortMembersEntry,_J:cwsServiceDomainPortMembersTableSnmpKey,'cwsServiceDomainPortMembers':cwsServiceDomainPortMembers,'cwsServiceDomainLinkedReferencesTable':cwsServiceDomainLinkedReferencesTable,'cwsServiceDomainLinkedReferencesEntry':cwsServiceDomainLinkedReferencesEntry,_F:cwsServiceDomainLinkedReferencesTableSnmpKey,'cwsServiceDomainServiceMembersTable':cwsServiceDomainServiceMembersTable,'cwsServiceDomainServiceMembersEntry':cwsServiceDomainServiceMembersEntry,_K:cwsServiceDomainServiceMembersTableSnmpKey,'cwsServiceDomainServiceMembers':cwsServiceDomainServiceMembers})