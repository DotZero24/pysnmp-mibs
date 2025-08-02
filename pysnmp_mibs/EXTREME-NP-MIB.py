_L='extremeMplsTlsNum'
_K='extremeATMPvc'
_J='extremeATMPortNum'
_I='extremeATMPortNumber'
_H='extremeSMASlotNumber'
_G='extremeNPModuleSlotNumber'
_F='OctetString'
_E='EXTREME-NP-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
extremeNPMib=ModuleIdentity((1,3,6,1,4,1,1916,1,21))
_ExtremeNPModule_ObjectIdentity=ObjectIdentity
extremeNPModule=_ExtremeNPModule_ObjectIdentity((1,3,6,1,4,1,1916,1,21,1))
_ExtremeNPModuleTable_Object=MibTable
extremeNPModuleTable=_ExtremeNPModuleTable_Object((1,3,6,1,4,1,1916,1,21,1,1))
if mibBuilder.loadTexts:extremeNPModuleTable.setStatus(_A)
_ExtremeNPModuleEntry_Object=MibTableRow
extremeNPModuleEntry=_ExtremeNPModuleEntry_Object((1,3,6,1,4,1,1916,1,21,1,1,1))
extremeNPModuleEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:extremeNPModuleEntry.setStatus(_A)
class _ExtremeNPModuleSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeNPModuleSlotNumber_Type.__name__=_D
_ExtremeNPModuleSlotNumber_Object=MibTableColumn
extremeNPModuleSlotNumber=_ExtremeNPModuleSlotNumber_Object((1,3,6,1,4,1,1916,1,21,1,1,1,1),_ExtremeNPModuleSlotNumber_Type())
extremeNPModuleSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleSlotNumber.setStatus(_A)
class _ExtremeNPModuleDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeNPModuleDescription_Type.__name__=_C
_ExtremeNPModuleDescription_Object=MibTableColumn
extremeNPModuleDescription=_ExtremeNPModuleDescription_Object((1,3,6,1,4,1,1916,1,21,1,1,1,2),_ExtremeNPModuleDescription_Type())
extremeNPModuleDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleDescription.setStatus(_A)
class _ExtremeNPModuleCurrentSoftware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_ExtremeNPModuleCurrentSoftware_Type.__name__=_C
_ExtremeNPModuleCurrentSoftware_Object=MibTableColumn
extremeNPModuleCurrentSoftware=_ExtremeNPModuleCurrentSoftware_Object((1,3,6,1,4,1,1916,1,21,1,1,1,3),_ExtremeNPModuleCurrentSoftware_Type())
extremeNPModuleCurrentSoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleCurrentSoftware.setStatus(_A)
class _ExtremeNPModulePrimarySoftware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_ExtremeNPModulePrimarySoftware_Type.__name__=_C
_ExtremeNPModulePrimarySoftware_Object=MibTableColumn
extremeNPModulePrimarySoftware=_ExtremeNPModulePrimarySoftware_Object((1,3,6,1,4,1,1916,1,21,1,1,1,4),_ExtremeNPModulePrimarySoftware_Type())
extremeNPModulePrimarySoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModulePrimarySoftware.setStatus(_A)
class _ExtremeNPModuleSecondarySoftware_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_ExtremeNPModuleSecondarySoftware_Type.__name__=_C
_ExtremeNPModuleSecondarySoftware_Object=MibTableColumn
extremeNPModuleSecondarySoftware=_ExtremeNPModuleSecondarySoftware_Object((1,3,6,1,4,1,1916,1,21,1,1,1,5),_ExtremeNPModuleSecondarySoftware_Type())
extremeNPModuleSecondarySoftware.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleSecondarySoftware.setStatus(_A)
class _ExtremeNPModuleBootromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ExtremeNPModuleBootromVersion_Type.__name__=_C
_ExtremeNPModuleBootromVersion_Object=MibTableColumn
extremeNPModuleBootromVersion=_ExtremeNPModuleBootromVersion_Object((1,3,6,1,4,1,1916,1,21,1,1,1,6),_ExtremeNPModuleBootromVersion_Type())
extremeNPModuleBootromVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleBootromVersion.setStatus(_A)
class _ExtremeNPModuleProcessorState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ExtremeNPModuleProcessorState_Type.__name__=_F
_ExtremeNPModuleProcessorState_Object=MibTableColumn
extremeNPModuleProcessorState=_ExtremeNPModuleProcessorState_Object((1,3,6,1,4,1,1916,1,21,1,1,1,7),_ExtremeNPModuleProcessorState_Type())
extremeNPModuleProcessorState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeNPModuleProcessorState.setStatus(_A)
_ExtremeSMAModule_ObjectIdentity=ObjectIdentity
extremeSMAModule=_ExtremeSMAModule_ObjectIdentity((1,3,6,1,4,1,1916,1,21,2))
_ExtremeSMATable_Object=MibTable
extremeSMATable=_ExtremeSMATable_Object((1,3,6,1,4,1,1916,1,21,2,1))
if mibBuilder.loadTexts:extremeSMATable.setStatus(_A)
_ExtremeSMAEntry_Object=MibTableRow
extremeSMAEntry=_ExtremeSMAEntry_Object((1,3,6,1,4,1,1916,1,21,2,1,1))
extremeSMAEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:extremeSMAEntry.setStatus(_A)
class _ExtremeSMASlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeSMASlotNumber_Type.__name__=_D
_ExtremeSMASlotNumber_Object=MibTableColumn
extremeSMASlotNumber=_ExtremeSMASlotNumber_Object((1,3,6,1,4,1,1916,1,21,2,1,1,1),_ExtremeSMASlotNumber_Type())
extremeSMASlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMASlotNumber.setStatus(_A)
class _ExtremeSMAProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ExtremeSMAProtocolVersion_Type.__name__=_D
_ExtremeSMAProtocolVersion_Object=MibTableColumn
extremeSMAProtocolVersion=_ExtremeSMAProtocolVersion_Object((1,3,6,1,4,1,1916,1,21,2,1,1,2),_ExtremeSMAProtocolVersion_Type())
extremeSMAProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMAProtocolVersion.setStatus(_A)
class _ExtremeSMAServiceVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ExtremeSMAServiceVersion_Type.__name__=_C
_ExtremeSMAServiceVersion_Object=MibTableColumn
extremeSMAServiceVersion=_ExtremeSMAServiceVersion_Object((1,3,6,1,4,1,1916,1,21,2,1,1,3),_ExtremeSMAServiceVersion_Type())
extremeSMAServiceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMAServiceVersion.setStatus(_A)
_ExtremeSMAUpTime_Type=Unsigned32
_ExtremeSMAUpTime_Object=MibTableColumn
extremeSMAUpTime=_ExtremeSMAUpTime_Object((1,3,6,1,4,1,1916,1,21,2,1,1,4),_ExtremeSMAUpTime_Type())
extremeSMAUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMAUpTime.setStatus(_A)
_ExtremeSMACpuUtilization_Type=Unsigned32
_ExtremeSMACpuUtilization_Object=MibTableColumn
extremeSMACpuUtilization=_ExtremeSMACpuUtilization_Object((1,3,6,1,4,1,1916,1,21,2,1,1,5),_ExtremeSMACpuUtilization_Type())
extremeSMACpuUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMACpuUtilization.setStatus(_A)
_ExtremeSMAMemUtilization_Type=Unsigned32
_ExtremeSMAMemUtilization_Object=MibTableColumn
extremeSMAMemUtilization=_ExtremeSMAMemUtilization_Object((1,3,6,1,4,1,1916,1,21,2,1,1,6),_ExtremeSMAMemUtilization_Type())
extremeSMAMemUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMAMemUtilization.setStatus(_A)
_ExtremeSMAQosBroadcaster_Type=Unsigned32
_ExtremeSMAQosBroadcaster_Object=MibTableColumn
extremeSMAQosBroadcaster=_ExtremeSMAQosBroadcaster_Object((1,3,6,1,4,1,1916,1,21,2,1,1,7),_ExtremeSMAQosBroadcaster_Type())
extremeSMAQosBroadcaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMAQosBroadcaster.setStatus(_A)
_ExtremeSMANumFromBroadcaster_Type=Unsigned32
_ExtremeSMANumFromBroadcaster_Object=MibTableColumn
extremeSMANumFromBroadcaster=_ExtremeSMANumFromBroadcaster_Object((1,3,6,1,4,1,1916,1,21,2,1,1,8),_ExtremeSMANumFromBroadcaster_Type())
extremeSMANumFromBroadcaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMANumFromBroadcaster.setStatus(_A)
_ExtremeSMANumToListener_Type=Unsigned32
_ExtremeSMANumToListener_Object=MibTableColumn
extremeSMANumToListener=_ExtremeSMANumToListener_Object((1,3,6,1,4,1,1916,1,21,2,1,1,9),_ExtremeSMANumToListener_Type())
extremeSMANumToListener.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMANumToListener.setStatus(_A)
_ExtremeSMABytesBroadcaster_Type=Counter64
_ExtremeSMABytesBroadcaster_Object=MibTableColumn
extremeSMABytesBroadcaster=_ExtremeSMABytesBroadcaster_Object((1,3,6,1,4,1,1916,1,21,2,1,1,10),_ExtremeSMABytesBroadcaster_Type())
extremeSMABytesBroadcaster.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMABytesBroadcaster.setStatus(_A)
_ExtremeSMABytesListener_Type=Counter64
_ExtremeSMABytesListener_Object=MibTableColumn
extremeSMABytesListener=_ExtremeSMABytesListener_Object((1,3,6,1,4,1,1916,1,21,2,1,1,11),_ExtremeSMABytesListener_Type())
extremeSMABytesListener.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeSMABytesListener.setStatus(_A)
_ExtremeATMModule_ObjectIdentity=ObjectIdentity
extremeATMModule=_ExtremeATMModule_ObjectIdentity((1,3,6,1,4,1,1916,1,21,3))
_ExtremeATMCellPduTable_Object=MibTable
extremeATMCellPduTable=_ExtremeATMCellPduTable_Object((1,3,6,1,4,1,1916,1,21,3,1))
if mibBuilder.loadTexts:extremeATMCellPduTable.setStatus(_A)
_ExtremeATMCellPduEntry_Object=MibTableRow
extremeATMCellPduEntry=_ExtremeATMCellPduEntry_Object((1,3,6,1,4,1,1916,1,21,3,1,1))
extremeATMCellPduEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:extremeATMCellPduEntry.setStatus(_A)
class _ExtremeATMPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ExtremeATMPortNumber_Type.__name__=_D
_ExtremeATMPortNumber_Object=MibTableColumn
extremeATMPortNumber=_ExtremeATMPortNumber_Object((1,3,6,1,4,1,1916,1,21,3,1,1,1),_ExtremeATMPortNumber_Type())
extremeATMPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMPortNumber.setStatus(_A)
_ExtremeATMRxCell_Type=Unsigned32
_ExtremeATMRxCell_Object=MibTableColumn
extremeATMRxCell=_ExtremeATMRxCell_Object((1,3,6,1,4,1,1916,1,21,3,1,1,2),_ExtremeATMRxCell_Type())
extremeATMRxCell.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMRxCell.setStatus(_A)
_ExtremeATMTxCell_Type=Unsigned32
_ExtremeATMTxCell_Object=MibTableColumn
extremeATMTxCell=_ExtremeATMTxCell_Object((1,3,6,1,4,1,1916,1,21,3,1,1,3),_ExtremeATMTxCell_Type())
extremeATMTxCell.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMTxCell.setStatus(_A)
_ExtremeATMRxCellHecError_Type=Unsigned32
_ExtremeATMRxCellHecError_Object=MibTableColumn
extremeATMRxCellHecError=_ExtremeATMRxCellHecError_Object((1,3,6,1,4,1,1916,1,21,3,1,1,4),_ExtremeATMRxCellHecError_Type())
extremeATMRxCellHecError.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMRxCellHecError.setStatus(_A)
_ExtremeATMRxCellError_Type=Unsigned32
_ExtremeATMRxCellError_Object=MibTableColumn
extremeATMRxCellError=_ExtremeATMRxCellError_Object((1,3,6,1,4,1,1916,1,21,3,1,1,5),_ExtremeATMRxCellError_Type())
extremeATMRxCellError.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMRxCellError.setStatus(_A)
_ExtremeATMRxAAL5Pdu_Type=Unsigned32
_ExtremeATMRxAAL5Pdu_Object=MibTableColumn
extremeATMRxAAL5Pdu=_ExtremeATMRxAAL5Pdu_Object((1,3,6,1,4,1,1916,1,21,3,1,1,6),_ExtremeATMRxAAL5Pdu_Type())
extremeATMRxAAL5Pdu.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMRxAAL5Pdu.setStatus(_A)
_ExtremeATMTxAAL5Pdu_Type=Unsigned32
_ExtremeATMTxAAL5Pdu_Object=MibTableColumn
extremeATMTxAAL5Pdu=_ExtremeATMTxAAL5Pdu_Object((1,3,6,1,4,1,1916,1,21,3,1,1,7),_ExtremeATMTxAAL5Pdu_Type())
extremeATMTxAAL5Pdu.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMTxAAL5Pdu.setStatus(_A)
_ExtremeATMRxAAL5Bytes_Type=Counter64
_ExtremeATMRxAAL5Bytes_Object=MibTableColumn
extremeATMRxAAL5Bytes=_ExtremeATMRxAAL5Bytes_Object((1,3,6,1,4,1,1916,1,21,3,1,1,8),_ExtremeATMRxAAL5Bytes_Type())
extremeATMRxAAL5Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMRxAAL5Bytes.setStatus(_A)
_ExtremeATMTxAAL5Bytes_Type=Counter64
_ExtremeATMTxAAL5Bytes_Object=MibTableColumn
extremeATMTxAAL5Bytes=_ExtremeATMTxAAL5Bytes_Object((1,3,6,1,4,1,1916,1,21,3,1,1,9),_ExtremeATMTxAAL5Bytes_Type())
extremeATMTxAAL5Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMTxAAL5Bytes.setStatus(_A)
class _ExtremeATMPortStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_ExtremeATMPortStatus_Type.__name__=_C
_ExtremeATMPortStatus_Object=MibTableColumn
extremeATMPortStatus=_ExtremeATMPortStatus_Object((1,3,6,1,4,1,1916,1,21,3,1,1,10),_ExtremeATMPortStatus_Type())
extremeATMPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMPortStatus.setStatus(_A)
_ExtremeATMVpiVciTable_Object=MibTable
extremeATMVpiVciTable=_ExtremeATMVpiVciTable_Object((1,3,6,1,4,1,1916,1,21,3,2))
if mibBuilder.loadTexts:extremeATMVpiVciTable.setStatus(_A)
_ExtremeATMVpiVciEntry_Object=MibTableRow
extremeATMVpiVciEntry=_ExtremeATMVpiVciEntry_Object((1,3,6,1,4,1,1916,1,21,3,2,1))
extremeATMVpiVciEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:extremeATMVpiVciEntry.setStatus(_A)
class _ExtremeATMPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ExtremeATMPortNum_Type.__name__=_D
_ExtremeATMPortNum_Object=MibTableColumn
extremeATMPortNum=_ExtremeATMPortNum_Object((1,3,6,1,4,1,1916,1,21,3,2,1,1),_ExtremeATMPortNum_Type())
extremeATMPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMPortNum.setStatus(_A)
class _ExtremeATMPvc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3072))
_ExtremeATMPvc_Type.__name__=_D
_ExtremeATMPvc_Object=MibTableColumn
extremeATMPvc=_ExtremeATMPvc_Object((1,3,6,1,4,1,1916,1,21,3,2,1,2),_ExtremeATMPvc_Type())
extremeATMPvc.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMPvc.setStatus(_A)
class _ExtremeATMVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ExtremeATMVpi_Type.__name__=_D
_ExtremeATMVpi_Object=MibTableColumn
extremeATMVpi=_ExtremeATMVpi_Object((1,3,6,1,4,1,1916,1,21,3,2,1,3),_ExtremeATMVpi_Type())
extremeATMVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMVpi.setStatus(_A)
class _ExtremeATMVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(17,4095))
_ExtremeATMVci_Type.__name__=_D
_ExtremeATMVci_Object=MibTableColumn
extremeATMVci=_ExtremeATMVci_Object((1,3,6,1,4,1,1916,1,21,3,2,1,4),_ExtremeATMVci_Type())
extremeATMVci.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeATMVci.setStatus(_A)
_ExtremeMplsModule_ObjectIdentity=ObjectIdentity
extremeMplsModule=_ExtremeMplsModule_ObjectIdentity((1,3,6,1,4,1,1916,1,21,4))
_ExtremeMplsTlsTable_Object=MibTable
extremeMplsTlsTable=_ExtremeMplsTlsTable_Object((1,3,6,1,4,1,1916,1,21,4,1))
if mibBuilder.loadTexts:extremeMplsTlsTable.setStatus(_A)
_ExtremeMplsTlsEntry_Object=MibTableRow
extremeMplsTlsEntry=_ExtremeMplsTlsEntry_Object((1,3,6,1,4,1,1916,1,21,4,1,1))
extremeMplsTlsEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:extremeMplsTlsEntry.setStatus(_A)
class _ExtremeMplsTlsNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16384))
_ExtremeMplsTlsNum_Type.__name__=_D
_ExtremeMplsTlsNum_Object=MibTableColumn
extremeMplsTlsNum=_ExtremeMplsTlsNum_Object((1,3,6,1,4,1,1916,1,21,4,1,1,1),_ExtremeMplsTlsNum_Type())
extremeMplsTlsNum.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsNum.setStatus(_A)
class _ExtremeMplsTlsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeMplsTlsName_Type.__name__=_C
_ExtremeMplsTlsName_Object=MibTableColumn
extremeMplsTlsName=_ExtremeMplsTlsName_Object((1,3,6,1,4,1,1916,1,21,4,1,1,2),_ExtremeMplsTlsName_Type())
extremeMplsTlsName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsName.setStatus(_A)
_ExtremeMplsTlsLocalIpAddr_Type=IpAddress
_ExtremeMplsTlsLocalIpAddr_Object=MibTableColumn
extremeMplsTlsLocalIpAddr=_ExtremeMplsTlsLocalIpAddr_Object((1,3,6,1,4,1,1916,1,21,4,1,1,3),_ExtremeMplsTlsLocalIpAddr_Type())
extremeMplsTlsLocalIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsLocalIpAddr.setStatus(_A)
_ExtremeMplsTlsPeerIpAddr_Type=IpAddress
_ExtremeMplsTlsPeerIpAddr_Object=MibTableColumn
extremeMplsTlsPeerIpAddr=_ExtremeMplsTlsPeerIpAddr_Object((1,3,6,1,4,1,1916,1,21,4,1,1,4),_ExtremeMplsTlsPeerIpAddr_Type())
extremeMplsTlsPeerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsPeerIpAddr.setStatus(_A)
_ExtremeMplsTlsLocalVlanID_Type=Unsigned32
_ExtremeMplsTlsLocalVlanID_Object=MibTableColumn
extremeMplsTlsLocalVlanID=_ExtremeMplsTlsLocalVlanID_Object((1,3,6,1,4,1,1916,1,21,4,1,1,5),_ExtremeMplsTlsLocalVlanID_Type())
extremeMplsTlsLocalVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsLocalVlanID.setStatus(_A)
class _ExtremeMplsTlsLocalVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_ExtremeMplsTlsLocalVlanName_Type.__name__=_C
_ExtremeMplsTlsLocalVlanName_Object=MibTableColumn
extremeMplsTlsLocalVlanName=_ExtremeMplsTlsLocalVlanName_Object((1,3,6,1,4,1,1916,1,21,4,1,1,6),_ExtremeMplsTlsLocalVlanName_Type())
extremeMplsTlsLocalVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsLocalVlanName.setStatus(_A)
_ExtremeMplsTlsDynamic_Type=Unsigned32
_ExtremeMplsTlsDynamic_Object=MibTableColumn
extremeMplsTlsDynamic=_ExtremeMplsTlsDynamic_Object((1,3,6,1,4,1,1916,1,21,4,1,1,7),_ExtremeMplsTlsDynamic_Type())
extremeMplsTlsDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsDynamic.setStatus(_A)
_ExtremeMplsTlsType_Type=Unsigned32
_ExtremeMplsTlsType_Object=MibTableColumn
extremeMplsTlsType=_ExtremeMplsTlsType_Object((1,3,6,1,4,1,1916,1,21,4,1,1,8),_ExtremeMplsTlsType_Type())
extremeMplsTlsType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsType.setStatus(_A)
_ExtremeMplsTlsVcID_Type=Unsigned32
_ExtremeMplsTlsVcID_Object=MibTableColumn
extremeMplsTlsVcID=_ExtremeMplsTlsVcID_Object((1,3,6,1,4,1,1916,1,21,4,1,1,9),_ExtremeMplsTlsVcID_Type())
extremeMplsTlsVcID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsVcID.setStatus(_A)
_ExtremeMplsTlsLocalGroupID_Type=Unsigned32
_ExtremeMplsTlsLocalGroupID_Object=MibTableColumn
extremeMplsTlsLocalGroupID=_ExtremeMplsTlsLocalGroupID_Object((1,3,6,1,4,1,1916,1,21,4,1,1,10),_ExtremeMplsTlsLocalGroupID_Type())
extremeMplsTlsLocalGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsLocalGroupID.setStatus(_A)
_ExtremeMplsTlsRemoteGroupID_Type=Unsigned32
_ExtremeMplsTlsRemoteGroupID_Object=MibTableColumn
extremeMplsTlsRemoteGroupID=_ExtremeMplsTlsRemoteGroupID_Object((1,3,6,1,4,1,1916,1,21,4,1,1,11),_ExtremeMplsTlsRemoteGroupID_Type())
extremeMplsTlsRemoteGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsRemoteGroupID.setStatus(_A)
_ExtremeMplsTlsIngressVcLabel_Type=Unsigned32
_ExtremeMplsTlsIngressVcLabel_Object=MibTableColumn
extremeMplsTlsIngressVcLabel=_ExtremeMplsTlsIngressVcLabel_Object((1,3,6,1,4,1,1916,1,21,4,1,1,12),_ExtremeMplsTlsIngressVcLabel_Type())
extremeMplsTlsIngressVcLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsIngressVcLabel.setStatus(_A)
_ExtremeMplsTlsEgressVcLabel_Type=Unsigned32
_ExtremeMplsTlsEgressVcLabel_Object=MibTableColumn
extremeMplsTlsEgressVcLabel=_ExtremeMplsTlsEgressVcLabel_Object((1,3,6,1,4,1,1916,1,21,4,1,1,13),_ExtremeMplsTlsEgressVcLabel_Type())
extremeMplsTlsEgressVcLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsEgressVcLabel.setStatus(_A)
class _ExtremeMplsTlsVcState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ExtremeMplsTlsVcState_Type.__name__=_C
_ExtremeMplsTlsVcState_Object=MibTableColumn
extremeMplsTlsVcState=_ExtremeMplsTlsVcState_Object((1,3,6,1,4,1,1916,1,21,4,1,1,14),_ExtremeMplsTlsVcState_Type())
extremeMplsTlsVcState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsVcState.setStatus(_A)
_ExtremeMplsTlsPacketTx_Type=Unsigned32
_ExtremeMplsTlsPacketTx_Object=MibTableColumn
extremeMplsTlsPacketTx=_ExtremeMplsTlsPacketTx_Object((1,3,6,1,4,1,1916,1,21,4,1,1,15),_ExtremeMplsTlsPacketTx_Type())
extremeMplsTlsPacketTx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsPacketTx.setStatus(_A)
_ExtremeMplsTlsPacketRx_Type=Unsigned32
_ExtremeMplsTlsPacketRx_Object=MibTableColumn
extremeMplsTlsPacketRx=_ExtremeMplsTlsPacketRx_Object((1,3,6,1,4,1,1916,1,21,4,1,1,16),_ExtremeMplsTlsPacketRx_Type())
extremeMplsTlsPacketRx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsPacketRx.setStatus(_A)
_ExtremeMplsTlsOctetTx_Type=Counter64
_ExtremeMplsTlsOctetTx_Object=MibTableColumn
extremeMplsTlsOctetTx=_ExtremeMplsTlsOctetTx_Object((1,3,6,1,4,1,1916,1,21,4,1,1,17),_ExtremeMplsTlsOctetTx_Type())
extremeMplsTlsOctetTx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsOctetTx.setStatus(_A)
_ExtremeMplsTlsOctetRx_Type=Counter64
_ExtremeMplsTlsOctetRx_Object=MibTableColumn
extremeMplsTlsOctetRx=_ExtremeMplsTlsOctetRx_Object((1,3,6,1,4,1,1916,1,21,4,1,1,18),_ExtremeMplsTlsOctetRx_Type())
extremeMplsTlsOctetRx.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMplsTlsOctetRx.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeNPMib':extremeNPMib,'extremeNPModule':extremeNPModule,'extremeNPModuleTable':extremeNPModuleTable,'extremeNPModuleEntry':extremeNPModuleEntry,_G:extremeNPModuleSlotNumber,'extremeNPModuleDescription':extremeNPModuleDescription,'extremeNPModuleCurrentSoftware':extremeNPModuleCurrentSoftware,'extremeNPModulePrimarySoftware':extremeNPModulePrimarySoftware,'extremeNPModuleSecondarySoftware':extremeNPModuleSecondarySoftware,'extremeNPModuleBootromVersion':extremeNPModuleBootromVersion,'extremeNPModuleProcessorState':extremeNPModuleProcessorState,'extremeSMAModule':extremeSMAModule,'extremeSMATable':extremeSMATable,'extremeSMAEntry':extremeSMAEntry,_H:extremeSMASlotNumber,'extremeSMAProtocolVersion':extremeSMAProtocolVersion,'extremeSMAServiceVersion':extremeSMAServiceVersion,'extremeSMAUpTime':extremeSMAUpTime,'extremeSMACpuUtilization':extremeSMACpuUtilization,'extremeSMAMemUtilization':extremeSMAMemUtilization,'extremeSMAQosBroadcaster':extremeSMAQosBroadcaster,'extremeSMANumFromBroadcaster':extremeSMANumFromBroadcaster,'extremeSMANumToListener':extremeSMANumToListener,'extremeSMABytesBroadcaster':extremeSMABytesBroadcaster,'extremeSMABytesListener':extremeSMABytesListener,'extremeATMModule':extremeATMModule,'extremeATMCellPduTable':extremeATMCellPduTable,'extremeATMCellPduEntry':extremeATMCellPduEntry,_I:extremeATMPortNumber,'extremeATMRxCell':extremeATMRxCell,'extremeATMTxCell':extremeATMTxCell,'extremeATMRxCellHecError':extremeATMRxCellHecError,'extremeATMRxCellError':extremeATMRxCellError,'extremeATMRxAAL5Pdu':extremeATMRxAAL5Pdu,'extremeATMTxAAL5Pdu':extremeATMTxAAL5Pdu,'extremeATMRxAAL5Bytes':extremeATMRxAAL5Bytes,'extremeATMTxAAL5Bytes':extremeATMTxAAL5Bytes,'extremeATMPortStatus':extremeATMPortStatus,'extremeATMVpiVciTable':extremeATMVpiVciTable,'extremeATMVpiVciEntry':extremeATMVpiVciEntry,_J:extremeATMPortNum,_K:extremeATMPvc,'extremeATMVpi':extremeATMVpi,'extremeATMVci':extremeATMVci,'extremeMplsModule':extremeMplsModule,'extremeMplsTlsTable':extremeMplsTlsTable,'extremeMplsTlsEntry':extremeMplsTlsEntry,_L:extremeMplsTlsNum,'extremeMplsTlsName':extremeMplsTlsName,'extremeMplsTlsLocalIpAddr':extremeMplsTlsLocalIpAddr,'extremeMplsTlsPeerIpAddr':extremeMplsTlsPeerIpAddr,'extremeMplsTlsLocalVlanID':extremeMplsTlsLocalVlanID,'extremeMplsTlsLocalVlanName':extremeMplsTlsLocalVlanName,'extremeMplsTlsDynamic':extremeMplsTlsDynamic,'extremeMplsTlsType':extremeMplsTlsType,'extremeMplsTlsVcID':extremeMplsTlsVcID,'extremeMplsTlsLocalGroupID':extremeMplsTlsLocalGroupID,'extremeMplsTlsRemoteGroupID':extremeMplsTlsRemoteGroupID,'extremeMplsTlsIngressVcLabel':extremeMplsTlsIngressVcLabel,'extremeMplsTlsEgressVcLabel':extremeMplsTlsEgressVcLabel,'extremeMplsTlsVcState':extremeMplsTlsVcState,'extremeMplsTlsPacketTx':extremeMplsTlsPacketTx,'extremeMplsTlsPacketRx':extremeMplsTlsPacketRx,'extremeMplsTlsOctetTx':extremeMplsTlsOctetTx,'extremeMplsTlsOctetRx':extremeMplsTlsOctetRx})