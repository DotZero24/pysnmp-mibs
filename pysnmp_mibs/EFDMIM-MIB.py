_F='false'
_E='read-write'
_D='true'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_CommsDevice_ObjectIdentity=ObjectIdentity
commsDevice=_CommsDevice_ObjectIdentity((1,3,6,1,4,1,52,1))
_Subsystem_ObjectIdentity=ObjectIdentity
subsystem=_Subsystem_ObjectIdentity((1,3,6,1,4,1,52,1,6))
_Nb55_ObjectIdentity=ObjectIdentity
nb55=_Nb55_ObjectIdentity((1,3,6,1,4,1,52,1,6,4))
_Rev1_ObjectIdentity=ObjectIdentity
rev1=_Rev1_ObjectIdentity((1,3,6,1,4,1,52,1,6,4,1))
_EfdmimRingTable_Object=MibTable
efdmimRingTable=_EfdmimRingTable_Object((1,3,6,1,4,1,52,1,6,4,1,1))
if mibBuilder.loadTexts:efdmimRingTable.setStatus(_A)
_EfdmimRingEntry_Object=MibTableRow
efdmimRingEntry=_EfdmimRingEntry_Object((1,3,6,1,4,1,52,1,6,4,1,1,1))
if mibBuilder.loadTexts:efdmimRingEntry.setStatus(_A)
_EfdmimRingUpstreamMac_Type=OctetString
_EfdmimRingUpstreamMac_Object=MibTableColumn
efdmimRingUpstreamMac=_EfdmimRingUpstreamMac_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,1),_EfdmimRingUpstreamMac_Type())
efdmimRingUpstreamMac.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingUpstreamMac.setStatus(_A)
_EfdmimRingNodeClass_Type=Integer32
_EfdmimRingNodeClass_Object=MibTableColumn
efdmimRingNodeClass=_EfdmimRingNodeClass_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,2),_EfdmimRingNodeClass_Type())
efdmimRingNodeClass.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingNodeClass.setStatus(_A)
_EfdmimRingMacs_Type=Counter32
_EfdmimRingMacs_Object=MibTableColumn
efdmimRingMacs=_EfdmimRingMacs_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,3),_EfdmimRingMacs_Type())
efdmimRingMacs.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingMacs.setStatus(_A)
_EfdmimRingNonMasterPhys_Type=Integer32
_EfdmimRingNonMasterPhys_Object=MibTableColumn
efdmimRingNonMasterPhys=_EfdmimRingNonMasterPhys_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,4),_EfdmimRingNonMasterPhys_Type())
efdmimRingNonMasterPhys.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingNonMasterPhys.setStatus(_A)
_EfdmimRingMasterPhys_Type=Integer32
_EfdmimRingMasterPhys_Object=MibTableColumn
efdmimRingMasterPhys=_EfdmimRingMasterPhys_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,5),_EfdmimRingMasterPhys_Type())
efdmimRingMasterPhys.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingMasterPhys.setStatus(_A)
_EfdmimRingTopology_Type=Integer32
_EfdmimRingTopology_Object=MibTableColumn
efdmimRingTopology=_EfdmimRingTopology_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,6),_EfdmimRingTopology_Type())
efdmimRingTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingTopology.setStatus(_A)
_EfdmimRingDuplicate_Type=Integer32
_EfdmimRingDuplicate_Object=MibTableColumn
efdmimRingDuplicate=_EfdmimRingDuplicate_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,7),_EfdmimRingDuplicate_Type())
efdmimRingDuplicate.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingDuplicate.setStatus(_A)
_EfdmimRingMacAddress_Type=OctetString
_EfdmimRingMacAddress_Object=MibTableColumn
efdmimRingMacAddress=_EfdmimRingMacAddress_Object((1,3,6,1,4,1,52,1,6,4,1,1,1,8),_EfdmimRingMacAddress_Type())
efdmimRingMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingMacAddress.setStatus(_A)
_EfdmimBdgPortTable_Object=MibTable
efdmimBdgPortTable=_EfdmimBdgPortTable_Object((1,3,6,1,4,1,52,1,6,4,1,2))
if mibBuilder.loadTexts:efdmimBdgPortTable.setStatus(_A)
_EfdmimBdgPortEntry_Object=MibTableRow
efdmimBdgPortEntry=_EfdmimBdgPortEntry_Object((1,3,6,1,4,1,52,1,6,4,1,2,1))
if mibBuilder.loadTexts:efdmimBdgPortEntry.setStatus(_A)
_EfdmimBdgPortState_Type=OctetString
_EfdmimBdgPortState_Object=MibTableColumn
efdmimBdgPortState=_EfdmimBdgPortState_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,1),_EfdmimBdgPortState_Type())
efdmimBdgPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortState.setStatus('optional')
_EfdmimBdgPortReceivedPkts_Type=Integer32
_EfdmimBdgPortReceivedPkts_Object=MibTableColumn
efdmimBdgPortReceivedPkts=_EfdmimBdgPortReceivedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,2),_EfdmimBdgPortReceivedPkts_Type())
efdmimBdgPortReceivedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortReceivedPkts.setStatus(_A)
_EfdmimBdgPortFilteredPkts_Type=Integer32
_EfdmimBdgPortFilteredPkts_Object=MibTableColumn
efdmimBdgPortFilteredPkts=_EfdmimBdgPortFilteredPkts_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,3),_EfdmimBdgPortFilteredPkts_Type())
efdmimBdgPortFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortFilteredPkts.setStatus(_A)
_EfdmimBdgPortForwardedPkts_Type=Integer32
_EfdmimBdgPortForwardedPkts_Object=MibTableColumn
efdmimBdgPortForwardedPkts=_EfdmimBdgPortForwardedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,4),_EfdmimBdgPortForwardedPkts_Type())
efdmimBdgPortForwardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortForwardedPkts.setStatus(_A)
_EfdmimBdgPortTransmittedPkts_Type=Integer32
_EfdmimBdgPortTransmittedPkts_Object=MibScalar
efdmimBdgPortTransmittedPkts=_EfdmimBdgPortTransmittedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,5),_EfdmimBdgPortTransmittedPkts_Type())
efdmimBdgPortTransmittedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortTransmittedPkts.setStatus(_A)
_EfdmimBdgPortErrorPkts_Type=Integer32
_EfdmimBdgPortErrorPkts_Object=MibScalar
efdmimBdgPortErrorPkts=_EfdmimBdgPortErrorPkts_Object((1,3,6,1,4,1,52,1,6,4,1,2,1,6),_EfdmimBdgPortErrorPkts_Type())
efdmimBdgPortErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBdgPortErrorPkts.setStatus(_A)
_EfdmimPhyTable_Object=MibTable
efdmimPhyTable=_EfdmimPhyTable_Object((1,3,6,1,4,1,52,1,6,4,1,3))
if mibBuilder.loadTexts:efdmimPhyTable.setStatus(_A)
_EfdmimPhyEntry_Object=MibTableRow
efdmimPhyEntry=_EfdmimPhyEntry_Object((1,3,6,1,4,1,52,1,6,4,1,3,1))
if mibBuilder.loadTexts:efdmimPhyEntry.setStatus(_A)
_EfdmimPhyWithold_Type=Integer32
_EfdmimPhyWithold_Object=MibTableColumn
efdmimPhyWithold=_EfdmimPhyWithold_Object((1,3,6,1,4,1,52,1,6,4,1,3,1,1),_EfdmimPhyWithold_Type())
efdmimPhyWithold.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimPhyWithold.setStatus(_A)
_EfdmimDeviceStatus_Type=OctetString
_EfdmimDeviceStatus_Object=MibScalar
efdmimDeviceStatus=_EfdmimDeviceStatus_Object((1,3,6,1,4,1,52,1,6,4,1,20),_EfdmimDeviceStatus_Type())
efdmimDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceStatus.setStatus(_A)
_EfdmimDeviceBdgName_Type=OctetString
_EfdmimDeviceBdgName_Object=MibScalar
efdmimDeviceBdgName=_EfdmimDeviceBdgName_Object((1,3,6,1,4,1,52,1,6,4,1,21),_EfdmimDeviceBdgName_Type())
efdmimDeviceBdgName.setMaxAccess(_E)
if mibBuilder.loadTexts:efdmimDeviceBdgName.setStatus(_A)
_EfdmimDeviceType_Type=OctetString
_EfdmimDeviceType_Object=MibScalar
efdmimDeviceType=_EfdmimDeviceType_Object((1,3,6,1,4,1,52,1,6,4,1,22),_EfdmimDeviceType_Type())
efdmimDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceType.setStatus(_A)
_EfdmimDeviceVersion_Type=OctetString
_EfdmimDeviceVersion_Object=MibScalar
efdmimDeviceVersion=_EfdmimDeviceVersion_Object((1,3,6,1,4,1,52,1,6,4,1,23),_EfdmimDeviceVersion_Type())
efdmimDeviceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceVersion.setStatus(_A)
_EfdmimDeviceLocation_Type=OctetString
_EfdmimDeviceLocation_Object=MibScalar
efdmimDeviceLocation=_EfdmimDeviceLocation_Object((1,3,6,1,4,1,52,1,6,4,1,24),_EfdmimDeviceLocation_Type())
efdmimDeviceLocation.setMaxAccess(_E)
if mibBuilder.loadTexts:efdmimDeviceLocation.setStatus(_A)
_EfdmimDeviceUptime_Type=Counter32
_EfdmimDeviceUptime_Object=MibScalar
efdmimDeviceUptime=_EfdmimDeviceUptime_Object((1,3,6,1,4,1,52,1,6,4,1,25),_EfdmimDeviceUptime_Type())
efdmimDeviceUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceUptime.setStatus(_A)
class _EfdmimDeviceDisableBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_F,2)))
_EfdmimDeviceDisableBridge_Type.__name__=_C
_EfdmimDeviceDisableBridge_Object=MibScalar
efdmimDeviceDisableBridge=_EfdmimDeviceDisableBridge_Object((1,3,6,1,4,1,52,1,6,4,1,26),_EfdmimDeviceDisableBridge_Type())
efdmimDeviceDisableBridge.setMaxAccess(_E)
if mibBuilder.loadTexts:efdmimDeviceDisableBridge.setStatus(_A)
class _EfdmimDeviceResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_D,1))
_EfdmimDeviceResetCounters_Type.__name__=_C
_EfdmimDeviceResetCounters_Object=MibScalar
efdmimDeviceResetCounters=_EfdmimDeviceResetCounters_Object((1,3,6,1,4,1,52,1,6,4,1,27),_EfdmimDeviceResetCounters_Type())
efdmimDeviceResetCounters.setMaxAccess('write-only')
if mibBuilder.loadTexts:efdmimDeviceResetCounters.setStatus(_A)
_EfdmimDeviceSwitchSettings_Type=Integer32
_EfdmimDeviceSwitchSettings_Object=MibScalar
efdmimDeviceSwitchSettings=_EfdmimDeviceSwitchSettings_Object((1,3,6,1,4,1,52,1,6,4,1,28),_EfdmimDeviceSwitchSettings_Type())
efdmimDeviceSwitchSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceSwitchSettings.setStatus(_A)
_EfdmimDeviceReceivedPkts_Type=Integer32
_EfdmimDeviceReceivedPkts_Object=MibScalar
efdmimDeviceReceivedPkts=_EfdmimDeviceReceivedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,29),_EfdmimDeviceReceivedPkts_Type())
efdmimDeviceReceivedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceReceivedPkts.setStatus(_A)
_EfdmimDeviceFilteredPkts_Type=Integer32
_EfdmimDeviceFilteredPkts_Object=MibScalar
efdmimDeviceFilteredPkts=_EfdmimDeviceFilteredPkts_Object((1,3,6,1,4,1,52,1,6,4,1,30),_EfdmimDeviceFilteredPkts_Type())
efdmimDeviceFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceFilteredPkts.setStatus(_A)
_EfdmimDeviceForwardedPkts_Type=Integer32
_EfdmimDeviceForwardedPkts_Object=MibScalar
efdmimDeviceForwardedPkts=_EfdmimDeviceForwardedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,31),_EfdmimDeviceForwardedPkts_Type())
efdmimDeviceForwardedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceForwardedPkts.setStatus(_A)
_EfdmimDeviceTransmittedPkts_Type=Integer32
_EfdmimDeviceTransmittedPkts_Object=MibScalar
efdmimDeviceTransmittedPkts=_EfdmimDeviceTransmittedPkts_Object((1,3,6,1,4,1,52,1,6,4,1,32),_EfdmimDeviceTransmittedPkts_Type())
efdmimDeviceTransmittedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceTransmittedPkts.setStatus(_A)
_EfdmimDeviceErrorPkts_Type=Integer32
_EfdmimDeviceErrorPkts_Object=MibScalar
efdmimDeviceErrorPkts=_EfdmimDeviceErrorPkts_Object((1,3,6,1,4,1,52,1,6,4,1,33),_EfdmimDeviceErrorPkts_Type())
efdmimDeviceErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceErrorPkts.setStatus(_A)
_EfdmimCfmState_Type=Integer32
_EfdmimCfmState_Object=MibScalar
efdmimCfmState=_EfdmimCfmState_Object((1,3,6,1,4,1,52,1,6,4,1,34),_EfdmimCfmState_Type())
efdmimCfmState.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimCfmState.setStatus(_A)
class _EfdmimBypassAttached_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_F,2)))
_EfdmimBypassAttached_Type.__name__=_C
_EfdmimBypassAttached_Object=MibScalar
efdmimBypassAttached=_EfdmimBypassAttached_Object((1,3,6,1,4,1,52,1,6,4,1,35),_EfdmimBypassAttached_Type())
efdmimBypassAttached.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBypassAttached.setStatus(_A)
_EfdmimOscillations_Type=Counter32
_EfdmimOscillations_Object=MibScalar
efdmimOscillations=_EfdmimOscillations_Object((1,3,6,1,4,1,52,1,6,4,1,36),_EfdmimOscillations_Type())
efdmimOscillations.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimOscillations.setStatus(_A)
_EfdmimRingUpTime_Type=Counter32
_EfdmimRingUpTime_Object=MibScalar
efdmimRingUpTime=_EfdmimRingUpTime_Object((1,3,6,1,4,1,52,1,6,4,1,37),_EfdmimRingUpTime_Type())
efdmimRingUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRingUpTime.setStatus(_A)
_EfdmimDownstreamMac_Type=OctetString
_EfdmimDownstreamMac_Object=MibScalar
efdmimDownstreamMac=_EfdmimDownstreamMac_Object((1,3,6,1,4,1,52,1,6,4,1,38),_EfdmimDownstreamMac_Type())
efdmimDownstreamMac.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDownstreamMac.setStatus(_A)
class _EfdmimBypassStuck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_F,2)))
_EfdmimBypassStuck_Type.__name__=_C
_EfdmimBypassStuck_Object=MibScalar
efdmimBypassStuck=_EfdmimBypassStuck_Object((1,3,6,1,4,1,52,1,6,4,1,39),_EfdmimBypassStuck_Type())
efdmimBypassStuck.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimBypassStuck.setStatus(_A)
class _EfdmimMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('encapsulation',1),('translation',2)))
_EfdmimMode_Type.__name__=_C
_EfdmimMode_Object=MibScalar
efdmimMode=_EfdmimMode_Object((1,3,6,1,4,1,52,1,6,4,1,40),_EfdmimMode_Type())
efdmimMode.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimMode.setStatus(_A)
_EfdmimRmtState_Type=Integer32
_EfdmimRmtState_Object=MibScalar
efdmimRmtState=_EfdmimRmtState_Object((1,3,6,1,4,1,52,1,6,4,1,41),_EfdmimRmtState_Type())
efdmimRmtState.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimRmtState.setStatus(_A)
_EfdmimDeviceBridgeAddr_Type=OctetString
_EfdmimDeviceBridgeAddr_Object=MibScalar
efdmimDeviceBridgeAddr=_EfdmimDeviceBridgeAddr_Object((1,3,6,1,4,1,52,1,6,4,1,42),_EfdmimDeviceBridgeAddr_Type())
efdmimDeviceBridgeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:efdmimDeviceBridgeAddr.setStatus(_A)
mibBuilder.exportSymbols('EFDMIM-MIB',**{'cabletron':cabletron,'commsDevice':commsDevice,'subsystem':subsystem,'nb55':nb55,'rev1':rev1,'efdmimRingTable':efdmimRingTable,'efdmimRingEntry':efdmimRingEntry,'efdmimRingUpstreamMac':efdmimRingUpstreamMac,'efdmimRingNodeClass':efdmimRingNodeClass,'efdmimRingMacs':efdmimRingMacs,'efdmimRingNonMasterPhys':efdmimRingNonMasterPhys,'efdmimRingMasterPhys':efdmimRingMasterPhys,'efdmimRingTopology':efdmimRingTopology,'efdmimRingDuplicate':efdmimRingDuplicate,'efdmimRingMacAddress':efdmimRingMacAddress,'efdmimBdgPortTable':efdmimBdgPortTable,'efdmimBdgPortEntry':efdmimBdgPortEntry,'efdmimBdgPortState':efdmimBdgPortState,'efdmimBdgPortReceivedPkts':efdmimBdgPortReceivedPkts,'efdmimBdgPortFilteredPkts':efdmimBdgPortFilteredPkts,'efdmimBdgPortForwardedPkts':efdmimBdgPortForwardedPkts,'efdmimBdgPortTransmittedPkts':efdmimBdgPortTransmittedPkts,'efdmimBdgPortErrorPkts':efdmimBdgPortErrorPkts,'efdmimPhyTable':efdmimPhyTable,'efdmimPhyEntry':efdmimPhyEntry,'efdmimPhyWithold':efdmimPhyWithold,'efdmimDeviceStatus':efdmimDeviceStatus,'efdmimDeviceBdgName':efdmimDeviceBdgName,'efdmimDeviceType':efdmimDeviceType,'efdmimDeviceVersion':efdmimDeviceVersion,'efdmimDeviceLocation':efdmimDeviceLocation,'efdmimDeviceUptime':efdmimDeviceUptime,'efdmimDeviceDisableBridge':efdmimDeviceDisableBridge,'efdmimDeviceResetCounters':efdmimDeviceResetCounters,'efdmimDeviceSwitchSettings':efdmimDeviceSwitchSettings,'efdmimDeviceReceivedPkts':efdmimDeviceReceivedPkts,'efdmimDeviceFilteredPkts':efdmimDeviceFilteredPkts,'efdmimDeviceForwardedPkts':efdmimDeviceForwardedPkts,'efdmimDeviceTransmittedPkts':efdmimDeviceTransmittedPkts,'efdmimDeviceErrorPkts':efdmimDeviceErrorPkts,'efdmimCfmState':efdmimCfmState,'efdmimBypassAttached':efdmimBypassAttached,'efdmimOscillations':efdmimOscillations,'efdmimRingUpTime':efdmimRingUpTime,'efdmimDownstreamMac':efdmimDownstreamMac,'efdmimBypassStuck':efdmimBypassStuck,'efdmimMode':efdmimMode,'efdmimRmtState':efdmimRmtState,'efdmimDeviceBridgeAddr':efdmimDeviceBridgeAddr})