_f='alaDHCPv6SrvLeaseUtilizationThresholdGroup'
_e='alaDHCPv6SrvNotificationsGroup'
_d='alaDHCPv6SrvGroup'
_c='alaDHCPv6RelayGroup'
_b='alaDHCPv6SrvLeaseUtilizationThresholdTrap'
_a='alaDHCPv6SrvLeaseType'
_Z='alaDHCPv6SrvLeaseValidLeaseExpiry'
_Y='alaDHCPv6SrvLeasePrefLeaseExpiry'
_X='alaDHCPv6SrvLeaseLeaseGrant'
_W='alaDHCPv6SrvGlobalClearStat'
_V='alaDHCPv6SrvGlobalRestart'
_U='alaDHCPv6SrvGlobalConfigStatus'
_T='alaDHCPv6RelayDestinationRowStatus'
_S='alaDHCPv6RelayInterfaceAdminStatus'
_R='alaDHCPv6RelayAdminStatus'
_Q='accessible-for-notify'
_P='alaDHCPv6SrvLeaseIpv6Address'
_O='alaDHCPv6RelayDestinationAddress'
_N='alaDHCPv6RelayDestinationAddressType'
_M='read-create'
_L='alaDHCPv6SrvSubnetDescriptor'
_K='alaDHCPv6SrvLeaseThresholdStatus'
_J='not-accessible'
_I='disable'
_H='enable'
_G='ipv6IfIndex'
_F='IPV6-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-DHCPV6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Ipv6,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1Ipv6')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ipv6IfIndex,=mibBuilder.importSymbols(_F,_G)
Ipv6Address,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6IfIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
alcatelIND1DHCPv6MIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2))
if mibBuilder.loadTexts:alcatelIND1DHCPv6MIB.setRevisions(('2013-03-22 00:00',))
_AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1DHCPv6MIBNotifications=_AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,0))
_AlcatelIND1DHCPv6MIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DHCPv6MIBObjects=_AlcatelIND1DHCPv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,1))
_AlaDHCPv6RelayConfig_ObjectIdentity=ObjectIdentity
alaDHCPv6RelayConfig=_AlaDHCPv6RelayConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,1))
class _AlaDHCPv6RelayAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaDHCPv6RelayAdminStatus_Type.__name__=_C
_AlaDHCPv6RelayAdminStatus_Object=MibScalar
alaDHCPv6RelayAdminStatus=_AlaDHCPv6RelayAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,1,1),_AlaDHCPv6RelayAdminStatus_Type())
alaDHCPv6RelayAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHCPv6RelayAdminStatus.setStatus(_A)
_AlaDHCPv6SrvConfig_ObjectIdentity=ObjectIdentity
alaDHCPv6SrvConfig=_AlaDHCPv6SrvConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,2))
class _AlaDHCPv6SrvGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaDHCPv6SrvGlobalConfigStatus_Type.__name__=_C
_AlaDHCPv6SrvGlobalConfigStatus_Object=MibScalar
alaDHCPv6SrvGlobalConfigStatus=_AlaDHCPv6SrvGlobalConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,2,1),_AlaDHCPv6SrvGlobalConfigStatus_Type())
alaDHCPv6SrvGlobalConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHCPv6SrvGlobalConfigStatus.setStatus(_A)
class _AlaDHCPv6SrvGlobalRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('restart',2)))
_AlaDHCPv6SrvGlobalRestart_Type.__name__=_C
_AlaDHCPv6SrvGlobalRestart_Object=MibScalar
alaDHCPv6SrvGlobalRestart=_AlaDHCPv6SrvGlobalRestart_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,2,2),_AlaDHCPv6SrvGlobalRestart_Type())
alaDHCPv6SrvGlobalRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHCPv6SrvGlobalRestart.setStatus(_A)
class _AlaDHCPv6SrvGlobalClearStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('reset',2)))
_AlaDHCPv6SrvGlobalClearStat_Type.__name__=_C
_AlaDHCPv6SrvGlobalClearStat_Object=MibScalar
alaDHCPv6SrvGlobalClearStat=_AlaDHCPv6SrvGlobalClearStat_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,2,3),_AlaDHCPv6SrvGlobalClearStat_Type())
alaDHCPv6SrvGlobalClearStat.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDHCPv6SrvGlobalClearStat.setStatus(_A)
_AlaDHCPv6RelayInterfaceTable_Object=MibTable
alaDHCPv6RelayInterfaceTable=_AlaDHCPv6RelayInterfaceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,3))
if mibBuilder.loadTexts:alaDHCPv6RelayInterfaceTable.setStatus(_A)
_AlaDHCPv6RelayInterfaceEntry_Object=MibTableRow
alaDHCPv6RelayInterfaceEntry=_AlaDHCPv6RelayInterfaceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,3,1))
alaDHCPv6RelayInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:alaDHCPv6RelayInterfaceEntry.setStatus(_A)
class _AlaDHCPv6RelayInterfaceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AlaDHCPv6RelayInterfaceAdminStatus_Type.__name__=_C
_AlaDHCPv6RelayInterfaceAdminStatus_Object=MibTableColumn
alaDHCPv6RelayInterfaceAdminStatus=_AlaDHCPv6RelayInterfaceAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,3,1,1),_AlaDHCPv6RelayInterfaceAdminStatus_Type())
alaDHCPv6RelayInterfaceAdminStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:alaDHCPv6RelayInterfaceAdminStatus.setStatus(_A)
_AlaDHCPv6RelayDestinationTable_Object=MibTable
alaDHCPv6RelayDestinationTable=_AlaDHCPv6RelayDestinationTable_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,4))
if mibBuilder.loadTexts:alaDHCPv6RelayDestinationTable.setStatus(_A)
_AlaDHCPv6RelayDestinationEntry_Object=MibTableRow
alaDHCPv6RelayDestinationEntry=_AlaDHCPv6RelayDestinationEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,4,1))
alaDHCPv6RelayDestinationEntry.setIndexNames((0,_F,_G),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:alaDHCPv6RelayDestinationEntry.setStatus(_A)
_AlaDHCPv6RelayDestinationAddressType_Type=InetAddressType
_AlaDHCPv6RelayDestinationAddressType_Object=MibTableColumn
alaDHCPv6RelayDestinationAddressType=_AlaDHCPv6RelayDestinationAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,4,1,1),_AlaDHCPv6RelayDestinationAddressType_Type())
alaDHCPv6RelayDestinationAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:alaDHCPv6RelayDestinationAddressType.setStatus(_A)
_AlaDHCPv6RelayDestinationAddress_Type=InetAddress
_AlaDHCPv6RelayDestinationAddress_Object=MibTableColumn
alaDHCPv6RelayDestinationAddress=_AlaDHCPv6RelayDestinationAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,4,1,2),_AlaDHCPv6RelayDestinationAddress_Type())
alaDHCPv6RelayDestinationAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:alaDHCPv6RelayDestinationAddress.setStatus(_A)
_AlaDHCPv6RelayDestinationRowStatus_Type=RowStatus
_AlaDHCPv6RelayDestinationRowStatus_Object=MibTableColumn
alaDHCPv6RelayDestinationRowStatus=_AlaDHCPv6RelayDestinationRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,4,1,3),_AlaDHCPv6RelayDestinationRowStatus_Type())
alaDHCPv6RelayDestinationRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:alaDHCPv6RelayDestinationRowStatus.setStatus(_A)
_AlaDHCPv6SrvLease_ObjectIdentity=ObjectIdentity
alaDHCPv6SrvLease=_AlaDHCPv6SrvLease_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5))
_AlaDHCPv6SrvLeaseTable_Object=MibTable
alaDHCPv6SrvLeaseTable=_AlaDHCPv6SrvLeaseTable_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1))
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseTable.setStatus(_A)
_AlaDHCPv6SrvLeaseEntry_Object=MibTableRow
alaDHCPv6SrvLeaseEntry=_AlaDHCPv6SrvLeaseEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1))
alaDHCPv6SrvLeaseEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseEntry.setStatus(_A)
_AlaDHCPv6SrvLeaseIpv6Address_Type=Ipv6Address
_AlaDHCPv6SrvLeaseIpv6Address_Object=MibTableColumn
alaDHCPv6SrvLeaseIpv6Address=_AlaDHCPv6SrvLeaseIpv6Address_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1,1),_AlaDHCPv6SrvLeaseIpv6Address_Type())
alaDHCPv6SrvLeaseIpv6Address.setMaxAccess(_J)
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseIpv6Address.setStatus(_A)
_AlaDHCPv6SrvLeaseLeaseGrant_Type=DateAndTime
_AlaDHCPv6SrvLeaseLeaseGrant_Object=MibTableColumn
alaDHCPv6SrvLeaseLeaseGrant=_AlaDHCPv6SrvLeaseLeaseGrant_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1,2),_AlaDHCPv6SrvLeaseLeaseGrant_Type())
alaDHCPv6SrvLeaseLeaseGrant.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseLeaseGrant.setStatus(_A)
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Type=DateAndTime
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Object=MibTableColumn
alaDHCPv6SrvLeasePrefLeaseExpiry=_AlaDHCPv6SrvLeasePrefLeaseExpiry_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1,3),_AlaDHCPv6SrvLeasePrefLeaseExpiry_Type())
alaDHCPv6SrvLeasePrefLeaseExpiry.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHCPv6SrvLeasePrefLeaseExpiry.setStatus(_A)
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Type=DateAndTime
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Object=MibTableColumn
alaDHCPv6SrvLeaseValidLeaseExpiry=_AlaDHCPv6SrvLeaseValidLeaseExpiry_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1,4),_AlaDHCPv6SrvLeaseValidLeaseExpiry_Type())
alaDHCPv6SrvLeaseValidLeaseExpiry.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseValidLeaseExpiry.setStatus(_A)
class _AlaDHCPv6SrvLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unavailable',1),('dynamic',2),('manual',3)))
_AlaDHCPv6SrvLeaseType_Type.__name__=_C
_AlaDHCPv6SrvLeaseType_Object=MibTableColumn
alaDHCPv6SrvLeaseType=_AlaDHCPv6SrvLeaseType_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,5,1,1,5),_AlaDHCPv6SrvLeaseType_Type())
alaDHCPv6SrvLeaseType.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseType.setStatus(_A)
_AlaDHCPv6SrvTrapsObj_ObjectIdentity=ObjectIdentity
alaDHCPv6SrvTrapsObj=_AlaDHCPv6SrvTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,6))
class _AlaDHCPv6SrvLeaseThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('crossedBelow80Threshold',1),('crossedAbove80Threshold',2),('reached100Threshold',3)))
_AlaDHCPv6SrvLeaseThresholdStatus_Type.__name__=_C
_AlaDHCPv6SrvLeaseThresholdStatus_Object=MibScalar
alaDHCPv6SrvLeaseThresholdStatus=_AlaDHCPv6SrvLeaseThresholdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,6,1),_AlaDHCPv6SrvLeaseThresholdStatus_Type())
alaDHCPv6SrvLeaseThresholdStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseThresholdStatus.setStatus(_A)
_AlaDHCPv6SrvSubnetDescriptor_Type=DisplayString
_AlaDHCPv6SrvSubnetDescriptor_Object=MibScalar
alaDHCPv6SrvSubnetDescriptor=_AlaDHCPv6SrvSubnetDescriptor_Object((1,3,6,1,4,1,6486,801,1,2,1,29,2,1,6,2),_AlaDHCPv6SrvSubnetDescriptor_Type())
alaDHCPv6SrvSubnetDescriptor.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaDHCPv6SrvSubnetDescriptor.setStatus(_A)
_AlcatelIND1DHCPv6MIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DHCPv6MIBConformance=_AlcatelIND1DHCPv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,2))
_AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DHCPv6MIBCompliances=_AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,1))
_AlcatelIND1DHCPv6MIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DHCPv6MIBGroups=_AlcatelIND1DHCPv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,2))
alaDHCPv6RelayGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,2,1))
alaDHCPv6RelayGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:alaDHCPv6RelayGroup.setStatus(_A)
alaDHCPv6SrvGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,2,2))
alaDHCPv6SrvGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:alaDHCPv6SrvGroup.setStatus(_A)
alaDHCPv6SrvLeaseUtilizationThresholdGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,2,4))
alaDHCPv6SrvLeaseUtilizationThresholdGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseUtilizationThresholdGroup.setStatus(_A)
alaDHCPv6SrvLeaseUtilizationThresholdTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,29,2,0,1))
alaDHCPv6SrvLeaseUtilizationThresholdTrap.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaDHCPv6SrvLeaseUtilizationThresholdTrap.setStatus(_A)
alaDHCPv6SrvNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,2,3))
alaDHCPv6SrvNotificationsGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:alaDHCPv6SrvNotificationsGroup.setStatus(_A)
alaDHCPv6Compliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,29,2,2,1,1))
alaDHCPv6Compliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:alaDHCPv6Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1DHCPv6MIB':alcatelIND1DHCPv6MIB,'alcatelIND1DHCPv6MIBNotifications':alcatelIND1DHCPv6MIBNotifications,_b:alaDHCPv6SrvLeaseUtilizationThresholdTrap,'alcatelIND1DHCPv6MIBObjects':alcatelIND1DHCPv6MIBObjects,'alaDHCPv6RelayConfig':alaDHCPv6RelayConfig,_R:alaDHCPv6RelayAdminStatus,'alaDHCPv6SrvConfig':alaDHCPv6SrvConfig,_U:alaDHCPv6SrvGlobalConfigStatus,_V:alaDHCPv6SrvGlobalRestart,_W:alaDHCPv6SrvGlobalClearStat,'alaDHCPv6RelayInterfaceTable':alaDHCPv6RelayInterfaceTable,'alaDHCPv6RelayInterfaceEntry':alaDHCPv6RelayInterfaceEntry,_S:alaDHCPv6RelayInterfaceAdminStatus,'alaDHCPv6RelayDestinationTable':alaDHCPv6RelayDestinationTable,'alaDHCPv6RelayDestinationEntry':alaDHCPv6RelayDestinationEntry,_N:alaDHCPv6RelayDestinationAddressType,_O:alaDHCPv6RelayDestinationAddress,_T:alaDHCPv6RelayDestinationRowStatus,'alaDHCPv6SrvLease':alaDHCPv6SrvLease,'alaDHCPv6SrvLeaseTable':alaDHCPv6SrvLeaseTable,'alaDHCPv6SrvLeaseEntry':alaDHCPv6SrvLeaseEntry,_P:alaDHCPv6SrvLeaseIpv6Address,_X:alaDHCPv6SrvLeaseLeaseGrant,_Y:alaDHCPv6SrvLeasePrefLeaseExpiry,_Z:alaDHCPv6SrvLeaseValidLeaseExpiry,_a:alaDHCPv6SrvLeaseType,'alaDHCPv6SrvTrapsObj':alaDHCPv6SrvTrapsObj,_K:alaDHCPv6SrvLeaseThresholdStatus,_L:alaDHCPv6SrvSubnetDescriptor,'alcatelIND1DHCPv6MIBConformance':alcatelIND1DHCPv6MIBConformance,'alcatelIND1DHCPv6MIBCompliances':alcatelIND1DHCPv6MIBCompliances,'alaDHCPv6Compliance':alaDHCPv6Compliance,'alcatelIND1DHCPv6MIBGroups':alcatelIND1DHCPv6MIBGroups,_c:alaDHCPv6RelayGroup,_d:alaDHCPv6SrvGroup,_e:alaDHCPv6SrvNotificationsGroup,_f:alaDHCPv6SrvLeaseUtilizationThresholdGroup})