_u='cfmRtpMetricsGroup'
_t='cfmRtpMetricsIntTransit'
_s='cfmRtpMetricsIntTransitPrecision'
_r='cfmRtpMetricsIntTransitScale'
_q='cfmRtpMetricsIntJitter'
_p='cfmRtpMetricsIntJitterPrecision'
_o='cfmRtpMetricsIntJitterScale'
_n='cfmRtpMetricsIntAvgLossDistance'
_m='cfmRtpMetricsIntAvgLD'
_l='cfmRtpMetricsIntAvgLDPrecision'
_k='cfmRtpMetricsIntAvgLDScale'
_j='cfmRtpMetricsIntLIs'
_i='cfmRtpMetricsIntFrac'
_h='cfmRtpMetricsIntFracPrecision'
_g='cfmRtpMetricsIntFracScale'
_f='cfmRtpMetricsIntLostPkts'
_e='cfmRtpMetricsIntExpectedPkts'
_d='cfmRtpMetricsIntValid'
_c='cfmRtpMetricsTableChanged'
_b='cfmRtpMetricsJitter'
_a='cfmRtpMetricsJitterPrecision'
_Z='cfmRtpMetricsJitterScale'
_Y='cfmRtpMetricsAvgLossDistance'
_X='cfmRtpMetricsAvgLD'
_W='cfmRtpMetricsAvgLDPrecision'
_V='cfmRtpMetricsAvgLDScale'
_U='cfmRtpMetricsLIs'
_T='cfmRtpMetricsFrac'
_S='cfmRtpMetricsFracPrecision'
_R='cfmRtpMetricsFracScale'
_Q='cfmRtpMetricsLostPkts'
_P='cfmRtpMetricsExpectedPkts'
_O='cfmRtpMetricsValid'
_N='avgLossDistance'
_M='lossIntervals'
_L='lossFraction'
_K='lostPkts'
_J='expectedPkts'
_I='cfmFlowMetricsIntNumber'
_H='Bits'
_G='cfmFlowMonitorId'
_F='cfmFlowId'
_E='packets'
_D='CISCO-FLOW-MONITOR-MIB'
_C='read-only'
_B='CISCO-RTP-METRICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cfmFlowId,cfmFlowMetricsIntNumber,cfmFlowMonitorId=mibBuilder.importSymbols(_D,_F,_I,_G)
FlowMetricPrecision,FlowMetricScale,FlowMetricValue=mibBuilder.importSymbols('CISCO-FLOW-MONITOR-TC-MIB','FlowMetricPrecision','FlowMetricScale','FlowMetricValue')
ReportIntervalCount,=mibBuilder.importSymbols('CISCO-REPORT-INTERVAL-TC-MIB','ReportIntervalCount')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoRtpMetricsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,703))
if mibBuilder.loadTexts:ciscoRtpMetricsMIB.setRevisions(('2009-06-17 00:00',))
_CiscoRtpMetricsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBNotifs=_CiscoRtpMetricsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,703,0))
_CiscoRtpMetricsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBObjects=_CiscoRtpMetricsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,703,1))
_CfmRtpMetrics_ObjectIdentity=ObjectIdentity
cfmRtpMetrics=_CfmRtpMetrics_ObjectIdentity((1,3,6,1,4,1,9,9,703,1,1))
_CfmRtpMetricsTable_Object=MibTable
cfmRtpMetricsTable=_CfmRtpMetricsTable_Object((1,3,6,1,4,1,9,9,703,1,1,1))
if mibBuilder.loadTexts:cfmRtpMetricsTable.setStatus(_A)
_CfmRtpMetricsEntry_Object=MibTableRow
cfmRtpMetricsEntry=_CfmRtpMetricsEntry_Object((1,3,6,1,4,1,9,9,703,1,1,1,1))
cfmRtpMetricsEntry.setIndexNames((0,_D,_G),(0,_D,_F))
if mibBuilder.loadTexts:cfmRtpMetricsEntry.setStatus(_A)
class _CfmRtpMetricsValid_Type(Bits):namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),('avgLossDuration',4),(_N,5),('jitter',6)))
_CfmRtpMetricsValid_Type.__name__=_H
_CfmRtpMetricsValid_Object=MibTableColumn
cfmRtpMetricsValid=_CfmRtpMetricsValid_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,1),_CfmRtpMetricsValid_Type())
cfmRtpMetricsValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsValid.setStatus(_A)
_CfmRtpMetricsExpectedPkts_Type=Counter64
_CfmRtpMetricsExpectedPkts_Object=MibTableColumn
cfmRtpMetricsExpectedPkts=_CfmRtpMetricsExpectedPkts_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,2),_CfmRtpMetricsExpectedPkts_Type())
cfmRtpMetricsExpectedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsExpectedPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmRtpMetricsExpectedPkts.setUnits(_E)
_CfmRtpMetricsLostPkts_Type=Counter64
_CfmRtpMetricsLostPkts_Object=MibTableColumn
cfmRtpMetricsLostPkts=_CfmRtpMetricsLostPkts_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,3),_CfmRtpMetricsLostPkts_Type())
cfmRtpMetricsLostPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsLostPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmRtpMetricsLostPkts.setUnits(_E)
_CfmRtpMetricsFracScale_Type=FlowMetricScale
_CfmRtpMetricsFracScale_Object=MibTableColumn
cfmRtpMetricsFracScale=_CfmRtpMetricsFracScale_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,4),_CfmRtpMetricsFracScale_Type())
cfmRtpMetricsFracScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsFracScale.setStatus(_A)
_CfmRtpMetricsFracPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsFracPrecision_Object=MibTableColumn
cfmRtpMetricsFracPrecision=_CfmRtpMetricsFracPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,5),_CfmRtpMetricsFracPrecision_Type())
cfmRtpMetricsFracPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsFracPrecision.setStatus(_A)
_CfmRtpMetricsFrac_Type=FlowMetricValue
_CfmRtpMetricsFrac_Object=MibTableColumn
cfmRtpMetricsFrac=_CfmRtpMetricsFrac_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,6),_CfmRtpMetricsFrac_Type())
cfmRtpMetricsFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsFrac.setStatus(_A)
_CfmRtpMetricsLIs_Type=Counter64
_CfmRtpMetricsLIs_Object=MibTableColumn
cfmRtpMetricsLIs=_CfmRtpMetricsLIs_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,7),_CfmRtpMetricsLIs_Type())
cfmRtpMetricsLIs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsLIs.setStatus(_A)
_CfmRtpMetricsAvgLDScale_Type=FlowMetricScale
_CfmRtpMetricsAvgLDScale_Object=MibTableColumn
cfmRtpMetricsAvgLDScale=_CfmRtpMetricsAvgLDScale_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,8),_CfmRtpMetricsAvgLDScale_Type())
cfmRtpMetricsAvgLDScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsAvgLDScale.setStatus(_A)
_CfmRtpMetricsAvgLDPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsAvgLDPrecision_Object=MibTableColumn
cfmRtpMetricsAvgLDPrecision=_CfmRtpMetricsAvgLDPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,9),_CfmRtpMetricsAvgLDPrecision_Type())
cfmRtpMetricsAvgLDPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsAvgLDPrecision.setStatus(_A)
_CfmRtpMetricsAvgLD_Type=FlowMetricValue
_CfmRtpMetricsAvgLD_Object=MibTableColumn
cfmRtpMetricsAvgLD=_CfmRtpMetricsAvgLD_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,10),_CfmRtpMetricsAvgLD_Type())
cfmRtpMetricsAvgLD.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsAvgLD.setStatus(_A)
_CfmRtpMetricsAvgLossDistance_Type=Gauge32
_CfmRtpMetricsAvgLossDistance_Object=MibTableColumn
cfmRtpMetricsAvgLossDistance=_CfmRtpMetricsAvgLossDistance_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,11),_CfmRtpMetricsAvgLossDistance_Type())
cfmRtpMetricsAvgLossDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsAvgLossDistance.setStatus(_A)
_CfmRtpMetricsJitterScale_Type=FlowMetricScale
_CfmRtpMetricsJitterScale_Object=MibTableColumn
cfmRtpMetricsJitterScale=_CfmRtpMetricsJitterScale_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,12),_CfmRtpMetricsJitterScale_Type())
cfmRtpMetricsJitterScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsJitterScale.setStatus(_A)
_CfmRtpMetricsJitterPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsJitterPrecision_Object=MibTableColumn
cfmRtpMetricsJitterPrecision=_CfmRtpMetricsJitterPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,13),_CfmRtpMetricsJitterPrecision_Type())
cfmRtpMetricsJitterPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsJitterPrecision.setStatus(_A)
_CfmRtpMetricsJitter_Type=FlowMetricValue
_CfmRtpMetricsJitter_Object=MibTableColumn
cfmRtpMetricsJitter=_CfmRtpMetricsJitter_Object((1,3,6,1,4,1,9,9,703,1,1,1,1,14),_CfmRtpMetricsJitter_Type())
cfmRtpMetricsJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsJitter.setStatus(_A)
if mibBuilder.loadTexts:cfmRtpMetricsJitter.setUnits('seconds')
_CfmRtpMetricsTableChanged_Type=TimeStamp
_CfmRtpMetricsTableChanged_Object=MibScalar
cfmRtpMetricsTableChanged=_CfmRtpMetricsTableChanged_Object((1,3,6,1,4,1,9,9,703,1,1,2),_CfmRtpMetricsTableChanged_Type())
cfmRtpMetricsTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsTableChanged.setStatus(_A)
_CfmRtpMetricsIntTable_Object=MibTable
cfmRtpMetricsIntTable=_CfmRtpMetricsIntTable_Object((1,3,6,1,4,1,9,9,703,1,1,3))
if mibBuilder.loadTexts:cfmRtpMetricsIntTable.setStatus(_A)
_CfmRtpMetricsIntEntry_Object=MibTableRow
cfmRtpMetricsIntEntry=_CfmRtpMetricsIntEntry_Object((1,3,6,1,4,1,9,9,703,1,1,3,1))
cfmRtpMetricsIntEntry.setIndexNames((0,_D,_G),(0,_D,_F),(0,_D,_I))
if mibBuilder.loadTexts:cfmRtpMetricsIntEntry.setStatus(_A)
class _CfmRtpMetricsIntValid_Type(Bits):namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_M,3),('avgLossIntervalDuration',4),(_N,5),('maxJitter',6),('maxMinTransit',7)))
_CfmRtpMetricsIntValid_Type.__name__=_H
_CfmRtpMetricsIntValid_Object=MibTableColumn
cfmRtpMetricsIntValid=_CfmRtpMetricsIntValid_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,1),_CfmRtpMetricsIntValid_Type())
cfmRtpMetricsIntValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntValid.setStatus(_A)
_CfmRtpMetricsIntExpectedPkts_Type=ReportIntervalCount
_CfmRtpMetricsIntExpectedPkts_Object=MibTableColumn
cfmRtpMetricsIntExpectedPkts=_CfmRtpMetricsIntExpectedPkts_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,2),_CfmRtpMetricsIntExpectedPkts_Type())
cfmRtpMetricsIntExpectedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntExpectedPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmRtpMetricsIntExpectedPkts.setUnits(_E)
_CfmRtpMetricsIntLostPkts_Type=ReportIntervalCount
_CfmRtpMetricsIntLostPkts_Object=MibTableColumn
cfmRtpMetricsIntLostPkts=_CfmRtpMetricsIntLostPkts_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,3),_CfmRtpMetricsIntLostPkts_Type())
cfmRtpMetricsIntLostPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntLostPkts.setStatus(_A)
if mibBuilder.loadTexts:cfmRtpMetricsIntLostPkts.setUnits(_E)
_CfmRtpMetricsIntFracScale_Type=FlowMetricScale
_CfmRtpMetricsIntFracScale_Object=MibTableColumn
cfmRtpMetricsIntFracScale=_CfmRtpMetricsIntFracScale_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,4),_CfmRtpMetricsIntFracScale_Type())
cfmRtpMetricsIntFracScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntFracScale.setStatus(_A)
_CfmRtpMetricsIntFracPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsIntFracPrecision_Object=MibTableColumn
cfmRtpMetricsIntFracPrecision=_CfmRtpMetricsIntFracPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,5),_CfmRtpMetricsIntFracPrecision_Type())
cfmRtpMetricsIntFracPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntFracPrecision.setStatus(_A)
_CfmRtpMetricsIntFrac_Type=FlowMetricValue
_CfmRtpMetricsIntFrac_Object=MibTableColumn
cfmRtpMetricsIntFrac=_CfmRtpMetricsIntFrac_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,6),_CfmRtpMetricsIntFrac_Type())
cfmRtpMetricsIntFrac.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntFrac.setStatus(_A)
_CfmRtpMetricsIntLIs_Type=ReportIntervalCount
_CfmRtpMetricsIntLIs_Object=MibTableColumn
cfmRtpMetricsIntLIs=_CfmRtpMetricsIntLIs_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,7),_CfmRtpMetricsIntLIs_Type())
cfmRtpMetricsIntLIs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntLIs.setStatus(_A)
_CfmRtpMetricsIntAvgLDScale_Type=FlowMetricScale
_CfmRtpMetricsIntAvgLDScale_Object=MibTableColumn
cfmRtpMetricsIntAvgLDScale=_CfmRtpMetricsIntAvgLDScale_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,8),_CfmRtpMetricsIntAvgLDScale_Type())
cfmRtpMetricsIntAvgLDScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntAvgLDScale.setStatus(_A)
_CfmRtpMetricsIntAvgLDPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsIntAvgLDPrecision_Object=MibTableColumn
cfmRtpMetricsIntAvgLDPrecision=_CfmRtpMetricsIntAvgLDPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,9),_CfmRtpMetricsIntAvgLDPrecision_Type())
cfmRtpMetricsIntAvgLDPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntAvgLDPrecision.setStatus(_A)
_CfmRtpMetricsIntAvgLD_Type=FlowMetricValue
_CfmRtpMetricsIntAvgLD_Object=MibTableColumn
cfmRtpMetricsIntAvgLD=_CfmRtpMetricsIntAvgLD_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,10),_CfmRtpMetricsIntAvgLD_Type())
cfmRtpMetricsIntAvgLD.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntAvgLD.setStatus(_A)
_CfmRtpMetricsIntAvgLossDistance_Type=ReportIntervalCount
_CfmRtpMetricsIntAvgLossDistance_Object=MibTableColumn
cfmRtpMetricsIntAvgLossDistance=_CfmRtpMetricsIntAvgLossDistance_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,11),_CfmRtpMetricsIntAvgLossDistance_Type())
cfmRtpMetricsIntAvgLossDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntAvgLossDistance.setStatus(_A)
_CfmRtpMetricsIntJitterScale_Type=FlowMetricScale
_CfmRtpMetricsIntJitterScale_Object=MibTableColumn
cfmRtpMetricsIntJitterScale=_CfmRtpMetricsIntJitterScale_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,12),_CfmRtpMetricsIntJitterScale_Type())
cfmRtpMetricsIntJitterScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntJitterScale.setStatus(_A)
_CfmRtpMetricsIntJitterPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsIntJitterPrecision_Object=MibTableColumn
cfmRtpMetricsIntJitterPrecision=_CfmRtpMetricsIntJitterPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,13),_CfmRtpMetricsIntJitterPrecision_Type())
cfmRtpMetricsIntJitterPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntJitterPrecision.setStatus(_A)
_CfmRtpMetricsIntJitter_Type=FlowMetricValue
_CfmRtpMetricsIntJitter_Object=MibTableColumn
cfmRtpMetricsIntJitter=_CfmRtpMetricsIntJitter_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,14),_CfmRtpMetricsIntJitter_Type())
cfmRtpMetricsIntJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntJitter.setStatus(_A)
_CfmRtpMetricsIntTransitScale_Type=FlowMetricScale
_CfmRtpMetricsIntTransitScale_Object=MibTableColumn
cfmRtpMetricsIntTransitScale=_CfmRtpMetricsIntTransitScale_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,15),_CfmRtpMetricsIntTransitScale_Type())
cfmRtpMetricsIntTransitScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntTransitScale.setStatus(_A)
_CfmRtpMetricsIntTransitPrecision_Type=FlowMetricPrecision
_CfmRtpMetricsIntTransitPrecision_Object=MibTableColumn
cfmRtpMetricsIntTransitPrecision=_CfmRtpMetricsIntTransitPrecision_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,16),_CfmRtpMetricsIntTransitPrecision_Type())
cfmRtpMetricsIntTransitPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntTransitPrecision.setStatus(_A)
_CfmRtpMetricsIntTransit_Type=FlowMetricValue
_CfmRtpMetricsIntTransit_Object=MibTableColumn
cfmRtpMetricsIntTransit=_CfmRtpMetricsIntTransit_Object((1,3,6,1,4,1,9,9,703,1,1,3,1,17),_CfmRtpMetricsIntTransit_Type())
cfmRtpMetricsIntTransit.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmRtpMetricsIntTransit.setStatus(_A)
_CiscoRtpMetricsMIBConform_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBConform=_CiscoRtpMetricsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,703,2))
_CiscoRtpMetricsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBCompliances=_CiscoRtpMetricsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,703,2,1))
_CiscoRtpMetricsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBGroups=_CiscoRtpMetricsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,703,2,2))
_CiscoRtpMetricsMIBIds_ObjectIdentity=ObjectIdentity
ciscoRtpMetricsMIBIds=_CiscoRtpMetricsMIBIds_ObjectIdentity((1,3,6,1,4,1,9,9,703,3))
_CfmRtpMonitoredElements_ObjectIdentity=ObjectIdentity
cfmRtpMonitoredElements=_CfmRtpMonitoredElements_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1))
_CfmeRtpSsrcMismatch_ObjectIdentity=ObjectIdentity
cfmeRtpSsrcMismatch=_CfmeRtpSsrcMismatch_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,1))
if mibBuilder.loadTexts:cfmeRtpSsrcMismatch.setStatus(_A)
_CfmeRtpCumulativeLostPkts_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeLostPkts=_CfmeRtpCumulativeLostPkts_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,2))
if mibBuilder.loadTexts:cfmeRtpCumulativeLostPkts.setStatus(_A)
_CfmeRtpCumulativeLossFraction_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeLossFraction=_CfmeRtpCumulativeLossFraction_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,3))
if mibBuilder.loadTexts:cfmeRtpCumulativeLossFraction.setStatus(_A)
_CfmeRtpCumulativeLossIntervals_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeLossIntervals=_CfmeRtpCumulativeLossIntervals_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,4))
if mibBuilder.loadTexts:cfmeRtpCumulativeLossIntervals.setStatus(_A)
_CfmeRtpCumulativeAvgLossDuration_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeAvgLossDuration=_CfmeRtpCumulativeAvgLossDuration_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,5))
if mibBuilder.loadTexts:cfmeRtpCumulativeAvgLossDuration.setStatus(_A)
_CfmeRtpCumulativeAvgLossDistance_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeAvgLossDistance=_CfmeRtpCumulativeAvgLossDistance_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,6))
if mibBuilder.loadTexts:cfmeRtpCumulativeAvgLossDistance.setStatus(_A)
_CfmeRtpCumulativeJitter_ObjectIdentity=ObjectIdentity
cfmeRtpCumulativeJitter=_CfmeRtpCumulativeJitter_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,7))
if mibBuilder.loadTexts:cfmeRtpCumulativeJitter.setStatus(_A)
_CfmeRtpLostPkts_ObjectIdentity=ObjectIdentity
cfmeRtpLostPkts=_CfmeRtpLostPkts_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,8))
if mibBuilder.loadTexts:cfmeRtpLostPkts.setStatus(_A)
_CfmeRtpLossFraction_ObjectIdentity=ObjectIdentity
cfmeRtpLossFraction=_CfmeRtpLossFraction_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,9))
if mibBuilder.loadTexts:cfmeRtpLossFraction.setStatus(_A)
_CfmeRtpLossIntervals_ObjectIdentity=ObjectIdentity
cfmeRtpLossIntervals=_CfmeRtpLossIntervals_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,10))
if mibBuilder.loadTexts:cfmeRtpLossIntervals.setStatus(_A)
_CfmeRtpAvgLossDuration_ObjectIdentity=ObjectIdentity
cfmeRtpAvgLossDuration=_CfmeRtpAvgLossDuration_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,11))
if mibBuilder.loadTexts:cfmeRtpAvgLossDuration.setStatus(_A)
_CfmeRtpAvgLossDistance_ObjectIdentity=ObjectIdentity
cfmeRtpAvgLossDistance=_CfmeRtpAvgLossDistance_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,12))
if mibBuilder.loadTexts:cfmeRtpAvgLossDistance.setStatus(_A)
_CfmeRtpMaxJitter_ObjectIdentity=ObjectIdentity
cfmeRtpMaxJitter=_CfmeRtpMaxJitter_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,13))
if mibBuilder.loadTexts:cfmeRtpMaxJitter.setStatus(_A)
_CfmeRtpMaxMinTransit_ObjectIdentity=ObjectIdentity
cfmeRtpMaxMinTransit=_CfmeRtpMaxMinTransit_ObjectIdentity((1,3,6,1,4,1,9,9,703,3,1,14))
if mibBuilder.loadTexts:cfmeRtpMaxMinTransit.setStatus(_A)
cfmRtpMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,703,2,2,1))
cfmRtpMetricsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cfmRtpMetricsGroup.setStatus(_A)
ciscoRtpMetricsCompliance01=ModuleCompliance((1,3,6,1,4,1,9,9,703,2,1,1))
ciscoRtpMetricsCompliance01.setObjects((_B,_u))
if mibBuilder.loadTexts:ciscoRtpMetricsCompliance01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoRtpMetricsMIB':ciscoRtpMetricsMIB,'ciscoRtpMetricsMIBNotifs':ciscoRtpMetricsMIBNotifs,'ciscoRtpMetricsMIBObjects':ciscoRtpMetricsMIBObjects,'cfmRtpMetrics':cfmRtpMetrics,'cfmRtpMetricsTable':cfmRtpMetricsTable,'cfmRtpMetricsEntry':cfmRtpMetricsEntry,_O:cfmRtpMetricsValid,_P:cfmRtpMetricsExpectedPkts,_Q:cfmRtpMetricsLostPkts,_R:cfmRtpMetricsFracScale,_S:cfmRtpMetricsFracPrecision,_T:cfmRtpMetricsFrac,_U:cfmRtpMetricsLIs,_V:cfmRtpMetricsAvgLDScale,_W:cfmRtpMetricsAvgLDPrecision,_X:cfmRtpMetricsAvgLD,_Y:cfmRtpMetricsAvgLossDistance,_Z:cfmRtpMetricsJitterScale,_a:cfmRtpMetricsJitterPrecision,_b:cfmRtpMetricsJitter,_c:cfmRtpMetricsTableChanged,'cfmRtpMetricsIntTable':cfmRtpMetricsIntTable,'cfmRtpMetricsIntEntry':cfmRtpMetricsIntEntry,_d:cfmRtpMetricsIntValid,_e:cfmRtpMetricsIntExpectedPkts,_f:cfmRtpMetricsIntLostPkts,_g:cfmRtpMetricsIntFracScale,_h:cfmRtpMetricsIntFracPrecision,_i:cfmRtpMetricsIntFrac,_j:cfmRtpMetricsIntLIs,_k:cfmRtpMetricsIntAvgLDScale,_l:cfmRtpMetricsIntAvgLDPrecision,_m:cfmRtpMetricsIntAvgLD,_n:cfmRtpMetricsIntAvgLossDistance,_o:cfmRtpMetricsIntJitterScale,_p:cfmRtpMetricsIntJitterPrecision,_q:cfmRtpMetricsIntJitter,_r:cfmRtpMetricsIntTransitScale,_s:cfmRtpMetricsIntTransitPrecision,_t:cfmRtpMetricsIntTransit,'ciscoRtpMetricsMIBConform':ciscoRtpMetricsMIBConform,'ciscoRtpMetricsMIBCompliances':ciscoRtpMetricsMIBCompliances,'ciscoRtpMetricsCompliance01':ciscoRtpMetricsCompliance01,'ciscoRtpMetricsMIBGroups':ciscoRtpMetricsMIBGroups,_u:cfmRtpMetricsGroup,'ciscoRtpMetricsMIBIds':ciscoRtpMetricsMIBIds,'cfmRtpMonitoredElements':cfmRtpMonitoredElements,'cfmeRtpSsrcMismatch':cfmeRtpSsrcMismatch,'cfmeRtpCumulativeLostPkts':cfmeRtpCumulativeLostPkts,'cfmeRtpCumulativeLossFraction':cfmeRtpCumulativeLossFraction,'cfmeRtpCumulativeLossIntervals':cfmeRtpCumulativeLossIntervals,'cfmeRtpCumulativeAvgLossDuration':cfmeRtpCumulativeAvgLossDuration,'cfmeRtpCumulativeAvgLossDistance':cfmeRtpCumulativeAvgLossDistance,'cfmeRtpCumulativeJitter':cfmeRtpCumulativeJitter,'cfmeRtpLostPkts':cfmeRtpLostPkts,'cfmeRtpLossFraction':cfmeRtpLossFraction,'cfmeRtpLossIntervals':cfmeRtpLossIntervals,'cfmeRtpAvgLossDuration':cfmeRtpAvgLossDuration,'cfmeRtpAvgLossDistance':cfmeRtpAvgLossDistance,'cfmeRtpMaxJitter':cfmeRtpMaxJitter,'cfmeRtpMaxMinTransit':cfmeRtpMaxMinTransit})