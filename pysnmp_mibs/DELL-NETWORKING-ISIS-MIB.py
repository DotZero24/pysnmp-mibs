_S='dellNetIsisNotificationGroup'
_R='dellNetIsisSystemGroup'
_Q='dellNetIsisAdjChanges'
_P='dellNetIsisSysOloadV6WaitForBgp'
_O='dellNetIsisSysLevelV6OverloadState'
_N='dellNetIsisSysLevelOverloadState'
_M='dellNetIsisSysOloadV6SetOloadOnStartupUntil'
_L='dellNetIsisSysOloadV6SetOverload'
_K='dellNetIsisSysOloadWaitForBgp'
_J='dellNetIsisSysOloadSetOloadOnStartupUntil'
_I='dellNetIsisSysOloadSetOverload'
_H='read-only'
_G='dellNetIsisSysLevelIndex'
_F='TruthValue'
_E='Seconds'
_D='Unsigned32'
_C='read-write'
_B='DELL-NETWORKING-ISIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
dellNetIsisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,18))
if mibBuilder.loadTexts:dellNetIsisMib.setRevisions(('2011-07-01 00:00',))
class DellNetIsisISLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('area',1),('domain',2)))
_DellNetIsisNotifications_ObjectIdentity=ObjectIdentity
dellNetIsisNotifications=_DellNetIsisNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,18,0))
_DellNetIsisObjects_ObjectIdentity=ObjectIdentity
dellNetIsisObjects=_DellNetIsisObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,18,1))
class _DellNetIsisSysOloadSetOverload_Type(TruthValue):defaultValue=2
_DellNetIsisSysOloadSetOverload_Type.__name__=_F
_DellNetIsisSysOloadSetOverload_Object=MibScalar
dellNetIsisSysOloadSetOverload=_DellNetIsisSysOloadSetOverload_Object((1,3,6,1,4,1,6027,3,18,1,1),_DellNetIsisSysOloadSetOverload_Type())
dellNetIsisSysOloadSetOverload.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadSetOverload.setStatus(_A)
class _DellNetIsisSysOloadSetOloadOnStartupUntil_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_DellNetIsisSysOloadSetOloadOnStartupUntil_Type.__name__=_D
_DellNetIsisSysOloadSetOloadOnStartupUntil_Object=MibScalar
dellNetIsisSysOloadSetOloadOnStartupUntil=_DellNetIsisSysOloadSetOloadOnStartupUntil_Object((1,3,6,1,4,1,6027,3,18,1,2),_DellNetIsisSysOloadSetOloadOnStartupUntil_Type())
dellNetIsisSysOloadSetOloadOnStartupUntil.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadSetOloadOnStartupUntil.setStatus(_A)
if mibBuilder.loadTexts:dellNetIsisSysOloadSetOloadOnStartupUntil.setUnits(_E)
class _DellNetIsisSysOloadWaitForBgp_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_DellNetIsisSysOloadWaitForBgp_Type.__name__=_D
_DellNetIsisSysOloadWaitForBgp_Object=MibScalar
dellNetIsisSysOloadWaitForBgp=_DellNetIsisSysOloadWaitForBgp_Object((1,3,6,1,4,1,6027,3,18,1,3),_DellNetIsisSysOloadWaitForBgp_Type())
dellNetIsisSysOloadWaitForBgp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadWaitForBgp.setStatus(_A)
if mibBuilder.loadTexts:dellNetIsisSysOloadWaitForBgp.setUnits(_E)
class _DellNetIsisSysOloadV6SetOverload_Type(TruthValue):defaultValue=2
_DellNetIsisSysOloadV6SetOverload_Type.__name__=_F
_DellNetIsisSysOloadV6SetOverload_Object=MibScalar
dellNetIsisSysOloadV6SetOverload=_DellNetIsisSysOloadV6SetOverload_Object((1,3,6,1,4,1,6027,3,18,1,4),_DellNetIsisSysOloadV6SetOverload_Type())
dellNetIsisSysOloadV6SetOverload.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadV6SetOverload.setStatus(_A)
class _DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type.__name__=_D
_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Object=MibScalar
dellNetIsisSysOloadV6SetOloadOnStartupUntil=_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Object((1,3,6,1,4,1,6027,3,18,1,5),_DellNetIsisSysOloadV6SetOloadOnStartupUntil_Type())
dellNetIsisSysOloadV6SetOloadOnStartupUntil.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadV6SetOloadOnStartupUntil.setStatus(_A)
if mibBuilder.loadTexts:dellNetIsisSysOloadV6SetOloadOnStartupUntil.setUnits(_E)
class _DellNetIsisSysOloadV6WaitForBgp_Type(Unsigned32):defaultValue=600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,86400))
_DellNetIsisSysOloadV6WaitForBgp_Type.__name__=_D
_DellNetIsisSysOloadV6WaitForBgp_Object=MibScalar
dellNetIsisSysOloadV6WaitForBgp=_DellNetIsisSysOloadV6WaitForBgp_Object((1,3,6,1,4,1,6027,3,18,1,6),_DellNetIsisSysOloadV6WaitForBgp_Type())
dellNetIsisSysOloadV6WaitForBgp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIsisSysOloadV6WaitForBgp.setStatus(_A)
if mibBuilder.loadTexts:dellNetIsisSysOloadV6WaitForBgp.setUnits(_E)
_DellNetIsisSysLevelTable_Object=MibTable
dellNetIsisSysLevelTable=_DellNetIsisSysLevelTable_Object((1,3,6,1,4,1,6027,3,18,1,7))
if mibBuilder.loadTexts:dellNetIsisSysLevelTable.setStatus(_A)
_DellNetIsisSysLevelEntry_Object=MibTableRow
dellNetIsisSysLevelEntry=_DellNetIsisSysLevelEntry_Object((1,3,6,1,4,1,6027,3,18,1,7,1))
dellNetIsisSysLevelEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dellNetIsisSysLevelEntry.setStatus(_A)
_DellNetIsisSysLevelIndex_Type=DellNetIsisISLevel
_DellNetIsisSysLevelIndex_Object=MibTableColumn
dellNetIsisSysLevelIndex=_DellNetIsisSysLevelIndex_Object((1,3,6,1,4,1,6027,3,18,1,7,1,1),_DellNetIsisSysLevelIndex_Type())
dellNetIsisSysLevelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dellNetIsisSysLevelIndex.setStatus(_A)
_DellNetIsisSysLevelOverloadState_Type=TruthValue
_DellNetIsisSysLevelOverloadState_Object=MibTableColumn
dellNetIsisSysLevelOverloadState=_DellNetIsisSysLevelOverloadState_Object((1,3,6,1,4,1,6027,3,18,1,7,1,2),_DellNetIsisSysLevelOverloadState_Type())
dellNetIsisSysLevelOverloadState.setMaxAccess(_H)
if mibBuilder.loadTexts:dellNetIsisSysLevelOverloadState.setStatus(_A)
_DellNetIsisSysLevelV6OverloadState_Type=TruthValue
_DellNetIsisSysLevelV6OverloadState_Object=MibTableColumn
dellNetIsisSysLevelV6OverloadState=_DellNetIsisSysLevelV6OverloadState_Object((1,3,6,1,4,1,6027,3,18,1,7,1,3),_DellNetIsisSysLevelV6OverloadState_Type())
dellNetIsisSysLevelV6OverloadState.setMaxAccess(_H)
if mibBuilder.loadTexts:dellNetIsisSysLevelV6OverloadState.setStatus(_A)
_DellNetIsisConformance_ObjectIdentity=ObjectIdentity
dellNetIsisConformance=_DellNetIsisConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2))
_DellNetIsisGroups_ObjectIdentity=ObjectIdentity
dellNetIsisGroups=_DellNetIsisGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2,1))
_DellNetIsisCompliances_ObjectIdentity=ObjectIdentity
dellNetIsisCompliances=_DellNetIsisCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,18,2,2))
dellNetIsisSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,18,2,1,1))
dellNetIsisSystemGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dellNetIsisSystemGroup.setStatus(_A)
dellNetIsisAdjChanges=NotificationType((1,3,6,1,4,1,6027,3,18,0,1))
if mibBuilder.loadTexts:dellNetIsisAdjChanges.setStatus(_A)
dellNetIsisNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,18,2,1,2))
dellNetIsisNotificationGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:dellNetIsisNotificationGroup.setStatus(_A)
dellNetIsisCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,18,2,2,1))
dellNetIsisCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:dellNetIsisCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DellNetIsisISLevel':DellNetIsisISLevel,'dellNetIsisMib':dellNetIsisMib,'dellNetIsisNotifications':dellNetIsisNotifications,_Q:dellNetIsisAdjChanges,'dellNetIsisObjects':dellNetIsisObjects,_I:dellNetIsisSysOloadSetOverload,_J:dellNetIsisSysOloadSetOloadOnStartupUntil,_K:dellNetIsisSysOloadWaitForBgp,_L:dellNetIsisSysOloadV6SetOverload,_M:dellNetIsisSysOloadV6SetOloadOnStartupUntil,_P:dellNetIsisSysOloadV6WaitForBgp,'dellNetIsisSysLevelTable':dellNetIsisSysLevelTable,'dellNetIsisSysLevelEntry':dellNetIsisSysLevelEntry,_G:dellNetIsisSysLevelIndex,_N:dellNetIsisSysLevelOverloadState,_O:dellNetIsisSysLevelV6OverloadState,'dellNetIsisConformance':dellNetIsisConformance,'dellNetIsisGroups':dellNetIsisGroups,_R:dellNetIsisSystemGroup,_S:dellNetIsisNotificationGroup,'dellNetIsisCompliances':dellNetIsisCompliances,'dellNetIsisCompliance':dellNetIsisCompliance})