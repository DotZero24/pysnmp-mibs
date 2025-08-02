_P='macNotifySystemGroup'
_O='macNotifyTrapsGroup'
_N='macNotifyDataGroup'
_M='arubaWiredMacNotifyMacAddressTableChange'
_L='arubaWiredMacNotifyEnable'
_K='arubaWiredMacNotifyToDest'
_J='arubaWiredMacNotifyFromDest'
_I='arubaWiredMacNotifyVlanId'
_H='arubaWiredMacNotifyToPortId'
_G='arubaWiredMacNotifyFromPortId'
_F='arubaWiredMacNotifyAction'
_E='Integer32'
_D='arubaWiredMacNotifyMacAddress'
_C='accessible-for-notify'
_B='current'
_A='ARUBAWIRED-MACNOTIFY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
macNotify=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,19))
if mibBuilder.loadTexts:macNotify.setRevisions(('2021-03-24 00:00',))
_ArubaWiredMacNotifyNotificationObjects_ObjectIdentity=ObjectIdentity
arubaWiredMacNotifyNotificationObjects=_ArubaWiredMacNotifyNotificationObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,0))
_ArubaWiredMacNotifyConfigObjects_ObjectIdentity=ObjectIdentity
arubaWiredMacNotifyConfigObjects=_ArubaWiredMacNotifyConfigObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,1))
class _ArubaWiredMacNotifyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ArubaWiredMacNotifyEnable_Type.__name__=_E
_ArubaWiredMacNotifyEnable_Object=MibScalar
arubaWiredMacNotifyEnable=_ArubaWiredMacNotifyEnable_Object((1,3,6,1,4,1,47196,4,1,1,3,19,1,1),_ArubaWiredMacNotifyEnable_Type())
arubaWiredMacNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:arubaWiredMacNotifyEnable.setStatus(_B)
_ArubaWiredMacNotifyConformance_ObjectIdentity=ObjectIdentity
arubaWiredMacNotifyConformance=_ArubaWiredMacNotifyConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,2))
_ArubaWiredMacNotify_ObjectIdentity=ObjectIdentity
arubaWiredMacNotify=_ArubaWiredMacNotify_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,3))
_MacNotifyChangeTable_Object=MibTable
macNotifyChangeTable=_MacNotifyChangeTable_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1))
if mibBuilder.loadTexts:macNotifyChangeTable.setStatus(_B)
_MacNotifyChangeTableEntry_Object=MibTableRow
macNotifyChangeTableEntry=_MacNotifyChangeTableEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1))
macNotifyChangeTableEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:macNotifyChangeTableEntry.setStatus(_B)
class _ArubaWiredMacNotifyAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('aged',0),('learned',1),('moved',2),('removed',3)))
_ArubaWiredMacNotifyAction_Type.__name__=_E
_ArubaWiredMacNotifyAction_Object=MibTableColumn
arubaWiredMacNotifyAction=_ArubaWiredMacNotifyAction_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,1),_ArubaWiredMacNotifyAction_Type())
arubaWiredMacNotifyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyAction.setStatus(_B)
_ArubaWiredMacNotifyMacAddress_Type=MacAddress
_ArubaWiredMacNotifyMacAddress_Object=MibTableColumn
arubaWiredMacNotifyMacAddress=_ArubaWiredMacNotifyMacAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,2),_ArubaWiredMacNotifyMacAddress_Type())
arubaWiredMacNotifyMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyMacAddress.setStatus(_B)
_ArubaWiredMacNotifyFromPortId_Type=Integer32
_ArubaWiredMacNotifyFromPortId_Object=MibTableColumn
arubaWiredMacNotifyFromPortId=_ArubaWiredMacNotifyFromPortId_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,3),_ArubaWiredMacNotifyFromPortId_Type())
arubaWiredMacNotifyFromPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyFromPortId.setStatus(_B)
_ArubaWiredMacNotifyToPortId_Type=Integer32
_ArubaWiredMacNotifyToPortId_Object=MibTableColumn
arubaWiredMacNotifyToPortId=_ArubaWiredMacNotifyToPortId_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,4),_ArubaWiredMacNotifyToPortId_Type())
arubaWiredMacNotifyToPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyToPortId.setStatus(_B)
_ArubaWiredMacNotifyVlanId_Type=Integer32
_ArubaWiredMacNotifyVlanId_Object=MibTableColumn
arubaWiredMacNotifyVlanId=_ArubaWiredMacNotifyVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,5),_ArubaWiredMacNotifyVlanId_Type())
arubaWiredMacNotifyVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyVlanId.setStatus(_B)
_ArubaWiredMacNotifyFromDest_Type=DisplayString
_ArubaWiredMacNotifyFromDest_Object=MibTableColumn
arubaWiredMacNotifyFromDest=_ArubaWiredMacNotifyFromDest_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,6),_ArubaWiredMacNotifyFromDest_Type())
arubaWiredMacNotifyFromDest.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyFromDest.setStatus(_B)
_ArubaWiredMacNotifyToDest_Type=DisplayString
_ArubaWiredMacNotifyToDest_Object=MibTableColumn
arubaWiredMacNotifyToDest=_ArubaWiredMacNotifyToDest_Object((1,3,6,1,4,1,47196,4,1,1,3,19,3,1,1,7),_ArubaWiredMacNotifyToDest_Type())
arubaWiredMacNotifyToDest.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredMacNotifyToDest.setStatus(_B)
_MacNotifyConformance_ObjectIdentity=ObjectIdentity
macNotifyConformance=_MacNotifyConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,4))
_MacNotifyDataGroups_ObjectIdentity=ObjectIdentity
macNotifyDataGroups=_MacNotifyDataGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,4,1))
_MacNotifyTrapsGroups_ObjectIdentity=ObjectIdentity
macNotifyTrapsGroups=_MacNotifyTrapsGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,4,2))
_MacNotifySystemGroups_ObjectIdentity=ObjectIdentity
macNotifySystemGroups=_MacNotifySystemGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,4,3))
_MacNotifyCompliance_ObjectIdentity=ObjectIdentity
macNotifyCompliance=_MacNotifyCompliance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,19,4,4))
macNotifyDataGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,19,4,1,1))
macNotifyDataGroup.setObjects(*((_A,_F),(_A,_D),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:macNotifyDataGroup.setStatus(_B)
macNotifySystemGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,19,4,1,3))
macNotifySystemGroup.setObjects((_A,_L))
if mibBuilder.loadTexts:macNotifySystemGroup.setStatus(_B)
arubaWiredMacNotifyMacAddressTableChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,19,0,1))
arubaWiredMacNotifyMacAddressTableChange.setObjects(*((_A,_F),(_A,_D),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:arubaWiredMacNotifyMacAddressTableChange.setStatus(_B)
macNotifyTrapsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,19,4,1,2))
macNotifyTrapsGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:macNotifyTrapsGroup.setStatus(_B)
macNotifyComplianceGroups=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,19,4,4,1))
macNotifyComplianceGroups.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:macNotifyComplianceGroups.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'macNotify':macNotify,'arubaWiredMacNotifyNotificationObjects':arubaWiredMacNotifyNotificationObjects,_M:arubaWiredMacNotifyMacAddressTableChange,'arubaWiredMacNotifyConfigObjects':arubaWiredMacNotifyConfigObjects,_L:arubaWiredMacNotifyEnable,'arubaWiredMacNotifyConformance':arubaWiredMacNotifyConformance,'arubaWiredMacNotify':arubaWiredMacNotify,'macNotifyChangeTable':macNotifyChangeTable,'macNotifyChangeTableEntry':macNotifyChangeTableEntry,_F:arubaWiredMacNotifyAction,_D:arubaWiredMacNotifyMacAddress,_G:arubaWiredMacNotifyFromPortId,_H:arubaWiredMacNotifyToPortId,_I:arubaWiredMacNotifyVlanId,_J:arubaWiredMacNotifyFromDest,_K:arubaWiredMacNotifyToDest,'macNotifyConformance':macNotifyConformance,'macNotifyDataGroups':macNotifyDataGroups,_N:macNotifyDataGroup,_O:macNotifyTrapsGroup,_P:macNotifySystemGroup,'macNotifyTrapsGroups':macNotifyTrapsGroups,'macNotifySystemGroups':macNotifySystemGroups,'macNotifyCompliance':macNotifyCompliance,'macNotifyComplianceGroups':macNotifyComplianceGroups})