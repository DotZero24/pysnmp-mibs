_I='hwSlbTrapGroup'
_H='hwSlbObjectGroup'
_G='hwSlbRserverStateDown'
_F='hwSlbRserverStateUp'
_E='accessible-for-notify'
_D='hwSlbServerIp'
_C='hwSlbServerIndex'
_B='current'
_A='HUAWEI-SECURITY-SLB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwSlb=ModuleIdentity((1,3,6,1,4,1,2011,6,122,67))
if mibBuilder.loadTexts:hwSlb.setRevisions(('2014-01-07 16:09',))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwSlbNotification_ObjectIdentity=ObjectIdentity
hwSlbNotification=_HwSlbNotification_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,1))
_HwSlbTrapObjects_ObjectIdentity=ObjectIdentity
hwSlbTrapObjects=_HwSlbTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,1,1))
_HwSlbServerIndex_Type=Gauge32
_HwSlbServerIndex_Object=MibScalar
hwSlbServerIndex=_HwSlbServerIndex_Object((1,3,6,1,4,1,2011,6,122,67,1,1,1),_HwSlbServerIndex_Type())
hwSlbServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSlbServerIndex.setStatus(_B)
_HwSlbServerIp_Type=IpAddress
_HwSlbServerIp_Object=MibScalar
hwSlbServerIp=_HwSlbServerIp_Object((1,3,6,1,4,1,2011,6,122,67,1,1,2),_HwSlbServerIp_Type())
hwSlbServerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:hwSlbServerIp.setStatus(_B)
_HwSlbTraps_ObjectIdentity=ObjectIdentity
hwSlbTraps=_HwSlbTraps_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,2))
_HwSlbConformance_ObjectIdentity=ObjectIdentity
hwSlbConformance=_HwSlbConformance_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,3))
_HwSlbCompliances_ObjectIdentity=ObjectIdentity
hwSlbCompliances=_HwSlbCompliances_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,3,1))
_HwSlbMibGroups_ObjectIdentity=ObjectIdentity
hwSlbMibGroups=_HwSlbMibGroups_ObjectIdentity((1,3,6,1,4,1,2011,6,122,67,3,2))
hwSlbObjectGroup=ObjectGroup((1,3,6,1,4,1,2011,6,122,67,3,2,1))
hwSlbObjectGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwSlbObjectGroup.setStatus(_B)
hwSlbRserverStateUp=NotificationType((1,3,6,1,4,1,2011,6,122,67,2,1))
hwSlbRserverStateUp.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwSlbRserverStateUp.setStatus(_B)
hwSlbRserverStateDown=NotificationType((1,3,6,1,4,1,2011,6,122,67,2,2))
hwSlbRserverStateDown.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hwSlbRserverStateDown.setStatus(_B)
hwSlbTrapGroup=NotificationGroup((1,3,6,1,4,1,2011,6,122,67,3,2,2))
hwSlbTrapGroup.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hwSlbTrapGroup.setStatus(_B)
hwSlbCompliance=ModuleCompliance((1,3,6,1,4,1,2011,6,122,67,3,1,1))
hwSlbCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hwSlbCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwSlb':hwSlb,'hwSlbNotification':hwSlbNotification,'hwSlbTrapObjects':hwSlbTrapObjects,_C:hwSlbServerIndex,_D:hwSlbServerIp,'hwSlbTraps':hwSlbTraps,_F:hwSlbRserverStateUp,_G:hwSlbRserverStateDown,'hwSlbConformance':hwSlbConformance,'hwSlbCompliances':hwSlbCompliances,'hwSlbCompliance':hwSlbCompliance,'hwSlbMibGroups':hwSlbMibGroups,_H:hwSlbObjectGroup,_I:hwSlbTrapGroup})