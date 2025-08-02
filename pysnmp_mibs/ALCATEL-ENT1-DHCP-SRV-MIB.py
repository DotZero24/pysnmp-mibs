_X='alaDhcpSrvLeaseUtilizationThresholdGroup'
_W='alaDhcpSrvNotificationGroup'
_V='alaDhcpSrvLeaseGroup'
_U='alaDhcpSrvGlobalConfigGroup'
_T='alaDhcpSrvLeaseUtilizationThresholdTrap'
_S='alaDhcpSrvLeaseType'
_R='alaDhcpSrvLeaseLeaseExpiry'
_Q='alaDhcpSrvLeaseLeaseGrant'
_P='alaDhcpSrvLeaseMACAddress'
_O='alaDhcpSrvGlobalClearStat'
_N='alaDhcpSrvGlobalRestart'
_M='alaDhcpSrvGlobalConfigStatus'
_L='accessible-for-notify'
_K='not-accessible'
_J='alaDhcpSrvLeaseInetAddress'
_I='alaDhcpSrvLeaseInetAddressType'
_H='InetAddress'
_G='alaDhcpSrvSubnetDescriptor'
_F='alaDhcpSrvLeaseThresholdStatus'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-ENT1-DHCP-SRV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1DhcpSrv,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1DhcpSrv')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention')
alcatelIND1DhcpSrvMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIB.setRevisions(('2009-10-26 00:00',))
_AlcatelIND1DhcpSrvMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1DhcpSrvMIBNotifications=_AlcatelIND1DhcpSrvMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,0))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBNotifications.setStatus(_A)
_AlcatelIND1DhcpSrvMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1DhcpSrvMIBObjects=_AlcatelIND1DhcpSrvMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,1))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBObjects.setStatus(_A)
class _AlaDhcpSrvGlobalConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaDhcpSrvGlobalConfigStatus_Type.__name__=_C
_AlaDhcpSrvGlobalConfigStatus_Object=MibScalar
alaDhcpSrvGlobalConfigStatus=_AlaDhcpSrvGlobalConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,1),_AlaDhcpSrvGlobalConfigStatus_Type())
alaDhcpSrvGlobalConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDhcpSrvGlobalConfigStatus.setStatus(_A)
class _AlaDhcpSrvGlobalRestart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('restart',2)))
_AlaDhcpSrvGlobalRestart_Type.__name__=_C
_AlaDhcpSrvGlobalRestart_Object=MibScalar
alaDhcpSrvGlobalRestart=_AlaDhcpSrvGlobalRestart_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,2),_AlaDhcpSrvGlobalRestart_Type())
alaDhcpSrvGlobalRestart.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDhcpSrvGlobalRestart.setStatus(_A)
class _AlaDhcpSrvGlobalClearStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('reset',2)))
_AlaDhcpSrvGlobalClearStat_Type.__name__=_C
_AlaDhcpSrvGlobalClearStat_Object=MibScalar
alaDhcpSrvGlobalClearStat=_AlaDhcpSrvGlobalClearStat_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,3),_AlaDhcpSrvGlobalClearStat_Type())
alaDhcpSrvGlobalClearStat.setMaxAccess(_E)
if mibBuilder.loadTexts:alaDhcpSrvGlobalClearStat.setStatus(_A)
_AlaDhcpSrvLease_ObjectIdentity=ObjectIdentity
alaDhcpSrvLease=_AlaDhcpSrvLease_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4))
_AlaDhcpSrvLeaseTable_Object=MibTable
alaDhcpSrvLeaseTable=_AlaDhcpSrvLeaseTable_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1))
if mibBuilder.loadTexts:alaDhcpSrvLeaseTable.setStatus(_A)
_AlaDhcpSrvLeaseEntry_Object=MibTableRow
alaDhcpSrvLeaseEntry=_AlaDhcpSrvLeaseEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1))
alaDhcpSrvLeaseEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:alaDhcpSrvLeaseEntry.setStatus(_A)
_AlaDhcpSrvLeaseInetAddressType_Type=InetAddressType
_AlaDhcpSrvLeaseInetAddressType_Object=MibTableColumn
alaDhcpSrvLeaseInetAddressType=_AlaDhcpSrvLeaseInetAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,1),_AlaDhcpSrvLeaseInetAddressType_Type())
alaDhcpSrvLeaseInetAddressType.setMaxAccess(_K)
if mibBuilder.loadTexts:alaDhcpSrvLeaseInetAddressType.setStatus(_A)
class _AlaDhcpSrvLeaseInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AlaDhcpSrvLeaseInetAddress_Type.__name__=_H
_AlaDhcpSrvLeaseInetAddress_Object=MibTableColumn
alaDhcpSrvLeaseInetAddress=_AlaDhcpSrvLeaseInetAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,2),_AlaDhcpSrvLeaseInetAddress_Type())
alaDhcpSrvLeaseInetAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:alaDhcpSrvLeaseInetAddress.setStatus(_A)
_AlaDhcpSrvLeaseMACAddress_Type=MacAddress
_AlaDhcpSrvLeaseMACAddress_Object=MibTableColumn
alaDhcpSrvLeaseMACAddress=_AlaDhcpSrvLeaseMACAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,3),_AlaDhcpSrvLeaseMACAddress_Type())
alaDhcpSrvLeaseMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDhcpSrvLeaseMACAddress.setStatus(_A)
_AlaDhcpSrvLeaseLeaseGrant_Type=DateAndTime
_AlaDhcpSrvLeaseLeaseGrant_Object=MibTableColumn
alaDhcpSrvLeaseLeaseGrant=_AlaDhcpSrvLeaseLeaseGrant_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,4),_AlaDhcpSrvLeaseLeaseGrant_Type())
alaDhcpSrvLeaseLeaseGrant.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDhcpSrvLeaseLeaseGrant.setStatus(_A)
_AlaDhcpSrvLeaseLeaseExpiry_Type=DateAndTime
_AlaDhcpSrvLeaseLeaseExpiry_Object=MibTableColumn
alaDhcpSrvLeaseLeaseExpiry=_AlaDhcpSrvLeaseLeaseExpiry_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,5),_AlaDhcpSrvLeaseLeaseExpiry_Type())
alaDhcpSrvLeaseLeaseExpiry.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDhcpSrvLeaseLeaseExpiry.setStatus(_A)
class _AlaDhcpSrvLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unavailable',1),('dynamic',2),('manual',3)))
_AlaDhcpSrvLeaseType_Type.__name__=_C
_AlaDhcpSrvLeaseType_Object=MibTableColumn
alaDhcpSrvLeaseType=_AlaDhcpSrvLeaseType_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,4,1,1,6),_AlaDhcpSrvLeaseType_Type())
alaDhcpSrvLeaseType.setMaxAccess(_D)
if mibBuilder.loadTexts:alaDhcpSrvLeaseType.setStatus(_A)
_AlaDhcpSrvTrapsObj_ObjectIdentity=ObjectIdentity
alaDhcpSrvTrapsObj=_AlaDhcpSrvTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,5))
class _AlaDhcpSrvLeaseThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('crossedBelow80Threshold',1),('crossedAbove80Threshold',2),('reached100Threshold',3)))
_AlaDhcpSrvLeaseThresholdStatus_Type.__name__=_C
_AlaDhcpSrvLeaseThresholdStatus_Object=MibScalar
alaDhcpSrvLeaseThresholdStatus=_AlaDhcpSrvLeaseThresholdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,5,1),_AlaDhcpSrvLeaseThresholdStatus_Type())
alaDhcpSrvLeaseThresholdStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:alaDhcpSrvLeaseThresholdStatus.setStatus(_A)
_AlaDhcpSrvSubnetDescriptor_Type=DisplayString
_AlaDhcpSrvSubnetDescriptor_Object=MibScalar
alaDhcpSrvSubnetDescriptor=_AlaDhcpSrvSubnetDescriptor_Object((1,3,6,1,4,1,6486,801,1,2,1,59,1,1,5,2),_AlaDhcpSrvSubnetDescriptor_Type())
alaDhcpSrvSubnetDescriptor.setMaxAccess(_L)
if mibBuilder.loadTexts:alaDhcpSrvSubnetDescriptor.setStatus(_A)
_AlcatelIND1DhcpSrvMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1DhcpSrvMIBConformance=_AlcatelIND1DhcpSrvMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,2))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBConformance.setStatus(_A)
_AlcatelIND1DhcpSrvMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1DhcpSrvMIBGroups=_AlcatelIND1DhcpSrvMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,1))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBGroups.setStatus(_A)
_AlcatelIND1DhcpSrvMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1DhcpSrvMIBCompliances=_AlcatelIND1DhcpSrvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,2))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBCompliances.setStatus(_A)
alaDhcpSrvGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,1,1))
alaDhcpSrvGlobalConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:alaDhcpSrvGlobalConfigGroup.setStatus(_A)
alaDhcpSrvLeaseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,1,2))
alaDhcpSrvLeaseGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:alaDhcpSrvLeaseGroup.setStatus(_A)
alaDhcpSrvLeaseUtilizationThresholdGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,1,4))
alaDhcpSrvLeaseUtilizationThresholdGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:alaDhcpSrvLeaseUtilizationThresholdGroup.setStatus(_A)
alaDhcpSrvLeaseUtilizationThresholdTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,59,1,0,1))
alaDhcpSrvLeaseUtilizationThresholdTrap.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:alaDhcpSrvLeaseUtilizationThresholdTrap.setStatus(_A)
alaDhcpSrvNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,1,3))
alaDhcpSrvNotificationGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:alaDhcpSrvNotificationGroup.setStatus(_A)
alcatelIND1DhcpSrvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,59,1,2,2,1))
alcatelIND1DhcpSrvMIBCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:alcatelIND1DhcpSrvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1DhcpSrvMIB':alcatelIND1DhcpSrvMIB,'alcatelIND1DhcpSrvMIBNotifications':alcatelIND1DhcpSrvMIBNotifications,_T:alaDhcpSrvLeaseUtilizationThresholdTrap,'alcatelIND1DhcpSrvMIBObjects':alcatelIND1DhcpSrvMIBObjects,_M:alaDhcpSrvGlobalConfigStatus,_N:alaDhcpSrvGlobalRestart,_O:alaDhcpSrvGlobalClearStat,'alaDhcpSrvLease':alaDhcpSrvLease,'alaDhcpSrvLeaseTable':alaDhcpSrvLeaseTable,'alaDhcpSrvLeaseEntry':alaDhcpSrvLeaseEntry,_I:alaDhcpSrvLeaseInetAddressType,_J:alaDhcpSrvLeaseInetAddress,_P:alaDhcpSrvLeaseMACAddress,_Q:alaDhcpSrvLeaseLeaseGrant,_R:alaDhcpSrvLeaseLeaseExpiry,_S:alaDhcpSrvLeaseType,'alaDhcpSrvTrapsObj':alaDhcpSrvTrapsObj,_F:alaDhcpSrvLeaseThresholdStatus,_G:alaDhcpSrvSubnetDescriptor,'alcatelIND1DhcpSrvMIBConformance':alcatelIND1DhcpSrvMIBConformance,'alcatelIND1DhcpSrvMIBGroups':alcatelIND1DhcpSrvMIBGroups,_U:alaDhcpSrvGlobalConfigGroup,_V:alaDhcpSrvLeaseGroup,_W:alaDhcpSrvNotificationGroup,_X:alaDhcpSrvLeaseUtilizationThresholdGroup,'alcatelIND1DhcpSrvMIBCompliances':alcatelIND1DhcpSrvMIBCompliances,'alcatelIND1DhcpSrvMIBCompliance':alcatelIND1DhcpSrvMIBCompliance})