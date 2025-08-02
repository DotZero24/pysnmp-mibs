_A1='cpqHoMibHealthStatusArray'
_A0='cpqHoBootPagingFileVolumeFreeSpace'
_z='cpqServerUUID'
_y='cpqSerialNum'
_x='cpqPwrWarnDuration'
_w='cpqPwrWarnThreshold'
_v='cpqPwrWarnType'
_u='cpqHoSWRunningRedundancyMode'
_t='cpqHoSWRunningIdentifier'
_s='cpqHoSWRunningConfigStatus'
_r='cpqHoSWRunningStatus'
_q='cpqHoSWRunningVersion'
_p='cpqHoSWRunningDesc'
_o='cpqHoCriticalSoftwareUpdateData'
_n='cpqHoFwVerIndex'
_m='cpqHoClientIndex'
_l='cpqHoSwVerIndex'
_k='cpqHoSWRunningIndex'
_j='cpqHoIfPhysMapIndex'
_i='cpqHoFileSysIndex'
_h='cpqHoCpuUtilUnitIndex'
_g='disabled'
_f='cpqHoOsCommonModuleIndex'
_e='NotificationType'
_d='cpqHoBootPagingFileMinimumSize'
_c='cpqHoBootPagingFileSize'
_b='cpqHoSWRunningEventTime'
_a='cpqHoSWRunningCountMax'
_Z='cpqHoSWRunningCountMin'
_Y='cpqHoSWRunningCount'
_X='cpqHoSwRunningTrapDesc'
_W='cpqHoSwPerfAppErrorDesc'
_V='cpqHoGenericData'
_U='cpqHoCrashDumpState'
_T='cpqHoSWRunningName'
_S='cpqHoIfPhysMapPort'
_R='failed'
_Q='degraded'
_P='ok'
_O='unknown'
_N='cpqHoIfPhysMapSlot'
_M='other'
_L='OctetString'
_K='optional'
_J='cpqHoTrapFlags'
_I='deprecated'
_H='sysName'
_G='SNMPv2-MIB'
_F='read-write'
_E='Integer32'
_D='DisplayString'
_C='CPQHOST-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_e,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_e,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqHostOs_ObjectIdentity=ObjectIdentity
cpqHostOs=_CpqHostOs_ObjectIdentity((1,3,6,1,4,1,232,11))
_CpqHoMibRev_ObjectIdentity=ObjectIdentity
cpqHoMibRev=_CpqHoMibRev_ObjectIdentity((1,3,6,1,4,1,232,11,1))
class _CpqHoMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqHoMibRevMajor_Type.__name__=_E
_CpqHoMibRevMajor_Object=MibScalar
cpqHoMibRevMajor=_CpqHoMibRevMajor_Object((1,3,6,1,4,1,232,11,1,1),_CpqHoMibRevMajor_Type())
cpqHoMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMibRevMajor.setStatus(_A)
class _CpqHoMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoMibRevMinor_Type.__name__=_E
_CpqHoMibRevMinor_Object=MibScalar
cpqHoMibRevMinor=_CpqHoMibRevMinor_Object((1,3,6,1,4,1,232,11,1,2),_CpqHoMibRevMinor_Type())
cpqHoMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMibRevMinor.setStatus(_A)
class _CpqHoMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoMibCondition_Type.__name__=_E
_CpqHoMibCondition_Object=MibScalar
cpqHoMibCondition=_CpqHoMibCondition_Object((1,3,6,1,4,1,232,11,1,3),_CpqHoMibCondition_Type())
cpqHoMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMibCondition.setStatus(_A)
_CpqHoComponent_ObjectIdentity=ObjectIdentity
cpqHoComponent=_CpqHoComponent_ObjectIdentity((1,3,6,1,4,1,232,11,2))
_CpqHoInterface_ObjectIdentity=ObjectIdentity
cpqHoInterface=_CpqHoInterface_ObjectIdentity((1,3,6,1,4,1,232,11,2,1))
_CpqHoOsCommon_ObjectIdentity=ObjectIdentity
cpqHoOsCommon=_CpqHoOsCommon_ObjectIdentity((1,3,6,1,4,1,232,11,2,1,4))
class _CpqHoOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoOsCommonPollFreq_Type.__name__=_E
_CpqHoOsCommonPollFreq_Object=MibScalar
cpqHoOsCommonPollFreq=_CpqHoOsCommonPollFreq_Object((1,3,6,1,4,1,232,11,2,1,4,1),_CpqHoOsCommonPollFreq_Type())
cpqHoOsCommonPollFreq.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoOsCommonPollFreq.setStatus(_A)
_CpqHoOsCommonModuleTable_Object=MibTable
cpqHoOsCommonModuleTable=_CpqHoOsCommonModuleTable_Object((1,3,6,1,4,1,232,11,2,1,4,2))
if mibBuilder.loadTexts:cpqHoOsCommonModuleTable.setStatus(_I)
_CpqHoOsCommonModuleEntry_Object=MibTableRow
cpqHoOsCommonModuleEntry=_CpqHoOsCommonModuleEntry_Object((1,3,6,1,4,1,232,11,2,1,4,2,1))
cpqHoOsCommonModuleEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cpqHoOsCommonModuleEntry.setStatus(_I)
class _CpqHoOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqHoOsCommonModuleIndex_Type.__name__=_E
_CpqHoOsCommonModuleIndex_Object=MibTableColumn
cpqHoOsCommonModuleIndex=_CpqHoOsCommonModuleIndex_Object((1,3,6,1,4,1,232,11,2,1,4,2,1,1),_CpqHoOsCommonModuleIndex_Type())
cpqHoOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsCommonModuleIndex.setStatus(_I)
class _CpqHoOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoOsCommonModuleName_Type.__name__=_D
_CpqHoOsCommonModuleName_Object=MibTableColumn
cpqHoOsCommonModuleName=_CpqHoOsCommonModuleName_Object((1,3,6,1,4,1,232,11,2,1,4,2,1,2),_CpqHoOsCommonModuleName_Type())
cpqHoOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsCommonModuleName.setStatus(_I)
class _CpqHoOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqHoOsCommonModuleVersion_Type.__name__=_D
_CpqHoOsCommonModuleVersion_Object=MibTableColumn
cpqHoOsCommonModuleVersion=_CpqHoOsCommonModuleVersion_Object((1,3,6,1,4,1,232,11,2,1,4,2,1,3),_CpqHoOsCommonModuleVersion_Type())
cpqHoOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsCommonModuleVersion.setStatus(_I)
class _CpqHoOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoOsCommonModuleDate_Type.__name__=_L
_CpqHoOsCommonModuleDate_Object=MibTableColumn
cpqHoOsCommonModuleDate=_CpqHoOsCommonModuleDate_Object((1,3,6,1,4,1,232,11,2,1,4,2,1,4),_CpqHoOsCommonModuleDate_Type())
cpqHoOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsCommonModuleDate.setStatus(_I)
class _CpqHoOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoOsCommonModulePurpose_Type.__name__=_D
_CpqHoOsCommonModulePurpose_Object=MibTableColumn
cpqHoOsCommonModulePurpose=_CpqHoOsCommonModulePurpose_Object((1,3,6,1,4,1,232,11,2,1,4,2,1,5),_CpqHoOsCommonModulePurpose_Type())
cpqHoOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsCommonModulePurpose.setStatus(_I)
_CpqHoInfo_ObjectIdentity=ObjectIdentity
cpqHoInfo=_CpqHoInfo_ObjectIdentity((1,3,6,1,4,1,232,11,2,2))
class _CpqHoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoName_Type.__name__=_D
_CpqHoName_Object=MibScalar
cpqHoName=_CpqHoName_Object((1,3,6,1,4,1,232,11,2,2,1),_CpqHoName_Type())
cpqHoName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoName.setStatus(_A)
class _CpqHoVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoVersion_Type.__name__=_D
_CpqHoVersion_Object=MibScalar
cpqHoVersion=_CpqHoVersion_Object((1,3,6,1,4,1,232,11,2,2,2),_CpqHoVersion_Type())
cpqHoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoVersion.setStatus(_A)
class _CpqHoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoDesc_Type.__name__=_D
_CpqHoDesc_Object=MibScalar
cpqHoDesc=_CpqHoDesc_Object((1,3,6,1,4,1,232,11,2,2,3),_CpqHoDesc_Type())
cpqHoDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoDesc.setStatus(_A)
class _CpqHoOsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58)));namedValues=NamedValues(*((_M,1),('netware',2),('windowsnt',3),('sco-unix',4),('unixware',5),('os-2',6),('ms-dos',7),('dos-windows',8),('windows95',9),('windows98',10),('open-vms',11),('nsk',12),('windowsCE',13),('linux',14),('windows2000',15),('tru64UNIX',16),('windows2003',17),('windows2003-x64',18),('solaris',19),('windows2003-ia64',20),('windows2008',21),('windows2008-x64',22),('windows2008-ia64',23),('vmware-esx',24),('vmware-esxi',25),('windows2012',26),('windows7',27),('windows7-x64',28),('windows8',29),('windows8-x64',30),('windows81',31),('windows81-x64',32),('windowsxp',33),('windowsxp-x64',34),('windowsvista',35),('windowsvista-x64',36),('windows2008-r2',37),('windows2012-r2',38),('rhel',39),('rhel-64',40),('solaris-64',41),('sles',42),('sles-64',43),('ubuntu',44),('ubuntu-64',45),('debian',46),('debian-64',47),('linux-64-bit',48),('other-64-bit',49),('centos-32bit',50),('centos-64bit',51),('oracle-linux32',52),('oracle-linux64',53),('apple-osx',54),('windows2016',55),('nanoserver',56),('windows2019',57),('windows10-x64',58)))
_CpqHoOsType_Type.__name__=_E
_CpqHoOsType_Object=MibScalar
cpqHoOsType=_CpqHoOsType_Object((1,3,6,1,4,1,232,11,2,2,4),_CpqHoOsType_Type())
cpqHoOsType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoOsType.setStatus(_A)
class _CpqHoTelnet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('available',2),('notavailable',3)))
_CpqHoTelnet_Type.__name__=_E
_CpqHoTelnet_Object=MibScalar
cpqHoTelnet=_CpqHoTelnet_Object((1,3,6,1,4,1,232,11,2,2,5),_CpqHoTelnet_Type())
cpqHoTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoTelnet.setStatus(_A)
class _CpqHoSystemRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqHoSystemRole_Type.__name__=_D
_CpqHoSystemRole_Object=MibScalar
cpqHoSystemRole=_CpqHoSystemRole_Object((1,3,6,1,4,1,232,11,2,2,6),_CpqHoSystemRole_Type())
cpqHoSystemRole.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSystemRole.setStatus(_A)
class _CpqHoSystemRoleDetail_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CpqHoSystemRoleDetail_Type.__name__=_D
_CpqHoSystemRoleDetail_Object=MibScalar
cpqHoSystemRoleDetail=_CpqHoSystemRoleDetail_Object((1,3,6,1,4,1,232,11,2,2,7),_CpqHoSystemRoleDetail_Type())
cpqHoSystemRoleDetail.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSystemRoleDetail.setStatus(_A)
class _CpqHoCrashDumpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('completememorydump',1),('kernelmemorydump',2),('smallmemorydump',3),('none',4)))
_CpqHoCrashDumpState_Type.__name__=_E
_CpqHoCrashDumpState_Object=MibScalar
cpqHoCrashDumpState=_CpqHoCrashDumpState_Object((1,3,6,1,4,1,232,11,2,2,8),_CpqHoCrashDumpState_Type())
cpqHoCrashDumpState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCrashDumpState.setStatus(_A)
class _CpqHoCrashDumpCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoCrashDumpCondition_Type.__name__=_E
_CpqHoCrashDumpCondition_Object=MibScalar
cpqHoCrashDumpCondition=_CpqHoCrashDumpCondition_Object((1,3,6,1,4,1,232,11,2,2,9),_CpqHoCrashDumpCondition_Type())
cpqHoCrashDumpCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCrashDumpCondition.setStatus(_A)
class _CpqHoCrashDumpMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_g,2)))
_CpqHoCrashDumpMonitoring_Type.__name__=_E
_CpqHoCrashDumpMonitoring_Object=MibScalar
cpqHoCrashDumpMonitoring=_CpqHoCrashDumpMonitoring_Object((1,3,6,1,4,1,232,11,2,2,10),_CpqHoCrashDumpMonitoring_Type())
cpqHoCrashDumpMonitoring.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoCrashDumpMonitoring.setStatus(_K)
class _CpqHoMaxLogicalCPUSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoMaxLogicalCPUSupported_Type.__name__=_E
_CpqHoMaxLogicalCPUSupported_Object=MibScalar
cpqHoMaxLogicalCPUSupported=_CpqHoMaxLogicalCPUSupported_Object((1,3,6,1,4,1,232,11,2,2,11),_CpqHoMaxLogicalCPUSupported_Type())
cpqHoMaxLogicalCPUSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMaxLogicalCPUSupported.setStatus(_K)
class _CpqHoSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSystemName_Type.__name__=_D
_CpqHoSystemName_Object=MibScalar
cpqHoSystemName=_CpqHoSystemName_Object((1,3,6,1,4,1,232,11,2,2,12),_CpqHoSystemName_Type())
cpqHoSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSystemName.setStatus(_A)
class _CpqHosysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHosysDescr_Type.__name__=_D
_CpqHosysDescr_Object=MibScalar
cpqHosysDescr=_CpqHosysDescr_Object((1,3,6,1,4,1,232,11,2,2,13),_CpqHosysDescr_Type())
cpqHosysDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHosysDescr.setStatus(_K)
_CpqHoUtil_ObjectIdentity=ObjectIdentity
cpqHoUtil=_CpqHoUtil_ObjectIdentity((1,3,6,1,4,1,232,11,2,3))
_CpqHoCpuUtilTable_Object=MibTable
cpqHoCpuUtilTable=_CpqHoCpuUtilTable_Object((1,3,6,1,4,1,232,11,2,3,1))
if mibBuilder.loadTexts:cpqHoCpuUtilTable.setStatus(_A)
_CpqHoCpuUtilEntry_Object=MibTableRow
cpqHoCpuUtilEntry=_CpqHoCpuUtilEntry_Object((1,3,6,1,4,1,232,11,2,3,1,1))
cpqHoCpuUtilEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cpqHoCpuUtilEntry.setStatus(_A)
class _CpqHoCpuUtilUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoCpuUtilUnitIndex_Type.__name__=_E
_CpqHoCpuUtilUnitIndex_Object=MibTableColumn
cpqHoCpuUtilUnitIndex=_CpqHoCpuUtilUnitIndex_Object((1,3,6,1,4,1,232,11,2,3,1,1,1),_CpqHoCpuUtilUnitIndex_Type())
cpqHoCpuUtilUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilUnitIndex.setStatus(_A)
_CpqHoCpuUtilMin_Type=Integer32
_CpqHoCpuUtilMin_Object=MibTableColumn
cpqHoCpuUtilMin=_CpqHoCpuUtilMin_Object((1,3,6,1,4,1,232,11,2,3,1,1,2),_CpqHoCpuUtilMin_Type())
cpqHoCpuUtilMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilMin.setStatus(_A)
_CpqHoCpuUtilFiveMin_Type=Integer32
_CpqHoCpuUtilFiveMin_Object=MibTableColumn
cpqHoCpuUtilFiveMin=_CpqHoCpuUtilFiveMin_Object((1,3,6,1,4,1,232,11,2,3,1,1,3),_CpqHoCpuUtilFiveMin_Type())
cpqHoCpuUtilFiveMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilFiveMin.setStatus(_A)
_CpqHoCpuUtilThirtyMin_Type=Integer32
_CpqHoCpuUtilThirtyMin_Object=MibTableColumn
cpqHoCpuUtilThirtyMin=_CpqHoCpuUtilThirtyMin_Object((1,3,6,1,4,1,232,11,2,3,1,1,4),_CpqHoCpuUtilThirtyMin_Type())
cpqHoCpuUtilThirtyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilThirtyMin.setStatus(_A)
_CpqHoCpuUtilHour_Type=Integer32
_CpqHoCpuUtilHour_Object=MibTableColumn
cpqHoCpuUtilHour=_CpqHoCpuUtilHour_Object((1,3,6,1,4,1,232,11,2,3,1,1,5),_CpqHoCpuUtilHour_Type())
cpqHoCpuUtilHour.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilHour.setStatus(_A)
class _CpqHoCpuUtilHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoCpuUtilHwLocation_Type.__name__=_D
_CpqHoCpuUtilHwLocation_Object=MibTableColumn
cpqHoCpuUtilHwLocation=_CpqHoCpuUtilHwLocation_Object((1,3,6,1,4,1,232,11,2,3,1,1,6),_CpqHoCpuUtilHwLocation_Type())
cpqHoCpuUtilHwLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCpuUtilHwLocation.setStatus(_K)
_CpqHoFileSys_ObjectIdentity=ObjectIdentity
cpqHoFileSys=_CpqHoFileSys_ObjectIdentity((1,3,6,1,4,1,232,11,2,4))
_CpqHoFileSysTable_Object=MibTable
cpqHoFileSysTable=_CpqHoFileSysTable_Object((1,3,6,1,4,1,232,11,2,4,1))
if mibBuilder.loadTexts:cpqHoFileSysTable.setStatus(_A)
_CpqHoFileSysEntry_Object=MibTableRow
cpqHoFileSysEntry=_CpqHoFileSysEntry_Object((1,3,6,1,4,1,232,11,2,4,1,1))
cpqHoFileSysEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cpqHoFileSysEntry.setStatus(_A)
class _CpqHoFileSysIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoFileSysIndex_Type.__name__=_E
_CpqHoFileSysIndex_Object=MibTableColumn
cpqHoFileSysIndex=_CpqHoFileSysIndex_Object((1,3,6,1,4,1,232,11,2,4,1,1,1),_CpqHoFileSysIndex_Type())
cpqHoFileSysIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysIndex.setStatus(_A)
class _CpqHoFileSysDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoFileSysDesc_Type.__name__=_D
_CpqHoFileSysDesc_Object=MibTableColumn
cpqHoFileSysDesc=_CpqHoFileSysDesc_Object((1,3,6,1,4,1,232,11,2,4,1,1,2),_CpqHoFileSysDesc_Type())
cpqHoFileSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysDesc.setStatus(_A)
_CpqHoFileSysSpaceTotal_Type=Integer32
_CpqHoFileSysSpaceTotal_Object=MibTableColumn
cpqHoFileSysSpaceTotal=_CpqHoFileSysSpaceTotal_Object((1,3,6,1,4,1,232,11,2,4,1,1,3),_CpqHoFileSysSpaceTotal_Type())
cpqHoFileSysSpaceTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysSpaceTotal.setStatus(_A)
_CpqHoFileSysSpaceUsed_Type=Integer32
_CpqHoFileSysSpaceUsed_Object=MibTableColumn
cpqHoFileSysSpaceUsed=_CpqHoFileSysSpaceUsed_Object((1,3,6,1,4,1,232,11,2,4,1,1,4),_CpqHoFileSysSpaceUsed_Type())
cpqHoFileSysSpaceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysSpaceUsed.setStatus(_A)
_CpqHoFileSysPercentSpaceUsed_Type=Integer32
_CpqHoFileSysPercentSpaceUsed_Object=MibTableColumn
cpqHoFileSysPercentSpaceUsed=_CpqHoFileSysPercentSpaceUsed_Object((1,3,6,1,4,1,232,11,2,4,1,1,5),_CpqHoFileSysPercentSpaceUsed_Type())
cpqHoFileSysPercentSpaceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysPercentSpaceUsed.setStatus(_A)
_CpqHoFileSysAllocUnitsTotal_Type=Integer32
_CpqHoFileSysAllocUnitsTotal_Object=MibTableColumn
cpqHoFileSysAllocUnitsTotal=_CpqHoFileSysAllocUnitsTotal_Object((1,3,6,1,4,1,232,11,2,4,1,1,6),_CpqHoFileSysAllocUnitsTotal_Type())
cpqHoFileSysAllocUnitsTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysAllocUnitsTotal.setStatus(_A)
_CpqHoFileSysAllocUnitsUsed_Type=Integer32
_CpqHoFileSysAllocUnitsUsed_Object=MibTableColumn
cpqHoFileSysAllocUnitsUsed=_CpqHoFileSysAllocUnitsUsed_Object((1,3,6,1,4,1,232,11,2,4,1,1,7),_CpqHoFileSysAllocUnitsUsed_Type())
cpqHoFileSysAllocUnitsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysAllocUnitsUsed.setStatus(_A)
class _CpqHoFileSysStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoFileSysStatus_Type.__name__=_E
_CpqHoFileSysStatus_Object=MibTableColumn
cpqHoFileSysStatus=_CpqHoFileSysStatus_Object((1,3,6,1,4,1,232,11,2,4,1,1,8),_CpqHoFileSysStatus_Type())
cpqHoFileSysStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysStatus.setStatus(_A)
class _CpqHoFileSysShortDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoFileSysShortDesc_Type.__name__=_D
_CpqHoFileSysShortDesc_Object=MibTableColumn
cpqHoFileSysShortDesc=_CpqHoFileSysShortDesc_Object((1,3,6,1,4,1,232,11,2,4,1,1,9),_CpqHoFileSysShortDesc_Type())
cpqHoFileSysShortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysShortDesc.setStatus(_A)
class _CpqHoFileSysCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoFileSysCondition_Type.__name__=_E
_CpqHoFileSysCondition_Object=MibScalar
cpqHoFileSysCondition=_CpqHoFileSysCondition_Object((1,3,6,1,4,1,232,11,2,4,2),_CpqHoFileSysCondition_Type())
cpqHoFileSysCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFileSysCondition.setStatus(_A)
_CpqHoIfPhysMap_ObjectIdentity=ObjectIdentity
cpqHoIfPhysMap=_CpqHoIfPhysMap_ObjectIdentity((1,3,6,1,4,1,232,11,2,5))
_CpqHoIfPhysMapTable_Object=MibTable
cpqHoIfPhysMapTable=_CpqHoIfPhysMapTable_Object((1,3,6,1,4,1,232,11,2,5,1))
if mibBuilder.loadTexts:cpqHoIfPhysMapTable.setStatus(_I)
_CpqHoIfPhysMapEntry_Object=MibTableRow
cpqHoIfPhysMapEntry=_CpqHoIfPhysMapEntry_Object((1,3,6,1,4,1,232,11,2,5,1,1))
cpqHoIfPhysMapEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cpqHoIfPhysMapEntry.setStatus(_I)
class _CpqHoIfPhysMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoIfPhysMapIndex_Type.__name__=_E
_CpqHoIfPhysMapIndex_Object=MibTableColumn
cpqHoIfPhysMapIndex=_CpqHoIfPhysMapIndex_Object((1,3,6,1,4,1,232,11,2,5,1,1,1),_CpqHoIfPhysMapIndex_Type())
cpqHoIfPhysMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapIndex.setStatus(_I)
class _CpqHoIfPhysMapSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqHoIfPhysMapSlot_Type.__name__=_E
_CpqHoIfPhysMapSlot_Object=MibTableColumn
cpqHoIfPhysMapSlot=_CpqHoIfPhysMapSlot_Object((1,3,6,1,4,1,232,11,2,5,1,1,2),_CpqHoIfPhysMapSlot_Type())
cpqHoIfPhysMapSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapSlot.setStatus(_I)
_CpqHoIfPhysMapIoBaseAddr_Type=Integer32
_CpqHoIfPhysMapIoBaseAddr_Object=MibTableColumn
cpqHoIfPhysMapIoBaseAddr=_CpqHoIfPhysMapIoBaseAddr_Object((1,3,6,1,4,1,232,11,2,5,1,1,3),_CpqHoIfPhysMapIoBaseAddr_Type())
cpqHoIfPhysMapIoBaseAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapIoBaseAddr.setStatus(_I)
class _CpqHoIfPhysMapIrq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqHoIfPhysMapIrq_Type.__name__=_E
_CpqHoIfPhysMapIrq_Object=MibTableColumn
cpqHoIfPhysMapIrq=_CpqHoIfPhysMapIrq_Object((1,3,6,1,4,1,232,11,2,5,1,1,4),_CpqHoIfPhysMapIrq_Type())
cpqHoIfPhysMapIrq.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapIrq.setStatus(_I)
_CpqHoIfPhysMapDma_Type=Integer32
_CpqHoIfPhysMapDma_Object=MibTableColumn
cpqHoIfPhysMapDma=_CpqHoIfPhysMapDma_Object((1,3,6,1,4,1,232,11,2,5,1,1,5),_CpqHoIfPhysMapDma_Type())
cpqHoIfPhysMapDma.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapDma.setStatus(_I)
_CpqHoIfPhysMapMemBaseAddr_Type=Integer32
_CpqHoIfPhysMapMemBaseAddr_Object=MibTableColumn
cpqHoIfPhysMapMemBaseAddr=_CpqHoIfPhysMapMemBaseAddr_Object((1,3,6,1,4,1,232,11,2,5,1,1,6),_CpqHoIfPhysMapMemBaseAddr_Type())
cpqHoIfPhysMapMemBaseAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapMemBaseAddr.setStatus(_I)
_CpqHoIfPhysMapPort_Type=Integer32
_CpqHoIfPhysMapPort_Object=MibTableColumn
cpqHoIfPhysMapPort=_CpqHoIfPhysMapPort_Object((1,3,6,1,4,1,232,11,2,5,1,1,7),_CpqHoIfPhysMapPort_Type())
cpqHoIfPhysMapPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapPort.setStatus(_I)
class _CpqHoIfPhysMapDuplexState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('half',2),('full',3)))
_CpqHoIfPhysMapDuplexState_Type.__name__=_E
_CpqHoIfPhysMapDuplexState_Object=MibTableColumn
cpqHoIfPhysMapDuplexState=_CpqHoIfPhysMapDuplexState_Object((1,3,6,1,4,1,232,11,2,5,1,1,8),_CpqHoIfPhysMapDuplexState_Type())
cpqHoIfPhysMapDuplexState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapDuplexState.setStatus(_I)
class _CpqHoIfPhysMapCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoIfPhysMapCondition_Type.__name__=_E
_CpqHoIfPhysMapCondition_Object=MibTableColumn
cpqHoIfPhysMapCondition=_CpqHoIfPhysMapCondition_Object((1,3,6,1,4,1,232,11,2,5,1,1,9),_CpqHoIfPhysMapCondition_Type())
cpqHoIfPhysMapCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapCondition.setStatus(_I)
class _CpqHoIfPhysMapOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_P,2),(_Q,3),(_R,4)))
_CpqHoIfPhysMapOverallCondition_Type.__name__=_E
_CpqHoIfPhysMapOverallCondition_Object=MibScalar
cpqHoIfPhysMapOverallCondition=_CpqHoIfPhysMapOverallCondition_Object((1,3,6,1,4,1,232,11,2,5,2),_CpqHoIfPhysMapOverallCondition_Type())
cpqHoIfPhysMapOverallCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoIfPhysMapOverallCondition.setStatus(_I)
_CpqHoSWRunning_ObjectIdentity=ObjectIdentity
cpqHoSWRunning=_CpqHoSWRunning_ObjectIdentity((1,3,6,1,4,1,232,11,2,6))
_CpqHoSWRunningTable_Object=MibTable
cpqHoSWRunningTable=_CpqHoSWRunningTable_Object((1,3,6,1,4,1,232,11,2,6,1))
if mibBuilder.loadTexts:cpqHoSWRunningTable.setStatus(_A)
_CpqHoSWRunningEntry_Object=MibTableRow
cpqHoSWRunningEntry=_CpqHoSWRunningEntry_Object((1,3,6,1,4,1,232,11,2,6,1,1))
cpqHoSWRunningEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cpqHoSWRunningEntry.setStatus(_A)
class _CpqHoSWRunningIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoSWRunningIndex_Type.__name__=_E
_CpqHoSWRunningIndex_Object=MibTableColumn
cpqHoSWRunningIndex=_CpqHoSWRunningIndex_Object((1,3,6,1,4,1,232,11,2,6,1,1,1),_CpqHoSWRunningIndex_Type())
cpqHoSWRunningIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningIndex.setStatus(_A)
class _CpqHoSWRunningName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSWRunningName_Type.__name__=_D
_CpqHoSWRunningName_Object=MibTableColumn
cpqHoSWRunningName=_CpqHoSWRunningName_Object((1,3,6,1,4,1,232,11,2,6,1,1,2),_CpqHoSWRunningName_Type())
cpqHoSWRunningName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningName.setStatus(_A)
class _CpqHoSWRunningDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSWRunningDesc_Type.__name__=_D
_CpqHoSWRunningDesc_Object=MibTableColumn
cpqHoSWRunningDesc=_CpqHoSWRunningDesc_Object((1,3,6,1,4,1,232,11,2,6,1,1,3),_CpqHoSWRunningDesc_Type())
cpqHoSWRunningDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningDesc.setStatus(_A)
class _CpqHoSWRunningVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSWRunningVersion_Type.__name__=_D
_CpqHoSWRunningVersion_Object=MibTableColumn
cpqHoSWRunningVersion=_CpqHoSWRunningVersion_Object((1,3,6,1,4,1,232,11,2,6,1,1,4),_CpqHoSWRunningVersion_Type())
cpqHoSWRunningVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningVersion.setStatus(_A)
class _CpqHoSWRunningDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoSWRunningDate_Type.__name__=_L
_CpqHoSWRunningDate_Object=MibTableColumn
cpqHoSWRunningDate=_CpqHoSWRunningDate_Object((1,3,6,1,4,1,232,11,2,6,1,1,5),_CpqHoSWRunningDate_Type())
cpqHoSWRunningDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningDate.setStatus(_A)
class _CpqHoSWRunningMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('start',2),('stop',3),('startAndStop',4),('count',5),('startAndCount',6),('countAndStop',7),('startCountAndStop',8)))
_CpqHoSWRunningMonitor_Type.__name__=_E
_CpqHoSWRunningMonitor_Object=MibTableColumn
cpqHoSWRunningMonitor=_CpqHoSWRunningMonitor_Object((1,3,6,1,4,1,232,11,2,6,1,1,6),_CpqHoSWRunningMonitor_Type())
cpqHoSWRunningMonitor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningMonitor.setStatus(_A)
class _CpqHoSWRunningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('started',2),('stopped',3)))
_CpqHoSWRunningState_Type.__name__=_E
_CpqHoSWRunningState_Object=MibTableColumn
cpqHoSWRunningState=_CpqHoSWRunningState_Object((1,3,6,1,4,1,232,11,2,6,1,1,7),_CpqHoSWRunningState_Type())
cpqHoSWRunningState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningState.setStatus(_A)
class _CpqHoSWRunningCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoSWRunningCount_Type.__name__=_E
_CpqHoSWRunningCount_Object=MibTableColumn
cpqHoSWRunningCount=_CpqHoSWRunningCount_Object((1,3,6,1,4,1,232,11,2,6,1,1,8),_CpqHoSWRunningCount_Type())
cpqHoSWRunningCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningCount.setStatus(_K)
class _CpqHoSWRunningCountMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoSWRunningCountMin_Type.__name__=_E
_CpqHoSWRunningCountMin_Object=MibTableColumn
cpqHoSWRunningCountMin=_CpqHoSWRunningCountMin_Object((1,3,6,1,4,1,232,11,2,6,1,1,9),_CpqHoSWRunningCountMin_Type())
cpqHoSWRunningCountMin.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSWRunningCountMin.setStatus(_K)
class _CpqHoSWRunningCountMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoSWRunningCountMax_Type.__name__=_E
_CpqHoSWRunningCountMax_Object=MibTableColumn
cpqHoSWRunningCountMax=_CpqHoSWRunningCountMax_Object((1,3,6,1,4,1,232,11,2,6,1,1,10),_CpqHoSWRunningCountMax_Type())
cpqHoSWRunningCountMax.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSWRunningCountMax.setStatus(_K)
class _CpqHoSWRunningEventTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoSWRunningEventTime_Type.__name__=_L
_CpqHoSWRunningEventTime_Object=MibTableColumn
cpqHoSWRunningEventTime=_CpqHoSWRunningEventTime_Object((1,3,6,1,4,1,232,11,2,6,1,1,11),_CpqHoSWRunningEventTime_Type())
cpqHoSWRunningEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningEventTime.setStatus(_K)
class _CpqHoSWRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_O,1),('normal',2),('warning',3),('minor',4),('major',5),('critical',6),(_g,7)))
_CpqHoSWRunningStatus_Type.__name__=_E
_CpqHoSWRunningStatus_Object=MibTableColumn
cpqHoSWRunningStatus=_CpqHoSWRunningStatus_Object((1,3,6,1,4,1,232,11,2,6,1,1,12),_CpqHoSWRunningStatus_Type())
cpqHoSWRunningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningStatus.setStatus(_K)
class _CpqHoSWRunningConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('starting',2),('initialized',3),('configured',4),('operational',5)))
_CpqHoSWRunningConfigStatus_Type.__name__=_E
_CpqHoSWRunningConfigStatus_Object=MibTableColumn
cpqHoSWRunningConfigStatus=_CpqHoSWRunningConfigStatus_Object((1,3,6,1,4,1,232,11,2,6,1,1,13),_CpqHoSWRunningConfigStatus_Type())
cpqHoSWRunningConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningConfigStatus.setStatus(_K)
class _CpqHoSWRunningIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSWRunningIdentifier_Type.__name__=_D
_CpqHoSWRunningIdentifier_Object=MibTableColumn
cpqHoSWRunningIdentifier=_CpqHoSWRunningIdentifier_Object((1,3,6,1,4,1,232,11,2,6,1,1,14),_CpqHoSWRunningIdentifier_Type())
cpqHoSWRunningIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningIdentifier.setStatus(_K)
class _CpqHoSWRunningRedundancyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('master',2),('backup',3),('slave',4)))
_CpqHoSWRunningRedundancyMode_Type.__name__=_E
_CpqHoSWRunningRedundancyMode_Object=MibTableColumn
cpqHoSWRunningRedundancyMode=_CpqHoSWRunningRedundancyMode_Object((1,3,6,1,4,1,232,11,2,6,1,1,15),_CpqHoSWRunningRedundancyMode_Type())
cpqHoSWRunningRedundancyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSWRunningRedundancyMode.setStatus(_K)
class _CpqHoSwRunningTrapDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSwRunningTrapDesc_Type.__name__=_D
_CpqHoSwRunningTrapDesc_Object=MibScalar
cpqHoSwRunningTrapDesc=_CpqHoSwRunningTrapDesc_Object((1,3,6,1,4,1,232,11,2,6,2),_CpqHoSwRunningTrapDesc_Type())
cpqHoSwRunningTrapDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwRunningTrapDesc.setStatus(_A)
_CpqHoSwVer_ObjectIdentity=ObjectIdentity
cpqHoSwVer=_CpqHoSwVer_ObjectIdentity((1,3,6,1,4,1,232,11,2,7))
_CpqHoSwVerNextIndex_Type=Integer32
_CpqHoSwVerNextIndex_Object=MibScalar
cpqHoSwVerNextIndex=_CpqHoSwVerNextIndex_Object((1,3,6,1,4,1,232,11,2,7,1),_CpqHoSwVerNextIndex_Type())
cpqHoSwVerNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerNextIndex.setStatus(_A)
_CpqHoSwVerTable_Object=MibTable
cpqHoSwVerTable=_CpqHoSwVerTable_Object((1,3,6,1,4,1,232,11,2,7,2))
if mibBuilder.loadTexts:cpqHoSwVerTable.setStatus(_A)
_CpqHoSwVerEntry_Object=MibTableRow
cpqHoSwVerEntry=_CpqHoSwVerEntry_Object((1,3,6,1,4,1,232,11,2,7,2,1))
cpqHoSwVerEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cpqHoSwVerEntry.setStatus(_A)
class _CpqHoSwVerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoSwVerIndex_Type.__name__=_E
_CpqHoSwVerIndex_Object=MibTableColumn
cpqHoSwVerIndex=_CpqHoSwVerIndex_Object((1,3,6,1,4,1,232,11,2,7,2,1,1),_CpqHoSwVerIndex_Type())
cpqHoSwVerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerIndex.setStatus(_A)
class _CpqHoSwVerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('loaded',2),('notloaded',3)))
_CpqHoSwVerStatus_Type.__name__=_E
_CpqHoSwVerStatus_Object=MibTableColumn
cpqHoSwVerStatus=_CpqHoSwVerStatus_Object((1,3,6,1,4,1,232,11,2,7,2,1,2),_CpqHoSwVerStatus_Type())
cpqHoSwVerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerStatus.setStatus(_A)
class _CpqHoSwVerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),('driver',2),('agent',3),('sysutil',4),('application',5),('keyfile',6),('firmware',7)))
_CpqHoSwVerType_Type.__name__=_E
_CpqHoSwVerType_Object=MibTableColumn
cpqHoSwVerType=_CpqHoSwVerType_Object((1,3,6,1,4,1,232,11,2,7,2,1,3),_CpqHoSwVerType_Type())
cpqHoSwVerType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSwVerType.setStatus(_A)
class _CpqHoSwVerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqHoSwVerName_Type.__name__=_D
_CpqHoSwVerName_Object=MibTableColumn
cpqHoSwVerName=_CpqHoSwVerName_Object((1,3,6,1,4,1,232,11,2,7,2,1,4),_CpqHoSwVerName_Type())
cpqHoSwVerName.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSwVerName.setStatus(_A)
class _CpqHoSwVerDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqHoSwVerDescription_Type.__name__=_D
_CpqHoSwVerDescription_Object=MibTableColumn
cpqHoSwVerDescription=_CpqHoSwVerDescription_Object((1,3,6,1,4,1,232,11,2,7,2,1,5),_CpqHoSwVerDescription_Type())
cpqHoSwVerDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSwVerDescription.setStatus(_A)
class _CpqHoSwVerDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoSwVerDate_Type.__name__=_L
_CpqHoSwVerDate_Object=MibTableColumn
cpqHoSwVerDate=_CpqHoSwVerDate_Object((1,3,6,1,4,1,232,11,2,7,2,1,6),_CpqHoSwVerDate_Type())
cpqHoSwVerDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerDate.setStatus(_A)
class _CpqHoSwVerLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoSwVerLocation_Type.__name__=_D
_CpqHoSwVerLocation_Object=MibTableColumn
cpqHoSwVerLocation=_CpqHoSwVerLocation_Object((1,3,6,1,4,1,232,11,2,7,2,1,7),_CpqHoSwVerLocation_Type())
cpqHoSwVerLocation.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoSwVerLocation.setStatus(_A)
class _CpqHoSwVerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqHoSwVerVersion_Type.__name__=_D
_CpqHoSwVerVersion_Object=MibTableColumn
cpqHoSwVerVersion=_CpqHoSwVerVersion_Object((1,3,6,1,4,1,232,11,2,7,2,1,8),_CpqHoSwVerVersion_Type())
cpqHoSwVerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerVersion.setStatus(_A)
class _CpqHoSwVerVersionBinary_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqHoSwVerVersionBinary_Type.__name__=_D
_CpqHoSwVerVersionBinary_Object=MibTableColumn
cpqHoSwVerVersionBinary=_CpqHoSwVerVersionBinary_Object((1,3,6,1,4,1,232,11,2,7,2,1,9),_CpqHoSwVerVersionBinary_Type())
cpqHoSwVerVersionBinary.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerVersionBinary.setStatus(_A)
class _CpqHoSwVerAgentsVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqHoSwVerAgentsVer_Type.__name__=_D
_CpqHoSwVerAgentsVer_Object=MibScalar
cpqHoSwVerAgentsVer=_CpqHoSwVerAgentsVer_Object((1,3,6,1,4,1,232,11,2,7,3),_CpqHoSwVerAgentsVer_Type())
cpqHoSwVerAgentsVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwVerAgentsVer.setStatus(_A)
_CpqHoGeneric_ObjectIdentity=ObjectIdentity
cpqHoGeneric=_CpqHoGeneric_ObjectIdentity((1,3,6,1,4,1,232,11,2,8))
class _CpqHoGenericData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CpqHoGenericData_Type.__name__=_D
_CpqHoGenericData_Object=MibScalar
cpqHoGenericData=_CpqHoGenericData_Object((1,3,6,1,4,1,232,11,2,8,1),_CpqHoGenericData_Type())
cpqHoGenericData.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoGenericData.setStatus(_A)
class _CpqHoCriticalSoftwareUpdateData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CpqHoCriticalSoftwareUpdateData_Type.__name__=_D
_CpqHoCriticalSoftwareUpdateData_Object=MibScalar
cpqHoCriticalSoftwareUpdateData=_CpqHoCriticalSoftwareUpdateData_Object((1,3,6,1,4,1,232,11,2,8,2),_CpqHoCriticalSoftwareUpdateData_Type())
cpqHoCriticalSoftwareUpdateData.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoCriticalSoftwareUpdateData.setStatus(_A)
_CpqHoSwPerf_ObjectIdentity=ObjectIdentity
cpqHoSwPerf=_CpqHoSwPerf_ObjectIdentity((1,3,6,1,4,1,232,11,2,9))
class _CpqHoSwPerfAppErrorDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CpqHoSwPerfAppErrorDesc_Type.__name__=_D
_CpqHoSwPerfAppErrorDesc_Object=MibScalar
cpqHoSwPerfAppErrorDesc=_CpqHoSwPerfAppErrorDesc_Object((1,3,6,1,4,1,232,11,2,9,1),_CpqHoSwPerfAppErrorDesc_Type())
cpqHoSwPerfAppErrorDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoSwPerfAppErrorDesc.setStatus(_A)
_CpqHoSystemStatus_ObjectIdentity=ObjectIdentity
cpqHoSystemStatus=_CpqHoSystemStatus_ObjectIdentity((1,3,6,1,4,1,232,11,2,10))
class _CpqHoMibStatusArray_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,256))
_CpqHoMibStatusArray_Type.__name__=_L
_CpqHoMibStatusArray_Object=MibScalar
cpqHoMibStatusArray=_CpqHoMibStatusArray_Object((1,3,6,1,4,1,232,11,2,10,1),_CpqHoMibStatusArray_Type())
cpqHoMibStatusArray.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMibStatusArray.setStatus(_A)
class _CpqHoConfigChangedDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoConfigChangedDate_Type.__name__=_L
_CpqHoConfigChangedDate_Object=MibScalar
cpqHoConfigChangedDate=_CpqHoConfigChangedDate_Object((1,3,6,1,4,1,232,11,2,10,2),_CpqHoConfigChangedDate_Type())
cpqHoConfigChangedDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoConfigChangedDate.setStatus(_A)
class _CpqHoGUID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,17))
_CpqHoGUID_Type.__name__=_L
_CpqHoGUID_Object=MibScalar
cpqHoGUID=_CpqHoGUID_Object((1,3,6,1,4,1,232,11,2,10,3),_CpqHoGUID_Type())
cpqHoGUID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoGUID.setStatus(_A)
_CpqHoCodeServer_Type=Integer32
_CpqHoCodeServer_Object=MibScalar
cpqHoCodeServer=_CpqHoCodeServer_Object((1,3,6,1,4,1,232,11,2,10,4),_CpqHoCodeServer_Type())
cpqHoCodeServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoCodeServer.setStatus(_A)
_CpqHoWebMgmtPort_Type=Integer32
_CpqHoWebMgmtPort_Object=MibScalar
cpqHoWebMgmtPort=_CpqHoWebMgmtPort_Object((1,3,6,1,4,1,232,11,2,10,5),_CpqHoWebMgmtPort_Type())
cpqHoWebMgmtPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoWebMgmtPort.setStatus(_A)
class _CpqHoGUIDCanonical_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,36))
_CpqHoGUIDCanonical_Type.__name__=_L
_CpqHoGUIDCanonical_Object=MibScalar
cpqHoGUIDCanonical=_CpqHoGUIDCanonical_Object((1,3,6,1,4,1,232,11,2,10,6),_CpqHoGUIDCanonical_Type())
cpqHoGUIDCanonical.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoGUIDCanonical.setStatus(_A)
class _CpqHoMibHealthStatusArray_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_CpqHoMibHealthStatusArray_Type.__name__=_L
_CpqHoMibHealthStatusArray_Object=MibScalar
cpqHoMibHealthStatusArray=_CpqHoMibHealthStatusArray_Object((1,3,6,1,4,1,232,11,2,10,7),_CpqHoMibHealthStatusArray_Type())
cpqHoMibHealthStatusArray.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoMibHealthStatusArray.setStatus(_A)
_CpqHoTrapInfo_ObjectIdentity=ObjectIdentity
cpqHoTrapInfo=_CpqHoTrapInfo_ObjectIdentity((1,3,6,1,4,1,232,11,2,11))
_CpqHoTrapFlags_Type=Integer32
_CpqHoTrapFlags_Object=MibScalar
cpqHoTrapFlags=_CpqHoTrapFlags_Object((1,3,6,1,4,1,232,11,2,11,1),_CpqHoTrapFlags_Type())
cpqHoTrapFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoTrapFlags.setStatus(_A)
_CpqHoClients_ObjectIdentity=ObjectIdentity
cpqHoClients=_CpqHoClients_ObjectIdentity((1,3,6,1,4,1,232,11,2,12))
class _CpqHoClientLastModified_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqHoClientLastModified_Type.__name__=_L
_CpqHoClientLastModified_Object=MibScalar
cpqHoClientLastModified=_CpqHoClientLastModified_Object((1,3,6,1,4,1,232,11,2,12,1),_CpqHoClientLastModified_Type())
cpqHoClientLastModified.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientLastModified.setStatus(_A)
class _CpqHoClientDelete_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqHoClientDelete_Type.__name__=_D
_CpqHoClientDelete_Object=MibScalar
cpqHoClientDelete=_CpqHoClientDelete_Object((1,3,6,1,4,1,232,11,2,12,2),_CpqHoClientDelete_Type())
cpqHoClientDelete.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqHoClientDelete.setStatus(_A)
_CpqHoClientTable_Object=MibTable
cpqHoClientTable=_CpqHoClientTable_Object((1,3,6,1,4,1,232,11,2,12,3))
if mibBuilder.loadTexts:cpqHoClientTable.setStatus(_A)
_CpqHoClientEntry_Object=MibTableRow
cpqHoClientEntry=_CpqHoClientEntry_Object((1,3,6,1,4,1,232,11,2,12,3,1))
cpqHoClientEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cpqHoClientEntry.setStatus(_A)
class _CpqHoClientIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqHoClientIndex_Type.__name__=_E
_CpqHoClientIndex_Object=MibTableColumn
cpqHoClientIndex=_CpqHoClientIndex_Object((1,3,6,1,4,1,232,11,2,12,3,1,1),_CpqHoClientIndex_Type())
cpqHoClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIndex.setStatus(_A)
class _CpqHoClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqHoClientName_Type.__name__=_D
_CpqHoClientName_Object=MibTableColumn
cpqHoClientName=_CpqHoClientName_Object((1,3,6,1,4,1,232,11,2,12,3,1,2),_CpqHoClientName_Type())
cpqHoClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientName.setStatus(_A)
class _CpqHoClientIpxAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_CpqHoClientIpxAddress_Type.__name__=_L
_CpqHoClientIpxAddress_Object=MibTableColumn
cpqHoClientIpxAddress=_CpqHoClientIpxAddress_Object((1,3,6,1,4,1,232,11,2,12,3,1,3),_CpqHoClientIpxAddress_Type())
cpqHoClientIpxAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIpxAddress.setStatus(_A)
_CpqHoClientIpAddress_Type=IpAddress
_CpqHoClientIpAddress_Object=MibTableColumn
cpqHoClientIpAddress=_CpqHoClientIpAddress_Object((1,3,6,1,4,1,232,11,2,12,3,1,4),_CpqHoClientIpAddress_Type())
cpqHoClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientIpAddress.setStatus(_A)
class _CpqHoClientCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_CpqHoClientCommunity_Type.__name__=_D
_CpqHoClientCommunity_Object=MibTableColumn
cpqHoClientCommunity=_CpqHoClientCommunity_Object((1,3,6,1,4,1,232,11,2,12,3,1,5),_CpqHoClientCommunity_Type())
cpqHoClientCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientCommunity.setStatus(_A)
class _CpqHoClientID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_CpqHoClientID_Type.__name__=_L
_CpqHoClientID_Object=MibTableColumn
cpqHoClientID=_CpqHoClientID_Object((1,3,6,1,4,1,232,11,2,12,3,1,6),_CpqHoClientID_Type())
cpqHoClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoClientID.setStatus(_A)
_CpqHoMemory_ObjectIdentity=ObjectIdentity
cpqHoMemory=_CpqHoMemory_ObjectIdentity((1,3,6,1,4,1,232,11,2,13))
_CpqHoPhysicalMemorySize_Type=Integer32
_CpqHoPhysicalMemorySize_Object=MibScalar
cpqHoPhysicalMemorySize=_CpqHoPhysicalMemorySize_Object((1,3,6,1,4,1,232,11,2,13,1),_CpqHoPhysicalMemorySize_Type())
cpqHoPhysicalMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoPhysicalMemorySize.setStatus(_A)
_CpqHoPhysicalMemoryFree_Type=Integer32
_CpqHoPhysicalMemoryFree_Object=MibScalar
cpqHoPhysicalMemoryFree=_CpqHoPhysicalMemoryFree_Object((1,3,6,1,4,1,232,11,2,13,2),_CpqHoPhysicalMemoryFree_Type())
cpqHoPhysicalMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoPhysicalMemoryFree.setStatus(_A)
_CpqHoPagingMemorySize_Type=Integer32
_CpqHoPagingMemorySize_Object=MibScalar
cpqHoPagingMemorySize=_CpqHoPagingMemorySize_Object((1,3,6,1,4,1,232,11,2,13,3),_CpqHoPagingMemorySize_Type())
cpqHoPagingMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoPagingMemorySize.setStatus(_A)
_CpqHoPagingMemoryFree_Type=Integer32
_CpqHoPagingMemoryFree_Object=MibScalar
cpqHoPagingMemoryFree=_CpqHoPagingMemoryFree_Object((1,3,6,1,4,1,232,11,2,13,4),_CpqHoPagingMemoryFree_Type())
cpqHoPagingMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoPagingMemoryFree.setStatus(_A)
class _CpqHoBootPagingFileSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqHoBootPagingFileSize_Type.__name__=_D
_CpqHoBootPagingFileSize_Object=MibScalar
cpqHoBootPagingFileSize=_CpqHoBootPagingFileSize_Object((1,3,6,1,4,1,232,11,2,13,5),_CpqHoBootPagingFileSize_Type())
cpqHoBootPagingFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoBootPagingFileSize.setStatus(_A)
class _CpqHoBootPagingFileMinimumSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqHoBootPagingFileMinimumSize_Type.__name__=_D
_CpqHoBootPagingFileMinimumSize_Object=MibScalar
cpqHoBootPagingFileMinimumSize=_CpqHoBootPagingFileMinimumSize_Object((1,3,6,1,4,1,232,11,2,13,6),_CpqHoBootPagingFileMinimumSize_Type())
cpqHoBootPagingFileMinimumSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoBootPagingFileMinimumSize.setStatus(_A)
class _CpqHoBootPagingFileVolumeFreeSpace_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_CpqHoBootPagingFileVolumeFreeSpace_Type.__name__=_D
_CpqHoBootPagingFileVolumeFreeSpace_Object=MibScalar
cpqHoBootPagingFileVolumeFreeSpace=_CpqHoBootPagingFileVolumeFreeSpace_Object((1,3,6,1,4,1,232,11,2,13,7),_CpqHoBootPagingFileVolumeFreeSpace_Type())
cpqHoBootPagingFileVolumeFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoBootPagingFileVolumeFreeSpace.setStatus(_K)
_CpqHoFwVer_ObjectIdentity=ObjectIdentity
cpqHoFwVer=_CpqHoFwVer_ObjectIdentity((1,3,6,1,4,1,232,11,2,14))
_CpqHoFwVerTable_Object=MibTable
cpqHoFwVerTable=_CpqHoFwVerTable_Object((1,3,6,1,4,1,232,11,2,14,1))
if mibBuilder.loadTexts:cpqHoFwVerTable.setStatus(_A)
_CpqHoFwVerEntry_Object=MibTableRow
cpqHoFwVerEntry=_CpqHoFwVerEntry_Object((1,3,6,1,4,1,232,11,2,14,1,1))
cpqHoFwVerEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cpqHoFwVerEntry.setStatus(_A)
_CpqHoFwVerIndex_Type=Integer32
_CpqHoFwVerIndex_Object=MibTableColumn
cpqHoFwVerIndex=_CpqHoFwVerIndex_Object((1,3,6,1,4,1,232,11,2,14,1,1,1),_CpqHoFwVerIndex_Type())
cpqHoFwVerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerIndex.setStatus(_A)
class _CpqHoFwVerCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),('storage',2),('nic',3),('rib',4),('system',5)))
_CpqHoFwVerCategory_Type.__name__=_E
_CpqHoFwVerCategory_Object=MibTableColumn
cpqHoFwVerCategory=_CpqHoFwVerCategory_Object((1,3,6,1,4,1,232,11,2,14,1,1,2),_CpqHoFwVerCategory_Type())
cpqHoFwVerCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerCategory.setStatus(_A)
class _CpqHoFwVerDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*((_M,1),('internalArrayController',2),('fibreArrayController',3),('scsiController',4),('fibreChannelTapeController',5),('modularDataRouter',6),('ideCdRomDrive',7),('ideDiskDrive',8),('scsiCdRom-ScsiAttached',9),('scsiDiskDrive-ScsiAttached',10),('scsiTapeDrive-ScsiAttached',11),('scsiTapeLibrary-ScsiAttached',12),('scsiDiskDrive-ArrayAttached',13),('scsiTapeDrive-ArrayAttached',14),('scsiTapeLibrary-ArrayAttached',15),('scsiDiskDrive-FibreAttached',16),('scsiTapeDrive-FibreAttached',17),('scsiTapeLibrary-FibreAttached',18),('scsiEnclosureBackplaneRom-ScsiAttached',19),('scsiEnclosureBackplaneRom-ArrayAttached',20),('scsiEnclosureBackplaneRom-FibreAttached',21),('scsiEnclosureBackplaneRom-ra4x00',22),('systemRom',23),('networkInterfaceController',24),('remoteInsightBoard',25),('sasDiskDrive-SasAttached',26),('sataDiskDrive-SataAttached',27),('usbController',28),('sasControllerAdapter',29),('sataControllerAdapter',30),('systemDevice',31),('fibreChannelHba',32),('convergedNetworkAdapter',33),('ideController',34)))
_CpqHoFwVerDeviceType_Type.__name__=_E
_CpqHoFwVerDeviceType_Object=MibTableColumn
cpqHoFwVerDeviceType=_CpqHoFwVerDeviceType_Object((1,3,6,1,4,1,232,11,2,14,1,1,3),_CpqHoFwVerDeviceType_Type())
cpqHoFwVerDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerDeviceType.setStatus(_A)
class _CpqHoFwVerDisplayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqHoFwVerDisplayName_Type.__name__=_D
_CpqHoFwVerDisplayName_Object=MibTableColumn
cpqHoFwVerDisplayName=_CpqHoFwVerDisplayName_Object((1,3,6,1,4,1,232,11,2,14,1,1,4),_CpqHoFwVerDisplayName_Type())
cpqHoFwVerDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerDisplayName.setStatus(_A)
class _CpqHoFwVerVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CpqHoFwVerVersion_Type.__name__=_D
_CpqHoFwVerVersion_Object=MibTableColumn
cpqHoFwVerVersion=_CpqHoFwVerVersion_Object((1,3,6,1,4,1,232,11,2,14,1,1,5),_CpqHoFwVerVersion_Type())
cpqHoFwVerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerVersion.setStatus(_A)
class _CpqHoFwVerLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoFwVerLocation_Type.__name__=_D
_CpqHoFwVerLocation_Object=MibTableColumn
cpqHoFwVerLocation=_CpqHoFwVerLocation_Object((1,3,6,1,4,1,232,11,2,14,1,1,6),_CpqHoFwVerLocation_Type())
cpqHoFwVerLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerLocation.setStatus(_A)
class _CpqHoFwVerXmlString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqHoFwVerXmlString_Type.__name__=_D
_CpqHoFwVerXmlString_Object=MibTableColumn
cpqHoFwVerXmlString=_CpqHoFwVerXmlString_Object((1,3,6,1,4,1,232,11,2,14,1,1,7),_CpqHoFwVerXmlString_Type())
cpqHoFwVerXmlString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerXmlString.setStatus(_A)
class _CpqHoFwVerKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CpqHoFwVerKeyString_Type.__name__=_D
_CpqHoFwVerKeyString_Object=MibTableColumn
cpqHoFwVerKeyString=_CpqHoFwVerKeyString_Object((1,3,6,1,4,1,232,11,2,14,1,1,8),_CpqHoFwVerKeyString_Type())
cpqHoFwVerKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerKeyString.setStatus(_A)
class _CpqHoFwVerUpdateMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('noUpdate',2),('softwareflash',3),('replacePhysicalRom',4)))
_CpqHoFwVerUpdateMethod_Type.__name__=_E
_CpqHoFwVerUpdateMethod_Object=MibTableColumn
cpqHoFwVerUpdateMethod=_CpqHoFwVerUpdateMethod_Object((1,3,6,1,4,1,232,11,2,14,1,1,9),_CpqHoFwVerUpdateMethod_Type())
cpqHoFwVerUpdateMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoFwVerUpdateMethod.setStatus(_A)
_CpqHoHWInfo_ObjectIdentity=ObjectIdentity
cpqHoHWInfo=_CpqHoHWInfo_ObjectIdentity((1,3,6,1,4,1,232,11,2,15))
class _CpqHoHWInfoPlatform_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('cellular',2),('foundation',3),('virtualMachine',4),('serverBlade',5)))
_CpqHoHWInfoPlatform_Type.__name__=_E
_CpqHoHWInfoPlatform_Object=MibScalar
cpqHoHWInfoPlatform=_CpqHoHWInfoPlatform_Object((1,3,6,1,4,1,232,11,2,15,1),_CpqHoHWInfoPlatform_Type())
cpqHoHWInfoPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqHoHWInfoPlatform.setStatus(_K)
_CpqPwrThreshold_ObjectIdentity=ObjectIdentity
cpqPwrThreshold=_CpqPwrThreshold_ObjectIdentity((1,3,6,1,4,1,232,11,2,16))
class _CpqPwrWarnType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CpqPwrWarnType_Type.__name__=_D
_CpqPwrWarnType_Object=MibScalar
cpqPwrWarnType=_CpqPwrWarnType_Object((1,3,6,1,4,1,232,11,2,16,1),_CpqPwrWarnType_Type())
cpqPwrWarnType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqPwrWarnType.setStatus(_A)
_CpqPwrWarnThreshold_Type=Integer32
_CpqPwrWarnThreshold_Object=MibScalar
cpqPwrWarnThreshold=_CpqPwrWarnThreshold_Object((1,3,6,1,4,1,232,11,2,16,2),_CpqPwrWarnThreshold_Type())
cpqPwrWarnThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqPwrWarnThreshold.setStatus(_A)
_CpqPwrWarnDuration_Type=Integer32
_CpqPwrWarnDuration_Object=MibScalar
cpqPwrWarnDuration=_CpqPwrWarnDuration_Object((1,3,6,1,4,1,232,11,2,16,3),_CpqPwrWarnDuration_Type())
cpqPwrWarnDuration.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqPwrWarnDuration.setStatus(_A)
class _CpqSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CpqSerialNum_Type.__name__=_D
_CpqSerialNum_Object=MibScalar
cpqSerialNum=_CpqSerialNum_Object((1,3,6,1,4,1,232,11,2,16,4),_CpqSerialNum_Type())
cpqSerialNum.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqSerialNum.setStatus(_A)
class _CpqServerUUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_CpqServerUUID_Type.__name__=_D
_CpqServerUUID_Object=MibScalar
cpqServerUUID=_CpqServerUUID_Object((1,3,6,1,4,1,232,11,2,16,5),_CpqServerUUID_Type())
cpqServerUUID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpqServerUUID.setStatus(_A)
cpqHoGenericTrap=NotificationType((1,3,6,1,4,1,232,0,11001))
cpqHoGenericTrap.setObjects((_C,_V))
if mibBuilder.loadTexts:cpqHoGenericTrap.setStatus('')
cpqHoAppErrorTrap=NotificationType((1,3,6,1,4,1,232,0,11002))
cpqHoAppErrorTrap.setObjects((_C,_W))
if mibBuilder.loadTexts:cpqHoAppErrorTrap.setStatus('')
cpqHo2GenericTrap=NotificationType((1,3,6,1,4,1,232,0,11003))
cpqHo2GenericTrap.setObjects(*((_G,_H),(_C,_J),(_C,_V)))
if mibBuilder.loadTexts:cpqHo2GenericTrap.setStatus('')
cpqHo2AppErrorTrap=NotificationType((1,3,6,1,4,1,232,0,11004))
cpqHo2AppErrorTrap.setObjects(*((_G,_H),(_C,_J),(_C,_W)))
if mibBuilder.loadTexts:cpqHo2AppErrorTrap.setStatus('')
cpqHo2NicStatusOk=NotificationType((1,3,6,1,4,1,232,0,11005))
cpqHo2NicStatusOk.setObjects(*((_G,_H),(_C,_J),(_C,_N)))
if mibBuilder.loadTexts:cpqHo2NicStatusOk.setStatus('')
cpqHo2NicStatusFailed=NotificationType((1,3,6,1,4,1,232,0,11006))
cpqHo2NicStatusFailed.setObjects(*((_G,_H),(_C,_J),(_C,_N)))
if mibBuilder.loadTexts:cpqHo2NicStatusFailed.setStatus('')
cpqHo2NicSwitchoverOccurred=NotificationType((1,3,6,1,4,1,232,0,11007))
cpqHo2NicSwitchoverOccurred.setObjects(*((_G,_H),(_C,_J),(_C,_N),(_C,_N)))
if mibBuilder.loadTexts:cpqHo2NicSwitchoverOccurred.setStatus('')
cpqHo2NicStatusOk2=NotificationType((1,3,6,1,4,1,232,0,11008))
cpqHo2NicStatusOk2.setObjects(*((_G,_H),(_C,_J),(_C,_N),(_C,_S)))
if mibBuilder.loadTexts:cpqHo2NicStatusOk2.setStatus('')
cpqHo2NicStatusFailed2=NotificationType((1,3,6,1,4,1,232,0,11009))
cpqHo2NicStatusFailed2.setObjects(*((_G,_H),(_C,_J),(_C,_N),(_C,_S)))
if mibBuilder.loadTexts:cpqHo2NicStatusFailed2.setStatus('')
cpqHo2NicSwitchoverOccurred2=NotificationType((1,3,6,1,4,1,232,0,11010))
cpqHo2NicSwitchoverOccurred2.setObjects(*((_G,_H),(_C,_J),(_C,_N),(_C,_S),(_C,_N),(_C,_S)))
if mibBuilder.loadTexts:cpqHo2NicSwitchoverOccurred2.setStatus('')
cpqHoProcessEventTrap=NotificationType((1,3,6,1,4,1,232,0,11011))
cpqHoProcessEventTrap.setObjects(*((_G,_H),(_C,_J),(_C,_X)))
if mibBuilder.loadTexts:cpqHoProcessEventTrap.setStatus('')
cpqHoProcessCountWarning=NotificationType((1,3,6,1,4,1,232,0,11012))
cpqHoProcessCountWarning.setObjects(*((_G,_H),(_C,_J),(_C,_T),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b)))
if mibBuilder.loadTexts:cpqHoProcessCountWarning.setStatus('')
cpqHoProcessCountNormal=NotificationType((1,3,6,1,4,1,232,0,11013))
cpqHoProcessCountNormal.setObjects(*((_G,_H),(_C,_J),(_C,_T),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b)))
if mibBuilder.loadTexts:cpqHoProcessCountNormal.setStatus('')
cpqHoCriticalSoftwareUpdateTrap=NotificationType((1,3,6,1,4,1,232,0,11014))
cpqHoCriticalSoftwareUpdateTrap.setObjects(*((_G,_H),(_C,_J),(_C,_o)))
if mibBuilder.loadTexts:cpqHoCriticalSoftwareUpdateTrap.setStatus('')
cpqHoCrashDumpNotEnabledTrap=NotificationType((1,3,6,1,4,1,232,0,11015))
cpqHoCrashDumpNotEnabledTrap.setObjects(*((_G,_H),(_C,_J),(_C,_U)))
if mibBuilder.loadTexts:cpqHoCrashDumpNotEnabledTrap.setStatus('')
cpqHoBootPagingFileTooSmallTrap=NotificationType((1,3,6,1,4,1,232,0,11016))
cpqHoBootPagingFileTooSmallTrap.setObjects(*((_G,_H),(_C,_J),(_C,_U),(_C,_c),(_C,_d)))
if mibBuilder.loadTexts:cpqHoBootPagingFileTooSmallTrap.setStatus('')
cpqHoSWRunningStatusChangeTrap=NotificationType((1,3,6,1,4,1,232,0,11017))
cpqHoSWRunningStatusChangeTrap.setObjects(*((_G,_H),(_C,_J),(_C,_T),(_C,_p),(_C,_X),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u)))
if mibBuilder.loadTexts:cpqHoSWRunningStatusChangeTrap.setStatus('')
cpqHo2PowerThresholdTrap=NotificationType((1,3,6,1,4,1,232,0,11018))
cpqHo2PowerThresholdTrap.setObjects(*((_G,_H),(_C,_J),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z)))
if mibBuilder.loadTexts:cpqHo2PowerThresholdTrap.setStatus('')
cpqHoBootPagingFileOrFreeSpaceTooSmallTrap=NotificationType((1,3,6,1,4,1,232,0,11019))
cpqHoBootPagingFileOrFreeSpaceTooSmallTrap.setObjects(*((_G,_H),(_C,_J),(_C,_U),(_C,_c),(_C,_A0),(_C,_d)))
if mibBuilder.loadTexts:cpqHoBootPagingFileOrFreeSpaceTooSmallTrap.setStatus('')
cpqHoMibHealthStatusArrayChangeTrap=NotificationType((1,3,6,1,4,1,232,0,11020))
cpqHoMibHealthStatusArrayChangeTrap.setObjects(*((_G,_H),(_C,_J),(_C,_A1)))
if mibBuilder.loadTexts:cpqHoMibHealthStatusArrayChangeTrap.setStatus('')
mibBuilder.exportSymbols(_C,**{'compaq':compaq,'cpqHoGenericTrap':cpqHoGenericTrap,'cpqHoAppErrorTrap':cpqHoAppErrorTrap,'cpqHo2GenericTrap':cpqHo2GenericTrap,'cpqHo2AppErrorTrap':cpqHo2AppErrorTrap,'cpqHo2NicStatusOk':cpqHo2NicStatusOk,'cpqHo2NicStatusFailed':cpqHo2NicStatusFailed,'cpqHo2NicSwitchoverOccurred':cpqHo2NicSwitchoverOccurred,'cpqHo2NicStatusOk2':cpqHo2NicStatusOk2,'cpqHo2NicStatusFailed2':cpqHo2NicStatusFailed2,'cpqHo2NicSwitchoverOccurred2':cpqHo2NicSwitchoverOccurred2,'cpqHoProcessEventTrap':cpqHoProcessEventTrap,'cpqHoProcessCountWarning':cpqHoProcessCountWarning,'cpqHoProcessCountNormal':cpqHoProcessCountNormal,'cpqHoCriticalSoftwareUpdateTrap':cpqHoCriticalSoftwareUpdateTrap,'cpqHoCrashDumpNotEnabledTrap':cpqHoCrashDumpNotEnabledTrap,'cpqHoBootPagingFileTooSmallTrap':cpqHoBootPagingFileTooSmallTrap,'cpqHoSWRunningStatusChangeTrap':cpqHoSWRunningStatusChangeTrap,'cpqHo2PowerThresholdTrap':cpqHo2PowerThresholdTrap,'cpqHoBootPagingFileOrFreeSpaceTooSmallTrap':cpqHoBootPagingFileOrFreeSpaceTooSmallTrap,'cpqHoMibHealthStatusArrayChangeTrap':cpqHoMibHealthStatusArrayChangeTrap,'cpqHostOs':cpqHostOs,'cpqHoMibRev':cpqHoMibRev,'cpqHoMibRevMajor':cpqHoMibRevMajor,'cpqHoMibRevMinor':cpqHoMibRevMinor,'cpqHoMibCondition':cpqHoMibCondition,'cpqHoComponent':cpqHoComponent,'cpqHoInterface':cpqHoInterface,'cpqHoOsCommon':cpqHoOsCommon,'cpqHoOsCommonPollFreq':cpqHoOsCommonPollFreq,'cpqHoOsCommonModuleTable':cpqHoOsCommonModuleTable,'cpqHoOsCommonModuleEntry':cpqHoOsCommonModuleEntry,_f:cpqHoOsCommonModuleIndex,'cpqHoOsCommonModuleName':cpqHoOsCommonModuleName,'cpqHoOsCommonModuleVersion':cpqHoOsCommonModuleVersion,'cpqHoOsCommonModuleDate':cpqHoOsCommonModuleDate,'cpqHoOsCommonModulePurpose':cpqHoOsCommonModulePurpose,'cpqHoInfo':cpqHoInfo,'cpqHoName':cpqHoName,'cpqHoVersion':cpqHoVersion,'cpqHoDesc':cpqHoDesc,'cpqHoOsType':cpqHoOsType,'cpqHoTelnet':cpqHoTelnet,'cpqHoSystemRole':cpqHoSystemRole,'cpqHoSystemRoleDetail':cpqHoSystemRoleDetail,_U:cpqHoCrashDumpState,'cpqHoCrashDumpCondition':cpqHoCrashDumpCondition,'cpqHoCrashDumpMonitoring':cpqHoCrashDumpMonitoring,'cpqHoMaxLogicalCPUSupported':cpqHoMaxLogicalCPUSupported,'cpqHoSystemName':cpqHoSystemName,'cpqHosysDescr':cpqHosysDescr,'cpqHoUtil':cpqHoUtil,'cpqHoCpuUtilTable':cpqHoCpuUtilTable,'cpqHoCpuUtilEntry':cpqHoCpuUtilEntry,_h:cpqHoCpuUtilUnitIndex,'cpqHoCpuUtilMin':cpqHoCpuUtilMin,'cpqHoCpuUtilFiveMin':cpqHoCpuUtilFiveMin,'cpqHoCpuUtilThirtyMin':cpqHoCpuUtilThirtyMin,'cpqHoCpuUtilHour':cpqHoCpuUtilHour,'cpqHoCpuUtilHwLocation':cpqHoCpuUtilHwLocation,'cpqHoFileSys':cpqHoFileSys,'cpqHoFileSysTable':cpqHoFileSysTable,'cpqHoFileSysEntry':cpqHoFileSysEntry,_i:cpqHoFileSysIndex,'cpqHoFileSysDesc':cpqHoFileSysDesc,'cpqHoFileSysSpaceTotal':cpqHoFileSysSpaceTotal,'cpqHoFileSysSpaceUsed':cpqHoFileSysSpaceUsed,'cpqHoFileSysPercentSpaceUsed':cpqHoFileSysPercentSpaceUsed,'cpqHoFileSysAllocUnitsTotal':cpqHoFileSysAllocUnitsTotal,'cpqHoFileSysAllocUnitsUsed':cpqHoFileSysAllocUnitsUsed,'cpqHoFileSysStatus':cpqHoFileSysStatus,'cpqHoFileSysShortDesc':cpqHoFileSysShortDesc,'cpqHoFileSysCondition':cpqHoFileSysCondition,'cpqHoIfPhysMap':cpqHoIfPhysMap,'cpqHoIfPhysMapTable':cpqHoIfPhysMapTable,'cpqHoIfPhysMapEntry':cpqHoIfPhysMapEntry,_j:cpqHoIfPhysMapIndex,_N:cpqHoIfPhysMapSlot,'cpqHoIfPhysMapIoBaseAddr':cpqHoIfPhysMapIoBaseAddr,'cpqHoIfPhysMapIrq':cpqHoIfPhysMapIrq,'cpqHoIfPhysMapDma':cpqHoIfPhysMapDma,'cpqHoIfPhysMapMemBaseAddr':cpqHoIfPhysMapMemBaseAddr,_S:cpqHoIfPhysMapPort,'cpqHoIfPhysMapDuplexState':cpqHoIfPhysMapDuplexState,'cpqHoIfPhysMapCondition':cpqHoIfPhysMapCondition,'cpqHoIfPhysMapOverallCondition':cpqHoIfPhysMapOverallCondition,'cpqHoSWRunning':cpqHoSWRunning,'cpqHoSWRunningTable':cpqHoSWRunningTable,'cpqHoSWRunningEntry':cpqHoSWRunningEntry,_k:cpqHoSWRunningIndex,_T:cpqHoSWRunningName,_p:cpqHoSWRunningDesc,_q:cpqHoSWRunningVersion,'cpqHoSWRunningDate':cpqHoSWRunningDate,'cpqHoSWRunningMonitor':cpqHoSWRunningMonitor,'cpqHoSWRunningState':cpqHoSWRunningState,_Y:cpqHoSWRunningCount,_Z:cpqHoSWRunningCountMin,_a:cpqHoSWRunningCountMax,_b:cpqHoSWRunningEventTime,_r:cpqHoSWRunningStatus,_s:cpqHoSWRunningConfigStatus,_t:cpqHoSWRunningIdentifier,_u:cpqHoSWRunningRedundancyMode,_X:cpqHoSwRunningTrapDesc,'cpqHoSwVer':cpqHoSwVer,'cpqHoSwVerNextIndex':cpqHoSwVerNextIndex,'cpqHoSwVerTable':cpqHoSwVerTable,'cpqHoSwVerEntry':cpqHoSwVerEntry,_l:cpqHoSwVerIndex,'cpqHoSwVerStatus':cpqHoSwVerStatus,'cpqHoSwVerType':cpqHoSwVerType,'cpqHoSwVerName':cpqHoSwVerName,'cpqHoSwVerDescription':cpqHoSwVerDescription,'cpqHoSwVerDate':cpqHoSwVerDate,'cpqHoSwVerLocation':cpqHoSwVerLocation,'cpqHoSwVerVersion':cpqHoSwVerVersion,'cpqHoSwVerVersionBinary':cpqHoSwVerVersionBinary,'cpqHoSwVerAgentsVer':cpqHoSwVerAgentsVer,'cpqHoGeneric':cpqHoGeneric,_V:cpqHoGenericData,_o:cpqHoCriticalSoftwareUpdateData,'cpqHoSwPerf':cpqHoSwPerf,_W:cpqHoSwPerfAppErrorDesc,'cpqHoSystemStatus':cpqHoSystemStatus,'cpqHoMibStatusArray':cpqHoMibStatusArray,'cpqHoConfigChangedDate':cpqHoConfigChangedDate,'cpqHoGUID':cpqHoGUID,'cpqHoCodeServer':cpqHoCodeServer,'cpqHoWebMgmtPort':cpqHoWebMgmtPort,'cpqHoGUIDCanonical':cpqHoGUIDCanonical,_A1:cpqHoMibHealthStatusArray,'cpqHoTrapInfo':cpqHoTrapInfo,_J:cpqHoTrapFlags,'cpqHoClients':cpqHoClients,'cpqHoClientLastModified':cpqHoClientLastModified,'cpqHoClientDelete':cpqHoClientDelete,'cpqHoClientTable':cpqHoClientTable,'cpqHoClientEntry':cpqHoClientEntry,_m:cpqHoClientIndex,'cpqHoClientName':cpqHoClientName,'cpqHoClientIpxAddress':cpqHoClientIpxAddress,'cpqHoClientIpAddress':cpqHoClientIpAddress,'cpqHoClientCommunity':cpqHoClientCommunity,'cpqHoClientID':cpqHoClientID,'cpqHoMemory':cpqHoMemory,'cpqHoPhysicalMemorySize':cpqHoPhysicalMemorySize,'cpqHoPhysicalMemoryFree':cpqHoPhysicalMemoryFree,'cpqHoPagingMemorySize':cpqHoPagingMemorySize,'cpqHoPagingMemoryFree':cpqHoPagingMemoryFree,_c:cpqHoBootPagingFileSize,_d:cpqHoBootPagingFileMinimumSize,_A0:cpqHoBootPagingFileVolumeFreeSpace,'cpqHoFwVer':cpqHoFwVer,'cpqHoFwVerTable':cpqHoFwVerTable,'cpqHoFwVerEntry':cpqHoFwVerEntry,_n:cpqHoFwVerIndex,'cpqHoFwVerCategory':cpqHoFwVerCategory,'cpqHoFwVerDeviceType':cpqHoFwVerDeviceType,'cpqHoFwVerDisplayName':cpqHoFwVerDisplayName,'cpqHoFwVerVersion':cpqHoFwVerVersion,'cpqHoFwVerLocation':cpqHoFwVerLocation,'cpqHoFwVerXmlString':cpqHoFwVerXmlString,'cpqHoFwVerKeyString':cpqHoFwVerKeyString,'cpqHoFwVerUpdateMethod':cpqHoFwVerUpdateMethod,'cpqHoHWInfo':cpqHoHWInfo,'cpqHoHWInfoPlatform':cpqHoHWInfoPlatform,'cpqPwrThreshold':cpqPwrThreshold,_v:cpqPwrWarnType,_w:cpqPwrWarnThreshold,_x:cpqPwrWarnDuration,_y:cpqSerialNum,_z:cpqServerUUID})