_T='ciscoWredMIBGroup'
_S='cwredStatMaxFilteredPkts'
_R='cwredStatRandomFilteredPkts'
_Q='cwredStatSwitchedPkts'
_P='cwredQueueDepth'
_O='cwredQueueAverage'
_N='cwredConfigPrecedPktsDropFraction'
_M='cwredConfigPrecedMaxDepthThreshold'
_L='cwredConfigPrecedMinDepthThreshold'
_K='cwredConfigGlobQueueWeight'
_J='cwredStatEntry'
_I='cwredQueueEntry'
_H='cwredConfigPrecedPrecedence'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='packets'
_C='read-only'
_B='CISCO-WRED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWredMIB=ModuleIdentity((1,3,6,1,4,1,9,9,83))
if mibBuilder.loadTexts:ciscoWredMIB.setRevisions(('1997-07-18 00:00',))
_CiscoWredMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWredMIBObjects=_CiscoWredMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,83,1))
_CwredConfig_ObjectIdentity=ObjectIdentity
cwredConfig=_CwredConfig_ObjectIdentity((1,3,6,1,4,1,9,9,83,1,1))
_CwredConfigGlobTable_Object=MibTable
cwredConfigGlobTable=_CwredConfigGlobTable_Object((1,3,6,1,4,1,9,9,83,1,1,1))
if mibBuilder.loadTexts:cwredConfigGlobTable.setStatus(_A)
_CwredConfigGlobEntry_Object=MibTableRow
cwredConfigGlobEntry=_CwredConfigGlobEntry_Object((1,3,6,1,4,1,9,9,83,1,1,1,1))
cwredConfigGlobEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:cwredConfigGlobEntry.setStatus(_A)
_CwredConfigGlobQueueWeight_Type=Integer32
_CwredConfigGlobQueueWeight_Object=MibTableColumn
cwredConfigGlobQueueWeight=_CwredConfigGlobQueueWeight_Object((1,3,6,1,4,1,9,9,83,1,1,1,1,1),_CwredConfigGlobQueueWeight_Type())
cwredConfigGlobQueueWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredConfigGlobQueueWeight.setStatus(_A)
_CwredConfigPrecedTable_Object=MibTable
cwredConfigPrecedTable=_CwredConfigPrecedTable_Object((1,3,6,1,4,1,9,9,83,1,1,2))
if mibBuilder.loadTexts:cwredConfigPrecedTable.setStatus(_A)
_CwredConfigPrecedEntry_Object=MibTableRow
cwredConfigPrecedEntry=_CwredConfigPrecedEntry_Object((1,3,6,1,4,1,9,9,83,1,1,2,1))
cwredConfigPrecedEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cwredConfigPrecedEntry.setStatus(_A)
class _CwredConfigPrecedPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CwredConfigPrecedPrecedence_Type.__name__=_G
_CwredConfigPrecedPrecedence_Object=MibTableColumn
cwredConfigPrecedPrecedence=_CwredConfigPrecedPrecedence_Object((1,3,6,1,4,1,9,9,83,1,1,2,1,1),_CwredConfigPrecedPrecedence_Type())
cwredConfigPrecedPrecedence.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cwredConfigPrecedPrecedence.setStatus(_A)
_CwredConfigPrecedMinDepthThreshold_Type=Integer32
_CwredConfigPrecedMinDepthThreshold_Object=MibTableColumn
cwredConfigPrecedMinDepthThreshold=_CwredConfigPrecedMinDepthThreshold_Object((1,3,6,1,4,1,9,9,83,1,1,2,1,2),_CwredConfigPrecedMinDepthThreshold_Type())
cwredConfigPrecedMinDepthThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredConfigPrecedMinDepthThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwredConfigPrecedMinDepthThreshold.setUnits(_D)
_CwredConfigPrecedMaxDepthThreshold_Type=Integer32
_CwredConfigPrecedMaxDepthThreshold_Object=MibTableColumn
cwredConfigPrecedMaxDepthThreshold=_CwredConfigPrecedMaxDepthThreshold_Object((1,3,6,1,4,1,9,9,83,1,1,2,1,3),_CwredConfigPrecedMaxDepthThreshold_Type())
cwredConfigPrecedMaxDepthThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredConfigPrecedMaxDepthThreshold.setStatus(_A)
if mibBuilder.loadTexts:cwredConfigPrecedMaxDepthThreshold.setUnits(_D)
_CwredConfigPrecedPktsDropFraction_Type=Integer32
_CwredConfigPrecedPktsDropFraction_Object=MibTableColumn
cwredConfigPrecedPktsDropFraction=_CwredConfigPrecedPktsDropFraction_Object((1,3,6,1,4,1,9,9,83,1,1,2,1,4),_CwredConfigPrecedPktsDropFraction_Type())
cwredConfigPrecedPktsDropFraction.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredConfigPrecedPktsDropFraction.setStatus(_A)
_CwredStats_ObjectIdentity=ObjectIdentity
cwredStats=_CwredStats_ObjectIdentity((1,3,6,1,4,1,9,9,83,1,2))
_CwredQueueTable_Object=MibTable
cwredQueueTable=_CwredQueueTable_Object((1,3,6,1,4,1,9,9,83,1,2,1))
if mibBuilder.loadTexts:cwredQueueTable.setStatus(_A)
_CwredQueueEntry_Object=MibTableRow
cwredQueueEntry=_CwredQueueEntry_Object((1,3,6,1,4,1,9,9,83,1,2,1,1))
if mibBuilder.loadTexts:cwredQueueEntry.setStatus(_A)
_CwredQueueAverage_Type=Gauge32
_CwredQueueAverage_Object=MibTableColumn
cwredQueueAverage=_CwredQueueAverage_Object((1,3,6,1,4,1,9,9,83,1,2,1,1,1),_CwredQueueAverage_Type())
cwredQueueAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredQueueAverage.setStatus(_A)
if mibBuilder.loadTexts:cwredQueueAverage.setUnits(_D)
_CwredQueueDepth_Type=Gauge32
_CwredQueueDepth_Object=MibTableColumn
cwredQueueDepth=_CwredQueueDepth_Object((1,3,6,1,4,1,9,9,83,1,2,1,1,2),_CwredQueueDepth_Type())
cwredQueueDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredQueueDepth.setStatus(_A)
if mibBuilder.loadTexts:cwredQueueDepth.setUnits(_D)
_CwredStatTable_Object=MibTable
cwredStatTable=_CwredStatTable_Object((1,3,6,1,4,1,9,9,83,1,2,2))
if mibBuilder.loadTexts:cwredStatTable.setStatus(_A)
_CwredStatEntry_Object=MibTableRow
cwredStatEntry=_CwredStatEntry_Object((1,3,6,1,4,1,9,9,83,1,2,2,1))
if mibBuilder.loadTexts:cwredStatEntry.setStatus(_A)
_CwredStatSwitchedPkts_Type=Counter32
_CwredStatSwitchedPkts_Object=MibTableColumn
cwredStatSwitchedPkts=_CwredStatSwitchedPkts_Object((1,3,6,1,4,1,9,9,83,1,2,2,1,1),_CwredStatSwitchedPkts_Type())
cwredStatSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredStatSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cwredStatSwitchedPkts.setUnits(_D)
_CwredStatRandomFilteredPkts_Type=Counter32
_CwredStatRandomFilteredPkts_Object=MibTableColumn
cwredStatRandomFilteredPkts=_CwredStatRandomFilteredPkts_Object((1,3,6,1,4,1,9,9,83,1,2,2,1,2),_CwredStatRandomFilteredPkts_Type())
cwredStatRandomFilteredPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredStatRandomFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:cwredStatRandomFilteredPkts.setUnits(_D)
_CwredStatMaxFilteredPkts_Type=Counter32
_CwredStatMaxFilteredPkts_Object=MibTableColumn
cwredStatMaxFilteredPkts=_CwredStatMaxFilteredPkts_Object((1,3,6,1,4,1,9,9,83,1,2,2,1,3),_CwredStatMaxFilteredPkts_Type())
cwredStatMaxFilteredPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cwredStatMaxFilteredPkts.setStatus(_A)
if mibBuilder.loadTexts:cwredStatMaxFilteredPkts.setUnits(_D)
_CiscoWredMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWredMIBConformance=_CiscoWredMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,83,3))
_CiscoWredMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWredMIBCompliances=_CiscoWredMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,83,3,1))
_CiscoWredMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWredMIBGroups=_CiscoWredMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,83,3,2))
cwredConfigGlobEntry.registerAugmentions((_B,_I))
cwredQueueEntry.setIndexNames(*cwredConfigGlobEntry.getIndexNames())
cwredConfigPrecedEntry.registerAugmentions((_B,_J))
cwredStatEntry.setIndexNames(*cwredConfigPrecedEntry.getIndexNames())
ciscoWredMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,83,3,2,1))
ciscoWredMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoWredMIBGroup.setStatus(_A)
ciscoWredMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,83,3,1,1))
ciscoWredMIBCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:ciscoWredMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWredMIB':ciscoWredMIB,'ciscoWredMIBObjects':ciscoWredMIBObjects,'cwredConfig':cwredConfig,'cwredConfigGlobTable':cwredConfigGlobTable,'cwredConfigGlobEntry':cwredConfigGlobEntry,_K:cwredConfigGlobQueueWeight,'cwredConfigPrecedTable':cwredConfigPrecedTable,'cwredConfigPrecedEntry':cwredConfigPrecedEntry,_H:cwredConfigPrecedPrecedence,_L:cwredConfigPrecedMinDepthThreshold,_M:cwredConfigPrecedMaxDepthThreshold,_N:cwredConfigPrecedPktsDropFraction,'cwredStats':cwredStats,'cwredQueueTable':cwredQueueTable,_I:cwredQueueEntry,_O:cwredQueueAverage,_P:cwredQueueDepth,'cwredStatTable':cwredStatTable,_J:cwredStatEntry,_Q:cwredStatSwitchedPkts,_R:cwredStatRandomFilteredPkts,_S:cwredStatMaxFilteredPkts,'ciscoWredMIBConformance':ciscoWredMIBConformance,'ciscoWredMIBCompliances':ciscoWredMIBCompliances,'ciscoWredMIBCompliance':ciscoWredMIBCompliance,'ciscoWredMIBGroups':ciscoWredMIBGroups,_T:ciscoWredMIBGroup})