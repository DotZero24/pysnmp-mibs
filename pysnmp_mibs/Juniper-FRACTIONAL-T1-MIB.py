_O='juniFt1Group2'
_N='juniFt1Group'
_M='juniFt1IfDataPolarity'
_L='juniFt1IfIndex'
_K='juniFt1IfLoopbackConfig'
_J='juniFt1IfTimeSlotRate'
_I='juniFt1IfTimeSlotMap'
_H='juniFt1IfLowerIfIndex'
_G='juniFt1IfRowStatus'
_F='juniFt1NextIfIndex'
_E='obsolete'
_D='Integer32'
_C='read-create'
_B='current'
_A='Juniper-FRACTIONAL-T1-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,JuniTimeSlotMap=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex','JuniTimeSlotMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniFt1MIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,6))
if mibBuilder.loadTexts:juniFt1MIB.setRevisions(('2002-09-16 21:44','2000-09-26 17:30','1999-07-14 00:00','1998-11-13 00:00'))
_JuniFt1Objects_ObjectIdentity=ObjectIdentity
juniFt1Objects=_JuniFt1Objects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,6,1))
_JuniFt1NextIfIndex_Type=JuniNextIfIndex
_JuniFt1NextIfIndex_Object=MibScalar
juniFt1NextIfIndex=_JuniFt1NextIfIndex_Object((1,3,6,1,4,1,4874,2,2,6,1,1),_JuniFt1NextIfIndex_Type())
juniFt1NextIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:juniFt1NextIfIndex.setStatus(_B)
_JuniFt1IfTable_Object=MibTable
juniFt1IfTable=_JuniFt1IfTable_Object((1,3,6,1,4,1,4874,2,2,6,1,2))
if mibBuilder.loadTexts:juniFt1IfTable.setStatus(_B)
_JuniFt1IfEntry_Object=MibTableRow
juniFt1IfEntry=_JuniFt1IfEntry_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1))
juniFt1IfEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:juniFt1IfEntry.setStatus(_B)
_JuniFt1IfIndex_Type=InterfaceIndex
_JuniFt1IfIndex_Object=MibTableColumn
juniFt1IfIndex=_JuniFt1IfIndex_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,1),_JuniFt1IfIndex_Type())
juniFt1IfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniFt1IfIndex.setStatus(_B)
_JuniFt1IfRowStatus_Type=RowStatus
_JuniFt1IfRowStatus_Object=MibTableColumn
juniFt1IfRowStatus=_JuniFt1IfRowStatus_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,2),_JuniFt1IfRowStatus_Type())
juniFt1IfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfRowStatus.setStatus(_B)
_JuniFt1IfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniFt1IfLowerIfIndex_Object=MibTableColumn
juniFt1IfLowerIfIndex=_JuniFt1IfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,3),_JuniFt1IfLowerIfIndex_Type())
juniFt1IfLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfLowerIfIndex.setStatus(_B)
_JuniFt1IfTimeSlotMap_Type=JuniTimeSlotMap
_JuniFt1IfTimeSlotMap_Object=MibTableColumn
juniFt1IfTimeSlotMap=_JuniFt1IfTimeSlotMap_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,4),_JuniFt1IfTimeSlotMap_Type())
juniFt1IfTimeSlotMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfTimeSlotMap.setStatus(_B)
class _JuniFt1IfTimeSlotRate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nx56kbps',0),('nx64kbps',1)))
_JuniFt1IfTimeSlotRate_Type.__name__=_D
_JuniFt1IfTimeSlotRate_Object=MibTableColumn
juniFt1IfTimeSlotRate=_JuniFt1IfTimeSlotRate_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,5),_JuniFt1IfTimeSlotRate_Type())
juniFt1IfTimeSlotRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfTimeSlotRate.setStatus(_B)
class _JuniFt1IfDataPolarity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('inverted',1)))
_JuniFt1IfDataPolarity_Type.__name__=_D
_JuniFt1IfDataPolarity_Object=MibTableColumn
juniFt1IfDataPolarity=_JuniFt1IfDataPolarity_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,6),_JuniFt1IfDataPolarity_Type())
juniFt1IfDataPolarity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfDataPolarity.setStatus(_E)
class _JuniFt1IfLoopbackConfig_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noLoop',0),('loop',1)))
_JuniFt1IfLoopbackConfig_Type.__name__=_D
_JuniFt1IfLoopbackConfig_Object=MibTableColumn
juniFt1IfLoopbackConfig=_JuniFt1IfLoopbackConfig_Object((1,3,6,1,4,1,4874,2,2,6,1,2,1,7),_JuniFt1IfLoopbackConfig_Type())
juniFt1IfLoopbackConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:juniFt1IfLoopbackConfig.setStatus(_B)
_JuniFt1Conformance_ObjectIdentity=ObjectIdentity
juniFt1Conformance=_JuniFt1Conformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,6,4))
_JuniFt1Compliances_ObjectIdentity=ObjectIdentity
juniFt1Compliances=_JuniFt1Compliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,6,4,1))
_JuniFt1Groups_ObjectIdentity=ObjectIdentity
juniFt1Groups=_JuniFt1Groups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,6,4,2))
juniFt1Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,6,4,2,1))
juniFt1Group.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:juniFt1Group.setStatus(_E)
juniFt1Group2=ObjectGroup((1,3,6,1,4,1,4874,2,2,6,4,2,2))
juniFt1Group2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniFt1Group2.setStatus(_B)
juniFt1Compliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,6,4,1,1))
juniFt1Compliance.setObjects((_A,_N))
if mibBuilder.loadTexts:juniFt1Compliance.setStatus(_E)
juniFt1Compliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,6,4,1,2))
juniFt1Compliance2.setObjects((_A,_O))
if mibBuilder.loadTexts:juniFt1Compliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniFt1MIB':juniFt1MIB,'juniFt1Objects':juniFt1Objects,_F:juniFt1NextIfIndex,'juniFt1IfTable':juniFt1IfTable,'juniFt1IfEntry':juniFt1IfEntry,_L:juniFt1IfIndex,_G:juniFt1IfRowStatus,_H:juniFt1IfLowerIfIndex,_I:juniFt1IfTimeSlotMap,_J:juniFt1IfTimeSlotRate,_M:juniFt1IfDataPolarity,_K:juniFt1IfLoopbackConfig,'juniFt1Conformance':juniFt1Conformance,'juniFt1Compliances':juniFt1Compliances,'juniFt1Compliance':juniFt1Compliance,'juniFt1Compliance2':juniFt1Compliance2,'juniFt1Groups':juniFt1Groups,_N:juniFt1Group,_O:juniFt1Group2})