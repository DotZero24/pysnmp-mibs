_R='cDot11RadioDiagConfigGroupRev1'
_Q='cDot11RadioDiagConfigGlobalGroup'
_P='cDot11RadioDiagTempDataRateSet'
_O='cDot11RadioDiagTempClientTxPower'
_N='deprecated'
_M='TruthValue'
_L='Integer32'
_K='ifIndex'
_J='IF-MIB'
_I='OctetString'
_H='cDot11RadioDiagSettingsEnabled'
_G='cDot11RadioDiagMode'
_F='cDot11RadioDiagTempTxPowerLevel'
_E='cDot11RadioDiagTempChannel'
_D='Unsigned32'
_C='read-write'
_B='current'
_A='CISCO-DOT11-RADIO-DIAGNOSTIC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_M)
ciscoDot11RadioDiagMIB=ModuleIdentity((1,3,6,1,4,1,9,10,105))
if mibBuilder.loadTexts:ciscoDot11RadioDiagMIB.setRevisions(('2003-12-23 00:00','2003-05-08 00:00'))
_CDot11RadioDiagMIBNotifs_ObjectIdentity=ObjectIdentity
cDot11RadioDiagMIBNotifs=_CDot11RadioDiagMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,105,0))
_CDot11RadioDiagMIBObjects_ObjectIdentity=ObjectIdentity
cDot11RadioDiagMIBObjects=_CDot11RadioDiagMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,105,1))
_CDot11RadioDiagConfigGlobal_ObjectIdentity=ObjectIdentity
cDot11RadioDiagConfigGlobal=_CDot11RadioDiagConfigGlobal_ObjectIdentity((1,3,6,1,4,1,9,10,105,1,1))
_CDot11RadioDiagTable_Object=MibTable
cDot11RadioDiagTable=_CDot11RadioDiagTable_Object((1,3,6,1,4,1,9,10,105,1,1,1))
if mibBuilder.loadTexts:cDot11RadioDiagTable.setStatus(_B)
_CDot11RadioDiagEntry_Object=MibTableRow
cDot11RadioDiagEntry=_CDot11RadioDiagEntry_Object((1,3,6,1,4,1,9,10,105,1,1,1,1))
cDot11RadioDiagEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cDot11RadioDiagEntry.setStatus(_B)
class _CDot11RadioDiagTempChannel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14),ValueRangeConstraint(34,34),ValueRangeConstraint(36,36),ValueRangeConstraint(38,38),ValueRangeConstraint(40,40),ValueRangeConstraint(42,42),ValueRangeConstraint(44,44),ValueRangeConstraint(46,46),ValueRangeConstraint(48,48),ValueRangeConstraint(52,52),ValueRangeConstraint(56,56),ValueRangeConstraint(60,60),ValueRangeConstraint(64,64),ValueRangeConstraint(100,100),ValueRangeConstraint(104,104),ValueRangeConstraint(108,108),ValueRangeConstraint(112,112),ValueRangeConstraint(116,116),ValueRangeConstraint(120,120),ValueRangeConstraint(124,124),ValueRangeConstraint(128,128),ValueRangeConstraint(132,132),ValueRangeConstraint(136,136),ValueRangeConstraint(140,140),ValueRangeConstraint(149,149),ValueRangeConstraint(153,153),ValueRangeConstraint(157,157),ValueRangeConstraint(161,161))
_CDot11RadioDiagTempChannel_Type.__name__=_D
_CDot11RadioDiagTempChannel_Object=MibTableColumn
cDot11RadioDiagTempChannel=_CDot11RadioDiagTempChannel_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,1),_CDot11RadioDiagTempChannel_Type())
cDot11RadioDiagTempChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagTempChannel.setStatus(_B)
class _CDot11RadioDiagTempTxPowerLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CDot11RadioDiagTempTxPowerLevel_Type.__name__=_D
_CDot11RadioDiagTempTxPowerLevel_Object=MibTableColumn
cDot11RadioDiagTempTxPowerLevel=_CDot11RadioDiagTempTxPowerLevel_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,2),_CDot11RadioDiagTempTxPowerLevel_Type())
cDot11RadioDiagTempTxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagTempTxPowerLevel.setStatus(_B)
class _CDot11RadioDiagMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('apRadioDiscovery',2),('siteSurveyTempSettings',3),('siteSurveyNonTempSettings',4)))
_CDot11RadioDiagMode_Type.__name__=_L
_CDot11RadioDiagMode_Object=MibTableColumn
cDot11RadioDiagMode=_CDot11RadioDiagMode_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,3),_CDot11RadioDiagMode_Type())
cDot11RadioDiagMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagMode.setStatus(_B)
class _CDot11RadioDiagSettingsEnabled_Type(TruthValue):defaultValue=2
_CDot11RadioDiagSettingsEnabled_Type.__name__=_M
_CDot11RadioDiagSettingsEnabled_Object=MibTableColumn
cDot11RadioDiagSettingsEnabled=_CDot11RadioDiagSettingsEnabled_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,4),_CDot11RadioDiagSettingsEnabled_Type())
cDot11RadioDiagSettingsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagSettingsEnabled.setStatus(_B)
class _CDot11RadioDiagTempClientTxPower_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CDot11RadioDiagTempClientTxPower_Type.__name__=_D
_CDot11RadioDiagTempClientTxPower_Object=MibTableColumn
cDot11RadioDiagTempClientTxPower=_CDot11RadioDiagTempClientTxPower_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,5),_CDot11RadioDiagTempClientTxPower_Type())
cDot11RadioDiagTempClientTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagTempClientTxPower.setStatus(_B)
class _CDot11RadioDiagTempDataRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_CDot11RadioDiagTempDataRateSet_Type.__name__=_I
_CDot11RadioDiagTempDataRateSet_Object=MibTableColumn
cDot11RadioDiagTempDataRateSet=_CDot11RadioDiagTempDataRateSet_Object((1,3,6,1,4,1,9,10,105,1,1,1,1,6),_CDot11RadioDiagTempDataRateSet_Type())
cDot11RadioDiagTempDataRateSet.setMaxAccess(_C)
if mibBuilder.loadTexts:cDot11RadioDiagTempDataRateSet.setStatus(_B)
_CDot11RadioDiagMIBConform_ObjectIdentity=ObjectIdentity
cDot11RadioDiagMIBConform=_CDot11RadioDiagMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,105,2))
_CDot11RadioDiagMIBCompliances_ObjectIdentity=ObjectIdentity
cDot11RadioDiagMIBCompliances=_CDot11RadioDiagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,105,2,1))
_CDot11RadioDiagMIBGroups_ObjectIdentity=ObjectIdentity
cDot11RadioDiagMIBGroups=_CDot11RadioDiagMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,105,2,2))
cDot11RadioDiagConfigGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,10,105,2,2,1))
cDot11RadioDiagConfigGlobalGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cDot11RadioDiagConfigGlobalGroup.setStatus(_N)
cDot11RadioDiagConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,105,2,2,2))
cDot11RadioDiagConfigGroupRev1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:cDot11RadioDiagConfigGroupRev1.setStatus(_B)
cDot11RadioDiagMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,105,2,1,1))
cDot11RadioDiagMIBCompliance.setObjects((_A,_Q))
if mibBuilder.loadTexts:cDot11RadioDiagMIBCompliance.setStatus(_N)
cDot11RadioDiagMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,105,2,1,2))
cDot11RadioDiagMIBComplianceRev1.setObjects((_A,_R))
if mibBuilder.loadTexts:cDot11RadioDiagMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoDot11RadioDiagMIB':ciscoDot11RadioDiagMIB,'cDot11RadioDiagMIBNotifs':cDot11RadioDiagMIBNotifs,'cDot11RadioDiagMIBObjects':cDot11RadioDiagMIBObjects,'cDot11RadioDiagConfigGlobal':cDot11RadioDiagConfigGlobal,'cDot11RadioDiagTable':cDot11RadioDiagTable,'cDot11RadioDiagEntry':cDot11RadioDiagEntry,_E:cDot11RadioDiagTempChannel,_F:cDot11RadioDiagTempTxPowerLevel,_G:cDot11RadioDiagMode,_H:cDot11RadioDiagSettingsEnabled,_O:cDot11RadioDiagTempClientTxPower,_P:cDot11RadioDiagTempDataRateSet,'cDot11RadioDiagMIBConform':cDot11RadioDiagMIBConform,'cDot11RadioDiagMIBCompliances':cDot11RadioDiagMIBCompliances,'cDot11RadioDiagMIBCompliance':cDot11RadioDiagMIBCompliance,'cDot11RadioDiagMIBComplianceRev1':cDot11RadioDiagMIBComplianceRev1,'cDot11RadioDiagMIBGroups':cDot11RadioDiagMIBGroups,_Q:cDot11RadioDiagConfigGlobalGroup,_R:cDot11RadioDiagConfigGroupRev1})