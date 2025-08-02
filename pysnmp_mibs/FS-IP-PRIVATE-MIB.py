_M='fsIPPrivateAcNotifyChangeIpv4AddressAlarm'
_L='fsIPPrivateAcApGateway'
_K='fsIPPrivateAcApMask'
_J='fsIPPrivateAcNotifyIpv4ChangeIfIndex'
_I='fsIPPrivateAcNotifyIpv4ChangeAddressMask'
_H='fsIPPrivateAcNotifyIpv4ChangeAddress'
_G='fsIPPrivateAcNotifyIpv4AddressChangeType'
_F='fsIPPrivateAcApIp'
_E='fsIPPrivateAcApMacAddr'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='FS-IP-PRIVATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsIPPrivateMgmt=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,73))
if mibBuilder.loadTexts:fsIPPrivateMgmt.setRevisions(('2009-09-18 00:00',))
_FsIPPrivateAcNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
fsIPPrivateAcNotificationsMIBObjects=_FsIPPrivateAcNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,1))
_FsIPPrivateAcNtfObjects_ObjectIdentity=ObjectIdentity
fsIPPrivateAcNtfObjects=_FsIPPrivateAcNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,1,1))
_FsIPPrivateAcNotifyIpv4AddressChangeType_Type=Integer32
_FsIPPrivateAcNotifyIpv4AddressChangeType_Object=MibScalar
fsIPPrivateAcNotifyIpv4AddressChangeType=_FsIPPrivateAcNotifyIpv4AddressChangeType_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,1,1),_FsIPPrivateAcNotifyIpv4AddressChangeType_Type())
fsIPPrivateAcNotifyIpv4AddressChangeType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPPrivateAcNotifyIpv4AddressChangeType.setStatus(_B)
_FsIPPrivateAcNotifyIpv4ChangeAddress_Type=IpAddress
_FsIPPrivateAcNotifyIpv4ChangeAddress_Object=MibScalar
fsIPPrivateAcNotifyIpv4ChangeAddress=_FsIPPrivateAcNotifyIpv4ChangeAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,1,2),_FsIPPrivateAcNotifyIpv4ChangeAddress_Type())
fsIPPrivateAcNotifyIpv4ChangeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPPrivateAcNotifyIpv4ChangeAddress.setStatus(_B)
_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Type=IpAddress
_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Object=MibScalar
fsIPPrivateAcNotifyIpv4ChangeAddressMask=_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,1,3),_FsIPPrivateAcNotifyIpv4ChangeAddressMask_Type())
fsIPPrivateAcNotifyIpv4ChangeAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPPrivateAcNotifyIpv4ChangeAddressMask.setStatus(_B)
_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Type=Integer32
_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Object=MibScalar
fsIPPrivateAcNotifyIpv4ChangeIfIndex=_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,1,4),_FsIPPrivateAcNotifyIpv4ChangeIfIndex_Type())
fsIPPrivateAcNotifyIpv4ChangeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPPrivateAcNotifyIpv4ChangeIfIndex.setStatus(_B)
_FsIPPrivateAcNotifications_ObjectIdentity=ObjectIdentity
fsIPPrivateAcNotifications=_FsIPPrivateAcNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,1,2))
_FsIPPrivateAcQueryApMIBObject_ObjectIdentity=ObjectIdentity
fsIPPrivateAcQueryApMIBObject=_FsIPPrivateAcQueryApMIBObject_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,1,3))
_FsIPPrivateAcQueryApInfo_ObjectIdentity=ObjectIdentity
fsIPPrivateAcQueryApInfo=_FsIPPrivateAcQueryApInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1))
_FsIPPrivateAcQueryApMIBTable_Object=MibTable
fsIPPrivateAcQueryApMIBTable=_FsIPPrivateAcQueryApMIBTable_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1))
if mibBuilder.loadTexts:fsIPPrivateAcQueryApMIBTable.setStatus(_B)
_FsIPPrivateApInfoEntry_Object=MibTableRow
fsIPPrivateApInfoEntry=_FsIPPrivateApInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1,1))
fsIPPrivateApInfoEntry.setIndexNames((0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:fsIPPrivateApInfoEntry.setStatus(_B)
_FsIPPrivateAcApMacAddr_Type=MacAddress
_FsIPPrivateAcApMacAddr_Object=MibTableColumn
fsIPPrivateAcApMacAddr=_FsIPPrivateAcApMacAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1,1,1),_FsIPPrivateAcApMacAddr_Type())
fsIPPrivateAcApMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPPrivateAcApMacAddr.setStatus(_B)
_FsIPPrivateAcApIp_Type=IpAddress
_FsIPPrivateAcApIp_Object=MibTableColumn
fsIPPrivateAcApIp=_FsIPPrivateAcApIp_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1,1,2),_FsIPPrivateAcApIp_Type())
fsIPPrivateAcApIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPPrivateAcApIp.setStatus(_B)
_FsIPPrivateAcApMask_Type=IpAddress
_FsIPPrivateAcApMask_Object=MibTableColumn
fsIPPrivateAcApMask=_FsIPPrivateAcApMask_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1,1,3),_FsIPPrivateAcApMask_Type())
fsIPPrivateAcApMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPPrivateAcApMask.setStatus(_B)
_FsIPPrivateAcApGateway_Type=IpAddress
_FsIPPrivateAcApGateway_Object=MibTableColumn
fsIPPrivateAcApGateway=_FsIPPrivateAcApGateway_Object((1,3,6,1,4,1,52642,1,1,10,2,73,1,3,1,1,1,4),_FsIPPrivateAcApGateway_Type())
fsIPPrivateAcApGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPPrivateAcApGateway.setStatus(_B)
_FsIPPrivateMIBConformance_ObjectIdentity=ObjectIdentity
fsIPPrivateMIBConformance=_FsIPPrivateMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,2))
_FsIPPrivateMIBCompliances_ObjectIdentity=ObjectIdentity
fsIPPrivateMIBCompliances=_FsIPPrivateMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,2,1))
_FsIPPrivateMIBGroups_ObjectIdentity=ObjectIdentity
fsIPPrivateMIBGroups=_FsIPPrivateMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,73,2,2))
fsIPPrivateMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,73,2,2,1))
fsIPPrivateMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:fsIPPrivateMIBGroup.setStatus(_B)
fsIPPrivateAcNotifyChangeIpv4AddressAlarm=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,73,1,2,1))
fsIPPrivateAcNotifyChangeIpv4AddressAlarm.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:fsIPPrivateAcNotifyChangeIpv4AddressAlarm.setStatus(_B)
fsIPPrivateTrapGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,73,2,2,2))
fsIPPrivateTrapGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:fsIPPrivateTrapGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsIPPrivateMgmt':fsIPPrivateMgmt,'fsIPPrivateAcNotificationsMIBObjects':fsIPPrivateAcNotificationsMIBObjects,'fsIPPrivateAcNtfObjects':fsIPPrivateAcNtfObjects,_G:fsIPPrivateAcNotifyIpv4AddressChangeType,_H:fsIPPrivateAcNotifyIpv4ChangeAddress,_I:fsIPPrivateAcNotifyIpv4ChangeAddressMask,_J:fsIPPrivateAcNotifyIpv4ChangeIfIndex,'fsIPPrivateAcNotifications':fsIPPrivateAcNotifications,_M:fsIPPrivateAcNotifyChangeIpv4AddressAlarm,'fsIPPrivateAcQueryApMIBObject':fsIPPrivateAcQueryApMIBObject,'fsIPPrivateAcQueryApInfo':fsIPPrivateAcQueryApInfo,'fsIPPrivateAcQueryApMIBTable':fsIPPrivateAcQueryApMIBTable,'fsIPPrivateApInfoEntry':fsIPPrivateApInfoEntry,_E:fsIPPrivateAcApMacAddr,_F:fsIPPrivateAcApIp,_K:fsIPPrivateAcApMask,_L:fsIPPrivateAcApGateway,'fsIPPrivateMIBConformance':fsIPPrivateMIBConformance,'fsIPPrivateMIBCompliances':fsIPPrivateMIBCompliances,'fsIPPrivateMIBGroups':fsIPPrivateMIBGroups,'fsIPPrivateMIBGroup':fsIPPrivateMIBGroup,'fsIPPrivateTrapGroup':fsIPPrivateTrapGroup})