_A1='cpqIdeAtaEraseFailureType'
_A0='cpqIdeLogicalDriveStatus'
_z='cpqIdeControllerSlot'
_y='cpqIdeControllerModel'
_x='cpqIdeAtapiDeviceIndex'
_w='cpqIdeAtapiDeviceControllerIndex'
_v='device1'
_u='device0'
_t='channel1'
_s='channel0'
_r='ssdWearOut'
_q='optional'
_p='cpqIdeControllerIndex'
_o='removableDisk'
_n='commDev'
_m='jukeBox'
_l='optical'
_k='scanner'
_j='cd-rom'
_i='wormDrive'
_h='processor'
_g='printer'
_f='cpqIdeOsCommonModuleIndex'
_e='NotificationType'
_d='cpqIdeAtaDiskLocation'
_c='cpqIdeAtaDiskSSDWearStatus'
_b='cpqIdeAtaDiskNumber'
_a='cpqIdeAtaDiskStatus'
_Z='cpqIdeLogicalDriveIndex'
_Y='cpqIdeLogicalDriveControllerIndex'
_X='false'
_W='true'
_V='OctetString'
_U='cpqIdeAtaDiskChannel'
_T='cpqIdeAtaDiskFwRev'
_S='cpqIdeAtaDiskModel'
_R='cpqIdeIdentIndex'
_Q='cpqIdeAtaDiskSerialNumber'
_P='cpqIdeAtaDiskIndex'
_O='cpqIdeAtaDiskControllerIndex'
_N='deprecated'
_M='degraded'
_L='failed'
_K='sysName'
_J='SNMPv2-MIB'
_I='cpqHoTrapFlags'
_H='CPQHOST-MIB'
_G='DisplayString'
_F='ok'
_E='other'
_D='Integer32'
_C='CPQIDE-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_H,'compaq',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_e,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_e,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_CpqIde_ObjectIdentity=ObjectIdentity
cpqIde=_CpqIde_ObjectIdentity((1,3,6,1,4,1,232,14))
_CpqIdeMibRev_ObjectIdentity=ObjectIdentity
cpqIdeMibRev=_CpqIdeMibRev_ObjectIdentity((1,3,6,1,4,1,232,14,1))
class _CpqIdeMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqIdeMibRevMajor_Type.__name__=_D
_CpqIdeMibRevMajor_Object=MibScalar
cpqIdeMibRevMajor=_CpqIdeMibRevMajor_Object((1,3,6,1,4,1,232,14,1,1),_CpqIdeMibRevMajor_Type())
cpqIdeMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeMibRevMajor.setStatus(_A)
class _CpqIdeMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIdeMibRevMinor_Type.__name__=_D
_CpqIdeMibRevMinor_Object=MibScalar
cpqIdeMibRevMinor=_CpqIdeMibRevMinor_Object((1,3,6,1,4,1,232,14,1,2),_CpqIdeMibRevMinor_Type())
cpqIdeMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeMibRevMinor.setStatus(_A)
class _CpqIdeMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeMibCondition_Type.__name__=_D
_CpqIdeMibCondition_Object=MibScalar
cpqIdeMibCondition=_CpqIdeMibCondition_Object((1,3,6,1,4,1,232,14,1,3),_CpqIdeMibCondition_Type())
cpqIdeMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeMibCondition.setStatus(_A)
_CpqIdeComponent_ObjectIdentity=ObjectIdentity
cpqIdeComponent=_CpqIdeComponent_ObjectIdentity((1,3,6,1,4,1,232,14,2))
_CpqIdeInterface_ObjectIdentity=ObjectIdentity
cpqIdeInterface=_CpqIdeInterface_ObjectIdentity((1,3,6,1,4,1,232,14,2,1))
_CpqIdeOsCommon_ObjectIdentity=ObjectIdentity
cpqIdeOsCommon=_CpqIdeOsCommon_ObjectIdentity((1,3,6,1,4,1,232,14,2,1,4))
class _CpqIdeOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIdeOsCommonPollFreq_Type.__name__=_D
_CpqIdeOsCommonPollFreq_Object=MibScalar
cpqIdeOsCommonPollFreq=_CpqIdeOsCommonPollFreq_Object((1,3,6,1,4,1,232,14,2,1,4,1),_CpqIdeOsCommonPollFreq_Type())
cpqIdeOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqIdeOsCommonPollFreq.setStatus(_A)
_CpqIdeOsCommonModuleTable_Object=MibTable
cpqIdeOsCommonModuleTable=_CpqIdeOsCommonModuleTable_Object((1,3,6,1,4,1,232,14,2,1,4,2))
if mibBuilder.loadTexts:cpqIdeOsCommonModuleTable.setStatus(_N)
_CpqIdeOsCommonModuleEntry_Object=MibTableRow
cpqIdeOsCommonModuleEntry=_CpqIdeOsCommonModuleEntry_Object((1,3,6,1,4,1,232,14,2,1,4,2,1))
cpqIdeOsCommonModuleEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cpqIdeOsCommonModuleEntry.setStatus(_N)
class _CpqIdeOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqIdeOsCommonModuleIndex_Type.__name__=_D
_CpqIdeOsCommonModuleIndex_Object=MibTableColumn
cpqIdeOsCommonModuleIndex=_CpqIdeOsCommonModuleIndex_Object((1,3,6,1,4,1,232,14,2,1,4,2,1,1),_CpqIdeOsCommonModuleIndex_Type())
cpqIdeOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeOsCommonModuleIndex.setStatus(_N)
class _CpqIdeOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeOsCommonModuleName_Type.__name__=_G
_CpqIdeOsCommonModuleName_Object=MibTableColumn
cpqIdeOsCommonModuleName=_CpqIdeOsCommonModuleName_Object((1,3,6,1,4,1,232,14,2,1,4,2,1,2),_CpqIdeOsCommonModuleName_Type())
cpqIdeOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeOsCommonModuleName.setStatus(_N)
class _CpqIdeOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqIdeOsCommonModuleVersion_Type.__name__=_G
_CpqIdeOsCommonModuleVersion_Object=MibTableColumn
cpqIdeOsCommonModuleVersion=_CpqIdeOsCommonModuleVersion_Object((1,3,6,1,4,1,232,14,2,1,4,2,1,3),_CpqIdeOsCommonModuleVersion_Type())
cpqIdeOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeOsCommonModuleVersion.setStatus(_N)
class _CpqIdeOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqIdeOsCommonModuleDate_Type.__name__=_V
_CpqIdeOsCommonModuleDate_Object=MibTableColumn
cpqIdeOsCommonModuleDate=_CpqIdeOsCommonModuleDate_Object((1,3,6,1,4,1,232,14,2,1,4,2,1,4),_CpqIdeOsCommonModuleDate_Type())
cpqIdeOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeOsCommonModuleDate.setStatus(_N)
class _CpqIdeOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeOsCommonModulePurpose_Type.__name__=_G
_CpqIdeOsCommonModulePurpose_Object=MibTableColumn
cpqIdeOsCommonModulePurpose=_CpqIdeOsCommonModulePurpose_Object((1,3,6,1,4,1,232,14,2,1,4,2,1,5),_CpqIdeOsCommonModulePurpose_Type())
cpqIdeOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeOsCommonModulePurpose.setStatus(_N)
_CpqIdeIdent_ObjectIdentity=ObjectIdentity
cpqIdeIdent=_CpqIdeIdent_ObjectIdentity((1,3,6,1,4,1,232,14,2,2))
_CpqIdeIdentTable_Object=MibTable
cpqIdeIdentTable=_CpqIdeIdentTable_Object((1,3,6,1,4,1,232,14,2,2,1))
if mibBuilder.loadTexts:cpqIdeIdentTable.setStatus(_A)
_CpqIdeIdentEntry_Object=MibTableRow
cpqIdeIdentEntry=_CpqIdeIdentEntry_Object((1,3,6,1,4,1,232,14,2,2,1,1))
cpqIdeIdentEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cpqIdeIdentEntry.setStatus(_A)
class _CpqIdeIdentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIdeIdentIndex_Type.__name__=_D
_CpqIdeIdentIndex_Object=MibTableColumn
cpqIdeIdentIndex=_CpqIdeIdentIndex_Object((1,3,6,1,4,1,232,14,2,2,1,1,1),_CpqIdeIdentIndex_Type())
cpqIdeIdentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentIndex.setStatus(_A)
class _CpqIdeIdentModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,41))
_CpqIdeIdentModel_Type.__name__=_G
_CpqIdeIdentModel_Object=MibTableColumn
cpqIdeIdentModel=_CpqIdeIdentModel_Object((1,3,6,1,4,1,232,14,2,2,1,1,2),_CpqIdeIdentModel_Type())
cpqIdeIdentModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentModel.setStatus(_A)
class _CpqIdeIdentSerNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,21))
_CpqIdeIdentSerNum_Type.__name__=_G
_CpqIdeIdentSerNum_Object=MibTableColumn
cpqIdeIdentSerNum=_CpqIdeIdentSerNum_Object((1,3,6,1,4,1,232,14,2,2,1,1,3),_CpqIdeIdentSerNum_Type())
cpqIdeIdentSerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentSerNum.setStatus(_A)
class _CpqIdeIdentFWVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqIdeIdentFWVers_Type.__name__=_G
_CpqIdeIdentFWVers_Object=MibTableColumn
cpqIdeIdentFWVers=_CpqIdeIdentFWVers_Object((1,3,6,1,4,1,232,14,2,2,1,1,4),_CpqIdeIdentFWVers_Type())
cpqIdeIdentFWVers.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentFWVers.setStatus(_A)
class _CpqIdeIdentCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeIdentCondition_Type.__name__=_D
_CpqIdeIdentCondition_Object=MibTableColumn
cpqIdeIdentCondition=_CpqIdeIdentCondition_Object((1,3,6,1,4,1,232,14,2,2,1,1,5),_CpqIdeIdentCondition_Type())
cpqIdeIdentCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentCondition.setStatus(_N)
class _CpqIdeIdentErrorNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqIdeIdentErrorNumber_Type.__name__=_G
_CpqIdeIdentErrorNumber_Object=MibTableColumn
cpqIdeIdentErrorNumber=_CpqIdeIdentErrorNumber_Object((1,3,6,1,4,1,232,14,2,2,1,1,6),_CpqIdeIdentErrorNumber_Type())
cpqIdeIdentErrorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentErrorNumber.setStatus(_A)
class _CpqIdeIdentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),('disk',2),('tape',3),(_g,4),(_h,5),(_i,6),(_j,7),(_k,8),(_l,9),(_m,10),(_n,11)))
_CpqIdeIdentType_Type.__name__=_D
_CpqIdeIdentType_Object=MibTableColumn
cpqIdeIdentType=_CpqIdeIdentType_Object((1,3,6,1,4,1,232,14,2,2,1,1,7),_CpqIdeIdentType_Type())
cpqIdeIdentType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentType.setStatus(_A)
class _CpqIdeIdentTypeExtended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('pdcd',2),(_o,3)))
_CpqIdeIdentTypeExtended_Type.__name__=_D
_CpqIdeIdentTypeExtended_Object=MibTableColumn
cpqIdeIdentTypeExtended=_CpqIdeIdentTypeExtended_Object((1,3,6,1,4,1,232,14,2,2,1,1,8),_CpqIdeIdentTypeExtended_Type())
cpqIdeIdentTypeExtended.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentTypeExtended.setStatus(_A)
class _CpqIdeIdentCondition2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeIdentCondition2_Type.__name__=_D
_CpqIdeIdentCondition2_Object=MibTableColumn
cpqIdeIdentCondition2=_CpqIdeIdentCondition2_Object((1,3,6,1,4,1,232,14,2,2,1,1,9),_CpqIdeIdentCondition2_Type())
cpqIdeIdentCondition2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentCondition2.setStatus(_A)
class _CpqIdeIdentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),('preFailureDegraded',3),('ultraAtaDegraded',4)))
_CpqIdeIdentStatus_Type.__name__=_D
_CpqIdeIdentStatus_Object=MibTableColumn
cpqIdeIdentStatus=_CpqIdeIdentStatus_Object((1,3,6,1,4,1,232,14,2,2,1,1,10),_CpqIdeIdentStatus_Type())
cpqIdeIdentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentStatus.setStatus(_A)
class _CpqIdeIdentUltraAtaAvailability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('noNotSupportedByDeviceAndController',2),('noNotSupportedByDevice',3),('noNotSupportedByController',4),('noDisabledInSetup',5),('yesEnabledInSetup',6)))
_CpqIdeIdentUltraAtaAvailability_Type.__name__=_D
_CpqIdeIdentUltraAtaAvailability_Object=MibTableColumn
cpqIdeIdentUltraAtaAvailability=_CpqIdeIdentUltraAtaAvailability_Object((1,3,6,1,4,1,232,14,2,2,1,1,11),_CpqIdeIdentUltraAtaAvailability_Type())
cpqIdeIdentUltraAtaAvailability.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeIdentUltraAtaAvailability.setStatus(_A)
_CpqIdeController_ObjectIdentity=ObjectIdentity
cpqIdeController=_CpqIdeController_ObjectIdentity((1,3,6,1,4,1,232,14,2,3))
_CpqIdeControllerTable_Object=MibTable
cpqIdeControllerTable=_CpqIdeControllerTable_Object((1,3,6,1,4,1,232,14,2,3,1))
if mibBuilder.loadTexts:cpqIdeControllerTable.setStatus(_A)
_CpqIdeControllerEntry_Object=MibTableRow
cpqIdeControllerEntry=_CpqIdeControllerEntry_Object((1,3,6,1,4,1,232,14,2,3,1,1))
cpqIdeControllerEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:cpqIdeControllerEntry.setStatus(_A)
_CpqIdeControllerIndex_Type=Integer32
_CpqIdeControllerIndex_Object=MibTableColumn
cpqIdeControllerIndex=_CpqIdeControllerIndex_Object((1,3,6,1,4,1,232,14,2,3,1,1,1),_CpqIdeControllerIndex_Type())
cpqIdeControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerIndex.setStatus(_A)
class _CpqIdeControllerOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeControllerOverallCondition_Type.__name__=_D
_CpqIdeControllerOverallCondition_Object=MibTableColumn
cpqIdeControllerOverallCondition=_CpqIdeControllerOverallCondition_Object((1,3,6,1,4,1,232,14,2,3,1,1,2),_CpqIdeControllerOverallCondition_Type())
cpqIdeControllerOverallCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerOverallCondition.setStatus(_A)
_CpqIdeControllerModel_Type=DisplayString
_CpqIdeControllerModel_Object=MibTableColumn
cpqIdeControllerModel=_CpqIdeControllerModel_Object((1,3,6,1,4,1,232,14,2,3,1,1,3),_CpqIdeControllerModel_Type())
cpqIdeControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerModel.setStatus(_A)
_CpqIdeControllerFwRev_Type=DisplayString
_CpqIdeControllerFwRev_Object=MibTableColumn
cpqIdeControllerFwRev=_CpqIdeControllerFwRev_Object((1,3,6,1,4,1,232,14,2,3,1,1,4),_CpqIdeControllerFwRev_Type())
cpqIdeControllerFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerFwRev.setStatus(_A)
_CpqIdeControllerSlot_Type=Integer32
_CpqIdeControllerSlot_Object=MibTableColumn
cpqIdeControllerSlot=_CpqIdeControllerSlot_Object((1,3,6,1,4,1,232,14,2,3,1,1,5),_CpqIdeControllerSlot_Type())
cpqIdeControllerSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerSlot.setStatus(_A)
class _CpqIdeControllerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_L,3)))
_CpqIdeControllerStatus_Type.__name__=_D
_CpqIdeControllerStatus_Object=MibTableColumn
cpqIdeControllerStatus=_CpqIdeControllerStatus_Object((1,3,6,1,4,1,232,14,2,3,1,1,6),_CpqIdeControllerStatus_Type())
cpqIdeControllerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerStatus.setStatus(_A)
class _CpqIdeControllerCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeControllerCondition_Type.__name__=_D
_CpqIdeControllerCondition_Object=MibTableColumn
cpqIdeControllerCondition=_CpqIdeControllerCondition_Object((1,3,6,1,4,1,232,14,2,3,1,1,7),_CpqIdeControllerCondition_Type())
cpqIdeControllerCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerCondition.setStatus(_A)
_CpqIdeControllerSerialNumber_Type=DisplayString
_CpqIdeControllerSerialNumber_Object=MibTableColumn
cpqIdeControllerSerialNumber=_CpqIdeControllerSerialNumber_Object((1,3,6,1,4,1,232,14,2,3,1,1,8),_CpqIdeControllerSerialNumber_Type())
cpqIdeControllerSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerSerialNumber.setStatus(_A)
_CpqIdeControllerHwLocation_Type=DisplayString
_CpqIdeControllerHwLocation_Object=MibTableColumn
cpqIdeControllerHwLocation=_CpqIdeControllerHwLocation_Object((1,3,6,1,4,1,232,14,2,3,1,1,9),_CpqIdeControllerHwLocation_Type())
cpqIdeControllerHwLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerHwLocation.setStatus(_q)
_CpqIdeControllerPciLocation_Type=DisplayString
_CpqIdeControllerPciLocation_Object=MibTableColumn
cpqIdeControllerPciLocation=_CpqIdeControllerPciLocation_Object((1,3,6,1,4,1,232,14,2,3,1,1,10),_CpqIdeControllerPciLocation_Type())
cpqIdeControllerPciLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeControllerPciLocation.setStatus(_q)
_CpqIdeAtaDisk_ObjectIdentity=ObjectIdentity
cpqIdeAtaDisk=_CpqIdeAtaDisk_ObjectIdentity((1,3,6,1,4,1,232,14,2,4))
_CpqIdeAtaDiskTable_Object=MibTable
cpqIdeAtaDiskTable=_CpqIdeAtaDiskTable_Object((1,3,6,1,4,1,232,14,2,4,1))
if mibBuilder.loadTexts:cpqIdeAtaDiskTable.setStatus(_A)
_CpqIdeAtaDiskEntry_Object=MibTableRow
cpqIdeAtaDiskEntry=_CpqIdeAtaDiskEntry_Object((1,3,6,1,4,1,232,14,2,4,1,1))
cpqIdeAtaDiskEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:cpqIdeAtaDiskEntry.setStatus(_A)
_CpqIdeAtaDiskControllerIndex_Type=Integer32
_CpqIdeAtaDiskControllerIndex_Object=MibTableColumn
cpqIdeAtaDiskControllerIndex=_CpqIdeAtaDiskControllerIndex_Object((1,3,6,1,4,1,232,14,2,4,1,1,1),_CpqIdeAtaDiskControllerIndex_Type())
cpqIdeAtaDiskControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskControllerIndex.setStatus(_A)
_CpqIdeAtaDiskIndex_Type=Integer32
_CpqIdeAtaDiskIndex_Object=MibTableColumn
cpqIdeAtaDiskIndex=_CpqIdeAtaDiskIndex_Object((1,3,6,1,4,1,232,14,2,4,1,1,2),_CpqIdeAtaDiskIndex_Type())
cpqIdeAtaDiskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskIndex.setStatus(_A)
_CpqIdeAtaDiskModel_Type=DisplayString
_CpqIdeAtaDiskModel_Object=MibTableColumn
cpqIdeAtaDiskModel=_CpqIdeAtaDiskModel_Object((1,3,6,1,4,1,232,14,2,4,1,1,3),_CpqIdeAtaDiskModel_Type())
cpqIdeAtaDiskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskModel.setStatus(_A)
_CpqIdeAtaDiskFwRev_Type=DisplayString
_CpqIdeAtaDiskFwRev_Object=MibTableColumn
cpqIdeAtaDiskFwRev=_CpqIdeAtaDiskFwRev_Object((1,3,6,1,4,1,232,14,2,4,1,1,4),_CpqIdeAtaDiskFwRev_Type())
cpqIdeAtaDiskFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskFwRev.setStatus(_A)
_CpqIdeAtaDiskSerialNumber_Type=DisplayString
_CpqIdeAtaDiskSerialNumber_Object=MibTableColumn
cpqIdeAtaDiskSerialNumber=_CpqIdeAtaDiskSerialNumber_Object((1,3,6,1,4,1,232,14,2,4,1,1,5),_CpqIdeAtaDiskSerialNumber_Type())
cpqIdeAtaDiskSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSerialNumber.setStatus(_A)
class _CpqIdeAtaDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_F,2),('smartError',3),(_L,4),(_r,5),('removed',6),('inserted',7)))
_CpqIdeAtaDiskStatus_Type.__name__=_D
_CpqIdeAtaDiskStatus_Object=MibTableColumn
cpqIdeAtaDiskStatus=_CpqIdeAtaDiskStatus_Object((1,3,6,1,4,1,232,14,2,4,1,1,6),_CpqIdeAtaDiskStatus_Type())
cpqIdeAtaDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskStatus.setStatus(_A)
class _CpqIdeAtaDiskCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeAtaDiskCondition_Type.__name__=_D
_CpqIdeAtaDiskCondition_Object=MibTableColumn
cpqIdeAtaDiskCondition=_CpqIdeAtaDiskCondition_Object((1,3,6,1,4,1,232,14,2,4,1,1,7),_CpqIdeAtaDiskCondition_Type())
cpqIdeAtaDiskCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskCondition.setStatus(_A)
_CpqIdeAtaDiskCapacity_Type=Integer32
_CpqIdeAtaDiskCapacity_Object=MibTableColumn
cpqIdeAtaDiskCapacity=_CpqIdeAtaDiskCapacity_Object((1,3,6,1,4,1,232,14,2,4,1,1,8),_CpqIdeAtaDiskCapacity_Type())
cpqIdeAtaDiskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskCapacity.setStatus(_A)
class _CpqIdeAtaDiskSmartEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_W,2),(_X,3)))
_CpqIdeAtaDiskSmartEnabled_Type.__name__=_D
_CpqIdeAtaDiskSmartEnabled_Object=MibTableColumn
cpqIdeAtaDiskSmartEnabled=_CpqIdeAtaDiskSmartEnabled_Object((1,3,6,1,4,1,232,14,2,4,1,1,9),_CpqIdeAtaDiskSmartEnabled_Type())
cpqIdeAtaDiskSmartEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSmartEnabled.setStatus(_A)
class _CpqIdeAtaDiskTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_E,1),('pioMode0',2),('pioMode1',3),('pioMode2',4),('pioMode3',5),('pioMode4',6),('dmaMode0',7),('dmaMode1',8),('dmaMode2',9),('ultraDmaMode0',10),('ultraDmaMode1',11),('ultraDmaMode2',12),('ultraDmaMode3',13),('ultraDmaMode4',14),('ultraDmaMode5',15)))
_CpqIdeAtaDiskTransferMode_Type.__name__=_D
_CpqIdeAtaDiskTransferMode_Object=MibTableColumn
cpqIdeAtaDiskTransferMode=_CpqIdeAtaDiskTransferMode_Object((1,3,6,1,4,1,232,14,2,4,1,1,10),_CpqIdeAtaDiskTransferMode_Type())
cpqIdeAtaDiskTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskTransferMode.setStatus(_A)
class _CpqIdeAtaDiskChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_s,2),(_t,3),('serial',4)))
_CpqIdeAtaDiskChannel_Type.__name__=_D
_CpqIdeAtaDiskChannel_Object=MibTableColumn
cpqIdeAtaDiskChannel=_CpqIdeAtaDiskChannel_Object((1,3,6,1,4,1,232,14,2,4,1,1,11),_CpqIdeAtaDiskChannel_Type())
cpqIdeAtaDiskChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskChannel.setStatus(_A)
class _CpqIdeAtaDiskNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44)));namedValues=NamedValues(*((_E,1),(_u,2),(_v,3),('sataDevice0',4),('sataDevice1',5),('sataDevice2',6),('sataDevice3',7),('sataDevice4',8),('sataDevice5',9),('sataDevice6',10),('sataDevice7',11),('sataDevice8',12),('sataDevice9',13),('sataDevice10',14),('sataDevice11',15),('sataDevice12',16),('sataDevice13',17),('sataDevice14',18),('sataDevice15',19),('sataDevice16',20),('bay1',21),('bay2',22),('bay3',23),('bay4',24),('bay5',25),('bay6',26),('bay7',27),('bay8',28),('bay9',29),('bay10',30),('bay11',31),('bay12',32),('bay13',33),('bay14',34),('bay15',35),('bay16',36),('bay17',37),('bay18',38),('bay19',39),('bay20',40),('bay21',41),('bay22',42),('bay23',43),('bay24',44)))
_CpqIdeAtaDiskNumber_Type.__name__=_D
_CpqIdeAtaDiskNumber_Object=MibTableColumn
cpqIdeAtaDiskNumber=_CpqIdeAtaDiskNumber_Object((1,3,6,1,4,1,232,14,2,4,1,1,12),_CpqIdeAtaDiskNumber_Type())
cpqIdeAtaDiskNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskNumber.setStatus(_A)
class _CpqIdeAtaDiskLogicalDriveMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_W,2),(_X,3)))
_CpqIdeAtaDiskLogicalDriveMember_Type.__name__=_D
_CpqIdeAtaDiskLogicalDriveMember_Object=MibTableColumn
cpqIdeAtaDiskLogicalDriveMember=_CpqIdeAtaDiskLogicalDriveMember_Object((1,3,6,1,4,1,232,14,2,4,1,1,13),_CpqIdeAtaDiskLogicalDriveMember_Type())
cpqIdeAtaDiskLogicalDriveMember.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskLogicalDriveMember.setStatus(_A)
class _CpqIdeAtaDiskIsSpare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_W,2),(_X,3)))
_CpqIdeAtaDiskIsSpare_Type.__name__=_D
_CpqIdeAtaDiskIsSpare_Object=MibTableColumn
cpqIdeAtaDiskIsSpare=_CpqIdeAtaDiskIsSpare_Object((1,3,6,1,4,1,232,14,2,4,1,1,14),_CpqIdeAtaDiskIsSpare_Type())
cpqIdeAtaDiskIsSpare.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskIsSpare.setStatus(_A)
class _CpqIdeAtaDiskOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeAtaDiskOsName_Type.__name__=_G
_CpqIdeAtaDiskOsName_Object=MibTableColumn
cpqIdeAtaDiskOsName=_CpqIdeAtaDiskOsName_Object((1,3,6,1,4,1,232,14,2,4,1,1,15),_CpqIdeAtaDiskOsName_Type())
cpqIdeAtaDiskOsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskOsName.setStatus(_A)
class _CpqIdeAtaDiskType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('ata',2),('sata',3)))
_CpqIdeAtaDiskType_Type.__name__=_D
_CpqIdeAtaDiskType_Object=MibTableColumn
cpqIdeAtaDiskType=_CpqIdeAtaDiskType_Object((1,3,6,1,4,1,232,14,2,4,1,1,16),_CpqIdeAtaDiskType_Type())
cpqIdeAtaDiskType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskType.setStatus(_A)
class _CpqIdeAtaDiskSataVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('sataOne',2),('sataTwo',3)))
_CpqIdeAtaDiskSataVersion_Type.__name__=_D
_CpqIdeAtaDiskSataVersion_Object=MibTableColumn
cpqIdeAtaDiskSataVersion=_CpqIdeAtaDiskSataVersion_Object((1,3,6,1,4,1,232,14,2,4,1,1,17),_CpqIdeAtaDiskSataVersion_Type())
cpqIdeAtaDiskSataVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSataVersion.setStatus(_A)
class _CpqIdeAtaDiskMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('rotatingPlatters',2),('solidState',3)))
_CpqIdeAtaDiskMediaType_Type.__name__=_D
_CpqIdeAtaDiskMediaType_Object=MibTableColumn
cpqIdeAtaDiskMediaType=_CpqIdeAtaDiskMediaType_Object((1,3,6,1,4,1,232,14,2,4,1,1,18),_CpqIdeAtaDiskMediaType_Type())
cpqIdeAtaDiskMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskMediaType.setStatus(_A)
class _CpqIdeAtaDiskSSDWearStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('fiftySixDayThreshold',3),('fivePercentThreshold',4),('twoPercentThreshold',5),(_r,6)))
_CpqIdeAtaDiskSSDWearStatus_Type.__name__=_D
_CpqIdeAtaDiskSSDWearStatus_Object=MibTableColumn
cpqIdeAtaDiskSSDWearStatus=_CpqIdeAtaDiskSSDWearStatus_Object((1,3,6,1,4,1,232,14,2,4,1,1,19),_CpqIdeAtaDiskSSDWearStatus_Type())
cpqIdeAtaDiskSSDWearStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSSDWearStatus.setStatus(_A)
_CpqIdeAtaDiskPowerOnHours_Type=Counter32
_CpqIdeAtaDiskPowerOnHours_Object=MibTableColumn
cpqIdeAtaDiskPowerOnHours=_CpqIdeAtaDiskPowerOnHours_Object((1,3,6,1,4,1,232,14,2,4,1,1,20),_CpqIdeAtaDiskPowerOnHours_Type())
cpqIdeAtaDiskPowerOnHours.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskPowerOnHours.setStatus(_A)
_CpqIdeAtaDiskSSDPercntEndrnceUsed_Type=Gauge32
_CpqIdeAtaDiskSSDPercntEndrnceUsed_Object=MibTableColumn
cpqIdeAtaDiskSSDPercntEndrnceUsed=_CpqIdeAtaDiskSSDPercntEndrnceUsed_Object((1,3,6,1,4,1,232,14,2,4,1,1,21),_CpqIdeAtaDiskSSDPercntEndrnceUsed_Type())
cpqIdeAtaDiskSSDPercntEndrnceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSSDPercntEndrnceUsed.setStatus(_A)
_CpqIdeAtaDiskSSDEstTimeRemainingHours_Type=Counter32
_CpqIdeAtaDiskSSDEstTimeRemainingHours_Object=MibTableColumn
cpqIdeAtaDiskSSDEstTimeRemainingHours=_CpqIdeAtaDiskSSDEstTimeRemainingHours_Object((1,3,6,1,4,1,232,14,2,4,1,1,22),_CpqIdeAtaDiskSSDEstTimeRemainingHours_Type())
cpqIdeAtaDiskSSDEstTimeRemainingHours.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskSSDEstTimeRemainingHours.setStatus(_A)
_CpqIdeAtaDiskCurrTemperature_Type=Gauge32
_CpqIdeAtaDiskCurrTemperature_Object=MibTableColumn
cpqIdeAtaDiskCurrTemperature=_CpqIdeAtaDiskCurrTemperature_Object((1,3,6,1,4,1,232,14,2,4,1,1,23),_CpqIdeAtaDiskCurrTemperature_Type())
cpqIdeAtaDiskCurrTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskCurrTemperature.setStatus(_A)
_CpqIdeAtaDiskTemperatureThreshold_Type=Gauge32
_CpqIdeAtaDiskTemperatureThreshold_Object=MibTableColumn
cpqIdeAtaDiskTemperatureThreshold=_CpqIdeAtaDiskTemperatureThreshold_Object((1,3,6,1,4,1,232,14,2,4,1,1,24),_CpqIdeAtaDiskTemperatureThreshold_Type())
cpqIdeAtaDiskTemperatureThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskTemperatureThreshold.setStatus(_A)
_CpqIdeAtaDiskMaximumOperatingTemp_Type=Gauge32
_CpqIdeAtaDiskMaximumOperatingTemp_Object=MibTableColumn
cpqIdeAtaDiskMaximumOperatingTemp=_CpqIdeAtaDiskMaximumOperatingTemp_Object((1,3,6,1,4,1,232,14,2,4,1,1,25),_CpqIdeAtaDiskMaximumOperatingTemp_Type())
cpqIdeAtaDiskMaximumOperatingTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskMaximumOperatingTemp.setStatus(_A)
_CpqIdeAtaDiskDestructiveOperatingTemp_Type=Gauge32
_CpqIdeAtaDiskDestructiveOperatingTemp_Object=MibTableColumn
cpqIdeAtaDiskDestructiveOperatingTemp=_CpqIdeAtaDiskDestructiveOperatingTemp_Object((1,3,6,1,4,1,232,14,2,4,1,1,26),_CpqIdeAtaDiskDestructiveOperatingTemp_Type())
cpqIdeAtaDiskDestructiveOperatingTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskDestructiveOperatingTemp.setStatus(_A)
class _CpqIdeAtaDiskLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeAtaDiskLocation_Type.__name__=_G
_CpqIdeAtaDiskLocation_Object=MibTableColumn
cpqIdeAtaDiskLocation=_CpqIdeAtaDiskLocation_Object((1,3,6,1,4,1,232,14,2,4,1,1,27),_CpqIdeAtaDiskLocation_Type())
cpqIdeAtaDiskLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaDiskLocation.setStatus(_A)
class _CpqIdeAtaEraseFailureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('secureEraseFailed',1),('secureEraseNotSupported',2),('noEraseSupported',3)))
_CpqIdeAtaEraseFailureType_Type.__name__=_D
_CpqIdeAtaEraseFailureType_Object=MibScalar
cpqIdeAtaEraseFailureType=_CpqIdeAtaEraseFailureType_Object((1,3,6,1,4,1,232,14,2,4,2),_CpqIdeAtaEraseFailureType_Type())
cpqIdeAtaEraseFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtaEraseFailureType.setStatus(_A)
_CpqIdeAtapiDevice_ObjectIdentity=ObjectIdentity
cpqIdeAtapiDevice=_CpqIdeAtapiDevice_ObjectIdentity((1,3,6,1,4,1,232,14,2,5))
_CpqIdeAtapiDeviceTable_Object=MibTable
cpqIdeAtapiDeviceTable=_CpqIdeAtapiDeviceTable_Object((1,3,6,1,4,1,232,14,2,5,1))
if mibBuilder.loadTexts:cpqIdeAtapiDeviceTable.setStatus(_A)
_CpqIdeAtapiDeviceEntry_Object=MibTableRow
cpqIdeAtapiDeviceEntry=_CpqIdeAtapiDeviceEntry_Object((1,3,6,1,4,1,232,14,2,5,1,1))
cpqIdeAtapiDeviceEntry.setIndexNames((0,_C,_w),(0,_C,_x))
if mibBuilder.loadTexts:cpqIdeAtapiDeviceEntry.setStatus(_A)
_CpqIdeAtapiDeviceControllerIndex_Type=Integer32
_CpqIdeAtapiDeviceControllerIndex_Object=MibTableColumn
cpqIdeAtapiDeviceControllerIndex=_CpqIdeAtapiDeviceControllerIndex_Object((1,3,6,1,4,1,232,14,2,5,1,1,1),_CpqIdeAtapiDeviceControllerIndex_Type())
cpqIdeAtapiDeviceControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceControllerIndex.setStatus(_A)
_CpqIdeAtapiDeviceIndex_Type=Integer32
_CpqIdeAtapiDeviceIndex_Object=MibTableColumn
cpqIdeAtapiDeviceIndex=_CpqIdeAtapiDeviceIndex_Object((1,3,6,1,4,1,232,14,2,5,1,1,2),_CpqIdeAtapiDeviceIndex_Type())
cpqIdeAtapiDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceIndex.setStatus(_A)
_CpqIdeAtapiDeviceModel_Type=DisplayString
_CpqIdeAtapiDeviceModel_Object=MibTableColumn
cpqIdeAtapiDeviceModel=_CpqIdeAtapiDeviceModel_Object((1,3,6,1,4,1,232,14,2,5,1,1,3),_CpqIdeAtapiDeviceModel_Type())
cpqIdeAtapiDeviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceModel.setStatus(_A)
_CpqIdeAtapiDeviceFwRev_Type=DisplayString
_CpqIdeAtapiDeviceFwRev_Object=MibTableColumn
cpqIdeAtapiDeviceFwRev=_CpqIdeAtapiDeviceFwRev_Object((1,3,6,1,4,1,232,14,2,5,1,1,4),_CpqIdeAtapiDeviceFwRev_Type())
cpqIdeAtapiDeviceFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceFwRev.setStatus(_A)
class _CpqIdeAtapiDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),('disk',2),('tape',3),(_g,4),(_h,5),(_i,6),(_j,7),(_k,8),(_l,9),(_m,10),(_n,11)))
_CpqIdeAtapiDeviceType_Type.__name__=_D
_CpqIdeAtapiDeviceType_Object=MibTableColumn
cpqIdeAtapiDeviceType=_CpqIdeAtapiDeviceType_Object((1,3,6,1,4,1,232,14,2,5,1,1,5),_CpqIdeAtapiDeviceType_Type())
cpqIdeAtapiDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceType.setStatus(_A)
class _CpqIdeAtapiDeviceTypeExtended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('pdcd',2),(_o,3)))
_CpqIdeAtapiDeviceTypeExtended_Type.__name__=_D
_CpqIdeAtapiDeviceTypeExtended_Object=MibTableColumn
cpqIdeAtapiDeviceTypeExtended=_CpqIdeAtapiDeviceTypeExtended_Object((1,3,6,1,4,1,232,14,2,5,1,1,6),_CpqIdeAtapiDeviceTypeExtended_Type())
cpqIdeAtapiDeviceTypeExtended.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceTypeExtended.setStatus(_A)
class _CpqIdeAtapiDeviceChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_s,2),(_t,3)))
_CpqIdeAtapiDeviceChannel_Type.__name__=_D
_CpqIdeAtapiDeviceChannel_Object=MibTableColumn
cpqIdeAtapiDeviceChannel=_CpqIdeAtapiDeviceChannel_Object((1,3,6,1,4,1,232,14,2,5,1,1,7),_CpqIdeAtapiDeviceChannel_Type())
cpqIdeAtapiDeviceChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceChannel.setStatus(_A)
class _CpqIdeAtapiDeviceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_u,2),(_v,3)))
_CpqIdeAtapiDeviceNumber_Type.__name__=_D
_CpqIdeAtapiDeviceNumber_Object=MibTableColumn
cpqIdeAtapiDeviceNumber=_CpqIdeAtapiDeviceNumber_Object((1,3,6,1,4,1,232,14,2,5,1,1,8),_CpqIdeAtapiDeviceNumber_Type())
cpqIdeAtapiDeviceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeAtapiDeviceNumber.setStatus(_A)
_CpqIdeLogicalDrive_ObjectIdentity=ObjectIdentity
cpqIdeLogicalDrive=_CpqIdeLogicalDrive_ObjectIdentity((1,3,6,1,4,1,232,14,2,6))
_CpqIdeLogicalDriveTable_Object=MibTable
cpqIdeLogicalDriveTable=_CpqIdeLogicalDriveTable_Object((1,3,6,1,4,1,232,14,2,6,1))
if mibBuilder.loadTexts:cpqIdeLogicalDriveTable.setStatus(_A)
_CpqIdeLogicalDriveEntry_Object=MibTableRow
cpqIdeLogicalDriveEntry=_CpqIdeLogicalDriveEntry_Object((1,3,6,1,4,1,232,14,2,6,1,1))
cpqIdeLogicalDriveEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:cpqIdeLogicalDriveEntry.setStatus(_A)
_CpqIdeLogicalDriveControllerIndex_Type=Integer32
_CpqIdeLogicalDriveControllerIndex_Object=MibTableColumn
cpqIdeLogicalDriveControllerIndex=_CpqIdeLogicalDriveControllerIndex_Object((1,3,6,1,4,1,232,14,2,6,1,1,1),_CpqIdeLogicalDriveControllerIndex_Type())
cpqIdeLogicalDriveControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveControllerIndex.setStatus(_A)
_CpqIdeLogicalDriveIndex_Type=Integer32
_CpqIdeLogicalDriveIndex_Object=MibTableColumn
cpqIdeLogicalDriveIndex=_CpqIdeLogicalDriveIndex_Object((1,3,6,1,4,1,232,14,2,6,1,1,2),_CpqIdeLogicalDriveIndex_Type())
cpqIdeLogicalDriveIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveIndex.setStatus(_A)
class _CpqIdeLogicalDriveRaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('raid0',2),('raid1',3),('raid0plus1',4),('raid5',5),('raid15',6),('volume',7)))
_CpqIdeLogicalDriveRaidLevel_Type.__name__=_D
_CpqIdeLogicalDriveRaidLevel_Object=MibTableColumn
cpqIdeLogicalDriveRaidLevel=_CpqIdeLogicalDriveRaidLevel_Object((1,3,6,1,4,1,232,14,2,6,1,1,3),_CpqIdeLogicalDriveRaidLevel_Type())
cpqIdeLogicalDriveRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveRaidLevel.setStatus(_A)
_CpqIdeLogicalDriveCapacity_Type=Integer32
_CpqIdeLogicalDriveCapacity_Object=MibTableColumn
cpqIdeLogicalDriveCapacity=_CpqIdeLogicalDriveCapacity_Object((1,3,6,1,4,1,232,14,2,6,1,1,4),_CpqIdeLogicalDriveCapacity_Type())
cpqIdeLogicalDriveCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveCapacity.setStatus(_A)
class _CpqIdeLogicalDriveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),('rebuilding',4),(_L,5)))
_CpqIdeLogicalDriveStatus_Type.__name__=_D
_CpqIdeLogicalDriveStatus_Object=MibTableColumn
cpqIdeLogicalDriveStatus=_CpqIdeLogicalDriveStatus_Object((1,3,6,1,4,1,232,14,2,6,1,1,5),_CpqIdeLogicalDriveStatus_Type())
cpqIdeLogicalDriveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveStatus.setStatus(_A)
class _CpqIdeLogicalDriveCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_M,3),(_L,4)))
_CpqIdeLogicalDriveCondition_Type.__name__=_D
_CpqIdeLogicalDriveCondition_Object=MibTableColumn
cpqIdeLogicalDriveCondition=_CpqIdeLogicalDriveCondition_Object((1,3,6,1,4,1,232,14,2,6,1,1,6),_CpqIdeLogicalDriveCondition_Type())
cpqIdeLogicalDriveCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveCondition.setStatus(_A)
class _CpqIdeLogicalDriveDiskIds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeLogicalDriveDiskIds_Type.__name__=_V
_CpqIdeLogicalDriveDiskIds_Object=MibTableColumn
cpqIdeLogicalDriveDiskIds=_CpqIdeLogicalDriveDiskIds_Object((1,3,6,1,4,1,232,14,2,6,1,1,7),_CpqIdeLogicalDriveDiskIds_Type())
cpqIdeLogicalDriveDiskIds.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveDiskIds.setStatus(_A)
_CpqIdeLogicalDriveStripeSize_Type=Integer32
_CpqIdeLogicalDriveStripeSize_Object=MibTableColumn
cpqIdeLogicalDriveStripeSize=_CpqIdeLogicalDriveStripeSize_Object((1,3,6,1,4,1,232,14,2,6,1,1,8),_CpqIdeLogicalDriveStripeSize_Type())
cpqIdeLogicalDriveStripeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveStripeSize.setStatus(_A)
class _CpqIdeLogicalDriveSpareIds_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeLogicalDriveSpareIds_Type.__name__=_V
_CpqIdeLogicalDriveSpareIds_Object=MibTableColumn
cpqIdeLogicalDriveSpareIds=_CpqIdeLogicalDriveSpareIds_Object((1,3,6,1,4,1,232,14,2,6,1,1,9),_CpqIdeLogicalDriveSpareIds_Type())
cpqIdeLogicalDriveSpareIds.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveSpareIds.setStatus(_A)
_CpqIdeLogicalDriveRebuildingDisk_Type=Integer32
_CpqIdeLogicalDriveRebuildingDisk_Object=MibTableColumn
cpqIdeLogicalDriveRebuildingDisk=_CpqIdeLogicalDriveRebuildingDisk_Object((1,3,6,1,4,1,232,14,2,6,1,1,10),_CpqIdeLogicalDriveRebuildingDisk_Type())
cpqIdeLogicalDriveRebuildingDisk.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveRebuildingDisk.setStatus(_A)
class _CpqIdeLogicalDriveOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqIdeLogicalDriveOsName_Type.__name__=_G
_CpqIdeLogicalDriveOsName_Object=MibTableColumn
cpqIdeLogicalDriveOsName=_CpqIdeLogicalDriveOsName_Object((1,3,6,1,4,1,232,14,2,6,1,1,11),_CpqIdeLogicalDriveOsName_Type())
cpqIdeLogicalDriveOsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqIdeLogicalDriveOsName.setStatus(_A)
cpqIdeDriveDegraded=NotificationType((1,3,6,1,4,1,232,0,14001))
cpqIdeDriveDegraded.setObjects(*((_J,_K),(_H,_I),(_C,_R)))
if mibBuilder.loadTexts:cpqIdeDriveDegraded.setStatus('')
cpqIdeDriveOk=NotificationType((1,3,6,1,4,1,232,0,14002))
cpqIdeDriveOk.setObjects(*((_J,_K),(_H,_I),(_C,_R)))
if mibBuilder.loadTexts:cpqIdeDriveOk.setStatus('')
cpqIdeDriveUltraAtaDegraded=NotificationType((1,3,6,1,4,1,232,0,14003))
cpqIdeDriveUltraAtaDegraded.setObjects(*((_J,_K),(_H,_I),(_C,_R)))
if mibBuilder.loadTexts:cpqIdeDriveUltraAtaDegraded.setStatus('')
cpqIdeAtaDiskStatusChange=NotificationType((1,3,6,1,4,1,232,0,14004))
cpqIdeAtaDiskStatusChange.setObjects(*((_J,_K),(_H,_I),(_C,_O),(_C,_P),(_C,_S),(_C,_T),(_C,_Q),(_C,_a),(_C,_U),(_C,_b)))
if mibBuilder.loadTexts:cpqIdeAtaDiskStatusChange.setStatus('')
cpqIdeLogicalDriveStatusChange=NotificationType((1,3,6,1,4,1,232,0,14005))
cpqIdeLogicalDriveStatusChange.setObjects(*((_J,_K),(_H,_I),(_C,_y),(_C,_z),(_C,_Y),(_C,_Z),(_C,_A0)))
if mibBuilder.loadTexts:cpqIdeLogicalDriveStatusChange.setStatus('')
cpqIdeAtaDiskSSDWearStatusChange=NotificationType((1,3,6,1,4,1,232,0,14006))
cpqIdeAtaDiskSSDWearStatusChange.setObjects(*((_J,_K),(_H,_I),(_C,_O),(_C,_P),(_C,_S),(_C,_T),(_C,_Q),(_C,_c),(_C,_U),(_C,_b)))
if mibBuilder.loadTexts:cpqIdeAtaDiskSSDWearStatusChange.setStatus('')
cpqIdeAtaSecureEraseFailed=NotificationType((1,3,6,1,4,1,232,0,14007))
cpqIdeAtaSecureEraseFailed.setObjects(*((_J,_K),(_H,_I),(_C,_O),(_C,_P),(_C,_Q),(_C,_A1)))
if mibBuilder.loadTexts:cpqIdeAtaSecureEraseFailed.setStatus('')
cpqIdeAtaDiskStatusChange2=NotificationType((1,3,6,1,4,1,232,0,14008))
cpqIdeAtaDiskStatusChange2.setObjects(*((_J,_K),(_H,_I),(_C,_O),(_C,_P),(_C,_S),(_C,_T),(_C,_Q),(_C,_a),(_C,_U),(_C,_d)))
if mibBuilder.loadTexts:cpqIdeAtaDiskStatusChange2.setStatus('')
cpqIdeAtaDiskSSDWearStatusChange2=NotificationType((1,3,6,1,4,1,232,0,14009))
cpqIdeAtaDiskSSDWearStatusChange2.setObjects(*((_J,_K),(_H,_I),(_C,_O),(_C,_P),(_C,_S),(_C,_T),(_C,_Q),(_C,_c),(_C,_U),(_C,_d)))
if mibBuilder.loadTexts:cpqIdeAtaDiskSSDWearStatusChange2.setStatus('')
mibBuilder.exportSymbols(_C,**{'cpqIdeDriveDegraded':cpqIdeDriveDegraded,'cpqIdeDriveOk':cpqIdeDriveOk,'cpqIdeDriveUltraAtaDegraded':cpqIdeDriveUltraAtaDegraded,'cpqIdeAtaDiskStatusChange':cpqIdeAtaDiskStatusChange,'cpqIdeLogicalDriveStatusChange':cpqIdeLogicalDriveStatusChange,'cpqIdeAtaDiskSSDWearStatusChange':cpqIdeAtaDiskSSDWearStatusChange,'cpqIdeAtaSecureEraseFailed':cpqIdeAtaSecureEraseFailed,'cpqIdeAtaDiskStatusChange2':cpqIdeAtaDiskStatusChange2,'cpqIdeAtaDiskSSDWearStatusChange2':cpqIdeAtaDiskSSDWearStatusChange2,'cpqIde':cpqIde,'cpqIdeMibRev':cpqIdeMibRev,'cpqIdeMibRevMajor':cpqIdeMibRevMajor,'cpqIdeMibRevMinor':cpqIdeMibRevMinor,'cpqIdeMibCondition':cpqIdeMibCondition,'cpqIdeComponent':cpqIdeComponent,'cpqIdeInterface':cpqIdeInterface,'cpqIdeOsCommon':cpqIdeOsCommon,'cpqIdeOsCommonPollFreq':cpqIdeOsCommonPollFreq,'cpqIdeOsCommonModuleTable':cpqIdeOsCommonModuleTable,'cpqIdeOsCommonModuleEntry':cpqIdeOsCommonModuleEntry,_f:cpqIdeOsCommonModuleIndex,'cpqIdeOsCommonModuleName':cpqIdeOsCommonModuleName,'cpqIdeOsCommonModuleVersion':cpqIdeOsCommonModuleVersion,'cpqIdeOsCommonModuleDate':cpqIdeOsCommonModuleDate,'cpqIdeOsCommonModulePurpose':cpqIdeOsCommonModulePurpose,'cpqIdeIdent':cpqIdeIdent,'cpqIdeIdentTable':cpqIdeIdentTable,'cpqIdeIdentEntry':cpqIdeIdentEntry,_R:cpqIdeIdentIndex,'cpqIdeIdentModel':cpqIdeIdentModel,'cpqIdeIdentSerNum':cpqIdeIdentSerNum,'cpqIdeIdentFWVers':cpqIdeIdentFWVers,'cpqIdeIdentCondition':cpqIdeIdentCondition,'cpqIdeIdentErrorNumber':cpqIdeIdentErrorNumber,'cpqIdeIdentType':cpqIdeIdentType,'cpqIdeIdentTypeExtended':cpqIdeIdentTypeExtended,'cpqIdeIdentCondition2':cpqIdeIdentCondition2,'cpqIdeIdentStatus':cpqIdeIdentStatus,'cpqIdeIdentUltraAtaAvailability':cpqIdeIdentUltraAtaAvailability,'cpqIdeController':cpqIdeController,'cpqIdeControllerTable':cpqIdeControllerTable,'cpqIdeControllerEntry':cpqIdeControllerEntry,_p:cpqIdeControllerIndex,'cpqIdeControllerOverallCondition':cpqIdeControllerOverallCondition,_y:cpqIdeControllerModel,'cpqIdeControllerFwRev':cpqIdeControllerFwRev,_z:cpqIdeControllerSlot,'cpqIdeControllerStatus':cpqIdeControllerStatus,'cpqIdeControllerCondition':cpqIdeControllerCondition,'cpqIdeControllerSerialNumber':cpqIdeControllerSerialNumber,'cpqIdeControllerHwLocation':cpqIdeControllerHwLocation,'cpqIdeControllerPciLocation':cpqIdeControllerPciLocation,'cpqIdeAtaDisk':cpqIdeAtaDisk,'cpqIdeAtaDiskTable':cpqIdeAtaDiskTable,'cpqIdeAtaDiskEntry':cpqIdeAtaDiskEntry,_O:cpqIdeAtaDiskControllerIndex,_P:cpqIdeAtaDiskIndex,_S:cpqIdeAtaDiskModel,_T:cpqIdeAtaDiskFwRev,_Q:cpqIdeAtaDiskSerialNumber,_a:cpqIdeAtaDiskStatus,'cpqIdeAtaDiskCondition':cpqIdeAtaDiskCondition,'cpqIdeAtaDiskCapacity':cpqIdeAtaDiskCapacity,'cpqIdeAtaDiskSmartEnabled':cpqIdeAtaDiskSmartEnabled,'cpqIdeAtaDiskTransferMode':cpqIdeAtaDiskTransferMode,_U:cpqIdeAtaDiskChannel,_b:cpqIdeAtaDiskNumber,'cpqIdeAtaDiskLogicalDriveMember':cpqIdeAtaDiskLogicalDriveMember,'cpqIdeAtaDiskIsSpare':cpqIdeAtaDiskIsSpare,'cpqIdeAtaDiskOsName':cpqIdeAtaDiskOsName,'cpqIdeAtaDiskType':cpqIdeAtaDiskType,'cpqIdeAtaDiskSataVersion':cpqIdeAtaDiskSataVersion,'cpqIdeAtaDiskMediaType':cpqIdeAtaDiskMediaType,_c:cpqIdeAtaDiskSSDWearStatus,'cpqIdeAtaDiskPowerOnHours':cpqIdeAtaDiskPowerOnHours,'cpqIdeAtaDiskSSDPercntEndrnceUsed':cpqIdeAtaDiskSSDPercntEndrnceUsed,'cpqIdeAtaDiskSSDEstTimeRemainingHours':cpqIdeAtaDiskSSDEstTimeRemainingHours,'cpqIdeAtaDiskCurrTemperature':cpqIdeAtaDiskCurrTemperature,'cpqIdeAtaDiskTemperatureThreshold':cpqIdeAtaDiskTemperatureThreshold,'cpqIdeAtaDiskMaximumOperatingTemp':cpqIdeAtaDiskMaximumOperatingTemp,'cpqIdeAtaDiskDestructiveOperatingTemp':cpqIdeAtaDiskDestructiveOperatingTemp,_d:cpqIdeAtaDiskLocation,_A1:cpqIdeAtaEraseFailureType,'cpqIdeAtapiDevice':cpqIdeAtapiDevice,'cpqIdeAtapiDeviceTable':cpqIdeAtapiDeviceTable,'cpqIdeAtapiDeviceEntry':cpqIdeAtapiDeviceEntry,_w:cpqIdeAtapiDeviceControllerIndex,_x:cpqIdeAtapiDeviceIndex,'cpqIdeAtapiDeviceModel':cpqIdeAtapiDeviceModel,'cpqIdeAtapiDeviceFwRev':cpqIdeAtapiDeviceFwRev,'cpqIdeAtapiDeviceType':cpqIdeAtapiDeviceType,'cpqIdeAtapiDeviceTypeExtended':cpqIdeAtapiDeviceTypeExtended,'cpqIdeAtapiDeviceChannel':cpqIdeAtapiDeviceChannel,'cpqIdeAtapiDeviceNumber':cpqIdeAtapiDeviceNumber,'cpqIdeLogicalDrive':cpqIdeLogicalDrive,'cpqIdeLogicalDriveTable':cpqIdeLogicalDriveTable,'cpqIdeLogicalDriveEntry':cpqIdeLogicalDriveEntry,_Y:cpqIdeLogicalDriveControllerIndex,_Z:cpqIdeLogicalDriveIndex,'cpqIdeLogicalDriveRaidLevel':cpqIdeLogicalDriveRaidLevel,'cpqIdeLogicalDriveCapacity':cpqIdeLogicalDriveCapacity,_A0:cpqIdeLogicalDriveStatus,'cpqIdeLogicalDriveCondition':cpqIdeLogicalDriveCondition,'cpqIdeLogicalDriveDiskIds':cpqIdeLogicalDriveDiskIds,'cpqIdeLogicalDriveStripeSize':cpqIdeLogicalDriveStripeSize,'cpqIdeLogicalDriveSpareIds':cpqIdeLogicalDriveSpareIds,'cpqIdeLogicalDriveRebuildingDisk':cpqIdeLogicalDriveRebuildingDisk,'cpqIdeLogicalDriveOsName':cpqIdeLogicalDriveOsName})