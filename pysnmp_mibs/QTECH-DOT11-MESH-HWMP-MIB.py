_T='qtechDot11MeshHWMPGroup'
_S='dot11MeshHWMPconfirmationInterval'
_R='dot11MeshHWMPmaintenanceInterval'
_Q='dot11MeshHWMPtargetOnly'
_P='dot11MeshHWMPrannInterval'
_O='dot11MeshHWMProotInterval'
_N='dot11MeshHWMProotMode'
_M='dot11MeshHWMPactivePathTimeout'
_L='dot11MeshHWMPactivePathToRootTimeout'
_K='dot11MeshHWMPperrMinInterval'
_J='dot11MeshHWMPpreqMinInterval'
_I='dot11MeshHWMPnetDiameterTraversalTime'
_H='dot11MeshHWMPnetDiameter'
_G='dot11MeshHWMPmaxPREQretries'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='QTECH-DOT11-MESH-HWMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechDot11MeshHWMPMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,92))
if mibBuilder.loadTexts:qtechDot11MeshHWMPMIB.setRevisions(('2010-02-28 00:00',))
_Apdot11MeshHWMPConfigObjects_ObjectIdentity=ObjectIdentity
apdot11MeshHWMPConfigObjects=_Apdot11MeshHWMPConfigObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,92,1))
_Dot11MeshHWMPConfigTable_Object=MibTable
dot11MeshHWMPConfigTable=_Dot11MeshHWMPConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1))
if mibBuilder.loadTexts:dot11MeshHWMPConfigTable.setStatus(_A)
_Dot11MeshHWMPConfigEntry_Object=MibTableRow
dot11MeshHWMPConfigEntry=_Dot11MeshHWMPConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1))
dot11MeshHWMPConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot11MeshHWMPConfigEntry.setStatus(_A)
class _Dot11MeshHWMPmaxPREQretries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Dot11MeshHWMPmaxPREQretries_Type.__name__=_C
_Dot11MeshHWMPmaxPREQretries_Object=MibTableColumn
dot11MeshHWMPmaxPREQretries=_Dot11MeshHWMPmaxPREQretries_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,1),_Dot11MeshHWMPmaxPREQretries_Type())
dot11MeshHWMPmaxPREQretries.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPmaxPREQretries.setStatus(_A)
class _Dot11MeshHWMPnetDiameter_Type(Integer32):defaultValue=31;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11MeshHWMPnetDiameter_Type.__name__=_C
_Dot11MeshHWMPnetDiameter_Object=MibTableColumn
dot11MeshHWMPnetDiameter=_Dot11MeshHWMPnetDiameter_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,2),_Dot11MeshHWMPnetDiameter_Type())
dot11MeshHWMPnetDiameter.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPnetDiameter.setStatus(_A)
class _Dot11MeshHWMPnetDiameterTraversalTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPnetDiameterTraversalTime_Type.__name__=_C
_Dot11MeshHWMPnetDiameterTraversalTime_Object=MibTableColumn
dot11MeshHWMPnetDiameterTraversalTime=_Dot11MeshHWMPnetDiameterTraversalTime_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,3),_Dot11MeshHWMPnetDiameterTraversalTime_Type())
dot11MeshHWMPnetDiameterTraversalTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPnetDiameterTraversalTime.setStatus(_A)
class _Dot11MeshHWMPpreqMinInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPpreqMinInterval_Type.__name__=_C
_Dot11MeshHWMPpreqMinInterval_Object=MibTableColumn
dot11MeshHWMPpreqMinInterval=_Dot11MeshHWMPpreqMinInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,4),_Dot11MeshHWMPpreqMinInterval_Type())
dot11MeshHWMPpreqMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPpreqMinInterval.setStatus(_A)
class _Dot11MeshHWMPperrMinInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPperrMinInterval_Type.__name__=_C
_Dot11MeshHWMPperrMinInterval_Object=MibTableColumn
dot11MeshHWMPperrMinInterval=_Dot11MeshHWMPperrMinInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,5),_Dot11MeshHWMPperrMinInterval_Type())
dot11MeshHWMPperrMinInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPperrMinInterval.setStatus(_A)
class _Dot11MeshHWMPactivePathToRootTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPactivePathToRootTimeout_Type.__name__=_C
_Dot11MeshHWMPactivePathToRootTimeout_Object=MibTableColumn
dot11MeshHWMPactivePathToRootTimeout=_Dot11MeshHWMPactivePathToRootTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,6),_Dot11MeshHWMPactivePathToRootTimeout_Type())
dot11MeshHWMPactivePathToRootTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPactivePathToRootTimeout.setStatus(_A)
class _Dot11MeshHWMPactivePathTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPactivePathTimeout_Type.__name__=_C
_Dot11MeshHWMPactivePathTimeout_Object=MibTableColumn
dot11MeshHWMPactivePathTimeout=_Dot11MeshHWMPactivePathTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,7),_Dot11MeshHWMPactivePathTimeout_Type())
dot11MeshHWMPactivePathTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPactivePathTimeout.setStatus(_A)
class _Dot11MeshHWMProotMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*(('noRoot',0),('proactivePREQnoPREP',2),('proactivePREQwithPREP',3),('rann',4)))
_Dot11MeshHWMProotMode_Type.__name__=_C
_Dot11MeshHWMProotMode_Object=MibTableColumn
dot11MeshHWMProotMode=_Dot11MeshHWMProotMode_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,8),_Dot11MeshHWMProotMode_Type())
dot11MeshHWMProotMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMProotMode.setStatus(_A)
class _Dot11MeshHWMProotInterval_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMProotInterval_Type.__name__=_C
_Dot11MeshHWMProotInterval_Object=MibTableColumn
dot11MeshHWMProotInterval=_Dot11MeshHWMProotInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,9),_Dot11MeshHWMProotInterval_Type())
dot11MeshHWMProotInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMProotInterval.setStatus(_A)
class _Dot11MeshHWMPrannInterval_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPrannInterval_Type.__name__=_C
_Dot11MeshHWMPrannInterval_Object=MibTableColumn
dot11MeshHWMPrannInterval=_Dot11MeshHWMPrannInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,10),_Dot11MeshHWMPrannInterval_Type())
dot11MeshHWMPrannInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPrannInterval.setStatus(_A)
class _Dot11MeshHWMPtargetOnly_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('intermediateMSTA',0),('targetOnly',1)))
_Dot11MeshHWMPtargetOnly_Type.__name__=_C
_Dot11MeshHWMPtargetOnly_Object=MibTableColumn
dot11MeshHWMPtargetOnly=_Dot11MeshHWMPtargetOnly_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,11),_Dot11MeshHWMPtargetOnly_Type())
dot11MeshHWMPtargetOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPtargetOnly.setStatus(_A)
class _Dot11MeshHWMPmaintenanceInterval_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPmaintenanceInterval_Type.__name__=_C
_Dot11MeshHWMPmaintenanceInterval_Object=MibTableColumn
dot11MeshHWMPmaintenanceInterval=_Dot11MeshHWMPmaintenanceInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,12),_Dot11MeshHWMPmaintenanceInterval_Type())
dot11MeshHWMPmaintenanceInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPmaintenanceInterval.setStatus(_A)
class _Dot11MeshHWMPconfirmationInterval_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MeshHWMPconfirmationInterval_Type.__name__=_C
_Dot11MeshHWMPconfirmationInterval_Object=MibTableColumn
dot11MeshHWMPconfirmationInterval=_Dot11MeshHWMPconfirmationInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,92,1,1,1,13),_Dot11MeshHWMPconfirmationInterval_Type())
dot11MeshHWMPconfirmationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MeshHWMPconfirmationInterval.setStatus(_A)
_QtechDot11MeshHWMPConformance_ObjectIdentity=ObjectIdentity
qtechDot11MeshHWMPConformance=_QtechDot11MeshHWMPConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,92,2))
_QtechDot11MeshHWMPCompliances_ObjectIdentity=ObjectIdentity
qtechDot11MeshHWMPCompliances=_QtechDot11MeshHWMPCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,92,2,1))
_QtechDot11MeshHWMPGroups_ObjectIdentity=ObjectIdentity
qtechDot11MeshHWMPGroups=_QtechDot11MeshHWMPGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,92,2,2))
qtechDot11MeshHWMPGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,92,2,2,1))
qtechDot11MeshHWMPGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qtechDot11MeshHWMPGroup.setStatus(_A)
qtechDot11MeshHWMPCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,92,2,1,1))
qtechDot11MeshHWMPCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:qtechDot11MeshHWMPCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDot11MeshHWMPMIB':qtechDot11MeshHWMPMIB,'apdot11MeshHWMPConfigObjects':apdot11MeshHWMPConfigObjects,'dot11MeshHWMPConfigTable':dot11MeshHWMPConfigTable,'dot11MeshHWMPConfigEntry':dot11MeshHWMPConfigEntry,_G:dot11MeshHWMPmaxPREQretries,_H:dot11MeshHWMPnetDiameter,_I:dot11MeshHWMPnetDiameterTraversalTime,_J:dot11MeshHWMPpreqMinInterval,_K:dot11MeshHWMPperrMinInterval,_L:dot11MeshHWMPactivePathToRootTimeout,_M:dot11MeshHWMPactivePathTimeout,_N:dot11MeshHWMProotMode,_O:dot11MeshHWMProotInterval,_P:dot11MeshHWMPrannInterval,_Q:dot11MeshHWMPtargetOnly,_R:dot11MeshHWMPmaintenanceInterval,_S:dot11MeshHWMPconfirmationInterval,'qtechDot11MeshHWMPConformance':qtechDot11MeshHWMPConformance,'qtechDot11MeshHWMPCompliances':qtechDot11MeshHWMPCompliances,'qtechDot11MeshHWMPCompliance':qtechDot11MeshHWMPCompliance,'qtechDot11MeshHWMPGroups':qtechDot11MeshHWMPGroups,_T:qtechDot11MeshHWMPGroup})