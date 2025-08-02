_H='rlPhyTestGetType'
_G='NETGEAR-RADLAN-PHY-MIB'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
rlPhy=ModuleIdentity((1,3,6,1,4,1,4526,17,90))
if mibBuilder.loadTexts:rlPhy.setRevisions(('2002-09-30 00:24','2003-09-21 00:24'))
class RlPhyTestType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('rlPhyTestTableNoTest',1),('rlPhyTestTableCableStatus',2),('rlPhyTestTableCableFault',3),('rlPhyTestTableCableLength',4),('rlPhyTestTableTransceiverTemp',5),('rlPhyTestTableTransceiverSupply',6),('rlPhyTestTableTxBias',7),('rlPhyTestTableTxOutput',8),('rlPhyTestTableRxOpticalPower',9),('rlPhyTestTableDataReady',10),('rlPhyTestTableLOS',11),('rlPhyTestTableTxFault',12),('rlPhyTestTableCableChannel1',13),('rlPhyTestTableCableChannel2',14),('rlPhyTestTableCableChannel3',15),('rlPhyTestTableCableChannel4',16),('rlPhyTestTableCablePolarity1',17),('rlPhyTestTableCablePolarity2',18),('rlPhyTestTableCablePolarity3',19),('rlPhyTestTableCablePolarity4',20),('rlPhyTestTableCablePairSkew1',21),('rlPhyTestTableCablePairSkew2',22),('rlPhyTestTableCablePairSkew3',23),('rlPhyTestTableCablePairSkew4',24),('rlPhyTestTableCableStatusFast',25),('rlPhyTestTableSFPEepromQualified',26)))
_RlPhyTest_ObjectIdentity=ObjectIdentity
rlPhyTest=_RlPhyTest_ObjectIdentity((1,3,6,1,4,1,4526,17,90,1))
_RlPhyTestSetTable_Object=MibTable
rlPhyTestSetTable=_RlPhyTestSetTable_Object((1,3,6,1,4,1,4526,17,90,1,1))
if mibBuilder.loadTexts:rlPhyTestSetTable.setStatus(_A)
_RlPhyTestSetEntry_Object=MibTableRow
rlPhyTestSetEntry=_RlPhyTestSetEntry_Object((1,3,6,1,4,1,4526,17,90,1,1,1))
rlPhyTestSetEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPhyTestSetEntry.setStatus(_A)
_RlPhyTestSetType_Type=RlPhyTestType
_RlPhyTestSetType_Object=MibTableColumn
rlPhyTestSetType=_RlPhyTestSetType_Object((1,3,6,1,4,1,4526,17,90,1,1,1,1),_RlPhyTestSetType_Type())
rlPhyTestSetType.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlPhyTestSetType.setStatus(_A)
_RlPhyTestGetTable_Object=MibTable
rlPhyTestGetTable=_RlPhyTestGetTable_Object((1,3,6,1,4,1,4526,17,90,1,2))
if mibBuilder.loadTexts:rlPhyTestGetTable.setStatus(_A)
_RlPhyTestGetEntry_Object=MibTableRow
rlPhyTestGetEntry=_RlPhyTestGetEntry_Object((1,3,6,1,4,1,4526,17,90,1,2,1))
rlPhyTestGetEntry.setIndexNames((0,_D,_E),(0,_G,_H))
if mibBuilder.loadTexts:rlPhyTestGetEntry.setStatus(_A)
_RlPhyTestGetType_Type=RlPhyTestType
_RlPhyTestGetType_Object=MibTableColumn
rlPhyTestGetType=_RlPhyTestGetType_Object((1,3,6,1,4,1,4526,17,90,1,2,1,1),_RlPhyTestGetType_Type())
rlPhyTestGetType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetType.setStatus(_A)
class _RlPhyTestGetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('success',2),('inProgress',3),('notSupported',4),('unAbleToRun',5),('aborted',6),('failed',7)))
_RlPhyTestGetStatus_Type.__name__=_C
_RlPhyTestGetStatus_Object=MibTableColumn
rlPhyTestGetStatus=_RlPhyTestGetStatus_Object((1,3,6,1,4,1,4526,17,90,1,2,1,2),_RlPhyTestGetStatus_Type())
rlPhyTestGetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetStatus.setStatus(_A)
_RlPhyTestGetResult_Type=Integer32
_RlPhyTestGetResult_Object=MibTableColumn
rlPhyTestGetResult=_RlPhyTestGetResult_Object((1,3,6,1,4,1,4526,17,90,1,2,1,3),_RlPhyTestGetResult_Type())
rlPhyTestGetResult.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetResult.setStatus(_A)
class _RlPhyTestGetUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('integer',1),('boolean',2),('downUP',3),('reverseNormal',4),('mdiMdix',5),('meter',6),('degree',7),('microVolt',8),('microOham',9),('microAmper',10),('microWatt',11),('millisecond',12),('alaskaPhyLength',13),('alaskaPhyStatus',14),('dbm',15),('decidbm',16),('milidbm',17),('abcd',18),('nanosecond',19)))
_RlPhyTestGetUnits_Type.__name__=_C
_RlPhyTestGetUnits_Object=MibTableColumn
rlPhyTestGetUnits=_RlPhyTestGetUnits_Object((1,3,6,1,4,1,4526,17,90,1,2,1,4),_RlPhyTestGetUnits_Type())
rlPhyTestGetUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetUnits.setStatus(_A)
class _RlPhyTestGetAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notRelevant',1),('noAlarmSet',2),('lowWarning',3),('highWarning',4),('lowAlarm',5),('highAlarm',6)))
_RlPhyTestGetAlarm_Type.__name__=_C
_RlPhyTestGetAlarm_Object=MibTableColumn
rlPhyTestGetAlarm=_RlPhyTestGetAlarm_Object((1,3,6,1,4,1,4526,17,90,1,2,1,5),_RlPhyTestGetAlarm_Type())
rlPhyTestGetAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetAlarm.setStatus(_A)
class _RlPhyTestGetTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlPhyTestGetTimeStamp_Type.__name__=_F
_RlPhyTestGetTimeStamp_Object=MibTableColumn
rlPhyTestGetTimeStamp=_RlPhyTestGetTimeStamp_Object((1,3,6,1,4,1,4526,17,90,1,2,1,6),_RlPhyTestGetTimeStamp_Type())
rlPhyTestGetTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPhyTestGetTimeStamp.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'RlPhyTestType':RlPhyTestType,'rlPhy':rlPhy,'rlPhyTest':rlPhyTest,'rlPhyTestSetTable':rlPhyTestSetTable,'rlPhyTestSetEntry':rlPhyTestSetEntry,'rlPhyTestSetType':rlPhyTestSetType,'rlPhyTestGetTable':rlPhyTestGetTable,'rlPhyTestGetEntry':rlPhyTestGetEntry,_H:rlPhyTestGetType,'rlPhyTestGetStatus':rlPhyTestGetStatus,'rlPhyTestGetResult':rlPhyTestGetResult,'rlPhyTestGetUnits':rlPhyTestGetUnits,'rlPhyTestGetAlarm':rlPhyTestGetAlarm,'rlPhyTestGetTimeStamp':rlPhyTestGetTimeStamp})