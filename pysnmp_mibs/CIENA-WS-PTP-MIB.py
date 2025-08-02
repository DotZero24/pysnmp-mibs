_Aa='cienaWsPtpGroup'
_AZ='cwsPtpTraceExpOper'
_AY='cwsPtpTraceExpDapi'
_AX='cwsPtpTraceExpSapi'
_AW='cwsPtpTraceRxOper'
_AV='cwsPtpTraceRxDapi'
_AU='cwsPtpTraceRxSapi'
_AT='cwsPtpTraceTxOperMode'
_AS='cwsPtpTraceTxOperActual'
_AR='cwsPtpTraceTxOper'
_AQ='cwsPtpTraceTxDapi'
_AP='cwsPtpTraceTxSapi'
_AO='cwsPtpTraceMismatchFailMode'
_AN='cwsPtpTraceMismatchMode'
_AM='cwsPtpRsRemoteFault'
_AL='cwsPtpRsLocalFault'
_AK='cwsPtpRsLinkDown'
_AJ='cwsPtpPcsHighBitErrorRate'
_AI='cwsPtpPcsLossOfBlockLock'
_AH='cwsPtpPcsLossOfAlignmentMarker'
_AG='cwsPtpFecLossOfAlignmentMarkerLock'
_AF='cwsPtpPmaSerdesOutOfLock'
_AE='cwsPtpPtpTxOpticalDiagnosticsLossOfLock'
_AD='cwsPtpPtpTxOpticalDiagnosticsLossOfSignal'
_AC='cwsPtpPtpRxOpticalDiagnosticsLossOfLock'
_AB='cwsPtpPtpRxOpticalDiagnosticsLossOfSignal'
_AA='cwsPtpDiagnosticsNumberOfEthernet'
_A9='cwsPtpDiagnosticsNumberOfChannels'
_A8='cwsXcvrTxStatusLowWarningStatus'
_A7='cwsXcvrTxStatusHighWarningStatus'
_A6='cwsXcvrTxStatusLowAlarmStatus'
_A5='cwsXcvrTxStatusHighAlarmStatus'
_A4='cwsXcvrTxPowerMinimumRecordedTime'
_A3='cwsXcvrTxPowerMaximumRecordedTime'
_A2='cwsXcvrTxPowerMinimum'
_A1='cwsXcvrTxPowerMaximum'
_A0='cwsXcvrTxPowerActual'
_z='cwsPtpRxStatusLossOfLock'
_y='cwsPtpRxStatusLossOfSignal'
_x='cwsXcvrRxStatusLowWarningStatus'
_w='cwsXcvrRxStatusHighWarningStatus'
_v='cwsXcvrRxStatusLowAlarmStatus'
_u='cwsXcvrRxStatusHighAlarmStatus'
_t='cwsXcvrRxPowerMinimumRecordedTime'
_s='cwsXcvrRxPowerMaximumRecordedTime'
_r='cwsXcvrRxPowerMinimum'
_q='cwsXcvrRxPowerMaximum'
_p='cwsXcvrRxPowerActual'
_o='cwsPtpChannelsNumberOfChannels'
_n='cwsPtpWavelengthActual'
_m='cwsPtpWavelengthMaxValue'
_l='cwsPtpWavelengthMinValue'
_k='cwsPtpWavelengthValue'
_j='cwsPtpTransmitterState'
_i='cwsPtpPtpPropertiesRate'
_h='cwsPtpPtpPropertiesParentIndex'
_g='cwsPtpPtpPropertiesXcvrType'
_f='cwsPtpPtpStateSpliManagement'
_e='cwsPtpPtpStateOperationalState'
_d='cwsPtpPtpStateAdminState'
_c='cwsPtpPtpIdName'
_b='cwsPtpTraceTableSnmpKey'
_a='cwsPtpRsTableSnmpKey'
_Z='cwsPtpPcsTableSnmpKey'
_Y='cwsPtpFecTableSnmpKey'
_X='cwsPtpPmaTableSnmpKey'
_W='cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey'
_V='cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey'
_U='cwsPtpDiagnosticsTableSnmpKey'
_T='cwsPtpTxStatusTableSnmpKey'
_S='cwsPtpTxPowerTableSnmpKey'
_R='cwsPtpRxStatusTableSnmpKey'
_Q='cwsPtpRxPowerTableSnmpKey'
_P='cwsPtpChannelsTableSnmpKey'
_O='cwsPtpWavelengthTableSnmpKey'
_N='cwsPtpTransmitterTableSnmpKey'
_M='cwsPtpPtpPropertiesTableSnmpKey'
_L='cwsPtpPtpStateTableSnmpKey'
_K='cwsPtpPtpIdTableSnmpKey'
_J='cwsPtpPtpOpticalDiagnosticsChannelNumber'
_I='cwsPtpPtpEthernetDiagnosticsEthernetId'
_H='cwsPtpChannelChannelNumber'
_G='read-write'
_F='not-accessible'
_E='cwsPtpPtpsPtpIndex'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-PTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
ChannelsNumber,Decimal1Dig,Decimal2Dig,Decimal2DigSmall,EnabledDisabledEnum,EnabledDisabledNaEnum,NameString,PtpId,StringMaxl15,StringMaxl32,TraceMismatchFailMode,TraceMismatchMode,TraceTxOperMode,XcvrId,XcvrType=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','ChannelsNumber','Decimal1Dig','Decimal2Dig','Decimal2DigSmall','EnabledDisabledEnum','EnabledDisabledNaEnum','NameString','PtpId','StringMaxl15','StringMaxl32','TraceMismatchFailMode','TraceMismatchMode','TraceTxOperMode','XcvrId','XcvrType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsPtpMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,8))
if mibBuilder.loadTexts:cienaWsPtpMIB.setRevisions(('2017-08-07 00:00','2017-03-02 00:00','2016-12-12 00:00','2016-06-14 00:00','2016-02-01 00:00','2015-04-29 00:00'))
class PtpOpEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('up',0),('down',1),('tuning',2),('fault',3),('unknown',4)))
_CienaWsPtpObjects_ObjectIdentity=ObjectIdentity
cienaWsPtpObjects=_CienaWsPtpObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,8,1))
_CienaWsPtpConformance_ObjectIdentity=ObjectIdentity
cienaWsPtpConformance=_CienaWsPtpConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,8,2))
_CienaWsPtpGroups_ObjectIdentity=ObjectIdentity
cienaWsPtpGroups=_CienaWsPtpGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,8,2,1))
_CienaWsPtpCompliances_ObjectIdentity=ObjectIdentity
cienaWsPtpCompliances=_CienaWsPtpCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,8,2,2))
_CwsPtpPtpsTable_Object=MibTable
cwsPtpPtpsTable=_CwsPtpPtpsTable_Object((1,3,6,1,4,1,1271,3,4,8,3))
if mibBuilder.loadTexts:cwsPtpPtpsTable.setStatus(_A)
_CwsPtpPtpsEntry_Object=MibTableRow
cwsPtpPtpsEntry=_CwsPtpPtpsEntry_Object((1,3,6,1,4,1,1271,3,4,8,3,1))
cwsPtpPtpsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cwsPtpPtpsEntry.setStatus(_A)
class _CwsPtpPtpsPtpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpsPtpIndex_Type.__name__=_D
_CwsPtpPtpsPtpIndex_Object=MibTableColumn
cwsPtpPtpsPtpIndex=_CwsPtpPtpsPtpIndex_Object((1,3,6,1,4,1,1271,3,4,8,3,1,1),_CwsPtpPtpsPtpIndex_Type())
cwsPtpPtpsPtpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpsPtpIndex.setStatus(_A)
_CwsPtpPtpIdTable_Object=MibTable
cwsPtpPtpIdTable=_CwsPtpPtpIdTable_Object((1,3,6,1,4,1,1271,3,4,8,4))
if mibBuilder.loadTexts:cwsPtpPtpIdTable.setStatus(_A)
_CwsPtpPtpIdEntry_Object=MibTableRow
cwsPtpPtpIdEntry=_CwsPtpPtpIdEntry_Object((1,3,6,1,4,1,1271,3,4,8,4,1))
cwsPtpPtpIdEntry.setIndexNames((0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:cwsPtpPtpIdEntry.setStatus(_A)
class _CwsPtpPtpIdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpIdTableSnmpKey_Type.__name__=_D
_CwsPtpPtpIdTableSnmpKey_Object=MibTableColumn
cwsPtpPtpIdTableSnmpKey=_CwsPtpPtpIdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,4,1,1),_CwsPtpPtpIdTableSnmpKey_Type())
cwsPtpPtpIdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPtpIdTableSnmpKey.setStatus(_A)
_CwsPtpPtpIdName_Type=NameString
_CwsPtpPtpIdName_Object=MibTableColumn
cwsPtpPtpIdName=_CwsPtpPtpIdName_Object((1,3,6,1,4,1,1271,3,4,8,4,1,2),_CwsPtpPtpIdName_Type())
cwsPtpPtpIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpIdName.setStatus(_A)
_CwsPtpPtpStateTable_Object=MibTable
cwsPtpPtpStateTable=_CwsPtpPtpStateTable_Object((1,3,6,1,4,1,1271,3,4,8,5))
if mibBuilder.loadTexts:cwsPtpPtpStateTable.setStatus(_A)
_CwsPtpPtpStateEntry_Object=MibTableRow
cwsPtpPtpStateEntry=_CwsPtpPtpStateEntry_Object((1,3,6,1,4,1,1271,3,4,8,5,1))
cwsPtpPtpStateEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:cwsPtpPtpStateEntry.setStatus(_A)
class _CwsPtpPtpStateTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpStateTableSnmpKey_Type.__name__=_D
_CwsPtpPtpStateTableSnmpKey_Object=MibTableColumn
cwsPtpPtpStateTableSnmpKey=_CwsPtpPtpStateTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,5,1,1),_CwsPtpPtpStateTableSnmpKey_Type())
cwsPtpPtpStateTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPtpStateTableSnmpKey.setStatus(_A)
_CwsPtpPtpStateAdminState_Type=EnabledDisabledEnum
_CwsPtpPtpStateAdminState_Object=MibTableColumn
cwsPtpPtpStateAdminState=_CwsPtpPtpStateAdminState_Object((1,3,6,1,4,1,1271,3,4,8,5,1,2),_CwsPtpPtpStateAdminState_Type())
cwsPtpPtpStateAdminState.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpPtpStateAdminState.setStatus(_A)
_CwsPtpPtpStateOperationalState_Type=PtpOpEnum
_CwsPtpPtpStateOperationalState_Object=MibTableColumn
cwsPtpPtpStateOperationalState=_CwsPtpPtpStateOperationalState_Object((1,3,6,1,4,1,1271,3,4,8,5,1,3),_CwsPtpPtpStateOperationalState_Type())
cwsPtpPtpStateOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpStateOperationalState.setStatus(_A)
_CwsPtpPtpStateSpliManagement_Type=EnabledDisabledEnum
_CwsPtpPtpStateSpliManagement_Object=MibTableColumn
cwsPtpPtpStateSpliManagement=_CwsPtpPtpStateSpliManagement_Object((1,3,6,1,4,1,1271,3,4,8,5,1,4),_CwsPtpPtpStateSpliManagement_Type())
cwsPtpPtpStateSpliManagement.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpPtpStateSpliManagement.setStatus(_A)
_CwsPtpPtpPropertiesTable_Object=MibTable
cwsPtpPtpPropertiesTable=_CwsPtpPtpPropertiesTable_Object((1,3,6,1,4,1,1271,3,4,8,6))
if mibBuilder.loadTexts:cwsPtpPtpPropertiesTable.setStatus(_A)
_CwsPtpPtpPropertiesEntry_Object=MibTableRow
cwsPtpPtpPropertiesEntry=_CwsPtpPtpPropertiesEntry_Object((1,3,6,1,4,1,1271,3,4,8,6,1))
cwsPtpPtpPropertiesEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:cwsPtpPtpPropertiesEntry.setStatus(_A)
class _CwsPtpPtpPropertiesTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpPropertiesTableSnmpKey_Type.__name__=_D
_CwsPtpPtpPropertiesTableSnmpKey_Object=MibTableColumn
cwsPtpPtpPropertiesTableSnmpKey=_CwsPtpPtpPropertiesTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,6,1,1),_CwsPtpPtpPropertiesTableSnmpKey_Type())
cwsPtpPtpPropertiesTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPtpPropertiesTableSnmpKey.setStatus(_A)
_CwsPtpPtpPropertiesXcvrType_Type=XcvrType
_CwsPtpPtpPropertiesXcvrType_Object=MibTableColumn
cwsPtpPtpPropertiesXcvrType=_CwsPtpPtpPropertiesXcvrType_Object((1,3,6,1,4,1,1271,3,4,8,6,1,2),_CwsPtpPtpPropertiesXcvrType_Type())
cwsPtpPtpPropertiesXcvrType.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpPtpPropertiesXcvrType.setStatus(_A)
_CwsPtpPtpPropertiesParentIndex_Type=XcvrId
_CwsPtpPtpPropertiesParentIndex_Object=MibTableColumn
cwsPtpPtpPropertiesParentIndex=_CwsPtpPtpPropertiesParentIndex_Object((1,3,6,1,4,1,1271,3,4,8,6,1,3),_CwsPtpPtpPropertiesParentIndex_Type())
cwsPtpPtpPropertiesParentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpPropertiesParentIndex.setStatus(_A)
class _CwsPtpPtpPropertiesRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),('linerate10dot3125gbps',1),('linerate41dot25gbps',2),('linerate103dot125gpbs',3),('linerate2xotu4',4),('linerate1xotu4',5),('linerate1dot5xotu4',6)))
_CwsPtpPtpPropertiesRate_Type.__name__=_D
_CwsPtpPtpPropertiesRate_Object=MibTableColumn
cwsPtpPtpPropertiesRate=_CwsPtpPtpPropertiesRate_Object((1,3,6,1,4,1,1271,3,4,8,6,1,4),_CwsPtpPtpPropertiesRate_Type())
cwsPtpPtpPropertiesRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpPropertiesRate.setStatus(_A)
_CwsPtpTransmitterTable_Object=MibTable
cwsPtpTransmitterTable=_CwsPtpTransmitterTable_Object((1,3,6,1,4,1,1271,3,4,8,7))
if mibBuilder.loadTexts:cwsPtpTransmitterTable.setStatus(_A)
_CwsPtpTransmitterEntry_Object=MibTableRow
cwsPtpTransmitterEntry=_CwsPtpTransmitterEntry_Object((1,3,6,1,4,1,1271,3,4,8,7,1))
cwsPtpTransmitterEntry.setIndexNames((0,_B,_E),(0,_B,_N))
if mibBuilder.loadTexts:cwsPtpTransmitterEntry.setStatus(_A)
class _CwsPtpTransmitterTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpTransmitterTableSnmpKey_Type.__name__=_D
_CwsPtpTransmitterTableSnmpKey_Object=MibTableColumn
cwsPtpTransmitterTableSnmpKey=_CwsPtpTransmitterTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,7,1,1),_CwsPtpTransmitterTableSnmpKey_Type())
cwsPtpTransmitterTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpTransmitterTableSnmpKey.setStatus(_A)
_CwsPtpTransmitterState_Type=EnabledDisabledNaEnum
_CwsPtpTransmitterState_Object=MibTableColumn
cwsPtpTransmitterState=_CwsPtpTransmitterState_Object((1,3,6,1,4,1,1271,3,4,8,7,1,2),_CwsPtpTransmitterState_Type())
cwsPtpTransmitterState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpTransmitterState.setStatus(_A)
_CwsPtpWavelengthTable_Object=MibTable
cwsPtpWavelengthTable=_CwsPtpWavelengthTable_Object((1,3,6,1,4,1,1271,3,4,8,8))
if mibBuilder.loadTexts:cwsPtpWavelengthTable.setStatus(_A)
_CwsPtpWavelengthEntry_Object=MibTableRow
cwsPtpWavelengthEntry=_CwsPtpWavelengthEntry_Object((1,3,6,1,4,1,1271,3,4,8,8,1))
cwsPtpWavelengthEntry.setIndexNames((0,_B,_E),(0,_B,_O))
if mibBuilder.loadTexts:cwsPtpWavelengthEntry.setStatus(_A)
class _CwsPtpWavelengthTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpWavelengthTableSnmpKey_Type.__name__=_D
_CwsPtpWavelengthTableSnmpKey_Object=MibTableColumn
cwsPtpWavelengthTableSnmpKey=_CwsPtpWavelengthTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,8,1,1),_CwsPtpWavelengthTableSnmpKey_Type())
cwsPtpWavelengthTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpWavelengthTableSnmpKey.setStatus(_A)
_CwsPtpWavelengthValue_Type=Decimal2Dig
_CwsPtpWavelengthValue_Object=MibTableColumn
cwsPtpWavelengthValue=_CwsPtpWavelengthValue_Object((1,3,6,1,4,1,1271,3,4,8,8,1,2),_CwsPtpWavelengthValue_Type())
cwsPtpWavelengthValue.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpWavelengthValue.setStatus(_A)
_CwsPtpWavelengthMinValue_Type=Decimal2DigSmall
_CwsPtpWavelengthMinValue_Object=MibTableColumn
cwsPtpWavelengthMinValue=_CwsPtpWavelengthMinValue_Object((1,3,6,1,4,1,1271,3,4,8,8,1,3),_CwsPtpWavelengthMinValue_Type())
cwsPtpWavelengthMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpWavelengthMinValue.setStatus(_A)
_CwsPtpWavelengthMaxValue_Type=Decimal2DigSmall
_CwsPtpWavelengthMaxValue_Object=MibTableColumn
cwsPtpWavelengthMaxValue=_CwsPtpWavelengthMaxValue_Object((1,3,6,1,4,1,1271,3,4,8,8,1,4),_CwsPtpWavelengthMaxValue_Type())
cwsPtpWavelengthMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpWavelengthMaxValue.setStatus(_A)
_CwsPtpWavelengthActual_Type=Decimal2Dig
_CwsPtpWavelengthActual_Object=MibTableColumn
cwsPtpWavelengthActual=_CwsPtpWavelengthActual_Object((1,3,6,1,4,1,1271,3,4,8,8,1,5),_CwsPtpWavelengthActual_Type())
cwsPtpWavelengthActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpWavelengthActual.setStatus(_A)
_CwsPtpChannelsTable_Object=MibTable
cwsPtpChannelsTable=_CwsPtpChannelsTable_Object((1,3,6,1,4,1,1271,3,4,8,9))
if mibBuilder.loadTexts:cwsPtpChannelsTable.setStatus(_A)
_CwsPtpChannelsEntry_Object=MibTableRow
cwsPtpChannelsEntry=_CwsPtpChannelsEntry_Object((1,3,6,1,4,1,1271,3,4,8,9,1))
cwsPtpChannelsEntry.setIndexNames((0,_B,_E),(0,_B,_P))
if mibBuilder.loadTexts:cwsPtpChannelsEntry.setStatus(_A)
class _CwsPtpChannelsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpChannelsTableSnmpKey_Type.__name__=_D
_CwsPtpChannelsTableSnmpKey_Object=MibTableColumn
cwsPtpChannelsTableSnmpKey=_CwsPtpChannelsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,9,1,1),_CwsPtpChannelsTableSnmpKey_Type())
cwsPtpChannelsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpChannelsTableSnmpKey.setStatus(_A)
_CwsPtpChannelsNumberOfChannels_Type=ChannelsNumber
_CwsPtpChannelsNumberOfChannels_Object=MibTableColumn
cwsPtpChannelsNumberOfChannels=_CwsPtpChannelsNumberOfChannels_Object((1,3,6,1,4,1,1271,3,4,8,9,1,2),_CwsPtpChannelsNumberOfChannels_Type())
cwsPtpChannelsNumberOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpChannelsNumberOfChannels.setStatus(_A)
_CwsPtpChannelTable_Object=MibTable
cwsPtpChannelTable=_CwsPtpChannelTable_Object((1,3,6,1,4,1,1271,3,4,8,10))
if mibBuilder.loadTexts:cwsPtpChannelTable.setStatus(_A)
_CwsPtpChannelEntry_Object=MibTableRow
cwsPtpChannelEntry=_CwsPtpChannelEntry_Object((1,3,6,1,4,1,1271,3,4,8,10,1))
cwsPtpChannelEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:cwsPtpChannelEntry.setStatus(_A)
class _CwsPtpChannelChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpChannelChannelNumber_Type.__name__=_D
_CwsPtpChannelChannelNumber_Object=MibTableColumn
cwsPtpChannelChannelNumber=_CwsPtpChannelChannelNumber_Object((1,3,6,1,4,1,1271,3,4,8,10,1,1),_CwsPtpChannelChannelNumber_Type())
cwsPtpChannelChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpChannelChannelNumber.setStatus(_A)
_CwsPtpRxPowerTable_Object=MibTable
cwsPtpRxPowerTable=_CwsPtpRxPowerTable_Object((1,3,6,1,4,1,1271,3,4,8,11))
if mibBuilder.loadTexts:cwsPtpRxPowerTable.setStatus(_A)
_CwsPtpRxPowerEntry_Object=MibTableRow
cwsPtpRxPowerEntry=_CwsPtpRxPowerEntry_Object((1,3,6,1,4,1,1271,3,4,8,11,1))
cwsPtpRxPowerEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:cwsPtpRxPowerEntry.setStatus(_A)
class _CwsPtpRxPowerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpRxPowerTableSnmpKey_Type.__name__=_D
_CwsPtpRxPowerTableSnmpKey_Object=MibTableColumn
cwsPtpRxPowerTableSnmpKey=_CwsPtpRxPowerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,11,1,1),_CwsPtpRxPowerTableSnmpKey_Type())
cwsPtpRxPowerTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpRxPowerTableSnmpKey.setStatus(_A)
_CwsXcvrRxPowerActual_Type=Decimal1Dig
_CwsXcvrRxPowerActual_Object=MibTableColumn
cwsXcvrRxPowerActual=_CwsXcvrRxPowerActual_Object((1,3,6,1,4,1,1271,3,4,8,11,1,2),_CwsXcvrRxPowerActual_Type())
cwsXcvrRxPowerActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerActual.setStatus(_A)
_CwsXcvrRxPowerMaximum_Type=Decimal1Dig
_CwsXcvrRxPowerMaximum_Object=MibTableColumn
cwsXcvrRxPowerMaximum=_CwsXcvrRxPowerMaximum_Object((1,3,6,1,4,1,1271,3,4,8,11,1,3),_CwsXcvrRxPowerMaximum_Type())
cwsXcvrRxPowerMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerMaximum.setStatus(_A)
_CwsXcvrRxPowerMinimum_Type=Decimal1Dig
_CwsXcvrRxPowerMinimum_Object=MibTableColumn
cwsXcvrRxPowerMinimum=_CwsXcvrRxPowerMinimum_Object((1,3,6,1,4,1,1271,3,4,8,11,1,4),_CwsXcvrRxPowerMinimum_Type())
cwsXcvrRxPowerMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerMinimum.setStatus(_A)
_CwsXcvrRxPowerMaximumRecordedTime_Type=StringMaxl32
_CwsXcvrRxPowerMaximumRecordedTime_Object=MibTableColumn
cwsXcvrRxPowerMaximumRecordedTime=_CwsXcvrRxPowerMaximumRecordedTime_Object((1,3,6,1,4,1,1271,3,4,8,11,1,5),_CwsXcvrRxPowerMaximumRecordedTime_Type())
cwsXcvrRxPowerMaximumRecordedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerMaximumRecordedTime.setStatus(_A)
_CwsXcvrRxPowerMinimumRecordedTime_Type=StringMaxl32
_CwsXcvrRxPowerMinimumRecordedTime_Object=MibTableColumn
cwsXcvrRxPowerMinimumRecordedTime=_CwsXcvrRxPowerMinimumRecordedTime_Object((1,3,6,1,4,1,1271,3,4,8,11,1,6),_CwsXcvrRxPowerMinimumRecordedTime_Type())
cwsXcvrRxPowerMinimumRecordedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxPowerMinimumRecordedTime.setStatus(_A)
_CwsPtpRxStatusTable_Object=MibTable
cwsPtpRxStatusTable=_CwsPtpRxStatusTable_Object((1,3,6,1,4,1,1271,3,4,8,12))
if mibBuilder.loadTexts:cwsPtpRxStatusTable.setStatus(_A)
_CwsPtpRxStatusEntry_Object=MibTableRow
cwsPtpRxStatusEntry=_CwsPtpRxStatusEntry_Object((1,3,6,1,4,1,1271,3,4,8,12,1))
cwsPtpRxStatusEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_R))
if mibBuilder.loadTexts:cwsPtpRxStatusEntry.setStatus(_A)
class _CwsPtpRxStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpRxStatusTableSnmpKey_Type.__name__=_D
_CwsPtpRxStatusTableSnmpKey_Object=MibTableColumn
cwsPtpRxStatusTableSnmpKey=_CwsPtpRxStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,12,1,1),_CwsPtpRxStatusTableSnmpKey_Type())
cwsPtpRxStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpRxStatusTableSnmpKey.setStatus(_A)
_CwsXcvrRxStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrRxStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrRxStatusHighAlarmStatus=_CwsXcvrRxStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,8,12,1,2),_CwsXcvrRxStatusHighAlarmStatus_Type())
cwsXcvrRxStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrRxStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrRxStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrRxStatusLowAlarmStatus=_CwsXcvrRxStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,8,12,1,3),_CwsXcvrRxStatusLowAlarmStatus_Type())
cwsXcvrRxStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrRxStatusHighWarningStatus_Type=TruthValue
_CwsXcvrRxStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrRxStatusHighWarningStatus=_CwsXcvrRxStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,8,12,1,4),_CwsXcvrRxStatusHighWarningStatus_Type())
cwsXcvrRxStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxStatusHighWarningStatus.setStatus(_A)
_CwsXcvrRxStatusLowWarningStatus_Type=TruthValue
_CwsXcvrRxStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrRxStatusLowWarningStatus=_CwsXcvrRxStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,8,12,1,5),_CwsXcvrRxStatusLowWarningStatus_Type())
cwsXcvrRxStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrRxStatusLowWarningStatus.setStatus(_A)
_CwsPtpRxStatusLossOfSignal_Type=TruthValue
_CwsPtpRxStatusLossOfSignal_Object=MibTableColumn
cwsPtpRxStatusLossOfSignal=_CwsPtpRxStatusLossOfSignal_Object((1,3,6,1,4,1,1271,3,4,8,12,1,6),_CwsPtpRxStatusLossOfSignal_Type())
cwsPtpRxStatusLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpRxStatusLossOfSignal.setStatus(_A)
_CwsPtpRxStatusLossOfLock_Type=TruthValue
_CwsPtpRxStatusLossOfLock_Object=MibTableColumn
cwsPtpRxStatusLossOfLock=_CwsPtpRxStatusLossOfLock_Object((1,3,6,1,4,1,1271,3,4,8,12,1,7),_CwsPtpRxStatusLossOfLock_Type())
cwsPtpRxStatusLossOfLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpRxStatusLossOfLock.setStatus(_A)
_CwsPtpTxPowerTable_Object=MibTable
cwsPtpTxPowerTable=_CwsPtpTxPowerTable_Object((1,3,6,1,4,1,1271,3,4,8,13))
if mibBuilder.loadTexts:cwsPtpTxPowerTable.setStatus(_A)
_CwsPtpTxPowerEntry_Object=MibTableRow
cwsPtpTxPowerEntry=_CwsPtpTxPowerEntry_Object((1,3,6,1,4,1,1271,3,4,8,13,1))
cwsPtpTxPowerEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_S))
if mibBuilder.loadTexts:cwsPtpTxPowerEntry.setStatus(_A)
class _CwsPtpTxPowerTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpTxPowerTableSnmpKey_Type.__name__=_D
_CwsPtpTxPowerTableSnmpKey_Object=MibTableColumn
cwsPtpTxPowerTableSnmpKey=_CwsPtpTxPowerTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,13,1,1),_CwsPtpTxPowerTableSnmpKey_Type())
cwsPtpTxPowerTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpTxPowerTableSnmpKey.setStatus(_A)
_CwsXcvrTxPowerActual_Type=Decimal1Dig
_CwsXcvrTxPowerActual_Object=MibTableColumn
cwsXcvrTxPowerActual=_CwsXcvrTxPowerActual_Object((1,3,6,1,4,1,1271,3,4,8,13,1,2),_CwsXcvrTxPowerActual_Type())
cwsXcvrTxPowerActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerActual.setStatus(_A)
_CwsXcvrTxPowerMaximum_Type=Decimal1Dig
_CwsXcvrTxPowerMaximum_Object=MibTableColumn
cwsXcvrTxPowerMaximum=_CwsXcvrTxPowerMaximum_Object((1,3,6,1,4,1,1271,3,4,8,13,1,3),_CwsXcvrTxPowerMaximum_Type())
cwsXcvrTxPowerMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerMaximum.setStatus(_A)
_CwsXcvrTxPowerMinimum_Type=Decimal1Dig
_CwsXcvrTxPowerMinimum_Object=MibTableColumn
cwsXcvrTxPowerMinimum=_CwsXcvrTxPowerMinimum_Object((1,3,6,1,4,1,1271,3,4,8,13,1,4),_CwsXcvrTxPowerMinimum_Type())
cwsXcvrTxPowerMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerMinimum.setStatus(_A)
_CwsXcvrTxPowerMaximumRecordedTime_Type=StringMaxl32
_CwsXcvrTxPowerMaximumRecordedTime_Object=MibTableColumn
cwsXcvrTxPowerMaximumRecordedTime=_CwsXcvrTxPowerMaximumRecordedTime_Object((1,3,6,1,4,1,1271,3,4,8,13,1,5),_CwsXcvrTxPowerMaximumRecordedTime_Type())
cwsXcvrTxPowerMaximumRecordedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerMaximumRecordedTime.setStatus(_A)
_CwsXcvrTxPowerMinimumRecordedTime_Type=StringMaxl32
_CwsXcvrTxPowerMinimumRecordedTime_Object=MibTableColumn
cwsXcvrTxPowerMinimumRecordedTime=_CwsXcvrTxPowerMinimumRecordedTime_Object((1,3,6,1,4,1,1271,3,4,8,13,1,6),_CwsXcvrTxPowerMinimumRecordedTime_Type())
cwsXcvrTxPowerMinimumRecordedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxPowerMinimumRecordedTime.setStatus(_A)
_CwsPtpTxStatusTable_Object=MibTable
cwsPtpTxStatusTable=_CwsPtpTxStatusTable_Object((1,3,6,1,4,1,1271,3,4,8,14))
if mibBuilder.loadTexts:cwsPtpTxStatusTable.setStatus(_A)
_CwsPtpTxStatusEntry_Object=MibTableRow
cwsPtpTxStatusEntry=_CwsPtpTxStatusEntry_Object((1,3,6,1,4,1,1271,3,4,8,14,1))
cwsPtpTxStatusEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_T))
if mibBuilder.loadTexts:cwsPtpTxStatusEntry.setStatus(_A)
class _CwsPtpTxStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpTxStatusTableSnmpKey_Type.__name__=_D
_CwsPtpTxStatusTableSnmpKey_Object=MibTableColumn
cwsPtpTxStatusTableSnmpKey=_CwsPtpTxStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,14,1,1),_CwsPtpTxStatusTableSnmpKey_Type())
cwsPtpTxStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpTxStatusTableSnmpKey.setStatus(_A)
_CwsXcvrTxStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrTxStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrTxStatusHighAlarmStatus=_CwsXcvrTxStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,8,14,1,2),_CwsXcvrTxStatusHighAlarmStatus_Type())
cwsXcvrTxStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrTxStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrTxStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrTxStatusLowAlarmStatus=_CwsXcvrTxStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,8,14,1,3),_CwsXcvrTxStatusLowAlarmStatus_Type())
cwsXcvrTxStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrTxStatusHighWarningStatus_Type=TruthValue
_CwsXcvrTxStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrTxStatusHighWarningStatus=_CwsXcvrTxStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,8,14,1,4),_CwsXcvrTxStatusHighWarningStatus_Type())
cwsXcvrTxStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxStatusHighWarningStatus.setStatus(_A)
_CwsXcvrTxStatusLowWarningStatus_Type=TruthValue
_CwsXcvrTxStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrTxStatusLowWarningStatus=_CwsXcvrTxStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,8,14,1,5),_CwsXcvrTxStatusLowWarningStatus_Type())
cwsXcvrTxStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrTxStatusLowWarningStatus.setStatus(_A)
_CwsPtpDiagnosticsTable_Object=MibTable
cwsPtpDiagnosticsTable=_CwsPtpDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,8,15))
if mibBuilder.loadTexts:cwsPtpDiagnosticsTable.setStatus(_A)
_CwsPtpDiagnosticsEntry_Object=MibTableRow
cwsPtpDiagnosticsEntry=_CwsPtpDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,8,15,1))
cwsPtpDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_U))
if mibBuilder.loadTexts:cwsPtpDiagnosticsEntry.setStatus(_A)
class _CwsPtpDiagnosticsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpDiagnosticsTableSnmpKey_Type.__name__=_D
_CwsPtpDiagnosticsTableSnmpKey_Object=MibTableColumn
cwsPtpDiagnosticsTableSnmpKey=_CwsPtpDiagnosticsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,15,1,1),_CwsPtpDiagnosticsTableSnmpKey_Type())
cwsPtpDiagnosticsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpDiagnosticsTableSnmpKey.setStatus(_A)
_CwsPtpDiagnosticsNumberOfChannels_Type=ChannelsNumber
_CwsPtpDiagnosticsNumberOfChannels_Object=MibTableColumn
cwsPtpDiagnosticsNumberOfChannels=_CwsPtpDiagnosticsNumberOfChannels_Object((1,3,6,1,4,1,1271,3,4,8,15,1,2),_CwsPtpDiagnosticsNumberOfChannels_Type())
cwsPtpDiagnosticsNumberOfChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpDiagnosticsNumberOfChannels.setStatus(_A)
_CwsPtpDiagnosticsNumberOfEthernet_Type=Unsigned32
_CwsPtpDiagnosticsNumberOfEthernet_Object=MibTableColumn
cwsPtpDiagnosticsNumberOfEthernet=_CwsPtpDiagnosticsNumberOfEthernet_Object((1,3,6,1,4,1,1271,3,4,8,15,1,3),_CwsPtpDiagnosticsNumberOfEthernet_Type())
cwsPtpDiagnosticsNumberOfEthernet.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpDiagnosticsNumberOfEthernet.setStatus(_A)
_CwsPtpPtpOpticalDiagnosticsTable_Object=MibTable
cwsPtpPtpOpticalDiagnosticsTable=_CwsPtpPtpOpticalDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,8,16))
if mibBuilder.loadTexts:cwsPtpPtpOpticalDiagnosticsTable.setStatus(_A)
_CwsPtpPtpOpticalDiagnosticsEntry_Object=MibTableRow
cwsPtpPtpOpticalDiagnosticsEntry=_CwsPtpPtpOpticalDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,8,16,1))
cwsPtpPtpOpticalDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:cwsPtpPtpOpticalDiagnosticsEntry.setStatus(_A)
class _CwsPtpPtpOpticalDiagnosticsChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpOpticalDiagnosticsChannelNumber_Type.__name__=_D
_CwsPtpPtpOpticalDiagnosticsChannelNumber_Object=MibTableColumn
cwsPtpPtpOpticalDiagnosticsChannelNumber=_CwsPtpPtpOpticalDiagnosticsChannelNumber_Object((1,3,6,1,4,1,1271,3,4,8,16,1,1),_CwsPtpPtpOpticalDiagnosticsChannelNumber_Type())
cwsPtpPtpOpticalDiagnosticsChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpOpticalDiagnosticsChannelNumber.setStatus(_A)
_CwsPtpPtpRxOpticalDiagnosticsTable_Object=MibTable
cwsPtpPtpRxOpticalDiagnosticsTable=_CwsPtpPtpRxOpticalDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,8,17))
if mibBuilder.loadTexts:cwsPtpPtpRxOpticalDiagnosticsTable.setStatus(_A)
_CwsPtpPtpRxOpticalDiagnosticsEntry_Object=MibTableRow
cwsPtpPtpRxOpticalDiagnosticsEntry=_CwsPtpPtpRxOpticalDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,8,17,1))
cwsPtpPtpRxOpticalDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_J),(0,_B,_V))
if mibBuilder.loadTexts:cwsPtpPtpRxOpticalDiagnosticsEntry.setStatus(_A)
class _CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type.__name__=_D
_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Object=MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey=_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,17,1,1),_CwsPtpPtpRxOpticalDiagnosticsTableSnmpKey_Type())
cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey.setStatus(_A)
_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Type=TruthValue
_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Object=MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsLossOfSignal=_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Object((1,3,6,1,4,1,1271,3,4,8,17,1,2),_CwsPtpPtpRxOpticalDiagnosticsLossOfSignal_Type())
cwsPtpPtpRxOpticalDiagnosticsLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpRxOpticalDiagnosticsLossOfSignal.setStatus(_A)
_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Type=TruthValue
_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Object=MibTableColumn
cwsPtpPtpRxOpticalDiagnosticsLossOfLock=_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Object((1,3,6,1,4,1,1271,3,4,8,17,1,3),_CwsPtpPtpRxOpticalDiagnosticsLossOfLock_Type())
cwsPtpPtpRxOpticalDiagnosticsLossOfLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpRxOpticalDiagnosticsLossOfLock.setStatus(_A)
_CwsPtpPtpTxOpticalDiagnosticsTable_Object=MibTable
cwsPtpPtpTxOpticalDiagnosticsTable=_CwsPtpPtpTxOpticalDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,8,18))
if mibBuilder.loadTexts:cwsPtpPtpTxOpticalDiagnosticsTable.setStatus(_A)
_CwsPtpPtpTxOpticalDiagnosticsEntry_Object=MibTableRow
cwsPtpPtpTxOpticalDiagnosticsEntry=_CwsPtpPtpTxOpticalDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,8,18,1))
cwsPtpPtpTxOpticalDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_J),(0,_B,_W))
if mibBuilder.loadTexts:cwsPtpPtpTxOpticalDiagnosticsEntry.setStatus(_A)
class _CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type.__name__=_D
_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Object=MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey=_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,18,1,1),_CwsPtpPtpTxOpticalDiagnosticsTableSnmpKey_Type())
cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey.setStatus(_A)
_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Type=TruthValue
_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Object=MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsLossOfSignal=_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Object((1,3,6,1,4,1,1271,3,4,8,18,1,2),_CwsPtpPtpTxOpticalDiagnosticsLossOfSignal_Type())
cwsPtpPtpTxOpticalDiagnosticsLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpTxOpticalDiagnosticsLossOfSignal.setStatus(_A)
_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Type=TruthValue
_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Object=MibTableColumn
cwsPtpPtpTxOpticalDiagnosticsLossOfLock=_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Object((1,3,6,1,4,1,1271,3,4,8,18,1,3),_CwsPtpPtpTxOpticalDiagnosticsLossOfLock_Type())
cwsPtpPtpTxOpticalDiagnosticsLossOfLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpTxOpticalDiagnosticsLossOfLock.setStatus(_A)
_CwsPtpPtpEthernetDiagnosticsTable_Object=MibTable
cwsPtpPtpEthernetDiagnosticsTable=_CwsPtpPtpEthernetDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,8,19))
if mibBuilder.loadTexts:cwsPtpPtpEthernetDiagnosticsTable.setStatus(_A)
_CwsPtpPtpEthernetDiagnosticsEntry_Object=MibTableRow
cwsPtpPtpEthernetDiagnosticsEntry=_CwsPtpPtpEthernetDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,8,19,1))
cwsPtpPtpEthernetDiagnosticsEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:cwsPtpPtpEthernetDiagnosticsEntry.setStatus(_A)
class _CwsPtpPtpEthernetDiagnosticsEthernetId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPtpEthernetDiagnosticsEthernetId_Type.__name__=_D
_CwsPtpPtpEthernetDiagnosticsEthernetId_Object=MibTableColumn
cwsPtpPtpEthernetDiagnosticsEthernetId=_CwsPtpPtpEthernetDiagnosticsEthernetId_Object((1,3,6,1,4,1,1271,3,4,8,19,1,1),_CwsPtpPtpEthernetDiagnosticsEthernetId_Type())
cwsPtpPtpEthernetDiagnosticsEthernetId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPtpEthernetDiagnosticsEthernetId.setStatus(_A)
_CwsPtpPmaTable_Object=MibTable
cwsPtpPmaTable=_CwsPtpPmaTable_Object((1,3,6,1,4,1,1271,3,4,8,20))
if mibBuilder.loadTexts:cwsPtpPmaTable.setStatus(_A)
_CwsPtpPmaEntry_Object=MibTableRow
cwsPtpPmaEntry=_CwsPtpPmaEntry_Object((1,3,6,1,4,1,1271,3,4,8,20,1))
cwsPtpPmaEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_X))
if mibBuilder.loadTexts:cwsPtpPmaEntry.setStatus(_A)
class _CwsPtpPmaTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPmaTableSnmpKey_Type.__name__=_D
_CwsPtpPmaTableSnmpKey_Object=MibTableColumn
cwsPtpPmaTableSnmpKey=_CwsPtpPmaTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,20,1,1),_CwsPtpPmaTableSnmpKey_Type())
cwsPtpPmaTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPmaTableSnmpKey.setStatus(_A)
_CwsPtpPmaSerdesOutOfLock_Type=TruthValue
_CwsPtpPmaSerdesOutOfLock_Object=MibTableColumn
cwsPtpPmaSerdesOutOfLock=_CwsPtpPmaSerdesOutOfLock_Object((1,3,6,1,4,1,1271,3,4,8,20,1,2),_CwsPtpPmaSerdesOutOfLock_Type())
cwsPtpPmaSerdesOutOfLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPmaSerdesOutOfLock.setStatus(_A)
_CwsPtpFecTable_Object=MibTable
cwsPtpFecTable=_CwsPtpFecTable_Object((1,3,6,1,4,1,1271,3,4,8,21))
if mibBuilder.loadTexts:cwsPtpFecTable.setStatus(_A)
_CwsPtpFecEntry_Object=MibTableRow
cwsPtpFecEntry=_CwsPtpFecEntry_Object((1,3,6,1,4,1,1271,3,4,8,21,1))
cwsPtpFecEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_Y))
if mibBuilder.loadTexts:cwsPtpFecEntry.setStatus(_A)
class _CwsPtpFecTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpFecTableSnmpKey_Type.__name__=_D
_CwsPtpFecTableSnmpKey_Object=MibTableColumn
cwsPtpFecTableSnmpKey=_CwsPtpFecTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,21,1,1),_CwsPtpFecTableSnmpKey_Type())
cwsPtpFecTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpFecTableSnmpKey.setStatus(_A)
_CwsPtpFecLossOfAlignmentMarkerLock_Type=TruthValue
_CwsPtpFecLossOfAlignmentMarkerLock_Object=MibTableColumn
cwsPtpFecLossOfAlignmentMarkerLock=_CwsPtpFecLossOfAlignmentMarkerLock_Object((1,3,6,1,4,1,1271,3,4,8,21,1,2),_CwsPtpFecLossOfAlignmentMarkerLock_Type())
cwsPtpFecLossOfAlignmentMarkerLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpFecLossOfAlignmentMarkerLock.setStatus(_A)
_CwsPtpPcsTable_Object=MibTable
cwsPtpPcsTable=_CwsPtpPcsTable_Object((1,3,6,1,4,1,1271,3,4,8,22))
if mibBuilder.loadTexts:cwsPtpPcsTable.setStatus(_A)
_CwsPtpPcsEntry_Object=MibTableRow
cwsPtpPcsEntry=_CwsPtpPcsEntry_Object((1,3,6,1,4,1,1271,3,4,8,22,1))
cwsPtpPcsEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_Z))
if mibBuilder.loadTexts:cwsPtpPcsEntry.setStatus(_A)
class _CwsPtpPcsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpPcsTableSnmpKey_Type.__name__=_D
_CwsPtpPcsTableSnmpKey_Object=MibTableColumn
cwsPtpPcsTableSnmpKey=_CwsPtpPcsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,22,1,1),_CwsPtpPcsTableSnmpKey_Type())
cwsPtpPcsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpPcsTableSnmpKey.setStatus(_A)
_CwsPtpPcsLossOfAlignmentMarker_Type=TruthValue
_CwsPtpPcsLossOfAlignmentMarker_Object=MibTableColumn
cwsPtpPcsLossOfAlignmentMarker=_CwsPtpPcsLossOfAlignmentMarker_Object((1,3,6,1,4,1,1271,3,4,8,22,1,2),_CwsPtpPcsLossOfAlignmentMarker_Type())
cwsPtpPcsLossOfAlignmentMarker.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPcsLossOfAlignmentMarker.setStatus(_A)
_CwsPtpPcsLossOfBlockLock_Type=TruthValue
_CwsPtpPcsLossOfBlockLock_Object=MibTableColumn
cwsPtpPcsLossOfBlockLock=_CwsPtpPcsLossOfBlockLock_Object((1,3,6,1,4,1,1271,3,4,8,22,1,3),_CwsPtpPcsLossOfBlockLock_Type())
cwsPtpPcsLossOfBlockLock.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPcsLossOfBlockLock.setStatus(_A)
_CwsPtpPcsHighBitErrorRate_Type=TruthValue
_CwsPtpPcsHighBitErrorRate_Object=MibTableColumn
cwsPtpPcsHighBitErrorRate=_CwsPtpPcsHighBitErrorRate_Object((1,3,6,1,4,1,1271,3,4,8,22,1,4),_CwsPtpPcsHighBitErrorRate_Type())
cwsPtpPcsHighBitErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpPcsHighBitErrorRate.setStatus(_A)
_CwsPtpRsTable_Object=MibTable
cwsPtpRsTable=_CwsPtpRsTable_Object((1,3,6,1,4,1,1271,3,4,8,23))
if mibBuilder.loadTexts:cwsPtpRsTable.setStatus(_A)
_CwsPtpRsEntry_Object=MibTableRow
cwsPtpRsEntry=_CwsPtpRsEntry_Object((1,3,6,1,4,1,1271,3,4,8,23,1))
cwsPtpRsEntry.setIndexNames((0,_B,_E),(0,_B,_I),(0,_B,_a))
if mibBuilder.loadTexts:cwsPtpRsEntry.setStatus(_A)
class _CwsPtpRsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpRsTableSnmpKey_Type.__name__=_D
_CwsPtpRsTableSnmpKey_Object=MibTableColumn
cwsPtpRsTableSnmpKey=_CwsPtpRsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,23,1,1),_CwsPtpRsTableSnmpKey_Type())
cwsPtpRsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpRsTableSnmpKey.setStatus(_A)
_CwsPtpRsLinkDown_Type=TruthValue
_CwsPtpRsLinkDown_Object=MibTableColumn
cwsPtpRsLinkDown=_CwsPtpRsLinkDown_Object((1,3,6,1,4,1,1271,3,4,8,23,1,2),_CwsPtpRsLinkDown_Type())
cwsPtpRsLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpRsLinkDown.setStatus(_A)
_CwsPtpRsLocalFault_Type=TruthValue
_CwsPtpRsLocalFault_Object=MibTableColumn
cwsPtpRsLocalFault=_CwsPtpRsLocalFault_Object((1,3,6,1,4,1,1271,3,4,8,23,1,3),_CwsPtpRsLocalFault_Type())
cwsPtpRsLocalFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpRsLocalFault.setStatus(_A)
_CwsPtpRsRemoteFault_Type=TruthValue
_CwsPtpRsRemoteFault_Object=MibTableColumn
cwsPtpRsRemoteFault=_CwsPtpRsRemoteFault_Object((1,3,6,1,4,1,1271,3,4,8,23,1,4),_CwsPtpRsRemoteFault_Type())
cwsPtpRsRemoteFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpRsRemoteFault.setStatus(_A)
_CwsPtpTraceTable_Object=MibTable
cwsPtpTraceTable=_CwsPtpTraceTable_Object((1,3,6,1,4,1,1271,3,4,8,24))
if mibBuilder.loadTexts:cwsPtpTraceTable.setStatus(_A)
_CwsPtpTraceEntry_Object=MibTableRow
cwsPtpTraceEntry=_CwsPtpTraceEntry_Object((1,3,6,1,4,1,1271,3,4,8,24,1))
cwsPtpTraceEntry.setIndexNames((0,_B,_E),(0,_B,_b))
if mibBuilder.loadTexts:cwsPtpTraceEntry.setStatus(_A)
class _CwsPtpTraceTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsPtpTraceTableSnmpKey_Type.__name__=_D
_CwsPtpTraceTableSnmpKey_Object=MibTableColumn
cwsPtpTraceTableSnmpKey=_CwsPtpTraceTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,8,24,1,1),_CwsPtpTraceTableSnmpKey_Type())
cwsPtpTraceTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsPtpTraceTableSnmpKey.setStatus(_A)
_CwsPtpTraceMismatchMode_Type=TraceMismatchMode
_CwsPtpTraceMismatchMode_Object=MibTableColumn
cwsPtpTraceMismatchMode=_CwsPtpTraceMismatchMode_Object((1,3,6,1,4,1,1271,3,4,8,24,1,2),_CwsPtpTraceMismatchMode_Type())
cwsPtpTraceMismatchMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceMismatchMode.setStatus(_A)
_CwsPtpTraceMismatchFailMode_Type=TraceMismatchFailMode
_CwsPtpTraceMismatchFailMode_Object=MibTableColumn
cwsPtpTraceMismatchFailMode=_CwsPtpTraceMismatchFailMode_Object((1,3,6,1,4,1,1271,3,4,8,24,1,3),_CwsPtpTraceMismatchFailMode_Type())
cwsPtpTraceMismatchFailMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceMismatchFailMode.setStatus(_A)
_CwsPtpTraceTxSapi_Type=StringMaxl15
_CwsPtpTraceTxSapi_Object=MibTableColumn
cwsPtpTraceTxSapi=_CwsPtpTraceTxSapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,4),_CwsPtpTraceTxSapi_Type())
cwsPtpTraceTxSapi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceTxSapi.setStatus(_A)
_CwsPtpTraceTxDapi_Type=StringMaxl15
_CwsPtpTraceTxDapi_Object=MibTableColumn
cwsPtpTraceTxDapi=_CwsPtpTraceTxDapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,5),_CwsPtpTraceTxDapi_Type())
cwsPtpTraceTxDapi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceTxDapi.setStatus(_A)
_CwsPtpTraceTxOper_Type=StringMaxl32
_CwsPtpTraceTxOper_Object=MibTableColumn
cwsPtpTraceTxOper=_CwsPtpTraceTxOper_Object((1,3,6,1,4,1,1271,3,4,8,24,1,6),_CwsPtpTraceTxOper_Type())
cwsPtpTraceTxOper.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceTxOper.setStatus(_A)
_CwsPtpTraceTxOperActual_Type=StringMaxl32
_CwsPtpTraceTxOperActual_Object=MibTableColumn
cwsPtpTraceTxOperActual=_CwsPtpTraceTxOperActual_Object((1,3,6,1,4,1,1271,3,4,8,24,1,7),_CwsPtpTraceTxOperActual_Type())
cwsPtpTraceTxOperActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpTraceTxOperActual.setStatus(_A)
_CwsPtpTraceTxOperMode_Type=TraceTxOperMode
_CwsPtpTraceTxOperMode_Object=MibTableColumn
cwsPtpTraceTxOperMode=_CwsPtpTraceTxOperMode_Object((1,3,6,1,4,1,1271,3,4,8,24,1,8),_CwsPtpTraceTxOperMode_Type())
cwsPtpTraceTxOperMode.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceTxOperMode.setStatus(_A)
_CwsPtpTraceRxSapi_Type=StringMaxl15
_CwsPtpTraceRxSapi_Object=MibTableColumn
cwsPtpTraceRxSapi=_CwsPtpTraceRxSapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,9),_CwsPtpTraceRxSapi_Type())
cwsPtpTraceRxSapi.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpTraceRxSapi.setStatus(_A)
_CwsPtpTraceRxDapi_Type=StringMaxl15
_CwsPtpTraceRxDapi_Object=MibTableColumn
cwsPtpTraceRxDapi=_CwsPtpTraceRxDapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,10),_CwsPtpTraceRxDapi_Type())
cwsPtpTraceRxDapi.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpTraceRxDapi.setStatus(_A)
_CwsPtpTraceRxOper_Type=StringMaxl32
_CwsPtpTraceRxOper_Object=MibTableColumn
cwsPtpTraceRxOper=_CwsPtpTraceRxOper_Object((1,3,6,1,4,1,1271,3,4,8,24,1,11),_CwsPtpTraceRxOper_Type())
cwsPtpTraceRxOper.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsPtpTraceRxOper.setStatus(_A)
_CwsPtpTraceExpSapi_Type=StringMaxl15
_CwsPtpTraceExpSapi_Object=MibTableColumn
cwsPtpTraceExpSapi=_CwsPtpTraceExpSapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,12),_CwsPtpTraceExpSapi_Type())
cwsPtpTraceExpSapi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceExpSapi.setStatus(_A)
_CwsPtpTraceExpDapi_Type=StringMaxl15
_CwsPtpTraceExpDapi_Object=MibTableColumn
cwsPtpTraceExpDapi=_CwsPtpTraceExpDapi_Object((1,3,6,1,4,1,1271,3,4,8,24,1,13),_CwsPtpTraceExpDapi_Type())
cwsPtpTraceExpDapi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceExpDapi.setStatus(_A)
_CwsPtpTraceExpOper_Type=StringMaxl32
_CwsPtpTraceExpOper_Object=MibTableColumn
cwsPtpTraceExpOper=_CwsPtpTraceExpOper_Object((1,3,6,1,4,1,1271,3,4,8,24,1,14),_CwsPtpTraceExpOper_Type())
cwsPtpTraceExpOper.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsPtpTraceExpOper.setStatus(_A)
cienaWsPtpGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,8,2,1,1))
cienaWsPtpGroup.setObjects(*((_B,_E),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_H),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_J),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_I),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:cienaWsPtpGroup.setStatus(_A)
cienaWsPtpCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,8,2,2,1))
cienaWsPtpCompliance.setObjects((_B,_Aa))
if mibBuilder.loadTexts:cienaWsPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PtpOpEnum':PtpOpEnum,'cienaWsPtpMIB':cienaWsPtpMIB,'cienaWsPtpObjects':cienaWsPtpObjects,'cienaWsPtpConformance':cienaWsPtpConformance,'cienaWsPtpGroups':cienaWsPtpGroups,_Aa:cienaWsPtpGroup,'cienaWsPtpCompliances':cienaWsPtpCompliances,'cienaWsPtpCompliance':cienaWsPtpCompliance,'cwsPtpPtpsTable':cwsPtpPtpsTable,'cwsPtpPtpsEntry':cwsPtpPtpsEntry,_E:cwsPtpPtpsPtpIndex,'cwsPtpPtpIdTable':cwsPtpPtpIdTable,'cwsPtpPtpIdEntry':cwsPtpPtpIdEntry,_K:cwsPtpPtpIdTableSnmpKey,_c:cwsPtpPtpIdName,'cwsPtpPtpStateTable':cwsPtpPtpStateTable,'cwsPtpPtpStateEntry':cwsPtpPtpStateEntry,_L:cwsPtpPtpStateTableSnmpKey,_d:cwsPtpPtpStateAdminState,_e:cwsPtpPtpStateOperationalState,_f:cwsPtpPtpStateSpliManagement,'cwsPtpPtpPropertiesTable':cwsPtpPtpPropertiesTable,'cwsPtpPtpPropertiesEntry':cwsPtpPtpPropertiesEntry,_M:cwsPtpPtpPropertiesTableSnmpKey,_g:cwsPtpPtpPropertiesXcvrType,_h:cwsPtpPtpPropertiesParentIndex,_i:cwsPtpPtpPropertiesRate,'cwsPtpTransmitterTable':cwsPtpTransmitterTable,'cwsPtpTransmitterEntry':cwsPtpTransmitterEntry,_N:cwsPtpTransmitterTableSnmpKey,_j:cwsPtpTransmitterState,'cwsPtpWavelengthTable':cwsPtpWavelengthTable,'cwsPtpWavelengthEntry':cwsPtpWavelengthEntry,_O:cwsPtpWavelengthTableSnmpKey,_k:cwsPtpWavelengthValue,_l:cwsPtpWavelengthMinValue,_m:cwsPtpWavelengthMaxValue,_n:cwsPtpWavelengthActual,'cwsPtpChannelsTable':cwsPtpChannelsTable,'cwsPtpChannelsEntry':cwsPtpChannelsEntry,_P:cwsPtpChannelsTableSnmpKey,_o:cwsPtpChannelsNumberOfChannels,'cwsPtpChannelTable':cwsPtpChannelTable,'cwsPtpChannelEntry':cwsPtpChannelEntry,_H:cwsPtpChannelChannelNumber,'cwsPtpRxPowerTable':cwsPtpRxPowerTable,'cwsPtpRxPowerEntry':cwsPtpRxPowerEntry,_Q:cwsPtpRxPowerTableSnmpKey,_p:cwsXcvrRxPowerActual,_q:cwsXcvrRxPowerMaximum,_r:cwsXcvrRxPowerMinimum,_s:cwsXcvrRxPowerMaximumRecordedTime,_t:cwsXcvrRxPowerMinimumRecordedTime,'cwsPtpRxStatusTable':cwsPtpRxStatusTable,'cwsPtpRxStatusEntry':cwsPtpRxStatusEntry,_R:cwsPtpRxStatusTableSnmpKey,_u:cwsXcvrRxStatusHighAlarmStatus,_v:cwsXcvrRxStatusLowAlarmStatus,_w:cwsXcvrRxStatusHighWarningStatus,_x:cwsXcvrRxStatusLowWarningStatus,_y:cwsPtpRxStatusLossOfSignal,_z:cwsPtpRxStatusLossOfLock,'cwsPtpTxPowerTable':cwsPtpTxPowerTable,'cwsPtpTxPowerEntry':cwsPtpTxPowerEntry,_S:cwsPtpTxPowerTableSnmpKey,_A0:cwsXcvrTxPowerActual,_A1:cwsXcvrTxPowerMaximum,_A2:cwsXcvrTxPowerMinimum,_A3:cwsXcvrTxPowerMaximumRecordedTime,_A4:cwsXcvrTxPowerMinimumRecordedTime,'cwsPtpTxStatusTable':cwsPtpTxStatusTable,'cwsPtpTxStatusEntry':cwsPtpTxStatusEntry,_T:cwsPtpTxStatusTableSnmpKey,_A5:cwsXcvrTxStatusHighAlarmStatus,_A6:cwsXcvrTxStatusLowAlarmStatus,_A7:cwsXcvrTxStatusHighWarningStatus,_A8:cwsXcvrTxStatusLowWarningStatus,'cwsPtpDiagnosticsTable':cwsPtpDiagnosticsTable,'cwsPtpDiagnosticsEntry':cwsPtpDiagnosticsEntry,_U:cwsPtpDiagnosticsTableSnmpKey,_A9:cwsPtpDiagnosticsNumberOfChannels,_AA:cwsPtpDiagnosticsNumberOfEthernet,'cwsPtpPtpOpticalDiagnosticsTable':cwsPtpPtpOpticalDiagnosticsTable,'cwsPtpPtpOpticalDiagnosticsEntry':cwsPtpPtpOpticalDiagnosticsEntry,_J:cwsPtpPtpOpticalDiagnosticsChannelNumber,'cwsPtpPtpRxOpticalDiagnosticsTable':cwsPtpPtpRxOpticalDiagnosticsTable,'cwsPtpPtpRxOpticalDiagnosticsEntry':cwsPtpPtpRxOpticalDiagnosticsEntry,_V:cwsPtpPtpRxOpticalDiagnosticsTableSnmpKey,_AB:cwsPtpPtpRxOpticalDiagnosticsLossOfSignal,_AC:cwsPtpPtpRxOpticalDiagnosticsLossOfLock,'cwsPtpPtpTxOpticalDiagnosticsTable':cwsPtpPtpTxOpticalDiagnosticsTable,'cwsPtpPtpTxOpticalDiagnosticsEntry':cwsPtpPtpTxOpticalDiagnosticsEntry,_W:cwsPtpPtpTxOpticalDiagnosticsTableSnmpKey,_AD:cwsPtpPtpTxOpticalDiagnosticsLossOfSignal,_AE:cwsPtpPtpTxOpticalDiagnosticsLossOfLock,'cwsPtpPtpEthernetDiagnosticsTable':cwsPtpPtpEthernetDiagnosticsTable,'cwsPtpPtpEthernetDiagnosticsEntry':cwsPtpPtpEthernetDiagnosticsEntry,_I:cwsPtpPtpEthernetDiagnosticsEthernetId,'cwsPtpPmaTable':cwsPtpPmaTable,'cwsPtpPmaEntry':cwsPtpPmaEntry,_X:cwsPtpPmaTableSnmpKey,_AF:cwsPtpPmaSerdesOutOfLock,'cwsPtpFecTable':cwsPtpFecTable,'cwsPtpFecEntry':cwsPtpFecEntry,_Y:cwsPtpFecTableSnmpKey,_AG:cwsPtpFecLossOfAlignmentMarkerLock,'cwsPtpPcsTable':cwsPtpPcsTable,'cwsPtpPcsEntry':cwsPtpPcsEntry,_Z:cwsPtpPcsTableSnmpKey,_AH:cwsPtpPcsLossOfAlignmentMarker,_AI:cwsPtpPcsLossOfBlockLock,_AJ:cwsPtpPcsHighBitErrorRate,'cwsPtpRsTable':cwsPtpRsTable,'cwsPtpRsEntry':cwsPtpRsEntry,_a:cwsPtpRsTableSnmpKey,_AK:cwsPtpRsLinkDown,_AL:cwsPtpRsLocalFault,_AM:cwsPtpRsRemoteFault,'cwsPtpTraceTable':cwsPtpTraceTable,'cwsPtpTraceEntry':cwsPtpTraceEntry,_b:cwsPtpTraceTableSnmpKey,_AN:cwsPtpTraceMismatchMode,_AO:cwsPtpTraceMismatchFailMode,_AP:cwsPtpTraceTxSapi,_AQ:cwsPtpTraceTxDapi,_AR:cwsPtpTraceTxOper,_AS:cwsPtpTraceTxOperActual,_AT:cwsPtpTraceTxOperMode,_AU:cwsPtpTraceRxSapi,_AV:cwsPtpTraceRxDapi,_AW:cwsPtpTraceRxOper,_AX:cwsPtpTraceExpSapi,_AY:cwsPtpTraceExpDapi,_AZ:cwsPtpTraceExpOper})