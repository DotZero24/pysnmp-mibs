_S='wwpLeosMPLSOamLspTraceRouteHopIndex'
_R='success'
_Q='seconds'
_P='requests'
_O='OctetString'
_N='milliseconds'
_M='LspType'
_L='wwpLeosMPLSOamLspPingCtlIndex'
_K='unknown'
_J='DisplayString'
_I='wwpLeosMPLSOamLspTraceRouteCtlIndex'
_H='enabled'
_G='disabled'
_F='WWP-LEOS-MPLS-OAM-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosMPLSOamMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,36))
if mibBuilder.loadTexts:wwpLeosMPLSOamMIB.setRevisions(('2006-05-26 00:00',))
class OperationResponseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6)));namedValues=NamedValues(*(('responseReceived',1),(_K,2),('requestTimedOut',4),('unknownLsp',5),('maxConcurrentLimitReached',6)))
class LspPingReturnCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,8,9,10,11,12)));namedValues=NamedValues(*(('noReturnCode',0),('malformedEchoRequest',1),('oneOrMoreTlvsNotUnderstood',2),('egressForFec',3),('noMappingForFec',4),('downstreamMappingMismatch',5),('upstreamInterfaceIndexUnknown',6),('labelSwitchedFec',8),('labelSwitchedNoForwardingFec',9),('wrongLabel',10),('noLabel',11),('unknownFec',12)))
class LspType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('rsvpTeTunnel',1))
_WwpLeosMPLSOamObjects_ObjectIdentity=ObjectIdentity
wwpLeosMPLSOamObjects=_WwpLeosMPLSOamObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,36,1))
_WwpLeosMPLSOAMLspPingMax_Type=Unsigned32
_WwpLeosMPLSOAMLspPingMax_Object=MibScalar
wwpLeosMPLSOAMLspPingMax=_WwpLeosMPLSOAMLspPingMax_Object((1,3,6,1,4,1,6141,2,60,36,1,1),_WwpLeosMPLSOAMLspPingMax_Type())
wwpLeosMPLSOAMLspPingMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOAMLspPingMax.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOAMLspPingMax.setUnits(_P)
_WwpLeosMPLSOAMLspTraceRtMax_Type=Unsigned32
_WwpLeosMPLSOAMLspTraceRtMax_Object=MibScalar
wwpLeosMPLSOAMLspTraceRtMax=_WwpLeosMPLSOAMLspTraceRtMax_Object((1,3,6,1,4,1,6141,2,60,36,1,2),_WwpLeosMPLSOAMLspTraceRtMax_Type())
wwpLeosMPLSOAMLspTraceRtMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOAMLspTraceRtMax.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOAMLspTraceRtMax.setUnits(_P)
_WwpLeosMPLSOamLspPingCtlTable_Object=MibTable
wwpLeosMPLSOamLspPingCtlTable=_WwpLeosMPLSOamLspPingCtlTable_Object((1,3,6,1,4,1,6141,2,60,36,1,3))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlTable.setStatus(_A)
_WwpLeosMPLSOamLspPingCtlEntry_Object=MibTableRow
wwpLeosMPLSOamLspPingCtlEntry=_WwpLeosMPLSOamLspPingCtlEntry_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1))
wwpLeosMPLSOamLspPingCtlEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlEntry.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_WwpLeosMPLSOamLspPingCtlIndex_Type.__name__=_D
_WwpLeosMPLSOamLspPingCtlIndex_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlIndex=_WwpLeosMPLSOamLspPingCtlIndex_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,1),_WwpLeosMPLSOamLspPingCtlIndex_Type())
wwpLeosMPLSOamLspPingCtlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlIndex.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlLspType_Type(LspType):defaultValue=1
_WwpLeosMPLSOamLspPingCtlLspType_Type.__name__=_M
_WwpLeosMPLSOamLspPingCtlLspType_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlLspType=_WwpLeosMPLSOamLspPingCtlLspType_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,3),_WwpLeosMPLSOamLspPingCtlLspType_Type())
wwpLeosMPLSOamLspPingCtlLspType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlLspType.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlLspName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosMPLSOamLspPingCtlLspName_Type.__name__=_J
_WwpLeosMPLSOamLspPingCtlLspName_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlLspName=_WwpLeosMPLSOamLspPingCtlLspName_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,4),_WwpLeosMPLSOamLspPingCtlLspName_Type())
wwpLeosMPLSOamLspPingCtlLspName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlLspName.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlPktSize_Type(Unsigned32):defaultValue=96;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,1464))
_WwpLeosMPLSOamLspPingCtlPktSize_Type.__name__=_E
_WwpLeosMPLSOamLspPingCtlPktSize_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlPktSize=_WwpLeosMPLSOamLspPingCtlPktSize_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,5),_WwpLeosMPLSOamLspPingCtlPktSize_Type())
wwpLeosMPLSOamLspPingCtlPktSize.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlPktSize.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlTimeOut_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_WwpLeosMPLSOamLspPingCtlTimeOut_Type.__name__=_E
_WwpLeosMPLSOamLspPingCtlTimeOut_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlTimeOut=_WwpLeosMPLSOamLspPingCtlTimeOut_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,6),_WwpLeosMPLSOamLspPingCtlTimeOut_Type())
wwpLeosMPLSOamLspPingCtlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlTimeOut.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlTimeOut.setUnits(_Q)
class _WwpLeosMPLSOamLspPingCtlCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosMPLSOamLspPingCtlCount_Type.__name__=_E
_WwpLeosMPLSOamLspPingCtlCount_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlCount=_WwpLeosMPLSOamLspPingCtlCount_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,7),_WwpLeosMPLSOamLspPingCtlCount_Type())
wwpLeosMPLSOamLspPingCtlCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlCount.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMPLSOamLspPingCtlAdminState_Type.__name__=_D
_WwpLeosMPLSOamLspPingCtlAdminState_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlAdminState=_WwpLeosMPLSOamLspPingCtlAdminState_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,8),_WwpLeosMPLSOamLspPingCtlAdminState_Type())
wwpLeosMPLSOamLspPingCtlAdminState.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlAdminState.setStatus(_A)
class _WwpLeosMPLSOamLspPingCtlTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpLeosMPLSOamLspPingCtlTtl_Type.__name__=_D
_WwpLeosMPLSOamLspPingCtlTtl_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlTtl=_WwpLeosMPLSOamLspPingCtlTtl_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,9),_WwpLeosMPLSOamLspPingCtlTtl_Type())
wwpLeosMPLSOamLspPingCtlTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlTtl.setStatus(_A)
_WwpLeosMPLSOamLspPingCtlRowStatus_Type=RowStatus
_WwpLeosMPLSOamLspPingCtlRowStatus_Object=MibTableColumn
wwpLeosMPLSOamLspPingCtlRowStatus=_WwpLeosMPLSOamLspPingCtlRowStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,3,1,10),_WwpLeosMPLSOamLspPingCtlRowStatus_Type())
wwpLeosMPLSOamLspPingCtlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingCtlRowStatus.setStatus(_A)
_WwpLeosMPLSOamLspPingResultsTable_Object=MibTable
wwpLeosMPLSOamLspPingResultsTable=_WwpLeosMPLSOamLspPingResultsTable_Object((1,3,6,1,4,1,6141,2,60,36,1,4))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsTable.setStatus(_A)
_WwpLeosMPLSOamLspPingResultsEntry_Object=MibTableRow
wwpLeosMPLSOamLspPingResultsEntry=_WwpLeosMPLSOamLspPingResultsEntry_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1))
wwpLeosMPLSOamLspPingResultsEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsEntry.setStatus(_A)
class _WwpLeosMPLSOamLspPingResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosMPLSOamLspPingResultsOperStatus_Type.__name__=_D
_WwpLeosMPLSOamLspPingResultsOperStatus_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsOperStatus=_WwpLeosMPLSOamLspPingResultsOperStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,1),_WwpLeosMPLSOamLspPingResultsOperStatus_Type())
wwpLeosMPLSOamLspPingResultsOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsOperStatus.setStatus(_A)
class _WwpLeosMPLSOamLspPingResultsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_R,2),('failed',3)))
_WwpLeosMPLSOamLspPingResultsStatus_Type.__name__=_D
_WwpLeosMPLSOamLspPingResultsStatus_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsStatus=_WwpLeosMPLSOamLspPingResultsStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,2),_WwpLeosMPLSOamLspPingResultsStatus_Type())
wwpLeosMPLSOamLspPingResultsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsStatus.setStatus(_A)
_WwpLeosMPLSOamLspPingResultsLspType_Type=LspType
_WwpLeosMPLSOamLspPingResultsLspType_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsLspType=_WwpLeosMPLSOamLspPingResultsLspType_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,3),_WwpLeosMPLSOamLspPingResultsLspType_Type())
wwpLeosMPLSOamLspPingResultsLspType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsLspType.setStatus(_A)
class _WwpLeosMPLSOamLspPingResultsLspName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosMPLSOamLspPingResultsLspName_Type.__name__=_O
_WwpLeosMPLSOamLspPingResultsLspName_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsLspName=_WwpLeosMPLSOamLspPingResultsLspName_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,4),_WwpLeosMPLSOamLspPingResultsLspName_Type())
wwpLeosMPLSOamLspPingResultsLspName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsLspName.setStatus(_A)
_WwpLeosMPLSOamLspPingResultsMinRtt_Type=Unsigned32
_WwpLeosMPLSOamLspPingResultsMinRtt_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsMinRtt=_WwpLeosMPLSOamLspPingResultsMinRtt_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,5),_WwpLeosMPLSOamLspPingResultsMinRtt_Type())
wwpLeosMPLSOamLspPingResultsMinRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsMinRtt.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsMinRtt.setUnits(_N)
_WwpLeosMPLSOamLspPingResultsMaxRtt_Type=Unsigned32
_WwpLeosMPLSOamLspPingResultsMaxRtt_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsMaxRtt=_WwpLeosMPLSOamLspPingResultsMaxRtt_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,6),_WwpLeosMPLSOamLspPingResultsMaxRtt_Type())
wwpLeosMPLSOamLspPingResultsMaxRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsMaxRtt.setUnits(_N)
_WwpLeosMPLSOamLspPingResultsAverageRtt_Type=Unsigned32
_WwpLeosMPLSOamLspPingResultsAverageRtt_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsAverageRtt=_WwpLeosMPLSOamLspPingResultsAverageRtt_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,7),_WwpLeosMPLSOamLspPingResultsAverageRtt_Type())
wwpLeosMPLSOamLspPingResultsAverageRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsAverageRtt.setUnits(_N)
_WwpLeosMPLSOamLspPingResultsProbesSent_Type=Unsigned32
_WwpLeosMPLSOamLspPingResultsProbesSent_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsProbesSent=_WwpLeosMPLSOamLspPingResultsProbesSent_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,8),_WwpLeosMPLSOamLspPingResultsProbesSent_Type())
wwpLeosMPLSOamLspPingResultsProbesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsProbesSent.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsProbesSent.setUnits('probes')
_WwpLeosMPLSOamLspPingResultsProbeResponses_Type=Unsigned32
_WwpLeosMPLSOamLspPingResultsProbeResponses_Object=MibTableColumn
wwpLeosMPLSOamLspPingResultsProbeResponses=_WwpLeosMPLSOamLspPingResultsProbeResponses_Object((1,3,6,1,4,1,6141,2,60,36,1,4,1,9),_WwpLeosMPLSOamLspPingResultsProbeResponses_Type())
wwpLeosMPLSOamLspPingResultsProbeResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsProbeResponses.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspPingResultsProbeResponses.setUnits('responses')
_WwpLeosMPLSOamLspTraceRouteCtlTable_Object=MibTable
wwpLeosMPLSOamLspTraceRouteCtlTable=_WwpLeosMPLSOamLspTraceRouteCtlTable_Object((1,3,6,1,4,1,6141,2,60,36,1,5))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlTable.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteCtlEntry_Object=MibTableRow
wwpLeosMPLSOamLspTraceRouteCtlEntry=_WwpLeosMPLSOamLspTraceRouteCtlEntry_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1))
wwpLeosMPLSOamLspTraceRouteCtlEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlEntry.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteCtlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_WwpLeosMPLSOamLspTraceRouteCtlIndex_Type.__name__=_D
_WwpLeosMPLSOamLspTraceRouteCtlIndex_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlIndex=_WwpLeosMPLSOamLspTraceRouteCtlIndex_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,1),_WwpLeosMPLSOamLspTraceRouteCtlIndex_Type())
wwpLeosMPLSOamLspTraceRouteCtlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlIndex.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteCtlLspType_Type(LspType):defaultValue=1
_WwpLeosMPLSOamLspTraceRouteCtlLspType_Type.__name__=_M
_WwpLeosMPLSOamLspTraceRouteCtlLspType_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlLspType=_WwpLeosMPLSOamLspTraceRouteCtlLspType_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,2),_WwpLeosMPLSOamLspTraceRouteCtlLspType_Type())
wwpLeosMPLSOamLspTraceRouteCtlLspType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlLspType.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteCtlLspName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_WwpLeosMPLSOamLspTraceRouteCtlLspName_Type.__name__=_J
_WwpLeosMPLSOamLspTraceRouteCtlLspName_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlLspName=_WwpLeosMPLSOamLspTraceRouteCtlLspName_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,3),_WwpLeosMPLSOamLspTraceRouteCtlLspName_Type())
wwpLeosMPLSOamLspTraceRouteCtlLspName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlLspName.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type.__name__=_E
_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlTimeOut=_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,4),_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type())
wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setUnits(_Q)
class _WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type.__name__=_E
_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlMaxTtl=_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,5),_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type())
wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setUnits('time-to-live value')
class _WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type.__name__=_D
_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlAdminStatus=_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,6),_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type())
wwpLeosMPLSOamLspTraceRouteCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlAdminStatus.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Type=RowStatus
_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlRowStatus=_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,5,1,7),_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Type())
wwpLeosMPLSOamLspTraceRouteCtlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteCtlRowStatus.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteResultsTable_Object=MibTable
wwpLeosMPLSOamLspTraceRouteResultsTable=_WwpLeosMPLSOamLspTraceRouteResultsTable_Object((1,3,6,1,4,1,6141,2,60,36,1,6))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsTable.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteResultsEntry_Object=MibTableRow
wwpLeosMPLSOamLspTraceRouteResultsEntry=_WwpLeosMPLSOamLspTraceRouteResultsEntry_Object((1,3,6,1,4,1,6141,2,60,36,1,6,1))
wwpLeosMPLSOamLspTraceRouteResultsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsEntry.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type.__name__=_D
_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsOperStatus=_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,6,1,1),_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type())
wwpLeosMPLSOamLspTraceRouteResultsOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsOperStatus.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteResultsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_R,2),('fail',3)))
_WwpLeosMPLSOamLspTraceRouteResultsStatus_Type.__name__=_D
_WwpLeosMPLSOamLspTraceRouteResultsStatus_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsStatus=_WwpLeosMPLSOamLspTraceRouteResultsStatus_Object((1,3,6,1,4,1,6141,2,60,36,1,6,1,2),_WwpLeosMPLSOamLspTraceRouteResultsStatus_Type())
wwpLeosMPLSOamLspTraceRouteResultsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsStatus.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Type=Gauge32
_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsCurHopCount=_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Object((1,3,6,1,4,1,6141,2,60,36,1,6,1,3),_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Type())
wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setUnits('hops')
_WwpLeosMPLSOamLspTraceRouteHopTable_Object=MibTable
wwpLeosMPLSOamLspTraceRouteHopTable=_WwpLeosMPLSOamLspTraceRouteHopTable_Object((1,3,6,1,4,1,6141,2,60,36,1,7))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopTable.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteHopEntry_Object=MibTableRow
wwpLeosMPLSOamLspTraceRouteHopEntry=_WwpLeosMPLSOamLspTraceRouteHopEntry_Object((1,3,6,1,4,1,6141,2,60,36,1,7,1))
wwpLeosMPLSOamLspTraceRouteHopEntry.setIndexNames((0,_F,_I),(0,_F,_S))
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopEntry.setStatus(_A)
class _WwpLeosMPLSOamLspTraceRouteHopIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_WwpLeosMPLSOamLspTraceRouteHopIndex_Type.__name__=_E
_WwpLeosMPLSOamLspTraceRouteHopIndex_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopIndex=_WwpLeosMPLSOamLspTraceRouteHopIndex_Object((1,3,6,1,4,1,6141,2,60,36,1,7,1,1),_WwpLeosMPLSOamLspTraceRouteHopIndex_Type())
wwpLeosMPLSOamLspTraceRouteHopIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopIndex.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopIndex.setUnits('hops')
_WwpLeosMPLSOamLspTraceRouteHopIp_Type=IpAddress
_WwpLeosMPLSOamLspTraceRouteHopIp_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopIp=_WwpLeosMPLSOamLspTraceRouteHopIp_Object((1,3,6,1,4,1,6141,2,60,36,1,7,1,2),_WwpLeosMPLSOamLspTraceRouteHopIp_Type())
wwpLeosMPLSOamLspTraceRouteHopIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopIp.setStatus(_A)
_WwpLeosMPLSOamLspTraceRouteHopLabel_Type=Unsigned32
_WwpLeosMPLSOamLspTraceRouteHopLabel_Object=MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopLabel=_WwpLeosMPLSOamLspTraceRouteHopLabel_Object((1,3,6,1,4,1,6141,2,60,36,1,7,1,3),_WwpLeosMPLSOamLspTraceRouteHopLabel_Type())
wwpLeosMPLSOamLspTraceRouteHopLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMPLSOamLspTraceRouteHopLabel.setStatus(_A)
_WwpLeosMPLSOamNotifications_ObjectIdentity=ObjectIdentity
wwpLeosMPLSOamNotifications=_WwpLeosMPLSOamNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,36,2))
_WwpLeosMPLSOamConformance_ObjectIdentity=ObjectIdentity
wwpLeosMPLSOamConformance=_WwpLeosMPLSOamConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,36,3))
mibBuilder.exportSymbols(_F,**{'OperationResponseStatus':OperationResponseStatus,'LspPingReturnCode':LspPingReturnCode,_M:LspType,'wwpLeosMPLSOamMIB':wwpLeosMPLSOamMIB,'wwpLeosMPLSOamObjects':wwpLeosMPLSOamObjects,'wwpLeosMPLSOAMLspPingMax':wwpLeosMPLSOAMLspPingMax,'wwpLeosMPLSOAMLspTraceRtMax':wwpLeosMPLSOAMLspTraceRtMax,'wwpLeosMPLSOamLspPingCtlTable':wwpLeosMPLSOamLspPingCtlTable,'wwpLeosMPLSOamLspPingCtlEntry':wwpLeosMPLSOamLspPingCtlEntry,_L:wwpLeosMPLSOamLspPingCtlIndex,'wwpLeosMPLSOamLspPingCtlLspType':wwpLeosMPLSOamLspPingCtlLspType,'wwpLeosMPLSOamLspPingCtlLspName':wwpLeosMPLSOamLspPingCtlLspName,'wwpLeosMPLSOamLspPingCtlPktSize':wwpLeosMPLSOamLspPingCtlPktSize,'wwpLeosMPLSOamLspPingCtlTimeOut':wwpLeosMPLSOamLspPingCtlTimeOut,'wwpLeosMPLSOamLspPingCtlCount':wwpLeosMPLSOamLspPingCtlCount,'wwpLeosMPLSOamLspPingCtlAdminState':wwpLeosMPLSOamLspPingCtlAdminState,'wwpLeosMPLSOamLspPingCtlTtl':wwpLeosMPLSOamLspPingCtlTtl,'wwpLeosMPLSOamLspPingCtlRowStatus':wwpLeosMPLSOamLspPingCtlRowStatus,'wwpLeosMPLSOamLspPingResultsTable':wwpLeosMPLSOamLspPingResultsTable,'wwpLeosMPLSOamLspPingResultsEntry':wwpLeosMPLSOamLspPingResultsEntry,'wwpLeosMPLSOamLspPingResultsOperStatus':wwpLeosMPLSOamLspPingResultsOperStatus,'wwpLeosMPLSOamLspPingResultsStatus':wwpLeosMPLSOamLspPingResultsStatus,'wwpLeosMPLSOamLspPingResultsLspType':wwpLeosMPLSOamLspPingResultsLspType,'wwpLeosMPLSOamLspPingResultsLspName':wwpLeosMPLSOamLspPingResultsLspName,'wwpLeosMPLSOamLspPingResultsMinRtt':wwpLeosMPLSOamLspPingResultsMinRtt,'wwpLeosMPLSOamLspPingResultsMaxRtt':wwpLeosMPLSOamLspPingResultsMaxRtt,'wwpLeosMPLSOamLspPingResultsAverageRtt':wwpLeosMPLSOamLspPingResultsAverageRtt,'wwpLeosMPLSOamLspPingResultsProbesSent':wwpLeosMPLSOamLspPingResultsProbesSent,'wwpLeosMPLSOamLspPingResultsProbeResponses':wwpLeosMPLSOamLspPingResultsProbeResponses,'wwpLeosMPLSOamLspTraceRouteCtlTable':wwpLeosMPLSOamLspTraceRouteCtlTable,'wwpLeosMPLSOamLspTraceRouteCtlEntry':wwpLeosMPLSOamLspTraceRouteCtlEntry,_I:wwpLeosMPLSOamLspTraceRouteCtlIndex,'wwpLeosMPLSOamLspTraceRouteCtlLspType':wwpLeosMPLSOamLspTraceRouteCtlLspType,'wwpLeosMPLSOamLspTraceRouteCtlLspName':wwpLeosMPLSOamLspTraceRouteCtlLspName,'wwpLeosMPLSOamLspTraceRouteCtlTimeOut':wwpLeosMPLSOamLspTraceRouteCtlTimeOut,'wwpLeosMPLSOamLspTraceRouteCtlMaxTtl':wwpLeosMPLSOamLspTraceRouteCtlMaxTtl,'wwpLeosMPLSOamLspTraceRouteCtlAdminStatus':wwpLeosMPLSOamLspTraceRouteCtlAdminStatus,'wwpLeosMPLSOamLspTraceRouteCtlRowStatus':wwpLeosMPLSOamLspTraceRouteCtlRowStatus,'wwpLeosMPLSOamLspTraceRouteResultsTable':wwpLeosMPLSOamLspTraceRouteResultsTable,'wwpLeosMPLSOamLspTraceRouteResultsEntry':wwpLeosMPLSOamLspTraceRouteResultsEntry,'wwpLeosMPLSOamLspTraceRouteResultsOperStatus':wwpLeosMPLSOamLspTraceRouteResultsOperStatus,'wwpLeosMPLSOamLspTraceRouteResultsStatus':wwpLeosMPLSOamLspTraceRouteResultsStatus,'wwpLeosMPLSOamLspTraceRouteResultsCurHopCount':wwpLeosMPLSOamLspTraceRouteResultsCurHopCount,'wwpLeosMPLSOamLspTraceRouteHopTable':wwpLeosMPLSOamLspTraceRouteHopTable,'wwpLeosMPLSOamLspTraceRouteHopEntry':wwpLeosMPLSOamLspTraceRouteHopEntry,_S:wwpLeosMPLSOamLspTraceRouteHopIndex,'wwpLeosMPLSOamLspTraceRouteHopIp':wwpLeosMPLSOamLspTraceRouteHopIp,'wwpLeosMPLSOamLspTraceRouteHopLabel':wwpLeosMPLSOamLspTraceRouteHopLabel,'wwpLeosMPLSOamNotifications':wwpLeosMPLSOamNotifications,'wwpLeosMPLSOamConformance':wwpLeosMPLSOamConformance})