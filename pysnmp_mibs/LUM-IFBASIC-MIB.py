_Al='ifBasicAdminGroupV4'
_Ak='ifBasicAdminGroupV3'
_Aj='ifBasicSignalGroupV6'
_Ai='ifBasicAdminGroupV2'
_Ah='ifBasicSignalGroupV5'
_Ag='ifBasicSignalGroupV4'
_Af='ifBasicSignalGroupV3'
_Ae='ifBasicSignalGroupV2'
_Ad='ifBasicSignalGroupV1'
_Ac='ifBasicAdminNotAvailableForUse'
_Ab='ifBasicSignalConnectorType'
_Aa='ifBasicIfPhysicalLocation'
_AZ='ifBasicIfAid'
_AY='ifBasicGeneralIfBasicSignalStateLastChangeTime'
_AX='ifBasicGeneralIfBasicSignalConfigLastChangeTime'
_AW='ifBasicGeneralIfBasicSignalTableSize'
_AV='ifBasicGeneralIfBasicAdminStateLastChangeTime'
_AU='ifBasicGeneralIfBasicAdminConfigLastChangeTime'
_AT='ifBasicGeneralIfBasicAdminTableSize'
_AS='ifBasicGeneralIfBasicIfStateLastChangeTime'
_AR='ifBasicGeneralIfBasicIfConfigLastChangeTime'
_AQ='ifBasicGeneralIfBasicIfTableSize'
_AP='ifBasicGeneralStateLastChangeTime'
_AO='ifBasicGeneralConfigLastChangeTime'
_AN='Unsigned32'
_AM='Integer32'
_AL='Counter64'
_AK='TruthValueWithNA'
_AJ='SignalFormat'
_AI='SignalDirection'
_AH='ResetWithNA'
_AG='PhysicalLayerMappingType'
_AF='OperStatusWithNA'
_AE='InterfaceType'
_AD='DisplayStringWithNA'
_AC='ConnectorType'
_AB='AutoAlarmStatus'
_AA='AdminStatusWithNA'
_A9='ifBasicSignalGroupV7'
_A8='ifBasicIfGroupV2'
_A7='ifBasicAdminIfType'
_A6='ifBasicAdminIfNo'
_A5='ifBasicSignalTerminalLoopbackEnabled'
_A4='ifBasicSignalTerminalLoopbackTimeout'
_A3='ifBasicSignalTerminalLoopback'
_A2='ifBasicSignalFacilityLoopbackEnabled'
_A1='ifBasicSignalFacilityLoopbackTimeout'
_A0='ifBasicSignalFacilityLoopback'
_z='ifBasicIfUpId'
_y='Unsigned32WithNA'
_x='Time7200minNo0'
_w='Time7200min'
_v='OpticalLayerMappingType'
_u='ifBasicIfGroupV3'
_t='ifBasicIfGroupV1'
_s='ifBasicAdminInterfaceStatus'
_r='ifBasicSignalPhysicalLayerMapping'
_q='ifBasicIfRxSignalStatus'
_p='ifBasicIfTxSignalStatus'
_o='ifBasicIfName'
_n='ifBasicSignalFormatConfigurationSharedWithInterface'
_m='ifBasicSignalFormatConfigurable'
_l='ifBasicSignalDirection'
_k='ifBasicSignalSpeed'
_j='ifBasicAdminAutoAlarmEnableReset'
_i='ifBasicAdminAutoAlarmEnableStatus'
_h='ifBasicAdminOperStatus'
_g='ifBasicAdminAdminStatus'
_f='ifBasicAdminRxPort'
_e='ifBasicAdminTxPort'
_d='ifBasicAdminSlot'
_c='ifBasicAdminSubrack'
_b='ifBasicAdminDescr'
_a='ifBasicAdminName'
_Z='ifBasicIfIndex'
_Y='EnabledDisabledWithNA'
_X='ifBasicAdminGroupV1'
_W='ifBasicSignalActualOpticalLayerMapping'
_V='ifBasicSignalConfigurationMismatch'
_U='ifBasicAdminIndex'
_T='ifBasicSignalOpticalLayerMapping'
_S='ifBasicSignalNearEndLoopbackEnabled'
_R='ifBasicSignalFarEndLoopbackEnabled'
_Q='ifBasicSignalNearEndLoopbackTimeout'
_P='ifBasicSignalNearEndLoopback'
_O='ifBasicSignalNearEndLoopbackTerminatingLayer'
_N='ifBasicSignalFarEndLoopbackTimeout'
_M='ifBasicSignalFarEndLoopback'
_L='ifBasicSignalFarEndLoopbackTerminatingLayer'
_K='ifBasicSignalSignalFormat'
_J='ifBasicSignalSignalStructure'
_I='ifBasicSignalName'
_H='read-create'
_G='ifBasicGeneralGroupV1'
_F='ifBasicSignalIndex'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-IFBASIC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfBasicMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfBasicMIB','lumModules')
AdminStatusWithNA,AutoAlarmStatus,CommandString,ConnectorType,DisplayStringWithNA,EnabledDisabledWithNA,FaultStatusWithNA,InterfaceStatus,InterfaceType,Layer,MgmtNameString,OperStatusWithNA,OpticalLayerMappingType,PhysicalLayerMappingType,ResetWithNA,SignalDirection,SignalFormat,SignalStatusWithNA,Time7200min,Time7200minNo0,TribPortIdType,TruthValueWithNA,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC',_AA,_AB,'CommandString',_AC,_AD,_Y,'FaultStatusWithNA','InterfaceStatus',_AE,'Layer','MgmtNameString',_AF,_v,_AG,_AH,_AI,_AJ,'SignalStatusWithNA',_w,_x,'TribPortIdType',_AK,_y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_AL,'Gauge32',_AM,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_AN,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfBasicMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,46))
if mibBuilder.loadTexts:lumIfBasicMIBModule.setRevisions(('2018-12-31 00:00','2018-06-29 00:00','2017-06-15 00:00','2016-11-30 00:00','2016-11-04 00:00','2016-01-31 00:00','2015-12-22 00:00','2015-10-30 00:00','2014-09-30 00:00','2014-05-16 00:00','2013-11-15 00:00','2012-11-20 00:00'))
_LumIfBasicConfs_ObjectIdentity=ObjectIdentity
lumIfBasicConfs=_LumIfBasicConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,46,1))
_LumIfBasicGroups_ObjectIdentity=ObjectIdentity
lumIfBasicGroups=_LumIfBasicGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,46,1,1))
_LumIfBasicCompl_ObjectIdentity=ObjectIdentity
lumIfBasicCompl=_LumIfBasicCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,46,1,2))
_LumIfBasicMIBObjects_ObjectIdentity=ObjectIdentity
lumIfBasicMIBObjects=_LumIfBasicMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,46,2))
_IfBasicGeneral_ObjectIdentity=ObjectIdentity
ifBasicGeneral=_IfBasicGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,46,2,1))
_IfBasicGeneralConfigLastChangeTime_Type=DateAndTime
_IfBasicGeneralConfigLastChangeTime_Object=MibScalar
ifBasicGeneralConfigLastChangeTime=_IfBasicGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,1),_IfBasicGeneralConfigLastChangeTime_Type())
ifBasicGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralConfigLastChangeTime.setStatus(_B)
_IfBasicGeneralStateLastChangeTime_Type=DateAndTime
_IfBasicGeneralStateLastChangeTime_Object=MibScalar
ifBasicGeneralStateLastChangeTime=_IfBasicGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,2),_IfBasicGeneralStateLastChangeTime_Type())
ifBasicGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralStateLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicIfTableSize_Type=Unsigned32
_IfBasicGeneralIfBasicIfTableSize_Object=MibScalar
ifBasicGeneralIfBasicIfTableSize=_IfBasicGeneralIfBasicIfTableSize_Object((1,3,6,1,4,1,8708,2,46,2,1,3),_IfBasicGeneralIfBasicIfTableSize_Type())
ifBasicGeneralIfBasicIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicIfTableSize.setStatus(_B)
_IfBasicGeneralIfBasicIfConfigLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicIfConfigLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicIfConfigLastChangeTime=_IfBasicGeneralIfBasicIfConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,4),_IfBasicGeneralIfBasicIfConfigLastChangeTime_Type())
ifBasicGeneralIfBasicIfConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicIfConfigLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicIfStateLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicIfStateLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicIfStateLastChangeTime=_IfBasicGeneralIfBasicIfStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,5),_IfBasicGeneralIfBasicIfStateLastChangeTime_Type())
ifBasicGeneralIfBasicIfStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicIfStateLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicAdminTableSize_Type=Unsigned32
_IfBasicGeneralIfBasicAdminTableSize_Object=MibScalar
ifBasicGeneralIfBasicAdminTableSize=_IfBasicGeneralIfBasicAdminTableSize_Object((1,3,6,1,4,1,8708,2,46,2,1,6),_IfBasicGeneralIfBasicAdminTableSize_Type())
ifBasicGeneralIfBasicAdminTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicAdminTableSize.setStatus(_B)
_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicAdminConfigLastChangeTime=_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,7),_IfBasicGeneralIfBasicAdminConfigLastChangeTime_Type())
ifBasicGeneralIfBasicAdminConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicAdminConfigLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicAdminStateLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicAdminStateLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicAdminStateLastChangeTime=_IfBasicGeneralIfBasicAdminStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,8),_IfBasicGeneralIfBasicAdminStateLastChangeTime_Type())
ifBasicGeneralIfBasicAdminStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicAdminStateLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicSignalTableSize_Type=Unsigned32
_IfBasicGeneralIfBasicSignalTableSize_Object=MibScalar
ifBasicGeneralIfBasicSignalTableSize=_IfBasicGeneralIfBasicSignalTableSize_Object((1,3,6,1,4,1,8708,2,46,2,1,9),_IfBasicGeneralIfBasicSignalTableSize_Type())
ifBasicGeneralIfBasicSignalTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicSignalTableSize.setStatus(_B)
_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicSignalConfigLastChangeTime=_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,10),_IfBasicGeneralIfBasicSignalConfigLastChangeTime_Type())
ifBasicGeneralIfBasicSignalConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicSignalConfigLastChangeTime.setStatus(_B)
_IfBasicGeneralIfBasicSignalStateLastChangeTime_Type=DateAndTime
_IfBasicGeneralIfBasicSignalStateLastChangeTime_Object=MibScalar
ifBasicGeneralIfBasicSignalStateLastChangeTime=_IfBasicGeneralIfBasicSignalStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,46,2,1,11),_IfBasicGeneralIfBasicSignalStateLastChangeTime_Type())
ifBasicGeneralIfBasicSignalStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicGeneralIfBasicSignalStateLastChangeTime.setStatus(_B)
_IfBasicIfList_ObjectIdentity=ObjectIdentity
ifBasicIfList=_IfBasicIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,46,2,2))
_IfBasicIfTable_Object=MibTable
ifBasicIfTable=_IfBasicIfTable_Object((1,3,6,1,4,1,8708,2,46,2,2,1))
if mibBuilder.loadTexts:ifBasicIfTable.setStatus(_B)
_IfBasicIfEntry_Object=MibTableRow
ifBasicIfEntry=_IfBasicIfEntry_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1))
ifBasicIfEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:ifBasicIfEntry.setStatus(_B)
_IfBasicIfIndex_Type=Unsigned32
_IfBasicIfIndex_Object=MibTableColumn
ifBasicIfIndex=_IfBasicIfIndex_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,1),_IfBasicIfIndex_Type())
ifBasicIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfIndex.setStatus(_B)
_IfBasicIfName_Type=MgmtNameString
_IfBasicIfName_Object=MibTableColumn
ifBasicIfName=_IfBasicIfName_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,2),_IfBasicIfName_Type())
ifBasicIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfName.setStatus(_B)
_IfBasicIfTxSignalStatus_Type=SignalStatusWithNA
_IfBasicIfTxSignalStatus_Object=MibTableColumn
ifBasicIfTxSignalStatus=_IfBasicIfTxSignalStatus_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,3),_IfBasicIfTxSignalStatus_Type())
ifBasicIfTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfTxSignalStatus.setStatus(_B)
_IfBasicIfRxSignalStatus_Type=SignalStatusWithNA
_IfBasicIfRxSignalStatus_Object=MibTableColumn
ifBasicIfRxSignalStatus=_IfBasicIfRxSignalStatus_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,4),_IfBasicIfRxSignalStatus_Type())
ifBasicIfRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfRxSignalStatus.setStatus(_B)
class _IfBasicIfUpId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfBasicIfUpId_Type.__name__=_AN
_IfBasicIfUpId_Object=MibTableColumn
ifBasicIfUpId=_IfBasicIfUpId_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,5),_IfBasicIfUpId_Type())
ifBasicIfUpId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfUpId.setStatus(_B)
_IfBasicIfAid_Type=DisplayString
_IfBasicIfAid_Object=MibTableColumn
ifBasicIfAid=_IfBasicIfAid_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,6),_IfBasicIfAid_Type())
ifBasicIfAid.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfAid.setStatus(_B)
_IfBasicIfPhysicalLocation_Type=DisplayString
_IfBasicIfPhysicalLocation_Object=MibTableColumn
ifBasicIfPhysicalLocation=_IfBasicIfPhysicalLocation_Object((1,3,6,1,4,1,8708,2,46,2,2,1,1,7),_IfBasicIfPhysicalLocation_Type())
ifBasicIfPhysicalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicIfPhysicalLocation.setStatus(_B)
_IfBasicAdminList_ObjectIdentity=ObjectIdentity
ifBasicAdminList=_IfBasicAdminList_ObjectIdentity((1,3,6,1,4,1,8708,2,46,2,3))
_IfBasicAdminTable_Object=MibTable
ifBasicAdminTable=_IfBasicAdminTable_Object((1,3,6,1,4,1,8708,2,46,2,3,1))
if mibBuilder.loadTexts:ifBasicAdminTable.setStatus(_B)
_IfBasicAdminEntry_Object=MibTableRow
ifBasicAdminEntry=_IfBasicAdminEntry_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1))
ifBasicAdminEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:ifBasicAdminEntry.setStatus(_B)
_IfBasicAdminIndex_Type=Unsigned32
_IfBasicAdminIndex_Object=MibTableColumn
ifBasicAdminIndex=_IfBasicAdminIndex_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,1),_IfBasicAdminIndex_Type())
ifBasicAdminIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminIndex.setStatus(_B)
_IfBasicAdminName_Type=MgmtNameString
_IfBasicAdminName_Object=MibTableColumn
ifBasicAdminName=_IfBasicAdminName_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,2),_IfBasicAdminName_Type())
ifBasicAdminName.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminName.setStatus(_B)
class _IfBasicAdminDescr_Type(DisplayStringWithNA):defaultValue=OctetString('')
_IfBasicAdminDescr_Type.__name__=_AD
_IfBasicAdminDescr_Object=MibTableColumn
ifBasicAdminDescr=_IfBasicAdminDescr_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,3),_IfBasicAdminDescr_Type())
ifBasicAdminDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicAdminDescr.setStatus(_B)
_IfBasicAdminSubrack_Type=Unsigned32WithNA
_IfBasicAdminSubrack_Object=MibTableColumn
ifBasicAdminSubrack=_IfBasicAdminSubrack_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,4),_IfBasicAdminSubrack_Type())
ifBasicAdminSubrack.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminSubrack.setStatus(_B)
_IfBasicAdminSlot_Type=Unsigned32WithNA
_IfBasicAdminSlot_Object=MibTableColumn
ifBasicAdminSlot=_IfBasicAdminSlot_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,5),_IfBasicAdminSlot_Type())
ifBasicAdminSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminSlot.setStatus(_B)
_IfBasicAdminTxPort_Type=Unsigned32WithNA
_IfBasicAdminTxPort_Object=MibTableColumn
ifBasicAdminTxPort=_IfBasicAdminTxPort_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,6),_IfBasicAdminTxPort_Type())
ifBasicAdminTxPort.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminTxPort.setStatus(_B)
_IfBasicAdminRxPort_Type=Unsigned32WithNA
_IfBasicAdminRxPort_Object=MibTableColumn
ifBasicAdminRxPort=_IfBasicAdminRxPort_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,7),_IfBasicAdminRxPort_Type())
ifBasicAdminRxPort.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminRxPort.setStatus(_B)
class _IfBasicAdminAdminStatus_Type(AdminStatusWithNA):defaultValue=3
_IfBasicAdminAdminStatus_Type.__name__=_AA
_IfBasicAdminAdminStatus_Object=MibTableColumn
ifBasicAdminAdminStatus=_IfBasicAdminAdminStatus_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,8),_IfBasicAdminAdminStatus_Type())
ifBasicAdminAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicAdminAdminStatus.setStatus(_B)
class _IfBasicAdminOperStatus_Type(OperStatusWithNA):defaultValue=1
_IfBasicAdminOperStatus_Type.__name__=_AF
_IfBasicAdminOperStatus_Object=MibTableColumn
ifBasicAdminOperStatus=_IfBasicAdminOperStatus_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,9),_IfBasicAdminOperStatus_Type())
ifBasicAdminOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminOperStatus.setStatus(_B)
class _IfBasicAdminAutoAlarmEnableStatus_Type(AutoAlarmStatus):defaultValue=1
_IfBasicAdminAutoAlarmEnableStatus_Type.__name__=_AB
_IfBasicAdminAutoAlarmEnableStatus_Object=MibTableColumn
ifBasicAdminAutoAlarmEnableStatus=_IfBasicAdminAutoAlarmEnableStatus_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,10),_IfBasicAdminAutoAlarmEnableStatus_Type())
ifBasicAdminAutoAlarmEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminAutoAlarmEnableStatus.setStatus(_B)
class _IfBasicAdminAutoAlarmEnableReset_Type(ResetWithNA):defaultValue=2
_IfBasicAdminAutoAlarmEnableReset_Type.__name__=_AH
_IfBasicAdminAutoAlarmEnableReset_Object=MibTableColumn
ifBasicAdminAutoAlarmEnableReset=_IfBasicAdminAutoAlarmEnableReset_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,11),_IfBasicAdminAutoAlarmEnableReset_Type())
ifBasicAdminAutoAlarmEnableReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminAutoAlarmEnableReset.setStatus(_B)
_IfBasicAdminInterfaceStatus_Type=InterfaceStatus
_IfBasicAdminInterfaceStatus_Object=MibTableColumn
ifBasicAdminInterfaceStatus=_IfBasicAdminInterfaceStatus_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,12),_IfBasicAdminInterfaceStatus_Type())
ifBasicAdminInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminInterfaceStatus.setStatus(_B)
class _IfBasicAdminIfNo_Type(Unsigned32WithNA):defaultValue=2147483647
_IfBasicAdminIfNo_Type.__name__=_y
_IfBasicAdminIfNo_Object=MibTableColumn
ifBasicAdminIfNo=_IfBasicAdminIfNo_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,13),_IfBasicAdminIfNo_Type())
ifBasicAdminIfNo.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminIfNo.setStatus(_B)
class _IfBasicAdminIfType_Type(InterfaceType):defaultValue=2147483647
_IfBasicAdminIfType_Type.__name__=_AE
_IfBasicAdminIfType_Object=MibTableColumn
ifBasicAdminIfType=_IfBasicAdminIfType_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,14),_IfBasicAdminIfType_Type())
ifBasicAdminIfType.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicAdminIfType.setStatus(_B)
class _IfBasicAdminNotAvailableForUse_Type(TruthValueWithNA):defaultValue=2147483647
_IfBasicAdminNotAvailableForUse_Type.__name__=_AK
_IfBasicAdminNotAvailableForUse_Object=MibTableColumn
ifBasicAdminNotAvailableForUse=_IfBasicAdminNotAvailableForUse_Object((1,3,6,1,4,1,8708,2,46,2,3,1,1,15),_IfBasicAdminNotAvailableForUse_Type())
ifBasicAdminNotAvailableForUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicAdminNotAvailableForUse.setStatus(_B)
_IfBasicSignalList_ObjectIdentity=ObjectIdentity
ifBasicSignalList=_IfBasicSignalList_ObjectIdentity((1,3,6,1,4,1,8708,2,46,2,4))
_IfBasicSignalTable_Object=MibTable
ifBasicSignalTable=_IfBasicSignalTable_Object((1,3,6,1,4,1,8708,2,46,2,4,1))
if mibBuilder.loadTexts:ifBasicSignalTable.setStatus(_B)
_IfBasicSignalEntry_Object=MibTableRow
ifBasicSignalEntry=_IfBasicSignalEntry_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1))
ifBasicSignalEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:ifBasicSignalEntry.setStatus(_B)
_IfBasicSignalIndex_Type=Unsigned32
_IfBasicSignalIndex_Object=MibTableColumn
ifBasicSignalIndex=_IfBasicSignalIndex_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,1),_IfBasicSignalIndex_Type())
ifBasicSignalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalIndex.setStatus(_B)
_IfBasicSignalName_Type=MgmtNameString
_IfBasicSignalName_Object=MibTableColumn
ifBasicSignalName=_IfBasicSignalName_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,2),_IfBasicSignalName_Type())
ifBasicSignalName.setMaxAccess(_H)
if mibBuilder.loadTexts:ifBasicSignalName.setStatus(_B)
class _IfBasicSignalSignalStructure_Type(Counter64):defaultValue=0
_IfBasicSignalSignalStructure_Type.__name__=_AL
_IfBasicSignalSignalStructure_Object=MibTableColumn
ifBasicSignalSignalStructure=_IfBasicSignalSignalStructure_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,3),_IfBasicSignalSignalStructure_Type())
ifBasicSignalSignalStructure.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalSignalStructure.setStatus(_B)
class _IfBasicSignalSignalFormat_Type(SignalFormat):defaultValue=10
_IfBasicSignalSignalFormat_Type.__name__=_AJ
_IfBasicSignalSignalFormat_Object=MibTableColumn
ifBasicSignalSignalFormat=_IfBasicSignalSignalFormat_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,4),_IfBasicSignalSignalFormat_Type())
ifBasicSignalSignalFormat.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalSignalFormat.setStatus(_B)
_IfBasicSignalFarEndLoopbackTerminatingLayer_Type=Layer
_IfBasicSignalFarEndLoopbackTerminatingLayer_Object=MibTableColumn
ifBasicSignalFarEndLoopbackTerminatingLayer=_IfBasicSignalFarEndLoopbackTerminatingLayer_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,5),_IfBasicSignalFarEndLoopbackTerminatingLayer_Type())
ifBasicSignalFarEndLoopbackTerminatingLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalFarEndLoopbackTerminatingLayer.setStatus(_B)
class _IfBasicSignalFarEndLoopback_Type(EnabledDisabledWithNA):defaultValue=1
_IfBasicSignalFarEndLoopback_Type.__name__=_Y
_IfBasicSignalFarEndLoopback_Object=MibTableColumn
ifBasicSignalFarEndLoopback=_IfBasicSignalFarEndLoopback_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,6),_IfBasicSignalFarEndLoopback_Type())
ifBasicSignalFarEndLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalFarEndLoopback.setStatus(_B)
class _IfBasicSignalFarEndLoopbackTimeout_Type(Time7200min):defaultValue=3
_IfBasicSignalFarEndLoopbackTimeout_Type.__name__=_w
_IfBasicSignalFarEndLoopbackTimeout_Object=MibTableColumn
ifBasicSignalFarEndLoopbackTimeout=_IfBasicSignalFarEndLoopbackTimeout_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,7),_IfBasicSignalFarEndLoopbackTimeout_Type())
ifBasicSignalFarEndLoopbackTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalFarEndLoopbackTimeout.setStatus(_B)
_IfBasicSignalNearEndLoopbackTerminatingLayer_Type=Layer
_IfBasicSignalNearEndLoopbackTerminatingLayer_Object=MibTableColumn
ifBasicSignalNearEndLoopbackTerminatingLayer=_IfBasicSignalNearEndLoopbackTerminatingLayer_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,8),_IfBasicSignalNearEndLoopbackTerminatingLayer_Type())
ifBasicSignalNearEndLoopbackTerminatingLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalNearEndLoopbackTerminatingLayer.setStatus(_B)
class _IfBasicSignalNearEndLoopback_Type(EnabledDisabledWithNA):defaultValue=1
_IfBasicSignalNearEndLoopback_Type.__name__=_Y
_IfBasicSignalNearEndLoopback_Object=MibTableColumn
ifBasicSignalNearEndLoopback=_IfBasicSignalNearEndLoopback_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,9),_IfBasicSignalNearEndLoopback_Type())
ifBasicSignalNearEndLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalNearEndLoopback.setStatus(_B)
class _IfBasicSignalNearEndLoopbackTimeout_Type(Time7200min):defaultValue=3
_IfBasicSignalNearEndLoopbackTimeout_Type.__name__=_w
_IfBasicSignalNearEndLoopbackTimeout_Object=MibTableColumn
ifBasicSignalNearEndLoopbackTimeout=_IfBasicSignalNearEndLoopbackTimeout_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,10),_IfBasicSignalNearEndLoopbackTimeout_Type())
ifBasicSignalNearEndLoopbackTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalNearEndLoopbackTimeout.setStatus(_B)
_IfBasicSignalFarEndLoopbackEnabled_Type=FaultStatusWithNA
_IfBasicSignalFarEndLoopbackEnabled_Object=MibTableColumn
ifBasicSignalFarEndLoopbackEnabled=_IfBasicSignalFarEndLoopbackEnabled_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,11),_IfBasicSignalFarEndLoopbackEnabled_Type())
ifBasicSignalFarEndLoopbackEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalFarEndLoopbackEnabled.setStatus(_B)
_IfBasicSignalNearEndLoopbackEnabled_Type=FaultStatusWithNA
_IfBasicSignalNearEndLoopbackEnabled_Object=MibTableColumn
ifBasicSignalNearEndLoopbackEnabled=_IfBasicSignalNearEndLoopbackEnabled_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,12),_IfBasicSignalNearEndLoopbackEnabled_Type())
ifBasicSignalNearEndLoopbackEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalNearEndLoopbackEnabled.setStatus(_B)
class _IfBasicSignalOpticalLayerMapping_Type(OpticalLayerMappingType):defaultValue=3
_IfBasicSignalOpticalLayerMapping_Type.__name__=_v
_IfBasicSignalOpticalLayerMapping_Object=MibTableColumn
ifBasicSignalOpticalLayerMapping=_IfBasicSignalOpticalLayerMapping_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,13),_IfBasicSignalOpticalLayerMapping_Type())
ifBasicSignalOpticalLayerMapping.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalOpticalLayerMapping.setStatus(_B)
_IfBasicSignalConfigurationMismatch_Type=FaultStatusWithNA
_IfBasicSignalConfigurationMismatch_Object=MibTableColumn
ifBasicSignalConfigurationMismatch=_IfBasicSignalConfigurationMismatch_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,14),_IfBasicSignalConfigurationMismatch_Type())
ifBasicSignalConfigurationMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalConfigurationMismatch.setStatus(_D)
class _IfBasicSignalActualOpticalLayerMapping_Type(OpticalLayerMappingType):defaultValue=0
_IfBasicSignalActualOpticalLayerMapping_Type.__name__=_v
_IfBasicSignalActualOpticalLayerMapping_Object=MibTableColumn
ifBasicSignalActualOpticalLayerMapping=_IfBasicSignalActualOpticalLayerMapping_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,15),_IfBasicSignalActualOpticalLayerMapping_Type())
ifBasicSignalActualOpticalLayerMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalActualOpticalLayerMapping.setStatus(_B)
class _IfBasicSignalSpeed_Type(Unsigned32WithNA):defaultValue=61440;subtypeSpec=Unsigned32WithNA.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(61440,1402500),ValueRangeConstraint(2147483647,2147483647))
_IfBasicSignalSpeed_Type.__name__=_y
_IfBasicSignalSpeed_Object=MibTableColumn
ifBasicSignalSpeed=_IfBasicSignalSpeed_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,16),_IfBasicSignalSpeed_Type())
ifBasicSignalSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalSpeed.setStatus(_B)
class _IfBasicSignalDirection_Type(SignalDirection):defaultValue=4
_IfBasicSignalDirection_Type.__name__=_AI
_IfBasicSignalDirection_Object=MibTableColumn
ifBasicSignalDirection=_IfBasicSignalDirection_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,17),_IfBasicSignalDirection_Type())
ifBasicSignalDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalDirection.setStatus(_B)
class _IfBasicSignalFormatConfigurable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,2147483647)));namedValues=NamedValues(*(('true',1),('false',2),('notApplicable',2147483647)))
_IfBasicSignalFormatConfigurable_Type.__name__=_AM
_IfBasicSignalFormatConfigurable_Object=MibTableColumn
ifBasicSignalFormatConfigurable=_IfBasicSignalFormatConfigurable_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,18),_IfBasicSignalFormatConfigurable_Type())
ifBasicSignalFormatConfigurable.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalFormatConfigurable.setStatus(_B)
_IfBasicSignalFormatConfigurationSharedWithInterface_Type=Unsigned32WithNA
_IfBasicSignalFormatConfigurationSharedWithInterface_Object=MibTableColumn
ifBasicSignalFormatConfigurationSharedWithInterface=_IfBasicSignalFormatConfigurationSharedWithInterface_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,19),_IfBasicSignalFormatConfigurationSharedWithInterface_Type())
ifBasicSignalFormatConfigurationSharedWithInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalFormatConfigurationSharedWithInterface.setStatus(_B)
class _IfBasicSignalPhysicalLayerMapping_Type(PhysicalLayerMappingType):defaultValue=1
_IfBasicSignalPhysicalLayerMapping_Type.__name__=_AG
_IfBasicSignalPhysicalLayerMapping_Object=MibTableColumn
ifBasicSignalPhysicalLayerMapping=_IfBasicSignalPhysicalLayerMapping_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,20),_IfBasicSignalPhysicalLayerMapping_Type())
ifBasicSignalPhysicalLayerMapping.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalPhysicalLayerMapping.setStatus(_B)
class _IfBasicSignalFacilityLoopback_Type(EnabledDisabledWithNA):defaultValue=1
_IfBasicSignalFacilityLoopback_Type.__name__=_Y
_IfBasicSignalFacilityLoopback_Object=MibTableColumn
ifBasicSignalFacilityLoopback=_IfBasicSignalFacilityLoopback_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,21),_IfBasicSignalFacilityLoopback_Type())
ifBasicSignalFacilityLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalFacilityLoopback.setStatus(_B)
class _IfBasicSignalFacilityLoopbackTimeout_Type(Time7200minNo0):defaultValue=3
_IfBasicSignalFacilityLoopbackTimeout_Type.__name__=_x
_IfBasicSignalFacilityLoopbackTimeout_Object=MibTableColumn
ifBasicSignalFacilityLoopbackTimeout=_IfBasicSignalFacilityLoopbackTimeout_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,22),_IfBasicSignalFacilityLoopbackTimeout_Type())
ifBasicSignalFacilityLoopbackTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalFacilityLoopbackTimeout.setStatus(_B)
_IfBasicSignalFacilityLoopbackEnabled_Type=FaultStatusWithNA
_IfBasicSignalFacilityLoopbackEnabled_Object=MibTableColumn
ifBasicSignalFacilityLoopbackEnabled=_IfBasicSignalFacilityLoopbackEnabled_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,23),_IfBasicSignalFacilityLoopbackEnabled_Type())
ifBasicSignalFacilityLoopbackEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalFacilityLoopbackEnabled.setStatus(_B)
class _IfBasicSignalTerminalLoopback_Type(EnabledDisabledWithNA):defaultValue=1
_IfBasicSignalTerminalLoopback_Type.__name__=_Y
_IfBasicSignalTerminalLoopback_Object=MibTableColumn
ifBasicSignalTerminalLoopback=_IfBasicSignalTerminalLoopback_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,24),_IfBasicSignalTerminalLoopback_Type())
ifBasicSignalTerminalLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalTerminalLoopback.setStatus(_B)
class _IfBasicSignalTerminalLoopbackTimeout_Type(Time7200minNo0):defaultValue=3
_IfBasicSignalTerminalLoopbackTimeout_Type.__name__=_x
_IfBasicSignalTerminalLoopbackTimeout_Object=MibTableColumn
ifBasicSignalTerminalLoopbackTimeout=_IfBasicSignalTerminalLoopbackTimeout_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,25),_IfBasicSignalTerminalLoopbackTimeout_Type())
ifBasicSignalTerminalLoopbackTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:ifBasicSignalTerminalLoopbackTimeout.setStatus(_B)
_IfBasicSignalTerminalLoopbackEnabled_Type=FaultStatusWithNA
_IfBasicSignalTerminalLoopbackEnabled_Object=MibTableColumn
ifBasicSignalTerminalLoopbackEnabled=_IfBasicSignalTerminalLoopbackEnabled_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,26),_IfBasicSignalTerminalLoopbackEnabled_Type())
ifBasicSignalTerminalLoopbackEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalTerminalLoopbackEnabled.setStatus(_B)
class _IfBasicSignalConnectorType_Type(ConnectorType):defaultValue=2147483647
_IfBasicSignalConnectorType_Type.__name__=_AC
_IfBasicSignalConnectorType_Object=MibTableColumn
ifBasicSignalConnectorType=_IfBasicSignalConnectorType_Object((1,3,6,1,4,1,8708,2,46,2,4,1,1,27),_IfBasicSignalConnectorType_Type())
ifBasicSignalConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBasicSignalConnectorType.setStatus(_B)
ifBasicGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,1))
ifBasicGeneralGroupV1.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY)))
if mibBuilder.loadTexts:ifBasicGeneralGroupV1.setStatus(_B)
ifBasicIfGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,2))
ifBasicIfGroupV1.setObjects(*((_A,_Z),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ifBasicIfGroupV1.setStatus(_D)
ifBasicAdminGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,3))
ifBasicAdminGroupV1.setObjects(*((_A,_U),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ifBasicAdminGroupV1.setStatus(_D)
ifBasicSignalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,4))
ifBasicSignalGroupV1.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ifBasicSignalGroupV1.setStatus(_D)
ifBasicSignalGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,5))
ifBasicSignalGroupV2.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ifBasicSignalGroupV2.setStatus(_D)
ifBasicSignalGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,6))
ifBasicSignalGroupV3.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ifBasicSignalGroupV3.setStatus(_D)
ifBasicSignalGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,7))
ifBasicSignalGroupV4.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ifBasicSignalGroupV4.setStatus(_D)
ifBasicIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,8))
ifBasicIfGroupV2.setObjects(*((_A,_Z),(_A,_o),(_A,_p),(_A,_q),(_A,_z)))
if mibBuilder.loadTexts:ifBasicIfGroupV2.setStatus(_D)
ifBasicSignalGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,9))
ifBasicSignalGroupV5.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_r)))
if mibBuilder.loadTexts:ifBasicSignalGroupV5.setStatus(_D)
ifBasicSignalGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,10))
ifBasicSignalGroupV6.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_r),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ifBasicSignalGroupV6.setStatus(_D)
ifBasicAdminGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,11))
ifBasicAdminGroupV2.setObjects(*((_A,_U),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_s)))
if mibBuilder.loadTexts:ifBasicAdminGroupV2.setStatus(_D)
ifBasicIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,12))
ifBasicIfGroupV3.setObjects(*((_A,_Z),(_A,_o),(_A,_p),(_A,_q),(_A,_z),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ifBasicIfGroupV3.setStatus(_B)
ifBasicAdminGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,13))
ifBasicAdminGroupV3.setObjects(*((_A,_U),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_s),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:ifBasicAdminGroupV3.setStatus(_D)
ifBasicSignalGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,14))
ifBasicSignalGroupV7.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_r),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_Ab)))
if mibBuilder.loadTexts:ifBasicSignalGroupV7.setStatus(_B)
ifBasicAdminGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,46,1,1,15))
ifBasicAdminGroupV4.setObjects(*((_A,_U),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_s),(_A,_A6),(_A,_A7),(_A,_Ac)))
if mibBuilder.loadTexts:ifBasicAdminGroupV4.setStatus(_B)
lumIfBasicBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,1))
lumIfBasicBasicComplV1.setObjects(*((_A,_G),(_A,_t),(_A,_X),(_A,_Ad)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV1.setStatus(_D)
lumIfBasicBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,2))
lumIfBasicBasicComplV2.setObjects(*((_A,_G),(_A,_t),(_A,_X),(_A,_Ae)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV2.setStatus(_D)
lumIfBasicBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,3))
lumIfBasicBasicComplV3.setObjects(*((_A,_G),(_A,_t),(_A,_X),(_A,_Af)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV3.setStatus(_D)
lumIfBasicBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,4))
lumIfBasicBasicComplV4.setObjects(*((_A,_G),(_A,_A8),(_A,_X),(_A,_Ag)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV4.setStatus(_D)
lumIfBasicBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,5))
lumIfBasicBasicComplV5.setObjects(*((_A,_G),(_A,_A8),(_A,_X),(_A,_Ah)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV5.setStatus(_D)
lumIfBasicBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,6))
lumIfBasicBasicComplV6.setObjects(*((_A,_G),(_A,_u),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV6.setStatus(_D)
lumIfBasicBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,7))
lumIfBasicBasicComplV7.setObjects(*((_A,_G),(_A,_u),(_A,_Ak),(_A,_A9)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV7.setStatus(_D)
lumIfBasicBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,46,1,2,8))
lumIfBasicBasicComplV8.setObjects(*((_A,_G),(_A,_u),(_A,_Al),(_A,_A9)))
if mibBuilder.loadTexts:lumIfBasicBasicComplV8.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfBasicMIBModule':lumIfBasicMIBModule,'lumIfBasicConfs':lumIfBasicConfs,'lumIfBasicGroups':lumIfBasicGroups,_G:ifBasicGeneralGroupV1,_t:ifBasicIfGroupV1,_X:ifBasicAdminGroupV1,_Ad:ifBasicSignalGroupV1,_Ae:ifBasicSignalGroupV2,_Af:ifBasicSignalGroupV3,_Ag:ifBasicSignalGroupV4,_A8:ifBasicIfGroupV2,_Ah:ifBasicSignalGroupV5,_Aj:ifBasicSignalGroupV6,_Ai:ifBasicAdminGroupV2,_u:ifBasicIfGroupV3,_Ak:ifBasicAdminGroupV3,_A9:ifBasicSignalGroupV7,_Al:ifBasicAdminGroupV4,'lumIfBasicCompl':lumIfBasicCompl,'lumIfBasicBasicComplV1':lumIfBasicBasicComplV1,'lumIfBasicBasicComplV2':lumIfBasicBasicComplV2,'lumIfBasicBasicComplV3':lumIfBasicBasicComplV3,'lumIfBasicBasicComplV4':lumIfBasicBasicComplV4,'lumIfBasicBasicComplV5':lumIfBasicBasicComplV5,'lumIfBasicBasicComplV6':lumIfBasicBasicComplV6,'lumIfBasicBasicComplV7':lumIfBasicBasicComplV7,'lumIfBasicBasicComplV8':lumIfBasicBasicComplV8,'lumIfBasicMIBObjects':lumIfBasicMIBObjects,'ifBasicGeneral':ifBasicGeneral,_AO:ifBasicGeneralConfigLastChangeTime,_AP:ifBasicGeneralStateLastChangeTime,_AQ:ifBasicGeneralIfBasicIfTableSize,_AR:ifBasicGeneralIfBasicIfConfigLastChangeTime,_AS:ifBasicGeneralIfBasicIfStateLastChangeTime,_AT:ifBasicGeneralIfBasicAdminTableSize,_AU:ifBasicGeneralIfBasicAdminConfigLastChangeTime,_AV:ifBasicGeneralIfBasicAdminStateLastChangeTime,_AW:ifBasicGeneralIfBasicSignalTableSize,_AX:ifBasicGeneralIfBasicSignalConfigLastChangeTime,_AY:ifBasicGeneralIfBasicSignalStateLastChangeTime,'ifBasicIfList':ifBasicIfList,'ifBasicIfTable':ifBasicIfTable,'ifBasicIfEntry':ifBasicIfEntry,_Z:ifBasicIfIndex,_o:ifBasicIfName,_p:ifBasicIfTxSignalStatus,_q:ifBasicIfRxSignalStatus,_z:ifBasicIfUpId,_AZ:ifBasicIfAid,_Aa:ifBasicIfPhysicalLocation,'ifBasicAdminList':ifBasicAdminList,'ifBasicAdminTable':ifBasicAdminTable,'ifBasicAdminEntry':ifBasicAdminEntry,_U:ifBasicAdminIndex,_a:ifBasicAdminName,_b:ifBasicAdminDescr,_c:ifBasicAdminSubrack,_d:ifBasicAdminSlot,_e:ifBasicAdminTxPort,_f:ifBasicAdminRxPort,_g:ifBasicAdminAdminStatus,_h:ifBasicAdminOperStatus,_i:ifBasicAdminAutoAlarmEnableStatus,_j:ifBasicAdminAutoAlarmEnableReset,_s:ifBasicAdminInterfaceStatus,_A6:ifBasicAdminIfNo,_A7:ifBasicAdminIfType,_Ac:ifBasicAdminNotAvailableForUse,'ifBasicSignalList':ifBasicSignalList,'ifBasicSignalTable':ifBasicSignalTable,'ifBasicSignalEntry':ifBasicSignalEntry,_F:ifBasicSignalIndex,_I:ifBasicSignalName,_J:ifBasicSignalSignalStructure,_K:ifBasicSignalSignalFormat,_L:ifBasicSignalFarEndLoopbackTerminatingLayer,_M:ifBasicSignalFarEndLoopback,_N:ifBasicSignalFarEndLoopbackTimeout,_O:ifBasicSignalNearEndLoopbackTerminatingLayer,_P:ifBasicSignalNearEndLoopback,_Q:ifBasicSignalNearEndLoopbackTimeout,_R:ifBasicSignalFarEndLoopbackEnabled,_S:ifBasicSignalNearEndLoopbackEnabled,_T:ifBasicSignalOpticalLayerMapping,_V:ifBasicSignalConfigurationMismatch,_W:ifBasicSignalActualOpticalLayerMapping,_k:ifBasicSignalSpeed,_l:ifBasicSignalDirection,_m:ifBasicSignalFormatConfigurable,_n:ifBasicSignalFormatConfigurationSharedWithInterface,_r:ifBasicSignalPhysicalLayerMapping,_A0:ifBasicSignalFacilityLoopback,_A1:ifBasicSignalFacilityLoopbackTimeout,_A2:ifBasicSignalFacilityLoopbackEnabled,_A3:ifBasicSignalTerminalLoopback,_A4:ifBasicSignalTerminalLoopbackTimeout,_A5:ifBasicSignalTerminalLoopbackEnabled,_Ab:ifBasicSignalConnectorType})