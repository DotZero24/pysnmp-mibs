_P='FieldBits'
_O='not-accessible'
_N='KeyBits'
_M='rlSetsEntryPortListKey'
_L='rlSetsEntryBitsKey'
_K='fifthField'
_J='thirdField'
_I='secondField'
_H='firstField'
_G='fifthKey'
_F='thirdKey'
_E='secondKey'
_D='firstKey'
_C='read-create'
_B='SNMP-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rlSnmpTestSimulatedVariables,=mibBuilder.importSymbols('RADLAN-rndApplications','rlSnmpTestSimulatedVariables')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class KeyBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),('fourthKey',3),(_G,4)))
class FieldBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),('fourthField',3),(_K,4)))
_RlSnmpTestMibVersion_Type=Integer32
_RlSnmpTestMibVersion_Object=MibScalar
rlSnmpTestMibVersion=_RlSnmpTestMibVersion_Object((1,3,6,1,4,1,89,35,2,9,9,1),_RlSnmpTestMibVersion_Type())
rlSnmpTestMibVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlSnmpTestMibVersion.setStatus(_A)
_RlSetsTestTable_Object=MibTable
rlSetsTestTable=_RlSetsTestTable_Object((1,3,6,1,4,1,89,35,2,9,9,2))
if mibBuilder.loadTexts:rlSetsTestTable.setStatus(_A)
_RlSetsTestEntry_Object=MibTableRow
rlSetsTestEntry=_RlSetsTestEntry_Object((1,3,6,1,4,1,89,35,2,9,9,2,1))
rlSetsTestEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:rlSetsTestEntry.setStatus(_A)
class _RlSetsEntryBitsKey_Type(KeyBits):subtypeSpec=KeyBits.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,4)))
_RlSetsEntryBitsKey_Type.__name__=_N
_RlSetsEntryBitsKey_Object=MibTableColumn
rlSetsEntryBitsKey=_RlSetsEntryBitsKey_Object((1,3,6,1,4,1,89,35,2,9,9,2,1,1),_RlSetsEntryBitsKey_Type())
rlSetsEntryBitsKey.setMaxAccess(_O)
if mibBuilder.loadTexts:rlSetsEntryBitsKey.setStatus(_A)
_RlSetsEntryPortListKey_Type=PortList
_RlSetsEntryPortListKey_Object=MibTableColumn
rlSetsEntryPortListKey=_RlSetsEntryPortListKey_Object((1,3,6,1,4,1,89,35,2,9,9,2,1,2),_RlSetsEntryPortListKey_Type())
rlSetsEntryPortListKey.setMaxAccess(_O)
if mibBuilder.loadTexts:rlSetsEntryPortListKey.setStatus(_A)
class _RlSetsEntryBitsField_Type(FieldBits):subtypeSpec=FieldBits.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*((_H,0),(_I,1),(_J,2),(_K,4)))
_RlSetsEntryBitsField_Type.__name__=_P
_RlSetsEntryBitsField_Object=MibTableColumn
rlSetsEntryBitsField=_RlSetsEntryBitsField_Object((1,3,6,1,4,1,89,35,2,9,9,2,1,3),_RlSetsEntryBitsField_Type())
rlSetsEntryBitsField.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSetsEntryBitsField.setStatus(_A)
_RlSetsEntryPortListField_Type=PortList
_RlSetsEntryPortListField_Object=MibTableColumn
rlSetsEntryPortListField=_RlSetsEntryPortListField_Object((1,3,6,1,4,1,89,35,2,9,9,2,1,4),_RlSetsEntryPortListField_Type())
rlSetsEntryPortListField.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSetsEntryPortListField.setStatus(_A)
_RlSetsEntryCounter64Field_Type=Counter64
_RlSetsEntryCounter64Field_Object=MibTableColumn
rlSetsEntryCounter64Field=_RlSetsEntryCounter64Field_Object((1,3,6,1,4,1,89,35,2,9,9,2,1,5),_RlSetsEntryCounter64Field_Type())
rlSetsEntryCounter64Field.setMaxAccess(_C)
if mibBuilder.loadTexts:rlSetsEntryCounter64Field.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:KeyBits,_P:FieldBits,'rlSnmpTestMibVersion':rlSnmpTestMibVersion,'rlSetsTestTable':rlSetsTestTable,'rlSetsTestEntry':rlSetsTestEntry,_L:rlSetsEntryBitsKey,_M:rlSetsEntryPortListKey,'rlSetsEntryBitsField':rlSetsEntryBitsField,'rlSetsEntryPortListField':rlSetsEntryPortListField,'rlSetsEntryCounter64Field':rlSetsEntryCounter64Field})