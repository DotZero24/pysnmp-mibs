_U='hpnicfFcPsmLoginSWWN'
_T='hpnicfFcPsmLoginPWWN'
_S='hpnicfFcPsmViolationIndex'
_R='HpnicfFcPsmClearEntryType'
_Q='hpnicfFcPsmEnfIndex'
_P='hpnicfFcPsmIndex'
_O='hpnicfFcPsmLoginTime'
_N='hpnicfFcPsmLoginIntf'
_M='ifDescr'
_L='IF-MIB'
_K='read-create'
_J='not-accessible'
_I='noop'
_H='TruthValue'
_G='Unsigned32'
_F='Integer32'
_E='read-write'
_D='hpnicfFcPsmEnableVsanIndex'
_C='read-only'
_B='HPN-ICF-FC-PSM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcNameIdOrZero,=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcNameIdOrZero')
hpnicfSan,=mibBuilder.importSymbols('HPN-ICF-VSAN-MIB','hpnicfSan')
InterfaceIndex,InterfaceIndexOrZero,ifDescr=mibBuilder.importSymbols(_L,'InterfaceIndex','InterfaceIndexOrZero',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_H)
hpnicfFcPsm=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8))
if mibBuilder.loadTexts:hpnicfFcPsm.setRevisions(('2013-10-17 00:00',))
class HpnicfFcPsmPortBindDevType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nWWN',1),('pWWN',2),('sWWN',3),('wildCard',4)))
class HpnicfFcPsmClearEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clearStatic',1),('clearAutoLearn',2),('clearAll',3),(_I,4)))
_HpnicfFcPsmNotifications_ObjectIdentity=ObjectIdentity
hpnicfFcPsmNotifications=_HpnicfFcPsmNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8,0))
_HpnicfFcPsmObjects_ObjectIdentity=ObjectIdentity
hpnicfFcPsmObjects=_HpnicfFcPsmObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1))
_HpnicfFcPsmScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfFcPsmScalarObjects=_HpnicfFcPsmScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,1))
class _HpnicfFcPsmNotifyEnable_Type(TruthValue):defaultValue=2
_HpnicfFcPsmNotifyEnable_Type.__name__=_H
_HpnicfFcPsmNotifyEnable_Object=MibScalar
hpnicfFcPsmNotifyEnable=_HpnicfFcPsmNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,1,1),_HpnicfFcPsmNotifyEnable_Type())
hpnicfFcPsmNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmNotifyEnable.setStatus(_A)
_HpnicfFcPsmConfiguration_ObjectIdentity=ObjectIdentity
hpnicfFcPsmConfiguration=_HpnicfFcPsmConfiguration_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2))
_HpnicfFcPsmEnableTable_Object=MibTable
hpnicfFcPsmEnableTable=_HpnicfFcPsmEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,1))
if mibBuilder.loadTexts:hpnicfFcPsmEnableTable.setStatus(_A)
_HpnicfFcPsmEnableEntry_Object=MibTableRow
hpnicfFcPsmEnableEntry=_HpnicfFcPsmEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,1,1))
hpnicfFcPsmEnableEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfFcPsmEnableEntry.setStatus(_A)
class _HpnicfFcPsmEnableVsanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_HpnicfFcPsmEnableVsanIndex_Type.__name__=_G
_HpnicfFcPsmEnableVsanIndex_Object=MibTableColumn
hpnicfFcPsmEnableVsanIndex=_HpnicfFcPsmEnableVsanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,1,1,1),_HpnicfFcPsmEnableVsanIndex_Type())
hpnicfFcPsmEnableVsanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFcPsmEnableVsanIndex.setStatus(_A)
class _HpnicfFcPsmEnable_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enable',1),('enableWithAutoLearn',2),('disable',3),(_I,4)))
_HpnicfFcPsmEnable_Type.__name__=_F
_HpnicfFcPsmEnable_Object=MibTableColumn
hpnicfFcPsmEnable=_HpnicfFcPsmEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,1,1,2),_HpnicfFcPsmEnable_Type())
hpnicfFcPsmEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmEnable.setStatus(_A)
class _HpnicfFcPsmEnableState_Type(TruthValue):defaultValue=2
_HpnicfFcPsmEnableState_Type.__name__=_H
_HpnicfFcPsmEnableState_Object=MibTableColumn
hpnicfFcPsmEnableState=_HpnicfFcPsmEnableState_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,1,1,3),_HpnicfFcPsmEnableState_Type())
hpnicfFcPsmEnableState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmEnableState.setStatus(_A)
_HpnicfFcPsmConfigTable_Object=MibTable
hpnicfFcPsmConfigTable=_HpnicfFcPsmConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2))
if mibBuilder.loadTexts:hpnicfFcPsmConfigTable.setStatus(_A)
_HpnicfFcPsmConfigEntry_Object=MibTableRow
hpnicfFcPsmConfigEntry=_HpnicfFcPsmConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1))
hpnicfFcPsmConfigEntry.setIndexNames((0,_B,_D),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfFcPsmConfigEntry.setStatus(_A)
class _HpnicfFcPsmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_HpnicfFcPsmIndex_Type.__name__=_G
_HpnicfFcPsmIndex_Object=MibTableColumn
hpnicfFcPsmIndex=_HpnicfFcPsmIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1,1),_HpnicfFcPsmIndex_Type())
hpnicfFcPsmIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFcPsmIndex.setStatus(_A)
_HpnicfFcPsmLoginDevType_Type=HpnicfFcPsmPortBindDevType
_HpnicfFcPsmLoginDevType_Object=MibTableColumn
hpnicfFcPsmLoginDevType=_HpnicfFcPsmLoginDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1,2),_HpnicfFcPsmLoginDevType_Type())
hpnicfFcPsmLoginDevType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcPsmLoginDevType.setStatus(_A)
_HpnicfFcPsmLoginDev_Type=HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginDev_Object=MibTableColumn
hpnicfFcPsmLoginDev=_HpnicfFcPsmLoginDev_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1,3),_HpnicfFcPsmLoginDev_Type())
hpnicfFcPsmLoginDev.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcPsmLoginDev.setStatus(_A)
_HpnicfFcPsmLoginPoint_Type=InterfaceIndexOrZero
_HpnicfFcPsmLoginPoint_Object=MibTableColumn
hpnicfFcPsmLoginPoint=_HpnicfFcPsmLoginPoint_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1,4),_HpnicfFcPsmLoginPoint_Type())
hpnicfFcPsmLoginPoint.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcPsmLoginPoint.setStatus(_A)
_HpnicfFcPsmRowStatus_Type=RowStatus
_HpnicfFcPsmRowStatus_Object=MibTableColumn
hpnicfFcPsmRowStatus=_HpnicfFcPsmRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,2,1,5),_HpnicfFcPsmRowStatus_Type())
hpnicfFcPsmRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFcPsmRowStatus.setStatus(_A)
_HpnicfFcPsmEnfTable_Object=MibTable
hpnicfFcPsmEnfTable=_HpnicfFcPsmEnfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3))
if mibBuilder.loadTexts:hpnicfFcPsmEnfTable.setStatus(_A)
_HpnicfFcPsmEnfEntry_Object=MibTableRow
hpnicfFcPsmEnfEntry=_HpnicfFcPsmEnfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1))
hpnicfFcPsmEnfEntry.setIndexNames((0,_B,_D),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfFcPsmEnfEntry.setStatus(_A)
class _HpnicfFcPsmEnfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_HpnicfFcPsmEnfIndex_Type.__name__=_G
_HpnicfFcPsmEnfIndex_Object=MibTableColumn
hpnicfFcPsmEnfIndex=_HpnicfFcPsmEnfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1,1),_HpnicfFcPsmEnfIndex_Type())
hpnicfFcPsmEnfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFcPsmEnfIndex.setStatus(_A)
_HpnicfFcPsmEnfLoginDevType_Type=HpnicfFcPsmPortBindDevType
_HpnicfFcPsmEnfLoginDevType_Object=MibTableColumn
hpnicfFcPsmEnfLoginDevType=_HpnicfFcPsmEnfLoginDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1,2),_HpnicfFcPsmEnfLoginDevType_Type())
hpnicfFcPsmEnfLoginDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmEnfLoginDevType.setStatus(_A)
_HpnicfFcPsmEnfLoginDev_Type=HpnicfFcNameIdOrZero
_HpnicfFcPsmEnfLoginDev_Object=MibTableColumn
hpnicfFcPsmEnfLoginDev=_HpnicfFcPsmEnfLoginDev_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1,3),_HpnicfFcPsmEnfLoginDev_Type())
hpnicfFcPsmEnfLoginDev.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmEnfLoginDev.setStatus(_A)
_HpnicfFcPsmEnfLoginPoint_Type=InterfaceIndexOrZero
_HpnicfFcPsmEnfLoginPoint_Object=MibTableColumn
hpnicfFcPsmEnfLoginPoint=_HpnicfFcPsmEnfLoginPoint_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1,4),_HpnicfFcPsmEnfLoginPoint_Type())
hpnicfFcPsmEnfLoginPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmEnfLoginPoint.setStatus(_A)
class _HpnicfFcPsmEnfEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('learning',1),('learnt',2),('static',3)))
_HpnicfFcPsmEnfEntryType_Type.__name__=_F
_HpnicfFcPsmEnfEntryType_Object=MibTableColumn
hpnicfFcPsmEnfEntryType=_HpnicfFcPsmEnfEntryType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,3,1,5),_HpnicfFcPsmEnfEntryType_Type())
hpnicfFcPsmEnfEntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmEnfEntryType.setStatus(_A)
_HpnicfFcPsmCopyToConfigTable_Object=MibTable
hpnicfFcPsmCopyToConfigTable=_HpnicfFcPsmCopyToConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,4))
if mibBuilder.loadTexts:hpnicfFcPsmCopyToConfigTable.setStatus(_A)
_HpnicfFcPsmCopyToConfigEntry_Object=MibTableRow
hpnicfFcPsmCopyToConfigEntry=_HpnicfFcPsmCopyToConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,4,1))
hpnicfFcPsmCopyToConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfFcPsmCopyToConfigEntry.setStatus(_A)
class _HpnicfFcPsmCopyToConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copy',1),(_I,2)))
_HpnicfFcPsmCopyToConfig_Type.__name__=_F
_HpnicfFcPsmCopyToConfig_Object=MibTableColumn
hpnicfFcPsmCopyToConfig=_HpnicfFcPsmCopyToConfig_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,4,1,1),_HpnicfFcPsmCopyToConfig_Type())
hpnicfFcPsmCopyToConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmCopyToConfig.setStatus(_A)
_HpnicfFcPsmAutoLearnTable_Object=MibTable
hpnicfFcPsmAutoLearnTable=_HpnicfFcPsmAutoLearnTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,5))
if mibBuilder.loadTexts:hpnicfFcPsmAutoLearnTable.setStatus(_A)
_HpnicfFcPsmAutoLearnEntry_Object=MibTableRow
hpnicfFcPsmAutoLearnEntry=_HpnicfFcPsmAutoLearnEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,5,1))
hpnicfFcPsmAutoLearnEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfFcPsmAutoLearnEntry.setStatus(_A)
class _HpnicfFcPsmAutoLearnEnable_Type(TruthValue):defaultValue=2
_HpnicfFcPsmAutoLearnEnable_Type.__name__=_H
_HpnicfFcPsmAutoLearnEnable_Object=MibTableColumn
hpnicfFcPsmAutoLearnEnable=_HpnicfFcPsmAutoLearnEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,5,1,1),_HpnicfFcPsmAutoLearnEnable_Type())
hpnicfFcPsmAutoLearnEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmAutoLearnEnable.setStatus(_A)
_HpnicfFcPsmClearTable_Object=MibTable
hpnicfFcPsmClearTable=_HpnicfFcPsmClearTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,6))
if mibBuilder.loadTexts:hpnicfFcPsmClearTable.setStatus(_A)
_HpnicfFcPsmClearEntry_Object=MibTableRow
hpnicfFcPsmClearEntry=_HpnicfFcPsmClearEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,6,1))
hpnicfFcPsmClearEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfFcPsmClearEntry.setStatus(_A)
class _HpnicfFcPsmClearType_Type(HpnicfFcPsmClearEntryType):defaultValue=4
_HpnicfFcPsmClearType_Type.__name__=_R
_HpnicfFcPsmClearType_Object=MibTableColumn
hpnicfFcPsmClearType=_HpnicfFcPsmClearType_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,6,1,1),_HpnicfFcPsmClearType_Type())
hpnicfFcPsmClearType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmClearType.setStatus(_A)
_HpnicfFcPsmClearIntf_Type=InterfaceIndexOrZero
_HpnicfFcPsmClearIntf_Object=MibTableColumn
hpnicfFcPsmClearIntf=_HpnicfFcPsmClearIntf_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,2,6,1,2),_HpnicfFcPsmClearIntf_Type())
hpnicfFcPsmClearIntf.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmClearIntf.setStatus(_A)
_HpnicfFcPsmStats_ObjectIdentity=ObjectIdentity
hpnicfFcPsmStats=_HpnicfFcPsmStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3))
_HpnicfFcPsmStatsTable_Object=MibTable
hpnicfFcPsmStatsTable=_HpnicfFcPsmStatsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,1))
if mibBuilder.loadTexts:hpnicfFcPsmStatsTable.setStatus(_A)
_HpnicfFcPsmStatsEntry_Object=MibTableRow
hpnicfFcPsmStatsEntry=_HpnicfFcPsmStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,1,1))
hpnicfFcPsmStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfFcPsmStatsEntry.setStatus(_A)
_HpnicfFcPsmAllowedLogins_Type=Counter32
_HpnicfFcPsmAllowedLogins_Object=MibTableColumn
hpnicfFcPsmAllowedLogins=_HpnicfFcPsmAllowedLogins_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,1,1,1),_HpnicfFcPsmAllowedLogins_Type())
hpnicfFcPsmAllowedLogins.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmAllowedLogins.setStatus(_A)
_HpnicfFcPsmDeniedLogins_Type=Counter32
_HpnicfFcPsmDeniedLogins_Object=MibTableColumn
hpnicfFcPsmDeniedLogins=_HpnicfFcPsmDeniedLogins_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,1,1,2),_HpnicfFcPsmDeniedLogins_Type())
hpnicfFcPsmDeniedLogins.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmDeniedLogins.setStatus(_A)
class _HpnicfFcPsmStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),(_I,2)))
_HpnicfFcPsmStatsClear_Type.__name__=_F
_HpnicfFcPsmStatsClear_Object=MibTableColumn
hpnicfFcPsmStatsClear=_HpnicfFcPsmStatsClear_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,1,1,3),_HpnicfFcPsmStatsClear_Type())
hpnicfFcPsmStatsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFcPsmStatsClear.setStatus(_A)
_HpnicfFcPsmViolationTable_Object=MibTable
hpnicfFcPsmViolationTable=_HpnicfFcPsmViolationTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2))
if mibBuilder.loadTexts:hpnicfFcPsmViolationTable.setStatus(_A)
_HpnicfFcPsmViolationEntry_Object=MibTableRow
hpnicfFcPsmViolationEntry=_HpnicfFcPsmViolationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1))
hpnicfFcPsmViolationEntry.setIndexNames((0,_B,_D),(0,_B,_S))
if mibBuilder.loadTexts:hpnicfFcPsmViolationEntry.setStatus(_A)
class _HpnicfFcPsmViolationIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfFcPsmViolationIndex_Type.__name__=_G
_HpnicfFcPsmViolationIndex_Object=MibTableColumn
hpnicfFcPsmViolationIndex=_HpnicfFcPsmViolationIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,1),_HpnicfFcPsmViolationIndex_Type())
hpnicfFcPsmViolationIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFcPsmViolationIndex.setStatus(_A)
_HpnicfFcPsmLoginPWWN_Type=HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginPWWN_Object=MibTableColumn
hpnicfFcPsmLoginPWWN=_HpnicfFcPsmLoginPWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,2),_HpnicfFcPsmLoginPWWN_Type())
hpnicfFcPsmLoginPWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginPWWN.setStatus(_A)
_HpnicfFcPsmLoginNWWN_Type=HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginNWWN_Object=MibTableColumn
hpnicfFcPsmLoginNWWN=_HpnicfFcPsmLoginNWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,3),_HpnicfFcPsmLoginNWWN_Type())
hpnicfFcPsmLoginNWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginNWWN.setStatus(_A)
_HpnicfFcPsmLoginSWWN_Type=HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginSWWN_Object=MibTableColumn
hpnicfFcPsmLoginSWWN=_HpnicfFcPsmLoginSWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,4),_HpnicfFcPsmLoginSWWN_Type())
hpnicfFcPsmLoginSWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginSWWN.setStatus(_A)
_HpnicfFcPsmLoginIntf_Type=InterfaceIndex
_HpnicfFcPsmLoginIntf_Object=MibTableColumn
hpnicfFcPsmLoginIntf=_HpnicfFcPsmLoginIntf_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,5),_HpnicfFcPsmLoginIntf_Type())
hpnicfFcPsmLoginIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginIntf.setStatus(_A)
_HpnicfFcPsmLoginTime_Type=TimeStamp
_HpnicfFcPsmLoginTime_Object=MibTableColumn
hpnicfFcPsmLoginTime=_HpnicfFcPsmLoginTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,6),_HpnicfFcPsmLoginTime_Type())
hpnicfFcPsmLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginTime.setStatus(_A)
_HpnicfFcPsmLoginCount_Type=Counter32
_HpnicfFcPsmLoginCount_Object=MibTableColumn
hpnicfFcPsmLoginCount=_HpnicfFcPsmLoginCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,8,1,3,2,1,7),_HpnicfFcPsmLoginCount_Type())
hpnicfFcPsmLoginCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFcPsmLoginCount.setStatus(_A)
hpnicfFcPsmFPortDenyNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,8,0,1))
hpnicfFcPsmFPortDenyNotify.setObjects(*((_L,_M),(_B,_T),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpnicfFcPsmFPortDenyNotify.setStatus(_A)
hpnicfFcPsmEPortDenyNotify=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,8,0,2))
hpnicfFcPsmEPortDenyNotify.setObjects(*((_L,_M),(_B,_U),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpnicfFcPsmEPortDenyNotify.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfFcPsmPortBindDevType':HpnicfFcPsmPortBindDevType,_R:HpnicfFcPsmClearEntryType,'hpnicfFcPsm':hpnicfFcPsm,'hpnicfFcPsmNotifications':hpnicfFcPsmNotifications,'hpnicfFcPsmFPortDenyNotify':hpnicfFcPsmFPortDenyNotify,'hpnicfFcPsmEPortDenyNotify':hpnicfFcPsmEPortDenyNotify,'hpnicfFcPsmObjects':hpnicfFcPsmObjects,'hpnicfFcPsmScalarObjects':hpnicfFcPsmScalarObjects,'hpnicfFcPsmNotifyEnable':hpnicfFcPsmNotifyEnable,'hpnicfFcPsmConfiguration':hpnicfFcPsmConfiguration,'hpnicfFcPsmEnableTable':hpnicfFcPsmEnableTable,'hpnicfFcPsmEnableEntry':hpnicfFcPsmEnableEntry,_D:hpnicfFcPsmEnableVsanIndex,'hpnicfFcPsmEnable':hpnicfFcPsmEnable,'hpnicfFcPsmEnableState':hpnicfFcPsmEnableState,'hpnicfFcPsmConfigTable':hpnicfFcPsmConfigTable,'hpnicfFcPsmConfigEntry':hpnicfFcPsmConfigEntry,_P:hpnicfFcPsmIndex,'hpnicfFcPsmLoginDevType':hpnicfFcPsmLoginDevType,'hpnicfFcPsmLoginDev':hpnicfFcPsmLoginDev,'hpnicfFcPsmLoginPoint':hpnicfFcPsmLoginPoint,'hpnicfFcPsmRowStatus':hpnicfFcPsmRowStatus,'hpnicfFcPsmEnfTable':hpnicfFcPsmEnfTable,'hpnicfFcPsmEnfEntry':hpnicfFcPsmEnfEntry,_Q:hpnicfFcPsmEnfIndex,'hpnicfFcPsmEnfLoginDevType':hpnicfFcPsmEnfLoginDevType,'hpnicfFcPsmEnfLoginDev':hpnicfFcPsmEnfLoginDev,'hpnicfFcPsmEnfLoginPoint':hpnicfFcPsmEnfLoginPoint,'hpnicfFcPsmEnfEntryType':hpnicfFcPsmEnfEntryType,'hpnicfFcPsmCopyToConfigTable':hpnicfFcPsmCopyToConfigTable,'hpnicfFcPsmCopyToConfigEntry':hpnicfFcPsmCopyToConfigEntry,'hpnicfFcPsmCopyToConfig':hpnicfFcPsmCopyToConfig,'hpnicfFcPsmAutoLearnTable':hpnicfFcPsmAutoLearnTable,'hpnicfFcPsmAutoLearnEntry':hpnicfFcPsmAutoLearnEntry,'hpnicfFcPsmAutoLearnEnable':hpnicfFcPsmAutoLearnEnable,'hpnicfFcPsmClearTable':hpnicfFcPsmClearTable,'hpnicfFcPsmClearEntry':hpnicfFcPsmClearEntry,'hpnicfFcPsmClearType':hpnicfFcPsmClearType,'hpnicfFcPsmClearIntf':hpnicfFcPsmClearIntf,'hpnicfFcPsmStats':hpnicfFcPsmStats,'hpnicfFcPsmStatsTable':hpnicfFcPsmStatsTable,'hpnicfFcPsmStatsEntry':hpnicfFcPsmStatsEntry,'hpnicfFcPsmAllowedLogins':hpnicfFcPsmAllowedLogins,'hpnicfFcPsmDeniedLogins':hpnicfFcPsmDeniedLogins,'hpnicfFcPsmStatsClear':hpnicfFcPsmStatsClear,'hpnicfFcPsmViolationTable':hpnicfFcPsmViolationTable,'hpnicfFcPsmViolationEntry':hpnicfFcPsmViolationEntry,_S:hpnicfFcPsmViolationIndex,_T:hpnicfFcPsmLoginPWWN,'hpnicfFcPsmLoginNWWN':hpnicfFcPsmLoginNWWN,_U:hpnicfFcPsmLoginSWWN,_N:hpnicfFcPsmLoginIntf,_O:hpnicfFcPsmLoginTime,'hpnicfFcPsmLoginCount':hpnicfFcPsmLoginCount})