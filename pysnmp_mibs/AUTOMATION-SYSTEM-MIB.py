_A0='automationSwDownloadGroup'
_z='automationConfigIdGroup'
_y='automationOutbandGroup'
_x='automationIpGroup'
_w='automationRevisionChanged'
_v='automationOperStateChanged'
_u='automationSwDate'
_t='automationSwUser'
_s='automationConfigDate'
_r='automationConfigUser'
_q='automationConfigId'
_p='automationTimeZoneOffsetMinutes'
_o='automationTimeZoneOffsetHours'
_n='automationSystemOutbandSubnetMask'
_m='automationSystemOutbandIp'
_l='automationSystemIpGateway'
_k='automationSystemIpSubnetMask'
_j='automationSystemIpAddress'
_i='automationResetCounters'
_h='automationPowerUpCount'
_g='automationSystemRestart'
_f='automationApplicationOperState'
_e='automationRevisionDate'
_d='automationLocationTag'
_c='automationFunctionTag'
_b='automationRevisionCounter'
_a='automationSwRevision'
_Z='automationHwRevision'
_Y='automationSerialNumber'
_X='automationOrderNumber'
_W='automationManufacturerId'
_V='Unsigned32'
_U='OctetString'
_T='automationGeoLocationTimeShift'
_S='automationGeoLocation'
_R='automationStatusEvents'
_Q='automationConfigurationEvents'
_P='automationRemoteRestartGroup'
_O='automationGeoHeight'
_N='automationGeoLongitude'
_M='automationGeoLatitude'
_L='automationOperState'
_K='automationResetCounterGroup'
_J='automationStatusGroup'
_I='automationIM2Group'
_H='automationIM1Group'
_G='automationIM0Group'
_F='Integer32'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='AUTOMATION-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
automationMgmt,=mibBuilder.importSymbols('AUTOMATION-SMI','automationMgmt')
AutomationFunctionStringTC,AutomationLocationStringTC,AutomationOrderNumberTC,AutomationSerialNumberTC,AutomationTriggerTC,AutomationVersionNumberTC=mibBuilder.importSymbols('AUTOMATION-TC','AutomationFunctionStringTC','AutomationLocationStringTC','AutomationOrderNumberTC','AutomationSerialNumberTC','AutomationTriggerTC','AutomationVersionNumberTC')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
automationSystemMIB=ModuleIdentity((1,3,6,1,4,1,4329,6,3,2))
if mibBuilder.loadTexts:automationSystemMIB.setRevisions(('2013-08-27 00:00','2013-06-25 00:00','2012-07-01 00:00','2012-06-01 00:00','2009-03-10 00:00','2008-11-10 00:00','2008-04-29 00:00','2005-01-12 00:00'))
_AutomationSystemObjects_ObjectIdentity=ObjectIdentity
automationSystemObjects=_AutomationSystemObjects_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,1))
_AutomationSystemIdent_ObjectIdentity=ObjectIdentity
automationSystemIdent=_AutomationSystemIdent_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,1,1))
class _AutomationManufacturerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AutomationManufacturerId_Type.__name__=_V
_AutomationManufacturerId_Object=MibScalar
automationManufacturerId=_AutomationManufacturerId_Object((1,3,6,1,4,1,4329,6,3,2,1,1,1),_AutomationManufacturerId_Type())
automationManufacturerId.setMaxAccess(_C)
if mibBuilder.loadTexts:automationManufacturerId.setStatus(_B)
_AutomationOrderNumber_Type=AutomationOrderNumberTC
_AutomationOrderNumber_Object=MibScalar
automationOrderNumber=_AutomationOrderNumber_Object((1,3,6,1,4,1,4329,6,3,2,1,1,2),_AutomationOrderNumber_Type())
automationOrderNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:automationOrderNumber.setStatus(_B)
_AutomationSerialNumber_Type=AutomationSerialNumberTC
_AutomationSerialNumber_Object=MibScalar
automationSerialNumber=_AutomationSerialNumber_Object((1,3,6,1,4,1,4329,6,3,2,1,1,3),_AutomationSerialNumber_Type())
automationSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:automationSerialNumber.setStatus(_B)
_AutomationHwRevision_Type=AutomationVersionNumberTC
_AutomationHwRevision_Object=MibScalar
automationHwRevision=_AutomationHwRevision_Object((1,3,6,1,4,1,4329,6,3,2,1,1,4),_AutomationHwRevision_Type())
automationHwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:automationHwRevision.setStatus(_B)
_AutomationSwRevision_Type=AutomationVersionNumberTC
_AutomationSwRevision_Object=MibScalar
automationSwRevision=_AutomationSwRevision_Object((1,3,6,1,4,1,4329,6,3,2,1,1,5),_AutomationSwRevision_Type())
automationSwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:automationSwRevision.setStatus(_B)
_AutomationRevisionCounter_Type=Counter32
_AutomationRevisionCounter_Object=MibScalar
automationRevisionCounter=_AutomationRevisionCounter_Object((1,3,6,1,4,1,4329,6,3,2,1,1,6),_AutomationRevisionCounter_Type())
automationRevisionCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:automationRevisionCounter.setStatus(_B)
_AutomationRevisionDate_Type=DateAndTime
_AutomationRevisionDate_Object=MibScalar
automationRevisionDate=_AutomationRevisionDate_Object((1,3,6,1,4,1,4329,6,3,2,1,1,7),_AutomationRevisionDate_Type())
automationRevisionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:automationRevisionDate.setStatus(_B)
_AutomationFunctionTag_Type=AutomationFunctionStringTC
_AutomationFunctionTag_Object=MibScalar
automationFunctionTag=_AutomationFunctionTag_Object((1,3,6,1,4,1,4329,6,3,2,1,1,8),_AutomationFunctionTag_Type())
automationFunctionTag.setMaxAccess(_C)
if mibBuilder.loadTexts:automationFunctionTag.setStatus(_B)
_AutomationLocationTag_Type=AutomationLocationStringTC
_AutomationLocationTag_Object=MibScalar
automationLocationTag=_AutomationLocationTag_Object((1,3,6,1,4,1,4329,6,3,2,1,1,9),_AutomationLocationTag_Type())
automationLocationTag.setMaxAccess(_C)
if mibBuilder.loadTexts:automationLocationTag.setStatus(_B)
_AutomationGeoLatitude_Type=DisplayString
_AutomationGeoLatitude_Object=MibScalar
automationGeoLatitude=_AutomationGeoLatitude_Object((1,3,6,1,4,1,4329,6,3,2,1,1,10),_AutomationGeoLatitude_Type())
automationGeoLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:automationGeoLatitude.setStatus(_B)
_AutomationGeoLongitude_Type=DisplayString
_AutomationGeoLongitude_Object=MibScalar
automationGeoLongitude=_AutomationGeoLongitude_Object((1,3,6,1,4,1,4329,6,3,2,1,1,11),_AutomationGeoLongitude_Type())
automationGeoLongitude.setMaxAccess(_D)
if mibBuilder.loadTexts:automationGeoLongitude.setStatus(_B)
_AutomationGeoHeight_Type=DisplayString
_AutomationGeoHeight_Object=MibScalar
automationGeoHeight=_AutomationGeoHeight_Object((1,3,6,1,4,1,4329,6,3,2,1,1,12),_AutomationGeoHeight_Type())
automationGeoHeight.setMaxAccess(_D)
if mibBuilder.loadTexts:automationGeoHeight.setStatus(_B)
class _AutomationTimeZoneOffsetHours_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-23,23))
_AutomationTimeZoneOffsetHours_Type.__name__=_F
_AutomationTimeZoneOffsetHours_Object=MibScalar
automationTimeZoneOffsetHours=_AutomationTimeZoneOffsetHours_Object((1,3,6,1,4,1,4329,6,3,2,1,1,13),_AutomationTimeZoneOffsetHours_Type())
automationTimeZoneOffsetHours.setMaxAccess(_D)
if mibBuilder.loadTexts:automationTimeZoneOffsetHours.setStatus(_B)
class _AutomationTimeZoneOffsetMinutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-59,59))
_AutomationTimeZoneOffsetMinutes_Type.__name__=_F
_AutomationTimeZoneOffsetMinutes_Object=MibScalar
automationTimeZoneOffsetMinutes=_AutomationTimeZoneOffsetMinutes_Object((1,3,6,1,4,1,4329,6,3,2,1,1,14),_AutomationTimeZoneOffsetMinutes_Type())
automationTimeZoneOffsetMinutes.setMaxAccess(_D)
if mibBuilder.loadTexts:automationTimeZoneOffsetMinutes.setStatus(_B)
_AutomationSwUser_Type=DisplayString
_AutomationSwUser_Object=MibScalar
automationSwUser=_AutomationSwUser_Object((1,3,6,1,4,1,4329,6,3,2,1,1,15),_AutomationSwUser_Type())
automationSwUser.setMaxAccess(_C)
if mibBuilder.loadTexts:automationSwUser.setStatus(_B)
_AutomationSwDate_Type=DateAndTime
_AutomationSwDate_Object=MibScalar
automationSwDate=_AutomationSwDate_Object((1,3,6,1,4,1,4329,6,3,2,1,1,16),_AutomationSwDate_Type())
automationSwDate.setMaxAccess(_C)
if mibBuilder.loadTexts:automationSwDate.setStatus(_B)
_AutomationSystemStatus_ObjectIdentity=ObjectIdentity
automationSystemStatus=_AutomationSystemStatus_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,1,2))
class _AutomationOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('ok',0),('maintenanceRequired',1),('maintenanceDemanded',2),('fault',3)))
_AutomationOperState_Type.__name__=_F
_AutomationOperState_Object=MibScalar
automationOperState=_AutomationOperState_Object((1,3,6,1,4,1,4329,6,3,2,1,2,1),_AutomationOperState_Type())
automationOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:automationOperState.setStatus(_B)
class _AutomationApplicationOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noControl',1),('run',2),('stop',3)))
_AutomationApplicationOperState_Type.__name__=_F
_AutomationApplicationOperState_Object=MibScalar
automationApplicationOperState=_AutomationApplicationOperState_Object((1,3,6,1,4,1,4329,6,3,2,1,2,2),_AutomationApplicationOperState_Type())
automationApplicationOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:automationApplicationOperState.setStatus(_B)
_AutomationSystemGeneric_ObjectIdentity=ObjectIdentity
automationSystemGeneric=_AutomationSystemGeneric_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,1,3))
class _AutomationSystemRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('noOperation',0),('coldstart',1),('warmstart',2),('restartBasicDefaults',3),('restartCompleteDefaults',4)))
_AutomationSystemRestart_Type.__name__=_F
_AutomationSystemRestart_Object=MibScalar
automationSystemRestart=_AutomationSystemRestart_Object((1,3,6,1,4,1,4329,6,3,2,1,3,1),_AutomationSystemRestart_Type())
automationSystemRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemRestart.setStatus(_B)
_AutomationPowerUpCount_Type=Counter32
_AutomationPowerUpCount_Object=MibScalar
automationPowerUpCount=_AutomationPowerUpCount_Object((1,3,6,1,4,1,4329,6,3,2,1,3,3),_AutomationPowerUpCount_Type())
automationPowerUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:automationPowerUpCount.setStatus(_B)
_AutomationResetCounters_Type=AutomationTriggerTC
_AutomationResetCounters_Object=MibScalar
automationResetCounters=_AutomationResetCounters_Object((1,3,6,1,4,1,4329,6,3,2,1,3,4),_AutomationResetCounters_Type())
automationResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:automationResetCounters.setStatus(_B)
class _AutomationConfigId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_AutomationConfigId_Type.__name__=_U
_AutomationConfigId_Object=MibScalar
automationConfigId=_AutomationConfigId_Object((1,3,6,1,4,1,4329,6,3,2,1,3,5),_AutomationConfigId_Type())
automationConfigId.setMaxAccess(_C)
if mibBuilder.loadTexts:automationConfigId.setStatus(_B)
_AutomationConfigUser_Type=DisplayString
_AutomationConfigUser_Object=MibScalar
automationConfigUser=_AutomationConfigUser_Object((1,3,6,1,4,1,4329,6,3,2,1,3,6),_AutomationConfigUser_Type())
automationConfigUser.setMaxAccess(_C)
if mibBuilder.loadTexts:automationConfigUser.setStatus(_B)
_AutomationConfigDate_Type=DateAndTime
_AutomationConfigDate_Object=MibScalar
automationConfigDate=_AutomationConfigDate_Object((1,3,6,1,4,1,4329,6,3,2,1,3,7),_AutomationConfigDate_Type())
automationConfigDate.setMaxAccess(_C)
if mibBuilder.loadTexts:automationConfigDate.setStatus(_B)
_AutomationSystemIp_ObjectIdentity=ObjectIdentity
automationSystemIp=_AutomationSystemIp_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,1,4))
_AutomationSystemIpAddress_Type=IpAddress
_AutomationSystemIpAddress_Object=MibScalar
automationSystemIpAddress=_AutomationSystemIpAddress_Object((1,3,6,1,4,1,4329,6,3,2,1,4,1),_AutomationSystemIpAddress_Type())
automationSystemIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemIpAddress.setStatus(_E)
_AutomationSystemIpSubnetMask_Type=IpAddress
_AutomationSystemIpSubnetMask_Object=MibScalar
automationSystemIpSubnetMask=_AutomationSystemIpSubnetMask_Object((1,3,6,1,4,1,4329,6,3,2,1,4,2),_AutomationSystemIpSubnetMask_Type())
automationSystemIpSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemIpSubnetMask.setStatus(_E)
_AutomationSystemIpGateway_Type=IpAddress
_AutomationSystemIpGateway_Object=MibScalar
automationSystemIpGateway=_AutomationSystemIpGateway_Object((1,3,6,1,4,1,4329,6,3,2,1,4,3),_AutomationSystemIpGateway_Type())
automationSystemIpGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemIpGateway.setStatus(_E)
_AutomationSystemOutbandIp_Type=IpAddress
_AutomationSystemOutbandIp_Object=MibScalar
automationSystemOutbandIp=_AutomationSystemOutbandIp_Object((1,3,6,1,4,1,4329,6,3,2,1,4,4),_AutomationSystemOutbandIp_Type())
automationSystemOutbandIp.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemOutbandIp.setStatus(_E)
_AutomationSystemOutbandSubnetMask_Type=IpAddress
_AutomationSystemOutbandSubnetMask_Object=MibScalar
automationSystemOutbandSubnetMask=_AutomationSystemOutbandSubnetMask_Object((1,3,6,1,4,1,4329,6,3,2,1,4,5),_AutomationSystemOutbandSubnetMask_Type())
automationSystemOutbandSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:automationSystemOutbandSubnetMask.setStatus(_E)
_AutomationSystemNotifications_ObjectIdentity=ObjectIdentity
automationSystemNotifications=_AutomationSystemNotifications_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,2))
_AutomationSystemNotificationsV2_ObjectIdentity=ObjectIdentity
automationSystemNotificationsV2=_AutomationSystemNotificationsV2_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,2,0))
_AutomationSystemConformance_ObjectIdentity=ObjectIdentity
automationSystemConformance=_AutomationSystemConformance_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,3))
_AutomationSystemGroups_ObjectIdentity=ObjectIdentity
automationSystemGroups=_AutomationSystemGroups_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,3,1))
_AutomationSystemCompliances_ObjectIdentity=ObjectIdentity
automationSystemCompliances=_AutomationSystemCompliances_ObjectIdentity((1,3,6,1,4,1,4329,6,3,2,3,2))
automationIM0Group=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,1))
automationIM0Group.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:automationIM0Group.setStatus(_B)
automationIM1Group=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,2))
automationIM1Group.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:automationIM1Group.setStatus(_B)
automationIM2Group=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,3))
automationIM2Group.setObjects((_A,_e))
if mibBuilder.loadTexts:automationIM2Group.setStatus(_B)
automationStatusGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,4))
automationStatusGroup.setObjects(*((_A,_L),(_A,_f)))
if mibBuilder.loadTexts:automationStatusGroup.setStatus(_B)
automationRemoteRestartGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,5))
automationRemoteRestartGroup.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:automationRemoteRestartGroup.setStatus(_B)
automationResetCounterGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,6))
automationResetCounterGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:automationResetCounterGroup.setStatus(_B)
automationIpGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,7))
automationIpGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:automationIpGroup.setStatus(_E)
automationOutbandGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,8))
automationOutbandGroup.setObjects(*((_A,_m),(_A,_n)))
if mibBuilder.loadTexts:automationOutbandGroup.setStatus(_E)
automationGeoLocation=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,11))
automationGeoLocation.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:automationGeoLocation.setStatus(_B)
automationGeoLocationTimeShift=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,12))
automationGeoLocationTimeShift.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:automationGeoLocationTimeShift.setStatus(_B)
automationConfigIdGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,13))
automationConfigIdGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:automationConfigIdGroup.setStatus(_B)
automationSwDownloadGroup=ObjectGroup((1,3,6,1,4,1,4329,6,3,2,3,1,14))
automationSwDownloadGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:automationSwDownloadGroup.setStatus(_B)
automationOperStateChanged=NotificationType((1,3,6,1,4,1,4329,6,3,2,2,0,1))
automationOperStateChanged.setObjects((_A,_L))
if mibBuilder.loadTexts:automationOperStateChanged.setStatus(_B)
automationRevisionChanged=NotificationType((1,3,6,1,4,1,4329,6,3,2,2,0,2))
if mibBuilder.loadTexts:automationRevisionChanged.setStatus(_B)
automationStatusEvents=NotificationGroup((1,3,6,1,4,1,4329,6,3,2,3,1,9))
automationStatusEvents.setObjects((_A,_v))
if mibBuilder.loadTexts:automationStatusEvents.setStatus(_B)
automationConfigurationEvents=NotificationGroup((1,3,6,1,4,1,4329,6,3,2,3,1,10))
automationConfigurationEvents.setObjects((_A,_w))
if mibBuilder.loadTexts:automationConfigurationEvents.setStatus(_B)
automationSystemBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4329,6,3,2,3,2,1))
automationSystemBasicCompliance.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:automationSystemBasicCompliance.setStatus(_B)
automationSystemExtCompliance=ModuleCompliance((1,3,6,1,4,1,4329,6,3,2,3,2,2))
automationSystemExtCompliance.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_x),(_A,_y),(_A,_P),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:automationSystemExtCompliance.setStatus(_E)
automationSystemExtCompliance2=ModuleCompliance((1,3,6,1,4,1,4329,6,3,2,3,2,3))
automationSystemExtCompliance2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_P),(_A,_J),(_A,_K),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:automationSystemExtCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'automationSystemMIB':automationSystemMIB,'automationSystemObjects':automationSystemObjects,'automationSystemIdent':automationSystemIdent,_W:automationManufacturerId,_X:automationOrderNumber,_Y:automationSerialNumber,_Z:automationHwRevision,_a:automationSwRevision,_b:automationRevisionCounter,_e:automationRevisionDate,_c:automationFunctionTag,_d:automationLocationTag,_M:automationGeoLatitude,_N:automationGeoLongitude,_O:automationGeoHeight,_o:automationTimeZoneOffsetHours,_p:automationTimeZoneOffsetMinutes,_t:automationSwUser,_u:automationSwDate,'automationSystemStatus':automationSystemStatus,_L:automationOperState,_f:automationApplicationOperState,'automationSystemGeneric':automationSystemGeneric,_g:automationSystemRestart,_h:automationPowerUpCount,_i:automationResetCounters,_q:automationConfigId,_r:automationConfigUser,_s:automationConfigDate,'automationSystemIp':automationSystemIp,_j:automationSystemIpAddress,_k:automationSystemIpSubnetMask,_l:automationSystemIpGateway,_m:automationSystemOutbandIp,_n:automationSystemOutbandSubnetMask,'automationSystemNotifications':automationSystemNotifications,'automationSystemNotificationsV2':automationSystemNotificationsV2,_v:automationOperStateChanged,_w:automationRevisionChanged,'automationSystemConformance':automationSystemConformance,'automationSystemGroups':automationSystemGroups,_G:automationIM0Group,_H:automationIM1Group,_I:automationIM2Group,_J:automationStatusGroup,_P:automationRemoteRestartGroup,_K:automationResetCounterGroup,_x:automationIpGroup,_y:automationOutbandGroup,_R:automationStatusEvents,_Q:automationConfigurationEvents,_S:automationGeoLocation,_T:automationGeoLocationTimeShift,_z:automationConfigIdGroup,_A0:automationSwDownloadGroup,'automationSystemCompliances':automationSystemCompliances,'automationSystemBasicCompliance':automationSystemBasicCompliance,'automationSystemExtCompliance':automationSystemExtCompliance,'automationSystemExtCompliance2':automationSystemExtCompliance2})