_H='zxAnEmSlot'
_G='zxAnEmShelf'
_F='zxAnEmRack'
_E='not-accessible'
_D='read-write'
_C='ZTE-AN-VOICE-TRUNK-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoiceTrunkMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_MsagmajorVersion_ObjectIdentity=ObjectIdentity
msagmajorVersion=_MsagmajorVersion_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_MsagEmConfig_ObjectIdentity=ObjectIdentity
msagEmConfig=_MsagEmConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,11))
_ZxAnEmCfgTable_Object=MibTable
zxAnEmCfgTable=_ZxAnEmCfgTable_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1))
if mibBuilder.loadTexts:zxAnEmCfgTable.setStatus(_A)
_ZxAnEmCfgEntry_Object=MibTableRow
zxAnEmCfgEntry=_ZxAnEmCfgEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1))
zxAnEmCfgEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:zxAnEmCfgEntry.setStatus(_A)
class _ZxAnEmRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnEmRack_Type.__name__=_B
_ZxAnEmRack_Object=MibTableColumn
zxAnEmRack=_ZxAnEmRack_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,1),_ZxAnEmRack_Type())
zxAnEmRack.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnEmRack.setStatus(_A)
class _ZxAnEmShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZxAnEmShelf_Type.__name__=_B
_ZxAnEmShelf_Object=MibTableColumn
zxAnEmShelf=_ZxAnEmShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,2),_ZxAnEmShelf_Type())
zxAnEmShelf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnEmShelf.setStatus(_A)
class _ZxAnEmSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_ZxAnEmSlot_Type.__name__=_B
_ZxAnEmSlot_Object=MibTableColumn
zxAnEmSlot=_ZxAnEmSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,3),_ZxAnEmSlot_Type())
zxAnEmSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnEmSlot.setStatus(_A)
class _ZxAnEmAudioIfType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('twoWire',2),('fourWire',4)))
_ZxAnEmAudioIfType_Type.__name__=_B
_ZxAnEmAudioIfType_Object=MibTableColumn
zxAnEmAudioIfType=_ZxAnEmAudioIfType_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,4),_ZxAnEmAudioIfType_Type())
zxAnEmAudioIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEmAudioIfType.setStatus(_A)
class _ZxAnEmIfType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('emTypeI',1),('emTypeV',5)))
_ZxAnEmIfType_Type.__name__=_B
_ZxAnEmIfType_Object=MibTableColumn
zxAnEmIfType=_ZxAnEmIfType_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,5),_ZxAnEmIfType_Type())
zxAnEmIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEmIfType.setStatus(_A)
class _ZxAnEmOutGain_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnEmOutGain_Type.__name__=_B
_ZxAnEmOutGain_Object=MibTableColumn
zxAnEmOutGain=_ZxAnEmOutGain_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,6),_ZxAnEmOutGain_Type())
zxAnEmOutGain.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEmOutGain.setStatus(_A)
class _ZxAnEmInGain_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ZxAnEmInGain_Type.__name__=_B
_ZxAnEmInGain_Object=MibTableColumn
zxAnEmInGain=_ZxAnEmInGain_Object((1,3,6,1,4,1,3902,1015,5200,3,11,1,1,7),_ZxAnEmInGain_Type())
zxAnEmInGain.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnEmInGain.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zte':zte,'zxAn':zxAn,'zxAnVoiceTrunkMib':zxAnVoiceTrunkMib,'msagmajorVersion':msagmajorVersion,'msagEmConfig':msagEmConfig,'zxAnEmCfgTable':zxAnEmCfgTable,'zxAnEmCfgEntry':zxAnEmCfgEntry,_F:zxAnEmRack,_G:zxAnEmShelf,_H:zxAnEmSlot,'zxAnEmAudioIfType':zxAnEmAudioIfType,'zxAnEmIfType':zxAnEmIfType,'zxAnEmOutGain':zxAnEmOutGain,'zxAnEmInGain':zxAnEmInGain})