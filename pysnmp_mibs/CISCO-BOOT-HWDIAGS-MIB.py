_S='ciscoBootHwDiagsMIBMainObjectGroup'
_R='ciscoBootHwDiagsMIBResultCode'
_Q='ciscoBootHwDiagsMIBConfigCode'
_P='ciscoBootHwDiagsMIBNextBootArmed'
_O='ciscoBootHwDiagsMIBNextBootConfigured'
_N='ciscoBootHwDiagsMIBLastBootPassed'
_M='ciscoBootHwDiagsMIBLastBootExecuted'
_L='ciscoBootHwDiagsMIBTestName'
_K='ciscoBootHwDiagsMIBCurrentBank'
_J='ciscoBootHwDiagsMIBBankIndex'
_I='not-accessible'
_H='DisplayString'
_G='read-write'
_F='ciscoBootHwDiagsMIBTestIndex'
_E='TruthValue'
_D='Unsigned32'
_C='read-only'
_B='CISCO-BOOT-HWDIAGS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_E)
ciscoBootHwDiagsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,696))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIB.setRevisions(('2009-05-12 00:00',))
_CiscoBootHwDiagsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoBootHwDiagsMIBNotifs=_CiscoBootHwDiagsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,696,0))
_CiscoBootHwDiagsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBootHwDiagsMIBObjects=_CiscoBootHwDiagsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,696,1))
class _CiscoBootHwDiagsMIBCurrentBank_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CiscoBootHwDiagsMIBCurrentBank_Type.__name__=_D
_CiscoBootHwDiagsMIBCurrentBank_Object=MibScalar
ciscoBootHwDiagsMIBCurrentBank=_CiscoBootHwDiagsMIBCurrentBank_Object((1,3,6,1,4,1,9,9,696,1,1),_CiscoBootHwDiagsMIBCurrentBank_Type())
ciscoBootHwDiagsMIBCurrentBank.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBCurrentBank.setStatus(_A)
_CiscoBootHwDiagsMIBTestTable_Object=MibTable
ciscoBootHwDiagsMIBTestTable=_CiscoBootHwDiagsMIBTestTable_Object((1,3,6,1,4,1,9,9,696,1,2))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBTestTable.setStatus(_A)
_CiscoBootHwDiagsMIBTestEntry_Object=MibTableRow
ciscoBootHwDiagsMIBTestEntry=_CiscoBootHwDiagsMIBTestEntry_Object((1,3,6,1,4,1,9,9,696,1,2,1))
ciscoBootHwDiagsMIBTestEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBTestEntry.setStatus(_A)
_CiscoBootHwDiagsMIBTestIndex_Type=Unsigned32
_CiscoBootHwDiagsMIBTestIndex_Object=MibTableColumn
ciscoBootHwDiagsMIBTestIndex=_CiscoBootHwDiagsMIBTestIndex_Object((1,3,6,1,4,1,9,9,696,1,2,1,1),_CiscoBootHwDiagsMIBTestIndex_Type())
ciscoBootHwDiagsMIBTestIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBTestIndex.setStatus(_A)
class _CiscoBootHwDiagsMIBTestName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,255))
_CiscoBootHwDiagsMIBTestName_Type.__name__=_H
_CiscoBootHwDiagsMIBTestName_Object=MibTableColumn
ciscoBootHwDiagsMIBTestName=_CiscoBootHwDiagsMIBTestName_Object((1,3,6,1,4,1,9,9,696,1,2,1,2),_CiscoBootHwDiagsMIBTestName_Type())
ciscoBootHwDiagsMIBTestName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBTestName.setStatus(_A)
_CiscoBootHwDiagsMIBTable_Object=MibTable
ciscoBootHwDiagsMIBTable=_CiscoBootHwDiagsMIBTable_Object((1,3,6,1,4,1,9,9,696,1,3))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBTable.setStatus(_A)
_CiscoBootHwDiagsMIBEntry_Object=MibTableRow
ciscoBootHwDiagsMIBEntry=_CiscoBootHwDiagsMIBEntry_Object((1,3,6,1,4,1,9,9,696,1,3,1))
ciscoBootHwDiagsMIBEntry.setIndexNames((0,_B,_J),(0,_B,_F))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBEntry.setStatus(_A)
class _CiscoBootHwDiagsMIBBankIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CiscoBootHwDiagsMIBBankIndex_Type.__name__=_D
_CiscoBootHwDiagsMIBBankIndex_Object=MibTableColumn
ciscoBootHwDiagsMIBBankIndex=_CiscoBootHwDiagsMIBBankIndex_Object((1,3,6,1,4,1,9,9,696,1,3,1,1),_CiscoBootHwDiagsMIBBankIndex_Type())
ciscoBootHwDiagsMIBBankIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBBankIndex.setStatus(_A)
class _CiscoBootHwDiagsMIBLastBootExecuted_Type(TruthValue):defaultValue=2
_CiscoBootHwDiagsMIBLastBootExecuted_Type.__name__=_E
_CiscoBootHwDiagsMIBLastBootExecuted_Object=MibTableColumn
ciscoBootHwDiagsMIBLastBootExecuted=_CiscoBootHwDiagsMIBLastBootExecuted_Object((1,3,6,1,4,1,9,9,696,1,3,1,2),_CiscoBootHwDiagsMIBLastBootExecuted_Type())
ciscoBootHwDiagsMIBLastBootExecuted.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBLastBootExecuted.setStatus(_A)
_CiscoBootHwDiagsMIBLastBootPassed_Type=TruthValue
_CiscoBootHwDiagsMIBLastBootPassed_Object=MibTableColumn
ciscoBootHwDiagsMIBLastBootPassed=_CiscoBootHwDiagsMIBLastBootPassed_Object((1,3,6,1,4,1,9,9,696,1,3,1,3),_CiscoBootHwDiagsMIBLastBootPassed_Type())
ciscoBootHwDiagsMIBLastBootPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBLastBootPassed.setStatus(_A)
class _CiscoBootHwDiagsMIBNextBootConfigured_Type(TruthValue):defaultValue=2
_CiscoBootHwDiagsMIBNextBootConfigured_Type.__name__=_E
_CiscoBootHwDiagsMIBNextBootConfigured_Object=MibTableColumn
ciscoBootHwDiagsMIBNextBootConfigured=_CiscoBootHwDiagsMIBNextBootConfigured_Object((1,3,6,1,4,1,9,9,696,1,3,1,4),_CiscoBootHwDiagsMIBNextBootConfigured_Type())
ciscoBootHwDiagsMIBNextBootConfigured.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBNextBootConfigured.setStatus(_A)
class _CiscoBootHwDiagsMIBNextBootArmed_Type(TruthValue):defaultValue=2
_CiscoBootHwDiagsMIBNextBootArmed_Type.__name__=_E
_CiscoBootHwDiagsMIBNextBootArmed_Object=MibTableColumn
ciscoBootHwDiagsMIBNextBootArmed=_CiscoBootHwDiagsMIBNextBootArmed_Object((1,3,6,1,4,1,9,9,696,1,3,1,5),_CiscoBootHwDiagsMIBNextBootArmed_Type())
ciscoBootHwDiagsMIBNextBootArmed.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBNextBootArmed.setStatus(_A)
class _CiscoBootHwDiagsMIBConfigCode_Type(Unsigned32):defaultValue=0
_CiscoBootHwDiagsMIBConfigCode_Type.__name__=_D
_CiscoBootHwDiagsMIBConfigCode_Object=MibTableColumn
ciscoBootHwDiagsMIBConfigCode=_CiscoBootHwDiagsMIBConfigCode_Object((1,3,6,1,4,1,9,9,696,1,3,1,6),_CiscoBootHwDiagsMIBConfigCode_Type())
ciscoBootHwDiagsMIBConfigCode.setMaxAccess(_G)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBConfigCode.setStatus(_A)
_CiscoBootHwDiagsMIBResultCode_Type=Unsigned32
_CiscoBootHwDiagsMIBResultCode_Object=MibTableColumn
ciscoBootHwDiagsMIBResultCode=_CiscoBootHwDiagsMIBResultCode_Object((1,3,6,1,4,1,9,9,696,1,3,1,7),_CiscoBootHwDiagsMIBResultCode_Type())
ciscoBootHwDiagsMIBResultCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBResultCode.setStatus(_A)
_CiscoBootHwDiagsMIBConform_ObjectIdentity=ObjectIdentity
ciscoBootHwDiagsMIBConform=_CiscoBootHwDiagsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,696,2))
_CiscoBootHwDiagsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBootHwDiagsMIBCompliances=_CiscoBootHwDiagsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,696,2,1))
_CiscoBootHwDiagsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBootHwDiagsMIBGroups=_CiscoBootHwDiagsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,696,2,2))
ciscoBootHwDiagsMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,696,2,2,1))
ciscoBootHwDiagsMIBMainObjectGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBMainObjectGroup.setStatus(_A)
ciscoBootHwDiagsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,696,2,1,1))
ciscoBootHwDiagsMIBCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:ciscoBootHwDiagsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoBootHwDiagsMIB':ciscoBootHwDiagsMIB,'ciscoBootHwDiagsMIBNotifs':ciscoBootHwDiagsMIBNotifs,'ciscoBootHwDiagsMIBObjects':ciscoBootHwDiagsMIBObjects,_K:ciscoBootHwDiagsMIBCurrentBank,'ciscoBootHwDiagsMIBTestTable':ciscoBootHwDiagsMIBTestTable,'ciscoBootHwDiagsMIBTestEntry':ciscoBootHwDiagsMIBTestEntry,_F:ciscoBootHwDiagsMIBTestIndex,_L:ciscoBootHwDiagsMIBTestName,'ciscoBootHwDiagsMIBTable':ciscoBootHwDiagsMIBTable,'ciscoBootHwDiagsMIBEntry':ciscoBootHwDiagsMIBEntry,_J:ciscoBootHwDiagsMIBBankIndex,_M:ciscoBootHwDiagsMIBLastBootExecuted,_N:ciscoBootHwDiagsMIBLastBootPassed,_O:ciscoBootHwDiagsMIBNextBootConfigured,_P:ciscoBootHwDiagsMIBNextBootArmed,_Q:ciscoBootHwDiagsMIBConfigCode,_R:ciscoBootHwDiagsMIBResultCode,'ciscoBootHwDiagsMIBConform':ciscoBootHwDiagsMIBConform,'ciscoBootHwDiagsMIBCompliances':ciscoBootHwDiagsMIBCompliances,'ciscoBootHwDiagsMIBCompliance':ciscoBootHwDiagsMIBCompliance,'ciscoBootHwDiagsMIBGroups':ciscoBootHwDiagsMIBGroups,_S:ciscoBootHwDiagsMIBMainObjectGroup})