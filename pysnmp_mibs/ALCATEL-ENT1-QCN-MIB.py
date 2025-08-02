_Q='alaQcnPortInstanceGroup'
_P='alaQcnGlobalGroup'
_O='alaQcnPICncpReset'
_N='alaQcnPICncpStatsClear'
_M='alaQcnPIPriorityReset'
_L='alaQcnGlobalCID'
_K='alaQcnGlobalCNMVlanTag'
_J='alaQcnPIPriority'
_I='alaQcnPIIfIndex'
_H='alaQcnGlobalCompId'
_G='true'
_F='not-accessible'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='ALCATEL-ENT1-QCN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1QcnMib,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1QcnMib')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
alcatelIND1QcnMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1))
if mibBuilder.loadTexts:alcatelIND1QcnMIB.setRevisions(('2011-09-01 00:00',))
_AlcatelIND1QcnMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1QcnMIBObjects=_AlcatelIND1QcnMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,1))
if mibBuilder.loadTexts:alcatelIND1QcnMIBObjects.setStatus(_A)
_AlaQcnConfig_ObjectIdentity=ObjectIdentity
alaQcnConfig=_AlaQcnConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1))
_AlaQcnGlobalTable_Object=MibTable
alaQcnGlobalTable=_AlaQcnGlobalTable_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,1))
if mibBuilder.loadTexts:alaQcnGlobalTable.setStatus(_A)
_AlaQcnGlobalEntry_Object=MibTableRow
alaQcnGlobalEntry=_AlaQcnGlobalEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,1,1))
alaQcnGlobalEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:alaQcnGlobalEntry.setStatus(_A)
class _AlaQcnGlobalCompId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AlaQcnGlobalCompId_Type.__name__=_D
_AlaQcnGlobalCompId_Object=MibTableColumn
alaQcnGlobalCompId=_AlaQcnGlobalCompId_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,1,1,1),_AlaQcnGlobalCompId_Type())
alaQcnGlobalCompId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaQcnGlobalCompId.setStatus(_A)
class _AlaQcnGlobalCNMVlanTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_AlaQcnGlobalCNMVlanTag_Type.__name__=_D
_AlaQcnGlobalCNMVlanTag_Object=MibTableColumn
alaQcnGlobalCNMVlanTag=_AlaQcnGlobalCNMVlanTag_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,1,1,2),_AlaQcnGlobalCNMVlanTag_Type())
alaQcnGlobalCNMVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaQcnGlobalCNMVlanTag.setStatus(_A)
class _AlaQcnGlobalCID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AlaQcnGlobalCID_Type.__name__=_D
_AlaQcnGlobalCID_Object=MibTableColumn
alaQcnGlobalCID=_AlaQcnGlobalCID_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,1,1,3),_AlaQcnGlobalCID_Type())
alaQcnGlobalCID.setMaxAccess(_C)
if mibBuilder.loadTexts:alaQcnGlobalCID.setStatus(_A)
_AlaQcnPortInstanceTable_Object=MibTable
alaQcnPortInstanceTable=_AlaQcnPortInstanceTable_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2))
if mibBuilder.loadTexts:alaQcnPortInstanceTable.setStatus(_A)
_AlaQcnPortInstanceEntry_Object=MibTableRow
alaQcnPortInstanceEntry=_AlaQcnPortInstanceEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1))
alaQcnPortInstanceEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:alaQcnPortInstanceEntry.setStatus(_A)
_AlaQcnPIIfIndex_Type=Unsigned32
_AlaQcnPIIfIndex_Object=MibTableColumn
alaQcnPIIfIndex=_AlaQcnPIIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1,1),_AlaQcnPIIfIndex_Type())
alaQcnPIIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:alaQcnPIIfIndex.setStatus(_A)
_AlaQcnPIPriority_Type=Unsigned32
_AlaQcnPIPriority_Object=MibTableColumn
alaQcnPIPriority=_AlaQcnPIPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1,2),_AlaQcnPIPriority_Type())
alaQcnPIPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:alaQcnPIPriority.setStatus(_A)
class _AlaQcnPIPriorityReset_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_AlaQcnPIPriorityReset_Type.__name__=_E
_AlaQcnPIPriorityReset_Object=MibTableColumn
alaQcnPIPriorityReset=_AlaQcnPIPriorityReset_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1,3),_AlaQcnPIPriorityReset_Type())
alaQcnPIPriorityReset.setMaxAccess(_C)
if mibBuilder.loadTexts:alaQcnPIPriorityReset.setStatus(_A)
class _AlaQcnPICncpStatsClear_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_AlaQcnPICncpStatsClear_Type.__name__=_E
_AlaQcnPICncpStatsClear_Object=MibTableColumn
alaQcnPICncpStatsClear=_AlaQcnPICncpStatsClear_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1,4),_AlaQcnPICncpStatsClear_Type())
alaQcnPICncpStatsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:alaQcnPICncpStatsClear.setStatus(_A)
class _AlaQcnPICncpReset_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_AlaQcnPICncpReset_Type.__name__=_E
_AlaQcnPICncpReset_Object=MibTableColumn
alaQcnPICncpReset=_AlaQcnPICncpReset_Object((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,1,2,1,5),_AlaQcnPICncpReset_Type())
alaQcnPICncpReset.setMaxAccess(_C)
if mibBuilder.loadTexts:alaQcnPICncpReset.setStatus(_A)
_AlaQcnConformance_ObjectIdentity=ObjectIdentity
alaQcnConformance=_AlaQcnConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,1,2))
_AlcatelIND1QcnMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1QcnMIBConformance=_AlcatelIND1QcnMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,2))
if mibBuilder.loadTexts:alcatelIND1QcnMIBConformance.setStatus(_A)
_AlcatelIND1QcnMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1QcnMIBGroups=_AlcatelIND1QcnMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,2,1))
if mibBuilder.loadTexts:alcatelIND1QcnMIBGroups.setStatus(_A)
_AlcatelIND1QcnMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1QcnMIBCompliances=_AlcatelIND1QcnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,71,1,2,2))
if mibBuilder.loadTexts:alcatelIND1QcnMIBCompliances.setStatus(_A)
alaQcnGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,71,1,2,1,1))
alaQcnGlobalGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaQcnGlobalGroup.setStatus(_A)
alaQcnPortInstanceGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,71,1,2,1,2))
alaQcnPortInstanceGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:alaQcnPortInstanceGroup.setStatus(_A)
alcatelIND1QcnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,71,1,2,2,1))
alcatelIND1QcnMIBCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alcatelIND1QcnMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1QcnMIB':alcatelIND1QcnMIB,'alcatelIND1QcnMIBObjects':alcatelIND1QcnMIBObjects,'alaQcnConfig':alaQcnConfig,'alaQcnGlobalTable':alaQcnGlobalTable,'alaQcnGlobalEntry':alaQcnGlobalEntry,_H:alaQcnGlobalCompId,_K:alaQcnGlobalCNMVlanTag,_L:alaQcnGlobalCID,'alaQcnPortInstanceTable':alaQcnPortInstanceTable,'alaQcnPortInstanceEntry':alaQcnPortInstanceEntry,_I:alaQcnPIIfIndex,_J:alaQcnPIPriority,_M:alaQcnPIPriorityReset,_N:alaQcnPICncpStatsClear,_O:alaQcnPICncpReset,'alaQcnConformance':alaQcnConformance,'alcatelIND1QcnMIBConformance':alcatelIND1QcnMIBConformance,'alcatelIND1QcnMIBGroups':alcatelIND1QcnMIBGroups,_P:alaQcnGlobalGroup,_Q:alaQcnPortInstanceGroup,'alcatelIND1QcnMIBCompliances':alcatelIND1QcnMIBCompliances,'alcatelIND1QcnMIBCompliance':alcatelIND1QcnMIBCompliance})