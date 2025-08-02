_b='ntcDvbModAesConfGrpV1Standard'
_a='ntcDvbModAesCfgAesStrOdd'
_Z='ntcDvbModAesCfgAesStrEven'
_Y='ntcDvbModAesCfgAesStrEncOdd'
_X='ntcDvbModAesCfgAesStrEncEven'
_W='ntcDvbModAesCfgAesStrKeyPar'
_V='ntcDvbModAesCfgAesStrIsi'
_U='ntcDvbModAesCfgAesStrEnable'
_T='ntcDvbModAesCfgAesStrRowStatus'
_S='ntcDvbModAesCfgAesGloOdd'
_R='ntcDvbModAesCfgAesGloEven'
_Q='ntcDvbModAesCfgAesGloEncOdd'
_P='ntcDvbModAesCfgAesGloEncEven'
_O='ntcDvbModAesCfgAesGloKeyPar'
_N='ntcDvbModAesCfgAesClearKeys'
_M='ntcDvbModAesCfgAesGroupKey'
_L='ntcDvbModAesCfgAesKeyStrength'
_K='ntcDvbModAesCfgAesGlobEncr'
_J='ntcDvbModAesCfgAesEnable'
_I='ntcDvbModAesCfgAesStrName'
_H='NtcEnable'
_G='**********'
_F='Integer32'
_E='read-create'
_D='read-write'
_C='DisplayString'
_B='NEWTEC-MODULATORAES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
ntcDvbModulatorAes=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1010))
if mibBuilder.loadTexts:ntcDvbModulatorAes.setRevisions(('2018-02-02 09:00','2016-10-24 12:00'))
_NtcDvbModAesObjects_ObjectIdentity=ObjectIdentity
ntcDvbModAesObjects=_NtcDvbModAesObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,1))
if mibBuilder.loadTexts:ntcDvbModAesObjects.setStatus(_A)
_NtcDvbModAesCfgAes_ObjectIdentity=ObjectIdentity
ntcDvbModAesCfgAes=_NtcDvbModAesCfgAes_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,1,1))
if mibBuilder.loadTexts:ntcDvbModAesCfgAes.setStatus(_A)
class _NtcDvbModAesCfgAesEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcDvbModAesCfgAesEnable_Type.__name__=_F
_NtcDvbModAesCfgAesEnable_Object=MibScalar
ntcDvbModAesCfgAesEnable=_NtcDvbModAesCfgAesEnable_Object((1,3,6,1,4,1,5835,5,2,1010,1,1,1),_NtcDvbModAesCfgAesEnable_Type())
ntcDvbModAesCfgAesEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesEnable.setStatus(_A)
class _NtcDvbModAesCfgAesGlobEncr_Type(NtcEnable):defaultValue=1
_NtcDvbModAesCfgAesGlobEncr_Type.__name__=_H
_NtcDvbModAesCfgAesGlobEncr_Object=MibScalar
ntcDvbModAesCfgAesGlobEncr=_NtcDvbModAesCfgAesGlobEncr_Object((1,3,6,1,4,1,5835,5,2,1010,1,1,2),_NtcDvbModAesCfgAesGlobEncr_Type())
ntcDvbModAesCfgAesGlobEncr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGlobEncr.setStatus(_A)
class _NtcDvbModAesCfgAesKeyStrength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('aes64',0),('aes128',1),('aes256',2)))
_NtcDvbModAesCfgAesKeyStrength_Type.__name__=_F
_NtcDvbModAesCfgAesKeyStrength_Object=MibScalar
ntcDvbModAesCfgAesKeyStrength=_NtcDvbModAesCfgAesKeyStrength_Object((1,3,6,1,4,1,5835,5,2,1010,1,1,3),_NtcDvbModAesCfgAesKeyStrength_Type())
ntcDvbModAesCfgAesKeyStrength.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesKeyStrength.setStatus(_A)
class _NtcDvbModAesCfgAesGroupKey_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesGroupKey_Type.__name__=_C
_NtcDvbModAesCfgAesGroupKey_Object=MibScalar
ntcDvbModAesCfgAesGroupKey=_NtcDvbModAesCfgAesGroupKey_Object((1,3,6,1,4,1,5835,5,2,1010,1,1,4),_NtcDvbModAesCfgAesGroupKey_Type())
ntcDvbModAesCfgAesGroupKey.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGroupKey.setStatus(_A)
class _NtcDvbModAesCfgAesClearKeys_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('donothing',0),('clearkeys',1)))
_NtcDvbModAesCfgAesClearKeys_Type.__name__=_F
_NtcDvbModAesCfgAesClearKeys_Object=MibScalar
ntcDvbModAesCfgAesClearKeys=_NtcDvbModAesCfgAesClearKeys_Object((1,3,6,1,4,1,5835,5,2,1010,1,1,5),_NtcDvbModAesCfgAesClearKeys_Type())
ntcDvbModAesCfgAesClearKeys.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesClearKeys.setStatus(_A)
_NtcDvbModAesCfgAesGlo_ObjectIdentity=ObjectIdentity
ntcDvbModAesCfgAesGlo=_NtcDvbModAesCfgAesGlo_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,1,2))
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGlo.setStatus(_A)
class _NtcDvbModAesCfgAesGloKeyPar_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('even',0),('odd',1)))
_NtcDvbModAesCfgAesGloKeyPar_Type.__name__=_F
_NtcDvbModAesCfgAesGloKeyPar_Object=MibScalar
ntcDvbModAesCfgAesGloKeyPar=_NtcDvbModAesCfgAesGloKeyPar_Object((1,3,6,1,4,1,5835,5,2,1010,1,2,1),_NtcDvbModAesCfgAesGloKeyPar_Type())
ntcDvbModAesCfgAesGloKeyPar.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGloKeyPar.setStatus(_A)
class _NtcDvbModAesCfgAesGloEncEven_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesGloEncEven_Type.__name__=_C
_NtcDvbModAesCfgAesGloEncEven_Object=MibScalar
ntcDvbModAesCfgAesGloEncEven=_NtcDvbModAesCfgAesGloEncEven_Object((1,3,6,1,4,1,5835,5,2,1010,1,2,2),_NtcDvbModAesCfgAesGloEncEven_Type())
ntcDvbModAesCfgAesGloEncEven.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGloEncEven.setStatus(_A)
class _NtcDvbModAesCfgAesGloEncOdd_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesGloEncOdd_Type.__name__=_C
_NtcDvbModAesCfgAesGloEncOdd_Object=MibScalar
ntcDvbModAesCfgAesGloEncOdd=_NtcDvbModAesCfgAesGloEncOdd_Object((1,3,6,1,4,1,5835,5,2,1010,1,2,3),_NtcDvbModAesCfgAesGloEncOdd_Type())
ntcDvbModAesCfgAesGloEncOdd.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGloEncOdd.setStatus(_A)
class _NtcDvbModAesCfgAesGloEven_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesGloEven_Type.__name__=_C
_NtcDvbModAesCfgAesGloEven_Object=MibScalar
ntcDvbModAesCfgAesGloEven=_NtcDvbModAesCfgAesGloEven_Object((1,3,6,1,4,1,5835,5,2,1010,1,2,4),_NtcDvbModAesCfgAesGloEven_Type())
ntcDvbModAesCfgAesGloEven.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGloEven.setStatus(_A)
class _NtcDvbModAesCfgAesGloOdd_Type(DisplayString):defaultValue=OctetString(_G);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesGloOdd_Type.__name__=_C
_NtcDvbModAesCfgAesGloOdd_Object=MibScalar
ntcDvbModAesCfgAesGloOdd=_NtcDvbModAesCfgAesGloOdd_Object((1,3,6,1,4,1,5835,5,2,1010,1,2,5),_NtcDvbModAesCfgAesGloOdd_Type())
ntcDvbModAesCfgAesGloOdd.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesGloOdd.setStatus(_A)
_NtcDvbModAesCfgAesStrTable_Object=MibTable
ntcDvbModAesCfgAesStrTable=_NtcDvbModAesCfgAesStrTable_Object((1,3,6,1,4,1,5835,5,2,1010,1,3))
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrTable.setStatus(_A)
_NtcDvbModAesCfgAesStrEntry_Object=MibTableRow
ntcDvbModAesCfgAesStrEntry=_NtcDvbModAesCfgAesStrEntry_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1))
ntcDvbModAesCfgAesStrEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrEntry.setStatus(_A)
class _NtcDvbModAesCfgAesStrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcDvbModAesCfgAesStrName_Type.__name__=_C
_NtcDvbModAesCfgAesStrName_Object=MibTableColumn
ntcDvbModAesCfgAesStrName=_NtcDvbModAesCfgAesStrName_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,1),_NtcDvbModAesCfgAesStrName_Type())
ntcDvbModAesCfgAesStrName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrName.setStatus(_A)
_NtcDvbModAesCfgAesStrRowStatus_Type=RowStatus
_NtcDvbModAesCfgAesStrRowStatus_Object=MibTableColumn
ntcDvbModAesCfgAesStrRowStatus=_NtcDvbModAesCfgAesStrRowStatus_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,2),_NtcDvbModAesCfgAesStrRowStatus_Type())
ntcDvbModAesCfgAesStrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrRowStatus.setStatus(_A)
class _NtcDvbModAesCfgAesStrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcDvbModAesCfgAesStrEnable_Type.__name__=_F
_NtcDvbModAesCfgAesStrEnable_Object=MibTableColumn
ntcDvbModAesCfgAesStrEnable=_NtcDvbModAesCfgAesStrEnable_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,3),_NtcDvbModAesCfgAesStrEnable_Type())
ntcDvbModAesCfgAesStrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrEnable.setStatus(_A)
_NtcDvbModAesCfgAesStrIsi_Type=Unsigned32
_NtcDvbModAesCfgAesStrIsi_Object=MibTableColumn
ntcDvbModAesCfgAesStrIsi=_NtcDvbModAesCfgAesStrIsi_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,4),_NtcDvbModAesCfgAesStrIsi_Type())
ntcDvbModAesCfgAesStrIsi.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrIsi.setStatus(_A)
class _NtcDvbModAesCfgAesStrKeyPar_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('even',0),('odd',1)))
_NtcDvbModAesCfgAesStrKeyPar_Type.__name__=_F
_NtcDvbModAesCfgAesStrKeyPar_Object=MibTableColumn
ntcDvbModAesCfgAesStrKeyPar=_NtcDvbModAesCfgAesStrKeyPar_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,5),_NtcDvbModAesCfgAesStrKeyPar_Type())
ntcDvbModAesCfgAesStrKeyPar.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrKeyPar.setStatus(_A)
class _NtcDvbModAesCfgAesStrEncEven_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesStrEncEven_Type.__name__=_C
_NtcDvbModAesCfgAesStrEncEven_Object=MibTableColumn
ntcDvbModAesCfgAesStrEncEven=_NtcDvbModAesCfgAesStrEncEven_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,6),_NtcDvbModAesCfgAesStrEncEven_Type())
ntcDvbModAesCfgAesStrEncEven.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrEncEven.setStatus(_A)
class _NtcDvbModAesCfgAesStrEncOdd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesStrEncOdd_Type.__name__=_C
_NtcDvbModAesCfgAesStrEncOdd_Object=MibTableColumn
ntcDvbModAesCfgAesStrEncOdd=_NtcDvbModAesCfgAesStrEncOdd_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,7),_NtcDvbModAesCfgAesStrEncOdd_Type())
ntcDvbModAesCfgAesStrEncOdd.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrEncOdd.setStatus(_A)
class _NtcDvbModAesCfgAesStrEven_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesStrEven_Type.__name__=_C
_NtcDvbModAesCfgAesStrEven_Object=MibTableColumn
ntcDvbModAesCfgAesStrEven=_NtcDvbModAesCfgAesStrEven_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,8),_NtcDvbModAesCfgAesStrEven_Type())
ntcDvbModAesCfgAesStrEven.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrEven.setStatus(_A)
class _NtcDvbModAesCfgAesStrOdd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,64))
_NtcDvbModAesCfgAesStrOdd_Type.__name__=_C
_NtcDvbModAesCfgAesStrOdd_Object=MibTableColumn
ntcDvbModAesCfgAesStrOdd=_NtcDvbModAesCfgAesStrOdd_Object((1,3,6,1,4,1,5835,5,2,1010,1,3,1,9),_NtcDvbModAesCfgAesStrOdd_Type())
ntcDvbModAesCfgAesStrOdd.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcDvbModAesCfgAesStrOdd.setStatus(_A)
_NtcDvbModAesConformance_ObjectIdentity=ObjectIdentity
ntcDvbModAesConformance=_NtcDvbModAesConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,2))
if mibBuilder.loadTexts:ntcDvbModAesConformance.setStatus(_A)
_NtcDvbModAesConfCompliance_ObjectIdentity=ObjectIdentity
ntcDvbModAesConfCompliance=_NtcDvbModAesConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,2,1))
if mibBuilder.loadTexts:ntcDvbModAesConfCompliance.setStatus(_A)
_NtcDvbModAesConfGroup_ObjectIdentity=ObjectIdentity
ntcDvbModAesConfGroup=_NtcDvbModAesConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1010,2,2))
if mibBuilder.loadTexts:ntcDvbModAesConfGroup.setStatus(_A)
ntcDvbModAesConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1010,2,2,1))
ntcDvbModAesConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ntcDvbModAesConfGrpV1Standard.setStatus(_A)
ntcDvbModAesConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1010,2,1,1))
ntcDvbModAesConfCompV1Standard.setObjects((_B,_b))
if mibBuilder.loadTexts:ntcDvbModAesConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcDvbModulatorAes':ntcDvbModulatorAes,'ntcDvbModAesObjects':ntcDvbModAesObjects,'ntcDvbModAesCfgAes':ntcDvbModAesCfgAes,_J:ntcDvbModAesCfgAesEnable,_K:ntcDvbModAesCfgAesGlobEncr,_L:ntcDvbModAesCfgAesKeyStrength,_M:ntcDvbModAesCfgAesGroupKey,_N:ntcDvbModAesCfgAesClearKeys,'ntcDvbModAesCfgAesGlo':ntcDvbModAesCfgAesGlo,_O:ntcDvbModAesCfgAesGloKeyPar,_P:ntcDvbModAesCfgAesGloEncEven,_Q:ntcDvbModAesCfgAesGloEncOdd,_R:ntcDvbModAesCfgAesGloEven,_S:ntcDvbModAesCfgAesGloOdd,'ntcDvbModAesCfgAesStrTable':ntcDvbModAesCfgAesStrTable,'ntcDvbModAesCfgAesStrEntry':ntcDvbModAesCfgAesStrEntry,_I:ntcDvbModAesCfgAesStrName,_T:ntcDvbModAesCfgAesStrRowStatus,_U:ntcDvbModAesCfgAesStrEnable,_V:ntcDvbModAesCfgAesStrIsi,_W:ntcDvbModAesCfgAesStrKeyPar,_X:ntcDvbModAesCfgAesStrEncEven,_Y:ntcDvbModAesCfgAesStrEncOdd,_Z:ntcDvbModAesCfgAesStrEven,_a:ntcDvbModAesCfgAesStrOdd,'ntcDvbModAesConformance':ntcDvbModAesConformance,'ntcDvbModAesConfCompliance':ntcDvbModAesConfCompliance,'ntcDvbModAesConfCompV1Standard':ntcDvbModAesConfCompV1Standard,'ntcDvbModAesConfGroup':ntcDvbModAesConfGroup,_b:ntcDvbModAesConfGrpV1Standard})