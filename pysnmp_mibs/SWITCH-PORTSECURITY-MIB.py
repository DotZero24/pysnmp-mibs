_U='rcPortSecLastDelMacFlag'
_T='rcPortSecLastDelMacVlan'
_S='rcPortSecLastDelMacAddress'
_R='rcPortSecLastAgingMacVlan'
_Q='rcPortSecLastAgingMacAddress'
_P='rcPortSecLastAccessMacVlan'
_O='rcPortSecLastAccessMacAddress'
_N='rcPortSecFlag'
_M='rcPortSecPort'
_L='sticky'
_K='dynamic'
_J='static'
_I='rcPortSecIndx'
_H='read-create'
_G='rcPortSecMac'
_F='rcPortSecVlan'
_E='read-write'
_D='read-only'
_C='SWITCH-PORTSECURITY-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcPortsecurity=ModuleIdentity((1,3,6,1,4,1,8886,6,1,49))
_RcPortSecCfg_ObjectIdentity=ObjectIdentity
rcPortSecCfg=_RcPortSecCfg_ObjectIdentity((1,3,6,1,4,1,8886,6,1,49,1))
class _RcPortSecMacAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_RcPortSecMacAgingTime_Type.__name__=_B
_RcPortSecMacAgingTime_Object=MibScalar
rcPortSecMacAgingTime=_RcPortSecMacAgingTime_Object((1,3,6,1,4,1,8886,6,1,49,1,1),_RcPortSecMacAgingTime_Type())
rcPortSecMacAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecMacAgingTime.setStatus(_A)
_RcPortSecTable_Object=MibTable
rcPortSecTable=_RcPortSecTable_Object((1,3,6,1,4,1,8886,6,1,49,2))
if mibBuilder.loadTexts:rcPortSecTable.setStatus(_A)
_RcPortSecEntry_Object=MibTableRow
rcPortSecEntry=_RcPortSecEntry_Object((1,3,6,1,4,1,8886,6,1,49,2,1))
rcPortSecEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:rcPortSecEntry.setStatus(_A)
_RcPortSecIndx_Type=Integer32
_RcPortSecIndx_Object=MibTableColumn
rcPortSecIndx=_RcPortSecIndx_Object((1,3,6,1,4,1,8886,6,1,49,2,1,1),_RcPortSecIndx_Type())
rcPortSecIndx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcPortSecIndx.setStatus(_A)
_RcPortSecEnable_Type=EnableVar
_RcPortSecEnable_Object=MibTableColumn
rcPortSecEnable=_RcPortSecEnable_Object((1,3,6,1,4,1,8886,6,1,49,2,1,2),_RcPortSecEnable_Type())
rcPortSecEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecEnable.setStatus(_A)
class _RcPortSecMaxAllowedMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RcPortSecMaxAllowedMac_Type.__name__=_B
_RcPortSecMaxAllowedMac_Object=MibTableColumn
rcPortSecMaxAllowedMac=_RcPortSecMaxAllowedMac_Object((1,3,6,1,4,1,8886,6,1,49,2,1,3),_RcPortSecMaxAllowedMac_Type())
rcPortSecMaxAllowedMac.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecMaxAllowedMac.setStatus(_A)
class _RcPortSecMacViolationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_RcPortSecMacViolationAction_Type.__name__=_B
_RcPortSecMacViolationAction_Object=MibTableColumn
rcPortSecMacViolationAction=_RcPortSecMacViolationAction_Object((1,3,6,1,4,1,8886,6,1,49,2,1,4),_RcPortSecMacViolationAction_Type())
rcPortSecMacViolationAction.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecMacViolationAction.setStatus(_A)
class _RcPortSecShutUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_RcPortSecShutUp_Type.__name__=_B
_RcPortSecShutUp_Object=MibTableColumn
rcPortSecShutUp=_RcPortSecShutUp_Object((1,3,6,1,4,1,8886,6,1,49,2,1,5),_RcPortSecShutUp_Type())
rcPortSecShutUp.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecShutUp.setStatus(_A)
_RcPortSecMacStickyEnable_Type=EnableVar
_RcPortSecMacStickyEnable_Object=MibTableColumn
rcPortSecMacStickyEnable=_RcPortSecMacStickyEnable_Object((1,3,6,1,4,1,8886,6,1,49,2,1,6),_RcPortSecMacStickyEnable_Type())
rcPortSecMacStickyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecMacStickyEnable.setStatus(_A)
_RcPortSecTrapEnable_Type=EnableVar
_RcPortSecTrapEnable_Object=MibTableColumn
rcPortSecTrapEnable=_RcPortSecTrapEnable_Object((1,3,6,1,4,1,8886,6,1,49,2,1,7),_RcPortSecTrapEnable_Type())
rcPortSecTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecTrapEnable.setStatus(_A)
class _RcPortSecMacDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RcPortSecMacDel_Type.__name__=_B
_RcPortSecMacDel_Object=MibTableColumn
rcPortSecMacDel=_RcPortSecMacDel_Object((1,3,6,1,4,1,8886,6,1,49,2,1,8),_RcPortSecMacDel_Type())
rcPortSecMacDel.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPortSecMacDel.setStatus(_A)
class _RcPortSecCurMacNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RcPortSecCurMacNum_Type.__name__=_B
_RcPortSecCurMacNum_Object=MibTableColumn
rcPortSecCurMacNum=_RcPortSecCurMacNum_Object((1,3,6,1,4,1,8886,6,1,49,2,1,9),_RcPortSecCurMacNum_Type())
rcPortSecCurMacNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecCurMacNum.setStatus(_A)
class _RcPortSecMaxMacs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RcPortSecMaxMacs_Type.__name__=_B
_RcPortSecMaxMacs_Object=MibTableColumn
rcPortSecMaxMacs=_RcPortSecMaxMacs_Object((1,3,6,1,4,1,8886,6,1,49,2,1,10),_RcPortSecMaxMacs_Type())
rcPortSecMaxMacs.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecMaxMacs.setStatus(_A)
class _RcPortSecMacViolations_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcPortSecMacViolations_Type.__name__=_B
_RcPortSecMacViolations_Object=MibTableColumn
rcPortSecMacViolations=_RcPortSecMacViolations_Object((1,3,6,1,4,1,8886,6,1,49,2,1,11),_RcPortSecMacViolations_Type())
rcPortSecMacViolations.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecMacViolations.setStatus(_A)
class _RcPortSecViolationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_RcPortSecViolationStatus_Type.__name__=_B
_RcPortSecViolationStatus_Object=MibTableColumn
rcPortSecViolationStatus=_RcPortSecViolationStatus_Object((1,3,6,1,4,1,8886,6,1,49,2,1,12),_RcPortSecViolationStatus_Type())
rcPortSecViolationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecViolationStatus.setStatus(_A)
_RcPortSecLastAccessMacAddress_Type=MacAddress
_RcPortSecLastAccessMacAddress_Object=MibTableColumn
rcPortSecLastAccessMacAddress=_RcPortSecLastAccessMacAddress_Object((1,3,6,1,4,1,8886,6,1,49,2,1,13),_RcPortSecLastAccessMacAddress_Type())
rcPortSecLastAccessMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastAccessMacAddress.setStatus(_A)
class _RcPortSecLastAccessMacVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortSecLastAccessMacVlan_Type.__name__=_B
_RcPortSecLastAccessMacVlan_Object=MibTableColumn
rcPortSecLastAccessMacVlan=_RcPortSecLastAccessMacVlan_Object((1,3,6,1,4,1,8886,6,1,49,2,1,14),_RcPortSecLastAccessMacVlan_Type())
rcPortSecLastAccessMacVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastAccessMacVlan.setStatus(_A)
_RcPortSecLastAgingMacAddress_Type=MacAddress
_RcPortSecLastAgingMacAddress_Object=MibTableColumn
rcPortSecLastAgingMacAddress=_RcPortSecLastAgingMacAddress_Object((1,3,6,1,4,1,8886,6,1,49,2,1,15),_RcPortSecLastAgingMacAddress_Type())
rcPortSecLastAgingMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastAgingMacAddress.setStatus(_A)
class _RcPortSecLastAgingMacVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortSecLastAgingMacVlan_Type.__name__=_B
_RcPortSecLastAgingMacVlan_Object=MibTableColumn
rcPortSecLastAgingMacVlan=_RcPortSecLastAgingMacVlan_Object((1,3,6,1,4,1,8886,6,1,49,2,1,16),_RcPortSecLastAgingMacVlan_Type())
rcPortSecLastAgingMacVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastAgingMacVlan.setStatus(_A)
_RcPortSecLastDelMacAddress_Type=MacAddress
_RcPortSecLastDelMacAddress_Object=MibTableColumn
rcPortSecLastDelMacAddress=_RcPortSecLastDelMacAddress_Object((1,3,6,1,4,1,8886,6,1,49,2,1,17),_RcPortSecLastDelMacAddress_Type())
rcPortSecLastDelMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastDelMacAddress.setStatus(_A)
class _RcPortSecLastDelMacVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortSecLastDelMacVlan_Type.__name__=_B
_RcPortSecLastDelMacVlan_Object=MibTableColumn
rcPortSecLastDelMacVlan=_RcPortSecLastDelMacVlan_Object((1,3,6,1,4,1,8886,6,1,49,2,1,18),_RcPortSecLastDelMacVlan_Type())
rcPortSecLastDelMacVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastDelMacVlan.setStatus(_A)
class _RcPortSecLastDelMacFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_RcPortSecLastDelMacFlag_Type.__name__=_B
_RcPortSecLastDelMacFlag_Object=MibTableColumn
rcPortSecLastDelMacFlag=_RcPortSecLastDelMacFlag_Object((1,3,6,1,4,1,8886,6,1,49,2,1,19),_RcPortSecLastDelMacFlag_Type())
rcPortSecLastDelMacFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecLastDelMacFlag.setStatus(_A)
_RcPortSecMacTable_Object=MibTable
rcPortSecMacTable=_RcPortSecMacTable_Object((1,3,6,1,4,1,8886,6,1,49,3))
if mibBuilder.loadTexts:rcPortSecMacTable.setStatus(_A)
_RcPortSecMacEntry_Object=MibTableRow
rcPortSecMacEntry=_RcPortSecMacEntry_Object((1,3,6,1,4,1,8886,6,1,49,3,1))
rcPortSecMacEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rcPortSecMacEntry.setStatus(_A)
class _RcPortSecVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcPortSecVlan_Type.__name__=_B
_RcPortSecVlan_Object=MibTableColumn
rcPortSecVlan=_RcPortSecVlan_Object((1,3,6,1,4,1,8886,6,1,49,3,1,1),_RcPortSecVlan_Type())
rcPortSecVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecVlan.setStatus(_A)
_RcPortSecMac_Type=MacAddress
_RcPortSecMac_Object=MibTableColumn
rcPortSecMac=_RcPortSecMac_Object((1,3,6,1,4,1,8886,6,1,49,3,1,2),_RcPortSecMac_Type())
rcPortSecMac.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecMac.setStatus(_A)
_RcPortSecPort_Type=Integer32
_RcPortSecPort_Object=MibTableColumn
rcPortSecPort=_RcPortSecPort_Object((1,3,6,1,4,1,8886,6,1,49,3,1,3),_RcPortSecPort_Type())
rcPortSecPort.setMaxAccess(_H)
if mibBuilder.loadTexts:rcPortSecPort.setStatus(_A)
class _RcPortSecFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3)))
_RcPortSecFlag_Type.__name__=_B
_RcPortSecFlag_Object=MibTableColumn
rcPortSecFlag=_RcPortSecFlag_Object((1,3,6,1,4,1,8886,6,1,49,3,1,4),_RcPortSecFlag_Type())
rcPortSecFlag.setMaxAccess(_H)
if mibBuilder.loadTexts:rcPortSecFlag.setStatus(_A)
class _RcPortSecAgingTm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_RcPortSecAgingTm_Type.__name__=_B
_RcPortSecAgingTm_Object=MibTableColumn
rcPortSecAgingTm=_RcPortSecAgingTm_Object((1,3,6,1,4,1,8886,6,1,49,3,1,5),_RcPortSecAgingTm_Type())
rcPortSecAgingTm.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPortSecAgingTm.setStatus(_A)
_RcPortSecRowStatus_Type=RowStatus
_RcPortSecRowStatus_Object=MibTableColumn
rcPortSecRowStatus=_RcPortSecRowStatus_Object((1,3,6,1,4,1,8886,6,1,49,3,1,6),_RcPortSecRowStatus_Type())
rcPortSecRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rcPortSecRowStatus.setStatus(_A)
_RcPortSecTrapGroup_ObjectIdentity=ObjectIdentity
rcPortSecTrapGroup=_RcPortSecTrapGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,49,4))
rcPortSecLearningTrap=NotificationType((1,3,6,1,4,1,8886,6,1,49,4,1))
rcPortSecLearningTrap.setObjects(*((_C,_F),(_C,_G),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:rcPortSecLearningTrap.setStatus(_A)
rcPortSecViolationTrap=NotificationType((1,3,6,1,4,1,8886,6,1,49,4,2))
rcPortSecViolationTrap.setObjects(*((_C,_O),(_C,_P)))
if mibBuilder.loadTexts:rcPortSecViolationTrap.setStatus(_A)
rcPortSecAgingTrap=NotificationType((1,3,6,1,4,1,8886,6,1,49,4,3))
rcPortSecAgingTrap.setObjects(*((_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:rcPortSecAgingTrap.setStatus(_A)
rcPortSecDelTrap=NotificationType((1,3,6,1,4,1,8886,6,1,49,4,4))
rcPortSecDelTrap.setObjects(*((_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:rcPortSecDelTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcPortsecurity':rcPortsecurity,'rcPortSecCfg':rcPortSecCfg,'rcPortSecMacAgingTime':rcPortSecMacAgingTime,'rcPortSecTable':rcPortSecTable,'rcPortSecEntry':rcPortSecEntry,_I:rcPortSecIndx,'rcPortSecEnable':rcPortSecEnable,'rcPortSecMaxAllowedMac':rcPortSecMaxAllowedMac,'rcPortSecMacViolationAction':rcPortSecMacViolationAction,'rcPortSecShutUp':rcPortSecShutUp,'rcPortSecMacStickyEnable':rcPortSecMacStickyEnable,'rcPortSecTrapEnable':rcPortSecTrapEnable,'rcPortSecMacDel':rcPortSecMacDel,'rcPortSecCurMacNum':rcPortSecCurMacNum,'rcPortSecMaxMacs':rcPortSecMaxMacs,'rcPortSecMacViolations':rcPortSecMacViolations,'rcPortSecViolationStatus':rcPortSecViolationStatus,_O:rcPortSecLastAccessMacAddress,_P:rcPortSecLastAccessMacVlan,_Q:rcPortSecLastAgingMacAddress,_R:rcPortSecLastAgingMacVlan,_S:rcPortSecLastDelMacAddress,_T:rcPortSecLastDelMacVlan,_U:rcPortSecLastDelMacFlag,'rcPortSecMacTable':rcPortSecMacTable,'rcPortSecMacEntry':rcPortSecMacEntry,_F:rcPortSecVlan,_G:rcPortSecMac,_M:rcPortSecPort,_N:rcPortSecFlag,'rcPortSecAgingTm':rcPortSecAgingTm,'rcPortSecRowStatus':rcPortSecRowStatus,'rcPortSecTrapGroup':rcPortSecTrapGroup,'rcPortSecLearningTrap':rcPortSecLearningTrap,'rcPortSecViolationTrap':rcPortSecViolationTrap,'rcPortSecAgingTrap':rcPortSecAgingTrap,'rcPortSecDelTrap':rcPortSecDelTrap})