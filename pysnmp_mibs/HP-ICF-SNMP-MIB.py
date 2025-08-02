_b='hpicfSnmpNotificationGroup'
_a='hpicfSnmpNotifyObjectGroup'
_Z='hpicfSnmpTrapSourceAddrTableGroup'
_Y='hpicfSnmpResponseSourceAddrTableGroup'
_X='hpicfSnmpTrapSourceAddrTableCompliancesGroup'
_W='hpicfSnmpResponseSourceAddrTableCompliancesGroup'
_V='hpicfSnmpAuthFail'
_U='hpicfSnmpAuthNotifyEnable'
_T='hpicfSnmpTrapSourceAddrIfIndex'
_S='hpicfSnmpTrapSourceAddress'
_R='hpicfSnmpTrapSourceAddrPolicy'
_Q='dstIpOfRequest'
_P='configuredInterface'
_O='configuredIP'
_N='rfc1517'
_M='hpicfSnmpAuthFailIP'
_L='hpicfSnmpAuthFailIPType'
_K='hpicfSnmpAuthFailCount'
_J='hpicfSnmpTrapSourceAddressType'
_I='hpicfSnmpResponseSourceAddrIfIndex'
_H='hpicfSnmpResponseSourceAddress'
_G='hpicfSnmpResponseSourceAddrPolicy'
_F='Integer32'
_E='accessible-for-notify'
_D='hpicfSnmpResponseSourceAddressType'
_C='read-create'
_B='current'
_A='HP-ICF-SNMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfSnmpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38))
if mibBuilder.loadTexts:hpicfSnmpMIB.setRevisions(('2008-12-09 00:00','2007-08-24 00:00','2006-11-11 00:00','2006-09-01 00:00'))
_HpicfSnmpNotification_ObjectIdentity=ObjectIdentity
hpicfSnmpNotification=_HpicfSnmpNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,0))
_HpicfSnmpObjects_ObjectIdentity=ObjectIdentity
hpicfSnmpObjects=_HpicfSnmpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,1))
_HpicfSnmpConfig_ObjectIdentity=ObjectIdentity
hpicfSnmpConfig=_HpicfSnmpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1))
_HpicfSnmpGlobalCfg_ObjectIdentity=ObjectIdentity
hpicfSnmpGlobalCfg=_HpicfSnmpGlobalCfg_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1))
_HpicfSnmpResponseSourceAddrPolicyTable_Object=MibTable
hpicfSnmpResponseSourceAddrPolicyTable=_HpicfSnmpResponseSourceAddrPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1))
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrPolicyTable.setStatus(_B)
_HpicfSnmpResponseSourceAddrPolicyEntry_Object=MibTableRow
hpicfSnmpResponseSourceAddrPolicyEntry=_HpicfSnmpResponseSourceAddrPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1,1))
hpicfSnmpResponseSourceAddrPolicyEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrPolicyEntry.setStatus(_B)
_HpicfSnmpResponseSourceAddressType_Type=InetAddressType
_HpicfSnmpResponseSourceAddressType_Object=MibTableColumn
hpicfSnmpResponseSourceAddressType=_HpicfSnmpResponseSourceAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1,1,1),_HpicfSnmpResponseSourceAddressType_Type())
hpicfSnmpResponseSourceAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddressType.setStatus(_B)
class _HpicfSnmpResponseSourceAddrPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4)))
_HpicfSnmpResponseSourceAddrPolicy_Type.__name__=_F
_HpicfSnmpResponseSourceAddrPolicy_Object=MibTableColumn
hpicfSnmpResponseSourceAddrPolicy=_HpicfSnmpResponseSourceAddrPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1,1,2),_HpicfSnmpResponseSourceAddrPolicy_Type())
hpicfSnmpResponseSourceAddrPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrPolicy.setStatus(_B)
_HpicfSnmpResponseSourceAddress_Type=InetAddress
_HpicfSnmpResponseSourceAddress_Object=MibTableColumn
hpicfSnmpResponseSourceAddress=_HpicfSnmpResponseSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1,1,3),_HpicfSnmpResponseSourceAddress_Type())
hpicfSnmpResponseSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddress.setStatus(_B)
_HpicfSnmpResponseSourceAddrIfIndex_Type=InterfaceIndexOrZero
_HpicfSnmpResponseSourceAddrIfIndex_Object=MibTableColumn
hpicfSnmpResponseSourceAddrIfIndex=_HpicfSnmpResponseSourceAddrIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,1,1,4),_HpicfSnmpResponseSourceAddrIfIndex_Type())
hpicfSnmpResponseSourceAddrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrIfIndex.setStatus(_B)
_HpicfSnmpTrapSourceAddrTable_Object=MibTable
hpicfSnmpTrapSourceAddrTable=_HpicfSnmpTrapSourceAddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2))
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrTable.setStatus(_B)
_HpicfSnmpTrapSourceAddrEntry_Object=MibTableRow
hpicfSnmpTrapSourceAddrEntry=_HpicfSnmpTrapSourceAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2,1))
hpicfSnmpTrapSourceAddrEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrEntry.setStatus(_B)
_HpicfSnmpTrapSourceAddressType_Type=InetAddressType
_HpicfSnmpTrapSourceAddressType_Object=MibTableColumn
hpicfSnmpTrapSourceAddressType=_HpicfSnmpTrapSourceAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2,1,1),_HpicfSnmpTrapSourceAddressType_Type())
hpicfSnmpTrapSourceAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddressType.setStatus(_B)
class _HpicfSnmpTrapSourceAddrPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4)))
_HpicfSnmpTrapSourceAddrPolicy_Type.__name__=_F
_HpicfSnmpTrapSourceAddrPolicy_Object=MibTableColumn
hpicfSnmpTrapSourceAddrPolicy=_HpicfSnmpTrapSourceAddrPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2,1,2),_HpicfSnmpTrapSourceAddrPolicy_Type())
hpicfSnmpTrapSourceAddrPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrPolicy.setStatus(_B)
_HpicfSnmpTrapSourceAddress_Type=InetAddress
_HpicfSnmpTrapSourceAddress_Object=MibTableColumn
hpicfSnmpTrapSourceAddress=_HpicfSnmpTrapSourceAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2,1,3),_HpicfSnmpTrapSourceAddress_Type())
hpicfSnmpTrapSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddress.setStatus(_B)
_HpicfSnmpTrapSourceAddrIfIndex_Type=InterfaceIndexOrZero
_HpicfSnmpTrapSourceAddrIfIndex_Object=MibTableColumn
hpicfSnmpTrapSourceAddrIfIndex=_HpicfSnmpTrapSourceAddrIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,2,1,4),_HpicfSnmpTrapSourceAddrIfIndex_Type())
hpicfSnmpTrapSourceAddrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrIfIndex.setStatus(_B)
class _HpicfSnmpAuthNotifyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfSnmpAuthNotifyEnable_Type.__name__=_F
_HpicfSnmpAuthNotifyEnable_Object=MibScalar
hpicfSnmpAuthNotifyEnable=_HpicfSnmpAuthNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,1,1,3),_HpicfSnmpAuthNotifyEnable_Type())
hpicfSnmpAuthNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfSnmpAuthNotifyEnable.setStatus(_B)
_HpicfSnmpNotificationObjects_ObjectIdentity=ObjectIdentity
hpicfSnmpNotificationObjects=_HpicfSnmpNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,1,2))
_HpicfSnmpAuthFailCount_Type=Counter32
_HpicfSnmpAuthFailCount_Object=MibScalar
hpicfSnmpAuthFailCount=_HpicfSnmpAuthFailCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,2,1),_HpicfSnmpAuthFailCount_Type())
hpicfSnmpAuthFailCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfSnmpAuthFailCount.setStatus(_B)
_HpicfSnmpAuthFailIPType_Type=InetAddressType
_HpicfSnmpAuthFailIPType_Object=MibScalar
hpicfSnmpAuthFailIPType=_HpicfSnmpAuthFailIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,2,2),_HpicfSnmpAuthFailIPType_Type())
hpicfSnmpAuthFailIPType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfSnmpAuthFailIPType.setStatus(_B)
_HpicfSnmpAuthFailIP_Type=InetAddress
_HpicfSnmpAuthFailIP_Object=MibScalar
hpicfSnmpAuthFailIP=_HpicfSnmpAuthFailIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,38,1,2,3),_HpicfSnmpAuthFailIP_Type())
hpicfSnmpAuthFailIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfSnmpAuthFailIP.setStatus(_B)
_HpicfSnmpConformance_ObjectIdentity=ObjectIdentity
hpicfSnmpConformance=_HpicfSnmpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,2))
_HpicfSnmpCompliances_ObjectIdentity=ObjectIdentity
hpicfSnmpCompliances=_HpicfSnmpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,2,1))
_HpicfSnmpCompliancesGroups_ObjectIdentity=ObjectIdentity
hpicfSnmpCompliancesGroups=_HpicfSnmpCompliancesGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2))
hpicfSnmpResponseSourceAddrTableCompliancesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,1))
hpicfSnmpResponseSourceAddrTableCompliancesGroup.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrTableCompliancesGroup.setStatus(_B)
hpicfSnmpTrapSourceAddrTableCompliancesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,2))
hpicfSnmpTrapSourceAddrTableCompliancesGroup.setObjects(*((_A,_J),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrTableCompliancesGroup.setStatus(_B)
hpicfSnmpResponseSourceAddrTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,3))
hpicfSnmpResponseSourceAddrTableGroup.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfSnmpResponseSourceAddrTableGroup.setStatus(_B)
hpicfSnmpTrapSourceAddrTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,4))
hpicfSnmpTrapSourceAddrTableGroup.setObjects(*((_A,_D),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:hpicfSnmpTrapSourceAddrTableGroup.setStatus(_B)
hpicfSnmpNotifyObjectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,5))
hpicfSnmpNotifyObjectGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_U)))
if mibBuilder.loadTexts:hpicfSnmpNotifyObjectGroup.setStatus(_B)
hpicfSnmpAuthFail=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,38,0,1))
hpicfSnmpAuthFail.setObjects(*((_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfSnmpAuthFail.setStatus(_B)
hpicfSnmpNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,38,2,2,6))
hpicfSnmpNotificationGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:hpicfSnmpNotificationGroup.setStatus(_B)
hpicfSnmpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,38,2,1,1))
hpicfSnmpCompliance.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpicfSnmpCompliance.setStatus(_B)
hpicfSnmpCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,38,2,1,2))
hpicfSnmpCompliance1.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfSnmpCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfSnmpMIB':hpicfSnmpMIB,'hpicfSnmpNotification':hpicfSnmpNotification,_V:hpicfSnmpAuthFail,'hpicfSnmpObjects':hpicfSnmpObjects,'hpicfSnmpConfig':hpicfSnmpConfig,'hpicfSnmpGlobalCfg':hpicfSnmpGlobalCfg,'hpicfSnmpResponseSourceAddrPolicyTable':hpicfSnmpResponseSourceAddrPolicyTable,'hpicfSnmpResponseSourceAddrPolicyEntry':hpicfSnmpResponseSourceAddrPolicyEntry,_D:hpicfSnmpResponseSourceAddressType,_G:hpicfSnmpResponseSourceAddrPolicy,_H:hpicfSnmpResponseSourceAddress,_I:hpicfSnmpResponseSourceAddrIfIndex,'hpicfSnmpTrapSourceAddrTable':hpicfSnmpTrapSourceAddrTable,'hpicfSnmpTrapSourceAddrEntry':hpicfSnmpTrapSourceAddrEntry,_J:hpicfSnmpTrapSourceAddressType,_R:hpicfSnmpTrapSourceAddrPolicy,_S:hpicfSnmpTrapSourceAddress,_T:hpicfSnmpTrapSourceAddrIfIndex,_U:hpicfSnmpAuthNotifyEnable,'hpicfSnmpNotificationObjects':hpicfSnmpNotificationObjects,_K:hpicfSnmpAuthFailCount,_L:hpicfSnmpAuthFailIPType,_M:hpicfSnmpAuthFailIP,'hpicfSnmpConformance':hpicfSnmpConformance,'hpicfSnmpCompliances':hpicfSnmpCompliances,'hpicfSnmpCompliance':hpicfSnmpCompliance,'hpicfSnmpCompliance1':hpicfSnmpCompliance1,'hpicfSnmpCompliancesGroups':hpicfSnmpCompliancesGroups,_W:hpicfSnmpResponseSourceAddrTableCompliancesGroup,_X:hpicfSnmpTrapSourceAddrTableCompliancesGroup,_Y:hpicfSnmpResponseSourceAddrTableGroup,_Z:hpicfSnmpTrapSourceAddrTableGroup,_a:hpicfSnmpNotifyObjectGroup,_b:hpicfSnmpNotificationGroup})