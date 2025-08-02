_q='h3cTeTunnelPsGroup'
_p='h3cTeTunnelCorouteGroup'
_o='h3cTeTunnelStaticCrlspGroup'
_n='h3cTeTunnelScalarsGroup'
_m='h3cTeTunnelNotificationsGroup'
_l='h3cTeTunnelPsSwitchWtoP'
_k='h3cTeTunnelPsSwitchPtoW'
_j='h3cTeTunnelPsSwitchResult'
_i='h3cTeTunnelPsSwitchMode'
_h='h3cTeTunnelPsHoldOffTime'
_g='h3cTeTunnelPsWtrTime'
_f='h3cTeTunnelPsRevertiveMode'
_e='h3cTeTunnelPsProtectType'
_d='h3cTeTunnelPsProtectEgressLSRId'
_c='h3cTeTunnelPsProtectIngressLSRId'
_b='h3cTeTunnelPsProtectIndex'
_a='h3cTeTunnelCoReverseLspXCPointer'
_Z='h3cTeTunnelCoReverseLspInstance'
_Y='h3cTeTunnelCoBiMode'
_X='h3cTeTunnelStaticCrlspXCPointer'
_W='h3cTeTunnelStaticCrlspRole'
_V='h3cTeTunnelStaticCrlspStatus'
_U='h3cTeTunnelStaticCrlspName'
_T='h3cTeTunnelMaxTunnelIndex'
_S='inDefect'
_R='noDefect'
_Q='h3cTeTunnelPsEgressLSRId'
_P='h3cTeTunnelPsIngressLSRId'
_O='h3cTeTunnelPsIndex'
_N='h3cTeTunnelCoEgressLSRId'
_M='h3cTeTunnelCoIngressLSRId'
_L='h3cTeTunnelCoLspInstance'
_K='h3cTeTunnelCoIndex'
_J='h3cTeTunnelStaticCrlspInLabel'
_I='OctetString'
_H='Unsigned32'
_G='h3cTeTunnelPsProtectPathStatus'
_F='h3cTeTunnelPsWorkPathStatus'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='H3C-TE-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
MplsExtendedTunnelId,MplsLabel,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsExtendedTunnelId','MplsLabel','MplsTunnelIndex','MplsTunnelInstanceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
h3cTeTunnel=ModuleIdentity((1,3,6,1,4,1,2011,10,2,115))
_H3cTeTunnelScalars_ObjectIdentity=ObjectIdentity
h3cTeTunnelScalars=_H3cTeTunnelScalars_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,1))
_H3cTeTunnelMaxTunnelIndex_Type=MplsTunnelIndex
_H3cTeTunnelMaxTunnelIndex_Object=MibScalar
h3cTeTunnelMaxTunnelIndex=_H3cTeTunnelMaxTunnelIndex_Object((1,3,6,1,4,1,2011,10,2,115,1,1),_H3cTeTunnelMaxTunnelIndex_Type())
h3cTeTunnelMaxTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelMaxTunnelIndex.setStatus(_A)
_H3cTeTunnelObjects_ObjectIdentity=ObjectIdentity
h3cTeTunnelObjects=_H3cTeTunnelObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,2))
_H3cTeTunnelStaticCrlspTable_Object=MibTable
h3cTeTunnelStaticCrlspTable=_H3cTeTunnelStaticCrlspTable_Object((1,3,6,1,4,1,2011,10,2,115,2,1))
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspTable.setStatus(_A)
_H3cTeTunnelStaticCrlspEntry_Object=MibTableRow
h3cTeTunnelStaticCrlspEntry=_H3cTeTunnelStaticCrlspEntry_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1))
h3cTeTunnelStaticCrlspEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspEntry.setStatus(_A)
_H3cTeTunnelStaticCrlspInLabel_Type=MplsLabel
_H3cTeTunnelStaticCrlspInLabel_Object=MibTableColumn
h3cTeTunnelStaticCrlspInLabel=_H3cTeTunnelStaticCrlspInLabel_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1,1),_H3cTeTunnelStaticCrlspInLabel_Type())
h3cTeTunnelStaticCrlspInLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspInLabel.setStatus(_A)
class _H3cTeTunnelStaticCrlspName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cTeTunnelStaticCrlspName_Type.__name__=_I
_H3cTeTunnelStaticCrlspName_Object=MibTableColumn
h3cTeTunnelStaticCrlspName=_H3cTeTunnelStaticCrlspName_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1,2),_H3cTeTunnelStaticCrlspName_Type())
h3cTeTunnelStaticCrlspName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspName.setStatus(_A)
class _H3cTeTunnelStaticCrlspStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cTeTunnelStaticCrlspStatus_Type.__name__=_D
_H3cTeTunnelStaticCrlspStatus_Object=MibTableColumn
h3cTeTunnelStaticCrlspStatus=_H3cTeTunnelStaticCrlspStatus_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1,3),_H3cTeTunnelStaticCrlspStatus_Type())
h3cTeTunnelStaticCrlspStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspStatus.setStatus(_A)
class _H3cTeTunnelStaticCrlspRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transit',1),('tail',2)))
_H3cTeTunnelStaticCrlspRole_Type.__name__=_D
_H3cTeTunnelStaticCrlspRole_Object=MibTableColumn
h3cTeTunnelStaticCrlspRole=_H3cTeTunnelStaticCrlspRole_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1,4),_H3cTeTunnelStaticCrlspRole_Type())
h3cTeTunnelStaticCrlspRole.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspRole.setStatus(_A)
_H3cTeTunnelStaticCrlspXCPointer_Type=RowPointer
_H3cTeTunnelStaticCrlspXCPointer_Object=MibTableColumn
h3cTeTunnelStaticCrlspXCPointer=_H3cTeTunnelStaticCrlspXCPointer_Object((1,3,6,1,4,1,2011,10,2,115,2,1,1,5),_H3cTeTunnelStaticCrlspXCPointer_Type())
h3cTeTunnelStaticCrlspXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspXCPointer.setStatus(_A)
_H3cTeTunnelCoTable_Object=MibTable
h3cTeTunnelCoTable=_H3cTeTunnelCoTable_Object((1,3,6,1,4,1,2011,10,2,115,2,2))
if mibBuilder.loadTexts:h3cTeTunnelCoTable.setStatus(_A)
_H3cTeTunnelCoEntry_Object=MibTableRow
h3cTeTunnelCoEntry=_H3cTeTunnelCoEntry_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1))
h3cTeTunnelCoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:h3cTeTunnelCoEntry.setStatus(_A)
_H3cTeTunnelCoIndex_Type=MplsTunnelIndex
_H3cTeTunnelCoIndex_Object=MibTableColumn
h3cTeTunnelCoIndex=_H3cTeTunnelCoIndex_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,1),_H3cTeTunnelCoIndex_Type())
h3cTeTunnelCoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelCoIndex.setStatus(_A)
_H3cTeTunnelCoLspInstance_Type=MplsTunnelInstanceIndex
_H3cTeTunnelCoLspInstance_Object=MibTableColumn
h3cTeTunnelCoLspInstance=_H3cTeTunnelCoLspInstance_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,2),_H3cTeTunnelCoLspInstance_Type())
h3cTeTunnelCoLspInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelCoLspInstance.setStatus(_A)
_H3cTeTunnelCoIngressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelCoIngressLSRId_Object=MibTableColumn
h3cTeTunnelCoIngressLSRId=_H3cTeTunnelCoIngressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,3),_H3cTeTunnelCoIngressLSRId_Type())
h3cTeTunnelCoIngressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelCoIngressLSRId.setStatus(_A)
_H3cTeTunnelCoEgressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelCoEgressLSRId_Object=MibTableColumn
h3cTeTunnelCoEgressLSRId=_H3cTeTunnelCoEgressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,4),_H3cTeTunnelCoEgressLSRId_Type())
h3cTeTunnelCoEgressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelCoEgressLSRId.setStatus(_A)
class _H3cTeTunnelCoBiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coroutedActive',1),('coroutedPassive',2)))
_H3cTeTunnelCoBiMode_Type.__name__=_D
_H3cTeTunnelCoBiMode_Object=MibTableColumn
h3cTeTunnelCoBiMode=_H3cTeTunnelCoBiMode_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,5),_H3cTeTunnelCoBiMode_Type())
h3cTeTunnelCoBiMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelCoBiMode.setStatus(_A)
_H3cTeTunnelCoReverseLspInstance_Type=MplsTunnelInstanceIndex
_H3cTeTunnelCoReverseLspInstance_Object=MibTableColumn
h3cTeTunnelCoReverseLspInstance=_H3cTeTunnelCoReverseLspInstance_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,6),_H3cTeTunnelCoReverseLspInstance_Type())
h3cTeTunnelCoReverseLspInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelCoReverseLspInstance.setStatus(_A)
_H3cTeTunnelCoReverseLspXCPointer_Type=RowPointer
_H3cTeTunnelCoReverseLspXCPointer_Object=MibTableColumn
h3cTeTunnelCoReverseLspXCPointer=_H3cTeTunnelCoReverseLspXCPointer_Object((1,3,6,1,4,1,2011,10,2,115,2,2,1,7),_H3cTeTunnelCoReverseLspXCPointer_Type())
h3cTeTunnelCoReverseLspXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelCoReverseLspXCPointer.setStatus(_A)
_H3cTeTunnelPsTable_Object=MibTable
h3cTeTunnelPsTable=_H3cTeTunnelPsTable_Object((1,3,6,1,4,1,2011,10,2,115,2,3))
if mibBuilder.loadTexts:h3cTeTunnelPsTable.setStatus(_A)
_H3cTeTunnelPsEntry_Object=MibTableRow
h3cTeTunnelPsEntry=_H3cTeTunnelPsEntry_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1))
h3cTeTunnelPsEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:h3cTeTunnelPsEntry.setStatus(_A)
_H3cTeTunnelPsIndex_Type=MplsTunnelIndex
_H3cTeTunnelPsIndex_Object=MibTableColumn
h3cTeTunnelPsIndex=_H3cTeTunnelPsIndex_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,1),_H3cTeTunnelPsIndex_Type())
h3cTeTunnelPsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelPsIndex.setStatus(_A)
_H3cTeTunnelPsIngressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelPsIngressLSRId_Object=MibTableColumn
h3cTeTunnelPsIngressLSRId=_H3cTeTunnelPsIngressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,2),_H3cTeTunnelPsIngressLSRId_Type())
h3cTeTunnelPsIngressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelPsIngressLSRId.setStatus(_A)
_H3cTeTunnelPsEgressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelPsEgressLSRId_Object=MibTableColumn
h3cTeTunnelPsEgressLSRId=_H3cTeTunnelPsEgressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,3),_H3cTeTunnelPsEgressLSRId_Type())
h3cTeTunnelPsEgressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTeTunnelPsEgressLSRId.setStatus(_A)
_H3cTeTunnelPsProtectIndex_Type=MplsTunnelIndex
_H3cTeTunnelPsProtectIndex_Object=MibTableColumn
h3cTeTunnelPsProtectIndex=_H3cTeTunnelPsProtectIndex_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,4),_H3cTeTunnelPsProtectIndex_Type())
h3cTeTunnelPsProtectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsProtectIndex.setStatus(_A)
_H3cTeTunnelPsProtectIngressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelPsProtectIngressLSRId_Object=MibTableColumn
h3cTeTunnelPsProtectIngressLSRId=_H3cTeTunnelPsProtectIngressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,5),_H3cTeTunnelPsProtectIngressLSRId_Type())
h3cTeTunnelPsProtectIngressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsProtectIngressLSRId.setStatus(_A)
_H3cTeTunnelPsProtectEgressLSRId_Type=MplsExtendedTunnelId
_H3cTeTunnelPsProtectEgressLSRId_Object=MibTableColumn
h3cTeTunnelPsProtectEgressLSRId=_H3cTeTunnelPsProtectEgressLSRId_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,6),_H3cTeTunnelPsProtectEgressLSRId_Type())
h3cTeTunnelPsProtectEgressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsProtectEgressLSRId.setStatus(_A)
class _H3cTeTunnelPsProtectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneToOne',1),('onePlusOne',2)))
_H3cTeTunnelPsProtectType_Type.__name__=_D
_H3cTeTunnelPsProtectType_Object=MibTableColumn
h3cTeTunnelPsProtectType=_H3cTeTunnelPsProtectType_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,7),_H3cTeTunnelPsProtectType_Type())
h3cTeTunnelPsProtectType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsProtectType.setStatus(_A)
class _H3cTeTunnelPsRevertiveMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('noRevertive',2)))
_H3cTeTunnelPsRevertiveMode_Type.__name__=_D
_H3cTeTunnelPsRevertiveMode_Object=MibTableColumn
h3cTeTunnelPsRevertiveMode=_H3cTeTunnelPsRevertiveMode_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,8),_H3cTeTunnelPsRevertiveMode_Type())
h3cTeTunnelPsRevertiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsRevertiveMode.setStatus(_A)
class _H3cTeTunnelPsWtrTime_Type(Unsigned32):defaultValue=24;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_H3cTeTunnelPsWtrTime_Type.__name__=_H
_H3cTeTunnelPsWtrTime_Object=MibTableColumn
h3cTeTunnelPsWtrTime=_H3cTeTunnelPsWtrTime_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,9),_H3cTeTunnelPsWtrTime_Type())
h3cTeTunnelPsWtrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsWtrTime.setStatus(_A)
if mibBuilder.loadTexts:h3cTeTunnelPsWtrTime.setUnits('30 seconds')
class _H3cTeTunnelPsHoldOffTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_H3cTeTunnelPsHoldOffTime_Type.__name__=_H
_H3cTeTunnelPsHoldOffTime_Object=MibTableColumn
h3cTeTunnelPsHoldOffTime=_H3cTeTunnelPsHoldOffTime_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,10),_H3cTeTunnelPsHoldOffTime_Type())
h3cTeTunnelPsHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:h3cTeTunnelPsHoldOffTime.setUnits('500ms')
class _H3cTeTunnelPsSwitchMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uniDirectional',1),('biDirectional',2)))
_H3cTeTunnelPsSwitchMode_Type.__name__=_D
_H3cTeTunnelPsSwitchMode_Object=MibTableColumn
h3cTeTunnelPsSwitchMode=_H3cTeTunnelPsSwitchMode_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,11),_H3cTeTunnelPsSwitchMode_Type())
h3cTeTunnelPsSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsSwitchMode.setStatus(_A)
class _H3cTeTunnelPsWorkPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_R,2),(_S,3)))
_H3cTeTunnelPsWorkPathStatus_Type.__name__=_D
_H3cTeTunnelPsWorkPathStatus_Object=MibTableColumn
h3cTeTunnelPsWorkPathStatus=_H3cTeTunnelPsWorkPathStatus_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,12),_H3cTeTunnelPsWorkPathStatus_Type())
h3cTeTunnelPsWorkPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsWorkPathStatus.setStatus(_A)
class _H3cTeTunnelPsProtectPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_R,2),(_S,3)))
_H3cTeTunnelPsProtectPathStatus_Type.__name__=_D
_H3cTeTunnelPsProtectPathStatus_Object=MibTableColumn
h3cTeTunnelPsProtectPathStatus=_H3cTeTunnelPsProtectPathStatus_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,13),_H3cTeTunnelPsProtectPathStatus_Type())
h3cTeTunnelPsProtectPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsProtectPathStatus.setStatus(_A)
class _H3cTeTunnelPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('workPath',1),('protectPath',2)))
_H3cTeTunnelPsSwitchResult_Type.__name__=_D
_H3cTeTunnelPsSwitchResult_Object=MibTableColumn
h3cTeTunnelPsSwitchResult=_H3cTeTunnelPsSwitchResult_Object((1,3,6,1,4,1,2011,10,2,115,2,3,1,14),_H3cTeTunnelPsSwitchResult_Type())
h3cTeTunnelPsSwitchResult.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cTeTunnelPsSwitchResult.setStatus(_A)
_H3cTeTunnelNotifications_ObjectIdentity=ObjectIdentity
h3cTeTunnelNotifications=_H3cTeTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,3))
_H3cTeTunnelNotificationsPrefix_ObjectIdentity=ObjectIdentity
h3cTeTunnelNotificationsPrefix=_H3cTeTunnelNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,3,0))
_H3cTeTunnelConformance_ObjectIdentity=ObjectIdentity
h3cTeTunnelConformance=_H3cTeTunnelConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,4))
_H3cTeTunnelCompliances_ObjectIdentity=ObjectIdentity
h3cTeTunnelCompliances=_H3cTeTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,4,1))
_H3cTeTunnelGroups_ObjectIdentity=ObjectIdentity
h3cTeTunnelGroups=_H3cTeTunnelGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,115,4,2))
h3cTeTunnelScalarsGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,115,4,2,2))
h3cTeTunnelScalarsGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:h3cTeTunnelScalarsGroup.setStatus(_A)
h3cTeTunnelStaticCrlspGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,115,4,2,3))
h3cTeTunnelStaticCrlspGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h3cTeTunnelStaticCrlspGroup.setStatus(_A)
h3cTeTunnelCorouteGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,115,4,2,4))
h3cTeTunnelCorouteGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:h3cTeTunnelCorouteGroup.setStatus(_A)
h3cTeTunnelPsGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,115,4,2,5))
h3cTeTunnelPsGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_F),(_B,_G),(_B,_j)))
if mibBuilder.loadTexts:h3cTeTunnelPsGroup.setStatus(_A)
h3cTeTunnelPsSwitchWtoP=NotificationType((1,3,6,1,4,1,2011,10,2,115,3,0,1))
h3cTeTunnelPsSwitchWtoP.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:h3cTeTunnelPsSwitchWtoP.setStatus(_A)
h3cTeTunnelPsSwitchPtoW=NotificationType((1,3,6,1,4,1,2011,10,2,115,3,0,2))
h3cTeTunnelPsSwitchPtoW.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:h3cTeTunnelPsSwitchPtoW.setStatus(_A)
h3cTeTunnelNotificationsGroup=NotificationGroup((1,3,6,1,4,1,2011,10,2,115,4,2,1))
h3cTeTunnelNotificationsGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:h3cTeTunnelNotificationsGroup.setStatus(_A)
h3cTeTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,115,4,1,1))
h3cTeTunnelCompliance.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:h3cTeTunnelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cTeTunnel':h3cTeTunnel,'h3cTeTunnelScalars':h3cTeTunnelScalars,_T:h3cTeTunnelMaxTunnelIndex,'h3cTeTunnelObjects':h3cTeTunnelObjects,'h3cTeTunnelStaticCrlspTable':h3cTeTunnelStaticCrlspTable,'h3cTeTunnelStaticCrlspEntry':h3cTeTunnelStaticCrlspEntry,_J:h3cTeTunnelStaticCrlspInLabel,_U:h3cTeTunnelStaticCrlspName,_V:h3cTeTunnelStaticCrlspStatus,_W:h3cTeTunnelStaticCrlspRole,_X:h3cTeTunnelStaticCrlspXCPointer,'h3cTeTunnelCoTable':h3cTeTunnelCoTable,'h3cTeTunnelCoEntry':h3cTeTunnelCoEntry,_K:h3cTeTunnelCoIndex,_L:h3cTeTunnelCoLspInstance,_M:h3cTeTunnelCoIngressLSRId,_N:h3cTeTunnelCoEgressLSRId,_Y:h3cTeTunnelCoBiMode,_Z:h3cTeTunnelCoReverseLspInstance,_a:h3cTeTunnelCoReverseLspXCPointer,'h3cTeTunnelPsTable':h3cTeTunnelPsTable,'h3cTeTunnelPsEntry':h3cTeTunnelPsEntry,_O:h3cTeTunnelPsIndex,_P:h3cTeTunnelPsIngressLSRId,_Q:h3cTeTunnelPsEgressLSRId,_b:h3cTeTunnelPsProtectIndex,_c:h3cTeTunnelPsProtectIngressLSRId,_d:h3cTeTunnelPsProtectEgressLSRId,_e:h3cTeTunnelPsProtectType,_f:h3cTeTunnelPsRevertiveMode,_g:h3cTeTunnelPsWtrTime,_h:h3cTeTunnelPsHoldOffTime,_i:h3cTeTunnelPsSwitchMode,_F:h3cTeTunnelPsWorkPathStatus,_G:h3cTeTunnelPsProtectPathStatus,_j:h3cTeTunnelPsSwitchResult,'h3cTeTunnelNotifications':h3cTeTunnelNotifications,'h3cTeTunnelNotificationsPrefix':h3cTeTunnelNotificationsPrefix,_l:h3cTeTunnelPsSwitchWtoP,_k:h3cTeTunnelPsSwitchPtoW,'h3cTeTunnelConformance':h3cTeTunnelConformance,'h3cTeTunnelCompliances':h3cTeTunnelCompliances,'h3cTeTunnelCompliance':h3cTeTunnelCompliance,'h3cTeTunnelGroups':h3cTeTunnelGroups,_m:h3cTeTunnelNotificationsGroup,_n:h3cTeTunnelScalarsGroup,_o:h3cTeTunnelStaticCrlspGroup,_p:h3cTeTunnelCorouteGroup,_q:h3cTeTunnelPsGroup})