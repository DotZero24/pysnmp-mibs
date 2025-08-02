_L='wwpIpInterfaceSubnet'
_K='wwpIpInterfaceIpAddr'
_J='wwpIpInterfaceName'
_I='wwpIpExtInterfaceEntry'
_H='wwpIpInterfaceIndex'
_G='TruthValue'
_F='DisplayString'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='WWP-IP-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','TextualConvention',_G)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpIpInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,17))
if mibBuilder.loadTexts:wwpIpInterfaceMIB.setRevisions(('2003-05-02 00:00','2001-04-03 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpIpInterfaceMIBObjects_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBObjects=_WwpIpInterfaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,17,1))
_WwpIpInterface_ObjectIdentity=ObjectIdentity
wwpIpInterface=_WwpIpInterface_ObjectIdentity((1,3,6,1,4,1,6141,2,17,1,1))
_WwpIpInterfaceTable_Object=MibTable
wwpIpInterfaceTable=_WwpIpInterfaceTable_Object((1,3,6,1,4,1,6141,2,17,1,1,1))
if mibBuilder.loadTexts:wwpIpInterfaceTable.setStatus(_A)
_WwpIpInterfaceEntry_Object=MibTableRow
wwpIpInterfaceEntry=_WwpIpInterfaceEntry_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1))
wwpIpInterfaceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:wwpIpInterfaceEntry.setStatus(_A)
class _WwpIpInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpIpInterfaceIndex_Type.__name__=_D
_WwpIpInterfaceIndex_Object=MibTableColumn
wwpIpInterfaceIndex=_WwpIpInterfaceIndex_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1,1),_WwpIpInterfaceIndex_Type())
wwpIpInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpIpInterfaceIndex.setStatus(_A)
class _WwpIpInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpIpInterfaceName_Type.__name__=_F
_WwpIpInterfaceName_Object=MibTableColumn
wwpIpInterfaceName=_WwpIpInterfaceName_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1,2),_WwpIpInterfaceName_Type())
wwpIpInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpIpInterfaceName.setStatus(_A)
_WwpIpInterfaceIpAddr_Type=IpAddress
_WwpIpInterfaceIpAddr_Object=MibTableColumn
wwpIpInterfaceIpAddr=_WwpIpInterfaceIpAddr_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1,3),_WwpIpInterfaceIpAddr_Type())
wwpIpInterfaceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceIpAddr.setStatus(_A)
_WwpIpInterfaceSubnet_Type=IpAddress
_WwpIpInterfaceSubnet_Object=MibTableColumn
wwpIpInterfaceSubnet=_WwpIpInterfaceSubnet_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1,4),_WwpIpInterfaceSubnet_Type())
wwpIpInterfaceSubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceSubnet.setStatus(_A)
class _WwpIpInterfaceIfIndexXref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WwpIpInterfaceIfIndexXref_Type.__name__=_D
_WwpIpInterfaceIfIndexXref_Object=MibTableColumn
wwpIpInterfaceIfIndexXref=_WwpIpInterfaceIfIndexXref_Object((1,3,6,1,4,1,6141,2,17,1,1,1,1,5),_WwpIpInterfaceIfIndexXref_Type())
wwpIpInterfaceIfIndexXref.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpIpInterfaceIfIndexXref.setStatus(_A)
_WwpIpExtInterfaceTable_Object=MibTable
wwpIpExtInterfaceTable=_WwpIpExtInterfaceTable_Object((1,3,6,1,4,1,6141,2,17,1,1,2))
if mibBuilder.loadTexts:wwpIpExtInterfaceTable.setStatus(_A)
_WwpIpExtInterfaceEntry_Object=MibTableRow
wwpIpExtInterfaceEntry=_WwpIpExtInterfaceEntry_Object((1,3,6,1,4,1,6141,2,17,1,1,2,1))
if mibBuilder.loadTexts:wwpIpExtInterfaceEntry.setStatus(_A)
_WwpIpInterfaceEnable_Type=TruthValue
_WwpIpInterfaceEnable_Object=MibTableColumn
wwpIpInterfaceEnable=_WwpIpInterfaceEnable_Object((1,3,6,1,4,1,6141,2,17,1,1,2,1,1),_WwpIpInterfaceEnable_Type())
wwpIpInterfaceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceEnable.setStatus(_A)
_WwpIpInterfaceVlanId_Type=VlanId
_WwpIpInterfaceVlanId_Object=MibTableColumn
wwpIpInterfaceVlanId=_WwpIpInterfaceVlanId_Object((1,3,6,1,4,1,6141,2,17,1,1,2,1,2),_WwpIpInterfaceVlanId_Type())
wwpIpInterfaceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceVlanId.setStatus(_A)
class _WwpIpInterfaceMgmtPktPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpIpInterfaceMgmtPktPriority_Type.__name__=_D
_WwpIpInterfaceMgmtPktPriority_Object=MibTableColumn
wwpIpInterfaceMgmtPktPriority=_WwpIpInterfaceMgmtPktPriority_Object((1,3,6,1,4,1,6141,2,17,1,1,2,1,3),_WwpIpInterfaceMgmtPktPriority_Type())
wwpIpInterfaceMgmtPktPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceMgmtPktPriority.setStatus(_A)
class _WwpIpInterfaceAddrNotifEnabled_Type(TruthValue):defaultValue=1
_WwpIpInterfaceAddrNotifEnabled_Type.__name__=_G
_WwpIpInterfaceAddrNotifEnabled_Object=MibScalar
wwpIpInterfaceAddrNotifEnabled=_WwpIpInterfaceAddrNotifEnabled_Object((1,3,6,1,4,1,6141,2,17,1,1,3),_WwpIpInterfaceAddrNotifEnabled_Type())
wwpIpInterfaceAddrNotifEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpIpInterfaceAddrNotifEnabled.setStatus(_A)
_WwpIpInterfaceMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBNotificationPrefix=_WwpIpInterfaceMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,17,2))
_WwpIpInterfaceMIBNotifications_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBNotifications=_WwpIpInterfaceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,17,2,0))
_WwpIpInterfaceMIBConformance_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBConformance=_WwpIpInterfaceMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,17,3))
_WwpIpInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBCompliances=_WwpIpInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,17,3,1))
_WwpIpInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
wwpIpInterfaceMIBGroups=_WwpIpInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,17,3,2))
wwpIpInterfaceEntry.registerAugmentions((_B,_I))
wwpIpExtInterfaceEntry.setIndexNames(*wwpIpInterfaceEntry.getIndexNames())
wwpIpInterfaceAddrChgNotification=NotificationType((1,3,6,1,4,1,6141,2,17,2,0,1))
wwpIpInterfaceAddrChgNotification.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:wwpIpInterfaceAddrChgNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanId':VlanId,'wwpIpInterfaceMIB':wwpIpInterfaceMIB,'wwpIpInterfaceMIBObjects':wwpIpInterfaceMIBObjects,'wwpIpInterface':wwpIpInterface,'wwpIpInterfaceTable':wwpIpInterfaceTable,'wwpIpInterfaceEntry':wwpIpInterfaceEntry,_H:wwpIpInterfaceIndex,_J:wwpIpInterfaceName,_K:wwpIpInterfaceIpAddr,_L:wwpIpInterfaceSubnet,'wwpIpInterfaceIfIndexXref':wwpIpInterfaceIfIndexXref,'wwpIpExtInterfaceTable':wwpIpExtInterfaceTable,_I:wwpIpExtInterfaceEntry,'wwpIpInterfaceEnable':wwpIpInterfaceEnable,'wwpIpInterfaceVlanId':wwpIpInterfaceVlanId,'wwpIpInterfaceMgmtPktPriority':wwpIpInterfaceMgmtPktPriority,'wwpIpInterfaceAddrNotifEnabled':wwpIpInterfaceAddrNotifEnabled,'wwpIpInterfaceMIBNotificationPrefix':wwpIpInterfaceMIBNotificationPrefix,'wwpIpInterfaceMIBNotifications':wwpIpInterfaceMIBNotifications,'wwpIpInterfaceAddrChgNotification':wwpIpInterfaceAddrChgNotification,'wwpIpInterfaceMIBConformance':wwpIpInterfaceMIBConformance,'wwpIpInterfaceMIBCompliances':wwpIpInterfaceMIBCompliances,'wwpIpInterfaceMIBGroups':wwpIpInterfaceMIBGroups})