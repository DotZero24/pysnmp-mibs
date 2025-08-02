_Y='cfaInterworkGroup'
_X='cfaAdapterGroup'
_W='cfaInterworkIfTxAllocRate'
_V='cfaInterworkIfRxAllocRate'
_U='cfaInterworkIfTxAvailRate'
_T='cfaInterworkIfRxAvailRate'
_S='cfaAdapterIfOverbooking'
_R='cfaAdapterIfVbrServOflow'
_Q='cfaAdapterIfVcQOutqMarkThresh'
_P='cfaAdapterIfVcQInqMarkThresh'
_O='cfaAdapterIfVcQOutqDiscThresh'
_N='cfaAdapterIfVcQInqDiscThresh'
_M='cfaInterworkIfVcQService'
_L='not-accessible'
_K='cfaAdapterIfVcQService'
_J='TruthValue'
_I='bits-per-second'
_H='read-only'
_G='percent'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='CISCO-ATM-SWITCH-FR-RM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
ciscoAtmSwitchFrRmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,110))
class CfaInterworkServiceCategory(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vbrNrt',1),('abr',2),('ubr',3)))
_CiscoAtmSwitchFrRmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrRmMIBObjects=_CiscoAtmSwitchFrRmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,110,1))
_CfaAdapter_ObjectIdentity=ObjectIdentity
cfaAdapter=_CfaAdapter_ObjectIdentity((1,3,6,1,4,1,9,9,110,1,1))
_CfaAdapterIfVcQThresholdTable_Object=MibTable
cfaAdapterIfVcQThresholdTable=_CfaAdapterIfVcQThresholdTable_Object((1,3,6,1,4,1,9,9,110,1,1,1))
if mibBuilder.loadTexts:cfaAdapterIfVcQThresholdTable.setStatus(_A)
_CfaAdapterIfVcQThresholdEntry_Object=MibTableRow
cfaAdapterIfVcQThresholdEntry=_CfaAdapterIfVcQThresholdEntry_Object((1,3,6,1,4,1,9,9,110,1,1,1,1))
cfaAdapterIfVcQThresholdEntry.setIndexNames((0,_E,_F),(0,_B,_K))
if mibBuilder.loadTexts:cfaAdapterIfVcQThresholdEntry.setStatus(_A)
_CfaAdapterIfVcQService_Type=CfaInterworkServiceCategory
_CfaAdapterIfVcQService_Object=MibTableColumn
cfaAdapterIfVcQService=_CfaAdapterIfVcQService_Object((1,3,6,1,4,1,9,9,110,1,1,1,1,1),_CfaAdapterIfVcQService_Type())
cfaAdapterIfVcQService.setMaxAccess(_L)
if mibBuilder.loadTexts:cfaAdapterIfVcQService.setStatus(_A)
class _CfaAdapterIfVcQInqDiscThresh_Type(Integer32):defaultValue=87;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CfaAdapterIfVcQInqDiscThresh_Type.__name__=_C
_CfaAdapterIfVcQInqDiscThresh_Object=MibTableColumn
cfaAdapterIfVcQInqDiscThresh=_CfaAdapterIfVcQInqDiscThresh_Object((1,3,6,1,4,1,9,9,110,1,1,1,1,2),_CfaAdapterIfVcQInqDiscThresh_Type())
cfaAdapterIfVcQInqDiscThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfVcQInqDiscThresh.setStatus(_A)
if mibBuilder.loadTexts:cfaAdapterIfVcQInqDiscThresh.setUnits(_G)
class _CfaAdapterIfVcQOutqDiscThresh_Type(Integer32):defaultValue=87;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CfaAdapterIfVcQOutqDiscThresh_Type.__name__=_C
_CfaAdapterIfVcQOutqDiscThresh_Object=MibTableColumn
cfaAdapterIfVcQOutqDiscThresh=_CfaAdapterIfVcQOutqDiscThresh_Object((1,3,6,1,4,1,9,9,110,1,1,1,1,3),_CfaAdapterIfVcQOutqDiscThresh_Type())
cfaAdapterIfVcQOutqDiscThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfVcQOutqDiscThresh.setStatus(_A)
if mibBuilder.loadTexts:cfaAdapterIfVcQOutqDiscThresh.setUnits(_G)
class _CfaAdapterIfVcQInqMarkThresh_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CfaAdapterIfVcQInqMarkThresh_Type.__name__=_C
_CfaAdapterIfVcQInqMarkThresh_Object=MibTableColumn
cfaAdapterIfVcQInqMarkThresh=_CfaAdapterIfVcQInqMarkThresh_Object((1,3,6,1,4,1,9,9,110,1,1,1,1,4),_CfaAdapterIfVcQInqMarkThresh_Type())
cfaAdapterIfVcQInqMarkThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfVcQInqMarkThresh.setStatus(_A)
if mibBuilder.loadTexts:cfaAdapterIfVcQInqMarkThresh.setUnits(_G)
class _CfaAdapterIfVcQOutqMarkThresh_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CfaAdapterIfVcQOutqMarkThresh_Type.__name__=_C
_CfaAdapterIfVcQOutqMarkThresh_Object=MibTableColumn
cfaAdapterIfVcQOutqMarkThresh=_CfaAdapterIfVcQOutqMarkThresh_Object((1,3,6,1,4,1,9,9,110,1,1,1,1,5),_CfaAdapterIfVcQOutqMarkThresh_Type())
cfaAdapterIfVcQOutqMarkThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfVcQOutqMarkThresh.setStatus(_A)
if mibBuilder.loadTexts:cfaAdapterIfVcQOutqMarkThresh.setUnits(_G)
_CfaAdapterIfVbrServOflowTable_Object=MibTable
cfaAdapterIfVbrServOflowTable=_CfaAdapterIfVbrServOflowTable_Object((1,3,6,1,4,1,9,9,110,1,1,2))
if mibBuilder.loadTexts:cfaAdapterIfVbrServOflowTable.setStatus(_A)
_CfaAdapterIfVbrServOflowEntry_Object=MibTableRow
cfaAdapterIfVbrServOflowEntry=_CfaAdapterIfVbrServOflowEntry_Object((1,3,6,1,4,1,9,9,110,1,1,2,1))
cfaAdapterIfVbrServOflowEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cfaAdapterIfVbrServOflowEntry.setStatus(_A)
class _CfaAdapterIfVbrServOflow_Type(TruthValue):defaultValue=1
_CfaAdapterIfVbrServOflow_Type.__name__=_J
_CfaAdapterIfVbrServOflow_Object=MibTableColumn
cfaAdapterIfVbrServOflow=_CfaAdapterIfVbrServOflow_Object((1,3,6,1,4,1,9,9,110,1,1,2,1,1),_CfaAdapterIfVbrServOflow_Type())
cfaAdapterIfVbrServOflow.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfVbrServOflow.setStatus(_A)
_CfaAdapterIfFrConfigTable_Object=MibTable
cfaAdapterIfFrConfigTable=_CfaAdapterIfFrConfigTable_Object((1,3,6,1,4,1,9,9,110,1,1,3))
if mibBuilder.loadTexts:cfaAdapterIfFrConfigTable.setStatus(_A)
_CfaAdapterIfFrConfigEntry_Object=MibTableRow
cfaAdapterIfFrConfigEntry=_CfaAdapterIfFrConfigEntry_Object((1,3,6,1,4,1,9,9,110,1,1,3,1))
cfaAdapterIfFrConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cfaAdapterIfFrConfigEntry.setStatus(_A)
class _CfaAdapterIfOverbooking_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CfaAdapterIfOverbooking_Type.__name__=_C
_CfaAdapterIfOverbooking_Object=MibTableColumn
cfaAdapterIfOverbooking=_CfaAdapterIfOverbooking_Object((1,3,6,1,4,1,9,9,110,1,1,3,1,1),_CfaAdapterIfOverbooking_Type())
cfaAdapterIfOverbooking.setMaxAccess(_D)
if mibBuilder.loadTexts:cfaAdapterIfOverbooking.setStatus(_A)
if mibBuilder.loadTexts:cfaAdapterIfOverbooking.setUnits(_G)
_CfaInterwork_ObjectIdentity=ObjectIdentity
cfaInterwork=_CfaInterwork_ObjectIdentity((1,3,6,1,4,1,9,9,110,1,2))
_CfaInterworkIfResourceTable_Object=MibTable
cfaInterworkIfResourceTable=_CfaInterworkIfResourceTable_Object((1,3,6,1,4,1,9,9,110,1,2,1))
if mibBuilder.loadTexts:cfaInterworkIfResourceTable.setStatus(_A)
_CfaInterworkIfResourceEntry_Object=MibTableRow
cfaInterworkIfResourceEntry=_CfaInterworkIfResourceEntry_Object((1,3,6,1,4,1,9,9,110,1,2,1,1))
cfaInterworkIfResourceEntry.setIndexNames((0,_E,_F),(0,_B,_M))
if mibBuilder.loadTexts:cfaInterworkIfResourceEntry.setStatus(_A)
_CfaInterworkIfVcQService_Type=CfaInterworkServiceCategory
_CfaInterworkIfVcQService_Object=MibTableColumn
cfaInterworkIfVcQService=_CfaInterworkIfVcQService_Object((1,3,6,1,4,1,9,9,110,1,2,1,1,1),_CfaInterworkIfVcQService_Type())
cfaInterworkIfVcQService.setMaxAccess(_L)
if mibBuilder.loadTexts:cfaInterworkIfVcQService.setStatus(_A)
_CfaInterworkIfRxAvailRate_Type=Gauge32
_CfaInterworkIfRxAvailRate_Object=MibTableColumn
cfaInterworkIfRxAvailRate=_CfaInterworkIfRxAvailRate_Object((1,3,6,1,4,1,9,9,110,1,2,1,1,2),_CfaInterworkIfRxAvailRate_Type())
cfaInterworkIfRxAvailRate.setMaxAccess(_H)
if mibBuilder.loadTexts:cfaInterworkIfRxAvailRate.setStatus(_A)
if mibBuilder.loadTexts:cfaInterworkIfRxAvailRate.setUnits(_I)
_CfaInterworkIfTxAvailRate_Type=Gauge32
_CfaInterworkIfTxAvailRate_Object=MibTableColumn
cfaInterworkIfTxAvailRate=_CfaInterworkIfTxAvailRate_Object((1,3,6,1,4,1,9,9,110,1,2,1,1,3),_CfaInterworkIfTxAvailRate_Type())
cfaInterworkIfTxAvailRate.setMaxAccess(_H)
if mibBuilder.loadTexts:cfaInterworkIfTxAvailRate.setStatus(_A)
if mibBuilder.loadTexts:cfaInterworkIfTxAvailRate.setUnits(_I)
_CfaInterworkIfRxAllocRate_Type=Gauge32
_CfaInterworkIfRxAllocRate_Object=MibTableColumn
cfaInterworkIfRxAllocRate=_CfaInterworkIfRxAllocRate_Object((1,3,6,1,4,1,9,9,110,1,2,1,1,4),_CfaInterworkIfRxAllocRate_Type())
cfaInterworkIfRxAllocRate.setMaxAccess(_H)
if mibBuilder.loadTexts:cfaInterworkIfRxAllocRate.setStatus(_A)
if mibBuilder.loadTexts:cfaInterworkIfRxAllocRate.setUnits(_I)
_CfaInterworkIfTxAllocRate_Type=Gauge32
_CfaInterworkIfTxAllocRate_Object=MibTableColumn
cfaInterworkIfTxAllocRate=_CfaInterworkIfTxAllocRate_Object((1,3,6,1,4,1,9,9,110,1,2,1,1,5),_CfaInterworkIfTxAllocRate_Type())
cfaInterworkIfTxAllocRate.setMaxAccess(_H)
if mibBuilder.loadTexts:cfaInterworkIfTxAllocRate.setStatus(_A)
if mibBuilder.loadTexts:cfaInterworkIfTxAllocRate.setUnits(_I)
_CiscoAtmSwitchFrRmMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrRmMIBNotifications=_CiscoAtmSwitchFrRmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,110,2))
_CiscoAtmSwitchFrRmMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrRmMIBConformance=_CiscoAtmSwitchFrRmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,110,3))
_CiscoAtmSwitchFrRmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrRmMIBCompliances=_CiscoAtmSwitchFrRmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,110,3,1))
_CiscoAtmSwitchFrRmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmSwitchFrRmMIBGroups=_CiscoAtmSwitchFrRmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,110,3,2))
cfaAdapterGroup=ObjectGroup((1,3,6,1,4,1,9,9,110,3,2,1))
cfaAdapterGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cfaAdapterGroup.setStatus(_A)
cfaInterworkGroup=ObjectGroup((1,3,6,1,4,1,9,9,110,3,2,2))
cfaInterworkGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cfaInterworkGroup.setStatus(_A)
ciscoAtmSwitchFrRmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,110,3,1,1))
ciscoAtmSwitchFrRmMIBCompliance.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoAtmSwitchFrRmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CfaInterworkServiceCategory':CfaInterworkServiceCategory,'ciscoAtmSwitchFrRmMIB':ciscoAtmSwitchFrRmMIB,'ciscoAtmSwitchFrRmMIBObjects':ciscoAtmSwitchFrRmMIBObjects,'cfaAdapter':cfaAdapter,'cfaAdapterIfVcQThresholdTable':cfaAdapterIfVcQThresholdTable,'cfaAdapterIfVcQThresholdEntry':cfaAdapterIfVcQThresholdEntry,_K:cfaAdapterIfVcQService,_N:cfaAdapterIfVcQInqDiscThresh,_O:cfaAdapterIfVcQOutqDiscThresh,_P:cfaAdapterIfVcQInqMarkThresh,_Q:cfaAdapterIfVcQOutqMarkThresh,'cfaAdapterIfVbrServOflowTable':cfaAdapterIfVbrServOflowTable,'cfaAdapterIfVbrServOflowEntry':cfaAdapterIfVbrServOflowEntry,_R:cfaAdapterIfVbrServOflow,'cfaAdapterIfFrConfigTable':cfaAdapterIfFrConfigTable,'cfaAdapterIfFrConfigEntry':cfaAdapterIfFrConfigEntry,_S:cfaAdapterIfOverbooking,'cfaInterwork':cfaInterwork,'cfaInterworkIfResourceTable':cfaInterworkIfResourceTable,'cfaInterworkIfResourceEntry':cfaInterworkIfResourceEntry,_M:cfaInterworkIfVcQService,_T:cfaInterworkIfRxAvailRate,_U:cfaInterworkIfTxAvailRate,_V:cfaInterworkIfRxAllocRate,_W:cfaInterworkIfTxAllocRate,'ciscoAtmSwitchFrRmMIBNotifications':ciscoAtmSwitchFrRmMIBNotifications,'ciscoAtmSwitchFrRmMIBConformance':ciscoAtmSwitchFrRmMIBConformance,'ciscoAtmSwitchFrRmMIBCompliances':ciscoAtmSwitchFrRmMIBCompliances,'ciscoAtmSwitchFrRmMIBCompliance':ciscoAtmSwitchFrRmMIBCompliance,'ciscoAtmSwitchFrRmMIBGroups':ciscoAtmSwitchFrRmMIBGroups,_X:cfaAdapterGroup,_Y:cfaInterworkGroup})