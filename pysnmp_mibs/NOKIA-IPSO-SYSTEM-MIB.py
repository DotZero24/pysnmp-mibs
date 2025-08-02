_AS='systemTrapLicense'
_AR='systemTrapSnmpProcessShutdown'
_AQ='systemTrapDiskMirrorSyncSuccess'
_AP='systemTrapDiskMirrorSyncFailure'
_AO='systemTrapDiskMirrorSetDelete'
_AN='systemTrapDiskMirrorSetCreate'
_AM='systemTrapDiskFailure'
_AL='systemTrapNoDiskSpace'
_AK='systemTrapLowDiskSpace'
_AJ='systemTrapConfigurationSaveChange'
_AI='systemTrapConfigurationFileChange'
_AH='systemTrapConfigurationChange'
_AG='ipsoDiskDriveCapacity'
_AF='ipsoDiskDriveModel'
_AE='ipsoDiskSysDriveIndex'
_AD='ipsoPkgLicense'
_AC='ipsoPkgMinorVersion'
_AB='ipsoPkgMajorVersion'
_AA='ipsoPkgName'
_A9='ipsoProductModel'
_A8='ipsoOSVersion'
_A7='ipsoOSRelease'
_A6='ipsoMotherBoardModel'
_A5='ipsoMotherBoardRev'
_A4='ipsoMotherBoardSerNum'
_A3='ipsoKernMaxMem'
_A2='ipsoCPUFreq'
_A1='ipsoCPUMfr'
_A0='ipsoCPUModel'
_z='ipsoAssetChassisSerialNumber'
_y='ipsoTotalDiskMirrorSets'
_x='ipsoProcessPercentCPU'
_w='ipsoProcessMemory'
_v='ipsoProcessOwner'
_u='ipsoProcessParentID'
_t='ipsoProcessorUtilization'
_s='ipsoSIMMTotal'
_r='ipsoImageTimeOfLoad'
_q='ipsoImageSerialNumber'
_p='ipsoImageVersionNumber'
_o='ipsoConfigLogDescr'
_n='ipsoConfigLogSize'
_m='ipsoConfigFileDateAndTime'
_l='ipsoPowerSupplyOperStatus'
_k='ipsoPowerSupplyOverTemperature'
_j='ipsoFanOperStatus'
_i='ipsoCardOperStatus'
_h='ipsoChassisTemperature'
_g='ipsoChassisMBSerialNumber'
_f='ipsoChassisMBRevNumber'
_e='ipsoChassisMBType'
_d='ipsoChassisSerialNumber'
_c='notRunning'
_b='running'
_a='overTemperature'
_Z='normal'
_Y='ipsoDiskMirrorSetDestinationDriveIndex'
_X='ipsoDiskMirrorSetSourceDriveIndex'
_W='ipsoDaysToExpire'
_V='ipsoFeatureName'
_U='ipsoPkgIndex'
_T='ipsoProcessID'
_S='ipsoImageIndex'
_R='ipsoConfigLogIndex'
_Q='ipsoConfigIndex'
_P='ipsoPowerSupplyIndex'
_O='ipsoFanIndex'
_N='ipsoCardIndex'
_M='hrPartitionSize'
_L='hrPartitionLabel'
_K='hrPartitionIndex'
_J='hrFSMountPoint'
_I='ipsoConfigFilePath'
_H='ipsoDiskDriveIndex'
_G='ipsoDiskDriveLocation'
_F='ipsoDiskMirrorSetIndex'
_E='HOST-RESOURCES-MIB'
_D='Integer32'
_C='read-only'
_B='NOKIA-IPSO-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrFSMountPoint,hrPartitionIndex,hrPartitionLabel,hrPartitionSize=mibBuilder.importSymbols(_E,_J,_K,_L,_M)
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ipsoSystem=ModuleIdentity((1,3,6,1,4,1,94,1,21,1))
if mibBuilder.loadTexts:ipsoSystem.setRevisions(('1999-10-20 00:00','1900-01-11 00:00','1901-12-07 00:00'))
_Nokia_ObjectIdentity=ObjectIdentity
nokia=_Nokia_ObjectIdentity((1,3,6,1,4,1,94))
_NokiaProducts_ObjectIdentity=ObjectIdentity
nokiaProducts=_NokiaProducts_ObjectIdentity((1,3,6,1,4,1,94,1))
_IpsoProducts_ObjectIdentity=ObjectIdentity
ipsoProducts=_IpsoProducts_ObjectIdentity((1,3,6,1,4,1,94,1,21))
_IpsoChassisSerialNumber_Type=DisplayString
_IpsoChassisSerialNumber_Object=MibScalar
ipsoChassisSerialNumber=_IpsoChassisSerialNumber_Object((1,3,6,1,4,1,94,1,21,1,1,1),_IpsoChassisSerialNumber_Type())
ipsoChassisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoChassisSerialNumber.setStatus(_A)
_IpsoChassisMBType_Type=DisplayString
_IpsoChassisMBType_Object=MibScalar
ipsoChassisMBType=_IpsoChassisMBType_Object((1,3,6,1,4,1,94,1,21,1,1,2),_IpsoChassisMBType_Type())
ipsoChassisMBType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoChassisMBType.setStatus(_A)
_IpsoChassisMBRevNumber_Type=DisplayString
_IpsoChassisMBRevNumber_Object=MibScalar
ipsoChassisMBRevNumber=_IpsoChassisMBRevNumber_Object((1,3,6,1,4,1,94,1,21,1,1,3),_IpsoChassisMBRevNumber_Type())
ipsoChassisMBRevNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoChassisMBRevNumber.setStatus(_A)
_IpsoChassisMBSerialNumber_Type=DisplayString
_IpsoChassisMBSerialNumber_Object=MibScalar
ipsoChassisMBSerialNumber=_IpsoChassisMBSerialNumber_Object((1,3,6,1,4,1,94,1,21,1,1,4),_IpsoChassisMBSerialNumber_Type())
ipsoChassisMBSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoChassisMBSerialNumber.setStatus(_A)
class _IpsoChassisTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_IpsoChassisTemperature_Type.__name__=_D
_IpsoChassisTemperature_Object=MibScalar
ipsoChassisTemperature=_IpsoChassisTemperature_Object((1,3,6,1,4,1,94,1,21,1,1,5),_IpsoChassisTemperature_Type())
ipsoChassisTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoChassisTemperature.setStatus(_A)
_IpsoCardTable_Object=MibTable
ipsoCardTable=_IpsoCardTable_Object((1,3,6,1,4,1,94,1,21,1,1,6))
if mibBuilder.loadTexts:ipsoCardTable.setStatus(_A)
_IpsoCardEntry_Object=MibTableRow
ipsoCardEntry=_IpsoCardEntry_Object((1,3,6,1,4,1,94,1,21,1,1,6,1))
ipsoCardEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ipsoCardEntry.setStatus(_A)
class _IpsoCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoCardIndex_Type.__name__=_D
_IpsoCardIndex_Object=MibTableColumn
ipsoCardIndex=_IpsoCardIndex_Object((1,3,6,1,4,1,94,1,21,1,1,6,1,1),_IpsoCardIndex_Type())
ipsoCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoCardIndex.setStatus(_A)
class _IpsoCardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpsoCardOperStatus_Type.__name__=_D
_IpsoCardOperStatus_Object=MibTableColumn
ipsoCardOperStatus=_IpsoCardOperStatus_Object((1,3,6,1,4,1,94,1,21,1,1,6,1,2),_IpsoCardOperStatus_Type())
ipsoCardOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoCardOperStatus.setStatus(_A)
_IpsoFanTable_Object=MibTable
ipsoFanTable=_IpsoFanTable_Object((1,3,6,1,4,1,94,1,21,1,2,1))
if mibBuilder.loadTexts:ipsoFanTable.setStatus(_A)
_IpsoFanEntry_Object=MibTableRow
ipsoFanEntry=_IpsoFanEntry_Object((1,3,6,1,4,1,94,1,21,1,2,1,1))
ipsoFanEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ipsoFanEntry.setStatus(_A)
_IpsoFanIndex_Type=Integer32
_IpsoFanIndex_Object=MibTableColumn
ipsoFanIndex=_IpsoFanIndex_Object((1,3,6,1,4,1,94,1,21,1,2,1,1,1),_IpsoFanIndex_Type())
ipsoFanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoFanIndex.setStatus(_A)
class _IpsoFanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_IpsoFanOperStatus_Type.__name__=_D
_IpsoFanOperStatus_Object=MibTableColumn
ipsoFanOperStatus=_IpsoFanOperStatus_Object((1,3,6,1,4,1,94,1,21,1,2,1,1,2),_IpsoFanOperStatus_Type())
ipsoFanOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoFanOperStatus.setStatus(_A)
_IpsoPowerSupplyTable_Object=MibTable
ipsoPowerSupplyTable=_IpsoPowerSupplyTable_Object((1,3,6,1,4,1,94,1,21,1,3,1))
if mibBuilder.loadTexts:ipsoPowerSupplyTable.setStatus(_A)
_IpsoPowerSupplyEntry_Object=MibTableRow
ipsoPowerSupplyEntry=_IpsoPowerSupplyEntry_Object((1,3,6,1,4,1,94,1,21,1,3,1,1))
ipsoPowerSupplyEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ipsoPowerSupplyEntry.setStatus(_A)
class _IpsoPowerSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoPowerSupplyIndex_Type.__name__=_D
_IpsoPowerSupplyIndex_Object=MibTableColumn
ipsoPowerSupplyIndex=_IpsoPowerSupplyIndex_Object((1,3,6,1,4,1,94,1,21,1,3,1,1,1),_IpsoPowerSupplyIndex_Type())
ipsoPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPowerSupplyIndex.setStatus(_A)
class _IpsoPowerSupplyOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_IpsoPowerSupplyOverTemperature_Type.__name__=_D
_IpsoPowerSupplyOverTemperature_Object=MibTableColumn
ipsoPowerSupplyOverTemperature=_IpsoPowerSupplyOverTemperature_Object((1,3,6,1,4,1,94,1,21,1,3,1,1,2),_IpsoPowerSupplyOverTemperature_Type())
ipsoPowerSupplyOverTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPowerSupplyOverTemperature.setStatus(_A)
class _IpsoPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_IpsoPowerSupplyOperStatus_Type.__name__=_D
_IpsoPowerSupplyOperStatus_Object=MibTableColumn
ipsoPowerSupplyOperStatus=_IpsoPowerSupplyOperStatus_Object((1,3,6,1,4,1,94,1,21,1,3,1,1,3),_IpsoPowerSupplyOperStatus_Type())
ipsoPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPowerSupplyOperStatus.setStatus(_A)
_IpsoConfigTable_Object=MibTable
ipsoConfigTable=_IpsoConfigTable_Object((1,3,6,1,4,1,94,1,21,1,4,1))
if mibBuilder.loadTexts:ipsoConfigTable.setStatus(_A)
_IpsoConfigEntry_Object=MibTableRow
ipsoConfigEntry=_IpsoConfigEntry_Object((1,3,6,1,4,1,94,1,21,1,4,1,1))
ipsoConfigEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ipsoConfigEntry.setStatus(_A)
class _IpsoConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoConfigIndex_Type.__name__=_D
_IpsoConfigIndex_Object=MibTableColumn
ipsoConfigIndex=_IpsoConfigIndex_Object((1,3,6,1,4,1,94,1,21,1,4,1,1,1),_IpsoConfigIndex_Type())
ipsoConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoConfigIndex.setStatus(_A)
_IpsoConfigFilePath_Type=DisplayString
_IpsoConfigFilePath_Object=MibTableColumn
ipsoConfigFilePath=_IpsoConfigFilePath_Object((1,3,6,1,4,1,94,1,21,1,4,1,1,2),_IpsoConfigFilePath_Type())
ipsoConfigFilePath.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoConfigFilePath.setStatus(_A)
_IpsoConfigFileDateAndTime_Type=DateAndTime
_IpsoConfigFileDateAndTime_Object=MibTableColumn
ipsoConfigFileDateAndTime=_IpsoConfigFileDateAndTime_Object((1,3,6,1,4,1,94,1,21,1,4,1,1,3),_IpsoConfigFileDateAndTime_Type())
ipsoConfigFileDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoConfigFileDateAndTime.setStatus(_A)
class _IpsoConfigLogSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpsoConfigLogSize_Type.__name__=_D
_IpsoConfigLogSize_Object=MibScalar
ipsoConfigLogSize=_IpsoConfigLogSize_Object((1,3,6,1,4,1,94,1,21,1,4,2),_IpsoConfigLogSize_Type())
ipsoConfigLogSize.setMaxAccess('read-write')
if mibBuilder.loadTexts:ipsoConfigLogSize.setStatus(_A)
_IpsoConfigLogTable_Object=MibTable
ipsoConfigLogTable=_IpsoConfigLogTable_Object((1,3,6,1,4,1,94,1,21,1,4,3))
if mibBuilder.loadTexts:ipsoConfigLogTable.setStatus(_A)
_IpsoConfigLogEntry_Object=MibTableRow
ipsoConfigLogEntry=_IpsoConfigLogEntry_Object((1,3,6,1,4,1,94,1,21,1,4,3,1))
ipsoConfigLogEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ipsoConfigLogEntry.setStatus(_A)
class _IpsoConfigLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpsoConfigLogIndex_Type.__name__=_D
_IpsoConfigLogIndex_Object=MibTableColumn
ipsoConfigLogIndex=_IpsoConfigLogIndex_Object((1,3,6,1,4,1,94,1,21,1,4,3,1,1),_IpsoConfigLogIndex_Type())
ipsoConfigLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoConfigLogIndex.setStatus(_A)
_IpsoConfigLogDescr_Type=DisplayString
_IpsoConfigLogDescr_Object=MibTableColumn
ipsoConfigLogDescr=_IpsoConfigLogDescr_Object((1,3,6,1,4,1,94,1,21,1,4,3,1,2),_IpsoConfigLogDescr_Type())
ipsoConfigLogDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoConfigLogDescr.setStatus(_A)
_IpsoImageTable_Object=MibTable
ipsoImageTable=_IpsoImageTable_Object((1,3,6,1,4,1,94,1,21,1,5,1))
if mibBuilder.loadTexts:ipsoImageTable.setStatus(_A)
_IpsoImageEntry_Object=MibTableRow
ipsoImageEntry=_IpsoImageEntry_Object((1,3,6,1,4,1,94,1,21,1,5,1,1))
ipsoImageEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:ipsoImageEntry.setStatus(_A)
class _IpsoImageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoImageIndex_Type.__name__=_D
_IpsoImageIndex_Object=MibTableColumn
ipsoImageIndex=_IpsoImageIndex_Object((1,3,6,1,4,1,94,1,21,1,5,1,1,1),_IpsoImageIndex_Type())
ipsoImageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoImageIndex.setStatus(_A)
_IpsoImageVersionNumber_Type=DisplayString
_IpsoImageVersionNumber_Object=MibTableColumn
ipsoImageVersionNumber=_IpsoImageVersionNumber_Object((1,3,6,1,4,1,94,1,21,1,5,1,1,2),_IpsoImageVersionNumber_Type())
ipsoImageVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoImageVersionNumber.setStatus(_A)
_IpsoImageSerialNumber_Type=DisplayString
_IpsoImageSerialNumber_Object=MibTableColumn
ipsoImageSerialNumber=_IpsoImageSerialNumber_Object((1,3,6,1,4,1,94,1,21,1,5,1,1,3),_IpsoImageSerialNumber_Type())
ipsoImageSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoImageSerialNumber.setStatus(_A)
_IpsoImageTimeOfLoad_Type=DateAndTime
_IpsoImageTimeOfLoad_Object=MibTableColumn
ipsoImageTimeOfLoad=_IpsoImageTimeOfLoad_Object((1,3,6,1,4,1,94,1,21,1,5,1,1,4),_IpsoImageTimeOfLoad_Type())
ipsoImageTimeOfLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoImageTimeOfLoad.setStatus(_A)
class _IpsoSIMMTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoSIMMTotal_Type.__name__=_D
_IpsoSIMMTotal_Object=MibScalar
ipsoSIMMTotal=_IpsoSIMMTotal_Object((1,3,6,1,4,1,94,1,21,1,6,1),_IpsoSIMMTotal_Type())
ipsoSIMMTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoSIMMTotal.setStatus(_A)
_IpsoProcessorUtilization_Type=Gauge32
_IpsoProcessorUtilization_Object=MibScalar
ipsoProcessorUtilization=_IpsoProcessorUtilization_Object((1,3,6,1,4,1,94,1,21,1,7,1),_IpsoProcessorUtilization_Type())
ipsoProcessorUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessorUtilization.setStatus(_A)
_IpsoProcessTable_Object=MibTable
ipsoProcessTable=_IpsoProcessTable_Object((1,3,6,1,4,1,94,1,21,1,7,2))
if mibBuilder.loadTexts:ipsoProcessTable.setStatus(_A)
_IpsoProcessEntry_Object=MibTableRow
ipsoProcessEntry=_IpsoProcessEntry_Object((1,3,6,1,4,1,94,1,21,1,7,2,1))
ipsoProcessEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:ipsoProcessEntry.setStatus(_A)
class _IpsoProcessID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoProcessID_Type.__name__=_D
_IpsoProcessID_Object=MibTableColumn
ipsoProcessID=_IpsoProcessID_Object((1,3,6,1,4,1,94,1,21,1,7,2,1,1),_IpsoProcessID_Type())
ipsoProcessID.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessID.setStatus(_A)
class _IpsoProcessParentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoProcessParentID_Type.__name__=_D
_IpsoProcessParentID_Object=MibTableColumn
ipsoProcessParentID=_IpsoProcessParentID_Object((1,3,6,1,4,1,94,1,21,1,7,2,1,2),_IpsoProcessParentID_Type())
ipsoProcessParentID.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessParentID.setStatus(_A)
_IpsoProcessOwner_Type=DisplayString
_IpsoProcessOwner_Object=MibTableColumn
ipsoProcessOwner=_IpsoProcessOwner_Object((1,3,6,1,4,1,94,1,21,1,7,2,1,3),_IpsoProcessOwner_Type())
ipsoProcessOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessOwner.setStatus(_A)
class _IpsoProcessMemory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoProcessMemory_Type.__name__=_D
_IpsoProcessMemory_Object=MibTableColumn
ipsoProcessMemory=_IpsoProcessMemory_Object((1,3,6,1,4,1,94,1,21,1,7,2,1,4),_IpsoProcessMemory_Type())
ipsoProcessMemory.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessMemory.setStatus(_A)
class _IpsoProcessPercentCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_IpsoProcessPercentCPU_Type.__name__=_D
_IpsoProcessPercentCPU_Object=MibTableColumn
ipsoProcessPercentCPU=_IpsoProcessPercentCPU_Object((1,3,6,1,4,1,94,1,21,1,7,2,1,5),_IpsoProcessPercentCPU_Type())
ipsoProcessPercentCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProcessPercentCPU.setStatus(_A)
_SystemTraps_ObjectIdentity=ObjectIdentity
systemTraps=_SystemTraps_ObjectIdentity((1,3,6,1,4,1,94,1,21,1,8,1))
class _IpsoTotalDiskMirrorSets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoTotalDiskMirrorSets_Type.__name__=_D
_IpsoTotalDiskMirrorSets_Object=MibScalar
ipsoTotalDiskMirrorSets=_IpsoTotalDiskMirrorSets_Object((1,3,6,1,4,1,94,1,21,1,9,1),_IpsoTotalDiskMirrorSets_Type())
ipsoTotalDiskMirrorSets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoTotalDiskMirrorSets.setStatus(_A)
_IpsoDiskMirrorSetTable_Object=MibTable
ipsoDiskMirrorSetTable=_IpsoDiskMirrorSetTable_Object((1,3,6,1,4,1,94,1,21,1,9,2))
if mibBuilder.loadTexts:ipsoDiskMirrorSetTable.setStatus(_A)
_IpsoDiskMirrorSetEntry_Object=MibTableRow
ipsoDiskMirrorSetEntry=_IpsoDiskMirrorSetEntry_Object((1,3,6,1,4,1,94,1,21,1,9,2,1))
ipsoDiskMirrorSetEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ipsoDiskMirrorSetEntry.setStatus(_A)
class _IpsoDiskMirrorSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoDiskMirrorSetIndex_Type.__name__=_D
_IpsoDiskMirrorSetIndex_Object=MibTableColumn
ipsoDiskMirrorSetIndex=_IpsoDiskMirrorSetIndex_Object((1,3,6,1,4,1,94,1,21,1,9,2,1,1),_IpsoDiskMirrorSetIndex_Type())
ipsoDiskMirrorSetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskMirrorSetIndex.setStatus(_A)
_IpsoDiskMirrorSetSourceDriveIndex_Type=Integer32
_IpsoDiskMirrorSetSourceDriveIndex_Object=MibTableColumn
ipsoDiskMirrorSetSourceDriveIndex=_IpsoDiskMirrorSetSourceDriveIndex_Object((1,3,6,1,4,1,94,1,21,1,9,2,1,2),_IpsoDiskMirrorSetSourceDriveIndex_Type())
ipsoDiskMirrorSetSourceDriveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskMirrorSetSourceDriveIndex.setStatus(_A)
_IpsoDiskMirrorSetDestinationDriveIndex_Type=Integer32
_IpsoDiskMirrorSetDestinationDriveIndex_Object=MibTableColumn
ipsoDiskMirrorSetDestinationDriveIndex=_IpsoDiskMirrorSetDestinationDriveIndex_Object((1,3,6,1,4,1,94,1,21,1,9,2,1,3),_IpsoDiskMirrorSetDestinationDriveIndex_Type())
ipsoDiskMirrorSetDestinationDriveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskMirrorSetDestinationDriveIndex.setStatus(_A)
_IpsoDiskMirrorSetSyncPercent_Type=DisplayString
_IpsoDiskMirrorSetSyncPercent_Object=MibTableColumn
ipsoDiskMirrorSetSyncPercent=_IpsoDiskMirrorSetSyncPercent_Object((1,3,6,1,4,1,94,1,21,1,9,2,1,4),_IpsoDiskMirrorSetSyncPercent_Type())
ipsoDiskMirrorSetSyncPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskMirrorSetSyncPercent.setStatus(_A)
_IpsoAssetChassisSerialNumber_Type=DisplayString
_IpsoAssetChassisSerialNumber_Object=MibScalar
ipsoAssetChassisSerialNumber=_IpsoAssetChassisSerialNumber_Object((1,3,6,1,4,1,94,1,21,1,10,1),_IpsoAssetChassisSerialNumber_Type())
ipsoAssetChassisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoAssetChassisSerialNumber.setStatus(_A)
_IpsoCPUModel_Type=DisplayString
_IpsoCPUModel_Object=MibScalar
ipsoCPUModel=_IpsoCPUModel_Object((1,3,6,1,4,1,94,1,21,1,10,2),_IpsoCPUModel_Type())
ipsoCPUModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoCPUModel.setStatus(_A)
_IpsoCPUMfr_Type=DisplayString
_IpsoCPUMfr_Object=MibScalar
ipsoCPUMfr=_IpsoCPUMfr_Object((1,3,6,1,4,1,94,1,21,1,10,3),_IpsoCPUMfr_Type())
ipsoCPUMfr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoCPUMfr.setStatus(_A)
_IpsoCPUFreq_Type=Integer32
_IpsoCPUFreq_Object=MibScalar
ipsoCPUFreq=_IpsoCPUFreq_Object((1,3,6,1,4,1,94,1,21,1,10,4),_IpsoCPUFreq_Type())
ipsoCPUFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoCPUFreq.setStatus(_A)
_IpsoKernMaxMem_Type=Integer32
_IpsoKernMaxMem_Object=MibScalar
ipsoKernMaxMem=_IpsoKernMaxMem_Object((1,3,6,1,4,1,94,1,21,1,10,5),_IpsoKernMaxMem_Type())
ipsoKernMaxMem.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoKernMaxMem.setStatus(_A)
_IpsoMotherBoardSerNum_Type=DisplayString
_IpsoMotherBoardSerNum_Object=MibScalar
ipsoMotherBoardSerNum=_IpsoMotherBoardSerNum_Object((1,3,6,1,4,1,94,1,21,1,10,6),_IpsoMotherBoardSerNum_Type())
ipsoMotherBoardSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoMotherBoardSerNum.setStatus(_A)
_IpsoMotherBoardRev_Type=DisplayString
_IpsoMotherBoardRev_Object=MibScalar
ipsoMotherBoardRev=_IpsoMotherBoardRev_Object((1,3,6,1,4,1,94,1,21,1,10,7),_IpsoMotherBoardRev_Type())
ipsoMotherBoardRev.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoMotherBoardRev.setStatus(_A)
_IpsoMotherBoardModel_Type=DisplayString
_IpsoMotherBoardModel_Object=MibScalar
ipsoMotherBoardModel=_IpsoMotherBoardModel_Object((1,3,6,1,4,1,94,1,21,1,10,8),_IpsoMotherBoardModel_Type())
ipsoMotherBoardModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoMotherBoardModel.setStatus(_A)
_IpsoOSRelease_Type=DisplayString
_IpsoOSRelease_Object=MibScalar
ipsoOSRelease=_IpsoOSRelease_Object((1,3,6,1,4,1,94,1,21,1,10,9),_IpsoOSRelease_Type())
ipsoOSRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoOSRelease.setStatus(_A)
_IpsoOSVersion_Type=DisplayString
_IpsoOSVersion_Object=MibScalar
ipsoOSVersion=_IpsoOSVersion_Object((1,3,6,1,4,1,94,1,21,1,10,10),_IpsoOSVersion_Type())
ipsoOSVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoOSVersion.setStatus(_A)
_IpsoProductModel_Type=DisplayString
_IpsoProductModel_Object=MibScalar
ipsoProductModel=_IpsoProductModel_Object((1,3,6,1,4,1,94,1,21,1,10,11),_IpsoProductModel_Type())
ipsoProductModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoProductModel.setStatus(_A)
_IpsoAssetTable_Object=MibTable
ipsoAssetTable=_IpsoAssetTable_Object((1,3,6,1,4,1,94,1,21,1,10,12))
if mibBuilder.loadTexts:ipsoAssetTable.setStatus(_A)
_IpsoAssetEntry_Object=MibTableRow
ipsoAssetEntry=_IpsoAssetEntry_Object((1,3,6,1,4,1,94,1,21,1,10,12,1))
ipsoAssetEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:ipsoAssetEntry.setStatus(_A)
_IpsoPkgIndex_Type=Integer32
_IpsoPkgIndex_Object=MibTableColumn
ipsoPkgIndex=_IpsoPkgIndex_Object((1,3,6,1,4,1,94,1,21,1,10,12,1,1),_IpsoPkgIndex_Type())
ipsoPkgIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPkgIndex.setStatus(_A)
_IpsoPkgName_Type=DisplayString
_IpsoPkgName_Object=MibTableColumn
ipsoPkgName=_IpsoPkgName_Object((1,3,6,1,4,1,94,1,21,1,10,12,1,2),_IpsoPkgName_Type())
ipsoPkgName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPkgName.setStatus(_A)
_IpsoPkgMajorVersion_Type=DisplayString
_IpsoPkgMajorVersion_Object=MibTableColumn
ipsoPkgMajorVersion=_IpsoPkgMajorVersion_Object((1,3,6,1,4,1,94,1,21,1,10,12,1,3),_IpsoPkgMajorVersion_Type())
ipsoPkgMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPkgMajorVersion.setStatus(_A)
_IpsoPkgMinorVersion_Type=DisplayString
_IpsoPkgMinorVersion_Object=MibTableColumn
ipsoPkgMinorVersion=_IpsoPkgMinorVersion_Object((1,3,6,1,4,1,94,1,21,1,10,12,1,4),_IpsoPkgMinorVersion_Type())
ipsoPkgMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPkgMinorVersion.setStatus(_A)
_IpsoPkgLicense_Type=DisplayString
_IpsoPkgLicense_Object=MibTableColumn
ipsoPkgLicense=_IpsoPkgLicense_Object((1,3,6,1,4,1,94,1,21,1,10,12,1,5),_IpsoPkgLicense_Type())
ipsoPkgLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoPkgLicense.setStatus(_A)
_IpsoDiskDriveTable_Object=MibTable
ipsoDiskDriveTable=_IpsoDiskDriveTable_Object((1,3,6,1,4,1,94,1,21,1,10,13))
if mibBuilder.loadTexts:ipsoDiskDriveTable.setStatus(_A)
_IpsoDiskDriveEntry_Object=MibTableRow
ipsoDiskDriveEntry=_IpsoDiskDriveEntry_Object((1,3,6,1,4,1,94,1,21,1,10,13,1))
ipsoDiskDriveEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ipsoDiskDriveEntry.setStatus(_A)
class _IpsoDiskDriveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoDiskDriveIndex_Type.__name__=_D
_IpsoDiskDriveIndex_Object=MibTableColumn
ipsoDiskDriveIndex=_IpsoDiskDriveIndex_Object((1,3,6,1,4,1,94,1,21,1,10,13,1,1),_IpsoDiskDriveIndex_Type())
ipsoDiskDriveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskDriveIndex.setStatus(_A)
class _IpsoDiskSysDriveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_IpsoDiskSysDriveIndex_Type.__name__=_D
_IpsoDiskSysDriveIndex_Object=MibTableColumn
ipsoDiskSysDriveIndex=_IpsoDiskSysDriveIndex_Object((1,3,6,1,4,1,94,1,21,1,10,13,1,2),_IpsoDiskSysDriveIndex_Type())
ipsoDiskSysDriveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskSysDriveIndex.setStatus(_A)
_IpsoDiskDriveModel_Type=DisplayString
_IpsoDiskDriveModel_Object=MibTableColumn
ipsoDiskDriveModel=_IpsoDiskDriveModel_Object((1,3,6,1,4,1,94,1,21,1,10,13,1,3),_IpsoDiskDriveModel_Type())
ipsoDiskDriveModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskDriveModel.setStatus(_A)
_IpsoDiskDriveCapacity_Type=DisplayString
_IpsoDiskDriveCapacity_Object=MibTableColumn
ipsoDiskDriveCapacity=_IpsoDiskDriveCapacity_Object((1,3,6,1,4,1,94,1,21,1,10,13,1,4),_IpsoDiskDriveCapacity_Type())
ipsoDiskDriveCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskDriveCapacity.setStatus(_A)
_IpsoDiskDriveLocation_Type=DisplayString
_IpsoDiskDriveLocation_Object=MibTableColumn
ipsoDiskDriveLocation=_IpsoDiskDriveLocation_Object((1,3,6,1,4,1,94,1,21,1,10,13,1,5),_IpsoDiskDriveLocation_Type())
ipsoDiskDriveLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDiskDriveLocation.setStatus(_A)
_IpsoFeatureName_Type=DisplayString
_IpsoFeatureName_Object=MibScalar
ipsoFeatureName=_IpsoFeatureName_Object((1,3,6,1,4,1,94,1,21,1,11,1),_IpsoFeatureName_Type())
ipsoFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoFeatureName.setStatus(_A)
_IpsoDaysToExpire_Type=Integer32
_IpsoDaysToExpire_Object=MibScalar
ipsoDaysToExpire=_IpsoDaysToExpire_Object((1,3,6,1,4,1,94,1,21,1,11,2),_IpsoDaysToExpire_Type())
ipsoDaysToExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:ipsoDaysToExpire.setStatus(_A)
ipsoChassisGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,1))
ipsoChassisGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_N),(_B,_i)))
if mibBuilder.loadTexts:ipsoChassisGroup.setStatus(_A)
ipsoFanGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,2))
ipsoFanGroup.setObjects(*((_B,_O),(_B,_j)))
if mibBuilder.loadTexts:ipsoFanGroup.setStatus(_A)
ipsoPowerSupplyGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,3))
ipsoPowerSupplyGroup.setObjects(*((_B,_P),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ipsoPowerSupplyGroup.setStatus(_A)
ipsoConfigGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,4))
ipsoConfigGroup.setObjects(*((_B,_Q),(_B,_I),(_B,_m),(_B,_n),(_B,_R),(_B,_o)))
if mibBuilder.loadTexts:ipsoConfigGroup.setStatus(_A)
ipsoImageGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,5))
ipsoImageGroup.setObjects(*((_B,_S),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ipsoImageGroup.setStatus(_A)
ipsoStorageGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,6))
ipsoStorageGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:ipsoStorageGroup.setStatus(_A)
ipsoProcessGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,7))
ipsoProcessGroup.setObjects(*((_B,_t),(_B,_T),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ipsoProcessGroup.setStatus(_A)
ipsoDiskMirrorGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,9))
ipsoDiskMirrorGroup.setObjects(*((_B,_y),(_B,'ipsoMirrorSetIndex'),(_B,'ipsoMirrorSetSourceDrive'),(_B,'ipsoMirrorSetDestinationDrive'),(_B,'ipsoMirrorSetSyncPercent')))
if mibBuilder.loadTexts:ipsoDiskMirrorGroup.setStatus(_A)
ipsoAssetGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,10))
ipsoAssetGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_U),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_H),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_G)))
if mibBuilder.loadTexts:ipsoAssetGroup.setStatus(_A)
ipsoLicenseGroup=ObjectGroup((1,3,6,1,4,1,94,1,21,1,11))
ipsoLicenseGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ipsoLicenseGroup.setStatus(_A)
systemTrapConfigurationChange=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,1))
if mibBuilder.loadTexts:systemTrapConfigurationChange.setStatus(_A)
systemTrapConfigurationFileChange=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,2))
systemTrapConfigurationFileChange.setObjects((_B,_I))
if mibBuilder.loadTexts:systemTrapConfigurationFileChange.setStatus(_A)
systemTrapConfigurationSaveChange=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,3))
systemTrapConfigurationSaveChange.setObjects((_B,_I))
if mibBuilder.loadTexts:systemTrapConfigurationSaveChange.setStatus(_A)
systemTrapLowDiskSpace=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,4))
systemTrapLowDiskSpace.setObjects(*((_E,_K),(_E,_L),(_E,_M),(_E,_J)))
if mibBuilder.loadTexts:systemTrapLowDiskSpace.setStatus(_A)
systemTrapNoDiskSpace=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,5))
systemTrapNoDiskSpace.setObjects(*((_E,_K),(_E,_L),(_E,_M),(_E,_J)))
if mibBuilder.loadTexts:systemTrapNoDiskSpace.setStatus(_A)
systemTrapDiskFailure=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,6))
systemTrapDiskFailure.setObjects((_B,_H))
if mibBuilder.loadTexts:systemTrapDiskFailure.setStatus(_A)
systemTrapDiskMirrorSetCreate=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,7))
systemTrapDiskMirrorSetCreate.setObjects(*((_B,_F),(_B,_X),(_B,_Y),(_B,_G),(_B,_G)))
if mibBuilder.loadTexts:systemTrapDiskMirrorSetCreate.setStatus(_A)
systemTrapDiskMirrorSetDelete=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,8))
systemTrapDiskMirrorSetDelete.setObjects(*((_B,_F),(_B,_X),(_B,_Y),(_B,_G),(_B,_G)))
if mibBuilder.loadTexts:systemTrapDiskMirrorSetDelete.setStatus(_A)
systemTrapSnmpProcessShutdown=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,9))
if mibBuilder.loadTexts:systemTrapSnmpProcessShutdown.setStatus(_A)
systemTrapDiskMirrorSyncFailure=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,10))
systemTrapDiskMirrorSyncFailure.setObjects((_B,_F))
if mibBuilder.loadTexts:systemTrapDiskMirrorSyncFailure.setStatus(_A)
systemTrapDiskMirrorSyncSuccess=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,11))
systemTrapDiskMirrorSyncSuccess.setObjects((_B,_F))
if mibBuilder.loadTexts:systemTrapDiskMirrorSyncSuccess.setStatus(_A)
systemTrapLicense=NotificationType((1,3,6,1,4,1,94,1,21,1,8,1,16))
systemTrapLicense.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:systemTrapLicense.setStatus(_A)
ipsoNotificationGroup=NotificationGroup((1,3,6,1,4,1,94,1,21,1,8))
ipsoNotificationGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ipsoNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nokia':nokia,'nokiaProducts':nokiaProducts,'ipsoProducts':ipsoProducts,'ipsoSystem':ipsoSystem,'ipsoChassisGroup':ipsoChassisGroup,_d:ipsoChassisSerialNumber,_e:ipsoChassisMBType,_f:ipsoChassisMBRevNumber,_g:ipsoChassisMBSerialNumber,_h:ipsoChassisTemperature,'ipsoCardTable':ipsoCardTable,'ipsoCardEntry':ipsoCardEntry,_N:ipsoCardIndex,_i:ipsoCardOperStatus,'ipsoFanGroup':ipsoFanGroup,'ipsoFanTable':ipsoFanTable,'ipsoFanEntry':ipsoFanEntry,_O:ipsoFanIndex,_j:ipsoFanOperStatus,'ipsoPowerSupplyGroup':ipsoPowerSupplyGroup,'ipsoPowerSupplyTable':ipsoPowerSupplyTable,'ipsoPowerSupplyEntry':ipsoPowerSupplyEntry,_P:ipsoPowerSupplyIndex,_k:ipsoPowerSupplyOverTemperature,_l:ipsoPowerSupplyOperStatus,'ipsoConfigGroup':ipsoConfigGroup,'ipsoConfigTable':ipsoConfigTable,'ipsoConfigEntry':ipsoConfigEntry,_Q:ipsoConfigIndex,_I:ipsoConfigFilePath,_m:ipsoConfigFileDateAndTime,_n:ipsoConfigLogSize,'ipsoConfigLogTable':ipsoConfigLogTable,'ipsoConfigLogEntry':ipsoConfigLogEntry,_R:ipsoConfigLogIndex,_o:ipsoConfigLogDescr,'ipsoImageGroup':ipsoImageGroup,'ipsoImageTable':ipsoImageTable,'ipsoImageEntry':ipsoImageEntry,_S:ipsoImageIndex,_p:ipsoImageVersionNumber,_q:ipsoImageSerialNumber,_r:ipsoImageTimeOfLoad,'ipsoStorageGroup':ipsoStorageGroup,_s:ipsoSIMMTotal,'ipsoProcessGroup':ipsoProcessGroup,_t:ipsoProcessorUtilization,'ipsoProcessTable':ipsoProcessTable,'ipsoProcessEntry':ipsoProcessEntry,_T:ipsoProcessID,_u:ipsoProcessParentID,_v:ipsoProcessOwner,_w:ipsoProcessMemory,_x:ipsoProcessPercentCPU,'ipsoNotificationGroup':ipsoNotificationGroup,'systemTraps':systemTraps,_AH:systemTrapConfigurationChange,_AI:systemTrapConfigurationFileChange,_AJ:systemTrapConfigurationSaveChange,_AK:systemTrapLowDiskSpace,_AL:systemTrapNoDiskSpace,_AM:systemTrapDiskFailure,_AN:systemTrapDiskMirrorSetCreate,_AO:systemTrapDiskMirrorSetDelete,_AR:systemTrapSnmpProcessShutdown,_AP:systemTrapDiskMirrorSyncFailure,_AQ:systemTrapDiskMirrorSyncSuccess,_AS:systemTrapLicense,'ipsoDiskMirrorGroup':ipsoDiskMirrorGroup,_y:ipsoTotalDiskMirrorSets,'ipsoDiskMirrorSetTable':ipsoDiskMirrorSetTable,'ipsoDiskMirrorSetEntry':ipsoDiskMirrorSetEntry,_F:ipsoDiskMirrorSetIndex,_X:ipsoDiskMirrorSetSourceDriveIndex,_Y:ipsoDiskMirrorSetDestinationDriveIndex,'ipsoDiskMirrorSetSyncPercent':ipsoDiskMirrorSetSyncPercent,'ipsoAssetGroup':ipsoAssetGroup,_z:ipsoAssetChassisSerialNumber,_A0:ipsoCPUModel,_A1:ipsoCPUMfr,_A2:ipsoCPUFreq,_A3:ipsoKernMaxMem,_A4:ipsoMotherBoardSerNum,_A5:ipsoMotherBoardRev,_A6:ipsoMotherBoardModel,_A7:ipsoOSRelease,_A8:ipsoOSVersion,_A9:ipsoProductModel,'ipsoAssetTable':ipsoAssetTable,'ipsoAssetEntry':ipsoAssetEntry,_U:ipsoPkgIndex,_AA:ipsoPkgName,_AB:ipsoPkgMajorVersion,_AC:ipsoPkgMinorVersion,_AD:ipsoPkgLicense,'ipsoDiskDriveTable':ipsoDiskDriveTable,'ipsoDiskDriveEntry':ipsoDiskDriveEntry,_H:ipsoDiskDriveIndex,_AE:ipsoDiskSysDriveIndex,_AF:ipsoDiskDriveModel,_AG:ipsoDiskDriveCapacity,_G:ipsoDiskDriveLocation,'ipsoLicenseGroup':ipsoLicenseGroup,_V:ipsoFeatureName,_W:ipsoDaysToExpire})