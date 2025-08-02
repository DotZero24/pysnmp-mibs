_K='ctChasFanModuleNum'
_J='installedAndNotOperating'
_I='installedAndOperating'
_H='notInstalled'
_G='infoNotAvailable'
_F='ctChasPowerSupplyNum'
_E='CTRON-CHASSIS-MIB'
_D='notSupported'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctronChassis,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctronChassis')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtChas_ObjectIdentity=ObjectIdentity
ctChas=_CtChas_ObjectIdentity((1,3,6,1,4,1,52,4,3,1,1))
class _CtChasFNB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absent',1),('present',2)))
_CtChasFNB_Type.__name__=_B
_CtChasFNB_Object=MibScalar
ctChasFNB=_CtChasFNB_Object((1,3,6,1,4,1,52,4,3,1,1,1),_CtChasFNB_Type())
ctChasFNB.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasFNB.setStatus(_A)
class _CtChasAlarmEna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('enable',2),(_D,3)))
_CtChasAlarmEna_Type.__name__=_B
_CtChasAlarmEna_Object=MibScalar
ctChasAlarmEna=_CtChasAlarmEna_Object((1,3,6,1,4,1,52,4,3,1,1,2),_CtChasAlarmEna_Type())
ctChasAlarmEna.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctChasAlarmEna.setStatus(_A)
class _ChassisAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chassisNoFaultCondition',1),('chassisFaultCondition',2),(_D,3)))
_ChassisAlarmState_Type.__name__=_B
_ChassisAlarmState_Object=MibScalar
chassisAlarmState=_ChassisAlarmState_Object((1,3,6,1,4,1,52,4,3,1,1,3),_ChassisAlarmState_Type())
chassisAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:chassisAlarmState.setStatus(_A)
_CtEnviron_ObjectIdentity=ObjectIdentity
ctEnviron=_CtEnviron_ObjectIdentity((1,3,6,1,4,1,52,4,3,1,2))
_CtChasPowerTable_Object=MibTable
ctChasPowerTable=_CtChasPowerTable_Object((1,3,6,1,4,1,52,4,3,1,2,1))
if mibBuilder.loadTexts:ctChasPowerTable.setStatus(_A)
_CtChasPowerEntry_Object=MibTableRow
ctChasPowerEntry=_CtChasPowerEntry_Object((1,3,6,1,4,1,52,4,3,1,2,1,1))
ctChasPowerEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ctChasPowerEntry.setStatus(_A)
_CtChasPowerSupplyNum_Type=Integer32
_CtChasPowerSupplyNum_Object=MibTableColumn
ctChasPowerSupplyNum=_CtChasPowerSupplyNum_Object((1,3,6,1,4,1,52,4,3,1,2,1,1,1),_CtChasPowerSupplyNum_Type())
ctChasPowerSupplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasPowerSupplyNum.setStatus(_A)
class _CtChasPowerSupplyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_CtChasPowerSupplyState_Type.__name__=_B
_CtChasPowerSupplyState_Object=MibTableColumn
ctChasPowerSupplyState=_CtChasPowerSupplyState_Object((1,3,6,1,4,1,52,4,3,1,2,1,1,2),_CtChasPowerSupplyState_Type())
ctChasPowerSupplyState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasPowerSupplyState.setStatus(_A)
class _CtChasPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ac-dc',1),('dc-dc',2),(_D,3),('highOutput',4)))
_CtChasPowerSupplyType_Type.__name__=_B
_CtChasPowerSupplyType_Object=MibTableColumn
ctChasPowerSupplyType=_CtChasPowerSupplyType_Object((1,3,6,1,4,1,52,4,3,1,2,1,1,3),_CtChasPowerSupplyType_Type())
ctChasPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasPowerSupplyType.setStatus(_A)
class _CtChasPowerSupplyRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('redundant',1),('notRedundant',2),(_D,3)))
_CtChasPowerSupplyRedundancy_Type.__name__=_B
_CtChasPowerSupplyRedundancy_Object=MibTableColumn
ctChasPowerSupplyRedundancy=_CtChasPowerSupplyRedundancy_Object((1,3,6,1,4,1,52,4,3,1,2,1,1,4),_CtChasPowerSupplyRedundancy_Type())
ctChasPowerSupplyRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasPowerSupplyRedundancy.setStatus(_A)
_CtFanModule_ObjectIdentity=ObjectIdentity
ctFanModule=_CtFanModule_ObjectIdentity((1,3,6,1,4,1,52,4,3,1,3))
_CtChasFanModuleTable_Object=MibTable
ctChasFanModuleTable=_CtChasFanModuleTable_Object((1,3,6,1,4,1,52,4,3,1,3,1))
if mibBuilder.loadTexts:ctChasFanModuleTable.setStatus(_A)
_CtChasFanModuleEntry_Object=MibTableRow
ctChasFanModuleEntry=_CtChasFanModuleEntry_Object((1,3,6,1,4,1,52,4,3,1,3,1,1))
ctChasFanModuleEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:ctChasFanModuleEntry.setStatus(_A)
_CtChasFanModuleNum_Type=Integer32
_CtChasFanModuleNum_Object=MibTableColumn
ctChasFanModuleNum=_CtChasFanModuleNum_Object((1,3,6,1,4,1,52,4,3,1,3,1,1,1),_CtChasFanModuleNum_Type())
ctChasFanModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasFanModuleNum.setStatus(_A)
class _CtChasFanModuleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_CtChasFanModuleState_Type.__name__=_B
_CtChasFanModuleState_Object=MibTableColumn
ctChasFanModuleState=_CtChasFanModuleState_Object((1,3,6,1,4,1,52,4,3,1,3,1,1,2),_CtChasFanModuleState_Type())
ctChasFanModuleState.setMaxAccess(_C)
if mibBuilder.loadTexts:ctChasFanModuleState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ctChas':ctChas,'ctChasFNB':ctChasFNB,'ctChasAlarmEna':ctChasAlarmEna,'chassisAlarmState':chassisAlarmState,'ctEnviron':ctEnviron,'ctChasPowerTable':ctChasPowerTable,'ctChasPowerEntry':ctChasPowerEntry,_F:ctChasPowerSupplyNum,'ctChasPowerSupplyState':ctChasPowerSupplyState,'ctChasPowerSupplyType':ctChasPowerSupplyType,'ctChasPowerSupplyRedundancy':ctChasPowerSupplyRedundancy,'ctFanModule':ctFanModule,'ctChasFanModuleTable':ctChasFanModuleTable,'ctChasFanModuleEntry':ctChasFanModuleEntry,_K:ctChasFanModuleNum,'ctChasFanModuleState':ctChasFanModuleState})