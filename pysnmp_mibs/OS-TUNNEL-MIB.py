_e='osTunnelNotificationsGroup'
_d='osWanMandatoryGroup'
_c='osTunnelMandatoryGroup'
_b='osTunnelDown'
_a='osTunnelUp'
_Z='osWanIpv6Receive'
_Y='osWanRemoteIpv6Address'
_X='osWanLocalIpv6Address'
_W='osWanIpv4Receive'
_V='osWanRemoteIpv4Address'
_U='osWanLocalIpv4Address'
_T='osTunnelOperStatus'
_S='osTunnelAdminStatus'
_R='osTunnelStatus'
_Q='osTunnelLocation'
_P='osTunnelEncapsMethod'
_O='osTunnelRemoteAddress'
_N='osTunnelLocalAddress'
_M='osTunnelAddressType'
_L='receive'
_K='noreceive'
_J='osWanModule'
_I='not-accessible'
_H='osTunnelName'
_G='osTunnelDescription'
_F='DisplayString'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='OS-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAtunnelType,=mibBuilder.importSymbols('IANAifType-MIB','IANAtunnelType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
osTunnelMIB=ModuleIdentity((1,3,6,1,4,1,629,1,50,23))
if mibBuilder.loadTexts:osTunnelMIB.setRevisions(('2020-04-06 00:00','2017-02-22 00:00'))
_OsTunnelNotifications_ObjectIdentity=ObjectIdentity
osTunnelNotifications=_OsTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,0))
_OsTunnelMIBObjects_ObjectIdentity=ObjectIdentity
osTunnelMIBObjects=_OsTunnelMIBObjects_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,1))
_OsTunnel_ObjectIdentity=ObjectIdentity
osTunnel=_OsTunnel_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,1,1))
_OsTunnelTable_Object=MibTable
osTunnelTable=_OsTunnelTable_Object((1,3,6,1,4,1,629,1,50,23,1,1,1))
if mibBuilder.loadTexts:osTunnelTable.setStatus(_A)
_OsTunnelEntry_Object=MibTableRow
osTunnelEntry=_OsTunnelEntry_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1))
osTunnelEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:osTunnelEntry.setStatus(_A)
class _OsTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_OsTunnelName_Type.__name__=_F
_OsTunnelName_Object=MibTableColumn
osTunnelName=_OsTunnelName_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,1),_OsTunnelName_Type())
osTunnelName.setMaxAccess(_I)
if mibBuilder.loadTexts:osTunnelName.setStatus(_A)
_OsTunnelAddressType_Type=InetAddressType
_OsTunnelAddressType_Object=MibTableColumn
osTunnelAddressType=_OsTunnelAddressType_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,2),_OsTunnelAddressType_Type())
osTunnelAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelAddressType.setStatus(_A)
_OsTunnelLocalAddress_Type=InetAddress
_OsTunnelLocalAddress_Object=MibTableColumn
osTunnelLocalAddress=_OsTunnelLocalAddress_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,3),_OsTunnelLocalAddress_Type())
osTunnelLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelLocalAddress.setStatus(_A)
_OsTunnelRemoteAddress_Type=InetAddress
_OsTunnelRemoteAddress_Object=MibTableColumn
osTunnelRemoteAddress=_OsTunnelRemoteAddress_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,4),_OsTunnelRemoteAddress_Type())
osTunnelRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelRemoteAddress.setStatus(_A)
_OsTunnelEncapsMethod_Type=IANAtunnelType
_OsTunnelEncapsMethod_Object=MibTableColumn
osTunnelEncapsMethod=_OsTunnelEncapsMethod_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,5),_OsTunnelEncapsMethod_Type())
osTunnelEncapsMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:osTunnelEncapsMethod.setStatus(_A)
class _OsTunnelLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OsTunnelLocation_Type.__name__=_F
_OsTunnelLocation_Object=MibTableColumn
osTunnelLocation=_OsTunnelLocation_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,6),_OsTunnelLocation_Type())
osTunnelLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelLocation.setStatus(_A)
class _OsTunnelDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OsTunnelDescription_Type.__name__=_F
_OsTunnelDescription_Object=MibTableColumn
osTunnelDescription=_OsTunnelDescription_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,7),_OsTunnelDescription_Type())
osTunnelDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelDescription.setStatus(_A)
_OsTunnelStatus_Type=RowStatus
_OsTunnelStatus_Object=MibTableColumn
osTunnelStatus=_OsTunnelStatus_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,8),_OsTunnelStatus_Type())
osTunnelStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelStatus.setStatus(_A)
class _OsTunnelAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_OsTunnelAdminStatus_Type.__name__=_E
_OsTunnelAdminStatus_Object=MibTableColumn
osTunnelAdminStatus=_OsTunnelAdminStatus_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,9),_OsTunnelAdminStatus_Type())
osTunnelAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osTunnelAdminStatus.setStatus(_A)
class _OsTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_OsTunnelOperStatus_Type.__name__=_E
_OsTunnelOperStatus_Object=MibTableColumn
osTunnelOperStatus=_OsTunnelOperStatus_Object((1,3,6,1,4,1,629,1,50,23,1,1,1,1,10),_OsTunnelOperStatus_Type())
osTunnelOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osTunnelOperStatus.setStatus(_A)
_OsWanTable_Object=MibTable
osWanTable=_OsWanTable_Object((1,3,6,1,4,1,629,1,50,23,1,1,2))
if mibBuilder.loadTexts:osWanTable.setStatus(_A)
_OsWanEntry_Object=MibTableRow
osWanEntry=_OsWanEntry_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1))
osWanEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osWanEntry.setStatus(_A)
class _OsWanModule_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_OsWanModule_Type.__name__=_F
_OsWanModule_Object=MibTableColumn
osWanModule=_OsWanModule_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,1),_OsWanModule_Type())
osWanModule.setMaxAccess(_I)
if mibBuilder.loadTexts:osWanModule.setStatus(_A)
_OsWanLocalIpv4Address_Type=InetAddress
_OsWanLocalIpv4Address_Object=MibTableColumn
osWanLocalIpv4Address=_OsWanLocalIpv4Address_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,2),_OsWanLocalIpv4Address_Type())
osWanLocalIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanLocalIpv4Address.setStatus(_A)
_OsWanRemoteIpv4Address_Type=InetAddress
_OsWanRemoteIpv4Address_Object=MibTableColumn
osWanRemoteIpv4Address=_OsWanRemoteIpv4Address_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,3),_OsWanRemoteIpv4Address_Type())
osWanRemoteIpv4Address.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanRemoteIpv4Address.setStatus(_A)
class _OsWanIpv4Receive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_OsWanIpv4Receive_Type.__name__=_E
_OsWanIpv4Receive_Object=MibTableColumn
osWanIpv4Receive=_OsWanIpv4Receive_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,4),_OsWanIpv4Receive_Type())
osWanIpv4Receive.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanIpv4Receive.setStatus(_A)
_OsWanLocalIpv6Address_Type=InetAddress
_OsWanLocalIpv6Address_Object=MibTableColumn
osWanLocalIpv6Address=_OsWanLocalIpv6Address_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,5),_OsWanLocalIpv6Address_Type())
osWanLocalIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanLocalIpv6Address.setStatus(_A)
_OsWanRemoteIpv6Address_Type=InetAddress
_OsWanRemoteIpv6Address_Object=MibTableColumn
osWanRemoteIpv6Address=_OsWanRemoteIpv6Address_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,6),_OsWanRemoteIpv6Address_Type())
osWanRemoteIpv6Address.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanRemoteIpv6Address.setStatus(_A)
class _OsWanIpv6Receive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_OsWanIpv6Receive_Type.__name__=_E
_OsWanIpv6Receive_Object=MibTableColumn
osWanIpv6Receive=_OsWanIpv6Receive_Object((1,3,6,1,4,1,629,1,50,23,1,1,2,1,7),_OsWanIpv6Receive_Type())
osWanIpv6Receive.setMaxAccess(_C)
if mibBuilder.loadTexts:osWanIpv6Receive.setStatus(_A)
_OsTunnelConformance_ObjectIdentity=ObjectIdentity
osTunnelConformance=_OsTunnelConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,10))
_OsTunnelMIBCompliances_ObjectIdentity=ObjectIdentity
osTunnelMIBCompliances=_OsTunnelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,10,1))
_OsTunnelMIBGroups_ObjectIdentity=ObjectIdentity
osTunnelMIBGroups=_OsTunnelMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,23,10,2))
osTunnelMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,23,10,2,1))
osTunnelMandatoryGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:osTunnelMandatoryGroup.setStatus(_A)
osWanMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,23,10,2,2))
osWanMandatoryGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:osWanMandatoryGroup.setStatus(_A)
osTunnelUp=NotificationType((1,3,6,1,4,1,629,1,50,23,0,1))
osTunnelUp.setObjects((_B,_G))
if mibBuilder.loadTexts:osTunnelUp.setStatus(_A)
osTunnelDown=NotificationType((1,3,6,1,4,1,629,1,50,23,0,2))
osTunnelDown.setObjects((_B,_G))
if mibBuilder.loadTexts:osTunnelDown.setStatus(_A)
osTunnelNotificationsGroup=NotificationGroup((1,3,6,1,4,1,629,1,50,23,10,2,3))
osTunnelNotificationsGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:osTunnelNotificationsGroup.setStatus(_A)
osTunnelMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,23,10,1,1))
osTunnelMIBCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:osTunnelMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osTunnelMIB':osTunnelMIB,'osTunnelNotifications':osTunnelNotifications,_a:osTunnelUp,_b:osTunnelDown,'osTunnelMIBObjects':osTunnelMIBObjects,'osTunnel':osTunnel,'osTunnelTable':osTunnelTable,'osTunnelEntry':osTunnelEntry,_H:osTunnelName,_M:osTunnelAddressType,_N:osTunnelLocalAddress,_O:osTunnelRemoteAddress,_P:osTunnelEncapsMethod,_Q:osTunnelLocation,_G:osTunnelDescription,_R:osTunnelStatus,_S:osTunnelAdminStatus,_T:osTunnelOperStatus,'osWanTable':osWanTable,'osWanEntry':osWanEntry,_J:osWanModule,_U:osWanLocalIpv4Address,_V:osWanRemoteIpv4Address,_W:osWanIpv4Receive,_X:osWanLocalIpv6Address,_Y:osWanRemoteIpv6Address,_Z:osWanIpv6Receive,'osTunnelConformance':osTunnelConformance,'osTunnelMIBCompliances':osTunnelMIBCompliances,'osTunnelMIBCompliance':osTunnelMIBCompliance,'osTunnelMIBGroups':osTunnelMIBGroups,_c:osTunnelMandatoryGroup,_d:osWanMandatoryGroup,_e:osTunnelNotificationsGroup})