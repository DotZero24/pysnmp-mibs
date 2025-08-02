_AW='cienaWsXcvrGroup'
_AV='cwsXcvrXcvrProfilePropertiesSerdesRxEmphasis'
_AU='cwsXcvrXcvrProfilePropertiesSerdesRxAmplitude'
_AT='cwsXcvrXcvrProfilePropertiesSerdesTxEq'
_AS='cwsXcvrXcvrProfileIdVendorRev'
_AR='cwsXcvrXcvrProfileIdVendorPn'
_AQ='cwsXcvrXcvrProfileIdVendorOui'
_AP='cwsXcvrXcvrProfileIdVendorName'
_AO='cwsXcvrTxPowerThresholdLowWarningThreshold'
_AN='cwsXcvrTxPowerThresholdHighWarningThreshold'
_AM='cwsXcvrTxPowerThresholdLowAlarmThreshold'
_AL='cwsXcvrTxPowerThresholdHighAlarmThreshold'
_AK='cwsXcvrTxPowerStatusLowWarningStatus'
_AJ='cwsXcvrTxPowerStatusHighWarningStatus'
_AI='cwsXcvrTxPowerStatusLowAlarmStatus'
_AH='cwsXcvrTxPowerStatusHighAlarmStatus'
_AG='cwsXcvrChannelTxPowerActual'
_AF='cwsXcvrRxPowerThresholdLowWarningThreshold'
_AE='cwsXcvrRxPowerThresholdHighWarningThreshold'
_AD='cwsXcvrRxPowerThresholdLowAlarmThreshold'
_AC='cwsXcvrRxPowerThresholdHighAlarmThreshold'
_AB='cwsXcvrRxPowerStatusLowWarningStatus'
_AA='cwsXcvrRxPowerStatusHighWarningStatus'
_A9='cwsXcvrRxPowerStatusLowAlarmStatus'
_A8='cwsXcvrRxPowerStatusHighAlarmStatus'
_A7='cwsXcvrChannelRxPowerActual'
_A6='cwsXcvrTemperatureThresholdLowWarningThreshold'
_A5='cwsXcvrTemperatureThresholdHighWarningThreshold'
_A4='cwsXcvrTemperatureThresholdLowAlarmThreshold'
_A3='cwsXcvrTemperatureThresholdHighAlarmThreshold'
_A2='cwsXcvrTemperatureStatusLowWarningStatus'
_A1='cwsXcvrTemperatureStatusHighWarningStatus'
_A0='cwsXcvrTemperatureStatusLowAlarmStatus'
_z='cwsXcvrTemperatureStatusHighAlarmStatus'
_y='cwsXcvrTemperatureActual'
_x='cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement'
_w='cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement'
_v='cwsXcvrVendorTransmitterNominalBitRate'
_u='cwsXcvrDeviceIdConnectorType'
_t='cwsXcvrVendorIdManufacturedDate'
_s='cwsXcvrVendorIdSerialNumber'
_r='cwsXcvrVendorIdRevision'
_q='cwsXcvrVendorIdPartNumber'
_p='cwsXcvrVendorIdName'
_o='cwsXcvrCienaIdDescription'
_n='cwsXcvrCienaIdRevision'
_m='cwsXcvrCienaIdCienaItemNumber'
_l='cwsXcvrXcvrPropertiesNumberOfChannels'
_k='cwsXcvrXcvrPropertiesMode'
_j='cwsXcvrXcvrPropertiesType'
_i='cwsXcvrXcvrStatePowerState'
_h='cwsXcvrXcvrStateOperationalState'
_g='cwsXcvrXcvrStateAdminState'
_f='cwsXcvrXcvrIdDescription'
_e='cwsXcvrXcvrIdName'
_d='cwsXcvrXcvrProfilePropertiesTableSnmpKey'
_c='cwsXcvrXcvrProfileIdTableSnmpKey'
_b='cwsXcvrTxPowerThresholdTableSnmpKey'
_a='cwsXcvrTxPowerStatusTableSnmpKey'
_Z='cwsXcvrChannelTxPowerTableSnmpKey'
_Y='cwsXcvrRxPowerThresholdTableSnmpKey'
_X='cwsXcvrRxPowerStatusTableSnmpKey'
_W='cwsXcvrChannelRxPowerTableSnmpKey'
_V='cwsXcvrTemperatureThresholdTableSnmpKey'
_U='cwsXcvrTemperatureStatusTableSnmpKey'
_T='cwsXcvrTemperatureTableSnmpKey'
_S='cwsXcvrVendorDiagnosticMonitoringTableSnmpKey'
_R='cwsXcvrVendorTransmitterTableSnmpKey'
_Q='cwsXcvrDeviceIdTableSnmpKey'
_P='cwsXcvrVendorIdTableSnmpKey'
_O='cwsXcvrCienaIdTableSnmpKey'
_N='cwsXcvrChildPtpIdTableSnmpKey'
_M='cwsXcvrXcvrStateTableSnmpKey'
_L='cwsXcvrXcvrIdTableSnmpKey'
_K='cwsXcvrXcvrPropertiesTableSnmpKey'
_J='cwsXcvrXcvrProfilesXcvrProfileIndex'
_I='OctetString'
_H='cwsXcvrChannelDiagnosticsChannelNumber'
_G='read-write'
_F='not-accessible'
_E='cwsXcvrXcvrsXcvrIndex'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-XCVR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
ChannelsNumber,ConnectorTypeDescEnum,Decimal1Dig,EnabledDisabledEnum,NameString,PtpId,StringMaxl128,StringMaxl16,StringMaxl254,StringMaxl32,XcvrId,XcvrMode,XcvrProfileId,XcvrSerdesRxAmplitude,XcvrSerdesRxEmphasis,XcvrSerdesTxEq,XcvrType=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','ChannelsNumber','ConnectorTypeDescEnum','Decimal1Dig','EnabledDisabledEnum','NameString','PtpId','StringMaxl128','StringMaxl16','StringMaxl254','StringMaxl32','XcvrId','XcvrMode','XcvrProfileId','XcvrSerdesRxAmplitude','XcvrSerdesRxEmphasis','XcvrSerdesTxEq','XcvrType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsXcvrMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,15))
if mibBuilder.loadTexts:cienaWsXcvrMIB.setRevisions(('2017-07-24 00:00','2017-03-02 00:00','2016-12-12 00:00','2016-06-14 00:00','2015-02-25 00:00'))
class XcvrOpEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('empty',0),('up',1),('down',2),('uncertified',3),('lowpowermode',4),('unknown',5)))
_CienaWsXcvrObjects_ObjectIdentity=ObjectIdentity
cienaWsXcvrObjects=_CienaWsXcvrObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,15,1))
_CienaWsXcvrConformance_ObjectIdentity=ObjectIdentity
cienaWsXcvrConformance=_CienaWsXcvrConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,15,2))
_CienaWsXcvrGroups_ObjectIdentity=ObjectIdentity
cienaWsXcvrGroups=_CienaWsXcvrGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,15,2,1))
_CienaWsXcvrCompliances_ObjectIdentity=ObjectIdentity
cienaWsXcvrCompliances=_CienaWsXcvrCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,15,2,2))
_CwsXcvrXcvrsTable_Object=MibTable
cwsXcvrXcvrsTable=_CwsXcvrXcvrsTable_Object((1,3,6,1,4,1,1271,3,4,15,3))
if mibBuilder.loadTexts:cwsXcvrXcvrsTable.setStatus(_A)
_CwsXcvrXcvrsEntry_Object=MibTableRow
cwsXcvrXcvrsEntry=_CwsXcvrXcvrsEntry_Object((1,3,6,1,4,1,1271,3,4,15,3,1))
cwsXcvrXcvrsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cwsXcvrXcvrsEntry.setStatus(_A)
class _CwsXcvrXcvrsXcvrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrsXcvrIndex_Type.__name__=_D
_CwsXcvrXcvrsXcvrIndex_Object=MibTableColumn
cwsXcvrXcvrsXcvrIndex=_CwsXcvrXcvrsXcvrIndex_Object((1,3,6,1,4,1,1271,3,4,15,3,1,1),_CwsXcvrXcvrsXcvrIndex_Type())
cwsXcvrXcvrsXcvrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrsXcvrIndex.setStatus(_A)
_CwsXcvrXcvrIdTable_Object=MibTable
cwsXcvrXcvrIdTable=_CwsXcvrXcvrIdTable_Object((1,3,6,1,4,1,1271,3,4,15,4))
if mibBuilder.loadTexts:cwsXcvrXcvrIdTable.setStatus(_A)
_CwsXcvrXcvrIdEntry_Object=MibTableRow
cwsXcvrXcvrIdEntry=_CwsXcvrXcvrIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,4,1))
cwsXcvrXcvrIdEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:cwsXcvrXcvrIdEntry.setStatus(_A)
class _CwsXcvrXcvrIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrIdTableSnmpKey_Type.__name__=_D
_CwsXcvrXcvrIdTableSnmpKey_Object=MibTableColumn
cwsXcvrXcvrIdTableSnmpKey=_CwsXcvrXcvrIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,4,1,1),_CwsXcvrXcvrIdTableSnmpKey_Type())
cwsXcvrXcvrIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrXcvrIdTableSnmpKey.setStatus(_A)
_CwsXcvrXcvrIdName_Type=NameString
_CwsXcvrXcvrIdName_Object=MibTableColumn
cwsXcvrXcvrIdName=_CwsXcvrXcvrIdName_Object((1,3,6,1,4,1,1271,3,4,15,4,1,2),_CwsXcvrXcvrIdName_Type())
cwsXcvrXcvrIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrIdName.setStatus(_A)
_CwsXcvrXcvrIdDescription_Type=StringMaxl128
_CwsXcvrXcvrIdDescription_Object=MibTableColumn
cwsXcvrXcvrIdDescription=_CwsXcvrXcvrIdDescription_Object((1,3,6,1,4,1,1271,3,4,15,4,1,3),_CwsXcvrXcvrIdDescription_Type())
cwsXcvrXcvrIdDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrIdDescription.setStatus(_A)
_CwsXcvrXcvrStateTable_Object=MibTable
cwsXcvrXcvrStateTable=_CwsXcvrXcvrStateTable_Object((1,3,6,1,4,1,1271,3,4,15,5))
if mibBuilder.loadTexts:cwsXcvrXcvrStateTable.setStatus(_A)
_CwsXcvrXcvrStateEntry_Object=MibTableRow
cwsXcvrXcvrStateEntry=_CwsXcvrXcvrStateEntry_Object((1,3,6,1,4,1,1271,3,4,15,5,1))
cwsXcvrXcvrStateEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:cwsXcvrXcvrStateEntry.setStatus(_A)
class _CwsXcvrXcvrStateTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrStateTableSnmpKey_Type.__name__=_D
_CwsXcvrXcvrStateTableSnmpKey_Object=MibTableColumn
cwsXcvrXcvrStateTableSnmpKey=_CwsXcvrXcvrStateTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,5,1,1),_CwsXcvrXcvrStateTableSnmpKey_Type())
cwsXcvrXcvrStateTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrXcvrStateTableSnmpKey.setStatus(_A)
_CwsXcvrXcvrStateAdminState_Type=EnabledDisabledEnum
_CwsXcvrXcvrStateAdminState_Object=MibTableColumn
cwsXcvrXcvrStateAdminState=_CwsXcvrXcvrStateAdminState_Object((1,3,6,1,4,1,1271,3,4,15,5,1,2),_CwsXcvrXcvrStateAdminState_Type())
cwsXcvrXcvrStateAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrStateAdminState.setStatus(_A)
_CwsXcvrXcvrStateOperationalState_Type=XcvrOpEnum
_CwsXcvrXcvrStateOperationalState_Object=MibTableColumn
cwsXcvrXcvrStateOperationalState=_CwsXcvrXcvrStateOperationalState_Object((1,3,6,1,4,1,1271,3,4,15,5,1,3),_CwsXcvrXcvrStateOperationalState_Type())
cwsXcvrXcvrStateOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrStateOperationalState.setStatus(_A)
class _CwsXcvrXcvrStatePowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('low',1)))
_CwsXcvrXcvrStatePowerState_Type.__name__=_D
_CwsXcvrXcvrStatePowerState_Object=MibTableColumn
cwsXcvrXcvrStatePowerState=_CwsXcvrXcvrStatePowerState_Object((1,3,6,1,4,1,1271,3,4,15,5,1,4),_CwsXcvrXcvrStatePowerState_Type())
cwsXcvrXcvrStatePowerState.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrStatePowerState.setStatus(_A)
_CwsXcvrXcvrPropertiesTable_Object=MibTable
cwsXcvrXcvrPropertiesTable=_CwsXcvrXcvrPropertiesTable_Object((1,3,6,1,4,1,1271,3,4,15,6))
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesTable.setStatus(_A)
_CwsXcvrXcvrPropertiesEntry_Object=MibTableRow
cwsXcvrXcvrPropertiesEntry=_CwsXcvrXcvrPropertiesEntry_Object((1,3,6,1,4,1,1271,3,4,15,6,1))
cwsXcvrXcvrPropertiesEntry.setIndexNames((0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesEntry.setStatus(_A)
class _CwsXcvrXcvrPropertiesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrPropertiesTableSnmpKey_Type.__name__=_D
_CwsXcvrXcvrPropertiesTableSnmpKey_Object=MibTableColumn
cwsXcvrXcvrPropertiesTableSnmpKey=_CwsXcvrXcvrPropertiesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,6,1,1),_CwsXcvrXcvrPropertiesTableSnmpKey_Type())
cwsXcvrXcvrPropertiesTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesTableSnmpKey.setStatus(_A)
_CwsXcvrXcvrPropertiesType_Type=XcvrType
_CwsXcvrXcvrPropertiesType_Object=MibTableColumn
cwsXcvrXcvrPropertiesType=_CwsXcvrXcvrPropertiesType_Object((1,3,6,1,4,1,1271,3,4,15,6,1,2),_CwsXcvrXcvrPropertiesType_Type())
cwsXcvrXcvrPropertiesType.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesType.setStatus(_A)
_CwsXcvrXcvrPropertiesMode_Type=XcvrMode
_CwsXcvrXcvrPropertiesMode_Object=MibTableColumn
cwsXcvrXcvrPropertiesMode=_CwsXcvrXcvrPropertiesMode_Object((1,3,6,1,4,1,1271,3,4,15,6,1,3),_CwsXcvrXcvrPropertiesMode_Type())
cwsXcvrXcvrPropertiesMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesMode.setStatus(_A)
_CwsXcvrXcvrPropertiesNumberOfChannels_Type=ChannelsNumber
_CwsXcvrXcvrPropertiesNumberOfChannels_Object=MibTableColumn
cwsXcvrXcvrPropertiesNumberOfChannels=_CwsXcvrXcvrPropertiesNumberOfChannels_Object((1,3,6,1,4,1,1271,3,4,15,6,1,4),_CwsXcvrXcvrPropertiesNumberOfChannels_Type())
cwsXcvrXcvrPropertiesNumberOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrPropertiesNumberOfChannels.setStatus(_A)
_CwsXcvrChildPtpIdTable_Object=MibTable
cwsXcvrChildPtpIdTable=_CwsXcvrChildPtpIdTable_Object((1,3,6,1,4,1,1271,3,4,15,7))
if mibBuilder.loadTexts:cwsXcvrChildPtpIdTable.setStatus(_A)
_CwsXcvrChildPtpIdEntry_Object=MibTableRow
cwsXcvrChildPtpIdEntry=_CwsXcvrChildPtpIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,7,1))
cwsXcvrChildPtpIdEntry.setIndexNames((0,_B,_E),(0,_B,_K),(0,_B,_N))
if mibBuilder.loadTexts:cwsXcvrChildPtpIdEntry.setStatus(_A)
class _CwsXcvrChildPtpIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrChildPtpIdTableSnmpKey_Type.__name__=_D
_CwsXcvrChildPtpIdTableSnmpKey_Object=MibTableColumn
cwsXcvrChildPtpIdTableSnmpKey=_CwsXcvrChildPtpIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,7,1,1),_CwsXcvrChildPtpIdTableSnmpKey_Type())
cwsXcvrChildPtpIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrChildPtpIdTableSnmpKey.setStatus(_A)
_CwsXcvrChildPtpId_Type=PtpId
_CwsXcvrChildPtpId_Object=MibTableColumn
cwsXcvrChildPtpId=_CwsXcvrChildPtpId_Object((1,3,6,1,4,1,1271,3,4,15,7,1,2),_CwsXcvrChildPtpId_Type())
cwsXcvrChildPtpId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrChildPtpId.setStatus(_A)
_CwsXcvrCienaIdTable_Object=MibTable
cwsXcvrCienaIdTable=_CwsXcvrCienaIdTable_Object((1,3,6,1,4,1,1271,3,4,15,8))
if mibBuilder.loadTexts:cwsXcvrCienaIdTable.setStatus(_A)
_CwsXcvrCienaIdEntry_Object=MibTableRow
cwsXcvrCienaIdEntry=_CwsXcvrCienaIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,8,1))
cwsXcvrCienaIdEntry.setIndexNames((0,_B,_E),(0,_B,_O))
if mibBuilder.loadTexts:cwsXcvrCienaIdEntry.setStatus(_A)
class _CwsXcvrCienaIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrCienaIdTableSnmpKey_Type.__name__=_D
_CwsXcvrCienaIdTableSnmpKey_Object=MibTableColumn
cwsXcvrCienaIdTableSnmpKey=_CwsXcvrCienaIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,8,1,1),_CwsXcvrCienaIdTableSnmpKey_Type())
cwsXcvrCienaIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrCienaIdTableSnmpKey.setStatus(_A)
_CwsXcvrCienaIdCienaItemNumber_Type=StringMaxl32
_CwsXcvrCienaIdCienaItemNumber_Object=MibTableColumn
cwsXcvrCienaIdCienaItemNumber=_CwsXcvrCienaIdCienaItemNumber_Object((1,3,6,1,4,1,1271,3,4,15,8,1,2),_CwsXcvrCienaIdCienaItemNumber_Type())
cwsXcvrCienaIdCienaItemNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrCienaIdCienaItemNumber.setStatus(_A)
_CwsXcvrCienaIdRevision_Type=StringMaxl32
_CwsXcvrCienaIdRevision_Object=MibTableColumn
cwsXcvrCienaIdRevision=_CwsXcvrCienaIdRevision_Object((1,3,6,1,4,1,1271,3,4,15,8,1,3),_CwsXcvrCienaIdRevision_Type())
cwsXcvrCienaIdRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrCienaIdRevision.setStatus(_A)
_CwsXcvrCienaIdDescription_Type=StringMaxl254
_CwsXcvrCienaIdDescription_Object=MibTableColumn
cwsXcvrCienaIdDescription=_CwsXcvrCienaIdDescription_Object((1,3,6,1,4,1,1271,3,4,15,8,1,4),_CwsXcvrCienaIdDescription_Type())
cwsXcvrCienaIdDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrCienaIdDescription.setStatus(_A)
_CwsXcvrVendorIdTable_Object=MibTable
cwsXcvrVendorIdTable=_CwsXcvrVendorIdTable_Object((1,3,6,1,4,1,1271,3,4,15,9))
if mibBuilder.loadTexts:cwsXcvrVendorIdTable.setStatus(_A)
_CwsXcvrVendorIdEntry_Object=MibTableRow
cwsXcvrVendorIdEntry=_CwsXcvrVendorIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,9,1))
cwsXcvrVendorIdEntry.setIndexNames((0,_B,_E),(0,_B,_P))
if mibBuilder.loadTexts:cwsXcvrVendorIdEntry.setStatus(_A)
class _CwsXcvrVendorIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrVendorIdTableSnmpKey_Type.__name__=_D
_CwsXcvrVendorIdTableSnmpKey_Object=MibTableColumn
cwsXcvrVendorIdTableSnmpKey=_CwsXcvrVendorIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,9,1,1),_CwsXcvrVendorIdTableSnmpKey_Type())
cwsXcvrVendorIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrVendorIdTableSnmpKey.setStatus(_A)
_CwsXcvrVendorIdName_Type=StringMaxl32
_CwsXcvrVendorIdName_Object=MibTableColumn
cwsXcvrVendorIdName=_CwsXcvrVendorIdName_Object((1,3,6,1,4,1,1271,3,4,15,9,1,2),_CwsXcvrVendorIdName_Type())
cwsXcvrVendorIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorIdName.setStatus(_A)
_CwsXcvrVendorIdPartNumber_Type=StringMaxl32
_CwsXcvrVendorIdPartNumber_Object=MibTableColumn
cwsXcvrVendorIdPartNumber=_CwsXcvrVendorIdPartNumber_Object((1,3,6,1,4,1,1271,3,4,15,9,1,3),_CwsXcvrVendorIdPartNumber_Type())
cwsXcvrVendorIdPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorIdPartNumber.setStatus(_A)
_CwsXcvrVendorIdRevision_Type=StringMaxl32
_CwsXcvrVendorIdRevision_Object=MibTableColumn
cwsXcvrVendorIdRevision=_CwsXcvrVendorIdRevision_Object((1,3,6,1,4,1,1271,3,4,15,9,1,4),_CwsXcvrVendorIdRevision_Type())
cwsXcvrVendorIdRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorIdRevision.setStatus(_A)
_CwsXcvrVendorIdSerialNumber_Type=StringMaxl32
_CwsXcvrVendorIdSerialNumber_Object=MibTableColumn
cwsXcvrVendorIdSerialNumber=_CwsXcvrVendorIdSerialNumber_Object((1,3,6,1,4,1,1271,3,4,15,9,1,5),_CwsXcvrVendorIdSerialNumber_Type())
cwsXcvrVendorIdSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorIdSerialNumber.setStatus(_A)
_CwsXcvrVendorIdManufacturedDate_Type=StringMaxl16
_CwsXcvrVendorIdManufacturedDate_Object=MibTableColumn
cwsXcvrVendorIdManufacturedDate=_CwsXcvrVendorIdManufacturedDate_Object((1,3,6,1,4,1,1271,3,4,15,9,1,6),_CwsXcvrVendorIdManufacturedDate_Type())
cwsXcvrVendorIdManufacturedDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorIdManufacturedDate.setStatus(_A)
_CwsXcvrDeviceIdTable_Object=MibTable
cwsXcvrDeviceIdTable=_CwsXcvrDeviceIdTable_Object((1,3,6,1,4,1,1271,3,4,15,10))
if mibBuilder.loadTexts:cwsXcvrDeviceIdTable.setStatus(_A)
_CwsXcvrDeviceIdEntry_Object=MibTableRow
cwsXcvrDeviceIdEntry=_CwsXcvrDeviceIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,10,1))
cwsXcvrDeviceIdEntry.setIndexNames((0,_B,_E),(0,_B,_Q))
if mibBuilder.loadTexts:cwsXcvrDeviceIdEntry.setStatus(_A)
class _CwsXcvrDeviceIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrDeviceIdTableSnmpKey_Type.__name__=_D
_CwsXcvrDeviceIdTableSnmpKey_Object=MibTableColumn
cwsXcvrDeviceIdTableSnmpKey=_CwsXcvrDeviceIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,10,1,1),_CwsXcvrDeviceIdTableSnmpKey_Type())
cwsXcvrDeviceIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrDeviceIdTableSnmpKey.setStatus(_A)
_CwsXcvrDeviceIdConnectorType_Type=ConnectorTypeDescEnum
_CwsXcvrDeviceIdConnectorType_Object=MibTableColumn
cwsXcvrDeviceIdConnectorType=_CwsXcvrDeviceIdConnectorType_Object((1,3,6,1,4,1,1271,3,4,15,10,1,2),_CwsXcvrDeviceIdConnectorType_Type())
cwsXcvrDeviceIdConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrDeviceIdConnectorType.setStatus(_A)
_CwsXcvrVendorTransmitterTable_Object=MibTable
cwsXcvrVendorTransmitterTable=_CwsXcvrVendorTransmitterTable_Object((1,3,6,1,4,1,1271,3,4,15,11))
if mibBuilder.loadTexts:cwsXcvrVendorTransmitterTable.setStatus(_A)
_CwsXcvrVendorTransmitterEntry_Object=MibTableRow
cwsXcvrVendorTransmitterEntry=_CwsXcvrVendorTransmitterEntry_Object((1,3,6,1,4,1,1271,3,4,15,11,1))
cwsXcvrVendorTransmitterEntry.setIndexNames((0,_B,_E),(0,_B,_R))
if mibBuilder.loadTexts:cwsXcvrVendorTransmitterEntry.setStatus(_A)
class _CwsXcvrVendorTransmitterTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrVendorTransmitterTableSnmpKey_Type.__name__=_D
_CwsXcvrVendorTransmitterTableSnmpKey_Object=MibTableColumn
cwsXcvrVendorTransmitterTableSnmpKey=_CwsXcvrVendorTransmitterTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,11,1,1),_CwsXcvrVendorTransmitterTableSnmpKey_Type())
cwsXcvrVendorTransmitterTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrVendorTransmitterTableSnmpKey.setStatus(_A)
_CwsXcvrVendorTransmitterNominalBitRate_Type=StringMaxl16
_CwsXcvrVendorTransmitterNominalBitRate_Object=MibTableColumn
cwsXcvrVendorTransmitterNominalBitRate=_CwsXcvrVendorTransmitterNominalBitRate_Object((1,3,6,1,4,1,1271,3,4,15,11,1,2),_CwsXcvrVendorTransmitterNominalBitRate_Type())
cwsXcvrVendorTransmitterNominalBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorTransmitterNominalBitRate.setStatus(_A)
_CwsXcvrVendorDiagnosticMonitoringTable_Object=MibTable
cwsXcvrVendorDiagnosticMonitoringTable=_CwsXcvrVendorDiagnosticMonitoringTable_Object((1,3,6,1,4,1,1271,3,4,15,12))
if mibBuilder.loadTexts:cwsXcvrVendorDiagnosticMonitoringTable.setStatus(_A)
_CwsXcvrVendorDiagnosticMonitoringEntry_Object=MibTableRow
cwsXcvrVendorDiagnosticMonitoringEntry=_CwsXcvrVendorDiagnosticMonitoringEntry_Object((1,3,6,1,4,1,1271,3,4,15,12,1))
cwsXcvrVendorDiagnosticMonitoringEntry.setIndexNames((0,_B,_E),(0,_B,_S))
if mibBuilder.loadTexts:cwsXcvrVendorDiagnosticMonitoringEntry.setStatus(_A)
class _CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type.__name__=_D
_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Object=MibTableColumn
cwsXcvrVendorDiagnosticMonitoringTableSnmpKey=_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,12,1,1),_CwsXcvrVendorDiagnosticMonitoringTableSnmpKey_Type())
cwsXcvrVendorDiagnosticMonitoringTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrVendorDiagnosticMonitoringTableSnmpKey.setStatus(_A)
class _CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('zeroma',0),('averagepower',1),('yes',2),('no',3)))
_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type.__name__=_D
_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Object=MibTableColumn
cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement=_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Object((1,3,6,1,4,1,1271,3,4,15,12,1,2),_CwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement_Type())
cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement.setStatus(_A)
class _CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notsupported',0),('supported',1),('yes',2),('no',3)))
_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type.__name__=_D
_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Object=MibTableColumn
cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement=_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Object((1,3,6,1,4,1,1271,3,4,15,12,1,3),_CwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement_Type())
cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement.setStatus(_A)
_CwsXcvrTemperatureTable_Object=MibTable
cwsXcvrTemperatureTable=_CwsXcvrTemperatureTable_Object((1,3,6,1,4,1,1271,3,4,15,13))
if mibBuilder.loadTexts:cwsXcvrTemperatureTable.setStatus(_A)
_CwsXcvrTemperatureEntry_Object=MibTableRow
cwsXcvrTemperatureEntry=_CwsXcvrTemperatureEntry_Object((1,3,6,1,4,1,1271,3,4,15,13,1))
cwsXcvrTemperatureEntry.setIndexNames((0,_B,_E),(0,_B,_T))
if mibBuilder.loadTexts:cwsXcvrTemperatureEntry.setStatus(_A)
class _CwsXcvrTemperatureTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrTemperatureTableSnmpKey_Type.__name__=_D
_CwsXcvrTemperatureTableSnmpKey_Object=MibTableColumn
cwsXcvrTemperatureTableSnmpKey=_CwsXcvrTemperatureTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,13,1,1),_CwsXcvrTemperatureTableSnmpKey_Type())
cwsXcvrTemperatureTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrTemperatureTableSnmpKey.setStatus(_A)
_CwsXcvrTemperatureActual_Type=Integer32
_CwsXcvrTemperatureActual_Object=MibTableColumn
cwsXcvrTemperatureActual=_CwsXcvrTemperatureActual_Object((1,3,6,1,4,1,1271,3,4,15,13,1,2),_CwsXcvrTemperatureActual_Type())
cwsXcvrTemperatureActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureActual.setStatus(_A)
_CwsXcvrTemperatureStatusTable_Object=MibTable
cwsXcvrTemperatureStatusTable=_CwsXcvrTemperatureStatusTable_Object((1,3,6,1,4,1,1271,3,4,15,14))
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusTable.setStatus(_A)
_CwsXcvrTemperatureStatusEntry_Object=MibTableRow
cwsXcvrTemperatureStatusEntry=_CwsXcvrTemperatureStatusEntry_Object((1,3,6,1,4,1,1271,3,4,15,14,1))
cwsXcvrTemperatureStatusEntry.setIndexNames((0,_B,_E),(0,_B,_U))
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusEntry.setStatus(_A)
class _CwsXcvrTemperatureStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrTemperatureStatusTableSnmpKey_Type.__name__=_D
_CwsXcvrTemperatureStatusTableSnmpKey_Object=MibTableColumn
cwsXcvrTemperatureStatusTableSnmpKey=_CwsXcvrTemperatureStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,14,1,1),_CwsXcvrTemperatureStatusTableSnmpKey_Type())
cwsXcvrTemperatureStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusTableSnmpKey.setStatus(_A)
_CwsXcvrTemperatureStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrTemperatureStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrTemperatureStatusHighAlarmStatus=_CwsXcvrTemperatureStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,14,1,2),_CwsXcvrTemperatureStatusHighAlarmStatus_Type())
cwsXcvrTemperatureStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrTemperatureStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrTemperatureStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrTemperatureStatusLowAlarmStatus=_CwsXcvrTemperatureStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,14,1,3),_CwsXcvrTemperatureStatusLowAlarmStatus_Type())
cwsXcvrTemperatureStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrTemperatureStatusHighWarningStatus_Type=TruthValue
_CwsXcvrTemperatureStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrTemperatureStatusHighWarningStatus=_CwsXcvrTemperatureStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,14,1,4),_CwsXcvrTemperatureStatusHighWarningStatus_Type())
cwsXcvrTemperatureStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusHighWarningStatus.setStatus(_A)
_CwsXcvrTemperatureStatusLowWarningStatus_Type=TruthValue
_CwsXcvrTemperatureStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrTemperatureStatusLowWarningStatus=_CwsXcvrTemperatureStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,14,1,5),_CwsXcvrTemperatureStatusLowWarningStatus_Type())
cwsXcvrTemperatureStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureStatusLowWarningStatus.setStatus(_A)
_CwsXcvrTemperatureThresholdTable_Object=MibTable
cwsXcvrTemperatureThresholdTable=_CwsXcvrTemperatureThresholdTable_Object((1,3,6,1,4,1,1271,3,4,15,15))
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdTable.setStatus(_A)
_CwsXcvrTemperatureThresholdEntry_Object=MibTableRow
cwsXcvrTemperatureThresholdEntry=_CwsXcvrTemperatureThresholdEntry_Object((1,3,6,1,4,1,1271,3,4,15,15,1))
cwsXcvrTemperatureThresholdEntry.setIndexNames((0,_B,_E),(0,_B,_V))
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdEntry.setStatus(_A)
class _CwsXcvrTemperatureThresholdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrTemperatureThresholdTableSnmpKey_Type.__name__=_D
_CwsXcvrTemperatureThresholdTableSnmpKey_Object=MibTableColumn
cwsXcvrTemperatureThresholdTableSnmpKey=_CwsXcvrTemperatureThresholdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,15,1,1),_CwsXcvrTemperatureThresholdTableSnmpKey_Type())
cwsXcvrTemperatureThresholdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdTableSnmpKey.setStatus(_A)
_CwsXcvrTemperatureThresholdHighAlarmThreshold_Type=Integer32
_CwsXcvrTemperatureThresholdHighAlarmThreshold_Object=MibTableColumn
cwsXcvrTemperatureThresholdHighAlarmThreshold=_CwsXcvrTemperatureThresholdHighAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,15,1,2),_CwsXcvrTemperatureThresholdHighAlarmThreshold_Type())
cwsXcvrTemperatureThresholdHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdHighAlarmThreshold.setStatus(_A)
_CwsXcvrTemperatureThresholdLowAlarmThreshold_Type=Integer32
_CwsXcvrTemperatureThresholdLowAlarmThreshold_Object=MibTableColumn
cwsXcvrTemperatureThresholdLowAlarmThreshold=_CwsXcvrTemperatureThresholdLowAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,15,1,3),_CwsXcvrTemperatureThresholdLowAlarmThreshold_Type())
cwsXcvrTemperatureThresholdLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdLowAlarmThreshold.setStatus(_A)
_CwsXcvrTemperatureThresholdHighWarningThreshold_Type=Integer32
_CwsXcvrTemperatureThresholdHighWarningThreshold_Object=MibTableColumn
cwsXcvrTemperatureThresholdHighWarningThreshold=_CwsXcvrTemperatureThresholdHighWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,15,1,4),_CwsXcvrTemperatureThresholdHighWarningThreshold_Type())
cwsXcvrTemperatureThresholdHighWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdHighWarningThreshold.setStatus(_A)
_CwsXcvrTemperatureThresholdLowWarningThreshold_Type=Integer32
_CwsXcvrTemperatureThresholdLowWarningThreshold_Object=MibTableColumn
cwsXcvrTemperatureThresholdLowWarningThreshold=_CwsXcvrTemperatureThresholdLowWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,15,1,5),_CwsXcvrTemperatureThresholdLowWarningThreshold_Type())
cwsXcvrTemperatureThresholdLowWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTemperatureThresholdLowWarningThreshold.setStatus(_A)
_CwsXcvrChannelDiagnosticsTable_Object=MibTable
cwsXcvrChannelDiagnosticsTable=_CwsXcvrChannelDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,15,16))
if mibBuilder.loadTexts:cwsXcvrChannelDiagnosticsTable.setStatus(_A)
_CwsXcvrChannelDiagnosticsEntry_Object=MibTableRow
cwsXcvrChannelDiagnosticsEntry=_CwsXcvrChannelDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,15,16,1))
cwsXcvrChannelDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cwsXcvrChannelDiagnosticsEntry.setStatus(_A)
class _CwsXcvrChannelDiagnosticsChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrChannelDiagnosticsChannelNumber_Type.__name__=_D
_CwsXcvrChannelDiagnosticsChannelNumber_Object=MibTableColumn
cwsXcvrChannelDiagnosticsChannelNumber=_CwsXcvrChannelDiagnosticsChannelNumber_Object((1,3,6,1,4,1,1271,3,4,15,16,1,1),_CwsXcvrChannelDiagnosticsChannelNumber_Type())
cwsXcvrChannelDiagnosticsChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrChannelDiagnosticsChannelNumber.setStatus(_A)
_CwsXcvrChannelRxPowerTable_Object=MibTable
cwsXcvrChannelRxPowerTable=_CwsXcvrChannelRxPowerTable_Object((1,3,6,1,4,1,1271,3,4,15,17))
if mibBuilder.loadTexts:cwsXcvrChannelRxPowerTable.setStatus(_A)
_CwsXcvrChannelRxPowerEntry_Object=MibTableRow
cwsXcvrChannelRxPowerEntry=_CwsXcvrChannelRxPowerEntry_Object((1,3,6,1,4,1,1271,3,4,15,17,1))
cwsXcvrChannelRxPowerEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_W))
if mibBuilder.loadTexts:cwsXcvrChannelRxPowerEntry.setStatus(_A)
class _CwsXcvrChannelRxPowerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrChannelRxPowerTableSnmpKey_Type.__name__=_D
_CwsXcvrChannelRxPowerTableSnmpKey_Object=MibTableColumn
cwsXcvrChannelRxPowerTableSnmpKey=_CwsXcvrChannelRxPowerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,17,1,1),_CwsXcvrChannelRxPowerTableSnmpKey_Type())
cwsXcvrChannelRxPowerTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrChannelRxPowerTableSnmpKey.setStatus(_A)
_CwsXcvrChannelRxPowerActual_Type=Decimal1Dig
_CwsXcvrChannelRxPowerActual_Object=MibTableColumn
cwsXcvrChannelRxPowerActual=_CwsXcvrChannelRxPowerActual_Object((1,3,6,1,4,1,1271,3,4,15,17,1,2),_CwsXcvrChannelRxPowerActual_Type())
cwsXcvrChannelRxPowerActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrChannelRxPowerActual.setStatus(_A)
_CwsXcvrRxPowerStatusTable_Object=MibTable
cwsXcvrRxPowerStatusTable=_CwsXcvrRxPowerStatusTable_Object((1,3,6,1,4,1,1271,3,4,15,18))
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusTable.setStatus(_A)
_CwsXcvrRxPowerStatusEntry_Object=MibTableRow
cwsXcvrRxPowerStatusEntry=_CwsXcvrRxPowerStatusEntry_Object((1,3,6,1,4,1,1271,3,4,15,18,1))
cwsXcvrRxPowerStatusEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_X))
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusEntry.setStatus(_A)
class _CwsXcvrRxPowerStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrRxPowerStatusTableSnmpKey_Type.__name__=_D
_CwsXcvrRxPowerStatusTableSnmpKey_Object=MibTableColumn
cwsXcvrRxPowerStatusTableSnmpKey=_CwsXcvrRxPowerStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,18,1,1),_CwsXcvrRxPowerStatusTableSnmpKey_Type())
cwsXcvrRxPowerStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusTableSnmpKey.setStatus(_A)
_CwsXcvrRxPowerStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrRxPowerStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrRxPowerStatusHighAlarmStatus=_CwsXcvrRxPowerStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,18,1,2),_CwsXcvrRxPowerStatusHighAlarmStatus_Type())
cwsXcvrRxPowerStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrRxPowerStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrRxPowerStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrRxPowerStatusLowAlarmStatus=_CwsXcvrRxPowerStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,18,1,3),_CwsXcvrRxPowerStatusLowAlarmStatus_Type())
cwsXcvrRxPowerStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrRxPowerStatusHighWarningStatus_Type=TruthValue
_CwsXcvrRxPowerStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrRxPowerStatusHighWarningStatus=_CwsXcvrRxPowerStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,18,1,4),_CwsXcvrRxPowerStatusHighWarningStatus_Type())
cwsXcvrRxPowerStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusHighWarningStatus.setStatus(_A)
_CwsXcvrRxPowerStatusLowWarningStatus_Type=TruthValue
_CwsXcvrRxPowerStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrRxPowerStatusLowWarningStatus=_CwsXcvrRxPowerStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,18,1,5),_CwsXcvrRxPowerStatusLowWarningStatus_Type())
cwsXcvrRxPowerStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerStatusLowWarningStatus.setStatus(_A)
_CwsXcvrRxPowerThresholdTable_Object=MibTable
cwsXcvrRxPowerThresholdTable=_CwsXcvrRxPowerThresholdTable_Object((1,3,6,1,4,1,1271,3,4,15,19))
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdTable.setStatus(_A)
_CwsXcvrRxPowerThresholdEntry_Object=MibTableRow
cwsXcvrRxPowerThresholdEntry=_CwsXcvrRxPowerThresholdEntry_Object((1,3,6,1,4,1,1271,3,4,15,19,1))
cwsXcvrRxPowerThresholdEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_Y))
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdEntry.setStatus(_A)
class _CwsXcvrRxPowerThresholdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrRxPowerThresholdTableSnmpKey_Type.__name__=_D
_CwsXcvrRxPowerThresholdTableSnmpKey_Object=MibTableColumn
cwsXcvrRxPowerThresholdTableSnmpKey=_CwsXcvrRxPowerThresholdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,19,1,1),_CwsXcvrRxPowerThresholdTableSnmpKey_Type())
cwsXcvrRxPowerThresholdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdTableSnmpKey.setStatus(_A)
_CwsXcvrRxPowerThresholdHighAlarmThreshold_Type=Decimal1Dig
_CwsXcvrRxPowerThresholdHighAlarmThreshold_Object=MibTableColumn
cwsXcvrRxPowerThresholdHighAlarmThreshold=_CwsXcvrRxPowerThresholdHighAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,19,1,2),_CwsXcvrRxPowerThresholdHighAlarmThreshold_Type())
cwsXcvrRxPowerThresholdHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdHighAlarmThreshold.setStatus(_A)
_CwsXcvrRxPowerThresholdLowAlarmThreshold_Type=Decimal1Dig
_CwsXcvrRxPowerThresholdLowAlarmThreshold_Object=MibTableColumn
cwsXcvrRxPowerThresholdLowAlarmThreshold=_CwsXcvrRxPowerThresholdLowAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,19,1,3),_CwsXcvrRxPowerThresholdLowAlarmThreshold_Type())
cwsXcvrRxPowerThresholdLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdLowAlarmThreshold.setStatus(_A)
_CwsXcvrRxPowerThresholdHighWarningThreshold_Type=Decimal1Dig
_CwsXcvrRxPowerThresholdHighWarningThreshold_Object=MibTableColumn
cwsXcvrRxPowerThresholdHighWarningThreshold=_CwsXcvrRxPowerThresholdHighWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,19,1,4),_CwsXcvrRxPowerThresholdHighWarningThreshold_Type())
cwsXcvrRxPowerThresholdHighWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdHighWarningThreshold.setStatus(_A)
_CwsXcvrRxPowerThresholdLowWarningThreshold_Type=Decimal1Dig
_CwsXcvrRxPowerThresholdLowWarningThreshold_Object=MibTableColumn
cwsXcvrRxPowerThresholdLowWarningThreshold=_CwsXcvrRxPowerThresholdLowWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,19,1,5),_CwsXcvrRxPowerThresholdLowWarningThreshold_Type())
cwsXcvrRxPowerThresholdLowWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerThresholdLowWarningThreshold.setStatus(_A)
_CwsXcvrChannelTxPowerTable_Object=MibTable
cwsXcvrChannelTxPowerTable=_CwsXcvrChannelTxPowerTable_Object((1,3,6,1,4,1,1271,3,4,15,20))
if mibBuilder.loadTexts:cwsXcvrChannelTxPowerTable.setStatus(_A)
_CwsXcvrChannelTxPowerEntry_Object=MibTableRow
cwsXcvrChannelTxPowerEntry=_CwsXcvrChannelTxPowerEntry_Object((1,3,6,1,4,1,1271,3,4,15,20,1))
cwsXcvrChannelTxPowerEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_Z))
if mibBuilder.loadTexts:cwsXcvrChannelTxPowerEntry.setStatus(_A)
class _CwsXcvrChannelTxPowerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrChannelTxPowerTableSnmpKey_Type.__name__=_D
_CwsXcvrChannelTxPowerTableSnmpKey_Object=MibTableColumn
cwsXcvrChannelTxPowerTableSnmpKey=_CwsXcvrChannelTxPowerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,20,1,1),_CwsXcvrChannelTxPowerTableSnmpKey_Type())
cwsXcvrChannelTxPowerTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrChannelTxPowerTableSnmpKey.setStatus(_A)
_CwsXcvrChannelTxPowerActual_Type=Decimal1Dig
_CwsXcvrChannelTxPowerActual_Object=MibTableColumn
cwsXcvrChannelTxPowerActual=_CwsXcvrChannelTxPowerActual_Object((1,3,6,1,4,1,1271,3,4,15,20,1,2),_CwsXcvrChannelTxPowerActual_Type())
cwsXcvrChannelTxPowerActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrChannelTxPowerActual.setStatus(_A)
_CwsXcvrTxPowerStatusTable_Object=MibTable
cwsXcvrTxPowerStatusTable=_CwsXcvrTxPowerStatusTable_Object((1,3,6,1,4,1,1271,3,4,15,21))
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusTable.setStatus(_A)
_CwsXcvrTxPowerStatusEntry_Object=MibTableRow
cwsXcvrTxPowerStatusEntry=_CwsXcvrTxPowerStatusEntry_Object((1,3,6,1,4,1,1271,3,4,15,21,1))
cwsXcvrTxPowerStatusEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_a))
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusEntry.setStatus(_A)
class _CwsXcvrTxPowerStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrTxPowerStatusTableSnmpKey_Type.__name__=_D
_CwsXcvrTxPowerStatusTableSnmpKey_Object=MibTableColumn
cwsXcvrTxPowerStatusTableSnmpKey=_CwsXcvrTxPowerStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,21,1,1),_CwsXcvrTxPowerStatusTableSnmpKey_Type())
cwsXcvrTxPowerStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusTableSnmpKey.setStatus(_A)
_CwsXcvrTxPowerStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrTxPowerStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrTxPowerStatusHighAlarmStatus=_CwsXcvrTxPowerStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,21,1,2),_CwsXcvrTxPowerStatusHighAlarmStatus_Type())
cwsXcvrTxPowerStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrTxPowerStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrTxPowerStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrTxPowerStatusLowAlarmStatus=_CwsXcvrTxPowerStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,15,21,1,3),_CwsXcvrTxPowerStatusLowAlarmStatus_Type())
cwsXcvrTxPowerStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrTxPowerStatusHighWarningStatus_Type=TruthValue
_CwsXcvrTxPowerStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrTxPowerStatusHighWarningStatus=_CwsXcvrTxPowerStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,21,1,4),_CwsXcvrTxPowerStatusHighWarningStatus_Type())
cwsXcvrTxPowerStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusHighWarningStatus.setStatus(_A)
_CwsXcvrTxPowerStatusLowWarningStatus_Type=TruthValue
_CwsXcvrTxPowerStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrTxPowerStatusLowWarningStatus=_CwsXcvrTxPowerStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,15,21,1,5),_CwsXcvrTxPowerStatusLowWarningStatus_Type())
cwsXcvrTxPowerStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerStatusLowWarningStatus.setStatus(_A)
_CwsXcvrTxPowerThresholdTable_Object=MibTable
cwsXcvrTxPowerThresholdTable=_CwsXcvrTxPowerThresholdTable_Object((1,3,6,1,4,1,1271,3,4,15,22))
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdTable.setStatus(_A)
_CwsXcvrTxPowerThresholdEntry_Object=MibTableRow
cwsXcvrTxPowerThresholdEntry=_CwsXcvrTxPowerThresholdEntry_Object((1,3,6,1,4,1,1271,3,4,15,22,1))
cwsXcvrTxPowerThresholdEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_b))
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdEntry.setStatus(_A)
class _CwsXcvrTxPowerThresholdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrTxPowerThresholdTableSnmpKey_Type.__name__=_D
_CwsXcvrTxPowerThresholdTableSnmpKey_Object=MibTableColumn
cwsXcvrTxPowerThresholdTableSnmpKey=_CwsXcvrTxPowerThresholdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,22,1,1),_CwsXcvrTxPowerThresholdTableSnmpKey_Type())
cwsXcvrTxPowerThresholdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdTableSnmpKey.setStatus(_A)
_CwsXcvrTxPowerThresholdHighAlarmThreshold_Type=Decimal1Dig
_CwsXcvrTxPowerThresholdHighAlarmThreshold_Object=MibTableColumn
cwsXcvrTxPowerThresholdHighAlarmThreshold=_CwsXcvrTxPowerThresholdHighAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,22,1,2),_CwsXcvrTxPowerThresholdHighAlarmThreshold_Type())
cwsXcvrTxPowerThresholdHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdHighAlarmThreshold.setStatus(_A)
_CwsXcvrTxPowerThresholdLowAlarmThreshold_Type=Decimal1Dig
_CwsXcvrTxPowerThresholdLowAlarmThreshold_Object=MibTableColumn
cwsXcvrTxPowerThresholdLowAlarmThreshold=_CwsXcvrTxPowerThresholdLowAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,15,22,1,3),_CwsXcvrTxPowerThresholdLowAlarmThreshold_Type())
cwsXcvrTxPowerThresholdLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdLowAlarmThreshold.setStatus(_A)
_CwsXcvrTxPowerThresholdHighWarningThreshold_Type=Decimal1Dig
_CwsXcvrTxPowerThresholdHighWarningThreshold_Object=MibTableColumn
cwsXcvrTxPowerThresholdHighWarningThreshold=_CwsXcvrTxPowerThresholdHighWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,22,1,4),_CwsXcvrTxPowerThresholdHighWarningThreshold_Type())
cwsXcvrTxPowerThresholdHighWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdHighWarningThreshold.setStatus(_A)
_CwsXcvrTxPowerThresholdLowWarningThreshold_Type=Decimal1Dig
_CwsXcvrTxPowerThresholdLowWarningThreshold_Object=MibTableColumn
cwsXcvrTxPowerThresholdLowWarningThreshold=_CwsXcvrTxPowerThresholdLowWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,15,22,1,5),_CwsXcvrTxPowerThresholdLowWarningThreshold_Type())
cwsXcvrTxPowerThresholdLowWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerThresholdLowWarningThreshold.setStatus(_A)
_CwsXcvrXcvrProfilesTable_Object=MibTable
cwsXcvrXcvrProfilesTable=_CwsXcvrXcvrProfilesTable_Object((1,3,6,1,4,1,1271,3,4,15,23))
if mibBuilder.loadTexts:cwsXcvrXcvrProfilesTable.setStatus(_A)
_CwsXcvrXcvrProfilesEntry_Object=MibTableRow
cwsXcvrXcvrProfilesEntry=_CwsXcvrXcvrProfilesEntry_Object((1,3,6,1,4,1,1271,3,4,15,23,1))
cwsXcvrXcvrProfilesEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cwsXcvrXcvrProfilesEntry.setStatus(_A)
class _CwsXcvrXcvrProfilesXcvrProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrProfilesXcvrProfileIndex_Type.__name__=_D
_CwsXcvrXcvrProfilesXcvrProfileIndex_Object=MibTableColumn
cwsXcvrXcvrProfilesXcvrProfileIndex=_CwsXcvrXcvrProfilesXcvrProfileIndex_Object((1,3,6,1,4,1,1271,3,4,15,23,1,1),_CwsXcvrXcvrProfilesXcvrProfileIndex_Type())
cwsXcvrXcvrProfilesXcvrProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrXcvrProfilesXcvrProfileIndex.setStatus(_A)
_CwsXcvrXcvrProfileIdTable_Object=MibTable
cwsXcvrXcvrProfileIdTable=_CwsXcvrXcvrProfileIdTable_Object((1,3,6,1,4,1,1271,3,4,15,24))
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdTable.setStatus(_A)
_CwsXcvrXcvrProfileIdEntry_Object=MibTableRow
cwsXcvrXcvrProfileIdEntry=_CwsXcvrXcvrProfileIdEntry_Object((1,3,6,1,4,1,1271,3,4,15,24,1))
cwsXcvrXcvrProfileIdEntry.setIndexNames((0,_B,_J),(0,_B,_c))
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdEntry.setStatus(_A)
class _CwsXcvrXcvrProfileIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrProfileIdTableSnmpKey_Type.__name__=_D
_CwsXcvrXcvrProfileIdTableSnmpKey_Object=MibTableColumn
cwsXcvrXcvrProfileIdTableSnmpKey=_CwsXcvrXcvrProfileIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,24,1,1),_CwsXcvrXcvrProfileIdTableSnmpKey_Type())
cwsXcvrXcvrProfileIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdTableSnmpKey.setStatus(_A)
class _CwsXcvrXcvrProfileIdVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CwsXcvrXcvrProfileIdVendorName_Type.__name__=_I
_CwsXcvrXcvrProfileIdVendorName_Object=MibTableColumn
cwsXcvrXcvrProfileIdVendorName=_CwsXcvrXcvrProfileIdVendorName_Object((1,3,6,1,4,1,1271,3,4,15,24,1,2),_CwsXcvrXcvrProfileIdVendorName_Type())
cwsXcvrXcvrProfileIdVendorName.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdVendorName.setStatus(_A)
class _CwsXcvrXcvrProfileIdVendorOui_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CwsXcvrXcvrProfileIdVendorOui_Type.__name__=_I
_CwsXcvrXcvrProfileIdVendorOui_Object=MibTableColumn
cwsXcvrXcvrProfileIdVendorOui=_CwsXcvrXcvrProfileIdVendorOui_Object((1,3,6,1,4,1,1271,3,4,15,24,1,3),_CwsXcvrXcvrProfileIdVendorOui_Type())
cwsXcvrXcvrProfileIdVendorOui.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdVendorOui.setStatus(_A)
class _CwsXcvrXcvrProfileIdVendorPn_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CwsXcvrXcvrProfileIdVendorPn_Type.__name__=_I
_CwsXcvrXcvrProfileIdVendorPn_Object=MibTableColumn
cwsXcvrXcvrProfileIdVendorPn=_CwsXcvrXcvrProfileIdVendorPn_Object((1,3,6,1,4,1,1271,3,4,15,24,1,4),_CwsXcvrXcvrProfileIdVendorPn_Type())
cwsXcvrXcvrProfileIdVendorPn.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdVendorPn.setStatus(_A)
class _CwsXcvrXcvrProfileIdVendorRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CwsXcvrXcvrProfileIdVendorRev_Type.__name__=_I
_CwsXcvrXcvrProfileIdVendorRev_Object=MibTableColumn
cwsXcvrXcvrProfileIdVendorRev=_CwsXcvrXcvrProfileIdVendorRev_Object((1,3,6,1,4,1,1271,3,4,15,24,1,5),_CwsXcvrXcvrProfileIdVendorRev_Type())
cwsXcvrXcvrProfileIdVendorRev.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfileIdVendorRev.setStatus(_A)
_CwsXcvrXcvrProfilePropertiesTable_Object=MibTable
cwsXcvrXcvrProfilePropertiesTable=_CwsXcvrXcvrProfilePropertiesTable_Object((1,3,6,1,4,1,1271,3,4,15,25))
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesTable.setStatus(_A)
_CwsXcvrXcvrProfilePropertiesEntry_Object=MibTableRow
cwsXcvrXcvrProfilePropertiesEntry=_CwsXcvrXcvrProfilePropertiesEntry_Object((1,3,6,1,4,1,1271,3,4,15,25,1))
cwsXcvrXcvrProfilePropertiesEntry.setIndexNames((0,_B,_J),(0,_B,_d))
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesEntry.setStatus(_A)
class _CwsXcvrXcvrProfilePropertiesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrXcvrProfilePropertiesTableSnmpKey_Type.__name__=_D
_CwsXcvrXcvrProfilePropertiesTableSnmpKey_Object=MibTableColumn
cwsXcvrXcvrProfilePropertiesTableSnmpKey=_CwsXcvrXcvrProfilePropertiesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,15,25,1,1),_CwsXcvrXcvrProfilePropertiesTableSnmpKey_Type())
cwsXcvrXcvrProfilePropertiesTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesTableSnmpKey.setStatus(_A)
_CwsXcvrXcvrProfilePropertiesSerdesTxEq_Type=XcvrSerdesTxEq
_CwsXcvrXcvrProfilePropertiesSerdesTxEq_Object=MibTableColumn
cwsXcvrXcvrProfilePropertiesSerdesTxEq=_CwsXcvrXcvrProfilePropertiesSerdesTxEq_Object((1,3,6,1,4,1,1271,3,4,15,25,1,2),_CwsXcvrXcvrProfilePropertiesSerdesTxEq_Type())
cwsXcvrXcvrProfilePropertiesSerdesTxEq.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesSerdesTxEq.setStatus(_A)
_CwsXcvrXcvrProfilePropertiesSerdesRxAmplitude_Type=XcvrSerdesRxAmplitude
_CwsXcvrXcvrProfilePropertiesSerdesRxAmplitude_Object=MibTableColumn
cwsXcvrXcvrProfilePropertiesSerdesRxAmplitude=_CwsXcvrXcvrProfilePropertiesSerdesRxAmplitude_Object((1,3,6,1,4,1,1271,3,4,15,25,1,3),_CwsXcvrXcvrProfilePropertiesSerdesRxAmplitude_Type())
cwsXcvrXcvrProfilePropertiesSerdesRxAmplitude.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesSerdesRxAmplitude.setStatus(_A)
_CwsXcvrXcvrProfilePropertiesSerdesRxEmphasis_Type=XcvrSerdesRxEmphasis
_CwsXcvrXcvrProfilePropertiesSerdesRxEmphasis_Object=MibTableColumn
cwsXcvrXcvrProfilePropertiesSerdesRxEmphasis=_CwsXcvrXcvrProfilePropertiesSerdesRxEmphasis_Object((1,3,6,1,4,1,1271,3,4,15,25,1,4),_CwsXcvrXcvrProfilePropertiesSerdesRxEmphasis_Type())
cwsXcvrXcvrProfilePropertiesSerdesRxEmphasis.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrXcvrProfilePropertiesSerdesRxEmphasis.setStatus(_A)
cienaWsXcvrGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,15,2,1,1))
cienaWsXcvrGroup.setObjects(*((_B,_E),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_H),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_J),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:cienaWsXcvrGroup.setStatus(_A)
cienaWsXcvrCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,15,2,2,1))
cienaWsXcvrCompliance.setObjects((_B,_AW))
if mibBuilder.loadTexts:cienaWsXcvrCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'XcvrOpEnum':XcvrOpEnum,'cienaWsXcvrMIB':cienaWsXcvrMIB,'cienaWsXcvrObjects':cienaWsXcvrObjects,'cienaWsXcvrConformance':cienaWsXcvrConformance,'cienaWsXcvrGroups':cienaWsXcvrGroups,_AW:cienaWsXcvrGroup,'cienaWsXcvrCompliances':cienaWsXcvrCompliances,'cienaWsXcvrCompliance':cienaWsXcvrCompliance,'cwsXcvrXcvrsTable':cwsXcvrXcvrsTable,'cwsXcvrXcvrsEntry':cwsXcvrXcvrsEntry,_E:cwsXcvrXcvrsXcvrIndex,'cwsXcvrXcvrIdTable':cwsXcvrXcvrIdTable,'cwsXcvrXcvrIdEntry':cwsXcvrXcvrIdEntry,_L:cwsXcvrXcvrIdTableSnmpKey,_e:cwsXcvrXcvrIdName,_f:cwsXcvrXcvrIdDescription,'cwsXcvrXcvrStateTable':cwsXcvrXcvrStateTable,'cwsXcvrXcvrStateEntry':cwsXcvrXcvrStateEntry,_M:cwsXcvrXcvrStateTableSnmpKey,_g:cwsXcvrXcvrStateAdminState,_h:cwsXcvrXcvrStateOperationalState,_i:cwsXcvrXcvrStatePowerState,'cwsXcvrXcvrPropertiesTable':cwsXcvrXcvrPropertiesTable,'cwsXcvrXcvrPropertiesEntry':cwsXcvrXcvrPropertiesEntry,_K:cwsXcvrXcvrPropertiesTableSnmpKey,_j:cwsXcvrXcvrPropertiesType,_k:cwsXcvrXcvrPropertiesMode,_l:cwsXcvrXcvrPropertiesNumberOfChannels,'cwsXcvrChildPtpIdTable':cwsXcvrChildPtpIdTable,'cwsXcvrChildPtpIdEntry':cwsXcvrChildPtpIdEntry,_N:cwsXcvrChildPtpIdTableSnmpKey,'cwsXcvrChildPtpId':cwsXcvrChildPtpId,'cwsXcvrCienaIdTable':cwsXcvrCienaIdTable,'cwsXcvrCienaIdEntry':cwsXcvrCienaIdEntry,_O:cwsXcvrCienaIdTableSnmpKey,_m:cwsXcvrCienaIdCienaItemNumber,_n:cwsXcvrCienaIdRevision,_o:cwsXcvrCienaIdDescription,'cwsXcvrVendorIdTable':cwsXcvrVendorIdTable,'cwsXcvrVendorIdEntry':cwsXcvrVendorIdEntry,_P:cwsXcvrVendorIdTableSnmpKey,_p:cwsXcvrVendorIdName,_q:cwsXcvrVendorIdPartNumber,_r:cwsXcvrVendorIdRevision,_s:cwsXcvrVendorIdSerialNumber,_t:cwsXcvrVendorIdManufacturedDate,'cwsXcvrDeviceIdTable':cwsXcvrDeviceIdTable,'cwsXcvrDeviceIdEntry':cwsXcvrDeviceIdEntry,_Q:cwsXcvrDeviceIdTableSnmpKey,_u:cwsXcvrDeviceIdConnectorType,'cwsXcvrVendorTransmitterTable':cwsXcvrVendorTransmitterTable,'cwsXcvrVendorTransmitterEntry':cwsXcvrVendorTransmitterEntry,_R:cwsXcvrVendorTransmitterTableSnmpKey,_v:cwsXcvrVendorTransmitterNominalBitRate,'cwsXcvrVendorDiagnosticMonitoringTable':cwsXcvrVendorDiagnosticMonitoringTable,'cwsXcvrVendorDiagnosticMonitoringEntry':cwsXcvrVendorDiagnosticMonitoringEntry,_S:cwsXcvrVendorDiagnosticMonitoringTableSnmpKey,_w:cwsXcvrVendorDiagnosticMonitoringRxPowerMeasurement,_x:cwsXcvrVendorDiagnosticMonitoringTxPowerMeasurement,'cwsXcvrTemperatureTable':cwsXcvrTemperatureTable,'cwsXcvrTemperatureEntry':cwsXcvrTemperatureEntry,_T:cwsXcvrTemperatureTableSnmpKey,_y:cwsXcvrTemperatureActual,'cwsXcvrTemperatureStatusTable':cwsXcvrTemperatureStatusTable,'cwsXcvrTemperatureStatusEntry':cwsXcvrTemperatureStatusEntry,_U:cwsXcvrTemperatureStatusTableSnmpKey,_z:cwsXcvrTemperatureStatusHighAlarmStatus,_A0:cwsXcvrTemperatureStatusLowAlarmStatus,_A1:cwsXcvrTemperatureStatusHighWarningStatus,_A2:cwsXcvrTemperatureStatusLowWarningStatus,'cwsXcvrTemperatureThresholdTable':cwsXcvrTemperatureThresholdTable,'cwsXcvrTemperatureThresholdEntry':cwsXcvrTemperatureThresholdEntry,_V:cwsXcvrTemperatureThresholdTableSnmpKey,_A3:cwsXcvrTemperatureThresholdHighAlarmThreshold,_A4:cwsXcvrTemperatureThresholdLowAlarmThreshold,_A5:cwsXcvrTemperatureThresholdHighWarningThreshold,_A6:cwsXcvrTemperatureThresholdLowWarningThreshold,'cwsXcvrChannelDiagnosticsTable':cwsXcvrChannelDiagnosticsTable,'cwsXcvrChannelDiagnosticsEntry':cwsXcvrChannelDiagnosticsEntry,_H:cwsXcvrChannelDiagnosticsChannelNumber,'cwsXcvrChannelRxPowerTable':cwsXcvrChannelRxPowerTable,'cwsXcvrChannelRxPowerEntry':cwsXcvrChannelRxPowerEntry,_W:cwsXcvrChannelRxPowerTableSnmpKey,_A7:cwsXcvrChannelRxPowerActual,'cwsXcvrRxPowerStatusTable':cwsXcvrRxPowerStatusTable,'cwsXcvrRxPowerStatusEntry':cwsXcvrRxPowerStatusEntry,_X:cwsXcvrRxPowerStatusTableSnmpKey,_A8:cwsXcvrRxPowerStatusHighAlarmStatus,_A9:cwsXcvrRxPowerStatusLowAlarmStatus,_AA:cwsXcvrRxPowerStatusHighWarningStatus,_AB:cwsXcvrRxPowerStatusLowWarningStatus,'cwsXcvrRxPowerThresholdTable':cwsXcvrRxPowerThresholdTable,'cwsXcvrRxPowerThresholdEntry':cwsXcvrRxPowerThresholdEntry,_Y:cwsXcvrRxPowerThresholdTableSnmpKey,_AC:cwsXcvrRxPowerThresholdHighAlarmThreshold,_AD:cwsXcvrRxPowerThresholdLowAlarmThreshold,_AE:cwsXcvrRxPowerThresholdHighWarningThreshold,_AF:cwsXcvrRxPowerThresholdLowWarningThreshold,'cwsXcvrChannelTxPowerTable':cwsXcvrChannelTxPowerTable,'cwsXcvrChannelTxPowerEntry':cwsXcvrChannelTxPowerEntry,_Z:cwsXcvrChannelTxPowerTableSnmpKey,_AG:cwsXcvrChannelTxPowerActual,'cwsXcvrTxPowerStatusTable':cwsXcvrTxPowerStatusTable,'cwsXcvrTxPowerStatusEntry':cwsXcvrTxPowerStatusEntry,_a:cwsXcvrTxPowerStatusTableSnmpKey,_AH:cwsXcvrTxPowerStatusHighAlarmStatus,_AI:cwsXcvrTxPowerStatusLowAlarmStatus,_AJ:cwsXcvrTxPowerStatusHighWarningStatus,_AK:cwsXcvrTxPowerStatusLowWarningStatus,'cwsXcvrTxPowerThresholdTable':cwsXcvrTxPowerThresholdTable,'cwsXcvrTxPowerThresholdEntry':cwsXcvrTxPowerThresholdEntry,_b:cwsXcvrTxPowerThresholdTableSnmpKey,_AL:cwsXcvrTxPowerThresholdHighAlarmThreshold,_AM:cwsXcvrTxPowerThresholdLowAlarmThreshold,_AN:cwsXcvrTxPowerThresholdHighWarningThreshold,_AO:cwsXcvrTxPowerThresholdLowWarningThreshold,'cwsXcvrXcvrProfilesTable':cwsXcvrXcvrProfilesTable,'cwsXcvrXcvrProfilesEntry':cwsXcvrXcvrProfilesEntry,_J:cwsXcvrXcvrProfilesXcvrProfileIndex,'cwsXcvrXcvrProfileIdTable':cwsXcvrXcvrProfileIdTable,'cwsXcvrXcvrProfileIdEntry':cwsXcvrXcvrProfileIdEntry,_c:cwsXcvrXcvrProfileIdTableSnmpKey,_AP:cwsXcvrXcvrProfileIdVendorName,_AQ:cwsXcvrXcvrProfileIdVendorOui,_AR:cwsXcvrXcvrProfileIdVendorPn,_AS:cwsXcvrXcvrProfileIdVendorRev,'cwsXcvrXcvrProfilePropertiesTable':cwsXcvrXcvrProfilePropertiesTable,'cwsXcvrXcvrProfilePropertiesEntry':cwsXcvrXcvrProfilePropertiesEntry,_d:cwsXcvrXcvrProfilePropertiesTableSnmpKey,_AT:cwsXcvrXcvrProfilePropertiesSerdesTxEq,_AU:cwsXcvrXcvrProfilePropertiesSerdesRxAmplitude,_AV:cwsXcvrXcvrProfilePropertiesSerdesRxEmphasis})