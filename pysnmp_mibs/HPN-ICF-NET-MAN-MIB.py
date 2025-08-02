_K='hpnicfNMNotificationGroup'
_J='hpnicfNMMonitorGroup'
_I='hpnicfIpAddrChangeNotify'
_H='hpnicfNMSerialNum'
_G='hpnicfNMCustomBuildInfo'
_F='hpnicfNMIpAddress'
_E='hpnicfNMIpAddressType'
_D='accessible-for-notify'
_C='OctetString'
_B='current'
_A='HPN-ICF-NET-MAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfNetMan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90))
if mibBuilder.loadTexts:hpnicfNetMan.setRevisions(('2008-04-16 17:00',))
_HpnicfNMConfigObjects_ObjectIdentity=ObjectIdentity
hpnicfNMConfigObjects=_HpnicfNMConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,1))
_HpnicfNMMonitorObjects_ObjectIdentity=ObjectIdentity
hpnicfNMMonitorObjects=_HpnicfNMMonitorObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,2))
_HpnicfNMNotify_ObjectIdentity=ObjectIdentity
hpnicfNMNotify=_HpnicfNMNotify_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,3))
_HpnicfNMNotifyScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfNMNotifyScalarObjects=_HpnicfNMNotifyScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,3,1))
_HpnicfNMIpAddressType_Type=InetAddressType
_HpnicfNMIpAddressType_Object=MibScalar
hpnicfNMIpAddressType=_HpnicfNMIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,90,3,1,1),_HpnicfNMIpAddressType_Type())
hpnicfNMIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNMIpAddressType.setStatus(_B)
_HpnicfNMIpAddress_Type=InetAddress
_HpnicfNMIpAddress_Object=MibScalar
hpnicfNMIpAddress=_HpnicfNMIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,90,3,1,2),_HpnicfNMIpAddress_Type())
hpnicfNMIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNMIpAddress.setStatus(_B)
class _HpnicfNMCustomBuildInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfNMCustomBuildInfo_Type.__name__=_C
_HpnicfNMCustomBuildInfo_Object=MibScalar
hpnicfNMCustomBuildInfo=_HpnicfNMCustomBuildInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,90,3,1,3),_HpnicfNMCustomBuildInfo_Type())
hpnicfNMCustomBuildInfo.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfNMCustomBuildInfo.setStatus(_B)
class _HpnicfNMSerialNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfNMSerialNum_Type.__name__=_C
_HpnicfNMSerialNum_Object=MibScalar
hpnicfNMSerialNum=_HpnicfNMSerialNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,90,3,1,4),_HpnicfNMSerialNum_Type())
hpnicfNMSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfNMSerialNum.setStatus(_B)
_HpnicfNMNotifyObjects_ObjectIdentity=ObjectIdentity
hpnicfNMNotifyObjects=_HpnicfNMNotifyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,3,2))
_HpnicfNMNotifyObjectsPrefix_ObjectIdentity=ObjectIdentity
hpnicfNMNotifyObjectsPrefix=_HpnicfNMNotifyObjectsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,3,2,0))
_HpnicfNetManConformance_ObjectIdentity=ObjectIdentity
hpnicfNetManConformance=_HpnicfNetManConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,4))
_HpnicfNetManCompliances_ObjectIdentity=ObjectIdentity
hpnicfNetManCompliances=_HpnicfNetManCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,4,1))
_HpnicfNetManGroups_ObjectIdentity=ObjectIdentity
hpnicfNetManGroups=_HpnicfNetManGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,90,4,2))
hpnicfNMMonitorGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,90,4,2,1))
hpnicfNMMonitorGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpnicfNMMonitorGroup.setStatus(_B)
hpnicfIpAddrChangeNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,90,3,2,0,1))
hpnicfIpAddrChangeNotify.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpnicfIpAddrChangeNotify.setStatus(_B)
hpnicfNMNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,90,4,2,2))
hpnicfNMNotificationGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:hpnicfNMNotificationGroup.setStatus(_B)
hpnicfNetManCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,90,4,1,1))
hpnicfNetManCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpnicfNetManCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpnicfNetMan':hpnicfNetMan,'hpnicfNMConfigObjects':hpnicfNMConfigObjects,'hpnicfNMMonitorObjects':hpnicfNMMonitorObjects,'hpnicfNMNotify':hpnicfNMNotify,'hpnicfNMNotifyScalarObjects':hpnicfNMNotifyScalarObjects,_E:hpnicfNMIpAddressType,_F:hpnicfNMIpAddress,_G:hpnicfNMCustomBuildInfo,_H:hpnicfNMSerialNum,'hpnicfNMNotifyObjects':hpnicfNMNotifyObjects,'hpnicfNMNotifyObjectsPrefix':hpnicfNMNotifyObjectsPrefix,_I:hpnicfIpAddrChangeNotify,'hpnicfNetManConformance':hpnicfNetManConformance,'hpnicfNetManCompliances':hpnicfNetManCompliances,'hpnicfNetManCompliance':hpnicfNetManCompliance,'hpnicfNetManGroups':hpnicfNetManGroups,_J:hpnicfNMMonitorGroup,_K:hpnicfNMNotificationGroup})