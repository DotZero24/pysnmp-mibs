_K='h3cNMNotificationGroup'
_J='h3cNMMonitorGroup'
_I='h3cIpAddrChangeNotify'
_H='h3cNMSerialNum'
_G='h3cNMCustomBuildInfo'
_F='h3cNMIpAddress'
_E='h3cNMIpAddressType'
_D='accessible-for-notify'
_C='OctetString'
_B='current'
_A='H3C-NET-MAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cNetMan=ModuleIdentity((1,3,6,1,4,1,2011,10,2,90))
if mibBuilder.loadTexts:h3cNetMan.setRevisions(('2008-04-16 17:00',))
_H3cNMConfigObjects_ObjectIdentity=ObjectIdentity
h3cNMConfigObjects=_H3cNMConfigObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,1))
_H3cNMMonitorObjects_ObjectIdentity=ObjectIdentity
h3cNMMonitorObjects=_H3cNMMonitorObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,2))
_H3cNMNotify_ObjectIdentity=ObjectIdentity
h3cNMNotify=_H3cNMNotify_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,3))
_H3cNMNotifyScalarObjects_ObjectIdentity=ObjectIdentity
h3cNMNotifyScalarObjects=_H3cNMNotifyScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,3,1))
_H3cNMIpAddressType_Type=InetAddressType
_H3cNMIpAddressType_Object=MibScalar
h3cNMIpAddressType=_H3cNMIpAddressType_Object((1,3,6,1,4,1,2011,10,2,90,3,1,1),_H3cNMIpAddressType_Type())
h3cNMIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNMIpAddressType.setStatus(_B)
_H3cNMIpAddress_Type=InetAddress
_H3cNMIpAddress_Object=MibScalar
h3cNMIpAddress=_H3cNMIpAddress_Object((1,3,6,1,4,1,2011,10,2,90,3,1,2),_H3cNMIpAddress_Type())
h3cNMIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNMIpAddress.setStatus(_B)
class _H3cNMCustomBuildInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cNMCustomBuildInfo_Type.__name__=_C
_H3cNMCustomBuildInfo_Object=MibScalar
h3cNMCustomBuildInfo=_H3cNMCustomBuildInfo_Object((1,3,6,1,4,1,2011,10,2,90,3,1,3),_H3cNMCustomBuildInfo_Type())
h3cNMCustomBuildInfo.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cNMCustomBuildInfo.setStatus(_B)
class _H3cNMSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cNMSerialNum_Type.__name__=_C
_H3cNMSerialNum_Object=MibScalar
h3cNMSerialNum=_H3cNMSerialNum_Object((1,3,6,1,4,1,2011,10,2,90,3,1,4),_H3cNMSerialNum_Type())
h3cNMSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNMSerialNum.setStatus(_B)
_H3cNMNotifyObjects_ObjectIdentity=ObjectIdentity
h3cNMNotifyObjects=_H3cNMNotifyObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,3,2))
_H3cNMNotifyObjectsPrefix_ObjectIdentity=ObjectIdentity
h3cNMNotifyObjectsPrefix=_H3cNMNotifyObjectsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,3,2,0))
_H3cNetManConformance_ObjectIdentity=ObjectIdentity
h3cNetManConformance=_H3cNetManConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,4))
_H3cNetManCompliances_ObjectIdentity=ObjectIdentity
h3cNetManCompliances=_H3cNetManCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,4,1))
_H3cNetManGroups_ObjectIdentity=ObjectIdentity
h3cNetManGroups=_H3cNetManGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,90,4,2))
h3cNMMonitorGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,90,4,2,1))
h3cNMMonitorGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cNMMonitorGroup.setStatus(_B)
h3cIpAddrChangeNotify=NotificationType((1,3,6,1,4,1,2011,10,2,90,3,2,0,1))
h3cIpAddrChangeNotify.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:h3cIpAddrChangeNotify.setStatus(_B)
h3cNMNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,10,2,90,4,2,2))
h3cNMNotificationGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:h3cNMNotificationGroup.setStatus(_B)
h3cNetManCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,90,4,1,1))
h3cNetManCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:h3cNetManCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cNetMan':h3cNetMan,'h3cNMConfigObjects':h3cNMConfigObjects,'h3cNMMonitorObjects':h3cNMMonitorObjects,'h3cNMNotify':h3cNMNotify,'h3cNMNotifyScalarObjects':h3cNMNotifyScalarObjects,_E:h3cNMIpAddressType,_F:h3cNMIpAddress,_G:h3cNMCustomBuildInfo,_H:h3cNMSerialNum,'h3cNMNotifyObjects':h3cNMNotifyObjects,'h3cNMNotifyObjectsPrefix':h3cNMNotifyObjectsPrefix,_I:h3cIpAddrChangeNotify,'h3cNetManConformance':h3cNetManConformance,'h3cNetManCompliances':h3cNetManCompliances,'h3cNetManCompliance':h3cNetManCompliance,'h3cNetManGroups':h3cNetManGroups,_J:h3cNMMonitorGroup,_K:h3cNMNotificationGroup})