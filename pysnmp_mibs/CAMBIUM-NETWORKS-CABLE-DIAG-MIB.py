_M='cnCableDiagPortIndex'
_L='CAMBIUM-NETWORKS-CABLE-DIAG-MIB'
_K='no-test'
_J='test-failed'
_I='test-in-progress'
_H='pair-busy'
_G='cross-pair-short'
_F='same-pair-short'
_E='pair-open'
_D='pair-ok'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
cnCableDiagMib=ModuleIdentity((1,3,6,1,4,1,17713,24,7))
if mibBuilder.loadTexts:cnCableDiagMib.setRevisions(('2020-11-16 00:00',))
_CnCableDiagObjects_ObjectIdentity=ObjectIdentity
cnCableDiagObjects=_CnCableDiagObjects_ObjectIdentity((1,3,6,1,4,1,17713,24,7,0))
_CnCableDiagPortTable_Object=MibTable
cnCableDiagPortTable=_CnCableDiagPortTable_Object((1,3,6,1,4,1,17713,24,7,0,1))
if mibBuilder.loadTexts:cnCableDiagPortTable.setStatus(_A)
_CnCableDiagPortEntry_Object=MibTableRow
cnCableDiagPortEntry=_CnCableDiagPortEntry_Object((1,3,6,1,4,1,17713,24,7,0,1,1))
cnCableDiagPortEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:cnCableDiagPortEntry.setStatus(_A)
class _CnCableDiagPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagPortIndex_Type.__name__=_B
_CnCableDiagPortIndex_Object=MibTableColumn
cnCableDiagPortIndex=_CnCableDiagPortIndex_Object((1,3,6,1,4,1,17713,24,7,0,1,1,1),_CnCableDiagPortIndex_Type())
cnCableDiagPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cnCableDiagPortIndex.setStatus(_A)
class _CnCableDiagTestResultPair1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8)))
_CnCableDiagTestResultPair1_Type.__name__=_B
_CnCableDiagTestResultPair1_Object=MibTableColumn
cnCableDiagTestResultPair1=_CnCableDiagTestResultPair1_Object((1,3,6,1,4,1,17713,24,7,0,1,1,2),_CnCableDiagTestResultPair1_Type())
cnCableDiagTestResultPair1.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagTestResultPair1.setStatus(_A)
class _CnCableDiagTestResultPair2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8)))
_CnCableDiagTestResultPair2_Type.__name__=_B
_CnCableDiagTestResultPair2_Object=MibTableColumn
cnCableDiagTestResultPair2=_CnCableDiagTestResultPair2_Object((1,3,6,1,4,1,17713,24,7,0,1,1,3),_CnCableDiagTestResultPair2_Type())
cnCableDiagTestResultPair2.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagTestResultPair2.setStatus(_A)
class _CnCableDiagTestResultPair3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8)))
_CnCableDiagTestResultPair3_Type.__name__=_B
_CnCableDiagTestResultPair3_Object=MibTableColumn
cnCableDiagTestResultPair3=_CnCableDiagTestResultPair3_Object((1,3,6,1,4,1,17713,24,7,0,1,1,4),_CnCableDiagTestResultPair3_Type())
cnCableDiagTestResultPair3.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagTestResultPair3.setStatus(_A)
class _CnCableDiagTestResultPair4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_G,4),(_H,5),(_I,6),(_J,7),(_K,8)))
_CnCableDiagTestResultPair4_Type.__name__=_B
_CnCableDiagTestResultPair4_Object=MibTableColumn
cnCableDiagTestResultPair4=_CnCableDiagTestResultPair4_Object((1,3,6,1,4,1,17713,24,7,0,1,1,5),_CnCableDiagTestResultPair4_Type())
cnCableDiagTestResultPair4.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagTestResultPair4.setStatus(_A)
class _CnCableDiagFaultLengthPair1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagFaultLengthPair1_Type.__name__=_B
_CnCableDiagFaultLengthPair1_Object=MibTableColumn
cnCableDiagFaultLengthPair1=_CnCableDiagFaultLengthPair1_Object((1,3,6,1,4,1,17713,24,7,0,1,1,6),_CnCableDiagFaultLengthPair1_Type())
cnCableDiagFaultLengthPair1.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagFaultLengthPair1.setStatus(_A)
class _CnCableDiagFaultLengthPair2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagFaultLengthPair2_Type.__name__=_B
_CnCableDiagFaultLengthPair2_Object=MibTableColumn
cnCableDiagFaultLengthPair2=_CnCableDiagFaultLengthPair2_Object((1,3,6,1,4,1,17713,24,7,0,1,1,7),_CnCableDiagFaultLengthPair2_Type())
cnCableDiagFaultLengthPair2.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagFaultLengthPair2.setStatus(_A)
class _CnCableDiagFaultLengthPair3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagFaultLengthPair3_Type.__name__=_B
_CnCableDiagFaultLengthPair3_Object=MibTableColumn
cnCableDiagFaultLengthPair3=_CnCableDiagFaultLengthPair3_Object((1,3,6,1,4,1,17713,24,7,0,1,1,8),_CnCableDiagFaultLengthPair3_Type())
cnCableDiagFaultLengthPair3.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagFaultLengthPair3.setStatus(_A)
class _CnCableDiagFaultLengthPair4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagFaultLengthPair4_Type.__name__=_B
_CnCableDiagFaultLengthPair4_Object=MibTableColumn
cnCableDiagFaultLengthPair4=_CnCableDiagFaultLengthPair4_Object((1,3,6,1,4,1,17713,24,7,0,1,1,9),_CnCableDiagFaultLengthPair4_Type())
cnCableDiagFaultLengthPair4.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagFaultLengthPair4.setStatus(_A)
class _CnCableDiagTimeStamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CnCableDiagTimeStamp_Type.__name__=_B
_CnCableDiagTimeStamp_Object=MibTableColumn
cnCableDiagTimeStamp=_CnCableDiagTimeStamp_Object((1,3,6,1,4,1,17713,24,7,0,1,1,10),_CnCableDiagTimeStamp_Type())
cnCableDiagTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cnCableDiagTimeStamp.setStatus(_A)
class _CnCableDiagStartTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start-test',1),('default-value',2)))
_CnCableDiagStartTest_Type.__name__=_B
_CnCableDiagStartTest_Object=MibTableColumn
cnCableDiagStartTest=_CnCableDiagStartTest_Object((1,3,6,1,4,1,17713,24,7,0,1,1,11),_CnCableDiagStartTest_Type())
cnCableDiagStartTest.setMaxAccess('read-write')
if mibBuilder.loadTexts:cnCableDiagStartTest.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'cnCableDiagMib':cnCableDiagMib,'cnCableDiagObjects':cnCableDiagObjects,'cnCableDiagPortTable':cnCableDiagPortTable,'cnCableDiagPortEntry':cnCableDiagPortEntry,_M:cnCableDiagPortIndex,'cnCableDiagTestResultPair1':cnCableDiagTestResultPair1,'cnCableDiagTestResultPair2':cnCableDiagTestResultPair2,'cnCableDiagTestResultPair3':cnCableDiagTestResultPair3,'cnCableDiagTestResultPair4':cnCableDiagTestResultPair4,'cnCableDiagFaultLengthPair1':cnCableDiagFaultLengthPair1,'cnCableDiagFaultLengthPair2':cnCableDiagFaultLengthPair2,'cnCableDiagFaultLengthPair3':cnCableDiagFaultLengthPair3,'cnCableDiagFaultLengthPair4':cnCableDiagFaultLengthPair4,'cnCableDiagTimeStamp':cnCableDiagTimeStamp,'cnCableDiagStartTest':cnCableDiagStartTest})