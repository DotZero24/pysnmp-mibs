_T='virtualNwIfNotificationGroup'
_S='virtualNwIfGroup'
_R='virtualNwIfDeleteEntryNotify'
_Q='virtualNwIfCreateEntryNotify'
_P='virtualNwIfRowStatus'
_O='virtualNwIfOperStatusCauseDescr'
_N='virtualNwIfOperStatusCause'
_M='virtualNwIfFcId'
_L='not-accessible'
_K='virtualNwIfId'
_J='virtualNwIfType'
_I='ifName'
_H='IF-MIB'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='Integer32'
_D='virtualNwIfIndex'
_C='read-only'
_B='CISCO-VIRTUAL-NW-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcAddressId,=mibBuilder.importSymbols('CISCO-ST-TC','FcAddressId')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
InterfaceIndex,ifName=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVirtualNwIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,290))
if mibBuilder.loadTexts:ciscoVirtualNwIfMIB.setRevisions(('2002-10-02 00:00',))
_CiscoVirtualNwIfObjects_ObjectIdentity=ObjectIdentity
ciscoVirtualNwIfObjects=_CiscoVirtualNwIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,290,1))
_VirtualNwIfConfig_ObjectIdentity=ObjectIdentity
virtualNwIfConfig=_VirtualNwIfConfig_ObjectIdentity((1,3,6,1,4,1,9,9,290,1,1))
_VirtualNwIfTable_Object=MibTable
virtualNwIfTable=_VirtualNwIfTable_Object((1,3,6,1,4,1,9,9,290,1,1,1))
if mibBuilder.loadTexts:virtualNwIfTable.setStatus(_A)
_VirtualNwIfEntry_Object=MibTableRow
virtualNwIfEntry=_VirtualNwIfEntry_Object((1,3,6,1,4,1,9,9,290,1,1,1,1))
virtualNwIfEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:virtualNwIfEntry.setStatus(_A)
class _VirtualNwIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vsan',1),('vlan',2)))
_VirtualNwIfType_Type.__name__=_E
_VirtualNwIfType_Object=MibTableColumn
virtualNwIfType=_VirtualNwIfType_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,1),_VirtualNwIfType_Type())
virtualNwIfType.setMaxAccess(_L)
if mibBuilder.loadTexts:virtualNwIfType.setStatus(_A)
_VirtualNwIfId_Type=Unsigned32
_VirtualNwIfId_Object=MibTableColumn
virtualNwIfId=_VirtualNwIfId_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,2),_VirtualNwIfId_Type())
virtualNwIfId.setMaxAccess(_L)
if mibBuilder.loadTexts:virtualNwIfId.setStatus(_A)
_VirtualNwIfIndex_Type=InterfaceIndex
_VirtualNwIfIndex_Object=MibTableColumn
virtualNwIfIndex=_VirtualNwIfIndex_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,3),_VirtualNwIfIndex_Type())
virtualNwIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualNwIfIndex.setStatus(_A)
_VirtualNwIfFcId_Type=FcAddressId
_VirtualNwIfFcId_Object=MibTableColumn
virtualNwIfFcId=_VirtualNwIfFcId_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,4),_VirtualNwIfFcId_Type())
virtualNwIfFcId.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualNwIfFcId.setStatus(_A)
class _VirtualNwIfOperStatusCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('adminDown',2),('vsanNotOperational',3),('noFcid',4),('kernelConfFailure',5)))
_VirtualNwIfOperStatusCause_Type.__name__=_E
_VirtualNwIfOperStatusCause_Object=MibTableColumn
virtualNwIfOperStatusCause=_VirtualNwIfOperStatusCause_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,5),_VirtualNwIfOperStatusCause_Type())
virtualNwIfOperStatusCause.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualNwIfOperStatusCause.setStatus(_A)
_VirtualNwIfOperStatusCauseDescr_Type=SnmpAdminString
_VirtualNwIfOperStatusCauseDescr_Object=MibTableColumn
virtualNwIfOperStatusCauseDescr=_VirtualNwIfOperStatusCauseDescr_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,6),_VirtualNwIfOperStatusCauseDescr_Type())
virtualNwIfOperStatusCauseDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualNwIfOperStatusCauseDescr.setStatus(_A)
_VirtualNwIfRowStatus_Type=RowStatus
_VirtualNwIfRowStatus_Object=MibTableColumn
virtualNwIfRowStatus=_VirtualNwIfRowStatus_Object((1,3,6,1,4,1,9,9,290,1,1,1,1,7),_VirtualNwIfRowStatus_Type())
virtualNwIfRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:virtualNwIfRowStatus.setStatus(_A)
_VirtualNwIfStatistics_ObjectIdentity=ObjectIdentity
virtualNwIfStatistics=_VirtualNwIfStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,290,1,2))
_VirtualNwIfNotification_ObjectIdentity=ObjectIdentity
virtualNwIfNotification=_VirtualNwIfNotification_ObjectIdentity((1,3,6,1,4,1,9,9,290,1,3))
_VirtualNwIfNotifications_ObjectIdentity=ObjectIdentity
virtualNwIfNotifications=_VirtualNwIfNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,290,1,3,0))
_VirtualNwIfMIBConformance_ObjectIdentity=ObjectIdentity
virtualNwIfMIBConformance=_VirtualNwIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,290,2))
_VirtualNwIfMIBCompliances_ObjectIdentity=ObjectIdentity
virtualNwIfMIBCompliances=_VirtualNwIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,290,2,1))
_VirtualNwIfMIBGroups_ObjectIdentity=ObjectIdentity
virtualNwIfMIBGroups=_VirtualNwIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,290,2,2))
virtualNwIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,290,2,2,1))
virtualNwIfGroup.setObjects(*((_B,_D),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:virtualNwIfGroup.setStatus(_A)
virtualNwIfCreateEntryNotify=NotificationType((1,3,6,1,4,1,9,9,290,1,3,0,1))
virtualNwIfCreateEntryNotify.setObjects(*((_B,_D),(_H,_I)))
if mibBuilder.loadTexts:virtualNwIfCreateEntryNotify.setStatus(_A)
virtualNwIfDeleteEntryNotify=NotificationType((1,3,6,1,4,1,9,9,290,1,3,0,2))
virtualNwIfDeleteEntryNotify.setObjects((_B,_D))
if mibBuilder.loadTexts:virtualNwIfDeleteEntryNotify.setStatus(_A)
virtualNwIfNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,290,2,2,2))
virtualNwIfNotificationGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:virtualNwIfNotificationGroup.setStatus(_A)
virtualNwIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,290,2,1,1))
virtualNwIfMIBCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:virtualNwIfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVirtualNwIfMIB':ciscoVirtualNwIfMIB,'ciscoVirtualNwIfObjects':ciscoVirtualNwIfObjects,'virtualNwIfConfig':virtualNwIfConfig,'virtualNwIfTable':virtualNwIfTable,'virtualNwIfEntry':virtualNwIfEntry,_J:virtualNwIfType,_K:virtualNwIfId,_D:virtualNwIfIndex,_M:virtualNwIfFcId,_N:virtualNwIfOperStatusCause,_O:virtualNwIfOperStatusCauseDescr,_P:virtualNwIfRowStatus,'virtualNwIfStatistics':virtualNwIfStatistics,'virtualNwIfNotification':virtualNwIfNotification,'virtualNwIfNotifications':virtualNwIfNotifications,_Q:virtualNwIfCreateEntryNotify,_R:virtualNwIfDeleteEntryNotify,'virtualNwIfMIBConformance':virtualNwIfMIBConformance,'virtualNwIfMIBCompliances':virtualNwIfMIBCompliances,'virtualNwIfMIBCompliance':virtualNwIfMIBCompliance,'virtualNwIfMIBGroups':virtualNwIfMIBGroups,_S:virtualNwIfGroup,_T:virtualNwIfNotificationGroup})