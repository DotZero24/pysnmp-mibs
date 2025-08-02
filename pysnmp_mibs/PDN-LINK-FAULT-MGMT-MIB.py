_T='pdnLinkFaultMgmtGeneralGroup'
_S='pdnLinkFailureSfBerThreshold'
_R='pdnLinkFailureSdBerThreshold'
_Q='pdnLinkFailureSfPeriodBeforeSwitching'
_P='pdnLinkFailureSdPeriodBeforeSwitching'
_O='pdnLinkFailureAISLPeriodBeforeSwitching'
_N='pdnLinkFailureLOFPeriodBeforeSwitching'
_M='pdnLinkFailureLOSPeriodBeforeSwitching'
_L='pdnDualLinkSelection'
_K='pdnLinkFaultMgmtSwitchoverSelection'
_J='pdnLinkFaultMgmtApsSelection'
_I='ifIndex'
_H='IF-MIB'
_G='disabled'
_F='enabled'
_E='seconds'
_D='read-write'
_C='Integer32'
_B='PDN-LINK-FAULT-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
pdnLinkFaultMgmt,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnLinkFaultMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnLinkFaultMgmtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,40,1))
if mibBuilder.loadTexts:pdnLinkFaultMgmtMIB.setRevisions(('2003-04-23 18:00',))
_PdnLinkFaultMgmtMIBObjects_ObjectIdentity=ObjectIdentity
pdnLinkFaultMgmtMIBObjects=_PdnLinkFaultMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,40,1,1))
class _PdnLinkFaultMgmtApsSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PdnLinkFaultMgmtApsSelection_Type.__name__=_C
_PdnLinkFaultMgmtApsSelection_Object=MibScalar
pdnLinkFaultMgmtApsSelection=_PdnLinkFaultMgmtApsSelection_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,1),_PdnLinkFaultMgmtApsSelection_Type())
pdnLinkFaultMgmtApsSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFaultMgmtApsSelection.setStatus(_A)
class _PdnLinkFaultMgmtSwitchoverSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PdnLinkFaultMgmtSwitchoverSelection_Type.__name__=_C
_PdnLinkFaultMgmtSwitchoverSelection_Object=MibScalar
pdnLinkFaultMgmtSwitchoverSelection=_PdnLinkFaultMgmtSwitchoverSelection_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,2),_PdnLinkFaultMgmtSwitchoverSelection_Type())
pdnLinkFaultMgmtSwitchoverSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFaultMgmtSwitchoverSelection.setStatus(_A)
_PdnLinkFailureConfigTable_Object=MibTable
pdnLinkFailureConfigTable=_PdnLinkFailureConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3))
if mibBuilder.loadTexts:pdnLinkFailureConfigTable.setStatus(_A)
_PdnLinkFailureConfigEntry_Object=MibTableRow
pdnLinkFailureConfigEntry=_PdnLinkFailureConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1))
pdnLinkFailureConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pdnLinkFailureConfigEntry.setStatus(_A)
class _PdnLinkFailureLOSPeriodBeforeSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PdnLinkFailureLOSPeriodBeforeSwitching_Type.__name__=_C
_PdnLinkFailureLOSPeriodBeforeSwitching_Object=MibTableColumn
pdnLinkFailureLOSPeriodBeforeSwitching=_PdnLinkFailureLOSPeriodBeforeSwitching_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,1),_PdnLinkFailureLOSPeriodBeforeSwitching_Type())
pdnLinkFailureLOSPeriodBeforeSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureLOSPeriodBeforeSwitching.setStatus(_A)
if mibBuilder.loadTexts:pdnLinkFailureLOSPeriodBeforeSwitching.setUnits(_E)
class _PdnLinkFailureLOFPeriodBeforeSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PdnLinkFailureLOFPeriodBeforeSwitching_Type.__name__=_C
_PdnLinkFailureLOFPeriodBeforeSwitching_Object=MibTableColumn
pdnLinkFailureLOFPeriodBeforeSwitching=_PdnLinkFailureLOFPeriodBeforeSwitching_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,2),_PdnLinkFailureLOFPeriodBeforeSwitching_Type())
pdnLinkFailureLOFPeriodBeforeSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureLOFPeriodBeforeSwitching.setStatus(_A)
if mibBuilder.loadTexts:pdnLinkFailureLOFPeriodBeforeSwitching.setUnits(_E)
class _PdnLinkFailureAISLPeriodBeforeSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PdnLinkFailureAISLPeriodBeforeSwitching_Type.__name__=_C
_PdnLinkFailureAISLPeriodBeforeSwitching_Object=MibTableColumn
pdnLinkFailureAISLPeriodBeforeSwitching=_PdnLinkFailureAISLPeriodBeforeSwitching_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,3),_PdnLinkFailureAISLPeriodBeforeSwitching_Type())
pdnLinkFailureAISLPeriodBeforeSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureAISLPeriodBeforeSwitching.setStatus(_A)
if mibBuilder.loadTexts:pdnLinkFailureAISLPeriodBeforeSwitching.setUnits(_E)
class _PdnLinkFailureSdPeriodBeforeSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PdnLinkFailureSdPeriodBeforeSwitching_Type.__name__=_C
_PdnLinkFailureSdPeriodBeforeSwitching_Object=MibTableColumn
pdnLinkFailureSdPeriodBeforeSwitching=_PdnLinkFailureSdPeriodBeforeSwitching_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,4),_PdnLinkFailureSdPeriodBeforeSwitching_Type())
pdnLinkFailureSdPeriodBeforeSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureSdPeriodBeforeSwitching.setStatus(_A)
if mibBuilder.loadTexts:pdnLinkFailureSdPeriodBeforeSwitching.setUnits(_E)
class _PdnLinkFailureSfPeriodBeforeSwitching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PdnLinkFailureSfPeriodBeforeSwitching_Type.__name__=_C
_PdnLinkFailureSfPeriodBeforeSwitching_Object=MibTableColumn
pdnLinkFailureSfPeriodBeforeSwitching=_PdnLinkFailureSfPeriodBeforeSwitching_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,5),_PdnLinkFailureSfPeriodBeforeSwitching_Type())
pdnLinkFailureSfPeriodBeforeSwitching.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureSfPeriodBeforeSwitching.setStatus(_A)
if mibBuilder.loadTexts:pdnLinkFailureSfPeriodBeforeSwitching.setUnits(_E)
class _PdnLinkFailureSdBerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_PdnLinkFailureSdBerThreshold_Type.__name__=_C
_PdnLinkFailureSdBerThreshold_Object=MibTableColumn
pdnLinkFailureSdBerThreshold=_PdnLinkFailureSdBerThreshold_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,6),_PdnLinkFailureSdBerThreshold_Type())
pdnLinkFailureSdBerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureSdBerThreshold.setStatus(_A)
class _PdnLinkFailureSfBerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_PdnLinkFailureSfBerThreshold_Type.__name__=_C
_PdnLinkFailureSfBerThreshold_Object=MibTableColumn
pdnLinkFailureSfBerThreshold=_PdnLinkFailureSfBerThreshold_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,3,1,7),_PdnLinkFailureSfBerThreshold_Type())
pdnLinkFailureSfBerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnLinkFailureSfBerThreshold.setStatus(_A)
class _PdnDualLinkSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PdnDualLinkSelection_Type.__name__=_C
_PdnDualLinkSelection_Object=MibScalar
pdnDualLinkSelection=_PdnDualLinkSelection_Object((1,3,6,1,4,1,1795,2,24,2,40,1,1,4),_PdnDualLinkSelection_Type())
pdnDualLinkSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDualLinkSelection.setStatus(_A)
_PdnLinkFaultMgmtMIBConformance_ObjectIdentity=ObjectIdentity
pdnLinkFaultMgmtMIBConformance=_PdnLinkFaultMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,40,1,2))
_PdnLinkFaultMgmtCompliances_ObjectIdentity=ObjectIdentity
pdnLinkFaultMgmtCompliances=_PdnLinkFaultMgmtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,40,1,2,1))
_PdnLinkFaultMgmtGroups_ObjectIdentity=ObjectIdentity
pdnLinkFaultMgmtGroups=_PdnLinkFaultMgmtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,40,1,2,2))
pdnLinkFaultMgmtGeneralGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,40,1,2,2,1))
pdnLinkFaultMgmtGeneralGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:pdnLinkFaultMgmtGeneralGroup.setStatus(_A)
pdnLinkSwitchoverGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,40,1,2,2,2))
pdnLinkSwitchoverGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:pdnLinkSwitchoverGroup.setStatus(_A)
pdnLinkFaultMgmtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,40,1,2,1,1))
pdnLinkFaultMgmtCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:pdnLinkFaultMgmtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnLinkFaultMgmtMIB':pdnLinkFaultMgmtMIB,'pdnLinkFaultMgmtMIBObjects':pdnLinkFaultMgmtMIBObjects,_J:pdnLinkFaultMgmtApsSelection,_K:pdnLinkFaultMgmtSwitchoverSelection,'pdnLinkFailureConfigTable':pdnLinkFailureConfigTable,'pdnLinkFailureConfigEntry':pdnLinkFailureConfigEntry,_M:pdnLinkFailureLOSPeriodBeforeSwitching,_N:pdnLinkFailureLOFPeriodBeforeSwitching,_O:pdnLinkFailureAISLPeriodBeforeSwitching,_P:pdnLinkFailureSdPeriodBeforeSwitching,_Q:pdnLinkFailureSfPeriodBeforeSwitching,_R:pdnLinkFailureSdBerThreshold,_S:pdnLinkFailureSfBerThreshold,_L:pdnDualLinkSelection,'pdnLinkFaultMgmtMIBConformance':pdnLinkFaultMgmtMIBConformance,'pdnLinkFaultMgmtCompliances':pdnLinkFaultMgmtCompliances,'pdnLinkFaultMgmtCompliance':pdnLinkFaultMgmtCompliance,'pdnLinkFaultMgmtGroups':pdnLinkFaultMgmtGroups,_T:pdnLinkFaultMgmtGeneralGroup,'pdnLinkSwitchoverGroup':pdnLinkSwitchoverGroup})