_Q='aristaXcvrDwdmGroup'
_P='aristaXcvrDwdmUncorrectedCodewords'
_O='aristaXcvrDwdmAdminFrequency'
_N='aristaXcvrDwdmModulationFormat'
_M='aristaXcvrDwdmTunable'
_L='aristaXcvrDwdmAdminGrid'
_K='aristaXcvrDwdmAdminChannel'
_J='aristaXcvrDwdmOperFrequency'
_I='aristaXcvrDwdmOperGrid'
_H='aristaXcvrDwdmOperChannel'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='ARISTA-XCVR-DWDM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
aristaXcvrDwdmMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,19))
if mibBuilder.loadTexts:aristaXcvrDwdmMIB.setRevisions(('2018-08-27 00:00','2018-05-16 00:00','2016-03-11 00:00'))
class AristaDwdmGridSpacing(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(6250,6250),ValueRangeConstraint(12500,12500),ValueRangeConstraint(25000,25000),ValueRangeConstraint(50000,50000),ValueRangeConstraint(100000,100000))
class AristaModulationFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notApplicable',0),('none',1),('qpsk',2),('eightQam',3),('sixteenQam',4)))
_AristaXcvrDwdmTable_Object=MibTable
aristaXcvrDwdmTable=_AristaXcvrDwdmTable_Object((1,3,6,1,4,1,30065,3,19,1))
if mibBuilder.loadTexts:aristaXcvrDwdmTable.setStatus(_A)
_AristaXcvrDwdmEntry_Object=MibTableRow
aristaXcvrDwdmEntry=_AristaXcvrDwdmEntry_Object((1,3,6,1,4,1,30065,3,19,1,1))
aristaXcvrDwdmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:aristaXcvrDwdmEntry.setStatus(_A)
_AristaXcvrDwdmOperChannel_Type=Unsigned32
_AristaXcvrDwdmOperChannel_Object=MibTableColumn
aristaXcvrDwdmOperChannel=_AristaXcvrDwdmOperChannel_Object((1,3,6,1,4,1,30065,3,19,1,1,1),_AristaXcvrDwdmOperChannel_Type())
aristaXcvrDwdmOperChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmOperChannel.setStatus(_A)
_AristaXcvrDwdmOperGrid_Type=AristaDwdmGridSpacing
_AristaXcvrDwdmOperGrid_Object=MibTableColumn
aristaXcvrDwdmOperGrid=_AristaXcvrDwdmOperGrid_Object((1,3,6,1,4,1,30065,3,19,1,1,2),_AristaXcvrDwdmOperGrid_Type())
aristaXcvrDwdmOperGrid.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmOperGrid.setStatus(_A)
_AristaXcvrDwdmOperFrequency_Type=Unsigned32
_AristaXcvrDwdmOperFrequency_Object=MibTableColumn
aristaXcvrDwdmOperFrequency=_AristaXcvrDwdmOperFrequency_Object((1,3,6,1,4,1,30065,3,19,1,1,3),_AristaXcvrDwdmOperFrequency_Type())
aristaXcvrDwdmOperFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmOperFrequency.setStatus(_A)
class _AristaXcvrDwdmAdminChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1000))
_AristaXcvrDwdmAdminChannel_Type.__name__=_G
_AristaXcvrDwdmAdminChannel_Object=MibTableColumn
aristaXcvrDwdmAdminChannel=_AristaXcvrDwdmAdminChannel_Object((1,3,6,1,4,1,30065,3,19,1,1,6),_AristaXcvrDwdmAdminChannel_Type())
aristaXcvrDwdmAdminChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXcvrDwdmAdminChannel.setStatus(_A)
_AristaXcvrDwdmAdminGrid_Type=AristaDwdmGridSpacing
_AristaXcvrDwdmAdminGrid_Object=MibTableColumn
aristaXcvrDwdmAdminGrid=_AristaXcvrDwdmAdminGrid_Object((1,3,6,1,4,1,30065,3,19,1,1,7),_AristaXcvrDwdmAdminGrid_Type())
aristaXcvrDwdmAdminGrid.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXcvrDwdmAdminGrid.setStatus(_A)
_AristaXcvrDwdmTunable_Type=TruthValue
_AristaXcvrDwdmTunable_Object=MibTableColumn
aristaXcvrDwdmTunable=_AristaXcvrDwdmTunable_Object((1,3,6,1,4,1,30065,3,19,1,1,8),_AristaXcvrDwdmTunable_Type())
aristaXcvrDwdmTunable.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmTunable.setStatus(_A)
_AristaXcvrDwdmModulationFormat_Type=AristaModulationFormat
_AristaXcvrDwdmModulationFormat_Object=MibTableColumn
aristaXcvrDwdmModulationFormat=_AristaXcvrDwdmModulationFormat_Object((1,3,6,1,4,1,30065,3,19,1,1,9),_AristaXcvrDwdmModulationFormat_Type())
aristaXcvrDwdmModulationFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmModulationFormat.setStatus(_A)
_AristaXcvrDwdmAdminFrequency_Type=Unsigned32
_AristaXcvrDwdmAdminFrequency_Object=MibTableColumn
aristaXcvrDwdmAdminFrequency=_AristaXcvrDwdmAdminFrequency_Object((1,3,6,1,4,1,30065,3,19,1,1,10),_AristaXcvrDwdmAdminFrequency_Type())
aristaXcvrDwdmAdminFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaXcvrDwdmAdminFrequency.setStatus(_A)
_AristaXcvrDwdmUncorrectedCodewords_Type=Counter64
_AristaXcvrDwdmUncorrectedCodewords_Object=MibTableColumn
aristaXcvrDwdmUncorrectedCodewords=_AristaXcvrDwdmUncorrectedCodewords_Object((1,3,6,1,4,1,30065,3,19,1,1,11),_AristaXcvrDwdmUncorrectedCodewords_Type())
aristaXcvrDwdmUncorrectedCodewords.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaXcvrDwdmUncorrectedCodewords.setStatus(_A)
_AristaXcvrDwdmMibConformance_ObjectIdentity=ObjectIdentity
aristaXcvrDwdmMibConformance=_AristaXcvrDwdmMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,19,2))
_AristaXcvrDwdmMibCompliances_ObjectIdentity=ObjectIdentity
aristaXcvrDwdmMibCompliances=_AristaXcvrDwdmMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,19,2,1))
_AristaXcvrDwdmMibGroups_ObjectIdentity=ObjectIdentity
aristaXcvrDwdmMibGroups=_AristaXcvrDwdmMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,19,2,2))
aristaXcvrDwdmGroup=ObjectGroup((1,3,6,1,4,1,30065,3,19,2,2,1))
aristaXcvrDwdmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:aristaXcvrDwdmGroup.setStatus(_A)
aristaXcvrDwdmMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,19,2,1,1))
aristaXcvrDwdmMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:aristaXcvrDwdmMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AristaDwdmGridSpacing':AristaDwdmGridSpacing,'AristaModulationFormat':AristaModulationFormat,'aristaXcvrDwdmMIB':aristaXcvrDwdmMIB,'aristaXcvrDwdmTable':aristaXcvrDwdmTable,'aristaXcvrDwdmEntry':aristaXcvrDwdmEntry,_H:aristaXcvrDwdmOperChannel,_I:aristaXcvrDwdmOperGrid,_J:aristaXcvrDwdmOperFrequency,_K:aristaXcvrDwdmAdminChannel,_L:aristaXcvrDwdmAdminGrid,_M:aristaXcvrDwdmTunable,_N:aristaXcvrDwdmModulationFormat,_O:aristaXcvrDwdmAdminFrequency,_P:aristaXcvrDwdmUncorrectedCodewords,'aristaXcvrDwdmMibConformance':aristaXcvrDwdmMibConformance,'aristaXcvrDwdmMibCompliances':aristaXcvrDwdmMibCompliances,'aristaXcvrDwdmMibCompliance':aristaXcvrDwdmMibCompliance,'aristaXcvrDwdmMibGroups':aristaXcvrDwdmMibGroups,_Q:aristaXcvrDwdmGroup})