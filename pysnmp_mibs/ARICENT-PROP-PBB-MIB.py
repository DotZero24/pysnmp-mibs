_X='fsPbbInstanceId'
_W='fsPbbPcpEncodingDropEligible'
_V='fsPbbPcpEncodingPriority'
_U='fsPbbPcpEncodingPcpSelRow'
_T='fsPbbPcpDecodingPcpValue'
_S='fsPbbPcpDecodingPcpSelRow'
_R='fsPbbCBPServiceMappingBackboneSid'
_Q='PriorityCodePoint'
_P='OctetString'
_O='read-create'
_N='TruthValue'
_M='DisplayString'
_L='ifIndex'
_K='IF-MIB'
_J='fsPbbContextId'
_I='fsPbbPipIfIndex'
_H='ARICENT-PBB-MIB'
_G='not-accessible'
_F='read-only'
_E='deprecated'
_D='ARICENT-PROP-PBB-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PriorityCodePoint,=mibBuilder.importSymbols('ARICENT-DOT1AD-MIB',_Q)
fsPbbCBPServiceMappingBackboneSid,fsPbbPipIfIndex=mibBuilder.importSymbols(_H,_R,_I)
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention',_N)
aricentProviderBackboneBridgeMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,15))
if mibBuilder.loadTexts:aricentProviderBackboneBridgeMIB.setRevisions(('2012-09-05 00:00',))
_FsPbbSystem_ObjectIdentity=ObjectIdentity
fsPbbSystem=_FsPbbSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,15,1))
class _FsPbbShutdownStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPbbShutdownStatus_Type.__name__=_C
_FsPbbShutdownStatus_Object=MibScalar
fsPbbShutdownStatus=_FsPbbShutdownStatus_Object((1,3,6,1,4,1,29601,2,15,1,1),_FsPbbShutdownStatus_Type())
fsPbbShutdownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbShutdownStatus.setStatus(_A)
class _FsPbbGlbOUI_Type(OctetString):defaultValue=OctetString('00:1E:83')
_FsPbbGlbOUI_Type.__name__=_P
_FsPbbGlbOUI_Object=MibScalar
fsPbbGlbOUI=_FsPbbGlbOUI_Object((1,3,6,1,4,1,29601,2,15,1,2),_FsPbbGlbOUI_Type())
fsPbbGlbOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbGlbOUI.setStatus(_A)
class _FsPbbMaxNoOfISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16777214))
_FsPbbMaxNoOfISID_Type.__name__=_C
_FsPbbMaxNoOfISID_Object=MibScalar
fsPbbMaxNoOfISID=_FsPbbMaxNoOfISID_Object((1,3,6,1,4,1,29601,2,15,1,3),_FsPbbMaxNoOfISID_Type())
fsPbbMaxNoOfISID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbMaxNoOfISID.setStatus(_E)
_FsPbbMaxNoOfISIDPerContext_Type=Integer32
_FsPbbMaxNoOfISIDPerContext_Object=MibScalar
fsPbbMaxNoOfISIDPerContext=_FsPbbMaxNoOfISIDPerContext_Object((1,3,6,1,4,1,29601,2,15,1,4),_FsPbbMaxNoOfISIDPerContext_Type())
fsPbbMaxNoOfISIDPerContext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbMaxNoOfISIDPerContext.setStatus(_E)
_FsPbbMaxPortsPerISID_Type=Integer32
_FsPbbMaxPortsPerISID_Object=MibScalar
fsPbbMaxPortsPerISID=_FsPbbMaxPortsPerISID_Object((1,3,6,1,4,1,29601,2,15,1,5),_FsPbbMaxPortsPerISID_Type())
fsPbbMaxPortsPerISID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbMaxPortsPerISID.setStatus(_E)
_FsPbbMaxPortsPerISIDPerContext_Type=Integer32
_FsPbbMaxPortsPerISIDPerContext_Object=MibScalar
fsPbbMaxPortsPerISIDPerContext=_FsPbbMaxPortsPerISIDPerContext_Object((1,3,6,1,4,1,29601,2,15,1,6),_FsPbbMaxPortsPerISIDPerContext_Type())
fsPbbMaxPortsPerISIDPerContext.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbMaxPortsPerISIDPerContext.setStatus(_E)
_FsPbbMaxCurrentNoOfISID_Type=Integer32
_FsPbbMaxCurrentNoOfISID_Object=MibScalar
fsPbbMaxCurrentNoOfISID=_FsPbbMaxCurrentNoOfISID_Object((1,3,6,1,4,1,29601,2,15,1,7),_FsPbbMaxCurrentNoOfISID_Type())
fsPbbMaxCurrentNoOfISID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbMaxCurrentNoOfISID.setStatus(_E)
_FsPbbMaxCurrentISIDPerContext_Type=Integer32
_FsPbbMaxCurrentISIDPerContext_Object=MibScalar
fsPbbMaxCurrentISIDPerContext=_FsPbbMaxCurrentISIDPerContext_Object((1,3,6,1,4,1,29601,2,15,1,8),_FsPbbMaxCurrentISIDPerContext_Type())
fsPbbMaxCurrentISIDPerContext.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbMaxCurrentISIDPerContext.setStatus(_E)
_FsPbbMaxCurrentPortsPerISID_Type=Integer32
_FsPbbMaxCurrentPortsPerISID_Object=MibScalar
fsPbbMaxCurrentPortsPerISID=_FsPbbMaxCurrentPortsPerISID_Object((1,3,6,1,4,1,29601,2,15,1,9),_FsPbbMaxCurrentPortsPerISID_Type())
fsPbbMaxCurrentPortsPerISID.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbMaxCurrentPortsPerISID.setStatus(_E)
_FsPbbMaxCurrPortsPerISIDContext_Type=Integer32
_FsPbbMaxCurrPortsPerISIDContext_Object=MibScalar
fsPbbMaxCurrPortsPerISIDContext=_FsPbbMaxCurrPortsPerISIDContext_Object((1,3,6,1,4,1,29601,2,15,1,10),_FsPbbMaxCurrPortsPerISIDContext_Type())
fsPbbMaxCurrPortsPerISIDContext.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbMaxCurrPortsPerISIDContext.setStatus(_E)
class _FsPbbTraceInput_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,288))
_FsPbbTraceInput_Type.__name__=_M
_FsPbbTraceInput_Object=MibScalar
fsPbbTraceInput=_FsPbbTraceInput_Object((1,3,6,1,4,1,29601,2,15,1,11),_FsPbbTraceInput_Type())
fsPbbTraceInput.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbTraceInput.setStatus(_A)
class _FsPbbTraceOption_Type(Integer32):defaultValue=256
_FsPbbTraceOption_Type.__name__=_C
_FsPbbTraceOption_Object=MibScalar
fsPbbTraceOption=_FsPbbTraceOption_Object((1,3,6,1,4,1,29601,2,15,1,12),_FsPbbTraceOption_Type())
fsPbbTraceOption.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbTraceOption.setStatus(_A)
_FsPbbISIDConfig_ObjectIdentity=ObjectIdentity
fsPbbISIDConfig=_FsPbbISIDConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,15,2))
_FsPbbISIDOUITable_Object=MibTable
fsPbbISIDOUITable=_FsPbbISIDOUITable_Object((1,3,6,1,4,1,29601,2,15,2,1))
if mibBuilder.loadTexts:fsPbbISIDOUITable.setStatus(_A)
_FsPbbISIDOUIEntry_Object=MibTableRow
fsPbbISIDOUIEntry=_FsPbbISIDOUIEntry_Object((1,3,6,1,4,1,29601,2,15,2,1,1))
fsPbbISIDOUIEntry.setIndexNames((0,_D,_J),(0,_H,_R),(0,_K,_L))
if mibBuilder.loadTexts:fsPbbISIDOUIEntry.setStatus(_A)
class _FsPbbContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPbbContextId_Type.__name__=_C
_FsPbbContextId_Object=MibTableColumn
fsPbbContextId=_FsPbbContextId_Object((1,3,6,1,4,1,29601,2,15,2,1,1,1),_FsPbbContextId_Type())
fsPbbContextId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbContextId.setStatus(_A)
_FsPbbOUI_Type=OctetString
_FsPbbOUI_Object=MibTableColumn
fsPbbOUI=_FsPbbOUI_Object((1,3,6,1,4,1,29601,2,15,2,1,1,2),_FsPbbOUI_Type())
fsPbbOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbOUI.setStatus(_A)
_FsPbbOUIRowStatus_Type=RowStatus
_FsPbbOUIRowStatus_Object=MibTableColumn
fsPbbOUIRowStatus=_FsPbbOUIRowStatus_Object((1,3,6,1,4,1,29601,2,15,2,1,1,3),_FsPbbOUIRowStatus_Type())
fsPbbOUIRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsPbbOUIRowStatus.setStatus(_A)
_FsPbbPortConfig_ObjectIdentity=ObjectIdentity
fsPbbPortConfig=_FsPbbPortConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,15,3))
_FsPbbPortPisidTable_Object=MibTable
fsPbbPortPisidTable=_FsPbbPortPisidTable_Object((1,3,6,1,4,1,29601,2,15,3,1))
if mibBuilder.loadTexts:fsPbbPortPisidTable.setStatus(_A)
_FsPbbPortPisidEntry_Object=MibTableRow
fsPbbPortPisidEntry=_FsPbbPortPisidEntry_Object((1,3,6,1,4,1,29601,2,15,3,1,1))
fsPbbPortPisidEntry.setIndexNames((0,_D,_J),(0,_K,_L))
if mibBuilder.loadTexts:fsPbbPortPisidEntry.setStatus(_A)
_FsPbbPortPisid_Type=Integer32
_FsPbbPortPisid_Object=MibTableColumn
fsPbbPortPisid=_FsPbbPortPisid_Object((1,3,6,1,4,1,29601,2,15,3,1,1,1),_FsPbbPortPisid_Type())
fsPbbPortPisid.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPortPisid.setStatus(_A)
_FsPbbPIsidRowStatus_Type=RowStatus
_FsPbbPIsidRowStatus_Object=MibTableColumn
fsPbbPIsidRowStatus=_FsPbbPIsidRowStatus_Object((1,3,6,1,4,1,29601,2,15,3,1,1,2),_FsPbbPIsidRowStatus_Type())
fsPbbPIsidRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsPbbPIsidRowStatus.setStatus(_A)
_FsPbbPortTable_Object=MibTable
fsPbbPortTable=_FsPbbPortTable_Object((1,3,6,1,4,1,29601,2,15,3,2))
if mibBuilder.loadTexts:fsPbbPortTable.setStatus(_A)
_FsPbbPortEntry_Object=MibTableRow
fsPbbPortEntry=_FsPbbPortEntry_Object((1,3,6,1,4,1,29601,2,15,3,2,1))
fsPbbPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsPbbPortEntry.setStatus(_A)
class _FsPbbPortPcpSelectionRow_Type(PriorityCodePoint):defaultValue=1
_FsPbbPortPcpSelectionRow_Type.__name__=_Q
_FsPbbPortPcpSelectionRow_Object=MibTableColumn
fsPbbPortPcpSelectionRow=_FsPbbPortPcpSelectionRow_Object((1,3,6,1,4,1,29601,2,15,3,2,1,1),_FsPbbPortPcpSelectionRow_Type())
fsPbbPortPcpSelectionRow.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPortPcpSelectionRow.setStatus(_A)
class _FsPbbPortUseDei_Type(TruthValue):defaultValue=2
_FsPbbPortUseDei_Type.__name__=_N
_FsPbbPortUseDei_Object=MibTableColumn
fsPbbPortUseDei=_FsPbbPortUseDei_Object((1,3,6,1,4,1,29601,2,15,3,2,1,2),_FsPbbPortUseDei_Type())
fsPbbPortUseDei.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPortUseDei.setStatus(_A)
class _FsPbbPortReqDropEncoding_Type(TruthValue):defaultValue=2
_FsPbbPortReqDropEncoding_Type.__name__=_N
_FsPbbPortReqDropEncoding_Object=MibTableColumn
fsPbbPortReqDropEncoding=_FsPbbPortReqDropEncoding_Object((1,3,6,1,4,1,29601,2,15,3,2,1,3),_FsPbbPortReqDropEncoding_Type())
fsPbbPortReqDropEncoding.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPortReqDropEncoding.setStatus(_A)
_FsPbbPcpDecodingTable_Object=MibTable
fsPbbPcpDecodingTable=_FsPbbPcpDecodingTable_Object((1,3,6,1,4,1,29601,2,15,3,3))
if mibBuilder.loadTexts:fsPbbPcpDecodingTable.setStatus(_A)
_FsPbbPcpDecodingEntry_Object=MibTableRow
fsPbbPcpDecodingEntry=_FsPbbPcpDecodingEntry_Object((1,3,6,1,4,1,29601,2,15,3,3,1))
fsPbbPcpDecodingEntry.setIndexNames((0,_H,_I),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:fsPbbPcpDecodingEntry.setStatus(_A)
_FsPbbPcpDecodingPcpSelRow_Type=PriorityCodePoint
_FsPbbPcpDecodingPcpSelRow_Object=MibTableColumn
fsPbbPcpDecodingPcpSelRow=_FsPbbPcpDecodingPcpSelRow_Object((1,3,6,1,4,1,29601,2,15,3,3,1,1),_FsPbbPcpDecodingPcpSelRow_Type())
fsPbbPcpDecodingPcpSelRow.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbPcpDecodingPcpSelRow.setStatus(_A)
class _FsPbbPcpDecodingPcpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsPbbPcpDecodingPcpValue_Type.__name__=_C
_FsPbbPcpDecodingPcpValue_Object=MibTableColumn
fsPbbPcpDecodingPcpValue=_FsPbbPcpDecodingPcpValue_Object((1,3,6,1,4,1,29601,2,15,3,3,1,2),_FsPbbPcpDecodingPcpValue_Type())
fsPbbPcpDecodingPcpValue.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbPcpDecodingPcpValue.setStatus(_A)
class _FsPbbPcpDecodingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsPbbPcpDecodingPriority_Type.__name__=_C
_FsPbbPcpDecodingPriority_Object=MibTableColumn
fsPbbPcpDecodingPriority=_FsPbbPcpDecodingPriority_Object((1,3,6,1,4,1,29601,2,15,3,3,1,3),_FsPbbPcpDecodingPriority_Type())
fsPbbPcpDecodingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPcpDecodingPriority.setStatus(_A)
_FsPbbPcpDecodingDropEligible_Type=TruthValue
_FsPbbPcpDecodingDropEligible_Object=MibTableColumn
fsPbbPcpDecodingDropEligible=_FsPbbPcpDecodingDropEligible_Object((1,3,6,1,4,1,29601,2,15,3,3,1,4),_FsPbbPcpDecodingDropEligible_Type())
fsPbbPcpDecodingDropEligible.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPcpDecodingDropEligible.setStatus(_A)
_FsPbbPcpEncodingTable_Object=MibTable
fsPbbPcpEncodingTable=_FsPbbPcpEncodingTable_Object((1,3,6,1,4,1,29601,2,15,3,4))
if mibBuilder.loadTexts:fsPbbPcpEncodingTable.setStatus(_A)
_FsPbbPcpEncodingEntry_Object=MibTableRow
fsPbbPcpEncodingEntry=_FsPbbPcpEncodingEntry_Object((1,3,6,1,4,1,29601,2,15,3,4,1))
fsPbbPcpEncodingEntry.setIndexNames((0,_H,_I),(0,_D,_U),(0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:fsPbbPcpEncodingEntry.setStatus(_A)
_FsPbbPcpEncodingPcpSelRow_Type=PriorityCodePoint
_FsPbbPcpEncodingPcpSelRow_Object=MibTableColumn
fsPbbPcpEncodingPcpSelRow=_FsPbbPcpEncodingPcpSelRow_Object((1,3,6,1,4,1,29601,2,15,3,4,1,1),_FsPbbPcpEncodingPcpSelRow_Type())
fsPbbPcpEncodingPcpSelRow.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbPcpEncodingPcpSelRow.setStatus(_A)
class _FsPbbPcpEncodingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsPbbPcpEncodingPriority_Type.__name__=_C
_FsPbbPcpEncodingPriority_Object=MibTableColumn
fsPbbPcpEncodingPriority=_FsPbbPcpEncodingPriority_Object((1,3,6,1,4,1,29601,2,15,3,4,1,2),_FsPbbPcpEncodingPriority_Type())
fsPbbPcpEncodingPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbPcpEncodingPriority.setStatus(_A)
_FsPbbPcpEncodingDropEligible_Type=TruthValue
_FsPbbPcpEncodingDropEligible_Object=MibTableColumn
fsPbbPcpEncodingDropEligible=_FsPbbPcpEncodingDropEligible_Object((1,3,6,1,4,1,29601,2,15,3,4,1,3),_FsPbbPcpEncodingDropEligible_Type())
fsPbbPcpEncodingDropEligible.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbPcpEncodingDropEligible.setStatus(_A)
class _FsPbbPcpEncodingPcpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsPbbPcpEncodingPcpValue_Type.__name__=_C
_FsPbbPcpEncodingPcpValue_Object=MibTableColumn
fsPbbPcpEncodingPcpValue=_FsPbbPcpEncodingPcpValue_Object((1,3,6,1,4,1,29601,2,15,3,4,1,4),_FsPbbPcpEncodingPcpValue_Type())
fsPbbPcpEncodingPcpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbPcpEncodingPcpValue.setStatus(_A)
_FsPbbInstanceConfig_ObjectIdentity=ObjectIdentity
fsPbbInstanceConfig=_FsPbbInstanceConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,15,4))
_FsPbbInstanceTable_Object=MibTable
fsPbbInstanceTable=_FsPbbInstanceTable_Object((1,3,6,1,4,1,29601,2,15,4,1))
if mibBuilder.loadTexts:fsPbbInstanceTable.setStatus(_A)
_FsPbbInstanceEntry_Object=MibTableRow
fsPbbInstanceEntry=_FsPbbInstanceEntry_Object((1,3,6,1,4,1,29601,2,15,4,1,1))
fsPbbInstanceEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:fsPbbInstanceEntry.setStatus(_A)
class _FsPbbInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPbbInstanceId_Type.__name__=_C
_FsPbbInstanceId_Object=MibTableColumn
fsPbbInstanceId=_FsPbbInstanceId_Object((1,3,6,1,4,1,29601,2,15,4,1,1,1),_FsPbbInstanceId_Type())
fsPbbInstanceId.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPbbInstanceId.setStatus(_A)
_FsPbbInstanceMacAddr_Type=MacAddress
_FsPbbInstanceMacAddr_Object=MibTableColumn
fsPbbInstanceMacAddr=_FsPbbInstanceMacAddr_Object((1,3,6,1,4,1,29601,2,15,4,1,1,2),_FsPbbInstanceMacAddr_Type())
fsPbbInstanceMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbInstanceMacAddr.setStatus(_A)
class _FsPbbInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsPbbInstanceName_Type.__name__=_M
_FsPbbInstanceName_Object=MibTableColumn
fsPbbInstanceName=_FsPbbInstanceName_Object((1,3,6,1,4,1,29601,2,15,4,1,1,3),_FsPbbInstanceName_Type())
fsPbbInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbInstanceName.setStatus(_A)
_FsPbbInstanceIComponents_Type=Unsigned32
_FsPbbInstanceIComponents_Object=MibTableColumn
fsPbbInstanceIComponents=_FsPbbInstanceIComponents_Object((1,3,6,1,4,1,29601,2,15,4,1,1,4),_FsPbbInstanceIComponents_Type())
fsPbbInstanceIComponents.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbInstanceIComponents.setStatus(_A)
_FsPbbInstanceBComponents_Type=Unsigned32
_FsPbbInstanceBComponents_Object=MibTableColumn
fsPbbInstanceBComponents=_FsPbbInstanceBComponents_Object((1,3,6,1,4,1,29601,2,15,4,1,1,5),_FsPbbInstanceBComponents_Type())
fsPbbInstanceBComponents.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbInstanceBComponents.setStatus(_A)
_FsPbbInstanceBebPorts_Type=Unsigned32
_FsPbbInstanceBebPorts_Object=MibTableColumn
fsPbbInstanceBebPorts=_FsPbbInstanceBebPorts_Object((1,3,6,1,4,1,29601,2,15,4,1,1,6),_FsPbbInstanceBebPorts_Type())
fsPbbInstanceBebPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPbbInstanceBebPorts.setStatus(_A)
_FsPbbInstanceRowStatus_Type=RowStatus
_FsPbbInstanceRowStatus_Object=MibTableColumn
fsPbbInstanceRowStatus=_FsPbbInstanceRowStatus_Object((1,3,6,1,4,1,29601,2,15,4,1,1,7),_FsPbbInstanceRowStatus_Type())
fsPbbInstanceRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:fsPbbInstanceRowStatus.setStatus(_A)
_FsPbbInstanceMappingTable_Object=MibTable
fsPbbInstanceMappingTable=_FsPbbInstanceMappingTable_Object((1,3,6,1,4,1,29601,2,15,4,2))
if mibBuilder.loadTexts:fsPbbInstanceMappingTable.setStatus(_A)
_FsPbbInstanceMappingEntry_Object=MibTableRow
fsPbbInstanceMappingEntry=_FsPbbInstanceMappingEntry_Object((1,3,6,1,4,1,29601,2,15,4,2,1))
fsPbbInstanceMappingEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fsPbbInstanceMappingEntry.setStatus(_A)
class _FsPbbContextToInstanceId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPbbContextToInstanceId_Type.__name__=_C
_FsPbbContextToInstanceId_Object=MibTableColumn
fsPbbContextToInstanceId=_FsPbbContextToInstanceId_Object((1,3,6,1,4,1,29601,2,15,4,2,1,1),_FsPbbContextToInstanceId_Type())
fsPbbContextToInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPbbContextToInstanceId.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'aricentProviderBackboneBridgeMIB':aricentProviderBackboneBridgeMIB,'fsPbbSystem':fsPbbSystem,'fsPbbShutdownStatus':fsPbbShutdownStatus,'fsPbbGlbOUI':fsPbbGlbOUI,'fsPbbMaxNoOfISID':fsPbbMaxNoOfISID,'fsPbbMaxNoOfISIDPerContext':fsPbbMaxNoOfISIDPerContext,'fsPbbMaxPortsPerISID':fsPbbMaxPortsPerISID,'fsPbbMaxPortsPerISIDPerContext':fsPbbMaxPortsPerISIDPerContext,'fsPbbMaxCurrentNoOfISID':fsPbbMaxCurrentNoOfISID,'fsPbbMaxCurrentISIDPerContext':fsPbbMaxCurrentISIDPerContext,'fsPbbMaxCurrentPortsPerISID':fsPbbMaxCurrentPortsPerISID,'fsPbbMaxCurrPortsPerISIDContext':fsPbbMaxCurrPortsPerISIDContext,'fsPbbTraceInput':fsPbbTraceInput,'fsPbbTraceOption':fsPbbTraceOption,'fsPbbISIDConfig':fsPbbISIDConfig,'fsPbbISIDOUITable':fsPbbISIDOUITable,'fsPbbISIDOUIEntry':fsPbbISIDOUIEntry,_J:fsPbbContextId,'fsPbbOUI':fsPbbOUI,'fsPbbOUIRowStatus':fsPbbOUIRowStatus,'fsPbbPortConfig':fsPbbPortConfig,'fsPbbPortPisidTable':fsPbbPortPisidTable,'fsPbbPortPisidEntry':fsPbbPortPisidEntry,'fsPbbPortPisid':fsPbbPortPisid,'fsPbbPIsidRowStatus':fsPbbPIsidRowStatus,'fsPbbPortTable':fsPbbPortTable,'fsPbbPortEntry':fsPbbPortEntry,'fsPbbPortPcpSelectionRow':fsPbbPortPcpSelectionRow,'fsPbbPortUseDei':fsPbbPortUseDei,'fsPbbPortReqDropEncoding':fsPbbPortReqDropEncoding,'fsPbbPcpDecodingTable':fsPbbPcpDecodingTable,'fsPbbPcpDecodingEntry':fsPbbPcpDecodingEntry,_S:fsPbbPcpDecodingPcpSelRow,_T:fsPbbPcpDecodingPcpValue,'fsPbbPcpDecodingPriority':fsPbbPcpDecodingPriority,'fsPbbPcpDecodingDropEligible':fsPbbPcpDecodingDropEligible,'fsPbbPcpEncodingTable':fsPbbPcpEncodingTable,'fsPbbPcpEncodingEntry':fsPbbPcpEncodingEntry,_U:fsPbbPcpEncodingPcpSelRow,_V:fsPbbPcpEncodingPriority,_W:fsPbbPcpEncodingDropEligible,'fsPbbPcpEncodingPcpValue':fsPbbPcpEncodingPcpValue,'fsPbbInstanceConfig':fsPbbInstanceConfig,'fsPbbInstanceTable':fsPbbInstanceTable,'fsPbbInstanceEntry':fsPbbInstanceEntry,_X:fsPbbInstanceId,'fsPbbInstanceMacAddr':fsPbbInstanceMacAddr,'fsPbbInstanceName':fsPbbInstanceName,'fsPbbInstanceIComponents':fsPbbInstanceIComponents,'fsPbbInstanceBComponents':fsPbbInstanceBComponents,'fsPbbInstanceBebPorts':fsPbbInstanceBebPorts,'fsPbbInstanceRowStatus':fsPbbInstanceRowStatus,'fsPbbInstanceMappingTable':fsPbbInstanceMappingTable,'fsPbbInstanceMappingEntry':fsPbbInstanceMappingEntry,'fsPbbContextToInstanceId':fsPbbContextToInstanceId})