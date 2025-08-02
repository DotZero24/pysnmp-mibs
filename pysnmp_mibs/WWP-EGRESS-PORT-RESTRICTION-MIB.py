_G='PortList'
_F='read-only'
_E='wwpERestPortId'
_D='wwpERestVlanId'
_C='Integer32'
_B='WWP-EGRESS-PORT-RESTRICTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpEgressPortRestrictionMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,34))
if mibBuilder.loadTexts:wwpEgressPortRestrictionMIB.setRevisions(('2001-04-03 17:00',))
class PortList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpEgressPortRestrictionMIBObjects_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionMIBObjects=_WwpEgressPortRestrictionMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,34,1))
_WwpEgressPortRestriction_ObjectIdentity=ObjectIdentity
wwpEgressPortRestriction=_WwpEgressPortRestriction_ObjectIdentity((1,3,6,1,4,1,6141,2,34,1,1))
_WwpEgressPortRestrictionTable_Object=MibTable
wwpEgressPortRestrictionTable=_WwpEgressPortRestrictionTable_Object((1,3,6,1,4,1,6141,2,34,1,1,1))
if mibBuilder.loadTexts:wwpEgressPortRestrictionTable.setStatus(_A)
_WwpEgressPortRestrictionEntry_Object=MibTableRow
wwpEgressPortRestrictionEntry=_WwpEgressPortRestrictionEntry_Object((1,3,6,1,4,1,6141,2,34,1,1,1,1))
wwpEgressPortRestrictionEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:wwpEgressPortRestrictionEntry.setStatus(_A)
_WwpERestVlanId_Type=VlanId
_WwpERestVlanId_Object=MibTableColumn
wwpERestVlanId=_WwpERestVlanId_Object((1,3,6,1,4,1,6141,2,34,1,1,1,1,1),_WwpERestVlanId_Type())
wwpERestVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpERestVlanId.setStatus(_A)
class _WwpERestPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpERestPortId_Type.__name__=_C
_WwpERestPortId_Object=MibTableColumn
wwpERestPortId=_WwpERestPortId_Object((1,3,6,1,4,1,6141,2,34,1,1,1,1,2),_WwpERestPortId_Type())
wwpERestPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpERestPortId.setStatus(_A)
class _WwpERestEgreesPorts_Type(PortList):defaultHexValue='0000'
_WwpERestEgreesPorts_Type.__name__=_G
_WwpERestEgreesPorts_Object=MibTableColumn
wwpERestEgreesPorts=_WwpERestEgreesPorts_Object((1,3,6,1,4,1,6141,2,34,1,1,1,1,3),_WwpERestEgreesPorts_Type())
wwpERestEgreesPorts.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpERestEgreesPorts.setStatus(_A)
_WwpERestStatus_Type=RowStatus
_WwpERestStatus_Object=MibTableColumn
wwpERestStatus=_WwpERestStatus_Object((1,3,6,1,4,1,6141,2,34,1,1,1,1,4),_WwpERestStatus_Type())
wwpERestStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:wwpERestStatus.setStatus(_A)
_WwpEgressPortRestrictionNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionNotificationPrefix=_WwpEgressPortRestrictionNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,34,2))
_WwpEgressPortRestrictionNotifications_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionNotifications=_WwpEgressPortRestrictionNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,34,2,0))
_WwpEgressPortRestrictionMIBConformance_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionMIBConformance=_WwpEgressPortRestrictionMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,34,3))
_WwpEgressPortRestrictionMIBCompliances_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionMIBCompliances=_WwpEgressPortRestrictionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,34,3,1))
_WwpEgressPortRestrictionMIBGroups_ObjectIdentity=ObjectIdentity
wwpEgressPortRestrictionMIBGroups=_WwpEgressPortRestrictionMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,34,3,2))
mibBuilder.exportSymbols(_B,**{_G:PortList,'VlanId':VlanId,'wwpEgressPortRestrictionMIB':wwpEgressPortRestrictionMIB,'wwpEgressPortRestrictionMIBObjects':wwpEgressPortRestrictionMIBObjects,'wwpEgressPortRestriction':wwpEgressPortRestriction,'wwpEgressPortRestrictionTable':wwpEgressPortRestrictionTable,'wwpEgressPortRestrictionEntry':wwpEgressPortRestrictionEntry,_D:wwpERestVlanId,_E:wwpERestPortId,'wwpERestEgreesPorts':wwpERestEgreesPorts,'wwpERestStatus':wwpERestStatus,'wwpEgressPortRestrictionNotificationPrefix':wwpEgressPortRestrictionNotificationPrefix,'wwpEgressPortRestrictionNotifications':wwpEgressPortRestrictionNotifications,'wwpEgressPortRestrictionMIBConformance':wwpEgressPortRestrictionMIBConformance,'wwpEgressPortRestrictionMIBCompliances':wwpEgressPortRestrictionMIBCompliances,'wwpEgressPortRestrictionMIBGroups':wwpEgressPortRestrictionMIBGroups})