_F='etsysDot1dPriorityRewriteGroup'
_E='etsysDot1dPortPriorityRewrite'
_D='etsysDot1dPortPriorityEntry'
_C='EnabledStatus'
_B='ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePortEntry,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBasePortEntry')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysIetfpBridgeMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,33))
if mibBuilder.loadTexts:etsysIetfpBridgeMibExtMIB.setRevisions(('2002-12-20 22:16',))
_EtsysIetfpBridgeMibExt_ObjectIdentity=ObjectIdentity
etsysIetfpBridgeMibExt=_EtsysIetfpBridgeMibExt_ObjectIdentity((1,3,6,1,4,1,5624,1,2,33,1))
_EtsysDot1dPriority_ObjectIdentity=ObjectIdentity
etsysDot1dPriority=_EtsysDot1dPriority_ObjectIdentity((1,3,6,1,4,1,5624,1,2,33,1,1))
_EtsysDot1dPortPriorityTable_Object=MibTable
etsysDot1dPortPriorityTable=_EtsysDot1dPortPriorityTable_Object((1,3,6,1,4,1,5624,1,2,33,1,1,1))
if mibBuilder.loadTexts:etsysDot1dPortPriorityTable.setStatus(_A)
_EtsysDot1dPortPriorityEntry_Object=MibTableRow
etsysDot1dPortPriorityEntry=_EtsysDot1dPortPriorityEntry_Object((1,3,6,1,4,1,5624,1,2,33,1,1,1,1))
if mibBuilder.loadTexts:etsysDot1dPortPriorityEntry.setStatus(_A)
class _EtsysDot1dPortPriorityRewrite_Type(EnabledStatus):defaultValue=2
_EtsysDot1dPortPriorityRewrite_Type.__name__=_C
_EtsysDot1dPortPriorityRewrite_Object=MibTableColumn
etsysDot1dPortPriorityRewrite=_EtsysDot1dPortPriorityRewrite_Object((1,3,6,1,4,1,5624,1,2,33,1,1,1,1,1),_EtsysDot1dPortPriorityRewrite_Type())
etsysDot1dPortPriorityRewrite.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysDot1dPortPriorityRewrite.setStatus(_A)
_EtsysIetfpBridgeConformance_ObjectIdentity=ObjectIdentity
etsysIetfpBridgeConformance=_EtsysIetfpBridgeConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,33,2))
_EtsysIetfpBridgeGroups_ObjectIdentity=ObjectIdentity
etsysIetfpBridgeGroups=_EtsysIetfpBridgeGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,33,2,1))
_EtsysIetfpBridgeCompliances_ObjectIdentity=ObjectIdentity
etsysIetfpBridgeCompliances=_EtsysIetfpBridgeCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,33,2,2))
dot1dBasePortEntry.registerAugmentions((_B,_D))
etsysDot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
etsysDot1dPriorityRewriteGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,33,2,1,1))
etsysDot1dPriorityRewriteGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:etsysDot1dPriorityRewriteGroup.setStatus(_A)
etsysIetfpBridgeCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,33,2,2,1))
etsysIetfpBridgeCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:etsysIetfpBridgeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysIetfpBridgeMibExtMIB':etsysIetfpBridgeMibExtMIB,'etsysIetfpBridgeMibExt':etsysIetfpBridgeMibExt,'etsysDot1dPriority':etsysDot1dPriority,'etsysDot1dPortPriorityTable':etsysDot1dPortPriorityTable,_D:etsysDot1dPortPriorityEntry,_E:etsysDot1dPortPriorityRewrite,'etsysIetfpBridgeConformance':etsysIetfpBridgeConformance,'etsysIetfpBridgeGroups':etsysIetfpBridgeGroups,_F:etsysDot1dPriorityRewriteGroup,'etsysIetfpBridgeCompliances':etsysIetfpBridgeCompliances,'etsysIetfpBridgeCompliance':etsysIetfpBridgeCompliance})