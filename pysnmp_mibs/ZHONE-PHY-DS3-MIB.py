_I='dsx3ConfigExtAtmFraming'
_H='dsx3ConfigExtE3Framing'
_G='dsx3ConfigExtScrambleEnabled'
_F='dsx3ConfigExtEntry'
_E='TruthValue'
_D='read-write'
_C='Integer32'
_B='ZHONE-PHY-DS3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx3ConfigEntry,=mibBuilder.importSymbols('DS3-MIB','dsx3ConfigEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
zhoneDs3Ext,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneDs3Ext','zhoneModules')
phyDs3=ModuleIdentity((1,3,6,1,4,1,5504,6,17))
if mibBuilder.loadTexts:phyDs3.setRevisions(('2001-05-14 14:35','2001-04-25 14:25','2001-03-15 08:34'))
_Dsx3ConfigExtTable_Object=MibTable
dsx3ConfigExtTable=_Dsx3ConfigExtTable_Object((1,3,6,1,4,1,5504,5,10,2))
if mibBuilder.loadTexts:dsx3ConfigExtTable.setStatus(_A)
_Dsx3ConfigExtEntry_Object=MibTableRow
dsx3ConfigExtEntry=_Dsx3ConfigExtEntry_Object((1,3,6,1,4,1,5504,5,10,2,1))
if mibBuilder.loadTexts:dsx3ConfigExtEntry.setStatus(_A)
class _Dsx3ConfigExtScrambleEnabled_Type(TruthValue):defaultValue=1
_Dsx3ConfigExtScrambleEnabled_Type.__name__=_E
_Dsx3ConfigExtScrambleEnabled_Object=MibTableColumn
dsx3ConfigExtScrambleEnabled=_Dsx3ConfigExtScrambleEnabled_Object((1,3,6,1,4,1,5504,5,10,2,1,1),_Dsx3ConfigExtScrambleEnabled_Type())
dsx3ConfigExtScrambleEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3ConfigExtScrambleEnabled.setStatus(_A)
class _Dsx3ConfigExtE3Framing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('e3FrameOther',1),('e3FrameG832',2),('e3FrameG751',3)))
_Dsx3ConfigExtE3Framing_Type.__name__=_C
_Dsx3ConfigExtE3Framing_Object=MibTableColumn
dsx3ConfigExtE3Framing=_Dsx3ConfigExtE3Framing_Object((1,3,6,1,4,1,5504,5,10,2,1,2),_Dsx3ConfigExtE3Framing_Type())
dsx3ConfigExtE3Framing.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3ConfigExtE3Framing.setStatus(_A)
class _Dsx3ConfigExtAtmFraming_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dsx3AtmFramingOther',1),('dsx3AtmFramingPLCP',2),('dsx3AtmFramingDirectCellMapped',3)))
_Dsx3ConfigExtAtmFraming_Type.__name__=_C
_Dsx3ConfigExtAtmFraming_Object=MibTableColumn
dsx3ConfigExtAtmFraming=_Dsx3ConfigExtAtmFraming_Object((1,3,6,1,4,1,5504,5,10,2,1,3),_Dsx3ConfigExtAtmFraming_Type())
dsx3ConfigExtAtmFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3ConfigExtAtmFraming.setStatus(_A)
dsx3ConfigEntry.registerAugmentions((_B,_F))
dsx3ConfigExtEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
dsx3ConfigExtGroup=ObjectGroup((1,3,6,1,4,1,5504,5,10,1))
dsx3ConfigExtGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:dsx3ConfigExtGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsx3ConfigExtGroup':dsx3ConfigExtGroup,'dsx3ConfigExtTable':dsx3ConfigExtTable,_F:dsx3ConfigExtEntry,_G:dsx3ConfigExtScrambleEnabled,_H:dsx3ConfigExtE3Framing,_I:dsx3ConfigExtAtmFraming,'phyDs3':phyDs3})