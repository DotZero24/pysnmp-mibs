_T='ciscoLatitudeNotifsGroupRev1'
_S='ciscoLatitudeAlarmGroupRev1'
_R='mpMinSwAlarm'
_Q='mpMajSwAlarm'
_P='mpMinHwAlarm'
_O='mpMajHwAlarm'
_N='mpGWSimAlarm'
_M='mpT1Down'
_L='DisplayString'
_K='mpAlarmDesc'
_J='mpHwPort'
_I='mpHwSlot'
_H='mpHwUnit'
_G='mpHwDev'
_F='mpSysUnit'
_E='mpExCode'
_D='read-only'
_C='Integer32'
_B='current'
_A='CISCO-LATITUDE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
latitudeComm=ModuleIdentity((1,3,6,1,4,1,7185))
if mibBuilder.loadTexts:latitudeComm.setRevisions(('2004-08-16 00:00',))
_LatitudeReg_ObjectIdentity=ObjectIdentity
latitudeReg=_LatitudeReg_ObjectIdentity((1,3,6,1,4,1,7185,1))
_LatitudeModules_ObjectIdentity=ObjectIdentity
latitudeModules=_LatitudeModules_ObjectIdentity((1,3,6,1,4,1,7185,1,1))
_LatitudeGeneric_ObjectIdentity=ObjectIdentity
latitudeGeneric=_LatitudeGeneric_ObjectIdentity((1,3,6,1,4,1,7185,2))
_LatitudeProducts_ObjectIdentity=ObjectIdentity
latitudeProducts=_LatitudeProducts_ObjectIdentity((1,3,6,1,4,1,7185,3))
_Meetingplace_ObjectIdentity=ObjectIdentity
meetingplace=_Meetingplace_ObjectIdentity((1,3,6,1,4,1,7185,3,1))
_MeetingplaceConfs_ObjectIdentity=ObjectIdentity
meetingplaceConfs=_MeetingplaceConfs_ObjectIdentity((1,3,6,1,4,1,7185,3,1,1))
_CiscoLatitudeMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLatitudeMIBCompliances=_CiscoLatitudeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,7185,3,1,1,1))
_CiscoLatitudeMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLatitudeMIBGroups=_CiscoLatitudeMIBGroups_ObjectIdentity((1,3,6,1,4,1,7185,3,1,1,2))
_MeetingplaceObjs_ObjectIdentity=ObjectIdentity
meetingplaceObjs=_MeetingplaceObjs_ObjectIdentity((1,3,6,1,4,1,7185,3,1,2))
_MeetingplaceEvents_ObjectIdentity=ObjectIdentity
meetingplaceEvents=_MeetingplaceEvents_ObjectIdentity((1,3,6,1,4,1,7185,3,1,3))
_MeetingplaceEventsV2_ObjectIdentity=ObjectIdentity
meetingplaceEventsV2=_MeetingplaceEventsV2_ObjectIdentity((1,3,6,1,4,1,7185,3,1,3,0))
class _MpExCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_MpExCode_Type.__name__=_C
_MpExCode_Object=MibScalar
mpExCode=_MpExCode_Object((1,3,6,1,4,1,7185,3,1,3,1),_MpExCode_Type())
mpExCode.setMaxAccess(_D)
if mibBuilder.loadTexts:mpExCode.setStatus(_B)
class _MpSysUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_MpSysUnit_Type.__name__=_C
_MpSysUnit_Object=MibScalar
mpSysUnit=_MpSysUnit_Object((1,3,6,1,4,1,7185,3,1,3,2),_MpSysUnit_Type())
mpSysUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:mpSysUnit.setStatus(_B)
class _MpHwDev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('mpTemperature',1),('mpPowerSupply',2),('mpSerialPort',3),('mpTapeDrive',4),('mpHardDrive',5),('mpDisketteDrive',6),('mpEthernet',7),('mpModem',8),('mpSystemMisc',9),('mpDSPMSC',10),('mpDSPPRC',11),('mpT1Blade',12),('mpAnalogBlade',13),('mpT1Network',14),('mpSystemIntegrityCard',15),('mpMainMemory',16),('mpE1Blade',17),('mpE1Network',18),('mpVoIPBlade',19)))
_MpHwDev_Type.__name__=_C
_MpHwDev_Object=MibScalar
mpHwDev=_MpHwDev_Object((1,3,6,1,4,1,7185,3,1,3,3),_MpHwDev_Type())
mpHwDev.setMaxAccess(_D)
if mibBuilder.loadTexts:mpHwDev.setStatus(_B)
class _MpHwUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_MpHwUnit_Type.__name__=_C
_MpHwUnit_Object=MibScalar
mpHwUnit=_MpHwUnit_Object((1,3,6,1,4,1,7185,3,1,3,4),_MpHwUnit_Type())
mpHwUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:mpHwUnit.setStatus(_B)
class _MpHwSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_MpHwSlot_Type.__name__=_C
_MpHwSlot_Object=MibScalar
mpHwSlot=_MpHwSlot_Object((1,3,6,1,4,1,7185,3,1,3,5),_MpHwSlot_Type())
mpHwSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:mpHwSlot.setStatus(_B)
class _MpHwPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_MpHwPort_Type.__name__=_C
_MpHwPort_Object=MibScalar
mpHwPort=_MpHwPort_Object((1,3,6,1,4,1,7185,3,1,3,6),_MpHwPort_Type())
mpHwPort.setMaxAccess(_D)
if mibBuilder.loadTexts:mpHwPort.setStatus(_B)
class _MpAlarmDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MpAlarmDesc_Type.__name__=_L
_MpAlarmDesc_Object=MibScalar
mpAlarmDesc=_MpAlarmDesc_Object((1,3,6,1,4,1,7185,3,1,3,7),_MpAlarmDesc_Type())
mpAlarmDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:mpAlarmDesc.setStatus(_B)
ciscoLatitudeAlarmGroupRev1=ObjectGroup((1,3,6,1,4,1,7185,3,1,1,2,1))
ciscoLatitudeAlarmGroupRev1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoLatitudeAlarmGroupRev1.setStatus(_B)
mpT1Down=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,1))
if mibBuilder.loadTexts:mpT1Down.setStatus(_B)
mpGWSimAlarm=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,2))
if mibBuilder.loadTexts:mpGWSimAlarm.setStatus(_B)
mpMajHwAlarm=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,3))
mpMajHwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:mpMajHwAlarm.setStatus(_B)
mpMinHwAlarm=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,4))
mpMinHwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:mpMinHwAlarm.setStatus(_B)
mpMajSwAlarm=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,5))
mpMajSwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:mpMajSwAlarm.setStatus(_B)
mpMinSwAlarm=NotificationType((1,3,6,1,4,1,7185,3,1,3,0,6))
mpMinSwAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_K)))
if mibBuilder.loadTexts:mpMinSwAlarm.setStatus(_B)
ciscoLatitudeNotifsGroupRev1=NotificationGroup((1,3,6,1,4,1,7185,3,1,1,2,2))
ciscoLatitudeNotifsGroupRev1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoLatitudeNotifsGroupRev1.setStatus(_B)
ciscoLatitudeMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,7185,3,1,1,1,1))
ciscoLatitudeMIBComplianceRev1.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoLatitudeMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'latitudeComm':latitudeComm,'latitudeReg':latitudeReg,'latitudeModules':latitudeModules,'latitudeGeneric':latitudeGeneric,'latitudeProducts':latitudeProducts,'meetingplace':meetingplace,'meetingplaceConfs':meetingplaceConfs,'ciscoLatitudeMIBCompliances':ciscoLatitudeMIBCompliances,'ciscoLatitudeMIBComplianceRev1':ciscoLatitudeMIBComplianceRev1,'ciscoLatitudeMIBGroups':ciscoLatitudeMIBGroups,_S:ciscoLatitudeAlarmGroupRev1,_T:ciscoLatitudeNotifsGroupRev1,'meetingplaceObjs':meetingplaceObjs,'meetingplaceEvents':meetingplaceEvents,'meetingplaceEventsV2':meetingplaceEventsV2,_M:mpT1Down,_N:mpGWSimAlarm,_O:mpMajHwAlarm,_P:mpMinHwAlarm,_Q:mpMajSwAlarm,_R:mpMinSwAlarm,_E:mpExCode,_F:mpSysUnit,_G:mpHwDev,_H:mpHwUnit,_I:mpHwSlot,_J:mpHwPort,_K:mpAlarmDesc})