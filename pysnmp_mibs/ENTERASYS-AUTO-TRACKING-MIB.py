_V='etsysAutoTrackingPortGroup2'
_U='etsysAutoTrackingSystemGroup2'
_T='etsysAutoTrackingPortGroup'
_S='etsysAutoTrackingSystemGroup'
_R='etsysAutoTrackingPortRadiusRejectProfileIndex'
_Q='etsysAutoTrackingPortRadiusTimeoutProfileIndex'
_P='etsysAutoTrackingSystemAccountEnable'
_O='seconds'
_N='ifIndex'
_M='IF-MIB'
_L='etsysAutoTrackingPortIdleTimeout'
_K='etsysAutoTrackingPortSessionTimeout'
_J='etsysAutoTrackingPortAuthenticationsAllocated'
_I='etsysAutoTrackingPortAuthenticationsAllowed'
_H='etsysAutoTrackingPortEnable'
_G='deprecated'
_F='etsysAutoTrackingSystemEnable'
_E='EnabledStatus'
_D='Unsigned32'
_C='read-write'
_B='current'
_A='ENTERASYS-AUTO-TRACKING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_M,_N)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysAutoTrackingMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,92))
if mibBuilder.loadTexts:etsysAutoTrackingMIB.setRevisions(('2013-02-12 16:56','2013-02-11 15:57','2013-01-22 15:32'))
_EtsysAutoTrackingBody_ObjectIdentity=ObjectIdentity
etsysAutoTrackingBody=_EtsysAutoTrackingBody_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,2))
_EtsysAutoTrackingObjects_ObjectIdentity=ObjectIdentity
etsysAutoTrackingObjects=_EtsysAutoTrackingObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,2,1))
_EtsysAutoTrackingSystem_ObjectIdentity=ObjectIdentity
etsysAutoTrackingSystem=_EtsysAutoTrackingSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,2,1,1))
class _EtsysAutoTrackingSystemEnable_Type(EnabledStatus):defaultValue=2
_EtsysAutoTrackingSystemEnable_Type.__name__=_E
_EtsysAutoTrackingSystemEnable_Object=MibScalar
etsysAutoTrackingSystemEnable=_EtsysAutoTrackingSystemEnable_Object((1,3,6,1,4,1,5624,1,2,92,2,1,1,1),_EtsysAutoTrackingSystemEnable_Type())
etsysAutoTrackingSystemEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingSystemEnable.setStatus(_B)
class _EtsysAutoTrackingSystemAccountEnable_Type(EnabledStatus):defaultValue=2
_EtsysAutoTrackingSystemAccountEnable_Type.__name__=_E
_EtsysAutoTrackingSystemAccountEnable_Object=MibScalar
etsysAutoTrackingSystemAccountEnable=_EtsysAutoTrackingSystemAccountEnable_Object((1,3,6,1,4,1,5624,1,2,92,2,1,1,2),_EtsysAutoTrackingSystemAccountEnable_Type())
etsysAutoTrackingSystemAccountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingSystemAccountEnable.setStatus(_B)
_EtsysAutoTrackingPort_ObjectIdentity=ObjectIdentity
etsysAutoTrackingPort=_EtsysAutoTrackingPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,2,1,2))
_EtsysAutoTrackingPortTable_Object=MibTable
etsysAutoTrackingPortTable=_EtsysAutoTrackingPortTable_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1))
if mibBuilder.loadTexts:etsysAutoTrackingPortTable.setStatus(_B)
_EtsysAutoTrackingPortEntry_Object=MibTableRow
etsysAutoTrackingPortEntry=_EtsysAutoTrackingPortEntry_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1))
etsysAutoTrackingPortEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:etsysAutoTrackingPortEntry.setStatus(_B)
class _EtsysAutoTrackingPortEnable_Type(EnabledStatus):defaultValue=2
_EtsysAutoTrackingPortEnable_Type.__name__=_E
_EtsysAutoTrackingPortEnable_Object=MibTableColumn
etsysAutoTrackingPortEnable=_EtsysAutoTrackingPortEnable_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,1),_EtsysAutoTrackingPortEnable_Type())
etsysAutoTrackingPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortEnable.setStatus(_B)
_EtsysAutoTrackingPortAuthenticationsAllowed_Type=Unsigned32
_EtsysAutoTrackingPortAuthenticationsAllowed_Object=MibTableColumn
etsysAutoTrackingPortAuthenticationsAllowed=_EtsysAutoTrackingPortAuthenticationsAllowed_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,2),_EtsysAutoTrackingPortAuthenticationsAllowed_Type())
etsysAutoTrackingPortAuthenticationsAllowed.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysAutoTrackingPortAuthenticationsAllowed.setStatus(_B)
_EtsysAutoTrackingPortAuthenticationsAllocated_Type=Unsigned32
_EtsysAutoTrackingPortAuthenticationsAllocated_Object=MibTableColumn
etsysAutoTrackingPortAuthenticationsAllocated=_EtsysAutoTrackingPortAuthenticationsAllocated_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,3),_EtsysAutoTrackingPortAuthenticationsAllocated_Type())
etsysAutoTrackingPortAuthenticationsAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortAuthenticationsAllocated.setStatus(_B)
class _EtsysAutoTrackingPortSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysAutoTrackingPortSessionTimeout_Type.__name__=_D
_EtsysAutoTrackingPortSessionTimeout_Object=MibTableColumn
etsysAutoTrackingPortSessionTimeout=_EtsysAutoTrackingPortSessionTimeout_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,4),_EtsysAutoTrackingPortSessionTimeout_Type())
etsysAutoTrackingPortSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysAutoTrackingPortSessionTimeout.setUnits(_O)
class _EtsysAutoTrackingPortIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysAutoTrackingPortIdleTimeout_Type.__name__=_D
_EtsysAutoTrackingPortIdleTimeout_Object=MibTableColumn
etsysAutoTrackingPortIdleTimeout=_EtsysAutoTrackingPortIdleTimeout_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,5),_EtsysAutoTrackingPortIdleTimeout_Type())
etsysAutoTrackingPortIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortIdleTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysAutoTrackingPortIdleTimeout.setUnits(_O)
class _EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type.__name__=_D
_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Object=MibTableColumn
etsysAutoTrackingPortRadiusTimeoutProfileIndex=_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,6),_EtsysAutoTrackingPortRadiusTimeoutProfileIndex_Type())
etsysAutoTrackingPortRadiusTimeoutProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortRadiusTimeoutProfileIndex.setStatus(_B)
class _EtsysAutoTrackingPortRadiusRejectProfileIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysAutoTrackingPortRadiusRejectProfileIndex_Type.__name__=_D
_EtsysAutoTrackingPortRadiusRejectProfileIndex_Object=MibTableColumn
etsysAutoTrackingPortRadiusRejectProfileIndex=_EtsysAutoTrackingPortRadiusRejectProfileIndex_Object((1,3,6,1,4,1,5624,1,2,92,2,1,2,1,1,7),_EtsysAutoTrackingPortRadiusRejectProfileIndex_Type())
etsysAutoTrackingPortRadiusRejectProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAutoTrackingPortRadiusRejectProfileIndex.setStatus(_B)
_EtsysAutoTrackingConformance_ObjectIdentity=ObjectIdentity
etsysAutoTrackingConformance=_EtsysAutoTrackingConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,3))
_EtsysAutoTrackingGroups_ObjectIdentity=ObjectIdentity
etsysAutoTrackingGroups=_EtsysAutoTrackingGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,3,1))
_EtsysAutoTrackingCompliances_ObjectIdentity=ObjectIdentity
etsysAutoTrackingCompliances=_EtsysAutoTrackingCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,92,3,2))
etsysAutoTrackingSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,92,3,1,1))
etsysAutoTrackingSystemGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:etsysAutoTrackingSystemGroup.setStatus(_G)
etsysAutoTrackingPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,92,3,1,2))
etsysAutoTrackingPortGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:etsysAutoTrackingPortGroup.setStatus(_G)
etsysAutoTrackingSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,92,3,1,3))
etsysAutoTrackingSystemGroup2.setObjects(*((_A,_F),(_A,_P)))
if mibBuilder.loadTexts:etsysAutoTrackingSystemGroup2.setStatus(_B)
etsysAutoTrackingPortGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,92,3,1,4))
etsysAutoTrackingPortGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysAutoTrackingPortGroup2.setStatus(_B)
etsysAutoTrackingCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,92,3,2,1))
etsysAutoTrackingCompliance.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:etsysAutoTrackingCompliance.setStatus(_G)
etsysAutoTrackingCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,92,3,2,2))
etsysAutoTrackingCompliance2.setObjects(*((_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysAutoTrackingCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysAutoTrackingMIB':etsysAutoTrackingMIB,'etsysAutoTrackingBody':etsysAutoTrackingBody,'etsysAutoTrackingObjects':etsysAutoTrackingObjects,'etsysAutoTrackingSystem':etsysAutoTrackingSystem,_F:etsysAutoTrackingSystemEnable,_P:etsysAutoTrackingSystemAccountEnable,'etsysAutoTrackingPort':etsysAutoTrackingPort,'etsysAutoTrackingPortTable':etsysAutoTrackingPortTable,'etsysAutoTrackingPortEntry':etsysAutoTrackingPortEntry,_H:etsysAutoTrackingPortEnable,_I:etsysAutoTrackingPortAuthenticationsAllowed,_J:etsysAutoTrackingPortAuthenticationsAllocated,_K:etsysAutoTrackingPortSessionTimeout,_L:etsysAutoTrackingPortIdleTimeout,_Q:etsysAutoTrackingPortRadiusTimeoutProfileIndex,_R:etsysAutoTrackingPortRadiusRejectProfileIndex,'etsysAutoTrackingConformance':etsysAutoTrackingConformance,'etsysAutoTrackingGroups':etsysAutoTrackingGroups,_S:etsysAutoTrackingSystemGroup,_T:etsysAutoTrackingPortGroup,_U:etsysAutoTrackingSystemGroup2,_V:etsysAutoTrackingPortGroup2,'etsysAutoTrackingCompliances':etsysAutoTrackingCompliances,'etsysAutoTrackingCompliance':etsysAutoTrackingCompliance,'etsysAutoTrackingCompliance2':etsysAutoTrackingCompliance2})