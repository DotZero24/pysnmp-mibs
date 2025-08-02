_AE='vmwEnvironmentGroup2'
_AD='vmwEnvCIMToSNMP'
_AC='vmwEnvAlertGroup'
_AB='vmwESXEnvNotificationGroup'
_AA='vmwEnvIpmiSelCpuCleared'
_A9='vmwEnvIpmiSelCpuRaised'
_A8='vmwEnvIpmiSelFanCleared'
_A7='vmwEnvIpmiSelFanRaised'
_A6='vmwEnvIpmiSelPowerSupplyCleared'
_A5='vmwEnvIpmiSelPowerSupplyRaised'
_A4='vmwEnvIpmiSelMemoryCleared'
_A3='vmwEnvIpmiSelMemoryRaised'
_A2='vmwEnvIpmiSelFull'
_A1='vmwESXEnvBIOSAlert'
_A0='vmwESXEnvMemoryAlert'
_z='vmwESXEnvProcessorAlert'
_y='vmwESXEnvPowerAlert'
_x='vmwESXEnvDiskAlert'
_w='vmwESXEnvThermalAlert'
_v='vmwESXEnvChassisAlert'
_u='vmwESXEnvBatteryAlert'
_t='vmwESXEnvHardwareAlert'
_s='vmwESXEnvHardwareEvent'
_r='vmwEnvHardwareEvent'
_q='vmwEnvHrDeviceIndex'
_p='vmwEnvIndex'
_o='vmwESXEnvNotificationGroup3'
_n='vmwESXEnvNotificationGroup2'
_m='vmwEnvNotificationGroup'
_l='vmwEnvironmentGroup'
_k='vmwSELCapacity'
_j='obsolete'
_i='vmwEnvIndicationSkips'
_h='vmwEnvPropertySkips'
_g='vmwEnvGetClassErrs'
_f='vmwEnvCvtOidErrs'
_e='vmwEnvCvtSyntaxErrs'
_d='vmwEnvCvtValueErrs'
_c='vmwEnvIndOidErrs'
_b='vmwEnvInErrs'
_a='vmwEnvOutNotifications'
_Z='vmwEnvLastIn'
_Y='vmwEnvInIndications'
_X='vmwEnvSource'
_W='vmwEnvLastChange'
_V='vmwEnvNumber'
_U='vmwHardwareStatus'
_T='vmwSubsystemType'
_S='Integer32'
_R='vmwEnvSelSensorNumber'
_Q='accessible-for-notify'
_P='vmwEnvProviderName'
_O='vmwEnvSystemName'
_N='vmwEnvAlertingFormat'
_M='vmwEnvAlertingElement'
_L='vmwEnvSysCreationClassName'
_K='vmwEnvAlertType'
_J='vmwEnvPerceivedSeverity'
_I='vmwEnvIndicationTime'
_H='vmwEnvEventTime'
_G='vmwEnvDescription'
_F='vmwEnvHardwareTime'
_E='vmwEventDescription'
_D='read-only'
_C='deprecated'
_B='current'
_A='VMWARE-ENV-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_S,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
vmwESX,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwESX')
vmwNotifications,vmwProductSpecific=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwNotifications','vmwProductSpecific')
VmwCIMAlertFormat,VmwCIMAlertTypes,VmwCIMSeverity,VmwCimName,VmwLongSnmpAdminString,VmwSubsystemStatus,VmwSubsystemTypes=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwCIMAlertFormat','VmwCIMAlertTypes','VmwCIMSeverity','VmwCimName','VmwLongSnmpAdminString','VmwSubsystemStatus','VmwSubsystemTypes')
vmwEnvironmentalMIB=ModuleIdentity((1,3,6,1,4,1,6876,4,20,10))
if mibBuilder.loadTexts:vmwEnvironmentalMIB.setRevisions(('2017-06-05 00:00','2010-05-12 00:00','2008-10-30 00:00','2007-12-27 00:00'))
_VmwESXNotifications_ObjectIdentity=ObjectIdentity
vmwESXNotifications=_VmwESXNotifications_ObjectIdentity((1,3,6,1,4,1,6876,4,1,0))
if mibBuilder.loadTexts:vmwESXNotifications.setStatus(_B)
_VmwEnv_ObjectIdentity=ObjectIdentity
vmwEnv=_VmwEnv_ObjectIdentity((1,3,6,1,4,1,6876,4,20))
_VmwEnvNumber_Type=Integer32
_VmwEnvNumber_Object=MibScalar
vmwEnvNumber=_VmwEnvNumber_Object((1,3,6,1,4,1,6876,4,20,1),_VmwEnvNumber_Type())
vmwEnvNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvNumber.setStatus(_B)
_VmwEnvLastChange_Type=TimeTicks
_VmwEnvLastChange_Object=MibScalar
vmwEnvLastChange=_VmwEnvLastChange_Object((1,3,6,1,4,1,6876,4,20,2),_VmwEnvLastChange_Type())
vmwEnvLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvLastChange.setStatus(_B)
_VmwEnvTable_Object=MibTable
vmwEnvTable=_VmwEnvTable_Object((1,3,6,1,4,1,6876,4,20,3))
if mibBuilder.loadTexts:vmwEnvTable.setStatus(_B)
_VmwEnvEntry_Object=MibTableRow
vmwEnvEntry=_VmwEnvEntry_Object((1,3,6,1,4,1,6876,4,20,3,1))
vmwEnvEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:vmwEnvEntry.setStatus(_B)
class _VmwEnvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VmwEnvIndex_Type.__name__=_S
_VmwEnvIndex_Object=MibTableColumn
vmwEnvIndex=_VmwEnvIndex_Object((1,3,6,1,4,1,6876,4,20,3,1,1),_VmwEnvIndex_Type())
vmwEnvIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vmwEnvIndex.setStatus(_B)
_VmwSubsystemType_Type=VmwSubsystemTypes
_VmwSubsystemType_Object=MibTableColumn
vmwSubsystemType=_VmwSubsystemType_Object((1,3,6,1,4,1,6876,4,20,3,1,2),_VmwSubsystemType_Type())
vmwSubsystemType.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwSubsystemType.setStatus(_B)
_VmwHardwareStatus_Type=VmwSubsystemStatus
_VmwHardwareStatus_Object=MibTableColumn
vmwHardwareStatus=_VmwHardwareStatus_Object((1,3,6,1,4,1,6876,4,20,3,1,3),_VmwHardwareStatus_Type())
vmwHardwareStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwHardwareStatus.setStatus(_B)
_VmwEventDescription_Type=DisplayString
_VmwEventDescription_Object=MibTableColumn
vmwEventDescription=_VmwEventDescription_Object((1,3,6,1,4,1,6876,4,20,3,1,4),_VmwEventDescription_Type())
vmwEventDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEventDescription.setStatus(_B)
_VmwEnvHardwareTime_Type=DateAndTime
_VmwEnvHardwareTime_Object=MibTableColumn
vmwEnvHardwareTime=_VmwEnvHardwareTime_Object((1,3,6,1,4,1,6876,4,20,3,1,5),_VmwEnvHardwareTime_Type())
vmwEnvHardwareTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvHardwareTime.setStatus(_B)
class _VmwEnvHrDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_VmwEnvHrDeviceIndex_Type.__name__=_S
_VmwEnvHrDeviceIndex_Object=MibTableColumn
vmwEnvHrDeviceIndex=_VmwEnvHrDeviceIndex_Object((1,3,6,1,4,1,6876,4,20,3,1,6),_VmwEnvHrDeviceIndex_Type())
vmwEnvHrDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvHrDeviceIndex.setStatus(_B)
class _VmwEnvSelSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VmwEnvSelSensorNumber_Type.__name__=_S
_VmwEnvSelSensorNumber_Object=MibTableColumn
vmwEnvSelSensorNumber=_VmwEnvSelSensorNumber_Object((1,3,6,1,4,1,6876,4,20,3,1,7),_VmwEnvSelSensorNumber_Type())
vmwEnvSelSensorNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvSelSensorNumber.setStatus(_B)
_VmwEnvironmentalMIBConformance_ObjectIdentity=ObjectIdentity
vmwEnvironmentalMIBConformance=_VmwEnvironmentalMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,4,20,10,2))
_VmwEnvironmentMIBCompliances_ObjectIdentity=ObjectIdentity
vmwEnvironmentMIBCompliances=_VmwEnvironmentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,4,20,10,2,1))
_VmwEnvMIBGroups_ObjectIdentity=ObjectIdentity
vmwEnvMIBGroups=_VmwEnvMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,4,20,10,2,2))
class _VmwSELCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VmwSELCapacity_Type.__name__=_S
_VmwSELCapacity_Object=MibScalar
vmwSELCapacity=_VmwSELCapacity_Object((1,3,6,1,4,1,6876,4,20,30),_VmwSELCapacity_Type())
vmwSELCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwSELCapacity.setStatus(_B)
class _VmwEnvSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('sensors',2),('indications',3),('ipmi',4)))
_VmwEnvSource_Type.__name__=_S
_VmwEnvSource_Object=MibScalar
vmwEnvSource=_VmwEnvSource_Object((1,3,6,1,4,1,6876,4,20,100),_VmwEnvSource_Type())
vmwEnvSource.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvSource.setStatus(_B)
_VmwEnvInIndications_Type=Counter32
_VmwEnvInIndications_Object=MibScalar
vmwEnvInIndications=_VmwEnvInIndications_Object((1,3,6,1,4,1,6876,4,20,101),_VmwEnvInIndications_Type())
vmwEnvInIndications.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvInIndications.setStatus(_B)
_VmwEnvLastIn_Type=TimeTicks
_VmwEnvLastIn_Object=MibScalar
vmwEnvLastIn=_VmwEnvLastIn_Object((1,3,6,1,4,1,6876,4,20,102),_VmwEnvLastIn_Type())
vmwEnvLastIn.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvLastIn.setStatus(_B)
_VmwEnvOutNotifications_Type=Counter32
_VmwEnvOutNotifications_Object=MibScalar
vmwEnvOutNotifications=_VmwEnvOutNotifications_Object((1,3,6,1,4,1,6876,4,20,103),_VmwEnvOutNotifications_Type())
vmwEnvOutNotifications.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvOutNotifications.setStatus(_B)
_VmwEnvInErrs_Type=Counter32
_VmwEnvInErrs_Object=MibScalar
vmwEnvInErrs=_VmwEnvInErrs_Object((1,3,6,1,4,1,6876,4,20,104),_VmwEnvInErrs_Type())
vmwEnvInErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvInErrs.setStatus(_B)
_VmwEnvIndOidErrs_Type=Counter32
_VmwEnvIndOidErrs_Object=MibScalar
vmwEnvIndOidErrs=_VmwEnvIndOidErrs_Object((1,3,6,1,4,1,6876,4,20,105),_VmwEnvIndOidErrs_Type())
vmwEnvIndOidErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvIndOidErrs.setStatus(_B)
_VmwEnvCvtValueErrs_Type=Counter32
_VmwEnvCvtValueErrs_Object=MibScalar
vmwEnvCvtValueErrs=_VmwEnvCvtValueErrs_Object((1,3,6,1,4,1,6876,4,20,106),_VmwEnvCvtValueErrs_Type())
vmwEnvCvtValueErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvCvtValueErrs.setStatus(_B)
_VmwEnvCvtSyntaxErrs_Type=Counter32
_VmwEnvCvtSyntaxErrs_Object=MibScalar
vmwEnvCvtSyntaxErrs=_VmwEnvCvtSyntaxErrs_Object((1,3,6,1,4,1,6876,4,20,107),_VmwEnvCvtSyntaxErrs_Type())
vmwEnvCvtSyntaxErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvCvtSyntaxErrs.setStatus(_B)
_VmwEnvCvtOidErrs_Type=Counter32
_VmwEnvCvtOidErrs_Object=MibScalar
vmwEnvCvtOidErrs=_VmwEnvCvtOidErrs_Object((1,3,6,1,4,1,6876,4,20,108),_VmwEnvCvtOidErrs_Type())
vmwEnvCvtOidErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvCvtOidErrs.setStatus(_B)
_VmwEnvGetClassErrs_Type=Counter32
_VmwEnvGetClassErrs_Object=MibScalar
vmwEnvGetClassErrs=_VmwEnvGetClassErrs_Object((1,3,6,1,4,1,6876,4,20,109),_VmwEnvGetClassErrs_Type())
vmwEnvGetClassErrs.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvGetClassErrs.setStatus(_B)
_VmwEnvPropertySkips_Type=Counter32
_VmwEnvPropertySkips_Object=MibScalar
vmwEnvPropertySkips=_VmwEnvPropertySkips_Object((1,3,6,1,4,1,6876,4,20,110),_VmwEnvPropertySkips_Type())
vmwEnvPropertySkips.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvPropertySkips.setStatus(_B)
_VmwEnvIndicationSkips_Type=Counter32
_VmwEnvIndicationSkips_Object=MibScalar
vmwEnvIndicationSkips=_VmwEnvIndicationSkips_Object((1,3,6,1,4,1,6876,4,20,111),_VmwEnvIndicationSkips_Type())
vmwEnvIndicationSkips.setMaxAccess(_D)
if mibBuilder.loadTexts:vmwEnvIndicationSkips.setStatus(_B)
_VmwEnvIPMI_ObjectIdentity=ObjectIdentity
vmwEnvIPMI=_VmwEnvIPMI_ObjectIdentity((1,3,6,1,4,1,6876,4,25))
_VmwEnvCIM_ObjectIdentity=ObjectIdentity
vmwEnvCIM=_VmwEnvCIM_ObjectIdentity((1,3,6,1,4,1,6876,4,30))
_VmwEnvDescription_Type=VmwLongSnmpAdminString
_VmwEnvDescription_Object=MibScalar
vmwEnvDescription=_VmwEnvDescription_Object((1,3,6,1,4,1,6876,4,30,1),_VmwEnvDescription_Type())
vmwEnvDescription.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvDescription.setStatus(_C)
_VmwEnvEventTime_Type=DateAndTime
_VmwEnvEventTime_Object=MibScalar
vmwEnvEventTime=_VmwEnvEventTime_Object((1,3,6,1,4,1,6876,4,30,2),_VmwEnvEventTime_Type())
vmwEnvEventTime.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvEventTime.setStatus(_C)
_VmwEnvIndicationTime_Type=DateAndTime
_VmwEnvIndicationTime_Object=MibScalar
vmwEnvIndicationTime=_VmwEnvIndicationTime_Object((1,3,6,1,4,1,6876,4,30,3),_VmwEnvIndicationTime_Type())
vmwEnvIndicationTime.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvIndicationTime.setStatus(_C)
_VmwEnvPerceivedSeverity_Type=VmwCIMSeverity
_VmwEnvPerceivedSeverity_Object=MibScalar
vmwEnvPerceivedSeverity=_VmwEnvPerceivedSeverity_Object((1,3,6,1,4,1,6876,4,30,4),_VmwEnvPerceivedSeverity_Type())
vmwEnvPerceivedSeverity.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvPerceivedSeverity.setStatus(_C)
_VmwEnvAlertType_Type=VmwCIMAlertTypes
_VmwEnvAlertType_Object=MibScalar
vmwEnvAlertType=_VmwEnvAlertType_Object((1,3,6,1,4,1,6876,4,30,5),_VmwEnvAlertType_Type())
vmwEnvAlertType.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvAlertType.setStatus(_C)
_VmwEnvSysCreationClassName_Type=VmwCimName
_VmwEnvSysCreationClassName_Object=MibScalar
vmwEnvSysCreationClassName=_VmwEnvSysCreationClassName_Object((1,3,6,1,4,1,6876,4,30,6),_VmwEnvSysCreationClassName_Type())
vmwEnvSysCreationClassName.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvSysCreationClassName.setStatus(_C)
_VmwEnvAlertingElement_Type=VmwCimName
_VmwEnvAlertingElement_Object=MibScalar
vmwEnvAlertingElement=_VmwEnvAlertingElement_Object((1,3,6,1,4,1,6876,4,30,7),_VmwEnvAlertingElement_Type())
vmwEnvAlertingElement.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvAlertingElement.setStatus(_C)
_VmwEnvAlertingFormat_Type=VmwCIMAlertFormat
_VmwEnvAlertingFormat_Object=MibScalar
vmwEnvAlertingFormat=_VmwEnvAlertingFormat_Object((1,3,6,1,4,1,6876,4,30,8),_VmwEnvAlertingFormat_Type())
vmwEnvAlertingFormat.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvAlertingFormat.setStatus(_C)
_VmwEnvSystemName_Type=VmwCimName
_VmwEnvSystemName_Object=MibScalar
vmwEnvSystemName=_VmwEnvSystemName_Object((1,3,6,1,4,1,6876,4,30,9),_VmwEnvSystemName_Type())
vmwEnvSystemName.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvSystemName.setStatus(_C)
_VmwEnvProviderName_Type=VmwCimName
_VmwEnvProviderName_Object=MibScalar
vmwEnvProviderName=_VmwEnvProviderName_Object((1,3,6,1,4,1,6876,4,30,10),_VmwEnvProviderName_Type())
vmwEnvProviderName.setMaxAccess(_Q)
if mibBuilder.loadTexts:vmwEnvProviderName.setStatus(_C)
vmwEnvironmentGroup=ObjectGroup((1,3,6,1,4,1,6876,4,20,10,2,2,1))
vmwEnvironmentGroup.setObjects(*((_A,_V),(_A,_W),(_A,_T),(_A,_U),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:vmwEnvironmentGroup.setStatus(_C)
vmwEnvAlertGroup=ObjectGroup((1,3,6,1,4,1,6876,4,20,10,2,2,5))
vmwEnvAlertGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwEnvAlertGroup.setStatus(_j)
vmwEnvironmentGroup2=ObjectGroup((1,3,6,1,4,1,6876,4,20,10,2,2,6))
vmwEnvironmentGroup2.setObjects(*((_A,_V),(_A,_W),(_A,_k),(_A,_T),(_A,_U),(_A,_E),(_A,_F),(_A,_q),(_A,_R)))
if mibBuilder.loadTexts:vmwEnvironmentGroup2.setStatus(_B)
vmwEnvCIMToSNMP=ObjectGroup((1,3,6,1,4,1,6876,4,20,10,2,2,20))
vmwEnvCIMToSNMP.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:vmwEnvCIMToSNMP.setStatus(_B)
vmwEnvHardwareEvent=NotificationType((1,3,6,1,4,1,6876,0,301))
vmwEnvHardwareEvent.setObjects(*((_A,_T),(_A,_U),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:vmwEnvHardwareEvent.setStatus(_C)
vmwESXEnvHardwareEvent=NotificationType((1,3,6,1,4,1,6876,4,1,0,301))
vmwESXEnvHardwareEvent.setObjects(*((_A,_T),(_A,_U),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:vmwESXEnvHardwareEvent.setStatus(_C)
vmwESXEnvHardwareAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,302))
vmwESXEnvHardwareAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvHardwareAlert.setStatus(_C)
vmwESXEnvBatteryAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,303))
vmwESXEnvBatteryAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvBatteryAlert.setStatus(_C)
vmwESXEnvChassisAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,304))
vmwESXEnvChassisAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvChassisAlert.setStatus(_C)
vmwESXEnvThermalAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,305))
vmwESXEnvThermalAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvThermalAlert.setStatus(_C)
vmwESXEnvDiskAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,306))
vmwESXEnvDiskAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvDiskAlert.setStatus(_C)
vmwESXEnvPowerAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,307))
vmwESXEnvPowerAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvPowerAlert.setStatus(_C)
vmwESXEnvProcessorAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,308))
vmwESXEnvProcessorAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvProcessorAlert.setStatus(_C)
vmwESXEnvMemoryAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,309))
vmwESXEnvMemoryAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvMemoryAlert.setStatus(_C)
vmwESXEnvBIOSAlert=NotificationType((1,3,6,1,4,1,6876,4,1,0,310))
vmwESXEnvBIOSAlert.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwESXEnvBIOSAlert.setStatus(_C)
vmwEnvIpmiSelFull=NotificationType((1,3,6,1,4,1,6876,4,1,0,390))
vmwEnvIpmiSelFull.setObjects((_A,_k))
if mibBuilder.loadTexts:vmwEnvIpmiSelFull.setStatus(_B)
vmwEnvIpmiSelMemoryRaised=NotificationType((1,3,6,1,4,1,6876,4,1,0,400))
vmwEnvIpmiSelMemoryRaised.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelMemoryRaised.setStatus(_B)
vmwEnvIpmiSelMemoryCleared=NotificationType((1,3,6,1,4,1,6876,4,1,0,401))
vmwEnvIpmiSelMemoryCleared.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelMemoryCleared.setStatus(_B)
vmwEnvIpmiSelPowerSupplyRaised=NotificationType((1,3,6,1,4,1,6876,4,1,0,410))
vmwEnvIpmiSelPowerSupplyRaised.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelPowerSupplyRaised.setStatus(_B)
vmwEnvIpmiSelPowerSupplyCleared=NotificationType((1,3,6,1,4,1,6876,4,1,0,411))
vmwEnvIpmiSelPowerSupplyCleared.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelPowerSupplyCleared.setStatus(_B)
vmwEnvIpmiSelFanRaised=NotificationType((1,3,6,1,4,1,6876,4,1,0,420))
vmwEnvIpmiSelFanRaised.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelFanRaised.setStatus(_B)
vmwEnvIpmiSelFanCleared=NotificationType((1,3,6,1,4,1,6876,4,1,0,421))
vmwEnvIpmiSelFanCleared.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelFanCleared.setStatus(_B)
vmwEnvIpmiSelCpuRaised=NotificationType((1,3,6,1,4,1,6876,4,1,0,430))
vmwEnvIpmiSelCpuRaised.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelCpuRaised.setStatus(_B)
vmwEnvIpmiSelCpuCleared=NotificationType((1,3,6,1,4,1,6876,4,1,0,431))
vmwEnvIpmiSelCpuCleared.setObjects(*((_A,_R),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:vmwEnvIpmiSelCpuCleared.setStatus(_B)
vmwEnvNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,20,10,2,2,2))
vmwEnvNotificationGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:vmwEnvNotificationGroup.setStatus(_C)
vmwESXEnvNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,4,20,10,2,2,3))
vmwESXEnvNotificationGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:vmwESXEnvNotificationGroup.setStatus(_C)
vmwESXEnvNotificationGroup2=NotificationGroup((1,3,6,1,4,1,6876,4,20,10,2,2,4))
vmwESXEnvNotificationGroup2.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:vmwESXEnvNotificationGroup2.setStatus(_C)
vmwESXEnvNotificationGroup3=NotificationGroup((1,3,6,1,4,1,6876,4,20,10,2,2,10))
vmwESXEnvNotificationGroup3.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:vmwESXEnvNotificationGroup3.setStatus(_B)
vmwEnvMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,4,20,10,2,1,2))
vmwEnvMIBBasicCompliance.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:vmwEnvMIBBasicCompliance.setStatus(_j)
vmwEnvMIBBasicCompliance2=ModuleCompliance((1,3,6,1,4,1,6876,4,20,10,2,1,3))
vmwEnvMIBBasicCompliance2.setObjects(*((_A,_l),(_A,_AB),(_A,_m)))
if mibBuilder.loadTexts:vmwEnvMIBBasicCompliance2.setStatus(_C)
vmwEnvMIBBasicCompliance3=ModuleCompliance((1,3,6,1,4,1,6876,4,20,10,2,1,4))
vmwEnvMIBBasicCompliance3.setObjects(*((_A,_AC),(_A,_n),(_A,_n)))
if mibBuilder.loadTexts:vmwEnvMIBBasicCompliance3.setStatus(_j)
vmwEnvMIBBasicCompliance4=ModuleCompliance((1,3,6,1,4,1,6876,4,20,10,2,1,5))
vmwEnvMIBBasicCompliance4.setObjects(*((_A,_AD),(_A,_AE),(_A,_o),(_A,_o)))
if mibBuilder.loadTexts:vmwEnvMIBBasicCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_r:vmwEnvHardwareEvent,'vmwESXNotifications':vmwESXNotifications,_s:vmwESXEnvHardwareEvent,_t:vmwESXEnvHardwareAlert,_u:vmwESXEnvBatteryAlert,_v:vmwESXEnvChassisAlert,_w:vmwESXEnvThermalAlert,_x:vmwESXEnvDiskAlert,_y:vmwESXEnvPowerAlert,_z:vmwESXEnvProcessorAlert,_A0:vmwESXEnvMemoryAlert,_A1:vmwESXEnvBIOSAlert,_A2:vmwEnvIpmiSelFull,_A3:vmwEnvIpmiSelMemoryRaised,_A4:vmwEnvIpmiSelMemoryCleared,_A5:vmwEnvIpmiSelPowerSupplyRaised,_A6:vmwEnvIpmiSelPowerSupplyCleared,_A7:vmwEnvIpmiSelFanRaised,_A8:vmwEnvIpmiSelFanCleared,_A9:vmwEnvIpmiSelCpuRaised,_AA:vmwEnvIpmiSelCpuCleared,'vmwEnv':vmwEnv,_V:vmwEnvNumber,_W:vmwEnvLastChange,'vmwEnvTable':vmwEnvTable,'vmwEnvEntry':vmwEnvEntry,_p:vmwEnvIndex,_T:vmwSubsystemType,_U:vmwHardwareStatus,_E:vmwEventDescription,_F:vmwEnvHardwareTime,_q:vmwEnvHrDeviceIndex,_R:vmwEnvSelSensorNumber,'vmwEnvironmentalMIB':vmwEnvironmentalMIB,'vmwEnvironmentalMIBConformance':vmwEnvironmentalMIBConformance,'vmwEnvironmentMIBCompliances':vmwEnvironmentMIBCompliances,'vmwEnvMIBBasicCompliance':vmwEnvMIBBasicCompliance,'vmwEnvMIBBasicCompliance2':vmwEnvMIBBasicCompliance2,'vmwEnvMIBBasicCompliance3':vmwEnvMIBBasicCompliance3,'vmwEnvMIBBasicCompliance4':vmwEnvMIBBasicCompliance4,'vmwEnvMIBGroups':vmwEnvMIBGroups,_l:vmwEnvironmentGroup,_m:vmwEnvNotificationGroup,_AB:vmwESXEnvNotificationGroup,_n:vmwESXEnvNotificationGroup2,_AC:vmwEnvAlertGroup,_AE:vmwEnvironmentGroup2,_o:vmwESXEnvNotificationGroup3,_AD:vmwEnvCIMToSNMP,_k:vmwSELCapacity,_X:vmwEnvSource,_Y:vmwEnvInIndications,_Z:vmwEnvLastIn,_a:vmwEnvOutNotifications,_b:vmwEnvInErrs,_c:vmwEnvIndOidErrs,_d:vmwEnvCvtValueErrs,_e:vmwEnvCvtSyntaxErrs,_f:vmwEnvCvtOidErrs,_g:vmwEnvGetClassErrs,_h:vmwEnvPropertySkips,_i:vmwEnvIndicationSkips,'vmwEnvIPMI':vmwEnvIPMI,'vmwEnvCIM':vmwEnvCIM,_G:vmwEnvDescription,_H:vmwEnvEventTime,_I:vmwEnvIndicationTime,_J:vmwEnvPerceivedSeverity,_K:vmwEnvAlertType,_L:vmwEnvSysCreationClassName,_M:vmwEnvAlertingElement,_N:vmwEnvAlertingFormat,_O:vmwEnvSystemName,_P:vmwEnvProviderName})