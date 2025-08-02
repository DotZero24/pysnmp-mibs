_P='cmTopologyObjectGroup'
_O='cmTopologyLinkToPort'
_N='cmTopologyLinkId'
_M='cmTopologyItemDescr'
_L='cmTopologyItemId'
_K='cmTopologyRegionLastUpdateTime'
_J='cmTopologyRegionDescr'
_I='cmTopologyRegionId'
_H='neIndex'
_G='CM-ENTITY-MIB'
_F='cmTopologyLinkFromPort'
_E='read-only'
_D='read-write'
_C='DisplayString'
_B='CM-TOPOLOGY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
neIndex,shelfIndex,slotIndex=mibBuilder.importSymbols(_G,_H,'shelfIndex','slotIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'PhysAddress','TextualConvention','VariablePointer')
cmTopologyMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,9))
if mibBuilder.loadTexts:cmTopologyMIB.setRevisions(('2008-03-03 00:00',))
_CmTopologyObjects_ObjectIdentity=ObjectIdentity
cmTopologyObjects=_CmTopologyObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,9,1))
class _CmTopologyRegionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTopologyRegionId_Type.__name__=_C
_CmTopologyRegionId_Object=MibScalar
cmTopologyRegionId=_CmTopologyRegionId_Object((1,3,6,1,4,1,2544,1,12,9,1,1),_CmTopologyRegionId_Type())
cmTopologyRegionId.setMaxAccess(_D)
if mibBuilder.loadTexts:cmTopologyRegionId.setStatus(_A)
class _CmTopologyRegionDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CmTopologyRegionDescr_Type.__name__=_C
_CmTopologyRegionDescr_Object=MibScalar
cmTopologyRegionDescr=_CmTopologyRegionDescr_Object((1,3,6,1,4,1,2544,1,12,9,1,2),_CmTopologyRegionDescr_Type())
cmTopologyRegionDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cmTopologyRegionDescr.setStatus(_A)
_CmTopologyRegionLastUpdateTime_Type=DateAndTime
_CmTopologyRegionLastUpdateTime_Object=MibScalar
cmTopologyRegionLastUpdateTime=_CmTopologyRegionLastUpdateTime_Object((1,3,6,1,4,1,2544,1,12,9,1,3),_CmTopologyRegionLastUpdateTime_Type())
cmTopologyRegionLastUpdateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cmTopologyRegionLastUpdateTime.setStatus(_A)
_CmTopologyItemTable_Object=MibTable
cmTopologyItemTable=_CmTopologyItemTable_Object((1,3,6,1,4,1,2544,1,12,9,1,4))
if mibBuilder.loadTexts:cmTopologyItemTable.setStatus(_A)
_CmTopologyItemEntry_Object=MibTableRow
cmTopologyItemEntry=_CmTopologyItemEntry_Object((1,3,6,1,4,1,2544,1,12,9,1,4,1))
cmTopologyItemEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cmTopologyItemEntry.setStatus(_A)
class _CmTopologyItemId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CmTopologyItemId_Type.__name__=_C
_CmTopologyItemId_Object=MibTableColumn
cmTopologyItemId=_CmTopologyItemId_Object((1,3,6,1,4,1,2544,1,12,9,1,4,1,1),_CmTopologyItemId_Type())
cmTopologyItemId.setMaxAccess(_D)
if mibBuilder.loadTexts:cmTopologyItemId.setStatus(_A)
class _CmTopologyItemDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CmTopologyItemDescr_Type.__name__=_C
_CmTopologyItemDescr_Object=MibTableColumn
cmTopologyItemDescr=_CmTopologyItemDescr_Object((1,3,6,1,4,1,2544,1,12,9,1,4,1,2),_CmTopologyItemDescr_Type())
cmTopologyItemDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cmTopologyItemDescr.setStatus(_A)
_CmTopologyLinkTable_Object=MibTable
cmTopologyLinkTable=_CmTopologyLinkTable_Object((1,3,6,1,4,1,2544,1,12,9,1,5))
if mibBuilder.loadTexts:cmTopologyLinkTable.setStatus(_A)
_CmTopologyLinkEntry_Object=MibTableRow
cmTopologyLinkEntry=_CmTopologyLinkEntry_Object((1,3,6,1,4,1,2544,1,12,9,1,5,1))
cmTopologyLinkEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cmTopologyLinkEntry.setStatus(_A)
class _CmTopologyLinkId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmTopologyLinkId_Type.__name__=_C
_CmTopologyLinkId_Object=MibTableColumn
cmTopologyLinkId=_CmTopologyLinkId_Object((1,3,6,1,4,1,2544,1,12,9,1,5,1,1),_CmTopologyLinkId_Type())
cmTopologyLinkId.setMaxAccess(_D)
if mibBuilder.loadTexts:cmTopologyLinkId.setStatus(_A)
_CmTopologyLinkFromPort_Type=VariablePointer
_CmTopologyLinkFromPort_Object=MibTableColumn
cmTopologyLinkFromPort=_CmTopologyLinkFromPort_Object((1,3,6,1,4,1,2544,1,12,9,1,5,1,2),_CmTopologyLinkFromPort_Type())
cmTopologyLinkFromPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cmTopologyLinkFromPort.setStatus(_A)
_CmTopologyLinkToPort_Type=VariablePointer
_CmTopologyLinkToPort_Object=MibTableColumn
cmTopologyLinkToPort=_CmTopologyLinkToPort_Object((1,3,6,1,4,1,2544,1,12,9,1,5,1,3),_CmTopologyLinkToPort_Type())
cmTopologyLinkToPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cmTopologyLinkToPort.setStatus(_A)
_CmTopologyConformance_ObjectIdentity=ObjectIdentity
cmTopologyConformance=_CmTopologyConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,9,2))
_CmTopologyCompliances_ObjectIdentity=ObjectIdentity
cmTopologyCompliances=_CmTopologyCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,9,2,1))
_CmTopologyGroups_ObjectIdentity=ObjectIdentity
cmTopologyGroups=_CmTopologyGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,9,2,2))
cmTopologyObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,9,2,2,1))
cmTopologyObjectGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O)))
if mibBuilder.loadTexts:cmTopologyObjectGroup.setStatus(_A)
cmTopologyCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,9,2,1,1))
cmTopologyCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:cmTopologyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmTopologyMIB':cmTopologyMIB,'cmTopologyObjects':cmTopologyObjects,_I:cmTopologyRegionId,_J:cmTopologyRegionDescr,_K:cmTopologyRegionLastUpdateTime,'cmTopologyItemTable':cmTopologyItemTable,'cmTopologyItemEntry':cmTopologyItemEntry,_L:cmTopologyItemId,_M:cmTopologyItemDescr,'cmTopologyLinkTable':cmTopologyLinkTable,'cmTopologyLinkEntry':cmTopologyLinkEntry,_N:cmTopologyLinkId,_F:cmTopologyLinkFromPort,_O:cmTopologyLinkToPort,'cmTopologyConformance':cmTopologyConformance,'cmTopologyCompliances':cmTopologyCompliances,'cmTopologyCompliance':cmTopologyCompliance,'cmTopologyGroups':cmTopologyGroups,_P:cmTopologyObjectGroup})