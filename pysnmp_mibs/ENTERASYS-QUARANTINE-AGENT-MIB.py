_S='etsysQuarantineAgentSystemGroup2'
_R='etsysQuarantineAgentSystemGroup'
_Q='etsysQuarantineAgentSystemAccountEnable'
_P='etsysQuarantineAgentPortIdleTimeout'
_O='etsysQuarantineAgentPortSessionTimeout'
_N='etsysQuarantineAgentPortAuthenticationsAllocated'
_M='etsysQuarantineAgentPortAuthenticationsAllowed'
_L='etsysQuarantineAgentPortEnable'
_K='deprecated'
_J='seconds'
_I='ifIndex'
_H='IF-MIB'
_G='etsysQuarantineAgentPortGroup'
_F='etsysQuarantineAgentSystemEnable'
_E='Unsigned32'
_D='EnabledStatus'
_C='read-write'
_B='current'
_A='ENTERASYS-QUARANTINE-AGENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_H,_I)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysQuarantineAgentMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,93))
if mibBuilder.loadTexts:etsysQuarantineAgentMIB.setRevisions(('2013-02-11 18:57','2013-02-11 15:57','2013-01-22 15:32'))
_EtsysQuarantineAgentBody_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentBody=_EtsysQuarantineAgentBody_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,2))
_EtsysQuarantineAgentObjects_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentObjects=_EtsysQuarantineAgentObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,2,1))
_EtsysQuarantineAgentSystem_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentSystem=_EtsysQuarantineAgentSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,2,1,1))
class _EtsysQuarantineAgentSystemEnable_Type(EnabledStatus):defaultValue=2
_EtsysQuarantineAgentSystemEnable_Type.__name__=_D
_EtsysQuarantineAgentSystemEnable_Object=MibScalar
etsysQuarantineAgentSystemEnable=_EtsysQuarantineAgentSystemEnable_Object((1,3,6,1,4,1,5624,1,2,93,2,1,1,1),_EtsysQuarantineAgentSystemEnable_Type())
etsysQuarantineAgentSystemEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentSystemEnable.setStatus(_B)
class _EtsysQuarantineAgentSystemAccountEnable_Type(EnabledStatus):defaultValue=2
_EtsysQuarantineAgentSystemAccountEnable_Type.__name__=_D
_EtsysQuarantineAgentSystemAccountEnable_Object=MibScalar
etsysQuarantineAgentSystemAccountEnable=_EtsysQuarantineAgentSystemAccountEnable_Object((1,3,6,1,4,1,5624,1,2,93,2,1,1,2),_EtsysQuarantineAgentSystemAccountEnable_Type())
etsysQuarantineAgentSystemAccountEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentSystemAccountEnable.setStatus(_B)
_EtsysQuarantineAgentPort_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentPort=_EtsysQuarantineAgentPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,2,1,2))
_EtsysQuarantineAgentPortTable_Object=MibTable
etsysQuarantineAgentPortTable=_EtsysQuarantineAgentPortTable_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1))
if mibBuilder.loadTexts:etsysQuarantineAgentPortTable.setStatus(_B)
_EtsysQuarantineAgentPortEntry_Object=MibTableRow
etsysQuarantineAgentPortEntry=_EtsysQuarantineAgentPortEntry_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1))
etsysQuarantineAgentPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:etsysQuarantineAgentPortEntry.setStatus(_B)
class _EtsysQuarantineAgentPortEnable_Type(EnabledStatus):defaultValue=2
_EtsysQuarantineAgentPortEnable_Type.__name__=_D
_EtsysQuarantineAgentPortEnable_Object=MibTableColumn
etsysQuarantineAgentPortEnable=_EtsysQuarantineAgentPortEnable_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1,2),_EtsysQuarantineAgentPortEnable_Type())
etsysQuarantineAgentPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentPortEnable.setStatus(_B)
_EtsysQuarantineAgentPortAuthenticationsAllowed_Type=Unsigned32
_EtsysQuarantineAgentPortAuthenticationsAllowed_Object=MibTableColumn
etsysQuarantineAgentPortAuthenticationsAllowed=_EtsysQuarantineAgentPortAuthenticationsAllowed_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1,3),_EtsysQuarantineAgentPortAuthenticationsAllowed_Type())
etsysQuarantineAgentPortAuthenticationsAllowed.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysQuarantineAgentPortAuthenticationsAllowed.setStatus(_B)
_EtsysQuarantineAgentPortAuthenticationsAllocated_Type=Unsigned32
_EtsysQuarantineAgentPortAuthenticationsAllocated_Object=MibTableColumn
etsysQuarantineAgentPortAuthenticationsAllocated=_EtsysQuarantineAgentPortAuthenticationsAllocated_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1,4),_EtsysQuarantineAgentPortAuthenticationsAllocated_Type())
etsysQuarantineAgentPortAuthenticationsAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentPortAuthenticationsAllocated.setStatus(_B)
class _EtsysQuarantineAgentPortSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysQuarantineAgentPortSessionTimeout_Type.__name__=_E
_EtsysQuarantineAgentPortSessionTimeout_Object=MibTableColumn
etsysQuarantineAgentPortSessionTimeout=_EtsysQuarantineAgentPortSessionTimeout_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1,5),_EtsysQuarantineAgentPortSessionTimeout_Type())
etsysQuarantineAgentPortSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentPortSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysQuarantineAgentPortSessionTimeout.setUnits(_J)
class _EtsysQuarantineAgentPortIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysQuarantineAgentPortIdleTimeout_Type.__name__=_E
_EtsysQuarantineAgentPortIdleTimeout_Object=MibTableColumn
etsysQuarantineAgentPortIdleTimeout=_EtsysQuarantineAgentPortIdleTimeout_Object((1,3,6,1,4,1,5624,1,2,93,2,1,2,1,1,6),_EtsysQuarantineAgentPortIdleTimeout_Type())
etsysQuarantineAgentPortIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysQuarantineAgentPortIdleTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysQuarantineAgentPortIdleTimeout.setUnits(_J)
_EtsysQuarantineAgentConformance_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentConformance=_EtsysQuarantineAgentConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,3))
_EtsysQuarantineAgentGroups_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentGroups=_EtsysQuarantineAgentGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,3,1))
_EtsysQuarantineAgentCompliances_ObjectIdentity=ObjectIdentity
etsysQuarantineAgentCompliances=_EtsysQuarantineAgentCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,93,3,2))
etsysQuarantineAgentSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,93,3,1,1))
etsysQuarantineAgentSystemGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:etsysQuarantineAgentSystemGroup.setStatus(_K)
etsysQuarantineAgentPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,93,3,1,2))
etsysQuarantineAgentPortGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:etsysQuarantineAgentPortGroup.setStatus(_B)
etsysQuarantineAgentSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,93,3,1,3))
etsysQuarantineAgentSystemGroup2.setObjects(*((_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:etsysQuarantineAgentSystemGroup2.setStatus(_B)
etsysQuarantineAgentCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,93,3,2,1))
etsysQuarantineAgentCompliance.setObjects(*((_A,_R),(_A,_G)))
if mibBuilder.loadTexts:etsysQuarantineAgentCompliance.setStatus(_K)
etsysQuarantineAgentCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,93,3,2,2))
etsysQuarantineAgentCompliance2.setObjects(*((_A,_S),(_A,_G)))
if mibBuilder.loadTexts:etsysQuarantineAgentCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysQuarantineAgentMIB':etsysQuarantineAgentMIB,'etsysQuarantineAgentBody':etsysQuarantineAgentBody,'etsysQuarantineAgentObjects':etsysQuarantineAgentObjects,'etsysQuarantineAgentSystem':etsysQuarantineAgentSystem,_F:etsysQuarantineAgentSystemEnable,_Q:etsysQuarantineAgentSystemAccountEnable,'etsysQuarantineAgentPort':etsysQuarantineAgentPort,'etsysQuarantineAgentPortTable':etsysQuarantineAgentPortTable,'etsysQuarantineAgentPortEntry':etsysQuarantineAgentPortEntry,_L:etsysQuarantineAgentPortEnable,_M:etsysQuarantineAgentPortAuthenticationsAllowed,_N:etsysQuarantineAgentPortAuthenticationsAllocated,_O:etsysQuarantineAgentPortSessionTimeout,_P:etsysQuarantineAgentPortIdleTimeout,'etsysQuarantineAgentConformance':etsysQuarantineAgentConformance,'etsysQuarantineAgentGroups':etsysQuarantineAgentGroups,_R:etsysQuarantineAgentSystemGroup,_G:etsysQuarantineAgentPortGroup,_S:etsysQuarantineAgentSystemGroup2,'etsysQuarantineAgentCompliances':etsysQuarantineAgentCompliances,'etsysQuarantineAgentCompliance':etsysQuarantineAgentCompliance,'etsysQuarantineAgentCompliance2':etsysQuarantineAgentCompliance2})