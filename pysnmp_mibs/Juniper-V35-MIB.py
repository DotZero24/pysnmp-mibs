_Q='juniV35Group'
_P='juniV35IfLoopback'
_O='juniV35IfIgnoreDcd'
_N='juniV35IfTxClock'
_M='juniV35IfNrzEncoding'
_L='juniV35IfClockRate'
_K='juniV35IfMode'
_J='juniV35IfType'
_I='inverted'
_H='normal'
_G='read-only'
_F='juniV35IfIndex'
_E='Unsigned32'
_D='read-write'
_C='Integer32'
_B='Juniper-V35-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniV35MIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,59))
if mibBuilder.loadTexts:juniV35MIB.setRevisions(('2002-09-16 21:44','2002-02-08 16:25'))
_JuniV35Objects_ObjectIdentity=ObjectIdentity
juniV35Objects=_JuniV35Objects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,59,1))
_JuniV35IfTable_Object=MibTable
juniV35IfTable=_JuniV35IfTable_Object((1,3,6,1,4,1,4874,2,2,59,1,2))
if mibBuilder.loadTexts:juniV35IfTable.setStatus(_A)
_JuniV35IfEntry_Object=MibTableRow
juniV35IfEntry=_JuniV35IfEntry_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1))
juniV35IfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:juniV35IfEntry.setStatus(_A)
_JuniV35IfIndex_Type=InterfaceIndex
_JuniV35IfIndex_Object=MibTableColumn
juniV35IfIndex=_JuniV35IfIndex_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,1),_JuniV35IfIndex_Type())
juniV35IfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniV35IfIndex.setStatus(_A)
class _JuniV35IfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('x21',0),('v35',1),('interfaceTypeNoCable',2)))
_JuniV35IfType_Type.__name__=_C
_JuniV35IfType_Object=MibTableColumn
juniV35IfType=_JuniV35IfType_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,2),_JuniV35IfType_Type())
juniV35IfType.setMaxAccess(_G)
if mibBuilder.loadTexts:juniV35IfType.setStatus(_A)
class _JuniV35IfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dte',0),('dce',1),('interfaceModeNoCable',2)))
_JuniV35IfMode_Type.__name__=_C
_JuniV35IfMode_Object=MibTableColumn
juniV35IfMode=_JuniV35IfMode_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,3),_JuniV35IfMode_Type())
juniV35IfMode.setMaxAccess(_G)
if mibBuilder.loadTexts:juniV35IfMode.setStatus(_A)
class _JuniV35IfClockRate_Type(Unsigned32):defaultValue=2048000
_JuniV35IfClockRate_Type.__name__=_E
_JuniV35IfClockRate_Object=MibTableColumn
juniV35IfClockRate=_JuniV35IfClockRate_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,4),_JuniV35IfClockRate_Type())
juniV35IfClockRate.setMaxAccess(_D)
if mibBuilder.loadTexts:juniV35IfClockRate.setStatus(_A)
if mibBuilder.loadTexts:juniV35IfClockRate.setUnits('hertz')
class _JuniV35IfNrzEncoding_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_JuniV35IfNrzEncoding_Type.__name__=_C
_JuniV35IfNrzEncoding_Object=MibTableColumn
juniV35IfNrzEncoding=_JuniV35IfNrzEncoding_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,5),_JuniV35IfNrzEncoding_Type())
juniV35IfNrzEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:juniV35IfNrzEncoding.setStatus(_A)
class _JuniV35IfTxClock_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_JuniV35IfTxClock_Type.__name__=_C
_JuniV35IfTxClock_Object=MibTableColumn
juniV35IfTxClock=_JuniV35IfTxClock_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,6),_JuniV35IfTxClock_Type())
juniV35IfTxClock.setMaxAccess(_D)
if mibBuilder.loadTexts:juniV35IfTxClock.setStatus(_A)
class _JuniV35IfIgnoreDcd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ignoredNone',0),('dcdIgnored',1),('linkStateIgnored',2)))
_JuniV35IfIgnoreDcd_Type.__name__=_C
_JuniV35IfIgnoreDcd_Object=MibTableColumn
juniV35IfIgnoreDcd=_JuniV35IfIgnoreDcd_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,7),_JuniV35IfIgnoreDcd_Type())
juniV35IfIgnoreDcd.setMaxAccess(_D)
if mibBuilder.loadTexts:juniV35IfIgnoreDcd.setStatus(_A)
class _JuniV35IfLoopback_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('loopback',1)))
_JuniV35IfLoopback_Type.__name__=_C
_JuniV35IfLoopback_Object=MibTableColumn
juniV35IfLoopback=_JuniV35IfLoopback_Object((1,3,6,1,4,1,4874,2,2,59,1,2,1,8),_JuniV35IfLoopback_Type())
juniV35IfLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:juniV35IfLoopback.setStatus(_A)
_JuniV35Conformance_ObjectIdentity=ObjectIdentity
juniV35Conformance=_JuniV35Conformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,59,4))
_JuniV35Compliances_ObjectIdentity=ObjectIdentity
juniV35Compliances=_JuniV35Compliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,59,4,1))
_JuniV35Groups_ObjectIdentity=ObjectIdentity
juniV35Groups=_JuniV35Groups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,59,4,2))
juniV35Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,59,4,2,1))
juniV35Group.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:juniV35Group.setStatus(_A)
juniV35Compliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,59,4,1,1))
juniV35Compliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:juniV35Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniV35MIB':juniV35MIB,'juniV35Objects':juniV35Objects,'juniV35IfTable':juniV35IfTable,'juniV35IfEntry':juniV35IfEntry,_F:juniV35IfIndex,_J:juniV35IfType,_K:juniV35IfMode,_L:juniV35IfClockRate,_M:juniV35IfNrzEncoding,_N:juniV35IfTxClock,_O:juniV35IfIgnoreDcd,_P:juniV35IfLoopback,'juniV35Conformance':juniV35Conformance,'juniV35Compliances':juniV35Compliances,'juniV35Compliance':juniV35Compliance,'juniV35Groups':juniV35Groups,_Q:juniV35Group})