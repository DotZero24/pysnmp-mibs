_Y='currentObjectGroup'
_X='hwInfoPortIBMaxSpeed'
_W='hwInfoPortIBStartTime'
_V='hwInfoPortIBBufferOverrunErrors'
_U='hwInfoPortIBLinkErrors'
_T='hwInfoPortIBReceiveConstraintErrors'
_S='hwInfoPortIBNotSendPacakges'
_R='hwInfoPortIBReceiveTransmitErrors'
_Q='hwInfoPortIBRemoteReceiveErrors'
_P='hwInfoPortIBReceiveErrors'
_O='hwInfoPortIBLinkErrorRecovery'
_N='hwInfoPortIBSymbolError'
_M='hwInfoPortIBRole'
_L='hwInfoPortIBWWN'
_K='hwInfoPortIBWorkingRate'
_J='hwInfoPortIBType'
_I='hwInfoPortIBRunningStatus'
_H='hwInfoPortIBHealthStatus'
_G='hwInfoPortIBLocation'
_F='hwInfoPortIBParentID'
_E='hwInfoPortIBParentType'
_D='hwInfoPortIBID'
_C='read-only'
_B='HUAWEI-DEVICE-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
storage=ModuleIdentity((1,3,6,1,4,1,2011,2,251))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,2011,2))
_DeviceManager_ObjectIdentity=ObjectIdentity
deviceManager=_DeviceManager_ObjectIdentity((1,3,6,1,4,1,2011,2,251,22))
_HwInfoPortIBTable_Object=MibTable
hwInfoPortIBTable=_HwInfoPortIBTable_Object((1,3,6,1,4,1,2011,2,251,22,16500))
if mibBuilder.loadTexts:hwInfoPortIBTable.setStatus(_A)
_HwInfoPortIBEntry_Object=MibTableRow
hwInfoPortIBEntry=_HwInfoPortIBEntry_Object((1,3,6,1,4,1,2011,2,251,22,16500,1))
hwInfoPortIBEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hwInfoPortIBEntry.setStatus(_A)
_HwInfoPortIBID_Type=OctetString
_HwInfoPortIBID_Object=MibTableColumn
hwInfoPortIBID=_HwInfoPortIBID_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,1),_HwInfoPortIBID_Type())
hwInfoPortIBID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBID.setStatus(_A)
_HwInfoPortIBParentType_Type=Unsigned32
_HwInfoPortIBParentType_Object=MibTableColumn
hwInfoPortIBParentType=_HwInfoPortIBParentType_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,2),_HwInfoPortIBParentType_Type())
hwInfoPortIBParentType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBParentType.setStatus(_A)
_HwInfoPortIBParentID_Type=OctetString
_HwInfoPortIBParentID_Object=MibTableColumn
hwInfoPortIBParentID=_HwInfoPortIBParentID_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,3),_HwInfoPortIBParentID_Type())
hwInfoPortIBParentID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBParentID.setStatus(_A)
_HwInfoPortIBLocation_Type=OctetString
_HwInfoPortIBLocation_Object=MibTableColumn
hwInfoPortIBLocation=_HwInfoPortIBLocation_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,4),_HwInfoPortIBLocation_Type())
hwInfoPortIBLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBLocation.setStatus(_A)
_HwInfoPortIBHealthStatus_Type=Unsigned32
_HwInfoPortIBHealthStatus_Object=MibTableColumn
hwInfoPortIBHealthStatus=_HwInfoPortIBHealthStatus_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,5),_HwInfoPortIBHealthStatus_Type())
hwInfoPortIBHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBHealthStatus.setStatus(_A)
_HwInfoPortIBRunningStatus_Type=Unsigned32
_HwInfoPortIBRunningStatus_Object=MibTableColumn
hwInfoPortIBRunningStatus=_HwInfoPortIBRunningStatus_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,6),_HwInfoPortIBRunningStatus_Type())
hwInfoPortIBRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBRunningStatus.setStatus(_A)
_HwInfoPortIBType_Type=Unsigned32
_HwInfoPortIBType_Object=MibTableColumn
hwInfoPortIBType=_HwInfoPortIBType_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,7),_HwInfoPortIBType_Type())
hwInfoPortIBType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBType.setStatus(_A)
_HwInfoPortIBWorkingRate_Type=Unsigned32
_HwInfoPortIBWorkingRate_Object=MibTableColumn
hwInfoPortIBWorkingRate=_HwInfoPortIBWorkingRate_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,8),_HwInfoPortIBWorkingRate_Type())
hwInfoPortIBWorkingRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBWorkingRate.setStatus(_A)
_HwInfoPortIBWWN_Type=OctetString
_HwInfoPortIBWWN_Object=MibTableColumn
hwInfoPortIBWWN=_HwInfoPortIBWWN_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,9),_HwInfoPortIBWWN_Type())
hwInfoPortIBWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBWWN.setStatus(_A)
_HwInfoPortIBRole_Type=Unsigned32
_HwInfoPortIBRole_Object=MibTableColumn
hwInfoPortIBRole=_HwInfoPortIBRole_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,10),_HwInfoPortIBRole_Type())
hwInfoPortIBRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBRole.setStatus(_A)
_HwInfoPortIBSymbolError_Type=Unsigned32
_HwInfoPortIBSymbolError_Object=MibTableColumn
hwInfoPortIBSymbolError=_HwInfoPortIBSymbolError_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,11),_HwInfoPortIBSymbolError_Type())
hwInfoPortIBSymbolError.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBSymbolError.setStatus(_A)
_HwInfoPortIBLinkErrorRecovery_Type=Unsigned32
_HwInfoPortIBLinkErrorRecovery_Object=MibTableColumn
hwInfoPortIBLinkErrorRecovery=_HwInfoPortIBLinkErrorRecovery_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,12),_HwInfoPortIBLinkErrorRecovery_Type())
hwInfoPortIBLinkErrorRecovery.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBLinkErrorRecovery.setStatus(_A)
_HwInfoPortIBReceiveErrors_Type=Unsigned32
_HwInfoPortIBReceiveErrors_Object=MibTableColumn
hwInfoPortIBReceiveErrors=_HwInfoPortIBReceiveErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,13),_HwInfoPortIBReceiveErrors_Type())
hwInfoPortIBReceiveErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBReceiveErrors.setStatus(_A)
_HwInfoPortIBRemoteReceiveErrors_Type=Unsigned32
_HwInfoPortIBRemoteReceiveErrors_Object=MibTableColumn
hwInfoPortIBRemoteReceiveErrors=_HwInfoPortIBRemoteReceiveErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,14),_HwInfoPortIBRemoteReceiveErrors_Type())
hwInfoPortIBRemoteReceiveErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBRemoteReceiveErrors.setStatus(_A)
_HwInfoPortIBReceiveTransmitErrors_Type=Unsigned32
_HwInfoPortIBReceiveTransmitErrors_Object=MibTableColumn
hwInfoPortIBReceiveTransmitErrors=_HwInfoPortIBReceiveTransmitErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,15),_HwInfoPortIBReceiveTransmitErrors_Type())
hwInfoPortIBReceiveTransmitErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBReceiveTransmitErrors.setStatus(_A)
_HwInfoPortIBNotSendPacakges_Type=Unsigned32
_HwInfoPortIBNotSendPacakges_Object=MibTableColumn
hwInfoPortIBNotSendPacakges=_HwInfoPortIBNotSendPacakges_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,16),_HwInfoPortIBNotSendPacakges_Type())
hwInfoPortIBNotSendPacakges.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBNotSendPacakges.setStatus(_A)
_HwInfoPortIBReceiveConstraintErrors_Type=Unsigned32
_HwInfoPortIBReceiveConstraintErrors_Object=MibTableColumn
hwInfoPortIBReceiveConstraintErrors=_HwInfoPortIBReceiveConstraintErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,17),_HwInfoPortIBReceiveConstraintErrors_Type())
hwInfoPortIBReceiveConstraintErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBReceiveConstraintErrors.setStatus(_A)
_HwInfoPortIBLinkErrors_Type=Unsigned32
_HwInfoPortIBLinkErrors_Object=MibTableColumn
hwInfoPortIBLinkErrors=_HwInfoPortIBLinkErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,18),_HwInfoPortIBLinkErrors_Type())
hwInfoPortIBLinkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBLinkErrors.setStatus(_A)
_HwInfoPortIBBufferOverrunErrors_Type=Unsigned32
_HwInfoPortIBBufferOverrunErrors_Object=MibTableColumn
hwInfoPortIBBufferOverrunErrors=_HwInfoPortIBBufferOverrunErrors_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,19),_HwInfoPortIBBufferOverrunErrors_Type())
hwInfoPortIBBufferOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBBufferOverrunErrors.setStatus(_A)
_HwInfoPortIBStartTime_Type=OctetString
_HwInfoPortIBStartTime_Object=MibTableColumn
hwInfoPortIBStartTime=_HwInfoPortIBStartTime_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,20),_HwInfoPortIBStartTime_Type())
hwInfoPortIBStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBStartTime.setStatus(_A)
_HwInfoPortIBMaxSpeed_Type=Unsigned32
_HwInfoPortIBMaxSpeed_Object=MibTableColumn
hwInfoPortIBMaxSpeed=_HwInfoPortIBMaxSpeed_Object((1,3,6,1,4,1,2011,2,251,22,16500,1,21),_HwInfoPortIBMaxSpeed_Type())
hwInfoPortIBMaxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortIBMaxSpeed.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'huawei':huawei,'products':products,'storage':storage,'deviceManager':deviceManager,'hwInfoPortIBTable':hwInfoPortIBTable,'hwInfoPortIBEntry':hwInfoPortIBEntry,_D:hwInfoPortIBID,_E:hwInfoPortIBParentType,_F:hwInfoPortIBParentID,_G:hwInfoPortIBLocation,_H:hwInfoPortIBHealthStatus,_I:hwInfoPortIBRunningStatus,_J:hwInfoPortIBType,_K:hwInfoPortIBWorkingRate,_L:hwInfoPortIBWWN,_M:hwInfoPortIBRole,_N:hwInfoPortIBSymbolError,_O:hwInfoPortIBLinkErrorRecovery,_P:hwInfoPortIBReceiveErrors,_Q:hwInfoPortIBRemoteReceiveErrors,_R:hwInfoPortIBReceiveTransmitErrors,_S:hwInfoPortIBNotSendPacakges,_T:hwInfoPortIBReceiveConstraintErrors,_U:hwInfoPortIBLinkErrors,_V:hwInfoPortIBBufferOverrunErrors,_W:hwInfoPortIBStartTime,_X:hwInfoPortIBMaxSpeed,'isoConformance':isoConformance,'isoGroups':isoGroups,_Y:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})