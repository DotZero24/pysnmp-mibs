_e='digitMapTimeoutVer1'
_d='digitMapRefusedVer1'
_c='digitMapAllowedVer1'
_b='digitMapTimeoutInterDigit'
_a='digitMapTimeoutFirstDigit'
_Z='digitMapTimeoutCompletion'
_Y='digitMapRefusedLineToApply'
_X='digitMapRefusedIsValid'
_W='digitMapRefusedDigitMap'
_V='digitMapRefusedEnable'
_U='digitMapAllowedLineToApply'
_T='digitMapSuffixStringToRemove'
_S='digitMapPrependedString'
_R='digitMapPrefixedDigitRemovalCount'
_Q='digitMapAllowedIsValid'
_P='digitMapAllowedDigitMap'
_O='digitMapAllowedEnable'
_N='deprecated'
_M='invalid'
_L='enable'
_K='disable'
_J='MxEnableState'
_I='digitMapRefusedIndex'
_H='digitMapAllowedIndex'
_G='read-only'
_F='Integer32'
_E='Unsigned32'
_D='OctetString'
_C='read-write'
_B='MX-DIGIT-MAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
digitMapMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,55))
if mibBuilder.loadTexts:digitMapMIB.setRevisions(('2009-10-14 00:00','2008-10-16 00:00','2008-08-25 00:00','2004-11-01 00:00','2003-02-24 00:00','2003-02-17 00:00','2002-11-21 00:00'))
_DigitMapMIBObjects_ObjectIdentity=ObjectIdentity
digitMapMIBObjects=_DigitMapMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,55,1))
class _DigitMapProcessDigitsWhenPressed_Type(MxEnableState):defaultValue=1
_DigitMapProcessDigitsWhenPressed_Type.__name__=_J
_DigitMapProcessDigitsWhenPressed_Object=MibScalar
digitMapProcessDigitsWhenPressed=_DigitMapProcessDigitsWhenPressed_Object((1,3,6,1,4,1,4935,15,55,1,1),_DigitMapProcessDigitsWhenPressed_Type())
digitMapProcessDigitsWhenPressed.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapProcessDigitsWhenPressed.setStatus(_A)
_DigitMapAllowedTable_Object=MibTable
digitMapAllowedTable=_DigitMapAllowedTable_Object((1,3,6,1,4,1,4935,15,55,1,10))
if mibBuilder.loadTexts:digitMapAllowedTable.setStatus(_A)
_DigitMapAllowedEntry_Object=MibTableRow
digitMapAllowedEntry=_DigitMapAllowedEntry_Object((1,3,6,1,4,1,4935,15,55,1,10,1))
digitMapAllowedEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:digitMapAllowedEntry.setStatus(_A)
class _DigitMapAllowedIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_DigitMapAllowedIndex_Type.__name__=_E
_DigitMapAllowedIndex_Object=MibTableColumn
digitMapAllowedIndex=_DigitMapAllowedIndex_Object((1,3,6,1,4,1,4935,15,55,1,10,1,5),_DigitMapAllowedIndex_Type())
digitMapAllowedIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:digitMapAllowedIndex.setStatus(_A)
class _DigitMapAllowedEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DigitMapAllowedEnable_Type.__name__=_F
_DigitMapAllowedEnable_Object=MibTableColumn
digitMapAllowedEnable=_DigitMapAllowedEnable_Object((1,3,6,1,4,1,4935,15,55,1,10,1,10),_DigitMapAllowedEnable_Type())
digitMapAllowedEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapAllowedEnable.setStatus(_A)
class _DigitMapAllowedDigitMap_Type(OctetString):defaultValue=OctetString('x.T');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_DigitMapAllowedDigitMap_Type.__name__=_D
_DigitMapAllowedDigitMap_Object=MibTableColumn
digitMapAllowedDigitMap=_DigitMapAllowedDigitMap_Object((1,3,6,1,4,1,4935,15,55,1,10,1,15),_DigitMapAllowedDigitMap_Type())
digitMapAllowedDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapAllowedDigitMap.setStatus(_A)
class _DigitMapAllowedIsValid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('valid',1)))
_DigitMapAllowedIsValid_Type.__name__=_F
_DigitMapAllowedIsValid_Object=MibTableColumn
digitMapAllowedIsValid=_DigitMapAllowedIsValid_Object((1,3,6,1,4,1,4935,15,55,1,10,1,20),_DigitMapAllowedIsValid_Type())
digitMapAllowedIsValid.setMaxAccess(_G)
if mibBuilder.loadTexts:digitMapAllowedIsValid.setStatus(_N)
class _DigitMapPrefixedDigitRemovalCount_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_DigitMapPrefixedDigitRemovalCount_Type.__name__=_E
_DigitMapPrefixedDigitRemovalCount_Object=MibTableColumn
digitMapPrefixedDigitRemovalCount=_DigitMapPrefixedDigitRemovalCount_Object((1,3,6,1,4,1,4935,15,55,1,10,1,25),_DigitMapPrefixedDigitRemovalCount_Type())
digitMapPrefixedDigitRemovalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapPrefixedDigitRemovalCount.setStatus(_A)
class _DigitMapPrependedString_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DigitMapPrependedString_Type.__name__=_D
_DigitMapPrependedString_Object=MibTableColumn
digitMapPrependedString=_DigitMapPrependedString_Object((1,3,6,1,4,1,4935,15,55,1,10,1,30),_DigitMapPrependedString_Type())
digitMapPrependedString.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapPrependedString.setStatus(_A)
class _DigitMapSuffixStringToRemove_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_DigitMapSuffixStringToRemove_Type.__name__=_D
_DigitMapSuffixStringToRemove_Object=MibTableColumn
digitMapSuffixStringToRemove=_DigitMapSuffixStringToRemove_Object((1,3,6,1,4,1,4935,15,55,1,10,1,35),_DigitMapSuffixStringToRemove_Type())
digitMapSuffixStringToRemove.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapSuffixStringToRemove.setStatus(_A)
class _DigitMapAllowedLineToApply_Type(OctetString):defaultValue=OctetString('all');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DigitMapAllowedLineToApply_Type.__name__=_D
_DigitMapAllowedLineToApply_Object=MibTableColumn
digitMapAllowedLineToApply=_DigitMapAllowedLineToApply_Object((1,3,6,1,4,1,4935,15,55,1,10,1,50),_DigitMapAllowedLineToApply_Type())
digitMapAllowedLineToApply.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapAllowedLineToApply.setStatus(_A)
_DigitMapRefusedTable_Object=MibTable
digitMapRefusedTable=_DigitMapRefusedTable_Object((1,3,6,1,4,1,4935,15,55,1,20))
if mibBuilder.loadTexts:digitMapRefusedTable.setStatus(_A)
_DigitMapRefusedEntry_Object=MibTableRow
digitMapRefusedEntry=_DigitMapRefusedEntry_Object((1,3,6,1,4,1,4935,15,55,1,20,1))
digitMapRefusedEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:digitMapRefusedEntry.setStatus(_A)
class _DigitMapRefusedIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_DigitMapRefusedIndex_Type.__name__=_E
_DigitMapRefusedIndex_Object=MibTableColumn
digitMapRefusedIndex=_DigitMapRefusedIndex_Object((1,3,6,1,4,1,4935,15,55,1,20,1,5),_DigitMapRefusedIndex_Type())
digitMapRefusedIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:digitMapRefusedIndex.setStatus(_A)
class _DigitMapRefusedEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_DigitMapRefusedEnable_Type.__name__=_F
_DigitMapRefusedEnable_Object=MibTableColumn
digitMapRefusedEnable=_DigitMapRefusedEnable_Object((1,3,6,1,4,1,4935,15,55,1,20,1,10),_DigitMapRefusedEnable_Type())
digitMapRefusedEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapRefusedEnable.setStatus(_A)
class _DigitMapRefusedDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_DigitMapRefusedDigitMap_Type.__name__=_D
_DigitMapRefusedDigitMap_Object=MibTableColumn
digitMapRefusedDigitMap=_DigitMapRefusedDigitMap_Object((1,3,6,1,4,1,4935,15,55,1,20,1,15),_DigitMapRefusedDigitMap_Type())
digitMapRefusedDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapRefusedDigitMap.setStatus(_A)
class _DigitMapRefusedIsValid_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),('valid',1)))
_DigitMapRefusedIsValid_Type.__name__=_F
_DigitMapRefusedIsValid_Object=MibTableColumn
digitMapRefusedIsValid=_DigitMapRefusedIsValid_Object((1,3,6,1,4,1,4935,15,55,1,20,1,20),_DigitMapRefusedIsValid_Type())
digitMapRefusedIsValid.setMaxAccess(_G)
if mibBuilder.loadTexts:digitMapRefusedIsValid.setStatus(_N)
class _DigitMapRefusedLineToApply_Type(OctetString):defaultValue=OctetString('all');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DigitMapRefusedLineToApply_Type.__name__=_D
_DigitMapRefusedLineToApply_Object=MibTableColumn
digitMapRefusedLineToApply=_DigitMapRefusedLineToApply_Object((1,3,6,1,4,1,4935,15,55,1,20,1,50),_DigitMapRefusedLineToApply_Type())
digitMapRefusedLineToApply.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapRefusedLineToApply.setStatus(_A)
_DigitMapTimeouts_ObjectIdentity=ObjectIdentity
digitMapTimeouts=_DigitMapTimeouts_ObjectIdentity((1,3,6,1,4,1,4935,15,55,1,30))
class _DigitMapTimeoutCompletion_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_DigitMapTimeoutCompletion_Type.__name__=_E
_DigitMapTimeoutCompletion_Object=MibScalar
digitMapTimeoutCompletion=_DigitMapTimeoutCompletion_Object((1,3,6,1,4,1,4935,15,55,1,30,5),_DigitMapTimeoutCompletion_Type())
digitMapTimeoutCompletion.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapTimeoutCompletion.setStatus(_A)
class _DigitMapTimeoutFirstDigit_Type(Unsigned32):defaultValue=20000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,180000))
_DigitMapTimeoutFirstDigit_Type.__name__=_E
_DigitMapTimeoutFirstDigit_Object=MibScalar
digitMapTimeoutFirstDigit=_DigitMapTimeoutFirstDigit_Object((1,3,6,1,4,1,4935,15,55,1,30,10),_DigitMapTimeoutFirstDigit_Type())
digitMapTimeoutFirstDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapTimeoutFirstDigit.setStatus(_A)
class _DigitMapTimeoutInterDigit_Type(Unsigned32):defaultValue=4000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,10000))
_DigitMapTimeoutInterDigit_Type.__name__=_E
_DigitMapTimeoutInterDigit_Object=MibScalar
digitMapTimeoutInterDigit=_DigitMapTimeoutInterDigit_Object((1,3,6,1,4,1,4935,15,55,1,30,15),_DigitMapTimeoutInterDigit_Type())
digitMapTimeoutInterDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:digitMapTimeoutInterDigit.setStatus(_A)
_DigitMapConformance_ObjectIdentity=ObjectIdentity
digitMapConformance=_DigitMapConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,55,2))
_DigitMapCompliances_ObjectIdentity=ObjectIdentity
digitMapCompliances=_DigitMapCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,55,2,1))
_DigitMapGroups_ObjectIdentity=ObjectIdentity
digitMapGroups=_DigitMapGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,55,2,2))
digitMapAllowedVer1=ObjectGroup((1,3,6,1,4,1,4935,15,55,2,2,1))
digitMapAllowedVer1.setObjects(*((_B,_H),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:digitMapAllowedVer1.setStatus(_A)
digitMapRefusedVer1=ObjectGroup((1,3,6,1,4,1,4935,15,55,2,2,2))
digitMapRefusedVer1.setObjects(*((_B,_I),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:digitMapRefusedVer1.setStatus(_A)
digitMapTimeoutVer1=ObjectGroup((1,3,6,1,4,1,4935,15,55,2,2,3))
digitMapTimeoutVer1.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:digitMapTimeoutVer1.setStatus(_A)
digitMapComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,55,2,1,1))
digitMapComplVer1.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:digitMapComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'digitMapMIB':digitMapMIB,'digitMapMIBObjects':digitMapMIBObjects,'digitMapProcessDigitsWhenPressed':digitMapProcessDigitsWhenPressed,'digitMapAllowedTable':digitMapAllowedTable,'digitMapAllowedEntry':digitMapAllowedEntry,_H:digitMapAllowedIndex,_O:digitMapAllowedEnable,_P:digitMapAllowedDigitMap,_Q:digitMapAllowedIsValid,_R:digitMapPrefixedDigitRemovalCount,_S:digitMapPrependedString,_T:digitMapSuffixStringToRemove,_U:digitMapAllowedLineToApply,'digitMapRefusedTable':digitMapRefusedTable,'digitMapRefusedEntry':digitMapRefusedEntry,_I:digitMapRefusedIndex,_V:digitMapRefusedEnable,_W:digitMapRefusedDigitMap,_X:digitMapRefusedIsValid,_Y:digitMapRefusedLineToApply,'digitMapTimeouts':digitMapTimeouts,_Z:digitMapTimeoutCompletion,_a:digitMapTimeoutFirstDigit,_b:digitMapTimeoutInterDigit,'digitMapConformance':digitMapConformance,'digitMapCompliances':digitMapCompliances,'digitMapComplVer1':digitMapComplVer1,'digitMapGroups':digitMapGroups,_c:digitMapAllowedVer1,_d:digitMapRefusedVer1,_e:digitMapTimeoutVer1})