_A3='dSyslogAttackLogGroup'
_A2='dSyslogLogServerGroup'
_A1='dSyslogLogSmtpGroup'
_A0='dSyslogLogConsoleGroup'
_z='dSyslogDiscriminatorGroup'
_y='dSyslogGeneralGroup'
_x='dSyslogAttackLogDescription'
_w='dSyslogAttackLogDateAndTime'
_v='dSyslogAttackLogTableNum'
_u='dSyslogClearAttackLogBufByUnit'
_t='dSyslogServerDiscriminator'
_s='dSyslogServerFacility'
_r='dSyslogServerSeverity'
_q='dSyslogServerPort'
_p='dSyslogServerRowstatus'
_o='dSyslogSourceIfIndex'
_n='dSyslogLogSmtpDiscriminator'
_m='dSyslogLogSmtpSeverity'
_l='dSyslogLogSmtpEnabled'
_k='dSyslogLogConsoleDiscriminator'
_j='dSyslogLogConsoleSeverity'
_i='dSyslogLogConsoleEnabled'
_h='dSyslogDisSeverityList'
_g='dSyslogDisSeverityFilterMode'
_f='dSyslogDisFacilityFilterString'
_e='dSyslogDisFacilityFilterMode'
_d='dSyslogDiscriminatorRowstatus'
_c='dSyslogLogOnEnabled'
_b='dSyslogBufferDescription'
_a='dSyslogBufferDateAndTime'
_Z='dSyslogBufferTableNum'
_Y='dSyslogLogBufWriteDelay'
_X='dSyslogLogBufSeverity'
_W='dSyslogLogBufferEnabled'
_V='dSyslogClearLogBuffer'
_U='dSyslogAttackLogIndex'
_T='dSyslogAttackLogUnitId'
_S='dSyslogBufferIndex'
_R='dSyslogServerVrfName'
_Q='dSyslogServerAddress'
_P='dSyslogServerAddressType'
_O='includes'
_N='notSpecified'
_M='dSyslogDiscriminatorName'
_L='SyslogSeverity'
_K='SyslogFacility'
_J='DisplayString'
_I='dSyslogLogBufDiscriminator'
_H='Integer32'
_G='Unsigned32'
_F='read-only'
_E='not-accessible'
_D='read-create'
_C='read-write'
_B='DLINKSW-SYSLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkIndustrialCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkIndustrialCommon')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'PhysAddress','RowStatus','TextualConvention','TruthValue')
SyslogFacility,SyslogSeverity=mibBuilder.importSymbols('SYSLOG-TC-MIB',_K,_L)
dlinkSwSyslogMIB=ModuleIdentity((1,3,6,1,4,1,171,14,13))
if mibBuilder.loadTexts:dlinkSwSyslogMIB.setRevisions(('2013-09-14 00:00',))
_DSyslogMIBNotifications_ObjectIdentity=ObjectIdentity
dSyslogMIBNotifications=_DSyslogMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,14,13,0))
_DSyslogMIBObjects_ObjectIdentity=ObjectIdentity
dSyslogMIBObjects=_DSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,14,13,1))
_DSyslogGeneral_ObjectIdentity=ObjectIdentity
dSyslogGeneral=_DSyslogGeneral_ObjectIdentity((1,3,6,1,4,1,171,14,13,1,1))
_DSyslogSourceIfIndex_Type=InterfaceIndexOrZero
_DSyslogSourceIfIndex_Object=MibScalar
dSyslogSourceIfIndex=_DSyslogSourceIfIndex_Object((1,3,6,1,4,1,171,14,13,1,1,1),_DSyslogSourceIfIndex_Type())
dSyslogSourceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogSourceIfIndex.setStatus(_A)
_DSyslogDiscriminatorTable_Object=MibTable
dSyslogDiscriminatorTable=_DSyslogDiscriminatorTable_Object((1,3,6,1,4,1,171,14,13,1,1,2))
if mibBuilder.loadTexts:dSyslogDiscriminatorTable.setStatus(_A)
_DSyslogDiscriminatorEntry_Object=MibTableRow
dSyslogDiscriminatorEntry=_DSyslogDiscriminatorEntry_Object((1,3,6,1,4,1,171,14,13,1,1,2,1))
dSyslogDiscriminatorEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:dSyslogDiscriminatorEntry.setStatus(_A)
_DSyslogDiscriminatorName_Type=DisplayString
_DSyslogDiscriminatorName_Object=MibTableColumn
dSyslogDiscriminatorName=_DSyslogDiscriminatorName_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,1),_DSyslogDiscriminatorName_Type())
dSyslogDiscriminatorName.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogDiscriminatorName.setStatus(_A)
_DSyslogDiscriminatorRowstatus_Type=RowStatus
_DSyslogDiscriminatorRowstatus_Object=MibTableColumn
dSyslogDiscriminatorRowstatus=_DSyslogDiscriminatorRowstatus_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,2),_DSyslogDiscriminatorRowstatus_Type())
dSyslogDiscriminatorRowstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogDiscriminatorRowstatus.setStatus(_A)
class _DSyslogDisFacilityFilterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('drops',2),(_O,3)))
_DSyslogDisFacilityFilterMode_Type.__name__=_H
_DSyslogDisFacilityFilterMode_Object=MibTableColumn
dSyslogDisFacilityFilterMode=_DSyslogDisFacilityFilterMode_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,3),_DSyslogDisFacilityFilterMode_Type())
dSyslogDisFacilityFilterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogDisFacilityFilterMode.setStatus(_A)
_DSyslogDisFacilityFilterString_Type=DisplayString
_DSyslogDisFacilityFilterString_Object=MibTableColumn
dSyslogDisFacilityFilterString=_DSyslogDisFacilityFilterString_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,4),_DSyslogDisFacilityFilterString_Type())
dSyslogDisFacilityFilterString.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogDisFacilityFilterString.setStatus(_A)
class _DSyslogDisSeverityFilterMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('drops',2),(_O,3)))
_DSyslogDisSeverityFilterMode_Type.__name__=_H
_DSyslogDisSeverityFilterMode_Object=MibTableColumn
dSyslogDisSeverityFilterMode=_DSyslogDisSeverityFilterMode_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,5),_DSyslogDisSeverityFilterMode_Type())
dSyslogDisSeverityFilterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogDisSeverityFilterMode.setStatus(_A)
class _DSyslogDisSeverityList_Type(Bits):namedValues=NamedValues(*(('emerg',0),('alert',1),('crit',2),('err',3),('warning',4),('notice',5),('info',6),('debug',7)))
_DSyslogDisSeverityList_Type.__name__='Bits'
_DSyslogDisSeverityList_Object=MibTableColumn
dSyslogDisSeverityList=_DSyslogDisSeverityList_Object((1,3,6,1,4,1,171,14,13,1,1,2,1,6),_DSyslogDisSeverityList_Type())
dSyslogDisSeverityList.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogDisSeverityList.setStatus(_A)
_DSyslogLogOnEnabled_Type=TruthValue
_DSyslogLogOnEnabled_Object=MibScalar
dSyslogLogOnEnabled=_DSyslogLogOnEnabled_Object((1,3,6,1,4,1,171,14,13,1,1,3),_DSyslogLogOnEnabled_Type())
dSyslogLogOnEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogOnEnabled.setStatus(_A)
_DSyslogSourceIfType_Type=DisplayString
_DSyslogSourceIfType_Object=MibScalar
dSyslogSourceIfType=_DSyslogSourceIfType_Object((1,3,6,1,4,1,171,14,13,1,1,4),_DSyslogSourceIfType_Type())
dSyslogSourceIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogSourceIfType.setStatus(_A)
_DSyslogLogbuffer_ObjectIdentity=ObjectIdentity
dSyslogLogbuffer=_DSyslogLogbuffer_ObjectIdentity((1,3,6,1,4,1,171,14,13,1,2))
if mibBuilder.loadTexts:dSyslogLogbuffer.setStatus(_A)
class _DSyslogClearLogBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noOp',2)))
_DSyslogClearLogBuffer_Type.__name__=_H
_DSyslogClearLogBuffer_Object=MibScalar
dSyslogClearLogBuffer=_DSyslogClearLogBuffer_Object((1,3,6,1,4,1,171,14,13,1,2,1),_DSyslogClearLogBuffer_Type())
dSyslogClearLogBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogClearLogBuffer.setStatus(_A)
_DSyslogLogBufferEnabled_Type=TruthValue
_DSyslogLogBufferEnabled_Object=MibScalar
dSyslogLogBufferEnabled=_DSyslogLogBufferEnabled_Object((1,3,6,1,4,1,171,14,13,1,2,2),_DSyslogLogBufferEnabled_Type())
dSyslogLogBufferEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogBufferEnabled.setStatus(_A)
_DSyslogLogBufSeverity_Type=SyslogSeverity
_DSyslogLogBufSeverity_Object=MibScalar
dSyslogLogBufSeverity=_DSyslogLogBufSeverity_Object((1,3,6,1,4,1,171,14,13,1,2,3),_DSyslogLogBufSeverity_Type())
dSyslogLogBufSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogBufSeverity.setStatus(_A)
_DSyslogLogBufDiscriminator_Type=DisplayString
_DSyslogLogBufDiscriminator_Object=MibScalar
dSyslogLogBufDiscriminator=_DSyslogLogBufDiscriminator_Object((1,3,6,1,4,1,171,14,13,1,2,4),_DSyslogLogBufDiscriminator_Type())
dSyslogLogBufDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogBufDiscriminator.setStatus(_A)
_DSyslogLogBufWriteDelay_Type=Integer32
_DSyslogLogBufWriteDelay_Object=MibScalar
dSyslogLogBufWriteDelay=_DSyslogLogBufWriteDelay_Object((1,3,6,1,4,1,171,14,13,1,2,5),_DSyslogLogBufWriteDelay_Type())
dSyslogLogBufWriteDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogBufWriteDelay.setStatus(_A)
if mibBuilder.loadTexts:dSyslogLogBufWriteDelay.setUnits('seconds')
_DSyslogClearAttackLogBufByUnit_Type=Integer32
_DSyslogClearAttackLogBufByUnit_Object=MibScalar
dSyslogClearAttackLogBufByUnit=_DSyslogClearAttackLogBufByUnit_Object((1,3,6,1,4,1,171,14,13,1,2,6),_DSyslogClearAttackLogBufByUnit_Type())
dSyslogClearAttackLogBufByUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogClearAttackLogBufByUnit.setStatus(_A)
_DSyslogLogConsole_ObjectIdentity=ObjectIdentity
dSyslogLogConsole=_DSyslogLogConsole_ObjectIdentity((1,3,6,1,4,1,171,14,13,1,3))
if mibBuilder.loadTexts:dSyslogLogConsole.setStatus(_A)
_DSyslogLogConsoleEnabled_Type=TruthValue
_DSyslogLogConsoleEnabled_Object=MibScalar
dSyslogLogConsoleEnabled=_DSyslogLogConsoleEnabled_Object((1,3,6,1,4,1,171,14,13,1,3,1),_DSyslogLogConsoleEnabled_Type())
dSyslogLogConsoleEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogConsoleEnabled.setStatus(_A)
_DSyslogLogConsoleSeverity_Type=SyslogSeverity
_DSyslogLogConsoleSeverity_Object=MibScalar
dSyslogLogConsoleSeverity=_DSyslogLogConsoleSeverity_Object((1,3,6,1,4,1,171,14,13,1,3,2),_DSyslogLogConsoleSeverity_Type())
dSyslogLogConsoleSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogConsoleSeverity.setStatus(_A)
_DSyslogLogConsoleDiscriminator_Type=DisplayString
_DSyslogLogConsoleDiscriminator_Object=MibScalar
dSyslogLogConsoleDiscriminator=_DSyslogLogConsoleDiscriminator_Object((1,3,6,1,4,1,171,14,13,1,3,3),_DSyslogLogConsoleDiscriminator_Type())
dSyslogLogConsoleDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogConsoleDiscriminator.setStatus(_A)
_DSyslogLogSmtp_ObjectIdentity=ObjectIdentity
dSyslogLogSmtp=_DSyslogLogSmtp_ObjectIdentity((1,3,6,1,4,1,171,14,13,1,4))
if mibBuilder.loadTexts:dSyslogLogSmtp.setStatus(_A)
_DSyslogLogSmtpEnabled_Type=TruthValue
_DSyslogLogSmtpEnabled_Object=MibScalar
dSyslogLogSmtpEnabled=_DSyslogLogSmtpEnabled_Object((1,3,6,1,4,1,171,14,13,1,4,1),_DSyslogLogSmtpEnabled_Type())
dSyslogLogSmtpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogSmtpEnabled.setStatus(_A)
_DSyslogLogSmtpSeverity_Type=SyslogSeverity
_DSyslogLogSmtpSeverity_Object=MibScalar
dSyslogLogSmtpSeverity=_DSyslogLogSmtpSeverity_Object((1,3,6,1,4,1,171,14,13,1,4,2),_DSyslogLogSmtpSeverity_Type())
dSyslogLogSmtpSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogSmtpSeverity.setStatus(_A)
_DSyslogLogSmtpDiscriminator_Type=DisplayString
_DSyslogLogSmtpDiscriminator_Object=MibScalar
dSyslogLogSmtpDiscriminator=_DSyslogLogSmtpDiscriminator_Object((1,3,6,1,4,1,171,14,13,1,4,3),_DSyslogLogSmtpDiscriminator_Type())
dSyslogLogSmtpDiscriminator.setMaxAccess(_C)
if mibBuilder.loadTexts:dSyslogLogSmtpDiscriminator.setStatus(_A)
_DSyslogServerTable_Object=MibTable
dSyslogServerTable=_DSyslogServerTable_Object((1,3,6,1,4,1,171,14,13,1,5))
if mibBuilder.loadTexts:dSyslogServerTable.setStatus(_A)
_DSyslogServerEntry_Object=MibTableRow
dSyslogServerEntry=_DSyslogServerEntry_Object((1,3,6,1,4,1,171,14,13,1,5,1))
dSyslogServerEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:dSyslogServerEntry.setStatus(_A)
_DSyslogServerAddressType_Type=InetAddressType
_DSyslogServerAddressType_Object=MibTableColumn
dSyslogServerAddressType=_DSyslogServerAddressType_Object((1,3,6,1,4,1,171,14,13,1,5,1,1),_DSyslogServerAddressType_Type())
dSyslogServerAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogServerAddressType.setStatus(_A)
_DSyslogServerAddress_Type=InetAddress
_DSyslogServerAddress_Object=MibTableColumn
dSyslogServerAddress=_DSyslogServerAddress_Object((1,3,6,1,4,1,171,14,13,1,5,1,2),_DSyslogServerAddress_Type())
dSyslogServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogServerAddress.setStatus(_A)
class _DSyslogServerVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DSyslogServerVrfName_Type.__name__=_J
_DSyslogServerVrfName_Object=MibTableColumn
dSyslogServerVrfName=_DSyslogServerVrfName_Object((1,3,6,1,4,1,171,14,13,1,5,1,3),_DSyslogServerVrfName_Type())
dSyslogServerVrfName.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogServerVrfName.setStatus(_A)
_DSyslogServerRowstatus_Type=RowStatus
_DSyslogServerRowstatus_Object=MibTableColumn
dSyslogServerRowstatus=_DSyslogServerRowstatus_Object((1,3,6,1,4,1,171,14,13,1,5,1,4),_DSyslogServerRowstatus_Type())
dSyslogServerRowstatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogServerRowstatus.setStatus(_A)
class _DSyslogServerPort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(514,514),ValueRangeConstraint(1024,65535))
_DSyslogServerPort_Type.__name__=_G
_DSyslogServerPort_Object=MibTableColumn
dSyslogServerPort=_DSyslogServerPort_Object((1,3,6,1,4,1,171,14,13,1,5,1,5),_DSyslogServerPort_Type())
dSyslogServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogServerPort.setStatus(_A)
class _DSyslogServerSeverity_Type(SyslogSeverity):defaultValue=4
_DSyslogServerSeverity_Type.__name__=_L
_DSyslogServerSeverity_Object=MibTableColumn
dSyslogServerSeverity=_DSyslogServerSeverity_Object((1,3,6,1,4,1,171,14,13,1,5,1,6),_DSyslogServerSeverity_Type())
dSyslogServerSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogServerSeverity.setStatus(_A)
class _DSyslogServerFacility_Type(SyslogFacility):defaultValue=23
_DSyslogServerFacility_Type.__name__=_K
_DSyslogServerFacility_Object=MibTableColumn
dSyslogServerFacility=_DSyslogServerFacility_Object((1,3,6,1,4,1,171,14,13,1,5,1,7),_DSyslogServerFacility_Type())
dSyslogServerFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogServerFacility.setStatus(_A)
_DSyslogServerDiscriminator_Type=DisplayString
_DSyslogServerDiscriminator_Object=MibTableColumn
dSyslogServerDiscriminator=_DSyslogServerDiscriminator_Object((1,3,6,1,4,1,171,14,13,1,5,1,8),_DSyslogServerDiscriminator_Type())
dSyslogServerDiscriminator.setMaxAccess(_D)
if mibBuilder.loadTexts:dSyslogServerDiscriminator.setStatus(_A)
_DSyslogBufferTableNum_Type=Unsigned32
_DSyslogBufferTableNum_Object=MibScalar
dSyslogBufferTableNum=_DSyslogBufferTableNum_Object((1,3,6,1,4,1,171,14,13,1,6),_DSyslogBufferTableNum_Type())
dSyslogBufferTableNum.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogBufferTableNum.setStatus(_A)
_DSyslogBufferTable_Object=MibTable
dSyslogBufferTable=_DSyslogBufferTable_Object((1,3,6,1,4,1,171,14,13,1,7))
if mibBuilder.loadTexts:dSyslogBufferTable.setStatus(_A)
_DSyslogBufferEntry_Object=MibTableRow
dSyslogBufferEntry=_DSyslogBufferEntry_Object((1,3,6,1,4,1,171,14,13,1,7,1))
dSyslogBufferEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:dSyslogBufferEntry.setStatus(_A)
class _DSyslogBufferIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_DSyslogBufferIndex_Type.__name__=_G
_DSyslogBufferIndex_Object=MibTableColumn
dSyslogBufferIndex=_DSyslogBufferIndex_Object((1,3,6,1,4,1,171,14,13,1,7,1,1),_DSyslogBufferIndex_Type())
dSyslogBufferIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogBufferIndex.setStatus(_A)
_DSyslogBufferDateAndTime_Type=DateAndTime
_DSyslogBufferDateAndTime_Object=MibTableColumn
dSyslogBufferDateAndTime=_DSyslogBufferDateAndTime_Object((1,3,6,1,4,1,171,14,13,1,7,1,2),_DSyslogBufferDateAndTime_Type())
dSyslogBufferDateAndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogBufferDateAndTime.setStatus(_A)
_DSyslogBufferDescription_Type=DisplayString
_DSyslogBufferDescription_Object=MibTableColumn
dSyslogBufferDescription=_DSyslogBufferDescription_Object((1,3,6,1,4,1,171,14,13,1,7,1,3),_DSyslogBufferDescription_Type())
dSyslogBufferDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogBufferDescription.setStatus(_A)
_DSyslogAttackLogTableNum_Type=Unsigned32
_DSyslogAttackLogTableNum_Object=MibScalar
dSyslogAttackLogTableNum=_DSyslogAttackLogTableNum_Object((1,3,6,1,4,1,171,14,13,1,8),_DSyslogAttackLogTableNum_Type())
dSyslogAttackLogTableNum.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogAttackLogTableNum.setStatus(_A)
_DSyslogAttackLogTable_Object=MibTable
dSyslogAttackLogTable=_DSyslogAttackLogTable_Object((1,3,6,1,4,1,171,14,13,1,9))
if mibBuilder.loadTexts:dSyslogAttackLogTable.setStatus(_A)
_DSyslogAttackLogEntry_Object=MibTableRow
dSyslogAttackLogEntry=_DSyslogAttackLogEntry_Object((1,3,6,1,4,1,171,14,13,1,9,1))
dSyslogAttackLogEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:dSyslogAttackLogEntry.setStatus(_A)
class _DSyslogAttackLogUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DSyslogAttackLogUnitId_Type.__name__=_G
_DSyslogAttackLogUnitId_Object=MibTableColumn
dSyslogAttackLogUnitId=_DSyslogAttackLogUnitId_Object((1,3,6,1,4,1,171,14,13,1,9,1,1),_DSyslogAttackLogUnitId_Type())
dSyslogAttackLogUnitId.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogAttackLogUnitId.setStatus(_A)
class _DSyslogAttackLogIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_DSyslogAttackLogIndex_Type.__name__=_G
_DSyslogAttackLogIndex_Object=MibTableColumn
dSyslogAttackLogIndex=_DSyslogAttackLogIndex_Object((1,3,6,1,4,1,171,14,13,1,9,1,2),_DSyslogAttackLogIndex_Type())
dSyslogAttackLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dSyslogAttackLogIndex.setStatus(_A)
_DSyslogAttackLogDateAndTime_Type=DateAndTime
_DSyslogAttackLogDateAndTime_Object=MibTableColumn
dSyslogAttackLogDateAndTime=_DSyslogAttackLogDateAndTime_Object((1,3,6,1,4,1,171,14,13,1,9,1,3),_DSyslogAttackLogDateAndTime_Type())
dSyslogAttackLogDateAndTime.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogAttackLogDateAndTime.setStatus(_A)
_DSyslogAttackLogDescription_Type=DisplayString
_DSyslogAttackLogDescription_Object=MibTableColumn
dSyslogAttackLogDescription=_DSyslogAttackLogDescription_Object((1,3,6,1,4,1,171,14,13,1,9,1,4),_DSyslogAttackLogDescription_Type())
dSyslogAttackLogDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:dSyslogAttackLogDescription.setStatus(_A)
_DSyslogMIBConformance_ObjectIdentity=ObjectIdentity
dSyslogMIBConformance=_DSyslogMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,14,13,2))
_DSyslogMIBCompliances_ObjectIdentity=ObjectIdentity
dSyslogMIBCompliances=_DSyslogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,14,13,2,1))
_DSyslogMIBGroups_ObjectIdentity=ObjectIdentity
dSyslogMIBGroups=_DSyslogMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,14,13,2,1,2))
dSyslogGeneralGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,1))
dSyslogGeneralGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_I),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:dSyslogGeneralGroup.setStatus(_A)
dSyslogDiscriminatorGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,2))
dSyslogDiscriminatorGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_I)))
if mibBuilder.loadTexts:dSyslogDiscriminatorGroup.setStatus(_A)
dSyslogLogConsoleGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,3))
dSyslogLogConsoleGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:dSyslogLogConsoleGroup.setStatus(_A)
dSyslogLogSmtpGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,4))
dSyslogLogSmtpGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:dSyslogLogSmtpGroup.setStatus(_A)
dSyslogLogServerGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,5))
dSyslogLogServerGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:dSyslogLogServerGroup.setStatus(_A)
dSyslogAttackLogGroup=ObjectGroup((1,3,6,1,4,1,171,14,13,2,1,2,6))
dSyslogAttackLogGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:dSyslogAttackLogGroup.setStatus(_A)
dSyslogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,14,13,2,1,1))
dSyslogMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:dSyslogMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkSwSyslogMIB':dlinkSwSyslogMIB,'dSyslogMIBNotifications':dSyslogMIBNotifications,'dSyslogMIBObjects':dSyslogMIBObjects,'dSyslogGeneral':dSyslogGeneral,_o:dSyslogSourceIfIndex,'dSyslogDiscriminatorTable':dSyslogDiscriminatorTable,'dSyslogDiscriminatorEntry':dSyslogDiscriminatorEntry,_M:dSyslogDiscriminatorName,_d:dSyslogDiscriminatorRowstatus,_e:dSyslogDisFacilityFilterMode,_f:dSyslogDisFacilityFilterString,_g:dSyslogDisSeverityFilterMode,_h:dSyslogDisSeverityList,_c:dSyslogLogOnEnabled,'dSyslogSourceIfType':dSyslogSourceIfType,'dSyslogLogbuffer':dSyslogLogbuffer,_V:dSyslogClearLogBuffer,_W:dSyslogLogBufferEnabled,_X:dSyslogLogBufSeverity,_I:dSyslogLogBufDiscriminator,_Y:dSyslogLogBufWriteDelay,_u:dSyslogClearAttackLogBufByUnit,'dSyslogLogConsole':dSyslogLogConsole,_i:dSyslogLogConsoleEnabled,_j:dSyslogLogConsoleSeverity,_k:dSyslogLogConsoleDiscriminator,'dSyslogLogSmtp':dSyslogLogSmtp,_l:dSyslogLogSmtpEnabled,_m:dSyslogLogSmtpSeverity,_n:dSyslogLogSmtpDiscriminator,'dSyslogServerTable':dSyslogServerTable,'dSyslogServerEntry':dSyslogServerEntry,_P:dSyslogServerAddressType,_Q:dSyslogServerAddress,_R:dSyslogServerVrfName,_p:dSyslogServerRowstatus,_q:dSyslogServerPort,_r:dSyslogServerSeverity,_s:dSyslogServerFacility,_t:dSyslogServerDiscriminator,_Z:dSyslogBufferTableNum,'dSyslogBufferTable':dSyslogBufferTable,'dSyslogBufferEntry':dSyslogBufferEntry,_S:dSyslogBufferIndex,_a:dSyslogBufferDateAndTime,_b:dSyslogBufferDescription,_v:dSyslogAttackLogTableNum,'dSyslogAttackLogTable':dSyslogAttackLogTable,'dSyslogAttackLogEntry':dSyslogAttackLogEntry,_T:dSyslogAttackLogUnitId,_U:dSyslogAttackLogIndex,_w:dSyslogAttackLogDateAndTime,_x:dSyslogAttackLogDescription,'dSyslogMIBConformance':dSyslogMIBConformance,'dSyslogMIBCompliances':dSyslogMIBCompliances,'dSyslogMIBCompliance':dSyslogMIBCompliance,'dSyslogMIBGroups':dSyslogMIBGroups,_y:dSyslogGeneralGroup,_z:dSyslogDiscriminatorGroup,_A0:dSyslogLogConsoleGroup,_A1:dSyslogLogSmtpGroup,_A2:dSyslogLogServerGroup,_A3:dSyslogAttackLogGroup})