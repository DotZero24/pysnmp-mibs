_j='docsIfExt2CmtsGroup'
_i='docsIfExt2CmGroup'
_h='docsIfExt2CmtsUpChannelTotalCMs'
_g='docsIfExt2CmtsUpChannelMSCMinimumValue'
_f='docsIfExt2CmtsUpChannelMSCLimitIUC1'
_e='docsIfExt2CmtsUpChannelMSCTotalCMs'
_d='docsIfExt2CmtsUpChannelMscState'
_c='docsIfExt2CmtsCmMscStatusEffectiveSNR'
_b='docsIfExt2CmtsCmMscStatusMeasuredSNR'
_a='docsIfExt2CmtsCmMscStatusPowerHeadroom'
_Z='docsIfExt2CmtsCmMscStatusMaximumScheduledCodes'
_Y='docsIfExt2CmtsCmMscStatusCodeRatio'
_X='docsIfExt2CmtsCmMscStatusPowerShortfall'
_W='docsIfExt2CmtsMscGlobalEnable'
_V='docsIfExt2CmMscStatusIUC2Control'
_U='docsIfExt2CmMscStatusEffectivePower'
_T='docsIfExt2CmMscStatusPowerHeadroom'
_S='docsIfExt2CmMscStatusMaximumScheduledCodes'
_R='docsIfExt2CmMscStatusCodeRatio'
_Q='docsIfExt2CmMscStatusPowerShortfall'
_P='docsIfExt2CmMscStatusState'
_O='channelDisabled'
_N='channelEnabled'
_M='TruthValue'
_L='docsIfCmtsCmStatusIndex'
_K='TenthdBmV'
_J='DOCS-IF-MIB'
_I='read-write'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='TenthdB'
_C='read-only'
_B='DOCS-IFEXT2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjDocsis,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjDocsis')
TenthdB,TenthdBmV,docsIfCmtsCmStatusIndex=mibBuilder.importSymbols(_J,_D,_K,_L)
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_M)
docsIfExt2Mib=ModuleIdentity((1,3,6,1,4,1,4491,2,1,5))
if mibBuilder.loadTexts:docsIfExt2Mib.setRevisions(('2004-06-23 17:00','2004-11-10 17:00'))
_DocsIfExt2Notifications_ObjectIdentity=ObjectIdentity
docsIfExt2Notifications=_DocsIfExt2Notifications_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,0))
_DocsIfExt2MibObjects_ObjectIdentity=ObjectIdentity
docsIfExt2MibObjects=_DocsIfExt2MibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,1))
_DocsIfExt2BaseObjects_ObjectIdentity=ObjectIdentity
docsIfExt2BaseObjects=_DocsIfExt2BaseObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,1,1))
_DocsIfExt2CmObjects_ObjectIdentity=ObjectIdentity
docsIfExt2CmObjects=_DocsIfExt2CmObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,1,2))
_DocsIfExt2CmMscStatusTable_Object=MibTable
docsIfExt2CmMscStatusTable=_DocsIfExt2CmMscStatusTable_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1))
if mibBuilder.loadTexts:docsIfExt2CmMscStatusTable.setStatus(_A)
_DocsIfExt2CmMscStatusEntry_Object=MibTableRow
docsIfExt2CmMscStatusEntry=_DocsIfExt2CmMscStatusEntry_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1))
docsIfExt2CmMscStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:docsIfExt2CmMscStatusEntry.setStatus(_A)
class _DocsIfExt2CmMscStatusState_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),('active',3),('inactive',4),('unknown',5)))
_DocsIfExt2CmMscStatusState_Type.__name__=_H
_DocsIfExt2CmMscStatusState_Object=MibTableColumn
docsIfExt2CmMscStatusState=_DocsIfExt2CmMscStatusState_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,1),_DocsIfExt2CmMscStatusState_Type())
docsIfExt2CmMscStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusState.setStatus(_A)
class _DocsIfExt2CmMscStatusPowerShortfall_Type(TenthdB):defaultValue=0
_DocsIfExt2CmMscStatusPowerShortfall_Type.__name__=_D
_DocsIfExt2CmMscStatusPowerShortfall_Object=MibTableColumn
docsIfExt2CmMscStatusPowerShortfall=_DocsIfExt2CmMscStatusPowerShortfall_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,2),_DocsIfExt2CmMscStatusPowerShortfall_Type())
docsIfExt2CmMscStatusPowerShortfall.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusPowerShortfall.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusPowerShortfall.setUnits(_D)
class _DocsIfExt2CmMscStatusCodeRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2),ValueRangeConstraint(8,8),ValueRangeConstraint(16,16),ValueRangeConstraint(32,32))
_DocsIfExt2CmMscStatusCodeRatio_Type.__name__=_E
_DocsIfExt2CmMscStatusCodeRatio_Object=MibTableColumn
docsIfExt2CmMscStatusCodeRatio=_DocsIfExt2CmMscStatusCodeRatio_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,3),_DocsIfExt2CmMscStatusCodeRatio_Type())
docsIfExt2CmMscStatusCodeRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusCodeRatio.setStatus(_A)
class _DocsIfExt2CmMscStatusMaximumScheduledCodes_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,128))
_DocsIfExt2CmMscStatusMaximumScheduledCodes_Type.__name__=_E
_DocsIfExt2CmMscStatusMaximumScheduledCodes_Object=MibTableColumn
docsIfExt2CmMscStatusMaximumScheduledCodes=_DocsIfExt2CmMscStatusMaximumScheduledCodes_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,4),_DocsIfExt2CmMscStatusMaximumScheduledCodes_Type())
docsIfExt2CmMscStatusMaximumScheduledCodes.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusMaximumScheduledCodes.setStatus(_A)
class _DocsIfExt2CmMscStatusPowerHeadroom_Type(TenthdB):defaultValue=0
_DocsIfExt2CmMscStatusPowerHeadroom_Type.__name__=_D
_DocsIfExt2CmMscStatusPowerHeadroom_Object=MibTableColumn
docsIfExt2CmMscStatusPowerHeadroom=_DocsIfExt2CmMscStatusPowerHeadroom_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,5),_DocsIfExt2CmMscStatusPowerHeadroom_Type())
docsIfExt2CmMscStatusPowerHeadroom.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusPowerHeadroom.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusPowerHeadroom.setUnits(_D)
_DocsIfExt2CmMscStatusEffectivePower_Type=TenthdBmV
_DocsIfExt2CmMscStatusEffectivePower_Object=MibTableColumn
docsIfExt2CmMscStatusEffectivePower=_DocsIfExt2CmMscStatusEffectivePower_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,6),_DocsIfExt2CmMscStatusEffectivePower_Type())
docsIfExt2CmMscStatusEffectivePower.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusEffectivePower.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusEffectivePower.setUnits(_K)
class _DocsIfExt2CmMscStatusIUC2Control_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noIUC2',1),('limitedIUC2',2),('freeIUC2',3)))
_DocsIfExt2CmMscStatusIUC2Control_Type.__name__=_H
_DocsIfExt2CmMscStatusIUC2Control_Object=MibTableColumn
docsIfExt2CmMscStatusIUC2Control=_DocsIfExt2CmMscStatusIUC2Control_Object((1,3,6,1,4,1,4491,2,1,5,1,2,1,1,7),_DocsIfExt2CmMscStatusIUC2Control_Type())
docsIfExt2CmMscStatusIUC2Control.setMaxAccess(_I)
if mibBuilder.loadTexts:docsIfExt2CmMscStatusIUC2Control.setStatus(_A)
_DocsIfExt2CmtsObjects_ObjectIdentity=ObjectIdentity
docsIfExt2CmtsObjects=_DocsIfExt2CmtsObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,1,3))
class _DocsIfExt2CmtsMscGlobalEnable_Type(TruthValue):defaultValue=2
_DocsIfExt2CmtsMscGlobalEnable_Type.__name__=_M
_DocsIfExt2CmtsMscGlobalEnable_Object=MibScalar
docsIfExt2CmtsMscGlobalEnable=_DocsIfExt2CmtsMscGlobalEnable_Object((1,3,6,1,4,1,4491,2,1,5,1,3,1),_DocsIfExt2CmtsMscGlobalEnable_Type())
docsIfExt2CmtsMscGlobalEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:docsIfExt2CmtsMscGlobalEnable.setStatus(_A)
_DocsIfExt2CmtsCmMscStatusTable_Object=MibTable
docsIfExt2CmtsCmMscStatusTable=_DocsIfExt2CmtsCmMscStatusTable_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2))
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusTable.setStatus(_A)
_DocsIfExt2CmtsCmMscStatusEntry_Object=MibTableRow
docsIfExt2CmtsCmMscStatusEntry=_DocsIfExt2CmtsCmMscStatusEntry_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1))
docsIfExt2CmtsCmMscStatusEntry.setIndexNames((0,_J,_L))
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusEntry.setStatus(_A)
class _DocsIfExt2CmtsCmMscStatusPowerShortfall_Type(TenthdB):defaultValue=0
_DocsIfExt2CmtsCmMscStatusPowerShortfall_Type.__name__=_D
_DocsIfExt2CmtsCmMscStatusPowerShortfall_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusPowerShortfall=_DocsIfExt2CmtsCmMscStatusPowerShortfall_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,1),_DocsIfExt2CmtsCmMscStatusPowerShortfall_Type())
docsIfExt2CmtsCmMscStatusPowerShortfall.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusPowerShortfall.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusPowerShortfall.setUnits(_D)
class _DocsIfExt2CmtsCmMscStatusCodeRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,2),ValueRangeConstraint(8,8),ValueRangeConstraint(16,16),ValueRangeConstraint(32,32))
_DocsIfExt2CmtsCmMscStatusCodeRatio_Type.__name__=_E
_DocsIfExt2CmtsCmMscStatusCodeRatio_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusCodeRatio=_DocsIfExt2CmtsCmMscStatusCodeRatio_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,2),_DocsIfExt2CmtsCmMscStatusCodeRatio_Type())
docsIfExt2CmtsCmMscStatusCodeRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusCodeRatio.setStatus(_A)
class _DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,128))
_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type.__name__=_E
_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusMaximumScheduledCodes=_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,3),_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type())
docsIfExt2CmtsCmMscStatusMaximumScheduledCodes.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusMaximumScheduledCodes.setStatus(_A)
class _DocsIfExt2CmtsCmMscStatusPowerHeadroom_Type(TenthdB):defaultValue=0
_DocsIfExt2CmtsCmMscStatusPowerHeadroom_Type.__name__=_D
_DocsIfExt2CmtsCmMscStatusPowerHeadroom_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusPowerHeadroom=_DocsIfExt2CmtsCmMscStatusPowerHeadroom_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,4),_DocsIfExt2CmtsCmMscStatusPowerHeadroom_Type())
docsIfExt2CmtsCmMscStatusPowerHeadroom.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusPowerHeadroom.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusPowerHeadroom.setUnits(_D)
_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Type=TenthdB
_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusMeasuredSNR=_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,5),_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Type())
docsIfExt2CmtsCmMscStatusMeasuredSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusMeasuredSNR.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusMeasuredSNR.setUnits(_D)
_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Type=TenthdB
_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Object=MibTableColumn
docsIfExt2CmtsCmMscStatusEffectiveSNR=_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Object((1,3,6,1,4,1,4491,2,1,5,1,3,2,1,6),_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Type())
docsIfExt2CmtsCmMscStatusEffectiveSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusEffectiveSNR.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsCmMscStatusEffectiveSNR.setUnits(_D)
_DocsIfExt2CmtsUpChannelMscTable_Object=MibTable
docsIfExt2CmtsUpChannelMscTable=_DocsIfExt2CmtsUpChannelMscTable_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3))
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMscTable.setStatus(_A)
_DocsIfExt2CmtsUpChannelMscEntry_Object=MibTableRow
docsIfExt2CmtsUpChannelMscEntry=_DocsIfExt2CmtsUpChannelMscEntry_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3,1))
docsIfExt2CmtsUpChannelMscEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMscEntry.setStatus(_A)
class _DocsIfExt2CmtsUpChannelMscState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('dormant',3)))
_DocsIfExt2CmtsUpChannelMscState_Type.__name__=_H
_DocsIfExt2CmtsUpChannelMscState_Object=MibTableColumn
docsIfExt2CmtsUpChannelMscState=_DocsIfExt2CmtsUpChannelMscState_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3,1,1),_DocsIfExt2CmtsUpChannelMscState_Type())
docsIfExt2CmtsUpChannelMscState.setMaxAccess(_I)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMscState.setStatus(_A)
_DocsIfExt2CmtsUpChannelMSCTotalCMs_Type=Gauge32
_DocsIfExt2CmtsUpChannelMSCTotalCMs_Object=MibTableColumn
docsIfExt2CmtsUpChannelMSCTotalCMs=_DocsIfExt2CmtsUpChannelMSCTotalCMs_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3,1,2),_DocsIfExt2CmtsUpChannelMSCTotalCMs_Type())
docsIfExt2CmtsUpChannelMSCTotalCMs.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMSCTotalCMs.setStatus(_A)
class _DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type.__name__=_E
_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Object=MibTableColumn
docsIfExt2CmtsUpChannelMSCLimitIUC1=_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3,1,3),_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type())
docsIfExt2CmtsUpChannelMSCLimitIUC1.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMSCLimitIUC1.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMSCLimitIUC1.setUnits('codes')
class _DocsIfExt2CmtsUpChannelMSCMinimumValue_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_DocsIfExt2CmtsUpChannelMSCMinimumValue_Type.__name__=_E
_DocsIfExt2CmtsUpChannelMSCMinimumValue_Object=MibTableColumn
docsIfExt2CmtsUpChannelMSCMinimumValue=_DocsIfExt2CmtsUpChannelMSCMinimumValue_Object((1,3,6,1,4,1,4491,2,1,5,1,3,3,1,4),_DocsIfExt2CmtsUpChannelMSCMinimumValue_Type())
docsIfExt2CmtsUpChannelMSCMinimumValue.setMaxAccess(_I)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMSCMinimumValue.setStatus(_A)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelMSCMinimumValue.setUnits('codes')
_DocsIfExt2CmtsUpChannelTable_Object=MibTable
docsIfExt2CmtsUpChannelTable=_DocsIfExt2CmtsUpChannelTable_Object((1,3,6,1,4,1,4491,2,1,5,1,3,4))
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelTable.setStatus(_A)
_DocsIfExt2CmtsUpChannelEntry_Object=MibTableRow
docsIfExt2CmtsUpChannelEntry=_DocsIfExt2CmtsUpChannelEntry_Object((1,3,6,1,4,1,4491,2,1,5,1,3,4,1))
docsIfExt2CmtsUpChannelEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelEntry.setStatus(_A)
_DocsIfExt2CmtsUpChannelTotalCMs_Type=Gauge32
_DocsIfExt2CmtsUpChannelTotalCMs_Object=MibTableColumn
docsIfExt2CmtsUpChannelTotalCMs=_DocsIfExt2CmtsUpChannelTotalCMs_Object((1,3,6,1,4,1,4491,2,1,5,1,3,4,1,1),_DocsIfExt2CmtsUpChannelTotalCMs_Type())
docsIfExt2CmtsUpChannelTotalCMs.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfExt2CmtsUpChannelTotalCMs.setStatus(_A)
_DocsIfExt2Conformance_ObjectIdentity=ObjectIdentity
docsIfExt2Conformance=_DocsIfExt2Conformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,2))
_DocsIfExt2Compliances_ObjectIdentity=ObjectIdentity
docsIfExt2Compliances=_DocsIfExt2Compliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,2,1))
_DocsIfExt2Groups_ObjectIdentity=ObjectIdentity
docsIfExt2Groups=_DocsIfExt2Groups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,5,2,2))
docsIfExt2CmGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,5,2,2,1))
docsIfExt2CmGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:docsIfExt2CmGroup.setStatus(_A)
docsIfExt2CmtsGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,5,2,2,2))
docsIfExt2CmtsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:docsIfExt2CmtsGroup.setStatus(_A)
docsIfExt2Compliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,5,2,1,1))
docsIfExt2Compliance.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:docsIfExt2Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'docsIfExt2Mib':docsIfExt2Mib,'docsIfExt2Notifications':docsIfExt2Notifications,'docsIfExt2MibObjects':docsIfExt2MibObjects,'docsIfExt2BaseObjects':docsIfExt2BaseObjects,'docsIfExt2CmObjects':docsIfExt2CmObjects,'docsIfExt2CmMscStatusTable':docsIfExt2CmMscStatusTable,'docsIfExt2CmMscStatusEntry':docsIfExt2CmMscStatusEntry,_P:docsIfExt2CmMscStatusState,_Q:docsIfExt2CmMscStatusPowerShortfall,_R:docsIfExt2CmMscStatusCodeRatio,_S:docsIfExt2CmMscStatusMaximumScheduledCodes,_T:docsIfExt2CmMscStatusPowerHeadroom,_U:docsIfExt2CmMscStatusEffectivePower,_V:docsIfExt2CmMscStatusIUC2Control,'docsIfExt2CmtsObjects':docsIfExt2CmtsObjects,_W:docsIfExt2CmtsMscGlobalEnable,'docsIfExt2CmtsCmMscStatusTable':docsIfExt2CmtsCmMscStatusTable,'docsIfExt2CmtsCmMscStatusEntry':docsIfExt2CmtsCmMscStatusEntry,_X:docsIfExt2CmtsCmMscStatusPowerShortfall,_Y:docsIfExt2CmtsCmMscStatusCodeRatio,_Z:docsIfExt2CmtsCmMscStatusMaximumScheduledCodes,_a:docsIfExt2CmtsCmMscStatusPowerHeadroom,_b:docsIfExt2CmtsCmMscStatusMeasuredSNR,_c:docsIfExt2CmtsCmMscStatusEffectiveSNR,'docsIfExt2CmtsUpChannelMscTable':docsIfExt2CmtsUpChannelMscTable,'docsIfExt2CmtsUpChannelMscEntry':docsIfExt2CmtsUpChannelMscEntry,_d:docsIfExt2CmtsUpChannelMscState,_e:docsIfExt2CmtsUpChannelMSCTotalCMs,_f:docsIfExt2CmtsUpChannelMSCLimitIUC1,_g:docsIfExt2CmtsUpChannelMSCMinimumValue,'docsIfExt2CmtsUpChannelTable':docsIfExt2CmtsUpChannelTable,'docsIfExt2CmtsUpChannelEntry':docsIfExt2CmtsUpChannelEntry,_h:docsIfExt2CmtsUpChannelTotalCMs,'docsIfExt2Conformance':docsIfExt2Conformance,'docsIfExt2Compliances':docsIfExt2Compliances,'docsIfExt2Compliance':docsIfExt2Compliance,'docsIfExt2Groups':docsIfExt2Groups,_i:docsIfExt2CmGroup,_j:docsIfExt2CmtsGroup})