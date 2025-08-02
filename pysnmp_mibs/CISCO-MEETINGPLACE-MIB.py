_m='cmpInfoGroup'
_l='cmpNotifsGroup'
_k='cmpAlarmGroup'
_j='cmpMinSwAlarm'
_i='cmpMajSwAlarm'
_h='cmpMinHwAlarm'
_g='cmpMajHwAlarm'
_f='cmpGWSimAlarm'
_e='cmpT1Down'
_d='cmpSiteInfo'
_c='cmpRegionInfo'
_b='cmpNodeRole'
_a='cmpNodeDeployType'
_Z='cmpMaxVideoPortsUsage24Hours'
_Y='cmpMeetingCurrent'
_X='cmpMaxAudioPortsAvailable'
_W='cmpAudioPortsUsage'
_V='cmpMaxVideoPortsAvailable'
_U='cmpVideoPortsUsage'
_T='cmpMaxVideoLicense'
_S='cmpVideoLicense'
_R='cmpMaxAudioLicense'
_Q='cmpAudioLicense'
_P='cmpMaxAudioPortsUsage24Hours'
_O='cmpPeakHour'
_N='cmpPeakMeeting'
_M='cmpNotificationStatus'
_L='Integer32'
_K='cmpAlarmDesc'
_J='cmpHwPort'
_I='cmpHwSlot'
_H='cmpHwUnit'
_G='cmpHwDev'
_F='cmpSysUnit'
_E='cmpExceptionCode'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='CISCO-MEETINGPLACE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoMeetingPlaceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,733))
if mibBuilder.loadTexts:ciscoMeetingPlaceMIB.setRevisions(('2010-05-06 00:00',))
_CiscoMeetingPlaceMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoMeetingPlaceMIBNotifs=_CiscoMeetingPlaceMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,733,0))
_CiscoMeetingPlaceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMeetingPlaceMIBObjects=_CiscoMeetingPlaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,733,1))
_CmpAlarmObjects_ObjectIdentity=ObjectIdentity
cmpAlarmObjects=_CmpAlarmObjects_ObjectIdentity((1,3,6,1,4,1,9,9,733,1,1))
_CmpExceptionCode_Type=Unsigned32
_CmpExceptionCode_Object=MibScalar
cmpExceptionCode=_CmpExceptionCode_Object((1,3,6,1,4,1,9,9,733,1,1,1),_CmpExceptionCode_Type())
cmpExceptionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpExceptionCode.setStatus(_B)
_CmpSysUnit_Type=Unsigned32
_CmpSysUnit_Object=MibScalar
cmpSysUnit=_CmpSysUnit_Object((1,3,6,1,4,1,9,9,733,1,1,2),_CmpSysUnit_Type())
cmpSysUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpSysUnit.setStatus(_B)
class _CmpHwDev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('mpTemperature',1),('mpPowerSupply',2),('mpSerialPort',3),('mpTapeDrive',4),('mpHardDrive',5),('mpDisketteDrive',6),('mpEthernet',7),('mpModem',8),('mpSystemMisc',9),('mpDSPMSC',10),('mpDSPPRC',11),('mpT1Blade',12),('mpAnalogBlade',13),('mpT1Network',14),('mpSystemIntegrityCard',15),('mpMainMemory',16),('mpE1Blade',17),('mpE1Network',18),('mpVoIPBlade',19)))
_CmpHwDev_Type.__name__=_L
_CmpHwDev_Object=MibScalar
cmpHwDev=_CmpHwDev_Object((1,3,6,1,4,1,9,9,733,1,1,3),_CmpHwDev_Type())
cmpHwDev.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpHwDev.setStatus(_B)
_CmpHwUnit_Type=Unsigned32
_CmpHwUnit_Object=MibScalar
cmpHwUnit=_CmpHwUnit_Object((1,3,6,1,4,1,9,9,733,1,1,4),_CmpHwUnit_Type())
cmpHwUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpHwUnit.setStatus(_B)
_CmpHwSlot_Type=Unsigned32
_CmpHwSlot_Object=MibScalar
cmpHwSlot=_CmpHwSlot_Object((1,3,6,1,4,1,9,9,733,1,1,5),_CmpHwSlot_Type())
cmpHwSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpHwSlot.setStatus(_B)
_CmpHwPort_Type=Unsigned32
_CmpHwPort_Object=MibScalar
cmpHwPort=_CmpHwPort_Object((1,3,6,1,4,1,9,9,733,1,1,6),_CmpHwPort_Type())
cmpHwPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpHwPort.setStatus(_B)
_CmpAlarmDesc_Type=SnmpAdminString
_CmpAlarmDesc_Object=MibScalar
cmpAlarmDesc=_CmpAlarmDesc_Object((1,3,6,1,4,1,9,9,733,1,1,7),_CmpAlarmDesc_Type())
cmpAlarmDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:cmpAlarmDesc.setStatus(_B)
_CmpConferenceInfo_ObjectIdentity=ObjectIdentity
cmpConferenceInfo=_CmpConferenceInfo_ObjectIdentity((1,3,6,1,4,1,9,9,733,1,2))
_CmpPeakMeeting_Type=Unsigned32
_CmpPeakMeeting_Object=MibScalar
cmpPeakMeeting=_CmpPeakMeeting_Object((1,3,6,1,4,1,9,9,733,1,2,1),_CmpPeakMeeting_Type())
cmpPeakMeeting.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpPeakMeeting.setStatus(_B)
_CmpPeakHour_Type=Unsigned32
_CmpPeakHour_Object=MibScalar
cmpPeakHour=_CmpPeakHour_Object((1,3,6,1,4,1,9,9,733,1,2,2),_CmpPeakHour_Type())
cmpPeakHour.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpPeakHour.setStatus(_B)
_CmpMeetingCurrent_Type=Unsigned32
_CmpMeetingCurrent_Object=MibScalar
cmpMeetingCurrent=_CmpMeetingCurrent_Object((1,3,6,1,4,1,9,9,733,1,2,3),_CmpMeetingCurrent_Type())
cmpMeetingCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMeetingCurrent.setStatus(_B)
_CmpLicenseInfo_ObjectIdentity=ObjectIdentity
cmpLicenseInfo=_CmpLicenseInfo_ObjectIdentity((1,3,6,1,4,1,9,9,733,1,3))
_CmpAudioLicense_Type=Unsigned32
_CmpAudioLicense_Object=MibScalar
cmpAudioLicense=_CmpAudioLicense_Object((1,3,6,1,4,1,9,9,733,1,3,1),_CmpAudioLicense_Type())
cmpAudioLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpAudioLicense.setStatus(_B)
_CmpMaxAudioLicense_Type=Unsigned32
_CmpMaxAudioLicense_Object=MibScalar
cmpMaxAudioLicense=_CmpMaxAudioLicense_Object((1,3,6,1,4,1,9,9,733,1,3,2),_CmpMaxAudioLicense_Type())
cmpMaxAudioLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxAudioLicense.setStatus(_B)
_CmpVideoLicense_Type=Unsigned32
_CmpVideoLicense_Object=MibScalar
cmpVideoLicense=_CmpVideoLicense_Object((1,3,6,1,4,1,9,9,733,1,3,3),_CmpVideoLicense_Type())
cmpVideoLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpVideoLicense.setStatus(_B)
_CmpMaxVideoLicense_Type=Unsigned32
_CmpMaxVideoLicense_Object=MibScalar
cmpMaxVideoLicense=_CmpMaxVideoLicense_Object((1,3,6,1,4,1,9,9,733,1,3,4),_CmpMaxVideoLicense_Type())
cmpMaxVideoLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxVideoLicense.setStatus(_B)
_CmpUsageInfo_ObjectIdentity=ObjectIdentity
cmpUsageInfo=_CmpUsageInfo_ObjectIdentity((1,3,6,1,4,1,9,9,733,1,4))
_CmpVideoPortsUsage_Type=Unsigned32
_CmpVideoPortsUsage_Object=MibScalar
cmpVideoPortsUsage=_CmpVideoPortsUsage_Object((1,3,6,1,4,1,9,9,733,1,4,1),_CmpVideoPortsUsage_Type())
cmpVideoPortsUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpVideoPortsUsage.setStatus(_B)
_CmpMaxVideoPortsAvailable_Type=Unsigned32
_CmpMaxVideoPortsAvailable_Object=MibScalar
cmpMaxVideoPortsAvailable=_CmpMaxVideoPortsAvailable_Object((1,3,6,1,4,1,9,9,733,1,4,2),_CmpMaxVideoPortsAvailable_Type())
cmpMaxVideoPortsAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxVideoPortsAvailable.setStatus(_B)
_CmpAudioPortsUsage_Type=Unsigned32
_CmpAudioPortsUsage_Object=MibScalar
cmpAudioPortsUsage=_CmpAudioPortsUsage_Object((1,3,6,1,4,1,9,9,733,1,4,3),_CmpAudioPortsUsage_Type())
cmpAudioPortsUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpAudioPortsUsage.setStatus(_B)
_CmpMaxAudioPortsAvailable_Type=Unsigned32
_CmpMaxAudioPortsAvailable_Object=MibScalar
cmpMaxAudioPortsAvailable=_CmpMaxAudioPortsAvailable_Object((1,3,6,1,4,1,9,9,733,1,4,4),_CmpMaxAudioPortsAvailable_Type())
cmpMaxAudioPortsAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxAudioPortsAvailable.setStatus(_B)
_CmpMaxAudioPortsUsage24Hours_Type=Unsigned32
_CmpMaxAudioPortsUsage24Hours_Object=MibScalar
cmpMaxAudioPortsUsage24Hours=_CmpMaxAudioPortsUsage24Hours_Object((1,3,6,1,4,1,9,9,733,1,4,5),_CmpMaxAudioPortsUsage24Hours_Type())
cmpMaxAudioPortsUsage24Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxAudioPortsUsage24Hours.setStatus(_B)
_CmpMaxVideoPortsUsage24Hours_Type=Unsigned32
_CmpMaxVideoPortsUsage24Hours_Object=MibScalar
cmpMaxVideoPortsUsage24Hours=_CmpMaxVideoPortsUsage24Hours_Object((1,3,6,1,4,1,9,9,733,1,4,6),_CmpMaxVideoPortsUsage24Hours_Type())
cmpMaxVideoPortsUsage24Hours.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpMaxVideoPortsUsage24Hours.setStatus(_B)
_CmpNodeInfo_ObjectIdentity=ObjectIdentity
cmpNodeInfo=_CmpNodeInfo_ObjectIdentity((1,3,6,1,4,1,9,9,733,1,5))
_CmpNodeDeployType_Type=OctetString
_CmpNodeDeployType_Object=MibScalar
cmpNodeDeployType=_CmpNodeDeployType_Object((1,3,6,1,4,1,9,9,733,1,5,1),_CmpNodeDeployType_Type())
cmpNodeDeployType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpNodeDeployType.setStatus(_B)
_CmpNodeRole_Type=OctetString
_CmpNodeRole_Object=MibScalar
cmpNodeRole=_CmpNodeRole_Object((1,3,6,1,4,1,9,9,733,1,5,2),_CmpNodeRole_Type())
cmpNodeRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpNodeRole.setStatus(_B)
_CmpRegionInfo_Type=OctetString
_CmpRegionInfo_Object=MibScalar
cmpRegionInfo=_CmpRegionInfo_Object((1,3,6,1,4,1,9,9,733,1,5,3),_CmpRegionInfo_Type())
cmpRegionInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpRegionInfo.setStatus(_B)
_CmpSiteInfo_Type=OctetString
_CmpSiteInfo_Object=MibScalar
cmpSiteInfo=_CmpSiteInfo_Object((1,3,6,1,4,1,9,9,733,1,5,4),_CmpSiteInfo_Type())
cmpSiteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cmpSiteInfo.setStatus(_B)
_CmpNotificationStatus_Type=TruthValue
_CmpNotificationStatus_Object=MibScalar
cmpNotificationStatus=_CmpNotificationStatus_Object((1,3,6,1,4,1,9,9,733,1,6),_CmpNotificationStatus_Type())
cmpNotificationStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:cmpNotificationStatus.setStatus(_B)
_CiscoMeetingPlaceMIBConform_ObjectIdentity=ObjectIdentity
ciscoMeetingPlaceMIBConform=_CiscoMeetingPlaceMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,733,2))
_CmpMIBCompliances_ObjectIdentity=ObjectIdentity
cmpMIBCompliances=_CmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,733,2,1))
_CmpMIBGroups_ObjectIdentity=ObjectIdentity
cmpMIBGroups=_CmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,733,2,2))
cmpAlarmGroup=ObjectGroup((1,3,6,1,4,1,9,9,733,2,2,1))
cmpAlarmGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:cmpAlarmGroup.setStatus(_B)
cmpInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,733,2,2,3))
cmpInfoGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:cmpInfoGroup.setStatus(_B)
cmpT1Down=NotificationType((1,3,6,1,4,1,9,9,733,0,1))
if mibBuilder.loadTexts:cmpT1Down.setStatus(_B)
cmpGWSimAlarm=NotificationType((1,3,6,1,4,1,9,9,733,0,2))
if mibBuilder.loadTexts:cmpGWSimAlarm.setStatus(_B)
cmpMajHwAlarm=NotificationType((1,3,6,1,4,1,9,9,733,0,3))
cmpMajHwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cmpMajHwAlarm.setStatus(_B)
cmpMinHwAlarm=NotificationType((1,3,6,1,4,1,9,9,733,0,4))
cmpMinHwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cmpMinHwAlarm.setStatus(_B)
cmpMajSwAlarm=NotificationType((1,3,6,1,4,1,9,9,733,0,5))
cmpMajSwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:cmpMajSwAlarm.setStatus(_B)
cmpMinSwAlarm=NotificationType((1,3,6,1,4,1,9,9,733,0,6))
cmpMinSwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:cmpMinSwAlarm.setStatus(_B)
cmpNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,733,2,2,2))
cmpNotifsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cmpNotifsGroup.setStatus(_B)
cmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,733,2,1,1))
cmpMIBCompliance.setObjects(*((_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:cmpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoMeetingPlaceMIB':ciscoMeetingPlaceMIB,'ciscoMeetingPlaceMIBNotifs':ciscoMeetingPlaceMIBNotifs,_e:cmpT1Down,_f:cmpGWSimAlarm,_g:cmpMajHwAlarm,_h:cmpMinHwAlarm,_i:cmpMajSwAlarm,_j:cmpMinSwAlarm,'ciscoMeetingPlaceMIBObjects':ciscoMeetingPlaceMIBObjects,'cmpAlarmObjects':cmpAlarmObjects,_E:cmpExceptionCode,_F:cmpSysUnit,_G:cmpHwDev,_H:cmpHwUnit,_I:cmpHwSlot,_J:cmpHwPort,_K:cmpAlarmDesc,'cmpConferenceInfo':cmpConferenceInfo,_N:cmpPeakMeeting,_O:cmpPeakHour,_Y:cmpMeetingCurrent,'cmpLicenseInfo':cmpLicenseInfo,_Q:cmpAudioLicense,_R:cmpMaxAudioLicense,_S:cmpVideoLicense,_T:cmpMaxVideoLicense,'cmpUsageInfo':cmpUsageInfo,_U:cmpVideoPortsUsage,_V:cmpMaxVideoPortsAvailable,_W:cmpAudioPortsUsage,_X:cmpMaxAudioPortsAvailable,_P:cmpMaxAudioPortsUsage24Hours,_Z:cmpMaxVideoPortsUsage24Hours,'cmpNodeInfo':cmpNodeInfo,_a:cmpNodeDeployType,_b:cmpNodeRole,_c:cmpRegionInfo,_d:cmpSiteInfo,_M:cmpNotificationStatus,'ciscoMeetingPlaceMIBConform':ciscoMeetingPlaceMIBConform,'cmpMIBCompliances':cmpMIBCompliances,'cmpMIBCompliance':cmpMIBCompliance,'cmpMIBGroups':cmpMIBGroups,_k:cmpAlarmGroup,_l:cmpNotifsGroup,_m:cmpInfoGroup})