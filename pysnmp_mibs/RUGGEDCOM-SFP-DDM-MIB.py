_v='rcSfpDdmAlarmTrap'
_u='rcSfpDdmWarningTrap'
_t='rcSfpDdmThreshTxPowerAlarmHigh'
_s='rcSfpDdmThreshTxPowerWarnHigh'
_r='rcSfpDdmThreshTxPowerWarnLow'
_q='rcSfpDdmThreshTxPowerAlarmLow'
_p='rcSfpDdmThreshRxPowerAlarmHigh'
_o='rcSfpDdmThreshRxPowerWarnHigh'
_n='rcSfpDdmThreshRxPowerWarnLow'
_m='rcSfpDdmThreshRxPowerAlarmLow'
_l='rcSfpDdmThreshTxBiasAlarmHigh'
_k='rcSfpDdmThreshTxBiasWarnHigh'
_j='rcSfpDdmThreshTxBiasWarnLow'
_i='rcSfpDdmThreshTxBiasAlarmLow'
_h='rcSfpDdmThreshVoltageAlarmHigh'
_g='rcSfpDdmThreshVoltageWarnHigh'
_f='rcSfpDdmThreshVoltageWarnLow'
_e='rcSfpDdmThreshVoltageAlarmLow'
_d='rcSfpDdmThreshTempAlarmHigh'
_c='rcSfpDdmThreshTempWarnHigh'
_b='rcSfpDdmThreshTempWarnLow'
_a='rcSfpDdmThreshTempAlarmLow'
_Z='rcSfpDdmCurrentStatus'
_Y='rcSfpDdmImplemented'
_X='rcSfpDdmLinkLength'
_W='rcSfpDdmWavelength'
_V='rcSfpDdmConnectorType'
_U='rcSfpDdmNominalBitrate'
_T='rcSfpDdmEncoding'
_S='rcSfpDdmVendorSerialNumber'
_R='rcSfpDdmVendorRevision'
_Q='rcSfpDdmVendorPartNumber'
_P='rcSfpDdmVendorName'
_O='rcSfpPlugged'
_N='rcSfpDdmPollingInterval'
_M='rcSfpDdmAlarmFlags'
_L='rcSfpDdmWarningFlags'
_K='Bits'
_J='rcSfpDdmCurrentTxPower'
_I='rcSfpDdmCurrentRxPower'
_H='rcSfpDdmCurrentTxBiasCurrent'
_G='rcSfpDdmCurrentVoltage'
_F='rcSfpDdmCurrentTemperature'
_E='rcSfpPortId'
_D='Integer32'
_C='read-only'
_B='current'
_A='RUGGEDCOM-SFP-DDM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,ruggedcomTraps=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt','ruggedcomTraps')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcSfpDdm=ModuleIdentity((1,3,6,1,4,1,15004,4,17))
class RcSfpDdmAlarmWarnStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notAvailable',1),('ok',2),('warning',3),('alarm',4)))
_RcSfpDdmGlobalConfig_ObjectIdentity=ObjectIdentity
rcSfpDdmGlobalConfig=_RcSfpDdmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,15004,4,17,1))
class _RcSfpDdmPollingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_RcSfpDdmPollingInterval_Type.__name__=_D
_RcSfpDdmPollingInterval_Object=MibScalar
rcSfpDdmPollingInterval=_RcSfpDdmPollingInterval_Object((1,3,6,1,4,1,15004,4,17,1,1),_RcSfpDdmPollingInterval_Type())
rcSfpDdmPollingInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:rcSfpDdmPollingInterval.setStatus(_B)
if mibBuilder.loadTexts:rcSfpDdmPollingInterval.setUnits('minutes')
_RcSfpDdmTables_ObjectIdentity=ObjectIdentity
rcSfpDdmTables=_RcSfpDdmTables_ObjectIdentity((1,3,6,1,4,1,15004,4,17,2))
_RcSfpDdmPortTable_Object=MibTable
rcSfpDdmPortTable=_RcSfpDdmPortTable_Object((1,3,6,1,4,1,15004,4,17,2,1))
if mibBuilder.loadTexts:rcSfpDdmPortTable.setStatus(_B)
_RcSfpDdmPortEntry_Object=MibTableRow
rcSfpDdmPortEntry=_RcSfpDdmPortEntry_Object((1,3,6,1,4,1,15004,4,17,2,1,1))
rcSfpDdmPortEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:rcSfpDdmPortEntry.setStatus(_B)
class _RcSfpPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcSfpPortId_Type.__name__=_D
_RcSfpPortId_Object=MibTableColumn
rcSfpPortId=_RcSfpPortId_Object((1,3,6,1,4,1,15004,4,17,2,1,1,1),_RcSfpPortId_Type())
rcSfpPortId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcSfpPortId.setStatus(_B)
_RcSfpPlugged_Type=TruthValue
_RcSfpPlugged_Object=MibTableColumn
rcSfpPlugged=_RcSfpPlugged_Object((1,3,6,1,4,1,15004,4,17,2,1,1,2),_RcSfpPlugged_Type())
rcSfpPlugged.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpPlugged.setStatus(_B)
_RcSfpDdmVendorName_Type=DisplayString
_RcSfpDdmVendorName_Object=MibTableColumn
rcSfpDdmVendorName=_RcSfpDdmVendorName_Object((1,3,6,1,4,1,15004,4,17,2,1,1,3),_RcSfpDdmVendorName_Type())
rcSfpDdmVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmVendorName.setStatus(_B)
_RcSfpDdmVendorPartNumber_Type=DisplayString
_RcSfpDdmVendorPartNumber_Object=MibTableColumn
rcSfpDdmVendorPartNumber=_RcSfpDdmVendorPartNumber_Object((1,3,6,1,4,1,15004,4,17,2,1,1,4),_RcSfpDdmVendorPartNumber_Type())
rcSfpDdmVendorPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmVendorPartNumber.setStatus(_B)
_RcSfpDdmVendorRevision_Type=DisplayString
_RcSfpDdmVendorRevision_Object=MibTableColumn
rcSfpDdmVendorRevision=_RcSfpDdmVendorRevision_Object((1,3,6,1,4,1,15004,4,17,2,1,1,5),_RcSfpDdmVendorRevision_Type())
rcSfpDdmVendorRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmVendorRevision.setStatus(_B)
_RcSfpDdmVendorSerialNumber_Type=DisplayString
_RcSfpDdmVendorSerialNumber_Object=MibTableColumn
rcSfpDdmVendorSerialNumber=_RcSfpDdmVendorSerialNumber_Object((1,3,6,1,4,1,15004,4,17,2,1,1,6),_RcSfpDdmVendorSerialNumber_Type())
rcSfpDdmVendorSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmVendorSerialNumber.setStatus(_B)
_RcSfpDdmEncoding_Type=DisplayString
_RcSfpDdmEncoding_Object=MibTableColumn
rcSfpDdmEncoding=_RcSfpDdmEncoding_Object((1,3,6,1,4,1,15004,4,17,2,1,1,7),_RcSfpDdmEncoding_Type())
rcSfpDdmEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmEncoding.setStatus(_B)
_RcSfpDdmNominalBitrate_Type=DisplayString
_RcSfpDdmNominalBitrate_Object=MibTableColumn
rcSfpDdmNominalBitrate=_RcSfpDdmNominalBitrate_Object((1,3,6,1,4,1,15004,4,17,2,1,1,8),_RcSfpDdmNominalBitrate_Type())
rcSfpDdmNominalBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmNominalBitrate.setStatus(_B)
_RcSfpDdmConnectorType_Type=DisplayString
_RcSfpDdmConnectorType_Object=MibTableColumn
rcSfpDdmConnectorType=_RcSfpDdmConnectorType_Object((1,3,6,1,4,1,15004,4,17,2,1,1,9),_RcSfpDdmConnectorType_Type())
rcSfpDdmConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmConnectorType.setStatus(_B)
_RcSfpDdmWavelength_Type=DisplayString
_RcSfpDdmWavelength_Object=MibTableColumn
rcSfpDdmWavelength=_RcSfpDdmWavelength_Object((1,3,6,1,4,1,15004,4,17,2,1,1,10),_RcSfpDdmWavelength_Type())
rcSfpDdmWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmWavelength.setStatus(_B)
_RcSfpDdmLinkLength_Type=DisplayString
_RcSfpDdmLinkLength_Object=MibTableColumn
rcSfpDdmLinkLength=_RcSfpDdmLinkLength_Object((1,3,6,1,4,1,15004,4,17,2,1,1,11),_RcSfpDdmLinkLength_Type())
rcSfpDdmLinkLength.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmLinkLength.setStatus(_B)
_RcSfpDdmImplemented_Type=TruthValue
_RcSfpDdmImplemented_Object=MibTableColumn
rcSfpDdmImplemented=_RcSfpDdmImplemented_Object((1,3,6,1,4,1,15004,4,17,2,1,1,12),_RcSfpDdmImplemented_Type())
rcSfpDdmImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmImplemented.setStatus(_B)
_RcSfpDdmCurrentStatus_Type=RcSfpDdmAlarmWarnStatus
_RcSfpDdmCurrentStatus_Object=MibTableColumn
rcSfpDdmCurrentStatus=_RcSfpDdmCurrentStatus_Object((1,3,6,1,4,1,15004,4,17,2,1,1,13),_RcSfpDdmCurrentStatus_Type())
rcSfpDdmCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentStatus.setStatus(_B)
class _RcSfpDdmCurrentTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,128000))
_RcSfpDdmCurrentTemperature_Type.__name__=_D
_RcSfpDdmCurrentTemperature_Object=MibTableColumn
rcSfpDdmCurrentTemperature=_RcSfpDdmCurrentTemperature_Object((1,3,6,1,4,1,15004,4,17,2,1,1,14),_RcSfpDdmCurrentTemperature_Type())
rcSfpDdmCurrentTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentTemperature.setStatus(_B)
class _RcSfpDdmThreshTempAlarmLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,128000))
_RcSfpDdmThreshTempAlarmLow_Type.__name__=_D
_RcSfpDdmThreshTempAlarmLow_Object=MibTableColumn
rcSfpDdmThreshTempAlarmLow=_RcSfpDdmThreshTempAlarmLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,15),_RcSfpDdmThreshTempAlarmLow_Type())
rcSfpDdmThreshTempAlarmLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTempAlarmLow.setStatus(_B)
class _RcSfpDdmThreshTempWarnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,128000))
_RcSfpDdmThreshTempWarnLow_Type.__name__=_D
_RcSfpDdmThreshTempWarnLow_Object=MibTableColumn
rcSfpDdmThreshTempWarnLow=_RcSfpDdmThreshTempWarnLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,16),_RcSfpDdmThreshTempWarnLow_Type())
rcSfpDdmThreshTempWarnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTempWarnLow.setStatus(_B)
class _RcSfpDdmThreshTempWarnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,128000))
_RcSfpDdmThreshTempWarnHigh_Type.__name__=_D
_RcSfpDdmThreshTempWarnHigh_Object=MibTableColumn
rcSfpDdmThreshTempWarnHigh=_RcSfpDdmThreshTempWarnHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,17),_RcSfpDdmThreshTempWarnHigh_Type())
rcSfpDdmThreshTempWarnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTempWarnHigh.setStatus(_B)
class _RcSfpDdmThreshTempAlarmHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128000,128000))
_RcSfpDdmThreshTempAlarmHigh_Type.__name__=_D
_RcSfpDdmThreshTempAlarmHigh_Object=MibTableColumn
rcSfpDdmThreshTempAlarmHigh=_RcSfpDdmThreshTempAlarmHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,18),_RcSfpDdmThreshTempAlarmHigh_Type())
rcSfpDdmThreshTempAlarmHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTempAlarmHigh.setStatus(_B)
class _RcSfpDdmCurrentVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmCurrentVoltage_Type.__name__=_D
_RcSfpDdmCurrentVoltage_Object=MibTableColumn
rcSfpDdmCurrentVoltage=_RcSfpDdmCurrentVoltage_Object((1,3,6,1,4,1,15004,4,17,2,1,1,19),_RcSfpDdmCurrentVoltage_Type())
rcSfpDdmCurrentVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentVoltage.setStatus(_B)
class _RcSfpDdmThreshVoltageAlarmLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshVoltageAlarmLow_Type.__name__=_D
_RcSfpDdmThreshVoltageAlarmLow_Object=MibTableColumn
rcSfpDdmThreshVoltageAlarmLow=_RcSfpDdmThreshVoltageAlarmLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,20),_RcSfpDdmThreshVoltageAlarmLow_Type())
rcSfpDdmThreshVoltageAlarmLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshVoltageAlarmLow.setStatus(_B)
class _RcSfpDdmThreshVoltageWarnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshVoltageWarnLow_Type.__name__=_D
_RcSfpDdmThreshVoltageWarnLow_Object=MibTableColumn
rcSfpDdmThreshVoltageWarnLow=_RcSfpDdmThreshVoltageWarnLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,21),_RcSfpDdmThreshVoltageWarnLow_Type())
rcSfpDdmThreshVoltageWarnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshVoltageWarnLow.setStatus(_B)
class _RcSfpDdmThreshVoltageWarnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshVoltageWarnHigh_Type.__name__=_D
_RcSfpDdmThreshVoltageWarnHigh_Object=MibTableColumn
rcSfpDdmThreshVoltageWarnHigh=_RcSfpDdmThreshVoltageWarnHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,22),_RcSfpDdmThreshVoltageWarnHigh_Type())
rcSfpDdmThreshVoltageWarnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshVoltageWarnHigh.setStatus(_B)
class _RcSfpDdmThreshVoltageAlarmHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshVoltageAlarmHigh_Type.__name__=_D
_RcSfpDdmThreshVoltageAlarmHigh_Object=MibTableColumn
rcSfpDdmThreshVoltageAlarmHigh=_RcSfpDdmThreshVoltageAlarmHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,23),_RcSfpDdmThreshVoltageAlarmHigh_Type())
rcSfpDdmThreshVoltageAlarmHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshVoltageAlarmHigh.setStatus(_B)
class _RcSfpDdmCurrentTxBiasCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131070))
_RcSfpDdmCurrentTxBiasCurrent_Type.__name__=_D
_RcSfpDdmCurrentTxBiasCurrent_Object=MibTableColumn
rcSfpDdmCurrentTxBiasCurrent=_RcSfpDdmCurrentTxBiasCurrent_Object((1,3,6,1,4,1,15004,4,17,2,1,1,24),_RcSfpDdmCurrentTxBiasCurrent_Type())
rcSfpDdmCurrentTxBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentTxBiasCurrent.setStatus(_B)
class _RcSfpDdmThreshTxBiasAlarmLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131070))
_RcSfpDdmThreshTxBiasAlarmLow_Type.__name__=_D
_RcSfpDdmThreshTxBiasAlarmLow_Object=MibTableColumn
rcSfpDdmThreshTxBiasAlarmLow=_RcSfpDdmThreshTxBiasAlarmLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,25),_RcSfpDdmThreshTxBiasAlarmLow_Type())
rcSfpDdmThreshTxBiasAlarmLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxBiasAlarmLow.setStatus(_B)
class _RcSfpDdmThreshTxBiasWarnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131070))
_RcSfpDdmThreshTxBiasWarnLow_Type.__name__=_D
_RcSfpDdmThreshTxBiasWarnLow_Object=MibTableColumn
rcSfpDdmThreshTxBiasWarnLow=_RcSfpDdmThreshTxBiasWarnLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,26),_RcSfpDdmThreshTxBiasWarnLow_Type())
rcSfpDdmThreshTxBiasWarnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxBiasWarnLow.setStatus(_B)
class _RcSfpDdmThreshTxBiasWarnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131070))
_RcSfpDdmThreshTxBiasWarnHigh_Type.__name__=_D
_RcSfpDdmThreshTxBiasWarnHigh_Object=MibTableColumn
rcSfpDdmThreshTxBiasWarnHigh=_RcSfpDdmThreshTxBiasWarnHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,27),_RcSfpDdmThreshTxBiasWarnHigh_Type())
rcSfpDdmThreshTxBiasWarnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxBiasWarnHigh.setStatus(_B)
class _RcSfpDdmThreshTxBiasAlarmHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131070))
_RcSfpDdmThreshTxBiasAlarmHigh_Type.__name__=_D
_RcSfpDdmThreshTxBiasAlarmHigh_Object=MibTableColumn
rcSfpDdmThreshTxBiasAlarmHigh=_RcSfpDdmThreshTxBiasAlarmHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,28),_RcSfpDdmThreshTxBiasAlarmHigh_Type())
rcSfpDdmThreshTxBiasAlarmHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxBiasAlarmHigh.setStatus(_B)
class _RcSfpDdmCurrentRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553500))
_RcSfpDdmCurrentRxPower_Type.__name__=_D
_RcSfpDdmCurrentRxPower_Object=MibTableColumn
rcSfpDdmCurrentRxPower=_RcSfpDdmCurrentRxPower_Object((1,3,6,1,4,1,15004,4,17,2,1,1,29),_RcSfpDdmCurrentRxPower_Type())
rcSfpDdmCurrentRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentRxPower.setStatus(_B)
class _RcSfpDdmThreshRxPowerAlarmLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553500))
_RcSfpDdmThreshRxPowerAlarmLow_Type.__name__=_D
_RcSfpDdmThreshRxPowerAlarmLow_Object=MibTableColumn
rcSfpDdmThreshRxPowerAlarmLow=_RcSfpDdmThreshRxPowerAlarmLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,30),_RcSfpDdmThreshRxPowerAlarmLow_Type())
rcSfpDdmThreshRxPowerAlarmLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshRxPowerAlarmLow.setStatus(_B)
class _RcSfpDdmThreshRxPowerWarnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553500))
_RcSfpDdmThreshRxPowerWarnLow_Type.__name__=_D
_RcSfpDdmThreshRxPowerWarnLow_Object=MibTableColumn
rcSfpDdmThreshRxPowerWarnLow=_RcSfpDdmThreshRxPowerWarnLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,31),_RcSfpDdmThreshRxPowerWarnLow_Type())
rcSfpDdmThreshRxPowerWarnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshRxPowerWarnLow.setStatus(_B)
class _RcSfpDdmThreshRxPowerWarnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553500))
_RcSfpDdmThreshRxPowerWarnHigh_Type.__name__=_D
_RcSfpDdmThreshRxPowerWarnHigh_Object=MibTableColumn
rcSfpDdmThreshRxPowerWarnHigh=_RcSfpDdmThreshRxPowerWarnHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,32),_RcSfpDdmThreshRxPowerWarnHigh_Type())
rcSfpDdmThreshRxPowerWarnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshRxPowerWarnHigh.setStatus(_B)
class _RcSfpDdmThreshRxPowerAlarmHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6553500))
_RcSfpDdmThreshRxPowerAlarmHigh_Type.__name__=_D
_RcSfpDdmThreshRxPowerAlarmHigh_Object=MibTableColumn
rcSfpDdmThreshRxPowerAlarmHigh=_RcSfpDdmThreshRxPowerAlarmHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,33),_RcSfpDdmThreshRxPowerAlarmHigh_Type())
rcSfpDdmThreshRxPowerAlarmHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshRxPowerAlarmHigh.setStatus(_B)
class _RcSfpDdmCurrentTxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmCurrentTxPower_Type.__name__=_D
_RcSfpDdmCurrentTxPower_Object=MibTableColumn
rcSfpDdmCurrentTxPower=_RcSfpDdmCurrentTxPower_Object((1,3,6,1,4,1,15004,4,17,2,1,1,34),_RcSfpDdmCurrentTxPower_Type())
rcSfpDdmCurrentTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmCurrentTxPower.setStatus(_B)
class _RcSfpDdmThreshTxPowerAlarmLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshTxPowerAlarmLow_Type.__name__=_D
_RcSfpDdmThreshTxPowerAlarmLow_Object=MibTableColumn
rcSfpDdmThreshTxPowerAlarmLow=_RcSfpDdmThreshTxPowerAlarmLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,35),_RcSfpDdmThreshTxPowerAlarmLow_Type())
rcSfpDdmThreshTxPowerAlarmLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxPowerAlarmLow.setStatus(_B)
class _RcSfpDdmThreshTxPowerWarnLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshTxPowerWarnLow_Type.__name__=_D
_RcSfpDdmThreshTxPowerWarnLow_Object=MibTableColumn
rcSfpDdmThreshTxPowerWarnLow=_RcSfpDdmThreshTxPowerWarnLow_Object((1,3,6,1,4,1,15004,4,17,2,1,1,36),_RcSfpDdmThreshTxPowerWarnLow_Type())
rcSfpDdmThreshTxPowerWarnLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxPowerWarnLow.setStatus(_B)
class _RcSfpDdmThreshTxPowerWarnHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshTxPowerWarnHigh_Type.__name__=_D
_RcSfpDdmThreshTxPowerWarnHigh_Object=MibTableColumn
rcSfpDdmThreshTxPowerWarnHigh=_RcSfpDdmThreshTxPowerWarnHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,37),_RcSfpDdmThreshTxPowerWarnHigh_Type())
rcSfpDdmThreshTxPowerWarnHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxPowerWarnHigh.setStatus(_B)
class _RcSfpDdmThreshTxPowerAlarmHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6554))
_RcSfpDdmThreshTxPowerAlarmHigh_Type.__name__=_D
_RcSfpDdmThreshTxPowerAlarmHigh_Object=MibTableColumn
rcSfpDdmThreshTxPowerAlarmHigh=_RcSfpDdmThreshTxPowerAlarmHigh_Object((1,3,6,1,4,1,15004,4,17,2,1,1,38),_RcSfpDdmThreshTxPowerAlarmHigh_Type())
rcSfpDdmThreshTxPowerAlarmHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmThreshTxPowerAlarmHigh.setStatus(_B)
class _RcSfpDdmWarningFlags_Type(Bits):namedValues=NamedValues(*(('tempHighWarning',0),('tempLowWarning',1),('vccHighWarning',2),('vccLowWarning',3),('txbiasHighWarning',4),('txbiasLowWarning',5),('rxpowerHighWarning',6),('rxpowerLowWarning',7),('txpowerHighWarning',8),('txpowerLowWarning',9)))
_RcSfpDdmWarningFlags_Type.__name__=_K
_RcSfpDdmWarningFlags_Object=MibTableColumn
rcSfpDdmWarningFlags=_RcSfpDdmWarningFlags_Object((1,3,6,1,4,1,15004,4,17,2,1,1,39),_RcSfpDdmWarningFlags_Type())
rcSfpDdmWarningFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmWarningFlags.setStatus(_B)
class _RcSfpDdmAlarmFlags_Type(Bits):namedValues=NamedValues(*(('tempHighAlarm',0),('tempLowAlarm',1),('vccHighAlarm',2),('vccLowAlarm',3),('txbiasHighAlarm',4),('txbiasLowAlarm',5),('rxpowerHighAlarm',6),('rxpowerLowAlarm',7),('txpowerHighAlarm',8),('txpowerLowAlarm',9)))
_RcSfpDdmAlarmFlags_Type.__name__=_K
_RcSfpDdmAlarmFlags_Object=MibTableColumn
rcSfpDdmAlarmFlags=_RcSfpDdmAlarmFlags_Object((1,3,6,1,4,1,15004,4,17,2,1,1,40),_RcSfpDdmAlarmFlags_Type())
rcSfpDdmAlarmFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:rcSfpDdmAlarmFlags.setStatus(_B)
_RcSfpDdmConformance_ObjectIdentity=ObjectIdentity
rcSfpDdmConformance=_RcSfpDdmConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,17,3))
_RcSfpDdmGroups_ObjectIdentity=ObjectIdentity
rcSfpDdmGroups=_RcSfpDdmGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,17,3,2))
_RuggedcomSfpDdmTraps_ObjectIdentity=ObjectIdentity
ruggedcomSfpDdmTraps=_RuggedcomSfpDdmTraps_ObjectIdentity((1,3,6,1,4,1,15004,5,52))
rcSfpDdmCfgGroup=ObjectGroup((1,3,6,1,4,1,15004,4,17,3,2,1))
rcSfpDdmCfgGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:rcSfpDdmCfgGroup.setStatus(_B)
rcSfpDdmTableGroup=ObjectGroup((1,3,6,1,4,1,15004,4,17,3,2,2))
rcSfpDdmTableGroup.setObjects(*((_A,_E),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_F),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_G),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_H),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_I),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_J),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:rcSfpDdmTableGroup.setStatus(_B)
rcSfpDdmNotifyGroup=ObjectGroup((1,3,6,1,4,1,15004,4,17,3,2,3))
rcSfpDdmNotifyGroup.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:rcSfpDdmNotifyGroup.setStatus(_B)
rcSfpDdmWarningTrap=NotificationType((1,3,6,1,4,1,15004,5,52,1))
rcSfpDdmWarningTrap.setObjects(*((_A,_E),(_A,_L),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rcSfpDdmWarningTrap.setStatus(_B)
rcSfpDdmAlarmTrap=NotificationType((1,3,6,1,4,1,15004,5,52,2))
rcSfpDdmAlarmTrap.setObjects(*((_A,_E),(_A,_M),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rcSfpDdmAlarmTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RcSfpDdmAlarmWarnStatus':RcSfpDdmAlarmWarnStatus,'rcSfpDdm':rcSfpDdm,'rcSfpDdmGlobalConfig':rcSfpDdmGlobalConfig,_N:rcSfpDdmPollingInterval,'rcSfpDdmTables':rcSfpDdmTables,'rcSfpDdmPortTable':rcSfpDdmPortTable,'rcSfpDdmPortEntry':rcSfpDdmPortEntry,_E:rcSfpPortId,_O:rcSfpPlugged,_P:rcSfpDdmVendorName,_Q:rcSfpDdmVendorPartNumber,_R:rcSfpDdmVendorRevision,_S:rcSfpDdmVendorSerialNumber,_T:rcSfpDdmEncoding,_U:rcSfpDdmNominalBitrate,_V:rcSfpDdmConnectorType,_W:rcSfpDdmWavelength,_X:rcSfpDdmLinkLength,_Y:rcSfpDdmImplemented,_Z:rcSfpDdmCurrentStatus,_F:rcSfpDdmCurrentTemperature,_a:rcSfpDdmThreshTempAlarmLow,_b:rcSfpDdmThreshTempWarnLow,_c:rcSfpDdmThreshTempWarnHigh,_d:rcSfpDdmThreshTempAlarmHigh,_G:rcSfpDdmCurrentVoltage,_e:rcSfpDdmThreshVoltageAlarmLow,_f:rcSfpDdmThreshVoltageWarnLow,_g:rcSfpDdmThreshVoltageWarnHigh,_h:rcSfpDdmThreshVoltageAlarmHigh,_H:rcSfpDdmCurrentTxBiasCurrent,_i:rcSfpDdmThreshTxBiasAlarmLow,_j:rcSfpDdmThreshTxBiasWarnLow,_k:rcSfpDdmThreshTxBiasWarnHigh,_l:rcSfpDdmThreshTxBiasAlarmHigh,_I:rcSfpDdmCurrentRxPower,_m:rcSfpDdmThreshRxPowerAlarmLow,_n:rcSfpDdmThreshRxPowerWarnLow,_o:rcSfpDdmThreshRxPowerWarnHigh,_p:rcSfpDdmThreshRxPowerAlarmHigh,_J:rcSfpDdmCurrentTxPower,_q:rcSfpDdmThreshTxPowerAlarmLow,_r:rcSfpDdmThreshTxPowerWarnLow,_s:rcSfpDdmThreshTxPowerWarnHigh,_t:rcSfpDdmThreshTxPowerAlarmHigh,_L:rcSfpDdmWarningFlags,_M:rcSfpDdmAlarmFlags,'rcSfpDdmConformance':rcSfpDdmConformance,'rcSfpDdmGroups':rcSfpDdmGroups,'rcSfpDdmCfgGroup':rcSfpDdmCfgGroup,'rcSfpDdmTableGroup':rcSfpDdmTableGroup,'rcSfpDdmNotifyGroup':rcSfpDdmNotifyGroup,'ruggedcomSfpDdmTraps':ruggedcomSfpDdmTraps,_u:rcSfpDdmWarningTrap,_v:rcSfpDdmAlarmTrap})