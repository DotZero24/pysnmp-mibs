_S='f10IsisNotificationGroup'
_R='f10IsisSystemGroup'
_Q='f10IsisAdjChanges'
_P='f10IsisSysOloadV6WaitForBgp'
_O='f10IsisSysLevelV6OverloadState'
_N='f10IsisSysLevelOverloadState'
_M='f10IsisSysOloadV6SetOloadOnStartupUntil'
_L='f10IsisSysOloadV6SetOverload'
_K='f10IsisSysOloadWaitForBgp'
_J='f10IsisSysOloadSetOloadOnStartupUntil'
_I='f10IsisSysOloadSetOverload'
_H='read-only'
_G='f10IsisSysLevelIndex'
_F='TruthValue'
_E='Seconds'
_D='Unsigned32'
_C='read-write'
_B='F10-ISIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
f10IsisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,18))
if mibBuilder.loadTexts:f10IsisMib.setRevisions(('2011-07-01 00:00',))
class F10IsisISLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('area',1),('domain',2)))
_F10IsisNotifications_ObjectIdentity=ObjectIdentity
f10IsisNotifications=_F10IsisNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,18,0))
_F10IsisObjects_ObjectIdentity=ObjectIdentity
f10IsisObjects=_F10IsisObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,18,1))
class _F10IsisSysOloadSetOverload_Type(TruthValue):defaultValue=2
_F10IsisSysOloadSetOverload_Type.__name__=_F
_F10IsisSysOloadSetOverload_Object=MibScalar
f10IsisSysOloadSetOverload=_F10IsisSysOloadSetOverload_Object((1,3,6,1,4,1,6027,3,18,1,1),_F10IsisSysOloadSetOverload_Type())
f10IsisSysOloadSetOverload.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadSetOverload.setStatus(_A)
class _F10IsisSysOloadSetOloadOnStartupUntil_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_F10IsisSysOloadSetOloadOnStartupUntil_Type.__name__=_D
_F10IsisSysOloadSetOloadOnStartupUntil_Object=MibScalar
f10IsisSysOloadSetOloadOnStartupUntil=_F10IsisSysOloadSetOloadOnStartupUntil_Object((1,3,6,1,4,1,6027,3,18,1,2),_F10IsisSysOloadSetOloadOnStartupUntil_Type())
f10IsisSysOloadSetOloadOnStartupUntil.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadSetOloadOnStartupUntil.setStatus(_A)
if mibBuilder.loadTexts:f10IsisSysOloadSetOloadOnStartupUntil.setUnits(_E)
class _F10IsisSysOloadWaitForBgp_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_F10IsisSysOloadWaitForBgp_Type.__name__=_D
_F10IsisSysOloadWaitForBgp_Object=MibScalar
f10IsisSysOloadWaitForBgp=_F10IsisSysOloadWaitForBgp_Object((1,3,6,1,4,1,6027,3,18,1,3),_F10IsisSysOloadWaitForBgp_Type())
f10IsisSysOloadWaitForBgp.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadWaitForBgp.setStatus(_A)
if mibBuilder.loadTexts:f10IsisSysOloadWaitForBgp.setUnits(_E)
class _F10IsisSysOloadV6SetOverload_Type(TruthValue):defaultValue=2
_F10IsisSysOloadV6SetOverload_Type.__name__=_F
_F10IsisSysOloadV6SetOverload_Object=MibScalar
f10IsisSysOloadV6SetOverload=_F10IsisSysOloadV6SetOverload_Object((1,3,6,1,4,1,6027,3,18,1,4),_F10IsisSysOloadV6SetOverload_Type())
f10IsisSysOloadV6SetOverload.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadV6SetOverload.setStatus(_A)
class _F10IsisSysOloadV6SetOloadOnStartupUntil_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_F10IsisSysOloadV6SetOloadOnStartupUntil_Type.__name__=_D
_F10IsisSysOloadV6SetOloadOnStartupUntil_Object=MibScalar
f10IsisSysOloadV6SetOloadOnStartupUntil=_F10IsisSysOloadV6SetOloadOnStartupUntil_Object((1,3,6,1,4,1,6027,3,18,1,5),_F10IsisSysOloadV6SetOloadOnStartupUntil_Type())
f10IsisSysOloadV6SetOloadOnStartupUntil.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadV6SetOloadOnStartupUntil.setStatus(_A)
if mibBuilder.loadTexts:f10IsisSysOloadV6SetOloadOnStartupUntil.setUnits(_E)
class _F10IsisSysOloadV6WaitForBgp_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_F10IsisSysOloadV6WaitForBgp_Type.__name__=_D
_F10IsisSysOloadV6WaitForBgp_Object=MibScalar
f10IsisSysOloadV6WaitForBgp=_F10IsisSysOloadV6WaitForBgp_Object((1,3,6,1,4,1,6027,3,18,1,6),_F10IsisSysOloadV6WaitForBgp_Type())
f10IsisSysOloadV6WaitForBgp.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IsisSysOloadV6WaitForBgp.setStatus(_A)
if mibBuilder.loadTexts:f10IsisSysOloadV6WaitForBgp.setUnits(_E)
_F10IsisSysLevelTable_Object=MibTable
f10IsisSysLevelTable=_F10IsisSysLevelTable_Object((1,3,6,1,4,1,6027,3,18,1,7))
if mibBuilder.loadTexts:f10IsisSysLevelTable.setStatus(_A)
_F10IsisSysLevelEntry_Object=MibTableRow
f10IsisSysLevelEntry=_F10IsisSysLevelEntry_Object((1,3,6,1,4,1,6027,3,18,1,7,1))
f10IsisSysLevelEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:f10IsisSysLevelEntry.setStatus(_A)
_F10IsisSysLevelIndex_Type=F10IsisISLevel
_F10IsisSysLevelIndex_Object=MibTableColumn
f10IsisSysLevelIndex=_F10IsisSysLevelIndex_Object((1,3,6,1,4,1,6027,3,18,1,7,1,1),_F10IsisSysLevelIndex_Type())
f10IsisSysLevelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:f10IsisSysLevelIndex.setStatus(_A)
_F10IsisSysLevelOverloadState_Type=TruthValue
_F10IsisSysLevelOverloadState_Object=MibTableColumn
f10IsisSysLevelOverloadState=_F10IsisSysLevelOverloadState_Object((1,3,6,1,4,1,6027,3,18,1,7,1,2),_F10IsisSysLevelOverloadState_Type())
f10IsisSysLevelOverloadState.setMaxAccess(_H)
if mibBuilder.loadTexts:f10IsisSysLevelOverloadState.setStatus(_A)
_F10IsisSysLevelV6OverloadState_Type=TruthValue
_F10IsisSysLevelV6OverloadState_Object=MibTableColumn
f10IsisSysLevelV6OverloadState=_F10IsisSysLevelV6OverloadState_Object((1,3,6,1,4,1,6027,3,18,1,7,1,3),_F10IsisSysLevelV6OverloadState_Type())
f10IsisSysLevelV6OverloadState.setMaxAccess(_H)
if mibBuilder.loadTexts:f10IsisSysLevelV6OverloadState.setStatus(_A)
_F10IsisConformance_ObjectIdentity=ObjectIdentity
f10IsisConformance=_F10IsisConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2))
_F10IsisGroups_ObjectIdentity=ObjectIdentity
f10IsisGroups=_F10IsisGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2,1))
_F10IsisCompliances_ObjectIdentity=ObjectIdentity
f10IsisCompliances=_F10IsisCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2,2))
f10IsisSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,18,2,1,1))
f10IsisSystemGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:f10IsisSystemGroup.setStatus(_A)
f10IsisAdjChanges=NotificationType((1,3,6,1,4,1,6027,3,18,0,1))
if mibBuilder.loadTexts:f10IsisAdjChanges.setStatus(_A)
f10IsisNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,18,2,1,2))
f10IsisNotificationGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:f10IsisNotificationGroup.setStatus(_A)
f10IsisCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,18,2,2,1))
f10IsisCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:f10IsisCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'F10IsisISLevel':F10IsisISLevel,'f10IsisMib':f10IsisMib,'f10IsisNotifications':f10IsisNotifications,_Q:f10IsisAdjChanges,'f10IsisObjects':f10IsisObjects,_I:f10IsisSysOloadSetOverload,_J:f10IsisSysOloadSetOloadOnStartupUntil,_K:f10IsisSysOloadWaitForBgp,_L:f10IsisSysOloadV6SetOverload,_M:f10IsisSysOloadV6SetOloadOnStartupUntil,_P:f10IsisSysOloadV6WaitForBgp,'f10IsisSysLevelTable':f10IsisSysLevelTable,'f10IsisSysLevelEntry':f10IsisSysLevelEntry,_G:f10IsisSysLevelIndex,_N:f10IsisSysLevelOverloadState,_O:f10IsisSysLevelV6OverloadState,'f10IsisConformance':f10IsisConformance,'f10IsisGroups':f10IsisGroups,_R:f10IsisSystemGroup,_S:f10IsisNotificationGroup,'f10IsisCompliances':f10IsisCompliances,'f10IsisCompliance':f10IsisCompliance})