_K='etsysDot3adAggGlobalSinglePortGroup'
_J='etsysDot3adAggPortGroup'
_I='etsysDot3adAggGlobalGroup'
_H='etsysDot3adAggGlobalFormSinglePortLags'
_G='etsysDot3adAggPortEnable'
_F='etsysDot3adAggGlobalEnable'
_E='etsysDot3adAggPortEntry'
_D='read-write'
_C='EnabledStatus'
_B='ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot3adAggPortEntry,=mibBuilder.importSymbols('IEEE8023-LAG-MIB','dot3adAggPortEntry')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysIeee8023LagMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,35))
if mibBuilder.loadTexts:etsysIeee8023LagMibExtMIB.setRevisions(('2004-09-03 15:14','2003-01-31 23:16'))
_EtsysIeee8023LagMibExt_ObjectIdentity=ObjectIdentity
etsysIeee8023LagMibExt=_EtsysIeee8023LagMibExt_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,1))
_EtsysDot3adAggGlobal_ObjectIdentity=ObjectIdentity
etsysDot3adAggGlobal=_EtsysDot3adAggGlobal_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,1,1))
class _EtsysDot3adAggGlobalEnable_Type(EnabledStatus):defaultValue=1
_EtsysDot3adAggGlobalEnable_Type.__name__=_C
_EtsysDot3adAggGlobalEnable_Object=MibScalar
etsysDot3adAggGlobalEnable=_EtsysDot3adAggGlobalEnable_Object((1,3,6,1,4,1,5624,1,2,35,1,1,1),_EtsysDot3adAggGlobalEnable_Type())
etsysDot3adAggGlobalEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDot3adAggGlobalEnable.setStatus(_A)
class _EtsysDot3adAggGlobalFormSinglePortLags_Type(EnabledStatus):defaultValue=2
_EtsysDot3adAggGlobalFormSinglePortLags_Type.__name__=_C
_EtsysDot3adAggGlobalFormSinglePortLags_Object=MibScalar
etsysDot3adAggGlobalFormSinglePortLags=_EtsysDot3adAggGlobalFormSinglePortLags_Object((1,3,6,1,4,1,5624,1,2,35,1,1,2),_EtsysDot3adAggGlobalFormSinglePortLags_Type())
etsysDot3adAggGlobalFormSinglePortLags.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDot3adAggGlobalFormSinglePortLags.setStatus(_A)
_EtsysDot3adAggPort_ObjectIdentity=ObjectIdentity
etsysDot3adAggPort=_EtsysDot3adAggPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,1,2))
_EtsysDot3adAggPortTable_Object=MibTable
etsysDot3adAggPortTable=_EtsysDot3adAggPortTable_Object((1,3,6,1,4,1,5624,1,2,35,1,2,1))
if mibBuilder.loadTexts:etsysDot3adAggPortTable.setStatus(_A)
_EtsysDot3adAggPortEntry_Object=MibTableRow
etsysDot3adAggPortEntry=_EtsysDot3adAggPortEntry_Object((1,3,6,1,4,1,5624,1,2,35,1,2,1,1))
if mibBuilder.loadTexts:etsysDot3adAggPortEntry.setStatus(_A)
class _EtsysDot3adAggPortEnable_Type(EnabledStatus):defaultValue=1
_EtsysDot3adAggPortEnable_Type.__name__=_C
_EtsysDot3adAggPortEnable_Object=MibTableColumn
etsysDot3adAggPortEnable=_EtsysDot3adAggPortEnable_Object((1,3,6,1,4,1,5624,1,2,35,1,2,1,1,1),_EtsysDot3adAggPortEnable_Type())
etsysDot3adAggPortEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysDot3adAggPortEnable.setStatus(_A)
_EtsysIeee8023LagConformance_ObjectIdentity=ObjectIdentity
etsysIeee8023LagConformance=_EtsysIeee8023LagConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,2))
_EtsysIeee8023LagGroups_ObjectIdentity=ObjectIdentity
etsysIeee8023LagGroups=_EtsysIeee8023LagGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,2,1))
_EtsysIeee8023LagCompliances_ObjectIdentity=ObjectIdentity
etsysIeee8023LagCompliances=_EtsysIeee8023LagCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,35,2,2))
dot3adAggPortEntry.registerAugmentions((_B,_E))
etsysDot3adAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
etsysDot3adAggGlobalGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,35,2,1,1))
etsysDot3adAggGlobalGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:etsysDot3adAggGlobalGroup.setStatus(_A)
etsysDot3adAggPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,35,2,1,2))
etsysDot3adAggPortGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:etsysDot3adAggPortGroup.setStatus(_A)
etsysDot3adAggGlobalSinglePortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,35,2,1,3))
etsysDot3adAggGlobalSinglePortGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:etsysDot3adAggGlobalSinglePortGroup.setStatus(_A)
etsysIeee8023LagCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,35,2,2,1))
etsysIeee8023LagCompliance.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:etsysIeee8023LagCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysIeee8023LagMibExtMIB':etsysIeee8023LagMibExtMIB,'etsysIeee8023LagMibExt':etsysIeee8023LagMibExt,'etsysDot3adAggGlobal':etsysDot3adAggGlobal,_F:etsysDot3adAggGlobalEnable,_H:etsysDot3adAggGlobalFormSinglePortLags,'etsysDot3adAggPort':etsysDot3adAggPort,'etsysDot3adAggPortTable':etsysDot3adAggPortTable,_E:etsysDot3adAggPortEntry,_G:etsysDot3adAggPortEnable,'etsysIeee8023LagConformance':etsysIeee8023LagConformance,'etsysIeee8023LagGroups':etsysIeee8023LagGroups,_I:etsysDot3adAggGlobalGroup,_J:etsysDot3adAggPortGroup,_K:etsysDot3adAggGlobalSinglePortGroup,'etsysIeee8023LagCompliances':etsysIeee8023LagCompliances,'etsysIeee8023LagCompliance':etsysIeee8023LagCompliance})