_c='tptNgfwSystemNotificationGroup'
_b='tptNgfwSystemInfoGroup'
_a='tptNgfwSystemSmsNotAuthNotify'
_Z='tptNgfwSystemShutdownNotify'
_Y='tptNgfwSystemReadyNotify'
_X='tptNgfwSystemMasterKeySet'
_W='tptNgfwSystemFipsOperState'
_V='tptNgfwSystemFipsAdminState'
_U='tptNgfwSystemSmsManaged'
_T='tptNgfwSystemUpTime'
_S='tptNgfwSystemBootTime'
_R='tptNgfwSystemFailsafeVersion'
_Q='tptNgfwSystemHardwareRevision'
_P='tptNgfwSystemHardwareSerial'
_O='tptNgfwSystemModel'
_N='tptNgfwSystemDigitalVaccineVersion'
_M='tptNgfwSystemBuildRevision'
_L='tptNgfwSystemBuildType'
_K='tptNgfwSystemBuildDate'
_J='tptNgfwSystemSoftwareVersion'
_I='tptNgfwSystemSmsIpAddress'
_H='tptNgfwSystemSmsIpAddressType'
_G='tptNgfwNotifySeverity'
_F='TPT-NGFW-REG-MIB'
_E='tptNgfwSystemSerial'
_D='SnmpAdminString'
_C='read-only'
_B='current'
_A='TPT-NGFW-SYSTEM-INFO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
tpt_ngfw_compls,tpt_ngfw_eventsV2,tpt_ngfw_groups,tpt_ngfw_objs,tptNgfwNotifySeverity=mibBuilder.importSymbols(_F,'tpt-ngfw-compls','tpt-ngfw-eventsV2','tpt-ngfw-groups','tpt-ngfw-objs',_G)
tptNgfwSystemInfo=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,1))
if mibBuilder.loadTexts:tptNgfwSystemInfo.setRevisions(('2016-05-25 18:54','2013-01-03 17:39'))
class FipsState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('crypto',2),('full',3)))
class BuildType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('production',1),('development',2)))
class _TptNgfwSystemSerial_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemSerial_Type.__name__=_D
_TptNgfwSystemSerial_Object=MibScalar
tptNgfwSystemSerial=_TptNgfwSystemSerial_Object((1,3,6,1,4,1,10734,3,9,2,1,1),_TptNgfwSystemSerial_Type())
tptNgfwSystemSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemSerial.setStatus(_B)
class _TptNgfwSystemSoftwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemSoftwareVersion_Type.__name__=_D
_TptNgfwSystemSoftwareVersion_Object=MibScalar
tptNgfwSystemSoftwareVersion=_TptNgfwSystemSoftwareVersion_Object((1,3,6,1,4,1,10734,3,9,2,1,2),_TptNgfwSystemSoftwareVersion_Type())
tptNgfwSystemSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemSoftwareVersion.setStatus(_B)
_TptNgfwSystemBuildDate_Type=DateAndTime
_TptNgfwSystemBuildDate_Object=MibScalar
tptNgfwSystemBuildDate=_TptNgfwSystemBuildDate_Object((1,3,6,1,4,1,10734,3,9,2,1,3),_TptNgfwSystemBuildDate_Type())
tptNgfwSystemBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemBuildDate.setStatus(_B)
_TptNgfwSystemBuildType_Type=BuildType
_TptNgfwSystemBuildType_Object=MibScalar
tptNgfwSystemBuildType=_TptNgfwSystemBuildType_Object((1,3,6,1,4,1,10734,3,9,2,1,4),_TptNgfwSystemBuildType_Type())
tptNgfwSystemBuildType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemBuildType.setStatus(_B)
class _TptNgfwSystemBuildRevision_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemBuildRevision_Type.__name__=_D
_TptNgfwSystemBuildRevision_Object=MibScalar
tptNgfwSystemBuildRevision=_TptNgfwSystemBuildRevision_Object((1,3,6,1,4,1,10734,3,9,2,1,5),_TptNgfwSystemBuildRevision_Type())
tptNgfwSystemBuildRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemBuildRevision.setStatus(_B)
class _TptNgfwSystemDigitalVaccineVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemDigitalVaccineVersion_Type.__name__=_D
_TptNgfwSystemDigitalVaccineVersion_Object=MibScalar
tptNgfwSystemDigitalVaccineVersion=_TptNgfwSystemDigitalVaccineVersion_Object((1,3,6,1,4,1,10734,3,9,2,1,6),_TptNgfwSystemDigitalVaccineVersion_Type())
tptNgfwSystemDigitalVaccineVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemDigitalVaccineVersion.setStatus(_B)
class _TptNgfwSystemModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemModel_Type.__name__=_D
_TptNgfwSystemModel_Object=MibScalar
tptNgfwSystemModel=_TptNgfwSystemModel_Object((1,3,6,1,4,1,10734,3,9,2,1,7),_TptNgfwSystemModel_Type())
tptNgfwSystemModel.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemModel.setStatus(_B)
class _TptNgfwSystemHardwareSerial_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemHardwareSerial_Type.__name__=_D
_TptNgfwSystemHardwareSerial_Object=MibScalar
tptNgfwSystemHardwareSerial=_TptNgfwSystemHardwareSerial_Object((1,3,6,1,4,1,10734,3,9,2,1,8),_TptNgfwSystemHardwareSerial_Type())
tptNgfwSystemHardwareSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemHardwareSerial.setStatus(_B)
class _TptNgfwSystemHardwareRevision_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemHardwareRevision_Type.__name__=_D
_TptNgfwSystemHardwareRevision_Object=MibScalar
tptNgfwSystemHardwareRevision=_TptNgfwSystemHardwareRevision_Object((1,3,6,1,4,1,10734,3,9,2,1,9),_TptNgfwSystemHardwareRevision_Type())
tptNgfwSystemHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemHardwareRevision.setStatus(_B)
class _TptNgfwSystemFailsafeVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TptNgfwSystemFailsafeVersion_Type.__name__=_D
_TptNgfwSystemFailsafeVersion_Object=MibScalar
tptNgfwSystemFailsafeVersion=_TptNgfwSystemFailsafeVersion_Object((1,3,6,1,4,1,10734,3,9,2,1,10),_TptNgfwSystemFailsafeVersion_Type())
tptNgfwSystemFailsafeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemFailsafeVersion.setStatus(_B)
_TptNgfwSystemBootTime_Type=DateAndTime
_TptNgfwSystemBootTime_Object=MibScalar
tptNgfwSystemBootTime=_TptNgfwSystemBootTime_Object((1,3,6,1,4,1,10734,3,9,2,1,11),_TptNgfwSystemBootTime_Type())
tptNgfwSystemBootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemBootTime.setStatus(_B)
_TptNgfwSystemUpTime_Type=TimeTicks
_TptNgfwSystemUpTime_Object=MibScalar
tptNgfwSystemUpTime=_TptNgfwSystemUpTime_Object((1,3,6,1,4,1,10734,3,9,2,1,12),_TptNgfwSystemUpTime_Type())
tptNgfwSystemUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemUpTime.setStatus(_B)
_TptNgfwSystemSmsManaged_Type=TruthValue
_TptNgfwSystemSmsManaged_Object=MibScalar
tptNgfwSystemSmsManaged=_TptNgfwSystemSmsManaged_Object((1,3,6,1,4,1,10734,3,9,2,1,13),_TptNgfwSystemSmsManaged_Type())
tptNgfwSystemSmsManaged.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemSmsManaged.setStatus(_B)
_TptNgfwSystemSmsIpAddressType_Type=InetAddressType
_TptNgfwSystemSmsIpAddressType_Object=MibScalar
tptNgfwSystemSmsIpAddressType=_TptNgfwSystemSmsIpAddressType_Object((1,3,6,1,4,1,10734,3,9,2,1,14),_TptNgfwSystemSmsIpAddressType_Type())
tptNgfwSystemSmsIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemSmsIpAddressType.setStatus(_B)
_TptNgfwSystemSmsIpAddress_Type=InetAddress
_TptNgfwSystemSmsIpAddress_Object=MibScalar
tptNgfwSystemSmsIpAddress=_TptNgfwSystemSmsIpAddress_Object((1,3,6,1,4,1,10734,3,9,2,1,15),_TptNgfwSystemSmsIpAddress_Type())
tptNgfwSystemSmsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemSmsIpAddress.setStatus(_B)
_TptNgfwSystemFipsAdminState_Type=FipsState
_TptNgfwSystemFipsAdminState_Object=MibScalar
tptNgfwSystemFipsAdminState=_TptNgfwSystemFipsAdminState_Object((1,3,6,1,4,1,10734,3,9,2,1,16),_TptNgfwSystemFipsAdminState_Type())
tptNgfwSystemFipsAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemFipsAdminState.setStatus(_B)
_TptNgfwSystemFipsOperState_Type=FipsState
_TptNgfwSystemFipsOperState_Object=MibScalar
tptNgfwSystemFipsOperState=_TptNgfwSystemFipsOperState_Object((1,3,6,1,4,1,10734,3,9,2,1,17),_TptNgfwSystemFipsOperState_Type())
tptNgfwSystemFipsOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemFipsOperState.setStatus(_B)
_TptNgfwSystemMasterKeySet_Type=TruthValue
_TptNgfwSystemMasterKeySet_Object=MibScalar
tptNgfwSystemMasterKeySet=_TptNgfwSystemMasterKeySet_Object((1,3,6,1,4,1,10734,3,9,2,1,18),_TptNgfwSystemMasterKeySet_Type())
tptNgfwSystemMasterKeySet.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwSystemMasterKeySet.setStatus(_B)
tptNgfwSystemInfoGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,1))
tptNgfwSystemInfoGroup.setObjects(*((_A,_E),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_H),(_A,_I),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:tptNgfwSystemInfoGroup.setStatus(_B)
tptNgfwSystemReadyNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,11))
tptNgfwSystemReadyNotify.setObjects(*((_A,_E),(_F,_G)))
if mibBuilder.loadTexts:tptNgfwSystemReadyNotify.setStatus(_B)
tptNgfwSystemShutdownNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,12))
tptNgfwSystemShutdownNotify.setObjects(*((_A,_E),(_F,_G)))
if mibBuilder.loadTexts:tptNgfwSystemShutdownNotify.setStatus(_B)
tptNgfwSystemSmsNotAuthNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,13))
tptNgfwSystemSmsNotAuthNotify.setObjects(*((_A,_E),(_A,_H),(_A,_I),(_F,_G)))
if mibBuilder.loadTexts:tptNgfwSystemSmsNotAuthNotify.setStatus(_B)
tptNgfwSystemNotificationGroup=NotificationGroup((1,3,6,1,4,1,10734,3,9,1,1,9))
tptNgfwSystemNotificationGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:tptNgfwSystemNotificationGroup.setStatus(_B)
tptNgfwSystemInfoCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,1))
tptNgfwSystemInfoCompl.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:tptNgfwSystemInfoCompl.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'FipsState':FipsState,'BuildType':BuildType,_b:tptNgfwSystemInfoGroup,_c:tptNgfwSystemNotificationGroup,'tptNgfwSystemInfoCompl':tptNgfwSystemInfoCompl,'tptNgfwSystemInfo':tptNgfwSystemInfo,_E:tptNgfwSystemSerial,_J:tptNgfwSystemSoftwareVersion,_K:tptNgfwSystemBuildDate,_L:tptNgfwSystemBuildType,_M:tptNgfwSystemBuildRevision,_N:tptNgfwSystemDigitalVaccineVersion,_O:tptNgfwSystemModel,_P:tptNgfwSystemHardwareSerial,_Q:tptNgfwSystemHardwareRevision,_R:tptNgfwSystemFailsafeVersion,_S:tptNgfwSystemBootTime,_T:tptNgfwSystemUpTime,_U:tptNgfwSystemSmsManaged,_H:tptNgfwSystemSmsIpAddressType,_I:tptNgfwSystemSmsIpAddress,_V:tptNgfwSystemFipsAdminState,_W:tptNgfwSystemFipsOperState,_X:tptNgfwSystemMasterKeySet,_Y:tptNgfwSystemReadyNotify,_Z:tptNgfwSystemShutdownNotify,_a:tptNgfwSystemSmsNotAuthNotify})