_Y='broken'
_X='unbroken'
_W='auto-negotiate'
_V='offline'
_U='online'
_T='DisplayString'
_S='NotificationType'
_R='mcbMCRedundantGroupNo'
_Q='speed1000M'
_P='speed100M'
_O='speed10M'
_N='full'
_M='half'
_L='action'
_K='off'
_J='on'
_I='mcbMCSlotNo'
_H='DLINK-MCB-MIB'
_G='disabled'
_F='enabled'
_E='unsupported'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','TextualConvention')
_McbMediaConverterFamily_ObjectIdentity=ObjectIdentity
mcbMediaConverterFamily=_McbMediaConverterFamily_ObjectIdentity((1,3,6,1,4,1,171,41))
_McbMediaConverterChassis_ObjectIdentity=ObjectIdentity
mcbMediaConverterChassis=_McbMediaConverterChassis_ObjectIdentity((1,3,6,1,4,1,171,41,1))
_McbSNMPMIB_ObjectIdentity=ObjectIdentity
mcbSNMPMIB=_McbSNMPMIB_ObjectIdentity((1,3,6,1,4,1,171,41,1,1))
class _McbSNMPTrapPowerFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapPowerFail_Type.__name__=_B
_McbSNMPTrapPowerFail_Object=MibScalar
mcbSNMPTrapPowerFail=_McbSNMPTrapPowerFail_Object((1,3,6,1,4,1,171,41,1,1,1),_McbSNMPTrapPowerFail_Type())
mcbSNMPTrapPowerFail.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapPowerFail.setStatus(_A)
class _McbSNMPTrapFanFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapFanFail_Type.__name__=_B
_McbSNMPTrapFanFail_Object=MibScalar
mcbSNMPTrapFanFail=_McbSNMPTrapFanFail_Object((1,3,6,1,4,1,171,41,1,1,2),_McbSNMPTrapFanFail_Type())
mcbSNMPTrapFanFail.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapFanFail.setStatus(_A)
class _McbSNMPTrapMCPlugin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCPlugin_Type.__name__=_B
_McbSNMPTrapMCPlugin_Object=MibScalar
mcbSNMPTrapMCPlugin=_McbSNMPTrapMCPlugin_Object((1,3,6,1,4,1,171,41,1,1,3),_McbSNMPTrapMCPlugin_Type())
mcbSNMPTrapMCPlugin.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCPlugin.setStatus(_A)
class _McbSNMPTrapMCPullout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCPullout_Type.__name__=_B
_McbSNMPTrapMCPullout_Object=MibScalar
mcbSNMPTrapMCPullout=_McbSNMPTrapMCPullout_Object((1,3,6,1,4,1,171,41,1,1,4),_McbSNMPTrapMCPullout_Type())
mcbSNMPTrapMCPullout.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCPullout.setStatus(_A)
class _McbSNMPTrapMCLinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCLinkDown_Type.__name__=_B
_McbSNMPTrapMCLinkDown_Object=MibScalar
mcbSNMPTrapMCLinkDown=_McbSNMPTrapMCLinkDown_Object((1,3,6,1,4,1,171,41,1,1,5),_McbSNMPTrapMCLinkDown_Type())
mcbSNMPTrapMCLinkDown.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCLinkDown.setStatus(_A)
class _McbSNMPTrapMCLinkUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCLinkUp_Type.__name__=_B
_McbSNMPTrapMCLinkUp_Object=MibScalar
mcbSNMPTrapMCLinkUp=_McbSNMPTrapMCLinkUp_Object((1,3,6,1,4,1,171,41,1,1,6),_McbSNMPTrapMCLinkUp_Type())
mcbSNMPTrapMCLinkUp.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCLinkUp.setStatus(_A)
class _McbSNMPTrapMCLinkBroken_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCLinkBroken_Type.__name__=_B
_McbSNMPTrapMCLinkBroken_Object=MibScalar
mcbSNMPTrapMCLinkBroken=_McbSNMPTrapMCLinkBroken_Object((1,3,6,1,4,1,171,41,1,1,7),_McbSNMPTrapMCLinkBroken_Type())
mcbSNMPTrapMCLinkBroken.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCLinkBroken.setStatus(_A)
class _McbSNMPTrapMCActiveSlotChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCActiveSlotChange_Type.__name__=_B
_McbSNMPTrapMCActiveSlotChange_Object=MibScalar
mcbSNMPTrapMCActiveSlotChange=_McbSNMPTrapMCActiveSlotChange_Object((1,3,6,1,4,1,171,41,1,1,8),_McbSNMPTrapMCActiveSlotChange_Type())
mcbSNMPTrapMCActiveSlotChange.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCActiveSlotChange.setStatus(_A)
class _McbSNMPTrapMCActiveSlotLose_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbSNMPTrapMCActiveSlotLose_Type.__name__=_B
_McbSNMPTrapMCActiveSlotLose_Object=MibScalar
mcbSNMPTrapMCActiveSlotLose=_McbSNMPTrapMCActiveSlotLose_Object((1,3,6,1,4,1,171,41,1,1,9),_McbSNMPTrapMCActiveSlotLose_Type())
mcbSNMPTrapMCActiveSlotLose.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbSNMPTrapMCActiveSlotLose.setStatus(_A)
_McbAdministrator_ObjectIdentity=ObjectIdentity
mcbAdministrator=_McbAdministrator_ObjectIdentity((1,3,6,1,4,1,171,41,1,2))
_McbAdministratorHardwareRev_Type=DisplayString
_McbAdministratorHardwareRev_Object=MibScalar
mcbAdministratorHardwareRev=_McbAdministratorHardwareRev_Object((1,3,6,1,4,1,171,41,1,2,1),_McbAdministratorHardwareRev_Type())
mcbAdministratorHardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbAdministratorHardwareRev.setStatus(_A)
_McbAdministratorSoftwareRev_Type=DisplayString
_McbAdministratorSoftwareRev_Object=MibScalar
mcbAdministratorSoftwareRev=_McbAdministratorSoftwareRev_Object((1,3,6,1,4,1,171,41,1,2,2),_McbAdministratorSoftwareRev_Type())
mcbAdministratorSoftwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbAdministratorSoftwareRev.setStatus(_A)
_McbAdministratorBiosRev_Type=DisplayString
_McbAdministratorBiosRev_Object=MibScalar
mcbAdministratorBiosRev=_McbAdministratorBiosRev_Object((1,3,6,1,4,1,171,41,1,2,3),_McbAdministratorBiosRev_Type())
mcbAdministratorBiosRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbAdministratorBiosRev.setStatus(_A)
class _McbAdministratorFactoryReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_McbAdministratorFactoryReset_Type.__name__=_B
_McbAdministratorFactoryReset_Object=MibScalar
mcbAdministratorFactoryReset=_McbAdministratorFactoryReset_Object((1,3,6,1,4,1,171,41,1,2,4),_McbAdministratorFactoryReset_Type())
mcbAdministratorFactoryReset.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbAdministratorFactoryReset.setStatus(_A)
class _McbAdministratorFactoryResetCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_McbAdministratorFactoryResetCPU_Type.__name__=_B
_McbAdministratorFactoryResetCPU_Object=MibScalar
mcbAdministratorFactoryResetCPU=_McbAdministratorFactoryResetCPU_Object((1,3,6,1,4,1,171,41,1,2,5),_McbAdministratorFactoryResetCPU_Type())
mcbAdministratorFactoryResetCPU.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbAdministratorFactoryResetCPU.setStatus(_A)
class _McbAdministratorSoftwareReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_McbAdministratorSoftwareReboot_Type.__name__=_B
_McbAdministratorSoftwareReboot_Object=MibScalar
mcbAdministratorSoftwareReboot=_McbAdministratorSoftwareReboot_Object((1,3,6,1,4,1,171,41,1,2,6),_McbAdministratorSoftwareReboot_Type())
mcbAdministratorSoftwareReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbAdministratorSoftwareReboot.setStatus(_A)
_McbMCFrame_ObjectIdentity=ObjectIdentity
mcbMCFrame=_McbMCFrame_ObjectIdentity((1,3,6,1,4,1,171,41,1,3))
class _McbFramePowerOneOnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFramePowerOneOnStatus_Type.__name__=_B
_McbFramePowerOneOnStatus_Object=MibScalar
mcbFramePowerOneOnStatus=_McbFramePowerOneOnStatus_Object((1,3,6,1,4,1,171,41,1,3,1),_McbFramePowerOneOnStatus_Type())
mcbFramePowerOneOnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFramePowerOneOnStatus.setStatus(_A)
class _McbFramePowerTwoOnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFramePowerTwoOnStatus_Type.__name__=_B
_McbFramePowerTwoOnStatus_Object=MibScalar
mcbFramePowerTwoOnStatus=_McbFramePowerTwoOnStatus_Object((1,3,6,1,4,1,171,41,1,3,2),_McbFramePowerTwoOnStatus_Type())
mcbFramePowerTwoOnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFramePowerTwoOnStatus.setStatus(_A)
class _McbFramePowerOneFailStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFramePowerOneFailStatus_Type.__name__=_B
_McbFramePowerOneFailStatus_Object=MibScalar
mcbFramePowerOneFailStatus=_McbFramePowerOneFailStatus_Object((1,3,6,1,4,1,171,41,1,3,3),_McbFramePowerOneFailStatus_Type())
mcbFramePowerOneFailStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFramePowerOneFailStatus.setStatus(_A)
class _McbFramePowerTwoFailStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFramePowerTwoFailStatus_Type.__name__=_B
_McbFramePowerTwoFailStatus_Object=MibScalar
mcbFramePowerTwoFailStatus=_McbFramePowerTwoFailStatus_Object((1,3,6,1,4,1,171,41,1,3,4),_McbFramePowerTwoFailStatus_Type())
mcbFramePowerTwoFailStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFramePowerTwoFailStatus.setStatus(_A)
class _McbFrameFanOneFailStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFrameFanOneFailStatus_Type.__name__=_B
_McbFrameFanOneFailStatus_Object=MibScalar
mcbFrameFanOneFailStatus=_McbFrameFanOneFailStatus_Object((1,3,6,1,4,1,171,41,1,3,5),_McbFrameFanOneFailStatus_Type())
mcbFrameFanOneFailStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFrameFanOneFailStatus.setStatus(_A)
class _McbFrameFanTwoFailStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_McbFrameFanTwoFailStatus_Type.__name__=_B
_McbFrameFanTwoFailStatus_Object=MibScalar
mcbFrameFanTwoFailStatus=_McbFrameFanTwoFailStatus_Object((1,3,6,1,4,1,171,41,1,3,6),_McbFrameFanTwoFailStatus_Type())
mcbFrameFanTwoFailStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbFrameFanTwoFailStatus.setStatus(_A)
_McbMCSlots_ObjectIdentity=ObjectIdentity
mcbMCSlots=_McbMCSlots_ObjectIdentity((1,3,6,1,4,1,171,41,1,4))
_McbMCSlotCount_Type=Integer32
_McbMCSlotCount_Object=MibScalar
mcbMCSlotCount=_McbMCSlotCount_Object((1,3,6,1,4,1,171,41,1,4,1),_McbMCSlotCount_Type())
mcbMCSlotCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCSlotCount.setStatus(_A)
_McbMCSlotTable_Object=MibTable
mcbMCSlotTable=_McbMCSlotTable_Object((1,3,6,1,4,1,171,41,1,4,2))
if mibBuilder.loadTexts:mcbMCSlotTable.setStatus(_A)
_McbMCSlotEntry_Object=MibTableRow
mcbMCSlotEntry=_McbMCSlotEntry_Object((1,3,6,1,4,1,171,41,1,4,2,1))
mcbMCSlotEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:mcbMCSlotEntry.setStatus(_A)
_McbMCSlotNo_Type=Integer32
_McbMCSlotNo_Object=MibTableColumn
mcbMCSlotNo=_McbMCSlotNo_Object((1,3,6,1,4,1,171,41,1,4,2,1,1),_McbMCSlotNo_Type())
mcbMCSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCSlotNo.setStatus(_A)
class _McbMCSlotExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('exist',1),('nonexist',2),(_E,3)))
_McbMCSlotExist_Type.__name__=_B
_McbMCSlotExist_Object=MibTableColumn
mcbMCSlotExist=_McbMCSlotExist_Object((1,3,6,1,4,1,171,41,1,4,2,1,2),_McbMCSlotExist_Type())
mcbMCSlotExist.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCSlotExist.setStatus(_A)
_McbMCModelName_Type=DisplayString
_McbMCModelName_Object=MibTableColumn
mcbMCModelName=_McbMCModelName_Object((1,3,6,1,4,1,171,41,1,4,2,1,3),_McbMCModelName_Type())
mcbMCModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCModelName.setStatus(_A)
class _McbMCMediaOneType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tp',1),('fiber',2),(_E,3)))
_McbMCMediaOneType_Type.__name__=_B
_McbMCMediaOneType_Object=MibTableColumn
mcbMCMediaOneType=_McbMCMediaOneType_Object((1,3,6,1,4,1,171,41,1,4,2,1,4),_McbMCMediaOneType_Type())
mcbMCMediaOneType.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneType.setStatus(_A)
class _McbMCMediaTwoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tp',1),('fiber',2),(_E,3)))
_McbMCMediaTwoType_Type.__name__=_B
_McbMCMediaTwoType_Object=MibTableColumn
mcbMCMediaTwoType=_McbMCMediaTwoType_Object((1,3,6,1,4,1,171,41,1,4,2,1,5),_McbMCMediaTwoType_Type())
mcbMCMediaTwoType.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoType.setStatus(_A)
class _McbMCMediaOneLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_E,3)))
_McbMCMediaOneLinkStatus_Type.__name__=_B
_McbMCMediaOneLinkStatus_Object=MibTableColumn
mcbMCMediaOneLinkStatus=_McbMCMediaOneLinkStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,6),_McbMCMediaOneLinkStatus_Type())
mcbMCMediaOneLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneLinkStatus.setStatus(_A)
class _McbMCMediaTwoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_E,3)))
_McbMCMediaTwoLinkStatus_Type.__name__=_B
_McbMCMediaTwoLinkStatus_Object=MibTableColumn
mcbMCMediaTwoLinkStatus=_McbMCMediaTwoLinkStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,7),_McbMCMediaTwoLinkStatus_Type())
mcbMCMediaTwoLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoLinkStatus.setStatus(_A)
class _McbMCMediaOneDupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_E,3)))
_McbMCMediaOneDupStatus_Type.__name__=_B
_McbMCMediaOneDupStatus_Object=MibTableColumn
mcbMCMediaOneDupStatus=_McbMCMediaOneDupStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,8),_McbMCMediaOneDupStatus_Type())
mcbMCMediaOneDupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneDupStatus.setStatus(_A)
class _McbMCMediaTwoDupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_E,3)))
_McbMCMediaTwoDupStatus_Type.__name__=_B
_McbMCMediaTwoDupStatus_Object=MibTableColumn
mcbMCMediaTwoDupStatus=_McbMCMediaTwoDupStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,9),_McbMCMediaTwoDupStatus_Type())
mcbMCMediaTwoDupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoDupStatus.setStatus(_A)
class _McbMCMediaOneSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4)))
_McbMCMediaOneSpeedStatus_Type.__name__=_B
_McbMCMediaOneSpeedStatus_Object=MibTableColumn
mcbMCMediaOneSpeedStatus=_McbMCMediaOneSpeedStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,10),_McbMCMediaOneSpeedStatus_Type())
mcbMCMediaOneSpeedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneSpeedStatus.setStatus(_A)
class _McbMCMediaTwoSpeedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4)))
_McbMCMediaTwoSpeedStatus_Type.__name__=_B
_McbMCMediaTwoSpeedStatus_Object=MibTableColumn
mcbMCMediaTwoSpeedStatus=_McbMCMediaTwoSpeedStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,11),_McbMCMediaTwoSpeedStatus_Type())
mcbMCMediaTwoSpeedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoSpeedStatus.setStatus(_A)
class _McbMCSlotName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_McbMCSlotName_Type.__name__=_T
_McbMCSlotName_Object=MibTableColumn
mcbMCSlotName=_McbMCSlotName_Object((1,3,6,1,4,1,171,41,1,4,2,1,12),_McbMCSlotName_Type())
mcbMCSlotName.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSlotName.setStatus(_A)
class _McbMCEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCEnable_Type.__name__=_B
_McbMCEnable_Object=MibTableColumn
mcbMCEnable=_McbMCEnable_Object((1,3,6,1,4,1,171,41,1,4,2,1,13),_McbMCEnable_Type())
mcbMCEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCEnable.setStatus(_A)
class _McbMCSetLLCF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCSetLLCF_Type.__name__=_B
_McbMCSetLLCF_Object=MibTableColumn
mcbMCSetLLCF=_McbMCSetLLCF_Object((1,3,6,1,4,1,171,41,1,4,2,1,14),_McbMCSetLLCF_Type())
mcbMCSetLLCF.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetLLCF.setStatus(_A)
class _McbMCEnableMediaOne_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCEnableMediaOne_Type.__name__=_B
_McbMCEnableMediaOne_Object=MibTableColumn
mcbMCEnableMediaOne=_McbMCEnableMediaOne_Object((1,3,6,1,4,1,171,41,1,4,2,1,15),_McbMCEnableMediaOne_Type())
mcbMCEnableMediaOne.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCEnableMediaOne.setStatus(_A)
class _McbMCEnableMediaTwo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCEnableMediaTwo_Type.__name__=_B
_McbMCEnableMediaTwo_Object=MibTableColumn
mcbMCEnableMediaTwo=_McbMCEnableMediaTwo_Object((1,3,6,1,4,1,171,41,1,4,2,1,16),_McbMCEnableMediaTwo_Type())
mcbMCEnableMediaTwo.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCEnableMediaTwo.setStatus(_A)
class _McbMCSetMediaOneAutoNegotiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('force',2),(_E,3)))
_McbMCSetMediaOneAutoNegotiate_Type.__name__=_B
_McbMCSetMediaOneAutoNegotiate_Object=MibTableColumn
mcbMCSetMediaOneAutoNegotiate=_McbMCSetMediaOneAutoNegotiate_Object((1,3,6,1,4,1,171,41,1,4,2,1,17),_McbMCSetMediaOneAutoNegotiate_Type())
mcbMCSetMediaOneAutoNegotiate.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaOneAutoNegotiate.setStatus(_A)
class _McbMCSetMediaTwoAutoNegotiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('force',2),(_E,3)))
_McbMCSetMediaTwoAutoNegotiate_Type.__name__=_B
_McbMCSetMediaTwoAutoNegotiate_Object=MibTableColumn
mcbMCSetMediaTwoAutoNegotiate=_McbMCSetMediaTwoAutoNegotiate_Object((1,3,6,1,4,1,171,41,1,4,2,1,18),_McbMCSetMediaTwoAutoNegotiate_Type())
mcbMCSetMediaTwoAutoNegotiate.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaTwoAutoNegotiate.setStatus(_A)
class _McbMCSetMediaOneSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4)))
_McbMCSetMediaOneSpeed_Type.__name__=_B
_McbMCSetMediaOneSpeed_Object=MibTableColumn
mcbMCSetMediaOneSpeed=_McbMCSetMediaOneSpeed_Object((1,3,6,1,4,1,171,41,1,4,2,1,19),_McbMCSetMediaOneSpeed_Type())
mcbMCSetMediaOneSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaOneSpeed.setStatus(_A)
class _McbMCSetMediaTwoSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4)))
_McbMCSetMediaTwoSpeed_Type.__name__=_B
_McbMCSetMediaTwoSpeed_Object=MibTableColumn
mcbMCSetMediaTwoSpeed=_McbMCSetMediaTwoSpeed_Object((1,3,6,1,4,1,171,41,1,4,2,1,20),_McbMCSetMediaTwoSpeed_Type())
mcbMCSetMediaTwoSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaTwoSpeed.setStatus(_A)
class _McbMCSetMediaOneDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_E,3)))
_McbMCSetMediaOneDuplex_Type.__name__=_B
_McbMCSetMediaOneDuplex_Object=MibTableColumn
mcbMCSetMediaOneDuplex=_McbMCSetMediaOneDuplex_Object((1,3,6,1,4,1,171,41,1,4,2,1,21),_McbMCSetMediaOneDuplex_Type())
mcbMCSetMediaOneDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaOneDuplex.setStatus(_A)
class _McbMCSetMediaTwoDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_E,3)))
_McbMCSetMediaTwoDuplex_Type.__name__=_B
_McbMCSetMediaTwoDuplex_Object=MibTableColumn
mcbMCSetMediaTwoDuplex=_McbMCSetMediaTwoDuplex_Object((1,3,6,1,4,1,171,41,1,4,2,1,22),_McbMCSetMediaTwoDuplex_Type())
mcbMCSetMediaTwoDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaTwoDuplex.setStatus(_A)
class _McbMCSetMediaOneFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCSetMediaOneFlowControl_Type.__name__=_B
_McbMCSetMediaOneFlowControl_Object=MibTableColumn
mcbMCSetMediaOneFlowControl=_McbMCSetMediaOneFlowControl_Object((1,3,6,1,4,1,171,41,1,4,2,1,23),_McbMCSetMediaOneFlowControl_Type())
mcbMCSetMediaOneFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaOneFlowControl.setStatus(_A)
class _McbMCSetMediaTwoFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCSetMediaTwoFlowControl_Type.__name__=_B
_McbMCSetMediaTwoFlowControl_Object=MibTableColumn
mcbMCSetMediaTwoFlowControl=_McbMCSetMediaTwoFlowControl_Object((1,3,6,1,4,1,171,41,1,4,2,1,24),_McbMCSetMediaTwoFlowControl_Type())
mcbMCSetMediaTwoFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaTwoFlowControl.setStatus(_A)
class _McbMCSetMediaOneLLR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCSetMediaOneLLR_Type.__name__=_B
_McbMCSetMediaOneLLR_Object=MibTableColumn
mcbMCSetMediaOneLLR=_McbMCSetMediaOneLLR_Object((1,3,6,1,4,1,171,41,1,4,2,1,25),_McbMCSetMediaOneLLR_Type())
mcbMCSetMediaOneLLR.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaOneLLR.setStatus(_A)
class _McbMCSetMediaTwoLLR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_E,3)))
_McbMCSetMediaTwoLLR_Type.__name__=_B
_McbMCSetMediaTwoLLR_Object=MibTableColumn
mcbMCSetMediaTwoLLR=_McbMCSetMediaTwoLLR_Object((1,3,6,1,4,1,171,41,1,4,2,1,26),_McbMCSetMediaTwoLLR_Type())
mcbMCSetMediaTwoLLR.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCSetMediaTwoLLR.setStatus(_A)
class _McbMCMediaOneBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_E,3)))
_McbMCMediaOneBrokenStatus_Type.__name__=_B
_McbMCMediaOneBrokenStatus_Object=MibTableColumn
mcbMCMediaOneBrokenStatus=_McbMCMediaOneBrokenStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,27),_McbMCMediaOneBrokenStatus_Type())
mcbMCMediaOneBrokenStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneBrokenStatus.setStatus(_A)
class _McbMCMediaTwoBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_E,3)))
_McbMCMediaTwoBrokenStatus_Type.__name__=_B
_McbMCMediaTwoBrokenStatus_Object=MibTableColumn
mcbMCMediaTwoBrokenStatus=_McbMCMediaTwoBrokenStatus_Object((1,3,6,1,4,1,171,41,1,4,2,1,28),_McbMCMediaTwoBrokenStatus_Type())
mcbMCMediaTwoBrokenStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoBrokenStatus.setStatus(_A)
_McbMCMediaOneTxPacketCount_Type=Counter32
_McbMCMediaOneTxPacketCount_Object=MibTableColumn
mcbMCMediaOneTxPacketCount=_McbMCMediaOneTxPacketCount_Object((1,3,6,1,4,1,171,41,1,4,2,1,29),_McbMCMediaOneTxPacketCount_Type())
mcbMCMediaOneTxPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneTxPacketCount.setStatus(_A)
_McbMCMediaOneRxPacketCount_Type=Counter32
_McbMCMediaOneRxPacketCount_Object=MibTableColumn
mcbMCMediaOneRxPacketCount=_McbMCMediaOneRxPacketCount_Object((1,3,6,1,4,1,171,41,1,4,2,1,30),_McbMCMediaOneRxPacketCount_Type())
mcbMCMediaOneRxPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaOneRxPacketCount.setStatus(_A)
_McbMCMediaTwoTxPacketCount_Type=Counter32
_McbMCMediaTwoTxPacketCount_Object=MibTableColumn
mcbMCMediaTwoTxPacketCount=_McbMCMediaTwoTxPacketCount_Object((1,3,6,1,4,1,171,41,1,4,2,1,31),_McbMCMediaTwoTxPacketCount_Type())
mcbMCMediaTwoTxPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoTxPacketCount.setStatus(_A)
_McbMCMediaTwoRxPacketCount_Type=Counter32
_McbMCMediaTwoRxPacketCount_Object=MibTableColumn
mcbMCMediaTwoRxPacketCount=_McbMCMediaTwoRxPacketCount_Object((1,3,6,1,4,1,171,41,1,4,2,1,32),_McbMCMediaTwoRxPacketCount_Type())
mcbMCMediaTwoRxPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCMediaTwoRxPacketCount.setStatus(_A)
_McbMCRedundantGroups_ObjectIdentity=ObjectIdentity
mcbMCRedundantGroups=_McbMCRedundantGroups_ObjectIdentity((1,3,6,1,4,1,171,41,1,5))
_McbMCRedundantGroupCount_Type=Integer32
_McbMCRedundantGroupCount_Object=MibScalar
mcbMCRedundantGroupCount=_McbMCRedundantGroupCount_Object((1,3,6,1,4,1,171,41,1,5,1),_McbMCRedundantGroupCount_Type())
mcbMCRedundantGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCRedundantGroupCount.setStatus(_A)
_McbMCRedundantGroupTable_Object=MibTable
mcbMCRedundantGroupTable=_McbMCRedundantGroupTable_Object((1,3,6,1,4,1,171,41,1,5,2))
if mibBuilder.loadTexts:mcbMCRedundantGroupTable.setStatus(_A)
_McbMCRedundantGroupEntry_Object=MibTableRow
mcbMCRedundantGroupEntry=_McbMCRedundantGroupEntry_Object((1,3,6,1,4,1,171,41,1,5,2,1))
mcbMCRedundantGroupEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:mcbMCRedundantGroupEntry.setStatus(_A)
_McbMCRedundantGroupNo_Type=Integer32
_McbMCRedundantGroupNo_Object=MibTableColumn
mcbMCRedundantGroupNo=_McbMCRedundantGroupNo_Object((1,3,6,1,4,1,171,41,1,5,2,1,1),_McbMCRedundantGroupNo_Type())
mcbMCRedundantGroupNo.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCRedundantGroupNo.setStatus(_A)
_McbMCRedundantGroupPrimarySlot_Type=Integer32
_McbMCRedundantGroupPrimarySlot_Object=MibTableColumn
mcbMCRedundantGroupPrimarySlot=_McbMCRedundantGroupPrimarySlot_Object((1,3,6,1,4,1,171,41,1,5,2,1,2),_McbMCRedundantGroupPrimarySlot_Type())
mcbMCRedundantGroupPrimarySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCRedundantGroupPrimarySlot.setStatus(_A)
_McbMCRedundantGroupSecondarySlot_Type=Integer32
_McbMCRedundantGroupSecondarySlot_Object=MibTableColumn
mcbMCRedundantGroupSecondarySlot=_McbMCRedundantGroupSecondarySlot_Object((1,3,6,1,4,1,171,41,1,5,2,1,3),_McbMCRedundantGroupSecondarySlot_Type())
mcbMCRedundantGroupSecondarySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCRedundantGroupSecondarySlot.setStatus(_A)
class _McbMCRedundantGroupEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_McbMCRedundantGroupEnable_Type.__name__=_B
_McbMCRedundantGroupEnable_Object=MibTableColumn
mcbMCRedundantGroupEnable=_McbMCRedundantGroupEnable_Object((1,3,6,1,4,1,171,41,1,5,2,1,4),_McbMCRedundantGroupEnable_Type())
mcbMCRedundantGroupEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCRedundantGroupEnable.setStatus(_A)
_McbMCRedundantGroupActiveSlot_Type=Integer32
_McbMCRedundantGroupActiveSlot_Object=MibTableColumn
mcbMCRedundantGroupActiveSlot=_McbMCRedundantGroupActiveSlot_Object((1,3,6,1,4,1,171,41,1,5,2,1,5),_McbMCRedundantGroupActiveSlot_Type())
mcbMCRedundantGroupActiveSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mcbMCRedundantGroupActiveSlot.setStatus(_A)
class _McbMCRedundantGroupRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_McbMCRedundantGroupRestart_Type.__name__=_B
_McbMCRedundantGroupRestart_Object=MibTableColumn
mcbMCRedundantGroupRestart=_McbMCRedundantGroupRestart_Object((1,3,6,1,4,1,171,41,1,5,2,1,6),_McbMCRedundantGroupRestart_Type())
mcbMCRedundantGroupRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:mcbMCRedundantGroupRestart.setStatus(_A)
mcbPowerOneFail=NotificationType((1,3,6,1,4,1,171,41,1,0,1))
if mibBuilder.loadTexts:mcbPowerOneFail.setStatus('')
mcbFanOneFail=NotificationType((1,3,6,1,4,1,171,41,1,0,2))
if mibBuilder.loadTexts:mcbFanOneFail.setStatus('')
mcbPowerTwoFail=NotificationType((1,3,6,1,4,1,171,41,1,0,3))
if mibBuilder.loadTexts:mcbPowerTwoFail.setStatus('')
mcbFanTwoFail=NotificationType((1,3,6,1,4,1,171,41,1,0,4))
if mibBuilder.loadTexts:mcbFanTwoFail.setStatus('')
mcbMediaConverterPlugin=NotificationType((1,3,6,1,4,1,171,41,1,0,5))
mcbMediaConverterPlugin.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMediaConverterPlugin.setStatus('')
mcbMediaConverterPullout=NotificationType((1,3,6,1,4,1,171,41,1,0,6))
mcbMediaConverterPullout.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMediaConverterPullout.setStatus('')
mcbMCMediaOneLinkDown=NotificationType((1,3,6,1,4,1,171,41,1,0,7))
mcbMCMediaOneLinkDown.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaOneLinkDown.setStatus('')
mcbMCMediaTwoLinkDown=NotificationType((1,3,6,1,4,1,171,41,1,0,8))
mcbMCMediaTwoLinkDown.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaTwoLinkDown.setStatus('')
mcbMCMediaOneLinkUp=NotificationType((1,3,6,1,4,1,171,41,1,0,9))
mcbMCMediaOneLinkUp.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaOneLinkUp.setStatus('')
mcbMCMediaTwoLinkUp=NotificationType((1,3,6,1,4,1,171,41,1,0,10))
mcbMCMediaTwoLinkUp.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaTwoLinkUp.setStatus('')
mcbMCMediaOneBroken=NotificationType((1,3,6,1,4,1,171,41,1,0,11))
mcbMCMediaOneBroken.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaOneBroken.setStatus('')
mcbMCMediaTwoBroken=NotificationType((1,3,6,1,4,1,171,41,1,0,12))
mcbMCMediaTwoBroken.setObjects((_H,_I))
if mibBuilder.loadTexts:mcbMCMediaTwoBroken.setStatus('')
mcbMCActiveSlotChange=NotificationType((1,3,6,1,4,1,171,41,1,0,13))
mcbMCActiveSlotChange.setObjects((_H,_R))
if mibBuilder.loadTexts:mcbMCActiveSlotChange.setStatus('')
mcbMCActiveSlotLose=NotificationType((1,3,6,1,4,1,171,41,1,0,14))
mcbMCActiveSlotLose.setObjects((_H,_R))
if mibBuilder.loadTexts:mcbMCActiveSlotLose.setStatus('')
mibBuilder.exportSymbols(_H,**{'mcbMediaConverterFamily':mcbMediaConverterFamily,'mcbMediaConverterChassis':mcbMediaConverterChassis,'mcbPowerOneFail':mcbPowerOneFail,'mcbFanOneFail':mcbFanOneFail,'mcbPowerTwoFail':mcbPowerTwoFail,'mcbFanTwoFail':mcbFanTwoFail,'mcbMediaConverterPlugin':mcbMediaConverterPlugin,'mcbMediaConverterPullout':mcbMediaConverterPullout,'mcbMCMediaOneLinkDown':mcbMCMediaOneLinkDown,'mcbMCMediaTwoLinkDown':mcbMCMediaTwoLinkDown,'mcbMCMediaOneLinkUp':mcbMCMediaOneLinkUp,'mcbMCMediaTwoLinkUp':mcbMCMediaTwoLinkUp,'mcbMCMediaOneBroken':mcbMCMediaOneBroken,'mcbMCMediaTwoBroken':mcbMCMediaTwoBroken,'mcbMCActiveSlotChange':mcbMCActiveSlotChange,'mcbMCActiveSlotLose':mcbMCActiveSlotLose,'mcbSNMPMIB':mcbSNMPMIB,'mcbSNMPTrapPowerFail':mcbSNMPTrapPowerFail,'mcbSNMPTrapFanFail':mcbSNMPTrapFanFail,'mcbSNMPTrapMCPlugin':mcbSNMPTrapMCPlugin,'mcbSNMPTrapMCPullout':mcbSNMPTrapMCPullout,'mcbSNMPTrapMCLinkDown':mcbSNMPTrapMCLinkDown,'mcbSNMPTrapMCLinkUp':mcbSNMPTrapMCLinkUp,'mcbSNMPTrapMCLinkBroken':mcbSNMPTrapMCLinkBroken,'mcbSNMPTrapMCActiveSlotChange':mcbSNMPTrapMCActiveSlotChange,'mcbSNMPTrapMCActiveSlotLose':mcbSNMPTrapMCActiveSlotLose,'mcbAdministrator':mcbAdministrator,'mcbAdministratorHardwareRev':mcbAdministratorHardwareRev,'mcbAdministratorSoftwareRev':mcbAdministratorSoftwareRev,'mcbAdministratorBiosRev':mcbAdministratorBiosRev,'mcbAdministratorFactoryReset':mcbAdministratorFactoryReset,'mcbAdministratorFactoryResetCPU':mcbAdministratorFactoryResetCPU,'mcbAdministratorSoftwareReboot':mcbAdministratorSoftwareReboot,'mcbMCFrame':mcbMCFrame,'mcbFramePowerOneOnStatus':mcbFramePowerOneOnStatus,'mcbFramePowerTwoOnStatus':mcbFramePowerTwoOnStatus,'mcbFramePowerOneFailStatus':mcbFramePowerOneFailStatus,'mcbFramePowerTwoFailStatus':mcbFramePowerTwoFailStatus,'mcbFrameFanOneFailStatus':mcbFrameFanOneFailStatus,'mcbFrameFanTwoFailStatus':mcbFrameFanTwoFailStatus,'mcbMCSlots':mcbMCSlots,'mcbMCSlotCount':mcbMCSlotCount,'mcbMCSlotTable':mcbMCSlotTable,'mcbMCSlotEntry':mcbMCSlotEntry,_I:mcbMCSlotNo,'mcbMCSlotExist':mcbMCSlotExist,'mcbMCModelName':mcbMCModelName,'mcbMCMediaOneType':mcbMCMediaOneType,'mcbMCMediaTwoType':mcbMCMediaTwoType,'mcbMCMediaOneLinkStatus':mcbMCMediaOneLinkStatus,'mcbMCMediaTwoLinkStatus':mcbMCMediaTwoLinkStatus,'mcbMCMediaOneDupStatus':mcbMCMediaOneDupStatus,'mcbMCMediaTwoDupStatus':mcbMCMediaTwoDupStatus,'mcbMCMediaOneSpeedStatus':mcbMCMediaOneSpeedStatus,'mcbMCMediaTwoSpeedStatus':mcbMCMediaTwoSpeedStatus,'mcbMCSlotName':mcbMCSlotName,'mcbMCEnable':mcbMCEnable,'mcbMCSetLLCF':mcbMCSetLLCF,'mcbMCEnableMediaOne':mcbMCEnableMediaOne,'mcbMCEnableMediaTwo':mcbMCEnableMediaTwo,'mcbMCSetMediaOneAutoNegotiate':mcbMCSetMediaOneAutoNegotiate,'mcbMCSetMediaTwoAutoNegotiate':mcbMCSetMediaTwoAutoNegotiate,'mcbMCSetMediaOneSpeed':mcbMCSetMediaOneSpeed,'mcbMCSetMediaTwoSpeed':mcbMCSetMediaTwoSpeed,'mcbMCSetMediaOneDuplex':mcbMCSetMediaOneDuplex,'mcbMCSetMediaTwoDuplex':mcbMCSetMediaTwoDuplex,'mcbMCSetMediaOneFlowControl':mcbMCSetMediaOneFlowControl,'mcbMCSetMediaTwoFlowControl':mcbMCSetMediaTwoFlowControl,'mcbMCSetMediaOneLLR':mcbMCSetMediaOneLLR,'mcbMCSetMediaTwoLLR':mcbMCSetMediaTwoLLR,'mcbMCMediaOneBrokenStatus':mcbMCMediaOneBrokenStatus,'mcbMCMediaTwoBrokenStatus':mcbMCMediaTwoBrokenStatus,'mcbMCMediaOneTxPacketCount':mcbMCMediaOneTxPacketCount,'mcbMCMediaOneRxPacketCount':mcbMCMediaOneRxPacketCount,'mcbMCMediaTwoTxPacketCount':mcbMCMediaTwoTxPacketCount,'mcbMCMediaTwoRxPacketCount':mcbMCMediaTwoRxPacketCount,'mcbMCRedundantGroups':mcbMCRedundantGroups,'mcbMCRedundantGroupCount':mcbMCRedundantGroupCount,'mcbMCRedundantGroupTable':mcbMCRedundantGroupTable,'mcbMCRedundantGroupEntry':mcbMCRedundantGroupEntry,_R:mcbMCRedundantGroupNo,'mcbMCRedundantGroupPrimarySlot':mcbMCRedundantGroupPrimarySlot,'mcbMCRedundantGroupSecondarySlot':mcbMCRedundantGroupSecondarySlot,'mcbMCRedundantGroupEnable':mcbMCRedundantGroupEnable,'mcbMCRedundantGroupActiveSlot':mcbMCRedundantGroupActiveSlot,'mcbMCRedundantGroupRestart':mcbMCRedundantGroupRestart})