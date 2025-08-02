_c='cXdslLineConfProfileGroup'
_b='cXdslLineGroup'
_a='cXdslModeSpectrum'
_Z='cXdslModeLoopback'
_Y='cXdslTestBertBitRate'
_X='cXdslTestBertRunTime'
_W='cXdslTestBertBitErrors'
_V='cXdslTestBertErrors'
_U='cXdslTestTime'
_T='cXdslTestTrigger'
_S='cXdslTestType'
_R='cXdslTestStatus'
_Q='cXdslLineConfLinkUpDownTrap'
_P='cXdslLineConfAlarmsEnabled'
_O='cXdslLineConfPayloadScrambled'
_N='cXdslLineNoOfChanges'
_M='cXdslLineTimeSinceLastChange'
_L='cXdslLineConfProfileEntry'
_K='disabled'
_J='Unsigned32'
_I='read-create'
_H='TruthValue'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-XDSL-LINE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineConfProfileEntry,=mibBuilder.importSymbols('ADSL-LINE-MIB','adslLineConfProfileEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
ciscoXdslLineMIB=ModuleIdentity((1,3,6,1,4,1,9,9,204))
if mibBuilder.loadTexts:ciscoXdslLineMIB.setRevisions(('2001-02-10 00:00',))
_CiscoXdslLineMIBObjects_ObjectIdentity=ObjectIdentity
ciscoXdslLineMIBObjects=_CiscoXdslLineMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,204,1))
_CXdslLineTable_Object=MibTable
cXdslLineTable=_CXdslLineTable_Object((1,3,6,1,4,1,9,9,204,1,1))
if mibBuilder.loadTexts:cXdslLineTable.setStatus(_A)
_CXdslLineEntry_Object=MibTableRow
cXdslLineEntry=_CXdslLineEntry_Object((1,3,6,1,4,1,9,9,204,1,1,1))
cXdslLineEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cXdslLineEntry.setStatus(_A)
_CXdslLineTimeSinceLastChange_Type=TimeTicks
_CXdslLineTimeSinceLastChange_Object=MibTableColumn
cXdslLineTimeSinceLastChange=_CXdslLineTimeSinceLastChange_Object((1,3,6,1,4,1,9,9,204,1,1,1,1),_CXdslLineTimeSinceLastChange_Type())
cXdslLineTimeSinceLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslLineTimeSinceLastChange.setStatus(_A)
_CXdslLineNoOfChanges_Type=Counter32
_CXdslLineNoOfChanges_Object=MibTableColumn
cXdslLineNoOfChanges=_CXdslLineNoOfChanges_Object((1,3,6,1,4,1,9,9,204,1,1,1,2),_CXdslLineNoOfChanges_Type())
cXdslLineNoOfChanges.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslLineNoOfChanges.setStatus(_A)
_CXdslTestTable_Object=MibTable
cXdslTestTable=_CXdslTestTable_Object((1,3,6,1,4,1,9,9,204,1,2))
if mibBuilder.loadTexts:cXdslTestTable.setStatus(_A)
_CXdslTestEntry_Object=MibTableRow
cXdslTestEntry=_CXdslTestEntry_Object((1,3,6,1,4,1,9,9,204,1,2,1))
cXdslTestEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cXdslTestEntry.setStatus(_A)
class _CXdslTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('active',2),('passed',3),('failed',4),('aborted',5)))
_CXdslTestStatus_Type.__name__=_C
_CXdslTestStatus_Object=MibTableColumn
cXdslTestStatus=_CXdslTestStatus_Object((1,3,6,1,4,1,9,9,204,1,2,1,1),_CXdslTestStatus_Type())
cXdslTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslTestStatus.setStatus(_A)
class _CXdslTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('bertDigitalLocal',2),('bertAnalogLocal',3),('bertDigitalRemote',4),('bertAnalogRemote',5),('other',6)))
_CXdslTestType_Type.__name__=_C
_CXdslTestType_Object=MibTableColumn
cXdslTestType=_CXdslTestType_Object((1,3,6,1,4,1,9,9,204,1,2,1,2),_CXdslTestType_Type())
cXdslTestType.setMaxAccess(_E)
if mibBuilder.loadTexts:cXdslTestType.setStatus(_A)
class _CXdslTestTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stop',1),('start',2),('clear',3),('ready',4)))
_CXdslTestTrigger_Type.__name__=_C
_CXdslTestTrigger_Object=MibTableColumn
cXdslTestTrigger=_CXdslTestTrigger_Object((1,3,6,1,4,1,9,9,204,1,2,1,3),_CXdslTestTrigger_Type())
cXdslTestTrigger.setMaxAccess(_E)
if mibBuilder.loadTexts:cXdslTestTrigger.setStatus(_A)
class _CXdslTestTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_CXdslTestTime_Type.__name__=_C
_CXdslTestTime_Object=MibTableColumn
cXdslTestTime=_CXdslTestTime_Object((1,3,6,1,4,1,9,9,204,1,2,1,4),_CXdslTestTime_Type())
cXdslTestTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cXdslTestTime.setStatus(_A)
if mibBuilder.loadTexts:cXdslTestTime.setUnits('minutes')
class _CXdslTestBertErrors_Type(Bits):namedValues=NamedValues(*(('noError',0),('cpeBertAborted',1),('lostCpeSync',2),('noCpeSync',3),('noCpeResults',4),('coBertAborted',5),('lostCoSync',6),('noCoSync',7)))
_CXdslTestBertErrors_Type.__name__='Bits'
_CXdslTestBertErrors_Object=MibTableColumn
cXdslTestBertErrors=_CXdslTestBertErrors_Object((1,3,6,1,4,1,9,9,204,1,2,1,5),_CXdslTestBertErrors_Type())
cXdslTestBertErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslTestBertErrors.setStatus(_A)
class _CXdslTestBertBitErrors_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CXdslTestBertBitErrors_Type.__name__=_J
_CXdslTestBertBitErrors_Object=MibTableColumn
cXdslTestBertBitErrors=_CXdslTestBertBitErrors_Object((1,3,6,1,4,1,9,9,204,1,2,1,6),_CXdslTestBertBitErrors_Type())
cXdslTestBertBitErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslTestBertBitErrors.setStatus(_A)
class _CXdslTestBertRunTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_CXdslTestBertRunTime_Type.__name__=_C
_CXdslTestBertRunTime_Object=MibTableColumn
cXdslTestBertRunTime=_CXdslTestBertRunTime_Object((1,3,6,1,4,1,9,9,204,1,2,1,7),_CXdslTestBertRunTime_Type())
cXdslTestBertRunTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslTestBertRunTime.setStatus(_A)
if mibBuilder.loadTexts:cXdslTestBertRunTime.setUnits('seconds')
class _CXdslTestBertBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000000))
_CXdslTestBertBitRate_Type.__name__=_C
_CXdslTestBertBitRate_Object=MibTableColumn
cXdslTestBertBitRate=_CXdslTestBertBitRate_Object((1,3,6,1,4,1,9,9,204,1,2,1,8),_CXdslTestBertBitRate_Type())
cXdslTestBertBitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cXdslTestBertBitRate.setStatus(_A)
if mibBuilder.loadTexts:cXdslTestBertBitRate.setUnits('bps')
_CXdslModeTable_Object=MibTable
cXdslModeTable=_CXdslModeTable_Object((1,3,6,1,4,1,9,9,204,1,3))
if mibBuilder.loadTexts:cXdslModeTable.setStatus(_A)
_CXdslModeEntry_Object=MibTableRow
cXdslModeEntry=_CXdslModeEntry_Object((1,3,6,1,4,1,9,9,204,1,3,1))
cXdslModeEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cXdslModeEntry.setStatus(_A)
class _CXdslModeLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('loopbackAnalogLocal',2),('loopbackDigitalLocal',3),('loopbackAnalogRemote',4),('loopbackDigitalRemote',5),('other',6)))
_CXdslModeLoopback_Type.__name__=_C
_CXdslModeLoopback_Object=MibTableColumn
cXdslModeLoopback=_CXdslModeLoopback_Object((1,3,6,1,4,1,9,9,204,1,3,1,1),_CXdslModeLoopback_Type())
cXdslModeLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:cXdslModeLoopback.setStatus(_A)
class _CXdslModeSpectrum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),('spectrum1',2),('spectrum2',3),('spectrum3',4),('spectrum4',5),('spectrum5',6),('spectrum6',7)))
_CXdslModeSpectrum_Type.__name__=_C
_CXdslModeSpectrum_Object=MibTableColumn
cXdslModeSpectrum=_CXdslModeSpectrum_Object((1,3,6,1,4,1,9,9,204,1,3,1,2),_CXdslModeSpectrum_Type())
cXdslModeSpectrum.setMaxAccess(_E)
if mibBuilder.loadTexts:cXdslModeSpectrum.setStatus(_A)
_CXdslLineConfProfileTable_Object=MibTable
cXdslLineConfProfileTable=_CXdslLineConfProfileTable_Object((1,3,6,1,4,1,9,9,204,1,4))
if mibBuilder.loadTexts:cXdslLineConfProfileTable.setStatus(_A)
_CXdslLineConfProfileEntry_Object=MibTableRow
cXdslLineConfProfileEntry=_CXdslLineConfProfileEntry_Object((1,3,6,1,4,1,9,9,204,1,4,1))
if mibBuilder.loadTexts:cXdslLineConfProfileEntry.setStatus(_A)
class _CXdslLineConfPayloadScrambled_Type(TruthValue):defaultValue=1
_CXdslLineConfPayloadScrambled_Type.__name__=_H
_CXdslLineConfPayloadScrambled_Object=MibTableColumn
cXdslLineConfPayloadScrambled=_CXdslLineConfPayloadScrambled_Object((1,3,6,1,4,1,9,9,204,1,4,1,1),_CXdslLineConfPayloadScrambled_Type())
cXdslLineConfPayloadScrambled.setMaxAccess(_I)
if mibBuilder.loadTexts:cXdslLineConfPayloadScrambled.setStatus(_A)
class _CXdslLineConfAlarmsEnabled_Type(TruthValue):defaultValue=2
_CXdslLineConfAlarmsEnabled_Type.__name__=_H
_CXdslLineConfAlarmsEnabled_Object=MibTableColumn
cXdslLineConfAlarmsEnabled=_CXdslLineConfAlarmsEnabled_Object((1,3,6,1,4,1,9,9,204,1,4,1,2),_CXdslLineConfAlarmsEnabled_Type())
cXdslLineConfAlarmsEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:cXdslLineConfAlarmsEnabled.setStatus(_A)
class _CXdslLineConfLinkUpDownTrap_Type(TruthValue):defaultValue=2
_CXdslLineConfLinkUpDownTrap_Type.__name__=_H
_CXdslLineConfLinkUpDownTrap_Object=MibTableColumn
cXdslLineConfLinkUpDownTrap=_CXdslLineConfLinkUpDownTrap_Object((1,3,6,1,4,1,9,9,204,1,4,1,3),_CXdslLineConfLinkUpDownTrap_Type())
cXdslLineConfLinkUpDownTrap.setMaxAccess(_I)
if mibBuilder.loadTexts:cXdslLineConfLinkUpDownTrap.setStatus(_A)
_CiscoXdslLineMIBConformance_ObjectIdentity=ObjectIdentity
ciscoXdslLineMIBConformance=_CiscoXdslLineMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,204,3))
_CiscoXdslLineMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoXdslLineMIBCompliances=_CiscoXdslLineMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,204,3,1))
_CiscoXdslLineMIBGroups_ObjectIdentity=ObjectIdentity
ciscoXdslLineMIBGroups=_CiscoXdslLineMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,204,3,2))
adslLineConfProfileEntry.registerAugmentions((_B,_L))
cXdslLineConfProfileEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
cXdslLineGroup=ObjectGroup((1,3,6,1,4,1,9,9,204,3,2,1))
cXdslLineGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cXdslLineGroup.setStatus(_A)
cXdslLineConfProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,204,3,2,2))
cXdslLineConfProfileGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cXdslLineConfProfileGroup.setStatus(_A)
cXdslTestGroup=ObjectGroup((1,3,6,1,4,1,9,9,204,3,2,3))
cXdslTestGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cXdslTestGroup.setStatus(_A)
cXdslModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,204,3,2,4))
cXdslModeGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cXdslModeGroup.setStatus(_A)
ciscoXdslLineMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,204,3,1,1))
ciscoXdslLineMIBCompliance.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoXdslLineMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoXdslLineMIB':ciscoXdslLineMIB,'ciscoXdslLineMIBObjects':ciscoXdslLineMIBObjects,'cXdslLineTable':cXdslLineTable,'cXdslLineEntry':cXdslLineEntry,_M:cXdslLineTimeSinceLastChange,_N:cXdslLineNoOfChanges,'cXdslTestTable':cXdslTestTable,'cXdslTestEntry':cXdslTestEntry,_R:cXdslTestStatus,_S:cXdslTestType,_T:cXdslTestTrigger,_U:cXdslTestTime,_V:cXdslTestBertErrors,_W:cXdslTestBertBitErrors,_X:cXdslTestBertRunTime,_Y:cXdslTestBertBitRate,'cXdslModeTable':cXdslModeTable,'cXdslModeEntry':cXdslModeEntry,_Z:cXdslModeLoopback,_a:cXdslModeSpectrum,'cXdslLineConfProfileTable':cXdslLineConfProfileTable,_L:cXdslLineConfProfileEntry,_O:cXdslLineConfPayloadScrambled,_P:cXdslLineConfAlarmsEnabled,_Q:cXdslLineConfLinkUpDownTrap,'ciscoXdslLineMIBConformance':ciscoXdslLineMIBConformance,'ciscoXdslLineMIBCompliances':ciscoXdslLineMIBCompliances,'ciscoXdslLineMIBCompliance':ciscoXdslLineMIBCompliance,'ciscoXdslLineMIBGroups':ciscoXdslLineMIBGroups,_b:cXdslLineGroup,_c:cXdslLineConfProfileGroup,'cXdslTestGroup':cXdslTestGroup,'cXdslModeGroup':cXdslModeGroup})