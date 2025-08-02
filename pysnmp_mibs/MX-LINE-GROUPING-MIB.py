_R='lineGroupingVer1'
_Q='lineGrpConfCallForwardNoRessourceAddress'
_P='lineGrpConfCallForwardNoRessourceEnable'
_O='lineGrpConfLineSelectionAlgorithm'
_N='lineGrpAssocGroupIndex'
_M='lineGrpAssocIfType'
_L='lineGroupingNbGroups'
_K='read-only'
_J='MxSignalingAddress'
_I='MxEnableState'
_H='ifIndex'
_G='IF-MIB'
_F='groupIndex'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='MX-LINE-GROUPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,MxSignalingAddress=mibBuilder.importSymbols('MX-TC',_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lineGroupingMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,80))
if mibBuilder.loadTexts:lineGroupingMIB.setRevisions(('1903-07-17 00:00',))
_LineGroupingMIBObjects_ObjectIdentity=ObjectIdentity
lineGroupingMIBObjects=_LineGroupingMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,80,1))
class _LineGroupingNbGroups_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_LineGroupingNbGroups_Type.__name__=_D
_LineGroupingNbGroups_Object=MibScalar
lineGroupingNbGroups=_LineGroupingNbGroups_Object((1,3,6,1,4,1,4935,15,80,1,5),_LineGroupingNbGroups_Type())
lineGroupingNbGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:lineGroupingNbGroups.setStatus(_A)
_LineGroupingIfAssociationTable_Object=MibTable
lineGroupingIfAssociationTable=_LineGroupingIfAssociationTable_Object((1,3,6,1,4,1,4935,15,80,1,10))
if mibBuilder.loadTexts:lineGroupingIfAssociationTable.setStatus(_A)
_LineGroupingIfAssociationEntry_Object=MibTableRow
lineGroupingIfAssociationEntry=_LineGroupingIfAssociationEntry_Object((1,3,6,1,4,1,4935,15,80,1,10,5))
lineGroupingIfAssociationEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:lineGroupingIfAssociationEntry.setStatus(_A)
class _LineGrpAssocIfType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fxo',0),('fxs',1)))
_LineGrpAssocIfType_Type.__name__=_E
_LineGrpAssocIfType_Object=MibTableColumn
lineGrpAssocIfType=_LineGrpAssocIfType_Object((1,3,6,1,4,1,4935,15,80,1,10,5,5),_LineGrpAssocIfType_Type())
lineGrpAssocIfType.setMaxAccess(_K)
if mibBuilder.loadTexts:lineGrpAssocIfType.setStatus(_A)
class _LineGrpAssocGroupIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_LineGrpAssocGroupIndex_Type.__name__=_D
_LineGrpAssocGroupIndex_Object=MibTableColumn
lineGrpAssocGroupIndex=_LineGrpAssocGroupIndex_Object((1,3,6,1,4,1,4935,15,80,1,10,5,10),_LineGrpAssocGroupIndex_Type())
lineGrpAssocGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lineGrpAssocGroupIndex.setStatus(_A)
_LineGroupingGroupConfigTable_Object=MibTable
lineGroupingGroupConfigTable=_LineGroupingGroupConfigTable_Object((1,3,6,1,4,1,4935,15,80,1,15))
if mibBuilder.loadTexts:lineGroupingGroupConfigTable.setStatus(_A)
_LineGroupingGroupConfigEntry_Object=MibTableRow
lineGroupingGroupConfigEntry=_LineGroupingGroupConfigEntry_Object((1,3,6,1,4,1,4935,15,80,1,15,5))
lineGroupingGroupConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lineGroupingGroupConfigEntry.setStatus(_A)
class _GroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_GroupIndex_Type.__name__=_D
_GroupIndex_Object=MibTableColumn
groupIndex=_GroupIndex_Object((1,3,6,1,4,1,4935,15,80,1,15,5,5),_GroupIndex_Type())
groupIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:groupIndex.setStatus(_A)
class _LineGrpConfLineSelectionAlgorithm_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('roundRobin',0),('lowToHigh',1),('highToLow',2)))
_LineGrpConfLineSelectionAlgorithm_Type.__name__=_E
_LineGrpConfLineSelectionAlgorithm_Object=MibTableColumn
lineGrpConfLineSelectionAlgorithm=_LineGrpConfLineSelectionAlgorithm_Object((1,3,6,1,4,1,4935,15,80,1,15,5,10),_LineGrpConfLineSelectionAlgorithm_Type())
lineGrpConfLineSelectionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:lineGrpConfLineSelectionAlgorithm.setStatus(_A)
class _LineGrpConfCallForwardNoRessourceEnable_Type(MxEnableState):defaultValue=0
_LineGrpConfCallForwardNoRessourceEnable_Type.__name__=_I
_LineGrpConfCallForwardNoRessourceEnable_Object=MibTableColumn
lineGrpConfCallForwardNoRessourceEnable=_LineGrpConfCallForwardNoRessourceEnable_Object((1,3,6,1,4,1,4935,15,80,1,15,5,15),_LineGrpConfCallForwardNoRessourceEnable_Type())
lineGrpConfCallForwardNoRessourceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:lineGrpConfCallForwardNoRessourceEnable.setStatus(_A)
class _LineGrpConfCallForwardNoRessourceAddress_Type(MxSignalingAddress):defaultValue=OctetString('')
_LineGrpConfCallForwardNoRessourceAddress_Type.__name__=_J
_LineGrpConfCallForwardNoRessourceAddress_Object=MibTableColumn
lineGrpConfCallForwardNoRessourceAddress=_LineGrpConfCallForwardNoRessourceAddress_Object((1,3,6,1,4,1,4935,15,80,1,15,5,20),_LineGrpConfCallForwardNoRessourceAddress_Type())
lineGrpConfCallForwardNoRessourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lineGrpConfCallForwardNoRessourceAddress.setStatus(_A)
_LineGroupingConformance_ObjectIdentity=ObjectIdentity
lineGroupingConformance=_LineGroupingConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,80,5))
_LineGroupingCompliances_ObjectIdentity=ObjectIdentity
lineGroupingCompliances=_LineGroupingCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,80,5,1))
_LineGroupingGroups_ObjectIdentity=ObjectIdentity
lineGroupingGroups=_LineGroupingGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,80,5,5))
lineGroupingVer1=ObjectGroup((1,3,6,1,4,1,4935,15,80,5,5,10))
lineGroupingVer1.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:lineGroupingVer1.setStatus(_A)
lineGroupingComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,80,5,1,1))
lineGroupingComplVer1.setObjects((_B,_R))
if mibBuilder.loadTexts:lineGroupingComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lineGroupingMIB':lineGroupingMIB,'lineGroupingMIBObjects':lineGroupingMIBObjects,_L:lineGroupingNbGroups,'lineGroupingIfAssociationTable':lineGroupingIfAssociationTable,'lineGroupingIfAssociationEntry':lineGroupingIfAssociationEntry,_M:lineGrpAssocIfType,_N:lineGrpAssocGroupIndex,'lineGroupingGroupConfigTable':lineGroupingGroupConfigTable,'lineGroupingGroupConfigEntry':lineGroupingGroupConfigEntry,_F:groupIndex,_O:lineGrpConfLineSelectionAlgorithm,_P:lineGrpConfCallForwardNoRessourceEnable,_Q:lineGrpConfCallForwardNoRessourceAddress,'lineGroupingConformance':lineGroupingConformance,'lineGroupingCompliances':lineGroupingCompliances,'lineGroupingComplVer1':lineGroupingComplVer1,'lineGroupingGroups':lineGroupingGroups,_R:lineGroupingVer1})