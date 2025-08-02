_I='hwIpLinkTrapGroup'
_H='hwIpLinkObjectGroup'
_G='hwIpLinkDown'
_F='hwIpLinkUp'
_E='accessible-for-notify'
_D='hwIpLinkStatus'
_C='hwIpLinkName'
_B='current'
_A='HUAWEI-SECURITY-IPLINK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwIplink=ModuleIdentity((1,3,6,1,4,1,2011,6,122,45))
if mibBuilder.loadTexts:hwIplink.setRevisions(('2012-03-19 19:33',))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwIpLinkNotification_ObjectIdentity=ObjectIdentity
hwIpLinkNotification=_HwIpLinkNotification_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,1))
_HwIpLinkTrapObjects_ObjectIdentity=ObjectIdentity
hwIpLinkTrapObjects=_HwIpLinkTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,1,1))
_HwIpLinkName_Type=OctetString
_HwIpLinkName_Object=MibScalar
hwIpLinkName=_HwIpLinkName_Object((1,3,6,1,4,1,2011,6,122,45,1,1,1),_HwIpLinkName_Type())
hwIpLinkName.setMaxAccess(_E)
if mibBuilder.loadTexts:hwIpLinkName.setStatus(_B)
_HwIpLinkStatus_Type=OctetString
_HwIpLinkStatus_Object=MibScalar
hwIpLinkStatus=_HwIpLinkStatus_Object((1,3,6,1,4,1,2011,6,122,45,1,1,2),_HwIpLinkStatus_Type())
hwIpLinkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwIpLinkStatus.setStatus(_B)
_HwIpLinkTraps_ObjectIdentity=ObjectIdentity
hwIpLinkTraps=_HwIpLinkTraps_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,2))
_HwIpLinkConformance_ObjectIdentity=ObjectIdentity
hwIpLinkConformance=_HwIpLinkConformance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,3))
_HwIpLinkCompliances_ObjectIdentity=ObjectIdentity
hwIpLinkCompliances=_HwIpLinkCompliances_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,3,1))
_HwIpLinkMibGroups_ObjectIdentity=ObjectIdentity
hwIpLinkMibGroups=_HwIpLinkMibGroups_ObjectIdentity((1,3,6,1,4,1,2011,6,122,45,3,2))
hwIpLinkObjectGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,45,3,2,1))
hwIpLinkObjectGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwIpLinkObjectGroup.setStatus(_B)
hwIpLinkUp=NotificationType((1,3,6,1,4,1,2011,6,122,45,2,1))
hwIpLinkUp.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwIpLinkUp.setStatus(_B)
hwIpLinkDown=NotificationType((1,3,6,1,4,1,2011,6,122,45,2,2))
hwIpLinkDown.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwIpLinkDown.setStatus(_B)
hwIpLinkTrapGroup=NotificationGroup((1,3,6,1,4,1,2011,6,122,45,3,2,2))
hwIpLinkTrapGroup.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hwIpLinkTrapGroup.setStatus(_B)
hwIpLinkCompliance=ModuleCompliance((1,3,6,1,4,1,2011,6,122,45,3,1,1))
hwIpLinkCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hwIpLinkCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwIplink':hwIplink,'hwIpLinkNotification':hwIpLinkNotification,'hwIpLinkTrapObjects':hwIpLinkTrapObjects,_C:hwIpLinkName,_D:hwIpLinkStatus,'hwIpLinkTraps':hwIpLinkTraps,_F:hwIpLinkUp,_G:hwIpLinkDown,'hwIpLinkConformance':hwIpLinkConformance,'hwIpLinkCompliances':hwIpLinkCompliances,'hwIpLinkCompliance':hwIpLinkCompliance,'hwIpLinkMibGroups':hwIpLinkMibGroups,_H:hwIpLinkObjectGroup,_I:hwIpLinkTrapGroup})