_R='ciscoAtmDualPhyMIBGroup'
_Q='cadpStatAdminActivePhy'
_P='cadpStatUncorrectableHCSErrors'
_O='cadpStatCorrectableHCSErrors'
_N='cadpStatPathFEBErrors'
_M='cadpStatPathBIP8Errors'
_L='cadpStatLineFEBErrors'
_K='cadpStatLineBIP824Errors'
_J='cadpStatSectionBIP8Errors'
_I='cadpStatActive'
_H='cadpStatFarEndReceiveFailure'
_G='cadpStatLossOfSignal'
_F='ifIndex'
_E='IF-MIB'
_D='cadpStatOperActivePhy'
_C='read-only'
_B='CISCO-ATM-DUAL-PHY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','InterfaceIndexOrZero')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoAtmDualPhyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,60))
_CiscoAtmDualPhyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBObjects=_CiscoAtmDualPhyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,60,1))
_CadpStatistics_ObjectIdentity=ObjectIdentity
cadpStatistics=_CadpStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,60,1,1))
_CadpStatTable_Object=MibTable
cadpStatTable=_CadpStatTable_Object((1,3,6,1,4,1,9,9,60,1,1,1))
if mibBuilder.loadTexts:cadpStatTable.setStatus(_A)
_CadpStatEntry_Object=MibTableRow
cadpStatEntry=_CadpStatEntry_Object((1,3,6,1,4,1,9,9,60,1,1,1,1))
cadpStatEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cadpStatEntry.setStatus(_A)
_CadpStatLossOfSignal_Type=TruthValue
_CadpStatLossOfSignal_Object=MibTableColumn
cadpStatLossOfSignal=_CadpStatLossOfSignal_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,1),_CadpStatLossOfSignal_Type())
cadpStatLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatLossOfSignal.setStatus(_A)
_CadpStatFarEndReceiveFailure_Type=TruthValue
_CadpStatFarEndReceiveFailure_Object=MibTableColumn
cadpStatFarEndReceiveFailure=_CadpStatFarEndReceiveFailure_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,2),_CadpStatFarEndReceiveFailure_Type())
cadpStatFarEndReceiveFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatFarEndReceiveFailure.setStatus(_A)
_CadpStatActive_Type=TruthValue
_CadpStatActive_Object=MibTableColumn
cadpStatActive=_CadpStatActive_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,5),_CadpStatActive_Type())
cadpStatActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatActive.setStatus(_A)
_CadpStatSectionBIP8Errors_Type=Counter32
_CadpStatSectionBIP8Errors_Object=MibTableColumn
cadpStatSectionBIP8Errors=_CadpStatSectionBIP8Errors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,6),_CadpStatSectionBIP8Errors_Type())
cadpStatSectionBIP8Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatSectionBIP8Errors.setStatus(_A)
_CadpStatLineBIP824Errors_Type=Counter32
_CadpStatLineBIP824Errors_Object=MibTableColumn
cadpStatLineBIP824Errors=_CadpStatLineBIP824Errors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,7),_CadpStatLineBIP824Errors_Type())
cadpStatLineBIP824Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatLineBIP824Errors.setStatus(_A)
_CadpStatLineFEBErrors_Type=Counter32
_CadpStatLineFEBErrors_Object=MibTableColumn
cadpStatLineFEBErrors=_CadpStatLineFEBErrors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,8),_CadpStatLineFEBErrors_Type())
cadpStatLineFEBErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatLineFEBErrors.setStatus(_A)
_CadpStatPathBIP8Errors_Type=Counter32
_CadpStatPathBIP8Errors_Object=MibTableColumn
cadpStatPathBIP8Errors=_CadpStatPathBIP8Errors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,9),_CadpStatPathBIP8Errors_Type())
cadpStatPathBIP8Errors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatPathBIP8Errors.setStatus(_A)
_CadpStatPathFEBErrors_Type=Counter32
_CadpStatPathFEBErrors_Object=MibTableColumn
cadpStatPathFEBErrors=_CadpStatPathFEBErrors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,10),_CadpStatPathFEBErrors_Type())
cadpStatPathFEBErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatPathFEBErrors.setStatus(_A)
_CadpStatCorrectableHCSErrors_Type=Counter32
_CadpStatCorrectableHCSErrors_Object=MibTableColumn
cadpStatCorrectableHCSErrors=_CadpStatCorrectableHCSErrors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,11),_CadpStatCorrectableHCSErrors_Type())
cadpStatCorrectableHCSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatCorrectableHCSErrors.setStatus(_A)
_CadpStatUncorrectableHCSErrors_Type=Counter32
_CadpStatUncorrectableHCSErrors_Object=MibTableColumn
cadpStatUncorrectableHCSErrors=_CadpStatUncorrectableHCSErrors_Object((1,3,6,1,4,1,9,9,60,1,1,1,1,12),_CadpStatUncorrectableHCSErrors_Type())
cadpStatUncorrectableHCSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatUncorrectableHCSErrors.setStatus(_A)
_CadpStatOperActivePhy_Type=InterfaceIndexOrZero
_CadpStatOperActivePhy_Object=MibScalar
cadpStatOperActivePhy=_CadpStatOperActivePhy_Object((1,3,6,1,4,1,9,9,60,1,1,2),_CadpStatOperActivePhy_Type())
cadpStatOperActivePhy.setMaxAccess(_C)
if mibBuilder.loadTexts:cadpStatOperActivePhy.setStatus(_A)
_CadpStatAdminActivePhy_Type=InterfaceIndex
_CadpStatAdminActivePhy_Object=MibScalar
cadpStatAdminActivePhy=_CadpStatAdminActivePhy_Object((1,3,6,1,4,1,9,9,60,1,1,3),_CadpStatAdminActivePhy_Type())
cadpStatAdminActivePhy.setMaxAccess('read-write')
if mibBuilder.loadTexts:cadpStatAdminActivePhy.setStatus(_A)
_CiscoAtmDualPhyMIBTrapPrefix_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBTrapPrefix=_CiscoAtmDualPhyMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,60,2))
_CiscoAtmDualPhyMIBTraps_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBTraps=_CiscoAtmDualPhyMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,9,60,2,0))
_CiscoAtmDualPhyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBConformance=_CiscoAtmDualPhyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,60,3))
_CiscoAtmDualPhyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBCompliances=_CiscoAtmDualPhyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,60,3,1))
_CiscoAtmDualPhyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmDualPhyMIBGroups=_CiscoAtmDualPhyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,60,3,2))
ciscoAtmDualPhyMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,60,3,2,1))
ciscoAtmDualPhyMIBGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_D)))
if mibBuilder.loadTexts:ciscoAtmDualPhyMIBGroup.setStatus(_A)
ciscoAtmDualPhyChange=NotificationType((1,3,6,1,4,1,9,9,60,2,0,1))
ciscoAtmDualPhyChange.setObjects((_B,_D))
if mibBuilder.loadTexts:ciscoAtmDualPhyChange.setStatus(_A)
ciscoAtmDualPhyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,60,3,1,1))
ciscoAtmDualPhyMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoAtmDualPhyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAtmDualPhyMIB':ciscoAtmDualPhyMIB,'ciscoAtmDualPhyMIBObjects':ciscoAtmDualPhyMIBObjects,'cadpStatistics':cadpStatistics,'cadpStatTable':cadpStatTable,'cadpStatEntry':cadpStatEntry,_G:cadpStatLossOfSignal,_H:cadpStatFarEndReceiveFailure,_I:cadpStatActive,_J:cadpStatSectionBIP8Errors,_K:cadpStatLineBIP824Errors,_L:cadpStatLineFEBErrors,_M:cadpStatPathBIP8Errors,_N:cadpStatPathFEBErrors,_O:cadpStatCorrectableHCSErrors,_P:cadpStatUncorrectableHCSErrors,_D:cadpStatOperActivePhy,_Q:cadpStatAdminActivePhy,'ciscoAtmDualPhyMIBTrapPrefix':ciscoAtmDualPhyMIBTrapPrefix,'ciscoAtmDualPhyMIBTraps':ciscoAtmDualPhyMIBTraps,'ciscoAtmDualPhyChange':ciscoAtmDualPhyChange,'ciscoAtmDualPhyMIBConformance':ciscoAtmDualPhyMIBConformance,'ciscoAtmDualPhyMIBCompliances':ciscoAtmDualPhyMIBCompliances,'ciscoAtmDualPhyMIBCompliance':ciscoAtmDualPhyMIBCompliance,'ciscoAtmDualPhyMIBGroups':ciscoAtmDualPhyMIBGroups,_R:ciscoAtmDualPhyMIBGroup})