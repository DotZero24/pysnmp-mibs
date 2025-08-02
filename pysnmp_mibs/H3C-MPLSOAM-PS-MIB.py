_J='h3cMplsPsIndex'
_I='TruthValue'
_H='h3cMplsPsSwitchResult'
_G='h3cMplsPsProtectLspName'
_F='h3cMplsPsWorkLspName'
_E='read-only'
_D='read-create'
_C='H3C-MPLSOAM-PS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
h3cMplsOamPs=ModuleIdentity((1,3,6,1,4,1,2011,10,2,80))
_H3cMplsOamPsScalarGroup_ObjectIdentity=ObjectIdentity
h3cMplsOamPsScalarGroup=_H3cMplsOamPsScalarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,80,1))
class _H3cMplsOamPsTrapOpen_Type(TruthValue):defaultValue=2
_H3cMplsOamPsTrapOpen_Type.__name__=_I
_H3cMplsOamPsTrapOpen_Object=MibScalar
h3cMplsOamPsTrapOpen=_H3cMplsOamPsTrapOpen_Object((1,3,6,1,4,1,2011,10,2,80,1,1),_H3cMplsOamPsTrapOpen_Type())
h3cMplsOamPsTrapOpen.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cMplsOamPsTrapOpen.setStatus(_A)
_H3cMplsOamPsTable_ObjectIdentity=ObjectIdentity
h3cMplsOamPsTable=_H3cMplsOamPsTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,80,2))
_H3cMplsPsTable_Object=MibTable
h3cMplsPsTable=_H3cMplsPsTable_Object((1,3,6,1,4,1,2011,10,2,80,2,1))
if mibBuilder.loadTexts:h3cMplsPsTable.setStatus(_A)
_H3cMplsPsEntry_Object=MibTableRow
h3cMplsPsEntry=_H3cMplsPsEntry_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1))
h3cMplsPsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:h3cMplsPsEntry.setStatus(_A)
_H3cMplsPsIndex_Type=Integer32
_H3cMplsPsIndex_Object=MibTableColumn
h3cMplsPsIndex=_H3cMplsPsIndex_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,1),_H3cMplsPsIndex_Type())
h3cMplsPsIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cMplsPsIndex.setStatus(_A)
_H3cMplsPsGroupID_Type=Integer32
_H3cMplsPsGroupID_Object=MibTableColumn
h3cMplsPsGroupID=_H3cMplsPsGroupID_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,2),_H3cMplsPsGroupID_Type())
h3cMplsPsGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsGroupID.setStatus(_A)
_H3cMplsPsWorkLspName_Type=OctetString
_H3cMplsPsWorkLspName_Object=MibTableColumn
h3cMplsPsWorkLspName=_H3cMplsPsWorkLspName_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,3),_H3cMplsPsWorkLspName_Type())
h3cMplsPsWorkLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsWorkLspName.setStatus(_A)
_H3cMplsPsProtectLspName_Type=OctetString
_H3cMplsPsProtectLspName_Object=MibTableColumn
h3cMplsPsProtectLspName=_H3cMplsPsProtectLspName_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,4),_H3cMplsPsProtectLspName_Type())
h3cMplsPsProtectLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsProtectLspName.setStatus(_A)
class _H3cMplsPsRevertiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsRevertiveMode_Type.__name__=_B
_H3cMplsPsRevertiveMode_Object=MibTableColumn
h3cMplsPsRevertiveMode=_H3cMplsPsRevertiveMode_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,5),_H3cMplsPsRevertiveMode_Type())
h3cMplsPsRevertiveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsRevertiveMode.setStatus(_A)
_H3cMplsPsWTR_Type=Integer32
_H3cMplsPsWTR_Object=MibTableColumn
h3cMplsPsWTR=_H3cMplsPsWTR_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,6),_H3cMplsPsWTR_Type())
h3cMplsPsWTR.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsWTR.setStatus(_A)
if mibBuilder.loadTexts:h3cMplsPsWTR.setUnits('30s')
_H3cMplsPsHoldOff_Type=Integer32
_H3cMplsPsHoldOff_Object=MibTableColumn
h3cMplsPsHoldOff=_H3cMplsPsHoldOff_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,7),_H3cMplsPsHoldOff_Type())
h3cMplsPsHoldOff.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsHoldOff.setStatus(_A)
if mibBuilder.loadTexts:h3cMplsPsHoldOff.setUnits('100ms')
class _H3cMplsPsSwitchCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_H3cMplsPsSwitchCondition_Type.__name__=_B
_H3cMplsPsSwitchCondition_Object=MibTableColumn
h3cMplsPsSwitchCondition=_H3cMplsPsSwitchCondition_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,8),_H3cMplsPsSwitchCondition_Type())
h3cMplsPsSwitchCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsSwitchCondition.setStatus(_A)
class _H3cMplsPsWorkLspDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsWorkLspDetectState_Type.__name__=_B
_H3cMplsPsWorkLspDetectState_Object=MibTableColumn
h3cMplsPsWorkLspDetectState=_H3cMplsPsWorkLspDetectState_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,9),_H3cMplsPsWorkLspDetectState_Type())
h3cMplsPsWorkLspDetectState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMplsPsWorkLspDetectState.setStatus(_A)
class _H3cMplsPsWorkLspUpDownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsWorkLspUpDownState_Type.__name__=_B
_H3cMplsPsWorkLspUpDownState_Object=MibTableColumn
h3cMplsPsWorkLspUpDownState=_H3cMplsPsWorkLspUpDownState_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,10),_H3cMplsPsWorkLspUpDownState_Type())
h3cMplsPsWorkLspUpDownState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMplsPsWorkLspUpDownState.setStatus(_A)
class _H3cMplsPsProtLspDetectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsProtLspDetectState_Type.__name__=_B
_H3cMplsPsProtLspDetectState_Object=MibTableColumn
h3cMplsPsProtLspDetectState=_H3cMplsPsProtLspDetectState_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,11),_H3cMplsPsProtLspDetectState_Type())
h3cMplsPsProtLspDetectState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMplsPsProtLspDetectState.setStatus(_A)
class _H3cMplsPsProtLspUpDownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsProtLspUpDownState_Type.__name__=_B
_H3cMplsPsProtLspUpDownState_Object=MibTableColumn
h3cMplsPsProtLspUpDownState=_H3cMplsPsProtLspUpDownState_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,12),_H3cMplsPsProtLspUpDownState_Type())
h3cMplsPsProtLspUpDownState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMplsPsProtLspUpDownState.setStatus(_A)
class _H3cMplsPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_H3cMplsPsSwitchResult_Type.__name__=_B
_H3cMplsPsSwitchResult_Object=MibTableColumn
h3cMplsPsSwitchResult=_H3cMplsPsSwitchResult_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,13),_H3cMplsPsSwitchResult_Type())
h3cMplsPsSwitchResult.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMplsPsSwitchResult.setStatus(_A)
_H3cMplsPsRowStatus_Type=RowStatus
_H3cMplsPsRowStatus_Object=MibTableColumn
h3cMplsPsRowStatus=_H3cMplsPsRowStatus_Object((1,3,6,1,4,1,2011,10,2,80,2,1,1,14),_H3cMplsPsRowStatus_Type())
h3cMplsPsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMplsPsRowStatus.setStatus(_A)
_H3cMplsOamPsNotifications_ObjectIdentity=ObjectIdentity
h3cMplsOamPsNotifications=_H3cMplsOamPsNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,80,3))
h3cMplsPsSwitchPtoW=NotificationType((1,3,6,1,4,1,2011,10,2,80,3,1))
h3cMplsPsSwitchPtoW.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:h3cMplsPsSwitchPtoW.setStatus(_A)
h3cMplsPsSwitchWtoP=NotificationType((1,3,6,1,4,1,2011,10,2,80,3,2))
h3cMplsPsSwitchWtoP.setObjects(*((_C,_F),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:h3cMplsPsSwitchWtoP.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cMplsOamPs':h3cMplsOamPs,'h3cMplsOamPsScalarGroup':h3cMplsOamPsScalarGroup,'h3cMplsOamPsTrapOpen':h3cMplsOamPsTrapOpen,'h3cMplsOamPsTable':h3cMplsOamPsTable,'h3cMplsPsTable':h3cMplsPsTable,'h3cMplsPsEntry':h3cMplsPsEntry,_J:h3cMplsPsIndex,'h3cMplsPsGroupID':h3cMplsPsGroupID,_F:h3cMplsPsWorkLspName,_G:h3cMplsPsProtectLspName,'h3cMplsPsRevertiveMode':h3cMplsPsRevertiveMode,'h3cMplsPsWTR':h3cMplsPsWTR,'h3cMplsPsHoldOff':h3cMplsPsHoldOff,'h3cMplsPsSwitchCondition':h3cMplsPsSwitchCondition,'h3cMplsPsWorkLspDetectState':h3cMplsPsWorkLspDetectState,'h3cMplsPsWorkLspUpDownState':h3cMplsPsWorkLspUpDownState,'h3cMplsPsProtLspDetectState':h3cMplsPsProtLspDetectState,'h3cMplsPsProtLspUpDownState':h3cMplsPsProtLspUpDownState,_H:h3cMplsPsSwitchResult,'h3cMplsPsRowStatus':h3cMplsPsRowStatus,'h3cMplsOamPsNotifications':h3cMplsOamPsNotifications,'h3cMplsPsSwitchPtoW':h3cMplsPsSwitchPtoW,'h3cMplsPsSwitchWtoP':h3cMplsPsSwitchWtoP})