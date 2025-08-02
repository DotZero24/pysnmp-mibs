_Q='cSdwanAppCflowdTemplateGroup'
_P='cSdwanAppCflowdStatisticsGroup'
_O='appCflowdTemplateTemplateRefresh'
_N='appCflowdTemplateFlowInactiveTimeout'
_M='appCflowdTemplateFlowActiveTimeout'
_L='appCflowdTemplateName'
_K='appCflowdStatisticsFlowRateLimitDrop'
_J='appCflowdStatisticsFlowEndForced'
_I='appCflowdStatisticsFlowEndDetected'
_H='appCflowdStatisticsFlowAgeout'
_G='appCflowdStatisticsFlowRefresh'
_F='appCflowdStatisticsTotalPackets'
_E='appCflowdStatisticsTemplatePackets'
_D='appCflowdStatisticsDataPackets'
_C='read-only'
_B='CISCO-SDWAN-OPER-APP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSdwanOperAppMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1007))
if mibBuilder.loadTexts:ciscoSdwanOperAppMIB.setRevisions(('2021-05-26 00:00',))
_CiscoSdwanOperAppMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBNotifs=_CiscoSdwanOperAppMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1007,0))
_CiscoSdwanOperAppMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBObjects=_CiscoSdwanOperAppMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1007,1))
_App_ObjectIdentity=ObjectIdentity
app=_App_ObjectIdentity((1,3,6,1,4,1,9,9,1007,1,6))
_AppCflowd_ObjectIdentity=ObjectIdentity
appCflowd=_AppCflowd_ObjectIdentity((1,3,6,1,4,1,9,9,1007,1,6,1))
_AppCflowdStatistics_ObjectIdentity=ObjectIdentity
appCflowdStatistics=_AppCflowdStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,1007,1,6,1,3))
_AppCflowdStatisticsDataPackets_Type=Counter64
_AppCflowdStatisticsDataPackets_Object=MibScalar
appCflowdStatisticsDataPackets=_AppCflowdStatisticsDataPackets_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,1),_AppCflowdStatisticsDataPackets_Type())
appCflowdStatisticsDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsDataPackets.setStatus(_A)
_AppCflowdStatisticsTemplatePackets_Type=Counter64
_AppCflowdStatisticsTemplatePackets_Object=MibScalar
appCflowdStatisticsTemplatePackets=_AppCflowdStatisticsTemplatePackets_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,2),_AppCflowdStatisticsTemplatePackets_Type())
appCflowdStatisticsTemplatePackets.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsTemplatePackets.setStatus(_A)
_AppCflowdStatisticsTotalPackets_Type=Counter64
_AppCflowdStatisticsTotalPackets_Object=MibScalar
appCflowdStatisticsTotalPackets=_AppCflowdStatisticsTotalPackets_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,3),_AppCflowdStatisticsTotalPackets_Type())
appCflowdStatisticsTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsTotalPackets.setStatus(_A)
_AppCflowdStatisticsFlowRefresh_Type=Counter64
_AppCflowdStatisticsFlowRefresh_Object=MibScalar
appCflowdStatisticsFlowRefresh=_AppCflowdStatisticsFlowRefresh_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,4),_AppCflowdStatisticsFlowRefresh_Type())
appCflowdStatisticsFlowRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsFlowRefresh.setStatus(_A)
_AppCflowdStatisticsFlowAgeout_Type=Counter64
_AppCflowdStatisticsFlowAgeout_Object=MibScalar
appCflowdStatisticsFlowAgeout=_AppCflowdStatisticsFlowAgeout_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,5),_AppCflowdStatisticsFlowAgeout_Type())
appCflowdStatisticsFlowAgeout.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsFlowAgeout.setStatus(_A)
_AppCflowdStatisticsFlowEndDetected_Type=Counter64
_AppCflowdStatisticsFlowEndDetected_Object=MibScalar
appCflowdStatisticsFlowEndDetected=_AppCflowdStatisticsFlowEndDetected_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,6),_AppCflowdStatisticsFlowEndDetected_Type())
appCflowdStatisticsFlowEndDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsFlowEndDetected.setStatus(_A)
_AppCflowdStatisticsFlowEndForced_Type=Counter64
_AppCflowdStatisticsFlowEndForced_Object=MibScalar
appCflowdStatisticsFlowEndForced=_AppCflowdStatisticsFlowEndForced_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,7),_AppCflowdStatisticsFlowEndForced_Type())
appCflowdStatisticsFlowEndForced.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsFlowEndForced.setStatus(_A)
_AppCflowdStatisticsFlowRateLimitDrop_Type=Counter64
_AppCflowdStatisticsFlowRateLimitDrop_Object=MibScalar
appCflowdStatisticsFlowRateLimitDrop=_AppCflowdStatisticsFlowRateLimitDrop_Object((1,3,6,1,4,1,9,9,1007,1,6,1,3,8),_AppCflowdStatisticsFlowRateLimitDrop_Type())
appCflowdStatisticsFlowRateLimitDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdStatisticsFlowRateLimitDrop.setStatus(_A)
_AppCflowdTemplate_ObjectIdentity=ObjectIdentity
appCflowdTemplate=_AppCflowdTemplate_ObjectIdentity((1,3,6,1,4,1,9,9,1007,1,6,1,4))
_AppCflowdTemplateName_Type=OctetString
_AppCflowdTemplateName_Object=MibScalar
appCflowdTemplateName=_AppCflowdTemplateName_Object((1,3,6,1,4,1,9,9,1007,1,6,1,4,1),_AppCflowdTemplateName_Type())
appCflowdTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdTemplateName.setStatus(_A)
_AppCflowdTemplateFlowActiveTimeout_Type=Unsigned32
_AppCflowdTemplateFlowActiveTimeout_Object=MibScalar
appCflowdTemplateFlowActiveTimeout=_AppCflowdTemplateFlowActiveTimeout_Object((1,3,6,1,4,1,9,9,1007,1,6,1,4,2),_AppCflowdTemplateFlowActiveTimeout_Type())
appCflowdTemplateFlowActiveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdTemplateFlowActiveTimeout.setStatus(_A)
_AppCflowdTemplateFlowInactiveTimeout_Type=Unsigned32
_AppCflowdTemplateFlowInactiveTimeout_Object=MibScalar
appCflowdTemplateFlowInactiveTimeout=_AppCflowdTemplateFlowInactiveTimeout_Object((1,3,6,1,4,1,9,9,1007,1,6,1,4,3),_AppCflowdTemplateFlowInactiveTimeout_Type())
appCflowdTemplateFlowInactiveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdTemplateFlowInactiveTimeout.setStatus(_A)
_AppCflowdTemplateTemplateRefresh_Type=Unsigned32
_AppCflowdTemplateTemplateRefresh_Object=MibScalar
appCflowdTemplateTemplateRefresh=_AppCflowdTemplateTemplateRefresh_Object((1,3,6,1,4,1,9,9,1007,1,6,1,4,4),_AppCflowdTemplateTemplateRefresh_Type())
appCflowdTemplateTemplateRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:appCflowdTemplateTemplateRefresh.setStatus(_A)
_CiscoSdwanOperAppMIBNotifObjects_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBNotifObjects=_CiscoSdwanOperAppMIBNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1007,2))
_CiscoSdwanOperAppMIBConform_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBConform=_CiscoSdwanOperAppMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,1007,3))
_CiscoSdwanOperAppMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBCompliances=_CiscoSdwanOperAppMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1007,3,1))
_CiscoSdwanOperAppMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSdwanOperAppMIBGroups=_CiscoSdwanOperAppMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1007,3,2))
cSdwanAppCflowdStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,1007,3,2,1))
cSdwanAppCflowdStatisticsGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cSdwanAppCflowdStatisticsGroup.setStatus(_A)
cSdwanAppCflowdTemplateGroup=ObjectGroup((1,3,6,1,4,1,9,9,1007,3,2,2))
cSdwanAppCflowdTemplateGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cSdwanAppCflowdTemplateGroup.setStatus(_A)
ciscoSdwanOperAppMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,1007,3,1,1))
ciscoSdwanOperAppMIBCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoSdwanOperAppMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSdwanOperAppMIB':ciscoSdwanOperAppMIB,'ciscoSdwanOperAppMIBNotifs':ciscoSdwanOperAppMIBNotifs,'ciscoSdwanOperAppMIBObjects':ciscoSdwanOperAppMIBObjects,'app':app,'appCflowd':appCflowd,'appCflowdStatistics':appCflowdStatistics,_D:appCflowdStatisticsDataPackets,_E:appCflowdStatisticsTemplatePackets,_F:appCflowdStatisticsTotalPackets,_G:appCflowdStatisticsFlowRefresh,_H:appCflowdStatisticsFlowAgeout,_I:appCflowdStatisticsFlowEndDetected,_J:appCflowdStatisticsFlowEndForced,_K:appCflowdStatisticsFlowRateLimitDrop,'appCflowdTemplate':appCflowdTemplate,_L:appCflowdTemplateName,_M:appCflowdTemplateFlowActiveTimeout,_N:appCflowdTemplateFlowInactiveTimeout,_O:appCflowdTemplateTemplateRefresh,'ciscoSdwanOperAppMIBNotifObjects':ciscoSdwanOperAppMIBNotifObjects,'ciscoSdwanOperAppMIBConform':ciscoSdwanOperAppMIBConform,'ciscoSdwanOperAppMIBCompliances':ciscoSdwanOperAppMIBCompliances,'ciscoSdwanOperAppMIBCompliance':ciscoSdwanOperAppMIBCompliance,'ciscoSdwanOperAppMIBGroups':ciscoSdwanOperAppMIBGroups,_P:cSdwanAppCflowdStatisticsGroup,_Q:cSdwanAppCflowdTemplateGroup})