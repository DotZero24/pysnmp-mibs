_Y='csnSamplerGroup'
_X='csnNetflowTableSizeGroup'
_W='csnUsageThreshNotifGroup'
_V='csnUtilizationGroup'
_U='csnUsageThreshGroup'
_T='csnUsageThreshNotifControlGroup'
_S='csnGlobalGroup'
_R='csnUsageThreshExceededNotif'
_Q='csnSamplerAvailable'
_P='csnSamplerTotal'
_O='csnNetflowTableTotalEntries'
_N='csnUsageThreshExceedNotifEnable'
_M='csnNetflowDirectionType'
_L='Unsigned32'
_K='entPhysicalIndex'
_J='entPhysicalDescr'
_I='csnUtilization'
_H='csnUsageInterval'
_G='csnUsageThreshold'
_F='ENTITY-MIB'
_E='read-only'
_D='csnUsageDirection'
_C='read-write'
_B='CISCO-SWITCH-NETFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalDescr,entPhysicalIndex=mibBuilder.importSymbols(_F,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoSwitchNetflowMIB=ModuleIdentity((1,3,6,1,4,1,9,9,737))
if mibBuilder.loadTexts:ciscoSwitchNetflowMIB.setRevisions(('2010-05-26 00:00',))
class CsnNetflowDirectionTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('ingress',2),('egress',3),('ingressAndEgress',4)))
_CiscoSwitchNetflowMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoSwitchNetflowMIBNotifs=_CiscoSwitchNetflowMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,737,0))
_CiscoSwitchNetflowMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSwitchNetflowMIBObjects=_CiscoSwitchNetflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,737,1))
_CsnAccounting_ObjectIdentity=ObjectIdentity
csnAccounting=_CsnAccounting_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1))
_CsnAccGlobal_ObjectIdentity=ObjectIdentity
csnAccGlobal=_CsnAccGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,1))
_CsnNetflowDirectionType_Type=CsnNetflowDirectionTypes
_CsnNetflowDirectionType_Object=MibScalar
csnNetflowDirectionType=_CsnNetflowDirectionType_Object((1,3,6,1,4,1,9,9,737,1,1,1,1),_CsnNetflowDirectionType_Type())
csnNetflowDirectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:csnNetflowDirectionType.setStatus(_A)
_CsnAccNotifControl_ObjectIdentity=ObjectIdentity
csnAccNotifControl=_CsnAccNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,2))
_CsnUsageThreshExceedNotifEnable_Type=TruthValue
_CsnUsageThreshExceedNotifEnable_Object=MibScalar
csnUsageThreshExceedNotifEnable=_CsnUsageThreshExceedNotifEnable_Object((1,3,6,1,4,1,9,9,737,1,1,2,1),_CsnUsageThreshExceedNotifEnable_Type())
csnUsageThreshExceedNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:csnUsageThreshExceedNotifEnable.setStatus(_A)
_CshAccUsageThresh_ObjectIdentity=ObjectIdentity
cshAccUsageThresh=_CshAccUsageThresh_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,3))
_CsnUsageThreshTable_Object=MibTable
csnUsageThreshTable=_CsnUsageThreshTable_Object((1,3,6,1,4,1,9,9,737,1,1,3,1))
if mibBuilder.loadTexts:csnUsageThreshTable.setStatus(_A)
_CsnUsageThreshEntry_Object=MibTableRow
csnUsageThreshEntry=_CsnUsageThreshEntry_Object((1,3,6,1,4,1,9,9,737,1,1,3,1,1))
csnUsageThreshEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:csnUsageThreshEntry.setStatus(_A)
_CsnUsageDirection_Type=CsnNetflowDirectionTypes
_CsnUsageDirection_Object=MibTableColumn
csnUsageDirection=_CsnUsageDirection_Object((1,3,6,1,4,1,9,9,737,1,1,3,1,1,1),_CsnUsageDirection_Type())
csnUsageDirection.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:csnUsageDirection.setStatus(_A)
_CsnUsageThreshold_Type=Percent
_CsnUsageThreshold_Object=MibTableColumn
csnUsageThreshold=_CsnUsageThreshold_Object((1,3,6,1,4,1,9,9,737,1,1,3,1,1,2),_CsnUsageThreshold_Type())
csnUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:csnUsageThreshold.setStatus(_A)
class _CsnUsageInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CsnUsageInterval_Type.__name__=_L
_CsnUsageInterval_Object=MibTableColumn
csnUsageInterval=_CsnUsageInterval_Object((1,3,6,1,4,1,9,9,737,1,1,3,1,1,3),_CsnUsageInterval_Type())
csnUsageInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:csnUsageInterval.setStatus(_A)
if mibBuilder.loadTexts:csnUsageInterval.setUnits('seconds')
_CsnAccUtilization_ObjectIdentity=ObjectIdentity
csnAccUtilization=_CsnAccUtilization_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,4))
_CsnUtilizationTable_Object=MibTable
csnUtilizationTable=_CsnUtilizationTable_Object((1,3,6,1,4,1,9,9,737,1,1,4,1))
if mibBuilder.loadTexts:csnUtilizationTable.setStatus(_A)
_CsnUtilizationEntry_Object=MibTableRow
csnUtilizationEntry=_CsnUtilizationEntry_Object((1,3,6,1,4,1,9,9,737,1,1,4,1,1))
csnUtilizationEntry.setIndexNames((0,_F,_K),(0,_B,_D))
if mibBuilder.loadTexts:csnUtilizationEntry.setStatus(_A)
_CsnUtilization_Type=Percent
_CsnUtilization_Object=MibTableColumn
csnUtilization=_CsnUtilization_Object((1,3,6,1,4,1,9,9,737,1,1,4,1,1,1),_CsnUtilization_Type())
csnUtilization.setMaxAccess(_E)
if mibBuilder.loadTexts:csnUtilization.setStatus(_A)
_CsnAccNetflowTableSize_ObjectIdentity=ObjectIdentity
csnAccNetflowTableSize=_CsnAccNetflowTableSize_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,5))
_CsnNetflowTableSizeTable_Object=MibTable
csnNetflowTableSizeTable=_CsnNetflowTableSizeTable_Object((1,3,6,1,4,1,9,9,737,1,1,5,1))
if mibBuilder.loadTexts:csnNetflowTableSizeTable.setStatus(_A)
_CsnNetflowTableSizeEntry_Object=MibTableRow
csnNetflowTableSizeEntry=_CsnNetflowTableSizeEntry_Object((1,3,6,1,4,1,9,9,737,1,1,5,1,1))
csnNetflowTableSizeEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:csnNetflowTableSizeEntry.setStatus(_A)
_CsnNetflowTableTotalEntries_Type=Unsigned32
_CsnNetflowTableTotalEntries_Object=MibTableColumn
csnNetflowTableTotalEntries=_CsnNetflowTableTotalEntries_Object((1,3,6,1,4,1,9,9,737,1,1,5,1,1,1),_CsnNetflowTableTotalEntries_Type())
csnNetflowTableTotalEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:csnNetflowTableTotalEntries.setStatus(_A)
_CsnAccSampler_ObjectIdentity=ObjectIdentity
csnAccSampler=_CsnAccSampler_ObjectIdentity((1,3,6,1,4,1,9,9,737,1,1,6))
_CsnSamplerTotal_Type=Unsigned32
_CsnSamplerTotal_Object=MibScalar
csnSamplerTotal=_CsnSamplerTotal_Object((1,3,6,1,4,1,9,9,737,1,1,6,1),_CsnSamplerTotal_Type())
csnSamplerTotal.setMaxAccess(_E)
if mibBuilder.loadTexts:csnSamplerTotal.setStatus(_A)
_CsnSamplerAvailable_Type=Unsigned32
_CsnSamplerAvailable_Object=MibScalar
csnSamplerAvailable=_CsnSamplerAvailable_Object((1,3,6,1,4,1,9,9,737,1,1,6,2),_CsnSamplerAvailable_Type())
csnSamplerAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:csnSamplerAvailable.setStatus(_A)
_CiscoSwitchNetflowMIBConform_ObjectIdentity=ObjectIdentity
ciscoSwitchNetflowMIBConform=_CiscoSwitchNetflowMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,737,2))
_CsnMIBCompliances_ObjectIdentity=ObjectIdentity
csnMIBCompliances=_CsnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,737,2,1))
_CsnMIBGroups_ObjectIdentity=ObjectIdentity
csnMIBGroups=_CsnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,737,2,2))
csnGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,1))
csnGlobalGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:csnGlobalGroup.setStatus(_A)
csnUsageThreshNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,2))
csnUsageThreshNotifControlGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:csnUsageThreshNotifControlGroup.setStatus(_A)
csnUsageThreshGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,3))
csnUsageThreshGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:csnUsageThreshGroup.setStatus(_A)
csnUtilizationGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,4))
csnUtilizationGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:csnUtilizationGroup.setStatus(_A)
csnNetflowTableSizeGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,6))
csnNetflowTableSizeGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:csnNetflowTableSizeGroup.setStatus(_A)
csnSamplerGroup=ObjectGroup((1,3,6,1,4,1,9,9,737,2,2,7))
csnSamplerGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:csnSamplerGroup.setStatus(_A)
csnUsageThreshExceededNotif=NotificationType((1,3,6,1,4,1,9,9,737,0,1))
csnUsageThreshExceededNotif.setObjects(*((_F,_J),(_B,_I),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:csnUsageThreshExceededNotif.setStatus(_A)
csnUsageThreshNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,737,2,2,5))
csnUsageThreshNotifGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:csnUsageThreshNotifGroup.setStatus(_A)
csnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,737,2,1,1))
csnMIBCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:csnMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CsnNetflowDirectionTypes':CsnNetflowDirectionTypes,'ciscoSwitchNetflowMIB':ciscoSwitchNetflowMIB,'ciscoSwitchNetflowMIBNotifs':ciscoSwitchNetflowMIBNotifs,_R:csnUsageThreshExceededNotif,'ciscoSwitchNetflowMIBObjects':ciscoSwitchNetflowMIBObjects,'csnAccounting':csnAccounting,'csnAccGlobal':csnAccGlobal,_M:csnNetflowDirectionType,'csnAccNotifControl':csnAccNotifControl,_N:csnUsageThreshExceedNotifEnable,'cshAccUsageThresh':cshAccUsageThresh,'csnUsageThreshTable':csnUsageThreshTable,'csnUsageThreshEntry':csnUsageThreshEntry,_D:csnUsageDirection,_G:csnUsageThreshold,_H:csnUsageInterval,'csnAccUtilization':csnAccUtilization,'csnUtilizationTable':csnUtilizationTable,'csnUtilizationEntry':csnUtilizationEntry,_I:csnUtilization,'csnAccNetflowTableSize':csnAccNetflowTableSize,'csnNetflowTableSizeTable':csnNetflowTableSizeTable,'csnNetflowTableSizeEntry':csnNetflowTableSizeEntry,_O:csnNetflowTableTotalEntries,'csnAccSampler':csnAccSampler,_P:csnSamplerTotal,_Q:csnSamplerAvailable,'ciscoSwitchNetflowMIBConform':ciscoSwitchNetflowMIBConform,'csnMIBCompliances':csnMIBCompliances,'csnMIBCompliance':csnMIBCompliance,'csnMIBGroups':csnMIBGroups,_S:csnGlobalGroup,_T:csnUsageThreshNotifControlGroup,_U:csnUsageThreshGroup,_V:csnUtilizationGroup,_W:csnUsageThreshNotifGroup,_X:csnNetflowTableSizeGroup,_Y:csnSamplerGroup})