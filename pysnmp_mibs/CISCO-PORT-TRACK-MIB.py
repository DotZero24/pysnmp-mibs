_N='cptShutGroup'
_M='cptTrackGroup'
_L='cptPortForceState'
_K='cptPortTrackRowStatus'
_J='cptPortTrackVsanIndex'
_I='cptPortTrackVsanType'
_H='not-accessible'
_G='cptPortTrackTrackedPort'
_F='TruthValue'
_E='Integer32'
_D='read-create'
_C='cptPortTrackLinkedPort'
_B='CISCO-PORT-TRACK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
VsanIndex,=mibBuilder.importSymbols('CISCO-ST-TC','VsanIndex')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
ciscoPortTrackMIB=ModuleIdentity((1,3,6,1,4,1,9,9,437))
if mibBuilder.loadTexts:ciscoPortTrackMIB.setRevisions(('2005-04-27 00:00',))
_CiscoPortTrackObjects_ObjectIdentity=ObjectIdentity
ciscoPortTrackObjects=_CiscoPortTrackObjects_ObjectIdentity((1,3,6,1,4,1,9,9,437,1))
_CptConfig_ObjectIdentity=ObjectIdentity
cptConfig=_CptConfig_ObjectIdentity((1,3,6,1,4,1,9,9,437,1,1))
_CptPortTrackTable_Object=MibTable
cptPortTrackTable=_CptPortTrackTable_Object((1,3,6,1,4,1,9,9,437,1,1,1))
if mibBuilder.loadTexts:cptPortTrackTable.setStatus(_A)
_CptPortTrackEntry_Object=MibTableRow
cptPortTrackEntry=_CptPortTrackEntry_Object((1,3,6,1,4,1,9,9,437,1,1,1,1))
cptPortTrackEntry.setIndexNames((0,_B,_C),(0,_B,_G))
if mibBuilder.loadTexts:cptPortTrackEntry.setStatus(_A)
_CptPortTrackLinkedPort_Type=InterfaceIndex
_CptPortTrackLinkedPort_Object=MibTableColumn
cptPortTrackLinkedPort=_CptPortTrackLinkedPort_Object((1,3,6,1,4,1,9,9,437,1,1,1,1,1),_CptPortTrackLinkedPort_Type())
cptPortTrackLinkedPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cptPortTrackLinkedPort.setStatus(_A)
_CptPortTrackTrackedPort_Type=InterfaceIndex
_CptPortTrackTrackedPort_Object=MibTableColumn
cptPortTrackTrackedPort=_CptPortTrackTrackedPort_Object((1,3,6,1,4,1,9,9,437,1,1,1,1,2),_CptPortTrackTrackedPort_Type())
cptPortTrackTrackedPort.setMaxAccess(_H)
if mibBuilder.loadTexts:cptPortTrackTrackedPort.setStatus(_A)
class _CptPortTrackVsanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleVsan',1),('allVsans',2)))
_CptPortTrackVsanType_Type.__name__=_E
_CptPortTrackVsanType_Object=MibTableColumn
cptPortTrackVsanType=_CptPortTrackVsanType_Object((1,3,6,1,4,1,9,9,437,1,1,1,1,3),_CptPortTrackVsanType_Type())
cptPortTrackVsanType.setMaxAccess(_D)
if mibBuilder.loadTexts:cptPortTrackVsanType.setStatus(_A)
_CptPortTrackVsanIndex_Type=VsanIndex
_CptPortTrackVsanIndex_Object=MibTableColumn
cptPortTrackVsanIndex=_CptPortTrackVsanIndex_Object((1,3,6,1,4,1,9,9,437,1,1,1,1,4),_CptPortTrackVsanIndex_Type())
cptPortTrackVsanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cptPortTrackVsanIndex.setStatus(_A)
_CptPortTrackRowStatus_Type=RowStatus
_CptPortTrackRowStatus_Object=MibTableColumn
cptPortTrackRowStatus=_CptPortTrackRowStatus_Object((1,3,6,1,4,1,9,9,437,1,1,1,1,5),_CptPortTrackRowStatus_Type())
cptPortTrackRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cptPortTrackRowStatus.setStatus(_A)
_CptPortForceShutTable_Object=MibTable
cptPortForceShutTable=_CptPortForceShutTable_Object((1,3,6,1,4,1,9,9,437,1,1,2))
if mibBuilder.loadTexts:cptPortForceShutTable.setStatus(_A)
_CptPortForceShutEntry_Object=MibTableRow
cptPortForceShutEntry=_CptPortForceShutEntry_Object((1,3,6,1,4,1,9,9,437,1,1,2,1))
cptPortForceShutEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:cptPortForceShutEntry.setStatus(_A)
class _CptPortForceState_Type(TruthValue):defaultValue=2
_CptPortForceState_Type.__name__=_F
_CptPortForceState_Object=MibTableColumn
cptPortForceState=_CptPortForceState_Object((1,3,6,1,4,1,9,9,437,1,1,2,1,1),_CptPortForceState_Type())
cptPortForceState.setMaxAccess('read-write')
if mibBuilder.loadTexts:cptPortForceState.setStatus(_A)
_CptMIBConformance_ObjectIdentity=ObjectIdentity
cptMIBConformance=_CptMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,437,2))
_CptMIBCompliances_ObjectIdentity=ObjectIdentity
cptMIBCompliances=_CptMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,437,2,1))
_CptMIBGroups_ObjectIdentity=ObjectIdentity
cptMIBGroups=_CptMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,437,2,2))
cptTrackGroup=ObjectGroup((1,3,6,1,4,1,9,9,437,2,2,1))
cptTrackGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cptTrackGroup.setStatus(_A)
cptShutGroup=ObjectGroup((1,3,6,1,4,1,9,9,437,2,2,2))
cptShutGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:cptShutGroup.setStatus(_A)
cptMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,437,2,1,1))
cptMIBCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cptMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoPortTrackMIB':ciscoPortTrackMIB,'ciscoPortTrackObjects':ciscoPortTrackObjects,'cptConfig':cptConfig,'cptPortTrackTable':cptPortTrackTable,'cptPortTrackEntry':cptPortTrackEntry,_C:cptPortTrackLinkedPort,_G:cptPortTrackTrackedPort,_I:cptPortTrackVsanType,_J:cptPortTrackVsanIndex,_K:cptPortTrackRowStatus,'cptPortForceShutTable':cptPortForceShutTable,'cptPortForceShutEntry':cptPortForceShutEntry,_L:cptPortForceState,'cptMIBConformance':cptMIBConformance,'cptMIBCompliances':cptMIBCompliances,'cptMIBCompliance':cptMIBCompliance,'cptMIBGroups':cptMIBGroups,_M:cptTrackGroup,_N:cptShutGroup})