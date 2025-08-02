_Q='not-accessible'
_P='anStatusNotApplicable'
_O='anStatusNotAvailable'
_N='anStatusDisabled'
_M='tnRmdIfMauIndex'
_L='Unsigned32'
_K='SnmpAdminString'
_J='tnRmdIfIndex'
_I='Integer32'
_H='tnSysSwitchId'
_G='TROPIC-SYSTEM-MIB'
_F='tnRmdSystemId'
_E='TN-RMD-SYSTEM-MIB'
_D='TN-RMD-IF-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIdOrNone,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','VlanIdOrNone')
IANAifType,InterfaceIndex=mibBuilder.importSymbols('IF-MIB','IANAifType','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
tnRmdSystemId,=mibBuilder.importSymbols(_E,_F)
tnRmdMIBModules,tnRmdObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnRmdMIBModules','tnRmdObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_G,_H)
tnRmdIfMibModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,4,3))
if mibBuilder.loadTexts:tnRmdIfMibModule.setRevisions(('2020-11-13 12:00','2018-02-23 12:00','2016-11-16 00:00','2013-09-24 00:00','2012-11-28 00:00'))
class TnRmdIfOperationalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
class TnRmdAutoNegotiationStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('anStatusError',0),('anStatusConfiguring',1),('anStatusComplete',2),(_N,3),('anStatusParallelDetectFail',4),(_O,254),(_P,255)))
class TnRmdFrameForwardingMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('ffmStoreAndForward',0),('ffmCutThrough',1),('ffmNotApplicable',255)))
class TnRmdDuplexMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,254,255)));namedValues=NamedValues(*(('duplexHalf',0),('duplexFull',1),('duplexAuto',2),('duplexNotAvailable',254),('duplexNotApplicable',255)))
class TnRmdInterfaceSpeed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('ifSpeedTenMbs',0),('ifSpeedHundredMbs',1),('ifSpeedOneGbs',2),('ifSpeedTenGbs',3),('ifSpeedAuto',4),('ifSpeedNotAvailable',254),('ifSpeedNotApplicable',255)))
class TnRmdLoopbackMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,254,255)));namedValues=NamedValues(*(('loopbackDiagnosticMode',0),('loopbackReplaceMode',1),('loopbackSwapMode',2),('loopbackNotAvailable',254),('loopbackNotApplicable',255)))
class TnRmdLptStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('lptStatusUp',1),('lptStatusDown',2),('lptStatusNotApplicable',255)))
class TnRmdMasterSlaveRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,254,255)));namedValues=NamedValues(*(('msMaster',0),('msSlave',1),('msAuto',2),('msNotAvailable',254),('msNotApplicable',255)))
class TnRmdMdixMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,254,255)));namedValues=NamedValues(*(('mdi',0),('mdix',1),('mdiNotAvailable',254),('mdiNotApplicable',255)))
class TnRmdNimDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nimRx',0),('nimTx',1)))
class TnRmdPauseMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,254,255)));namedValues=NamedValues(*(('pauseDisabled',0),('pauseEnabled',1),('pauseTxEnabledRxDisabled',2),('pauseTxDisabledRxEnabled',3),('pauseAuto',4),('pauseNotAvailable',254),('pauseNotApplicable',255)))
class TnRmdTrafficState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('trafficStateEnabled',1),('trafficStateDisabled',2),('trafficStateNotAvailable',254),('trafficStateNotApplicable',255)))
class TnRmdAutoNegotiationConfigState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254,255)));namedValues=NamedValues(*(('anStatusEnabled',1),(_N,2),(_O,254),(_P,255)))
_TnRmdIfObjects_ObjectIdentity=ObjectIdentity
tnRmdIfObjects=_TnRmdIfObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,4,1,3))
_TnRmdIfAttributeTotal_Type=Integer32
_TnRmdIfAttributeTotal_Object=MibScalar
tnRmdIfAttributeTotal=_TnRmdIfAttributeTotal_Object((1,3,6,1,4,1,7483,6,4,1,3,1),_TnRmdIfAttributeTotal_Type())
tnRmdIfAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfAttributeTotal.setStatus(_A)
_TnRmdSystemInterfacesTable_Object=MibTable
tnRmdSystemInterfacesTable=_TnRmdSystemInterfacesTable_Object((1,3,6,1,4,1,7483,6,4,1,3,2))
if mibBuilder.loadTexts:tnRmdSystemInterfacesTable.setStatus(_A)
_TnRmdSystemInterfacesEntry_Object=MibTableRow
tnRmdSystemInterfacesEntry=_TnRmdSystemInterfacesEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,2,1))
tnRmdSystemInterfacesEntry.setIndexNames((0,_G,_H),(0,_E,_F))
if mibBuilder.loadTexts:tnRmdSystemInterfacesEntry.setStatus(_A)
_TnRmdSystemInterfacesFrameForwardingMode_Type=TnRmdFrameForwardingMode
_TnRmdSystemInterfacesFrameForwardingMode_Object=MibTableColumn
tnRmdSystemInterfacesFrameForwardingMode=_TnRmdSystemInterfacesFrameForwardingMode_Object((1,3,6,1,4,1,7483,6,4,1,3,2,1,1),_TnRmdSystemInterfacesFrameForwardingMode_Type())
tnRmdSystemInterfacesFrameForwardingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdSystemInterfacesFrameForwardingMode.setStatus(_A)
_TnRmdSystemLoopbackTable_Object=MibTable
tnRmdSystemLoopbackTable=_TnRmdSystemLoopbackTable_Object((1,3,6,1,4,1,7483,6,4,1,3,3))
if mibBuilder.loadTexts:tnRmdSystemLoopbackTable.setStatus(_A)
_TnRmdSystemLoopbackEntry_Object=MibTableRow
tnRmdSystemLoopbackEntry=_TnRmdSystemLoopbackEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,3,1))
tnRmdSystemLoopbackEntry.setIndexNames((0,_G,_H),(0,_E,_F))
if mibBuilder.loadTexts:tnRmdSystemLoopbackEntry.setStatus(_A)
_TnRmdSystemDefaultLoopbackMode_Type=TnRmdLoopbackMode
_TnRmdSystemDefaultLoopbackMode_Object=MibTableColumn
tnRmdSystemDefaultLoopbackMode=_TnRmdSystemDefaultLoopbackMode_Object((1,3,6,1,4,1,7483,6,4,1,3,3,1,1),_TnRmdSystemDefaultLoopbackMode_Type())
tnRmdSystemDefaultLoopbackMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdSystemDefaultLoopbackMode.setStatus(_A)
_TnRmdIfTable_Object=MibTable
tnRmdIfTable=_TnRmdIfTable_Object((1,3,6,1,4,1,7483,6,4,1,3,4))
if mibBuilder.loadTexts:tnRmdIfTable.setStatus(_A)
_TnRmdIfEntry_Object=MibTableRow
tnRmdIfEntry=_TnRmdIfEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1))
tnRmdIfEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:tnRmdIfEntry.setStatus(_A)
_TnRmdIfIndex_Type=InterfaceIndex
_TnRmdIfIndex_Object=MibTableColumn
tnRmdIfIndex=_TnRmdIfIndex_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,1),_TnRmdIfIndex_Type())
tnRmdIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:tnRmdIfIndex.setStatus(_A)
_TnRmdIfType_Type=IANAifType
_TnRmdIfType_Object=MibTableColumn
tnRmdIfType=_TnRmdIfType_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,2),_TnRmdIfType_Type())
tnRmdIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfType.setStatus(_A)
_TnRmdIfMacAddress_Type=MacAddress
_TnRmdIfMacAddress_Object=MibTableColumn
tnRmdIfMacAddress=_TnRmdIfMacAddress_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,3),_TnRmdIfMacAddress_Type())
tnRmdIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMacAddress.setStatus(_A)
_TnRmdIfTraffic_Type=TnRmdTrafficState
_TnRmdIfTraffic_Object=MibTableColumn
tnRmdIfTraffic=_TnRmdIfTraffic_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,4),_TnRmdIfTraffic_Type())
tnRmdIfTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfTraffic.setStatus(_A)
_TnRmdIfLinkPassThrough_Type=TruthValue
_TnRmdIfLinkPassThrough_Object=MibTableColumn
tnRmdIfLinkPassThrough=_TnRmdIfLinkPassThrough_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,5),_TnRmdIfLinkPassThrough_Type())
tnRmdIfLinkPassThrough.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfLinkPassThrough.setStatus(_A)
_TnRmdIfLinkPassThroughStatus_Type=TnRmdLptStatus
_TnRmdIfLinkPassThroughStatus_Object=MibTableColumn
tnRmdIfLinkPassThroughStatus=_TnRmdIfLinkPassThroughStatus_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,6),_TnRmdIfLinkPassThroughStatus_Type())
tnRmdIfLinkPassThroughStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfLinkPassThroughStatus.setStatus(_A)
_TnRmdIfOperationalState_Type=TnRmdIfOperationalState
_TnRmdIfOperationalState_Object=MibTableColumn
tnRmdIfOperationalState=_TnRmdIfOperationalState_Object((1,3,6,1,4,1,7483,6,4,1,3,4,1,7),_TnRmdIfOperationalState_Type())
tnRmdIfOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfOperationalState.setStatus(_A)
_TnRmdIfMauTable_Object=MibTable
tnRmdIfMauTable=_TnRmdIfMauTable_Object((1,3,6,1,4,1,7483,6,4,1,3,5))
if mibBuilder.loadTexts:tnRmdIfMauTable.setStatus(_A)
_TnRmdIfMauEntry_Object=MibTableRow
tnRmdIfMauEntry=_TnRmdIfMauEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1))
tnRmdIfMauEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J),(0,_D,_M))
if mibBuilder.loadTexts:tnRmdIfMauEntry.setStatus(_A)
class _TnRmdIfMauIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TnRmdIfMauIndex_Type.__name__=_I
_TnRmdIfMauIndex_Object=MibTableColumn
tnRmdIfMauIndex=_TnRmdIfMauIndex_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,1),_TnRmdIfMauIndex_Type())
tnRmdIfMauIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:tnRmdIfMauIndex.setStatus(_A)
_TnRmdIfMauAutoNegotiation_Type=TnRmdAutoNegotiationConfigState
_TnRmdIfMauAutoNegotiation_Object=MibTableColumn
tnRmdIfMauAutoNegotiation=_TnRmdIfMauAutoNegotiation_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,2),_TnRmdIfMauAutoNegotiation_Type())
tnRmdIfMauAutoNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauAutoNegotiation.setStatus(_A)
_TnRmdIfMauAutoNegotiationStatus_Type=TnRmdAutoNegotiationStatus
_TnRmdIfMauAutoNegotiationStatus_Object=MibTableColumn
tnRmdIfMauAutoNegotiationStatus=_TnRmdIfMauAutoNegotiationStatus_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,3),_TnRmdIfMauAutoNegotiationStatus_Type())
tnRmdIfMauAutoNegotiationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauAutoNegotiationStatus.setStatus(_A)
_TnRmdIfMauAutoNegotiationFallback_Type=TnRmdAutoNegotiationConfigState
_TnRmdIfMauAutoNegotiationFallback_Object=MibTableColumn
tnRmdIfMauAutoNegotiationFallback=_TnRmdIfMauAutoNegotiationFallback_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,4),_TnRmdIfMauAutoNegotiationFallback_Type())
tnRmdIfMauAutoNegotiationFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauAutoNegotiationFallback.setStatus(_A)
_TnRmdIfMauProvisionedSpeed_Type=TnRmdInterfaceSpeed
_TnRmdIfMauProvisionedSpeed_Object=MibTableColumn
tnRmdIfMauProvisionedSpeed=_TnRmdIfMauProvisionedSpeed_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,5),_TnRmdIfMauProvisionedSpeed_Type())
tnRmdIfMauProvisionedSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauProvisionedSpeed.setStatus(_A)
_TnRmdIfMauProvisionedDuplexMode_Type=TnRmdDuplexMode
_TnRmdIfMauProvisionedDuplexMode_Object=MibTableColumn
tnRmdIfMauProvisionedDuplexMode=_TnRmdIfMauProvisionedDuplexMode_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,6),_TnRmdIfMauProvisionedDuplexMode_Type())
tnRmdIfMauProvisionedDuplexMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauProvisionedDuplexMode.setStatus(_A)
_TnRmdIfMauProvisionedPauseMode_Type=TnRmdPauseMode
_TnRmdIfMauProvisionedPauseMode_Object=MibTableColumn
tnRmdIfMauProvisionedPauseMode=_TnRmdIfMauProvisionedPauseMode_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,7),_TnRmdIfMauProvisionedPauseMode_Type())
tnRmdIfMauProvisionedPauseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauProvisionedPauseMode.setStatus(_A)
_TnRmdIfMauProvisionedMasterSlaveRole_Type=TnRmdMasterSlaveRole
_TnRmdIfMauProvisionedMasterSlaveRole_Object=MibTableColumn
tnRmdIfMauProvisionedMasterSlaveRole=_TnRmdIfMauProvisionedMasterSlaveRole_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,8),_TnRmdIfMauProvisionedMasterSlaveRole_Type())
tnRmdIfMauProvisionedMasterSlaveRole.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfMauProvisionedMasterSlaveRole.setStatus(_A)
_TnRmdIfMauActualSpeed_Type=TnRmdInterfaceSpeed
_TnRmdIfMauActualSpeed_Object=MibTableColumn
tnRmdIfMauActualSpeed=_TnRmdIfMauActualSpeed_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,9),_TnRmdIfMauActualSpeed_Type())
tnRmdIfMauActualSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauActualSpeed.setStatus(_A)
_TnRmdIfMauActualDuplexMode_Type=TnRmdDuplexMode
_TnRmdIfMauActualDuplexMode_Object=MibTableColumn
tnRmdIfMauActualDuplexMode=_TnRmdIfMauActualDuplexMode_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,10),_TnRmdIfMauActualDuplexMode_Type())
tnRmdIfMauActualDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauActualDuplexMode.setStatus(_A)
_TnRmdIfMauActualPauseMode_Type=TnRmdPauseMode
_TnRmdIfMauActualPauseMode_Object=MibTableColumn
tnRmdIfMauActualPauseMode=_TnRmdIfMauActualPauseMode_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,11),_TnRmdIfMauActualPauseMode_Type())
tnRmdIfMauActualPauseMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauActualPauseMode.setStatus(_A)
_TnRmdIfMauActualMasterSlaveRole_Type=TnRmdMasterSlaveRole
_TnRmdIfMauActualMasterSlaveRole_Object=MibTableColumn
tnRmdIfMauActualMasterSlaveRole=_TnRmdIfMauActualMasterSlaveRole_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,12),_TnRmdIfMauActualMasterSlaveRole_Type())
tnRmdIfMauActualMasterSlaveRole.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauActualMasterSlaveRole.setStatus(_A)
_TnRmdIfMauMdixMode_Type=TnRmdMdixMode
_TnRmdIfMauMdixMode_Object=MibTableColumn
tnRmdIfMauMdixMode=_TnRmdIfMauMdixMode_Object((1,3,6,1,4,1,7483,6,4,1,3,5,1,13),_TnRmdIfMauMdixMode_Type())
tnRmdIfMauMdixMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMauMdixMode.setStatus(_A)
_TnRmdIfMsaTable_Object=MibTable
tnRmdIfMsaTable=_TnRmdIfMsaTable_Object((1,3,6,1,4,1,7483,6,4,1,3,6))
if mibBuilder.loadTexts:tnRmdIfMsaTable.setStatus(_A)
_TnRmdIfMsaEntry_Object=MibTableRow
tnRmdIfMsaEntry=_TnRmdIfMsaEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1))
tnRmdIfMsaEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J),(0,_D,_M))
if mibBuilder.loadTexts:tnRmdIfMsaEntry.setStatus(_A)
class _TnRmdIfMsaModuleVendorSerNo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_TnRmdIfMsaModuleVendorSerNo_Type.__name__=_K
_TnRmdIfMsaModuleVendorSerNo_Object=MibTableColumn
tnRmdIfMsaModuleVendorSerNo=_TnRmdIfMsaModuleVendorSerNo_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,1),_TnRmdIfMsaModuleVendorSerNo_Type())
tnRmdIfMsaModuleVendorSerNo.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaModuleVendorSerNo.setStatus(_A)
class _TnRmdIfMsaModuleVendor_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TnRmdIfMsaModuleVendor_Type.__name__=_K
_TnRmdIfMsaModuleVendor_Object=MibTableColumn
tnRmdIfMsaModuleVendor=_TnRmdIfMsaModuleVendor_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,2),_TnRmdIfMsaModuleVendor_Type())
tnRmdIfMsaModuleVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaModuleVendor.setStatus(_A)
_TnRmdIfMsaWavelength_Type=Unsigned32
_TnRmdIfMsaWavelength_Object=MibTableColumn
tnRmdIfMsaWavelength=_TnRmdIfMsaWavelength_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,3),_TnRmdIfMsaWavelength_Type())
tnRmdIfMsaWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaWavelength.setStatus(_A)
_TnRmdIfMsaModuleType_Type=SnmpAdminString
_TnRmdIfMsaModuleType_Object=MibTableColumn
tnRmdIfMsaModuleType=_TnRmdIfMsaModuleType_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,4),_TnRmdIfMsaModuleType_Type())
tnRmdIfMsaModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaModuleType.setStatus(_A)
_TnRmdIfMsaCLEI_Type=SnmpAdminString
_TnRmdIfMsaCLEI_Object=MibTableColumn
tnRmdIfMsaCLEI=_TnRmdIfMsaCLEI_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,5),_TnRmdIfMsaCLEI_Type())
tnRmdIfMsaCLEI.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaCLEI.setStatus(_A)
_TnRmdIfMsaUnitPartNum_Type=SnmpAdminString
_TnRmdIfMsaUnitPartNum_Object=MibTableColumn
tnRmdIfMsaUnitPartNum=_TnRmdIfMsaUnitPartNum_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,6),_TnRmdIfMsaUnitPartNum_Type())
tnRmdIfMsaUnitPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaUnitPartNum.setStatus(_A)
_TnRmdIfMsaSWPartNum_Type=SnmpAdminString
_TnRmdIfMsaSWPartNum_Object=MibTableColumn
tnRmdIfMsaSWPartNum=_TnRmdIfMsaSWPartNum_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,7),_TnRmdIfMsaSWPartNum_Type())
tnRmdIfMsaSWPartNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaSWPartNum.setStatus(_A)
_TnRmdIfMsaFactoryID_Type=SnmpAdminString
_TnRmdIfMsaFactoryID_Object=MibTableColumn
tnRmdIfMsaFactoryID=_TnRmdIfMsaFactoryID_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,8),_TnRmdIfMsaFactoryID_Type())
tnRmdIfMsaFactoryID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaFactoryID.setStatus(_A)
_TnRmdIfMsaDate_Type=SnmpAdminString
_TnRmdIfMsaDate_Object=MibTableColumn
tnRmdIfMsaDate=_TnRmdIfMsaDate_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,9),_TnRmdIfMsaDate_Type())
tnRmdIfMsaDate.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaDate.setStatus(_A)
_TnRmdIfMsaExtraData_Type=SnmpAdminString
_TnRmdIfMsaExtraData_Object=MibTableColumn
tnRmdIfMsaExtraData=_TnRmdIfMsaExtraData_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,10),_TnRmdIfMsaExtraData_Type())
tnRmdIfMsaExtraData.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaExtraData.setStatus(_A)
_TnRmdIfMsaMaximumCaseTemperature_Type=Integer32
_TnRmdIfMsaMaximumCaseTemperature_Object=MibTableColumn
tnRmdIfMsaMaximumCaseTemperature=_TnRmdIfMsaMaximumCaseTemperature_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,11),_TnRmdIfMsaMaximumCaseTemperature_Type())
tnRmdIfMsaMaximumCaseTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaMaximumCaseTemperature.setStatus(_A)
class _TnRmdIfMsaInterchangeabilityMarking_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_TnRmdIfMsaInterchangeabilityMarking_Type.__name__=_K
_TnRmdIfMsaInterchangeabilityMarking_Object=MibTableColumn
tnRmdIfMsaInterchangeabilityMarking=_TnRmdIfMsaInterchangeabilityMarking_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,12),_TnRmdIfMsaInterchangeabilityMarking_Type())
tnRmdIfMsaInterchangeabilityMarking.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaInterchangeabilityMarking.setStatus(_A)
class _TnRmdIfMsaAcronymCode_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_TnRmdIfMsaAcronymCode_Type.__name__=_K
_TnRmdIfMsaAcronymCode_Object=MibTableColumn
tnRmdIfMsaAcronymCode=_TnRmdIfMsaAcronymCode_Object((1,3,6,1,4,1,7483,6,4,1,3,6,1,13),_TnRmdIfMsaAcronymCode_Type())
tnRmdIfMsaAcronymCode.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfMsaAcronymCode.setStatus(_A)
_TnRmdIfDdmTable_Object=MibTable
tnRmdIfDdmTable=_TnRmdIfDdmTable_Object((1,3,6,1,4,1,7483,6,4,1,3,7))
if mibBuilder.loadTexts:tnRmdIfDdmTable.setStatus(_A)
_TnRmdIfDdmEntry_Object=MibTableRow
tnRmdIfDdmEntry=_TnRmdIfDdmEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1))
tnRmdIfDdmEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J),(0,_D,_M))
if mibBuilder.loadTexts:tnRmdIfDdmEntry.setStatus(_A)
_TnRmdIfDdmTemperature_Type=Integer32
_TnRmdIfDdmTemperature_Object=MibTableColumn
tnRmdIfDdmTemperature=_TnRmdIfDdmTemperature_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,1),_TnRmdIfDdmTemperature_Type())
tnRmdIfDdmTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTemperature.setStatus(_A)
_TnRmdIfDdmTempLowWarning_Type=Integer32
_TnRmdIfDdmTempLowWarning_Object=MibTableColumn
tnRmdIfDdmTempLowWarning=_TnRmdIfDdmTempLowWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,2),_TnRmdIfDdmTempLowWarning_Type())
tnRmdIfDdmTempLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTempLowWarning.setStatus(_A)
_TnRmdIfDdmTempLowAlarm_Type=Integer32
_TnRmdIfDdmTempLowAlarm_Object=MibTableColumn
tnRmdIfDdmTempLowAlarm=_TnRmdIfDdmTempLowAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,3),_TnRmdIfDdmTempLowAlarm_Type())
tnRmdIfDdmTempLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTempLowAlarm.setStatus(_A)
_TnRmdIfDdmTempHiWarning_Type=Integer32
_TnRmdIfDdmTempHiWarning_Object=MibTableColumn
tnRmdIfDdmTempHiWarning=_TnRmdIfDdmTempHiWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,4),_TnRmdIfDdmTempHiWarning_Type())
tnRmdIfDdmTempHiWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTempHiWarning.setStatus(_A)
_TnRmdIfDdmTempHiAlarm_Type=Integer32
_TnRmdIfDdmTempHiAlarm_Object=MibTableColumn
tnRmdIfDdmTempHiAlarm=_TnRmdIfDdmTempHiAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,5),_TnRmdIfDdmTempHiAlarm_Type())
tnRmdIfDdmTempHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTempHiAlarm.setStatus(_A)
_TnRmdIfDdmSupplyVoltage_Type=Integer32
_TnRmdIfDdmSupplyVoltage_Object=MibTableColumn
tnRmdIfDdmSupplyVoltage=_TnRmdIfDdmSupplyVoltage_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,6),_TnRmdIfDdmSupplyVoltage_Type())
tnRmdIfDdmSupplyVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmSupplyVoltage.setStatus(_A)
_TnRmdIfDdmSupplyVoltageLowWarning_Type=Integer32
_TnRmdIfDdmSupplyVoltageLowWarning_Object=MibTableColumn
tnRmdIfDdmSupplyVoltageLowWarning=_TnRmdIfDdmSupplyVoltageLowWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,7),_TnRmdIfDdmSupplyVoltageLowWarning_Type())
tnRmdIfDdmSupplyVoltageLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmSupplyVoltageLowWarning.setStatus(_A)
_TnRmdIfDdmSupplyVoltageLowAlarm_Type=Integer32
_TnRmdIfDdmSupplyVoltageLowAlarm_Object=MibTableColumn
tnRmdIfDdmSupplyVoltageLowAlarm=_TnRmdIfDdmSupplyVoltageLowAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,8),_TnRmdIfDdmSupplyVoltageLowAlarm_Type())
tnRmdIfDdmSupplyVoltageLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmSupplyVoltageLowAlarm.setStatus(_A)
_TnRmdIfDdmSupplyVoltageHiWarning_Type=Integer32
_TnRmdIfDdmSupplyVoltageHiWarning_Object=MibTableColumn
tnRmdIfDdmSupplyVoltageHiWarning=_TnRmdIfDdmSupplyVoltageHiWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,9),_TnRmdIfDdmSupplyVoltageHiWarning_Type())
tnRmdIfDdmSupplyVoltageHiWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmSupplyVoltageHiWarning.setStatus(_A)
_TnRmdIfDdmSupplyVoltageHiAlarm_Type=Integer32
_TnRmdIfDdmSupplyVoltageHiAlarm_Object=MibTableColumn
tnRmdIfDdmSupplyVoltageHiAlarm=_TnRmdIfDdmSupplyVoltageHiAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,10),_TnRmdIfDdmSupplyVoltageHiAlarm_Type())
tnRmdIfDdmSupplyVoltageHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmSupplyVoltageHiAlarm.setStatus(_A)
_TnRmdIfDdmTxBiasCurrent_Type=Integer32
_TnRmdIfDdmTxBiasCurrent_Object=MibTableColumn
tnRmdIfDdmTxBiasCurrent=_TnRmdIfDdmTxBiasCurrent_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,11),_TnRmdIfDdmTxBiasCurrent_Type())
tnRmdIfDdmTxBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxBiasCurrent.setStatus(_A)
_TnRmdIfDdmTxBiasCurrentLowWarning_Type=Integer32
_TnRmdIfDdmTxBiasCurrentLowWarning_Object=MibTableColumn
tnRmdIfDdmTxBiasCurrentLowWarning=_TnRmdIfDdmTxBiasCurrentLowWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,12),_TnRmdIfDdmTxBiasCurrentLowWarning_Type())
tnRmdIfDdmTxBiasCurrentLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxBiasCurrentLowWarning.setStatus(_A)
_TnRmdIfDdmTxBiasCurrentLowAlarm_Type=Integer32
_TnRmdIfDdmTxBiasCurrentLowAlarm_Object=MibTableColumn
tnRmdIfDdmTxBiasCurrentLowAlarm=_TnRmdIfDdmTxBiasCurrentLowAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,13),_TnRmdIfDdmTxBiasCurrentLowAlarm_Type())
tnRmdIfDdmTxBiasCurrentLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxBiasCurrentLowAlarm.setStatus(_A)
_TnRmdIfDdmTxBiasCurrentHiWarning_Type=Integer32
_TnRmdIfDdmTxBiasCurrentHiWarning_Object=MibTableColumn
tnRmdIfDdmTxBiasCurrentHiWarning=_TnRmdIfDdmTxBiasCurrentHiWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,14),_TnRmdIfDdmTxBiasCurrentHiWarning_Type())
tnRmdIfDdmTxBiasCurrentHiWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxBiasCurrentHiWarning.setStatus(_A)
_TnRmdIfDdmTxBiasCurrentHiAlarm_Type=Integer32
_TnRmdIfDdmTxBiasCurrentHiAlarm_Object=MibTableColumn
tnRmdIfDdmTxBiasCurrentHiAlarm=_TnRmdIfDdmTxBiasCurrentHiAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,15),_TnRmdIfDdmTxBiasCurrentHiAlarm_Type())
tnRmdIfDdmTxBiasCurrentHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxBiasCurrentHiAlarm.setStatus(_A)
_TnRmdIfDdmTxOutputPower_Type=Integer32
_TnRmdIfDdmTxOutputPower_Object=MibTableColumn
tnRmdIfDdmTxOutputPower=_TnRmdIfDdmTxOutputPower_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,16),_TnRmdIfDdmTxOutputPower_Type())
tnRmdIfDdmTxOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxOutputPower.setStatus(_A)
_TnRmdIfDdmTxOutputPowerLowWarning_Type=Integer32
_TnRmdIfDdmTxOutputPowerLowWarning_Object=MibTableColumn
tnRmdIfDdmTxOutputPowerLowWarning=_TnRmdIfDdmTxOutputPowerLowWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,17),_TnRmdIfDdmTxOutputPowerLowWarning_Type())
tnRmdIfDdmTxOutputPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxOutputPowerLowWarning.setStatus(_A)
_TnRmdIfDdmTxOutputPowerLowAlarm_Type=Integer32
_TnRmdIfDdmTxOutputPowerLowAlarm_Object=MibTableColumn
tnRmdIfDdmTxOutputPowerLowAlarm=_TnRmdIfDdmTxOutputPowerLowAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,18),_TnRmdIfDdmTxOutputPowerLowAlarm_Type())
tnRmdIfDdmTxOutputPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxOutputPowerLowAlarm.setStatus(_A)
_TnRmdIfDdmTxOutputPowerHiWarning_Type=Integer32
_TnRmdIfDdmTxOutputPowerHiWarning_Object=MibTableColumn
tnRmdIfDdmTxOutputPowerHiWarning=_TnRmdIfDdmTxOutputPowerHiWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,19),_TnRmdIfDdmTxOutputPowerHiWarning_Type())
tnRmdIfDdmTxOutputPowerHiWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxOutputPowerHiWarning.setStatus(_A)
_TnRmdIfDdmTxOutputPowerHiAlarm_Type=Integer32
_TnRmdIfDdmTxOutputPowerHiAlarm_Object=MibTableColumn
tnRmdIfDdmTxOutputPowerHiAlarm=_TnRmdIfDdmTxOutputPowerHiAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,20),_TnRmdIfDdmTxOutputPowerHiAlarm_Type())
tnRmdIfDdmTxOutputPowerHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmTxOutputPowerHiAlarm.setStatus(_A)
_TnRmdIfDdmRxOpticalPower_Type=Integer32
_TnRmdIfDdmRxOpticalPower_Object=MibTableColumn
tnRmdIfDdmRxOpticalPower=_TnRmdIfDdmRxOpticalPower_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,21),_TnRmdIfDdmRxOpticalPower_Type())
tnRmdIfDdmRxOpticalPower.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPower.setStatus(_A)
_TnRmdIfDdmRxOpticalPowerLowWarning_Type=Integer32
_TnRmdIfDdmRxOpticalPowerLowWarning_Object=MibTableColumn
tnRmdIfDdmRxOpticalPowerLowWarning=_TnRmdIfDdmRxOpticalPowerLowWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,22),_TnRmdIfDdmRxOpticalPowerLowWarning_Type())
tnRmdIfDdmRxOpticalPowerLowWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPowerLowWarning.setStatus(_A)
_TnRmdIfDdmRxOpticalPowerLowAlarm_Type=Integer32
_TnRmdIfDdmRxOpticalPowerLowAlarm_Object=MibTableColumn
tnRmdIfDdmRxOpticalPowerLowAlarm=_TnRmdIfDdmRxOpticalPowerLowAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,23),_TnRmdIfDdmRxOpticalPowerLowAlarm_Type())
tnRmdIfDdmRxOpticalPowerLowAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPowerLowAlarm.setStatus(_A)
_TnRmdIfDdmRxOpticalPowerHiWarning_Type=Integer32
_TnRmdIfDdmRxOpticalPowerHiWarning_Object=MibTableColumn
tnRmdIfDdmRxOpticalPowerHiWarning=_TnRmdIfDdmRxOpticalPowerHiWarning_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,24),_TnRmdIfDdmRxOpticalPowerHiWarning_Type())
tnRmdIfDdmRxOpticalPowerHiWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPowerHiWarning.setStatus(_A)
_TnRmdIfDdmRxOpticalPowerHiAlarm_Type=Integer32
_TnRmdIfDdmRxOpticalPowerHiAlarm_Object=MibTableColumn
tnRmdIfDdmRxOpticalPowerHiAlarm=_TnRmdIfDdmRxOpticalPowerHiAlarm_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,25),_TnRmdIfDdmRxOpticalPowerHiAlarm_Type())
tnRmdIfDdmRxOpticalPowerHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPowerHiAlarm.setStatus(_A)
class _TnRmdIfDdmRxOpticalPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('oma',0),('average',1)))
_TnRmdIfDdmRxOpticalPowerType_Type.__name__=_I
_TnRmdIfDdmRxOpticalPowerType_Object=MibTableColumn
tnRmdIfDdmRxOpticalPowerType=_TnRmdIfDdmRxOpticalPowerType_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,26),_TnRmdIfDdmRxOpticalPowerType_Type())
tnRmdIfDdmRxOpticalPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmRxOpticalPowerType.setStatus(_A)
_TnRmdIfDdmExternallyCalibrated_Type=TruthValue
_TnRmdIfDdmExternallyCalibrated_Object=MibTableColumn
tnRmdIfDdmExternallyCalibrated=_TnRmdIfDdmExternallyCalibrated_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,27),_TnRmdIfDdmExternallyCalibrated_Type())
tnRmdIfDdmExternallyCalibrated.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExternallyCalibrated.setStatus(_A)
_TnRmdIfDdmExtCalRxPower4_Type=Unsigned32
_TnRmdIfDdmExtCalRxPower4_Object=MibTableColumn
tnRmdIfDdmExtCalRxPower4=_TnRmdIfDdmExtCalRxPower4_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,28),_TnRmdIfDdmExtCalRxPower4_Type())
tnRmdIfDdmExtCalRxPower4.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalRxPower4.setStatus(_A)
_TnRmdIfDdmExtCalRxPower3_Type=Unsigned32
_TnRmdIfDdmExtCalRxPower3_Object=MibTableColumn
tnRmdIfDdmExtCalRxPower3=_TnRmdIfDdmExtCalRxPower3_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,29),_TnRmdIfDdmExtCalRxPower3_Type())
tnRmdIfDdmExtCalRxPower3.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalRxPower3.setStatus(_A)
_TnRmdIfDdmExtCalRxPower2_Type=Unsigned32
_TnRmdIfDdmExtCalRxPower2_Object=MibTableColumn
tnRmdIfDdmExtCalRxPower2=_TnRmdIfDdmExtCalRxPower2_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,30),_TnRmdIfDdmExtCalRxPower2_Type())
tnRmdIfDdmExtCalRxPower2.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalRxPower2.setStatus(_A)
_TnRmdIfDdmExtCalRxPower1_Type=Unsigned32
_TnRmdIfDdmExtCalRxPower1_Object=MibTableColumn
tnRmdIfDdmExtCalRxPower1=_TnRmdIfDdmExtCalRxPower1_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,31),_TnRmdIfDdmExtCalRxPower1_Type())
tnRmdIfDdmExtCalRxPower1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalRxPower1.setStatus(_A)
_TnRmdIfDdmExtCalRxPower0_Type=Unsigned32
_TnRmdIfDdmExtCalRxPower0_Object=MibTableColumn
tnRmdIfDdmExtCalRxPower0=_TnRmdIfDdmExtCalRxPower0_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,32),_TnRmdIfDdmExtCalRxPower0_Type())
tnRmdIfDdmExtCalRxPower0.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalRxPower0.setStatus(_A)
class _TnRmdIfDdmExtCalTxLaserBiasSlope_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnRmdIfDdmExtCalTxLaserBiasSlope_Type.__name__=_L
_TnRmdIfDdmExtCalTxLaserBiasSlope_Object=MibTableColumn
tnRmdIfDdmExtCalTxLaserBiasSlope=_TnRmdIfDdmExtCalTxLaserBiasSlope_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,33),_TnRmdIfDdmExtCalTxLaserBiasSlope_Type())
tnRmdIfDdmExtCalTxLaserBiasSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTxLaserBiasSlope.setStatus(_A)
class _TnRmdIfDdmExtCalTxLaserBiasOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32768))
_TnRmdIfDdmExtCalTxLaserBiasOffset_Type.__name__=_I
_TnRmdIfDdmExtCalTxLaserBiasOffset_Object=MibTableColumn
tnRmdIfDdmExtCalTxLaserBiasOffset=_TnRmdIfDdmExtCalTxLaserBiasOffset_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,34),_TnRmdIfDdmExtCalTxLaserBiasOffset_Type())
tnRmdIfDdmExtCalTxLaserBiasOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTxLaserBiasOffset.setStatus(_A)
class _TnRmdIfDdmExtCalTxPowerSlope_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnRmdIfDdmExtCalTxPowerSlope_Type.__name__=_L
_TnRmdIfDdmExtCalTxPowerSlope_Object=MibTableColumn
tnRmdIfDdmExtCalTxPowerSlope=_TnRmdIfDdmExtCalTxPowerSlope_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,35),_TnRmdIfDdmExtCalTxPowerSlope_Type())
tnRmdIfDdmExtCalTxPowerSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTxPowerSlope.setStatus(_A)
class _TnRmdIfDdmExtCalTxPowerOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32768))
_TnRmdIfDdmExtCalTxPowerOffset_Type.__name__=_I
_TnRmdIfDdmExtCalTxPowerOffset_Object=MibTableColumn
tnRmdIfDdmExtCalTxPowerOffset=_TnRmdIfDdmExtCalTxPowerOffset_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,36),_TnRmdIfDdmExtCalTxPowerOffset_Type())
tnRmdIfDdmExtCalTxPowerOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTxPowerOffset.setStatus(_A)
class _TnRmdIfDdmExtCalTemperatureSlope_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnRmdIfDdmExtCalTemperatureSlope_Type.__name__=_L
_TnRmdIfDdmExtCalTemperatureSlope_Object=MibTableColumn
tnRmdIfDdmExtCalTemperatureSlope=_TnRmdIfDdmExtCalTemperatureSlope_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,37),_TnRmdIfDdmExtCalTemperatureSlope_Type())
tnRmdIfDdmExtCalTemperatureSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTemperatureSlope.setStatus(_A)
class _TnRmdIfDdmExtCalTemperatureOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32768))
_TnRmdIfDdmExtCalTemperatureOffset_Type.__name__=_I
_TnRmdIfDdmExtCalTemperatureOffset_Object=MibTableColumn
tnRmdIfDdmExtCalTemperatureOffset=_TnRmdIfDdmExtCalTemperatureOffset_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,38),_TnRmdIfDdmExtCalTemperatureOffset_Type())
tnRmdIfDdmExtCalTemperatureOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalTemperatureOffset.setStatus(_A)
class _TnRmdIfDdmExtCalVoltageSlope_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TnRmdIfDdmExtCalVoltageSlope_Type.__name__=_L
_TnRmdIfDdmExtCalVoltageSlope_Object=MibTableColumn
tnRmdIfDdmExtCalVoltageSlope=_TnRmdIfDdmExtCalVoltageSlope_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,39),_TnRmdIfDdmExtCalVoltageSlope_Type())
tnRmdIfDdmExtCalVoltageSlope.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalVoltageSlope.setStatus(_A)
class _TnRmdIfDdmExtCalVoltageOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32768))
_TnRmdIfDdmExtCalVoltageOffset_Type.__name__=_I
_TnRmdIfDdmExtCalVoltageOffset_Object=MibTableColumn
tnRmdIfDdmExtCalVoltageOffset=_TnRmdIfDdmExtCalVoltageOffset_Object((1,3,6,1,4,1,7483,6,4,1,3,7,1,40),_TnRmdIfDdmExtCalVoltageOffset_Type())
tnRmdIfDdmExtCalVoltageOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfDdmExtCalVoltageOffset.setStatus(_A)
_TnRmdIfLoopbackTable_Object=MibTable
tnRmdIfLoopbackTable=_TnRmdIfLoopbackTable_Object((1,3,6,1,4,1,7483,6,4,1,3,8))
if mibBuilder.loadTexts:tnRmdIfLoopbackTable.setStatus(_A)
_TnRmdIfLoopbackEntry_Object=MibTableRow
tnRmdIfLoopbackEntry=_TnRmdIfLoopbackEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,8,1))
tnRmdIfLoopbackEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:tnRmdIfLoopbackEntry.setStatus(_A)
_TnRmdIfLoopbackIn_Type=TruthValue
_TnRmdIfLoopbackIn_Object=MibTableColumn
tnRmdIfLoopbackIn=_TnRmdIfLoopbackIn_Object((1,3,6,1,4,1,7483,6,4,1,3,8,1,1),_TnRmdIfLoopbackIn_Type())
tnRmdIfLoopbackIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfLoopbackIn.setStatus(_A)
_TnRmdIfLoopbackOut_Type=TruthValue
_TnRmdIfLoopbackOut_Object=MibTableColumn
tnRmdIfLoopbackOut=_TnRmdIfLoopbackOut_Object((1,3,6,1,4,1,7483,6,4,1,3,8,1,2),_TnRmdIfLoopbackOut_Type())
tnRmdIfLoopbackOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfLoopbackOut.setStatus(_A)
_TnRmdIfEvcLoopBack_Type=TruthValue
_TnRmdIfEvcLoopBack_Object=MibTableColumn
tnRmdIfEvcLoopBack=_TnRmdIfEvcLoopBack_Object((1,3,6,1,4,1,7483,6,4,1,3,8,1,3),_TnRmdIfEvcLoopBack_Type())
tnRmdIfEvcLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfEvcLoopBack.setStatus(_A)
_TnRmdIfEvcLoopBackVlanId_Type=VlanIdOrNone
_TnRmdIfEvcLoopBackVlanId_Object=MibTableColumn
tnRmdIfEvcLoopBackVlanId=_TnRmdIfEvcLoopBackVlanId_Object((1,3,6,1,4,1,7483,6,4,1,3,8,1,4),_TnRmdIfEvcLoopBackVlanId_Type())
tnRmdIfEvcLoopBackVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfEvcLoopBackVlanId.setStatus(_A)
_TnRmdIfCountersTable_Object=MibTable
tnRmdIfCountersTable=_TnRmdIfCountersTable_Object((1,3,6,1,4,1,7483,6,4,1,3,10))
if mibBuilder.loadTexts:tnRmdIfCountersTable.setStatus(_A)
_TnRmdIfCountersEntry_Object=MibTableRow
tnRmdIfCountersEntry=_TnRmdIfCountersEntry_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1))
tnRmdIfCountersEntry.setIndexNames((0,_G,_H),(0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:tnRmdIfCountersEntry.setStatus(_A)
_TnRmdIfCountersRxNrCorrectFrames_Type=Counter64
_TnRmdIfCountersRxNrCorrectFrames_Object=MibTableColumn
tnRmdIfCountersRxNrCorrectFrames=_TnRmdIfCountersRxNrCorrectFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,1),_TnRmdIfCountersRxNrCorrectFrames_Type())
tnRmdIfCountersRxNrCorrectFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrCorrectFrames.setStatus(_A)
_TnRmdIfCountersRxNrCorrectBytes_Type=Counter64
_TnRmdIfCountersRxNrCorrectBytes_Object=MibTableColumn
tnRmdIfCountersRxNrCorrectBytes=_TnRmdIfCountersRxNrCorrectBytes_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,2),_TnRmdIfCountersRxNrCorrectBytes_Type())
tnRmdIfCountersRxNrCorrectBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrCorrectBytes.setStatus(_A)
_TnRmdIfCountersRxNrErroredFcsFrames_Type=Counter64
_TnRmdIfCountersRxNrErroredFcsFrames_Object=MibTableColumn
tnRmdIfCountersRxNrErroredFcsFrames=_TnRmdIfCountersRxNrErroredFcsFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,3),_TnRmdIfCountersRxNrErroredFcsFrames_Type())
tnRmdIfCountersRxNrErroredFcsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrErroredFcsFrames.setStatus(_A)
_TnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames_Type=Counter64
_TnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames_Object=MibTableColumn
tnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames=_TnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,4),_TnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames_Type())
tnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames.setStatus(_A)
_TnRmdIfCountersRxNrDiscardedFrames_Type=Counter64
_TnRmdIfCountersRxNrDiscardedFrames_Object=MibTableColumn
tnRmdIfCountersRxNrDiscardedFrames=_TnRmdIfCountersRxNrDiscardedFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,5),_TnRmdIfCountersRxNrDiscardedFrames_Type())
tnRmdIfCountersRxNrDiscardedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrDiscardedFrames.setStatus(_A)
_TnRmdIfCountersRxNrDroppedQueueOverflowFrames_Type=Counter64
_TnRmdIfCountersRxNrDroppedQueueOverflowFrames_Object=MibTableColumn
tnRmdIfCountersRxNrDroppedQueueOverflowFrames=_TnRmdIfCountersRxNrDroppedQueueOverflowFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,6),_TnRmdIfCountersRxNrDroppedQueueOverflowFrames_Type())
tnRmdIfCountersRxNrDroppedQueueOverflowFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersRxNrDroppedQueueOverflowFrames.setStatus(_A)
_TnRmdIfCountersTxNrFrames_Type=Counter64
_TnRmdIfCountersTxNrFrames_Object=MibTableColumn
tnRmdIfCountersTxNrFrames=_TnRmdIfCountersTxNrFrames_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,7),_TnRmdIfCountersTxNrFrames_Type())
tnRmdIfCountersTxNrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersTxNrFrames.setStatus(_A)
_TnRmdIfCountersTxNrBytes_Type=Counter64
_TnRmdIfCountersTxNrBytes_Object=MibTableColumn
tnRmdIfCountersTxNrBytes=_TnRmdIfCountersTxNrBytes_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,8),_TnRmdIfCountersTxNrBytes_Type())
tnRmdIfCountersTxNrBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRmdIfCountersTxNrBytes.setStatus(_A)
_TnRmdIfCountersReset_Type=TruthValue
_TnRmdIfCountersReset_Object=MibTableColumn
tnRmdIfCountersReset=_TnRmdIfCountersReset_Object((1,3,6,1,4,1,7483,6,4,1,3,10,1,9),_TnRmdIfCountersReset_Type())
tnRmdIfCountersReset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnRmdIfCountersReset.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TnRmdIfOperationalState':TnRmdIfOperationalState,'TnRmdAutoNegotiationStatus':TnRmdAutoNegotiationStatus,'TnRmdFrameForwardingMode':TnRmdFrameForwardingMode,'TnRmdDuplexMode':TnRmdDuplexMode,'TnRmdInterfaceSpeed':TnRmdInterfaceSpeed,'TnRmdLoopbackMode':TnRmdLoopbackMode,'TnRmdLptStatus':TnRmdLptStatus,'TnRmdMasterSlaveRole':TnRmdMasterSlaveRole,'TnRmdMdixMode':TnRmdMdixMode,'TnRmdNimDirection':TnRmdNimDirection,'TnRmdPauseMode':TnRmdPauseMode,'TnRmdTrafficState':TnRmdTrafficState,'TnRmdAutoNegotiationConfigState':TnRmdAutoNegotiationConfigState,'tnRmdIfMibModule':tnRmdIfMibModule,'tnRmdIfObjects':tnRmdIfObjects,'tnRmdIfAttributeTotal':tnRmdIfAttributeTotal,'tnRmdSystemInterfacesTable':tnRmdSystemInterfacesTable,'tnRmdSystemInterfacesEntry':tnRmdSystemInterfacesEntry,'tnRmdSystemInterfacesFrameForwardingMode':tnRmdSystemInterfacesFrameForwardingMode,'tnRmdSystemLoopbackTable':tnRmdSystemLoopbackTable,'tnRmdSystemLoopbackEntry':tnRmdSystemLoopbackEntry,'tnRmdSystemDefaultLoopbackMode':tnRmdSystemDefaultLoopbackMode,'tnRmdIfTable':tnRmdIfTable,'tnRmdIfEntry':tnRmdIfEntry,_J:tnRmdIfIndex,'tnRmdIfType':tnRmdIfType,'tnRmdIfMacAddress':tnRmdIfMacAddress,'tnRmdIfTraffic':tnRmdIfTraffic,'tnRmdIfLinkPassThrough':tnRmdIfLinkPassThrough,'tnRmdIfLinkPassThroughStatus':tnRmdIfLinkPassThroughStatus,'tnRmdIfOperationalState':tnRmdIfOperationalState,'tnRmdIfMauTable':tnRmdIfMauTable,'tnRmdIfMauEntry':tnRmdIfMauEntry,_M:tnRmdIfMauIndex,'tnRmdIfMauAutoNegotiation':tnRmdIfMauAutoNegotiation,'tnRmdIfMauAutoNegotiationStatus':tnRmdIfMauAutoNegotiationStatus,'tnRmdIfMauAutoNegotiationFallback':tnRmdIfMauAutoNegotiationFallback,'tnRmdIfMauProvisionedSpeed':tnRmdIfMauProvisionedSpeed,'tnRmdIfMauProvisionedDuplexMode':tnRmdIfMauProvisionedDuplexMode,'tnRmdIfMauProvisionedPauseMode':tnRmdIfMauProvisionedPauseMode,'tnRmdIfMauProvisionedMasterSlaveRole':tnRmdIfMauProvisionedMasterSlaveRole,'tnRmdIfMauActualSpeed':tnRmdIfMauActualSpeed,'tnRmdIfMauActualDuplexMode':tnRmdIfMauActualDuplexMode,'tnRmdIfMauActualPauseMode':tnRmdIfMauActualPauseMode,'tnRmdIfMauActualMasterSlaveRole':tnRmdIfMauActualMasterSlaveRole,'tnRmdIfMauMdixMode':tnRmdIfMauMdixMode,'tnRmdIfMsaTable':tnRmdIfMsaTable,'tnRmdIfMsaEntry':tnRmdIfMsaEntry,'tnRmdIfMsaModuleVendorSerNo':tnRmdIfMsaModuleVendorSerNo,'tnRmdIfMsaModuleVendor':tnRmdIfMsaModuleVendor,'tnRmdIfMsaWavelength':tnRmdIfMsaWavelength,'tnRmdIfMsaModuleType':tnRmdIfMsaModuleType,'tnRmdIfMsaCLEI':tnRmdIfMsaCLEI,'tnRmdIfMsaUnitPartNum':tnRmdIfMsaUnitPartNum,'tnRmdIfMsaSWPartNum':tnRmdIfMsaSWPartNum,'tnRmdIfMsaFactoryID':tnRmdIfMsaFactoryID,'tnRmdIfMsaDate':tnRmdIfMsaDate,'tnRmdIfMsaExtraData':tnRmdIfMsaExtraData,'tnRmdIfMsaMaximumCaseTemperature':tnRmdIfMsaMaximumCaseTemperature,'tnRmdIfMsaInterchangeabilityMarking':tnRmdIfMsaInterchangeabilityMarking,'tnRmdIfMsaAcronymCode':tnRmdIfMsaAcronymCode,'tnRmdIfDdmTable':tnRmdIfDdmTable,'tnRmdIfDdmEntry':tnRmdIfDdmEntry,'tnRmdIfDdmTemperature':tnRmdIfDdmTemperature,'tnRmdIfDdmTempLowWarning':tnRmdIfDdmTempLowWarning,'tnRmdIfDdmTempLowAlarm':tnRmdIfDdmTempLowAlarm,'tnRmdIfDdmTempHiWarning':tnRmdIfDdmTempHiWarning,'tnRmdIfDdmTempHiAlarm':tnRmdIfDdmTempHiAlarm,'tnRmdIfDdmSupplyVoltage':tnRmdIfDdmSupplyVoltage,'tnRmdIfDdmSupplyVoltageLowWarning':tnRmdIfDdmSupplyVoltageLowWarning,'tnRmdIfDdmSupplyVoltageLowAlarm':tnRmdIfDdmSupplyVoltageLowAlarm,'tnRmdIfDdmSupplyVoltageHiWarning':tnRmdIfDdmSupplyVoltageHiWarning,'tnRmdIfDdmSupplyVoltageHiAlarm':tnRmdIfDdmSupplyVoltageHiAlarm,'tnRmdIfDdmTxBiasCurrent':tnRmdIfDdmTxBiasCurrent,'tnRmdIfDdmTxBiasCurrentLowWarning':tnRmdIfDdmTxBiasCurrentLowWarning,'tnRmdIfDdmTxBiasCurrentLowAlarm':tnRmdIfDdmTxBiasCurrentLowAlarm,'tnRmdIfDdmTxBiasCurrentHiWarning':tnRmdIfDdmTxBiasCurrentHiWarning,'tnRmdIfDdmTxBiasCurrentHiAlarm':tnRmdIfDdmTxBiasCurrentHiAlarm,'tnRmdIfDdmTxOutputPower':tnRmdIfDdmTxOutputPower,'tnRmdIfDdmTxOutputPowerLowWarning':tnRmdIfDdmTxOutputPowerLowWarning,'tnRmdIfDdmTxOutputPowerLowAlarm':tnRmdIfDdmTxOutputPowerLowAlarm,'tnRmdIfDdmTxOutputPowerHiWarning':tnRmdIfDdmTxOutputPowerHiWarning,'tnRmdIfDdmTxOutputPowerHiAlarm':tnRmdIfDdmTxOutputPowerHiAlarm,'tnRmdIfDdmRxOpticalPower':tnRmdIfDdmRxOpticalPower,'tnRmdIfDdmRxOpticalPowerLowWarning':tnRmdIfDdmRxOpticalPowerLowWarning,'tnRmdIfDdmRxOpticalPowerLowAlarm':tnRmdIfDdmRxOpticalPowerLowAlarm,'tnRmdIfDdmRxOpticalPowerHiWarning':tnRmdIfDdmRxOpticalPowerHiWarning,'tnRmdIfDdmRxOpticalPowerHiAlarm':tnRmdIfDdmRxOpticalPowerHiAlarm,'tnRmdIfDdmRxOpticalPowerType':tnRmdIfDdmRxOpticalPowerType,'tnRmdIfDdmExternallyCalibrated':tnRmdIfDdmExternallyCalibrated,'tnRmdIfDdmExtCalRxPower4':tnRmdIfDdmExtCalRxPower4,'tnRmdIfDdmExtCalRxPower3':tnRmdIfDdmExtCalRxPower3,'tnRmdIfDdmExtCalRxPower2':tnRmdIfDdmExtCalRxPower2,'tnRmdIfDdmExtCalRxPower1':tnRmdIfDdmExtCalRxPower1,'tnRmdIfDdmExtCalRxPower0':tnRmdIfDdmExtCalRxPower0,'tnRmdIfDdmExtCalTxLaserBiasSlope':tnRmdIfDdmExtCalTxLaserBiasSlope,'tnRmdIfDdmExtCalTxLaserBiasOffset':tnRmdIfDdmExtCalTxLaserBiasOffset,'tnRmdIfDdmExtCalTxPowerSlope':tnRmdIfDdmExtCalTxPowerSlope,'tnRmdIfDdmExtCalTxPowerOffset':tnRmdIfDdmExtCalTxPowerOffset,'tnRmdIfDdmExtCalTemperatureSlope':tnRmdIfDdmExtCalTemperatureSlope,'tnRmdIfDdmExtCalTemperatureOffset':tnRmdIfDdmExtCalTemperatureOffset,'tnRmdIfDdmExtCalVoltageSlope':tnRmdIfDdmExtCalVoltageSlope,'tnRmdIfDdmExtCalVoltageOffset':tnRmdIfDdmExtCalVoltageOffset,'tnRmdIfLoopbackTable':tnRmdIfLoopbackTable,'tnRmdIfLoopbackEntry':tnRmdIfLoopbackEntry,'tnRmdIfLoopbackIn':tnRmdIfLoopbackIn,'tnRmdIfLoopbackOut':tnRmdIfLoopbackOut,'tnRmdIfEvcLoopBack':tnRmdIfEvcLoopBack,'tnRmdIfEvcLoopBackVlanId':tnRmdIfEvcLoopBackVlanId,'tnRmdIfCountersTable':tnRmdIfCountersTable,'tnRmdIfCountersEntry':tnRmdIfCountersEntry,'tnRmdIfCountersRxNrCorrectFrames':tnRmdIfCountersRxNrCorrectFrames,'tnRmdIfCountersRxNrCorrectBytes':tnRmdIfCountersRxNrCorrectBytes,'tnRmdIfCountersRxNrErroredFcsFrames':tnRmdIfCountersRxNrErroredFcsFrames,'tnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames':tnRmdIfCountersRxNrLengthErrorOrOtherErrorFrames,'tnRmdIfCountersRxNrDiscardedFrames':tnRmdIfCountersRxNrDiscardedFrames,'tnRmdIfCountersRxNrDroppedQueueOverflowFrames':tnRmdIfCountersRxNrDroppedQueueOverflowFrames,'tnRmdIfCountersTxNrFrames':tnRmdIfCountersTxNrFrames,'tnRmdIfCountersTxNrBytes':tnRmdIfCountersTxNrBytes,'tnRmdIfCountersReset':tnRmdIfCountersReset})