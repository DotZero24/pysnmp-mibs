_M='qtechIPPrivateAcNotifyChangeIpv4AddressAlarm'
_L='qtechIPPrivateAcApGateway'
_K='qtechIPPrivateAcApMask'
_J='qtechIPPrivateAcNotifyIpv4ChangeIfIndex'
_I='qtechIPPrivateAcNotifyIpv4ChangeAddressMask'
_H='qtechIPPrivateAcNotifyIpv4ChangeAddress'
_G='qtechIPPrivateAcNotifyIpv4AddressChangeType'
_F='qtechIPPrivateAcApIp'
_E='qtechIPPrivateAcApMacAddr'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='QTECH-IP-PRIVATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
qtechIPPrivateMgmt=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,73))
if mibBuilder.loadTexts:qtechIPPrivateMgmt.setRevisions(('2009-09-18 00:00',))
_QtechIPPrivateAcNotificationsMIBObjects_ObjectIdentity=ObjectIdentity
qtechIPPrivateAcNotificationsMIBObjects=_QtechIPPrivateAcNotificationsMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,1))
_QtechIPPrivateAcNtfObjects_ObjectIdentity=ObjectIdentity
qtechIPPrivateAcNtfObjects=_QtechIPPrivateAcNtfObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,1,1))
_QtechIPPrivateAcNotifyIpv4AddressChangeType_Type=Integer32
_QtechIPPrivateAcNotifyIpv4AddressChangeType_Object=MibScalar
qtechIPPrivateAcNotifyIpv4AddressChangeType=_QtechIPPrivateAcNotifyIpv4AddressChangeType_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,1,1),_QtechIPPrivateAcNotifyIpv4AddressChangeType_Type())
qtechIPPrivateAcNotifyIpv4AddressChangeType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPPrivateAcNotifyIpv4AddressChangeType.setStatus(_B)
_QtechIPPrivateAcNotifyIpv4ChangeAddress_Type=IpAddress
_QtechIPPrivateAcNotifyIpv4ChangeAddress_Object=MibScalar
qtechIPPrivateAcNotifyIpv4ChangeAddress=_QtechIPPrivateAcNotifyIpv4ChangeAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,1,2),_QtechIPPrivateAcNotifyIpv4ChangeAddress_Type())
qtechIPPrivateAcNotifyIpv4ChangeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPPrivateAcNotifyIpv4ChangeAddress.setStatus(_B)
_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Type=IpAddress
_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Object=MibScalar
qtechIPPrivateAcNotifyIpv4ChangeAddressMask=_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,1,3),_QtechIPPrivateAcNotifyIpv4ChangeAddressMask_Type())
qtechIPPrivateAcNotifyIpv4ChangeAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPPrivateAcNotifyIpv4ChangeAddressMask.setStatus(_B)
_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Type=Integer32
_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Object=MibScalar
qtechIPPrivateAcNotifyIpv4ChangeIfIndex=_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,1,4),_QtechIPPrivateAcNotifyIpv4ChangeIfIndex_Type())
qtechIPPrivateAcNotifyIpv4ChangeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIPPrivateAcNotifyIpv4ChangeIfIndex.setStatus(_B)
_QtechIPPrivateAcNotifications_ObjectIdentity=ObjectIdentity
qtechIPPrivateAcNotifications=_QtechIPPrivateAcNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,1,2))
_QtechIPPrivateAcQueryApMIBObject_ObjectIdentity=ObjectIdentity
qtechIPPrivateAcQueryApMIBObject=_QtechIPPrivateAcQueryApMIBObject_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,1,3))
_QtechIPPrivateAcQueryApInfo_ObjectIdentity=ObjectIdentity
qtechIPPrivateAcQueryApInfo=_QtechIPPrivateAcQueryApInfo_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1))
_QtechIPPrivateAcQueryApMIBTable_Object=MibTable
qtechIPPrivateAcQueryApMIBTable=_QtechIPPrivateAcQueryApMIBTable_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1))
if mibBuilder.loadTexts:qtechIPPrivateAcQueryApMIBTable.setStatus(_B)
_QtechIPPrivateApInfoEntry_Object=MibTableRow
qtechIPPrivateApInfoEntry=_QtechIPPrivateApInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1,1))
qtechIPPrivateApInfoEntry.setIndexNames((0,_A,_E),(0,_A,_F))
if mibBuilder.loadTexts:qtechIPPrivateApInfoEntry.setStatus(_B)
_QtechIPPrivateAcApMacAddr_Type=MacAddress
_QtechIPPrivateAcApMacAddr_Object=MibTableColumn
qtechIPPrivateAcApMacAddr=_QtechIPPrivateAcApMacAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1,1,1),_QtechIPPrivateAcApMacAddr_Type())
qtechIPPrivateAcApMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIPPrivateAcApMacAddr.setStatus(_B)
_QtechIPPrivateAcApIp_Type=IpAddress
_QtechIPPrivateAcApIp_Object=MibTableColumn
qtechIPPrivateAcApIp=_QtechIPPrivateAcApIp_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1,1,2),_QtechIPPrivateAcApIp_Type())
qtechIPPrivateAcApIp.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIPPrivateAcApIp.setStatus(_B)
_QtechIPPrivateAcApMask_Type=IpAddress
_QtechIPPrivateAcApMask_Object=MibTableColumn
qtechIPPrivateAcApMask=_QtechIPPrivateAcApMask_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1,1,3),_QtechIPPrivateAcApMask_Type())
qtechIPPrivateAcApMask.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIPPrivateAcApMask.setStatus(_B)
_QtechIPPrivateAcApGateway_Type=IpAddress
_QtechIPPrivateAcApGateway_Object=MibTableColumn
qtechIPPrivateAcApGateway=_QtechIPPrivateAcApGateway_Object((1,3,6,1,4,1,27514,1,1,10,2,73,1,3,1,1,1,4),_QtechIPPrivateAcApGateway_Type())
qtechIPPrivateAcApGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIPPrivateAcApGateway.setStatus(_B)
_QtechIPPrivateMIBConformance_ObjectIdentity=ObjectIdentity
qtechIPPrivateMIBConformance=_QtechIPPrivateMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,2))
_QtechIPPrivateMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIPPrivateMIBCompliances=_QtechIPPrivateMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,2,1))
_QtechIPPrivateMIBGroups_ObjectIdentity=ObjectIdentity
qtechIPPrivateMIBGroups=_QtechIPPrivateMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,73,2,2))
qtechIPPrivateMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,73,2,2,1))
qtechIPPrivateMIBGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_E),(_A,_F),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:qtechIPPrivateMIBGroup.setStatus(_B)
qtechIPPrivateAcNotifyChangeIpv4AddressAlarm=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,73,1,2,1))
qtechIPPrivateAcNotifyChangeIpv4AddressAlarm.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:qtechIPPrivateAcNotifyChangeIpv4AddressAlarm.setStatus(_B)
qtechIPPrivateTrapGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,73,2,2,2))
qtechIPPrivateTrapGroup.setObjects((_A,_M))
if mibBuilder.loadTexts:qtechIPPrivateTrapGroup.setStatus(_B)
qtechIPPrivateMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,73,2,1,1))
qtechIPPrivateMIBCompliance.setObjects(*((_A,'qtechAcIPPrivateMIBGroup'),(_A,'qtechAcIPPrivateTrapGroup')))
if mibBuilder.loadTexts:qtechIPPrivateMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechIPPrivateMgmt':qtechIPPrivateMgmt,'qtechIPPrivateAcNotificationsMIBObjects':qtechIPPrivateAcNotificationsMIBObjects,'qtechIPPrivateAcNtfObjects':qtechIPPrivateAcNtfObjects,_G:qtechIPPrivateAcNotifyIpv4AddressChangeType,_H:qtechIPPrivateAcNotifyIpv4ChangeAddress,_I:qtechIPPrivateAcNotifyIpv4ChangeAddressMask,_J:qtechIPPrivateAcNotifyIpv4ChangeIfIndex,'qtechIPPrivateAcNotifications':qtechIPPrivateAcNotifications,_M:qtechIPPrivateAcNotifyChangeIpv4AddressAlarm,'qtechIPPrivateAcQueryApMIBObject':qtechIPPrivateAcQueryApMIBObject,'qtechIPPrivateAcQueryApInfo':qtechIPPrivateAcQueryApInfo,'qtechIPPrivateAcQueryApMIBTable':qtechIPPrivateAcQueryApMIBTable,'qtechIPPrivateApInfoEntry':qtechIPPrivateApInfoEntry,_E:qtechIPPrivateAcApMacAddr,_F:qtechIPPrivateAcApIp,_K:qtechIPPrivateAcApMask,_L:qtechIPPrivateAcApGateway,'qtechIPPrivateMIBConformance':qtechIPPrivateMIBConformance,'qtechIPPrivateMIBCompliances':qtechIPPrivateMIBCompliances,'qtechIPPrivateMIBCompliance':qtechIPPrivateMIBCompliance,'qtechIPPrivateMIBGroups':qtechIPPrivateMIBGroups,'qtechIPPrivateMIBGroup':qtechIPPrivateMIBGroup,'qtechIPPrivateTrapGroup':qtechIPPrivateTrapGroup})