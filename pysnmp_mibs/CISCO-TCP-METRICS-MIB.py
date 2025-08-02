_S='ciscoTcpMetricsGroup'
_R='cfmTcpMetricsIntRoundTripTime'
_Q='cfmTcpMetricsIntRoundTripTimePrecision'
_P='cfmTcpMetricsIntRoundTripTimeScale'
_O='cfmTcpMetricsIntValid'
_N='cfmTcpMetricsTableChanged'
_M='cfmTcpMetricsRoundTripTime'
_L='cfmTcpMetricsRoundTripTimePrecision'
_K='cfmTcpMetricsRoundTripTimeScale'
_J='cfmTcpMetricsValid'
_I='roundTripTime'
_H='cfmFlowMetricsIntNumber'
_G='Bits'
_F='cfmFlowMonitorId'
_E='cfmFlowId'
_D='CISCO-FLOW-MONITOR-MIB'
_C='read-only'
_B='CISCO-TCP-METRICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cfmFlowId,cfmFlowMetricsIntNumber,cfmFlowMonitorId=mibBuilder.importSymbols(_D,_E,_H,_F)
FlowMetricPrecision,FlowMetricScale,FlowMetricValue=mibBuilder.importSymbols('CISCO-FLOW-MONITOR-TC-MIB','FlowMetricPrecision','FlowMetricScale','FlowMetricValue')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoTcpMetricsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,770))
if mibBuilder.loadTexts:ciscoTcpMetricsMIB.setRevisions(('2011-03-06 00:00',))
_CiscoTcpMetricsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBNotifs=_CiscoTcpMetricsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,770,0))
_CiscoTcpMetricsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBObjects=_CiscoTcpMetricsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,770,1))
_CfmTcpMetrics_ObjectIdentity=ObjectIdentity
cfmTcpMetrics=_CfmTcpMetrics_ObjectIdentity((1,3,6,1,4,1,9,9,770,1,1))
_CfmTcpMetricsTable_Object=MibTable
cfmTcpMetricsTable=_CfmTcpMetricsTable_Object((1,3,6,1,4,1,9,9,770,1,1,1))
if mibBuilder.loadTexts:cfmTcpMetricsTable.setStatus(_A)
_CfmTcpMetricsEntry_Object=MibTableRow
cfmTcpMetricsEntry=_CfmTcpMetricsEntry_Object((1,3,6,1,4,1,9,9,770,1,1,1,1))
cfmTcpMetricsEntry.setIndexNames((0,_D,_F),(0,_D,_E))
if mibBuilder.loadTexts:cfmTcpMetricsEntry.setStatus(_A)
class _CfmTcpMetricsValid_Type(Bits):namedValues=NamedValues((_I,0))
_CfmTcpMetricsValid_Type.__name__=_G
_CfmTcpMetricsValid_Object=MibTableColumn
cfmTcpMetricsValid=_CfmTcpMetricsValid_Object((1,3,6,1,4,1,9,9,770,1,1,1,1,1),_CfmTcpMetricsValid_Type())
cfmTcpMetricsValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsValid.setStatus(_A)
_CfmTcpMetricsRoundTripTimeScale_Type=FlowMetricScale
_CfmTcpMetricsRoundTripTimeScale_Object=MibTableColumn
cfmTcpMetricsRoundTripTimeScale=_CfmTcpMetricsRoundTripTimeScale_Object((1,3,6,1,4,1,9,9,770,1,1,1,1,2),_CfmTcpMetricsRoundTripTimeScale_Type())
cfmTcpMetricsRoundTripTimeScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsRoundTripTimeScale.setStatus(_A)
_CfmTcpMetricsRoundTripTimePrecision_Type=FlowMetricPrecision
_CfmTcpMetricsRoundTripTimePrecision_Object=MibTableColumn
cfmTcpMetricsRoundTripTimePrecision=_CfmTcpMetricsRoundTripTimePrecision_Object((1,3,6,1,4,1,9,9,770,1,1,1,1,3),_CfmTcpMetricsRoundTripTimePrecision_Type())
cfmTcpMetricsRoundTripTimePrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsRoundTripTimePrecision.setStatus(_A)
_CfmTcpMetricsRoundTripTime_Type=FlowMetricValue
_CfmTcpMetricsRoundTripTime_Object=MibTableColumn
cfmTcpMetricsRoundTripTime=_CfmTcpMetricsRoundTripTime_Object((1,3,6,1,4,1,9,9,770,1,1,1,1,4),_CfmTcpMetricsRoundTripTime_Type())
cfmTcpMetricsRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsRoundTripTime.setStatus(_A)
_CfmTcpMetricsTableChanged_Type=TimeStamp
_CfmTcpMetricsTableChanged_Object=MibScalar
cfmTcpMetricsTableChanged=_CfmTcpMetricsTableChanged_Object((1,3,6,1,4,1,9,9,770,1,1,2),_CfmTcpMetricsTableChanged_Type())
cfmTcpMetricsTableChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsTableChanged.setStatus(_A)
_CfmTcpMetricsIntTable_Object=MibTable
cfmTcpMetricsIntTable=_CfmTcpMetricsIntTable_Object((1,3,6,1,4,1,9,9,770,1,1,3))
if mibBuilder.loadTexts:cfmTcpMetricsIntTable.setStatus(_A)
_CfmTcpMetricsIntEntry_Object=MibTableRow
cfmTcpMetricsIntEntry=_CfmTcpMetricsIntEntry_Object((1,3,6,1,4,1,9,9,770,1,1,3,1))
cfmTcpMetricsIntEntry.setIndexNames((0,_D,_F),(0,_D,_E),(0,_D,_H))
if mibBuilder.loadTexts:cfmTcpMetricsIntEntry.setStatus(_A)
class _CfmTcpMetricsIntValid_Type(Bits):namedValues=NamedValues((_I,0))
_CfmTcpMetricsIntValid_Type.__name__=_G
_CfmTcpMetricsIntValid_Object=MibTableColumn
cfmTcpMetricsIntValid=_CfmTcpMetricsIntValid_Object((1,3,6,1,4,1,9,9,770,1,1,3,1,1),_CfmTcpMetricsIntValid_Type())
cfmTcpMetricsIntValid.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsIntValid.setStatus(_A)
_CfmTcpMetricsIntRoundTripTimeScale_Type=FlowMetricScale
_CfmTcpMetricsIntRoundTripTimeScale_Object=MibTableColumn
cfmTcpMetricsIntRoundTripTimeScale=_CfmTcpMetricsIntRoundTripTimeScale_Object((1,3,6,1,4,1,9,9,770,1,1,3,1,2),_CfmTcpMetricsIntRoundTripTimeScale_Type())
cfmTcpMetricsIntRoundTripTimeScale.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsIntRoundTripTimeScale.setStatus(_A)
_CfmTcpMetricsIntRoundTripTimePrecision_Type=FlowMetricPrecision
_CfmTcpMetricsIntRoundTripTimePrecision_Object=MibTableColumn
cfmTcpMetricsIntRoundTripTimePrecision=_CfmTcpMetricsIntRoundTripTimePrecision_Object((1,3,6,1,4,1,9,9,770,1,1,3,1,3),_CfmTcpMetricsIntRoundTripTimePrecision_Type())
cfmTcpMetricsIntRoundTripTimePrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsIntRoundTripTimePrecision.setStatus(_A)
_CfmTcpMetricsIntRoundTripTime_Type=FlowMetricValue
_CfmTcpMetricsIntRoundTripTime_Object=MibTableColumn
cfmTcpMetricsIntRoundTripTime=_CfmTcpMetricsIntRoundTripTime_Object((1,3,6,1,4,1,9,9,770,1,1,3,1,4),_CfmTcpMetricsIntRoundTripTime_Type())
cfmTcpMetricsIntRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cfmTcpMetricsIntRoundTripTime.setStatus(_A)
_CiscoTcpMetricsMIBConform_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBConform=_CiscoTcpMetricsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,770,2))
_CiscoTcpMetricsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBCompliances=_CiscoTcpMetricsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,770,2,1))
_CiscoTcpMetricsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBGroups=_CiscoTcpMetricsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,770,2,2))
_CiscoTcpMetricsMIBIds_ObjectIdentity=ObjectIdentity
ciscoTcpMetricsMIBIds=_CiscoTcpMetricsMIBIds_ObjectIdentity((1,3,6,1,4,1,9,9,770,3))
ciscoTcpMetricsGroup=ObjectGroup((1,3,6,1,4,1,9,9,770,2,2,1))
ciscoTcpMetricsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoTcpMetricsGroup.setStatus(_A)
ciscoTcpMetricsMIBCompliance01=ModuleCompliance((1,3,6,1,4,1,9,9,770,2,1,1))
ciscoTcpMetricsMIBCompliance01.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoTcpMetricsMIBCompliance01.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoTcpMetricsMIB':ciscoTcpMetricsMIB,'ciscoTcpMetricsMIBNotifs':ciscoTcpMetricsMIBNotifs,'ciscoTcpMetricsMIBObjects':ciscoTcpMetricsMIBObjects,'cfmTcpMetrics':cfmTcpMetrics,'cfmTcpMetricsTable':cfmTcpMetricsTable,'cfmTcpMetricsEntry':cfmTcpMetricsEntry,_J:cfmTcpMetricsValid,_K:cfmTcpMetricsRoundTripTimeScale,_L:cfmTcpMetricsRoundTripTimePrecision,_M:cfmTcpMetricsRoundTripTime,_N:cfmTcpMetricsTableChanged,'cfmTcpMetricsIntTable':cfmTcpMetricsIntTable,'cfmTcpMetricsIntEntry':cfmTcpMetricsIntEntry,_O:cfmTcpMetricsIntValid,_P:cfmTcpMetricsIntRoundTripTimeScale,_Q:cfmTcpMetricsIntRoundTripTimePrecision,_R:cfmTcpMetricsIntRoundTripTime,'ciscoTcpMetricsMIBConform':ciscoTcpMetricsMIBConform,'ciscoTcpMetricsMIBCompliances':ciscoTcpMetricsMIBCompliances,'ciscoTcpMetricsMIBCompliance01':ciscoTcpMetricsMIBCompliance01,'ciscoTcpMetricsMIBGroups':ciscoTcpMetricsMIBGroups,_S:ciscoTcpMetricsGroup,'ciscoTcpMetricsMIBIds':ciscoTcpMetricsMIBIds})