_H='not-accessible'
_G='nbsJumperIndex'
_F='nbsJumperIfIndex'
_E='Integer32'
_D='NBS-JUMPER-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nbsJumperMib=ModuleIdentity((1,3,6,1,4,1,629,210))
_NbsJumperGrp_ObjectIdentity=ObjectIdentity
nbsJumperGrp=_NbsJumperGrp_ObjectIdentity((1,3,6,1,4,1,629,210,1))
if mibBuilder.loadTexts:nbsJumperGrp.setStatus(_A)
_NbsJumperTableSize_Type=Unsigned32
_NbsJumperTableSize_Object=MibScalar
nbsJumperTableSize=_NbsJumperTableSize_Object((1,3,6,1,4,1,629,210,1,1),_NbsJumperTableSize_Type())
nbsJumperTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsJumperTableSize.setStatus(_A)
_NbsJumperTable_Object=MibTable
nbsJumperTable=_NbsJumperTable_Object((1,3,6,1,4,1,629,210,1,2))
if mibBuilder.loadTexts:nbsJumperTable.setStatus(_A)
_NbsJumperEntry_Object=MibTableRow
nbsJumperEntry=_NbsJumperEntry_Object((1,3,6,1,4,1,629,210,1,2,1))
nbsJumperEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:nbsJumperEntry.setStatus(_A)
_NbsJumperIfIndex_Type=InterfaceIndex
_NbsJumperIfIndex_Object=MibTableColumn
nbsJumperIfIndex=_NbsJumperIfIndex_Object((1,3,6,1,4,1,629,210,1,2,1,1),_NbsJumperIfIndex_Type())
nbsJumperIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsJumperIfIndex.setStatus(_A)
_NbsJumperIndex_Type=Integer32
_NbsJumperIndex_Object=MibTableColumn
nbsJumperIndex=_NbsJumperIndex_Object((1,3,6,1,4,1,629,210,1,2,1,2),_NbsJumperIndex_Type())
nbsJumperIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsJumperIndex.setStatus(_A)
class _NbsJumperPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('off',2),('on',3)))
_NbsJumperPosition_Type.__name__=_E
_NbsJumperPosition_Object=MibTableColumn
nbsJumperPosition=_NbsJumperPosition_Object((1,3,6,1,4,1,629,210,1,2,1,3),_NbsJumperPosition_Type())
nbsJumperPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsJumperPosition.setStatus(_A)
class _NbsJumperInterpret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NbsJumperInterpret_Type.__name__=_C
_NbsJumperInterpret_Object=MibTableColumn
nbsJumperInterpret=_NbsJumperInterpret_Object((1,3,6,1,4,1,629,210,1,2,1,4),_NbsJumperInterpret_Type())
nbsJumperInterpret.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsJumperInterpret.setStatus(_A)
class _NbsJumperSilkScreen_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_NbsJumperSilkScreen_Type.__name__=_C
_NbsJumperSilkScreen_Object=MibTableColumn
nbsJumperSilkScreen=_NbsJumperSilkScreen_Object((1,3,6,1,4,1,629,210,1,2,1,5),_NbsJumperSilkScreen_Type())
nbsJumperSilkScreen.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsJumperSilkScreen.setStatus(_A)
class _NbsJumperDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsJumperDescription_Type.__name__=_C
_NbsJumperDescription_Object=MibTableColumn
nbsJumperDescription=_NbsJumperDescription_Object((1,3,6,1,4,1,629,210,1,2,1,6),_NbsJumperDescription_Type())
nbsJumperDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsJumperDescription.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsJumperMib':nbsJumperMib,'nbsJumperGrp':nbsJumperGrp,'nbsJumperTableSize':nbsJumperTableSize,'nbsJumperTable':nbsJumperTable,'nbsJumperEntry':nbsJumperEntry,_F:nbsJumperIfIndex,_G:nbsJumperIndex,'nbsJumperPosition':nbsJumperPosition,'nbsJumperInterpret':nbsJumperInterpret,'nbsJumperSilkScreen':nbsJumperSilkScreen,'nbsJumperDescription':nbsJumperDescription})