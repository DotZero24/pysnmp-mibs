_q='hpnicfTeTunnelPsGroup'
_p='hpnicfTeTunnelCorouteGroup'
_o='hpnicfTeTunnelStaticCrlspGroup'
_n='hpnicfTeTunnelScalarsGroup'
_m='hpnicfTeTunnelNotificationsGroup'
_l='hpnicfTeTunnelPsSwitchWtoP'
_k='hpnicfTeTunnelPsSwitchPtoW'
_j='hpnicfTeTunnelPsSwitchResult'
_i='hpnicfTeTunnelPsSwitchMode'
_h='hpnicfTeTunnelPsHoldOffTime'
_g='hpnicfTeTunnelPsWtrTime'
_f='hpnicfTeTunnelPsRevertiveMode'
_e='hpnicfTeTunnelPsProtectType'
_d='hpnicfTeTunnelPsProtectEgressLSRId'
_c='hpnicfTeTunnelPsProtectIngressLSRId'
_b='hpnicfTeTunnelPsProtectIndex'
_a='hpnicfTeTunnelCoReverseLspXCPointer'
_Z='hpnicfTeTunnelCoReverseLspInstance'
_Y='hpnicfTeTunnelCoBiMode'
_X='hpnicfTeTunnelStaticCrlspXCPointer'
_W='hpnicfTeTunnelStaticCrlspRole'
_V='hpnicfTeTunnelStaticCrlspStatus'
_U='hpnicfTeTunnelStaticCrlspName'
_T='hpnicfTeTunnelMaxTunnelIndex'
_S='inDefect'
_R='noDefect'
_Q='hpnicfTeTunnelPsEgressLSRId'
_P='hpnicfTeTunnelPsIngressLSRId'
_O='hpnicfTeTunnelPsIndex'
_N='hpnicfTeTunnelCoEgressLSRId'
_M='hpnicfTeTunnelCoIngressLSRId'
_L='hpnicfTeTunnelCoLspInstance'
_K='hpnicfTeTunnelCoIndex'
_J='hpnicfTeTunnelStaticCrlspInLabel'
_I='OctetString'
_H='Unsigned32'
_G='hpnicfTeTunnelPsProtectPathStatus'
_F='hpnicfTeTunnelPsWorkPathStatus'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-TE-TUNNEL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
MplsExtendedTunnelId,MplsLabel,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsExtendedTunnelId','MplsLabel','MplsTunnelIndex','MplsTunnelInstanceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
hpnicfTeTunnel=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115))
_HpnicfTeTunnelScalars_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelScalars=_HpnicfTeTunnelScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,1))
_HpnicfTeTunnelMaxTunnelIndex_Type=MplsTunnelIndex
_HpnicfTeTunnelMaxTunnelIndex_Object=MibScalar
hpnicfTeTunnelMaxTunnelIndex=_HpnicfTeTunnelMaxTunnelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,1,1),_HpnicfTeTunnelMaxTunnelIndex_Type())
hpnicfTeTunnelMaxTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelMaxTunnelIndex.setStatus(_A)
_HpnicfTeTunnelObjects_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelObjects=_HpnicfTeTunnelObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,2))
_HpnicfTeTunnelStaticCrlspTable_Object=MibTable
hpnicfTeTunnelStaticCrlspTable=_HpnicfTeTunnelStaticCrlspTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1))
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspTable.setStatus(_A)
_HpnicfTeTunnelStaticCrlspEntry_Object=MibTableRow
hpnicfTeTunnelStaticCrlspEntry=_HpnicfTeTunnelStaticCrlspEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1))
hpnicfTeTunnelStaticCrlspEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspEntry.setStatus(_A)
_HpnicfTeTunnelStaticCrlspInLabel_Type=MplsLabel
_HpnicfTeTunnelStaticCrlspInLabel_Object=MibTableColumn
hpnicfTeTunnelStaticCrlspInLabel=_HpnicfTeTunnelStaticCrlspInLabel_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1,1),_HpnicfTeTunnelStaticCrlspInLabel_Type())
hpnicfTeTunnelStaticCrlspInLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspInLabel.setStatus(_A)
class _HpnicfTeTunnelStaticCrlspName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HpnicfTeTunnelStaticCrlspName_Type.__name__=_I
_HpnicfTeTunnelStaticCrlspName_Object=MibTableColumn
hpnicfTeTunnelStaticCrlspName=_HpnicfTeTunnelStaticCrlspName_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1,2),_HpnicfTeTunnelStaticCrlspName_Type())
hpnicfTeTunnelStaticCrlspName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspName.setStatus(_A)
class _HpnicfTeTunnelStaticCrlspStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpnicfTeTunnelStaticCrlspStatus_Type.__name__=_D
_HpnicfTeTunnelStaticCrlspStatus_Object=MibTableColumn
hpnicfTeTunnelStaticCrlspStatus=_HpnicfTeTunnelStaticCrlspStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1,3),_HpnicfTeTunnelStaticCrlspStatus_Type())
hpnicfTeTunnelStaticCrlspStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspStatus.setStatus(_A)
class _HpnicfTeTunnelStaticCrlspRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transit',1),('tail',2)))
_HpnicfTeTunnelStaticCrlspRole_Type.__name__=_D
_HpnicfTeTunnelStaticCrlspRole_Object=MibTableColumn
hpnicfTeTunnelStaticCrlspRole=_HpnicfTeTunnelStaticCrlspRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1,4),_HpnicfTeTunnelStaticCrlspRole_Type())
hpnicfTeTunnelStaticCrlspRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspRole.setStatus(_A)
_HpnicfTeTunnelStaticCrlspXCPointer_Type=RowPointer
_HpnicfTeTunnelStaticCrlspXCPointer_Object=MibTableColumn
hpnicfTeTunnelStaticCrlspXCPointer=_HpnicfTeTunnelStaticCrlspXCPointer_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,1,1,5),_HpnicfTeTunnelStaticCrlspXCPointer_Type())
hpnicfTeTunnelStaticCrlspXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspXCPointer.setStatus(_A)
_HpnicfTeTunnelCoTable_Object=MibTable
hpnicfTeTunnelCoTable=_HpnicfTeTunnelCoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2))
if mibBuilder.loadTexts:hpnicfTeTunnelCoTable.setStatus(_A)
_HpnicfTeTunnelCoEntry_Object=MibTableRow
hpnicfTeTunnelCoEntry=_HpnicfTeTunnelCoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1))
hpnicfTeTunnelCoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfTeTunnelCoEntry.setStatus(_A)
_HpnicfTeTunnelCoIndex_Type=MplsTunnelIndex
_HpnicfTeTunnelCoIndex_Object=MibTableColumn
hpnicfTeTunnelCoIndex=_HpnicfTeTunnelCoIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,1),_HpnicfTeTunnelCoIndex_Type())
hpnicfTeTunnelCoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelCoIndex.setStatus(_A)
_HpnicfTeTunnelCoLspInstance_Type=MplsTunnelInstanceIndex
_HpnicfTeTunnelCoLspInstance_Object=MibTableColumn
hpnicfTeTunnelCoLspInstance=_HpnicfTeTunnelCoLspInstance_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,2),_HpnicfTeTunnelCoLspInstance_Type())
hpnicfTeTunnelCoLspInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelCoLspInstance.setStatus(_A)
_HpnicfTeTunnelCoIngressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelCoIngressLSRId_Object=MibTableColumn
hpnicfTeTunnelCoIngressLSRId=_HpnicfTeTunnelCoIngressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,3),_HpnicfTeTunnelCoIngressLSRId_Type())
hpnicfTeTunnelCoIngressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelCoIngressLSRId.setStatus(_A)
_HpnicfTeTunnelCoEgressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelCoEgressLSRId_Object=MibTableColumn
hpnicfTeTunnelCoEgressLSRId=_HpnicfTeTunnelCoEgressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,4),_HpnicfTeTunnelCoEgressLSRId_Type())
hpnicfTeTunnelCoEgressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelCoEgressLSRId.setStatus(_A)
class _HpnicfTeTunnelCoBiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coroutedActive',1),('coroutedPassive',2)))
_HpnicfTeTunnelCoBiMode_Type.__name__=_D
_HpnicfTeTunnelCoBiMode_Object=MibTableColumn
hpnicfTeTunnelCoBiMode=_HpnicfTeTunnelCoBiMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,5),_HpnicfTeTunnelCoBiMode_Type())
hpnicfTeTunnelCoBiMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelCoBiMode.setStatus(_A)
_HpnicfTeTunnelCoReverseLspInstance_Type=MplsTunnelInstanceIndex
_HpnicfTeTunnelCoReverseLspInstance_Object=MibTableColumn
hpnicfTeTunnelCoReverseLspInstance=_HpnicfTeTunnelCoReverseLspInstance_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,6),_HpnicfTeTunnelCoReverseLspInstance_Type())
hpnicfTeTunnelCoReverseLspInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelCoReverseLspInstance.setStatus(_A)
_HpnicfTeTunnelCoReverseLspXCPointer_Type=RowPointer
_HpnicfTeTunnelCoReverseLspXCPointer_Object=MibTableColumn
hpnicfTeTunnelCoReverseLspXCPointer=_HpnicfTeTunnelCoReverseLspXCPointer_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,2,1,7),_HpnicfTeTunnelCoReverseLspXCPointer_Type())
hpnicfTeTunnelCoReverseLspXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelCoReverseLspXCPointer.setStatus(_A)
_HpnicfTeTunnelPsTable_Object=MibTable
hpnicfTeTunnelPsTable=_HpnicfTeTunnelPsTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3))
if mibBuilder.loadTexts:hpnicfTeTunnelPsTable.setStatus(_A)
_HpnicfTeTunnelPsEntry_Object=MibTableRow
hpnicfTeTunnelPsEntry=_HpnicfTeTunnelPsEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1))
hpnicfTeTunnelPsEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfTeTunnelPsEntry.setStatus(_A)
_HpnicfTeTunnelPsIndex_Type=MplsTunnelIndex
_HpnicfTeTunnelPsIndex_Object=MibTableColumn
hpnicfTeTunnelPsIndex=_HpnicfTeTunnelPsIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,1),_HpnicfTeTunnelPsIndex_Type())
hpnicfTeTunnelPsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelPsIndex.setStatus(_A)
_HpnicfTeTunnelPsIngressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelPsIngressLSRId_Object=MibTableColumn
hpnicfTeTunnelPsIngressLSRId=_HpnicfTeTunnelPsIngressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,2),_HpnicfTeTunnelPsIngressLSRId_Type())
hpnicfTeTunnelPsIngressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelPsIngressLSRId.setStatus(_A)
_HpnicfTeTunnelPsEgressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelPsEgressLSRId_Object=MibTableColumn
hpnicfTeTunnelPsEgressLSRId=_HpnicfTeTunnelPsEgressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,3),_HpnicfTeTunnelPsEgressLSRId_Type())
hpnicfTeTunnelPsEgressLSRId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTeTunnelPsEgressLSRId.setStatus(_A)
_HpnicfTeTunnelPsProtectIndex_Type=MplsTunnelIndex
_HpnicfTeTunnelPsProtectIndex_Object=MibTableColumn
hpnicfTeTunnelPsProtectIndex=_HpnicfTeTunnelPsProtectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,4),_HpnicfTeTunnelPsProtectIndex_Type())
hpnicfTeTunnelPsProtectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsProtectIndex.setStatus(_A)
_HpnicfTeTunnelPsProtectIngressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelPsProtectIngressLSRId_Object=MibTableColumn
hpnicfTeTunnelPsProtectIngressLSRId=_HpnicfTeTunnelPsProtectIngressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,5),_HpnicfTeTunnelPsProtectIngressLSRId_Type())
hpnicfTeTunnelPsProtectIngressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsProtectIngressLSRId.setStatus(_A)
_HpnicfTeTunnelPsProtectEgressLSRId_Type=MplsExtendedTunnelId
_HpnicfTeTunnelPsProtectEgressLSRId_Object=MibTableColumn
hpnicfTeTunnelPsProtectEgressLSRId=_HpnicfTeTunnelPsProtectEgressLSRId_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,6),_HpnicfTeTunnelPsProtectEgressLSRId_Type())
hpnicfTeTunnelPsProtectEgressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsProtectEgressLSRId.setStatus(_A)
class _HpnicfTeTunnelPsProtectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneToOne',1),('onePlusOne',2)))
_HpnicfTeTunnelPsProtectType_Type.__name__=_D
_HpnicfTeTunnelPsProtectType_Object=MibTableColumn
hpnicfTeTunnelPsProtectType=_HpnicfTeTunnelPsProtectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,7),_HpnicfTeTunnelPsProtectType_Type())
hpnicfTeTunnelPsProtectType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsProtectType.setStatus(_A)
class _HpnicfTeTunnelPsRevertiveMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('noRevertive',2)))
_HpnicfTeTunnelPsRevertiveMode_Type.__name__=_D
_HpnicfTeTunnelPsRevertiveMode_Object=MibTableColumn
hpnicfTeTunnelPsRevertiveMode=_HpnicfTeTunnelPsRevertiveMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,8),_HpnicfTeTunnelPsRevertiveMode_Type())
hpnicfTeTunnelPsRevertiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsRevertiveMode.setStatus(_A)
class _HpnicfTeTunnelPsWtrTime_Type(Unsigned32):defaultValue=24;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HpnicfTeTunnelPsWtrTime_Type.__name__=_H
_HpnicfTeTunnelPsWtrTime_Object=MibTableColumn
hpnicfTeTunnelPsWtrTime=_HpnicfTeTunnelPsWtrTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,9),_HpnicfTeTunnelPsWtrTime_Type())
hpnicfTeTunnelPsWtrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsWtrTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfTeTunnelPsWtrTime.setUnits('30 seconds')
class _HpnicfTeTunnelPsHoldOffTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_HpnicfTeTunnelPsHoldOffTime_Type.__name__=_H
_HpnicfTeTunnelPsHoldOffTime_Object=MibTableColumn
hpnicfTeTunnelPsHoldOffTime=_HpnicfTeTunnelPsHoldOffTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,10),_HpnicfTeTunnelPsHoldOffTime_Type())
hpnicfTeTunnelPsHoldOffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfTeTunnelPsHoldOffTime.setUnits('500ms')
class _HpnicfTeTunnelPsSwitchMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uniDirectional',1),('biDirectional',2)))
_HpnicfTeTunnelPsSwitchMode_Type.__name__=_D
_HpnicfTeTunnelPsSwitchMode_Object=MibTableColumn
hpnicfTeTunnelPsSwitchMode=_HpnicfTeTunnelPsSwitchMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,11),_HpnicfTeTunnelPsSwitchMode_Type())
hpnicfTeTunnelPsSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsSwitchMode.setStatus(_A)
class _HpnicfTeTunnelPsWorkPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_R,2),(_S,3)))
_HpnicfTeTunnelPsWorkPathStatus_Type.__name__=_D
_HpnicfTeTunnelPsWorkPathStatus_Object=MibTableColumn
hpnicfTeTunnelPsWorkPathStatus=_HpnicfTeTunnelPsWorkPathStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,12),_HpnicfTeTunnelPsWorkPathStatus_Type())
hpnicfTeTunnelPsWorkPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsWorkPathStatus.setStatus(_A)
class _HpnicfTeTunnelPsProtectPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_R,2),(_S,3)))
_HpnicfTeTunnelPsProtectPathStatus_Type.__name__=_D
_HpnicfTeTunnelPsProtectPathStatus_Object=MibTableColumn
hpnicfTeTunnelPsProtectPathStatus=_HpnicfTeTunnelPsProtectPathStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,13),_HpnicfTeTunnelPsProtectPathStatus_Type())
hpnicfTeTunnelPsProtectPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsProtectPathStatus.setStatus(_A)
class _HpnicfTeTunnelPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('workPath',1),('protectPath',2)))
_HpnicfTeTunnelPsSwitchResult_Type.__name__=_D
_HpnicfTeTunnelPsSwitchResult_Object=MibTableColumn
hpnicfTeTunnelPsSwitchResult=_HpnicfTeTunnelPsSwitchResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,115,2,3,1,14),_HpnicfTeTunnelPsSwitchResult_Type())
hpnicfTeTunnelPsSwitchResult.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTeTunnelPsSwitchResult.setStatus(_A)
_HpnicfTeTunnelNotifications_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelNotifications=_HpnicfTeTunnelNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,3))
_HpnicfTeTunnelNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelNotificationsPrefix=_HpnicfTeTunnelNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,3,0))
_HpnicfTeTunnelConformance_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelConformance=_HpnicfTeTunnelConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,4))
_HpnicfTeTunnelCompliances_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelCompliances=_HpnicfTeTunnelCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,4,1))
_HpnicfTeTunnelGroups_ObjectIdentity=ObjectIdentity
hpnicfTeTunnelGroups=_HpnicfTeTunnelGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2))
hpnicfTeTunnelScalarsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2,2))
hpnicfTeTunnelScalarsGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:hpnicfTeTunnelScalarsGroup.setStatus(_A)
hpnicfTeTunnelStaticCrlspGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2,3))
hpnicfTeTunnelStaticCrlspGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpnicfTeTunnelStaticCrlspGroup.setStatus(_A)
hpnicfTeTunnelCorouteGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2,4))
hpnicfTeTunnelCorouteGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpnicfTeTunnelCorouteGroup.setStatus(_A)
hpnicfTeTunnelPsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2,5))
hpnicfTeTunnelPsGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_F),(_B,_G),(_B,_j)))
if mibBuilder.loadTexts:hpnicfTeTunnelPsGroup.setStatus(_A)
hpnicfTeTunnelPsSwitchWtoP=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,115,3,0,1))
hpnicfTeTunnelPsSwitchWtoP.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:hpnicfTeTunnelPsSwitchWtoP.setStatus(_A)
hpnicfTeTunnelPsSwitchPtoW=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,115,3,0,2))
hpnicfTeTunnelPsSwitchPtoW.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:hpnicfTeTunnelPsSwitchPtoW.setStatus(_A)
hpnicfTeTunnelNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,115,4,2,1))
hpnicfTeTunnelNotificationsGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:hpnicfTeTunnelNotificationsGroup.setStatus(_A)
hpnicfTeTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,115,4,1,1))
hpnicfTeTunnelCompliance.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:hpnicfTeTunnelCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfTeTunnel':hpnicfTeTunnel,'hpnicfTeTunnelScalars':hpnicfTeTunnelScalars,_T:hpnicfTeTunnelMaxTunnelIndex,'hpnicfTeTunnelObjects':hpnicfTeTunnelObjects,'hpnicfTeTunnelStaticCrlspTable':hpnicfTeTunnelStaticCrlspTable,'hpnicfTeTunnelStaticCrlspEntry':hpnicfTeTunnelStaticCrlspEntry,_J:hpnicfTeTunnelStaticCrlspInLabel,_U:hpnicfTeTunnelStaticCrlspName,_V:hpnicfTeTunnelStaticCrlspStatus,_W:hpnicfTeTunnelStaticCrlspRole,_X:hpnicfTeTunnelStaticCrlspXCPointer,'hpnicfTeTunnelCoTable':hpnicfTeTunnelCoTable,'hpnicfTeTunnelCoEntry':hpnicfTeTunnelCoEntry,_K:hpnicfTeTunnelCoIndex,_L:hpnicfTeTunnelCoLspInstance,_M:hpnicfTeTunnelCoIngressLSRId,_N:hpnicfTeTunnelCoEgressLSRId,_Y:hpnicfTeTunnelCoBiMode,_Z:hpnicfTeTunnelCoReverseLspInstance,_a:hpnicfTeTunnelCoReverseLspXCPointer,'hpnicfTeTunnelPsTable':hpnicfTeTunnelPsTable,'hpnicfTeTunnelPsEntry':hpnicfTeTunnelPsEntry,_O:hpnicfTeTunnelPsIndex,_P:hpnicfTeTunnelPsIngressLSRId,_Q:hpnicfTeTunnelPsEgressLSRId,_b:hpnicfTeTunnelPsProtectIndex,_c:hpnicfTeTunnelPsProtectIngressLSRId,_d:hpnicfTeTunnelPsProtectEgressLSRId,_e:hpnicfTeTunnelPsProtectType,_f:hpnicfTeTunnelPsRevertiveMode,_g:hpnicfTeTunnelPsWtrTime,_h:hpnicfTeTunnelPsHoldOffTime,_i:hpnicfTeTunnelPsSwitchMode,_F:hpnicfTeTunnelPsWorkPathStatus,_G:hpnicfTeTunnelPsProtectPathStatus,_j:hpnicfTeTunnelPsSwitchResult,'hpnicfTeTunnelNotifications':hpnicfTeTunnelNotifications,'hpnicfTeTunnelNotificationsPrefix':hpnicfTeTunnelNotificationsPrefix,_l:hpnicfTeTunnelPsSwitchWtoP,_k:hpnicfTeTunnelPsSwitchPtoW,'hpnicfTeTunnelConformance':hpnicfTeTunnelConformance,'hpnicfTeTunnelCompliances':hpnicfTeTunnelCompliances,'hpnicfTeTunnelCompliance':hpnicfTeTunnelCompliance,'hpnicfTeTunnelGroups':hpnicfTeTunnelGroups,_m:hpnicfTeTunnelNotificationsGroup,_n:hpnicfTeTunnelScalarsGroup,_o:hpnicfTeTunnelStaticCrlspGroup,_p:hpnicfTeTunnelCorouteGroup,_q:hpnicfTeTunnelPsGroup})