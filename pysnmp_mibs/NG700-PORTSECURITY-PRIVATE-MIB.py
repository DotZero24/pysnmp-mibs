_M='agentPortSecurityLastDiscardedMAC'
_L='agentPortSecurityDynamicMACAddress'
_K='agentPortSecurityDynamicVLANId'
_J='Unsigned32'
_I='NG700-PORTSECURITY-PRIVATE-MIB'
_H='read-only'
_G='ifIndex'
_F='IF-MIB'
_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ng700smartswitch,=mibBuilder.importSymbols('NG700-REF-MIB','ng700smartswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathPortSecurity=ModuleIdentity((1,3,6,1,4,1,4526,11,20))
if mibBuilder.loadTexts:fastPathPortSecurity.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentPortSecurityGroup_ObjectIdentity=ObjectIdentity
agentPortSecurityGroup=_AgentPortSecurityGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,20,1))
class _AgentGlobalPortSecurityMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentGlobalPortSecurityMode_Type.__name__=_C
_AgentGlobalPortSecurityMode_Object=MibScalar
agentGlobalPortSecurityMode=_AgentGlobalPortSecurityMode_Object((1,3,6,1,4,1,4526,11,20,1,1),_AgentGlobalPortSecurityMode_Type())
agentGlobalPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentGlobalPortSecurityMode.setStatus(_A)
_AgentPortSecurityTable_Object=MibTable
agentPortSecurityTable=_AgentPortSecurityTable_Object((1,3,6,1,4,1,4526,11,20,1,2))
if mibBuilder.loadTexts:agentPortSecurityTable.setStatus(_A)
_AgentPortSecurityEntry_Object=MibTableRow
agentPortSecurityEntry=_AgentPortSecurityEntry_Object((1,3,6,1,4,1,4526,11,20,1,2,1))
agentPortSecurityEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:agentPortSecurityEntry.setStatus(_A)
class _AgentPortSecurityMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentPortSecurityMode_Type.__name__=_C
_AgentPortSecurityMode_Object=MibTableColumn
agentPortSecurityMode=_AgentPortSecurityMode_Object((1,3,6,1,4,1,4526,11,20,1,2,1,1),_AgentPortSecurityMode_Type())
agentPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityMode.setStatus(_A)
class _AgentPortSecurityDynamicLimit_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_AgentPortSecurityDynamicLimit_Type.__name__=_J
_AgentPortSecurityDynamicLimit_Object=MibTableColumn
agentPortSecurityDynamicLimit=_AgentPortSecurityDynamicLimit_Object((1,3,6,1,4,1,4526,11,20,1,2,1,2),_AgentPortSecurityDynamicLimit_Type())
agentPortSecurityDynamicLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityDynamicLimit.setStatus(_A)
class _AgentPortSecurityStaticLimit_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_AgentPortSecurityStaticLimit_Type.__name__=_J
_AgentPortSecurityStaticLimit_Object=MibTableColumn
agentPortSecurityStaticLimit=_AgentPortSecurityStaticLimit_Object((1,3,6,1,4,1,4526,11,20,1,2,1,3),_AgentPortSecurityStaticLimit_Type())
agentPortSecurityStaticLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityStaticLimit.setStatus(_A)
class _AgentPortSecurityViolationTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentPortSecurityViolationTrapMode_Type.__name__=_C
_AgentPortSecurityViolationTrapMode_Object=MibTableColumn
agentPortSecurityViolationTrapMode=_AgentPortSecurityViolationTrapMode_Object((1,3,6,1,4,1,4526,11,20,1,2,1,4),_AgentPortSecurityViolationTrapMode_Type())
agentPortSecurityViolationTrapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityViolationTrapMode.setStatus(_A)
_AgentPortSecurityStaticMACs_Type=DisplayString
_AgentPortSecurityStaticMACs_Object=MibTableColumn
agentPortSecurityStaticMACs=_AgentPortSecurityStaticMACs_Object((1,3,6,1,4,1,4526,11,20,1,2,1,6),_AgentPortSecurityStaticMACs_Type())
agentPortSecurityStaticMACs.setMaxAccess(_H)
if mibBuilder.loadTexts:agentPortSecurityStaticMACs.setStatus(_A)
_AgentPortSecurityLastDiscardedMAC_Type=DisplayString
_AgentPortSecurityLastDiscardedMAC_Object=MibTableColumn
agentPortSecurityLastDiscardedMAC=_AgentPortSecurityLastDiscardedMAC_Object((1,3,6,1,4,1,4526,11,20,1,2,1,7),_AgentPortSecurityLastDiscardedMAC_Type())
agentPortSecurityLastDiscardedMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:agentPortSecurityLastDiscardedMAC.setStatus(_A)
_AgentPortSecurityMACAddressAdd_Type=DisplayString
_AgentPortSecurityMACAddressAdd_Object=MibTableColumn
agentPortSecurityMACAddressAdd=_AgentPortSecurityMACAddressAdd_Object((1,3,6,1,4,1,4526,11,20,1,2,1,8),_AgentPortSecurityMACAddressAdd_Type())
agentPortSecurityMACAddressAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityMACAddressAdd.setStatus(_A)
_AgentPortSecurityMACAddressRemove_Type=DisplayString
_AgentPortSecurityMACAddressRemove_Object=MibTableColumn
agentPortSecurityMACAddressRemove=_AgentPortSecurityMACAddressRemove_Object((1,3,6,1,4,1,4526,11,20,1,2,1,9),_AgentPortSecurityMACAddressRemove_Type())
agentPortSecurityMACAddressRemove.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityMACAddressRemove.setStatus(_A)
class _AgentPortSecurityMACAddressMove_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentPortSecurityMACAddressMove_Type.__name__=_C
_AgentPortSecurityMACAddressMove_Object=MibTableColumn
agentPortSecurityMACAddressMove=_AgentPortSecurityMACAddressMove_Object((1,3,6,1,4,1,4526,11,20,1,2,1,10),_AgentPortSecurityMACAddressMove_Type())
agentPortSecurityMACAddressMove.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityMACAddressMove.setStatus(_A)
class _AgentPortSecurityStickyMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentPortSecurityStickyMode_Type.__name__=_C
_AgentPortSecurityStickyMode_Object=MibTableColumn
agentPortSecurityStickyMode=_AgentPortSecurityStickyMode_Object((1,3,6,1,4,1,4526,11,20,1,2,1,11),_AgentPortSecurityStickyMode_Type())
agentPortSecurityStickyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortSecurityStickyMode.setStatus(_A)
_AgentPortSecurityDynamicTable_Object=MibTable
agentPortSecurityDynamicTable=_AgentPortSecurityDynamicTable_Object((1,3,6,1,4,1,4526,11,20,1,3))
if mibBuilder.loadTexts:agentPortSecurityDynamicTable.setStatus(_A)
_AgentPortSecurityDynamicEntry_Object=MibTableRow
agentPortSecurityDynamicEntry=_AgentPortSecurityDynamicEntry_Object((1,3,6,1,4,1,4526,11,20,1,3,1))
agentPortSecurityDynamicEntry.setIndexNames((0,_F,_G),(0,_I,_K),(0,_I,_L))
if mibBuilder.loadTexts:agentPortSecurityDynamicEntry.setStatus(_A)
_AgentPortSecurityDynamicVLANId_Type=Unsigned32
_AgentPortSecurityDynamicVLANId_Object=MibTableColumn
agentPortSecurityDynamicVLANId=_AgentPortSecurityDynamicVLANId_Object((1,3,6,1,4,1,4526,11,20,1,3,1,1),_AgentPortSecurityDynamicVLANId_Type())
agentPortSecurityDynamicVLANId.setMaxAccess(_H)
if mibBuilder.loadTexts:agentPortSecurityDynamicVLANId.setStatus(_A)
_AgentPortSecurityDynamicMACAddress_Type=MacAddress
_AgentPortSecurityDynamicMACAddress_Object=MibTableColumn
agentPortSecurityDynamicMACAddress=_AgentPortSecurityDynamicMACAddress_Object((1,3,6,1,4,1,4526,11,20,1,3,1,2),_AgentPortSecurityDynamicMACAddress_Type())
agentPortSecurityDynamicMACAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:agentPortSecurityDynamicMACAddress.setStatus(_A)
class _AgentGlobalPortSecurityStickyMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentGlobalPortSecurityStickyMode_Type.__name__=_C
_AgentGlobalPortSecurityStickyMode_Object=MibScalar
agentGlobalPortSecurityStickyMode=_AgentGlobalPortSecurityStickyMode_Object((1,3,6,1,4,1,4526,11,20,1,4),_AgentGlobalPortSecurityStickyMode_Type())
agentGlobalPortSecurityStickyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentGlobalPortSecurityStickyMode.setStatus(_A)
class _AgentGlobalPortSecurityViolationTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AgentGlobalPortSecurityViolationTrapMode_Type.__name__=_C
_AgentGlobalPortSecurityViolationTrapMode_Object=MibScalar
agentGlobalPortSecurityViolationTrapMode=_AgentGlobalPortSecurityViolationTrapMode_Object((1,3,6,1,4,1,4526,11,20,1,5),_AgentGlobalPortSecurityViolationTrapMode_Type())
agentGlobalPortSecurityViolationTrapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentGlobalPortSecurityViolationTrapMode.setStatus(_A)
_AgentPortSecurityTraps_ObjectIdentity=ObjectIdentity
agentPortSecurityTraps=_AgentPortSecurityTraps_ObjectIdentity((1,3,6,1,4,1,4526,11,20,2))
agentPortSecurityViolation=NotificationType((1,3,6,1,4,1,4526,11,20,2,1))
agentPortSecurityViolation.setObjects(*((_F,_G),(_I,_M)))
if mibBuilder.loadTexts:agentPortSecurityViolation.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'fastPathPortSecurity':fastPathPortSecurity,'agentPortSecurityGroup':agentPortSecurityGroup,'agentGlobalPortSecurityMode':agentGlobalPortSecurityMode,'agentPortSecurityTable':agentPortSecurityTable,'agentPortSecurityEntry':agentPortSecurityEntry,'agentPortSecurityMode':agentPortSecurityMode,'agentPortSecurityDynamicLimit':agentPortSecurityDynamicLimit,'agentPortSecurityStaticLimit':agentPortSecurityStaticLimit,'agentPortSecurityViolationTrapMode':agentPortSecurityViolationTrapMode,'agentPortSecurityStaticMACs':agentPortSecurityStaticMACs,_M:agentPortSecurityLastDiscardedMAC,'agentPortSecurityMACAddressAdd':agentPortSecurityMACAddressAdd,'agentPortSecurityMACAddressRemove':agentPortSecurityMACAddressRemove,'agentPortSecurityMACAddressMove':agentPortSecurityMACAddressMove,'agentPortSecurityStickyMode':agentPortSecurityStickyMode,'agentPortSecurityDynamicTable':agentPortSecurityDynamicTable,'agentPortSecurityDynamicEntry':agentPortSecurityDynamicEntry,_K:agentPortSecurityDynamicVLANId,_L:agentPortSecurityDynamicMACAddress,'agentGlobalPortSecurityStickyMode':agentGlobalPortSecurityStickyMode,'agentGlobalPortSecurityViolationTrapMode':agentGlobalPortSecurityViolationTrapMode,'agentPortSecurityTraps':agentPortSecurityTraps,'agentPortSecurityViolation':agentPortSecurityViolation})