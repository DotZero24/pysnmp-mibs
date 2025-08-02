_H='specialDB'
_G='ieee8021'
_F='relay'
_E='filter'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bridge,layerMgmt=mibBuilder.importSymbols('IRM-OIDS','bridge','layerMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_BridgeRev1_ObjectIdentity=ObjectIdentity
bridgeRev1=_BridgeRev1_ObjectIdentity((1,3,6,1,4,1,52,1,3,1))
_Bdgdevice_ObjectIdentity=ObjectIdentity
bdgdevice=_Bdgdevice_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,1))
class _BdgdeviceDisableBdg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disableBridge',0),('enableBridge',1)))
_BdgdeviceDisableBdg_Type.__name__=_D
_BdgdeviceDisableBdg_Object=MibScalar
bdgdeviceDisableBdg=_BdgdeviceDisableBdg_Object((1,3,6,1,4,1,52,1,3,1,1,1),_BdgdeviceDisableBdg_Type())
bdgdeviceDisableBdg.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceDisableBdg.setStatus(_A)
class _BdgdeviceRestoreSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('restoreSettings',0))
_BdgdeviceRestoreSettings_Type.__name__=_D
_BdgdeviceRestoreSettings_Object=MibScalar
bdgdeviceRestoreSettings=_BdgdeviceRestoreSettings_Object((1,3,6,1,4,1,52,1,3,1,1,2),_BdgdeviceRestoreSettings_Type())
bdgdeviceRestoreSettings.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceRestoreSettings.setStatus(_A)
_BdgdeviceBdgName_Type=OctetString
_BdgdeviceBdgName_Object=MibScalar
bdgdeviceBdgName=_BdgdeviceBdgName_Object((1,3,6,1,4,1,52,1,3,1,1,4),_BdgdeviceBdgName_Type())
bdgdeviceBdgName.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceBdgName.setStatus(_A)
_BdgdeviceNumPorts_Type=Integer32
_BdgdeviceNumPorts_Object=MibScalar
bdgdeviceNumPorts=_BdgdeviceNumPorts_Object((1,3,6,1,4,1,52,1,3,1,1,5),_BdgdeviceNumPorts_Type())
bdgdeviceNumPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceNumPorts.setStatus(_A)
_BdgdeviceType_Type=OctetString
_BdgdeviceType_Object=MibScalar
bdgdeviceType=_BdgdeviceType_Object((1,3,6,1,4,1,52,1,3,1,1,6),_BdgdeviceType_Type())
bdgdeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceType.setStatus(_A)
_BdgdeviceVersion_Type=OctetString
_BdgdeviceVersion_Object=MibScalar
bdgdeviceVersion=_BdgdeviceVersion_Object((1,3,6,1,4,1,52,1,3,1,1,7),_BdgdeviceVersion_Type())
bdgdeviceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceVersion.setStatus(_A)
_BdgdeviceLocation_Type=OctetString
_BdgdeviceLocation_Object=MibScalar
bdgdeviceLocation=_BdgdeviceLocation_Object((1,3,6,1,4,1,52,1,3,1,1,8),_BdgdeviceLocation_Type())
bdgdeviceLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceLocation.setStatus(_A)
_BdgdeviceStatus_Type=OctetString
_BdgdeviceStatus_Object=MibScalar
bdgdeviceStatus=_BdgdeviceStatus_Object((1,3,6,1,4,1,52,1,3,1,1,9),_BdgdeviceStatus_Type())
bdgdeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceStatus.setStatus(_A)
class _BdgdeviceRestartBdg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('restartBridge',0))
_BdgdeviceRestartBdg_Type.__name__=_D
_BdgdeviceRestartBdg_Object=MibScalar
bdgdeviceRestartBdg=_BdgdeviceRestartBdg_Object((1,3,6,1,4,1,52,1,3,1,1,10),_BdgdeviceRestartBdg_Type())
bdgdeviceRestartBdg.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceRestartBdg.setStatus(_A)
_BdgdeviceFrFwd_Type=Counter32
_BdgdeviceFrFwd_Object=MibScalar
bdgdeviceFrFwd=_BdgdeviceFrFwd_Object((1,3,6,1,4,1,52,1,3,1,1,11),_BdgdeviceFrFwd_Type())
bdgdeviceFrFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceFrFwd.setStatus(_A)
_BdgdeviceFrRx_Type=Counter32
_BdgdeviceFrRx_Object=MibScalar
bdgdeviceFrRx=_BdgdeviceFrRx_Object((1,3,6,1,4,1,52,1,3,1,1,12),_BdgdeviceFrRx_Type())
bdgdeviceFrRx.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceFrRx.setStatus(_A)
_BdgdeviceFrFlt_Type=Counter32
_BdgdeviceFrFlt_Object=MibScalar
bdgdeviceFrFlt=_BdgdeviceFrFlt_Object((1,3,6,1,4,1,52,1,3,1,1,13),_BdgdeviceFrFlt_Type())
bdgdeviceFrFlt.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceFrFlt.setStatus(_A)
_BdgdeviceErr_Type=Counter32
_BdgdeviceErr_Object=MibScalar
bdgdeviceErr=_BdgdeviceErr_Object((1,3,6,1,4,1,52,1,3,1,1,14),_BdgdeviceErr_Type())
bdgdeviceErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceErr.setStatus(_A)
_BdgdeviceSwitchSetting_Type=OctetString
_BdgdeviceSwitchSetting_Object=MibScalar
bdgdeviceSwitchSetting=_BdgdeviceSwitchSetting_Object((1,3,6,1,4,1,52,1,3,1,1,15),_BdgdeviceSwitchSetting_Type())
bdgdeviceSwitchSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceSwitchSetting.setStatus(_A)
_BdgdeviceNumRestarts_Type=Counter32
_BdgdeviceNumRestarts_Object=MibScalar
bdgdeviceNumRestarts=_BdgdeviceNumRestarts_Object((1,3,6,1,4,1,52,1,3,1,1,16),_BdgdeviceNumRestarts_Type())
bdgdeviceNumRestarts.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceNumRestarts.setStatus(_A)
class _BdgdeviceTypeFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),('both',2)))
_BdgdeviceTypeFiltering_Type.__name__=_D
_BdgdeviceTypeFiltering_Object=MibScalar
bdgdeviceTypeFiltering=_BdgdeviceTypeFiltering_Object((1,3,6,1,4,1,52,1,3,1,1,17),_BdgdeviceTypeFiltering_Type())
bdgdeviceTypeFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceTypeFiltering.setStatus(_A)
class _BdgdeviceSTAProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('dec',1),('none',2)))
_BdgdeviceSTAProtocol_Type.__name__=_D
_BdgdeviceSTAProtocol_Object=MibScalar
bdgdeviceSTAProtocol=_BdgdeviceSTAProtocol_Object((1,3,6,1,4,1,52,1,3,1,1,18),_BdgdeviceSTAProtocol_Type())
bdgdeviceSTAProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceSTAProtocol.setStatus(_A)
_BdgdeviceBridgeID_Type=OctetString
_BdgdeviceBridgeID_Object=MibScalar
bdgdeviceBridgeID=_BdgdeviceBridgeID_Object((1,3,6,1,4,1,52,1,3,1,1,19),_BdgdeviceBridgeID_Type())
bdgdeviceBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceBridgeID.setStatus(_A)
_BdgdeviceTopChgCnt_Type=Counter32
_BdgdeviceTopChgCnt_Object=MibScalar
bdgdeviceTopChgCnt=_BdgdeviceTopChgCnt_Object((1,3,6,1,4,1,52,1,3,1,1,20),_BdgdeviceTopChgCnt_Type())
bdgdeviceTopChgCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceTopChgCnt.setStatus(_A)
_BdgdeviceRootCost_Type=Integer32
_BdgdeviceRootCost_Object=MibScalar
bdgdeviceRootCost=_BdgdeviceRootCost_Object((1,3,6,1,4,1,52,1,3,1,1,21),_BdgdeviceRootCost_Type())
bdgdeviceRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceRootCost.setStatus(_A)
_BdgdeviceRootPort_Type=Integer32
_BdgdeviceRootPort_Object=MibScalar
bdgdeviceRootPort=_BdgdeviceRootPort_Object((1,3,6,1,4,1,52,1,3,1,1,22),_BdgdeviceRootPort_Type())
bdgdeviceRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceRootPort.setStatus(_A)
_BdgdeviceHelloTime_Type=Integer32
_BdgdeviceHelloTime_Object=MibScalar
bdgdeviceHelloTime=_BdgdeviceHelloTime_Object((1,3,6,1,4,1,52,1,3,1,1,23),_BdgdeviceHelloTime_Type())
bdgdeviceHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceHelloTime.setStatus(_A)
_BdgdeviceBdgMaxAge_Type=Integer32
_BdgdeviceBdgMaxAge_Object=MibScalar
bdgdeviceBdgMaxAge=_BdgdeviceBdgMaxAge_Object((1,3,6,1,4,1,52,1,3,1,1,24),_BdgdeviceBdgMaxAge_Type())
bdgdeviceBdgMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceBdgMaxAge.setStatus(_A)
_BdgdeviceBdgFwdDly_Type=Integer32
_BdgdeviceBdgFwdDly_Object=MibScalar
bdgdeviceBdgFwdDly=_BdgdeviceBdgFwdDly_Object((1,3,6,1,4,1,52,1,3,1,1,25),_BdgdeviceBdgFwdDly_Type())
bdgdeviceBdgFwdDly.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceBdgFwdDly.setStatus(_A)
_BdgdeviceTimeTopChg_Type=Integer32
_BdgdeviceTimeTopChg_Object=MibScalar
bdgdeviceTimeTopChg=_BdgdeviceTimeTopChg_Object((1,3,6,1,4,1,52,1,3,1,1,26),_BdgdeviceTimeTopChg_Type())
bdgdeviceTimeTopChg.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceTimeTopChg.setStatus(_A)
class _BdgdeviceTopChg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noTopologyChangeInProgress',0),('topologyChangeInProgress',1)))
_BdgdeviceTopChg_Type.__name__=_D
_BdgdeviceTopChg_Object=MibScalar
bdgdeviceTopChg=_BdgdeviceTopChg_Object((1,3,6,1,4,1,52,1,3,1,1,27),_BdgdeviceTopChg_Type())
bdgdeviceTopChg.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceTopChg.setStatus(_A)
_BdgdeviceDesigRoot_Type=OctetString
_BdgdeviceDesigRoot_Object=MibScalar
bdgdeviceDesigRoot=_BdgdeviceDesigRoot_Object((1,3,6,1,4,1,52,1,3,1,1,28),_BdgdeviceDesigRoot_Type())
bdgdeviceDesigRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceDesigRoot.setStatus(_A)
_BdgdeviceMaxAge_Type=Integer32
_BdgdeviceMaxAge_Object=MibScalar
bdgdeviceMaxAge=_BdgdeviceMaxAge_Object((1,3,6,1,4,1,52,1,3,1,1,29),_BdgdeviceMaxAge_Type())
bdgdeviceMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceMaxAge.setStatus(_A)
_BdgdeviceHoldTime_Type=Integer32
_BdgdeviceHoldTime_Object=MibScalar
bdgdeviceHoldTime=_BdgdeviceHoldTime_Object((1,3,6,1,4,1,52,1,3,1,1,30),_BdgdeviceHoldTime_Type())
bdgdeviceHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceHoldTime.setStatus(_A)
_BdgdeviceFwdDly_Type=Integer32
_BdgdeviceFwdDly_Object=MibScalar
bdgdeviceFwdDly=_BdgdeviceFwdDly_Object((1,3,6,1,4,1,52,1,3,1,1,31),_BdgdeviceFwdDly_Type())
bdgdeviceFwdDly.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceFwdDly.setStatus(_A)
_BdgdeviceBdgHello_Type=Integer32
_BdgdeviceBdgHello_Object=MibScalar
bdgdeviceBdgHello=_BdgdeviceBdgHello_Object((1,3,6,1,4,1,52,1,3,1,1,32),_BdgdeviceBdgHello_Type())
bdgdeviceBdgHello.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceBdgHello.setStatus(_A)
_BdgdeviceBdgPriority_Type=Integer32
_BdgdeviceBdgPriority_Object=MibScalar
bdgdeviceBdgPriority=_BdgdeviceBdgPriority_Object((1,3,6,1,4,1,52,1,3,1,1,33),_BdgdeviceBdgPriority_Type())
bdgdeviceBdgPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceBdgPriority.setStatus(_A)
class _BdgdeviceResetCounts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('resetCounts',0))
_BdgdeviceResetCounts_Type.__name__=_D
_BdgdeviceResetCounts_Object=MibScalar
bdgdeviceResetCounts=_BdgdeviceResetCounts_Object((1,3,6,1,4,1,52,1,3,1,1,34),_BdgdeviceResetCounts_Type())
bdgdeviceResetCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgdeviceResetCounts.setStatus(_A)
_BdgdeviceUptime_Type=Integer32
_BdgdeviceUptime_Object=MibScalar
bdgdeviceUptime=_BdgdeviceUptime_Object((1,3,6,1,4,1,52,1,3,1,1,35),_BdgdeviceUptime_Type())
bdgdeviceUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceUptime.setStatus(_A)
_BdgdeviceTrapType_Type=ObjectIdentifier
_BdgdeviceTrapType_Object=MibScalar
bdgdeviceTrapType=_BdgdeviceTrapType_Object((1,3,6,1,4,1,52,1,3,1,1,36),_BdgdeviceTrapType_Type())
bdgdeviceTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgdeviceTrapType.setStatus(_A)
_BdgPort_ObjectIdentity=ObjectIdentity
bdgPort=_BdgPort_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,2))
_BdgPortAddress_Type=OctetString
_BdgPortAddress_Object=MibScalar
bdgPortAddress=_BdgPortAddress_Object((1,3,6,1,4,1,52,1,3,1,2,1),_BdgPortAddress_Type())
bdgPortAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortAddress.setStatus(_A)
_BdgPortName_Type=OctetString
_BdgPortName_Object=MibScalar
bdgPortName=_BdgPortName_Object((1,3,6,1,4,1,52,1,3,1,2,2),_BdgPortName_Type())
bdgPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgPortName.setStatus(_A)
_BdgPortType_Type=OctetString
_BdgPortType_Object=MibScalar
bdgPortType=_BdgPortType_Object((1,3,6,1,4,1,52,1,3,1,2,3),_BdgPortType_Type())
bdgPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortType.setStatus(_A)
_BdgPortStatus_Type=OctetString
_BdgPortStatus_Object=MibScalar
bdgPortStatus=_BdgPortStatus_Object((1,3,6,1,4,1,52,1,3,1,2,4),_BdgPortStatus_Type())
bdgPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortStatus.setStatus(_A)
_BdgPortNetName_Type=OctetString
_BdgPortNetName_Object=MibScalar
bdgPortNetName=_BdgPortNetName_Object((1,3,6,1,4,1,52,1,3,1,2,5),_BdgPortNetName_Type())
bdgPortNetName.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgPortNetName.setStatus(_A)
_BdgPortFrRx_Type=Counter32
_BdgPortFrRx_Object=MibScalar
bdgPortFrRx=_BdgPortFrRx_Object((1,3,6,1,4,1,52,1,3,1,2,6),_BdgPortFrRx_Type())
bdgPortFrRx.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortFrRx.setStatus(_A)
_BdgPortDisInb_Type=Counter32
_BdgPortDisInb_Object=MibScalar
bdgPortDisInb=_BdgPortDisInb_Object((1,3,6,1,4,1,52,1,3,1,2,7),_BdgPortDisInb_Type())
bdgPortDisInb.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDisInb.setStatus(_A)
_BdgPortFwdOutb_Type=Counter32
_BdgPortFwdOutb_Object=MibScalar
bdgPortFwdOutb=_BdgPortFwdOutb_Object((1,3,6,1,4,1,52,1,3,1,2,8),_BdgPortFwdOutb_Type())
bdgPortFwdOutb.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortFwdOutb.setStatus(_A)
_BdgPortDisLOB_Type=Counter32
_BdgPortDisLOB_Object=MibScalar
bdgPortDisLOB=_BdgPortDisLOB_Object((1,3,6,1,4,1,52,1,3,1,2,9),_BdgPortDisLOB_Type())
bdgPortDisLOB.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDisLOB.setStatus(_A)
_BdgPortDisTDE_Type=Counter32
_BdgPortDisTDE_Object=MibScalar
bdgPortDisTDE=_BdgPortDisTDE_Object((1,3,6,1,4,1,52,1,3,1,2,10),_BdgPortDisTDE_Type())
bdgPortDisTDE.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDisTDE.setStatus(_A)
_BdgPortDisErr_Type=Counter32
_BdgPortDisErr_Object=MibScalar
bdgPortDisErr=_BdgPortDisErr_Object((1,3,6,1,4,1,52,1,3,1,2,11),_BdgPortDisErr_Type())
bdgPortDisErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDisErr.setStatus(_A)
_BdgPortColl_Type=Counter32
_BdgPortColl_Object=MibScalar
bdgPortColl=_BdgPortColl_Object((1,3,6,1,4,1,52,1,3,1,2,12),_BdgPortColl_Type())
bdgPortColl.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortColl.setStatus(_A)
_BdgPortTxAbrt_Type=Counter32
_BdgPortTxAbrt_Object=MibScalar
bdgPortTxAbrt=_BdgPortTxAbrt_Object((1,3,6,1,4,1,52,1,3,1,2,13),_BdgPortTxAbrt_Type())
bdgPortTxAbrt.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortTxAbrt.setStatus(_A)
_BdgPortOowColl_Type=Counter32
_BdgPortOowColl_Object=MibScalar
bdgPortOowColl=_BdgPortOowColl_Object((1,3,6,1,4,1,52,1,3,1,2,14),_BdgPortOowColl_Type())
bdgPortOowColl.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortOowColl.setStatus(_A)
_BdgPortCRCErr_Type=Counter32
_BdgPortCRCErr_Object=MibScalar
bdgPortCRCErr=_BdgPortCRCErr_Object((1,3,6,1,4,1,52,1,3,1,2,15),_BdgPortCRCErr_Type())
bdgPortCRCErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortCRCErr.setStatus(_A)
_BdgPortFrAlErr_Type=Counter32
_BdgPortFrAlErr_Object=MibScalar
bdgPortFrAlErr=_BdgPortFrAlErr_Object((1,3,6,1,4,1,52,1,3,1,2,16),_BdgPortFrAlErr_Type())
bdgPortFrAlErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortFrAlErr.setStatus(_A)
_BdgPortPriority_Type=Integer32
_BdgPortPriority_Object=MibScalar
bdgPortPriority=_BdgPortPriority_Object((1,3,6,1,4,1,52,1,3,1,2,17),_BdgPortPriority_Type())
bdgPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgPortPriority.setStatus(_A)
_BdgPortState_Type=OctetString
_BdgPortState_Object=MibScalar
bdgPortState=_BdgPortState_Object((1,3,6,1,4,1,52,1,3,1,2,18),_BdgPortState_Type())
bdgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortState.setStatus(_A)
_BdgPortPathCost_Type=Integer32
_BdgPortPathCost_Object=MibScalar
bdgPortPathCost=_BdgPortPathCost_Object((1,3,6,1,4,1,52,1,3,1,2,19),_BdgPortPathCost_Type())
bdgPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:bdgPortPathCost.setStatus(_A)
_BdgPortDesigCost_Type=Integer32
_BdgPortDesigCost_Object=MibScalar
bdgPortDesigCost=_BdgPortDesigCost_Object((1,3,6,1,4,1,52,1,3,1,2,20),_BdgPortDesigCost_Type())
bdgPortDesigCost.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDesigCost.setStatus(_A)
_BdgPortDesigBrdg_Type=OctetString
_BdgPortDesigBrdg_Object=MibScalar
bdgPortDesigBrdg=_BdgPortDesigBrdg_Object((1,3,6,1,4,1,52,1,3,1,2,21),_BdgPortDesigBrdg_Type())
bdgPortDesigBrdg.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDesigBrdg.setStatus(_A)
_BdgPortDesigPort_Type=Integer32
_BdgPortDesigPort_Object=MibScalar
bdgPortDesigPort=_BdgPortDesigPort_Object((1,3,6,1,4,1,52,1,3,1,2,22),_BdgPortDesigPort_Type())
bdgPortDesigPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDesigPort.setStatus(_A)
class _BdgPortTopChgAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noTopologyChangeIsOccurring',0),('topologyChangeIsOccurring',1)))
_BdgPortTopChgAck_Type.__name__=_D
_BdgPortTopChgAck_Object=MibScalar
bdgPortTopChgAck=_BdgPortTopChgAck_Object((1,3,6,1,4,1,52,1,3,1,2,23),_BdgPortTopChgAck_Type())
bdgPortTopChgAck.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortTopChgAck.setStatus(_A)
_BdgPortDesigRoot_Type=OctetString
_BdgPortDesigRoot_Object=MibScalar
bdgPortDesigRoot=_BdgPortDesigRoot_Object((1,3,6,1,4,1,52,1,3,1,2,24),_BdgPortDesigRoot_Type())
bdgPortDesigRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortDesigRoot.setStatus(_A)
_BdgPortRuntPackets_Type=Counter32
_BdgPortRuntPackets_Object=MibScalar
bdgPortRuntPackets=_BdgPortRuntPackets_Object((1,3,6,1,4,1,52,1,3,1,2,25),_BdgPortRuntPackets_Type())
bdgPortRuntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortRuntPackets.setStatus(_A)
_BdgPortOversizePackets_Type=Counter32
_BdgPortOversizePackets_Object=MibScalar
bdgPortOversizePackets=_BdgPortOversizePackets_Object((1,3,6,1,4,1,52,1,3,1,2,26),_BdgPortOversizePackets_Type())
bdgPortOversizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortOversizePackets.setStatus(_A)
_BdgPortFrFilt_Type=Counter32
_BdgPortFrFilt_Object=MibScalar
bdgPortFrFilt=_BdgPortFrFilt_Object((1,3,6,1,4,1,52,1,3,1,2,27),_BdgPortFrFilt_Type())
bdgPortFrFilt.setMaxAccess(_B)
if mibBuilder.loadTexts:bdgPortFrFilt.setStatus(_A)
_FilterDB_ObjectIdentity=ObjectIdentity
filterDB=_FilterDB_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3))
_AcqDB_ObjectIdentity=ObjectIdentity
acqDB=_AcqDB_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,1))
_AcqStats_ObjectIdentity=ObjectIdentity
acqStats=_AcqStats_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,1,1))
_AcqTotalEntries_Type=Integer32
_AcqTotalEntries_Object=MibScalar
acqTotalEntries=_AcqTotalEntries_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,1),_AcqTotalEntries_Type())
acqTotalEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:acqTotalEntries.setStatus(_A)
_AcqMaxEntries_Type=Integer32
_AcqMaxEntries_Object=MibScalar
acqMaxEntries=_AcqMaxEntries_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,2),_AcqMaxEntries_Type())
acqMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:acqMaxEntries.setStatus(_A)
_AcqStaticEntries_Type=Integer32
_AcqStaticEntries_Object=MibScalar
acqStaticEntries=_AcqStaticEntries_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,3),_AcqStaticEntries_Type())
acqStaticEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:acqStaticEntries.setStatus(_A)
_AcqStaticAgeTime_Type=Integer32
_AcqStaticAgeTime_Object=MibScalar
acqStaticAgeTime=_AcqStaticAgeTime_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,4),_AcqStaticAgeTime_Type())
acqStaticAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:acqStaticAgeTime.setStatus(_A)
_AcqDynEntries_Type=Integer32
_AcqDynEntries_Object=MibScalar
acqDynEntries=_AcqDynEntries_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,5),_AcqDynEntries_Type())
acqDynEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:acqDynEntries.setStatus(_A)
_AcqDynAgeTime_Type=Integer32
_AcqDynAgeTime_Object=MibScalar
acqDynAgeTime=_AcqDynAgeTime_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,6),_AcqDynAgeTime_Type())
acqDynAgeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:acqDynAgeTime.setStatus(_A)
class _AcqEraseDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('eraseAcquiredDatabase',0))
_AcqEraseDatabase_Type.__name__=_D
_AcqEraseDatabase_Object=MibScalar
acqEraseDatabase=_AcqEraseDatabase_Object((1,3,6,1,4,1,52,1,3,1,3,1,1,7),_AcqEraseDatabase_Type())
acqEraseDatabase.setMaxAccess(_C)
if mibBuilder.loadTexts:acqEraseDatabase.setStatus(_A)
_AcqOptions_ObjectIdentity=ObjectIdentity
acqOptions=_AcqOptions_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,1,2))
class _AcqCreate00_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createAcquiredEntryFilterPort1FilterPort2',0))
_AcqCreate00_Type.__name__=_D
_AcqCreate00_Object=MibScalar
acqCreate00=_AcqCreate00_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,1),_AcqCreate00_Type())
acqCreate00.setMaxAccess(_C)
if mibBuilder.loadTexts:acqCreate00.setStatus(_A)
class _AcqCreate20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createAcquiredEntryForwardPort1FilterPort2',0))
_AcqCreate20_Type.__name__=_D
_AcqCreate20_Object=MibScalar
acqCreate20=_AcqCreate20_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,2),_AcqCreate20_Type())
acqCreate20.setMaxAccess(_C)
if mibBuilder.loadTexts:acqCreate20.setStatus(_A)
class _AcqCreate01_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createAcquiredEntryFilterPort1ForwardPort2',0))
_AcqCreate01_Type.__name__=_D
_AcqCreate01_Object=MibScalar
acqCreate01=_AcqCreate01_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,3),_AcqCreate01_Type())
acqCreate01.setMaxAccess(_C)
if mibBuilder.loadTexts:acqCreate01.setStatus(_A)
class _AcqCreate21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createAcquiredEntryForwardPort1ForwardPort2',0))
_AcqCreate21_Type.__name__=_D
_AcqCreate21_Object=MibScalar
acqCreate21=_AcqCreate21_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,4),_AcqCreate21_Type())
acqCreate21.setMaxAccess(_C)
if mibBuilder.loadTexts:acqCreate21.setStatus(_A)
class _AcqDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('deleteAcquiredEntry',0))
_AcqDelete_Type.__name__=_D
_AcqDelete_Object=MibScalar
acqDelete=_AcqDelete_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,5),_AcqDelete_Type())
acqDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:acqDelete.setStatus(_A)
_AcqDispType_Type=OctetString
_AcqDispType_Object=MibScalar
acqDispType=_AcqDispType_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,6),_AcqDispType_Type())
acqDispType.setMaxAccess(_B)
if mibBuilder.loadTexts:acqDispType.setStatus(_A)
class _AcqDispOutp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_E,0),(_F,2)))
_AcqDispOutp1_Type.__name__=_D
_AcqDispOutp1_Object=MibScalar
acqDispOutp1=_AcqDispOutp1_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,7),_AcqDispOutp1_Type())
acqDispOutp1.setMaxAccess(_B)
if mibBuilder.loadTexts:acqDispOutp1.setStatus(_A)
class _AcqDispOutp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_AcqDispOutp2_Type.__name__=_D
_AcqDispOutp2_Object=MibScalar
acqDispOutp2=_AcqDispOutp2_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,8),_AcqDispOutp2_Type())
acqDispOutp2.setMaxAccess(_B)
if mibBuilder.loadTexts:acqDispOutp2.setStatus(_A)
_AcqSrcAddress_Type=OctetString
_AcqSrcAddress_Object=MibScalar
acqSrcAddress=_AcqSrcAddress_Object((1,3,6,1,4,1,52,1,3,1,3,1,2,9),_AcqSrcAddress_Type())
acqSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:acqSrcAddress.setStatus(_A)
_PermDB_ObjectIdentity=ObjectIdentity
permDB=_PermDB_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,2))
_PermStats_ObjectIdentity=ObjectIdentity
permStats=_PermStats_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,2,1))
_PermMaxEntries_Type=Integer32
_PermMaxEntries_Object=MibScalar
permMaxEntries=_PermMaxEntries_Object((1,3,6,1,4,1,52,1,3,1,3,2,1,1),_PermMaxEntries_Type())
permMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:permMaxEntries.setStatus(_A)
_PermCurrEntries_Type=Integer32
_PermCurrEntries_Object=MibScalar
permCurrEntries=_PermCurrEntries_Object((1,3,6,1,4,1,52,1,3,1,3,2,1,2),_PermCurrEntries_Type())
permCurrEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:permCurrEntries.setStatus(_A)
class _PermEraseDatabase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('erasePermanentDatabase',0))
_PermEraseDatabase_Type.__name__=_D
_PermEraseDatabase_Object=MibScalar
permEraseDatabase=_PermEraseDatabase_Object((1,3,6,1,4,1,52,1,3,1,3,2,1,3),_PermEraseDatabase_Type())
permEraseDatabase.setMaxAccess(_C)
if mibBuilder.loadTexts:permEraseDatabase.setStatus(_A)
_PermOptions_ObjectIdentity=ObjectIdentity
permOptions=_PermOptions_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,2,2))
class _PermCreate00_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createPermanentEntryFilterPort1FilterPort2',0))
_PermCreate00_Type.__name__=_D
_PermCreate00_Object=MibScalar
permCreate00=_PermCreate00_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,1),_PermCreate00_Type())
permCreate00.setMaxAccess(_C)
if mibBuilder.loadTexts:permCreate00.setStatus(_A)
class _PermCreate20_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createPermanentEntryForwardPort1FilterPort2',0))
_PermCreate20_Type.__name__=_D
_PermCreate20_Object=MibScalar
permCreate20=_PermCreate20_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,2),_PermCreate20_Type())
permCreate20.setMaxAccess(_C)
if mibBuilder.loadTexts:permCreate20.setStatus(_A)
class _PermCreate01_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createPermanentEntryFilterPort1ForwardPort2',0))
_PermCreate01_Type.__name__=_D
_PermCreate01_Object=MibScalar
permCreate01=_PermCreate01_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,3),_PermCreate01_Type())
permCreate01.setMaxAccess(_C)
if mibBuilder.loadTexts:permCreate01.setStatus(_A)
class _PermCreate21_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('createPermanentEntryForwardPort1ForwardPort2',0))
_PermCreate21_Type.__name__=_D
_PermCreate21_Object=MibScalar
permCreate21=_PermCreate21_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,4),_PermCreate21_Type())
permCreate21.setMaxAccess(_C)
if mibBuilder.loadTexts:permCreate21.setStatus(_A)
class _PermDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('deletePermanentEntry',0))
_PermDelete_Type.__name__=_D
_PermDelete_Object=MibScalar
permDelete=_PermDelete_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,5),_PermDelete_Type())
permDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:permDelete.setStatus(_A)
_PermDispType_Type=OctetString
_PermDispType_Object=MibScalar
permDispType=_PermDispType_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,6),_PermDispType_Type())
permDispType.setMaxAccess(_B)
if mibBuilder.loadTexts:permDispType.setStatus(_A)
class _PermDispOutp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_E,0),(_F,2)))
_PermDispOutp1_Type.__name__=_D
_PermDispOutp1_Object=MibScalar
permDispOutp1=_PermDispOutp1_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,7),_PermDispOutp1_Type())
permDispOutp1.setMaxAccess(_B)
if mibBuilder.loadTexts:permDispOutp1.setStatus(_A)
class _PermDispOutp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_PermDispOutp2_Type.__name__=_D
_PermDispOutp2_Object=MibScalar
permDispOutp2=_PermDispOutp2_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,8),_PermDispOutp2_Type())
permDispOutp2.setMaxAccess(_B)
if mibBuilder.loadTexts:permDispOutp2.setStatus(_A)
_PermSrcAddress_Type=OctetString
_PermSrcAddress_Object=MibScalar
permSrcAddress=_PermSrcAddress_Object((1,3,6,1,4,1,52,1,3,1,3,2,2,9),_PermSrcAddress_Type())
permSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:permSrcAddress.setStatus(_A)
_SpecialDB_ObjectIdentity=ObjectIdentity
specialDB=_SpecialDB_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,3))
_SpecStats_ObjectIdentity=ObjectIdentity
specStats=_SpecStats_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,3,1))
_SpecNumEntries_Type=Integer32
_SpecNumEntries_Object=MibScalar
specNumEntries=_SpecNumEntries_Object((1,3,6,1,4,1,52,1,3,1,3,3,1,1),_SpecNumEntries_Type())
specNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:specNumEntries.setStatus(_A)
_SpecMaxEntries_Type=Integer32
_SpecMaxEntries_Object=MibScalar
specMaxEntries=_SpecMaxEntries_Object((1,3,6,1,4,1,52,1,3,1,3,3,1,2),_SpecMaxEntries_Type())
specMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:specMaxEntries.setStatus(_A)
_SpecNextFilterNum_Type=Integer32
_SpecNextFilterNum_Object=MibScalar
specNextFilterNum=_SpecNextFilterNum_Object((1,3,6,1,4,1,52,1,3,1,3,3,1,3),_SpecNextFilterNum_Type())
specNextFilterNum.setMaxAccess(_B)
if mibBuilder.loadTexts:specNextFilterNum.setStatus(_A)
_SpecFilters_ObjectIdentity=ObjectIdentity
specFilters=_SpecFilters_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,3,3,2))
class _SpecEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disableFilter',0),('enableFilter',1)))
_SpecEnable_Type.__name__=_D
_SpecEnable_Object=MibScalar
specEnable=_SpecEnable_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,1),_SpecEnable_Type())
specEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:specEnable.setStatus(_A)
class _SpecPort1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_E,0),(_F,2)))
_SpecPort1_Type.__name__=_D
_SpecPort1_Object=MibScalar
specPort1=_SpecPort1_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,2),_SpecPort1_Type())
specPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:specPort1.setStatus(_A)
class _SpecPort2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SpecPort2_Type.__name__=_D
_SpecPort2_Object=MibScalar
specPort2=_SpecPort2_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,3),_SpecPort2_Type())
specPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:specPort2.setStatus(_A)
_SpecDestAddress_Type=OctetString
_SpecDestAddress_Object=MibScalar
specDestAddress=_SpecDestAddress_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,4),_SpecDestAddress_Type())
specDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:specDestAddress.setStatus(_A)
_SpecSrcAddress_Type=OctetString
_SpecSrcAddress_Object=MibScalar
specSrcAddress=_SpecSrcAddress_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,5),_SpecSrcAddress_Type())
specSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:specSrcAddress.setStatus(_A)
_SpecType_Type=OctetString
_SpecType_Object=MibScalar
specType=_SpecType_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,6),_SpecType_Type())
specType.setMaxAccess(_C)
if mibBuilder.loadTexts:specType.setStatus(_A)
_SpecDataField_Type=OctetString
_SpecDataField_Object=MibScalar
specDataField=_SpecDataField_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,7),_SpecDataField_Type())
specDataField.setMaxAccess(_C)
if mibBuilder.loadTexts:specDataField.setStatus(_A)
class _SpecDeleteFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('deleteFilter',0))
_SpecDeleteFilter_Type.__name__=_D
_SpecDeleteFilter_Object=MibScalar
specDeleteFilter=_SpecDeleteFilter_Object((1,3,6,1,4,1,52,1,3,1,3,3,2,8),_SpecDeleteFilter_Type())
specDeleteFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:specDeleteFilter.setStatus(_A)
_TrapTypes_ObjectIdentity=ObjectIdentity
trapTypes=_TrapTypes_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,4))
_BdgTables_ObjectIdentity=ObjectIdentity
bdgTables=_BdgTables_ObjectIdentity((1,3,6,1,4,1,52,1,3,1,5))
_Lmcommon_ObjectIdentity=ObjectIdentity
lmcommon=_Lmcommon_ObjectIdentity((1,3,6,1,4,1,52,2,1))
_MAC_ObjectIdentity=ObjectIdentity
mAC=_MAC_ObjectIdentity((1,3,6,1,4,1,52,2,2))
_Ieee8023_ObjectIdentity=ObjectIdentity
ieee8023=_Ieee8023_ObjectIdentity((1,3,6,1,4,1,52,2,2,1))
_PcIF_ObjectIdentity=ObjectIdentity
pcIF=_PcIF_ObjectIdentity((1,3,6,1,4,1,52,2,2,1,1))
_PcIfRev_ObjectIdentity=ObjectIdentity
pcIfRev=_PcIfRev_ObjectIdentity((1,3,6,1,4,1,52,2,2,1,1,1))
_PcDeviceName_Type=OctetString
_PcDeviceName_Object=MibScalar
pcDeviceName=_PcDeviceName_Object((1,3,6,1,4,1,52,2,2,1,1,1,1),_PcDeviceName_Type())
pcDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:pcDeviceName.setStatus(_A)
_PcBoardType_Type=ObjectIdentifier
_PcBoardType_Object=MibScalar
pcBoardType=_PcBoardType_Object((1,3,6,1,4,1,52,2,2,1,1,1,2),_PcBoardType_Type())
pcBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:pcBoardType.setStatus(_A)
_PcOwnerName_Type=OctetString
_PcOwnerName_Object=MibScalar
pcOwnerName=_PcOwnerName_Object((1,3,6,1,4,1,52,2,2,1,1,1,3),_PcOwnerName_Type())
pcOwnerName.setMaxAccess(_B)
if mibBuilder.loadTexts:pcOwnerName.setStatus(_A)
_PcLocation_Type=OctetString
_PcLocation_Object=MibScalar
pcLocation=_PcLocation_Object((1,3,6,1,4,1,52,2,2,1,1,1,4),_PcLocation_Type())
pcLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:pcLocation.setStatus(_A)
_PcMMACAddr_Type=OctetString
_PcMMACAddr_Object=MibScalar
pcMMACAddr=_PcMMACAddr_Object((1,3,6,1,4,1,52,2,2,1,1,1,5),_PcMMACAddr_Type())
pcMMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMMACAddr.setStatus(_A)
_PcMMACBoard_Type=OctetString
_PcMMACBoard_Object=MibScalar
pcMMACBoard=_PcMMACBoard_Object((1,3,6,1,4,1,52,2,2,1,1,1,6),_PcMMACBoard_Type())
pcMMACBoard.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMMACBoard.setStatus(_A)
_PcMMACPort_Type=OctetString
_PcMMACPort_Object=MibScalar
pcMMACPort=_PcMMACPort_Object((1,3,6,1,4,1,52,2,2,1,1,1,7),_PcMMACPort_Type())
pcMMACPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMMACPort.setStatus(_A)
_PcApplication_Type=OctetString
_PcApplication_Object=MibScalar
pcApplication=_PcApplication_Object((1,3,6,1,4,1,52,2,2,1,1,1,8),_PcApplication_Type())
pcApplication.setMaxAccess(_B)
if mibBuilder.loadTexts:pcApplication.setStatus(_A)
_PcDriverRev_Type=OctetString
_PcDriverRev_Object=MibScalar
pcDriverRev=_PcDriverRev_Object((1,3,6,1,4,1,52,2,2,1,1,1,9),_PcDriverRev_Type())
pcDriverRev.setMaxAccess(_B)
if mibBuilder.loadTexts:pcDriverRev.setStatus(_A)
_PcOnboardMemory_Type=Integer32
_PcOnboardMemory_Object=MibScalar
pcOnboardMemory=_PcOnboardMemory_Object((1,3,6,1,4,1,52,2,2,1,1,1,10),_PcOnboardMemory_Type())
pcOnboardMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:pcOnboardMemory.setStatus(_A)
_PcComment_Type=OctetString
_PcComment_Object=MibScalar
pcComment=_PcComment_Object((1,3,6,1,4,1,52,2,2,1,1,1,11),_PcComment_Type())
pcComment.setMaxAccess(_B)
if mibBuilder.loadTexts:pcComment.setStatus(_A)
_PcMACAddr_Type=OctetString
_PcMACAddr_Object=MibScalar
pcMACAddr=_PcMACAddr_Object((1,3,6,1,4,1,52,2,2,1,1,1,12),_PcMACAddr_Type())
pcMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMACAddr.setStatus(_A)
_PcFramesXmit_Type=Integer32
_PcFramesXmit_Object=MibScalar
pcFramesXmit=_PcFramesXmit_Object((1,3,6,1,4,1,52,2,2,1,1,1,13),_PcFramesXmit_Type())
pcFramesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:pcFramesXmit.setStatus(_A)
_PcBytesXmit_Type=Integer32
_PcBytesXmit_Object=MibScalar
pcBytesXmit=_PcBytesXmit_Object((1,3,6,1,4,1,52,2,2,1,1,1,14),_PcBytesXmit_Type())
pcBytesXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:pcBytesXmit.setStatus(_A)
_PcMcastXmit_Type=Integer32
_PcMcastXmit_Object=MibScalar
pcMcastXmit=_PcMcastXmit_Object((1,3,6,1,4,1,52,2,2,1,1,1,15),_PcMcastXmit_Type())
pcMcastXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMcastXmit.setStatus(_A)
_PcBcastXmit_Type=Integer32
_PcBcastXmit_Object=MibScalar
pcBcastXmit=_PcBcastXmit_Object((1,3,6,1,4,1,52,2,2,1,1,1,16),_PcBcastXmit_Type())
pcBcastXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:pcBcastXmit.setStatus(_A)
_PcDeferXmit_Type=Integer32
_PcDeferXmit_Object=MibScalar
pcDeferXmit=_PcDeferXmit_Object((1,3,6,1,4,1,52,2,2,1,1,1,17),_PcDeferXmit_Type())
pcDeferXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:pcDeferXmit.setStatus(_A)
_PcSglColl_Type=Integer32
_PcSglColl_Object=MibScalar
pcSglColl=_PcSglColl_Object((1,3,6,1,4,1,52,2,2,1,1,1,18),_PcSglColl_Type())
pcSglColl.setMaxAccess(_B)
if mibBuilder.loadTexts:pcSglColl.setStatus(_A)
_PcMultiColl_Type=Integer32
_PcMultiColl_Object=MibScalar
pcMultiColl=_PcMultiColl_Object((1,3,6,1,4,1,52,2,2,1,1,1,19),_PcMultiColl_Type())
pcMultiColl.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMultiColl.setStatus(_A)
_PcTotXmitErrs_Type=Integer32
_PcTotXmitErrs_Object=MibScalar
pcTotXmitErrs=_PcTotXmitErrs_Object((1,3,6,1,4,1,52,2,2,1,1,1,20),_PcTotXmitErrs_Type())
pcTotXmitErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcTotXmitErrs.setStatus(_A)
_PcLateColls_Type=Integer32
_PcLateColls_Object=MibScalar
pcLateColls=_PcLateColls_Object((1,3,6,1,4,1,52,2,2,1,1,1,21),_PcLateColls_Type())
pcLateColls.setMaxAccess(_B)
if mibBuilder.loadTexts:pcLateColls.setStatus(_A)
_PcXcessColls_Type=Integer32
_PcXcessColls_Object=MibScalar
pcXcessColls=_PcXcessColls_Object((1,3,6,1,4,1,52,2,2,1,1,1,22),_PcXcessColls_Type())
pcXcessColls.setMaxAccess(_B)
if mibBuilder.loadTexts:pcXcessColls.setStatus(_A)
_PcCarrErr_Type=Integer32
_PcCarrErr_Object=MibScalar
pcCarrErr=_PcCarrErr_Object((1,3,6,1,4,1,52,2,2,1,1,1,23),_PcCarrErr_Type())
pcCarrErr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcCarrErr.setStatus(_A)
_PcFramesRec_Type=Integer32
_PcFramesRec_Object=MibScalar
pcFramesRec=_PcFramesRec_Object((1,3,6,1,4,1,52,2,2,1,1,1,24),_PcFramesRec_Type())
pcFramesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcFramesRec.setStatus(_A)
_PcBytesRec_Type=Integer32
_PcBytesRec_Object=MibScalar
pcBytesRec=_PcBytesRec_Object((1,3,6,1,4,1,52,2,2,1,1,1,25),_PcBytesRec_Type())
pcBytesRec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcBytesRec.setStatus(_A)
_PcMcastRec_Type=Integer32
_PcMcastRec_Object=MibScalar
pcMcastRec=_PcMcastRec_Object((1,3,6,1,4,1,52,2,2,1,1,1,26),_PcMcastRec_Type())
pcMcastRec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcMcastRec.setStatus(_A)
_PcBcastRec_Type=Integer32
_PcBcastRec_Object=MibScalar
pcBcastRec=_PcBcastRec_Object((1,3,6,1,4,1,52,2,2,1,1,1,27),_PcBcastRec_Type())
pcBcastRec.setMaxAccess(_B)
if mibBuilder.loadTexts:pcBcastRec.setStatus(_A)
_PcTotRecErrs_Type=Integer32
_PcTotRecErrs_Object=MibScalar
pcTotRecErrs=_PcTotRecErrs_Object((1,3,6,1,4,1,52,2,2,1,1,1,28),_PcTotRecErrs_Type())
pcTotRecErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcTotRecErrs.setStatus(_A)
_PcTooLong_Type=Integer32
_PcTooLong_Object=MibScalar
pcTooLong=_PcTooLong_Object((1,3,6,1,4,1,52,2,2,1,1,1,29),_PcTooLong_Type())
pcTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:pcTooLong.setStatus(_A)
_PcTooShort_Type=Integer32
_PcTooShort_Object=MibScalar
pcTooShort=_PcTooShort_Object((1,3,6,1,4,1,52,2,2,1,1,1,30),_PcTooShort_Type())
pcTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:pcTooShort.setStatus(_A)
_PcAlignErrs_Type=Integer32
_PcAlignErrs_Object=MibScalar
pcAlignErrs=_PcAlignErrs_Object((1,3,6,1,4,1,52,2,2,1,1,1,31),_PcAlignErrs_Type())
pcAlignErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcAlignErrs.setStatus(_A)
_PcCRCErrs_Type=Integer32
_PcCRCErrs_Object=MibScalar
pcCRCErrs=_PcCRCErrs_Object((1,3,6,1,4,1,52,2,2,1,1,1,32),_PcCRCErrs_Type())
pcCRCErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcCRCErrs.setStatus(_A)
_PcLenErrs_Type=Integer32
_PcLenErrs_Object=MibScalar
pcLenErrs=_PcLenErrs_Object((1,3,6,1,4,1,52,2,2,1,1,1,33),_PcLenErrs_Type())
pcLenErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:pcLenErrs.setStatus(_A)
_PcIntRecErr_Type=Integer32
_PcIntRecErr_Object=MibScalar
pcIntRecErr=_PcIntRecErr_Object((1,3,6,1,4,1,52,2,2,1,1,1,34),_PcIntRecErr_Type())
pcIntRecErr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcIntRecErr.setStatus(_A)
_PcSqeErr_Type=Integer32
_PcSqeErr_Object=MibScalar
pcSqeErr=_PcSqeErr_Object((1,3,6,1,4,1,52,2,2,1,1,1,35),_PcSqeErr_Type())
pcSqeErr.setMaxAccess(_B)
if mibBuilder.loadTexts:pcSqeErr.setStatus(_A)
mibBuilder.exportSymbols('CTRON-BDG-MIB',**{'bridgeRev1':bridgeRev1,'bdgdevice':bdgdevice,'bdgdeviceDisableBdg':bdgdeviceDisableBdg,'bdgdeviceRestoreSettings':bdgdeviceRestoreSettings,'bdgdeviceBdgName':bdgdeviceBdgName,'bdgdeviceNumPorts':bdgdeviceNumPorts,'bdgdeviceType':bdgdeviceType,'bdgdeviceVersion':bdgdeviceVersion,'bdgdeviceLocation':bdgdeviceLocation,'bdgdeviceStatus':bdgdeviceStatus,'bdgdeviceRestartBdg':bdgdeviceRestartBdg,'bdgdeviceFrFwd':bdgdeviceFrFwd,'bdgdeviceFrRx':bdgdeviceFrRx,'bdgdeviceFrFlt':bdgdeviceFrFlt,'bdgdeviceErr':bdgdeviceErr,'bdgdeviceSwitchSetting':bdgdeviceSwitchSetting,'bdgdeviceNumRestarts':bdgdeviceNumRestarts,'bdgdeviceTypeFiltering':bdgdeviceTypeFiltering,'bdgdeviceSTAProtocol':bdgdeviceSTAProtocol,'bdgdeviceBridgeID':bdgdeviceBridgeID,'bdgdeviceTopChgCnt':bdgdeviceTopChgCnt,'bdgdeviceRootCost':bdgdeviceRootCost,'bdgdeviceRootPort':bdgdeviceRootPort,'bdgdeviceHelloTime':bdgdeviceHelloTime,'bdgdeviceBdgMaxAge':bdgdeviceBdgMaxAge,'bdgdeviceBdgFwdDly':bdgdeviceBdgFwdDly,'bdgdeviceTimeTopChg':bdgdeviceTimeTopChg,'bdgdeviceTopChg':bdgdeviceTopChg,'bdgdeviceDesigRoot':bdgdeviceDesigRoot,'bdgdeviceMaxAge':bdgdeviceMaxAge,'bdgdeviceHoldTime':bdgdeviceHoldTime,'bdgdeviceFwdDly':bdgdeviceFwdDly,'bdgdeviceBdgHello':bdgdeviceBdgHello,'bdgdeviceBdgPriority':bdgdeviceBdgPriority,'bdgdeviceResetCounts':bdgdeviceResetCounts,'bdgdeviceUptime':bdgdeviceUptime,'bdgdeviceTrapType':bdgdeviceTrapType,'bdgPort':bdgPort,'bdgPortAddress':bdgPortAddress,'bdgPortName':bdgPortName,'bdgPortType':bdgPortType,'bdgPortStatus':bdgPortStatus,'bdgPortNetName':bdgPortNetName,'bdgPortFrRx':bdgPortFrRx,'bdgPortDisInb':bdgPortDisInb,'bdgPortFwdOutb':bdgPortFwdOutb,'bdgPortDisLOB':bdgPortDisLOB,'bdgPortDisTDE':bdgPortDisTDE,'bdgPortDisErr':bdgPortDisErr,'bdgPortColl':bdgPortColl,'bdgPortTxAbrt':bdgPortTxAbrt,'bdgPortOowColl':bdgPortOowColl,'bdgPortCRCErr':bdgPortCRCErr,'bdgPortFrAlErr':bdgPortFrAlErr,'bdgPortPriority':bdgPortPriority,'bdgPortState':bdgPortState,'bdgPortPathCost':bdgPortPathCost,'bdgPortDesigCost':bdgPortDesigCost,'bdgPortDesigBrdg':bdgPortDesigBrdg,'bdgPortDesigPort':bdgPortDesigPort,'bdgPortTopChgAck':bdgPortTopChgAck,'bdgPortDesigRoot':bdgPortDesigRoot,'bdgPortRuntPackets':bdgPortRuntPackets,'bdgPortOversizePackets':bdgPortOversizePackets,'bdgPortFrFilt':bdgPortFrFilt,'filterDB':filterDB,'acqDB':acqDB,'acqStats':acqStats,'acqTotalEntries':acqTotalEntries,'acqMaxEntries':acqMaxEntries,'acqStaticEntries':acqStaticEntries,'acqStaticAgeTime':acqStaticAgeTime,'acqDynEntries':acqDynEntries,'acqDynAgeTime':acqDynAgeTime,'acqEraseDatabase':acqEraseDatabase,'acqOptions':acqOptions,'acqCreate00':acqCreate00,'acqCreate20':acqCreate20,'acqCreate01':acqCreate01,'acqCreate21':acqCreate21,'acqDelete':acqDelete,'acqDispType':acqDispType,'acqDispOutp1':acqDispOutp1,'acqDispOutp2':acqDispOutp2,'acqSrcAddress':acqSrcAddress,'permDB':permDB,'permStats':permStats,'permMaxEntries':permMaxEntries,'permCurrEntries':permCurrEntries,'permEraseDatabase':permEraseDatabase,'permOptions':permOptions,'permCreate00':permCreate00,'permCreate20':permCreate20,'permCreate01':permCreate01,'permCreate21':permCreate21,'permDelete':permDelete,'permDispType':permDispType,'permDispOutp1':permDispOutp1,'permDispOutp2':permDispOutp2,'permSrcAddress':permSrcAddress,_H:specialDB,'specStats':specStats,'specNumEntries':specNumEntries,'specMaxEntries':specMaxEntries,'specNextFilterNum':specNextFilterNum,'specFilters':specFilters,'specEnable':specEnable,'specPort1':specPort1,'specPort2':specPort2,'specDestAddress':specDestAddress,'specSrcAddress':specSrcAddress,'specType':specType,'specDataField':specDataField,'specDeleteFilter':specDeleteFilter,'trapTypes':trapTypes,'bdgTables':bdgTables,'lmcommon':lmcommon,'mAC':mAC,'ieee8023':ieee8023,'pcIF':pcIF,'pcIfRev':pcIfRev,'pcDeviceName':pcDeviceName,'pcBoardType':pcBoardType,'pcOwnerName':pcOwnerName,'pcLocation':pcLocation,'pcMMACAddr':pcMMACAddr,'pcMMACBoard':pcMMACBoard,'pcMMACPort':pcMMACPort,'pcApplication':pcApplication,'pcDriverRev':pcDriverRev,'pcOnboardMemory':pcOnboardMemory,'pcComment':pcComment,'pcMACAddr':pcMACAddr,'pcFramesXmit':pcFramesXmit,'pcBytesXmit':pcBytesXmit,'pcMcastXmit':pcMcastXmit,'pcBcastXmit':pcBcastXmit,'pcDeferXmit':pcDeferXmit,'pcSglColl':pcSglColl,'pcMultiColl':pcMultiColl,'pcTotXmitErrs':pcTotXmitErrs,'pcLateColls':pcLateColls,'pcXcessColls':pcXcessColls,'pcCarrErr':pcCarrErr,'pcFramesRec':pcFramesRec,'pcBytesRec':pcBytesRec,'pcMcastRec':pcMcastRec,'pcBcastRec':pcBcastRec,'pcTotRecErrs':pcTotRecErrs,'pcTooLong':pcTooLong,'pcTooShort':pcTooShort,'pcAlignErrs':pcAlignErrs,'pcCRCErrs':pcCRCErrs,'pcLenErrs':pcLenErrs,'pcIntRecErr':pcIntRecErr,'pcSqeErr':pcSqeErr})