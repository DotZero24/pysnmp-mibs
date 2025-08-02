_S='pppLCPExtensionsEntry'
_R='not-accessible'
_Q='pppAuthId'
_P='pppAuthSubId'
_O='seconds'
_N='Unsigned32'
_M='AtmVpIdentifier'
_L='AtmVcIdentifier'
_K='ZhoneAuthenticationProtocol'
_J='ifIndex'
_I='InterfaceIndexOrZero'
_H='IF-MIB'
_G='ZHONE-COM-PPP-MIB'
_F='read-write'
_E='OctetString'
_D='EnableFlag'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB',_L,_M)
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneModules,zhonePpp=mibBuilder.importSymbols('Zhone','zhoneModules','zhonePpp')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comPpp=ModuleIdentity((1,3,6,1,4,1,5504,6,69))
if mibBuilder.loadTexts:comPpp.setRevisions(('2001-06-06 16:00','2001-04-19 15:00','2001-03-20 09:30','2001-03-12 11:00','2001-03-01 11:00','2001-02-08 10:02'))
class ZhoneAuthenticationProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pap',1),('chap',2)))
class EnableFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_PppInterfaceTable_Object=MibTable
pppInterfaceTable=_PppInterfaceTable_Object((1,3,6,1,4,1,5504,4,5,1))
if mibBuilder.loadTexts:pppInterfaceTable.setStatus(_A)
_PppInterfaceEntry_Object=MibTableRow
pppInterfaceEntry=_PppInterfaceEntry_Object((1,3,6,1,4,1,5504,4,5,1,1))
pppInterfaceEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:pppInterfaceEntry.setStatus(_A)
_PppIfLowerIfIndex_Type=InterfaceIndex
_PppIfLowerIfIndex_Object=MibTableColumn
pppIfLowerIfIndex=_PppIfLowerIfIndex_Object((1,3,6,1,4,1,5504,4,5,1,1,1),_PppIfLowerIfIndex_Type())
pppIfLowerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfLowerIfIndex.setStatus(_A)
class _PppIfVpi_Type(AtmVpIdentifier):defaultValue=0
_PppIfVpi_Type.__name__=_M
_PppIfVpi_Object=MibTableColumn
pppIfVpi=_PppIfVpi_Object((1,3,6,1,4,1,5504,4,5,1,1,2),_PppIfVpi_Type())
pppIfVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfVpi.setStatus(_A)
class _PppIfVci_Type(AtmVcIdentifier):defaultValue=0
_PppIfVci_Type.__name__=_L
_PppIfVci_Object=MibTableColumn
pppIfVci=_PppIfVci_Object((1,3,6,1,4,1,5504,4,5,1,1,3),_PppIfVci_Type())
pppIfVci.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfVci.setStatus(_A)
class _PppIfCallMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCall',1),('inCall',2),('outCall',3)))
_PppIfCallMode_Type.__name__=_C
_PppIfCallMode_Object=MibTableColumn
pppIfCallMode=_PppIfCallMode_Object((1,3,6,1,4,1,5504,4,5,1,1,4),_PppIfCallMode_Type())
pppIfCallMode.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfCallMode.setStatus(_A)
class _PppIfFrameType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('frameRelay',2),('atmLLC',3),('atmVc',4)))
_PppIfFrameType_Type.__name__=_C
_PppIfFrameType_Object=MibTableColumn
pppIfFrameType=_PppIfFrameType_Object((1,3,6,1,4,1,5504,4,5,1,1,5),_PppIfFrameType_Type())
pppIfFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfFrameType.setStatus(_A)
class _PppIfNumChannels_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PppIfNumChannels_Type.__name__=_C
_PppIfNumChannels_Object=MibTableColumn
pppIfNumChannels=_PppIfNumChannels_Object((1,3,6,1,4,1,5504,4,5,1,1,6),_PppIfNumChannels_Type())
pppIfNumChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfNumChannels.setStatus(_A)
_PppIfRowStatus_Type=ZhoneRowStatus
_PppIfRowStatus_Object=MibTableColumn
pppIfRowStatus=_PppIfRowStatus_Object((1,3,6,1,4,1,5504,4,5,1,1,7),_PppIfRowStatus_Type())
pppIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIfRowStatus.setStatus(_A)
_PppLCPExtensionsTable_Object=MibTable
pppLCPExtensionsTable=_PppLCPExtensionsTable_Object((1,3,6,1,4,1,5504,4,5,2))
if mibBuilder.loadTexts:pppLCPExtensionsTable.setStatus(_A)
_PppLCPExtensionsEntry_Object=MibTableRow
pppLCPExtensionsEntry=_PppLCPExtensionsEntry_Object((1,3,6,1,4,1,5504,4,5,2,1))
if mibBuilder.loadTexts:pppLCPExtensionsEntry.setStatus(_A)
class _LcpExtReceiveAuthEnable_Type(EnableFlag):defaultValue=1
_LcpExtReceiveAuthEnable_Type.__name__=_D
_LcpExtReceiveAuthEnable_Object=MibTableColumn
lcpExtReceiveAuthEnable=_LcpExtReceiveAuthEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,1),_LcpExtReceiveAuthEnable_Type())
lcpExtReceiveAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtReceiveAuthEnable.setStatus(_A)
class _LcpExtReceiveAuthProtocol_Type(ZhoneAuthenticationProtocol):defaultValue=1
_LcpExtReceiveAuthProtocol_Type.__name__=_K
_LcpExtReceiveAuthProtocol_Object=MibTableColumn
lcpExtReceiveAuthProtocol=_LcpExtReceiveAuthProtocol_Object((1,3,6,1,4,1,5504,4,5,2,1,2),_LcpExtReceiveAuthProtocol_Type())
lcpExtReceiveAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtReceiveAuthProtocol.setStatus(_A)
class _LcpExtSendAuthEnable_Type(EnableFlag):defaultValue=2
_LcpExtSendAuthEnable_Type.__name__=_D
_LcpExtSendAuthEnable_Object=MibTableColumn
lcpExtSendAuthEnable=_LcpExtSendAuthEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,3),_LcpExtSendAuthEnable_Type())
lcpExtSendAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtSendAuthEnable.setStatus(_A)
class _LcpExtSendAuthProtocol_Type(ZhoneAuthenticationProtocol):defaultValue=1
_LcpExtSendAuthProtocol_Type.__name__=_K
_LcpExtSendAuthProtocol_Object=MibTableColumn
lcpExtSendAuthProtocol=_LcpExtSendAuthProtocol_Object((1,3,6,1,4,1,5504,4,5,2,1,4),_LcpExtSendAuthProtocol_Type())
lcpExtSendAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtSendAuthProtocol.setStatus(_A)
class _LcpExtSendAuthIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_LcpExtSendAuthIdentity_Type.__name__=_E
_LcpExtSendAuthIdentity_Object=MibTableColumn
lcpExtSendAuthIdentity=_LcpExtSendAuthIdentity_Object((1,3,6,1,4,1,5504,4,5,2,1,5),_LcpExtSendAuthIdentity_Type())
lcpExtSendAuthIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtSendAuthIdentity.setStatus(_A)
class _LcpExtQualityProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('lqr',1))
_LcpExtQualityProtocol_Type.__name__=_C
_LcpExtQualityProtocol_Object=MibTableColumn
lcpExtQualityProtocol=_LcpExtQualityProtocol_Object((1,3,6,1,4,1,5504,4,5,2,1,6),_LcpExtQualityProtocol_Type())
lcpExtQualityProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtQualityProtocol.setStatus(_A)
class _LcpExtMagicNumber_Type(Unsigned32):defaultValue=0
_LcpExtMagicNumber_Type.__name__=_N
_LcpExtMagicNumber_Object=MibTableColumn
lcpExtMagicNumber=_LcpExtMagicNumber_Object((1,3,6,1,4,1,5504,4,5,2,1,7),_LcpExtMagicNumber_Type())
lcpExtMagicNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMagicNumber.setStatus(_A)
class _LcpExtMaxPad_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LcpExtMaxPad_Type.__name__=_C
_LcpExtMaxPad_Object=MibTableColumn
lcpExtMaxPad=_LcpExtMaxPad_Object((1,3,6,1,4,1,5504,4,5,2,1,8),_LcpExtMaxPad_Type())
lcpExtMaxPad.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMaxPad.setStatus(_A)
class _LcpExtCallbackEnable_Type(EnableFlag):defaultValue=2
_LcpExtCallbackEnable_Type.__name__=_D
_LcpExtCallbackEnable_Object=MibTableColumn
lcpExtCallbackEnable=_LcpExtCallbackEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,9),_LcpExtCallbackEnable_Type())
lcpExtCallbackEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtCallbackEnable.setStatus(_A)
class _LcpExtCallbackType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('byAuth',1),('byDialStr',2),('byIdentifier',3),('byE164',4),('byName',5)))
_LcpExtCallbackType_Type.__name__=_C
_LcpExtCallbackType_Object=MibTableColumn
lcpExtCallbackType=_LcpExtCallbackType_Object((1,3,6,1,4,1,5504,4,5,2,1,10),_LcpExtCallbackType_Type())
lcpExtCallbackType.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtCallbackType.setStatus(_A)
class _LcpExtCallbackDialString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_LcpExtCallbackDialString_Type.__name__=_E
_LcpExtCallbackDialString_Object=MibTableColumn
lcpExtCallbackDialString=_LcpExtCallbackDialString_Object((1,3,6,1,4,1,5504,4,5,2,1,11),_LcpExtCallbackDialString_Type())
lcpExtCallbackDialString.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtCallbackDialString.setStatus(_A)
class _LcpExtRestartTimer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_LcpExtRestartTimer_Type.__name__=_C
_LcpExtRestartTimer_Object=MibTableColumn
lcpExtRestartTimer=_LcpExtRestartTimer_Object((1,3,6,1,4,1,5504,4,5,2,1,12),_LcpExtRestartTimer_Type())
lcpExtRestartTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtRestartTimer.setStatus(_A)
if mibBuilder.loadTexts:lcpExtRestartTimer.setUnits(_O)
class _LcpExtMaxConfigRetries_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_LcpExtMaxConfigRetries_Type.__name__=_C
_LcpExtMaxConfigRetries_Object=MibTableColumn
lcpExtMaxConfigRetries=_LcpExtMaxConfigRetries_Object((1,3,6,1,4,1,5504,4,5,2,1,13),_LcpExtMaxConfigRetries_Type())
lcpExtMaxConfigRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMaxConfigRetries.setStatus(_A)
class _LcpExtMaxTerminateRetries_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_LcpExtMaxTerminateRetries_Type.__name__=_C
_LcpExtMaxTerminateRetries_Object=MibTableColumn
lcpExtMaxTerminateRetries=_LcpExtMaxTerminateRetries_Object((1,3,6,1,4,1,5504,4,5,2,1,14),_LcpExtMaxTerminateRetries_Type())
lcpExtMaxTerminateRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMaxTerminateRetries.setStatus(_A)
class _LcpExtMaxFailureRetries_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_LcpExtMaxFailureRetries_Type.__name__=_C
_LcpExtMaxFailureRetries_Object=MibTableColumn
lcpExtMaxFailureRetries=_LcpExtMaxFailureRetries_Object((1,3,6,1,4,1,5504,4,5,2,1,15),_LcpExtMaxFailureRetries_Type())
lcpExtMaxFailureRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMaxFailureRetries.setStatus(_A)
class _LcpExtMRUEnable_Type(EnableFlag):defaultValue=1
_LcpExtMRUEnable_Type.__name__=_D
_LcpExtMRUEnable_Object=MibTableColumn
lcpExtMRUEnable=_LcpExtMRUEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,16),_LcpExtMRUEnable_Type())
lcpExtMRUEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtMRUEnable.setStatus(_A)
class _LcpExtACCMEnable_Type(EnableFlag):defaultValue=2
_LcpExtACCMEnable_Type.__name__=_D
_LcpExtACCMEnable_Object=MibTableColumn
lcpExtACCMEnable=_LcpExtACCMEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,17),_LcpExtACCMEnable_Type())
lcpExtACCMEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtACCMEnable.setStatus(_A)
class _LcpExtPFCEnable_Type(EnableFlag):defaultValue=2
_LcpExtPFCEnable_Type.__name__=_D
_LcpExtPFCEnable_Object=MibTableColumn
lcpExtPFCEnable=_LcpExtPFCEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,18),_LcpExtPFCEnable_Type())
lcpExtPFCEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtPFCEnable.setStatus(_A)
class _LcpExtACFCEnable_Type(EnableFlag):defaultValue=2
_LcpExtACFCEnable_Type.__name__=_D
_LcpExtACFCEnable_Object=MibTableColumn
lcpExtACFCEnable=_LcpExtACFCEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,19),_LcpExtACFCEnable_Type())
lcpExtACFCEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtACFCEnable.setStatus(_A)
class _LcpExtFCSAltEnable_Type(EnableFlag):defaultValue=2
_LcpExtFCSAltEnable_Type.__name__=_D
_LcpExtFCSAltEnable_Object=MibTableColumn
lcpExtFCSAltEnable=_LcpExtFCSAltEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,20),_LcpExtFCSAltEnable_Type())
lcpExtFCSAltEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtFCSAltEnable.setStatus(_A)
class _LcpExtSDPEnable_Type(EnableFlag):defaultValue=2
_LcpExtSDPEnable_Type.__name__=_D
_LcpExtSDPEnable_Object=MibTableColumn
lcpExtSDPEnable=_LcpExtSDPEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,21),_LcpExtSDPEnable_Type())
lcpExtSDPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtSDPEnable.setStatus(_A)
class _LcpExtNumModeEnable_Type(EnableFlag):defaultValue=2
_LcpExtNumModeEnable_Type.__name__=_D
_LcpExtNumModeEnable_Object=MibTableColumn
lcpExtNumModeEnable=_LcpExtNumModeEnable_Object((1,3,6,1,4,1,5504,4,5,2,1,22),_LcpExtNumModeEnable_Type())
lcpExtNumModeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:lcpExtNumModeEnable.setStatus(_A)
_PppNCPExtensionsTable_Object=MibTable
pppNCPExtensionsTable=_PppNCPExtensionsTable_Object((1,3,6,1,4,1,5504,4,5,3))
if mibBuilder.loadTexts:pppNCPExtensionsTable.setStatus(_A)
_PppNCPExtensionsEntry_Object=MibTableRow
pppNCPExtensionsEntry=_PppNCPExtensionsEntry_Object((1,3,6,1,4,1,5504,4,5,3,1))
pppNCPExtensionsEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:pppNCPExtensionsEntry.setStatus(_A)
class _NcpExtVJCompMaxSlotID_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_NcpExtVJCompMaxSlotID_Type.__name__=_C
_NcpExtVJCompMaxSlotID_Object=MibTableColumn
ncpExtVJCompMaxSlotID=_NcpExtVJCompMaxSlotID_Object((1,3,6,1,4,1,5504,4,5,3,1,1),_NcpExtVJCompMaxSlotID_Type())
ncpExtVJCompMaxSlotID.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtVJCompMaxSlotID.setStatus(_A)
class _NcpExtVJCompSlotID_Type(EnableFlag):defaultValue=2
_NcpExtVJCompSlotID_Type.__name__=_D
_NcpExtVJCompSlotID_Object=MibTableColumn
ncpExtVJCompSlotID=_NcpExtVJCompSlotID_Object((1,3,6,1,4,1,5504,4,5,3,1,2),_NcpExtVJCompSlotID_Type())
ncpExtVJCompSlotID.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtVJCompSlotID.setStatus(_A)
class _NcpExtIpAddrOptionEnable_Type(EnableFlag):defaultValue=2
_NcpExtIpAddrOptionEnable_Type.__name__=_D
_NcpExtIpAddrOptionEnable_Object=MibTableColumn
ncpExtIpAddrOptionEnable=_NcpExtIpAddrOptionEnable_Object((1,3,6,1,4,1,5504,4,5,3,1,3),_NcpExtIpAddrOptionEnable_Type())
ncpExtIpAddrOptionEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtIpAddrOptionEnable.setStatus(_A)
class _NcpExtRestartTimer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_NcpExtRestartTimer_Type.__name__=_C
_NcpExtRestartTimer_Object=MibTableColumn
ncpExtRestartTimer=_NcpExtRestartTimer_Object((1,3,6,1,4,1,5504,4,5,3,1,4),_NcpExtRestartTimer_Type())
ncpExtRestartTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtRestartTimer.setStatus(_A)
if mibBuilder.loadTexts:ncpExtRestartTimer.setUnits(_O)
class _NcpExtMaxConfigRetries_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_NcpExtMaxConfigRetries_Type.__name__=_C
_NcpExtMaxConfigRetries_Object=MibTableColumn
ncpExtMaxConfigRetries=_NcpExtMaxConfigRetries_Object((1,3,6,1,4,1,5504,4,5,3,1,5),_NcpExtMaxConfigRetries_Type())
ncpExtMaxConfigRetries.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtMaxConfigRetries.setStatus(_A)
class _NcpExtMaxTerminateRetries_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_NcpExtMaxTerminateRetries_Type.__name__=_C
_NcpExtMaxTerminateRetries_Object=MibTableColumn
ncpExtMaxTerminateRetries=_NcpExtMaxTerminateRetries_Object((1,3,6,1,4,1,5504,4,5,3,1,6),_NcpExtMaxTerminateRetries_Type())
ncpExtMaxTerminateRetries.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtMaxTerminateRetries.setStatus(_A)
class _NcpExtFailureRetries_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_NcpExtFailureRetries_Type.__name__=_C
_NcpExtFailureRetries_Object=MibTableColumn
ncpExtFailureRetries=_NcpExtFailureRetries_Object((1,3,6,1,4,1,5504,4,5,3,1,7),_NcpExtFailureRetries_Type())
ncpExtFailureRetries.setMaxAccess(_F)
if mibBuilder.loadTexts:ncpExtFailureRetries.setStatus(_A)
class _PppNextAuthId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppNextAuthId_Type.__name__=_C
_PppNextAuthId_Object=MibScalar
pppNextAuthId=_PppNextAuthId_Object((1,3,6,1,4,1,5504,4,5,4),_PppNextAuthId_Type())
pppNextAuthId.setMaxAccess('read-only')
if mibBuilder.loadTexts:pppNextAuthId.setStatus(_A)
_PppAuthenticationTable_Object=MibTable
pppAuthenticationTable=_PppAuthenticationTable_Object((1,3,6,1,4,1,5504,4,5,5))
if mibBuilder.loadTexts:pppAuthenticationTable.setStatus(_A)
_PppAuthenticationEntry_Object=MibTableRow
pppAuthenticationEntry=_PppAuthenticationEntry_Object((1,3,6,1,4,1,5504,4,5,5,1))
pppAuthenticationEntry.setIndexNames((0,_G,_P),(0,_G,_Q))
if mibBuilder.loadTexts:pppAuthenticationEntry.setStatus(_A)
class _PppAuthSubId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PppAuthSubId_Type.__name__=_C
_PppAuthSubId_Object=MibTableColumn
pppAuthSubId=_PppAuthSubId_Object((1,3,6,1,4,1,5504,4,5,5,1,1),_PppAuthSubId_Type())
pppAuthSubId.setMaxAccess(_R)
if mibBuilder.loadTexts:pppAuthSubId.setStatus(_A)
class _PppAuthId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PppAuthId_Type.__name__=_C
_PppAuthId_Object=MibTableColumn
pppAuthId=_PppAuthId_Object((1,3,6,1,4,1,5504,4,5,5,1,2),_PppAuthId_Type())
pppAuthId.setMaxAccess(_R)
if mibBuilder.loadTexts:pppAuthId.setStatus(_A)
class _PppAuthIpIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_PppAuthIpIfIndex_Type.__name__=_I
_PppAuthIpIfIndex_Object=MibTableColumn
pppAuthIpIfIndex=_PppAuthIpIfIndex_Object((1,3,6,1,4,1,5504,4,5,5,1,3),_PppAuthIpIfIndex_Type())
pppAuthIpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthIpIfIndex.setStatus(_A)
class _PppAuthLgId_Type(InterfaceIndexOrZero):defaultValue=0
_PppAuthLgId_Type.__name__=_I
_PppAuthLgId_Object=MibTableColumn
pppAuthLgId=_PppAuthLgId_Object((1,3,6,1,4,1,5504,4,5,5,1,4),_PppAuthLgId_Type())
pppAuthLgId.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthLgId.setStatus(_A)
class _PppAuthProtocol_Type(Bits):namedValues=NamedValues(*(('pap',0),('chap',1)))
_PppAuthProtocol_Type.__name__='Bits'
_PppAuthProtocol_Object=MibTableColumn
pppAuthProtocol=_PppAuthProtocol_Object((1,3,6,1,4,1,5504,4,5,5,1,5),_PppAuthProtocol_Type())
pppAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthProtocol.setStatus(_A)
class _PppAuthPAPPeerID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_PppAuthPAPPeerID_Type.__name__=_E
_PppAuthPAPPeerID_Object=MibTableColumn
pppAuthPAPPeerID=_PppAuthPAPPeerID_Object((1,3,6,1,4,1,5504,4,5,5,1,6),_PppAuthPAPPeerID_Type())
pppAuthPAPPeerID.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthPAPPeerID.setStatus(_A)
class _PppAuthPAPPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_PppAuthPAPPassword_Type.__name__=_E
_PppAuthPAPPassword_Object=MibTableColumn
pppAuthPAPPassword=_PppAuthPAPPassword_Object((1,3,6,1,4,1,5504,4,5,5,1,7),_PppAuthPAPPassword_Type())
pppAuthPAPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthPAPPassword.setStatus(_A)
class _PppAuthCHAPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_PppAuthCHAPName_Type.__name__=_E
_PppAuthCHAPName_Object=MibTableColumn
pppAuthCHAPName=_PppAuthCHAPName_Object((1,3,6,1,4,1,5504,4,5,5,1,8),_PppAuthCHAPName_Type())
pppAuthCHAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthCHAPName.setStatus(_A)
class _PppAuthCHAPSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_PppAuthCHAPSecret_Type.__name__=_E
_PppAuthCHAPSecret_Object=MibTableColumn
pppAuthCHAPSecret=_PppAuthCHAPSecret_Object((1,3,6,1,4,1,5504,4,5,5,1,9),_PppAuthCHAPSecret_Type())
pppAuthCHAPSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthCHAPSecret.setStatus(_A)
class _PppAuthStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_PppAuthStatus_Type.__name__=_C
_PppAuthStatus_Object=MibTableColumn
pppAuthStatus=_PppAuthStatus_Object((1,3,6,1,4,1,5504,4,5,5,1,10),_PppAuthStatus_Type())
pppAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthStatus.setStatus(_A)
_PppAuthRowStatus_Type=ZhoneRowStatus
_PppAuthRowStatus_Object=MibTableColumn
pppAuthRowStatus=_PppAuthRowStatus_Object((1,3,6,1,4,1,5504,4,5,5,1,12),_PppAuthRowStatus_Type())
pppAuthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthRowStatus.setStatus(_A)
pppInterfaceEntry.registerAugmentions((_G,_S))
pppLCPExtensionsEntry.setIndexNames(*pppInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{_K:ZhoneAuthenticationProtocol,_D:EnableFlag,'pppInterfaceTable':pppInterfaceTable,'pppInterfaceEntry':pppInterfaceEntry,'pppIfLowerIfIndex':pppIfLowerIfIndex,'pppIfVpi':pppIfVpi,'pppIfVci':pppIfVci,'pppIfCallMode':pppIfCallMode,'pppIfFrameType':pppIfFrameType,'pppIfNumChannels':pppIfNumChannels,'pppIfRowStatus':pppIfRowStatus,'pppLCPExtensionsTable':pppLCPExtensionsTable,_S:pppLCPExtensionsEntry,'lcpExtReceiveAuthEnable':lcpExtReceiveAuthEnable,'lcpExtReceiveAuthProtocol':lcpExtReceiveAuthProtocol,'lcpExtSendAuthEnable':lcpExtSendAuthEnable,'lcpExtSendAuthProtocol':lcpExtSendAuthProtocol,'lcpExtSendAuthIdentity':lcpExtSendAuthIdentity,'lcpExtQualityProtocol':lcpExtQualityProtocol,'lcpExtMagicNumber':lcpExtMagicNumber,'lcpExtMaxPad':lcpExtMaxPad,'lcpExtCallbackEnable':lcpExtCallbackEnable,'lcpExtCallbackType':lcpExtCallbackType,'lcpExtCallbackDialString':lcpExtCallbackDialString,'lcpExtRestartTimer':lcpExtRestartTimer,'lcpExtMaxConfigRetries':lcpExtMaxConfigRetries,'lcpExtMaxTerminateRetries':lcpExtMaxTerminateRetries,'lcpExtMaxFailureRetries':lcpExtMaxFailureRetries,'lcpExtMRUEnable':lcpExtMRUEnable,'lcpExtACCMEnable':lcpExtACCMEnable,'lcpExtPFCEnable':lcpExtPFCEnable,'lcpExtACFCEnable':lcpExtACFCEnable,'lcpExtFCSAltEnable':lcpExtFCSAltEnable,'lcpExtSDPEnable':lcpExtSDPEnable,'lcpExtNumModeEnable':lcpExtNumModeEnable,'pppNCPExtensionsTable':pppNCPExtensionsTable,'pppNCPExtensionsEntry':pppNCPExtensionsEntry,'ncpExtVJCompMaxSlotID':ncpExtVJCompMaxSlotID,'ncpExtVJCompSlotID':ncpExtVJCompSlotID,'ncpExtIpAddrOptionEnable':ncpExtIpAddrOptionEnable,'ncpExtRestartTimer':ncpExtRestartTimer,'ncpExtMaxConfigRetries':ncpExtMaxConfigRetries,'ncpExtMaxTerminateRetries':ncpExtMaxTerminateRetries,'ncpExtFailureRetries':ncpExtFailureRetries,'pppNextAuthId':pppNextAuthId,'pppAuthenticationTable':pppAuthenticationTable,'pppAuthenticationEntry':pppAuthenticationEntry,_P:pppAuthSubId,_Q:pppAuthId,'pppAuthIpIfIndex':pppAuthIpIfIndex,'pppAuthLgId':pppAuthLgId,'pppAuthProtocol':pppAuthProtocol,'pppAuthPAPPeerID':pppAuthPAPPeerID,'pppAuthPAPPassword':pppAuthPAPPassword,'pppAuthCHAPName':pppAuthCHAPName,'pppAuthCHAPSecret':pppAuthCHAPSecret,'pppAuthStatus':pppAuthStatus,'pppAuthRowStatus':pppAuthRowStatus,'comPpp':comPpp})