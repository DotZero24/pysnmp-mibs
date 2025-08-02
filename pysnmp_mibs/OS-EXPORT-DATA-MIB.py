_A0='osExportMandatoryGroup'
_z='osExportDataSecureMode'
_y='osExportDataSecureRemotePassword'
_x='osExportDataClientId'
_w='osExportDataDescription'
_v='osExportDataErrorStatus'
_u='osExportDataAdminStatus'
_t='osExportDataOperStatus'
_s='osExportDataLastTransferTime'
_r='osExportDataNextTransferTime'
_q='osExportDataLastSampleTime'
_p='osExportDataNextSampleTime'
_o='osExportDataLastStartTime'
_n='osExportDataStartTime'
_m='osExportDataTransfersCounter'
_l='osExportDataTransferBlockSize'
_k='osExportDataTransferProtocol'
_j='osExportDataSamplesCounter'
_i='osExportDataSampleInterval'
_h='osExportDataSampleType'
_g='osExportDataRemotePassword'
_f='osExportDataRemoteUsername'
_e='osExportDataRemoteFileName'
_d='osExportDataRemoteDirName'
_c='osExportDataServerAddress'
_b='osExportDataServerAddressType'
_a='osExportDataTransferProtocolSup'
_Z='osExportDataSampleTypeSup'
_Y='osExportDataExtEntry'
_X='osExportDataName'
_W='sftpClient'
_V='scpClient'
_U='ftpClient'
_T='tftpClient'
_S='soamTestLmStatsHistory'
_R='soamTestDmStatsHistory'
_Q='delayMeasureHrTests'
_P='rfc2544Tests'
_O='ipSlaTests'
_N='delayMeasureTests'
_M='loopbackTests'
_L='serviceCounters'
_K='SnmpAdminString'
_J='InetAddressType'
_I='InetAddress'
_H='Bits'
_G='DateAndTime'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='OS-EXPORT-DATA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,_J)
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,_F,'PhysAddress','TextualConvention')
osExportData=ModuleIdentity((1,3,6,1,4,1,6926,2,16))
if mibBuilder.loadTexts:osExportData.setRevisions(('2013-05-23 00:00','2011-06-01 00:00','2009-11-17 00:00'))
_OsExportDataCapabilities_ObjectIdentity=ObjectIdentity
osExportDataCapabilities=_OsExportDataCapabilities_ObjectIdentity((1,3,6,1,4,1,6926,2,16,1))
class _OsExportDataSampleTypeSup_Type(Bits):namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6),(_S,7)))
_OsExportDataSampleTypeSup_Type.__name__=_H
_OsExportDataSampleTypeSup_Object=MibScalar
osExportDataSampleTypeSup=_OsExportDataSampleTypeSup_Object((1,3,6,1,4,1,6926,2,16,1,1),_OsExportDataSampleTypeSup_Type())
osExportDataSampleTypeSup.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataSampleTypeSup.setStatus(_A)
class _OsExportDataTransferProtocolSup_Type(Bits):namedValues=NamedValues(*(('other',0),(_T,1),(_U,2),(_V,3),(_W,4)))
_OsExportDataTransferProtocolSup_Type.__name__=_H
_OsExportDataTransferProtocolSup_Object=MibScalar
osExportDataTransferProtocolSup=_OsExportDataTransferProtocolSup_Object((1,3,6,1,4,1,6926,2,16,1,2),_OsExportDataTransferProtocolSup_Type())
osExportDataTransferProtocolSup.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataTransferProtocolSup.setStatus(_A)
_OsExportDataTable_Object=MibTable
osExportDataTable=_OsExportDataTable_Object((1,3,6,1,4,1,6926,2,16,2))
if mibBuilder.loadTexts:osExportDataTable.setStatus(_A)
_OsExportDataEntry_Object=MibTableRow
osExportDataEntry=_OsExportDataEntry_Object((1,3,6,1,4,1,6926,2,16,2,1))
osExportDataEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:osExportDataEntry.setStatus(_A)
class _OsExportDataName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_OsExportDataName_Type.__name__=_K
_OsExportDataName_Object=MibTableColumn
osExportDataName=_OsExportDataName_Object((1,3,6,1,4,1,6926,2,16,2,1,1),_OsExportDataName_Type())
osExportDataName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:osExportDataName.setStatus(_A)
class _OsExportDataServerAddressType_Type(InetAddressType):defaultValue=1
_OsExportDataServerAddressType_Type.__name__=_J
_OsExportDataServerAddressType_Object=MibTableColumn
osExportDataServerAddressType=_OsExportDataServerAddressType_Object((1,3,6,1,4,1,6926,2,16,2,1,2),_OsExportDataServerAddressType_Type())
osExportDataServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataServerAddressType.setStatus(_A)
class _OsExportDataServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataServerAddress_Type.__name__=_I
_OsExportDataServerAddress_Object=MibTableColumn
osExportDataServerAddress=_OsExportDataServerAddress_Object((1,3,6,1,4,1,6926,2,16,2,1,3),_OsExportDataServerAddress_Type())
osExportDataServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataServerAddress.setStatus(_A)
class _OsExportDataRemoteDirName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataRemoteDirName_Type.__name__=_F
_OsExportDataRemoteDirName_Object=MibTableColumn
osExportDataRemoteDirName=_OsExportDataRemoteDirName_Object((1,3,6,1,4,1,6926,2,16,2,1,4),_OsExportDataRemoteDirName_Type())
osExportDataRemoteDirName.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataRemoteDirName.setStatus(_A)
class _OsExportDataRemoteFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_OsExportDataRemoteFileName_Type.__name__=_F
_OsExportDataRemoteFileName_Object=MibTableColumn
osExportDataRemoteFileName=_OsExportDataRemoteFileName_Object((1,3,6,1,4,1,6926,2,16,2,1,5),_OsExportDataRemoteFileName_Type())
osExportDataRemoteFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataRemoteFileName.setStatus(_A)
class _OsExportDataRemoteUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataRemoteUsername_Type.__name__=_F
_OsExportDataRemoteUsername_Object=MibTableColumn
osExportDataRemoteUsername=_OsExportDataRemoteUsername_Object((1,3,6,1,4,1,6926,2,16,2,1,6),_OsExportDataRemoteUsername_Type())
osExportDataRemoteUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataRemoteUsername.setStatus(_A)
class _OsExportDataRemotePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataRemotePassword_Type.__name__=_F
_OsExportDataRemotePassword_Object=MibTableColumn
osExportDataRemotePassword=_OsExportDataRemotePassword_Object((1,3,6,1,4,1,6926,2,16,2,1,7),_OsExportDataRemotePassword_Type())
osExportDataRemotePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataRemotePassword.setStatus(_A)
class _OsExportDataSampleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_OsExportDataSampleType_Type.__name__=_E
_OsExportDataSampleType_Object=MibTableColumn
osExportDataSampleType=_OsExportDataSampleType_Object((1,3,6,1,4,1,6926,2,16,2,1,10),_OsExportDataSampleType_Type())
osExportDataSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataSampleType.setStatus(_A)
class _OsExportDataSampleInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('once',1),('month',2),('week',3),('day',4),('every12hrs',5),('every8hrs',6),('every6hrs',7),('every4hrs',8),('every2hrs',9),('every1hr',10),('every30mins',11),('every15mins',12),('every10mins',13),('every5mins',14),('every2mins',15),('every1min',16),('every30secs',17),('every15secs',18),('every10secs',19),('every5secs',20),('every2secs',21),('every1sec',22)))
_OsExportDataSampleInterval_Type.__name__=_E
_OsExportDataSampleInterval_Object=MibTableColumn
osExportDataSampleInterval=_OsExportDataSampleInterval_Object((1,3,6,1,4,1,6926,2,16,2,1,11),_OsExportDataSampleInterval_Type())
osExportDataSampleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataSampleInterval.setStatus(_A)
class _OsExportDataSamplesCounter_Type(Integer32):defaultValue=0
_OsExportDataSamplesCounter_Type.__name__=_E
_OsExportDataSamplesCounter_Object=MibTableColumn
osExportDataSamplesCounter=_OsExportDataSamplesCounter_Object((1,3,6,1,4,1,6926,2,16,2,1,12),_OsExportDataSamplesCounter_Type())
osExportDataSamplesCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataSamplesCounter.setStatus(_A)
class _OsExportDataTransferProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_T,2),(_U,3),(_V,4),(_W,5)))
_OsExportDataTransferProtocol_Type.__name__=_E
_OsExportDataTransferProtocol_Object=MibTableColumn
osExportDataTransferProtocol=_OsExportDataTransferProtocol_Object((1,3,6,1,4,1,6926,2,16,2,1,15),_OsExportDataTransferProtocol_Type())
osExportDataTransferProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataTransferProtocol.setStatus(_A)
class _OsExportDataTransferBlockSize_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_OsExportDataTransferBlockSize_Type.__name__=_E
_OsExportDataTransferBlockSize_Object=MibTableColumn
osExportDataTransferBlockSize=_OsExportDataTransferBlockSize_Object((1,3,6,1,4,1,6926,2,16,2,1,16),_OsExportDataTransferBlockSize_Type())
osExportDataTransferBlockSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataTransferBlockSize.setStatus(_A)
class _OsExportDataTransfersCounter_Type(Integer32):defaultValue=0
_OsExportDataTransfersCounter_Type.__name__=_E
_OsExportDataTransfersCounter_Object=MibTableColumn
osExportDataTransfersCounter=_OsExportDataTransfersCounter_Object((1,3,6,1,4,1,6926,2,16,2,1,17),_OsExportDataTransfersCounter_Type())
osExportDataTransfersCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataTransfersCounter.setStatus(_A)
class _OsExportDataStartTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataStartTime_Type.__name__=_G
_OsExportDataStartTime_Object=MibTableColumn
osExportDataStartTime=_OsExportDataStartTime_Object((1,3,6,1,4,1,6926,2,16,2,1,20),_OsExportDataStartTime_Type())
osExportDataStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataStartTime.setStatus(_A)
class _OsExportDataLastStartTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataLastStartTime_Type.__name__=_G
_OsExportDataLastStartTime_Object=MibTableColumn
osExportDataLastStartTime=_OsExportDataLastStartTime_Object((1,3,6,1,4,1,6926,2,16,2,1,21),_OsExportDataLastStartTime_Type())
osExportDataLastStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataLastStartTime.setStatus(_A)
class _OsExportDataNextSampleTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataNextSampleTime_Type.__name__=_G
_OsExportDataNextSampleTime_Object=MibTableColumn
osExportDataNextSampleTime=_OsExportDataNextSampleTime_Object((1,3,6,1,4,1,6926,2,16,2,1,22),_OsExportDataNextSampleTime_Type())
osExportDataNextSampleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataNextSampleTime.setStatus(_A)
class _OsExportDataLastSampleTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataLastSampleTime_Type.__name__=_G
_OsExportDataLastSampleTime_Object=MibTableColumn
osExportDataLastSampleTime=_OsExportDataLastSampleTime_Object((1,3,6,1,4,1,6926,2,16,2,1,23),_OsExportDataLastSampleTime_Type())
osExportDataLastSampleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataLastSampleTime.setStatus(_A)
class _OsExportDataNextTransferTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataNextTransferTime_Type.__name__=_G
_OsExportDataNextTransferTime_Object=MibTableColumn
osExportDataNextTransferTime=_OsExportDataNextTransferTime_Object((1,3,6,1,4,1,6926,2,16,2,1,24),_OsExportDataNextTransferTime_Type())
osExportDataNextTransferTime.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataNextTransferTime.setStatus(_A)
class _OsExportDataLastTransferTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_OsExportDataLastTransferTime_Type.__name__=_G
_OsExportDataLastTransferTime_Object=MibTableColumn
osExportDataLastTransferTime=_OsExportDataLastTransferTime_Object((1,3,6,1,4,1,6926,2,16,2,1,25),_OsExportDataLastTransferTime_Type())
osExportDataLastTransferTime.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataLastTransferTime.setStatus(_A)
class _OsExportDataOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('waitForSchedule',1),('waitForSample',2),('sampleInProcess',3),('transferInProcess',4),('sampleCompletedOk',5),('transferCompletedOk',6),('sampleError',7),('transferError',8),('exportCanceled',9)))
_OsExportDataOperStatus_Type.__name__=_E
_OsExportDataOperStatus_Object=MibTableColumn
osExportDataOperStatus=_OsExportDataOperStatus_Object((1,3,6,1,4,1,6926,2,16,2,1,30),_OsExportDataOperStatus_Type())
osExportDataOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataOperStatus.setStatus(_A)
class _OsExportDataAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('stop',1),('start',2),('continue',3),('sample',4),('transfer',5),('invalid',6),('waitForInit',7)))
_OsExportDataAdminStatus_Type.__name__=_E
_OsExportDataAdminStatus_Object=MibTableColumn
osExportDataAdminStatus=_OsExportDataAdminStatus_Object((1,3,6,1,4,1,6926,2,16,2,1,31),_OsExportDataAdminStatus_Type())
osExportDataAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataAdminStatus.setStatus(_A)
class _OsExportDataErrorStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noError',1),('transferFailure',2),('sampleFailure',3),('stopFailure',4),('startFailure',5),('deleteFailure',6),('unknownError',7)))
_OsExportDataErrorStatus_Type.__name__=_E
_OsExportDataErrorStatus_Object=MibTableColumn
osExportDataErrorStatus=_OsExportDataErrorStatus_Object((1,3,6,1,4,1,6926,2,16,2,1,32),_OsExportDataErrorStatus_Type())
osExportDataErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataErrorStatus.setStatus(_A)
class _OsExportDataDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_OsExportDataDescription_Type.__name__=_F
_OsExportDataDescription_Object=MibTableColumn
osExportDataDescription=_OsExportDataDescription_Object((1,3,6,1,4,1,6926,2,16,2,1,40),_OsExportDataDescription_Type())
osExportDataDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataDescription.setStatus(_A)
class _OsExportDataClientId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataClientId_Type.__name__=_F
_OsExportDataClientId_Object=MibTableColumn
osExportDataClientId=_OsExportDataClientId_Object((1,3,6,1,4,1,6926,2,16,2,1,41),_OsExportDataClientId_Type())
osExportDataClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataClientId.setStatus(_A)
_OsExportDataExtTable_Object=MibTable
osExportDataExtTable=_OsExportDataExtTable_Object((1,3,6,1,4,1,6926,2,16,3))
if mibBuilder.loadTexts:osExportDataExtTable.setStatus(_A)
_OsExportDataExtEntry_Object=MibTableRow
osExportDataExtEntry=_OsExportDataExtEntry_Object((1,3,6,1,4,1,6926,2,16,3,1))
if mibBuilder.loadTexts:osExportDataExtEntry.setStatus(_A)
class _OsExportDataSecureRemotePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OsExportDataSecureRemotePassword_Type.__name__=_F
_OsExportDataSecureRemotePassword_Object=MibTableColumn
osExportDataSecureRemotePassword=_OsExportDataSecureRemotePassword_Object((1,3,6,1,4,1,6926,2,16,3,1,1),_OsExportDataSecureRemotePassword_Type())
osExportDataSecureRemotePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:osExportDataSecureRemotePassword.setStatus(_A)
class _OsExportDataSecureMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('plainPassword',1),('encryptedPassword',2)))
_OsExportDataSecureMode_Type.__name__=_E
_OsExportDataSecureMode_Object=MibTableColumn
osExportDataSecureMode=_OsExportDataSecureMode_Object((1,3,6,1,4,1,6926,2,16,3,1,2),_OsExportDataSecureMode_Type())
osExportDataSecureMode.setMaxAccess(_D)
if mibBuilder.loadTexts:osExportDataSecureMode.setStatus(_A)
_OsExportDataConformance_ObjectIdentity=ObjectIdentity
osExportDataConformance=_OsExportDataConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,16,100))
_OsExportDataMIBCompliances_ObjectIdentity=ObjectIdentity
osExportDataMIBCompliances=_OsExportDataMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,16,100,1))
_OsExportDataMIBGroups_ObjectIdentity=ObjectIdentity
osExportDataMIBGroups=_OsExportDataMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,16,100,2))
osExportDataEntry.registerAugmentions((_B,_Y))
osExportDataExtEntry.setIndexNames(*osExportDataEntry.getIndexNames())
osExportMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,16,100,2,1))
osExportMandatoryGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:osExportMandatoryGroup.setStatus(_A)
osExportMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,16,100,1,1))
osExportMIBCompliance.setObjects((_B,_A0))
if mibBuilder.loadTexts:osExportMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osExportData':osExportData,'osExportDataCapabilities':osExportDataCapabilities,_Z:osExportDataSampleTypeSup,_a:osExportDataTransferProtocolSup,'osExportDataTable':osExportDataTable,'osExportDataEntry':osExportDataEntry,_X:osExportDataName,_b:osExportDataServerAddressType,_c:osExportDataServerAddress,_d:osExportDataRemoteDirName,_e:osExportDataRemoteFileName,_f:osExportDataRemoteUsername,_g:osExportDataRemotePassword,_h:osExportDataSampleType,_i:osExportDataSampleInterval,_j:osExportDataSamplesCounter,_k:osExportDataTransferProtocol,_l:osExportDataTransferBlockSize,_m:osExportDataTransfersCounter,_n:osExportDataStartTime,_o:osExportDataLastStartTime,_p:osExportDataNextSampleTime,_q:osExportDataLastSampleTime,_r:osExportDataNextTransferTime,_s:osExportDataLastTransferTime,_t:osExportDataOperStatus,_u:osExportDataAdminStatus,_v:osExportDataErrorStatus,_w:osExportDataDescription,_x:osExportDataClientId,'osExportDataExtTable':osExportDataExtTable,_Y:osExportDataExtEntry,_y:osExportDataSecureRemotePassword,_z:osExportDataSecureMode,'osExportDataConformance':osExportDataConformance,'osExportDataMIBCompliances':osExportDataMIBCompliances,'osExportMIBCompliance':osExportMIBCompliance,'osExportDataMIBGroups':osExportDataMIBGroups,_A0:osExportMandatoryGroup})