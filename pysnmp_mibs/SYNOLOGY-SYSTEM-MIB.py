_R='systemGroup'
_Q='thermalStatus'
_P='memUtilization'
_O='cpuUtilization'
_N='controllerNumber'
_M='upgradeAvailable'
_L='version'
_K='serialNumber'
_J='modelName'
_I='cpuFanStatus'
_H='systemFanStatus'
_G='powerStatus'
_F='temperature'
_E='systemStatus'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synoSystem=ModuleIdentity((1,3,6,1,4,1,6574,1))
if mibBuilder.loadTexts:synoSystem.setRevisions(('2013-09-11 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
class _SystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SystemStatus_Type.__name__=_D
_SystemStatus_Object=MibScalar
systemStatus=_SystemStatus_Object((1,3,6,1,4,1,6574,1,1),_SystemStatus_Type())
systemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemStatus.setStatus(_A)
_Temperature_Type=Integer32
_Temperature_Object=MibScalar
temperature=_Temperature_Object((1,3,6,1,4,1,6574,1,2),_Temperature_Type())
temperature.setMaxAccess(_C)
if mibBuilder.loadTexts:temperature.setStatus(_A)
class _PowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_PowerStatus_Type.__name__=_D
_PowerStatus_Object=MibScalar
powerStatus=_PowerStatus_Object((1,3,6,1,4,1,6574,1,3),_PowerStatus_Type())
powerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:powerStatus.setStatus(_A)
_Fan_ObjectIdentity=ObjectIdentity
fan=_Fan_ObjectIdentity((1,3,6,1,4,1,6574,1,4))
class _SystemFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SystemFanStatus_Type.__name__=_D
_SystemFanStatus_Object=MibScalar
systemFanStatus=_SystemFanStatus_Object((1,3,6,1,4,1,6574,1,4,1),_SystemFanStatus_Type())
systemFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:systemFanStatus.setStatus(_A)
class _CpuFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CpuFanStatus_Type.__name__=_D
_CpuFanStatus_Object=MibScalar
cpuFanStatus=_CpuFanStatus_Object((1,3,6,1,4,1,6574,1,4,2),_CpuFanStatus_Type())
cpuFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuFanStatus.setStatus(_A)
_DsmInfo_ObjectIdentity=ObjectIdentity
dsmInfo=_DsmInfo_ObjectIdentity((1,3,6,1,4,1,6574,1,5))
_ModelName_Type=OctetString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,6574,1,5,1),_ModelName_Type())
modelName.setMaxAccess(_C)
if mibBuilder.loadTexts:modelName.setStatus(_A)
_SerialNumber_Type=OctetString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,6574,1,5,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_Version_Type=OctetString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,6574,1,5,3),_Version_Type())
version.setMaxAccess(_C)
if mibBuilder.loadTexts:version.setStatus(_A)
class _UpgradeAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_UpgradeAvailable_Type.__name__=_D
_UpgradeAvailable_Object=MibScalar
upgradeAvailable=_UpgradeAvailable_Object((1,3,6,1,4,1,6574,1,5,4),_UpgradeAvailable_Type())
upgradeAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:upgradeAvailable.setStatus(_A)
_ControllerNumber_Type=Integer32
_ControllerNumber_Object=MibScalar
controllerNumber=_ControllerNumber_Object((1,3,6,1,4,1,6574,1,6),_ControllerNumber_Type())
controllerNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:controllerNumber.setStatus(_A)
_Utilization_ObjectIdentity=ObjectIdentity
utilization=_Utilization_ObjectIdentity((1,3,6,1,4,1,6574,1,7))
class _CpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilization_Type.__name__=_D
_CpuUtilization_Object=MibScalar
cpuUtilization=_CpuUtilization_Object((1,3,6,1,4,1,6574,1,7,1),_CpuUtilization_Type())
cpuUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuUtilization.setStatus(_A)
class _MemUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MemUtilization_Type.__name__=_D
_MemUtilization_Object=MibScalar
memUtilization=_MemUtilization_Object((1,3,6,1,4,1,6574,1,7,2),_MemUtilization_Type())
memUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:memUtilization.setStatus(_A)
class _ThermalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ThermalStatus_Type.__name__=_D
_ThermalStatus_Object=MibScalar
thermalStatus=_ThermalStatus_Object((1,3,6,1,4,1,6574,1,8),_ThermalStatus_Type())
thermalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:thermalStatus.setStatus(_A)
_SystemConformance_ObjectIdentity=ObjectIdentity
systemConformance=_SystemConformance_ObjectIdentity((1,3,6,1,4,1,6574,1,9))
_SystemCompliances_ObjectIdentity=ObjectIdentity
systemCompliances=_SystemCompliances_ObjectIdentity((1,3,6,1,4,1,6574,1,9,1))
_SystemGroups_ObjectIdentity=ObjectIdentity
systemGroups=_SystemGroups_ObjectIdentity((1,3,6,1,4,1,6574,1,9,2))
systemGroup=ObjectGroup((1,3,6,1,4,1,6574,1,9,2,1))
systemGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:systemGroup.setStatus(_A)
systemCompliance=ModuleCompliance((1,3,6,1,4,1,6574,1,9,1,1))
systemCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:systemCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synoSystem':synoSystem,_E:systemStatus,_F:temperature,_G:powerStatus,'fan':fan,_H:systemFanStatus,_I:cpuFanStatus,'dsmInfo':dsmInfo,_J:modelName,_K:serialNumber,_L:version,_M:upgradeAvailable,_N:controllerNumber,'utilization':utilization,_O:cpuUtilization,_P:memUtilization,_Q:thermalStatus,'systemConformance':systemConformance,'systemCompliances':systemCompliances,'systemCompliance':systemCompliance,'systemGroups':systemGroups,_R:systemGroup})