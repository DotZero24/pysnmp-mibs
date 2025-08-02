_E='ciscoLecExtVlanMIBGroup'
_D='cLecToVlanId'
_C='cLecToVlanEntry'
_B='CISCO-LEC-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
lecConfigEntry,=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','lecConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoLecExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,77))
if mibBuilder.loadTexts:ciscoLecExtMIB.setRevisions(('1997-05-09 12:30',))
_CiscoLecExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBObjects=_CiscoLecExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,77,1))
_CLecExtVlan_ObjectIdentity=ObjectIdentity
cLecExtVlan=_CLecExtVlan_ObjectIdentity((1,3,6,1,4,1,9,9,77,1,1))
_CLecToVlanTable_Object=MibTable
cLecToVlanTable=_CLecToVlanTable_Object((1,3,6,1,4,1,9,9,77,1,1,1))
if mibBuilder.loadTexts:cLecToVlanTable.setStatus(_A)
_CLecToVlanEntry_Object=MibTableRow
cLecToVlanEntry=_CLecToVlanEntry_Object((1,3,6,1,4,1,9,9,77,1,1,1,1))
if mibBuilder.loadTexts:cLecToVlanEntry.setStatus(_A)
_CLecToVlanId_Type=VlanIndex
_CLecToVlanId_Object=MibTableColumn
cLecToVlanId=_CLecToVlanId_Object((1,3,6,1,4,1,9,9,77,1,1,1,1,1),_CLecToVlanId_Type())
cLecToVlanId.setMaxAccess('read-create')
if mibBuilder.loadTexts:cLecToVlanId.setStatus(_A)
_CiscoLecExtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBNotificationPrefix=_CiscoLecExtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,77,2))
_CiscoLecExtMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBNotifications=_CiscoLecExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,77,2,0))
_CiscoLecExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBConformance=_CiscoLecExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,77,3))
_CiscoLecExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBCompliances=_CiscoLecExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,77,3,1))
_CiscoLecExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLecExtMIBGroups=_CiscoLecExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,77,3,2))
lecConfigEntry.registerAugmentions((_B,_C))
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())
ciscoLecExtVlanMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,77,3,2,1))
ciscoLecExtVlanMIBGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:ciscoLecExtVlanMIBGroup.setStatus(_A)
ciscoLecExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,77,3,1,1))
ciscoLecExtMIBCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:ciscoLecExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLecExtMIB':ciscoLecExtMIB,'ciscoLecExtMIBObjects':ciscoLecExtMIBObjects,'cLecExtVlan':cLecExtVlan,'cLecToVlanTable':cLecToVlanTable,_C:cLecToVlanEntry,_D:cLecToVlanId,'ciscoLecExtMIBNotificationPrefix':ciscoLecExtMIBNotificationPrefix,'ciscoLecExtMIBNotifications':ciscoLecExtMIBNotifications,'ciscoLecExtMIBConformance':ciscoLecExtMIBConformance,'ciscoLecExtMIBCompliances':ciscoLecExtMIBCompliances,'ciscoLecExtMIBCompliance':ciscoLecExtMIBCompliance,'ciscoLecExtMIBGroups':ciscoLecExtMIBGroups,_E:ciscoLecExtVlanMIBGroup})