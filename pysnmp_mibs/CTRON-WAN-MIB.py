_l='ctWanHDSLLoopbacksHLUConnIndex'
_k='ctWanHDSLAlarmHistoryConnIndex'
_j='ctWanHDSLAlarmsHLUConnIndex'
_i='ctWanHDSLTestHLUConnIndex'
_h='ctWanHDSLStatisticsHLUConnIndex'
_g='ctWanHDSLPerformance24hSlotIndex'
_f='ctWanHDSLPerformance24hConnIndex'
_e='ctWanHDSLPerformance15mSlotIndex'
_d='ctWanHDSLPerformance15mConnIndex'
_c='ipPQAddressId'
_b='ds1PhysNum'
_a='recover'
_Z='ddsLineIndex'
_Y='frDcpCircuitDlci'
_X='frDcpCircuitIfIndex'
_W='wanRs232ExtensionsEntryIndex'
_V='wanDs1ExtensionsEntryIndex'
_U='deprecated'
_T='wanInterfaceEntryIndex'
_S='wanInterfacePhysPortIndex'
_R='wanInterfaceConnectionIndex'
_Q='wanPhysPortIndex'
_P='wanPhysPortConnectionIndex'
_O='wanConnIndex'
_N='none'
_M='OctetString'
_L='off'
_K='on'
_J='disable'
_I='enable'
_H='enabled'
_G='disabled'
_F='DisplayString'
_E='CTRON-WAN-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctWan,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctWan')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class Index(Integer32):0
class DLCI(Integer32):0
_CtWanConnection_ObjectIdentity=ObjectIdentity
ctWanConnection=_CtWanConnection_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,1))
_WanNumConnections_Type=Integer32
_WanNumConnections_Object=MibScalar
wanNumConnections=_WanNumConnections_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,1),_WanNumConnections_Type())
wanNumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:wanNumConnections.setStatus(_A)
_WanConnTable_Object=MibTable
wanConnTable=_WanConnTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2))
if mibBuilder.loadTexts:wanConnTable.setStatus(_A)
_WanConnEntry_Object=MibTableRow
wanConnEntry=_WanConnEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2,1))
wanConnEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wanConnEntry.setStatus(_A)
_WanConnIndex_Type=Integer32
_WanConnIndex_Object=MibTableColumn
wanConnIndex=_WanConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2,1,1),_WanConnIndex_Type())
wanConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanConnIndex.setStatus(_A)
_WanConnNumPhysPorts_Type=Integer32
_WanConnNumPhysPorts_Object=MibTableColumn
wanConnNumPhysPorts=_WanConnNumPhysPorts_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2,1,2),_WanConnNumPhysPorts_Type())
wanConnNumPhysPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanConnNumPhysPorts.setStatus(_A)
_WanConnDefaultPhysPort_Type=Integer32
_WanConnDefaultPhysPort_Object=MibTableColumn
wanConnDefaultPhysPort=_WanConnDefaultPhysPort_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2,1,3),_WanConnDefaultPhysPort_Type())
wanConnDefaultPhysPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wanConnDefaultPhysPort.setStatus(_A)
_WanConnActivePhysPort_Type=Integer32
_WanConnActivePhysPort_Object=MibTableColumn
wanConnActivePhysPort=_WanConnActivePhysPort_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,2,1,4),_WanConnActivePhysPort_Type())
wanConnActivePhysPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wanConnActivePhysPort.setStatus(_A)
_WanPhysPortTable_Object=MibTable
wanPhysPortTable=_WanPhysPortTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3))
if mibBuilder.loadTexts:wanPhysPortTable.setStatus(_A)
_WanPhysPortEntry_Object=MibTableRow
wanPhysPortEntry=_WanPhysPortEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3,1))
wanPhysPortEntry.setIndexNames((0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:wanPhysPortEntry.setStatus(_A)
_WanPhysPortConnectionIndex_Type=Integer32
_WanPhysPortConnectionIndex_Object=MibTableColumn
wanPhysPortConnectionIndex=_WanPhysPortConnectionIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3,1,1),_WanPhysPortConnectionIndex_Type())
wanPhysPortConnectionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPhysPortConnectionIndex.setStatus(_A)
_WanPhysPortIndex_Type=Integer32
_WanPhysPortIndex_Object=MibTableColumn
wanPhysPortIndex=_WanPhysPortIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3,1,2),_WanPhysPortIndex_Type())
wanPhysPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPhysPortIndex.setStatus(_A)
class _WanPhysPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_N,1),('t1',2),('e1',3),('synchronous',4),('dds',5),('di',6),('hdsl',7),('bri',8),('ds30',9),('t1DDS',10)))
_WanPhysPortType_Type.__name__=_C
_WanPhysPortType_Object=MibTableColumn
wanPhysPortType=_WanPhysPortType_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3,1,3),_WanPhysPortType_Type())
wanPhysPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPhysPortType.setStatus(_A)
_WanPhysPortSpecificMib_Type=ObjectIdentifier
_WanPhysPortSpecificMib_Object=MibTableColumn
wanPhysPortSpecificMib=_WanPhysPortSpecificMib_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,3,1,4),_WanPhysPortSpecificMib_Type())
wanPhysPortSpecificMib.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPhysPortSpecificMib.setStatus(_A)
_WanInterfaceTable_Object=MibTable
wanInterfaceTable=_WanInterfaceTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4))
if mibBuilder.loadTexts:wanInterfaceTable.setStatus(_A)
_WanInterfaceEntry_Object=MibTableRow
wanInterfaceEntry=_WanInterfaceEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1))
wanInterfaceEntry.setIndexNames((0,_E,_R),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:wanInterfaceEntry.setStatus(_A)
_WanInterfaceConnectionIndex_Type=Integer32
_WanInterfaceConnectionIndex_Object=MibTableColumn
wanInterfaceConnectionIndex=_WanInterfaceConnectionIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,1),_WanInterfaceConnectionIndex_Type())
wanInterfaceConnectionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceConnectionIndex.setStatus(_A)
_WanInterfacePhysPortIndex_Type=Integer32
_WanInterfacePhysPortIndex_Object=MibTableColumn
wanInterfacePhysPortIndex=_WanInterfacePhysPortIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,2),_WanInterfacePhysPortIndex_Type())
wanInterfacePhysPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfacePhysPortIndex.setStatus(_A)
_WanInterfaceEntryIndex_Type=Integer32
_WanInterfaceEntryIndex_Object=MibTableColumn
wanInterfaceEntryIndex=_WanInterfaceEntryIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,3),_WanInterfaceEntryIndex_Type())
wanInterfaceEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceEntryIndex.setStatus(_A)
_WanInterfaceEntryIfIndex_Type=Integer32
_WanInterfaceEntryIfIndex_Object=MibTableColumn
wanInterfaceEntryIfIndex=_WanInterfaceEntryIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,4),_WanInterfaceEntryIfIndex_Type())
wanInterfaceEntryIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceEntryIfIndex.setStatus(_A)
_WanInterfaceEntryProtocol_Type=Integer32
_WanInterfaceEntryProtocol_Object=MibTableColumn
wanInterfaceEntryProtocol=_WanInterfaceEntryProtocol_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,5),_WanInterfaceEntryProtocol_Type())
wanInterfaceEntryProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryProtocol.setStatus(_A)
class _WanInterfaceEntryCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WanInterfaceEntryCompression_Type.__name__=_C
_WanInterfaceEntryCompression_Object=MibTableColumn
wanInterfaceEntryCompression=_WanInterfaceEntryCompression_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,6),_WanInterfaceEntryCompression_Type())
wanInterfaceEntryCompression.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryCompression.setStatus(_A)
_WanInterfaceEntryMTU_Type=Integer32
_WanInterfaceEntryMTU_Object=MibTableColumn
wanInterfaceEntryMTU=_WanInterfaceEntryMTU_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,7),_WanInterfaceEntryMTU_Type())
wanInterfaceEntryMTU.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryMTU.setStatus(_A)
class _WanInterfaceEntryLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('jBZS',2),('invHDLC',3)))
_WanInterfaceEntryLineCoding_Type.__name__=_C
_WanInterfaceEntryLineCoding_Object=MibTableColumn
wanInterfaceEntryLineCoding=_WanInterfaceEntryLineCoding_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,8),_WanInterfaceEntryLineCoding_Type())
wanInterfaceEntryLineCoding.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryLineCoding.setStatus(_A)
class _WanInterfaceEntryCrcLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sixteen-bits',1),('thirty-two-bits',2)))
_WanInterfaceEntryCrcLength_Type.__name__=_C
_WanInterfaceEntryCrcLength_Object=MibTableColumn
wanInterfaceEntryCrcLength=_WanInterfaceEntryCrcLength_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,9),_WanInterfaceEntryCrcLength_Type())
wanInterfaceEntryCrcLength.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryCrcLength.setStatus(_A)
class _WanInterfaceEntryLexProtocolEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WanInterfaceEntryLexProtocolEnable_Type.__name__=_C
_WanInterfaceEntryLexProtocolEnable_Object=MibTableColumn
wanInterfaceEntryLexProtocolEnable=_WanInterfaceEntryLexProtocolEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,10),_WanInterfaceEntryLexProtocolEnable_Type())
wanInterfaceEntryLexProtocolEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryLexProtocolEnable.setStatus(_U)
class _WanInterfaceEntryLexProtocolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bound',1),('unbound',2)))
_WanInterfaceEntryLexProtocolStatus_Type.__name__=_C
_WanInterfaceEntryLexProtocolStatus_Object=MibTableColumn
wanInterfaceEntryLexProtocolStatus=_WanInterfaceEntryLexProtocolStatus_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,11),_WanInterfaceEntryLexProtocolStatus_Type())
wanInterfaceEntryLexProtocolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceEntryLexProtocolStatus.setStatus(_U)
class _WanInterfaceEntryCompRatio_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WanInterfaceEntryCompRatio_Type.__name__=_M
_WanInterfaceEntryCompRatio_Object=MibTableColumn
wanInterfaceEntryCompRatio=_WanInterfaceEntryCompRatio_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,12),_WanInterfaceEntryCompRatio_Type())
wanInterfaceEntryCompRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceEntryCompRatio.setStatus(_A)
class _WanInterfaceEntryCompStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_WanInterfaceEntryCompStatus_Type.__name__=_C
_WanInterfaceEntryCompStatus_Object=MibTableColumn
wanInterfaceEntryCompStatus=_WanInterfaceEntryCompStatus_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,13),_WanInterfaceEntryCompStatus_Type())
wanInterfaceEntryCompStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wanInterfaceEntryCompStatus.setStatus(_A)
class _WanInterfaceEntryBackUpIfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WanInterfaceEntryBackUpIfEnable_Type.__name__=_C
_WanInterfaceEntryBackUpIfEnable_Object=MibTableColumn
wanInterfaceEntryBackUpIfEnable=_WanInterfaceEntryBackUpIfEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,1,4,1,14),_WanInterfaceEntryBackUpIfEnable_Type())
wanInterfaceEntryBackUpIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanInterfaceEntryBackUpIfEnable.setStatus(_A)
_CtWanDs1_ObjectIdentity=ObjectIdentity
ctWanDs1=_CtWanDs1_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,2))
_WanDs1ExtensionsTable_Object=MibTable
wanDs1ExtensionsTable=_WanDs1ExtensionsTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1))
if mibBuilder.loadTexts:wanDs1ExtensionsTable.setStatus(_A)
_WanDs1ExtensionsEntry_Object=MibTableRow
wanDs1ExtensionsEntry=_WanDs1ExtensionsEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1))
wanDs1ExtensionsEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:wanDs1ExtensionsEntry.setStatus(_A)
_WanDs1ExtensionsEntryIndex_Type=Integer32
_WanDs1ExtensionsEntryIndex_Object=MibTableColumn
wanDs1ExtensionsEntryIndex=_WanDs1ExtensionsEntryIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,1),_WanDs1ExtensionsEntryIndex_Type())
wanDs1ExtensionsEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsEntryIndex.setStatus(_A)
_WanDs1ExtensionsNumInterfaces_Type=Integer32
_WanDs1ExtensionsNumInterfaces_Object=MibTableColumn
wanDs1ExtensionsNumInterfaces=_WanDs1ExtensionsNumInterfaces_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,2),_WanDs1ExtensionsNumInterfaces_Type())
wanDs1ExtensionsNumInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsNumInterfaces.setStatus(_A)
class _WanDs1ExtensionsToggleFracTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('update-table',1),('display-new',2),('display-old',3),('restore-old',4)))
_WanDs1ExtensionsToggleFracTable_Type.__name__=_C
_WanDs1ExtensionsToggleFracTable_Object=MibTableColumn
wanDs1ExtensionsToggleFracTable=_WanDs1ExtensionsToggleFracTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,3),_WanDs1ExtensionsToggleFracTable_Type())
wanDs1ExtensionsToggleFracTable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsToggleFracTable.setStatus(_A)
class _WanDs1ExtensionsLineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('zero',2),('minus-7point5',3),('minus-15',4),('a133to266feet',5),('a266to399feet',6),('a399to533feet',7),('a533to655feet',8)))
_WanDs1ExtensionsLineBuildOut_Type.__name__=_C
_WanDs1ExtensionsLineBuildOut_Object=MibTableColumn
wanDs1ExtensionsLineBuildOut=_WanDs1ExtensionsLineBuildOut_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,4),_WanDs1ExtensionsLineBuildOut_Type())
wanDs1ExtensionsLineBuildOut.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsLineBuildOut.setStatus(_A)
class _WanDs1ExtensionsCFADuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_WanDs1ExtensionsCFADuration_Type.__name__=_C
_WanDs1ExtensionsCFADuration_Object=MibTableColumn
wanDs1ExtensionsCFADuration=_WanDs1ExtensionsCFADuration_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,5),_WanDs1ExtensionsCFADuration_Type())
wanDs1ExtensionsCFADuration.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsCFADuration.setStatus(_A)
class _WanDs1ExtensionsDIEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('diDataEnabled',3)))
_WanDs1ExtensionsDIEnable_Type.__name__=_C
_WanDs1ExtensionsDIEnable_Object=MibTableColumn
wanDs1ExtensionsDIEnable=_WanDs1ExtensionsDIEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,6),_WanDs1ExtensionsDIEnable_Type())
wanDs1ExtensionsDIEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsDIEnable.setStatus(_A)
_WanDs1ExtensionsTotalValidIntervals_Type=Counter32
_WanDs1ExtensionsTotalValidIntervals_Object=MibTableColumn
wanDs1ExtensionsTotalValidIntervals=_WanDs1ExtensionsTotalValidIntervals_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,7),_WanDs1ExtensionsTotalValidIntervals_Type())
wanDs1ExtensionsTotalValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsTotalValidIntervals.setStatus(_A)
class _WanDs1ExtensionsBertTestMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('internal',2),('manual',3)))
_WanDs1ExtensionsBertTestMode_Type.__name__=_C
_WanDs1ExtensionsBertTestMode_Object=MibTableColumn
wanDs1ExtensionsBertTestMode=_WanDs1ExtensionsBertTestMode_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,8),_WanDs1ExtensionsBertTestMode_Type())
wanDs1ExtensionsBertTestMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsBertTestMode.setStatus(_A)
class _WanDs1ExtensionsBertRun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WanDs1ExtensionsBertRun_Type.__name__=_C
_WanDs1ExtensionsBertRun_Object=MibTableColumn
wanDs1ExtensionsBertRun=_WanDs1ExtensionsBertRun_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,9),_WanDs1ExtensionsBertRun_Type())
wanDs1ExtensionsBertRun.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsBertRun.setStatus(_A)
_WanDs1ExtensionsBertCurrentResults_Type=Integer32
_WanDs1ExtensionsBertCurrentResults_Object=MibTableColumn
wanDs1ExtensionsBertCurrentResults=_WanDs1ExtensionsBertCurrentResults_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,10),_WanDs1ExtensionsBertCurrentResults_Type())
wanDs1ExtensionsBertCurrentResults.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertCurrentResults.setStatus(_A)
_WanDs1ExtensionsBertCumulativeResults_Type=Integer32
_WanDs1ExtensionsBertCumulativeResults_Object=MibTableColumn
wanDs1ExtensionsBertCumulativeResults=_WanDs1ExtensionsBertCumulativeResults_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,11),_WanDs1ExtensionsBertCumulativeResults_Type())
wanDs1ExtensionsBertCumulativeResults.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertCumulativeResults.setStatus(_A)
_WanDs1ExtensionsBertPeakResults_Type=Integer32
_WanDs1ExtensionsBertPeakResults_Object=MibTableColumn
wanDs1ExtensionsBertPeakResults=_WanDs1ExtensionsBertPeakResults_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,12),_WanDs1ExtensionsBertPeakResults_Type())
wanDs1ExtensionsBertPeakResults.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertPeakResults.setStatus(_A)
_WanDs1ExtensionsBertAverageResult_Type=Integer32
_WanDs1ExtensionsBertAverageResult_Object=MibTableColumn
wanDs1ExtensionsBertAverageResult=_WanDs1ExtensionsBertAverageResult_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,13),_WanDs1ExtensionsBertAverageResult_Type())
wanDs1ExtensionsBertAverageResult.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertAverageResult.setStatus(_A)
class _WanDs1ExtensionsBertTestPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('patternOther',1),('pattern1s',2),('pattern63',3),('pattern511',4),('pattern2047',5),('pattern3in24',6),('patternQRSS',7)))
_WanDs1ExtensionsBertTestPattern_Type.__name__=_C
_WanDs1ExtensionsBertTestPattern_Object=MibTableColumn
wanDs1ExtensionsBertTestPattern=_WanDs1ExtensionsBertTestPattern_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,14),_WanDs1ExtensionsBertTestPattern_Type())
wanDs1ExtensionsBertTestPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsBertTestPattern.setStatus(_A)
_WanDs1ExtensionsBertSamplePeriod_Type=Integer32
_WanDs1ExtensionsBertSamplePeriod_Object=MibTableColumn
wanDs1ExtensionsBertSamplePeriod=_WanDs1ExtensionsBertSamplePeriod_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,15),_WanDs1ExtensionsBertSamplePeriod_Type())
wanDs1ExtensionsBertSamplePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsBertSamplePeriod.setStatus(_A)
_WanDs1ExtensionsBertNumPeriods_Type=Counter32
_WanDs1ExtensionsBertNumPeriods_Object=MibTableColumn
wanDs1ExtensionsBertNumPeriods=_WanDs1ExtensionsBertNumPeriods_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,16),_WanDs1ExtensionsBertNumPeriods_Type())
wanDs1ExtensionsBertNumPeriods.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertNumPeriods.setStatus(_A)
class _WanDs1ExtensionsBertTestTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WanDs1ExtensionsBertTestTraps_Type.__name__=_C
_WanDs1ExtensionsBertTestTraps_Object=MibTableColumn
wanDs1ExtensionsBertTestTraps=_WanDs1ExtensionsBertTestTraps_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,17),_WanDs1ExtensionsBertTestTraps_Type())
wanDs1ExtensionsBertTestTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:wanDs1ExtensionsBertTestTraps.setStatus(_A)
class _WanDs1ExtensionsBertDataStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('waitingForLink',2),('waitingForLoopback',3),('running',4)))
_WanDs1ExtensionsBertDataStatus_Type.__name__=_C
_WanDs1ExtensionsBertDataStatus_Object=MibTableColumn
wanDs1ExtensionsBertDataStatus=_WanDs1ExtensionsBertDataStatus_Object((1,3,6,1,4,1,52,4,1,2,7,1,2,1,1,18),_WanDs1ExtensionsBertDataStatus_Type())
wanDs1ExtensionsBertDataStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wanDs1ExtensionsBertDataStatus.setStatus(_A)
_CtWanRs232_ObjectIdentity=ObjectIdentity
ctWanRs232=_CtWanRs232_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,3))
_WanRs232ExtensionsTable_Object=MibTable
wanRs232ExtensionsTable=_WanRs232ExtensionsTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,3,1))
if mibBuilder.loadTexts:wanRs232ExtensionsTable.setStatus(_A)
_WanRs232ExtensionsEntry_Object=MibTableRow
wanRs232ExtensionsEntry=_WanRs232ExtensionsEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,3,1,1))
wanRs232ExtensionsEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:wanRs232ExtensionsEntry.setStatus(_A)
_WanRs232ExtensionsEntryIndex_Type=Integer32
_WanRs232ExtensionsEntryIndex_Object=MibTableColumn
wanRs232ExtensionsEntryIndex=_WanRs232ExtensionsEntryIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,3,1,1,1),_WanRs232ExtensionsEntryIndex_Type())
wanRs232ExtensionsEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wanRs232ExtensionsEntryIndex.setStatus(_A)
class _WanRs232ExtensionsCTSEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WanRs232ExtensionsCTSEnable_Type.__name__=_C
_WanRs232ExtensionsCTSEnable_Object=MibTableColumn
wanRs232ExtensionsCTSEnable=_WanRs232ExtensionsCTSEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,3,1,1,2),_WanRs232ExtensionsCTSEnable_Type())
wanRs232ExtensionsCTSEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanRs232ExtensionsCTSEnable.setStatus(_A)
class _WanRs232ExtensionsDSREnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WanRs232ExtensionsDSREnable_Type.__name__=_C
_WanRs232ExtensionsDSREnable_Object=MibTableColumn
wanRs232ExtensionsDSREnable=_WanRs232ExtensionsDSREnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,3,1,1,3),_WanRs232ExtensionsDSREnable_Type())
wanRs232ExtensionsDSREnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wanRs232ExtensionsDSREnable.setStatus(_A)
_CtFrDcp_ObjectIdentity=ObjectIdentity
ctFrDcp=_CtFrDcp_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,4))
_FrDcpCircuitTable_Object=MibTable
frDcpCircuitTable=_FrDcpCircuitTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1))
if mibBuilder.loadTexts:frDcpCircuitTable.setStatus(_A)
_FrDcpCircuitEntry_Object=MibTableRow
frDcpCircuitEntry=_FrDcpCircuitEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1))
frDcpCircuitEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:frDcpCircuitEntry.setStatus(_A)
_FrDcpCircuitIfIndex_Type=Index
_FrDcpCircuitIfIndex_Object=MibTableColumn
frDcpCircuitIfIndex=_FrDcpCircuitIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1,1),_FrDcpCircuitIfIndex_Type())
frDcpCircuitIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:frDcpCircuitIfIndex.setStatus(_A)
_FrDcpCircuitDlci_Type=DLCI
_FrDcpCircuitDlci_Object=MibTableColumn
frDcpCircuitDlci=_FrDcpCircuitDlci_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1,2),_FrDcpCircuitDlci_Type())
frDcpCircuitDlci.setMaxAccess(_B)
if mibBuilder.loadTexts:frDcpCircuitDlci.setStatus(_A)
class _FrDcpCircuitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_FrDcpCircuitEnable_Type.__name__=_C
_FrDcpCircuitEnable_Object=MibTableColumn
frDcpCircuitEnable=_FrDcpCircuitEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1,3),_FrDcpCircuitEnable_Type())
frDcpCircuitEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:frDcpCircuitEnable.setStatus(_A)
class _FrDcpCircuitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_FrDcpCircuitStatus_Type.__name__=_C
_FrDcpCircuitStatus_Object=MibTableColumn
frDcpCircuitStatus=_FrDcpCircuitStatus_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1,4),_FrDcpCircuitStatus_Type())
frDcpCircuitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:frDcpCircuitStatus.setStatus(_A)
class _FrDcpCircuitRatio_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_FrDcpCircuitRatio_Type.__name__=_M
_FrDcpCircuitRatio_Object=MibTableColumn
frDcpCircuitRatio=_FrDcpCircuitRatio_Object((1,3,6,1,4,1,52,4,1,2,7,1,4,1,1,5),_FrDcpCircuitRatio_Type())
frDcpCircuitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:frDcpCircuitRatio.setStatus(_A)
_CtDDS_ObjectIdentity=ObjectIdentity
ctDDS=_CtDDS_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,5))
_DdsConfigTable_Object=MibTable
ddsConfigTable=_DdsConfigTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1))
if mibBuilder.loadTexts:ddsConfigTable.setStatus(_A)
_DdsConfigEntry_Object=MibTableRow
ddsConfigEntry=_DdsConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1))
ddsConfigEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:ddsConfigEntry.setStatus(_A)
class _DdsLineIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DdsLineIndex_Type.__name__=_C
_DdsLineIndex_Object=MibTableColumn
ddsLineIndex=_DdsLineIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,1),_DdsLineIndex_Type())
ddsLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsLineIndex.setStatus(_A)
class _DdsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DdsIfIndex_Type.__name__=_C
_DdsIfIndex_Object=MibTableColumn
ddsIfIndex=_DdsIfIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,2),_DdsIfIndex_Type())
ddsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsIfIndex.setStatus(_A)
class _DdsLineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddsPri',1),('ddsCc',2)))
_DdsLineMode_Type.__name__=_C
_DdsLineMode_Object=MibTableColumn
ddsLineMode=_DdsLineMode_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,3),_DdsLineMode_Type())
ddsLineMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsLineMode.setStatus(_A)
class _DdsLineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ddsNone',1),('ddsJBZS',2),('otherLineCode',3)))
_DdsLineCoding_Type.__name__=_C
_DdsLineCoding_Object=MibTableColumn
ddsLineCoding=_DdsLineCoding_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,4),_DdsLineCoding_Type())
ddsLineCoding.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsLineCoding.setStatus(_A)
class _DdsLoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddsNoLoop',1),('ddsLineLoop',2)))
_DdsLoopbackConfig_Type.__name__=_C
_DdsLoopbackConfig_Object=MibTableColumn
ddsLoopbackConfig=_DdsLoopbackConfig_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,5),_DdsLoopbackConfig_Type())
ddsLoopbackConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsLoopbackConfig.setStatus(_A)
class _DdsLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ddsNoAlarm',1),('ddsLossOfSignal',2),('ddsOutOfService',3),('ddsOutOfFrame',4)))
_DdsLineStatus_Type.__name__=_C
_DdsLineStatus_Object=MibTableColumn
ddsLineStatus=_DdsLineStatus_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,6),_DdsLineStatus_Type())
ddsLineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsLineStatus.setStatus(_A)
class _DdsTxClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddsLoopTiming',1),('ddsLocalTiming',2)))
_DdsTxClockSource_Type.__name__=_C
_DdsTxClockSource_Object=MibTableColumn
ddsTxClockSource=_DdsTxClockSource_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,7),_DdsTxClockSource_Type())
ddsTxClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ddsTxClockSource.setStatus(_A)
_DdsPortInSpeed_Type=Integer32
_DdsPortInSpeed_Object=MibTableColumn
ddsPortInSpeed=_DdsPortInSpeed_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,8),_DdsPortInSpeed_Type())
ddsPortInSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsPortInSpeed.setStatus(_A)
_DdsPortOutSpeed_Type=Integer32
_DdsPortOutSpeed_Object=MibTableColumn
ddsPortOutSpeed=_DdsPortOutSpeed_Object((1,3,6,1,4,1,52,4,1,2,7,1,5,1,1,9),_DdsPortOutSpeed_Type())
ddsPortOutSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ddsPortOutSpeed.setStatus(_A)
_CtDs1Alarms_ObjectIdentity=ObjectIdentity
ctDs1Alarms=_CtDs1Alarms_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,6))
_Ds1AlarmsGlobalConfigGroup_ObjectIdentity=ObjectIdentity
ds1AlarmsGlobalConfigGroup=_Ds1AlarmsGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,6,1))
class _Ds1AlarmGlobalAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmGlobalAdmin_Type.__name__=_C
_Ds1AlarmGlobalAdmin_Object=MibScalar
ds1AlarmGlobalAdmin=_Ds1AlarmGlobalAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,1),_Ds1AlarmGlobalAdmin_Type())
ds1AlarmGlobalAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalAdmin.setStatus(_A)
class _Ds1AlarmGlobalAutoRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmGlobalAutoRecovery_Type.__name__=_C
_Ds1AlarmGlobalAutoRecovery_Object=MibScalar
ds1AlarmGlobalAutoRecovery=_Ds1AlarmGlobalAutoRecovery_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,2),_Ds1AlarmGlobalAutoRecovery_Type())
ds1AlarmGlobalAutoRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalAutoRecovery.setStatus(_A)
class _Ds1AlarmGlobalTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmGlobalTrapEnable_Type.__name__=_C
_Ds1AlarmGlobalTrapEnable_Object=MibScalar
ds1AlarmGlobalTrapEnable=_Ds1AlarmGlobalTrapEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,3),_Ds1AlarmGlobalTrapEnable_Type())
ds1AlarmGlobalTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalTrapEnable.setStatus(_A)
class _Ds1AlarmGlobalESCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_Ds1AlarmGlobalESCount_Type.__name__=_C
_Ds1AlarmGlobalESCount_Object=MibScalar
ds1AlarmGlobalESCount=_Ds1AlarmGlobalESCount_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,4),_Ds1AlarmGlobalESCount_Type())
ds1AlarmGlobalESCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalESCount.setStatus(_A)
class _Ds1AlarmGlobalESInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ds1AlarmGlobalESInterval_Type.__name__=_C
_Ds1AlarmGlobalESInterval_Object=MibScalar
ds1AlarmGlobalESInterval=_Ds1AlarmGlobalESInterval_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,5),_Ds1AlarmGlobalESInterval_Type())
ds1AlarmGlobalESInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalESInterval.setStatus(_A)
class _Ds1AlarmGlobalBPVErrorRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_Ds1AlarmGlobalBPVErrorRate_Type.__name__=_C
_Ds1AlarmGlobalBPVErrorRate_Object=MibScalar
ds1AlarmGlobalBPVErrorRate=_Ds1AlarmGlobalBPVErrorRate_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,6),_Ds1AlarmGlobalBPVErrorRate_Type())
ds1AlarmGlobalBPVErrorRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalBPVErrorRate.setStatus(_A)
class _Ds1AlarmGlobalBPVInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ds1AlarmGlobalBPVInterval_Type.__name__=_C
_Ds1AlarmGlobalBPVInterval_Object=MibScalar
ds1AlarmGlobalBPVInterval=_Ds1AlarmGlobalBPVInterval_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,7),_Ds1AlarmGlobalBPVInterval_Type())
ds1AlarmGlobalBPVInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalBPVInterval.setStatus(_A)
class _Ds1AlarmGlobalManualRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_a,1))
_Ds1AlarmGlobalManualRecovery_Type.__name__=_C
_Ds1AlarmGlobalManualRecovery_Object=MibScalar
ds1AlarmGlobalManualRecovery=_Ds1AlarmGlobalManualRecovery_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,1,8),_Ds1AlarmGlobalManualRecovery_Type())
ds1AlarmGlobalManualRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmGlobalManualRecovery.setStatus(_A)
_Ds1AlarmConfigTable_Object=MibTable
ds1AlarmConfigTable=_Ds1AlarmConfigTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2))
if mibBuilder.loadTexts:ds1AlarmConfigTable.setStatus(_A)
_Ds1AlarmConfigEntry_Object=MibTableRow
ds1AlarmConfigEntry=_Ds1AlarmConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1))
ds1AlarmConfigEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:ds1AlarmConfigEntry.setStatus(_A)
_Ds1PhysNum_Type=Integer32
_Ds1PhysNum_Object=MibTableColumn
ds1PhysNum=_Ds1PhysNum_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,1),_Ds1PhysNum_Type())
ds1PhysNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ds1PhysNum.setStatus(_A)
class _Ds1AlarmAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmAdmin_Type.__name__=_C
_Ds1AlarmAdmin_Object=MibTableColumn
ds1AlarmAdmin=_Ds1AlarmAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,2),_Ds1AlarmAdmin_Type())
ds1AlarmAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmAdmin.setStatus(_A)
class _Ds1AlarmAutoRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmAutoRecovery_Type.__name__=_C
_Ds1AlarmAutoRecovery_Object=MibTableColumn
ds1AlarmAutoRecovery=_Ds1AlarmAutoRecovery_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,3),_Ds1AlarmAutoRecovery_Type())
ds1AlarmAutoRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmAutoRecovery.setStatus(_A)
class _Ds1AlarmTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Ds1AlarmTrapEnable_Type.__name__=_C
_Ds1AlarmTrapEnable_Object=MibTableColumn
ds1AlarmTrapEnable=_Ds1AlarmTrapEnable_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,4),_Ds1AlarmTrapEnable_Type())
ds1AlarmTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmTrapEnable.setStatus(_A)
class _Ds1AlarmESCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_Ds1AlarmESCount_Type.__name__=_C
_Ds1AlarmESCount_Object=MibTableColumn
ds1AlarmESCount=_Ds1AlarmESCount_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,5),_Ds1AlarmESCount_Type())
ds1AlarmESCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmESCount.setStatus(_A)
class _Ds1AlarmESInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ds1AlarmESInterval_Type.__name__=_C
_Ds1AlarmESInterval_Object=MibTableColumn
ds1AlarmESInterval=_Ds1AlarmESInterval_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,6),_Ds1AlarmESInterval_Type())
ds1AlarmESInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmESInterval.setStatus(_A)
class _Ds1AlarmBPVErrorRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_Ds1AlarmBPVErrorRate_Type.__name__=_C
_Ds1AlarmBPVErrorRate_Object=MibTableColumn
ds1AlarmBPVErrorRate=_Ds1AlarmBPVErrorRate_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,7),_Ds1AlarmBPVErrorRate_Type())
ds1AlarmBPVErrorRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmBPVErrorRate.setStatus(_A)
class _Ds1AlarmBPVInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_Ds1AlarmBPVInterval_Type.__name__=_C
_Ds1AlarmBPVInterval_Object=MibTableColumn
ds1AlarmBPVInterval=_Ds1AlarmBPVInterval_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,8),_Ds1AlarmBPVInterval_Type())
ds1AlarmBPVInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmBPVInterval.setStatus(_A)
class _Ds1AlarmManualRecovery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_a,1))
_Ds1AlarmManualRecovery_Type.__name__=_C
_Ds1AlarmManualRecovery_Object=MibTableColumn
ds1AlarmManualRecovery=_Ds1AlarmManualRecovery_Object((1,3,6,1,4,1,52,4,1,2,7,1,6,2,1,9),_Ds1AlarmManualRecovery_Type())
ds1AlarmManualRecovery.setMaxAccess(_D)
if mibBuilder.loadTexts:ds1AlarmManualRecovery.setStatus(_A)
_CtIPPQFilters_ObjectIdentity=ObjectIdentity
ctIPPQFilters=_CtIPPQFilters_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,7))
_IpPQConfigGroup_ObjectIdentity=ObjectIdentity
ipPQConfigGroup=_IpPQConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,7,1))
class _IpPQAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpPQAdmin_Type.__name__=_C
_IpPQAdmin_Object=MibScalar
ipPQAdmin=_IpPQAdmin_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,1,1),_IpPQAdmin_Type())
ipPQAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:ipPQAdmin.setStatus(_A)
_IPPQMaxEntries_Type=Integer32
_IPPQMaxEntries_Object=MibScalar
iPPQMaxEntries=_IPPQMaxEntries_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,1,2),_IPPQMaxEntries_Type())
iPPQMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:iPPQMaxEntries.setStatus(_A)
_IPPQNumEntries_Type=Integer32
_IPPQNumEntries_Object=MibScalar
iPPQNumEntries=_IPPQNumEntries_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,1,3),_IPPQNumEntries_Type())
iPPQNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:iPPQNumEntries.setStatus(_A)
_IPPQAddAddress_Type=IpAddress
_IPPQAddAddress_Object=MibScalar
iPPQAddAddress=_IPPQAddAddress_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,1,4),_IPPQAddAddress_Type())
iPPQAddAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:iPPQAddAddress.setStatus(_A)
_IPPQDelAddress_Type=IpAddress
_IPPQDelAddress_Object=MibScalar
iPPQDelAddress=_IPPQDelAddress_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,1,5),_IPPQDelAddress_Type())
iPPQDelAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:iPPQDelAddress.setStatus(_A)
_IpPQAddressTable_Object=MibTable
ipPQAddressTable=_IpPQAddressTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,2))
if mibBuilder.loadTexts:ipPQAddressTable.setStatus(_A)
_IpPQAddressEntry_Object=MibTableRow
ipPQAddressEntry=_IpPQAddressEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,2,1))
ipPQAddressEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:ipPQAddressEntry.setStatus(_A)
class _IpPQAddressId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_IpPQAddressId_Type.__name__=_C
_IpPQAddressId_Object=MibTableColumn
ipPQAddressId=_IpPQAddressId_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,2,1,1),_IpPQAddressId_Type())
ipPQAddressId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipPQAddressId.setStatus(_A)
_IpPQIPAddress_Type=IpAddress
_IpPQIPAddress_Object=MibTableColumn
ipPQIPAddress=_IpPQIPAddress_Object((1,3,6,1,4,1,52,4,1,2,7,1,7,2,1,2),_IpPQIPAddress_Type())
ipPQIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipPQIPAddress.setStatus(_A)
_CtWanHDSLExt_ObjectIdentity=ObjectIdentity
ctWanHDSLExt=_CtWanHDSLExt_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,7,1,8))
_CtWanHDSLPerformance15mTable_Object=MibTable
ctWanHDSLPerformance15mTable=_CtWanHDSLPerformance15mTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1))
if mibBuilder.loadTexts:ctWanHDSLPerformance15mTable.setStatus(_A)
_CtWanHDSLPerformance15mEntry_Object=MibTableRow
ctWanHDSLPerformance15mEntry=_CtWanHDSLPerformance15mEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1))
ctWanHDSLPerformance15mEntry.setIndexNames((0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:ctWanHDSLPerformance15mEntry.setStatus(_A)
_CtWanHDSLPerformance15mConnIndex_Type=Integer32
_CtWanHDSLPerformance15mConnIndex_Object=MibTableColumn
ctWanHDSLPerformance15mConnIndex=_CtWanHDSLPerformance15mConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,1),_CtWanHDSLPerformance15mConnIndex_Type())
ctWanHDSLPerformance15mConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPerformance15mConnIndex.setStatus(_A)
_CtWanHDSLPerformance15mSlotIndex_Type=Integer32
_CtWanHDSLPerformance15mSlotIndex_Object=MibTableColumn
ctWanHDSLPerformance15mSlotIndex=_CtWanHDSLPerformance15mSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,2),_CtWanHDSLPerformance15mSlotIndex_Type())
ctWanHDSLPerformance15mSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPerformance15mSlotIndex.setStatus(_A)
_CtWanHDSLHLULoop1UAS15m_Type=Integer32
_CtWanHDSLHLULoop1UAS15m_Object=MibTableColumn
ctWanHDSLHLULoop1UAS15m=_CtWanHDSLHLULoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,3),_CtWanHDSLHLULoop1UAS15m_Type())
ctWanHDSLHLULoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop1UAS15m.setStatus(_A)
_CtWanHDSLHLULoop1ES15m_Type=Integer32
_CtWanHDSLHLULoop1ES15m_Object=MibTableColumn
ctWanHDSLHLULoop1ES15m=_CtWanHDSLHLULoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,4),_CtWanHDSLHLULoop1ES15m_Type())
ctWanHDSLHLULoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop1ES15m.setStatus(_A)
_CtWanHDSLHLULoop2UAS15m_Type=Integer32
_CtWanHDSLHLULoop2UAS15m_Object=MibTableColumn
ctWanHDSLHLULoop2UAS15m=_CtWanHDSLHLULoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,5),_CtWanHDSLHLULoop2UAS15m_Type())
ctWanHDSLHLULoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop2UAS15m.setStatus(_A)
_CtWanHDSLHLULoop2ES15m_Type=Integer32
_CtWanHDSLHLULoop2ES15m_Object=MibTableColumn
ctWanHDSLHLULoop2ES15m=_CtWanHDSLHLULoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,6),_CtWanHDSLHLULoop2ES15m_Type())
ctWanHDSLHLULoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop2ES15m.setStatus(_A)
_CtWanHDSLHRULoop1UAS15m_Type=Integer32
_CtWanHDSLHRULoop1UAS15m_Object=MibTableColumn
ctWanHDSLHRULoop1UAS15m=_CtWanHDSLHRULoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,7),_CtWanHDSLHRULoop1UAS15m_Type())
ctWanHDSLHRULoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop1UAS15m.setStatus(_A)
_CtWanHDSLHRULoop1ES15m_Type=Integer32
_CtWanHDSLHRULoop1ES15m_Object=MibTableColumn
ctWanHDSLHRULoop1ES15m=_CtWanHDSLHRULoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,8),_CtWanHDSLHRULoop1ES15m_Type())
ctWanHDSLHRULoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop1ES15m.setStatus(_A)
_CtWanHDSLHRULoop2UAS15m_Type=Integer32
_CtWanHDSLHRULoop2UAS15m_Object=MibTableColumn
ctWanHDSLHRULoop2UAS15m=_CtWanHDSLHRULoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,9),_CtWanHDSLHRULoop2UAS15m_Type())
ctWanHDSLHRULoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop2UAS15m.setStatus(_A)
_CtWanHDSLHRULoop2ES15m_Type=Integer32
_CtWanHDSLHRULoop2ES15m_Object=MibTableColumn
ctWanHDSLHRULoop2ES15m=_CtWanHDSLHRULoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,10),_CtWanHDSLHRULoop2ES15m_Type())
ctWanHDSLHRULoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop2ES15m.setStatus(_A)
_CtWanHDSLDb1NetworkLoop1UAS15m_Type=Integer32
_CtWanHDSLDb1NetworkLoop1UAS15m_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop1UAS15m=_CtWanHDSLDb1NetworkLoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,11),_CtWanHDSLDb1NetworkLoop1UAS15m_Type())
ctWanHDSLDb1NetworkLoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop1UAS15m.setStatus(_A)
_CtWanHDSLDb1NetworkLoop1ES15m_Type=Integer32
_CtWanHDSLDb1NetworkLoop1ES15m_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop1ES15m=_CtWanHDSLDb1NetworkLoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,12),_CtWanHDSLDb1NetworkLoop1ES15m_Type())
ctWanHDSLDb1NetworkLoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop1ES15m.setStatus(_A)
_CtWanHDSLDb1NetworkLoop2UAS15m_Type=Integer32
_CtWanHDSLDb1NetworkLoop2UAS15m_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop2UAS15m=_CtWanHDSLDb1NetworkLoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,13),_CtWanHDSLDb1NetworkLoop2UAS15m_Type())
ctWanHDSLDb1NetworkLoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop2UAS15m.setStatus(_A)
_CtWanHDSLDb1NetworkLoop2ES15m_Type=Integer32
_CtWanHDSLDb1NetworkLoop2ES15m_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop2ES15m=_CtWanHDSLDb1NetworkLoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,14),_CtWanHDSLDb1NetworkLoop2ES15m_Type())
ctWanHDSLDb1NetworkLoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop2ES15m.setStatus(_A)
_CtWanHDSLDb1CustomerLoop1UAS15m_Type=Integer32
_CtWanHDSLDb1CustomerLoop1UAS15m_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop1UAS15m=_CtWanHDSLDb1CustomerLoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,15),_CtWanHDSLDb1CustomerLoop1UAS15m_Type())
ctWanHDSLDb1CustomerLoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop1UAS15m.setStatus(_A)
_CtWanHDSLDb1CustomerLoop1ES15m_Type=Integer32
_CtWanHDSLDb1CustomerLoop1ES15m_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop1ES15m=_CtWanHDSLDb1CustomerLoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,16),_CtWanHDSLDb1CustomerLoop1ES15m_Type())
ctWanHDSLDb1CustomerLoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop1ES15m.setStatus(_A)
_CtWanHDSLDb1CustomerLoop2UAS15m_Type=Integer32
_CtWanHDSLDb1CustomerLoop2UAS15m_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop2UAS15m=_CtWanHDSLDb1CustomerLoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,17),_CtWanHDSLDb1CustomerLoop2UAS15m_Type())
ctWanHDSLDb1CustomerLoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop2UAS15m.setStatus(_A)
_CtWanHDSLDb1CustomerLoop2ES15m_Type=Integer32
_CtWanHDSLDb1CustomerLoop2ES15m_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop2ES15m=_CtWanHDSLDb1CustomerLoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,18),_CtWanHDSLDb1CustomerLoop2ES15m_Type())
ctWanHDSLDb1CustomerLoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop2ES15m.setStatus(_A)
_CtWanHDSLDb2NetworkLoop1UAS15m_Type=Integer32
_CtWanHDSLDb2NetworkLoop1UAS15m_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop1UAS15m=_CtWanHDSLDb2NetworkLoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,19),_CtWanHDSLDb2NetworkLoop1UAS15m_Type())
ctWanHDSLDb2NetworkLoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop1UAS15m.setStatus(_A)
_CtWanHDSLDb2NetworkLoop1ES15m_Type=Integer32
_CtWanHDSLDb2NetworkLoop1ES15m_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop1ES15m=_CtWanHDSLDb2NetworkLoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,20),_CtWanHDSLDb2NetworkLoop1ES15m_Type())
ctWanHDSLDb2NetworkLoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop1ES15m.setStatus(_A)
_CtWanHDSLDb2NetworkLoop2UAS15m_Type=Integer32
_CtWanHDSLDb2NetworkLoop2UAS15m_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop2UAS15m=_CtWanHDSLDb2NetworkLoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,21),_CtWanHDSLDb2NetworkLoop2UAS15m_Type())
ctWanHDSLDb2NetworkLoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop2UAS15m.setStatus(_A)
_CtWanHDSLDb2NetworkLoop2ES15m_Type=Integer32
_CtWanHDSLDb2NetworkLoop2ES15m_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop2ES15m=_CtWanHDSLDb2NetworkLoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,22),_CtWanHDSLDb2NetworkLoop2ES15m_Type())
ctWanHDSLDb2NetworkLoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop2ES15m.setStatus(_A)
_CtWanHDSLDb2CustomerLoop1UAS15m_Type=Integer32
_CtWanHDSLDb2CustomerLoop1UAS15m_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop1UAS15m=_CtWanHDSLDb2CustomerLoop1UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,23),_CtWanHDSLDb2CustomerLoop1UAS15m_Type())
ctWanHDSLDb2CustomerLoop1UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop1UAS15m.setStatus(_A)
_CtWanHDSLDb2CustomerLoop1ES15m_Type=Integer32
_CtWanHDSLDb2CustomerLoop1ES15m_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop1ES15m=_CtWanHDSLDb2CustomerLoop1ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,24),_CtWanHDSLDb2CustomerLoop1ES15m_Type())
ctWanHDSLDb2CustomerLoop1ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop1ES15m.setStatus(_A)
_CtWanHDSLDb2CustomerLoop2UAS15m_Type=Integer32
_CtWanHDSLDb2CustomerLoop2UAS15m_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop2UAS15m=_CtWanHDSLDb2CustomerLoop2UAS15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,25),_CtWanHDSLDb2CustomerLoop2UAS15m_Type())
ctWanHDSLDb2CustomerLoop2UAS15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop2UAS15m.setStatus(_A)
_CtWanHDSLDb2CustomerLoop2ES15m_Type=Integer32
_CtWanHDSLDb2CustomerLoop2ES15m_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop2ES15m=_CtWanHDSLDb2CustomerLoop2ES15m_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,1,1,26),_CtWanHDSLDb2CustomerLoop2ES15m_Type())
ctWanHDSLDb2CustomerLoop2ES15m.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop2ES15m.setStatus(_A)
_CtWanHDSLPerformance24hTable_Object=MibTable
ctWanHDSLPerformance24hTable=_CtWanHDSLPerformance24hTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2))
if mibBuilder.loadTexts:ctWanHDSLPerformance24hTable.setStatus(_A)
_CtWanHDSLPerformance24hEntry_Object=MibTableRow
ctWanHDSLPerformance24hEntry=_CtWanHDSLPerformance24hEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1))
ctWanHDSLPerformance24hEntry.setIndexNames((0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:ctWanHDSLPerformance24hEntry.setStatus(_A)
_CtWanHDSLPerformance24hConnIndex_Type=Integer32
_CtWanHDSLPerformance24hConnIndex_Object=MibTableColumn
ctWanHDSLPerformance24hConnIndex=_CtWanHDSLPerformance24hConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,1),_CtWanHDSLPerformance24hConnIndex_Type())
ctWanHDSLPerformance24hConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPerformance24hConnIndex.setStatus(_A)
_CtWanHDSLPerformance24hSlotIndex_Type=Integer32
_CtWanHDSLPerformance24hSlotIndex_Object=MibTableColumn
ctWanHDSLPerformance24hSlotIndex=_CtWanHDSLPerformance24hSlotIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,2),_CtWanHDSLPerformance24hSlotIndex_Type())
ctWanHDSLPerformance24hSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPerformance24hSlotIndex.setStatus(_A)
_CtWanHDSLHLULoop1UAS24h_Type=Integer32
_CtWanHDSLHLULoop1UAS24h_Object=MibTableColumn
ctWanHDSLHLULoop1UAS24h=_CtWanHDSLHLULoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,3),_CtWanHDSLHLULoop1UAS24h_Type())
ctWanHDSLHLULoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop1UAS24h.setStatus(_A)
_CtWanHDSLHLULoop1ES24h_Type=Integer32
_CtWanHDSLHLULoop1ES24h_Object=MibTableColumn
ctWanHDSLHLULoop1ES24h=_CtWanHDSLHLULoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,4),_CtWanHDSLHLULoop1ES24h_Type())
ctWanHDSLHLULoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop1ES24h.setStatus(_A)
_CtWanHDSLHLULoop2UAS24h_Type=Integer32
_CtWanHDSLHLULoop2UAS24h_Object=MibTableColumn
ctWanHDSLHLULoop2UAS24h=_CtWanHDSLHLULoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,5),_CtWanHDSLHLULoop2UAS24h_Type())
ctWanHDSLHLULoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop2UAS24h.setStatus(_A)
_CtWanHDSLHLULoop2ES24h_Type=Integer32
_CtWanHDSLHLULoop2ES24h_Object=MibTableColumn
ctWanHDSLHLULoop2ES24h=_CtWanHDSLHLULoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,6),_CtWanHDSLHLULoop2ES24h_Type())
ctWanHDSLHLULoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLULoop2ES24h.setStatus(_A)
_CtWanHDSLHRULoop1UAS24h_Type=Integer32
_CtWanHDSLHRULoop1UAS24h_Object=MibTableColumn
ctWanHDSLHRULoop1UAS24h=_CtWanHDSLHRULoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,7),_CtWanHDSLHRULoop1UAS24h_Type())
ctWanHDSLHRULoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop1UAS24h.setStatus(_A)
_CtWanHDSLHRULoop1ES24h_Type=Integer32
_CtWanHDSLHRULoop1ES24h_Object=MibTableColumn
ctWanHDSLHRULoop1ES24h=_CtWanHDSLHRULoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,8),_CtWanHDSLHRULoop1ES24h_Type())
ctWanHDSLHRULoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop1ES24h.setStatus(_A)
_CtWanHDSLHRULoop2UAS24h_Type=Integer32
_CtWanHDSLHRULoop2UAS24h_Object=MibTableColumn
ctWanHDSLHRULoop2UAS24h=_CtWanHDSLHRULoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,9),_CtWanHDSLHRULoop2UAS24h_Type())
ctWanHDSLHRULoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop2UAS24h.setStatus(_A)
_CtWanHDSLHRULoop2ES24h_Type=Integer32
_CtWanHDSLHRULoop2ES24h_Object=MibTableColumn
ctWanHDSLHRULoop2ES24h=_CtWanHDSLHRULoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,10),_CtWanHDSLHRULoop2ES24h_Type())
ctWanHDSLHRULoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRULoop2ES24h.setStatus(_A)
_CtWanHDSLDb1NetworkLoop1UAS24h_Type=Integer32
_CtWanHDSLDb1NetworkLoop1UAS24h_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop1UAS24h=_CtWanHDSLDb1NetworkLoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,11),_CtWanHDSLDb1NetworkLoop1UAS24h_Type())
ctWanHDSLDb1NetworkLoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop1UAS24h.setStatus(_A)
_CtWanHDSLDb1NetworkLoop1ES24h_Type=Integer32
_CtWanHDSLDb1NetworkLoop1ES24h_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop1ES24h=_CtWanHDSLDb1NetworkLoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,12),_CtWanHDSLDb1NetworkLoop1ES24h_Type())
ctWanHDSLDb1NetworkLoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop1ES24h.setStatus(_A)
_CtWanHDSLDb1NetworkLoop2UAS24h_Type=Integer32
_CtWanHDSLDb1NetworkLoop2UAS24h_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop2UAS24h=_CtWanHDSLDb1NetworkLoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,13),_CtWanHDSLDb1NetworkLoop2UAS24h_Type())
ctWanHDSLDb1NetworkLoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop2UAS24h.setStatus(_A)
_CtWanHDSLDb1NetworkLoop2ES24h_Type=Integer32
_CtWanHDSLDb1NetworkLoop2ES24h_Object=MibTableColumn
ctWanHDSLDb1NetworkLoop2ES24h=_CtWanHDSLDb1NetworkLoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,14),_CtWanHDSLDb1NetworkLoop2ES24h_Type())
ctWanHDSLDb1NetworkLoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1NetworkLoop2ES24h.setStatus(_A)
_CtWanHDSLDb1CustomerLoop1UAS24h_Type=Integer32
_CtWanHDSLDb1CustomerLoop1UAS24h_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop1UAS24h=_CtWanHDSLDb1CustomerLoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,15),_CtWanHDSLDb1CustomerLoop1UAS24h_Type())
ctWanHDSLDb1CustomerLoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop1UAS24h.setStatus(_A)
_CtWanHDSLDb1CustomerLoop1ES24h_Type=Integer32
_CtWanHDSLDb1CustomerLoop1ES24h_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop1ES24h=_CtWanHDSLDb1CustomerLoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,16),_CtWanHDSLDb1CustomerLoop1ES24h_Type())
ctWanHDSLDb1CustomerLoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop1ES24h.setStatus(_A)
_CtWanHDSLDb1CustomerLoop2UAS24h_Type=Integer32
_CtWanHDSLDb1CustomerLoop2UAS24h_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop2UAS24h=_CtWanHDSLDb1CustomerLoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,17),_CtWanHDSLDb1CustomerLoop2UAS24h_Type())
ctWanHDSLDb1CustomerLoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop2UAS24h.setStatus(_A)
_CtWanHDSLDb1CustomerLoop2ES24h_Type=Integer32
_CtWanHDSLDb1CustomerLoop2ES24h_Object=MibTableColumn
ctWanHDSLDb1CustomerLoop2ES24h=_CtWanHDSLDb1CustomerLoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,18),_CtWanHDSLDb1CustomerLoop2ES24h_Type())
ctWanHDSLDb1CustomerLoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb1CustomerLoop2ES24h.setStatus(_A)
_CtWanHDSLDb2NetworkLoop1UAS24h_Type=Integer32
_CtWanHDSLDb2NetworkLoop1UAS24h_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop1UAS24h=_CtWanHDSLDb2NetworkLoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,19),_CtWanHDSLDb2NetworkLoop1UAS24h_Type())
ctWanHDSLDb2NetworkLoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop1UAS24h.setStatus(_A)
_CtWanHDSLDb2NetworkLoop1ES24h_Type=Integer32
_CtWanHDSLDb2NetworkLoop1ES24h_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop1ES24h=_CtWanHDSLDb2NetworkLoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,20),_CtWanHDSLDb2NetworkLoop1ES24h_Type())
ctWanHDSLDb2NetworkLoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop1ES24h.setStatus(_A)
_CtWanHDSLDb2NetworkLoop2UAS24h_Type=Integer32
_CtWanHDSLDb2NetworkLoop2UAS24h_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop2UAS24h=_CtWanHDSLDb2NetworkLoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,21),_CtWanHDSLDb2NetworkLoop2UAS24h_Type())
ctWanHDSLDb2NetworkLoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop2UAS24h.setStatus(_A)
_CtWanHDSLDb2NetworkLoop2ES24h_Type=Integer32
_CtWanHDSLDb2NetworkLoop2ES24h_Object=MibTableColumn
ctWanHDSLDb2NetworkLoop2ES24h=_CtWanHDSLDb2NetworkLoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,22),_CtWanHDSLDb2NetworkLoop2ES24h_Type())
ctWanHDSLDb2NetworkLoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2NetworkLoop2ES24h.setStatus(_A)
_CtWanHDSLDb2CustomerLoop1UAS24h_Type=Integer32
_CtWanHDSLDb2CustomerLoop1UAS24h_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop1UAS24h=_CtWanHDSLDb2CustomerLoop1UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,23),_CtWanHDSLDb2CustomerLoop1UAS24h_Type())
ctWanHDSLDb2CustomerLoop1UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop1UAS24h.setStatus(_A)
_CtWanHDSLDb2CustomerLoop1ES24h_Type=Integer32
_CtWanHDSLDb2CustomerLoop1ES24h_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop1ES24h=_CtWanHDSLDb2CustomerLoop1ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,24),_CtWanHDSLDb2CustomerLoop1ES24h_Type())
ctWanHDSLDb2CustomerLoop1ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop1ES24h.setStatus(_A)
_CtWanHDSLDb2CustomerLoop2UAS24h_Type=Integer32
_CtWanHDSLDb2CustomerLoop2UAS24h_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop2UAS24h=_CtWanHDSLDb2CustomerLoop2UAS24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,25),_CtWanHDSLDb2CustomerLoop2UAS24h_Type())
ctWanHDSLDb2CustomerLoop2UAS24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop2UAS24h.setStatus(_A)
_CtWanHDSLDb2CustomerLoop2ES24h_Type=Integer32
_CtWanHDSLDb2CustomerLoop2ES24h_Object=MibTableColumn
ctWanHDSLDb2CustomerLoop2ES24h=_CtWanHDSLDb2CustomerLoop2ES24h_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,2,1,26),_CtWanHDSLDb2CustomerLoop2ES24h_Type())
ctWanHDSLDb2CustomerLoop2ES24h.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDb2CustomerLoop2ES24h.setStatus(_A)
_CtWanHDSLStatisticsTable_Object=MibTable
ctWanHDSLStatisticsTable=_CtWanHDSLStatisticsTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3))
if mibBuilder.loadTexts:ctWanHDSLStatisticsTable.setStatus(_A)
_CtWanHDSLStatisticsEntry_Object=MibTableRow
ctWanHDSLStatisticsEntry=_CtWanHDSLStatisticsEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1))
ctWanHDSLStatisticsEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:ctWanHDSLStatisticsEntry.setStatus(_A)
_CtWanHDSLStatisticsHLUConnIndex_Type=Integer32
_CtWanHDSLStatisticsHLUConnIndex_Object=MibTableColumn
ctWanHDSLStatisticsHLUConnIndex=_CtWanHDSLStatisticsHLUConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,1),_CtWanHDSLStatisticsHLUConnIndex_Type())
ctWanHDSLStatisticsHLUConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLStatisticsHLUConnIndex.setStatus(_A)
_CtWanHDSLSNRHLULoop1_Type=Integer32
_CtWanHDSLSNRHLULoop1_Object=MibTableColumn
ctWanHDSLSNRHLULoop1=_CtWanHDSLSNRHLULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,2),_CtWanHDSLSNRHLULoop1_Type())
ctWanHDSLSNRHLULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHLULoop1.setStatus(_A)
_CtWanHDSLSNRLowHLULoop1_Type=Integer32
_CtWanHDSLSNRLowHLULoop1_Object=MibTableColumn
ctWanHDSLSNRLowHLULoop1=_CtWanHDSLSNRLowHLULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,3),_CtWanHDSLSNRLowHLULoop1_Type())
ctWanHDSLSNRLowHLULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowHLULoop1.setStatus(_A)
_CtWanHDSLSNRHighHLULoop1_Type=Integer32
_CtWanHDSLSNRHighHLULoop1_Object=MibTableColumn
ctWanHDSLSNRHighHLULoop1=_CtWanHDSLSNRHighHLULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,4),_CtWanHDSLSNRHighHLULoop1_Type())
ctWanHDSLSNRHighHLULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighHLULoop1.setStatus(_A)
_CtWanHDSLSNRHLULoop2_Type=Integer32
_CtWanHDSLSNRHLULoop2_Object=MibTableColumn
ctWanHDSLSNRHLULoop2=_CtWanHDSLSNRHLULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,5),_CtWanHDSLSNRHLULoop2_Type())
ctWanHDSLSNRHLULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHLULoop2.setStatus(_A)
_CtWanHDSLSNRLowHLULoop2_Type=Integer32
_CtWanHDSLSNRLowHLULoop2_Object=MibTableColumn
ctWanHDSLSNRLowHLULoop2=_CtWanHDSLSNRLowHLULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,6),_CtWanHDSLSNRLowHLULoop2_Type())
ctWanHDSLSNRLowHLULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowHLULoop2.setStatus(_A)
_CtWanHDSLSNRHighHLULoop2_Type=Integer32
_CtWanHDSLSNRHighHLULoop2_Object=MibTableColumn
ctWanHDSLSNRHighHLULoop2=_CtWanHDSLSNRHighHLULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,7),_CtWanHDSLSNRHighHLULoop2_Type())
ctWanHDSLSNRHighHLULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighHLULoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationHLULoop1_Type=Integer32
_CtWanHDSLPulseAttenuationHLULoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationHLULoop1=_CtWanHDSLPulseAttenuationHLULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,8),_CtWanHDSLPulseAttenuationHLULoop1_Type())
ctWanHDSLPulseAttenuationHLULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationHLULoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationHLULoop2_Type=Integer32
_CtWanHDSLPulseAttenuationHLULoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationHLULoop2=_CtWanHDSLPulseAttenuationHLULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,9),_CtWanHDSLPulseAttenuationHLULoop2_Type())
ctWanHDSLPulseAttenuationHLULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationHLULoop2.setStatus(_A)
_CtWanHDSLBitStat1HLU_Type=Integer32
_CtWanHDSLBitStat1HLU_Object=MibTableColumn
ctWanHDSLBitStat1HLU=_CtWanHDSLBitStat1HLU_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,10),_CtWanHDSLBitStat1HLU_Type())
ctWanHDSLBitStat1HLU.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLBitStat1HLU.setStatus(_A)
_CtWanHDSLSNRHRULoop1_Type=Integer32
_CtWanHDSLSNRHRULoop1_Object=MibTableColumn
ctWanHDSLSNRHRULoop1=_CtWanHDSLSNRHRULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,11),_CtWanHDSLSNRHRULoop1_Type())
ctWanHDSLSNRHRULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHRULoop1.setStatus(_A)
_CtWanHDSLSNRLowHRULoop1_Type=Integer32
_CtWanHDSLSNRLowHRULoop1_Object=MibTableColumn
ctWanHDSLSNRLowHRULoop1=_CtWanHDSLSNRLowHRULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,12),_CtWanHDSLSNRLowHRULoop1_Type())
ctWanHDSLSNRLowHRULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowHRULoop1.setStatus(_A)
_CtWanHDSLSNRHighHRULoop1_Type=Integer32
_CtWanHDSLSNRHighHRULoop1_Object=MibTableColumn
ctWanHDSLSNRHighHRULoop1=_CtWanHDSLSNRHighHRULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,13),_CtWanHDSLSNRHighHRULoop1_Type())
ctWanHDSLSNRHighHRULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighHRULoop1.setStatus(_A)
_CtWanHDSLSNRHRULoop2_Type=Integer32
_CtWanHDSLSNRHRULoop2_Object=MibTableColumn
ctWanHDSLSNRHRULoop2=_CtWanHDSLSNRHRULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,14),_CtWanHDSLSNRHRULoop2_Type())
ctWanHDSLSNRHRULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHRULoop2.setStatus(_A)
_CtWanHDSLSNRLowHRULoop2_Type=Integer32
_CtWanHDSLSNRLowHRULoop2_Object=MibTableColumn
ctWanHDSLSNRLowHRULoop2=_CtWanHDSLSNRLowHRULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,15),_CtWanHDSLSNRLowHRULoop2_Type())
ctWanHDSLSNRLowHRULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowHRULoop2.setStatus(_A)
_CtWanHDSLSNRHighHRULoop2_Type=Integer32
_CtWanHDSLSNRHighHRULoop2_Object=MibTableColumn
ctWanHDSLSNRHighHRULoop2=_CtWanHDSLSNRHighHRULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,16),_CtWanHDSLSNRHighHRULoop2_Type())
ctWanHDSLSNRHighHRULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighHRULoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationHRULoop1_Type=Integer32
_CtWanHDSLPulseAttenuationHRULoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationHRULoop1=_CtWanHDSLPulseAttenuationHRULoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,17),_CtWanHDSLPulseAttenuationHRULoop1_Type())
ctWanHDSLPulseAttenuationHRULoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationHRULoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationHRULoop2_Type=Integer32
_CtWanHDSLPulseAttenuationHRULoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationHRULoop2=_CtWanHDSLPulseAttenuationHRULoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,18),_CtWanHDSLPulseAttenuationHRULoop2_Type())
ctWanHDSLPulseAttenuationHRULoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationHRULoop2.setStatus(_A)
_CtWanHDSLDs1FrameHRU_Type=Integer32
_CtWanHDSLDs1FrameHRU_Object=MibTableColumn
ctWanHDSLDs1FrameHRU=_CtWanHDSLDs1FrameHRU_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,19),_CtWanHDSLDs1FrameHRU_Type())
ctWanHDSLDs1FrameHRU.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLDs1FrameHRU.setStatus(_A)
_CtWanHDSLSNRDb1NetworkLoop1_Type=Integer32
_CtWanHDSLSNRDb1NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRDb1NetworkLoop1=_CtWanHDSLSNRDb1NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,20),_CtWanHDSLSNRDb1NetworkLoop1_Type())
ctWanHDSLSNRDb1NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb1NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRLowDb1NetworkLoop1_Type=Integer32
_CtWanHDSLSNRLowDb1NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRLowDb1NetworkLoop1=_CtWanHDSLSNRLowDb1NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,21),_CtWanHDSLSNRLowDb1NetworkLoop1_Type())
ctWanHDSLSNRLowDb1NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb1NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRHighDb1NetworkLoop1_Type=Integer32
_CtWanHDSLSNRHighDb1NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRHighDb1NetworkLoop1=_CtWanHDSLSNRHighDb1NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,22),_CtWanHDSLSNRHighDb1NetworkLoop1_Type())
ctWanHDSLSNRHighDb1NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb1NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRDb1NetworkLoop2_Type=Integer32
_CtWanHDSLSNRDb1NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRDb1NetworkLoop2=_CtWanHDSLSNRDb1NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,23),_CtWanHDSLSNRDb1NetworkLoop2_Type())
ctWanHDSLSNRDb1NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb1NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRLowDb1NetworkLoop2_Type=Integer32
_CtWanHDSLSNRLowDb1NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRLowDb1NetworkLoop2=_CtWanHDSLSNRLowDb1NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,24),_CtWanHDSLSNRLowDb1NetworkLoop2_Type())
ctWanHDSLSNRLowDb1NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb1NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRHighDb1NetworkLoop2_Type=Integer32
_CtWanHDSLSNRHighDb1NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRHighDb1NetworkLoop2=_CtWanHDSLSNRHighDb1NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,25),_CtWanHDSLSNRHighDb1NetworkLoop2_Type())
ctWanHDSLSNRHighDb1NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb1NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRDb1CustomerLoop1_Type=Integer32
_CtWanHDSLSNRDb1CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRDb1CustomerLoop1=_CtWanHDSLSNRDb1CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,26),_CtWanHDSLSNRDb1CustomerLoop1_Type())
ctWanHDSLSNRDb1CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb1CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRLowDb1CustomerLoop1_Type=Integer32
_CtWanHDSLSNRLowDb1CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRLowDb1CustomerLoop1=_CtWanHDSLSNRLowDb1CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,27),_CtWanHDSLSNRLowDb1CustomerLoop1_Type())
ctWanHDSLSNRLowDb1CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb1CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRHighDb1CustomerLoop1_Type=Integer32
_CtWanHDSLSNRHighDb1CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRHighDb1CustomerLoop1=_CtWanHDSLSNRHighDb1CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,28),_CtWanHDSLSNRHighDb1CustomerLoop1_Type())
ctWanHDSLSNRHighDb1CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb1CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRDb1CustomerLoop2_Type=Integer32
_CtWanHDSLSNRDb1CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRDb1CustomerLoop2=_CtWanHDSLSNRDb1CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,29),_CtWanHDSLSNRDb1CustomerLoop2_Type())
ctWanHDSLSNRDb1CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb1CustomerLoop2.setStatus(_A)
_CtWanHDSLSNRLowDb1CustomerLoop2_Type=Integer32
_CtWanHDSLSNRLowDb1CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRLowDb1CustomerLoop2=_CtWanHDSLSNRLowDb1CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,30),_CtWanHDSLSNRLowDb1CustomerLoop2_Type())
ctWanHDSLSNRLowDb1CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb1CustomerLoop2.setStatus(_A)
_CtWanHDSLSNRHighDb1CustomerLoop2_Type=Integer32
_CtWanHDSLSNRHighDb1CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRHighDb1CustomerLoop2=_CtWanHDSLSNRHighDb1CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,31),_CtWanHDSLSNRHighDb1CustomerLoop2_Type())
ctWanHDSLSNRHighDb1CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb1CustomerLoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Type=Integer32
_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb1NetworkLoop1=_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,32),_CtWanHDSLPulseAttenuationDb1NetworkLoop1_Type())
ctWanHDSLPulseAttenuationDb1NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb1NetworkLoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Type=Integer32
_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb1NetworkLoop2=_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,33),_CtWanHDSLPulseAttenuationDb1NetworkLoop2_Type())
ctWanHDSLPulseAttenuationDb1NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb1NetworkLoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Type=Integer32
_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb1CustomerLoop1=_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,34),_CtWanHDSLPulseAttenuationDb1CustomerLoop1_Type())
ctWanHDSLPulseAttenuationDb1CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb1CustomerLoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Type=Integer32
_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb1CustomerLoop2=_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,35),_CtWanHDSLPulseAttenuationDb1CustomerLoop2_Type())
ctWanHDSLPulseAttenuationDb1CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb1CustomerLoop2.setStatus(_A)
_CtWanHDSLSNRDb2NetworkLoop1_Type=Integer32
_CtWanHDSLSNRDb2NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRDb2NetworkLoop1=_CtWanHDSLSNRDb2NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,36),_CtWanHDSLSNRDb2NetworkLoop1_Type())
ctWanHDSLSNRDb2NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb2NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRLowDb2NetworkLoop1_Type=Integer32
_CtWanHDSLSNRLowDb2NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRLowDb2NetworkLoop1=_CtWanHDSLSNRLowDb2NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,37),_CtWanHDSLSNRLowDb2NetworkLoop1_Type())
ctWanHDSLSNRLowDb2NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb2NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRHighDb2NetworkLoop1_Type=Integer32
_CtWanHDSLSNRHighDb2NetworkLoop1_Object=MibTableColumn
ctWanHDSLSNRHighDb2NetworkLoop1=_CtWanHDSLSNRHighDb2NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,38),_CtWanHDSLSNRHighDb2NetworkLoop1_Type())
ctWanHDSLSNRHighDb2NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb2NetworkLoop1.setStatus(_A)
_CtWanHDSLSNRDb2NetworkLoop2_Type=Integer32
_CtWanHDSLSNRDb2NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRDb2NetworkLoop2=_CtWanHDSLSNRDb2NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,39),_CtWanHDSLSNRDb2NetworkLoop2_Type())
ctWanHDSLSNRDb2NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb2NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRLowDb2NetworkLoop2_Type=Integer32
_CtWanHDSLSNRLowDb2NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRLowDb2NetworkLoop2=_CtWanHDSLSNRLowDb2NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,40),_CtWanHDSLSNRLowDb2NetworkLoop2_Type())
ctWanHDSLSNRLowDb2NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb2NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRHighDb2NetworkLoop2_Type=Integer32
_CtWanHDSLSNRHighDb2NetworkLoop2_Object=MibTableColumn
ctWanHDSLSNRHighDb2NetworkLoop2=_CtWanHDSLSNRHighDb2NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,41),_CtWanHDSLSNRHighDb2NetworkLoop2_Type())
ctWanHDSLSNRHighDb2NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb2NetworkLoop2.setStatus(_A)
_CtWanHDSLSNRDb2CustomerLoop1_Type=Integer32
_CtWanHDSLSNRDb2CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRDb2CustomerLoop1=_CtWanHDSLSNRDb2CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,42),_CtWanHDSLSNRDb2CustomerLoop1_Type())
ctWanHDSLSNRDb2CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb2CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRLowDb2CustomerLoop1_Type=Integer32
_CtWanHDSLSNRLowDb2CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRLowDb2CustomerLoop1=_CtWanHDSLSNRLowDb2CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,43),_CtWanHDSLSNRLowDb2CustomerLoop1_Type())
ctWanHDSLSNRLowDb2CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb2CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRHighDb2CustomerLoop1_Type=Integer32
_CtWanHDSLSNRHighDb2CustomerLoop1_Object=MibTableColumn
ctWanHDSLSNRHighDb2CustomerLoop1=_CtWanHDSLSNRHighDb2CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,44),_CtWanHDSLSNRHighDb2CustomerLoop1_Type())
ctWanHDSLSNRHighDb2CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb2CustomerLoop1.setStatus(_A)
_CtWanHDSLSNRDb2CustomerLoop2_Type=Integer32
_CtWanHDSLSNRDb2CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRDb2CustomerLoop2=_CtWanHDSLSNRDb2CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,45),_CtWanHDSLSNRDb2CustomerLoop2_Type())
ctWanHDSLSNRDb2CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRDb2CustomerLoop2.setStatus(_A)
_CtWanHDSLSNRLowDb2CustomerLoop2_Type=Integer32
_CtWanHDSLSNRLowDb2CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRLowDb2CustomerLoop2=_CtWanHDSLSNRLowDb2CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,46),_CtWanHDSLSNRLowDb2CustomerLoop2_Type())
ctWanHDSLSNRLowDb2CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRLowDb2CustomerLoop2.setStatus(_A)
_CtWanHDSLSNRHighDb2CustomerLoop2_Type=Integer32
_CtWanHDSLSNRHighDb2CustomerLoop2_Object=MibTableColumn
ctWanHDSLSNRHighDb2CustomerLoop2=_CtWanHDSLSNRHighDb2CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,47),_CtWanHDSLSNRHighDb2CustomerLoop2_Type())
ctWanHDSLSNRHighDb2CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLSNRHighDb2CustomerLoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Type=Integer32
_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb2NetworkLoop1=_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,48),_CtWanHDSLPulseAttenuationDb2NetworkLoop1_Type())
ctWanHDSLPulseAttenuationDb2NetworkLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb2NetworkLoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Type=Integer32
_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb2NetworkLoop2=_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,49),_CtWanHDSLPulseAttenuationDb2NetworkLoop2_Type())
ctWanHDSLPulseAttenuationDb2NetworkLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb2NetworkLoop2.setStatus(_A)
_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Type=Integer32
_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb2CustomerLoop1=_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,50),_CtWanHDSLPulseAttenuationDb2CustomerLoop1_Type())
ctWanHDSLPulseAttenuationDb2CustomerLoop1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb2CustomerLoop1.setStatus(_A)
_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Type=Integer32
_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Object=MibTableColumn
ctWanHDSLPulseAttenuationDb2CustomerLoop2=_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,3,1,51),_CtWanHDSLPulseAttenuationDb2CustomerLoop2_Type())
ctWanHDSLPulseAttenuationDb2CustomerLoop2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLPulseAttenuationDb2CustomerLoop2.setStatus(_A)
_CtWanHDSLTestTable_Object=MibTable
ctWanHDSLTestTable=_CtWanHDSLTestTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4))
if mibBuilder.loadTexts:ctWanHDSLTestTable.setStatus(_A)
_CtWanHDSLTestEntry_Object=MibTableRow
ctWanHDSLTestEntry=_CtWanHDSLTestEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4,1))
ctWanHDSLTestEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:ctWanHDSLTestEntry.setStatus(_A)
_CtWanHDSLTestHLUConnIndex_Type=Integer32
_CtWanHDSLTestHLUConnIndex_Object=MibTableColumn
ctWanHDSLTestHLUConnIndex=_CtWanHDSLTestHLUConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4,1,1),_CtWanHDSLTestHLUConnIndex_Type())
ctWanHDSLTestHLUConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLTestHLUConnIndex.setStatus(_A)
_CtWanHDSLTestMode_Type=Integer32
_CtWanHDSLTestMode_Object=MibTableColumn
ctWanHDSLTestMode=_CtWanHDSLTestMode_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4,1,2),_CtWanHDSLTestMode_Type())
ctWanHDSLTestMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanHDSLTestMode.setStatus(_A)
_CtWanHDSLHLUTestResult_Type=Integer32
_CtWanHDSLHLUTestResult_Object=MibTableColumn
ctWanHDSLHLUTestResult=_CtWanHDSLHLUTestResult_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4,1,3),_CtWanHDSLHLUTestResult_Type())
ctWanHDSLHLUTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHLUTestResult.setStatus(_A)
_CtWanHDSLHRUTestResult_Type=Integer32
_CtWanHDSLHRUTestResult_Object=MibTableColumn
ctWanHDSLHRUTestResult=_CtWanHDSLHRUTestResult_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,4,1,4),_CtWanHDSLHRUTestResult_Type())
ctWanHDSLHRUTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLHRUTestResult.setStatus(_A)
_CtWanHDSLAlarmsTable_Object=MibTable
ctWanHDSLAlarmsTable=_CtWanHDSLAlarmsTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,5))
if mibBuilder.loadTexts:ctWanHDSLAlarmsTable.setStatus(_A)
_CtWanHDSLAlarmsEntry_Object=MibTableRow
ctWanHDSLAlarmsEntry=_CtWanHDSLAlarmsEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,5,1))
ctWanHDSLAlarmsEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:ctWanHDSLAlarmsEntry.setStatus(_A)
_CtWanHDSLAlarmsHLUConnIndex_Type=Integer32
_CtWanHDSLAlarmsHLUConnIndex_Object=MibTableColumn
ctWanHDSLAlarmsHLUConnIndex=_CtWanHDSLAlarmsHLUConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,5,1,1),_CtWanHDSLAlarmsHLUConnIndex_Type())
ctWanHDSLAlarmsHLUConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlarmsHLUConnIndex.setStatus(_A)
_CtWanHDSLAlarmsBackplane_Type=Integer32
_CtWanHDSLAlarmsBackplane_Object=MibTableColumn
ctWanHDSLAlarmsBackplane=_CtWanHDSLAlarmsBackplane_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,5,1,2),_CtWanHDSLAlarmsBackplane_Type())
ctWanHDSLAlarmsBackplane.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlarmsBackplane.setStatus(_A)
_CtWanHDSLAlarmsES_Type=Integer32
_CtWanHDSLAlarmsES_Object=MibTableColumn
ctWanHDSLAlarmsES=_CtWanHDSLAlarmsES_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,5,1,3),_CtWanHDSLAlarmsES_Type())
ctWanHDSLAlarmsES.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlarmsES.setStatus(_A)
_CtWanHDSLAlarmHistoryTable_Object=MibTable
ctWanHDSLAlarmHistoryTable=_CtWanHDSLAlarmHistoryTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6))
if mibBuilder.loadTexts:ctWanHDSLAlarmHistoryTable.setStatus(_A)
_CtWanHDSLAlarmHistoryEntry_Object=MibTableRow
ctWanHDSLAlarmHistoryEntry=_CtWanHDSLAlarmHistoryEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1))
ctWanHDSLAlarmHistoryEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:ctWanHDSLAlarmHistoryEntry.setStatus(_A)
_CtWanHDSLAlarmHistoryConnIndex_Type=Integer32
_CtWanHDSLAlarmHistoryConnIndex_Object=MibTableColumn
ctWanHDSLAlarmHistoryConnIndex=_CtWanHDSLAlarmHistoryConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,1),_CtWanHDSLAlarmHistoryConnIndex_Type())
ctWanHDSLAlarmHistoryConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlarmHistoryConnIndex.setStatus(_A)
class _CtWanHDSLAlHistLLOSFirst_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLLOSFirst_Type.__name__=_F
_CtWanHDSLAlHistLLOSFirst_Object=MibTableColumn
ctWanHDSLAlHistLLOSFirst=_CtWanHDSLAlHistLLOSFirst_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,2),_CtWanHDSLAlHistLLOSFirst_Type())
ctWanHDSLAlHistLLOSFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLLOSFirst.setStatus(_A)
class _CtWanHDSLAlHistLLOSLast_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLLOSLast_Type.__name__=_F
_CtWanHDSLAlHistLLOSLast_Object=MibTableColumn
ctWanHDSLAlHistLLOSLast=_CtWanHDSLAlHistLLOSLast_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,3),_CtWanHDSLAlHistLLOSLast_Type())
ctWanHDSLAlHistLLOSLast.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLLOSLast.setStatus(_A)
_CtWanHDSLAlHistLLOSCurrent_Type=Integer32
_CtWanHDSLAlHistLLOSCurrent_Object=MibTableColumn
ctWanHDSLAlHistLLOSCurrent=_CtWanHDSLAlHistLLOSCurrent_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,4),_CtWanHDSLAlHistLLOSCurrent_Type())
ctWanHDSLAlHistLLOSCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLLOSCurrent.setStatus(_A)
_CtWanHDSLAlHistLLOSCount_Type=Integer32
_CtWanHDSLAlHistLLOSCount_Object=MibTableColumn
ctWanHDSLAlHistLLOSCount=_CtWanHDSLAlHistLLOSCount_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,5),_CtWanHDSLAlHistLLOSCount_Type())
ctWanHDSLAlHistLLOSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLLOSCount.setStatus(_A)
class _CtWanHDSLAlHistRLOSFirst_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistRLOSFirst_Type.__name__=_F
_CtWanHDSLAlHistRLOSFirst_Object=MibTableColumn
ctWanHDSLAlHistRLOSFirst=_CtWanHDSLAlHistRLOSFirst_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,6),_CtWanHDSLAlHistRLOSFirst_Type())
ctWanHDSLAlHistRLOSFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistRLOSFirst.setStatus(_A)
class _CtWanHDSLAlHistRLOSLast_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistRLOSLast_Type.__name__=_F
_CtWanHDSLAlHistRLOSLast_Object=MibTableColumn
ctWanHDSLAlHistRLOSLast=_CtWanHDSLAlHistRLOSLast_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,7),_CtWanHDSLAlHistRLOSLast_Type())
ctWanHDSLAlHistRLOSLast.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistRLOSLast.setStatus(_A)
_CtWanHDSLAlHistRLOSCurrent_Type=Integer32
_CtWanHDSLAlHistRLOSCurrent_Object=MibTableColumn
ctWanHDSLAlHistRLOSCurrent=_CtWanHDSLAlHistRLOSCurrent_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,8),_CtWanHDSLAlHistRLOSCurrent_Type())
ctWanHDSLAlHistRLOSCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistRLOSCurrent.setStatus(_A)
_CtWanHDSLAlHistRLOSCount_Type=Integer32
_CtWanHDSLAlHistRLOSCount_Object=MibTableColumn
ctWanHDSLAlHistRLOSCount=_CtWanHDSLAlHistRLOSCount_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,9),_CtWanHDSLAlHistRLOSCount_Type())
ctWanHDSLAlHistRLOSCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistRLOSCount.setStatus(_A)
class _CtWanHDSLAlHistLOSW1First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLOSW1First_Type.__name__=_F
_CtWanHDSLAlHistLOSW1First_Object=MibTableColumn
ctWanHDSLAlHistLOSW1First=_CtWanHDSLAlHistLOSW1First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,10),_CtWanHDSLAlHistLOSW1First_Type())
ctWanHDSLAlHistLOSW1First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW1First.setStatus(_A)
class _CtWanHDSLAlHistLOSW1Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLOSW1Last_Type.__name__=_F
_CtWanHDSLAlHistLOSW1Last_Object=MibTableColumn
ctWanHDSLAlHistLOSW1Last=_CtWanHDSLAlHistLOSW1Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,11),_CtWanHDSLAlHistLOSW1Last_Type())
ctWanHDSLAlHistLOSW1Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW1Last.setStatus(_A)
_CtWanHDSLAlHistLOSW1Current_Type=Integer32
_CtWanHDSLAlHistLOSW1Current_Object=MibTableColumn
ctWanHDSLAlHistLOSW1Current=_CtWanHDSLAlHistLOSW1Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,12),_CtWanHDSLAlHistLOSW1Current_Type())
ctWanHDSLAlHistLOSW1Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW1Current.setStatus(_A)
_CtWanHDSLAlHistLOSW1Count_Type=Integer32
_CtWanHDSLAlHistLOSW1Count_Object=MibTableColumn
ctWanHDSLAlHistLOSW1Count=_CtWanHDSLAlHistLOSW1Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,13),_CtWanHDSLAlHistLOSW1Count_Type())
ctWanHDSLAlHistLOSW1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW1Count.setStatus(_A)
class _CtWanHDSLAlHistLOSW2First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLOSW2First_Type.__name__=_F
_CtWanHDSLAlHistLOSW2First_Object=MibTableColumn
ctWanHDSLAlHistLOSW2First=_CtWanHDSLAlHistLOSW2First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,14),_CtWanHDSLAlHistLOSW2First_Type())
ctWanHDSLAlHistLOSW2First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW2First.setStatus(_A)
class _CtWanHDSLAlHistLOSW2Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistLOSW2Last_Type.__name__=_F
_CtWanHDSLAlHistLOSW2Last_Object=MibTableColumn
ctWanHDSLAlHistLOSW2Last=_CtWanHDSLAlHistLOSW2Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,15),_CtWanHDSLAlHistLOSW2Last_Type())
ctWanHDSLAlHistLOSW2Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW2Last.setStatus(_A)
_CtWanHDSLAlHistLOSW2Current_Type=Integer32
_CtWanHDSLAlHistLOSW2Current_Object=MibTableColumn
ctWanHDSLAlHistLOSW2Current=_CtWanHDSLAlHistLOSW2Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,16),_CtWanHDSLAlHistLOSW2Current_Type())
ctWanHDSLAlHistLOSW2Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW2Current.setStatus(_A)
_CtWanHDSLAlHistLOSW2Count_Type=Integer32
_CtWanHDSLAlHistLOSW2Count_Object=MibTableColumn
ctWanHDSLAlHistLOSW2Count=_CtWanHDSLAlHistLOSW2Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,17),_CtWanHDSLAlHistLOSW2Count_Type())
ctWanHDSLAlHistLOSW2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistLOSW2Count.setStatus(_A)
class _CtWanHDSLAlHistES1First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistES1First_Type.__name__=_F
_CtWanHDSLAlHistES1First_Object=MibTableColumn
ctWanHDSLAlHistES1First=_CtWanHDSLAlHistES1First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,18),_CtWanHDSLAlHistES1First_Type())
ctWanHDSLAlHistES1First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES1First.setStatus(_A)
class _CtWanHDSLAlHistES1Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistES1Last_Type.__name__=_F
_CtWanHDSLAlHistES1Last_Object=MibTableColumn
ctWanHDSLAlHistES1Last=_CtWanHDSLAlHistES1Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,19),_CtWanHDSLAlHistES1Last_Type())
ctWanHDSLAlHistES1Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES1Last.setStatus(_A)
_CtWanHDSLAlHistES1Current_Type=Integer32
_CtWanHDSLAlHistES1Current_Object=MibTableColumn
ctWanHDSLAlHistES1Current=_CtWanHDSLAlHistES1Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,20),_CtWanHDSLAlHistES1Current_Type())
ctWanHDSLAlHistES1Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES1Current.setStatus(_A)
_CtWanHDSLAlHistES1Count_Type=Integer32
_CtWanHDSLAlHistES1Count_Object=MibTableColumn
ctWanHDSLAlHistES1Count=_CtWanHDSLAlHistES1Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,21),_CtWanHDSLAlHistES1Count_Type())
ctWanHDSLAlHistES1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES1Count.setStatus(_A)
class _CtWanHDSLAlHistES2First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistES2First_Type.__name__=_F
_CtWanHDSLAlHistES2First_Object=MibTableColumn
ctWanHDSLAlHistES2First=_CtWanHDSLAlHistES2First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,22),_CtWanHDSLAlHistES2First_Type())
ctWanHDSLAlHistES2First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES2First.setStatus(_A)
class _CtWanHDSLAlHistES2Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistES2Last_Type.__name__=_F
_CtWanHDSLAlHistES2Last_Object=MibTableColumn
ctWanHDSLAlHistES2Last=_CtWanHDSLAlHistES2Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,23),_CtWanHDSLAlHistES2Last_Type())
ctWanHDSLAlHistES2Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES2Last.setStatus(_A)
_CtWanHDSLAlHistES2Current_Type=Integer32
_CtWanHDSLAlHistES2Current_Object=MibTableColumn
ctWanHDSLAlHistES2Current=_CtWanHDSLAlHistES2Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,24),_CtWanHDSLAlHistES2Current_Type())
ctWanHDSLAlHistES2Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES2Current.setStatus(_A)
_CtWanHDSLAlHistES2Count_Type=Integer32
_CtWanHDSLAlHistES2Count_Object=MibTableColumn
ctWanHDSLAlHistES2Count=_CtWanHDSLAlHistES2Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,25),_CtWanHDSLAlHistES2Count_Type())
ctWanHDSLAlHistES2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistES2Count.setStatus(_A)
class _CtWanHDSLAlHistMargin1First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistMargin1First_Type.__name__=_F
_CtWanHDSLAlHistMargin1First_Object=MibTableColumn
ctWanHDSLAlHistMargin1First=_CtWanHDSLAlHistMargin1First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,26),_CtWanHDSLAlHistMargin1First_Type())
ctWanHDSLAlHistMargin1First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin1First.setStatus(_A)
class _CtWanHDSLAlHistMargin1Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistMargin1Last_Type.__name__=_F
_CtWanHDSLAlHistMargin1Last_Object=MibTableColumn
ctWanHDSLAlHistMargin1Last=_CtWanHDSLAlHistMargin1Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,27),_CtWanHDSLAlHistMargin1Last_Type())
ctWanHDSLAlHistMargin1Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin1Last.setStatus(_A)
_CtWanHDSLAlHistMargin1Current_Type=Integer32
_CtWanHDSLAlHistMargin1Current_Object=MibTableColumn
ctWanHDSLAlHistMargin1Current=_CtWanHDSLAlHistMargin1Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,28),_CtWanHDSLAlHistMargin1Current_Type())
ctWanHDSLAlHistMargin1Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin1Current.setStatus(_A)
_CtWanHDSLAlHistMargin1Count_Type=Integer32
_CtWanHDSLAlHistMargin1Count_Object=MibTableColumn
ctWanHDSLAlHistMargin1Count=_CtWanHDSLAlHistMargin1Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,29),_CtWanHDSLAlHistMargin1Count_Type())
ctWanHDSLAlHistMargin1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin1Count.setStatus(_A)
class _CtWanHDSLAlHistMargin2First_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistMargin2First_Type.__name__=_F
_CtWanHDSLAlHistMargin2First_Object=MibTableColumn
ctWanHDSLAlHistMargin2First=_CtWanHDSLAlHistMargin2First_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,30),_CtWanHDSLAlHistMargin2First_Type())
ctWanHDSLAlHistMargin2First.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin2First.setStatus(_A)
class _CtWanHDSLAlHistMargin2Last_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistMargin2Last_Type.__name__=_F
_CtWanHDSLAlHistMargin2Last_Object=MibTableColumn
ctWanHDSLAlHistMargin2Last=_CtWanHDSLAlHistMargin2Last_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,31),_CtWanHDSLAlHistMargin2Last_Type())
ctWanHDSLAlHistMargin2Last.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin2Last.setStatus(_A)
_CtWanHDSLAlHistMargin2Current_Type=Integer32
_CtWanHDSLAlHistMargin2Current_Object=MibTableColumn
ctWanHDSLAlHistMargin2Current=_CtWanHDSLAlHistMargin2Current_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,32),_CtWanHDSLAlHistMargin2Current_Type())
ctWanHDSLAlHistMargin2Current.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin2Current.setStatus(_A)
_CtWanHDSLAlHistMargin2Count_Type=Integer32
_CtWanHDSLAlHistMargin2Count_Object=MibTableColumn
ctWanHDSLAlHistMargin2Count=_CtWanHDSLAlHistMargin2Count_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,33),_CtWanHDSLAlHistMargin2Count_Type())
ctWanHDSLAlHistMargin2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistMargin2Count.setStatus(_A)
class _CtWanHDSLAlHistCleared_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CtWanHDSLAlHistCleared_Type.__name__=_F
_CtWanHDSLAlHistCleared_Object=MibTableColumn
ctWanHDSLAlHistCleared=_CtWanHDSLAlHistCleared_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,34),_CtWanHDSLAlHistCleared_Type())
ctWanHDSLAlHistCleared.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLAlHistCleared.setStatus(_A)
_CtWanHDSLAlHistClearit_Type=Integer32
_CtWanHDSLAlHistClearit_Object=MibTableColumn
ctWanHDSLAlHistClearit=_CtWanHDSLAlHistClearit_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,6,1,35),_CtWanHDSLAlHistClearit_Type())
ctWanHDSLAlHistClearit.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanHDSLAlHistClearit.setStatus(_A)
_CtWanHDSLLoopbacksTable_Object=MibTable
ctWanHDSLLoopbacksTable=_CtWanHDSLLoopbacksTable_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,7))
if mibBuilder.loadTexts:ctWanHDSLLoopbacksTable.setStatus(_A)
_CtWanHDSLLoopbacksEntry_Object=MibTableRow
ctWanHDSLLoopbacksEntry=_CtWanHDSLLoopbacksEntry_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,7,1))
ctWanHDSLLoopbacksEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:ctWanHDSLLoopbacksEntry.setStatus(_A)
_CtWanHDSLLoopbacksHLUConnIndex_Type=Integer32
_CtWanHDSLLoopbacksHLUConnIndex_Object=MibTableColumn
ctWanHDSLLoopbacksHLUConnIndex=_CtWanHDSLLoopbacksHLUConnIndex_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,7,1,1),_CtWanHDSLLoopbacksHLUConnIndex_Type())
ctWanHDSLLoopbacksHLUConnIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLLoopbacksHLUConnIndex.setStatus(_A)
_CtWanHDSLLoopbacksAdminType_Type=Integer32
_CtWanHDSLLoopbacksAdminType_Object=MibTableColumn
ctWanHDSLLoopbacksAdminType=_CtWanHDSLLoopbacksAdminType_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,7,1,2),_CtWanHDSLLoopbacksAdminType_Type())
ctWanHDSLLoopbacksAdminType.setMaxAccess(_D)
if mibBuilder.loadTexts:ctWanHDSLLoopbacksAdminType.setStatus(_A)
_CtWanHDSLLoopbacksOperType_Type=Integer32
_CtWanHDSLLoopbacksOperType_Object=MibTableColumn
ctWanHDSLLoopbacksOperType=_CtWanHDSLLoopbacksOperType_Object((1,3,6,1,4,1,52,4,1,2,7,1,8,7,1,3),_CtWanHDSLLoopbacksOperType_Type())
ctWanHDSLLoopbacksOperType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctWanHDSLLoopbacksOperType.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Index':Index,'DLCI':DLCI,'ctWanConnection':ctWanConnection,'wanNumConnections':wanNumConnections,'wanConnTable':wanConnTable,'wanConnEntry':wanConnEntry,_O:wanConnIndex,'wanConnNumPhysPorts':wanConnNumPhysPorts,'wanConnDefaultPhysPort':wanConnDefaultPhysPort,'wanConnActivePhysPort':wanConnActivePhysPort,'wanPhysPortTable':wanPhysPortTable,'wanPhysPortEntry':wanPhysPortEntry,_P:wanPhysPortConnectionIndex,_Q:wanPhysPortIndex,'wanPhysPortType':wanPhysPortType,'wanPhysPortSpecificMib':wanPhysPortSpecificMib,'wanInterfaceTable':wanInterfaceTable,'wanInterfaceEntry':wanInterfaceEntry,_R:wanInterfaceConnectionIndex,_S:wanInterfacePhysPortIndex,_T:wanInterfaceEntryIndex,'wanInterfaceEntryIfIndex':wanInterfaceEntryIfIndex,'wanInterfaceEntryProtocol':wanInterfaceEntryProtocol,'wanInterfaceEntryCompression':wanInterfaceEntryCompression,'wanInterfaceEntryMTU':wanInterfaceEntryMTU,'wanInterfaceEntryLineCoding':wanInterfaceEntryLineCoding,'wanInterfaceEntryCrcLength':wanInterfaceEntryCrcLength,'wanInterfaceEntryLexProtocolEnable':wanInterfaceEntryLexProtocolEnable,'wanInterfaceEntryLexProtocolStatus':wanInterfaceEntryLexProtocolStatus,'wanInterfaceEntryCompRatio':wanInterfaceEntryCompRatio,'wanInterfaceEntryCompStatus':wanInterfaceEntryCompStatus,'wanInterfaceEntryBackUpIfEnable':wanInterfaceEntryBackUpIfEnable,'ctWanDs1':ctWanDs1,'wanDs1ExtensionsTable':wanDs1ExtensionsTable,'wanDs1ExtensionsEntry':wanDs1ExtensionsEntry,_V:wanDs1ExtensionsEntryIndex,'wanDs1ExtensionsNumInterfaces':wanDs1ExtensionsNumInterfaces,'wanDs1ExtensionsToggleFracTable':wanDs1ExtensionsToggleFracTable,'wanDs1ExtensionsLineBuildOut':wanDs1ExtensionsLineBuildOut,'wanDs1ExtensionsCFADuration':wanDs1ExtensionsCFADuration,'wanDs1ExtensionsDIEnable':wanDs1ExtensionsDIEnable,'wanDs1ExtensionsTotalValidIntervals':wanDs1ExtensionsTotalValidIntervals,'wanDs1ExtensionsBertTestMode':wanDs1ExtensionsBertTestMode,'wanDs1ExtensionsBertRun':wanDs1ExtensionsBertRun,'wanDs1ExtensionsBertCurrentResults':wanDs1ExtensionsBertCurrentResults,'wanDs1ExtensionsBertCumulativeResults':wanDs1ExtensionsBertCumulativeResults,'wanDs1ExtensionsBertPeakResults':wanDs1ExtensionsBertPeakResults,'wanDs1ExtensionsBertAverageResult':wanDs1ExtensionsBertAverageResult,'wanDs1ExtensionsBertTestPattern':wanDs1ExtensionsBertTestPattern,'wanDs1ExtensionsBertSamplePeriod':wanDs1ExtensionsBertSamplePeriod,'wanDs1ExtensionsBertNumPeriods':wanDs1ExtensionsBertNumPeriods,'wanDs1ExtensionsBertTestTraps':wanDs1ExtensionsBertTestTraps,'wanDs1ExtensionsBertDataStatus':wanDs1ExtensionsBertDataStatus,'ctWanRs232':ctWanRs232,'wanRs232ExtensionsTable':wanRs232ExtensionsTable,'wanRs232ExtensionsEntry':wanRs232ExtensionsEntry,_W:wanRs232ExtensionsEntryIndex,'wanRs232ExtensionsCTSEnable':wanRs232ExtensionsCTSEnable,'wanRs232ExtensionsDSREnable':wanRs232ExtensionsDSREnable,'ctFrDcp':ctFrDcp,'frDcpCircuitTable':frDcpCircuitTable,'frDcpCircuitEntry':frDcpCircuitEntry,_X:frDcpCircuitIfIndex,_Y:frDcpCircuitDlci,'frDcpCircuitEnable':frDcpCircuitEnable,'frDcpCircuitStatus':frDcpCircuitStatus,'frDcpCircuitRatio':frDcpCircuitRatio,'ctDDS':ctDDS,'ddsConfigTable':ddsConfigTable,'ddsConfigEntry':ddsConfigEntry,_Z:ddsLineIndex,'ddsIfIndex':ddsIfIndex,'ddsLineMode':ddsLineMode,'ddsLineCoding':ddsLineCoding,'ddsLoopbackConfig':ddsLoopbackConfig,'ddsLineStatus':ddsLineStatus,'ddsTxClockSource':ddsTxClockSource,'ddsPortInSpeed':ddsPortInSpeed,'ddsPortOutSpeed':ddsPortOutSpeed,'ctDs1Alarms':ctDs1Alarms,'ds1AlarmsGlobalConfigGroup':ds1AlarmsGlobalConfigGroup,'ds1AlarmGlobalAdmin':ds1AlarmGlobalAdmin,'ds1AlarmGlobalAutoRecovery':ds1AlarmGlobalAutoRecovery,'ds1AlarmGlobalTrapEnable':ds1AlarmGlobalTrapEnable,'ds1AlarmGlobalESCount':ds1AlarmGlobalESCount,'ds1AlarmGlobalESInterval':ds1AlarmGlobalESInterval,'ds1AlarmGlobalBPVErrorRate':ds1AlarmGlobalBPVErrorRate,'ds1AlarmGlobalBPVInterval':ds1AlarmGlobalBPVInterval,'ds1AlarmGlobalManualRecovery':ds1AlarmGlobalManualRecovery,'ds1AlarmConfigTable':ds1AlarmConfigTable,'ds1AlarmConfigEntry':ds1AlarmConfigEntry,_b:ds1PhysNum,'ds1AlarmAdmin':ds1AlarmAdmin,'ds1AlarmAutoRecovery':ds1AlarmAutoRecovery,'ds1AlarmTrapEnable':ds1AlarmTrapEnable,'ds1AlarmESCount':ds1AlarmESCount,'ds1AlarmESInterval':ds1AlarmESInterval,'ds1AlarmBPVErrorRate':ds1AlarmBPVErrorRate,'ds1AlarmBPVInterval':ds1AlarmBPVInterval,'ds1AlarmManualRecovery':ds1AlarmManualRecovery,'ctIPPQFilters':ctIPPQFilters,'ipPQConfigGroup':ipPQConfigGroup,'ipPQAdmin':ipPQAdmin,'iPPQMaxEntries':iPPQMaxEntries,'iPPQNumEntries':iPPQNumEntries,'iPPQAddAddress':iPPQAddAddress,'iPPQDelAddress':iPPQDelAddress,'ipPQAddressTable':ipPQAddressTable,'ipPQAddressEntry':ipPQAddressEntry,_c:ipPQAddressId,'ipPQIPAddress':ipPQIPAddress,'ctWanHDSLExt':ctWanHDSLExt,'ctWanHDSLPerformance15mTable':ctWanHDSLPerformance15mTable,'ctWanHDSLPerformance15mEntry':ctWanHDSLPerformance15mEntry,_d:ctWanHDSLPerformance15mConnIndex,_e:ctWanHDSLPerformance15mSlotIndex,'ctWanHDSLHLULoop1UAS15m':ctWanHDSLHLULoop1UAS15m,'ctWanHDSLHLULoop1ES15m':ctWanHDSLHLULoop1ES15m,'ctWanHDSLHLULoop2UAS15m':ctWanHDSLHLULoop2UAS15m,'ctWanHDSLHLULoop2ES15m':ctWanHDSLHLULoop2ES15m,'ctWanHDSLHRULoop1UAS15m':ctWanHDSLHRULoop1UAS15m,'ctWanHDSLHRULoop1ES15m':ctWanHDSLHRULoop1ES15m,'ctWanHDSLHRULoop2UAS15m':ctWanHDSLHRULoop2UAS15m,'ctWanHDSLHRULoop2ES15m':ctWanHDSLHRULoop2ES15m,'ctWanHDSLDb1NetworkLoop1UAS15m':ctWanHDSLDb1NetworkLoop1UAS15m,'ctWanHDSLDb1NetworkLoop1ES15m':ctWanHDSLDb1NetworkLoop1ES15m,'ctWanHDSLDb1NetworkLoop2UAS15m':ctWanHDSLDb1NetworkLoop2UAS15m,'ctWanHDSLDb1NetworkLoop2ES15m':ctWanHDSLDb1NetworkLoop2ES15m,'ctWanHDSLDb1CustomerLoop1UAS15m':ctWanHDSLDb1CustomerLoop1UAS15m,'ctWanHDSLDb1CustomerLoop1ES15m':ctWanHDSLDb1CustomerLoop1ES15m,'ctWanHDSLDb1CustomerLoop2UAS15m':ctWanHDSLDb1CustomerLoop2UAS15m,'ctWanHDSLDb1CustomerLoop2ES15m':ctWanHDSLDb1CustomerLoop2ES15m,'ctWanHDSLDb2NetworkLoop1UAS15m':ctWanHDSLDb2NetworkLoop1UAS15m,'ctWanHDSLDb2NetworkLoop1ES15m':ctWanHDSLDb2NetworkLoop1ES15m,'ctWanHDSLDb2NetworkLoop2UAS15m':ctWanHDSLDb2NetworkLoop2UAS15m,'ctWanHDSLDb2NetworkLoop2ES15m':ctWanHDSLDb2NetworkLoop2ES15m,'ctWanHDSLDb2CustomerLoop1UAS15m':ctWanHDSLDb2CustomerLoop1UAS15m,'ctWanHDSLDb2CustomerLoop1ES15m':ctWanHDSLDb2CustomerLoop1ES15m,'ctWanHDSLDb2CustomerLoop2UAS15m':ctWanHDSLDb2CustomerLoop2UAS15m,'ctWanHDSLDb2CustomerLoop2ES15m':ctWanHDSLDb2CustomerLoop2ES15m,'ctWanHDSLPerformance24hTable':ctWanHDSLPerformance24hTable,'ctWanHDSLPerformance24hEntry':ctWanHDSLPerformance24hEntry,_f:ctWanHDSLPerformance24hConnIndex,_g:ctWanHDSLPerformance24hSlotIndex,'ctWanHDSLHLULoop1UAS24h':ctWanHDSLHLULoop1UAS24h,'ctWanHDSLHLULoop1ES24h':ctWanHDSLHLULoop1ES24h,'ctWanHDSLHLULoop2UAS24h':ctWanHDSLHLULoop2UAS24h,'ctWanHDSLHLULoop2ES24h':ctWanHDSLHLULoop2ES24h,'ctWanHDSLHRULoop1UAS24h':ctWanHDSLHRULoop1UAS24h,'ctWanHDSLHRULoop1ES24h':ctWanHDSLHRULoop1ES24h,'ctWanHDSLHRULoop2UAS24h':ctWanHDSLHRULoop2UAS24h,'ctWanHDSLHRULoop2ES24h':ctWanHDSLHRULoop2ES24h,'ctWanHDSLDb1NetworkLoop1UAS24h':ctWanHDSLDb1NetworkLoop1UAS24h,'ctWanHDSLDb1NetworkLoop1ES24h':ctWanHDSLDb1NetworkLoop1ES24h,'ctWanHDSLDb1NetworkLoop2UAS24h':ctWanHDSLDb1NetworkLoop2UAS24h,'ctWanHDSLDb1NetworkLoop2ES24h':ctWanHDSLDb1NetworkLoop2ES24h,'ctWanHDSLDb1CustomerLoop1UAS24h':ctWanHDSLDb1CustomerLoop1UAS24h,'ctWanHDSLDb1CustomerLoop1ES24h':ctWanHDSLDb1CustomerLoop1ES24h,'ctWanHDSLDb1CustomerLoop2UAS24h':ctWanHDSLDb1CustomerLoop2UAS24h,'ctWanHDSLDb1CustomerLoop2ES24h':ctWanHDSLDb1CustomerLoop2ES24h,'ctWanHDSLDb2NetworkLoop1UAS24h':ctWanHDSLDb2NetworkLoop1UAS24h,'ctWanHDSLDb2NetworkLoop1ES24h':ctWanHDSLDb2NetworkLoop1ES24h,'ctWanHDSLDb2NetworkLoop2UAS24h':ctWanHDSLDb2NetworkLoop2UAS24h,'ctWanHDSLDb2NetworkLoop2ES24h':ctWanHDSLDb2NetworkLoop2ES24h,'ctWanHDSLDb2CustomerLoop1UAS24h':ctWanHDSLDb2CustomerLoop1UAS24h,'ctWanHDSLDb2CustomerLoop1ES24h':ctWanHDSLDb2CustomerLoop1ES24h,'ctWanHDSLDb2CustomerLoop2UAS24h':ctWanHDSLDb2CustomerLoop2UAS24h,'ctWanHDSLDb2CustomerLoop2ES24h':ctWanHDSLDb2CustomerLoop2ES24h,'ctWanHDSLStatisticsTable':ctWanHDSLStatisticsTable,'ctWanHDSLStatisticsEntry':ctWanHDSLStatisticsEntry,_h:ctWanHDSLStatisticsHLUConnIndex,'ctWanHDSLSNRHLULoop1':ctWanHDSLSNRHLULoop1,'ctWanHDSLSNRLowHLULoop1':ctWanHDSLSNRLowHLULoop1,'ctWanHDSLSNRHighHLULoop1':ctWanHDSLSNRHighHLULoop1,'ctWanHDSLSNRHLULoop2':ctWanHDSLSNRHLULoop2,'ctWanHDSLSNRLowHLULoop2':ctWanHDSLSNRLowHLULoop2,'ctWanHDSLSNRHighHLULoop2':ctWanHDSLSNRHighHLULoop2,'ctWanHDSLPulseAttenuationHLULoop1':ctWanHDSLPulseAttenuationHLULoop1,'ctWanHDSLPulseAttenuationHLULoop2':ctWanHDSLPulseAttenuationHLULoop2,'ctWanHDSLBitStat1HLU':ctWanHDSLBitStat1HLU,'ctWanHDSLSNRHRULoop1':ctWanHDSLSNRHRULoop1,'ctWanHDSLSNRLowHRULoop1':ctWanHDSLSNRLowHRULoop1,'ctWanHDSLSNRHighHRULoop1':ctWanHDSLSNRHighHRULoop1,'ctWanHDSLSNRHRULoop2':ctWanHDSLSNRHRULoop2,'ctWanHDSLSNRLowHRULoop2':ctWanHDSLSNRLowHRULoop2,'ctWanHDSLSNRHighHRULoop2':ctWanHDSLSNRHighHRULoop2,'ctWanHDSLPulseAttenuationHRULoop1':ctWanHDSLPulseAttenuationHRULoop1,'ctWanHDSLPulseAttenuationHRULoop2':ctWanHDSLPulseAttenuationHRULoop2,'ctWanHDSLDs1FrameHRU':ctWanHDSLDs1FrameHRU,'ctWanHDSLSNRDb1NetworkLoop1':ctWanHDSLSNRDb1NetworkLoop1,'ctWanHDSLSNRLowDb1NetworkLoop1':ctWanHDSLSNRLowDb1NetworkLoop1,'ctWanHDSLSNRHighDb1NetworkLoop1':ctWanHDSLSNRHighDb1NetworkLoop1,'ctWanHDSLSNRDb1NetworkLoop2':ctWanHDSLSNRDb1NetworkLoop2,'ctWanHDSLSNRLowDb1NetworkLoop2':ctWanHDSLSNRLowDb1NetworkLoop2,'ctWanHDSLSNRHighDb1NetworkLoop2':ctWanHDSLSNRHighDb1NetworkLoop2,'ctWanHDSLSNRDb1CustomerLoop1':ctWanHDSLSNRDb1CustomerLoop1,'ctWanHDSLSNRLowDb1CustomerLoop1':ctWanHDSLSNRLowDb1CustomerLoop1,'ctWanHDSLSNRHighDb1CustomerLoop1':ctWanHDSLSNRHighDb1CustomerLoop1,'ctWanHDSLSNRDb1CustomerLoop2':ctWanHDSLSNRDb1CustomerLoop2,'ctWanHDSLSNRLowDb1CustomerLoop2':ctWanHDSLSNRLowDb1CustomerLoop2,'ctWanHDSLSNRHighDb1CustomerLoop2':ctWanHDSLSNRHighDb1CustomerLoop2,'ctWanHDSLPulseAttenuationDb1NetworkLoop1':ctWanHDSLPulseAttenuationDb1NetworkLoop1,'ctWanHDSLPulseAttenuationDb1NetworkLoop2':ctWanHDSLPulseAttenuationDb1NetworkLoop2,'ctWanHDSLPulseAttenuationDb1CustomerLoop1':ctWanHDSLPulseAttenuationDb1CustomerLoop1,'ctWanHDSLPulseAttenuationDb1CustomerLoop2':ctWanHDSLPulseAttenuationDb1CustomerLoop2,'ctWanHDSLSNRDb2NetworkLoop1':ctWanHDSLSNRDb2NetworkLoop1,'ctWanHDSLSNRLowDb2NetworkLoop1':ctWanHDSLSNRLowDb2NetworkLoop1,'ctWanHDSLSNRHighDb2NetworkLoop1':ctWanHDSLSNRHighDb2NetworkLoop1,'ctWanHDSLSNRDb2NetworkLoop2':ctWanHDSLSNRDb2NetworkLoop2,'ctWanHDSLSNRLowDb2NetworkLoop2':ctWanHDSLSNRLowDb2NetworkLoop2,'ctWanHDSLSNRHighDb2NetworkLoop2':ctWanHDSLSNRHighDb2NetworkLoop2,'ctWanHDSLSNRDb2CustomerLoop1':ctWanHDSLSNRDb2CustomerLoop1,'ctWanHDSLSNRLowDb2CustomerLoop1':ctWanHDSLSNRLowDb2CustomerLoop1,'ctWanHDSLSNRHighDb2CustomerLoop1':ctWanHDSLSNRHighDb2CustomerLoop1,'ctWanHDSLSNRDb2CustomerLoop2':ctWanHDSLSNRDb2CustomerLoop2,'ctWanHDSLSNRLowDb2CustomerLoop2':ctWanHDSLSNRLowDb2CustomerLoop2,'ctWanHDSLSNRHighDb2CustomerLoop2':ctWanHDSLSNRHighDb2CustomerLoop2,'ctWanHDSLPulseAttenuationDb2NetworkLoop1':ctWanHDSLPulseAttenuationDb2NetworkLoop1,'ctWanHDSLPulseAttenuationDb2NetworkLoop2':ctWanHDSLPulseAttenuationDb2NetworkLoop2,'ctWanHDSLPulseAttenuationDb2CustomerLoop1':ctWanHDSLPulseAttenuationDb2CustomerLoop1,'ctWanHDSLPulseAttenuationDb2CustomerLoop2':ctWanHDSLPulseAttenuationDb2CustomerLoop2,'ctWanHDSLTestTable':ctWanHDSLTestTable,'ctWanHDSLTestEntry':ctWanHDSLTestEntry,_i:ctWanHDSLTestHLUConnIndex,'ctWanHDSLTestMode':ctWanHDSLTestMode,'ctWanHDSLHLUTestResult':ctWanHDSLHLUTestResult,'ctWanHDSLHRUTestResult':ctWanHDSLHRUTestResult,'ctWanHDSLAlarmsTable':ctWanHDSLAlarmsTable,'ctWanHDSLAlarmsEntry':ctWanHDSLAlarmsEntry,_j:ctWanHDSLAlarmsHLUConnIndex,'ctWanHDSLAlarmsBackplane':ctWanHDSLAlarmsBackplane,'ctWanHDSLAlarmsES':ctWanHDSLAlarmsES,'ctWanHDSLAlarmHistoryTable':ctWanHDSLAlarmHistoryTable,'ctWanHDSLAlarmHistoryEntry':ctWanHDSLAlarmHistoryEntry,_k:ctWanHDSLAlarmHistoryConnIndex,'ctWanHDSLAlHistLLOSFirst':ctWanHDSLAlHistLLOSFirst,'ctWanHDSLAlHistLLOSLast':ctWanHDSLAlHistLLOSLast,'ctWanHDSLAlHistLLOSCurrent':ctWanHDSLAlHistLLOSCurrent,'ctWanHDSLAlHistLLOSCount':ctWanHDSLAlHistLLOSCount,'ctWanHDSLAlHistRLOSFirst':ctWanHDSLAlHistRLOSFirst,'ctWanHDSLAlHistRLOSLast':ctWanHDSLAlHistRLOSLast,'ctWanHDSLAlHistRLOSCurrent':ctWanHDSLAlHistRLOSCurrent,'ctWanHDSLAlHistRLOSCount':ctWanHDSLAlHistRLOSCount,'ctWanHDSLAlHistLOSW1First':ctWanHDSLAlHistLOSW1First,'ctWanHDSLAlHistLOSW1Last':ctWanHDSLAlHistLOSW1Last,'ctWanHDSLAlHistLOSW1Current':ctWanHDSLAlHistLOSW1Current,'ctWanHDSLAlHistLOSW1Count':ctWanHDSLAlHistLOSW1Count,'ctWanHDSLAlHistLOSW2First':ctWanHDSLAlHistLOSW2First,'ctWanHDSLAlHistLOSW2Last':ctWanHDSLAlHistLOSW2Last,'ctWanHDSLAlHistLOSW2Current':ctWanHDSLAlHistLOSW2Current,'ctWanHDSLAlHistLOSW2Count':ctWanHDSLAlHistLOSW2Count,'ctWanHDSLAlHistES1First':ctWanHDSLAlHistES1First,'ctWanHDSLAlHistES1Last':ctWanHDSLAlHistES1Last,'ctWanHDSLAlHistES1Current':ctWanHDSLAlHistES1Current,'ctWanHDSLAlHistES1Count':ctWanHDSLAlHistES1Count,'ctWanHDSLAlHistES2First':ctWanHDSLAlHistES2First,'ctWanHDSLAlHistES2Last':ctWanHDSLAlHistES2Last,'ctWanHDSLAlHistES2Current':ctWanHDSLAlHistES2Current,'ctWanHDSLAlHistES2Count':ctWanHDSLAlHistES2Count,'ctWanHDSLAlHistMargin1First':ctWanHDSLAlHistMargin1First,'ctWanHDSLAlHistMargin1Last':ctWanHDSLAlHistMargin1Last,'ctWanHDSLAlHistMargin1Current':ctWanHDSLAlHistMargin1Current,'ctWanHDSLAlHistMargin1Count':ctWanHDSLAlHistMargin1Count,'ctWanHDSLAlHistMargin2First':ctWanHDSLAlHistMargin2First,'ctWanHDSLAlHistMargin2Last':ctWanHDSLAlHistMargin2Last,'ctWanHDSLAlHistMargin2Current':ctWanHDSLAlHistMargin2Current,'ctWanHDSLAlHistMargin2Count':ctWanHDSLAlHistMargin2Count,'ctWanHDSLAlHistCleared':ctWanHDSLAlHistCleared,'ctWanHDSLAlHistClearit':ctWanHDSLAlHistClearit,'ctWanHDSLLoopbacksTable':ctWanHDSLLoopbacksTable,'ctWanHDSLLoopbacksEntry':ctWanHDSLLoopbacksEntry,_l:ctWanHDSLLoopbacksHLUConnIndex,'ctWanHDSLLoopbacksAdminType':ctWanHDSLLoopbacksAdminType,'ctWanHDSLLoopbacksOperType':ctWanHDSLLoopbacksOperType})