_W='asMacAddress'
_V='asRadiusServerIndex'
_U='asDhcpServerIp'
_T='DisplayString'
_S='NotificationType'
_R='accessSwitchVoltageCurValue'
_Q='accessSwitchFanRpmCurValue'
_P='accessSwitchSysTempCurValue'
_O='ifIndex'
_N='IF-MIB'
_M='disable'
_L='enable'
_K='accessSwitchSysTempIndex'
_J='accessSwitchVoltageIndex'
_I='accessSwitchFanRpmIndex'
_H='current'
_G='accessSwitchSystemCurrentStatus'
_F='accessSwitchProblemCause'
_E='Integer32'
_D='read-write'
_C='ZYXEL-AS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','Timeout')
ifIndex,=mibBuilder.importSymbols(_N,_O)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_S,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_T,'MacAddress','PhysAddress','RowStatus','TextualConvention')
class ASSlotNum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slot1',1),('slot2',2)))
class ASModuleType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('aes-100',1),('aes-100-1',2),('aam1008-61',3),('aam1008-63',4),('sam1008',5)))
_Zyxel_ObjectIdentity=ObjectIdentity
zyxel=_Zyxel_ObjectIdentity((1,3,6,1,4,1,890))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,890,1))
_AccessSwitch_ObjectIdentity=ObjectIdentity
accessSwitch=_AccessSwitch_ObjectIdentity((1,3,6,1,4,1,890,1,5))
_AccessSwitchCommon_ObjectIdentity=ObjectIdentity
accessSwitchCommon=_AccessSwitchCommon_ObjectIdentity((1,3,6,1,4,1,890,1,5,1))
_AccessSwitchMgnt_ObjectIdentity=ObjectIdentity
accessSwitchMgnt=_AccessSwitchMgnt_ObjectIdentity((1,3,6,1,4,1,890,1,5,1,1))
class _AccessSwitchSystemCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AccessSwitchSystemCurrentStatus_Type.__name__=_E
_AccessSwitchSystemCurrentStatus_Object=MibScalar
accessSwitchSystemCurrentStatus=_AccessSwitchSystemCurrentStatus_Object((1,3,6,1,4,1,890,1,5,1,1,1),_AccessSwitchSystemCurrentStatus_Type())
accessSwitchSystemCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSystemCurrentStatus.setStatus(_A)
_AccessSwitchProblemCause_Type=DisplayString
_AccessSwitchProblemCause_Object=MibScalar
accessSwitchProblemCause=_AccessSwitchProblemCause_Object((1,3,6,1,4,1,890,1,5,1,1,2),_AccessSwitchProblemCause_Type())
accessSwitchProblemCause.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchProblemCause.setStatus(_A)
_AccessSwitchSystemTemperature_Type=DisplayString
_AccessSwitchSystemTemperature_Object=MibScalar
accessSwitchSystemTemperature=_AccessSwitchSystemTemperature_Object((1,3,6,1,4,1,890,1,5,1,1,3),_AccessSwitchSystemTemperature_Type())
accessSwitchSystemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSystemTemperature.setStatus(_A)
_AccessSwitchFanRpmTable_Object=MibTable
accessSwitchFanRpmTable=_AccessSwitchFanRpmTable_Object((1,3,6,1,4,1,890,1,5,1,1,4))
if mibBuilder.loadTexts:accessSwitchFanRpmTable.setStatus(_A)
_AccessSwitchFanRpmEntry_Object=MibTableRow
accessSwitchFanRpmEntry=_AccessSwitchFanRpmEntry_Object((1,3,6,1,4,1,890,1,5,1,1,4,1))
accessSwitchFanRpmEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:accessSwitchFanRpmEntry.setStatus(_A)
_AccessSwitchFanRpmIndex_Type=Integer32
_AccessSwitchFanRpmIndex_Object=MibTableColumn
accessSwitchFanRpmIndex=_AccessSwitchFanRpmIndex_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,1),_AccessSwitchFanRpmIndex_Type())
accessSwitchFanRpmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmIndex.setStatus(_A)
_AccessSwitchFanRpmCurValue_Type=Integer32
_AccessSwitchFanRpmCurValue_Object=MibTableColumn
accessSwitchFanRpmCurValue=_AccessSwitchFanRpmCurValue_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,2),_AccessSwitchFanRpmCurValue_Type())
accessSwitchFanRpmCurValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmCurValue.setStatus(_A)
_AccessSwitchFanRpmMaxValue_Type=Integer32
_AccessSwitchFanRpmMaxValue_Object=MibTableColumn
accessSwitchFanRpmMaxValue=_AccessSwitchFanRpmMaxValue_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,3),_AccessSwitchFanRpmMaxValue_Type())
accessSwitchFanRpmMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmMaxValue.setStatus(_A)
_AccessSwitchFanRpmMinValue_Type=Integer32
_AccessSwitchFanRpmMinValue_Object=MibTableColumn
accessSwitchFanRpmMinValue=_AccessSwitchFanRpmMinValue_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,4),_AccessSwitchFanRpmMinValue_Type())
accessSwitchFanRpmMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmMinValue.setStatus(_A)
_AccessSwitchFanRpmLowThresh_Type=Integer32
_AccessSwitchFanRpmLowThresh_Object=MibTableColumn
accessSwitchFanRpmLowThresh=_AccessSwitchFanRpmLowThresh_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,5),_AccessSwitchFanRpmLowThresh_Type())
accessSwitchFanRpmLowThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmLowThresh.setStatus(_A)
_AccessSwitchFanRpmDescr_Type=DisplayString
_AccessSwitchFanRpmDescr_Object=MibTableColumn
accessSwitchFanRpmDescr=_AccessSwitchFanRpmDescr_Object((1,3,6,1,4,1,890,1,5,1,1,4,1,6),_AccessSwitchFanRpmDescr_Type())
accessSwitchFanRpmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFanRpmDescr.setStatus(_A)
_AccessSwitchVoltageTable_Object=MibTable
accessSwitchVoltageTable=_AccessSwitchVoltageTable_Object((1,3,6,1,4,1,890,1,5,1,1,5))
if mibBuilder.loadTexts:accessSwitchVoltageTable.setStatus(_A)
_AccessSwitchVoltageEntry_Object=MibTableRow
accessSwitchVoltageEntry=_AccessSwitchVoltageEntry_Object((1,3,6,1,4,1,890,1,5,1,1,5,1))
accessSwitchVoltageEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:accessSwitchVoltageEntry.setStatus(_A)
_AccessSwitchVoltageIndex_Type=Integer32
_AccessSwitchVoltageIndex_Object=MibTableColumn
accessSwitchVoltageIndex=_AccessSwitchVoltageIndex_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,1),_AccessSwitchVoltageIndex_Type())
accessSwitchVoltageIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageIndex.setStatus(_A)
_AccessSwitchVoltageCurValue_Type=Integer32
_AccessSwitchVoltageCurValue_Object=MibTableColumn
accessSwitchVoltageCurValue=_AccessSwitchVoltageCurValue_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,2),_AccessSwitchVoltageCurValue_Type())
accessSwitchVoltageCurValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageCurValue.setStatus(_A)
_AccessSwitchVoltageMaxValue_Type=Integer32
_AccessSwitchVoltageMaxValue_Object=MibTableColumn
accessSwitchVoltageMaxValue=_AccessSwitchVoltageMaxValue_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,3),_AccessSwitchVoltageMaxValue_Type())
accessSwitchVoltageMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageMaxValue.setStatus(_A)
_AccessSwitchVoltageMinValue_Type=Integer32
_AccessSwitchVoltageMinValue_Object=MibTableColumn
accessSwitchVoltageMinValue=_AccessSwitchVoltageMinValue_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,4),_AccessSwitchVoltageMinValue_Type())
accessSwitchVoltageMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageMinValue.setStatus(_A)
_AccessSwitchVoltageNominalValue_Type=Integer32
_AccessSwitchVoltageNominalValue_Object=MibTableColumn
accessSwitchVoltageNominalValue=_AccessSwitchVoltageNominalValue_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,5),_AccessSwitchVoltageNominalValue_Type())
accessSwitchVoltageNominalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageNominalValue.setStatus(_A)
_AccessSwitchVoltageLowThresh_Type=Integer32
_AccessSwitchVoltageLowThresh_Object=MibTableColumn
accessSwitchVoltageLowThresh=_AccessSwitchVoltageLowThresh_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,6),_AccessSwitchVoltageLowThresh_Type())
accessSwitchVoltageLowThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageLowThresh.setStatus(_A)
_AccessSwitchVoltageDescr_Type=DisplayString
_AccessSwitchVoltageDescr_Object=MibTableColumn
accessSwitchVoltageDescr=_AccessSwitchVoltageDescr_Object((1,3,6,1,4,1,890,1,5,1,1,5,1,7),_AccessSwitchVoltageDescr_Type())
accessSwitchVoltageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchVoltageDescr.setStatus(_A)
_AccessSwitchSysTempTable_Object=MibTable
accessSwitchSysTempTable=_AccessSwitchSysTempTable_Object((1,3,6,1,4,1,890,1,5,1,1,6))
if mibBuilder.loadTexts:accessSwitchSysTempTable.setStatus(_A)
_AccessSwitchSysTempEntry_Object=MibTableRow
accessSwitchSysTempEntry=_AccessSwitchSysTempEntry_Object((1,3,6,1,4,1,890,1,5,1,1,6,1))
accessSwitchSysTempEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:accessSwitchSysTempEntry.setStatus(_A)
_AccessSwitchSysTempIndex_Type=Integer32
_AccessSwitchSysTempIndex_Object=MibTableColumn
accessSwitchSysTempIndex=_AccessSwitchSysTempIndex_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,1),_AccessSwitchSysTempIndex_Type())
accessSwitchSysTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempIndex.setStatus(_A)
_AccessSwitchSysTempCurValue_Type=Integer32
_AccessSwitchSysTempCurValue_Object=MibTableColumn
accessSwitchSysTempCurValue=_AccessSwitchSysTempCurValue_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,2),_AccessSwitchSysTempCurValue_Type())
accessSwitchSysTempCurValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempCurValue.setStatus(_A)
_AccessSwitchSysTempMaxValue_Type=Integer32
_AccessSwitchSysTempMaxValue_Object=MibTableColumn
accessSwitchSysTempMaxValue=_AccessSwitchSysTempMaxValue_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,3),_AccessSwitchSysTempMaxValue_Type())
accessSwitchSysTempMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempMaxValue.setStatus(_A)
_AccessSwitchSysTempMinValue_Type=Integer32
_AccessSwitchSysTempMinValue_Object=MibTableColumn
accessSwitchSysTempMinValue=_AccessSwitchSysTempMinValue_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,4),_AccessSwitchSysTempMinValue_Type())
accessSwitchSysTempMinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempMinValue.setStatus(_A)
_AccessSwitchSysTempHighThresh_Type=Integer32
_AccessSwitchSysTempHighThresh_Object=MibTableColumn
accessSwitchSysTempHighThresh=_AccessSwitchSysTempHighThresh_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,5),_AccessSwitchSysTempHighThresh_Type())
accessSwitchSysTempHighThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempHighThresh.setStatus(_A)
_AccessSwitchSysTempDescr_Type=DisplayString
_AccessSwitchSysTempDescr_Object=MibTableColumn
accessSwitchSysTempDescr=_AccessSwitchSysTempDescr_Object((1,3,6,1,4,1,890,1,5,1,1,6,1,6),_AccessSwitchSysTempDescr_Type())
accessSwitchSysTempDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchSysTempDescr.setStatus(_A)
_AccessSwitchMaintenance_Type=Integer32
_AccessSwitchMaintenance_Object=MibScalar
accessSwitchMaintenance=_AccessSwitchMaintenance_Object((1,3,6,1,4,1,890,1,5,1,1,7),_AccessSwitchMaintenance_Type())
accessSwitchMaintenance.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchMaintenance.setStatus(_A)
_AccessSwitchMaintenancePort_Type=Integer32
_AccessSwitchMaintenancePort_Object=MibScalar
accessSwitchMaintenancePort=_AccessSwitchMaintenancePort_Object((1,3,6,1,4,1,890,1,5,1,1,8),_AccessSwitchMaintenancePort_Type())
accessSwitchMaintenancePort.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchMaintenancePort.setStatus(_A)
_AccessSwitchMaxNumOfStaticVlans_Type=Integer32
_AccessSwitchMaxNumOfStaticVlans_Object=MibScalar
accessSwitchMaxNumOfStaticVlans=_AccessSwitchMaxNumOfStaticVlans_Object((1,3,6,1,4,1,890,1,5,1,1,9),_AccessSwitchMaxNumOfStaticVlans_Type())
accessSwitchMaxNumOfStaticVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchMaxNumOfStaticVlans.setStatus(_A)
_AcccessSwitchChassisId_Type=Integer32
_AcccessSwitchChassisId_Object=MibScalar
acccessSwitchChassisId=_AcccessSwitchChassisId_Object((1,3,6,1,4,1,890,1,5,1,1,10),_AcccessSwitchChassisId_Type())
acccessSwitchChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:acccessSwitchChassisId.setStatus(_A)
_AccessSwitchSlotId_Type=ASSlotNum
_AccessSwitchSlotId_Object=MibScalar
accessSwitchSlotId=_AccessSwitchSlotId_Object((1,3,6,1,4,1,890,1,5,1,1,11),_AccessSwitchSlotId_Type())
accessSwitchSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchSlotId.setStatus(_A)
_AccessSwitchModuleType_Type=ASModuleType
_AccessSwitchModuleType_Object=MibScalar
accessSwitchModuleType=_AccessSwitchModuleType_Object((1,3,6,1,4,1,890,1,5,1,1,12),_AccessSwitchModuleType_Type())
accessSwitchModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchModuleType.setStatus(_A)
_AccessSwitchFWVersion_Type=DisplayString
_AccessSwitchFWVersion_Object=MibScalar
accessSwitchFWVersion=_AccessSwitchFWVersion_Object((1,3,6,1,4,1,890,1,5,1,1,13),_AccessSwitchFWVersion_Type())
accessSwitchFWVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchFWVersion.setStatus(_A)
_AccessSwitchDriverVersion_Type=DisplayString
_AccessSwitchDriverVersion_Object=MibScalar
accessSwitchDriverVersion=_AccessSwitchDriverVersion_Object((1,3,6,1,4,1,890,1,5,1,1,14),_AccessSwitchDriverVersion_Type())
accessSwitchDriverVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchDriverVersion.setStatus(_A)
_AccessSwitchModemCodeVersion_Type=DisplayString
_AccessSwitchModemCodeVersion_Object=MibScalar
accessSwitchModemCodeVersion=_AccessSwitchModemCodeVersion_Object((1,3,6,1,4,1,890,1,5,1,1,15),_AccessSwitchModemCodeVersion_Type())
accessSwitchModemCodeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:accessSwitchModemCodeVersion.setStatus(_A)
_AccessSwitchDSLConfOps_Type=Integer32
_AccessSwitchDSLConfOps_Object=MibScalar
accessSwitchDSLConfOps=_AccessSwitchDSLConfOps_Object((1,3,6,1,4,1,890,1,5,1,1,16),_AccessSwitchDSLConfOps_Type())
accessSwitchDSLConfOps.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchDSLConfOps.setStatus(_A)
_AccessSwitchDSLConfTarget_Type=OctetString
_AccessSwitchDSLConfTarget_Object=MibScalar
accessSwitchDSLConfTarget=_AccessSwitchDSLConfTarget_Object((1,3,6,1,4,1,890,1,5,1,1,17),_AccessSwitchDSLConfTarget_Type())
accessSwitchDSLConfTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchDSLConfTarget.setStatus(_A)
class _AccessSwitchDSLConfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AccessSwitchDSLConfProfileName_Type.__name__=_T
_AccessSwitchDSLConfProfileName_Object=MibScalar
accessSwitchDSLConfProfileName=_AccessSwitchDSLConfProfileName_Object((1,3,6,1,4,1,890,1,5,1,1,18),_AccessSwitchDSLConfProfileName_Type())
accessSwitchDSLConfProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchDSLConfProfileName.setStatus(_A)
_AccessSwitchDSLConfMode_Type=Integer32
_AccessSwitchDSLConfMode_Object=MibScalar
accessSwitchDSLConfMode=_AccessSwitchDSLConfMode_Object((1,3,6,1,4,1,890,1,5,1,1,19),_AccessSwitchDSLConfMode_Type())
accessSwitchDSLConfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:accessSwitchDSLConfMode.setStatus(_A)
_AsPacketForwardingTable_Object=MibTable
asPacketForwardingTable=_AsPacketForwardingTable_Object((1,3,6,1,4,1,890,1,5,1,1,20))
if mibBuilder.loadTexts:asPacketForwardingTable.setStatus(_A)
_AsPacketForwardingEntry_Object=MibTableRow
asPacketForwardingEntry=_AsPacketForwardingEntry_Object((1,3,6,1,4,1,890,1,5,1,1,20,1))
asPacketForwardingEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:asPacketForwardingEntry.setStatus(_A)
_AsPacketForwardingPortList_Type=PortList
_AsPacketForwardingPortList_Object=MibTableColumn
asPacketForwardingPortList=_AsPacketForwardingPortList_Object((1,3,6,1,4,1,890,1,5,1,1,20,1,1),_AsPacketForwardingPortList_Type())
asPacketForwardingPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:asPacketForwardingPortList.setStatus(_A)
class _AsDhcpRelayEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AsDhcpRelayEnable_Type.__name__=_E
_AsDhcpRelayEnable_Object=MibScalar
asDhcpRelayEnable=_AsDhcpRelayEnable_Object((1,3,6,1,4,1,890,1,5,1,1,21),_AsDhcpRelayEnable_Type())
asDhcpRelayEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:asDhcpRelayEnable.setStatus(_A)
class _AsDhcpRelayOption82Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AsDhcpRelayOption82Enable_Type.__name__=_E
_AsDhcpRelayOption82Enable_Object=MibScalar
asDhcpRelayOption82Enable=_AsDhcpRelayOption82Enable_Object((1,3,6,1,4,1,890,1,5,1,1,22),_AsDhcpRelayOption82Enable_Type())
asDhcpRelayOption82Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:asDhcpRelayOption82Enable.setStatus(_A)
_AsDhcpRelayOption82Info_Type=DisplayString
_AsDhcpRelayOption82Info_Object=MibScalar
asDhcpRelayOption82Info=_AsDhcpRelayOption82Info_Object((1,3,6,1,4,1,890,1,5,1,1,23),_AsDhcpRelayOption82Info_Type())
asDhcpRelayOption82Info.setMaxAccess(_D)
if mibBuilder.loadTexts:asDhcpRelayOption82Info.setStatus(_A)
_AsMaxNumOfDhcpServers_Type=Integer32
_AsMaxNumOfDhcpServers_Object=MibScalar
asMaxNumOfDhcpServers=_AsMaxNumOfDhcpServers_Object((1,3,6,1,4,1,890,1,5,1,1,24),_AsMaxNumOfDhcpServers_Type())
asMaxNumOfDhcpServers.setMaxAccess(_B)
if mibBuilder.loadTexts:asMaxNumOfDhcpServers.setStatus(_A)
_AsDhcpServerTable_Object=MibTable
asDhcpServerTable=_AsDhcpServerTable_Object((1,3,6,1,4,1,890,1,5,1,1,25))
if mibBuilder.loadTexts:asDhcpServerTable.setStatus(_A)
_AsDhcpServerEntry_Object=MibTableRow
asDhcpServerEntry=_AsDhcpServerEntry_Object((1,3,6,1,4,1,890,1,5,1,1,25,1))
asDhcpServerEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:asDhcpServerEntry.setStatus(_A)
_AsDhcpServerIp_Type=IpAddress
_AsDhcpServerIp_Object=MibTableColumn
asDhcpServerIp=_AsDhcpServerIp_Object((1,3,6,1,4,1,890,1,5,1,1,25,1,1),_AsDhcpServerIp_Type())
asDhcpServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:asDhcpServerIp.setStatus(_A)
_AsDhcpServerRowStatus_Type=RowStatus
_AsDhcpServerRowStatus_Object=MibTableColumn
asDhcpServerRowStatus=_AsDhcpServerRowStatus_Object((1,3,6,1,4,1,890,1,5,1,1,25,1,2),_AsDhcpServerRowStatus_Type())
asDhcpServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:asDhcpServerRowStatus.setStatus(_A)
_AsMaxNumberOfRadiusServers_Type=Integer32
_AsMaxNumberOfRadiusServers_Object=MibScalar
asMaxNumberOfRadiusServers=_AsMaxNumberOfRadiusServers_Object((1,3,6,1,4,1,890,1,5,1,1,28),_AsMaxNumberOfRadiusServers_Type())
asMaxNumberOfRadiusServers.setMaxAccess(_B)
if mibBuilder.loadTexts:asMaxNumberOfRadiusServers.setStatus(_A)
_AsRadiusServerTable_Object=MibTable
asRadiusServerTable=_AsRadiusServerTable_Object((1,3,6,1,4,1,890,1,5,1,1,29))
if mibBuilder.loadTexts:asRadiusServerTable.setStatus(_A)
_AsRadiusServerEntry_Object=MibTableRow
asRadiusServerEntry=_AsRadiusServerEntry_Object((1,3,6,1,4,1,890,1,5,1,1,29,1))
asRadiusServerEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:asRadiusServerEntry.setStatus(_A)
_AsRadiusServerIndex_Type=Integer32
_AsRadiusServerIndex_Object=MibTableColumn
asRadiusServerIndex=_AsRadiusServerIndex_Object((1,3,6,1,4,1,890,1,5,1,1,29,1,1),_AsRadiusServerIndex_Type())
asRadiusServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:asRadiusServerIndex.setStatus(_A)
_AsRadiusServerIp_Type=IpAddress
_AsRadiusServerIp_Object=MibTableColumn
asRadiusServerIp=_AsRadiusServerIp_Object((1,3,6,1,4,1,890,1,5,1,1,29,1,2),_AsRadiusServerIp_Type())
asRadiusServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:asRadiusServerIp.setStatus(_A)
_AsRadiusServerPort_Type=Integer32
_AsRadiusServerPort_Object=MibTableColumn
asRadiusServerPort=_AsRadiusServerPort_Object((1,3,6,1,4,1,890,1,5,1,1,29,1,3),_AsRadiusServerPort_Type())
asRadiusServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:asRadiusServerPort.setStatus(_A)
_AsRadiusSharedSecret_Type=DisplayString
_AsRadiusSharedSecret_Object=MibTableColumn
asRadiusSharedSecret=_AsRadiusSharedSecret_Object((1,3,6,1,4,1,890,1,5,1,1,29,1,4),_AsRadiusSharedSecret_Type())
asRadiusSharedSecret.setMaxAccess(_D)
if mibBuilder.loadTexts:asRadiusSharedSecret.setStatus(_A)
_AsRadiusServerRowStatus_Type=RowStatus
_AsRadiusServerRowStatus_Object=MibTableColumn
asRadiusServerRowStatus=_AsRadiusServerRowStatus_Object((1,3,6,1,4,1,890,1,5,1,1,29,1,5),_AsRadiusServerRowStatus_Type())
asRadiusServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:asRadiusServerRowStatus.setStatus(_A)
class _AsDot1xEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AsDot1xEnable_Type.__name__=_E
_AsDot1xEnable_Object=MibScalar
asDot1xEnable=_AsDot1xEnable_Object((1,3,6,1,4,1,890,1,5,1,1,30),_AsDot1xEnable_Type())
asDot1xEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:asDot1xEnable.setStatus(_A)
_AsDot1xPortTable_Object=MibTable
asDot1xPortTable=_AsDot1xPortTable_Object((1,3,6,1,4,1,890,1,5,1,1,31))
if mibBuilder.loadTexts:asDot1xPortTable.setStatus(_A)
_AsDot1xPortEntry_Object=MibTableRow
asDot1xPortEntry=_AsDot1xPortEntry_Object((1,3,6,1,4,1,890,1,5,1,1,31,1))
asDot1xPortEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:asDot1xPortEntry.setStatus(_A)
class _AsDot1xPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_AsDot1xPortEnable_Type.__name__=_E
_AsDot1xPortEnable_Object=MibTableColumn
asDot1xPortEnable=_AsDot1xPortEnable_Object((1,3,6,1,4,1,890,1,5,1,1,31,1,1),_AsDot1xPortEnable_Type())
asDot1xPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:asDot1xPortEnable.setStatus(_A)
class _AsDot1xPortControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('forceAuth',2),('forceUnAuth',3)))
_AsDot1xPortControl_Type.__name__=_E
_AsDot1xPortControl_Object=MibTableColumn
asDot1xPortControl=_AsDot1xPortControl_Object((1,3,6,1,4,1,890,1,5,1,1,31,1,2),_AsDot1xPortControl_Type())
asDot1xPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:asDot1xPortControl.setStatus(_A)
class _AsDot1xPortReAuthEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AsDot1xPortReAuthEnable_Type.__name__=_E
_AsDot1xPortReAuthEnable_Object=MibTableColumn
asDot1xPortReAuthEnable=_AsDot1xPortReAuthEnable_Object((1,3,6,1,4,1,890,1,5,1,1,31,1,3),_AsDot1xPortReAuthEnable_Type())
asDot1xPortReAuthEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:asDot1xPortReAuthEnable.setStatus(_A)
_AsDot1xPortReAuthPeriod_Type=Integer32
_AsDot1xPortReAuthPeriod_Object=MibTableColumn
asDot1xPortReAuthPeriod=_AsDot1xPortReAuthPeriod_Object((1,3,6,1,4,1,890,1,5,1,1,31,1,4),_AsDot1xPortReAuthPeriod_Type())
asDot1xPortReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:asDot1xPortReAuthPeriod.setStatus(_A)
_AccessSwitchStats_ObjectIdentity=ObjectIdentity
accessSwitchStats=_AccessSwitchStats_ObjectIdentity((1,3,6,1,4,1,890,1,5,1,2))
_AsMacStats_ObjectIdentity=ObjectIdentity
asMacStats=_AsMacStats_ObjectIdentity((1,3,6,1,4,1,890,1,5,1,2,1))
_AsMacDisplayTarget_Type=Integer32
_AsMacDisplayTarget_Object=MibScalar
asMacDisplayTarget=_AsMacDisplayTarget_Object((1,3,6,1,4,1,890,1,5,1,2,1,1),_AsMacDisplayTarget_Type())
asMacDisplayTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:asMacDisplayTarget.setStatus(_H)
_AsMacTable_Object=MibTable
asMacTable=_AsMacTable_Object((1,3,6,1,4,1,890,1,5,1,2,1,2))
if mibBuilder.loadTexts:asMacTable.setStatus(_H)
_AsMacEntry_Object=MibTableRow
asMacEntry=_AsMacEntry_Object((1,3,6,1,4,1,890,1,5,1,2,1,2,1))
asMacEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:asMacEntry.setStatus(_H)
_AsMacAddress_Type=MacAddress
_AsMacAddress_Object=MibTableColumn
asMacAddress=_AsMacAddress_Object((1,3,6,1,4,1,890,1,5,1,2,1,2,1,1),_AsMacAddress_Type())
asMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:asMacAddress.setStatus(_H)
_AsMacPort_Type=Integer32
_AsMacPort_Object=MibTableColumn
asMacPort=_AsMacPort_Object((1,3,6,1,4,1,890,1,5,1,2,1,2,1,2),_AsMacPort_Type())
asMacPort.setMaxAccess(_B)
if mibBuilder.loadTexts:asMacPort.setStatus(_H)
class _AsMacStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_AsMacStatus_Type.__name__=_E
_AsMacStatus_Object=MibTableColumn
asMacStatus=_AsMacStatus_Object((1,3,6,1,4,1,890,1,5,1,2,1,2,1,3),_AsMacStatus_Type())
asMacStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:asMacStatus.setStatus(_H)
reboot=NotificationType((1,3,6,1,4,1,890,1,5,0,1))
reboot.setObjects((_C,_F))
if mibBuilder.loadTexts:reboot.setStatus('')
systemShutdown=NotificationType((1,3,6,1,4,1,890,1,5,0,2))
systemShutdown.setObjects((_C,_F))
if mibBuilder.loadTexts:systemShutdown.setStatus('')
overheat=NotificationType((1,3,6,1,4,1,890,1,5,0,3))
overheat.setObjects(*((_C,_K),(_C,_P),(_C,_G)))
if mibBuilder.loadTexts:overheat.setStatus('')
overheatOver=NotificationType((1,3,6,1,4,1,890,1,5,0,4))
overheatOver.setObjects(*((_C,_K),(_C,_P),(_C,_G)))
if mibBuilder.loadTexts:overheatOver.setStatus('')
errLog=NotificationType((1,3,6,1,4,1,890,1,5,0,5))
errLog.setObjects((_C,_F))
if mibBuilder.loadTexts:errLog.setStatus('')
fanRpmLow=NotificationType((1,3,6,1,4,1,890,1,5,0,6))
fanRpmLow.setObjects(*((_C,_I),(_C,_Q),(_C,_G)))
if mibBuilder.loadTexts:fanRpmLow.setStatus('')
fanRpmNormal=NotificationType((1,3,6,1,4,1,890,1,5,0,7))
fanRpmNormal.setObjects(*((_C,_I),(_C,_Q),(_C,_G)))
if mibBuilder.loadTexts:fanRpmNormal.setStatus('')
voltageOutOfRange=NotificationType((1,3,6,1,4,1,890,1,5,0,8))
voltageOutOfRange.setObjects(*((_C,_J),(_C,_R),(_C,_G)))
if mibBuilder.loadTexts:voltageOutOfRange.setStatus('')
voltageNormal=NotificationType((1,3,6,1,4,1,890,1,5,0,9))
voltageNormal.setObjects(*((_C,_J),(_C,_R),(_C,_G)))
if mibBuilder.loadTexts:voltageNormal.setStatus('')
systemMaintenanceFailure=NotificationType((1,3,6,1,4,1,890,1,5,0,10))
systemMaintenanceFailure.setObjects((_C,_F))
if mibBuilder.loadTexts:systemMaintenanceFailure.setStatus('')
configChange=NotificationType((1,3,6,1,4,1,890,1,5,0,11))
configChange.setObjects((_C,_F))
if mibBuilder.loadTexts:configChange.setStatus('')
thermalSensorFailure=NotificationType((1,3,6,1,4,1,890,1,5,0,12))
thermalSensorFailure.setObjects((_C,_F))
if mibBuilder.loadTexts:thermalSensorFailure.setStatus('')
mibBuilder.exportSymbols(_C,**{'ASSlotNum':ASSlotNum,'ASModuleType':ASModuleType,'zyxel':zyxel,'products':products,'accessSwitch':accessSwitch,'reboot':reboot,'systemShutdown':systemShutdown,'overheat':overheat,'overheatOver':overheatOver,'errLog':errLog,'fanRpmLow':fanRpmLow,'fanRpmNormal':fanRpmNormal,'voltageOutOfRange':voltageOutOfRange,'voltageNormal':voltageNormal,'systemMaintenanceFailure':systemMaintenanceFailure,'configChange':configChange,'thermalSensorFailure':thermalSensorFailure,'accessSwitchCommon':accessSwitchCommon,'accessSwitchMgnt':accessSwitchMgnt,_G:accessSwitchSystemCurrentStatus,_F:accessSwitchProblemCause,'accessSwitchSystemTemperature':accessSwitchSystemTemperature,'accessSwitchFanRpmTable':accessSwitchFanRpmTable,'accessSwitchFanRpmEntry':accessSwitchFanRpmEntry,_I:accessSwitchFanRpmIndex,_Q:accessSwitchFanRpmCurValue,'accessSwitchFanRpmMaxValue':accessSwitchFanRpmMaxValue,'accessSwitchFanRpmMinValue':accessSwitchFanRpmMinValue,'accessSwitchFanRpmLowThresh':accessSwitchFanRpmLowThresh,'accessSwitchFanRpmDescr':accessSwitchFanRpmDescr,'accessSwitchVoltageTable':accessSwitchVoltageTable,'accessSwitchVoltageEntry':accessSwitchVoltageEntry,_J:accessSwitchVoltageIndex,_R:accessSwitchVoltageCurValue,'accessSwitchVoltageMaxValue':accessSwitchVoltageMaxValue,'accessSwitchVoltageMinValue':accessSwitchVoltageMinValue,'accessSwitchVoltageNominalValue':accessSwitchVoltageNominalValue,'accessSwitchVoltageLowThresh':accessSwitchVoltageLowThresh,'accessSwitchVoltageDescr':accessSwitchVoltageDescr,'accessSwitchSysTempTable':accessSwitchSysTempTable,'accessSwitchSysTempEntry':accessSwitchSysTempEntry,_K:accessSwitchSysTempIndex,_P:accessSwitchSysTempCurValue,'accessSwitchSysTempMaxValue':accessSwitchSysTempMaxValue,'accessSwitchSysTempMinValue':accessSwitchSysTempMinValue,'accessSwitchSysTempHighThresh':accessSwitchSysTempHighThresh,'accessSwitchSysTempDescr':accessSwitchSysTempDescr,'accessSwitchMaintenance':accessSwitchMaintenance,'accessSwitchMaintenancePort':accessSwitchMaintenancePort,'accessSwitchMaxNumOfStaticVlans':accessSwitchMaxNumOfStaticVlans,'acccessSwitchChassisId':acccessSwitchChassisId,'accessSwitchSlotId':accessSwitchSlotId,'accessSwitchModuleType':accessSwitchModuleType,'accessSwitchFWVersion':accessSwitchFWVersion,'accessSwitchDriverVersion':accessSwitchDriverVersion,'accessSwitchModemCodeVersion':accessSwitchModemCodeVersion,'accessSwitchDSLConfOps':accessSwitchDSLConfOps,'accessSwitchDSLConfTarget':accessSwitchDSLConfTarget,'accessSwitchDSLConfProfileName':accessSwitchDSLConfProfileName,'accessSwitchDSLConfMode':accessSwitchDSLConfMode,'asPacketForwardingTable':asPacketForwardingTable,'asPacketForwardingEntry':asPacketForwardingEntry,'asPacketForwardingPortList':asPacketForwardingPortList,'asDhcpRelayEnable':asDhcpRelayEnable,'asDhcpRelayOption82Enable':asDhcpRelayOption82Enable,'asDhcpRelayOption82Info':asDhcpRelayOption82Info,'asMaxNumOfDhcpServers':asMaxNumOfDhcpServers,'asDhcpServerTable':asDhcpServerTable,'asDhcpServerEntry':asDhcpServerEntry,_U:asDhcpServerIp,'asDhcpServerRowStatus':asDhcpServerRowStatus,'asMaxNumberOfRadiusServers':asMaxNumberOfRadiusServers,'asRadiusServerTable':asRadiusServerTable,'asRadiusServerEntry':asRadiusServerEntry,_V:asRadiusServerIndex,'asRadiusServerIp':asRadiusServerIp,'asRadiusServerPort':asRadiusServerPort,'asRadiusSharedSecret':asRadiusSharedSecret,'asRadiusServerRowStatus':asRadiusServerRowStatus,'asDot1xEnable':asDot1xEnable,'asDot1xPortTable':asDot1xPortTable,'asDot1xPortEntry':asDot1xPortEntry,'asDot1xPortEnable':asDot1xPortEnable,'asDot1xPortControl':asDot1xPortControl,'asDot1xPortReAuthEnable':asDot1xPortReAuthEnable,'asDot1xPortReAuthPeriod':asDot1xPortReAuthPeriod,'accessSwitchStats':accessSwitchStats,'asMacStats':asMacStats,'asMacDisplayTarget':asMacDisplayTarget,'asMacTable':asMacTable,'asMacEntry':asMacEntry,_W:asMacAddress,'asMacPort':asMacPort,'asMacStatus':asMacStatus})