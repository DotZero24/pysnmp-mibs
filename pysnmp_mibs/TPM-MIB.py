_Al='tpmExcpReportHCStatSumIXSq'
_Ak='tpmExcpReportOverflowStatSumIXSq'
_Aj='tpmExcpReportStatSumIXSq'
_Ai='tpmExcpReportHCStatSumIX'
_Ah='tpmExcpReportOverflowStatSumIX'
_Ag='tpmExcpReportStatSumIX'
_Af='tpmExcpReportHCStatSumSq'
_Ae='tpmExcpReportOverflowStatSumSq'
_Ad='tpmExcpReportStatSumSq'
_Ac='tpmExcpReportStatMinimum'
_Ab='tpmExcpReportStatMaximum'
_Aa='tpmExcpReportHCStatSumX'
_AZ='tpmExcpReportOverflowStatSumX'
_AY='tpmExcpReportStatSumX'
_AX='tpmExcpReportHCStatN'
_AW='tpmExcpReportOverflowStatN'
_AV='tpmExcpReportStatN'
_AU='tpmCurReportSize'
_AT='tpmCurReportCompletion'
_AS='tpmCurReportMetricValue'
_AR='tpmAggrReportHCStatSumIXSq'
_AQ='tpmAggrReportOverflowStatSumIXSq'
_AP='tpmAggrReportStatSumIXSq'
_AO='tpmAggrReportHCStatSumIX'
_AN='tpmAggrReportOverflowStatSumIX'
_AM='tpmAggrReportStatSumIX'
_AL='tpmAggrReportHCStatSumSq'
_AK='tpmAggrReportOverflowStatSumSq'
_AJ='tpmAggrReportStatSumSq'
_AI='tpmAggrReportStatMinimum'
_AH='tpmAggrReportStatMaximum'
_AG='tpmAggrReportHCStatSumX'
_AF='tpmAggrReportOverflowStatSumX'
_AE='tpmAggrReportStatSumX'
_AD='tpmAggrReportHCStatN'
_AC='tpmAggrReportOverflowStatN'
_AB='tpmAggrReportStatN'
_AA='tpmAggrReportCntrlStatus'
_A9='tpmAggrReportCntrlStorageType'
_A8='tpmAggrReportCntrlOwner'
_A7='tpmAggrReportCntrlDroppedFrames'
_A6='tpmAggrReportCntrlInsertsDenied'
_A5='tpmAggrReportCntrlReportNumber'
_A4='tpmAggrReportCntrlStartTime'
_A3='tpmAggrReportCntrlGrantedReports'
_A2='tpmAggrReportCntrlReqReports'
_A1='tpmAggrReportCntrlGrantedSize'
_A0='tpmAggrReportCntrlReqSize'
_z='tpmAggrReportCntrlInterval'
_y='tpmAggrReportCntrlAggrType'
_x='tpmAggrReportCntrlDataSource'
_w='tpmAggrReportCntrlApmCntrlIndex'
_v='tpmMetricDefGlobalID'
_u='tpmMetricDefReference'
_t='tpmMetricDefName'
_s='tpmMetricDefDirType'
_r='tpmMetricDefType'
_q='tpmTransMetricDirConfig'
_p='tpmTransMetricMetricIndex'
_o='tpmTransMetricProtocolIndex'
_n='tpmTransMetricDirLastChange'
_m='tpmClockSource'
_l='tpmClockMaxSkew'
_k='tpmClockResolution'
_j='tpmExcpReportTransMetricIndex'
_i='tpmCurReportApmTransactionID'
_h='tpmCurReportApmNameClientID'
_g='tpmCurReportServerAddress'
_f='tpmCurReportTransMetricIndex'
_e='tpmCurReportAppLocalIndex'
_d='tpmAggrReportApmNameClientID'
_c='tpmAggrReportServerAddress'
_b='tpmAggrReportTransMetricIndex'
_a='tpmAggrReportAppLocalIndex'
_Z='tpmAggrReportIndex'
_Y='tpmMetricDefinitionID'
_X='read-write'
_W='tpmTransMetricIndex'
_V='tpmTransMetricAppLocalIndex'
_U='apmReportGroup'
_T='apmExceptionIndex'
_S='apmExceptionGroup'
_R='apmAppDirResponsivenessType'
_Q='apmAppDirAppLocalIndex'
_P='tpmExceptionReportsGroup'
_O='tpmCurrentReportsGroup'
_N='protocolDirLocalIndex'
_M='RMON2-MIB'
_L='OctetString'
_K='tpmAggregateReportsGroup'
_J='tpmCapabilitiesGroup'
_I='tpmAggrReportCntrlIndex'
_H='Integer32'
_G='APM-MIB'
_F='read-create'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='TPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AppLocalIndex,DataSourceOrZero,RmonClientID,TransactionAggregationType,apmAppDirAppLocalIndex,apmAppDirResponsivenessType,apmExceptionGroup,apmExceptionIndex,apmReportGroup=mibBuilder.importSymbols(_G,'AppLocalIndex','DataSourceOrZero','RmonClientID','TransactionAggregationType',_Q,_R,_S,_T,_U)
ZeroBasedCounter64,=mibBuilder.importSymbols('HCNUM-TC','ZeroBasedCounter64')
OwnerString,rmon=mibBuilder.importSymbols('RMON-MIB','OwnerString','rmon')
ZeroBasedCounter32,protocolDirLocalIndex=mibBuilder.importSymbols(_M,'ZeroBasedCounter32',_N)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp')
SspmClockMaxSkew,SspmClockSource,SspmMicroSeconds=mibBuilder.importSymbols('SSPM-MIB','SspmClockMaxSkew','SspmClockSource','SspmMicroSeconds')
tpmMIB=ModuleIdentity((1,3,6,1,2,1,16,30))
if mibBuilder.loadTexts:tpmMIB.setRevisions(('2005-07-28 00:00',))
class TpmTransactionMetricIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class TpmMetricDefID(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpmCapabilities_ObjectIdentity=ObjectIdentity
tpmCapabilities=_TpmCapabilities_ObjectIdentity((1,3,6,1,2,1,16,30,1))
_TpmClockResolution_Type=SspmMicroSeconds
_TpmClockResolution_Object=MibScalar
tpmClockResolution=_TpmClockResolution_Object((1,3,6,1,2,1,16,30,1,1),_TpmClockResolution_Type())
tpmClockResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmClockResolution.setStatus(_A)
_TpmClockMaxSkew_Type=SspmClockMaxSkew
_TpmClockMaxSkew_Object=MibScalar
tpmClockMaxSkew=_TpmClockMaxSkew_Object((1,3,6,1,2,1,16,30,1,2),_TpmClockMaxSkew_Type())
tpmClockMaxSkew.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmClockMaxSkew.setStatus(_A)
_TpmClockSource_Type=SspmClockSource
_TpmClockSource_Object=MibScalar
tpmClockSource=_TpmClockSource_Object((1,3,6,1,2,1,16,30,1,3),_TpmClockSource_Type())
tpmClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmClockSource.setStatus(_A)
_TpmTransMetricDirLastChange_Type=TimeStamp
_TpmTransMetricDirLastChange_Object=MibScalar
tpmTransMetricDirLastChange=_TpmTransMetricDirLastChange_Object((1,3,6,1,2,1,16,30,1,4),_TpmTransMetricDirLastChange_Type())
tpmTransMetricDirLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmTransMetricDirLastChange.setStatus(_A)
_TpmTransMetricDirTable_Object=MibTable
tpmTransMetricDirTable=_TpmTransMetricDirTable_Object((1,3,6,1,2,1,16,30,1,5))
if mibBuilder.loadTexts:tpmTransMetricDirTable.setStatus(_A)
_TpmTransMetricDirEntry_Object=MibTableRow
tpmTransMetricDirEntry=_TpmTransMetricDirEntry_Object((1,3,6,1,2,1,16,30,1,5,1))
tpmTransMetricDirEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:tpmTransMetricDirEntry.setStatus(_A)
_TpmTransMetricAppLocalIndex_Type=AppLocalIndex
_TpmTransMetricAppLocalIndex_Object=MibTableColumn
tpmTransMetricAppLocalIndex=_TpmTransMetricAppLocalIndex_Object((1,3,6,1,2,1,16,30,1,5,1,1),_TpmTransMetricAppLocalIndex_Type())
tpmTransMetricAppLocalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmTransMetricAppLocalIndex.setStatus(_A)
_TpmTransMetricIndex_Type=TpmTransactionMetricIndex
_TpmTransMetricIndex_Object=MibTableColumn
tpmTransMetricIndex=_TpmTransMetricIndex_Object((1,3,6,1,2,1,16,30,1,5,1,2),_TpmTransMetricIndex_Type())
tpmTransMetricIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmTransMetricIndex.setStatus(_A)
class _TpmTransMetricProtocolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpmTransMetricProtocolIndex_Type.__name__=_E
_TpmTransMetricProtocolIndex_Object=MibTableColumn
tpmTransMetricProtocolIndex=_TpmTransMetricProtocolIndex_Object((1,3,6,1,2,1,16,30,1,5,1,3),_TpmTransMetricProtocolIndex_Type())
tpmTransMetricProtocolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmTransMetricProtocolIndex.setStatus(_A)
class _TpmTransMetricMetricIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpmTransMetricMetricIndex_Type.__name__=_E
_TpmTransMetricMetricIndex_Object=MibTableColumn
tpmTransMetricMetricIndex=_TpmTransMetricMetricIndex_Object((1,3,6,1,2,1,16,30,1,5,1,4),_TpmTransMetricMetricIndex_Type())
tpmTransMetricMetricIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmTransMetricMetricIndex.setStatus(_A)
class _TpmTransMetricDirConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('supportedOff',2),('supportedOn',3)))
_TpmTransMetricDirConfig_Type.__name__=_H
_TpmTransMetricDirConfig_Object=MibTableColumn
tpmTransMetricDirConfig=_TpmTransMetricDirConfig_Object((1,3,6,1,2,1,16,30,1,5,1,5),_TpmTransMetricDirConfig_Type())
tpmTransMetricDirConfig.setMaxAccess(_X)
if mibBuilder.loadTexts:tpmTransMetricDirConfig.setStatus(_A)
_TpmMetricDefTable_Object=MibTable
tpmMetricDefTable=_TpmMetricDefTable_Object((1,3,6,1,2,1,16,30,1,6))
if mibBuilder.loadTexts:tpmMetricDefTable.setStatus(_A)
_TpmMetricDefEntry_Object=MibTableRow
tpmMetricDefEntry=_TpmMetricDefEntry_Object((1,3,6,1,2,1,16,30,1,6,1))
tpmMetricDefEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:tpmMetricDefEntry.setStatus(_A)
_TpmMetricDefinitionID_Type=TpmMetricDefID
_TpmMetricDefinitionID_Object=MibTableColumn
tpmMetricDefinitionID=_TpmMetricDefinitionID_Object((1,3,6,1,2,1,16,30,1,6,1,1),_TpmMetricDefinitionID_Type())
tpmMetricDefinitionID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmMetricDefinitionID.setStatus(_A)
class _TpmMetricDefType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('connectMetric',2),('delayMetric',3),('lossMetric',4)))
_TpmMetricDefType_Type.__name__=_H
_TpmMetricDefType_Object=MibTableColumn
tpmMetricDefType=_TpmMetricDefType_Object((1,3,6,1,2,1,16,30,1,6,1,2),_TpmMetricDefType_Type())
tpmMetricDefType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmMetricDefType.setStatus(_A)
class _TpmMetricDefDirType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oneWay',1),('twoWay',2),('multiWay',3)))
_TpmMetricDefDirType_Type.__name__=_H
_TpmMetricDefDirType_Object=MibTableColumn
tpmMetricDefDirType=_TpmMetricDefDirType_Object((1,3,6,1,2,1,16,30,1,6,1,3),_TpmMetricDefDirType_Type())
tpmMetricDefDirType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmMetricDefDirType.setStatus(_A)
_TpmMetricDefName_Type=SnmpAdminString
_TpmMetricDefName_Object=MibTableColumn
tpmMetricDefName=_TpmMetricDefName_Object((1,3,6,1,2,1,16,30,1,6,1,4),_TpmMetricDefName_Type())
tpmMetricDefName.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmMetricDefName.setStatus(_A)
_TpmMetricDefReference_Type=SnmpAdminString
_TpmMetricDefReference_Object=MibTableColumn
tpmMetricDefReference=_TpmMetricDefReference_Object((1,3,6,1,2,1,16,30,1,6,1,5),_TpmMetricDefReference_Type())
tpmMetricDefReference.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmMetricDefReference.setStatus(_A)
_TpmMetricDefGlobalID_Type=ObjectIdentifier
_TpmMetricDefGlobalID_Object=MibTableColumn
tpmMetricDefGlobalID=_TpmMetricDefGlobalID_Object((1,3,6,1,2,1,16,30,1,6,1,6),_TpmMetricDefGlobalID_Type())
tpmMetricDefGlobalID.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmMetricDefGlobalID.setStatus(_A)
_TpmReports_ObjectIdentity=ObjectIdentity
tpmReports=_TpmReports_ObjectIdentity((1,3,6,1,2,1,16,30,2))
_TpmAggrReportCntrlTable_Object=MibTable
tpmAggrReportCntrlTable=_TpmAggrReportCntrlTable_Object((1,3,6,1,2,1,16,30,2,1))
if mibBuilder.loadTexts:tpmAggrReportCntrlTable.setStatus(_A)
_TpmAggrReportCntrlEntry_Object=MibTableRow
tpmAggrReportCntrlEntry=_TpmAggrReportCntrlEntry_Object((1,3,6,1,2,1,16,30,2,1,1))
tpmAggrReportCntrlEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:tpmAggrReportCntrlEntry.setStatus(_A)
class _TpmAggrReportCntrlIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpmAggrReportCntrlIndex_Type.__name__=_E
_TpmAggrReportCntrlIndex_Object=MibTableColumn
tpmAggrReportCntrlIndex=_TpmAggrReportCntrlIndex_Object((1,3,6,1,2,1,16,30,2,1,1,1),_TpmAggrReportCntrlIndex_Type())
tpmAggrReportCntrlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportCntrlIndex.setStatus(_A)
class _TpmAggrReportCntrlApmCntrlIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpmAggrReportCntrlApmCntrlIndex_Type.__name__=_E
_TpmAggrReportCntrlApmCntrlIndex_Object=MibTableColumn
tpmAggrReportCntrlApmCntrlIndex=_TpmAggrReportCntrlApmCntrlIndex_Object((1,3,6,1,2,1,16,30,2,1,1,2),_TpmAggrReportCntrlApmCntrlIndex_Type())
tpmAggrReportCntrlApmCntrlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlApmCntrlIndex.setStatus(_A)
_TpmAggrReportCntrlDataSource_Type=DataSourceOrZero
_TpmAggrReportCntrlDataSource_Object=MibTableColumn
tpmAggrReportCntrlDataSource=_TpmAggrReportCntrlDataSource_Object((1,3,6,1,2,1,16,30,2,1,1,3),_TpmAggrReportCntrlDataSource_Type())
tpmAggrReportCntrlDataSource.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlDataSource.setStatus(_A)
_TpmAggrReportCntrlAggrType_Type=TransactionAggregationType
_TpmAggrReportCntrlAggrType_Object=MibTableColumn
tpmAggrReportCntrlAggrType=_TpmAggrReportCntrlAggrType_Object((1,3,6,1,2,1,16,30,2,1,1,4),_TpmAggrReportCntrlAggrType_Type())
tpmAggrReportCntrlAggrType.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlAggrType.setStatus(_A)
class _TpmAggrReportCntrlInterval_Type(Unsigned32):defaultValue=3600
_TpmAggrReportCntrlInterval_Type.__name__=_E
_TpmAggrReportCntrlInterval_Object=MibTableColumn
tpmAggrReportCntrlInterval=_TpmAggrReportCntrlInterval_Object((1,3,6,1,2,1,16,30,2,1,1,5),_TpmAggrReportCntrlInterval_Type())
tpmAggrReportCntrlInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlInterval.setStatus(_A)
if mibBuilder.loadTexts:tpmAggrReportCntrlInterval.setUnits('Seconds')
_TpmAggrReportCntrlReqSize_Type=Unsigned32
_TpmAggrReportCntrlReqSize_Object=MibTableColumn
tpmAggrReportCntrlReqSize=_TpmAggrReportCntrlReqSize_Object((1,3,6,1,2,1,16,30,2,1,1,6),_TpmAggrReportCntrlReqSize_Type())
tpmAggrReportCntrlReqSize.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlReqSize.setStatus(_A)
_TpmAggrReportCntrlGrantedSize_Type=Unsigned32
_TpmAggrReportCntrlGrantedSize_Object=MibTableColumn
tpmAggrReportCntrlGrantedSize=_TpmAggrReportCntrlGrantedSize_Object((1,3,6,1,2,1,16,30,2,1,1,7),_TpmAggrReportCntrlGrantedSize_Type())
tpmAggrReportCntrlGrantedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlGrantedSize.setStatus(_A)
class _TpmAggrReportCntrlReqReports_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TpmAggrReportCntrlReqReports_Type.__name__=_E
_TpmAggrReportCntrlReqReports_Object=MibTableColumn
tpmAggrReportCntrlReqReports=_TpmAggrReportCntrlReqReports_Object((1,3,6,1,2,1,16,30,2,1,1,8),_TpmAggrReportCntrlReqReports_Type())
tpmAggrReportCntrlReqReports.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlReqReports.setStatus(_A)
class _TpmAggrReportCntrlGrantedReports_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpmAggrReportCntrlGrantedReports_Type.__name__=_E
_TpmAggrReportCntrlGrantedReports_Object=MibTableColumn
tpmAggrReportCntrlGrantedReports=_TpmAggrReportCntrlGrantedReports_Object((1,3,6,1,2,1,16,30,2,1,1,9),_TpmAggrReportCntrlGrantedReports_Type())
tpmAggrReportCntrlGrantedReports.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlGrantedReports.setStatus(_A)
_TpmAggrReportCntrlStartTime_Type=TimeStamp
_TpmAggrReportCntrlStartTime_Object=MibTableColumn
tpmAggrReportCntrlStartTime=_TpmAggrReportCntrlStartTime_Object((1,3,6,1,2,1,16,30,2,1,1,10),_TpmAggrReportCntrlStartTime_Type())
tpmAggrReportCntrlStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlStartTime.setStatus(_A)
_TpmAggrReportCntrlReportNumber_Type=Unsigned32
_TpmAggrReportCntrlReportNumber_Object=MibTableColumn
tpmAggrReportCntrlReportNumber=_TpmAggrReportCntrlReportNumber_Object((1,3,6,1,2,1,16,30,2,1,1,11),_TpmAggrReportCntrlReportNumber_Type())
tpmAggrReportCntrlReportNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlReportNumber.setStatus(_A)
_TpmAggrReportCntrlInsertsDenied_Type=Counter32
_TpmAggrReportCntrlInsertsDenied_Object=MibTableColumn
tpmAggrReportCntrlInsertsDenied=_TpmAggrReportCntrlInsertsDenied_Object((1,3,6,1,2,1,16,30,2,1,1,12),_TpmAggrReportCntrlInsertsDenied_Type())
tpmAggrReportCntrlInsertsDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlInsertsDenied.setStatus(_A)
_TpmAggrReportCntrlDroppedFrames_Type=Counter32
_TpmAggrReportCntrlDroppedFrames_Object=MibTableColumn
tpmAggrReportCntrlDroppedFrames=_TpmAggrReportCntrlDroppedFrames_Object((1,3,6,1,2,1,16,30,2,1,1,13),_TpmAggrReportCntrlDroppedFrames_Type())
tpmAggrReportCntrlDroppedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportCntrlDroppedFrames.setStatus(_A)
_TpmAggrReportCntrlOwner_Type=OwnerString
_TpmAggrReportCntrlOwner_Object=MibTableColumn
tpmAggrReportCntrlOwner=_TpmAggrReportCntrlOwner_Object((1,3,6,1,2,1,16,30,2,1,1,14),_TpmAggrReportCntrlOwner_Type())
tpmAggrReportCntrlOwner.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlOwner.setStatus(_A)
_TpmAggrReportCntrlStorageType_Type=StorageType
_TpmAggrReportCntrlStorageType_Object=MibTableColumn
tpmAggrReportCntrlStorageType=_TpmAggrReportCntrlStorageType_Object((1,3,6,1,2,1,16,30,2,1,1,15),_TpmAggrReportCntrlStorageType_Type())
tpmAggrReportCntrlStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlStorageType.setStatus(_A)
_TpmAggrReportCntrlStatus_Type=RowStatus
_TpmAggrReportCntrlStatus_Object=MibTableColumn
tpmAggrReportCntrlStatus=_TpmAggrReportCntrlStatus_Object((1,3,6,1,2,1,16,30,2,1,1,16),_TpmAggrReportCntrlStatus_Type())
tpmAggrReportCntrlStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tpmAggrReportCntrlStatus.setStatus(_A)
_TpmAggrReportTable_Object=MibTable
tpmAggrReportTable=_TpmAggrReportTable_Object((1,3,6,1,2,1,16,30,2,2))
if mibBuilder.loadTexts:tpmAggrReportTable.setStatus(_A)
_TpmAggrReportEntry_Object=MibTableRow
tpmAggrReportEntry=_TpmAggrReportEntry_Object((1,3,6,1,2,1,16,30,2,2,1))
tpmAggrReportEntry.setIndexNames((0,_B,_I),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_M,_N),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:tpmAggrReportEntry.setStatus(_A)
class _TpmAggrReportIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TpmAggrReportIndex_Type.__name__=_E
_TpmAggrReportIndex_Object=MibTableColumn
tpmAggrReportIndex=_TpmAggrReportIndex_Object((1,3,6,1,2,1,16,30,2,2,1,1),_TpmAggrReportIndex_Type())
tpmAggrReportIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportIndex.setStatus(_A)
_TpmAggrReportAppLocalIndex_Type=AppLocalIndex
_TpmAggrReportAppLocalIndex_Object=MibTableColumn
tpmAggrReportAppLocalIndex=_TpmAggrReportAppLocalIndex_Object((1,3,6,1,2,1,16,30,2,2,1,2),_TpmAggrReportAppLocalIndex_Type())
tpmAggrReportAppLocalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportAppLocalIndex.setStatus(_A)
_TpmAggrReportTransMetricIndex_Type=TpmTransactionMetricIndex
_TpmAggrReportTransMetricIndex_Object=MibTableColumn
tpmAggrReportTransMetricIndex=_TpmAggrReportTransMetricIndex_Object((1,3,6,1,2,1,16,30,2,2,1,3),_TpmAggrReportTransMetricIndex_Type())
tpmAggrReportTransMetricIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportTransMetricIndex.setStatus(_A)
class _TpmAggrReportServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,108))
_TpmAggrReportServerAddress_Type.__name__=_L
_TpmAggrReportServerAddress_Object=MibTableColumn
tpmAggrReportServerAddress=_TpmAggrReportServerAddress_Object((1,3,6,1,2,1,16,30,2,2,1,4),_TpmAggrReportServerAddress_Type())
tpmAggrReportServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportServerAddress.setStatus(_A)
_TpmAggrReportApmNameClientID_Type=RmonClientID
_TpmAggrReportApmNameClientID_Object=MibTableColumn
tpmAggrReportApmNameClientID=_TpmAggrReportApmNameClientID_Object((1,3,6,1,2,1,16,30,2,2,1,5),_TpmAggrReportApmNameClientID_Type())
tpmAggrReportApmNameClientID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmAggrReportApmNameClientID.setStatus(_A)
_TpmAggrReportStatN_Type=ZeroBasedCounter32
_TpmAggrReportStatN_Object=MibTableColumn
tpmAggrReportStatN=_TpmAggrReportStatN_Object((1,3,6,1,2,1,16,30,2,2,1,6),_TpmAggrReportStatN_Type())
tpmAggrReportStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatN.setStatus(_A)
_TpmAggrReportOverflowStatN_Type=ZeroBasedCounter32
_TpmAggrReportOverflowStatN_Object=MibTableColumn
tpmAggrReportOverflowStatN=_TpmAggrReportOverflowStatN_Object((1,3,6,1,2,1,16,30,2,2,1,7),_TpmAggrReportOverflowStatN_Type())
tpmAggrReportOverflowStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportOverflowStatN.setStatus(_A)
_TpmAggrReportHCStatN_Type=ZeroBasedCounter64
_TpmAggrReportHCStatN_Object=MibTableColumn
tpmAggrReportHCStatN=_TpmAggrReportHCStatN_Object((1,3,6,1,2,1,16,30,2,2,1,8),_TpmAggrReportHCStatN_Type())
tpmAggrReportHCStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportHCStatN.setStatus(_A)
_TpmAggrReportStatSumX_Type=ZeroBasedCounter32
_TpmAggrReportStatSumX_Object=MibTableColumn
tpmAggrReportStatSumX=_TpmAggrReportStatSumX_Object((1,3,6,1,2,1,16,30,2,2,1,9),_TpmAggrReportStatSumX_Type())
tpmAggrReportStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatSumX.setStatus(_A)
_TpmAggrReportOverflowStatSumX_Type=ZeroBasedCounter32
_TpmAggrReportOverflowStatSumX_Object=MibTableColumn
tpmAggrReportOverflowStatSumX=_TpmAggrReportOverflowStatSumX_Object((1,3,6,1,2,1,16,30,2,2,1,10),_TpmAggrReportOverflowStatSumX_Type())
tpmAggrReportOverflowStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportOverflowStatSumX.setStatus(_A)
_TpmAggrReportHCStatSumX_Type=ZeroBasedCounter64
_TpmAggrReportHCStatSumX_Object=MibTableColumn
tpmAggrReportHCStatSumX=_TpmAggrReportHCStatSumX_Object((1,3,6,1,2,1,16,30,2,2,1,11),_TpmAggrReportHCStatSumX_Type())
tpmAggrReportHCStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportHCStatSumX.setStatus(_A)
_TpmAggrReportStatMaximum_Type=ZeroBasedCounter32
_TpmAggrReportStatMaximum_Object=MibTableColumn
tpmAggrReportStatMaximum=_TpmAggrReportStatMaximum_Object((1,3,6,1,2,1,16,30,2,2,1,12),_TpmAggrReportStatMaximum_Type())
tpmAggrReportStatMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatMaximum.setStatus(_A)
_TpmAggrReportStatMinimum_Type=ZeroBasedCounter32
_TpmAggrReportStatMinimum_Object=MibTableColumn
tpmAggrReportStatMinimum=_TpmAggrReportStatMinimum_Object((1,3,6,1,2,1,16,30,2,2,1,13),_TpmAggrReportStatMinimum_Type())
tpmAggrReportStatMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatMinimum.setStatus(_A)
_TpmAggrReportStatSumSq_Type=ZeroBasedCounter32
_TpmAggrReportStatSumSq_Object=MibTableColumn
tpmAggrReportStatSumSq=_TpmAggrReportStatSumSq_Object((1,3,6,1,2,1,16,30,2,2,1,14),_TpmAggrReportStatSumSq_Type())
tpmAggrReportStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatSumSq.setStatus(_A)
_TpmAggrReportOverflowStatSumSq_Type=ZeroBasedCounter32
_TpmAggrReportOverflowStatSumSq_Object=MibTableColumn
tpmAggrReportOverflowStatSumSq=_TpmAggrReportOverflowStatSumSq_Object((1,3,6,1,2,1,16,30,2,2,1,15),_TpmAggrReportOverflowStatSumSq_Type())
tpmAggrReportOverflowStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportOverflowStatSumSq.setStatus(_A)
_TpmAggrReportHCStatSumSq_Type=ZeroBasedCounter64
_TpmAggrReportHCStatSumSq_Object=MibTableColumn
tpmAggrReportHCStatSumSq=_TpmAggrReportHCStatSumSq_Object((1,3,6,1,2,1,16,30,2,2,1,16),_TpmAggrReportHCStatSumSq_Type())
tpmAggrReportHCStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportHCStatSumSq.setStatus(_A)
_TpmAggrReportStatSumIX_Type=ZeroBasedCounter32
_TpmAggrReportStatSumIX_Object=MibTableColumn
tpmAggrReportStatSumIX=_TpmAggrReportStatSumIX_Object((1,3,6,1,2,1,16,30,2,2,1,17),_TpmAggrReportStatSumIX_Type())
tpmAggrReportStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatSumIX.setStatus(_A)
_TpmAggrReportOverflowStatSumIX_Type=ZeroBasedCounter32
_TpmAggrReportOverflowStatSumIX_Object=MibTableColumn
tpmAggrReportOverflowStatSumIX=_TpmAggrReportOverflowStatSumIX_Object((1,3,6,1,2,1,16,30,2,2,1,18),_TpmAggrReportOverflowStatSumIX_Type())
tpmAggrReportOverflowStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportOverflowStatSumIX.setStatus(_A)
_TpmAggrReportHCStatSumIX_Type=ZeroBasedCounter64
_TpmAggrReportHCStatSumIX_Object=MibTableColumn
tpmAggrReportHCStatSumIX=_TpmAggrReportHCStatSumIX_Object((1,3,6,1,2,1,16,30,2,2,1,19),_TpmAggrReportHCStatSumIX_Type())
tpmAggrReportHCStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportHCStatSumIX.setStatus(_A)
_TpmAggrReportStatSumIXSq_Type=ZeroBasedCounter32
_TpmAggrReportStatSumIXSq_Object=MibTableColumn
tpmAggrReportStatSumIXSq=_TpmAggrReportStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,2,1,20),_TpmAggrReportStatSumIXSq_Type())
tpmAggrReportStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportStatSumIXSq.setStatus(_A)
_TpmAggrReportOverflowStatSumIXSq_Type=ZeroBasedCounter32
_TpmAggrReportOverflowStatSumIXSq_Object=MibTableColumn
tpmAggrReportOverflowStatSumIXSq=_TpmAggrReportOverflowStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,2,1,21),_TpmAggrReportOverflowStatSumIXSq_Type())
tpmAggrReportOverflowStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportOverflowStatSumIXSq.setStatus(_A)
_TpmAggrReportHCStatSumIXSq_Type=ZeroBasedCounter64
_TpmAggrReportHCStatSumIXSq_Object=MibTableColumn
tpmAggrReportHCStatSumIXSq=_TpmAggrReportHCStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,2,1,22),_TpmAggrReportHCStatSumIXSq_Type())
tpmAggrReportHCStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmAggrReportHCStatSumIXSq.setStatus(_A)
_TpmCurReportTable_Object=MibTable
tpmCurReportTable=_TpmCurReportTable_Object((1,3,6,1,2,1,16,30,2,3))
if mibBuilder.loadTexts:tpmCurReportTable.setStatus(_A)
_TpmCurReportEntry_Object=MibTableRow
tpmCurReportEntry=_TpmCurReportEntry_Object((1,3,6,1,2,1,16,30,2,3,1))
tpmCurReportEntry.setIndexNames((0,_B,_I),(0,_B,_e),(0,_B,_f),(0,_M,_N),(0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:tpmCurReportEntry.setStatus(_A)
_TpmCurReportAppLocalIndex_Type=AppLocalIndex
_TpmCurReportAppLocalIndex_Object=MibTableColumn
tpmCurReportAppLocalIndex=_TpmCurReportAppLocalIndex_Object((1,3,6,1,2,1,16,30,2,3,1,1),_TpmCurReportAppLocalIndex_Type())
tpmCurReportAppLocalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmCurReportAppLocalIndex.setStatus(_A)
_TpmCurReportTransMetricIndex_Type=TpmTransactionMetricIndex
_TpmCurReportTransMetricIndex_Object=MibTableColumn
tpmCurReportTransMetricIndex=_TpmCurReportTransMetricIndex_Object((1,3,6,1,2,1,16,30,2,3,1,2),_TpmCurReportTransMetricIndex_Type())
tpmCurReportTransMetricIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmCurReportTransMetricIndex.setStatus(_A)
class _TpmCurReportServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,108))
_TpmCurReportServerAddress_Type.__name__=_L
_TpmCurReportServerAddress_Object=MibTableColumn
tpmCurReportServerAddress=_TpmCurReportServerAddress_Object((1,3,6,1,2,1,16,30,2,3,1,3),_TpmCurReportServerAddress_Type())
tpmCurReportServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmCurReportServerAddress.setStatus(_A)
_TpmCurReportApmNameClientID_Type=RmonClientID
_TpmCurReportApmNameClientID_Object=MibTableColumn
tpmCurReportApmNameClientID=_TpmCurReportApmNameClientID_Object((1,3,6,1,2,1,16,30,2,3,1,4),_TpmCurReportApmNameClientID_Type())
tpmCurReportApmNameClientID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmCurReportApmNameClientID.setStatus(_A)
class _TpmCurReportApmTransactionID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TpmCurReportApmTransactionID_Type.__name__=_E
_TpmCurReportApmTransactionID_Object=MibTableColumn
tpmCurReportApmTransactionID=_TpmCurReportApmTransactionID_Object((1,3,6,1,2,1,16,30,2,3,1,5),_TpmCurReportApmTransactionID_Type())
tpmCurReportApmTransactionID.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmCurReportApmTransactionID.setStatus(_A)
_TpmCurReportMetricValue_Type=ZeroBasedCounter32
_TpmCurReportMetricValue_Object=MibTableColumn
tpmCurReportMetricValue=_TpmCurReportMetricValue_Object((1,3,6,1,2,1,16,30,2,3,1,6),_TpmCurReportMetricValue_Type())
tpmCurReportMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmCurReportMetricValue.setStatus(_A)
class _TpmCurReportCompletion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A,1),('completed',2)))
_TpmCurReportCompletion_Type.__name__=_H
_TpmCurReportCompletion_Object=MibTableColumn
tpmCurReportCompletion=_TpmCurReportCompletion_Object((1,3,6,1,2,1,16,30,2,3,1,7),_TpmCurReportCompletion_Type())
tpmCurReportCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmCurReportCompletion.setStatus(_A)
_TpmCurReportSize_Type=Unsigned32
_TpmCurReportSize_Object=MibScalar
tpmCurReportSize=_TpmCurReportSize_Object((1,3,6,1,2,1,16,30,2,4),_TpmCurReportSize_Type())
tpmCurReportSize.setMaxAccess(_X)
if mibBuilder.loadTexts:tpmCurReportSize.setStatus(_A)
_TpmExcpReportTable_Object=MibTable
tpmExcpReportTable=_TpmExcpReportTable_Object((1,3,6,1,2,1,16,30,2,5))
if mibBuilder.loadTexts:tpmExcpReportTable.setStatus(_A)
_TpmExcpReportEntry_Object=MibTableRow
tpmExcpReportEntry=_TpmExcpReportEntry_Object((1,3,6,1,2,1,16,30,2,5,1))
tpmExcpReportEntry.setIndexNames((0,_G,_Q),(0,_G,_R),(0,_G,_T),(0,_B,_j))
if mibBuilder.loadTexts:tpmExcpReportEntry.setStatus(_A)
_TpmExcpReportTransMetricIndex_Type=TpmTransactionMetricIndex
_TpmExcpReportTransMetricIndex_Object=MibTableColumn
tpmExcpReportTransMetricIndex=_TpmExcpReportTransMetricIndex_Object((1,3,6,1,2,1,16,30,2,5,1,1),_TpmExcpReportTransMetricIndex_Type())
tpmExcpReportTransMetricIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpmExcpReportTransMetricIndex.setStatus(_A)
_TpmExcpReportStatN_Type=ZeroBasedCounter32
_TpmExcpReportStatN_Object=MibTableColumn
tpmExcpReportStatN=_TpmExcpReportStatN_Object((1,3,6,1,2,1,16,30,2,5,1,2),_TpmExcpReportStatN_Type())
tpmExcpReportStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatN.setStatus(_A)
_TpmExcpReportOverflowStatN_Type=ZeroBasedCounter32
_TpmExcpReportOverflowStatN_Object=MibTableColumn
tpmExcpReportOverflowStatN=_TpmExcpReportOverflowStatN_Object((1,3,6,1,2,1,16,30,2,5,1,3),_TpmExcpReportOverflowStatN_Type())
tpmExcpReportOverflowStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportOverflowStatN.setStatus(_A)
_TpmExcpReportHCStatN_Type=ZeroBasedCounter64
_TpmExcpReportHCStatN_Object=MibTableColumn
tpmExcpReportHCStatN=_TpmExcpReportHCStatN_Object((1,3,6,1,2,1,16,30,2,5,1,4),_TpmExcpReportHCStatN_Type())
tpmExcpReportHCStatN.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportHCStatN.setStatus(_A)
_TpmExcpReportStatSumX_Type=ZeroBasedCounter32
_TpmExcpReportStatSumX_Object=MibTableColumn
tpmExcpReportStatSumX=_TpmExcpReportStatSumX_Object((1,3,6,1,2,1,16,30,2,5,1,5),_TpmExcpReportStatSumX_Type())
tpmExcpReportStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatSumX.setStatus(_A)
_TpmExcpReportOverflowStatSumX_Type=ZeroBasedCounter32
_TpmExcpReportOverflowStatSumX_Object=MibTableColumn
tpmExcpReportOverflowStatSumX=_TpmExcpReportOverflowStatSumX_Object((1,3,6,1,2,1,16,30,2,5,1,6),_TpmExcpReportOverflowStatSumX_Type())
tpmExcpReportOverflowStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportOverflowStatSumX.setStatus(_A)
_TpmExcpReportHCStatSumX_Type=ZeroBasedCounter64
_TpmExcpReportHCStatSumX_Object=MibTableColumn
tpmExcpReportHCStatSumX=_TpmExcpReportHCStatSumX_Object((1,3,6,1,2,1,16,30,2,5,1,7),_TpmExcpReportHCStatSumX_Type())
tpmExcpReportHCStatSumX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportHCStatSumX.setStatus(_A)
_TpmExcpReportStatMaximum_Type=ZeroBasedCounter32
_TpmExcpReportStatMaximum_Object=MibTableColumn
tpmExcpReportStatMaximum=_TpmExcpReportStatMaximum_Object((1,3,6,1,2,1,16,30,2,5,1,8),_TpmExcpReportStatMaximum_Type())
tpmExcpReportStatMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatMaximum.setStatus(_A)
_TpmExcpReportStatMinimum_Type=ZeroBasedCounter32
_TpmExcpReportStatMinimum_Object=MibTableColumn
tpmExcpReportStatMinimum=_TpmExcpReportStatMinimum_Object((1,3,6,1,2,1,16,30,2,5,1,9),_TpmExcpReportStatMinimum_Type())
tpmExcpReportStatMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatMinimum.setStatus(_A)
_TpmExcpReportStatSumSq_Type=ZeroBasedCounter32
_TpmExcpReportStatSumSq_Object=MibTableColumn
tpmExcpReportStatSumSq=_TpmExcpReportStatSumSq_Object((1,3,6,1,2,1,16,30,2,5,1,10),_TpmExcpReportStatSumSq_Type())
tpmExcpReportStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatSumSq.setStatus(_A)
_TpmExcpReportOverflowStatSumSq_Type=ZeroBasedCounter32
_TpmExcpReportOverflowStatSumSq_Object=MibTableColumn
tpmExcpReportOverflowStatSumSq=_TpmExcpReportOverflowStatSumSq_Object((1,3,6,1,2,1,16,30,2,5,1,11),_TpmExcpReportOverflowStatSumSq_Type())
tpmExcpReportOverflowStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportOverflowStatSumSq.setStatus(_A)
_TpmExcpReportHCStatSumSq_Type=ZeroBasedCounter64
_TpmExcpReportHCStatSumSq_Object=MibTableColumn
tpmExcpReportHCStatSumSq=_TpmExcpReportHCStatSumSq_Object((1,3,6,1,2,1,16,30,2,5,1,12),_TpmExcpReportHCStatSumSq_Type())
tpmExcpReportHCStatSumSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportHCStatSumSq.setStatus(_A)
_TpmExcpReportStatSumIX_Type=ZeroBasedCounter32
_TpmExcpReportStatSumIX_Object=MibTableColumn
tpmExcpReportStatSumIX=_TpmExcpReportStatSumIX_Object((1,3,6,1,2,1,16,30,2,5,1,13),_TpmExcpReportStatSumIX_Type())
tpmExcpReportStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatSumIX.setStatus(_A)
_TpmExcpReportOverflowStatSumIX_Type=ZeroBasedCounter32
_TpmExcpReportOverflowStatSumIX_Object=MibTableColumn
tpmExcpReportOverflowStatSumIX=_TpmExcpReportOverflowStatSumIX_Object((1,3,6,1,2,1,16,30,2,5,1,14),_TpmExcpReportOverflowStatSumIX_Type())
tpmExcpReportOverflowStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportOverflowStatSumIX.setStatus(_A)
_TpmExcpReportHCStatSumIX_Type=ZeroBasedCounter64
_TpmExcpReportHCStatSumIX_Object=MibTableColumn
tpmExcpReportHCStatSumIX=_TpmExcpReportHCStatSumIX_Object((1,3,6,1,2,1,16,30,2,5,1,15),_TpmExcpReportHCStatSumIX_Type())
tpmExcpReportHCStatSumIX.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportHCStatSumIX.setStatus(_A)
_TpmExcpReportStatSumIXSq_Type=ZeroBasedCounter32
_TpmExcpReportStatSumIXSq_Object=MibTableColumn
tpmExcpReportStatSumIXSq=_TpmExcpReportStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,5,1,16),_TpmExcpReportStatSumIXSq_Type())
tpmExcpReportStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportStatSumIXSq.setStatus(_A)
_TpmExcpReportOverflowStatSumIXSq_Type=ZeroBasedCounter32
_TpmExcpReportOverflowStatSumIXSq_Object=MibTableColumn
tpmExcpReportOverflowStatSumIXSq=_TpmExcpReportOverflowStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,5,1,17),_TpmExcpReportOverflowStatSumIXSq_Type())
tpmExcpReportOverflowStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportOverflowStatSumIXSq.setStatus(_A)
_TpmExcpReportHCStatSumIXSq_Type=ZeroBasedCounter64
_TpmExcpReportHCStatSumIXSq_Object=MibTableColumn
tpmExcpReportHCStatSumIXSq=_TpmExcpReportHCStatSumIXSq_Object((1,3,6,1,2,1,16,30,2,5,1,18),_TpmExcpReportHCStatSumIXSq_Type())
tpmExcpReportHCStatSumIXSq.setMaxAccess(_C)
if mibBuilder.loadTexts:tpmExcpReportHCStatSumIXSq.setStatus(_A)
_TpmConformance_ObjectIdentity=ObjectIdentity
tpmConformance=_TpmConformance_ObjectIdentity((1,3,6,1,2,1,16,30,3))
_TpmMIBCompliances_ObjectIdentity=ObjectIdentity
tpmMIBCompliances=_TpmMIBCompliances_ObjectIdentity((1,3,6,1,2,1,16,30,3,1))
_TpmGroups_ObjectIdentity=ObjectIdentity
tpmGroups=_TpmGroups_ObjectIdentity((1,3,6,1,2,1,16,30,3,2))
tpmCapabilitiesGroup=ObjectGroup((1,3,6,1,2,1,16,30,3,2,1))
tpmCapabilitiesGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:tpmCapabilitiesGroup.setStatus(_A)
tpmAggregateReportsGroup=ObjectGroup((1,3,6,1,2,1,16,30,3,2,2))
tpmAggregateReportsGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:tpmAggregateReportsGroup.setStatus(_A)
tpmCurrentReportsGroup=ObjectGroup((1,3,6,1,2,1,16,30,3,2,3))
tpmCurrentReportsGroup.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:tpmCurrentReportsGroup.setStatus(_A)
tpmExceptionReportsGroup=ObjectGroup((1,3,6,1,2,1,16,30,3,2,4))
tpmExceptionReportsGroup.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:tpmExceptionReportsGroup.setStatus(_A)
tpmMIBCompliance=ModuleCompliance((1,3,6,1,2,1,16,30,3,1,1))
tpmMIBCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:tpmMIBCompliance.setStatus(_A)
tpmCurrentReportsCompliance=ModuleCompliance((1,3,6,1,2,1,16,30,3,1,2))
tpmCurrentReportsCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_O)))
if mibBuilder.loadTexts:tpmCurrentReportsCompliance.setStatus(_A)
tpmExceptionReportsCompliance=ModuleCompliance((1,3,6,1,2,1,16,30,3,1,3))
tpmExceptionReportsCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_P),(_G,_U),(_G,_S)))
if mibBuilder.loadTexts:tpmExceptionReportsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TpmTransactionMetricIndex':TpmTransactionMetricIndex,'TpmMetricDefID':TpmMetricDefID,'tpmMIB':tpmMIB,'tpmCapabilities':tpmCapabilities,_k:tpmClockResolution,_l:tpmClockMaxSkew,_m:tpmClockSource,_n:tpmTransMetricDirLastChange,'tpmTransMetricDirTable':tpmTransMetricDirTable,'tpmTransMetricDirEntry':tpmTransMetricDirEntry,_V:tpmTransMetricAppLocalIndex,_W:tpmTransMetricIndex,_o:tpmTransMetricProtocolIndex,_p:tpmTransMetricMetricIndex,_q:tpmTransMetricDirConfig,'tpmMetricDefTable':tpmMetricDefTable,'tpmMetricDefEntry':tpmMetricDefEntry,_Y:tpmMetricDefinitionID,_r:tpmMetricDefType,_s:tpmMetricDefDirType,_t:tpmMetricDefName,_u:tpmMetricDefReference,_v:tpmMetricDefGlobalID,'tpmReports':tpmReports,'tpmAggrReportCntrlTable':tpmAggrReportCntrlTable,'tpmAggrReportCntrlEntry':tpmAggrReportCntrlEntry,_I:tpmAggrReportCntrlIndex,_w:tpmAggrReportCntrlApmCntrlIndex,_x:tpmAggrReportCntrlDataSource,_y:tpmAggrReportCntrlAggrType,_z:tpmAggrReportCntrlInterval,_A0:tpmAggrReportCntrlReqSize,_A1:tpmAggrReportCntrlGrantedSize,_A2:tpmAggrReportCntrlReqReports,_A3:tpmAggrReportCntrlGrantedReports,_A4:tpmAggrReportCntrlStartTime,_A5:tpmAggrReportCntrlReportNumber,_A6:tpmAggrReportCntrlInsertsDenied,_A7:tpmAggrReportCntrlDroppedFrames,_A8:tpmAggrReportCntrlOwner,_A9:tpmAggrReportCntrlStorageType,_AA:tpmAggrReportCntrlStatus,'tpmAggrReportTable':tpmAggrReportTable,'tpmAggrReportEntry':tpmAggrReportEntry,_Z:tpmAggrReportIndex,_a:tpmAggrReportAppLocalIndex,_b:tpmAggrReportTransMetricIndex,_c:tpmAggrReportServerAddress,_d:tpmAggrReportApmNameClientID,_AB:tpmAggrReportStatN,_AC:tpmAggrReportOverflowStatN,_AD:tpmAggrReportHCStatN,_AE:tpmAggrReportStatSumX,_AF:tpmAggrReportOverflowStatSumX,_AG:tpmAggrReportHCStatSumX,_AH:tpmAggrReportStatMaximum,_AI:tpmAggrReportStatMinimum,_AJ:tpmAggrReportStatSumSq,_AK:tpmAggrReportOverflowStatSumSq,_AL:tpmAggrReportHCStatSumSq,_AM:tpmAggrReportStatSumIX,_AN:tpmAggrReportOverflowStatSumIX,_AO:tpmAggrReportHCStatSumIX,_AP:tpmAggrReportStatSumIXSq,_AQ:tpmAggrReportOverflowStatSumIXSq,_AR:tpmAggrReportHCStatSumIXSq,'tpmCurReportTable':tpmCurReportTable,'tpmCurReportEntry':tpmCurReportEntry,_e:tpmCurReportAppLocalIndex,_f:tpmCurReportTransMetricIndex,_g:tpmCurReportServerAddress,_h:tpmCurReportApmNameClientID,_i:tpmCurReportApmTransactionID,_AS:tpmCurReportMetricValue,_AT:tpmCurReportCompletion,_AU:tpmCurReportSize,'tpmExcpReportTable':tpmExcpReportTable,'tpmExcpReportEntry':tpmExcpReportEntry,_j:tpmExcpReportTransMetricIndex,_AV:tpmExcpReportStatN,_AW:tpmExcpReportOverflowStatN,_AX:tpmExcpReportHCStatN,_AY:tpmExcpReportStatSumX,_AZ:tpmExcpReportOverflowStatSumX,_Aa:tpmExcpReportHCStatSumX,_Ab:tpmExcpReportStatMaximum,_Ac:tpmExcpReportStatMinimum,_Ad:tpmExcpReportStatSumSq,_Ae:tpmExcpReportOverflowStatSumSq,_Af:tpmExcpReportHCStatSumSq,_Ag:tpmExcpReportStatSumIX,_Ah:tpmExcpReportOverflowStatSumIX,_Ai:tpmExcpReportHCStatSumIX,_Aj:tpmExcpReportStatSumIXSq,_Ak:tpmExcpReportOverflowStatSumIXSq,_Al:tpmExcpReportHCStatSumIXSq,'tpmConformance':tpmConformance,'tpmMIBCompliances':tpmMIBCompliances,'tpmMIBCompliance':tpmMIBCompliance,'tpmCurrentReportsCompliance':tpmCurrentReportsCompliance,'tpmExceptionReportsCompliance':tpmExceptionReportsCompliance,'tpmGroups':tpmGroups,_J:tpmCapabilitiesGroup,_K:tpmAggregateReportsGroup,_O:tpmCurrentReportsGroup,_P:tpmExceptionReportsGroup})