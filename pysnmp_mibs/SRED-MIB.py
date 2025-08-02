_Q='swDscpMapCtrlDscpIndex'
_P='swDscpMapCtrlPortIndex'
_O='swDscpTrustPortCtrlPortIndex'
_N='yellow'
_M='sw8021pColorMapCtrlPriorityIndex'
_L='sw8021pColorMapCtrlPortIndex'
_K='swSredCtrlClassIndex'
_J='swSredCtrlPortIndex'
_I='swSredPortIndex'
_H='disabled'
_G='enabled'
_F='SRED-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swSredMIB=ModuleIdentity((1,3,6,1,4,1,171,12,51))
_SwSredCtrl_ObjectIdentity=ObjectIdentity
swSredCtrl=_SwSredCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,51,1))
class _SwSredGlobalState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwSredGlobalState_Type.__name__=_C
_SwSredGlobalState_Object=MibScalar
swSredGlobalState=_SwSredGlobalState_Object((1,3,6,1,4,1,171,12,51,1,1),_SwSredGlobalState_Type())
swSredGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredGlobalState.setStatus(_B)
_SwSredInfo_ObjectIdentity=ObjectIdentity
swSredInfo=_SwSredInfo_ObjectIdentity((1,3,6,1,4,1,171,12,51,2))
_SwSredDropCounterTable_Object=MibTable
swSredDropCounterTable=_SwSredDropCounterTable_Object((1,3,6,1,4,1,171,12,51,2,1))
if mibBuilder.loadTexts:swSredDropCounterTable.setStatus(_B)
_SwSredDropCounterEntry_Object=MibTableRow
swSredDropCounterEntry=_SwSredDropCounterEntry_Object((1,3,6,1,4,1,171,12,51,2,1,1))
swSredDropCounterEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:swSredDropCounterEntry.setStatus(_B)
_SwSredPortIndex_Type=Integer32
_SwSredPortIndex_Object=MibTableColumn
swSredPortIndex=_SwSredPortIndex_Object((1,3,6,1,4,1,171,12,51,2,1,1,1),_SwSredPortIndex_Type())
swSredPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swSredPortIndex.setStatus(_B)
_SwSredLowDropCounter_Type=Counter32
_SwSredLowDropCounter_Object=MibTableColumn
swSredLowDropCounter=_SwSredLowDropCounter_Object((1,3,6,1,4,1,171,12,51,2,1,1,2),_SwSredLowDropCounter_Type())
swSredLowDropCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:swSredLowDropCounter.setStatus(_B)
_SwSredHighDropCounter_Type=Counter32
_SwSredHighDropCounter_Object=MibTableColumn
swSredHighDropCounter=_SwSredHighDropCounter_Object((1,3,6,1,4,1,171,12,51,2,1,1,3),_SwSredHighDropCounter_Type())
swSredHighDropCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:swSredHighDropCounter.setStatus(_B)
_SwSredMgmt_ObjectIdentity=ObjectIdentity
swSredMgmt=_SwSredMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,51,3))
_SwSredCtrlTable_Object=MibTable
swSredCtrlTable=_SwSredCtrlTable_Object((1,3,6,1,4,1,171,12,51,3,1))
if mibBuilder.loadTexts:swSredCtrlTable.setStatus(_B)
_SwSredCtrlEntry_Object=MibTableRow
swSredCtrlEntry=_SwSredCtrlEntry_Object((1,3,6,1,4,1,171,12,51,3,1,1))
swSredCtrlEntry.setIndexNames((0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:swSredCtrlEntry.setStatus(_B)
_SwSredCtrlPortIndex_Type=Integer32
_SwSredCtrlPortIndex_Object=MibTableColumn
swSredCtrlPortIndex=_SwSredCtrlPortIndex_Object((1,3,6,1,4,1,171,12,51,3,1,1,1),_SwSredCtrlPortIndex_Type())
swSredCtrlPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swSredCtrlPortIndex.setStatus(_B)
_SwSredCtrlClassIndex_Type=Integer32
_SwSredCtrlClassIndex_Object=MibTableColumn
swSredCtrlClassIndex=_SwSredCtrlClassIndex_Object((1,3,6,1,4,1,171,12,51,3,1,1,2),_SwSredCtrlClassIndex_Type())
swSredCtrlClassIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swSredCtrlClassIndex.setStatus(_B)
class _SwSredCtrlThresholdLow_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwSredCtrlThresholdLow_Type.__name__=_C
_SwSredCtrlThresholdLow_Object=MibTableColumn
swSredCtrlThresholdLow=_SwSredCtrlThresholdLow_Object((1,3,6,1,4,1,171,12,51,3,1,1,3),_SwSredCtrlThresholdLow_Type())
swSredCtrlThresholdLow.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredCtrlThresholdLow.setStatus(_B)
class _SwSredCtrlThresholdHigh_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwSredCtrlThresholdHigh_Type.__name__=_C
_SwSredCtrlThresholdHigh_Object=MibTableColumn
swSredCtrlThresholdHigh=_SwSredCtrlThresholdHigh_Object((1,3,6,1,4,1,171,12,51,3,1,1,4),_SwSredCtrlThresholdHigh_Type())
swSredCtrlThresholdHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredCtrlThresholdHigh.setStatus(_B)
class _SwSredCtrlDropRateLow_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SwSredCtrlDropRateLow_Type.__name__=_C
_SwSredCtrlDropRateLow_Object=MibTableColumn
swSredCtrlDropRateLow=_SwSredCtrlDropRateLow_Object((1,3,6,1,4,1,171,12,51,3,1,1,5),_SwSredCtrlDropRateLow_Type())
swSredCtrlDropRateLow.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredCtrlDropRateLow.setStatus(_B)
class _SwSredCtrlDropRateHigh_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SwSredCtrlDropRateHigh_Type.__name__=_C
_SwSredCtrlDropRateHigh_Object=MibTableColumn
swSredCtrlDropRateHigh=_SwSredCtrlDropRateHigh_Object((1,3,6,1,4,1,171,12,51,3,1,1,6),_SwSredCtrlDropRateHigh_Type())
swSredCtrlDropRateHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredCtrlDropRateHigh.setStatus(_B)
class _SwSredCtrlDropGreenState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwSredCtrlDropGreenState_Type.__name__=_C
_SwSredCtrlDropGreenState_Object=MibTableColumn
swSredCtrlDropGreenState=_SwSredCtrlDropGreenState_Object((1,3,6,1,4,1,171,12,51,3,1,1,7),_SwSredCtrlDropGreenState_Type())
swSredCtrlDropGreenState.setMaxAccess(_D)
if mibBuilder.loadTexts:swSredCtrlDropGreenState.setStatus(_B)
_Sw8021pColorMapCtrlTable_Object=MibTable
sw8021pColorMapCtrlTable=_Sw8021pColorMapCtrlTable_Object((1,3,6,1,4,1,171,12,51,3,2))
if mibBuilder.loadTexts:sw8021pColorMapCtrlTable.setStatus(_A)
_Sw8021pColorMapCtrlEntry_Object=MibTableRow
sw8021pColorMapCtrlEntry=_Sw8021pColorMapCtrlEntry_Object((1,3,6,1,4,1,171,12,51,3,2,1))
sw8021pColorMapCtrlEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:sw8021pColorMapCtrlEntry.setStatus(_A)
_Sw8021pColorMapCtrlPortIndex_Type=Integer32
_Sw8021pColorMapCtrlPortIndex_Object=MibTableColumn
sw8021pColorMapCtrlPortIndex=_Sw8021pColorMapCtrlPortIndex_Object((1,3,6,1,4,1,171,12,51,3,2,1,1),_Sw8021pColorMapCtrlPortIndex_Type())
sw8021pColorMapCtrlPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sw8021pColorMapCtrlPortIndex.setStatus(_A)
_Sw8021pColorMapCtrlPriorityIndex_Type=Integer32
_Sw8021pColorMapCtrlPriorityIndex_Object=MibTableColumn
sw8021pColorMapCtrlPriorityIndex=_Sw8021pColorMapCtrlPriorityIndex_Object((1,3,6,1,4,1,171,12,51,3,2,1,2),_Sw8021pColorMapCtrlPriorityIndex_Type())
sw8021pColorMapCtrlPriorityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:sw8021pColorMapCtrlPriorityIndex.setStatus(_A)
class _Sw8021pColorMapCtrlColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('red',2),(_N,3)))
_Sw8021pColorMapCtrlColor_Type.__name__=_C
_Sw8021pColorMapCtrlColor_Object=MibTableColumn
sw8021pColorMapCtrlColor=_Sw8021pColorMapCtrlColor_Object((1,3,6,1,4,1,171,12,51,3,2,1,3),_Sw8021pColorMapCtrlColor_Type())
sw8021pColorMapCtrlColor.setMaxAccess(_D)
if mibBuilder.loadTexts:sw8021pColorMapCtrlColor.setStatus(_A)
_SwDscpTrustPortCtrlTable_Object=MibTable
swDscpTrustPortCtrlTable=_SwDscpTrustPortCtrlTable_Object((1,3,6,1,4,1,171,12,51,3,3))
if mibBuilder.loadTexts:swDscpTrustPortCtrlTable.setStatus(_A)
_SwDscpTrustPortCtrlEntry_Object=MibTableRow
swDscpTrustPortCtrlEntry=_SwDscpTrustPortCtrlEntry_Object((1,3,6,1,4,1,171,12,51,3,3,1))
swDscpTrustPortCtrlEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:swDscpTrustPortCtrlEntry.setStatus(_A)
_SwDscpTrustPortCtrlPortIndex_Type=Integer32
_SwDscpTrustPortCtrlPortIndex_Object=MibTableColumn
swDscpTrustPortCtrlPortIndex=_SwDscpTrustPortCtrlPortIndex_Object((1,3,6,1,4,1,171,12,51,3,3,1,1),_SwDscpTrustPortCtrlPortIndex_Type())
swDscpTrustPortCtrlPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swDscpTrustPortCtrlPortIndex.setStatus(_A)
class _SwDscpTrustPortCtrlState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDscpTrustPortCtrlState_Type.__name__=_C
_SwDscpTrustPortCtrlState_Object=MibTableColumn
swDscpTrustPortCtrlState=_SwDscpTrustPortCtrlState_Object((1,3,6,1,4,1,171,12,51,3,3,1,2),_SwDscpTrustPortCtrlState_Type())
swDscpTrustPortCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swDscpTrustPortCtrlState.setStatus(_A)
_SwDscpMapCtrlTable_Object=MibTable
swDscpMapCtrlTable=_SwDscpMapCtrlTable_Object((1,3,6,1,4,1,171,12,51,3,4))
if mibBuilder.loadTexts:swDscpMapCtrlTable.setStatus(_A)
_SwDscpMapCtrlEntry_Object=MibTableRow
swDscpMapCtrlEntry=_SwDscpMapCtrlEntry_Object((1,3,6,1,4,1,171,12,51,3,4,1))
swDscpMapCtrlEntry.setIndexNames((0,_F,_P),(0,_F,_Q))
if mibBuilder.loadTexts:swDscpMapCtrlEntry.setStatus(_A)
_SwDscpMapCtrlPortIndex_Type=Integer32
_SwDscpMapCtrlPortIndex_Object=MibTableColumn
swDscpMapCtrlPortIndex=_SwDscpMapCtrlPortIndex_Object((1,3,6,1,4,1,171,12,51,3,4,1,1),_SwDscpMapCtrlPortIndex_Type())
swDscpMapCtrlPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swDscpMapCtrlPortIndex.setStatus(_A)
_SwDscpMapCtrlDscpIndex_Type=Integer32
_SwDscpMapCtrlDscpIndex_Object=MibTableColumn
swDscpMapCtrlDscpIndex=_SwDscpMapCtrlDscpIndex_Object((1,3,6,1,4,1,171,12,51,3,4,1,2),_SwDscpMapCtrlDscpIndex_Type())
swDscpMapCtrlDscpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swDscpMapCtrlDscpIndex.setStatus(_A)
class _SwDscpMapCtrl8021pPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwDscpMapCtrl8021pPriority_Type.__name__=_C
_SwDscpMapCtrl8021pPriority_Object=MibTableColumn
swDscpMapCtrl8021pPriority=_SwDscpMapCtrl8021pPriority_Object((1,3,6,1,4,1,171,12,51,3,4,1,3),_SwDscpMapCtrl8021pPriority_Type())
swDscpMapCtrl8021pPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swDscpMapCtrl8021pPriority.setStatus(_A)
class _SwDscpMapCtrlNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwDscpMapCtrlNewDscp_Type.__name__=_C
_SwDscpMapCtrlNewDscp_Object=MibTableColumn
swDscpMapCtrlNewDscp=_SwDscpMapCtrlNewDscp_Object((1,3,6,1,4,1,171,12,51,3,4,1,4),_SwDscpMapCtrlNewDscp_Type())
swDscpMapCtrlNewDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:swDscpMapCtrlNewDscp.setStatus(_A)
class _SwDscpMapCtrlColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('red',2),(_N,3)))
_SwDscpMapCtrlColor_Type.__name__=_C
_SwDscpMapCtrlColor_Object=MibTableColumn
swDscpMapCtrlColor=_SwDscpMapCtrlColor_Object((1,3,6,1,4,1,171,12,51,3,4,1,5),_SwDscpMapCtrlColor_Type())
swDscpMapCtrlColor.setMaxAccess(_D)
if mibBuilder.loadTexts:swDscpMapCtrlColor.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'swSredMIB':swSredMIB,'swSredCtrl':swSredCtrl,'swSredGlobalState':swSredGlobalState,'swSredInfo':swSredInfo,'swSredDropCounterTable':swSredDropCounterTable,'swSredDropCounterEntry':swSredDropCounterEntry,_I:swSredPortIndex,'swSredLowDropCounter':swSredLowDropCounter,'swSredHighDropCounter':swSredHighDropCounter,'swSredMgmt':swSredMgmt,'swSredCtrlTable':swSredCtrlTable,'swSredCtrlEntry':swSredCtrlEntry,_J:swSredCtrlPortIndex,_K:swSredCtrlClassIndex,'swSredCtrlThresholdLow':swSredCtrlThresholdLow,'swSredCtrlThresholdHigh':swSredCtrlThresholdHigh,'swSredCtrlDropRateLow':swSredCtrlDropRateLow,'swSredCtrlDropRateHigh':swSredCtrlDropRateHigh,'swSredCtrlDropGreenState':swSredCtrlDropGreenState,'sw8021pColorMapCtrlTable':sw8021pColorMapCtrlTable,'sw8021pColorMapCtrlEntry':sw8021pColorMapCtrlEntry,_L:sw8021pColorMapCtrlPortIndex,_M:sw8021pColorMapCtrlPriorityIndex,'sw8021pColorMapCtrlColor':sw8021pColorMapCtrlColor,'swDscpTrustPortCtrlTable':swDscpTrustPortCtrlTable,'swDscpTrustPortCtrlEntry':swDscpTrustPortCtrlEntry,_O:swDscpTrustPortCtrlPortIndex,'swDscpTrustPortCtrlState':swDscpTrustPortCtrlState,'swDscpMapCtrlTable':swDscpMapCtrlTable,'swDscpMapCtrlEntry':swDscpMapCtrlEntry,_P:swDscpMapCtrlPortIndex,_Q:swDscpMapCtrlDscpIndex,'swDscpMapCtrl8021pPriority':swDscpMapCtrl8021pPriority,'swDscpMapCtrlNewDscp':swDscpMapCtrlNewDscp,'swDscpMapCtrlColor':swDscpMapCtrlColor})