_A9='otnSmTcmPmMinimalGroupV2'
_A8='otnSmTcmPmMinimalGroupV1'
_A7='otnSmTcmPmGroupV3'
_A6='otnSmTcmPmGroupV2'
_A5='otnSmTcmPmGroup'
_A4='otnGeneralSmTcmPmTableSize'
_A3='otnSmTcmPmBackwardIncomingAlignmentError'
_A2='otnSmTcmPmIncomingAlignmentError'
_A1='otnGeneralMibImplVersion'
_A0='otnGeneralMibSpecVersion'
_z='otnGeneralTestAndIncr'
_y='SubrackNumber'
_x='SlotNumber'
_w='PortNumber'
_v='OtnTIMDetMode'
_u='OtnMonitorConfig'
_t='MgmtNameString'
_s='BoardOrInterfaceOperStatus'
_r='BoardOrInterfaceAdminStatus'
_q='otnGeneralMinimalGroupV1'
_p='otnSmTcmPmNoRemoteTerminatedTcm'
_o='otnSmTcmPmClientMaintenanceIndication'
_n='otnGeneralLastChangeTime'
_m='Integer32'
_l='otnGeneralGroup'
_k='otnSmTcmPmSetTerminatedTcmCommand'
_j='Unsigned32'
_i='otnSmTcmPmLockedDefectIndication'
_h='otnSmTcmPmOpenConnectionIndication'
_g='otnSmTcmPmAlarmIndicationSignal'
_f='otnSmTcmPmBackwardDefectIndication'
_e='otnSmTcmPmTraceMismatch'
_d='otnSmTcmPmObjectProperty'
_c='otnSmTcmPmTraceAlarmMode'
_b='otnSmTcmPmTraceIdMMDetectionMode'
_a='otnSmTcmPmOpSpecificTraceReceived'
_Z='otnSmTcmPmOpSpecificTraceTransmitted'
_Y='otnSmTcmPmDapiTraceExpected'
_X='otnSmTcmPmDapiTraceReceived'
_W='otnSmTcmPmDapiTraceReceivedByte0'
_V='otnSmTcmPmDapiTraceTransmitted'
_U='otnSmTcmPmSapiTraceExpected'
_T='otnSmTcmPmSapiTraceReceived'
_S='otnSmTcmPmSapiTraceReceivedByte0'
_R='otnSmTcmPmSapiTraceTransmitted'
_Q='otnSmTcmPmOperStatus'
_P='otnSmTcmPmAdminStatus'
_O='otnSmTcmPmTxPort'
_N='otnSmTcmPmSlot'
_M='otnSmTcmPmSubrack'
_L='otnSmTcmPmDescr'
_K='otnSmTcmPmTerminatedTcm'
_J='otnSmTcmPmMonitorConfig'
_I='otnSmTcmPmType'
_H='otnSmTcmPmName'
_G='deprecated'
_F='otnSmTcmPmIndex'
_E='read-write'
_D='DisplayString'
_C='read-only'
_B='current'
_A='LUM-OTN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumOtnMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumOtnMIB')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,MgmtNameString,ObjectProperty,OtnMonitorConfig,OtnMonitorType,OtnTIMDetMode,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_r,_s,'CommandString','FaultStatus',_t,'ObjectProperty',_u,'OtnMonitorType',_v,_w,_x,_y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_m,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_j,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'PhysAddress','TextualConvention','TestAndIncr')
lumOtnMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,34))
if mibBuilder.loadTexts:lumOtnMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2012-03-30 00:00','2009-06-15 00:00'))
_LumOtnConfs_ObjectIdentity=ObjectIdentity
lumOtnConfs=_LumOtnConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,34,1))
_LumOtnGroups_ObjectIdentity=ObjectIdentity
lumOtnGroups=_LumOtnGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,34,1,1))
_LumOtnCompl_ObjectIdentity=ObjectIdentity
lumOtnCompl=_LumOtnCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,34,1,2))
_LumOtnMinimalGroups_ObjectIdentity=ObjectIdentity
lumOtnMinimalGroups=_LumOtnMinimalGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,34,1,3))
_LumOtnMinimalCompl_ObjectIdentity=ObjectIdentity
lumOtnMinimalCompl=_LumOtnMinimalCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,34,1,4))
_LumOtnMIBObjects_ObjectIdentity=ObjectIdentity
lumOtnMIBObjects=_LumOtnMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,34,2))
_OtnGeneral_ObjectIdentity=ObjectIdentity
otnGeneral=_OtnGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,34,2,1))
_OtnGeneralTestAndIncr_Type=TestAndIncr
_OtnGeneralTestAndIncr_Object=MibScalar
otnGeneralTestAndIncr=_OtnGeneralTestAndIncr_Object((1,3,6,1,4,1,8708,2,34,2,1,1),_OtnGeneralTestAndIncr_Type())
otnGeneralTestAndIncr.setMaxAccess(_E)
if mibBuilder.loadTexts:otnGeneralTestAndIncr.setStatus(_B)
class _OtnGeneralMibSpecVersion_Type(DisplayString):defaultValue=OctetString('')
_OtnGeneralMibSpecVersion_Type.__name__=_D
_OtnGeneralMibSpecVersion_Object=MibScalar
otnGeneralMibSpecVersion=_OtnGeneralMibSpecVersion_Object((1,3,6,1,4,1,8708,2,34,2,1,2),_OtnGeneralMibSpecVersion_Type())
otnGeneralMibSpecVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:otnGeneralMibSpecVersion.setStatus(_B)
class _OtnGeneralMibImplVersion_Type(DisplayString):defaultValue=OctetString('')
_OtnGeneralMibImplVersion_Type.__name__=_D
_OtnGeneralMibImplVersion_Object=MibScalar
otnGeneralMibImplVersion=_OtnGeneralMibImplVersion_Object((1,3,6,1,4,1,8708,2,34,2,1,3),_OtnGeneralMibImplVersion_Type())
otnGeneralMibImplVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:otnGeneralMibImplVersion.setStatus(_B)
_OtnGeneralLastChangeTime_Type=DateAndTime
_OtnGeneralLastChangeTime_Object=MibScalar
otnGeneralLastChangeTime=_OtnGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,34,2,1,4),_OtnGeneralLastChangeTime_Type())
otnGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:otnGeneralLastChangeTime.setStatus(_B)
_OtnGeneralStateLastChangeTime_Type=DateAndTime
_OtnGeneralStateLastChangeTime_Object=MibScalar
otnGeneralStateLastChangeTime=_OtnGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,34,2,1,5),_OtnGeneralStateLastChangeTime_Type())
otnGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:otnGeneralStateLastChangeTime.setStatus(_B)
_OtnGeneralSmTcmPmTableSize_Type=Unsigned32
_OtnGeneralSmTcmPmTableSize_Object=MibScalar
otnGeneralSmTcmPmTableSize=_OtnGeneralSmTcmPmTableSize_Object((1,3,6,1,4,1,8708,2,34,2,1,6),_OtnGeneralSmTcmPmTableSize_Type())
otnGeneralSmTcmPmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:otnGeneralSmTcmPmTableSize.setStatus(_B)
_OtnSmTcmPmList_ObjectIdentity=ObjectIdentity
otnSmTcmPmList=_OtnSmTcmPmList_ObjectIdentity((1,3,6,1,4,1,8708,2,34,2,2))
_OtnSmTcmPmTable_Object=MibTable
otnSmTcmPmTable=_OtnSmTcmPmTable_Object((1,3,6,1,4,1,8708,2,34,2,2,1))
if mibBuilder.loadTexts:otnSmTcmPmTable.setStatus(_B)
_OtnSmTcmPmEntry_Object=MibTableRow
otnSmTcmPmEntry=_OtnSmTcmPmEntry_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1))
otnSmTcmPmEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:otnSmTcmPmEntry.setStatus(_B)
class _OtnSmTcmPmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OtnSmTcmPmIndex_Type.__name__=_j
_OtnSmTcmPmIndex_Object=MibTableColumn
otnSmTcmPmIndex=_OtnSmTcmPmIndex_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,1),_OtnSmTcmPmIndex_Type())
otnSmTcmPmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmIndex.setStatus(_B)
class _OtnSmTcmPmName_Type(MgmtNameString):defaultValue=OctetString('')
_OtnSmTcmPmName_Type.__name__=_t
_OtnSmTcmPmName_Object=MibTableColumn
otnSmTcmPmName=_OtnSmTcmPmName_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,2),_OtnSmTcmPmName_Type())
otnSmTcmPmName.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmName.setStatus(_B)
_OtnSmTcmPmType_Type=OtnMonitorType
_OtnSmTcmPmType_Object=MibTableColumn
otnSmTcmPmType=_OtnSmTcmPmType_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,3),_OtnSmTcmPmType_Type())
otnSmTcmPmType.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmType.setStatus(_B)
class _OtnSmTcmPmMonitorConfig_Type(OtnMonitorConfig):defaultValue=1
_OtnSmTcmPmMonitorConfig_Type.__name__=_u
_OtnSmTcmPmMonitorConfig_Object=MibTableColumn
otnSmTcmPmMonitorConfig=_OtnSmTcmPmMonitorConfig_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,4),_OtnSmTcmPmMonitorConfig_Type())
otnSmTcmPmMonitorConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmMonitorConfig.setStatus(_B)
class _OtnSmTcmPmTerminatedTcm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),('tcm1',1),('tcm2',2),('tcm3',3),('tcm4',4),('tcm5',5),('tcm6',6)))
_OtnSmTcmPmTerminatedTcm_Type.__name__=_m
_OtnSmTcmPmTerminatedTcm_Object=MibTableColumn
otnSmTcmPmTerminatedTcm=_OtnSmTcmPmTerminatedTcm_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,5),_OtnSmTcmPmTerminatedTcm_Type())
otnSmTcmPmTerminatedTcm.setMaxAccess('read-create')
if mibBuilder.loadTexts:otnSmTcmPmTerminatedTcm.setStatus(_B)
class _OtnSmTcmPmDescr_Type(DisplayString):defaultValue=OctetString('')
_OtnSmTcmPmDescr_Type.__name__=_D
_OtnSmTcmPmDescr_Object=MibTableColumn
otnSmTcmPmDescr=_OtnSmTcmPmDescr_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,6),_OtnSmTcmPmDescr_Type())
otnSmTcmPmDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmDescr.setStatus(_B)
class _OtnSmTcmPmSubrack_Type(SubrackNumber):defaultValue=0
_OtnSmTcmPmSubrack_Type.__name__=_y
_OtnSmTcmPmSubrack_Object=MibTableColumn
otnSmTcmPmSubrack=_OtnSmTcmPmSubrack_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,7),_OtnSmTcmPmSubrack_Type())
otnSmTcmPmSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmSubrack.setStatus(_B)
class _OtnSmTcmPmSlot_Type(SlotNumber):defaultValue=0
_OtnSmTcmPmSlot_Type.__name__=_x
_OtnSmTcmPmSlot_Object=MibTableColumn
otnSmTcmPmSlot=_OtnSmTcmPmSlot_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,8),_OtnSmTcmPmSlot_Type())
otnSmTcmPmSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmSlot.setStatus(_B)
class _OtnSmTcmPmTxPort_Type(PortNumber):defaultValue=0
_OtnSmTcmPmTxPort_Type.__name__=_w
_OtnSmTcmPmTxPort_Object=MibTableColumn
otnSmTcmPmTxPort=_OtnSmTcmPmTxPort_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,9),_OtnSmTcmPmTxPort_Type())
otnSmTcmPmTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmTxPort.setStatus(_B)
class _OtnSmTcmPmAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_OtnSmTcmPmAdminStatus_Type.__name__=_r
_OtnSmTcmPmAdminStatus_Object=MibTableColumn
otnSmTcmPmAdminStatus=_OtnSmTcmPmAdminStatus_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,10),_OtnSmTcmPmAdminStatus_Type())
otnSmTcmPmAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmAdminStatus.setStatus(_B)
class _OtnSmTcmPmOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_OtnSmTcmPmOperStatus_Type.__name__=_s
_OtnSmTcmPmOperStatus_Object=MibTableColumn
otnSmTcmPmOperStatus=_OtnSmTcmPmOperStatus_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,11),_OtnSmTcmPmOperStatus_Type())
otnSmTcmPmOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmOperStatus.setStatus(_B)
class _OtnSmTcmPmSapiTraceTransmitted_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmSapiTraceTransmitted_Type.__name__=_D
_OtnSmTcmPmSapiTraceTransmitted_Object=MibTableColumn
otnSmTcmPmSapiTraceTransmitted=_OtnSmTcmPmSapiTraceTransmitted_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,12),_OtnSmTcmPmSapiTraceTransmitted_Type())
otnSmTcmPmSapiTraceTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmSapiTraceTransmitted.setStatus(_B)
class _OtnSmTcmPmSapiTraceReceivedByte0_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OtnSmTcmPmSapiTraceReceivedByte0_Type.__name__=_j
_OtnSmTcmPmSapiTraceReceivedByte0_Object=MibTableColumn
otnSmTcmPmSapiTraceReceivedByte0=_OtnSmTcmPmSapiTraceReceivedByte0_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,13),_OtnSmTcmPmSapiTraceReceivedByte0_Type())
otnSmTcmPmSapiTraceReceivedByte0.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmSapiTraceReceivedByte0.setStatus(_B)
class _OtnSmTcmPmSapiTraceReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmSapiTraceReceived_Type.__name__=_D
_OtnSmTcmPmSapiTraceReceived_Object=MibTableColumn
otnSmTcmPmSapiTraceReceived=_OtnSmTcmPmSapiTraceReceived_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,14),_OtnSmTcmPmSapiTraceReceived_Type())
otnSmTcmPmSapiTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmSapiTraceReceived.setStatus(_B)
class _OtnSmTcmPmSapiTraceExpected_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmSapiTraceExpected_Type.__name__=_D
_OtnSmTcmPmSapiTraceExpected_Object=MibTableColumn
otnSmTcmPmSapiTraceExpected=_OtnSmTcmPmSapiTraceExpected_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,15),_OtnSmTcmPmSapiTraceExpected_Type())
otnSmTcmPmSapiTraceExpected.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmSapiTraceExpected.setStatus(_B)
class _OtnSmTcmPmDapiTraceTransmitted_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmDapiTraceTransmitted_Type.__name__=_D
_OtnSmTcmPmDapiTraceTransmitted_Object=MibTableColumn
otnSmTcmPmDapiTraceTransmitted=_OtnSmTcmPmDapiTraceTransmitted_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,16),_OtnSmTcmPmDapiTraceTransmitted_Type())
otnSmTcmPmDapiTraceTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmDapiTraceTransmitted.setStatus(_B)
class _OtnSmTcmPmDapiTraceReceivedByte0_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OtnSmTcmPmDapiTraceReceivedByte0_Type.__name__=_j
_OtnSmTcmPmDapiTraceReceivedByte0_Object=MibTableColumn
otnSmTcmPmDapiTraceReceivedByte0=_OtnSmTcmPmDapiTraceReceivedByte0_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,17),_OtnSmTcmPmDapiTraceReceivedByte0_Type())
otnSmTcmPmDapiTraceReceivedByte0.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmDapiTraceReceivedByte0.setStatus(_B)
class _OtnSmTcmPmDapiTraceReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmDapiTraceReceived_Type.__name__=_D
_OtnSmTcmPmDapiTraceReceived_Object=MibTableColumn
otnSmTcmPmDapiTraceReceived=_OtnSmTcmPmDapiTraceReceived_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,18),_OtnSmTcmPmDapiTraceReceived_Type())
otnSmTcmPmDapiTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmDapiTraceReceived.setStatus(_B)
class _OtnSmTcmPmDapiTraceExpected_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_OtnSmTcmPmDapiTraceExpected_Type.__name__=_D
_OtnSmTcmPmDapiTraceExpected_Object=MibTableColumn
otnSmTcmPmDapiTraceExpected=_OtnSmTcmPmDapiTraceExpected_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,19),_OtnSmTcmPmDapiTraceExpected_Type())
otnSmTcmPmDapiTraceExpected.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmDapiTraceExpected.setStatus(_B)
class _OtnSmTcmPmOpSpecificTraceTransmitted_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_OtnSmTcmPmOpSpecificTraceTransmitted_Type.__name__=_D
_OtnSmTcmPmOpSpecificTraceTransmitted_Object=MibTableColumn
otnSmTcmPmOpSpecificTraceTransmitted=_OtnSmTcmPmOpSpecificTraceTransmitted_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,20),_OtnSmTcmPmOpSpecificTraceTransmitted_Type())
otnSmTcmPmOpSpecificTraceTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmOpSpecificTraceTransmitted.setStatus(_B)
class _OtnSmTcmPmOpSpecificTraceReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_OtnSmTcmPmOpSpecificTraceReceived_Type.__name__=_D
_OtnSmTcmPmOpSpecificTraceReceived_Object=MibTableColumn
otnSmTcmPmOpSpecificTraceReceived=_OtnSmTcmPmOpSpecificTraceReceived_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,21),_OtnSmTcmPmOpSpecificTraceReceived_Type())
otnSmTcmPmOpSpecificTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmOpSpecificTraceReceived.setStatus(_B)
class _OtnSmTcmPmTraceIdMMDetectionMode_Type(OtnTIMDetMode):defaultValue=0
_OtnSmTcmPmTraceIdMMDetectionMode_Type.__name__=_v
_OtnSmTcmPmTraceIdMMDetectionMode_Object=MibTableColumn
otnSmTcmPmTraceIdMMDetectionMode=_OtnSmTcmPmTraceIdMMDetectionMode_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,22),_OtnSmTcmPmTraceIdMMDetectionMode_Type())
otnSmTcmPmTraceIdMMDetectionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmTraceIdMMDetectionMode.setStatus(_B)
class _OtnSmTcmPmTraceAlarmMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_OtnSmTcmPmTraceAlarmMode_Type.__name__=_m
_OtnSmTcmPmTraceAlarmMode_Object=MibTableColumn
otnSmTcmPmTraceAlarmMode=_OtnSmTcmPmTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,23),_OtnSmTcmPmTraceAlarmMode_Type())
otnSmTcmPmTraceAlarmMode.setMaxAccess(_E)
if mibBuilder.loadTexts:otnSmTcmPmTraceAlarmMode.setStatus(_B)
_OtnSmTcmPmObjectProperty_Type=ObjectProperty
_OtnSmTcmPmObjectProperty_Object=MibTableColumn
otnSmTcmPmObjectProperty=_OtnSmTcmPmObjectProperty_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,24),_OtnSmTcmPmObjectProperty_Type())
otnSmTcmPmObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmObjectProperty.setStatus(_B)
_OtnSmTcmPmTraceMismatch_Type=FaultStatus
_OtnSmTcmPmTraceMismatch_Object=MibTableColumn
otnSmTcmPmTraceMismatch=_OtnSmTcmPmTraceMismatch_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,25),_OtnSmTcmPmTraceMismatch_Type())
otnSmTcmPmTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmTraceMismatch.setStatus(_B)
_OtnSmTcmPmBackwardDefectIndication_Type=FaultStatus
_OtnSmTcmPmBackwardDefectIndication_Object=MibTableColumn
otnSmTcmPmBackwardDefectIndication=_OtnSmTcmPmBackwardDefectIndication_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,26),_OtnSmTcmPmBackwardDefectIndication_Type())
otnSmTcmPmBackwardDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmBackwardDefectIndication.setStatus(_B)
_OtnSmTcmPmAlarmIndicationSignal_Type=FaultStatus
_OtnSmTcmPmAlarmIndicationSignal_Object=MibTableColumn
otnSmTcmPmAlarmIndicationSignal=_OtnSmTcmPmAlarmIndicationSignal_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,27),_OtnSmTcmPmAlarmIndicationSignal_Type())
otnSmTcmPmAlarmIndicationSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmAlarmIndicationSignal.setStatus(_B)
_OtnSmTcmPmOpenConnectionIndication_Type=FaultStatus
_OtnSmTcmPmOpenConnectionIndication_Object=MibTableColumn
otnSmTcmPmOpenConnectionIndication=_OtnSmTcmPmOpenConnectionIndication_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,28),_OtnSmTcmPmOpenConnectionIndication_Type())
otnSmTcmPmOpenConnectionIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmOpenConnectionIndication.setStatus(_B)
_OtnSmTcmPmClientMaintenanceIndication_Type=FaultStatus
_OtnSmTcmPmClientMaintenanceIndication_Object=MibTableColumn
otnSmTcmPmClientMaintenanceIndication=_OtnSmTcmPmClientMaintenanceIndication_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,29),_OtnSmTcmPmClientMaintenanceIndication_Type())
otnSmTcmPmClientMaintenanceIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmClientMaintenanceIndication.setStatus(_G)
_OtnSmTcmPmLockedDefectIndication_Type=FaultStatus
_OtnSmTcmPmLockedDefectIndication_Object=MibTableColumn
otnSmTcmPmLockedDefectIndication=_OtnSmTcmPmLockedDefectIndication_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,30),_OtnSmTcmPmLockedDefectIndication_Type())
otnSmTcmPmLockedDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmLockedDefectIndication.setStatus(_B)
_OtnSmTcmPmSetTerminatedTcmCommand_Type=CommandString
_OtnSmTcmPmSetTerminatedTcmCommand_Object=MibTableColumn
otnSmTcmPmSetTerminatedTcmCommand=_OtnSmTcmPmSetTerminatedTcmCommand_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,31),_OtnSmTcmPmSetTerminatedTcmCommand_Type())
otnSmTcmPmSetTerminatedTcmCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmSetTerminatedTcmCommand.setStatus(_B)
_OtnSmTcmPmNoRemoteTerminatedTcm_Type=FaultStatus
_OtnSmTcmPmNoRemoteTerminatedTcm_Object=MibTableColumn
otnSmTcmPmNoRemoteTerminatedTcm=_OtnSmTcmPmNoRemoteTerminatedTcm_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,32),_OtnSmTcmPmNoRemoteTerminatedTcm_Type())
otnSmTcmPmNoRemoteTerminatedTcm.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmNoRemoteTerminatedTcm.setStatus(_B)
_OtnSmTcmPmIncomingAlignmentError_Type=FaultStatus
_OtnSmTcmPmIncomingAlignmentError_Object=MibTableColumn
otnSmTcmPmIncomingAlignmentError=_OtnSmTcmPmIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,33),_OtnSmTcmPmIncomingAlignmentError_Type())
otnSmTcmPmIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmIncomingAlignmentError.setStatus(_B)
_OtnSmTcmPmBackwardIncomingAlignmentError_Type=FaultStatus
_OtnSmTcmPmBackwardIncomingAlignmentError_Object=MibTableColumn
otnSmTcmPmBackwardIncomingAlignmentError=_OtnSmTcmPmBackwardIncomingAlignmentError_Object((1,3,6,1,4,1,8708,2,34,2,2,1,1,34),_OtnSmTcmPmBackwardIncomingAlignmentError_Type())
otnSmTcmPmBackwardIncomingAlignmentError.setMaxAccess(_C)
if mibBuilder.loadTexts:otnSmTcmPmBackwardIncomingAlignmentError.setStatus(_B)
otnGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,1,1))
otnGeneralGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_n)))
if mibBuilder.loadTexts:otnGeneralGroup.setStatus(_B)
otnSmTcmPmGroup=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,1,2))
otnSmTcmPmGroup.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_o),(_A,_i)))
if mibBuilder.loadTexts:otnSmTcmPmGroup.setStatus(_G)
otnSmTcmPmGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,1,3))
otnSmTcmPmGroupV2.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_p)))
if mibBuilder.loadTexts:otnSmTcmPmGroupV2.setStatus(_G)
otnSmTcmPmGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,1,4))
otnSmTcmPmGroupV3.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_p),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:otnSmTcmPmGroupV3.setStatus(_B)
otnGeneralMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,3,1))
otnGeneralMinimalGroupV1.setObjects(*((_A,_n),(_A,_A4)))
if mibBuilder.loadTexts:otnGeneralMinimalGroupV1.setStatus(_B)
otnSmTcmPmMinimalGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,3,2))
otnSmTcmPmMinimalGroupV1.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_b),(_A,_R),(_A,_V),(_A,_Z),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_a),(_A,_U),(_A,_Y),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_o),(_A,_i)))
if mibBuilder.loadTexts:otnSmTcmPmMinimalGroupV1.setStatus(_G)
otnSmTcmPmMinimalGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,34,1,3,3))
otnSmTcmPmMinimalGroupV2.setObjects(*((_A,_F),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_b),(_A,_R),(_A,_V),(_A,_Z),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_a),(_A,_U),(_A,_Y),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k)))
if mibBuilder.loadTexts:otnSmTcmPmMinimalGroupV2.setStatus(_B)
lumOtnBasicCompl1=ModuleCompliance((1,3,6,1,4,1,8708,2,34,1,2,1))
lumOtnBasicCompl1.setObjects(*((_A,_l),(_A,_A5)))
if mibBuilder.loadTexts:lumOtnBasicCompl1.setStatus(_G)
lumOtnBasicCompl2=ModuleCompliance((1,3,6,1,4,1,8708,2,34,1,2,2))
lumOtnBasicCompl2.setObjects(*((_A,_l),(_A,_A6)))
if mibBuilder.loadTexts:lumOtnBasicCompl2.setStatus(_G)
lumOtnBasicCompl3=ModuleCompliance((1,3,6,1,4,1,8708,2,34,1,2,3))
lumOtnBasicCompl3.setObjects(*((_A,_l),(_A,_A7)))
if mibBuilder.loadTexts:lumOtnBasicCompl3.setStatus(_B)
lumOtmMinimalComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,34,1,4,1))
lumOtmMinimalComplV1.setObjects(*((_A,_q),(_A,_A8)))
if mibBuilder.loadTexts:lumOtmMinimalComplV1.setStatus(_G)
lumOtmMinimalComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,34,1,4,2))
lumOtmMinimalComplV2.setObjects(*((_A,_q),(_A,_A9)))
if mibBuilder.loadTexts:lumOtmMinimalComplV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumOtnMIBModule':lumOtnMIBModule,'lumOtnConfs':lumOtnConfs,'lumOtnGroups':lumOtnGroups,_l:otnGeneralGroup,_A5:otnSmTcmPmGroup,_A6:otnSmTcmPmGroupV2,_A7:otnSmTcmPmGroupV3,'lumOtnCompl':lumOtnCompl,'lumOtnBasicCompl1':lumOtnBasicCompl1,'lumOtnBasicCompl2':lumOtnBasicCompl2,'lumOtnBasicCompl3':lumOtnBasicCompl3,'lumOtnMinimalGroups':lumOtnMinimalGroups,_q:otnGeneralMinimalGroupV1,_A8:otnSmTcmPmMinimalGroupV1,_A9:otnSmTcmPmMinimalGroupV2,'lumOtnMinimalCompl':lumOtnMinimalCompl,'lumOtmMinimalComplV1':lumOtmMinimalComplV1,'lumOtmMinimalComplV2':lumOtmMinimalComplV2,'lumOtnMIBObjects':lumOtnMIBObjects,'otnGeneral':otnGeneral,_z:otnGeneralTestAndIncr,_A0:otnGeneralMibSpecVersion,_A1:otnGeneralMibImplVersion,_n:otnGeneralLastChangeTime,'otnGeneralStateLastChangeTime':otnGeneralStateLastChangeTime,_A4:otnGeneralSmTcmPmTableSize,'otnSmTcmPmList':otnSmTcmPmList,'otnSmTcmPmTable':otnSmTcmPmTable,'otnSmTcmPmEntry':otnSmTcmPmEntry,_F:otnSmTcmPmIndex,_H:otnSmTcmPmName,_I:otnSmTcmPmType,_J:otnSmTcmPmMonitorConfig,_K:otnSmTcmPmTerminatedTcm,_L:otnSmTcmPmDescr,_M:otnSmTcmPmSubrack,_N:otnSmTcmPmSlot,_O:otnSmTcmPmTxPort,_P:otnSmTcmPmAdminStatus,_Q:otnSmTcmPmOperStatus,_R:otnSmTcmPmSapiTraceTransmitted,_S:otnSmTcmPmSapiTraceReceivedByte0,_T:otnSmTcmPmSapiTraceReceived,_U:otnSmTcmPmSapiTraceExpected,_V:otnSmTcmPmDapiTraceTransmitted,_W:otnSmTcmPmDapiTraceReceivedByte0,_X:otnSmTcmPmDapiTraceReceived,_Y:otnSmTcmPmDapiTraceExpected,_Z:otnSmTcmPmOpSpecificTraceTransmitted,_a:otnSmTcmPmOpSpecificTraceReceived,_b:otnSmTcmPmTraceIdMMDetectionMode,_c:otnSmTcmPmTraceAlarmMode,_d:otnSmTcmPmObjectProperty,_e:otnSmTcmPmTraceMismatch,_f:otnSmTcmPmBackwardDefectIndication,_g:otnSmTcmPmAlarmIndicationSignal,_h:otnSmTcmPmOpenConnectionIndication,_o:otnSmTcmPmClientMaintenanceIndication,_i:otnSmTcmPmLockedDefectIndication,_k:otnSmTcmPmSetTerminatedTcmCommand,_p:otnSmTcmPmNoRemoteTerminatedTcm,_A2:otnSmTcmPmIncomingAlignmentError,_A3:otnSmTcmPmBackwardIncomingAlignmentError})