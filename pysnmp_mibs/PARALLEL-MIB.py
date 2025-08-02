_T='paraGroup'
_S='paraOutSigChanges'
_R='paraOutSigState'
_Q='paraInSigChanges'
_P='paraInSigState'
_O='paraPortOutSigNumber'
_N='paraPortInSigNumber'
_M='paraPortType'
_L='paraNumber'
_K='paperout'
_J='online'
_I='paraOutSigName'
_H='paraOutSigPortIndex'
_G='paraInSigName'
_F='paraInSigPortIndex'
_E='paraPortIndex'
_D='Integer32'
_C='read-only'
_B='PARALLEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
para=ModuleIdentity((1,3,6,1,2,1,10,34))
_ParaNumber_Type=Integer32
_ParaNumber_Object=MibScalar
paraNumber=_ParaNumber_Object((1,3,6,1,2,1,10,34,1),_ParaNumber_Type())
paraNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:paraNumber.setStatus(_A)
_ParaPortTable_Object=MibTable
paraPortTable=_ParaPortTable_Object((1,3,6,1,2,1,10,34,2))
if mibBuilder.loadTexts:paraPortTable.setStatus(_A)
_ParaPortEntry_Object=MibTableRow
paraPortEntry=_ParaPortEntry_Object((1,3,6,1,2,1,10,34,2,1))
paraPortEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:paraPortEntry.setStatus(_A)
_ParaPortIndex_Type=InterfaceIndex
_ParaPortIndex_Object=MibTableColumn
paraPortIndex=_ParaPortIndex_Object((1,3,6,1,2,1,10,34,2,1,1),_ParaPortIndex_Type())
paraPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:paraPortIndex.setStatus(_A)
class _ParaPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('centronics',2),('dataproducts',3)))
_ParaPortType_Type.__name__=_D
_ParaPortType_Object=MibTableColumn
paraPortType=_ParaPortType_Object((1,3,6,1,2,1,10,34,2,1,2),_ParaPortType_Type())
paraPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:paraPortType.setStatus(_A)
_ParaPortInSigNumber_Type=Integer32
_ParaPortInSigNumber_Object=MibTableColumn
paraPortInSigNumber=_ParaPortInSigNumber_Object((1,3,6,1,2,1,10,34,2,1,3),_ParaPortInSigNumber_Type())
paraPortInSigNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:paraPortInSigNumber.setStatus(_A)
_ParaPortOutSigNumber_Type=Integer32
_ParaPortOutSigNumber_Object=MibTableColumn
paraPortOutSigNumber=_ParaPortOutSigNumber_Object((1,3,6,1,2,1,10,34,2,1,4),_ParaPortOutSigNumber_Type())
paraPortOutSigNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:paraPortOutSigNumber.setStatus(_A)
_ParaInSigTable_Object=MibTable
paraInSigTable=_ParaInSigTable_Object((1,3,6,1,2,1,10,34,3))
if mibBuilder.loadTexts:paraInSigTable.setStatus(_A)
_ParaInSigEntry_Object=MibTableRow
paraInSigEntry=_ParaInSigEntry_Object((1,3,6,1,2,1,10,34,3,1))
paraInSigEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:paraInSigEntry.setStatus(_A)
_ParaInSigPortIndex_Type=InterfaceIndex
_ParaInSigPortIndex_Object=MibTableColumn
paraInSigPortIndex=_ParaInSigPortIndex_Object((1,3,6,1,2,1,10,34,3,1,1),_ParaInSigPortIndex_Type())
paraInSigPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:paraInSigPortIndex.setStatus(_A)
class _ParaInSigName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('power',1),(_J,2),('busy',3),(_K,4),('fault',5)))
_ParaInSigName_Type.__name__=_D
_ParaInSigName_Object=MibTableColumn
paraInSigName=_ParaInSigName_Object((1,3,6,1,2,1,10,34,3,1,2),_ParaInSigName_Type())
paraInSigName.setMaxAccess(_C)
if mibBuilder.loadTexts:paraInSigName.setStatus(_A)
class _ParaInSigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('on',2),('off',3)))
_ParaInSigState_Type.__name__=_D
_ParaInSigState_Object=MibTableColumn
paraInSigState=_ParaInSigState_Object((1,3,6,1,2,1,10,34,3,1,3),_ParaInSigState_Type())
paraInSigState.setMaxAccess(_C)
if mibBuilder.loadTexts:paraInSigState.setStatus(_A)
_ParaInSigChanges_Type=Counter32
_ParaInSigChanges_Object=MibTableColumn
paraInSigChanges=_ParaInSigChanges_Object((1,3,6,1,2,1,10,34,3,1,4),_ParaInSigChanges_Type())
paraInSigChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:paraInSigChanges.setStatus(_A)
_ParaOutSigTable_Object=MibTable
paraOutSigTable=_ParaOutSigTable_Object((1,3,6,1,2,1,10,34,4))
if mibBuilder.loadTexts:paraOutSigTable.setStatus(_A)
_ParaOutSigEntry_Object=MibTableRow
paraOutSigEntry=_ParaOutSigEntry_Object((1,3,6,1,2,1,10,34,4,1))
paraOutSigEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:paraOutSigEntry.setStatus(_A)
_ParaOutSigPortIndex_Type=InterfaceIndex
_ParaOutSigPortIndex_Object=MibTableColumn
paraOutSigPortIndex=_ParaOutSigPortIndex_Object((1,3,6,1,2,1,10,34,4,1,1),_ParaOutSigPortIndex_Type())
paraOutSigPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:paraOutSigPortIndex.setStatus(_A)
class _ParaOutSigName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('power',1),(_J,2),('busy',3),(_K,4),('fault',5)))
_ParaOutSigName_Type.__name__=_D
_ParaOutSigName_Object=MibTableColumn
paraOutSigName=_ParaOutSigName_Object((1,3,6,1,2,1,10,34,4,1,2),_ParaOutSigName_Type())
paraOutSigName.setMaxAccess(_C)
if mibBuilder.loadTexts:paraOutSigName.setStatus(_A)
class _ParaOutSigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('on',2),('off',3)))
_ParaOutSigState_Type.__name__=_D
_ParaOutSigState_Object=MibTableColumn
paraOutSigState=_ParaOutSigState_Object((1,3,6,1,2,1,10,34,4,1,3),_ParaOutSigState_Type())
paraOutSigState.setMaxAccess(_C)
if mibBuilder.loadTexts:paraOutSigState.setStatus(_A)
_ParaOutSigChanges_Type=Counter32
_ParaOutSigChanges_Object=MibTableColumn
paraOutSigChanges=_ParaOutSigChanges_Object((1,3,6,1,2,1,10,34,4,1,4),_ParaOutSigChanges_Type())
paraOutSigChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:paraOutSigChanges.setStatus(_A)
_ParaConformance_ObjectIdentity=ObjectIdentity
paraConformance=_ParaConformance_ObjectIdentity((1,3,6,1,2,1,10,34,5))
_ParaGroups_ObjectIdentity=ObjectIdentity
paraGroups=_ParaGroups_ObjectIdentity((1,3,6,1,2,1,10,34,5,1))
_ParaCompliances_ObjectIdentity=ObjectIdentity
paraCompliances=_ParaCompliances_ObjectIdentity((1,3,6,1,2,1,10,34,5,2))
paraGroup=ObjectGroup((1,3,6,1,2,1,10,34,5,1,1))
paraGroup.setObjects(*((_B,_L),(_B,_E),(_B,_M),(_B,_N),(_B,_O),(_B,_F),(_B,_G),(_B,_P),(_B,_Q),(_B,_H),(_B,_I),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:paraGroup.setStatus(_A)
paraCompliance=ModuleCompliance((1,3,6,1,2,1,10,34,5,2,1))
paraCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:paraCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'para':para,_L:paraNumber,'paraPortTable':paraPortTable,'paraPortEntry':paraPortEntry,_E:paraPortIndex,_M:paraPortType,_N:paraPortInSigNumber,_O:paraPortOutSigNumber,'paraInSigTable':paraInSigTable,'paraInSigEntry':paraInSigEntry,_F:paraInSigPortIndex,_G:paraInSigName,_P:paraInSigState,_Q:paraInSigChanges,'paraOutSigTable':paraOutSigTable,'paraOutSigEntry':paraOutSigEntry,_H:paraOutSigPortIndex,_I:paraOutSigName,_R:paraOutSigState,_S:paraOutSigChanges,'paraConformance':paraConformance,'paraGroups':paraGroups,_T:paraGroup,'paraCompliances':paraCompliances,'paraCompliance':paraCompliance})