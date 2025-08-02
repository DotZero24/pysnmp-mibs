_J='hpnicfMplsPsIndex'
_I='TruthValue'
_H='hpnicfMplsPsSwitchResult'
_G='hpnicfMplsPsProtectLspName'
_F='hpnicfMplsPsWorkLspName'
_E='read-only'
_D='read-create'
_C='HPN-ICF-MPLSOAM-PS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfMplsOamPs=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,80))
_HpnicfMplsOamPsScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfMplsOamPsScalarGroup=_HpnicfMplsOamPsScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,80,1))
class _HpnicfMplsOamPsTrapOpen_Type(TruthValue):defaultValue=2
_HpnicfMplsOamPsTrapOpen_Type.__name__=_I
_HpnicfMplsOamPsTrapOpen_Object=MibScalar
hpnicfMplsOamPsTrapOpen=_HpnicfMplsOamPsTrapOpen_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,1,1),_HpnicfMplsOamPsTrapOpen_Type())
hpnicfMplsOamPsTrapOpen.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfMplsOamPsTrapOpen.setStatus(_A)
_HpnicfMplsOamPsTable_ObjectIdentity=ObjectIdentity
hpnicfMplsOamPsTable=_HpnicfMplsOamPsTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,80,2))
_HpnicfMplsPsTable_Object=MibTable
hpnicfMplsPsTable=_HpnicfMplsPsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1))
if mibBuilder.loadTexts:hpnicfMplsPsTable.setStatus(_A)
_HpnicfMplsPsEntry_Object=MibTableRow
hpnicfMplsPsEntry=_HpnicfMplsPsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1))
hpnicfMplsPsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:hpnicfMplsPsEntry.setStatus(_A)
_HpnicfMplsPsIndex_Type=Integer32
_HpnicfMplsPsIndex_Object=MibTableColumn
hpnicfMplsPsIndex=_HpnicfMplsPsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,1),_HpnicfMplsPsIndex_Type())
hpnicfMplsPsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfMplsPsIndex.setStatus(_A)
_HpnicfMplsPsGroupID_Type=Integer32
_HpnicfMplsPsGroupID_Object=MibTableColumn
hpnicfMplsPsGroupID=_HpnicfMplsPsGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,2),_HpnicfMplsPsGroupID_Type())
hpnicfMplsPsGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsGroupID.setStatus(_A)
_HpnicfMplsPsWorkLspName_Type=OctetString
_HpnicfMplsPsWorkLspName_Object=MibTableColumn
hpnicfMplsPsWorkLspName=_HpnicfMplsPsWorkLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,3),_HpnicfMplsPsWorkLspName_Type())
hpnicfMplsPsWorkLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsWorkLspName.setStatus(_A)
_HpnicfMplsPsProtectLspName_Type=OctetString
_HpnicfMplsPsProtectLspName_Object=MibTableColumn
hpnicfMplsPsProtectLspName=_HpnicfMplsPsProtectLspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,4),_HpnicfMplsPsProtectLspName_Type())
hpnicfMplsPsProtectLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsProtectLspName.setStatus(_A)
class _HpnicfMplsPsRevertiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsRevertiveMode_Type.__name__=_B
_HpnicfMplsPsRevertiveMode_Object=MibTableColumn
hpnicfMplsPsRevertiveMode=_HpnicfMplsPsRevertiveMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,5),_HpnicfMplsPsRevertiveMode_Type())
hpnicfMplsPsRevertiveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsRevertiveMode.setStatus(_A)
_HpnicfMplsPsWTR_Type=Integer32
_HpnicfMplsPsWTR_Object=MibTableColumn
hpnicfMplsPsWTR=_HpnicfMplsPsWTR_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,6),_HpnicfMplsPsWTR_Type())
hpnicfMplsPsWTR.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsWTR.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsPsWTR.setUnits('30s')
_HpnicfMplsPsHoldOff_Type=Integer32
_HpnicfMplsPsHoldOff_Object=MibTableColumn
hpnicfMplsPsHoldOff=_HpnicfMplsPsHoldOff_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,7),_HpnicfMplsPsHoldOff_Type())
hpnicfMplsPsHoldOff.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsHoldOff.setStatus(_A)
if mibBuilder.loadTexts:hpnicfMplsPsHoldOff.setUnits('100ms')
class _HpnicfMplsPsSwitchCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_HpnicfMplsPsSwitchCondition_Type.__name__=_B
_HpnicfMplsPsSwitchCondition_Object=MibTableColumn
hpnicfMplsPsSwitchCondition=_HpnicfMplsPsSwitchCondition_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,8),_HpnicfMplsPsSwitchCondition_Type())
hpnicfMplsPsSwitchCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsSwitchCondition.setStatus(_A)
class _HpnicfMplsPsWorkLspDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsWorkLspDetectState_Type.__name__=_B
_HpnicfMplsPsWorkLspDetectState_Object=MibTableColumn
hpnicfMplsPsWorkLspDetectState=_HpnicfMplsPsWorkLspDetectState_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,9),_HpnicfMplsPsWorkLspDetectState_Type())
hpnicfMplsPsWorkLspDetectState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMplsPsWorkLspDetectState.setStatus(_A)
class _HpnicfMplsPsWorkLspUpDownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsWorkLspUpDownState_Type.__name__=_B
_HpnicfMplsPsWorkLspUpDownState_Object=MibTableColumn
hpnicfMplsPsWorkLspUpDownState=_HpnicfMplsPsWorkLspUpDownState_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,10),_HpnicfMplsPsWorkLspUpDownState_Type())
hpnicfMplsPsWorkLspUpDownState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMplsPsWorkLspUpDownState.setStatus(_A)
class _HpnicfMplsPsProtLspDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsProtLspDetectState_Type.__name__=_B
_HpnicfMplsPsProtLspDetectState_Object=MibTableColumn
hpnicfMplsPsProtLspDetectState=_HpnicfMplsPsProtLspDetectState_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,11),_HpnicfMplsPsProtLspDetectState_Type())
hpnicfMplsPsProtLspDetectState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMplsPsProtLspDetectState.setStatus(_A)
class _HpnicfMplsPsProtLspUpDownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsProtLspUpDownState_Type.__name__=_B
_HpnicfMplsPsProtLspUpDownState_Object=MibTableColumn
hpnicfMplsPsProtLspUpDownState=_HpnicfMplsPsProtLspUpDownState_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,12),_HpnicfMplsPsProtLspUpDownState_Type())
hpnicfMplsPsProtLspUpDownState.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMplsPsProtLspUpDownState.setStatus(_A)
class _HpnicfMplsPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_HpnicfMplsPsSwitchResult_Type.__name__=_B
_HpnicfMplsPsSwitchResult_Object=MibTableColumn
hpnicfMplsPsSwitchResult=_HpnicfMplsPsSwitchResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,13),_HpnicfMplsPsSwitchResult_Type())
hpnicfMplsPsSwitchResult.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMplsPsSwitchResult.setStatus(_A)
_HpnicfMplsPsRowStatus_Type=RowStatus
_HpnicfMplsPsRowStatus_Object=MibTableColumn
hpnicfMplsPsRowStatus=_HpnicfMplsPsRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,80,2,1,1,14),_HpnicfMplsPsRowStatus_Type())
hpnicfMplsPsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMplsPsRowStatus.setStatus(_A)
_HpnicfMplsOamPsNotifications_ObjectIdentity=ObjectIdentity
hpnicfMplsOamPsNotifications=_HpnicfMplsOamPsNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,80,3))
hpnicfMplsPsSwitchPtoW=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,80,3,1))
hpnicfMplsPsSwitchPtoW.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:hpnicfMplsPsSwitchPtoW.setStatus(_A)
hpnicfMplsPsSwitchWtoP=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,80,3,2))
hpnicfMplsPsSwitchWtoP.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:hpnicfMplsPsSwitchWtoP.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfMplsOamPs':hpnicfMplsOamPs,'hpnicfMplsOamPsScalarGroup':hpnicfMplsOamPsScalarGroup,'hpnicfMplsOamPsTrapOpen':hpnicfMplsOamPsTrapOpen,'hpnicfMplsOamPsTable':hpnicfMplsOamPsTable,'hpnicfMplsPsTable':hpnicfMplsPsTable,'hpnicfMplsPsEntry':hpnicfMplsPsEntry,_J:hpnicfMplsPsIndex,'hpnicfMplsPsGroupID':hpnicfMplsPsGroupID,_F:hpnicfMplsPsWorkLspName,_G:hpnicfMplsPsProtectLspName,'hpnicfMplsPsRevertiveMode':hpnicfMplsPsRevertiveMode,'hpnicfMplsPsWTR':hpnicfMplsPsWTR,'hpnicfMplsPsHoldOff':hpnicfMplsPsHoldOff,'hpnicfMplsPsSwitchCondition':hpnicfMplsPsSwitchCondition,'hpnicfMplsPsWorkLspDetectState':hpnicfMplsPsWorkLspDetectState,'hpnicfMplsPsWorkLspUpDownState':hpnicfMplsPsWorkLspUpDownState,'hpnicfMplsPsProtLspDetectState':hpnicfMplsPsProtLspDetectState,'hpnicfMplsPsProtLspUpDownState':hpnicfMplsPsProtLspUpDownState,_H:hpnicfMplsPsSwitchResult,'hpnicfMplsPsRowStatus':hpnicfMplsPsRowStatus,'hpnicfMplsOamPsNotifications':hpnicfMplsOamPsNotifications,'hpnicfMplsPsSwitchPtoW':hpnicfMplsPsSwitchPtoW,'hpnicfMplsPsSwitchWtoP':hpnicfMplsPsSwitchWtoP})