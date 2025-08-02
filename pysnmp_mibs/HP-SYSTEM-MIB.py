_s='hpNotificationsGroup'
_r='hpNotificationsConfigGroup'
_q='hpStatusGroup'
_p='hpEnvGroup'
_o='hpConfigGroup'
_n='hpSystemGroup'
_m='hpAdminAuthFailure'
_l='hpDistributionEvent'
_k='hpFailover'
_j='temperatureAlarm'
_i='fanDown'
_h='hpAdminAuthFailureNotificationEnabled'
_g='hpDistributionNotificationEnabled'
_f='hpFailoverNotificationEnabled'
_e='hpNumClients'
_d='hpNumAccessControllers'
_c='hpTechSupportEnabled'
_b='hpPeerIpAddress'
_a='hpState'
_Z='hpSystemID'
_Y='hpName'
_X='hpFanSpeed'
_W='hpFanOperational'
_V='hpChassisTemperature'
_U='hpPowerSupplyTemperature'
_T='hpProductLastChange'
_S='hpProductSerialNumber'
_R='hpProductSWVersion'
_Q='hpProductHWVersion'
_P='hpProductDescription'
_O='DisplayString'
_N='OctetString'
_M='hpFailedAdminIpAddress'
_L='hpDistributionStatus'
_K='hpDistributionType'
_J='hpIpAddress'
_I='hpCpuTemperature'
_H='unknown'
_G='TruthValue'
_F='hpFanNumber'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='HP-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpProcurveCommon,=mibBuilder.importSymbols('HP-BASE-MIB','hpProcurveCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention',_G)
hpProcurveSystem=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1))
if mibBuilder.loadTexts:hpProcurveSystem.setRevisions(('2005-02-01 14:55',))
_HpSystemTraps_ObjectIdentity=ObjectIdentity
hpSystemTraps=_HpSystemTraps_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0))
_HpProcurveSysMib_ObjectIdentity=ObjectIdentity
hpProcurveSysMib=_HpProcurveSysMib_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1))
_HpProductDescription_Type=OctetString
_HpProductDescription_Object=MibScalar
hpProductDescription=_HpProductDescription_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,1),_HpProductDescription_Type())
hpProductDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpProductDescription.setStatus(_B)
_HpProductHWVersion_Type=OctetString
_HpProductHWVersion_Object=MibScalar
hpProductHWVersion=_HpProductHWVersion_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,2),_HpProductHWVersion_Type())
hpProductHWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpProductHWVersion.setStatus(_B)
_HpProductSWVersion_Type=OctetString
_HpProductSWVersion_Object=MibScalar
hpProductSWVersion=_HpProductSWVersion_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,3),_HpProductSWVersion_Type())
hpProductSWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpProductSWVersion.setStatus(_B)
_HpProductSerialNumber_Type=OctetString
_HpProductSerialNumber_Object=MibScalar
hpProductSerialNumber=_HpProductSerialNumber_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,4),_HpProductSerialNumber_Type())
hpProductSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpProductSerialNumber.setStatus(_B)
_HpProductLastChange_Type=OctetString
_HpProductLastChange_Object=MibScalar
hpProductLastChange=_HpProductLastChange_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,5),_HpProductLastChange_Type())
hpProductLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:hpProductLastChange.setStatus(_B)
_HpCpuTemperature_Type=OctetString
_HpCpuTemperature_Object=MibScalar
hpCpuTemperature=_HpCpuTemperature_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,6),_HpCpuTemperature_Type())
hpCpuTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hpCpuTemperature.setStatus(_B)
_HpPowerSupplyTemperature_Type=OctetString
_HpPowerSupplyTemperature_Object=MibScalar
hpPowerSupplyTemperature=_HpPowerSupplyTemperature_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,7),_HpPowerSupplyTemperature_Type())
hpPowerSupplyTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hpPowerSupplyTemperature.setStatus('deprecated')
_HpChassisTemperature_Type=OctetString
_HpChassisTemperature_Object=MibScalar
hpChassisTemperature=_HpChassisTemperature_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,8),_HpChassisTemperature_Type())
hpChassisTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hpChassisTemperature.setStatus(_B)
_HpFanStatusTable_Object=MibTable
hpFanStatusTable=_HpFanStatusTable_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,9))
if mibBuilder.loadTexts:hpFanStatusTable.setStatus(_B)
_HpFanStatusEntry_Object=MibTableRow
hpFanStatusEntry=_HpFanStatusEntry_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,9,1))
hpFanStatusEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:hpFanStatusEntry.setStatus(_B)
class _HpFanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cpu',1),('power',2)))
_HpFanNumber_Type.__name__=_E
_HpFanNumber_Object=MibTableColumn
hpFanNumber=_HpFanNumber_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,9,1,1),_HpFanNumber_Type())
hpFanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFanNumber.setStatus(_B)
class _HpFanOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HpFanOperational_Type.__name__=_E
_HpFanOperational_Object=MibTableColumn
hpFanOperational=_HpFanOperational_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,9,1,2),_HpFanOperational_Type())
hpFanOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFanOperational.setStatus(_B)
_HpFanSpeed_Type=Integer32
_HpFanSpeed_Object=MibTableColumn
hpFanSpeed=_HpFanSpeed_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,1,9,1,3),_HpFanSpeed_Type())
hpFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFanSpeed.setStatus(_B)
_HpSystemMIBObjects_ObjectIdentity=ObjectIdentity
hpSystemMIBObjects=_HpSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2))
_HpConfig_ObjectIdentity=ObjectIdentity
hpConfig=_HpConfig_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1))
class _HpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpName_Type.__name__=_O
_HpName_Object=MibScalar
hpName=_HpName_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,2),_HpName_Type())
hpName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpName.setStatus(_B)
class _HpSystemID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpSystemID_Type.__name__=_N
_HpSystemID_Object=MibScalar
hpSystemID=_HpSystemID_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,3),_HpSystemID_Type())
hpSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSystemID.setStatus(_B)
class _HpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('up',2),('down',3),('primary',4),('secondary',5)))
_HpState_Type.__name__=_E
_HpState_Object=MibScalar
hpState=_HpState_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,4),_HpState_Type())
hpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpState.setStatus(_B)
class _HpDistributionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('rightsPush',2)))
_HpDistributionType_Type.__name__=_E
_HpDistributionType_Object=MibScalar
hpDistributionType=_HpDistributionType_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,5),_HpDistributionType_Type())
hpDistributionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDistributionType.setStatus(_B)
class _HpDistributionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('succeeded',2),('failed',3)))
_HpDistributionStatus_Type.__name__=_E
_HpDistributionStatus_Object=MibScalar
hpDistributionStatus=_HpDistributionStatus_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,6),_HpDistributionStatus_Type())
hpDistributionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpDistributionStatus.setStatus(_B)
_HpIpAddress_Type=IpAddress
_HpIpAddress_Object=MibScalar
hpIpAddress=_HpIpAddress_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,7),_HpIpAddress_Type())
hpIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpIpAddress.setStatus(_B)
_HpPeerIpAddress_Type=IpAddress
_HpPeerIpAddress_Object=MibScalar
hpPeerIpAddress=_HpPeerIpAddress_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,8),_HpPeerIpAddress_Type())
hpPeerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpPeerIpAddress.setStatus(_B)
class _HpTechSupportEnabled_Type(TruthValue):defaultValue=2
_HpTechSupportEnabled_Type.__name__=_G
_HpTechSupportEnabled_Object=MibScalar
hpTechSupportEnabled=_HpTechSupportEnabled_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,9),_HpTechSupportEnabled_Type())
hpTechSupportEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpTechSupportEnabled.setStatus(_B)
_HpFailedAdminIpAddress_Type=IpAddress
_HpFailedAdminIpAddress_Object=MibScalar
hpFailedAdminIpAddress=_HpFailedAdminIpAddress_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,1,10),_HpFailedAdminIpAddress_Type())
hpFailedAdminIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpFailedAdminIpAddress.setStatus(_B)
_HpStatus_ObjectIdentity=ObjectIdentity
hpStatus=_HpStatus_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,2))
_HpNumAccessControllers_Type=Unsigned32
_HpNumAccessControllers_Object=MibScalar
hpNumAccessControllers=_HpNumAccessControllers_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,2,1),_HpNumAccessControllers_Type())
hpNumAccessControllers.setMaxAccess(_C)
if mibBuilder.loadTexts:hpNumAccessControllers.setStatus(_B)
_HpNumClients_Type=Gauge32
_HpNumClients_Object=MibScalar
hpNumClients=_HpNumClients_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,2,2),_HpNumClients_Type())
hpNumClients.setMaxAccess(_C)
if mibBuilder.loadTexts:hpNumClients.setStatus(_B)
_HpNotificationsConfig_ObjectIdentity=ObjectIdentity
hpNotificationsConfig=_HpNotificationsConfig_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,3))
_HpFailoverNotificationEnabled_Type=TruthValue
_HpFailoverNotificationEnabled_Object=MibScalar
hpFailoverNotificationEnabled=_HpFailoverNotificationEnabled_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,3,1),_HpFailoverNotificationEnabled_Type())
hpFailoverNotificationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpFailoverNotificationEnabled.setStatus(_B)
class _HpDistributionNotificationEnabled_Type(TruthValue):defaultValue=2
_HpDistributionNotificationEnabled_Type.__name__=_G
_HpDistributionNotificationEnabled_Object=MibScalar
hpDistributionNotificationEnabled=_HpDistributionNotificationEnabled_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,3,2),_HpDistributionNotificationEnabled_Type())
hpDistributionNotificationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpDistributionNotificationEnabled.setStatus(_B)
class _HpAdminAuthFailureNotificationEnabled_Type(TruthValue):defaultValue=2
_HpAdminAuthFailureNotificationEnabled_Type.__name__=_G
_HpAdminAuthFailureNotificationEnabled_Object=MibScalar
hpAdminAuthFailureNotificationEnabled=_HpAdminAuthFailureNotificationEnabled_Object((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,2,3,3),_HpAdminAuthFailureNotificationEnabled_Type())
hpAdminAuthFailureNotificationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:hpAdminAuthFailureNotificationEnabled.setStatus(_B)
_HpSystemMIBConformance_ObjectIdentity=ObjectIdentity
hpSystemMIBConformance=_HpSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3))
_HpCompliances_ObjectIdentity=ObjectIdentity
hpCompliances=_HpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,1))
_HpGroups_ObjectIdentity=ObjectIdentity
hpGroups=_HpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2))
hpSystemGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,1))
hpSystemGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:hpSystemGroup.setStatus(_B)
hpEnvGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,2))
hpEnvGroup.setObjects(*((_A,_I),(_A,_U),(_A,_V),(_A,_F),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpEnvGroup.setStatus(_B)
hpConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,3))
hpConfigGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_J),(_A,_b),(_A,_c),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpConfigGroup.setStatus(_B)
hpStatusGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,4))
hpStatusGroup.setObjects(*((_A,_d),(_A,_e)))
if mibBuilder.loadTexts:hpStatusGroup.setStatus(_B)
hpNotificationsConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,5))
hpNotificationsConfigGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpNotificationsConfigGroup.setStatus(_B)
fanDown=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,1))
fanDown.setObjects((_A,_F))
if mibBuilder.loadTexts:fanDown.setStatus(_B)
fanUp=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,2))
fanUp.setObjects((_A,_F))
if mibBuilder.loadTexts:fanUp.setStatus(_B)
temperatureAlarm=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,3))
temperatureAlarm.setObjects((_A,_I))
if mibBuilder.loadTexts:temperatureAlarm.setStatus(_B)
hpFailover=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,4))
hpFailover.setObjects((_A,_J))
if mibBuilder.loadTexts:hpFailover.setStatus(_B)
hpDistributionEvent=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,5))
hpDistributionEvent.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:hpDistributionEvent.setStatus(_B)
hpAdminAuthFailure=NotificationType((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,0,6))
hpAdminAuthFailure.setObjects((_A,_M))
if mibBuilder.loadTexts:hpAdminAuthFailure.setStatus(_B)
hpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,2,6))
hpNotificationsGroup.setObjects(*((_A,_i),(_A,'fanUp'),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:hpNotificationsGroup.setStatus(_B)
hpSystemMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,3,7,11,17,7,1,1,3,1,1))
hpSystemMIBCompliance1.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:hpSystemMIBCompliance1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpProcurveSystem':hpProcurveSystem,'hpSystemTraps':hpSystemTraps,_i:fanDown,'fanUp':fanUp,_j:temperatureAlarm,_k:hpFailover,_l:hpDistributionEvent,_m:hpAdminAuthFailure,'hpProcurveSysMib':hpProcurveSysMib,_P:hpProductDescription,_Q:hpProductHWVersion,_R:hpProductSWVersion,_S:hpProductSerialNumber,_T:hpProductLastChange,_I:hpCpuTemperature,_U:hpPowerSupplyTemperature,_V:hpChassisTemperature,'hpFanStatusTable':hpFanStatusTable,'hpFanStatusEntry':hpFanStatusEntry,_F:hpFanNumber,_W:hpFanOperational,_X:hpFanSpeed,'hpSystemMIBObjects':hpSystemMIBObjects,'hpConfig':hpConfig,_Y:hpName,_Z:hpSystemID,_a:hpState,_K:hpDistributionType,_L:hpDistributionStatus,_J:hpIpAddress,_b:hpPeerIpAddress,_c:hpTechSupportEnabled,_M:hpFailedAdminIpAddress,'hpStatus':hpStatus,_d:hpNumAccessControllers,_e:hpNumClients,'hpNotificationsConfig':hpNotificationsConfig,_f:hpFailoverNotificationEnabled,_g:hpDistributionNotificationEnabled,_h:hpAdminAuthFailureNotificationEnabled,'hpSystemMIBConformance':hpSystemMIBConformance,'hpCompliances':hpCompliances,'hpSystemMIBCompliance1':hpSystemMIBCompliance1,'hpGroups':hpGroups,_n:hpSystemGroup,_p:hpEnvGroup,_o:hpConfigGroup,_q:hpStatusGroup,_r:hpNotificationsConfigGroup,_s:hpNotificationsGroup})