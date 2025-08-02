_N='etsysIeee8021BridgeMibExtMrpGroup'
_M='etsysIeee8021BridgeMibExtBasePortGroup'
_L='etsysIeee8021BridgeMibExtBaseModeGroup'
_K='etsysIeee8021BridgeMibExtMrpPeriodicEnabled'
_J='etsys8021BridgePortComponentId'
_I='etsysIeee8021BridgeBaseMode'
_H='etsysIeee8021BridgeMibExtMrpEntry'
_G='read-write'
_F='Integer32'
_E='EnabledStatus'
_D='ieee8021BridgeBasePort'
_C='IEEE8021-BRIDGE-MIB'
_B='ENTERASYS-IEEE8021-BRIDGE-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ieee8021BridgeBasePort,ieee8021BridgeBasePortEntry=mibBuilder.importSymbols(_C,_D,'ieee8021BridgeBasePortEntry')
IEEE8021PbbComponentIdentifier,=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysIeee8021BridgeMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,90))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMIB.setRevisions(('2012-02-07 14:35',))
_EtsysIeee8021BridgeMibExtObjects_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeMibExtObjects=_EtsysIeee8021BridgeMibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,1))
_EtsysIeee8021BridgeBase_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeBase=_EtsysIeee8021BridgeBase_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,1,1))
class _EtsysIeee8021BridgeBaseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerBackboneBridge',3)))
_EtsysIeee8021BridgeBaseMode_Type.__name__=_F
_EtsysIeee8021BridgeBaseMode_Object=MibScalar
etsysIeee8021BridgeBaseMode=_EtsysIeee8021BridgeBaseMode_Object((1,3,6,1,4,1,5624,1,2,90,1,1,1),_EtsysIeee8021BridgeBaseMode_Type())
etsysIeee8021BridgeBaseMode.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIeee8021BridgeBaseMode.setStatus(_A)
_EtsysIeee8021BridgeBasePortTable_Object=MibTable
etsysIeee8021BridgeBasePortTable=_EtsysIeee8021BridgeBasePortTable_Object((1,3,6,1,4,1,5624,1,2,90,1,1,2))
if mibBuilder.loadTexts:etsysIeee8021BridgeBasePortTable.setStatus(_A)
_EtsysIeee8021BridgeBasePortEntry_Object=MibTableRow
etsysIeee8021BridgeBasePortEntry=_EtsysIeee8021BridgeBasePortEntry_Object((1,3,6,1,4,1,5624,1,2,90,1,1,2,1))
etsysIeee8021BridgeBasePortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:etsysIeee8021BridgeBasePortEntry.setStatus(_A)
_Etsys8021BridgePortComponentId_Type=IEEE8021PbbComponentIdentifier
_Etsys8021BridgePortComponentId_Object=MibTableColumn
etsys8021BridgePortComponentId=_Etsys8021BridgePortComponentId_Object((1,3,6,1,4,1,5624,1,2,90,1,1,2,1,1),_Etsys8021BridgePortComponentId_Type())
etsys8021BridgePortComponentId.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsys8021BridgePortComponentId.setStatus(_A)
_EtsysIeee8021BridgeMibExtMrpBranch_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeMibExtMrpBranch=_EtsysIeee8021BridgeMibExtMrpBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,1,2))
_EtsysIeee8021BridgeMibExtMrpTable_Object=MibTable
etsysIeee8021BridgeMibExtMrpTable=_EtsysIeee8021BridgeMibExtMrpTable_Object((1,3,6,1,4,1,5624,1,2,90,1,2,1))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMrpTable.setStatus(_A)
_EtsysIeee8021BridgeMibExtMrpEntry_Object=MibTableRow
etsysIeee8021BridgeMibExtMrpEntry=_EtsysIeee8021BridgeMibExtMrpEntry_Object((1,3,6,1,4,1,5624,1,2,90,1,2,1,1))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMrpEntry.setStatus(_A)
class _EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type(EnabledStatus):defaultValue=2
_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type.__name__=_E
_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Object=MibTableColumn
etsysIeee8021BridgeMibExtMrpPeriodicEnabled=_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Object((1,3,6,1,4,1,5624,1,2,90,1,2,1,1,1),_EtsysIeee8021BridgeMibExtMrpPeriodicEnabled_Type())
etsysIeee8021BridgeMibExtMrpPeriodicEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMrpPeriodicEnabled.setStatus(_A)
_EtsysIeee8021BridgeMibExtConformance_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeMibExtConformance=_EtsysIeee8021BridgeMibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,2))
_EtsysIeee8021BridgeMibExtGroups_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeMibExtGroups=_EtsysIeee8021BridgeMibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,2,1))
_EtsysIeee8021BridgeMibExtCompliances_ObjectIdentity=ObjectIdentity
etsysIeee8021BridgeMibExtCompliances=_EtsysIeee8021BridgeMibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,90,2,2))
ieee8021BridgeBasePortEntry.registerAugmentions((_B,_H))
etsysIeee8021BridgeMibExtMrpEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
etsysIeee8021BridgeMibExtBaseModeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,90,2,1,1))
etsysIeee8021BridgeMibExtBaseModeGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtBaseModeGroup.setStatus(_A)
etsysIeee8021BridgeMibExtBasePortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,90,2,1,2))
etsysIeee8021BridgeMibExtBasePortGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtBasePortGroup.setStatus(_A)
etsysIeee8021BridgeMibExtMrpGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,90,2,1,3))
etsysIeee8021BridgeMibExtMrpGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMrpGroup.setStatus(_A)
etsysIeee8021BridgeMibExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,90,2,2,1))
etsysIeee8021BridgeMibExtCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtCompliance.setStatus(_A)
etsysIeee8021BridgeMibExtMrpCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,90,2,2,2))
etsysIeee8021BridgeMibExtMrpCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:etsysIeee8021BridgeMibExtMrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysIeee8021BridgeMibExtMIB':etsysIeee8021BridgeMibExtMIB,'etsysIeee8021BridgeMibExtObjects':etsysIeee8021BridgeMibExtObjects,'etsysIeee8021BridgeBase':etsysIeee8021BridgeBase,_I:etsysIeee8021BridgeBaseMode,'etsysIeee8021BridgeBasePortTable':etsysIeee8021BridgeBasePortTable,'etsysIeee8021BridgeBasePortEntry':etsysIeee8021BridgeBasePortEntry,_J:etsys8021BridgePortComponentId,'etsysIeee8021BridgeMibExtMrpBranch':etsysIeee8021BridgeMibExtMrpBranch,'etsysIeee8021BridgeMibExtMrpTable':etsysIeee8021BridgeMibExtMrpTable,_H:etsysIeee8021BridgeMibExtMrpEntry,_K:etsysIeee8021BridgeMibExtMrpPeriodicEnabled,'etsysIeee8021BridgeMibExtConformance':etsysIeee8021BridgeMibExtConformance,'etsysIeee8021BridgeMibExtGroups':etsysIeee8021BridgeMibExtGroups,_L:etsysIeee8021BridgeMibExtBaseModeGroup,_M:etsysIeee8021BridgeMibExtBasePortGroup,_N:etsysIeee8021BridgeMibExtMrpGroup,'etsysIeee8021BridgeMibExtCompliances':etsysIeee8021BridgeMibExtCompliances,'etsysIeee8021BridgeMibExtCompliance':etsysIeee8021BridgeMibExtCompliance,'etsysIeee8021BridgeMibExtMrpCompliance':etsysIeee8021BridgeMibExtMrpCompliance})